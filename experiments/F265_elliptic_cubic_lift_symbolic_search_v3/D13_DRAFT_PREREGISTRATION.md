# F265-D13 draft preregistration amendment — complete source-interface closure

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

Read all ten authenticated bytes in full. Apply only the explicit
replacements and additions below. Every D09--D12 preregistration clause not
explicitly replaced here survives literally. Preserve every predecessor byte.

D13 replaces every future `F265-D12`, `f265_d12_`, `F265-D12.`, and
`F265_D12_` source or artifact token by its D13 counterpart. The four source
roles, eight modes, ten invocation grammars, and every option name and role
restriction in D12 otherwise survive exactly.

## 1. Closed orders, scalar encodings, and root classes

### 1.1 Total orders

`BYTEWISE` compares unsigned ASCII bytes from left to right. If one byte string
is a proper prefix of the other, the shorter string is first. `BYTEWISE` is the
only order for basenames and for tokens without a registered rank. Locale
collation is forbidden.

The exact fixture rank, from zero through 36, is the displayed order:

```text
CURVE_U32 CURVE_POWER32 RBELOW128 FACTOR129
RNG_SEMANTIC SOURCE_BRANCH SOURCE_CHRONO320 SOURCE_AFFINE_STOP3
SOURCE_ROW_STOP2 DECODER_SUPPORT3 DECODER_SUPPORT64 DECODER_EMPTY
DECODER_S0 DECODER_S1 DENSE_GF2 EVENT130 PACKET_EVENT60373
RATE_GCD RATE_SAT RATE_DIV RATE_TREE RATE_RECON RATE_TERMINAL
RATE_COMPARE RATE_IO RATE_NODE RATE_TOUCH RATE_LEAF RATE_EXP
RATE_PARITY RATE_GF2 RATE_EXACT_PRODUCT RATE_MOD_PRODUCT RATE_ISQRT
RATE_INVERSE RATE_SIGNED RATE_BASIS_RECORD
```

Numeric tuple components are compared as mathematical integers. Mask tuples
are compared by word zero through word four as unsigned 64-bit integers.
`PACKET` has scope rank zero and `BANK` has scope rank one. `L` has basis rank
zero and `Q` has basis rank one. Prime family `q` has numeric code and rank
zero; prime family `r` has numeric code and rank one. Split rank is discovery
zero, heldout one, and fixture two where fixture use is expressly allowed.

Every D12 phrase `ordered by (fixture,...)` now means fixture rank followed by
the stated numeric fields. Every phrase `ordered by scope` means scope rank,
then bank ordinal, then the registered counter rank. Basenames in a directory
membership record use `BYTEWISE`. These rules replace any implicit lexical or
locale order in D12.

### 1.2 Scalar encodings

`DEC` is a canonical nonnegative decimal integer. `SDEC` is `DEC` or `-`
followed by a positive `DEC`. `HEX` is a canonical nonnegative lower-case
hexadecimal integer without a prefix. `SHEX` is `HEX` or `-` followed by a
positive `HEX`. Zero is exactly `0`. `MASK` is exactly 16 lower-case
hexadecimal digits. `SHA256` is exactly 64 lower-case hexadecimal digits.
`BOOL` is `0` or `1`. `TOKEN` is a nonempty string using only `A-Z`, `0-9`,
and underscore. The literal absent value is `-` and is legal only where a
schema says `or -`.

Unless a later literal schema states otherwise:

- version, split, shape, basis, status, class-name, and kind fields are exact
  text tokens;
- ordinals, indices, counts, caps, numeric status codes, phases, class codes,
  sides, curves, rows, nonces, and Booleans use `DEC`;
- public corpus `N` uses the authenticated corpus's canonical `DEC` spelling;
- `A,B,u,v,a,g,b,R_mod_N,X,rho`, factors, and unsigned arithmetic witnesses
  use `HEX`;
