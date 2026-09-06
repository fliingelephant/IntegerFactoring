# F224 hostile audit

## Verdict

**PASS.**

The AP-Fermat bound, the pullback of the promoted P193 root bounds, the
maximum-atom law, and the hybrid two-thirds phase theorem are correct in the
stated model. The raw-coefficient and resultant/local-nullity bounds are
combined by a valid union bound. They are not treated as disjoint events.

This verdict uses the standard meaning of a Fermat scan cap: it is a positive
integer. The proof writes the main argument for caps at least two. The missing
cap-one case is proved in Section 5 below. A zero-test "cap" would make Theorem
C false and is not covered by this verdict.

## 1. Authentication

I read each manifest before reading its hashed inputs.

The D01 hashes match `FROZEN_MANIFEST.md` exactly:

- `PREREGISTRATION.md`:
  `0913845ed617edc0ac0ade7ad9ecede101ecaf92ad5367fe94fbe59cd41545f9`;
- `scan.c`:
  `c41f93502da4ea19e42633bb4aca3d95d7c65055cfeb09f70866f573241e753f`;
- `remote_run.sh`:
  `4b7cd053ea307ccfaf8ecb48aa65e44eaef4e85a4bba725685109ed3e90bd3bd`.

The D02 hashes match `D02_FROZEN_MANIFEST.md` exactly:

- `D02_PREREGISTRATION.md`:
  `b1a879372284de3259d65a48c7a8650a75622d4159ffd7f6af31de1f5af7502f`;
- `D02_remote_run.sh`:
  `f796dbf191e84358b5a0b69598b5b1e2183f0b156d8bcfa7c765c146bdfa40fe`;
- unchanged `scan.c`:
  `c41f93502da4ea19e42633bb4aca3d95d7c65055cfeb09f70866f573241e753f`.

The preserved run artifacts also match their recorded hashes:

- D01 failed log:
  `68426631c913c2661499e6d67cdc8fbea908179f089d17855ad1c0340bbb72c6`;
- D01 zero-byte output:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
- D02 output:
  `453ba8bbac8e92f38b78651e06c7f22d07f68356e4b3625f473730e01cd15d42`;
- D02 log:
  `de3ac3dc27d167caf790fef37b109c3af0d3e83d840e1fb2efdbb1fc7c686218`.

F224 imports P193. I authenticated the promoted F222 V2 packet against
`V2_MANIFEST.md`. Its statement, proof, self-audit, result, and provenance
hashes all match. In particular, the authoritative statement and proof hashes
are

```text
586d2edd549a8c580aa9d66c9dd2cee7866ee4f0d74ed0956bc3f07772ad6cd9
e098bb138dd033537436cdc64ed8a46e67b80ba4ae1e0c489c48a8d0c71ff4c1
```

The F224 manifests freeze the experimental inputs. They do not state hashes
for `STATEMENT.md`, `PROOF.md`, or `SELF_AUDIT.md`. This audit does not claim
manifest authentication for those three files.

## 2. AP-Fermat test-count bound

From `p congruent s (mod L)` and `gcd(L,N)=1`, the residue `s` is a unit
modulo `L`. Thus

\[
q\equiv Ns^{-1}=:u\pmod L.
\]

The true center `A_*=(p+q)/2` satisfies

\[
2A_*\equiv s+u\pmod L.
\]

With `g=gcd(2,L)` and `m=L/g`, a consistent linear congruence of this form is
one class modulo `m`. This includes odd `L`, even `L`, and `L=1`. The loss from
`L` to `m` is at most a factor of two.

Let `A_0` be the first member of the class at or above `sqrt(N)`. Since `A_*`
is in the same class, the number `K` of tested centers through `A_*` obeys

\[
K=1+{A_*-A_0\over m}
 \le 1+{A_*-\sqrt N\over m}.
\]

The exact displacement is

\[
A_*-\sqrt N
={d^2\over2(\sqrt p+\sqrt q)^2}
<{d^2\over8p}.
\]

Since `m>=L/2`,

\[
K<1+{d^2\over4pL}.
\]

At `A_*`, the square is `(d/2)^2` and returns `p,q`. Any earlier square would
give a positive factorization of `pq`. The only nontrivial factorization is
the same pair, while the trivial `(1,N)` representation has a larger center.
Thus an earlier square cannot invalidate the terminal.

The claimed numerical-QP terminal follows when the displayed test count and
the public CRT operands have numerical-QP encoding and arithmetic cost. In
the stated active application, the prior certificate supplies this encoding
scope.

