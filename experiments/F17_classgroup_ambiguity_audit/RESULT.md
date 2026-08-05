# F17 hostile audit — imaginary-quadratic ambiguity

**Audit verdict:** the exact-uniform obstruction and the ambiguous-form
classification survive, but the submitted report does **not** survive
unchanged. Five corrections are mandatory:

1. In the even-discriminant branch, the public factorization
   $\Delta=(-4)N$ already gives the factor-free genus character
   $\chi_{-4}=\chi_N$. The assertion that every individual standard genus
   character requires a hidden prime-discriminant divisor is false.
2. An inverse-orbit collision can leave $X^2$, which can be useful
   2-torsion. The collision is still redundant, but its correct probability
   is governed by $G[4]$, not exactly by the direct-hit formula.
3. “Near-uniform” is undefined and is not closed by the exact-iid proof.
4. The congruence $b^2\equiv\Delta\pmod{4\ell}$ has four residue classes
   modulo $4\ell$, not two. They form two classes modulo $2\ell$, and those
   two signs give inverse form classes.
5. The calculations do not prove that order/exponent information is
   *necessary* for every powering strategy. They analyze only the displayed
   powers and identify the data those powers require.

With those repairs, the corrected theorem below is accepted by this hostile
audit. It remains only a special-semiprime method obstruction, not an
integer-factoring algorithm.

## 1. Setup and form/class distinction

Let $N=pq$, where $p<q$ are distinct odd primes. Since $-N$ is
squarefree, the field discriminant of $\mathbb Q(\sqrt{-N})$ is

\[
\Delta=
\begin{cases}
-N,&N\equiv3\pmod4,\\
-4N,&N\equiv1\pmod4.
\end{cases}
\]

Both cases have $\Delta<-4$. A primitive positive form $[a,b,c]$ of
discriminant $\Delta$ is taken in the canonical reduced domain

\[
|b|\le a\le c,
\qquad
b\ge0\quad\text{when }|b|=a\text{ or }a=c.
\]

For this convention each proper class has one canonical reduced
representative. Inversion sends the class of $[a,b,c]$ to the class of
$[a,-b,c]$. Comparing canonical representatives proves that the **class**
is fixed by inversion exactly when its reduced representative satisfies

\[
b=0,\qquad b=a,\qquad\text{or}\qquad a=c. \tag{A1}
\]

The boundary sign convention is essential: forms with $b=-a$, or with
$a=c$ and $b<0$, reduce to the displayed positive-$b$ representative.
Thus “ambiguous form” below means the canonical representative of a class in
$G[2]$, where $G=\operatorname{Cl}(\Delta)$; it is not an equality of two
arbitrary form triples.

Reduction, inversion, equality, and one composition are polynomial-time in
$\log|\Delta|$ for reduced-form inputs. Reduced coefficients and the
standard composition/reduction intermediates have polynomially bounded bit
length, and the algorithms use integer arithmetic and extended gcd, not the
factorization of $N$.

## 2. Exhaustive ambiguous-form classification

### 2.1 Odd discriminant

When $N\equiv3\pmod4$, the two canonical ambiguous forms are

\[
P=[1,1,(N+1)/4]
\]

and

\[
A=
\begin{cases}
[p,p,(p+q)/4],&q>3p,\\
[(p+q)/4,(q-p)/2,(p+q)/4],&q<3p.
\end{cases} \tag{A2}
\]

Parity excludes $b=0$. If $b=a$, then $N=a(4c-a)$, and $a\le c$ is
equivalent to $4c-a\ge3a$. The ordered factor pairs of the squarefree
semiprime are therefore $(1,N)$ and, when $q>3p$, $(p,q)$. If $a=c$, then

\[
N=(2a-b)(2a+b),
\]

and reducedness permits $(p,q)$ exactly when $q<3p$; the pair $(1,N)$ is not
reduced. Equality $q=3p$ is impossible because $p,q$ are distinct primes.
Primitivity in the $b=a$ nonprincipal case follows from
$p\nmid(p+q)/4$; in the $a=c$ case a common divisor of $a,b$ would divide
both $2a-b=p$ and $2a+b=q$.

