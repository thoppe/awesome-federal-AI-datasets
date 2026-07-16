"""Deterministic validation for the legacy federal-dataset catalog."""

from __future__ import annotations

import argparse
import csv
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATASETS = ROOT / "data" / "datasets"
QUESTIONS_PATH = ROOT / "src" / "AI_ready_questions.yaml"
DEPARTMENTS_PATH = ROOT / "data" / "acronyms" / "department.csv"
AGENCIES_PATH = ROOT / "data" / "acronyms" / "agency.csv"
REQUIRED_FIELDS = {
    "AI_ready_questions",
    "agency",
    "department",
    "description",
    "homepage",
    "title",
}


def load_yaml(path: Path, errors: list[str]) -> Any:
    try:
        with path.open(encoding="utf-8") as stream:
            return yaml.safe_load(stream)
    except yaml.YAMLError as error:
        errors.append(
            f"{path.relative_to(ROOT)}: invalid YAML: {error.problem}"
        )
    except OSError as error:
        errors.append(f"{path.relative_to(ROOT)}: cannot read: {error}")
    return None


def load_csv(path: Path, errors: list[str]) -> list[dict[str, str]]:
    try:
        with path.open(encoding="utf-8", newline="") as stream:
            return list(csv.DictReader(stream))
    except OSError as error:
        errors.append(f"{path.relative_to(ROOT)}: cannot read: {error}")
        return []


def valid_http_url(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return (
        parsed.scheme in {"http", "https"}
        and bool(parsed.netloc)
        and not (parsed.username or parsed.password)
    )


def validate() -> tuple[list[str], list[dict[str, Any]]]:
    errors: list[str] = []
    question_sheet = load_yaml(QUESTIONS_PATH, errors)
    departments = load_csv(DEPARTMENTS_PATH, errors)
    agencies = load_csv(AGENCIES_PATH, errors)
    if not isinstance(question_sheet, dict):
        errors.append("src/AI_ready_questions.yaml: expected a mapping")
        return errors, []

    questions = question_sheet.get("AI_ready_questions")
    rankings = question_sheet.get("Ranking")
    if not isinstance(questions, list) or not isinstance(rankings, list):
        errors.append(
            "src/AI_ready_questions.yaml: missing question list or rankings"
        )
        return errors, []

    allowed: dict[str, set[str]] = {}
    max_score = 0
    for index, question in enumerate(questions):
        prefix = f"src/AI_ready_questions.yaml: AI_ready_questions[{index}]"
        if not isinstance(question, dict):
            errors.append(f"{prefix}: expected mapping")
            continue
        identifier, score, responses = (
            question.get("id"),
            question.get("score"),
            question.get("responses"),
        )
        if not isinstance(identifier, str) or not identifier:
            errors.append(f"{prefix}.id: expected non-empty string")
            continue
        if identifier in allowed:
            errors.append(f"{prefix}.id: duplicate {identifier!r}")
        if not isinstance(score, (int, float)) or score < 0:
            errors.append(f"{prefix}.score: expected non-negative number")
        else:
            max_score += score
        if (
            not isinstance(responses, list)
            or not all(isinstance(value, str) and value for value in responses)
            or len(responses) != len(set(responses))
        ):
            errors.append(
                f"{prefix}.responses: expected unique non-empty strings"
            )
        else:
            allowed[identifier] = set(responses)
    ranking_scores = [
        item.get("score")
        for item in rankings
        if isinstance(item, dict)
        and isinstance(item.get("score"), (int, float))
    ]
    if not ranking_scores or max(ranking_scores) > max_score:
        errors.append(
            "src/AI_ready_questions.yaml: rankings do not cover maximum score"
        )

    department_names = {row.get("department", "") for row in departments}
    if not department_names or "" in department_names:
        errors.append(
            "data/acronyms/department.csv: invalid department registry"
        )
    if len(department_names) != len(departments):
        errors.append("data/acronyms/department.csv: duplicate departments")
    agency_pairs = {
        (row.get("agency", ""), row.get("department", "")) for row in agencies
    }
    if len(agency_pairs) != len(agencies) or any(
        not all(pair) for pair in agency_pairs
    ):
        errors.append(
            "data/acronyms/agency.csv: invalid or duplicate "
            "agency/department pair"
        )

    manifests: list[dict[str, Any]] = []
    identities: set[tuple[str, str, str]] = set()
    for path in sorted(DATASETS.glob("*.yaml")):
        record = load_yaml(path, errors)
        if not isinstance(record, dict):
            if record is not None:
                errors.append(f"{path.relative_to(ROOT)}: expected mapping")
            continue
        label = str(path.relative_to(ROOT))
        if set(record) != REQUIRED_FIELDS:
            errors.append(
                f"{label}: fields must be exactly {sorted(REQUIRED_FIELDS)}"
            )
        for field in ("title", "description", "department", "agency"):
            if not isinstance(record.get(field), str):
                errors.append(f"{label}.{field}: expected string")
        for field in ("title", "description", "department"):
            if (
                not isinstance(record.get(field), str)
                or not record[field].strip()
            ):
                errors.append(f"{label}.{field}: must be non-empty")
        if not valid_http_url(record.get("homepage")):
            errors.append(
                f"{label}.homepage: expected absolute HTTP(S) URL "
                "without credentials"
            )
        department, agency = record.get("department"), record.get("agency")
        if department not in department_names:
            errors.append(f"{label}.department: unknown {department!r}")
        if agency and (agency, department) not in agency_pairs:
            errors.append(
                f"{label}.agency: unknown pair {(agency, department)!r}"
            )
        answers = record.get("AI_ready_questions")
        if not isinstance(answers, dict):
            errors.append(f"{label}.AI_ready_questions: expected mapping")
        elif set(answers) != set(allowed):
            errors.append(
                f"{label}.AI_ready_questions: must match "
                "configured question IDs"
            )
        else:
            for key, value in answers.items():
                if value not in allowed[key] | {"Unknown"}:
                    errors.append(
                        f"{label}.AI_ready_questions.{key}: "
                        f"invalid value {value!r}"
                    )
        identity = (str(department), str(agency), str(record.get("title")))
        if identity in identities:
            errors.append(
                f"{label}: duplicate department/agency/title identity"
            )
        identities.add(identity)
        manifests.append(record)
    if not manifests:
        errors.append("data/datasets: no manifest files found")
    return errors, manifests


def check_urls(records: list[dict[str, Any]]) -> int:
    failures = 0
    for record in records:
        request = urllib.request.Request(
            record["homepage"],
            headers={"User-Agent": "catalog-health-check/1.0"},
        )
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                print(f"{response.status} {response.url} :: {record['title']}")
        except urllib.error.HTTPError as error:
            print(f"{error.code} {error.url} :: {record['title']}")
            failures += 1
        except urllib.error.URLError as error:
            print(
                f"UNKNOWN {record['homepage']} :: {record['title']} "
                f"({error.reason})"
            )
            failures += 1
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-urls", action="store_true", help="run optional live probes"
    )
    args = parser.parse_args()
    errors, records = validate()
    if errors:
        print("Catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Catalog validation passed: {len(records)} manifests")
    if args.check_urls:
        failures = check_urls(records)
        print(
            "URL observations complete: "
            f"{len(records) - failures} reachable, "
            f"{failures} non-2xx/unknown"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
