# F83 — prime saturation has a complete deterministic support-two decoder

**Status:** proof-only candidate. No research computation was run. This is a
conditional decoder theorem for an explicit relation list, not a relation
source or a factoring algorithm.

## 1. Closest prior result and material difference

P66 gives a complete binary square-class decoder. P73/P74 identify the exact
closure and non-global-root gates after one feedback relation. Their
completeness uses the special fact that a field has only two square roots of
one.

The present result extends the decoder to every public prime
\(\ell=\operatorname{poly}(\log N)\). A basis alone is no longer complete,
but all combinations supported on at most two basis vectors are complete for
the exact identity-kernel gate. This opens a genuine odd-prime saturation
operation that the feedback proposal's \(2\)-saturation step omits.

## 2. Exact prime-saturation root map

Let

\[
N=pq
\]

for distinct odd primes. Let \(q_1,\ldots,q_s\) be pairwise-coprime positive
unit blocks, and let

\[
A_i=\prod_{j=1}^s q_j^{e_{ji}}\equiv1\pmod N,
\qquad
1\le i\le m,
\tag{1}
\]

be an explicit list with nonnegative integer exponents. Let \(E\) be the
\(s\times m\) exponent matrix. Fix a public prime \(\ell\), and compute

\[
V=\ker(E\bmod\ell)\le\mathbb F_\ell^m.
\]

For \(c\in V\), take coordinate representatives
\(c_i\in\{0,\ldots,\ell-1\}\), and define the exact integer and its
canonical modular residue by

\[
\widetilde R(c)
=
\prod_{j=1}^s
q_j^{\,(\sum_i e_{ji}c_i)/\ell},
\qquad
R(c)=[\widetilde R(c)]_N.
\tag{2}
\]

Every exponent in (2) is an integer. Moreover,

\[
\widetilde R(c)^\ell
\equiv
\prod_i A_i^{c_i}
\equiv1\pmod N.
\tag{3}
\]

### Theorem 1

The map

\[
\rho:V\longrightarrow
\mu_\ell(\mathbb F_p)\times\mu_\ell(\mathbb F_q),
\qquad
c\longmapsto(R(c)\bmod p,R(c)\bmod q)
\]

is a group homomorphism. For \(r\in\{p,q\}\), put

\[
K_r=\{c\in V:R(c)\equiv1\pmod r\}.
\]

Then \(K_r\) is either all of \(V\) or a hyperplane. For every \(c\in V\),

\[
\boxed{
1<\gcd(R(c)-1,N)<N
\iff
c\in K_p\mathbin\triangle K_q.
}
\tag{4}
\]

### Proof

For \(c,d\in V\), let \(e\) be their coordinatewise sum modulo \(\ell\), and
write

\[
c+d=e+\ell t
\]

over the integers. Comparing the exact block exponents in (2) gives

\[
\widetilde R(c)\widetilde R(d)
=
\widetilde R(e)\prod_i A_i^{t_i}.
\]

Reduction modulo \(N\) gives \(R(c)R(d)=R(e)\), so \(\rho\) is a
homomorphism. Each local image has order dividing the
prime \(\ell\), so it has order \(1\) or \(\ell\). Its kernel is accordingly
all of \(V\) or a codimension-one subspace. Finally, the gcd in (4) is proper
exactly when one local root, but not the other, is the identity.
\(\square\)

For uniform \(c\in V\), let \(d_p,d_q\in\{0,1\}\) be the two local map
ranks and let \(d\in\{0,1,2\}\) be their joint rank. The exact success
density is

\[
\boxed{
\Pr(c\in K_p\mathbin\triangle K_q)
=
\ell^{-d_p}+\ell^{-d_q}-2\ell^{-d}.
}
\tag{5}
\]

If the kernels differ, this is either

\[
1-\frac1\ell
\quad\text{or}\quad
\frac{2(\ell-1)}{\ell^2}.
\]

If the kernels agree, it is zero. In particular, a public polynomial-size
prime gives inverse-polynomial density whenever the gate is open.

## 3. Deterministic support-two completeness

Let

\[
b_1,\ldots,b_D
\]

be any public basis of \(V\). Define the menu

\[
\mathcal C
=
\{b_i:1\le i\le D\}
\cup
\{b_i+t b_j:1\le i<j\le D,\ t\in\mathbb F_\ell^\times\}.
\tag{6}
\]

