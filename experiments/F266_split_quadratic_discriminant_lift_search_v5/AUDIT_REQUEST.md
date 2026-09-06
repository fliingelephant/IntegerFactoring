# F266-D05 fresh independent hostile pre-run audit request

Status: **STATIC ONLY — PASS required before any target invocation.**

Audit the exact F266-D05 packet independently and from first principles. D05
is a packaging successor to D04. Do not treat the stopped D04 handoff as an
audit, and do not reuse a D01, D02, or D03 verdict.

## Frozen-root authentication

The audit coordinator must supply the expected SHA-256 of the exact D05
`FROZEN.sha256` bytes outside this packet. This out-of-band value is the D05
frozen root. First compute the observed SHA-256 of `FROZEN.sha256` and require
exact equality with the supplied value. Then authenticate every manifest
entry with `sha256sum -c FROZEN.sha256` or an equivalent read-only check.

`FROZEN.sha256` cannot contain its own digest. Do not accept a root value from
any frozen input as a substitute for the coordinator-supplied value.

The frozen inputs named by `FROZEN.sha256` must be exactly this set, with no
duplicate, missing, or extra filename:

```text
ALGEBRA.md
PREREGISTRATION.md
search.cpp
remote_run.sh
PROVENANCE.md
AUDIT_REQUEST.md
PRELAUNCH_MANIFEST.md
```

`FROZEN.sha256` is the root object and is not an entry in itself. The future
`HOSTILE_PRERUN_AUDIT.md` is auditor output and is not a frozen input.

Before relying on provenance, independently authenticate the immutable D04
root and entries recorded in `PROVENANCE.md`. Also authenticate the D01--D03
roots and their hostile FAIL audit hashes. Confirm that D04 contains no
hostile audit and that the stopped handoff produced no verdict artifact.

## Priority checks

Check these surfaces in order. Any decisive blocker requires FAIL.

1. Prove that D05 `ALGEBRA.md`, `PREREGISTRATION.md`, and `search.cpp` are
   byte-for-byte equal to their authenticated D04 counterparts. Prove that
   the runner diff is limited to frozen-packet filename assertion,
   authentication, evidence accounting, uncompressed-manifest inclusion,
   and archive inclusion. Reject any change to mathematics, grammar, cohort
   IDs, rankings, schemas, phase commands, deadlines, or resource constants.
2. Reconstruct the runner packet-list gate. Its required filenames and the
   filenames in `FROZEN.sha256` must be exactly equal. The same central list
   must place `AUDIT_REQUEST.md`, `PROVENANCE.md`, and every other frozen
   input into all packet authentication, evidence-size, complete
   uncompressed-manifest, and archive paths.
3. Verify the D04 sidecar closure. Each selection and corpus sidecar must bind
   its embedded digest and fixed target basename to the read-only digest
   captured from closed discovery stdout. It must also authenticate the
   target bytes. Reject alternate digest, filename, separator, line count, or
   byte count. Verify every repeated check and the focused malformed-record
   self-check.
4. Verify one exact eight-stage direct-screen chronology in algebra,
   preregistration, `DirectStage`, source counters, TSV schema, and runner
   checks. Stage `source` must contain attempted `a`, `r`, `s`, `r-s`, and
   inverse seed `u`. Stage `base` must contain `A0`, `B0`, `C0`, `Delta0`,
   and supplied root `x`, once per retained base and lift level. Check the
   exact 32 counter columns and every `tests=unit+full+proper` partition.
5. Verify the inherited gauge, exact divisibility, registered-screen,
   equal-row/template, replayable-certificate, mandatory
   `UNKNOWN_OPAQUE_NOT_NEEDED`, eligible distinct-row baseline, and held-out
   null gates. The null coverage quantifiers must be one selected family
   across every cell, with explicit zero and ineligible evidence.
6. Verify the exact registered ranking tuple and population, immutable
   selection and corpus byte binding, complete public/private firewall,
   factor-free worker boundary, cohort generation, held-out chronology, and
   all positive, null, and inconclusive labels. Check that no algebraic
   family, candidate, decoy, cohort, rank field, score, or selection rule
   drifted.
7. Verify every exact arithmetic assertion, signed-gcd channel, carry and
   resultant ticket, residual row map, block reconstruction, parity kernel,
   exact-square gate, P66 decoder route, certificate replay field, cap, and
   output schema promised by the two theory files.
8. Verify the whole-packet four-hour deadline, 4 GiB virtual-memory limit,
   one-GiB file and aggregate-output gates, fixed one-worker 1/16 preflight,
   measured serialized evidence bytes, conservative projections, eight-worker
   production cap, conflict firewall, phase manifests, final resource record,
   complete uncompressed manifest, and one-thread nice/timeout/pipefail
   compression. Check all paths through failure as well as success.

Treat `PRELAUNCH_MANIFEST.md` and `PROVENANCE.md` as claims to verify. They are
not audit evidence.

## Static-only restrictions

Use read-only static inspection only. Do not compile or execute `search.cpp`.
Do not invoke, source, or parse-run `remote_run.sh`. Do not access a remote
host. Do not generate, inspect, score, or open any discovery, preflight, or
held-out cohort. Do not edit a frozen input, any predecessor, or any durable
ledger. Do not repair a blocker in place.

Write only `HOSTILE_PRERUN_AUDIT.md` in the D05 directory. Give one strict
PASS or FAIL. A PASS must contain these exact standalone lines:

```text
# Verdict: PASS
frozen_manifest_sha256: <lowercase SHA-256 of the exact D05 FROZEN.sha256 bytes>
```

A FAIL must contain `# Verdict: FAIL` and must not contain the PASS line.
Record the authenticated hashes and decisive findings. The audit must not
claim compiler, self-test, preflight, runtime, memory, remote, or cohort
evidence. After closing the audit file, report its SHA-256 to the coordinator.
