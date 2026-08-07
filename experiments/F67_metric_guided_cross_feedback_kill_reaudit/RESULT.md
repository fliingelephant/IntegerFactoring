# F67 fresh hostile re-audit — metric-guided cross-feedback

**Candidate audited:**
experiments/F67_metric_guided_cross_feedback_kill/RESULT.md

**Verified candidate SHA-256:**
e6413ba7703a5daa371a104a15a10c326fb881c2538f6dbd7b1cf3fec304de79

**Verdict: PASS.**

This re-audit was reconstructed from the corrected candidate and the stated
mathematics. The first hostile audit was not used as evidence. No research
computation was run. All finite checks below use hand arithmetic.

The exact menu, filtering order, and occurrence semantics are coherent. The
\(N=77\) example is correctly conditional on a faulty global-retaining
variant. The \(N=143\) equal-score example is exact. The full old and new
\(N=209\) menus reconstruct as claimed. The strengthened subgroup statement
also survives arbitrary integer block exponents because all old blocks are
powers of \(3\) modulo \(209\), while \(10\) is not.

## 1. Exact menu and semantics — PASS

The menu is

\[
\mathcal O_{=2}(B)=
\left\{
\{u,u^{-1}\}:
u=\operatorname{can}(B_i^\epsilon B_j^\eta\bmod N),\quad
i<j,\quad \epsilon,\eta\in\{-1,1\}
\right\}.
\]

It has four signed products for each unordered pair of distinct block
indices. It has at most \(4\binom{s}{2}\) entries before inverse-orbit
deduplication. It excludes:

- the empty product;
- support-one products;
- a repeated block index;
- exponents outside \(\{-1,1\}\); and
- a free global coefficient \(-1\).

These exclusions are used later. In particular, the subgroup claim at
\(N=209\) would have a different answer if a free \(-1\) were present.

The round order is also coherent:

1. enumerate the signed products and deduplicate unordered inverse orbits
   into the complete menu;
2. run the immediate screens;
3. remove any global singleton orbits;
4. rank the remaining factor-free orbits; and
5. append selected exact endpoint relations.

Under the default semantics, an identical indexed endpoint relation adds no
new occurrence. A different endpoint presentation of an equal value can
still matter because its integer gcd overlaps can split an old block. These
are distinct cases, and the candidate keeps them distinct.

## 2. Torsion identities and direct-screen boundary — PASS

Let \(w\equiv r^{-1}\pmod\ell\), where \(\ell\mid N\) is prime, and put
\(d=r-w\). Then

\[
r d\equiv r^2-1\pmod\ell.
\]

Since \(r\) is a unit,

\[
\ell\mid d
\quad\Longleftrightarrow\quad
r^2\equiv1\pmod\ell.
\]

Also,

\[
d^2+4
\equiv(r-r^{-1})^2+4
\equiv(r+r^{-1})^2\pmod\ell.
\]

This vanishes exactly when \(r^2\equiv-1\pmod\ell\). Because
\(N=pq\) is squarefree, equality of local prime supports gives both gcd
equalities in equation (3). The supports are disjoint: an odd prime cannot
divide both \(d\) and \(d^2+4\).

For \(0<\delta=|d|<N\), a direct \(r\pm1\) separator exists exactly when
\(\gcd(\delta,N)>1\). This gcd is automatically proper. If every hidden
component satisfied \(r^2=1\), then \(r\) would be self-inverse and
\(\delta=0\). Hence a non-self-inverse direct separator has

\[
\delta\ge\min(p,q).
\]

The \(\delta=0\) exception is necessary. Both global roots and both useful
mixed roots have \(d=0\), while their direct screens have different
outcomes.

The discriminant gcd can also equal \(N\). This happens when
\(r^2=-1\) at both hidden primes and gives no factor. The corrected
candidate states this boundary.

Inversion preserves each local sign:

\[
r\equiv\pm1\pmod\ell
\quad\Longleftrightarrow\quad
r^{-1}\equiv\pm1\pmod\ell.
\]

Thus the two endpoint direct gcds are equal, as claimed.

## 3. Square certificate and fibre count — PASS

If \(r\ne w\), then

\[
rw\le(N-1)(N-2)<(N-1)^2.
\]

If \(rw=m^2\), the relation gives \(m^2\equiv1\pmod N\), while the strict
bound gives \(2\le m\le N-2\). Thus \(m\) is neither global root. For a
product of two distinct odd primes, it has mixed CRT signs and both
\(\gcd(m-1,N)\) and \(\gcd(m+1,N)\) are proper.

