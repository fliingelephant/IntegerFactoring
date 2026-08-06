# F45 focused hostile audit

**Artifact audited:** experiments/F45_hadamard_paley_kill/RESULT.md

**Audit mode:** proof-only. I used no finite experiment or computational
number-theoretic evidence. I read the candidate in full and checked it against
PROMPT.md, the preregistered F09/F45 row in REGISTRY.md, P53, X47, and the
relevant durable scope. A byte-level presentation check found valid UTF-8 and no
ASCII control character other than ordinary line breaks.

## Verdict

**PASS.** I found no mathematical error, quantifier leak, hidden factoring
call, or unsupported all-input inference in the theorem as stated. No
mathematical amendment is required before the prescribed fresh proof-blind
reconstruction.

The pass is narrow in exactly the way the candidate says. Sections 4--6 concern
an accepted row only when its acceptance probability is positive; in the
stated balanced, fixed-constant polynomial-size regime this holds for all
sufficiently large inputs because \(m=O(n)\) while
\(p,q=2^{\Theta(n)}\). The exact finite formulas remain valid at \(m=p\),
but then there is no accepted conditional law and hence no accepted-row
protocol to which Sections 5--6 could apply. This is already excluded by the
candidate's asymptotic regime and by the premise that the protocol receives an
accepted row; it is not an additional theorem claim.

Likewise, the sequential theorem compares only the delivered one-bit transcript
after each source and word have been discarded. If a concrete implementation
samples raw residues and checks gcds, a proper-gcd outcome is a separate
absorbing factoring success. It must not be charged to the statistical hybrid.
The candidate gives its exact probability and explicitly makes this separation.

## 1. Normalization, duplicate coordinates, and local injectivity

After reduction modulo \(N\), two retained shifts are either equal modulo
\(N\) or have a nonzero difference modulo \(N\). Equal residues are collected.
For two distinct retained residues, the gcd of their difference with
\(N=pq\) is therefore \(1,p\), or \(q\); it cannot be \(N\). A proper gcd is
already a factor, and on the continuing branch the difference is a unit. Thus
the retained shifts are injective modulo both local fields.

The individual screening is necessary. Multiplying many differences before
taking one gcd could combine a \(p\)-collision and a \(q\)-collision into the
uninformative answer \(N\). The candidate instead screens every pair, which is
polynomial work for \(m=O(n)\).

Collecting global duplicates loses no information from the genuine extended or
accepted word: every duplicate occurrence is exactly a copy of the retained
coordinate. A test on the raw duplicated word can be pulled back along this
copying map. Under that pullback, a Walsh monomial can only lose degree because
repeated copies square to one; its degree cannot increase.

The warning about independently filling duplicates is correct. If two copies
of one zero coordinate received independent signs, their product would have
conditional expectation zero at the root, whereas away from the root it would
be one. Its unconditional mean would therefore be the nonzero probability,
not a squarefree two-shift character sum. That artificial law is not the
genuine transcript and is properly excluded.

## 2. Filled-zero identity and exact local coefficients

For a selected set \(S\), conditional on \(X\), if none of its coordinates is
zero then

\[
 \prod_{j\in S}W_j=\prod_{j\in S}Y_j.
\]

If at least one selected coordinate is zero, the product of filling signs
contains an independent centered sign. Its conditional expectation is zero,
as is the product of the corresponding \(Y_j\)'s. Hence

\[
 \mathbb E_\varepsilon\chi_S(W)=\prod_{j\in S}Y_j
\]

for every \(S\), including \(S=\varnothing\), \(|S|=1\), and \(|S|=2\).

For squarefree \(N=pq\), the extended Jacobi symbol factors pointwise as the
product of the two extended Legendre symbols, including at nonunits. CRT sends
uniform \(X\bmod N\) to independent uniform local coordinates. Therefore

\[
 c_S=\mathbb E\chi_S(W)=\frac{A_p(S)A_q(S)}{pq}
\]

exactly; no independence among coordinates of the word is being assumed.

Local injectivity makes
\(\prod_{j\in S}(u+a_j)\) squarefree over each field. The endpoint constants
are as follows.

* At \(t=1\), translation of the complete quadratic character sum gives
  \(A_r(S)=0\), hence \(c_S=0\).
* At \(t=2\), for distinct \(a_i,a_j\), the map
  \(u\mapsto (u+a_i)/(u+a_j)\) sends
  \(\mathbb F_r\setminus\{-a_j\}\) bijectively to
  \(\mathbb F_r\setminus\{1\}\). The square denominator disappears under the
  character, and the omitted pole contributes zero. Thus
  \(A_r(S)=\sum_{v\ne1}\chi_r(v)=-1\) and \(c_S=1/N\), not merely
  \(O(N^{-1/2})\).
