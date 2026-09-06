# F265-D07 draft preregistration amendment: resource-closed mixed cubic-row bank

## Status and exact composition

This is an unfrozen theory-only amendment. It has not passed a hostile
theory audit. No D07 C++ source, runner, manifest, freeze, compilation,
preflight, local execution, remote execution, discovery cohort, or held-out
cohort exists or is authorized.

D07 imports exactly these immutable draft bytes:

| imported artifact | SHA-256 |
|---|---|
| `D05_DRAFT_ALGEBRA.md` | `e3cbefeb597f263501d327f15f9dd4c7b78ee37d37178135ab1c0a5ff73e9fd3` |
| `D05_DRAFT_PREREGISTRATION.md` | `a62dcb0f7d501778ef1f6092468d38a6ee15c794ec5b609bf145a3d7bf345a35` |
| `D06_DRAFT_ALGEBRA.md` | `e79ea109a9cd8141dd27c4fc99cc7ec2957c454619b0e015802ab4eff5c45f74` |
| `D06_DRAFT_PREREGISTRATION.md` | `67aa6011accffedbed24d0be95614e481f006b80f163a6b5e831dc4fafef6754` |

The complete transitive D02 source boundary is authenticated directly:

| D02 artifact | SHA-256 |
|---|---|
| `../F265_elliptic_cubic_lift_symbolic_search_v2/FROZEN.sha256` | `26f7940244242edc549a2612fc08120372e0f8fab64a2dca154b69ed02d55d6a` |
| `../F265_elliptic_cubic_lift_symbolic_search_v2/ALGEBRA.md` | `d20b5271bb4441fe7d280e35e09a73ff5b0142abf2ed6d3e9839fe22ff4914c4` |
| `../F265_elliptic_cubic_lift_symbolic_search_v2/PREREGISTRATION.md` | `8e3c90420014939ba3ae58490bac2e85fc0a7a45523e12d332cadb5e1f6b384f` |
| `../F265_elliptic_cubic_lift_symbolic_search_v2/search.cpp` | `eeceba4db014346cc78dae3cbae29a65fb32946163becc5d9f5617fc465a7957` |

There is no implicit version-name substitution. A literal `D05` or `D06`
in an imported file continues to identify that historical layer. The
normative D07 proposal is formed in this order:

1. start with the exact D05 algebra and preregistration;
2. apply only the explicit D06 replacements named in D06;
3. replace D06 Preregistration Sections 2.1 and 2.3 by D07 Sections 2 and 3;
4. retain D06 Section 2.2 verbatim, now over the closed D07 journal;
5. replace D06 Sections 3.1, 3.3, and 3.5 by D07 Section 4;
6. insert D07 Section 5 after D06 Section 4;
7. replace D06 Section 6 by D07 Section 6 and D06 Section 8 by D07 Section 7;
8. append D07 Section 8 to the surviving resource contract, replace D06
   Section 9 by D07 Section 9, and apply the D07 algebra amendment.

The two D06 composition sentences that rebind the complete token `D05` are
replaced by this literal section map; they do not survive as substitutions.
All other D06 clauses remain literal. If two surviving clauses conflict,
the composition fails audit; no source author may choose one silently. A
future standalone packet must materialize the fully resolved text and hash
all five inputs before source is written. This amendment does not authorize
that source.

The future lineage table must change the proposed D05/D06 targets
`random_below`, `add_points`, `choose_curve`, `append_curve_rows`, and
`record_factor` to `DERIVED`. The only permitted new semantics are the
replay-wide counters and benchmark-only draw injection specified here, the
closed factor metadata, and sticky journaling before return or throw.
Production random values, affine point/factor results, and curve acceptance
must remain identical to the authenticated D02 bodies for the same input
draw stream. Every derived body needs a unified diff. No other exact body is
silently relaxed.

## 1. New constants and exact static counts

All D06 caps survive. D07 adds these literal constants:

| constant | value | type and scope |
|---|---:|---|
| `FACTOR_CLASS_COUNT` | 12 | `uint8_t`, closed enum |
| `FACTOR_PHASE_COUNT` | 7 | `uint8_t`, closed enum |
| `FACTOR_SIDE_COUNT` | 3 | `uint8_t`, closed enum |
| `FACTOR_EVENT_OVERFLOWS_PACKET_MAX` | 768 | `uint32_t`, full packet |
| `EUCLID_MOD_STEPS_361_MAX` | 724 | `uint16_t`, one gcd |
| `CURVE_ATTEMPTS_MAX` | 32 | `uint8_t`, one curve stream |
| `CURVE_ATTEMPTS_PACKET_MAX` | 49,152 | `uint32_t`, 768 banks |
| `RANDOM_BELOW_ATTEMPTS_MAX` | 4,096 | `uint16_t`, one call |
| `RANDOM_BELOW_CALLS_PACKET_MAX` | 98,304 | `uint32_t`, 768 banks |
| `RANDOM_BELOW_ITERATIONS_PACKET_MAX` | 402,653,184 | `uint32_t`, 768 banks |
| `DIAGNOSTIC_NO_ROW` | 65,535 | `uint16_t` sentinel |
| `DIAGNOSTIC_NO_KEY_U8` | 255 | `uint8_t` sentinel |

The static equalities are

\[
 768\cdot2\cdot32=49{,}152,
\]

\[
 768\bigl(32\cdot3+32\cdot1\bigr)=98{,}304,
\]

and

\[
 98{,}304\cdot4{,}096=402{,}653{,}184.
\]

The three calls in the first term are the `A,x_0,y_0` calls of one `U`
attempt. The one call in the second term is the `s` call of one `POWER`
attempt. Charging both complete 32-attempt streams for every intended bank
is conservative when an earlier curve or random-sampling rejection stops a
bank.

The factor-event hit maximum remains

\[
 768\cdot4{,}096=3{,}145{,}728.
\]

At most one attempted 4,097th event can throw for one bank, so the packet
overflow-attempt maximum is 768. Neither count includes explanatory
diagnostic gcds.

Every product, aggregate counter, byte count, and projection multiplication
uses checked `uint64_t` arithmetic or `cpp_int` as appropriate. Narrow types
in the table are serialized field types, not types for packet arithmetic.

## 2. Closed factor-event contract

### 2.1 Canonical enums

The following table is the complete factor-class enum. An exhaustive source
`switch` has no `default`, and a compile-time assertion requires exactly 12
values.

| code | enum token | reachable production screen |
|---:|---|---|
| 0 | `CURVE_DISCRIMINANT` | `gcd(4A^3+27B^2,N)` |
| 1 | `FACTOR_X_SIGN` | affine equal-`x`, non-global signed-`y` branch |
| 2 | `AFFINE_DENOMINATOR` | affine addition or doubling denominator |
| 3 | `ROW_ROOT` | admitted/prospective row root `v_i` |
| 4 | `SINGLETON` | verified singleton normalized-root signed gcd |
| 5 | `PAIR_X` | public row-pair `x` difference |
| 6 | `PAIR_Y_MINUS` | public row-pair `y` difference |
| 7 | `PAIR_Y_PLUS` | public row-pair `y` sum |
| 8 | `PAIR_CHORD` | same-curve public chord expression with `N` |
| 9 | `SUPPORT2` | verified support-two normalized-root signed gcd |
| 10 | `LOW_BASIS` | verified low-basis normalized-root signed gcd |
| 11 | `STRUCTURAL_Q` | verified structural-complement signed gcd |

No string returned by production affine arithmetic may bypass this enum.
In particular, the authenticated predecessor status `FACTOR_X_SIGN` maps to
class code 1 before the affine call can return to its caller. A proper gcd
from that branch is sticky evidence even if the orbit then stops.

The phase enum is

| code | token |
|---:|---|
| 0 | `CURVE_PHASE` |
| 1 | `AFFINE_PHASE` |
| 2 | `ROW_PHASE` |
| 3 | `SINGLETON_PHASE` |
| 4 | `PAIR_PHASE` |
| 5 | `LOW_BASIS_PHASE` |
| 6 | `STRUCTURAL_Q_PHASE` |

