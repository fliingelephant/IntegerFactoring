# F245 V2 blind reconstruction

## Authentication and verdict

- Expected SHA-256: `ad4ff2a363de6e30c12245a7ecaefa7990dc560893e3ddebb68bfb14d8338440`
- Observed SHA-256: `ad4ff2a363de6e30c12245a7ecaefa7990dc560893e3ddebb68bfb14d8338440`
- Authentication: **PASS**
- Strict statement-only verdict: **FAIL**

The inverse-quotient estimates, marker construction, marker-avoidance
estimates, cyclic-group calculation, common-order calculation, and carry
identities reconstruct.  The final restricted-grammar and Markov conclusion
does not reconstruct from the statement alone.  The statement does not
define the restricted grammar or the torus factor screens whose outputs the
probability bound must exhaust.  This is a self-containment failure, not a
counterexample to the reconstructed arithmetic lemmas.

## 1. Inverse quotients

Fix (t).  If (K(u)=t), then

\[
uv=1+tN<N^2.
\]

Each admissible (u) is a positive divisor of (1+tN), and (v) is then
fixed.  Dropping the restrictions (u,v<N) and (gcd(uv,N)=1) can only
increase the count.  Hence

\[
\#\{u:K(u)=t\}\leq \tau(1+tN)\leq \Delta_N,
\]

so

\[
\Pr(K(U)=t)\leq {\Delta_N\over\varphi(N)}.
\]

Only (K=0) and (K=1) merge when (K) is replaced by (widehat K).
Thus every atom of (widehat K) has mass at most
(2\Delta_N/\varphi(N)).  Its support is contained in an interval of fewer
than (N) consecutive integers.  A residue class modulo a prime
(ell<N) therefore contains at most (lceil N/\ell\rceil) possible
values, giving

\[
\Pr(\widehat K\equiv r\pmod\ell)
\leq {2\lceil N/\ell\rceil\Delta_N\over\varphi(N)}
=\beta_{N,\ell}.
\]

For distinct odd primes (p,q),

\[
{\varphi(N)\over N}=(1-1/p)(1-1/q)\geq {8\over15}>{1\over2}.
\]

Also (lceil N/\ell\rceil<2N/\ell).  Consequently

\[
\beta_{N,\ell}<{8\Delta_N\over\ell}.
\]

For two fresh copies, condition on (K_i).  If
(ell\mid\Gamma_{ij}), equality is excluded by the replacement value
(1), and (K_jequiv K_i\pmodell).  The residue-class mass of (K_j)
is at most
(lceil N/\ell\rceil\Delta_N/\varphi(N)leqeta_{N,ell}).
This proves (2).

Sequential conditional uniformity is sufficient.  At the time a fresh
seed is drawn, the same atom or residue bound holds conditional on the
prior transcript.  Pad a stopped run to the public cap if necessary.  If a
selected product is divisible by (ell), then at least one of the at most

\[
Q(n)+{Q(n)\choose2}
\]

available values or differences is divisible by (ell).  A union bound
proves (3).  Selection, positive exponents, and stopping do not alter this
implication.

## 2. Marker family

Let the four distinct marker primes lie in ([X,2X]), with (X) tending
to infinity.  Choose primitive residues at the two (ho)-markers.  The
first CRT class is reduced modulo

\[
M_1=24\lambda_+\lambda_-\rho_+\rho_-.
\]

Linnik's theorem supplies a prime (p) in this class and constants (C,L)
independent of (X) such that

\[
p\leq C M_1^L\leq C_1X^{4L}.
\]

The specified residues give

\[
\lambda_+\mid p-1,quad \lambda_-\mid p+1,quad
\operatorname{ord}_{\rho_\pm}(p)=\rho_\pm-1.
\]

Because (p\equiv13\pmod {24}), write

\[
p^2-1=2^3 3^eS,qquad
S=\prod_{s\geq5}s^{e_s},qquad e\geq1.
\]

The (ho)-markers do not divide (p^2-1), since (p) has order
(ho_pm-1>2) modulo them.  Thus all moduli in the second CRT system are
coprime.  For every (s\geq5), a unit residue that is neither (+1) nor
(-1) exists.  At a (lambda)-marker, a primitive residue is such a
choice.  The second class is therefore reduced.  Its modulus (M_2)
satisfies

