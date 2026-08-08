# F118 failed runs

One environment-only failure is preserved.

`RUN_FAILED_20260808T052055Z_EXIT_1.log` records a Sage import failure. The
workspace sandbox blocked Sage from writing its cache under `~/.sage`.
`OUTPUT_FAILED_20260808T052055Z_EXIT_1.json` records `NO_OUTPUT`.

The failure occurred before prime generation or source execution. The same
registered runner was rerun with access to the existing Sage cache. That run
passed. No source, corpus rule, timeout, or acceptance condition changed.