- carry uses `SHEX`;
- masks use `MASK`; and
- digests and roots use `SHA256`.

### 1.3 Complete root-class map

The numeric operand code and serialized text are bijective:

| Numeric code | Text token | Meaning |
|---:|---|---|
| 0 | `GLOBAL_PLUS` | normalized root equals `1 mod N` |
| 1 | `GLOBAL_MINUS` | normalized root equals `N-1 mod N` |
| 2 | `LOW_NON_GLOBAL` | non-global image of an `L` vector |
| 3 | `STRUCTURAL_Q_NON_GLOBAL` | non-global `Q` image with all `L` images global |
| 4 | `STRUCTURAL_ONLY_LOW_IMAGE` | `Q` image on the branch where an `L` image is non-global |

The `BASIS_RECORD` operand uses the one-digit `HEX` spelling of the numeric
code. Public basis files use the text token. The D11 phrase `non-global
structural` means code 3 and no other code. No other root-class code or token
is legal.

## 2. Exact path-object contract

This section replaces D12 Section 2 lines 64--77 and its undifferentiated
before/after metadata sentence. D12's `ABS` grammar, no-follow component walk,
root nonaliasing, output permissions, fixed temporary names, and manifest line
grammar otherwise survive.

### 2.1 Option-object types

The options `--discovery-public`, `--heldout-public`, `--public-corpus`,
`--discovery-private`, and `--heldout-private` name immutable input files.
Every option whose name ends in `-root`, except `--output-root`, names an
immutable input directory. `--output-root` names the one mutating output
directory. No option changes type by mode.

### 2.2 Immutable input files

Open an input file once with a descriptor-relative no-follow call from its
retained parent descriptor. Require a regular file. Before the first byte is
used, record this exact identity tuple:

```text
device inode size permission_bits uid gid link_count mtime_ns ctime_ns sha256
```

Compute `sha256` over the complete file bytes read from that descriptor. Take
`fstat` immediately before and after the hash and require equality of every
non-hash tuple field. Rewind and use only the same retained descriptor. Before
success, recompute the complete SHA-256 and tuple from that descriptor and
require byte-for-byte equality with the first tuple. A read-only filesystem
namespace is still mandatory; the two hashes are tamper evidence, not a
replacement for namespace immutability.

### 2.3 Immutable input directories

Open an input root once with the descriptor-relative no-follow walk. Require a
directory. Record only

```text
device inode permission_bits uid gid
```

for the directory itself. Do not hash directory bytes and do not compare its
size, link count, or timestamps.

Enumerate the directory through the retained descriptor. Require exactly the
fixed basenames assigned to that root type and no temporary or extra entry.
Sort membership by `BYTEWISE`. For each member, record basename, file type,
device, and inode; then open the required regular file no-follow and apply
Section 2.2. Immediately before process success, repeat the enumeration and
require the identical ordered membership records and identical root identity
tuple. No pathname is reopened.

### 2.4 Mutating output directory

Open the already existing output root once with the descriptor-relative
no-follow walk. Require a directory, effective-UID ownership, no group or other
permission bit, and empty membership. Record device, inode, permission bits,
uid, and gid. Its size, link count, and timestamps are expected to change and
are never compared.

Create a temporary only with descriptor-relative exclusive creation,
no-follow, mode `0600`, and the fixed `.X.tmp` basename. Require a regular
one-link file owned by the effective UID. Flush and close it, verify its
complete bytes and cap, and rename it within the retained output descriptor to
the absent final basename. Before success, require the original output-root
identity tuple, exactly the mode-owned final basenames in `BYTEWISE` order, no
temporary, and no extra entry. Compare every created file's device/inode pair
against every retained input-file pair. Any equality, input link-count change,
or input/output root ancestry is fatal.

## 3. Closed fixture files

This section replaces D12's open expected-counter and expected-semantics
contracts. D12's three operand files, opcode argument layouts, expansion rule,
operand digest, expected-digest schema, materializer attestation, payload
manifest, operation caps, and byte caps survive with D13 prefixes.

