# F13 Teichmuller lift hostile-audit manifest

**Approach-family ID:** `F13_teichmuller_lift_audit`.

The audit read the author `RESULT.md`, `RUN_MANIFEST.md`, source, wrapper,
log, and complete JSON output.  A01 then independently recomputed the
mathematics with the named source `audit.py`; it did not import the author
source or read the author output for mathematical computations. The author
directory was read separately for the hostile prose/source review, artifact
hashing, and A03's post-computation certificate comparison.

## Run summary

| Run | Status | Timeout | Coverage | Log | Output |
| --- | --- | ---: | --- | --- | --- |
| A01 | exit 0, PASS WITH CORRECTION | 180 s | Nine author instances, global and local structural checks, exact additive/iterate/high-digit reproduction, 90 balanced fibre censuses, twin-prime sweep below 202, author hash audit | `logs/A01.log` | `output/A01.json` |
| A02 | exit 0, PASS | 60 s | Independent reproduction of every named fixed small probe and all rounded-exponent checks | `logs/A02.log` | `output/A02.json` |
| A03 | exit 0, PASS | 30 s | Byte-addressed comparison of all retained A02 fixed-probe fields against the hashed author R01 JSON | `logs/A03.log` | `output/A03.json` |

There were no failed or timed-out audit runs.

## Exact invocation

The retained wrapper was invoked from the repository root as

```sh
./experiments/F13_teichmuller_lift_audit/run.sh
```

Its timed command was

```sh
/opt/homebrew/bin/timeout 180s python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F13_teichmuller_lift_audit/audit.py --output /Users/zhou/autoresearch/IntegerFactoring/experiments/F13_teichmuller_lift_audit/output/A01.json
```

The second retained wrapper was invoked as

```sh
./experiments/F13_teichmuller_lift_audit/run_fixed.sh
```

and ran

```sh
/opt/homebrew/bin/timeout 60s python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F13_teichmuller_lift_audit/fixed_probe_audit.py --output /Users/zhou/autoresearch/IntegerFactoring/experiments/F13_teichmuller_lift_audit/output/A02.json
```

The comparison wrapper was invoked as

```sh
./experiments/F13_teichmuller_lift_audit/run_compare.sh
```

and ran

```sh
/opt/homebrew/bin/timeout 30s python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F13_teichmuller_lift_audit/compare_fixed.py --author /Users/zhou/autoresearch/IntegerFactoring/experiments/F13_teichmuller_lift_kill/output/R01.json --audit /Users/zhou/autoresearch/IntegerFactoring/experiments/F13_teichmuller_lift_audit/output/A02.json --output /Users/zhou/autoresearch/IntegerFactoring/experiments/F13_teichmuller_lift_audit/output/A03.json
```

All three logs record Python 3.14.5, `STARTED`, their respective hard limits, and
their terminal pass status.

## SHA-256

| Artifact | SHA-256 |
| --- | --- |
| `audit.py` | `776a073fa517671e45e2c32dabaa880d269a99fab5ca6f3a5ed9220d7b5a39a6` |
| `run.sh` | `a4d35da36a3537bc225df2de2a1e2eeb0bd928f6b3d58d15d76a99e6c1941c4a` |
| `output/A01.json` | `5771c0db249d30db68c4d83d47b4a28b4bdb35e08dd34f9426c9315137edf812` |
| `logs/A01.log` | `d9069cfe1a38f8a1718b9af06b0e52e3d501fc1e0068066781bbe686a91d9dac` |
| `fixed_probe_audit.py` | `4ee7bc49a78286e5c4f148b013168d8546d6c758ff08c817b3f34461afe4e15e` |
| `run_fixed.sh` | `0f03667ca9396ebb904266aba795e8e901b539413e7720c183e5fab985495c7a` |
| `output/A02.json` | `3bbaca4ccdeaa2f57e52cc7ff8e06b0136d82d31e037bfccfd16560acf0a96e0` |
| `logs/A02.log` | `38be60c287efd218508c3c5ee2f2f2ea0e071945a10bf378ac9a3b40c2bc06f4` |
| `compare_fixed.py` | `0150924068d7d77491d042abb7958cafbc326642e2e05e7482a10b1f217f808a` |
| `run_compare.sh` | `933c01463342099d48bcd2756993cdefdabf15c74bef1cd1e25c113f4e3bede1` |
| `output/A03.json` | `5e6b15997fdff5ff57ad49fb8c7dacc1d3f9577ac5b54c1c9af73a6a15fe1b9a` |
| `logs/A03.log` | `26b9398b36345c30327a95d33625c10e509736b36af62512e707d059803f12e0` |

Each audit source hash is embedded in its corresponding JSON and was
computed by the source before it wrote that certificate. The sources and
wrappers were not edited after their runs.
