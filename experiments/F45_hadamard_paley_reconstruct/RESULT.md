# F45 proof-blind reconstruction

## Verdict

**PASS for the stated analytic claims and for the conditional reduction.** No formula below needs repair. This is not an unconditional factoring theorem: the HP-LR decoder in Section 7 is an explicit missing hypothesis, and none of the moment estimates constructs it.

There is one necessary domain condition. Pairwise screening implies only \(m\le p<q\). The accepted distribution exists only when

\[
\alpha=(1-m/p)(1-m/q)>0,
\]

equivalently here \(m<p\). If \(m=p\), every residue modulo \(p\) is forbidden and acceptance has probability zero. The asymptotic balanced-semiprime regime has \(m<p\), and the all-input conditional reduction enforces the analogous condition by trial division before sampling.

## 1. Screening and the filled word

Normalize the public shifts to distinct elements \(a_1,\ldots,a_m\in\mathbb Z/N\mathbb Z\). For every \(j\ne k\), compute

\[
g_{jk}=\gcd(a_j-a_k,N).
\]

A value \(1<g_{jk}<N\) is already a factor. The case \(g_{jk}=N\) cannot remain after normalization and deduplication. Hence, on the no-factor branch,

\[
\gcd(a_j-a_k,N)=1\qquad(j\ne k).
\]

For \(N=pq\), this makes the shifts injective modulo both \(p\) and \(q\), and consequently \(m\le p,q\). This screening uses only public shifts and gcds with \(N\), not either hidden prime.

Let \(X\) be uniform modulo \(N\), and write

\[
Y_j=\left(\frac{X+a_j}{N}\right)\in\{-1,0,1\}
\]

for the Jacobi symbol. Whenever \(Y_j=0\), replace that coordinate by its own independent fair sign; leave nonzero coordinates unchanged. Denote the resulting word by \(W\in\{\pm1\}^m\). Independence of all the filling signs is essential.

For \(S\subseteq[m]\), put \(t=|S|\), \(F_{r,S}(u)=\prod_{j\in S}(u+a_j)\) over \(\mathbb F_r\), and

\[
A_r(S)=\sum_{u\in\mathbb F_r}\chi_r(F_{r,S}(u)),
\]

where \(\chi_r(0)=0\). Conditional on \(X\), if a coordinate in \(S\) is zero, the independent filling coin makes the conditional product mean zero; otherwise the product is the product of the Jacobi signs. Thus in all cases

\[
\mathbb E\!\left[\prod_{j\in S}W_j\mid X\right]
=\prod_{j\in S}\left(\frac{X+a_j}{N}\right).
\]

The CRT and multiplicativity of the Jacobi symbol now give, including all zero cases,

\[
\boxed{
c_S:=\mathbb E\prod_{j\in S}W_j
=\frac{A_p(S)A_q(S)}{N}.}
\]

For \(S=\varnothing\), this reads \(c_\varnothing=1\), since \(A_p(\varnothing)=p\) and \(A_q(\varnothing)=q\).

## 2. Endpoint values and the Weil estimate

For \(t=1\), a translate permutes the field and the nontrivial quadratic character sums to zero. Hence

\[
A_p(S)=A_q(S)=0,\qquad \boxed{c_S=0}.
\]

For \(t=2\), the two roots are distinct modulo each prime. For any odd prime \(r\) and distinct \(a,b\pmod r\),

\[
\sum_u\chi_r((u+a)(u+b))=-1.
\]

One elementary verification counts the pairs \((u,z)\) satisfying \(z^2=(u+a)(u+b)\). After an invertible affine change, this is a difference-of-squares equation whose two factors have fixed nonzero product; it has \(r-1\) solutions. On the other hand its number of solutions is \(r+\sum_u\chi_r((u+a)(u+b))\). Therefore the sum is \(-1\). It follows that

\[
A_p(S)=A_q(S)=-1,\qquad \boxed{c_S=1/N}.
\]

