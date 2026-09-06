# F165-R04 V2 blind reconstruction report

## Verdict

Finite published claims: **PASS**.

- The corpus digest matches.
- All published base and feedback counts match.
- The unique base certificate matches.
- All 63 base-null inputs remain null through both feedback levels.
- No feedback direct certificate, duplicate-root split, or level-two-only
  certificate occurs.
- The first published block refinements match.

Overall statement verdict: **PENDING EXTERNAL AUDIT**.

Candidate, exact-value, block, and selected-column sequence equality remains
pending comparison with an independently registered reference. The independent
fixed-depth quasipolynomial proof remains a self-audited candidate pending the
required external proof audit. Therefore this report does not promote the
overall result to PASS.

R04 ran once. It was not rerun. Its source, runner, log, and output remain
byte-identical after execution. The original D01 source, output, and result
were not inspected.

## Independence boundary

The reconstruction used `V2_BLIND_STATEMENT.md` as its only F165 mathematical,
evidence, or source file before source freeze. Repository-root `PROMPT.md` was
read only for computation protocol. All later diagnosis and repair used only
the independently written source and its generated R03/R04 artifacts.

## R04 frozen and generated artifacts

| Artifact | SHA-256 |
|---|---|
| Blind statement | `1681967c7ac14b44361d58284716250e73a7f8bda15203f3bc2d6a4971139cdd` |
| R04 source `f165_r04_v2_blind_reconstruct.py` | `a3b1a94440d3e6e580bccc6efe189a73a86adc366c4e617acc06a5a56377b42f` |
| R04 runner `f165_r04_v2_blind_timeout_runner.py` | `0c539e36369d308c71d96b09cd4aac60fcc908cf801d7044631306c75f6d301b` |
| R04 proof `F165_R04_V2_FIXED_DEPTH_PROOF_DRAFT.md` | `39a36e862162d405d15943f59995010c1471e6af8baef6e2b7b9d7f984a9b380` |
| R04 source provenance `F165_R04_SOURCE_DIFF.md` | `265ff3c579510ac274bd90fe705db4f203edba66f9f4642f67c8137b23854036` |
| R04 preregistration | `36e9daca443757cc0b1b153aac6e648f258089dbac64418e1630bee3a0d8c840` |
| R04 log, 7,930 bytes | `da45648fe4dc2aaa8299564d2c85b47be3369e79d6c9d74e40aebed2944f8a9c` |
| R04 output, 3,868,616 bytes | `f29dddd1893c81cde798425cacc40da0c619b1260a9763793973bb016881a56d` |

Authoritative command:

`python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r04_v2_blind_timeout_runner.py`

Registered timeout: 600 seconds. Estimated peak memory: 256 MiB. Runner exit
code: 0. Output replay status: `STATED_FINITE_CLAIMS_MATCH`. First mismatch:
null. Recorded mismatches: none. The output intentionally leaves final status
as `PENDING_REGISTERED_SEQUENCE_HASH_COMPARISON_AND_PROOF_AUDIT`.

## Corpus and certificates

- Ordered pair count: 64.
- Flattened element count: 128.
- Observed corpus SHA-256:
  `bd1d2987d2eaa6d3cfda3fceea72fbd471592a659137df26ae05a3d86cec7fb3`.
- Base-positive inputs: 1.
- Base-null inputs: 63.
- Inputs still null after both feedback levels: 63.
- Level-one successes: 0.
- Level-two successes: 0.
- Level-two-only successes: 0.

The unique base certificate is

\[
N=100160063,
\qquad
A=100160064=10008^2,
\]

with supplied-root-normalized residue 10008 and

\[
\gcd(10008-1,N)=10007,
\qquad
\gcd(10008+1,N)=10009.
\]

Post-public classification confirms both proper gcd outputs are the supplied
corpus factors. The public analyzer received only (N).

## Complete aggregate accounting

