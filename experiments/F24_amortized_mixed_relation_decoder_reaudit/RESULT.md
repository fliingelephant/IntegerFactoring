# Fresh hostile re-audit of revised F24

**Object audited:** the substantively revised F24 report.

**Computation:** none. This is a symbolic audit.

**Verdict:** **PASS WITH CORRECTIONS.**

The direct-sampling theorem survives. The floor constants, pairwise
independence, second-moment bound, CRT independence, cancellation-free gcd
predicate, and promise-only Las Vegas reduction are correct. The sign-free
meet-in-the-middle identity is also correct. Monic product/remainder trees over
\(\mathbb Z/N\mathbb Z\) are division-safe, and a carry-safe
Kronecker-substitution implementation gives the claimed
\(N^{1/4+o(1)}\) bit-time and bit-space bounds at this threshold.

There is one localized mathematical mismatch in the optional Hurwitz section.
P30 proves both row and image uniformity for the **raw residual quaternion**
\(\widetilde\beta=x+yi+zj+wk\), whose norm is divisible by \(N\). It does
not prove both marginals for an arbitrarily normalized norm-\(N\) one-sided-gcd
output. Section 9 calls its \(\beta,\gamma\) primitive norm-\(N\) outputs and
then invokes both P30 marginals. Replace them by two independent raw residual
quaternions, or delete the dispensable prefix. With the raw objects the
\(2/s_r\) trace bound and retention argument are valid.

Subject to that correction, strict proof-blind reconstruction is warranted.
It should reconstruct the direct theorem and evaluator, not inherit the
literal norm-\(N\) source wording in Section 9.

## 1. Threshold and local probability

Assume

\[
  N=pq, \qquad 53\le p<q<2p,
\]

for distinct odd primes, and set

\[
 h=\lfloor\sqrt N\rfloor, \quad
 b=\lfloor\log_2h\rfloor, \quad
 K=b-3, \quad T=2^K, \quad m=T-1.
\]

Because \(\sqrt N>p\ge53\), one has \(h\ge53\), \(b\ge5\), and
\(K\ge2\). From \(2^b\le h<2^{b+1}\),

\[
  \frac h{16}<T\le\frac h8.                         \tag{1.1}
\]

Since \(h>\sqrt N-1\),

\[
  m>\frac{\sqrt N-17}{16}.                          \tag{1.2}
\]

Balance gives

\[
 p<\sqrt N<q, \qquad
 p>\frac{\sqrt N}{\sqrt2}, \qquad
 q<\sqrt{2N}.                                       \tag{1.3}
\]

For either \(r\in\{p,q\}\), with \(\mu_r=m/r\), these imply

\[
  \frac1{32\sqrt2}<\mu_r<\frac{\sqrt2}{8}.          \tag{1.4}
\]

The lower bound uses \(r\le q<\sqrt{2N}\), (1.2), and
\(\sqrt N>34\). The sharper upper bounds are

\[
 \mu_p<\frac18\sqrt{\frac qp}<\frac{\sqrt2}{8},
 \qquad
 \mu_q<\frac18.
\]

No floor or endpoint case is lost.

For independent uniform \(a_1,\ldots,a_K\) modulo \(N\), define

\[
 L_S=\sum_{i\in S}a_i, \qquad
 Z_r=\#\{\varnothing\ne S\subseteq[K]:L_S=0\pmod r\}.
\]

Every nonempty incidence vector is nonzero. Two distinct \(0/1\) incidence
vectors cannot be scalar multiples over \(\mathbb F_r\): equal support would
be necessary, and an occupied coordinate then forces the scalar to be one.
Thus \((L_S,L_U)\) is uniform in \(\mathbb F_r^2\) for \(S\ne U\), and

\[
 \mathbb E Z_r=\mu_r, \qquad
 \operatorname{Var}(Z_r)=\mu_r\left(1-\frac1r\right).
\]

For \(E_r=\{Z_r>0\}\), Cauchy--Schwarz and the union bound give