For every nonempty \(S\), injectivity of the shifts makes \(F_{r,S}\) squarefree. The squarefree quadratic-character Weil bound gives

\[
|A_r(S)|\le (t-1)\sqrt r.
\]

Consequently

\[
\boxed{|c_S|\le \frac{(t-1)^2}{\sqrt N}.}
\]

This includes the exact zero bound at \(t=1\), while at \(t=2\) the exact value \(1/N\) is much sharper than the generic \(1/\sqrt N\) estimate.

## 3. Exact Walsh--Parseval identity and whole-word bounds

Let \(\mu\) be the law of \(W\), let \(U\) be uniform on \(\{\pm1\}^m\), and let

\[
\psi_S(w)=\prod_{j\in S}w_j.
\]

For the density \(g=d\mu/dU=2^m\mu(w)\), its normalized Walsh coefficient is

\[
\widehat g(S)=\mathbb E_U[g\psi_S]=\mathbb E_\mu\psi_S=c_S.
\]

Walsh inversion and Parseval therefore give the exact identities

\[
g=\sum_{S\subseteq[m]}c_S\psi_S,
\]

and

\[
\boxed{
\chi^2(\mu\Vert U)
:=\mathbb E_U[(g-1)^2]
=\sum_{\varnothing\ne S\subseteq[m]}c_S^2.}
\]

Define

\[
K_{m,N}:=\frac{\binom m2}{N^2}
+\frac1N\sum_{t=3}^m\binom mt(t-1)^4,
\]

with empty sums interpreted as zero. The endpoint values and Weil bound imply

\[
\chi^2(\mu\Vert U)\le K_{m,N},
\]

so Cauchy--Schwarz yields the whole-word upper bound

\[
\boxed{
d_{\rm TV}(\mu,U)
\le \frac12\sqrt{\sum_{S\ne\varnothing}c_S^2}
\le \frac12\sqrt{K_{m,N}}.}
\]

There is also a useful support obstruction. For any distribution supported on \(K\) words,

\[
1+\chi^2(\mu\Vert U)=2^m\sum_w\mu(w)^2\ge \frac{2^m}{K}.
\]

Thus

\[
|\operatorname{supp}\mu|\ge \frac{2^m}{1+\chi^2(\mu\Vert U)}
\ge \frac{2^m}{1+K_{m,N}}.
\]

In the other direction, the generative construction has small support. For a fixed \(X\), at most one coordinate vanishes modulo \(p\) and at most one modulo \(q\). Counting CRT residue types gives

\[
\begin{array}{c|c|c}
\text{root pattern}&\text{number of }X&\text{number of fills}\\ \hline
\text{neither}&(p-m)(q-m)&1\\
\text{\(p\)-root only}&m(q-m)&2\\
\text{\(q\)-root only}&m(p-m)&2\\
\text{same index at \(p,q\)}&m&2\\
\text{different indices at \(p,q\)}&m(m-1)&4.
\end{array}
\]

The resulting pairs \((X,\text{fill})\) can collide in their output word, so this is an upper bound, not an equality:

\[
\boxed{
|\operatorname{supp}\mu|
\le L_{m,p,q}:=N+m(p+q)+m^2-2m
\le 4N.}
\]

Combining support with the variational characterization of TV gives

\[
\boxed{
\max\!\left\{0,1-\frac{L_{m,p,q}}{2^m}\right\}
\le d_{\rm TV}(\mu,U)
\le \min\!\left\{1,\frac12\sqrt{K_{m,N}}\right\}.}
\]

This explains why the low-degree result below must not be promoted to full-word pseudorandomness: when \(2^m\gg N\), the support bound itself makes the full word statistically distinguishable.

## 4. Acceptance and the exact gcd partition

Let

\[
\mathcal A=\{\gcd(X+a_j,N)=1\text{ for every }j\}.
\]

There are \(m\) forbidden residues modulo each prime, independently under CRT, so

