# F265-D11 draft preregistration amendment — materialized rate and source fixtures

## Status and exact imports

This is an unfrozen theory-only additive draft. It creates no evaluator source,
runner, manifest, freeze, compilation, preflight, execution, result, or ledger
entry. It authorizes none of those actions by itself.

| Artifact | SHA-256 |
|---|---|
| `D09_DRAFT_ALGEBRA.md` | `93ee6021b969a3624cf499df5e18ea9c262e2a095a6b0634644cc1d69ee8030d` |
| `D09_DRAFT_PREREGISTRATION.md` | `3b499578678a0f71c75f52608e53f2fba7f390fb5a09a95bc20c61d09fe1c0a4` |
| `D10_DRAFT_ALGEBRA.md` | `aab2397c601b645f71da0bc79a8f58ed9ef79ea984fa7f7458ab2a49582a17a7` |
| `D10_DRAFT_PREREGISTRATION.md` | `be7e2a05a1eac6659000cdfe71469697d76b867b42cb60c1c244b06ec63afb6e` |
| `D11_DRAFT_ALGEBRA.md` | `a177438e425a20550342e7efa94ec1f70d30f40fe204640f983435dc36554f27` |

Read all five authenticated bytes in full. Apply only the replacements and
additions below. Every D09/D10 preregistration clause not named here survives
literally. Preserve all predecessor bytes.

D11 makes exactly four repairs.

1. The D11 algebra removes the orphan P222 wording.
2. Section 6 makes evaluator-source drafting the only possible theory-PASS
   authorization while containment is pending.
3. Sections 2--3 materialize every new D10 rate fixture.
4. Sections 1 and 4 split the synthetic source projection into a chronological
   no-terminal body workload and separate injected terminal-body workloads.

## 1. Exact source timing workloads

This section replaces D10 preregistration lines 178--199. D10's untimed source
semantic suite survives.

### 1.1 Common modulus and draw encoding

Use the exact D10 prime

```text
N_star = 162259276829213363391578010288127 = 2^107-1.
```

Perform the D10 Lucas--Lehmer certificate outside every timer. For an injected
first-try `random_below` result `z`, supply exactly two limbs

```text
low  = z mod 2^64
high = floor(z/2^64).
```

The production sampler concatenates `high` above `low`, applies its registered
107-bit mask, and must return `z` in one iteration. No warm-up draw occurs.

### 1.2 Chronological no-terminal maximum-bank body workload

`SOURCE_CHRONO320` is one fixture-only split-2 bank. It follows production
phase order and never takes a terminal branch. Its proposal tape is:

| Mode | Slots | Injected values | Required result |
|---|---:|---|---|
| `U` | 0--30 | `A=N_star-3, x=1, y=0` | `B=2`, full discriminant gcd, reject |
| `U` | 31 | `A=1, x=N_star-1, y=N_star-1` | `B=3`, unit discriminant gcd, accept |
| `POWER` | 0--30 | `s=N_star-1` | `A=0, x=1, y=N_star-1, B=0`, full discriminant gcd, reject |
| `POWER` | 31 | `s=1` | `A=2, x=1, y=1, B=N_star-2`, unit discriminant gcd, accept |

The sampler target is `A-1` for a `U` coefficient draw, the displayed `x` or
`y` for a coordinate draw, and `s-1` for a `POWER` draw. Thus the workload
makes exactly 128 entered sampler calls, 128 accepted iterations, 256 RNG
limb draws, 64 proposal screens, and 64 discriminant gcds.

Benchmark-only affine injection is below the shared production addition body
and is unreachable for split codes 0 and 1. It preserves bank phase order but
does not pretend that reset operands form a scalar orbit. Source semantics are
checked by the separate D10 semantic suite and by evaluation replay.

For the accepted `U` curve, emit its base row once. Then make exactly 159
addition calls. Each call resets both operands to

```text
P = Q = (N_star-1,N_star-1), A=1, B=3.
```