\[
 \frac{\mu_r}{\mu_r+1-1/r}
 \le\Pr(E_r)\le\mu_r.                               \tag{1.5}
\]

Hence, writing \(\alpha_r=\Pr(E_r)\),

\[
 \frac1{32\sqrt2+1}<\alpha_r<\frac{\sqrt2}{8}.      \tag{1.6}
\]

This is a genuine second-moment union estimate; mutual independence of all
subset tickets is neither claimed nor needed.

## 2. CRT independence, exact gcd predicate, and Las Vegas scope

CRT is a bijection

\[
 \mathbb Z/N\mathbb Z \simeq \mathbb F_p\times\mathbb F_q.
\]

Exact uniform sampling modulo \(N\) therefore makes the entire local
\(p\)-vector independent of the entire local \(q\)-vector. Consequently
\(E_p\) and \(E_q\) are independent, and

\[
\begin{aligned}
 \Pr(E_p\mathbin\triangle E_q)
 &=\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p)\\
 &\ge
 \frac2{32\sqrt2+1}
 \left(1-\frac{\sqrt2}{8}\right)
 =:\delta>0.
\end{aligned}                                        \tag{2.1}
\]

For

\[
 Q_K=\prod_{\varnothing\ne S\subseteq[K]}L_S\pmod N,
\]

the integral-domain property of each local field gives

\[
 Q_K=0\pmod r \quad\Longleftrightarrow\quad E_r.
\]

Because the promise has exactly the two distinct factors \(p,q\),

\[
 1<\gcd(Q_K,N)<N
 \quad\Longleftrightarrow\quad
 E_p\mathbin\triangle E_q.                          \tag{2.2}
\]

Thus this is an exact local OR, with no additive cancellation.

Fresh trials are independent. Equation (2.1) bounds the expected trial count
by \(1/\delta\) and makes nontermination probability zero. Every returned gcd
is verified. Drawing \(n\)-bit strings and rejecting values at least \(N\)
accepts with probability at least one half for
\(n=\lceil\log_2(N+1)\rceil\). Thus \(K=O(n)\) residues use
\(O(n^2)\) expected random bits per trial. Integer square root, \(b,K\),
modular arithmetic, gcd, and exact division all have polynomial bit cost.

Accordingly, a deterministic uniform exact polynomial-bit evaluator, or a
Las Vegas exact evaluator with the same expected bound, yields the stated
promise factorer. It does not yield an all-input algorithm.

## 3. Meet-in-the-middle identity and signs

Partition \([K]=A\mathbin{\dot\cup}B\), with
\(|A|=\lfloor K/2\rfloor\) and
\(|B|=\lceil K/2\rceil\). For all half-subsets, including empty ones, put

\[
 x_U=\sum_{i\in U}a_i, \qquad y_V=\sum_{i\in V}a_i.
\]

Define

\[
 F_A(X)=\prod_{U\subseteq A}(X+x_U), \qquad
 Q_A=\prod_{\varnothing\ne U\subseteq A}x_U.
\]

Every nonempty full subset has a unique pair \((U,V)\). Separating
\(V=\varnothing\) proves

\[
 Q_K=Q_A\prod_{\varnothing\ne V\subseteq B}F_A(y_V). \tag{3.1}
\]

This identity is sign-free and division-free even when half sums coincide or
vanish.

For

\[
 P_A(X)=\prod_{U\ne\varnothing}(X+x_U), \qquad
 R_B(X)=\prod_{V\ne\varnothing}(X-y_V),
 \qquad m_B=2^{|B|}-1,
\]

the candidate's monic-first convention gives

\[
 \operatorname{Res}(R_B,P_A)
 =\prod_{V\ne\varnothing}P_A(y_V).
\]

Also \(P_A(0)=Q_A\) and
\(R_B(0)=(-1)^{m_B}\prod_{V\ne\varnothing}y_V\). Therefore

\[
 Q_K=(-1)^{m_B}P_A(0)R_B(0)
 \operatorname{Res}(R_B,P_A).                       \tag{3.2}
\]

The two signs cancel. The argument order and sign in the revision are correct.

