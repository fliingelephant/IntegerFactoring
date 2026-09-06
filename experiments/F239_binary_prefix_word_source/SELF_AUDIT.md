# F239 self-audit

## Exact-claim checks

1. The literal quotient range includes `K_n=0`.  It is not called a valid
   F238 word.
2. Every corrected word uses only nonzero absolute factors and is positive.
3. The exponent `n` saturates every residual prime power after one
   prime-support hit because its exponent is smaller than `n`.
4. The quotient interval law is valid for every prime, including two.
5. The local congruence law uses inversion of `2^j` and is stated only for
   odd residual primes.
6. Positive and centered suffixes use distinct incidence laws.  They are
   not inferred from the quotient law.
7. Round-half-up is explicit.  In particular, `C_1=-1` for odd `N`.
8. The reported factor-bit sums are rigorous word-size bounds.  They are not
   called exact bit lengths.
9. Construction of a word does not factor `p-1`, `q-1`, or a residual.
   Residual factorizations are analysis variables only.
10. The Mersenne and Fermat-neighbor criteria exclude residual primes that
    divide `N`.  They assert no infinite semiprime family.

## Evidence checks

1. The first broad run aborted on the invalid `ell=2` local cross-check.
   It produced no result and is not evidence.
2. The original preregistration and empty aborted output are preserved.
3. The protocol repair was frozen before rerun.
4. The corrected scanner checks each residual twice: prime incidence and
   whole-residual modular words.
5. The F236-domain count is exactly 34,463 on both completed runs.
6. The broad domain is exhaustive only for `p<2^16` and balance `p<q<2p`.
7. The broad `r<=n^3` count is a finite-bound cutoff effect.
8. The F237 factorization is imported from its frozen certificate.  F239
   makes no new primality inference for that row.
9. No random diagnostic or heuristic sample enters an exact claim.
10. No finite maximum is promoted to an asymptotic theorem or
    counterfamily.

## Remaining question

The F238 source problem remains open.  A positive result needs an all-input
quasipolynomial upper bound on one remaining residual.  A negative result
needs an infinite semiprime family with a super-quasipolynomial residual
lower bound.  This packet supplies neither.
