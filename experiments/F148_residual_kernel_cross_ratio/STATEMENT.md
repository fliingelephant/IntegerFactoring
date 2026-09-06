# F148 candidate statement — residual-kernel cross-ratio closure

## Status and scope

This is a proof-only conditional decoder and source target for the P128
lifted relation family. It does not prove that the required cycles exist on
every input. It is not an integer factoring algorithm.

The closest results are P66, P108, P111, P112, P127, and P128--P131. P66
decodes a supplied square relation. P108 shows that two relation layers can
be useful only together on one fixed input. P111, P112, and P127 show that
fresh private rows can prevent closure. P128 and P129 turn squared-anchor
feedback into bridge columns and give their exact cycle root. P130 removes
formal cycles. P131 proves that one wrapped positive cycle needs anchor mass
above `sqrt(N)` and gives a metric factor window when its residual product is
already a square. P131 also notes that the product of the anchors of two
wrapped cycles exceeds `N`, so its combined-product metric window cannot
certify such a pair.

F148 uses a different metric comparison. It pairs two cycles by the square
class of their residual products and compares two cross-products. This can
certify a factor even when each residual product is nonsquare and the product
of the two anchor products exceeds `N`.

## 1. Directed containment cycles

For a legal P128 squared-anchor position, write

\[
U_e=q_ea_e^2,
\qquad
c_e=[U_e]_N=r_eT_e,
\]

where all displayed factors are positive units modulo the odd composite
input `N`. A directed containment cycle has `r_e=q_{e+1}` cyclically. Put

\[
\alpha_i=\prod_{e\in\mathcal C_i}a_e,
\qquad
T_i=\prod_{e\in\mathcal C_i}T_e.
\]

P131 gives the exact public congruence

\[
\boxed{\alpha_i^2\equiv T_i\pmod N.}
\tag{1}
\]

The bridge boundary of this cycle is exactly the rational square class of
`T_i`. The cycle need not be a square relation by itself.

## 2. Residual-kernel pairing theorem

Take two cycle vectors whose actual retained-column supports are disjoint
after global exact-value deduplication. Suppose their residual products have
the same rational square class. Equivalently, the factor-free decoder can
write

\[
T_i=d s_i^2,
\qquad
T_j=d s_j^2
\tag{2}
\]

with positive integers `d,s_i,s_j`. No rational-prime factorization is
needed to obtain such a common factor-free core `d`.

The union of the two cycle vectors is an exact P128 square relation. Its
normalized root is

\[
\boxed{
\rho_{ij}
\equiv
{\alpha_i\alpha_j\over d s_i s_j}
\equiv
{\alpha_i s_j\over\alpha_j s_i}
\pmod N.
}
\tag{3}
\]

Therefore its two terminal gcds can be evaluated with the smaller
cross-products:

\[
\boxed{
\gcd(\rho_{ij}-1,N)
=
\gcd(\alpha_i s_j-\alpha_j s_i,N),
}
\tag{4}
\]

\[
\boxed{
\gcd(\rho_{ij}+1,N)
=
\gcd(\alpha_i s_j+\alpha_j s_i,N).
}
\tag{5}
\]

These formulas use only public exact integers and gcd. They are not a new
source of modular information; they are a smaller integer representation of
the normalized root already present in the combined relation.

## 3. Cross-ratio metric theorem

If

\[
\alpha_i s_j\ne\alpha_j s_i
\tag{6}
\]

and

\[
\boxed{
\alpha_i s_j+\alpha_j s_i<N,
}
\tag{7}
\]

then both gcds in (4)--(5) are proper divisors of `N`.

This is the material difference from P131's combined-product window. For
two wrapped cycles, `alpha_i*alpha_j>N` is automatic. Condition (7) can
still hold. For example, it is compatible with both anchor products being
just above `sqrt(N)` and both `s` values being small.

The failure mode is exact. Define

\[
z_i=\alpha_i s_i^{-1}\pmod N.
\]

Every member of one residual-core bucket satisfies `z_i^2=d mod N`. Pair
`i,j` is useful exactly when `z_i` and `z_j` are in different classes modulo
the global sign `+/-`. Thus all pairs in a bucket are global-root decoys if
and only if all `z_i` occupy one global-sign class. Under the pairwise metric
bound (7), no factor is possible only when all exact rational slopes
`alpha_i/s_i` in that bucket are equal.

## 4. Quasipolynomial amortization corollary

Let `R,H` be positive integers. Suppose an explicit retained source supplies
more than `R` column-disjoint directed containment cycles such that:

1. `T_i<=R` for every cycle;
2. `alpha_i<=H` for every cycle;
3. after writing `T_i=d_i*s_i^2`, no two cycles with the same `d_i` have
   the same exact rational slope `alpha_i/s_i`;
4. `2*H*sqrt(R)<N`.

There are at most `R` possible positive squarefree residual cores `d_i`.
Two cycles therefore have the same core. Their `s` values are at most
`sqrt(R)`, so (7) holds. Their slopes differ, so (6) holds. Equations
(4)--(5) factor `N`.

If the number of cycles and `R` are bounded by `2^polylog(n)`, and the total
compact presentation length is quasipolynomial, joint gcd-free refinement,
parity bucketing, slope deduplication, and all gcd tests take
quasipolynomial time. The numerical bound `H` in item 4 can be much larger
than quasipolynomial. Its ordinary binary representation has only `O(n)`
bits when `H<N`.

This corollary is conditional. No current theorem supplies more than `R`
such long cycles, bounds all residual products by `R`, or forces distinct
slopes. It changes the exact missing target:

> It is enough to amortize many small-residual cycles across residual square
> classes. One does not need one cycle whose residual product is already a
> square.

## 5. Nondegenerate finite certificate

Let

\[
N=745=5\cdot149,
\qquad d=6.
\]

Use two one-edge containment cycles:

\[
(q_1,\alpha_1,T_1)=(57,119,6),
\qquad
(q_2,\alpha_2,T_2)=(92,179,6).
\]

They satisfy

\[
119^2=19N+6,
\qquad
179^2=43N+6.
\]

Hence

\[
[57\cdot119^2]_N=57\cdot6=342,
\qquad
[92\cdot179^2]_N=92\cdot6=552.
\]

The canonical inverses are `403` and `193`. The four actual P128 values are

\[
137826,
\quad
325292331,
\quad
106536,
\quad
568919996.
\]

They are distinct and individually nonsquare. Neither two-column cycle
product is a square. Their four-value product is

\[
2717393685268861431892777536
=
52128626351256^2.
\]

The normalized root is

\[
52128626351256\equiv446\pmod{745}.
\]

It gives

\[
\gcd(446-1,745)=5,
\qquad
\gcd(446+1,745)=149.
\]

The smaller cross-ratio witnesses are

\[
\gcd(179-119,745)=5,
\qquad
\gcd(179+119,745)=149.
\]

All four endpoint sign screens are null: their gcds are `1` or `745`.
This certificate shows the mechanism. It gives no frequency or all-input
claim.

## 6. Exact unresolved theorem

A positive F26-Q continuation can now target either of these statements:

1. produce one wrapped cycle whose residual product is a square and lies in
   P131's metric window; or
2. produce enough wrapped cycles in the F148 bounds to force a repeated
   residual square class with a new exact slope.

The second target is strictly more permissive on each individual cycle. Its
hard source-side requirements remain cycle construction, small residual
products, and slope diversity. This candidate proves none of them.
