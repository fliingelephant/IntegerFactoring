# F165-R04 V2 blind reconstruction preregistration draft

Status: frozen draft for root registration. Do not run until the root agent
registers this exact revision and gives explicit authorization.

## Lineage and independence

R03 is preserved as FAIL. Its statement-only output proved that one
early-return branch skipped both required feedback levels for the unique
base-positive input. R04 copies the byte-frozen R03 mathematical source to a
fresh path and makes only the control-flow repair recorded in
`F165_R04_SOURCE_DIFF.md`:

- execute exactly two feedback levels for every input, even after a
  certificate is known;
- preserve the earliest success stage and canonicalize repeated certificates;
- aggregate and inspect feedback over all inputs that now execute it.

No mathematical operation, corpus rule, decoder rule, candidate order, hash
encoding, or claimed expectation changed. The blind statement remains the
only F165 mathematical, evidence, or source file used to design the replay.
The original D01 source, output, and result were not inspected. R04 has not
been run.

## Frozen artifacts

| Artifact | Absolute path | SHA-256 |
|---|---|---|
| Blind statement | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/V2_BLIND_STATEMENT.md` | `1681967c7ac14b44361d58284716250e73a7f8bda15203f3bc2d6a4971139cdd` |
| R04 mathematical source | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r04_v2_blind_reconstruct.py` | `a3b1a94440d3e6e580bccc6efe189a73a86adc366c4e617acc06a5a56377b42f` |
| R04 timeout runner | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r04_v2_blind_timeout_runner.py` | `0c539e36369d308c71d96b09cd4aac60fcc908cf801d7044631306c75f6d301b` |
| R04 fixed-depth proof | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/F165_R04_V2_FIXED_DEPTH_PROOF_DRAFT.md` | `39a36e862162d405d15943f59995010c1471e6af8baef6e2b7b9d7f984a9b380` |
| R04 source-diff provenance | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/F165_R04_SOURCE_DIFF.md` | `265ff3c579510ac274bd90fe705db4f203edba66f9f4642f67c8137b23854036` |
| Preserved R03 failure report | `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/BLIND_RECONSTRUCTION_FAILED.md` | `dfb9cfeb7b13f7d97a8ab981f6a655dee48d5a3e53bdecc0355bbaf0beb17217` |

The runner verifies the frozen statement and R04 source hashes before launch.
Its own digest is frozen by registration.

## Run registration

- Working directory:
  `/Users/zhou/autoresearch/IntegerFactoring`
- Authoritative command:
  `python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r04_v2_blind_timeout_runner.py`
- Hard timeout: 600 seconds.
- Intended log:
  `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r04_v2_blind_run.log`
- Intended output:
  `/Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r04_v2_blind_output.json`
- Estimated peak memory: 256 MiB.
- Both R04 result paths were absent at freeze time. The runner creates them
  exclusively and refuses to overwrite either path.
- The root's external memory/process audit for this byte-equivalent workload
  remains the authorization gate. The runner also records `vm_stat` before it
  launches the child.

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
7. For every input, run exactly two levels. At each level, freeze the selected
   basis, scan support one in basis order, then scan support two
   lexicographically. Rebuild only after the scan.
8. Compare old active parity blocks with all new factor-free components,
   including components that become square-only in the union.
9. Record all accounting, certificates, raw canonical sequences, detailed
   hashes, and value-only hashes.

The sequence encoding remains typed recursive framing with `N/T/F/I/S/L/D`
tags, unsigned eight-byte big-endian lengths, shortest unsigned big-endian
integers, and lexically sorted dictionary keys.

## Decision rule

FAIL at the first mismatch in this order:

1. corpus digest;
2. base null/positive count and the unique base certificate;
3. survival through both levels and absence of level-two-only success;
4. level-one and level-two aggregate accounting over all 64 executed inputs;
5. first stated block refinements;
6. registered candidate, exact-value, block, and selected-column sequences.

The blind statement does not publish reference sequence digests or their
encoding. The replay therefore reports stated finite agreement while external
registered sequence comparison and proof audit remain pending; it does not
manufacture PASS. PASS is permitted only after all finite comparisons pass and
the independent fixed-depth proof survives the required audit. No finite
result establishes a factoring success theorem or any stronger excluded
claim.
