# F265-D06 draft preregistration: resource-closed mixed cubic-row bank

## Status and resolved predecessor

This is an unfrozen preregistration draft. It has not passed a hostile theory
audit. No D06 C++ source, runner, manifest, compilation, local preflight,
remote execution, or production cohort exists or is authorized.

D06 preserves every D05 clause not replaced below. The exact imports are:

| imported draft | SHA-256 |
|---|---|
| `D05_DRAFT_ALGEBRA.md` | `e3cbefeb597f263501d327f15f9dd4c7b78ee37d37178135ab1c0a5ff73e9fd3` |
| `D05_DRAFT_PREREGISTRATION.md` | `a62dcb0f7d501778ef1f6092468d38a6ee15c794ec5b609bf145a3d7bf345a35` |

The normative draft is the two imported bytes plus this file and
`D06_DRAFT_ALGEBRA.md`. In imported prose, the complete token `D05` names the
proposed packet and is rebound to `D06`. No other implicit substitution is
allowed. This file replaces the D05 passages about label quantifiers,
factor-event retention, P66 fixtures, generation projection, diagnostic
fixture and ordering, relation-certificate staging, memory accounting, and
the runtime formula. All other seeds, source rows, curve domains, cohorts,
bank grammar, operation chronology, caps, output categories, mathematical
verification rules, and novelty boundaries remain unchanged.

A future standalone source packet must materialize this composite contract,
authenticate all four draft bytes, and pass a fresh byte-level review. This
amendment is not source authorization.

## 1. New and retained constants

The D05 constants remain, including

`ROW_BITS_MAX=361`, `ROWS_MAX=320`, `RESIDUAL_ROWS_MAX=64`,
`SPLITS_MAX=20000`, `REFINEMENT_GCD_MAX=1000000`,
`BLOCKS_MAX=4096`, and `EXPONENT_CELLS_MAX=262144`.

D06 adds these literal constants:

| constant | value | scope |
|---|---:|---|
| `SPARSE_EXPONENT_ENTRIES_MAX` | 262,144 | one P66 decoder |
| `CORPUS_CANDIDATE_ITERATIONS_MAX` | 16,777,216 | one complete two-split corpus replay |
| `CORPUS_PAIR_RETRIES_MAX` | 98,304 | one complete two-split corpus replay |
| `FACTOR_EVENTS_PER_BANK_MAX` | 4,096 | one intended bank |
| `FACTOR_EVENTS_PACKET_MAX` | 3,145,728 | 768 banks times 4,096 |
| `RELATION_CERT_STAGE_COUNT_MAX` | 64 | one active worker bank |
| `RELATION_CERT_BYTES_MAX` | 65,536 | one rendered certificate |
| `RELATION_CERT_STAGE_PAYLOAD_MAX` | 4,194,304 | one active worker bank |
| `DIAGNOSTIC_NO_ROW` | 65,535 | unsigned 16-bit row sentinel |
| `DIAGNOSTIC_PAIR` | 0 | diagnostic task kind |
| `DIAGNOSTIC_ANCHORED_THIRD` | 1 | diagnostic task kind |
| `PREDICATE_FALSE` | 0 | diagnostic tri-state |
| `PREDICATE_TRUE` | 1 | diagnostic tri-state |
| `PREDICATE_NOT_APPLICABLE` | 2 | diagnostic tri-state |

The corpus candidate cap is deliberately much smaller than the sum of the
inner per-request caps. Every entered iteration of `random_prime`, whether
ordinary or safe, and every entered iteration of `next_prime_same_bits`
increments the one replay-wide counter before candidate work. Crossing the
cap aborts that complete corpus replay with
`RESOURCE_REJECT_CORPUS_CANDIDATE_CAP`. It is not a shortfall that can be
excluded from a projection denominator. The retry counter increments on
entry to every `make_case` retry. Its static maximum is

`2 splits * 8 sizes * 3 shapes * 16 indices * 128 = 98,304`.

