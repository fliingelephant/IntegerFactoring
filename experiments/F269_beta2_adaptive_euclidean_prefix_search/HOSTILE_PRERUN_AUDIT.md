# Verdict: FAIL
frozen_manifest_sha256: a1d6d3493ffac3a68bee992fd524a94a8e68db7294a52c650f679ae504d4486b

## Scope and method

This was a hostile static pre-run audit of the exact F269-D01 frozen packet.
I did not compile or execute `f269.cpp`, run `remote_run.sh`, start a local or
remote cohort, or modify a frozen byte. The failure attaches to this exact
packet and sticks. A repaired packet needs a new immutable version and a new
hostile review.

Before inspecting claims, I authenticated `FROZEN.sha256`. It has exactly 11
entries. Its own SHA-256 is the value above, and `sha256sum -c` accepted every
listed file:

```text
9bf47b7c8facea2e6d23f8d07ca6b76a433c8ee9b3f314cfc40454e51c29e0ab  DRAFT_ALGEBRA.md
9179b7fe4b24f9be80a9c75afbbaed60ac432d98a31c2268726aacf22debde8b  DRAFT_PREREGISTRATION.md
d473590ea9feaabef8f03e37afc3af30827114cddce9e3cee5216d01474b6edb  ALGEBRA.md
17e9731fbc3e973679f2326cb529f72d8ad05666b42a50a219827c25d554b18e  PREREGISTRATION.md
ee5af083ba43236b92a4c52996e4134f7f40f10cb7db9997212c821482f097b4  F269-D01.baselines.tsv
0217d68c26e88a405521deaa8e9fdfefa53dd0c17e2691f531144400cfd6f78e  f269.cpp
d5f9341d57dd72c79939a38735be19b68b36795e41a4a5dac96e4c58e35d2a53  remote_run.sh
35b714fa057019b983ceffe3a8be7acd3cce94ee34325a3323cde63f978ac107  PROVENANCE.md
5b5cf78c3cc8d94f2fc5ce3fb1366be2ab3bd4f5037abd0ff78c4437ac964b59  PRELAUNCH_MANIFEST.md
4fddd1390f246ac49c66ce2818ea02804eb9e9a4169c2ef33128c4b64fe4755b  AUDIT_REQUEST.md
e236088f3dcb7ac636101f75839619513730e8c75cbd229d780f202a0e660527  VALIDATION_PENDING.md
```

I read the resolved algebra, preregistration, source, runner, provenance,
prelaunch manifest, validation state, audit request, both predecessor drafts,
and baseline. I also checked the project statement and the relevant P185,
F210, F261, F263, F265, P220, failure, registry, and progress boundaries.

## Fatal findings

### F1. Complete mode deterministically fails its own component gate

`PREREGISTRATION.md` Section 10 assigns 84,934,656 bytes to the primary
corpus and reserves 8,388,608 bytes only for manifests and sidecars.
`remote_run.sh:137-144` instead defines `sidecars` as every regular file
outside `logs/`, except the three preflight serialization/compression
transients. It therefore charges all semantic outputs, the executable, the
worker file, and preflight files against the 8 MiB sidecar cap.

The failure after discovery is forced without estimating variable fields.
`f269.cpp:1820-1835` puts two 112-byte root masks and ten 64-byte SHA-256
fields in each primary corpus row. Thus each row has at least

```text
2*112 + 10*64 = 864 bytes
```

before its other fields, tabs, or final LF. The mandatory 10,752 discovery
rows alone therefore occupy at least 9,289,728 bytes, which exceeds the
8,388,608-byte sidecar cap. `remote_run.sh:338-342` writes the corpus and then
unconditionally calls `check_components`. The runner exits there. It cannot
authenticate a selection, generate heldout, compress final evidence, or
close a complete packet.

This is independently sufficient for FAIL.

### F2. The F265 exclusion does not implement the frozen contract

`PREREGISTRATION.md:13-14`, `1996`, and `2013-2014` forbid compile,
benchmark, corpus generation, or any F269 run while an F265 production or
validation process is active. `remote_run.sh:43-48` recognizes only

```text
[F]265-D0[12].*(search|remote_run)|[f]265_search
```

It misses D03 through D07 and any F265 compiler, preflight, corpus,
validation, audit, or renamed executable whose argument string does not have
the narrow suffix. Every later `refuse_overlap` call has the same hole.

### F3. The registered checked-writer and failure-reserve protocol is absent

`PREREGISTRATION.md:1521-1535` requires one process-shared atomic logical-size
ledger, reservation before every extending write, checked shell log writers,
and a dedicated failure-manifest writer as the only consumer of the final
1 MiB reserve. The source's `checked_write_file` at `f269.cpp:1320-1334`
rescans current files and then truncates/writes; it is not an atomic shared
reservation. More importantly, `remote_run.sh` writes logs, preflight TSVs,
gzip temporaries, the compression manifest, and the final hash list through
ordinary shell redirections. Those writes bypass the source check entirely.

No failure-manifest writer or failure-manifest artifact exists in either the
source or runner. `FAILURE_RESERVE` is only a constant reported by the gate.
The promised 30-second failure closure and exact-counter preservation cannot
occur on a cap, deadline, thread, or source failure.

