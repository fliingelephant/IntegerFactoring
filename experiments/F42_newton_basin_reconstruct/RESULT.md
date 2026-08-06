# Exact Newton dynamics and the surviving factoring obstruction

## Attestation

This proof was reconstructed solely from the theorem statement and key ideas supplied in the task. I did not open, read, search, list, or otherwise inspect any candidate proof, audit, canonical file, registry, progress note, other experiment artifact, or Git history. I used no numerical, symbolic, programmatic, or experimental computation and made no external search. Apart from creating the requested target directory, the only filesystem action was writing this file.

## 1. The projective map over a prime field

Let (r) be an odd prime, let (s\in\mathbb F_r^*), put (a=s^2), and define

\[
F([X:Z])=[X^2+s^2Z^2:2XZ]
\quad\text{on }\mathbb P^1(\mathbb F_r).
\]

The two displayed homogeneous forms have degree (2). They have no common projective zero, even over an algebraic closure of (\mathbb F_r). Indeed, a common zero would satisfy (2XZ=0). Since (r) is odd, either (X=0) or (Z=0). If (X=0), then (X^2+s^2Z^2=s^2Z^2\ne0) at a projective point; if (Z=0), then (X^2+s^2Z^2=X^2\ne0). Thus (F) is everywhere defined. Because its homogeneous coordinate forms are coprime quadratics, it is a morphism of degree (2).

Define

\[
M([X:Z])=[X-sZ:X+sZ].
\]

Its matrix has determinant (2s\ne0), so (M\in\operatorname{PGL}_2(\mathbb F_r)) is a global projective automorphism. In fact,

\[
M^{-1}([U:V])=[s(U+V):V-U].
\]

Writing (F([X:Z])=[A:B]), direct homogeneous algebra gives

\[
\begin{aligned}
A-sB&=X^2+s^2Z^2-2sXZ=(X-sZ)^2,\\
A+sB&=X^2+s^2Z^2+2sXZ=(X+sZ)^2.
\end{aligned}
\]

Consequently, for (Q([U:V])=[U^2:V^2]),

\[
M\circ F=Q\circ M,
\qquad\text{hence}\qquad
M\circ F\circ M^{-1}=Q
\]

on all of (\mathbb P^1), not merely on an affine chart.

The four potentially exceptional affine/projective points are covered explicitly:

\[
\begin{array}{c|c|c}
P&M(P)&Q(M(P))\\ \hline
s=[s:1]&[0:1]&[0:1]\\
-s=[-s:1]&[1:0]&[1:0]\\
0=[0:1]&[-1:1]&[1:1]\\
\infty=[1:0]&[1:1]&[1:1].
\end{array}
\]

Thus (F(s)=s), (F(-s)=-s), (F(0)=\infty), and (F(\infty)=\infty).

For every (k\ge0),

\[
Q^k([U:V])=[U^{2^k}:V^{2^k}].
\]

The point (s) corresponds to ([0:1]), and (Q^k([U:V])=[0:1]) holds exactly when (U=0), which already means the initial point was (s). Likewise, (-s) corresponds to ([1:0]), and an iterate equals it exactly when (V=0), which already means the initial point was (-s). Therefore

\[
F^k(P)=s\iff P=s,
\qquad
F^k(P)=-s\iff P=-s
\]

for every (P\in\mathbb P^1(\mathbb F_r)) and every (k\ge0). Each root has no basin beyond itself.

## 2. Nonvanishing when (r\equiv3\pmod4)

Assume now (r\equiv3\pmod4). Then (-1) is not a square in (\mathbb F_r): if (z^2=-1), Fermat's theorem would give

\[
1=z^{r-1}=(z^2)^{(r-1)/2}=(-1)^{(r-1)/2}=-1,
\]

because ((r-1)/2) is odd.

For any (x\in\mathbb F_r^*),

\[
x^2+a=x^2+s^2=s^2\bigl((x/s)^2+1\bigr)\ne0.
\]

Also (2x\ne0). Hence the affine Newton rule

\[
T(x)=\frac{x^2+a}{2x}
\]

maps (\mathbb F_r^*) into (\mathbb F_r^*). By induction, a nonzero start has only nonzero affine iterates; it never reaches (0), no denominator vanishes, and (x_k^2+a\ne0) at every iterate.

## 3. Exact named gcd tickets modulo (N=pq)

Let (N=pq), where (p\ne q) are primes congruent to (3\pmod4). Let (s\in(\mathbb Z/N\mathbb Z)^*) be public, set (a=s^2), and take (x_0) uniformly from ((\mathbb Z/N\mathbb Z)^*). For (r\in\{p,q\}), define the disjoint events

\[
E_r^+=[x_0\equiv s\pmod r],
\qquad
E_r^-=[x_0\equiv-s\pmod r],
\qquad
E_r=E_r^+\vee E_r^-.
\]

