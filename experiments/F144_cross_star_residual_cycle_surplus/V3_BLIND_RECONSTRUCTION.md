# F144 V3 blind reconstruction

## Source boundary and verdict

This reconstruction used only `V3_STATEMENT.md` from the F144 directory.
Its SHA-256 is

```text
87dacd7af5121f66561cea4136d1445f10cfe0185bd9229277fd48b358bf5f6f
```

This equals the expected hash.

**Verdict: PASS.** The cycle identities, equality cases, residual-square
root, metric gcd certificate, exact-value deletion, (N=35) example,
determinant trap, rectangle identification, and asymptotic scope all follow
from the stated data. No counterexample was found.

There are two interpretation notes, neither of which changes the verdict.

1. The four rectangle identities are identities in
   ((\mathbb Z/N\mathbb Z)^\times), or identities after reduction by
   ([\cdot]_N). They need not be literal equalities of unreduced positive
   integers.
2. Claims about the contents of named external results such as P114--P116,
   or about transcript provenance, cannot be re-audited from this statement
   alone. The algebraic hypotheses that V3 says it supplies to those results
   are verified below.

## 1. One-cycle law and its exact equality case

Index a directed cycle by (i\in\mathbb Z/k\mathbb Z). Write its vertices as
(q_i), so the edge (q_i\to q_{i+1}) gives

\[
q_i a_i^2=U_i=c_i+t_iN,
\qquad
c_i=q_{i+1}T_i,
\qquad t_i\ge 0.
\]

Reduction modulo (N) gives

\[
q_i a_i^2\equiv q_{i+1}T_i\pmod N.
\]

Multiplication over the cycle cancels the same product of vertex blocks on
the two sides. Those blocks are units modulo (N). Hence

\[
A_{\mathcal C}^2
=\prod_i a_i^2
\equiv \prod_iT_i
=T_{\mathcal C}\pmod N,
\]

which proves

\[
N\mid A_{\mathcal C}^2-T_{\mathcal C}.
\]

The exact size comparison is just as direct. For each edge,

\[
\frac{U_i}{c_i}
=\frac{q_i a_i^2}{q_{i+1}T_i}\ge 1.
\]

Multiplication again cancels the vertex blocks and yields

\[
\prod_i\frac{U_i}{c_i}
=\frac{A_{\mathcal C}^2}{T_{\mathcal C}}\ge1.
\]

All factors are positive and at least one. Their product equals one exactly
when every factor equals one. This is equivalent to (U_i=c_i), hence to
(t_i=0), on every edge. Therefore

\[
A_{\mathcal C}^2\ge T_{\mathcal C},
\]

with equality exactly for a fully unwrapped cycle.

If one edge wraps, the inequality is strict. The positive integer
(A_{\mathcal C}^2-T_{\mathcal C}) is divisible by (N), so

\[
A_{\mathcal C}^2-T_{\mathcal C}\ge N,
\qquad
A_{\mathcal C}^2\ge N+T_{\mathcal C}.
\]

Since (T_{\mathcal C}\ge1), this also gives

\[
A_{\mathcal C}>\sqrt N.
\]

No square condition on (T_{\mathcal C}) was used.

## 2. Exact dependency and normalized root

Now take an indexed union of directed cycles. Edge occurrences retain their
multiplicity. Set

\[
Q=\prod_e q_{\mathrm{source}(e)},
\qquad
W=\prod_e w_e,
\qquad
\mathcal A=\prod_ea_e,
\qquad
\mathcal T=\prod_eT_e.
\]

The multiset of source vertices equals the multiset of target vertices in a
union of cycles. Thus the product of all source blocks and the product of
all target blocks are both (Q). For every edge,

\[
C_eL_e=(c_ew_e)(U_ew_e)=U_ec_ew_e^2.
\]

Using (U_e=q_{\mathrm{source}(e)}a_e^2) and
(c_e=q_{\mathrm{target}(e)}T_e), multiplication gives the exact integer
identity

\[
\prod_e C_eL_e
=Q^2\mathcal A^2\mathcal T W^2.
\]

If (\mathcal T=S^2) for (S>0), this becomes

