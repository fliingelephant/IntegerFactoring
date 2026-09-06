# F279-D01 draft preregistration — canonical biased Rédei power-coset search

## Status and authority

F279-D01 is an unfrozen preregistration draft. It authorizes no source-code
creation, compilation, validation run, local production, remote access, or
ledger edit.

The proposed experiment is a freeze-first C++17 symbolic and numerical
search in the clean two-mode lane left open by P228/F278. Its exact question
is:

> Does one fixed factor-blind bank of canonical integer source-target pairs
> produce a repeated exclusive Rédei power-coset hit after every public input
> gcd, near-square, orbit, bounded-torsion, and phase/Miller explanation is
> removed?

A finite lead is discovery evidence only. A finite null is a null for this
grammar only. Neither result proves an all-input factoring statement or a
lower bound.

The normative algebra for a future frozen packet is `DRAFT_ALGEBRA.md`.
P228/F278 remains the closest promoted boundary. No theorem is imported by
reference into the algebra identities.

## 1. Promised rows and public notation

Every labelled research row satisfies

```text
N = p*q
p and q are distinct odd primes
p < q < 2*p
B = floor(sqrt(N))
n = bitlength(N)
```

The factors are generator labels. They are not inputs to a candidate,
candidate order, public screen, source construction, target construction,
selection score, or stopping rule.

The executable must recompute `B` with an exact integer square root and
verify

```text
B*B <= N < (B+1)*(B+1).
```

All modular values use canonical residues in `[0,N)`. Every Euclidean
quotient, remainder, least positive inverse, and inverse quotient is formed
as an integer before modular reduction.

## 2. Fixed canonical grammar

The shift set is exactly

```text
C = {-4,-3,-2,-1,0,1,2,3,4}.
```

For every `c` in `C`, define

```text
x_c = B+c
d_c = floor(N/x_c)
r_c = N-x_c*d_c
u_c = least positive inverse of x_c modulo N
k_c = (x_c*u_c-1)/N
```

The inverse is constructed only after `gcd(x_c,N)=1`.

The ten signed expression names at anchor `c` are exactly

```text
+x_c, -x_c,
+d_c, -d_c,
+r_c, -r_c,
+u_c, -u_c,
+k_c, -k_c.
```

Signs are applied as integers and then reduced canonically modulo `N`.

For each source anchor `c`, choose ordered expression names

```text
t_name   in E_c
eta_name in E_c.
```

For each target anchor `c'` in `C` with `abs(c'-c)<=1`, choose

```text
v_name in E_c'.
```

The candidate name is the literal tuple

```text
(source_anchor,t_name,eta_name,target_anchor,v_name).
```

The enumeration order is increasing source anchor, the displayed expression
order for `t`, the displayed expression order for `eta`, increasing target
anchor, and the displayed expression order for `v`.

There are exactly

```text
25,000 candidates
900 named source pairs
```

as proved in `DRAFT_ALGEBRA.md`. The self-test must assert both counts.
Duplicate numerical values on one row remain distinct named syntaxes. The
implementation may cache their arithmetic, but it may not merge their
scores or names.

No discovery result can add a shift, sign, atom, coefficient, operation,
source pair, target, or candidate.

## 3. Exact endpoint computation

For one source `(t,eta)`, compute

```text
(t+w)^B = P_B + Q_B*w,  w^2=eta,
```

by binary powering of pairs with

```text
(R,S) * (R',S') = (R*R' + eta*S*S', R*S' + S*R') mod N.
```

For target `v`, compute

```text
F_B(t,eta,v) = P_B-v*Q_B mod N.
```

The literal matrix control is

```text
C = [[(t-v)/2, 1],
     [(eta-v^2)/4, (t+v)/2]] mod N.
```

The self-test must verify on every test case that

```text
(C^B)[0][0] = 2^(-B)*F_B mod N
```

by an independent ordinary `2 by 2` binary power.

The production path uses pair powering, not eigenvalues, square roots,
Legendre symbols, or hidden-field arithmetic.

## 4. Mandatory logical screen chronology

The following order defines the evidence classification. The implementation
may cache or batch arithmetic. It may lazily replay expensive bounded-phase
checks after a raw endpoint hit. It must not update a score, emit a selected
hit, or classify a hit as nondirect until every logically earlier check has
been replayed in this order.

### 4.1 Row validation and direct cleanup

1. Verify the promised row, exact square-root inequalities, distinctness,
   balance, and factor bit length.