The two production split invocations each replay the full two-split order.
The runtime projection therefore charges two complete candidate caps and two
complete retry caps. The cap is fixed before any cohort execution. Exceeding
it yields no held-out label.

The future lineage table changes `random_prime`, `next_prime_same_bits`,
`make_case`, `make_corpus`, and `record_factor` from D05's proposed `EXACT`
status to `DERIVED`. Their only allowed semantic changes are the counters,
caps, sticky factor journal, and explicit failures in this document. Every
other D05 `EXACT` routine remains byte-exact. No source exists yet.

## 2. Factor journal and held-out labels

### 2.1 Per-bank journal

Every prescribed factor-screen gcd result `g` is classified immediately. If
`1<g<N` and `N mod g=0`, the worker calls one production
`record_factor_event` path before it can continue or throw for any later
reason. Explanatory diagnostic gcds are not factor screens and cannot enter
this journal. The path performs, in order:

1. set `observed_useful_factor=true`;
2. preserve the first overall witness and the first witness in each of the
   11 frozen D05 factor classes;
3. increment the lower-bound occurrence counter;
4. if 4,096 events have already been hashed, set
   `factor_event_overflow=true` and throw
   `RESOURCE_REJECT_FACTOR_EVENT_CAP`; otherwise
5. render and hash the canonical event line, then increment
   `factor_events_hashed`.

The canonical LF-terminated event line has these tab-separated fields:

`event_ordinal,phase_ordinal,class_code,side,curve,row_1,row_2,mask_hex,g_hex`.

Numeric sentinels are fixed unsigned maxima for absent coordinates. `side`
is `MINUS`, `PLUS`, or `NONE`. `mask_hex` is five lowercase, zero-padded,
16-hex-digit words in original-row order, or `NONE`. `g_hex` is lowercase
without a prefix. `event_ordinal` starts at zero. The journal hashes the
literal UTF-8 bytes including tabs and LF.

The event order is the mandatory D05 operation chronology, then loop order
inside a phase. A worker maintains one SHA-256 state and does not retain all
event lines. The overflow attempt is not hashed, but its sticky Boolean and
the occurrence lower bound of at least 4,097 are committed. The first factor
witness is never lost.

For every intended slot, including a shortfall or rejected bank, the split
factor-summary stream contains one LF-terminated line in canonical case
order:

`split,bits,shape,index,status,observed,occurrence_lower_bound,`
`hashed_count,overflow,bank_event_sha256`.

The split SHA-256 hashes these literal lines. This two-level construction is
deterministic under parallel workers. A resource rejection cannot delete or
rewrite an earlier journal state.

### 2.2 Null and positive labels

Replace the D05 held-out null definition with this exact one.

`finite_quotient_null_signal` requires:

- zero `observed_useful_factor` flags across all 384 intended held-out slots;
- zero factor-event overflow flags across all 384 intended held-out slots;
- complete P66, low-RREF, complement, and root verification on every eligible
  held-out bank;
- `quotient_defined=true` on every eligible held-out bank;
- zero non-global quotient-complement basis images on every eligible held-out
  bank;
- at least 346 eligible held-out banks; and
- at least 12 eligible banks in every factor-size/shape cell.

Thus a verified direct, singleton, support-two, or low-basis factor anywhere
prevents null even if a later peel, decoder, output, memory, or other core cap
rejects that bank. A structural-complement factor also prevents null. A
shortfall has no invented factor event and remains governed by coverage. The
label does not claim that unexecuted screens are null.

The D05 positive label and strictness rule remain unchanged. Factor-event
counters and digests are primary counters, not diagnostics.

### 2.3 Maximum-cost factor-event fixture

Preflight constructs one maximum-width bank key, one five-word relation mask,
the 120-bit modulus

`N_factor=735592564497057472472983056100764157`