\[
\prod_e C_eL_e=(Q\mathcal A S W)^2.
\]

So the selected actual relation values form an exact-square dependency. Its
positive exact root is

\[
R=Q\mathcal A S W.
\]

The inverse (S^{-1}\pmod N) exists. Indeed, (c_e) and its target block
are units, while (c_e=q_{\mathrm{target}(e)}T_e). Hence every (T_e),
their product (S^2), and (S) are units modulo (N).

Also (c_ew_e\equiv1\pmod N). Since

\[
\prod_ec_e=Q\mathcal T=QS^2,
\]

we have

\[
QS^2W\equiv1\pmod N.
\]

It follows that

\[
R=Q\mathcal A S W
\equiv \mathcal A S^{-1}\pmod N.
\]

This proves the normalized-root formula

\[
\rho\equiv\mathcal A S^{-1}\pmod N.
\]

Multiplying the one-cycle congruences over the selected cycles also gives

\[
\mathcal A^2\equiv\mathcal T=S^2\pmod N.
\]

For each cycle, its squared anchor product is at least its residual product.
If one selected cycle wraps, one factor inequality is strict. Therefore

\[
\mathcal A^2>S^2.
\]

The difference is divisible by (N), so

\[
\mathcal A^2-S^2=mN
\quad(m\ge1),
\qquad
\mathcal A\ge\sqrt{N+S^2}>\sqrt N.
\]

The lower bound is non-strict. Equality occurs when (m=1), as the
(N=35) example shows.

## 3. Wrapped-cycle count and residual closure

For an unwrapped cycle (\mathcal C), the equality case above gives

\[
T_{\mathcal C}=A_{\mathcal C}^2.
\]

Its residual is already a square. Taking its positive residual root to be
(A_{\mathcal C}), its normalized contribution is
(A_{\mathcal C}A_{\mathcal C}^{-1}=1).

If two selected cycles each wrap, each separately satisfies

\[
A_{\mathcal C_j}>\sqrt N.
\]

All other anchor factors are positive integers, so the collection satisfies

\[
\mathcal A\ge
A_{\mathcal C_1}A_{\mathcal C_2}>N.
\]

It cannot also satisfy (2\mathcal A<N).

If exactly one cycle wraps, write its residual as (T_w). The product of
all unwrapped residuals is a square, say (B^2), and their anchor product is
the same (B). Thus the total residual (T_wB^2) is a square exactly when
(T_w) is a square. If (T_w=S_w^2), then

\[
\frac{\mathcal A}{S}
=\frac{A_wB}{S_wB}
=\frac{A_w}{S_w}.
\]

Unwrapped cycles neither enable residual closure nor alter the normalized
root. Hence the metric argument can apply to at most one wrapped cycle.

## 4. The metric gcd certificate and exact intervals

Assume at least one selected cycle wraps, (\mathcal T=S^2), and

\[
2\mathcal A<N.
\]

The strict surplus gives (\mathcal A>S>0). Therefore

\[
0<\mathcal A-S<\mathcal A+S<2\mathcal A<N.
\]

On the other hand,

\[
N\mid(\mathcal A^2-S^2)
=(\mathcal A-S)(\mathcal A+S).
\]

If (\gcd(\mathcal A-S,N)=1), cancellation modulo (N) would imply
(N\mid\mathcal A+S), which is impossible because
(0<\mathcal A+S<N). Hence that gcd is greater than one. The same argument
with the two factors exchanged proves that
(\gcd(\mathcal A+S,N)>1). Each gcd is smaller than (N), since its
positive argument is smaller than (N). Thus

\[
1<\gcd(\mathcal A-S,N)<N,
\qquad
1<\gcd(\mathcal A+S,N)<N.
\]

For a fixed positive integer (S), the exact two metric inequalities are

\[
\sqrt{N+S^2}\le\mathcal A<N/2.
\]

After existentially projecting away the positive integer (S), the lower
bound becomes strict:

\[
\sqrt N<\mathcal A<N/2.
\]

