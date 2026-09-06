# F218-D01 preregistration — affine Cartier and theta fast-forward tests

## Family and purpose

Approach family: `F218_eisenstein_fastforward_boundary`.

Closest prior routes are X23/P29, F203/P179, F204/P181,
F206/P182, F215/P187, and the self-audited F217 packet.  This run is
materially different because it tests two exact consequences of the new
moving-modulus relation

\[
N=2K+1
\]

after `factor(K)` is granted:

1. an affine base-`r` Cartier recurrence from the smaller index `r+1` to
   the target `2r+1` when `K=r` is prime; and
2. a Frobenius-compressed theta-power attempt to isolate the moving
   Eisenstein coefficient.

The experiment is deterministic.  It is for discovery and exact finite
counterexamples only.  No finite survival result will be treated as an
unbounded theorem or a complexity bound.

## Input family

Enumerate every prime

\[
5\le r\le 2,000,000
\]

for which

\[
N=2r+1=pq,\qquad p<q<2p
\]

with distinct primes `p,q`.  These are exactly finite instances of the
balanced, distinct, odd semiprime, prime-`K` branch.  All factorizations in
the run are obtained by a deterministic smallest-prime-factor sieve and
are used only to evaluate the tested identities.

For each row define

\[
t_r=\sigma_1(2r+1)\bmod r,
\qquad
u_r=\sigma_1(r+1)\bmod r,
\]

and the Fermat quotients

\[
q_r(a)=\frac{a^{r-1}-1}{r}\bmod r
\quad(a=2,3),
\]

computed by modular exponentiation modulo `r^2`.

## Test A — bounded affine one-child recurrences

Split rows by `r mod 24`.  Exhaustively test these two preregistered banks
inside each residue class:

\[
t_r\equiv A u_r+B\pmod r,
\qquad |A|,|B|\le64,
\tag{A1}
\]

and

\[
t_r\equiv A u_r+B+Cq_r(2)+Dq_r(3)\pmod r,
\qquad |A|,|B|,|C|,|D|\le8.
\tag{A2}
\]

The split modulo `24` permits every fixed eta-multiplier sign or phase
class.  The Fermat quotients in (A2) are the simplest first-order
Frobenius-lift data computable in polynomial time from `r`.

For each class, preserve every row used until the candidate bank becomes
empty, the candidate count after each row, and any survivors after the
full range.  Empty output is an exact finite elimination of the declared
bounded bank only.  A survivor is a conjecture candidate only.

## Test B — affine Cartier state of order at most eight

For each input-family row with `r <= 200,000`, in increasing `r`, form

\[
b_j=\sigma_1(jr+1)\bmod r,qquad 0\le j\le17,
\]

and differences `d_j=b_(j+1)-b_j`.  Compute the exact determinant modulo
`r` of

\[
H_r=(d_{i+j})_{0\le i,j\le8}.
\]

Stop at the first nonzero determinant and preserve `r`, the factorization
of `2r+1`, all `b_j`, all `d_j`, and the determinant.  A nonzero determinant
is an exact counterexample to the auxiliary claim that every such
`r`-Cartier section obeys an affine linear recurrence of order at most
eight over `F_r`: differencing any such affine recurrence gives a
homogeneous recurrence of the same order, which forces this Hankel
determinant to vanish.

This does not address nonlinear, variable-order, or quasipolynomial-state
Cartier systems.

## Test C — theta-power Eisenstein isolation

Let

\[
\vartheta(q)=\sum_{m\in\mathbb Z}q^{m^2},
\qquad k=(r+1)/2.
\]

Frobenius gives

\[
\vartheta(q)^{2r+2}
\equiv\vartheta(q^r)^2\vartheta(q)^2\pmod r.
\]

At `N=2r+1`, compute its coefficient from

\[
R_2(N)+4R_2(r+1)+4R_2(1),
\]

where `R_2(m)=[q^m] theta(q)^2`.  On this branch `R_2(N)=0`, but the code
will compute it rather than assume it.

The odd-index coefficient of the Eisenstein projection of
`theta^(4k)` is

\[
C_k\sigma_{2k-1}(N),
\qquad
C_k=(-1)^{k+1}\frac{4k}{(2^{2k}-1)B_{2k}}.
\]

For prime `r>3`, Kummer congruence reduces `C_k` modulo `r` to
`(-1)^(k+1) 8`, and Fermat reduces `sigma_r(N)` to `sigma_1(N)`.
The code therefore records

\[
c_r=R_{2r+2}(N)-(-1)^{k+1}8t_r\pmod r.
\]

The preregistered isolation claim is `c_r=0` on the input family.  The
first nonzero `c_r`, with all terms preserved, is an exact counterexample.
Zeroes over a finite range are not a proof.

## Resources, command, and artifacts

The named source is `search.py`.  Before execution, the remote host must
record load, memory, disk, and active CPU consumers.  The planned sieve
limit is `4,000,001`, so the smallest-prime-factor array uses about 16 MB.
The bounded candidate bank and row data keep expected peak memory below
150 MB.  The expected runtime is under five minutes on one CPU core.

Run on the SSH alias `seetacloud` with a 600-second timeout.  Preserve:

- `REMOTE_RESOURCE_CHECK.log` — pre-run resource inspection;
- `RUN.log` — stdout, stderr, timing, and exit status;
- `RESULT.json` — deterministic exact output;
- `RUN_MANIFEST.md` — command lines and SHA-256 hashes.

No durable ledger is edited by this subagent.
