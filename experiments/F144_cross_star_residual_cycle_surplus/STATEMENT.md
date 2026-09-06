# F144 candidate statement — short cross-star residual cycles have automatic useful roots

## Status and scope

This is a proof-only positive boundary for the P128 lifted source.  It does
not change that source and it does not prove that the required cycles exist
on every input.  It proves two new facts.

1. A directed cycle of cross-star endpoint containments reduces the full
   rank-and-root problem to one exact square test on small residuals.  If at
   least one edge wraps and the anchor product is below \(N/2\), the resulting
   root is automatically non-global.
2. In the near-\(N\) block range, more than a polylogarithmic number of short
   directed cycles forces such a residual-square combination by binary
   linear algebra.  The complete test remains quasipolynomial.

Thus this result removes the separate normalized-root gate on one explicit
cross-star regime.  The remaining source-side gate is to force enough short
endpoint-containment cycles.

The closest results are P128 and P129.  P128 supplies the canonical and
lifted relation pair.  P129 identifies its bridge square class and gives the
root of a formal endpoint cycle.  F143 shows that arbitrary formal Cayley
cycles can restate hidden half-relations and that commutation diamonds have
root \(+1\).  F144 does not use a commutation diamond.  It uses only edges in
their stored positive direction, permits a non-square residual on each edge,
and closes those residuals across several cycles.

P119 classifies a dependency made from two canonical exact values.  F144
instead selects two actual P128 values for every bridge occurrence.  P114--
P116 use a four-point inverse-carry determinant.  F144 uses an exact P66
square dependency.  Section 6 records the precise separation.

## 1. One legal cross-star edge

Let \(N\ge3\) be odd.  Work in one frozen P118 named basis, whose blocks are
pairwise coprime positive units modulo \(N\).  Let \(q\) be one current named
block and let \(a\) be a positive unit such that the frozen word

\[
U=qa^2
\tag{1}
\]

is a legal P128 position.  Put

\[
c=[U]_N,
\qquad
w=\iota_N(c),
\qquad
U=c+tN,
\qquad t\ge0.
\tag{2}
\]

The actual canonical and lifted relation values are

\[
C=cw,
\qquad
L=Uw.
\tag{3}
\]

Both are positive integers congruent to one modulo \(N\).  Their conceptual
bridge is

\[
D=Uc=qa^2c,
\qquad D\equiv c^2\pmod N.
\tag{4}
\]

Let \(r\ne q\) be another current named block.  If exact division gives

\[
c=rT,
\qquad T\in\mathbb Z_{>0},
\tag{5}
\]

call this occurrence a **directed containment edge**

\[
e:q\longrightarrow r
\tag{6}
\]

with anchor \(a_e=a\) and residual \(T_e=T\).  This is a public condition.
It uses integer divisibility, not a hidden factor of \(N\).  Since \(c\) is
a unit modulo \(N\), both \(r\) and \(T\) are units modulo \(N\).

An edge is **wrapped** when \(t>0\), equivalently \(U>c\).

## 2. Directed residual-cycle theorem

Take any nonempty indexed collection of directed cycles made from legal
containment edges.  Logical edge occurrences are retained with
multiplicity at this stage; the same source edge can occur in two different
cycles.

Let

\[
\mathcal A=\prod_e a_e,
\qquad
\mathcal T=\prod_e T_e,
\tag{7}
\]

where the products run over all selected logical edge occurrences.  Suppose

\[
\boxed{\mathcal T=S^2}
\tag{8}
\]

for a positive integer \(S\).

Select both actual P128 values \(C_e,L_e\) for every logical edge occurrence.
Their product is an exact integer square.  Its positive root modulo \(N\) is

\[
\boxed{
\rho\equiv \mathcal A S^{-1}\pmod N.
}
\tag{9}
\]

Equivalently,

\[
\boxed{\mathcal A^2\equiv S^2\pmod N.}
\tag{10}
\]

If at least one selected edge is wrapped, then

\[
\boxed{\mathcal A>S.}
\tag{11}
\]

Consequently, if

\[
\boxed{2\mathcal A<N,}
\tag{12}
\]

then \(\rho\not\equiv\pm1\pmod N\).  In fact both public integers

\[
\gcd(\mathcal A-S,N),
\qquad
\gcd(\mathcal A+S,N)
\tag{13}
\]

are proper divisors on the preprocessed non-prime-power branch.

This theorem also covers one directed cycle.  For an exact endpoint cycle
\(T_e=1\) on every edge, it gives \(S=1\) and recovers the P129 root
\(\prod_ea_e\).  It adds the metric conclusion: a wrapped cycle with
\(2\prod_ea_e<N\) is automatically useful.  No second root-asymmetry theorem
is required.

## 3. Global exact-value deletion is harmless

The theorem is stated with logical occurrences because two cycles can share
an edge and different source positions can have equal exact relation values.
Restore all selected actual values \(C_e,L_e\), group equal integers, and
delete equal occurrences in pairs.  Deleting a pair of one exact value \(P\)
removes the square \(P^2\).  Its positive root is \(P\equiv1\pmod N\), so
the normalized root changes by \(+1\).

After all pair deletions, select the globally retained representative of
each value with odd multiplicity.  The remaining P128 ledger therefore has
an exact square dependency with the same root (9).  If (11)--(12) hold, it
cannot collapse to the zero dependency.

