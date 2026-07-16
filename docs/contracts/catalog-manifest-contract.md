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

## v2 migration contract

Before a record can be described as verified or AI-ready, add a stable `id`,
publisher/data-access URLs, license or reuse terms, update cadence, data status
(`active`, `historical`, `retired`, or `unknown`), and dated evidence for every
readiness assertion. Unknown is an honest value, not a passing score.

The validator enforces v1 today. v2 fields become a release requirement only
when the remediation contract marks the migration complete; this avoids
misrepresenting legacy claims as newly verified evidence.
