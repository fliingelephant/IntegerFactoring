# Hostile audit of F29: uniform full-lattice random codes

**Verdict: PASS WITH REQUIRED CORRECTIONS.**

The central probabilistic theorem is correct in its stated narrow model.  The
exact CRT identities, determinant, one-factor slices, deterministic
shortest-vector cutoff, incidence calculation, union bound, tie handling, and
the two asymptotic branches all survive hostile checking.  There is one
false/ambiguous summary claim that must be repaired before promotion: the
explicit cube-volume right-hand side in (0.1) is not itself uniformly
\(N^{-u/2+o(1)}\) in the fixed dimensions \(u<m<2u\).  The *event
probability* nevertheless has the claimed bound because in those dimensions
the relevant divided balls eventually contain no nonzero integer point.  The
candidate's Section 5 already uses this sharper discrete observation, so the
repair does not change the theorem.

No computation was used in this audit.

## Audited scope

I audited only the following statement.  Let \(N=pq\) for distinct balanced
primes, let \(C_p\le\mathbb F_p^m\) and
\(C_q\le\mathbb F_q^m\) be uniform \(u\)-subspaces, and put

\[
L=\{x\in\mathbb Z^m:x\bmod p\in C_p,
                         \ x\bmod q\in C_q\}.
\]

Here \(u\) and the balance and polynomial-dimension constants are fixed,
while \(u<m\le(\log N)^K\).  The conclusion concerns the existence of an
**exact shortest vector** whose coordinate gcd with \(N\) is \(p\) or \(q\).
It is not a conclusion about biased or dependent arithmetic codes, CVP, LLL,
nonshortest observables, nonlinear decoders, or arbitrary lattices
manufactured from \(N\).

## 1. Exact algebraic identities

All exact identities check.

1. Reduction modulo \(r\) has kernel \(r\mathbb Z^m\), and the preimage of a
   dimension-\(u\) subspace has index \(r^{m-u}\).  Coordinate CRT therefore
   gives
   \[
   L=L_p\cap L_q,
   \qquad [\mathbb Z^m:L]=p^{m-u}q^{m-u}=N^{m-u}.
   \]
   Thus \(\det L=N^{m-u}\).

2. If \(x=py\), the modulo-\(p\) constraint is automatic and multiplication
   by \(p\) is invertible modulo \(q\).  Hence
   \[
   L\cap p\mathbb Z^m=pL_q,
   \qquad L\cap q\mathbb Z^m=qL_p.
   \]
   Their intersection is \(N\mathbb Z^m\).

3. Because \(N\) is squarefree, a nonzero \(x\in L\) has proper coordinate
   gcd \(p\) exactly when \(x=py\), \(y\in L_q\), and
   \(y\notin q\mathbb Z^m\); the symmetric statement holds for \(q\).
   This exhausts the coordinate-gcd cases.  There is no missing class and no
   proxy substitution.

The equal local dimensions also do make \(C_p\times C_q\) a free rank-\(u\)
submodule over \(\mathbb Z/N\mathbb Z\), so the optional \(E+N\mathbb Z^m\)
description is consistent.  It is not used in the probability proof.

## 2. Incidence and finite event bound

For a uniform \(u\)-subspace \(C\le\mathbb F_r^m\), transitivity or direct
double counting gives, for each fixed nonzero \(z\),

\[
\Pr[z\in C]=\frac{r^u-1}{r^m-1}=\theta_r.
\]

Only a marginal law is used.  Independence of \(C_p,C_q\) is therefore not
silently invoked in either one-slice union bound.

The centered-cube argument gives

\[
Z_m(s)\le v_m(s+\sqrt m/2)^m.
\]

Minkowski, followed by a limiting enlargement of the open ball, gives

\[
\lambda_1(L)\le 2v_m^{-1/m}N^{1-u/m}=R_M.
\]

Also \(Ne_i\in L\), so every shortest vector has norm at most
\(R_0=\min(R_M,N)\).

For the \(p\)-slice, every eligible divided vector \(y\) has
\(0\ne y\bmod q\), hence costs exactly \(\theta_q\).  A union bound over the
eligible vectors, whose number is at most \(Z_m(R/p)\), proves

\[
\Pr(E_p(R))
 \le \theta_q Z_m(R/p)
 \le \theta_q v_m(R/p+\sqrt m/2)^m.
\]

The wording "enlarged ... to all integer points" must be understood as an
enlargement of the **number of eligible indices**, not as assigning
probability \(\theta_q\) to residue-zero points (whose incidence probability
is one).  With that interpretation the displayed inequality is valid.  For
maximum precision one may write the sharper intermediate count

\[
\theta_q\,\#\{y\in\mathbb Z^m:\|y\|\le R/p,
                                 \ y\bmod q\ne0\}.
\]

The symmetric argument proves the \(q\)-slice term.  Since every shortest
vector lies within \(R_0\), their union proves (0.1).  This event contains all
shortest-vector ties simultaneously, so no tie-breaking hypothesis is
hidden.

