# Hostile audit of F41: metric ACD decoder boundary

**Artifact audited:** `experiments/F41_metric_acd_decoder_kill/RESULT.md`

**Method:** proof-only. No computation was run.

## Verdict

**Amendment required; Theorem 4.1 and Corollary 4.2 survive, but the
artifact must not be promoted unchanged.**

The central positive statement is sound: for independent uniform quotients
and arbitrarily correlated bounded errors, the displayed simultaneous-
approximation lattice plus ordinary LLL factors with the probability in
(4.4). Its optimization really gives the sufficient relative-error scale

\[
  \log_2(1/\epsilon)\ge (1+o(1))\sqrt n,
\]

and dimension \(\Theta(\sqrt n)\). The artifact also correctly disclaims any
hardness conclusion at inverse-polynomial relative error.

Three corrections are mandatory.

1. Proposition 2.2 proves only \(q\nmid a\). It does **not** prove that its
   shorter coefficient is a nonfactor: \(a\) may equal \(p\), or may be a
   positive multiple of \(p\) below \(q\). Consequently it obstructs reading
   the designated denominator \(q\) from the factor vector, but as stated it
   does not obstruct a shortest-vector **factoring** algorithm followed by a
   gcd. To guarantee a unit coefficient, the Dirichlet parameter must also
   satisfy \(A<p\).
2. “Metric identifiability” is too strong a name for what Section 2 proves.
   The propositions concern isolation of a simultaneous-approximation
   denominator in a specified range, not statistical identifiability of the
   factors or all publicly representable candidates. Moreover Proposition
   2.2 has a \(\sqrt m\) loss which is not harmless in every regime. The two
   propositions give the same \(\Theta(n/\log n)\) order for
   \(\epsilon=n^{-c}\), but they do not prove an exact matching threshold.
3. Lemma 6.1 is a standard divisor-Coppersmith theorem, but the paragraph
   offered as its proof is only a roadmap. It supplies neither the ranges of
   \(i,j\), the lattice dimension and determinant, nor the norm inequality
   which forces integer vanishing. Under a self-contained-proof requirement,
   this lemma has not been proved. In addition, balancedness gives
   \(p\ge C^{-1}\sqrt N\), not necessarily \(p\ge\sqrt N\); the application
   must choose a fixed \(\beta<1/2\) and reallocate the exponent slack.

All other quantitative checks are recorded below.

## 1. Model, adversarial errors, and gcd preprocessing

The probability quantifiers are coherent. For every fixed coefficient \(a\),
both Proposition 2.3 and Theorem 4.1 replace the error-dependent short-vector
event by a necessary event involving only the individual quotient \(t_i\).
The latter events are independent because the \(t_i\) are independent. Thus
the errors may be an arbitrary joint function of the complete quotient tuple;
no independence of the errors is silently used.

The gcd preprocessing is safe and can only help the later theorem. The prose
that it “catches zero errors [and] equal errors” should be weakened to
“often catches.” If \(r_i=0=t_i\), then \(\gcd(N,z_i)=N\), not a proper
factor. Likewise, if \(r_i=r_j\) and \(t_i=t_j\), the difference gcd is
\(N\). For a zero error with \(t_i\ne0\), or equal errors with distinct
quotients, the advertised proper factor \(p\) is obtained.

No algorithmic step requires knowing \(p\) or \(q\). The proof parameters
\(R,A,\theta\) may depend on them because they are used only to state a
promise and analyze success. Scaling by a public upper bound for \(B\) is
also legitimate; a dyadic sweep has only \(O(n)\) guesses and every candidate
factor is verified.

## 2. Dirichlet lemma and the shorter-vector proposition

Lemma 2.1, including its factor 2, is correct. With
\(Q=\lfloor A^{1/m}\rfloor\), the hypothesis \(A\ge2^m\) gives
\(Q\ge A^{1/m}/2\). Pigeonholing \(Q^m+1\) points into \(Q^m\) half-open
boxes yields \(1\le a\le Q^m\le A\) and circular coordinate error at most
\(1/Q\le2A^{-1/m}\).

