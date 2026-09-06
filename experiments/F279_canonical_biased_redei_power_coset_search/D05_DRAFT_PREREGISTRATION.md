# F279-D05 additive counter-carry and status-schema repair

## Status, ancestry, and exact scope

F279-D05 is an unfrozen theory/interface amendment. It authorizes no source,
runner, fixture, tape, source freeze, compile, self-test, benchmark,
validation, experiment, remote access, private-label access, ledger change,
git staging, or commit.

The authenticated immediate inputs are:

```text
D04_DRAFT_ALGEBRA.md
3f801eb810f6019c5c54e2879c3d6f88d8ae2d99d7891e96da96e8b8c9718133

D04_DRAFT_PREREGISTRATION.md
2a21322b509a16a85162d8f16654e092f965c09b704179b2501f9b8153c59cf5

D03_HOSTILE_THEORY_AUDIT.md
859a170e6ca26d19f696559df1e7b570fc7f06a55240226fdf46cdf19e51e676
```

The fresh D04 audit authenticated those hashes, returned `REVISE`, and
wrote no audit file. Its only blockers were missing authenticated packet-
counter carry into held-out mode and incomplete status JSON.

Read D05 additively with the complete D01-D04 chain. D05 supersedes only:

1. the D04 held-out and held-out-replay input descriptors and argv;
2. the two phase-summary counter fields affected by packet carry; and
3. D04 Sections 7 and 8 as to status values, error tokens, and precedence.

Every mathematical statement, cap value, cap scope, public/private role,
firewall rule, manifest chronology, replay workload, resource projection,
probability condition, authorization gate, and nonclaim remains unchanged.
Every future artifact prefix and JSON version is `F279-D05`.

## 1. Authenticated packet-counter carry

The packet caps remain exactly:

```text
MAX_RAW_HITS_TOTAL             131072
MAX_GLOBAL_ORDER_CHECKS_TOTAL  131072
```

They apply to discovery plus held-out. They are not two per-phase caps. A
runner cannot check them only after held-out. Selection bytes are not a
counter source.

### 1.1 Summary counter fields

D05 inserts these four keys immediately after `global_order_checks` in the
inherited phase-summary key order:

```text
carry_raw_hits
carry_global_order_checks
packet_raw_hits
packet_global_order_checks
```

All six affected fields are canonical unsigned JSON integers:

```text
raw_hits
global_order_checks
carry_raw_hits
carry_global_order_checks
packet_raw_hits
packet_global_order_checks
```

Their meanings are exact.

```text
raw_hits
    raw proper ranked endpoints produced in this phase

global_order_checks
    large registered mixed-order checks executed in this phase

carry_raw_hits
    authenticated packet raw-hit total before this phase

carry_global_order_checks
    authenticated packet global-order-check total before this phase

packet_raw_hits
    carry_raw_hits+raw_hits

packet_global_order_checks
    carry_global_order_checks+global_order_checks
```

The discovery summary must satisfy:

```text
carry_raw_hits=0
carry_global_order_checks=0
packet_raw_hits=raw_hits
packet_global_order_checks=global_order_checks
packet_raw_hits<=131072
packet_global_order_checks<=131072
```

The held-out summary must satisfy the same sum equations with the
authenticated discovery packet totals as its two carry fields.

No field is a quoted string, Boolean, null, floating value, signed value, or
JSON object. Overflow while parsing or adding is `input_schema` failure.

### 1.2 Exact public carry inputs

Held-out mode receives both closed public files:

```text
F279-D05.discovery.public.manifest.tsv
F279-D05.discovery.summary.json
```

The first is descriptor 11. The second is descriptor 12. Both are read-only
regular files. Neither file contains a private fixture, factor, cohort,
local character, label, or lead field.

Descriptor 11 must have the inherited exact manifest header and seven
discovery records. Its complete SHA-256 must equal the new trusted CLI hash.
The manifest record for `F279-D05.discovery.summary.json` must give the exact
descriptor-12 byte length and SHA-256. Descriptor 12 must also have the
exact D05 summary schema, `phase="discovery"`, the authenticated discovery
fixture/tape/selection hashes, and the discovery counter identities in
Section 1.1.

