# F144 proof — residual-cycle closure and metric root separation

## 1. One bridge occurrence

For one legal squared-anchor word, use the notation

\[
U=qa^2,
\qquad
c=[U]_N,
\qquad
w=\iota_N(c),
\qquad
U=c+tN.
\]

P128 retains

\[
C=cw,
\qquad
L=Uw.
\]

Their product is

\[
CL=Uc\,w^2.
\tag{1}
\]

If \(c=rT\), then the bridge part in (1) is

\[
Uc=qa^2rT.
\tag{2}
\]

All factors displayed here are units modulo \(N\).  In particular, \(T\)
is a unit because it divides the unit \(c\).

## 2. Products around directed cycles

Select a nonempty indexed collection of directed cycles.  Let the products
over all logical edge occurrences be

\[
Q_{\rm tail}=\prod_eq_e,
\qquad
Q_{\rm head}=\prod_er_e,
\qquad
\mathcal A=\prod_ea_e,
\qquad
\mathcal T=\prod_eT_e,
\qquad
W=\prod_ew_e.
\]

Every directed cycle has the same multiset of tail and head vertices.
Multiplying over any collection of cycles therefore gives the exact integer
identity

\[
Q_{\rm tail}=Q_{\rm head}=:Q.
\tag{3}
\]

The endpoint factorizations \(c_e=r_eT_e\) give

\[
\prod_ec_e=Q\mathcal T.
\tag{4}
\]

Assume \(\mathcal T=S^2\).  Multiplying (1)--(2) over all occurrences and
using (3) gives

\[
\prod_eC_eL_e
=Q^2\mathcal A^2S^2W^2
=(Q\mathcal A S W)^2.
\tag{5}
\]

Thus the selected actual P128 values have an exact positive square root

\[
R_0=Q\mathcal A S W.
\tag{6}
\]

Because \(w_e\equiv c_e^{-1}\pmod N\), equations (4) and
\(\mathcal T=S^2\) give

\[
W\equiv(QS^2)^{-1}\pmod N.
\]

Substitution in (6) proves

\[
R_0\equiv\mathcal A S^{-1}\pmod N.
\tag{7}
\]

Squaring (7) proves

\[
\mathcal A^2\equiv S^2\pmod N.
\tag{8}
\]

This proves the exact dependency and root formulas.

## 3. A wrap makes the root metrically asymmetric

For every occurrence, \(U_e=c_e+t_eN\ge c_e\).  If at least one edge is
wrapped, one inequality is strict.  Hence

\[
\prod_eU_e>\prod_ec_e.
\tag{9}
\]

The left side is \(Q\mathcal A^2\) by (3), and the right side is
\(QS^2\) by (4).  Cancel the positive integer \(Q\).  Equation (9) gives

\[
\mathcal A^2>S^2,
\qquad
\mathcal A>S.
\tag{10}
\]

Now assume \(2\mathcal A<N\).  Then

\[
0<\mathcal A-S< N,
\qquad
0<\mathcal A+S< N.
\tag{11}
\]

Equation (8) says that \(N\) divides
\((\mathcal A-S)(\mathcal A+S)\).  Neither factor in (11) is divisible by
\(N\).  Neither can be invertible modulo \(N\), because invertibility of
one would force the other to be zero modulo \(N\).  Therefore

\[
1<\gcd(\mathcal A-S,N)<N,
\qquad
1<\gcd(\mathcal A+S,N)<N.
\tag{12}
\]

Equivalently, (7) is neither global sign.  This proves the metric root
claim without a distribution or random-scalar assumption.

If no edge wraps, then every \(U_e=c_e\).  Equations (3)--(4) give
\(Q\mathcal A^2=QS^2\), so \(\mathcal A=S\) and the normalized root is
\(+1\).  Thus wrapping is the exact source of the metric asymmetry in this
lemma.

## 4. Exact-value deletion

The logical selection in (5) can use the same source bridge in two cycles,
and distinct source positions can give the same actual exact value.  Work at
the actual \(C_e,L_e\) level.  If one exact integer \(P\) occurs at least
twice, remove two occurrences.  This divides the selected product by
\(P^2\), so it remains an exact square.  Its positive root is divided by
\(P\).  Since every actual retained relation value satisfies
\(P\equiv1\pmod N\), the residue of the root is unchanged.

Repeat until every exact value has multiplicity zero or one, and use the
globally retained representative for every odd multiplicity.  The result is
a legal binary dependency in the deduplicated P128 ledger with root (7).
Under (10)--(12), that dependency cannot be empty.  This proves the
deduplication claim.

## 5. Near-\(N\) edges are wrapped and have small residuals

Let \(q,r>N/R\), let \(q\ne r\) be current named blocks, let \(a\le H\),
and suppose \(c=[qa^2]_N=rT\).  Since \(c<N\),

\[
T={c\over r}<R.
\tag{13}
\]

Suppose the edge were unwrapped.  Then \(c=qa^2\), so \(r\mid qa^2\).
Current named blocks are pairwise coprime, hence \(\gcd(q,r)=1\), and
\(r\mid a^2\).  But the size condition gives

\[
r>N/R>H^2\ge a^2,
\]

which is impossible.  Every such cross edge is therefore wrapped.

## 6. Cycle surplus forces a residual square

Take \(J=R+1\) distinct simple directed cycles of length at most \(K\).
For cycle \(j\), form the parity vector of

\[
T(C_j)=\prod_{e\in C_j}T_e.
\]

