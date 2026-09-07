# Nonuniform coupled-rank search

**Family:** route:F31

Status: complete exact finite search. The return-map formulas are
author-derived and finitely checked. This packet establishes no asymptotic
success law, source advantage, QP factoring algorithm, or novelty claim.

## Prerequisite and protocol

The independent `return_map_checks.py` run passed before this search started.
Its full check covered 4,396 general `(N,a,t)` cases through odd `N<=31`,
964,448 accepted `(k,q)` pairs, 2,045,068 floor-sum calls, and 4,396 uniform
distinct-rank laws. Its engineered-source check through odd `N<=511` retained
57 first-generation gcd exits, 18 second-generation gcd exits, 177 unit
sources, and 51,898 accepted-pair checks. It found no anomaly.

The search then reused every frozen F337 source record on `N=209,1333,10807`:
168 source attempts, including all 15 standalone generation-factor records,
153 units, and 459 unit/threshold cells. No source parameter or rule was
selected from an output, factor label, or offline energy.

For every unit cell the solver rebuilt the sorted rank map only as an offline
oracle. It independently evaluated the public return-map rank by floor sums,
kept a uniform starting index denominator `m=t+1`, and evaluated all six fixed
rules:

    1, floor(L/2), alpha, beta, beta-alpha, N  (all modulo L).

A zero residue is a failed proposal. An endpoint outside `A={0,...,m-1}` is a
failed attempt. Duplicate rule residues remain separate paired views. Every
nonzero rule passed the exact endpoint count `K(q)` and deleted-visit rank
displacement identities. The analytic uniform-nonzero-`q` and direct
uniform-rank controls are retained in every cell.

Each rule also gcd-screens the deduplicated public list
`t,m,L,u,v,alpha,beta,q,q-m,c,L-c`, with `c=qu mod L`, as a separate control.
All observed deleted sizes satisfy `d<=2316`, below the declared diagnostic
limit 4,096, so every full fixed-`q` menu was enumerated and charged. The
menus used 509,249 deduplicated gcds and 4,183,836 gcd Euclidean divisions.
The eleven-value controls used 21,128 gcds and 101,590 divisions. Offline
array traversal is validation work, not public runtime work.

## Per-input and per-rule outcomes

Each table cell is the cell-wise mean unconditional `acceptance / factor`
probability, followed by `positive cells (positive cells without a factor in
the eleven-value direct control)`. Exact fractions and all source/profile
splits are in `search_aggregate_output.json`.

| rule | N=209 | N=1333 | N=10807 |
|---|---|---|---|
| `q_one` | .89579 / 0; 0 (0) | .90193 / 0; 0 (0) | .88852 / 0; 0 (0) |
| `q_half` | .90863 / .01377; 19 (16) | .90957 / .00566; 21 (20) | .90523 / .00184; 18 (16) |
| `q_alpha` | .88921 / .00685; 11 (3) | .94036 / .00027; 2 (2) | .91924 / .00006; 1 (0) |
| `q_beta` | .77187 / .02717; 15 (6) | .78073 / .01101; 6 (4) | .84976 / .00246; 3 (3) |
| `q_gap_difference` | .90259 / .07696; 35 (26) | .90515 / .00250; 5 (2) | .87609 / .00256; 6 (2) |
| `q_N_mod_L` | .91183 / .03260; 33 (25) | .91140 / .00728; 25 (22) | .87782 / .01314; 33 (30) |

The analytic uniform-nonzero-`q` mean factor probabilities are 0.07574,
0.03218, and 0.01141, with mean acceptance 0.92030, 0.92488, and 0.91735.
Thus `q_gap_difference` is largest at `N=209`, `q_beta` is largest at
`N=1333`, and `q_N_mod_L` is largest at `N=10807`. No fixed rule is the
largest on all three inputs. The adjacent rule `q_one` has no coupled factor
on any cell.