The nonprincipal form exposes $p,q$ by these product identities. The
principal form gives only $1\cdot N$. Hence a uniform ambiguous-class hit
succeeds on exactly one of the two classes.

### 2.2 Even discriminant

When $N\equiv1\pmod4$, the four canonical ambiguous forms are

\[
\begin{aligned}
P&=[1,0,N],\\
E&=[2,2,(N+1)/2],\\
F_0&=[p,0,q],\\
F_1&=
\begin{cases}
[2p,2p,(p+q)/2],&q>3p,\\
[(p+q)/2,q-p,(p+q)/2],&q<3p.
\end{cases}
\end{aligned} \tag{A3}
\]

For $b=0$, $N=ac$, yielding $P,F_0$. For $b=a=2u$,
$N=u(2c-u)$, yielding $E$ and the first $F_1$ branch. For $a=c$,

\[
N=(a-b/2)(a+b/2),
\]

yielding the second $F_1$ branch; the pair $(1,N)$ violates reducedness.
The same $q<3p$ versus $q>3p$ inequalities follow directly from
$|b|\le a\le c$.

The primitivity checks omitted from the candidate’s terse exhaustiveness
paragraph are harmless but necessary. The coefficients $(N+1)/2$ and
$(p+q)/2$ in the $b=a$ forms are odd; neither is divisible by the relevant
odd leading prime. In the $a=c$ branch, a common divisor divides $2p,2q$
and also the odd coefficient $a$, hence is one.

The extraction identities are

\[
\begin{array}{c|c}
b=0 & N=ac,\\
b=a & N=(a/2)((4c-a)/2),\\
a=c & N=(a-b/2)(a+b/2).
\end{array}
\]

They give $p,q$ for $F_0,F_1$, but only $1,N$ for $P,E$. In particular

\[
N=21,\qquad \Delta=-84,\qquad E=[2,2,11]
\]

is primitive, canonical reduced, nonprincipal, and ambiguous, while its
displayed extraction is $1\cdot21$. Since $E$ is a deterministic function
of $N$, and $\gcd(2,21)=\gcd(11,21)=1$, supplying its displayed coefficients
gives no immediate coefficient gcd and no side information beyond $N$.
This is a counterexample to universal extraction from a nonprincipal
ambiguous form, not a hardness result for arbitrary algorithms.

