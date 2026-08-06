# Fresh hostile re-audit of amended F41: metric ACD decoder boundary

**Artifact audited:**
`experiments/F41_metric_acd_decoder_kill/RESULT.md`

**Preserved failed audit checked:**
`experiments/F41_metric_acd_decoder_audit/RESULT.md`

**Method:** proof-only.  No computation was run.

## Verdict

**CLEAN PASS.**

The amended artifact corrects every mathematical objection in the preserved
failed audit.  I independently tried to refute the amended statements,
including their constants, probability quantifiers, asymptotic deductions,
bit-complexity accounting, and scope.  I found no remaining counterexample or
proof gap.

In particular:

* Proposition 2.2 now has two valid and explicitly different conclusions.
  Under (2.4), the shorter coefficient is proved only to be nonzero modulo
  `q`.  Under the stronger (2.4u), it is proved to be a unit modulo `N`.
  Neither conclusion is misrepresented as failure of a gcd-of-SVP factoring
  algorithm.
* Proposition 2.3 and Theorem 4.1 remain valid when the errors are chosen as
  an arbitrary joint function of the complete quotient tuple.  Their bad
  events are replaced by necessary events depending only on the independent
  quotients.
* Theorem 4.1's union bound and its terminal `a=0`/`q | a` argument are exact.
* Corollary 4.2 really gives exponentially small failure at relative error
  (2^{-(1+\eta)\sqrt n}), and optimizing the same certificate gives the
  (2^{-(1+o(1))\sqrt n}) boundary.
* Section 5 proves only failure of this worst-case ordinary-LLL certificate at
  inverse-polynomial relative error.  It makes no LLL, ACD, or arbitrary-
  decoder hardness claim.
* Section 6 is now an explicitly imported, non-premise benchmark with the
  necessary fixed-balance slack (\beta<1/2).  It is not used in any F41
  theorem or method-boundary conclusion.
* The artifact repeatedly and correctly states that the approximate-multiple
  source is granted, not manufactured from bare `N`, and that F41 is neither
  an all-input factoring algorithm nor completion of the top-level Las Vegas
  goal.

The clean pass applies to the amended artifact only.  The first audit remains
a valid failed audit of the earlier version and should stay preserved.

---

## 1. Historical objections were substantively corrected

The first audit required three mathematical corrections.  All three are
present and are not cosmetic.

### 1.1 The shorter Dirichlet coefficient

The earlier version inferred a nonfactor from (q\nmid a).  The amended
Proposition 2.2 instead states:

1. under (2.4), (1\le a<q), hence only (q\nmid a);
2. under (2.4u), (1\le a<p,q), hence (\gcd(a,N)=1).

The discussion immediately following (2.9) explicitly allows the weak
branch's coefficient to be a multiple of `p`.  It also says that even the
unit competitor does not rule out a still shorter factor-bearing vector.
Thus the artifact now distinguishes all of the following:

* the designated (v_q) is not shortest;
* a particular shorter coefficient is a unit under (2.4u);
* an exact-SVP routine might nevertheless output another short coefficient
  whose gcd factors `N`.

No SVP-factoring impossibility is inferred.

### 1.2 Approximation isolation versus factor identifiability

The amended title and statements use “approximation-denominator isolation.”
They expressly deny statistical factor identifiability.  Equation (2.10)
retains the (\frac12\log m) contribution coming from (\sqrt d), and the
text claims only the same **coarse** (\Theta(n/\log n)) order at
inverse-polynomial noise.  It no longer asserts an exact matching threshold.

### 1.3 The one-sample benchmark

The divisor-Coppersmith statement is labeled “Imported theorem 6.1.”  The
artifact says it is neither proved there nor used by Theorem 4.1,
Corollary 4.2, or the F41 boundary.  Its balanced application now chooses

\[
 \xi=\eta/4,\qquad \beta=1/2-\xi,\qquad \eta'=\eta/4,
\]

rather than silently assuming (p\ge\sqrt N).  This correction is checked in
Section 8 below.

The preprocessing language was also corrected from an unconditional claim to
“often catches”: if both the error and the associated quotient difference
vanish, the gcd can be `N` rather than a proper factor.

---

## 2. Model and probability quantifiers

The model fixes

\[
 N=pq,\qquad z_i=pt_i+r_i,\qquad |r_i|\le B,
 \qquad \epsilon=B/p,
\]

with balanced distinct odd primes, independent uniform
(t_i\in\{0,\ldots,q-1\}), and errors chosen after the adversary sees the
entire quotient tuple.  All probability is over the quotients.  No later
proof conditions on an error distribution.

The constraints (B\ge1), (B<p/8), and (0\le z_i<N) are consistent with
the uses of (B) and imply (0<\epsilon<1/8).  The lattice construction uses
the usual integer error bound `B`; replacing an error bound by an integer
ceiling or by a public constant-factor upper bound only changes `epsilon` by
that factor, as the artifact notes.

