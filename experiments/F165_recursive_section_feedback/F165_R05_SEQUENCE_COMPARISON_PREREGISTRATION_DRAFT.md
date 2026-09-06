# F165-R05 semantic sequence comparison preregistration draft

Status: frozen draft for root registration. Do not run until the root agent
adds this exact packet to `REGISTRY.md` and gives explicit authorization.

## Exact claim

Compare the complete ordered F165-D01 and F165-R04 finite transcripts after
translating their different encodings into the same semantics. The comparison
covers all 64 corpus inputs and all three snapshots for each input.

The registered D01 commitments have these meanings:

- feedback candidate: the ordered eight-integer payload
  `(support size, first basis index + 1, second basis index + 1 or 0, z, w,
  A, gcd minus, gcd plus)` with no trailing element count;
- exact value: the ordered retained `A` values;
- block: the ordered active parity-block values;
- selected column: the ordered original ledger indices selected by
  first-occurrence elimination with largest active row as pivot.

R04 stores typed dictionaries with more metadata. The comparison source does
not import or execute either F165 implementation. It reads the two frozen
outputs and does all of the following:

1. verifies every pinned input hash;
2. checks corpus and stage alignment;
3. reconstructs every base candidate from `N`;
4. reconstructs every feedback candidate from the prior frozen selected
   basis, including support order, record indices, decorated residue,
   canonical inverse, exact value, both gcds, disposition, and duplicate-root
   status;
5. replays first-occurrence ledger metadata and compares every detailed R04
   exact-value entry;
6. translates every R04 candidate, exact-value, block, and selected-column
   sequence into the D01 encodings and checks the registered per-stage D01
   digests;
7. independently reconstructs parity decompositions and deterministic
   selected-column bases from the exact values and ordered blocks, then
   compares every detailed R04 selected-column entry;
8. checks pairwise block coprimality, absence of perfect-power blocks, unit
   status modulo `N`, and decorated-lift identities;
9. recomputes all R04 per-stage detailed/value-only hashes and all four R04
   aggregate hashes;
10. compares adjacent rows, columns, rank, nullity, normalized-root counts,
    and selected-basis counts so a sequence match cannot hide a decoder-summary
    mismatch.

The output returns `PASS` only if every check matches. Otherwise it returns
`FAIL`, a category count, and the first exact mismatch. It retains at most 128
mismatch examples while still counting all mismatches.

## Frozen artifacts

| Artifact | Absolute path | SHA-256 |
|---|---|---|
| Comparison source | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r05_sequence_compare.py` | `2dcb4e871b890c16c575f2c0168295c757e40187b514a0d1c223a7034f85e397` |
| Timeout runner | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r05_sequence_compare_timeout_runner.py` | `477fb932338c873cdb60f1ffd5fab576bd75592e8db260d343f0ad1a3ca5c1a4` |
| D01 source | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/search.py` | `2a7852f8438003f0db1dd49b7721d02ae2c1cfcea8b114f1e58cc69b74f04427` |
| D01 output | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/OUTPUT.json` | `94ca36ee995819d384e260d50213105b58c3b91377b3a8e51ba155fa7b218dcc` |
| D01 result | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/RESULT.md` | `04ff14f6f0664073565c36370308c610569518f84fbd005b8ad3f835edd717d3` |
| D01 manifest | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/MANIFEST.md` | `df609f058087c0632e48f2d88192c8abca9d59032d8ad008ca1d74e9dbf8c50c` |
| Blind statement | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/V2_BLIND_STATEMENT.md` | `1681967c7ac14b44361d58284716250e73a7f8bda15203f3bc2d6a4971139cdd` |
| R04 source | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r04_v2_blind_reconstruct.py` | `a3b1a94440d3e6e580bccc6efe189a73a86adc366c4e617acc06a5a56377b42f` |
| R04 output | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r04_v2_blind_output.json` | `f29dddd1893c81cde798425cacc40da0c619b1260a9763793973bb016881a56d` |
| R04 log | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r04_v2_blind_run.log` | `da45648fe4dc2aaa8299564d2c85b47be3369e79d6c9d74e40aebed2944f8a9c` |
| R04 report | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/F165_R04_BLIND_RECONSTRUCTION.md` | `dfcf023c8d9a011e758bdb36183b3351083ffc78bb98197f08b196ef18a5c321` |
| R04 proof | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/F165_R04_V2_FIXED_DEPTH_PROOF_DRAFT.md` | `39a36e862162d405d15943f59995010c1471e6af8baef6e2b7b9d7f984a9b380` |

## Preserved failure history

The runner also pins the existing failure records and refuses to alter them:

| Artifact | SHA-256 |
|---|---|
| `BLIND_PRELAUNCH_FAILED.md` | `5acd76f4dface996e91d8a650ab5d507ea965a97a82015e5cda9a787a3a92374` |
| `F165_R02_FAILURE.md` | `9fe1950843427f04311df0be2cefd878b197b2e8ecf335b66014782d733d9efc` |
| `F165_R02_PROOF_HASH_PROVENANCE.md` | `8cad01061c02a2443f5622364d885729a779eae03f02338af5de491d3ab3588e` |
| `BLIND_RECONSTRUCTION_FAILED.md` | `dfb9cfeb7b13f7d97a8ab981f6a655dee48d5a3e53bdecc0355bbaf0beb17217` |

## Run registration

- Working directory:
  `/Users/zhou/autoresearch/IntegerFactoring`
- Authoritative command:
  `python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r05_sequence_compare_timeout_runner.py`
- Hard timeout: 600 seconds.
- Intended log:
  `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r05_sequence_compare_run.log`
- Intended output:
  `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r05_sequence_compare_output.json`
- Estimated peak memory: 256 MiB.
- Both result paths are absent at freeze time.
- The runner creates the log exclusively.
- The comparison source creates the output exclusively.
- The runner refuses to overwrite either path.
- The root must inspect current memory pressure and running processes before
  authorization. The runner records `vm_stat` but does not run the
  sandbox-incompatible `ps` preflight that caused preserved R02 to fail.

## Decision rule

Return `PASS` only if all sequence, semantic, hash-integrity, and adjacent
decoder-summary checks match. Return `FAIL` otherwise. Preserve the log and
output even on mathematical mismatch. A nonzero exit caused by `FAIL` is a
valid completed audit result and must not be rerun at the same paths.

This is a finite transcript comparison only. It cannot establish an all-input
success theorem, a density statement, a growing-depth bound, or the top-level
factoring claim. The fixed-depth theorem receives a separate proof-only
hostile audit and is not decided by this computation.
