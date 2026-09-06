# Integer Factoring Research

The target is an all-input classical Las Vegas factoring algorithm with expected
quasipolynomial bit complexity. [STATEMENT.md](STATEMENT.md) fixes the target.
This repository contains attempts and partial results, not a completed
algorithm or a verified novelty claim.

## Start here

1. Read [the current state](research/STATE.md).
2. Read [PROMPT.md](PROMPT.md) before starting an authorized research run.
3. Use the Rust reader to find records, inspect heads, and open relevant bodies.

```sh
cargo build --release --locked --jobs 1
./target/release/research list --kind route --limit 40
./target/release/research list --query Frobenius --kind result
./target/release/research head P132 --json
./target/release/research show P132
./target/release/research graph goal:normalized-route --format mermaid
./target/release/research check
```

Use `--help` for options. `list`, `head`, `show`, `sync`, and `check`
support JSON output for agent tooling. Dependencies are pinned in `Cargo.lock`.
The runtime needs no Python, database, server, or model API.

## Read progressively

The TOML catalogs are the navigation layer. Original mathematical bodies remain
in their existing files. Search can inspect bodies without printing them in
full. Heads expose recorded metadata; `show` retrieves the original text.
Missing scope is unknown, not permission to generalize a result.

- [Records](research/catalog.toml): P/X/C statements and notes.
- [Routes](research/routes.toml): conceptual mechanisms.
- [Experiments](research/experiments.toml): packets and supported route mappings.
- [Graph](research/graph.toml): selected dependencies, obligations, and evidence.
- [Identifiers](research/IDENTIFIERS.md): stable IDs and source selectors.
- [Graph guide](research/GRAPH.md): relation meanings and queries.
- [Provenance](research/PROVENANCE.md): retained sources and known gaps.

The imported corpus has 563 records, 32 routes, and 498 experiment packets.
There are 192 supported packet-to-route assignments and 306 explicit unknowns.
Unknown relationships do not prevent reading a packet and are not negative
mathematical results. Do not infer a route from an experiment's numeric prefix.

`REGISTRY.md`, `PROVED.md`, `FAILED.md`, and `notes/Progress.md` retain
historical labels and recommendations. These are data about earlier work, not
current instructions or independent mathematical certification. The old
`Current synthesis` is not the restart entry point.

## Record new work

Workers write their assigned packets. The root, or one designated record keeper,
merges records and updates shared catalogs. Keep IDs stable and unique.

Use `## P<number> -- Title` in `PROVED.md`, `## X<number> -- Title` in
`FAILED.md`, and `### C<number> -- Title` in `notes/Progress.md`. Preserve
existing zero-padded IDs. Include an exact statement, recorded status, scope,
proof or observation, and evidence. A malformed record heading is an error.

```sh
./target/release/research sync
./target/release/research check
cargo test --locked --jobs 1
```

`sync` regenerates record metadata and discovers new route rows and experiment
directories. It preserves existing supported mappings and marks new packet
assignments as unknown. It does not infer mathematical graph edges. Add these
to `research/graph.toml` only with explicit sources and scope.

After each substantive research cycle, refresh `research/STATE.md` with the
current question, latest result, next action, and unfinished tasks. Keep it
short instead of appending another historical ledger.

## Sources and evidence

[Zhihu](notes/Zhihu.md) supplies motivation and technical seeds, not assumptions.
[Inspirations](notes/Inspirations.md) is an optional idea pool. The
[feedback brief](FEEDBACK_ROUTE_RESEARCH_BRIEF.md) describes an earlier stage.
Programs, reports, logs, and certificates remain under `experiments/`.

Repository content is written in English. Structural validation does not prove
mathematical claims. Runtime caches and Rust build products are ignored.
