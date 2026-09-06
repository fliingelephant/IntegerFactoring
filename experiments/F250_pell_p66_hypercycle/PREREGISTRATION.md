# F250 preregistration — canonical Pell P66 hypercycles

## Purpose

Test whether a short public Pell trajectory supplies a useful, nonduplicate,
multirow exact-square relation to the factor-free P66 decoder.

For a fixed positive nonsquare integer `D`, let

`epsilon_D = S_1 + T_1 sqrt(D)`

be the least positive Pell unit.  Its powers are

`epsilon_D^j = S_j + T_j sqrt(D)`.

For an odd balanced semiprime `N`, use the canonical coordinate

`y_j = T_j mod N`

and the row

`A_j = 1 + D*y_j^2`,

with supplied modular root `x_j = S_j mod N`.

This is a finite discovery and counterexample scan.  It is not proof of an
asymptotic success law.

This file and `scan.py` are frozen before any execution of the source.

## Frozen runtime

Run only on the SSH host `seetacloud`.

- Python: `/root/miniconda3/bin/python`, version at least 3.11.
- One process under `nice -n 15`.
- Virtual-memory limit: 2 GiB.
- Hard timeout: 1,800 seconds.
- Runner: `remote_run.sh`.
- Expected peak memory: below 512 MiB.
- Expected one-core runtime: below 15 minutes.

The pre-run read-only resource check observed 32 logical CPUs, 503 GiB RAM,
367 GiB available RAM, 22 GiB free disk, and load average 56.60.  The scan
uses only one low-priority process because the host is CPU-busy.

If the Python version, hash, output checks, or resource limits fail, abort.
Do not substitute a runtime, host, source, cohort, or decoder.

## Frozen cohort

The cohort seed is

`F250-pell-p66-hypercycle-cohort-v1`.

Use these target bit lengths and sixteen inputs at each length:

- training: `20, 24, 28, 32` bits;
- held-out: `36, 40, 44, 48` bits.

For target length `n`, generate both verifier primes in
`[2^(n/2-1),2^(n/2))` from separate SHA-256 streams.  Use the deterministic
64-bit Miller--Rabin bases in `scan.py`.  Accept only distinct primes `p<q`
with `q<2p` and exact `n`-bit product.  Reject duplicate moduli.

The factors only construct and label the verifier cohort.  The public row
source, cleanup, and decoder receive only `N`, `D`, and the frozen window.

Write and finish the complete training output before the held-out scan.
Do not change a parameter after viewing training data.

## Frozen source

Use the positive nonsquare menu

`D in {2, 3, 5, 6, 7, 10, 11, 13}`.

Find the least positive Pell unit by the continued-fraction recurrence in
`scan.py`.  Verify `S_1^2-D*T_1^2=1`.

For each `(N,D)`, generate powers `j=0,...,4n`.  Update the exact Pell pair
by multiplication by the fundamental unit.  Verify the Pell identity after
every update.  Reduce `S_j,T_j` modulo `N` only after the exact update.

The row window is linear in `n`; it is not claimed to be quasipolynomially
optimal.  Exact Pell coordinates have `O(n)` bits in this window.

## Frozen public cleanup

Process rows in increasing `j`.

1. The `j=0` row is `A=1`.  Remove it as the pre-wrap trivial row.
2. Compute `gcd(x_j,N)`.  Log a proper divisor and remove that row.
3. Verify `x_j^2=A_j mod N`.
4. If `A_j` is an exact integer square `R^2`, test
   `gcd(R-x_j,N)` and `gcd(R+x_j,N)`.  Log a proper divisor and remove the
   row.  Otherwise record its root class as global and remove it.
5. If the canonical coordinate `y_j` has appeared before for this `D`,
   test the supplied-root ratio through
   `gcd(x_j-x_k,N)` and `gcd(x_j+x_k,N)`, where `k` is the first retained
   occurrence.  Log a proper divisor and remove the duplicate.  Otherwise
   record its root class as global and remove the duplicate.
6. Retain every remaining row.  Do not deduplicate by exact integer value
   across different `D` values.

The script separately labels the first index `j` for which `T_j>=N`.  This
is the first coefficient wrap.  It reports retained pre-wrap and post-wrap
counts.  Pre-wrap singleton squares and all coordinate collisions are
removed by the rules above.

## Frozen tangent-triple diagnostic

For every ordered pair of distinct retained positive coordinates `(y,z)`
within one `D`, test the rational tangent coefficient

`t=(y+z)/(1-D*y*z)`.

Only exact integral `t` with `0<=abs(t)<N` is a tangent event.  Classify it
as:

- zero or a repeated coordinate;
- a new coordinate already present in the retained bank;
- an integral coordinate absent from the bank.

For every present triple, multiply its three rows, verify whether the exact
product is a square, and, when it is, run the normalized-root gcds.  This
diagnostic is kept separate from the full P66 bank.  The algebraic analysis
predicts no distinct positive-coordinate triple for the nonsquare menu.

## Frozen full P66 decoder

Use the complete factor-free gcd-refinement decoder specified in P66/P106.
Start with `(A_j,2^j)` for the retained ordered records.  Repeatedly split a
pair with gcd `g>1` into its gcd and exact cofactors with the XOR masks.
Remove zero masks.  At termination, remove exact-square fragments.  The
distinct remaining masks are the complete parity rows.

Compute a deterministic full binary kernel basis.  For each basis vector:

- multiply the selected exact rows;
- require that the product is an exact square `R^2`;
- multiply the supplied roots modulo `N` to get `X`;
- require `R^2=X^2 mod N`;
- test `gcd(R-X,N)` and `gcd(R+X,N)`.

A non-global normalized root is a P66 hit.  Store up to three exact replay
certificates per bank.  The decoder does not receive `p` or `q`.

Decode these frozen banks:

1. each individual `D` bank;
2. the union of all retained `D` banks.

## Frozen measurements

For each input and bank, record:

- total generated, pre-wrap, post-wrap, singleton-square, duplicate, and
  retained rows;
- direct-factor events from every cleanup screen;
- tangent-event classes and tangent square/root results;
- P66 columns, parity rows, rank, nullity, basis-root classes, and up to
  three replay certificates;
- source and decoder wall/CPU time;
- whether a P66 hit occurs with no earlier public cleanup factor.

The aggregate report separates training and held-out inputs, bit lengths,
individual `D` banks, and the union bank.

## Frozen interpretation

- `strong finite signal`: at least four strict screen-free P66 hits on
  distinct held-out inputs, covering at least two bit lengths.
- `weak finite signal`: at least one strict screen-free P66 hit on a held-out
  input.
- `null finite signal`: no strict screen-free held-out P66 hit.

Any finite hit is guidance only.  It does not prove inverse-QP progress or
an all-input theorem.  A null result is not an impossibility theorem.