\[
\boxed{
\alpha:=\Pr(\mathcal A)=(1-m/p)(1-m/q),
\qquad
\beta:=1-\alpha=\frac{m(p+q-m)}N.}
\]

When \(\alpha>0\), let \(\mu_{\rm acc}\) be the law of \(W\mid\mathcal A\). Conditioning the joint law of \((X,W)\) changes it in TV by exactly \(1-\alpha\), and marginalization cannot increase TV. Equivalently, write the unconditioned word law as

\[
\mu=\alpha\mu_{\rm acc}+\beta\mu_{\rm rej}.
\]

It follows that

\[
\boxed{d_{\rm TV}(\mu_{\rm acc},\mu)\le\beta.}
\]

The rejected sources have an exact, factor-relevant partition. A gcd equal to \(N\) occurs exactly when \(X=-a_j\pmod N\) for one of the \(m\) distinct shifts, so

\[
\boxed{\rho=\Pr(\text{some gcd is }N)=m/N.}
\]

If this occurs at index \(j\), every other coordinate is a unit by difference screening. Every other rejection has at least one proper gcd, and hence produces a factor. Therefore

\[
\boxed{
\sigma=\Pr(\text{proper-gcd success})
=\beta-\rho
=\frac{m(p+q-m-1)}N.}
\]

Thus \(\alpha+\rho+\sigma=1\) exactly.

## 5. Bounded low-degree decisions

Let \(f:\{\pm1\}^m\to[0,1]\) have Walsh degree at most the integer \(D\), and write

\[
f=\sum_S\widehat f(S)\psi_S,
\qquad
\widehat f(S)=\mathbb E_U[f\psi_S].
\]

Set

\[
R_D^2=\sum_{1\le |S|\le D}c_S^2.
\]

Then

\[
\mathbb E_\mu f-\mathbb E_U f
=\sum_{1\le|S|\le D}\widehat f(S)c_S.
\]

The nonconstant Fourier energy is

\[
\sum_{S\ne\varnothing}\widehat f(S)^2
=\operatorname{Var}_U(f)\le\frac14,
\]

because \(0\le f\le1\). Cauchy--Schwarz, followed by the conditioning bound, proves

\[
\boxed{
|\mathbb E_{\mu_{\rm acc}}f-\mathbb E_Uf|
\le \beta+\frac{R_D}{2}.}
\]

This uses neither a Fourier-\(\ell_1\) hypothesis nor a support-size hypothesis. The factor \(1/2\) comes from the variance bound for a bounded scalar function.

Here is an explicit uniform asymptotic form. With

\[
n=\lceil\log_2(N+1)\rceil,
\]

one has \(2^{n-1}\le N\le2^n-1\). Balance gives \(p>\sqrt{N/2}\), and hence, for \(m\le Cn\),

\[
\beta\le \frac{2\sqrt2\,m}{\sqrt N}
\le 4Cn\,2^{-n/2}.
\]

For \(D\le n/(20\log_2n)\), the endpoint and Weil estimates give

\[
R_D^2
\le \frac{m^2}{2N^2}+\frac{D^5m^D}{N}.
\]

Indeed, the first term bounds the \(t=2\) contribution, while for \(3\le t\le D\) there are at most \(D\) values of \(t\), each coefficient square is at most \(D^4/N\), and each \(\binom mt\le m^D\).

Define

\[
n_0(C)=\left\lceil\max\left\{16,C,4\bigl(1+\log_2\max\{1,C\}\bigr)\right\}\right\rceil.
\]

For \(n\ge n_0(C)\), \(m\le n^2\), \(D^5\le n^5\), and

\[
m^D\le(n^2)^D\le2^{n/10}.
\]

Using \(N\ge2^{n-1}\),

\[
R_D^2\le4n^5\,2^{-9n/10},
\qquad
\frac{R_D}{2}\le n^{5/2}2^{-9n/20}.
\]

Also, \(2^{n/4}\ge n\) for \(n\ge16\), while the last term in \(n_0(C)\) makes \(2^{n/4-1}\ge C\). Since

