# F45 — Hadamard--Paley word: exact Walsh law and the low-degree boundary

**Method:** proof-only kill-first analysis. No computation was used.

**Verdict:** the proposed word has an exact Walsh/Parseval obstruction, but only
after public shift normalization and only after averaging over a hidden source.
For a balanced distinct semiprime, every bounded decision rule of Walsh degree

\[
d\le {n\over20\log_2 n}
\]

has exponentially small bias on one fresh hidden-source accepted row, uniformly
even when its Fourier expansion has superpolynomial support. The same remains
true for a sequential protocol that immediately compresses each fresh row to one
bit and discards the source and word.

This does **not** kill the motivating Hadamard--Paley proposal. That proposal
retains the sampled \(x\), releases the full word, and asks for a high-order or
characteristic-order list-recovery decoder across rows. None of those operations
is covered here. No decoder and no factoring algorithm are obtained.

## 1. Shift normalization is mandatory

Let

\[
N=pq,
\qquad p<q<2p,
\]

where \(p,q\) are distinct odd primes. Start with an arbitrary public list of
integer shifts.

1. Reduce every shift modulo \(N\).
2. Collect equal residues and retain one coordinate for each distinct residue.
   The original extended or accepted word is recovered by copying that
   coordinate, so this loses no genuine transcript information.
3. For every two distinct retained shifts \(a_i,a_j\), compute
   \(\gcd(a_i-a_j,N)\). A proper gcd already factors \(N\). On the surviving
   branch every difference is a unit modulo \(N\), hence the shifts are distinct
   modulo both \(p\) and \(q\).

Write \(m\) for the number of retained shifts. The no-factor branch itself
implies \(m\le p,q\); in the balanced polynomial-size regime it has \(m<p,q\).

Deduplication cannot be omitted from the auxiliary filling argument. If two
equal occurrences are independently filled at a common zero, their filled
product has expectation equal to the probability that the underlying Jacobi
symbol is nonzero, which is close to one rather than Weil-small. Likewise, a
collision modulo just one unknown prime destroys squarefreeness locally. Thus
the theorem below applies to the normalized, difference-screened word, not to a
raw multiset with independently filled duplicate occurrences.

## 2. Extended word and exact filled Walsh coefficients

Draw \(X\) uniformly from \(\mathbb Z/N\mathbb Z\), and define the extended
word

\[
Y_j=\left({X+a_j\over N}\right)\in\{-1,0,1\},
\qquad 1\le j\le m.
\tag{2.1}
\]

Let \(\varepsilon_1,\ldots,\varepsilon_m\) be independent fair signs,
independent of \(X\), and fill each zero coordinate by

\[
W_j=Y_j+(1-Y_j^2)\varepsilon_j\in\{-1,1\}.
\tag{2.2}
\]

For \(S\subseteq[m]\), put \(\chi_S(w)=\prod_{j\in S}w_j\). Conditional on
\(X\), independence and centering of the filling signs give the exact identity

\[
\mathbb E_\varepsilon\chi_S(W)
=\prod_{j\in S}Y_j.
\tag{2.3}
\]

Indeed, if no selected coordinate is zero, both sides are the same product; if
at least one is zero, both sides have expectation zero. This includes every
nonempty \(S\), with no exception for one- or two-coordinate moments.

For \(r\in\{p,q\}\), extend the Legendre symbol by \(\chi_r(0)=0\), and set

\[
A_r(S)=\sum_{u\in\mathbb F_r}
 \chi_r\!\left(\prod_{j\in S}(u+a_j)\right).
\tag{2.4}
\]

CRT and (2.3) prove the exact Walsh-moment formula

\[
\boxed{
c_S:=\mathbb E\chi_S(W)={A_p(S)A_q(S)\over N}.}
\tag{2.5}
\]

The screened shifts make the polynomial in (2.4) squarefree over both fields.
Consequently:

- \(c_\varnothing=1\);
- if \(|S|=1\), then \(A_p(S)=A_q(S)=0\), hence
  \(\boxed{c_S=0}\);
- if \(|S|=2\), then the classical exact quadratic sum is
  \(A_p(S)=A_q(S)=-1\), hence
  \(\boxed{c_S=1/N}\);
- if \(t=|S|\ge2\), the squarefree character-sum bound gives

  \[
  |A_r(S)|\le(t-1)\sqrt r,
  \qquad
  \boxed{|c_S|\le{(t-1)^2\over\sqrt N}}.
  \tag{2.6}
  \]