2. Compute `gcd(B,N)`. A proper gcd is `boundary_cleanup`.
3. For every integer `j` from `-64` through `64`, compute
   `gcd(B+j,N)` when `0<B+j<N`. A proper gcd is
   `near_square_offset_cleanup`.
4. Run exactly 65 Fermat trials. Put `X=B+1+j` for `0<=j<=64`. If
   `X^2-N` is a nonnegative square, verify the two nontrivial factors. This
   is `fermat_cleanup`.
5. Construct every `x_c,d_c,r_c,u_c,k_c` in increasing `c` and the atom
   order shown in Section 2. Gcd-screen every constructed nonzero atom with
   `N`. A proper gcd is `atom_cleanup`. A saturated atom is invalid and
   aborts the row; it is not replaced.

A row with any cleanup factor is recorded in the cleanup table and is not
eligible for candidate selection. Later labelled inspection may name the
factor. It cannot restore the row.

### 4.2 Candidate input invariants

For a candidate `(t,eta,v)`, screen in this order:

```text
g_eta   = gcd(eta,N)
g_delta = gcd(t^2-eta,N)
g_H     = gcd(v^2-eta,N).
```

The omitted factors `4` are units because `N` is odd. A proper gcd is an
`input_invariant_factor`. A saturated gcd makes the candidate locally
degenerate in both CRT components. Such a candidate is `input_degenerate`
and is not eligible. Only the triple `(1,1,1)` reaches the clean lane.

This is the affine `e=1` chart. The general theorem still records

```text
delta = det(C)
eta   = discriminant(C)
e     = L(I)
H     = det(A*I-e*C).
```

The `e=0` homogeneous chart is represented only by the `Q_B` control below.
No ranked candidate uses it.

### 4.3 Bounded source-order screens

For every clean source pair, compute `Q_m(t,eta)` for each

```text
m in {2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}.
```

A proper `gcd(Q_m,N)` is `bounded_source_order_factor`. A saturated gcd
marks the source `global_bounded_source_order`. Every ranked candidate using
that source is a decoy on that row. A gcd of one passes.

### 4.4 Known orbit-target screens

The orbit-offset set is exactly

```text
E_orbit = {-16,-15,...,-1,1,...,15,16}.
```

For positive `e`, screen

```text
O_e = P_e(t,eta)-v*Q_e(t,eta).
```

For negative `e`, screen

```text
O_e = P_abs(e)(t,eta)+v*Q_abs(e)(t,eta).
```

A proper `gcd(O_e,N)` is `direct_orbit_target_factor`. A saturated gcd is
`global_orbit_target_e`; it makes the endpoint an order test with exponent
`B-e`. Neither outcome is a free-coset hit.

The target grammar contains no power operation. These numerical screens
still run because an atom can coincide with a bounded orbit value on one
input.

### 4.5 Bounded target torsion and mixed phase screens

The target-torsion set is exactly

```text
M_target = {2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}.
```

For each `m`, screen

```text
Q_m(v,eta).
```

A proper gcd is `bounded_target_torsion_factor`. A saturated gcd records
`global_target_torsion_m` and makes a later endpoint hit a known finite
phase.

The mixed phase box is exactly

```text
E_phase = {-4,-3,-2,-1,0,1,2,3,4}
M_phase = {2,3,4,5,6,8}.
```

For each `(e,m)`, compute the pair for `lambda(v)^m` as

```text
(R,S) = (P_m(v,eta),Q_m(v,eta)).
```

Let `(P,Q)` represent `z^(e*m)`:

```text
if e*m >= 0: (P,Q) = (P_(e*m)(t,eta), Q_(e*m)(t,eta))
if e*m <  0: (P,Q) = (P_abs(e*m)(t,eta), -Q_abs(e*m)(t,eta)).
```

Screen the exact equality determinant

```text
Z_(e,m) = R*Q-S*P mod N.
```

A proper gcd is `mixed_phase_relation_factor`. A saturated gcd records the
global relation

```text
lambda^m = z^(e*m).
```

If the endpoint later hits under a global relation, compute

```text
Q_(m*(B-e))(t,eta)
```

and its gcd. A proper gcd is the prior order factor. A saturated gcd plus a
proper endpoint is `known_phase_split`. A gcd of one is inconsistent with
the claimed endpoint and global relation and aborts the run.

Every `global_orbit_target`, `global_target_torsion`, or
`known_phase_split` is a decoy. It cannot be counted as nondirect.

