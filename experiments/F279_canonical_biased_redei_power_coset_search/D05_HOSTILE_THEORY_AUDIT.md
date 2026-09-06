# F279-D05 fresh hostile theory audit

## Verdict

**STRICT PASS.**

The authenticated D05 pair is a coherent additive repair of the
authenticated D04 pair. It closes the two D04 byte-interface blockers. I
found no mathematical, counter-carry, descriptor, command-line, replay,
firewall, status-schema, resource-accounting, or authority blocker.

This is a theory/interface-only PASS. It authorizes drafting only the one
standalone C++17 portable evaluator source:

```text
f279_public.cpp
```

It authorizes no private fixture/label source, runner source, containment
choice, source freeze, compilation, self-test, benchmark, validation,
fixture or tape creation, experiment, remote access, private-label access,
ledger change, git staging, or commit. A later source packet still needs its
own immutable freeze and hostile static PASS. Any later execution still
needs the applicable validation and explicit user authorization.

## Authenticated inputs and additive composition

I authenticated the D05 files before I read them.

```text
D05_DRAFT_ALGEBRA.md
5e27479a5298b2ed6758bc81ba6f1aabaca107b97a624887aa7d420eef114763

D05_DRAFT_PREREGISTRATION.md
2d76c815fe752d1bc7f50caac788ab8943a8ec2a46377e7773677590a416cdb5
```

I also authenticated the immediate D04 inputs and the required D03 hostile
PASS before I read them.

```text
D04_DRAFT_ALGEBRA.md
3f801eb810f6019c5c54e2879c3d6f88d8ae2d99d7891e96da96e8b8c9718133

D04_DRAFT_PREREGISTRATION.md
2a21322b509a16a85162d8f16654e092f965c09b704179b2501f9b8153c59cf5

D03_HOSTILE_THEORY_AUDIT.md
859a170e6ca26d19f696559df1e7b570fc7f06a55240226fdf46cdf19e51e676
```

The D03 audit is an authenticated strict theory-only PASS. Its recorded
predecessor hashes also match the local bytes:

```text
D03_DRAFT_ALGEBRA.md
d9f2fa7c490b96214e976478740257b0e6cc675f20bf7f7219760e4ca450e159

D03_DRAFT_PREREGISTRATION.md
6b5f1633e2cf2654adb8ec8bb2f79bf84a242550ef57cb4dc6cf964013413a1b

D02_DRAFT_ALGEBRA.md
f87f787bad0943b7149d276e158d28a6350dc8ab72836e80112acf33240cf843

D02_DRAFT_PREREGISTRATION.md
93e207fb2e3e4c489eb009f56e16751b3df79d7ecc329b602a678761795533f9

DRAFT_ALGEBRA.md
328c8c26d5c06e3033300539fd5900f7ddcb55f253b75fae851c58db47eea424

DRAFT_PREREGISTRATION.md
4498a4f3e2404297d6eda58036fc45e097915a13d73077dc9511dea4e6cb7e7e
```

I applied the stated additive merge rules through D01, D02, D03, D04, and
D05. I did not read D05 as a standalone replacement. The fresh D04 audit
returned `REVISE` and wrote no PASS artifact. D05 changes only its two
reported interface defects: authenticated packet-counter carry and the
total status schema.

## Counter-carry and authentication audit

- Held-out and replay-heldout receive the same closed public discovery
  manifest on descriptor 11 and its discovery summary on descriptor 12.
  Both descriptors are read-only regular files. They are closed in every
  other mode.
- The trusted CLI hash authenticates all descriptor-11 bytes. The exact
  seven-row manifest then authenticates the descriptor-12 basename, byte
  length, and SHA-256. No separate unbound summary hash is needed.
- The evaluator checks the manifest header, exact row set, unsigned-byte
  order, and exact discovery-summary row. It then checks the canonical D05
  discovery-summary schema, phase, committed input hashes, sealed selection
  hash, counter identities, and cap ranges.
- The failure partition is closed. Descriptor set, type, and access errors
  fail at the earlier descriptor check. Read failures are `input_io`. Hash
  and authenticated byte-length mismatches are `input_auth`. Malformed
  authenticated rows, values, orders, equations, ranges, and overflows are
  `input_schema`.
- Descriptor 8 remains an independently authenticated source of candidate
  identities and ranks only. It cannot supply, imply, or replace a packet
  counter.

The D05 phase summary inserts these exact keys after
`global_order_checks`:

```text
carry_raw_hits
carry_global_order_checks
packet_raw_hits
packet_global_order_checks
```

The inherited `raw_hits` and `global_order_checks` fields and the four new
fields are canonical unsigned JSON integers. Discovery uses zero carry.
Held-out uses the authenticated discovery packet totals. Both phases obey
the exact sum identities. All packet totals are at most 131,072. Successful
held-out output records the authenticated carry and final totals. Both
public replay modes recompute the applicable six values.

## Online cap audit

The two inherited limits remain exactly:

```text
MAX_RAW_HITS_TOTAL             131072
MAX_GLOBAL_ORDER_CHECKS_TOTAL  131072
```

