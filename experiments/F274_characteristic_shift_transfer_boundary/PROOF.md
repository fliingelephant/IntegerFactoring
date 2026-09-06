# Proof of F274

## 1. Balanced range

From \(p<q\),

\[
 p^2<pq<q^2.
\]

Taking square roots gives

\[
 p<\sqrt N<q.
\]

Since \(p\) is an integer,

\[
 p\leq\lfloor\sqrt N\rfloor=B<q,
\]

which proves (3).

## 2. Minimal polynomial of the regular shift

Let \(e_a\in V_r\) be the delta function at \(a\in\mathbb F_r\).  With
indices read modulo \(r\), translation permutes this basis in one cycle:

\[
 T_re_a=e_{a-1}.
\tag{34}
\]

Therefore \(T_r^r=I\).  The vector \(e_0\) is cyclic, because

\[
 e_0,T_re_0,\ldots,T_r^{r-1}e_0
\]

is the complete delta-function basis.  A polynomial of degree below \(r\)
cannot annihilate a cyclic vector spanning an \(r\)-dimensional space.
Hence the minimal polynomial has degree at least \(r\).  Since it divides
\(Z^r-1\), it is exactly

\[
 \mu_{T_r}(Z)=Z^r-1.
\tag{35}
\]

In characteristic \(r\), the binomial theorem gives

\[
 Z^r-1=(Z-1)^r.
\tag{36}
\]

Substituting \(T_r=I+\Delta_r\) into the minimal-polynomial statement
proves

\[
 \mu_{\Delta_r}(Z)=Z^r.
\tag{37}
\]

Thus \(\Delta_r^r=0\), while \(\Delta_r^{r-1}\ne0\).  This proves (8).
Combining it with \(p\leq B<q\) proves (9).

The nonzero assertion in the \(q\)-component is about the operator.  It
follows from its minimal polynomial and does not select a witness vector.

## 3. Subquotient dimension

Every \(T_r\)-stable subspace inherits the relation

\[
 (T_r-I)^r=0.
\]

Every quotient inherits it as well, and hence so does every subquotient.
Thus \(\overline\Delta_r\) is a nilpotent endomorphism of the
\(d_r\)-dimensional vector space \(W_r\).

For any nilpotent endomorphism on a \(d_r\)-dimensional vector space, the
strict chain

\[
 W_r\supseteq\operatorname{im}\overline\Delta_r
 \supseteq\operatorname{im}\overline\Delta_r^2\supseteq\cdots
\]

can have at most \(d_r\) nonzero strict descents.  Equivalently, its Jordan
blocks have size at most \(d_r\).  Therefore

\[
 \overline\Delta_r^{d_r}=0,
\]

proving (12).  If \(d_r\leq d\leq B\), then

\[
 \overline\Delta_r^B=0.
\]

Apply this once with \(r=p\) and once with \(r=q\) to obtain (13).  A local
rank drop cannot invalidate the conclusion because it decreases \(d_r\).

For the asymptotic statement, (1) gives

\[
 \sqrt{N/2}<p<\sqrt N.
\]

Hence \(\log_2p=\tfrac12\log_2N+O(1)=\Theta(n)\), which proves (14).
For fixed \(C,k\),

\[
 C(\log_2(n+1))^k=o(n).
\]

From the definition of \(n\), for \(n\geq4\),

\[
 N>2^{n-2},
\qquad
 p>\sqrt{N/2}>2^{(n-3)/2}.
\]

The quasipolynomial exponent is \(o(n)\), so it is smaller than
\((n-3)/2\) for all sufficiently large \(n\).  This proves (15).

Nothing in this argument applies to an implicit representation that does
not expose a \(d\)-element basis, or to a state that does not intertwine
cyclic translation.

## 4. Integer-polynomial forward differences

The ordinary finite-difference formula gives

\[
 \delta^kF(a)
 =\sum_{j=0}^{k}(-1)^{k-j}\binom kjF(a+j).
\tag{38}
\]

For a monomial at zero, the standard surjection count gives

\[
 \sum_{j=0}^{k}(-1)^{k-j}\binom kjj^t
 =k!S(t,k).
\tag{39}
\]

For completeness, count all maps from a \(t\)-element labelled set to a
\(k\)-element labelled set by inclusion-exclusion over missing image
points.  The left side of (39) is the number of surjections.  Partitioning
the domain into the \(k\) nonempty labelled fibres gives \(k!S(t,k)\).
When \(t<k\), both sides are zero.

Expand a shifted monomial:

\[
 (a+X)^m=\sum_{t=0}^{m}\binom mt a^{m-t}X^t.
\tag{40}
\]

Translation invariance of finite differences says

