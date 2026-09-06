# F253 hostile audit

## Verdict

**PASS, with two computation qualifications.** The class-fibre, rank,
nullity, square-subset, odd-multiple, normalized-root, and carry claims all
reconstruct. The displayed `N=4331` dependency is exact, is the first
dependency returned by the frozen V2 workflow, and has global normalized
root. It gives no factor.

The rank bound is sharp from a fibre cap alone. The displayed subset-count
bounds are valid but are not asserted or proved sharp by the theorem. In
particular, for `k=2` the fibre cap also gives

\[
Z_2\le {m(B_\Sigma-1)\over2},
\]

which is stronger than the packet's general marked-subset estimate. Thus the
word `strongest` in item 1 of `MANIFEST.md` is safe for the rank conclusion,
but it must not be read as an optimality claim for every displayed
square-subset bound.

The computation qualifications are reproducibility and invariant-hardening
issues. They do not affect the exact finite certificate. They are stated in
the computation section below.

## Authentication

All six supplied SHA-256 values match the on-disk frozen files. The task's
labels `SELF` and `MANIFEST` refer to `SELF_AUDIT.md` and `MANIFEST.md`.

| File | SHA-256 | Result |
|---|---|---|
| `STATEMENT.md` | `a9b32bd8bfdc68da9fb789ffae7640d1ae504b4ba382363a80427626a75bf2a0` | match |
| `PROOF.md` | `8e4152f81aa709138003317bfc35b713746dbdcc385517284437ad34b59e6b90` | match |
| `SELF_AUDIT.md` | `d1049f7a678ae51bf9ea8c19eda86604706ae1f7cbad93c73d34f42170b0ccaf` | match |
| `PROVENANCE.md` | `dbfb371a979b919e383686c125eca1c95d77bc68baf33594191b5d8b17d0dc39` | match |
| `COMPUTATION.md` | `9ed4823c56462470b8e816af540e8494331b73560c857a709c35207e95b96415` | match |
| `MANIFEST.md` | `dc12ba42c05adc0c84ab693c99464a9a79887dc73f2b91c2b04229a5be37fa65` | match |

The seven subordinate computation hashes in `MANIFEST.md` also match their
files.

## Independent mathematical reconstruction

### 1. Class fibres

Every positive rational square class has one positive squarefree integer
representative `a`. For a positive integer `A`,

\[
[A]=[a]\quad\Longleftrightarrow\quad A=au^2
\quad\Longleftrightarrow\quad aA=(au)^2
\]

for an integer `u`. Fixing `a` and one `D`, P214 therefore bounds the
coordinates in that class by `B_D`. No repeated coordinate within a fixed
`D` converts this coordinate bound into the same row bound. Summing over
the finite menu gives the simultaneous deterministic fibre cap

\[
\#\{i:v_i=v\}\le B_\Sigma.
\]

This use of P214 is valid even though the class is identified
retrospectively: P214 is uniform over every fixed positive integer, not a
probabilistic statement requiring one class to be preregistered.

Removing exact-square singleton rows removes the zero class. Since an
`r`-dimensional span has only `2^r-1` nonzero elements,

\[
m\le B_\Sigma(2^r-1).
\]

The stated ceiling bound for `r` and upper bound for `d=m-r` follow. No
lower bound on `d` follows: arbitrarily many independent nonzero abstract
vectors have fibre size one and nullity zero.

### 2. Abstract sharpness and the retrospective quantifier

Take `B` labelled copies of every nonzero vector of
`\mathbb F_2^r`. The fibre cap is `B`, the rank is `r`, and

\[
m=B(2^r-1).
\]

This proves exact sharpness of the rank inequality at the level of fibre
information. It does not claim that a Pell bank realizes the construction.

An exposed final circuit member has one target class determined by an
earlier subset. P214 bounds closers for each fixed target. It does not
replace the up to `2^r` targets represented by the earlier span with one
target. Greedy-basis and circuit-pivot orderings do not change this
quantifier. The packet correctly refuses to infer an inverse-QP
retrospective bound.

### 3. Square subsets

For each zero-sum `k`-subset, mark one of its `k` members. After fixing the
other `k-1` members, the marked member must lie in one prescribed class,
which has at most `B_\Sigma` rows. Ignoring the exclusion of the already
selected rows only enlarges the count. Hence

\[
kZ_k\le B_\Sigma {m\choose k-1}.
\]

Division by `k{m\choose k}` gives the stated
`B_\Sigma/(m-k+1)` probability. This counts all dependencies, not only
minimal circuits.

The subset-to-class map from `\mathbb F_2^m` is surjective onto a space of
dimension `r`. Its kernel has `2^{m-r}` elements. A uniformly random subset
is therefore square with exact probability `2^{-r}`, and the rank bound
gives the stated relaxation `B_\Sigma/(m+B_\Sigma)`. Utility is a subset of
exact-square closure, so these are valid upper bounds for useful subsets.
They neither force a dependency nor control its normalized-root image.

### 4. Odd-multiple identity