and its proper 60-bit factor `g_factor=933956397855941843` (the complementary
factor is `787609107005141999`). It asserts the multiplication and both
proper-factor inequalities. It then invokes the exact production
`record_factor_event` path 4,096 times. The 11 factor classes occur first in
their frozen class order, so every first-class witness branch is exercised;
the remaining events cycle through those classes. It asserts the complete
counter, first witnesses, no overflow, and an independently computed final
SHA-256. A 4,097th call in an untimed copy must set the sticky overflow and
throw the exact cap status without clearing the first witness.

Run the 4,096-event fixture eight times. Let

\[
 \rho_{\rm factor}={\max T_{\rm factor4096}\over4096}.
\]

The production projection charges
`FACTOR_EVENTS_PACKET_MAX*rho_factor`. This times rendering, the counter,
first-witness branches, and the streaming SHA hit path at the maximum
occurrence cap. No proper-factor hit path is left inside an unrelated gcd
proxy.

## 3. Cap-complete P66 decoder suite

This section replaces D05 Section 10.2. It uses the same production
refinement primitive, failed-comparison loop, terminal verifier, parity
builder, and kernel verifier. Benchmark-only state injection is unreachable
from production.

### 3.1 Long-gcd width charge

Keep the D05 Fibonacci fixture exactly: `F_520,F_521` have 360 and 361 bits.
Eight repetitions each call the production gcd 65,536 times. Define

\[
 \rho_{\rm dgcd}={\max T_{\rm dgcd65536}\over65536}.
\]

### 3.2 Full 20,000 split path

Keep the D05 near-cap split/merge fixture exactly. Each of four repetitions
executes 20,000 permitted splits, including gcd, divisions, exponent-vector
addition, overflow check, two worst-position erases, three appends, and the
4,096-block cap check. Restoration is outside each call timer but inside the
preflight wall. Let `T_split20k` be the largest repetition time.

### 3.3 Exact one-million failed-refinement loop

Let `r_t` be the `t`-th rational prime, starting with `r_0=2`, for
`0<=t<4096`. Put

\[
 B_t=r_t^{e_t},\qquad
 e_t=\max\{e:r_t^e<2^{360}\}.
\]

Assert that all 4,096 operands are pairwise coprime and have between 344 and
360 bits. Inject them into a 4,096-live-block production container. Invoke
the exact production failed-refinement scan over the first 1,000,000 pairs
in lexicographic index order. Every comparison must return gcd one. The timed
loop includes iterator/index advancement, operand access, the integer gcd,
result classification, comparison-counter increment, branch, and cap check.
After exactly 1,000,000 comparisons it must report the registered cap state;
an attempted next comparison in an untimed copy must throw the cap status.

Run this fixture four times and let `T_refinefail1m` be the largest complete
loop time. An isolated gcd rate is not used for these one million failed
iterations.

### 3.4 Full dense and sparse terminal caps

Take the first 4,096 rational primes at least 4,099. Every block has the dense
64-entry exponent vector `(1,1,...,1)`. Define each of the 64 synthetic rows
as the product of all 4,096 blocks. Inject this already-refined state into the
exact terminal verifier and assert:

- exactly 4,096 final blocks;
- exactly 262,144 scanned dense exponent cells;
- exactly 262,144 nonzero sparse exponent entries;
- pairwise block coprimality and exact reconstruction of all 64 rows;
- parity rank one and kernel dimension 63;
- verification of every returned parity equation; and
- an exact positive square root for the first canonical support-two kernel
  vector.

The fixture deliberately exceeds the production row-total bit bound. It is a
cap and cost fixture, not source evidence. It reaches the literal sparse cap,
not merely the dense-cell cap. Run it four times and let
`T_terminal_sparse4096` be the largest wall time.

### 3.5 Maximum basis fixture and charge

Keep the D05 64-square-row fixture and its assertions. Let `T_square64` be
the largest of four repetitions.

The registered per-bank decoder charge is

