# Proof of the F151 V3 large-order and torus boundary

## 1. The exact-value decoder interface is complete

First consider any ordered list in (5). Removing a value equal to one does
not change an exact square class or a modular root.

Suppose one exact value \(A\equiv1\pmod N\) occurs twice in a selected
product. Removing those two copies divides the product by \(A^2\), so it
divides the positive root by \(A\). This does not change the root modulo
\(N\). Repeating this cancellation reduces the multiplicity of each exact
value modulo two. Therefore retaining only the first occurrence preserves
every binary square class and every root image modulo \(N\).

Repeated gcd splitting terminates because every proper split decreases the
integer blocks. Exact perfect-power extraction replaces \(h=a^k\) by the
base \(a\) and multiplies its exponent coordinates by \(k\). Repeating these
operations gives (6) with pairwise-coprime blocks that are not perfect
powers. This process uses gcd and exact division. It does not require the
rational-prime factorization of an input value.

For \(z\in\mathbb F_2^m\), put

\[
u_j=\sum_{i:z_i=1}E_{ji}.
\]

Then

\[
Q_z=\prod_j g_j^{u_j}.
\]

If every \(u_j\) is even, this is a square. Conversely, suppose some
\(u_j\) is odd. The block \(g_j\) is not a square, so it has a rational
prime divisor of odd valuation. Pairwise coprimality prevents another block
from changing that valuation. Thus \(Q_z\) is not a square. This proves
(10), and for a closure it gives the exact root

\[
R_z=\prod_jg_j^{u_j/2}.
\]

