# Fixed Research Statement

## Input and output

The input is an integer \(N\ge 2\), given in binary, with bit length

\[
n=\lceil\log_2(N+1)\rceil.
\]

For this task, a quasipolynomial bound in \(n\) means

\[
Q(n)=2^{C(\log_2(n+1))^k}
\]

for fixed constants \(C>0\) and \(k\ge1\), independent of \(N\) and its
unknown factors. This includes polynomial bounds.

The required output is its complete prime factorization

\[
N=\prod_{i=1}^k p_i^{e_i},
\]

where the \(p_i\) are distinct primes and the \(e_i\) are positive integers.

## Exact claim to prove

Every integer \(N\ge 2\) can be factored completely by a classical Las Vegas algorithm in expected quasipolynomial time in the input length \(n\), without promises such as semiprimality, balanced factors, squarefreeness, special factor congruences, or smoothness conditions.

Equivalently, a solution may give a classical Las Vegas algorithm that returns a nontrivial divisor of every composite \(N\), provided it also proves the reduction to complete factorization and accounts for the total expected bit complexity.

## Computational conventions

- A Las Vegas algorithm returns only correct outputs, terminates with probability one, and has expected running time bounded by a fixed quasipolynomial \(Q(n)\) for every input.
- A deterministic worst-case quasipolynomial-time algorithm qualifies.
- A bounded-error routine qualifies only after efficient verification and an explicit Las Vegas conversion with a proved expected quasipolynomial bound.
- Running time is uniform bit complexity. It includes random-bit generation, all arithmetic, invoked subroutines, intermediate bit lengths, data structures, recursion, repetition, and verification.
- The proof must exhibit fixed constants \(C>0\) and \(k\ge1\), independent of \(N\) and its unknown factors, such that \(\mathbb E[T(N)]\le 2^{C(\log_2(n+1))^k}\) for every \(N\).
- Every randomized or restart step needs proof of correctness of every returned answer, almost-sure termination, and a sufficient success-probability or expected-trial bound.
- The complete algorithm must cover primes, prime powers, repeated factors, even integers, and arbitrary composites.

## Non-solutions

None of the following meets the claim unless it implies the exact theorem above:

- algorithms for only a special class of inputs;
- heuristic or average-case analyses;
- running time polynomial in \(N\), or any bound larger than quasipolynomial in \(n\), such as \(\exp(n^\alpha)\) for fixed \(\alpha>0\);
- constant/exponent improvements to QS/GNFS-style methods;
- reductions to conjectures or unproved theorem-strength lemmas;
- quantum algorithms;
- verification through any finite input bound;
- candidate algorithms lacking complete correctness and expected-runtime proofs.

This statement is fixed for the run and must not be weakened to fit a result.
