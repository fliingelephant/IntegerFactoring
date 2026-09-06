# F265-D10 draft preregistration amendment — closed replay and private-label chronology

## Status and exact imports

This is an unfrozen, theory-only additive draft. It creates no source, runner,
manifest, freeze, compilation, preflight, execution, result, or ledger entry.
It authorizes none of those actions.

| Artifact | SHA-256 |
|---|---|
| `D09_DRAFT_ALGEBRA.md` | `93ee6021b969a3624cf499df5e18ea9c262e2a095a6b0634644cc1d69ee8030d` |
| `D09_DRAFT_PREREGISTRATION.md` | `3b499578678a0f71c75f52608e53f2fba7f390fb5a09a95bc20c61d09fe1c0a4` |
| `D10_DRAFT_ALGEBRA.md` | `aab2397c601b645f71da0bc79a8f58ed9ef79ea984fa7f7458ab2a49582a17a7` |

Read both authenticated D09 bytes in full. Apply this exact replacement map:

- D10 Sections 1 and 6 replace D09 Section 2's process-firewall and private-
  label chronology paragraphs; its hashes, schemas, counts, filters, and bank
  order survive.
- D10 Sections 1, 3, and 6 replace D09 Section 4's bank/replay/decision/auditor
  chronology; its at-most-eight-bank chunk scheduler survives.
- D10 Sections 2 and 6 replace D09 Section 5's resource/invariant and global-
  failure semantics; its enum, event schema, sticky fields, and size proof
  survive.
- D10 Section 3 adds to D09 Sections 6--7 and replaces their replay scope and
  theorem-breach semantics. Every displayed D09 cap not changed here survives.
- D10 Section 6 replaces D09 Section 8's empty-quotient and factor-bit-cell
  meanings; its remaining finite-label clauses survive.
- D10 Sections 4--5 replace all of D09 Section 11 except the component fixtures
  and rates they expressly retain.
- D10 Sections 7 and 8 replace D09 Sections 12 and 13 respectively.

Every other D09 preregistration clause survives literally. No D05--D08 runtime
rule is composed directly with D10. The D09 import table remains the complete
provenance table.

## 1. Source meaning and nonadaptive corpus firewall

This section implements the D09 Sections 2 and 4 entries in the replacement
map above. D09's finite question and deliberate pair-control omission survive.

The fixed cohort remains the 180 discovery and 288 heldout public F268-D04
rows authenticated by D09. Filtering, bank order, seed derivation, 32 proposal
slots per mode, 128-attempt rejection sampler, and every proposal screen are
unchanged. Private `p,q` and label columns cannot take part in authentication,
filtering, fixture selection, source construction, resource reservation, bank
status, diagnostics, or the finite decision.

`U union POWER` means an ordered, tagged concatenation: all accepted `U`
rows in scalar order, followed by all accepted `POWER` rows in scalar order.
It is not a mathematical set operation. Equal row values are not deduplicated.
The sole cross-mode duplicate screen is the already specified accepted curve
tuple check. A proper factor stops the bank at its first reached source site;
no partial orbit reaches the peel and no new proposal is tried after an
accepted curve later stops. A relation factor does not stop later basis-root
classifications.

Discovery evaluation and replay finish before heldout evaluation starts. No
discovery statistic selects or changes a heldout byte, seed, ordering, cap,
fixture, diagnostic, threshold, or label rule. The authenticated reused corpus
is not pristine: `heldout` means only unseen by the D10 evaluator process.

The phase order for a bank is exactly:

1. authenticate its public row and initialize counters and sticky journal;
2. finish `U`, then finish `POWER`, or commit the first source terminal;
3. seal the tagged row-stream digest;
4. execute one simultaneous peel against the complete original bank;
5. commit the D10 algebra's exact empty certificate, or reserve and run F271
   on a residual of 1 through 64 rows, or resource-reject a larger residual;
6. construct the complete low basis and canonical complement, classify every
   basis root in ordinal order, and atomically commit the public core.

No factor discovered in one phase is fed back into any row, peel, F271, or
later bank.

## 2. Failure classes and empty cores

The exact empty residual values are D10 algebra Section 2. In particular,
`quotient_defined=true`, `Q` is empty, and `all_Q_images_global=true`. It uses
no reservation. A nonempty residual containing a unit row is not an empty
core and uses the F271 `S=0` law.

These remain recoverable bank-local resource outcomes: rejection after 128
sampler attempts; exhaustion of 32 curve proposals; residual size above 64
before F271; denial of the smaller packet reservation before F271; counted
arena exhaustion; and pre-commit record or writer cap exhaustion. Sticky
events already committed by the bank remain sticky.

