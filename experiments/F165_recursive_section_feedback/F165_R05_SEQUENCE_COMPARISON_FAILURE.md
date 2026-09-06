# F165-R05 semantic sequence comparison: FAIL

Status: completed registered hostile comparison. The authorized command ran
exactly once. It was not rerun. The source, runner, log, and output remain
byte-identical after execution.

## Verdict

All four complete ordered sequence families match semantically across all 64
inputs and all three snapshots per input:

- candidate sequences: PASS;
- exact-value sequences: PASS;
- block sequences: PASS;
- selected-column sequences: PASS.

The overall registered comparison returns **FAIL** because R04 does not
reproduce three adjacent D01 decoder-summary fields after feedback. There are
exactly 384 mismatches and all have one cause: R04 omits the retained exact
record `A=1` from its decoder columns, while D01 keeps it as a zero parity
column.

## Frozen and generated artifacts

| Artifact | SHA-256 |
|---|---|
| R05 source `f165_r05_sequence_compare.py` | `2dcb4e871b890c16c575f2c0168295c757e40187b514a0d1c223a7034f85e397` |
| R05 runner `f165_r05_sequence_compare_timeout_runner.py` | `477fb932338c873cdb60f1ffd5fab576bd75592e8db260d343f0ad1a3ca5c1a4` |
| R05 preregistration | `92d0a3e49df9967598c8c512a1edbff3ed8720b91bd8cd1b0e502948eb058bfd` |
| R05 log `f165_r05_sequence_compare_run.log` | `efa73913905e03c2b89c330eee8aa6103c8c5d64506f21c1a57b4645b28211b1` |
| R05 output `f165_r05_sequence_compare_output.json` | `9b61f73aa8b860ae6741b868edc1acaf309ce57f75e895c8a71dc3b637fba080` |

The frozen source, runner, and preregistration hashes after the run equal their
registered pre-run hashes.

Authoritative command:

`python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r05_sequence_compare_timeout_runner.py`

The registered timeout was 600 seconds. The estimated peak memory was 256
MiB. The runner exited 1 because the mathematical comparison returned `FAIL`.
This was not an infrastructure failure. The log and output are authoritative
and must not be overwritten or regenerated at the same paths.

## Complete comparison coverage

| Check | Count | Mismatches |
|---|---:|---:|
| Corpus inputs | 64 | 0 |
| Base/feedback snapshots | 192 | 0 structural |
| Candidate entries | 15,644 | 0 |
| Exact-value entries | 3,220 | 0 |
| Block entries | 4,323 | 0 |
| Selected-column entries | 3,089 | 0 |
| D01 feedback candidate digests | 128 | 0 |
| D01 exact-value digests | 192 | 0 |
| D01 block digests | 192 | 0 |
| D01 selected-column digests | 192 | 0 |
| R04 per-stage detailed/value-only hash checks | 1,536 | 0 |
| R04 detailed/value-only aggregate hash checks | 8 | 0 |

The normalized detailed aggregate sequence hashes are exactly the published
R04 detailed hashes:

| Sequence | SHA-256 |
|---|---|
| Candidate | `96972dcb941ca98ed1fd45bda9e75cb5b5b79e27317d6b2f3767d60ba7b60f88` |
| Exact value | `b17a5884e2017f2f47d2e3b268a1220d0aab6c6be2f69df7a2160373cefbd08c` |
| Block | `bda32c2be9c39b5616c168c250ca6a3596f4be6ecda20cee2015c785a17ea1df` |
| Selected column | `23eaa0350432570c030c5648e6bc85401d3402a054482450686df61cf0d632df` |

Thus the different D01 and R04 encodings commit to the same complete ordered
candidate values and arithmetic, retained values and metadata, active blocks,
and selected basis columns.

## First exact mismatch

For the first corpus input `N=100160063`, after level one:

| Field | D01 | R04 |
|---|---:|---:|
| Columns | 15 | 14 |
| Nullity | 2 | 1 |
| Global-plus kernel roots | 1 | 0 |

The output records the first mismatch as:

`instances[0].N=100160063.level_1.columns`: expected D01 value `15`, actual
R04 value `14`.

## Exhaustive mismatch classification

Every corpus input retains `A=1` during level one. The same record remains in
the union at level two. Therefore the mismatch occurs at both feedback
snapshots for every input:

| Field | Mismatched snapshots | R04 delta from D01 |
|---|---:|---:|
| Columns | 128 | -1 |
| Nullity | 128 | -1 |
| Global-plus kernel roots | 128 | -1 |
| **Total** | **384** | |

No base snapshot mismatches. No row, rank, non-global-root,
global-minus-root, selected-basis, candidate, exact-value, block, or selected
column mismatch occurs.

## Root cause

D01 uses two different scopes inside `decode`:

1. it sends only labelled values `A>1` to factor-free integer refinement;
2. it then allocates parity vectors, lifts, and elimination columns for every
   retained ledger record, including `A=1`.

For `A=1`, the decomposition is

\[
1=1^2
\]

with empty parity vector and decorated lift 1. It is a zero parity column. It
adds one kernel dependency with global-plus normalized root. It adds no row
and cannot change rank or the selected basis.

R04 instead creates `active_records` by filtering to `A>1` and uses that same
filtered list for both integer refinement and column construction. This drops
the `A=1` column completely. The omission explains all 384 mismatches.

## Consequence and repair boundary

The error is inert for the feedback candidate grammar in this corpus. A zero
parity column is never selected, so it cannot affect selected-column order,
decorated lifts, support enumeration, candidate arithmetic, retained exact
values, block refinement, rank, or factor certificates. This is why all four
full sequence families and all substantive finite outcomes match.

It is still a real exact-reconstruction failure. R04 cannot receive overall
PASS as a complete D01 replay while its recorded column, nullity, and
global-plus counts differ.

The minimal mathematical repair is to keep the `A>1` filter only on the
factor-free refinement inputs and to build decoder columns over the complete
ledger. No corpus, ledger, refinement, elimination, feedback, hash encoding,
certificate, or fixed-depth proof change is needed.

## Scope

This failure concerns exact finite transcript reconstruction. It does not
refute the fixed-depth cost theorem. It also does not establish any success
density, minimum depth, growing-depth bound, all-input source theorem, or
factoring algorithm.
