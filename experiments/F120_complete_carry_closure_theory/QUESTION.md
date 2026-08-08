# F120 Preregistered Question — Complete Carry Closure

## Fixed object

For an odd input `N`, use the complete F116/F118 no-stop source:

1. seed residues `2..n`, where `n=N.bit_length()`;
2. both orientations of every frozen seed-basis pair through exponent `n^2`;
3. both orientations `[u^e v]_N` and `[u v^e]_N` for every unordered
   `2 <= u < v <= n` and every `0 <= e <= n^2`;
4. canonical-residue first occurrence;
5. global positive-exact-value first occurrence, with `P=1` removed.

For a retained unit residue `c`, let `w` be its least positive inverse and

```text
P_N(c) = c*w = 1 + kappa_N(c)*N.
```

The final object is the set `K_N` of distinct nonzero carries. Prime rows are
the odd valuation parities in `1+kN`.

## Question

Prove one of the following, or isolate its exact missing lemma.

### A. Stable-private obstruction

Construct an infinite trial-hard odd distinct-semiprime, non-perfect-power
family on which protected rows remain private against the complete
self-generated `K_N`, not only against a selected submatrix.

### B. Forced progress

Prove a deterministic consequence of the complete word menu. Keep these
claims separate:

1. `REUSE`: every odd prime-row occurrence repeats;
2. `CLOSE`: the exact square-class matrix has a nonzero kernel;
3. `ROOT`: some kernel element has a non-global positive square root modulo
   `N`.

## Exact finite falsifier computation

A theorem proved below before the run will show that a prime row
`r > (N-1)/2` is private among every possible canonical exact-value column.
The seed `2` has exact value `N+1`. Thus a distinct-semiprime input

```text
N = p*ell,
r = (N+1)/2 prime
```

is a deterministic finite counterexample to universal semiprime `REUSE`.

Search the first 10,000 ordinal pairs of proven consecutive primes, starting
`p` at the first prime at least 1,000,000 and `ell` at the first prime at
least 2,000,000. Stop at the first pair for which `r` is a proven prime and
both factors exceed `N.bit_length()^2`.

The named hard timeout is
`F120_SEMIPRIME_PRIVATE_ROW_HARD_TIMEOUT`, 60 seconds. The search is used only
for the finite falsifier. It cannot prove an infinite family.

## Proof rules and falsifiers

- Use exact carry, endpoint, gcd, valuation, and congruence arguments.
- Do not use smoothness or random-matrix heuristics.
- A private row in one selected submatrix is not stable full-source privacy.
- One private row refutes `REUSE`; it does not refute `CLOSE`.
- `REUSE` does not imply `CLOSE`.
- `CLOSE` does not imply `ROOT`.
- An infinite family with a fixed small factor is not a trial-hard semiprime
  obstruction.
- A finite semiprime falsifier does not prove an asymptotic family.

No durable ledger will be edited.
