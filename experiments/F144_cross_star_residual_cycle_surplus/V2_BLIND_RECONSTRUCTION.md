# F144 V2 statement-only blind reconstruction

## Isolation and provenance

- File examined: `V2_STATEMENT.md` only.
- Expected SHA-256: `a07a992ac3d43dac6f25c2cc337e470f81c9a8265eb54e091922ecd63cef138b`.
- Observed SHA-256: `a07a992ac3d43dac6f25c2cc337e470f81c9a8265eb54e091922ecd63cef138b`.
- I did not inspect the V2 proof, either V1 file, an audit, a manifest, a
  ledger, or any other F144 file.

## Verdict

**Refuted as written.**  The central square-root obstruction is correct, as
are the residual-square dependency, its normalized root, the two proper-gcd
conclusions, exact-value deletion, the bounded-magnitude asymptotic
consequence, the arithmetic part of the `N=35` certificate, and the
cross-star determinant trap.

However, boxed equation (15) has a false strict inequality.  Equation (14)
only gives

\[
\mathcal A^2\ge N+S^2,
\qquad
\boxed{\mathcal A\ge\sqrt{N+S^2}>\sqrt N}.
\]

Equality can occur when the integer `m` in (14) is one.  The statement's own
certificate is such a case:

\[
N=35,\quad \mathcal A=6,\quad S=1,\quad
\mathcal A^2-S^2=35,
\quad 6=\sqrt{35+1}.
\]

Thus the certificate directly contradicts the first `>` sign in (15).  No
central later conclusion needs that false strict sign.  They need only
`\mathcal A>\sqrt N`, which remains strict because `S>0`.

There is also a precision issue in (18).  After correcting (15), the literal
joint bounds for fixed `S` are

\[
\sqrt{N+S^2}\le \mathcal A<N/2.
\]

The displayed range `\sqrt N<\mathcal A<N/2` is the coarser projection that
forgets `S`; it is not an exact restatement of (15)--(16).

## Conventions needed by the statement

The reconstruction uses the conventions implicit in the text:

1. `[x]_N` is the positive canonical residue of a unit.
2. `\iota_N(c)` is a positive integer congruent to `c^{-1}` modulo `N`.
3. A directed cycle has the same multiset of source blocks and target
   blocks.

The claims that a position is legal P128 data, that all of its data are
public, and that cited P114--P116, P118, F130, F141, or F143 rules apply are
imports from outside this statement.  I do not use those imports to prove
the arithmetic claims below.

## 1. One-cycle size law

For an edge `e:q_e\to r_e`, the definitions give

\[
q_ea_e^2=r_eT_e+t_eN,
\qquad t_e\ge0.
\]

Let

\[
Q=\prod_{e\in\mathcal C}q_e
  =\prod_{e\in\mathcal C}r_e.
\]

The equality is exact because the edges form a directed cycle.  Multiplying
the edge congruences gives

\[
Q A_{\mathcal C}^2\equiv Q T_{\mathcal C}\pmod N.
\]

Every block is a unit, so `Q` is a unit modulo `N`.  Cancelling it proves

\[
N\mid A_{\mathcal C}^2-T_{\mathcal C}.
\]

This reconstructs (7).

There is also an exact comparison:

\[
\prod_e U_e=Q A_{\mathcal C}^2,
\qquad
\prod_e c_e=Q T_{\mathcal C}.
\]

Each `U_e\ge c_e>0`.  Hence (8) holds.  Equality of the products holds if
and only if every individual inequality is an equality.  This is equivalent
to `t_e=0` for every edge.

If one edge wraps, the product inequality is strict.  Therefore
`A_{\mathcal C}^2-T_{\mathcal C}` is a positive multiple of `N`.  This proves

\[
A_{\mathcal C}^2-T_{\mathcal C}\ge N,
\qquad
A_{\mathcal C}^2\ge N+T_{\mathcal C},
\qquad
A_{\mathcal C}>\sqrt N.
\]

Thus (9), including all of its quantifiers, is correct.  It does not require
`T_{\mathcal C}` to be a square.

## 2. Collection dependency and normalized root

Keep all edge occurrences with multiplicity.  Let

\[
Q=\prod_e q_e=\prod_e r_e,
\qquad
W=\prod_e w_e.
\]

