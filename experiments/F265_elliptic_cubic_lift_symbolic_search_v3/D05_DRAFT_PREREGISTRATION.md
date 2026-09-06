# F265-D05 draft preregistration: fixed mixed cubic-row bank

## Status

This is an unfrozen preregistration draft. It has not passed a hostile theory
audit. No D05 C++ source, runner, frozen manifest, compilation, local
execution, remote preflight, discovery run, or held-out run exists or is
authorized.

## 1. Exact predecessor and evidence imports

D05 imports no predecessor by name alone. The only proposed implementation
origin is the following immutable D02 packet.

| artifact | SHA-256 |
|---|---|
| `experiments/F265_elliptic_cubic_lift_symbolic_search_v2/FROZEN.sha256` | `26f7940244242edc549a2612fc08120372e0f8fab64a2dca154b69ed02d55d6a` |
| `experiments/F265_elliptic_cubic_lift_symbolic_search_v2/ALGEBRA.md` | `d20b5271bb4441fe7d280e35e09a73ff5b0142abf2ed6d3e9839fe22ff4914c4` |
| `experiments/F265_elliptic_cubic_lift_symbolic_search_v2/PREREGISTRATION.md` | `8e3c90420014939ba3ae58490bac2e85fc0a7a45523e12d332cadb5e1f6b384f` |
| `experiments/F265_elliptic_cubic_lift_symbolic_search_v2/search.cpp` | `eeceba4db014346cc78dae3cbae29a65fb32946163becc5d9f5617fc465a7957` |

Before any source audit, a future D05 manifest must authenticate all four
files. The table below fixes every D02 routine proposed for exact reuse or
semantic derivation. A routine hash is the SHA-256 of the inclusive line
range from the authenticated D02 `search.cpp`, with its literal LF after
each line. These are source-body hashes, not symbol-name assertions.

| D02 body | lines | body SHA-256 | D05 status |
|---|---:|---|---|
| `ResourceReject` | 48--50 | `a600cc27394c802b562f634f10873192f5d5e8c530de424b84196ab9eaedcc53` | exact |
| `mix64` | 52--57 | `70546655b5ebf81bdeed4ec06c1cac2ffdeabf454ac1e2692c013da3bb159327` | exact |
| `seed_key` | 59--63 | `b006ee9fac8df7cefa733aba73c6440965cf8a32e12c10f6a4c686df4b20ff1b` | exact body; D05 master constant |
| `Rng` | 65--69 | `1c00a9fa73974264bf8f2a937d2205ae051731d935d39119d417de7582216142` | exact |
| `absz` | 71--71 | `be575e306c7aff833fc751c60cb980a6a5d32e6539c7f6fc40e76cc2d1cd2260` | exact |
| `modz` | 73--77 | `4a92bd5687425d59b79bb86682d48aeca724bc01ff95f70d4b8878a7cfc46f62` | exact |
| `gcdz` | 79--88 | `b115b2964578a1519bbe9ad8cdc596216f88ce4122f9f9f672ce199ec7a0b202` | exact |
| `powz` | 90--98 | `bbda92c13a8a2aa85d3e178646a883ea653cbadd0377b0d24fe1f8e04e8f6530` | exact |
| `powmod` | 100--109 | `cfd94499c1f6d65c121a10f955e5fcc5bf21b8dc4160d82e0e86cdb20bc41cdb` | exact |
| `invmod` | 111--125 | `49fb806c7033cda6cee78bba56e17babdc1452c28311b74ff0b8281ec04a2199` | exact |
| `bitlen` | 127--130 | `ac6cd4043f7e7db9add50a13ea25ee6584f7d80d5ca358fdf2d24982ed224fa6` | exact |
| `isqrtz` | 132--145 | `547e00d64a98a5f0b097eed70e6966f53aa92ea94ed3474c7fc59c568a1835df` | exact |
| `squarez` | 147--153 | `d73c5bd7c59777eaa9c206c136710769e54d968b54cb0e914952471de9b7fd76` | exact |
| `dec` | 155--155 | `28f6ed73a16964490be302e6959f617da58d6cecf9b179cbe1fb8769d3682d35` | exact |
| `mulmod64` | 157--159 | `8a610811d27337a16d3d4378a4478db56c111e8f207f09363c696d59997b2593` | exact |
| `powmod64` | 161--169 | `79ded6e3da50dc706c224329fa1f08c82b7621f792d3d4c795bcb8da261f64ab` | exact |
| `prime64` | 171--198 | `c62d171bb7615eb589f27d023041e56a8c3ff071e1bcffffa2f70a92aa654b08` | exact |
| `random_prime` | 200--217 | `2c5e5bb686d1fadb0832886cb7525132cf3b130ef61f9f7e1f1edce19c5ccc9e` | exact |
| `next_prime_same_bits` | 219--226 | `8b13b8bf28c57be5faffde85c43932a4b63d763a27186e480dfe15a8ac2be369` | exact |
| `random_below` | 228--238 | `5f366424877ce89147014e60c774336b077261e17ea86edd5e61daebc38d8046` | exact |
| `shape_name` | 258--260 | `7b126d9ed011f052bca12d6aa866c55fd4ac62f9184ebf255f9ba763a1e916e8` | exact |
| `make_case` | 262--290 | `8a96fcdd44724bdbe5f33a088bac7b18fdf30e70049a7fa7715ab18e78484dd4` | exact body; D05 seed flows through `seed_key` |
| `make_corpus` | 292--315 | `d8789349ae9f34a0242560f2455e5a50ddf43a2b111150e76ce8515b248b6856` | exact production order |
| `add_points` | 328--362 | `31e693b4851676cd7ca162ef8e231361e241889f187e8d0fee47b00703eaa445` | exact |
| `record_factor` | 471--480 | `c8be500f7e232798f168e632fc34d68f471693d9b13c4ea65466e4fff1465f74` | exact |
| `choose_curve` | 482--531 | `0c58f43df900536e8a5267bc250890c8d5436a31cc80aac4a1b790aea4978932` | derived only as specified in Section 3 |
| `append_curve_rows` | 533--581 | `dbd92c6cd2d24d3b886700028bc98910d1cc5271a7fe4d129f1a14b671108aef` | derived only for fixed all-index `K` |
| `bit_get` | 592--594 | `2851f1ed382fdd963fa03765e5823a2ef0bb8961dcf1bcdedf938a56f721d69e` | exact |
| `bit_flip` | 596--598 | `90118885b0f1c1617b079ce8239f855400a5483e3e6a0d306183b6da957d197a` | exact |
| `bit_xor` | 600--602 | `19d6d74c5bceb8bf998ea243caa51fcef9eded896d81d1cc20f07ed3935a8eb9` | exact |
| `decode_rows` | 604--718 | `9d18711794544e97ddad974f0ac2205a07bfb19557da9282bf4628eeeb619133` | derived; new counters, fixtures, and caps |

