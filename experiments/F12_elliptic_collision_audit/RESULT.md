# Hostile audit of F12 elliptic collision and torus reduction

## Verdict

The two central mathematical results survive:

1. For `m >= 3`, the cleared elliptic `x`-collision product vanishes exactly
   when the affine point order is at most `2m-1`.  At
   `N=101*103`, `m=floor(sqrt(N))=101`, Hasse therefore forces simultaneous
   vanishing for every short Weierstrass curve good at both primes and every
   global affine point.  The retained denominator-clean witness is correct.
2. A uniform exact evaluator for the torus product

   \[
   S_m(a)=\prod_{d=1}^{m-1}(1-a^d)^{m-d}\pmod N
   \]

   in time polynomial in `log N + log m` would give a classical Las Vegas
   polynomial-time factorer for every integer.

Neither result is an unconditional factoring algorithm.  The elliptic product
fails separation on the balanced certificate, and no polylogarithmic evaluator
for the torus product is supplied.

Three corrections narrow the original prose:

- the elliptic order trichotomy needs `m >= 3` (it is false at `m=2` for a
  point of order 2);
- a bad discriminant gives a factor only when its gcd with `N` is proper;
  `gcd(discriminant,N)=N` is possible and is merely a retry case;
- `O(n^2 T(n))` is the expected cost of one conditional split, not the entire
  recursive factorization.  A simple all-recursion bound is
  `O(n^3 T(O(n)) + poly(n))`, still polynomial.

## 1. Division-polynomial identity and signs

Use the standard convention

\[
\psi_1=1,\qquad
\phi_r=x\psi_r^2-\psi_{r+1}\psi_{r-1},\qquad
x([r]P)=\frac{\phi_r(P)}{\psi_r(P)^2},
\]

with the full factor `2y` in even division polynomials.  The standard addition
recurrence is

\[
\psi_{u+v}\psi_{u-v}
=\psi_{u+1}\psi_{u-1}\psi_v^2
 -\psi_{v+1}\psi_{v-1}\psi_u^2.
\]

For `1 <= i < j`, take `u=j`, `v=i`.  Direct substitution gives

\[
\begin{aligned}
\phi_i\psi_j^2-\phi_j\psi_i^2
&=\psi_{j+1}\psi_{j-1}\psi_i^2
  -\psi_{i+1}\psi_{i-1}\psi_j^2\\
&=\boxed{\psi_{i+j}\psi_{j-i}}.
\end{aligned}
\]

Thus the sign in F12 is correct for its ordered difference
`x([i]P)-x([j]P)`.  Reversing the Vandermonde convention would reverse the
sign.  The argument is in the coordinate ring of a nonsingular short
Weierstrass curve in characteristic different from 2 and 3.

Consequently

\[
C_m=\prod_{1\le i<j\le m}\psi_{i+j}\psi_{j-i}.
\]

The difference index `d` occurs `m-d` times.  For a sum index `s`, the allowed
first index satisfies

\[
\max(1,s-m)\le i\le\left\lfloor\frac{s-1}{2}\right\rfloor,
\]

so its multiplicity is

\[
c_s=\max\left(0,
\left\lfloor\frac{s-1}{2}\right\rfloor-max(1,s-m)+1\right).
\]

The combined exponent of `psi_k` is

\[
e_k=\mathbf 1_{1\le k\le m-1}(m-k)+c_k.
\]

For `m >= 3`, `e_k>0` for every `2 <= k <= 2m-1`, and no nonconstant index
outside that interval occurs.  The `k=1` factor is harmless because
`psi_1=1`.

For an affine point of order `t`,

\[
\psi_k(P)=0\quad\Longleftrightarrow\quad [k]P=O
\quad\Longleftrightarrow\quad t\mid k.
\]

An affine point has `t>=2`.  Hence, for `m>=3`,

\[
C_m(P)=0\quad\Longleftrightarrow\quad t\le2m-1,
\]

while all denominators through `m` are nonzero exactly when `t>m`.  This gives
the stated three cases:

| point order | denominators through `m` | `C_m` |
|---|---|---|
| `t <= m` | at least one zero | zero |
| `m < t <= 2m-1` | all nonzero | zero |
| `t > 2m-1` | all nonzero | nonzero |

In the middle case, `(i,j)=(t-m,m)` satisfies `1<=i<j<=m` and `i+j=t`, so
the collision is exactly the ambiguity `x(Q)=x(-Q)`.

The restriction `m>=3` is real: for `m=2`, `C_2=psi_3`, so a point of order
2 has a zero denominator but generally `C_2 != 0`.  This does not affect the
F12 instance, where `m=101`.

## 2. Universal Hasse synchronization and the clean witness

For good reduction modulo a prime `ell`, every point order is at most

\[
\#E(\mathbf F_\ell)\le
\left\lfloor\ell+1+2\sqrt\ell\right\rfloor.
\]

For

\[
N=10403=101\cdot103,qquad m=101,qquad 2m-1=201,
\]

the two integral Hasse upper bounds are 122 and 124.  Every affine local point
therefore has order in `[2,201]`, independently of the curve or point
distribution.  The preceding theorem forces

\[
C_m(P)=0\pmod {101},\qquad C_m(P)=0\pmod {103}.
\]

Since `N` is squarefree, `C_m(P)=0 mod N` and its gcd with `N` is `N`.
This proves the universal failure for every short Weierstrass curve with good
reduction at both primes and every global affine point.

The retained witness is also correct:

\[
E:y^2=x^3+x+5,qquad P=(5461,5889)\pmod {10403}.
\]

Its discriminant is `-16(4+27*25)`, congruent to 9942 modulo `N`, and is a
unit.  CRT gives

| prime | local point | group order | point order | first collision at `m=101` |
|---:|---:|---:|---:|---:|
| 101 | `(7,31)` | 112 | 112 | `(11,101)` |
| 103 | `(2,18)` | 106 | 106 | `(5,101)` |

Both orders are strictly between 101 and 201.  Thus all multiples through 101
are affine, while the two collision-index sums equal the respective orders.
The independent audit recomputed the curve cardinalities, point orders, all
multiples, 45 and 48 floor-length collisions, and division-polynomial values
using only integer modular arithmetic.

The original singular-curve aside was too absolute.  If
`1 < gcd(discriminant,N) < N`, the discriminant exposes a factor.  If the
curve is singular at both primes, that gcd can be `N`; no factor has yet been
obtained, and Hasse's elliptic-curve argument does not apply.  An algorithm can
reject and resample such a curve, but the universal counterexample is exactly
the good-reduction statement above.

## 3. Elliptic probability formula

For

\[
G\cong\mathbf Z/a\mathbf Z\times\mathbf Z/b\mathbf Z,qquad a\mid b,
\]

the number killed by multiplication by `e` is

\[
|G[e]|=\gcd(e,a)\gcd(e,b).
\]

Möbius inversion therefore gives the exact-order count

\[
B_G(d)=\sum_{e\mid d}\mu(d/e)\gcd(e,a)\gcd(e,b).
\]

If `alpha_G(T)` is the proportion of all group points of order at most `T`,
then for fixed groups and independent uniform local points, exact-one-side
vanishing has probability

\[
\alpha_{G_p}(T)(1-\alpha_{G_q}(T))
+(1-\alpha_{G_p}(T))\alpha_{G_q}(T),
\qquad T=2m-1.
\]

For affine points, identity must be removed from numerator and denominator.
Any curve distribution can be averaged over its joint local group
distribution provided the stated conditional point sampling is retained.  On
the balanced F12 instance every nonidentity local point has order at most
`T`, so both proportions are 1 and the separation probability is exactly
zero without any independence assumption.

## 4. Torus Vandermonde identity and off-by-one threshold

With the explicit orientation used in F12,

\[
\begin{aligned}
D_m(a)
&=\prod_{0\le i<j<m}(a^i-a^j)\\
&=a^{\sum_{i<j}i}\prod_{i<j}(1-a^{j-i})\\
&=\boxed{a^{\binom m3}
\prod_{d=1}^{m-1}(1-a^d)^{m-d}}.
\end{aligned}
\]

