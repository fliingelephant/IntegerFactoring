# F165-R06 corrected reconstruction and comparison preregistration draft

Status: frozen draft for root registration. Do not run until the root agent
adds this exact packet to `REGISTRY.md`, completes the required external
memory/process audit, and explicitly authorizes the exact command below.

## Closest prior run and preserved failure

The closest prior run is F165-R05. Its registered comparison ran once and
returned mathematical `FAIL`. It found zero mismatches in all candidate,
exact-value, block, and selected-column sequences, but exactly 384
decoder-summary mismatches. R04 omitted one retained `A=1` zero parity column
at each of 128 feedback snapshots. This lowered columns, nullity, and
global-plus count by one at each snapshot.

R05 remains preserved:

| Artifact | SHA-256 |
|---|---|
| R05 source | `2dcb4e871b890c16c575f2c0168295c757e40187b514a0d1c223a7034f85e397` |
| R05 runner | `477fb932338c873cdb60f1ffd5fab576bd75592e8db260d343f0ad1a3ca5c1a4` |
| R05 preregistration | `92d0a3e49df9967598c8c512a1edbff3ed8720b91bd8cd1b0e502948eb058bfd` |
| R05 log | `efa73913905e03c2b89c330eee8aa6103c8c5d64506f21c1a57b4645b28211b1` |
| R05 output | `9b61f73aa8b860ae6741b868edc1acaf309ce57f75e895c8a71dc3b637fba080` |
| R05 failure report | `ef36a2c90a556d6d917ac9087c066487ca51fd3161a7b6b1bdf67d4431d0cc97` |

R06 uses fresh sources and fresh result paths. It does not rerun or overwrite
R05.

## Sole mathematical repair

The R06 reconstruction starts from byte-frozen R04. It keeps the full ledger
for parity-column construction and applies `A>1` only to factor-free integer
refinement inputs. Therefore retained `A=1` records become empty-vector,
lift-one columns exactly as in D01.

The only mathematical source diff is the placement of this filter. The
docstring and output schema also receive R06 identifiers. The complete exact
diff and the comparison lineage are frozen in
`F165_R06_SOURCE_PROVENANCE.md`.

## One sequential workflow

The single runner performs two stages under one 600-second deadline:

1. run the fresh R06 reconstruction and create its output exclusively;
2. only if reconstruction exits zero, run the fresh R06 hostile comparison
   against D01 and the preserved R04 transcript, then create its output
   exclusively.

The log contains separate `stage_begin` and `stage_return_code` sections for
reconstruction and comparison. A failure or timeout at either stage is
preserved and stops the workflow. No stage is rerun.

The comparison preserves all R05 normalization and semantic replay. It also
requires:

- all D01/R06 sequence and decoder-summary comparisons to pass;
- all R06 sequences to remain exactly equal to R04 sequences;
- all 64 base decoder summaries to remain unchanged from R04;
- at all 128 feedback snapshots, R06 columns, nullity, and global-plus count
  to equal R04 plus one;
- rows, rank, global-minus count, and non-global count to remain unchanged;
- all observed counts and aggregate hashes to equal
  `F165_R06_EXPECTED_OUTPUTS.json`.

## Frozen artifacts

| Artifact | Absolute path | SHA-256 |
|---|---|---|
| R06 reconstruction source | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r06_v2_reconstruct.py` | `252123931d35856febfd93c07c8e22072564bf6310d75093d5eb169a07f09838` |
| R06 comparison source | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r06_sequence_compare.py` | `fa2742f2562f2288f7c93114fb4f02d1a6691ab920c46b62fbae23dfd4285c7b` |
| Sequential timeout runner | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r06_timeout_runner.py` | `dd048920430b9003dcdcd498e3de9e2c44026703a9d8b7e026ff712732eacf0f` |
| Frozen expected outputs | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/F165_R06_EXPECTED_OUTPUTS.json` | `f4b066fbb1580a67846538c2381e9b7a377ad00225b9116fa3aaffa709eb1c68` |
| Source provenance | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/F165_R06_SOURCE_PROVENANCE.md` | `14e0f62f90205f5a26f9215cdc175b3bf5b365e81c3ba45721069b403d0d0589` |
| D01 source | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/search.py` | `2a7852f8438003f0db1dd49b7721d02ae2c1cfcea8b114f1e58cc69b74f04427` |
| D01 output | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/OUTPUT.json` | `94ca36ee995819d384e260d50213105b58c3b91377b3a8e51ba155fa7b218dcc` |
| R04 source | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r04_v2_blind_reconstruct.py` | `a3b1a94440d3e6e580bccc6efe189a73a86adc366c4e617acc06a5a56377b42f` |
| R04 output | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r04_v2_blind_output.json` | `f29dddd1893c81cde798425cacc40da0c619b1260a9763793973bb016881a56d` |
| R04 fixed-depth proof | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/F165_R04_V2_FIXED_DEPTH_PROOF_DRAFT.md` | `39a36e862162d405d15943f59995010c1471e6af8baef6e2b7b9d7f984a9b380` |

The runner additionally pins the R04 log/report/runner, all R05 frozen and
generated artifacts, and the R01-R03 failure records before launch.

## Frozen expected outputs

The exact machine-readable expectations are in
`F165_R06_EXPECTED_OUTPUTS.json`. In summary:

- reconstruction schema: `F165-R06-V2-reconstruction-1`;
- reconstruction replay status: `STATED_FINITE_CLAIMS_MATCH`;
- comparison status: `PASS`;
- comparison mismatches: 0;
- inputs compared: 64;
- snapshots compared: 192;
- candidate entries: 15,644;
- exact-value entries: 3,220;
- block entries: 4,323;
- selected-column entries: 3,089;
- D01 candidate digest checks: 128;
- D01 exact/block/selected digest checks: 192 each;
- corrected feedback snapshots: 128;
- all detailed and value-only aggregate sequence hashes unchanged from R04.

No generated output file hash is predicted. The outputs must be created by the
registered workflow, then hashed and preserved.

## Run registration

- Working directory:
  `/Users/zhou/autoresearch/IntegerFactoring`
- Authoritative command:
  `python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r06_timeout_runner.py`
- Total hard timeout: 600 seconds across both child stages.
- Estimated peak memory: 256 MiB. The stages execute sequentially.
- Intended log:
  `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r06_run.log`
- Intended reconstruction output:
  `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r06_v2_reconstruct_output.json`
- Intended comparison output:
  `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r06_sequence_compare_output.json`
- All three result paths are absent at freeze time.
- The runner and both children use exclusive creation and refuse overwrite.
- The runner records `vm_stat`. It does not use the sandbox-incompatible `ps`
  preflight that caused preserved R02 to fail.

## Decision rule

Return workflow `PASS` only if reconstruction exits zero, produces its output,
comparison exits zero, produces its output, and every frozen expected check
passes. Return nonzero at the first failed stage. Preserve all created
artifacts and do not rerun at the same paths after any mathematical,
infrastructure, or timeout failure.

This packet decides only exact finite reconstruction. It does not decide the
fixed-depth proof audit and makes no density, growing-depth, all-input success,
or factoring claim.