For completeness, the exact \(t=2\) local sum follows by sending
\(u\ne-a_j\) to \((u+a_i)/(u+a_j)\): the image is
\(\mathbb F_r\setminus\{1\}\), and the quadratic character sums to \(-1\)
there. The exact \(1/N\) coefficient is substantially smaller than the generic
\(1/\sqrt N\) estimate.

## 3. Exact whole-word chi-square identity

Let \(\mu\) be the law of \(W\) on \(\{-1,1\}^m\), let \(U_m\) be uniform,
and let

\[
L(w)={d\mu\over dU_m}(w)=2^m\mu(w).
\]

Under the standard Walsh normalization,

\[
\widehat L(S)=\mathbb E_{U_m}L(W)\chi_S(W)=c_S.
\]

Parseval therefore gives the **exact** identity

\[
\boxed{
\chi^2(\mu\Vert U_m)
=\mathbb E_{U_m}(L-1)^2
=\sum_{\varnothing\ne S\subseteq[m]}c_S^2
=\sum_{\varnothing\ne S\subseteq[m]}
 {A_p(S)^2A_q(S)^2\over N^2}.}
\tag{3.1}
\]

Equations (2.5)--(2.6) imply

\[
\chi^2(\mu\Vert U_m)
\le {\binom m2\over N^2}
   +{1\over N}\sum_{t=3}^m\binom mt(t-1)^4,
\tag{3.2}
\]

and hence

\[
\boxed{
d_{\rm TV}(\mu,U_m)
\le {1\over2}
\left({\binom m2\over N^2}
   +{1\over N}\sum_{t=3}^m\binom mt(t-1)^4\right)^{1/2}.}
\tag{3.3}
\]

A convenient whole-word simplification is

\[
d_{\rm TV}(\mu,U_m)
\le {1\over2}
\left({\binom m2\over N^2}+{m^4 2^m\over N}\right)^{1/2}.
\tag{3.4}
\]

This is a valid marginal bound, but it is not uniformly useful throughout
\(m=\Theta(n)\). It is exponentially small, for example, when
\(m\le(1-\delta)n-O(\log n)\) for fixed \(\delta>0\). It gives no small bound
at the general \(m=Cn\) scale when \(C\ge1\).

There is also a direct support warning. For screened shifts, a source has zero
in at most two coordinates. Classifying its local root indices shows that the
filled law has support of size at most

\[
K_{\rm fill}
=(p-m)(q-m)
 +2\{m(q-m)+m(p-m)+m\}
 +4m(m-1)
=N+m(p+q)+m^2-2m<4N.
\tag{3.5}
\]

Therefore

\[
d_{\rm TV}(\mu,U_m)
\ge \max\left(0,1-{K_{\rm fill}\over2^m}\right).
\tag{3.6}
\]

In particular, once \(m\) exceeds the source bit length by a growing amount,
whole-word closeness is impossible. More fundamentally, (3.1)--(3.4) average
over a **hidden** \(X\). Conditional on a public \(X\), the word is usually a
point mass because zero coordinates are rare. Thus none of these equations is
a closeness statement for the pair \((X,W)\) or for a decoder allowed to use
the retained source.

## 4. The actually accepted no-zero word

Let

\[
\mathcal A=\{\gcd(X+a_j,N)=1\text{ for every }j\}.
\]

Because the shifts exclude \(m\) distinct residues modulo each prime, CRT gives

\[
\boxed{
\alpha:=\Pr(\mathcal A)
=\left(1-{m\over p}\right)\left(1-{m\over q}\right),
\qquad
\beta:=1-\alpha
={m\over p}+{m\over q}-{m^2\over N}.}
\tag{4.1}
\]

Let \(\mu_{\rm acc}\) be the law of the accepted word
\(Y\in\{-1,1\}^m\) conditional on \(\mathcal A\). Under the coupling already
defined, \(W=Y\) on \(\mathcal A\), so conditioning the joint law and then
projecting gives

\[
\boxed{d_{\rm TV}(\mu_{\rm acc},\mu)\le\beta.}
\tag{4.2}
\]

Equivalently, for every \(f:\{-1,1\}^m\to[0,1]\),

\[
|\mathbb E_{\mu_{\rm acc}}f-\mathbb E_\mu f|\le\beta.
\tag{4.3}
\]

This coefficient is exact at the level of the unprojected conditioning law:
writing the unconditional mean as
\(\alpha\mathbb E[f\mid\mathcal A]+\beta\mathbb E[f\mid\mathcal A^c]\)
proves (4.3) directly.

