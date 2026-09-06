# F241 self-audit

1. The deterministic word does not claim that `N-1` contains all of either
   P205 residual.  It removes only complete primary parts whose rational
   primes meet `N-1`.
2. The exponent `n` saturates every hidden primary because every exponent
   in an integer below `N` is strictly less than `n`.
3. Equal integer samples are excluded.  They would otherwise appear as
   modular collisions but give the unusable difference zero.
4. Formula `(CE)` uses squarefree moduli because `Delta^n` turns one
   rational-prime hit into complete primary saturation.
5. The P205 implication averages only after conditioning on the sampled
   public word.  The later group element is fresh.
6. Formula `(D)` applies only when `gcd(m,N-1)=1`, as required for the
   character group.  The deterministic word has already removed all other
   residual primaries.
7. The subgroup-size bound subtracts the exact integer-equality mass.
   Without `T>=2Q`, it need not be positive.
8. The conditional bank uses a union bound over fewer than `n` rational
   primes.  It does not assume independence between different primes.
9. Uniform random radices do not create a new law: complementary quotients
   are uniform divisors of the same integer.
10. Complete factorization of `N-1` is granted.  No recursive factoring
    algorithm is inferred.
11. The theorem is conditional.  It proves no all-input bound on `h_ell`
    and no numerical-QP factoring algorithm.
12. No computation was used.