There are two zero `q_alpha`, 55 zero `q_beta`, seven zero
`q_gap_difference`, and seven zero `q_N_mod_L` proposals. Their failed status
is retained. Rule collisions are also explicit: across all 459 cells, alpha,
beta, gap-difference, and `N mod L` have 254, 63, 66, and 174 duplicate views.

## Strongest cells after the fixed rule set was evaluated

The strongest cell without a factor in the eleven-value direct control is
post hoc. It is `N=1333`, source `inverse_1_2`, public denominator 25,
`a=160`, `t=166`, `L=183`, `d=16`, and rule `q_beta=47`. Its acceptance is
`151/167`; its unconditional factor probability is `115/167`, split into 27
starts returning 31 and 88 returning 43. The analytic uniform-`q` control is
`613/15197`, and direct uniform-rank gcd mass is `8/167`. Its complete menu
has 34 deduplicated gcds and exposes 31, 43, 124, and 129. The coupling's
expected public cost includes 25 setup rank queries,
`8954/167` floor-sum calls, `28677/167` floor-sum iterations, and `318/167`
gcd calls before any direct-control comparison.

The repeated `N=209` inverse-denominator-three half-window cell has
`a=70,t=104,L=107,d=2,q_gap_difference=34`. Its acceptance is `103/105`
and factor probability `22/35`, versus uniform-`q` `46/371` and direct-rank
mass `2/15`. All 66 factor starts return 11. Its six-entry menu directly
exposes `gcd(33,209)=11`.

At `N=10807`, source `direct_1_2`, `a=105`, `t=5403`, `L=5455`, `d=51`,
the rule `q_N_mod_L=5352` has acceptance `5353/5404` and factor probability
`175/386`, versus uniform-`q` `68914/3684177` and direct-rank mass `103/5404`.
Its 104-entry menu exposes 101 and 5,350, whose gcd is 107. This cell occurred
twice under the retained source streams.

Every coupled factor in the complete search is covered by its enumerated
fixed-`q` menu, as required by the return-map theorem. A menu can cost much
more than one sampled coupling attempt, so this dominance alone is not a
cost/success obstruction. The strongest cells show exact finite
concentration but are each explained by a menu of 6, 34, or 104 direct gcds.
They do not provide a public parameter-density law.

## Cost and scope

Each rule row retains source generation, extremum setup, inverse-modulo-`L`,
fair-bit rejection, accepted rank evaluations, gcd work, endpoint failures,
factor witnesses, and exact expected operation counts over uniform `k`.
Direct controls and full menus have separate cost vectors and never alter the
coupled outcome. Offline prime factors only label a proper gcd after it is
computed.

The later unpromoted `ALGEBRA.md` proposes sharper controls for the fifth rule,
including a four-value half-window menu. Those statements did not choose or
change this frozen search and require their separately requested finite check
before dependency use.

The results are exact only for the retained cells. They do not rule out a
different nonuniform jump, parameter source, nonlinear transcript, shifted
rank, partial output, or variable-duration Las Vegas procedure.

## Evidence

- Design: `COUPLING_SEARCH.md`, SHA-256
  `50f50d5c75e68388d0ce62ebcc8371d2525c5270165b10f559c5105a67e1a0f5`.
- Author return-map note: `RETURN_MAP_JUMPS.md`, SHA-256
  `cbe3426744bb0d263a4439afdcd0847d7f1fe6992a18217914b2f857c970b8a8`.
- Independent finite prerequisite: `CHECKS_REPORT.md`, `return_map_checks.py`,
  `check_output.json`, and `check_SHA256SUMS.txt`.
- Search source: `coupling_search.py`, SHA-256
  `c7cedb00a566b850a265dfd7312810166b2c54ee21bc7c027d38bc26a5d51c6c`.
- Search outputs: `search_pilot_output.json`, `search_N209_output.json`,
  `search_N1333_output.json`, `search_N10807_output.json`, and
  `search_aggregate_output.json`, with their status and log files.
- Resource record: `SEARCH_RESOURCE.md`. `search_SHA256SUMS.txt` covers the
  search source, report, resources, and all search artifacts.
