# F174 manifest

## Approach-family ID

`F174_instrumented_hh_prime_escape`

## Artifact type

Proof-only candidate. No computation was run.

## External premise

Harvey--Hittmeir Algorithm 3.1 and its stated complexity and smooth-number
lemma from arXiv:2601.11131v2:

<https://arxiv.org/html/2601.11131>

## Question

What exact reusable output does a QP-target Harvey--Hittmeir run provide
when combined with P150/P154 factor-first order screens?

## Candidate answer

For every odd composite, it gives a factor, a factored exact common-order
state larger than the target, or an algorithm-selected prime hard block. A
truncated smooth-prefix argument forces the last prime to have value
\((\log D)^{O(1)}\), hence \((\log n)^{O(1)}\) for a QP target. The hard
block has one local absolute primary component above \(D\) and local quotient
order above \(C\) in every hidden prime-power component.

This is a source and classification theorem. It does not factor the hard
branch.

## Files

- `STATEMENT.md`: frozen theorem, exact outcomes, cost, and exclusions.
- `PROOF.md`: exit audit, common-state invariant, smooth cutoff, and
  factor-first classification.
- `SELF_AUDIT.md`: prime-power, quantifier, cost, and scope checks.

## Required next checks

1. Fresh hostile proof audit against the primary Algorithm 3.1 text.
2. Fresh statement-only reconstruction.
3. Recheck the constants in the smooth-prefix cutoff.
4. Recheck every small-input, prime-power, and line-13 exit.
5. Confirm that QP means numerical scan length, exponent bit length, and
   complete provenance all remain within one fixed QP bound.

No durable proof ledger should be updated before those checks.
