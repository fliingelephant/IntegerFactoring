# F225 blind reconstruction

## Verdict

**PASS**, with Theorem B's numerical bounds read under the standing
hypothesis `c>=3` introduced before Theorem A.  The exact XOR probability
identities themselves do not need that hypothesis.  The case `c=1` is
outside the sparse-root claim and is addressed explicitly below.

Verified statement SHA-256, computed before reading any F225 file:

```text
57a0764b549a79a5a725612b95a6f57b41791760bc6a1a2d188354041d6b1a20
```

This reconstruction used only `PROMPT.md` for workflow context and the
hash-matched F225 `STATEMENT.md` for mathematical content.  It did not use a
proof, audit, result, provenance, manifest, ledger, or another agent's work.
No mathematical computation was run.

## Standing facts

Let

\[
N=pq,\qquad p<q<2p,
\]

where `p` and `q` are distinct odd primes, and let

\[
c=2p-q,\qquad d=q-p=p-c.
\]

The inequalities give `0<c<p`.  Since `2p` is even and `q` is odd, `c` is
odd.  Under `c>=3`,

\[
k=c-2\ge1,\qquad s={c+1\over2}\ge2.
\]

Also `s<q`; in fact `c<p<q`, so `(c+1)/2<q`.  These facts ensure that all
degree arguments below concern nonzero polynomials.

Write

\[
H_N(X)=(X+1)^N-X^N-1.
\]

Because `N` is odd, both exceptional points are roots in either local
field:

\[
H_N(0)=0,\qquad H_N(-1)=0.
\]

They are distinct because both fields have odd characteristic.

## Theorem A: reconstruction modulo `p`

Frobenius in \(\mathbb F_p\) gives \(a^p=a\) for every `a`.  Hence, as
functions on \(\mathbb F_p\),

\[
H_N(x)=(x+1)^q-x^q-1.
\]

For \(x\notin\{0,-1\}\), both `x` and `x+1` are nonzero.  Since

\[
q=2p-c=2(p-1)-(c-2)=2(p-1)-k,
\]

Fermat's theorem gives

\[
(x+1)^q=(x+1)^{-k},\qquad x^q=x^{-k}.
\]

Multiplication by the nonzero element \([x(x+1)]^k\) is reversible.
Therefore

\[
\begin{aligned}
H_N(x)=0
&\iff (x+1)^{-k}-x^{-k}-1=0\\
&\iff x^k-(x+1)^k-[x(x+1)]^k=0\\
&\iff P_k(x)=0.
\end{aligned}
\]

Together with the two exceptional roots, this proves the exact, disjoint
decomposition

\[
A_p=2+\#\{x\in\mathbb F_p\setminus\{0,-1\}:P_k(x)=0\}.
\]

The term \(-[X(X+1)]^k\) has degree `2k` and leading coefficient `-1`.
The other two terms have degree at most `k`.  Thus `P_k` is nonzero of
degree exactly `2k`.  A nonzero polynomial over a field has at most its
degree many roots, even when that degree exceeds the field size.  It
follows that

\[
A_p\le2+2k=2c-2.
\]

## Theorem A: reconstruction modulo `q`

Frobenius in \(\mathbb F_q\) instead gives, as functions on
\(\mathbb F_q\),

\[
H_N(x)=(x+1)^p-x^p-1.
\]

The relation `q=2p-c` and the definition of `s` imply

\[
p={q+c\over2}={q-1\over2}+s.
\]

For nonzero \(a\in\mathbb F_q\), Euler's criterion therefore gives

\[
a^p=a^{(q-1)/2}a^s=\chi(a)a^s.
\]

Consequently, for \(x\notin\{0,-1\}\), the unique pair

\[
(\epsilon,\delta)=(\chi(x+1),\chi(x))\in\{\pm1\}^2
\]

satisfies

\[
H_N(x)=0
\iff
\epsilon(x+1)^s-\delta x^s-1=0
\iff Q_{\epsilon,\delta}(x)=0.
\]

Every nonexceptional point has exactly one character pair, so the four
restricted sets are pairwise disjoint and exhaust all nonexceptional
roots.  Adding `0` and `-1` proves the exact decomposition

\[
A_q=2+\sum_{\epsilon,\delta\in\{\pm1\}}
\#\left\{
\begin{array}{c}
x\in\mathbb F_q\setminus\{0,-1\}:\\
\chi(x+1)=\epsilon,\ \chi(x)=\delta,\\
Q_{\epsilon,\delta}(x)=0
\end{array}
\right\}.
\]

