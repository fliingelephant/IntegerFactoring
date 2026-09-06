# F169 kill-first semantic audit

## Verdict

The finite test is meaningful only after five corrections. With those
corrections, the test survives as a clean capability experiment. It is not a
source theorem.

## Naive versions that fail

1. **Exact-value refinement is not endpoint refinement.** F165-D01 refines
   each distinct exact value `A` as one integer. It does not refine the two
   endpoint presentations `z,w` separately. Its reported block splits cannot
   be passed to P154 as feedback-created endpoint blocks.
2. **Exact-value deletion can delete the relevant presentation.** Equal
   products can have different endpoint overlaps. The exact relation ledger
   may delete the later column only after its supplied root is checked. The
   endpoint ledger must keep both occurrences.
3. **A source level cannot consume its own output.** The decorated relation
   basis, candidate order, and endpoint batch must be frozen before a level
   starts. Otherwise the experiment changes the declared depth-two source.
4. **A base-first capped replay ignores new blocks.** If the base pool already
   stores `C+1` fingerprints, a later BFS with the same base-first generator
   order can stop before it uses a feedback-created generator. This is not a
   test of feedback. Each later frozen BFS must put blocks first exposed at
   that level before historical blocks.
5. **Capacity is not growth.** Reaching `C+1` values again proves only the
   same common lower bound. It does not prove an independent quotient
   direction, subgroup enlargement, or a factor.

## Corrected semantics

- Start from the public certified state `g=-1 mod N`, `M=2` on each odd
  input.
- Keep a root-aware, exact-value-deduplicated relation ledger for the section
  source and normalized-root decoder.
- Keep every endpoint occurrence in a separate presentation ledger. Rebuild
  its deterministic gcd-free integer basis after each frozen source level.
- Call a terminal integer block **base-visible** only if the base endpoint
  batch exposed it as a separate block. Call it **feedback-only** if it first
  becomes a separate block after level one or level two. A descendant created
  by splitting an old base block is feedback-only, even if it occurs inside a
  base endpoint.
- Retain old blocks as historical public generators and retain their exact
  decompositions into later terminal blocks.
- Fully saturate the base block pool under P154 before level one starts.
- After a source level is complete, scan all blocks factor-first. On strict
  common-order growth, discard the fingerprint table, keep both ledgers and
  all provenance, and restart the frozen block scan.
- In a later full-pool BFS, order the newly exposed blocks first. Compare each
  candidate fingerprint with every stored fingerprint before global
  deduplication.
- Attribute a later result to feedback only if the replayed factor or
  state-growth word has a nonzero occurrence of a feedback-only block. A
  base-only word found after generator reordering is reported separately.

## Scope that remains after correction

The experiment can show or refute a finite capability claim:

> On this frozen corpus, endpoint feedback supplies a block that makes the
> promoted P154 updater factor or strictly enlarge the certified common-order
> state after the base workflow has saturated.

It cannot show that a repeated capacity certificate is independent. It
cannot show a success density. It cannot prove a quasipolynomial factoring
algorithm.