\[
M_2
=8\,3^{\max(e,2)}S\rho_+\rho_-
\leq 12(p^2-1)X^2.
\]

A second use of Linnik gives

\[
q\leq C M_2^L\leq C_2(p^2X^2)^L.
\]

The congruences at (ho_pm) and the primitive residues at
(lambda_pm) now give all four divisibilities and order identities in
(5)--(6).  Also (p\not=q), since (p\equiv1\pmod3) and
(q\equiv2\pmod3).

The local valuations determine the four signed gcds.  Namely,

\[
v_2(p-1)=2,quad v_2(p+1)=1,quad
v_2(q-1)=1,quad v_2(q+1)=2,
\]

(3mid p-1), (3\nmid p+1), (3\nmid q-1), and
(v_3(q+1)=1).  Every prime (s\geq5) dividing (p^2-1) divides neither
(q-1) nor (q+1).  Hence

\[
\gcd(p-1,q-1)=2,quad
\gcd(p-1,q+1)=12,quad
\gcd(p+1,q-1)=2,quad
\gcd(p+1,q+1)=2.
\]

Equivalently, (gcd(p^2-1,q^2-1)=24).

The two Linnik bounds imply (N=pq\leq C_3X^A) for one absolute
constant (A).  Therefore

\[
n\leq A\log_2X+O(1).
\]

After decreasing an absolute positive constant (c), every marker in
([X,2X]) exceeds (2^{cn}) for all sufficiently large (X).  Taking
an unbounded sequence of (X)'s gives an infinite family of distinct
semiprimes.

## 3. Signed powers and the square baseline

Suppose a marker (ell) divides (N^k-\sigma).  At a
(lambda_a)-marker, (N\equiv aq\pmodell), so squaring the equality
((aq)^k=\sigma) gives

\[
q^{2k}=1\pmodell.
\]

Thus (ell-1mid2k), and (k\geq(\ell-1)/2).  The same argument at a
(ho_b)-marker uses (N\equiv bppmodell).  A single such signed-power
factor has binary length at least

\[
k\log_2N-O(1)=2^{\Omega(n)}.
\]

A fixed numerical-quasipolynomial (Q(n)) is (2^{o(n)}).  Therefore no
factor, and hence no nonzero product of total binary length at most (Q(n)),
can contain a marker for all sufficiently large family members.  This
proves (9).

The baseline also misses every marker.  For example, modulo
(lambda_a),

\[
N^2\equiv q^2\not\equiv1,
\]

because (q) has order (lambda_a-1>2).  The (ho_b) case is
identical.

Finally, modulo (lambda_a),

\[
N-ab\equiv a(q-b).
\]

If (lambda_amid N-ab), then it divides
(gcd(p-a,q-b)), which is one of the four numbers in (7), all at most
(12).  This is impossible for a large marker.  The argument for
(ho_b) is symmetric.  Hence the baseline, signed powers, and base
exponent all miss the appropriate markers.

## 4. Bank probability and divisor growth

The standard maximum-order divisor bound

\[
\tau(m)\leq
\exp\!\left(O\!\left({\log m\over\log\log m}\right)\right)
\]

for (m<N^2) gives (Delta_N=2^{o(n)}).  Summing (3) over the four
markers gives

\[
\Pr\bigl(\gcd(W_{\rm iq},
\lambda_+\lambda_-\rho_+\rho_-)>1\bigr)
\leq
32\left(Q+{Q\choose2}\right){\Delta_N\over\min\ell}
=2^{-\Omega(n)}.
\]

Thus (12) and the marker-avoidance assertion for (13) reconstruct.

## 5. What reconstructs at the torus interface

There is a standard sufficient model for the claimed torus calculation.
For a prime (r), let

\[
\mathcal A_r=\mathbb F_r[w]/(w^2-D)
\]

with conjugation (w\mapsto-w).  If the quadratic character of (D) is
(epsilon\in\{+1,-1\}), the norm-one group has order (r-\epsilon).
The Hilbert--90 map

\[
z\longmapsto z/\bar z
\]

maps uniform units of (mathcal A_r) uniformly onto this group.  If a
coefficient pair is uniform modulo (N) and one conditions on its norm
being a unit modulo both (p) and (q), CRT makes the two local units, and
hence the two torus points, independent and uniform.

