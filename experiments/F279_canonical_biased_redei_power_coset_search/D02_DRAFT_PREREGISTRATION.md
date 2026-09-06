# F279-D02 draft preregistration — canonical biased Rédei power-coset search

## Status, authority, and predecessor

F279-D02 is an unfrozen theory-only preregistration. It authorizes no source,
runner, fixture, random tape, freeze, compile, benchmark, experiment, remote
access, private-label access, ledger change, git staging, or commit.

The immutable D01 drafts remain at these hashes:

```text
DRAFT_ALGEBRA.md
328c8c26d5c06e3033300539fd5900f7ddcb55f253b75fae851c58db47eea424

DRAFT_PREREGISTRATION.md
4498a4f3e2404297d6eda58036fc45e097915a13d73077dc9511dea4e6cb7e7e
```

The normative D02 algebra is `D02_DRAFT_ALGEBRA.md`. D02 asks only:

> Does one fixed factor-blind bank of canonical integer source-target pairs
> produce repeated held-out `box_unexplained_exclusive` hits after every
> cleanup and relation in the explicitly registered D02 screen box?

The phrase `box_unexplained_exclusive` has the finite meaning in the D02
algebra. It makes no claim about relations outside the registered box.

Every canonical JSON `version` value is the exact string `F279-D02`.

## 1. Noncircular authorization sequence

The workflow has four separate authority states.

1. **Theory draft.** The present state permits edits to the two D02 theory
   drafts only.
2. **Theory PASS.** A strict fresh no-context audit of exact D02 hashes may
   authorize drafting source and a runner. It authorizes only text creation
   and static inspection. It does not authorize compilation or execution.
3. **Static implementation PASS.** A later hostile audit must pass the exact
   source, runner, schemas, and containment manifest. Only that PASS may
   authorize freezing the implementation packet and compiling it.
4. **Validated packet.** The frozen binary must pass self-tests, the capacity
   benchmark, the preflight formulas, fixture authentication, and the fixed
   runtime boundary. Only then may a separately authorized experiment run.

Source cannot be statically audited before it exists. Therefore source
drafting is intentionally allowed after state 2, while every compile or run
remains forbidden until state 3. No state permits an unaudited fallback.

## 2. Promised rows and split fixture model

Every labelled row satisfies

```text
N = p*q
p and q are distinct odd primes
p < q < 2*p
p and q have the declared exact factor bit length
B = floor(sqrt(N))
n = bitlength(N)
```

The generator creates two different fixtures for each phase.

### 2.1 Public-N fixture

The public classifier can read only this schema:

```text
row_id<TAB>N<TAB>diagnostic
```

`diagnostic` is `0` or `1`. The fixture contains no `p`, `q`, local
character, hit orientation, or per-row cohort token.

### 2.2 Private-label fixture

Only the promise validator and the post-seal label process can read this
schema:

```text
row_id<TAB>p<TAB>q<TAB>factor_bits<TAB>cohort
```

The allowed cohort tokens are exactly:

```text
random_balanced
wide_gap
four_capacity_at_most_32
consecutive_prime
```

The private fixture is never an argument, open file descriptor, mapped file,
environment value, working-directory descendant, or readable path of the
public classifier.

### 2.3 Promise attestation

Before public classification, a separate label-aware validator authenticates
both fixtures, joins them by `row_id`, and verifies every promised condition,
cohort predicate, count, and distinct-`N` condition. It writes a public
attestation containing only:

```text
version
phase
public_fixture_bytes
public_fixture_sha256
private_fixture_bytes
private_fixture_sha256
row_count
promise_pass
validator_binary_sha256
```

The private-fixture hash authenticates bytes without exposing their fields.
The public classifier authenticates the public fixture and the attestation.
It does not repeat a factor-label check that it cannot perform without
`p,q`.

The public classifier recomputes `B` with an exact integer square root and
checks

```text
B*B <= N < (B+1)*(B+1).
```

It also checks that `N` is odd, `N>1`, every row ID is canonical, and the
public row count is exact.

Both fixture files have the displayed header as their first line. Public
rows use row-ID byte order. Private rows use the same row-ID order.

## 3. Canonical integer and byte conventions

All modular values are canonical residues in `[0,N)`. Euclidean division
uses nonnegative operands. Every quotient, remainder, inverse, and inverse
quotient is formed as an integer before reduction modulo `N`.

All text artifacts use this byte grammar:

1. Encoding is UTF-8, restricted to ASCII bytes `0x20` through `0x7e`, TAB,
   and LF.
2. A line ends with one LF byte. CR is forbidden. Every nonempty text file
   has one final LF.
3. TSV uses one TAB between fields. Spaces around fields are forbidden.
4. An unsigned integer is `0` or a decimal digit `1` through `9` followed by
   zero or more decimal digits. Leading zeroes and `+` are forbidden.
5. A signed integer is `0` or optional `-` followed by a canonical unsigned
   nonzero integer.
6. A hash is exactly 64 lowercase hexadecimal bytes.
7. A present enum or identifier must match its registered token exactly.
8. An absent TSV field is one hyphen byte `-`.
9. JSON never omits a schema key. An absent JSON value is `null`.
10. JSON is one line. It has no insignificant whitespace. Keys occur in the
    schema order. Integers use the decimal rule above. Booleans are `true`
    or `false`. Strings use only registered ASCII token characters and need
    no escape sequence.