### 4.6 Powered collision and half-order screens

For each source, after computing `(P_B,Q_B)`, screen

```text
g_Q = gcd(Q_B,N)
g_P = gcd(P_B,N).
```

A proper `g_Q` is the P228 powered-collision/order factor. A proper `g_P`
is the target `lambda=-1` half-order factor and a Miller phase inside
`z^(2B)=1`. Every target under that source is direct on the row.

A saturated `Q_B` or `P_B` is recorded. It is not a proper factor. The
candidate endpoint can continue, but a global zero must agree with the
exact pair identities in replay.

### 4.7 Ranked endpoint

Finally compute

```text
F = P_B-v*Q_B mod N
g_F = gcd(F,N).
```

The outcome is one of:

```text
g_F = 1          no_hit
1 < g_F < N      proper_hit
g_F = N          saturated_hit.
```

A `proper_hit` is `nondirect_exclusive` only when:

1. the row passed every row-level cleanup;
2. all three input-invariant gcds are one;
3. every source, orbit, torsion, mixed-phase, `P_B`, and `Q_B` proper gcd is
   absent;
4. no applicable relation is globally saturated; and
5. exact replay passes.

The labels `p,q` may verify that `g_F` equals one hidden prime after the
public classification. They do not define success.

## 5. Fresh-uniform target controls

Uniform controls never enter ranking or selection.

For every clean named source pair and each control index in `{0,1}`, sample
`V,W` exactly uniformly from `[0,N)^2` with a counter-based SplitMix64
stream. Use the source ordinal `0,...,899` from Section 2. Initialize the
64-bit state by

```text
state = 0xF279C07A01234567
        xor phase_tag
        xor (row_id        * 0x9E3779B97F4A7C15)
        xor (source_ordinal * 0xBF58476D1CE4E5B9)
        xor (control_index  * 0x94D049BB133111EB)

phase_tag(discovery) = 0xD15C0A1B2C3D4E5F
phase_tag(heldout)   = 0xA11D5EED0042F279.
```

All additions, multiplications, and xor operations in the seed calculation
are modulo `2^64`. One SplitMix64 output is exactly

```text
state += 0x9E3779B97F4A7C15
z = state
z = (z xor (z >> 30)) * 0xBF58476D1CE4E5B9
z = (z xor (z >> 27)) * 0x94D049BB133111EB
output = z xor (z >> 31).
```

For this packet `N<2^112`, so concatenate two outputs, first output as the
high 64 bits, to obtain uniform `R` in `[0,2^128)`. Put

```text
L = floor(2^128/N)*N.
```

Reject `R>=L`; otherwise return `R mod N`. This gives an exact uniform
integer below `N`. Reject `(V,W)` unless

```text
gcd(V,W,N)=1
gcd(V^2-eta*W^2,N)=1.
```

Record every proper gcd encountered before resampling as a control cleanup.
A saturated target invariant is rejected. There are at most 64 attempts;
exhaustion aborts instead of changing the control count.

For an accepted target, compute

```text
F_uniform = W*P_B-V*Q_B mod N.
```

Conditional on acceptance, the two local projective targets are independent
and uniform on the clean target sets. The exact local hit probability is

```text
1/(r-Legendre(eta,r)).
```

The production construction never computes the Legendre symbols. Labelled
postprocessing reports the exact expected count and observed count by local
orientation. Uniform-control hits are never candidate leads.

## 6. Small high-order diagnostic control

This control runs on exactly the first four `random_balanced` rows at each
factor size in each phase. It is not ranked.

Put

```text
D0 = n
A0 = n^2+n.
```

Scan `a=2,...,A0` in increasing order. Screen `gcd(a,N)`. For every unit
base, compute incremental powers for `e=1,...,D0` and screen
`gcd(a^e-1,N)`.

```text
proper gcd:  diagnostic_factor_exit
saturated gcd: reject this base
all gcds one: retain the first base z
no retained base by A0: diagnostic_shortfall.
```

For a retained `z`, both local orders exceed `D0` by the complete exponent
scan. Screen `gcd(z-1,N)`, then construct

```text
eta = 1
t = (z+1)/(z-1) mod N.
```

Use all 90 affine target expressions `v` in the union of the nine anchored
target banks, preserving their names. Report endpoint and decoy outcomes.
Do not add them to the 25,000 candidates, discovery scores, selection, or
lead gate.