The side enum is `NONE=0`, `MINUS=1`, and `PLUS=2`. Legal combinations are
closed:

| class | legal phase | legal side |
|---|---|---|
| `CURVE_DISCRIMINANT` | `CURVE_PHASE` | `NONE` |
| `FACTOR_X_SIGN` | `AFFINE_PHASE` | `MINUS` |
| `AFFINE_DENOMINATOR` | `AFFINE_PHASE` | `NONE` |
| `ROW_ROOT` | `ROW_PHASE` | `NONE` |
| `SINGLETON` | `SINGLETON_PHASE` | `MINUS` or `PLUS` |
| `PAIR_X` | `PAIR_PHASE` | `NONE` |
| `PAIR_Y_MINUS` | `PAIR_PHASE` | `MINUS` |
| `PAIR_Y_PLUS` | `PAIR_PHASE` | `PLUS` |
| `PAIR_CHORD` | `PAIR_PHASE` | `NONE` |
| `SUPPORT2` | `PAIR_PHASE` | `MINUS` or `PLUS` |
| `LOW_BASIS` | `LOW_BASIS_PHASE` | `MINUS` or `PLUS` |
| `STRUCTURAL_Q` | `STRUCTURAL_Q_PHASE` | `MINUS` or `PLUS` |

Any other combination is an assertion failure that closes the packet. It
cannot be hashed as an unknown class. The first witness table has 12 slots,
one per class code.

### 2.2 Byte-exact event lines

One hashed factor-event line has exactly 15 tab-separated fields in this
order:

`event_ordinal, phase_code, class_code, side_code, curve_id, row_1, row_2,`
`mask_present, mask_w0, mask_w1, mask_w2, mask_w3, mask_w4, g_hex, bank_nonce`.

The commas above separate field names only. The bytes use one ASCII tab
between fields and one ASCII LF after `bank_nonce`. There is no CR, header,
space, quote, prefix, locale formatting, or final extra line.

- `event_ordinal` and `bank_nonce` are `uint32_t` rendered in canonical
  unsigned decimal. Ordinals are `0,...,4095`. `bank_nonce` is the low
  32 bits of the frozen `seed_key({split,bits,shape,index})` and prevents
  accidental cross-bank stream reuse; it is evidence only.
- `phase_code`, `class_code`, `side_code`, and `mask_present` are `uint8_t`
  rendered in canonical unsigned decimal. `mask_present` is 0 or 1.
- `curve_id`, `row_1`, and `row_2` are `uint16_t` rendered in canonical
  unsigned decimal. Actual curve IDs are 0 or 1. Actual original row IDs are
  `0,...,319`. An absent coordinate is exactly decimal `65535`.
- Each `mask_wj` is one `uint64_t` rendered as exactly 16 lowercase
  hexadecimal digits without `0x`. Word `j` contains original row IDs
  `64j,...,64j+63`, with row `64j` in bit zero. If `mask_present=0`, all five
  words must be zero. If it is 1, the five-word mask must be nonzero.
- `g_hex` is the lowercase hexadecimal expansion of the verified positive
  factor, without `0x` or leading zeroes. It has 1 through 30 digits because
  `1<g<N<2^120`.

Canonical unsigned decimal has no leading zero unless the value is zero.
Every event is checked again for `1<g<N` and `N mod g=0` before rendering.
The SHA-256 state starts empty and consumes the literal complete event line,
including its LF, immediately after rendering and before any later public
work. The standard empty-stream digest is used when no event occurred.

`CURVE_DISCRIMINANT` uses the attempted curve ID and two absent row
coordinates. An affine event uses its curve ID and the two deterministic
prospective original row slots of the scalar operands; doubling repeats the
same row slot. `ROW_ROOT` uses its curve ID, the prospective original row
slot as `row_1`, and an absent `row_2`. `SINGLETON` uses its row as `row_1`.
The four direct pair classes and `SUPPORT2` use increasing original row IDs.
`LOW_BASIS` and `STRUCTURAL_Q` use absent row coordinates and require
`mask_present=1`; all other classes require it to be zero. These coordinate
rules are enum validation, not prose for a serializer to guess.

