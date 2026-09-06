# F219 V2 candidate: Las Vegas beta-two refinements need integer bias

## Status and scope

This is a self-audited proof-only boundary for the balanced beta-two branch,
with one preregistered finite discovery run. It is not a factoring algorithm.
It strengthens the common-order interface by permitting primary
contributions from unrelated annihilators. It then proves an exact law for
the time to sample the true dyadic refinement. Along that certified
true-refinement route, the waiting cost cancels the gain from the larger
terminal modulus. Wrong refinements can still reveal a verified factor, so
this is not a lower bound on the total runtime of every such Las Vegas
algorithm.

The closest prior results are P165, P172, P173, P175, and P191. P165 treats
uniform group bases and whole common orders. The new parts here are:

1. individual certified prime-power contributions from unrelated
   annihilators;
2. their exact generalized-CRT combination with a beta-two reciprocal
   prefix;
3. the exact Las Vegas true-refinement probability and its certified
   expected-cost cancellation for uniform prefix refinements;
4. the same bijection for the integer-specific top multipliers
   `(-1)^B binom(rN-1,B)`.

No generic group-base sampler is proposed as the positive source.

## Setup

Let

\[
N=pq,\qquad p<q<2p,
\qquad B=\lfloor\sqrt N\rfloor,
\]

where \(p,q\) are distinct odd primes. Let \(n\) be the bit length of
\(N\). A numerical-QP function is QP in \(n\).

## Theorem A: unrelated primary annihilator certificates accumulate

Let \(a\) be a public unit modulo an odd integer \(N\), and let \(A\) be a
fully factored public positive integer such that

\[
a^A=1\pmod N.
\]

For a prime power \(\ell^e\parallel A\) with \(\gcd(\ell,N)=1\), put

\[
G_{a,A,\ell}=\gcd(a^{A/\ell}-1,N).
\]

Then:

- a proper \(G_{a,A,\ell}\) factors \(N\);
- if \(G_{a,A,\ell}=1\), then

  \[
  \boxed{\ell^e\mid r-1\quad\text{for every rational prime }r\mid N.}
  \]

Consequently, certified prime powers obtained from any number of unrelated
pairs \((a_i,A_i)\) can be accumulated as

\[
M=\operatorname{lcm}(2,\ell_1^{e_1},\ldots,\ell_s^{e_s}).
\]

On the no-factor branch, \(M\mid r-1\) for every rational prime \(r\mid N\).
No single public element of order \(M\), and no whole exact common order, is
required.

## Theorem B: CRT combination and exact true-hit cancellation

Assume a certified even \(M\) satisfies

\[
p\equiv q\equiv1\pmod M.
\]

Suppose the correct beta-two reciprocal prefix

\[
u_s=p^{-1}\pmod {2^s}
\]

is known, where \(s\ge1\), and put

\[
L_s=\operatorname{lcm}(M,2^s).
\]

It determines one correct residue class for \(p\pmod {L_s}\). For any
\(t\ge s\), put \(L_t=\operatorname{lcm}(M,2^t)\). There are exactly

\[
\boxed{H=\frac{L_t}{L_s}}
\]

compatible refinements modulo \(L_t\), exactly one of which contains \(p\).
Uniform sampling therefore hits the true refinement with exact probability

\[
\boxed{H^{-1}=\frac{L_s}{L_t}.}
\]

If \(L_s\ge N^{1/4}\), take \(t=s\), so no guess is needed. Otherwise,
choose the least \(t\ge s\) for which \(L_t\ge N^{1/4}\). Then
\(L_t<2N^{1/4}\).
Sample independently with replacement. Run the known-residue-class terminal
on each sampled class and verify every returned divisor. The waiting time
until the true class is sampled is geometric with exact mean

\[
\frac{L_t}{L_s}=O\!\left(\frac{N^{1/4}}{L_s}\right).
\]

The actual waiting time until any verified factor is returned is at most
this true-class waiting time. It can be smaller because a wrong refinement
can fortuitously reveal a factor.

More generally, combining the per-class terminal cost
\(\widetilde O(N^{1/4}/L_t)\) with uniform refinement gives

\[
\frac{L_t}{L_s}\cdot
\widetilde O\!\left(\frac{N^{1/4}}{L_t}\right)
=\widetilde O\!\left(\frac{N^{1/4}}{L_s}\right).
\]