The production unit-denominator branch must return `(6,15)`. For the accepted
`POWER` curve, emit its base row once. Then make exactly 159 addition calls,
each resetting

```text
P = Q = (1,1), A=2, B=N_star-2.
```

With `inv2=(N_star+1)/2`, the required slope is `5*inv2 mod N_star`; the
required returned coordinates are

```text
x3 = slope^2-2 mod N_star
y3 = slope*(1-x3)-1 mod N_star.
```

Before timing, independently verify both curve equations, returned points,
and every nonzero unit row root. The timed workload makes exactly 318 affine
additions, 320 row-root gcds, and 320 row renderings.

Below the shared product-and-peel input seam, replace the rendered row values
by the exact positive tape

```text
w_i = 2^180 + 2*i + 1
a_i = w_i^2                       for 0 <= i < 320.
```

Build the product by exactly 319 left-fold multiplications. Execute all 320
production peel cells, including their exact divisions, base remainders,
binary modular powers, gcds, residual divisions, and square tests. This tape
is only a width workload; it cannot enter evaluation.

For each of eight repetitions, materialize the tape and independent expected
trace before timing. Start the monotonic timer immediately before bank-state
initialization. Stop it only after the final peel result, all production
counters, the production FNV-1a checksum, and the production SHA-256 trace have
committed in memory. Include
all production allocation, rendering, counter, and trace-update work. Exclude
Lucas--Lehmer verification, tape construction, independent verification, and
metric-file I/O. Require the exact counters above and equality between the
production and independent trace digests. Let `T_source_chrono320` be the
maximum elapsed time.

The source packet must materialize the proposal tape, both affine tapes, all
320 peel operands, the complete expected counter tuple, the literal expected
FNV-1a checksum, and the literal expected trace digest as immutable preflight
fixture bytes. A later source audit must authenticate those bytes before
compilation can be considered.

### 1.3 Separately timed terminal bodies

Terminal fixtures inject operands immediately below the shared bodies. They do
not invoke the bank driver, so one stop cannot censor a later fixture call.
They never enter evaluation.

`SOURCE_AFFINE_STOP3` uses `N=35,A=B=1` and, in this order, calls:

```text
(0,1) + (0,34)   -> global infinity
(0,1) + (0,6)    -> equal-x MINUS factor 5
(0,1) + (7,1)    -> denominator factor 7.
```

One repetition resets state, starts the timer, makes exactly these three
production addition calls, folds the three status records into the production
trace, and stops the timer. Verify statuses, factors, call counters, and the
independent trace digest outside the timer. Let `T_source_affine_stop3` be the
maximum of eight repetitions.

`SOURCE_ROW_STOP2` calls the exact production prospective-row-root body with

```text
N=35, v=5  -> proper factor 5
N=35, v=0  -> full-gcd BANK_SKIP.
```

One repetition times exactly these two calls and their production trace
updates. Verify both results, counters, and the independent trace digest
outside the timer. Let `T_source_row_stop2` be the maximum of eight
repetitions.

The source packet must materialize both terminal operand streams, expected
status streams, counter tuples, literal FNV-1a checksums, and literal SHA-256
digests. Event-journal rendering remains charged by `rho_factor`; it is not
included in either terminal timer.

## 2. Common contract for the twelve added rate fixtures

This section replaces D10 preregistration lines 215--223. D09's retained rate
fixtures and D10's semantic fixtures survive.

All twelve fixtures call the same production body used by evaluation. Any
injection is below that body and is unreachable outside split code 2. Every
fixture runs eight repetitions. In each repetition:

1. materialize operands, reserve storage, reset state, and construct an
   independent expected-result stream before timing;
2. initialize production FNV-1a and SHA-256 states, start the monotonic timer,
   execute the exact loop below, append each specified result record to both
   states, finalize them, and stop the timer;
3. outside the timer, require the registered operation count, checksum,
   semantic result, and equality of production and independent digests; and
4. retain only the fixture name, operand digest, result digest, exact counter,
   checksum, and eight elapsed times.

