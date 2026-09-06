# F147 proof — bounded-anchor wrapped-core reduction

## 1. The carry bound

For one legal position, write

\[
qa^2=c+tN,
\qquad
1\le c<N.
\]

Because `q<N`,

\[
0\le t=\left\lfloor\frac{qa^2}{N}\right\rfloor<a^2\le H^2.
\tag{1}
\]

Thus a wrapped position has `1 <= t < H^2`.

## 2. A wrapped cycle cannot contain an unwrapped edge

Assume a directed cycle has at least one wrapped edge and at least one
unwrapped edge.  Follow the cycle from an unwrapped edge until the first
wrapped edge.  Let the last unwrapped edge in this segment be

\[
q\longrightarrow r
\]

with anchor `a`, and let the next wrapped edge have source `r` and anchor
`b`.

The unwrapped equality is

\[
qa^2=rT.
\tag{2}
\]

The frozen named blocks `q` and `r` are distinct and pairwise coprime.
Therefore (2) implies

\[
r\mid a^2,
\qquad
r\le a^2.
\tag{3}
\]

The next edge wraps, so

\[
rb^2>N.
\tag{4}
\]

Equations (3)--(4) give

\[
a^2b^2\ge rb^2>N.
\tag{5}
\]

But `a,b <= H` and `H^4 <= N`, so

\[
a^2b^2\le H^4\le N,
\]

contradicting (5).  Hence every edge of a cycle that contains one wrapped
edge is wrapped.

## 3. Large centers and small residuals

For a wrapped edge `e:q -> r`,

\[
qa^2>N.
\]

Since `a <= H`,

\[
q>\frac{N}{a^2}\ge\frac{N}{H^2}.
\tag{6}
\]

Every target `r` in a directed cycle is the source of the next edge.  The
previous section makes that next edge wrapped, so the same argument gives

\[
r>\frac{N}{H^2}.
\tag{7}
\]

The residue satisfies `c=rT<N`.  Equation (7) gives

\[
1\le T<\frac{N}{r}<H^2.
\tag{8}
\]

Together, (1), (6), (7), and (8) prove the four bounds in the statement.

## 4. Uniqueness of the large target

Suppose two distinct named blocks `r,s>N/H^2` both divide the same residue
`c<N`.  They are pairwise coprime, so `rs|c`.  But

\[
rs>\frac{N^2}{H^4}\ge N>c,
\]

which is impossible.  Thus every position has at most one large named
target.

Sections 2--4 also prove completeness of the graph extraction: every
wrapped cycle uses only wrapped edges between large vertices, and the scan
keeps the unique large target of each of its word positions.

## 5. Exact residual factorization

Let `1 <= T < H^2`.  Trial-divide `T` by every integer, or only every
prime, through `H`.  After removing all such prime powers, the remaining
cofactor is either one or prime.  If it had two prime factors, both would be
greater than `H`, and their product would exceed `H^2>T`.

This gives the exact rational-prime factorization of every residual in time
polynomial in `H` and `log T`.  The standard complete gcd-free refinement
can instead refine these residuals jointly with the named centers without
rationally factoring a large center.  Maximal perfect-power extraction then
gives the exact square-class coordinates used by P66.

## 6. Bridge kernel and normalized root

For one edge,

\[
D=Uc=(qa^2)(rT)=qra^2T.
\tag{9}
\]

Also `U=c mod N`, so

\[
D\equiv c^2\pmod N.
\tag{10}
\]

Let `x` be in the binary kernel of the exact square-class columns of the
`D_e`.  By definition,

\[
Z_x=\prod_{e:x_e=1}D_e=Y_x^2
\tag{11}
\]

for a positive integer `Y_x`.  Multiplying (10) over the selected edges
gives

\[
Y_x^2\equiv
\left(\prod_{e:x_e=1}c_e\right)^2
\pmod N.
\tag{12}
\]

Every factor is a unit unless an earlier declared gcd already succeeded.
Thus (7) of the statement is a square root of one modulo `N`.

For the actual P128 values,

\[
C_eL_e=(c_ew_e)(U_ew_e)=D_ew_e^2.
\tag{13}
\]

The selected actual product has positive root

\[
Y_x\prod_{e:x_e=1}w_e.
\]

Since `w_e=c_e^{-1} mod N`, this root modulo `N` is exactly (7) of the
statement.  This proves bridge-to-ledger correctness.

If an actual integer relation value occurs twice, deleting the pair removes
its square and divides the positive root by that value.  Every relation
value is one modulo `N`, so the normalized root is unchanged.  Iterating
proves the exact-value deletion claim.  If every selected actual value
cancels, the remaining positive root is a product of deleted relation
values and is therefore `+1 mod N`.  Hence a non-global root cannot collapse
to the zero ledger vector.

The dependency map and the normalized-root map are homomorphisms over
binary addition.  Gaussian elimination can therefore compute a basis after
the exact-value map.  If all basis roots are global, every combination is
global.  If one is non-global, the standard gcd extracts a proper divisor.

## 7. Edge-surplus bound

Before the residuals are inserted, the `m` frozen named blocks are
pairwise coprime and power-free.  Let `R_H` be the set of rational primes
that divide at least one residual.  Joint refinement can split a named block
only at primes in `R_H`.  Splitting all such primes increases the number of
power-free decoder blocks by at most `|R_H|`.  The residuals add no other
prime rows.  Therefore the bridge matrix has at most

\[
m+|R_H|
\]

rows.  Rank-nullity gives

\[
\dim\ker(M_H)\ge E_H-m-|R_H|.
\tag{14}
\]

Every residual is below `H^2`, so every prime in `R_H` is below `H^2`.
Consequently `|R_H|<=pi(H^2)`, which proves the second bound in the
statement.  This only forces a conceptual bridge kernel.  Exact-value
survival and root asymmetry are later maps and do not follow from
rank-nullity.

## 8. Cost

There are at most `Q` positions and `Q` named blocks.  Constructing every
residue and carry uses arithmetic on `O(n+log H)`-bit integers.  Testing all
possible targets uses at most `Q^2` exact remainders.  Direct screens use a
constant number of gcds per position.

The residual trial division uses `O(QH)` divisions.  All actual values have
`O(n+log H)` bits.  Exact-value sorting, complete refinement, perfect-power
extraction, binary elimination, modular roots, and final gcds are polynomial
in the explicit transcript size.  This proves the cost bound in the
statement.

If both `Q` and `H` are `2^{(log n)^{O(1)}}`, every displayed cost is
quasipolynomial in `n`.  Also `log(H^4)=polylog(n)=o(n)`, while
`log N=Theta(n)`, so `H^4<=N` for all sufficiently large inputs.

## 9. What the proof does not give

The proof does not force a large-to-large containment edge.  It does not
force a directed cycle, a bridge-kernel vector after all fresh rows are
included, survival under global exact-value deletion, or a non-global root.
It also does not cover adaptive promotion of arbitrary residues or gcd
aggregates to new generator states.

Reaching `prod(a_e)>sqrt(N)` along one specified path satisfies only P131's
necessary magnitude condition.  It supplies none of the missing arithmetic
conditions above.
