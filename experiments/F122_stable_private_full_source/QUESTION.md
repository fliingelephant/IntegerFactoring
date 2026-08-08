# F122 Preregistered Diagnostic — Stable Private Row Versus CLOSE and ROOT

## Fixed input

```text
N = 2,000,887,089,301
p = 1,000,289
q = 2,000,309
n = 41
B = n^2 = 1,681
r = (N+1)/2 = 1,000,443,544,651 prime
```

F120 proves that row `r` occurs to odd valuation in the seed-`2` exact value
`N+1=2r` and is private against every canonical exact-value column.

## Question

Determine `CLOSE` and `ROOT` for the complete fixed F116/F118 source while
that universe-private column is present.

The diagnostic must answer separately:

1. Does the globally exact-value-deduplicated matrix have a nonzero kernel?
2. Does its complete fundamental kernel basis have nonzero normalized-root
   image modulo the global signs?
3. Does every basis dependency exclude the private seed-`2` column?
4. Does any direct residue or endpoint sign screen find a proper factor?

This is a finite separation test. It is not an asymptotic theorem.

## Exact no-stop source

Use this order without a success stop:

1. seeds `2..n`;
2. the deterministic F116 seed-endpoint gcd/perfect-power basis;
3. both trajectories of all frozen seed-basis pairs for exponents `0..B`;
4. every unordered seed pair `2 <= u < v <= n` in lexicographic order;
5. both residues `[u^e v]_N` then `[u v^e]_N` for `e=0..B`.

Apply one global canonical-residue first-occurrence set. Run every direct gcd
screen on each new residue and record every proper event, but never stop.

For the parity matrix, apply one global positive-exact-value first-occurrence
set after the residue screens. Remove `P=1`.

The exact attempt count is

```text
40 + 40*2*1682 + binomial(40,2)*2*1682 = 2,758,520.
```

## Decoder

Factor the retained endpoints with proof-enabled Sage/Pari assistance. Use
the hidden odd prime-valuation rows.

For a factorization `P=product prime^e`, initialize the positive half-root as

```text
product prime^floor(e/2) mod N.
```

During binary elimination, multiplying two parity expressions multiplies
their half-roots and one copy of every prime in the intersection of their odd
supports. Every zero reduction is one fundamental basis dependency. Classify
its exact positive root as `+1`, `-1`, or non-global modulo `N`.

Track the seed-`2` coordinate through every pivot combination. A singleton
private row forces that coordinate to be zero in every dependency.

## Registered execution contract

- Corpus: `CORPUS.json`.
- Source: `scan_complete_source.py`.
- Runner: `run_with_timeout.py`.
- Named timeout: `F122_STABLE_PRIVATE_FULL_SOURCE_HARD_TIMEOUT`.
- Hard timeout: 900 seconds.
- Authoritative output: `OUTPUT.json`.
- Authoritative log: `RUN.log`.
- Final manifest: `MANIFEST.md`.
- Failed attempts: timestamped `OUTPUT_FAILED_*` and `RUN_FAILED_*` files.
- Sage cache: experiment-local `.sage` from the first run.

The source, corpus, runner, timeout, and artifact names must be pinned in
`REGISTRATION.json` before execution.

## Falsifiers and boundary

- Do not stop after a direct factor or non-global root.
- Raw residue duplicates do not enter the matrix twice.
- Distinct residues with the same positive exact value do not enter the
  matrix twice.
- Kernel nullity does not imply nonzero root image.
- One non-global basis root proves `ROOT` but does not explain an asymptotic
  law.
- If a direct screen or `ROOT` factors this input, the feedback gate is
  closed.

No durable ledger will be edited.
