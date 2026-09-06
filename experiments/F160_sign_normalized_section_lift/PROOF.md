# Proof of F160 sign-normalized section lifts

## 1. The sign-normalized lift

Fix \(r\in\{p,q\}\). Since \(g_r\) has order \(M\) and
\(\gcd(a,M)=1\), the element \(g_r^a\) also has order \(M\). Let

\[
d_r=\operatorname{ord}_r(x).
\]

Equation (2) gives

\[
\frac{d_r}{\gcd(d_r,2)}=M.
\tag{17}
\]

### Even \(M\)

If \(M\) is even, \(d_r\) cannot be odd. Equation (17) therefore gives

\[
d_r=2M.
\]

This holds for both hidden primes, so \(x\) is already the next
common-order generator.

### Odd \(M\)

If \(M\) is odd, two is invertible modulo \(M\). Let \(k\) be the unique
solution of \(2k\equiv a\pmod M\). Then \(g_r^k\) is an internal square
root of \(g_r^a\). Odd characteristic gives exactly two local roots, so

\[
x\equiv\pm g^k\pmod r.
\tag{18}
\]

The gcd in (6) distinguishes the four CRT sign patterns.

- A mixed sign gives a proper factor.
- If both signs are positive, then \(d=N\) and \(x\equiv g^k\pmod N\).
  The procedure replaces it by \(-x\).
- If both signs are negative, then \(d=1\) and the procedure keeps \(x\).

In either no-factor case, \(y\equiv-g^k\) in both hidden fields.
Coprimality of \(a\) with \(M\) and invertibility of two give
\(\gcd(k,M)=1\), so \(g_r^k\) has order \(M\). Since \(M\) is odd,
\(-g_r^k\) has order \(2M\). Hence (4) holds.

Exact local order \(2M\) implies the public P144 certificate for
\((y,2M)\): \(y^{2M}\equiv1\pmod N\), and for every prime
\(\ell\mid2M\), neither local reduction of \(y^{2M/\ell}\) is one.
Therefore each certificate gcd is one. The factorization of \(2M\) is
obtained from the supplied factorization of \(M\).

For odd \(M\), taking the public internal root \(x_0=g^k\) and then its
negative gives the source-free doubling stated in Section 1.

## 2. The section bridge

Equation (7) and the public equality (8) give

\[
(uz_v)^2\equiv u^2Q(v)\equiv g^a\pmod N.
\]

Thus \(x=uz_v\) satisfies every hypothesis of Section 1. Verification uses
only parity-span coordinates, modular multiplication, one modular
congruence, an integer gcd, and the sign-normalization test. These
operations are polynomial in the explicit transcript length. Scanning a
quasipolynomial candidate list therefore remains quasipolynomial.

For an F154 inverse representative, \(s_v^2\equiv Q(v)^{-1}\pmod N\).
Equation (10) then gives \(s_v^2\equiv g^a\pmod N\), so the same theorem
applies with \(x=s_v\).

## 3. The even-order character formula

Fix \(r\in\{p,q\}\), and choose a primitive element \(\zeta_r\) of
\(\mathbf F_r^\times\). Since \(g_r\) has exact order \(M\), it has the
form

\[
g_r=\zeta_r^{c_rt_r},
\qquad
c_r=\frac{r-1}{M},
\qquad
\gcd(t_r,M)=1.
\]

Because \(M\) is even, both \(t_r\) and every \(a\) coprime to \(M\) are
odd. Euler's criterion gives

\[
\left(\frac{g^a}{r}\right)
=(-1)^{c_rt_ra}
=(-1)^{c_r},
\]

which proves (12).

A square root exists in \(\mathbf F_r\) exactly when \(c_r\) is even,
equivalently when \(2M\mid r-1\). Multiplying the two characters proves the
two Jacobi cases. The displayed \(M=2\) examples verify that Jacobi value
\(+1\) is compatible with both local-capacity patterns:

\[
174^2=30276\equiv-1\pmod{221},
\]

while both \(7\) and \(11\) are \(3\pmod4\), so \(-1\) is nonsquare in
both fields modulo \(77\).

## 4. The paired-discriminant equivalence

Assume \(\left(\frac gN\right)=+1\) and
\(\left(\frac DN\right)=-1\). Multiplicativity gives

\[
\left(\frac EN\right)
=\left(\frac DN\right)
 \left(\frac {g^a}N\right)
=-1.
\]

Equation (14) follows from \(E\equiv Dg^a\pmod N\). If
\(x^2\equiv g^a\pmod N\), then \((Dx)^2\equiv DE\pmod N\).
Conversely, if \(z^2\equiv DE\pmod N\), then
\((D^{-1}z)^2\equiv g^a\pmod N\). Both transformations use a public unit
and are exact modulo \(N\). This proves (15)--(16).

Thus the natural P140 pair and the original primitive-root gate are the
same scalar-root problem under a public change of coordinates. Jacobi data
creates the orientation pair, but it does not create the required root.
