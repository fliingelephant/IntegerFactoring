# Polynomial root basins and gcd screening

## 1. The local backward basin

Let

\[
H(x)=x(x-1)=x^2-x
\]

over \(\mathbb F_r\), where \(r\) is an odd prime, \(r\ne 5\), and
\(\left(\frac 5r\right)=-1\). Put \(A_r=\{0,1\}\).

The equation \(H(x)=0\) has exactly the roots \(0\) and \(1\). The equation
\(H(x)=1\) is

\[
x^2-x-1=0.
\]

Its discriminant is \(5\). Since \(5\) is a quadratic nonresidue modulo
\(r\), this equation has no root in \(\mathbb F_r\). Therefore

\[
H^{-1}(A_r)=A_r. \tag{1}
\]

Also, \(H(0)=H(1)=0\), so \(H(A_r)\subseteq A_r\). If an orbit
\(x_{i+1}=H(x_i)\) satisfies \(x_i\in A_r\) for some \(i\geq 1\), then
(1) gives \(x_{i-1}\in A_r\). Repeating this argument gives
\(x_0\in A_r\). The converse follows from forward invariance. Hence

\[
(\exists i\geq0:\ x_i\in A_r)\quad\Longleftrightarrow\quad x_0\in A_r.
\tag{2}
\]

Equivalently, \(H^{-i}(A_r)=A_r\) for every \(i\geq0\). Thus the full
backward basin of the two targets has only two points.

## 2. Exact probability modulo a semiprime

Let \(N=pq\), where \(p\ne q\) are odd primes satisfying the local
hypotheses above. CRT identifies a residue \(x\pmod N\) with
\((x_p,x_q)\in\mathbb F_p\times\mathbb F_q\), and iteration of \(H\)
acts coordinatewise.

At each screened state, including the initial state \(x_0\), compute

\[
d_{i,0}=\gcd(x_i,N),\qquad d_{i,1}=\gcd(x_i-1,N).
\]

A success means that one of these gcds is \(p\) or \(q\), not \(1\) or
\(N\).

By (2), a coordinate that does not start in \(\{0,1\}\) never enters it.
It is therefore enough to classify the two initial CRT coordinates:

* If neither coordinate is in \(\{0,1\}\), no target gcd can succeed.
* If exactly one coordinate is in \(\{0,1\}\), the corresponding gcd at
  time zero returns the prime on that side.
* If both coordinates are targets with different labels, namely
  \((0,1)\) or \((1,0)\), a time-zero gcd returns a proper factor.
* If both coordinates have the same label, namely \((0,0)\) or
  \((1,1)\), the relevant gcd is \(N\). Both target labels map to \(0\),
  so later screening cannot separate the two sides.

There are \(2(q-2)\) starts whose \(p\)-coordinate alone is a target,
\(2(p-2)\) whose \(q\)-coordinate alone is a target, and two mixed-label
target starts. Thus a uniform residue modulo \(N\) succeeds with exact
probability

\[
P_{\mathrm{all}}
=\frac{2(q-2)+2(p-2)+2}{pq}
=\boxed{\frac{2p+2q-6}{pq}}. \tag{3}
\]

This event is already decided by the initial CRT classes. Consequently,
(3) is unchanged for every time cap \(t\geq0\), provided that screening
includes \(x_0\). If screening starts only after the first application of
\(H\), the two mixed-label starts have already coalesced at \((0,0)\), so
the numerator would instead be \(2p+2q-8\). This convention matters.

### Uniform starts in the unit group

Now sample \(x_0\) uniformly from \((\mathbb Z/N\mathbb Z)^\times\). Its
CRT coordinates are independent and uniform in
\(\mathbb F_p^\times\) and \(\mathbb F_q^\times\). The only available
target in each local unit group is \(1\). A proper gcd occurs exactly when
one coordinate equals \(1\) and the other does not. The all-\(1\) start
gives \(\gcd(x_0-1,N)=N\), and then maps to the all-zero start. Therefore

\[
P_{\mathrm{units}}
=\frac{(q-2)+(p-2)}{(p-1)(q-1)}
=\boxed{\frac{p+q-4}{(p-1)(q-1)}}. \tag{4}
\]

This probability is also independent of the time cap.

