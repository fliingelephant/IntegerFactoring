# F268-D04 independent hostile result audit

# Verdict: PASS

## Exact finite interpretation

The packaged result is an authenticated `FINITE_NULL_SIGNAL` for the exact
frozen F268-D04 experiment.

For all 1,184 held-out banks formed by the four frozen selected families on
the 296 held-out cases, every bank was eligible, no public factor occurred at
any stage, and the complete P66 kernel had dimension zero. Therefore there
was no singleton, support-two, or residual square-class relation to compare.
Every one of the 48 ordinary selected-family/factor-bit/shape cells had 24 of
24 eligible banks. The frozen finite-null predicate recomputes to true, and
the frozen strict-lead predicate recomputes to false.

This statement is finite only. It closes this grammar, these separate
per-family banks, and these cohorts. It does not close a post-hoc union of
families. It does not prove an all-input event law, a factoring algorithm, or
an asymptotic running-time bound.

## Authentication

I authenticated the following exact bytes independently:

- `FROZEN.sha256`:
  `de76f2e3fbb264b917cedb5639fde75c979f272e43841452c6f642b8132cdbf4`.
  All 11 frozen entries pass.
- `HOSTILE_PRERUN_AUDIT.md`:
  `22644c280c477e0d6f0272d343bdf15f9421036b9db7c169b951e647cbee26be`.
- `F268-D04.final.sha256`:
  `bdc96777472722a05cd6ef22eb710d03bc1249fe6bda09cf03ef10514e058afc`.
  All 44 records pass after replacing only the recorded remote path prefix
  with the local package path.
- `RESULT.md`:
  `3a2242b29347ac4c0872049fa2af50e4ced356ba30bbda2549def667f30b8ce6`.
- `RUN_MANIFEST.md`:
  `e93f326a0dfc6fd13752873e2589c4e2db55ee7c8b987b2ec44d239caf6bdf5f`.

The 44 manifested files contain 44,657,476 bytes. Adding the 6,246-byte raw
manifest gives 45 raw files and 44,663,722 file bytes, exactly as packaged.
The recorded remote `du -sb` value is 44,669,051 bytes. `RESULT.md` and
`RUN_MANIFEST.md` are later package records and are correctly outside the raw
manifest.

## Corpus and hidden-label boundary

I independently parsed and checked every public and label row. The discovery
corpus has 180 ordinary rows plus eight marker controls. The held-out corpus
has 288 ordinary rows plus eight marker controls. Across both splits:

- all 484 moduli are globally unique;
- every displayed factor pair satisfies `N=p*q`, deterministic 64-bit
  primality, exact declared factor bits, and `p<q<2p`;
- all safe-safe rows have prime `(p-1)/2` and `(q-1)/2`;
- all neighbor rows are nonconsecutive and meet the registered skip bound;
- every ordinary cell has exactly its registered 12 or 24 indices;
- every marker cell has both indices 0 and 1;
- all 16 marker rows satisfy the congruence classes, four distinct prime
  markers above five, the four incidence divisibilities, the four primitive
  order tests, and shifted-gcd tuple `(2,12,2,2)`; and
- the marker-shortfall table is correctly empty.

Both label files retain mode 0600. The two label reports independently match
the raw bank tables: discovery has 188 label rows, eight marker rows, and 356
factor-bearing bank rows; heldout has 296 label rows, eight marker rows, and
zero factor-bearing bank rows.

The search `Case` contains only public metadata and `N`. Discovery ranking
accepts arithmetic `BankResult` records, not labels or factor data. The
runner gives heldout only the public corpus, frozen family syntax, and the
closed selection bytes. It invokes both label audits only after heldout,
heldout replay validation, and lead generation have closed.

## Independent bank and evidence reconstruction

I regenerated the frozen public source grammar from `N`, the master seed,
family, slot, retry, and role. All 109,336 discovery/heldout row records and
all 2,292 preflight row records reproduce exactly, including base, exponent
tag, syntax, group, role, and orbit metadata. For every row I recomputed

`U = a^E mod N^2`, `Y = a^(E/2) mod N`, `low = U mod N`, and
`high = (U-low)/N`,

