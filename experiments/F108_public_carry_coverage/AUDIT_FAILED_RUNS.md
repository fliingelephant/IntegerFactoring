# F108 hostile-audit failed runs

## 2026-08-08 02:23:31Z — Sage cache permission

- Status: environment failure before the verifier loaded.
- Exit code: 1.
- Cause: the sandbox denied Sage access to its cache under
  `/Users/zhou/.sage/cache`.
- Evidence: `AUDIT_FAILED_20260808T022331Z_SAGE_CACHE.log`.
- Mathematical status: excluded. No candidate check ran.

## 2026-08-08 02:24:14Z — Sage seed type

- Status: verifier implementation failure after all fixed F98 checks and the
  exhaustive small saturation sweep.
- Exit code: 1.
- Cause: Sage preparsed the deterministic random seed as a Sage integer, but
  Python's `random.Random` accepts only native seed types.
- Evidence: `AUDIT_FAILED_20260808T022414Z_SAGE_SEED.log`.
- Mathematical status: excluded. The verifier had not reached the randomized
  theorem tests, the F99 boundary, or final claim comparisons.
