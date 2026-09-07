# F326 direct Gauss-ranked pairing

**Family:** route:F31

The construction ranks the same inverse and sign-selected residue geometry
directly, so it belongs to the retained modular-hyperbola family.

Status: exact candidate construction with independent blind reconstruction
and finite implementation checks. No quasipolynomial traversal or factoring
bound is established.

The candidate gives a direct polynomial-time reduction from FacRoot to an
odd-interval involution. Start with the unit involution of Jerabek,
arXiv:1207.5220, Lemma 4.3. Include every nonunit in its signed domain and
fix those points. The all-residue Gauss identity makes the resulting domain
odd when Jacobi(a,N)=1. Two Euclidean floor sums count its prefix exactly;
binary search gives exact rank and selection without factoring N.

`STATEMENT.md` contains only definitions, hypotheses, and requested
conclusions for blind reconstruction. `PROOF.md` contains the candidate
proof, including a derivation of the needed composite Gauss identity from
permutation signs and an explicit floor-sum recurrence.

This examination found no invalidating issue with composite moduli,
nonunits, trivial roots, rank direction, domain parity, or uniformity.
It also derives two auxiliary involutions with a unique fixed point at
coordinate zero: adjacent pairing after deleting its rank, and cyclic
rank reflection. Both create a terminating alternating path to a useful
fixed point of the arithmetic involution.

The proven elementary traversal bound remains O(N) local evaluations.
The new question is whether the ranked arithmetic path admits an efficient
shortcut or a randomized source with a sufficient cost-to-success bound.
PPA membership alone gives neither. No novelty or quasipolynomial factoring
claim is made. No computation was launched by this proof worker.

## Finite implementation evidence

direct_gauss_pairing.py implements the Euclidean floor sum, exact size,
rank, selection, arithmetic involution, all fixed-point decoders, and both
auxiliary matchings. Explicit domain lists are used only as validation
oracles. They do not enter the reported algorithm operation counts.

The small exhaustive control covers all odd N through 101 and every unit
a<=16. An independent trial-factor Jacobi oracle verifies 625 all-residue
Gauss parity instances. All 17,070 domain points in the 388
Jacobi-positive instances pass exact domain, rank/select, and F-squared
checks. Every one of 3,002 fixed points decodes to a verified divisor or
square root. Both auxiliary involutions pass on 34,140 ranks, and all 776
full alternating paths terminate at decoded fixed points. The largest
observed complete path uses 38 F calls for delete-adjacent and 37 for rank
reflection.

The public comparison reuses the eight exact F324 pairs at each of
N=209, 1333, 10807, 66013, and 256027. Only N and Jacobi-positive a enter
the new pairing; b appears only in the retained F322 references. No
offline quadratic-residue label selects an input or transition.

| Method | Runs | Completed | F or r calls | Factor endpoints | Root endpoints |
|---|---:|---:|---:|---:|---:|
| Direct delete-adjacent | 40 | 40 | 6,741 | 36 | 4 |
| Direct rank reflection | 40 | 40 | 4,250 | 39 | 1 |
| F322 adjacent reference | 40 | 40 | 3,826 | 39 | 1 |
| F322 negation reference | 40 | 29 | 117,888 | 18 | 11 |

The F322 negation total includes eleven paths censored at the retained
F324 cap. The direct methods have no censors; their largest observed paths
use 1,333 and 516 calls respectively. These methods use different domains
and local-evaluation costs, so the table is a finite operational comparison,
not a uniform speedup claim.

The separate Rabin mode draws its hidden candidate uniformly from
1,...,N-1. A proper generation gcd returns immediately. Otherwise the
solver receives only N, a=r^2 modulo N, an independent matching coin, and
the public cap. The hidden r is retained outside the solver until final
root decoding. Across 32 seeded trials at each of the five moduli, all 160
trials return verified factors: eight during hidden-unit generation, 151
directly from fixed points, and one from a returned-root difference gcd.
The 152 solver calls use 18,646 F evaluations and have no censors. This
finite sample does not prove a lower bound on valid-output probability or
an expected quasipolynomial cost.

The four main runs take 0.123, 0.339, 0.038, and 0.807 seconds. Their
largest peak RSS is 61,603,840 bytes. Every run uses an internal 28-second
alarm, external 30-second timeout, and 512 MiB ceiling. RESOURCE.md and
the named JSON outputs, logs, status files, and checksums retain exact
scope and resource evidence.
