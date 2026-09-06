# F144 V3 candidate statement — positive cross-star cycles require square-root-scale anchor mass

## Status and scope

This is the second corrected proof-only boundary for the P128 lifted source.
The frozen V1 and V2 files and their reviews are preserved unchanged.  V1's
hostile audit found that its proposed short-cycle surplus regime was
vacuous.  V2 removed that regime and passed hostile audit, but its blind
reconstruction found one strictness error.  V3 replaces that one false
strict inequality by the exact non-strict bound and states the fixed-
residual and projected anchor intervals separately.

The surviving result has one positive and one negative part.

1. A directed cross-star cycle, or a collection of such cycles, has an exact
   public residual relation.  When the combined residual product is a
   square, the actual P128 columns give an exact dependency with a known
   normalized root.
2. Every positive-direction cycle containing a canonical wrap already needs
   anchor product greater than \(\sqrt N\), even before its residual is a
   square.  Thus bounded wrapped positive cycles with total raw anchor
   product
   \(2^{\operatorname{polylog} n}=2^{o(n)}\) are asymptotically impossible.

This does not close the feedback route.  A selected path of polynomial
length can accumulate anchor product above \(\sqrt N\) while using only
polynomially many source records.  The general F130 word cap also permits
raw anchors whose compact presentations have quasipolynomial bit length.
Neither case is ruled out.

The closest promoted results are P128 and P129.  P128 supplies the
canonical/lifted relation pair.  P129 gives the bridge class and the root of
an exact endpoint cycle.  F143 shows that signed commutation cycles have
root \(+1\) and that useful formal cycles are hidden half-relations.  F144
V3 concerns stored positive-direction containment cycles.  It permits a
non-square residual on each edge and closes those residuals across cycles.

## 1. Legal directed containment edges

Let \(N\ge3\) be odd.  Work in one frozen P118 named basis.  Its blocks are
pairwise coprime positive units modulo \(N\).

For one legal P128 squared-anchor position, write

\[
U=qa^2,
\qquad
c=[U]_N,
\qquad
w=\iota_N(c),
\qquad
U=c+tN,
\qquad t\ge0.
\tag{1}
\]

The actual canonical and lifted relation values are

\[
C=cw,
\qquad
L=Uw.
\tag{2}
\]

Both are positive integers congruent to one modulo \(N\).  Their conceptual
bridge is

\[
D=Uc=qa^2c,
\qquad
D\equiv c^2\pmod N.
\tag{3}
\]

Let \(r\ne q\) be another current named block.  If exact division gives

\[
c=rT,
\qquad T\in\mathbb Z_{>0},
\tag{4}
\]

call this occurrence a directed containment edge

\[
e:q\longrightarrow r
\tag{5}
\]

with anchor \(a_e=a\) and residual \(T_e=T\).  The edge is wrapped when
\(t>0\), equivalently \(U>c\).  All data in (1)--(5) are public.

## 2. Exact size law for one positive directed cycle

Let \(\mathcal C\) be one directed containment cycle.  Define

\[
A_{\mathcal C}=\prod_{e\in\mathcal C}a_e,
\qquad
T_{\mathcal C}=\prod_{e\in\mathcal C}T_e.
\tag{6}
\]

Then

\[
\boxed{
N\mid A_{\mathcal C}^{\,2}-T_{\mathcal C}.
}
\tag{7}
\]

Every edge satisfies \(U_e\ge c_e\).  Therefore

\[
A_{\mathcal C}^{\,2}\ge T_{\mathcal C},
\tag{8}
\]

with equality exactly when every edge in the cycle is unwrapped.

If at least one edge wraps, then

\[
\boxed{
A_{\mathcal C}^{\,2}-T_{\mathcal C}\ge N,
\qquad
A_{\mathcal C}^{\,2}\ge N+T_{\mathcal C},
\qquad
A_{\mathcal C}>\sqrt N.
}
\tag{9}
\]

This theorem does not assume that \(T_{\mathcal C}\) is a square.  It is a
necessary size law for every stored positive-direction wrapped cycle.

## 3. Residual-square dependency and exact root

Take any nonempty indexed collection of directed containment cycles.
Logical edge occurrences are kept with multiplicity at first.  Put

\[
\mathcal A=\prod_ea_e,
\qquad
\mathcal T=\prod_eT_e.
\tag{10}
\]

