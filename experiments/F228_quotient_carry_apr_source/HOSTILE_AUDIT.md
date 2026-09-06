# F228 hostile audit

## Verdict

**FAIL.**  The exact carry identities, the odd-divisor restriction, the APR
inverse-lift equivalences, the compatible-support bound, and the harmonic
inequalities (16)--(18) survive hostile review.  Promotion is nevertheless
blocked by three defects in the frozen packet.

1. The common-primary defect `u-R_u+cB` can be zero.  Equation (8) then
   becomes a tautology against the hidden integer `D_N^odd`; zero is not an
   admissible integer-factorization child.  The advertised public,
   recursion-safe collapse needs a separate zero-defect branch, which the
   packet does not state.
2. D01 does not implement its preregistered `W_u`.  The preregistration puts
   every odd prime factor of every positive `Q_u+c` into `W_u`; the source
   deletes factors that divide `N` before applying `omega(W_u)<=20`.  This
   changes a frozen row and makes the stated D01 numerator and total false
   for the declared predicate.
3. The consequence after (18) omits the hypotheses needed to keep `Y` and
   `W` numerical-QP.  It needs numerical-QP bounds on `K`, `T`, and
   `Delta^{-1}` (and on the inverse target probability).  Equations
   (16)--(18) themselves are correct.

These are repair defects, not evidence against the surviving identities.
I did not edit a frozen theorem, source, run artifact, or durable ledger.  I
wrote only this audit.

## Frozen-input authentication

I read `MANIFEST.md` first, recomputed every listed digest, and read the
frozen files only after all 21 digests matched.  The expected and observed
SHA-256 values are identical:

