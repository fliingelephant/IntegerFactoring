# F59 — Dispersed completion batches and symbolic decoys

**Status:** self-audited finite experiment. The repaired D01/D02 path passed
the hostile source re-audit. The general symbolic-decoy theorem and D03
interpretation are undergoing the separate F60 verification cadence.

**Verdict:** the tested random sources create no square dependency. The tested
offset source creates exact dependencies, including seven beyond the direct
$(N-1)^2$ loop. F59-D03 proves that every dependency in these 12 offset
batches is already a public symbolic square identity with global root. The
source creates algebraic structure, but no factor-specific structure.

This is finite evidence and a structural certificate. It is not a success-
probability theorem and not a factoring algorithm.

## 1. Corrected dispersed-batch replay

F59-D01-R2 uses 12 balanced semiprimes at factor targets 10, 14, 18, and 22
bits and ratios $21/20$, $4/3$, and $7/4$. For each input it runs:

- eight batches of $n^2$ independent unit samples;
- eight batches of $n$ random starts with at most $n$ descent steps; and
- one deterministic batch from starts $N-c$, $1\le c\le n$, with at most
  $n$ steps.

The corrected source gcd-checks the endpoint produced by the last allowed
transition. The runner preserves the source status. F59-A03 pins D01 and R2
and compares all 12 inputs, all 192 child seeds, and every non-direct relation,
metric, rank, kernel, and root field. Everything matches. The direct-event
counts also match: 22 for independent rejection, seven for random tails, and
two for offsets.

The exact rank results are:

- all 96 independent batches have full squareclass rank;
- all 96 random-tail batches have full squareclass rank; and
- the 12 offset batches have total kernel dimension 19.

No tested batch has a useful non-global root.

## 2. Exact offset certificates

F59-D02 records a complete kernel basis for each offset batch.

- Twelve vectors are the forced singleton $(N-1)^2$, one per input.
- Seven additional vectors occur on five inputs.
- The seven supports have sizes $3,3,6,7,3,3,3$.
- Six roots are global $-1$ and one root is global $+1$.
- All seven survive deletion of every global-square singleton relation.
- The same quotient supports survive deletion of the raw path started at
  $N-1$.

The label “arithmetic-only” used by D02 is narrow. It refers to parity of the
retained first numeric endpoint representatives. It does not mean that no
other symbolic endpoint explanation exists. Different offset paths can also
merge into states first reached from $N-1$.

F59-A02 independently reconstructs every trajectory and verifies direct
events, deduplication, supports, relation identities, exact roots, signs,
endpoint parity, loop flags, gcd certificates, and totals. It does not
independently recompute the kernel matrix. The hostile source re-audit supplies
the separate decoder proof.

## 3. Generic-versus-specialized classification

For each selected relation, F59-D03 replaces the fixed input by a symbolic
variable $T$ along the same executed branch. The current value, inverse, and
quotient remain affine polynomials over $\mathbb Q[T]$, and every relation has
the form

\[
A_i(T)=1+T K_i(T).
\]

D03 lifts the complete numeric kernel basis. All 19 basis products are exact
squares over $\mathbb Q[T]$. Sage independently verifies each polynomial
identity. Every root polynomial has constant term $1$ or $-1$, and its
coefficient denominator is coprime to the tested $N$.

Therefore the generic symbolic kernel equals the numeric square kernel on all
12 batches. Since the numeric root map is a homomorphism, every possible
dependency in each batch has global root. Testing another subset cannot help.

The seven residual instances reduce to four symbolic identities. Four copies
share the root

\[
\frac{(T-3)(T-5)(2T-1)}{15},
\]

which has constant term $-1$. The other three roots have degrees 3, 6, and 7,
denominator least common multiples 230, 22533, and 5040, and constants
$-1,+1,-1$.

## 4. What changed

Before D03, the seven residual relations looked like possible source-side
progress. After D03, they are classified as public decoys. A generic identity
whose symbolic root denominator is coprime to $N$ can increase kernel
dimension without carrying information about the hidden factors. A generic
identity with a nonunit denominator is not covered by that conclusion and can
itself expose a factor.

The decoder should therefore keep two spaces:

1. the numeric square kernel; and
2. its certified unit-denominator generic symbolic subspace.

Only the quotient by this certified harmless subspace can contain new factor
information. It can contain specialization-only relations and generic
relations with nonunit denominators. A nonzero quotient is still not
sufficient; its root image must also be non-global.

## 5. Authoritative artifacts

- Repaired replay output:
  `d6a56efdeb8cdebe5253fc0b26c65b6580deef7acc89e4a40cf227cc0311fe79`.
- Offset-certificate output:
  `23c1272fdaebfd932fb727b75d73e47f46b34a0d468b761c39956b9075073b6e`.
- Offset audit output:
  `baae2e6069a0ae702038e9b6f91765338c30591507a409a230308ccdda420cc6`.
- Replay audit output:
  `10a9c0c1e4da7a9c4ade1cdc7b2fc8c1a102fef62a95e8890fd7b4caea0092f4`.
- Symbolic-classification source:
  `5306268bf01ac569f2c75ca0be635dc1b8ed6bffc0065f6a307bbd6abf515d42`.
- Symbolic-classification output:
  `9c62739d882055f480b14b0d2d6b271cb894842c9a07b9d2965220d475d20f84`.
- Hostile repaired-path audit: `SOURCE_REAUDIT.md`.

The initial D01 run, its narrow failed source audit, the corrected replay, the
Sage cache failure, and all three timed-out D03 implementations remain
preserved in the manifest.

## 6. Remaining gap

The current offset sampler has no factor-bearing event in the finite test. The
next source must create a relation outside the certified harmless subspace and
a non-global root, or expose a factor through a symbolic denominator, with an
all-input inverse-polynomial law. Neither property is proved here.
