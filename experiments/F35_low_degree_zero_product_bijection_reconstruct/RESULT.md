# Proof-blind reconstruction: low-degree zero-product bijections

**Verdict: RECONSTRUCTED.**

The theorem package follows from CRT, univariate root counting, and finite-set
bijectivity.  The algorithmic consequence is conditional on explicit uniformity
and circuit-access promises stated below.  There is one important quantifier
qualification: for repeated runs to have expected polynomial cost, the asserted
TV bound must stay below (1/2) by a fixed constant or, more generally, by an
inverse polynomial.  A merely pointwise assertion (delta_N<1/2), with no
uniform lower bound on (1/2-delta_N), is insufficient.

This reconstruction uses no classification theorem for scheme automorphisms.

## 1. Setup and CRT factorization

Let

\[
N=pq,qquad R=\mathbb Z/N\mathbb Z,qquad
\Omega_N=\{(k,x)\in R^2:kx=0\},
\]

where (p\ne q) are primes.  For a prime (r), write

\[
\Omega_r=\{(u,v)\in\mathbb F_r^2:uv=0\}
          =L_{K,r}\cup L_{X,r},
\]

where (L_{K,r}=\{(t,0):t\in\mathbb F_r\}) and
(L_{X,r}=\{(0,t):t\in\mathbb F_r\}).

CRT gives

\[
R^2\simeq \mathbb F_p^2\times\mathbb F_q^2,
\qquad
\Omega_N\simeq\Omega_p\times\Omega_q.
\]

Indeed, (kx=0\pmod N) is equivalent to its two reductions being zero
modulo (p) and modulo (q).

Let (T=(F,G)), where (F,G\in R[K,X]) are the exact formal outputs and
have total degree at most (D).  Reducing their coefficients modulo (r)
defines

\[
T_r=(F_r,G_r):\mathbb F_r^2\longrightarrow\mathbb F_r^2.
\]

Under CRT, the restriction of (T) to (Omega_N) is exactly the product
map (T_p\times T_q).  If (T) maps (Omega_N) into itself, then each
(T_r) maps (Omega_r) into itself: pair an arbitrary point of
(Omega_r) with any point of the other local cross and lift by CRT.  If
(T_p\times T_q) is bijective, each factor is bijective.  For injectivity,
hold the other local input fixed; for surjectivity, prescribe an arbitrary
other local target and use global surjectivity.  Thus a global bijection
(T:\Omega_N\to\Omega_N) induces bijections

\[
T_p:\Omega_p\to\Omega_p,
\qquad
T_q:\Omega_q\to\Omega_q.
\]

No assumption about an inverse polynomial is used here.

## 2. The local axis lemma

Fix a prime (r) for which (2D<r).  On the (K)-axis put

\[
a(t)=F_r(t,0),\qquad b(t)=G_r(t,0).
\]

Both have degree at most (D).  Since (T_r(t,0)\in\Omega_r),

\[
a(t)b(t)=0\qquad\text{for every }t\in\mathbb F_r.
\]

The formal polynomial (ab\in\mathbb F_r[t]) has degree at most (2D<r)
and has all (r) field elements as roots.  Hence (ab=0) as a formal
polynomial.  Since (mathbb F_r[t]) is an integral domain, either (a=0)
or (b=0).  They cannot both vanish: otherwise the (r\ge2) points of the
source axis would all map to the origin, contradicting injectivity.
Consequently the whole source (K)-axis maps into exactly one target axis.
The same argument, applied to (F_r(0,t)G_r(0,t)), handles the source
(X)-axis.

The two source axes cannot both map into the same target axis.  Their union
is all of (Omega_r), so the image would miss every nonorigin point of the
other target axis, contradicting surjectivity.  Therefore precisely one of
the following holds:

\[
\begin{array}{c|cc}
&L_{K,r}&L_{X,r}\\ \hline
\text{preserved}&L_{K,r}&L_{X,r}\\
\text{swapped}&L_{X,r}&L_{K,r}.
\end{array}
\]

The common source origin lies on both source axes, so its image lies on both
of the two distinct target axes.  Thus

\[
T_r(0,0)=(0,0).
\]

Finally, the restriction from a source axis into its assigned target axis is
injective between two sets of size (r), hence is a bijection.  In
particular, its active coordinate sends nonzero field elements to nonzero
field elements.