The future packet must contain `ROUTINE_LINEAGE.tsv`. For every row above it
must give the D02 name, line range, D02 body hash, D05 target name, D05 body
hash, and `EXACT` or `DERIVED`. Every `EXACT` target body must byte-match its
D02 body. Every `DERIVED` row must include a unified diff. A prose assertion
that a routine is "the D02 routine" is not evidence.

The imported dependency constants are also literal:
`RANDOM_BELOW_MAX=4096` and all 64-bit primality bases and candidate caps are
those inside the hashed bodies. D05 fixes `ROW_BITS_MAX=361`,
`ROWS_MAX=320`, `RESIDUAL_ROWS_MAX=64`, `SPLITS_MAX=20000`,
`REFINEMENT_GCD_MAX=1000000`, `BLOCKS_MAX=4096`, and
`EXPONENT_CELLS_MAX=262144`. A future manifest must hash the constant block
separately.

The following immutable result bytes may be used only as heuristic
motivation. They do not enter the D05 runtime projection.

| result artifact | SHA-256 |
|---|---|
| D02 `RESULT.md` | `9548db54f38c38f23e2b91dc5c14c7b440c294b995edcf84e173f33302fbe819` |
| D02 preflight `metrics.tsv` | `1d1d1d5c86e579d36da19b46bfa03d4237a888c2b1e06cbcc2032b619260b249` |
| D02 preflight `banks.tsv` | `be708656d7d2c7121e6e4dbc1c7933ac2c5ede4ad5e08a861b06d3889cb2be8e` |
| D02 preflight `blocks.tsv` | `2c369e2d91ce84d39792fb9e38ec7275c99861d68eddeb960758e90860ae0b08` |

## 2. Finite question

For the fixed public `U + POWER` two-curve bank, after all direct public
screens, complete support-at-most-two testing, saturated private-primary
peeling, and complete P66 decoding of a residual core, does the quotient by
the support-at-most-two span have a non-global normalized-root image?

Useful support-one and support-two relations are retained as factor
certificates. They are never quotiented away before their signed gcds are
recorded. If their span has non-global image, that factor certificate is the
terminal mathematical result and the induced normalized-root quotient is
explicitly undefined. The complete kernel and structural complement are
still computed. The search asks a finite quotient question only on the
global-low-image branch. It makes no probability or all-input claim.

## 3. Exact deterministic source proposal

The proposed 64-bit master seed is

`0x0F265D05C0DEC0DE`.

The future source must use the exact bodies in Section 1. If the key tuple is
`(x_0,...,x_{r-1})`, all entries are converted to `uint64_t` and

`h_0 = 0x0F265D05C0DEC0DE`,

`h_{j+1} = mix64(h_j xor mix64(x_j))`.

`seed_key` returns `h_r`. An `Rng` starts with that returned state, and each
draw replaces its state by `mix64(state)` and returns the new state. There is
no discarded warm-up draw. Production split codes are `0` for discovery and
`1` for heldout. Code `2` is reserved for preflight and cannot enter either
production corpus.

A production case RNG has the exact key tuple

`seed_key({0xC0A0, split, factor_bits, shape_id, case_index})`,

where shape IDs are `0=random`, `1=neighbor`, and `2=safe` and case indices
are `0,...,15`.

One case keeps one RNG across all 128 pair retries. On each retry, the draw
order is literal:

- `random`: call `random_prime(bits,false)` for `p`, then for `q`;
- `neighbor`: call `random_prime(bits,false)` for `p`, then consume one
  `rng.next()` and set `offset=2*(2+(draw mod 2048))`, then call
  `next_prime_same_bits(p+offset,bits)` if `p` is nonzero; and
- `safe`: call `random_prime(bits,true)` for `p`, then for `q`.

The neighbor offset draw is consumed even if the preceding prime request
returns zero. Each ordinary-prime request examines at most 200,000
candidates. Each safe-prime request examines at most 1,000,000 candidates.
Each candidate consumes exactly one RNG draw. Sort a nonzero distinct pair
so `p<q` before forming `N=p*q` and before storing its label.

Each modulus has exactly two proposed curve streams:

| curve | mode | domain | exact RNG key |
|---:|---|---:|---|
| 0 | `U` | 100 | `seed_key({0xEC265,split,bits,shape,index,100,0})` |
| 1 | `POWER` | 108 | `seed_key({0xEC265,split,bits,shape,index,108,1})` |

For `U`, choose nonzero `A` and unrestricted `x0,y0` as in the authenticated
routine. For `POWER`, choose nonzero `s` and set
`x0=s^2 mod N`, `y0=s^3 mod N`, and `A=s+1 mod N`. In both modes set

`B=(y0^2-x0^3-A*x0) mod N`.

Generate curve 0 completely before curve 1. Each stream keeps its own RNG
state through exactly 32 attempts. A `U` attempt draws
`A=1+random_below(N-1)`, then `x0=random_below(N)`, then
`y0=random_below(N)`. A `POWER` attempt draws only
`s=1+random_below(N-1)` before its displayed deterministic assignments.
Then compute `B` and the discriminant gcd. `B=0`, a full discriminant gcd,
or a literal duplicate clean tuple `(A,B,x0,y0)` consumes one attempt. The
only curve-tuple collision table is local to one bank. Curve 0 owns its
accepted tuple; a matching curve-1 proposal consumes a curve-1 retry. There
is no cross-bank curve-tuple collision rule. A proper discriminant gcd is a
direct factor and stops that bank. Attempt exhaustion is a resource
rejection.

