# F228-D01 preregistration — bounded quotient/carry APR source

## Purpose and finite scope

This discovery run tests one fixed, recursion-safe quotient menu.  It does
not prove an asymptotic success bound.  A failure row is an exact obstruction
to this menu on that input.  A favorable rate is numerical guidance only.

For an odd semiprime `N=pq`, put

```
n = bit_length(N)
B = 2^floor(n/2)
uN = Q_u B + R_u, 0 < R_u < B.
```

The cohort is the first 512 consecutive pairs `(p,q)` in the increasing
list of safe primes `r=2s+1` with `r >= 2^18`.  Primality is decided by the
deterministic 64-bit Miller--Rabin bases in the frozen source.  A row is used
only when `q<2p`; otherwise the program stops with an error instead of
changing the cohort.

For every row, the trial menu is:

- odd `u` with `1 <= u <= 255`;
- shifts `c` with `-4 <= c <= 4`;
- public exponents `i` with `0 <= i < 256`;
- squarefree-divisor cap `2^omega(W_u) <= 2^20`, where `W_u` is the product
  of the distinct odd prime divisors of all positive `Q_u+c >= 2`.

Each `Q_u+c` is factored exactly by trial division using a sieve-generated
prime table.  For each exponent `i`, define the hidden analysis product

```
C_{u,i} = product of ell | W_u with p == N^i (mod ell).
```

The run counts a trial as terminal exactly when the divisor cap passes and
some `C_{u,i}` is at least `J=ceil(N^(1/4))`.  The integer fourth root and
all threshold comparisons are exact.  Candidate products are saturated at
`J`, which preserves this predicate exactly.  The selected trial maximizes
`min(C_{u,i},J)`, with first occurrence breaking ties.  The program records
its exact compatible prime list and reconstructs the exact decimal product
of that list using base-`10^9` limbs.  It also records `omega`, the selected
`u,i`, and the exact numerator out of 128 trials.

## Decisive interpretation frozen before the run

- A row with zero successful multipliers is an exact counterexample to this
  complete fixed menu, even with hidden knowledge of the compatible subset.
- A row whose success numerator is positive but smaller than 128 shows only
  a finite input-dependent probability.
- No finite lower bound, fitted curve, or average is evidence for an
  all-input inverse-QP theorem.
- Safe-prime rows have `gcd(p-1,q-1)=2`.  Thus no odd common-primary order
  certificate can grow on this cohort.  Any terminal success in this run is
  from the APR-compatible residue product, not from an odd common-order
  contribution.
- The run does not test non-scalar APR identities, adaptive shifts, larger
  exponent banks, or multipliers outside the frozen menu.

## Resources and exact command

The remote host inspection found `/usr/bin/timeout` and `/usr/bin/g++`.
It did not find Python, Sage, or Boost headers.  The first source draft used
Boost multiprecision, but a dependency-only preflight failed before any data
run.  This preregistration and source were revised before launch to use exact
threshold saturation and a local base-`10^9` decimal formatter.  The cohort,
menu, decisive interpretation, and output certificate did not change.
The host reported 128 logical CPUs, load
about 57, 503 GiB RAM with 367 GiB available, and 22 GiB free disk.  This
run is single-threaded.  Estimated peak memory is below 64 MiB.  Estimated
runtime is below 300 seconds.

Source:
`experiments/F228_quotient_carry_apr_source/run_F228_D01.cpp`

Remote source and binary:
`/root/F228/run_F228_D01.cpp`, `/root/F228/run_F228_D01`

Timeout: 300 seconds via `/usr/bin/timeout`.

Output: `/root/F228/D01_OUTPUT.tsv`.

Log: `/root/F228/D01_RUN.log`.

Frozen remote command:

```sh
/usr/bin/g++ -O3 -std=c++17 /root/F228/run_F228_D01.cpp -o /root/F228/run_F228_D01
/usr/bin/timeout 300s /root/F228/run_F228_D01 /root/F228/D01_OUTPUT.tsv > /root/F228/D01_RUN.log 2>&1
```

The compile step and the timed run are separate named commands.  A compile
failure or timeout ends D01.  No alternate runtime or mathematical menu will
be substituted under this preregistration.
