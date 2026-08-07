# F93 proof-blind reconstruction statement

Reconstruct or refute the claims below without reading the F93 candidate,
any F93 audit, later F93 artifacts, or later durable-state entries.

Let \(H\) be a finite abelian group and put

\[
r_\ell=\dim_{\mathbb F_\ell}(H/\ell H)
\]

for each prime \(\ell\mid |H|\).

1. Prove or refute that \(d\) independent uniform elements generate \(H\)
   with exact probability

   \[
   \prod_{\ell\mid |H|}
   \prod_{i=0}^{r_\ell-1}(1-\ell^{i-d}).
   \]

   Check the Sylow decomposition, the Frattini-quotient criterion, and all
   rank-zero edge cases.

2. Define

   \[
   c_0=
   \prod_{\ell\ {\rm prime}}
   \prod_{k=2}^{\infty}(1-\ell^{-k}).
   \]

   Prove that \(c_0>0\), and prove or refute that if \(|H|<2^n\), then \(n\)
   uniform elements generate \(H\) with probability at least \(c_0\).

3. Let \(N\ge2\) and

   \[
   n=\lceil\log_2(N+1)\rceil.
   \]

   Sample \(n\) independent integers uniformly from
   \(\{1,\ldots,N-1\}\), and gcd-test each against \(N\). Prove or refute
   that one batch returns a proper factor or supplies a generating list for
   \(G_N=(\mathbb Z/N\mathbb Z)^\times\) with probability at least \(c_0\).
   Check conditioning, exact uniformity, the case of low unit density, random
   bits, and polynomial bit complexity. The algorithm need not recognize a
   generating list.

4. For \(N=pq\) with distinct odd primes, prove or refute that three exact
   uniform units generate \(G_N\) with probability at least

   \[
   1/(\zeta(2)\zeta(3)).
   \]

5. Prove or refute that \(G_N\) contains an element \(x\) with

   \[
   1<\gcd(x-1,N)<N
   \]

   for every composite \(N\). Check prime powers, powers of two, and
   composites with at least two distinct prime divisors.

6. Prove or refute the following interpretation. Conditioned on a batch
   that generates \(G_N\), every unit block exposed later by canonical
   feedback is already in the abstract generated subgroup. Feedback can
   still give new public word access, a canonical integer presentation, or
   relation provenance. It therefore need not be algorithmically redundant,
   but its gain is not abstract subgroup enlargement on this batch.

7. Verify the promise reduction: if a polynomial-bounded procedure factors
   with inverse-polynomial probability on every list generating \(G_N\),
   returns only verified factors or failure on every list, then fresh
   factor-or-generate batches give a classical Las Vegas
   expected-polynomial factorer.

State the exact scope. The source theorem does not give the promised
localizer, a useful direct-sampling density, an order algorithm, a classical
HSP solver, or a factoring algorithm.