Byte comparison means unsigned lexicographic comparison. If one byte string
is a prefix of another, the shorter string sorts first. Numeric comparison
means mathematical integer comparison. A schema always states which order
it uses.

## 4. Canonical anchors, expressions, sources, and candidates

The anchor array is exactly

```text
anchor[0..8] = {-4,-3,-2,-1,0,1,2,3,4}.
```

The expression array is exactly

```text
expr[00] = +x
expr[01] = -x
expr[02] = +d
expr[03] = -d
expr[04] = +r
expr[05] = -r
expr[06] = +u
expr[07] = -u
expr[08] = +k
expr[09] = -k
```

For source-anchor index `i`, trace-expression ordinal `tt`, and
discriminant-expression ordinal `ee`, the source ID is exactly

```text
sI-tTT-eEE
```

where `I` is one digit `0` through `8`, and `TT,EE` are two digits `00`
through `09`. The source ordinal is

```text
source_ordinal = 100*i + 10*tt + ee.
```

For target-anchor index `j` and target-expression ordinal `vv`, the complete
candidate ID is exactly

```text
sI-tTT-eEE-dJ-vVV
```

with the same widths. A candidate is valid only when `abs(i-j)<=1`.

Candidate numeric order is lexicographic order of

```text
(i,tt,ee,j,vv)
```

using integer comparison. Because every component has fixed-width ASCII
digits in its registered position, this order equals unsigned byte order of
the candidate ID. Enumeration and every score tie-break use this order.

There are exactly 900 source IDs and 25,000 valid candidate IDs. Their
ordinals are their zero-based positions in these numeric orders. Equal
numerical values retain all source and candidate IDs. Cached arithmetic is
fanned back to every ID and never merges scores.

## 5. Fixed canonical grammar and endpoint

For each anchor value `c`, define

```text
x_c = B+c
d_c = floor(N/x_c)
r_c = N-x_c*d_c
u_c = least positive inverse of x_c modulo N
k_c = (x_c*u_c-1)/N.
```

Construct `u_c` only after `gcd(x_c,N)=1`. Apply expression signs as
integers, then reduce modulo `N`.

For source anchor `c=anchor[i]`, choose `t` and `eta` from the two named
expressions. For target anchor `c'=anchor[j]`, choose `v` from its named
expression.

Compute

```text
(t+w)^B = P_B+Q_B*w,  w^2=eta
F = P_B-v*Q_B mod N
```

with the pair law

```text
(R,S)*(R2,S2)
  = (R*R2+eta*S*S2, R*S2+S*R2) mod N.
```

The literal control matrix is

```text
C = [[(t-v)/2, 1],
     [(eta-v^2)/4, (t+v)/2]] mod N.
```

An independent ordinary `2 by 2` binary power must verify

```text
(C^B)[0][0] = 2^(-B)*F mod N
```

for every replay certificate.

## 6. Exact public screen chronology

Operational caching can change cost but cannot change this logical order.
The classifier may evaluate candidate-specific relation screens only after
a raw proper endpoint. It must replay the complete registered box before it
updates a `box_unexplained_exclusive` score.

### 6.1 Registered row cleanup

1. Authenticate the public fixture and promise attestation.
2. Verify the public row conditions in Section 2.
3. Screen `gcd(B,N)`.
4. For numeric `j=-64,...,64`, screen `gcd(B+j,N)` when
   `0<B+j<N`.
5. For numeric `j=0,...,64`, put `X=B+1+j`. If `X^2-N` is a
   nonnegative square, verify the two nontrivial factors `X-Y` and `X+Y`.
6. In anchor-index order and atom order `x,d,r,u,k`, construct and screen
   every nonzero atom. A proper gcd is a cleanup factor. A saturated atom
   aborts the row.

The cleanup codes are exactly:

```text
boundary_cleanup
offset_cleanup
fermat_cleanup
atom_cleanup
atom_saturated
```

A cleanup row remains in the 1,024-row phase table but has no eligible
candidate.

### 6.2 Source invariants

For each named source, screen in this order:

```text
g_eta   = gcd(eta,N)
g_delta = gcd(t^2-eta,N)
```

A proper gcd is `source_invariant_factor`. A saturated gcd is
`source_degenerate`. Only `(g_eta,g_delta)=(1,1)` reaches source powering.

For every clean source, screen `gcd(Q_m(t,eta),N)` for numeric
`m=2,...,16`. A proper gcd is `source_order_factor`. A saturated gcd is
`global_source_order_m`. Every candidate using such a source is a
registered-box decoy.

After computing `(P_B,Q_B)`, screen in this order:

```text
g_Q = gcd(Q_B,N)
g_P = gcd(P_B,N).
```

A proper `g_Q` is `powered_collision_factor`. A proper `g_P` is
`half_order_factor`. Either makes every target under the source direct. A
global zero is recorded and checked during replay.

### 6.3 Target invariant and raw endpoint

For each candidate under a clean source, screen

```text
g_H = gcd(v^2-eta,N).
```

A proper gcd is `target_invariant_factor`. A saturated gcd is
`target_degenerate`. Only `g_H=1` reaches the endpoint.

