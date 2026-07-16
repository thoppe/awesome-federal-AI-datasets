# Catalog quality contracts

This directory is the authoritative specification for the catalog and its
publication harness. Code implements these contracts; a README table is a
generated view, not an independent source of truth.

Run the offline gate with `make validate`, confirm the committed README with
`make verify`, and run the optional, non-gating network observations with
`make check-urls`.

The current catalog is a legacy metadata baseline. Its readiness assertions are
not evidence-backed until the migration in
[catalog-remediation-contract.md](contracts/catalog-remediation-contract.md)
is complete.

## Contract index

- [Catalog manifest](contracts/catalog-manifest-contract.md)
- [AI-readiness scoring](contracts/ai-readiness-scoring-contract.md)
- [Link health](contracts/link-health-contract.md)
- [Validation and publication](contracts/validation-and-publication-contract.md)
- [Assessment boundary](contracts/data-assessment-boundary-contract.md)
- [Remediation](contracts/catalog-remediation-contract.md)
- [2026-07-16 baseline](quality-assessment-baseline-2026-07-16.md)
- [Phase 1 publisher verification](publisher-verification-2026-07-16.md)
- [v2 catalog evidence registry](../data/catalog_evidence.yaml)
