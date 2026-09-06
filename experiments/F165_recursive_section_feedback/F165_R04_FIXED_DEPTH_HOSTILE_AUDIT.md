# F165-R04 fixed-depth theorem: hostile audit

Status: hostile audit PASS. This report does not edit or promote a durable
ledger claim.

## Audited artifact and scope

Audited proof:

`F165_R04_V2_FIXED_DEPTH_PROOF_DRAFT.md`

SHA-256:

`39a36e862162d405d15943f59995010c1471e6af8baef6e2b7b9d7f984a9b380`

Audited statement source:

`V2_BLIND_STATEMENT.md`

SHA-256:

`1681967c7ac14b44361d58284716250e73a7f8bda15203f3bc2d6a4971139cdd`

The audit checks only this claim: if the explicit base transcript has
quasipolynomial total bit length, `R_0 <= 2^(C L^a)`, the support cap satisfies
`D <= L^b`, and the number of layers `H` is fixed independently of the input,
then generation, retention, complete factor-free refinement, and full decoding
through layer `H` use `2^(L^(O_H(1)))` bit operations and space.

The audit does not use the finite F165 replay to prove an unbounded bound.

## Verdict

**PASS.** I found no counterexample, missing asymptotic factor, uncontrolled
integer length, or hidden factoring call. The proof establishes the stated
fixed-depth upper bound.

The dependence on fixed `H` is essential. The proof does not establish a
uniform quasipolynomial bound when `H` grows with the input. It also proves no
factor certificate exists at any depth.

## 1. Layer attempt count

At layer `h`, the selected basis has rank `r_h <= R_h`. The number of attempted
nonempty subsets is

\[
M_{h+1}=\sum_{d=1}^{\min(D,r_h)}\binom{r_h}{d}.
\]

For every `d <= D`, `binom(r_h,d) <= (R_h+1)^D`. There are at most `D+1`
terms. Therefore

\[
M_{h+1}\le (D+1)(R_h+1)^D.
\]

At most one record is retained per attempt, so

\[
R_{h+1}\le R_h+M_{h+1}.
\]

If `R_h <= 2^(L^k_h)` and `D <= L^b`, then

\[
\log_2(M_{h+1}+1)
  =O(D\log(R_h+1)+\log(D+2))
  =L^{O(k_h+b+1)}.
\]

Thus one layer maps a quasipolynomial record count to another
quasipolynomial record count. The bound includes `D=0`, rank zero, and an empty
ledger after a fixed constant adjustment for small `L`.

## 2. Generated integer lengths

Each decorated lift is reduced modulo `N` after every multiplication and block
correction. It has `O(n)` bits. A selected lift is a unit. Each parity block
used in a correction divides a unit relation value, so it is also a unit
modulo `N`. Its modular inverse can be computed with the extended Euclidean
algorithm. If this unit invariant fails, the gcd already exposes a factor and
cannot increase the cost.

For a generated residue `1 <= z < N`, its least positive inverse satisfies
`1 <= w < N`. The retained exact value is

\[
A=zw<N^2.
\]

Thus each generated value and residue has `O(n)` bits. A subset reference has
at most

\[
D\lceil\log_2(R_h+1)\rceil
\]

bits. Compact references are sufficient. Expanded recursive provenance is not
required by the algorithm or theorem.

Let `S_h` be the complete retained transcript length. Generation can use a
fixed polynomial amount of work and metadata per attempt. Therefore

\[
S_{h+1}\le S_h+M_{h+1}
  \operatorname{poly}(n,D,\log(R_h+1),S_h).
\]

Since `n <= 2^L`, this recurrence preserves the form
`S_h <= 2^(L^s_h)` at each fixed layer. It counts duplicate attempts. A
balanced comparison tree keyed by exact value gives a deterministic
alternative to hashing.

## 3. Factor-free refinement

Represent each component by a positive base `q` and a sparse multiplicity
vector `(e_(q,i))_i`. The invariant is

\[
A_i=\prod_q q^{e_{q,i}}
\]

for every retained labelled value.

Both transformations preserve this invariant:

1. If `q=r^e`, replace `(q,v)` by `(r,e v)`.
2. For bases `x,y` with `g=gcd(x,y)>1`, replace them by `g`, `x/g`, and
   `y/g`. Give `g` the sum of the old multiplicity vectors. Give each quotient
   its corresponding old vector. Merge equal bases.

Use the potential

\[
\Phi=\sum_{\text{distinct live bases }q}\log_2 q.
\]

Initially `Phi <= S_h`. A perfect-power extraction decreases `Phi` by at
least one. For a gcd split, the replacement contribution is at most

\[
\log_2 g+\log_2(x/g)+\log_2(y/g)
=\log_2 x+\log_2 y-\log_2 g.
\]

Since `g >= 2`, this also decreases `Phi` by at least one. Merging an equal
base only decreases it further. Hence there are at most `S_h` transformations.

