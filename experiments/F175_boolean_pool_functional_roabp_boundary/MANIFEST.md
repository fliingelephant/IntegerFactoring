# F175 manifest

## Purpose

F175 reopens P34 only under the new quasipolynomial target. It asks whether
the exact Boolean many-relation product can be compressed by a one-pass or
separated functional representation. The candidate theorem proves an exact
exponential singleton-cut rank over each P34 hidden field.

## Current status

**Candidate after one hostile audit; repair re-audit pending.** The hostile
audit passed the core theorem and proof. It required two scope corrections:
the cube-Laplacian power-of-two normalization and wording that had made the
verified two-block construction sound like a general resultant lower bound.
Both corrections, plus two recommended definition clarifications, were made
after the audit. A focused audit of this repaired version is still required.
Statement-only blind reconstruction has not started.

No computation was run. No finite evidence is claimed. No durable ledger was
edited by this candidate packet.

## Repaired candidate hashes

- `STATEMENT.md`:
  `5119a4ba746b40b17f4b1a886fb660ef0463803298c281b36c529b7e55116bfe`
- `PROOF.md`:
  `eddfc89e8b3e3284e023a07ecff5874f012626d44cc117935368ba9e9c73b0d5`
- `SELF_AUDIT.md`:
  `a3a8ce7f4c083b349cc9b4d186a68e859c7df72f639709f37941c83fde60f984`
- initial `HOSTILE_AUDIT.md`:
  `edadacf4b177955199d367f05f5ed01724e6f31cbdb962883ba5658b32e8a169`

The initial audit records the pre-repair hashes separately. Its mathematical
rank audit remains evidence for the unchanged core proof, but the protocol
status stays candidate until the repaired files receive a focused re-audit.

## Exact candidate claim

For

\[
Q_K=\prod_{\varnothing\ne S\subseteq[K]}\sum_{i\in S}X_i,
\qquad d=2^{K-1},
\]

and every prime `r>d`, the function matrix across each singleton-variable
cut has rank exactly `d`. Hence every exact functional ROABP in any variable
order, even with arbitrary nonuniform univariate layer functions, has width
at least `d`. The corresponding one-pass linear-state, tensor-train,
single-variable-leaf tree-tensor, and exact separated-sum bounds follow.

For P34, `r>2^K` and `K=Theta(n)`, so this width is exponential in `n`, not
quasipolynomial.

## Scope exclusions

F175 is not a bit-time lower bound. It does not close general multipass
arithmetic circuits, implicit exponential-width state, global determinants,
Moore/Frobenius alternatives, branching or denominator factor screens,
random-input evaluators, alternative local-zero observables, or gcd-only
detectors. The general P34 QP evaluator remains open.
