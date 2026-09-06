# Self-audit of F226

## Scope and quantifiers

1. The top-bit child is one `(n-1)`-bit recursive call.  F226 does not claim
   that QP many such calls are safe.
2. The random-bank recursion uses only children of at most `floor(n/2)`
   bits.  Its branching recurrence is solved explicitly.
3. Gcd screening occurs before a prefix child or its prime factors are used
   as auxiliary units.
4. Local orbit membership is not treated as public.  Numerical scans grant
   the hidden factor only to measure an ideal oracle.
5. Local orbit membership and cross-prime exponent compatibility are
   separate.  Both appear explicitly.
6. A compatible exponent for `p` makes the exponent for `q` equal to `1-i`;
   no same-exponent claim is made for the two hidden factors.
7. The conditional terminal enumerates at most `H<=QP` exponents.  A large
   local order is not called useful merely because the auxiliary modulus is
   large.
8. The affine-torsor probability is a named model over formal local
   factorizations.  It is not presented as the distribution of adversarial
   integer factors or of the multiplier `u`.
9. The scalar-transcript boundary expressly excludes non-scalar APR/CL
   identities, rational zero divisors, and an evaluator that already
   separates the two CRT components.
10. Equation `S|(N^i-p)` is a characterization of compatible support, not a
    method to compute the hidden integer on the right.
11. Theorem G repairs the hidden-subset issue only for a polylogarithmic
    block whose complete squarefree-divisor list is below the cap.  It does
    not silently discard rejecting primes.
12. The exponent bank in Theorems F--H consists of numeric exponents
    `0<=i<T`, with `T` numerical QP.  A QP-bit exponent of exponentially
    larger numeric value is outside the support-size bound (F5).
13. The potential law is exact, but its lower bound is conditional on its
    displayed expectation exceeding the terminal threshold.  No input-wise
    harmonic-mass lower bound is asserted.
14. The safe-prime-shift calculation is a named conditional model.  It does
    not assert an infinite family and it obstructs the guaranteed
    `i=0,1` classes, not every possible larger exponent.
15. The favorable-state corollary does not assume that the divisor `d` is
    public.  It uses a public QP upper bound `Q`, and complete capped divisor
    enumeration tries `d`.  Its all-input gap is the existence of such a
    QP-bounded shifted divisor.

## Complexity

16. Random-bit generation uses `O(n)` bits per bank.
17. A bank has `O(n^2)` total child encoding, not an exponential explicit
    product.
18. Factoring every `ell-1` adds only QP many half-size descendants per
    level.  It is included in the recurrence.
19. The recursion depth is `O(log n)`.  Multiplying numerical-QP branching
    factors over that depth remains numerical QP with one extra power of
    `log n` in the exponent.
20. The capped divisor enumeration has expected list-size control before
    Markov truncation.  It never materializes the complete all-multiplier
    double-factorial product.
21. Random children need not be balanced or semiprime.  Every recursion
    statement is conditional on an all-input dispatch that is correct on
    arbitrary half-size integers.
22. No runtime conclusion is inferred from the finite scans.

## Arithmetic details

23. Oddness makes every canonical binary prefix nonzero and odd.
24. Only consecutive changed prefixes are asserted coprime.  Nonconsecutive
    prefixes can share odd factors, which are deduplicated.
25. The top-bit identity `N=2^(n-1) mod ell` is not extended to a random
    multiplier bank; there the forced APR anchor remains `N`.
26. The totient lower bound uses that the selected auxiliary modulus is odd
    and squarefree.  Repeated auxiliary primes are discarded.
27. Proper gcd outputs and final factors are directly verified.
28. The ensemble product identities include multiplicity.  Candidate
    moduli and support products are squarefree after prime deduplication.
29. Prefix incidences are correlated.  Only marginal counting and union
    bounds are used for (E5), (E6), and (H1).
30. The enumeration-dominance theorem concerns discovery of compatible
    prime values.  It does not identify the compatible subset or remove the
    random grouping used by Theorem G.  It also does not simulate a future
    use of the quotient `floor(uN/2^m)`.

## Numerical provenance

31. D01 and D02 stopped before mathematical output.  D03 did not complete
    under the orchestration call.  D04 completed an upper-half scan, but its
    pooled bank was later recognized as recursion-unsafe; it is preserved as
    discovery history, not theorem evidence.
32. D05 completed calculations but produced invalid partial JSON due to a
    Sage integer serialization error.  D06 changed serialization only and
    is the valid recursion-safe deterministic output.
33. D07 computed exact random-multiplier numerators, but Sage-to-JSON
    conversion displayed rational rates as zero.  D08 changed only the rate
    postprocessing and preserves D07's exact numerators and denominators.
34. The finite cohorts are 19–29 bits.  At this scale `n^4` is usually
    larger than the auxiliary orders.  No large-input extrapolation is made.

## Conclusion

The exact bank construction, capped-divisor Las Vegas bridge, and
prime-support enumeration boundary survive this self-audit.  The all-input
inverse-QP harmonic-mass law, or a factor/carry transition on scalar
rejection, remains unproved.
