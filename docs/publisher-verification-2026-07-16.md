# Publisher verification record — 2026-07-16

Evidence tier: publisher documentation and publisher metadata. This record
supports Phase 1 remediation statuses; it does not certify unverified legacy
AI-readiness claims.

## USPTO Open Data Portal

- [USPTO's BDSS retirement notice](https://www.uspto.gov/system-status/20250408-bulk-data-storage-system-bdss-retirement)
  confirms the legacy Bulk Data Storage System was retired and directs users to
  ODP's Bulk Data Directory.
- [ODP registration notice](https://data.uspto.gov/apis/bulk-data/search)
  states that a valid USPTO.gov account is required from June 18, 2026 and that
  API access requires an API key.

The two USPTO records therefore use `Registration required` and retain only
that verified access fact. Product-specific download, format, schema, image,
and scale assertions are `Unknown` pending authenticated product evidence.

## iCite and Regulations.gov

- [NIH iCite bulk-data and API documentation](https://support.icite.nih.gov/hc/en-us/articles/9513563045787-Bulk-Data-and-API)
  documents public resource endpoints and bulk snapshots. The bare `/api` path
  is not a suitable catalog landing page.
- [GSA Regulations.gov API documentation](https://open.gsa.gov/api/regulationsgov/)
  documents the public, API-key-backed query API and notes that a permanent
  bulk-download solution remains pending.
- [GSA eRulemaking services](https://www.gsa.gov/policy-regulations/regulations/managing-the-federal-rulemaking-process-erulemaking/services-for-federal-rulemaking-agencies)
  establishes the GSA program attribution for Regulations.gov.

## CDC historical COVID dataset

The [CDC dataset metadata](https://data.cdc.gov/api/views/n8mc-b4w4) states
that reporting discontinued July 1, 2024; public access continues without
updates. It gives temporal applicability through 2024-07-05 and a July 9, 2024
data-last-updated timestamp. The catalog now describes this record as
historical.
