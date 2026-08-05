# F14 hostile-audit run manifest

## Scope

- Experiment: `F14_torus_qfactorial_audit`
- Target: `experiments/F14_torus_qfactorial_evaluator`
- Deliverable: independent symbolic hostile audit
- Canonical project files edited: none
- Author files edited: none
- Files created: `RESULT.md`, `RUN_MANIFEST.md`
- Commit created: no

## Inputs and provenance

- Parent task statement
- Repository `AGENTS.md` instructions supplied in the task context
- `experiments/F14_torus_qfactorial_evaluator/RESULT.md`, read in full
- `experiments/F14_torus_qfactorial_evaluator/RUN_MANIFEST.md`, read in full
- No other experiment artifact was used
- No web source was used
- No subagent was used

## Computation

No computational experiment was used.  The audit consists entirely of
symbolic algebra, elementary finite-field/order arguments, valuation checks,
coefficient-sign arguments, and exact hand-checkable modular arithmetic.
There are therefore no source programs, timeout-bearing commands, execution
logs, or generated numeric outputs to register.

## Claims audited

1. Prime-support equivalence of `P_M` and `S_m`, including prime-power gcd
   behavior.
2. The universal threshold-binomial theorem, all quantifiers, the distinction
   between divisibility and equality, exact-order field witnesses, positive
   and zero weights, repeated exponents, parity endpoints, and small `M`.
3. The `M=4`, order-12 lcm counterexample.
4. Exact q-Pochhammer addition identities and the limited leaf-count model.
5. Dense shifted-polynomial coefficient counts and specialization scope.
6. Cyclotomic exponents, equal-floor group count, and the limit of the
   nonconstant-weight argument.
7. The characteristic-zero threshold-root degree bound and its elementary
   totient estimate.
8. The absence of any arithmetic-circuit lower bound or closure of P20's
   evaluator gap.
