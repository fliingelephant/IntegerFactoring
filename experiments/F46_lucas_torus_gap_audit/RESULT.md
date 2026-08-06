# F46 focused hostile audit

**Artifact audited:** experiments/F46_lucas_torus_gap_kill/RESULT.md

**Audit mode:** proof-only. I ran no finite number-theoretic experiment and
used no web source. I read the candidate in full together with PROMPT.md, the
preregistered F27 row of REGISTRY.md, and the relevant P12 and P20--P21 scope.
I independently reconstructed every theorem below rather than accepting the
candidate's derivation.

## Verdict

**PASS.** I found no mathematical error, quantifier leak, hidden factoring
oracle, unsupported generic-group inference, or all-input overclaim. No
mathematical amendment is required before the prescribed fresh proof-blind
reconstruction.

The reduction's most delicate point is sound, but its justification is a
coupling rather than a conditional-fairness assertion. If an implementation
stops when a denominator pole exposes a factor, the transcripts on which it
reaches the decoder are not distributed as unconditional fair-orientation
transcripts. Couple that implementation to an ideal generator that ignores
the factor, keeps the same \(D\), and resamples \(t\) until clean. On every
sample path where the ideal decoder would succeed, the implementation either
has already succeeded certainly on a pole or reaches the same clean transcript
and succeeds through the decoder. Hence early termination can only increase
the success probability. This validates the candidate's reduction without
claiming that the no-pole conditional transcript is fair.

The pass remains strictly promise-only. The exact relation and conditional
reduction concern distinct odd semiprimes. The generic theorem concerns
independently random-encoded cyclic groups of one common prime order with a
random exponent. It is not a lower bound for explicit Lucas coordinates,
cross-discriminant operations, unequal or composite torus orders,
non-generators, deterministic factor gaps, prime powers, or arbitrary
composites.

## 1. Quadratic algebra, norm, and unit criterion

Let \(R=\mathbb Z/N\mathbb Z\) for odd \(N\), let \(D\in R^\times\), and put

\[
A_D=R[w]/(w^2-D).
\]

The assignment \(a+bw\mapsto a-bw\) respects \(w^2=D\), is multiplicative,
and squares to the identity. Thus it is an \(R\)-algebra involution. Direct
multiplication gives

\[
\operatorname{Nm}(a+bw)=(a+bw)(a-bw)=a^2-Db^2.
\]

If this norm is a unit of \(R\), then

\[
(a+bw)^{-1}=(a-bw)(a^2-Db^2)^{-1}.
\]

Conversely, if \(x\in A_D\) is a unit, then its conjugate is a unit and
\(\operatorname{Nm}(x)=x\bar x\) is a unit of \(A_D\). Since the norm lies
in the embedded copy of \(R\), it is a unit of \(R\): an inverse in \(A_D\)
to a scalar \(r\in R\) forces multiplication by \(r\) on the free
\(R\)-module \(A_D\) to be invertible, equivalently \(r\in R^\times\).
More directly, writing an \(A_D\)-inverse in the basis \(1,w\) gives a scalar
inverse among its coefficient equations. Hence

\[
x\in A_D^\times\quad\Longleftrightarrow\quad
\operatorname{Nm}(x)\in R^\times.
\]

The norm-one units consequently form a group.

For \(t\in R\),

\[
\operatorname{Nm}(1-tw)=1-Dt^2=:z_D(t).
\]

When this scalar is a unit,

\[
\begin{aligned}
U_D(t)
&=(1+tw)(1-tw)^{-1}\\
&=\frac{(1+tw)^2}{1-Dt^2}\\
&=\frac{1+Dt^2}{1-Dt^2}
  +\frac{2t}{1-Dt^2}w.
\end{aligned}
\]

The numerator \(1+tw\) and denominator \(1-tw\) have the same norm, so
\(\operatorname{Nm}(U_D(t))=1\). All divisions made here are therefore
justified exactly on the stated denominator-clean branch.

## 2. Local Cayley parametrization and torus orders

