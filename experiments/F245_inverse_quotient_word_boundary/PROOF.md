# Proof of the F245 inverse-quotient word boundary

## 1. Exact atoms and residue classes

For (0\le k<N), the inverse-quotient fibre is

\[
K^{-1}(k)=\{u:k<u<N,\ u\mid Nk+1\}.
\tag{7}
\]

Every member is a divisor of (Nk+1<N^2). Hence

\[
|K^{-1}(k)|\le\tau(Nk+1)\le\Delta_N.
\]

Uniformity of (U) on the \(\varphi(N)\) canonical units gives

\[
\Pr(K(U)=k)\le{\Delta_N\over\varphi(N)}.
\tag{8}
\]

Replacing zero by one merges at most two exact atoms, proving the factor two
for \(\widehat K\).

There are at most \(\lceil N/\ell\rceil\) integers in
\(\{0,\ldots,N-1\}\) in one residue class modulo \(\ell\). Therefore its
mass under \(\widehat K\) is at most

\[
{2\lceil N/\ell\rceil\Delta_N\over\varphi(N)}.
\]

For distinct odd primes (p,q),

\[
{N\over\varphi(N)}={p\over p-1}{q\over q-1}\le{15\over8}.
\]

Since \(\ell<N\), \(\lceil N/\ell\rceil<2N/\ell\). Thus the last display
is less than (8\Delta_N/\ell), proving (1).

For two independent quotient values, let \(\rho_r\) be the mass of residue
class (r\bmod\ell). Then

\[
\Pr(K_i\equiv K_j\pmod\ell)=\sum_r\rho_r^2
\le\max_r\rho_r\le\beta_{N,\ell}.
\]

Deleting exact equality by replacing its zero difference with one can only
decrease the event for odd \(\ell\). This proves (2). Conditional on an
arbitrary past, a fresh conditionally uniform unit has the same fixed law,
so the same argument is history-wise.

## 2. Complete-bank union bound

If \(\ell\) divides a positive product, it divides at least one factor.
There are at most (Q) quotient factors and \({Q\choose2}\) distinct-pair
difference factors in the complete available bank. A union bound using (2)
proves (3). The later selection rule and the positive exponents do not alter
this necessary event.

## 3. The marker family

F244 supplies an absolute (c>0), infinitely many distinct odd semiprimes,
and four markers greater than (2^{cn}). It also proves pathwise that every
numerical-QP-bit signed-power word misses them and that all shifted common
orders have lcm dividing (12).

The standard maximal-order estimate for the divisor function is

\[
\max_{m\le x}\log\tau(m)=O\!\left({\log x\over\log\log x}\right).
\]

At (x=N^2), this gives

\[
\Delta_N=2^{O(n/\log n)}=2^{o(n)}.
\]

Every numerical-QP count satisfies (Q(n)=2^{o(n)}). Applying (3) to each
of the four markers and taking one more union bound proves (4).

When no marker is captured, the square baseline and signed-power factors
also miss the relevant marker. In orientation ((a,b)), \(\lambda_a\)
remains in the (p)-side residual and \(\rho_b\) remains in the (q)-side
residual. The clean P208 success probability is at most the sum of the two
local return probabilities, hence at most

\[
{1\over\lambda_a}+{1\over\rho_b}=2^{-\Omega(n)}.
\]

Numerical-QP repetition preserves an exponential upper bound. Accumulated
common orders divide (12) and do not absorb a marker. This proves the
combined scoped obstruction.

## 4. Hilbert--90 carry algebra

The Hilbert--90 quotient of (z=a+bw) is

\[
{z\over\bar z}={A+Bw\over g}.
\]

The definitions of (X,Y,q_A,q_B) give

\[
X=Av-Nq_A,qquad Y=Bv-Nq_B.
\]

Also (gv-1=N\widetilde d). Therefore

\[
\begin{aligned}
gX-A
&=A(gv-1)-gNq_A
=N(A\widetilde d-gq_A),\\
gY-B
&=B(gv-1)-gNq_B
=N(B\widetilde d-gq_B),
\end{aligned}
\]

which proves (5).

Since

\[
A^2-DB^2=(a^2-Db^2)^2=g^2,
\]

substitute (gX=A+Nk) and (gY=B+Nl):

\[
g^2(X^2-DY^2)
=g^2+2N(Ak-DBl)+N^2(k^2-Dl^2).
\]

Subtract (g^2), divide by (Ng^2), and obtain (6). Every quantity in
these formulas is public and has polynomial bit cost in its explicit input
encoding. The formulas are reductions, not distributional bounds for their
nonlinear right-hand sides.
