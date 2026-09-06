# F186 self-audit

## Verdict

The one-child theorem and its P162/F185 cross-resultant specialization are
internally consistent. This is a proof-only candidate. It still requires a
fresh hostile audit and a statement-only blind reconstruction.

## Attacks checked

1. **Prime powers.** Local orders are coprime to the hidden rational prime.
   Reduction is injective on each generated cyclic subgroup. Identity gcds
   therefore select complete hidden prime-power components.

2. **Insufficient valuation.** A support entry may contain a covered prime
   only once. Raising it to the public power \(n\) supplies more copies than
   any valuation in a local order below \(N<2^n\).

3. **Cumulative versus final annihilator.** Coverage proves only that the
   cumulative exponent eventually kills all orders. The proof uses the first
   global return. At that step
   \(v_i=v_{i-1}^{A_i^n}=1\), so the single final power \(A_i^n\) annihilates
   the current element. It does not falsely claim that it annihilates the
   original element.

4. **Earlier identity status.** Before the first global return, absence of a
   proper gcd forces every identity gcd to equal one. Hence the current local
   orders are all nontrivial when the final child is selected.

5. **Loss of roughness.** Peeling replaces each order by a divisor. Any
   nontrivial divisor of a \(T\)-rough order remains \(T\)-rough. The exact
   common order returned after stripping is therefore above \(T\).

6. **Entries sharing a factor with the input.** Every entry is screened
   against \(N\) before use. A proper gcd factors. Since a nontrivial entry
   has at most \(n-1\) bits, it is strictly below \(N\), so a gcd equal to
   \(N\) cannot occur.

7. **Duplicates and unit entries.** Repeated entries only repeat a harmless
   filter. An entry equal to one is skipped and cannot be the first global
   return after a one-valued identity gcd.

8. **Recursive cost.** The proof uses one child, not a QP number of siblings.
   A one-bit decrease gives \(\mathcal T(n)\le\mathcal T(n-1)+Q(n)\), which
   is QP. The theorem expressly does not authorize extra uncharged recursive
   children in an enclosing algorithm.

9. **Cross-resultant coverage.** Both menu extinctions are evaluated on the
   same original unit. Each local-order prime is a common-root prime for one
   polynomial from each separated menu, so it divides a listed resultant.

10. **Scope.** The result does not close the wide-shift-hard branch and does
    not turn an exact common order into a universal factoring terminal. No
    all-input factoring or inverse-probability success claim is made.

No computation, cross-family audit, human audit, or publication-level
literature review has run. No durable proved/failed ledger was edited by the
candidate construction.
