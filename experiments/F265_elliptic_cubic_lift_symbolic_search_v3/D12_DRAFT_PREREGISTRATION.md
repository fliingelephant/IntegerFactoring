# F265-D12 draft preregistration amendment — closed source and fixture interface

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

Read all eight authenticated bytes in full. Apply only the replacements and
additions below. Every D09--D11 preregistration clause not named here survives
literally. Preserve every predecessor byte. D12 changes interfaces and
artifact chronology only; the complete D09+D10+D11 scientific contract
survives.

## 1. Four source roles and eight process modes

D12 replaces every implicit one-binary interface by four separately compiled
source roles. They share no nonstandard object file or generated source.

| Executable role | Exact mode | Private bytes possible |
|---|---|---|
| `f265_d12_fixture_materialize` | `materialize` | no |
| `f265_d12_fixture_verify` | `verify` | no |
| `f265_d12_public` | `preflight` | no |
| `f265_d12_public` | `evaluate` | no |
| `f265_d12_public` | `replay` | no |
| `f265_d12_public` | `seal-public` | no |
| `f265_d12_public` | `diagnostics` | no |
| `f265_d12_private` | `classify` | yes, only in this mode |

The public executable contains no private TSV schema, private hash, private
path option, factor pair, or private-classification body. The private
executable contains no curve source, peel, F271 decoder, basis constructor,
diagnostic, finite-decision, or fixture-injection body. The materializer and
verifier contain no corpus or private-label parser. Source-level separation is
part of the firewall; operating-system namespace separation remains required.

Every source fixes version text `F265-D12`. Every process sets the C locale,
uses binary file mode, ignores the current working directory for path
resolution, rejects every unknown or repeated option, and rejects positional
arguments. No environment variable can select a file, mode, split, worker
count, seed, cap, or output byte.

## 2. Closed lexical grammar

Each invocation begins with one literal `--mode MODE` pair. Option pairs may
follow in any order, but each required option occurs exactly once. An option
value is one operating-system argument and cannot contain NUL by construction.

`ABS` is an ASCII absolute path of 1 through 1,024 bytes. It starts with one
`/`; has no trailing `/` unless it is `/`; uses only bytes
`A-Z a-z 0-9 / _ - .`; contains no empty, `.` or `..` component; and contains
no repeated `/`. The path `/` is never a legal input or output root. Before
opening a path, the process walks every existing component without following
a symbolic link. Every input file must be a regular file. Every input root
must be a directory. Input and output roots must have distinct device/inode
pairs and neither may be an ancestor of the other.

The walk is descriptor-relative from an opened `/` directory. Every component
is opened with the platform no-follow flag and checked by `fstat`; later files
are opened relative to the retained root descriptor, also no-follow. A path
string is never reopened after validation. The process records device, inode,
size, mode, owner, and SHA-256 before use and checks them again before success.
Any replacement, hard-link alias to a writable output, or metadata change is
fatal. The future source audit must verify the exact platform implementation;
a pre-open `lstat` sequence alone is insufficient.

`SHA256` is exactly 64 lower-case hexadecimal digits. `WORKERS` is one decimal
digit in `1,...,8`. `SPLIT` is exactly `discovery` or `heldout`. Decimal output
integers have no leading zero except zero itself. General hexadecimal integers
are lower-case without a prefix or leading zero except zero itself. A fixed
64-bit mask is exactly 16 lower-case hexadecimal digits. A Boolean is `0` or
`1`. Every TSV file is ASCII, LF-terminated, and contains no CR or NUL.

An output root must already exist, be empty, be owned by the process effective
UID, and have no group or other permission bit. A process sets `umask 077` and
creates only the fixed names assigned to its mode. Every required file is
rendered and capped before append, written to a mode-owned temporary, flushed,
closed, and atomically renamed. The temporary for basename `X` is exactly
`.X.tmp` in the same output root. No other temporary name is legal. A failed
mode leaves no success manifest.

Every file named `*.sha256` uses only lines of the form
`64-lower-hex`, two ASCII spaces, basename, LF. A basename contains no `/`.
Lines occur in the order stated for that mode. A manifest never lists itself.
When it authenticates a read-only input manifest, the line hashes that input
manifest's complete bytes and uses its fixed basename.

## 3. Exact CLI grammars

The displayed line wraps are editorial. These are grammars, not launch
commands and not execution authorization.

```text
f265_d12_fixture_materialize
  --mode materialize
  --output-root ABS
```

