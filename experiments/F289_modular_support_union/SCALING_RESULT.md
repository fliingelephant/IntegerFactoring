# F289: affine-patch scaling at \(M=\Theta(N)\)

Status: exact and budgeted finite observations. This is not a uniform node
bound, a fast support claim, or a factoring complexity result.

## Scaling question

For each balanced labelled semiprime, the experiment sets \(M\) to the largest
power of two at most \(N/8\). Thus

\[
\frac{N}{16}<M\leq\frac{N}{8}.
\]

It queries the theorem-relevant dyadic endpoint normals \(a/b=1,2\), followed
by the diagnostic interior ratios

\[
\frac54,\frac43,\frac32,\frac74.
\]

The full \(O(n)\) dyadic menu is needed for unbalanced inputs. This pilot uses
balanced factor ratios in \([1,2]\), so the two endpoint normals are the
relevant dyadic pair.

Each hierarchy node calls the exact one-patch oracle in
F288/PATCH_SUPPORT.py. The heap uses its full tuple
\((aX+bY,XY,X,Y)\) as the node bound. No target leaves are enumerated except
for the separate streaming baseline on the smallest input.

Three stopping events are recorded independently:

1. **Early factor detection:** any returned public point satisfies
   \(XY=N\) with \(X,Y>1\).
2. **1.01-relative support certificate:** for incumbent cost \(C\) and
   minimum live-node objective \(L_{\rm live}\), use the global lower bound
   \(L=\min(C,L_{\rm live})\) and test \(100C\leq101L\). If the heap is
   empty, set \(L=C\).
3. **Exact support termination:** the best-first heap is exhausted.

A query that reaches its 2.5-second or 100,000-node soft limit is recorded as
budget exhausted. Its incumbent, live lower bound, factor event, and relative
certificate remain in the output. It is not classified as a support failure.
The budget gates execute before the live parent is removed from the heap.
After a parent is removed, both children are queried before the next gate.
Thus every successful soft-budget exit retains a complete frontier over all
unresolved subtrees.

## Validation before scaling

On the 18-bit input with \(M=16384\), all six exact hierarchy results matched
the streaming full-union baseline in complete tuple order. The baseline
scanned 3,447 eligible \(x\)-values. Four separate capped node checks had
already matched the geometry route's exact patch oracle.

## Results

| \(N\) bits | \(M=2^k\) | Depth | Formal leaves | Queries | Exact | Budget exhausted | Total nodes | Peak heap |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 18 | \(2^{14}\) | 7 | 64 | 6 | 6 | 0 | 36 | 5 |
| 25 | \(2^{21}\) | 10 | 512 | 6 | 6 | 0 | 364 | 48 |
| 33 | \(2^{29}\) | 14 | 8,192 | 6 | 4 | 2 | 1,834 | 251 |
| 41 | \(2^{37}\) | 18 | 131,072 | 6 | 0 | 6 | 778 | 94 |

All 16 exactly terminated queries returned a proper factor point. No exact
query returned a trivial factor or nonfactor point.

Across all 24 queries:

- 17 detected a proper factor before their final node count;
- one budget-exhausted query had already detected a proper factor;
- 16 obtained a certified 1.01-relative answer, all proper factors;
- four obtained that relative certificate with fewer nodes than their final
  exact run;
- 8 queries exhausted the time budget; and
- no query reached the node limit.

The 18-, 25-, and 33-bit inputs each had at least one early factor, one
1.01-certified factor, and one exact factor result. The 41-bit input had none
within the available time. All six of its statuses are budget exhausted, so
this is an unresolved scaling point.

The 33-bit searches first pruned at depth 5 and accepted their first exact
coarse result at depth 6. Aggregated queried-node counts by depth were

    6, 12, 24, 48, 96, 186, 326, 534, 410, 152, 34, 6.

At 41 bits, the six budgeted searches reached depth 12. Their aggregate counts
were

    6, 12, 24, 48, 90, 164, 264, 104, 52, 10, 2, 2.

No node had yet been pruned or accepted at that input size when the budgets
ended.

## Separation certificate

For

\[
N=8464705853,\quad M=2^{29},\quad (a,b)=(2,1),
\]

the patch oracle returned the proper factor point

\[
(73771,114743)
\]

at depth 7 after 164 hierarchy nodes and 1.316 seconds. Its objective is
262285 and its product is exactly \(N\). Exact support had not terminated
when the query stopped at 397 nodes after 2.502 seconds. This is a concrete
case where public factor detection succeeds before exact support termination.
No 1.01 global certificate had yet been established.

For the same input and normal \((5,4)\), exact support terminated after 369
nodes and 2.446 seconds at the same factor pair. The formal leaf count was
8,192.

## Cost accounting

The 24 queries made:

- 3,012 patch SUPPORT calls;
- 92,877 SEEK calls;
- 3,858,704 NEXT calls; and
- 26,752,556 exact ray casts.

The large gap between hierarchy-node count and primitive calls is retained
explicitly. A small node count does not make the current prototype fast.

The single process stopped at its 26.03-second global soft budget. It did not
hit the 30-second hard alarm. Peak RSS was 21,790,720 bytes, below the 128 MB
cap. The next scheduled factor scale was not started.

## Run provenance

The retained scaling_output.json is the final run. It reports 16 exact and
8 budget-exhausted queries. An earlier live run reported 15 exact and
9 budget-exhausted queries, elapsed time 26.031087 seconds, and peak RSS
22,167,552 bytes. That run was overwritten before the provenance request, so
its full JSON is unavailable. It is not reconstructed. The one-query
difference is consistent with the wall-clock 2.5-second soft gate, but no
claim about the unavailable detailed record is made.

The global-bound labels were corrected after the final run without rerunning
the experiment. The raw final JSON before this metadata-only correction is
retained as scaling_output_pre_bound_label.json. In transformed relative
events, recorded_comparison_objective preserves the old stored value, while
global_lower_objective contains its minimum with the incumbent objective.

## Artifacts

- scaling_support.py: exact and budget-aware source;
- scaling_output.json: per-query milestones, live bounds, depth profiles,
  primitive counts, and representative certificates;
- scaling_output_pre_bound_label.json: unchanged final-run JSON before the
  global-bound metadata correction;
- scaling_run.log: scale timings and stop reason; and
- SCALING_RESOURCE_ESTIMATE.md: resource limits and pre-run snapshot.

Factor labels construct the balanced cases and audit verified product-\(N\)
points after each query. They do not choose moduli, normals, incumbents,
nodes, pruning, or stopping events.
