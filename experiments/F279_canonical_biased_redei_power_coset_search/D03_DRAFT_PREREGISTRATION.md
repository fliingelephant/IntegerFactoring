# F279-D03 additive preregistration repair — canonical biased Rédei power-coset search

## Status, ancestry, and merge rule

F279-D03 is an unfrozen theory-only repair. It authorizes no source, runner,
fixture, random tape, freeze, compile, self-test, benchmark, experiment,
remote access, private-label access, ledger change, git staging, or commit.

The immutable predecessors are:

```text
DRAFT_ALGEBRA.md
328c8c26d5c06e3033300539fd5900f7ddcb55f253b75fae851c58db47eea424

DRAFT_PREREGISTRATION.md
4498a4f3e2404297d6eda58036fc45e097915a13d73077dc9511dea4e6cb7e7e

D02_DRAFT_ALGEBRA.md
f87f787bad0943b7149d276e158d28a6350dc8ab72836e80112acf33240cf843

D02_DRAFT_PREREGISTRATION.md
93e207fb2e3e4c489eb009f56e16751b3df79d7ecc329b602a678761795533f9
```

Read this file with both D02 drafts. D03 supersedes only the D02 clauses
named here. Unchanged D02 clauses remain normative. Every runtime artifact
prefix and canonical JSON `version` is changed mechanically from
`F279-D02` to `F279-D03`. Candidate IDs, source IDs, row IDs, numeric
collation, grammar counts, cohort order, endpoint signs, residual exponents,
the `K=16` relation box, and the finite lead gate remain unchanged.

The normative D03 algebra repair is `D03_DRAFT_ALGEBRA.md`.

## 1. Total source and candidate state machine

This section supersedes D02 Sections 6.2, 6.3, and the affected endpoint
checksum status rules in D02 Section 12.4. It chooses the ineligible-source
repair. A proper source-level direct factor stops all targets under that
named source. The experiment does not evaluate or score an endpoint after
that factor.

### 1.1 Source chronology

For each named source, use this exact order.

1. Compute `g_eta`. A proper gcd gives terminal state
   `source_invariant_factor_eta`. A saturated gcd gives terminal state
   `source_degenerate_eta`.
2. Compute `g_delta`. A proper gcd gives terminal state
   `source_invariant_factor_delta`. A saturated gcd gives terminal state
   `source_degenerate_delta`.
3. For numeric `m=2,...,16`, compute `gcd(Q_m(t,eta),N)`. Stop at the
   first proper gcd. Its terminal state is `source_order_factor`, and its
   event is `soMM`. A saturated gcd sets its registered mask bit and does
   not stop the loop.
4. Compute `(P_B,Q_B)`.
5. Compute `g_Q=gcd(Q_B,N)` and then `g_P=gcd(P_B,N)`. Both gcds are
   computed. If `g_Q` is proper, the terminal state is
   `powered_collision_factor` with event `qb`. Otherwise, if `g_P` is
   proper, the terminal state is `half_order_factor` with event `pb`.
6. A saturated `g_Q` or `g_P` sets its registered mask bit. Saturation is
   not terminal. If no earlier proper source event occurred, the source is
   `endpoint_eligible`.

The first proper source event is final. Later target invariants, ranked
endpoints, controls, and certificates under that source are not computed.
In particular, if `g_Q` is proper modulo one hidden prime while a target
would have hit the other hidden prime, that uncomputed target is not a raw
hit. The already public `g_Q` factor is the complete classification.

A globally saturated source-order, `Q_B`, or `P_B` relation remains an
endpoint-eligible registered decoy. If its endpoint is proper, the D02
saturation mask and global certificate classification apply.

### 1.2 Candidate chronology

For each target under an `endpoint_eligible` source, compute `g_H`.

```text
proper g_H     target_invariant_factor
saturated g_H  target_degenerate
g_H=1          endpoint_eligible_candidate
```

Only an `endpoint_eligible_candidate` computes `F` and `g_F`. D02 relation
replay and certificate classification then apply without change.

### 1.3 Counts and scores

The exact meanings are:

