# F265 preregistration: elliptic cubic-lift symbolic search

## 1. Frozen question

For public factor-free modular elliptic curves, do canonical cubic rows

\[
 a_k=u_k^3+Au_k+B\equiv v_k^2\pmod N
\]

produce exact nonduplicate square-class relations whose normalized root is
non-global, after all cheaper public gcd screens have failed?

The search also asks which exact tangent, chord, carry, index, and
square-multiple patterns explain verified global or useful relations.

The closest prior route is X14/P20. F265 differs because it does not form the
`sqrt(N)`-length cleared collision product. It searches the full P66 kernel
of a small-index cubic-lift bank.

## 2. Immutable source rules

All source randomness is deterministic from `(split, factor_bits, shape,
case_index, family_id, curve_index)` and the frozen 64-bit master seed

`0xF265E11C0B1C5EED`.

It never reads `p` or `q` after forming `N`. The hidden factors are used only
to generate cohort moduli and to label a final certificate after every
public computation is complete.

For every curve attempt, the source chooses `A,x0,y0` by one of the modes
below and sets

`B = (y0^2 - x0^3 - A*x0) mod N`.

It rejects `B=0` and a full discriminant gcd. A proper discriminant gcd is a
direct factor. Each curve has at most 32 seed attempts. Exhaustion is a
resource rejection, not a null result.

Orbit arithmetic is factor-first affine arithmetic from `ALGEBRA.md`.
Every proper denominator gcd stops that bank. A global point at infinity is
handled by the group law. No factor is used to continue an orbit.

## 3. Frozen family grammar

Each family uses two curves. Let

`n = ceil(log2(N+1))` and `K = min(multiplier*n, 192)`.

The modes are:

- `U`: `A,x0,y0` are independent uniform residues, with `A` nonzero.
- `XS`: `x0` is uniform in `[1,2^min(16,n-1)-1]`; the other values use `U`.
- `YS`: `y0` is small by the same rule.
- `AS`: `A` is small by the same rule.
- `CENTER`: each value is uniform in the central half of `[0,N)`.
- `POWER`: for uniform nonzero `s`, set `x0=s^2`, `y0=s^3`, and `A=s+1`
  modulo `N`.

The schedules emit these scalar indices after the sequential orbit has been
computed:

- `ALL`: every index;
- `ODD`: index 1 and every odd index;
- `PRIME`: index 1 and every prime index;
- `LOWHAM`: index 1 and indices with binary Hamming weight at most two.

The twelve candidates are frozen as follows.

| ID | Mode | Schedule | Multiplier | Domain |
|---:|---|---|---:|---:|
| 0 | U | ALL | 1 | 100 |
| 1 | U | ALL | 2 | 101 |
| 2 | U | ODD | 2 | 102 |
| 3 | U | PRIME | 3 | 103 |
| 4 | XS | ALL | 2 | 104 |
| 5 | YS | ALL | 2 | 105 |
| 6 | AS | ALL | 2 | 106 |
| 7 | CENTER | ALL | 2 | 107 |
| 8 | POWER | ALL | 2 | 108 |
| 9 | POWER | ODD | 3 | 109 |
| 10 | U | LOWHAM | 4 | 110 |
| 11 | XS | PRIME | 4 | 111 |

Any source change creates a new version. Discovery cannot add a family.

## 4. Cohorts and firewall

Factor sizes are

`12,16,20,24,32,40,48,60` bits.

For each size and each shape, generate 16 distinct balanced semiprimes.

- `random`: two independent random primes of the declared bit size;
- `neighbor`: one random prime and the next distinct prime after a public
  small offset;
- `safe`: two distinct safe primes generated under the same bounded rule. A
  cell that does not reach 16 distinct pairs is reported as a shortfall.

There are 384 intended moduli in discovery and 384 in heldout. The split
uses disjoint seed domains and enforces global modulus distinctness. The
source records any shortfall. A shortfall is not silently backfilled from a
different shape.

The fixed `N=10403` synchronization reconstruction is a self-test only. It
does not enter either split.

Discovery evaluates all 12 families. It writes a deterministic selection
file. The runner hashes this file with SHA-256 and verifies the hash before
heldout starts. Heldout evaluates only the four selected family IDs.

The held-out evaluator cannot see discovery certificates. It reads only the
authenticated family-ID file.

## 5. Cleanup and direct controls

For every bank, perform these controls before a later P66 result can count as
strict:

1. curve discriminant gcd;
2. every affine denominator gcd;
3. every row-root gcd;
4. singleton exact-square root comparison;
5. all pairwise `x`-difference and signed-`y` gcds;
6. all same-curve chord-expression gcds with `N`;
7. equal-row and inverse-root comparison;
8. every exact square-multiple pair and its normalized-root gcds.