It remains to count degrees without losing two roots.  If
`epsilon != delta`, then the coefficient of \(X^s\) is
`epsilon-delta`, which is nonzero because `q` is odd.  Each of these two
polynomials has degree `s`.  If `epsilon=delta`, the degree-`s` terms
cancel and the coefficient of \(X^{s-1}\) is `epsilon*s`.  This is
nonzero modulo `q` because `0<s<q`.  Each of these two polynomials has
degree exactly `s-1`.  Thus the four polynomials have at most

\[
2s+2(s-1)=4s-2=2c
\]

roots in total before the character restrictions are imposed.  Adding
the two exceptional roots gives

\[
A_q\le2c+2.
\]

This degree split is essential.  Bounding all four polynomials by degree
`s` would give a weaker bound by two.

## Theorem B: uniform-residue XOR law

For uniform \(x\bmod N\), CRT identifies `x` with independent uniform
coordinates in \(\mathbb F_p\) and \(\mathbb F_q\).  Put

\[
\alpha={A_p\over p},\qquad \beta={A_q\over q}.
\]

Because `N=pq` is squarefree with exactly two prime factors,
\(\gcd(H_N(x),N)\) is proper and nontrivial exactly when `H_N(x)` is zero
in one local field and nonzero in the other.  This is the XOR event.
Independence gives

\[
\Pr(1<\gcd(H_N(x),N)<N)
=\alpha(1-\beta)+\beta(1-\alpha).
\]

Under `c>=3`, Theorem A gives

\[
\begin{aligned}
\Pr(1<\gcd(H_N(x),N)<N)
&\le \alpha+\beta\\
&\le {2c-2\over p}+{2c+2\over q}\\
&\le {4c\over p},
\end{aligned}
\]

where the last step uses `q>p`.

## Theorem B: uniform-unit XOR law

Uniform choice from \(U(N)\) becomes independent uniform choice from
\(\mathbb F_p^\times\) and \(\mathbb F_q^\times\) under CRT.  Exactly one
local root, namely `0`, has been removed from each field.  The other
exceptional root `-1` remains a unit.  Hence the two local root
probabilities are exactly

\[
\alpha_U={A_p-1\over p-1},\qquad
\beta_U={A_q-1\over q-1}.
\]

The same XOR argument proves

\[
\Pr(1<\gcd(H_N(x),N)<N\mid x\in U(N))
=\alpha_U(1-\beta_U)+\beta_U(1-\alpha_U).
\]

Using Theorem A and `q>p`,

\[
\begin{aligned}
\Pr(1<\gcd(H_N(x),N)<N\mid x\in U(N))
&\le\alpha_U+\beta_U\\
&\le {2c-3\over p-1}+{2c+1\over q-1}\\
&\le {4c-2\over p-1}.
\end{aligned}
\]

The subtraction of one, rather than two, in each local numerator is
forced by the fact that `-1` is still in the multiplicative group.

### Exact unit sampling by gcd screening

If `X` is uniform modulo `N`, then conditioning on
\(\gcd(X,N)=1\) gives the uniform distribution on `U(N)`: every unit had
the same unconditional mass `1/N`.  A proper nonunit is already a
factor-finding success.  Its exact probability is

\[
{(q-1)+(p-1)\over pq}
={1\over p}+{1\over q}-{2\over pq}
=O(1/p).
\]

The only remaining nonunit outcome is `X=0 mod N`, whose gcd is `N`; it
can be rejected and resampled.  Thus screening implements exact uniform
unit sampling on the branch where it has not already returned a factor.
For the family below, the screening-success probability is smaller than
the scalar channel's \(O(p^{-2/5})\) upper bound and does not alter the
obstruction.

## Theorem C: the BHP family with explicit quantifiers

The external prime-gap input used here is the following quantified form
of the Baker--Harman--Pintz theorem:

> There is a constant \(X_0\) such that, for every real
> \(X\ge X_0\), the interval \([X-X^{0.525},X]\) contains a prime.

For each odd prime `p`, define

\[
m_p=\lfloor p^{3/5}\rfloor,\qquad X_p=2p-m_p.
\]

As `p` tends to infinity through the primes, `X_p` tends to infinity.
Therefore there is `p_0` such that for every odd prime `p>=p_0`, BHP
supplies at least one prime `q` satisfying

\[
X_p-X_p^{0.525}\le q\le X_p.
\]

For all sufficiently large `p`,

\[
2p-p^{3/5}-(2p)^{0.525}>p.
\]

Since `m_p<=p^(3/5)` and `X_p<=2p`, this implies the lower endpoint of
the BHP interval is greater than `p`.  The upper endpoint is strictly
less than `2p`.  Thus every chosen `q` is an odd prime with

\[
p<q<2p.
\]

The endpoint inequalities give exact bounds on `c`:

\[
m_p\le c=2p-q\le m_p+X_p^{0.525}.
\]

Because \(m_p=p^{3/5}+O(1)\), \(X_p^{0.525}=O(p^{0.525})\), and
`0.525<3/5`,

\[
c=\Theta(p^{3/5}).
\]

In particular, `c>=3` for all sufficiently large members of the family.
Also

\[
d=q-p=p-c=p-\Theta(p^{3/5})=\Theta(p).
\]

More concretely, `d>=p/2` eventually.  Hence `d>=p^(2/3)` eventually,
which is stronger than the stated regime \(d\ge p^{2/3-o(1)}\).

Theorem B now gives, for one fresh uniform residue,

\[
\Pr(1<\gcd(H_N(x),N)<N)
\le {4c\over p}=O(p^{-2/5}).
\]

The uniform-unit bound has the same order.  Since

\[
p^2<N=pq<2p^2,
\]

for \(n=\lceil\log_2N\rceil\) one has
`log_2(p)=Theta(n)`.  In particular,
\(p^{-2/5}=2^{-\Omega(n)}\).  The fact that the prompt's input-length
convention can also be written \(\lceil\log_2(N+1)\rceil\) causes no
difference here: `N` is odd and is not a power of two, so the two
expressions agree.

## Fresh-uniform adaptive banks

Let the history before trial `i` include all earlier sampled points,
scalar values, gcd results, and the decision whether to continue.  A
trial is *fresh uniform* if, conditional on this entire history and on
the trial being executed, its new point is still uniform on the chosen
allowed domain (all residues or all units).  The decision to stop or
continue may be adaptive; the conditional distribution of the new point
may not be biased.

For the BHP family there are fixed constants `a>0` and `K>0` such that
the conditional probability of an individual proper-gcd event on every
executed fresh-uniform trial is at most

\[
\rho_n=K2^{-an}
\]

for all sufficiently large `n`.  If at most

\[
T(n)\le 2^{C(\log_2(n+1))^k}
\]

trials are executed, the conditional union bound gives

\[
\Pr(\text{some individual gcd succeeds})
\le T(n)\rho_n
\le 2^{C(\log_2(n+1))^k-an+O(1)}
=2^{-\Omega(n)},
\]

because every fixed power of `log(n+1)` is `o(n)`.  The same proof works
for an adaptive random trial count `tau` with
\(\mathbb E[\tau]\le T(n)\): summing the conditional probabilities of
the executed trials gives at most \(\rho_n\mathbb E[\tau]\).  Adding the
gcd-screening event for raw residue samples contributes only
`O(1/p)=2^(-Omega(n))` per executed trial, so the conclusion is unchanged.

This argument permits adaptive stopping and a history-dependent choice
between the two allowed uniform sampling procedures.  It does not permit
the history to bias the next point, and it says nothing about extracting
information by jointly processing nonzero scalar values.

## Edge cases and exact scope

- The hypothesis `c>=3` excludes exactly the possible positive odd case
  `c=1`.  This exclusion is necessary.  When `c=1`, one has
  `q=2p-1` and `q` is congruent to `1 mod (p-1)`.  The same local
  reduction shows that `H_N` vanishes at every point of
  \(\mathbb F_p\), so `A_p=p`; the sparse bound for `A_p` does not extend
  to this case.  Thus Theorem B's displayed upper bounds must inherit the
  `c>=3` hypothesis.  The exact XOR identities remain valid for any
  local root counts.
- The points `0` and `-1` are handled before division or use of Euler's
  criterion.  No inversion is applied at either point.
- The construction of Theorem C discards only finitely many small `p`.
  This is sufficient for an unbounded hostile family and ensures
  `p<q<2p`, oddness, distinctness, and `c>=3` simultaneously.
- The proved obstruction concerns distinct odd semiprimes in the stated
  near-balanced range.  It makes no claim for prime inputs, prime powers,
  repeated-prime composites, even inputs, or general unbalanced
  composites.
- The channel is exactly the public shift `1`, a fresh uniform residue or
  unit, and an individual gcd of each scalar `H_N(x)` with `N`, repeated
  only a numerical-quasipolynomial number of times.
- It does not rule out a carry-biased or otherwise nonuniform point
  distribution, an adaptively constructed point whose distribution uses
  observed values, joint processing of typical nonzero values,
  coefficient-vector information, quotient-ring ranks, or a method that
  certifies a new contribution to a common modulus `M`.
- Consequently this is a channel-specific obstruction, not a factoring
  algorithm and not an impossibility theorem for the other listed
  mechanisms.

Subject to the explicit standard BHP input and the inherited `c>=3`
scope, all exact identities, root bounds, family quantifiers, and
probability conclusions in the statement follow.