```text
source_slots
    all 900 named sources on every one of the 1,024 phase rows

candidate_slots
    all 25,000 named candidates on every one of the 1,024 phase rows

eligible_sources
    named sources in state endpoint_eligible

eligible_candidates
    named candidates in state endpoint_eligible_candidate

raw_hits
    eligible candidates with 1<g_F<N

box_unexplained_hits
    raw hits that pass the complete registered D03 box and replay
```

Source-direct and target-invariant factors do not increment
`eligible_candidates`, `raw_hits`, either candidate score, any selection
field, or a certificate count. Global registered decoys can increment the
clean proper-endpoint score. They cannot increment the
`box_unexplained_exclusive` score.

Controls exist only for `endpoint_eligible` named sources. This control set
is fixed by public source outcomes before tape attempts are read.

### 1.4 Total endpoint-checksum serialization

The D03 endpoint checksum stream has this exact header:

```text
phase	row_id	candidate_id	status	F	g_F	classification	first_direct_event
```

It has one record for every nominal candidate slot in phase, row, candidate
numeric order. Its status is exactly one of:

```text
row_cleanup
source_invariant_factor_eta
source_invariant_factor_delta
source_degenerate_eta
source_degenerate_delta
source_order_factor
powered_collision_factor
half_order_factor
target_invariant_factor
target_degenerate
no_hit
raw_proper_hit
saturated_hit
```

The three source-direct statuses serialize as follows:

```text
source_order_factor       -  -  direct_source_order       soMM
powered_collision_factor  -  -  direct_powered_collision  qb
half_order_factor          -  -  direct_half_order         pb
```

The two proper invariant statuses use:

```text
source_invariant_factor_eta    direct_source_invariant_eta    ge
source_invariant_factor_delta  direct_source_invariant_delta  gd
target_invariant_factor        direct_target_invariant        gh
```

Their `F` and `g_F` fields are `-`. Degenerate and row-cleanup records use
`-` in all four trailing fields. `no_hit` and `saturated_hit` record `F`
and `g_F`, with `-` for classification and event. A `raw_proper_hit`
records its certificate classification and its D02 event or `-`.

The event tokens are exactly `ge`, `gd`, `gh`, `soMM`, `qb`, `pb`, or the
registered D02 orbit, target-torsion, and mixed-phase event tokens. Thus
every nominal slot has one executable status even when no endpoint exists.

Certificate rows exist only for `raw_proper_hit`. Therefore `soMM`, `qb`,
and `pb` do not occur in a D03 certificate `first_direct_event` field. They
occur in the total endpoint checksum stream. The direct orbit,
target-torsion, and mixed-phase certificate classes remain unchanged.

## 2. Promise attestation and clean descriptor boundary

This section supersedes D02 Sections 2.3 and the descriptor list in D02
Section 10.

### 2.1 Exact files and promise bytes

The phase fixture names are exactly:

```text
F279-D03.discovery.public.tsv
F279-D03.discovery.private.tsv
F279-D03.heldout.public.tsv
F279-D03.heldout.private.tsv
```

The two promise files are exactly:

```text
F279-D03.discovery.promise.json
F279-D03.heldout.promise.json
```

Each promise is one canonical JSON line under the D02 byte grammar. Its keys
occur in this exact order:

```text
version,phase,public_fixture_name,public_fixture_bytes,
public_fixture_sha256,private_fixture_name,private_fixture_bytes,
private_fixture_sha256,tape_name,tape_bytes,tape_sha256,
tape_provenance_sha256,row_count,promise_pass,
validator_binary_sha256,containment_manifest_sha256
```

The line has one final LF and is at most 4,096 bytes. `phase` is
`discovery` or `heldout`. `promise_pass` is the Boolean `true`. Every name
is the exact basename registered here. The row count is exactly 1,024. The
validator writes no promise with `promise_pass=false`; a failed validation
produces no releasable phase.

The label-aware validator joins the exact public and private fixtures by
row ID. It verifies every D02 promise, cohort count, phase count, and the
cross-phase distinct-`N` condition before it writes either promise.

### 2.2 Frozen containment trust anchor

A later implementation packet must have this exact static file:

```text
F279-D03.containment.json
```

Its canonical JSON keys occur in this exact order:

```text
version,fixture_label_binary_sha256,public_binary_sha256,
runner_binary_sha256,runner_uid,public_uid,label_uid,
public_fixture_fd,tape_fd,promise_fd,inputs_manifest_fd,
containment_manifest_fd,selection_fd,output_dir_fd
```

The descriptor values are exactly `3,4,5,6,7,8,9` in the displayed
descriptor-key order. The numeric UIDs and binary hashes must be concrete
before a static implementation PASS. The exact SHA-256 of this containment
manifest is the trust anchor recorded by that PASS and supplied to the
authorized launcher. No runtime-generated attestation can replace it.

Before fixture validation, the launcher authenticates the containment
manifest against that trusted hash and authenticates all three binaries
against the manifest. The promise repeats the authenticated validator hash
and containment-manifest hash. A mismatch aborts before discovery.

### 2.3 Exact public exec boundary

Immediately before `execve` of `f279_public`, the runner places these
read-only descriptors at fixed numbers:

```text
3  phase public fixture
4  phase ExactTape256 file
5  phase promise JSON
6  F279-D03.inputs.manifest.tsv
7  F279-D03.containment.json
8  sealed discovery selection, held-out only
9  new public output directory, opened as a directory
```

Descriptor 8 is closed in discovery mode. Standard error is descriptor 2.
No other descriptor remains open. The environment is exactly `LC_ALL=C`.
The working directory is the empty public scratch directory. The process
has already dropped permanently to the public UID.

The exact semantic arguments name the phase and descriptor numbers. They
also carry the trusted containment-manifest hash and the input-manifest hash
that the runner computed before it opened any discovery output. They carry
no fixture path, tape path, private path, seed, cohort, or factor label.

Before it evaluates one row, `f279_public`:

1. hashes descriptor 7 and compares it with the trusted containment hash;
2. checks the promise validator hash against that manifest; the launcher
   has already authenticated the running public binary before `execve`;
3. parses descriptor 6 and checks its exact precommitted hash;
4. hashes descriptors 3, 4, and 5 and checks their manifest and promise
   records;
5. checks every promised filename, byte length, phase, row count, and
   `promise_pass=true`; and
6. in held-out mode, authenticates descriptor 8 against the discovery
   selection hash.

Any missing descriptor, extra descriptor, writable input descriptor,
nonregular input, hash mismatch, byte mismatch, owner or mode mismatch,
parse difference, or phase mismatch aborts. The public process does not
accept a path fallback.

## 3. Input commitment manifest and tape provenance

### 3.1 Pre-discovery input manifest

The label-side setup closes all committed inputs before discovery. It then
writes exactly:

```text
F279-D03.inputs.manifest.tsv
```

Its exact header is:

```text
artifact	bytes	sha256
```

It has exactly these eleven records in unsigned byte order:

```text
F279-D03.containment.json
F279-D03.discovery.private.tsv
F279-D03.discovery.promise.json
F279-D03.discovery.public.tsv
F279-D03.discovery.tape.bin
F279-D03.heldout.private.tsv
F279-D03.heldout.promise.json
F279-D03.heldout.public.tsv
F279-D03.heldout.tape.bin
F279-D03.heldout_seed.commitment.json
F279-D03.tape.provenance.json
```

The manifest contains basenames, not paths. Each byte count and hash is for
an already closed regular file. The manifest excludes itself. It is created
with exclusive creation, closed, made read-only, and hashed before the
discovery output directory is opened. Its retained hash is written into
both phase summaries and the final evidence manifest.

The manifest is the authenticated artifact that commits both complete tape
files before selection. Its private-fixture rows expose only names, byte
counts, and hashes to the public process.

### 3.2 Tape and held-out-seed generation

The ExactTape256 file names and sizes are exactly:

```text
F279-D03.discovery.tape.bin  176947200 bytes
F279-D03.heldout.tape.bin    176947200 bytes
```

The label-side setup uses the Linux `getrandom` system call with `flags=0`.
It first requests the 32-byte held-out fixture seed. It then fills discovery
tape and held-out tape in that order. Each request asks for at most
1,048,576 remaining bytes.

