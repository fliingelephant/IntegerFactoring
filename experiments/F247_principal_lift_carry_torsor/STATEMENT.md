# F247 candidate — principal-lift carry torsor

## Status and scope

This is a proof-only candidate. It studies the second base-\(N\) digit of an
ordinary or quadratic-torus power after the corresponding modulo-\(N\)
order trial has returned no factor.

The main result is exact. A change of lift that is invisible modulo \(N\)
acts affinely on the carry. If the lift parameter is uniform and the
exponent is a unit modulo \(N\), the free carry coordinate is exactly
uniform, even after the complete modulo-\(N\) transcript is fixed.

This rules out one inference:

\[
\boxed{
\text{a failed modulo-}N\text{ order transcript alone}
\;\Longrightarrow\;
\text{a biased lift carry}.}
\]

It does **not** rule out the canonical integer section. The canonical carry
uses one fixed lift, not a random lift from the fibre. Its distribution can
still contain factor-correlated information.

Throughout, \(N\) is odd and

\[
\langle z\rangle_N\in\{0,\ldots,N-1\}
\]

denotes the least nonnegative residue of \(z\) modulo \(N\).

## 1. Ordinary affine lift law

Let \(a\) be a unit modulo \(N\). Fix an integer exponent \(E\ge1\) with

\[
\gcd(E,N)=1.
\]

For \(t\in\mathbb Z/N\mathbb Z\), put

\[
a_t=a+Nt\pmod {N^2},
\qquad
x=\langle a^E\rangle_N.
\]

Define \(K_t\in\mathbb Z/N\mathbb Z\) by

\[
a_t^E\equiv x+NK_t\pmod {N^2}.
\tag{1}
\]

Then

\[
\boxed{
K_t=K_0+Ea^{E-1}t\pmod N.
}
\tag{2}
\]

The coefficient in (2) is a unit modulo \(N\). Therefore \(t\mapsto K_t\)
is a bijection of \(\mathbb Z/N\mathbb Z\).

Every \(a_t\) has the same residue modulo \(N\). Hence every ordinary
order-return transcript that is computed only modulo \(N\) is unchanged as
\(t\) varies. Conditional on that complete transcript, a uniform fresh \(t\)
makes \(K_t\) exactly uniform modulo \(N\).

The same affine law holds for a signed carry. If

\[
a_t^E\equiv \sigma+NC_t\pmod {N^2},
\qquad \sigma\in\{+1,-1\},
\]

then

\[
C_t=C_0+Ea^{E-1}t\pmod N.
\tag{3}
\]

For a negative return, the canonical-residue carry and signed carry differ
by one: \(C_t=K_t+1\).

## 2. Exact probability laws for a uniform carry

Assume now that

\[
N=pq
\]

for distinct odd primes \(p\) and \(q\). Let \(K\) be uniform on
\(\{0,\ldots,N-1\}\). Then

\[
\Pr(\gcd(K,N)=1)={\varphi(N)\over N},
\tag{4}
\]

\[
\boxed{
\Pr(1<\gcd(K,N)<N)={p+q-2\over N},
}
\tag{5}
\]

and

\[
\Pr(\gcd(K,N)=N)={1\over N}.
\tag{6}
\]

If \(L\) is fixed and \(K\) is uniform, then \(K-L\bmod N\) is uniform.
Thus the next formula is exact even after a complete past that fixes \(L\):

\[
\boxed{
\Pr(1<\gcd(K-L,N)<N)={p+q-2\over N}.
}
\tag{7}
\]

This remains true if the exact zero difference is replaced by one.

There is also an exact collision law for an exterior prime \(\ell\). Write

\[
N=s\ell+r,
\qquad 0\le r<\ell.
\]

Then

\[
\Pr(\ell\mid K)={\lceil N/\ell\rceil\over N}.
\tag{8}
\]

If \(\widehat K=K\) for \(K>0\) and \(\widehat K=1\) for \(K=0\), then

\[
\Pr(\ell\mid\widehat K)
={\lfloor(N-1)/\ell\rfloor\over N}
<{1\over\ell}.
\tag{9}
\]

For independent \(K,L\),

\[
\boxed{
\Pr(K\ne L,\ K\equiv L\pmod\ell)
={\ell s(s-1)+2rs\over N^2}
\le {1\over\ell}.
}
\tag{10}
\]

There is also a history-wise exact form. If the past fixes
\(L\in\{0,\ldots,N-1\}\), let

\[
c_\ell(L)=
\#\{0\le z<N:z\equiv L\pmod\ell\}.
\]

A new conditionally uniform \(K\) satisfies

\[
\boxed{
\Pr(K\ne L,\ K\equiv L\pmod\ell\mid L)
={c_\ell(L)-1\over N}
\le {1\over\ell}.
}
\tag{11}
\]

Equations (5), (7), and (9)--(11) show that a fresh random lift gives the
same scale as a fresh uniform scalar. The order transcript does not amplify
its factor or marker incidence.

## 3. Meaning of a signed carry

Let \(r\in\{p,q\}\). Suppose

\[
a^E\equiv\sigma\pmod r,
\qquad
a^E\equiv\sigma+NC\pmod {N^2},
\]

and \(r\nmid E\). Then

\[
\boxed{
r\mid C
\quad\Longleftrightarrow\quad
a^E\equiv\sigma\pmod {r^2}.
}
\tag{12}
\]

Let \(m=\operatorname{ord}_r(a)\). The local order modulo \(r^2\) is
either \(m\) or \(rm\), and