### 2.3 Byte-exact per-slot factor summaries

The status enum is `SHORTFALL=0`, `BANK_SKIP=1`, `RESOURCE_REJECT=2`,
`ELIGIBLE=3`, and `DIRECT_STOP=4`. An internal invariant failure aborts the
split and produces no held-out label; it is not serialized as an ordinary
status.

For every intended slot, the factor-summary line has exactly 12 tab-separated
fields:

`split, bits_rank, shape, index, status_code, observed,`
`occurrence_lower_bound, hashed_count, overflow, first_class,`
`bank_event_sha256, bank_nonce`.

The line ends with one LF. `split`, `bits_rank`, `shape`, `status_code`,
`observed`, `overflow`, and `first_class` are `uint8_t` decimal.
`first_class=255` is the no-event sentinel. `index` and `hashed_count` are
`uint16_t` decimal. `occurrence_lower_bound` and `bank_nonce` are `uint32_t`
decimal. The digest is exactly 64 lowercase hexadecimal digits. `bits_rank`
is 0 through 7 and `shape` is 0 through 2. A shortfall uses the empty-event
digest, zero counts, `observed=0`, `overflow=0`, and `first_class=255`.

The split factor-summary SHA hashes these literal lines in canonical slot
order. The sticky held-out quantifier and coverage clauses from D06 remain,
now over this closed 12-class journal. Thus a `FACTOR_X_SIGN` event in any
held-out slot prevents `finite_quotient_null_signal`, including when the
same bank later rejects.

## 3. Factor-class and 4,097-call fixtures

Use D06's 120-bit `N_factor` and proper factor `g_factor`. Construct the
16 legal `(class,side)` templates in enum order, with `MINUS` before `PLUS`
inside a two-side class. Fill valid phases, sentinels, row coordinates, and
one nonzero five-word relation mask according to Section 2. Cycle these
templates until exactly 4,096 valid events have traversed the production
`record_factor_event` function. The first cycle must populate all 12 first-
class witness slots. Every line is parsed by a separate preflight parser and
re-rendered; the bytes and the two SHA states must agree exactly.

The same fixture then makes the attempted 4,097th call without resetting
the journal. That call must, in this order:

1. leave `observed_useful_factor=true` and every first witness unchanged;
2. advance `occurrence_lower_bound` from 4,096 to 4,097;
3. leave `hashed_count=4,096` and the event SHA unchanged;
4. set `factor_event_overflow=true`; and
5. throw `RESOURCE_REJECT_FACTOR_EVENT_CAP`.

The overflow call is not rendered or hashed. It is nevertheless timed.
Run the full fixture eight times. In each repetition time the first 4,096
calls and the 4,097th call separately. Define

\[
 \rho_{\rm factor}={\max T_{\rm factor4096}\over4096},
 \qquad
 \rho_{\rm factor\_overflow}=\max T_{\rm factor4097th}.
\]

Both intervals include production validation, counters, first-witness
branches when applicable, rendering, streaming SHA for hit calls, and
throw/catch plus sticky-state verification for the overflow call. The raw
projection charges

\[
 3{,}145{,}728\rho_{\rm factor}
 +768\rho_{\rm factor\_overflow}.
\]

The old untimed overflow copy is forbidden.

Separately, invoke the exact affine production path on

\[
 N=35,quad A=1,quad B=1,quad P=(0,1),\quad Q=(0,6).
\]

