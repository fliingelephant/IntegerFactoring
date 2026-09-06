# F269-D02 hostile static audit request

This request is inactive while `FROZEN.sha256` contains the NOT-FROZEN
sentinel. Do not audit the mutable candidate.

Authenticate and read every byte named in `FROZEN.sha256`. Do not compile or
execute the source or runner during this static gate. The D01 failed audit is
lineage evidence, not a D02 verdict.

First confirm that D02 preserves the D01 algebra, grammar, cohort, hidden-label
chronology, ranking, selection, and verdict semantics. Then try to return
`KILL` for one exact defect in any of these repair gates:

1. every semantic output class has its own registered cap; sidecars, logs,
   transients, the two ledger files, exact root-relative classification, and
   the global cap cannot mask one;
2. the generic case-insensitive F265 process scan catches every D-number and
   executable/validation name without matching its own probe;
3. every evidence extension, including command stdout/stderr, shell text,
   gzip output, truncation, compression commit, and final hashes, uses one
   process-shared atomic ledger; only the failure writer can consume 1 MiB;
   a mid-command ledger failure closes pipes, kills the acknowledged child
   process group, reaps it, and only then writes that failure record;
4. all logs close before final hashing, the stable ledger files are hashed,
   final counters match, and no later evidence mutation is possible;
5. writable `cgroup.kill` is mandatory and the watchdog has no fallback;
6. every external command and every used GNU option is enumerated and gated;
7. maximum-work allocates and updates the literal production discovery and
   heldout aggregate/set/counterexample/heap structures; and
8. every grammar repetition emits the full fixed root-attempt mask and every
   retained syntax control-case mask, with count, digest, and seven-way byte
   authentication.

Also inspect for a C++17 or Bash error, component-classification ambiguity,
unchecked bootstrap evidence, failure-reserve bypass, deadline hole, or
source/contract drift.

If the packet passes, create `HOSTILE_PRERUN_AUDIT.md` with these exact first
two lines:

```text
# Verdict: PASS
frozen_manifest_sha256: <SHA-256 of FROZEN.sha256>
```

Then state what was independently reconstructed. Do not claim a dynamic test.
Any edit after the audit invalidates that audit and requires a new immutable
version and fresh review.
