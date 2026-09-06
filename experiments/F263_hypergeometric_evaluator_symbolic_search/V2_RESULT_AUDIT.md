# F263-D02 V2 result audit

## Decision

**PASS.** The retrieved F263-D02 V2 result is byte-authenticated and conforms
to the frozen V2 protocol. The finite lead decision is **NULL**: no selected
candidate passes the lead gate. This result does not prove a lower bound.

The strongest finite interpretation is sharper than a generic null. At
40--60 factor bits, the complete 148-candidate grammar finds a proper divisor
only in the consecutive-prime cohort. Every one of those moduli factors in
one public Fermat trial. No random, safe-safe, or bounded-capacity held-out
row has a proper hit. The apparent non-direct hits are also confined to these
one-trial Fermat cases and to public block lengths next to the small prime
gap. They are not evidence for a general evaluator.

## Authentication

Authentication preceded result interpretation.

```text
V2_FROZEN.sha256                  2a41fb0ca76955522843fdc0b15c69b1b2d811a3ac79021b0518bf6da9224271
V2_HOSTILE_PRERUN_AUDIT.md       c4f7ce5b506574e7f501999e4a10d77c9c39bb26a2bbf265322940e0a8cad397
retrieved F263-D02.manifest      f8a352f85b373b9310b231a055e9594f60f4219cf4e1b30bcf51322a7206b1ee
frozen production source         05c0b87a453eb3c2c40c01bf058b0559a6ff2e9b943d16ddcf68d147b1f4c827
remote production binary         d8ce872f62c3c488bf22b29899423caad2f287279db144a6488227771766420a
```

`shasum -a 256 -c V2_FROZEN.sha256` passes for all 17 entries. The
retrieved manifest repeats the frozen packet, source, runner, manifest, and
binary hashes. Every retrieved output and every retrieved non-manifest log
matches its manifest entry:

