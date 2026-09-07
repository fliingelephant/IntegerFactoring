# F334 gcd-screened count descent

**Family:** route:F31  
**Status:** completed finite experiment; no asymptotic probability or factoring
claim.

## Protocol

The candidate starts at t=(N-1)/2. At each stage it gcd-screens t, computes
q=Q_a(t) with the frozen F326 floor sum, gcd-screens every nonzero value among
q and t-q, fails on an empty side, and otherwise replaces t by
min(q,t-q). It stops with failure when the new t is at most one. The identity

    min(q,t-q) = (t-|2q-t|)/2

was checked at every stage. Thus every continuing stage halves t and every
trajectory has O(log N) count calls.

Three paired methods use the same initial Jacobi-positive unit a:

1. fixed_multiplier keeps a and starts at h;
2. fresh_multiplier starts with that a and samples a new public
   Jacobi-positive unit at each later stage;
3. inverse_start_fixed_multiplier keeps a but starts at
   min(a^(-1) mod N, N-a^(-1) mod N).

Initial sampling uses exact fair-bit rejection on 1,...,N-1. Jacobi-negative
units are charged retries. A nonunit draw ends a separate factor-success
attempt. Sampling continues only to obtain the requested number of conditional
Jacobi-positive parameters. No trajectory work is charged to an earlier
generation-factor attempt. The conditional denominator is therefore 256 per
scale input. The generation-inclusive denominator adds the separate factor
events.

Fresh-mode inner streams have independent derived seeds for each pair
(modulus, accepted-index). They are reproducible finite randomness. The small
fixed and inverse-start controls enumerate all eligible a. The small fresh
control uses one independent reproducible inner stream per enumerated a and is
not exhaustive over its inner randomness.

The direct menu for cutoff D tests the deduplicated union of all integer
candidates in

    [t0/2^(j+1)-D, t0/2^(j+1)+D/2] intersect [1,h].

The fixed-start menu has t0=h and depends only on N. The inverse-start menu
uses its public parameter-dependent t0 and is reported separately. Every
retained candidate is gcd-screened and charged. A trajectory whose observed
maximum defect exceeds D is recorded as outside the cutoff. A menu miss is
not a descent failure.

## Validation

CountOracle directly aliases the frozen F326 GaussPairing.floor_sum, K, and Q
method objects. No Gauss domain or full graph is enumerated. On every small
stage, direct enumeration independently checked Q and both signed-remainder
count identities. On every small and scale stage, the run checked:

- all recorded gcd values and all returned divisors;
- the halving and defect-child identities;
- |2Q_a(t)-t| <= |rep(a*t)|;
- |2Q_a(t)-t| <= 10 S(a,N), with S computed by Euclid;
- the exact first inverse-start count at signed remainder 1 or -1; and
- containment of every observed bounded-defect child in its public menu.

The first inverse-start child factor was labeled by whether it divides a-1 or
a+1. Offline F328 factors were attached only after a public gcd returned.
They never selected a parameter, state, menu candidate, branch, or stopping
rule.

All pilot, exact-small, twelve scale, and aggregate jobs passed. There were no
time censors. Empty-side and t-at-most-one outcomes below are algorithmic
stopping failures.

## Exact small control

There are 25 odd composite N at most 101 and 547 Jacobi-positive units in
total. Fixed and inverse-start success counts are exact over this finite
conditional set:

- fixed: 341/547;
- fresh: 437/547, comprising 277 count gcds and 160 fresh-generation gcds;
- inverse-start: 272/547, comprising 168 first-count a±1 reproductions and
  104 later count gcds.

The fresh total is a one-stream-per-a finite random observation. It is not an
exact probability over fresh inner coins.

In the next table, a fresh split is count/generation, an inverse split is
first-count/later, and each cost cell is Q calls/gcd calls. Exhaustive
enumeration itself is validation work and is not charged as parameter
generation.