* For squarefree degree \(t\ge2\), the quadratic Weil bound is

  \[
   |A_r(S)|\le(t-1)\sqrt r.
  \]

  For odd \(t\), this is the direct Hasse--Weil bound on the one-point-at-
  infinity hyperelliptic model. For even \(t\), monicity gives the sharper
  centered statement \(|A_r(S)+1|\le(t-2)\sqrt r\); since \(r\) is odd, it
  implies the displayed generic bound. The genus-zero case \(t=2\) agrees with
  the exact value above.

Multiplying the two local bounds and dividing by \(pq\) gives precisely

\[
 |c_S|\le\frac{(t-1)^2}{\sqrt N}.
\]

No Hasse--Weil constant or low-degree exception is missing.

## 3. Walsh normalization and exact chi-square identity

With uniform measure \(U_m\) on the cube and
\(L=d\mu/dU_m=2^m\mu\), the candidate uses the orthonormal Walsh convention

\[
 \widehat L(S)=\mathbb E_{U_m}[L\chi_S].
\]

This equals \(\mathbb E_\mu\chi_S=c_S\). Parseval and
\(\widehat L(\varnothing)=1\) therefore give, with no missing factor of
\(2^m\),

\[
 \chi^2(\mu\Vert U_m)
 =\mathbb E_{U_m}(L-1)^2
 =\sum_{S\ne\varnothing}c_S^2.
\]

The \(t=1\) contribution is zero, the exact \(t=2\) contribution is
\(\binom m2/N^2\), and the remaining contribution is bounded by

\[
 \frac1N\sum_{t=3}^m\binom mt(t-1)^4.
\]

The standard inequality
\(d_{\rm TV}(\mu,U_m)\le\tfrac12\sqrt{\chi^2(\mu\Vert U_m)}\)
then proves (3.3), and
\((t-1)^4\le m^4\) with at most \(2^m\) subsets proves (3.4).
For fixed \(\delta>0\), the latter is exponentially small when
\(m\le(1-\delta)n-O(\log n)\), using \(N\ge2^{n-1}\). It makes no useful
claim for general \(m=Cn\) with \(C\ge1\), exactly as stated.

## 4. Whole-word support lower bounds

A screened source has at most one local root index modulo \(p\) and at most
one modulo \(q\). Counting source/filling pairs, which is an upper bound on
the number of distinct output words, gives five cases:

\[
\begin{array}{c|c}
\text{local root pattern}&\text{number of filled outputs counted}\\ \hline
\text{no root}&(p-m)(q-m)\\
p\text{-root only}&2m(q-m)\\
q\text{-root only}&2m(p-m)\\
\text{same root index at both primes}&2m\\
\text{two different root indices}&4m(m-1).
\end{array}
\]

Their sum is

\[
 K_{\rm fill}=N+m(p+q)+m^2-2m.
\]

Since \(m\le p,q\),

\[
 \frac{K_{\rm fill}}N
 =1+\frac mp+\frac mq+\frac{m^2}{pq}-\frac{2m}{pq}<4.
\]

If a distribution is supported on at most \(K\) cube points, its total
variation distance from uniform is at least \(1-K/2^m\). This proves (3.6).
The same argument for the deterministic accepted word uses only its
\((p-m)(q-m)\) possible accepted sources and proves (4.5). Thus the candidate's
upper and lower support regimes are compatible: low-degree indistinguishability
does not imply whole-word pseudorandomness.

## 5. Acceptance, gcd partition, and conditioning

The \(m\) forbidden residues are distinct in each local field. Therefore

\[
 \alpha=\Pr(\mathcal A)
 =\frac{(p-m)(q-m)}{pq},
 \qquad
 \beta=1-\alpha
 =\frac mp+\frac mq-\frac{m^2}{N}.
\]

On \(\mathcal A\), no filling sign is used and \(W=Y\). The total-variation
distance between an unconditioned joint law and that law conditioned on an
event of probability \(\alpha>0\) is \(1-\alpha=\beta\); projection to the
word cannot increase it. Hence

\[
 d_{\rm TV}(\mu_{\rm acc},\mu)\le\beta.
\]

Equivalently, the direct convex decomposition of an expectation proves the
same bound for every \([0,1]\)-valued test. The coefficient is exact before
projection, although projection can make the inequality strict.

There are exactly \(m\) global residues \(X=-a_j\bmod N\) at which one gcd is
\(N\). Pairwise-unit differences force every other coordinate to be a unit on
those residues. Thus the single-trial outcomes are disjoint and have exact
probabilities

\[
 \alpha=\frac{(p-m)(q-m)}N,
 \qquad
 \rho=\frac mN,
 \qquad
 \sigma=1-\alpha-\rho
       =\frac{m(p+q-m-1)}N.
\]