If \(\delta=1\), the endpoints are consecutive and coprime. A square
product would make both endpoints squares. The only consecutive
nonnegative squares with difference one are \(0,1\), which are outside the
distinct positive endpoint case. The candidate's exclusion is correct.

For each signed difference \(d\), the quadratic

\[
r^2-dr-1=0\pmod N
\]

has at most two roots modulo each prime and at most four modulo \(N\).
Therefore:

- \(d=0\) contributes at most four oriented states and four singleton
  inverse orbits;
- each positive absolute difference contributes at most eight oriented
  states; and
- inversion pairs those states into at most four unordered orbits.

This proves the bounds \(4+8D\) and \(4+4D\). They are upper bounds only and
do not imply that a transcript menu contains a useful root.

## 4. The \(N=77\) menu and conditional fixed point — PASS

Take

\[
N=77,\qquad 2\cdot39=78.
\]

The old blocks are \(2,39\), with

\[
2^{-1}=39,\qquad39^{-1}=2\pmod{77}.
\]

For the only distinct block pair, the four sign choices give

\[
\begin{array}{c|c}
(\epsilon,\eta)&2^\epsilon39^\eta\pmod{77}\\ \hline
(1,1)&1\\
(1,-1)&4\\
(-1,1)&58\\
(-1,-1)&1.
\end{array}
\]

Since \(4\cdot58=232=3\cdot77+1\), the exact deduplicated menu consists of

\[
\{1\},\qquad\{4,58\}.
\]

Their scores are \(0\) and \(54\). The screens are exact:

\[
\gcd(4-1,77)=\gcd(4+1,77)=1,
\]

and

\[
54^2+4=2920,\qquad\gcd(2920,77)=1.
\]

The identity has no proper direct gcd and
\(\gcd(4,77)=1\) for its discriminant.

The fixed-point claim is explicitly conditional. If a faulty variant keeps
the identity, takes \(K=1\), and gives an identity append no block or
occurrence effect, it selects \(\{1\}\) forever. The corrected round removes
this orbit before ranking and does not claim to suffer this fixed point.

The minimality claim is also correct. If \(3\mid N\), every local unit has
square \(1\) modulo \(3\). If \(5\mid N\), every local unit has square
\(1\) or \(-1\) modulo \(5\). Thus no unit can make both torsion gcds equal
to one on a semiprime with factor \(3\) or \(5\). Every product of two
distinct odd primes below \(7\cdot11=77\) has one of those factors. At
\(N=77\), \(r=4\) has

\[
4^2\equiv2\pmod7,\qquad4^2\equiv5\pmod{11},
\]

which is neither \(1\) nor \(-1\) in either field. Hence \(77\) is the
smallest product in the stated scope.

Strictly, removing the identity alone is enough to remove this particular
fixed point. Deduplication and the explicit \(k=0\) rule are additional
bookkeeping safeguards. This wording point does not affect the conditional
theorem or the corrected algorithm.

## 5. The \(N=143\) equal-score example — PASS

Every displayed product is exact:

\[
9\cdot16=144=1+143,
\]

\[
61\cdot68=4148=1+29\cdot143,
\]

\[
75\cdot82=6150=1+43\cdot143,
\]

\[
127\cdot134=17018=1+119\cdot143.
\]

All four displayed orientations have signed difference \(-7\), so they
satisfy the same equation

\[
r^2+7r-1=0\pmod{143}.
\]

The common screens fail:

\[
\gcd(7,143)=1,\qquad
\gcd(7^2+4,143)=\gcd(53,143)=1.
\]

The first product is \(12^2\), and

\[
\gcd(12-1,143)=11,\qquad
\gcd(12+1,143)=13.
\]

The nonsquare certificates are exact:

\[
64^2=4096<4148<4225=65^2,
\]

\[
78^2=6084<6150<6241=79^2,
\]

\[
130^2=16900<17018<17161=131^2.
\]

Thus equal inverse distance and equal torsion screens do not determine the
singleton square certificate. The public integer-square test, not the
metric, detects the first pair.

## 6. The \(N=209\) score comparison — PASS

The two inverse relations are exact:

\[
80\cdot81=6480=1+31\cdot209,
\]

\[
10\cdot21=210=1+209.
\]

The first has score one and survives:

\[
\gcd(79,209)=\gcd(81,209)=1,\qquad
\gcd(5,209)=1.
\]

The second has score eleven but exposes