The gcd outcomes are also exact. Pairwise-unit differences imply that if one
coordinate has gcd \(N\), all other coordinates are units. Thus a single trial
has the three disjoint outcomes

\[
\begin{array}{c|c}
\text{outcome}&\text{probability}\\ \hline
\text{accepted no-zero word}&
\alpha={(p-m)(q-m)\over N}\\[2mm]
\gcd=N\text{ rejection}&
\rho={m\over N}\\[2mm]
\text{at least one proper gcd}&
\sigma=1-\alpha-\rho
={m(p+q-m-1)\over N}.
\end{array}
\tag{4.4}
\]

A proper gcd is a factoring success, not a statistical error term. A gcd of
\(N\) is only a rejection and must not be counted as success. Conditional on
delivery, the accepted source is uniform on the
\((p-m)(q-m)\) allowed CRT residues.

The accepted word is a deterministic function of that source, so independently
of the upper coupling bound,

\[
d_{\rm TV}(\mu_{\rm acc},U_m)
\ge \max\left(0,1-{(p-m)(q-m)\over2^m}\right).
\tag{4.5}
\]

This is another reason not to interpret the low-degree result below as
whole-word pseudorandomness.

## 5. Sharp low-degree expectation and decision bound

For an integer \(d\ge0\), put \(D=\min(d,m)\) and define the exact projected
likelihood radius

\[
R_D^2=\sum_{1\le|S|\le D}c_S^2.
\tag{5.1}
\]

If \(f:\{-1,1\}^m\to[0,1]\) has Walsh degree at most \(D\), then

\[
\mathbb E_\mu f-\mathbb E_{U_m}f
=\sum_{1\le|S|\le D}\widehat f(S)c_S.
\tag{5.2}
\]

There is no extra normalization hypothesis. Parseval and the range of \(f\)
automatically give

\[
\sum_{S\ne\varnothing}\widehat f(S)^2
=\operatorname{Var}_{U_m}(f)\le {1\over4}.
\tag{5.3}
\]

Consequently Cauchy--Schwarz gives the uniform norm-sharp estimate

\[
\boxed{
|\mathbb E_\mu f-\mathbb E_{U_m}f|
\le \sqrt{\operatorname{Var}_{U_m}(f)}\,R_D
\le {R_D\over2}.}
\tag{5.4}
\]

The first inequality is the exact Hilbert-space bound against the degree-\(D\)
projection of \(L-1\); equality is possible for an unrestricted centered
\(L^2\) test aligned with that projection. The final factor \(1/2\) is the
sharp universal variance bound for a \([0,1]\)-valued test.

For the accepted word, (4.3) adds only the conditioning cost:

\[
\boxed{
|\mathbb E_{\mu_{\rm acc}}f-\mathbb E_{U_m}f|
\le \beta+{R_D\over2}.}
\tag{5.5}
\]

If a randomized one-bit decision outputs \(1\) with probability \(f(w)\), the
left side of (5.4) or (5.5) is exactly the total-variation distance between
the two Bernoulli output laws. With equal priors, the excess classification
success over \(1/2\) is half that quantity.

The exact two-coordinate moment and the Weil bound yield

\[
R_D^2
\le
\mathbf 1_{D\ge2}{\binom m2\over N^2}
+{1\over N}\sum_{t=3}^D\binom mt(t-1)^4.
\tag{5.6}
\]

Now define the input bit length unambiguously by

\[
n=\lceil\log_2(N+1)\rceil.
\tag{5.7}
\]

For integer \(N\), this means

\[
\boxed{2^{n-1}\le N<2^n.}
\tag{5.8}
\]

Fix a constant \(C>0\), assume \(m\le Cn\), and suppose

\[
D\le {n\over20\log_2 n}.
\tag{5.9}
\]

The number of subsets of size at most \(D\) is at most \((m+1)^D\). For
\(n\ge\max(2,C+1)\), one has \(m+1\le n^2\), so

\[
(m+1)^D\le2^{n/10}.
\]

Using \((t-1)^4\le n^4\) and (5.8) in (5.6) gives the explicit bound

\[
\boxed{
R_D^2
\le C^2n^2\,2^{1-2n}
   +n^4\,2^{1-9n/10}.}
\tag{5.10}
\]

Balance also gives \(p>\sqrt{N/2}\) and \(q>\sqrt N\), whence

