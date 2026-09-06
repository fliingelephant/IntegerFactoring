# F165 V2 blind reconstruction: FAIL

Status: statement-only independent reconstruction. First exact mismatch:

`level_1.attempted_subsets`: expected `5,020`, actual `4,942`.

The registered R03 command ran once. It was not rerun. The R03 mathematical
source, runner, log, and output remain byte-identical after the run.

## Evidence boundary

Before the source freeze, the reconstruction used
`V2_BLIND_STATEMENT.md` as its only F165 mathematical, evidence, or source
file. Repository-root `PROMPT.md` was read only for protocol. This report uses
only the frozen reconstruction artifacts and the generated R03 log/output. It
does not inspect the original D01 source, output, or result.

## Registered and generated artifacts

| Artifact | SHA-256 |
|---|---|
| Blind statement | `1681967c7ac14b44361d58284716250e73a7f8bda15203f3bc2d6a4971139cdd` |
| Mathematical source `f165_r02_v2_blind_reconstruct.py` | `d6b0dc314c3ab4108218acc709b7a04a0b1e040a6213497a41b6356c9a09d6c1` |
| R03 runner `f165_r03_v2_blind_timeout_runner.py` | `e48fce6d89b3ef0993244ba69dc6de5493b4334ca254d6e40f8ebb3f304fa4d5` |
| R03 preregistration | `a8a074b8092a2d5f4b236f8a9dfb6389bcc4cbe39e78eea32e7b30b8544f68c2` |
| R03 fixed-depth proof | `4e115e98dd9a212876c977ece94abbe7cbc0bf4b1794dc08f72caa1e946975c8` |
| R03 log, 7,921 bytes | `6ab027db34ebfbe995c73ecda3db33f8afb7409d2754489373f612ccd5886437` |
| R03 output, 3,827,097 bytes | `ebe8434731abc0eef7da425aa9b6a425bb63931f1deb0e5db6f8dd4033a49604` |

Authoritative command:

`python3 /Users/zhou/autoresearch/IntegerFactoring/experiments/F165_recursive_section_feedback/f165_r03_v2_blind_timeout_runner.py`

The registered timeout was 600 seconds. The estimated peak memory was
256 MiB.

## Decision order and result

The preregistered decision order was:

1. corpus digest;
2. base null/positive count and unique base certificate;
3. survival through both feedback levels and absence of level-two-only
   success;
4. level-one and level-two aggregate accounting;
5. first stated block refinements;
6. candidate, exact-value, block, and selected-column sequences.

Gates 1--3 passed for the 63 base-null inputs. Gate 4 failed first at
level-one attempted subsets. The output recorded these mismatches in exact
order:

1. level-one attempted subsets: expected 5,020; actual 4,942;
2. level-one strict new exact values: expected 315; actual 313;
3. level-one duplicate exact values: expected 4,705; actual 4,629;
4. level-one inputs with positive rank gain: expected 63; actual 62;
5. level-one total rank gain: expected 251; actual 250;
6. level-two attempted subsets: expected 8,896; actual 8,805;
7. level-two duplicate exact values: expected 8,586; actual 8,495.

All other stated aggregate fields matched. The first block refinements also
matched, but they occur after the failed decision gate and do not change the
verdict. External sequence-hash comparison remained pending because the blind
statement publishes neither reference digests nor their encoding.

## Corpus and certificate status

- Pair count: 64.
- Observed corpus SHA-256:
  `bd1d2987d2eaa6d3cfda3fceea72fbd471592a659137df26ae05a3d86cec7fb3`.
  It matches the statement.
- Base-positive inputs: 1.
- Base-null inputs: 63.
- Inputs null after both executed feedback levels: 63.
- Level-one factor certificates: 0.
- Level-two factor certificates: 0.
- Level-two-only factor certificates: 0.
- Duplicate-root splits: 0 at both levels.
- Proper feedback direct candidates: 0 at both levels.

The unique base certificate was reproduced for

\[
N=100160063,
\quad A=100160064=10008^2,
\]

with supplied-root-normalized residue 10008 and

\[
\gcd(10008-1,N)=10007,
\qquad
\gcd(10008+1,N)=10009.
\]

Post-public classification confirmed both proper outputs are the true factors.

## Complete aggregate accounting

Here, delta means actual minus expected.