### 3.1 Exhaustive fixture counters

The complete fixture-counter vocabulary and rank are the displayed order:

```text
CURVE_PROPOSALS RANDOM_BELOW_CALLS RANDOM_BELOW_ITERATIONS RNG_DRAWS
ADMITTED_ROWS AFFINE_ADDITIONS AFFINE_SAFETY_GCDS DISCRIMINANT_GCDS
ROW_ROOT_GCDS ROW_RECORDS PRODUCT_MULTIPLICATIONS PEEL_EXACT_DIVISIONS
PEEL_BASE_REMAINDERS PEEL_MODULAR_MULTIPLICATIONS PEEL_GCDS
PEEL_RESIDUAL_DIVISIONS PEEL_SQUARE_TESTS F271_SCALAR_GCDS
F271_SATURATION_POWERS F271_REFINEMENT_DIVISIONS F271_RECURSION_NODES
F271_TOUCHES F271_LEAF_ASSIGNMENTS F271_TREE_NODE_UPDATES
F271_EXPONENT_COORD_UPDATES F271_RECONSTRUCTION_INCIDENCES
F271_TERMINAL_BLOCKS F271_REPLACEMENT_COMPARISONS
F271_FINAL_COMPARISONS F271_BLOCK_COMPARISONS F271_PARITY_CELLS
F271_GF2_WORD_OPERATIONS SELECTED_EXACT_PRODUCTS
SELECTED_MODULAR_PRODUCTS INTEGER_SQUARE_ROOTS MODULAR_INVERSIONS
SIGNED_RELATION_GCDS BASIS_RECORDS FACTOR_EVENT_LINES IO_BYTES
```

`F265-D13.expected_counters.tsv` retains the D12 header. It contains exactly
40 counter rows for each of the 37 fixtures: all counters above, including
zeros. Rows use fixture rank then counter rank. `value` is `DEC`. No alias,
fixture-local counter name, implementation counter, or additional row is
legal. Returned-block counts, emitted-mask counts, checksums, sums, XORs, and
semantic assertion counts are semantic aggregates, not production counters.

### 3.2 Exhaustive semantic kinds

`F265-D13.expected_semantics.tsv` retains this header:

```text
version	fixture	ordinal	kind	value0	value1	value2	value3	value4	value5	value6	value7
```

The complete kind rank and field schemas are:

| Kind | `value0` through `value7` |
|---|---|
| `STATUS` | subject `TOKEN`, subject ordinal `DEC`, status `TOKEN`, result zero `HEX or -`, result one `HEX or -`, factor `HEX or -`, auxiliary `DEC or -`, `-` |
| `RANDOM_RESULT` | call `DEC`, `n` `HEX`, value `HEX or -`, iterations `DEC`, draws `DEC`, status `TOKEN`, `-`, `-` |
| `AFFINE_RESULT` | call `DEC`, status `TOKEN`, `x3` `HEX or -`, `y3` `HEX or -`, factor `HEX or -`, safety-gcd count `DEC`, row one `DEC`, row two `DEC` |
| `ROW_ROOT_RESULT` | call `DEC`, status `TOKEN`, factor `HEX or -`, curve `DEC`, row `DEC`, gcd count `DEC`, `-`, `-` |
| `PEEL_RESULT` | original row `DEC`, `g` `HEX`, `b` `HEX`, square `BOOL`, survivor `BOOL`, `-`, `-`, `-` |
| `FACTOR_RESULT` | event ordinal `DEC`, phase `DEC`, class `DEC`, side `DEC`, `g` `HEX`, curve `DEC`, row one `DEC`, row two `DEC` |
| `DECODER_SUMMARY` | rows `DEC`, blocks `DEC`, rank `DEC`, kernel dimension `DEC`, `L` dimension `DEC`, `Q` dimension `DEC`, quotient-defined `BOOL`, status `TOKEN` |
| `KERNEL_VECTOR` | ordinal `DEC`, mask zero through mask four `MASK`, source `TOKEN`, `-` |
| `BASIS_VECTOR` | basis `L or Q`, ordinal `DEC`, mask zero through mask four `MASK`, class code `DEC` |
| `BASIS_ROOT` | basis `L or Q`, ordinal `DEC`, `R_mod_N` `HEX`, `X` `HEX`, `rho` `HEX`, minus gcd `HEX`, plus gcd `HEX`, root-class text `TOKEN` |
| `PRIME` | family code `DEC`, index `DEC`, prime `HEX`, primality `BOOL`, preceding-gap completeness `BOOL`, `-`, `-`, `-` |
| `EXPONENT` | index `DEC`, exponent `DEC`, row bits `DEC`, maximal `BOOL`, row `HEX`, `-`, `-`, `-` |
| `GF2_SUMMARY` | input masks `DEC`, unpadded word operations `DEC`, padded word operations `DEC`, rank `DEC`, kernel dimension `DEC`, generator `MASK`, scratch `HEX`, status `TOKEN` |
| `AGGREGATE` | metric `TOKEN`, typed value, `-`, `-`, `-`, `-`, `-`, `-` |
| `CERTIFICATE` | certificate `TOKEN`, result `BOOL`, witness zero `HEX or -`, witness one `HEX or -`, `-`, `-`, `-`, `-` |