| File | SHA-256 |
|---|---|
| `STATEMENT.md` | `d7b55ac83089b7b67783fe58f5669ae4ee035de8087b9303da07e9f8bb7f4f12` |
| `PROOF.md` | `9ee7b7f2b7a9c70b210eed28c6b254f2c5f9ddebbb3753431d4cac04ce48c269` |
| `SELF_AUDIT.md` | `5967451fcc4deab476dbce92d3d8f8394f447556e7eacc5c22a294aad771da50` |
| `PROVENANCE.md` | `5260fe203030413612721e045e3247a91e0191c8fc2cd4531e9be5d5377bd486` |
| `D00_INCIDENT.md` | `5a938f06b839f51d8ef0785766617a23e5ca3b8d2e21c59049d0c23b221d721e` |
| `D01_PREREG.md` | `3dc98596abf7c71191bb750b10e59901b68604bbf90fcc328551b9eda6e59e6f` |
| `run_F228_D01.cpp` | `c3ebba44df3ba098e383fa84239c81503040fcf17e8dbed42927d5e601941256` |
| `D01_OUTPUT.tsv` | `1702c92fd32dddb33a9f309e660a50ce0066c819f6d6e8837cfe134ddfdcee33` |
| `D01_RUN.log` | `942e0c411cd3685c694049a09da3c953aac1a4d9a723b5d2be095a936d74d942` |
| `D02_PREREG.md` | `337560cb1c35b78a80b026610f30fa3ce5ced1e1ed94daaca4f5954a19689f3a` |
| `run_F228_D02.cpp` | `0a1b68b31e2029fafdcf6ec7ff6bc05666c0c4485e7e5ce4ea6129ec094aa606` |
| `D02_OUTPUT.tsv` | `314ab2df46ba6b56c0a429266e050182725b4a28aa33b0b3d6b4b29ab1cd9392` |
| `D02_RUN.log` | `e38839d743941696d709fcfa5910adda6e52343027d993631c1162d6b272a6aa` |
| `D03_PREREG.md` | `040eb7a5bd5b25b271aa0c61a5f27fa380813e58ae0a4f3c01d2d54e2fbe0a67` |
| `run_F228_D03.cpp` | `af923ebe14525856c360e1f62c9a390bd4ede95031b68d5680f6feafad0288d5` |
| `D03_OUTPUT.tsv` | `a6de38c9e5a448d6dd5c1548989bd23e39787dd0054997f1e30e771901a5abc9` |
| `D03_RUN.log` | `b9fec96c9c0a5d8546c9777878a8d02978e4af06d55307971ad24bedbb0a0da2` |
| `VERIFY_PREREG.md` | `c99d60afcaf47134cf7e4211635a0bb7510324b9074bca3820b71aaf083f00d6` |
| `verify_F228.py` | `23204fb244392db96aba1c4f9868730c05437b26aa160dca2628733ffa2a5ea4` |
| `VERIFY_OUTPUT.txt` | `6ab95948da2a42e462eb601ae23f5f26a79b0fffb5ec584762fa668b8e34cd06` |
| `VERIFY_RUN.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

The observed SHA-256 of `MANIFEST.md` is
`1cf4aaed064a5676a6dd69cd22286f581559ea9952d3c469f5b675e68873992d`.
There is no separate `RESULT.md` in the manifest.  I treated the finite
guidance in `STATEMENT.md`, the three TSV files, and the run logs as the
result artifacts.

## 1. Promotion blocker: the common defect can be zero

Put

\[
E_{u,c}=u-R_u+cB.
\]

For nonzero `E_{u,c}`, its absolute value is public and has
half-plus-polylogarithmic bit length:

\[
|E_{u,c}|\le u+(|c|+1)B.
\]

It is then an admissible smaller integer.  Equation (8) really does put
every certified odd common-primary block into its factorization.  The
frozen statement does not require `E_{u,c}` to be nonzero.

A balanced-semiprime counterexample to admissibility is

\[
N=2881=43\cdot67,qquad n=12,qquad B=64,qquad u=1,qquad c=0.
\]

Here

\[
2881=45\cdot64+1,qquad A_{1,0}=45,qquad R_1=1,
\]

and

\[
D_N=\gcd(42,66)=6,qquad D_N^{\rm odd}=3,qquad E_{1,0}=0.
\]

Thus (8) reads

\[
\gcd(45,3)=3=\gcd(0,3).
\]

The equality is true, but the right side supplies no factorable public
support.  Computing it also presupposes the hidden `D_N^odd`.

This is not a merely hypothetical common block.  The public base `565` has
order three modulo both 43 and 67.  In particular,

\[
565^{45}=1\pmod {2881},
\]

while

\[
\gcd(565^{15}-1,2881)=2881,qquad
\gcd(565^5-1,2881)=1.
\]

The factored exponent 45 therefore admits a genuine global return that
strips to the common odd block 3, while the advertised defect is zero.
The packet correctly distinguishes support from the return witness, but
that distinction does not make zero an integer-factorization child.

There is a clean repair.  If `E_{u,c}=0`, then

\[
B A_{u,c}=u(N-1).
\]

Since `u` is odd, `gcd(u,B)=1`, so `B|(N-1)`.  With

\[
H=(N-1)/B,
\]

one gets `A_{u,c}=uH`.  The positive public integer `H` has at most
half-size, and the primes in `u` belong to the deterministic multiplier
bank.  A revised theorem can therefore split into `E!=0` and `E=0` cases.
The frozen theorem and proof do not state or use this branch, so their
operational “public half-size defect” conclusion is incomplete as written.

## 2. Promotion blocker: D01's source changes the registered predicate

`D01_PREREG.md` defines `W_u` as the product of all distinct odd prime
divisors of all nine positive integers `Q_u+c`.  It says that a trial is
terminal exactly when

\[
\omega(W_u)\le20
\]

and one compatible product reaches `J`.  The source first constructs that
prime union, but then deletes every `ell` with `ell|N` before computing
`omega`, the cap, or the compatible products.  The preregistration does not
define this screened `W_u` and does not declare a direct-gcd terminal before
the cap.

The difference occurs in the frozen cohort.  D01 row 90 has

\[
p=280223,\quad q=280499,\quad N=78602271277,\quad B=262144.
\]

For `u=29`,

\[
Q_u=8695472,qquad Q_u-3=8695469=31\cdot280499=31q.
\]

The union over `-4<=c<=4` has 21 distinct odd prime factors:

```
3, 5, 7, 23, 29, 31, 47, 73, 97, 109, 307, 347, 881,
1307, 3191, 6653, 8329, 8353, 23629, 280499, 4347737
```

The preregistered cap therefore rejects this multiplier.  The source
deletes `q=280499`, obtains `omega=20`, and accepts it because at `i=16`
the compatible factors include

\[
47\cdot3191=149977>J=530.
\]

An exhaustive recomputation gives 53 successes for the source's screened
predicate but 52 for the literal preregistered predicate on row 90.  Across
all 512 D01 rows, the declared predicate totals 22,961, not the frozen
22,962.  The only other direct quotient hit is row 89, `u=29`, where
`Q_u-3=31p`; both the screened and unscreened prime unions exceed the cap,
so it does not create another literal-predicate difference.

Interpreting the erased prime as an earlier direct-gcd success does not
repair the registered count.  Under that interpretation row 89 is an
additional terminal multiplier that the source does not count, and the
complete-menu total would instead be 22,963.  The frozen 22,962 is exact
only for the unstated policy “erase direct factors, ignore the direct
success, then apply the cap.”

D02 and D03 inherit the same deletion.  I exhaustively checked their 96-row
cohort and found no shifted quotient divisible by `p` or `q`, so this
specific policy mismatch does not change their recorded totals.  D01 must
nevertheless be relabeled as a screened post-gcd statistic, or a newly
preregistered run must implement the literal predicate.  The old frozen
preregistration cannot retrospectively be changed.

## 3. Promotion blocker: the tail corollary has free complexity parameters

For one prime, one residue class occurs at most `W/ell+1` times in `W`
consecutive shifts.  Equation (16) follows.  A union bound over `K` shifts,
weighted linearity of expectation, the support bound (15), and Markov's
inequality give (17) and (18) with the stated signs and constants.
Independence between different prime events is not used.

The next sentence is not valid at its stated quantifiers.  To make the
right side of (18) at most a target `epsilon`, it is enough to take both
cutoffs on the scale

\[
Y,W\ \gtrsim\ {KnT^2\over\Delta\epsilon}.
\]

Such `Y` and `W` are numerical-QP only when `K`, `T`, `Delta^{-1}`, and
`epsilon^{-1}` have numerical-QP bounds.  Theorem D introduces unrestricted
`K`, `T`, and `Delta>0`, then asserts numerical-QP cutoffs for any specified
inverse-QP target.  A super-QP `K` or `T`, or a super-QP-small `Delta`, makes
that conclusion unavailable.  A revised statement should say explicitly:
for numerical-QP `K,T`, inverse-QP positive `Delta`, and an inverse-QP
target `epsilon`, numerical-QP `Y,W` suffice.

This defect does not alter the harmonic inequalities or the stated
exclusions for biased multipliers, adaptive heavy shifts, and joint carry
processing.

## 4. Exact algebra that survives

The size and recurrence argument is sound.  Since

\[
Q_u<u2^{\lceil n/2\rceil},
\]

a positive `Q_u+c` has `n/2+polylog(n)` bits under fixed numerical-QP
multiplier and shift bounds.  For sufficiently large `n`, this is at most
`2n/3`.  A prime divisor and its `ell-1` child are no larger.  Numerical-QP
branching over `O(log n)` fixed-ratio levels remains numerical-QP.  This is
only a cost theorem conditional on a correct arbitrary-child dispatcher,
as the packet says.

Substitution of `N=KB+S` proves (4), including the carry floor and remainder
signs.  Multiplication by `B` gives

\[
B A_{u,c}=uN-R_u+cB.
\]

Modulo `N`, this gives the direct defect `R_u-cB`, so (5) has the correct
sign.  Modulo an odd `d|N-1`, it gives `u-R_u+cB`, so (6) also has the
correct sign.  Oddness is essential because `B` must be invertible modulo
`d`.

For every rational prime `r|N`, `r=1 mod D_N`.  Multiplying the prime
factors with multiplicity gives `N=1 mod D_N`, hence `D_N|N-1`.  Equation
(8) follows for the odd part.  It does not cover the common two-primary
block.  The safe-prime experiments correctly have

\[
\gcd(p-1,q-1)=2
\]

and therefore no odd common-primary capacity.

Apart from the zero-defect admissibility issue above, the global-return
scope is honest.  A certified block `ell^e` obtained from a factored
exponent divides both `A_{u,c}` and every `r-1`, so (8) puts it in the
defect.  The packet does not claim that the defect reproduces the quotient's
annihilator or return event, and it does not accept a block without a
witness.  I found no false event-equivalence or global-return distinctness
claim.

I exhaustively tested (4)--(8) for 335,372 small admissible
`(N,u,c,d)` combinations without a mismatch.  This numerical check is not
used as a proof.

## 5. APR inverse lift that survives

After the direct gcd screen, `ell|A_{u,c}` implies `ell` does not divide
`N`.  Equation (19) gives

\[
uN=a\pmod\ell,qquad a=R_u-cB.
\]

For `ell` not dividing `u`, both `u` and `a` are units modulo `ell`, and
(10) follows.  Raising to the `i`th power proves (11) in both directions.
At `i=0`, it says `p=1 mod ell`; combining this with `N=pq=a/u` gives
exactly `uq=a mod ell`, which is (12).  For `i>=1`, division gives

\[
q=(u/a)^{i-1}\pmod\ell,
\]

which is equivalent to (13).  There is no missed endpoint or sign.

Thus, inside the stated screened class `ell` not dividing `u`, compatibility
is exactly

\[
\ell\mid A_{u,c}\quad\hbox{and}\quad
\ell\mid u^ip-a^i.
\]

At `i=0`, the hidden integer is `p-1`.  At `i=1`, it can vanish only when
`p=a/u`, which directly reveals the factor.  For `i>=2`, prime valuations
exclude equality.  Primes dividing `u` are outside the inverse step and
are bounded by the public numerical-QP multiplier cap, as stated.

Every compatible prime also divides `N^i-p`.  This integer is nonzero for
all `i>=0`, including `1-p` at zero.  Its magnitude proves the strict
squarefree-support bound (15).  I exhaustively checked (10)--(13) on
1,059,453 small semiprime/prime/exponent instances without a mismatch.

## 6. Run reproduction and provenance

The frozen verifier passes unchanged:

```
PASS hashes=6 d01_rows=512 d02_rows=96 d03_rows=96
PASS d02_cap20_matches_d03_rowwise
PASS d03_safe_prime_and_selected_support_certificates=96
```

I independently compiled all three C++ sources and reran them.  The three
TSV outputs were byte-for-byte identical to the frozen files, with SHA-256
values `1702c92f...`, `314ab2df...`, and `a6de38c9...`.  The rerun summaries
also reproduced every frozen total.  This confirms that the files are
faithful outputs of the frozen source; it does not cure the D01
preregistration/source mismatch.

On the remote `seetacloud` host, the current D01--D03 source, TSV, and log
hashes all match the manifest.  The remote file chronology is also
consistent with the declared compile-then-run sequence:

| Run | Source time | Binary time | Output time |
|---|---|---|---|
| D01 | 09:45:58 | 09:46:18 | 09:46:32 |
| D02 | 09:50:30 | 09:50:43 | 09:50:57 |
| D03 | 09:53:04 | 09:53:17 | 09:53:26 |

All times are 2026-08-13 UTC+08:00.  The named remote paths currently
resolve to GNU `timeout` 8.32 and GCC 11.4.0.  I found no source-copy or
output-copy drift.  The run logs contain only program stdout, not the
invoked command, compiler digest, timeout status, or source digest, so they
do not independently attest the exact wrapper command.  D02 and D03 also
name their own source paths before execution but do not put their own source
hashes in their preregistration documents; their hashes were frozen later
in the manifest.  Current remote hashes, timestamps, and exact local
reproduction support the declared history, but this is an evidence limit.

The D00 incident is accurately disclosed.  The D01 preregistration and
source predate the accidental local run.  The surviving temporary D00
output has the same SHA-256 as D01, and the incident record predates the
remote D01 source copy and run.  Therefore the remote D01 result was known
locally before its remote execution, but the frozen menu was already fixed.
The remote run is a deterministic replication, not an independent blinded
discovery.  The packet does not hide that fact.

D02's cap-zero interpretation was too strong, exactly as the packet says.
D03 validly separates the no-cap predicate from cap pressure on the same
96 rows.  Its no-cap totals 2,754, 1,514, and 788, its cap-20 totals 524,
92, and 15, and its maximum `omega` values 29, 31, and 34 all reproduce.
No no-cap row is zero, and cap 40 equals no cap on this finite cohort.  The
packet does not extrapolate these values to an all-input lower bound.

## 7. Minor frozen presentation defect

Equation (7) contains a raw carriage-return byte between the backslash and
`m` in the intended `\rm prime` qualifier.  The surrounding prose makes the
intended definition recoverable, but the displayed TeX is malformed and
should be corrected in any revised packet.

## Final assessment

The core quotient/carry algebra is useful and largely correct.  The packet
also preserves the important distinction between common-primary support
and the global return that certifies it.  It cannot be promoted in its
frozen form.  A revision must add the zero-defect branch, close the
complexity quantifiers after (18), and either withdraw D01's exact
registered-predicate count or replace it with a genuinely preregistered
screened/direct-gcd policy and fresh evidence.
