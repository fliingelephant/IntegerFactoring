# F17 hostile-audit run manifest

All authoritative computation in this directory serves family **F17**.  The
finite checks are sanity checks only; the unbounded audit is proved in
`RESULT.md`.

## Environment

- Date: 2026-08-06 (Asia/Hong_Kong)
- Sage executable: `/usr/local/bin/sage` (SageMath 10.9 bundle)
- Timeout executable: `/opt/homebrew/bin/timeout`
- Working directory: `/Users/zhou/autoresearch/IntegerFactoring`
- Per-run timeout: 300 seconds, set literally in each runner

## Runs

| Run | Exact source and runner | Timeout | Log | Output | Disposition |
| --- | --- | ---: | --- | --- | --- |
| D00 | Noncompliant inline Python environment diagnostic | none | not retained | none | Disqualified. It checked only whether `cypari2` and `sympy` were importable; it made no mathematical assertion. It violated the named-source rule and is not evidence. |
| A00 | `scripts/F17_A01_exhaustive.sage`; `run_F17_A01.sh` | 300 s | not retained | none | Failed before importing Sage because the sandbox denied writes to Sage's user cache. The runner then reused the same log path for A01, so the original log was unintentionally overwritten. Exact failure class: `PermissionError` under `/Users/zhou/.sage/cache`. No mathematical assertion ran. |
| F17_A01 | `scripts/F17_A01_exhaustive.sage`; `run_F17_A01.sh` | 300 s | `runs/F17_A01_failed_json.log` | `artifacts/F17_A01_failed_partial.json` | Failed after all assertions, while `json.dump` tried to serialize a Sage `Integer`. The partial JSON is deliberately retained and is not authoritative. |
| F17_A02 | `scripts/F17_A02_exhaustive_json_fix.sage`, which loads the retained A01 definitions and changes only the JSON serializer; `run_F17_A02.sh` | 300 s | `runs/F17_A02.log` | `artifacts/F17_A02_output.json` | **Pass.** Checked all 630 distinct-odd semiprimes with both primes below 160, 21 exact Stirling counts, and nine finite abelian-group powering cases. |

The exact successful command was:

```text
experiments/F17_classgroup_ambiguity_audit/run_F17_A02.sh
```

The runner invokes:

```text
/opt/homebrew/bin/timeout 300 /usr/local/bin/sage experiments/F17_classgroup_ambiguity_audit/scripts/F17_A02_exhaustive_json_fix.sage experiments/F17_classgroup_ambiguity_audit/artifacts/F17_A02_output.json
```

The actual runner uses absolute paths derived from its own directory and pipes
combined stdout/stderr through `tee` to the named log.

## What F17_A02 checks

- independent enumeration of every canonical primitive reduced form;
- the fixed-point criterion and the proposed complete ambiguous-form lists;
- exact extraction versus the principal and even-discriminant decoys;
- the failure-count numerator in the Stirling formula by brute force for
  \(1\le H\le3\) and \(0\le m\le6\);
- the images of the powers \(\lambda(G)/2\) and \(h(G)/2\) on small abelian
  groups with two- and four-element 2-torsion.

The run does not prove an unbounded theorem, validate Siegel's theorem, or
construct a class sampler.

## SHA-256

```text
bb7087134dc9204f6f83f15844d81fdb2a6f3fa2abf1c9eed74676fd1d297805  scripts/F17_A01_exhaustive.sage
8f4163c3df308befd860fb70b8b28632d4d6f13b374483f86148879159b9f084  scripts/F17_A02_exhaustive_json_fix.sage
a5391748caa5c8dd84458f2508a209a631406710cdcf736716679170fd48c3a5  scripts/F17_A01_exhaustive.sage.py
7616b39cf2a6618048493f70f511daa3e957d6b1faba39853427f62ffb5e7363  scripts/F17_A02_exhaustive_json_fix.sage.py
bfaf7b4013e3cff6ac9d97d574448d1331a2d4d304acf2ee113f80fd2af410a0  run_F17_A01.sh
b60b97623064d21f64e32125772a48e9b093e09df312acbbc83ceed16dbff5cd  run_F17_A02.sh
75f11bd90023e720968ca0e701efa1c298aa1cfa716591710847cfc6cfb5866e  runs/F17_A01_failed_json.log
1485454935127a0520aa8e255639e0b9570a75258e60d0728ebdcdce3b6db347  runs/F17_A02.log
4e7136ea6b09363e9b0e8612331b9499551cabd4fe6e8e410ed6a075ee2f1719  artifacts/F17_A01_failed_partial.json
0e4e1f6dd2e6b76461f3128aa6d59a4050a90ca90a845a3a7cf9a9d07911235f  artifacts/F17_A02_output.json
```