\[
 \rho_{\rm decoder}=
 T_{\rm split20k}+T_{\rm refinefail1m}
 +T_{\rm terminal\_sparse4096}+T_{\rm square64}
 +\rho_{\rm dgcd}\binom{4096}{2}.
\]

The terminal fixture already executes its full pairwise-coprimality scan.
The last term deliberately charges that scan a second time at the
production-width long-Euclid rate. The failed-refinement fixture, rather than
`rho_dgcd`, charges all one million refinement-loop iterations. This suite
exercises every P66 count cap, including the independent sparse-entry cap.

## 4. Generation cap fixtures and projection

The D05 96-case generation sample remains audit output only. Its four cases
per cell cannot enter the runtime projection.

### 4.1 Candidate-iteration envelopes

Use the fixed safe prime

`p_safe=933956397855941843`

and its prime Sophie Germain half

`q_safe=466978198927970921`.

The exact imported `prime64` must accept both. Use three benchmark-only
drivers around the exact production primitives:

- `ORDINARY` executes `Rng.next`, the 60-bit ordinary mask, range work,
  `prime64(p_safe)`, the replay-wide counter increment and cap branch;
- `SAFE` executes `Rng.next`, both safe masks and range checks,
  `prime64(q_safe)`, `prime64(p_safe)`, the counter increment and cap branch;
  both primality calls take their full prime path; and
- `NEIGHBOR_NEXT` executes the same bound check, candidate increment by two,
  `prime64(p_safe)`, the counter increment and cap branch used by
  `next_prime_same_bits`.

Each driver executes the literal loop-control operations of its named
production candidate kind. Run 262,144 consecutive iterations of each driver
in each of eight repetitions. Let

\[
 \rho_{\rm gen\_candidate}=
 {\max_{k,r} T_{k,r,262144}\over262144},
\]

where `k` ranges over all three drivers and `r` over repetitions. Taking the
maximum gives one registered charge for every entered production candidate
iteration; no unproved timing dominance between candidate kinds is used.

### 4.2 Retry-tail envelope

Prepopulate the exact production modulus-ownership `std::set` with 768
distinct 120-bit decimal keys, including the product of
`787609107005141999` and `933956397855941843`. A `DUPLICATE` retry-tail
iteration uses those two factors and performs one extra neighbor offset draw,
the exact sort branch, `cpp_int` multiplication, decimal conversion,
ownership insertion attempt, duplicate branch, retry-counter increment, and
retry-cap check. It also executes the exact case-key `seed_key` construction,
which conservatively overcharges its once-per-case use.

An `ACCEPTED` retry-tail iteration starts from a 767-entry set, uses a unique
product, performs the same work through successful insertion, constructs and
moves the public `Case` and private `FactorLabel`, and then stops the retry.
Restoring the 767-entry set is outside the per-iteration timer but inside the
preflight wall.

Run 98,304 duplicate iterations in each of eight repetitions. Separately run
768 accepted iterations in each of eight repetitions. Let

\[
 \rho_{\rm gen\_retry}=\max\left(
 {\max T_{\rm duplicate98304}\over98304},
 {\max T_{\rm accepted768}\over768}\right).
\]

The fixtures assert set sizes, branch results, case bytes, retry counts, and
cap status. Charging the slower tail to every possible retry covers both
duplicate and accepted ownership paths.

### 4.3 Registered generation charge

One production split invocation performs one complete two-split replay. The
packet invokes it twice. Therefore

\[
 T_{\rm generation}=2\bigl(
 16{,}777{,}216\rho_{\rm gen\_candidate}
 +98{,}304\rho_{\rm gen\_retry}\bigr).
\]

This term depends only on frozen candidate and retry caps. No maximum of four
sampled cases appears in it. Candidate or retry cap failure closes production
before a held-out label.

## 5. Production-width diagnostic fixture

This section replaces D05 Section 10.4. Use the fixed 120-bit odd modulus

`N_diag=1329227995784915872903807060280344457`,