## 3. Scaling and affine conjugacy

Let \(c\in(\mathbb Z/N\mathbb Z)^\times\), and let \(L_c(y)=cy\). Then

\[
H_c(x)=\frac{x(x-c)}c,
\qquad
H_c(L_c(y))=cH(y)=L_c(H(y)).
\]

Thus

\[
H_c=L_c\circ H\circ L_c^{-1}. \tag{5}
\]

The image of \(\{0,1\}\) is \(\{0,c\}\). Reduction of \(c\) is nonzero
on both prime sides, so (1) and (5) give

\[
H_{c,r}^{-1}(\{0,c_r\})=\{0,c_r\},\qquad r\in\{p,q\}.
\]

Multiplication by a unit preserves both the uniform distribution on all
residues and the uniform distribution on units. Hence screening
\(\gcd(x_i,N)\) and \(\gcd(x_i-c,N)\) has exactly (3) for uniform residue
starts and exactly (4) for uniform unit starts.

More generally, let

\[
L(y)=ay+b,\qquad a\in(\mathbb Z/N\mathbb Z)^\times,
\]

and define

\[
G=L\circ H\circ L^{-1}.
\]

Explicitly,

\[
G(x)=\frac{(x-b)(x-b-a)}a+b. \tag{6}
\]

Its target set is

\[
T=L(\{0,1\})=\{b,b+a\}.
\]

For each prime side, \(G_r^{-1}(T_r)=T_r\), and an orbit reaches \(T_r\)
if and only if it starts there. An affine bijection preserves the uniform
distribution on all residues. Thus checks against the two targets have
probability (3) for a raw uniform residue modulo \(N\).

There is a required distinction for unit sampling. Translation does not,
in general, preserve the unit group. Formula (4) remains valid when one
samples \(y\) uniformly from the units and then sets \(x=L(y)\). It need
not remain valid when one instead samples raw \(x\) uniformly from the
units.

For completeness, the raw-unit probability under an affine conjugate can
be counted exactly. Write \(t_0=b\), \(t_1=b+a\), and define

\[
S_r=\{j\in\{0,1\}:t_j\not\equiv0\pmod r\},
\quad k_r=|S_r|,
\quad m=|S_p\cap S_q|.
\]

Among raw unit starts, the number of successful CRT pairs is

\[
k_p(q-1-k_q)+k_q(p-1-k_p)+(k_pk_q-m),
\]

so the probability is

\[
\frac{k_p(q-1)+k_q(p-1)-k_pk_q-m}{(p-1)(q-1)}. \tag{7}
\]

The last term in the first count is the number of pairs with two different
target labels. On a factor-free branch, either one target is zero modulo
\(N\), which gives (4), or both targets are units, which gives

\[
\frac{2p+2q-10}{(p-1)(q-1)}.
\]

Thus an arbitrary affine translation cannot silently inherit the raw-unit
formula (4).

### Raw parameter sampling and mixed public data

Division by \(c\) in (5) is valid only after checking \(\gcd(c,N)=1\).
For a raw uniform \(c\pmod N\), the cases are:

\[
\begin{array}{c|c}
\text{case}&\text{number of residues}\cr
\hline
\gcd(c,N)=1&(p-1)(q-1)\cr
\gcd(c,N)\in\{p,q\}&p+q-2\cr
c=0\pmod N&1.
\end{array}
\]

The middle branch has already factored \(N\). The last branch makes
\(H_c\) undefined and must be rejected; \(\gcd(c,N)=N\) is not a proper
factor. Conditional on the unit branch, the orbit probabilities are
exactly (3) or (4), according to the start distribution.

If one insists on one unconditional raw-\(c\) trial, treats \(c=0\) as a
failed invalid trial, and uses an independent uniform-residue start, its
total success probability is

\[
\frac{p+q-2}{pq}
+\frac{(p-1)(q-1)}{pq}\,P_{\mathrm{all}}. \tag{8}
\]

For a uniform-unit start, replace \(P_{\mathrm{all}}\) in (8) by
\(P_{\mathrm{units}}\). A protocol that rejects and redraws \(c=0\) has a
different normalization, \(pq-1\). These construction-gcd branches must
not be credited to basin growth.