The complete `STATUS` subject vocabulary is:

```text
FIXTURE SAMPLER U_PROPOSAL POWER_PROPOSAL AFFINE ROW_ROOT PEEL
DECODER EVENT_JOURNAL PACKET_JOURNAL TERMINAL GF2 TREE WRITER
```

The complete `KERNEL_VECTOR` source vocabulary is `FULL`, `L`, `Q`, and
`GF2`. A `BASIS_VECTOR` with basis `L` uses D09 class code 4. A
`BASIS_VECTOR` with basis `Q` uses D09 class code 5. A `PRIME` family code is
zero for `q` and one for `r`.

The complete status-token vocabulary is:

```text
PASS ACCEPT REJECT_FULL_DISCRIMINANT REJECT_B_ZERO REJECT_DUPLICATE
FACTOR_CURVE_DISCRIMINANT RESOURCE_REJECT_RANDOM_BELOW_CAP
RESOURCE_REJECT_CURVE_ATTEMPTS GLOBAL_INFINITY FACTOR_X_SIGN_MINUS
FACTOR_X_SIGN_PLUS FACTOR_DENOMINATOR UNRESOLVED_EQUAL_X
UNRESOLVED_DENOMINATOR OK UNIT FACTOR_ROW_ROOT FULL_ROW_ROOT
EMPTY_KERNEL ZERO_KERNEL INVARIANT_EVENT_CAP INVARIANT_PACKET_EVENT_CAP
```

The complete `AGGREGATE` metric vocabulary and value type are:

| Metric | Type |
|---|---|
| `CALLS` | `DEC` |
| `RESULT_RECORDS` | `DEC` |
| `RESULT_BYTES` | `DEC` |
| `OUTPUT_SUM` | `DEC` |
| `OUTPUT_XOR` | `HEX` |
| `ONE_BITS` | `DEC` |
| `EMITTED_MASKS` | `DEC` |
| `RETURNED_BLOCKS` | `DEC` |
| `FINAL_VALUE` | `HEX` |
| `FINAL_MASK` | `MASK` |
| `RANK` | `DEC` |
| `KERNEL_DIMENSION` | `DEC` |
| `ROW_COUNT` | `DEC` |
| `SURVIVOR_COUNT` | `DEC` |
| `PRIME_COUNT` | `DEC` |
| `MAX_BITS` | `DEC` |
| `BYTE_COUNT` | `DEC` |
| `CHECKSUM64` | exactly 16 lower-case hexadecimal digits |
| `STREAM_SHA256` | `SHA256` |
| `OPERAND_SHA256` | `SHA256` |

