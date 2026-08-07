# PASS

The SHA-256 digest of the reconstruction statement is

~~~text
7868d3f7c31a558bed9d0e2afd129a593658285de07aefff1208e40e0ddc64b4
~~~

It matches the pinned digest. Every theorem claim is correct. The fixed
\(N=215\) certificate is also arithmetically correct, with the stated scope
defect.

## 1. Integral exponents and the root identity

Let \(c\in V\), with the specified representatives
\(0\le c_i<\ell\). Since \(Ec=0\) over \(\mathbb F_\ell\), every row obeys

\[
\sum_i e_{ji}c_i\equiv0\pmod\ell.
\]

Thus every exponent

\[
n_j(c)=\frac{\sum_i e_{ji}c_i}{\ell}
\]

is a nonnegative integer. Moreover,

\[
\begin{aligned}
\widetilde R(c)^\ell
&=\prod_jq_j^{\sum_i e_{ji}c_i}\\
&=\prod_i\left(\prod_jq_j^{e_{ji}}\right)^{c_i}\\
&=\prod_iA_i^{c_i}
\equiv1\pmod N.
\end{aligned}
\]

Consequently \(R(c)^\ell\equiv1\pmod N\).

## 2. Homomorphism despite canonical representatives

Take \(c,c'\in V\), and let \(d\) be the canonical representative vector of
\(c+c'\) in \(\mathbb F_\ell^m\). For each coordinate there is
\(k_i\in\{0,1\}\) such that

\[
d_i=c_i+c_i'-\ell k_i.
\]

For every row \(j\),

\[
n_j(d)=n_j(c)+n_j(c')-\sum_i e_{ji}k_i.
\]

Rearranging the corresponding integer products gives

\[
\widetilde R(c)\widetilde R(c')
=
\widetilde R(d)\prod_iA_i^{k_i}.
\]

Every \(A_i\equiv1\pmod N\), so

\[
R(c+c')=R(c)R(c')\quad\text{in }(\mathbb Z/N\mathbb Z)^\times.
\]

Claim 1 shows that both local components are \(\ell\)-th roots of unity.
Therefore

\[
\rho:V\longrightarrow
\mu_\ell(\mathbb F_p)\times\mu_\ell(\mathbb F_q)
\]

is a group homomorphism. The wraparound correction from canonical
coordinates is exactly a product of the known relations, so it disappears
modulo \(N\).

## 3. Local kernels, including characteristic \(\ell\)

Let \(\rho_r\) be the \(r\)-component of \(\rho\). Its image is a subgroup
of \(\mu_\ell(\mathbb F_r)\).

If \(r\ne\ell\), this root group has order either \(1\) or \(\ell\), because
\(\ell\) is prime. Hence the image of \(\rho_r\) has order \(1\) or
\(\ell\). Its kernel \(K_r\) is correspondingly all of \(V\) or has index
\(\ell\), which makes it a hyperplane over \(\mathbb F_\ell\).

If \(r=\ell\), then in characteristic \(\ell\),

\[
X^\ell-1=(X-1)^\ell.
\]

Thus \(\mu_\ell(\mathbb F_\ell)=\{1\}\). The local map is zero and
\(K_r=V\). This covers the exceptional characteristic explicitly.

Equivalently, after choosing a generator when the root group is nontrivial,
each local map is an \(\mathbb F_\ell\)-linear functional, possibly the zero
functional.

## 4. Exact hidden-kernel gate

The root \(R(c)\) is a unit. Since \(N=pq\) with distinct primes,

\[
1<\gcd(R(c)-1,N)<N
\]

holds exactly when \(R(c)\) is \(1\) modulo one, but not both, of \(p,q\).
By the definitions of \(K_p,K_q\), this is exactly

\[
c\in K_p\mathbin\triangle K_q.
\]

The test itself is public even though this characterization names the hidden
prime factors.

## 5. Uniform density

Let \(D=\dim_{\mathbb F_\ell}V\). A linear map of rank \(d_p\) has a kernel
of size

\[
|K_p|=\ell^{D-d_p}=|V|\ell^{-d_p},
\]

and similarly for \(K_q\). The intersection \(K_p\cap K_q\) is the kernel
of the joint local map, so

\[
|K_p\cap K_q|=|V|\ell^{-d}.
\]

The symmetric-difference identity therefore gives

\[
\begin{aligned}
\Pr(c\in K_p\mathbin\triangle K_q)
&=\frac{|K_p|+|K_q|-2|K_p\cap K_q|}{|V|}\\
&=\ell^{-d_p}+\ell^{-d_q}-2\ell^{-d}.
\end{aligned}
\]

If the kernels differ, there are only two cases.

* One local functional is zero and the other is nonzero. The ranks are
  \(0,1,1\), and the density is
  \(1+1/\ell-2/\ell=1-1/\ell\).
* Both are nonzero. Different kernels mean the functionals are not
  proportional, so their joint rank is \(2\). The density is
  \(2/\ell-2/\ell^2=2(\ell-1)/\ell^2\).

The second case automatically requires \(D\ge2\).

## 6. Deterministic menu completeness

Identify the two local maps with linear functionals

\[
f,g:V\longrightarrow\mathbb F_\ell,
\]

allowing either functional to be zero. Their kernels are \(K_p,K_q\).

If a menu element gives a proper gcd, it lies in the symmetric difference,
so \(K_p\ne K_q\). This proves the easy implication.

Conversely, assume \(K_p\ne K_q\). If a basis vector \(b_i\) already
satisfies exactly one of \(f(b_i),g(b_i)=0\), it is the required menu
element.

Suppose no basis vector does this. Then for every \(i\),

\[
f(b_i)=0\iff g(b_i)=0. \tag{1}
\]

If one functional were zero, (1) would force the other to be zero, contrary
to the different-kernel assumption. Thus both are nonzero. On their common
nonzero coordinate support, put

\[
\lambda_i=\frac{f(b_i)}{g(b_i)}.
\]

If all \(\lambda_i\) were equal, then \(f\) and \(g\) would be proportional
on the basis and hence on all of \(V\). Their kernels would be equal. Thus
there are indices \(i<j\) with \(\lambda_i\ne\lambda_j\). Define

\[
t=-\frac{f(b_i)}{f(b_j)}\in\mathbb F_\ell^\times.
\]

Then

\[
f(b_i+t b_j)=0,
\]

while

\[
g(b_i+t b_j)
=g(b_i)-\frac{f(b_i)}{f(b_j)}g(b_j)\ne0
\]

because the two ratios differ. This menu element lies in
\(K_p\mathbin\triangle K_q\), and the public gcd returns a proper factor.
The equivalence follows.

### Edge cases

If both functionals are zero, both kernels are \(V\), and no vector can
work. If exactly one is zero, some basis vector has a nonzero value under
the other and works immediately.

If both are nonzero and proportional, they have the same identity kernel.
No vector, in the menu or outside it, lies in the symmetric difference.
This remains true when the two characters take different nonidentity values.

If \(D=0\), then \(V=\{0\}\), both maps are zero, both kernels agree, and
\(\mathcal C=\varnothing\). Both sides of the completeness equivalence are
false.

If \(D=1\), every two nonzero functionals are proportional. Different
kernels can occur only when exactly one functional is zero. The sole basis
vector then works. The pair part of the menu is empty.

### Distinctness and exact menu size

In basis coordinates, \(b_i\) has support \(\{i\}\), while
\(b_i+t b_j\), with \(t\ne0\), has support \(\{i,j\}\). Hence no pair
element equals a basis vector. Two pair elements with different index pairs
have different support. For the same ordered pair \(i<j\), their
\(b_j\)-coefficients distinguish different values of \(t\). All menu
elements are therefore distinct, and

\[
|\mathcal C|
=D+(\ell-1)\binom D2.
\]

### The binary case

Over \(\mathbb F_2\), the only nonzero scalar is \(1\). Two nonzero
functionals have the same kernel exactly when they are equal. If
\(K_p\ne K_q\), the coordinate vectors of \(f\) and \(g\) in the public
basis therefore differ. Some basis coordinate has one value \(0\) and the
other value \(1\). That basis vector alone gives a proper gcd. Thus for
\(\ell=2\), basis vectors are a complete menu; pair sums are unnecessary.

## 7. Deterministic bit complexity and public inputs

Let the total explicit relation presentation have bit length \(L\), and
assume the numerical value of \(\ell\) is polynomial in
\(L+\log N\). The numerical assumption is important because the menu has a
factor linear in \(\ell\).

Gaussian elimination on \(E\bmod\ell\) uses polynomially many field
operations on \(O(\log\ell)\)-bit values. It produces a public basis with
\(D\le m\le L\). The menu has

\[
O(\ell D^2)
\]

elements, hence polynomially many under the hypothesis.

For each menu vector, convert its coordinates to
\(\{0,\ldots,\ell-1\}\), and compute

\[
n_j(c)=\frac{\sum_i e_{ji}c_i}{\ell}
\]

by exact integer division. The numerator bit lengths are polynomial in the
input length. Repeated squaring computes

\[
R(c)=\prod_jq_j^{n_j(c)}\bmod N
\]

in polynomial time, and Euclid's algorithm computes
\(\gcd(R(c)-1,N)\). Multiplying these costs by the polynomial menu size is
still polynomial.

The executable algorithm uses only \(N,\ell\), the public integers
\(q_j\), and the public exponent matrix \(E\). It neither knows nor uses
\(p,q\), the local characters, or their kernels.

## 8. Fixed operation-separation certificate

The arithmetic starts with

\[
5\cdot43=215,
\qquad
8\cdot27=216=1+215.
\]

Both \(5\) and \(43\) are prime. With public blocks \(2,3\), the relation is

\[
2^3 3^3\equiv1\pmod{215},
\]

so its exponent matrix is the single column

\[
E=\begin{pmatrix}3\\3\end{pmatrix}.
\]

Modulo \(2\), this column becomes \((1,1)^T\). The map
\(\mathbb F_2\to\mathbb F_2^2\) sends \(c\) to \((c,c)\), so its kernel is
\(\{0\}\). There is no nonzero binary saturation relation.

The individual endpoint sign tests and the raw endpoint difference are all
trivial:

\[
\begin{aligned}
\gcd(8-1,215)&=\gcd(7,215)=1,\\
\gcd(8+1,215)&=\gcd(9,215)=1,\\
\gcd(27-1,215)&=\gcd(26,215)=1,\\
\gcd(27+1,215)&=\gcd(28,215)=1,\\
\gcd(27-8,215)&=\gcd(19,215)=1.
\end{aligned}
\]

Modulo \(3\), the exponent column is zero, so
\(V=\mathbb F_3\). For \(c=1\), each divided exponent is \(1\), and hence

\[
R=2\cdot3=6.
\]

Then

\[
R^3=216\equiv1\pmod{215},
\qquad
\gcd(R-1,215)=\gcd(5,215)=5.
\]

The hidden-kernel picture is consistent: modulo \(5\), \(6\equiv1\), so the
local kernel is all of \(V\); modulo \(43\), \(6\) has order \(3\), so the
local kernel is \(\{0\}\).

The promised scope defect is real:

\[
\gcd(8+27,215)=\gcd(35,215)=5.
\]

Thus this fixed witness separates odd-prime saturation from the nonzero
binary relation space, and also from the listed individual sign and
difference tests. It does not separate saturation from every broader
endpoint screen, because the raw endpoint sum already factors \(N\).

## 9. Scope

The theorem is a factor-free, deterministic polynomial decoder conditional
on a supplied explicit relation state and on \(K_p\ne K_q\). Its executable
steps use no hidden factor. The theorem does not construct a relation state
with asymmetric local identity kernels, guarantee a useful prime
\(\ell\) on every input, or give a density or source law for such states.

Proportional nonzero local characters have the same identity kernel. They
therefore remain invisible to this positive-sign decoder even if their
nonidentity phases differ. Other operations can behave differently, but
they are outside this theorem.

No claim here proves literature novelty, a computational lower bound, or a
general factoring algorithm.