For odd `k`, separating the even and odd binomial terms in
`(X+Y\sqrt D)^k` leaves only even powers of `X` after respectively factoring
one `X` or one `\sqrt D`. Substitution of `X^2=1+DY^2` gives the integer
polynomials displayed in `PROOF.md` and

\[
(X+Y\sqrt D)^k=XG_{k,D}(Y)+F_{k,D}(Y)\sqrt D.
\]

Taking norms gives

\[
1+DF_{k,D}(Y)^2=(1+DY^2)G_{k,D}(Y)^2.
\]

For `k=3`, direct expansion gives

\[
F_{3,D}(Y)=Y(3+4DY^2),\qquad G_{3,D}(Y)=1+4DY^2.
\]

Applying the identity to `\epsilon^j=S_j+T_j\sqrt D`, then reducing modulo
`N`, gives

\[
y_{kj}\equiv F_{k,D}(y_j),\qquad
x_{kj}\equiv x_jG_{k,D}(y_j)\pmod N.
\]

The coefficients of `F` are nonnegative. The no-carry hypothesis
`F_{k,D}(y_j)<N` therefore turns the first congruence into equality of
canonical representatives. The norm identity then gives

\[
A_{kj}=A_jG_{k,D}(y_j)^2,
\qquad
A_jA_{kj}=(A_jG_{k,D}(y_j))^2.
\]

If both supplied roots are units, their product is congruent to the positive
exact root. The normalized root is `+1`. The normalized-root map is a
homomorphism on the parity kernel, so every span generated by these clean
pair vectors also maps to `+1`.

### 5. Carry boundary

Canonical reduction uniquely gives

\[
F_{k,D}(y_j)=y_{kj}+cN,qquad c\ge0.
\]

Substitution into the norm identity yields exactly

\[
A_jG_{k,D}(y_j)^2-A_{kj}=DcN(2y_{kj}+cN).
\]

For `c>0`, the clean polynomial witness is broken by a positive multiple of
`N`, while its modular congruence survives. This does not prove that the two
integer square classes can never coincide for another reason; the proof
correctly says that the exact relation *need not* survive. Carried
specializations, other arithmetic coincidences, and cross-family relations
remain uncontrolled. The packet makes no frequency or factoring claim for
that residual kernel.

## Finite computation and provenance

The frozen V2 transformation inserts the declared screen-free condition at
the unique occurrence of the dependency search. Replaying that exact source
transformation independently returned

```text
N=4331, p=61, q=71, support_j=[17, 51],
generated=4486, retained=3344, tested=98,
earlier_screens=[].
```

The elapsed-time field naturally differed. The durable output was a
post-run transcription, not a raw captured log; `COMPUTATION.md` discloses
this. The literal wrapper also depends on the absent absolute temporary path
`/private/tmp/pell_orbit_circuit_search.py`. Copying the authenticated
`search.py` there, or applying its single authenticated textual replacement
in memory, is required for replay. This disclosed path dependency prevents a
one-command archival replay but does not change the executed logic.

Trial division is complete in the frozen range. Here `p<=500`, `q<2p`, and
`y<N`, so `A=1+2y^2<1+2N^2` and `sqrt(A)<10^6`. The frozen prime table
therefore suffices for exact parity classes. Binary elimination correctly
returns the first dependent retained column.

One additional source-hardening defect is present. `search.py` treats only
`1<gcd(x,N)<N` as a nonunit branch; it does not assert `gcd(x,N)=1` before
retaining the row. The rare value `gcd(x,N)=N` occurs elsewhere in the
frozen scan, for example at `N=209`, `j=15`. Such a row has no normalized
root and should be rejected or should stop the run under the full F250
invariant. This did not create an earlier returned dependency. It also does
not affect the selected modulus: an independent scan of all
`0<=j<=52` for `N=4331` found every supplied root to be a unit. The selected
certificate and its screen-free classification are therefore unchanged.

For `N=4331`, direct recurrence and cleanup reconstruction gave no proper
root, singleton-square, or duplicate-coordinate gcd in the complete frozen
window. It retained 47 rows for that modulus and returned `[17,51]` as its
first dependency. The certificate arithmetic is

\[
4331=61\cdot71,
\quad F_{3,2}(6)=1746,
\quad G_{3,2}(6)=289,
\]

\[
A_{17}=73,
\quad A_{51}=6097033=73\cdot289^2,
\quad A_{17}A_{51}=21097^2,
\]

and

\[
1692\cdot3916\equiv21097\equiv3773\pmod{4331}.
\]

Both roots are units, and

\[
\gcd(21097-3773,4331)=4331,
\qquad
\gcd(21097+3773,4331)=1.
\]

Thus the dependency is an exact global-root decoy, not a factorization.
The search covers only `D=2`, the declared small balanced semiprimes, and
indices through `4 bitlength(N)`. It provides no asymptotic frequency,
success probability, or algorithm. The adaptive V2 design, temporary-path
defect, and post-run stdout transcription are all disclosed in the frozen
provenance record. No frozen input or durable ledger was changed by this
audit.

