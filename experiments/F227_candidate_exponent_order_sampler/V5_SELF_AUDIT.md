# F227 V5 self-audit

## Verdict

**PASS at self-audited V5 status. Do not promote.** V5 repairs the sole V4
hostile-audit failure. It restores the upper-bound relation in (B6). No
fresh hostile re-audit, blind statement reconstruction, cross-family audit,
or human audit has run on V5.

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, public-web search, or numerical fit was used.

## Predecessor integrity

Before writing V5, I recomputed the SHA-256 hashes of all six V1 files, all
six V2 files, all six V3 files, and all six V4 files, including every
hostile FAIL. Every hash matched its frozen identity. No predecessor file
was edited.

## Exact repair audit

The V4 hostile re-audit found one false frozen assertion. V4 said that every
`Q`-diffuse bank “has total useful probability” equal to

\[
Q(n)2^{-c_0n}.
\]

That equality is false because the definition permits fewer than `Q(n)`
trials and different banks have different useful probabilities. V5 restores
both parts of the intended upper-bound syntax:

1. the prose says “at most”; and
2. (B6) explicitly states

\[
\Pr(\text{at least one useful trial})
\le Q(n)2^{-c_0n}=2^{-\Omega(n)}.
\]

This is exactly what the unchanged proof establishes. Conditional on every
reachable no-progress history, (B5) bounds the next trial by
`2^(-c_0 n)`. Summing these conditional bounds over at most `Q(n)` trials
gives (B6). Cross-trial independence is not needed. Since the one fixed
envelope is subexponential in `n`, the product is `2^(-Omega(n))`.

The V5 statement otherwise changes only version and repair-status prose.
The V5 proof changes only its version number in the title. Every
mathematical definition, premise, equation other than the repaired (B6)
display, proof step, scope exclusion, and remaining gap is identical to V4.

## Regression audit

The V4 hostile re-audit passed all of the following, and V5 does not change
them:

1. the AP gcd mean, including soluble-class endpoints and nonuniform laws;
2. the exact one-trial fresh-uniform-base upper bound;
3. the fixed-base return progression and exact stale classification;
4. the residual-order floor bound;
5. the geometric reach-tail cost without success-cost independence;
6. the exact same-size potential, including the final state;
7. the P161 rough-descendant transfer; and
8. the external all-input-oracle boundary and every cost multiplicity.

In particular, `FactorAll` remains explicit and external. Its uniform
all-input expected-cost bound is `F_all`. Equation (C9) remains an
oracle-relative current-node estimate. It is not a recurrence, it is not
unrolled, and it implies no numerical-QP all-input factoring theorem.

## Remaining gaps

1. No certified inverse-QP source of suitable nonstale bases is known.
2. No correct all-input dispatcher with a proved uniform QP cost is known.
3. A randomized source still needs capped batching or another recognizable
   success rule.

A fresh hostile re-audit and, only after a hostile PASS, a strict
statement-only reconstruction remain required before promotion.