The gcd preprocessing is safe.  It can only return after verifying a proper
divisor.  Failure of a preprocessing gcd to be proper does not enter any
lattice theorem.

---

## 3. Lemma 2.1 and both branches of Proposition 2.2

### 3.1 Lemma 2.1

Let (Q=\lfloor A^{1/m}\rfloor).  The (Q^m+1) points used in the proof
occupy (Q^m) half-open boxes, so two have an index difference
(1\le a\le Q^m\le A) and coordinatewise circular distance at most (1/Q).
The assumption (A\ge2^m) gives (A^{1/m}\ge2) and hence

\[
 Q\ge A^{1/m}/2,
 \qquad 1/Q\le2A^{-1/m}.
\]

The factor 2 and every endpoint are correct.

### 3.2 Weak branch (2.4)

Write

\[
 X=\left(\frac{2\sqrt d}{\epsilon}\right)^m.
\]

Condition (2.4), (X<q/(2\sqrt d)), certainly permits a real `A` with

\[
 X<A<q/\sqrt d.
\]

Moreover (X>2^m), since (\sqrt d/\epsilon>1); thus the selected `A`
meets Lemma 2.1's (A\ge2^m) premise.  With nearest integers `k_i`, the
lemma gives

\[
 |a|B<\frac{qB}{\sqrt d},
 \qquad
 |az_i-Nk_i|
 \le2N A^{-1/m}
 <\frac{N\epsilon}{\sqrt d}
 =\frac{qB}{\sqrt d}.
\]

All (d=m+1) coordinates are strictly below (qB/\sqrt d), so the norm is
strictly below `qB`.  Also

\[
 1\le a\le A<q/\sqrt d<q,
\]

which proves exactly (q\nmid a), and no stronger gcd conclusion.

### 3.3 Unit branch (2.4u)

If an `A` obeys

\[
 X<A<\min(p,q/\sqrt d),
\]

the identical coordinate proof applies.  Now

\[
 1\le a\le A<p
 \quad\text{and}\quad
 1\le a\le A<q,
\]

so, because (N=pq) with prime `p,q`, (\gcd(a,N)=1).  This is the exact
unit conclusion claimed.

For (\epsilon=n^{-c}), fixed balance and a sufficiently small fixed
(\kappa_{c,C}>0) make the logarithm of `X` smaller than both
(\log p) and (\log(q/\sqrt d)) throughout
(m\le\kappa_{c,C}n/\log n).  Thus the claimed coarse-order availability of
the unit branch is valid.  The artifact does not claim a sharp constant.

---

## 4. Proposition 2.3 under jointly adversarial errors

For a fixed (1\le a<q), the observed inequality (2.11) implies, regardless
of how the errors were chosen,

\[
 \left\|\frac{at_i}{q}\right\|
 \le \epsilon+\frac{a|r_i|}{N}
 <\epsilon+\frac{qB}{pq}
 =2\epsilon.
\]

The right side is an event involving only `t_i`.  Since `q` is prime and
(a\not\equiv0\pmod q), multiplication by `a` permutes the residues modulo
`q`.  At most (4\epsilon q+1) centered residues have distance at most
(2\epsilon q) from (q\mathbb Z).  Independence of the quotients therefore
gives

\[
 \Pr[\text{the necessary event for this fixed }a]
 \le(4\epsilon+1/q)^m.
\]

Union-bounding fewer than `q` positive coefficients proves (2.12).  The
errors may be correlated with all samples because they have disappeared from
the necessary event before independence is invoked.

Since (\epsilon<1/8) and `q` is an odd prime, the denominator in (2.14) is
positive.  The displayed sufficient sample count follows algebraically from
requiring the right side of (2.12) to be at most `delta`.

---

## 5. Lattice representation and determinant

The basis in (3.1) is triangular and full rank.  Its determinant is exactly

\[
 \det L=BN^m.
\]

The first coordinate uniquely fixes the coefficient `a`, so every lattice
vector has the representation (3.3).  Substituting (N=pq) and
(z_i=pt_i+r_i) gives the factor vector

\[
 v_q=(qB,qr_1,\ldots,qr_m),
 \qquad qB\le\|v_q\|_2\le qB\sqrt d.
\]

The determinant-scale identity is also exact:

\[
 \begin{aligned}
 \left(\frac{qB}{(BN^m)^{1/d}}\right)^d
 &=\frac{q^{m+1}B^{m+1}}{BN^m}\\
 &=\frac{q^{m+1}B^m}{(pq)^m}\\
 &=q(B/p)^m=\epsilon^m q.
 \end{aligned}
\]

Equation (3.6) is only an `asymp` statement under fixed balance and is used
only as a heuristic explanation, not as a proof premise.

