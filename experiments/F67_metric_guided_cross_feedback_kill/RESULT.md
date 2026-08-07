# F67 metric-guided cross-feedback kill

**Family:** F26.

**Status:** revised proof-only mandatory kill test. No research computation
was run. The first hostile audit rejected an undefined menu and occurrence
semantics; this version states both explicitly.

**Verdict:** the inverse-diagonal score does not justify the proposed
ranking. The retry is materially new only in rounds that change the integer
block presentation or an explicitly declared occurrence budget.

- For a unit residue \(r\), with canonical inverse \(w\) and
  \(\delta=|r-w|\), the direct \(r\pm1\) screen is exactly the hidden-prime
  divisibility of \(\delta\), apart from the special case \(\delta=0\).
- The proposed discriminant screen detects \(r^2=-1\) in a hidden CRT
  component. It gives a proper factor only when this holds in some, but not
  all, hidden components. Its prime support is disjoint from the nonzero
  direct-sign event.
- Every non-self-inverse direct separator has
  \(\delta\ge \min(p,q)\). Thus, on balanced semiprimes, ranking by small
  positive \(\delta\) puts an exponentially large score interval before any
  such separator.
- If the polynomial menu has already been exhaustively gcd-screened, its
  ordering cannot improve its current-round success. Conditional on a miss,
  the score can matter only through later block or occurrence-budget changes.
- Equal values of \(\delta\), with identical direct and discriminant outcomes,
  can produce different square-closure behavior. The score does not predict
  whether the appended relation has a square endpoint product.
- If the global identity is not removed before truncation, $N=77$ gives a
  conditional fixed point for $K=1$ when identity appends change no state. Its
  nontrivial menu orbit avoids both local torsion conditions at every hidden
  prime.

The adaptive operation itself is not universally killed. A hand-checkable
\(N=209\) state shows that a lowest positive-score relation can introduce new
block generators outside the old generated subgroup and make a factor visible
in the next menu. What does not survive is a
universal monotonicity, closure, or all-input hitting claim based only on
\(\delta\).

## 1. Setup

Let

\[
N=pq
\]

with distinct odd primes \(p,q\). Let \(r\in\{1,\ldots,N-1\}\) be a unit,
and let \(w\in\{1,\ldots,N-1\}\) be its canonical inverse. Put

\[
d=r-w,
\qquad
\delta=|d|,
\qquad
\Delta=\delta^2+4.
\]

The exact inverse relation is

\[
rw=1+kN
\]

for a public nonnegative integer \(k\).

Let the current pairwise-coprime integer block types be
$B_1,\ldots,B_s$. This result uses the **exact distinct-block pair menu**

\[
\mathcal O_{=2}(B)=
\left\{
\{u,u^{-1}\}:
u=\operatorname{can}(B_i^\epsilon B_j^\eta\bmod N),\
i<j,\ \epsilon,\eta\in\{-1,1\}
\right\},
\tag{M}
\]

with duplicate unordered inverse orbits removed. Here $\operatorname{can}$
is the least positive residue. Menu (M) uses exactly two distinct block
indices. It excludes support-zero and support-one terms, repeated indices,
exponents other than $\pm1$, and an independent global coefficient $-1$.
This definition is narrower than a support-at-most-two exponent box.

The proposed round enumerates (M), runs every immediate public screen, removes
the global orbits $\{1\}$ and $\{N-1\}$, retains at most
$K=\operatorname{poly}(\log N)$ lowest-score factor-free inverse pairs,
appends their exact inverse relations, gcd-refines the integer endpoints, and
repeats.

The default semantics here has no implicit occurrence budget. Re-appending an
identical indexed endpoint relation is ignored unless a separate algorithm
explicitly authorizes and charges a new occurrence. An equal relation value
with a different endpoint factorization is not automatically identical: its
new integer overlaps can still refine the block presentation. The $N=77$
fixed-point example below deliberately analyzes the faulty variant that keeps
the global identity before filtering; it also states the no-occurrence-change
condition explicitly. The parameter $K$ counts distinct inverse orbits only
after the stated deduplication and filters.

## 2. Exact meaning of the metric

### Theorem 1: the two torsion tickets

For every prime \(\ell\mid N\),

\[
\boxed{
\ell\mid d
\quad\Longleftrightarrow\quad
r^2\equiv1\pmod\ell
}
\tag{1}
\]

and

\[
\boxed{
\ell\mid d^2+4
\quad\Longleftrightarrow\quad
r^2\equiv-1\pmod\ell.
}
\tag{2}
\]

Consequently, because \(N\) is squarefree,

\[
\boxed{
\gcd(d,N)=\gcd(r^2-1,N),
\qquad
\gcd(d^2+4,N)=\gcd(r^2+1,N).
}
\tag{3}
\]

