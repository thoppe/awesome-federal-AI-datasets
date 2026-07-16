# Validation and publication contract

The offline release gate is deterministic and non-interactive:

1. `make validate` safely parses all manifests and validates schema, registry,
   score configuration, score values, and duplicate identities.
2. `make verify` runs that gate and renders README content in memory; it fails
   if committed `README.md` differs.
3. `make build` first validates, then writes the generated README. It never
   invokes the interactive supplementation tool.
4. `make test` runs the harness tests. Checks are triggered in this workspace
   as part of each major change handoff; this repository intentionally has no
   hosted workflow.

Validation errors are aggregated with paths and fields; a single malformed
record must not hide later defects. Generated README changes must be reviewed
alongside their manifest changes.

## Change handoff contract

Each major completed change must end in an intentional local commit after its
applicable contract gates pass. A major change is any contract, catalog,
generated README, validation-harness, dependency, or workflow change that
alters published behavior or release confidence. Keep unrelated work out of
that commit.

After creating the commit, the implementer must explicitly offer to push it
and state the branch and commit SHA. Pushing remains a separate user-authorized
action unless the user requested a deploy, which includes commit and push.
