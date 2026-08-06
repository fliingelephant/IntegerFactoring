# Fresh hostile re-audit of corrected F29

**Verdict: CLEAN PASS.**

The corrected candidate supports its stated narrow theorem.  The Outcome now
distinguishes the literal cube-volume right-hand side of (0.1) from the
probability estimate (0.2) for the actual proper-gcd shortest-vector event.
The sharper eligible-point union bound (4.4) is stated before the volume
relaxation and is used explicitly in the fixed-dimensional range
\(u<m<2u\).  The correction requested by the first hostile audit is therefore
complete.

I rechecked the exact lattice identities, the probability model, both
asymptotic branches, all shortest-vector ties, and every displayed-equation
reference.  I found no new defect and did not transfer the result beyond the
candidate's explicit scope.  No computation was used.

## Audited theorem and scope

The theorem being audited is only the following.  Let \(N=pq\), where
\(p\ne q\) are balanced primes, and let \(C_p\) and \(C_q\) be uniform
\(u\)-dimensional subspaces of \(\mathbb F_p^m\) and
\(\mathbb F_q^m\).  Here \(u\), the balance constant, and the
polynomial-dimension exponent are fixed, while

\[
u<m\le (\log N)^K.
\]

For the full CRT Construction-A lattice

\[
L=\{x\in\mathbb Z^m:x\bmod p\in C_p,
                         \ x\bmod q\in C_q\},
\]

the probability that **some exact shortest vector** has coordinate gcd
\(p\) or \(q\) is at most \(N^{-u/2+o(1)}\), uniformly in the allowed
dimension.  The statement is not about biased arithmetic subspaces, CVP,
LLL, nonshortest vectors, nonlinear decoding, or a different full-lattice
observable.

## 1. Exact algebra and deterministic radius

The algebraic part remains correct.

- The local preimage has index \(r^{m-u}\), coordinate CRT gives
  \(L=L_p\cap L_q\), and hence
  \(\det L=N^{m-u}\).
- If \(x=py\), the modulo-\(p\) constraint is automatic and multiplication
  by \(p\) is invertible modulo \(q\).  Thus
  \(L\cap p\mathbb Z^m=pL_q\), and symmetrically
  \(L\cap q\mathbb Z^m=qL_p\).
- For nonzero \(x\), squarefreeness makes these two punctured slices exactly
  the vectors with coordinate gcd \(p\) or \(q\).  Their intersection is
  \(N\mathbb Z^m\), the coordinate-gcd-\(N\) case.

Minkowski and the public vectors \(Ne_i\) give the deterministic cutoff

\[
\lambda_1(L)\le R_0
=\min\!\left(2v_m^{-1/m}N^{1-u/m},N\right).
\]

Consequently, union-bounding every proper-gcd vector of norm at most \(R_0\)
really does cover every shortest vector simultaneously, including all ties.

## 2. Corrected eligible-point bound

For each fixed nonzero residue \(z\in\mathbb F_r^m\), a uniform
\(u\)-subspace contains \(z\) with probability

\[
\theta_r=\frac{r^u-1}{r^m-1}.
\]

If a vector of coordinate gcd \(p\) is written as \(x=py\), eligibility is
exactly

\[
\|y\|_2\le R/p,
\qquad y\bmod q\ne0.
\]

The modulo-\(p\) condition is automatic, while the remaining random event is
\(y\bmod q\in C_q\), with probability \(\theta_q\).  Thus the candidate's
corrected equation (4.4),

\[
\Pr(E_p(R))
\le \theta_q
\#\{y\in\mathbb Z^m:\|y\|_2\le R/p,\ y\bmod q\ne0\},
\]

is the proper union bound.  Only the **number of eligible indices** is then
enlarged to all integer points before applying the centered-cube estimate.
No incidence probability is incorrectly assigned to residue-zero points.
The symmetric \(q\)-slice statement is identical.  Equations (4.5)--(4.6)
therefore prove the finite cube-volume bound (0.1).