The two gcds in (3) are coprime.

#### Proof

Modulo \(\ell\), \(w\equiv r^{-1}\). Multiplication by the unit \(r\) gives

\[
r(r-w)\equiv r^2-1\pmod\ell,
\]

which proves (1). Also,

\[
d^2+4
\equiv(r-r^{-1})^2+4
\equiv(r+r^{-1})^2\pmod\ell.
\]

This vanishes exactly when \(r+r^{-1}\equiv0\), or \(r^2\equiv-1\), which
proves (2). Equal prime supports give (3) because \(N=pq\) is squarefree. A
prime common to the two gcds would divide both \(d\) and \(d^2+4\), hence
would divide \(4\), which is impossible for odd \(N\). \(\square\)

### Corollary 1: direct success and self-inversion

If \(\delta>0\), then

\[
\boxed{
r\text{ passes a proper }\gcd(r-1,N)\text{ or }\gcd(r+1,N)\text{ screen}
\quad\Longleftrightarrow\quad
\gcd(\delta,N)>1.
}
\tag{4}
\]

In this case \(\gcd(\delta,N)<N\), because \(0<\delta<N\). Thus
\(\gcd(\delta,N)\) itself returns the factor.

If \(\delta=0\), then \(r=w\), equivalently \(r^2\equiv1\pmod N\). The four
CRT possibilities are the two global roots \(1,N-1\) and the two useful
mixed-sign roots. The direct \(r\pm1\) checks distinguish them.

For \(\delta>0\), every direct separator therefore satisfies

\[
\boxed{\delta\ge\min(p,q).}
\tag{5}
\]

This is the central obstruction to a monotone interpretation. A small
positive value of \(\delta\) is not an approximate direct hit. Below the
smallest prime factor, direct success is impossible. On a balanced semiprime,
the forbidden score interval has length \(N^{1/2+o(1)}\), exponential in the
bit length.

Equation (2) gives a separate fact. The discriminant ticket detects a local
fourth root of unity: \(r^2=-1\) in one hidden component. If
\(\gcd(\delta^2+4,N)=N\), this condition holds in both components and the gcd
does not factor \(N\). If both gcds in (3) equal \(1\), then every hidden
component satisfies

\[
r^2\not\equiv1,-1.
\]

The remaining score magnitude has no further local torsion meaning.

### Corollary 2: inversion adds no second current screen

For every divisor of \(N\),

\[
r\equiv\pm1
\quad\Longleftrightarrow\quad
w\equiv\pm1
\]

with the same sign. Hence

\[
\gcd(r-1,N)=\gcd(w-1,N),
\qquad
\gcd(r+1,N)=\gcd(w+1,N).
\tag{6}
\]

Appending the canonical inverse endpoint does not create a direct hit that
was absent when \(r\) was screened. Its possible value is in the new integer
factor overlaps and the later menus that those overlaps generate.

### Lemma 2: a public singleton square certificate

If \(r\ne w\) and \(rw\) is an integer square, write \(rw=m^2\). Then

\[
m^2\equiv1\pmod N,
\qquad
2\le m\le N-2.
\]

Therefore \(m\) is a non-global self-inverse residue, and

\[
\gcd(m-1,N),\ \gcd(m+1,N)
\]

give the two factors.

#### Proof

The inverse relation gives \(m^2=1+kN\). Since \(r,w\) are distinct positive
canonical residues, \(rw>1\) and

\[
rw\le(N-1)(N-2)<(N-1)^2.
\]

Thus \(2\le m<N-1\). A square root of one in this interval is neither global
root, so it has mixed CRT signs. \(\square\)

This perfect-square test is public and cheaper than another feedback round.
It should occur before truncation. It is not implied by a small value of
\(\delta\). In particular, if \(\delta=1\), then \(r,w\) are consecutive and
coprime. If their product were a square, both would be squares, but no two
positive consecutive integers are squares. Thus the smallest positive score
can never give a singleton square certificate.

### Lemma 3: small fibres do not give menu coverage

For each signed \(d\), the congruence

\[
r^2-dr-1\equiv0\pmod N
\]

has at most four roots. Therefore the full inverse graph contains at most

\[
4+8D
\]

oriented residues with \(\delta\le D\), and at most \(4+4D\) unordered
inverse pairs.

This is the valid part of the ranking intuition: score ties have constant
size for a semiprime. It does not imply that a block menu contains either
useful \(\delta=0\) root. It also does not connect a retained factor-free pair
to future block novelty. F66's harmonic mass theorem concerns the full unit
group. It does not transfer to an arbitrary transcript-derived subset.

## 3. Ranking an exhausted menu is not a selector theorem

