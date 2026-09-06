# F285 — Differentiated matrix powers collapse to one Lucas scalar

Status: author-derived candidate theorem with exact finite checks. No independent
blind reconstruction has run. This is not an all-input factoring algorithm.

## Question and prior difference

Can the efficiently computed Fréchet derivative of the map `A -> A^N` on the
rank-four algebra `M_2(Z/N)` reveal a local rank difference caused by the
split/nonsplit type of `A`? The public exponent has zero derivative on scalar
directions in both local characteristics. Noncommuting directions might retain
different information. This question was proposed before retrieving prior bodies.

The operator is

\[
L_A(H)=\sum_{i=0}^{N-1} A^i H A^{N-1-i}.
\]

Binary matrix powering with a tangent propagated by the product rule computes
the entire four-by-four matrix of this operator with `O(log N)` fixed-size
modular matrix operations. This does not assume a characteristic-specific
Frobenius map, an order oracle, or a factoring oracle.

Closest priors retrieved with the Rust reader: `route:F03`, `route:F05`,
`route:F08`, `route:F10`, P06, P09, P132, and P55. P06/P09 show failures of
specific global-N Frobenius substitutions. P132 treats fresh uniform nonunits,
generic Krylov probes, monomial maps, and short Hasse jets. The present operator
is a structured noncommutative derivative whose entries can be computed without
expanding N terms. The new calculation identifies the entire operator, its exact
rank law, and a repeated-root branch; it does not merely invoke sparse random
sampling. P55 concerns quadratic norm-one tori and signed factor-gap relations.
The resulting Lucas scalar connects this attempt to the same elementary
quadratic multiplicative structure, but is not the P55 gap decoder.

The prescribed existing-paper cache `.knowledge/INDEX.md` is absent. No external
source is used in the proof below. The root confirmed that focused primary-source
retrieval would be allowed if needed. No literature novelty claim is made.

## Exact operator identity

Let N be odd and R=Z/N. Put t=tr(A), d=det(A), Delta=t^2-4d, and suppose
Delta is a unit. Define B=2A-tI. Cayley-Hamilton gives B^2=Delta I. Conjugation

\[
C(H)=BHB/\Delta
\]

is an involution. Its negative projector is

\[
P_-(H)=\frac12(H-BHB/\Delta).
\]

Let u_m,v_m be the uniquely specified recurrence coefficients obtained by
reducing X^m modulo X^2-tX+d, so A^m=u_m A+v_m I. Then

\[
\boxed{L_A=u_N P_-.}
\tag{1}
\]

Proof: on the positive summand H commutes with A, and L_A(H)=N A^{N-1}H=0.
On the negative summand BH=-HB, hence HA=(tI-A)H. Set Abar=tI-A. The sum
in L becomes S H, where S=sum_i A^i Abar^{N-1-i}. Since A-Abar=B is a
unit, telescoping gives S=(A^N-Abar^N)/B=u_N I. This proves (1) over R
without choosing eigenvectors or dividing by an unknown factor.

Over each odd prime field where Delta is nonzero, P_- has rank two: after
extension to the splitting field of A it keeps exactly the two off-diagonal
matrix units. Thus the local rank of L is zero or two according as u_N is
zero or nonzero. The coefficient ideal of the whole operator is exactly (u_N):
one inclusion follows from (1), and the converse follows from
tr(L)=2u_N. Indeed tr(C)=tr(B)tr(B)/Delta=0, so tr(P_-)=2.
Consequently

\[
\gcd(N,\text{all 16 entries of }L_A)=\gcd(N,u_N).
\]

This identity does not claim that every individual entry has the same gcd.
An entry or a selected projection can have additional zeros from P_-. The
result identifies the invariant rank profile and common coefficient content.

## Exact semiprime rank law and probability

Suppose N=pq with distinct odd primes p<q. Work at a local prime r with other
prime s. Write alpha,beta for the distinct roots of the characteristic
polynomial in a splitting field. Then

\[
u_N=\frac{\alpha^N-\beta^N}{\alpha-\beta}.
\]

If either root is zero, u_N is nonzero. Otherwise rho=alpha/beta satisfies
rho^N=1 exactly when rho^s=1, since r-th powering is a field automorphism.
For split polynomials rho belongs to F_r^* (order r-1). For irreducible
quadratics, beta=alpha^r, so rho belongs to the norm-one subgroup (order r+1).
In either case rho is not 1. Since s is prime, the necessary and sufficient
condition for a zero is that rho have order s.

At r=p, the other prime q is greater than p+1, so no such ratio exists.
At r=q, a zero exists precisely when p divides q-1 or q+1. For any A with
unit discriminant, therefore,

