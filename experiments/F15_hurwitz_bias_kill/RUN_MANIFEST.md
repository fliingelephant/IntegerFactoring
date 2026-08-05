# F15 Hurwitz-bias kill manifest

**Approach-family ID:** `F15_hurwitz_bias_kill` (follow-up inside F15).

## Inputs inspected

The study read the complete root `REGISTRY.md`, `FAILED.md`, corrected hostile
audit `experiments/F15_hurwitz_gcd_audit/RESULT.md`, proof-blind reconstruction
`experiments/F15_hurwitz_gcd_reconstruct/reconstruction.md`, and original
candidate `experiments/F15_hurwitz_gcd_kill/RESULT.md` before stating the new
claim.  It does not edit canonical files and does not import prior experiment
code.

No cited four-square algorithm supports a runtime claim in this study.  The only
sampler whose complexity is used is the coordinate-triple rejection sampler
defined and analyzed from first principles in `RESULT.md`.

## Run summary

| Run | Status | Timeout | Coverage | Log | Output |
| --- | --- | ---: | --- | --- | --- |
| F15-B01 | exit 0, PASS | 120 s | Exact integer norm-shell enumeration; row-orientation fibres; iid collision tables; sample-dependent Q8 canonicalization; all 144 projective-unit pairs for the right-orbit stabilizer formula; lexicographic semiprime scan through 300 | `logs/F15-B01.log` | `output/F15-B01.json` |

There were no failed, interrupted, or timed-out runs.

## Exact invocation

The retained wrapper was invoked from the repository root as

```sh
zsh experiments/F15_hurwitz_bias_kill/run_F15_B01.sh
```

Its timed command was

```sh
/opt/homebrew/bin/timeout 120s python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F15_hurwitz_bias_kill/scripts/F15_B01_coordinate_slice.py --output /Users/zhou/autoresearch/IntegerFactoring/experiments/F15_hurwitz_bias_kill/output/F15-B01.json
```

The log records the run ID, family ID, UTC start and finish, and hard limit.  The
source computes and embeds its own pre-output SHA-256.  Neither source nor wrapper
was edited after the run.

## SHA-256

| Artifact | SHA-256 |
| --- | --- |
| `scripts/F15_B01_coordinate_slice.py` | `bcd71f20cfc56e2fed96bca07df74e2b6e3a07fe1a3d7e29bdc0d5075eec9a78` |
| `run_F15_B01.sh` | `b35fdfb8ebf4e3bfcfdb1895a154cc949a9cac5a5e2b103e9f5f574997a101ca` |
| `output/F15-B01.json` | `7012ca1dde400acd50aef988dd2cb89820ba456d4f2f5c3823171f2b202110c1` |
| `logs/F15-B01.log` | `6cf0bcad6942877a444dc29b550c769a711c956edd3d7d77108e600312ebc681` |

## Scope

The run is finite checking only.  It does not prove the unbounded fibre,
rejection-cost, finite-menu, or stabilizer theorems.  Those are proved
symbolically in `RESULT.md`.  The scan's “first” wording is restricted to the
explicit ordered set of distinct odd semiprimes with product at most 300.