Let \(M_t\) be the complete polynomial menu in round \(t\).

1. If some \(r\in M_t\) passes a gcd screen, exhaustive enumeration already
   factors \(N\). Its rank is irrelevant.
2. If every \(r\in M_t\) is factor-free, ranking changes no current-round
   fact. It only chooses which exact relations can affect round \(t+1\).
3. If appending a chosen pair changes neither the gcd-free block
   presentation nor a declared occurrence budget, rebuilding produces the
   same menu. Repeating the rank is an exact no-op.
4. If an identical relation is appended as a fresh authorized occurrence,
   the block set can remain fixed while exponent budgets grow. P70 shows that
   such deliberate reuse can be material. It is a multiplicity or power
   rule, not evidence learned from the metric. The algorithm must state this
   semantics and charge every occurrence.
5. A genuinely block-adaptive round introduces a new canonical endpoint
   residual, or splits an old gcd-free block through a new overlap, and then
   constructs residues not present in \(M_t\).

This separates the retry from F65. Sorting the already exhausted F65-D02
signed distinct-block pair menu cannot alter its null result. The retry becomes new
only after a retained inverse relation changes the next block presentation or
the explicitly authorized exponent box.

## 4. Exact obstructions

### 4.1 A global-identity fixed point at \(N=77\)

Take

\[
N=77=7\cdot11
\]

and the valid inverse relation

\[
2\cdot39=78=1+N.
\]

Its gcd-free blocks are \(2,39\). The exact menu (M) has the
following two inverse orbits:

\[
2\cdot39\equiv1\pmod {77},
\]

and, since \(39^{-1}\equiv2\pmod {77}\),

\[
2\cdot39^{-1}\equiv4\pmod {77},
\qquad
4^{-1}\equiv58\pmod {77}.
\]

Their scores are

\[
\delta(1)=0,
\qquad
\delta(4)=|4-58|=54.
\]

The identity produces no proper direct gcd, and

\[
\gcd(0^2+4,77)=1.
\]

The nontrivial pair is also factor-free:

\[
\gcd(4-1,77)=\gcd(4+1,77)=1,
\]

\[
\gcd(54^2+4,77)=\gcd(2920,77)=1.
\]

Thus, for the faulty variant that retains global residues, if $K=1$ and an
identity append changes neither the block presentation nor any occurrence
budget, the ranker retains $r=w=1$. Appending $1\cdot1=1$ creates no endpoint
block and no new menu. Every later round is identical. This is an exact
conditional fixed point, not a probabilistic failure. The filtered round
defined after (M) removes this obstruction before ranking.

The example also pins the smallest product $pq$ of distinct odd primes for
which there exists a unit $r\not\equiv\pm1\pmod N$ such that both gcds in
(3) equal $1$. If $3\mid N$,
every unit is
\(\pm1\pmod3\), so the direct ticket always fires locally. If \(5\mid N\),
every unit modulo \(5\) is either \(\pm1\), or has square \(-1\), so one of
the two torsion tickets always fires locally. Every smaller product of two
distinct odd primes has a factor \(3\) or \(5\). The first product that can
have a nontrivial survivor is \(7\cdot11=77\), and \(r=4\) above is one.

This obstruction is removed by explicitly discarding \(1,N-1\), deduplicating
inverse orbits, and forbidding \(k=0\) feedback. Those rules are necessary;
they do not supply a positive ranking theorem.

### 4.2 The metric is not monotone toward a direct separator

At

\[
N=209=11\cdot19,
\]

the canonical inverse pair

\[
80\cdot81=6480=1+31\cdot209
\]

has the minimum positive score

\[
\delta=1.
\]

It survives both tickets:

\[
\gcd(80-1,209)=\gcd(80+1,209)=1,
\qquad
\gcd(1^2+4,209)=1.
\]

In contrast,

\[
10\cdot21=210=1+209
\]

has the larger score \(\delta=11\), but

\[
\gcd(10+1,209)=11.
\]

The lower score is strictly farther from present direct success. This is the
smallest clean \(\delta=1\) pair from F66, now compared with an exact direct
separator on the same modulus. It refutes any universal monotone claim based
on score order.

### 4.3 Equal scores have different square closure at \(N=143\)

Take

\[
N=143=11\cdot13.
\]

The four canonical inverse pairs

\[
\begin{array}{c|c|c}
(r,w)&rw&\delta\\ \hline
(9,16)&144=1+143&7\\
(61,68)&4148=1+29\cdot143&7\\
(75,82)&6150=1+43\cdot143&7\\
(127,134)&17018=1+119\cdot143&7
\end{array}
\]

all have the same signed-fibre equation. The two torsion tickets are also
identical for all four:

\[
\gcd(7,143)=1,
\qquad
\gcd(7^2+4,143)=\gcd(53,143)=1.
\]

The first endpoint product is the square \(12^2\), and

\[
\gcd(12-1,143)=11,
\qquad
\gcd(12+1,143)=13.
\]

The other three products lie strictly between consecutive squares:

\[
64^2<4148<65^2,
\]

\[
78^2<6150<79^2,
\]

\[
130^2<17018<131^2.
\]

Therefore \(\delta\), the direct screens, and the discriminant screen do not
determine even the singleton square-closure behavior of the appended
relation. The integer-square test does determine it, so an implementation
should run that public test directly. Calling the success a consequence of
the diagonal rank would be false.

## 5. A hand-checkable genuinely adaptive round survives

The preceding obstructions do not make every feedback relation useless. At

\[
N=209,
\]

start from the two exact relations

\[
31\cdot27=837=1+4\cdot209,
\]

\[
3\cdot70=210=1+209.
\]

Their gcd-free blocks are

\[
\{3,31,70\}.
\]

Since \(3^{-1}\equiv70\pmod {209}\), menu (M) contains

\[
r\equiv31\cdot3^{-1}
\equiv31\cdot70
\equiv80\pmod {209}.
\]

Its canonical inverse is \(81\), and \(\delta=1\). Apart from the global
identity, the inverse orbits in menu (M) are

\[
\{80,81\},
\qquad
\{9,93\}.
\]

Neither orbit passes the direct or discriminant screen. The first is the
unique lowest positive-score orbit.

Appending

\[
80\cdot81=1+31\cdot209
\]

is genuinely adaptive in this history. The endpoint identities

\[
80=2^4\cdot5,
\qquad
81=3^4,
\qquad
70=2\cdot5\cdot7,
\qquad
27=3^3
\]

refine the blocks to

\[
\{2,3,5,7,31\}.
\]

The next menu (M) contains \(2\cdot5=10\), and

\[
\gcd(10+1,209)=11.
\]

This proves that the new operation can work and that it is not merely a
renaming of the first menu. It proves no all-input law. The success depends
on the canonical endpoint factor overlaps, a property not encoded by
\(\delta\) alone.

There is a stronger exact distinction. Before feedback,

\[
70\equiv3^{-1},
\qquad
31\equiv3^{-3}\pmod {209},
\]

so the subgroup generated by all old block residues is $H_0=\langle3\rangle$.
Modulo $11$, this subgroup has order $5$ and does not contain
$-1\equiv10$. Hence $10\notin H_0$: no ordinary monomial in the old blocks,
with arbitrary integer exponents but no free global minus sign, can produce
the successful residue.

The feedback endpoints $80$ and $81$ themselves still lie in $H_0$. The
algorithmic change occurs only after integer gcd refinement splits composite
blocks and exposes $2$ and $5$ separately. The enlarged block-generated
subgroup contains $2\cdot5=10$ and is strictly larger than $H_0$. Thus a
canonical inverse endpoint need not enlarge the old modular subgroup, while
its **integer factor overlaps can create new block generators that do**. This
is the concrete representation-level gain of feedback.

The same residue also shows why novelty is history-dependent. If the relation
\(80\cdot81\) is already present, appending it again creates no new endpoint
information. If duplicate occurrences are ignored, it is redundant. If they
are counted, it is a deliberate multiplicity update. The numerical score is
the same in all three interpretations.

## 6. Sharply specified surviving claim

The following is the narrow claim that remains open:

> After removing global residues and running every public immediate screen,
> retain distinct factor-free inverse orbits from a precisely defined
> polynomial exact distinct-block pair menu (M). Charge duplicate occurrences
> explicitly. Rebuild the menu only after a strict gcd-free block refinement
> or an explicit occurrence-budget increase. Prove that, for every specified
> odd squarefree semiprime input and source transcript, polynomially many
> retained orbits and rounds expose a proper gcd with inverse-polynomial
> probability.

The immediate screens must include \(\gcd(\delta,N)\),
\(\gcd(\delta^2+4,N)\), the \(\delta=0\) mixed-root check, and the integer
square test on \(rw\). The algorithm must also state how it treats the global
outcomes \(1,N-1\) and \(\gcd(\delta^2+4,N)=N\). These tests and classifications
precede ranking.

No result here proves or refutes that claim for every possible selector. The
inverse-diagonal score supplies no monotonicity lemma toward it. A valid retry
must add a theorem about endpoint-block novelty or the distribution of the
next menu. It cannot inherit F66's full-group target-mass bound, and it cannot
count a reordered F65 menu as new evidence.

**Classification:** kill the metric-based universal ranking justification.
Keep genuinely adaptive canonical-endpoint feedback as an open, narrower
route.
