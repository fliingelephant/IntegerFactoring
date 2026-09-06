# F265-D06 draft algebra: peeled elliptic cubic-row kernel

## Status and composition

This is an unfrozen theory draft. It has not received a hostile audit. There
is no D06 source, runner, compilation, preflight, freeze, production run, or
cohort result.

D06 preserves the mathematical core of the following D05 draft byte for
byte, except where this document explicitly replaces it:

| imported draft | SHA-256 |
|---|---|
| `D05_DRAFT_ALGEBRA.md` | `e3cbefeb597f263501d327f15f9dd4c7b78ee37d37178135ab1c0a5ff73e9fd3` |

The normative D06 algebra is the imported D05 algebra together with the
replacements below. In imported prose, the complete token `D05` names the
proposed packet and is rebound to `D06`. No other textual substitution is
implicit. If a replacement below conflicts with imported text, the D06
replacement controls. A future standalone preregistration must materialize
the resolved text and pass another byte-level audit before source is written.

## 1. Surviving mathematical core

The following claims are unchanged.

1. Each admitted public elliptic row has
   `a_i=u_i^3+A*u_i+B>0` and a supplied unit square root `v_i (mod N)`.
2. For an active set `S`, the saturated private part

   \[
   b_i={a_i\over\gcd(a_i,P_i^{L_i})},\qquad
   P_i=\prod_{j\in S\setminus\{i\}}a_j,
   \quad L_i=\operatorname{bitlen}(a_i),
   \]

   contains exactly the primary parts of `a_i` absent from every other
   active row.
3. Simultaneously deleting every row with nonsquare `b_i`, and repeating to
   a fixed point, preserves the complete integer-square kernel and every
   normalized root after zero coordinates are reinserted.
4. Singleton testing and the test

   \[
   a_i a_j\text{ square}\iff
   a_i/\gcd(a_i,a_j)\text{ and }
   a_j/\gcd(a_i,a_j)\text{ square}
   \]

   are complete for support at most two.
5. The normalized-root map is a homomorphism on the square kernel. A
   canonical basis of the low-support span therefore suffices to decide
   whether its image is global. On the global-low-image branch, a canonical
   complement basis suffices to decide the finite quotient question.
6. Relation-local chord data are explanatory only. They are evaluated after
   the mathematical result is committed and do not create a parity relation.

D06 adds no elliptic source theorem, success law, residual-core bound, or
all-input factoring claim.

## 2. Sticky public factor events

A **public factor event** is the verified result `1<g<N` and `g|N` of a
prescribed factor-screen gcd. It excludes explanatory diagnostic gcds whose
outputs need not divide `N`. It includes direct curve, affine, row, coordinate, and chord
screens and every signed gcd attached to a verified singleton, support-two,
low-basis, or structural-complement relation. The event is defined before
any later continuation or resource decision.

For each intended bank `h`, let `F(h)` be the ordered stream of public factor
events that were actually reached. The first event sets the sticky Boolean

`observed_useful_factor(h)=true`.

Neither an exception nor a later resource rejection can clear that Boolean,
the first witness, the event count, or the event-stream digest state. A bank
summary is committed for every intended slot, including corpus shortfalls,
early direct-factor stops, and later resource rejections. If the event cap is
crossed, the overflow marker is also sticky and the bank is ineligible.

This is an evidence invariant. It does not feed a factor back into curve
generation, peeling, P66, relation construction, or diagnostic selection.

## 3. Exact held-out null quantifiers

Let `H` be the 384 preregistered held-out slots and let `E` be the subset
whose full mathematical core is eligible. A useful direct or low-support
factor found in any slot in `H` prevents the null label, even when that bank
later becomes ineligible.

More precisely, `finite_quotient_null_signal` is true only if all of the
following hold.

1. For every `h in H`, `observed_useful_factor(h)=false` and its factor-event
   overflow bit is false.
2. For every `h in E`, the complete P66 kernel, canonical low basis,
   structural complement, and every prescribed root verification completed.
3. For every `h in E`, the low image is global, the quotient is defined, and
   every quotient-complement basis image is global.
4. At least 90 percent of `H` is eligible, and every factor-size/shape cell
   has at least 12 eligible banks.

Condition 1 quantifies over all intended held-out slots, not only eligible
banks. A shortfall or an unexecuted later screen is not asserted to be a
mathematical null; it is handled only by the explicit coverage conditions.
The label means a finite observed null under those coverage conditions.

The positive quotient label is unchanged: it requires two strict useful
quotient-hit banks in two factor-size cells. A quotient hit is strict only
when that bank has no earlier direct or useful low-support factor.

## 4. Resource caps do not create null evidence

Every candidate, retry, factor-event, decoder, relation, memory, record,
output, and wall cap is a visible resource boundary. A core cap crossing
makes the affected bank ineligible. A factor observed before that crossing
remains in `F(h)` and still prevents the held-out null label.

The full sparse exponent-entry cap is part of the P66 state, not shorthand
for the dense-cell cap. D06 requires an independent preflight fixture that
reaches exactly 262,144 nonzero sparse entries. Failed refinement comparisons
include loop traversal, counter, branch, and cap-check cost; timing a gcd in
isolation is not a substitute for that loop.

## 5. Diagnostic task domain

Every diagnostic task has one of two kinds:

- `PAIR=0`: one unordered same-curve pair; or
- `ANCHORED_THIRD=1`: one ordered choice of a pair anchor and the third row
  inside an unordered same-curve triple.

Rows in the anchor are stored increasingly. A pair task uses the unsigned
16-bit sentinel `NO_ROW=65535` for `third_row`. Its third-root result and all
six three-index predicates use the tri-state value `NOT_APPLICABLE=2`.
Boolean false and true are `0` and `1`. An anchored-third task has an actual
third row and no sentinel.

The total task order is

`(split,bits_rank,shape,index,basis_ordinal,task_kind,curve,`
`pair_row_1,pair_row_2,third_row)`.

Here `bits_rank` is the position in the frozen factor-bit menu, row IDs are
original bank row IDs, `pair_row_1<pair_row_2`, and `basis_ordinal` is the
ordinal among the selected structural-complement vectors. The key is unique.
Every task advances the complete task counter and digest in this order,
whether or not a predicate matches. Retained details are the first records
in this same order. Thus a pair sentinel, an anchor choice, and a truncated
detail stream have one deterministic interpretation.

## 6. Scope

The D06 changes close evidence and resource-accounting ambiguities. They do
not strengthen the peeled-kernel theorem. A fresh no-context hostile theory
audit must pass before any source is written.
