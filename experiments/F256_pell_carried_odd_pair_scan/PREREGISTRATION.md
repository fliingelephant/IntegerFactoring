# F256 preregistration — carried odd-multiple Pell pair scan

## Purpose

Test the exact two-row square mechanism forced by canonical-wrap carries in
a public Pell trajectory.  The primary measurements are the frequency of
carried square pairs and whether any such pair has a non-global normalized
root.

This is finite discovery evidence only.  It cannot prove an inverse-QP
success probability or an all-input theorem.

This file, `ALGEBRA.md`, `scan.py`, and `remote_run.sh` are frozen before the
mathematical run.

## Frozen source and pair family

Use the positive nonsquare menu

`D in {2,3,5,6,7,10,11,13}`.

For the least positive norm-one Pell unit

`epsilon_D=S_1+T_1*sqrt(D)`, generate exact powers

`epsilon_D^j=S_j+T_j*sqrt(D)`

through `j=12*n`, where `n=bitlength(N)`.  Verify every Pell identity.  Use
the canonical public row

`y_j=T_j mod N`, `A_j=1+D*y_j^2`, `x_j=S_j mod N`.

Apply the public cleanup in increasing `j`, separately for each `D`:

1. remove a row when `gcd(x_j,N)>1`; record a proper factor if exposed;
2. verify `x_j^2=A_j mod N`;
3. remove every exact-square `A_j`, after testing both root-difference gcds;
4. remove every repeated `y_j`, after testing both supplied-root gcds against
   the first retained row with that coordinate;
5. retain every other row.

The tested odd multipliers are

`h in {3,5,7,9}`.

For every `j` with `h*j<=12*n`, admit the pair `(j,h*j)` only when both rows
are distinct retained rows.  Evaluate the frozen integer polynomials
`F_(h,D)` and `G_(h,D)` from `ALGEBRA.md` at `y_j`.  Require

`F_(h,D)(y_j)=y_(hj)+c*N`

with integer `c>=0`, and test only the carried cases `c>0`.  Verify the exact
identity

`A_j*G_(h,D)(y_j)^2-A_(hj)=N*H`,

where `H=D*c*(2*y_(hj)+c*N)`.

For each carried pair compute

`d=gcd(A_j,A_(hj))=gcd(A_j,H)`.

The pair is an exact square dependency if and only if both

`A_j/d` and `A_(hj)/d`

are exact integer squares.  For every dependency, compute its positive
integer root `R`, supplied modular root `X=x_j*x_(hj) mod N`, normalized root
`rho=R/X mod N`, and the two gcds with `R-X` and `R+X`.  Classify `rho` as
`+1`, `-1`, or `non_global`.  A non-global class must expose both verifier
prime factors.

The factors of `N` are never passed to the source, cleanup, pair generator,
square test, root classifier, or gcd decoder.

## Frozen cohort

The cohort seed is

`F256-pell-carried-odd-pair-cohort-v1`.

Generate 128 distinct balanced semiprimes at every target bit length:

- training: `20,24,28,32` bits;
- held-out: `36,40,44,48` bits.

For target length `n`, generate the two verifier primes independently in
`[2^(n/2-1),2^(n/2))` from SHA-256 streams.  Use the deterministic 64-bit
Miller--Rabin bases frozen in `scan.py`.  Accept only distinct `p<q` with
`q<2p` and exact `n`-bit product.  Reject duplicate moduli.  Split labels in
the hash stream make training and held-out cohorts disjoint.

Write and finish all 512 training records before starting the 512 held-out
records.  Do not change a parameter after reading training output.

The 12n window contains every target row for about

`12n*(1/3+1/5+1/7+1/9)`

candidate source indices per `D`, before cleanup.  The full run therefore
tests about 2.5 million structured pairs.  This size was fixed without
observing any cohort result.

## Frozen measurements

For each input and in aggregates by split, bit length, `D`, and multiplier,
record:

- generated, retained, singleton, duplicate, and nonunit rows;
- earlier public cleanup factors;
- admissible pairs, carried pairs, `d=1`, and `d>1` counts;
- which quotient-square conditions hold;
- exact square-dependency counts and normalized-root classes;
- inputs with any dependency, any non-global dependency, and any non-global
  dependency without an earlier cleanup factor;
- up to five exact dependency certificates and five non-global certificates;
- wall time, CPU time, and process peak memory.

All integer assertions are exact.  No integer factorization is used.

## Frozen interpretation

- `strong finite signal`: at least four strict screen-free non-global pair
  hits on distinct held-out inputs, at two or more held-out bit lengths;
- `weak finite signal`: at least one strict screen-free non-global pair hit
  on a held-out input;
- `global-only finite structure`: at least one held-out square dependency,
  but no held-out non-global pair;
- `null finite signal`: no held-out square dependency.

A finite hit is guidance only.  A null result is not an impossibility
theorem.

## Frozen runtime

Run only on SSH host `seetacloud` with `/root/miniconda3/bin/python` 3.11 or
newer.  Use one process under `nice -n 15`, a 2 GiB virtual-memory limit, and
a 1,800 second hard timeout.  The expected peak memory is below 512 MiB and
the expected one-core runtime is below 20 minutes.

The pre-freeze read-only check observed 128 logical CPUs, 503 GiB RAM, 367
GiB available RAM, 22 GiB free disk, and load average 55.88.  The visible
container process list was essentially idle.  The host-wide load is high,
so the run must remain one low-priority process.

The runner verifies all frozen hashes before a source self-test and before
the mathematical run.  If a hash, runtime, invariant, output count, resource
limit, or timeout check fails, abort.  Do not substitute a host, runtime,
source, cohort, window, pair menu, or interpretation.

