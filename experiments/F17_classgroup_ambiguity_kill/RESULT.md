# F17 — imaginary-quadratic ambiguity kill-first analysis

**Status:** self-audited symbolic result. No computation was used.

## Prior-route check

The closest prior route is F09/P15, because its cyclotomic-ideal discussion also
asks for a factor-free orientation whose different hidden local choices expose a
gcd.  The present route is materially different: its state space is the proper
class group of the imaginary quadratic field determined by $N$, its target is
the fixed-point set of class inversion, and its success is controlled by

\[
|\operatorname{Cl}(\Delta)[2]|/h(\Delta),
\]

not by the rank of scalar residue characters.  No class-group/ambiguous-form
route occurs in the current registry or closed-route files.

## Setup

Let $N=pq$, where $p<q$ are distinct odd primes.  The fundamental
discriminant of $K=\mathbb Q(\sqrt{-N})$ is computable from $N$ without its
factorization:

\[
\Delta=
\begin{cases}
-N,&N\equiv3\pmod4,\\
-4N,&N\equiv1\pmod4.
\end{cases}
\]

Write a primitive positive form as $f=[a,b,c]$, with
$b^2-4ac=\Delta$.  Use the canonical Gauss convention

\[
|b|\le a\le c,
\qquad b\ge0\text{ if }|b|=a\text{ or }a=c.
\]

Its inverse class is represented by $[a,-b,c]$.  The standard reduced-form
fixed-point lemma says that a canonical reduced form is ambiguous (its class has
order dividing two) exactly when

\[
b=0,\qquad b=a,\qquad\text{or}\qquad a=c. \tag{1}
\]

This follows by comparing the reduced representatives of $f$ and its inverse:
in the interior equality forces $b=0$, and the only identifications on the
boundary of the reduced domain are $b=a$ and $a=c$.  Canonical reduction,
inversion, equality testing, and composition all use polynomially many bit
operations on $O(\log |\Delta|)$-bit coefficients.  This makes ambiguity easy
to *recognize*; it does not make an ambiguous class easy to *sample*.

## Theorem 1 — exact ambiguous-form classification and extraction

### Odd fundamental discriminant: $N\equiv3\pmod4$

Here $p,q$ have opposite residues modulo four.  There are exactly two
ambiguous reduced forms.  The principal form is

\[
P=[1,1,(N+1)/4].
\]

The unique nonprincipal ambiguous form is

\[
A=\begin{cases}
[p,p,(p+q)/4],&q>3p,\\[2mm]
[(p+q)/4,(q-p)/2,(p+q)/4],&q<3p.
\end{cases} \tag{2}
\]

The equality $q=3p$ is impossible for distinct primes.  Both versions expose
the factorization without an oracle:

\[
\begin{array}{c|c}
b=a & N=a(4c-a),\\
a=c & N=(2a-b)(2a+b).
\end{array} \tag{3}
\]

If a noncanonical representative uses the opposite sign of $b$, the two
factors in the second line are merely swapped.

Thus every nonprincipal ambiguous class in the odd-discriminant case gives a
proper divisor.

### Even fundamental discriminant: $N\equiv1\pmod4$

Here $p,q$ have the same residue modulo four.  There are exactly four
ambiguous reduced forms:

\[
\begin{aligned}
P&=[1,0,N],\\
E&=[2,2,(N+1)/2],\\
F_0&=[p,0,q],\\
F_1&=\begin{cases}
[2p,2p,(p+q)/2],&q>3p,\\[2mm]
[(p+q)/2,q-p,(p+q)/2],&q<3p.
\end{cases}
\end{aligned} \tag{4}
\]

The two useful classes $F_0,F_1$ expose the factors by

\[
\begin{array}{c|c}
b=0 & N=ac,\\
b=a & N=(a/2)((4c-a)/2),\\
a=c & N=(a-b/2)(a+b/2).
\end{array} \tag{5}
\]

Again, changing the sign of $b$ only swaps the last pair.

The divisions by two are exact because $b$ and $a=b$ are even.  The class
$E$, however, yields only the trivial decomposition $N=1\cdot N$ in (5).
It is computable directly from $N$, so its mere appearance supplies no new
information.  It is nonprincipal because $E$ and $P$ are distinct canonical
reduced forms.

