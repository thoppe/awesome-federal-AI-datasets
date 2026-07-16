# AI-readiness scoring contract

The legacy score is a discovery aid, not a quality certification. It measures
only open access, bulk download, machine-readable format, single-file access,
and scale. It does not establish provenance, licensing, schema quality,
freshness, privacy, bias, or fitness for a particular model.

For v2, every scored criterion must carry its value, publisher evidence URL,
short evidence note, `verified_at` date, and verifier. A green label requires
both the configured numeric threshold and complete dated evidence coverage.
Any `Unknown`, missing evidence, or stale evidence prevents a green label and
sets `review_required`.

Documentation, schema/data dictionary, license, provenance, versioning/update
cadence, and privacy/bias/safety are mandatory disclosures in v2 even when
they do not contribute to a numeric score. Do not infer a score from a landing
page response code.
