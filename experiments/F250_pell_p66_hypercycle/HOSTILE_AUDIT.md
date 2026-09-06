# F250 hostile audit

## Verdict

**PASS for the exact algebra and the registered finite interpretation, with
two nonoperative protocol qualifications.**

The frozen source constructs the declared deterministic cohort, generates the
declared Pell rows, applies the public direct screens, and runs a complete
factor-free P66/P106 decoder.  All 1,152 decoded banks have full column rank
and zero kernel dimension.  The 64 held-out inputs have neither a cleanup
factor nor a decoder hit.  Therefore the registered held-out classification
is exactly `null finite signal`.

This is finite guidance for the frozen menu and window.  It is not an
asymptotic statement about Pell trajectories or a factoring algorithm.

Two exact protocol defects must remain attached to this verdict.

1. `PREREGISTRATION.md` requests ordered tangent pairs.  `scan.py` uses
   `retained[left_index + 1:]`, so it tests each unordered pair once.  The
   tangent formula and every event class are symmetric, so a nonzero event
   count would be smaller by a factor of two.  The actual count is zero, and
   the exact tangent lemma proves that no retained pair can contribute an
   event.  This defect does not change the frozen result.
2. The requested source measurements are not all stored per individual
   `D` bank.  The JSON records aggregate generated, pre-wrap, post-wrap,
   singleton-square, and duplicate counts.  They store only retained count
   and first-wrap index per `D`.  In particular, they do not store per-`D`
   singleton/duplicate counts or retained-pre-wrap/retained-post-wrap counts.
   The direct events retain their `D` labels.  The missing reporting does not
   affect any bank's recorded matrix, rank, nullity, or root result.

There is also one harmless loop-bound detail.  After processing `j=4n`, the
source computes the unused Pell pair at `j=4n+1` and exits without checking
that final unused update.  No row is reduced or emitted from it.

## 1. Artifact authentication

I computed the four frozen-input hashes before inspecting their contents.
They match the supplied expected values:

| Artifact | SHA-256 |
|---|---|
| `PREREGISTRATION.md` | `6da9f635db9890b7eb5552965a7dc82ad4e1196f7c53dabce61fc06222d60364` |
| `ALGEBRA.md` | `e85c8a3dd60eec764639555722360da1abaa374f5b99c443ac1676f584c6e9cc` |
| `scan.py` | `dde3bfa5075b1cfa92389bfb30b11d4d2faace2b865ba5352d7872ea0d5b4948` |
| `remote_run.sh` | `7c1ad7ca11f015e19e83c22e7337ee9858162cddbd16f0d9ecde66029e45d3fd` |

Every copied remote artifact matches the digest recorded in
`output/REMOTE_SHA256SUMS`:

| Artifact | SHA-256 |
|---|---|
| `TRAIN.jsonl` | `7c8186d607b81beb7a27ffba1c9122063264b73df95c4810de22971b00e1dca8` |
| `HELDOUT.jsonl` | `f66e01c84b602392ae0146136aaf50b386ff76a5767cef8f0c6d1313be8d7a9c` |
| `SUMMARY.json` | `cf2c046af7d99e21fbd84e20a079c678d1bba7c5b8b77936c764576a1803e833` |
| `RUN.stdout` | `9185a5e4c35512a4c3856be09c5f1481b07342668705e712d6c634480c75476d` |
| `RUN.stderr` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `WALL_SECONDS.txt` | `151797cae5e8e5798aca2def54dcd44f0dfd5213c2f2a05e21483b12d57399be` |

The local digest of `REMOTE_SHA256SUMS` itself is
`deef90abe3d41d7ea782ccbdceba2b33d5ea11c79593e50abf516dcbf592626f`.
The stderr file is empty.  The recorded wall time is 335 seconds.  The
summary reports Python 3.12.3 and a Linux maximum RSS value of 20,232 KiB,
well below the declared 512 MiB estimate and the runner's 2 GiB virtual
memory limit.

These hashes authenticate the copied byte streams.  They are not an external
attestation that the historical resource check preceded execution or that
the process ran on the named host.  The runner itself does use one
`nice -n 15` Python process under the declared timeout and memory limit.

## 2. Cohort and split reconstruction

The cohort source uses separate SHA-256 streams for the two factor labels.
It searches upward within the prescribed half-bit interval, uses the frozen
deterministic Miller--Rabin bases, sorts the factors, and rejects equal,
unbalanced, wrong-bit-length, and duplicate products.

I independently reconstructed both SHA-256 streams without importing
`scan.py`.  The resulting 64 training and 64 held-out tuples match every
recorded tuple in order.  Exact trial division independently verifies all
256 factor labels as primes.  Every product, balance inequality, exact bit
length, within-bit index, and cross-cohort uniqueness check passes.

`RUN.stdout` has 129 lines: 64 training progress lines, then 64 held-out
progress lines, then the exact JSON summary.  Thus the frozen execution
finished and wrote the complete training output before it started the
held-out output.  No parameter is learned from training data.

## 3. Pell source and public cleanup

The continued-fraction routine returns the least positive norm-one Pell unit
for every frozen nonsquare `D`.  The exact recurrence processes
`j=0,...,4n`.  It checks

\[
S_j^2-DT_j^2=1
\]

before reducing either coordinate modulo `N`.  It then supplies

\[
y_j=T_j\bmod N,\qquad x_j=S_j\bmod N,
\qquad A_j=1+Dy_j^2,
\]

and checks `x_j^2=A_j mod N` for every row that reaches the bank.

The cleanup order matches the operative rules:

1. remove `j=0`;
2. extract and remove a proper `gcd(x_j,N)` event;
3. compare every exact integer square with the supplied root and remove it;
4. compare repeated coordinates within the same `D` and remove them;
5. retain all other rows, with no cross-`D` value deduplication.

