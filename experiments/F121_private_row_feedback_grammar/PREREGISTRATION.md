# F121 preregistered finite computation

## Purpose

The general proof treats `N=2q-1` symbolically. One finite replay is registered
only to compare the declared F116 source and a precisely defined one-step
feedback extension at `N=4033`.

## Fixed input

```text
N = 4033
n = bit_length(N) = 12
B = n^2 = 144
q = (N+1)/2 = 2017
```

## Declared static source

The source is generated without stopping:

1. seeds `2..n`;
2. deterministic seed-endpoint gcd basis and one frozen pair per seed relation;
3. both orientations for each frozen pair and every exponent `0..B`;
4. every unordered seed pair `2<=u<v<=n` in lexicographic order, with both
   orientations and every exponent `0..B`;
5. one global canonical-residue first-occurrence set;
6. global exact-value first-occurrence deduplication after source completion.

The trial and endpoint sign screens are recorded but do not stop this
mathematical no-stop replay.

## Feedback semantics

Two meanings are kept separate.

1. **Recognition only.** Check whether the seed relation for `2` already makes
   `q` a seed-basis block and `(2,q)` a declared frozen pair.
2. **One-step promotion.** After the complete static source, attempt pairs
   `(a,q)` for every seed `a=2..n`, in seed order. For each pair, attempt
   `[a^e q]_N` then `[a q^e]_N` for `e=0..B`, using the existing global
   residue and exact-value sets.

The one-step layer is not part of F116. It is measured as a hypothetical
feedback extension.

## Registered outputs

The computation will record:

- trial factors and all direct sign screens;
- deterministic seed basis and frozen pairs;
- complete static source attempt, residue, and exact-column counts;
- the multiplicative order of 2;
- whether every `(a,q)` word equals the corresponding inverse-power-of-2
  Laurent word;
- new canonical residues and new exact columns from one-step promotion;
- the occurrence count of the `q` valuation row in the static, promoted, and
  full canonical-unit exact-value universes;
- exact prime-parity rank, nullity, every kernel-basis root class, and terminal
  gcds for the static and promoted exact-value matrices;
- the declared `(10,11,e=1)` witness `c=110` separately from feedback.

## Falsifiers

- If `(2,q)` is not already the frozen pair of the seed-2 relation, the
  recognition theorem fails for this witness.
- If any promoted word is not its stated inverse-power-of-2 Laurent word, the
  grammar reduction fails.
- If a second distinct canonical exact value has odd `q`-valuation, global
  privacy fails.
- New feedback columns do not by themselves prove `CLOSE`.
- A square dependency does not prove `ROOT` unless its positive root is
  non-global.
- An existing static witness must not be attributed to feedback.

## Execution contract

Source: `analyze.py`.

Runner: `run_with_timeout.py`.

Named timeout: `F121_TIMEOUT_SECONDS=120`.

Authoritative output: `OUTPUT.json`.

Authoritative log: `RUN.log`.

Every timeout, nonzero exit, malformed output, or failed check is preserved
under a timestamped `FAILED_` filename and recorded in `FAILED_RUNS.md`.
