# F260 algebra — exact integer-source scores

This file fixes the exact scores used by the F260 discovery search.  Hidden
factors are diagnostic labels only.  Every candidate integer and every
operation that constructs it is a function of the public input `N`.

## Completely factored annihilators

Let `N=pq` with distinct odd primes.  Let

\[
A=\prod_\ell \ell^{e_\ell}
\]

be a public, completely factored exponent.  For a uniform unit `a mod N`,
the local return probabilities are

\[
\alpha_p={\gcd(A,p-1)\over p-1},\qquad
\alpha_q={\gcd(A,q-1)\over q-1}.
\]

They are independent.  Thus a direct identity gcd is proper with exact
probability

\[
\boxed{\alpha_p+\alpha_q-2\alpha_p\alpha_q}.                 \tag{1}
\]

On the simultaneous-return branch, fix `ell^e || A` and put

\[
f_i=\min(e,v_\ell(i-1)),\qquad i\in\{p,q\}.
\]

If `T_i` is the `ell`-adic exponent of the order of the returned local
element, then

\[
\Pr(T_i=0)=\ell^{-f_i},
\]

and, for `1<=t<=f_i`,

\[
\Pr(T_i=t)=(\ell-1)\ell^{t-1-f_i}.                         \tag{2}
\]

The primary pairs for different `ell` are independent.  The factor-first
stripping chain factors when `T_p != T_q`.  Equality at `t` certifies the
common block `ell^t`.  Relative to a current certified modulus `M`, the
gain is

\[
\max(t-v_\ell(M),0)\log_2\ell.                             \tag{3}
\]

Equations (1)--(3) give the exact probability of a factor, the exact
probability of strict lcm growth, and the expected log-lcm gain.  F260
reports three states: public `M=1`, the public small-prime state supplied by
the candidate grammar, and the hidden diagnostic state `M=gcd(p-1,q-1)`.
Only public states are eligible for program ranking.  The last state is a
hostile/oracle stratum, not an algorithm.

## Unfactored words

Put

\[
d=\gcd(p-1,q-1),\quad s_p=(p-1)/d,\quad s_q=(q-1)/d.
\]

For a public positive word `W`, set

\[
r_p={s_p\over\gcd(s_p,W)},\qquad
r_q={s_q\over\gcd(s_q,W)}.
\]

The F205 trial with exponent `(N-1)W` has exact return probabilities
`1/r_p,1/r_q`.  Its exact Miller-chain factor probability is computed with
the two-primary formula in P205.  The simpler primary rank is

\[
\boxed{H(W)=\max(1/r_p,1/r_q)},                             \tag{4}
\]

which differs from the exact factor probability by at most a constant
factor.  F260 records both.

Candidate words are never materialized when a modular support computation
suffices.  This changes neither (4) nor the exact Miller score.

## Collision-energy words

For a public finite integer multiset `Z={z_1,...,z_m}` and prime `ell`,
define

\[
\kappa_\ell(Z)
 ={1\over m^2}\#\{(i,j):i\ne j,\ z_i\ne z_j,
                         \ z_i\equiv z_j\pmod\ell\}.       \tag{5}
\]

This is computed exactly by residue buckets with a correction for repeated
integer values.  If `ell^e` divides one P205 residual and a distinct pair
collides modulo `ell`, the public word

\[
W=|z_i-z_j|^n
\]

captures the complete primary `ell^e`, because `ell^e<N<2^n`.
For several residual primes, F260 also computes the exact P241
inclusion--exclusion score from the complete joint residue buckets.  The
primary statistic is the expected captured log mass

\[
\boxed{\sum_{\ell^e\parallel r}\kappa_\ell(Z)e\log_2\ell}. \tag{6}
\]

This is diagnostic per hidden side.  Candidate selection uses the minimum
of the two sides and the exact P205 score averaged over all distinct-pair
words when the source has at most 64 values.

## Dyadic terminal score

If the beta-two route gives `p mod 2^t` and common certificates accumulate
to `M`, the terminal modulus is

\[
L=\operatorname{lcm}(2^t,M).
\]

F260 uses the public precision strata

\[
t\in\{\lfloor n/8\rfloor,\lfloor n/6\rfloor,
       \lfloor n/5\rfloor\}.
\]

It records the exact distribution of

\[
\Delta\Phi=
\max(0,\lceil\log_2(J/L)\rceil)
-\max(0,\lceil\log_2(J/L')\rceil),                         \tag{7}
\]

where `J=ceil(N^(1/4)/n^4)` and `L'` includes the certified block from the
annihilator trial.  Integer fourth roots are used; no floating comparison
decides terminality.

## Hypergeometric boundary

For `B=floor(sqrt(N))`, `H=floor(B/2)`, and fixed small `r,c`, define the
ratio

\[
R_{r,c}={\binom{B+c}{H+r}\over\binom BH}={P_{r,c}\over Q_{r,c}}
\]

in lowest terms.  Each ratio is represented by signed interval products;
the grammar never materializes either central binomial coefficient.
It admits only:

* the reduced numerator and denominator;
* adjacent exact ratios;
* determinants `P_i Q_j-P_j Q_i`;
* sums and differences after cross multiplication; and
* exact divisions whose divisibility is checked at runtime.

These expressions cost `O((|r|+|c|) polylog N)` bit operations for the
fixed menu.  A full central binomial coefficient is retained only as a
named nonoperational oracle control and is ineligible for ranking.  This
separates a factor-oracle identity from an efficiently evaluable source.

