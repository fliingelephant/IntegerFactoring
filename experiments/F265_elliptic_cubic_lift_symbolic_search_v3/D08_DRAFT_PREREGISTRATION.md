# F265-D08 draft preregistration amendment: closed mixed cubic-row bank

## Status and exact composition

This is an unfrozen theory-only amendment. It has not passed a hostile
theory audit. No D08 C++ source, runner, manifest, freeze, compilation,
preflight, local execution, remote execution, discovery cohort, or held-out
cohort exists or is authorized.

D08 imports exactly these immutable draft bytes:

| imported artifact | SHA-256 |
|---|---|
| `D05_DRAFT_ALGEBRA.md` | `e3cbefeb597f263501d327f15f9dd4c7b78ee37d37178135ab1c0a5ff73e9fd3` |
| `D05_DRAFT_PREREGISTRATION.md` | `a62dcb0f7d501778ef1f6092468d38a6ee15c794ec5b609bf145a3d7bf345a35` |
| `D06_DRAFT_ALGEBRA.md` | `e79ea109a9cd8141dd27c4fc99cc7ec2957c454619b0e015802ab4eff5c45f74` |
| `D06_DRAFT_PREREGISTRATION.md` | `67aa6011accffedbed24d0be95614e481f006b80f163a6b5e831dc4fafef6754` |
| `D07_DRAFT_ALGEBRA.md` | `fbc4831cb4f11f849a779bf165cbedf2e6a3e8140228ba40b0d01ec103a2abbf` |
| `D07_DRAFT_PREREGISTRATION.md` | `2151d3549be3322de14d6e787f87a210bb6c0721c9fedfcc8397457a7d0c4fc1` |
| `D08_DRAFT_ALGEBRA.md` | `3af4a847ab65f9acde05ffd2ea98f4d5cee143c0162f915284b599e8fe007839` |

The immediate D07 draft received a conversation-only hostile `REVISE`.
There is no audit artifact and no audit hash. The review accepted the
mathematical core and gave exactly four repair classes: resolve duplicate
curve acceptance, restore `T_square64`, totalize every factor/diagnostic byte
and status field, and replace sampled `cpp_int` remainder dominance with a
genuinely source-enforced operation envelope. D08 addresses only these
classes and byte-level inconsistencies found while closing them.

The complete transitive D02 boundary remains:

| D02 artifact | SHA-256 |
|---|---|
| `../F265_elliptic_cubic_lift_symbolic_search_v2/FROZEN.sha256` | `26f7940244242edc549a2612fc08120372e0f8fab64a2dca154b69ed02d55d6a` |
| `../F265_elliptic_cubic_lift_symbolic_search_v2/ALGEBRA.md` | `d20b5271bb4441fe7d280e35e09a73ff5b0142abf2ed6d3e9839fe22ff4914c4` |
| `../F265_elliptic_cubic_lift_symbolic_search_v2/PREREGISTRATION.md` | `8e3c90420014939ba3ae58490bac2e85fc0a7a45523e12d332cadb5e1f6b384f` |
| `../F265_elliptic_cubic_lift_symbolic_search_v2/search.cpp` | `eeceba4db014346cc78dae3cbae29a65fb32946163becc5d9f5617fc465a7957` |

There is no token rebinding or unnamed priority rule. Form the normative D08
contract as follows.

1. Form the exact D07 composite by its literal composition map.
2. Replace D07's proposed D02-equivalence sentence for curve selection by
   D08 Section 1.
3. Keep D07 Section 2.1. Replace the coordinate and nonce rules in D07
   Sections 2.2 and 2.3 by D08 Section 2.
4. Replace D07 Section 3 by D08 Section 3.
5. Replace D07 Section 4 and the inherited D06 long-gcd charge by D08
   Sections 4 and 5.
6. Keep D07 Section 5, with its duplicate variants interpreted by D08
   Section 1.
7. Replace the surviving D06 production-width diagnostic fixture by D08
   Section 6. Keep D07's 20-field task and 14-field status schemas, now with
   the frozen fixture keys and corrected digests in D08 Section 6.
8. Keep D07's raw projection formula, with `rho_decoder` replaced by D08
   Section 5.3. Remove `EUCLID_MOD_STEPS_361_MAX`, `rho_mod361`, and
   `rho_dgcd` from the normative projection.
