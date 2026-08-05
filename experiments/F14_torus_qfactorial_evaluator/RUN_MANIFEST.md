# F14 run manifest

## Scope

- Experiment: `F14_torus_qfactorial_evaluator`
- Deliverable type: proof-only narrow obstruction and counterexample
- Canonical project files edited: none
- Files created: `RESULT.md`, `RUN_MANIFEST.md`
- Commit created: no

## Inputs and provenance

- Task statement supplied by the parent agent
- Repository `AGENTS.md` instructions supplied in the task context
- No prior experiment artifact was opened or copied
- No web source was used
- No subagent was used

## Computation

No computational experiment was needed. All claims in `RESULT.md` are algebraic proofs or direct hand-checkable modular calculations. Consequently there are no source programs, timed commands, stdout/stderr logs, or generated numeric output files to record.

## Failed approaches retained in the result

The following mechanisms were investigated and rejected only to the stated scope:

1. Direct q-Pochhammer/q-Barnes addition-law recursion: exact recurrence has two shifted children and linear leaf count.
2. Dense symbolic boundary state: all coefficients are nonzero, giving linear or quadratic materialized state.
3. Single-lcm binomial/resultant: false positive at `M=4`, `a=2` in `F_13`.
4. A polylogarithmic product of threshold binomials: ruled out by the proved `ceil(M/2)` distinct-exponent lower bound.
5. One aggregate per equal-floor cyclotomic group: at least `2 floor(sqrt(M)) - 1` groups, with nonconstant weights inside each group.
6. Explicit characteristic-zero root-set polynomial: degree at least `M^2 / (4(1 + log_2 M))`.

No claim is made that these arguments rule out arbitrary arithmetic circuits or all possible exact evaluators.