Fix an odd prime \(r\nmid D\), write \(k=\mathbb F_r\), and consider

\[
A_{D,r}=k[w]/(w^2-D).
\]

For a nonpole \(t\), the Cayley image cannot equal \(-1\), because

\[
1+tw=-(1-tw)
\]

would imply \(2=0\). Conversely, take \(u=a+bw\) with norm one and
\(u\ne-1\). Its norm equation is

\[
a^2-Db^2=1.
\]

If \(a=-1\), then \(Db^2=0\), and \(D\ne0\) forces \(b=0\), contradicting
\(u\ne-1\). Therefore \(a+1\ne0\), and

\[
t=\frac{b}{a+1}
\]

is defined. The denominator satisfies

\[
1-Dt^2
=\frac{(a+1)^2-Db^2}{(a+1)^2}
=\frac{2}{a+1}\ne0.
\]

Substitution into the two Cayley coefficients returns \(a\) and \(b\):
using \(Db^2=a^2-1\),

\[
\frac{1+Dt^2}{1-Dt^2}=a,\qquad
\frac{2t}{1-Dt^2}=b.
\]

Thus

\[
\{t\in k:1-Dt^2\ne0\}
\longrightarrow T_D(k)\setminus\{-1\}
\]

is a bijection, with the displayed inverse. There is no exceptional
generator assumption.

If \(\chi_r(D)=+1\), choose \(\delta^2=D\). The equation
\(1-Dt^2=0\) has exactly the two roots \(t=\pm\delta^{-1}\). The split map

\[
a+bw\longmapsto(a+b\delta,a-b\delta)
\]

identifies the norm-one group with

\[
\{(x,x^{-1}):x\in k^\times\},
\]

so it is cyclic of order \(r-1\). The \(r-2\) nonpole parameters match the
\(r-2\) elements after deleting \(-1\).

If \(\chi_r(D)=-1\), the quadratic algebra is \(\mathbb F_{r^2}\), there
are no poles, and

\[
w^r=wD^{(r-1)/2}=-w.
\]

Thus conjugation is Frobenius and the displayed norm is the field norm.
The kernel of the norm on the cyclic group of order \(r^2-1\) has order
\((r^2-1)/(r-1)=r+1\). The \(r\) parameters again match the norm-one
elements other than \(-1\). Therefore, exactly as claimed,

\[
|T_D(\mathbb F_r)|=r-\chi_r(D).
\]

## 3. CRT denominator law and orientation distribution

Now let \(N=pq\), where \(3\le p<q\) are distinct primes, and choose a unit
\(D\) with Jacobi symbol \(-1\). Exactly one of \(D\bmod p,D\bmod q\) is a
square.

In orientation \((+,-)\), the equation \(z_D(t)=0\) has two solutions
modulo \(p\) and none modulo \(q\). Uniform \(t\bmod N\) has independent
uniform CRT components. Hence

\[
\Pr(\gcd(z_D(t),N)=p)=\frac2p,\qquad
\Pr(\gcd(z_D(t),N)=1)=1-\frac2p,
\]

and the probabilities of gcd \(q\) and \(N\) are zero. In orientation
\((-,+)\), the same argument gives

\[
\Pr(\gcd(z_D(t),N)=q)=\frac2q,\qquad
\Pr(\gcd(z_D(t),N)=1)=1-\frac2q,
\]

with the other two probabilities zero. In particular, every pole returns
the unique split local prime, and the nonsplit component makes gcd \(N\)
impossible.

For fixed \(D\), repeated uniform \(t\)'s are clean after expected

\[
\frac1{1-2/r_s}\le3
\]

draws, because the split prime \(r_s\ge3\). Conditioning on cleanliness
removes two values only from the split CRT coordinate and removes none from
the nonsplit coordinate. Independence of the two CRT components is retained,
and the Cayley bijection therefore makes the two local points independently
uniform on their respective tori with \(-1\) deleted. This is a statement
about uniform points, not generators.