## 3. Balanced cell and generalized AP pullback

The balance inequalities give

\[
\sqrt{N/2}<p<\sqrt N<q.
\]

The real interval length is

\[
\sqrt N-\sqrt{N/2}< (\sqrt2-1)p<p.
\]

Rounding the endpoints cannot increase its integer diameter past `p`.
Therefore reduction of `I_N` is injective modulo `p`. It is also injective
modulo `q`.

The interval is below `q` and below `2p`. Its only nonunit modulo `N` is
`x=p`. Hence the preliminary integer gcd separates the exact candidate, and
every off-target integer is a unit to which P193 applies.

Restricting an injective pullback to

\[
\mathcal C_{L,s}=\{x\in I_N:x\equiv s\pmod L\}
\]

cannot increase the size of a bad local residue set. No CRT independence or
uniformity modulo the hidden primes is used in this step. This is important:
an AP-conditioned integer shift is generally not a uniform CRT shift.

## 4. P193 degree bounds, root counts, and maximum atoms

Under `r<d<p-1`, the authenticated P193 proof gives these already-unioned
sets of unit shifts:

| channel | local field | maximum number of shifts |
|---|---:|---:|
| some raw cyclic coefficient is zero | `F_p` | `rd` |
| some raw cyclic coefficient is zero | `F_q` | `rd(r+1)` |
| positive local nullity | `F_p` | `rd` |
| positive local nullity | `F_q` | `2rd` |

The first two rows already include the scan over all `r` raw coefficients.
The last two rows already include the union over all roots of `X^r-1`.

On the `q` coefficient side, the cleared numerator has degree at most
`d(r+1)-1` in each cyclic position. The at most `r` roots of
`D(a)=1-(-a)^r` are one common exceptional set. They are counted once, not
once per coefficient:

\[
r+r\bigl(d(r+1)-1\bigr)=rd(r+1).
\]

On the two nullity sides, the root polynomials have degrees at most `d` and
`2d-1`, respectively. The P193 nonvanishing arguments remain valid under
exactly `r<d<p-1` and `gcd(r,N)=1`.

After injective pullback, a union bound gives at most

\[
rd+rd(r+1)+rd+2rd=rd(r+5)
\]

off-target cell integers. This sum is valid even when the four sets overlap.
A proper raw-coefficient gcd is only a subset of the corresponding local-zero
union. A proper resultant gcd is only a subset of the local-nullity union.
Local zeros in both hidden fields, repeated roots across channels, and common
raw/resultant events can only make the useful set smaller.

If a law on the cell has maximum atom `eta`, any set of `B` points has mass
at most `B eta`. Adding the single exact point gives

\[
\Pr(\text{useful trial})
\le(1+rd(r+5))\eta.
\]

For the uniform law, `eta=1/H`. If the law and `r` are measurable with
respect to the prior transcript and the next shift is fresh, the same bound
holds conditionally. A conditional union bound needs no independence between
different stages.

## 5. Hybrid theorem and every boundary inequality

Fix a constant `epsilon>0`. Let `Q_F(n)` be a fixed positive integer-valued
numerical-QP cap. Let `T(n)` be a fixed numerical-QP trial bound. Let all
admissible `r_i>=2` be bounded by one fixed numerical-QP envelope `R(n)` and
be chosen before their respective fresh uniform cell shifts.

First take `Q_F>=2`. If the AP-Fermat scan fails within its cap, its true test
count `K` satisfies

\[
Q_F<K<1+{d^2\over4pL}.
\]

Therefore

\[
L<{d^2\over4p(Q_F-1)}
=O\!\left({d^2\over pQ_F}\right).
\]

The same strict inequality gives

\[
d^2>4pL(Q_F-1)\ge4p.
\]

Thus `d>2 sqrt(p)`. Every numerical-QP `r_i` is eventually below `d`, and it
is also below `p` and `q`. Since `p,q` are prime, this also makes
`gcd(r_i,N)=1` automatically.

The cap-one edge case omitted from the written proof has the same conclusion.
If one tested center does not reach `A_*`, then `A_*-A_0>=m`. Hence

\[
{d^2\over8p}>A_*-\sqrt N\ge m\ge {L\over2},
\]

so `L<d^2/(4p)` and `d>2 sqrt(p)`. Thus the rest of the argument also covers
`Q_F=1`.

On the failed branch and under `d<=p^(2/3-epsilon)`,

\[
L=O\!\left(p^{1/3-2\epsilon}\right)=o(p).
\]