For a cyclic group (C_m), the kernel of (x\mapsto x^E) has exactly
(gcd(E,m)) elements.  Therefore, for an exponent fixed before a fresh
uniform point is sampled,

\[
\Pr(x^E=1)={\gcd(E,m)\over m}.
\]

If (E=(N-ab)W) misses (lambda_a) and (ho_b), then

\[
{\gcd(E,p-a)\over p-a}\leq {1\over\lambda_a},qquad
{\gcd(E,q-b)\over q-b}\leq {1\over\rho_b}.
\]

Hence any *specified* factor test whose success implies at least one of
these two local identity events has probability at most their sum.

Likewise, if a coefficient pair is uniform in (mathbb F_r^2), the
equation (a^2-Db^2=0) has fewer than (2r) solutions.  A union bound over
(p,q) then gives the stated (2/p+2/q) bound.  This derivation needs the
uniform coefficient law.

The common-order statement is purely algebraic.  An integer that is the
exact order of an element in both local groups divides both group orders,
and hence divides their gcd.  Across the four orientations, the lcm of all
such integers divides

\[
\operatorname{lcm}(2,12,2,2)=12.
\]

Thus common-order lcm accumulation cannot add a large marker.

These facts establish the numerical bound (14) only after the legal torus
samples and factor-return tests have been formally specified.

## 6. Markov truncation and the decisive gap

If a Las Vegas algorithm had expected running time at most (Q(n)), then
Markov's inequality would give

\[
\Pr(T\leq2Q(n))\geq {1\over2}.
\]

For a formally defined grammar in which every factor return within the
truncation came from one of the following exhaustive events,

1. an inverse-quotient bank value contains a marker;
2. a nonclean uniform norm screen returns a factor; or
3. a clean fresh torus trial has a local return,

the preceding bounds and a union bound over at most a numerical-QP number
of operations would make the probability of any verified factor within
(2Q(n)) equal to (2^{-\Omega(n)}).  That would contradict the Markov
lower bound.

The authenticated statement does not define that grammar.  In particular,
it does not define:

- the probability space for a “factor-free Hilbert--90 sample” or for a
  “public coefficient pair”;
- the coefficient screens, norm screens, clean identity screens, or their
  exact factor-return rules;
- the associated two-primary Miller chain, its endpoint exponent, or the
  event by which it returns a factor;
- when the public exponent is fixed relative to the point it powers; or
- the complete list of operations and output paths allowed to an algorithm
  “confined to this grammar.”

Without the coefficient law, the (2/p+2/q) expression is not a defined
probability.  Without fixing (E) before the sampled point, the exact
kernel formula (10) need not describe the trial.  Most importantly, without
definitions of the screens and the grammar, the assertion that every legal
factor return requires a local return under (E) cannot be proved or even
checked for exhaustiveness.  Consequently, the transition from (14) to an
upper bound on the algorithm's total verified-factor probability is
missing.  Markov's inequality itself is correct, but it cannot close the
unstated algorithm class.

If the torus-interface sentences are instead taken as axioms about a
separately defined grammar, the obstruction after (14) is a valid
conditional consequence.  They cannot serve simultaneously as the
from-first-principles proof required by a self-contained statement-only
reconstruction.

## 7. Carry identities

Since

\[
X=Av-Nq_A,qquad gv=1+N\widetilde d,
\]

direct substitution gives

\[
{gX-A\over N}=A\widetilde d-gq_A.
\]

The calculation with (Y=Bv-Nq_B) is identical, proving (15) for any
signed or noncanonical (g) that is nonzero and invertible modulo (N).

Write (gX=A+Nk) and (gY=B+Nl).  The identity

\[
A^2-DB^2=(a^2-Db^2)^2=g^2
\]

then yields

\[
g^2(X^2-DY^2-1)
=2N(Ak-DBl)+N^2(k^2-Dl^2).
\]

Division by (Ng^2) proves (16).  The terms contain products and squares
of inverse-quotient-derived carries.  Nothing in the atom or residue union
bound for the linear bank controls these nonlinear transforms.

## Final assessment

All explicit number-theoretic and algebraic subclaims above pass the blind
reconstruction.  The advertised exclusion of every expected-QP Las Vegas
algorithm “confined to this grammar” fails the strict self-contained check
because the grammar and its exhaustive success events are absent.  The
overall verdict is therefore **FAIL** at the requested SHA.
