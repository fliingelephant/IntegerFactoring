# F255 hostile audit

## Verdict

**PASS, with scope qualifications.** The hashes, fixed public word grammar,
modular evaluation, all 50,304 stored rows, all 200 JSON summaries, and the
stated safe-safe tail null survive independent review. The pass applies to
the limited conclusion in `RESULT.md`: this frozen word grammar is a finite
null. It gives no asymptotic theorem and no inverse-quasipolynomial progress
bound.

This is not a pass for literal compliance with every sentence of the
preregistration. The two 12-bit cohorts overlap in 22 semiprimes, the JSON
omits the requested global per-word aggregates, and the run packet does not
preserve the self-test output, peak memory, dependency-installation record,
or launch ownership. `RESULT.md` discloses these defects. None changes the
authenticated finite null at 32--60 factor bits.

## Authentication

I computed the input hashes and matched them to `PRELAUNCH_MANIFEST.md`
before reading the result artifacts.

| Frozen input | Supplied and computed SHA-256 |
|---|---|
| `PREREGISTRATION.md` | `6f5c61b09d01b5a17b3a2d54558ac828732d660f4024e826fee70177c14bc67c` |
| `search.cpp` | `b207e826311792aff8e1a74c87e23011a9bbde4e011a0eda43be94ef10548cd2` |
| `remote_run.sh` | `6477c8899881629955d781de39b94ec9780314eb5c0ee3931f1ca81aa0e3cd70` |
| `PRELAUNCH_MANIFEST.md` | `f1d30bbaa71c09a4e03c659ccce3ff23c055068cab909a15ce61198dfb45e439` |

The copied run artifacts have these current hashes:

| Artifact | SHA-256 |
|---|---|
| `output/F255-D01.json` | `955c0b4776ae8bbd2fca82a24b2dd86262c93f5ccabc40ecbe296e587e69af9e` |
| `output/F255-D01.tsv` | `35054d382c31dd2777da5e3cd2e8e67172642150d55d5a06aaa9f243ea1a5873` |
| `logs/F255-D01.stdout` | `dd698f2052f5fc986934ce704324146a7b3941a5fc9cd12062b8edd317cca3c2` |
| `logs/F255-D01.stderr` | `230109af6d114c0504ad1b113bf45a2e089e26469c6db605e07810ab1d6ea3ed` |
| `logs/F255-D01.manifest` | `7fff875ad068b53b40cb9eb36981ebeb43c9b89f8d038a8ea6a9c1c0163d6b26` |
| `RUN_MANIFEST.md` | `05ec90b018108e5ae6803b1781ecaec61fb8f6147ba03dcd026629e3cba2e08d` |
| `RESULT.md` | `39a94d029e7e4f89c5610d377920450daf44dd31fc7fa4ad90aee9999cbe2b5a` |

The remote manifest repeats the frozen source and runner hashes, records the
compiled binary hash
`77fecee76df2dbfa1b93e1430299045770541a12c46824be65178068100f2bfb`,
records exit status zero, and records the interval
`2026-08-13T13:17:08Z`--`2026-08-13T13:19:30Z`. The mathematical stdout is
exactly the 50,304-input PASS line. The stderr has 197 well-formed progress
records, exactly the multiples of 256 followed by 50,304; their elapsed
times are monotone, and there is no failure record.

These facts authenticate the preserved bytes and their internal
consistency. They do not independently authenticate who launched the
runner.

## Public-word and hidden-label boundary

The source implements the frozen bank

```text
D = 2,3,5,6,7,10,11,13
1 <= j <= 4*bitlength(N)
```

and retains exactly the rows with positive canonical quotient `k`. It
implements all six same-discriminant offsets, the two odd-multiple menus,
all same-index cross-discriminant pairs, and four deterministic hash
partners per retained row. The hash depends only on `N`, the public row
position, and the partner number. It implements the displayed resultant,
the two same-discriminant norm factors, both carry polynomials, and the
neutral factor one when a carry vanishes.

Every channel starts with one factor `N-1`. Each non-baseline factor is
inserted into its own channel and into `combined`; no call inserts a factor
into `combined` twice merely because it is combined. The final modular
power is exactly the public exponent `n=bitlength(N)`.

The factors `p,q` enter word evaluation only through `N` and the two hidden
residual moduli. Exact row retention, edge selection, carries, and hash
partners use `N` but not the hidden labels. Reduction modulo the residuals
is only a memory-efficient evaluation of already fixed public factors. The
stored score then uses the labels, as preregistered. I found no
factor-dependent candidate selection, factorization of a candidate word,
or hidden-label branch in word generation.

For each residual `s`, the implementation computes

```text
gcd((V mod s)^n mod s, s) = gcd(V^n, s).
```

