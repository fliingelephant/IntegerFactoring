# F265-D18 draft preregistration amendment — exact transient RATE_IO lifecycle

## Status and exact imports

This is an unfrozen theory-only additive draft. It creates no source, fixture
byte, runner, manifest, freeze, compilation, preflight, execution, result, or
ledger entry. It authorizes none of those actions by itself.

| Artifact | SHA-256 |
|---|---|
| `D09_DRAFT_ALGEBRA.md` | `93ee6021b969a3624cf499df5e18ea9c262e2a095a6b0634644cc1d69ee8030d` |
| `D09_DRAFT_PREREGISTRATION.md` | `3b499578678a0f71c75f52608e53f2fba7f390fb5a09a95bc20c61d09fe1c0a4` |
| `D10_DRAFT_ALGEBRA.md` | `aab2397c601b645f71da0bc79a8f58ed9ef79ea984fa7f7458ab2a49582a17a7` |
| `D10_DRAFT_PREREGISTRATION.md` | `be7e2a05a1eac6659000cdfe71469697d76b867b42cb60c1c244b06ec63afb6e` |
| `D11_DRAFT_ALGEBRA.md` | `a177438e425a20550342e7efa94ec1f70d30f40fe204640f983435dc36554f27` |
| `D11_DRAFT_PREREGISTRATION.md` | `9b477799e006a9b2bb49eebcf062917f1a3c91a9852ce8fbe825fcea1a1df23e` |
| `D11_HOSTILE_THEORY_AUDIT.md` | `777ccd163959a7ec4e14bdcd3c9d12fc1d58732207f12520806e1ad2a2705246` |
| `D12_DRAFT_ALGEBRA.md` | `eae660da5a5c5344b83ccd99301cfb4f2db89d5c259cf73194f85892e2d7dcb0` |
| `D12_DRAFT_PREREGISTRATION.md` | `65682542478a2c2270f3657d2c741ea253445ad3cf160758449a0ce21e806ecd` |
| `D13_DRAFT_ALGEBRA.md` | `915ec124f6be79a1530af3df628f8c65eaa5bde845f073f67f5077e66258ea9c` |
| `D13_DRAFT_PREREGISTRATION.md` | `42667461ac3a21820f3ea1d5de545d17ff03c719a38cd405dbdb0e91ff083c17` |
| `D14_DRAFT_ALGEBRA.md` | `42690a13d5a0fade1dd644bf29d299d9bab3b5cdd6a68d08354f1e9a5c6fb4f6` |
| `D14_DRAFT_PREREGISTRATION.md` | `4b02e30cfe2986fbc04dbf8c4faf22743c18acb1a64d2a07b30eefe2c6338b9b` |
| `D14_HOSTILE_THEORY_AUDIT.md` | `b7067c104eaf96dfa81d7bd08dcc9326e7616016fb66202c078bf1c2ea5ef03e` |
| `D15_DRAFT_ALGEBRA.md` | `563293afda1cf4d183b4d70ec30da60d0339086a52d9395df8b4d70d1e7ceeb6` |
| `D15_DRAFT_PREREGISTRATION.md` | `9c3b7cc4d855e906d8c9f35bcf7846631d28d728138df07f0e812cf59c12798d` |
| `D16_DRAFT_ALGEBRA.md` | `10d0e74462aac944a32dbc68404aa30c730d1f5b919f1fb4dd9e5a76ae92f5b2` |
| `D16_DRAFT_PREREGISTRATION.md` | `8a27d1d3af5b6f46d5f90e2f3545928cde55932c8012c6829b7c67207bd556a2` |
| `D17_DRAFT_ALGEBRA.md` | `e784dfb9d151e816ef43644e480e705c7414d4af34114250da7d399c319d46d3` |
| `D17_DRAFT_PREREGISTRATION.md` | `acd92da342f2f88667a6b3cbfc3be1c13e9f8fdeabf4789020f3472319ed62d3` |
| `D17_HOSTILE_THEORY_AUDIT.md` | `fc068523f2d45f1a853aac1db860fc64ccb66f6ffbf8f8f8b372a2ed3937f638` |
| `D18_DRAFT_ALGEBRA.md` | `6a163bb4a642760f41a5d0fab0b5bbea40e936eef2dff93921b65fe7c7ce815d` |

