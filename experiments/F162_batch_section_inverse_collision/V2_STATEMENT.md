# F162 candidate V2 — batch signed-inverse detection for section products

## Status and scope

V2 repairs only the explicit-list normalization cost omitted by V1. It does
not change the detector, source interface, finite evidence, or claim scope.

This is a proof-only batch-decoder candidate. It gives a factor-free
subquadratic selector for one pair-product channel inside P143/F156. It also
compresses the fixed P147/F157 witness from 65 pair occurrences to eight
public scalar values.

The closest evaluator result is P34: monic product and remainder trees permit
exact multipoint evaluation over `Z/NZ` without hidden division by a
data-dependent residue. The closest source results are P143 and P147.

The material difference is that one product polynomial detects all signed
inverse collisions among an explicit quasipolynomial list of section values.
It does not enumerate all pairs. This improves the locator for this channel.
It does not force a collision, cover every intersection-corrected F156 pair,
or prove an all-input factoring algorithm.

## 1. General batch theorem

Let `N>=2`. Let

\[
a_1,\ldots,a_r\in(\mathbf Z/N\mathbf Z)^\times
\tag{1}
\]

be an explicit public list. There is a deterministic factor-free algorithm
that returns a proper factor of `N` whenever

\[
1<\gcd(a_i a_j-\epsilon,N)<N
\tag{2}
\]

for some distinct positions `i<j` and some sign
`epsilon in {+1,-1}`.

Let `A` be the set of distinct canonical residues in the list and let
`m=|A|`. Form the monic polynomial

\[
P(X)=\prod_{b\in A}(X-b)\pmod N.
\tag{3}
\]

For every `a in A` and `epsilon in {+1,-1}`, put

\[
x_{a,\epsilon}=\epsilon a^{-1}\pmod N.
\tag{4}
\]

Use

\[
H_{a,\epsilon}=
\begin{cases}
P(x_{a,\epsilon}),&x_{a,\epsilon}\notin A,\\
P'(x_{a,\epsilon}),&x_{a,\epsilon}\in A.
\end{cases}
\tag{5}
\]

The derivative case removes the one exact global partner that would make
the ordinary evaluation zero modulo all of `N`. Test

\[
\gcd(H_{a,\epsilon},N)
\tag{6}
\]

for all `(a,epsilon)`. Also test `gcd(a^2-epsilon,N)` for every distinct
`a`. This handles equal-value source positions and is a valid extra public
factor test even when a value occurs once.

If (6) equals `N`, localize one contributing value with a scalar subproduct
tree. A leaf is `x_{a,epsilon}-b` with
`b != x_{a,epsilon}` as canonical residues. Such a nonzero difference has
absolute value less than `N`, so its gcd with `N` cannot equal `N`. The
descent therefore returns a proper factor.

With fast polynomial arithmetic, the complete detector has bit cost

\[
\widetilde O\!\left(rn+(m(n+\log m))^{1+o(1)}
+m\,\mathsf M(n)\log n\right),
\qquad n=\lceil\log_2(N+1)\rceil,
\tag{7}
\]

The term `rn` pays for reading, canonicalizing, and deterministically
deduplicating the explicit position list. The post-normalization polynomial
working storage is soft-linear in `mn`. Exact multiplicity counters use
`O(m log(r+1))` further bits; one duplicate flag per value is sufficient for
this detector because every self screen is tested unconditionally. Counting
the resident input itself adds `O(rn)` bits. In particular, the detector is
subquadratic in the list length and remains quasipolynomial when the explicit
list has quasipolynomial size.

## 2. Shared-block normalization

At one frozen P143/F156 stage, let the public parity-basis lift `i` be

\[
e_i=(v_i,z_i),
\qquad
q_i=Q(v_i)=z_i^2\pmod N.
\tag{8}
\]

For a public block subset `T subseteq v_i`, put

\[
C_T=\prod_{b\in T}b,
\qquad
a_{i,T}=q_i C_T^{-1}\pmod N.
\tag{9}
\]

