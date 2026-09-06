# Integer Factoring Research

The target is an all-input classical Las Vegas factoring algorithm with expected
quasipolynomial bit complexity. [STATEMENT.md](STATEMENT.md) fixes the target.
The repository contains research attempts and partial results, not a completed
algorithm or a verified claim of novelty.

## Start here

1. Read [the current state](research/STATE.md).
2. Read [PROMPT.md](PROMPT.md) before starting an authorized research run.
3. Find relevant records; read their heads before their bodies.

```sh
python3 research/records.py list --kind route --limit 40
python3 research/records.py list --query normalized
python3 research/records.py head P132
python3 research/records.py show P132
python3 research/records.py head route:F12
python3 research/records.py head experiment:F13_teichmuller_lift_kill
python3 research/records.py check
```

The reader requires Python 3.11 or newer and uses only the standard library.
See `python3 research/records.py --help` for filtering and catalog maintenance.
Run `build` after changing P/X/C ledger sections, then run `check`. The route
and experiment catalogs are explicit metadata; update them when adding a route
or packet. The checker detects missing packets, stale sections, duplicate IDs,
and invalid links.

## Progressive reading

The TOML catalogs in `research/` provide a small navigation layer. Mathematical
bodies remain in their existing files. A head helps select material; it does
not replace the exact statement, its assumptions, or a proof. A missing or
unreviewed scope requires reading the body before using the result.

- [Routes](research/routes.toml): conceptual mechanisms.
- [Experiments](research/experiments.toml): historical packets and supported
  route mappings.
- [Results and notes](research/catalog.toml): P/X/C records by stable ID.
- [Identifier rules](research/IDENTIFIERS.md): namespaces and historical aliases.
- [Evidence provenance](research/PROVENANCE.md): retained sources and known gaps.

At the 2026-09-06 cleanup checkpoint, all 498 historical packets are indexed. The available records
directly support 192 route assignments; 306 remain explicitly unresolved.
An unresolved route does not prevent opening a packet and is not a negative
mathematical result. Do not infer a route from its experiment number.

`REGISTRY.md`, `PROVED.md`, `FAILED.md`, and `notes/Progress.md` are historical
ledgers. Their labels and research recommendations are records of earlier work,
not instructions or independent mathematical certification. In particular,
`FAILED.md` includes execution and verification failures, and the old
`Current synthesis` is not the latest entry point. Use the catalogs rather than
reading these ledgers in full at every restart.

## Sources and evidence

[Zhihu](notes/Zhihu.md) supplies motivation and technical seeds; its claims are
not assumptions. [Inspirations](notes/Inspirations.md) is an optional idea pool.
The [feedback brief](FEEDBACK_ROUTE_RESEARCH_BRIEF.md) describes an earlier
research stage. Experimental programs, reports, logs, and exact certificates
remain under `experiments/`.

Repository content is written in English. Preserve evidence, keep identifiers
stable, and distinguish mathematical results from finite observations and
execution status. Runtime caches are ignored; they are not research evidence.