Every bound proved by source chronology or F271 is instead an invariant.
Thus an attempted 33rd proposal, 129th sampler iteration, 321st row, F271
theorem-envelope breach after admission, false exact identity, 130th bank
event, 60,373rd evaluation packet event, or crossing of a derived packet
counter aborts the split and permits no finite label. No such event is
converted to `RESOURCE_REJECT`.

## 3. One-pass caps and independent replay

The D09 source and peel caps remain exact one-pass caps. The following table
closes operations D09 omitted. A `parity cell` is one exponent-parity read for
one final block and one residual coordinate. A `GF2 word operation` is one
64-bit pivot test, XOR, or assignment in the production elimination body.

| Added one-pass counter | Cap |
|---|---:|
| F271 parity cells | 56,160,000 |
| F271 GF(2) word operations, `468*524,288` | 245,366,784 |
| selected-row exact products | 1,916,928 |
| selected-row modular products | 1,916,928 |
| integer square roots | 29,952 |
| modular inversions | 29,952 |
| signed relation gcds | 59,904 |
| basis records | 29,952 |

For one bank the fixed elimination inserts at most 1,875 parity masks of 64
bits, reduces left-to-right against pivots 0 through 63, performs one reverse
reduction, then reduces at most 128 low/complement candidates by the same
rule. Counting every pivot test, XOR, and assignment is below 524,288; the
runtime counter is nevertheless checked before every operation. The parity
cap is `877,500*64`. The remaining caps are `468*64*64`, `468*64`, or twice
those quantities as appropriate.

The F271 scalar-gcd reservation ledger is initialized to zero once before
discovery and is not reset at the split boundary. Its one-pass cap remains
8,388,608. The D09 atomic 91,111-call reservation and canonical batching rule
remain literal. A later empty residual remains eligible without a reservation.

Replay starts with a separate zero ledger and every counter starts at zero.
It regenerates both tagged source streams, all terminal choices, the peel,
the empty certificate or F271 result, bases, roots, event bytes, and core bytes.
It has the identical cap for every operation, including source, sampler,
affine, row, peel, F271, parity, GF(2), root, serialization, and factor-journal
operations. It must reproduce every evaluation count and digest byte-for-byte.
The following selected totals make the duplication explicit; all unlisted D09
one-pass counters are doubled by the same rule.

| Counter | Evaluation | Evaluation plus replay |
|---|---:|---:|
| curve proposals | 29,952 | 59,904 |
| `random_below` calls / iterations / draws | 59,904 / 7,667,712 / 15,335,424 | 119,808 / 15,335,424 / 30,670,848 |
| rows / affine additions | 122,112 / 121,176 | 244,224 / 242,352 |
| product multiplications | 121,644 | 243,288 |
| each 122,112-operation peel counter | 122,112 | 244,224 |
| peel modular multiplications | 1,953,792 | 3,907,584 |
| F271 scalar gcds | 8,388,608 | 16,777,216 |
| saturation powers / refinement divisions | 4,893,354 / 13,981,013 | 9,786,708 / 27,962,026 |
| recursion nodes / touches | 4,194,304 / 699,050 | 8,388,608 / 1,398,100 |
| leaf assignments / tree updates | 4,923,306 / 54,156,366 | 9,846,612 / 108,312,732 |
| exponent updates / reconstruction incidences | 313,174,656 / 10,812,672 | 626,349,312 / 21,625,344 |
| terminal blocks / block comparisons | 877,500 / 39,012,624 | 1,755,000 / 78,025,248 |
| parity cells / GF(2) word operations | 56,160,000 / 245,366,784 | 112,320,000 / 490,733,568 |
| each selected-product counter | 1,916,928 | 3,833,856 |
| square roots / inversions / basis records | 29,952 each | 59,904 each |
| signed relation gcds | 59,904 | 119,808 |
| factor-event lines | 60,372 | 120,744 |

Diagnostics are not replayed and cannot consume a core counter.

## 4. Mandatory semantic and rate fixtures

All injection occurs below the same production body used by evaluation and
is unreachable for corpus split codes 0 and 1. Split code 2 is fixture-only.
Every fixture checks exact counters and a digest outside its timed interval.

The RNG suite asserts `mix64(0)=0xe220a8397b1dcdaf`, no warm-up draw, and the
literal limb order. For `random_below(17)`, inject 17 then 16 and require one
rejection and one acceptance. For `random_below(2^65)`, inject low limb
`2^64-1` and high limb 1 and require accepted value `2^65-1`. Separately
reject 128 times and require the resource status. `T_rbelow128` is the maximum
time of an exact 128-attempt call over eight repetitions.

The source branch suite uses `N=35,A=B=1` and exact curve points. It checks
`(0,1)+(0,34)` as global infinity, `(0,1)+(0,6)` as equal-`x` minus factor 5,
`(0,1)+(7,1)` as denominator factor 7, and `(0,1)+(9,2)` as the unit branch.
It checks row roots 5, 0, and 1 as proper factor, full skip, and unit. Signed
relation gcds are always evaluated minus before plus.

