# F226-D01 preregistration — binary-child APR orbit scan

## Purpose

Test the exact local-orbit and cross-prime compatibility supplied by
recursively factorable binary truncation children.  This is a discovery run,
not evidence for an asymptotic runtime claim.

## Cohort

For each prime `p` in `[2^9,2^14)`, and for each target ratio

`rho in {1.05, 1.25, 1.50, 1.90}`,

let `q` be the least prime at least `ceil(rho*p)`.  Keep the row when
`p<q<2p`.  Put `N=p*q` and `n=ceil(log2(N+1))`.

## Frozen calculations

For each binary level `j` with `ceil(n/2)<=j<n`, form

`A_j = N mod 2^j`.

Factor `A_j`.  For each distinct odd prime `ell|A_j`, compute

`h_ell=ord_ell(N)` and the unique local exponent class

`i_ell mod h_ell`

when `p` belongs to `<N mod ell>`.  Record local acceptance and exact
generalized-CRT compatibility.

For the top-bit child `A_{n-1}=N-2^(n-1)`, record:

1. its factorization;
2. the product of locally accepted auxiliary primes;
3. the largest product of a compatible subset whose exponent-modulus lcm is
   at most `n^4`;
4. the same compatible product without the `n^4` cap; and
5. comparison with `ceil(N^(1/4))`.

Repeat items 2–5 after pooling all distinct auxiliary primes from all frozen
levels.  A pooled prime uses its one intrinsic orbit and exponent class, so
duplicates do not add mass.

The compatible-subset optimization is exhaustive.  The cohort is small
enough that rows with more than 22 accepted distinct primes abort instead of
silently changing the calculation.

## Resources

One local SageMath process.  Runtime cap: 300 seconds.  Expected runtime:
under 60 seconds.  Expected peak memory: under 300 MiB.  The host load was
`1.60, 1.63, 1.65` before launch; `vm_stat` showed no throttled pages.

## Outputs

- machine-readable summary: `D01_OUTPUT.json`;
- process log and timing: `logs/F226-D01.log`.