Assert the curve equations, `gcd(4A^3+27B^2,N)=1`, equal global `x`, neither
global signed-`y` equality, and the returned proper factor 5. The call must
reach enum `FACTOR_X_SIGN`, side `MINUS`, journal the event before return,
and produce the separately rendered expected event line. The unused second
signed check would have gcd 7, but the production order returns at the first
proper gcd. More generally, for two valid same-curve points with equal
global `x`, mixed local signs make the first signed gcd proper; if it is one,
the second signed gcd is full. Therefore a `FACTOR_X_SIGN` event with side
`PLUS` is not reachable in the authenticated production path and is not a
legal enum combination.

Every other class is exercised by the 16-template production journal
fixture. The future source audit must also give a closed call-site table:
every prescribed production gcd site maps to exactly one row of Section
2.1, and no other site can call the journal.

## 4. Arbitrary-width failed-refinement charge

This section replaces D06 Sections 3.1, 3.3, and 3.5. Preserve the exact
D06 one-million-iteration failed-refinement fixture, including operand
access, production gcd, classification, comparison counter, branch, cap
check, and the untimed attempted next comparison. Rename its maximum time
`T_refine_loop1m`. It measures the complete loop path; its particular
prime-power gcd inputs are not claimed to dominate arbitrary inputs.

For any positive `x,y<2^361`, the Euclidean algorithm makes at most 724
remainder operations. Indeed, after at most one initial order swap, every
two remainder operations reduce the smaller positive operand by at least a
factor of two: if the first remainder is at most half, this is immediate;
otherwise the next remainder is the difference from a number larger than
half. After 361 such bit reductions the remainder is zero. The literal 724
allows the initial swap and one terminal operation.

Time the same `cpp_int r=a%b` expression used inside production `gcdz` on
the 256 frozen width pairs

\[
 A_j=2^{361}-(2j+1),\qquad B_j=2^{360}+(2j+1),
 \qquad0\le j<256.
\]

Assert that both operands have 361 bits and `A_j>B_j>0`. One repetition
performs exactly 262,144 remainder operations by cycling through the pairs,
retaining a checksum of every remainder so the compiler cannot remove the
work. Run eight repetitions and set

\[
 \rho_{\rm mod361}={\max T_{\rm mod361,262144}\over262144}.
\]

This timing rate is a finite machine gate, not a symbolic complexity proof.
The mathematical value of the fixture is the input-independent 724-operation
envelope. The registered per-bank decoder charge is now

\[
\begin{aligned}
 \rho_{\rm decoder}={}&T_{\rm split20k}+T_{\rm refine\_loop1m}
 +T_{\rm terminal\_sparse4096}+T_{\rm square64}\\
 &+724\rho_{\rm mod361}
   \left(1{,}000{,}000+\binom{4096}{2}\right).
\end{aligned}
\]

The added term is exactly

`6,795,869,440 * rho_mod361`

per bank. It charges every permitted failed-refinement comparison and every
terminal pairwise-coprimality comparison as an arbitrary 361-bit gcd at the
mathematical remainder-operation maximum. `T_refine_loop1m` and the terminal
fixture separately charge the complete loop and verifier overhead, so this
is deliberate double charging of their sampled gcd work. The D06 Fibonacci
gcd fixture remains an audit cross-check but contributes no weaker
substitution to this formula.

## 5. Curve-attempt and `random_below` cap suite

This section is inserted after D06 Section 4. It uses the exact production
`choose_curve` loop and the exact production `random_below` loop. A
benchmark-only frozen draw source may be injected below those loops. It is
not a reimplementation: production and benchmark wrappers call one shared
body, and source-audit reachability must prove that corpus and evaluator
modes can supply only the ordinary `Rng` source.

### 5.1 Complete 4,096-attempt calls

Use `N_factor`, which has 120 bits. One successful-tail draw stream supplies
the 128-bit masked value `2^120-1` for the first 4,095 iterations and zero
for iteration 4,096. The exact production body must reject the first 4,095
values, accept the last, consume exactly 8,192 64-bit draws, and return zero.

An exhaustion stream supplies `2^120-1` for all 4,096 iterations. It must
consume exactly 8,192 draws and throw `RANDOM_BELOW_CAP` only after the
complete loop. Run each path 16 times and define