Consequently, the claim “every nontrivial ambiguous class factors $N$” is
false.  The smallest clean certificate in this branch is

\[
N=21,\quad \Delta=-84,\quad E=[2,2,11].
\]

The form is primitive, reduced, nonprincipal, and ambiguous, but (5) gives
$1\cdot21$, and each coefficient has gcd one with 21 except for the trivial
full-modulus combinations.  This is a counterexample only to the canonical
ambiguous-form extraction claim, not a hardness claim about arbitrary
algorithms given $N$ and $E$.

### Proof of exhaustiveness

For $\Delta=-N$, parity excludes $b=0$.  If $b=a$, then

\[
N=a(4c-a),
\]

and reducedness is $4c-a\ge3a$.  Since $N=pq$, the factor pair is either
$(1,N)$, which is $P$, or $(p,q)$, which is the first line of (2) and is
reduced exactly when $q>3p$.  If $a=c$, then

\[
N=(2a-b)(2a+b).
\]

The pair $(1,N)$ violates reducedness for semiprime $N$, while $(p,q)$
gives the second line of (2), reduced exactly when $q<3p$.

For $\Delta=-4N$, the case $b=0$ gives $N=ac$, hence $P$ and $F_0$.
In the case $b=a$, write $a=2u$; then

\[
N=u(2c-u).
\]

The factor pairs $(1,N)$ and $(p,q)$ give $E$ and the first version of
$F_1$, the latter reduced exactly when $q>3p$.  Finally, when $a=c$, put

\[
x=a-b/2,\qquad y=a+b/2.
\]

Then $xy=N$.  The pair $(1,N)$ is not reduced, while $(p,q)$ gives the
second version of $F_1$, reduced exactly when $q<3p$.  Because
$N\equiv1\pmod4$, $(N+1)/2$ and $(p+q)/2$ are odd; this proves
primitivity in the two $b=a$ cases and accounts for the full 2-adic issue.

Genus theory independently gives the same counts.  Factoring a fundamental
discriminant into prime discriminants gives two factors when $\Delta=-N$ and
three when $\Delta=-4N$.  Therefore

\[
t:=|\operatorname{Cl}(\Delta)[2]|=
\begin{cases}
2,&\Delta=-N,\\
4,&\Delta=-4N.
\end{cases} \tag{6}
\]

In either case exactly $t/2$ torsion classes expose $p,q$.  The nonfactor
torsion classes form a subgroup

\[
T_0=\begin{cases}
\{P\},&t=2,\\
\{P,E\},&t=4,
\end{cases}
\]

and the useful classes form its other coset in
$T=\operatorname{Cl}(\Delta)[2]$.

Once a proper divisor $d$ is extracted, put $d'=N/d$, compute
$u=d^{-1}\bmod d'$, and set $e=du\bmod N$.  Then $e=0\bmod d$,
$e=1\bmod d'$, so this gives the requested nontrivial CRT idempotent in
polynomial bit complexity.

## Theorem 2 — exact uniform-sampling and retry boundary

Let $G=\operatorname{Cl}(\Delta)$, $h=|G|=h(\Delta)$, and $t=|G[2]|$.
Assume for this section a granted oracle returning independent *exactly uniform*
classes of $G$.  This is an oracle assumption, not an implemented sampler.

### Direct inversion fixed points

Canonical reduction followed by $f=f^{-1}$ hits an ambiguous class with
probability $t/h$, and hits a factor-exposing class with exact probability

\[
\boxed{\frac{t}{2h}}. \tag{7}
\]

For $m$ independent samples the exact success probability is

\[
1-\left(1-\frac{t}{2h}\right)^m, \tag{8}
\]

and the exact expected number of samples until a factor is

\[
\boxed{\frac{2h}{t}}. \tag{9}
\]

Conditioned on a nonprincipal ambiguous hit, success is $1$ for $t=2$ and
$2/3$ for $t=4$.  Conditioned on an arbitrary ambiguous hit, it is $1/2$
in both cases.

### Pairwise inversion collisions do not create torsion

A collision of inverse orbits only says $X_j=X_i$ or $X_j=X_i^{-1}$.
The corresponding quotient or product is the identity; the other natural
combination is $X_i^2$, which need not have order two.  Only a fixed inverse
orbit, $X_i=X_i^{-1}$, is ambiguous, returning to (7).  Thus ordinary
birthday collisions modulo inversion do not amplify this mechanism.

