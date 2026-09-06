# F268-D03 preregistration — canonical scalar-section multirow search

## 1. Frozen question

For the canonical scalar rows

\[
 U_E(a)=[a^E]_{N^2}\equiv Y_E(a)^2\pmod N,
\]

does a factor-blind public bank contain a non-global exact square-class
dependency after all registered direct screens and the complete singleton and
support-two square-class subspace have been removed?

The search is finite guidance. It neither proves nor estimates an unbounded
success probability.

## 2. Immutable algebra and source boundary

`ALGEBRA.md` is the exact algebra. The only P66 rows are positive canonical
power residues `U_E(a)`. High digits, base carries, inverse quotients,
multiplication quotients, differences, sums, and Miller-chain values are
direct controls only. They never enter the square-class list.

All five exponents and all twelve families are frozen in
`FAMILY_SYNTAX.tsv`. Any family, exponent, template, cap, cohort, rank tuple,
or screen change creates a new version.

The analysis process receives a public case containing only
`(version,split,shape,factor_bits,index,N)`. Its `Case` type has no `p`, `q`,
marker, shifted-order, or hidden-residual field. Base generation, row
generation, screens, decoding, and pattern predicates use only `N`, frozen
syntax identifiers, and public arithmetic. Discovery aggregation and ranking
receive only arithmetic `BankResult` records. Their interface has no `Case`,
shape, factor-bit, `p,q`, marker, or hidden-label field.

Corpus construction is a separate C++ process. It necessarily constructs
`p,q`, but writes them only to a mode-600 label file. The public corpus ends
at `N`. The corpus process exits before search starts. A separate post-run
label audit can read the label file only after the complete held-out public
evaluation and lead gate are closed. Labels never flow back into selection or
ranking.

## 3. Bounded factor-blind base source

The master seed is

`0xF268CA110A5E5EED`.

For every `(N,family,syntax slot,attempt)`, SplitMix64 hashes the complete
public `N` and identifiers. A candidate is reduced into `[1,N)`. Every
candidate gcd is stage 1. A proper gcd is a direct factor and a full gcd is a
rejection. Each requested seed has 256 attempts. A family has 8192 total
source attempts, including orbit candidates. Exhaustion is `RESOURCE_REJECT`,
not a null bank.

Derived values are canonical residues. They receive the same gcd treatment.
Each bank enforces unique retained bases, so its frozen construction has no
duplicate `(base,exponent)` rows. Syntax and occurrence metadata remain
attached.

The twelve families are exactly the family rows in `FAMILY_SYNTAX.tsv`.
Discovery is the broad small-bank stage. It uses 24 rows per family, except
family 10, which uses four bases crossed with five exponents for 20 rows.
Heldout is the frozen larger-bank replay. It uses 48 rows for each selected
family, except family 10, which uses nine bases crossed with five exponents
for 45 rows. Both tiers perform their complete singleton and pair
classification. A small-bank result is never represented as a complete test
of its larger heldout bank.

Family 11 enumerates pairs `(i,j)` in increasing `i+j`, then decreasing `i`,
starting at `(1,0),(0,1)`, and uses `[a^i b^j]_N`. It rotates the five
exponent tags by that public order. No score or hidden label prunes the orbit.

## 4. Cohorts

The ordinary shapes are:

- `random`: independent exact-bit primes;
- `neighbor`: choose `p`, skip a public interval of at least `2^(bits/4)`,
  then take the first prime. The constructor verifies that this is not the
  immediate next prime after `p`;
- `safe-safe`: `p=2r+1` and `q=2s+1`, with all four values prime.

All rows have distinct primes, `p<q<2p`, exact declared factor bits, and
globally distinct moduli.

```text
discovery factor bits: 12,16,20,24,32
discovery count:       12 per bit and ordinary shape
heldout factor bits:   40,48,56,60
heldout count:         24 per bit and ordinary shape
```

This gives 180 intended ordinary discovery moduli and 288 intended ordinary
held-out moduli.

### Finite P209/F244 control

The constructor also tries to build `marker-control` rows. These are finite
interface controls, not instances of the unbounded Linnik theorem. It accepts
only a pair with four distinct public label primes
`lambda_plus,lambda_minus,rho_plus,rho_minus>5` satisfying

```text
lambda_plus  | p-1,   lambda_minus | p+1,
rho_plus     | q-1,   rho_minus    | q+1,
ord_lambda_plus(q)=lambda_plus-1,
ord_lambda_minus(q)=lambda_minus-1,
ord_rho_plus(p)=rho_plus-1,
ord_rho_minus(p)=rho_minus-1,
gcd(p-1,q-1)=2, gcd(p-1,q+1)=12,
gcd(p+1,q-1)=2, gcd(p+1,q+1)=2.
```

