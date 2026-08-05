# F15 Hurwitz-gcd hostile-audit manifest

**Approach-family ID:** `F15_hurwitz_gcd_audit`.

## Inputs inspected

The audit read the root `AGENTS.md`, `PROMPT.md`, the complete author
`experiments/F15_hurwitz_gcd_kill/RESULT.md`, and the fixed task statement.  A
targeted search found no F15/Hurwitz entry yet in the canonical registry,
failures, proved results, or progress note.  The author directory contains no
manifest or computational artifact; its result explicitly records that no
computation was used.

The cited find-one/uniform-sampling distinction was checked against excerpts from
the Pollack--Treviño paper's introduction and unconditional-algorithm section.
The paper was not used as a substitute for a proof of exact-uniform sampling, and
the F15 theorem does not depend on a find-one algorithm.

## Run summary

| Run | Status | Timeout | Coverage | Log | Output |
| --- | --- | ---: | --- | --- | --- |
| F15-A01 | exit 0, PASS | 60 s | Exact Hurwitz enumeration at \(N=15\); row/image fibres; free unit orbits; direct right/left divisor handedness; complete ordered-pair gcd categories; complete product incidences; self-conjugation; fixed scalar/non-scalar transforms; 73,728 mixed barred/unbarred local identities; \(N=2,6,9\) non-extension checks | `logs/F15-A01.log` | `output/F15-A01.json` |

There were no failed or timed-out runs.

## Exact invocation

The retained wrapper was invoked from the repository root as

```sh
./experiments/F15_hurwitz_gcd_audit/run_F15_A01.sh
```

Its timed command was

```sh
/opt/homebrew/bin/timeout 60s python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F15_hurwitz_gcd_audit/scripts/F15_A01_exact_small.py --output /Users/zhou/autoresearch/IntegerFactoring/experiments/F15_hurwitz_gcd_audit/output/F15-A01.json
```

The log records the run ID, family ID, UTC start and finish, hard limit, and
terminal status.  The source does not import or execute author code.

## SHA-256

| Artifact | SHA-256 |
| --- | --- |
| `scripts/F15_A01_exact_small.py` | `4f114811494c5185556b6cf1428a99836370b4d837eb57bc4818ded19e96a190` |
| `run_F15_A01.sh` | `0d6b9102a7762fa05245a08134efaf7c2f13e5f8275f37f532714bcc62d93656` |
| `output/F15-A01.json` | `743aa13efe656027ad8ac6bbeada04474cf40f15ccb5c1f808fa0b537b943cac` |
| `logs/F15-A01.log` | `1e884f2db8eda701aed6233ee53802f490f2a607fab444e8ec049000e8c44d53` |

The source hash is embedded in the JSON and was computed by the source before it
wrote the certificate.  The source and wrapper were not edited after the run.
