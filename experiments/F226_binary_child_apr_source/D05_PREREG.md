# F226-D05 preregistration — recursion-safe lower-half truncation bank

## Question

Does the exact local-orbit pattern seen in D04 survive after enforcing the
all-input recursion budget?

## Cohort

Use the frozen D01 semiprime cohort.

## Bank

For each row, use every distinct nonzero child

`A_j=N mod 2^j`, for `2<=j<=floor(n/2)`.

Each child is below `2^(n/2)`, so a numerical-QP number of recursive calls
has the safe recurrence `T(n)<=QP(n)T(ceil(n/2))+QP(n)`.  The children are
odd.  Duplicate values are evaluated once.

For every distinct auxiliary prime `ell` in the factorizations, compute
`h=ord_ell(N)`.  Accept it locally exactly when `p` belongs to `<N mod ell>`.
Compute its exact local exponent class.  Exhaustively find the largest
product of a generalized-CRT-compatible subset whose exponent-modulus lcm
is at most `n^4`.  Abort if more than 22 distinct primes accept locally.

Compare that product with `ceil(N^(1/4))`.  Preserve aggregate counts and
every failing row with full child factorizations and local records.  Do not
write successful row detail.  This keeps the output compact.

## Resources

One local SageMath process.  Runtime cap: 300 seconds.  Expected runtime:
under 90 seconds.  Expected peak memory: under 600 MiB.  Immediately before
the run, host load was `2.43, 2.11, 1.84`; `vm_stat` showed zero throttled
pages and more than 3 GiB of free plus inactive memory.

Output: `D05_OUTPUT.json`.  Log: `logs/F226-D05.log`.