Indeed, (S\ge1) makes the fixed-(S) lower bound strictly larger than
(\sqrt N). Conversely, for integral (\mathcal A>\sqrt N), the integer
(\mathcal A^2-N) is at least one, so (S=1) satisfies the projected lower
inequality. This verifies the stated projection as an inequality projection;
it does not assert that every point in it comes from a legal cycle.

If no edge wraps, every cycle is unwrapped. Then
(\mathcal T=\mathcal A^2), the positive residual root is
(S=\mathcal A), and (\rho=1). Thus wrapping is necessary for this
metric mechanism to produce a non-global root.

## 5. Exact-value deletion

Every selected actual value is congruent to one modulo (N):

\[
C_e=c_ew_e\equiv1,
\qquad
L_e=U_ew_e\equiv c_ew_e\equiv1\pmod N.
\]

Suppose an exact positive integer value (P) occurs at least twice in the
logical multiset. If the full product is (R^2), removing two occurrences
changes it to

\[
\frac{R^2}{P^2}=\left(\frac RP\right)^2.
\]

The quotient (R/P) is an integer. Also (P\equiv1\pmod N), so the new
root has the same residue modulo (N). Repeating this operation reduces
every exact-value multiplicity modulo two. Selecting the ledger's one
retained representative for each odd multiplicity therefore preserves both
the square dependency and its normalized root.

Under the metric hypotheses, the remainder cannot be empty. An empty
dependency has exact root (1) and hence normalized root (+1), while the
gcd argument above forces the retained root to be neither (+1) nor
(-1) modulo (N).

## 6. The (N=35) certificate

Take (N=35), (q=13), (r=17), (a=2), and (b=3). The first edge is

\[
13\cdot2^2=52=17+35,
\]

so it is (13\to17), with (t=1) and residual (T=1). The second is

\[
17\cdot3^2=153=13+4\cdot35,
\]

so it is (17\to13), with (t=4) and residual (T=1). Both edges wrap.
Thus

\[
\mathcal A=2\cdot3=6,
\qquad
S=1,
\qquad
\mathcal A^2-S^2=36-1=35.
\]

Consequently

\[
6=\sqrt{35+1},
\qquad
\sqrt{35}<6<35/2,
\]

and

\[
\gcd(6-1,35)=5,
\qquad
\gcd(6+1,35)=7.
\]

The needed inverse representatives are

\[
17^{-1}\equiv33\pmod{35},
\qquad
13^{-1}\equiv27\pmod{35}.
\]

They give the four actual values

\[
17\cdot33=561,
\quad
52\cdot33=1716,
\quad
13\cdot27=351,
\quad
153\cdot27=4131.
\]

Their product is

\[
561\cdot1716\cdot351\cdot4131
=1{,}395{,}861{,}909{,}156
=1{,}181{,}466^2,
\]

and

\[
1{,}181{,}466\equiv6\pmod{35}.
\]

Also (gcd(13,17)=1), both centers are units modulo (35), and (2,3)
are prime anchors. Each raw word has the displayed center to exponent one
and anchor to exponent two, hence support two. Its status as an actual P128
position remains conditional on the stated frozen-basis hypothesis. No
claim about the actual (N=35) transcript is needed for the arithmetic
certificate.

## 7. Cross-star determinant trap

For two endpoints, set

\[
U=qa^2=c+tN,
\qquad
V=rb^2=d+sN.
\]

Then

\[
\Delta=sc-td
=s(qa^2-tN)-t(rb^2-sN)
=qa^2s-rb^2t.
\]

If (h=\gcd(c,d)), both (sc) and (td) are divisible by (h), so

\[
h\mid\Delta.
\]

Because (c,d) are positive reduced residues,

\[
0\le t<\frac{qa^2}{N},
\qquad
0\le s<\frac{rb^2}{N}.
\]

Both (qa^2s) and (rb^2t) therefore lie in the half-open interval

\[
\left[0,\frac{qr a^2b^2}{N}\right).
\]

The absolute difference of two numbers in that interval is strictly less
than its length. Hence

\[
|\Delta|<\frac{qr a^2b^2}{N}.
\]

If (hN\ge qr a^2b^2), the right side is at most (h). Since (\Delta)
is an integer multiple of (h) with ( |\Delta|<h), it follows that