The same rule applies to every public coefficient, denominator, target,
and root. For any two public residues \(z,w\),

\[
z\equiv w\pmod p,quad z\not\equiv w\pmod q
\quad\Longrightarrow\quad
\gcd(z-w,N)=p,
\]

and the symmetric case returns \(q\). Taking \(w=0\) handles a public
value that vanishes on only one prime side. Therefore a mixed target/root
equality, a root collision on only one side, a nonunit affine multiplier,
or a mixed-zero target is an immediate gcd factor. The dynamical analysis
properly starts only on the branch where all required inverses exist and
no such public relation already factors \(N\).

## 4. An infinite balanced family

For every odd prime \(r\ne5\), quadratic reciprocity gives

\[
\left(\frac5r\right)=\left(\frac r5\right),
\]

because \(5\equiv1\pmod4\). The nonzero quadratic residues modulo \(5\)
are \(1\) and \(4\). Hence every prime \(r\equiv2\pmod5\) satisfies
\(\left(\frac5r\right)=-1\).

The prime number theorem in arithmetic progressions gives

\[
\pi(2X;5,2)-\pi(X;5,2)\sim\frac{X}{4\log X}.
\]

For every sufficiently large \(X\), the interval \([X,2X]\) therefore
contains at least two distinct primes congruent to \(2\pmod5\). Taking
such primes as \(p\) and \(q\), and taking a sequence of disjoint growing
intervals, gives infinitely many distinct semiprimes with

\[
X\le p,q\le2X.
\]

They are balanced: \(p/q\in[1/2,2]\), and \(p,q=\Theta(\sqrt N)\). It
follows from (3) and (4) that

\[
P_{\mathrm{all}}=\Theta(N^{-1/2}),
\qquad
P_{\mathrm{units}}=\Theta(N^{-1/2}),
\]

and in particular both are \(O(N^{-1/2})\). With independent fresh starts,
the number of trials to first success is geometric with mean \(1/P\).
Thus the expected number of trials is \(\Omega(\sqrt N)\); the expected
number of failed restarts, \((1-P)/P\), is also \(\Omega(\sqrt N)\).

## 5. The general backward-basin bound

Fix a public map \(F_N\) whose reduction commutes with CRT. For
\(r\in\{p,q\}\), write the induced local map as

\[
F_r:\mathbb F_r\longrightarrow\mathbb F_r,
\]

and let \(A_r\subseteq\mathbb F_r\) be the local target set for the
prescribed target-triggered gcd checks. For a time cap \(t\geq0\), define

\[
B_{r,t}
=\bigcup_{i=0}^{t}F_r^{-i}(A_r)
=\{u\in\mathbb F_r:\exists i\leq t, F_r^i(u)\in A_r\}. \tag{9}
\]

Let \(S_t\) be the event that the target-triggered gcd mechanism produces
a proper factor by time \(t\). A target ticket requires at least one local
orbit to hit its local target set. Therefore

\[
S_t\subseteq
\{U_p\in B_{p,t}\}\cup\{U_q\in B_{q,t}\}. \tag{10}
\]

For uniform \(U\pmod N\), CRT makes \(U_p,U_q\) independent and uniform.
Consequently,

\[
\Pr(S_t)
\leq
\frac{|B_{p,t}|}{p}+\frac{|B_{q,t}|}{q}
-\frac{|B_{p,t}|\,|B_{q,t}|}{pq}
\leq
\boxed{\frac{|B_{p,t}|}{p}+\frac{|B_{q,t}|}{q}}. \tag{11}
\]

Only the final, weaker union bound is needed. Equality with the union event
does not imply equality for factor success: both sides can hit matching
targets and yield gcd \(N\).

Now let \(R\) be public construction randomness, independent of the
uniform start. Let \(E\) be the factor-free construction branch: every
required public denominator is invertible and no public coefficient,
target, root, or relevant difference has a proper gcd with \(N\). For
each fixed outcome \(R=\rho\) in this branch, define
\(F_{r,\rho}\), \(A_{r,\rho}\), and \(B_{r,t}(\rho)\). Applying (11) first
and then averaging gives

