# F229 blind reconstruction

## Protocol and verdict

Before reading the statement, I computed its SHA-256 as

```text
715d27021f59e53f2d1198ae7440985d8cf7749123aa2f94463d9d870ce49dfb
```

which is the required hash. I then read only the repository-root
`PROMPT.md` and this candidate's `STATEMENT.md`. I did not use another F229
artifact, a durable ledger, or a computation beyond hashing.

**Verdict: PASS WITH QUALIFICATIONS.** The mathematical obstruction and all
boxed bounds reconstruct. Two literal readings need correction:

1. Formula (C.2) is a uniform **upper bound**. It cannot be a two-sided
   asymptotic equality, since the probability is exactly zero when
   (H^d<p), and it can also be smaller for other intervals.
2. The sentence after (E.1), "Before (C_X\ge p), no hidden component can
   divide it," is valid for (X>1). It is false for (X=1), because then
   (C_X=0), which every hidden component divides. This is harmless only
   because Theorem A separately classifies (X=1) as an order-one global
   return with no nontrivial certified block.

There is also a standalone-definition qualification. The statement does not
define the mechanics of the named P197 tests. The lcm conclusion reconstructs
from the stated contract that a "certified common primary block" is proved to
divide both local orders. No claim about an unspecified test implementation is
needed or checked here.

## 1. Fixed-gap family and size

A bounded-prime-gap theorem supplies infinitely many prime pairs whose
positive gaps lie in a fixed finite set. Apart from the one pair involving
2, such gaps are even. Pigeonhole therefore supplies one fixed even
(d\ge2) and infinitely many odd-prime pairs

\[
q=p+d.
\]

For (p>d),

\[
p<q=p+d<2p.
\]

Furthermore,

\[
\log_2 N=\log_2p+\log_2(p+d)
=2\log_2p+\log_2(1+d/p),
\]

and taking the prescribed ceiling changes this by at most a constant. Thus

\[
n=2\log_2p+O(1),
\qquad
p=2^{n/2+O(1)}.
\]

If (Q(n)\le 2^{C(\log_2(n+1))^k}), then

\[
\log_2 Q(n)=O((\log n)^k)=o(n).
\]

This elementary comparison is what makes every fixed numerical-QP height
smaller than (p^{1/d}) eventually and makes a numerical-QP union bound
negligible against (2^{-cn}).

## 2. Reconstruction of Theorem A

Put (A=N-1=pq-1). Exponents of units modulo (p) reduce modulo (p-1).
Since (p\equiv1\pmod{p-1}) and (q=p+d\equiv1+d\pmod{p-1}),

\[
A=pq-1\equiv d\pmod{p-1}.
\]

At (q), the sign is different. Since (q\equiv1\pmod{q-1}) and
(p=q-d\equiv1-d\pmod{q-1}),

\[
A\equiv-d\pmod{q-1}.
\]

Consequently, for a unit (X\bmod N),

\[
\begin{aligned}
p\mid X^A-1
&\iff X^d\equiv1\pmod p,\\
q\mid X^A-1
&\iff X^{-d}\equiv1\pmod q
 \iff X^d\equiv1\pmod q.
\end{aligned}
\]

The second line uses invertibility; it does **not** assert the generally
false congruence (X^A\equiv X^d\pmod q). Since (N=pq) is squarefree, the
same subset of \(\{p,q\}\) divides both integers (X^A-1) and (X^d-1).
This proves (A.1):

\[
\gcd(X^{N-1}-1,N)=\gcd(X^d-1,N).
\]

Let (o_p=\operatorname{ord}_p(X)) and
(o_q=\operatorname{ord}_q(X)). A global return says that both local
congruences above hold, so

\[
o_p\mid d,
\qquad
o_q\mid d.
\]

A common primary block correctly certified by order stripping divides both
local orders. It therefore divides (d). If blocks (b_i) are certified
from any finite or infinite history, every finite accumulated value satisfies

\[
\operatorname{lcm}(b_1,\ldots,b_t)\mid d.
\]

Thus the accumulator has the absolute ceiling (d); arbitrarily many global
returns cannot make it drift past that ceiling. The same statement covers a
block composed of several primary parts because each part divides the
corresponding primary part of (d).

