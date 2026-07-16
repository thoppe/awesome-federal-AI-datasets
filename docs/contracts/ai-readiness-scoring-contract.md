# AI-readiness scoring contract

The legacy score is a discovery aid, not a quality certification. It measures
only open access, bulk download, machine-readable format, single-file access,
and scale. It does not establish provenance, licensing, schema quality,
freshness, privacy, bias, or fitness for a particular model.

For v2, the manifest's scored criterion must be covered by its matching
evidence-registry record, which carries a publisher evidence URL, short note,
verification date, verifier, and lifecycle review date. A green label requires
both the configured numeric threshold and complete fresh evidence coverage.
Any `Unknown`, missing evidence, or overdue review prevents a green label and
sets `review_required`.

Documentation, schema/data dictionary, license, provenance, versioning/update
cadence, and privacy/bias/safety are mandatory disclosures in v2 even when
they do not contribute to a numeric score. Do not infer a score from a landing
page response code.
