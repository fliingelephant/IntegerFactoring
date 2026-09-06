# Proof of the F153 Jacobi-torus section obstruction

## 1. The discriminant orientation is a character

For every unit modulo an odd prime, the Legendre symbol is multiplicative and
depends only on the exponent modulo two. Therefore

\[
\left(\frac{\prod_iD_i^{e_i}}p\right)
=\prod_i\left(\frac{D_i}p\right)^{e_i}
=\prod_i\epsilon(D_i)^{e_i}=\eta.
\tag{1.1}
\]

Because every \(D_i\) has Jacobi symbol minus one,

\[
\left(\frac{D_i}q\right)=-\epsilon(D_i).
\]

Hence

\[
\left(\frac{\prod_iD_i^{e_i}}q\right)
=(-1)^{\sum_i e_i}\eta=(-1)^\delta\eta.
\tag{1.2}
\]

This proves (3). If two words have the same local squareclass, their quotient
has Legendre symbol one at both primes, so their values of \(\eta\) agree. If
a word is a square modulo \(N\), (1.1) gives \(\eta=1\), and (1.2) then gives
\((-1)^\delta=1\).

In additive \(\mathbf F_2\) notation, the map

\[
[D]\longmapsto
\begin{cases}
0,&(D/p)=1,\\
1,&(D/p)=-1
\end{cases}
\]

is a linear functional on the generated squareclass space. Thus every word
presentation receives one well-defined character value. Any purported lift
rule that contains no hidden datum beyond this value is the restriction of
that same homomorphism. Two presentations of one squareclass cannot disagree.
This is exactly the formal no-disagreement case in the repaired F152
split-or-section vocabulary. It says nothing about extra integer or torus
coordinates.

## 2. The signed gap and its one forced division by two

At a prime \(r\), the norm-one torus associated with \(D\) has order

\[
r-\left(\frac Dr\right).
\]

With \(\epsilon=(D/p)=-(D/q)\), the two orders are

\[
m_p=p-\epsilon,
\qquad
m_q=q+\epsilon.
\tag{2.1}
\]

Direct multiplication gives

\[
m_pm_q
=(p-\epsilon)(q+\epsilon)
=pq-1-\epsilon(q-p)
=N-1-\epsilon g.
\tag{2.2}
\]

The difference between the exponents in (6) is a multiple of both local
orders, so (6) follows componentwise. Since \(p,q\) are odd, both \(m_p\)
and \(m_q\) are even. Thus

\[
\frac{m_pm_q}{2}
=m_p\frac{m_q}{2}
=m_q\frac{m_p}{2}
\tag{2.3}
\]

is also a multiple of both orders. The exponents \((N-1)/2\) and \(g/2\)
are integers. Dividing (2.2) by two and reducing in both local groups proves
(7). Its square is (6), so the public half is synchronized.

For a further division by \(2^k\), this same exponent argument needs
\(2^k\mid m_q\) to retain divisibility by \(m_p\), and
\(2^k\mid m_p\) to retain divisibility by \(m_q\). It also needs
\(2^k\mid g\). If \(k\ge2\), the first two requirements imply

\[
p\equiv\epsilon\pmod4,
\qquad
q\equiv-\epsilon\pmod4,
\]

and hence

\[
g=q-p\equiv-2\epsilon\pmod4.
\]

This contradicts \(4\mid g\). Therefore the direct P55 exponent division
cannot continue beyond the one forced halving.

## 3. Exact Cayley halving

The Cayley product is

\[
U_D(a)U_D(b)
=U_D\!\left(\frac{a+b}{1+Dab}\right)
\tag{3.1}
\]

whenever the named denominators are units. Setting \(a=b=s\), injectivity
of the clean Cayley chart gives

\[
t=\frac{2s}{1+Ds^2}.
\]

After clearing its unit denominator, this is (9). Its ordinary quadratic
discriminant is

\[
(-2)^2-4(Dt)t=4(1-Dt^2)=4z_D(t).
\]

If \(s\) solves (9), put \(r=1-Dts\). Then

\[
r^2
=1-2Dts+D^2t^2s^2.
\]

Multiplying (9) by \(Dt\) gives

\[
D^2t^2s^2=2Dts-Dt^2.
\]

Substitution yields \(r^2=1-Dt^2=z_D(t)\). Conversely, the quadratic formula
over each CRT field gives (12); CRT assembles a global solution exactly when
the selected local roots assemble to a square root modulo \(N\). A solution
cannot have \(1+Ds^2=0\) in a local field: substituting that equality into
(9) gives \(-2s=0\), which contradicts \(Ds^2=-1\). Thus the clean formulas
are consistent.