No seed, corpus, expected digest, or input path is accepted. The source pins
the D09--D12 theory hashes, every operand, every repetition count, and every
format rule.

```text
f265_d12_fixture_verify
  --mode verify
  --fixture-root ABS
  --output-root ABS
```

The verifier source pins the same theory hashes independently. It does not
accept an expected fixture root on the command line.

```text
f265_d12_public
  --mode preflight
  --fixture-root ABS
  --fixture-verification-root ABS
  --discovery-public ABS
  --heldout-public ABS
  --output-root ABS
  --workers WORKERS
```

```text
f265_d12_public
  --mode evaluate
  --split discovery
  --fixture-root ABS
  --fixture-verification-root ABS
  --public-corpus ABS
  --output-root ABS
  --workers WORKERS
```

```text
f265_d12_public
  --mode evaluate
  --split heldout
  --fixture-root ABS
  --fixture-verification-root ABS
  --public-corpus ABS
  --prior-evaluation-root ABS
  --prior-replay-root ABS
  --output-root ABS
  --workers WORKERS
```

```text
f265_d12_public
  --mode replay
  --split discovery
  --fixture-root ABS
  --fixture-verification-root ABS
  --public-corpus ABS
  --evaluation-root ABS
  --output-root ABS
  --workers WORKERS
```

```text
f265_d12_public
  --mode replay
  --split heldout
  --fixture-root ABS
  --fixture-verification-root ABS
  --public-corpus ABS
  --evaluation-root ABS
  --prior-replay-root ABS
  --output-root ABS
  --workers WORKERS
```

```text
f265_d12_public
  --mode seal-public
  --discovery-public ABS
  --heldout-public ABS
  --discovery-evaluation-root ABS
  --discovery-replay-root ABS
  --heldout-evaluation-root ABS
  --heldout-replay-root ABS
  --output-root ABS
```

```text
f265_d12_public
  --mode diagnostics
  --discovery-public ABS
  --heldout-public ABS
  --discovery-evaluation-root ABS
  --heldout-evaluation-root ABS
  --sealed-root ABS
  --output-root ABS
```

```text
f265_d12_private
  --mode classify
  --discovery-public ABS
  --heldout-public ABS
  --discovery-private ABS
  --heldout-private ABS
  --discovery-evaluation-root ABS
  --heldout-evaluation-root ABS
  --sealed-root ABS
  --diagnostics-root ABS
  --output-root ABS
```

`evaluate` checks that the public header's split equals `SPLIT`. `replay`
checks that both the corpus and evaluation root equal `SPLIT`. No caller may
rename one split into the other. `WORKERS` changes only the at-most-eight
worker schedule fixed by D09; it changes no arithmetic or serialized order.
Discovery forbids both prior-root options. Heldout evaluation requires a PASS
discovery evaluation root and its matching PASS discovery replay root. It
initializes every one-pass packet counter and the F271 reservation ledger from
the discovery evaluation's final cumulative values. Heldout replay requires a
PASS discovery replay root and initializes its independent packet counters and
ledger from that replay's final cumulative values. Thus process separation
does not reset any D10 split-spanning cap. A prior root never changes a
heldout source byte, seed, bank order, fixture, or threshold.

The fixture and fixture-verification roots are pinned by two compile-time
SHA-256 constants in any compilable public source. A pre-materialization
source draft instead contains two syntactically invalid fixed tokens

```text
@F265_D12_FIXTURE_PAYLOAD_ROOT@
@F265_D12_FIXTURE_VERIFICATION_ROOT@
```

in the constant initializers. No command-line value can override them. After
fixture verification, an ordinary `apply_patch` edit replaces each token by
one exact 64-digit root. The resulting source is new evidence and requires a
fresh source audit. The unpatched draft cannot compile.

## 4. Deterministic fixture materialization

This section replaces D11's requirement that all literal expected digests
already exist before an evaluator-source draft. It does not weaken the
requirement before source freeze, source audit, or compilation.

### 4.1 Canonical compact operand encoding

The materializer writes these eight fixed files:

```text
F265-D12.source_operands.tsv
F265-D12.decoder_operands.tsv
F265-D12.rate_operands.tsv
F265-D12.expected_counters.tsv
F265-D12.expected_semantics.tsv
F265-D12.expected_digests.tsv
F265-D12.materializer_attestation.tsv
F265-D12.PAYLOAD.sha256
```

The three operand files have this literal header:

```text
version	fixture	group	item	cycle_count	opcode	arg0	arg1	arg2	arg3	arg4	arg5	arg6	arg7	arg8	arg9	arg10	arg11	arg12	arg13	arg14	arg15
```

`version` is `F265-D12`. Fixture and opcode tokens use only upper-case ASCII,
digits, and underscore. `group`, `item`, and `cycle_count` are canonical
decimal integers, with positive `cycle_count`. Arguments are canonical
lower-case hexadecimal integers, fixed masks, or the literal `-` for an
absent slot. Every row has all 16 argument fields.

Rows are ordered by `(fixture,group,item)`. Groups and items start at zero and
are consecutive. Every row in one group has the same `cycle_count`. The exact
expanded logical stream for a group is: for cycle zero through
`cycle_count-1`, visit its items in increasing order. If a group has `p`
items, that visit's derived `expanded_index` is the total expanded length of
all preceding groups in the fixture plus `cycle*p+item`. Groups concatenate
in increasing order. `expanded_index` supplies every D09--D11
loop or repeat index used in an expected result line; it is not an arithmetic
operand field. Thus repeated operands are represented once without losing
their exact order, index, or multiplicity. Before any timer, preflight expands the
named fixture into reserved memory and independently checks its expanded
operand digest. Compact encoding changes no D11 timed operation or result
stream.

For `operand_sha256`, each expanded logical operand is serialized as one line:

```text
fixture	expanded_index	opcode	arg0	arg1	arg2	arg3	arg4	arg5	arg6	arg7	arg8	arg9	arg10	arg11	arg12	arg13	arg14	arg15
```

The derived index is canonical decimal. All other bytes are copied from the
canonical operand row. The digest covers these LF-terminated lines in expanded
order and no header.

The source operand file contains the complete `SOURCE_CHRONO320`,
`SOURCE_AFFINE_STOP3`, `SOURCE_ROW_STOP2`, RNG, curve-screen, affine, row,
factor-journal, and packet-journal operands. The decoder operand file contains
the support-three, support-64, empty, `S=0`, `S=1`, dense-GF(2), terminal, and
all retained F271 operands. The rate operand file contains every retained D09
rate and all twelve D11 rate streams. Every D11 loop order and denominator is
represented by the displayed expansion rule.

The complete fixture-token vocabulary is:

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

The complete opcode vocabulary and nonabsent argument meanings are:

| Opcode | Arguments in order |
|---|---|
| `RANDOM_BELOW` | `n,low_limb,high_limb,expected_value,expected_iterations` |
| `U_PROPOSAL` | `N,A,x,y` |
| `POWER_PROPOSAL` | `N,s` |
| `AFFINE` | `N,A,B,x1,y1,x2,y2,row1,row2` |
| `ROW_ROOT` | `N,v,curve,row` |
| `PEEL_ROW` | `original_row,w,a` |
| `EVENT` | `phase,class,side,curve,row1,row2,mask_present,mask0,mask1,mask2,mask3,mask4,g,nonce` |
| `DECODER_ROW` | `original_row,N,a,v` |
| `SUPPORT64_PRIME` | `family,index,prime` with `family=0` for `q` and `1` for `r` |
| `SUPPORT64_EXPONENT` | `index,e` |
| `PARITY_MASK` | `ordinal,mask` |
| `SAME_SUPPORT` | `x,y,supplied_d` |
| `TWO_BASE` | `x,y,supplied_g` |
| `LEAF_ASSIGN` | `block,exponent_mask` |
| `EXP_UPDATE` | `u,w,v,delta` |
| `PARITY_CELL` | `coordinate,exponent` |
| `GF2_MASK` | `ordinal,mask` |
| `EXACT_FACTOR` | `row,a` |
| `MOD_FACTOR` | `row,v,N` |
| `ISQRT` | `A` |
| `INVERSE` | `x,N` |
| `SIGNED` | `rho,N` |
| `BASIS_RECORD` | `mask0,mask1,mask2,mask3,mask4,class,ordinal,R_mod_N,X,rho,gcd_minus,gcd_plus,root_class` |
| `GCD` | `x,y` |
| `SAT` | `u,v` |
| `DIV` | `dividend,divisor` |
| `TREE_TOGGLE` | `leaf,old_value,new_value` |
| `RECON` | `accumulator,block,exponent` |
| `TERMINAL_BLOCK` | `ordinal,q` |
| `COMPARE` | `x,y` |
| `IO_BYTES` | `byte_count,fill_byte` |
| `FACTOR_TOKEN` | the 14 `EVENT` arguments |