Then compute `g_F=gcd(F,N)`. Its outcomes are:

```text
1          no_hit
1<g_F<N    raw_proper_hit
N          saturated_hit
```

### 6.4 Complete registered relation box for a raw hit

The box constant is exactly `K=16`.

Orbit offsets are checked in numeric order

```text
-16,-15,...,-1,1,...,15,16.
```

For positive `e`, screen

```text
O_e = P_e(t,eta)-v*Q_e(t,eta).
```

For negative `e`, screen

```text
O_e = P_abs(e)(t,eta)+v*Q_abs(e)(t,eta).
```

Target torsion is checked for numeric `m=2,...,16` by screening

```text
Q_m(v,eta).
```

Mixed phases are checked in nested numeric order:

```text
for e=-16,...,16:
    for m=2,...,16:
```

Let `(R,S)=(P_m(v,eta),Q_m(v,eta))`. Let `(P,Q)` represent `z^(e*m)`,
using `(P_k,Q_k)` for a nonnegative exponent and `(P_k,-Q_k)` for
exponent `-k`. Screen

```text
Z_(e,m) = R*Q-S*P mod N.
```

A proper relation gcd is a direct registered-box factor. A saturated
relation is a global registered-box decoy. For a saturated mixed relation
and a raw endpoint, screen

```text
gcd(Q_(m*(B-e))(t,eta),N).
```

Here `B>16`, so the exponent is positive. A proper gcd is the prior order
factor. A saturated gcd is `registered_phase_split`. A gcd of one is an
algebraic inconsistency and aborts the packet.

The cumulative number of these large mixed-order checks across both phases
cannot exceed

```text
MAX_GLOBAL_ORDER_CHECKS_TOTAL = 131072.
```

Crossing the cap aborts. It never drops a relation or changes the box.

### 6.5 Finite evidence class

A raw proper hit is `box_unexplained_exclusive` only when:

1. its row, source, and target are clean;
2. every registered source, orbit, target-torsion, mixed-phase, powered
   collision, and half-order screen has no proper gcd;
3. no registered relation is globally saturated;
4. the mixed-order consistency checks pass; and
5. public and labelled replay pass.

No output token says `free`, `exhaustive`, or `relation_free`.

## 7. ExactTape256 controls

Uniform controls never enter candidate scores, selection, or the lead gate.

### 7.1 Tape sample space and files

Each phase has one raw binary tape file. It has no header and has exactly

```text
1024*900*2*3*32 = 176947200 bytes.
```

The two phase payloads are independent uniform byte strings in the declared
sample space. This is equivalent to 11,059,200 independent uniform 256-bit
blocks across the complete packet. The total tape size is exactly
353,894,400 bytes.

The tape draw is independent of both fixture seeds, every generated factor,
every public modulus, and every grammar value.

Both tape byte lengths and SHA-256 hashes are committed before discovery.
The discovery process can read only the discovery tape. The held-out tape
stays in the held-out private root until the sealed selection is
authenticated.

The probability claims are with respect to this uniform tape space. The
packet records entropy provenance but does not claim that observed bytes can
prove their physical origin.

### 7.2 Exact row IDs and counters

Within each phase, size index is `0,1,2,3` in the displayed size order.
Cohort offsets within a 256-row size block are:

```text
random_balanced             0
wide_gap                   96
four_capacity_at_most_32  160
consecutive_prime          224
```

For cohort-local ordinal `k`, define

```text
row_ordinal = 256*size_index + cohort_offset + k.
```

It is in `0,...,1023`. The public row ID is exactly `dRRRR` for discovery
or `hRRRR` for held-out, where `RRRR` is the four-digit zero-padded row
ordinal.

For `source_ordinal=0,...,899`, `control_index=0,1`, and
`attempt=0,1,2`, the phase-local block index is

```text
block_index = (((row_ordinal*900 + source_ordinal)*2
                + control_index)*3 + attempt).
```

The byte offset is exactly `32*block_index`. This mapping is injective and
covers every 32-byte block once. A block is interpreted as one unsigned
big-endian 256-bit integer. There is no mutable stream state.

### 7.3 Draw and attempt semantics

For each clean named source and each control index, inspect attempts
`0,1,2` in order. Put `M=N*N` and

```text
L = floor(2^256/M)*M.
```

For the attempt block `R`:

1. If `R>=L`, reject this attempt.
2. Otherwise put `U=R mod M`, `V=floor(U/N)`, and `W=U mod N`.
3. Compute `g_vector=gcd(V,W,N)` and
   `g_target=gcd(V^2-eta*W^2,N)`.
4. Here `gcd(V,W,N)` means `gcd(gcd(V,W),N)`. Record every proper gcd as a
   control-only cleanup event.
5. Accept exactly when `(g_vector,g_target)=(1,1)`.
6. On acceptance, compute `F_uniform=W*P_B-V*Q_B mod N` and stop.

Every inspected attempt consumes exactly its assigned block. An uninspected
later block remains unused. A modulo rejection and a target rejection each
consume one attempt. There is no scalar redraw, whole-pair redraw, counter
shift, fourth attempt, or substitute generator.

Three failures give `control_shortfall` and abort the phase before any score
or selection is sealed. Conditional on phase success, the controls are
independent and exactly projective-uniform as proved in the D02 algebra.

