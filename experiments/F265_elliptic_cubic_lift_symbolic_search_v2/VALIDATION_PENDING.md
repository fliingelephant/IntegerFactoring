# F265-D02 validation status

Status: `STATIC_FROZEN; HOSTILE_AUDIT_PENDING; TARGET_VALIDATION_PENDING`

F265-D02 has not been compiled or executed. No self-test, preflight,
discovery, heldout, selection, or summary command has run. No corpus has been
generated or inspected.

Dynamic validation is forbidden while F258-D01 is active. After F258-D01 has
ended, the exact frozen `remote_run.sh` can start only if a fresh independent
hostile audit gives PASS. The runner must then authenticate `FROZEN.sha256`,
pass its host gates, compile, pass self-test, and pass preflight before either
corpus.

Any failure is preserved. A changed source or protocol requires a new
immutable version and new hashes.