Class, side, curve, root-class, and absent-row values use the numeric D09
codes. `supplied_d` and `supplied_g` are never absent in these fixtures. Every
argument after the listed sequence is `-`. No unlisted fixture or opcode is
legal. Repetition changes only how often the exact listed production body is
called. Apart from the exact `expanded_index` and repetition rule above, it
never permits a formula or runtime-generated operand to replace an immutable
operand row.

The counter file header is:

```text
version	fixture	counter	value
```

It contains every complete expected counter tuple, including zero counters.
Rows are ordered by `(fixture,counter)` and counter names use the fixture-token
alphabet. The expected-semantics header is:

```text
version	fixture	ordinal	kind	value0	value1	value2	value3	value4	value5	value6	value7
```

It materializes the exact expected status, factor, row, root, basis, kernel,
terminal, and aggregate semantic records required outside each timer. Kinds
use the fixture-token alphabet; values use canonical integers, masks, or `-`.
Rows are ordered by `(fixture,ordinal)`, and ordinals start at zero. This file
contains the complete terminal status streams and every non-digest semantic
witness named by D09--D11. The digest file header is:

```text
version	fixture	operand_sha256	result_fnv1a64	result_sha256	semantic_sha256
```

`result_fnv1a64` is exactly 16 lower-case hexadecimal digits. The two result
digests are over the D11 LF-terminated result bytes. `semantic_sha256` hashes
the complete LF-terminated expected-semantics rows for that fixture; the
whole-file header is not part of a per-fixture hash. Rows are ordered by
fixture name. A row exists exactly for the D10/D11 fixtures whose contract
requires an FNV or SHA trace. Retained D09 fixtures keep their D09 checksum
semantics in `expected_semantics.tsv`; D12 does not invent a new result-record
format for them. No expected value is read from a timed production run.

For the three D11 source timing fixtures, the production result-trace records
are fixed here. Fields are separated by one tab and terminated by LF. Indices
and nonnegative integers use the D11 lower-case hexadecimal encoding. A
negative carry is `-` followed by the canonical positive hexadecimal
magnitude. Status tokens are the exact production status names. An absent
coordinate is `-`.

```text
SOURCE_CHRONO320	PROPOSAL	curve	slot	status	A	B	x	y	d
SOURCE_CHRONO320	AFFINE	curve	call	status	x3	y3	factor
SOURCE_CHRONO320	ROW	curve	scalar	status	factor
SOURCE_CHRONO320	RENDER	original_row	u	v	a	carry
SOURCE_CHRONO320	PEEL	original_row	g	b	b_square	survivor
SOURCE_AFFINE_STOP3	AFFINE	call	status	x3	y3	factor
SOURCE_ROW_STOP2	ROW	call	status	factor
```

`SOURCE_CHRONO320` emits records in production chronology: every reached U
proposal; U base row and then each U affine/row/render sequence; every reached
POWER proposal; POWER base row and then each POWER affine/row/render sequence;
then all peel rows in original-row order. A base row has no affine record.
Proposal `d` is the reached discriminant gcd. A clean accepted proposal has
status `ACCEPT`; the two rejected cases use `REJECT_FULL_DISCRIMINANT` and
`REJECT_B_ZERO`. A unit row has status `UNIT`. An affine success has status
`OK`; the terminal fixtures use `GLOBAL_INFINITY`, `FACTOR_X_SIGN_MINUS`, and
`FACTOR_DENOMINATOR`. A terminal row uses `FACTOR_ROW_ROOT` or
`FULL_ROW_ROOT`. A no-factor field is `1`. The production FNV and SHA states
consume exactly these bytes and no counter or wrapper record. Expected
counters remain the separate complete tuple.

For `RATE_BASIS_RECORD`, the production record is the Section 5 basis schema
with `version=F265-D12`, `split=fixture`, `factor_bits=60`, `shape=random`,
`index=0`, `basis_kind=Q`, and the remaining semantic fields exactly as fixed
by D11. Thus its repeated byte sequence is defined before materialization;
`fixture` is legal only inside this preflight result stream and never in a
public evaluation file.

The materializer-attestation header is:

```text
version	theory_root	logical_operands	result_records	result_bytes	payload_bytes	status
```

