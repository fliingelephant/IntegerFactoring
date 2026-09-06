# F266-D03 preregistration — split-quadratic discriminant-lift search

F266-D03 is the narrow successor to immutable failed packet F266-D02. D01,
D02, and both hostile FAIL audits remain unchanged. The algebraic grammar,
family IDs, word source, matrix caps, lift levels, tickets, decoys, cohorts,
and registered ranking tuple are unchanged. D03 keeps the valid D02
shared-lift, stage-order, certificate, opaque-block, and baseline repairs. It
repairs only D02's null-coverage quantifier, missing direct counters,
preflight-byte evidence, selection phase anchor, compression envelope, and
ranking-row implementation drift.

## 1. Frozen question

Do public canonical `SL_2(Z)` orbits of split binary quadratic forms produce
any of the following after all cheaper direct screens fail?

- an orbit singleton square with a mixed supplied root;
- a proper invariant-carry gcd;
- a useful exact square-multiple template; or
- a nonduplicate multirow P66 relation with a non-global root.

The search also asks whether safe-safe and neighbor semiprimes force private
gcd-free pivots, global roots, or linearly worsening carry-ticket rates.

Finite data are guidance only.

## 2. Public-source firewall

The source seed is

`0xF26651D17A11C0DE`.

For one registered input, hidden `p,q` are used only to construct the corpus
and to label a factor after exact public evaluation. The following objects
are functions only of the complete public `N`, the frozen seed, the split
name, and public syntax identifiers:

- all base residues `a,r,s`;
- all `N^2` lift gauges;
- every quadratic coefficient;
- both lift levels;
- every `SL_2(Z)` word and matrix;
- every public row cap and hash choice;
- all canonicalization decisions;
- every direct screen and relation calculation; and
- discovery ranking and family selection.

The executable has one analysis entry point that accepts `N` but no factor.
Labels are attached only after it returns. The self-test checks this interface.

Every source unit uses a public stream of at most 128 candidates. A rejected
candidate is gcd-screened. A proper gcd is a direct certificate. A full gcd
is rejected. Stream exhaustion is `RESOURCE_REJECT`.

## 3. Frozen base families

Each family uses two public base IDs. Roots are canonicalized as an unordered
pair. The eight families are:

| ID | root mode | maximum word length | public matrix cap |
|---:|---|---:|---:|
| 0 | independent uniform units | 3 | 16 |
| 1 | small coprime units below `min(N,n^3+31)` | 5 | 20 |
| 2 | adjacent units `s=r+1` after screens | 7 | 24 |
| 3 | symmetric units `s=-r` after screens | 6 | 24 |
| 4 | inverse-correlated units `s=r^-1` | 7 | 24 |
| 5 | affine units `s=2r+1` | 6 | 24 |
| 6 | central-half units | 5 | 20 |
| 7 | power-correlated units `r=u^2,s=u^3` | 7 | 24 |

The leading coefficient is a separate public unit in every family. If a
formula gives equal roots or a nonunit root/difference, the source advances
the bounded public stream. It does not change family.

At level `m=N`, use the canonical base residues. Before any word is selected
or evaluated, choose one public gauge triple for each base ID. At level
`m=N^2`, replace each of `a,r,s` by

`value + N*(public gauge in [0,N))`.

Thus the two levels have the same residues and supplied root modulo `N`.
Every matrix in the base uses the same three lifted integers and the same
exact `N^2` base discriminant. No word-dependent gauge is permitted.

## 4. Frozen word source

Enumerate words in length/code order over

`U(1), U(-1), L(1), L(-1), S`.

Adjacent exact inverse letters are rejected. Compute each matrix over the
integers. Require determinant one and the frozen `4^7` entry bound.
Canonicalize `M` and `-M` by the lexicographically smaller four-entry tuple.
Deduplicate exact matrices.

Identity is always retained. Rank all other matrices by

`SplitMix64(hash(N),family,base,word syntax,source seed)`

and retain the smallest keys up to the family cap. This selection is public
and happens before a coefficient or row is evaluated.

After both lift levels are evaluated, canonicalize exact coefficient triples,
then equal rows and square multiples as specified in `ALGEBRA.md`. If more
than 96 residual rows remain, retain the 96 smallest public syntax hashes.
No score or factor label enters this cap.

## 5. Direct-screen order

The complete direct order is fixed:

1. source root/coefficient/difference gcds;
2. base discriminant and supplied-root gcds;
3. transformed coefficient and discriminant gcds;
4. projective root coordinate and determinant gcds;
5. pairwise quadratic resultants;
6. invariant-carry, same-level quotient, and cross-level quotient gcds;
7. base and orbit singleton-square comparisons; and
8. equal-row and square-multiple comparisons.

Every exact result is retained in counters. The first proper gcd is retained
as a certificate. Analysis may finish already public arithmetic, but no later
event in that bank is strict.

