# F165-R03 V2 blind reconstruction preregistration draft

Status: frozen draft for root registration. Do not run until the root agent
registers this exact revision and gives explicit authorization.

## Lineage and independence

F165-R03 reuses the byte-identical F165-R02 mathematical source. It uses a
fresh R03 proof path and does not depend on the disputed registered digest for
the R02 proof path. R02 failed before it launched the mathematical child
because its in-run `ps` preflight was denied by the sandbox. The sole runner
change in R03 is removal of that `ps` subprocess. The root agent already
completed the required process and memory audit externally. The
sandbox-compatible `vm_stat` preflight stays in the runner.

The blind statement was the only F165 mathematical, evidence, or source file
read before the source freeze. Repository-root `PROMPT.md` was read only for
the computation protocol. No F165 program was imported. R02 performed no
mathematical computation, and R03 has not been run.

## Frozen artifacts

| Artifact | Absolute path | SHA-256 |
|---|---|---|
| Blind statement | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/V2_BLIND_STATEMENT.md` | `1681967c7ac14b44361d58284716250e73a7f8bda15203f3bc2d6a4971139cdd` |
| Reused mathematical source | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r02_v2_blind_reconstruct.py` | `d6b0dc314c3ab4108218acc709b7a04a0b1e040a6213497a41b6356c9a09d6c1` |
| R03 timeout runner | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r03_v2_blind_timeout_runner.py` | `e48fce6d89b3ef0993244ba69dc6de5493b4334ca254d6e40f8ebb3f304fa4d5` |
| Fresh R03 fixed-depth proof | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/F165_R03_V2_FIXED_DEPTH_PROOF_DRAFT.md` | `4e115e98dd9a212876c977ece94abbe7cbc0bf4b1794dc08f72caa1e946975c8` |
| R02 failure record | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/F165_R02_FAILURE.md` | `9fe1950843427f04311df0be2cefd878b197b2e8ecf335b66014782d733d9efc` |
| R02 proof-hash provenance | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/F165_R02_PROOF_HASH_PROVENANCE.md` | `8cad01061c02a2443f5622364d885729a779eae03f02338af5de491d3ab3588e` |

The R03 runner verifies the statement and mathematical-source hashes before
launch. Its own digest is frozen by registration.

## Run registration

- Working directory:
  `/Users/zhou/autoresearch/IntegerFactoring`
- Authoritative command:
  `python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r03_v2_blind_timeout_runner.py`
- Hard timeout: 600 seconds.
- Intended log:
  `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r03_v2_blind_run.log`
- Intended output:
  `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r03_v2_blind_output.json`
- Estimated peak memory: 256 MiB.
- Both R03 result paths were absent at freeze time. The runner creates them
  exclusively and refuses to overwrite either path.

## Frozen mathematical workflow

1. Construct the stated 64-pair lexicographic corpus and verify its special
   digest before public analysis.
2. Give the analyzer only (N). Use (p,q) only after its result is complete,
   to classify proper gcd outputs.
3. Retain first exact values. Compare decorated roots before discarding an
   equal value.
4. Use maximal-perfect-power extraction and multiplicity-aware gcd refinement
   to construct pairwise coprime nonsquare parity blocks without factoring.
5. Compute the complete kernel basis and a first-occurrence selected-column
   basis with largest-active-row pivots and actual decorated lifts.
6. Check every kernel-basis dependency by exact square root, normalized
   supplied root, and both signed gcds.
7. At each of two levels, freeze the selected basis. Scan support one in basis
   order and support two lexicographically. Rebuild only after the scan.
8. Compare old active parity blocks with all new factor-free components,
   including components that become square-only in the union.
9. Record all accounting, certificates, raw canonical sequences, detailed
   hashes, and value-only hashes.

The sequence encoding remains the R02 frozen encoding: typed recursive
framing with `N/T/F/I/S/L/D` tags, unsigned eight-byte big-endian lengths,
shortest unsigned big-endian integers, and lexically sorted dictionary keys.
The statement publishes no reference sequence digests or encoding. The output
therefore cannot manufacture PASS. It reports the first stated mismatch, or
reports that the stated finite counts match while external registered sequence
comparison and proof audit remain pending.

## Decision rule

FAIL at the first mismatch in corpus digest, base result, feedback survival,
aggregate accounting, stated first refinements, or registered sequence
comparison. PASS is permitted only after all finite comparisons pass and the
independent fixed-depth proof survives audit. No finite result establishes a
factoring success theorem or any stronger excluded claim.
