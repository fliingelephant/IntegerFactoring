# Proof of F194 V2

## 1. Range

The balance promise gives

\[
p^2<N<2p^2,
\]

and hence

\[
p\le B<\sqrt2p<2p,
\qquad B<q.
\tag{17}
\]

Thus \(1,\ldots,B\) contains \(p\), but contains neither \(2p\) nor \(q\).

## 2. One hidden cancellation

The exact integer identity

\[
k!A_k=\prod_{i=1}^k(i-N)
\tag{18}
\]

holds for every \(k\). If \(k<p\), every denominator is a unit modulo \(N\),
so each factor \((i-N)/i\) is one modulo \(N\). Hence \(A_k\equiv1\).

Let \(p\le k\le B\), and put

\[
U=\prod_{\substack{1\le i\le k\\i\ne p}}i,
\qquad
V=\prod_{\substack{1\le i\le k\\i\ne p}}(i-N).
\]

The integer \(U\) is a unit modulo \(N\). Isolating the one nonunit factor
in (18) gives

\[
pUA_k=(p-N)V=p(1-q)V.
\]

Cancel \(p\) in \(\mathbb Z\), before reduction. Then

\[
UA_k=(1-q)V.
\]

Modulo \(N\), one has \(V\equiv U\), so cancellation of the unit \(U\)
proves (1).

For \(1\le k\le B\),

\[
k\binom Nk=N\binom{N-1}{k-1}.
\tag{19}
\]

When \(k\ne p\), the integer \(k\) is a unit modulo \(N\), which proves the
zero case of (2). At \(k=p\), exact integer cancellation gives

\[
\binom Np=q\binom{N-1}{p-1}\equiv q\pmod N,
\]

because \(p-1\) is before the jump. This proves (2).

The alternating prefix identity

\[
\sum_{k=0}^B(-1)^k\binom Nk=(-1)^B\binom{N-1}{B}
\tag{20}
\]

has only the terms \(1\) and \((-1)^pq=-q\) modulo \(N\). Therefore

\[
(-1)^B\binom{N-1}{B}\equiv1-q\pmod N.
\tag{21}
\]

This proves (3) and (4).

Finally, the adjacent-binomial ratio gives

\[
(k+1)A_{k+1}=-(N-1-k)A_k=(k+1-N)A_k,
\]

which is exactly (5).

## 3. Central-binomial comparisons

Let \(m=\lceil B/2\rceil\). One has

\[
m\le\frac{B+1}{2}<p,
\]

because \(B<\sqrt2p\) and \(\sqrt2p+1<2p\) for odd \(p\ge3\). Also

\[
p\le B\le2m.
\]

Since \(B<q\), integrality gives \(B+1\le q\), while \(2m\le B+1\).
Equality \(2m=q\) is impossible because \(2m\) is even and \(q\) is odd.
Thus

\[
m<p\le2m<q.
\tag{22}
\]

In \(\binom{2m}{m}\), the denominator is a unit modulo \(N\), and the
numerator interval contains exactly one multiple of \(p\) and no multiple of
\(q\). This proves (6).

In \(\binom{2B}{B}\), the denominator contains exactly the multiple \(p\)
and no multiple of \(q\). The numerator interval \([B+1,2B]\) contains
\(2p\) and \(q\). It contains no further multiple of \(p\), because
\(2B<2\sqrt2p<3p\), and no second multiple of \(q\), because \(2B<2q\).
The \(p\)-valuations cancel, while one \(q\) remains. This proves (7).

## 4. Polynomial moments

Write

\[
W(T)-W(0)=TV(T)
\]

with \(V\in\mathbb Z[T]\). By (19),

\[
\sum_{k=1}^{N-1}(W(k)-W(0))\binom Nk
=N\sum_{k=1}^{N-1}V(k)\binom{N-1}{k-1},
\]

which is zero modulo \(N\). The constant part is

\[
W(0)\sum_{k=1}^{N-1}\binom Nk=W(0)(2^N-2).
\]

This proves (8).

## 5. Frobenius block and Boolean incidence

Repeated squaring gives an \(O(\log N)\)-gate circuit for (9), and formal
differentiation gives

\[
E_N'=N(1+X)^{N-1}-NX^{N-1}=0
\]

over \(\mathbb Z/N\mathbb Z\).

In characteristic \(p\), Frobenius additivity gives (10). Its inner
polynomial has zero constant coefficient and nonzero linear coefficient
\(q\bmod p\), so its \(X\)-adic order is one. Its \(p\)-th power has exact
order \(p\). The argument modulo \(q\) proves (11) and exact order \(q\).

Write \(q=p+d\), where \(1\le d<p\). In characteristic \(p\),

\[
(1+X)^q-1-X^q
=\sum_{j=1}^d\binom djX^j
+X^p\sum_{j=0}^{d-1}\binom djX^j.
\]

Taking the \(p\)-th power proves (12). The two exponent ranges are disjoint,
and every coefficient is nonzero modulo \(p\). Equation (13) follows from

\[
(1+X)^p-1-X^p=\sum_{j=1}^{p-1}\binom pjX^j
\]

and the \(q\)-th power; these coefficients are nonzero modulo \(q\).

If \(d<R\), enumerate \(1\le\delta<R\). At \(\delta=d\),

\[
\delta^2+4N=(p+q)^2,
\]

and the square root recovers

\[
p=\frac{\sqrt{\delta^2+4N}-\delta}{2},
\qquad
q=\frac{\sqrt{\delta^2+4N}+\delta}{2}.
\]

The trial count is numerical QP because \(R\) is.

Now assume \(d\ge R\) and \(r\le R<p\). Multiplication by \(p\) or \(q\)
permutes \(\mathbb Z/r\mathbb Z\). Equation (12) contains the nonzero source
terms at exponents \(p,2p,\ldots,rp\), and (13) contains those at
\(q,2q,\ldots,rq\). Each list meets every residue class modulo \(r\). This
proves only the stated Boolean incidence claim.

## 6. Modular carry pair

Equation (21) makes the quotient (14) integral, and rearrangement proves
(16). Modulo \(2^t\), the two residues in (15) give \(q\bmod2^t\). Since
\(0<q<2^t\), they give the integer \(q\).

Conversely, with \(C\bmod2^t\) fixed, (16) gives

\[
h\equiv N^{-1}(q-1+(-1)^BC)\pmod{2^t}.
\]

Because \(N\) is odd, this is one value for every proposed \(q\bmod2^t\).
No computational conclusion beyond this congruence is used.