Read all twenty-two authenticated bytes in full. Apply only the replacements
and additions below. Every D09--D17 clause not explicitly replaced by D18
survives literally. Preserve every predecessor byte.

D18 replaces every future source-version token `F265-D17`, executable prefix
`f265_d17_`, artifact prefix `F265-D17.`, and fixture-root placeholder prefix
`F265_D17_` by the corresponding D18 token. The four source roles, eight
modes, ten invocation grammars, option names, scientific schemas, final
artifact memberships, caps, and role restrictions otherwise survive exactly.

## 1. Preflight-owned ephemeral object names

Only `f265_d18_public --mode preflight` may create the two names in this
section. It creates them only through its retained, already validated
`--output-root` descriptor:

```text
F265-D18.RATE_IO.bin
.F265-D18.RATE_IO.bin.tmp
```

The first is the ephemeral final basename. The second is its sole temporary,
using D13's dot-prefix and `.tmp` convention. They are fixed source constants;
no command-line value, environment value, current working directory, fixture
field, or implementation choice can rebind them.

These names are a narrow exception to D12's ordinary fixed-output-membership
sentence. They are legal only during one `RATE_IO` repetition. They are never
legal in a materializer, verifier, evaluate, replay, seal-public,
diagnostics, or classify output root. They are never legal at successful
preflight interval end or process exit.

The fixed successful preflight output remains exactly:

```text
F265-D18.preflight.tsv
F265-D18.PREFLIGHT.sha256
```

The ephemeral names enter no manifest, root identity, TSV field,
`preflight_bytes`, payload byte count, fixture byte count, public core,
diagnostic stream, private output, or finite-label input.

## 2. Registered deterministic RATE_IO bytes

`F265-D18.rate_operands.tsv` contains the inherited compact `RATE_IO`
fixture and `IO_BYTES` opcode. For the one logical timed operand, require:

```text
opcode       IO_BYTES
arg0         4000000
arg1         one canonical HEX integer in [0,ff]
arg2..arg15  -
```

Here `arg0` is hexadecimal and equals 67,108,864. Interpret `arg1` as one
unsigned byte. The complete deterministic file is exactly 67,108,864 copies
of that byte. No index, header, newline, checksum, sparse hole, filesystem
zero-fill, compressed representation, formula-generated substitute, or
trailing byte enters the timed file.

The materializer independently computes the SHA-256 of this complete byte
stream and records it for `RATE_IO` as the applicable
`AGGREGATE/STREAM_SHA256` semantic witness. It also records
`AGGREGATE/BYTE_COUNT=67108864`. The independently authored verifier
reconstructs the full logical stream from the authenticated operand row and
requires both values. Preflight computes the production SHA-256 from the
actual final file descriptor and compares it to this authenticated expected
value.

For one successful repetition, the exact `IO_BYTES` production counter is
67,108,864. Each repetition resets its local fixture counter and SHA state.
The expected counter is not multiplied by four: as for every inherited rate
fixture, the expected tuple describes one repetition and each repetition must
match it independently.

## 3. Exact four-repetition lifecycle

Perform exactly four repetitions serially. Timers never overlap. Before the
first timer, parse and authenticate the operand and expected semantic bytes,
reserve any fixed-size production buffer, construct the independent expected
digest state, and reset the first repetition's production counter. These
operations retain the inherited outside-timer meaning.

For repetition `r=0,1,2,3`, perform this exact chronology.

1. Enumerate the retained output-root descriptor. Require empty membership.
   Independently require descriptor-relative no-follow probes of both
   ephemeral names to fail with `ENOENT`. Any other result is fatal.
2. Start the monotonic repetition timer immediately before the exclusive
   create call.
3. Create `.F265-D18.RATE_IO.bin.tmp` with descriptor-relative
   `O_CREAT|O_EXCL|O_NOFOLLOW|O_CLOEXEC`, write-only access, and requested
   mode `0600` under the inherited `umask 077`. Require a regular, one-link
   file owned by the effective UID, on the output root's device, with actual
   permission bits `0600`. Record its device and inode.
4. Write the registered byte exactly 67,108,864 times through the production
   writer. Partial system-call writes are completed in order. Before each
   accepted byte count, require that the next count cannot cross 67,108,864.
   At completion require both the exact file offset and `IO_BYTES` counter to
   equal 67,108,864. A zero-byte or failed write is fatal.