\[
\gcd(10+1,209)=11.
\]

Thus positive score order is not monotone toward a direct separator.

## 7. Exact old \(N=209\) menu — PASS

Start from

\[
31\cdot27=837=1+4\cdot209,
\qquad
3\cdot70=210=1+209.
\]

Gcd refinement gives the old block types

\[
\{3,31,70\}.
\]

The needed inverses are

\[
3^{-1}=70,\qquad31^{-1}=27,\qquad70^{-1}=3\pmod{209}.
\]

For sign order \((++,+-,-+,--)\), all three distinct block pairs give:

\[
\begin{array}{c|c}
\text{block pair}&\text{four residues}\\ \hline
(3,31)&93,\ 81,\ 80,\ 9\\
(3,70)&1,\ 9,\ 93,\ 1\\
(31,70)&80,\ 93,\ 9,\ 81.
\end{array}
\]

The inverse identities

\[
80\cdot81=6480\equiv1\pmod{209},
\qquad
9\cdot93=837\equiv1\pmod{209}
\]

show that the exact deduplicated menu is

\[
\{1\},\qquad\{80,81\},\qquad\{9,93\}.
\]

After the global filter, the scores are

\[
1,\qquad84.
\]

Both non-global pairs pass every immediate screen. For \(\{9,93\}\),

\[
\gcd(8,209)=\gcd(10,209)=1,
\]

and

\[
84^2+4=7060,\qquad\gcd(7060,209)=1.
\]

Neither endpoint product is a square:

\[
80^2<6480<81^2,
\qquad
28^2<837<29^2.
\]

Thus \(\{80,81\}\) is the unique lowest positive-score orbit after all
stated filters.

## 8. Subgroup and refinement distinction — PASS

Before feedback,

\[
70\equiv3^{-1}\pmod{209}
\]

and

\[
31\equiv27^{-1}\equiv3^{-3}\pmod{209}.
\]

Therefore every old-block monomial with arbitrary integer exponents lies in

\[
H_0=\langle3\rangle,
\]

and conversely block \(3\) generates all of \(H_0\). This proves equality,
not merely containment.

Modulo \(11\), successive powers give

\[
3,\ 9,\ 5,\ 4,\ 1.
\]

Thus the reduction of \(H_0\) has order \(5\). It cannot contain
\(-1\equiv10\), which has order \(2\). Since the integer residue \(10\)
reduces to \(-1\) modulo \(11\),

\[
10\notin H_0.
\]

This proves the claim for arbitrary positive and negative block exponents.
The absence of a free global \(-1\) is essential. Indeed, a direct hand
check gives

\[
3^{20}\equiv199\equiv-10\pmod{209},
\]

so adjoining a free \(-1\) would produce \(10\). Menu (M) explicitly does
not adjoin it.

The selected feedback endpoints remain old-subgroup elements:

\[
81=3^4,\qquad80\equiv3^{-4}\pmod{209}.
\]

The integer endpoint overlaps nevertheless change the block presentation:

\[
80=2^4\cdot5,\qquad
81=3^4,\qquad
70=2\cdot5\cdot7,\qquad
27=3^3.
\]

Concretely,

\[
\gcd(70,80)=10,\qquad
70/10=7,\qquad80/10=8,
\]

and

\[
\gcd(10,8)=2.
\]

Complete gcd refinement therefore yields

\[
\{2,3,5,7,31\}.
\]

The new exact distinct-block pair menu contains

\[
2\cdot5=10.
\]

Since \(10\notin H_0\), the subgroup generated by the refined blocks is
strictly larger. Its direct screen returns

\[
\gcd(10+1,209)=11.
\]

This verifies the strengthened distinction: the feedback endpoints do not
enlarge the old modular subgroup, but their integer overlaps expose block
generators that do.

## 9. Final scope — PASS

The examples prove no all-input success law. They establish only:

- the inverse-distance score has no direct-factor monotonicity;
- current-round ranking cannot improve an already exhausted menu;
- equal scores do not determine singleton square closure;
- a global-retaining, no-occurrence-change variant can have an exact fixed
  point; and
- a genuinely refined endpoint presentation can expand the block-generated
  subgroup even when both new endpoints lie in the old subgroup.

The candidate does not transfer F66's full-group mass bound to the
transcript menu. It does not claim that square-class closure is sufficient
for a non-global root. It also keeps explicit occurrence amplification
separate from information gained by gcd refinement.

No counterexample to the corrected mathematical claims was found.
**Final verdict: PASS.**
