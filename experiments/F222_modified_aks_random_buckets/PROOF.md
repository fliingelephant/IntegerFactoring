# F222 proof

## 1. Local normal form

In characteristic \(p\), Frobenius gives

\[
\begin{aligned}
E_a(X)
&=(X+a)^{pq}-X^{pq}-a^{pq}\\
&=\bigl((X+a)^q-X^q-a^q\bigr)^p
=h_{q,a}(X)^p.
\end{aligned}
\tag{1}
\]

The analogous identity modulo \(q\) is

\[
E_a=h_{p,a}^q.
\tag{2}
\]

In \(\mathbb F_p[X]/(X^r-1)\), the map

\[
\sum_j c_jX^j\longmapsto\sum_jc_j^pX^{pj}
\]

permutes coefficient positions because \(\gcd(p,r)=1\). It is a ring
automorphism and therefore preserves both support size and multiplication
nullity. The same holds modulo \(q\).

For \(a\ne0\), direct scaling gives

\[
h_{m,a}(X)=a^m h_{m,1}(X/a).
\tag{3}
\]

Thus \(h_{m,a}\) and \(X^r-1\) share a root exactly when there is a nonzero
root \(y\) of \(h_{m,1}\) such that

\[
(ay)^r=1,
\qquad y^r=a^{-r}\in\mathbb F_\ell^\times.
\tag{4}
\]

The map \(a\mapsto a^{-r}\) from \(\mathbb F_\ell^\times\) has image
\((\mathbb F_\ell^\times)^r\) and every fibre has cardinality
\(g_\ell=\gcd(r,\ell-1)\). Counting its accepted image values proves the
formula in Theorem A.

CRT makes uniform local unit components independent. A global resultant is
zero modulo exactly one hidden prime with probability

\[
\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p),
\]

and modulo both with probability \(\alpha_p\alpha_q\). A division-free
resultant computation over \(\mathbb Z/N\mathbb Z\), followed by an integer
gcd, implements the proper event in time polynomial in \(r\) and \(n\).

## 2. Counting local annihilating shifts at bounded gap

Let \(\xi\) be one of the \(r\) distinct roots of \(X^r-1\) in an
algebraic closure. In characteristic \(p\), use \(q=p+d\) and Frobenius:

\[
h_{q,a}(\xi)
=\xi^p\bigl((\xi+a)^d-\xi^d\bigr)
+a\bigl((\xi+a)^d-a^d\bigr).
\tag{5}
\]

For \(a\in\mathbb F_p\), this is a polynomial of degree at most \(d\).
It is not the zero polynomial when \(p>d^2+1\). Indeed, its coefficients of
\(a^d\) and \(a\) are respectively

\[
\xi(\xi^{p-1}+d),
\qquad
\xi^d(d\xi^{p-1}+1).
\tag{6}
\]

If both vanished, then \(d^2=1\pmod p\), impossible for the positive even
prime gap \(d\) under \(p>d^2+1\). Hence each \(\xi\) permits at most \(d\)
shifts in \(\mathbb F_p\), and the union bound over the \(r\) roots gives

\[
\Pr(\nu_p(a,r)>0)\le\frac{rd}{p-1}
\tag{7}
\]

for a uniform nonzero local shift.

In characteristic \(q\), put \(p=q-d\). For
\(a\ne0,-\xi\), the equality \(h_{q-d,a}(\xi)=0\), after multiplication by
\(a^{d-1}(\xi+a)^d\), implies

\[
P_\xi(a)=
a^{d-1}(\xi^q+a)
-a^{d-1}\xi^{q-d}(\xi+a)^d
-(\xi+a)^d=0.
\tag{8}
\]

This polynomial has degree \(2d-1\) and leading coefficient
\(-\xi^{q-d}\ne0\). It has at most \(2d-1\) roots. Adding the possibly
excluded value \(a=-\xi\), when it lies in \(\mathbb F_q^\times\), gives at
most \(2d\) accepted unit shifts per \(\xi\). Therefore

\[
\Pr(\nu_q(a,r)>0)\le\frac{2rd}{q-1}.
\tag{9}
\]

Equations (7)--(9) prove Theorem B. For several calls, condition on the
previous transcript. Once \(r_i\) is fixed, the next fresh local shifts are
again independent and uniform, so the same bound applies. A union bound
gives

\[
\Pr(\text{some annihilation})
\le
\left(\frac d{p-1}+\frac{2d}{q-1}\right)\sum_i r_i.
\tag{10}
\]

The promoted bounded-gap theorem used in P165 gives infinitely many prime
pairs with gap at most one absolute constant. Since only finitely many even
gaps occur in that range, one value \(d_0\) occurs infinitely often. On
that subfamily, \(p,q=2^{\Theta(n)}\). If \(\sum_i r_i\) is numerical QP,
(10) is \(2^{-\Omega(n)}\).

## 3. The coefficient-support dichotomy

Equation (5) is an identity of polynomials, not only an identity at roots:

\[
h_{q,a}(X)
=X^p\bigl((X+a)^d-X^d\bigr)
+a\bigl((X+a)^d-a^d\bigr)
\pmod p.
\tag{11}
\]

The first bracket has at most \(d\) monomials and the second has at most
\(d\) monomials. Thus \(h_{q,a}\), after reduction modulo \(X^r-1\), has
support at most \(2d\). Frobenius in (1) only permutes positions, so

\[
|\operatorname{supp}(E_a\bmod p)|\le2d.
\tag{12}
\]

Suppose the complete global coefficient scan returns no proper gcd. At any
position, a coefficient cannot be zero in exactly one hidden field, because
its gcd with \(N\) would then be the corresponding prime. Hence the two
local zero sets, and therefore the two local supports, are identical.
Equation (12) proves that both have size at most \(2d\). This proves the
dichotomy.

When \(r>2d\), this conclusion is nonvacuous. But then a QP numerical \(r\)
forces a QP numerical gap. Fermat starts at \(\lceil\sqrt N\rceil\). Its
real gap for factors \(p,q\) is

\[
\frac{p+q}{2}-\sqrt{pq}
=\frac{(q-p)^2}{2(\sqrt p+\sqrt q)^2}
=O(d^2/\sqrt N).
\tag{13}
\]

Rounding changes the required number of scan positions by only a constant.
For numerical-QP \(d\), this is QP. Thus the currently proved raw-bucket
gain occurs only inside an independently easy close-factor branch.