Fix one global root \(r\). The roots \(r\) and \(-r\) reverse sign in both
CRT components. In each local cyclic torus, the two distinct halves of one
element differ by its unique nonidentity two-torsion point, namely \(-1\).
Therefore the corresponding global halves differ by \((-1,-1)\), the global
element \(-1\).

If \(r'\) is another square root not congruent to \(r\) or \(-r\) modulo
\(N\), then

\[
k=r'r^{-1},\qquad k^2=1\pmod N,
\]

and \(k\ne\pm1\). Hence one of \(\gcd(k-1,N)\) and \(\gcd(k+1,N)\) is a
proper factor. Equivalently one can use \(\gcd(r'-r,N)\) and
\(\gcd(r'+r,N)\). The mixed half choice therefore contains the factor before
it is interpreted in the torus.

## 4. Products of discriminants and quadratic algebras

For \(F=DE\), Theorem 1 gives

\[
\left(\frac Fp\right)
=\left(\frac Fq\right)
=\epsilon(D)\epsilon(E)=\eta.
\tag{4.1}
\]

The local orders of \(T_F\) are \(p-\eta\) and \(q-\eta\). Also

\[
(p-\eta)(q-\eta)
=pq-\eta(p+q)+1
=N-1-\eta(p+q-2\eta).
\tag{4.2}
\]

The exponent difference in (4.2) is divisible by both local orders. This
proves (14) for every point, including nongenerators. Substituting
\(\eta=1\) gives \(p+q-2\); substituting \(\eta=-1\) gives
\(-(p+q+2)\).

Now let \(\phi:A_D\to A_E\) be a unital \(R\)-algebra map that commutes with
conjugation. Write

\[
\phi(w_D)=a+bw_E.
\]

Commutation with conjugation gives

\[
-a-bw_E=a-bw_E.
\]

Because \(N\) is odd, two is a unit, so \(a=0\). Preserving the equation
\(w_D^2=D\) then gives

\[
b^2E=D.
\tag{4.3}
\]

Since \(D,E\) are units, so is \(b\). Conversely, any unit satisfying
(4.3) defines the stated isomorphism, with inverse
\(w_E\mapsto b^{-1}w_D\). By (4.1), \(D/E\) is a square in both fields
exactly when \(\epsilon(D)=\epsilon(E)\), which proves (15) and its existence
criterion. Opposite global choices \(b,-b\) differ by conjugation. Any two
roots not opposite globally have a non-global quotient of square one and
factor \(N\), as in Section 3.

For the norm identities, let \(\tau_D\) flip \(w_D\) and fix \(w_E\), and
let \(\tau_E\) flip \(w_E\) and fix \(w_D\). The fixed rings of
\(\tau_E,\tau_D,\tau_D\tau_E\) are respectively \(A_D,A_E,A_F\), with
\(w_F=w_Dw_E\). Since

\[
\tau_D(U)=U^{-1},
\qquad
\tau_E(V)=V^{-1},
\]

and each other action fixes the other point,

\[
(UV)\tau_E(UV)=U^2,
\]

\[
(UV)\tau_D(UV)=V^2,
\]

\[
(UV)(\tau_D\tau_E)(UV)=UVU^{-1}V^{-1}=1.
\]

These are exactly (17).

## 5. Ordinary high order and the nonsplit torus

The image order of a homomorphism between finite groups divides both the
source order and the target order. For a nonsquare \(D\) modulo \(r\), those
orders are \(r-1\) and \(r+1\). Their gcd is two, proving (18).

Consequently no homomorphic construction can transfer the large odd-order
part of an ordinary unit into the nonsplit local torus. On a
Jacobi-minus-one discriminant, one of the two hidden components is always
nonsplit. A globally uniform homomorphic splice therefore cannot preserve a
Harvey--Hittmeir large-order certificate in both components.

F151 already computes the natural Kummer alternative. For

\[
x=(\alpha+\alpha^{-1})/2,
\qquad
y^2=D^{-1}(x^2-1),
\]

the right side has local quadratic character \((D/r)\). Hence a \(y\)
exists only in the split component. Keeping only \(x\) gives the
discriminant-independent Chebyshev identity

\[
T_m(x)=(\alpha^m+\alpha^{-m})/2.
\]

Thus the direct non-homomorphic splice also supplies no second orientation
lift. No conclusion follows for a new torus-native high-order algorithm or
for a coordinate map with a separately proved torus-order law.

## 6. Scope

The proof classifies the stated direct operations only. It does not give a
lower bound for all coordinate algorithms, and it does not exclude a
resultant, determinant, derivative, first lift, metric rule, or another
non-norm invariant of the rank-four biquadratic algebra. It also does not
extend P55 from distinct odd semiprimes to arbitrary composite inputs.

Its exact negative conclusion is narrower: Jacobi orientation alone is one
compatible character section, and the standard doubling, halving, norm, and
ordinary-high-order splices do not force that section to disagree with
itself.