9. Keep every other surviving D05/D06/D07 seed, cohort, firewall, screen,
   counter, cap, output, memory, timeout, sticky-factor, label, diagnostic,
   and finite-scope clause literally.
10. Replace the prior audit gate by D08 Section 8.

If this ordered construction has any conflict not resolved by the listed
replacements, the composition fails audit. A source author may not choose a
clause silently. A later standalone draft must materialize the resolved text
and authenticate all seven inputs before source is written.

### Draft self-audit disclosure

During unfrozen D08 drafting, the first fixture calculator accidentally
hashed the two-byte printable sequences backslash-`t` and backslash-`n`
instead of byte 9 and byte 10. The mistake was found by comparing the claimed
one-line lengths with the literal Markdown code-block bytes. None of those
candidate hashes was frozen, executed, or used as evidence.

The discarded `(byte count,SHA-256)` pairs were:

- factor stream `(624042,e5851fda850a23aed58e09e7625e226d5bf2c0c5e2ab600b2aab485f0270e9e7)`;
- factor summary `(114,b83bc1a9f07cc0758508ca6e933d7009ebafc2c067504c4d9a7c83fcaad3789f)`;
- affine event `(129,64f3ebabc2f9097f19ea56a1a01a47d8f3118cd5317e83e5c4f5d0a7beec9467)`;
- gcd stream `(3576986,4433fc035eca0069c444650a24732caafa3a148d1dc622afbe7291dc39807c44)`;
- diagnostic row stream `(not recorded,a29f8b67d93ff7b0e682fbd1b107216546347a6c9aacf59aa2ed15b55de16e7d)`;
- diagnostic task stream `(912840,ee07b6ca11040488e731ee6f4ddac5b11a37bbaf321a0e41b9d9ee22fcb1b32d)`; and
- diagnostic status `(138,13fcdbcfddf53f8112a49f6fda1a454bad4997df8ad2a202ede6007ce5e8cf8a)`.

The normative values below were reconstructed independently in Python and
Ruby with separators created from numeric byte values 9 and 10. A third
independent JavaScript `BigInt` reconstruction, using Node's cryptographic
SHA-256 implementation and the same numeric byte construction, matched every
normative byte count and digest, including the fixed-gcd checksum. This
disclosure is provenance, not an experiment result.

## 1. Curve acceptance and the exact D02 exception

The D05 bank grammar controls curve acceptance. Within one bank, curve 0
owns its accepted clean tuple `(A,B,x0,y0)`. A later clean proposal for curve
1 that has the same complete tuple consumes one curve-1 attempt and is
rejected as `DUPLICATE_CURVE_TUPLE`. The table is bank-local and is empty at
the start of every bank. It has no cross-bank effect.

For a fixed draw stream, the derived D08 curve routines preserve D02's draw
values, `A,x0,y0,B`, discriminant gcd, affine arithmetic, and factor result
on each reached attempt. They preserve D02's `B=0`, full-discriminant,
proper-factor, and clean acceptance decisions except for exactly one new
decision: a D02-clean tuple is rejected when it duplicates an earlier clean
tuple in the same bank. This duplicate rejection is explicitly exempt from
D02 acceptance equivalence. There is no other exemption.

The frozen duplicate fixture uses

`N_factor=735592564497057472472983056100764157`.

It first feeds the `U` stream `A=2,x0=1,y0=1`, then feeds the `POWER`
stream `s=1`. Both proposals give

`(A,B,x0,y0)=(2,735592564497057472472983056100764155,1,1)`.

The fixture asserts `gcd(140,N_factor)=1`. Curve 0 accepts the tuple. The
first curve-1 attempt reaches the clean duplicate check, consumes the
attempt, emits no factor event, and continues. The same shared production
body is used by D07's full 32-attempt duplicate variants.

The future lineage table marks `choose_curve` as `DERIVED` and names this
duplicate check as the sole curve-acceptance difference from D02. All other
production random values and curve/affine results remain identical for the
same reached draws.

## 2. Total factor metadata, nonce, and status contract

### 2.1 Factor-size fields and bank nonce