\[
p>2^{(n-2)/2}=2^{n/4}2^{n/4-1},
\]

this range automatically has \(m<p\), so acceptance is positive.

For a bound valid at every finite \(n\) for which \(\mu_{\rm acc}\) is defined, put

\[
K_C=1+4C+2^{9n_0(C)/20}
\]

and

\[
\boxed{
\varepsilon_{n,C}
=\min\left\{1,K_Cn^{5/2}2^{-9n/20}\right\}.}
\]

For \(n\ge n_0(C)\), the displayed estimates are dominated by the second argument of this minimum. For \(n<n_0(C)\), that argument is at least one, and the trivial bound applies. Therefore

\[
|\mathbb E_{\mu_{\rm acc}}f-\mathbb E_Uf|\le\varepsilon_{n,C},
\]

uniformly over the shifts and \(f\) subject to the stated hypotheses. For fixed \(C\),

\[
\varepsilon_{n,C}=2^{-9n/20+O_C(\log n)}
\]

in the nontrivial asymptotic range.

## 6. The exact sequential consequence, and nothing stronger

Consider a sequential protocol in which round \(i\):

1. draws a fresh, independent accepted hidden-source row;
2. computes, possibly as a function of the previous released bits, a function \(f_{i,h}:\{\pm1\}^{m_i}\to[0,1]\) satisfying the same degree bound for every possible history \(h\);
3. releases one Bernoulli bit of parameter \(f_{i,h}(W_i)\); and
4. discards both the source \(X_i\) and the word \(W_i\).

Compare this with the protocol using a fresh uniform word in every round and the same history-dependent rule. At every common history, the two next-bit Bernoulli parameters differ by at most \(\varepsilon_i\). TV between Bernoulli laws is exactly the absolute parameter difference. A kernel hybrid, replacing one round at a time, therefore gives

\[
\boxed{
d_{\rm TV}(\text{real transcript},\text{uniform-word transcript})
\le\sum_i\varepsilon_i.}
\]

There is no additional factor \(1/2\) at this step: that factor has already entered through \(\operatorname{Var}_U(f)\le1/4\), whereas Bernoulli TV equals \(|p-q|\). Deterministic binary classification is the special case \(f\in\{0,1\}\).

The proof deliberately excludes all of the following.

- **Retaining \(X\).** Marginal control of \(W\) says nothing about the joint pair \((X,W)\); conditional on a source, the word has only the zero-filling randomness.
- **Releasing the full word.** Its support is at most \(4N\), and the full-word TV can be close to one.
- **Reusing one source or making several decisions from one word.** After an earlier same-word decision, the conditional law of the word changes. A later conditional probability is generally a ratio of Fourier expressions and need not retain the original degree bound. Equivalently, a joint output event may have much higher degree.
- **High- or characteristic-order degree.** The low-degree count is exactly what makes \(R_D\) small. A characteristic-order list decoder need not be low degree.
- **Exact transforms.** Exact symbolic, Walsh, correlation, or list-recovery transforms can expose a many-bit or high-degree statistic. Computational exactness is not a low-degree hypothesis.
- **Raw proper-gcd branches.** The theorem conditions on acceptance. A raw proper-gcd event actually reveals a divisor and is not simulated by a uniform word. The gcd-\(N\) discard branch is likewise a separate branch of the sampler.

## 7. Arbitrary odd composites and the conditional HP-LR reduction

Let

\[
M=\prod_{r\mid M}r^{e_r}
\]

be odd. On a unit \(z\),

\[
\left(\frac zM\right)
=\prod_{r\mid M}\left(\frac zr\right)^{e_r}
=\prod_{r:\ e_r\text{ odd}}\left(\frac zr\right).
\]

