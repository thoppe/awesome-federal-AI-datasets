# Catalog manifest contract

## Current v1 baseline

Each `data/datasets/*.yaml` file is one catalog record. It must safely parse to
a mapping with exactly these fields: `AI_ready_questions`, `agency`,
`department`, `description`, `homepage`, and `title`.

- `title` and `description` are non-empty strings; use a YAML block scalar for
  multi-sentence prose.
- `homepage` is an absolute HTTP(S) publisher landing page with no credentials.
- `department` is a key in `data/acronyms/department.csv`.
- A non-empty `agency` is a valid agency/department pair in
  `data/acronyms/agency.csv`. A blank agency is permitted only for legacy v1
  records and must have a remediation item.
- The five score responses use only the configured response value or `Unknown`.
- The department/agency/title identity is unique.

## v2 evidence contract

Every v1 manifest must carry an `evidence_id` equal to its filename stem. Its
authoritative evidence record lives in `data/catalog_evidence.yaml`; this keeps
the concise discovery manifest separate from evidence that changes on a review
cadence.

Each evidence record must provide a publisher URL and note, reuse-terms URL and
note, lifecycle status/cadence/next-review date, and source evidence for all
five readiness criteria. The criterion values remain in the manifest and are
accepted only when the evidence registry covers each one. `Unknown` is an
honest, evidence-backed result—not a passing score. The validator rejects a
missing, orphaned, malformed, or overdue evidence record.