`factor_bits` is the actual prime-generator argument in the frozen menu
`12,16,20,24,32,40,48,60`. It is not a bit rank. A generated factor labeled
with `factor_bits=b` satisfies `2^(b-1)<=p,q<2^b`; the hidden values `p,q`
never enter a public event byte. `bits_rank` is only the index `0,...,7` of
`factor_bits` in that menu and is the value serialized in a slot summary or
diagnostic line.

For every slot, including a shortfall, define

`bank_nonce = low32(seed_key({split_code,factor_bits,shape_code,case_index}))`.

All four tuple entries are converted to `uint64_t`. `seed_key` is the exact
D05 function with master seed `0x0F265D05C0DEC0DE`. `split_code` is 0 for
discovery, 1 for heldout, and 2 only for a preflight fixture. `shape_code` is
0, 1, or 2. The nonce uses the actual `factor_bits`, never `bits_rank`.

### 2.2 Complete class-to-coordinate table

The D07 15-field event line and numeric widths survive. The following table
completely determines `curve_id,row_1,row_2,mask_present` and the mask words.
`NO_CURVE=NO_ROW=65535`. Pair row IDs are increasing. An affine doubling can
repeat one row ID.

| class | `curve_id` | `row_1,row_2` | mask |
|---|---|---|---|
| `CURVE_DISCRIMINANT` | attempted curve 0 or 1 | `NO_ROW,NO_ROW` | absent, five zero words |
| `FACTOR_X_SIGN` | common operand curve | increasing distinct operand row IDs; doubling is not this call site | absent, five zero words |
| `AFFINE_DENOMINATOR` | common operand curve | increasing operand row IDs, or the repeated ID for doubling | absent, five zero words |
| `ROW_ROOT` | prospective row's curve | prospective row ID, `NO_ROW` | absent, five zero words |
| `SINGLETON` | selected row's curve | row ID, `NO_ROW` | absent, five zero words |
| `PAIR_X` | common curve when same-curve, otherwise `NO_CURVE` | increasing pair row IDs | absent, five zero words |
| `PAIR_Y_MINUS` | common curve when same-curve, otherwise `NO_CURVE` | increasing pair row IDs | absent, five zero words |
| `PAIR_Y_PLUS` | common curve when same-curve, otherwise `NO_CURVE` | increasing pair row IDs | absent, five zero words |
| `PAIR_CHORD` | common curve; cross-curve is not a call site | increasing pair row IDs | absent, five zero words |
| `SUPPORT2` | common curve when same-curve, otherwise `NO_CURVE` | increasing pair row IDs | absent, five zero words |
| `LOW_BASIS` | always `NO_CURVE`, even for one-curve support | `NO_ROW,NO_ROW` | present, exact nonzero relation mask |
| `STRUCTURAL_Q` | always `NO_CURVE`, even for one-curve support | `NO_ROW,NO_ROW` | present, exact nonzero relation mask |

For an affine event, an operand row ID is its deterministic original-bank
slot. Curve-0 IDs are `0,...,K-1` and curve-1 IDs are
`K,...,2K-1`. The base point owns the first slot of its curve. These IDs are
defined even when the failed addition prevents the next output row.

The D07 phase and side table remains exhaustive. In particular,
`FACTOR_X_SIGN` has only side `MINUS`; `PAIR_CHORD` is always same-curve;
and low/structural events always carry a mask and no row or curve metadata.
Schema validation occurs before the sticky journal mutates.

### 2.3 Total status precedence

The D07 status codes survive. Exactly one code is chosen by this precedence:

1. `SHORTFALL` when corpus replay produced no public case for the slot;
2. `RESOURCE_REJECT` when a case existed and any core resource, factor-event,
   writer, memory, output, or wall cap rejected it;
3. `ELIGIBLE` when the complete mathematical core committed under every cap,
   whether or not a factor event occurred;
4. `DIRECT_STOP` when a verified curve, affine, or row factor stopped an
   incomplete orbit and no resource rejection occurred; or
5. `BANK_SKIP` for every remaining non-resource incomplete bank, including
   a full gcd or unresolved global affine exception.

An internal invariant failure aborts the split and produces no held-out
label. It is not mapped to a status code. Sticky `observed`, occurrence,
overflow, first-witness, and digest fields are independent of status. Thus a
factor followed by a resource rejection has status `RESOURCE_REJECT` and
still prevents the all-slot null label; a factor followed by a fully
committed core has status `ELIGIBLE` and also prevents null.