For a `getrandom` call:

1. a positive partial return advances by exactly that many bytes;
2. `EINTR` increments the retry count and retries the unchanged suffix;
3. a zero return is failure;
4. any other error is failure; and
5. no byte source, PRNG expansion, retry cap, or substitute API is allowed.

Each destination starts as a label-owned exclusive `.partial` regular file.
Writes retry `EINTR` and partial writes over the unchanged byte suffix. A
zero write or another write error fails. SHA-256 is updated over the exact
bytes in file order. After the exact size is written, setup calls `fsync`,
closes, reopens read-only, hashes and checks the complete file, and renames
it without replacement to its registered final name. It never maps a tape.

The success provenance file is exactly:

```text
F279-D03.tape.provenance.json
```

Its canonical JSON keys occur in this exact order:

```text
version,entropy_api,flags,request_chunk_bytes,
heldout_seed_requested_bytes,heldout_seed_returned_bytes,heldout_seed_calls,
discovery_requested_bytes,discovery_returned_bytes,discovery_calls,
heldout_requested_bytes,heldout_returned_bytes,heldout_calls,
partial_returns,eintr_retries,discovery_tape_sha256,
heldout_tape_sha256,status
```

The exact tokens are `entropy_api="linux_getrandom"` and `status="pass"`.
The numeric fields record actual calls and returns. The provenance file is
closed before the input manifest and is authenticated by it.

The held-out seed commitment file is exactly:

```text
F279-D03.heldout_seed.commitment.json
```

Its keys are exactly `version,domain,sha256`. `domain` is
`F279-D03-heldout-seed`, and the hash is the inherited D02 domain-separated
commitment to the 32 seed bytes. The seed itself remains in the label-only
root until the final reveal.

On failure, setup never renames a partial tape and never writes the input
manifest. If possible, it writes one non-evidence failure record named
`F279-D03.tape.failure.json` in the label-only failure root. Its keys are:

```text
version,stage,tape,requested_bytes,returned_bytes,calls,
partial_returns,eintr_retries,errno,status
```

`stage` is exactly `open`, `getrandom`, `write`, `fsync`, `close`,
`reopen`, `hash`, or `rename`. `tape` is `heldout_seed`, `discovery`, or
`heldout`. `status` is `fail`. Failure to write this diagnostic does not
permit continuation.

### 3.3 Exact tape read semantics

Before controls, the public process checks the tape descriptor size and
SHA-256. For one assigned block, it uses `pread` at the exact D02 byte
offset until exactly 32 bytes arrive.

```text
positive partial read  advance by the returned byte count
EINTR                  retry the unchanged suffix
zero before 32 bytes   abort the phase
other error            abort the phase
bytes beyond offset+32 never enter this block
```

There is no mutable stream position and no `mmap`. Replay repeats the full
tape authentication and the same `pread` rule.

These procedures record provenance. They do not prove physical entropy.
The probability model remains the declared independent uniform tape sample
space, with the narrow conditioning in Section 9.

## 4. Closed-file hashes and public evidence manifests

This section supersedes the D02 successful output list and the affected
summary and replay schemas.

### 4.1 Successful evidence files

Discovery produces:

```text
F279-D03.discovery.rows.tsv
F279-D03.discovery.scores.tsv
F279-D03.discovery.selection.tsv
F279-D03.discovery.certificates.tsv
F279-D03.discovery.summary.json
F279-D03.discovery.controls.json
F279-D03.discovery.diagnostic.tsv
F279-D03.discovery.public.manifest.tsv
F279-D03.discovery.labels.tsv
```

Held-out produces:

```text
F279-D03.heldout.rows.tsv
F279-D03.heldout.scores.tsv
F279-D03.heldout.lead.tsv
F279-D03.heldout.certificates.tsv
F279-D03.heldout.summary.json
F279-D03.heldout.controls.json
F279-D03.heldout.diagnostic.tsv
F279-D03.heldout.public.manifest.tsv
F279-D03.heldout.labels.tsv
```