We also use these event symbols as their (0)-(1) indicators in exponents.

Reduction modulo either prime turns the recurrence into the prime-field map just proved. Starting from a unit, the nonvanishing result shows inductively that both (2x_k) and (x_k^2+a) are units modulo both primes. Thus (x_{k+1}) is well defined modulo (N) for every (k), and

\[
\gcd(2x_k,N)=1,
\qquad
\gcd(x_k^2+a,N)=1.
\]

Root rigidity gives, for each (r\in\{p,q\}),

\[
x_k\equiv s\pmod r\iff E_r^+,
\qquad
x_k\equiv-s\pmod r\iff E_r^-.
\]

Since (r) is odd,

\[
r\mid x_k^2-a
\iff x_k\equiv s\text{ or }-s\pmod r
\iff E_r.
\]

Because (N) is squarefree, its gcd with any integer is the product of precisely the primes that divide that integer. Therefore, for every (k\ge0), exactly

\[
\boxed{\gcd(2x_k,N)=1},
\qquad
\boxed{\gcd(x_k^2+a,N)=1},
\]

\[
\boxed{\gcd(x_k^2-a,N)=p^{E_p}q^{E_q}},
\]

\[
\boxed{\gcd(x_k-s,N)=p^{E_p^+}q^{E_q^+}},
\qquad
\boxed{\gcd(x_k+s,N)=p^{E_p^-}q^{E_q^-}}.
\]

These factorizations do not depend on (k). Hence iteration after (k=0) adds no opportunity among the named denominator, numerator, residual, and root-difference gcd tickets: every prime that any such later ticket can expose was already determined by the corresponding initial local-root event.

## 4. Exact count for an accepted uniform-unit restart

By the Chinese remainder theorem, unit classes modulo (N) are pairs in (\mathbb F_p^*\times\mathbb F_q^*), so there are ((p-1)(q-1)) of them. In each (\mathbb F_r^*), exactly two residues are (s) and (-s), and (r-3) are neither. The complete partition is

\[
\begin{array}{c|c|c}
\text{local status}&\text{number of unit classes}&\text{named-ticket result}\\ \hline
E_p^c\cap E_q^c&(p-3)(q-3)&\text{failure}\\
E_p\cap E_q^c&2(q-3)&\text{proper factor}\\
E_p^c\cap E_q&2(p-3)&\text{proper factor}\\
E_p\cap E_q&4&\text{two successes, two failures}.
\end{array}
\]

For the last row, the four CRT square roots of (a) have sign patterns

\[
(+,+),\quad(+,-),\quad(-,+),\quad(-,-).
\]

The same-sign patterns are the public global roots (s) and (-s). At (s), for example, the residual and (x-s) gcds equal (N), while the (x+s) gcd equals (1); all are trivial. The analogous statement holds at (-s). These two classes are unhelpful. For the opposite-sign pattern ((+,-)), the two root-difference gcds are (p) and (q), respectively; for ((-,+)) they are (q) and (p). These two classes are successful, even though the residual gcd is (N).

It follows that the exact number of successful unit starts is

\[
2(q-3)+2(p-3)+2=2p+2q-10,
\]

and the exact accepted-unit success probability is

\[
\boxed{\alpha(p,q)=\frac{2p+2q-10}{(p-1)(q-1)}}.
\]

Equivalently, the failure count is

\[
(p-3)(q-3)+2.
\]

This count includes the endpoint (p=3) or (q=3). When (r=3), the number (r-3) of non-root units is exactly zero, while (s\ne-s) still holds; every row and formula above remains valid without an exceptional correction.

## 5. Exact uniform-residue rejection

Consider one complete restart defined as follows. Draw (Y) uniformly modulo (N) and compute (d=\gcd(Y,N)). If (1<d<N), return that proper factor. If (Y=0), redraw. Otherwise (d=1), so use (Y) as the uniform-unit Newton start. The instruction to redraw only at zero is exhaustive because (\gcd(Y,N)=N) occurs for a residue modulo (N) exactly when (Y=0).

After zero rejection, the accepted residue is uniform among the (N-1=pq-1) nonzero residues. Of these,

* (q-1) are nonzero multiples of (p), and immediately return (p);
* (p-1) are nonzero multiples of (q), and immediately return (q);
* ((p-1)(q-1)) are units, of which (2p+2q-10) are successful by the preceding count.

Thus the exact complete-restart success count is

\[
(q-1)+(p-1)+(2p+2q-10)=3p+3q-12,
\]

so

\[
\boxed{\beta(p,q)=\frac{3p+3q-12}{pq-1}}.
\]

Failure occurs only at one of the unsuccessful unit starts, giving exactly

\[
\boxed{1-\beta(p,q)=\frac{(p-3)(q-3)+2}{pq-1}}.
\]