For each local prime, exactly half the nonzero residues have either Legendre
sign. Thus each of the four sign pairs contains

\[
\frac{p-1}{2}\frac{q-1}{2}
\]

global units. Conditional on Jacobi symbol \(-1\), the two orientations are
exactly equiprobable. Independent accepted choices of \(D\) give independent
fair orientations.

This fairness survives keeping \(D\) and resampling only \(t\), because every
chosen \(D\) eventually contributes exactly one retained relation. It does
not survive rejecting the whole pair \((D,t)\). For one-shot pair
conditioning, Bayes' rule gives

\[
\Pr((+,-)\mid\mathrm{clean})
=\frac{1-2/p}{(1-2/p)+(1-2/q)}
\]

and the complementary formula with \(p,q\) exchanged. Since \(p<q\), the
\((-,+)\) orientation is favored. Averaging before any conditioning gives

\[
\Pr(\gcd(z_D(t),N)=p)=\frac1p,\quad
\Pr(\gcd(z_D(t),N)=q)=\frac1q,\quad
\Pr(\gcd(z_D(t),N)=1)=1-\frac1p-\frac1q.
\]

All four probability claims in the candidate are therefore exact.

## 4. Early termination versus a fair decoder transcript

The candidate correctly distinguishes the samplers, but the conditional
reduction deserves an explicit coupling audit.

Define an ideal transcript generator \(G\) as follows. For each relation it
uses rejection sampling until it obtains a unit \(D\) of Jacobi symbol
\(-1\), then keeps that \(D\) and resamples \(t\) until the denominator is
clean. It records only the final clean triple. It deliberately ignores every
proper gcd encountered during these rejections. The resulting \(K\)-triple
transcript has exactly the unconditional fair-orientation distribution in
the decoder contract.

Define the actual factoring implementation \(A\) on the same infinite random
tape. It performs the same draws, but returns immediately whenever a
discriminant or denominator gcd is proper. If no such gcd occurs before all
\(K\) clean triples are ready, it gives those triples to the decoder and
verifies the returned candidate.

Let \(P\) be the event that a proper gcd is encountered during this coupled
trial, and let \(S\) be the event that the decoder succeeds on the complete
ideal transcript generated from the same random tape. On \(P\), algorithm
\(A\) succeeds certainly. On \(P^c\), \(A\) reaches the decoder with exactly
the same transcript as \(G\), so it succeeds whenever \(S\) occurs. Therefore

\[
\mathbf 1_{\{A\text{ succeeds}\}}
\ge \mathbf 1_S
\]

pointwise, and

\[
\Pr(A\text{ succeeds})\ge\Pr(S).
\]

This proves that an unconditional inverse-polynomial decoder guarantee
transfers unchanged to the early-terminating factoring implementation.
There is no need, and it would be false, to assert that the transcript
conditioned on \(P^c\) remains fair. The actual trial also performs no more
work than the ideal generator on the same tape. Thus the coupling preserves
both the success lower bound and the polynomial expected-cost bound.

The same argument covers nonunit discriminant draws: the ideal rejection
sampler discards them, whereas the actual algorithm succeeds on every proper
gcd. A draw \(D=0\bmod N\), whose gcd is \(N\), is merely retried in both
processes.

Consequently the sentence that a discriminant or denominator gcd may
terminate earlier is mathematically valid. An explicit coupling is the
right proof; no change to the candidate's theorem or algorithm is needed.

## 5. Pointwise factor-gap identity

Put \(g=q-p>0\). CRT identifies the global torus with the product of its two
local tori. It suffices to reduce \(N-1\) modulo the applicable local group
orders.

For orientation \((+,-)\), the orders are \(p-1\) at \(p\) and \(q+1\) at
\(q\). Modulo \(p-1\),

\[
N-1=pq-1\equiv q-1\equiv q-p=g.
\]

Modulo \(q+1\),

\[
N-1=pq-1\equiv-p-1\equiv q-p=g.
\]

For orientation \((-,+)\), the orders are \(p+1\) and \(q-1\). Modulo
\(p+1\),