| N | J+ units | fixed success | fresh success | inverse success | fixed cost | fresh cost | inverse cost |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 9 | 6 | 0 | 0 (0/0) | 0 (0/0) | 10/26 | 10/28 | 6/16 |
| 15 | 4 | 3 | 3 (3/0) | 1 (1/0) | 4/11 | 4/11 | 4/12 |
| 21 | 6 | 4 | 4 (4/0) | 2 (2/0) | 6/16 | 6/16 | 6/16 |
| 25 | 20 | 0 | 7 (0/7) | 4 (4/0) | 52/146 | 41/145 | 28/76 |
| 27 | 9 | 8 | 8 (7/1) | 6 (4/2) | 11/32 | 10/31 | 11/33 |
| 33 | 10 | 0 | 7 (0/7) | 0 (0/0) | 28/76 | 12/49 | 14/36 |
| 35 | 12 | 3 | 8 (0/8) | 5 (3/2) | 34/98 | 18/73 | 17/50 |
| 39 | 12 | 11 | 11 (9/2) | 8 (5/3) | 15/44 | 12/38 | 16/48 |
| 45 | 12 | 10 | 10 (10/0) | 6 (4/2) | 12/34 | 12/34 | 20/58 |
| 49 | 42 | 14 | 25 (13/12) | 8 (4/4) | 110/316 | 95/337 | 90/252 |
| 51 | 16 | 15 | 14 (13/1) | 12 (7/5) | 19/56 | 18/56 | 23/68 |
| 55 | 20 | 6 | 14 (6/8) | 6 (4/2) | 52/151 | 33/128 | 37/106 |
| 57 | 18 | 12 | 14 (7/7) | 4 (4/0) | 36/102 | 25/91 | 30/82 |
| 63 | 18 | 17 | 17 (17/0) | 15 (9/6) | 18/53 | 18/53 | 24/72 |
| 65 | 24 | 0 | 18 (0/18) | 6 (4/2) | 88/250 | 45/190 | 44/122 |
| 69 | 22 | 20 | 20 (17/3) | 16 (12/4) | 28/82 | 25/81 | 32/92 |
| 75 | 20 | 19 | 19 (19/0) | 16 (9/7) | 20/59 | 20/59 | 30/89 |
| 77 | 30 | 0 | 19 (0/19) | 6 (6/0) | 124/356 | 73/326 | 78/222 |
| 81 | 54 | 46 | 52 (37/15) | 34 (24/10) | 110/322 | 80/279 | 92/264 |
| 85 | 32 | 26 | 28 (20/8) | 14 (6/8) | 50/144 | 40/140 | 64/182 |
| 87 | 28 | 27 | 26 (22/4) | 23 (13/10) | 39/116 | 34/118 | 42/126 |
| 91 | 36 | 13 | 27 (15/12) | 11 (6/5) | 115/335 | 75/302 | 83/240 |
| 93 | 30 | 28 | 27 (23/4) | 24 (14/10) | 38/112 | 39/129 | 48/142 |
| 95 | 36 | 30 | 30 (15/15) | 20 (8/12) | 88/260 | 58/224 | 71/209 |
| 99 | 30 | 29 | 29 (20/9) | 25 (15/10) | 43/128 | 31/104 | 45/134 |

Total exact-small arithmetic charges were:

| method | Q calls | floor-sum calls | floor-sum Euclid iterations | gcd calls | gcd Euclid divisions | random fair bits | inversions |
|---|---:|---:|---:|---:|---:|---:|---:|
| fixed | 1,150 | 2,300 | 8,668 | 3,325 | 11,906 | 0 | 0 |
| fresh | 834 | 1,668 | 6,500 | 3,042 | 11,731 | 5,720 | 0 |
| inverse | 955 | 1,910 | 7,140 | 2,747 | 10,105 | 0 | 547 |

The per-N actual maximum defect and continued-fraction sum are shown as
defect/S for fixed, fresh, and inverse:

| N | fixed | fresh | inverse |
|---:|---:|---:|---:|
| 9 | 4/9 | 4/9 | 2/6 |
| 15 | 7/15 | 7/15 | 1/9 |
| 21 | 10/21 | 10/21 | 2/9 |
| 25 | 12/25 | 12/25 | 6/14 |
| 27 | 13/27 | 13/27 | 2/15 |
| 33 | 16/33 | 16/33 | 8/18 |
| 35 | 17/35 | 17/35 | 8/19 |
| 39 | 19/39 | 19/39 | 3/21 |
| 45 | 22/45 | 22/45 | 3/15 |
| 49 | 24/49 | 24/49 | 12/26 |
| 51 | 25/51 | 25/51 | 5/27 |
| 55 | 27/55 | 27/55 | 13/29 |
| 57 | 28/57 | 28/57 | 14/30 |
| 63 | 31/63 | 31/63 | 6/33 |
| 65 | 32/65 | 32/65 | 16/34 |
| 69 | 34/69 | 34/69 | 5/21 |
| 75 | 37/75 | 37/75 | 6/39 |
| 77 | 38/77 | 38/77 | 9/23 |
| 81 | 40/81 | 40/81 | 20/42 |
| 85 | 42/85 | 42/85 | 14/31 |
| 87 | 43/87 | 43/87 | 9/45 |
| 91 | 45/91 | 45/91 | 22/47 |
| 93 | 46/93 | 46/93 | 6/27 |
| 95 | 47/95 | 47/95 | 23/49 |
| 99 | 49/99 | 49/99 | 8/51 |

All three fixed-start menus found a factor for every small modulus. This is
expected at these cutoffs because the windows cover many of the tiny public
integers. It is a direct-menu result, not evidence for a trajectory
correlation.

## Scale results

Each of the twelve retained F328 semiprimes has 256 paired conditional initial
parameters. One additional initial generation event, before accepted index 170
of b20_i1, returned factor 919. Thus the combined conditional denominator is
3,072 and the separate generation-inclusive denominator is 3,073.

The conditional results are:

- fixed: 0/3,072;
- fresh: 52/3,072, all 52 from fresh-parameter generation gcds and zero from
  count children;
- inverse-start: 13/3,072, all from later count children and zero from the
  first-count a±1 control.

Adding the one shared initial-generation event gives generation-inclusive
counts 1/3,073, 53/3,073, and 14/3,073. These views have different meanings
and are not merged in the output.

In the next table, E/S gives empty-side/t-at-most-one failures. Cost is Q
calls/gcd calls and includes accepted initial-parameter generation for the
conditional sampled method.

| input | initial generation factors | fixed: success E/S cost | fresh: success E/S cost | inverse: success E/S cost |
|---|---:|---|---|---|
| b20_i0 | 0 | 0 93/163 4,366/13,543 | 21 136/99 4,102/20,512 | 8 94/154 3,898/12,138 |
| b20_i1 | 1 | 0 92/164 4,457/13,816 | 23 132/101 4,158/20,879 | 4 91/161 4,009/12,473 |
| b28_i0 | 0 | 0 101/155 6,456/19,763 | 4 155/97 6,372/31,855 | 1 97/158 6,085/18,654 |
| b28_i1 | 0 | 0 90/166 6,432/19,678 | 3 151/102 6,259/31,112 | 0 78/178 6,030/18,484 |
| b36_i0 | 0 | 0 96/160 8,502/25,933 | 0 147/109 8,406/41,928 | 0 90/166 8,092/24,709 |
| b36_i1 | 0 | 0 103/153 8,455/25,774 | 1 132/123 8,367/41,639 | 0 98/158 8,063/24,603 |
| b44_i0 | 0 | 0 99/157 10,482/31,856 | 0 146/110 10,390/51,794 | 0 93/163 10,107/30,737 |
| b44_i1 | 0 | 0 97/159 10,606/32,247 | 0 158/98 10,521/52,159 | 0 92/164 10,261/31,217 |
| b60_i0 | 0 | 0 104/152 14,700/44,496 | 0 152/104 14,623/72,898 | 0 99/157 14,337/43,412 |
| b60_i1 | 0 | 0 105/151 14,618/44,272 | 0 144/112 14,561/72,859 | 0 92/164 14,197/43,022 |
| b92_i0 | 0 | 0 98/158 22,766/68,731 | 0 144/112 22,698/113,080 | 0 96/160 22,350/67,485 |
| b92_i1 | 0 | 0 97/159 22,910/69,117 | 0 156/100 22,796/114,126 | 0 88/168 22,553/68,055 |