There is one data row. `status` is `PASS`. `theory_root` is the SHA-256 of a
canonical LF-terminated list of nine lines. The first eight are the hashes in
the import-table order. The ninth is the final SHA-256 of this
`D12_DRAFT_PREREGISTRATION.md` byte as authenticated by the future D12 theory
audit. Each line is `filename`, one tab, the 64-digit hash, and LF. The source
pins all nine values; no command-line value can rebind one.
`payload_bytes` is the exact sum of the first six data-file widths: the three
operand files, expected counters, expected semantics, and expected digests. It
excludes the attestation and manifest and therefore has no self-reference.
The payload manifest has one line

```text
sha256<two spaces>filename
```

for each of the first seven files, in the displayed order, and no other line.
It never lists itself. The public fixture payload root is the SHA-256 of the
complete `F265-D12.PAYLOAD.sha256` byte.

### 4.2 Exact materializer caps

The materializer is serial. It stops before the next operation if any cap
would be crossed:

```text
MATERIALIZER_LOGICAL_OPERANDS_MAX       8,388,608
MATERIALIZER_RESULT_RECORDS_MAX         4,194,304
MATERIALIZER_RESULT_BYTES_MAX         134,217,728
MATERIALIZER_BIGINT_OPERATIONS_MAX     33,554,432
MATERIALIZER_GF2_WORD_OPERATIONS_MAX    1,048,576
MATERIALIZER_PRIME_CANDIDATES_MAX          65,536
MATERIALIZER_WALL_SECONDS_MAX               1,200
```

The wall cap is an inner monotonic deadline. It is not dynamic containment.
Crossing a cap writes no PASS attestation or payload manifest.

The exact per-file byte caps are:

| File | Cap |
|---|---:|
| source operands | 1,048,576 |
| decoder operands | 4,194,304 |
| rate operands | 4,194,304 |
| expected counters | 1,048,576 |
| expected semantics | 1,048,576 |
| expected digests | 1,048,576 |
| materializer attestation | 65,536 |
| payload manifest | 65,536 |
| **materializer-root total** | **12,713,984** |

These files are part of D09's 67,108,864-byte preflight category. Timed
result streams are hashed incrementally and are not written. The materializer
stores at most one rendered result record and one fixture operand expansion at
a time.

### 4.3 Independent verifier

The verifier is independently authored from the normative D09--D12 bytes. It
shares no source, header containing executable logic, object file, generated
code, SHA-256 implementation, FNV implementation, big-integer wrapper, GF(2)
body, or fixture parser with the materializer or public evaluator. It may use
the same standard C++ library and the same separately linked unmodified
big-integer library.

The verifier authenticates the seven payload hashes and manifest bytes, parses
every canonical row, reconstructs every expanded stream, recomputes all
operand, result, semantic, FNV, and SHA values, and checks every explicit
counter. It independently verifies the Lucas--Lehmer certificate, support-64
prime completeness and maximal exponents, `A64=R64^2`, all curve equations,
terminal statuses, F271 certificates, dense rank and kernel, exact rate result
records, and the D11 projection denominators. It uses no production timer and
does not call a public production body.

The verifier writes exactly:

```text
F265-D12.verifier_attestation.tsv
F265-D12.VERIFIED.sha256
```

The attestation header is:

```text
version	payload_root	theory_root	files	logical_operands	result_records	result_bytes	status
```

There is one `PASS` data row. The verification manifest hashes the attestation
first and the read-only input `F265-D12.PAYLOAD.sha256` second, using the same
two-space manifest grammar. The public verification root is the SHA-256 of
the complete verification-manifest byte. Each verifier output file is capped
at 65,536 bytes, for a 131,072-byte verification root. The complete immutable
fixture addition is therefore at most `12,845,056` bytes, leaving
`54,263,808` bytes in D09's preflight category.
The attestation field `files` is exactly 7, the number of hashes in the input
payload manifest. Its three count fields must equal the materializer
attestation exactly.

A fresh reviewer must compare the materializer and verifier sources and reject
shared executable logic disguised by copying, generated tables, or common
headers. Matching outputs are evidence of two implementations, not a theorem
that either implementation is correct.

## 5. Public evaluation artifact schema

Every `evaluate` process writes exactly these seven files, with the split token
substituted literally in each name:

```text
F265-D12.SPLIT.meta.tsv
F265-D12.SPLIT.banks.tsv
F265-D12.SPLIT.rows.tsv
F265-D12.SPLIT.basis.tsv
F265-D12.SPLIT.event_witnesses.tsv
F265-D12.SPLIT.counters.tsv
F265-D12.SPLIT.CORE.sha256
```

The literal headers are:

```text
version	split	public_sha256	fixture_payload_root	fixture_verification_root	prior_evaluation_root	prior_replay_root	bank_count	row_count	basis_count	event_count	packet_event_sha256	status
```

```text
version	split	factor_bits	shape	index	N	status	K	row_count	survivor_count	kernel_dimension	singleton_count	support_two_count	L_dimension	Q_dimension	quotient_defined	all_Q_images_global	decoder_strict_structural_hit	low_hit	observed_factor	event_count	event_sha256	row_stream_sha256	peel_sha256	basis_sha256	decoder_reservation	decoder_call_count	bank_nonce
```

```text
version	split	factor_bits	shape	index	original_row	curve	scalar	A	B	u	v	a	carry	peel_g	peel_b	peel_b_square	survivor
```

```text
version	split	factor_bits	shape	index	basis_kind	ordinal	mask_0	mask_1	mask_2	mask_3	mask_4	R_mod_N	X	rho	gcd_minus	gcd_plus	root_class
```

```text
version	split	factor_bits	shape	index	witness_slot	bank_event_ordinal	phase	class	side	curve	row_1	row_2	mask_present	mask_0	mask_1	mask_2	mask_3	mask_4	g_hex	bank_nonce
```

```text
version	split	scope	bank_ordinal	counter	value	cap
```

The meta file has one data row. `status` is `PASS`. Both prior-root fields are
`-` for discovery and are the authenticated discovery root identities for
heldout. Bank status is the D09
numeric code. `basis_kind` is `L` or `Q`; ordinal is zero-based inside that
basis. Root class is exactly `GLOBAL_PLUS`, `GLOBAL_MINUS`, `LOW_NON_GLOBAL`,
`STRUCTURAL_Q_NON_GLOBAL`, or `STRUCTURAL_ONLY_LOW_IMAGE`. `witness_slot` is
`OVERALL` or one of the six D09 factor-class names. An absent witness has no
row. Event ordinals are zero-based. Shape uses the public corpus spelling.

Rows are ordered by canonical bank order and then original row. Basis rows are
ordered by bank, `L` before `Q`, then ordinal. Witness rows are ordered by bank,
`OVERALL`, then factor-class numeric code. Counter scope is `PACKET` with bank
ordinal `-`, or `BANK` with a zero-based bank ordinal. Counter rows are ordered
by scope, bank ordinal, then the fixed D09+D10 counter-table order. Every
counter, including zero, is present. The core manifest hashes the first six
files in displayed order and does not hash itself. Its byte SHA-256 is the
evaluation-root identity.

Discovery's packet event count and digest cover discovery. Heldout reconstructs
that authenticated discovery event prefix from its prior evaluation root,
then appends heldout events in canonical order. Its cumulative packet count
and digest therefore cover all 468 banks without requiring a live hash state
to cross a process boundary.

The counter-table order is exactly:

```text
CURVE_PROPOSALS RANDOM_BELOW_CALLS RANDOM_BELOW_ITERATIONS RNG_DRAWS
ADMITTED_ROWS AFFINE_ADDITIONS AFFINE_SAFETY_GCDS DISCRIMINANT_GCDS
ROW_ROOT_GCDS PRODUCT_MULTIPLICATIONS PEEL_EXACT_DIVISIONS
PEEL_BASE_REMAINDERS PEEL_MODULAR_MULTIPLICATIONS PEEL_GCDS
PEEL_RESIDUAL_DIVISIONS PEEL_SQUARE_TESTS F271_SCALAR_GCDS
F271_SATURATION_POWERS F271_REFINEMENT_DIVISIONS F271_RECURSION_NODES
F271_TOUCHES F271_LEAF_ASSIGNMENTS F271_TREE_NODE_UPDATES
F271_EXPONENT_COORD_UPDATES F271_RECONSTRUCTION_INCIDENCES
F271_TERMINAL_BLOCKS F271_REPLACEMENT_COMPARISONS F271_FINAL_COMPARISONS
F271_BLOCK_COMPARISONS F271_PARITY_CELLS F271_GF2_WORD_OPERATIONS
SELECTED_EXACT_PRODUCTS SELECTED_MODULAR_PRODUCTS INTEGER_SQUARE_ROOTS
MODULAR_INVERSIONS SIGNED_RELATION_GCDS BASIS_RECORDS FACTOR_EVENT_LINES
```

`cap` is the applicable D09/D10 bank theorem cap or one-pass packet cap. It is
`-` only for an exact uncapped derived summary. No implementation-specific
counter can be inserted into this table or its digest.

