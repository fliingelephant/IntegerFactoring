# Blind reconstruction of F189

## Isolation and verdict

I read only **PROMPT.md** and **STATEMENT.md**. The SHA-256 digest of the
frozen statement was

\[
\mathtt{2e7c4df447013db2e5ebc5d51045eec0abff3a36f1bf59760d74ae31f4adbfc1}.
\]

I did not read another F189 file or a durable ledger. I used no mathematical
computation.

**Verdict: PASS under the standard sampling convention.** All mathematical
claims reconstruct. In the affine-source section, “sampled residues” must
mean that $U$ and $V$ are independent uniform residues before the unit
conditioning. This is the distribution under which the asserted uniformity
of $a=UV^{-1}$ and all displayed probabilities hold. Without a distribution
on $U,V$, a probability statement would be undefined. This is an implicit
convention, not a mathematical defect in the stated source.

The result is only a conditional splitter on a balanced-semiprime promise
and a collection of exact named-model boundaries. It supplies neither the
segment-zero oracle nor an all-input factoring algorithm.

## 1. Jacobi zeros and the floor identity

For odd $N$, the Jacobi symbol takes values in $\{-1,0,1\}$ and is zero
exactly when its numerator is not coprime to $N$. Therefore

\[
1-\chi_N(x)^2
=\mathbf 1_{\gcd(x,N)>1}.
\]

A finite product of Jacobi symbols is zero exactly when at least one factor
is zero. This proves (2) and (3).

Now let $x,N$ be positive and odd. Set

\[
h=\frac{N-1}{2},
\qquad
k=\frac{x-1}{2}.
\]

Consider the $hk$ lattice pairs

\[
(i,j),\qquad 1\le i\le h,\quad 1\le j\le k.
\]

The sum $F(x,N)$ counts pairs satisfying $jN\le ix$. Indeed,
$ix/N<x/2=k+1/2$, so every integer counted by the floor lies in the
displayed rectangle. Similarly, $F(N,x)$ counts pairs satisfying
$ix\le jN$.

Every strict pair is counted exactly once in the two sums. An equality pair
is counted twice. Write

\[
d=\gcd(x,N),\qquad x=dx_0,\qquad N=dN_0,
\qquad \gcd(x_0,N_0)=1.
\]

The equality $ix=jN$ has precisely the solutions

\[
i=N_0\ell,\qquad j=x_0\ell.
\]

The two half-range constraints are both equivalent to

\[
1\le\ell\le\frac{d-1}{2}.
\]

There are therefore $(d-1)/2$ equality pairs. Hence

\[
F(x,N)+F(N,x)
=hk+\frac{d-1}{2}
=\frac{(x-1)(N-1)}4+\frac{\gcd(x,N)-1}{2},
\]

which proves (5). Both summands on the right are integers because all three
of $x,N,d$ are odd.

For $\gcd(x,N)=1$, the usual Eisenstein form of Gauss's lemma for the Jacobi
symbol is

\[
\left(\frac{x}{N}\right)
=(-1)^{\sum_{i=1}^{(N-1)/2}\lfloor ix/N\rfloor}
=(-1)^{F(x,N)}.
\]

This proves (6). If the gcd is nontrivial, the Jacobi symbol is zero, while
the displayed power of minus one is necessarily a sign. The additional
lattice points in (5) measure the failure by exactly
$(\gcd(x,N)-1)/2$.

Multiplying (5) by two and rearranging gives, for each positive odd $x$,

\[
\gcd(x,N)-1
=2(F(x,N)+F(N,x))-\frac{N-1}{2}(x-1).
\]

Summing this identity over a finite multiset proves (8). Every summand in
$G_N(\mathcal A)$ is nonnegative. Thus its sum is zero exactly when every
member of $\mathcal A$ is a unit modulo $N$.

Because $N$ is odd,

\[
\gcd(2^ju,N)=\gcd(u,N).
\]

If $1\le a<N$ and $1\le L<N$, then every member of the segment is below
$2N$. Its 2-adic valuation has only $O(n)$ possible values. For fixed
$j$, the numbers with valuation exactly $j$ have the form