## 8. Elementary high-order diagnostic

The diagnostic runs on public row ordinals

```text
256*i + 0, 256*i + 1, 256*i + 2, 256*i + 3
```

for size index `i=0,1,2,3` in each phase. These are exactly the rows with
`diagnostic=1` in the public fixture. The classifier does not read a cohort
label to choose them.

Put

```text
D0 = bitlength(N)
A0 = D0^2+D0.
```

Scan bases `a=2,...,A0` in numeric order. Screen `gcd(a,N)`. For each
unit base, compute incremental powers and screen `gcd(a^e-1,N)` for every
numeric `e=1,...,D0`.

```text
proper gcd     diagnostic_factor
saturated gcd  reject base
all gcds one   retain first base
cap exhausted  diagnostic_shortfall
```

For a retained `z`, both local orders exceed `D0`. Construct

```text
eta=1
t=(z+1)/(z-1) mod N
```

and evaluate the 90 named target expressions. These outcomes never enter
ranking or the gate.

## 9. Deterministic bounded cohort generator

### 9.1 Sizes and counts

Discovery factor sizes are exactly

```text
18,24,30,36
```

Held-out factor sizes are exactly

```text
40,46,52,56
```

At each size the generator requests, in this order:

```text
random_balanced                         96 rows
wide_gap                                64 rows
four_capacity_at_most_32                64 rows
consecutive_prime                       32 rows
```

Each phase has 1,024 rows. Every `N` is distinct across both phases.

The extra predicates are exactly:

```text
wide_gap:
    q-p >= ceil(p/4)

four_capacity_at_most_32:
    max(gcd(p-1,q-1),gcd(p-1,q+1),
        gcd(p+1,q-1),gcd(p+1,q+1)) <= 32

consecutive_prime:
    q is the least prime greater than p
```

### 9.2 Deterministic candidate words

The generator is deterministic conditional on a 32-byte phase seed. It
makes no uniformity or independence claim about its candidate words.

For a zero-based 64-bit word counter, form these bytes in order:

```text
ASCII bytes: F279-D02-fixture-word
one NUL byte
32 seed bytes
8-byte unsigned big-endian counter
```

Compute SHA-256 of the exact bytes. The candidate word is the unsigned
big-endian integer in digest bytes `0,...,7`. Increment the counter after
every requested word. Counter wrap aborts.

The discovery seed is the 32 bytes encoded by this exact lowercase hex:

```text
f279d15c0a1b2c3df279d15c0a1b2c3df279d15c0a1b2c3df279d15c0a1b2c3d
```

Before either fixture is generated, a separate 32-byte held-out seed is
placed in the held-out private root. Only this commitment is public before
held-out completion:

```text
SHA256(ASCII "F279-D02-heldout-seed" || NUL || heldout_seed_bytes).
```

The held-out seed is not compiled into any executable, passed to discovery,
or revealed before the selection hash is sealed. It is published after
held-out replay.

Fixture creation generates discovery first and held-out second. Each phase
word counter starts at zero. The duplicate-`N` set persists across the phase
boundary. A shortfall in either phase aborts creation of the complete fixture
pair.

### 9.3 Prime test

A factor candidate consumes one candidate word, masks it to `b` bits, sets
bits `b-1` and `0`, and tests the resulting odd integer. Primality for all
at-most-56-bit candidates uses deterministic Miller-Rabin with bases

```text
2,325,9375,28178,450775,9780504,1795265022.
```

The implementation first handles `n<4`, even `n`, and equality with a test
base. It writes `n-1=d*2^s` with odd `d` and performs the standard strong
probable-prime test after reducing each base modulo `n`.

Precisely, `2` and `3` are prime; values below `2` and even values above `2`
are composite. For each listed base `a`, put `a=a mod n`. If `a=0`, that
base passes. Otherwise compute `x=a^d mod n`. The base passes if `x=1` or
`x=n-1`. If not, square `x` modulo `n` for numeric indices
`1,...,s-1`; the base passes at its first `x=n-1`. If no such value occurs,
the candidate is composite. A candidate is prime only if every listed base
passes.

### 9.4 One unambiguous row-attempt chronology

Each requested row has row attempts `0,...,4095`. The phase word counter is
continuous across sizes, cohorts, rows, attempts, and failed searches.

For the first three cohorts, one row attempt is exactly:

1. Request at most 65,536 candidate words for `p`. Retain the first prime.
   If none occurs, the row attempt fails.
2. With that fixed `p`, request at most 65,536 candidate words for `q`.
   Retain the first candidate that is prime and simultaneously satisfies
   exact bit length, `p<q<2p`, and the active cohort predicate.
3. If no qualifying `q` occurs, the row attempt fails. Do not keep `p` and
   start a second `q` search.
4. Form `N=pq`. If `N` duplicates any prior row in either phase, the row
   attempt fails.
5. Otherwise accept the row.

For `random_balanced`, the active extra cohort predicate in step 2 is the
constant `true`.

For `consecutive_prime`, one row attempt is exactly:

1. Generate `p` by the same bounded 65,536-word prime search.
2. Test `p+2*k` for numeric `k=1,...,65536`, without consuming candidate
   words. Retain the first prime as `q`.
