# F265-D15 draft preregistration amendment — closed digest and duration bytes

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

Read all fifteen authenticated bytes in full. Apply only the replacements
and additions below. Every D09--D14 clause not explicitly replaced here
survives literally. Preserve every predecessor byte.

D15 replaces every future source-version token `F265-D14`, executable prefix
`f265_d14_`, artifact prefix `F265-D14.`, and fixture-root placeholder prefix
`F265_D14_` by the corresponding D15 token. The four source roles, eight
modes, ten invocation grammars, option names, schemas, caps, and role
restrictions otherwise survive exactly.

## 1. Exact bank-local digest preimages

This section defines the previously unstated preimages of the three bank-local
digests in the D13 bank schema. Every preimage byte is ASCII. Fields are
separated by one tab and every record is terminated by one LF. The scalar
encodings and token spellings are exactly D13's. No CR, NUL, header, wrapper,
version, split, factor-bit value, shape, or bank key enters any of these three
preimages.

The SHA-256 of a zero-line stream is the SHA-256 of the empty byte string:

```text
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

### 1.1 Source-row stream

For every admitted source row, append exactly this suffix line:

```text
original_row<TAB>curve<TAB>scalar<TAB>u<TAB>v<TAB>a<TAB>carry<LF>
```

`original_row`, `curve`, and `scalar` are `DEC`; `u`, `v`, and `a` are
`HEX`; and `carry` is `SHEX`. Lines use production row order: every admitted
`U` row in increasing scalar order, followed by every admitted `POWER` row in
increasing scalar order. Equal integer rows remain distinct lines. A row
admitted before a later source stop remains in this stream. The SHA-256 of the
complete stream is `row_stream_sha256`. If no row was admitted, the stream is
empty.

### 1.2 Simultaneous-peel stream

Only after the complete simultaneous peel atomically commits, append exactly
one line for every admitted row, in the same order as Section 1.1:

```text
original_row<TAB>peel_g<TAB>peel_b<TAB>peel_b_square<TAB>survivor<LF>
```

`original_row` is `DEC`; `peel_g` and `peel_b` are `HEX`; and the last two
fields are `BOOL`. The SHA-256 of all lines is `peel_sha256`. If the complete
peel does not commit, the preimage is empty. No computed prefix, abandoned
temporary, or absent-field spelling enters the digest.

### 1.3 Basis stream

After the complete basis stream atomically commits, append one suffix line
per published basis record:

```text
basis_kind<TAB>ordinal<TAB>mask_0<TAB>mask_1<TAB>mask_2<TAB>mask_3<TAB>mask_4<TAB>R_mod_N<TAB>X<TAB>rho<TAB>gcd_minus<TAB>gcd_plus<TAB>root_class<LF>
```

`basis_kind` is `L` or `Q`; `ordinal` is `DEC`; every mask is `MASK`; the
five arithmetic values are `HEX`; and `root_class` is the D13 text token.
Lines use canonical `L` then `Q` order and increasing ordinal inside each
basis. The SHA-256 of all lines is `basis_sha256`. If the complete basis
stream does not commit, the preimage is empty and no basis row is published.

### 1.4 Required two-way reconstruction

Evaluation computes each bank digest from its immutable logical records
before public serialization. After the complete public files are rendered in
memory, it independently projects the committed TSV data rows:

- from `rows.tsv`, select the seven Section 1.1 fields for the row digest;
- from rows whose four peel fields are present, select the five Section 1.2
  fields for the peel digest; and
- from `basis.tsv`, remove only the five bank-wrapper fields and select the
  thirteen Section 1.3 fields.

It reconstructs every LF-terminated suffix byte, recomputes all three hashes,
and requires equality with the internal values and bank-summary fields before
writing a success manifest. Replay performs both computations again from its
regenerated internal records and from the authenticated committed TSV rows.
Any disagreement is fatal and permits no success manifest or finite label.

The split-level core manifests continue to hash complete wrapped public files.
The event digests retain their distinct D09/D13 raw-event suffix preimages.
No digest is a continuation from a final digest value.

## 2. Partial-source publication and atomic absence

This section adds an express absence permission to the D13 scalar-row schema.
Only these four fields may now be the literal `-`:

```text
peel_g peel_b peel_b_square survivor
```

They are either all present or all absent in every row of one bank. No mixed
state is legal.

Every admitted source row is published in `F265-D15.SPLIT.rows.tsv`, including
a row admitted before a later `DIRECT_STOP`, `BANK_SKIP`, or
`RESOURCE_REJECT`. Rows retain the Section 1.1 order. The packet
counter remains split-spanning as required by D12. Define the split-local
`ADMITTED_ROWS` value as the discovery packet value for discovery and as the
heldout packet value minus the authenticated final discovery packet value for
heldout. This split-local value, the sum of the split's bank `row_count`
fields, the split meta `row_count`, and the scalar TSV data-row count must all
be equal. The serialized heldout packet counter remains cumulative and is not
reset. If no row is admitted in a split, all four split-local counts are zero;
every empty bank row stream has the empty hash.

No partial orbit enters the peel or F271. The complete mixed bank must reach
the inherited peel boundary before any peel result can commit. The peel is
constructed in a bank-local temporary state and publishes atomically:

- if the complete peel commits, all four peel fields are present on every row,
  `survivor_count` is the exact sum of survivor bits, and `peel_sha256` covers
  all rows;
- if source generation stops first, or a recoverable resource result prevents
  the complete peel commit, all four fields are `-` on every published row,
  `survivor_count=0`, and `peel_sha256` is the empty hash.

A later decoder, record, or writer resource result does not erase a peel that
already committed. Conversely, no partial peel row or partial peel digest is
published. The absent survivor spelling is not the Boolean zero and is not
counted as a nonsurvivor.

Basis publication is also all or nothing. No basis row is published and the
basis digest is empty unless the complete canonical `L`-then-`Q` stream and
all classifications commit. A later non-basis resource outcome does not
rewrite a basis stream that already committed.

These rules change no status precedence. Sticky factor events remain public
under the inherited D13 rule even when a later resource result rejects the
bank. Bank counters retain every operation actually performed. No absent peel
or basis field is converted into a mathematical zero, an empty-core
certificate, or an eligibility claim.

The `-` spellings only shorten a scalar row, so the corrected D14 450-byte
maximum and unchanged 512-byte row cap remain safe. The packet row maximum was
already the `ADMITTED_ROWS` cap of 122,112, so every file and aggregate byte
cap remains unchanged.

## 3. Exact duration bytes and rational projection

### 3.1 `SECONDS9`

`SECONDS9` is a canonical nonnegative decimal number of seconds. Its integer
part is `DEC`, followed by one dot and exactly nine decimal fractional digits.
It has no sign and no exponent. Examples are `0.000000000`, `1.000000001`,
and `10800.000000000`.

For every monotonic interval, represent the clock-tick difference and the
clock period as exact integers. Convert the elapsed value to rational
nanoseconds and take the mathematical ceiling. No floating-point conversion
or truncating duration cast is legal. The result is one nonnegative integer
number of nanoseconds.

To serialize an integer `t_ns`, write `floor(t_ns/1,000,000,000)` as the
integer part and write `t_ns mod 1,000,000,000` as exactly nine digits after
the dot. This is the only conversion from a duration to public text.

### 3.2 Exact fixture rates and projection

Each fixture repetition first converts its elapsed interval to an integer
nanosecond ceiling. A fixture time is the maximum of its registered repetition
values. Every rate is the exact nonnegative rational

```text
fixture_maximum_nanoseconds / exact_registered_denominator.
```

All additions and multiplications in `T_source`, `T_decoder`, `T_pass`,
`T_raw`, and `T_projected` use arbitrary-precision integers and exact reduced
rationals measured in nanoseconds. No binary or decimal floating-point value
enters a gate. The inherited D11 source and decoder expressions survive, and
the inherited D14 I/O coefficient gives

```text
T_pass = T_source + T_decoder
       + 60,372*rho_factor
       + 226,088,448*rho_io.