Let

\[
 n=\lceil\log_2(N+1)\rceil,\qquad K=\min(2n,160).
\]

Each curve must complete every affine scalar from 1 through `K`. Retain all
of them. Row order is `(curve,index)`. A proper affine denominator or row-root
gcd is direct. A full gcd or unresolved global affine exception makes the
bank incomplete. No partial orbit reaches peeling or P66.

## 4. Cohorts and factor-label firewall

Factor sizes are `12,16,20,24,32,40,48,60` bits. Each split has 16 distinct
moduli for every factor-size and shape cell:

- `random`: two independent declared-size primes;
- `neighbor`: one declared-size prime and the next distinct prime after the
  exact imported small-offset draw; and
- `safe`: two distinct declared-size safe primes under the imported bounded
  generator.

Each split intends 384 moduli. Production modulus ownership uses one global
ordered map. Its total proposal order is

`split 0, then split 1; bits in 12,16,20,24,32,40,48,60 order; shape 0,1,2;
index 0,...,15`.

The first accepted tuple in this order owns its modulus. If a later tuple
proposes the same `N`, the owner is unchanged and the later tuple consumes
one of its 128 retries using its continuing case RNG. A failed tuple owns
nothing. To generate either production split in isolation, the executable
must replay this complete two-split order and discard the nonrequested split
only after all ownership decisions. Thus running heldout alone cannot change
a collision outcome. Preflight split 2 uses a separate empty ownership map
and never owns or rejects a production modulus. A shortfall is explicit and
is never backfilled from another cell.

The public `Case` object ends at `(split,bits,shape,index,N)`. A disjoint
`FactorLabel` store holds `p,q`. Curve construction, rows, screens, peeling,
P66, relation roots, counters, commit artifacts, and diagnostic selection
receive only the public case. Labels can be attached only after every public
worker for that split has joined. No factor can affect continuation,
eligibility, a result label, or diagnostic retention.

There is no family selection file. Discovery is exploratory and cannot
change held-out grammar, seeds, order, caps, or labels.

## 5. Complete screen and operation chronology

For each bank, use this exact order.

1. Generate both complete curves and orbits with discriminant, denominator,
   and row-root gcds before every unsafe operation.
2. For each row, run one exact singleton square test. On a hit, compute its
   exact positive root, verify the root and congruence, compute one modular
   inverse and one normalized-root multiplication, and compute exactly two
   signed normalized-root gcds.
3. In one canonical unordered-pair loop, run the direct coordinate controls,
   same-curve chord control, template comparisons, and complete support-two
   test specified below. There is no hidden second pair scan.
4. Run the canonical simultaneous saturated peel to its fixed point.
5. If at most 64 rows survive, run the complete P66 decoder. Otherwise emit
   `RESOURCE_REJECT_RESIDUAL_CORE`.
6. Independently of every earlier factor, verify the canonical low-span
   basis, construct the canonical structural complement, and verify each of
   its basis vectors using exact integer product squares, supplied modular
   roots, one modular inverse, and both signed gcds. If the low image is
   global, this structural complement is also the quotient complement. If
   the low image is non-global, record `UNDEFINED_LOW_IMAGE`; do not stop or
   reinterpret the complement as a quotient.
7. Commit all bank results and split labels as defined in Section 8.
8. Only after the commit, run bounded explanatory diagnostics.

Once both orbits are complete, all later public work finishes even if an
earlier direct or low-support factor was recorded. That factor is not used.
A truncated orbit, cap crossing, incomplete pair loop, incomplete peel,
incomplete P66 matrix, incomplete low RREF, incomplete complement, or failed
exact relation check is never eligible.

### 5.1 Exact unordered-pair ledger

For every unordered pair `(i,j)`, increment `unordered_pairs` once and
unconditionally perform:

1. `gcd(u_i-u_j,N)`;
2. `gcd(v_i-v_j,N)`;
3. `gcd(v_i+v_j,N)`;
4. if the curves agree, `gcd(H_ij,N)` with
   `H_ij=u_i^2+u_i*u_j+u_j^2+A`;
5. one integer gcd `d=gcd(a_i,a_j)`;
6. two exact divisions `a_i/d` and `a_j/d`; and
7. two exact integer-square tests on those quotients.

Equality, inverse, and square-multiple template comparisons use these same
values and add no second square-class scan. The unconditional counters are

- `coordinate_gcds = 3*unordered_pairs`;
- `same_curve_chord_gcds = same_curve_pairs`;
- `support2_gcds = unordered_pairs`;
- `support2_exact_divisions = 2*unordered_pairs`; and
- `support2_square_tests = 2*unordered_pairs`.

If and only if both quotient square tests pass, increment `support2_hits`,
form `s=d*x*y`, verify `s*s=a_i*a_j`, form
`V=(v_i*v_j) mod N`, verify `s*s=V*V (mod N)`, compute
`z=(s mod N)*invmod(V,N) mod N`, and compute exactly the two signed gcds
`gcd((s mod N)-V,N)` and `gcd((s mod N)+V,N)`. Thus every hit performs one
exact root construction, one exact product/root verification, one supplied
root modular multiplication, one modular inversion, one normalized-root
modular multiplication, and two signed gcds. The corresponding counters are

- `support2_root_constructions = support2_hits`;
- `support2_root_verifications = support2_hits`;
- `support2_supplied_muls = support2_hits`;
- `support2_inversions = support2_hits`;
- `support2_normalized_muls = support2_hits`; and

`support2_signed_gcds = 2*support2_hits`.

Because `V` is a unit, these two gcds equal `gcd(z-1,N)` and `gcd(z+1,N)`.
The source records both the supplied-root form and the normalized root and
asserts the equality of the two classifications.