\[
 T_{\rm rbelow4096}=\max(
   \max T_{\rm success4096},\max T_{\rm exhaustion4096}).
\]

The timing includes draw calls, 128-bit assembly, masking, comparison,
counter and cap branches, the accepted return or the exhaustion throw/catch,
and checksum/state verification. It is charged once for every possible
entered call, not once per accepted curve.

### 5.2 Complete 32-attempt curve streams

Use the same `N_factor`. Every `random_below` call in this fixture accepts on
its first iteration; the separate term in Section 5.3 supplies the maximum
tail charge. Run these exact production variants:

- `U_FULL`: attempts 1 through 31 use
  `A=N_factor-3,x=1,y=0`, so `B=2` and the discriminant gcd is full;
  attempt 32 uses `A=1,x=0,y=1` and is accepted.
- `U_ZERO`: attempts 1 through 31 use `A=1,x=0,y=0`, so `B=0`;
  attempt 32 uses the accepted `U_FULL` endpoint.
- `U_DUPLICATE`: a benchmark-local tuple table already owns
  `(A,B,x,y)=(1,1,0,1)`; attempts 1 through 31 reproduce it after the full
  discriminant screen, and attempt 32 uses `A=1,x=0,y=2`.
- `POWER_ZERO`: attempts 1 through 31 use `s=N_factor-1`, hence `A=0` and
  `B=0`; attempt 32 uses `s=2`.
- `POWER_DUPLICATE`: the local table already owns the clean tuple produced
  by `s=1`; attempts 1 through 31 reproduce it after the full discriminant
  screen, and attempt 32 uses `s=2`.

Before timing, assert every displayed `B`, discriminant gcd, duplicate
branch, accepted tuple, draw count, attempt count, and final status. Also run
the corresponding all-32-rejected variants and include their terminal
`CURVE_ATTEMPT_EXHAUSTED` throw/catch. Run every variant eight times. Let

\[
 T_{\rm curveU32}=\max T_{\rm all\ U\ variants},\qquad
 T_{\rm curvePOWER32}=\max T_{\rm all\ POWER\ variants}.
\]

These are exact full-loop charges. A timing of one successful attempt cannot
replace them.

### 5.3 Packet charge

The registered curve/sampling charge is

\[
 T_{\rm curve\_caps}=
 768(T_{\rm curveU32}+T_{\rm curvePOWER32})
 +98{,}304T_{\rm rbelow4096}.
\]

The second term covers exactly 402,653,184 possible inner sampling
iterations. The first term separately covers 49,152 curve-attempt bodies,
including `B`, discriminant, duplicate, success, exhaustion, counter, and
status work. It deliberately double charges the one-iteration sampling work
inside the curve fixtures. The real-bank `rho_orbit` term also remains, so
ordinary observed curve work is double charged again. These duplications
are explicit safety margins, not missing subtraction rules.

Fixture draw buffers, tuple tables, counters, and checksums are allocated
inside the preflight category and released before production. A largest
4,096-attempt draw buffer has 8,192 `uint64_t` words, exactly 65,536 bytes.

## 6. Byte-exact diagnostic stream

This section replaces D06 Section 6 while preserving its total task order,
post-commit noninterference, timeout semantics, and retention caps.

The task-kind enum is `PAIR=0` and `ANCHORED_THIRD=1`. The tri-state enum is
`FALSE=0`, `TRUE=1`, and `NOT_APPLICABLE=2`. Shape codes are
`RANDOM=0`, `NEIGHBOR=1`, and `SAFE=2`. All are `uint8_t`. The row sentinel
is the `uint16_t` value 65,535. The diagnostic status enum is
`COMPLETE=0`, `TIMEOUT=1`, and `NOT_RUN=2`.

One diagnostic task line has exactly 20 tab-separated fields in this order:

`split, bits_rank, shape, index, basis_ordinal, task_kind, curve,`
`pair_row_1, pair_row_2, third_row, tangent_hex, chord_hex, disc_hex,`
`third_root, index_sum, index_difference, index_twice, index_thrice,`
`index_product, index_equal_v2`.