The control records `D0`, `A0`, bases attempted, exponent gcds, the retained
base or shortfall, every factor exit, and every endpoint outcome. It claims
no target correlation and imports no large-order constructor.

## 7. Deterministic labelled cohorts

Factors have the declared exact bit length. Every phase enforces distinct
`N` values across all sizes and cohorts.

Discovery factor sizes are exactly

```text
18, 24, 30, 36 bits.
```

Held-out factor sizes are exactly

```text
40, 46, 52, 56 bits.
```

At each size, generate exactly:

```text
random_balanced                         96 rows
wide_gap                                64 rows
four_capacity_at_most_32                64 rows
consecutive_prime                       32 rows
```

Thus each phase has exactly `4*256=1024` rows, before public cleanup.

The extra cohort predicates are:

```text
wide_gap:
    q-p >= ceil(p/4)

four_capacity_at_most_32:
    max(gcd(p-1,q-1), gcd(p-1,q+1),
        gcd(p+1,q-1), gcd(p+1,q+1)) <= 32

consecutive_prime:
    q is the least prime greater than p.
```

Consecutive-prime rows are direct-screen controls. They are expected to
leave by the Fermat or offset screens. They remain in the fixed cohort and
cannot be replaced for that reason.

The fixture generator uses SplitMix64 with literal phase seeds

```text
discovery: 0xF279D15C0A1B2C3D
held-out:  0xF279A11D5EED0042
```

Generate sizes in increasing order, cohorts in the displayed order, and
row ordinals in increasing order, using one continuous phase stream. One
random factor candidate consumes one SplitMix64 output, masks to `b` bits,
then sets bit `b-1` and bit zero. A random prime search returns the first
prime among at most 65,536 such independent candidates. It does not walk
from a failed random candidate.

For `random_balanced`, `wide_gap`, and `four_capacity_at_most_32`, generate
`p` and then generate `q` from the same stream until all generic and cohort
predicates hold. For `consecutive_prime`, generate `p`, then test
`p+2,p+4,...` in order and retain the first prime. A row attempt restarts
from a fresh generated `p` when its bounded `q` search fails or any final
predicate fails.

Primality for the at-most-56-bit factors uses deterministic Miller-Rabin
with bases

```text
2, 325, 9375, 28178, 450775, 9780504, 1795265022.
```

Each requested row has at most 4096 row attempts. Each prime search and
consecutive-prime walk has at most 65536 odd candidates. Exhaustion,
equality, wrong bit length, imbalance, a failed cohort predicate, or a
duplicate restarts the bounded row attempt. Final exhaustion aborts the
phase. It never shrinks or substitutes a cohort.

## 8. Held-out authentication and firewall

The final runnable packet must create both fixture files before discovery
selection and record:

```text
fixture byte length
row count
SHA-256
generator seed commitment
generator executable SHA-256
```

The held-out rows must be stored in a private fixture root that the discovery
process cannot list or read. The frozen public seed authenticates
reproducibility, but it is not passed as an argument to discovery mode. The
discovery process receives only the discovery fixture path, its output path,
and the frozen grammar. Static audit must prove that discovery mode neither
invokes the fixture generator nor reconstructs a fixture from a compiled
seed. This is an authenticated executable firewall. It is not a claim of
information-theoretic blindness from a human who has read the frozen seed.

The final containment design for this separation is pending the user's
explicit workflow decision. No substitute filesystem convention is
authorized by this draft.

After discovery selection is sealed, held-out mode must authenticate the
private fixture against the precommitted byte length and SHA-256 before it
evaluates one row. After completion, the packet publishes the held-out
fixture, seed, generator provenance, and authentication result.

Any missing fixture, readable held-out path during discovery, hash mismatch,
row-count mismatch, or cohort-count mismatch aborts. It never regenerates a
fixture after selection.

## 9. Factor-blind discovery selection

All 25,000 candidate syntaxes are fixed before any labelled row exists.
Discovery ranks them by these public outcome fields, in order:

1. nondirect exclusive rows, descending;
2. distinct public scales with a nondirect exclusive row,
   descending;
3. the minimum nondirect count across the four public scales, descending;
4. all proper endpoint rows, descending; and
5. candidate name, ascending.

For every row, the public scale is

```text
b_pub = ceil(bitlength(N)/2).
```

It equals the declared factor size on the promised cohorts. The score uses
only `N`, public construction values, public gcd outcomes, `b_pub`, and the
fixed decoy classification. It does not use which hidden factor was returned
or the labelled cohort type.

