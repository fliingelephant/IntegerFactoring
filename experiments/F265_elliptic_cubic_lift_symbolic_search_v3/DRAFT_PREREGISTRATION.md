# F265-D03 draft preregistration: fixed mixed cubic-row bank

## Status

This is an unfrozen preregistration draft. It has not passed a hostile audit.
No C++ source, runner, frozen manifest, local execution, or remote execution
exists or is authorized.

## 1. Finite question

For the fixed public `U + POWER` two-curve bank, after every direct public
screen, saturated private-primary peeling, and complete P66 decoding of the
residual core, does the quotient by all support-one and support-two square
relations contain a verified relation with a non-global normalized root?

The search also records useful low-support relations separately. It asks a
finite question. It makes no probability or all-input claim.

## 2. Immutable source proposal

Use the F265-D02 public curve construction, affine arithmetic, row law, and
factor-label firewall. Use two curves per modulus:

- curve 0: `U`, with domain tag `100`;
- curve 1: `POWER`, with domain tag `108`.

Use a new master seed and new split domains. The exact seed is to be chosen
before freezing. Reject a literal duplicate public seed tuple. Use

\[
 K=\min(2\lceil\log_2(N+1)\rceil,160)
\]

and retain every index from 1 through `K`. There is one bank per modulus and
no discovery family ranking.

The discovery and held-out cohorts remain disjoint and keep the D02 cells:

- factor bits `12,16,20,24,32,40,48,60`;
- shapes `random,neighbor,safe`;
- 16 distinct moduli per cell and split.

Each split therefore intends 384 moduli. Hidden factors remain outside all
curve, row, decoder, counter, and result-selection code until public
evaluation has ended.

## 3. Complete screen chronology

For every bank, use this order.

1. Generate both curves with the D02 discriminant screens.
2. Generate both complete affine orbits with factor-first denominator and
   row-root screens.
3. Run every singleton exact-square comparison.
4. Run every unordered row-pair `x` difference and signed-`y` gcd.
5. Run every same-curve chord-expression gcd with `N`.
6. Run equal-row and inverse controls.
7. Run the complete support-two square test from `DRAFT_ALGEBRA.md` and both
   normalized-root gcds for every hit.
8. Run the canonical saturated private-primary peel to a fixed point.
9. Run the complete P66 decoder on the residual active set.
10. Verify every low-support generator and every canonical quotient basis
    relation by an exact integer product square and both signed gcds.
11. Emit the bounded relation-local diagnostics. Diagnostic work is
    non-gating.

A proper factor is recorded. Once both complete orbits exist, later exact
screens and P66 still finish so that the bank evidence is complete. An orbit
that stops before its scalar limit is incomplete and never reaches P66.
The support-one and support-two vectors are enumerated on the full bank.
Private-pivot rows cannot occur in any such vector, so restricting the list
to the fixed-point core gives exactly the same low-support subspace used in
the quotient.

## 4. Canonical peeling and decoder

At each peel round, compute all saturated residuals from the same active set.
Delete every nonsquare residual simultaneously. Serialize, for each deleted
row, its round, `g_i`, `b_i`, the exact identity `a_i=g_i*b_i`, and the
nonsquare-test result. Serialize the active set after every round.

The fixed point has at most 64 rows. If it has more, report
`RESOURCE_REJECT_RESIDUAL_CORE`; do not run a partial decoder and do not count
the bank as eligible.

For a core of at most 64 rows, run the full P66 gcd-free refinement. Keep the
D02 requirements:

- pairwise-coprime final opaque blocks;
- exact row reconstruction;
- exact-square status for every block;
- complete parity matrix and canonical kernel basis;
- exact product-square verification for every reported basis vector; and
- both normalized-root signed gcds.

Use the original row order with zeros inserted at peeled coordinates. The
low-support span and quotient complement use the canonical RREF rules in the
algebra draft. A claimed residual relation is one outside the complete
support-at-most-two span, not merely a relation whose displayed basis vector
has support at least three.

## 5. Result counters and diagnostics

The primary bank counters are:

- complete bank;
- eligible bank;
- direct factor and first direct screen;
- peel rounds and peeled rows;
- residual-core size;
- full kernel dimension;
- low-support dimension;
- quotient dimension;
- useful low-support relations;
- useful quotient-basis relations; and
- strict useful quotient-basis relations.

`strict` means that the complete orbit and all earlier direct and low-support
screens found no factor. A useful relation always carries its exact positive
root, supplied modular root, normalized root, and proper signed gcd.

For explanatory output only, process the first eight quotient-basis vectors
of support at most 16. Run every same-curve pair and unordered third-row test
inside each selected support. Record tangent, chord, discriminant, third-root,
and frozen scalar-index predicates. Diagnostic limits cannot cause resource
rejection and no diagnostic counter enters a result label.

## 6. Held-out labels

There is no family selection file. Discovery is exploratory and cannot alter
the held-out grammar.

The held-out result is `finite_positive_signal` only if at least two strict
useful quotient-hit banks occur in at least two factor-size cells.

It is `finite_null_signal` only if:

- no held-out bank has a strict useful quotient relation;
- at least 90 percent of the 384 intended held-out banks are eligible; and
- every factor-size/shape cell has at least 12 eligible banks.