The packet-wide evidence files are:

```text
F279-D03.inputs.manifest.tsv
F279-D03.preflight.json
F279-D03.replay.json
F279-D03.heldout_seed.commitment.json
F279-D03.heldout_seed.reveal.json
F279-D03.tape.provenance.json
F279-D03.discovery.promise.json
F279-D03.heldout.promise.json
F279-D03.evidence.manifest.tsv
```

Fixtures, tapes, and the static containment manifest are committed inputs.
Their exact hashes occur in `F279-D03.inputs.manifest.tsv`. They are not
classification-output bytes.

### 4.2 Phase close order and summary hashes

For discovery, close files in this dependency order:

1. rows, scores, certificates, controls, and diagnostic;
2. selection;
3. summary; and
4. public manifest.

For held-out, close rows, scores, certificates, controls, and diagnostic;
then close summary; then close the public manifest. Labels and lead do not
exist yet.

The D03 summary keys occur in this exact order:

```text
version,phase,promise_sha256,inputs_manifest_sha256,
containment_manifest_sha256,public_fixture_sha256,tape_sha256,
selection_sha256,row_count,cleanup_rows,eligible_rows,source_slots,
candidate_slots,raw_hits,box_unexplained_hits,global_order_checks,
operation_counts,output_bytes,rows_sha256,scores_sha256,
certificates_sha256,controls_sha256,diagnostic_sha256,endpoint_checksum
```

Both phase summaries record the sealed discovery selection SHA-256.
`output_bytes` is the sum of the already closed phase files that precede
the summary. The public manifest later accounts for the summary itself.

The `operation_counts` keys occur in this exact order:

```text
pair_muls,mod_muls,gcds,inverses,matrix_muls,sha256_contexts,
sha256_updates,sha256_bytes,tape_blocks,endpoint_checksum_records,
control_checksum_records,diagnostic_scan_records
```

### 4.3 Exact public manifests

Each public manifest has the exact header:

```text
artifact	bytes	sha256
```

Rows use unsigned byte order by basename. The discovery manifest lists
exactly these seven already closed files:

```text
F279-D03.discovery.certificates.tsv
F279-D03.discovery.controls.json
F279-D03.discovery.diagnostic.tsv
F279-D03.discovery.rows.tsv
F279-D03.discovery.scores.tsv
F279-D03.discovery.selection.tsv
F279-D03.discovery.summary.json
```

The held-out manifest lists exactly these six already closed files:

```text
F279-D03.heldout.certificates.tsv
F279-D03.heldout.controls.json
F279-D03.heldout.diagnostic.tsv
F279-D03.heldout.rows.tsv
F279-D03.heldout.scores.tsv
F279-D03.heldout.summary.json
```

Every listed file is closed and reopened read-only before hashing. A
manifest excludes itself. Its hash enters the later replay JSON and final
evidence manifest.

### 4.4 Label, lead, replay, reveal, and final manifest hashes

After the chronology in Section 5 permits labels, the label process closes
both label files and the held-out lead file. Replay then authenticates them.
The D03 replay JSON keys occur in this exact order:

```text
version,inputs_manifest_sha256,discovery_public_manifest_sha256,
heldout_public_manifest_sha256,public_fixture_auth,
public_manifest_complete,score_match,selection_match,certificate_match,
diagnostic_match,control_match,public_replay_count,label_replay_count,
matrix_checks,residual_checks,discovery_labels_sha256,
heldout_labels_sha256,lead_sha256,failures,replay_checksum,replay_pass
```

After replay passes, the label process writes
`F279-D03.heldout_seed.reveal.json`. Its keys are exactly
`version,seed_hex,commitment_sha256,reveal_status`. `seed_hex` is exactly
64 lowercase hexadecimal digits, and `reveal_status` is `pass`. Replay or
the runner verifies the commitment before final sealing.

The final `F279-D03.evidence.manifest.tsv` uses the same three-column
manifest header. It lists every successful evidence file in Sections 4.1
through 4.4 except itself, in unsigned byte order. It therefore hashes both
phase public manifests, both label files, lead, replay, preflight, promises,
input manifest, provenance, commitment, and reveal. The input manifest in
turn commits fixtures, tapes, and containment bytes. The final manifest is
the only self-excluding root. Its SHA-256 is the final runner result and is
recorded in the immutable run log outside the evidence directory.