For singleton hits, the exact analogous identities are
`singleton_root_constructions=singleton_root_verifications=
singleton_inversions=singleton_normalized_muls=singleton_hits` and
`singleton_signed_gcds=2*singleton_hits`. Its supplied root is the one stored
row root, so there is no singleton supplied-root product multiplication.

Every data-dependent counter is serialized even when zero. The support-two
signed-gcd bound is twice the unordered-pair count. Singleton signed gcds and
low/structural-basis signed gcds have separate counters. No signed gcd is
silently included in a generic pair counter.

## 6. Canonical peel and complete residual decoder

At each peel round, build one active product tree. For every active row,
derive the complementary product by exact division, compute the saturated
modular power, gcd, residual division, and square test, all against the same
active set. Delete all nonsquare residuals simultaneously. Serialize the
round number, active-set digest, deleted row IDs, `g_i`, `b_i`, the identity
`a_i=g_i*b_i`, and the square-test bit. A row-round cap crossing is a visible
resource rejection.

The residual core has at most 64 rows and at most 23,104 total row-value
bits. Its complete P66 path has these fail-safe caps:

- 20,000 gcd-free split/merge steps;
- 1,000,000 refinement-loop block-pair gcd comparisons;
- 4,096 final opaque blocks;
- 262,144 dense block-by-row exponent cells;
- 262,144 nonzero sparse exponent entries; and
- 64 kernel-basis vectors.

The decoder must check pairwise coprimality of final blocks, exact row
reconstruction, each block's exact-square status, every parity equation,
and every reported exact product square. A cap crossing rejects the bank. It
does not yield a partial matrix or a null.

Every support-one and support-two hit is enumerated and verified on the full
bank. Insert its 320-bit mask into a streaming canonical RREF in singleton
order followed by lexicographic pair order. This retains at most 320 pivot
masks while the complete hit counter and complete mask-stream SHA-256
continue. Peeled coordinates are zero in all kernel vectors, so restrict the
retained span basis to the fixed-point core and recompute its canonical RREF
`L_low`. Verify every vector of `L_low`.

Reduce the canonical P66 basis against `L_low` and earlier complement pivots
to obtain the canonical structural complement `Q` on every eligible bank.
Verify every vector of `Q`, even if a direct or low-support factor was
already recorded. If every low-basis root is global, set
`quotient_defined=true` and interpret `Q` as the quotient complement. If any
low-basis root is non-global, record its terminal low-support factor, set
`quotient_defined=false` and `quotient_status=UNDEFINED_LOW_IMAGE`, and mark
all `Q` root records `STRUCTURAL_ONLY_LOW_IMAGE`. They cannot supply a
quotient hit. No low-factor branch can skip a kernel, RREF, relation-root,
counter, commit, or diagnostic operation.

For each low-basis or structural-complement vector `C`, the common verifier
forms `A_C` by multiplying its selected positive rows and `V_C` by one
modular multiplication per selected row starting from one. It computes the
positive integer square root `s_C`, verifies `s_C^2=A_C` and
`s_C^2=V_C^2 (mod N)`, computes
`z_C=(s_C mod N)*invmod(V_C,N) mod N`, and computes exactly
`gcd((s_C mod N)-V_C,N)` and `gcd((s_C mod N)+V_C,N)`. Separate counters
record selected-row exact multiplications, supplied-root modular
multiplications, root constructions, both verifications, inversions,
normalized-root multiplications, and signed gcds. A basis vector is not
complete until all counters have advanced by their prescribed amounts.

## 7. Primary counters and held-out labels

`eligible` means that both orbits, the full singleton and pair ledgers, the
fixed-point peel, P66 decoder, streaming and final low RREFs, structural
complement, every prescribed relation verifier, and the mathematical core
commit completed under all caps. A recorded direct or low-support factor
does not make an otherwise completed bank ineligible. An incomplete or
resource-rejected bank is never eligible.

Each bank records at least:

- complete, eligible, bank-skip, and resource-reject status;
- direct factor, first direct screen, and strict status;
- rows, unordered pairs, and all seven pair-ledger counters;
- singleton square tests, hits, and signed gcds;
- peel rounds, row-round tests, peeled rows, and residual-core size;
- P66 refinement gcds, split steps, block count, dense and sparse exponent
  counts, kernel dimension, and verification count;
- low-generator count, streaming-RREF insertions, low dimension, low-basis
  root verifications, modular multiplications, inversions, and signed gcds;
- structural-complement dimension, basis root verifications, modular
  multiplications, inversions, signed gcds, `quotient_defined`, quotient
  dimension, and useful quotient hits;
- useful low-support factors; and
- diagnostic task, match, retention, truncation, and timeout counters.

A relation certificate gives the exact selected rows, exact positive root,
supplied modular root, normalized root, and both signed gcds. `strict useful
quotient` means that both orbits were complete and no earlier direct or
useful low-support screen produced a factor. Computation may continue for
evidence after an earlier factor, but such a quotient hit is not strict.

The held-out label is `finite_quotient_positive_signal` only if at least two
strict useful quotient-hit banks occur in at least two factor-size cells.

It is `finite_quotient_null_signal` only if:

- every eligible held-out bank completed its P66 kernel, low RREF,
  structural complement, and all registered root verifications;
- every eligible held-out bank has `quotient_defined=true`;
- no eligible held-out quotient-complement basis has a non-global image,
  whether or not a direct factor was recorded;
- at least 90 percent of the 384 intended held-out banks are eligible; and
- every factor-size/shape cell has at least 12 eligible banks.

Every other outcome is `finite_quotient_mixed_or_inconclusive`. In
particular, one useful low-support relation makes the quotient undefined and
prevents a quotient-null label. Useful singleton or support-two factors are
reported but do not by themselves satisfy the quotient-positive label.

## 8. Result commit and non-gating diagnostics

All core bank rows, relation masks, counters, certificates, and the split
summary are written first in canonical case order. The writer closes each
file, atomically renames its temporary file, computes its SHA-256, and writes
a `CORE_COMMIT.sha256`. The held-out decision is already present in the
committed split summary. No committed core file is reopened for writing.

