# F15 Hurwitz-bias hostile-audit manifest

**Approach-family ID:** `F15_hurwitz_bias_audit`

No canonical file was edited.  In particular, this local manifest records the
run because the audit assignment expressly forbids editing `REGISTRY.md`.

## Inputs inspected

- `PROMPT.md`, including its computation contract;
- promoted background `PROVED.md` P25;
- `experiments/F15_hurwitz_gcd_audit/RESULT.md` and
  `experiments/F15_hurwitz_gcd_reconstruct/reconstruction.md`;
- all retained files under `experiments/F15_hurwitz_bias_kill/`; and
- the candidate source, wrapper, JSON, log, and manifest hashes.

The audit source imports no candidate module.  It reads the candidate JSON only
to compare the retained scan's coverage and hash; all quaternion arithmetic,
splittings, shell enumeration, orientations, unit actions, and right-divisor
checks are independently implemented.

## Retained run

| Run | Status | Hard timeout | Log | Output |
| --- | --- | ---: | --- | --- |
| F15-BA01 | exit 0, PASS | 120 s | `logs/F15-BA01.log` | `output/F15-BA01.json` |

There was no failed, interrupted, timed-out, or superseded audit run.

Coverage: complete enumeration of all 53 distinct odd semiprimes \(pq\le300\),
the canonical right-unit stabilizer probability on each, row and image fibres
and left/right unit-orbit integrality at \(N=15,39\), direct norm-\(p\) and
norm-\(q\) common-right-divisor checks for the unit-orbit cases, projective-unit
faithfulness for every odd prime appearing in the scan, Q8 canonicalization at
\(N=15\), and rejection weights including 48 \(d=0\) representations at
\(N=21\).

## Exact invocation

Invoked from the repository root:

```sh
zsh experiments/F15_hurwitz_bias_audit/run_F15_BA01.sh
```

The wrapper's timed command was:

```sh
/opt/homebrew/bin/timeout 120s python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F15_hurwitz_bias_audit/scripts/F15_BA01_independent.py --candidate-output /Users/zhou/autoresearch/IntegerFactoring/experiments/F15_hurwitz_bias_kill/output/F15-B01.json --output /Users/zhou/autoresearch/IntegerFactoring/experiments/F15_hurwitz_bias_audit/output/F15-BA01.json
```

## SHA-256

| Artifact | SHA-256 |
| --- | --- |
| `scripts/F15_BA01_independent.py` | `e4f860bbe8f52c0cfd4dbc27c7181030297288705781d9d79a6308ae233323eb` |
| `run_F15_BA01.sh` | `53de639f22669ce3303b35671e858b54988b120d40a9e31cd0d8c8f54269925b` |
| `output/F15-BA01.json` | `f73e1b3d1d464c0562d879c4ea408af8df9429e95988f67f142230fcb0f211eb` |
| `logs/F15-BA01.log` | `d03dffbad807f70857d9e869e2b1bfc1438576d6bebac8b35e2f4e3b167fce25` |

The JSON embeds the source hash and the inspected candidate-output hash.  Finite
enumeration is evidence only for the displayed instances; every unbounded claim
in the audit is proved symbolically in `RESULT.md`.