They remain cumulative across discovery and held-out. They are not reset at
the phase boundary.

- A proper ranked endpoint checks `packet_raw_hits==131072` before the next
  increment and before every later action for that hit. The abort therefore
  precedes relation work, scoring, certificates, endpoint-checksum output,
  diagnostics, summary mutation, and output extension.
- A large registered mixed-order check tests
  `packet_global_order_checks==131072` before the next increment. The abort
  precedes exponent construction, pair powering, gcd work, record mutation,
  and output extension.
- Equality is sufficient because each authenticated starting value is at
  most the cap and each successful charge adds exactly one.
- Neither failure truncates, samples, splits, or seals output. The failed
  root is not evidence.

## Descriptor, argv, replay, and firewall audit

The six exact open-descriptor sets are mutually closed and match their six
exact command lines:

```text
self-test          2,10
benchmark          2,9,10
discovery          2,3,4,5,6,7,9,10
heldout            2,3,4,5,6,7,8,9,10,11,12
replay-discovery   2,3,4,5,6,7,8,9,10
replay-heldout     2,3,4,5,6,7,8,9,10,11,12
```

Held-out and replay-heldout each contain the exact fd-11, fd-12, and trusted
discovery-manifest-hash options. The other four argv forms remain exact.
All options retain separate values, fixed order, canonical descriptor
digits, lowercase 64-byte hashes, and no repetition, reordering, extra
element, `--option=value`, path fallback, environment fallback, or literal
counter input.

The containment schema appends descriptor keys 11 and 12 after
`status_fd`, and keeps `deployment_contract_sha256` last. The exact five
tail descriptor values are `8,9,10,11,12`.

The discovery manifest and summary are public evidence. They contain no
private fixture, factor, cohort, local character, label, or lead field. The
runner retains the authenticated discovery-manifest hash with the selection
seal. Held-out imports only its two packet totals. Replay-heldout imports the
same carry from the same authenticated bytes. Both public replay PASS
records and the same discovery-manifest hash remain prerequisites to any
post-classification private-label access. The label role cannot write,
replace, reinterpret, or repair the carry artifacts.

## Self-test and failure-status audit

The self-test PASS field `checks` is the exact ordered JSON array:

```json
["candidate_source_counts","pair_multiplication","endpoint_matrix_identity","split_nonsplit_examples","target_chart_controls","f278_half_order_example","input_invariant_factors","orbit_offsets","mixed_bounded_phase","uniform_projective_counts"]
```

These tokens map in order to the ten inherited required self-test groups.
A PASS has all ten and no prefix, duplicate, reordering, unknown token, or
optional token. The other fixed PASS values and key order are complete. A
self-test failure uses the controlled-failure schema, exit 69, and
`self_test`.

The controlled-failure vocabulary is disjoint and total for the evaluator:

```text
64  cli
65  descriptor,input_io,input_auth,input_schema
66  output_exists,serialization,output_cap,output_io
67  arithmetic,replay
68  workload_cap,raw_hit_cap,global_order_cap,memory_cap,
    control_shortfall,thread_resource
69  self_test,benchmark
70  internal
```

The exit-66 distinctions separate existing names, invalid canonical bytes,
valid bytes that cross a cap, and later operating-system output failures.
The exit-68 distinctions separate fixed-workload caps, the two online
packet counters, memory, three-attempt control exhaustion, and exact
four-thread resource failures. No token belongs to two exits.

The fail-fast precedence is one exact total order. It puts descriptor and
input failures before output work, serialization before output size, each
online cap before its protected action, and memory allocation failures
before `internal`. A status-channel failure cannot emit a second controlled
record. It exits 70 without a valid status line. The inherited single-write,
partial-write, `EINTR`, final-LF, and 65,536-byte rules remain exact.

## Preserved mathematics, resources, and authority

D05 changes no algebra. The endpoint remains `F=P_B-v*Q_B`. The residual
exponents remain `s+chi_p` and `chi_q-h`. Negative powers remain
`(P_k,-Q_k)`. Exponent zero remains `(1,0)`. The finite box remains `K=16`.
The probability statement remains conditional only on `A_ctrl`. The only
positive evidence token remains `box_unexplained_exclusive` relative to the
registered finite box.

The additional descriptors and four summary integers do not change any
row, source, candidate, control, diagnostic, certificate, replay, or output
record maximum. They add no evidence file. The inherited JSON per-file cap
already covers the longer summaries. The inherited artifact-read bound and
fixed overhead cover authentication of these already bounded public files.
The 281,186,304-byte successful-output bound, 536,870,912-byte hard cap,
14,400-second wall gate, 25-percent virtual-memory projection, and 4 GiB
memory gate remain unchanged. A cap or resource abort remains nonevidence.

D05 preserves the D04 noncircular build and validation stages. This PASS
permits only drafting `f279_public.cpp`. It does not choose deployment
inputs or authorize either future private/deployment source role. No source
was created. Nothing was compiled or executed. No private label, remote
host, or ledger was accessed. No file was staged or committed.
