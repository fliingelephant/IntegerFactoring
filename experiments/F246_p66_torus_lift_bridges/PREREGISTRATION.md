# F246 preregistration — two live P66 bridges

## Purpose

Test two exact public sources of positive integers with known square roots
modulo a balanced semiprime:

1. norm-one quadratic-torus coordinates;
2. scalar high-digit lifts modulo `N^2`.

Every retained list is decoded by the complete factor-free P66 gcd-free
parity decoder.  This is a finite discovery scan.  It is not a proof of an
asymptotic success law.

This file is frozen before the first execution of `scan.py`.

## Frozen cohorts

The cohort seed is

`F246-p66-live-bridges-cohort-v1`.

Use these target bit lengths and eight inputs at each length:

- training: `20, 24, 28` bits;
- held-out: `32, 36, 40` bits.

For target length `n`, both hidden primes are generated in
`[2^(n/2-1),2^(n/2))`.  The script uses SHA-256 candidate streams and the
deterministic Miller--Rabin bases stated in the source.  It accepts only
distinct primes `p<q<2p` for which `pq` has exactly `n` bits.  It rejects a
duplicate modulus.  The factors define the verifier cohort only.  No source
or decoder function receives them.

The script completes and writes the training cohort before it starts the
held-out cohort.  No parameter changes are permitted between the two parts.

## Frozen pseudorandom source

The source seed is

`F246-p66-live-bridges-source-v1`.

Each input and source label gets a separate SHA-256 counter stream.  A draw
modulo `m` uses rejection above the largest multiple of `m` below `2^256`.
This removes reduction bias.  The stream is reproducible.  It is a finite
pseudorandom experiment, not a proof about truly random samples.

## Arm A: torus norm integers

Use the fixed signed discriminant menu

`D in {-1, 2, 3, 5, 7, 11}`.

Replace `D` by its canonical residue `D0 in {1,...,N-1}` for integer-value
construction.  First compute `gcd(D0,N)`.  A proper value is a direct factor.

For each `D`, collect exactly 32 accepted Hilbert--90 points.  Draw
`a,b` uniformly modulo `N`.  Apply the public coefficient screen

`gcd(N,a,b)`

and the public norm screen

`gcd(a^2-D0*b^2,N)`.

A proper gcd is logged as a direct factor.  A global zero is rejected.  A
unit norm gives the exact norm-one point

`U=(x,y)=((a^2+D0*b^2)/nu, 2ab/nu) mod N`.

Abort the run if one `(N,D)` needs more than 4096 coefficient attempts.  Do
not reduce the sample count.

From each accepted `U`, construct three public points:

- `raw`: `V=U`;
- `p208_w1`: `V=U^(N-J)`, where `J=Jacobi(D0,N)`;
- `p209`: `V=U^(N^2-1)`.

For every `V=(x,y)`, compute both signed-identity screens

`G_plus=gcd(N,x-1,y)` and `G_minus=gcd(N,x+1,y)`.

A proper value is a direct factor.  If `G_plus=N`, run the full public
two-primary Miller square chain for the same exponent and log any proper
factor separately.  Global `+1` and `-1` points have `y=0` and give the
trivial integer 1.  Do not send them to P66.

Only points with `G_plus=G_minus=1` enter the genuine failed-return P66 bank.
For each such point retain

`A=1+D0*y^2`, with supplied root `x mod N`.

Verify `x^2=A mod N` and screen `gcd(x,N)` before admission.

## Arm B: scalar high-digit lifts

Collect exactly 192 public unit bases `a` for each `N`.  Draw each base
uniformly modulo `N`, compute `gcd(a,N)`, log a proper factor, and reject
zero or a nonunit.  Abort after 4096 attempts.  Use the same accepted bases
for both exponents

- `nm1`: `E=N-1`;
- `n2m1`: `E=N^2-1`.

Both exponents are even.  Compute

`L_E(a)=a^E mod N^2`,

