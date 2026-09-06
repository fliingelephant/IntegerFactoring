# F145 candidate statement — quasipolynomial finite-algebra source boundary

## Status and relation to prior work

This is a proof-only candidate. It is not a factoring algorithm. It has not
passed a hostile audit or a proof-blind reconstruction.

The closest general theorem is P40. Parts I and II specialize P40 to finite
algebras. They explain why nilpotents, different local splitting partitions,
and generic Krylov ranks do not change the low-degree probability bound.
Parts III--V study two ways to leave that model: a true local Frobenius map
and a succinct characteristic-scale power.

The closest source-specific results are P06--P09, P13, P17, and the F04
results P11, P14, P18, and P24. F145 does not retry a fixed low-degree
splitting test or the standard AKS error family. It gives a common
quasipolynomial boundary for arbitrary finite commutative algebras, generic
Krylov probes, monomial power maps, and low-order divided-power jets.

Throughout Parts I--IV, let

\[
N=pq
\]

for distinct primes \(p,q\), and put \(R=\mathbb Z/N\mathbb Z\). Let
\(n=\lceil\log_2(N+1)\rceil\).

## Part I — uniform nonunits in any finite commutative algebra

Let \(K=\mathbb F_r\). Let \(A\) be a finite-dimensional commutative
\(K\)-algebra of dimension \(d\). If \(J=\operatorname{Jac}(A)\), write

\[
A/J\simeq\prod_{i=1}^{s}\mathbb F_{r^{e_i}}.
\tag{1}
\]

Then a uniform \(a\in A\) has exact nonunit probability

\[
\alpha_r(A)
=1-\prod_{i=1}^{s}(1-r^{-e_i})
\le \sum_{i=1}^{s}r^{-e_i}
\le \frac d r.
\tag{2}
\]

Now let \(\mathcal A\) be a finite free commutative \(R\)-algebra of rank
\(d\), and let

\[
\mathcal A_r=\mathcal A\otimes_R\mathbb F_r
\qquad(r=p,q).
\]

For uniform \(a\in\mathcal A\), let

\[
D(a)=\det(m_a)\in R,
\]

where \(m_a\) is multiplication by \(a\). Then

\[
\Pr[1<\gcd(D(a),N)<N]
=\alpha_p+\alpha_q-2\alpha_p\alpha_q
\le d\left(\frac1p+\frac1q\right).
\tag{3}
\]

For \(M\) fresh uniform probes, including probes that are conditionally
fresh after an adaptive transcript, the probability that any determinant
gives a proper gcd is at most

\[
Md\left(\frac1p+\frac1q\right).
\tag{4}
\]

If \(M,d=2^{(\log n)^{O(1)}}\) and
\(\min(p,q)=2^{\Omega(n)}\), this probability is \(2^{-\Omega(n)}\).
Nilpotents do not increase the probability in (2).

## Part II — generic Krylov rank in a small finite etale algebra

Let \(A\) be a finite etale \(\mathbb F_r\)-algebra of dimension \(d<r\).
Then \(A\) is monogenic: there is \(b\in A\) with

\[
A=\mathbb F_r[b].
\tag{5}
\]

For \(a\in A\), let

\[
K(a)=[1,a,a^2,\ldots,a^{d-1}]
\tag{6}
\]

be the Krylov matrix in any fixed basis. For uniform \(a\in A\),

\[
\Pr[\operatorname{rank}K(a)<d]
\le \min\left(1,\frac{d(d-1)}r\right).
\tag{7}
\]

Suppose both reductions \(\mathcal A_p,\mathcal A_q\) of a rank-\(d\)
finite free \(R\)-algebra are etale and \(d<\min(p,q)\). Their
factor-degree partitions can be different. Nevertheless, for uniform
\(a\in\mathcal A\),

\[
\Pr[\operatorname{rank}K(a_p)\ne\operatorname{rank}K(a_q)]
\le d(d-1)\left(\frac1p+\frac1q\right).
\tag{8}
\]

Thus quasipolynomially many such probes still have total mismatch
probability \(2^{-\Omega(n)}\) on balanced semiprimes.

## Part III — the genuine local Frobenius is factor-bearing

Let \(f\in R[X]\) be monic of degree \(d\). Suppose \(f\bmod p\) and
\(f\bmod q\) are squarefree. Write their factor-degree partitions as

\[
\lambda_r=(e_{r,1},\ldots,e_{r,s_r})
\qquad(r=p,q).
\]

Let \(F_r\) be absolute Frobenius on

\[
A_r=\mathbb F_r[X]/(f),
\qquad F_r(x)=x^r,
\]