The combined charged totals are:

| method | Q calls | floor-sum calls | floor-sum Euclid iterations | gcd calls | gcd Euclid divisions | random fair bits | inversions |
|---|---:|---:|---:|---:|---:|---:|---:|
| fixed | 134,750 | 269,500 | 5,201,971 | 409,226 | 5,308,611 | 392,492 | 0 |
| fresh | 133,253 | 266,506 | 5,183,672 | 664,841 | 14,847,270 | 21,840,048 | 0 |
| inverse | 129,982 | 259,964 | 4,956,754 | 394,989 | 7,760,421 | 392,492 | 3,072 |

The separate continued-fraction validation used 84,230 Euclidean divisions
for fixed, 4,686,732 for fresh, and 84,230 for inverse-start. The output also
retains Jacobi loop counts, fair-bit trials and rejections, gcd categories,
modular-inverse Euclidean divisions, factor verifications, and per-success
costs. A zero-success conditional cell has a null cost-per-success field.

The actual per-input maximum defect and maximum observed continued-fraction
sum are:

| input | fixed defect/S | fresh defect/S | inverse defect/S |
|---|---:|---:|---:|
| b20_i0 | 780/1,576 | 6,143/39,019 | 780/1,576 |
| b20_i1 | 685/2,317 | 830/23,163 | 693/2,317 |
| b28_i0 | 3,903/7,868 | 3,903/74,689 | 3,902/7,868 |
| b28_i1 | 624/1,292 | 24,553/56,834 | 622/1,292 |
| b36_i0 | 8,128/18,111 | 16,427/681,581 | 8,125/18,111 |
| b36_i1 | 20,787/41,626 | 291,938/884,489 | 3,019/41,626 |
| b44_i0 | 1,424/3,067 | 7,361/182,876 | 1,444/3,067 |
| b44_i1 | 912/2,230 | 89,354/207,409 | 908/2,230 |
| b60_i0 | 3,859/9,738 | 157,415/10,817,953 | 3,880/9,738 |
| b60_i1 | 2,542/13,892 | 34,856/16,708,857 | 2,547/13,892 |
| b92_i0 | 12,490/27,722 | 142,775/17,381,877 | 11,080/27,722 |
| b92_i1 | 3,570/7,377 | 506,357/1,027,473 | 3,565/7,377 |

The largest observed number of count stages was 18, 26, 34, 42, 58, and 90
at 20, 28, 36, 44, 60, and 92 bits respectively. Every continuation passed
the exact halving assertion.

## Public dyadic menus

For fixed start, each entry is menu success/deduplicated candidates followed
by trajectories whose observed maximum defect stayed within D:

| input | D=8 | D=32 | D=128 |
|---|---|---|---|
| b20_i0 | 0/181; 115/256 | 0/629; 214/256 | 0/2,134; 247/256 |
| b20_i1 | 0/185; 116/256 | 0/643; 219/256 | 1/2,188; 253/256 |
| b28_i0 | 0/280; 78/256 | 0/1,025; 202/256 | 0/3,719; 239/256 |
| b28_i1 | 0/280; 73/256 | 0/1,013; 201/256 | 0/3,657; 247/256 |
| b36_i0 | 0/375; 49/256 | 0/1,401; 187/256 | 0/5,216; 232/256 |
| b36_i1 | 0/372; 40/256 | 0/1,393; 188/256 | 0/5,188; 238/256 |
| b44_i0 | 0/469; 23/256 | 0/1,777; 164/256 | 0/6,721; 232/256 |
| b44_i1 | 0/476; 19/256 | 0/1,802; 173/256 | 0/6,817; 236/256 |
| b60_i0 | 0/665; 6/256 | 0/2,564; 141/256 | 0/9,873; 231/256 |
| b60_i1 | 0/662; 6/256 | 0/2,552; 151/256 | 0/9,823; 223/256 |
| b92_i0 | 0/1,045; 0/256 | 0/4,083; 81/256 | 0/15,945; 203/256 |
| b92_i1 | 0/1,050; 0/256 | 0/4,104; 87/256 | 0/16,032; 207/256 |

The fixed menus charged 6,040, 22,986, and 87,313 gcds for D=8, 32, and
128. Only the b20_i1 D=128 menu found a factor. It did so despite all 256
fixed-multiplier descents failing.

For the parameter-dependent inverse-start menus, each entry is successful
menus/256, total gcd calls, and trajectories within D:

| input | D=8 | D=32 | D=128 |
|---|---|---|---|
| b20_i0 | 21; 42,109; 139 | 97; 143,435; 220 | 230; 475,050; 248 |
| b20_i1 | 22; 42,524; 122 | 87; 145,219; 225 | 214; 482,271; 253 |
| b28_i0 | 2; 67,651; 96 | 11; 245,572; 206 | 49; 883,569; 240 |
| b28_i1 | 4; 66,455; 78 | 11; 240,861; 205 | 33; 864,757; 248 |
| b36_i0 | 1; 91,014; 53 | 1; 339,278; 190 | 7; 1,258,608; 236 |
| b36_i1 | 0; 90,907; 46 | 2; 338,711; 189 | 7; 1,256,201; 240 |
| b44_i0 | 0; 115,738; 24 | 0; 437,931; 170 | 0; 1,653,005; 231 |
| b44_i1 | 0; 117,189; 28 | 0; 443,798; 167 | 0; 1,676,467; 238 |
| b60_i0 | 0; 166,019; 11 | 0; 638,984; 144 | 0; 2,457,125; 232 |
| b60_i1 | 0; 164,592; 7 | 0; 633,427; 158 | 0; 2,435,030; 224 |
| b92_i0 | 0; 262,625; 1 | 0; 1,025,668; 79 | 0; 4,004,094; 206 |
| b92_i1 | 0; 264,507; 0 | 0; 1,033,043; 87 | 0; 4,033,510; 207 |

Across all inputs, the inverse menus charged 1,491,330, 5,665,927, and
21,479,687 gcds. They found 50, 209, and 540 successful parameter menus.
Their gcd Euclid totals were 29,908,327, 118,019,859, and 465,030,519.
Among the 13 inverse-start descent factors, the D=8, 32, and 128 menus found
the same factor in 8, 11, and 12 cases.

The menu totals must be read with their defect flags. For example, 269 of the
3,072 inverse trajectories had an observed defect above 128. A menu miss on
one of those rows says nothing about the unrestricted descent.

## Result

The fixed-multiplier descent produced no scale factor. The fresh control
produced factors only through its additional public unit-generation gcds.
The inverse-start control produced thirteen later count factors at 20 or 28
bits, but none from its exact first-count a±1 effect. No descent method
returned a factor on either retained input at 44, 60, or 92 bits.

The direct menus explain much of the bounded-defect opportunity but become
expensive: the D=128 inverse menu used more than 21 million gcds and found no
factor at 44 bits or above. This finite experiment supplies no useful uniform
success law for P249 and no expected-quasipolynomial factoring result.
Likewise, the observed zeros do not prove an asymptotic obstruction to count
descent, fresh public parameters, inverse starts, dyadic menus, or another
off-path randomized proposal.