The coordinate inequalities in Proposition 2.2 are also correct. If

\[
  \left(\frac{2\sqrt d}{\epsilon}\right)^m<A<\frac q{\sqrt d},
\]

then

\[
 |a|B<\frac{qB}{\sqrt d},\qquad
 |az_i-Nk_i|<\frac{qB}{\sqrt d},
\]

so the resulting nonzero vector has Euclidean norm strictly below \(qB\).
Since \(a<q\), it is not divisible by \(q\). The factor vector has norm at
least \(qB\), exactly as claimed.

The invalid step is calling this coefficient a “nonfactor.” From \(a<q\) one
cannot infer \(\gcd(a,N)=1\). A corrected unit-coefficient version is:
if there is an \(A\) satisfying

\[
 \left(\frac{2\sqrt d}{\epsilon}\right)^m
   <A<\min\!\left(p,\frac q{\sqrt d}\right),
\tag{A2.1}
\]

then the same proof produces a strictly shorter vector with
\(1\le a<\min(p,q)\), hence \(\gcd(a,N)=1\). A convenient sufficient
condition is to put a fixed slack factor between the left side of (A2.1) and
that minimum. Fixed balance makes this available through the same asymptotic
\(\Theta(n/\log n)\) range for inverse-polynomial \(\epsilon\), away from
the constant-factor boundary. It is not implied by the current hypothesis
(2.4) for every allowed \(p/q,m,\epsilon\).

The impact on later claims must be stated precisely:

* the current proposition proves that \(v_q\) is not a shortest vector;
* it defeats the instruction “return the coefficient of \(v_q\) as \(q\)”;
* it does not by itself defeat “return the gcd of the coefficient of an SVP
  output,” because a shorter coefficient could expose \(p\).

## 3. Denominator isolation, not information-theoretic identifiability

Proposition 2.3 is correct. If \(1\le a<q\) obeys (2.11), then

\[
 \left\|\frac{at_i}{q}\right\|
 \le \epsilon+\frac{aB}{N}<2\epsilon.
\]

For fixed nonzero \(a\bmod q\), multiplication by \(a\) permutes the
residues, and at most \(4\epsilon q+1\) centered residues are allowed.
Taking the product over independent quotients and union-bounding fewer than
\(q\) coefficients gives (2.12), uniformly over the joint error rule.

This is only isolation among positive coefficients below \(q\), at the
specified tolerance. It is not isolation among all coefficients that the
later LLL output might possess; Theorem 4.1 separately handles signed
\(|a|\le A\). It is also not factor identifiability: \(N\) already fixes its
unordered factor pair, and a competing denominator need not divide \(N\).
The recommended terminology is “approximation-denominator isolation.”

The scale discussion needs one qualification. Taking logarithms of (2.4)
gives

\[
 m\left(\log(1/\epsilon)+\log(2\sqrt{m+1})\right)
 <\log q-O(\log m),
\]

not merely \(m\log(1/\epsilon)<\log q\). For
\(\epsilon=n^{-c}\) this still gives \(m=\Theta(n/\log n)\), but the
\(\tfrac12\log m\) term changes the constant in front. For fixed
\(\epsilon\), it changes this particular shorter-vector lower bound from
order \(\log q\) to order \(\log q/\log\log q\). Thus “harmless” is valid
only at the level of the coarse order claimed for inverse-polynomial noise.

If the goal is merely to prove a competing denominator rather than a vector
strictly shorter than \(v_q\), Lemma 2.1 can instead use
\((2/\epsilon)^m<A<q\), removing the \(\sqrt d\) term. That distinct
argument should be written if Section 2 wants a general denominator-isolation
threshold. As written, Propositions 2.2 and 2.3 match only coarsely in the
inverse-polynomial regime, not as an exact threshold.

## 4. Lattice, determinant, and factor vector

The row lattice in (3.1) is full rank and every vector has the unique form
(3.3). Its determinant is \(BN^m\), and