3. If there is no prime in the walk, or if the retained `q` has the wrong
   bit length, violates `q<2p`, or makes a duplicate `N`, the row attempt
   fails.
4. Otherwise accept the row. Since every smaller odd integer above `p` was
   tested, `q` is the least prime greater than `p`.

Failure of all 4,096 row attempts produces

```text
fixture_shortfall:<phase>:<size>:<cohort>:<cohort_row_ordinal>
```

and aborts fixture creation. It never shrinks, replaces, or relabels a
cohort. Thus the generator is a total function from seeds to either the
exact fixtures or one canonical shortfall code.

## 10. Discovery, held-out, and private-label firewall

The generator and promise validator create and authenticate both phases,
both private-label fixtures, both public-N fixtures, and both control tapes
before discovery selection. The held-out seed, fixtures, tape, and generator
state then remain in the held-out private root.

The implementation packet must contain separate binaries:

```text
f279_fixture_label
f279_public
f279_runner
```

`f279_public` contains no fixture generator, phase seed, private-fixture
parser, primality generator, cohort predicate, or label-join code.

The runtime uses three distinct numeric UIDs recorded in the frozen
containment manifest: runner, public classifier, and label process. The
private root is owned by the label UID with mode `0700`. The public UID has
no supplementary groups. Before `execve` of `f279_public`, the runner:

1. opens only the authenticated public-N fixture, the permitted phase tape,
   the sealed selection when applicable, and a new public output root;
2. closes every other file descriptor except standard error;
3. clears the environment except fixed locale `LC_ALL=C`;
4. changes directory to an empty public scratch directory;
5. drops permanently to the public numeric UID; and
6. applies the frozen resource limits and network-deny rule.

The public process receives descriptor numbers, not private paths. A runtime
negative probe must show that the public UID cannot stat, list, or open the
private-label or held-out roots. Any failed drop, unexpected descriptor,
readable private path, network capability, or probe mismatch aborts. There
is no same-UID, container, shell-only, or permissions-convention fallback.

The exact chronology is:

1. The label process validates and seals both fixture pairs and commitments.
2. The label process releases only the discovery public-N fixture and
   discovery tape into a read-only runner-owned release root. The held-out
   public-N fixture and tape remain in a label-owned `0700` sealed root.
3. The discovery public process classifies discovery rows and seals its
   rows, scores, certificates, controls, summary, and selection bytes.
4. Only after the runner authenticates the selection hash may the discovery
   label process read discovery `p,q` and append label records.
5. The label process then releases only the authenticated held-out public-N
   fixture and held-out tape into a new read-only runner-owned release root.
   The held-out private labels and seed remain label-only.
6. The held-out public process receives the released held-out public-N
   fixture, tape, and sealed selection. It classifies and seals public
   outputs without labels.
7. Only after held-out public sealing may the held-out label process join
   `p,q`, local characters, hit orientation, and cohort labels.
8. Public exhaustive replay runs without labels. Labelled replay and the
   cohort-dependent lead gate run only on already sealed public bytes.

Labels can verify or veto a record. They cannot add a hit, change a public
classification, rerank a candidate, replace selection, or repair bytes.

This is an executable input firewall, not information-theoretic secrecy.
Small labelled factors are mathematically recoverable from `N`. The later
static audit must therefore also prove that `f279_public` implements only the
registered public operations and contains no trial-division, fixture-
reconstruction, or private-label recovery path.

## 11. Factor-blind selection and finite held-out gate

Discovery ranks all 25,000 candidate IDs by this numeric tuple:

1. `box_unexplained_exclusive` rows, descending;
2. public scales with such a row, descending;
3. minimum such count over the four public scales, descending;
4. all clean raw proper endpoint rows, descending; and
5. candidate numeric order from Section 4, ascending.

The public scale is

```text
b_pub = ceil(bitlength(N)/2).
```

Discovery writes exactly the first 128 ranked candidates. Held-out verifies
the complete candidate IDs, ranks `1,...,128`, score ranges, tuple order,
exact bytes, and selection SHA-256. It never reranks or substitutes.

Held-out evaluates all 25,000 candidates. Only a selected candidate can pass
the gate. A finite D02 lead requires:

1. at least eight held-out `box_unexplained_exclusive` rows;
2. hits at three or more held-out public scales;
3. a hit at public scale 52 or 56;
4. after the public outputs are sealed, at least one labelled hit in each of
   `wide_gap` and `four_capacity_at_most_32`;
5. complete public and labelled replay; and
6. no registered D02-box cleanup or decoy for any gate hit.

The gate says nothing about an orbit, torsion, phase, or relation outside
the registered D02 box.

## 12. Exact artifact schemas and serialization

The successful packet has exactly these output files:

```text
F279-D02.discovery.rows.tsv
F279-D02.discovery.scores.tsv
F279-D02.discovery.selection.tsv
F279-D02.discovery.certificates.tsv
F279-D02.discovery.summary.json
F279-D02.discovery.controls.json
F279-D02.discovery.labels.tsv
F279-D02.heldout.rows.tsv
F279-D02.heldout.scores.tsv
F279-D02.heldout.lead.tsv
F279-D02.heldout.certificates.tsv
F279-D02.heldout.summary.json
F279-D02.heldout.controls.json
F279-D02.heldout.labels.tsv
F279-D02.preflight.json
F279-D02.replay.json
```

