# Research State

Navigation snapshot: 2026-09-06. This page summarizes the existing records. The
cleanup did not re-prove their mathematical claims or establish their novelty.

The Rust reader now provides typed catalog and graph queries. The initial
[graph](graph.toml) records a few explicit relations and one conditional route
plan; it is not a complete dependency map or a choice of research direction.

## Target and completion

Read [STATEMENT.md](../STATEMENT.md) for the exact all-input classical Las Vegas
quasipolynomial factoring target and bit-cost conventions. No complete solution
meeting that target is established by this repository.

No new preferred mathematical route was selected during cleanup. Earlier
rejections apply only to their exact hypotheses and computational models.

## Main research stages

| Stage | What the records study | What remains missing |
| --- | --- | --- |
| Retained relations and integer feedback | Canonical inverses, gcd-free refinement, and jointly useful square relations; `route:F26` and the feedback brief | A public, affordable source with an all-input useful-relation guarantee |
| Integer words and order residuals | P205/P206 reduce selected semiprime tasks to constructing factor-correlated integer words | A uniformly affordable source and a sufficient success law; a reduction does not supply that source |
| Compressed arithmetic evaluation | P230 and the [random-shift packet](../experiments/F282_shifted_normalized_difference_random_splitter/STATEMENT.md) give a conditional splitter for balanced distinct odd semiprimes | The fast normalized-difference evaluator, plus an extension or reduction to the full input class |
| Boundaries of named evaluators | P231 and the [evaluator-boundary packet](../experiments/F283_shifted_normalized_difference_evaluator_boundary/STATEMENT.md) analyze specific representations for P230 | The record explicitly leaves other evaluators open; it is not a general circuit lower bound |

The older synthesis at the start of `notes/Progress.md` centers on P203-P207.
Later sections reach C242/P231. The August feedback brief is useful historical
context, not a current roadmap.

## What computation already did

- The [Pell word scan](../experiments/F255_pell_resultant_word_anomaly_search/RESULT.md)
  recorded 50,304 remote inputs over a fixed word menu.
- The [symbolic-search audit](../experiments/F263_hypergeometric_evaluator_symbolic_search/V2_RESULT_AUDIT.md)
  covers symbolic and numerical discovery and explains
  the recorded finite hits using a boundary mechanism.
- The [retained-bank run](../experiments/F268_canonical_scalar_section_multirow_v4/results/F268-D04_run_20260814T0442Z/RESULT.md)
  tested retained relations, including held-out cases.
- Several other packets stopped during setup or preflight. Such failures are
  not mathematical counterexamples.

These are pointers for selective reading, not independent validations or
evidence of all-input complexity. Use the experiment catalog to locate packets.

## Next research cycle

The Astra root performs creative mathematics and can assign bounded mathematical
gaps to Astra subagents. Turning a pattern into a theorem or proving a missing
key lemma remains creative work even when the statement is precise. Sol max
workers navigate records, implement and run Astra-designed searches, reproduce
results, and verify supplied arguments within resource budgets. They return
tasks that need new mathematical ideas to Astra. Blind reconstruction is
optional and defaults to Sol max. A promising finite pattern can justify
investigation before a full algorithm or QP transition exists.

Before relying on an old result, retrieve the exact statement and scope. Before
closing a mechanism, check that the obstruction covers the proposed mechanism.
Use `PROMPT.md` for the full research workflow.

After each substantive cycle, replace the active question, latest finding,
next action, and unfinished-task information here. Do not wait for a manual
pause before making the state safe to resume after context compaction.
