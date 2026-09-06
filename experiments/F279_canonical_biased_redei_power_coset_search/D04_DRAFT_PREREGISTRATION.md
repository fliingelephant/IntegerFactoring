# F279-D04 additive authority and evaluator-interface repair

## Status, ancestry, and merge rule

F279-D04 is an unfrozen theory and interface draft. It authorizes no source,
runner, fixture, tape, source freeze, compile, self-test, benchmark,
validation, experiment, remote access, private-label access, ledger change,
git staging, or commit.

The immediate immutable inputs are:

```text
D03_DRAFT_ALGEBRA.md
d9f2fa7c490b96214e976478740257b0e6cc675f20bf7f7219760e4ca450e159

D03_DRAFT_PREREGISTRATION.md
6b5f1633e2cf2654adb8ec8bb2f79bf84a242550ef57cb4dc6cf964013413a1b

D03_HOSTILE_THEORY_AUDIT.md
859a170e6ca26d19f696559df1e7b570fc7f06a55240226fdf46cdf19e51e676
```

Read D04 additively with the complete authenticated D01-D03 chain. D04
supersedes only:

1. the D02/D03 ordering between precompile source audit and compiled-binary
   hashes;
2. the scope of source drafting authorized by a future D04 theory PASS;
3. binary-role ownership; and
4. the portable public evaluator's exact modes, arguments, descriptors,
   basenames, and status channel.

Every mathematical statement, grammar, screen, cohort, serialization,
manifest dependency, replay requirement, probability scope, workload count,
resource gate, and nonclaim from D01-D03 remains normative unless this file
explicitly changes its operator.

Every future D04 artifact uses prefix `F279-D04` and every canonical JSON
`version` is `F279-D04`. Candidate IDs, source IDs, row IDs, and their
collation do not change.

## 1. Noncircular authority stages

This section supersedes D02 Section 1 and D03 Section 2.2 only as to stage
ordering. There are seven separate states.

### 1.1 D04 theory draft

This is the present state. Only the two D04 theory/interface files may be
authored and statically checked.

### 1.2 Fresh D04 theory PASS

A strict fresh no-context audit must authenticate the exact D04 pair and the
complete D01-D03 chain. A PASS authorizes drafting only one portable public
evaluator source and binary role name:

```text
f279_public.cpp
f279_public
```

`f279_public.cpp` is one standalone C++17 translation unit. A D04 theory
PASS authorizes no second source file, generated source, vendored library,
or build output.

That PASS does not authorize a source freeze, compilation, execution,
fixture or tape creation, private-label source, runner source, containment
source, deployment manifest, or experiment.

### 1.3 Deployment decision and source completion

The user must separately choose and authorize the deployment containment.
That later decision must fix numeric UIDs, privilege transitions, the exact
network-deny mechanism, namespace or cgroup use if any, RLIMIT deployment,
process-group ownership, lock ownership, and host prerequisites.

Only a later additive interface PASS may authorize drafting the private
fixture/label role and deployment runner role. D04 itself does not authorize
those source bytes.

### 1.4 Precompile hostile source audit

After all three role sources exist under later authority, a hostile
precompile audit binds only closed text bytes:

```text
portable evaluator source
private fixture/label source
runner and containment source
exact build recipe
compiler identity recipe
```

The bound artifact is exactly `F279-D04.precompile.manifest.tsv`. Its header
is:

```text
artifact	bytes	sha256
```

It is self-excluding and has exactly these records in unsigned byte order:

```text
F279-D04.build.recipe.txt
f279_fixture_label.cpp
f279_public.cpp
f279_runner.cpp
```

The audit records byte lengths and SHA-256 hashes for those text artifacts.
It requires no compiled file and no compiled-binary hash. A binary hash is
forbidden as an input or prerequisite to this precompile verdict.

### 1.5 Exact build