For each of the eight stages, every bank writes four exact counters:
`tests`, `unit`, `full`, and `proper`. They satisfy
`tests = unit + full + proper`. A normalized-root comparison contributes its
two signed gcd tests. These counters include rejected source attempts and
global-root decoys.

Each numbered item is one global stage across all retained rows or pairs. A
later stage for one row cannot run before an earlier stage finishes for every
row. Every exact invariant and quotient divisibility assertion is fatal on
failure. Such a failure cannot become an ineligible bank or a null result.

## 6. Residual decoder and labels

After canonical decoys are removed, run the complete factor-free P66 decoder.
Every opaque block is labelled `UNKNOWN_OPAQUE_NOT_NEEDED`. No Pollard-rho or
unbounded integer factorization runs.

One residual row map and every final block value, sparse exponent vector,
exact-square flag, and status are serialized for every eligible bank.

Every relation certificate verifies the exact product square, supplied root,
normalized root, and both signed gcds. The first applicable label is:

1. `BASE_SINGLETON`;
2. `ORBIT_SINGLETON`;
3. `CARRY_TICKET`;
4. `EQUAL_ROW_DECOY`;
5. `SQUARE_MULTIPLE_TEMPLATE`;
6. `STABILIZER_DECOY`;
7. `SAME_BASE_MULTIROW`;
8. `CROSS_BASE_MULTIROW`; or
9. `CROSS_LEVEL_MULTIROW`.

An equal positive row always keeps `EQUAL_ROW_DECOY`; it never increments the
square-multiple-template score. Singleton, equal-row, square-multiple, carry,
resultant, and P66 factor certificates retain the original integer ticket and
all row data needed for exact replay.

Root class is separately `GLOBAL_PLUS`, `GLOBAL_MINUS`, or `USEFUL`.

## 7. Cohorts and generation caps

Factor sizes and counts per shape are:

```text
discovery: 12,16,20,24,32 bits; 16 rows per size and shape
heldout:    40,48,56,60 bits;    32 rows per size and shape
```

Shapes are:

- `random`: two independent exact-bit primes;
- `neighbor`: one exact-bit prime and the next prime after a public odd
  offset, while preserving the exact bit size and balance; and
- `safe-safe`: `p=2r+1,q=2s+1` with all four values prime.

Every row satisfies `p<q<2p`. All moduli are distinct across both splits and
all shapes. Discovery has 240 intended moduli. Heldout has 384 intended
moduli. A cell shortfall is explicit and is never refilled from another
shape.

One ordinary prime request has 200,000 candidate tests. One safe-prime
request has 1,000,000 candidate tests. One corpus row has 128 pair retries.
One neighbor scan has 200,000 candidates. All primality tests are deterministic
for 64-bit factors.

## 8. Discovery selection and held-out firewall

Discovery evaluates all eight families. It ranks them by the exact tuple:

1. strict multirow-hit banks per eligible bank, descending;
2. carry-ticket banks with no earlier coefficient/root/resultant factor,
   descending;
3. orbit-singleton banks, descending;
4. useful square-multiple banks, descending;
5. residual kernel dimension, descending;
6. private-pivot deficit, descending;
7. eligible safe-safe banks, descending;
8. total tested rows after coefficient-triple deduplication but before
   exact-square and rational-square-class removal, ascending; and
9. family ID, ascending.

Rates are compared by exact integer cross-products. Select the first four
families.

Write one canonical selection file. It contains the version, public discovery
corpus SHA-256, the complete rank tuple for all eight families, and the four
IDs. Close the file and compute SHA-256 from its exact bytes. The discovery
process emits that digest and the corpus digest only after it closes all
discovery output. The runner captures those emitted bytes directly in shell
memory and makes both digest variables read-only before it reads a sidecar.
It then hashes the selection and corpus bytes independently and requires both
hashes and both convenience sidecars to match the captured discovery values.
The sidecars are never a digest authority. Heldout receives the captured
selection digest as a command argument, reads the selection bytes once,
verifies the digest internally, parses those same bytes, and requires four
unique known IDs. The parser requires those IDs, in order, to equal the first
four IDs in the authenticated rank rows and validates every rank-field
syntax. It reads no discovery certificate or metric file.

The heldout process verifies the public discovery-corpus digest named inside
the selection packet. It generates heldout inputs only after both checks pass.

## 9. Frozen output

Discovery writes exactly:

```text
F266-D03.discovery.corpus.tsv
F266-D03.discovery.corpus.sha256
F266-D03.discovery.banks.tsv
F266-D03.discovery.families.tsv
F266-D03.discovery.certificates.jsonl
F266-D03.discovery.opaque.jsonl
F266-D03.selection.tsv
F266-D03.selection.sha256
F266-D03.discovery.manifest.tsv
```

Heldout adds exactly:

```text
F266-D03.heldout.corpus.tsv
F266-D03.heldout.banks.tsv
F266-D03.heldout.families.tsv
F266-D03.heldout.certificates.jsonl
F266-D03.heldout.opaque.jsonl
F266-D03.heldout.lead_gate.tsv
F266-D03.heldout.manifest.tsv
```

