# F145 hostile audit — PASS

## Frozen inputs

I audited the complete proof-only candidate with hashes

- STATEMENT.md:
  c00dfc7f43a2ec5fc5b39841a140f744a046f2e31f580d7c430e23963eb8e6bd;
- PROOF.md:
  3837fa6cbd0b5b93700c26b0834998133e3ff181fa61afafb5b70254f2d49b40.

Both hashes matched before the audit. I did not modify either frozen file. I
used no research computation.

## Verdict

**PASS.** I found no false theorem, missing hypothesis, or complexity
overclaim in the frozen candidate.

F145 is a boundary result. It is not a factoring algorithm and it is not a
general lower bound. Parts I and II are finite-algebra instances of P40.
Part III is conditional on receiving the genuine CRT-glued local Frobenius
and on a local splitting mismatch. Parts IV and V identify hidden
characteristic-scale conditions; they do not construct them.

The audit also found a strict strengthening of Part V. For every composite
integer, including a prime power, the first selective binomial coefficient
is indexed by the least prime factor. This strengthening is not needed for
the frozen claim and does not weaken the pass.

## 1. Arbitrary commutative algebras and the radical

For a finite-dimensional commutative unital algebra $A/\mathbb F_r$, the
Artinian quotient has the stated form

\[
A/J\simeq\prod_i\mathbb F_{r^{e_i}}.
\]

The quotient map has equal fibres. Also, $a\in A$ is a unit exactly when its
image is a unit in $A/J$. Hence

\[
\Pr(a\notin A^\times)
=1-\prod_i(1-r^{-e_i})
\leq\sum_i r^{-e_i}\leq d/r.
\]

This remains true for a nonreduced algebra with a large nilpotent radical.
The sentence “nilpotents do not increase the probability” must be read
relative to a fixed semisimple quotient: adjoining a nilpotent radical
leaves the probability unchanged. It is not a comparison between all
algebras of the same total dimension. For example,

\[
\alpha_r(\mathbb F_r[\epsilon]/(\epsilon^2))=1/r,
\qquad
\alpha_r(\mathbb F_{r^2})=1/r^2.
\]

The theorem and proof use only the correct quotient-relative meaning.

For a finite free algebra over $\mathbb Z/N\mathbb Z$, CRT makes the two
local algebra elements independent and uniform. Multiplication by an
element is invertible exactly when the element is a unit. Therefore the
determinant is zero in exactly one residue field with probability

\[
\alpha_p(1-\alpha_q)+(1-\alpha_p)\alpha_q.
\]

This is the claimed formula. Conditional freshness after an adaptive
transcript is enough. Apply the same conditional bound at each step and
then use the union bound.

## 2. Monogenic etale algebras and Krylov ranks

Write

\[
A\simeq\prod_e(\mathbb F_{r^e})^{m_e},
\qquad \sum_e em_e=d<r.
\]

For $e=1$, there are $r$ distinct linear polynomials and $m_1<r$. For
$e\geq2$, the proof's subfield union bound gives at least $r$ elements of
exact degree $e$. Thus the number $I_r(e)$ of degree-$e$ irreducibles is at
least $r/e$. Since

\[
m_e\leq d/e<r/e,
\]

one can choose distinct component minimal polynomials. Their product has
degree $d$, so the resulting element generates $A$. The monogenic claim is
valid, including repeated field degrees.

The discriminant

\[
\Delta(a)=\prod_{i<j}(\sigma_i(a)-\sigma_j(a))^2
\]

is a nonzero polynomial of total degree $d(d-1)$. A generator makes it
nonzero. If the Krylov matrix is not full rank, the minimal polynomial of
$a$ has degree below $d$, so $\Delta(a)=0$. Schwartz--Zippel gives the
claimed bound. When $d(d-1)\geq r$, the displayed minimum correctly makes
the bound trivial. In the quasipolynomial-rank and
exponential-characteristic regime, it is nontrivial for all sufficiently
large inputs.

If the two local ranks differ, some minor is zero in exactly one component.
Thus the mismatch is factor-extractable from a public Krylov matrix. A
direct scan of all square minors uses at most
$4^d\operatorname{poly}(d,n)$ bit operations. This is quasipolynomial when
$d=(\log n)^{O(1)}$. The frozen statement only bounds the probability of
the mismatch, so it does not need this extra extraction lemma. It correctly
excludes separators based on particular intermediate entries or minors when
the final ranks agree.

Different local factor-degree partitions do not change the probability
argument. Both local Krylov matrices normally have full rank. A rank
mismatch requires at least one local discriminant zero.

## 3. Genuine Frobenius and extraction

On one factor $\mathbb F_{r^e}$, a normal basis makes absolute Frobenius an
$e$-cycle. Its characteristic polynomial is $T^e-1$. Products of field
factors give

\[
\chi_{F_r}(T)=\prod_{e\in\lambda_r}(T^e-1).
\]

The cyclotomic exponents recover the numbers of parts divisible by each
integer. Downward subtraction then recovers every part multiplicity. Thus
$\lambda\mapsto H_\lambda$ is injective over $\mathbb Z[T]$.

Each coefficient of $H_\lambda$ has absolute value at most $2^d$. A
nonzero difference of two such coefficients has absolute value at most
$2^{d+1}$. Under $p,q>2^{d+1}$, it cannot disappear modulo either local
prime. When the candidate partition equals $\lambda_p$, every coefficient
difference is zero modulo $p$, and at least one is nonzero modulo $q$. Its
gcd with $N$ is $p$.

