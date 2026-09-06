# F236 preregistration: zero-defect integer-word source scan

## Purpose

This computation is for conjecture discovery and counterexample search only.
It does not certify an asymptotic theorem.

## Exact finite domain

Enumerate every pair of distinct odd primes

\[
3\le p<2^{22},\qquad p<q<2p,
\]

for which, with

\[
N=pq,\quad n=\lceil\log_2(N+1)\rceil,\quad
B=2^{\lfloor n/2\rfloor},
\]

one has `B | N-1`.  Candidate `q` values will be generated from
`q = p^{-1} (mod B)` and the interval `p < q < 2p`; primality and every
domain condition will then be checked directly.

For each pair, compute

\[
e=v_2(p-1)=v_2(q-1),\quad
D=\gcd((p-1)/2^e,(q-1)/2^e),
\]

and the coprime residuals `s_p,s_q` from P204.  Abort and report if the two
2-adic valuations differ.

## Frozen public word menus

Put `K=U=C=n` and `H=(N-1)/B`.  Measure the exact residuals left by:

1. `W_N = product_{1<=k<=K} (N^k-1)`;
2. `W_H = product_{1<=k<=K} (H^k-1)`, omitting zero factors;
3. `W_shift = product_{1<=u<=U,-C<=c<=C,uH+c>0} (uH+c)^n`;
4. the product of the preceding three words;
5. `K!`.

The program will compute each gcd modulo `s_p` and `s_q`; it will not
materialize the full words.  It will also compute the exact multiplicative
orders `ord_{s_p}(N),ord_{s_q}(N)`.  Since `H` need not be a unit modulo a
residual, its orders will be measured modulo the largest divisors of
`s_p,s_q` that are coprime to `H`.  The order modulo one is one.

## Frozen outputs

Report:

- the number of admissible pairs by bit length;
- the maxima of the smaller `N`-meta-order and smaller `H`-meta-order;
- the maxima of `min(r_p,r_q)` for each frozen word menu;
- every record-setting pair for those quantities;
- the ten worst pairs under the combined menu, ordered by
  `min(r_p,r_q)` and then by `N`;
- for each record pair, the factorization of `s_p,s_q`, the gap `q-p`,
  the inverse-product carry `H`, and the centered residues of `H` modulo
  each residual prime.

No menu, bound, or output ranking will be changed after the scan starts.
Any follow-up computation will receive a separate preregistration.