---

## 6. Theorem 4.1

### 6.1 LLL length bound

In dimension (d=m+1), ordinary (\delta=3/4) LLL gives

\[
 \|b_1\|_2\le2^{(d-1)/2}\lambda_1(L)
 \le2^{m/2}\|v_q\|_2
 \le \Gamma qB\sqrt d=R.
\]

No distributional assumption appears in this step.

### 6.2 Bad coefficients and the union bound

For any vector of norm at most `R` with (a\ne0) and (q\nmid a),

\[
 |a|\le R/B=A.
\]

The residual coordinate gives

\[
 |apt_i+ar_i-pqk_i|\le R,
\]

and hence

\[
 \operatorname{dist}(at_i,q\mathbb Z)
 \le\frac{R+|a|B}{p}
 \le\frac{2R}{p}.
\]

For fixed `a` not divisible by `q`, at most (4R/p+1) residues satisfy this.
Dividing by `q` and using (R=\Gamma qB\sqrt d) gives exactly

\[
 \min\left(1,\frac{4R/p+1}{q}\right)
 =\min(1,4\Gamma\epsilon\sqrt d+1/q)=\theta.
\]

Again this necessary event contains no errors.  It therefore has probability
at most (\theta^m) even if the error vector is a joint function of the full
quotient vector.  There are at most (2\lfloor A\rfloor\le2A) eligible
nonzero signed coefficients.  This proves the bad-event bound
(2A\theta^m).  There is no need to union-bound the integers `k_i`.

### 6.3 The terminal cases

On the complement of the bad event, the LLL output has either `a=0` or
(q\mid a).

If `a=0`, uniqueness of (3.3) makes a nonzero vector lie in

\[
 \{0\}\times N\mathbb Z^m,
\]

so its norm is at least `N`.  This contradicts (\|b_1\|\le R<N).

Thus (q\mid a).  Also

\[
 0<|a|\le A<N.
\]

If `p` also divided `a`, then `N` would divide the nonzero integer `a`, which
is impossible below `N`.  Therefore

\[
 \gcd(|a|,N)=q.
\]

This remains true when `a` is a nontrivial multiple of `q`; the theorem does
not need (a=\pm q).  The final gcd verifies every returned factor.

The two displayed size conditions are harmless; indeed (B\ge1) and
(R<N) already imply (A=R/B<N).

### 6.4 Solving the exact bound

To force (2A\theta^m\le\delta), set

\[
 u=\left(\frac{\delta}{2\Gamma q\sqrt d}\right)^{1/m}.
\]

When (u>1/q), inequality (4.10) makes the untruncated expression in
`theta` at most `u`; since `u<1`, it follows that
(\theta\le u), and the desired failure bound follows.  Expanding `u` and
the denominator (4\Gamma\sqrt d) gives, up to the qualifications stated in
the artifact,

\[
 \epsilon\lesssim q^{-1/m}2^{-m/2}m^{-1/2}.
\]

The (2^{-m/2}) factor is genuinely the ordinary-LLL approximation loss.

---

## 7. Corollary 4.2, optimization, and Section 5

### 7.1 Fixed-slack many-sample regime

Let (s=\sqrt n), (a_0=1+\eta/2), and
(m=a_0s+O(1)).  Also let
(h=\log_2(1/\epsilon)\ge(1+\eta)s) and
(L=\log_2q=n/2+O_C(1)).

For large `n`, the (1/q) term in `theta` is smaller than the first term.
Consequently

\[
 \log_2(2A\theta^m)
 \le L+\frac{m^2}{2}-mh+O(m\log m).
\]

The coefficient of `n` in the leading part is

\[
 \frac12+\frac{a_0^2}{2}-a_0(1+\eta)
 =-\eta-\frac{3\eta^2}{8}<0.
\]

Since (m\log m=o(n)), the failure probability is
(2^{-\Omega_\eta(n)}).

The size conditions are also exact consequences of the same parameters:

\[
 \frac RN=\Gamma\epsilon\sqrt d
 =2^{-\Omega_\eta(\sqrt n)},
 \qquad
 \frac AN=\frac{\Gamma\sqrt d}{p}=o(1).
\]

Thus Corollary 4.2 is correct.

### 7.2 Optimized boundary

The leading requirement

\[
 h\ge L/m+m/2
\]

is minimized at (m=\sqrt{2L}), with value (\sqrt{2L}).  Under fixed
balance (2L=n+O_C(1)).  The terms suppressed in (4.15) are lower order for
constant or inverse-polynomial target failure, so the stated

\[
 \epsilon\le2^{-(1+o(1))\sqrt n}
\]

ordinary-LLL boundary is valid in its explicitly asymptotic sense.  The
fixed-slack Corollary 4.2 supplies the nonambiguous theorem.

### 7.3 Inverse-polynomial relative error