Result records are LF-terminated TSV. Tags are the literal upper-case fixture
names below. Unsigned integers are lower-case hexadecimal without a prefix or
leading zero, except zero is `0`. Masks are exactly 16 lower-case hexadecimal
digits. In addition to SHA-256, fold the same result bytes through FNV-1a-64:

```text
h = 14695981039346656037
for each byte b in order:
    h = (h xor b) * 1099511628211 mod 2^64.
```

The exact non-basis result lines are:

```text
RATE_NODE           q 1 1
RATE_TOUCH          q 1 1
RATE_LEAF           loop_index block unit_exponent_mask
RATE_EXP            loop_index output
RATE_PARITY         group_index mask
RATE_GF2            W 3f ffffffffffffffff 123456789abcdef
RATE_EXACT_PRODUCT  repeat_index A64
RATE_MOD_PRODUCT    repeat_index 4
RATE_ISQRT          loop_index R64
RATE_INVERSE        loop_index 4
RATE_SIGNED         repeat_index 3 5
```

Spaces in this display denote one tab. Loop, group, and repeat indices start at
zero and use the integer encoding above. `RATE_LEAF` uses mask
`0000000000000001` for `e_0` and `8000000000000000` for `e_63`. The GF(2)
scratch word starts at `123456789abcdef` and self-assignment leaves it equal
to that value. `RATE_BASIS_RECORD` is the sole exception: its result bytes are
the production record itself, with no fixture wrapper.

The source packet must materialize every operand stream, literal expected
FNV-1a checksum, and literal expected SHA-256 digest as immutable fixture
bytes. No per-iteration result record is written by preflight.

The timer includes the named production call and its result-trace update. It
excludes operand generation, independent calculation, verification, and file
I/O. Rates are the maximum elapsed time divided by the exact denominator in
Section 3. Timers never overlap. Work shared with an older rate is deliberately
double charged.

Let `F64` denote the exact D10 support-64 fixture after its immutable
materialization. Write its rows as `a_0,...,a_63`, its exact root as `R64`, and
put

```text
A64 = product(a_0,...,a_63) = R64^2.
```

Before any rate timer, independently verify the D10 prime sequence, absence of
an omitted prime congruent to one modulo 15 between consecutive materialized
entries, every maximal exponent, every row, `A64=R64^2`, and the fixture SHA.

## 3. Exact fixture-to-rate map

### 3.1 Refinement and representation rates

Put `q=2^360`.

`RATE_NODE` makes exactly 65,536 independent calls to
`SAME_SUPPORT(q,q,d=q)`. Each call must visit exactly one equal-support
recursion node and return the single local block `(q,1,1)`. Its result record
is `RATE_NODE` followed by `q,1,1`. Require recursion-node count 65,536 and
returned-block count 65,536. Define

```text
rho_node = max_time(RATE_NODE) / 65,536.
```

`RATE_TOUCH` makes exactly 65,536 independent calls to
`TWO_BASE(q,q,g=q)`. Each call must make one touch, one recursion node, and
return `(q,1,1)`. Require touch count 65,536. Define

```text
rho_touch = max_time(RATE_TOUCH) / 65,536.
```

`RATE_LEAF` uses a preallocated 2,048-leaf tree and calls only the exact leaf-
assignment body; ancestor updates remain charged by `rho_tree`. For even loop
index assign block `2` with exponent vector `e_0` to leaf zero. For odd index
assign block `4` with exponent vector `e_63`. Make exactly 262,144 assignments.
The final leaf is `(4,e_63)`. The result trace contains one record per
assignment. Define

```text
rho_leaf = max_time(RATE_LEAF) / 262,144.
```

`RATE_EXP` calls the checked production coordinate update
`out=u*w+v*delta` exactly 262,144 times, cycling these tuples in order:

```text
(u,w,v,delta) = (1,359,1,0), (2,179,1,0),
                  (1,1,359,1), (17,0,343,1).
```

The outputs are `359,358,360,343`. Require every output at most 360, output
sum 93,061,120, and output xor zero. Define

