# F221-D01 preregistration

## Purpose

Test the surviving fixed-shift scalar channel

\[
H_1(x)=(x+1)^N-x^N-1\pmod N
\]

on a small exact corpus of balanced semiprimes.  The proved torsion-coset
bound for F221 applies when the multiplicative scale is refreshed.  It does
not by itself bound the root count when the shift is fixed and only `x` is
sampled.

This run is discovery only.  It cannot prove an asymptotic success law.

## Frozen corpus and outputs

- Sieve all primes through `4000`.
- For each prime `p >= 101`, choose at most three primes `q` in the frozen
  ratio windows `[1, 1.08]`, `[1.25, 1.35]`, and `[1.50, 1.65]`, always
  taking the least eligible `q` with `p < q < 2p` and `pq = 3 mod 4`.
- For each pair, enumerate every residue in both local fields and count the
  roots of `H_1` exactly.
- Record the exact CRT XOR probability, the gap, and
  `gcd(p-1,q-1)`.
- Preserve aggregate ranges and the 40 largest XOR probabilities.

## Resource estimate and snapshot

The corpus has fewer than 2,000 pairs and fewer than 16 million modular
power evaluations.  Expected runtime is below 30 seconds.  Peak memory is
below 50 MiB.  Before preregistration, local load averages were
`1.97 1.86 1.73`.  `vm_stat` showed 51,121 free 16-KiB pages, no throttled
pages, and existing compression/swap pressure.  The frozen cap is therefore
kept small.  Process inspection was unavailable because `ps` was denied by
the sandbox.  No parallel worker is permitted.

## Authoritative command

From the repository root:

```sh
/opt/homebrew/bin/timeout 60s /opt/homebrew/bin/python3 experiments/F221_beta2_random_aks_torsion_coset/fixed_shift_scan.py --limit 4000 --output experiments/F221_beta2_random_aks_torsion_coset/D01_OUTPUT.json > experiments/F221_beta2_random_aks_torsion_coset/D01_RUN.log 2>&1
```

Any change to the source, limit, corpus rule, timeout, or output schema
requires a new run ID.
