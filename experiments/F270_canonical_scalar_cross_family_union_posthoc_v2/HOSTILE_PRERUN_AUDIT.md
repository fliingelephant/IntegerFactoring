# F270-D02 hostile static pre-run audit

verdict: REVISE
frozen_manifest_sha256: 91468b7190d3b1feb88f644fd3b1d7f95d1dbb462c41a980d8b88d2c1fbeccdf8c

## Scope and authentication

This is a launch-blocking static verdict. Do not compile or execute F270-D02.
Preserve this packet and audit. A repair requires a new frozen D03 packet and a
fresh hostile pre-run audit.

I did not compile the source or run its self-test, preflight, target, runner, or
any remote command. I did not edit a frozen file or a ledger.

Before inspecting claims, I authenticated the exact `FROZEN.sha256` root above
and every record in it:

```text
873a59f560a32bfc9a15ff288554168961c4c15c38b1d7f1d896d13d97b7fe2f  POSTHOC_PROTOCOL.md
42f7e2420dbddb80f4916dd592f77112b1ef7005162d1e5f89878484b844e04f  RESOURCE_ESTIMATE.md
18501b46f051b99c0fc7c84bbbe022bf8642c43a7046870553192cb839d3e254  f270_union.cpp
b766f501f1788049fa395c66f532385c6ff364624b111fe6881481ce30272843  remote_run.sh
03eeb1bf996f342954c822c889cf58b03cd3b29747f68e8007063ed94d3cb2cc  PRELAUNCH_MANIFEST.md
fb0e2cd31ae5b1dbee5d1480f94c1dd21016644aee416ec7dcefc9f8e68844d5  STATIC_AUDIT_REQUEST.md
```

I also authenticated and read the complete D01 packet. Its frozen root is
`4fe9f85f7a52f7e6fce505d6165cd223e4ec394de5c536dfca6bc474398efe2f`.
Its immutable failed audit authenticated at
`74c9c078b94a89f81db7891c2d51546978087895c8265b23196aa2c870c3f730`.

## Launch blocker: the process firewall is not generic or complete

The new exclusive lock is effective only for packets that cooperate by opening
`/tmp/integer_factoring.production.lock`. The prelaunch scan must therefore
detect an already-running legacy or noncooperating production runner.

It does not. `remote_run.sh:177-190` recognizes only these forms:

1. a literal `--mode` followed by one of five mode words;
2. a literal mode option such as `--target`; or
3. an `F` plus exactly three digits, followed later in the same argument string
   by one of a short list of words.

For example, this nonancestor process is visibly a runner but matches none of
those expressions when its paths are generic:

```text
bash remote_run.sh /data/e.tsv /data/b.tsv /data/c.tsv /data/legacy-run 8 <root>
```

A legacy runner need not hold the new lock. F270-D02 can therefore observe that
process in its complete `ps` input, set `PROCESS_FIREWALL=PASS`, and proceed
concurrently. This contradicts checklist item 16 and the protocol claim that
the generic scan rejects every other production runner. The bound and hash of
the snapshot do not repair a false-negative classifier.

The claimed exact self-exclusion is also not proved. `remote_run.sh:169-176`
walks at most 16 parents and does not require that the walk reached PID 1. Thus
the recorded exclusion can be a silently truncated prefix rather than the exact
ancestor chain required by checklist item 16.

## Checks that otherwise survive static attack

The D01-approved arithmetic chronology is preserved. The global `case_index`
join remains distinct from the corpus cell-local `index`; only `ROW` evidence
enters arithmetic; every equal-value root pair is compared before deduplication;
the union block system is recomputed and reconstructed; original and family
ranks expand all provenance; peeling is simultaneous to a fixed point; and the
fixed-core singleton, support-two, and complete residual-quotient logic is
unchanged. Relation authentication still checks the exact root, supplied root,
normalization, both signed gcds, and root class. Clean/control and held-out
status logic remain restricted as specified, including the literal all-empty
core kill and absence of a direct gcd screen.

D02 also repairs the D01 resource defects in the source: it checks all 284 row
values before deduplication, shares the union/core refinement-step counter,
atomically reserves each relation count and exact final line bytes before the
case-vector append, cancels concurrent generation after a failed reservation,
streams deterministic case-ordered batches of at most eight, reserves every
other write, keeps bounded aggregates and witnesses, and checks final file
sizes against the exact ledger.

The runner otherwise supplies the required absolute deadline and closure
reserves, cgroup-v2 and RLIMIT containment, raw/log/packet gates, compression
transient inequality, deterministic tar/gzip construction, raw per-file hashes,
archive hashes, and a final hash inventory with no later in-tree mutation on the
success path. These checks do not override the process-firewall blocker.

## Minimal D03 repair

Create a new frozen packet. Keep the arithmetic and resource changes. Replace
the process classifier with a bounded PID-sorted scan that checks every
nonexcluded process's command line, executable path, and working directory.
At minimum, reject a nonancestor `remote_run` or `remote_run.sh` independently
of an F-number, argument order, or path spelling. Retain the semantic mode and
production-workload checks. Treat every read failure, PID-snapshot inconsistency,
or byte overflow as rejection.

Enumerate parents until PID 1. Apply a finite depth/byte cap, but reject if the
cap is reached before PID 1; do not silently truncate. Exclude only that proved
chain and the identified watchdog process. Bind the resulting complete
snapshot, exact exclusions, and literal firewall PASS into the same archived
and final evidence. Then freeze D03 and obtain a fresh static audit before any
dynamic action.