the curve coefficients `A=2`, `B=2221`, and the base point

`P=(N_diag-2,N_diag-47)`.

Generate `P,2P,...,16P` with the exact production `add_points` routine. For
row `i`, use curve ID zero, scalar index `i`, the affine coordinates
`u_i,v_i`, and

\[
 a_i=u_i^3+2u_i+2221
\]

over the integers. Assert all of the following before timing:

- `N_diag` is odd and has 120 bits;
- the discriminant gcd with `N_diag` is one;
- every denominator gcd reached by the exact addition trace is one;
- the 16 affine points are distinct and every `v_i` is a unit;
- `a_i=v_i^2 (mod N_diag)` for every row;
- every row operand has between 354 and 360 bits; and
- the SHA-256 of the 16 LF-terminated decimal lines
  `index<TAB>u<TAB>v<TAB>a`, with no header, is
  `e8a5018e7f5b7cf4659d6061a82cfaa33c999580b1a089b5e9e427dcca4315a0`.

No primality assumption is needed: the asserted discriminant and denominator
gcds are the exact public safety conditions used by the diagnostic path.

Pass eight tagged copies of this support to the exact production diagnostic
function. It must execute 960 pair tasks, 13,440 anchored-third tasks,
complete aggregates, all six index predicates, the total order in Section 6,
and the same 64-record detail cap as one maximum bank. Run it 16 times and
let `rho_diag` be the largest call time. The timed gcd operands now have the
production row width; no unstated width extrapolation is used.

## 6. Diagnostic task schema, sentinels, and ordering

Each selected basis support creates a conceptual record for every executed
task, whether or not any predicate matches.

| field | pair task | anchored-third task |
|---|---|---|
| `task_kind` | `0` | `1` |
| `curve` | actual curve | actual curve |
| `pair_row_1` | smaller original row ID | smaller anchor row ID |
| `pair_row_2` | larger original row ID | larger anchor row ID |
| `third_row` | `65535` | actual original row ID |
| `third_root` | `2` (`NOT_APPLICABLE`) | `0` or `1` |
| six index predicates | each `2` | each `0` or `1` |

`pair_row_1<pair_row_2`; an anchored third row differs from both. There are
no cross-curve tasks. Tangent, chord, and discriminant gcd classifications
are present for both kinds. The pair task does not invent a `gamma`.

The unique total key is

`(split,bits_rank,shape,index,basis_ordinal,task_kind,curve,`
`pair_row_1,pair_row_2,third_row)`.

`bits_rank` is 0 through 7 in the frozen factor-size order. Tasks are
generated, hashed, aggregated, and considered for retention in this exact
lexicographic order. Every task increments `diagnostic_tasks`; every true
predicate increments its named match counter; every complete task line
updates `diagnostic_task_sha256`. Retain the first 64 lines per bank and then
the first 8,192 per split under the same order. Record oversize omission does
not alter the task digest or aggregates.

On timeout, record the completed prefix count, prefix digest, exact next task
key, and `DIAGNOSTIC_NOT_RUN_TIMEOUT` for all remaining aggregate cells. The
prefix is never called exhaustive. Diagnostics remain post-commit and
non-gating.

## 7. Deterministic relation-certificate staging

For each bank, relation order remains

`(relation_class, five-word original-row mask)`

inside canonical bank order. During mathematical work, a worker streams the
complete relation count and digest and stages only that bank's first 64 full
certificates. Later certificates in the same bank cannot precede those 64 in
the split order, so they need no payload retention.

Each staged certificate is one contiguous rendered byte vector of at most
65,536 bytes. The stage therefore has at most

`64*65,536 = 4,194,304 bytes`

of payload, plus at most 64 KiB of fixed locator/length metadata and one
65,536-byte render buffer. All of it is allocated from the worker's counted
256 MiB arena. A worker cannot start another bank until the canonical writer
has consumed or discarded its current certificate stage.