T_raw = 2*T_pass + 900,000,000,000 nanoseconds.
T_projected = (7/4)*T_raw.
```

The multiplier `1.75` is therefore exactly `7/4`. Define

```text
projected_ns = ceil(T_projected).
```

The production projection gate is evaluated as the exact rational comparison

```text
T_projected <= 10,800,000,000,000 nanoseconds.
```

Because the right side is an integer, this is equivalent to
`projected_ns<=10,800,000,000,000`. Both checks must agree. Serialize
`projected_seconds` by applying `SECONDS9` to `projected_ns`.

The 900-second diagnostic charge appears exactly once as shown. The separate
14,400-second whole-process runner deadline and 300-second finalization
reserve remain authoritative and are not replaced by this arithmetic.

### 3.3 Complete preflight interval

In `preflight` mode, first complete lexical CLI and option validation. This
includes the mode grammar, the exact option set, repeated-option rejection,
the `ABS` string grammar, and the `WORKERS` grammar. It does not open an input
file or input root.

Start the monotonic preflight interval immediately after that validation and
before opening or authenticating any preflight input. The interval includes:

1. every descriptor-relative input and output-root check performed before
   output creation;
2. complete fixture-root, verification-root, and both public-corpus
   authentication;
3. fixture parsing, expansion, operand-digest checks, every registered
   repetition and trace update, and all outside-timer semantic verification;
4. exact rate and projection arithmetic and both projection comparisons;
5. preparation of every non-duration preflight TSV field in memory,
   including `fixtures` and `preflight_bytes`; and
6. the final retained-input reauthentication and stable-membership checks.

Take the end timestamp after all six items succeed and before opening or
creating the preflight output temporary. Convert the interval to its integer
nanosecond ceiling `preflight_ns`. Require

```text
preflight_ns <= 1,200,000,000,000.
```

Serialize `preflight_seconds` by applying `SECONDS9` to `preflight_ns`. A
failed time or projection gate writes no PASS manifest. Output-root temporary
creation, file writing, flush, close, verification, and rename occur after the
preflight interval but remain inside the separate whole-process deadline.

### 3.4 `fixtures` and `preflight_bytes`

`fixtures` is the decimal integer `37`, the complete D13 fixture vocabulary.

The earlier composition did not define `preflight_bytes`. D15 defines it as
the exact **unique authenticated input footprint** of preflight. Sum the
recorded complete-file `size` values, once per required logical input file,
for these twelve files:

1. the eight fixed members of the fixture payload root;
2. the two fixed members of the fixture verification root; and
3. the discovery and heldout public corpus files.

Use the sizes from the authenticated first identity tuples. Reauthentication
must confirm those sizes. Count each required logical file role once even if
the implementation reads or hashes it more than once. Do not count directory
bytes, in-memory operand expansion, in-memory result traces, repeated reads,
or any output-root byte. Serialize the sum as `DEC`.

This definition has no self-reference: neither `F265-D15.preflight.tsv` nor
`F265-D15.PREFLIGHT.sha256` enters the field it contains. Their actual byte
sizes remain governed separately by the inherited 1,048,576-byte TSV cap and
65,536-byte manifest cap. `preflight_bytes` is ready before the interval end
required by Section 3.3.

## 4. D15 roots, names, and source tokens

The D15 materializer theory root is the SHA-256 of sixteen LF-terminated
lines. The first fifteen lines are the import table above in displayed order.
The sixteenth line is the final SHA-256 of this
`D15_DRAFT_PREREGISTRATION.md` byte as authenticated by a future D15 theory
audit. Every line is `filename`, tab, hash, LF. The materializer and
independently authored verifier pin all sixteen names, hashes, and their order.
This sixteen-line rule replaces every inherited reference to the thirteen-line
D14 rule.

All fixture filenames, payload and verification manifests, evaluation files,
replay files, seal files, diagnostic files, private files, and their root
constructions retain their D14 rules with `F265-D15` prefixes. The four source
roles and ten invocation grammars retain their D14 rules with `f265_d15_`
prefixes.

The future public source contains exactly one occurrence of each token:

```text
@F265_D15_FIXTURE_PAYLOAD_ROOT@
@F265_D15_FIXTURE_VERIFICATION_ROOT@
```

The future private source contains one separate occurrence of each same
token. The four-occurrence one-edit replacement, fresh source evidence, and
fresh hostile source-audit requirement survive unchanged. Materializer and
verifier source contain no placeholder.

## 5. Explicitly unchanged caps and authorization

D15 changes no row, event, file, packet, output, temporary, directory,
operation, timer, arena, RSS, process, or deadline cap. In particular, the
256-byte event-row cap, 512-byte scalar-row cap, 226,088,448-byte total output
cap, 262,400-byte one-bank temporary cap, 309,990,912-byte directory-peak cap,
128 MiB per-file cap, 3.5 GiB measured-RSS cap, 1,200-second preflight cap,
10,800-second projection gate, 300-second finalization reserve, and
14,400-second whole-process deadline survive.

No D15 mode is authorized to execute under this draft. A fresh no-context
D15 theory audit must authenticate all fifteen inputs and audit the complete
D09--D15 additive composition. A D15 theory PASS may authorize only drafting
the four D15 source roles. It does not authorize source freezing, a source
PASS, compilation, a fixture byte, fixture verification, preflight, local or
remote execution, a result, packaging, or a ledger edit.

Pending approved hard dynamic containment remains an absolute gate for every
fixture, scientific, audit-process, and production mode. D15 supplies no
runner, launch command, or fallback.