If `\mathcal T=S^2`, the product of all selected actual values is

\[
\begin{aligned}
\prod_e C_eL_e
  &=\prod_e U_ec_ew_e^2\\
  &=(Q\mathcal A^2)(Q\mathcal T)W^2\\
  &=(Q\mathcal A S W)^2.
\end{aligned}
\]

This is an exact integer square, not only a modular square.

All inverses in (12) exist.  Indeed, `c_e=r_eT_e` is a unit and `r_e` is a
unit, so every `T_e` is a unit.  Hence `S^2=\mathcal T` and `S` are units.
Likewise, `q_ea_e^2\equiv c_e` shows that every anchor is a unit.

The positive exact root is

\[
R=Q\mathcal A S W.
\]

Moreover,

\[
W\equiv\left(\prod_e c_e\right)^{-1}
 \equiv(QS^2)^{-1}\pmod N.
\]

It follows that

\[
R\equiv \mathcal A S^{-1}\pmod N.
\]

This proves the exact dependency and (12).  Squaring the result, or
multiplying the cycle congruences, proves (13).

For each selected cycle, `A_{\mathcal C}^2\ge T_{\mathcal C}`.  If at least
one cycle wraps, at least one of these inequalities is strict.  Multiplying
them gives

\[
\mathcal A^2>S^2.
\]

Together with (13), this proves (14):

\[
\mathcal A^2-S^2=mN
\quad\text{for an integer }m\ge1.
\]

It proves only a non-strict first inequality in the corrected form of (15).

## 3. Number and type of wrapped cycles

For an unwrapped cycle, equality in (8) gives

\[
T_{\mathcal C}=A_{\mathcal C}^2.
\]

Its positive residual root is `A_{\mathcal C}`, so (12) gives normalized
root `+1`.  This proves (15a) and the no-wrap root claim.

If two indexed cycles wrap, then each has anchor product greater than
`\sqrt N`.  All anchors are positive integers, so the whole collection has

\[
\mathcal A\ge A_{\mathcal C_1}A_{\mathcal C_2}>N.
\]

This proves (15b), including the case in which the indexed cycles repeat
logical data.  Such a collection cannot satisfy `2\mathcal A<N`.

If exactly one cycle wraps, every other cycle contributes a square
`A_{\mathcal C}^2` to the residual product.  Multiplication by these squares
cannot change whether the wrapped cycle's residual is a square.  If it is a
square, the extra factor `A_{\mathcal C}` occurs in both `\mathcal A` and
`S`, so it cancels from `\mathcal A S^{-1}`.  The residual-closure and
root-cancellation claims are correct.

Consequently, the metric test `2\mathcal A<N` can apply to at most one
wrapped cycle.  This fact does not prove that collections with more wrapped
cycles have global roots.  The statement correctly declines to make that
claim.

## 4. Proper-gcd conclusion

Assume at least one selected cycle wraps and `2\mathcal A<N`.  From (14),
set

\[
x=\mathcal A-S,
\qquad y=\mathcal A+S.
\]

Then

\[
0<x<y<2\mathcal A<N,
\qquad N\mid xy.
\]

If `\gcd(x,N)=1`, then `N\mid y`, which is impossible because `0<y<N`.
The same argument with `x` and `y` exchanged proves `\gcd(y,N)>1`.
Because both `x` and `y` are less than `N`, neither gcd can equal `N`.
Therefore both inequalities in (17) are correct.

Since `S` is a unit,

\[
\gcd(\mathcal A\mathbin{\pm}S,N)
=\gcd(\rho\mathbin{\pm}1,N)
\]

up to multiplication by a unit.  Thus the normalized root is neither
globally `+1` nor globally `-1`.  The term "non-global" is justified by the
two proper gcds.

## 5. Exact-value deletion

Every actual relation value `P` used here is congruent to `1` modulo `N`.
Suppose the selected exact product is `R^2` and the same exact integer `P`
occurs twice.  Removing those occurrences leaves

\[
R^2/P^2=(R/P)^2.
\]

The quotient `R/P` is an integer by prime valuations.  Its residue is the
old normalized root multiplied by `P^{-1}\equiv1`.  Pair deletion therefore
preserves both exact squareness and the normalized root.  Iteration leaves
one occurrence precisely for each value class with odd selected
multiplicity.