Thus its quality is exactly

\[
\max\{\gcd(s_p,W)/s_p,\gcd(s_q,W)/s_q\}.
\]

The use of modular residues changes neither the public word nor its exact
gcd score.

## Size and resource claim

For fixed `D` and `j<=4n`, every Pell coordinate has `O(n)` bits. Therefore
`k`, `y`, every row value, resultant, norm factor, and carry factor has
`O(n)` bits. There are `O(n)` rows and `O(n)` edges in each frozen menu.
The base product consequently has `O(n^2)` bits, and its final `n`th power
has `O(n^3)` bits. Repeated edges do not change this bound. The source uses
only exact integer and modular arithmetic; it never factors a word.

The runner fixes eight threads, `nice -n 15`, and a 14,400-second timeout.
The output confirms eight threads and 139.224 seconds of mathematical run
time. There is no peak-resident-memory record, so the four-GiB ceiling is
not empirically certified. The prelaunch manifest states that the user
authorized installing Boost 1.74, but no package-manager transcript is
preserved. I could not independently rebuild the source on the local Mac
because its compiler environment lacks the Boost multiprecision header.
This does not affect the independent arithmetic reconstruction below.

## Independent full-data checks

I parsed all 50,304 TSV rows independently. A deterministic 64-bit
Miller--Rabin check and exact integer checks found no error in:

- primality, declared factor bit length, order, and balance of `p,q`;
- `N=pq`, `n=bitlength(N)`, and both residuals;
- the safe-prime labels in every safe-safe row;
- divisibility of every stored gcd into its residual;
- all 503,040 stored `-log2(H)` values; and
- every baseline gcd recomputed directly from `(N-1)^n`.

Each individual `(factor_bits,cohort)` cell has the preregistered row count
and no internal duplicate. There are 50,282 distinct semiprimes overall.
The difference is exactly the 22 cross-cohort overlaps at 12 factor bits.
Every random/safe counterpart at 16 bits or more is disjoint.

I reaggregated the TSV with exact rational comparisons. All 200 JSON
records match in count, mean, interpolated median, 90th and 99th
percentiles, minimum-quality witness, strict-improvement count, and
saturation count. The exact global totals are:

| Word | Strict improvements | Saturations |
|---|---:|---:|
| `baseline` | 0 | 127 |
| `rows` | 39,826 | 15,188 |
| `same_res` | 41,052 | 22,763 |
| `cross_res` | 40,322 | 18,237 |
| `hash_res` | 40,463 | 19,197 |
| `norm_minus` | 40,679 | 20,827 |
| `norm_plus` | 40,719 | 20,863 |
| `carry3` | 39,641 | 13,604 |
| `carry5` | 39,293 | 11,273 |
| `combined` | 41,351 | 24,163 |

Finally, I wrote an independent in-memory implementation from the frozen
formulas. It did not import or execute the discovery source. On the first
stored input from each of the 20 cohort cells, it regenerated every Pell
row, every edge menu, every hash partner, every carry, and all ten channel
products. All 400 resulting gcd values matched the TSV.

## Decisive finite interpretation

For every safe-safe input at factor bits 32, 40, 48, 56, and 60, every
candidate channel equals the baseline in both stored gcds. This is a
row-by-row equality, not merely equality of an aggregate. In particular,
all those cells have zero strict improvements and zero saturated residuals.
The maximum `-log2(H)` for `combined` is respectively

```text
30.9752817105, 38.9803727948, 46.9743810321,
54.9707153909, 58.9854458990.
```

This is the preregistered finite-null behavior. Random inputs contain real
finite anomalies, including many strict improvements, but the reported
random worst samples also retain linear growth. Those anomalies may motivate
a different grammar; they do not make this grammar a useful all-input lead.

## Protocol qualifications

1. The source rejects duplicates only within a cohort. It does not enforce
   random/safe disjointness. The actual 12-bit intersection has 22 exact
   semiprimes. Any literal 12-bit between-cohort comparison is therefore
   qualified.
2. The JSON reports the global input count and elapsed time but not the
   preregistered global per-word aggregates. They remain exactly
   reconstructible from the frozen per-row TSV and are displayed above.
3. `remote_run.sh` executes `--self-test` under `set -e`, so the later run
   implies a zero self-test status. Its stdout was not redirected into the
   preserved experiment logs. The self-test text itself is unauthenticated.
4. The packet records neither peak memory nor an installation transcript.
   The Boost version and user authorization are assertions in the frozen
   prelaunch manifest. Launch ownership is unknown.

None of these qualifications licenses an asymptotic inference. The only
audited conclusion is the fixed-grammar finite null stated in `RESULT.md`.