Here `sum_(i<j) i = binomial(m,3)`, and a difference `d` occurs `m-d`
times.  There is no missing sign for this orientation.

For a unit of multiplicative order `t` modulo a prime,

\[
S_m(a)=0\quad\Longleftrightarrow\quad
t\mid d\text{ for some }1\le d\le m-1
\quad\Longleftrightarrow\quad t\le m-1.
\]

Thus nonvanishing begins at `t=m`, exactly as claimed.

## 5. Distinct-semiprime probability

Let `N=pq`, `p<q`, and `m=floor(sqrt(N))`.  Then

\[
p\le m<q.
\]

For every unit, its order modulo `p` is at most `p-1<=m-1`, so `p` divides
`S_m(a)`.  Modulo `q`, the product is nonzero exactly when the order is at
least `m`.  Since `F_q^*` is cyclic, a uniform local unit has exact order `d`
for exactly `phi(d)` residues.  Therefore the exact conditional probability
of the proper gcd `p` is

\[
\boxed{\frac1{q-1}
\sum_{\substack{d\mid q-1\\d\ge m}}\varphi(d)}.
\]

The two retained values, `16/51` for `101*103` and `3/5` for `11*101`, were
independently reproduced exhaustively.

Primitive residues give the lower bound `phi(q-1)/(q-1)`.  If
`r_1<...<r_k` are the distinct prime divisors of `t`, then `r_i>=i+1` and

\[
\frac{t}{\varphi(t)}
=\prod_i\frac{r_i}{r_i-1}
\le\prod_i\frac{i+1}{i}=k+1
\le1+\log_2t.
\]

Hence the inverse-log lower bound is valid.

Sampling uniformly from `1,...,N-1` and taking a gcd first is also sound.  A
nonunit gives a proper gcd because zero itself was excluded.  Conditional on
being a unit, CRT gives independent uniform local residues.  If `u` is the
conditional primitive-residue success probability, total success is
`1-Pr(unit)+Pr(unit)*u >= u`.  Thus every trial succeeds with probability at
least `1/(1+log_2 N)`.

## 6. Conditional all-input reduction

First use deterministic primality testing and exact perfect-power detection.
A detected perfect power supplies a verified proper root divisor.  If the
remaining composite is not a perfect power, it has at least two distinct prime
divisors.  Write its unknown factorization as

\[
N=\prod_i p_i^{e_i},\qquad s=\sum_i e_i.
\]

Because at least two distinct primes occur, the weighted geometric mean is
strictly between the extreme primes:

\[
p_{\min}<N^{1/s}<p_{\max}.
\]

Consequently

\[
p_{\min}\le m_s:=\lfloor N^{1/s}\rfloor<p_{\max}.
\]

Also `2<=s<=n`, where `n` is the bit length, since `N>=2^s`.  The algorithm
does not need `s`: it computes exact integer floors

\[
m_k=\lfloor N^{1/k}\rfloor,qquad 2\le k\le n,
\]

once, skipping values below 2.

On a unit whose residue modulo `q=p_max` is primitive, at the hidden index
`k=s`:

- modulo `p_min`, every unit order is at most `p_min-1<=m_s-1`, so
  `p_min | S_(m_s)(a)`;
- modulo `q`, the order is `q-1>=m_s`, so `q` does not divide the product.

Thus the gcd is nontrivial and proper even with repeated prime powers: it
contains at least one copy of `p_min` and no copy of `q`.  Other prime powers
may also enter, which does not affect correctness.  Every returned divisor is
verified by gcd and divisibility.

Assume an exact uniform evaluator with cost `T(L)=poly(L)` on inputs of total
bit length `L=O(log N+log m)`.  At a node of bit length at most `n`, one trial
uses at most `n` evaluator calls.  The inverse-log bound gives at most `n+1`
expected trials, so one split costs

\[
O(n^2T(O(n))+\operatorname{poly}(n))
\]