### Pairwise square collisions

If $X_i^2=X_j^2$, then $X_iX_j^{-1}\in T$.  A specified independent pair
produces a useful torsion class with the same exact probability $t/(2h)$ as
(7), but all pairs can be tested, giving a birthday improvement.

Put

\[
H=h/t=|G/T|.
\]

Each fiber of the squaring map has $t$ elements and splits into the two equal
cosets of $T_0$.  A useful quotient occurs exactly when one square fiber has
been sampled in both cosets.  If $S(m,k)$ is a Stirling number of the second
kind, the exact success probability after $m$ iid samples is

\[
\boxed{
1-\frac{1}{(2H)^m}
\sum_{k=0}^{\min(m,H)}
\binom Hk 2^k k!S(m,k).} \tag{10}
\]

Indeed, on failure choose the $k$ occupied square fibers, choose one of two
allowed cosets in each fiber, and map the $m$ labeled samples surjectively
onto those fibers.  The exact expected stopping sample count is the sum over
$m\ge0$ of the complementary probability in (10).  Its birthday scale is

\[
\Theta(\sqrt H)=\Theta(\sqrt{h/t}), \tag{11}
\]

and, without any asymptotics, the union bound gives

\[
\Pr(\text{success by }m)
\le \binom m2\frac{t}{2h}. \tag{12}
\]

Colliding inverse-orbits of squares can change constants, but intersections then
depend on $G[4]$, not only $t,h$; it does not change the exponential boundary
proved below.

### Random walks and canonical reduction

Starting a walk in the exact uniform stationary distribution gives (7) for each
marginal.  If sufficiently separated states have a proved iid-uniform law, (10)
applies.  Canonical reduction only supplies normal forms; it proves neither a
generating set nor a mixing time.  A walk started at the identity, a designed
nonuniform walk, and correlated stopping rules are not covered by the uniform
calculation and are not ruled out here.

## Theorem 3 — unconditional exponential uniform-hit obstruction

For a negative fundamental discriminant $D<-4$, the analytic class-number
formula and Siegel's unconditional lower bound imply that for every fixed
$\varepsilon>0$

\[
h(D)\ge c_\varepsilon |D|^{1/2-\varepsilon}, \tag{13}
\]

with an ineffective positive constant $c_\varepsilon$.  Ineffectivity affects
explicit thresholds, not the asymptotic probability statement.  Taking
$\varepsilon=1/4$, using $|\Delta|\in\{N,4N\}$, and writing
$n=\lceil\log_2(N+1)\rceil$, (7) and (12) give, for every
$m=\operatorname{poly}(n)$,

\[
\Pr(\text{direct success})
\le \frac{mt}{2h}=2^{-\Omega(n)},
\]

\[
\Pr(\text{square-collision success})
\le \binom m2\frac{t}{2h}=2^{-\Omega(n)}. \tag{14}
\]

There are infinite balanced families $p<q<2p$ in either desired mod-four
pattern: choose primes in fixed proportional intervals and fixed nonzero
residue classes modulo four, using the prime number theorem in arithmetic
progressions.  Hence (14) is an unconditional obstruction on infinite balanced
semiprime families, not merely on an adversarial finite example.

Genus theory is decisive here because $t$ stays equal to two or four while
$h$ grows exponentially in the input bit length.  Even granting every genus
label can partition a uniform distribution into only $t$ genera, so genus
postselection changes this bound by at most a constant factor.

## Powering to 2-torsion and the hidden oracle

Powering has a different boundary and must not be conflated with uniform hits.
If the exact group exponent is

\[
\lambda(G)=2^a m\quad(m\text{ odd}),
\]

then

\[
\phi(X)=X^{\lambda(G)/2}\in T.
\]

For uniform $X$, $\phi(X)$ is uniform on the subgroup
$W=\operatorname{im}\phi$, so its exact factor probability is

\[
\boxed{\frac{|W\cap(T\setminus T_0)|}{|W|}.} \tag{15}
\]