## 4. Ring-safe uniform bit complexity

Let \(s=2^{\lceil K/2\rceil}\). Gray-code enumeration produces both
half-sum lists in \(O(s)\) modular additions. A balanced product tree builds
\(F_A\), a monic subproduct tree builds the point polynomial, and a remainder
tree evaluates \(F_A\) at all \(y_V\).

There is no hidden field division:

1. Every divisor in the remainder tree is monic.
2. Reversal changes a monic degree-\(d\) divisor into a polynomial with
   constant coefficient one.
3. Its truncated inverse exists over every commutative ring. Newton doubling
   \(h\mapsto h(2-gh)\) uses additions and multiplications only, since
   \(1-gh(2-gh)=(1-gh)^2\). It inverts neither two nor an unknown residue.
4. Fast quotient/remainder computation is therefore valid over
   \(\mathbb Z/N\mathbb Z\). Repeated points remain harmless because every
   leaf \(X-y_V\) is monic.

A uniform bit implementation follows by carry-safe Kronecker substitution.
Represent coefficients canonically in \([0,N)\). For a degree-at-most-\(d\)
product choose a power-of-two packing base with bit width

\[
 w\ge2n+\lceil\log_2(d+1)\rceil+2.
\]

Each integer convolution coefficient is below this base. Ordinary integer
multiplication therefore packs the polynomial product without cross-coefficient
carry; unpacking and coefficientwise reduction modulo \(N\) gives the exact
ring product. Packed operands have \(O(d(n+\log d))\) bits.

Using standard uniform fast integer multiplication at every tree level gives

\[
 \widetilde O\bigl(s\,\operatorname{poly}(n,K)\bigr)
\]

bit operations. Storing the tree levels and packed temporaries takes

\[
 \widetilde O\bigl(s(n+K)\bigr)
\]

bits. Here \(K\le n\), so the candidate's
\(\widetilde O(sn)\) display is valid. Since
\(2^K=\Theta(\sqrt N)\) and
\(s=\Theta(2^{K/2})\),

\[
 \text{time}=N^{1/4+o(1)}, \qquad
 \text{space}=N^{1/4+o(1)}.
\]

This validates the **bit** bound, not merely a ring-operation count. The
Gray-code alternative takes \(N^{1/2+o(1)}\) bit time and polynomial working
space.

The phrase `best explicit general evaluator in this report` is safely
qualified by `in this report`. No optimality among arbitrary evaluators is
proved.

## 5. Structural claims

For \(P=\operatorname{diag}(0,1)\), tensor-factor projections \(P_i\), and
\(P_0=(I-P)^{\otimes K}\), the operator

\[
 H_K=P_0+\sum_i a_iP_i
\]

has eigenvalue one on the empty state and \(L_S\) on every nonempty state.
Thus \(\det H_K=Q_K\). This is a succinct description of a
\(2^K\)-dimensional matrix, not a small determinant computation.

Over \(\mathbb Q(a_1,\ldots,a_K)\), the unmodified subset-sum diagonal has
\(2^K\) distinct eigenvalues and minimal-polynomial degree \(2^K\). This only
constrains representations required to retain the full spectrum.

For the direction-weighted \(K\)-cube, the Laplacian eigenvalues are
\(2L_S\). The matrix-tree theorem gives

\[
 \tau_K=\frac1{2^K}\prod_{S\ne\varnothing}2L_S
 =2^{2^K-K-1}Q_K.                                   \tag{5.1}
\]

The exponent is correct. This is an integral polynomial identity, so reduction
modulo odd \(N\) is valid and the power of two is a unit. The cofactor still
has dimension \(2^K-1\).

For \(a_i=u2^{i-1}\), nonempty subsets correspond bijectively to
\(1,\ldots,2^K-1\), and

\[
 Q_K=u^{2^K-1}(2^K-1)!\pmod N.                      \tag{5.2}
\]

This exact specialization loses the independent-uniform law and supplies no
general evaluator.