Thus the certified route through the true refinement gives no asymptotic
improvement over the information already present in \(L_s\). This argument
does not exclude a speedup from verified factors returned on wrong
refinements. A useful selector justified by true-prefix hits must give the
true refinement inverse-QP probability by using additional integer
information.

## Theorem C: random top multipliers are exactly carry guesses

For every positive integer \(r\), define

\[
A_r=(-1)^B\binom{rN-1}{B},\qquad
h_r=\frac{A_r-(1-rq)}N.
\]

Then \(h_r\) is an integer. For every \(t\ge1\), put

\[
z_{r,t}=N^{-1}(A_r-1)\pmod {2^t}.
\]

The exact identity is

\[
\boxed{h_r-z_{r,t}\equiv r p^{-1}\pmod {2^t}.}
\]

For odd \(r\), the affine map

\[
c\longmapsto r^{-1}(c-z_{r,t})\pmod {2^t}
\]

is a bijection from guessed carry residues \(c\) to guessed reciprocal
prefixes. It also bijects the public carry residues compatible with \(M\)
to the \(L_t/L_1\) compatible CRT refinements. Hence a uniform carry guess
has exact success probability \(M/L_t\), independent of how \(r\) is
randomized.

For arbitrary efficiently sampled conditional carry laws \(\mu_r\) and a
public law \(\rho\) on odd top multipliers, the exact useful hit probability
is

\[
\boxed{
\Pr(\text{correct prefix})
=\sum_r\rho(r)\,\mu_r(h_r\bmod2^t).}
\]

Therefore top-multiplier randomization is useful only if one proves
inverse-QP mass on the actual integer carry. Randomness in \(r\) alone does
not supply that mass.

For \(r\) of QP bit length, the power-of-two binomial routine used in P173,
run at precision at least \(\lceil\log_2(rN)\rceil\), computes
\(z_{r,t}\) in QP time. It does not compute \(h_r\).

## Theorem D: exact probability law and a bounded-gap capacity obstruction

For a fully factored exponent \(A\), let

\[
d_p=\gcd(A,p-1),\qquad d_q=\gcd(A,q-1).
\]

If \(a\) is uniform in \((\mathbb Z/N\mathbb Z)^\times\), then for
\(\ell^e\parallel A\), the exact probability of both
\(a^A=1\pmod N\) and \(G_{a,A,\ell}=1\) is

\[
\boxed{
\frac{d_pd_q}{(p-1)(q-1)}
\left(1-\frac1\ell\right)^2}
\]

when \(v_\ell(d_p)=v_\ell(d_q)=e\), and is zero otherwise.

On the beta-two child \(K=(N-1)/2\), the fully factored annihilator
\(A=N-1=2K\) has

\[
d_p=d_q=d=\gcd(p-1,q-1).
\]

Thus the displayed primary-certificate probability is at most
\(d^2/((p-1)(q-1))\). More strongly, every ordinary primary contribution
from every annihilator divides \(d\), so their accumulated modulus always
satisfies

\[
\boxed{M\mid d.}
\]

P165 supplies an infinite balanced bounded-gap prime-pair family. On that
family \(d\mid q-p\), hence \(M=O(1)\) for every possible ordinary
annihilator sampler, not merely for uniform sampling. Combining these
certificates with P175 still requires

\[
s\ge\frac14\log_2N-(\log n)^{O(1)}
\]

reciprocal bits for a QP terminal. The primary-certificate weakening is
valid and useful on favorable inputs, but it cannot replace the quarter-bit
integer selector on all balanced semiprimes.

## Finite discovery evidence

The frozen F219-D01 run checked 432,480 exact identities for all balanced
prime pairs with \(5\le p\le97\), all odd \(1\le r<2^t\), and
\(4\le t\le11\). At \(t=11\), both the \(h_r\) and \(h_r/r\) images had
between 176 and 840 residues among 1,024 samples, and every largest fibre
had size between 3 and 33. For \(N=77\), the zero fibre was empty at every
tested precision. This is finite guidance only.

The preregistered F219-D02 full-period run failed before mathematical work
because the active Python environment did not contain `sympy`. No alternate
run was substituted.
