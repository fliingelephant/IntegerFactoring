# F265-D18 draft algebra amendment — closed transient RATE_IO ownership

## Status and exact construction

This is an unfrozen theory-only additive draft. It creates no source, fixture
byte, runner, manifest, freeze, compilation, preflight, execution, result, or
ledger entry. It authorizes none of those actions by itself.

D18 has exactly these authenticated predecessor bytes:

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

Read all twenty-one authenticated bytes in full. Apply only the replacements
and additions in this file and in `D18_DRAFT_PREREGISTRATION.md`. Every
D09--D17 clause not explicitly replaced by D18 survives literally. Preserve
every predecessor byte.

The D11, D14, and D17 hostile PASS artifacts remain evidence only for their
exact authenticated compositions. The D17 PASS does not transfer to D18.

## 1. Exact repair scope

The inherited `RATE_IO` fixture must time four repetitions of a
67,108,864-byte writer path. D10 required a temporary, atomic rename, final
hash, and unlink, but it did not assign those transient objects a legal
preflight-owned basename. D12 allowed a mode to create only its assigned
names, while D15 required every fixture to finish before the preflight TSV
temporary opens. Those clauses left no legal object for the timed payload.

D18 repairs only that ownership defect. In `preflight` mode, the retained
output-root descriptor owns these two ephemeral names during `RATE_IO`:

```text
F265-D18.RATE_IO.bin
.F265-D18.RATE_IO.bin.tmp
```

They are not preflight result files, root members, manifest members, fixture
payloads, fixture-verification outputs, corpus inputs, or finite-label
evidence. They exist only inside one complete timed repetition. The separate
preregistration defines their exact descriptor-relative lifecycle.

No input or output option is added. No current-working-directory,
environment, unnamed path, alternate writable root, in-memory substitute, or
implementation-selected basename is permitted.

D18 also narrowly replaces D15 preregistration's sentence saying that
output-root temporary creation, writing, flush, close, verification, and
rename occur after the preflight interval. In D18, that sentence applies to
the retained preflight result files and their ordinary temporaries. It does
not apply to the two RATE_IO ephemeral names above: their complete lifecycle
is fixture execution inside the D15 interval, and both names are absent before
the retained preflight TSV temporary opens. No other D15 timing sentence
changes.

## 2. One-inode transient meaning

One repetition begins with both ephemeral names absent. It exclusively
creates the temporary, writes exactly 67,108,864 registered deterministic
bytes, flushes, closes, and verifies that one file. It then atomically renames
the temporary to the absent final basename. Rename changes the name of the
same inode; it does not create a second payload. The repetition authenticates
the complete final bytes, unlinks the final name, synchronizes the directory,
and proves both names absent before it commits its elapsed time.

Therefore the temporary and final payload are never two distinct full files.
D18 expressly supersedes D10's ambiguous sentence that a 64 MiB target and a
64 MiB temporary can coexist. The registered transient disk peak is exactly
one 67,108,864-byte payload plus filesystem metadata, not two payloads. The
inherited 67,108,864-byte preflight category remains unchanged.

Exactly four complete repetitions are required. A partial write, failed
flush, failed close, identity mismatch, rename failure, digest mismatch,
unlink failure, directory-sync failure, unexpected name, or incomplete
cleanup is a fatal preflight failure. It contributes no timing sample, rate,
projection term, PASS row, or success manifest.

After all four repetitions, the output root is empty again. Only then can the
later D15 preflight-output boundary open
`.F265-D18.preflight.tsv.tmp`. At successful process exit, the output root
contains exactly `F265-D18.preflight.tsv` and
`F265-D18.PREFLIGHT.sha256`; both RATE_IO names are absent and illegal in the
final membership.

## 3. Preserved mathematics, evidence, and caps

D18 changes no source law, random stream, factor-first chronology, affine
operation, prospective-row test, simultaneous peel, F271 V2 operation,
kernel, low basis, structural complement, normalized root, root class,
fixture operand, result trace, operation counter, rate denominator,
projection formula, duration encoding, finite label, diagnostic, replay,
private firewall, theorem boundary, or scope claim.

The `RATE_IO` timed body still writes, renames, hashes, and removes exactly
67,108,864 bytes in each of four repetitions. Its registered rate is still
the maximum complete elapsed time divided by 67,108,864. The 128 MiB per-file
cap, 67,108,864-byte preflight category, 226,088,448-byte total-output cap,
309,990,912-byte directory-peak cap, memory limits, operation limits,
projection gate, preflight deadline, finalization reserve, and whole-process
deadline remain unchanged.

## 4. Mechanical D18 composition

D18 replaces every future source-version token `F265-D17`, executable prefix
`f265_d17_`, artifact prefix `F265-D17.`, and fixture-root placeholder prefix
`F265_D17_` by the corresponding D18 token. This replacement applies only to
future artifacts and source. It does not rename or modify a predecessor file.
The version text `F265-D18` remains eight bytes.

The D18 materializer theory root includes the twenty-one predecessor hashes
above, the final hash of this D18 algebra amendment, and the final hash of the
D18 preregistration amendment. The D18 preregistration fixes the exact
twenty-three-line order. No other root construction changes.

## 5. Authorization boundary

A fresh no-context D18 theory PASS may authorize only source drafting for the
four D18 roles. It does not authorize source freezing, a source PASS,
compilation, fixture materialization, fixture verification, preflight,
evaluation, replay, sealing, diagnostics, private classification, packaging,
result release, remote execution, or a ledger edit.

Pending approved hard dynamic containment remains an absolute gate for every
fixture, scientific, audit-process, and production mode. D18 contains no
source, fixture byte, runner, launch command, containment fallback, or
execution authorization.
