# Preserved failed runs

## F01 — sandboxed Sage cache failure

The first named runner exited 1 before loading the analysis source because
Sage tried to write its cache under `/Users/zhou/.sage`, which the workspace
sandbox did not permit. No mathematical assertion ran. The same named runner
was then authorized to use the Sage cache.

## F02 — JSON serialization failure

The authorized run completed the mathematical analysis but exited 1 while
serializing a Sage `Integer` stored in `orientation_counts`:

```text
TypeError: Object of type Integer is not JSON serializable
when serializing dict item 'u_power_times_v'
when serializing dict item 'orientation_counts'
```

The source was changed only to pass `default=int` to `json.dumps`. A new
timeout-bounded run is required for evidence.

## F03 — corrected-source sandboxed Sage cache failure

The first run after the audit-label correction invoked the same named runner
and hard 120-second timeout. It exited 1 while Sage imported its libraries:

```text
PermissionError: [Errno 1] Operation not permitted:
'/Users/zhou/.sage/cache/tmptnjchb6p'
```

No candidate assertion ran. The runner overwrote `RUN.log` on the later
authorized retry, so this note preserves the failed disposition. The retry
used the same corrected source and command, exited zero, and is authoritative.