The complete peel stream and complete opaque-block stream keep counters and
SHA-256 digests; retain only their first 32 detail records per bank in round/
row order and block-value order. The streaming low mask input keeps its
complete counter and digest and at most 320 in-memory pivots. Commit all
canonical low and structural-complement basis masks, at most 128 per bank.
Order full relation certificates by
`(split,bits,shape,index,relation_class,mask)` and retain the first 64 per
split. Every additional certificate advances the complete counter and
digest. Independently of that detail cap, every proper-factor occurrence
advances a complete factor-stream counter and digest. The bank summary keeps
the first canonical proper factor overall and the first in each of these 11
fixed source classes: `CURVE_DISCRIMINANT`, `AFFINE_DENOMINATOR`, `ROW_ROOT`,
`SINGLETON`, `PAIR_X`, `PAIR_Y_MINUS`, `PAIR_Y_PLUS`, `PAIR_CHORD`,
`SUPPORT2`, `LOW_BASIS`, and `STRUCTURAL_Q`. Each witness has its signed-gcd
side when applicable and its row, pair, or relation-mask coordinates. These
bounded witnesses are sufficient to verify every factor
class used by a label. The retention rules cannot change a bank status,
basis, root classification, or label.

Diagnostics then read only committed relation masks plus public row data.
They cannot mutate an eligibility bit, relation root, counter used by a
label, split summary, or core digest. A diagnostic failure or timeout writes
a separate diagnostic status and leaves the committed mathematical result
valid.

For explanatory diagnostics, process the first eight canonical structural-
complement vectors whose support is at most 16. This selection is identical
when `quotient_defined` is false; only its interpretation is structural. For
each support:

- process every same-curve pair;
- process every same-curve unordered triple through all three anchors
  `(i,j;k)`, `(i,k;j)`, and `(j,k;i)`;
- reject every cross-curve third row from the chord-root predicate; and
- for each anchor, sort its pair scalar indices as `alpha<=beta`, call the
  third index `gamma`, and aggregate tangent, chord, discriminant,
  third-root, `alpha+beta=gamma`, `beta-alpha=gamma`, `2*alpha=beta`,
  `3*alpha=beta`, `alpha*beta=gamma`, and
  `v2(alpha)=v2(beta)` over every executed task.

Here `v2(r)` is the exponent of 2 in the positive scalar index `r`.

The maxima are 960 same-curve pair tasks and 13,440 anchored-third-row tasks
per bank. Across 768 banks, the anchored maximum is 10,321,920.

Detailed records are ordered by
`(split,bits,shape,index,basis_ordinal,curve,pair_row_1,pair_row_2,third_row)`.
Retain only the first 64 detailed records per bank and the first 8,192 per
split in that order. Render a record in memory first. If it exceeds 4,096
bytes, omit it and increment `diagnostic_oversize_records`. Thus detailed
diagnostic bytes are at most 64 MiB across both splits. Truncation changes
only retained details. Complete aggregate counters continue.

The entire post-commit diagnostic phase has a 900-second wall cap and must
also leave the common five-minute finalization reserve. It runs as a
separate caught phase. A timeout marks the remaining aggregate cells
`DIAGNOSTIC_NOT_RUN_TIMEOUT`; it cannot change a core result or held-out
label. The record-count and byte truncation rules are deterministic; no
wall-clock prefix is represented as exhaustive.

## 9. Exact static task maxima

For declared factor-bit size `b`, `n<=2b`. The row and pair maxima are:

| factor bits | `K_max` | rows | unordered pairs |
|---:|---:|---:|---:|
| 12 | 48 | 96 | 4,560 |
| 16 | 64 | 128 | 8,128 |
| 20 | 80 | 160 | 12,720 |
| 24 | 96 | 192 | 18,336 |
| 32 | 128 | 256 | 32,640 |
| 40 | 160 | 320 | 51,040 |
| 48 | 160 | 320 | 51,040 |
| 60 | 160 | 320 | 51,040 |

There are 96 intended banks at each size across both splits. Therefore the
full packet has these registered maxima:

- 768 banks and 172,032 admitted rows;
- 22,032,384 unordered row pairs;
- 10,973,184 same-curve pairs and 11,059,200 cross-curve pairs;
- 66,097,152 direct coordinate gcds;
- 10,973,184 direct same-curve chord gcds;
- 22,032,384 support-two integer gcds;
- 44,064,768 support-two exact divisions;
- 44,064,768 support-two square tests;
- at most 22,032,384 support-two root constructions, product/root
  verifications, supplied-root modular multiplications, modular inversions,
  and normalized-root modular multiplications;
- 172,032 singleton square tests and at most 172,032 complete singleton
  relation verifications;
- at most 22,204,416 streaming low-RREF insertions;
- at most 98,304 complete low-plus-structural-basis relation verifications;
- at most 22,302,720 complete relation verifications and 44,605,440 signed
  relation gcds across singleton, support-two, low-basis, and structural-
  complement vectors;
- at most 6,291,456 selected-row exact-product multiplications and the same
  number of supplied-root modular multiplications inside the 98,304
  maximum-support basis verifications;
- 22,204,416 peel row-round tests;
- at most 377,475,072 peel modular multiplications under the algebraic
  per-row bound;
- 115,520 bits in one maximum active product;
- 64 residual rows and 23,104 residual row bits per eligible P66 decoder;
- at most 20,000 decoder split/merge steps, 1,000,000 refinement block-pair
  gcds, 4,096 final blocks, 262,144 dense exponent cells, 262,144 nonzero
  exponent entries, and 64 kernel vectors per eligible bank;
- 737,280 relation-local diagnostic pair tasks; and
- 10,321,920 relation-local anchored-third-row tasks.

Every maximum is checked in the executable. A counter mismatch aborts the
phase. A cap crossing is visible. It cannot reduce a denominator in a
frequency label without also reducing eligibility.

## 10. Task-specific dynamic preflight

D05 uses no D02 work-unit ratio. Its own executable must pass all of the
following source-independent and real-bank measurements before production is
opened. All timers are monotonic wall timers. Fixture repetitions run
serially. The executable records CPU time and operation counters as audit
data, but only the displayed wall-time maxima enter the gate.