Thus an accepted shifted-Jacobi word is exactly the coordinatewise product of the local Paley words belonging to odd-exponent primes. Even-exponent prime components disappear from the signs. In contrast, the Jacobi symbol is zero whenever any prime divisor of \(M\) divides \(z\), and \(\gcd(z,M)\) detects such divisibility regardless of exponent. This is the precise sense in which signs retain exactly the odd-exponent components while zeros and gcds see all components.

The missing algorithm can be isolated as follows.

### HP-LR decoder hypothesis

There exist fixed polynomials \(L,Q,T\) and a uniform randomized algorithm \(\mathsf{Dec}\) with the following property. For an input of bit length \(k\), set

\[
m(k)=k,\qquad B_0(k)=4k^2,
\]

and use the public shifts \(a_j=j-1\), \(1\le j\le k\). For every odd, composite, non-perfect-power \(M\) of bit length \(k\) whose prime divisors all exceed \(B_0(k)\), give \(\mathsf{Dec}\) the following \(L(k)\) independent full accepted rows with their retained sources:

\[
\left(X_i,
\left(\left(\frac{X_i+a_j}{M}\right)\right)_{j=1}^{k}
\right),
\]

where each \(X_i\) is uniform conditional on all shifted values being units. The decoder runs in at most \(T(k)\) bit operations and, with probability at least \(1/Q(k)\) over both the rows and its coins, returns a labeled integer \(r\) such that

\[
r\text{ is prime},\qquad r\mid M,\qquad v_r(M)\text{ is odd}.
\]

It receives neither the factorization of \(M\) nor any hidden prime. “Labeled” must include the numerical divisor \(r\); returning only an abstract local codeword is insufficient for factoring. The restriction on small primes is not a promise on the original factoring input: deterministic trial division below handles that complementary case before the decoder is invoked. Without such preprocessing, \(m\ge r\) could make acceptance impossible.

This is an explicit, theorem-strength hypothesis. No construction of \(\mathsf{Dec}\) has been supplied here.

### Exact sampler partition for general \(M\)

After trial division, all \(r>B_0(k)>m(k)\), so the consecutive shifts are distinct modulo every prime divisor and all pairwise differences are units modulo \(M\). For uniform \(X\pmod M\), CRT across the prime-power factors gives

\[
\boxed{
\alpha_M=\Pr(\text{all shifts are units})
=\prod_{r\mid M}(1-m/r).}
\]

As before, a gcd equal to \(M\) occurs exactly at one of the \(m\) sources \(X=-a_j\pmod M\). Difference screening makes every other shifted value a unit there. Hence the three exhaustive events have probabilities

\[
\boxed{
\Pr(A)=\alpha_M,
\qquad
\Pr(G_M)=m/M,
\qquad
\Pr(G_{\rm proper})=1-\alpha_M-m/M.}
\]

Here \(G_{\rm proper}\) means that at least one shifted gcd lies strictly between \(1\) and \(M\). This partition remains exact with prime powers and repeated factors.

The number of distinct prime divisors is at most \(k\). Therefore

\[
\alpha_M
\ge1-\sum_{r\mid M}\frac mr
>1-\frac{k\,m}{4k^2}
=\frac34.
\]

So accepted rows can be sampled with constant expected overhead, without knowing any factor.

### Conditional Las Vegas algorithm

On an arbitrary input \(N\ge2\), recursively do the following.