Run the general batch theorem separately on the owner list

\[
I_T=\{i:T\subseteq v_i\}
\tag{10}
\]

using the values `a_{i,T}`.

If two basis vectors have exact intersection

\[
v_i\cap v_j=T,
\tag{11}
\]

then their F156 star value is

\[
Q(v_i\mathbin\triangle v_j)
=\frac{q_iq_j}{C_T^2}
=a_{i,T}a_{j,T}\pmod N.
\tag{12}
\]

Therefore the `T`-batch finds a factor whenever this F156 pair has a proper
direct sign screen. Pairs whose intersection strictly contains `T` can only
cause additional valid factor outputs; they cannot cause an incorrect
output.

For a public intersection cap `t`, enumerate every `T subseteq v_i` with
`|T|<=t`. Define the total owner incidence

\[
S_t=\sum_i\sum_{k=0}^{\min(t,|v_i|)}\binom{|v_i|}{k}.
\tag{13}
\]

The combined batch cost is soft-linear in `S_t` up to coefficient and gcd
costs. Here `S_t` counts owner positions before per-list deduplication, so it
also pays for the sum of all explicit-list read and normalization terms. It
detects every support-two F156 hit whose exact block-intersection
support is at most `t`. If `t=polylog(n)` and the frozen transcript has
quasipolynomial explicit size, then `S_t` and the detector remain
quasipolynomial.

The case `T=emptyset` is especially small. It processes one list of at most
`r` values and detects every F156 hit with disjoint parity supports. It can
also return a valid factor from an uncorrected product of two intersecting
supports.

## 3. Exact F157 structural compression

The frozen F157 output contains 65 successful support-two occurrences for

\[
N=3{,}241{,}632{,}473.
\tag{14}
\]

Grouping the serialized certificates by the public triple
`(q_mod_N,z,w)` gives only eight distinct scalar tests, with occurrence
counts

\[
25,27,4,2,2,2,2,1.
\tag{15}
\]

Every occurrence is a minus-sign hit. Sixty-three expose `41011`; two
expose `79043`. Thus the 65 occurrences are not 65 independent decoder
directions. Equal `z` fixes the same canonical inverse `w` and the same exact
feedback value `zw`. Global exact-value deletion collapses each such group
to one retained relation value.

Exactly 28 of the 65 occurrences have empty public block intersection. One
is the public basis pair

```text
basis indices = (656, 10097)
C             = 1
q_i*q_j mod N = 2922074762
gcd(q_i*q_j - 1, N) = 41011
```

Therefore the single `T=emptyset` batch is already a public factor-free
subquadratic locator for this fixed witness. It does not need the disclosed
factors used by the registered F157 discovery index.

## 4. Relation to earlier results

- P108 and P117 concern parity-kernel dependencies and normalized-root
  images across retained relation layers. The F157 direct hits occur before
  that decoder. Their repeated public triples do not create cross-layer
  rank after exact-value deduplication.
- P110 is a many-relation kernel success. F157 is different: a two-basis
  product gives a local signed-inverse collision and one terminal gcd.
- P111 constrains prime-row reuse among exact carry values. It does not
  create or exclude the modular collisions detected here.
- P118 and P143 supply the explicit quasipolynomial source. This theorem
  changes only how one pair channel is evaluated.
- P147 gives the fixed-input existence certificate. This theorem removes
  its quadratic public pair scan for the disjoint-support subchannel.

## 5. Exact remaining gap

The theorem accelerates a collision that already exists. It gives no lower
bound on the number of useful signed-inverse collisions. The four F157
58-bit controls have no support-at-most-two F156 star hit, but that fact does
not determine whether the larger uncorrected batch channel has an extra hit.

The full F156 pair value uses the complete intersection product. Enumerating
all possible dense intersections can lose the subquadratic advantage, even
though it stays quasipolynomial under the declared transcript bounds.

The all-input problem is unchanged: one must force a direct batch collision,
a useful named refinement, or a non-global normalized-root direction on
every surviving composite input.