The complete certificate vocabulary is:

```text
MIX64_ZERO LUCAS_LEHMER SUPPORT64_PRIMES_COMPLETE
SUPPORT64_EXPONENTS_MAXIMAL A64_EQUALS_R64_SQUARED CURVE_EQUATIONS
ROOT_CONGRUENCES PEEL_EXACTNESS TERMINAL_COPRIMALITY DENSE_KERNEL
EVENT_DIGEST_UNCHANGED PACKET_DIGEST_UNCHANGED TRACE_MATCH
```

No other subject, status, metric, certificate, kind, or field spelling is
legal. Every fixture has exactly one `STATUS/FIXTURE/0/PASS` row. It then has
all and only the applicable non-digest semantic witnesses required by the
authenticated D09--D11 fixture, expressed by the most specific kind above.
The complete profile is fixed as follows:

| Fixtures | Required kinds in addition to fixture PASS |
|---|---|
| `CURVE_U32`, `CURVE_POWER32` | `STATUS`, `RANDOM_RESULT`, `FACTOR_RESULT`, `AGGREGATE` |
| `RBELOW128`, `RNG_SEMANTIC` | `STATUS`, `RANDOM_RESULT`, `AGGREGATE`, `CERTIFICATE` |
| `FACTOR129`, `EVENT130` | `STATUS`, `FACTOR_RESULT`, `AGGREGATE`, `CERTIFICATE` |
| `PACKET_EVENT60373` | `STATUS`, `AGGREGATE`, `CERTIFICATE`; its complete compact event operands and unchanged digest carry the accepted prefix |
| `SOURCE_BRANCH`, `SOURCE_AFFINE_STOP3`, `SOURCE_ROW_STOP2` | `STATUS`, `AFFINE_RESULT`, `ROW_ROOT_RESULT`, `FACTOR_RESULT`, `AGGREGATE` as applicable |
| `SOURCE_CHRONO320` | `STATUS`, `AGGREGATE`, `CERTIFICATE`; its complete operation results are the D12 result trace |
| `DECODER_SUPPORT3`, `DECODER_SUPPORT64`, `DECODER_EMPTY`, `DECODER_S0`, `DECODER_S1` | `STATUS`, `PEEL_RESULT`, `DECODER_SUMMARY`, `KERNEL_VECTOR`, `BASIS_VECTOR`, `BASIS_ROOT`, `PRIME`, `EXPONENT`, `CERTIFICATE` as applicable |
| `DENSE_GF2` | `STATUS`, `GF2_SUMMARY`, `KERNEL_VECTOR`, `CERTIFICATE` |
| every `RATE_*` fixture | `STATUS`, `AGGREGATE`, `CERTIFICATE` as applicable; detailed result bytes remain in the registered result digest |

Within one fixture, rows use kind rank from the schema table. The within-kind
key is: subject rank then subject ordinal for `STATUS`; call for random,
affine, and row-root results; original row for peel; event ordinal for factor;
zero for the single decoder and GF(2) summaries; ordinal for kernel vectors;
basis rank then ordinal for basis rows; family rank then index for primes;
index for exponents; metric-table rank for aggregates; and certificate-list
rank for certificates. `ordinal` is the zero-based position in this complete
order and must equal the row position. Duplicate keys are forbidden.

### 3.3 D13 theory and fixture roots

The D13 materializer theory root is the SHA-256 of eleven LF-terminated lines.
The first ten lines are the import table above in displayed order. The eleventh
line is the final SHA-256 of this D13 preregistration as authenticated by the
future D13 theory audit. Each line remains `filename`, tab, hash, LF. The
materializer and independently authored verifier pin all eleven values.