### Theorem 2

The direct gcd tests on (6) are complete:

\[
\boxed{
K_p\ne K_q
\iff
\exists c\in\mathcal C:
1<\gcd(R(c)-1,N)<N.
}
\tag{7}
\]

The menu size is

\[
D+(\ell-1)\binom D2.
\]

### Proof

Choose hidden identifications of each nontrivial local root group with the
additive group \(\mathbb F_\ell\). The two local maps become linear
functionals

\[
\alpha,\beta:V\to\mathbb F_\ell,
\]

with the zero functional allowed. Write

\[
\alpha_i=\alpha(b_i),
\qquad
\beta_i=\beta(b_i).
\]

If one basis vector belongs to exactly one of the two kernels, it is already
in the first part of (6).

Otherwise \(\alpha_i=0\) exactly when \(\beta_i=0\). If the kernels still
differ, the two coefficient vectors are not scalar multiples. There are
indices \(i<j\) with

\[
\alpha_i\beta_j-\alpha_j\beta_i\ne0.
\]

The shared zero pattern makes all four displayed coefficients nonzero. Put

\[
t=-\alpha_i/\alpha_j\in\mathbb F_\ell^\times.
\]

Then

\[
\alpha(b_i+t b_j)=0,
\qquad
\beta(b_i+t b_j)\ne0.
\]

This menu element passes (4). Conversely, if the kernels agree, no element
of \(V\), and hence no menu element, can pass. \(\square\)

For \(\ell=2\), two nonzero coefficient vectors with the same support are
equal. The basis vectors alone are therefore complete, recovering the
special binary behavior behind P66.

## 4. Bit complexity

Gaussian elimination computes the basis of \(V\) in polynomial time.
For each menu vector, the integer block exponents in (2) are obtained by
matrix-vector multiplication and exact division by \(\ell\). The algorithm
computes \(R(c)\) directly modulo \(N\); it need not materialize the full
integer root.

If the relation presentation has total bit length \(L\) and
\(\ell=\operatorname{poly}(L+\log N)\), then:

- \(D\le m\le L\);
- the menu has \(O(\ell D^2)\) elements;
- every derived exponent has bit length polynomial in \(L+\log\ell\); and
- every modular power, product, and gcd has polynomial bit complexity.

Thus (6) gives a deterministic factor-free polynomial-time decoder for every
explicit polynomial-size prime-saturation state.

## 5. Odd-prime saturation is a real operation change

Let

\[
N=215=5\cdot43.
\]

The single canonical relation

\[
8\cdot27=216=1+N
\]

has gcd-free blocks \(2,3\) and exponent column

\[
\begin{pmatrix}3\\3\end{pmatrix}.
\]

Modulo \(2\), this column is nonzero, so the binary relation kernel is zero.
There is no nontrivial \(2\)-saturation dependency. The endpoint sign and
difference gcds are also trivial.

Modulo \(3\), the column is zero. Taking \(c=1\) gives the exact cube root

\[
R=2\cdot3=6,
\qquad
R^3=216\equiv1\pmod{215}.
\]

Its local labels differ:

\[
6\equiv1\pmod5,
\qquad
6\not\equiv1\pmod{43}.
\]

Therefore

\[
\boxed{\gcd(6-1,215)=5}.
\]

This fixed witness proves that odd-prime saturation can succeed when complete
\(2\)-saturation has no nonzero relation.

## 6. Exact remaining gap

The decoder is complete only for the identity-kernel gate
\(K_p\ne K_q\). Two nontrivial local root characters can differ by a nonzero
scalar while having the same kernel; then no relation in \(V\) has identity
in exactly one component, and the present gcd target is empty.

More importantly, the theorem does not manufacture a useful
\(\ell\)-saturation state. A general factoring algorithm still needs a
public polynomial relation source and a polynomial-size prime \(\ell\) for
which the two hidden kernels differ on every unresolved input with
inverse-polynomial probability.

The \(N=215\) witness is manufactured and its cube is publicly recognizable.
No novelty claim relative to classical congruence-of-powers methods is made
without a literature review. The theorem changes the exact decoder and
removes the restriction to \(2\)-saturation, but it proves no all-input
factoring algorithm.