The cap-safe source timing fixture is one synthetic split-2 bank with
`K=160` and prime modulus

```text
N_star = 2^107-1 = 162259276829213363391578010288127.
```

Before timing, verify that 107 has no prime divisor at most its square root,
then set `s_0=4`, compute `s_{j+1}=s_j^2-2 mod N_star` for
`0<=j<105`, and require `s_105=0`. This is the fixed Lucas--Lehmer proof.
The fixture cannot produce a proper modulus factor. Fixed operand tapes below the shared proposal,
affine, row, rendering, product, and peel bodies execute serially: 32 reached
`U` proposal slots, 32 reached `POWER` slots, two complete 160-row streams,
all terminal affine and row branches once, 320 row renders, one 320-row
full-product fold, and all 320 simultaneous peel cells. The unit affine tape
uses the valid curve `A=1,B=3` and resets the point `(N_star-1,N_star-1)` for
doubling; fixed positive at-most-361-bit peel operands exercise the maximum
product width: for `0<=i<320`, use
`w_i=2^180+2i+1` and `a_i=w_i^2`. Assert every count and digest. Let
`T_source_max` be the maximum
of eight repetitions. Proposal samplers accept first in this fixture because
the separate sampler term charges their worst case.

The decoder suite sends all D10 algebra fixtures through production. It must
obtain the exact support-3 mask `111`, root 285541, normalized root 4, and gcds
3 then 5. It must obtain the exact full-support 64-cycle mask, a near-23,104-bit
selected product, and gcds 3 then 5. It also runs the empty peel, nonempty
`S=0`, and `S=1` cases.

The dense GF(2) fixture injects exactly 1,875 parity masks below parity
extraction. Its first 63 masks are `e_i xor e_63` for `0<=i<63`; its remaining
1,812 masks are the 64-bit all-ones word. The exact production elimination
must report rank 63 and the sole canonical kernel generator equal to the
all-ones word. This exercises dense reduction at the maximum `1,875 by 64`
shape. Let `rho_gf2` be maximum wall time divided by the exact counted word
operations.

Retain all D09 component fixtures except `SOURCE12` and the all-square
`T_basis64`; those two are deleted. Add exact production rates for recursion
nodes, touches, leaf assignments, exponent-coordinate updates, parity cells,
GF(2) word operations, selected exact products, selected modular products,
integer square roots, modular inversions, signed relation gcds, and basis
record rendering. Each rate is the maximum of eight repetitions divided by
its nonzero exact counter. The full-support fixture supplies the wide product,
root, and serialization operands. Operand menus are empirical rates, not
dominance theorems; the common hard deadline remains authoritative.

The event fixture first accepts 129 valid lines, then attempts a 130th and
requires an invariant without mutating count or digest. A separate fixture
injects prevalidated event tokens below the bank journals into the exact
packet-aggregation body. It accepts 60,372 ordered tokens, then attempts token
60,373 with the same requirement. Let `rho_factor` charge the complete
accepted-line path.

## 5. Literal serial projection

Let the added component rates have names matching their counters:
`rho_node`, `rho_touch`, `rho_leaf`, `rho_exp`, `rho_parity`, `rho_gf2`,
`rho_exact_product`, `rho_mod_product`, `rho_isqrt`, `rho_inverse`,
`rho_signed`, and `rho_basis_record`. Retain D09's `rho_gcd`, `rho_sat`,
`rho_div`, `rho_tree`, `rho_recon`, `rho_terminal`, `rho_compare`, and
`rho_io`. Define

\[
 T_{\rm source}=468T_{\rm source\_max}+59{,}904T_{\rm rbelow128}.
\]

This schedules 468 maximum banks serially. It deliberately charges maximum
320-row work to every smaller bank and double-charges first-try sampler work.
It makes no worker-speedup or censoring assumption.

\[
\begin{aligned}
T_{\rm decoder}={}&8{,}388{,}608\rho_{\rm gcd}
+4{,}893{,}354\rho_{\rm sat}
+13{,}981{,}013\rho_{\rm div}\\
&+4{,}194{,}304\rho_{\rm node}
+699{,}050\rho_{\rm touch}
+4{,}923{,}306\rho_{\rm leaf}\\
&+54{,}156{,}366\rho_{\rm tree}
+313{,}174{,}656\rho_{\rm exp}
+10{,}812{,}672\rho_{\rm recon}\\
&+877{,}500\rho_{\rm terminal}
+39{,}012{,}624\rho_{\rm compare}
+56{,}160{,}000\rho_{\rm parity}\\
&+245{,}366{,}784\rho_{\rm gf2}
+1{,}916{,}928(\rho_{\rm exact\_product}+\rho_{\rm mod\_product})\\
&+29{,}952(\rho_{\rm isqrt}+\rho_{\rm inverse}+\rho_{\rm basis\_record})
+59{,}904\rho_{\rm signed}.
\end{aligned}
\]