and checked `Y^2 mod N = low`, the canonical ranges, and unique
`(base,exponent)` rows within each bank.

For every bank I reconstructed every row exactly from the serialized opaque
blocks and sparse exponent vectors. I checked all final blocks pairwise for
coprimality, independently checked every `SQUARE`/`NONSQUARE` label, rebuilt
the parity matrix, and performed binary elimination.

The independent aggregates are:

| Metric | Discovery | Heldout |
|---|---:|---:|
| cases | 188 | 296 |
| banks / eligible / rejected | 2,256 / 2,256 / 0 | 1,184 / 1,184 / 0 |
| rows / parity rank | 53,392 / 53,392 | 55,944 / 55,944 |
| opaque blocks | 70,821 | 71,625 |
| kernel / low / residual dimension | 0 / 0 / 0 | 0 / 0 / 0 |
| singleton tests | 53,392 | 55,944 |
| support-two tests | 606,488 | 1,294,704 |
| singleton / support-two / residual records | 0 / 0 / 0 | 0 / 0 / 0 |
| any-factor / earlier-factor / strict banks | 356 / 356 / 0 | 0 / 0 / 0 |

No evidence file contains a `SINGLETON`, `SUPPORT_TWO`, or `RESIDUAL` record.
This is consistent with the independently reconstructed zero kernels; it is
not missing relation evidence.

All stage partitions satisfy `tests=unit+full+proper`. Discovery stages 1--4
aggregate respectively to `(50,771,50,762,0,9)`,
`(688,742,687,685,20,1,037)`,
`(4,851,904,4,830,243,17,771,3,890)`, and
`(20,680,20,680,0,0)`, where each tuple is
`(tests,unit,full,proper)`. Thus the reported 4,936 proper events are exactly
`9+1,037+3,890`, all before P66 and spread across 356 banks. Heldout stages
1--4 are `(45,288,45,288,0,0)`, `(700,170,700,170,0,0)`,
`(10,357,632,10,330,992,26,640,0)`, and `(10,656,10,656,0,0)`.
Stages 5--8 have zero gcd comparisons because no square relation exists.

The largest observed main bank has 48 rows, 69 blocks, 137 gcd-free steps,
11,484 input-row bits, and 26,829 evidence bytes. These are below the frozen
caps of 48 rows, 4,096 blocks, 25,000 steps, 65,536 bits, and 2,097,152
bytes. All relation counts and relation bits are zero. No source, decoder,
evidence, or output cap produced a rejection.

## Finite full-rank structure

I also tested a stronger finite property visible in the raw block data. A
private pivot is a final nonsquare opaque block whose exponent is odd in
exactly one row of its bank. Its parity equation is that row's unit vector.

- Discovery has 70,781 nonsquare blocks and 40 square blocks. There are
  54,044 private pivots covering all 53,392 rows. Of the rows, 52,745 have
  one private pivot, 642 have two, and five have three. Every family-10 bank
  has coverage 20/20, and every other discovery bank has coverage 24/24.
- Heldout has 71,618 nonsquare blocks and seven square blocks. There are
  56,212 private pivots covering all 55,944 rows. Of the rows, 55,676 have
  one private pivot and 268 have two. Every family-10 bank has coverage
  45/45, and every other held-out bank has coverage 48/48.
- Preflight has 2,929 nonsquare blocks and no square block. Its 2,300 private
  pivots cover all 2,292 rows: 2,284 rows have one and eight have two.

Thus minimum and maximum private-pivot coverage are both 100% in every tier.
Zero rows and zero banks require a non-private linear combination to establish
rank. Each bank separately contains an identity submatrix, which explains its
full rank and zero kernel. This is a post-result finite observation. It is not
an asymptotic claim and does not combine families after selection.

For each discovery modulus, a factor-blind union of all 12 family row lists is
reconstructible from the emitted raw `ROW` records alone: they contain exact
`U`, supplied root, base, exponent, and syntax. One must recompute the
gcd-free refinement from the concatenated rows; the per-bank `BLOCK` lists
cannot simply be concatenated because their coprimality guarantee is only
within one bank. No hidden label is needed. For heldout, the emitted raw rows
contain only selected families `10,0,1,2`, so a 12-family union is not
reconstructible from heldout raw rows/blocks alone. The missing eight row
lists could be regenerated from public `N` and the frozen deterministic
source, but that would be a new post-hoc experiment. I did not run or count
either union as part of this audit.