The transfer to a globally retained representative is valid provided the
deduplicated ledger retains one representative of every exact value class,
as the statement says.  The representative has the same integer value, so
the exact product does not change.

If all selected values disappeared, the remaining positive exact root would
be `1`, with normalized root `+1`.  This contradicts (17), because root
`+1` would imply `N\mid\mathcal A-S`.  Thus the non-collapse claim is
correct.  It relies on (17), not on the false strict part of (15).

## 6. Quasipolynomial scope

For a wrapped cycle with `a_e\le H`, (9) gives

\[
H^k\ge A_{\mathcal C}>\sqrt N.
\]

The antecedent itself forces `H>1`.  Taking logarithms proves (19), with a
strict `>`:

\[
k>\frac{\log N}{2\log H}.
\]

Let `n=\lceil\log_2(N+1)\rceil`.  Then `N\ge2^{n-1}`.  For every fixed
constant `C`,

\[
(\log n)^C=o(n).
\]

Hence a uniform family with

\[
\log_2\prod_ea_e=O((\log n)^C)
\]

has total anchor product below `\sqrt N` for all sufficiently large `n`.
It cannot contain a wrapped positive directed cycle.  This proves the
substance of (20).  The equality notation
`2^{(\log n)^{O(1)}}=2^{o(n)}` must mean that every fixed-polylog exponent
is `o(n)`; the two growth classes are not equal in the reverse direction.

If `H\le n^c` and `k\le(\log n)^d` for fixed constants `c,d`, then

\[
\log_2 A_{\mathcal C}
\le ck\log_2 n
=O((\log n)^{d+1})
=o(n).
\]

Thus the first listed special case is valid.  A fixed number of
"small-prime-anchor" positions is also covered if that external term means
each anchor has `2^{o(n)}` magnitude, as the list suggests.  The assertion
about the V1 regime cannot be checked from the V2 statement alone because
that regime is not defined here.

For `a\le n^3`, a path of length

\[
k\asymp\frac{n}{6\log_2n}
\]

can have upper-envelope anchor product

\[
(n^3)^k=2^{3k\log_2n}\asymp2^{n/2},
\]

which is the `\sqrt N` scale.  This is a capacity calculation.  It is not
an existence or selection theorem.  The path contains only
`O(n/\log n)` specified records, so its record count is polynomial.  This
does not imply that exhaustive path enumeration is quasipolynomial.

The theorem restricts raw anchor magnitude, not description length.  Thus
an external source format that permits quasipolynomial-bit monomial words
can encode integers above `\sqrt N`.  The logical caveat about F130 is
sound, but the claim that F130 in fact permits those words is external and
was not independently verified here.

The obstruction is therefore arithmetic and restricted to wrapped cycles
whose total raw anchor product is `2^{o(n)}`.  It is not a runtime lower
bound and does not exclude unwrapped cycles, specified polynomial-length
paths, or large raw anchors with compact allowed descriptions.

## 7. The `N=35` certificate

The two edges reconstruct as follows.

| edge | `U` | `c` | `t` | `T` | `w=c^{-1} mod 35` | `C=cw` | `L=Uw` |
|---|---:|---:|---:|---:|---:|---:|---:|
| `13\to17`, `a=2` | 52 | 17 | 1 | 1 | 33 | 561 | 1716 |
| `17\to13`, `b=3` | 153 | 13 | 4 | 1 | 27 | 351 | 4131 |

Both carries are positive.  Hence both edges wrap.  The anchor and residual
root products are `\mathcal A=6` and `S=1`.  Direct calculation gives

\[
\gcd(5,35)=5,
\qquad
\gcd(7,35)=7,
\]

and

\[
561\cdot1716\cdot351\cdot4131
=1{,}395{,}861{,}909{,}156
=1{,}181{,}466^2.
\]

Also `1{,}181{,}466\equiv6\pmod{35}`.  The four selected exact values are
pairwise distinct, so no internal exact-value pair disappears.

The centers satisfy

\[
\gcd(13,35)=\gcd(17,35)=\gcd(13,17)=1,
\]