\[
\Delta=0.
\]

This zero determinant is a decoy, not an asymmetric dependency. Directly,

\[
Ud-Vc
=(c+tN)d-(d+sN)c
=N(td-sc)
=-N\Delta.
\]

Thus (\Delta=0) gives (Ud=Vc). For the two conceptual bridges
(D_1=Uc) and (D_2=Vd),

\[
D_1D_2=(Uc)(Vd)=(Ud)(Vc)=(Ud)^2.
\]

The exact root is (Ud), while the canonical modular root is (cd).
Since (U\equiv c\pmod N),

\[
Ud\equiv cd\pmod N.
\]

The normalized root is therefore exactly (+1). This proof also covers
the unwrapped case (t=s=0).

## 8. The multiplicative rectangle

All quantities in this subsection are residue classes modulo (N). The
inverses exist because the endpoints and named blocks are units. Define

\[
u=[qa^2]_N,
\qquad
\alpha=[rq^{-1}]_N,
\qquad
\beta=[b^2a^{-2}]_N.
\]

Then

\[
u\alpha\equiv ra^2,
\qquad
u\beta\equiv qb^2,
\qquad
u\alpha\beta\equiv rb^2\pmod N.
\]

Hence, with the displayed row-column ordering, the four endpoints are

\[
u,quad u\alpha,quad u\beta,quad u\alpha\beta
\]

after reduction modulo (N). This is precisely the multiplicative
rectangle relation. It supplies the algebraic input needed by any earlier
inverse-carry determinant theorem stated for such rectangles. The rectangle
identity alone supplies no density or existence statement for that
determinant scalar.

## 9. Quasipolynomial scope

Let a wrapped cycle have (k) edges and (a_e\le H). Its existence already
implies (H>1), because its anchor product exceeds (\sqrt N>1). Therefore
logs are valid, and

\[
H^k\ge A_{\mathcal C}>\sqrt N
\]

gives

\[
k>\frac{\log N}{2\log H}.
\]

Now put (n=\lceil\log_2(N+1)\rceil). Then

\[
2^{n-1}<N+1\le2^n,
\]

so (\sqrt N=2^{\Theta(n)}). In contrast,

\[
2^{(\log n)^{O(1)}}=2^{o(n)}.
\]

Thus a total raw anchor product bounded by the latter expression is smaller
than (\sqrt N) for all sufficiently large (n). It cannot contain the
anchor product of a wrapped positive directed cycle. In particular, if
(a_e\le n^d) and (k\le(\log n)^c) for fixed (c,d), then

\[
\log_2 A_{\mathcal C}
\le dk\log_2 n
=O((\log n)^{c+1})
=o(n),
\]

so such a wrapped cycle is impossible asymptotically. The same reasoning
covers any fixed number of bounded small-prime anchors.

Residual closure does not evade this size obstruction. Two wrapped cycles
force total anchor product greater than (N). One wrapped cycle plus any
number of unwrapped cycles gets no help with squareness and no change to its
normalized root.

The result does not imply a runtime lower bound. If anchors can be as large
as (n^3), then a path whose anchors are near that upper scale reaches
(\sqrt N) after approximately

\[
k\sim\frac{(1/2)n}{3\log_2n}
=\frac{n}{6\log_2n}
\]

steps. A specified path of that polynomial length uses only polynomially
many records and has polynomial-bit accumulated products. This observation
does not make exhaustive enumeration of all such paths cheap.

Nor does a quasipolynomial description-size or bit-length cap imply that the
represented integer anchor is at most (2^{\operatorname{polylog} n}) in
magnitude under every compact word representation. Large-exponent monomial
words can represent anchors above (\sqrt N) while still having the stated
compact or quasipolynomial arithmetic cost. Therefore the proof excludes
bounded-magnitude wrapped positive cycles. It does not exclude
polynomial-length selected trajectories, large represented anchors,
non-containment hypercycles, or non-formal signed cycles.

## Final scope

The proved result is a necessary size and residual-closure law. It gives a
conditional factor certificate when a suitable wrapped cycle and the metric
bound both occur. It proves neither the existence of such a cycle for every
input nor a factoring algorithm.