### 10.1 Real generation and bank measurements

Using preflight split code `2`, generate four public cases for every one of
the 24 factor-size/shape cells, with indices `0,...,3`. This is a 96-case
generation fixture. Record wall and CPU time separately for each case and
the exact prime-candidate, retry, and random-draw counters.

For each 60-bit shape, scan preflight indices `64,...,127` in increasing
order until the first bank completes both 160-scalar curves. This gives one
320-row real bank per shape. Every attempted case and rejection is retained.
Failure to obtain all three banks within the exact 64-index range fails the
preflight. Each accepted real bank runs the complete singleton, pair, peel,
residual-P66, basis-verification, core-serialization, and diagnostic-input
construction paths. A residual core above 64 or any cap crossing fails the
preflight instead of becoming a cheap timing sample.

Instrument disjoint times for `orbit_base`, `pair_base`, `peel`, and
`core_commit`. `orbit_base` contains curve attempts, affine work, all direct
orbit screens, row construction, and singleton square tests, but excludes a
singleton-hit relation verifier. `pair_base` contains every unconditional
operation in Section 5.1, but excludes the support-two hit verifier and its
low-RREF insertion. `peel` contains product-tree construction, every
complementary exact division, every saturated modular multiplication, gcd,
residual division, square test, deletion, and digest update. No production
operation can be assigned to two of these base timers. Record exact rows,
pairs, hit counts, row-round tests, operation counters, and committed bytes
for each real bank.

### 10.2 Cap-complete P66 decoder suite

The suite calls the same refinement primitive, terminal verifier, parity
builder, and kernel verifier used by production. A benchmark-only injection
point may supply an already-refined block state. That injection point is not
reachable from a production mode.

First, form consecutive Fibonacci integers `F_520,F_521` with
`F_0=0,F_1=1`. Assert their bit lengths are 360 and 361 and their gcd is one.
In each of eight repetitions, call the production integer gcd on this pair
65,536 times. Let `rho_dgcd` be the largest repetition time divided by
65,536. This deliberately charges a long Euclidean quotient chain at the
maximum row-value width.

Second, for every `t=0,...,19999`, put

`x_t=2^359+4t+3`, `y_t=x_t+2`.

Assert `gcd(x_t,y_t)=1` and `gcd(2x_t,2y_t)=2`. Give the two operands
64-entry exponent vectors with a unit entry at `t mod 64` and
`(t+1) mod 64`, respectively. Apply the exact production split/merge
primitive, including gcd, both exact divisions, exponent addition, overflow
check, and result construction. For each timed call, the selected operands
occupy the first and last positions of a 4,095-live-block production
container; the call includes both erases, the worst-position shift, three
appends, and the resulting 4,096-block cap check. A benchmark-only driver
restores that prebuilt state between calls. Restoration is outside the
per-call timer but inside the 1,800-second preflight wall. One repetition
therefore executes exactly 20,000 permitted split steps on 361-bit operands
with near-cap container mutation. Run four repetitions and let
`T_split20k` be the largest sum of the 20,000 per-call times.

Third, take the first 4,096 rational primes at least 4,099. Block `t` has a
dense 64-entry exponent vector with ones at rows `t mod 64` and
`(t+1) mod 64`. Inject these 4,096 pairwise-coprime blocks into the exact
terminal verifier. Define each synthetic row as the product of its incident
blocks. The verifier must assert:

- exactly 4,096 final blocks and 262,144 scanned dense exponent cells;
- exactly 8,192 nonzero exponent entries;
- exact reconstruction of all 64 rows and pairwise block coprimality;
- parity rank 63 and the one-dimensional all-one kernel; and
- exact square root equal to the product of all 4,096 blocks for the
  all-row relation.

Run this terminal fixture four times and let `T_terminal4096` be the largest
wall time. It exercises the literal block cap, full terminal pair scan,
reconstruction, matrix construction, RREF, kernel verification, and exact
all-row product/root check. It is intentionally larger than any core implied
by the 23,104-bit production row-total cap. It supplies no source evidence.

The fourth fixture has

\[
 a_i=(181\cdot2^{173}+2i+1)^2,\qquad 0\le i<64.
\]

It must assert no peel deletion, a zero parity matrix after exact-square
blocks are removed, and kernel dimension 64. It exercises maximal basis
construction and exact-square verification. Run it four times and let
`T_square64` be the largest wall time.

The registered conservative per-bank decoder charge is

\[
 \rho_{\rm decoder}=T_{\rm split20k}+T_{\rm terminal4096}+T_{\rm square64}
 +\rho_{\rm dgcd}\left(1{,}000{,}000+\binom{4096}{2}\right).
\]

The terminal fixture already executes its final pair scan. The last term
charges that scan a second time at the 360-bit Fibonacci-gcd rate and also
charges the complete refinement-gcd cap. This is deliberate domination, not
an empirical average. The suite therefore exercises the allowed 20,000
splits and 4,096 blocks and has a defined scaling rule for every failed gcd
comparison. A fixture assertion failure closes production.

### 10.3 Complete relation and low-RREF fixtures

Set `p_rel=2^61-1`, `N_rel=p_rel^2`, and

\[
 w_i=181\cdot2^{173}+2i+1,\quad a_i=w_i^2,\quad
 v_i=w_i\bmod N_{\rm rel},\qquad0\le i<64.
\]

Assert with the exact imported 64-bit primality routine that `p_rel` is
prime, assert that `N_rel` has 122 bits, every `v_i` is a unit, every row has
exactly 361 bits, the all-row product has exactly 23,104 bits, and
`a_i=v_i^2 (mod N_rel)`. Run the exact production relation
paths in 16 repetitions, with disjoint timers:

1. verify all 64 singleton relations, including the exact positive root,
   congruence check, one modular inverse, normalized-root multiplication,
   and both signed gcds;
2. verify all 2,016 support-two hits, starting with `d=gcd(a_i,a_j)` and its
   two quotient roots, then executing `d*x*y`, exact product/root
   verification, supplied-root modular multiplication, congruence check,
   modular inverse, normalized-root multiplication, and both signed gcds;
