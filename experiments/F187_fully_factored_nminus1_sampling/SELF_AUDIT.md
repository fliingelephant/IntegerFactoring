# F187 self-audit

## Verdict

The deterministic stripping theorem and exact probability laws are
internally consistent. The elementary obstruction holds for every bounded-gap
prime pair. The infinite-family conclusion uses the standard
bounded-prime-gap theorem.

This is a proof-only candidate. It still requires a fresh hostile audit and,
if that passes, a statement-only blind reconstruction.

## Attacks checked

1. **Prime-power components.** A full \((N-1)\)-root has order coprime to
   the hidden rational prime. Reduction modulo that prime is injective on
   the root subgroup. Every stripping gcd therefore selects an entire hidden
   prime-power component. Partial lifts can occur only in the initial gcd and
   already give a proper divisor.

2. **The formula \(d_i=\gcd(N-1,p_i-1)\).** The omitted
   \(p_i^{e_i-1}\) part of \(\varphi(p_i^{e_i})\) is coprime to \(N-1\),
   because \(p_i\mid N\).

3. **Complete nonreturn.** If \(a^{N-1}\ne1\pmod {p_i}\), no exponent
   dividing \(N-1\) can return modulo that component. When the initial gcd
   is one, this holds at every hidden prime, so all divisor-exponent gcds are
   one.

4. **Order stripping.** A gcd equal to one at \(R/q\) means every local
   order needs the current \(q\)-adic valuation. A gcd equal to \(N\) means
   none needs it. Mixed need gives a proper factor. Hence a no-factor terminal
   has one exact common order, not merely a common multiple.

5. **Order distribution.** Conditional on full return, CRT gives independent
   uniform elements in cyclic groups of sizes \(d_i\). There are exactly
   \(\varphi(r)\) elements of order \(r\), which gives the power
   \(\varphi(r)^s\) and requires \(r\mid\gcd_i d_i\).

6. **No-progress state.** A common returned order changes the lcm state
   exactly when it does not divide the existing state. Equation (17) includes
   both this synchronized nongrowth and complete nonreturn.

7. **Semiprime formula.** For \(m=pq-1\), both root-group sizes equal
   \(d=\gcd(p-1,q-1)\). At initial state one, only double nonreturn and the
   double identity tuple fail to factor or grow. Expansion gives equation
   (20).

8. **Bounded-gap quantifier.** The probability obstruction is elementary
   for each pair satisfying \(q-p\le H\). Infinitely many such inputs are
   obtained only by invoking the proved bounded-prime-gap theorem. No twin
   prime conjecture or fixed prescribed gap is assumed.

9. **Uniform residues versus uniform units.** A nonunit sample can expose a
   factor, but on \(pq\) its probability is only \(O(p^{-1})\). It does not
   repair the exponential bound.

10. **Accumulation.** On the bounded-gap family, every synchronized order
    divides the fixed integer \(d\le H\). Repeated growth cannot cross \(H\),
    and every fresh uniform sample still has success probability
    \(O_H(p^{-1})\).

11. **Prime terminal.** If the accumulated order divides \(p-1\) for every
    hidden prime and exceeds \(\sqrt N\), a composite input would have a
    prime divisor both at most \(\sqrt N\) and greater than \(\sqrt N\).

12. **Prime powers.** For \(p^e\), every unit returns modulo \(p\), while
    only a fraction \(p^{1-e}\) returns modulo \(p^e\). All other units give
    a proper partial-power gcd. Perfect-power preprocessing is independent of
    the random route.

13. **One-child correction.** Factoring \((N-1)/2\) is a single child with
    one-bit decrease. This gives a QP chain only when the enclosing stage has
    no other recursive children. Recursively completing both sides of a
    returned split is outside that recurrence and is not claimed QP.

14. **Scope.** The obstruction covers independent uniform random bases after
    complete factorization of \(N-1\). It is not a lower bound for adaptive,
    deterministic, biased, or algebraically constructed bases, and it is not
    a lower bound for factoring.

No mathematical computation, search, cross-family audit, or literature audit
was run. No durable proved/failed ledger was edited.