Only after a precompile PASS and separate user authorization may the frozen
build recipe run. It compiles the exact audited bytes. The build produces
the first possible hashes for:

```text
f279_public
f279_fixture_label
f279_runner
```

It also creates `F279-D04.build.manifest.tsv` with the same three-column
header. That self-excluding manifest has exactly these records in unsigned
byte order:

```text
F279-D04.build.recipe.txt
F279-D04.precompile.manifest.tsv
f279_fixture_label
f279_public
f279_runner
```

No scientific mode may run merely because compilation succeeded.

### 1.6 Postcompile validation binding

The build step creates a closed build manifest that binds the precompile
source manifest, build recipe, compiler provenance, binary basenames, byte
lengths, and binary SHA-256 hashes. The authorized deployment step then
instantiates the containment manifest with the concrete binary hashes,
numeric UIDs, descriptor map, and authorized containment choices.

Validation authenticates both manifests before it runs any self-test or
capacity benchmark. It writes a postcompile validation attestation that
binds:

```text
precompile source-manifest SHA-256
build-manifest SHA-256
containment-manifest SHA-256
all three binary SHA-256 hashes
self-test result SHA-256
benchmark result SHA-256
preflight SHA-256
deployment-probe result SHA-256
validation_pass
```

The attestation basename is exactly:

```text
F279-D04.validation.attestation.json
```

Its canonical JSON keys occur in this exact order:

```text
version,precompile_manifest_sha256,build_manifest_sha256,
containment_manifest_sha256,deployment_contract_sha256,
fixture_label_binary_sha256,public_binary_sha256,runner_binary_sha256,
self_test_sha256,benchmark_sha256,preflight_sha256,
deployment_probe_sha256,validation_pass
```

Every hash is lowercase SHA-256. `validation_pass` is the Boolean `true`.
A failed validation writes no passing attestation and unlocks no scientific
mode.

The exact containment-manifest SHA-256 recorded by a passing postcompile
attestation becomes the runtime trust anchor. Promise generation and public
classification cannot precede that binding.

### 1.7 Scientific authorization

A postcompile validation PASS still does not authorize an experiment. The
user must separately authorize fixture and tape creation and the scientific
run. Live resource gates must pass at that later time.

This sequence breaks the prior cycle. Precompile audit binds source and
recipe bytes. Compile creates binary hashes. Postcompile validation binds
those hashes before any scientific mode.

## 2. Unresolved deployment inputs

D04 deliberately does not choose:

```text
runner_uid
public_uid
label_uid
network-deny implementation
Linux namespace policy
cgroup version or cgroup path
RLIMIT_NPROC value or ownership
privileged launcher mechanism
process-group and lock deployment
remote host
```

The inherited hard limits remain requirements. Their deployment mechanism
is not inferred from this draft. In particular, D04 does not approve a
numeric-UID fallback, container, user namespace, cgroup, systemd unit,
seccomp filter, firewall rule, or shell-only convention.

The portable evaluator accepts no UID, group, namespace, cgroup, network,
RLIMIT, nice, process-group, lock, or host option. It contains no constant
for any unresolved deployment value. At runtime it can compare its current
public identity and descriptor state with an already authenticated
containment manifest. It does not establish that state.

## 3. Exact binary roles and ownership

The binary role basenames remain exactly:

```text
f279_public
f279_fixture_label
f279_runner
```

### 3.1 `f279_public`

This is the only source role that a fresh D04 theory PASS can authorize for
drafting. It owns:

1. canonical public-fixture parsing;
2. public promise, input-manifest, containment-manifest, tape, and selection
   authentication;
3. exact integer and modular arithmetic;
4. the 900-source and 25,000-candidate grammar;
5. row cleanup, source and target states, endpoint computation, the finite
   relation box, controls, diagnostics, ranking, and selection;
6. public certificates, phase summaries, and canonical checksum streams;
7. exhaustive public replay of one phase per invocation;
8. deterministic serialization; and
9. the exact benchmark kernels and capacity allocation needed by D03.

