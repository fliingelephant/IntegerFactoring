# F91 proof-blind reconstruction statement

Reconstruct or refute the claims below without reading the F91 candidate,
audit, later F91 artifacts, or later durable-state entries.

Let \(N=pq\) for distinct odd primes, let

\[
G=(\mathbb Z/N\mathbb Z)^\times,
\]

and put

\[
g=\gcd(p-1,q-1),
\qquad
A=(p-1)/g,
\qquad
B=(q-1)/g,
\qquad
S_N=G^{N-1}.
\]

Using the supplied F89 rectangularization theorem, or a self-contained
proof, prove or refute that

\[
S_N\cong C_A\times C_B\cong C_{AB},
\qquad
\gcd(A,B)=1,
\qquad
AB>1.
\]

Prove or refute that \(S_N\) contains exactly \(A+B-2\) positive
separators with uniform density

\[
1/A+1/B-2/(AB).
\]

Check the edge cases \(A=1\), \(B=1\), and why \(A=B=1\) is impossible
under the distinct-prime premise.

Now sample \(a\) uniformly from \(\{1,\ldots,N-1\}\). Compute
\(\gcd(a,N)\), return a proper factor if found, and otherwise accept the
unit and set

\[
y=a^{N-1}\pmod N.
\]

Prove or refute that accepted \(a\) is exactly uniform in \(G\), that \(y\)
is exactly uniform in \(S_N\), and that accepted-unit sampling has constant
expected overhead. Verify the claimed inequality

\[
\varphi(N)/(N-1)>1/2.
\]

For two independent accepted units, prove or refute

\[
\Pr(\langle y_1,y_2\rangle=S_N)
=
\prod_{\ell\mid AB}(1-\ell^{-2})
\ge
6/\pi^2.
\]

Check cyclic primary decomposition, independence across primes, repeated
prime powers, and the empty-product issue.

Prove or refute the following reduction. Suppose an axis-localization
procedure takes \(N\) and a public list that generates \(S_N\), has
polynomial bounded work on every list, returns only a verified proper
factor or failure, and succeeds with inverse-polynomial probability on every
promised generating list. Then fresh two-sample batches plus that procedure
give a classical Las Vegas expected-polynomial factorer for distinct odd
semiprimes. The reduction must not need to recognize whether a batch
generates \(S_N\).

Explain precisely why the generator source and near-uniform subgroup sampler
do not themselves localize an axis when both \(A,B\) are large. Do not claim
a lower bound. Identify the two axes as the unique subgroups of orders
\(A\) and \(B\) inside the cyclic group of order \(AB\).

Verify the supplied fixed cases.

1. At \(N=4033=37\cdot109\), show
   \(g=36,A=1,B=3\) and check the supplied factor identity
   \(\gcd(5^{4032}-1,4033)=37\).
2. At \(N=2047=23\cdot89\), show
   \(g=22,A=1,B=4\), so one uniform element of \(S_N\) gives a proper gcd
   with probability \(3/4\). Explain why this does not contradict the
   supplied fact that the smaller feedback subgroup \(\langle11,2\rangle\)
   is killed by \(N-1\).

State the exact scope. This is an all-input constant-probability source of
public generators for a factor-bearing subgroup on distinct odd semiprimes.
It does not give an axis decoder, compute hidden orders, handle prime powers
or more CRT components, simulate order finding, or prove a complete
factoring algorithm.