\[
p\nmid(q^2-1)\quad\Longrightarrow\quad
\operatorname{rank}_{p}L_A=\operatorname{rank}_{q}L_A=2.
\tag{2}
\]

This is pointwise and does not assume that A is random. Different splitting
types alone are insufficient.

For the concrete sampler choose t,d independently uniformly modulo N and set
A=[[0,-d],[1,t]]. Condition on Delta being a unit. Local characteristic
polynomials are independent and uniform on their r(r-1) separable monic
quadratics. At q, if p divides q-1, ordered root pairs with ratio of order p
number (q-1)(p-1); division by two gives (q-1)(p-1)/2 polynomials.
If p divides q+1, the map alpha -> alpha/alpha^q from F_(q^2)^* onto the
norm-one group has fibers of size q-1. The p-1 ratios of order p similarly
give (q-1)(p-1)/2 irreducible polynomials after identifying conjugate roots.
The two divisibilities cannot both hold because p is odd. Therefore

\[
\boxed{\Pr(\text{rank mismatch}\mid\Delta\text{ unit})=
\begin{cases}(p-1)/(2q),&p\mid q^2-1,\\0,&p\nmid q^2-1.\end{cases}}
\tag{3}
\]

On a mismatch, gcd(u_N,N)=q, a verified proper divisor. The sampler also
has ordinary discriminant gcd opportunities before this conditioning.
Equation (3) is not a statement that all coordinate probes have zero chance.

## Nonseparable branch

The natural repeated-root degeneration does not repair this operator. Over an
odd local field with Delta=0, write A=lambda I+J, with J^2=0. Expanding with
one marked tangent H gives, for N>=3,

\[
L_A(H)=N\lambda^{N-1}H+
\binom N2\lambda^{N-2}(JH+HJ)+
\binom N3\lambda^{N-3}JHJ.
\tag{4}
\]

For a prime r>3 dividing N, all three integer coefficients vanish modulo r.
Hence L_A is zero at every such repeated-root component. If p,q>3 and
gcd(Delta,N)=N, the ranks are both zero. If Delta vanishes at exactly one
component, its gcd already supplies a factor before using L. The primes 2
and 3 are detectable by constant-cost trial division.

Thus neither the separable split/nonsplit distinction nor an uninformative
double repeated-root degeneration provides an all-input rank separator in
this exact two-by-two differentiated-power family. This is not a statement
about other matrix functions, higher dimensions, high derivatives, or a
coordinate-sensitive decoder.

## Computation and cost

`pilot.py` is a single-process exact Python program with a five-second alarm.
Preflight estimate: less than five seconds and 30 MB. Observed preflight:
load 1.80/1.94/1.97, memory available 74%, no swap. Local `ps` was blocked by
the sandbox. The root supplied a fresh successful shared process snapshot:
one OS suggestd process at one core, Codex at 1.7%, other apps low, and no
active numerical research process. The root authorized the pilot on that
complete shared preflight. No heavy computation was started.

Run command:

```
python3 experiments/F285_finite_algebra_operator_search/pilot.py > experiments/F285_finite_algebra_operator_search/run.log
```

Artifacts: source `pilot.py`, exact counts `results.json`, stdout `run.log`.
Nine semiprimes were used as offline labels. Public matrix actions use only N
and the fixed random seed 285; local enumeration uses known factors only to
check the formulas. The final run verifies the predicted counts for every
separable quadratic at each labeled prime, checks (1) on all four tangent
basis matrices for 210 sampled matrices, and checks (4)'s zero consequence
for 112 repeated-root matrices. All assertions pass. The final exact elapsed
time and platform RSS are in the JSON; the run took less than 0.1 seconds and
less than 20 MB on this Mac. These are finite checks, not independent proof
verification and not asymptotic evidence.

The public operator/scalar uses O(n) fixed-size arithmetic steps on O(n)-bit
residues. With schoolbook arithmetic a conservative O(n^3) bit bound covers
one trial, including modular powering, gcds, and inverses. Sampling two uniform
residues uses O(n) expected random bits. Stored state is O(n) bits. Computing
the scalar directly is cheaper than materializing the full operator and has
the same invariant rank information.

## Remaining gap and restart point

The candidate proof needs fresh statement-only reconstruction before promotion.
Even if verified, it only settles this explicitly defined operator family.
It supplies no all-input success law. A useful next finite-algebra candidate
must exhibit a public computable operator whose rank is not just the collision
condition of two quadratic eigenvalues under the same exponent. Higher degree
or coordinate-sensitive constructions are open here; no claim is made that
they succeed or fail. No shared catalog, ledger, or Git commit was changed by
this worker.