The public analysis sees only shape `marker-control` and `N`. Discovery tries
two rows at each of 12,16,20,24 factor bits. Heldout tries two rows at each of
20,24,28,32 factor bits under a disjoint seed domain. Each requested marker
row has exactly 4,096 seeded pair attempts. Within one pair attempt, the
constructor tests at most 128 candidates for `p = 13 (mod 24)` and then at
most 128 candidates for `q = 11 (mod 72)`. Failure of either constrained-prime
request discards that pair attempt. These nested caps are part of the finite
cohort. They permit at most 1,048,576 constrained-prime candidate tests per
requested marker row. A shortfall is explicit and is not backfilled or
treated as a null result. The post-run label auditor verifies every displayed
condition, the mode-600 label boundary, and the exact shortfall count in every
registered marker cell.

Ordinary exact-bit prime requests have 200,000 candidates. Constrained marker
prime requests have 128 candidates. Safe-prime requests have 1,000,000. One
ordinary corpus row has 128 pair retries. Neighbor scanning has 200,000
candidates. Primality is deterministic for every 64-bit factor.

## 5. Complete screen order and eligibility

The eight global stages are exactly those in `ALGEBRA.md`. Every stage emits
`tests,unit,full,proper` and the partition identity. Every exact quotient
checks divisibility and its algebraic congruence. The stage-4 carry equalities
are fatal assertions.

All registered stage-1 through stage-6 screens finish before P66. A proper
gcd makes the bank non-strict, but public arithmetic already scheduled in the
same stage finishes and keeps its counters. A failed identity aborts the
entire run. It never becomes an ineligible or null bank.

A bank is eligible only if it supplies its full frozen row set, stays within
every cap, authenticates its complete P66 kernel, and serializes replay
evidence. On the no-useful-low-support branch it also completes the residual
quotient and stage 8. A useful singleton or pair is already a terminal exact
factor disposition. That bank serializes the certificate and closes the
residual branch instead of quotienting the useful vector.

If a later P66 or evidence cap rejects a bank after the full low-support scan,
all completed singleton and pair records remain serialized when any of them
is useful. The bank stays `RESOURCE_REJECT` and is not eligible or null, but
the already exact factor certificates are never erased. Replay reconstructs
the complete low-support list in that disposition. A rejection before the
complete low-support scan has no low-support interpretation.

## 6. Exact low-support quotient and certificates

The immutable target chronology is:

1. use the stage-1 source gcds to construct the complete public bank and
   attach frozen syntax metadata;
2. finish direct stages 2 through 4 without modifying the bank;
3. classify every exact rational singleton and support-two squareclass;
4. count and serialize every useful low-support factor certificate;
5. put only verified `GLOBAL_PLUS` or `GLOBAL_MINUS` decoys into the
   low-support basis;
6. authenticate the complete P66 kernel; and
7. only on the no-useful branch, extend the global-decoy basis to `K` and
   test the residual quotient basis.

Thus no useful singleton or support-two relation is discarded. If one
exists, it terminates the residual branch for that bank. Otherwise the
verified-global basis is exactly the complete span `L_<=2`, and only the
complement vectors are residual relations.

Every residual vector has support at least three. Every relation record gives
the selected row IDs, exact product root, supplied root, normalized root, two
signed gcds, root class, and all matching frozen template IDs. Every bank
also emits all rows and every pairwise-coprime opaque block with its complete
sparse exponent vector. Thus validation can reconstruct the parity matrix,
the low-support span, and the quotient basis without factoring a block.

## 7. Caps

```text
discovery rows per bank             20 or 24
heldout rows per bank               45 or 48
total input-row bits                    65,536
gcd-free split/merge steps              25,000
final opaque blocks                      4,096
low-support relation certificates        1,176
quotient-basis relations                    48
exact relation bits per bank          1,500,000
serialized evidence per bank          2,097,152 bytes
workers                                      8
total uncompressed output             805,306,368 bytes
target wall projection                     12,600 seconds
target peak RSS                         3.5 GiB
```

Crossing a bank cap is `RESOURCE_REJECT`. It is not a null result. Crossing a
global cap stops before discovery or heldout as appropriate.

## 8. Discovery ranking

Discovery evaluates all twelve families. Exact rational rates are compared
by integer cross-products. The rank tuple is:

1. eligible banks per intended bank, descending;
2. strict residual-factor banks per eligible bank, descending;
3. residual-quotient-positive banks per eligible bank, descending;
4. total residual quotient dimension per eligible bank, descending;
5. total tested rows, ascending; and
6. family ID, ascending.

The first four families are selected.