It ends with one LF and has no header, CR, spaces, quotes, prefixes, or
locale formatting.

- The first seven fields are `uint8_t` canonical unsigned decimal except
  `index`, which is `uint16_t`. `basis_ordinal` is 0 through 7 and `curve`
  is 0 or 1.
- The three row fields are `uint16_t` canonical unsigned decimal. Anchor
  rows are increasing original IDs in `0,...,319`. A pair task uses
  `third_row=65535`. An anchored-third task uses a distinct actual row.
- `tangent_hex`, `chord_hex`, and `disc_hex` are positive lowercase
  hexadecimal integers without `0x` or leading zeroes. Each has at most 91
  digits because every diagnostic gcd divides a positive at-most-361-bit
  row value.
- The final seven fields are `uint8_t` canonical unsigned decimal in the
  tri-state enum. For a pair task all seven equal 2. For an anchored-third
  task all seven are 0 or 1; `third_root=0` when the chord gcd does not
  exceed one.

Every generated task is schema-validated, rendered once, and fed including
its LF into `diagnostic_task_sha256` in the D06 lexicographic task order.
The retained detail line is this same byte vector; it is not separately
serialized. A second preflight parser must parse and byte-identically
re-render every line of the 14,400-task production-width fixture before its
two SHA states are compared.

The diagnostic status line has exactly 14 tab-separated fields:

`status_code, completed_count, task_sha256, next_split, next_bits_rank,`
`next_shape, next_index, next_basis_ordinal, next_task_kind, next_curve,`
`next_pair_row_1, next_pair_row_2, next_third_row, retained_count`.

It ends with one LF. Counts are `uint64_t` canonical decimal. The digest is
64 lowercase hex digits. On timeout, the next-key fields contain the exact
next task. On complete or not-run status, all `uint8_t` next-key fields are
255 and all `uint16_t` next-key fields are 65,535. No unfinished suffix is
represented as exhaustive.

The task maxima remain exactly 960 pair and 13,440 anchored-third tasks per
maximum bank, 737,280 pair and 10,321,920 anchored-third tasks across the
packet, and 11,059,200 tasks total. The first-64-per-bank and first-8,192-
per-split detail rules still imply the unchanged 67,108,864-byte diagnostic
category because each retained record is checked against 4,096 bytes.

## 7. Revised raw projection

This section replaces D06 Section 8. Preserve every D06 definition not
explicitly replaced above. With the same static totals

`R_max=172,032`, `P_max=22,032,384`, `W_max=22,204,416`,
`H_max=22,204,416`, `V_basis,max=98,304`, and
`C_final=588,251,136`, use

\[
\begin{aligned}
T_{\rm raw}={}&T_{\rm generation}+T_{\rm curve\_caps}
 +\rho_{\rm orbit}R_{\max}
 +\rho_{\rm pair}P_{\max}
 +\rho_{\rm peel}W_{\max}\\
&+\rho_{\rm rel1}R_{\max}
 +\rho_{\rm rel2}P_{\max}
 +\rho_{\rm lowinsert}H_{\max}\\
&+768\rho_{\rm lowfinal}
 +768\rho_{\rm decoder}
 +\rho_{\rm rel64}V_{\rm basis,max}\\
&+3{,}145{,}728\rho_{\rm factor}
 +768\rho_{\rm factor\_overflow}\\
&+768\max(\rho_{\rm commit},\rho_{\rm commit,real})
 +768\rho_{\rm diag}
 +\rho_{\rm io}C_{\rm final}.
\end{aligned}
\]

Here `T_generation` is still the D06 two-replay candidate/retry cap charge.
The one-million loop plus arbitrary-width Euclid charge is inside the new
`rho_decoder`. The 32-attempt and 4,096-sampling-attempt terms are inside
`T_curve_caps`. The 4,097th factor-event attempt is the explicit overflow
term. None is hidden in an empirical per-row ratio.

