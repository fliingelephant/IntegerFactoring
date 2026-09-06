# F205-D01 preregistration — joint half-child selector search

## Closest prior routes and material difference

The closest prior routes are P165/F187 and F202. P165 recursively factors
`(N-1)/2` and proves that independent uniform bases still have exponentially
small useful-return probability on bounded-gap semiprimes. F202 recursively
factors `E=N-floor(sqrt(N))^2` and proves that its literal congruence, genus,
ramified-class, and second-principal-norm routes need not orient the factors.

F205-D01 differs by giving one public feature constructor both complete child
factorizations at once. It tests joint integer statistics, rather than either
child in isolation. It also tests the exact recurrence shape

`T(n) <= T(n-1) + Q(n) T(ceil(rho*n)) + Q(n)`.

The recurrence is handled symbolically. D01 is only a finite discovery and
counterexample search for the joint postprocessor.

## Fixed question

For balanced squarefree semiprimes `N=p*q` with `p<q<2p` and `N == 3 mod 4`,
let

- `B=floor(sqrt(N))`,
- `K=(N-1)/2`, and
- `E=N-B^2`.

Assume the complete prime factorizations of `K` and `E` are public. Search for
a public rule that does at least one of these tasks:

1. predicts the first nontrivial bit of `p^(-1) mod 4`;
2. predicts the equivalent sign of the P179 `chi_4` twisted divisor term;
3. produces a proper gcd through a fixed joint base/exponent bank;
4. predicts whether the gap coordinate `d=p+q-2B` is supported on primes of
   `2*K*E`;
5. predicts whether the F202 mixed class is principal, as certified by a
   second mixed representation `N=x^2+E*y^2`; or
6. supplies a split-prime or ordinary common-order transition.

The factor pair is used only in `hidden_labels`. The function `public_record`
accepts only `N`. It constructs every feature and every gcd certificate from
`N`, `B`, and the complete factorizations of `K` and `E`.

## Input cohorts fixed before the run

- Training: 5,000 deterministic pseudorandom accepted inputs. The smaller
  factor has 12 through 17 bits. Seed: `20501`.
- Holdout: 2,500 deterministic pseudorandom accepted inputs. The smaller
  factor has 18 through 23 bits. Seed: `20502`.
- Small counterexample scan: all accepted prime pairs with `p <= 1000`.
- Frozen prior witness: `N=2627=37*71` is evaluated separately.

Acceptance uses only the declared promise `p<q<2p` and the public condition
`N == 3 mod 4`. It does not balance, filter, or resample by the target bit or
by any tested outcome.

## Public feature family fixed before the run

The source constructs these features.

- residues modulo 4, 8, and 16 of `N,B,K,E,M,R`, where
  `M=lcm(K,E)` and `R^2 == N mod M` is the CRT root obtained from the two
  child factorizations;
- `omega`, `Omega`, residue-class counts, smallest and largest prime factors,
  radical, Euler phi, Carmichael lambda, ordinary divisor sum, and the
  `chi_4`-twisted divisor sum of `K`, `E`, and `M`;
- gcd and size statistics involving `B-1`, `B+1`, `K`, `E`, and their overlap;
- split, inert, ramified, and Jacobi-sign counts for child-support primes in
  the order of discriminant `-4E`;
- fixed signs, parities, comparisons, residue indicators, and fixed-quantile
  decision stumps derived from the preceding scalar values.

The direct bank uses only public bases drawn from

`2,3,5,B,K,E,M,R`, the child arithmetic functions above, and at most the 12
smallest plus 12 largest child-support primes.

It uses public exponents drawn from

`N-1,K,E,M`, the radicals, phi values, lambda values, and one-prime quotients
of `N-1`, `E`, and `M`. It tests `gcd(a^e-1,N)`, `gcd(a^e+1,N)`, and the
P165 factor-first stripping procedure after a global return to exponent
`N-1`.

The bank stops at its first proper gcd. This does not affect its null cases.

## Rule selection and holdout

The primary selector cohort contains only public coprime-square-gap inputs on
which the fixed direct bank did not factor. For every predeclared binary
feature and every scalar stump at the 10%, 25%, 50%, 75%, and 90% training
quantiles, training selects the prediction orientation. The single rule with
best training balanced accuracy is frozen by lexicographic tie-break before
holdout scoring.

The output reports training and holdout accuracy, balanced accuracy, label
balance, every holdout error of the selected rule up to the stored cap, and
the smallest error. A rule with one error is not a universal selector. A
finite perfect holdout is discovery evidence only.

The fixed interpretation thresholds are:

- zero holdout errors: an exact finite selector candidate, still not a proof;
- holdout balanced accuracy at least 0.60: a correlation lead;
- holdout balanced accuracy below 0.55: a null for this fixed feature family;
- a value in `[0.55,0.60)` with an error: weak and inconclusive.

Any fixed-bank failure refutes universality of that exact bank. Any exact
`d`-support, no-split-support, or no-second-norm witness refutes only its
corresponding universal auxiliary claim.

## Preserved nulls and counterexamples

The output preserves the smallest observed examples of:

- failure of the fixed direct bank;
- failure of prime support of `d` by `2*K*E`;
- no split prime from `K` for discriminant `-4E`;
- no second mixed principal norm representation; and
- ordinary common-order capacity `gcd(p-1,q-1) <= 2`.

The complete train and holdout rows are written as gzip-compressed JSONL.
Finite evidence will not be promoted as an unbounded theorem.

## Run budget and remote safety

- Family and run ID: `F205-D01`.
- Remote alias: `seetacloud` from the local SSH configuration.
- Remote working directory: `/root/IntegerFactoring_F205/F205-D01`.
- Runtime: `/root/miniconda3/bin/python` with SymPy and NumPy already present.
- Timeout: 900 seconds.
- Concurrency: one Python process; no worker processes.
- Estimated peak memory: below 1 GiB.
- Estimated disk: below 100 MiB.

Before preregistration, the host reported 32 CPUs, 503 GiB RAM, 367 GiB
available RAM, and 22 GiB free disk. The host load average was about 56, while
the visible container had no CPU-intensive process. The single-process cap is
intended to avoid material load pressure.