There are initially at most `R_h` components. A gcd split increases the live
component count by at most one. Perfect-power extraction does not increase it.
Thus at most `R_h+S_h` components are live at any time.

All component bases are divisors of prior explicit values. Their lengths are
bounded by `S_h`. Each multiplicity is bounded by the corresponding exact
integer valuation, so its binary length is also polynomial in `S_h`. A naive
scan of all component pairs at every transformation is still polynomial in
`S_h`.

Perfect-power extraction does not call factoring. Test exponents up to the
base bit length and use exact integer-root computation. This uses polynomial
bit complexity. Gcd, division, multiplication, and sparse-vector addition are
also polynomial.

At termination, the bases are pairwise coprime and are not perfect powers.
Splitting each multiplicity into its even part and parity gives

\[
A_i=s_i^2\prod_j q_j^{v_{j,i}},\qquad v_{j,i}\in\{0,1\}.
\]

The expression is unique relative to these pairwise coprime bases. Components
that have even multiplicity in every record contribute only to square parts.
They do not create parity rows.

## 4. Complete decoding

The parity matrix has at most `R_h` columns and at most `R_h+S_h` rows. A
retained `A=1` record is one zero parity column. It fits this bound. Gaussian
elimination, a complete kernel basis, and deterministic first-occurrence
column selection use polynomial time and space in `S_h`.

There are at most `R_h` kernel-basis dependencies. A binary dependency uses
each retained record at most once. The bit length of its exact product is at
most the sum of the input record lengths, which is at most `S_h`. Its exact
square root exists because every parity-row multiplicity is even. Exact square
root, modular supplied-root multiplication, normalization, and both signed gcd
tests have polynomial bit complexity.

All square parts, decorated lifts, selected columns, dependency supports, and
kernel data occupy polynomial space in `S_h`. This accounts for the complete
decoder, not only matrix rank.

For one feedback attempt, an implementation can scan all parity rows, count
the selected-row multiplicities, apply the required modular block corrections,
and reduce after every multiplication. This uses polynomial time in the
current transcript. Multiplication by the quasipolynomial attempt count
preserves the quasipolynomial bound.

## 5. Fixed-depth induction

The hypotheses give

\[
R_0,S_0\le 2^{L^{O(1)}}.
\]

Sections 1-4 show that one layer preserves this form for record count,
transcript length, time, and space. The exponent can increase with the layer.
Induction over the fixed finite set `0,1,...,H` gives

\[
T_H,\operatorname{Space}_H\le2^{L^{O_H(1)}}.
\]

A polynomial of a quantity of this form has the same form. A sum over fixed
`H` also has the same form. This is a bit-complexity bound. It includes
integer arithmetic, exact roots, gcds, modular inverses, subset enumeration,
retention, and all decoder data.

## Hostile checks that did not break the proof

- **Zero parity columns:** R05 exposed R04's finite omission of `A=1`. Adding
  all such columns can increase `R_h`, nullity, and kernel work only within the
  already counted `R_h` bound.
- **Duplicate attempts:** The recurrence counts every attempt. It does not
  assume a favorable duplicate rate.
- **Component explosion:** The potential bounds the number of refinement
  transformations and live components by a polynomial in `S_h`.
- **Perfect-power oracle:** Exact root testing is deterministic polynomial-time
  integer arithmetic. It is not factoring or order finding.
- **Large dependency products:** Their total bit length is bounded by the
  explicit transcript length, not by their numeric magnitude as a unary
  integer.
- **Dense matrices:** A dense polynomial in `R_h+S_h` remains within the stated
  quasipolynomial bound.
- **All-attempt storage:** Even storing every attempt uses
  `M_(h+1) poly(S_h)` space, which remains quasipolynomial at fixed depth.
- **Small inputs:** The finitely many cases with `L<2` are absorbed by a fixed
  constant.
- **Growing depth:** The proof does not hide this case. Repeated exponent
  growth is why its conclusion is restricted to fixed `H`.

## Precision notes

One sentence says that canonicalization can use a dictionary keyed by the
exact integer and decorated root. The exact-value ledger should instead use
the exact integer `A` as its lookup key and store the first decorated root for
the required ratio comparison. This wording does not affect the cost proof:
either representation retains at most one record per attempt, and an
`A`-keyed balanced tree has the stated polynomial overhead.

The proof also uses compact subset references. This is a valid implementation
choice. An implementation that gratuitously copies an expanded recursive
provenance tree into every record is outside the proved recurrence, but no such
copy is required for generation, verification, or decoding.

## Status boundary

This audit advances no durable status by itself. Under the repository's strict
verification cadence, promotion remains the root agent's decision and must
respect the required ordering and independence rules.

The proved result remains only a fixed-depth cost theorem. It supplies no
uniform growing-depth bound and no success theorem. It does not resolve the
integer factoring task.