All D12 fixture filenames and manifest rules survive with `F265-D13` prefixes.
The payload manifest still hashes the three operand files, expected counters,
expected semantics, expected digests, and materializer attestation in that
order. The verification manifest still hashes the verifier attestation and
the read-only payload manifest in that order. Their byte hashes remain the
payload and verification root identities.

## 4. Complete public event evidence

This section replaces D12's witness-only reconstruction rule. It also replaces
D09's statement that the complete factor-event stream is not an output
category. The D09 event law, 15-field raw event bytes, sticky semantics,
129-event bank bound, and 60,372-event packet bound survive exactly.

### 4.1 Evaluation files and schema

Each evaluation writes these eight files:

```text
F265-D13.SPLIT.meta.tsv
F265-D13.SPLIT.banks.tsv
F265-D13.SPLIT.rows.tsv
F265-D13.SPLIT.basis.tsv
F265-D13.SPLIT.events.tsv
F265-D13.SPLIT.event_witnesses.tsv
F265-D13.SPLIT.counters.tsv
F265-D13.SPLIT.CORE.sha256
```

The event header is:

```text
version	split	factor_bits	shape	index	bank_event_ordinal	phase	class	side	curve	row_1	row_2	mask_present	mask_0	mask_1	mask_2	mask_3	mask_4	g_hex	bank_nonce
```

The file contains every sticky event originating in that split, including all
events from a bank later marked `RESOURCE_REJECT`. Rows use canonical bank
order then numeric bank-event ordinal. The 15-field suffix beginning with
`bank_event_ordinal` is byte-identical to the D09 event line before its LF.
The file wrapper never enters the scientific packet-event digest.

The split core manifest hashes the first seven files in displayed order. Its
byte SHA-256 is the evaluation-root identity. The witness file remains a
redundant bounded index of the first overall and first per-class events. Every
witness row must equal its referenced complete event row byte-for-byte in the
shared event fields.

### 4.2 Sticky commit and cumulative reconstruction

The bank temporary renders all complete event-file rows before any global
append. At bank finalization, its event rows and bank summary append in
canonical order even if a later counted-arena, record-rendering, or non-event
core-writer cap selected `RESOURCE_REJECT`. Failure to preserve, render, or
append a schema-valid event is a split-fatal invariant failure, not a
recoverable resource result. A failed split writes no core manifest.

Discovery's packet digest hashes the exact D09 15-field suffix plus LF for
every discovery event row. Heldout authenticates the discovery core, parses
every discovery event row, reconstructs and hashes those suffix bytes, checks
the discovery count and digest, and only then appends heldout suffix bytes.
Thus the heldout cumulative digest covers all 468 banks. It never treats a
final SHA-256 digest as a continuation state.

Discovery replay performs the same reconstruction from its evaluation root.
Heldout replay first reconstructs the discovery prefix from the authenticated
discovery evaluation root named transitively by its heldout evaluation and
matching prior replay, checks the prior replay count and digest, and appends
the regenerated heldout events. Evaluation and replay event bytes, counts,
bank digests, split digests, and cumulative digests must all match.

D13 replaces the D12 heldout replay grammar by this exact grammar so the
transitively named discovery root also has an authenticated input path:

```text
f265_d13_public
  --mode replay
  --split heldout
  --fixture-root ABS
  --fixture-verification-root ABS
  --public-corpus ABS
  --evaluation-root ABS
  --prior-evaluation-root ABS
  --prior-replay-root ABS
  --output-root ABS
  --workers WORKERS
```

Discovery replay forbids both prior-root options. Heldout replay requires the
prior evaluation root to be the discovery root named by the heldout evaluation
meta row and authenticated by the discovery replay manifest. No other D12 CLI
grammar or option changes.

The private classifier reads both authenticated event files. It writes exactly
one factor-check row for every event, in split rank, bank order, event-ordinal
order. `checked_events` equals the sum of the two event-file data-row counts.
It requires every `g_hex` to equal the joined private `p` or `q`. It performs no
curve, peel, decoder, basis-construction, or fixture-injection operation.