The D09 bank-summary, row, basis, global-summary, per-file, total-output, and
directory-peak caps remain literal. A bank temporary renders every required
row before atomic canonical append. There is no full event stream file; the
bank event digest and first witnesses retain D09's exact semantics.

## 6. Replay, seal, diagnostics, and private schemas

### 6.1 Replay

Replay reads one authenticated evaluation root and writes exactly:

```text
F265-D12.SPLIT.replay.tsv
F265-D12.SPLIT.replay_counters.tsv
F265-D12.SPLIT.REPLAY.sha256
```

The replay header is:

```text
version	split	public_sha256	evaluation_root	prior_replay_root	fixture_payload_root	fixture_verification_root	banks	rows	basis_records	events	all_counters_match	all_digests_match	status
```

The replay-counter header is:

```text
version	split	counter	value	cap
```

There is one `PASS` summary row. Its prior replay field is `-` for discovery
and the authenticated discovery replay identity for heldout. Replay regenerates
all D10 source, terminal, peel,
F271, basis, root, event, and core bytes. Its independent replay ledger starts
at zero for discovery and resumes the authenticated discovery values for
heldout. It
requires byte identity. Counter rows use the complete Section 5 counter-table
order and store cumulative packet values. The replay manifest hashes the
replay TSV, replay counters, and input core-manifest byte in that order. A
heldout replay manifest then hashes the discovery replay manifest as a fourth
line; a discovery replay has no fourth line.

### 6.2 Public seal

`seal-public` accepts only two PASS evaluation roots and their matching PASS
replay roots. It requires the same compile-time fixture payload and verification
roots in all four inputs, reauthenticates both public corpora, and derives the
D10 finite decision from public core bytes only. It writes:

```text
F265-D12.decision.tsv
F265-D12.SEALED.sha256
```

The decision header is:

```text
version	discovery_public_sha256	heldout_public_sha256	discovery_core	discovery_replay	heldout_core	heldout_replay	decision	heldout_events	heldout_eligible	heldout_decoder_strict_hits	hit_factor_bit_cells	all_null_clauses	status
```

There is one `PASS` row. `decision` is one of the four literal D09 finite
labels. The seal manifest hashes the decision TSV, both core manifests, and
both replay manifests in discovery-then-heldout order. Its byte hash is the
sealed-root identity. No diagnostic or private field occurs in either file.

### 6.3 Diagnostics

`diagnostics` requires a PASS sealed root. It writes exactly:

```text
F265-D12.diagnostic_summary.tsv
F265-D12.diagnostic_details.tsv
F265-D12.DIAGNOSTICS.sha256
```

The summary header is:

```text
version	sealed_root	status	completed_tasks	pair_tasks	anchored_tasks	gcd_calls	coordinate_multiplications	predicate_evaluations	chord_remainders	stream_sha256	next_task_key	omitted_details
```

There is one row. `status` is `COMPLETE` or `TIMEOUT`. An absent next task key
is `-`; otherwise it is the ten D09 decimal key fields joined by commas. The
detail header is:

```text
version	task_kind	split	factor_bits_rank	shape	index	basis_ordinal	curve	pair_row_1	pair_row_2	third_row	payload
```

`payload` is the exact D09 pair or anchored-third payload with internal fields
joined by commas. Details retain only the first 16 per bank. The diagnostics
manifest hashes summary, details, and the sealed manifest in that order.
Diagnostics cannot modify the sealed root.

### 6.4 Private classification

Only `f265_d12_private` can parse the D09 private header. It requires both
pinned private hashes, one-to-one public joins, a PASS sealed root, and a
`COMPLETE` or `TIMEOUT` diagnostic root. It writes exactly:

```text
F265-D12.private_classification.tsv
F265-D12.factor_checks.tsv
F265-D12.PRIVATE.sha256
```

The headers are:

```text
version	sealed_root	diagnostics_root	discovery_private_sha256	heldout_private_sha256	joined_rows	checked_events	status
```

```text
version	split	factor_bits	shape	index	event_ordinal	g_hex	matches_private_factor
```

Only public event coordinates and the Boolean match leave the private process.
No `p`, `q`, lambda, rho-label, unmatched private row, or private factor
spelling is written. Rows are in split, bank, event order. The private manifest
hashes classification, checks, the sealed manifest, and the diagnostics
manifest in that order. Any mismatch writes no PASS manifest and releases no
finite label. A PASS releases the already sealed public decision unchanged;
the private process does not select, promote, demote, or rewrite that decision.

