# F234 self-audit

## Verdict

The candidate survives self-audit as an exact random-bank identity, a
single-prime terminal dichotomy, and a conditional harmonic-mass lemma.  It
does not supply the missing all-input lower bound on expected captured mass.

## Checks

1. The arbitrary-bank formula uses only linearity of expectation.  It does
   not assume independence across primes, children, or adaptive stages.
2. The iid specialization uses independence only for repeated draws from
   the same declared distribution.
3. Saturating exponent `n` is sufficient for every primary valuation below
   `N`; no valuation of a child factor is confused with a valuation of a
   residual order.
4. The known residue `z_ell` is public after `ell` is exposed.  Equation
   (12) is also the direct reduction of `N mod ell`; the child factorization
   supplies the previously unknown modulus, not a secret residue value.
5. The row is unordered.  F234 never claims to know whether `ell` belongs
   to `p-1` or `q-1`.  It explicitly tries both orientations for one prime.
   It also does not promote a row modulo `ell` to one modulo a hidden
   `ell^e`; saturating the exponent word and certifying a residue modulus are
   distinct operations.
   Every exposed child prime is tried, including nonresidual primes.  The
   complete visible list and its public prime-power levels have QP size, and
   false rows cannot survive gcd verification.
6. Exclusivity makes `z_ell!=1` and makes `ell` coprime to the accumulated
   common modulus `M`.
7. Deterministic direct child factors stop before the projected stage and
   only improve success.
8. The harmonic surplus bound uses the bounded range `0<=X<=L`; it is not a
   misuse of Markov's inequality.  The exact denominator is `log_2R`, since
   `L_p-T_p=log_2R` on the declared `S_p>R` branch.
9. The P202 lower bound after `min(r_p,r_q)<=R` distinguishes the residual-one
   case from the two-nontrivial-residual case.
10. Combining bank probability and projected probability uses a fresh unit
    sampled after the public bank, so conditional history-wise bounds apply.

## Hostile targets

A reviewer should attack the equivalence between captured support and
residue rows, the claim `z_ell!=1` when `D` and one quotient share a prime,
the CRT coprimality with `L_0`, the threshold event in (20), and the P202
probability multiplication in (21).
