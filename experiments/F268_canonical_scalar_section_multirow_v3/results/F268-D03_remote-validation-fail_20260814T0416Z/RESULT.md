# F268-D03 remote validation result

status: `VALIDATION_FAIL`

The unchanged frozen runner compiled all three C++ programs. The corpus
self-test passed. The search self-test then printed
`F268_SEARCH_FATAL family syntax SHA mismatch` and returned 70. The runner
stopped under `set -e`. It did not run the label self-test, corpus generation,
preflight, discovery, or heldout phases. The target's `preflight/` directory is
empty. This packet produced no search evidence.

## Chronology

1. The first invocation stopped at `remote_run.sh:29` because
   `/usr/bin/time` did not exist. This assertion precedes target creation at
   lines 117--118, so that invocation created no target and no run log.
2. The standard Ubuntu `time` package, version `1.9-0.1build2`, was installed
   from 2026-08-14 04:26:35 through 04:26:36 +0800. The copied APT and dpkg
   logs preserve this event.
3. The same frozen runner was invoked again. It created the target and recorded
   resources at 04:26:48 +0800. All three compilations completed. The corpus
   self-test passed at 04:27:45 +0800.
4. The search self-test failed immediately afterward at 04:27:45 +0800. The
   runner exited 70 through the search program's exception handler.

## Diagnosis

The advertised digest and invocation are correct:

- Remote and local `sha256sum` both give
  `aea7c29e0c077c701ba8201ec6acb6ff8ca26adbccf1e3096f97b659604bc6ce`
  for `FAMILY_SYNTAX.tsv`.
- The same value appears in `remote_run.sh` and `search.cpp`.
- `remote_run.sh:130-132` passes the family file path followed by that digest,
  which matches the search program's argument order.

The custom SHA-256 implementation is wrong. At `search.cpp:137`, round
constant 46 is `0x2748774U`. SHA-256 requires `0x2748774cU`. Thus the internal
digest cannot equal the correct externally frozen digest.

The self-test order hid the specific defect. `self_test()` authenticates the
family file at line 2241 before it checks the `"abc"` SHA-256 known answer at
lines 2242--2244. The family check therefore fails first.

## Exact clean repair

Create a new immutable F268-D04 packet. Do both changes:

1. Change only the bad SHA-256 round constant from `0x2748774U` to
   `0x2748774cU`.
2. Run the `"abc"` known-answer check before the first call to
   `authenticate_family_syntax()` so a SHA implementation failure is isolated
   before any artifact authentication.

Then update the D04 version and output names, freeze all successor bytes, and
obtain a fresh hostile pre-run audit. Use a new remote source directory and a
new target. Do not reuse D03 binaries or its failed target.