## 7. Process ownership and firewall chronology

The future controller must enforce this exact order. A numbered step joins and
exits before the next step starts.

1. Authenticate expected private hashes in a controller-only namespace. Do
   not stage a private pathname, descriptor, ancestor, environment value, or
   byte in any public namespace.
2. After separate user authorization and approved containment, run
   `materialize`; join it.
3. Mount the materializer root read-only in a new namespace, run `verify` with
   a distinct output root; join it. Seal both fixture identities.
4. Patch only the two public-source fixture-root tokens. Obtain a fresh source
   audit before any public compilation.
5. Run `preflight` with public corpus copies only; join it.
6. Run discovery `evaluate`; join it. Mount its root read-only and run
   discovery `replay`; join it.
7. Run heldout `evaluate`; join it. Mount its root read-only and run heldout
   `replay`; join it. Discovery output cannot alter a heldout input or option.
8. Mount all four roots read-only and run `seal-public`; join it. The finite
   decision is now fixed.
9. Run `diagnostics` against read-only public and sealed roots; join it.
10. Verify that every materializer, verifier, public evaluator, replay, seal,
    diagnostic, and writer process has exited. Seal their hashes. Only now
    stage the authenticated private files in a fresh private namespace.
11. Run `classify`. It has read-only public, core, seal, diagnostic, and
    private inputs and one new output root. It has no writable public path,
    shared memory, signal channel, pipe, socket, or return channel to a public
    process. Join it before packaging.

Each role writes only its new output root. No output root is reused. Input
hashes are checked before and after the role. Any mutation, process overlap,
unexpected descriptor, namespace leak, abnormal exit, signal, common-deadline
expiry, containment failure, or packaging failure prevents release.

## 8. Preflight and containment gates

Preflight expands the immutable fixture descriptions before each timer,
checks their operand digests, runs the exact D09--D11 production bodies, and
compares their counters, FNV values, SHA values, and semantic records to the
literal fixture files. It writes only aggregate metrics. Its fixed output is:

```text
F265-D12.preflight.tsv
F265-D12.PREFLIGHT.sha256
```

The preflight header is:

```text
version	fixture_payload_root	fixture_verification_root	fixtures	projected_seconds	preflight_seconds	preflight_bytes	status
```

There is one data row. `status` is `PASS`. All D11 projection terms,
thresholds, double charges, timer boundaries, and failure rules survive.
The TSV is capped at 1,048,576 bytes and the manifest at 65,536 bytes. Both
remain inside the `54,263,808` bytes left in D09's preflight category after
the immutable fixture addition.

No mode in Section 1 is authorized to execute under the present D12 draft.
The pending replacement for unavailable cgroup-v2 containment remains a hard
gate for materialization, verification, preflight, evaluation, replay,
sealing, diagnostics, and private classification. Inner operation, byte, and
wall caps do not replace a hard aggregate memory/process envelope.

An approved later runner must bind the exact executable hash, complete
argument vector, numeric UID isolation, exclusive lock, descendant count,
aggregate address-space bound, core-dump ban, common deadline, kill path,
filesystem namespaces, descriptors, and cleanup. D12 supplies no fallback.

## 9. Source-drafting and audit gates

A fresh no-context reviewer must authenticate all eight D12 inputs and try to
kill:

- preservation of every D09--D11 mathematical and timing clause;
- the four-role source separation, eight modes, and ten closed invocation
  grammars;
- path aliasing, symlink, ancestry, repeated-option, environment, and split
  rebinding attacks;
- compact operand expansion order and equality to every D11 logical stream;
- every fixture counter, digest, byte cap, operation cap, and manifest root;
- independence of future materializer and verifier implementations;
- the deliberately uncompilable two-token evaluator-source boundary;
- all public, replay, seal, diagnostic, and private schemas and orderings;
- public decision sealing before diagnostics and private staging;
- absence of private values from public and released private-audit bytes; and
- the absolute containment and no-execution boundary.

A D12 theory PASS authorizes only drafting the four source roles. It does not
authorize a source freeze, source PASS, compilation, fixture byte, preflight,
execution, result, or ledger edit. Materializer/verification execution needs
separate user approval, approved containment, immutable source bytes, and a
fresh hostile source audit. Public or private source cannot be frozen or
compiled until the verified fixture roots exist and the two source tokens have
been replaced and re-audited.
