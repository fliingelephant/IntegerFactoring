# F328 capped random-square paths

**Family:** route:F31

The capped paths use F326's ranked inverse and sign-selected residue
involution, so they belong to the retained modular-hyperbola family.

Status: passed bounded randomized experiment. This is finite seeded evidence,
not a success-probability bound or a factoring complexity theorem.

## Outcome

All 192 planned outer trials are retained: 16 trials for each of two balanced
semiprimes at target sizes 20, 28, 36, 44, 60, and 92 bits. Each eligible trial
runs one arithmetic path for at most 2,048 F calls. The 32-, 128-, and 512-call
results are exact prefix snapshots of that same path.

The experiment returned 39 verified proper factors by cap 2,048. All 39 came
from `fixed_nonunit` endpoints. The other 153 trials remained censored. There
were no generation-gcd factors, valid-root endpoints, invalid outputs, or root
decoding failures in this sample. Zero counts are descriptive only.

| Target bits | cap 32 | cap 128 | cap 512 | cap 2,048 |
|---:|---:|---:|---:|---:|
| 20 | 1 / 32 | 8 / 32 | 18 / 32 | 31 / 32 |
| 28 | 3 / 32 | 3 / 32 | 4 / 32 | 7 / 32 |
| 36 | 0 / 32 | 0 / 32 | 0 / 32 | 1 / 32 |
| 44 | 0 / 32 | 0 / 32 | 0 / 32 | 0 / 32 |
| 60 | 0 / 32 | 0 / 32 | 0 / 32 | 0 / 32 |
| 92 | 0 / 32 | 0 / 32 | 0 / 32 | 0 / 32 |

Each entry is `verified factor successes / charged attempts`. Every
non-success in this table is a retained censor at that cap.

## Charged cost

Every total charges all 192 attempts, including censored prefixes. Setup floor
sums and the setup modular inverse are included. Each attempt also pays for one
generation gcd and exact hidden-residue sampling. A root-decoding gcd would be
charged only after a verified root; none occurred.

| Cap | Factors | Censors | F calls | F/factor | Floor iterations | Floor iterations/factor | Total gcds | Inversions | Charged seconds | Seconds/factor |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 32 | 4 | 188 | 6,110 | 1,527.5 | 6,319,050 | 1,579,762.5 | 6,114 | 6,106 | 2.089 | 0.522 |
| 128 | 11 | 181 | 23,959 | 2,178.1 | 25,608,171 | 2,328,015.5 | 23,970 | 23,948 | 8.421 | 0.766 |
| 512 | 22 | 170 | 91,009 | 4,136.8 | 99,770,912 | 4,535,041.5 | 91,031 | 90,987 | 32.812 | 1.491 |
| 2,048 | 39 | 153 | 336,576 | 8,630.2 | 394,405,596 | 10,112,964.0 | 336,615 | 336,537 | 130.348 | 3.342 |

At cap 2,048, the per-scale ratios are reported only for scales with at least
one factor success.

| Target bits | Factors | F calls | F/factor | Floor iterations/factor | Total gcds/factor | Seconds/factor |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 31 | 20,528 | 662.2 | 97,646.6 | 663.2 | 0.020 |
| 28 | 7 | 54,268 | 7,752.6 | 2,257,681.0 | 7,753.6 | 0.484 |
| 36 | 1 | 65,172 | 65,172.0 | 31,964,466.0 | 65,173.0 | 8.145 |
| 44 | 0 | 65,536 | -- | -- | -- | -- |
| 60 | 0 | 65,536 | -- | -- | -- | -- |
| 92 | 0 | 65,536 | -- | -- | -- | -- |

The independent matching coins selected `delete_adjacent` 93 times and
`rank_reflection` 99 times. At cap 2,048 they produced 18 and 21 factors,
respectively. This finite difference is not interpreted as a method ranking.

## Input generation and random sampling

`moduli.json` retains all 12 exact `(N,p,q)` rows. Sage 10.9 generated the 24
primes with proof-enabled `Integer.next_prime`. Each prime has half the target
bit length, every product has exactly the requested bit length, and the largest
prime-balance ratio is 1.187. The factors are offline labels. They validate the
input products and remain outside the arithmetic solver.

The ideal outer sampler uses rejection from fair bits. It draws
`ceil(log2(N-1))` bits, rejects values outside `0,...,N-2`, and adds one. After
a unit draw, one independent fair bit selects the auxiliary matching. The
finite implementation replaces these bits with separate, reproducibly derived
`random.Random.getrandbits` streams. It is deterministic evidence, not a claim
that a seeded pseudorandom stream is an ideal random source.

Across the 192 trials, hidden-residue rejection used one draw 132 times, two
draws 43 times, three draws 9 times, four draws 6 times, five draws once, and
six draws once. The charged totals are 12,936 hidden-sampling bits and 192
matching bits.

## Solver isolation and validation

`arithmetic_walk` has exactly the interface `(N,a,method,cap)`. It retains one
current rank and four fixed-size measurement snapshots. It does not construct
the explicit domain, keep a visited set, receive the hidden root, or receive
offline factors. It imports F326 `GaussPairing` and `auxiliary` at the frozen
source hash recorded in `aggregate_output.json`. The F326 complete walk is used
only by the tiny agreement check.

That check covers four small composite inputs and both methods. The new walk
and the frozen validated F326 walk agree in all eight cases on stopping step,
fixed coordinate, endpoint type, and decoded output. The retained aggregate was
also checked for exact trial coverage, deterministic regeneration of every
hidden draw and matching coin, `a=r^2 mod N`, exact divisibility of every
returned factor, monotone prefix costs, and persistent success after a stopping
cap. No anomaly was found.

## Resource result and scope

Sage startup peaked at 256,065,536 bytes. Ordinary Python scale jobs peaked at
28,442,624 bytes; the aggregation process peaked at 31,244,288 bytes. The
longest fresh scale job took 9.870 seconds. Every job remained single-threaded
and below its 25-second internal alarm, 30-second external timeout, and 512 MiB
measured peak-RSS limit. `RESOURCE.md` records the preflight, pilot decision,
batch sizes, and actual ranges.

The absence of observed success at 44, 60, and 92 bits does not imply zero
success probability. The data supports only the reported capped cost and
outcome counts. It does not shorten the proven `O(N)` complete-path bound and
does not establish a polynomial or quasipolynomial factoring algorithm.