## 3. Minkowski-radius branch

When \(R_M\le N\), raising the branch inequality to the \(m\)-th power gives

\[
\frac{2^m}{v_m}\le N^u.
\]

Using \(v_m\le(2\pi e/m)^{m/2}\) implies
\(m\log m=O(\log N)\), uniformly on this branch.  Consequently
\(m=o(\log N)\) and \(2^m=N^{o(1)}\).

Without cube inflation, direct substitution is exact and gives

\[
\theta_qv_m(R_M/p)^m
=\frac{2^m}{p^u}
  \frac{q^{m-u}(q^u-1)}{q^m-1}
<\frac{2^m}{p^u},
\]

and symmetrically a bound below \(2^m/q^u\).

The discrete/inflation split is exhaustive and uniform because \(u\) is
fixed.

- If \(u<m<2u\), then
  \(R_M/p,R_M/q=O(p^{1-2u/m})=o(1)\).  Both are eventually below one, so
  there is no nonzero integer divided vector and both proper-slice events
  are empty.
- If \(m=2u\), the divided radii are bounded by constants depending only on
  \(u\) and the balance constant.  There are only constantly many divided
  vectors, while \(\theta_p,\theta_q=O(N^{-u/2})\).
- If \(m\ge2u+1\), balance gives both divided radii at least
  \(p^{c_u-o(1)}\), with for example any fixed
  \(c_u<1/(2u+1)\).  Since \(m\) is polylogarithmic,
  \(m(\sqrt m/2)/(R_M/p)\) and its \(q\)-analogue tend uniformly to zero.
  Thus each cube-inflation multiplier is \(1+o(1)\).

Together with \(p,q=N^{1/2+o(1)}\), these cases prove an upper bound
\(N^{-u/2+o(1)}\) for the actual event on this branch.

## 4. Public-\(N\)-radius branch

When \(R_M>N\), the exact finite bound and
\(\theta_q\le2q^{u-m}\) give

\[
\Pr(E_p(N))\le2v_mq^u(1+\sqrt m/(2q))^m,
\]

and symmetrically \(2v_mp^u\) times its inflation factor.  Since
\(m\le(\log N)^K\) and \(p,q=\Theta(\sqrt N)\), both inflation factors are
uniformly \(1+o(1)\).

The branch inequality is

\[
v_mN^u<2^m.
\]

For \(m<\log N/\sqrt{\log\log N}\), uniformly
\(m=o(\log N)\), so the preceding display converts the two bounds to
\(2^{m+1}/p^u\) and \(2^{m+1}/q^u\), both
\(N^{-u/2+o(1)}\).  Above that split,

\[
\log v_m\le-\tfrac12m\log m+O(m)=-\omega(\log N),
\]

and multiplying by \(p^u\) or \(q^u\) still leaves a bound smaller than
every fixed power of \(N^{-1}\).  The split covers every permitted \(m\)
uniformly, including dimensions growing as any fixed power of \(\log N\).

## 5. Required correction

The sentence following (0.1) says that "the bound" is
\(N^{-u/2+o(1)}\).  If "the bound" denotes the boxed right-hand side, this
is false when \(u<m<2u\).  In such a fixed dimension,
\(R_0/p,R_0/q=o(1)\), but the cube relaxation retains its origin cube.  For
example, the first boxed term behaves as

\[
\theta_qv_m(\sqrt m/2+o(1))^m
=N^{-(m-u)/2+o(1)},
\]

which is larger than \(N^{-u/2+o(1)}\) because \(m-u<u\).  The actual event
is zero, as the candidate correctly observes later; the loose volume RHS is
not.

Before promotion, make both of these changes:

1. Replace the Outcome claim by the unambiguous statement
   \[
   \Pr(\exists\text{ proper-gcd shortest vector})
   \le N^{-u/2+o(1)},
   \]
   and do not identify this asymptotic estimate with the literal RHS of
   (0.1).
2. In Section 4 or at the start of Section 5, explicitly record the sharper
   eligible-point union bound above (or simply \(\theta_r(Z_m(s)-1)\)) and
   say that the \(u<m<2u\) case uses its exact zero count rather than the
   cube-volume relaxation.

This is a required logical clarification, not a repair to the main event
theorem.  The proof already contains the necessary discrete argument.

## 6. Scope and final assessment

After that correction, the following narrow conclusion is supported:

> For independent uniform local \(u\)-subspaces with fixed \(u\), balanced
> distinct semiprimes, and \(u<m\le(\log N)^K\), the probability that any
> exact shortest vector of the full CRT Construction-A lattice has proper
> coordinate gcd is at most \(N^{-u/2+o(1)}\), uniformly in \(m\).

This includes all exact-shortest-vector multiplicities and ties.  It does
not support any transfer to biased/dependent arithmetic subspaces, affine
targets, CVP, LLL, nonlinear combinations, nonshortest vectors, or another
observable of the full lattice.  Those exclusions in the candidate are
correct and must remain explicit.