Define

\[
 T_{\rm pass}=T_{\rm source}+T_{\rm decoder}
              +60{,}372\rho_{\rm factor}
              +210{,}632{,}704\rho_{\rm io},
\]

\[
 T_{\rm raw}=2T_{\rm pass}+900,
 \qquad T_{\rm projected}=1.75T_{\rm raw}.
\]

The factor two is the complete independent replay, including source. The 900
seconds is the single diagnostic allowance. Preflight must finish in 1,200
seconds and production requires `T_projected<=10,800` seconds plus the D09
300-second finalization reserve inside the 14,400-second common deadline.
Any zero denominator, mismatch, projection failure, or insufficient live
remainder stops before discovery.

The 64 MiB I/O rate payload is transient. In each of four repetitions write
one temp, close it, rename it, hash it, and unlink it before the next phase.
At most a 64 MiB target and 64 MiB temp coexist. Retain only aggregate metrics
under the 64 MiB preflight category. D09's retained total 210,632,704 bytes,
per-file cap, worker temporaries, and 294,006,784-byte directory peak remain
literal and now include this transient maximum.

## 6. Finite labels and private-label staging

The D10 algebra's pair-control disclaimer is part of every result. A
`factor-bit cell` in the positive rule means one distinct numeric heldout
`factor_bits` value in `{40,48,56,60}`; shape is irrelevant to this diversity
count. Positive therefore requires at least two decoder-strict hit banks whose
public rows contain at least two distinct values from that set. Null retains
the 12 separate factor-bits-by-shape coverage cells and uses the exact empty
quotient semantics above.

The public core fixes the finite-decision bytes only after discovery replay
and heldout replay join. Then diagnostics run in canonical order. Expiry of
the inner 900-second diagnostic timer is a normal `TIMEOUT` prefix and cannot
change those bytes. The 14,400-second common deadline, containment failure,
signal, abnormal child exit, or package-writer failure always prevents release,
even after core commit.

Private labels obey this exact chronology:

1. A controller authenticates the expected private hashes without exposing
   label bytes or paths to any evaluator process.
2. Evaluation, replay, and diagnostics receive public copies only. Their
   readable namespace contains no private path, descriptor, environment
   value, symlink, readable ancestor, copied field, or embedded label text.
3. All evaluator, replay, and diagnostic processes exit. The controller
   verifies that none remains and seals the public core, counters, finite
   decision, and hashes.
4. Only then does the controller materialize authenticated private files in a
   separate auditor namespace and start the label auditor.
5. The auditor can validate the fixed event factors and cohort join only. It
   has no writable public-core path, shared memory, signal channel, pipe, or
   return channel to an evaluator. It exits before final packaging.
6. A private-hash, join, factor, auditor, or packaging failure releases no
   finite label. Success releases the already fixed core decision together
   with a separate label-audit result.

This is an access-control requirement, not a claim that path omission alone
is a firewall.

## 7. Dynamic containment is pending

This section replaces D09 Section 12. D10 has no approved dynamic-containment
implementation and therefore cannot proceed to source, compilation, preflight,
or execution. D09's cgroup-v2 mechanism is not silently inherited as launch
authorization on a host where it is unavailable.

A fresh numeric UID combined with a generic exclusive lock, serial heavy-phase
topology, `RLIMIT_NPROC`, per-process `RLIMIT_AS`, and `RLIMIT_CORE=0` is only
a non-authorizing deployment option. It becomes eligible for review only after
an immutable runner gives numeric limits and proves a hard aggregate envelope,
including every controller, evaluator, replay, diagnostic, auditor, writer,
and descendant. `RLIMIT_AS` alone is per-process; `RLIMIT_NPROC` can count
other processes sharing a UID. Sampled RSS is not containment.

The user must explicitly approve a replacement workflow. A fresh no-context
hostile audit must then authenticate its exact bytes and attack its lock,
UID isolation, process count, address-space product, core-dump ban, kill path,
common deadline, filesystem firewall, and cleanup. Until both events occur,
dynamic containment is a hard pending gate.

## 8. Hostile theory release gate

A fresh reviewer must authenticate all three input hashes and try to kill:
the tagged `U`/`POWER` source, factor chronology, one-round kernel isomorphism,
empty and unit-row boundaries, exact F271 import, omitted pair controls, every
evaluation/replay cap and reservation transition, synthetic source projection,
support-3/full-support/dense fixtures, reused-corpus firewall, private-label
chronology, finite-cell scope, output peaks, deadline precedence, and the
pending containment gate.

A theory PASS authorizes only C++17 source drafting. It does not authorize a
runner, freeze, compilation, preflight, local or remote execution, result, or
ledger edit.