\[
\boxed{
\beta
\le (1+\sqrt2)mN^{-1/2}
\le(1+\sqrt2)Cn\,2^{(1-n)/2}.}
\tag{5.11}
\]

Combining (5.5), (5.10), and (5.11), every accepted-row decision in this
class has advantage at most

\[
\boxed{
\epsilon_{n,C}
=(1+\sqrt2)Cn\,2^{(1-n)/2}
+{1\over2}\sqrt{
 C^2n^2\,2^{1-2n}+n^4\,2^{1-9n/10}}
=2^{-9n/20+O_C(\log n)}.}
\tag{5.12}
\]

This conclusion assumes Walsh degree. It cannot be inferred from circuit size:
a small circuit may compute a degree-\(m\) parity/product or perform
characteristic-order processing, while a degree-\(D\) function may have
superpolynomially many nonzero Fourier coefficients.

## 6. Correct sequential hybrid

Consider \(T\) rounds. In round \(i\), after seeing the previous **one-bit**
transcript and public randomness, a protocol may choose a screened shift menu
and a function

\[
f_{i,h}:\{-1,1\}^{m_i}\to[0,1]
\]

of Walsh degree at most \(d_i\). It then receives a fresh independently sampled
accepted row whose source \(X_i\) is hidden, outputs a fresh Bernoulli bit with
success probability \(f_{i,h}(W_i)\), and discards both \(X_i\) and the row.
Let the reference protocol instead use a fresh uniform sign word in each round,
with the same past-adaptive rule.

For every fixed history \(h\), (5.5) bounds the total variation between the two
conditional Bernoulli transition kernels by

\[
\epsilon_i=\beta_i+R_{D_i}/2.
\]

Replacing the kernels one at a time gives the standard pathwise hybrid

\[
\boxed{
d_{\rm TV}\bigl(\mathcal L(B_1,\ldots,B_T),
                 \mathcal L(\widetilde B_1,\ldots,\widetilde B_T)\bigr)
\le\sum_{i=1}^T\epsilon_i.}
\tag{6.1}
\]

The conditioning is on the same history in each hybrid transition, so past
adaptivity causes no independence error. In the uniform regime of (5.12), the
right side is at most \(T\epsilon_{n,C}\), still exponentially small for
polynomial \(T\).

The restrictions in this statement are essential. It does not cover:

- a current test that sees or later retains \(X_i\);
- release or retention of the full row as protocol state;
- several adaptive decisions on one source or one retained row;
- a high-degree or characteristic-order decoder;
- exact symbolic transforms of the full word.

If a row is retained, future transition rules can use arbitrary high-degree
information about it, and the one-bit kernel hybrid no longer describes the
protocol. Freshness alone does not repair that mismatch.

## 7. Prime-power multiplicities and a conditional all-input reduction

The preceding Walsh theorem is for a balanced distinct semiprime. An all-input
factoring claim needs a separate decoder theorem. The Jacobi multiplicity audit
shows exactly what such a theorem would have to handle.

Let

\[
M=\prod_{r\mid M}r^{e_r}
\]

be odd. At a unit \(z\),

\[
\boxed{
\left({z\over M}\right)
=\prod_{r\mid M}\chi_r(z)^{e_r}
=\prod_{e_r\text{ odd}}\chi_r(z).}
\tag{7.1}
\]

Thus an odd prime-power multiplicity contributes one local Paley word, whereas
an even multiplicity contributes no sign at all. Every prime divisor, regardless
of multiplicity, still contributes zeros and gcd events.

Consequences:

- if every \(e_r\) is even, \(M\) is a square and the accepted Jacobi word is
  the constant \(+1\) word;
- for \(p^e\), the accepted word is the local Paley word when \(e\) is odd and
  constant \(+1\) when \(e\) is even;
- on a mixed input such as \(p^2q\), the sign word sees \(q\) but not \(p\);
  recovering \(q\) still gives a valid split, after which recursion can handle
  \(p^2\);
- a decoder that merely recovers an unlabeled sign pattern, without an integer
  modulus or another verifiable proper-divisor witness, is insufficient for a
  Las Vegas reduction.

Here is the precise missing assumption under which an all-input reduction would
be valid.