and let \(F=(F_p,F_q)\) be their CRT-glued \(R\)-linear endomorphism of
\(A=R[X]/(f)\). Then

\[
\chi_{F_r}(T)=H_{\lambda_r}(T)
:=\prod_{e\in\lambda_r}(T^e-1).
\tag{9}
\]

The map \(\lambda\mapsto H_\lambda\) is injective over the integers.
Assume

\[
\lambda_p\ne\lambda_q,
\qquad
p,q>2^{d+1}.
\tag{10}
\]

Given the matrix of the genuine glued map \(F\), one can extract \(p\) or
\(q\). The extraction uses a division-free characteristic polynomial,
enumeration of the integer partitions of \(d\), coefficient subtraction,
and gcds with \(N\). If \(d=(\log n)^{O(1)}\), its bit complexity is
quasipolynomial.

Conversely, given \(p,q\), one constructs \(F\) by computing
\(X^p\bmod(f,p)\), \(X^q\bmod(f,q)\), and CRT-gluing the coefficients.
Thus construction of the genuine glued Frobenius contains a factor
certificate on the explicit mismatch promise (10). The public power map
\(x\mapsto x^N\) is not this map in general.

## Part IV — monomial powers expose an order condition

Let \(K=\mathbb F_{r^e}\), let \(E\ge1\), and choose \(x\) uniformly in
\(K\). Then

\[
\#\{x\in K:x^E=x\}=1+\gcd(E-1,r^e-1),
\tag{11}
\]

and

\[
\Pr[x^E=x]
=\frac{1+\gcd(E-1,r^e-1)}{r^e}.
\tag{12}
\]

As a function on \(K\), the monomial map \(x\mapsto x^E\) is additive if
and only if

\[
E\equiv r^j\pmod{r^e-1}
\tag{13}
\]

for some \(0\le j<e\). It is the identity if and only if

\[
r^e-1\mid E-1.
\tag{14}
\]

For \(E=N^k\) in the base field,

\[
p-1\mid N^k-1
\quad\Longleftrightarrow\quad
p-1\mid q^k-1.
\tag{15}
\]

If \(q\) is a unit modulo \(p-1\), (15) is equivalent to

\[
\operatorname{ord}_{p-1}(q)\mid k.
\tag{16}
\]

If \(e\mid k\), then

\[
p^e-1\mid N^k-1
\quad\Longleftrightarrow\quad
p^e-1\mid q^k-1.
\tag{17}
\]

Equation (12) says that fixed-point density at least \(\delta\) requires

\[
\gcd(E-1,r^e-1)\ge \delta r^e-1.
\]

A local Frobenius power requires the exact congruence (13). For the public
family \(E=N^k\), full identity reduces to the cross-order conditions
(15)--(17). These identities do not prove that no adaptive
quasipolynomial menu can force a large asymmetric gcd or an asymmetric
Frobenius congruence.

## Part V — the first selective binomial jet is the least factor

Assume \(p<q\). In the Hasse expansion

\[
(X+T)^N-X^N
=\sum_{k=1}^{N}\binom Nk X^{N-k}T^k,
\tag{18}
\]

every coefficient before index \(p\) vanishes modulo all of \(N\):

\[
N\mid\binom Nk
\qquad(1\le k<p).
\tag{19}
\]

At the first exceptional index,

\[
\gcd\left(\binom Np,N\right)=q.
\tag{20}
\]

Therefore, on balanced semiprimes, a divided-power truncation through any
quasipolynomial **numerical order** is synchronized in the two CRT
components for all sufficiently large inputs. The first selective
coefficient is indexed by the unknown least factor.

This does not cover a sparse menu of large binary-encoded indices, a
compressed interval-coefficient algorithm, or a different succinct
high-degree invariant.

## Exact scope

F145 does not rule out:

1. a nonuniform or factor-correlated algebra-element source;
2. same-sample adaptive polynomials outside the fresh-uniform model;
3. a joint decoder that uses typical nonzero values;
4. a succinct nonmonomial high-degree map;
5. an adaptive exponent menu with an asymmetric order-hitting theorem;
6. a compressed evaluator for large Hasse-index ranges; or
7. finite algebras of characteristic-scale rank; or
8. intermediate elimination entries or matrix invariants other than the
   final Krylov rank.

F145 proves that changing the runtime target from polynomial to
quasipolynomial does not rescue uniform nonunit sampling, generic Krylov
rank sampling, or low-order characteristic jets on balanced semiprimes. It
also shows the exact hidden congruence that a monomial replacement for the
unknown local Frobenius must satisfy; it does not prove that no menu can
satisfy it.