\[
2^j u
\]

where the odd quotients $u$ form one arithmetic subsegment with common
difference two. Replacing every segment member by its odd part preserves
its gcd with $N$. Applying (8) to the resulting multiset therefore gives
the claimed exact reduction. It does not give a fast way to evaluate the
floor-sum aggregate.

## 2. Conditional one-child isolation

Suppose an input interval has length $L<N$, has zero Jacobi product, and
contains no multiple of $N$. Split it into a left half and a right half and
query the oracle only on the left half.

- If the left product is zero, retain the left half.
- If the left product is nonzero, it has no zero entry. Since the product
  of the full interval is zero, the right half must contain a zero. Retain
  the right half.

Thus exactly one child is retained, and its zero-product invariant is
preserved. Repeated halving reaches a singleton after at most
$\lceil\log_2L\rceil$ queries.

The oracle's start bound remains valid. An initial interval with
$1\le a<2N$, length below $N$, and no multiple of $N$ cannot extend through
$2N$. Every retained subinterval therefore also starts below $2N$.

At the final singleton $x$, the Jacobi symbol is zero, so
$\gcd(x,N)>1$. The no-multiple premise implies $N\nmid x$, hence

\[
1<\gcd(x,N)<N.
\]

This is a verifiable proper factor.

Since $\log_2L<n$, the oracle work is at most $nQ(n)$. Interval
bookkeeping and the final gcd are polynomial in $n$. Multiplication by $n$
preserves the QP class. This proves the conditional one-child theorem.

An interval of length below $N$ contains at most one multiple of $N$.
Such a point is numerically public. It can be excluded from the premise or
the trial can be rejected. No hidden test is required.

## 3. The affine-source law

Assume $N=pq$ as in (13), and sample $U,V$ independently and uniformly
modulo $N$. Conditional on both being units, they are independent uniform
elements of the unit group. For every fixed unit $V$, multiplication by
$V^{-1}$ is a permutation of that group. Hence

\[
a=UV^{-1}\pmod N
\]

is uniform in $(\mathbb Z/N\mathbb Z)^\times$.

Since $V$ is a unit,

\[
U+tV\equiv V(a+t)\pmod N.
\]

Thus $U+tV$ and $a+t$ have exactly the same hidden prime divisors.

Put $S=\lfloor\sqrt N\rfloor$ and
$B=2^{\lfloor\log_2S\rfloor}$. Then $T=B/8$. Balance gives
$\sqrt N<\sqrt2\,p$ and, more importantly,

\[
\sqrt N>p,\qquad S\ge p.
\]

Since $B\le S<2B$,

\[
\frac p{16}\le\frac S{16}<T\le\frac S8<\frac{\sqrt N}{8}<p<q.
\tag{A1}
\]

The lower restriction $p\ge53$ ensures that $K$ and $T$ are positive
integers in the displayed definition.

Under CRT, the components $a_p,a_q$ of a uniform global unit are independent
and uniform in $\mathbb F_p^\times$ and $\mathbb F_q^\times$. The unique
local zero position is

\[
t_r\equiv-a_r\pmod r.
\]

Represented in $\{1,\ldots,r-1\}$, it is uniform there. Since $T<r$, the
pool positions $0,\ldots,T-1$ contain a local zero exactly when

\[
t_r\in\{1,\ldots,T-1\}.
\]

The two hit probabilities are therefore

\[
\alpha_p=\frac{T-1}{p-1},
\qquad
\alpha_q=\frac{T-1}{q-1},
\]

and the two events are independent. Inclusion-exclusion proves (17).

The interval contains a multiple of $N$ exactly when the two local root
positions are the same integer $t$ in $\{1,\ldots,T-1\}$. For each such
$t$, the pair of local roots has probability
$1/((p-1)(q-1))$. The cases are disjoint, so their total probability is

\[
\beta=\frac{T-1}{(p-1)(q-1)}.
\]

Because each prime has at most one root in an interval shorter than that
prime, this common-root case is the only zero event with no proper-factor
singleton. Subtracting it from the union probability proves (19).

