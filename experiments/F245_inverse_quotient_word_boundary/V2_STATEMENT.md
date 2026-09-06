# F245 V2 candidate — fresh inverse quotients and their differences miss four shifted markers

## Status and exact scope

This is a self-contained proof-only boundary for one restricted Las Vegas
grammar.  It is not an all-input factoring algorithm and not a lower bound
against biased, dependent, or nonlinear integer sources.

Let

\[
N=pq,
\qquad
n=\lceil\log_2(N+1)\rceil,
\]

where `p` and `q` are distinct odd primes.  Put

\[
\Delta_N=\max_{1\le m<N^2}\tau(m).
\]

For a canonical unit \(u\in\{1,\ldots,N-1\}\), let \(v\) be its least
positive inverse modulo \(N\), and define

\[
K(u)={uv-1\over N}\in\{0,\ldots,N-1\},
\qquad
\widehat K(u)=\begin{cases}K(u),&K(u)>0,\\1,&K(u)=0.\end{cases}
\]

## 1. Exact inverse-quotient bounds

If \(U\) is uniform on the canonical units modulo \(N\), every exact value
of \(K(U)\) has probability at most

\[
{\Delta_N\over\varphi(N)},
\]

and every exact value of \(\widehat K(U)\) has probability at most

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

For independent copies \(K_i,K_j\), put

\[
\Gamma_{ij}=\begin{cases}|K_i-K_j|,&K_i\ne K_j,\\1,&K_i=K_j.\end{cases}
\]

Then

\[
\Pr(\ell\mid\widehat K_i)\le\beta_{N,\ell},
\qquad
\boxed{\Pr(\ell\mid\Gamma_{ij})\le\beta_{N,\ell}.}
\tag{2}
\]

These inequalities remain valid after conditioning on the complete prior
transcript whenever each new seed is exactly uniform on the canonical units
given that transcript.

## 2. Complete adaptive bank

Take at most \(Q(n)\) fresh conditionally uniform inverse seeds.  After the
complete transcript is known, select any subcollection of the positive
values \(\widehat K_i\) and the positive unequal-value differences
\(\Gamma_{ij}\), and give the selected nonzero factors arbitrary positive
integer exponents.  If their product is \(W_{\rm iq}\), then

\[
\boxed{
\Pr(\ell\mid W_{\rm iq})
\le
\left(Q(n)+{Q(n)\choose2}\right)\beta_{N,\ell}.
}
\tag{3}
\]

The selection and the stopping rule can be adaptive.  The public envelope
\(Q(n)\) is fixed before the input and does not depend on a hidden factor.

## 3. Exact marker and torus interfaces used below

The following statements make the cross-family interface explicit.

There is an absolute constant \(c>0\) and an infinite family of distinct
odd semiprimes \(N=pq\) with four distinct primes

\[
\lambda_+,\lambda_-,\rho_+,\rho_->2^{cn}
\tag{4}
\]

such that, for \(a,b\in\{+1,-1\}\),

\[
\lambda_a\mid p-a,
\qquad
\rho_b\mid q-b,
\tag{5}
\]

\[
\operatorname{ord}_{\lambda_a}(q)=\lambda_a-1,
\qquad
\operatorname{ord}_{\rho_b}(p)=\rho_b-1,
\tag{6}
\]

and

\[
\gcd(p-1,q-1)=2,
\quad
\gcd(p-1,q+1)=12,
\quad
\gcd(p+1,q-1)=2,
\quad
\gcd(p+1,q+1)=2.
\tag{7}
\]

Here is the unconditional construction interface.  Choose the four marker
primes in comparable intervals and choose primitive roots modulo them.  Use
one reduced CRT class to choose by Linnik a prime \(p\) satisfying

\[
p\equiv13\pmod {24},
\quad p\equiv+1\pmod{\lambda_+},
\quad p\equiv-1\pmod{\lambda_-},
\]

with \(p\) primitive modulo both \(\rho_+\) and \(\rho_-\).  After this
\(p\) is fixed, factor

\[
p^2-1=2^3 3^e\prod_{s\ge5}s^{e_s}.
\]

Use a second reduced CRT class to choose by Linnik a prime \(q\) satisfying

\[
q\equiv3\pmod8,
\qquad
q\equiv2\pmod {3^{\max(e,2)}},
\qquad
q\equiv\pm1\pmod{\rho_\pm},
\]

and, for every \(s^{e_s}\parallel p^2-1\) with \(s\ge5\), choose
\(q\bmod s^{e_s}\) to be a unit whose reduction is neither sign.  At
\(s=\lambda_+\) or \(\lambda_-\), choose it to be a primitive root.
The \(\rho\)-markers do not divide \(p^2-1\), so these moduli are pairwise
coprime.  This gives (5)--(7) and in fact
\(\gcd(p^2-1,q^2-1)=24\).  The uniform polynomial bound in Linnik's
theorem, applied to both displayed moduli, makes every marker exceed
\(2^{cn}\) for one absolute \(c>0\).