| Quantity | L1 expected | L1 actual | L1 delta | L2 expected | L2 actual | L2 delta |
|---|---:|---:|---:|---:|---:|---:|
| attempted subsets | 5,020 | 4,942 | -78 | 8,896 | 8,805 | -91 |
| strict new exact values | 315 | 313 | -2 | 310 | 310 | 0 |
| duplicate exact values | 4,705 | 4,629 | -76 | 8,586 | 8,495 | -91 |
| inputs with positive rank gain | 63 | 62 | -1 | 57 | 57 | 0 |
| total rank gain | 251 | 250 | -1 | 310 | 310 | 0 |
| inputs with strict old-block splits | 42 | 42 | 0 | 38 | 38 | 0 |
| total strictly split old blocks | 67 | 67 | 0 | 69 | 69 | 0 |
| proper direct candidates | 0 | 0 | 0 | 0 | 0 | 0 |
| duplicate-root splits | 0 | 0 | 0 | 0 | 0 | 0 |

For the 63 base-null inputs, the base-rank distribution was:

| Rank | Input count |
|---:|---:|
| 8 | 2 |
| 9 | 6 |
| 10 | 13 |
| 11 | 6 |
| 12 | 13 |
| 13 | 8 |
| 14 | 8 |
| 15 | 5 |
| 16 | 1 |
| 18 | 1 |

Their total base rank was 747. Their total rank after level one was 997.
Their total rank after level two was 1,307. The only executed input with zero
level-one rank gain was (N=105663913): base rank 12, 78 level-one attempts,
one strict new value, 77 duplicates, and unchanged rank 12.

## First block refinements

The first level-one refinements matched at (N=100440259):

\[
1291243=23\cdot56141,
\qquad
32284369=13\cdot2483413.
\]

The first level-two refinement matched at (N=100740469):

\[
11992913=23\cdot521431.
\]

## Frozen sequence hashes

| Sequence | Detailed aggregate hash | Value-only aggregate hash |
|---|---|---|
| candidate | `1331e6f74a4887ba52c42968ff7deaead8e52d75969163330e7bdafb4686efc4` | `51f015a1c6bb94491553c1f5052a0315bc457ec5de8f73d6632dda9012b3d21f` |
| exact value | `4225cb659d03c7da94b72d595730b69db68c7ffb8c835255613580a9382cd2a1` | `c89ab2a991f877578a773583be120051ba8f59f23fc81fda6c2f2fd0e88a7f72` |
| block | `1e931b3a58c5020bc817da44356d5141541e8baaca6bfe5d4251cd49c5c03427` | `111f983b3c2a46b6486cd4a18d15bd809619e01faa99923c229f6da35eec12d0` |
| selected column | `fececa62404d4478eb6c2729548d281a7ac4430c5afced825fa0a5e3ab37ce32` | `7730d25e1d594367dd04f3619df29170203a656e6420d125b0d7431ecbd6cad6` |

## Semantic diagnosis

The statement says to run exactly two frozen feedback levels. The
reconstruction instead returned immediately when the unique base certificate
was found. Thus it omitted both feedback scans for (N=100160063).

The public output is sufficient to account for every mismatch:

- This input had base rank 12, so its omitted support-one/support-two scan has
  (12+{12\choose2}=78) attempts. This is exactly the level-one attempt
  deficit.
- The aggregate deltas partition those 78 attempts into 2 strict new values
  and 76 duplicates. They add one rank, exactly reconciling both level-one
  rank-gain deficits.
- The resulting rank is 13, so the omitted level-two scan has
  (13+{13\choose2}=91) attempts. This is exactly the level-two deficit. The
  other level-two deltas show all 91 would be duplicates with no rank gain.
- Split counts, direct screens, and duplicate-root screens already match at
  both levels.

Therefore the mismatch is an early-termination error in the reconstruction,
not evidence against the public finite claim. Under the frozen decision rule,
the R03 reconstruction still returns FAIL and cannot be repaired or rerun
without a newly registered source.

## Fixed-depth theorem

The fixed-depth quasipolynomial cost theorem independently survives this
reconstruction. The proof bounds layer (h+1) attempts by

\[
(D+1)(R_h+1)^D,
\]

controls every generated record at quasipolynomial bit length, proves that
multiplicity-aware gcd/perfect-power refinement is polynomial in retained
transcript length, and counts complete binary decoding. Induction through each
fixed (H) gives (2^{L^{O_H(1)}}) bit operations and space. The exponent is
not uniform when (H) grows, and the proof gives no success theorem.

This proof status is independent candidate, self-audited in this
reconstruction. It has not completed the hostile-audit and fresh-reconstruction
cadence needed for verifier-backed status. The finite replay failure does not
invalidate the cost theorem.