A proper factor from any item is `direct`. The source may finish exact
analysis of already public rows, but no later event in that bank is `strict`.

## 6. Exact decoder and certificates

The gcd-free decoder retains exact exponent vectors. It verifies:

- pairwise coprimality of final opaque blocks;
- exact reconstruction of every row;
- exact nonsquare status for each parity block;
- every binary-kernel equation;
- every reported product as an exact integer square; and
- every normalized-root signed gcd.

Opaque block factorization is reported as `UNKNOWN_NOT_NEEDED`. It is never
used as a primality or private-prime assertion. No Pollard-Rho inference is
part of the correctness path.

For each split and family, at most 64 full relation certificates are
serialized. Aggregate counters continue after this cap. A certificate gives
`N,A,B`, curve/index/coordinate provenance, all selected rows, the exact
root, supplied root product, normalized root, both gcds, carry values, and
the fixed template label.

## 7. Frozen template labels

Every verified basis relation receives the first applicable label:

1. `SINGLETON`;
2. `INVERSE_DUPLICATE`;
3. `EQUAL_ROW`;
4. `SQUARE_MULTIPLE_PAIR`;
5. `TANGENT_SUPPORTED`;
6. `CHORD_SUPPORTED`;
7. `DISCRIMINANT_SUPPORTED`;
8. `CROSS_CURVE`;
9. `OTHER_SAME_CURVE`.

The root class is separately `GLOBAL_PLUS`, `GLOBAL_MINUS`, or `USEFUL`.
No template label implies a root class.

For chord-supported blocks, the source tests the third-root congruence
`u+v+w=0 mod block` when a third incident coordinate exists. It records
index formulas from the frozen menu

`i+j=k`, `|i-j|=k`, `2i=j`, `3i=j`, `i*j=k`, and equal binary valuation.

These tests mine patterns. They do not prove an unbounded theorem.

## 8. Discovery selection rule

For each family, compute integer counters. Rank by this frozen tuple:

1. strict-hit banks per million eligible banks, descending;
2. strict useful basis relations, descending;
3. banks with a verified residual nonduplicate relation, descending;
4. total verified residual nonduplicate relations, descending;
5. chord-supported verified relations, descending;
6. eligible banks, descending;
7. admitted rows, ascending;
8. family ID, ascending.

`eligible` means the curve bank reached the decoder and every exact
certificate check passed. A resource rejection is not eligible. Select the
first four families. Ties use exact integer cross-products before the final
tuple fields; no floating-point rank can change selection.

The exact selection bytes contain the version, discovery cohort hash, rank
tuple, and the four IDs in order.

## 9. Held-out decision labels

The result is `finite_positive_signal` only if heldout has at least two
strict-hit banks in at least two different factor-size cells.

It is `finite_null_signal` only if:

- no held-out bank has a strict useful relation;
- at least 90 percent of intended selected-family banks are eligible; and
- every factor-size/shape cell has at least 12 eligible moduli for one
  selected family.

All other outcomes are `finite_mixed_or_inconclusive`.

None of these labels is an asymptotic conclusion.

## 10. Resource contract

The target host has a 4-hour wall cap for the complete packet. The runner
uses at most eight workers, `nice 15`, a 4 GiB virtual-memory cap, and a 1
GiB output-file cap.

Static maxima are:

- factor bits: 60;
- row bits: 361;
- scalar index: 192;
- curves per bank: 2;
- admitted rows per bank: 384;
- exact relation-product bits: at most 138,624 before a small guard margin;
- full certificates: 64 per family/split.

Ordinary prime generation has 200,000 candidates per request. Safe-prime
generation has 1,000,000 candidates per request. One cohort case has 128
pair retries. A failed case becomes an explicit shortfall. Curve generation
has 32 attempts. Gcd-free refinement has at most 20,000 split/merge steps,
4,096 final opaque blocks, and 160,000 total row bits. Crossing a cap emits
`RESOURCE_REJECT` and makes the bank ineligible. No opaque-block
factorization is attempted, so there is no unbounded Pollard--Rho retry.

Before discovery, a preflight runs a scaled corpus. It reports wall time,
CPU time, peak RSS, rows, pair controls, gcd-free splits, and projected full
runtime. The runner stops unless projected wall time is at most 12,600
seconds and peak RSS is at most 3.5 GiB. This leaves 30 minutes for compile,
self-test, serialization, and variance.

## 11. Launch gate and interpretation

The packet can be compiled and self-tested only after the static files are
frozen. Remote dynamic validation and every cohort are `PENDING` while F258
uses the host. A fresh hostile pre-run audit must pass before any cohort.

The search is finite evidence. A useful certificate is real factoring of its
displayed modulus, but it is not an all-input probability theorem. A null is
only a null for this frozen grammar and corpus.