3. verify 64 tagged copies of the all-row support, including all 64 supplied-
   root modular multiplications, the 23,104-bit product and root, modular
   inverse, normalized-root multiplication, and both signed gcds.

Let `rho_rel1`, `rho_rel2`, and `rho_rel64` be the maximum corresponding
single-repetition time divided by 64, 2,016, and 64. These three charges
include every root construction and verification, every supplied-root
modular multiplication, every relation inversion, and every signed relation
gcd. There is no separate sampled signed-gcd proxy.

For the streaming low-RREF fixture, use 320-bit masks. Insert the 320 unit
masks in increasing pivot order. Then insert the all-one mask 51,040 times.
Every repeated mask crosses all 320 established pivots and reduces to zero.
One repetition has exactly 51,360 insertions, the maximum support-one plus
support-two mask count of one 320-row bank. Run eight repetitions and set

\[
 \rho_{\rm lowinsert}=
 {\max T_{\rm lowinsert,51360}\over 51360}.
\]

For the low-finalization fixture, restrict a 320-pivot full-width basis to a
fixed 64-coordinate survivor set, canonicalize it, and then run a second
case with zero low basis and a 64-vector P66 basis so all 64 structural-
complement insertions survive. The exact production restriction, canonical
RREF, and complement routines must run in both cases. Run the combined
fixture 16 times and let `rho_lowfinal` be the largest combined time. This
is charged once to every intended bank.

### 10.4 Valid same-curve diagnostic fixture

Use the prime modulus `N_diag=1,000,003`, the curve

\[
 y^2=x^3+2x+3\pmod {N_{\rm diag}},
\]

and base point `(3,6)`. Generate scalar multiples `1P,...,16P` with the exact
production `add_points` routine. For row `i`, set its curve ID to zero, its
scalar index to `i`, `u_i=x(iP)`, `v_i=y(iP)`, `A=2`, `B=3`, and
`a_i=u_i^3+2u_i+3` over the integers. Assert primality, discriminant gcd one,
16 distinct affine points, unit `v_i`, and
`a_i=v_i^2 (mod N_diag)`. The SHA-256 of the 16 LF-terminated decimal lines
`index<TAB>u<TAB>v<TAB>a` with no header must be

`21b54a1a899c715deff060cd44dcb48b9573c04935836383f76287b8e99a8b83`.

Pass eight tagged copies of this valid same-curve 16-row support to the exact
production diagnostic function. It must execute 960 pair tasks, 13,440
anchored-third-row tasks, complete aggregates, all six index predicates, and
the same 64-record detail cap as one maximum production bank. Run it 16
times. Let `rho_diag` be the largest individual-call wall time. No graph
fixture or invented curve metadata enters this timing claim.

### 10.5 Commit, output-throughput, and explicit projection

The maximum retained core payload attributable to one bank is 442,368 bytes:
one 16,384-byte bank record, 320 row records of at most 512 bytes, 32 peel
records of at most 2,048 bytes, 32 block records of at most 4,096 bytes, and
128 basis-mask records of at most 512 bytes. Run the exact production
temporary-write, close, atomic-rename, SHA-256, and commit-record path on this
payload eight times. Let `rho_commit` be the largest call time.

Separately, run the same atomic writer and hasher on exactly 67,108,864 bytes
four times. Let `rho_io` be the largest time divided by 67,108,864. The
projection charges every final output byte at this rate in addition to the
per-bank commit charge.

For each generation cell `c`, let `gamma_c` be the maximum single-case
generation time among its four preflight cases. Let

\[
 \rho_{\rm orbit}=\max_s
   {T_{{\rm orbit\_base},s}\over R_s},
\quad
 \rho_{\rm pair}=\max_s
   {T_{{\rm pair\_base},s}\over P_s},
\]

\[
 \rho_{\rm peel}=\max_s
   {T_{{\rm peel},s}\over W_s},
\quad
 \rho_{\rm commit,real}=\max_s T_{{\rm core\_commit},s},
\]

where `s` runs over the three real shapes, `R_s` is its row count, `P_s` its
unordered-pair count, and `W_s` its nonzero peel row-round count. A zero
denominator fails the preflight.

Use the registered worst-case counts

\[
 R_{\max}=172032,\quad P_{\max}=22032384,
\quad W_{\max}=22204416,
\]


`H_max=R_max+P_max=22,204,416`,

`V_basis,max=128*768=98,304`, and the literal final-output cap
`C_final=588,251,136` bytes from Section 11.

The raw production projection is exactly

\[
\begin{aligned}
 T_{\rm raw}={}&
 32\sum_{c=1}^{24}\gamma_c
 +\rho_{\rm orbit}R_{\max}
 +\rho_{\rm pair}P_{\max}
 +\rho_{\rm peel}W_{\max}\\
 &+\rho_{\rm rel1}R_{\max}
 +\rho_{\rm rel2}P_{\max}
 +\rho_{\rm lowinsert}H_{\max}\\
 &+768\rho_{\rm lowfinal}
 +768\rho_{\rm decoder}
 +\rho_{\rm rel64}V_{\rm basis,max}\\
 &+768\max(\rho_{\rm commit},\rho_{\rm commit,real})
 +768\rho_{\rm diag}
 +\rho_{\rm io}C_{\rm final}.
\end{aligned}
\]

The factor 32 is the intended number of cases per production cell across
both splits. It uses the slowest of the four same-cell preflight cases. The
relation terms charge every possible singleton and pair as a hit and every
eligible bank for 128 maximum-support basis verifications. The low-insertion
term charges every possible low mask. The decoder term charges every bank at
all decoder caps. The diagnostic term charges a maximum diagnostic bank to
every bank. These are deliberately conservative finite runtime estimates,
not complexity proofs.

Set

\[
 T_{\rm projected}=1.75T_{\rm raw}.
\]