The two displayed numerators sum to (pq-1), as they must. A raw draw is nonzero with probability ((N-1)/N); therefore the number of raw draws required to obtain the nonzero residue of one complete restart is geometric with exact mean

\[
\boxed{\frac{N}{N-1}}.
\]

## 6. Fresh restarts and adaptive public choices of (s)

Suppose that before fresh restart (i), an algorithm chooses (s_i) as an arbitrary function of its public history, subject to the choice being factor-free and valid: (\gcd(s_i,N)=1), and the choice is made before the fresh random start is drawn. Conditional on every possible prior history, multiplication by (s_i^{-1}) is a bijection of ((\mathbb Z/N\mathbb Z)^*). Hence the fresh ratio (x_{0,i}/s_i) is uniform on the unit group, and the successful set has the same cardinality (2p+2q-10), independently of the chosen unit (s_i). Thus the conditional success probability of an accepted-unit restart is always exactly (\alpha(p,q)).

The same argument applies to the unit part of uniform-residue rejection, while the counts of nonzero nonunits do not involve (s_i). Hence the conditional success probability of a complete uniform-residue restart is always exactly (\beta(p,q)).

For either restart model, write (\rho=\alpha) or (\rho=\beta), respectively. A union bound conditional on the successive histories gives

\[
\Pr(\text{success in at most }K\text{ fresh restarts})
\le \min\{1,K\rho\}.
\]

If all (K) restarts are carried out, the stronger identity (1-(1-\rho)^K) holds, since at each stage the conditional failure probability is (1-\rho); the union bound is the claimed consequence. History-dependent public selection of valid (s_i) does not alter either conclusion. A proposed (s_i) whose gcd with (N) is already a proper factor is itself a prior factoring success, not a factor-free parameter choice covered by this conditional statement.

## 7. Infinitely many balanced hard instances

The prime number theorem in arithmetic progressions gives

\[
\pi(t;4,3)\sim\frac{t}{2\log t}.
\]

Consequently,

\[
\pi(2X;4,3)-\pi(X;4,3)\sim\frac{X}{2\log X}\longrightarrow\infty.
\]

Thus, for every sufficiently large (X), the interval ([X,2X]) contains at least two distinct primes congruent to (3\pmod4). To make an infinite family with no reused primes, take (X_j=3^j) for all sufficiently large (j) and choose two such primes (p_j\ne q_j) in ([X_j,2X_j]). These intervals are pairwise disjoint, so the resulting balanced pairs are distinct.

For a pair in ([X,2X]), (X^2\le N=pq\le4X^2). Moreover,

\[
\alpha(p,q)
\le \frac{8X}{(X-1)^2}
=O(X^{-1})
=O(N^{-1/2}),
\]

and

\[
\beta(p,q)
\le \frac{12X}{X^2-1}
=O(X^{-1})
=O(N^{-1/2}).
\]

The last equality in each line uses (\sqrt N\le2X), so (X^{-1}\le2N^{-1/2}).

Let (n=\lceil\log_2N\rceil), the input bit length. For any (K(n)) polynomial in (n), the fresh-restart bound is

\[
K(n)\rho=O\!\left(K(n)N^{-1/2}\right)
=O\!\left(K(n)2^{-n/2}\right),
\]

up to an inessential constant caused by the ceiling. This is negligible in (n): it is eventually smaller than (n^{-c}) for every fixed (c>0).

If fresh restarts continue until the first success, the constant conditional success probability makes the number of restarts geometric with exact mean (1/\rho), even under the history-dependent valid choices of (s_i) above. Therefore, on this balanced infinite family, repeat-until-success requires

\[
\mathbb E[\text{restarts}]=\Omega(\sqrt N)
\]

in both the accepted-unit and complete uniform-residue models.

## Scope and verdict

The analysis concerns exactly the named denominator (\gcd(2x_k,N)), numerator (\gcd(x_k^2+a,N)), residual (\gcd(x_k^2-a,N)), and root-difference (\gcd(x_k\mp s,N)) tickets. It makes no assertion about longer cross-iterate collisions, order tests, arbitrary nonlinear processing of a transcript, primes congruent to (1\pmod4), other maps, (p)-adic lifts, stochastic, piecewise, or canonical-metric dynamics, or factoring in general.

**Verdict.** All claims stated within that scope are correct. The exact surviving obstruction is that the global conjugacy turns Newton iteration into coordinatewise squaring, and the two root hyperplanes (U=0) and (V=0) have no preimages beyond themselves. Consequently iteration never enlarges the local-root event set. Modulo (pq), named-ticket success is confined to the starts that are a root at exactly one prime, together with the two opposite-sign CRT roots; the two same-sign public roots remain trivial. This leaves only (O(p+q)) successful classes among (\Theta(pq)) possible starts, while raw-residue gcd rejection adds only another (O(p+q)), yielding the exact (O(N^{-1/2})) balanced-instance rate.
