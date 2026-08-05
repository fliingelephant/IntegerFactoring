# F13 Teichmuller lift kill manifest

**Approach-family ID:** `F13_teichmuller_lift_kill`.

Every mathematical computation used the named source
`teichmuller_kill.py`, an explicit 180-second hard timeout, a retained log,
and a retained JSON output.  The successful source was not edited after the
run.  Python's standard library was the only dependency.

## Run summary

| Run | Status | Coverage | Log | Output |
| --- | --- | --- | --- | --- |
| R01 | exit 0, PASS | Nine small/balanced semiprimes; local lift identities; full principal subgroup for all feasible instances; exact additive and iteration probabilities; high-digit exhaustion/bounds; fixed probes | `logs/R01.log` | `output/R01.json` |

Instances:

```text
(3,5), (3,7), (5,7), (7,11), (11,13), (13,17),
(101,103), (1009,1013), (10007,10009)
```

For \(N\le50{,}000\), R01 exhaustively checked all \(k\pmod N\) in the
principal subgroup and all unit bases in the three-value high-digit test.
For larger \(N\), it checked 101 named principal coefficients, exhaustive
local ratio distributions, exact group-count probabilities, analytic
high-digit bounds, and fixed bases through 64/pairs from the first 12 units.

## Exact invocation

The retained wrapper was invoked from the repository root as

```sh
./experiments/F13_teichmuller_lift_kill/run.sh
```

Its timed computation was

```sh
/opt/homebrew/bin/timeout 180s python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F13_teichmuller_lift_kill/teichmuller_kill.py --output /Users/zhou/autoresearch/IntegerFactoring/experiments/F13_teichmuller_lift_kill/output/R01.json
```

Standard output and error were appended to
`experiments/F13_teichmuller_lift_kill/logs/R01.log`.  The wrapper recorded
`STARTED`, the 180-second limit, Python 3.14.5, and `PASS`.

## SHA-256

| Artifact | SHA-256 |
| --- | --- |
| `teichmuller_kill.py` | `200cfb7d28fea4c643dde0b6602f348e41ac5f71ad9fe4b09ca2864d849823f1` |
| `run.sh` | `e91c52d055ee9e7f8ed9becb747d3e14fef2c1b6bae25a268d59c4238cafbf70` |
| `output/R01.json` | `7a2c6c678acd99f38b6ff274c21f7512a3aca156ecfc760b8a41f5eb14ea399d` |
| `logs/R01.log` | `7273da35708dc28077f25727c9ae2ab2c2aeb86f7141ca7f835c79bcff46b0ca` |

The source hash is also embedded in `output/R01.json` and was computed by the
source itself before the JSON certificate was written.