## Representative and adversarial reconstructions

- Heldout marker-control case 289, family 10, has
  `N=435463689503`, 45 rows, 54 blocks, and rank 45. Row 0 has
  `U=85969537308777956373204`, `Y=1425145871`,
  `low=220445369880`, and
  `U=2^2*3*7^2*146206696103363871383`. The last nonsquare block has sparse
  vector `0:1`, so it is row 0's private pivot. The supplied root congruence
  recomputes exactly.
- The heldout safe-safe case 281, family 0, is an adverse square-block check.
  It has 48 rows and 62 blocks, including square block `361=19^2` with sparse
  vector `2:1,3:1`. Excluding that square block is correct. The remaining 61
  nonsquare equations include 48 private pivots and still have rank 48.
- Discovery case 0, family 7, has
  `N=12767327=3433*3719`, 24 rows, 34 blocks, rank 24, and zero kernel. Its
  first direct certificate is `ROW_MINUS_ONE=3433`. This bank has 186 proper
  stage-2 events and 512 proper stage-3 events. The displayed first factor is
  exactly a labelled prime factor of `N`; the direct hit is not a P66
  relation.

## Selection, gates, chronology, and resources

Reaggregation gives the family rank
`10,0,1,2,3,4,5,6,7,8,9,11`. All arithmetic rates tie at zero after equal
eligibility. Family 10 ranks first because it uses 3,760 discovery rows rather
than 4,512; the rest follow the family-ID tie-break. Every template incidence
is zero, so template rank is `0,1,2,3,4,5,6,7,8,9,10,11`.

The exact selection hash is
`7117de790efaa2afb7a7f84ff2917ca744560671c1d0f7a8a271586418f89df5`.
It embeds the authenticated family-syntax hash and discovery-corpus hash,
contains selected families `10,0,1,2` and templates `0,1,2,3,4,5`, and its
sidecar matches. Every held-out case contains exactly those four families in
that order. I did not construct or assess any post-hoc cross-family bank.

The lead report recomputes exactly: zero strict authenticated banks, factor
sizes, templates, hostile shapes, and any-factor banks; 1,184 eligible of
1,184 intended; and all 48 ordinary coverage rows equal 24/24. Hence
`strict_finite_lead=0` and `finite_null_signal=1`.

Preflight uses the largest real modulus in each of the four shapes and all 12
families. It has 48 tasks, 2,292 row/singleton tests, 53,592 pair tests,
428,736 stage-3 gcds, zero rejects, and 44 completed 48-row banks. Its full
scale recomputes to 3,440 tasks, 110,224 rows, 1,942,040 pair bundles, and
15,536,320 stage-3 pair gcds.

From the raw metrics, the pair-scaled, task-scaled, and F265-floor projections
recompute to 3,682.454560, 7,282.766667, and 5,435.036324 seconds. Adding
twice the 0.04-second corpus time gives 7,282.846667 seconds. Projected output
is 225,349,437 bytes; projected live memory is 1,404,560 KiB. These pass the
12,600-second, 3.5-GiB, and 768-MiB gates.

The recorded actual metrics also reaggregate exactly: discovery used
59.146005 wall seconds, 107,388 KiB peak RSS, and 16,651,834 output bytes;
heldout used 1,082.001378 wall seconds, 159,664 KiB peak RSS, and 26,181,829
output bytes. The resource snapshots span exactly 2,262 seconds.

Preserved times and logs follow the frozen sequence: corpus at 20:50:34 UTC,
preflight at 20:51:25, closed discovery selection at 20:52:24, discovery
validation at 20:53:16, heldout and lead at 21:11:18, then heldout validation,
label audits, and final raw manifest at 21:27:18. Compilation and all three
self-test logs precede corpus generation. Every pass log, evidence digest,
label report, resource metric, and output count agrees with the authenticated
raw files.

No frozen or raw artifact was modified during this audit. This verdict
authenticates only the exact finite result stated above.