It remains to verify the numerical lower bound. Write $h=T-1$. The useful
event contains the event that the $p$-root lies in the pool but the
$q$-root is not at the same position. Hence

\[
\rho_{\rm use}
\ge\alpha_p-\beta
=\frac{h}{p-1}\frac{q-2}{q-1}.
\tag{A2}
\]

From (A1),

\[
h=T-1>\frac{p-16}{16}.
\]

The function $(p-16)/(p-1)$ increases for $p>1$. Also, distinct odd primes
with $q>p\ge53$ satisfy $q\ge55$. Therefore

\[
\rho_{\rm use}
>
\frac{37}{16\cdot52}\frac{53}{54}
=\frac{1961}{44928}
>\frac1{40}.
\]

This proves the claimed constant.

On a useful zero trial, the public interval contains no multiple of $N$.
The conditional isolation theorem returns a proper gcd. On the common-root
trial, the multiple of $N$ is public and the trial is rejected. Unit
conditioning has constant probability on this balanced family; a nonunit
sample normally gives a factor directly, while a globally zero sample can
be rejected. Thus sampling and public rejections add only constant expected
overhead. The conditional source success probability above gives
expected fewer than a constant number of oracle trials. This proves the
promised QP splitter on (13), but not beyond that promise.

## 4. Exact Fourier and recurrence obstructions

Let $m=\operatorname{rad}(N)$. The value $z_N(x)$ depends only on whether
one of the distinct primes dividing $N$ divides $x$. It is therefore
periodic modulo $m$.

To prove minimality, suppose $h$ is a period and take a prime $r\mid m$.
If $r\nmid h$, CRT supplies an integer $x$ such that

\[
x\equiv-h\pmod r,
\qquad
x\equiv1\pmod s\quad(s\mid m,\ s\ne r).
\]

Then $x$ is a unit modulo $m$, so $z_N(x)=0$, while
$r\mid x+h$, so $z_N(x+h)=1$. This contradicts periodicity. Hence every
prime $r\mid m$ divides $h$, and $m\mid h$. The least period is exactly
$m$.

For the Fourier claim, let

\[
u(x)=\mathbf1_{\gcd(x,m)=1}=1-z_N(x).
\]

Under CRT, the Fourier transform of $u$ factors into local transforms. At a
prime $r\mid m$, summing a local additive character over
$\mathbb F_r^\times$ gives $r-1$ at zero frequency and $-1$ at every
nonzero frequency. Every local factor is nonzero. Thus
$\widehat u(a)\ne0$ for every frequency $a$.

At a nonzero global frequency, the constant function has zero Fourier
coefficient, so

\[
\widehat z_N(a)=-\widehat u(a)\ne0.
\]

At zero frequency,

\[
\widehat z_N(0)=m-\varphi(m)>0.
\]

Therefore all $m$ Fourier frequencies occur.

For any complex periodic sequence, the shift acts diagonally on its Fourier
modes. Its minimal nonzero constant-coefficient annihilator is the product
of $X-\lambda$ over the distinct supported shift eigenvalues $\lambda$.
Here every $m$-th root of unity is supported. The minimal recurrence
therefore has degree $m$ and characteristic polynomial

\[
X^m-1.
\]

This proves (20)--(21).

For $N=pq$, inclusion-exclusion gives

\[
z_N(x)
=\mathbf1_{p\mid x}+\mathbf1_{q\mid x}-\mathbf1_{N\mid x}.
\]

Thus the correction in (22) is exactly

\[
c_N(x)=\mathbf1_{p\mid x}+\mathbf1_{q\mid x}.
\]

Over one period modulo $N$, the Fourier support of
$\mathbf1_{p\mid x}$ consists of the $p$ frequencies corresponding to all
$p$-th roots of unity. The support of $\mathbf1_{q\mid x}$ consists of the
$q$ frequencies corresponding to all $q$-th roots. Their only common
frequency is zero, and their coefficients there add rather than cancel.
The union has exact size $p+q-1$.

The minimal annihilator is consequently

\[
\operatorname{lcm}(X^p-1,X^q-1).
\]