## 3. Byte-complete factor fixtures

Use D07's `N_factor` and

`g_factor=933956397855941843=0xcf6146541e824d3`.

The 4,096-event fixture bank is exactly

`(split=0,factor_bits=60,bits_rank=7,shape=0,index=0)`,

whose nonce is decimal `4093429121`. Let

`Z=0000000000000000`

and let the one present mixed-curve mask be

`M=(0000000000000010,Z,0000001000000000,Z,Z)`.

The following 16 templates freeze every field other than event ordinal,
`g_hex`, and nonce. `S` means decimal 65535. `Z5` means five `Z` words.

| template | phase | class | side | curve | row 1 | row 2 | present | words |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 0 | 0 | 0 | 0 | 0 | S | S | 0 | Z5 |
| 1 | 1 | 1 | 1 | 0 | 4 | 9 | 0 | Z5 |
| 2 | 1 | 2 | 0 | 1 | 164 | 169 | 0 | Z5 |
| 3 | 2 | 3 | 0 | 1 | 164 | S | 0 | Z5 |
| 4 | 3 | 4 | 1 | 0 | 4 | S | 0 | Z5 |
| 5 | 3 | 4 | 2 | 0 | 4 | S | 0 | Z5 |
| 6 | 4 | 5 | 0 | S | 4 | 164 | 0 | Z5 |
| 7 | 4 | 6 | 1 | 0 | 4 | 9 | 0 | Z5 |
| 8 | 4 | 7 | 2 | S | 4 | 164 | 0 | Z5 |
| 9 | 4 | 8 | 0 | 1 | 164 | 169 | 0 | Z5 |
| 10 | 4 | 9 | 1 | S | 4 | 164 | 0 | Z5 |
| 11 | 4 | 9 | 2 | S | 4 | 164 | 0 | Z5 |
| 12 | 5 | 10 | 1 | S | S | S | 1 | M |
| 13 | 5 | 10 | 2 | S | S | S | 1 | M |
| 14 | 6 | 11 | 1 | S | S | S | 1 | M |
| 15 | 6 | 11 | 2 | S | S | S | 1 | M |

For ordinal `o=0,...,4095`, use template `o mod 16`, `g_hex` as above, and
the fixed nonce. The resulting 4,096 LF-terminated lines contain exactly
562,602 bytes and have SHA-256

`b237d6d7c4cc52549fd1a03c7c5535fc005326b19ec2ae91d241d2cdcb622cdc`.

The first line is literally

```text
0	0	0	0	0	65535	65535	0	0000000000000000	0000000000000000	0000000000000000	0000000000000000	0000000000000000	cf6146541e824d3	4093429121
```

and the last line is literally

```text
4095	6	11	2	65535	65535	65535	1	0000000000000010	0000000000000000	0000001000000000	0000000000000000	0000000000000000	cf6146541e824d3	4093429121
```

Each displayed code block contains its final LF. The independent parser must
re-render every line and reproduce the byte count and digest.

The attempted 4,097th call uses template 0. It renders and hashes no bytes,
leaves the digest above unchanged, sets overflow, advances the occurrence
lower bound to 4,097, and has the separately timed throw/catch behavior from
D07. Status precedence then gives this exact one-slot summary line:

```text
0	7	0	0	2	1	4097	4096	1	0	b237d6d7c4cc52549fd1a03c7c5535fc005326b19ec2ae91d241d2cdcb622cdc	4093429121
```

It is 102 bytes including LF and has SHA-256

`bca703c328b0f9f8070e8ef7beb3c856e45196f7cdce2c1661765072c6272c3d`.

The affine `N=35,A=1,B=1,P=(0,1),Q=(0,6)` fixture uses the preflight bank
key `(split=2,factor_bits=12,bits_rank=0,shape=0,index=0)`, nonce
`4143359229`, curve 0, and prospective rows 0 and 1. Its expected event line
is literally

```text
0	1	1	1	0	0	1	0	0000000000000000	0000000000000000	0000000000000000	0000000000000000	0000000000000000	5	4143359229
```

It is 114 bytes including LF and has SHA-256

`e9a6f189dfe788f3fd48afd1a466a13cfbe83e7f8fd8e76e72f396f98181768b`.