| Quantity | Level 1 expected | Level 1 actual | Level 2 expected | Level 2 actual |
|---|---:|---:|---:|---:|
| attempted subsets | 5,020 | 5,020 | 8,896 | 8,896 |
| strict new exact values | 315 | 315 | 310 | 310 |
| duplicate exact values | 4,705 | 4,705 | 8,586 | 8,586 |
| inputs with positive rank gain | 63 | 63 | 57 | 57 |
| total rank gain | 251 | 251 | 310 | 310 |
| inputs with strict old-block splits | 42 | 42 | 38 | 38 |
| total strictly split old blocks | 67 | 67 | 69 | 69 |
| proper direct candidates | 0 | 0 | 0 | 0 |
| duplicate-root splits | 0 | 0 | 0 | 0 |

The base-positive input accounts for the R03 repair exactly:

- level one: rank 12 to 13, 78 attempts, 2 new values, 76 duplicates;
- level two: rank 13 to 13, 91 attempts, 0 new values, 91 duplicates;
- no strict old-block split, direct certificate, or duplicate-root split at
  either feedback level.

## First block refinements

The first level-one refinements occur at (N=100440259):

\[
1291243=23\cdot56141,
\qquad
32284369=13\cdot2483413.
\]

The first level-two refinement occurs at (N=100740469):

\[
11992913=23\cdot521431.
\]

These are factor-free blocks inside exact relation values, not factors of
(N).

## R04 sequence hashes

| Sequence | Detailed aggregate hash | Value-only aggregate hash |
|---|---|---|
| candidate | `96972dcb941ca98ed1fd45bda9e75cb5b5b79e27317d6b2f3767d60ba7b60f88` | `de09e266f8e84359dc607078fb14fb1cd1834fcc053ef520517d30aea017709c` |
| exact value | `b17a5884e2017f2f47d2e3b268a1220d0aab6c6be2f69df7a2160373cefbd08c` | `ef8f327ac85850234089c153c8362dfdb482d2737f78845239540ff3ee18f063` |
| block | `bda32c2be9c39b5616c168c250ca6a3596f4be6ecda20cee2015c785a17ea1df` | `0f1d97498b64c6f16ec6ad587e26c42961e004b2c0dec5e8f2b268da59134652` |
| selected column | `23eaa0350432570c030c5648e6bc85401d3402a054482450686df61cf0d632df` | `da4d73fa3244fdb36ae3b120e951c46ca09d9f499db8e16812ef6252eaf108ef` |

The frozen encoding uses typed recursive framing with `N/T/F/I/S/L/D` tags,
unsigned eight-byte big-endian lengths, shortest unsigned big-endian integer
payloads, and lexically sorted dictionary keys. The blind statement publishes
no reference sequence digests or encoding. Equality is therefore still
pending an external registered comparison.

## Fixed-depth theorem status

The fresh R04 proof independently derives the claimed fixed-depth
quasipolynomial bound. It bounds the next layer's attempt count by

\[
(D+1)(R_h+1)^D,
\]

controls generated record lengths, proves polynomial factor-free refinement
in retained transcript length, counts complete kernel decoding, and inducts
through fixed (H). It also preserves the required limitations: no uniform
bound for growing (H), and no success theorem.

Status: independent self-audited candidate. External hostile proof audit and
fresh end-to-end proof reconstruction remain pending. Thus the proof has not
yet earned verifier-backed status.

## Failure chain and provenance

### R01: withdrawn before run

R01 was frozen, then withdrawn before execution when static review found that
old active parity blocks were compared only with new active rows. A newly
exposed component can instead become square-only across the union. No R01
mathematical computation ran.

Historical R01 packet hashes:

| Artifact | SHA-256 |
|---|---|
| source | `201822a7de92837d15dd66581811d17652d2814e38b057204db90f67ae9c5343` |
| runner | `9de85e9c6d1adadef93ebdea1af83597acbb1007392a9c537f57de7d5efed04c` |
| preregistration | `0466703738df733c464b8f1d32dd189885526a714df533a46355e55cfa91655a` |
| proof | `6684527b567bec8c2505dc4eb98aec6c2c6ee2c65ab021fe499e071b513f1a9d` |

### R02: infrastructure failure before mathematical launch