Production remains closed unless `T_projected <= 12,600 seconds` and also
fits within the live common deadline after subtracting elapsed
authentication, compilation, self-test, and preflight time plus a 300-second
finalization reserve. It also remains closed unless
`1.75*768*rho_diag <= 900 seconds`, matching the separate diagnostic cap.
No D02 elapsed time, unmeasured hit path, or undefined mixed work proxy
appears in this formula.

## 11. Resource, output, and timeout gates

The entire remote runner has one four-hour wall cap, starting before
authentication and compilation. It uses at most eight workers and `nice 15`.
Before every phase it rejects overlap, load above twice the visible CPU
count, less than 8 GiB available memory, or less than 4 GiB free disk.

The runner and every child inherit a 4 GiB virtual-memory cap and a 128 MiB
per-file cap. Measured peak RSS must be at most 3.5 GiB. The complete
preflight has a 1,800-second cap. Every production executable uses the
remaining common deadline minus the five-minute finalization reserve.

Evaluation uses deterministic batches of at most 64 banks and at most eight
workers. Each worker has a 256 MiB arena cap. A completed bank is written to
its bounded temporary artifact and releases its arena; only its path and
fixed counters wait for case-order commit. Writer and scheduler storage is
capped at 512 MiB. Thus the static in-memory allowance is
`8*256 MiB+512 MiB=2.5 GiB`, before allocator and executable overhead. The
measured whole-process peak RSS must still be at most 3.5 GiB.

Every complete stream is hashed while it is generated. Detail truncation
never truncates a counter or digest. The final artifact categories and hard
byte maxima are literal:

| final category | exact byte cap |
|---|---:|
| 768 bank summaries, 16,384 bytes each | 12,582,912 |
| 64 cell/split/global/hash summaries, 16,384 bytes each | 1,048,576 |
| 172,032 public row records, 512 bytes each | 88,080,384 |
| 32 peel details per bank, 2,048 bytes each | 50,331,648 |
| 32 opaque-block details per bank, 4,096 bytes each | 100,663,296 |
| 128 low/structural basis-mask records per bank, 512 bytes each | 50,331,648 |
| 64 full relation certificates per split, 65,536 bytes each | 8,388,608 |
| diagnostic details across both splits | 67,108,864 |
| corpora, labels, ownership and retry ledgers | 8,388,608 |
| all preflight artifacts | 134,217,728 |
| all stdout, stderr, time, and resource logs | 33,554,432 |
| sources, binary, manifests, and hash catalogs | 33,554,432 |

The first seven mathematical-core rows total 311,427,072 bytes. All rows
total exactly 588,251,136 bytes. There is no measured or undefined
"variable portion." Before appending a record, render it in memory and check
its row-category limit. On overflow, omit only a detail record, increment its
oversize counter, and continue its complete stream digest. A bank summary,
public row, basis mask, factor certificate needed for a reported terminal
factor, aggregate, or digest overflow is a core resource rejection, never a
truncation.

A public row record stores only fixed integer IDs plus lowercase hexadecimal
`u,v,a,carry`; its bank summary stores `N,A,B,x0,y0`. Because
`0<=u,v,A,B<N<2^120`, the cubic row satisfies `a<N^3` and
`|carry|=|a-v^2|/N<N^2`. Thus there are at most 30 hex digits for each
residue, 90 for `a`, and 60 plus one sign for `carry`, so the 512-byte
rendered-row cap has explicit slack. A basis mask is exactly five
64-bit hexadecimal words plus fixed IDs and root-class fields. A peel detail
contains one row ID and its at-most-361-bit `a_i,g_i,b_i`. A block detail
contains one at-most-361-bit value and at most 64 `(row,exponent)` entries.
The writer still measures each rendered record; these formulas do not waive
the hard byte checks.

The largest one-bank temporary is 442,368 bytes. At most 64 such temporaries
can wait for ordered commit. Atomic replacement can additionally duplicate
the 134,217,728-byte preflight category. Therefore the registered peak
experiment-directory bound is

`588,251,136 + 64*442,368 + 134,217,728 = 750,780,416 bytes`,

which is below 768 MiB. The executable checks each category, final total,
temporary total, and peak directory bytes after every commit. The per-file
cap is 128 MiB. No result mode may relax these limits.

Any wall, memory, task, record, or byte cap failure is explicit. A core cap
failure makes the affected bank ineligible. A post-commit diagnostic cap or
timeout changes only diagnostic status.

## 12. D02 heuristic motivation and novelty boundary

The exact D02 result bytes in Section 1 report 18,790 generated rows,
2,369,895 pair controls, 41,719 gcd-free splits, 9,450,761 chord-pattern
operations, and a resource projection stop before discovery. In the exact
hashed bank/block evidence, 105 banks reached P66 and all 18,670 rows in
those banks had an odd nonsquare opaque block incident only to that row.
That finite observation motivated testing private-primary peeling. It is not
a runtime calibration, a source theorem, or evidence about D05 cohorts.

P217/F252 already establishes the structural precedent of factor-free
saturation and private-pivot removal for a polynomial Pell bank. D05 claims
no new elliptic source theorem beyond that boundary. Its proposed novelty is
only a source-agnostic iterative decoder optimization and a finite test of
the resulting explicit cubic-row core.

## 13. Audit gate

Before source is written, a fresh no-context hostile theory review must try
to kill:

- valuation saturation and simultaneous fixed-point deletion;
- kernel and normalized-root preservation;
- support-two completeness and every operation counter;
- the normalized-root homomorphism and basis sufficiency;
- deterministic completion after a low-support factor and the fully defined
  `finite_quotient_null_signal` gate;
- same-curve chord provenance and all three anchors per unordered triple;
- core-result commit before diagnostics and diagnostic noninterference;
- deterministic diagnostic retention and all output/time caps;
- exact seeds, domains, corpus disjointness, and D02 byte imports;
- the 20,000-split/4,096-block decoder suite, refinement-gcd scaling, complete
  relation/RREF charges, and valid same-curve diagnostic fixture;
- every static maximum and projection term; and
- the honest P217/F252 novelty boundary.

A passing theory review authorizes drafting source only. It does not
authorize freezing, compilation, preflight, or remote execution.
