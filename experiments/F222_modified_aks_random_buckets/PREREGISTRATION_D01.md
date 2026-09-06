# F222-D01 preregistration — modified-AKS coefficient factor search

## Fixed question

For balanced semiprimes

\[
N=pq,\qquad p<q<2p,
\]

measure the exact shift probability that the global coefficient vector

\[
E_a(X)=(X+a)^N-X^N-a^N\pmod{X^r-1,N}
\]

contains a coefficient with proper gcd with `N`.  F222 proves an exponential
bounded-gap obstruction for local nullity with a fresh uniform unit shift.
It does not cover this raw coefficient-gcd channel.

The run is finite discovery and counterexample evidence.  It cannot prove an
unbounded probability bound or a factoring algorithm.

## Frozen cohorts

The source generates consecutive prime pairs `(p,q)` and keeps those with
`5 <= p <= 500` and `q < 2*p`.  It reports every pair and also groups rows by
the exact gap `d=q-p`.

The modulus bank is

`r in {3,5,7,11,13,17,19,23,29,31}`

with rows omitted when `gcd(r,N) != 1`.

For every retained `(p,q,r)`, the source exhaustively tests every unit shift
`a mod N`.  This is feasible because it avoids exponentiation by using the
integer-specific Frobenius formula modulo each hidden prime.  Hidden factors
are used only to label the two local coefficient vectors and their mismatch.

## Exact local construction

Modulo `p`, put `d=q-p` and form

\[
h_{q,a}(X)=
X^p((X+a)^d-X^d)+a((X+a)^d-a^d)\pmod{X^r-1,p}.
\]

Then Frobenius permutes coefficient positions by multiplication by `p mod r`:
`E_a mod p = h_(q,a)^p`.  The source uses the analogous direct binomial
construction for `h_(p,a)` modulo `q`, followed by the `q mod r` permutation.
It asserts both against direct modular binomial coefficients on a frozen
small validation set before the main run.

A coefficient gives a proper gcd exactly when its zero status differs between
the two local vectors.  The row success count is therefore the number of unit
shifts for which the two zero-support sets differ.

## Frozen outputs and interpretation

For every `(p,q,r)`, report:

- exact numerator and denominator of the coefficient-factor probability;
- the smallest successful shift, or null;
- minimum, maximum, and mean local support sizes;
- whether all unit shifts have synchronized zero supports.

For every gap and modulus, report the maximum and minimum exact probabilities,
the number of zero-probability rows, and the largest tested `p` with zero
probability.

The primary discovery questions are:

1. Does any fixed small `r` have a positive constant lower envelope over the
   tested balanced inputs?
2. Do fixed-gap rows show probability proportional to `r*d/p`, matching the
   scale of the annihilation obstruction?
3. Are there explicit rows where every unit shift has synchronized supports?

Interpretation is fixed as follows.

- A zero-probability row kills universality of that exact `(r, uniform-shift,
  coefficient-gcd)` source.
- If one `r` has a positive minimum across this finite cohort, call it a finite
  lead only.
- Otherwise call the fixed bank a finite null.
- No fitted asymptotic law is promoted as a theorem.

## Frozen budget and remote safety

- Run ID: `F222-D01`.
- Remote alias: `seetacloud`.
- Remote directory: `/root/IntegerFactoring_F222/F222-D01`.
- Runtime: `/root/miniconda3/bin/python`, version 3.12.3.
- Dependencies: Python standard library only.
- Timeout: 900 seconds.
- CPU: one Python process and no worker processes.
- Address-space cap: 2 GiB.
- Estimated peak memory: below 256 MiB.
- Estimated disk: below 20 MiB.

The preflight found 32 CPUs, 503 GiB RAM, 367 GiB available RAM, 22 GiB free
disk, and load average about 56.  The visible container had no CPU-heavy user
process.  The one-process and 2-GiB caps are mandatory.

## Exact launch workflow

Freeze and hash this preregistration, the source, and the runner.  Copy only
the frozen source and runner to the declared remote directory.  The remote
command must print both hashes before running the runner.  Retrieve the log
and JSON output without modifying the frozen inputs.  Do not retry with a
changed cohort, source, command, dependency, or timeout under this run ID.