Suppose

\[
\boxed{\mathcal T=S^2}
\tag{11}
\]

for a positive integer \(S\).  Select both actual P128 values \(C_e,L_e\)
for every logical edge occurrence.  Their product is an exact square.  Its
normalized root is

\[
\boxed{
\rho\equiv\mathcal A S^{-1}\pmod N,
}
\tag{12}
\]

and

\[
\boxed{
\mathcal A^2\equiv S^2\pmod N.
}
\tag{13}
\]

If at least one selected cycle contains a wrapped edge, then

\[
\boxed{
\mathcal A^2-S^2=mN
\quad\text{for some integer }m\ge1.
}
\tag{14}
\]

In particular,

\[
\boxed{\mathcal A\ge\sqrt{N+S^2}>\sqrt N.}
\tag{15}
\]

There is a sharper collection boundary.  For each unwrapped directed cycle
\(\mathcal C\), equation (8) is an equality:

\[
T_{\mathcal C}=A_{\mathcal C}^{\,2}.
\tag{15a}
\]

It is already a residual square and contributes normalized root \(+1\).
If an indexed collection contains two cycles that each have a wrapped edge,
then (9) applies to each of them separately, so

\[
\boxed{
\mathcal A
\ge A_{\mathcal C_1}A_{\mathcal C_2}
>N.
}
\tag{15b}
\]

Such a collection cannot satisfy \(2\mathcal A<N\).  If a collection
contains exactly one wrapped cycle, adjoining any number of unwrapped cycles
does not help residual closure: the total residual is a square exactly when
the wrapped cycle's residual is a square, and the unwrapped cycles cancel
from the normalized root.

Thus the metric argument can certify at most one wrapped cycle at a time.
Combinations of two or more wrapped cycles can still have useful P66 roots,
but V3 gives no automatic root-asymmetry theorem for them.

If the additional public metric condition

\[
\boxed{2\mathcal A<N}
\tag{16}
\]

holds, then the root is automatically non-global.  Both

\[
\boxed{
1<\gcd(\mathcal A-S,N)<N,
\qquad
1<\gcd(\mathcal A+S,N)<N
}
\tag{17}
\]

are proper divisors.

For fixed residual root \(S\), the exact metric interval from (15)--(16)
is

\[
\sqrt{N+S^2}\le\mathcal A<N/2.
\tag{18}
\]

If \(S\) is projected away, its coarser anchor-only projection is
\(\sqrt N<\mathcal A<N/2\).  The exact \(N=35\) certificate in Section 6
attains the lower endpoint of the fixed-\(S\) interval.

If no selected edge wraps, then \(\mathcal A=S\) and the normalized root is
\(+1\).  Thus canonical wrapping is necessary for metric asymmetry in this
positive-direction lemma.

## 4. Exact-value deletion

The formulas above use logical bridge occurrences.  Restore their actual
canonical and lifted values before global exact-value deletion.  If an exact
integer value \(P\) occurs twice, remove that pair.  This removes the square
\(P^2\) and divides the positive exact root by
\(P\equiv1\pmod N\).  The normalized root is unchanged.

Repeat until every exact value has multiplicity zero or one, then use the
globally retained representative of each odd class.  The deduplicated P128
ledger contains a dependency with the same root (12).  A dependency that
satisfies (15)--(17) cannot collapse to zero.

## 5. Consequence for the quasipolynomial source

Let a positive directed cycle have length \(k\) and anchors \(a_e\le H\).
If it contains a wrapped edge, (9) gives

\[
\boxed{
H^k\ge A_{\mathcal C}>\sqrt N,
\qquad
k>\frac{\log N}{2\log H}.
}
\tag{19}
\]

Therefore any proposed family with total raw anchor product

\[
\prod_ea_e
\le 2^{(\log n)^{O(1)}}
=2^{o(n)}
\tag{20}
\]

contains no wrapped positive directed cycle for all sufficiently large
\(n=\lceil\log_2(N+1)\rceil\).

Important special cases are:

- anchors bounded by \(n^{O(1)}\) and cycle length
  \((\log n)^{O(1)}\);
- any fixed number of F141 small-prime-anchor positions; and
- the failed V1 near-\(N\) short-cycle surplus regime.

