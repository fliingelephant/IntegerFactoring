# F339 algebra and continued-fraction diagnostics

**Family:** route:F31

Status: complete finite checks. All jobs passed and first_anomaly is null.
These checks do not replace independent proof reconstruction and establish no
source-mass theorem, asymptotic success law, or expected-QP algorithm.

## Frozen inputs

| Input | SHA256 |
|---|---|
| ALGEBRA.md | f16d505b234b039a85016f0c84fdb53deb02098d42692f38dbe7cd12b0d26abd |
| ALGEBRA_STATEMENT_ONLY.md | afc08f373adabe1f79314fa1d15666ac0d553e4226748d8b2ca6cf67d9ac4df6 |
| CONTINUED_FRACTIONS.md | 5e427539c31eb7924fed1448714d51e247d75b16f623f2ba7ccfc5c0f4522e77 |
| F337 random_rank_gaps.py | 187e35a09f704ce29bdce7c42820a23551801cb835a80fc32575f4732e4e08e1 |
| F339 coupling_search.py | c7cedb00a566b850a265dfd7312810166b2c54ee21bc7c027d38bc26a5d51c6c |

The checker is algebra_checks.py, SHA256
7e29fe1ca365b14102e5ffecf0d15739752b356483a8d65619634e8b9a442e71.
The aggregate output is algebra_output.json, SHA256
25190a9baa470fade31c24437500d0aa715e06378580d3b7f8ba540753a6298f.

## Generic orbit states

The full identity job enumerated every odd N<=31, every unit a, every
1<=t<N, every full-rotation phase k, and every 0<=q<L. It used direct sorted
residue arrays and incrementally built deleted-visit prefixes as the finite
oracle.

| Quantity | Count |
|---|---:|
| Odd moduli | 15 |
| Unit parameters | 212 |
| Orbit states (N,a,t) | 4,396 |
| CF conservation checks | 4,396 |
| Arbitrary-phase (k,q) discrepancy checks | 1,305,530 |
| Nonzero fifth-rule states | 3,120 |
| q=0 fifth-rule states | 1,276 |
| Accepted fifth-rule pairs | 30,216 |
| Rejected fifth-rule endpoints | 2,924 |

Every state satisfied

    S(u,L)+S(alpha,alpha+beta)=S(a,N)+2

and S(u,L)<=S(a,N). Every arbitrary-phase direct count H satisfied both
exact integer inequalities

    |H*L-q*d| <= 5*S(u,L)*L <= 5*S(a,N)*L.

For the N-linked fifth jump, every accepted or reversed pair satisfied
H<=floor(N/L), H<=d, D=s-H, the sharper direct-menu containment, and the
physical index and residue identities. The largest observed H was 2. The
largest deduplicated short menu was 6.

## Half-orbit identities through N=511

The half-orbit job checked every unit a on every odd 3<=N<=511:

| Quantity | Count |
|---|---:|
| Odd moduli | 255 |
| Unit parameters | 53,186 |
| Actual centered r=1 parameters | 510 |
| Four-menu gcd identity checks | 212,744 |
| Unit parameters with a proper half-menu factor | 9,656 |

Every parameter matched the signed centered-inverse extremum formulas,
L=N-s0*r, the actual centered jump, and the four gcd identities. For every
r>=2, the odd residual R obeyed 1<=R<2r, all four residuals were below 5r,
and their gcds matched the four quotient-menu gcds in order.

### The r=1 branch

All 510 r=1 parameters used the actual centered branch s=1. Its arguments
are 1,0,1,-1 and none yields a proper gcd. The checker never substituted the
raw quotient s0=t into this source.

For audit clarity, a separately labeled counterfactual computed what the raw
s0 four-test source would do. It found 168 factor-producing parameters, with
examples exposing factor 3. These are different-source diagnostics and are
never credited to the actual r=1 source or its costs.

### Distinct-semiprime bound