```text
discovery rows                    fa2290d7b35625ce45008baf5c63d4d6e451f6022c44f9157a2751f80686a2b7
discovery summary                 1e7911ef79531e79479b323bc7ed46d177dcc58bff9cd6989480ca17a90deff4
selection                         86207ddc1654623888c24f31cd2ea982fb0f622fab308432bcad3d0a22c8efa8
held-out rows                     58b1e1ebde26af9ccdca43449fafff6d1737c932ceb2c3f9849571919c0f10a1
held-out summary                  95bb89d57c6a45cc964c70ec57db7c95f8fc5e0dfcd96d5e3df4c005559f46cb
held-out lead gate                ad6a59e572c95b6d362fa05539c478f1437c85da8ed3d63281c1230ab0d0f436
selection hash log                469962333d46961ed35000f51b00bc651b47eefd3bee6b7d404e201a44fb81fb
resource snapshot                 6c269adacb624569abd4227b33fb1756be1c537713b14cefdb174fecb070fa2f
self-test stdout                  a704f95947f722b1a4df485d8f89b6335b390c5459bbbe3a9737e33e0e77f81c
all empty stderr/stdout streams     e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The manifest excludes itself by construction. Its hash above identifies the
retrieved copy; all artifacts that it is meant to authenticate match it.

## Independent row and bitset reconstruction

A separate read-only parser decoded the 37 hexadecimal nibbles in source
candidate order, least-significant bit first. It reaggregated all 2,000 rows
and all 148 candidates without using either JSON summary.

For every row it independently checked:

- canonical field syntax, `N=pq`, exact factor and modulus bit lengths;
- deterministic 64-bit primality of both factors, `p<q<2p`, and global
  modulus uniqueness;
- the exact cohort counts, index ranges, consecutive-prime condition,
  safe-safe halves and capacity two, and bounded capacity at most 16;
- `B=floor(sqrt(N))`, `H=floor(B/2)`, parity, cleanup gcd, and capacity;
- the public query lengths and starts from `bitlength(N)`, exact query and
  leaf counts, and central and shifted coverage;
- disjoint proper and saturated bits, and non-direct bits as a subset of
  proper bits;
- all root, tree, oracle-path, recomputation, and coverage control fields;
  and
- first-witness divisor, support syntax, leaf bound, and direct flag.

The reconstructed cohort sizes are exact:

```text
discovery: 848 = 272 at 16 bits + 288 at 24 bits + 288 at 32 bits
held-out:  1152 = 288 at each of 40, 48, 56, and 60 bits
```

There are 10 discovery cleanup rows and 8 held-out cleanup rows. All cleanup
rows have empty candidate bitsets and no numerical work. The parser's 148
per-candidate aggregates equal both JSON summaries exactly. No row has a
saturated final status. The discovery and held-out symbolic objects are
exactly equal as parsed objects.

## Selection and lead gate

The exact selection bytes hash to
`86207ddc1654623888c24f31cd2ea982fb0f622fab308432bcad3d0a22c8efa8`.
The independent ranking by hostile hits, proper hits, size count, and syntax
reproduces all 64 rows, fields, ranks, and their order.

Held-out evaluation still covers all 148 candidates. The selected 64 capture
all 248 held-out rows with a proper hit and all 67 rows with a non-direct hit.
The other 84 candidates add no held-out hit. Thus this run has no selection
loss.

The independent lead-gate reconstruction matches all 64 output rows:

```text
gate 1, at least 16 proper rows:                  16 candidates
gate 2, size, high-size, and hostile coverage:     0 candidates
gate 3, at least one non-direct row:                6 candidates
gate 4, authenticated operational target:           0 candidates
all four gates:                                     0 candidates
```

Gate 4 is empty because symbolic discovery authenticates no operational
parent target and no unit-target dyadic recurrence. Every final `pass` bit is
zero.

## Symbolic result

Both phases report the registered symbolic result:

```text
columns=70, ranks=58,58, nullities=12,12
signed halves=9801, signature classes=9193, exact rows=192
sparse relations=14, small basis relations=12,12, controls=12
operational shortcuts=0
adjacent recurrences=4, all full_scan and non-unit-target
dyadic recurrences=0
```

All 14 sparse relations are authenticated merge controls. Their dependency
audits reject them as recursive merges or as having two parent targets. The
five non-operational controls and their classes match the preregistration.
This is an authenticated finite symbolic null, not a proof that another
grammar cannot evaluate the block.

## Held-out pattern

The held-out row result has a simple cohort split:

```text
cohort                         rows   rows with any proper candidate
random                          512                                0
safe-safe                       128                                0
bounded capacity <=16           256                                0
consecutive primes              256                              248
```

The other 8 consecutive-prime rows exit through cleanup with `B=p`. For all
256 consecutive-prime rows,

```text
B + 1 = (p + q)/2.
```

Therefore one Fermat difference-of-squares trial factors every positive row,
including every cleanup, direct, and non-direct hit. Their prime gaps range
from 2 through 192.

The dominant direct candidates are the expected singular-block controls:
`central.u0` and all three central transfer determinants hit 248 rows;
`shifted.v0` also hits 248; four adjacent shifted-denominator controls hit
239. Their retained support contains the true singular index.

Exactly six candidates have held-out non-direct hits. Their complete pattern
is:

| Candidate | Rows by factor bits 40/48/56/60 | `s=B-p` values | `q-p` values |
| --- | --- | --- | --- |
| `shifted.u1` | 11/11/7/4 | 9, 10, 17, 18 | 20, 22, 36, 38 |
| `shifted.v1` | 11/10/5/8 | 7, 8, 15, 16, 31, 32, 63, 64 | 16, 18, 32, 34, 64, 66, 128, 130 |
| `shifted.jet_det02` | 7/3/4/4 | 9, 17 | 20, 36 |
| `shifted.transfer_f0` | 7/3/4/4 | 9, 17 | 20, 36 |
| `shifted.transfer_r0` | 7/3/4/4 | 9, 17 | 20, 36 |
| `shifted.transfer_det01` | 4/8/3/0 | 10, 18 | 22, 38 |

These 136 candidate-row incidences have a union of 67 rows. Every one is a
consecutive-prime row. The `s` values sit at a power-of-two query boundary or
one or two positions next to it. No non-direct hit survives on a random or
hostile held-out modulus. This is a small-gap boundary effect, not a genuine
gain over the public Fermat screen.

## Bounded exact witness checks

A separate exact evaluator checked representative supports, not only their
stored bits.

- Cleanup: held-out 40-bit consecutive row 8 has
  `p=1004300281109`, `q=p+2`, `B=p`, and `gcd(B,N)=p`.
- Direct: on 40-bit consecutive row 7,
  `p=880583251871`, `q-p=36`, and `B-p=17`. The central block
  `[440291625928,440291625944)` contains `(p-1)/2` and its `u0` gcd is `p`.
  The shifted block `[0,32)` contains shifted index 16 and its `v0` gcd is
  `p`.
- Non-direct on the same row: the shifted block `[0,16)` excludes index 16,
  but `jet_det02`, `transfer_f0`, and `transfer_r0` each have gcd `p`.
  A right-edge shifted block of length 16 also gives a non-direct `u1` gcd
  of `p`.
- Second non-direct orientation: held-out 40-bit consecutive row 5 has
  `q-p=18` and shifted index 7. Its right-edge shifted block of length 8
  excludes index 7, while `v1` has gcd `q`.

These checks confirm that the non-direct labels are literal support labels.
They also expose the power-of-two boundary mechanism behind the finite hits.

## Output and resource gates

The output directory has exactly the six registered, nonempty files. Row
files have 848 and 1,152 data rows. Selection and lead files each have 64
data rows. All files end in one newline and both summaries parse as JSON.
Their file payload is 761,647 bytes. The remote `du -sb` value in the
manifest is 761,893 bytes including directory storage, far below 1 GiB.

The authenticated runner reports:

```text
start_utc=2026-08-13T17:30:27Z
end_utc=2026-08-13T17:37:41Z
discovery_status=0
heldout_status=0
```

Elapsed wall time is 7 minutes 14 seconds. Compile and both phase streams are
empty. The algebra self-test passes. The frozen runner applies eight threads,
`nice 15`, one shared four-hour deadline, a 4 GiB virtual-memory cap, and a
1 GiB file cap. The pre-run snapshot records 32 CPUs, load
`55.62 56.82 57.63`, 367 GiB available memory, and 22 GiB free disk. The
authenticated overlap checks and exact output-set gates completed with
status zero.

## Evidence boundary

This audit authenticates one deterministic finite run. It rejects this
frozen symbolic and numerical grammar as a useful general lead at the tested
sizes. It does not prove that the gate lacks a different numerical-QP
evaluator, and it does not prove an all-input factoring algorithm.
