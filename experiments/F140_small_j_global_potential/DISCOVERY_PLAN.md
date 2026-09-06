# F140-D01 preregistration — small-quotient path discovery

## Closest prior route and material difference

The closest boundaries are X73--X77 and P120--P125.  P124 proves only that
one released transition recenters at a small quotient or descends at a large
quotient.  It does not control repeated small-quotient interruptions.  This
finite search differs only by following several exact canonical transitions
while enforcing endpoint screens, exact-value deduplication, and parity-rank
independence.  It is discovery or counterexample evidence only.

## Frozen source

- Source: `search_paths.sage`
- Corrected authoritative SHA-256:
  `6188ef3ce918b4769d948267d7dfe34b422aebc27f8c3c34a87cb229ca3b9a04`
- Preserved JSON-only correction SHA-256:
  `a2168bfeaa968dc7b56c185918cb0f820b9d477e426e80de5903d2412916a043`
- Preserved first-run SHA-256:
  `2ebdcdec4bf45d8c12f7c5709315a347a4adedd16c54c1ebf520d92143b686e9`
- Timeout: 300 seconds
- Log: `RUN.log`
- Machine-readable output: `OUTPUT.json`

The authoritative command is:

```text
gtimeout 300 sage experiments/F140_small_j_global_potential/search_paths.sage
```

Its standard output is also written to `RUN.log` by the shell runner.

The first unrestricted run of the preserved source completed the search but
failed during JSON serialization.  `RUN_CODE_FAILED.md` records that failure.
The next run exposed a Sage-preparser XOR error and is preserved in
`RUN_LOGICAL_FAILED.md`.  The final source uses `operator.xor`, converts
configuration and score values to Python integers, and hashes the registered
`.sage` file.  It does not change a corpus or path criterion.

## Frozen corpus and path criteria

The corpus consists of all balanced products (N=pq), where (p<q<2p)
and (p,q) are distinct primes in `[11,97]`.  The anchor caps are
(C\in\{5,7,11\}).  The script uses prime anchors at most (C).

For each unit state (s<N/C), it computes the least positive inverse, its
exact carry, every nonzero induced anchor digit, and both canonical
endpoints.  It discards a source position if either endpoint sign screen
gives a proper factor of (N).

A path must satisfy all of these conditions:

1. every transition obeys the exact P124 divisor-carry law;
2. every retained carry is new, so exact-value deduplication does not remove
   a path column;
3. every active state is new;
4. every appended exact-value parity column increases binary rank, so the
   selected path has zero kernel and no normalized root to test;
5. the depth is at most 10.

Two release modes are frozen:

- `conditional_releases`: a prime factor of the current retained reciprocal
  endpoint satisfies the P124 size bound.  This tests the path dynamics but
  does not claim that the factor is publicly isolated.
- `public_releases`: an exact gcd of the current reciprocal endpoint and a
  different endpoint in the same complete anchor star gives the released
  integer.  This is a factor-free public release certificate.

The lexicographic score is:

```text
(path length, exact alternation flag, number of small/large alternations,
 all-small flag, number of small quotients, number of large quotients).
```

The search stops after 250,000 DFS expansions per `(N,C,mode)` and records
the cap flag.  A finite witness can refute a universal local claim at its
displayed depth.  It cannot prove an asymptotic path bound or factoring
algorithm.
