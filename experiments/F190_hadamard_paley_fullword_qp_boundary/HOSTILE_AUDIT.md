# Hostile audit of F190

## Integrity and verdict

The frozen package uses **MANIFEST.md**. Its recorded hashes are:

- **STATEMENT.md**:
  `78e8cfd74e5ed824e6bb74c3aacbef0e9af6c67746373aa6e478a77ed9930b38`;
- **PROOF.md**:
  `03a3a80387d43fd9a89e5c5453ac36af7c1dd09133f7029b419cdeacc4dd41bb`;
- **SELF_AUDIT.md**:
  `4a542af975f48836fc168024bab8ce1b339c34d6154ba427d9d79051914e4724`.

Fresh SHA-256 checks reproduced all three hashes. I read all three files in
full. I did not run mathematical computation.

**Verdict: PASS, with one non-fatal interpretation constraint.** Every exact
formula, QP estimate, reduction, and named-model boundary is correct under
its stated hypotheses. The phrase “the birthday scale is
$K=\Theta(\sqrt p)$” must mean the scale at which the union-bound guarantee
in (24) ceases to be small. Equation (24) does not prove a matching collision
threshold for every allocation of $K=Rm$ arguments. For example, one row has
no within-row collision at any screened size. This does not affect the
proved conclusion that QP many arguments have exponentially small collision
probability.

I found no other qualification, hidden squarefreeness assumption, QP leak,
or retained-source overclaim.

## 1. Global quantifiers and QP accounting

For fixed constants $C,k$,

\[
\log_2\mathcal Q(n)=C(\log_2(n+1))^k=o(n).
\]

Thus every fixed QP envelope is $2^{o(n)}$. A fixed product of such
envelopes is still $2^{(\log n)^{O(1)}}$. On a balanced semiprime,

\[
p,q=2^{n/2+O(1)}.
\]

Consequently, every QP shift count, row count, total support, coefficient
norm, polynomial count, and polynomial degree is eventually smaller than
$p$ and $q$. Every expression of the form

\[
\frac{\mathcal Q_1(n)\cdots\mathcal Q_c(n)}{\sqrt N}
\]

is $2^{-n/2+o(n)}$. Conversely, $\varphi(N)$, $N^{1/4}$, and $2^{cn}$ for
fixed $c>0$ are exponential in $n$ and are not QP. The proof applies these
facts consistently.

The definition

\[
n=\lceil\log_2(N+1)\rceil
\]

does imply $2^{n-1}\le N<2^n$. All later conversions between $N$-scale and
$n$-scale lose only constant factors in the exponent.

The exact Fourier, correlation, list, distance, and collision claims are
explicitly restricted to $N=pq$ with distinct odd balanced primes. The proof
does not apply any of them to repeated prime powers.

## 2. Retained-source decoder equivalence

### Transcript generation is public

Given $M$, $X$, and the shifts, every gcd and Jacobi symbol is computable in
polynomial bit complexity. QP many rows and entries therefore cost QP. The
retained row adds no oracle value beyond its retained numerical source.
This observation does not say that joint processing is useless, and F190
does not make that stronger claim.

### Acceptance probability

After trial division through $B=4m(k)k$, every remaining prime divisor
$r$ exceeds $B$ and hence exceeds $m$. Consecutive shifts
$0,\ldots,m-1$ are distinct modulo every such $r$. For a uniform source
modulo $r^e$, exactly an $m/r$ fraction of residues have one shifted
argument divisible by $r$. CRT independence across distinct prime powers
therefore gives

\[
\alpha_M=\prod_{r\mid M}(1-m/r).
\]

Since $\omega(M)\le k$,

\[
1-\alpha_M
\le\sum_{r\mid M}\frac m r
<\frac{mk}{B}=\frac14.
\]

Trial division through a QP bound costs QP. Rejection sampling each accepted
source has constant expected overhead. If a coordinate gcd is a proper
divisor, factoring has already succeeded. If it is $M$, that source is a
public rejection. Thus sampling does not conceal a difficult conditioning
step.