The evaluator authenticates in this order:

1. hash descriptor 11 and compare it with the trusted manifest hash;
2. parse all seven manifest rows and their unsigned-byte order;
3. find the one exact discovery-summary row;
4. compare descriptor 12 type, byte length, and SHA-256 with that row;
5. parse descriptor 12 under the exact canonical JSON grammar;
6. verify its phase, input hashes, selection hash, and counter identities;
7. verify both packet totals are at most their inherited caps; and
8. initialize held-out cumulative counters from `packet_raw_hits` and
   `packet_global_order_checks`.

A failure in steps 1, 4, or a hash comparison is `input_auth`. A malformed
manifest row, summary value, field order, phase, identity, counter equation,
range, or overflow is `input_schema`. An underlying read failure is
`input_io`.

Selection descriptor 8 remains independently authenticated. It supplies
candidate identities and ranks only. It supplies no counter, and the
evaluator never infers a counter from its rows, byte length, or hash.

### 1.3 Abort before the next raw-hit record

Discovery starts `packet_raw_hits=0`. Held-out starts it at the authenticated
discovery value. When an eligible endpoint produces `1<g_F<N`, perform this
check before any action for that raw hit:

```text
if packet_raw_hits == MAX_RAW_HITS_TOTAL:
    fail with exit 68 and error_code raw_hit_cap
else:
    packet_raw_hits += 1
    phase raw_hits += 1
```

The failure occurs before a registered relation check, score update,
certificate row, endpoint-checksum row, diagnostic reference, summary
update, or output extension for that candidate. The failed output root is
not evidence. No truncation or phase split is permitted.

### 1.4 Abort before the next global-order check

Discovery starts `packet_global_order_checks=0`. Held-out starts it at the
authenticated discovery value. Immediately before one inherited large
mixed-order consistency check, perform:

```text
if packet_global_order_checks == MAX_GLOBAL_ORDER_CHECKS_TOTAL:
    fail with exit 68 and error_code global_order_cap
else:
    packet_global_order_checks += 1
    phase global_order_checks += 1
    execute the one check
```

The failure occurs before exponent construction, pair powering, gcd,
certificate mutation, checksum-record mutation, or output extension for
that next check. A check cannot be reserved and later returned. It cannot be
charged after execution.

### 1.5 Held-out completion

On successful held-out completion, its summary writes the phase counts, the
two authenticated carry values, and the two final packet totals. Public
replay recomputes all six values. Label processing cannot change them.

## 2. Descriptor and containment amendment

D04 descriptors 2 through 10 retain their meanings. Add:

```text
11  discovery public manifest, read-only regular file
12  discovery public summary, read-only regular file
```

The exact open-descriptor sets become:

```text
self-test
    2,10

benchmark
    2,9,10

discovery
    2,3,4,5,6,7,9,10

heldout
    2,3,4,5,6,7,8,9,10,11,12

replay-discovery
    2,3,4,5,6,7,8,9,10

replay-heldout
    2,3,4,5,6,7,8,9,10,11,12
```

Descriptors 11 and 12 are closed in every other mode. Descriptors 0 and 1
remain closed. No path or environment fallback exists.

The D05 containment-manifest descriptor keys end in this exact order:

```text
selection_fd,output_dir_fd,status_fd,
discovery_public_manifest_fd,discovery_summary_fd,
deployment_contract_sha256
```

Their descriptor values are exactly `8,9,10,11,12`. The deployment-contract
hash remains an opaque unresolved deployment input as in D04.

## 3. Exact six mode command lines

The D04 argv grammar remains exact: separate option/value elements, displayed
order, no repetition, no reordering, no `--option=value`, no extra element,
canonical descriptor digits, and lowercase `H64` hash values.

### 3.1 Self-test

```text
f279_public --mode self-test --status-fd 10
```

### 3.2 Benchmark

```text
f279_public --mode benchmark --scratch-dir-fd 9 --status-fd 10
```

### 3.3 Discovery