The production affine path must journal those bytes before returning the
factor. These fixtures replace D07's underspecified 16 templates and affine
event.

## 4. Fixed-shape P66 gcd primitive

### 4.1 Source contract

Add these literal constants:

| constant | value | type and scope |
|---|---:|---|
| `P66_FIXED_LIMBS` | 6 | `uint8_t`, one fixed operand |
| `P66_BINARY_ROUNDS` | 722 | `uint16_t`, one fixed gcd call |
| `P66_GCD_CALLS_PER_BANK_MAX` | 9,386,560 | `uint32_t`, one decoder |
| `P66_GCD_CALLS_PACKET_MAX` | 7,208,878,080 | `uint64_t`, 768 decoders |
| `P66_BINARY_ROUNDS_PACKET_MAX` | 5,204,809,973,760 | `uint64_t`, full packet |

Remove `EUCLID_MOD_STEPS_361_MAX` from the normative D08 constants.

The residual decoder stores each positive block value in a canonical
six-limb `U361` beside the exact `cpp_int` used for split divisions and row
reconstruction. At initial-block or split-result construction, one fixed
six-limb converter validates positivity, the 361-bit cap, upper padding, and
agreement between the two representations. A validation failure is an
invariant failure, not an ordinary resource rejection. No conversion or
validation is repeated inside a block-pair comparison. Its construction cost
is inside the surviving exact split/result-construction fixtures. Every
refinement comparison and every
final pairwise-coprimality comparison calls the exact
`p66_gcd361_fixed(U361,U361)` primitive from D08 Algebra. No P66 comparison
may call D02 `gcdz`, Boost gcd, GMP gcd, `%`, or `/`.

The primitive executes exactly 722 rounds for every input pair, including
the total zero-input self-test lanes. All scans, both subtractions, offset
candidates, shifts, and mask selections execute in every round, including
the absorbing equal-state suffix. A
future compiled-source audit must inspect the emitted function and reject it
if it contains an input-dependent branch, input-dependent address, call,
allocation, division, or remainder. Benchmark injection cannot change this
body.

### 4.2 Correctness and rate fixture

The exact correctness cycle contains these four ordered pairs:

1. `(F_520,F_521)` with `F_0=0,F_1=1`, expected gcd 1;
2. `(2^360,2^359)`, expected gcd `2^359`;
3. `(2^361-1,2^360+1)`, expected gcd 1; and
4. `(2^360+12345,2^360+12345)`, expected gcd `2^360+12345`.

Assert operand widths `(360,361)`, `(361,360)`, `(361,361)`, and
`(361,361)`. A correctness repetition makes 65,536 calls, using pair
`o mod 4` at ordinal `o`. Outside the timed interval, serialize

`ordinal<TAB>gcd_hex<LF>`

for all returned values. The 3,445,914-byte stream has SHA-256

`d7ba2d8c604546d8f6c5ae2ba9da7a8962e6b9d14fe3d3d5ed97c4c3df26dd66`.

Run eight timed repetitions. Each includes the same 65,536 primitive calls
and a fixed six-limb checksum of every return, but excludes stream rendering
and SHA. The four input pairs reside in a volatile six-limb array, every call
reloads its selected pair, and the primitive is a non-inlined production
symbol. The emitted-object audit must confirm that the timed loop calls that
symbol 65,536 times and that no input or return was constant-folded.

The checksum starts at `0x0F265D08C0DEC0DE`. For ordinal `o` and returned
little-endian limb `j=0,...,5`, update in this order

`checksum = mix64(checksum xor limb_j xor mix64(6*o+j))`.

The exact D05 `mix64` is used. After one repetition the checksum must be
`0xcf6349190001c459`. The checksum is committed after timing, so none of the
calls can be dead-code-eliminated. Define

\[
 \rho_{\rm p66gcd}={\max T_{\rm p66gcd65536}\over65536}.
\]

Because every permitted input executes the same fixed-width instruction
schedule, this is a rate for the production primitive itself. It is not a
sampled claim that selected `cpp_int` quotient shapes dominate other shapes.
The global 1.75 multiplier remains the host-noise safety margin.

The source self-test must also compare the primitive with exact mathematical
gcd on zero, one-zero, equal, even/even, even/odd, maximum-width, power-of-two,
consecutive-Fibonacci, and a frozen independent pseudorandom corpus. It must
assert zero upper padding in every returned nonzero value. Those correctness
tests do not enter the runtime rate.

