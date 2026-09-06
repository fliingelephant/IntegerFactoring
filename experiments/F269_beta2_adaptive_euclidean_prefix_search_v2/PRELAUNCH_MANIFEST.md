# F269-D02 prelaunch manifest

## Status

This is an unexecuted C++17 repair candidate. It is not frozen.
`FROZEN.sha256` contains a blocking sentinel, not an audit manifest. The
intended host has no writable delegated cgroup-v2 leaf, while this candidate
requires one before compile. After an explicit enforcement decision and a
consistent freeze, a `PASS` audit must name the SHA-256 of `FROZEN.sha256` in
`HOSTILE_PRERUN_AUDIT.md`. The runner refuses to compile without that
authentication.

## Scientific boundary

D02 preserves the D01 algebra, 444-root and 5,120-tuple grammar, deterministic
discovery and heldout cohorts, hidden-label chronology, selector/direct total
orders, 256-row selection firewall, and finite verdict thresholds. The D02
changes are operational: evidence separation, ledger closure, resource gates,
the real production aggregate stress allocation, and complete grammar masks.

## Entry points

The scientific modes are:

```text
--self-test BASELINES
--grammar-once
--max-work-round W ROUND
--serialization-write EVIDENCE ABSOLUTE_PATH
--splitmix-stream-write EVIDENCE ABSOLUTE_PATH
--checked-truncate EVIDENCE ABSOLUTE_PATH
--gate METRICS E_GATE_NS EVIDENCE OUTPUT
--discovery BASELINES EVIDENCE W
--heldout BASELINES EVIDENCE W SELECTION SELECTION_SHA DISCOVERY_CORPUS_SHA
```

The evidence-control modes are:

```text
--ledger-init EVIDENCE STATE
--ledger-check EVIDENCE STATE
--ledger-write EVIDENCE STATE replace|append PATH
--failure-manifest EVIDENCE STATE PATH
--checked-copy EVIDENCE STATE SOURCE DESTINATION
--checked-exec EVIDENCE STATE OUT_MODE OUT ERR_MODE ERR -- COMMAND...
--compression-commit EVIDENCE STATE SOURCE TEMP REPLACEMENT
--close-logs EVIDENCE STATE
--finalize-hashes EVIDENCE STATE OUTPUT
```

The runner modes remain:

```text
remote_run.sh ABSOLUTE_NEW_EVIDENCE_DIRECTORY preflight
remote_run.sh ABSOLUTE_NEW_EVIDENCE_DIRECTORY complete
```

There is no shortened cohort mode.

## Exact finite work

```text
root syntax attempts                         444
tuple attempts                            5,120
maximum final syntax count                5,564
selector orientations                    11,128
direct discovery families                 1,024
selected selector rules                     192
selected heldout direct families             64
discovery primary moduli                     896
heldout primary moduli                     1,280
all primary moduli                         2,176
discovery stage rows                      10,752
heldout stage rows                        30,720
all primary stage rows                    41,472
discovery direct-ticket cap           44,040,192
heldout direct-ticket cap              7,864,320
all direct-ticket cap                  51,904,512
child factorizations                           0
characteristic-size scans                       0
```

## Evidence repair

Primary core rows and control/alias rows use separate phase files. Discovery
selector and direct-family rows also use separate files. This makes all eleven
semantic caps independently reconstructible. The source classifies every
regular path. It enforces each semantic cap, the 8 MiB sidecar cap, the 16 MiB
log cap, the 535,822,336-byte ordinary cap, and the 536,870,912-byte absolute
cap.

The 192-byte state and eight-byte immutable-identity lock are inside the
evidence root and count as sidecars. Every writer takes `flock(2)`, verifies a full filesystem scan,
reserves before extension, closes and rescans, then commits. Checked command
pipes cover stdout and stderr. Each child acknowledges its dedicated process
group before exec. A ledger failure closes both pipes, kills that group, and
reaps its leader before the failure writer starts. Gzip output is `TRANSIENT`
until one checked commit replaces its source. Only `F269-D02.failure.tsv` can
use the final 1 MiB reserve. The failure trap is armed as soon as the ledger
exists, including during checked bootstrap imports.

The finalizer closes logs before hashing. It reserves the projected final
counters, writes a hash list that authenticates the exact future frozen ledger
bytes, syncs the list, and only then atomically commits those frozen bytes. A
crash before that commit leaves `frozen=0`. The runner read-verifies the list.
No later evidence mutation is permitted. Final PASS text is terminal-only.

## Resource closure

The runner requires and reads back cgroup-v2 memory limits, requires writable
`memory.peak` and `cgroup.kill`, and has no watchdog fallback. The authoritative wall limit is
14,400 seconds. Source work stops at 14,370 seconds. `RLIMIT_AS` is exactly
4 GiB and `RLIMIT_FSIZE` exactly 512 MiB. The worker count is one of
`{1,2,4,8}` and cannot increase after resource inspection.

The overlap gate scans complete process arguments in Bash and rejects every
other case-insensitive `f265` occurrence. It uses unlimited-width `ps` output
and does not spawn a process that contains the probe word. The runner
enumerates every external command, gates the exact `/usr/bin/env` shebang,
and checks the GNU help entries for every used nonportable option.

Each maximum-work thread allocates the real maximum `DiscoveryWorker` and
`HeldoutWorker` structures. The round simultaneously keeps real maximum
`DiscoveryAggregates` and `HeldoutAggregates` tables live. It fills real hit
sets with strings wider than production moduli, fills counterexample slots and
both production heap types with full-width integers, then updates real cells,
partitions, and heaps.
Each of seven grammar files contains the full 444-bit attempt mask and the
complete syntax-ID-ordered control-mask array; the runner recomputes and
cross-authenticates all seven.

## Execution state

```text
local compile                 NOT RUN
remote compile                NOT RUN
exact self-tests              NOT RUN
stress preflight              NOT RUN
discovery cohort              NOT RUN
heldout cohort                NOT RUN
static hostile pre-run audit  PENDING
deployment enforcement       BLOCKED BEFORE FREEZE
```