One bank row contains all direct-channel counters, canonicalization counters,
P66 rank/nullity, root-class counters, the number of distinct positive row
values, and the exact comparison numerator `2*k` and denominator `N` for the
uniform principal-digit baseline. Only eligible banks contribute to cell
baseline sums. Equal integer values count once. The direct counters are the
four-way `tests/unit/full/proper` partition for each registered stage.

At most 64 full certificates are written per family and split. Aggregate
counters continue after the cap. A strict certificate is selected before any
nonstrict certificate in its bank. Positive lead gates count only strict hits
whose full certificate was retained under the cap. Writers refuse overwrite,
check every close, and check the aggregate one-GiB byte budget before each
write.

No dense candidate-by-input matrix is written. Output is plain TSV/JSONL. The
runner compresses a copy with `zstd -T1 -3` only after all uncompressed hashes
and manifests are closed. Compressed bytes do not replace exact evidence.

## 10. Frozen lead gates

A strong finite orbit lead requires all of:

1. at least two strict non-singleton useful banks in heldout;
2. hits in at least two factor sizes;
3. one hit in `safe-safe` or `neighbor`;
4. no hit is preceded by any direct screen; and
5. exact certificates pass every replay check.

A carry lead requires a proper invariant-carry or quotient gcd at 48 bits or
larger in two shapes and two sizes, with no earlier coefficient, root, or
resultant factor.

A singleton anomaly is reported separately. At each cell, report the observed
base and orbit singleton counts and the exact sum of comparison masses
`sum(2*k/N)`. Observed singleton counts include banks that later become
ineligible; comparison mass includes eligible banks only. Emit all 12
size/shape rows, including explicit zero and ineligible counts. No observed
singleton can satisfy the multirow or carry gate.

A null signal requires no heldout public factor in any channel, at least 90
percent eligible selected-family banks, and at least 24 eligible moduli in
every heldout size/shape cell for one and the same selected family. Formally,
the coverage gate is `exists family: for every cell, eligible >= 24`; the
weaker `for every cell: exists family` condition is forbidden. Emit all 48
selected-family/cell coverage rows with intended, eligible, ineligible, and
pass counts, and emit the first covering family ID or `-1`. Other outcomes
are inconclusive.

No finite label is an asymptotic conclusion.

## 11. Resource contract

The complete remote packet has a four-hour wall cap. It uses at most eight
workers, `nice 15`, a 4 GiB virtual-memory cap, and a 1 GiB uncompressed
output cap. Source maxima are:

- factor bits: 60;
- input bits: 120;
- lift level: `N^2`;
- row bits: `4n+2 <= 482`;
- bases per family: 2;
- matrices per base: 24;
- rows before canonicalization: 96;
- residual rows: 96;
- exact relation-product bits: at most 46,272;
- gcd-free steps: 25,000;
- opaque blocks: 4,096;
- certificates: 64 per family and split; and
- workers: 8.

Before compilation, the runner records and gates CPUs, load, memory, disk, and
the top processes. The deadline starts before compilation. Compilation,
self-test, preflight, discovery, heldout, evidence hashing, and compression all
use the remaining deadline; every executable phase has the 4 GiB virtual-memory
and one-GiB file-size limits. Preflight uses a fixed 1/16 corpus and one worker.
It records wall time, CPU time, peak RSS, rows, pairs, resultants, gcd-free
steps, the measured serialized byte counts for corpus, bank, family,
certificate, and opaque-block payloads, their exact sum, and conservative
eight-worker full-run wall, RSS, and output projections. It stops unless
projected wall time is at most 12,600 seconds, projected RSS is at most
3.5 GiB, projected output is at most 900 MiB, and resource rejections are
zero.

The runner refuses overlap with F258 through F266 production or validation.
Every generation retry and refinement loop has the caps above. It refuses an
existing output, log, preflight, or archive path. Every phase manifest records
byte count, line count, and SHA-256. The aggregate uncompressed cap includes
outputs, preflight evidence, and logs and is checked after every phase. The
final resource record, run manifest, complete uncompressed manifest, and its
digest are closed before compression. Final compression is bounded by the
remaining wall time, `nice 15`, 4 GiB, one GiB per output file, and one
thread. One timeout process owns a pipefail-enabled shell containing both
`tar` and `zstd`; niceness is applied to that shell and inherited by both
pipeline children. An external compression manifest records the archive byte
count, line count, and SHA-256.

## 12. Launch gate

This packet freezes algebra, preregistration, C++17 source, runner, and hashes.
Remote compilation, self-test, preflight, discovery, and heldout are all
`PENDING`.

A fresh hostile pre-run audit must pass before any remote dynamic validation
or corpus execution. A failed audit remains attached to this exact version.
No durable ledger is edited by this freeze.

The F266-D01 and F266-D02 FAIL audits remain attached only to their exact
versions. Neither authorizes a D03 step. D03 needs a fresh independent audit
of its own frozen bytes.