The ranking code receives only arithmetic bank results. It receives no
`Case`, shape, factor-bit, `p,q`, marker, or label object. Cohort names are
used only in heldout coverage and finite interpretation after selection.

The twelve frozen pattern predicates are ranked by:

1. strict residual-factor bank incidences, descending;
2. residual relation incidences, descending; and
3. template ID, ascending.

The first six templates are selected. A relation can match multiple templates.
No discovered syntax can become a new template in D03.

## 9. Selection authentication and heldout firewall

The exact bytes of `FAMILY_SYNTAX.tsv` have a compiled SHA-256 in the search
source. Both discovery and heldout read the bytes once, compute SHA-256
internally, and require that digest. The runner independently checks the same
bytes against `FROZEN.sha256`.

Discovery closes its output and selection file, computes the selection digest
from the exact closed bytes, and emits that digest. The runner captures the
emitted digest in a read-only shell variable and independently hashes the
file. A sidecar is convenience only.

Heldout receives the captured digest as an argument. It reads the selection
bytes once, verifies the digest internally, validates all rank fields, reruns
both rank comparators, requires the selected IDs to be the rank prefixes, and
requires the embedded family-syntax and discovery-corpus digests. It reads no
discovery bank, relation, certificate, or pattern evidence. The runner
rechecks the same selection bytes after heldout.

Heldout evaluates only the four authenticated families. The lead report
counts only the six authenticated templates, while still reporting all frozen
template diagnostics separately.

## 10. Frozen lead gates

A `strict finite lead` requires all of:

- at least two exact stage-8 factor certificates;
- at least two factor sizes;
- at least one safe-safe, nonconsecutive-neighbor, or marker-control row;
- at least two authenticated selected templates among the certificates;
- no earlier proper gcd in each counted bank; and
- complete replay validation.

A `finite null signal` requires no public factor at any stage, at least 90%
eligible intended held-out banks, and one selected family with at least 20
eligible banks in every ordinary held-out cell. Marker-control shortfalls do
not invalidate ordinary coverage. Neither gate has asymptotic meaning.

## 11. Preflight and launch gate

The C++ corpus generator first creates the complete real discovery and
held-out corpora, including safe-safe generation and bounded marker-control
attempts. Its full generation wall and RSS are timed. The search preflight
timer starts before family authentication and public-corpus parsing, then
evaluates every family on the largest
real public `N` in each ordinary shape and the largest available marker
control. Ordinary sample cases come from heldout and therefore use the
larger 45/48-row layouts. This includes a 48-row bank and its complete pair
scan, source grammar construction, row powers, all eight stage-3 gcds per
unordered row pair, every singleton and support-two rational squareclass test,
low-support quotient, P66 decoder, certificates, and serialization. Preflight
records and asserts the exact row-power, singleton, pair-gcd, and
support-two-test counts. It cannot substitute nominal counts for executing
these paths.

The staged scale responds to a measured neighboring-packet failure, not to a
post-result edit. F265-D02 observed 2,369,895 complete pair bundles in
3,316.220420 wall seconds, or 714.637358152448 pair bundles per wall second,
and rejected its 335,199-second full projection. F268 compiles that observed
rate into its C++ gate. It computes the conservative worst-selected-family
pair-bundle count from the generated corpus and the frozen
discovery/heldout row counts. Its analysis projection is the largest of:

1. twice the measured F268 preflight wall time scaled by exact pair bundles;
2. twice the measured F268 preflight wall time scaled by task count; and
3. twice the full pair bundles divided by the observed F265 rate.

The final wall projection adds twice the complete measured corpus-generation
wall time to the largest analysis projection.

This historical floor cannot make a slow F268 preflight pass. Complete
support-at-most-two testing remains mandatory inside every eligible bank.

The runner measures corpus-generation and bank-preflight wall time and RSS
with `/usr/bin/time`. A C++ gate combines both measurements. It uses a factor
two wall/output safety multiplier, eight-worker measured RSS, the exact task
counts, and exact sample byte components. It must project at most 12,600
seconds, 3.5 GiB RSS, and 768 MiB uncompressed output. Its live-memory gate is
the maximum of measured RSS and `512 MiB + 4*projected_output_bytes`, which
covers retained bank objects, serialization, and replay copies. It also requires zero
preflight resource rejects and at least one completed 48-row bank.

Only a passing gate permits discovery. F268 must not compile or launch while
F265 is active. The frozen packet therefore stops at static hostile pre-run
audit.

## 12. Interpretation

A strict certificate factors its displayed finite modulus. A repeated
held-out pattern can motivate a theorem. It cannot establish an all-input
probability or runtime law. A null closes only this exact finite grammar and
these exact cohorts.