The balanced interval has length `Theta(p)`. A residue class modulo
`L=o(p)` therefore has

\[
H={\Theta(p)\over L}+O(1)=\Theta(p/L).
\]

Using the maximum-atom law and `r_i<=R`, including the exact-candidate term,
the complete bank has probability

\[
O\!\left(T R^2{dL\over p}\right)
=O\!\left({TR^2\over Q_F}{d^3\over p^2}\right).
\]

At the closed boundary `d=p^(2/3-epsilon)`,

\[
{d^3\over p^2}\le p^{-3\epsilon}.
\]

Numerical-QP values are `2^((log n)^O(1))=2^o(n)`, while balance gives
`p=2^(n/2+O(1))`. For fixed positive `epsilon`,

\[
2^{o(n)}p^{-3\epsilon}=2^{-\Omega(n)}.
\]

This proves the dichotomy for every sufficiently large member of every
family in the stated gap range. If `epsilon>=2/3`, there are no sufficiently
large positive even gaps satisfying the premise, so that part is vacuous.

For an adaptive random sequence of moduli, the rigorous bank bound is the
expectation of the sum of the conditional bounds, or the deterministic
`T,R` envelope displayed above. The theorem does not cover a modulus chosen
after observing its own shift, a nonuniform cell law, or an unbounded random
trial count without a fixed numerical-QP envelope.

For `d=Theta(p^(3/5))`, `epsilon=1/15` gives

\[
{d^3\over p^2}=\Theta(p^{-1/5}),
\]

as claimed.

## 6. Small and edge cases

I ran a small exact Sage enumeration after redirecting only Sage's cache to a
permitted temporary directory. It checked:

- 24,279 AP-Fermat cases with odd primes `3<=p<80`, `p<q<2p`, and every
  coprime `1<=L<=3p`;
- 163 balanced integer cells, including `p=3,q=5` and one-point cells;
- 876 admissible `(p,q,r)` cases for all tested `2<=r<min(d,8)`;
- all four P193 cardinality bounds by exact finite-field coefficient and
  polynomial-gcd computation; and
- the `N=187` local evaluations.

There were no violations. The enumeration is a consistency check, not part of
the proof.

For `N=187`, the stated evaluations are correct:

\[
(1,6)\pmod {11},\qquad(5,3)\pmod {17}.
\]

Since two is invertible in both fields, they give cyclic coefficient pairs
`(9,3) mod 11` and `(4,1) mod 17`. All coefficients and all root evaluations
are nonzero. Thus the only useful point in the cell is the separately screened
exact candidate `11`.

## 7. D01 preservation and D02 evidence scope

D01 is preserved as a failed workflow. Its log contains only

```text
remote_run.sh: line 11: /usr/bin/time: No such file or directory
```

The output is zero bytes. The source was compiled, but the mathematical binary
did not run and no mathematical row was produced. No alternate D01 runner was
used.

D02 preserves the cohort, source, compiler options, 2-GiB virtual-memory
limit, priority, and 600-second timeout. Its evidence-relevant change is the
approved replacement of `/usr/bin/time -v` by Bash `time -p`. The runner also
uses D02-specific default filenames and a D02-specific temporary binary path;
the exact preregistered command supplies the output names, and neither change
alters the mathematical computation. D02 correctly makes no peak-RSS claim.

An independent aggregation of `D02_OUTPUT.tsv` reproduces every stated
summary:

- 480 rows;
- 11,767,411 off-target integers;
- 197 exclusive roots in 115 rows;
- maximum five exclusive roots in one row;
- maximum row fraction `1/77`;
- zero rows with a `both` event;
- exactly one exact candidate in every row;
- zero row-total failures;
- 104 capacity-scale rows, with 15 roots among 933,751 off-target integers in
  13 positive rows; and
- bit-scale fractions
  `9.9320969e-4`, `2.4397914e-4`, `5.6534747e-5`, `1.2306490e-5`, and
  `3.9945640e-6`.

This experiment tests only the scalar `X=1` specialization and supplies
finite obstruction guidance. It does not establish the full coefficient or
resultant theorem, the AP pullback, or the asymptotic phase law. None of its
numerical claims is used in the proof.

## 8. Exact scope of the PASS

The PASS covers uniform draws from the full AP cell, or a prior-transcript
fixed law through the stated maximum-atom bound. It does not cover a useful
proved heavy atom, choosing `r` after seeing the same shift, joint processing
of typical nonzero coefficient vectors, or gaps at
`p^(2/3-o(1))` and above. It also does not turn the obstruction into an
all-input factoring lower bound.