## 4. A forced quasipolynomial cycle-surplus regime

Let \(R,H,K\ge2\).  In one frozen named basis, define the near-\(N\) vertex
set

\[
V_R=\{q:q>N/R\}.
\tag{14}
\]

Use only eligible prime anchors \(a\le H\).  For every legal P128 position
\(U=qa^2\) with \(q\in V_R\), compute \(c=[U]_N\).  For every distinct
\(r\in V_R\) with \(r\mid c\), insert the directed edge

\[
q\longrightarrow r,
\qquad
T=c/r.
\tag{15}
\]

Assume the two explicit size conditions

\[
\boxed{N/R>H^2,}
\qquad
\boxed{2H^{K(R+1)}<N.}
\tag{16}
\]

Then every edge in (15) is wrapped and every residual satisfies

\[
1\le T<R.
\tag{17}
\]

Suppose this directed multigraph contains at least \(R+1\) distinct simple
directed cycles, each of length at most \(K\).  Factor the residuals, which
are all below \(R\), and form one binary residual-parity column for each
cycle.  There are fewer than \(R\) possible rational-prime rows.  Therefore
the \(R+1\) cycle columns have a nonzero binary dependency.

For the selected cycles in that dependency, the combined residual product
is an exact square.  Their anchor product is at most

\[
H^{K(R+1)}<N/2.
\tag{18}
\]

The directed residual-cycle theorem now gives a proper factor of \(N\).
Cycle overlaps do not invalidate the result because Section 3 removes even
logical occurrences without changing the root.

Thus:

\[
\boxed{
R+1\text{ short cross-star cycles among blocks }>N/R
\Longrightarrow
\text{a proper factor},
}
\tag{19}
\]

subject only to the public size conditions (16).

## 5. Quasipolynomial search cost

Take

\[
R=(\log n)^{O(1)},
\qquad
H=(\log n)^{O(1)},
\qquad
K=(\log n)^{O(1)},
\tag{20}
\]

with fixed exponents, where \(n=\lceil\log_2(N+1)\rceil\).  The inequalities
in (16) hold for all sufficiently large \(n\); they can also be checked
directly.

The P118 transcript has quasipolynomially many frozen blocks and stages.
For each stage, all edges (15) can be found by exact division.  Enumerating
all simple directed cycles through length \(K\) takes

\[
2^{(\log n)^{O(1)}}
\tag{21}
\]

work because the graph itself has quasipolynomial size and \(K\) is
polylogarithmic.  Trial division of numbers below \(R\), binary linear
algebra on the first \(R+1\) cycles, exact products, an integer square root,
and the final gcds have no larger cost.

This scan adds no source position.  It is a deterministic quasipolynomial
decoder for a public condition already present in P128.

## 6. Cross-star determinant traps

Two tempting determinant arguments do not prove (19).

First, for arbitrary cross-star endpoints write

\[
c=qa^2-tN,
\qquad
d=rb^2-sN,
\tag{22}
\]

and define the public two-endpoint carry determinant

\[
\Delta=sc-td=qa^2s-rb^2t.
\tag{23}
\]

If \(h=\gcd(c,d)\), then

\[
h\mid\Delta,
\qquad
|\Delta|<\frac{qr a^2b^2}{N}.
\tag{24}
\]

If \(\Delta=0\), the two bridges do form an exact square, but their
normalized root is exactly \(+1\).  Therefore forcing a very large shared
endpoint block until (24) makes \(\Delta=0\) produces a global decoy, not a
factor.

In particular,

\[
\boxed{
hN\ge qr a^2b^2
\Longrightarrow
\Delta=0
\Longrightarrow
\text{normalized root }+1.
}
\tag{25}
\]

Second, the four endpoints

\[
[qa^2]_N,\ [ra^2]_N,\ [qb^2]_N,\ [rb^2]_N
\tag{26}
\]

are exactly a P114 multiplicative rectangle.  Taking

\[
u=[qa^2]_N,
\quad
\alpha=[rq^{-1}]_N,
\quad
\beta=[b^2a^{-2}]_N
\tag{27}
\]

gives its four corners.  The four-by-four inverse-carry determinant of P114
on (26) is therefore exactly the existing P114 channel, with the
P115--P116 boundaries.  F144 makes no density claim for that scalar.

The positive mechanism in Sections 2--4 is different.  It uses exact
opposite-center containment and residual square classes, then decodes a
retained relation dependency.

## 7. Exact remaining gate

F144 does not show that a near-\(N\) block has one outgoing cross-star edge.
It does not show that the containment graph has a directed cycle, much less
\(R+1\) short cycles.  A quasipolynomial source can still produce a directed
acyclic graph or only long cycles.  Relation count and old-row reuse do not
imply (19).

The new source-side target is precise:

> Prove that on every surviving input, some frozen P128 stage contains
> \(R+1\) distinct directed containment cycles of polylogarithmic length
> among blocks larger than \(N/R\), for fixed polylogarithmic \(R,H,K\); or
> prove a weaker cycle family whose residual parity columns still have a
> nonzero dependency and whose total anchor product is below \(N/2\).

This is strictly narrower than the former combined rank-and-root target.
Once this public cycle-surplus condition holds, F144 supplies the factor.
