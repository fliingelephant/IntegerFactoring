# F265-D02 hostile result audit

## Verdict

**PASS for the preflight-only stop.** The retained evidence authenticates the
frozen packet and all 19 copied remote artifacts. It also supports the stated
phase order, the projection rejection, and the claim that discovery,
selection, heldout, and summary did not start.

This verdict is only about the preserved preflight-stop package. It does not
authorize a changed runner or a production rerun. It gives no mathematical
result for the frozen search grammar.

I did not compile or execute `search.cpp`, invoke `remote_run.sh`, generate a
corpus, or access the remote host. I only read the retained files and ran
local hash, schema, counter, and arithmetic checks.

## Authentication

The current SHA-256 of the local `FROZEN.sha256` is

```text
26f7940244242edc549a2612fc08120372e0f8fab64a2dca154b69ed02d55d6a
```

All seven entries in that file authenticate the current local frozen files.
The terminal `logs/F265-D02.manifest` records the same seven file hashes and
the same `FROZEN.sha256` hash. The retained authentication stdout contains
seven `OK` lines and has empty stderr.

`REMOTE_ARTIFACTS.sha256` lists exactly the 19 files under the retained
`logs/` and `preflight/` directories. There are no missing or extra files in
that set. All 19 current bytes pass that manifest. Every row of
`ARTIFACT_HASHES.tsv` also matches the current byte count, current SHA-256,
recorded remote SHA-256, recorded local SHA-256, and `match=yes`. Its path set
is identical to `REMOTE_ARTIFACTS.sha256`.

For the 18 copied files other than the terminal manifest itself, the hashes
in `REMOTE_ARTIFACTS.sha256` also equal the hashes embedded in the terminal
manifest. `REMOTE_ARTIFACTS.sha256` separately binds the terminal manifest.
The current hashes of the three packaging records are:

```text
5023638a838754c32a3f55e279a948db7f2f1c3e72437fb514f0d6928fa13803  REMOTE_ARTIFACTS.sha256
21eff8030f64cdc09304fbeb4b160af4432d632334bb0da73554d22055f9ab01  ARTIFACT_HASHES.tsv
9548db54f38c38f23e2b91dc5c14c7b440c294b995edcf84e173f33302fbe819  RESULT.md
```

## Chronology

The frozen runner is sequential. Its retained timestamps and terminal status
fields give this order:

1. The runner started at `2026-08-13T18:15:31Z` and recorded the initial host
   state.
2. Authentication output closed at
   `2026-08-13T18:15:31.786019930Z`. All seven entries were `OK`.
3. Compilation completed with `compile_status=0` before the self-test could
   start.
4. Self-test output closed at
   `2026-08-13T18:16:04.651375401Z`. It contains `SELF_TEST_PASS`, stderr is
   empty, and the terminal status is `selftest_status=0`.
5. Preflight stdout was opened at
   `2026-08-13T18:16:04.671376223Z`. All eight preflight artifacts and the
   rejection stderr closed at `2026-08-13T19:11:20.895581711Z`.
6. Final resource evidence closed at
   `2026-08-13T19:11:20.915582410Z`. The terminal manifest closed at
   `2026-08-13T19:11:20.967584230Z` and records
   `preflight_status=2`.

The exact compiled-binary mtime quoted in `RESULT.md` is not independently
recoverable from this package. The binary was not copied, and neither hash
manifest records its mtime. This is a narrow provenance limitation, not a
material chronology defect. The frozen runner order, the terminal binary
hash and compile status, and the subsequent authenticated self-test output
still establish compilation before self-test and preflight.

## Projection recomputation

The seven preflight sidecars, excluding the final JSON, total exactly
`5,186,876` bytes. This equals `preflight_output_bytes` in the JSON.

Using the frozen family schedules and work formula, the nine retained moduli
have bit lengths

```text
24, 23, 24, 64, 64, 64, 120, 120, 120
```

The independently recomputed planned work is:

```text
planned_full_work       = 1,523,265,600
planned_preflight_work  =    26,372,676
work_ratio              = 57.759235354046...
generation_ratio        = 1536 / 9 = 170.666666666667...
```

These values agree with the six-decimal serialized ratios. Applying the
frozen formulas gives:

```text
projected evaluation  = 335,198.892429 s
projected generation  =       0.298667 s
projected full wall   = 335,199.191096 s
projected output      = 374,487,489.545316 bytes
```

Recomputation from only the six-decimal serialized wall time and ratio differs
from the recorded full projection by about `0.002` seconds. This is exactly
the expected loss from decimal serialization. Recomputing output from the
exact integer work ratio matches the recorded output projection.

The gate comparison is therefore:

| Gate | Observed | Limit | Result |
|---|---:|---:|---|
| corpus shortfall | 0 | 0 | pass |
| projected wall | 335,199.191096 s | 12,600 s | **fail** |
| peak RSS | 13,304 KiB | 3,670,016 KiB | pass |
| projected output | 374,487,489.545316 B | 805,306,368 B | pass |

The wall projection is about `26.6031` times the limit. It exceeds the limit
by about `322,599.191096` seconds. Thus the frozen Boolean gate must be false.
The JSON records `"pass":false`. The source writes and closes that JSON, then
throws `preflight projection rejected full packet`; `main` converts the
exception to status `2`. The retained stderr and terminal status match this
path exactly.

The aggregate sidecar counters are also coherent. Both the 108 bank rows and
the 12 family metric rows sum to the JSON values:

```text
rows             = 18,790
pair controls    = 2,369,895
gcd-free splits  = 41,719
pattern work     = 9,450,761
```

## Production-phase absence

The terminal manifest records:

```text
discovery_status=125
selection_status=125
heldout_status=125
summary_status=125
```

It contains no hash below the remote `output/` directory and no discovery,
selection, heldout, or summary log. The copied artifact set likewise contains
no production-phase filename and no `output/` directory. Because the frozen
runner exits immediately when `preflight_status` is nonzero, it cannot reach
the discovery invocation on this path. Therefore no discovery or heldout
cohort was opened, and the remote output directory was empty when the exit
trap made the terminal manifest.

The preserved result is a resource-feasibility rejection only. It is neither
a positive factoring signal nor a finite null for the registered grammar.