Every point counted by \(\sigma\) gives at least one proper gcd, possibly at
two coordinates. Such a point is a factoring success. It is neither a
gcd-\(N\) rejection nor an error incurred by replacing an accepted word with a
uniform word.

## 6. Low-degree test bound and explicit bit-length constants

For a degree-\(D\) test \(f:\{-1,1\}^m\to[0,1]\), Fourier orthogonality gives

\[
 \mathbb E_\mu f-\mathbb E_{U_m}f
 =\sum_{1\le|S|\le D}\widehat f(S)c_S.
\]

No coefficient-count or \(\ell^1\) hypothesis is needed. Parseval gives

\[
 \sum_{S\ne\varnothing}\widehat f(S)^2
 =\operatorname{Var}_{U_m}(f),
\]

and a random variable in \([0,1]\) automatically has variance at most \(1/4\).
Cauchy--Schwarz therefore proves the exact \(L^2\) test bound

\[
 |\mathbb E_\mu f-\mathbb E_{U_m}f|\le R_D/2,
\]

and conditioning adds at most \(\beta\). For a randomized one-bit rule whose
success parameter is \(f(w)\), this expectation difference is exactly the TV
distance between the two Bernoulli output laws. Its equal-prior classification
excess is half that TV distance; the candidate keeps those two quantities
distinct.

Now \(n=\lceil\log_2(N+1)\rceil\) implies
\(2^{n-1}\le N<2^n\). Under \(m\le Cn\),
\(D\le n/(20\log_2 n)\), and \(n\ge\max(2,C+1)\),

\[
 \sum_{t=0}^D\binom mt\le(m+1)^D
 \le(n^2)^{n/(20\log_2 n)}=2^{n/10}.
\]

Also \(t\le D<n\), so \((t-1)^4\le n^4\). Consequently

\[
 R_D^2
 \le C^2n^2\,2^{1-2n}+n^4\,2^{1-9n/10},
\]

including the exact improvement for the two-coordinate terms.

From \(p<q<2p\) one has \(p>\sqrt{N/2}\) and \(q>\sqrt N\), so

\[
 \beta\le(1+\sqrt2)Cn\,2^{(1-n)/2}.
\]

The square-root term in \(R_D/2\) is asymptotically
\(2^{-9n/20+O(\log n)}\), while the conditioning term is
\(2^{-n/2+O_C(\log n)}\). Their sum is therefore exactly of the stated scale

\[
 \epsilon_{n,C}=2^{-9n/20+O_C(\log n)}.
\]

This is a uniform bound for every bounded degree-\(D\) rule, even one with
superpolynomially many nonzero Fourier coefficients. It is not a small-circuit
bound, and the candidate does not call it one.

## 7. Sequential accepted-row hybrid and direct factoring branches

Fix any common one-bit history and the public coins. The menu and test for the
next round are then fixed. A fresh accepted source has exactly the law audited
above, so the real and reference Bernoulli transition kernels differ in TV by
at most

\[
 \epsilon_i=\beta_i+R_{D_i}/2.
\]

The standard one-kernel-at-a-time hybrid compares both kernels at the same
history. Thus different histories in the two completed processes cause no
independence assumption, and

\[
 d_{\rm TV}(\mathcal L(B_1,\ldots,B_T),
             \mathcal L(\widetilde B_1,\ldots,\widetilde B_T))
 \le\sum_i\epsilon_i.
\]

When the uniform bounds on \(m_i,D_i\) hold for every realized history, this is
at most \(T\epsilon_{n,C}\), exponentially small for polynomial \(T\).

No direct factoring outcome is missing from this conditional statement. Its
round premise is that an accepted row is delivered. In a raw implementation,
each attempted source instead has the three-way partition in Section 5 above.
The proper-gcd branch must be represented by a separate absorbing success
symbol; it is not covered by the Bernoulli kernel comparison. The gcd-\(N\)
branch can be rejected and resampled. On the balanced \(m=O(n)\) family, the
proper-gcd probability per raw attempt is itself \(O_C(n/\sqrt N)\), but that
extra union bound would be a different unconditioned transcript theorem. The
candidate does not claim it and explicitly says that a proper gcd is success.

The hybrid also fails if a current or future rule receives \(X_i\), retains the
full word, makes several decisions from one word, adapts within one source, or
uses a high-degree/characteristic-order transform. In all those cases the
state contains information not coupled by the one-bit transition. Every one of
these exclusions is explicit in the candidate.

## 8. Prime powers and the HP-LR conditional reduction

For odd \(M=\prod_r r^{e_r}\) and any unit \(z\), the Jacobi definition gives

