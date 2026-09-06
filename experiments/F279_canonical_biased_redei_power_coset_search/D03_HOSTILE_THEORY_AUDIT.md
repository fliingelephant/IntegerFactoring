# F279-D03 fresh hostile theory audit

## Verdict

**STRICT PASS.**

The authenticated D03 pair is a coherent additive repair of the authenticated
D02 pair. I found no mathematical, evidence-interface, serialization,
containment, resource-accounting, or authorization blocker.

This is a theory-only PASS. It does not authorize fixture or tape creation,
compilation, self-tests, benchmarks, experiments, remote access, private-label
access, ledger changes, git staging, or commits. The later implementation and
containment packet still needs its own immutable freeze and hostile static
PASS. An experiment still needs explicit user authorization.

## Authenticated inputs

I authenticated the D03 files before I read them.

```text
D03_DRAFT_ALGEBRA.md
d9f2fa7c490b96214e976478740257b0e6cc675f20bf7f7219760e4ca450e159

D03_DRAFT_PREREGISTRATION.md
6b5f1633e2cf2654adb8ec8bb2f79bf84a242550ef57cb4dc6cf964013413a1b
```

I also authenticated and read the complete predecessor chain.

```text
DRAFT_ALGEBRA.md
328c8c26d5c06e3033300539fd5900f7ddcb55f253b75fae851c58db47eea424

DRAFT_PREREGISTRATION.md
4498a4f3e2404297d6eda58036fc45e097915a13d73077dc9511dea4e6cb7e7e

D02_DRAFT_ALGEBRA.md
f87f787bad0943b7149d276e158d28a6350dc8ab72836e80112acf33240cf843

D02_DRAFT_PREREGISTRATION.md
93e207fb2e3e4c489eb009f56e16751b3df79d7ecc329b602a678761795533f9
```

The hashes agree with the D03 ancestry block. I applied the stated additive
merge rule. I did not treat D03 as a standalone replacement.

## Mathematical audit

- The chart repair is exact. For `D=diag(b,1)`, direct multiplication gives
  `D^(-1) C D=[[a,1],[bc,d]]`. The clean condition `H=-bc` makes `b` and
  `c` units. Diagonal conjugation preserves the upper-left entry of every
  power.
- The endpoint sign is `F=P_B-v Q_B`. It agrees with the literal matrix
  control and with `z^B=lambda` under the stated Cayley coordinates.
- The residual exponents remain `s+chi_p` and `chi_q-h`. The negative- and
  zero-exponent pair conventions have the correct signs.
- ExactTape256 rejection produces a uniform vector on `[0,N)^2`. The two
  gcd acceptance conditions factor over the two CRT components. Every clean
  projective line has the same number of nonzero vector representatives.
- The probability statement conditions only on the product of local control
  success events `A_ctrl`. It does not condition on phase success, runtime,
  replay, checksums, resources, or a lead.
- The `K=16` orbit, torsion, mixed-phase, source-order, powered-collision,
  half-order, and near-square screens remain explicitly finite. The evidence
  label remains only `box_unexplained_exclusive`.

## Evidence-interface audit

- Every named source has one terminal or endpoint-eligible state. Proper
  source-order, `g_Q`, and `g_P` outcomes stop all targets under that source.
  Their total endpoint-stream statuses, classifications, event tokens, and
  slot-count meanings are complete. Global saturations remain eligible
  registered decoys.
- Every one of the 51,200,000 primary ranked candidate slots has one endpoint
  checksum record. Primary plus replay gives 102,400,000 endpoint-stream hash
  records. The control-stream bound is 22,118,400 primary-plus-replay attempt
  records.
- The promise bytes, fixture and tape names, fixed descriptors `3` through
  `9`, discovery closure of descriptor `8`, clean environment, empty working
  directory, UID drop, input manifest, containment trust anchor, and binary
  hashes form one executable public boundary. No path fallback is allowed.
- The input manifest commits both complete tapes, both fixture pairs, both
  promises, the containment manifest, tape provenance, and the held-out seed
  commitment before discovery output opens.
- The discovery and held-out public manifests are complete for their sealed
  public phases. The final evidence manifest commits the later labels, lead,
  replay, reveal, preflight, promises, provenance, and both public manifests.
- There is one consistent chronology: discovery public seal, held-out public
  release and seal, exhaustive public replay, private-label access, label
  replay and lead, replay seal, seed reveal, then final evidence manifest.

## Diagnostic and resource audit

For `D0<=112` and `A0<=12656`, the worst-case primary diagnostic counts are
exactly:

```text
base gcd checks       32*(12656-1)       =    404960
exponent gcd checks   32*(12656-1)*112   =  45355520
primary scan checks                         45760480
primary plus replay                         91520960
```

The diagnostic scan stream, row checksum, target records, literal matrix
checks, full registered relation-box replay, and operation counters cover all
32 diagnostic rows. The endpoint, control, diagnostic-scan, and diagnostic-
target serialization/SHA kernels charge primary work plus exhaustive public
replay.

The output arithmetic is exact:

```text
output_bound_bytes            = 281186304
ceil(5*output_bound_bytes/4)   = 351482880
hard aggregate cap            = 536870912
```

The wall projection keeps the inherited single-core benchmark rule, exact
kernel counts, measured read/write charges, factor-two timing margin, and
14,400-second gate. The capacity test touches the added diagnostic, SHA,
manifest, and counter state. The 25-percent virtual-memory projection and
4 GiB gate remain in force. Tape creation keeps its separate deadline,
memory, provenance, failure, and exact `pread` rules. The containment, live
load, free-memory, disk, lock, process-group, network, UID, and no-local-
production gates remain normative.

## Serialization and generation audit

- The inherited ASCII, LF, TSV, canonical integer, lowercase hash, restricted
  JSON, and unsigned-byte collation rules determine the new records.
- The displayed input-manifest and public-manifest orders agree with unsigned
  byte order. Candidate and source fixed-width IDs preserve numeric order.
- The output cap accounts for all successful record classes, JSON files, TSV
  headers, diagnostic rows, and manifest rows.
- Cohort sizes, row IDs, generator chronology, deterministic primality test,
  cross-phase `N` uniqueness, diagnostic-row flags, selection order, and held-
  out gate remain total and factor-blind.
- `getrandom`, partial returns, `EINTR`, writes, `fsync`, close/reopen hashing,
  no-replacement rename, provenance, commitment, and exact 32-byte `pread`
  failure behavior are explicit. No substitute entropy or tape path exists.

No source was created. Nothing was compiled or executed. No private label or
ledger was read. No file was staged or committed.