```text
rho_exp = max_time(RATE_EXP) / 262,144.
```

`RATE_PARITY` calls the exact exponent-parity-cell body 262,144 times. The
coordinate is the loop index modulo 64. The exponent cycles through
`0,1,359,360`. Reset the destination mask before each group of 64 cells and
append it after the group. Require exactly 131,072 one bits and 4,096 emitted
masks, each equal to `6666666666666666`. Define

```text
rho_parity = max_time(RATE_PARITY) / 262,144.
```

### 3.2 Dense elimination rate

`RATE_GF2` uses the exact D10 dense 1,875-mask stream. Run the complete
production insertion, reverse reduction, canonical-nullspace, low/complement
reduction, and verification once. Require rank 63 and sole kernel generator
`ffffffffffffffff`.

Let `W` be the production GF(2) word-operation count when that result is
obtained. Require `0<W<=524,288`. Then call the exact counted production
assignment primitive on a scratch word exactly `524,288-W` times, assigning
the scratch word to itself. Require final total 524,288 and unchanged semantic
output. The trace contains the unpadded count `W`, rank, generator, and final
scratch word. Define

```text
rho_gf2 = max_time(RATE_GF2) / 524,288.
```

Padding is fixture-only. It fixes the timing denominator and cannot enter
evaluation or its operation counter.

### 3.3 Root and record rates

`RATE_EXACT_PRODUCT` repeats 1,024 times. In each repeat set `z=1` and call the
selected-row exact-product body on `a_0,...,a_63` in order. Require exactly 64
multiplications and final `z=A64` per repeat. The total denominator is 65,536.

```text
rho_exact_product = max_time(RATE_EXACT_PRODUCT) / 65,536.
```

`RATE_MOD_PRODUCT` repeats 4,096 times. In each repeat set `z=1` and call the
selected-row modular-product body modulo 15 on the D10 supplied roots
`4,1,...,1` in row order. Require 64 multiplications and final `z=4` per
repeat. The total denominator is 262,144.

```text
rho_mod_product = max_time(RATE_MOD_PRODUCT) / 262,144.
```

`RATE_ISQRT` calls the exact production integer-square-root body on `A64`
exactly 256 times. Every call must return `R64`, with checked remainder zero.

```text
rho_isqrt = max_time(RATE_ISQRT) / 256.
```

`RATE_INVERSE` calls the exact production modular inverse body on `(4,15)`
exactly 262,144 times. Every result is 4. Require result sum 1,048,576 and
result xor zero.

```text
rho_inverse = max_time(RATE_INVERSE) / 262,144.
```

`RATE_SIGNED` repeats the D10 support-three normalized-root classification
131,072 times. Each repeat calls the production signed-gcd body in fixed order
on `(rho,N)=(4,15)`: minus returns 3, then plus returns 5. Require exactly
262,144 signed gcd calls and the alternating result stream `3,5`.

```text
rho_signed = max_time(RATE_SIGNED) / 262,144.
```

`RATE_BASIS_RECORD` renders exactly 65,536 copies of the D10 full-support
structural record through the production renderer and its 512-byte check. Its
semantic fields are:

```text
original mask = (ffffffffffffffff,0000000000000000,
                 0000000000000000,0000000000000000,
                 0000000000000000)
class = STRUCTURAL_Q, ordinal = 0
R mod 15 = 1, X = 4, rho = 4
minus gcd = 3, plus gcd = 5
root class = non-global structural.
```

Every rendered byte sequence must be identical and within 512 bytes. The
result digest is over those exact rendered records, with no wrapper line.

```text
rho_basis_record = max_time(RATE_BASIS_RECORD) / 65,536.
```

The complete mapping is therefore:

| Rate | Fixture | Exact denominator |
|---|---|---:|
| `rho_node` | `RATE_NODE` | 65,536 recursion nodes |
| `rho_touch` | `RATE_TOUCH` | 65,536 touches |
| `rho_leaf` | `RATE_LEAF` | 262,144 leaf assignments |
| `rho_exp` | `RATE_EXP` | 262,144 coordinate updates |
| `rho_parity` | `RATE_PARITY` | 262,144 parity cells |
| `rho_gf2` | `RATE_GF2` | 524,288 GF(2) word operations |
| `rho_exact_product` | `RATE_EXACT_PRODUCT` | 65,536 exact products |
| `rho_mod_product` | `RATE_MOD_PRODUCT` | 262,144 modular products |
| `rho_isqrt` | `RATE_ISQRT` | 256 square roots |
| `rho_inverse` | `RATE_INVERSE` | 262,144 inversions |
| `rho_signed` | `RATE_SIGNED` | 262,144 signed gcds |
| `rho_basis_record` | `RATE_BASIS_RECORD` | 65,536 records |

Any zero denominator, wrong counter, checksum mismatch, digest mismatch,
oversize record, fixture-cap crossing, or semantic mismatch stops preflight.
The menus are empirical rate fixtures, not dominance theorems. The hard common
deadline remains authoritative.

## 4. Repaired literal serial projection

Replace D10's definition of `T_source` by

\[
\begin{aligned}
T_{\rm source}={}&468\bigl(T_{\rm source\_chrono320}
 +T_{\rm source\_affine\_stop3}
 +T_{\rm source\_row\_stop2}\bigr)\\
&+59{,}904T_{\rm rbelow128}.
\end{aligned}
\]

The coefficient 468 deliberately charges every registered bank for the full
320-row chronological workload, all three affine stop bodies, and both row
stop bodies even though a real bank can stop only once. The sampler term still
charges 128 iterations to every possible sampler call and double charges the
first-try calls inside `SOURCE_CHRONO320`. No worker speedup is assumed.

Retain D10's displayed `T_decoder` literally, using the twelve rates fixed in
Section 3. Retain

\[
 T_{\rm pass}=T_{\rm source}+T_{\rm decoder}
              +60{,}372\rho_{\rm factor}
              +210{,}632{,}704\rho_{\rm io},
\]

\[
 T_{\rm raw}=2T_{\rm pass}+900,
 \qquad T_{\rm projected}=1.75T_{\rm raw}.
\]

Thus evaluation and replay both receive the repaired source and terminal-body
charges. All D10 projection thresholds, live-deadline subtraction, deliberate
double charges, I/O rules, and failure semantics survive.

## 5. Digest and byte accounting

The immutable operand and expected-digest files required above are preflight
artifacts. They remain inside D09's 67,108,864-byte preflight category and its
128 MiB per-file cap. Timed result streams are hashed in memory and are never
written per iteration. D09's total-output and 294,006,784-byte directory-peak
bounds survive unchanged. A future source packet must give exact file widths
and prove the category sum before a source audit can pass.

## 6. Containment and release gate

Replace D10 preregistration lines 338--341 by:

> D11 has no approved dynamic-containment implementation. A fresh theory PASS
> may authorize evaluator-source drafting only. Pending containment forbids
> runner drafting, freezing, compilation, preflight, local or remote execution,
> result release, and ledger edits. D09's cgroup-v2 mechanism is not silently
> inherited as authorization on any host.

The rest of D10 Sections 7--8 survives literally. In particular, the user must
approve a replacement containment workflow, an immutable runner must state a
hard aggregate envelope, and a later no-context audit must authenticate and
attack its exact bytes before any post-source action is authorized.

Before evaluator source is drafted, a fresh no-context theory reviewer must
authenticate all five input hashes and try to kill the D09+D10+D11 composition,
the exact source tapes and chronology, every terminal-body operand, all twelve
rate loops and timer boundaries, every checksum and digest rule, the repaired
projection coefficients, byte accounting, the closed F271-only provenance,
and the pending-containment authorization boundary.

A theory PASS authorizes only C++17 evaluator-source drafting. It does not
authorize a runner, freeze, compilation, preflight, local or remote execution,
result, or ledger edit.
