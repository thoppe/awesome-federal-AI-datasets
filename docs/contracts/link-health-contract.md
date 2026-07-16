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

`make check-urls` is observational and never a release gate: publisher bot
protections and authentication can make automated probes inconclusive. It must
not bypass access controls.