The dictionary of prior coordinates contains only retained nonsquare rows.
This is sufficient.  A repeat of a removed square has the same square
integer `A`, and a repeat of a nonunit-root row is again nonunit at the same
hidden prime.

For every output record, I checked the exact partition

\[
\text{generated}
=\text{j0 removed}+\text{root-gcd removed}
 +\text{square removed}+\text{duplicate removed}+\text{retained}.
\]

I also checked `generated=prewrap+postwrap`, the eight `j=0` removals, the
sum of the eight first-wrap indices, the sum of the eight retained counts,
and every logged direct divisor.  Each logged factor is proper and divides
the recorded modulus.

The algebraic cleanup claims are exact.  Before coefficient wrap,
`A_j=S_j^2`.  A post-wrap exact square is another nonnegative Pell solution,
so its coordinate is an earlier Pell coordinate.  Equal coordinates within
one `D` give equal exact row values.  The two root-sign gcds either factor
the semiprime or certify a global sign.  Removing the certified square and
duplicate rows therefore cannot remove a non-global P66 root class.

## 4. Tangent diagnostic

The identity behind the diagnostic is

\[
(1+Dy^2)(1+Dz^2)
=(1-Dyz)^2\left(1+D\left({y+z\over1-Dyz}\right)^2\right).
\]

For positive `y<=z` and `D>=2`, integrality implies
`Dyz-1<=y+z`.  If `y>=2`, this is impossible.  If `y=1`, the only possible
cases are `(D;y,z)=(2;1,1),(2;1,2),(3;1,1)`, up to order, and the absolute
tangent coordinate repeats an input coordinate.  Coordinate deduplication
and singleton-square cleanup remove these cases from the retained bank.

The source correctly handles sign with an absolute coordinate, bounds it by
`N`, and checks the exact product and both normalized-root gcds for a new
present coordinate.  All 128 records report zero tangent events.  The use of
unordered rather than ordered pairs is the protocol qualification stated in
the verdict; it cannot change this zero.

## 5. Factor-free P66/P106 decoder

For a bank with columns `A_i`, the code starts with `(A_i,2^i)`.  A gcd split
replaces `(a,u),(b,v)` by the nontrivial, nonzero-mask members of

\[
(\gcd(a,b),u\mathbin{\mathrm{xor}}v),\quad
(a/\gcd(a,b),u),\quad(b/\gcd(a,b),v).
\]

For each hidden prime, this preserves its valuation-parity row.  The stable
blocks are pairwise coprime at termination.  A square stable block has zero
prime-parity contribution and is removed.  Deduplicating the remaining
masks preserves the row space.  Thus the public masks have exactly the P66
kernel.

The binary elimination uses the least set bit as a pivot.  It solves free
columns in decreasing pivot order.  Each returned vector is checked against
every parity row, and rank plus basis size is checked against the number of
columns.  For a basis vector, the code verifies the exact square product,
the modular square-root congruence, the normalized 2-torsion value, and both
factor gcds.  All supplied roots that reach this code are units.

I independently replayed `D=2` on two fixed inputs with a different
global-first-pair gcd-refinement schedule:

| Split | Bits | N | Columns | Parity rows | Rank | Nullity |
|---|---:|---:|---:|---:|---:|---:|
| training | 20 | 544,967 | 72 | 89 | 72 | 0 |
| held-out | 36 | 48,295,387,579 | 130 | 155 | 130 | 0 |

Both independent results match the frozen output exactly.  This replay was a
bounded local diagnostic.  It used no factor labels and wrote no artifact.

Across all output records, I checked the bank names and column counts,
rank-nullity, basis-class totals, certificate counts, strict-hit formula,
and the linkage between per-`D` and union-bank columns.  Every check passes.

## 6. Strict metric and finite result

For each bank the implementation sets

\[
\text{strict hit}
\iff
(\text{non-global basis hit})\ \wedge\
(\text{no cleanup factor on the input}).
\]

All cleanup screens finish before any bank decoder, so this is the declared
screen-free metric.  The input-level booleans are the disjunctions of the
nine bank booleans.  The summary recomputes those booleans without changing
the threshold.

The authenticated result is:

| Split | Inputs | Inputs with cleanup factor | Inputs with decoder hit | Strict hits |
|---|---:|---:|---:|---:|
| training | 64 | 21 | 0 | 0 |
| held-out | 64 | 0 | 0 | 0 |

Every individual `D` bank and every union bank has nullity zero.  Therefore
root-sign classification is never reached by a nonempty basis vector, and
there is no hidden ambiguity behind the zero decoder-hit count.

The held-out rule requires at least one strict hit for a weak signal and at
least four across two bit lengths for a strong signal.  Zero gives the exact
registered classification `null finite signal`.  It only rejects this frozen
short canonical Pell/P66 bank as a positive empirical source.  It does not
exclude a longer window, another discriminant family, a noncanonical
coordinate, a different algebraic relation, or an all-input inverse-QP law.

## 7. Audit diagnostics and evidence limits

I ran three read-only, bounded diagnostics after the frozen run:

- an independent SHA-256 cohort reconstruction plus exact trial-division
  validation of the small verifier factors;
- the two-input `D=2` Pell/cleanup/refinement replay above;
- exhaustive JSON consistency checks over all 128 records and 1,152 banks.

An initial optional SymPy import for the primality diagnostic failed because
SymPy is not installed.  It produced no data.  I disclosed that failure and
used exact trial division instead; every factor is below `2^24`.

No diagnostic modified a frozen input or output.  This audit writes only this
file.  The finite evidence is internally authenticated and reproducible from
the frozen source, subject to the ordinary limitation that local hashes are
not signed remote-execution attestations.