as the least positive residue, with supplied root

`r_E(a)=a^(E/2) mod N`.

Verify `r_E(a)^2=L_E(a) mod N` and `gcd(r_E(a),N)=1`.

Before P66, compute `gcd(L_E(a)-1,N)` and
`gcd(L_E(a)+1,N)`.  A proper value is a direct endpoint factor and that row
is not admitted.  If `L_E(a)=1 mod N`, test
`gcd(r_E(a)-1,N)` and `gcd(r_E(a)+1,N)`.  A proper value is logged as a
square-root/Miller factor and that row is not admitted.  A null global
return remains an exact nonclosing relation and is admitted with a flag.

No exact-value deduplication is allowed.  Equal integers with different
supplied roots can themselves create a useful P66 dependency.

## Frozen P66 decoder

For each ordered list `(A_i,x_i)`, apply the parity-only multiset refinement
from P66.  Start with `(A_i,2^i)`.  Whenever two current integers have gcd
`d>1`, replace them by the nonunit members

`(d,mask_1 xor mask_2)`, `(A_1/d,mask_1)`, and
`(A_2/d,mask_2)`.

Discard zero masks.  At termination the integer fragments are pairwise
coprime.  Remove an entire fragment row only when the fragment is an exact
integer square.  The remaining distinct masks are the complete parity
matrix.

Compute a deterministic full binary kernel basis.  For every basis vector
`c`, compute the exact positive root

`R=sqrt(product A_i^c_i)`

and the supplied modular root

`X=product x_i^c_i mod N`.

Test `gcd(R-X,N)` and `gcd(R+X,N)`.  A proper value is a non-global
basis-root hit.  Every claimed hit must include a replay certificate and
must pass exact-square, root-congruence, and divisor checks.

Run the decoder on these frozen banks:

1. each of the 18 atomic `(D,torus mode)` banks;
2. each torus mode across all six `D` values;
3. each `D` across all three torus modes;
4. all torus rows;
5. each of the two lift exponents;
6. both lift exponents together;
7. the union of all torus and lift rows.

## Frozen measurements

For each input, record:

- attempted and admitted source rows;
- every direct-gcd, signed-return, and Miller-screen count;
- exact source operation counts and source wall/CPU time;

For each decoder bank, record:

- P66 columns, parity rows, rank, and kernel dimension;
- gcd-refinement work and decoder wall/CPU time;
- the number of non-global basis-root hits;
- up to three exact replay certificates;
- whether a decoder hit occurred with no earlier public factor anywhere in
  the frozen source schedule.

The aggregate report separates training and held-out results.  It also
separates screen factors from decoder factors.

## Frozen interpretation

- `strong finite signal`: at least three strict screen-free decoder hits on
  distinct held-out moduli, covering at least two held-out bit lengths;
- `weak finite signal`: at least one strict screen-free decoder hit on a
  held-out modulus;
- `null finite signal`: no strict screen-free held-out decoder hit.

A strict screen-free hit means that the P66 basis exposes a non-global root
and no public direct or Miller screen exposed a factor anywhere in that
input's frozen source schedule.

Any finite signal is guidance only.  It does not establish inverse-QP
success.  A null signal does not prove an obstruction.

## Frozen resource envelope

There are 48 moduli and at most 960 admitted rows per modulus.  The largest
bit length of one torus integer is below `3n+2`; one lift integer is below
`2n`.  The largest binary mask has 960 bits.  The 32-bank list gives
fewer than 90 million pairwise gcd scans in the simple worst-case estimate.

The expected peak memory is below 512 MiB.  The expected one-core runtime is
20 to 90 minutes.  Run one Python process only, with `nice -n 15`, a 4 GiB
address-space limit, and a three-hour hard timeout.  If a required command,
Python version, hash, cohort size, or output check fails, abort.  Do not
substitute a smaller cohort, another library, another host, or another
algorithm.
