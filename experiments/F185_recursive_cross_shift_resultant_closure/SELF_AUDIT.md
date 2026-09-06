# F185 self-audit

## Verdict

The fixed-contraction cross-resultant transition and its recursive QP
accounting are internally consistent. The result is conditional on the
strong-induction factoring calls and leaves the wide-shift-hard descendant
unresolved. A fresh hostile audit and a strict statement-only reconstruction
are required before any promotion.

## Kill-first checks

1. **The contraction is in bit length.** The exact condition
   \(K(1+K\lambda)\le\lfloor\rho n\rfloor\), not merely
   \(R<N\), gives every recursive input a fixed-factor bit contraction.
2. **The admissible range is exact.** Solving
   \(\lambda K^2+K\le\lfloor\rho n\rfloor\) gives the displayed upper
   endpoint. The range is explicitly allowed to be empty for finitely many
   small inputs.
3. **Both filters use the original state.** Otherwise double extinction
   would not certify two polynomial vanishings for each original order
   prime.
4. **All nonunit cases are present.** Index zero is the linear polynomial
   \(X+\delta\); multiplicative order is used only for units.
5. **No evaluated filter factor is zero.** Every \(N+\delta>1\), so all
   factors in \(C_\delta\) are positive.
6. **No resultant is zero.** Linear cases are explicit. In the nonlinear
   case, cross-menu center distance at least three separates the two unit
   circles.
7. **Unit resultants are harmless.** They receive no recursive factoring
   call and contribute no prime to \(U\).
8. **Arbitrary order prime powers are covered.** Every order-prime exponent
   is less than \(n\), and the outer \(n\)-th power of \(U\) supplies all
   multiplicities.
9. **Repeated factors of \(N\) are covered.** Coprimality of every filtered
   order with the hidden rational prime makes reduction to the prime field
   injective on the generated subgroup. A gcd cannot select only part of a
   hidden prime power.
10. **A prime-power input is covered.** The gcd branches can then be only
    one or \(N\), but double extinction still gives the annihilator and
    stripping returns its exact local order.
11. **Recursive factorization is not hidden.** Every resultant greater than
    one is an explicit recursive input below \(N\). The candidate clearly
    states that it relies on strong induction and does not call this a
    top-level factoring proof.
12. **All siblings are counted.** One node has at most
    \(L^2(K+1)^2\) recursive calls. The recurrence multiplies this branching
    over every contracted level.
13. **The recurrence remains QP.** Fixed-factor bit contraction gives
    \(O(\log n)\) depth. Multiplying QP branching over those levels raises
    the polylogarithmic exponent by at most one.
14. **The exponent and annihilator are explicit.** Their bit lengths, all
    resultant arithmetic, and every stripping attempt are included in the
    local QP bound.
15. **The hard branch is not inflated.** A surviving order prime is a unit
    with period above \(K\) for all shifts in one menu, but this supplies
    neither a factor nor an exact common order.
16. **The carry claim is narrow.** It proves only that a positive canonical
    inverse carry is smaller than both endpoints and coprime to them. It
    makes no general impossibility claim about multiple nonlinear carry
    relations.

## Computation and ledger state

No mathematical computation or checker was run. No durable ledger was
edited by this candidate artifact.
