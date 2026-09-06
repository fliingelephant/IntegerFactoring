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

`routes.toml` is the authoritative index of conceptual route identifiers.
`experiments.toml` lists every current top-level directory under `experiments/`.
Each experiment ID is derived from the complete existing directory basename.

An experiment has `route_ids = []` when the current registry or its own packet
does not directly support a route assignment. Empty means unresolved. It does
not mean that the experiment has no conceptual relationship to a route.

`route_evidence` contains navigation pointers for recorded assignments. These
pointers document identity only. They do not change the mathematical status of
the cited artifact. Historical instructions inside preserved packets remain
historical instructions.

The order of entries is for reading convenience. Order is never identity.