Set `T_projected=1.75*T_raw`. The D05/D06 12,600-second production gate,
1,800-second preflight cap, four-hour common deadline, 300-second
finalization reserve, diagnostic inequality, worker, load, memory, disk,
and output gates remain. If this conservative formula does not fit, the
packet stops. A smaller post-timing formula requires a new version and a new
hostile audit.

## 8. Rechecked count, memory, and output closure

The unchanged static arithmetic was recomputed:

- `172,032` rows and `22,032,384` unordered pairs;
- `22,204,416` maximum peel row-round tests;
- `44,064,768` support-two exact divisions and square tests;
- `98,304` maximum low-plus-structural basis verifications;
- `3,145,728` hashed factor events and at most `768` overflow attempts;
- `49,152` curve attempts, `98,304` entered `random_below` calls, and
  `402,653,184` inner sampling iterations;
- `262,144` dense and independently `262,144` sparse exponent entries per
  cap-complete decoder; and
- `11,059,200` diagnostic tasks.

The D06 4,194,304-byte certificate payload per active worker remains inside
its 256 MiB arena. D07 adds at most one 65,536-byte draw buffer, a 256-pair
modulo table, one factor-line render buffer of at most 512 bytes, and one
diagnostic-line render buffer of at most 4,096 bytes to a serial preflight
fixture. These objects are released before production and fit inside the
unchanged 134,217,728-byte preflight artifact category and preflight process
limits. Streaming factor and diagnostic SHA states retain no complete event
or task stream.

Adding one first witness slot for `FACTOR_X_SIGN` changes no output category.
Each witness uses the same at-most-512-byte bounded event representation;
12 slots use at most 6,144 bytes inside the existing 16,384-byte bank
summary. The writer still measures the complete summary. Overflow is a core
resource rejection, not truncation.

The final category sum remains exactly `588,251,136` bytes. The one-bank
on-disk temporary remains 442,368 bytes because factor-event lines are
streamed into a digest and only bounded witnesses enter the summary. Hence
the registered experiment-directory peak remains

\[
 588{,}251{,}136+64\cdot442{,}368+134{,}217{,}728
 =750{,}780{,}416\text{ bytes},
\]

below 768 MiB. The 128 MiB per-file, 4 GiB virtual-memory, 3.5 GiB measured
RSS, 2.5 GiB static live-allocation, and 1 GiB total-output gates are
unchanged. Every fixture assertion or cap failure closes production.

## 9. Exact finite scope and audit gate

The saturated peel is a decoder optimization and a finite-source opening.
It is not an elliptic source theorem. D07 proves no private-pivot frequency,
residual-core bound, useful-relation probability, or all-input factoring
claim. Numerical output, if later authorized, is finite guidance only.

Before source is written, a fresh no-context hostile theory reviewer must
reconstruct all authenticated imports and try to kill at least:

- the 12-value closed factor enum, every production call-site mapping, and
  the explicit `FACTOR_X_SIGN` affine witness;
- legal phase/side combinations, widths, sentinels, exact factor bytes,
  per-bank and split SHA determinism, and all-intended-slot null quantifier;
- timing and projection of both the first 4,096 journal calls and the
  attempted 4,097th overflow call;
- the 724-step Euclidean bound, full one-million-iteration loop charge,
  arbitrary 361-bit modulo charge, and terminal pair-scan charge;
- all 32 `U` and `POWER` curve attempts, all 4,096 `random_below` iterations,
  the exact packet multipliers, and benchmark-injection unreachability;
- the byte-exact 20-field diagnostic task line, numeric types, sentinels,
  enum values, total order, timeout next-key line, and parser/SHA fixture;
- the relation-certificate stage, every live-memory term, all output sums,
  and the revised raw projection; and
- the unchanged private-primary theorem, low-image quotient logic, factor
  firewall, corpus disjointness, sticky rejection semantics, and honest
  finite-only novelty boundary.

A pass authorizes only materialization of one standalone resolved contract.
It does not authorize C++ source, freezing, compilation, preflight, or any
execution.