All other outcomes are `finite_mixed_or_inconclusive`. Useful support-one or
support-two factors are reported, but do not by themselves satisfy the
residual positive label.

## 7. Exact maximum task counts

For a declared factor-bit size `b`, use the upper bound `n<=2b`. The proposed
maximum rows and unordered pairs per bank are:

| factor bits | `K_max` | rows | unordered pairs |
|---:|---:|---:|---:|
| 12 | 48 | 96 | 4,560 |
| 16 | 64 | 128 | 8,128 |
| 20 | 80 | 160 | 12,720 |
| 24 | 96 | 192 | 18,336 |
| 32 | 128 | 256 | 32,640 |
| 40 | 160 | 320 | 51,040 |
| 48 | 160 | 320 | 51,040 |
| 60 | 160 | 320 | 51,040 |

Across both splits there are at most 96 banks at each factor size. Therefore
the full packet has these exact registered maxima:

- 768 banks;
- 172,032 admitted rows;
- 22,032,384 unordered row pairs;
- 10,973,184 same-curve pairs;
- 11,059,200 cross-curve pairs;
- 66,097,152 coordinate gcds from three gcds per unordered pair;
- 10,973,184 direct same-curve chord gcds;
- 51,360 peel row-round tests per maximum-size bank;
- 115,520 bits in a maximum active product;
- 64 residual rows and 23,104 residual row bits per eligible decoder; and
- 3,440,640 diagnostic triples over the full packet.

The pair loop also performs the complete support-two test. The exact number
of square hits is data-dependent. The listed pair maximum does not hide a
second pair scan.

Retain the D02 four-hour common deadline, 12,600-second projected experiment
gate, 4 GiB virtual-memory limit, 3.5 GiB measured peak-RSS gate, 1 GiB total
output cap, 768 MiB projected experiment-output gate, eight-worker maximum,
`nice 15`, host-load gate, memory gate, disk gate, and five-minute finalization
reserve. D03 does not relax a D02 gate.

## 8. D02 evidence and cost comparison

The authenticated D02 nine-case preflight observed:

- 18,790 generated rows;
- 2,369,895 pair controls;
- 41,719 gcd-free splits;
- 9,450,761 chord-pattern operations;
- 36 banks rejected only by `CHORD_PATTERN_CAP`; and
- zero P66 relations.

The retained block evidence gives a sharper heuristic fact. Every one of the
18,670 rows in the 105 banks that reached the decoder had a nonsquare opaque
block with odd exponent incident to that row alone. Thus the kernel was
already provably zero in every decoded preflight bank. D02 nevertheless ran
the bank-wide chord diagnostic before it inspected the empty kernel. This is
discovery evidence, not a theorem about D03 cohorts.

D02's audited planned full-work proxy was `1,523,265,600`. The D03 maximum
sum of `rows^2` over the fixed 768 banks is `44,236,800`, a ratio of
`0.0290408`. Applying that ratio to D02's already 1.75-safety-multiplied
projection gives `9,734.44` seconds. Adding a further 25 percent redesign
reserve gives `12,168.05` seconds, below 12,600 seconds.

This comparison is not a runtime bound. The work units mix different
big-integer operations, and the D03 peel has not been timed. It only shows
that the fixed mixed bank is a credible preflight candidate. No launch is
permitted unless the new executable's own frozen projection passes every
gate.

## 9. Smallest proposed preflight certificate

After a hostile theory audit and a separate hostile source audit, the
smallest admissible dynamic preflight is:

1. generate one deterministic 60-bit modulus for each of `random`,
   `neighbor`, and `safe`;
2. evaluate the complete 320-row mixed bank for each shape;
3. require all three banks to finish every direct screen, fixed-point peel,
   and complete residual P66 path, or fail the preflight;
4. record generation wall/CPU time separately from evaluation wall/CPU time;
5. record every exact task counter in Section 7, peak RSS, and output bytes;
6. project the full 768-bank packet from exact registered task ratios; and
7. apply the unchanged 1.75 safety multiplier and all D02 gates.

The three maximum-size real banks are one certificate unit. A direct or
incomplete first candidate does not silently become a cheap timing sample;
the deterministic preflight case stream advances, under a frozen attempt
cap, until it obtains one complete maximum bank per shape. Exhaustion fails
the preflight. The preflight may not open discovery or heldout on failure.

Because a real three-bank sample cannot prove a worst-case residual-core
distribution, every production bank retains the 64-row residual cap and all
decoder work caps. A cap crossing is explicit and reduces eligibility. The
90-percent and cell-floor rules prevent such rejections from becoming a
false finite null.

## 10. Audit gate

Before any source is written, a fresh no-context hostile theory review must
try to kill:

- valuation saturation;
- simultaneous peel determinism;
- the kernel isomorphism at each round;
- completeness of the support-two criterion and quotient;
- normalized-root completeness of the quotient basis;
- diagnostic noninterference;
- exact task totals;
- residual-cap semantics; and
- the distinction from P217 and P20.

A passing theory review authorizes drafting source only. It does not authorize
compilation, preflight, or remote execution.