\[
 \left(\frac zM\right)=\prod_r\chi_r(z)^{e_r}
 =\prod_{e_r\ {\rm odd}}\chi_r(z).
\]

Thus even multiplicities vanish only from the sign component. They remain
visible as zero and gcd events. All-even exponents make \(M\) a perfect square;
a prime power is either prime or an exact perfect power; and a non-perfect-power
integer has gcd of prime exponents one, hence at least one odd exponent. The
candidate does not extrapolate the balanced-semiprime Walsh theorem to these
inputs. It separately assumes HP-LR for every odd composite non-perfect-power
input.

Under HP-LR, choose the decoder's prescribed integer
\(m\in[cn_M,Cn_M]\) and trial-divide through
\(B_0=\lceil2Cn_M^2\rceil\). A discovered proper divisor is an immediate
verified split. Otherwise every prime divisor \(r\) exceeds \(B_0>m\), so the
consecutive shifts are distinct modulo every \(r\). CRT across prime-power
components gives the exact acceptance probability

\[
 \alpha_M=\prod_{r\mid M}(1-m/r).
\]

There are fewer than \(n_M\) distinct prime divisors, and therefore

\[
 1-\alpha_M
 \le m\sum_{r\mid M}\frac1r
 \le\frac{Cn_M^2}{B_0}\le\frac12.
\]

The exact outcome refinement is also correct. There are \(m\) residues modulo
\(M\) at which one shifted value is zero modulo all of \(M\), so

\[
 \rho_M=m/M,
 \qquad
 \sigma_M=1-\alpha_M-\rho_M.
\]

Pairwise-unit differences ensure that a gcd-\(M\) coordinate cannot coexist
with another nonunit coordinate. Every point counted by \(\sigma_M\) therefore
produces at least one proper divisor, including on arbitrary prime powers and
repeated-factor inputs.

Exact uniform residues modulo \(M\), gcds, Jacobi symbols, and the
\(O(n_M^2)\) trial divisions all have polynomial bit complexity. Since
\(\alpha_M\ge1/2\), collecting at most \(n_M^B\) accepted rows takes polynomial
expected raw trials unless a proper gcd factors the node earlier. The retained
sources and full words contain polynomially many \(O(n_M)\)-bit data.

For a fresh attempted batch, either a proper gcd factors the node before the
batch is complete, or HP-LR is run on independent accepted rows. If \(u\) is
the probability of reaching the decoder, the probability that this attempt
returns a verified factor is at least

\[
 (1-u)+u n_M^{-A}\ge n_M^{-A}.
\]

Thus fresh attempts terminate almost surely and use at most \(n_M^A\) attempts
in expectation. Every proposed integer is checked for primality and exact
divisibility. A verified prime divisor is proper because the current \(M\) is
composite, so decoder errors can delay termination but can never corrupt the
factorization.

Even inputs are handled by recording the power of two. Prime nodes terminate
under deterministic primality testing. Exact perfect-power detection handles
\(M=a^k\) by recursively factoring \(a\) and multiplying exponents by \(k\).
Every other composite odd node satisfies the HP-LR premise. Verified splits
strictly reduce the integer arguments. The number of split/perfect-power nodes
is \(O(n)\) (and any coarser polynomial bound would suffice), while every local
expected cost is bounded by one fixed polynomial in the original input length.
Linearity of expectation gives a fixed polynomial total expected bit cost, and
the finite recursion together with geometric restarts gives almost-sure
termination.

Accordingly, HP-LR really would imply all-input classical Las Vegas factoring,
including arbitrary prime powers and repeated factors. This is only a
conditional implication. HP-LR already contains the missing uniform recovery
of a returned, labeled prime divisor with inverse-polynomial probability. The
candidate supplies no such decoder and makes no unconditional factoring claim.

## 9. Scope and evidence discipline

F45 is materially stronger than P53 only along its stated axis: Parseval gives
automatic \(L^2\) control of an arbitrary bounded low-Walsh-degree rule even
when its explicit Fourier support and coefficient \(\ell^1\)-norm are
superpolynomial. It does not promote P53's scalar mean bound into an arbitrary
decoder bound.

The proved object is a marginal hidden-\(X\) word. Conditional on a public
accepted \(X\), the word is deterministic, and no marginal coupling controls
the pair \((X,W)\). Whole-word closeness is asserted only in the support regime
where (3.4) is small. General \(m=Cn\), the retained full word, same-source
reuse, high Fourier degree, characteristic-order list recovery, and exact
symbolic transforms remain open. The balanced-semiprime theorem is not used as
an all-input theorem; Section 7 explicitly introduces a separate all-input
hypothesis.

The artifact is internally well presented: equations and section boundaries
are intact, no control-character corruption was found, and its proof-only
status is accurate. No computation ledger entry is required.