For $t=2$, the Sylow-2 subgroup is cyclic and $W=T$, giving probability
$1/2$.  For $t=4$, write the Sylow-2 subgroup as
$C_{2^a}\times C_{2^b}$, $a\ge b\ge1$.  If $a=b$, then $W=T$ and the
probability is $1/2$.  If $a>b$, then $|W|=2$: the probability is $1/2$
when its nonidentity element is $F_0$ or $F_1$, and zero when it is the
known exceptional class $E$.  Thus powering success is not determined by
$t,h$ alone.

The naive class-number exponent behaves even more sharply.  If $t=2$, then
$X^{h/2}$ is uniform on $T$.  If $t=4$, then

\[
X^{h/2}=1\qquad\text{for every }X\in G, \tag{16}
\]

because $v_2(h/2)=a+b-1\ge a$, while the odd part of $h/2$ kills the odd
component.  Other powers, the odd part of $h$, and generic 2-group
decomposition can behave differently; they require additional invariant-factor
information and are not ruled out.

Neither exact $h(\Delta)$, the exponent, nor a multiple of its odd part is
supplied by reduction of forms or by genus theory.  Enumerating all reduced
forms already costs on the scale of $h$, and no unconditional
expected-polynomial-in-$\log N$ procedure for these data is proved here.
Conversely, this report does **not** prove that any one of these oracle problems is
factoring-equivalent.  The correct conclusion is only that the natural powering
proposal has moved the missing theorem into exact class-group order/exponent
information (and, for a randomized version, class sampling).

## Exact-uniform oracle versus an actual sampler

The probability theorems above deliberately grant exact iid uniform samples.
No such unconditional expected-polynomial sampler is constructed here.  The
following operations are factor-free and polynomial-time once a class is
supplied:

* canonical reduction and equality with the inverse;
* composition and squaring of forms;
* extracting a divisor from $A,F_0,F_1$ using (3) or (5).

They do not establish randomness.  A random walk additionally needs an
explicit generating set and a proved mixing bound.  Exact uniformity generally
needs still more information, such as group order/invariant factors or a
perfect-sampling argument.  None is a consequence of the fundamental
discriminant formula.

There is a genuine surviving factor-free way to construct *some* classes.  For
an auxiliary odd prime $\ell\nmid\Delta$ with
$(\Delta/\ell)=1$, find a root $b^2=\Delta\pmod{4\ell}$, form

\[
[\ell,b,(b^2-\Delta)/(4\ell)],
\]

and reduce it.  Choosing one of the two roots chooses inverse prime-ideal
classes.  All of this is polynomial in $\log N+\log\ell$.  What is missing is
an unconditional theorem that a polynomial-time distribution on such
$\ell$'s, their products, or walk lengths places inverse-polynomial mass on
$A,F_0,F_1$.  A deliberately biased sampler might do so; the uniform lower
bound does not refute it.

The standard genus characters do not currently supply that bias.  Their
explicit definitions require a nontrivial prime-discriminant divisor of
$\Delta$, which is the hidden orientation.  The factor-free aggregate is
constant: if an equivalent primitive form has leading coefficient $r$ coprime
to $\Delta$ (equivalently, $r$ is primitively represented), its discriminant
identity gives $\Delta\equiv b^2\pmod{4r}$, hence

\[
\left(\frac{\Delta}{r}\right)=1.
\]

This only kills the aggregate-character shortcut.  It is not a proof that a
vector-valued, symmetric, or otherwise canonically constructed genus mechanism
cannot exist.

## Exact retry boundary and scope

The kill-first result is:

* a direct exact-uniform trial needs exactly $2h/t$ expected samples;
* the complete iid square-collision scheme has exact success (10) and birthday
  scale $\sqrt{h/t}$;
* polynomially many samples have exponentially small success on infinite
  balanced families by (13)--(14);
* the even-discriminant class $E=[2,2,(N+1)/2]$ is a concrete nonprincipal
  ambiguous counterexample to universal extraction;
* exponent powering can evade the $1/h$ hit rate only after receiving
  theorem-strength order/exponent information, and even the most naive such
  power can land entirely in the exceptional direction.

This closes only iid/near-uniform ambiguity hunting, ordinary inverse
collisions, square-collision birthday amplification, and the displayed naive
powering rules.  It does not rule out designed nonuniform class samplers,
nonuniform exponent choices, richer genus vectors, factor-revealing failures
inside a composition algorithm, real-quadratic infrastructure, or class-group
methods not based on locating these ambiguous forms.