\[
 \delta^kX^m\big|_{X=a}
 =\delta^k(a+X)^m\big|_{X=0}.
\]

Applying (39) term by term to (40) yields

\[
 \frac{\delta^kX^m(a)}{k!}
 =\sum_{t=k}^{m}\binom mt a^{m-t}S(t,k)\in\mathbb Z.
\tag{41}
\]

Linearity over the integer coefficients \(c_m\) proves (19) and (17).
Putting \(m=k\) and \(a=0\) gives \(S(k,k)=1\), hence (20).

The entrywise vector and matrix statement follows by applying (17) to each
entry.  At \(k=B\), equation (3) shows that \(B!\) contains \(p\) and no
multiple of \(q\).  This proves the stated common-factor conclusion.
It does not control the remaining integer multiplier in (19), which may
itself vanish modulo either prime.

Dividing the integer identity by \(B!\) produces the explicit integer in
(19).  But \(p\mid B!\), so replacing exact integer division by modular
inversion over \(\mathbb Z/N\mathbb Z\) is invalid.  Evaluating the right
side independently computes the normalized value, from which the common
\(B!\) factor has been removed.

The example \(\binom XB=X(X-1)\cdots(X-B+1)/B!\) shows why the
\(\mathbb Z[X]\) hypothesis cannot be enlarged silently to all
integer-valued rational polynomials: its \(B\)-th difference is \(1\).

## 5. Rational shift coboundaries

First suppose

\[
 R(X)=\frac{h(X+1)}{h(X)}.
\tag{42}
\]

If \(h(X)=cX^d(1+O(X^{-1}))\) at infinity, then

\[
 \frac{h(X+1)}{h(X)}=1+O(X^{-1}),
\]

so \(R(X)\to1\).

Fix one translation orbit of monic irreducibles and enumerate it as

\[
 \ldots,P_{-1},P_0,P_1,\ldots,
 \qquad P_{j+1}(X)=P_j(X+1).
\tag{43}
\]

No nonconstant polynomial over characteristic zero is periodic under a
nonzero integer translation, so these orbit elements are distinct.  Let

\[
 u_j=v_{P_j}(h).
\]

Only finitely many \(u_j\) are nonzero.  From (42), the valuation sequence
of \(R\) along this orbit is a first difference of the \(u_j\), with one of
the two equivalent index conventions:

\[
 v_{P_j}(R)=u_{j-1}-u_j.
\tag{44}
\]

Therefore

\[
 \sum_jv_{P_j}(R)=0.
\tag{45}
\]

This proves necessity of both conditions.

Conversely, assume the two conditions.  On each orbit, let

\[
 e_j=v_{P_j}(R)
\]

have finite support and sum zero.  The recurrence

\[
 u_{j-1}-u_j=e_j
\tag{46}
\]

has a finitely supported integer solution: take cumulative sums from one
end of the finite support, and use \(\sum e_j=0\) to make the other tail
zero.  Form the finite rational product

\[
 h_0(X)=\prod_{\mathcal O}\prod_jP_j(X)^{u_j}.
\tag{47}
\]

Then \(h_0(X+1)/h_0(X)\) has exactly the same finite irreducible
valuations as \(R\).  Their quotient is a nonzero rational constant.
The limit at infinity is \(1\), so that constant is \(1\).  Thus \(h=h_0\)
satisfies (23), proving sufficiency.

Multiplying (23) at \(X,X+1,\ldots,X+m-1\) cancels every intermediate
factor and gives (25).

For \(R=(X+1)/X\), choose \(h=X\).  For \(R=X\), the limit at infinity is
not \(1\), so no rational gauge exists.  Every nonconstant polynomial has
the same failure.  The modular denominator warning follows because equality
in \(\mathbb Q(X)\) does not define inversion at a zero divisor.

## 6. Matrix determinant

Take determinants in (29).  Multiplicativity gives

\[
 \det G(X+1)=\det A(X)\det G(X).
\]

Since \(G\) is invertible over \(\mathbb Q(X)\), division by
\(\det G(X)\) in that field proves (30).  Theorem 4 now supplies every
determinant condition in Corollary 4.1.

Iterating (29) gives

\[
 G(X+m)
 =A(X+m-1)\cdots A(X)G(X).
\]

Right multiplication by \(G(X)^{-1}\) proves (32).  The order of the
noncommuting matrices is fixed by this derivation.

If \(\det A=1\), equation (30) only says that \(\det G\) is periodic.
It supplies no obstruction to the remaining matrix entries.  Likewise, a
determinant satisfying Theorem 4 is only a necessary condition for a full
matrix gauge.  These observations prove the stated surviving seams and
the exact exclusions.
