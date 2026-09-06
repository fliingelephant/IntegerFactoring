# F226 provenance

## Closest prior route

The closest prior route is F223, which gives the conditional APR/CL residue
terminal and defeats fixed banks, a generic independent-residue heuristic,
and one uniform primary-2 anchor.  F226 differs materially because its bank
is input-dependent, refreshed after seeing `N`, and obtained from complete
factorizations of exact-uniform half-size binary children.  F226 also proves
the full recursion bound and the affine hyperbola model for this source.

P175 supplies the quarter-bit known-residue terminal.  F220 supplies the
aggregate-common-order formulation.  P215 is the closest scalar reciprocity
boundary; F226 restates the exact affine involution for arbitrary bank
modulus `S` rather than a divisor of `(N-1)/2`.

No claim in F226 needs a web citation.  The generalized CRT, cyclicity of
`(Z/ell Z)^times`, and the known-residue terminal are used in the same scope
as the promoted or frozen prior packets.

## Discovery sequence

1. The proposed top-bit child was factored conceptually.  Its primes give
   `N=2^(n-1) mod ell`, but this alone did not supply local orbit acceptance.
2. D04 scanned the top child and upper-half truncations.  The pooled pattern
   looked strong, but factoring many `(n-1)`-bit children has no QP
   recurrence.  This exposed the recursion error.
3. Restricting to lower-half prefixes made every child half-size and exposed
   the exact nested-prefix recurrence.  A first draft incorrectly extended
   consecutive coprimality to all prefix pairs; self-audit removed that
   false extension before freezing.
4. Multiplication by odd `N` modulo `2^m` gave an exact-uniform Las Vegas
   refresh mechanism.
5. D06 found deterministic counterexamples even with ideal local labels.
6. D08 found a large finite repair rate under random multipliers, motivating
   the positive source theorem but not an asymptotic probability claim.
7. The affine torsor calculation isolated why binary uniformity and hidden
   orbit uniformity are different random variables.
8. Exact enumeration over all multipliers then showed that the full child
   product is a double factorial independent of `N`.  Prime incidence is
   reciprocal in the prime size.
9. Grouping accepted primes by local order identified the hidden common
   cyclotomic gcd `gcd(p^h-1,q^h-1)`.  Grouping by compatible exponent
   identified the sharper support integer `N^i-p`.
10. A polylogarithmic block with capped complete divisor enumeration turned
    compatible hidden support into a concrete Las Vegas attempt.  This
    removed the need to assume an oracle that selects good primes.
11. The exponents zero and one then gave an exact favorable-state theorem:
    a QP-sized shifted divisor of `p-1` or `q-1` that closes the terminal
    gap is captured and tried with inverse-QP probability.
12. The reciprocal-incidence law and the bit-size of `N^i-p` yielded the
    QP-enumeration dominance theorem.  This is the exact all-input boundary
    for the prime-support-only use of the random bank.

## Remote environment note

The requested `ssh seetacloud` host was inspected before scaling.  It had 32
reported CPUs, 503 GiB RAM with 367 GiB available, 22 GiB free disk, and a
host load near 56.  The container had no Python, SageMath, PARI/GP, or Julia;
only GCC/G++ and coreutils `factor` were available.  No package installation
or remote mathematical run was performed.  The exact local scans stayed on
the Mac after checking load and memory pressure.