### F4. The final hash list is stale at the moment of success

At `remote_run.sh:399-400`, the runner hashes every existing evidence file,
including `logs/runner.log`, while stdout and stderr still append to that log.
It then calls `du_gate final_hashes` at line 401. `du_gate` prints a
`DU_PASS` line at line 134, which appends new bytes to `runner.log` after its
hash was recorded. Only afterward do lines 403-404 restore stdout and close
the log descriptors. Consequently `F269-D01.final.sha256` does not
authenticate the final `runner.log` bytes even on an otherwise successful
path.

### F5. The authoritative cgroup deadline is optional in the runner

The frozen contract says the cgroup kill is authoritative and permits no
watchdog-only fallback. The setup checks `memory.max`, `memory.swap.max`, and
`cgroup.procs`, but never requires a writable `cgroup.kill`. At
`remote_run.sh:89`, the watchdog kills the leaf only if `cgroup.kill` happens
to exist. If it is absent, the watchdog sleeps, attempts `rmdir`, and does not
enforce the 14,400-second packet deadline. Several closing commands are not
wrapped by `timeout`, so this is not repaired elsewhere.

### F6. The executable prerequisite gate is incomplete

The command inventory at `remote_run.sh:25-29` omits external commands that
the script later invokes: `dirname`, `grep`, `sleep`, `rmdir`, `mv`, `rm`,
and `xargs`. (`cut` is not invoked by this runner.) A missing command can
therefore stop the packet after the claimed prerequisite gate. The listed
but unused `readlink`, `truncate`, and `wc` do not close this defect.

### F7. The maximum-work fixture does not allocate the declared production aggregates

The preregistration requires every fresh worker round to allocate the maximum
per-worker production aggregate and witness buffers. `maximum_worker` uses a
single `vector<u64>` for all selector aggregates and six `u64` counters per
direct family (`f269.cpp:1395-1400`). Production uses 11,128
`DiscoveryRuleAggregate` objects, each with 28 full `CellStats`, separately
for every worker, plus `DirectAggregate` sets and heaps
(`f269.cpp:1978-2019`). The stress fixture therefore does not exercise the
declared production aggregate allocation or update path. Its RSS projection
is not the registered maximum-work evidence.

### F8. The grammar preflight omits required mask evidence

`PREREGISTRATION.md:1755-1766` requires each grammar repetition to report the
fixed 444-bit root-attempt mask and every retained syntax's control-case
mask. `--grammar-once` reports only counts, byte length, and one grammar
digest (`f269.cpp:3129-3141`). The self-test merely constructs the literal
attempt-mask text and checks its length (`f269.cpp:3065-3066`). No preflight
artifact contains the required mask or per-syntax mask table.

## Static reconstruction that did not produce a separate kill

I independently reconstructed these frozen definitions against the source:

- the factor-bit/reciprocal-bit conversion `e=a xor kappa`;
- the translated four-corner rectangle, six gaps, quotient-one shell, and
  branch-local `J-2K` controls;
- both ordered same-coordinate resultants, coefficient signs, evaluation
  convention, discriminants, and first-Fermat exclusion;
- exact signed `cpp_int` division, remainder, centered-remainder, bit-length,
  valuation, and value-cap semantics;
- the 14 tails, 444 root-attempt IDs, zero-gap propagation, actual-tail alias
  rejection, strict depth predicate, and unscored ninth lookahead;
- provenance unions, canonical syntax, SplitMix tuple construction, FNV
  direct-bank selection, and the selector/direct total orders;
- stateless discovery and heldout cell construction, stage counts, delayed
  hidden-label attachment, selection authentication order, exact rational
  accuracy comparisons, ticket partitions, witness heaps, and lead gates;
- the two reciprocal-orientation fixtures, three zero-gap/alias fixtures,
  two 120-bit transcript fixtures and registered digest constants, and the
  composite-Q/gcd-17 negative regression; and
- the finite count formulas: 2,176 moduli, 41,472 stage rows, 51,904,512
  direct-ticket attempts, 2,016 baseline aggregates, and the 277,979,136-byte
  registered serialization image.

This is a static consistency statement only. None of the embedded transcript
digests, primality checks, grammar counts, timing projections, memory
readings, cohort counts, or compression sizes was dynamically tested in this
audit.

## Required disposition

Do not launch this packet. Preserve its frozen bytes and this failed audit.
A new immutable version must at minimum:

1. distinguish semantic output components from manifests/sidecars, enforce
   each registered component budget, and enforce the independent global cap;
2. reject any active F265/f265 production or validation process, for every
   D-number and executable name, without matching the overlap probe itself;
3. route every evidence extension through one atomic checked ledger and
   implement the reserved failure-manifest path;
4. close all mutable logs before computing the final authenticated hash list;
5. require and read back the authoritative `cgroup.kill` facility;
6. preflight every external command actually used;
7. allocate and update the real maximum production aggregate structures in
   the stress fixture; and
8. emit the frozen root-attempt and per-syntax control-mask evidence required
   by the grammar preflight.

These are operational repairs, not permission to edit this failed packet.