5. Call `fsync` on the temporary descriptor. Require success. Use `fstat` to
   require the recorded identity, regular type, one link, effective-UID
   ownership, `0600` permissions, and exact 67,108,864-byte size. Close the
   descriptor and require close success.
6. Reopen the temporary read-only from the retained output-root descriptor
   with `O_NOFOLLOW|O_CLOEXEC`. Require the same device/inode, type,
   ownership, permissions, link count, and size. Read exactly the complete
   file, reject an early EOF or extra byte, and compute SHA-256. Require the
   authenticated expected digest. Require the identity tuple to remain stable
   across this read, then close successfully. This is the complete temporary
   verification.
7. Re-probe `F265-D18.RATE_IO.bin` and require `ENOENT`. Atomically rename the
   temporary to that final basename with `renameat` inside the same retained
   output descriptor. Require success, then `fsync` the output-root
   descriptor and require success.
8. Require the temporary name absent. Require the final name to be a regular,
   one-link, effective-UID-owned `0600` file with the same device/inode and
   size as the verified temporary. A rename-induced timestamp change is not
   an identity failure; device, inode, type, owner, group, permissions, link
   count, size, and byte hash remain authoritative.
9. Open the final file read-only, descriptor-relative and no-follow. Hash
   exactly its 67,108,864 bytes, reject early EOF or an extra byte, require
   the same authoritative identity fields before and after the read, require
   the authenticated expected SHA-256, and close successfully.
10. Unlink only `F265-D18.RATE_IO.bin` through the retained output-root
    descriptor. Require success. Call `fsync` on the output-root descriptor
    and require success. Enumerate and require empty membership, and require
    both independent no-follow name probes to return `ENOENT`.
11. Stop the monotonic timer after the final absence proofs. Convert the
    elapsed interval to its conservative integer-nanosecond ceiling under
    D15 `SECONDS9` arithmetic. Only now atomically commit this repetition's
    elapsed value, exact counter tuple, and matching digest result in memory.

The registered fixture time is the maximum of the four committed repetition
durations. The exact rate remains

```text
rho_io = maximum_complete_RATE_IO_nanoseconds / 67108864.
```

The temporary verification and final hash are both inside the timer. The
independent expected digest construction is outside it. No other file-system
operation, filename, or timing boundary is legal.

## 4. One-inode and byte-cap accounting

Before `renameat`, only the temporary name refers to the payload inode. After
successful `renameat`, only the final name refers to that same inode. The two
names never refer to two distinct payload inodes, and no copy operation is
permitted. This section replaces only D10's sentence saying that a 64 MiB
target and a 64 MiB temporary can coexist.

The exact transient payload peak is therefore:

```text
1 * 67,108,864 = 67,108,864 bytes.
```

Filesystem metadata is not a second payload. The inherited 67,108,864-byte
preflight-artifact category remains the authoritative category allowance.
The transient file is below the inherited 128 MiB per-file cap. Because both
ephemeral names are absent before ordinary preflight output creation, D18 adds
zero retained bytes and changes no 226,088,448-byte total-output or
309,990,912-byte experiment-directory peak calculation.

The four repetitions are serial and unlink before the next starts. Thus they
never multiply the transient peak by four.

## 5. Failure, cleanup, and non-evidence

Any failure in Steps 1--11 is a fatal preflight failure. It stops all later
fixtures or projection work and permits no preflight PASS TSV or manifest. A
partial repetition never enters the maximum, a rate, `T_pass`, `T_raw`,
`T_projected`, or any released counter or digest.

On an ordinary caught failure after exclusive creation, close every owned
descriptor. Through the retained output-root descriptor, unlink an ephemeral
name only when a no-follow identity check shows that it still names the
payload inode created by this repetition. Attempt temporary first and final
second, then `fsync` the directory and require both names absent. Cleanup
success does not convert the failed repetition into evidence and does not
permit preflight to continue.

If identity-safe cleanup cannot prove both names absent, cleanup itself is
fatal. No success artifact is written. A signal, abnormal exit, common
deadline, or containment kill can prevent in-process cleanup; the separately
authorized future runner must then discard the entire unreleased output root
under its inherited cleanup contract. It must not package or reuse a partial
RATE_IO object.

Local attempted-write and byte-count state can exist in memory for failure
diagnosis, but D18 adds no failure artifact or schema. Only a fully completed
repetition atomically commits its exact `IO_BYTES=67108864` tuple. All four
complete tuples must match the authenticated expected counter before a rate
exists.