1. Remove the complete power of \(2\). At every odd subproblem of bit length \(k\), trial-divide by every prime at most \(B_0(k)=4k^2\), removing and recording its full exponent. This is polynomial bit complexity. Replace the subproblem by the remaining cofactor; if it is \(1\), return the recorded factors. Otherwise recompute its bit length. Its surviving primes still exceed the new cutoff.
2. Apply deterministic polynomial-time primality testing to the remaining cofactor. If it is prime, record it.
3. Deterministically test exact \(e\)-th powers for \(2\le e\le k\), using integer-root computation followed by exact exponentiation. If \(M=b^e\), recursively factor \(b\) and multiply every returned exponent by \(e\). This handles prime powers and every composite for which all prime exponents have a common divisor.
4. The remaining case is odd, composite, and not a perfect power, with every prime divisor greater than \(B_0(k)\). Start a fresh decoder attempt using \(m=k\) consecutive shifts. Draw exact uniform sources \(X\pmod M\). For each source compute every \(g_j=\gcd(X+a_j,M)\):
   - if some \(1<g_j<M\), return that verified proper divisor immediately;
   - if some \(g_j=M\), discard the source;
   - otherwise retain \(X\) and its full Jacobi word as one accepted row.
   After \(L(k)\) accepted rows, run \(\mathsf{Dec}\). Accept its output only after checking \(1<r<M\), \(r\mid M\), deterministic primality of \(r\), and that repeated division gives odd \(v_r(M)\). On any failure, discard the batch and restart with fresh rows and coins.
5. Recursively factor the verified divisor and its cofactor, and aggregate equal primes and their exponents. A proper gcd is allowed to be composite; recursion handles it.

All arithmetic above is factor-free until a gcd or verified decoder output actually exposes a divisor. Exact uniform sampling modulo \(M\) uses \(O(k)\) random bits in expectation by rejection from \(k\)-bit strings. Each source requires \(k\) gcds and, on acceptance, \(k\) Jacobi-symbol computations, all on \(O(k)\)-bit integers.

Because \(\alpha_M>3/4\), obtaining \(L(k)\) accepted rows would take less than \(4L(k)/3\) raw draws in expectation even if proper-gcd successes were ignored. In an attempt, either a proper gcd ends the attempt successfully or the decoder is reached. Conditional on reaching it, the retained rows have exactly the independent accepted distribution in the hypothesis. Thus the success probability of every fresh attempt is at least \(1/Q(k)\), and the expected number of attempts is at most \(Q(k)\). Sampling, decoding, and all verification therefore have expected cost bounded by a fixed polynomial in \(k\). Geometric retry also proves almost-sure termination at each split.

Every recursive call is on a strict divisor, except that a perfect-power step replaces \(M\) by a base of at most half its bit length. The total number of prime factors counted with multiplicity is at most \(\log_2N<n\); hence the split tree has \(O(n)\) binary nodes, and allowing the shrinking perfect-power chains still gives \(O(n^2)\) calls. If \(P(k)\) bounds the expected work at one \(k\)-bit call, the total expectation is at most \(O(n^2P(n))\), a fixed polynomial. A finite recursive tree of almost-surely terminating calls terminates almost surely. Every accepted split is divisibility-verified, and every terminal factor is primality-verified, so every output is correct.

This proves the all-input Las Vegas factoring theorem **conditional on HP-LR**. It does not prove it unconditionally. HP-LR is precisely the absent high-order/list-recovery algorithm, and its promised output is already an inverse-polynomial-probability factor. The low-degree indistinguishability theorem neither supplies nor implies that decoder.

## 8. Edge-condition audit

- Normalization, deduplication, and all difference gcds occur before any probabilistic claim.
- No-factor screening implies \(m\le p,q\); accepted conditioning additionally requires \(m<p\).
- Every zero coordinate gets a separate fair sign. Correlated or single shared filling coins would invalidate the moment formula.
- \(c_\varnothing=1\), the \(t=1\) value is exactly zero, and the \(t=2\) value is exactly \(1/N\).
- The bit convention is \(n=\lceil\log_2(N+1)\rceil\), hence \(2^{n-1}\le N\le2^n-1\).
- TV is normalized as \(\frac12\sum|\mu-U|\). Bounded test expectations differ by at most TV; Bernoulli TV is \(|p-q|\).
- Prime powers, even factors, repeated factors, arbitrary odd composites, verification, recursive aggregation, expected bit complexity, and almost-sure termination are all explicit in the conditional reduction.
- The proof uses unknown factors only to analyze distributions. The executable preprocessing and sampler use public arithmetic, gcds, Jacobi symbols, and the hypothesized factor-free decoder.