Discovery writes exactly the first 128 candidates. It writes all score
fields in canonical decimal form and one final newline. The runner seals
the exact bytes with SHA-256.

Held-out mode verifies:

```text
exact header
exact byte length
final newline
128 unique known candidate names
ranks 1 through 128
canonical score fields
score ranges
declared ordering
selection SHA-256.
```

It does not rerank or replace a selected candidate. It evaluates all 25,000
candidates to distinguish selection loss from a grammar null, but only the
sealed 128 can pass the lead gate.

## 10. Held-out lead gate

A selected candidate is a finite lead only when all conditions hold.

1. It has at least eight held-out nondirect exclusive rows.
2. It hits at least three held-out public scales.
3. It hits public scale `52` or `56`.
4. It has at least one nondirect exclusive hit in each of the held-out
   `wide_gap` and `four_capacity_at_most_32` cohorts.
5. Every raw and nondirect hit has a passing exact replay certificate.
6. No hit used by the gate is a cleanup, input degeneration, powered
   collision, half-order event, known orbit target, bounded target torsion,
   mixed finite phase, or direct target relation.

The gate is deliberately strong relative to the exact uniform baseline. A
pass is still finite discovery. It requires a new proof and a new packet.

## 11. Exact replay certificates

Every proper endpoint gcd, whether direct or nondirect, writes one canonical
certificate row containing:

```text
phase, row_id, factor_size, cohort, N, B
candidate rank if selected, complete candidate syntax
all five atom integers at every referenced anchor
t, eta, v
t^2-eta, v^2-eta modulo N and their gcds
P_B, Q_B, F, gcd(P_B,N), gcd(Q_B,N), gcd(F,N)
all nonunit or saturated chronology events
the first matching orbit/torsion/phase index, if any
source-power and endpoint operation counts
certificate classification and reason.
```

Labelled fields `p,q,chi_p,chi_q` are appended only after the public record
is sealed. They verify exclusivity and the local laws. They never alter the
classification.

Replay mode must independently recompute:

1. the row promise and exact `B`;
2. every referenced atom and inverse identity;
3. all input invariant gcds;
4. `(P_B,Q_B)` by pair powering;
5. the literal matrix power in Section 3;
6. every applicable orbit, torsion, mixed-phase, `P_B`, and `Q_B` screen;
7. the endpoint gcd and factor multiplication; and
8. the local residual equations
   `z_p^(s+chi_p)=lambda_p` and
   `z_q^(chi_q-h)=lambda_q` in division-free pair form.

Replay reads certificates only. It does not generate candidates, rerank,
or repair a failed record.

## 12. Planned C++17 implementation

No implementation belongs to this draft. A later packet may contain one
C++17 executable with modes

```text
--self-test
--benchmark
--generate-fixtures
--discovery
--heldout
--replay.
```

The plan uses:

- `uint64_t` for labelled factors and generator candidates;
- `boost::multiprecision::cpp_int` for `N`, products, exact square roots,
  Euclidean division, modular inverses, and modular arithmetic;
- immutable syntax IDs for the 25,000 candidates;
- one cached binary power per named or numerically deduplicated source;
- exact gcds, never probabilistic divisibility labels;
- four or fewer worker threads with deterministic row partitioning; and
- stable output sorting independent of thread completion order.

The arithmetic engine may deduplicate equal numerical source values within
one row. It must fan the result back to every original syntax ID. It may
compute expensive phase screens only for raw endpoint hits. It must then
replay the full logical chronology before scoring.

Required self-tests include:

1. `25,000` candidates and `900` source pairs;
2. the pair multiplication law against direct quadratic-algebra powers;
3. the endpoint identity against literal matrix powering;
4. split and nonsplit local examples;
5. `v=t`, `v=-t`, `v=0`, and homogeneous infinity controls;
6. the F278 `N=187` half-order example, classified as a phase decoy;
7. one proper input-invariant factor for each of `eta`, `delta`, and `H`;
8. positive and negative orbit offsets;
9. one mixed bounded-phase relation; and
10. uniform-projective target counts on small prime fields.

## 13. Exact work bounds and abort gates

Before cleanup, the two phases together contain exactly 2048 rows. The
fixed grammar gives the following absolute main-loop counts:

```text
named source endpoints: at most 1,843,200
ranked endpoint expressions: exactly 51,200,000 before invalid skips
uniform target controls: at most 3,686,400 accepted controls.
```