## 6. D15 preflight interval and final membership

RATE_IO remains inside D15's preflight interval because it is fixture
execution. All four repetitions, their hashes, counter checks, final unlinks,
directory synchronizations, and absence proofs complete before the remaining
projection and final-input-reauthentication work finishes.

D18 replaces only D15 preregistration's sentence saying that output-root
temporary creation, file writing, flush, close, verification, and rename occur
after the preflight interval. Its D18 replacement is:

> Creation, writing, flush, close, verification, and rename of each retained
> preflight result-file temporary occur after the preflight interval. The two
> preflight-owned RATE_IO ephemeral names instead complete their full timed
> lifecycle during fixture execution inside the interval and are both absent
> before any retained result-file temporary opens. All of these operations
> remain inside the separate whole-process deadline.

This replacement changes no other D15 interval boundary or duration rule.

Immediately before D15 takes the interval end timestamp, enumerate the
preflight output root and require it is empty. Take the timestamp only after
all D15 non-duration fields are ready and all retained inputs have passed
their final checks. Only after that timestamp may the process open or create
`.F265-D18.preflight.tsv.tmp`.

At process success, require the original output-root identity tuple and exact
`BYTEWISE` membership:

```text
F265-D18.PREFLIGHT.sha256
F265-D18.preflight.tsv
```

Both ephemeral names must independently be absent. Their appearance in the
final membership, either manifest, `preflight_bytes`, or any root preimage is
fatal. D15's definition of `preflight_bytes` as the twelve unique immutable
input files survives literally; RATE_IO is a transient output and contributes
zero to that field.

## 7. D18 roots, names, and source tokens

The D18 materializer theory root is the SHA-256 of twenty-three
LF-terminated lines. Lines 1--21 are the D09--D17 predecessor and hostile
audit hashes in the D18 algebra import table's displayed order. Line 22 is
the authenticated D18 algebra line in this file's import table. Line 23 is
the final SHA-256 of this `D18_DRAFT_PREREGISTRATION.md` byte as authenticated
by a future D18 theory audit. Every line is `filename`, one tab, the 64-digit
hash, and LF. The materializer and independently authored verifier pin all
twenty-three names, hashes, and their order. No audit of D18 is inside the
root and no line is self-referential.

All fixture filenames, payload and verification manifests, evaluation files,
replay files, seal files, diagnostic files, private files, and their root
constructions retain their D17 rules with `F265-D18` prefixes. The four source
roles and ten invocation grammars retain their D17 rules with `f265_d18_`
prefixes.

The future public source contains exactly one occurrence of each token:

```text
@F265_D18_FIXTURE_PAYLOAD_ROOT@
@F265_D18_FIXTURE_VERIFICATION_ROOT@
```

The future private source contains one separate occurrence of each same
token. The four-occurrence one-edit replacement, fresh source evidence, and
fresh hostile source-audit requirement survive unchanged. Materializer and
verifier source contain no placeholder.

## 8. Preserved contracts and fresh-audit gate

D18 changes no scientific input, operand stream, expected result stream,
counter vocabulary, public schema, private schema, bank stage, final hit,
historical reservation, digest preimage, replay rule, decision rule,
diagnostic, firewall, resource threshold, or deadline. It adds no CLI option,
final artifact, manifest line, retained byte, worker, process, or writable
root.

No D18 mode is authorized to execute under this draft. A fresh no-context D18
theory audit must authenticate all twenty-two inputs and audit the complete
D09--D18 additive composition. It must try to kill the exclusive name
ownership, deterministic bytes, exact four-repetition chronology, timer
boundary, one-inode proof, temporary and final identity checks, two complete
hashes, directory synchronization, cleanup, partial-evidence exclusion,
D15 interval compatibility, final membership, byte arithmetic, root
construction, mechanical token replacement, and absolute containment gate.

A D18 theory PASS may authorize only drafting the four D18 source roles. It
does not authorize source freezing, a source PASS, compilation, a fixture
byte, fixture verification, preflight, local or remote execution, a result,
packaging, staging, commit, or a ledger edit.

Pending approved hard dynamic containment remains an absolute gate for every
fixture, scientific, audit-process, and production mode. D18 supplies no
runner, launch command, or fallback.