and the anchors 2 and 3 are primes.  The monomials `13\cdot2^2` and
`17\cdot3^2` each have support two and exponents 1 and 2.  These facts
verify the stated elementary eligibility conditions.  Actual inclusion in
a P118 frozen basis remains explicitly conditional and cannot be inferred
from this arithmetic certificate.

The certificate validates (7)--(14), the corrected (15), (16), (17), and
(18).  It refutes original (15), because

\[
6=\sqrt{35+1},
\quad\text{not}\quad
6>\sqrt{35+1}.
\]

## 8. Cross-star determinant trap

Write

\[
U=qa^2=c+tN,
\qquad
V=rb^2=d+sN.
\]

Then

\[
\Delta=sc-td=sU-tV,
\]

which proves (28).  If `h=\gcd(c,d)`, both terms in `sc-td` are divisible by
`h`, so `h\mid\Delta`.

Because `c,d>0`,

\[
0\le t<U/N,
\qquad
0\le s<V/N.
\]

Both `sU` and `tV` are strictly less than `UV/N`.  They are nonnegative, so

\[
|\Delta|=|sU-tV|<UV/N=qr a^2b^2/N.
\]

This proves (29).  If `hN\ge UV`, then `|\Delta|<h`.  Since `h` divides
`\Delta`, this forces `\Delta=0`.

There is an exact identity

\[
Ud-Vc=N(td-sc)=-N\Delta.
\]

When `\Delta=0`, let `X=Ud=Vc`.  The product of the two conceptual bridges
is

\[
(Uc)(Vd)=(Ud)(Vc)=X^2.
\]

After restoring the two inverse factors, its positive exact root is
`Xw_cw_d`.  Since `X=Ud\equiv cd\pmod N`,

\[
Xw_cw_d\equiv cd\,c^{-1}d^{-1}\equiv1\pmod N.
\]

This proves every arithmetic implication in (30), including the exact
square and normalized-root claim.

## 9. Multiplicative rectangle and remaining gate

In the multiplicative group modulo `N`, the four endpoint identities are

\[
\begin{aligned}
[u\alpha]_N&=[ra^2]_N,\\
[u\beta]_N&=[qb^2]_N,\\
[u\alpha\beta]_N&=[rb^2]_N.
\end{aligned}
\]

Thus (31)--(32) do form a multiplicative rectangle.  The products
`u\alpha`, `u\beta`, and `u\alpha\beta` need reduction modulo `N`; they are
not, in general, equal as ordinary canonical integers.  The phrase "they
are `u,u\alpha,u\beta,u\alpha\beta`" is correct only as group notation.
The P114 classification, its uniqueness wording, and the cited
P115--P116 boundaries are external to this statement and cannot be
reconstructed statement-only.

The final scope claim is accurate.  The proved gate is necessary, not
sufficient:

\[
\text{wrapped positive cycle}\Longrightarrow\prod_ea_e>\sqrt N.
\]

Nothing in the statement proves that a qualifying cycle exists, selects
one, makes its residual product a square, or makes its root non-global.
Therefore V2 proves neither an all-input existence theorem nor a factoring
algorithm.

## Claim accounting

| Claim | Blind result |
|---|---|
| Definitions and congruences (1)--(5) | Correct under the stated inverse convention; P128 legality/publicity is external. |
| Cycle laws (7)--(9) | Proved. |
| Exact dependency and root (11)--(14) | Proved, including invertibility of `S`. |
| First inequality in (15) | **False.** Replace `>` by `\ge`. |
| Unwrapped and multi-wrapped claims (15a)--(15b) | Proved. |
| Metric gcd result (16)--(17) | Proved; both gcds are nontrivial and proper. |
| Range (18) | Correct as a coarser anchor-only range, not as the literal fixed-`S` interval from corrected (15)--(16). |
| Exact-value deletion | Proved under the stated representative-retention policy. |
| Bounds (19)--(21) | Correct with fixed uniform asymptotic constants; (21) is capacity, not existence. |
| `N=35` arithmetic | Verified exactly; it is also a counterexample to original (15). |
| Determinant laws (27)--(30) | Proved. |
| Rectangle (31)--(32) | Proved modulo `N`; external P114--P116 classifications were not checked. |
| All-input or algorithmic conclusion | None is proved, as the statement correctly says. |