```text
f279_public --mode discovery --public-fixture-fd 3 --tape-fd 4 --promise-fd 5 --inputs-manifest-fd 6 --containment-manifest-fd 7 --output-dir-fd 9 --status-fd 10 --trusted-containment-sha256 H64 --trusted-inputs-manifest-sha256 H64
```

### 3.4 Held-out

```text
f279_public --mode heldout --public-fixture-fd 3 --tape-fd 4 --promise-fd 5 --inputs-manifest-fd 6 --containment-manifest-fd 7 --selection-fd 8 --discovery-public-manifest-fd 11 --discovery-summary-fd 12 --output-dir-fd 9 --status-fd 10 --trusted-containment-sha256 H64 --trusted-inputs-manifest-sha256 H64 --trusted-selection-sha256 H64 --trusted-discovery-public-manifest-sha256 H64
```

### 3.5 Discovery replay

```text
f279_public --mode replay-discovery --public-fixture-fd 3 --tape-fd 4 --promise-fd 5 --inputs-manifest-fd 6 --containment-manifest-fd 7 --selection-fd 8 --phase-dir-fd 9 --status-fd 10 --trusted-containment-sha256 H64 --trusted-inputs-manifest-sha256 H64 --trusted-selection-sha256 H64
```

### 3.6 Held-out replay

```text
f279_public --mode replay-heldout --public-fixture-fd 3 --tape-fd 4 --promise-fd 5 --inputs-manifest-fd 6 --containment-manifest-fd 7 --selection-fd 8 --discovery-public-manifest-fd 11 --discovery-summary-fd 12 --phase-dir-fd 9 --status-fd 10 --trusted-containment-sha256 H64 --trusted-inputs-manifest-sha256 H64 --trusted-selection-sha256 H64 --trusted-discovery-public-manifest-sha256 H64
```

The two unchanged command lines are repeated to make the six-mode grammar
closed. No mode accepts literal carry counters.

## 4. Replay and firewall composition

The public chronology is now exact.

1. Discovery closes its seven public files.
2. The runner creates and authenticates the discovery public manifest.
3. The runner retains that manifest's exact SHA-256 as part of the selection
   seal.
4. Held-out receives selection, the discovery public manifest, and its
   discovery summary through descriptors 8, 11, and 12.
5. Held-out authenticates and imports only the two public packet counters.
6. Held-out closes its six public files. The runner creates its public
   manifest.
7. `replay-discovery` reconstructs the discovery phase and its final packet
   counters.
8. `replay-heldout` authenticates the same discovery manifest and summary,
   imports the same carry, and reconstructs held-out counters and outputs.
9. The runner requires both replay PASS records and the same discovery
   manifest hash before it permits private-label access.

The carry files are public discovery evidence. They reveal no private label.
The label role cannot write, replace, or reinterpret them. This preserves the
public/private firewall and the D03 seal-label-replay chronology.

## 5. Total self-test PASS status

The self-test PASS field `checks` is a JSON array of strings. It is not a
count, object, null, or free-form array. On PASS it equals this exact ordered
array:

```text
["candidate_source_counts","pair_multiplication","endpoint_matrix_identity","split_nonsplit_examples","target_chart_controls","f278_half_order_example","input_invariant_factors","orbit_offsets","mixed_bounded_phase","uniform_projective_counts"]
```

These ten tokens correspond in order to the ten inherited required
self-test groups. Each group must pass completely before its token enters
the array. A PASS record always contains all ten. It cannot contain a
prefix, duplicate, reordered token, unknown token, or optional token.

The self-test PASS status remains one canonical JSON line with keys:

```text
version,role,mode,phase,checks,failures,status
```

Its other fixed values remain:

```text
version  "F279-D05"
role     "f279_public"
mode     "self-test"
phase    null
failures []
status   "pass"
```

A self-test failure does not emit a partial PASS schema. It emits the exact
controlled-failure schema with `error_code="self_test"` and exit 69.

## 6. Total controlled-failure vocabulary

The controlled-failure key order remains:

```text
version,role,mode,phase,status,exit_code,error_code
```

`exit_code` is a canonical unsigned JSON integer. `error_code` is one exact
string from this complete mapping:

```text
exit 64
    cli

exit 65
    descriptor
    input_io
    input_auth
    input_schema

exit 66
    output_exists
    serialization
    output_cap
    output_io

exit 67
    arithmetic
    replay

exit 68
    workload_cap
    raw_hit_cap
    global_order_cap
    memory_cap
    control_shortfall
    thread_resource

exit 69
    self_test
    benchmark

exit 70
    internal
```

No error token belongs to two exits. No controlled failure uses a token not
listed here.

### 6.1 Exit 66 distinctions

Use `output_exists` when any required output or benchmark temporary basename
already exists at its first exclusive-create check.

Use `serialization` when a value cannot be represented by its exact schema,
contains a forbidden byte or token, violates canonical integer or JSON/TSV
grammar, exceeds its per-record cap, or would produce a wrong header, field
count, key order, collation, or final-LF form.

Use `output_cap` when already valid canonical bytes would make one file
exceed `RLIMIT_FSIZE` or the packet classification-output total exceed
`536870912` bytes. The check occurs before opening or extending the file for
those bytes.

Use `output_io` only for an OS create, write, partial-write retry, `fsync`,
close, reopen, seek, stat, or output-hash failure after the earlier checks
pass.

### 6.2 Exit 68 distinctions

Use `workload_cap` for a fixed nominal source, candidate, control-attempt,
certificate-replay, or diagnostic-work count that would exceed an inherited
maximum other than the next two named packet counters.

Use `raw_hit_cap` only for the pre-increment check in Section 1.3.

Use `global_order_cap` only for the pre-increment check in Section 1.4.

Use `memory_cap` for a checked allocation-size overflow, a failed production
allocation, or a measured/projected evaluator capacity that exceeds the
inherited memory gate. An external RLIMIT or signal that prevents a status
record remains a runner-observed resource failure, not a forged controlled
record.

Use `control_shortfall` only when all three assigned ExactTape256 attempts
fail for one required eligible control.

Use `thread_resource` only when creation or joining of the exact four public
worker threads fails. There is no smaller worker-count fallback.

## 7. Failure precedence

The evaluator is fail-fast. It records the first failure in normative mode
chronology and performs no later check. If more than one predicate is
available at the same checkpoint, use this exact precedence from first to
last:

```text
cli
descriptor
input_io
input_auth
input_schema
output_exists
workload_cap
memory_cap
thread_resource
raw_hit_cap
global_order_cap
control_shortfall
arithmetic
replay
self_test
benchmark
serialization
output_cap
output_io
internal
```

Additional local rules are:

1. Authenticate raw bytes before schema interpretation. Thus a known hash
   mismatch is `input_auth`; malformed authenticated bytes are
   `input_schema`.
2. Build canonical output bytes before any size check. Thus an invalid
   encoding is `serialization`; valid bytes that cross a cap are
   `output_cap`.
3. Check the raw-hit cap before every later action for that hit.
4. Check the global-order cap before constructing or executing that check.
5. `bad_alloc` and checked allocation overflow are `memory_cap`. Any other
   uncaught exception is `internal`.
6. A status-pipe write failure cannot produce a second controlled record.
   It exits 70 with no valid status line.

The status record is at most 65,536 bytes, has one final LF, and is written
exactly once through descriptor 10 under the inherited partial-write and
`EINTR` rules.

## 8. Preserved authority and resource boundary

D05 does not change the D04 noncircular stages. A future fresh D05 theory
PASS can authorize drafting only the one standalone portable evaluator
source `f279_public.cpp`. It cannot authorize private or runner source,
containment selection, source freeze, compile, validation, or execution.

The additional two public input descriptors and four summary integers do not
change candidate, control, diagnostic, replay, or output record maxima. The
public discovery manifest and summary already exist in the inherited output
bound. No new evidence file is added.

The packet-wide caps are enforced online and unchanged. A resource abort is
not evidence. The exact probability claim remains conditional only on
`A_ctrl`, never on packet success or these cap checks.

This exact D05 pair must now be released unchanged for a fresh no-context
hostile theory audit. Its authors do not grant it a PASS.