## 5. Restored cap-complete decoder suite

### 5.1 Surviving fixtures

Preserve the D06 exact 20,000 split fixture, the exact one-million failed
refinement loop, and the full 4,096-block dense-and-sparse terminal fixture.
They now call `p66_gcd361_fixed` at every P66 comparison. Keep their complete
loop, branch, counter, container, reconstruction, parity, kernel, and cap
assertions. Their times remain `T_split20k`, `T_refine_loop1m`, and
`T_terminal_sparse4096`.

The D07 256-pair `cpp_int` remainder fixture, `rho_mod361`, the D06 isolated
Fibonacci `rho_dgcd`, and every 724-times-sampled-remainder projection term
are removed. They cannot calibrate or substitute for the fixed primitive.

### 5.2 Complete restored `T_square64`

For `i=0,...,63`, set

\[
 w_i=181\cdot2^{173}+2i+1,
 \qquad a_i=w_i^2.
\]

Assert that every `w_i` is positive and odd, every `a_i` has exactly 361
bits, and the input has exactly 64 rows. Inject these exact rows at the same
production peel boundary used by a residual bank. The fixture must execute
the exact simultaneous peel, P66 refinement, terminal verification, parity
builder, canonical kernel builder, and integer-square verifier. It asserts:

- the first simultaneous peel round deletes no row and is terminal;
- all 64 rows survive;
- exact row reconstruction holds;
- every non-square opaque block has an all-even exponent row, so the retained
  parity matrix has rank zero;
- the canonical kernel has dimension 64 and is the 64 unit masks in original
  row order; and
- every unit-mask relation has exact positive root `w_i`.

Run the complete fixture four times and let `T_square64` be the largest wall
time. Its P66 construction necessarily performs and validates the maximum 64
initial `cpp_int`-to-`U361` conversions. The split fixture similarly includes
all `U361` construction for split results. No benchmark-only shortcut may
bypass a surviving production stage.
This section restores the definition accidentally removed by D07's
composition map.

### 5.3 Decoder charge

One bank can perform at most

\[
 1{,}000{,}000+\binom{4096}{2}=9{,}386{,}560
\]

P66 gcd comparisons. Each comparison executes 722 fixed rounds, or at most
6,777,096,320 fixed rounds per bank. Across 768 intended banks this is
7,208,878,080 fixed primitive calls and exactly 5,204,809,973,760 fixed
rounds. The registered per-bank decoder charge
is

\[
\begin{aligned}
 \rho_{\rm decoder}={}&T_{\rm split20k}+T_{\rm refine\_loop1m}
 +T_{\rm terminal\_sparse4096}+T_{\rm square64}\\
 &+9{,}386{,}560\rho_{\rm p66gcd}.
\end{aligned}
\]

The loop and terminal fixtures already execute their fixed gcd calls. The
last term deliberately charges every permitted call a second time. If the
exact suite or conservative projection cannot fit the
surviving 1,800-second preflight and 12,600-second production gates, the
packet stops. No smaller post-timing formula is permitted.

D07's raw formula survives with this `rho_decoder`. All other curve,
generation, relation, RREF, factor, commit, diagnostic, and I/O terms remain.

## 6. Fully keyed production-width diagnostic fixture

This section replaces the surviving D06 diagnostic fixture and supplements
D07's byte schemas. Use the same literal

`N_diag=1329227995784915872903807060280344457`, `A=2`, `B=2221`, and
`P=(N_diag-2,N_diag-47)`.

Generate `P,2P,...,16P` with the exact D02 `add_points` trace. Use original
row IDs `0,...,15`, scalar indices `1,...,16`, and curve ID zero. The bank
tags are exactly

`split=2,bits_rank=7,shape=0,index=127`.

The eight tagged supports use `basis_ordinal=0,...,7`. Within each support,
generate the 120 pair tasks and 1,680 anchored-third tasks, then order all
14,400 lines by the surviving D07 total key. Pair and third-row predicates
use scalar indices, not original row IDs.

Before timing, assert all D06 curve, discriminant, denominator, unit-root,
congruence, distinctness, and 354-through-360-bit row conditions. The exact
16-line stream