After a useful form yields $d\in\{p,q\}$, put $d'=N/d$, compute
$u=d^{-1}\bmod d'$, and set $e=du\bmod N$. Coprimality gives
$e\equiv0\pmod d$ and $e\equiv1\pmod{d'}$. Extended Euclid and the
surrounding arithmetic have polynomial bit complexity. This CRT-idempotent
step is correct within the squarefree-semiprime scope.

### 2.3 Torsion identities

Criterion (A1) and the exhaustive lists prove directly, without genus theory,
that

\[
t:=|G[2]|=
\begin{cases}
2,&\Delta=-N,\\
4,&\Delta=-4N.
\end{cases}
\]

Every element of $T=G[2]$ has order at most two. In the even case $E\ne P$
because the canonical reduced representatives differ, so
$T_0=\{P,E\}$ is a subgroup. In the odd case set $T_0=\{P\}$. The useful
classes are exactly $T\setminus T_0$, the other coset of this index-two
subgroup. No unproved form-composition identity is hidden here: the claim
follows from the complete list and the elementary subgroup fact.

The usual prime-discriminant count agrees: $-N$ has two prime-discriminant
factors and $-4N$ has three, so genus theory gives $2$ and $4$ elements of
$G[2]$, respectively.

## 3. Exact iid-uniform probabilities

Grant an oracle returning independent, exactly uniform reduced
representatives of $G$. Put $h=|G|$, $T=G[2]$, $t=|T|$,
$U=T\setminus T_0$, and $H=h/t$.

### 3.1 Direct fixed points

A sample is ambiguous with probability $t/h$ and useful with probability

\[
\Pr(X\in U)=\frac{t}{2h}.
\]

Thus $m$ iid trials succeed with exact probability

\[
1-\left(1-\frac{t}{2h}\right)^m,
\]

and their expected stopping count is exactly $2h/t$. Conditional on an
arbitrary ambiguous hit, success is $1/2$. Conditional on a nonprincipal
ambiguous hit, it is $1$ for $t=2$ and $2/3$ for $t=4$.

### 3.2 Ordinary inverse-orbit collisions: corrected statement

If two samples have the same unordered inverse orbit, then $Y=X$ or
$Y=X^{-1}$. Products and quotients supply the identity and $X^2$ (up to
inversion). The identity is useless. Contrary to the candidate’s shorthand,
$X^2$ **can** be useful when $X$ has order four.

This does not give birthday amplification because $X^2$ was already
computable from the single sample $X$. The exact one-sample probability is

\[
\Pr(X^2\in U)=\frac{t\,|U\cap G^2|}{h}
\le \frac{t^2}{2h}, \tag{A4}
\]

since every element in the image of squaring has exactly $t$ square roots.
For this family $t\le4$, so (A4) differs from the direct rate by at most a
constant. Any stronger claim about inverse-orbit collisions must state what
additional output is used and account for $G[4]$.

### 3.3 Square collisions

For independent $X_i,X_j$, the quotient is uniform in $G$. Hence

\[
X_i^2=X_j^2,\quad X_iX_j^{-1}\in U
\]

has exact probability $t/(2h)=1/(2H)$ for a specified pair.

Each square fiber is a coset of $T$. Its $t$ elements split into the two
equal $T_0$-cosets, and a useful quotient occurs exactly when both halves of
one fiber have been sampled. After discarding the irrelevant $t/2$-fold
multiplicity within each half, every sample is uniform on $2H$ coarse states.
Failure with exactly $k$ occupied fibers has count

\[
\binom Hk 2^k k!S(m,k).
\]

Therefore the exact success probability is

\[
1-\frac1{(2H)^m}
\sum_{k=0}^{\min(m,H)}\binom Hk2^k k!S(m,k). \tag{A5}
\]

If $\tau$ is the first successful sample count while every preceding pair is
tested, the candidate’s expected-value expression is also exact:

\[
\mathbb E[\tau]=\sum_{m\ge0}\Pr(\tau>m),
\]

where $\Pr(\tau>m)$ is the complementary term in (A5). This is the standard
tail-sum identity for a nonnegative integer-valued stopping time.

The union bound gives

\[
\Pr(\text{success by }m)\le \binom m2\frac1{2H}.
\]

This proves an $\Omega(\sqrt H)$ expected stopping count. For the matching
upper bound, expose the coarse state as an independent uniform fiber and fair
bit. In $4\lfloor\sqrt H\rfloor$ samples, both bit values occur at least
$\lfloor\sqrt H\rfloor$ times with constant probability. The first set has
$\Omega(\sqrt H)$ distinct fibers with constant probability because its
expected number of internal collision pairs is $O(1)$; the other set then
hits one of those fibers with constant probability. Independent blocks give
$O(\sqrt H)$ expectation. Thus the birthday scale is genuinely

\[
\Theta(\sqrt H)=\Theta(\sqrt{h/t}).
\]

Comparing inverse orbits of the squares adds the event
$X_i^2=X_j^{-2}$. A union bound over the corresponding useful product and
quotient events changes only a constant factor. Exact intersections can
depend on $G[4]$, as the candidate says.

The bit cost of the literal all-pairs test is
$O(m^2\operatorname{poly}(\log|\Delta|))$, with
$O(m\log|\Delta|)$ stored bits up to polynomial factors. This does not alter
the sample obstruction.

For a random walk, an exactly uniform stationary start makes every marginal
uniform, so the one-time rate and the union-bound obstruction remain valid
without independence. The exact retry and Stirling formulas require the
stronger iid law stated above. Canonical reduction supplies only normal
forms; it supplies neither a generating set, a mixing theorem, nor exact
sampling. The candidate’s stated random-walk limitations are therefore
correct.

## 4. Unconditional asymptotic obstruction

The exact theorem needed is Siegel’s lower bound for primitive real Dirichlet
characters: for every fixed $\varepsilon>0$, there exists an ineffective
$c_\varepsilon>0$ such that

\[
L(1,\chi_D)\ge c_\varepsilon |D|^{-\varepsilon}
\]

for every negative fundamental discriminant $D$. For $D<-4$, the analytic
class-number formula gives

\[
h(D)=\frac{\sqrt{|D|}}{\pi}L(1,\chi_D),
\]

so $h(D)\ge c'_\varepsilon|D|^{1/2-\varepsilon}$. The constant and threshold
are ineffective; the asymptotic quantifiers are nevertheless unconditional.

Take $\varepsilon=1/4$. Since $|\Delta|\in\{N,4N\}$, $t\le4$, and
$N\ge2^{n-1}$, every fixed polynomial $m(n)$ satisfies

\[
m\frac{t}{2h}=2^{-\Omega(n)},
\qquad
\binom m2\frac{t}{2h}=2^{-\Omega(n)}. \tag{A6}
\]

Thus polynomially many exact iid-uniform direct samples or square-collision
pairs have exponentially small success, on all sufficiently large semiprimes
in the family, not merely on a selected subsequence.

The claimed infinite balanced subfamilies also exist. For any prescribed
nonzero residue classes $r,s\pmod4$, the prime number theorem in arithmetic
progressions supplies, for all sufficiently large $x$, a prime
$p\equiv r\pmod4$ in $(x,1.1x)$ and a prime $q\equiv s\pmod4$ in
$(1.5x,1.6x)$. Then $p<q<2p$. Choosing equal or opposite residues selects
the desired discriminant branch.

This proof is exact-iid only. It extends to an explicitly quantified
distribution only after bounding its point masses or total-variation error.
An inverse-polynomial perturbation could deliberately put inverse-polynomial
mass on $U$, so the candidate’s unqualified word “near-uniform” must be
deleted.

## 5. Genus information: one false claim and the corrected boundary

The statement that standard individual genus characters always require a
hidden prime-discriminant divisor is false. In the even branch,

\[
\Delta=(-4)N
\]

is already a public factorization into discriminants. Consequently
$\chi_{-4}=\chi_N$ is a nontrivial factor-free genus character. It is also
explicitly evaluable without finding $p,q$: here $b$ is even, and primitivity
ensures that at least one of $a,c$ is odd, so one may evaluate $(-4/a)$ when
$a$ is odd and $(-4/c)$ otherwise. At the candidate’s own smallest example
$\Delta=-84$, use primitively represented coefficients coprime to $\Delta$:

\[
\begin{array}{c|c|c}
\text{class}&r&(-4/r)\\ \hline
P=[1,0,21]&1&+1\\
E=[2,2,11]&11&-1\\
F_0=[3,0,7]&31=F_0(1,2)&-1\\
F_1=[5,4,5]&5&+1.
\end{array}
\]

So this public character crosses both the decoy and useful pairs; it is not
the hidden factor orientation on $N=21$. In other residue cases it can align
differently with the torsion classes, but it still supplies only one public
bit.

The exponential boundary survives. There are exactly
$|G/G^2|=|G[2]|=t$ genera, each of size $h/t$. Even if the complete genus
vector were supplied for free and an algorithm could sample a chosen genus at
unit cost, that genus contains at most $|U|=t/2$ useful torsion classes. Its
conditional useful mass is therefore at most

\[
\frac{t/2}{h/t}=\frac{t^2}{2h},
\]

only a factor $t\le4$ above the direct uniform mass. The public
$\chi_{-4}$ gives at most the corresponding factor-two conditioning.
Characters attached to the individual $p$- and $q$-prime discriminants do
require the hidden factorization.

The aggregate identity in the candidate remains correct after clarifying its
hypothesis. If $r$, coprime to $\Delta$, is primitively represented by a
class, an equivalent form has leading coefficient $r$, and
$\Delta\equiv b^2\pmod{4r}$. Hence the Kronecker/Jacobi aggregate satisfies

\[
(\Delta/r)=1.
\]

This is only the product relation among prime-discriminant character labels.
It neither removes the public $-4$ character nor rules out a different
factor-free genus construction.

## 6. Powering statements

Write the group exponent as

\[
\lambda(G)=2^a m,\qquad m\text{ odd}.
\]

Because $t\ge2$, $a\ge1$. The map
$\phi(X)=X^{\lambda(G)/2}$ has image $W\le T$, and a uniform input maps
uniformly to $W$. Its exact useful probability is

\[
\frac{|W\cap U|}{|W|}. \tag{A7}
\]

If $t=2$, the Sylow-2 subgroup has rank one and is cyclic; $\phi$ maps it
onto $T$, so (A7) is $1/2$. If $t=4$, its invariant factors are

\[
C_{2^a}\times C_{2^b},\qquad a\ge b\ge1.
\]

When $a=b$, $W=T$ and the probability is $1/2$. When $a>b$, $W$ has order
two. Its nonidentity element can be $E,F_0$, or $F_1$; the probability is
respectively $0,1/2,1/2$. This checks exponent rather than group order and
contains no order/exponent confusion.

For the different power $h/2$, decompose $G$ into its Sylow-2 and odd parts.
If $t=2$, the Sylow-2 part is $C_{2^a}$, and $X^{h/2}$ is uniform on $T$.
If $t=4$, the Sylow-2 order is $2^{a+b}$; hence $h/2$ is divisible by
$2^a$ because $b\ge1$, while its odd factor kills the odd part. Therefore

\[
X^{h/2}=1
\]

for every $X$. These statements are correct.

Given $\lambda(G)$ or $h$ in binary, their bit lengths are
$O(\log|\Delta|)$: reducedness gives
$a\le\sqrt{|\Delta|/3}$ and the crude count of possible pairs $(a,b)$ is
$O(|\Delta|)$, so $h=O(|\Delta|)$ and $\lambda(G)\le h$. Binary powering
therefore uses polynomially many form compositions. What is unproved is a
factor-free polynomial-time method to obtain the required order/exponent
data. The audit accepts that missing-data statement, but not the stronger
suggestion that every possible successful powering rule must receive exactly
this information.

## 7. Auxiliary split primes and bit complexity

For an odd prime $\ell\nmid\Delta$ with $(\Delta/\ell)=1$, choose $b$
satisfying

\[
b^2\equiv\Delta\pmod{4\ell}
\]

and form

\[
[\ell,b,(b^2-\Delta)/(4\ell)].
\]

The form is integral, positive, and primitive: if $\ell$ divided both $b$
and the third coefficient, it would divide $\Delta$. Reduction gives a class
without factoring $N$. A modular square root modulo the supplied prime
$\ell$ is available by a standard Las Vegas polynomial-time finite-field
algorithm; parity supplies the modulus-four condition.

There are four literal roots modulo $4\ell$. The pairs differing by $2\ell$
yield properly equivalent forms, so there are two roots modulo $2\ell$, and
the two signs give inverse prime-ideal classes. This is the precise version
of the candidate’s “two roots” sentence.

All coefficients have $O(\log|\Delta|+\log\ell)$ bits, and construction and
reduction have polynomial bit complexity in that quantity. This does not
supply a polynomial-time distribution on $\ell$, prove mixing, or give exact
uniform class samples. Those remain the live gap, along with deliberately
nonuniform sampling and other class-group mechanisms.

## 8. Computational audit and final scope

The timeout-bounded Sage run F17_A02 independently enumerated all reduced
forms for 630 semiprimes with $p,q<160$, matched every ambiguous-form list and
extraction, brute-counted (A5) in 21 small cases, and checked the displayed
power images in nine abelian groups. It passed. These finite checks support
only the exact small cases; the proofs above carry the unbounded claims. The
failed cache and JSON runs and the noncompliant environment diagnostic are
fully disclosed in RUN_MANIFEST.md.

The corrected result closes:

- direct exact-iid uniform ambiguity hunting;
- the complete exact-iid square-collision scheme;
- ordinary inverse-orbit collisions using only the resulting group relations;
- the displayed $\lambda(G)/2$ and $h/2$ power rules absent their required
  order/exponent data;
- genus postselection of an exact uniform distribution, up to the proved
  constant factor.

It does **not** close quantitatively unspecified near-uniform distributions,
designed nonuniform samplers, other exponents, factor-revealing failures in
composition, real-quadratic infrastructure, or arbitrary class-group methods.
It supplies no classical polynomial-time factoring algorithm.
