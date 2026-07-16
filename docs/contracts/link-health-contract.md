# Link-health contract

Landing-page reachability, artifact downloadability, and API availability are
separate facts. A probe records URL, final URL, method, timestamp, status code,
and one outcome: `healthy`, `redirected`, `auth_required`, `blocked`, `broken`,
or `unknown`.

- A 2xx response is healthy; a documented redirect is redirected and its
  canonical target should be reviewed.
- 401/403 means auth-required or blocked, not broken.
- 404/410 is broken. DNS/network failure is unknown until retried.
- Active records are rechecked every 90 days; historical records every 365.
  Broken records need a replacement, historical classification, or removal
  decision within 14 days.

The 90/365-day link-health recheck is a minimum operational cadence, independent
of a publisher's release cadence or a longer-form content/evidence assessment.
An active record's `next_review_at` therefore cannot be later than its next
90-day link-health review. Historical records may use the 365-day cadence.

`make check-urls` is observational and never a release gate: publisher bot
protections and authentication can make automated probes inconclusive. It must
not bypass access controls.

`make check-resources` applies the same observational policy to direct artifact,
schema, and documentation links recorded in the evidence registry. It never
downloads an artifact and is not a release gate.