It does not parse `p`, `q`, a cohort token, a local character, or a private
fixture. It does not generate primes, fixtures, a held-out seed, or tape. It
does not call `getrandom`. It does not write labels, lead, reveal, public
manifests, final replay JSON, preflight JSON, or the final evidence manifest.
It does not change UID, groups, namespaces, cgroups, RLIMITs, nice level,
network state, locks, or process groups. It does not fork, execute another
program, open a network endpoint, or accept an input path.

Scientific classification and public replay use one process. Each uses
exactly four worker threads. Worker `i` owns public row ordinals congruent to
`i modulo 4`. The calling thread performs authentication and the stable
four-way merge. It performs no candidate evaluation while workers run.
Thread creation failure aborts. There is no one-, two-, or three-worker
fallback. Self-test and benchmark modes use one thread.

### 3.2 `f279_fixture_label`

This future private role owns deterministic fixture generation, primality,
cohort predicates, cross-phase uniqueness, `getrandom`, tape creation,
promise validation, the input manifest, private-label joins, residual and
label replay, lead, seed commitment, and seed reveal. It cannot rank or
replace a candidate. D04 does not authorize its source drafting.

### 3.3 `f279_runner`

This future deployment role owns build and containment authentication,
privilege setup, fixed descriptor placement, environment cleanup, output
roots, public manifests, preflight composition, deadlines, signals, process
groups, locks, live resource gates, phase release, final replay composition,
and the final evidence manifest. It cannot compute a candidate, generate a
factor label, or reinterpret a public classification. D04 does not authorize
its source drafting.

## 4. Exact public input and output basenames

The evaluator receives descriptors, not paths. It checks these basenames in
the authenticated promise or manifest.

### 4.1 Phase inputs

```text
F279-D04.discovery.public.tsv
F279-D04.discovery.tape.bin
F279-D04.discovery.promise.json
F279-D04.heldout.public.tsv
F279-D04.heldout.tape.bin
F279-D04.heldout.promise.json
F279-D04.inputs.manifest.tsv
F279-D04.containment.json
F279-D04.discovery.selection.tsv
```

Private fixture basenames can occur only as opaque committed names and
hashes inside a promise or input manifest. The evaluator never receives a
private-fixture descriptor.

### 4.2 Discovery files written by `f279_public`

```text
F279-D04.discovery.rows.tsv
F279-D04.discovery.scores.tsv
F279-D04.discovery.selection.tsv
F279-D04.discovery.certificates.tsv
F279-D04.discovery.summary.json
F279-D04.discovery.controls.json
F279-D04.discovery.diagnostic.tsv
```

The runner writes `F279-D04.discovery.public.manifest.tsv` only after the
evaluator exits successfully and the seven files are closed.

### 4.3 Held-out files written by `f279_public`

```text
F279-D04.heldout.rows.tsv
F279-D04.heldout.scores.tsv
F279-D04.heldout.certificates.tsv
F279-D04.heldout.summary.json
F279-D04.heldout.controls.json
F279-D04.heldout.diagnostic.tsv
```

The evaluator does not write labels or lead. The runner writes
`F279-D04.heldout.public.manifest.tsv` after successful closure.

### 4.4 Replay inputs

`replay-discovery` reads the discovery public manifest, its seven files,
and the sealed selection from the phase-directory descriptor.
`replay-heldout` reads the held-out public manifest, its six files, and the
same sealed selection. Each replay invocation reconstructs its complete
phase. The runner permits private-label access only after both invocations
return passing attestations.

The two phase invocations together are the one exhaustive public replay in
D03. They do not double the D03 replay workload.

## 5. Exact descriptor contract

Descriptor numbers are:

```text
2   standard error
3   phase public fixture, read-only regular file
4   phase tape, read-only regular file
5   phase promise, read-only regular file
6   F279-D04.inputs.manifest.tsv, read-only regular file
7   F279-D04.containment.json, read-only regular file
8   sealed discovery selection, read-only regular file
9   directory descriptor
10  write end of an anonymous status pipe
```

Descriptor 9 is a new writable phase directory for `discovery` and
`heldout`, a sealed read-only phase directory for replay, and a new writable
scratch directory for `benchmark`.

The runner opens a directory descriptor read-only with directory search
permission. The evaluator creates files only with `openat` relative to that
descriptor and uses exclusive creation. A writable directory descriptor is
not required.

Descriptor 10 is an anonymous pipe. It is not a regular file, socket, or
named FIFO. The evaluator owns only its write end. Status bytes are not
scientific evidence.

The exact open-descriptor sets after `execve` are:

```text
self-test
    2,10

benchmark
    2,9,10

discovery
    2,3,4,5,6,7,9,10

heldout
    2,3,4,5,6,7,8,9,10

replay-discovery
    2,3,4,5,6,7,8,9,10

replay-heldout
    2,3,4,5,6,7,8,9,10
```

Descriptors 0 and 1 are closed. Descriptor 8 is closed in discovery mode.
No other descriptor is open. The environment is exactly `LC_ALL=C`. The
working directory is the empty public scratch directory. All inherited
descriptors have the exact access direction above. The evaluator checks the
set by querying the current descriptor limit and using `fcntl(F_GETFD)` on
every possible descriptor number. A set, type, or access mismatch is a
descriptor failure. No path fallback exists.

The D04 postcompile containment-manifest schema adds `status_fd` after
`output_dir_fd`; its exact value is `10`. The values for
`public_fixture_fd,tape_fd,promise_fd,inputs_manifest_fd,
containment_manifest_fd,selection_fd,output_dir_fd,status_fd` are exactly
`3,4,5,6,7,8,9,10`.

## 6. Exact `f279_public` command lines

`argv[0]` can contain directory components. Its basename must be exactly
`f279_public`. Every option and value is a separate argv element. Options
must occur exactly once in the displayed order. `--option=value`, an empty
value, a repeated option, a reordered option, an unknown option, or a
trailing element is a CLI failure.

`H64` below is a metavariable for exactly 64 lowercase hexadecimal bytes.
It is not a literal argv value. File-descriptor values are the displayed
single canonical decimal digits.

### 6.1 Self-test

```text
f279_public --mode self-test --status-fd 10
```

### 6.2 Capacity benchmark

```text
f279_public --mode benchmark --scratch-dir-fd 9 --status-fd 10
```

The benchmark uses the exact D03 kernels, trials, workload counts, I/O
bytes, and capacity allocation. Its only temporary basename is:

```text
.F279-D04.benchmark.io.tmp
```

It creates that file exclusively below descriptor 9 and removes it only
after close, `fsync`, reopen, and hash. A preexisting name aborts. The
scratch directory is outside every evidence root.

### 6.3 Discovery

```text
f279_public --mode discovery --public-fixture-fd 3 --tape-fd 4 --promise-fd 5 --inputs-manifest-fd 6 --containment-manifest-fd 7 --output-dir-fd 9 --status-fd 10 --trusted-containment-sha256 H64 --trusted-inputs-manifest-sha256 H64
```

### 6.4 Held-out

```text
f279_public --mode heldout --public-fixture-fd 3 --tape-fd 4 --promise-fd 5 --inputs-manifest-fd 6 --containment-manifest-fd 7 --selection-fd 8 --output-dir-fd 9 --status-fd 10 --trusted-containment-sha256 H64 --trusted-inputs-manifest-sha256 H64 --trusted-selection-sha256 H64
```

### 6.5 Discovery public replay