\[
 v_q=(qB,qr_1,\ldots,qr_m),\qquad
 qB\le\|v_q\|_2\le qB\sqrt d.
\]

Raising the scale ratio in (3.5) to the \(d=m+1\) power gives the exact
identity

\[
 \left(\frac{qB}{(BN^m)^{1/d}}\right)^d=\epsilon^m q.
\tag{A4.1}
\]

The artifact writes \((\epsilon^m p)^{1/d}\) only after an
\(\asymp\) sign. That is valid under fixed balance, but (A4.1) is the exact
formula and would be cleaner.

## 5. Theorem 4.1 survives the hostile audit

For \(\delta=3/4\), ordinary LLL gives
\(\|b_1\|\le2^{(d-1)/2}\lambda_1(L)\), hence (4.5). If a vector of norm at
most \(R\) has \(a\ne0\) and \(q\nmid a\), then

\[
 |a|\le R/B=A,
 \qquad
 \operatorname{dist}(at_i,q\mathbb Z)
 \le (R+|a|B)/p\le2R/p.
\]

The number of centered residues satisfying the latter bound is at most
\(4R/p+1\). Dividing by \(q\) gives exactly

\[
 \min\left(1,4\Gamma\epsilon\sqrt d+\frac1q\right)=\theta.
\]

There are fewer than \(2A\) eligible nonzero signed coefficients. The union
bound \(2A\theta^m\) therefore holds without union-bounding the \(k_i\), and
without conditioning on independent errors.

On the complementary event, an LLL output with \(a=0\) would be a nonzero
vector in \(\{0\}\times N\mathbb Z^m\), of norm at least \(N\), contradicting
\(R<N\). Thus \(q\mid a\). The bound \(0<|a|<N=pq\) rules out \(p\mid a\),
so \(\gcd(a,N)=q\). This last implication is correct even when \(a\) is a
nontrivial multiple of \(q\).

Because \(B\ge1\), \(R<N\) actually implies \(A=R/B<N\), so the two
conditions in (4.3) are redundant but harmless. Solving
\(2A\theta^m\le\delta\) gives (4.9)--(4.11); the extra
\(2^{-m/2}\) factor is genuinely the worst-case LLL approximation loss.

## 6. Optimization and bit complexity

Corollary 4.2 has the right exponent. Let
\(a_0=1+\eta/2\), so \(m=a_0\sqrt n+O(1)\), and take
\(h=(1+\eta)\sqrt n\). The order-\(n\) coefficient in (4.14) is

\[
 \frac12+\frac{a_0^2}{2}-a_0(1+\eta)
 =-\eta-\frac{3\eta^2}{8}<0.
\]

The omitted \(O(m\log m)=o(n)\) terms do not consume this fixed margin.
Moreover

\[
 R/N=\Gamma\epsilon\sqrt d=2^{-\Omega_\eta(\sqrt n)},
 \qquad
 A/N=\Gamma\sqrt d/p=o(1),

\]

so the size conditions hold for sufficiently large \(n\). The claimed
failure probability \(2^{-\Omega_\eta(n)}\) follows.

Minimizing \(L/m+m/2\) gives \(m=\sqrt{2L}\) and value
\(\sqrt{2L}=\sqrt{n+O_C(1)}\). To obtain a stated success probability one
also needs the additive lower-order terms in (4.15), so (4.16) is correct
only in its intended \((1+o(1))\) sense; Corollary 4.2 supplies an unambiguous
fixed-slack version.

The bit-complexity claim is sound. The dimension is \(m+1\), the basis
entries have \(O(n)\) bits, and exact-arithmetic LLL is polynomial in both.
At \(m=\Theta(\sqrt n)\), the \(O(m^2)\) gcd preprocessing is polynomial as
well. Fresh-batch repetition is genuinely Las Vegas because every proposed
factor is verified; the expected-time conclusion remains conditional on a
polynomial-time source producing fresh independent quotient batches.