In characteristic zero the \(L_S\) are distinct nonassociate irreducible
linear forms. If nonzero \(G\) vanishes identically on every hyperplane
\(L_S=0\), then

\[
 Q_K\mid G, \qquad \deg G\ge2^K-1.
\]

The candidate correctly restricts the determinant consequence to bounded
entry degree and universal characteristic-zero vanishing. It does not
lower-bound high-degree short circuits, modular branching, or
characteristic-sensitive formulas. The displayed identity
\(Q_3=e_1e_3(e_1e_2-e_3)\) is correct.

If \(D_r\) counts distinct subset sums including the empty one and \(C_r\)
counts colliding unordered pairs, then \(T-D_r\le C_r\). Every pair collides
with probability \(1/r\), so

\[
 \mathbb E D_r\ge
 T-\binom T2\frac1r
 =T\left(1-\frac{T-1}{2r}\right).
\]

This is an expected literal-table-size statement, not concentration or a
compressed-state lower bound.

## 6. Optional Hurwitz prefix: the required correction

P30's raw residual construction gives a primitive Lipschitz quaternion

\[
 \widetilde\beta=x+yi+zj+wk,
 \qquad N\mid\operatorname{nrd}(\widetilde\beta),
\]

whose row and, separately, image line are conditionally uniform on

\[
 \mathcal S_r=
 \{[u:v]\in\mathbf P^1(\mathbb F_r):u^2+v^2\ne0\},
 \qquad
 s_r=r-\left(\frac{-1}{r}\right).
\]

A norm-\(N\) greatest common right divisor inherits the row; a greatest common
left divisor inherits the image. P30 does not assert that one arbitrarily
normalized norm-\(N\) output inherits both. P31 treats the opposite hand as a
different marginal. Thus Section 9's norm-\(N\) source description is not
licensed by the both-hand law it invokes.

Use two independent **raw** residual quaternions
\(\widetilde\beta,\widetilde\gamma\). Locally write their nonzero rank-one
matrices as

\[
 B=uv^{\mathsf T}, \qquad C=xy^{\mathsf T}.
\]

Then

\[
 \operatorname{tr}(BC)
 =(v^{\mathsf T}x)(y^{\mathsf T}u).
\]

Across independent calls, each cross-call row/image pair is independent
uniform on \(\mathcal S_r\). Orthogonal complement preserves
\(\mathcal S_r\), so each factor vanishes with probability \(1/s_r\). The
union bound gives

\[
 \Pr\bigl(r\mid
 \operatorname{trd}(\widetilde\beta\widetilde\gamma)\bigr)
 \le\frac2{s_r}.                                    \tag{6.1}
\]

No within-call row/image independence is used. For \(p,q\ge53\), nonunit
discard probability is at most

\[
 \frac2{s_p}+\frac2{s_q}\le\frac1{13},
\]

so \(K\) retained units require at most \(13K/12\) expected attempts.
Multiplication by fresh uniform \(\lambda_i\) then makes
\(a_i=\lambda_i c_i\) independent uniform residues conditional on all prior
history. Hence the optional conclusions survive the correction. Direct
sampling remains the cleaner theorem.

## 7. Classification and final decision

The terminal mechanism is correctly F02/P21-adjacent: an exponentially long
structured product has a useful local zero predicate, but no polylogarithmic
evaluator is supplied. F14/P30 is erasable provenance; P31 is unused by the
direct theorem. Unlike a polynomial union of rare F14 comparisons, this
Boolean norm aggregates exponentially many tickets and has a proved
constant-mass local event.

The report correctly excludes prime inputs, prime powers, repeated factors,
even composites, unbalanced semiprimes, composites with more factors,
recursive complete factorization, a polynomial evaluator, and any general
circuit lower bound. It therefore does not meet the top-level success
criterion in PROMPT.md.

**Final verdict: PASS WITH CORRECTIONS.** Correct or delete the norm-\(N\)
sentence in Section 9 as above. The main theorem and evaluator need no
substantive repair. A fresh strict proof-blind reconstruction is now
**warranted** for the corrected statement and key ideas.