```text
f279_public --mode replay-discovery --public-fixture-fd 3 --tape-fd 4 --promise-fd 5 --inputs-manifest-fd 6 --containment-manifest-fd 7 --selection-fd 8 --phase-dir-fd 9 --status-fd 10 --trusted-containment-sha256 H64 --trusted-inputs-manifest-sha256 H64 --trusted-selection-sha256 H64
```

### 6.6 Held-out public replay

```text
f279_public --mode replay-heldout --public-fixture-fd 3 --tape-fd 4 --promise-fd 5 --inputs-manifest-fd 6 --containment-manifest-fd 7 --selection-fd 8 --phase-dir-fd 9 --status-fd 10 --trusted-containment-sha256 H64 --trusted-inputs-manifest-sha256 H64 --trusted-selection-sha256 H64
```

There is no fixture-generation, label, lead, seed, runner, containment,
thread-count, path, overwrite, resume, sample, or force mode in
`f279_public`.

## 7. Exact status-pipe records

The evaluator ignores `SIGPIPE` and writes status bytes with retry on
`EINTR` and positive partial writes. A zero write, `EPIPE`, or another error
is a status failure. Each invocation writes exactly one canonical JSON line
with one final LF, closes descriptor 10, and then exits. The line is at most
65,536 bytes. No other descriptor receives status JSON.

### 7.1 Self-test PASS

Keys occur in this order:

```text
version,role,mode,phase,checks,failures,status
```

The fixed values are `role="f279_public"`, `mode="self-test"`,
`phase=null`, `failures=[]`, and `status="pass"`.

### 7.2 Benchmark PASS

Keys occur in this order:

```text
version,role,mode,phase,kernel_counts,kernel_ns,read_ns_per_byte,
write_ns_per_byte,capacity_touched_bytes,checksum,status
```

`phase=null`. `kernel_counts` and `kernel_ns` use the exact D03 key order,
including the four D03 hash and diagnostic kernels. `checksum` is one
lowercase SHA-256 hash. `status` is `pass` only when every trial and
capacity allocation completes. `capacity_touched_bytes` is the exact sum of
the production-typed objects allocated and touched by the evaluator. The
future runner measures the process peak virtual bytes from the operating
system and writes `capacity_peak_bytes` into preflight. This split does not
change the D03 25-percent memory projection or 4 GiB gate.

### 7.3 Discovery or held-out PASS

Keys occur in this order:

```text
version,role,mode,phase,summary_sha256,status
```

The mode and phase are the same exact token. The evaluator writes this
record only after every mode-owned file is closed and the summary hash is
recomputed from a read-only descriptor.

### 7.4 Phase replay PASS

Keys occur in this order:

```text
version,role,mode,phase,inputs_manifest_sha256,
public_manifest_sha256,selection_sha256,endpoint_checksum,
control_checksum,diagnostic_sha256,public_replay_count,matrix_checks,
failures,status
```

The mode is `replay-discovery` or `replay-heldout`. The phase is its suffix.
`failures=[]` and `status="pass"`. All hashes are lowercase SHA-256. The
counts cover that phase only. The runner sums the two phase counts when it
constructs the final D03 replay schema.

### 7.5 Failure record

Every controlled failure writes keys in this exact order:

```text
version,role,mode,phase,status,exit_code,error_code
```

`status` is `fail`. `phase` is `null` for self-test and benchmark. If CLI
parsing fails before a valid mode exists, `mode=null` and `phase=null`.
`error_code` is exactly one of:

```text
cli
descriptor
input_auth
input_schema
input_io
output_exists
output_io
cap
arithmetic
replay
self_test
benchmark
internal
```

An external signal or inability to write descriptor 10 yields no valid PASS
record. The runner treats a missing, partial, duplicate, oversized, or
noncanonical status line as failure.

## 8. Exact exit semantics and failure closure

Exit codes are:

```text
0   exact PASS status delivered
64  CLI or role-basename failure
65  descriptor, authentication, input schema, or input I/O failure
66  output exists, output I/O, serialization, or output-cap failure
67  arithmetic or replay inconsistency
68  workload, raw-hit, global-order, or memory-cap failure
69  self-test or benchmark failure
70  internal invariant, exception, or status-channel failure
```

Exit `0` is valid only after the complete PASS record reaches descriptor 10.
A nonzero exit can leave exclusively created partial mode files. The runner
marks the whole new output root failed. It never seals, resumes, renames,
samples, truncates, or reuses that root. No byte from it can enter selection,
labels, replay, lead, or a final evidence manifest.

The runner owns the shared hard deadline. If it sends a signal, the absence
of an exact PASS status closes the phase as a resource failure. The
evaluator enforces the inherited logical caps before extending a file or
record stream. It cannot weaken a cap after observing data.

## 9. Postcompile containment and trust bytes

D04 changes the time at which `F279-D04.containment.json` becomes concrete.
It is instantiated only after exact compilation. Its keys remain the D03
keys, with `status_fd` appended after `output_dir_fd`:

```text
version,fixture_label_binary_sha256,public_binary_sha256,
runner_binary_sha256,runner_uid,public_uid,label_uid,
public_fixture_fd,tape_fd,promise_fd,inputs_manifest_fd,
containment_manifest_fd,selection_fd,output_dir_fd,status_fd
```

Append one final containment key after `status_fd`:

```text
deployment_contract_sha256
```

This hash binds a separate runner-owned deployment contract. That future
contract must specify every authorized network, namespace, cgroup, RLIMIT,
nice, process-group, and lock mechanism. Its schema and values remain
unresolved deployment inputs. The portable evaluator treats the hash as an
opaque lowercase SHA-256 value. It does not parse the deployment contract.

The build manifest and postcompile validation attestation are deployment
artifacts. Their exact schemas must be frozen by that later supplement. They
must bind the hashes listed in Section 1.6. They cannot be silently replaced
by a shell log, compiler timestamp, executable path, or human assertion.

After postcompile validation, the authenticated containment-manifest hash is
passed in the exact CLI position in Section 6. The portable evaluator hashes
descriptor 7 and compares it with that value. It then compares its running
public identity and the fixed descriptor values with the authenticated
manifest. The authenticated launcher, not the evaluator, checks the
`f279_public` binary hash before `execve`. The evaluator has no executable
path lookup, `/proc` lookup, or self-hash fallback.

## 10. Preserved evidence and resource contract

The following D03 rules are unchanged:

1. promise and input-manifest bytes and their pre-discovery chronology;
2. the public/private fixture split and label firewall;
3. ExactTape256 generation, provenance, commitments, and exact `pread`;
4. total source and candidate statuses;
5. the finite relation box and certificate priority;
6. diagnostic scan and target evidence;
7. phase public manifests, label chronology, replay JSON, seed reveal, and
   final evidence manifest;
8. all endpoint, control, diagnostic, serialization, SHA, I/O, output, wall,
   memory, and disk counts; and
9. the probability claim conditional only on `A_ctrl`.

Splitting public replay into two invocations changes no record count. The
discovery invocation reconstructs 25,600,000 nominal candidate slots and
its phase controls. The held-out invocation reconstructs the other
25,600,000 slots and its phase controls. Their sum is the one D03 public
replay workload.

No output count gains a status-pipe file. Status records travel through an
anonymous pipe and are not evidence bytes. Public manifests remain
runner-owned and retain their exact D03 record counts.

## 11. Exact next authority

This D04 pair must be released unchanged for a fresh no-context hostile
theory audit. Its authors do not grant it a PASS.

If and only if that audit passes, it may authorize drafting one standalone
C++17 portable evaluator source for role `f279_public`. It does not
authorize drafting `f279_fixture_label` or `f279_runner`, choosing
containment, freezing source, compiling, executing, creating inputs, reading
private labels, editing ledgers, staging, or committing.