The gcd screen gives an exhaustive treatment of nonunits. Since (N=pq),

- (1<\gcd(X,N)<N) is exactly (p) or (q), hence is already a factor;
- \(\gcd(X,N)=N\) is equivalent to (N\mid X), and is only a full-gcd
  screen result, not a unit annihilator test;
- otherwise (X) is a unit and (A.1) applies.

In particular, (X=1) is a unit and gives a global return, but
(o_p=o_q=1). It certifies no nontrivial order block. This identity case
must not be treated as evidence that a positive multiple of (N) occurs in
(X^d-1).

## 3. Reconstruction of Theorem B

Let (H(n)) be bounded by a fixed numerical-QP function. Since (d) is
fixed,

\[
\log_2 H(n)^d
\le dC(\log_2(n+1))^k
=o(n),
\]

whereas \(\log_2p=n/2+O(1)\). Hence eventually

\[
H(n)^d<p,
\]

which proves (B.1).

For (2\le X\le H(n)), this implies (X<p<q), so (X) is a unit. It also
gives

\[
0<X^d-1<p.
\]

Neither (p) nor (q) divides this positive integer. Formula (A.1) now
gives

\[
\gcd(X,N)=1,
\qquad
G_A(X)=1,
\]

which is (B.2).

This conclusion is pointwise, so adaptivity cannot change it. At every
history, each supported value in \(\{0,1,\ldots,H(n)\}\) has one of the
following outcomes:

- (X=0): the initial gcd is (N), which is trivial;
- (X=1): the return is global of exact local order one, with no nontrivial
  block;
- (2\le X\le H(n)): the initial gcd and return are both trivial in the
  sense of (B.2).

Thus the useful-event probability is exactly zero, irrespective of the
history-dependent probabilities placed on those values. The general mention
of a proper initial gcd is logically correct, but on this eventual family
that branch is absent because every positive supported value is less than
(p).

For the word in (B.3), unique real logarithms give

\[
\log_2X=\sum_{j=1}^k\log_2b_j.
\]

Condition (B.4) is precisely (X^d<p). Since a nonempty word with
(b_j\ge2) has (X\ge2), the preceding argument gives (G_A(X)=1). The
contrapositive says that evading this literal integer-height obstruction
requires

\[
\sum_j\log_2b_j
\ge \frac{\log_2p}{d}
=\frac{n}{2d}+O(1),
\]

which is (B.5). It is only necessary: crossing the threshold does not force
either hidden prime to divide (X^d-1).

## 4. Reconstruction of Theorem C

The small-height branch is already proved: if (H^d<p), every
(X\in\{2,\ldots,H\}) has useful probability zero.

Now suppose (H^d\ge p). For (r\in\{p,q\}), define the overcounting event

\[
E_r(X):\quad r\mid X
\quad\text{or}\quad
X^d\equiv1\pmod r.
\]

Every useful outcome lies in (E_p\cup E_q): a proper initial gcd supplies
the divisibility alternative; a proper unit return supplies exactly one
local root alternative; and a global return, including one on which a block
is certified, supplies both local root alternatives. Multiples of (N) and
order-one global returns can be included in this union because an upper bound
may overcount them.

The polynomial (T^d-1\) has at most (d) roots in either prime field. One
residue class modulo (r) occurs at most (H/r+1) times in
\(\{2,\ldots,H\}\), while the number of multiples of (r) is at most
(H/r). Therefore

\[
\#E_r\le \frac Hr+d\left(\frac Hr+1\right).
\]

There are (H-1) sample points. Since (q>p), the union bound gives

\[
\begin{aligned}
\Pr(\mathrm{useful})
&\le
\frac{H/p+H/q+d(H/p+1)+d(H/q+1)}{H-1}\\
&\le
\frac{2(1+d)H/p+2d}{H-1}\\
&\le \frac{4+4d}{p}+\frac{4d}{H}.
\end{aligned}
\]

The last line uses (H/(H-1)\le2) and
(1/(H-1)\le2/H) for (H\ge2). From (H^d\ge p),