For (\epsilon=n^{-c}), (h=O(\log n)).  Proposition 2.2's condition holds
through a sufficiently small constant multiple of (n/\log n), including
the unit strengthening after reducing that constant.  This validates (5.1)
without claiming a sharp coefficient.

The claim that the proved ordinary-LLL certificate is trivial for every
dimension can be made directly from the exact bound.  If `theta=1`, then
(2A\theta^m=2A>1).  If `theta<1`, then

\[
 \theta\ge4\Gamma\epsilon\sqrt d,
\]

so

\[
 \begin{aligned}
 \log_2(2A\theta^m)
 &\ge L+\frac{m^2}{2}-mh
    +\frac m2+2m+\frac{m+1}{2}\log_2d+1\\
 &\ge L-\frac{h^2}{2}+\frac{(m-h)^2}{2}\\
 &\ge L-\frac{h^2}{2}
  =\frac n2-O(\log^2n)>0
 \end{aligned}
\]

for all sufficiently large `n`.  Hence no choice of `m` makes this **proved
failure bound** nontrivial at inverse-polynomial relative precision.

The artifact correctly stops there.  It does not infer that LLL never works
on a more favorable distribution, that no different decoder exists, or that
ACD is hard.  Its exact-SVP paragraph is explicitly about known exponential-
dimension enumeration methods and expressly disclaims an all-algorithm lower
bound.

---

## 8. External divisor-Coppersmith benchmark

Imported Theorem 6.1 is segregated from the self-contained F41 proof.  No
earlier or later F41 theorem cites it as a premise.  Its corrected balance
application is arithmetically sound.

For fixed target (0<\eta<1/4), the chosen parameters give

\[
 \beta^2-\eta'
 =\left(\frac12-\frac\eta4\right)^2-\frac\eta4
 =\frac14-\frac\eta2+\frac{\eta^2}{16}
 >\frac14-\eta.
\]

Fixed balance implies

\[
 p\ge C^{-1}\sqrt N\ge N^{1/2-\eta/4}=N^\beta
\]

for all sufficiently large `N`.  Therefore
(B\le N^{1/4-\eta}) lies strictly inside the imported theorem's root bound.

For (f(X)=X-z_1),

\[
 f(r_1)=r_1-z_1=-pt_1\equiv0\pmod p.
\]

When (0<t_1<q), (\gcd(N,z_1-r_1)=p); at (t_1=0), it is `N`, and a
fresh independent sample avoids that endpoint with probability (1-1/q).
These are exactly the qualifications stated.

Because the imported theorem is contextual and not a premise, F41 promotion
does not depend on accepting an unproved shift-lattice derivation.  The
artifact also rejects the use of a formal growing-dimensional multivariate
determinant exponent without dimension, LLL-loss, independence, and root-
extraction proofs.

---

## 9. Bit complexity, Las Vegas conversion, and scope

At (m=\Theta(\sqrt n)), the lattice dimension is (O(\sqrt n)) and every
basis entry has (O(n)) bits.  Exact-arithmetic LLL is polynomial in these
two parameters.  Lattice construction, (O(m^2)) preprocessing gcds,
coefficient extraction, the final gcd, division, and factor verification are
therefore polynomial in `n`.  The approximation factor (2^{m/2}) changes
the guarantee but not the input size or the polynomial bit-complexity of LLL.

If an external source produces fresh independent batches in polynomial time
and Theorem 4.1 gives inverse-polynomial success, repeating batches until a
verified proper gcd appears is Las Vegas: every output is correct, the good
quotient events give a geometric expected-trial bound, and termination is
almost sure.  Corollary 4.2 has success tending to one.

This is deliberately conditional.  The artifact does not produce those
samples from bare `N`.  It assumes a balanced semiprime and a granted source,
does not cover primes, prime powers, repeated factors, even inputs, or
arbitrary composites, and does not claim to meet the top-level all-input
factorization theorem.  These limitations are stated rather than hidden.

## Certified surviving statement

The amended F41 artifact supports exactly this method boundary:

1. Under (2.4), the natural `q`-factor vector is not shortest; under (2.4u),
   a strictly shorter unit-coefficient vector exists.  Neither statement
   defeats gcd-of-SVP factoring.
2. The explicit ordinary-LLL decoder factors uniformly over all admissible
   adversarial error rules with success at least
   (1-2A\theta^m).
3. A fixed-slack polynomial-time regime is
   (B/p\le2^{-(1+\eta)\sqrt n}), using (m=\Theta(\sqrt n)) samples.
4. The same proved certificate is noninformative at
   (B/p=1/\operatorname{poly}(n)).
5. No conclusion follows about a different decoder, helpful error
   correlations, manufacture of the source from bare `N`, or classical
   all-input polynomial-time factoring.

I found no claim in the amended artifact that exceeds this scope.