The range contains 96 products of two distinct odd primes. For each one, the
checker enumerated all phi(N)/2 centered unit indices r and checked both
prime-specific counts:

    actual_ell <= B_ell

and the resulting uniform-unit probability bound. This gives 192 per-prime
checks. The sum of actual successful-r union counts over these inputs was
2,664. The sum of all two-prime B values was 796,952. No prime-specific bound
was tight in this finite range. This confirms the inequalities only; their
large slack is retained.

### Bounded rational height

For every odd composite N<=511, offline factorization supplied only the
validation labels P and the composite class. The checker retained every
1<=x,y<=floor(P/5) in the declared numerator-then-denominator screen order.
All 174 guarded pairs were units and none produced a half-menu factor.

| Composite class | Moduli | Guarded unit pairs |
|---|---:|---:|
| Distinct semiprime | 96 | 136 |
| Prime power | 12 | 30 |
| Nonsquarefree with multiple primes | 35 | 6 |
| Squarefree with at least three primes | 16 | 2 |

The classes include repeated factors and nonsquarefree non-prime-powers. Many
least-prime-3 inputs have floor(P/5)=0 and therefore contribute no positive
guarded pair. No unknown factor selected a runtime action.

## Frozen F337 half/eighth cells

The source check retained all 168 F337 source attempts: 153 unit records and
15 generation-factor records. Every unit contributes its half and eighth
cell, for 306 cells. Duplicate public parameters remain repeated. Rebuilt
sorted arrays matched every frozen extremum and rank-map digest, and all 306
cells satisfied the continued-fraction conservation identity.

The new short-menu indicator, the fifth-rule probability over k, and the
existing basic controls are separate fields with separate costs and
denominators:

| N | scale | generation + unit records | unit short-menu successes | fifth-positive unit cells | basic 11-value cells | r=1 / q=0 | Mean fifth probability on units | Standalone short successes / 56 |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 209 | eighth | 7+49 | 13 | 10 | 6 | 0/0 | 0.03476946 | 20/56 |
| 209 | half | 7+49 | 16 | 15 | 6 | 12/0 | 0.14169096 | 23/56 |
| 1,333 | eighth | 8+48 | 5 | 3 | 4 | 0/0 | 0.00474052 | 13/56 |
| 1,333 | half | 8+48 | 1 | 1 | 1 | 10/0 | 0.00049975 | 9/56 |
| 10,807 | eighth | 0+56 | 2 | 2 | 0 | 0/0 | 0.00697896 | 2/56 |
| 10,807 | half | 0+56 | 4 | 4 | 4 | 5/0 | 0.00069393 | 4/56 |

All 35 fifth-positive cells are covered by the new short menu. The short menu
succeeds on 41 unit cells, so it also has six direct successes in cells where
the sampled fifth coupling has zero factor starts. This is expected for a
dominating menu and is a legitimate direct factor source; it is not a
per-index coupling success.

There are 27 actual r=1 half cells and no q=0 cell in this frozen corpus.
Their zero counts are retained rather than removed. The half quotient menu
and the rank-derived short menu have identical success and factor sets in all
153 half cells. The largest eighth menu has 16 tested integers.

The short rank menus charged 1,480 direct menu gcds and 9,458 total gcd
Euclidean divisions after including their standalone source/setup work.
The half quotient implementation made 242 total modular inversions, including
source transforms, and 504 actual four-menu gcd calls. Only the 126 non-r=1
unit half cells execute the four quotient gcds. All summaries retain complete
per-source denominators and null cost-per-success fields for zero cells.

## Runtime and scope

The pilot passed in 0.067 seconds at 81.3 MiB. The full identity job passed in
2.296 seconds at 41.8 MiB. The frozen-source job passed in 0.576 seconds at
186.7 MiB. No timeout, resource censor, or anomaly occurred.

These are exact finite diagnostics on the stated ranges and frozen cells.
They do not establish the author proofs, an unbounded source law, or an
expected factoring bound. The two mathematical notes and all earlier
check/search artifacts remain unchanged.
