# Research identifiers

This directory adds stable navigation identifiers. It does not rename, renumber,
or reinterpret historical research artifacts.

## Namespaces

- `route:F12` identifies one conceptual route from the approach table in
  `REGISTRY.md`.
- `experiment:F13_teichmuller_lift_kill` identifies exactly the historical
  directory `experiments/F13_teichmuller_lift_kill`.
- `P...`, `X...`, and `C...` identifiers keep their existing meanings and remain
  unchanged.
- `goal:<name>` and `question:<name>` identify explicit graph goals and open
  obligations. They are not claims that an algorithm or proof exists.

The namespace is mandatory. A bare token such as `F12` is ambiguous because it
can name a conceptual route, a historical run label, or the numeric prefix of an
experiment directory. Use `route:F12` for the conceptual route. Use the full
`experiment:<directory-basename>` identifier for an experiment packet.

## Historical numeric prefixes

An experiment prefix is historical data. It does not determine the conceptual
route. For example:

- `experiment:F12_elliptic_collision_kill` maps to `route:F02`.
- `experiment:F13_teichmuller_lift_kill` maps to `route:F12`.
- `experiment:F16_affine_stabilizer_kill` maps to `route:F13`.

Numeric prefixes can also be reused. The catalog therefore distinguishes
`experiment:F206_beta2_vector_completion_boundary` from
`experiment:F206_joint_halfchild_recursion_torsor` by the complete directory
basename. It never assigns a route from `F206` alone.

## Catalog rules

The schema-3 catalogs use typed record kinds and source selectors. Historical
status text is stored as `recorded_status`, not as a correctness verdict.
`routes.toml` indexes conceptual routes. `experiments.toml` lists every current
top-level experiment directory. Each experiment ID retains its full existing
directory basename. `sync` discovers new entries without inferring route links.

An experiment has `route_ids = []` when the current registry or its own packet
does not directly support a route assignment. Empty means unresolved. It does
not mean that the experiment has no conceptual relationship to a route.

`route_evidence` contains navigation pointers for recorded assignments. These
pointers document identity only. They do not change the mathematical status of
the cited artifact. Historical instructions inside preserved packets remain
historical instructions.

The order of entries is for reading convenience. Order is never identity.

## Stable source selectors

Source references are TOML objects, not `path:line` strings:

```toml
source = { kind = "row", path = "REGISTRY.md", table = "routes", key = "F12" }
route_evidence = [
  { kind = "row", path = "REGISTRY.md", table = "runs", key = "F13-R01" },
  { kind = "field", path = "experiments/F47_teichmuller_cocycle_pooling_kill/RESULT.md", field = "Family" },
]
```

`kind` selects one source type, with only that type's fields:

| Kind | Fields | Selected content |
| --- | --- | --- |
| `record` | `path`, `id` | One complete P/X/C record, by exact ID |
| `row` | `path`, `table`, `key` | One route or run table row |
| `field` | `path`, `field` | One named metadata field with continuation lines |
| `file` | `path` | An explicitly referenced whole document |

The Rust types perform dispatch after input parsing. Unknown kinds, mixed
variant fields, old untagged references, and positional strings are rejected.

`table = "routes"` selects the registry table whose first header is `ID`;
`table = "runs"` selects the table whose first header is `Run`. `key` is the
exact complete first-cell label, including any run or version suffix. These
namespaces remain distinct even if a route and a run share the same label.

`field` selects the exact bold metadata label and its continuation lines, up to
a blank line, another metadata field, or a heading. For example, `field = "Status"` can retrieve
a route declaration that appears on the second line of the status paragraph.

The reader requires exactly one matching row or field. A missing or duplicate
selector is an error. It does not guess a nearby row, use a numeric prefix, or
fall back to a line number. Inserting lines and reordering rows do not change
the target. Intentionally changing a key or field name requires updating its
references. Any displayed line number is a current location hint, not identity.