R02 corrected old-block refinement. Its runner created the log, then the
sandbox denied its in-run `ps` preflight:

`PermissionError: [Errno 1] Operation not permitted: 'ps'`

The mathematical child was never launched. The intended R02 output is absent.
The run was not retried.

| Artifact | SHA-256 |
|---|---|
| source | `d6b0dc314c3ab4108218acc709b7a04a0b1e040a6213497a41b6356c9a09d6c1` |
| runner | `cb155b48c2f2708e83a3d703cc306577450ded7d3cd55da0e30d093ffdda991b` |
| preregistration | `50923bb132036eabaf4618fb931771b07261cc28df936cd44abafad63c030917` |
| observed proof file | `ceb6e30d5759f21ad51dc4b97f41370b6fb7234546adeb1c9264653b34aa03aa` |
| registry-preserved disputed proof digest | `ceb6e30d5759f21ad51dc4eb98aec6c2c6ee2c65ab021fe499e071b513f1a9d` |
| failed log | `ad26d005d1d5a51ae08a20189af1c44fef29b2c7ac972cd7b0403a49e0e2fc91` |
| failure record | `9fe1950843427f04311df0be2cefd878b197b2e8ecf335b66014782d733d9efc` |
| proof-hash provenance | `8cad01061c02a2443f5622364d885729a779eae03f02338af5de491d3ab3588e` |

The disputed digest is the first 24 hexadecimal digits of the observed R02
proof hash joined to the last 40 digits of the historical R01 proof hash. No
file with that digest was observed. The actual R02 proof file was preserved,
and R03 used a fresh proof path.

### R03: mathematical FAIL with exact diagnosis

R03 removed only the sandbox-blocked `ps` preflight and ran the frozen
statement-only source. It completed all 64 public analyses but returned FAIL:

`level_1.attempted_subsets`: expected 5,020; actual 4,942.

The source returned after the unique base certificate and omitted both
feedback levels for that one input. Its omitted rank-12 and rank-13 scans
explain all seven aggregate deltas. This was a reconstruction control-flow
error, not evidence against the finite claim.

| Artifact | SHA-256 |
|---|---|
| reused mathematical source | `d6b0dc314c3ab4108218acc709b7a04a0b1e040a6213497a41b6356c9a09d6c1` |
| runner | `e48fce6d89b3ef0993244ba69dc6de5493b4334ca254d6e40f8ebb3f304fa4d5` |
| final preregistration | `a8a074b8092a2d5f4b236f8a9dfb6389bcc4cbe39e78eea32e7b30b8544f68c2` |
| fresh proof | `4e115e98dd9a212876c977ece94abbe7cbc0bf4b1794dc08f72caa1e946975c8` |
| log | `6ab027db34ebfbe995c73ecda3db33f8afb7409d2754489373f612ccd5886437` |
| output | `ebe8434731abc0eef7da425aa9b6a425bb63931f1deb0e5db6f8dd4033a49604` |
| failure report | `dfb9cfeb7b13f7d97a8ab981f6a655dee48d5a3e53bdecc0355bbaf0beb17217` |

R03 detailed aggregate sequence hashes were:

- candidate:
  `1331e6f74a4887ba52c42968ff7deaead8e52d75969163330e7bdafb4686efc4`;
- exact value:
  `4225cb659d03c7da94b72d595730b69db68c7ffb8c835255613580a9382cd2a1`;
- block:
  `1e931b3a58c5020bc817da44356d5141541e8baaca6bfe5d4251cd49c5c03427`;
- selected column:
  `fececa62404d4478eb6c2729548d281a7ac4430c5afced825fa0a5e3ab37ce32`.

R04 repaired only that control-flow defect. The complete R03-to-R04 source
diff is frozen in `F165_R04_SOURCE_DIFF.md`.

## Scope

This is finite evidence for the exact-value relation decoder plus an
independent candidate proof of the fixed-depth cost theorem. It is not evidence
for a presentation-complete endpoint grammar, density law, minimum-depth law,
all-input success law, or factoring algorithm.
