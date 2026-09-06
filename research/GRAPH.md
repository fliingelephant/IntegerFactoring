# Research graph

The graph is a partial navigation aid. Catalog records are its nodes;
`graph.toml` adds named goals and questions where needed. Relations have explicit
sources but are not a new mathematical audit. Missing edges are unknown. They
do not mean that a result is independent or a goal is solved.

## Relations

| Relation | Meaning of `from -> to` |
| --- | --- |
| `uses` | The source explicitly uses the target's premise, definition, or result. |
| `requires` | The source goal or question needs the target obligation resolved. |
| `supports` | The source supplies evidence for the target within the recorded scope. |
| `refutes` | The source contradicts the target's exact claim within the recorded scope. |

`uses` and `requires` form the dependency DAG. The checker rejects cycles in
that subset. Evidence links may have cycles. Support is not proof, and a failed
program or finite null search is not a general refutation.

Every edge needs source evidence. Neither `sync` nor search creates edges from
ID mentions. Verify the exact scope before recording a relation. The tool does
not propagate certainty or close research directions automatically.

## Conditional results and missing obligations

The initial graph includes one example plan, `goal:normalized-route`. It uses
P230's conditional splitter while separately requiring a fast evaluator and an
all-input extension. P230 itself is not marked as requiring the existence of
its assumed evaluator. P231 is not recorded as refuting every evaluator. This
example does not select the route over other directions.

Other initial links include the explicit P110/P109 and X01/P01 uses, and the
fixed-input matrix evidence supporting P24. They do not make the graph a
complete account of the imported corpus.

## Queries

```sh
./target/release/research graph goal:normalized-route
./target/release/research graph question:normalized-evaluator --reverse
./target/release/research graph P24 --format json
./target/release/research graph --format mermaid
```

A targeted query shows the recorded dependency slice and relevant evidence.
`--reverse` follows affected downstream records. With no ID, the tool exports
the explicit graph rather than every isolated historical record.

## Add a relation

```toml
[[edges]]
from = "P110"
to = "P109"
relation = "uses"
evidence = [{ kind = "record", path = "PROVED.md", id = "P110" }]
note = "Append monotonicity extends the verified prefix root on the specified input."
```

Use existing record IDs instead of duplicate claim nodes. Give new goals and
questions stable `goal:<name>` and `question:<name>` IDs, a clear title, a source,
and any needed scope. Run `check` after editing. Unknown endpoints, duplicate
edges, missing evidence, and dependency cycles must be resolved.