There are $\exp(O(\sqrt d))$ integer partitions. Their enumeration and a
division-free characteristic polynomial are quasipolynomial for
$d=(\log n)^{O(1)}$. All ring coefficients use $O(n)$ bits.

Known factors construct the map by local modular powers and CRT. The reverse
direction is deliberately narrower. A supplied genuine map factors the
input only on the explicit partition-mismatch promise. F145 does not show
how to generate such a promise for every $N$. It does not claim an
all-input factoring equivalence. This scope agrees with P05--P09 and P17.

## 4. Monomial functions and cross-orders

For $Q=r^e$, the nonzero group is cyclic of order $Q-1$. Therefore

\[
\#\{x:x^E=x\}=1+\gcd(E-1,Q-1).
\]

This includes $x=0$. It also includes $E=1$, with
$\gcd(0,Q-1)=Q-1$.

Every function on $\mathbb F_Q$ has one polynomial representative of degree
below $Q$. Every additive function has one linearized representative

\[
\sum_{j=0}^{e-1}c_jX^{r^j}.
\]

Reduce the positive exponent $E$ to the representative in
$\{1,\ldots,Q-1\}$. This preserves the value at zero and at all nonzero
points. A single monomial can equal a linearized polynomial only at one
exponent $r^j$. This proves the additivity classification.

The edge cases are correct. For $e=1$, additivity is exactly
$E\equiv1\pmod{r-1}$. For $Q=2$, every positive monomial is the identity
because the exponent modulus is one.

The reductions for $E=N^k$ are exact. Modulo $p-1$, one has $p\equiv1$,
so $N^k\equiv q^k$. If $q$ is invertible modulo $p-1$, the condition is
the displayed multiplicative-order condition. If it is not invertible and
$k\geq1$, then $q^k\equiv1\pmod{p-1}$ is impossible. A common prime would
divide $q^k$ but not $q^k-1$. Thus the nonunit case is an obstruction, not
an omitted order branch. In the usual ordering $p<q$, $q$ is automatically
a unit modulo $p-1$.

For extension degree $e$, the identity condition is always

\[
N^k\equiv1\pmod{p^e-1}.
\]

When $e\mid k$, it reduces exactly to
$q^k\equiv1\pmod{p^e-1}$, as claimed. Without $e\mid k$, the frozen
statement makes no such reduction. Its general Frobenius congruence is the
correct condition.

## 5. Binomial jets, including repeated factors

The frozen semiprime proof is correct. In fact, let $N$ be any composite
integer and let $P$ be its least prime divisor. For $1\leq k<P$, one has
$\gcd(k,N)=1$, and

\[
k\binom Nk=N\binom{N-1}{k-1}
\]

implies $N\mid\binom Nk$.

At $k=P$,

\[
\binom NP=\frac NP\binom{N-1}{P-1}.
\]

Lucas's theorem gives

\[
\binom{N-1}{P-1}\equiv1\pmod P,
\]

because the least base-$P$ digit of $N-1$ is $P-1$. Thus this second
factor is not divisible by $P$. The first factor contains every prime-power
divisor of $N$ to its full multiplicity except that it contains one fewer
copy of $P$. Therefore

\[
\boxed{\gcd\!\left(\binom NP,N\right)=N/P.}
\]

For $N=pq$ with $p<q$, this is exactly the frozen value $q$. It also covers
$N=P^a$, even inputs, repeated factors, and composites with more than two
prime factors. The frozen restriction is conservative, not erroneous.

A quasipolynomial numerical cutoff remains below $P$ only on families with
$P=2^{\Omega(n)}$. If $P$ is small, direct trial division through the same
cutoff is already useful. The result does not cover sparse large
binary-encoded indices or compressed interval evaluation, exactly as the
statement says.

## 6. Quasipolynomial scale and prior routes

If $M,d=2^{(\log n)^{O(1)}}$, then $Md^2$ is still
$2^{(\log n)^{O(1)}}=2^{o(n)}$. On balanced semiprimes,

\[
Md^2(1/p+1/q)=2^{-\Omega(n)}.
\]

Thus the union bounds in Parts I and II survive the relaxed runtime target.

The novelty and scope claims are accurate:

- Part I is P40 applied to the determinant polynomial, with an exact sharper
  unit count from the semisimple quotient.
- Part II is P40 applied to the discriminant obstruction for a final Krylov
  rank, plus the monogenic lemma. It does not control all matrix minors or
  intermediate elimination data when both final ranks agree.
- Part III formalizes why the true local Frobenius would carry the desired
  component label. P06, P09, and F04 show why replacing the hidden local
  characteristic by $N$ can synchronize or erase that label.
- Part IV gives the exact congruence faced by the simplest succinct monomial
  replacement. It is not a lower bound against adaptive exponent menus.
- Part V closes only low **numerical** Hasse order. It does not close a
  succinct characteristic-scale coefficient source.

F145 gives a correct common boundary and a useful stronger jet lemma. Its
mathematical content is mostly a synthesis and sharpening of standard
finite-algebra facts and existing project boundaries. It does not open a
new factoring route by itself.

## Residual risk

This is an internal proof audit, not a publication-level literature review.
A context-free proof-blind reconstruction is still required before
promotion under the project protocol.