The implementation must count actual pair multiplications, modular
multiplications, gcds, inverse calls, uniform-target attempts, raw hits,
certificates, and output bytes.

The raw proper-hit cap is exactly

```text
MAX_RAW_HITS = 262144.
```

Crossing it aborts the phase. It never samples or truncates hits. Aggregate
output is capped at `512 MiB`. A write that would cross the cap aborts before
opening or extending the file.

The public benchmark uses exactly eight deterministic semiprime moduli. For
`i=0,...,7`, let `p_i` be the least prime not below

```text
2^35 + i*2^20 + 1001,
```

and let `q_i` be the least prime not below

```text
p_i + 2^33 + i*2^17.
```

The same deterministic 64-bit Miller-Rabin test and a 65,536-odd-candidate
cap apply. Failure to construct all eight aborts validation. The benchmark
uses the complete 25,000-candidate grammar. It emits only operation counts,
elapsed time, peak memory, and a checksum over all endpoints. It suppresses
candidate names, gcd outcomes, hit rows, and selection fields.

Production is permitted only if preflight projects all of:

```text
total wall time <= 14400 seconds
peak virtual memory <= 4 GiB
aggregate output <= 512 MiB
raw hits <= MAX_RAW_HITS.
```

An estimate above a gate kills D01. The packet cannot reduce rows, sizes,
controls, decoy checks, replay, or held-out separation after seeing the
estimate.

## 14. Planned outputs

Discovery would write exactly:

```text
F279-D01.discovery.rows.tsv
F279-D01.discovery.cleanup.tsv
F279-D01.discovery.summary.json
F279-D01.discovery.selection.tsv
F279-D01.discovery.certificates.tsv
F279-D01.discovery.uniform_controls.json
F279-D01.discovery.high_order_control.json
```

Held-out would add exactly:

```text
F279-D01.heldout.rows.tsv
F279-D01.heldout.cleanup.tsv
F279-D01.heldout.summary.json
F279-D01.heldout.lead_gate.tsv
F279-D01.heldout.certificates.tsv
F279-D01.heldout.uniform_controls.json
F279-D01.heldout.high_order_control.json
```

Replay would add exactly:

```text
F279-D01.replay.json
```

Every phase refuses to overwrite an existing output. The runner verifies
the exact file set, nonempty required files, byte caps, row counts,
candidate counts, selection count, certificate counts, fixture hashes, and
replay status.

## 15. Resource safety and unresolved containment

This Mac has 16 GiB of RAM. No production process may run locally. Before a
local compile, self-test, or benchmark, the operator must inspect CPU load,
memory pressure, swap, and existing heavy processes. Validation is limited
to one low-priority core and the benchmark in Section 13.

Any future remote production must first inspect remote CPU count, load,
memory, swap, disk, and competing processes. The intended caps are:

```text
threads <= 4
nice level 15
one generic production lock
one audited process group
RLIMIT_CORE = 0
virtual memory <= 4 GiB
output <= 512 MiB
one shared hard deadline <= 14400 seconds.
```

The available host has no approved cgroup-v2 workflow. Replacement by a
fresh numeric UID plus `RLIMIT_NPROC` and `RLIMIT_AS` is still waiting for
the user's explicit decision. This draft does not authorize that
replacement. It also does not authorize a container, user systemd, cgroup
v1, or an unaudited shell fallback.

No source, runner, freeze, compile, validation, fixture generation,
production, or remote access may occur until:

1. the theory and preregistration receive a fresh no-context kill audit;
2. all audit objections are repaired in a new draft;
3. source and runner receive a separate static hostile audit;
4. the complete packet is frozen with SHA-256 hashes;
5. the user explicitly decides the containment workflow; and
6. live resource gates pass.

## 16. Interpretation of outcomes

A lead means only that one frozen canonical biased source-target syntax has
repeated held-out nondirect exclusive hits under this finite design. The
next step is an exact theorem attempt. The experiment itself does not give
an inverse-QP probability or all-input law.

A null means only that no selected syntax passes the held-out gate. It does
not close deterministic biased torus targets, other integer sections,
larger expression grammars, adaptive feedback, higher modes, or semilinear
actions.

A resource abort is not mathematical evidence. A containment block is not
resource or mathematical evidence. A direct-decoy result strengthens only
the named orbit, bounded-torsion, phase, order, or near-square
classification that produced it.