This proof uses neither division by (2) nor a distinction between (t) and
(-t).  It therefore includes characteristic (2).  More concretely, if
(r=2), then (2D<2) forces (D=0); a constant polynomial map cannot be a
bijection of the three-point set (Omega_2).  Thus the hypotheses are
inconsistent in that edge case, rather than hiding an exceptional map.

Applying this lemma at (p) and (q) proves the claimed local conclusion
whenever (2D<\min(p,q)).

## 3. Mixed local orientations expose a factor

Consider the four restrictions in (R[Z]):

\[
A(Z)=F(Z,0),\quad B(Z)=G(Z,0),\quad
C(Z)=F(0,Z),\quad E(Z)=G(0,Z).
\]

At a local prime (r), preservation means

\[
B_r=0,quad C_r=0,quad A_r\ne0,quad E_r\ne0,
\]

while swapping means

\[
A_r=0,quad E_r=0,quad B_r\ne0,quad C_r\ne0.
\]

The nonzero assertions are formal, not merely pointwise: each active
coordinate is a bijection of an axis, so it is not the zero function and
therefore not the zero polynomial.

Suppose, for example, that (T_p) preserves and (T_q) swaps.  Then
(A_p\ne0) while (A_q=0).  Choose a coefficient (c\in R) of (A) whose
reduction modulo (p) is nonzero.  Every coefficient of (A) is zero
modulo (q), so, for the canonical integer representative of (c),

\[
q\mid c,qquad p\nmid c,qquad \gcd(c,N)=q.
\]

This is a proper factor.  If the orientations are reversed, the same
argument gives a coefficient with gcd (p).  In fact, under mixed
orientations each of the four displayed restrictions has some coefficient
which is zero at exactly one CRT prime, although one restriction is enough.

It follows contrapositively that if scanning all coefficients of these four
restrictions produces no proper gcd with (N), then the (p)- and
(q)-orientations agree.

Define the disjoint union

\[
\mathcal A_N=
(R^\times\times\{0\})\;\dot\cup\;
(\{0\}\times R^\times)\;\dot\cup\;
\{(0,0)\}.
\]