\[
r\mid C
\quad\Longleftrightarrow\quad
\operatorname{ord}_{r^2}(a)=m.
\tag{13}
\]

Thus the carry is a real second-order return channel. A proper
\(\gcd(C,N)\) factors \(N\). But the uniform-lift law (5) shows that this
channel is exponentially sparse on balanced semiprimes. It does not, by
itself, add support from \(p\pm1\) or \(q\pm1\) to a P205/P208 exponent.

## 4. A canonical null witness

Take the canonical base

\[
a=N-1.
\]

For every even \(E\),

\[
(N-1)^E\equiv1-EN\pmod {N^2},
\]

so

\[
\boxed{K_0=-E\pmod N.}
\tag{14}
\]

In particular, for \(E=(N-1)W\),

\[
K_0=W\pmod N.
\tag{15}
\]

The base has order two in every hidden component. Every signed power screen
is global and gives only gcd \(1\) or \(N\). With \(W=1\), the complete
ordinary return is null and the canonical carry is also the useless value
\(1\). Therefore even a genuine global return does not force a useful
canonical carry.

## 5. Quadratic-torus affine lift law

Let

\[
\mathcal A_{N^2}=(\mathbb Z/N^2\mathbb Z)[w]/(w^2-D)
\]

with conjugation \(\overline{x+yw}=x-yw\), trace
\(\operatorname{Tr}\), and norm \(\operatorname{Nm}\). Let \(U\) be a
unit with

\[
\operatorname{Nm}(U)=1\pmod {N^2}.
\]

Use the same exponent condition \(\gcd(E,N)=1\).

Every exact norm-one lift of the same residue modulo \(N\) has the unique
form

\[
U_t=U(1+Ntw),
\qquad t\in\mathbb Z/N\mathbb Z.
\tag{16}
\]

Fix a public lift \(X\) of \(U^E\bmod N\). Define its normalized carry
\(C_t\in\mathcal A_N\) by

\[
U_t^E X^{-1}=1+NC_t\pmod {N^2}.
\tag{17}
\]

Then

\[
\boxed{
C_t=C_0+Etw.
}
\tag{18}
\]

Write \(C_t=c_{0,t}+c_{1,t}w\). If

\[
\operatorname{Nm}(X)=1+Nh\pmod {N^2},
\]

then exact norm one forces

\[
2c_{0,t}=-h\pmod N,
\tag{19}
\]

while \(c_{1,t}=c_{1,0}+Et\). Hence a uniform \(t\) makes the one
free tangent coordinate exactly uniform modulo \(N\), conditional on the
complete modulo-\(N\) torus transcript. Its direct-gcd and independent
collision probabilities are exactly (5), (7), and (9)--(11).

If the lift is not required to have exact norm one, the complete lift fibre
is

\[
U_{s,t}=U(1+N(s+tw)),
\]

and the normalized carry changes by \(E(s+tw)\). Both coordinates are
uniform when \(s,t\) are uniform.

## 6. Same-chain carries are affine, not independent

For the ordinary source, let

\[
a^E\equiv x+NK_E\pmod {N^2},
\qquad x=\langle a^E\rangle_N.
\]

For every \(m\ge1\), put

\[
x_m=\langle x^m\rangle_N,
\qquad
Q_m={x^m-x_m\over N}.
\]

Then

\[
\boxed{
K_{mE}=Q_m+mx^{m-1}K_E\pmod N.
}
\tag{20}
\]

Thus a Miller or repeated-squaring chain does not supply independent high
digits. Conditional on one carry, every later carry in the same
multiplicative chain is fixed by an affine formula.

For the torus source, choose one section \(S(y)\) from residues modulo
\(N\) to units modulo \(N^2\). Put \(X_E=S(U^E\bmod N)\) and

\[
U^E X_E^{-1}=1+NC_E.
\]

Define the public section cocycle \(Q_m\) by

\[
X_E^m X_{mE}^{-1}=1+NQ_m.
\]

Then

\[
\boxed{C_{mE}=Q_m+mC_E.}
\tag{21}
\]

## 7. Scoped quasipolynomial consequence

Take a bank of \(T\) fresh lift parameters. Require each new parameter to
be conditionally uniform after the complete prior transcript. Replace zero
carry values and exact-zero differences by one. A product of these positive
atoms and their positive powers can contain an exterior prime \(\ell\) only
if one of at most \(T+\binom T2\) atoms contains it. The history-wise laws
(9) and (11) therefore give

\[
\boxed{
\Pr(\ell\mid W_{\rm lift})
\le {T+\binom T2\over\ell}.
}
\tag{22}
\]

This bound is valid under adaptive choices of later bases and exponents,
provided each new lift parameter remains conditionally uniform and each
chosen exponent is a unit modulo \(N\).

On the F244 four-marker family, all four relevant marker primes are
\(2^{\Omega(n)}\). Therefore a numerical-quasipolynomial bank of these
fresh gauge carries and differences hits any marker with probability
\(2^{-\Omega(n)}\). Adding this bank to the F244 signed-power grammar does
not give inverse-quasipolynomial progress.

This consequence does not cover canonical carries, same-gauge nonlinear
functions, cross-base section identities, sums or determinants, Euclidean
quotients, retained exact relations, or a decoder that uses more than prime
support in a product word.

## Exact remaining gap

The surviving question is source-side and section-specific. One must prove
that a **canonical** high digit, or a nonlinear combination of canonical
high digits, has inverse-quasipolynomial divisibility or collision bias for
enough of one P205/P208 residual. The affine lift laws neither give nor
exclude such a theorem.