\[
\Pr(S_t\mid E)
\leq
\mathbb E\!\left[
\frac{|B_{p,t}(R)|}{p}+\frac{|B_{q,t}(R)|}{q}
\,\middle|\,E
\right]. \tag{12}
\]

Without conditioning, a valid upper bound must separately include the
construction branch:

\[
\Pr(\text{any factor success})
\leq \Pr(E^c)
+\Pr(E)\,
\mathbb E\!\left[
\frac{|B_{p,t}(R)|}{p}+\frac{|B_{q,t}(R)|}{q}
\,\middle|\,E
\right]. \tag{13}
\]

If only part of \(E^c\) actually exposes a proper gcd, (13) can be
sharpened by using that event instead. Formula (12) is the precise averaged
claim on the factor-free branch.

## 6. Exact scope of the conclusion

The basin condition is necessary, not sufficient. A local target hit may
occur on both sides with the same public label and return \(N\), or the
decoder may fail to turn an asymmetric hit into its required gcd. Thus a
small basin proves a small upper bound for this target-ticket mechanism;
a large basin does not by itself prove a successful factorization method.

The special two-point conclusion for \(H\) and its conjugates does not
cover the following cases without a new analysis:

* A full-orbit decoder that uses periods, collisions, orbit comparisons,
  or other information without requiring a hit on the stated targets.
* An unrelated map, or a rule chosen as a function of \(N\), whose local
  backward basins may differ. Bound (11) can be applied only after its own
  CRT-compatible local maps and basins are defined.
* An iteration with extra state. Its basin lives in the full state space,
  not only in \(\mathbb F_r\).
* Starts whose CRT coordinates are correlated or whose distribution is
  concentrated on a special subset. The factors \(|B_{r,t}|/r\) use
  uniform local marginals; the product refinement also uses independence.
* Integer, prime-power, or p-adic lifts that extract information absent
  from the dynamics over \(\mathbb F_p\) and \(\mathbb F_q\).
* Construction branches on which a coefficient, denominator, target,
  root, or public difference already has a proper gcd with \(N\). Those
  branches factor immediately and are accounted for before orbit analysis.

Noninvertibility alone does not force a target basin to grow. A functional
graph can have many collisions far from the selected targets while the
targets have no incoming edges from outside their own set. Equation (1) is
an explicit example.

Likewise, exponential formal composition degree gives only an upper bound,
not a lower bound, on the number of preimages. Although the formal degree
of \(H^{\circ i}\) is \(2^i\), roots can overlap, equations can have far
fewer roots than their degree, and polynomials of high degree can represent
the same function on a finite field after reduction modulo \(x^r-x\). The
reverse-reachable part of the functional graph, not formal degree, controls
\(|B_{r,t}|\). Here that size stays exactly two for every \(t\).

## 7. Edge cases

The prime \(5\) must be excluded. In \(\mathbb F_5\), the equation
\(x^2-x-1=0\) has discriminant zero and the double root

\[
x=\frac12=3\pmod5.
\]

Indeed, \(H(3)=1\). Hence

\[
H^{-1}(\{0,1\})=\{0,1,3\}
\]

over \(\mathbb F_5\), so the two-point basin theorem and the resulting
iteration-count independence do not apply. In fact \(3\to1\to0\), while
\(H(x)=3\) has no solution modulo \(5\), so the full basin is
\(\{0,1,3\}\).

The usual Legendre symbol in the denominator is stated for odd primes, so
\(r=2\) is outside the hypothesis. Directly, \(\{0,1\}=\mathbb F_2\) and
\(H\) is the zero function on \(\mathbb F_2\); therefore
\(H^{-1}(\{0,1\})=\{0,1\}\) holds trivially, but for a different reason.
If one allows \(N=2q\) and keeps the same time-zero screening convention,
a direct CRT count happens to give (3) and (4) with \(p=2\). This does not
justify using the odd-prime discriminant proof, and such moduli are not the
balanced odd-semiprime family constructed above.

## Verdict

**SUCCESS.** The bare theorem is proved with the necessary conventions:
the initial state is screened; division parameters and affine multipliers
are units; construction-gcd branches are counted separately; and affine
translation preserves the raw-residue statement but not, in general, a
raw-unit sampling statement. The general basin estimate is a necessary
target-ticket bound only, with the exclusions stated above.