\[
N-1\equiv-q-1\equiv p-q=-g,
\]

and modulo \(q-1\),

\[
N-1\equiv p-1\equiv p-q=-g.
\]

It follows for every global norm-one unit \(U\), not merely a generator or
a generic point, that

\[
U^{N-1}=U^g\quad\text{in orientation }(+,-),
\]

\[
U^{N-1}=U^{-g}\quad\text{in orientation }(-,+).
\]

Negative powers are legitimate because \(U\) is a unit. The proof includes
the identity element, \(-1\), all lower-order elements, and every other
non-generator. Clean Cayley samples form a subset of these elements, so no
exceptional sample was omitted.

## 6. Uniform generation and bit complexity

Uniform rejection from \(n\)-bit strings generates an exact uniform residue
modulo \(N\) with expected \(O(n)\) random bits, since
\(2^{n-1}\le N<2^n\). For a uniform residue \(D\), gcd screening either
returns a proper factor, retries \(D=0\), or reaches a unit. Among units of a
distinct odd semiprime, exactly half have Jacobi symbol \(-1\). Thus a raw
draw is accepted with probability

\[
\frac{\varphi(N)}{2N}
=\frac{(p-1)(q-1)}{2pq}
\ge\frac4{15},
\]

where equality occurs at \(p=3,q=5\). Rejections therefore have constant
expected count unless a factor is found first.

For a clean \(t\), one modular inverse and the displayed coefficient formulas
construct \(U\). Ring multiplication uses a constant number of modular
multiplications, and binary powering to exponent \(N-1\) uses \(O(n)\) ring
multiplications. All coefficients are reduced modulo \(N\), so their stored
length is \(O(n)\). Standard multiplication, modular reduction, Jacobi, gcd,
extended gcd, and exact uniform sampling give the claimed polynomial bit
cost. In the notation \(M(n)\) for \(n\)-bit multiplication, the candidate's

\[
O(nM(n)+M(n)\log n)
\]

per-relation bound is a valid coarse bound, and \(K\) relations cost
\(O(KnM(n))\) expected bit operations and \(O(Kn)\) expected random bits.
Keeping \(D\) while resampling \(t\) contributes only the factor at most
three established above. No unreduced exponential-size power is ever
materialized.

## 7. Gap verification and exact promise scope

Given an integer candidate \(h\), the verifier first enforces \(0<h<N\).
Hence \(h\), \(h^2+4N\), its integer square root, and every subsequent
quantity have \(O(n)\) bits. If

\[
\Delta=h^2+4N=s^2,\qquad s\equiv h\pmod2,
\]

then

\[
p'=\frac{s-h}{2},\qquad q'=\frac{s+h}{2}
\]

are integers. The stated inequalities make them nontrivial, and the final
test \(p'q'=N\) makes every accepted result correct on every input.

For the true gap \(h=q-p\),

\[
h^2+4N=(q-p)^2+4pq=(p+q)^2,
\]

so \(s=p+q\) and the verifier returns \(p,q\). This proves the deterministic
gap-to-factor map.

Assume the decoder contract exactly as stated: for every distinct odd
semiprime, \(K=\operatorname{poly}(n)\) clean triples from the fair
choose-\(D\)-first sampler yield the magnitude \(q-p\) with
inverse-polynomial probability in polynomial bit time. The coupling in
Section 4 transfers that probability to an implementation that stops on
proper gcds. Every decoder output is verified, so errors only cause a retry.
Independent trials give a geometric number of attempts with polynomial
expectation and almost-sure termination. This is a valid classical Las Vegas
reduction for the distinct odd-semiprime promise.

It does not cover prime squares: their squared local character supplies no
Jacobi-minus-one orientation. Nor does the local field-order argument cover
prime powers. With at least three distinct prime factors, there are many sign
patterns and no single two-factor gap identity; the square-discriminant
reconstruction is likewise two-factor-specific. Even inputs, repeated
factors, arbitrary composites, recursion, and complete factorization are not
reduced to this decoder. The candidate explicitly preserves all these gaps
and does not claim the top-level result.