Every mode refuses to overwrite any path. A failure packet is not a
successful packet and cannot pass the gate.

### 12.1 TSV headers

The exact rows header is

```text
row_id	B	b_pub	status	cleanup_code	cleanup_gcd	eligible_sources	eligible_candidates	raw_hits	box_unexplained_hits	control_status
```

The exact scores header is

```text
candidate_id	box_unexplained_rows	scale_count	min_scale_count	proper_endpoint_rows
```

The exact selection header is

```text
rank	candidate_id	box_unexplained_rows	scale_count	min_scale_count	proper_endpoint_rows
```

The exact lead header is

```text
rank	candidate_id	box_unexplained_rows	scale_count	high_scale_hit	wide_gap_hit	four_capacity_hit	replay_ok	lead
```

The exact certificate header is

```text
certificate_id	phase	row_id	candidate_rank	candidate_id	N	B	source_anchor	target_anchor	sx	sd	sr	su	sk	tx	td	tr	tu	tk	t	eta	v	delta4	H4	g_eta	g_delta	g_H	P_B	Q_B	F	g_P	g_Q	g_F	saturated_mask	first_direct_event	global_order_checks	pair_muls	mod_muls	gcds	classification	reason
```

The source atom columns use the source anchor. The target atom columns use
the target anchor, even when both anchors are equal. `delta4=t^2-eta mod N`
and `H4=v^2-eta mod N`. Atom columns contain the five nonnegative canonical
integer atoms before an expression sign or modular reduction.

The exact label header is

```text
certificate_id	row_id	p	q	cohort	hit_factor	chi_p	chi_q	p_residual_ok	q_residual_ok	matrix_ok	label_status
```

`certificate_id` is exactly

```text
<phase-letter><four-digit-row-ordinal>-<candidate_id>
```

where the phase letter is `d` or `h`. Certificate records use phase order,
row numeric order, then candidate numeric order. Label records use the same
order. Scores use candidate numeric order. Selection and lead use rank
numeric order.

Every TSV field whose name ends in `_ok`, plus `high_scale_hit`,
`wide_gap_hit`, `four_capacity_hit`, and `lead`, is exactly `0` or `1`.
`chi_p` and `chi_q` are exactly `-1` or `1`. `label_status` is exactly
`pass` or `fail`.

The `phase` TSV field is exactly `discovery` or `heldout`. The row `status`
field is exactly `eligible` or `cleanup`. The row `control_status` field is
exactly `pass`, `not_run`, or `shortfall`; a successful packet contains no
`shortfall`. `cleanup_code` is `-` or one token from Section 6.1.

The certificate `classification` field is exactly one of:

```text
box_unexplained_exclusive
registered_global_source_order
registered_global_powered_collision
registered_global_half_order
registered_global_orbit
registered_global_target_torsion
registered_global_mixed_phase
registered_phase_split
direct_registered_orbit
direct_registered_target_torsion
direct_registered_mixed_phase
```

The `reason` field is the same token as `classification`, except a direct
classification appends one colon and its canonical `first_direct_event`.
No other status, classification, reason, event, or cleanup token is valid.

If more than one registered relation is saturated, the first one in Section
6 chronology chooses the global classification and every saturation remains
set in the mask. `registered_phase_split` takes priority over
`registered_global_mixed_phase` for the same mixed relation. A proper
relation takes priority over every global classification and the first proper
event in chronology determines the direct classification.

### 12.2 Screen mask and event tokens

The registered saturation mask has 559 meaningful bits and one zero padding
bit. It is serialized as exactly 140 lowercase hexadecimal digits. Bit `i`
is the bit with value `0x80>>(i mod 8)` in byte `floor(i/8)`.

The bit assignment is:

```text
0..14    source order m=2..16
15..46   orbit e=-16..-1,1..16
47..61   target torsion m=2..16
62..556  mixed phase, e outer -16..16, m inner 2..16
557      Q_B
558      P_B
559      padding, always zero
```

`first_direct_event` is `-` or one exact token:

```text
soMM
orSEE
ttMM
mxSEE-MM
qb
pb
```

`MM` is two digits. `SEE` is `00` or a sign followed by two digits, such as
`-16` or `+04`. The first event is determined by the chronology in Section
6. A box-unexplained certificate has an all-zero mask and `-` first event.

### 12.3 Restricted canonical JSON

Summary JSON keys occur in this exact order:

```text
version,phase,public_fixture_sha256,selection_sha256,row_count,
cleanup_rows,eligible_rows,source_slots,candidate_slots,raw_hits,
box_unexplained_hits,global_order_checks,operation_counts,output_bytes,
endpoint_checksum
```

`selection_sha256` is `null` for held-out summary. `operation_counts` is an
object with keys in this exact order:

```text
pair_muls,mod_muls,gcds,inverses,matrix_muls,sha256_calls,tape_blocks
```

Controls JSON keys occur in this exact order:

```text
version,phase,tape_sha256,tape_bytes,potential_controls,eligible_controls,
attempts,modulo_rejections,target_rejections,proper_cleanup_events,
shortfalls,proper_hits,control_checksum
```

Preflight JSON keys occur in this exact order:

```text
version,binary_sha256,manifest_sha256,kernel_counts,kernel_ns,read_ns_per_byte,
write_ns_per_byte,projected_wall_seconds,capacity_peak_bytes,
projected_virtual_bytes,projected_output_bytes,projected_output_with_margin,
wall_pass,memory_pass,output_pass
```

Replay JSON keys occur in this exact order:

```text
version,public_fixture_auth,public_manifest_complete,score_match,
selection_match,certificate_match,public_replay_count,label_replay_count,
matrix_checks,residual_checks,failures,replay_checksum,replay_pass
```

`kernel_counts` and `kernel_ns` use the key order in Section 14.2.
`failures` is an array in phase, row, candidate, check order. A successful
replay has the empty array `[]`. Each nonempty element is one JSON string of
the exact form

```text
<phase>:<row_id>:<candidate_id-or-hyphen>:<check_code>
```

where `check_code` is exactly one of `fixture_auth`, `manifest`, `score`,
`selection`, `certificate`, `matrix`, `residual`, or `control`.

Every hash is over exact closed-file bytes. No file contains its own hash.
The runner records hashes in the next chronological manifest or summary.

### 12.4 Canonical internal checksum streams

The endpoint checksum is SHA-256 of a canonical internal TSV stream that is
hashed but not written. Its exact header is

```text
phase	row_id	candidate_id	status	F	g_F	classification
```

It has one record for every nominal candidate slot in phase, row, candidate
numeric order. Ineligible slots use their registered status and `-` for
uncomputed fields. This stream makes invalid skips part of replay.

The endpoint-stream status token is exactly one of:

```text
row_cleanup
source_ineligible
target_ineligible
no_hit
raw_proper_hit
saturated_hit
```

Only `raw_proper_hit` has a non-absent classification.

The control checksum is SHA-256 of another hashed, unwritten TSV stream. Its
exact header is

```text
phase	row_id	source_id	control_index	attempt	outcome	V	W	g_vector	g_target	F_uniform	g_F_uniform
```

It has one record for every inspected attempt in row, source, control, attempt
order. The outcome token is exactly `modulo_reject`, `target_reject`, or
`accept`. Fields not computed for an outcome are `-`. An ineligible source
has no control record; eligibility is fixed by the public endpoint stream and
phase summary. Replay reconstructs both streams byte-for-byte.

## 13. Replay completeness and label chronology

The public replay does not trust a certificate-only subset. It reads the
authenticated public fixtures, tapes, exact candidate grammar, public phase
outputs, and sealed selection. It independently enumerates all 51,200,000
nominal candidate slots and reconstructs:

1. every cleanup and eligible source;
2. every clean endpoint and raw proper-hit manifest;
3. every complete registered-box classification for a raw hit;
4. all 25,000 score rows in both phases;
5. the exact discovery ranking and selection bytes;
6. every certificate row and saturation mask; and
7. every uniform control and control checksum.

Any omitted, added, duplicated, reordered, or altered hit fails replay.

For every raw proper endpoint, public replay also recomputes the literal
matrix power independently. Only after the public manifest matches can the
label process read the private fixture. It then verifies:

1. `N=pq`, factor order, primality, balance, factor size, and cohort;
2. `g_F` is exactly `p` or `q`;
3. `chi_p` and `chi_q` from Euler's criterion;
4. both residual equations in division-free pair form; and
5. the matrix-control equality.

The label process writes one label row per public certificate. It cannot
change the public certificate. A failed label or replay check makes the
packet ineligible for a lead.

## 14. Exact work bounds and conservative preflight

Fixture and tape creation occur before classification preflight. They use one
low-priority core, stream all bytes, have a fixed 3,600-second deadline and
1 GiB virtual-memory limit, and abort without evidence on any deadline,
entropy, disk, or fixture shortfall. Classification preflight starts only
after all input bytes and commitments exist. It cannot use partial fixture
generation as a timing sample.

### 14.1 Hard workload caps

The complete packet has these fixed maxima before invalid skips:

```text
total rows                                  2048
named source slots                         1843200
primary candidate endpoint slots          51200000
potential accepted controls                3686400
assigned control attempts                 11059200
raw proper hits across both phases          131072
large global mixed-order checks              131072
public replay endpoint slots              51200000
public replay control attempts            11059200
labelled certificate replays                131072
```

The cumulative caps are carried from discovery into held-out. Crossing a
cap aborts before writing the next record. The packet never samples,
truncates, replaces, or silently omits work.

### 14.2 Exact benchmark kernels and counts

After static implementation PASS and compilation, the frozen binary runs a
single-core capacity benchmark. It uses 112-bit odd moduli, exponent
`2^56-1` for source and matrix powers, exponent `16*(2^56-1+16)` for the
large order kernel, consecutive Fibonacci operands below `2^112` for gcd,
and maximum-width canonical records. Every kernel updates a volatile
checksum that is emitted.

Each kernel runs 4,096 iterations in each of seven trials. For kernel `k`,
`kernel_ns[k]` is the ceiling of the maximum trial elapsed nanoseconds
divided by 4,096. No warm-up trial is discarded. The key order and projected
counts are exactly:

```text
source_power       3686400
candidate_endpoint 102400000
control_attempt    22118400
control_endpoint    7372800
registered_decoy     262144
global_order          262144
matrix_replay         262144
label_residual        131072
certificate_serialize 131072
label_serialize       131072
```