\[
H^{-1}\le p^{-1/d},
\qquad
p^{-1}\le p^{-1/d}.
\]

This proves all of (C.1):

\[
\Pr(\mathrm{useful})
\le \frac{4+4d}{p}+\frac{4d}{H}
\le(4+8d)p^{-1/d}.
\]

Using \(\log_2p=n/2+O(1)\), the correct interpretation of (C.2) is

\[
\Pr(\mathrm{useful})
\le 2^{-n/(2d)+O(1)}
=2^{-\Omega(n)}.
\]

No lower bound follows, so the first equality in the displayed wording of
(C.2) must not be read as \(\Theta(2^{-n/(2d)})\).

This proof is uniform in (H); it never assumes that (H) is near (p),
or even that it has polynomial bit length. Thus it covers arbitrary-height
intervals as a probability statement. An algorithmic claim naturally limits
the bit length and the work per stage; allowing numerical-QP bit length is
consistent with that claim.

Finally, independence across stages is unnecessary. If each conditional
useful probability at each reached history is at most
(\varepsilon_n=2^{-\Omega(n)}), then for any bank of at most (Q(n))
stages,

\[
\Pr(\text{some useful stage})
\le Q(n)\varepsilon_n
=2^{O((\log n)^k)-\Omega(n)}
=2^{-\Omega(n)}.
\]

This remains valid when the next (H) is selected adaptively from the full
prior history.

## 5. Reconstruction of Theorem D

Write (B=B(n)). Conditions (D.1) mean

\[
\frac{\log n}{\log B}\longrightarrow0,
\qquad
\frac{\log B}{n}\longrightarrow0.
\]

Since \(\log p=\Theta(n)\), the second relation gives (B<p<q) eventually.
The example (D.2) has \(\log B\asymp(\log n)^3\), so it satisfies both
relations and is numerical-QP.

Let (G=\mathcal G_N(B)), and let
(G_p=\mathcal G_p(B)), (G_q=\mathcal G_q(B)) be its projection images.
All generators are units. A uniform element of a finite group projects
uniformly onto the image of a homomorphism, because all fibers are cosets of
the same kernel. Hence an exact-uniform (a\in G) has exact-uniform local
projection in each of (G_p,G_q), even though those two projections need not
be independent.

Every subgroup of \(\mathbb F_p^\times\) is cyclic. For a cyclic group of
order (m), the equation (z^A=1) has exactly \(\gcd(A,m)\) solutions.
Here \(|G_p|\mid p-1\), and the exponent calculation from Theorem A gives

\[
A\equiv d\pmod{|G_p|}.
\]

Therefore

\[
\Pr(p\mid a^A-1)
=\frac{\gcd(A,|G_p|)}{|G_p|}
=\frac{\gcd(d,|G_p|)}{|G_p|}
\le\frac d{|G_p|},
\]

which is (D.4). At (q), one has (A\equiv-d\pmod{|G_q|}\), but
(\gcd(-d,|G_q|)=\gcd(d,|G_q|)\), so the analogous formula is exact there as
well. This is the second place where retaining the fixed-gap sign matters.

To prove (D.5), take a positive (B)-smooth integer (s\le p). Since
(B<p), (s\ne p), so actually (1\le s\le p-1). Its residue is a product
of the declared prime generators and lies in (G_p). Distinct such integers
give distinct residues modulo (p). Thus

\[
|G_p|\ge\Psi(p,B).
\]

The identical injection for (1\le s\le q-1) proves

\[
|G_q|\ge\Psi(q,B).
\]

For completeness, (D.6) follows under (D.1) from a direct smooth-number
lower bound. Let (x\in\{p,q\}), (y=B),
(u=\log x/\log y\), and (k=\lfloor u\rfloor). Then (u\to\infty).
Let (M=\pi(y)). A standard elementary prime-counting lower bound gives
(M\ge c y/\log y) for all sufficiently large (y). The condition
(\log n=o(\log y)) makes (M\gg k). Every product of a (k)-element subset
of the primes at most (y) is a distinct (y)-smooth integer and is at most
(y^k\le x). Hence

\[
\Psi(x,y)\ge {M\choose k}\ge (M/k)^k.
\]