## 8. Generic shared-exponent theorem

### 8.1 Formal expressions and collision set

Fix the algorithm's random coins and run a symbolic generic oracle. In group
\(i\), the three initial handles represent

\[
0,\qquad 1,\qquad \sigma_iX.
\]

Products add affine expressions, inverses negate them, and known-scalar
powers multiply them by a known scalar. A scalar selected adaptively as a
function of opaque labels is still fixed on the particular symbolic
transcript; because those ideal labels are independent of \(e\), this does
not introduce \(e\) into the coefficients. Every materialized handle
therefore has an affine formal exponent \(a+bX\).

Let \(q_i\) be the number of operation outputs in group \(i\). Equality tests
create no handles, so

\[
\sum_iq_i\le Q,\qquad m_i\le3+q_i.
\]

For two distinct affine expressions in one group, their difference is a
nonzero affine polynomial and has at most one root in \(\mathbb F_\ell\).
Thus the union \(B\) of all exponent values causing a surprise collision on
the ideal run obeys

\[
|B|\le C:=\sum_{i=1}^K\binom{m_i}{2}
\le\sum_{i=1}^K\binom{q_i+3}{2}.
\]

This deliberately overcounts pairs with equal slope and unequal intercept,
which have no root, and repeated occurrences of the same formal expression,
which need not be paired at all. Initial collisions such as \(e=0\) or
\(\sigma_i e=1\) are included among the three initial-handle pairs. Identity
expressions and zero expressions therefore create no missing case.

The function \(q\mapsto\binom{q+3}{2}\) is convex on nonnegative integers.
Moving operations from a smaller occupied group to a larger one cannot
decrease the sum. Hence, subject to \(\sum_iq_i\le Q\),

\[
C\le\binom{Q+3}{2}+3(K-1).
\]

The further inequality

\[
\binom{Q+3}{2}+3(K-1)
\le\binom{Q+3K}{2}
\]

holds for \(K\ge1,Q\ge0\), so both constants in the candidate are valid.

There is one harmless proof-presentation edge case. A lazy ideal oracle
cannot assign distinct labels to more than \(\ell\) distinct formal
expressions in one order-\(\ell\) group. If the untruncated right side of
the theorem is at least one, however, the asserted minimum with 1 is already
the trivial probability bound and no coupling proof is needed. In the only
nontrivial case \(1/\ell+C/\ell<1\), one has \(C<\ell-1\), which precludes
more than \(\ell\) distinct expressions in any group. The fresh-label
construction is then well-defined. This supplies the implicit case split
behind the candidate's displayed minimum; it does not change the theorem or
its constant.

### 8.2 Adaptive coupling and success probability

For \(e\notin B\), distinct formal expressions encountered within one group
evaluate to distinct group elements. The ideal oracle's lazy assignment of
uniform unused labels can therefore be extended to a uniform random
bijection \(\xi_i:\mathbb F_\ell\to\mathcal L_i\). Independent lazy
assignments across the tagged groups extend to independent encodings.

The coupling is fully adaptive. Until a surprise collision, the real and
ideal executions present the same labels and equality answers, so the
algorithm requests the same next operation. A first deviation must be an
equality of two already materialized, formally distinct affine expressions,
and is charged to \(B\). Counting every pair of materialized handles also
covers an algorithm that notices equal label strings without issuing a
separately counted equality query.

The complete ideal transcript and the algorithm's ideal output depend on
the random encodings and its coins, but not on uniform \(e\). Its probability
of outputting \(e\) is therefore \(1/\ell\). The real execution can differ
only when \(e\in B\), an event of probability at most \(C/\ell\). Averaging
over the ideal labels and the algorithm's coins yields

\[
\Pr(\widehat e=e)
\le\min\left\{1,\frac1\ell+
\frac{\binom{Q+3}{2}+3(K-1)}{\ell}\right\}.
\]