The doubled source, endpoint, control, decoy, and order counts include
primary evaluation plus exhaustive public replay. `registered_decoy` runs
all 32 orbit, 15 target-torsion, and 495 mixed determinants and their gcds.
`source_power` includes source invariants, 15 source-order screens, binary
pair power, and `P_B,Q_B` gcds. `candidate_endpoint` includes the target
invariant, endpoint expression, gcd, and score update.

The I/O benchmark reads and hashes one 64 MiB file and writes, closes,
`fsync`s, reopens, and hashes one 64 MiB file on the actual packet
filesystem. It runs three trials. `read_ns_per_byte` and
`write_ns_per_byte` are the ceilings from the slowest trials. Temporary
benchmark bytes are outside every evidence path and are removed after their
hashes are recorded.

The serialization kernels create maximum-width records but perform no file
I/O. File I/O is charged separately below.

Define

```text
tape_read_bytes = 5*353894400 = 1769472000
artifact_read_bytes = 3*274026496 = 822079488
output_bound_bytes = 274026496
```

The five complete tape-read budgets are commitment hashing, primary phase
authentication, primary control reads, replay authentication, and replay
control reads. The three artifact-read budgets are public replay, label join,
and final runner authentication.

Define the projected work by

```text
work_ns = sum(kernel_count[k]*kernel_ns[k])
        + (tape_read_bytes+artifact_read_bytes)*read_ns_per_byte
        + output_bound_bytes*write_ns_per_byte

projected_wall_seconds
    = 600 + ceil(2*work_ns/1000000000).
```

The projection gives no parallel speedup credit. The factor `2` is the
fixed timing margin. The 600 seconds cover process launch, fixture parsing,
hashing small artifacts, close/fsync boundaries, and runner checks.

The wall gate is exactly

```text
projected_wall_seconds <= 14400.
```

No measured hit rate, private label, cohort outcome, or optimistic thread
scaling enters the formula.

### 14.3 Exact output projection

Every successful serializer enforces these inclusive record caps, including
the final LF:

```text
certificate record    1536 bytes
label record            384 bytes
score record            256 bytes
row record              512 bytes
selection/lead record   256 bytes
each JSON file      1048576 bytes
each TSV header         4096 bytes
```

There are at most 131,072 certificate and label records, 50,000 score
records, 2,048 row records, 256 selection-plus-lead records, eight JSON
files, and sixteen TSV headers. Therefore

```text
output_bound_bytes
  = 131072*1536
  + 131072*384
  + 50000*256
  + 2048*512
  + 256*256
  + 8*1048576
  + 16*4096
  = 274026496.

projected_output_with_margin
  = ceil(5*output_bound_bytes/4)
  = 342533120.
```

The projection passes only because `342533120 < 536870912`. The hard
aggregate output cap remains exactly 512 MiB (`536870912` bytes). The
runner checks projected bytes before opening evidence files and actual bytes
before every extension.

### 14.4 Memory projection

The implementation must stream the control tape with `pread`; it cannot
map a tape file. It must stream certificates in phase-row-candidate order.
At most four worker row buffers, the complete 25,000-candidate score table,
fixed queues, replay state, and one 1 MiB I/O buffer can be live.

The capacity benchmark allocates and touches every maximum-capacity object
with the exact production types, fills four rows with 25,000 maximum-width
certificate candidates, runs the stable merge path, and records peak virtual
bytes from the operating system. Define

```text
projected_virtual_bytes
    = ceil(5*capacity_peak_bytes/4).
```

The memory gate is exactly

```text
projected_virtual_bytes <= 4294967296.
```

No estimate can reduce a workload. Failure of any wall, memory, or output
gate kills D02 for that frozen implementation.

## 15. Fixed runtime resource and containment contract

The runtime contract is part of the later static audit. It is not selected
after benchmark results.

```text
worker threads <= 4
nice level = 15
RLIMIT_CORE = 0
RLIMIT_AS = 4294967296
RLIMIT_FSIZE = 536870912 for every individual evidence file
shared hard deadline = 14400 seconds
one packet lock
one audited process group
network denied
distinct runner/public/label numeric UIDs
private roots mode 0700 and label-owned
```

Before any future benchmark or run, the runner records CPU count, load,
available memory, swap, free disk, and competing packet processes. It
requires at least 6 GiB available memory and 2 GiB free disk, no existing
packet lock, and one-minute load below half the logical CPU count. Failure
aborts. It does not request a containment decision or substitute another
mechanism.

The local 16 GiB Mac is not a production host. A future benchmark there is
limited to one low-priority core after the same live checks. D02 authorizes
no such benchmark in its current theory state.

## 16. Interpretation

A lead means only that one frozen syntax passed the finite held-out D02 gate
relative to the registered screen box. It requires a new algebraic analysis
before promotion.

A null means only that no sealed selected syntax passed that finite gate.
It does not close other target sections, expression grammars, relation
boxes, higher modes, semilinear actions, or adaptive constructions.

A fixture shortfall, control shortfall, replay failure, resource failure,
containment failure, or cap abort is not mathematical evidence. No result
from a failed packet can be selected or promoted.

This D02 pair must now be released unchanged for a fresh no-context theory
audit. Its authors do not grant it a PASS by writing it.