Now \(k\log y\ge\log x-\log y\), while
(\log k+\log\log y=O(\log n)=o(\log y)\). It follows that

\[
\begin{aligned}
\log\Psi(x,y)
&\ge k\bigl(\log y-O(\log\log y+\log k)\bigr)\\
&=\log x-o(\log x).
\end{aligned}
\]

The trivial upper bound \(\Psi(x,y)\le x\) gives

\[
\Psi(p,B)=p^{1-o(1)},
\qquad
\Psi(q,B)=q^{1-o(1)},
\]

which reconstructs (D.6) without assuming a delicate uniform Dickman
asymptotic.

Because sampled elements are units, the event "proper return or global
return" is exactly the union of the two local return events. A union bound,
not an independence assertion, now gives

\[
\begin{aligned}
\Pr(\text{proper return or global return})
&\le \frac d{|G_p|}+\frac d{|G_q|}\\
&\le \frac d{\Psi(p,B)}+\frac d{\Psi(q,B)}\\
&=2^{-n/2+o(n)}.
\end{aligned}
\]

This proves (D.7). Conditional exact uniformity at each reached history
repeats the same argument verbatim. A numerical-QP union bound remains
(2^{-\Omega(n)}). On the rare global-return histories, Theorem A still
forces every certified common block, and therefore their entire lcm, to
divide (d).

## 6. Reconstruction of (E.1)--(E.3) and the surviving boundary

For a screened unit word value, (A.1) makes the declared return depend only
on

\[
C_X=X^d-1,
\]

which is (E.1). If the word is made only from rational primes below
(B<p), it is automatically a unit. For a more general integer word, this
sentence applies after the initial gcd screen; a nonunit may instead factor
(N) immediately.

For (X>1), (C_X>0). If (C_X<p), neither (p) nor (q) can divide it.
Thus a one-sided return requires

\[
C_X=k_pp
\quad\text{or}\quad
C_X=k_qq
\]

with the corresponding quotient a positive, hence nonzero, integer. This is
(E.2). If (X>1) gives a global return, then (N\mid C_X) and positivity
gives

\[
C_X=kN,
\qquad k\ge1,
\]

which is (E.3). At (X=1), instead, (C_X=0); this is the necessary
exception to the prose following (E.1), and it has already been disposed of
by the exact order-one analysis.

For a nonempty positive word, (X^d<p) is equivalent to total log-height
below \(\log_2p/d\). Therefore any useful unit word source must cross the
linear threshold (B.5), thereby permitting a nonzero modular quotient. It
must also place inverse-numerical-QP mass on a useful subset of the union of
the two local (d)-torsion sets. Exact uniform mass on the full generated
subgroup is exponentially too small by (D.7). Neither requirement is
sufficient: threshold crossing alone creates no divisibility, and membership
in both torsion sets can yield only an order-one return or blocks already
bounded by (d).

## 7. Quantifier and scope audit

- The hostile inputs are only the sufficiently large members of one
  infinite fixed-gap semiprime family. The result is not a lower bound for
  factoring arbitrary integers.
- The constant (d) is selected once. It does not depend on (N), a stage,
  or a history. This is essential both for the lcm ceiling and for the
  exponential bounds.
- Theorem B covers every distribution on a fixed numerical-QP bounded set,
  including adaptive and degenerate distributions, because its assertion is
  pointwise.
- Theorem C covers every exact-uniform prefix interval
  \(\{2,\ldots,H\}\), with (H) selected after any history and with no
  height restriction in the counting argument. It does not cover an
  arbitrary nonuniform distribution on that interval.
- Theorem D grants exact uniformity on the entire generated subgroup and
  asserts no efficient exact sampler. Its projection calculation uses equal
  fibers and a union bound, never independence.
- The word obstruction before (B.5) concerns the unreduced positive integer
  value. It does not by itself control a long, factor-correlated,
  nonuniform modular-word law after wraparound.
- All statements about primary blocks use only the semantic guarantee that a
  certified common block divides both local orders. With that guarantee, the
  lcm ceiling is exact and independent of the number of samples.
- None of these claims supplies the top-level factoring algorithm required
  by the repository prompt.