For every fixed numerical-quasipolynomial function \(Q\), every sufficiently
large member of this family has the following signed-power property.  If

\[
W_{\rm sp}=\prod_{j=1}^{s}|N^{k_j}-\sigma_j|^{e_j},
\qquad
k_j,e_j\ge1,
\quad
\sigma_j\in\{+1,-1\},
\tag{8}
\]

is nonzero and has binary length at most \(Q(n)\), then

\[
\gcd(W_{\rm sp},\lambda_+\lambda_-\rho_+\rho_-)=1.
\tag{9}
\]

Indeed, marker divisibility of one factor in (8) implies
\(q^{2k_j}=1\) or \(p^{2k_j}=1\) modulo that marker.  Equation (6) then
forces \(k_j\ge(\ell-1)/2\), so that single factor already has exponential
binary length.

For completeness, the clean quadratic-torus interface is the following.
In orientation \((a,b)\), the two local cyclic tori have orders

\[
m_p=p-a,
\qquad
m_q=q-b.
\]

A factor-free Hilbert--90 sample, conditional on its public coefficient and
norm gcd screens being clean, gives independent uniform points in these two
cyclic groups.  For a public exponent \(E\), the local return probabilities
are exactly

\[
{\gcd(E,m_p)\over m_p},
\qquad
{\gcd(E,m_q)\over m_q}.
\tag{10}
\]

Every factor produced by the clean identity screens or the associated
two-primary Miller chain requires at least one local return under \(E\).
Hence its probability is at most the sum in (10).  The public nonclean norm
screen has factor probability below \(2/p+2/q\) per coefficient pair.
Every exact order certified as common to both local groups divides
\(\gcd(m_p,m_q)\).  Thus (7) makes the lcm of all common orders accumulated
over all four orientations divide \(12\).

## 4. Infinite obstruction after the square baseline

The maximum-order divisor estimate gives

\[
\Delta_N=2^{o(n)}.
\tag{11}
\]

For every fixed numerical-QP \(Q\), equations (1)--(4) give

\[
\boxed{
\Pr\!\left(
\gcd(W_{\rm iq},\lambda_+\lambda_-\rho_+\rho_-)>1
\right)=2^{-\Omega(n)}.
}
\tag{12}
\]

With probability \(1-2^{-\Omega(n)}\), the combined word

\[
W=(N^2-1)^n W_{\rm sp}W_{\rm iq}
\tag{13}
\]

misses all four markers.  In orientation \((a,b)\), use the public base
exponent \(N-ab\) and word \(W\).  By (7), neither marker divides the base
exponent.  The two residual local orders are therefore still divisible by
\(\lambda_a\) and \(\rho_b\).  Equation (10) bounds one clean powered trial
by

\[
{1\over\lambda_a}+{1\over\rho_b}=2^{-\Omega(n)}.
\tag{14}
\]

The nonclean screen, any numerical-QP number of trials, and exact
common-order accumulation preserve an exponential upper bound.  Thus the
restricted combination

\[
\text{square baseline}
+\text{signed powers}
+\text{fresh uniform inverse quotients/differences}
+\text{common-order lcm}
\]

does not have inverse-QP progress on this infinite family.

This also excludes an expected-QP Las Vegas algorithm confined to this
grammar.  If its expected running time were at most \(Q(n)\), Markov's
inequality would make it finish within \(2Q(n)\) time with probability at
least one half.  The truncated transcript has a numerical-QP number of
seeds and trials, whereas (12)--(14) make its verified-factor probability
exponentially small.

## 5. Hilbert--90 carries are nonlinear inverse-quotient transforms

Let \(w^2=D\), take public integers \(a,b\), and put

\[
g=a^2-Db^2,
\qquad
A=a^2+Db^2,
\qquad
B=2ab.
\]

Assume \(g\ne0\) and \(\gcd(g,N)=1\).  Let
\(v\in\{1,\ldots,N-1\}\) be the inverse of \(g\bmod N\), and set

\[
X=\langle Av\rangle_N,
\qquad
Y=\langle Bv\rangle_N,
\]

\[
\widetilde d={gv-1\over N},
\qquad
q_A={Av-X\over N},
\qquad
q_B={Bv-Y\over N}.
\]

Then the canonical coordinate carries are

\[
\boxed{
k={gX-A\over N}=A\widetilde d-gq_A,
\qquad
l={gY-B\over N}=B\widetilde d-gq_B.
}
\tag{15}
\]

The canonical norm carry is

\[
\boxed{
{X^2-DY^2-1\over N}
={2(Ak-DBl)+N(k^2-Dl^2)\over g^2}.
}
\tag{16}
\]

Equations (15)--(16) are exact for signed or noncanonical \(g\).  They do
not put the nonlinear right-hand sides inside the probability grammar of
(3).

## Exact remaining gap

Fresh uniform inverse seeds are too diffuse.  This theorem does not cover a
history-dependent nonuniform seed, inverse-quotient descent, canonical
feedback, cross-coordinate determinants, norm carries, higher quotient
digits, or a decoder that uses the full relation transcript without first
placing a marker in a product word.