## 7. What the inverse-polynomial calculation does and does not prove

For \(h=O(\log n)\), minimizing

\[
 \frac n2+\frac{m^2}{2}-mh

\]

gives \(n/2-h^2/2>0\). If \(m\) is made still larger, then
\(4\Gamma\epsilon\sqrt d\ge1\) and the exact bound is already trivial.
Thus no choice of \(m\) makes **this proved worst-case LLL certificate**
nontrivial at inverse-polynomial relative error. This calculation is valid.

It is not an LLL failure theorem, an ACD hardness theorem, or an
identifiability lower bound for arbitrary decoders. The artifact generally
says this correctly. The one overstatement is the use of Proposition 2.2 as
a blanket “shortest-vector selection is defeated” claim: without (A2.1), a
shorter output may itself have gcd \(p\). The safe statement is that the
designated \(q\)-vector is not shortest and cannot simply be singled out by
its length.

The exact-SVP paragraph is acceptable as an accounting statement about
currently known enumeration algorithms, because it explicitly disclaims an
all-algorithm lower bound. It should continue to say “known algorithms,” not
suggest that exponential dependence on dimension has been proved necessary.

## 8. The Coppersmith benchmark needs a real proof or an explicit import

The mathematical theorem quoted in Lemma 6.1 is the usual monic univariate
small-root theorem modulo an unknown divisor, with exponent \(\beta^2\) in
degree one. But the text after the lemma does not prove it. In particular,
“polynomials of the form”

\[
 N^{h-i}f(X)^iX^j

\]

does not specify the ranges or extra shifts, and no dimension, scaled
determinant, LLL norm, Howgrave--Graham integer-vanishing inequality, or list
bound is derived. Saying that a triangular determinant gives “exactly the
exponent” is the missing argument, not its proof. The artifact must either
provide that derivation or label Lemma 6.1 as an explicitly imported standard
theorem under whatever citation/import policy governs the project.

The balanced application also needs a parameter correction. Fixed balance
only gives

\[
 p\ge C^{-1}N^{1/2}.

\]

For every fixed \(\xi>0\), this implies \(p\ge N^{1/2-\xi}\) for all
sufficiently large \(N\). Given a target slack \(\eta>0\), choose a small
fixed \(\xi\) and a separate theorem slack \(\eta'>0\) such that

\[
 (1/2-\xi)^2-\eta'\ge1/4-\eta.

\]

Applying Lemma 6.1 with \(\beta=1/2-\xi\) then yields (6.3). Thus the
conclusion survives, but it does not follow by silently setting
\(\beta=1/2\) when \(p<\sqrt N\).

For \(f(X)=X-z_1\), the congruence
\(f(r_1)=-pt_1\equiv0\pmod p\) is correct. Once \(r_1\) is recovered,
\(\gcd(N,z_1-r_1)=p\) unless \(t_1=0\), in which case it is \(N\).
Under the stated uniform quotient law, an independent retry avoids this
endpoint with probability \(1-1/q\). Accordingly, “one-sample recovery” is
deterministic recovery of the error root, while one-sample factor recovery
has this explicitly noted exceptional quotient.

## 9. Required canonical wording

After amendment, F41 supports the following boundary and no stronger one:

* the natural \(q\)-factor vector is deterministically not shortest under
  (2.4), but the exhibited shorter coefficient is known only to satisfy
  \(q\nmid a\);
* ordinary LLL has a rigorously proved, adversarial-error-uniform factoring
  regime at relative precision \(2^{-(1+\eta)\sqrt n}\);
* the same proof certificate is trivial at inverse-polynomial relative
  precision;
* this says nothing about a different decoder, favorable error structure, or
  manufacture of the source from bare \(N\);
* the divisor-Coppersmith comparison may be retained only after a complete
  proof/import and the \(\beta<1/2\) balance correction.

With those changes, the main method boundary survives. It is neither a
factoring algorithm from bare \(N\) nor a general lower bound for metric or
approximate-common-divisor approaches.