### 4.3 Event byte caps and revised totals

One D13 event-file row is capped at 256 bytes including LF.

The inherited D09 raw event cap is 192 bytes including LF. The D13 wrapper adds
at most 8 version bytes, 7 split bytes, 2 factor-bit bytes, 9 shape bytes, 2
index bytes, and 5 tabs, for at most 225 bytes. The literal header is 157
bytes. Thus the 256-byte line cap has explicit slack.

Each split event file is capped at

```text
(60,372 data rows + 1 header) * 256 = 15,455,488 bytes.
```

Because the packet cap spans both splits, the two headers and all data rows
together are capped at

```text
(60,372 data rows + 2 headers) * 256 = 15,455,744 bytes.
```

This complete event category replaces D09's zero-byte event-output category.
The total output cap becomes

```text
210,632,704 + 15,455,744 = 226,088,448 bytes.
```

Accordingly, D13 replaces only the I/O term in D10/D11 `T_pass`:

```text
210,632,704*rho_io  ->  226,088,448*rho_io.
```

Every other source, decoder, event, replay, diagnostic, multiplier, threshold,
and reserve term survives literally.

The one-bank temporary replaces `129*192` raw event bytes by `129*256`
wrapped event rows:

```text
16,384 + 320*512 + 64*512 + 16*1,024 + 129*256
= 262,400 bytes.
```

The directory-peak cap becomes

```text
226,088,448 + 64*262,400 + 67,108,864
= 309,990,912 bytes.
```

The 128 MiB per-file cap, 128 MiB worker arena, 256 MiB scheduler/writer
allowance, 1.25 GiB static allowance, and 3.5 GiB measured RSS cap survive.

## 5. Explicit bank and row replacement

This section explicitly replaces D09 preregistration lines 685--689 and D12's
bank and row headers. A scalar row never repeats `N,A,B`. The bank row stores
`N` once and the accepted coefficients for each curve once.

The D13 bank header is:

```text
version	split	factor_bits	shape	index	N	A_0	B_0	A_1	B_1	status	K	row_count	survivor_count	kernel_dimension	singleton_count	support_two_count	L_dimension	Q_dimension	quotient_defined	all_Q_images_global	decoder_strict_structural_hit	low_hit	observed_factor	event_count	event_sha256	row_stream_sha256	peel_sha256	basis_sha256	decoder_reservation	decoder_call_count	bank_nonce
```

An unaccepted or unreached curve has `-` in both coefficient fields. An
accepted curve has canonical `HEX` coefficients. No one-of-two absence is
legal.

The D13 row header is:

```text
version	split	factor_bits	shape	index	original_row	curve	scalar	u	v	a	carry	peel_g	peel_b	peel_b_square	survivor
```

For the maximum data row, `version` has 8 bytes, `heldout` 7, factor bits 2,
`safe-safe` 9, index 2, original row 3, curve 1, scalar 3, `u,v` 30 each,
`a,peel_g,peel_b` 91 each, carry at most 62 including a sign, two Booleans 1
each, and the 15 tabs plus LF use 16. Therefore

```text
8+7+2+9+2+3+1+3+2*30+3*91+62+2+16 = 448 bytes.
```

The literal 512-byte row cap has 64 bytes of slack. The D09 bank-summary cap
remains 16,384 bytes. The two-byte index bound is the maximum authenticated
spelling among the retained rows of both pinned public corpus files. Replay
regenerates both coefficients and requires exact agreement with the bank row
before using any scalar row.

All other D12 public schemas survive with D13 prefixes. Public counter rows use
`PACKET` before `BANK`, then numeric bank ordinal and D12 Section 5's exact
38-counter table rank. The 40-counter rank in Section 3.1 applies only to the
fixture counter file. The core manifest order is the order in Section 4.1.

## 6. Exact preflight manifest

Preflight writes exactly:

```text
F265-D13.preflight.tsv
F265-D13.PREFLIGHT.sha256
```