When the local orientations agree, (T) preserves (mathcal A_N) setwise.
For instance, if (u\in R^\times), then both reductions (u_p,u_q) are
nonzero.  Under two preserving local maps, ((u,0)) acquires a nonzero
(K)-coordinate at both primes and zero (X)-coordinate, hence maps to
((u',0)) with (u'\in R^\times).  Under two swapping maps it maps to
((0,u')) with (u'\in R^\times).  The same reasoning applies to the other
axis, and the origin is fixed.  Thus the two unit axes are either preserved
or exchanged.  Since (T) is injective and (mathcal A_N) is finite, the
inclusion (T(\mathcal A_N)\subseteq\mathcal A_N) is equality.

## 4. Explicit mixed-orientation witness

Let (e_p,e_q\in R) be the complementary CRT idempotents

\[
e_p\equiv1\pmod p, e_p\equiv0\pmod q,qquad
e_q\equiv0\pmod p, e_q\equiv1\pmod q.
\]

Thus

\[
e_p^2=e_p,quad e_q^2=e_q,quad e_pe_q=0,quad e_p+e_q=1.
\]

Define the degree-one map

\[
F(K,X)=e_pK+e_qX,qquad
G(K,X)=e_pX+e_qK.
\]

It preserves the zero-product locus because

\[
FG=(e_p+e_q)KX=KX.
\]

It is an involution:

\[
e_pF+e_qG=K,qquad e_pG+e_qF=X.
\]

Modulo (p) it is the identity, while modulo (q) it swaps (K) and (X).
Its restrictions are

\[
F(K,0)=e_pK,quad G(K,0)=e_qK,quad
F(0,X)=e_qX,quad G(0,X)=e_pX.
\]

Moreover (gcd(e_p,N)=q) and (gcd(e_q,N)=p).  This witness confirms both
that mixed orientations really occur and that their visible coefficients
necessarily disclose the CRT split.  It is not a counterexample to the
coefficient conclusion.

## 5. Extracting restrictions from a division-free circuit

Let a fully explicit straight-line circuit over (R), with inputs (K,X)
and gates (+,-,\times), have (g) gates and total encoding length (L).
Suppose its exact formal outputs are (F,G\in R[K,X]) of total degree at most
(D).  Work in

\[
S_D=R[Z]/(Z^{D+1}).
\]

Evaluate the circuit twice, first at ((K,X)=(Z,0)) in (S_D), then at
((K,X)=(0,Z)).  A polynomial is represented by its (D+1) coefficients.
Addition and subtraction use (O(D)) ring operations; naive truncated
convolution uses (O(D^2)).  Therefore the two evaluations together use

\[
O(gD^2)
\]

ring operations in (R), with only a constant factor for the second pass.
They return exactly

\[
F(Z,0),\ G(Z,0),\ F(0,Z),\ G(0,Z).
\]

The justification remains valid when intermediate gates have enormous
formal degree and the low-degree final answer is obtained by cancellations.
Substitution followed by reduction modulo (Z^{D+1}) is a ring
homomorphism.  Interpreting every gate in the quotient therefore gives the
image of the exact polynomial computed at that gate.  Since the final
restrictions have degree at most (D), their images in the quotient retain
all their coefficients.  No discarded high-degree term can later contribute
to a low degree through (+,-,\times); the homomorphism argument is the
formal reason.

The encoding length matters for bit complexity and access: (g=O(L)) in a
standard explicit gate encoding, constants can be reduced modulo (N) in
time linear in their encoded length times a polynomial in (n), and all
stored coefficients thereafter have (O(n)) bits.  The procedure does **not**
certify either promise.  It cannot tell whether invisible higher-degree final
terms existed, and it does not test that the induced map is a bijection of
(Omega_N).  Exact output degree and global bijectivity are semantic
promises defining the eligible class.

## 6. Uniform adaptive monitoring

For the algorithmic statement, the necessary uniform model is as follows.
Let

\[
n=\lceil\log_2(N+1)\rceil.
\]

There are fixed polynomials (P,Q), independent of (N), its unknown
factors, the random tape, the history, and the step.  A public numeric bound
(D_N\le P(n)) is fixed before a run.  Every realized transition first
materializes an explicit division-free circuit whose exact outputs have
degree at most (D_N) and whose map is, on the whole of (Omega_N), a
bijection.  If the realized circuit encodings have lengths (L_1,L_2,\ldots),
then

\[
\mathbb E\!\left[\sum_i L_i\right]\le Q(n).
\]

The underlying run is almost surely finite and has expected polynomial base
cost.  These are uniform promises, not facts inferred separately after each
random execution.

Before running, scan the integers (a=2,3,\ldots,2D_N), computing
(d=\gcd(a,N)).  A proper gcd is a factor.  If none is found, neither (p)
nor (q) is at most (2D_N), because the scan would encounter that prime
itself.  Hence

\[
2D_i\le2D_N<\min(p,q)
\]

for every realized branch circuit.  This supplies the strict root-counting
condition without knowing (p) or (q).  The scan has polynomial bit cost
because (D_N\le P(n)).

For every materialized circuit, evaluate both axis substitutions in
(R[Z]/(Z^{D_N+1})) and take gcds of the at most (4(D_N+1)) resulting
coefficients with (N).  Let (S=\sum_iL_i).  A standard explicit encoding
has (sum_i g_i=O(S)) and at most (O(S)) circuits.  Using ordinary
polynomial-time modular arithmetic and gcd, the monitor's realized overhead
is bounded by

\[
\operatorname{poly}(n)\bigl(D_N+S D_N^2\bigr).
\]

Consequently its expectation is at most

\[
\operatorname{poly}(n)\bigl(P(n)+Q(n)P(n)^2\bigr),
\]

which is polynomial.  This linear dependence on the realized encoding
length is why an expectation bound on total length suffices; no worst-case
bound on the number of realized steps is needed.

Adaptive, state-dependent selection is allowed in a precise pathwise sense.
After the selector's randomness and history choose a branch, that branch must
materialize one deterministic circuit which itself defines a global
bijection of (Omega_N).  The effective rule

\[
z\longmapsto T_{C(z)}(z)
\]

may be a stitched piecewise map and need not itself be polynomial or
bijective.  The proof never applies the theorem to that stitched rule; it
applies it to the selected global map (T_{C(z)}), and hence obtains the
invariant one step at a time.  In contrast, it is not enough that a stitched
map is globally bijective if its individual branch circuits are not.
Likewise, random selection among materialized qualifying bijections is
covered, while an opaque stochastic kernel is not.

## 7. The pathwise event and the TV bound

Let a run start at (Z_0=(k_0,x_0)\in\Omega_N), make only the transitions
just described, terminate almost surely, and output its final current state
(Y\in\Omega_N).  Define (H) to be the event that a proper gcd with (N)
is found either

1. from one of the two initializer coordinates (k_0,x_0), or
2. from a coefficient of one of the four axis restrictions of any circuit
   materialized along the realized run.

The deterministic trial scan is logically prior: if it finds a factor the
algorithm is already done; below assume that it certified the degree
condition.

For a point of (Omega_N), absence of a proper gcd in both coordinates means
that each coordinate is either zero modulo (N) or a unit.  Their product is
zero, so they cannot both be units.  Therefore

\[
Z_0\notin\mathcal A_N
\quad\Longrightarrow\quad
\text{an initializer coordinate has a proper gcd with }N.
\]

On (H^c), the initializer is consequently in (mathcal A_N).  Also, every
realized circuit has no factor-bearing restriction coefficient, so its two
local orientations synchronize and it preserves (mathcal A_N).  Induction
over the finite realized transcript gives (Y\in\mathcal A_N).  Thus,
pathwise up to the null event of nontermination,

\[
\boxed{\{Y\in\mathcal B_N\}\subseteq H},
\qquad
\mathcal B_N:=\Omega_N\setminus\mathcal A_N.
\]

Let (mu) be the **unconditional** terminal law of the original run.  For
this statement the monitor is coupled to the full original transcript but
does not stop or condition that run; otherwise its terminal law could change.
Let (pi_N) be uniform on (Omega_N).  Since

\[
|\Omega_r|=2r-1,
\]

CRT gives

\[
|\Omega_N|=(2p-1)(2q-1).
\]

Moreover

\[
|\mathcal A_N|=2|R^\times|+1
=2(p-1)(q-1)+1,
\]

and therefore

\[
|\mathcal B_N|=(2p-1)(2q-1)-\bigl(2(p-1)(q-1)+1\bigr)
=2pq-2=2N-2.
\]

Hence

\[
\rho_N:=\pi_N(\mathcal B_N)
=\frac{2N-2}{(2p-1)(2q-1)}.
\]

It is strictly larger than (1/2), since

\[
2(2pq-2)-(2p-1)(2q-1)=2p+2q-5>0.
\]

Using (d_{\rm TV}(\mu,\pi)=\sup_E|\mu(E)-\pi(E)|), the pathwise inclusion
and the event (E=\mathcal B_N) give

\[
\boxed{
\Pr(H)\ge\mu(\mathcal B_N)
\ge\rho_N-d_{\rm TV}(\mu,\pi_N).
}
\]

There is no contradiction in an accurate sampler: it may reveal a factor in
its initializer or in a circuit coefficient.  The mixed-idempotent witness
shows exactly how this can happen.  Conversely, if the run is factor-free in
the precise sense (Pr(H)=0), then (mu(\mathcal B_N)=0), and

\[
d_{\rm TV}(\mu,\pi_N)\ge\rho_N>\tfrac12.
\]

## 8. Fresh repetition and the stopped-cost calculation

Assume fresh independent runs can be generated with the same promises and
expected polynomial full-run cost (M(n)), including monitoring.  Suppose

\[
d_{\rm TV}(\mu,\pi_N)\le\delta.
\]

If (delta<1/2) is one fixed constant, then every run exposes a proper factor
with probability

\[
s_N:=\Pr(H)\ge\rho_N-\delta>\tfrac12-\delta=:\varepsilon>0.
\]

More generally, the same conclusion is expected-polynomial when a uniform
bound (\varepsilon(n):=1/2-delta(n)\ge1/\operatorname{poly}(n)) is given.

Repeat fresh runs and stop at the first detected proper gcd.  Every returned
answer is correct by direct gcd verification, and independent repetition
terminates almost surely.  To bound cost without assuming that successful
runs and cheap runs are independent, couple each attempted run to its full
counterfactual cost (C_i), even though the real monitor may stop it early.
Let (\tau) be the first run whose full transcript has event (H_i).  Then

\[
\begin{aligned}
\mathbb E\!\left[\sum_{i=1}^{\tau}C_i\right]
&=\sum_{i\ge1}\mathbb E[\mathbf1_{\{\tau\ge i\}}C_i]\\
&=\sum_{i\ge1}(1-s_N)^{i-1}\mathbb E[C_i]\\
&=\frac{M(n)}{s_N}.
\end{aligned}
\]

The second equality is valid because ({\tau\ge i\}) depends only on the
previous fresh runs and is independent of the entire (i)-th run.  The
actual stopped cost is no larger.  Thus the procedure is Las Vegas and has
expected polynomial cost when (1/s_N) is polynomially bounded.

If all that is known is a separate inequality (delta_N<1/2) for each
(N), with (1/2-delta_N) possibly exponentially small, the displayed
argument gives no polynomial bound.  This is the exact quantifier gap hidden
by an unqualified phrase “(delta<1/2).”

This is only a splitter for inputs promised to be products of two distinct
primes.  On such an input a proper gcd is one of the two prime factors.  The
argument supplies neither termination nor a success bound on primes, prime
powers, nonsquarefree integers, or arbitrary composites, so it does not by
itself imply complete all-input integer factorization.

## 9. Boundary of the result and counterexample checks

The proof has the following exact scope.

- **Characteristic-scale or high degree.**  The implication from pointwise
  vanishing to formal vanishing fails once the degree reaches the field
  scale; (Z^r-Z) is the standard witness.  There are also actual split-axis
  bijections at high degree.  For (r\ge3), fix (a\in\mathbb F_r^\times)
  and put (delta_a(t)=1-(t-a)^{r-1}), the indicator of (t=a) on
  (mathbb F_r).  On (Omega_r), the degree-((r-1)) formulas

  \[
  F(k,x)=k-a\delta_a(k)+a\delta_a(x),\qquad
  G(k,x)=x+a\delta_a(k)-a\delta_a(x)
  \]

  transpose ((a,0)) and ((0,a)) and fix every other point.  Thus a source
  axis need not go wholly to one target axis after the low-degree hypothesis
  is removed.

- **Noninvertible and stochastic moves.**  A noninvertible transition or a
  stochastic kernel need not preserve the invariant.  Randomness is covered
  only when each realized move materializes a deterministic qualifying
  global bijection.

- **Auxiliary or lifted kernels.**  A bijection on a larger state space whose
  projection is a transition on (Omega_N) is not a polynomial bijection of
  (Omega_N).  The local-axis theorem cannot be applied to that projection
  without a new argument.

- **Rational, division, or opaque circuits.**  The quotient-ring evaluator
  relies on the functoriality of (+,-,\times).  Division can be undefined at
  zero divisors and can invalidate the truncation reasoning; an opaque call
  does not expose formal restriction coefficients.  Such representations
  are outside the extraction claim.

- **Piecewise branches.**  A state-dependent choice among circuits is safe
  only when every selected circuit is itself a global bijection.  It is not
  enough for a piecewise stitching of non-bijective branch circuits to happen
  to be a bijection.  For example, the identity on a finite set can be
  stitched from one constant circuit per current point, although none of
  those constant circuits is globally bijective.

- **Warm starts.**  A starting point in (mathcal B_N) already has a
  nonzero zero-divisor coordinate and hence already factors (N) by a gcd.
  Therefore a warm-start procedure with useful mass in (mathcal B_N) is
  not a free factor-independent resource; its own construction and cost must
  be counted.  If it avoids every such gcd, it starts in (mathcal A_N).

- **Prime powers and nonsquarefree bases.**  The proof uses
  (R\simeq\mathbb F_p\times\mathbb F_q), integral-domain root counting in
  both components, and the two-orientation dichotomy.  These statements do
  not apply to (mathbb Z/p^e\mathbb Z) or general nonsquarefree (N).

- **Uniformity and termination.**  A separate finite degree bound for each
  realized history, a polynomial depending on the history, or an expected
  degree bound does not give the public trial scan or the overhead bound.
  Likewise the law used above must be the unconditional law of an
  almost-surely finite run, not a law conditioned on avoiding (H).

Finally, the semantic hypothesis here is much weaker than being an
automorphism of the affine scheme cut out by (KX).  A scheme automorphism
requires an invertible coordinate-ring map and algebraic preservation over
all base algebras.  Here one assumes only a polynomial-induced bijection of
the finite set of (R)-points and pointwise zero-product preservation there,
plus a degree bound.  Conversely, a polynomial map can permute these finite
points without possessing a polynomial inverse in the coordinate ring.
Accordingly, no classification or property of scheme automorphisms is needed
or implied beyond what follows directly from the theorem's stated
hypotheses.