> **HP-LR decoder hypothesis.** There are fixed constants \(c,C,A,B>0\) and a
> specified uniform randomized algorithm \(\mathcal D\) with polynomial bit
> complexity such that the following holds for every odd, composite,
> non-perfect-power \(M\). With \(n_M=\lceil\log_2(M+1)\rceil\), use
> \(cn_M\le m\le Cn_M\) public consecutive shifts and give \(\mathcal D\) at
> most \(n_M^B\) independent accepted rows, including each retained source
> \(x_i\) and the full Jacobi word. The algorithm outputs a list of at most
> \(n_M^B\) pairs \((r,V^{(r)})\). With probability at least \(n_M^{-A}\), the
> list contains some prime \(r\mid M\) of odd exponent together with its
> correctly labeled local word
> \(V^{(r)}_{i,j}=\chi_r(x_i+j)\). In particular, the returned integer \(r\)
> is available for deterministic divisibility and primality verification.

This is an explicitly quantified high-order list-recovery interface, not a
consequence of the low-degree theorem. No such decoder is supplied here.

Conditional on HP-LR, accepted transcripts can be generated in expected
polynomial time on every remaining node. Trial-divide first through

\[
B_0=\lceil2Cn_M^2\rceil.
\]

If no divisor is found, every prime divisor of \(M\) exceeds \(B_0>m\), so the
consecutive shifts are automatically pairwise distinct modulo every prime. For
uniform \(X\bmod M\), CRT over the distinct prime-power components gives

\[
\Pr(\text{accepted})
=\prod_{r\mid M}\left(1-{m\over r}\right).
\tag{7.2}
\]

There are fewer than \(n_M\) distinct prime divisors. A union bound therefore
gives

\[
\Pr(\text{rejected or gcd-success})
\le m\sum_{r\mid M}{1\over r}
\le {Cn_M^2\over B_0}\le{1\over2},
\]

so (7.2) is at least \(1/2\). More exactly, after pairwise-unit screening the
three outcomes for arbitrary \(M\) are

\[
\alpha_M=\prod_{r\mid M}(1-m/r),
\qquad
\rho_M={m\over M},
\qquad
\sigma_M=1-\alpha_M-\rho_M,
\tag{7.3}
\]

where \(\rho_M\) is gcd-\(M\) rejection and \(\sigma_M\) is at least one proper
gcd and hence immediate success. Thus collecting a polynomial number of rows
either factors early or costs only polynomial expected time.

The conditional all-input Las Vegas algorithm is then:

1. use deterministic primality testing and strip powers of \(2\);
2. detect exact perfect powers; if \(M=a^k\), factor \(a\) recursively and
   multiply the recovered prime multiplicities by \(k\);
3. trial-divide through \(B_0\), then generate fresh accepted batches as above;
4. run \(\mathcal D\), verify every proposed \(r\) by primality testing and
   exact divisibility, and repeat fresh batches until a verified proper factor
   appears;
5. recurse on the verified factor and quotient.

After perfect-power removal, the gcd of the prime exponents is one, so at least
one exponent is odd; HP-LR therefore applies. Even-multiplicity components may
remain invisible in the current sign word, but an odd component supplies the
split and recursion exposes the rest. Prime powers are already handled by exact
perfect-power reduction. Every proposed split is verified, inverse-polynomial
decoder success gives polynomial expected batches, and a factor tree has
\(O(n)\) nodes. Hence this would be a classical all-input Las Vegas
polynomial-time factorization.

The implication is only bookkeeping around HP-LR. The hypothesis contains the
missing characteristic-order recovery of a labeled prime component with
inverse-polynomial success; replacing it by an unspecified "list decoder," by a
decoder for balanced semiprimes only, or by an unlabeled recovered word does not
yield the all-input conclusion.

## 8. Closest prior result and final classification

The closest proved result is P53. P53 controls one shifted-Jacobi product, an
explicit polynomial-\(\ell_1\) linear combination of such products, or one
fresh compressed scalar per adaptive round. F45 differs materially because one
bounded degree-\(d\) rule on a jointly released \(m\)-bit word can have
superpolynomially many Fourier monomials and no polynomial \(\ell_1\) bound.
The exact filled-word Fourier law plus Parseval replaces that missing
\(\ell_1\) control by automatic \(L^2\) control.

**Classification:** rigorous partial obstruction, not family closure. F45 kills
every fresh-hidden-source, immediate, bounded low-Walsh-degree decision channel
in the stated balanced-semiprime regime, including past-adaptive sequences of
such one-bit channels. It leaves public or retained \(x\), full-word release,
same-source reuse, high-degree/characteristic-order decoding, exact symbolic
transforms, and actual product-code list recovery open. The conditional
all-input reduction becomes valid only under HP-LR, which is precisely the
unproved algorithmic core.