At canonical commit, the writer takes staged certificates until the frozen
64-per-split output cap is full, writes one certificate at a time, and uses
no second 4 MiB copy. It then releases the worker stage. At most eight stages,
33,554,432 payload bytes total, can coexist. This memory is not part of the
on-disk one-bank temporary and does not change the 8,388,608-byte final
certificate category.

The per-worker arena partition reserves at most 240 MiB for rows, P66,
big-integer work, and ordinary serialization; 4 MiB for certificate payload;
64 KiB for certificate metadata; 64 KiB for its render buffer; and the
remaining arena for allocator overhead and scratch. The hard 256 MiB arena
and 3.5 GiB measured process RSS gates still control. Thus the static
`8*256 MiB+512 MiB=2.5 GiB` allowance already includes, rather than omits,
the maximum 32 MiB of live certificate payloads.

## 8. Revised dynamic runtime formula

Keep the D05 real-bank `rho_orbit`, `rho_pair`, `rho_peel`, relation fixtures,
low-RREF fixtures, commit fixture, output-throughput fixture, all registered
task maxima, and final-output cap, except for the replacements above.

Use

\[
 R_{\max}=172032,\quad P_{\max}=22032384,
 \quad W_{\max}=22204416,
\]

`H_max=22,204,416`, `V_basis,max=98,304`, and
`C_final=588,251,136` bytes as in D05. The raw projection is

\[
\begin{aligned}
T_{\rm raw}={}&T_{\rm generation}
 +\rho_{\rm orbit}R_{\max}
 +\rho_{\rm pair}P_{\max}
 +\rho_{\rm peel}W_{\max}\\
&+\rho_{\rm rel1}R_{\max}
 +\rho_{\rm rel2}P_{\max}
 +\rho_{\rm lowinsert}H_{\max}\\
&+768\rho_{\rm lowfinal}
 +768\rho_{\rm decoder}
 +\rho_{\rm rel64}V_{\rm basis,max}\\
&+3{,}145{,}728\rho_{\rm factor}
 +768\max(\rho_{\rm commit},\rho_{\rm commit,real})\\
&+768\rho_{\rm diag}
 +\rho_{\rm io}C_{\rm final}.
\end{aligned}
\]

Set `T_projected=1.75*T_raw`. Production remains closed unless the D05
12,600-second projection gate, common-deadline reserve, memory gates, output
gates, and separate diagnostic inequality all pass. The old
`32*sum(gamma_c)` term is forbidden. The old isolated-gcd charge for one
million failed refinement comparisons is forbidden. Every factor-event hit
path is charged explicitly.

The complete preflight remains under 1,800 seconds. A fixture timeout or
assertion failure closes production; it cannot be replaced by a smaller
fixture after seeing timing.

## 9. Audit gate

Before source is written, a fresh no-context hostile review must reconstruct
the D05 imports and try to kill at least:

- the saturated private-primary theorem, simultaneous peel, and kernel/root
  preservation;
- support-at-most-two completeness and low-image quotient logic;
- the all-intended-bank factor-event quantifier and sticky journal through
  every rejection path;
- the event encoding, 4,096-per-bank cap, packet maximum, SHA determinism,
  and explicit maximum-hit timing charge;
- the replay-wide candidate counter, retry bound, two-invocation generation
  charge, and cap-failure semantics;
- the exact million-iteration failed-refinement fixture and the independent
  262,144-sparse-entry terminal fixture;
- the production-width elliptic diagnostic fixture and its fixed digest;
- task-kind coverage, sentinels, unique total order, timeout-prefix status,
  and post-commit noninterference;
- the 64-by-65,536-byte per-worker certificate stage and all live-memory
  arithmetic; and
- every surviving D05 output, wall, seed, corpus, firewall, and novelty
  clause.

A pass authorizes only a standalone resolved theory/preregistration draft.
It does not authorize source, freezing, compilation, preflight, or execution.