Since $p,q$ are distinct primes,

\[
\gcd(X^p-1,X^q-1)=X-1,
\]

which proves the formula and degree in (23).

On a balanced squarefree semiprime, $m=N=2^{\Theta(n)}$, while
$p+q-1=2^{\Theta(n)}$. Therefore a materialized period, all supported
Fourier modes, or either displayed dense recurrence has exponential size.
This is only an output-size obstruction in those exact representations.

## 5. Exact DFA size

The language in (24) depends only on the value modulo $m$. Tracking

\[
r\longmapsto 2r+b\pmod m
\]

after reading a bit $b$ gives a deterministic automaton with $m$ states.
Every residue is reachable by reading a binary representation of an integer
in $\{0,\ldots,m-1\}$.

To prove that no two residue states can merge, take distinct
$u,v\bmod m$. Choose a prime $r\mid m$ for which $u\not\equiv v\pmod r$.
Choose a suffix length $\ell$ with $2^\ell>m$. Since all primes dividing
$m$ are odd, multiplication by $2^\ell$ is invertible locally. By CRT,
choose $y\bmod m$ so that

\[
y\equiv-2^\ell u\pmod r
\]

and, for every other prime $s\mid m$, choose its residue so that

\[
y\not\equiv-2^\ell v\pmod s.
\]

At $r$, the first congruence also differs from
$-2^\ell v$ because $u\not\equiv v\pmod r$. Take the representative
$0\le y<m<2^\ell$ and write it as an $\ell$-bit suffix, padding with leading
zeros.

After this suffix, the state from $u$ is divisible by $r$ and is accepted.
The state from $v$ is nonzero modulo every prime dividing $m$ and is
rejected. Thus all $m$ reachable residue states are pairwise
Myhill--Nerode distinguishable. The minimal deterministic automaton has
exactly $m$ states.

This proves the finite-state lower bound in the stated deterministic binary
model. It is not a lower bound for an arithmetic algorithm with unbounded
integer registers or a nonlinear implicit state.

## 6. Factorials, binomials, and hidden-base carries

The rising-product identity is

\[
\prod_{t=0}^{L-1}(a+t)
=\frac{(a+L-1)!}{(a-1)!}
=L!\binom{a+L-1}{L}.
\]

If $L<r$, then $r\nmid L!$. Therefore

\[
r\mid R_{a,L}
\iff
r\mid\binom{a+L-1}{L},
\]

which proves (26).

Kummer's theorem says that the $r$-adic valuation of

\[
\binom{(a-1)+L}{L}
\]

equals the number of carries when adding $a-1$ and $L$ in base $r$.
Because $L<r$, its base-$r$ expansion has only its lowest digit nonzero.
If the lowest digit does not cause a carry, no higher digit can cause one.
If it does cause a carry, the binomial is divisible by $r$. Thus a carry
exists exactly when

\[
((a-1)\bmod r)+L\ge r,
\]

which proves (27). This is a reformulation in the unknown base $r$, not an
evaluation procedure.

## 7. Approximation threshold and exact remaining boundary

For $N=pq$ with $p<q<2p$, every positive summand in

\[
\sum_{t=0}^{L-1}(\gcd(a+t,N)-1)
\]

is at least $p-1$. Balance gives $p>\sqrt{N/2}$, so every positive total is
strictly larger than

\[
\sqrt{N/2}-1.
\]

Let

\[
\Delta=\frac{\sqrt{N/2}-1}{2}.
\]

If a certified approximation has additive error less than $\Delta$, then a
true zero produces an approximation of magnitude below $\Delta$, while a
positive total produces an approximation strictly above $\Delta$. The
public threshold $\Delta$ therefore distinguishes the cases.

No construction of this approximation, of the exact sum, or of the
segment-zero oracle appears in the statement. The recurrence, Fourier, and
DFA arguments constrain only their named explicit representations. They do
not constrain nonlinear arithmetic, integer-register, determinant,
implicit-state, randomized, or new gcd-based algorithms. Thus the final
boundary and every stated nonclaim are consistent with the proofs above.