`scalar_index<TAB>u<TAB>v<TAB>a<LF>`

has SHA-256

`e8a5018e7f5b7cf4659d6061a82cfaa33c999580b1a089b5e9e427dcca4315a0`.

This byte recomputation confirms the inherited D06 row digest. D08 freezes
the previously missing fixture tags and the complete task/status bytes below.

Render every task by the D07 20-field schema. The complete 14,400-line task
stream is 624,840 bytes and has SHA-256

`3617fd351c0e3dedcb28af4def708a8f7daeffe107e45bfff58e3ca6c9701419`.

Its first line is literally

```text
2	7	0	127	0	0	0	0	1	65535	1	1	1	2	2	2	2	2	2	2
```

and its last line is literally

```text
2	7	0	127	7	1	0	14	15	13	1	1	1	0	0	0	0	0	0	0
```

Each displayed code block contains its final LF. The fixture retains exactly
the first 64 task lines. Its complete status line is literally

```text
0	14400	3617fd351c0e3dedcb28af4def708a8f7daeffe107e45bfff58e3ca6c9701419	255	255	255	65535	255	255	255	65535	65535	65535	64
```

It is 124 bytes including LF and has SHA-256

`b4ea9bd6429e20d0080147e5cdd6df4e31dcc6d98537701e79c45160f84ac486`.

A second parser must byte-identically re-render all task and status lines and
reproduce every byte count and digest before timing. Run the exact production
diagnostic function 16 times as in D06 and retain the same definition of
`rho_diag`. Fixture parsing and hashing are outside that timer but inside the
preflight wall and artifact caps.

Production diagnostic lines still use split 0 or 1 and case indices 0
through 15. Split 2 and index 127 are reserved fixture tags and cannot enter
a production result.

## 7. Rechecked closure and finite scope

The conversation-only D07 hostile review, which has no artifact hash,
verified the unchanged static totals:

- 12 factor classes and 16 legal class/side templates;
- 3,145,728 hashed factor-event calls plus at most 768 overflow attempts;
- 49,152 curve attempts, 98,304 `random_below` calls, and 402,653,184 inner
  sampling iterations;
- 11,059,200 diagnostic tasks;
- 588,251,136 final bytes; and
- 750,780,416 peak experiment-directory bytes.

D08 changes no one of those totals. The fixed gcd fixture stream and the
corrected diagnostic fixture stream are preflight artifacts inside the
surviving 134,217,728-byte preflight category. No production output category
or memory allowance changes.

The sticky all-intended-slot null quantifier, relation-certificate staging,
factor-label firewall, corpus disjointness, post-commit diagnostics, and
coverage floors survive. D08 remains a finite experiment contract. The peel
is only a source-agnostic decoder optimization. There is no elliptic source
success theorem, probability statement, residual-core theorem, or all-input
factoring claim.

## 8. Audit and authorization gate

Before source is written, a fresh no-context hostile reviewer must
reconstruct every imported byte and try to kill at least:

- the D05 bank-local duplicate rule, its sole explicit exemption from
  D02-equivalent acceptance, and the exact collision fixture;
- actual `factor_bits` versus `bits_rank`, the nonce tuple, all 12
  class-to-curve/row/mask mappings, cross-curve sentinels, and affine
  prospective row IDs;
- status precedence through eligible factors, direct stops, bank skips,
  resource rejection, overflow, and shortfall;
- every byte of the 16-template factor stream, 4,097th no-byte overflow,
  one-slot summary, affine witness, expected lengths, nonces, and digests;
- the binary-gcd proof, six-limb boundary, exact 722-round schedule, closed
  P66 call sites, emitted no-data-dependent-control-flow requirement,
  correctness digest, and projection multiplier;
- the restored complete `T_square64` fixture and its contribution to
  `rho_decoder`;
- the corrected diagnostic row digest, frozen fixture tags, complete task
  digest, status bytes, total ordering, and scalar-index semantics;
- every surviving generation, curve, relation, RREF, commit, diagnostic,
  memory, output, wall, coverage, and label clause; and
- the honest decoder-optimization and finite-only novelty boundary.

A pass authorizes only materialization of one standalone resolved theory and
preregistration contract. It does not authorize C++ source, freezing,
compilation, preflight, local execution, remote execution, or a cohort run.
