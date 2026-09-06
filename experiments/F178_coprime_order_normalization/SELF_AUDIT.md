# F178 self-audit

## Verdict

The stated postprocessor is internally consistent. It needs an independent
hostile audit and a fresh statement-only reconstruction before promotion.

## Kill-first checks

1. **Arbitrary prime powers.** The proof works with each full component
   \(p^a\). The least-prime step uses reduction modulo \(p\), and the
   small-common-order step uses the standard lift
   \(\operatorname{ord}_{p^a}(4)=\operatorname{ord}_p(4)p^u\).
2. **Removal exponent.** Since every local order is less than \(N<2^n\),
   \(N^n\) contains enough of every prime dividing \(N\) to remove its full
   primary part from every local order.
3. **Identity-global branch.** The least hidden prime excludes all nontrivial
   prime divisors of \(\operatorname{ord}_p(4)\). The only remaining case is
   \(p=3\), which is a public proper gcd even for a pure power of three.
4. **Small common order.** It is not declared a state. The least component
   forces \(m=\operatorname{ord}_p(4)\), while the old hard inequality
   \(e_j>C\) proves that \(\gcd(4^m-1,N)\) cannot equal \(N\).
5. **Sign quotient.** The QP cap condition is \(T\ge2C\), not merely
   \(T\ge C\), because an even order can lose one factor two.
6. **No circular factorization.** Only \(\Lambda_T\) is factored, using its
   public sieve construction. No factorization of \(N^k-1\), a cyclotomic
   value, or an unknown local order is assumed.
7. **Exact limitation.** The final local orders are coprime to \(N\), but
   they need not be equal. This does not complete the factoring algorithm.

## Computation

No mathematical computation was run. No durable result ledger was edited by
this candidate artifact.