The accepted sources obtained by rejection sampling are independent and
uniform on the accepted set. A factor found while constructing a batch is a
terminal success, not a sampling failure.

### Forward reduction

If one decoder attempt costs at most QP and succeeds with probability at
least inverse-QP, fresh independent attempts have QP expected total cost.
Primality and divisibility checks make the reduction Las Vegas.

A non-perfect-power integer has gcd one among its hidden prime exponents.
Therefore at least one exponent is odd. Exact perfect-power processing
handles the complementary case. Removing powers of two, trial-dividing
small primes, and recursively processing verified proper splits covers all
positive factoring inputs under the standard convention $N\ge2$.

A complete factor tree has $O(k)$ nodes because the total number of prime
factors counted with multiplicity is at most $k$. A polynomial number of
QP node costs remains QP. No unproved one-child recurrence is being used
here.

### Reverse reduction

A Las Vegas QP factorer can ignore the transcript and obtain a prime divisor
of odd exponent from any non-perfect-power composite. If the decoder model
requires a fixed QP time cap rather than expected time, truncate the factorer
at a constant multiple of its expected QP bound. Markov's inequality leaves
constant success probability. Thus the reverse implication also has the
claimed resource bounds.

The equivalence is intentionally narrow. It applies only to a decoder whose
promised output is already a numerical hidden prime. It does not rule out a
weaker structural output.

## 3. Fourier support, recurrence, and Hankel rank

Under CRT, the global additive character factors into local additive
characters. Its local frequency vanishes modulo $r$ exactly when
$r\mid a$. The quadratic Gauss sum is zero at zero frequency and has
magnitude $\sqrt r$ at every nonzero frequency. Hence

\[
\widehat s(a)=0\iff(a,N)>1,
\qquad
|\widehat s(a)|=\sqrt N\iff(a,N)=1.
\]

There are exactly $\varphi(N)$ nonzero modes.

Fourier inversion expresses $s$ as a sum of the distinct exponentials
$t\mapsto\zeta_N^{at}$ for unit $a$, each with nonzero coefficient. If
$P(E)s=0$, linear independence forces $P(\zeta_N^a)=0$ for every unit
$a$. These are precisely the primitive $N$-th roots, so $\Phi_N\mid P$.
Conversely, $\Phi_N(E)$ annihilates every supported mode. The minimal
constant-coefficient complex recurrence order is therefore exactly
$\varphi(N)$.

For the periodic Hankel matrix,

\[
H=V\operatorname{diag}(\widehat s(a)/N)V^{\mathsf T}.
\]

$V$ has full column rank, $V^{\mathsf T}$ has full row rank, and the middle
diagonal matrix is invertible. Hence the product has rank $\varphi(N)$.
There is no cancellation loophole.

Balance gives

\[
\varphi(N)=N-p-q+1=N-O(\sqrt N)=2^{\Theta(n)}.
\]

Thus explicit mode output, a degree-materialized recurrence, and dense
Hankel/Prony/Padé objects are exponential. This is an output-size statement
inside those named models. F190 correctly excludes succinct arithmetic
representations and algorithms that do not materialize those objects.

## 4. Autocorrelation and raw sampling

For an odd prime $r$,

\[
\sum_u\chi_r(u)\chi_r(u+d)
=
\begin{cases}
r-1,&d=0,\\
-1,&d\ne0.
\end{cases}
\]

CRT multiplication gives all four values in (12). The two nontrivial
factor-sensitive values occur exactly when $\gcd(d,N)$ is already a proper
factor. Duplicate shift $d=0$ is removed separately. Thus every nontrivial
difference-screened complete pair correlation is the public value one.

For a unit frequency, the empirical Fourier variable has mean of magnitude
$N^{-1/2}$ and variance $(\varphi(N)-1)/N$. Dividing the variance of an
$R$-sample mean by the squared mean gives exact relative mean-squared error
$(\varphi(N)-1)/R$.

