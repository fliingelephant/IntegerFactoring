# F176 manifest

## Approach-family ID

`F176_hh_two_base_normal_form`

## Artifact type

Proof-only candidate. No registered computation is used as evidence.

## Imported premise

The complete frozen F174 instrumented Harvey--Hittmeir trichotomy, including
its common-state invariant, line-13 prefix facts, factor-first absolute and
relative screens, prime-power scope, and QP cost.

## Question

When the F174 target is the input length \(D=n\), how many line-13 hard
primes can really survive a small exact-integer collision screen?

## Candidate answer

Only two. A polynomial bank of three-smooth integers factors every escape
at a prime at least five. Escape at two is the generic hard branch. Escape
at three forces \(N=2^n-1\); a composite exponent factors immediately, so
the only surviving case is a composite Mersenne number with prime exponent.

This is a stronger source normal form. It does not factor either remaining
hard branch.

## Files

- `STATEMENT.md`: exact normal-form theorem, costs, recursion, and exclusions.
- `PROOF.md`: collision, Mersenne, prime-power, and complexity proofs.
- `SELF_AUDIT.md`: finite-threshold, root-count, scope, and cost checks.

## Required next checks

1. Fresh hostile proof audit against frozen F174 and the primary HH loop.
2. Fresh statement-only reconstruction.
3. Recheck the finite threshold and the strict \(<N\) bank bound.
4. Recheck that beta three has no earlier nontrivial source except two.
5. Recheck complete-factor recursion for repeated prime powers.

No durable proof ledger should be updated before those checks.