No output is opened for extension after its hash enters a later artifact.
Every writer uses exclusive creation. No mode overwrites, repairs, or
appends to a sealed file.

## 5. One seal, release, label, and replay chronology

This section supersedes both D02 label-access chronologies.

1. Before candidate evaluation, the label-aware validator may read private
   labels only to create and validate fixtures, promises, tapes, and the
   input manifest. It then seals the private roots.
2. The discovery public process authenticates its clean descriptors. It
   writes and closes every discovery public file through the discovery
   public manifest. It reads no private label.
3. The runner rehashes every discovery manifest entry, validates the exact
   file set, authenticates the selection bytes and hash, and seals the
   discovery public directory. This is the selection seal.
4. Only after that seal, the label process releases read-only descriptors
   for the held-out public fixture and tape. It releases no private fixture,
   held-out seed, or cohort token.
5. The held-out public process authenticates the held-out promise, input
   manifest, fixture, tape, and sealed selection. It writes and closes every
   held-out public file through the held-out public manifest.
6. Public replay now reads both authenticated public fixtures, both tapes,
   the selection, and both public manifests. It exhaustively reconstructs
   both phases, including diagnostic evidence. Both public manifests must
   match before any post-classification private-label access.
7. Only after public replay passes may the label process reopen the two
   private fixtures. It writes the two label files and the held-out lead
   file from already sealed public certificates and selection bytes.
8. Label replay verifies promises, factors, cohorts, local characters,
   residual equations, matrix checks, label rows, and the lead gate. It
   cannot change a public byte.
9. Replay JSON closes. The held-out seed reveal then closes and verifies its
   commitment. The final evidence manifest closes last.

Labels can veto a certificate or lead. They cannot add a hit, change a
public classification, rerank a candidate, replace selection, change a
diagnostic record, or repair an output.

## 6. Complete high-order diagnostic evidence

This section supersedes D02 Section 8 and adds its missing evidence,
replay, and capacity contract. The diagnostic still runs only on the 32
registered rows and never enters ranking or the lead gate.

### 6.1 Exact scan state machine

For a diagnostic row that survived row cleanup, put `D0=n` and
`A0=D0^2+D0`. For numeric `a=2,...,A0`:

1. Screen `gcd(a,N)`. A proper gcd stops the diagnostic row with
   `diagnostic_factor` and exponent `0`. A saturated gcd rejects the base.
2. For a unit base, update `a^e mod N` incrementally for numeric
   `e=1,...,D0` and screen `gcd(a^e-1,N)`.
3. The first proper gcd stops the diagnostic row with
   `diagnostic_factor`. The first saturated gcd rejects that base and moves
   to `a+1`.
4. If all `D0` exponent gcds are one, retain that first base and stop the
   scan with `retained`.
5. Exhaustion without a retained base gives `diagnostic_shortfall`.

No scan outcome aborts the phase. A diagnostic factor is public control
evidence only. A shortfall does not change rows, selection, or the lead
gate.

For the internal scan checksum, hash this exact unwritten TSV stream:

```text
phase	row_id	base	exponent	value	gcd	outcome
```

`exponent=0` denotes `gcd(a,N)` and uses `value=a`. A positive exponent
uses `value=a^e-1 mod N`. `outcome` is exactly `one`, `proper`, or
`saturated`. Records use scan order and stop exactly with the state machine.

### 6.2 Exact target evidence

For a retained base `z`, construct the inherited split source and evaluate
the 90 target IDs

```text
dJ-vVV
```

in numeric `(J,VV)` order, with `J=0,...,8` and `VV=00,...,09`. Apply the
D03 source terminal state, target invariant, endpoint, and complete
registered `K=16` relation-box chronology. Every one of the 90 nominal
targets gets one record. These outcomes do not update a ranked count.

Each phase diagnostic file has this exact header:

```text
phase	row_id	N	B	D0	A0	scan_status	stop_base	stop_exponent	direct_factor	retained_z	bases_screened	exponent_checks	scan_checksum	target_id	target_status	t	eta	v	P_B	Q_B	F	g_P	g_Q	g_F	classification	first_direct_event
```

`scan_status` is exactly `row_cleanup`, `diagnostic_factor`,
`diagnostic_shortfall`, or `retained`. A non-retained row writes one record
with `target_id=-` and absent target fields. A retained row writes exactly
90 records and repeats the scan fields. `target_status` is exactly one of:

```text
powered_collision_factor
half_order_factor
target_invariant_factor
target_degenerate
no_hit
raw_proper_hit
saturated_hit
```

The target classification and direct-event fields use the exact Section 1
serialization. They are diagnostic fields only and never enter a ranked
count. For `row_cleanup`, `scan_checksum` is `-`. For every other scan
status, it is the SHA-256 of the exact scan stream, including its header.
For `diagnostic_factor`, `stop_base`, `stop_exponent`, and `direct_factor`
are present. For `retained`, `stop_base=retained_z`,
`stop_exponent=D0`, and `direct_factor=-`. For
`diagnostic_shortfall`, all four stop, factor, and retained fields are `-`.

Each phase has at most 1,440 diagnostic records. Each record, including LF,
has a hard cap of 1,024 bytes. Public replay recomputes the full scan stream,
its checksum, all target records, all registered decoy checks, and every
literal matrix equality. An omitted, added, reordered, or altered diagnostic
record fails replay.

### 6.3 Worst-case diagnostic work

Every diagnostic modulus has `D0<=112` and `A0<=12656`. There are exactly
32 potential diagnostic rows. A conservative packet-wide primary cap is:

```text
base gcd checks
    32*(12656-1) = 404960

exponent gcd checks
    32*(12656-1)*112 = 45355520

all diagnostic scan gcd checks
    45760480

diagnostic target evaluations
    32*90 = 2880
```

Public replay doubles these caps. They are charged in Section 8. No timing
projection may use an observed early retained base.

## 7. Replay completeness after D03 repairs

The D02 exhaustive public replay list remains normative and gains these
requirements:

1. authenticate both promises, the containment trust anchor, and the input
   manifest;
2. reconstruct the total source state and every nominal endpoint-checksum
   status in Section 1;
3. reconstruct every inspected control attempt and the control checksum;
4. reconstruct all diagnostic scan checksums and target records;
5. authenticate both exact public manifests before label access; and
6. verify the hashes of labels and lead before `replay_pass=true`.

`public_replay_count` remains the number of nominal ranked candidate slots.
Diagnostic target records are counted separately in `operation_counts`.
The failure-code vocabulary gains exactly `promise`, `input_manifest`,
`diagnostic`, `public_manifest`, `labels`, and `lead`.

The label process writes one label row for each public ranked certificate,
as in D02. Source-direct slots have no certificate and no label row.

## 8. Corrected benchmark and conservative preflight

This section supersedes D02 Sections 14.2 and 14.3 where stated. Existing
D02 kernel definitions and counts remain unchanged. Add these exact
maximum-count kernels:

```text
endpoint_stream_hash   102400000
control_stream_hash     22118400
diagnostic_scan         91520960
diagnostic_target           5760
```

`endpoint_stream_hash` serializes one maximum-width D03 endpoint checksum
record and updates one streaming SHA-256 context. `control_stream_hash`
does the same for one maximum-width D02 control checksum record. Each trial
initializes one context, performs 4,096 record updates, and finalizes it.
The measured kernel includes integer formatting, TAB and LF bytes, buffer
copy, SHA-256 update, and checksum finalization amortized over the trial.

`diagnostic_scan` performs one worst-width incremental modular-power step,
one gcd, one maximum-width scan-record serialization, and one streaming
SHA-256 update. This deliberately overcharges base-gcd records that need no
power multiplication. `diagnostic_target` performs one complete clean
target invariant, endpoint, all registered decoy screens, literal matrix
control, maximum-width diagnostic record serialization, and hash update.
It deliberately charges the full relation box for every diagnostic target.

