# Catalog remediation contract

An item is complete only with its acceptance evidence, not when a finding is
noted. This initial backlog is part of the contract.

| ID | Finding | Status | Required disposition and acceptance evidence |
| --- | --- | --- | --- |
| R1 | Four malformed YAML manifests | Complete | Repair and prove `make validate` passes. |
| R2 | Generated README drift/build failure | Complete | Regenerate and prove `make verify` passes. |
| R3 | CMS landing page returned 404 | Complete | Review an official replacement and prove its URL is reachable with `make check-urls`. |
| R4 | USPTO legacy bulk-data host failed; publisher moved to its Open Data Portal | In progress | Canonical landing page and legacy access label were updated; acquire per-criterion v2 evidence before treating the score as verified. |
| R5 | iCite returned 401; Regulations.gov returned 403 | Open | Classify as auth-required/blocked or replace after manual publisher verification; do not call broken from these probes alone. |
| R6 | ClinicalTrials, PMC, and NOAA redirect | Complete | Canonical landing pages were updated and must remain covered by `make check-urls`. |
| R7 | COVID surveillance source is end-of-series | Open | Mark historical or replace, with publisher metadata evidence. |
| R8 | NOAA/FARA descriptions blank; GSA agency blank | In progress | NOAA/FARA descriptions are complete; fill GSA publisher-supported metadata or add an explicit v2 rationale. |
| R9 | Legacy scores lack dated evidence | Open | Migrate every claim to the v2 scoring contract before presenting it as verified. |
| R10 | No automated release gate/CI | In progress | The workflow and pinned gate dependencies are committed locally; its first remote run must pass `make verify` and `make test`. |

Each remediation record must name an owner, status, evidence URL or command,
verification date, and next review date when it is operationalized.