For a unit difference, the empirical autocorrelation variable has mean
$1/N$. Its square is one exactly when neither of two distinct residues is
hit modulo either prime, so

\[
\mathbb EW^2=(1-2/p)(1-2/q)=\rho_d.
\]

The exact relative mean-squared error is
$(N^2\rho_d-1)/R$. Both displayed sample requirements follow. They concern
only the ordinary unbiased empirical averages. They are not lower bounds
against arbitrary estimators, and the statement says so.

## 5. Explicit correlations at QP scale

After collecting multiplicities, let $u$ be the number of distinct shifts.
If some multiplicity is odd, remove the roots arising only from even
multiplicities from the complete squarefree character sum. The local sum is
bounded by $(u-1)\sqrt r$. CRT therefore gives

\[
|\mathbb EY_H|\le\frac{(u-1)^2}{\sqrt N}.
\]

If every multiplicity is even, the monomial is one exactly when all $u$
arguments are units. Its mean and deviation from the constant-one baseline
are exactly

\[
(1-u/p)(1-u/q),
\qquad
\frac{u(p+q-u)}N.
\]

On the balanced family both branches have
$O(u^2/\sqrt N)$ drift. Multiplying by a QP coefficient
$\ell_1$-norm and a QP support bound gives

\[
\frac{\mathcal Q(n)^3}{\sqrt N}=2^{-n/2+o(n)}.
\]

The earlier P53 sequential bound has pathwise error

\[
\frac{2\Lambda T+T^2/2}{\sqrt N}.
\]

F190 uses $\Lambda=\sqrt2$ and changes only $T$ from polynomial to a fixed
QP envelope. The proof of P53 depends on $T$ through this displayed
polynomial expression, so substitution gives
$2^{-n/2+o(n)}$ without changing its hypotheses.

The exclusions are essential and correctly repeated. This argument releases
one scalar per fresh source. It does not retain the source, retain a row,
make several decisions on a row, or control a succinct statistic with a
non-QP Walsh expansion.

## 6. Short-puncture exact lists

For nonempty $S$, the selected linear factors are distinct. Their product is
squarefree. The complete quadratic-character sum has magnitude at most
$(|S|-1)\sqrt r$. Excluding the $m-|S|$ roots associated with shifts outside
$S$ changes that sum by at most $m-|S|$. Therefore

\[
|B_r(S)|
\le (|S|-1)\sqrt r+(m-|S|)
\le(m-1)\sqrt r.
\]

The empty sum is exactly $r-m$.

On the accepted domain, expansion of the exact sign indicator gives (17).
The factor $2^{-m}$ cancels the count of at most $2^m-1$ nonempty terms, so
the stated uniform local error follows.

The same indicator expansion for a pair of local words gives (18).
Every nonempty product is at most $(m-1)^2\sqrt N$. Again, the normalized
sum of $2^m-1$ such errors is at most
$(m-1)^2\sqrt N$, which proves (19).

If $m\le(1/2-\delta)\log_2N$, the ratio of this error to the main term is

\[
O\!\left(\frac{m^2 2^m}{\sqrt N}\right)
\le O(m^2N^{-\delta})=o(1).
\]

Also, $(p-m)(q-m)=N(1-o(1))$. This proves (21) uniformly for every product
word.

The equivalence

\[
2^m\text{ is QP}\iff m=(\log n)^{O(1)}
\]

is exact up to fixed envelopes. In this regime,
$N/2^m=2^{n-o(n)}$, so every exact row-only list is exponential. If
$N/2^m$ is at most QP, then

\[
m\ge\log_2N-(\log n)^{O(1)}=n-(\log n)^{O(1)},
\]

and brute sign splitting costs $2^{\Theta(n)}$.

This last entropy implication does not extend the character-sum estimate to
$m$ near $n$. The statement explicitly avoids that inference. The list
counts pairs of local sources, equivalently global sources under CRT, but it
forgets the retained numerical label. It is therefore only a row-only
obstruction. No source-aware indistinguishability claim follows.

## 7. Long-word distance