The TSV header and data row remain D12's schema with version `F265-D13`. The
manifest has exactly one record and no other byte. Its record grammar is:

```text
<SHA256><two ASCII spaces>F265-D13.preflight.tsv<LF>
```

`SHA256` is the lower-case SHA-256 of the complete TSV bytes. The
manifest never hashes a fixture, corpus, or itself. Its complete-byte hash is
the preflight-root identity. D12's 1,048,576-byte TSV cap and 65,536-byte
manifest cap survive.

## 7. Public and private fixture-root tokens

The public source contains exactly one occurrence of each token in constant
initializers:

```text
@F265_D13_FIXTURE_PAYLOAD_ROOT@
@F265_D13_FIXTURE_VERIFICATION_ROOT@
```

The private source contains exactly one separate occurrence of each same token
in constant initializers. Thus the two source files contain exactly four token
occurrences. Both drafts are syntactically invalid and cannot compile.

After materialization and independent verification, one ordinary reviewed
`apply_patch` edit replaces all four occurrences by the same two 64-digit
roots. The public source validates both roots in every mode. The private source
requires the sealed and diagnostic roots to transitively name the same two
compile-time roots before it reads a private data row. No command-line option,
environment value, manifest field, or private byte can override a compile-time
root.

The patch creates new public and private source evidence. Both files require a
fresh hostile source PASS. Neither can be frozen or compiled before that PASS.
The materializer and verifier sources contain no root placeholder because they
produce and independently verify the roots.

## 8. Repaired process chronology

D12's process-role firewall and eleven-step chronology survive with these
exact replacements:

1. D13 artifact and executable prefixes replace D12 prefixes.
2. The fixture materializer theory root uses the eleven-line D13 rule.
3. After fixture verification, patch all four public/private token occurrences
   in the one reviewed edit from Section 7. Audit both resulting sources.
4. Evaluation roots contain the complete split event file. Every later public
   and private process mounts those roots read-only and authenticates that file
   through the core manifest.
5. The private classifier is staged only after every fixture, evaluator,
   replay, seal, diagnostic, writer, and controller-owned public child has
   exited and the public decision is sealed. It has no writable public path,
   shared memory, signal channel, pipe, socket, or return channel to a public
   process.

Every input directory uses the stable-membership contract in Section 2. Every
output directory uses the mutating-output contract. No output root is reused.

## 9. Containment and authorization gates

No D13 mode is authorized to execute under this draft. Pending replacement of
the unavailable cgroup-v2 workflow remains a hard gate for fixture
materialization, fixture verification, preflight, evaluation, replay, public
sealing, diagnostics, and private classification. Inner operation, byte,
timer, file, and directory caps do not replace a hard aggregate memory/process
envelope.

An approved later runner must bind the exact executable hashes, complete
argument vectors, numeric UID isolation, exclusive lock, descendant count,
aggregate address-space bound, core-dump ban, common deadline, kill path,
filesystem namespaces, retained descriptors, mount permissions, and cleanup.
D13 supplies no runner or fallback.

A fresh no-context D13 reviewer must authenticate all ten inputs and try to
kill the D09--D13 additive composition, root-class map, exhaustive fixture
schemas, complete sticky event stream, split-spanning digest reconstruction,
private every-event checks, three path-object contracts, preflight manifest,
four root-token occurrences, bank/row replacement and width arithmetic, every
registered total order, revised byte/peak caps, role firewall, and absolute
containment boundary.

A D13 theory PASS authorizes only drafting the four source roles. It does not
authorize source freezing, a source PASS, compilation, a fixture byte,
preflight, local or remote execution, a result, packaging, or a ledger edit.
Materializer or verifier execution needs separate user approval, approved
containment, immutable source bytes, and a fresh hostile source audit. Public
and private source cannot be frozen or compiled until the verified roots have
replaced all four tokens and the patched bytes have passed a fresh audit.
