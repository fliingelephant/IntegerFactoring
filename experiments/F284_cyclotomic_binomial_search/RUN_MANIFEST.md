# F284 cyclotomic-binomial jet run manifest

## Scope

This packet verifies formulas supplied by the root. It makes no novelty claim
and draws no integer-factoring conclusion.

The authoritative run checks:

- the Bernoulli-polynomial power-sum formula against direct sums for
  `0 <= M <= 30` and powers `1` through `12`;
- the order-12 logarithmic and exponential jets against literal Gaussian
  q-binomial polynomials for every `0 <= k <= m <= 30`;
- the supplied q-Lucas congruence modulo `Phi_d(q)` for every
  `1 <= d <= 12` and every `0 <= k <= m <= 30`; and
- the order-12 jet for `m=2B`, `k=B`, `B=2^512+12345`, using Bernoulli power
  sums without constructing the literal Gaussian polynomial or binomial.

## Sources and runner

- Sage source: `verify_cyclotomic_binomial_jets.sage`
- timeout runner: `run_with_timeout.py`
- fixed invocation: `run.sh`
- Sage executable: `/usr/local/bin/sage`
- Sage state: `DOT_SAGE=/private/tmp/f284_cyclotomic_binomial_search_sage`
- hard timeout: 60 seconds

From the repository root, the authoritative command was:

```sh
bash experiments/F284_cyclotomic_binomial_search/run.sh
```

The wrapper executed:

```sh
/usr/local/bin/sage \
  experiments/F284_cyclotomic_binomial_search/verify_cyclotomic_binomial_jets.sage \
  --output experiments/F284_cyclotomic_binomial_search/output/D05.json
```

It used a separate process group and retained the command, UTC timestamps,
duration, timeout flag, exit code, disposition, and log hash.

## Authoritative result: D05

`D05` exited 0 without timeout.

| Measurement | Value |
| --- | ---: |
| Wrapper duration | 2.111226875 seconds |
| Internal total | 0.522698208 seconds |
| Direct power-sum checks | 372 |
| Literal Gaussian jet cases | 496 |
| Highest literal polynomial degree | 225 |
| q-Lucas remainder checks | 5,952 |
| Remote `B` bit length | 513 |
| Remote jet coefficients | 13, degrees 0 through 12 |
| Largest remote log-coefficient numerator | 6,661 bits |
| Largest remote coefficient numerator | 12,273 bits |
| Largest remote log denominator | 30 bits |
| Largest remote coefficient denominator | 27 bits |

The remote coefficient denominators are retained exactly in `D05.json`:

```text
1, 2, 4, 12, 48, 240, 1440, 10080, 16128, 725760,
79833600, 7257600, 38320128
```

The output records `materialized_literal_polynomial=false`. Every asserted
literal comparison and cyclotomic remainder equality passed.

## SHA-256

| Artifact | SHA-256 |
| --- | --- |
| `verify_cyclotomic_binomial_jets.sage` | `3238b81e266ae80d91f0e894f67e88ed30e6e409eceeb9234cb220f2b09c3c55` |
| `run_with_timeout.py` | `56dc4e8429d2d1914e1d36dd084fe2de497ff11cb424afcc7b04b569d3c7aca9` |
| `run.sh` | `d24fd676a4f6c6b1e2838ac7c13102f84f1bff5bed0090653ad6b593a89adc89` |
| `output/D05.json` | `3d82a685cd53ec3ff02b2787113b51484f8bb6bf7a367c96a8253a6b9b2d87a2` |
| `logs/D05.log` | `12712cc0d726448407c7a64ae4aa1b46e2bcce5d9e3a286293fe36cea52652a9` |
| `output/D05.status.json` | `e649865e78280391ff31839a1775a7455be309c91d5b94f07139e419f1a746f9` |

The D04 and D05 mathematical JSON payloads are identical after removing the
environment and timing fields; their canonical `jq` output then has SHA-256
`0cec8121ecccde88dfb529cc701ca209fd58e8b5e7cf5858dbd9197192ff9efa`.

## Environment

- SageMath 10.9, release date 2026-05-04
- Python 3.14.3 inside Sage
- macOS arm64

See `FAILED_RUNS.md` for the three preserved implementation failures and the
non-authoritative D04 metadata issue.

## Symbolic central-index run: S01

The separate source `factor_central_symbolic_jets.sage` treats `B` as an
indeterminate over `QQ[B]`. It computes and factors `c_1` through `c_12`, forms
`mu_j=j!*c_j`, and factors the moment Hankel determinants of sizes 1 through 5.
The size-5 determinant uses moments only through `mu_8`.

S01 was the only Sage process launched for this symbolic task. It exited 0
without timeout. The wrapper duration was 2.215618459 seconds and the internal
symbolic time was 0.038205583 seconds. All three supplied sanity identities
passed:

```text
c_1 = B^2/2
c_2 = B^2*(3*B^2+2*B+1)/24
c_3 = B^4*(B+1)^2/48
```

The exact expanded polynomials, rational factor lists, common denominators,
integer numerators, coefficient bit lengths, moments, and Hankel determinants
are retained in `output/S01.json`. A compact readable rendering is retained in
`output/S01.txt`.

| Artifact | SHA-256 |
| --- | --- |
| `factor_central_symbolic_jets.sage` | `2d45f86242885de1107bff6a1d563a6f2c616503bd855d48818b6e438fd57569` |
| `run_symbolic.sh` | `0e73e6a2b4b5af2158ce83f655f15b6ce4f26ce7af142a73ccfddf7e58de6738` |
| `output/S01.json` | `7791b815425fb3233b54706bb015dc0516a105b0d1c8960249bc567298d261f3` |
| `output/S01.txt` | `800f7c9eb6409f016e7d5104f51f991893bd70ba040b6f626626832a2ad940a2` |
| `logs/S01.log` | `ae0544f4014401a6643c639e67c48c3ae72de5ef3752888a62e2248570804bd4` |
| `output/S01.status.json` | `c4eeee2b5ffffbbdeec5ac355f710e1076ed57c35de78c666a627d04b79ebda7` |

This run records exact symbolic structure only. It makes no prime-asymmetry,
factoring, or novelty claim.