These four keys follow `label_serialize` in both `kernel_counts` and
`kernel_ns`. They use the same seven trials, 4,096 iterations, maximum-trial
ceiling rule, one core, and volatile checksum as the D02 kernels.

The counts include primary evaluation and one exhaustive public replay.
The endpoint and control streams are hashed but not written. Therefore their
serialization and SHA cost enters `work_ns` only through the two explicit
hash kernels. It is not hidden in candidate arithmetic or file I/O.

Use these revised byte constants:

```text
tape_read_bytes = 5*353894400 = 1769472000
output_bound_bytes = 281186304
artifact_read_bytes = 3*281186304 = 843558912
```

The work formula remains:

```text
work_ns = sum(kernel_count[k]*kernel_ns[k])
        + (tape_read_bytes+artifact_read_bytes)*read_ns_per_byte
        + output_bound_bytes*write_ns_per_byte

projected_wall_seconds
    = 600 + ceil(2*work_ns/1000000000).
```

The wall gate remains 14,400 seconds. The factor `2` gives no parallel
speedup credit. Tape creation retains its separate inherited deadline and
must also satisfy the exact provenance protocol.

The revised successful-output caps are:

```text
certificate records       131072*1536 bytes
label records             131072*384 bytes
score records              50000*256 bytes
row records                 2048*512 bytes
selection and lead           256*256 bytes
diagnostic records          2880*1024 bytes
manifest records              64*256 bytes
at most 12 JSON files        12*1048576 bytes
16 TSV headers                16*4096 bytes
```

Therefore:

```text
output_bound_bytes
  = 131072*1536
  + 131072*384
  + 50000*256
  + 2048*512
  + 256*256
  + 2880*1024
  + 64*256
  + 12*1048576
  + 16*4096
  = 281186304.

projected_output_with_margin
  = ceil(5*281186304/4)
  = 351482880.
```

The margin remains below 512 MiB. The hard aggregate classification-output
cap remains `536870912` bytes. Fixtures and the two fixed-size tapes are
inputs. The live disk gate must include their bytes plus this output bound,
temporary-file headroom, and the inherited 2 GiB minimum free-space rule.

The capacity allocation must also touch the diagnostic row buffer, three
streaming SHA-256 contexts, the exact manifest tables, and the expanded
operation counters. The inherited 25-percent virtual-memory projection and
4 GiB gate remain unchanged.

No measured endpoint rate, control attempt rate, early diagnostic success,
private label, cohort result, or thread speedup can reduce a projected
count.

## 9. Exact control probability scope

This section supersedes the last sentence of D02 Section 7.3.

Fix public fixtures and all public source eligibility. For each eligible
control `i`, let `A_i` mean that one of its three assigned attempts is
accepted. Let `A_ctrl` be the intersection of these control-local events.
Conditional on `A_ctrl`, accepted controls are independent and exactly
projective-uniform, as proved in the D03 algebra repair.

D03 makes no probability claim conditional on phase success, packet
success, runtime completion, a resource gate, a checksum, replay, or a lead.
Those events may depend on control attempt paths. A realized tape that
aborts has no replacement, and no conditional hit-rate claim is reported
for it.

## 10. Preserved gates and interpretation

All unchanged D02 authorization states, fixture grammar, deterministic
cohort generation, cross-phase uniqueness, selection tuple, finite lead
gate, runtime containment contract, and mathematical nonclaims remain in
force.

In particular:

1. `box_unexplained_exclusive` remains relative only to the registered
   finite D03 box.
2. The high-order lane remains an unranked diagnostic.
3. ExactTape256 states a mathematical sample space. Provenance does not
   prove physical entropy.
4. A finite lead is discovery evidence only.
5. A resource, entropy, fixture, containment, checksum, manifest, or replay
   failure is not mathematical evidence.

No source or runner may be drafted until this exact D03 algebra and
preregistration pair receives a fresh no-context theory PASS. No compile or
execution may occur from a theory PASS. Later source, schemas, containment,
and resource code need their own static hostile PASS and a new immutable
freeze. The user must still explicitly authorize the containment workflow
and any experiment.