This argument already grants the signs \(\sigma_i\), the identity label,
arbitrary adaptivity across all groups, nonuniform strategy in the public
parameters, and unlimited computation between oracle calls. Disjoint group
tags rule out cross-group label collisions by definition, and the theorem
does not silently use such collisions.

### 8.3 Subset, list, and nonuniform priors

If \(e\) is uniform on a public subset \(S\) of size \(H\), each distinct
affine pair still contributes at most one bad point of \(S\). Therefore
\(\Pr(e\in B)\le C/H\), while an ideal scalar guess succeeds with probability
at most \(1/H\). This proves

\[
\Pr(\widehat e=e)\le\min\left\{1,\frac{1+C}{H}\right\}.
\]

For a list of at most \(L\) outputs, the ideal term is at most \(L/H\), so
the numerator becomes \(L+C\), equivalently the candidate's instruction that
the baseline numerator 1 is replaced by \(L\). For an arbitrary prior
\(\mu\),

\[
\Pr(e\in B)\le C\max_x\mu(x)
\]

and the ideal guess succeeds with probability at most \(\max_x\mu(x)\).
Thus

\[
\Pr(\widehat e=e)\le(C+1)\max_x\mu(x).
\]

All three corollaries are valid, including intervals embedded injectively in
\(\mathbb F_\ell\). They are distributional generic bounds, not worst-case
bounds for a fixed factor gap.

## 9. Strict scope of the generic result

The generic theorem proves only that the number of relations alone does not
force efficient recovery in its opaque prime-order model. Each of the
candidate's exclusions is necessary:

* Actual Lucas elements have explicit coefficient pairs over
  \(\mathbb Z/N\mathbb Z\); they are not random labels.
* Different discriminants share one public coefficient ring, allowing
  coordinate arithmetic, resultants, determinants, gcds, and
  discriminant-changing constructions forbidden by tagged generic groups.
* Actual local orders \(p\pm1,q\pm1\) are unequal and usually composite, and
  the global torus is a product rather than one prime-order cyclic group.
* Cayley samples need not be generators; the exact gap identity is pointwise,
  but the generic theorem starts from fixed generators.
* For fixed \(N\), \(q-p\) is deterministic. No uniform or low-maximum-mass
  prior has been proved across a worst-case input family.
* A promised short interval changes the quantitative target. The subset
  theorem gives a birthday-scale generic bound but neither rules out nor
  supplies a polynomial explicit-coordinate interval decoder.
* Zero divisors and gcd outputs have no analogue in the field-valued generic
  group oracle.
* Prime powers, arbitrary composites, and all-input recursive factoring are
  outside both the exact semiprime decoder contract and the generic theorem.

Accordingly the candidate correctly labels its negative conclusion as method
failure for independently random-encoded common-prime-order relations. It
does not turn that model-specific obstruction into a factoring lower bound.
It also correctly keeps F27 open for a coordinate-specific decoder.

## 10. Prior-family comparison and final audit disposition

P20--P21 concern a succinct evaluator for an exponentially long torus
order-threshold product and provide a conditional all-input reduction. F46
instead evaluates only ordinary powers and exposes a promise-only shared gap.
The present generic theorem is not an arithmetic-circuit lower bound for the
P20 product.

P12 concerns dense moment or spectral representations for one multiplication
operator on a constructed family. It expressly excludes broad adaptive and
explicit-arithmetic claims. The F46 generic theorem uses a different opaque
multi-group model and cannot be cited as a lower bound for P12's excluded
algorithms. Neither result subsumes the other.

The candidate is internally well presented. A byte-level check found valid
UTF-8, no disallowed ASCII control character, no carriage return, and a final
newline. Section breaks, displayed equations, signs, and inequality
directions are intact. Its proof-only label is accurate, so no computation
ledger entry is required.

The hostile-audit disposition is therefore **PASS**, with no mathematical
repair requested. The next verification step is a fresh context-free
end-to-end reconstruction from the theorem statement and key ideas only.
