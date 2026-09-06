# F245 candidate — fresh inverse quotients and their differences miss the four shifted markers

## Status and scope

This is a proof-only candidate. It combines the exact inverse-quotient law
with the F244 ordinary--torus marker family. It is a Las Vegas boundary for
fresh uniform inverse seeds, their quotient values, their pairwise
differences, signed powers, and accumulated common orders. It is not an
all-input factoring algorithm or a lower bound against biased, dependent, or
nonlinear integer sources.

Let

\[
N=pq
\]

be a product of distinct odd primes and put

\[
n=\lceil\log_2(N+1)\rceil,
\qquad
\Delta_N=\max_{1\le m<N^2}\tau(m).
\]

For a canonical unit (u\in\{1,\ldots,N-1\}), let (v) be its least
positive inverse modulo (N) and define

\[
K(u)={uv-1\over N}\in\{0,\ldots,N-1\}.
\]

Replace the zero value by one:

\[
\widehat K(u)=\begin{cases}K(u),&K(u)>0,\\1,&K(u)=0.\end{cases}
\]

## 1. Exact residue-mass bound

If (U) is uniform on the canonical units modulo (N), then every exact
value of (K(U)) has probability at most

\[
{\Delta_N\over\varphi(N)}.
\]

Consequently every exact value of \(\widehat K(U)\) has probability at most

\[
{2\Delta_N\over\varphi(N)}.
\]

For every prime \(\ell<N\), every residue class modulo \(\ell\) therefore
has mass at most

\[
\boxed{
\beta_{N,\ell}
={2\lceil N/\ell\rceil\Delta_N\over\varphi(N)}
<{8\Delta_N\over\ell}.
}
\tag{1}
\]

For independent copies (K_i,K_j), put

\[
\Gamma_{ij}=\begin{cases}|K_i-K_j|,&K_i\ne K_j,\\1,&K_i=K_j.
\end{cases}
\]

Then

\[
\Pr(\ell\mid\widehat K_i)\le\beta_{N,\ell},
\qquad
\boxed{\Pr(\ell\mid\Gamma_{ij})\le\beta_{N,\ell}.}
\tag{2}
\]

The same bounds hold history-wise when each new seed is conditionally uniform
after the complete prior transcript is fixed.

## 2. Adaptive bank bound

Take at most (Q(n)) fresh conditionally uniform inverse seeds. After seeing
the complete transcript, select any subcollection of their positive quotient
values and pairwise unequal-value differences, with arbitrary positive
exponents. If (W_{\rm iq}) is the resulting product, then

\[
\boxed{
\Pr(\ell\mid W_{\rm iq})
\le
\left(Q(n)+{Q(n)\choose2}\right)\beta_{N,\ell}.
}
\tag{3}
\]

Selection can be adaptive. Equation (3) only uses the fact that a prime can
divide the final positive product only after it divides one member of the
complete available bank.

## 3. Infinite obstruction after the square baseline

On the unconditional F244 family there are four distinct marker primes

\[
\lambda_+,\lambda_-,\rho_+,\rho_->2^{cn}
\]

for one absolute (c>0), one in each of (p-1,p+1,q-1,q+1). Every
numerical-QP-bit signed-power word

\[
W_{\rm sp}=\prod_j|N^{k_j}-\sigma_j|^{e_j},
\qquad\sigma_j\in\{\pm1\},
\]

misses all four markers. The maximum-order divisor estimate gives

\[
\Delta_N=2^{o(n)}.
\]

Therefore, for every fixed numerical-QP (Q), a bank of at most (Q(n))
fresh inverse quotients satisfies

\[
\boxed{
\Pr\!\left(
\gcd(W_{\rm iq},
\lambda_+\lambda_-\rho_+\rho_-)>1
\right)=2^{-\Omega(n)}.
}
\tag{4}
\]

With probability (1-2^{-\Omega(n)}), the combined word

\[
W=(N^2-1)^nW_{\rm sp}W_{\rm iq}
\]

leaves one exponential marker on each hidden side of every P208 orientation.
Every clean powered trial then has exponentially small success. The F244
family also has total shifted common-order capacity (12), so accumulating
any number of exact common orders does not repair the failure.

Thus the natural combination

\[
\text{square baseline}
+\text{signed powers}
+\text{fresh uniform inverse quotients/differences}
+\text{common-order lcm}
\]

does not give inverse-QP Las Vegas progress on this family.

## 4. Hilbert--90 coordinate carries reduce to inverse-quotient data

Let (w^2=D), take public integers (a,b), and put

\[
g=a^2-Db^2,
\qquad A=a^2+Db^2,
\qquad B=2ab.
\]

Assume (g\ne0) and \(\gcd(g,N)=1\). Let (v\in\{1,\ldots,N-1\}) be
the inverse of (g\bmod N), and let

\[
X=\langle Av\rangle_N,qquad Y=\langle Bv\rangle_N.
\]

Define the exact public quotients

\[
\widetilde d={gv-1\over N},
\qquad q_A={Av-X\over N},
\qquad q_B={Bv-Y\over N}.
\]

Then the two canonical coordinate carries are

\[
\boxed{
k={gX-A\over N}=A\widetilde d-gq_A,
\qquad
l={gY-B\over N}=B\widetilde d-gq_B.
}
\tag{5}
\]

The canonical norm carry is

\[
\boxed{
{X^2-DY^2-1\over N}
={2(Ak-DBl)+N(k^2-Dl^2)\over g^2}.
}
\tag{6}
\]

Thus the obvious Hilbert--90 quotient and norm carries are explicit
nonlinear transforms of one modular-inverse quotient transcript. Equations
(5)--(6) do **not** put these transforms inside the probabilistic grammar of
(3). They identify the next live source precisely: a biased norm law or a
nonlinear transform of the inverse-quotient transcript with an all-input
inverse-QP marker-incidence theorem.

## Exact remaining gap

Fresh uniform inverse seeds are too diffuse. The theorem does not cover a
history-dependent nonuniform seed, inverse-quotient descent, canonical
feedback, cross-coordinate determinants, norm carries, higher quotient
digits, or a decoder that uses the full relation transcript without first
placing a marker in a product word.