Every \(T_e<R\), so every prime in every residual is strictly below \(R\).
There are at most \(R-1\) possible prime rows.  The \(J=R+1\) binary
columns are therefore linearly dependent.  Choose a nonzero kernel vector.
For the selected cycle indices, every rational-prime valuation in the total
residual product is even.  Hence that product is an exact integer square
\(S^2\).

The selected logical occurrences number at most \(K(R+1)\).  Their anchor
product satisfies

\[
\mathcal A\le H^{K(R+1)}<N/2.
\tag{14}
\]

The kernel vector is nonzero, so at least one nonempty cycle is selected.
Section 5 makes every occurrence on it wrapped.  Sections 2--3 now give the
proper factors (12).  Overlap between the selected cycles is handled by
Section 4.  This proves the cycle-surplus theorem.

## 7. Quasipolynomial cost

At one frozen stage, let \(M\) be the number of current named blocks.  The
P118 cost theorem bounds \(M\), the number of stages, and the complete
retained transcript by \(2^{(\log n)^{O(1)}}\).

For eligible prime anchors through \(H\), checking all ordered block pairs
for exact containment costs at most \(O(M^2H)\) arithmetic operations.
Enumerating all directed vertex sequences through length \(K\) costs at
most

\[
(M H)^{O(K)}.
\]

When \(H,K=(\log n)^{O(1)}\), this is
\(2^{(\log n)^{O(1)}}\).  Factoring each residual below
\(R=(\log n)^{O(1)}\) by trial division, binary linear algebra on \(R+1\)
columns, and all exact products and gcds also have quasipolynomial bit cost.
Multiplying by the quasipolynomial number of frozen stages preserves that
class.

Moreover,

\[
\log\left(H^{K(R+1)}\right)
=K(R+1)\log H
=(\log n)^{O(1)}
=o(n)
\]

for fixed polylogarithmic parameter exponents.  Since
\(N\ge2^{n-1}-1\), both size conditions hold for all sufficiently large
\(n\).  Direct integer comparisons verify them on every actual input.

## 8. The proportional-carry decoy

For two arbitrary cross-star endpoints, write

\[
c=qa^2-tN,
\qquad
d=rb^2-sN.
\]

Define

\[
\Delta=sc-td.
\]

Substitution gives the equivalent carry form

\[
\Delta=qa^2s-rb^2t.
\tag{15}
\]

If \(h=\gcd(c,d)\), then \(h\mid\Delta\).  Also

\[
0\le t<{qa^2\over N},
\qquad
0\le s<{rb^2\over N}.
\]

Both \(sc\) and \(td\) are strictly below \(qr a^2b^2/N\).  Their absolute
difference therefore satisfies

\[
|\Delta|<{qr a^2b^2\over N}.
\tag{16}
\]

It remains to classify \(\Delta=0\).  If \(t=0\), then \(sc=0\), so \(s=0\).
In this case both bridges are individual exact squares and their normalized
roots are \(+1\).

Otherwise \(t,s>0\).  Put

\[
g=\gcd(t,s),
\qquad
t=g\tau,
\qquad
s=g\sigma,
\qquad
\gcd(\tau,\sigma)=1.
\]

The equation \(\Delta=0\) is \(\sigma c=\tau d\).  Hence there is a positive
integer \(z\) with

\[
c=\tau z,
\qquad
d=\sigma z.
\tag{17}
\]

Let \(Z=z+gN\).  The unreduced words are

\[
qa^2=\tau Z,
\qquad
rb^2=\sigma Z.
\tag{18}
\]

The two bridge values are therefore

\[
qa^2c=\tau^2Zz,
\qquad
rb^2d=\sigma^2Zz.
\]

Their product is the exact square

\[
(\tau\sigma Zz)^2.
\]

The product of their supplied roots is
\(cd=\tau\sigma z^2\).  The normalized root is

\[
{Z\over z}\equiv1\pmod N.
\tag{19}
\]

Thus a zero two-endpoint carry determinant is an exact global-root decoy.
Together with (16), this also shows that making a common endpoint block so
large that it forces \(\Delta=0\) cannot prove useful closure.
Explicitly, if \(hN\ge qr a^2b^2\), then (16) gives
\(|\Delta|<h\); since \(h\mid\Delta\), one must have \(\Delta=0\).

## 9. P114 rectangle embedding

For two centers \(q,r\) and two anchors \(a,b\), put

\[
x_{00}=[qa^2]_N,
\quad x_{10}=[ra^2]_N,
\quad x_{01}=[qb^2]_N,
\quad x_{11}=[rb^2]_N.
\]

Set

\[
u=x_{00},
\qquad
\alpha=[rq^{-1}]_N,
\qquad
\beta=[b^2a^{-2}]_N.
\]

Direct multiplication modulo \(N\) gives

\[
[u\alpha]_N=x_{10},
\qquad
[u\beta]_N=x_{01},
\qquad
[u\alpha\beta]_N=x_{11}.
\]

Hence these four endpoints are exactly one P114 multiplicative rectangle.
The P114 inverse-carry determinant and its P115--P116 obstructions apply
without change.  This observation supplies no success-density theorem.
The residual-cycle proof above does not use this determinant.

## 10. Remaining limitation

All positive conclusions are conditional on public containment cycles.  The
proof gives no outgoing-edge theorem, no cycle-existence theorem, and no
bound on a longest acyclic cross-star transcript.  It only proves that a
polylogarithmic surplus of short cycles in the near-\(N\) range is already
enough: residual closure follows by linear algebra, and metric root
separation follows from canonical wrapping.