Every \(A_i\equiv1\pmod N\), so \(R_z^2\equiv1\pmod N\). If \(z,z'\) are
closures, then the positive roots for their common selected coordinates
contribute one factor \(A_i\) to \(R_zR_{z'}\). Hence

\[
R_{z+z'}\equiv R_zR_{z'}\pmod N.
\]

The root map from \(\ker M\) to the square roots of one modulo \(N\) is
therefore a homomorphism. If every vector in a kernel basis maps to a global
root \(\pm1\), every kernel vector does. Thus, if any closure has a
non-global root, every complete basis contains a vector with one. Since
\(N\mid(R_z-1)(R_z+1)\), either a trivial gcd in (9) would force
\(R_z\equiv\pm1\pmod N\). Thus both tests expose proper divisors for a
non-global root. This proves every decoder-interface claim in the statement.

## 2. The HH premise upgrades to every prime component

Invoke the HH premise. Its cost (3) is quasipolynomial for the choice (1).
Compute the powers \(\alpha^e\pmod N\) successively for
\(1\le e\le B\), and compute the gcd (12) after each multiplication. This
adds \(B\operatorname{poly}(n)\) bit operations and is quasipolynomial.

Let \(r\) be a rational prime divisor of \(N\). Suppose

\[
e=\operatorname{ord}_r(\alpha)\le B.
\]

Then \(r\mid\gcd(\alpha^e-1,N)\), so this gcd is larger than one. If it
were all of \(N\), then \(\alpha^e=1\pmod N\). This would give
\(\operatorname{ord}_N(\alpha)\le e\le B\), contrary to (HH). Therefore
the gcd is a proper factor.

On the surviving branch no such \(r\) exists. This proves (11), including
when \(N\) has repeated prime factors. It proves no claim about exponents
larger than \(B\).

## 3. The listed short-window screens are null

Fix a rational prime \(r\mid N\). On the surviving branch,

\[
\operatorname{ord}_r(\alpha)>B.
\tag{26}
\]

Let \(L=\lfloor B/4\rfloor\). For distinct \(e,f\le L\), a local zero of
one of the four expressions in (14) gives, in their displayed order,

\[
\alpha^{e-f}=1,
\qquad
\alpha^{e-f}=-1,
\qquad
\alpha^{e+f}=1,
\qquad
\alpha^{e+f}=-1
\pmod r.
\]

After squaring the two minus-one cases, a positive exponent from this list
is bounded respectively by

\[
L-1,
\qquad
2(L-1),
\qquad
2L,
\qquad
4L.
\]

Every bound is at most \(B\). Each case contradicts (26). No prime divisor
of \(N\) divides an expression in (14), so all four gcds are one.

By (2), \(w_e\equiv\alpha^{-e}\pmod N\). A local zero of
\(c_e-w_e\) gives \(\alpha^{2e}=1\pmod r\). A local zero of
\(c_e+w_e\) gives \(\alpha^{2e}=-1\pmod r\), and hence
\(\alpha^{4e}=1\pmod r\). The exponents satisfy

\[
2e\le2L\le B,
\qquad
4e\le4L\le B.
\]

Both cases contradict (26). This proves (15).

The definition of \(w_e\) also gives

\[
c_ew_e\equiv1\pmod N.
\]

Both endpoints are canonical positive integers. Hence (16) holds for an
integer \(\kappa_e\). The product could equal one only if
\(c_e=w_e=1\), which would contradict (26). Hence \(\kappa_e\ge1\).

### Exact witnesses outside the modular screens

For the equality witness, \(N=143\), \(B=8\), and \(\alpha=2\). Direct
calculation gives

\[
\operatorname{ord}_{11}(2)=10,
\qquad
\operatorname{ord}_{13}(2)=12.
\]

The first two canonical inverse pairs are

\[
(c_1,w_1)=(2,72),
\qquad
(c_2,w_2)=(4,36),
\]

and both products equal \(144\). Thus the first-occurrence rule has a real
duplicate to remove even though all listed screens are null.

For the closure witness, \(N=391\), \(B=12\), and \(\alpha=37\). Reduction
modulo the two prime factors gives

\[
\operatorname{ord}_{17}(37)=16,
\qquad
\operatorname{ord}_{23}(37)=22.
\]

Thus the complete scan through exponent \(12\) survives. The first two
canonical inverse pairs and values are

\[
(c_1,w_1)=(37,74),
\qquad
P_1=2738=2\cdot37^2,
\]

\[
(c_2,w_2)=(196,2),
\qquad
P_2=392=2^3\cdot7^2.
\]

A valid factor-free block basis is \((2,7,37)\). The two exponent columns
are

\[
(1,0,2)^T,
\qquad
(3,2,0)^T.
\]

They are equal modulo two. Their closure has

\[
P_1P_2=1{,}073{,}296=1036^2.
\]

Finally,

\[
\gcd(1035,391)=23,
\qquad
\gcd(1037,391)=17.
\]

This verifies (17). It is an existential capability witness, not an
all-input claim.

## 4. The Pilatte premise gives the stated catalogue boundary

The definitions of \(n\) and \(d\) give

\[
d=\Theta(\sqrt n).
\]

Choose a fixed positive \(C\) large enough that the norm premise is bounded
by \(R=\exp(Cd)\). A vector in this ball has \(d\) coordinates, each using
\(O(d)\) bits. One vector therefore has an \(O(d^2)=O(n)\)-bit coordinate
description.

The integer Euclidean ball is contained in the coordinate cube of radius
\(R\), so it has at most

\[
(2R+1)^d=\exp(O(d^2))
\]

points. It contains the coordinate cube of radius
\(\lfloor R/\sqrt d\rfloor\), so it has at least

\[
\left(2\left\lfloor\frac R{\sqrt d}\right\rfloor+1\right)^d
=\exp(\Theta(d^2))
\]

points. The full count is therefore

\[
\exp(\Theta(d^2))=\exp(\Theta(n)).
\]

This is not quasipolynomial in \(n\). A norm bound does not imply a support
bound. It permits all \(d\) coordinates to be nonzero. The premise says
nothing about a structured classical sampler, so no sampling lower bound
follows.

## 5. The direct Jacobi-torus splice

Let \(r\) be \(p\) or \(q\). The local-order condition with \(B\ge4\)
implies that \(\alpha\) is neither \(1\) nor \(-1\) modulo \(r\). Hence

\[
x^2-1
=
\left(\frac{\alpha-\alpha^{-1}}2\right)^2
\tag{27}
\]

is a nonzero square modulo \(r\). A quadratic character is unchanged by
inversion. Therefore

\[
\left(\frac{\Delta^{-1}(x^2-1)}r\right)
=
\left(\frac\Delta r\right),
\]

which proves (22).

The Jacobi-minus-one condition makes the two local Legendre symbols
opposite. Equation (23) is equivalent to \(y^2=b\). It has a solution in
exactly the split component and no solution modulo \(N\).

In the split field, a choice \(s^2=\Delta\) gives

\[
y=\frac{\alpha-\alpha^{-1}}{2s},
\qquad
x+ys=\alpha,
\qquad
x-ys=\alpha^{-1}.
\]

The nonsplit component has no coefficient \(y\) with this fixed \(x\).
These local data cannot be assembled as one public norm-one point over
\(\mathbb Z/N\mathbb Z\).

Finally, put

\[
S_m=\frac{\alpha^m+\alpha^{-m}}2.
\]

Direct multiplication gives

\[
S_0=1,
\qquad
S_1=x,
\qquad
S_{m+1}=2xS_m-S_{m-1}.
\]

The recurrence and initial values in (24) prove \(S_m=T_m(x)\) for every
integer \(m\ge0\), including \(m=0\). The formula contains no \(\Delta\).
It therefore loses the explicit split/nonsplit orientation in this direct
fixed-Kummer-coordinate splice. No conclusion about another coordinate or
another torus construction follows.