The Outcome now accurately says that this cube-volume right-hand side is
deliberately loose for \(u<m<2u\), and separately states (0.2) for the
actual event.  It no longer makes the conflation identified in the first
audit.

## 3. Minkowski-radius branch

Suppose \(R_M\le N\).  Raising that inequality to the \(m\)-th power gives

\[
\frac{2^m}{v_m}\le N^u.
\]

Together with
\(v_m\le(2\pi e/m)^{m/2}\), this implies
\(m\log m=O(\log N)\), hence \(m=o(\log N)\) and
\(2^m=N^{o(1)}\).  Before cube inflation, direct substitution gives

\[
\theta_qv_m(R_M/p)^m
=\frac{2^m}{p^u}
  \frac{q^{m-u}(q^u-1)}{q^m-1}
<\frac{2^m}{p^u},
\]

with the symmetric bound below \(2^m/q^u\).  The candidate's three-way
handling of the inflation is correct and exhaustive:

1. If \(u<m<2u\), balance gives
   \(R_M/p,R_M/q=O(p^{1-2u/m})=o(1)\).  Eventually both divided balls have
   radius below one, so the eligible-point sets in (4.4) are empty.  This is
   the exact discrete argument required by the first audit; the loose
   cube-volume bound is not used.
2. If \(m=2u\), both divided radii are bounded by constants.  There are
   only constantly many eligible integer points, while
   \(\theta_p,\theta_q=O(N^{-u/2})\).
3. If \(m\ge2u+1\), balance gives both divided radii at least
   \(p^{c_u-o(1)}\) for a fixed \(c_u>0\).  Since \(m\) is
   polylogarithmic, \(m(\sqrt m/2)/(R_M/p)\) and its symmetric analogue
   tend to zero.  Each cube-inflation multiplier is therefore \(1+o(1)\).

Since balanced primes satisfy \(p,q=N^{1/2+o(1)}\), all three cases give
the event estimate \(N^{-u/2+o(1)}\) uniformly on this branch.

## 4. Public-\(N\)-radius branch

Suppose \(R_M>N\).  Then \(R_0=N\), and the finite bound gives

\[
\Pr(E_p(N))\le2v_mq^u
   \left(1+\frac{\sqrt m}{2q}\right)^m,
\]

plus the symmetric \(2v_mp^u\) term.  The inflation factors are uniformly
\(1+o(1)\), because \(m\) is polylogarithmic whereas
\(p,q=\Theta(\sqrt N)\).

The branch inequality is \(v_mN^u<2^m\).  Below
\(\log N/\sqrt{\log\log N}\), one has \(m=o(\log N)\), so it changes the
two bounds into at most

\[
\frac{2^{m+1}}{p^u}(1+o(1)),
\qquad
\frac{2^{m+1}}{q^u}(1+o(1)),
\]

which are \(N^{-u/2+o(1)}\).  At and above that split,

\[
\log v_m\le-\tfrac12m\log m+O(m)=-\omega(\log N),
\]

so multiplying by \(p^u\) or \(q^u\) still gives a probability smaller
than every fixed negative power of \(N\).  The two ranges cover every
allowed dimension and support the claimed uniform estimate.

## 5. References, ties, and final assessment

All internal equation references remain correct after the repair:
(2.4) is the coordinate-gcd classification, (3.1) the incidence formula,
(4.1) the lattice-point volume estimate, (4.4) the eligible-point union
bound, (4.5)--(4.6) the relaxed finite bounds, (5.2)--(5.5) the
Minkowski-branch estimates, and (5.7)--(5.10) the public-radius estimates.
Equations (5.6) and (0.2) now refer to the actual event probability, as they
must.

The proof never selects one shortest vector, so multiplicity and arbitrary
tie-breaking introduce no gap.  It also does not claim a polynomial-time
SVP algorithm or extrapolate from uniform local subspaces to an arithmetic
source.  The explicit reopen conditions preserve those limitations.

The corrected F29 candidate is ready for proof-blind reconstruction within
this exact scope.