in expectation, including exact roots, sampling, gcds, and verification.
Independent resampling gives almost-sure termination.

A complete factorization tree has at most `n` leaves counted with
multiplicity and fewer than `n` internal split nodes.  A coarse uniform bound
for complete recursion is therefore

\[
O(n^3T(O(n))+\operatorname{poly}(n)).
\]

Linearity of expectation suffices; independence between recursive node costs
is unnecessary.  This repairs the cost scope while preserving polynomiality.

## 7. Exact scope of the missing evaluator

Maintaining the current power `a^m`, the displayed recurrence

\[
S_{m+1}=S_mP_m,
\qquad
P_{m+1}=P_m(1-a^{m+1})
\]

is an `O(m)`-iteration evaluation algorithm.  Calling it `Theta(m)` describes
that explicit recurrence, not the complexity of the function.

The cyclotomic collection is algebraically correct:

\[
S_m(a)=(-1)^{\binom m2}
\prod_{e=1}^{m-1}\Phi_e(a)^{
h_em-e h_e(h_e+1)/2},
\qquad h_e=\left\lfloor\frac{m-1}{e}\right\rfloor.
\]

It still displays `m-1` factors and does not itself construct a
polylogarithmic evaluator.  Conversely, neither this observation, polynomial
degree, failed divide-and-conquer closure, nor the linear recurrence proves an
`Omega(m)` circuit or bit-complexity lower bound.  The only justified claim is
conditional:

> A uniform exact polylogarithmic evaluator would imply factoring; no such
> evaluator is constructed here, and no impossibility theorem is proved.

## 8. Source, output, hash, and failure audit

The independent named run `R01_artifact_and_certificate_audit` passed under a
60-second hard timeout.  It established:

- all six successful-source SHA-256 values exactly match the manifest;
- all six successful JSON outputs parse, and the five hashes embedded in R10
  exactly match fresh hashes;
- R03 and R08 are invalid partial JSON exactly as disclosed;
- R02 and R05 have no output artifact, exactly as disclosed;
- all four failure logs contain the stated exception/assertion signatures;
- the six successful combined logs are retained but empty;
- the elliptic and torus numerical certificates independently recompute.

There are two provenance limitations:

1. The source revisions that produced failed runs R02, R03, R05, and R08 were
   subsequently repaired at the same paths and were not separately retained or
   hashed.  Their logs and partial outputs verify the failure *kind*, but the
   exact failed executions cannot be replayed from the retained source tree.
   These runs must remain diagnostic history and are not mathematical evidence.
2. Sage left five generated `.sage.py` files.  They were not listed in the
   original manifest and may be overwritten by later Sage runs.  The audit
   records their current hashes, but correctly treats the hashed `.sage`
   sources—not generated intermediates—as authoritative.

Empty success logs also do not independently attest an exit status or Sage
version; those facts come from the manifest.  Complete hashed outputs and the
fact that the successful source writes only after all assertions make the
mathematical certificate chain consistent, while the fresh audit supplies an
independent recomputation.

## Corrected strongest theorem

The strongest supported statement is:

> **Corrected F12 theorem.** For `m>=3`, on a nonsingular short Weierstrass
> curve in characteristic other than 2 or 3, the cleared product of all
> `x([i]P)-x([j]P)` for `1<=i<j<=m` vanishes at an affine point `P` exactly
> when `ord(P)<=2m-1`; its denominators through `m` are all nonzero exactly
> when `ord(P)>m`.  Hence at `N=101*103`, `m=101`, every curve good at both
> primes and every global affine point gives gcd `N`, including the verified
> denominator-clean witness above.  Separately, if `S_m(a) mod N` has a
> uniform exact evaluator polynomial in `log N+log m`, complete integer
> factoring is classical Las Vegas polynomial time by the hidden-total-
> multiplicity scan and inverse-log primitive-residue probability.

The elliptic statement does not cover curves bad at both prime factors,
denominator-based ECM, other coordinates, or other orbit lengths.  The torus
statement is a reduction to an unconstructed evaluator, not progress on that
evaluator and not a lower bound against one.

