# Catalog remediation contract

An item is complete only with its acceptance evidence, not when a finding is
noted. This initial backlog is part of the contract. Phase 1 publisher evidence
is recorded in [publisher-verification-2026-07-16.md](../publisher-verification-2026-07-16.md).

| ID | Finding | Status | Required disposition and acceptance evidence |
| --- | --- | --- | --- |
| R1 | Four malformed YAML manifests | Complete | Repair and prove `make validate` passes. |
| R2 | Generated README drift/build failure | Complete | Regenerate and prove `make verify` passes. |
| R3 | CMS landing page returned 404 | Complete | Review an official replacement and prove its URL is reachable with `make check-urls`. |
| R4 | USPTO legacy bulk-data host failed; publisher moved to its Open Data Portal | Complete | Canonical landing page and registration requirement are verified; unsupported product-level legacy claims are now `Unknown`. Capture authenticated product evidence in the v2 score migration. |
| R5 | iCite bare API returned 401 | Complete | NIH's documented support landing page now replaces the bare API URL; public resource endpoints and bulk snapshots remain subject to v2 evidence capture. |
| R5a | Regulations.gov bulk page returned 403 | Complete | GSA's documented key-backed API replaces the automation-blocked web page. It remains not fully downloadable; record a v2 access rationale. |
| R6 | ClinicalTrials, PMC, and NOAA redirect | Complete | Canonical landing pages were updated and must remain covered by `make check-urls`. |
| R7 | COVID surveillance source is end-of-series | Complete | Catalog description now identifies it as historical, including CDC's discontinuation and temporal-applicability dates. |
| R8 | NOAA/FARA descriptions blank; GSA agency blank | Complete | NOAA/FARA descriptions are complete; GSA Technology Transformation Services is now a registry-backed Regulations.gov agency attribution. |
| R9 | Legacy scores lack dated evidence | Complete | All 15 records now have criterion coverage, source notes, reuse terms, lifecycle status, and review dates in the v2 evidence registry. Unsupported claims are `Unknown`. |
| R10 | No automated release gate/CI | Complete | The first GitHub Actions run passed `make verify` and `make test`; CI continues to enforce the evidence registry. |

Each remediation record must name an owner, status, evidence URL or command,
verification date, and next review date when it is operationalized.
