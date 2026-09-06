# F165-R02 V2 blind reconstruction preregistration draft

Status: frozen draft for root registration. Do not run until the root agent
adds this run to `REGISTRY.md` and gives explicit authorization.

## Independence record

- The SHA-256 of `V2_BLIND_STATEMENT.md` was checked before the file was
  opened. It matched the required digest.
- That statement was the only F165 mathematical, evidence, or source file
  read.
- Repository-root `PROMPT.md` was read only for the computation protocol.
- No other file in the F165 experiment directory was read. No F165 program
  was imported.
- The replay source was independently implemented. No mathematical
  computation has been run.

## Frozen artifacts

| Artifact | Absolute path | SHA-256 |
|---|---|---|
| Blind statement | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/V2_BLIND_STATEMENT.md` | `1681967c7ac14b44361d58284716250e73a7f8bda15203f3bc2d6a4971139cdd` |
| Replay source | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r02_v2_blind_reconstruct.py` | `d6b0dc314c3ab4108218acc709b7a04a0b1e040a6213497a41b6356c9a09d6c1` |
| Timeout runner | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r02_v2_blind_timeout_runner.py` | `cb155b48c2f2708e83a3d703cc306577450ded7d3cd55da0e30d093ffdda991b` |
| Fixed-depth proof draft | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/F165_R02_V2_FIXED_DEPTH_PROOF_DRAFT.md` | `ceb6e30d5759f21ad51dc4b97f41370b6fb7234546adeb1c9264653b34aa03aa` |

The runner independently verifies the frozen statement and replay-source
hashes before it starts the child process. The runner itself is frozen by the
digest in this registration.

## Run registration

- Working directory:
  `/Users/zhou/autoresearch/IntegerFactoring`
- Authoritative command:
  `python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r02_v2_blind_timeout_runner.py`
- Hard timeout: 600 seconds.
- Intended log:
  `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r02_v2_blind_run.log`
- Intended output:
  `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r02_v2_blind_output.json`
- Estimated peak memory: 256 MiB.
- Both intended result paths were absent at freeze time. The runner uses
  exclusive creation and refuses to overwrite either path.

Before authorization, the root agent must inspect current memory pressure and
running processes. The runner also records `vm_stat` and the largest resident
processes in the log immediately before launch.

## Frozen reconstruction semantics

1. Construct the prime-pair corpus in the stated lexicographic order and check
   its special corpus digest before analyzing an input.
2. Give the public analyzer only (N). Use (p,q) only after the public result
   returns, to classify proper gcd outputs.
3. Retain the first exact (A). Before discarding a duplicate, compare the
   decorated roots by their modular ratio and test both signs.
4. Build a multiplicity-aware gcd-free basis from labelled exact values.
   Extract maximal perfect powers without factoring. Derive pairwise coprime
   nonsquare parity blocks and exact square parts.
5. Use largest-active-row Gaussian pivots. Record a complete kernel basis and
   the first-occurrence selected-column basis with its actual decorated lifts.
6. Test every kernel-basis square dependency with an exact positive square
   root, normalized supplied root, and both signed gcds.
7. Freeze the selected basis at each of exactly two levels. Scan support one in
   basis order. Then scan support two in lexicographic basis-index order. Do
   not expose a new record to the current scan.
8. Rebuild the complete union decoder after each level. Refine each old active
   parity block against all new factor-free components, including components
   that become square-only in the union. Record all required accounting,
   old-block refinements, certificates, raw canonical sequences, and hashes.

## Sequence-hash encoding

The statement does not publish reference sequence digests or their encoding.
This reconstruction therefore freezes both raw sequences and an independent
encoding before the run. The encoding is typed recursive framing:

- `N`, `T`, and `F` are the null and Boolean tags.
- `I`, `S`, `L`, and `D` tag a nonnegative integer, UTF-8 string, list, and
  dictionary.
- Every byte length or item count is an unsigned eight-byte big-endian value.
- Integer payloads use shortest unsigned big-endian form.
- Dictionary keys are strings and sort lexicographically.

The output contains detailed and value-only hashes at each input and level,
plus aggregate hashes. A PASS requires the root to compare these against an
independently registered reference or compare the raw sequences semantically.
The replay source does not manufacture a PASS when no reference digest was
published. It reports the first stated finite mismatch, or reports that the
stated counts match while the registered hash comparison and proof audit are
pending.

## Decision rule

Return FAIL at the first exact mismatch in this order:

1. corpus digest;
2. base null/positive count and the unique base certificate;
3. survival through both levels and absence of level-two-only success;
4. level-one and level-two aggregate accounting;
5. first stated block refinements;
6. registered candidate, exact-value, block, and selected-column sequences.

Return PASS only if all finite comparisons pass and the independent
fixed-depth proof survives audit. The finite replay is not evidence for a
success theorem or any stronger scope excluded by the statement.