For fixed distinct sources $x,z$, the complete quadratic-character identity
gives agreement minus disagreement equal to $-1$ on the $r-2$ shifts where
both symbols are nonzero. Hence the exact disagreement count is
$(r-1)/2$.

For $m$ uniformly selected distinct shifts, the number of these
disagreements is hypergeometric with mean

\[
\mu=m\frac{r-1}{2r}\ge m/3.
\]

The lower-tail bound gives probability at most $e^{-m/24}$ that this count
is below $m/6$. A union bound over fewer than $r^2/2$ source pairs and
$m\ge96\ln r$ gives failure probability below $r^{-2}$. Positions where
one symbol is zero were not counted as successes, so they cannot invalidate
the Hamming-distance lower bound.

Thus $O(\log r)$ columns can make the local code injective and give constant
relative distance. This is a random-column existence theorem. It is not a
claim about fixed consecutive columns, a public simultaneous construction
for both hidden primes, or an efficient modulus-blind decoder.

## 8. Independent collisions

Conditioning a uniform global source on row acceptance leaves independent
uniform local coordinates on

\[
U_r=\mathbb F_r\setminus\{-a_1,\ldots,-a_m\}.
\]

Different accepted rows remain independent. For two arguments in different
rows and a fixed first source coordinate, at most one value of the second
coordinate creates equality modulo $r$. Thus its probability is at most
$1/(r-m)$. Difference screening makes within-row equality impossible.
A union bound over all argument pairs and both primes gives (24).

Since $K,m=2^{o(n)}$ while $p,q=2^{n/2+O(1)}$, the right side is
$2^{-n/2+o(n)}$. A local but nonglobal equality exposes the same hidden
prime through the gcd of the public argument difference.

As noted in the verdict, $K=\Theta(\sqrt p)$ is the threshold of this
worst-case union-bound expression. It is not a proved matching collision
threshold for every structured division of $K$ into rows and shifts. Only
the former reading is used in the QP obstruction.

## 9. Bounded-degree correlated equalities

On a no-factor coefficient-screening branch, each coefficient is either
zero modulo both hidden primes or a unit modulo both. A polynomial not
discarded as zero modulo $N$ therefore has a unit coefficient and is
nonzero in both local fields.

For sufficiently large $n$, $D<p,q$. The elementary field root bound gives
at most $D$ roots locally. Uniformity of a fresh $Z\bmod N$ and a union
bound over $H$ polynomials and two primes prove

\[
\Pr[\text{some local root}]
\le HD(1/p+1/q)=2^{-n/2+o(n)}.
\]

Conditioning on any acceptance event of probability at least a fixed
positive constant multiplies this bound by at most the inverse constant.
For a past-adaptive menu, fixing the past makes the menu deterministic while
the new source remains fresh. Thus the same argument applies conditionally.
Polynomial differences $g_i-g_j$ cover the stated QP family of
bounded-degree equality tests.

The proof does not apply the degree bound to a succinct exponential-degree
polynomial, a rational relation with poles, or repeated nonlinear use of one
retained source. These mechanisms remain open.

## 10. Final scope audit

F190 proves a collection of model-specific boundaries:

- retained-prime output is QP-equivalent to factoring;
- dense Fourier, recurrence, and Hankel materialization is exponential;
- screened complete pair correlations contain no new factor-sensitive
  value;
- raw empirical Fourier and autocorrelation averages need exponential
  samples;
- explicitly expanded QP-support scalar correlations retain exponentially
  small drift;
- QP-width row-only punctures have exponentially large exact lists;
- QP many independent local-coordinate collision tests remain exponentially
  sparse;
- QP many QP-degree polynomial equality tests on a fresh source remain
  exponentially sparse.

It does **not** prove a generic lower bound for arithmetic circuits, full-row
algorithms, retained-source processing, high Walsh degree, succinct
characteristic-scale operations, or modulus-blind Paley-product
decomposition. The good-distance theorem specifically prevents an
information-theoretic closure of the long-word regime. The surviving
interface in Section 7 is therefore accurate and genuinely open.