This is an arithmetic impossibility for wrapped positive-direction cycles,
not a runtime lower bound.
The V1 combination also fails after residual closure: combining two wrapped
cycles makes the total anchor product exceed \(N\), while combining only one
wrapped cycle gains no residual-square help from unwrapped cycles.

The obstruction does not exclude a polynomial-length selected trajectory.
For the P128 anchor bank \(a\le n^3\), a length on the order of

\[
\frac{n}{6\log_2 n}
\tag{21}
\]

can already accumulate anchor product at the \(\sqrt N\) scale.  Generating
and checking one specified path of that length costs only polynomially many
records and remains inside quasipolynomial work.  Exhaustively enumerating
all such paths is not asserted to be quasipolynomial.

The obstruction also does not bound every F130 anchor by
\(2^{\operatorname{polylog} n}\) as an integer.  F130 permits compact
monomial words with quasipolynomial bit length.  A raw square anchor in such
a word can exceed \(\sqrt N\) while its description and arithmetic remain
quasipolynomial.  V3 therefore rules out the bounded-magnitude wrapped
positive-cycle idea, not the full P128 lifted source.

## 6. Exact conditional certificate

Take

\[
N=35,
\qquad
q=13,
\qquad
r=17,
\qquad
a=2,
\qquad
b=3.
\tag{22}
\]

Then

\[
[13\cdot2^2]_{35}=17,
\qquad
[17\cdot3^2]_{35}=13.
\tag{23}
\]

This is a two-edge directed cycle with residuals \(1,1\).  Both edges wrap.
The anchor and residual-root products are

\[
\mathcal A=6,
\qquad
S=1.
\tag{24}
\]

They satisfy

\[
\sqrt{35}<6=\sqrt{35+1}<35/2,
\qquad
\gcd(6-1,35)=5,
\qquad
\gcd(6+1,35)=7.
\tag{25}
\]

At the actual relation level,

\[
(561)(1716)(351)(4131)=1181466^2,
\qquad
1181466\equiv6\pmod{35}.
\tag{26}
\]

The centers are pairwise-coprime units and the anchors are eligible primes.
The two words have support two and exponents \(1,2\), so they are legal P128
positions conditional on \(13,17\) occurring together in one frozen named
basis.  This does not claim that the actual P118 transcript for \(N=35\)
reaches that basis.  Standard preprocessing can already factor this small
input.

## 7. Cross-star determinant traps

For two arbitrary cross-star endpoints, write

\[
c=qa^2-tN,
\qquad
d=rb^2-sN,
\tag{27}
\]

and define

\[
\Delta=sc-td=qa^2s-rb^2t.
\tag{28}
\]

If \(h=\gcd(c,d)\), then

\[
h\mid\Delta,
\qquad
|\Delta|<\frac{qr a^2b^2}{N}.
\tag{29}
\]

If \(\Delta=0\), the two conceptual bridges form an exact square, but their
normalized root is exactly \(+1\).  In particular,

\[
\boxed{
hN\ge qr a^2b^2
\Longrightarrow
\Delta=0
\Longrightarrow
\text{normalized root }+1.
}
\tag{30}
\]

A large cross-endpoint gcd that forces proportional carries is therefore a
global decoy.

The four endpoints

\[
[qa^2]_N,\ [ra^2]_N,\ [qb^2]_N,\ [rb^2]_N
\tag{31}
\]

form exactly one P114 multiplicative rectangle.  With

\[
u=[qa^2]_N,
\qquad
\alpha=[rq^{-1}]_N,
\qquad
\beta=[b^2a^{-2}]_N,
\tag{32}
\]

they are \(u,u\alpha,u\beta,u\alpha\beta\).  The P114 inverse-carry
determinant and P115--P116 boundaries apply without change.  V3 makes no
density claim for that scalar.

## 8. Exact remaining gate

The wrapped positive-direction target is no longer a bounded short cycle.  Any
wrapped cycle must first cross the characteristic scale
\(\prod a_e>\sqrt N\).

A useful continuation must do at least one of the following:

1. give a public quasipolynomial selector for a polynomial-length or
   large-raw-anchor cycle whose combined residual product is a square and
   whose normalized root is non-global;
2. exploit an arithmetic hypercycle that is not a union of stored
   positive-direction containment cycles; or
3. find a non-formal signed cycle whose root is not one of F143's
   commutation decoys.

V3 proves no all-input existence theorem and no factoring algorithm.
