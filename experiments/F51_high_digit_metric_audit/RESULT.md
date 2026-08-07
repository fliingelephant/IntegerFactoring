# F51 canonical high-digit metric: focused hostile audit

## Artifact, method, and verdict

I audited `experiments/F51_high_digit_metric_kill/RESULT.md` at SHA-256
`957fcfaa65003d40609986b1e8c9ae2d2b71627a28b2d5d9f80ae7c8b0b3f67b`
and its `RUN_MANIFEST.md` at SHA-256
`b3fd206c0edba6903ad79444cf5a380207b970eff9b2a8eb80aed1da7cd5e8a1`.

I read `AGENTS.md`, `PROMPT.md`, P22, P49, P51, P56, X16, X43,
X45, X50, the candidate, the manifest, all five sources, all five wrappers,
all five logs, and all five JSON outputs. I used no web source. I re-derived
the unbounded statements and treated the finite runs only as finite evidence.

**Verdict: FAIL AS WRITTEN.** All numbered identities and probability bounds
in Sections 2--7 are correct under their balanced-semiprime and iid
uniform-source hypotheses. The five computations and their provenance are
also internally consistent. The failure is one scope overclaim: (7.1)--(7.4)
do not close random-frequency probing without qualification. They prove
rarity of inverse-polynomial-heavy modes under uniform unit-frequency
sampling and give the MSE of one particular estimator. They do not rule out
exact symbolic evaluation or amplification of exponentially small
coefficients, and MSE alone is not an algorithm-independent fixed-confidence
detection lower bound. Section 9's claimed exact reopen list omits that
surviving channel.

The smallest correction is in Section 9 of this audit. No algebraic,
probabilistic, asymptotic, bit-cost, script, output, or hash correction is
otherwise required.

## 1. Uniform power map and simultaneous Teichmuller lift

Let \(N=pq\), where \(p<q<2p\) are distinct odd primes. On

\[
G_N\simeq C_{p-1}\times C_{q-1},
\]

the reduction \(x(a)=a^N\bmod N\) is the \(N\)-th power map. A prime divides
\(\operatorname{lcm}(p-1,q-1)\) only if it divides one of the two arguments.
The prime \(q\) exceeds both arguments. The only possible remaining event is
\(p\mid q-1\). Since \(p<q<2p\), this would force \(q-1=p\), impossible for
two odd primes. Hence

\[
\gcd\!\left(N,\operatorname{lcm}(p-1,q-1)\right)=1,
\]

so \(a\mapsto x(a)\) is an automorphism and sends a uniform unit to a
uniform unit.

Locally modulo \(p^2\), write a unit lift as \(a=\omega(1+pt)\), with
\(\omega\) Teichmuller. Then

\[
a^{pq}\equiv \omega^{pq}=\omega^q\pmod {p^2};
\]

the principal factor disappears because the exponent contains \(p\).
Reduction modulo \(p\) is \(x\equiv a^q\), so

\[
a^N\equiv[x\bmod p]_p\pmod {p^2}.
\]

The symmetric calculation holds modulo \(q^2\). CRT proves the candidate's
simultaneous Teichmuller law (2.1). This is consistent with P22 and with the
squarefree-odd descent case of P56.

## 2. Fermat-quotient and carry laws

Write the canonical simultaneous lift as

\[
T_N(x)=x+Nh,\qquad \lambda=h x^{-1}\pmod N.
\]

Then \(T_N(x)\equiv x(1+N\lambda)\pmod {N^2}\). Modulo \(p^2\), the left
side has \((p-1)\)-st power one. With
\(Q_p(x)=(x^{p-1}-1)/p\bmod p\), the first-order expansion is

\[
1\equiv(1+pQ_p(x))(1+pq(p-1)\lambda)
 \equiv1+p(Q_p(x)-q\lambda)\pmod {p^2}.
\]

Thus \(q\lambda\equiv Q_p(x)\pmod p\); multiplication by \(x\) gives
\(qh\equiv xQ_p(x)\pmod p\). The \(q\)-side gives
\(p\lambda\equiv Q_q(x)\pmod q\) and
\(ph\equiv xQ_q(x)\pmod q\). The signs and cross-prime multipliers in
(3.3)--(3.4) are correct.

For the carry form, write \(x=u+pk\), with \(1\le u<p\). The Teichmuller
lift of \(u\bmod p\) is \(u^p\bmod p^2\), so

\[
pq h\equiv u^p-(u+pk)
 =p\left(\frac{u^p-u}{p}-k\right)\pmod {p^2}.
\]

After division by \(p\), this is

\[
qh\equiv d_p(u)-k,\qquad
qu\lambda\equiv d_p(u)-k\pmod p.
\]

Writing \(x=v+q\ell\) gives the symmetric two equations modulo \(q\).
This proves (3.5)--(3.6), including the representative-dependent carry
terms.

## 3. Point masses, menus, collisions, and direct gcd events

For each \(u\in\{1,\ldots,p-1\}\), the admissible values are
\(0\le k<q\), except for the unique \(k\) that makes \(u+pk\) divisible by
\(q\). For fixed \(h\bmod p\), (3.5) selects one class of \(k\bmod p\).
Because \(q<2p\), that class occurs at most twice. The same argument works
for fixed \(\lambda\bmod p\), since \(u\ne0\bmod p\). After division by
\(\varphi(N)=(p-1)(q-1)\),

\[
\max_c\Pr(Z\equiv c\pmod p)\le\frac2{q-1},
\qquad Z\in\{h,\lambda\}.
\]

On the other side, \(0\le\ell<p<q\), so each selected class modulo \(q\)
occurs at most once for each of the \(q-1\) choices of \(v\). Therefore

\[
\max_c\Pr(Z\equiv c\pmod q)\le\frac1{p-1}.
\]

A full value fixes its \(q\)-residue, proving

\[
\max_z\Pr(Z=z)\le\frac1{p-1},\qquad
\Pr(Z\in S)\le\frac{|S|}{p-1}
\]

for every fixed set \(S\). For iid \(Z_1,Z_2\), squaring the marginal laws
gives the candidate's full and local collision bounds. A proper gcd of
\(Z_i-Z_j\) requires equality modulo \(p\) or modulo \(q\), so a union over
pairs proves (4.7).

The direct event is also valid. Since \(x\) is a unit and
\(h\equiv x\lambda\pmod N\),

\[
\gcd(h,N)=\gcd(\lambda,N).
\]

Taking the local target residue to be zero proves (4.8). The same argument
covers \(\gcd(Z-c,N)\) for any fixed named \(c\).

The menu quantifier needs the standard independence reading, and the
candidate's words "named set" are consistent with it. A deterministic menu
is covered. A menu chosen from earlier iid samples is also covered when it is
applied to a fresh sample: condition on the past, apply the fixed-set bound,
and average. The all-pairs estimate similarly covers a bounded
past-adaptive stopping rule by union over the scheduled iid samples.

The theorem does not cover a menu chosen from the same target's current
\((x,h)\) data, or a base distribution changed adaptively away from uniform.
Those would invalidate the conditioning step. The candidate explicitly
leaves nonlinear processing of \((x,h)\) and engineered adaptive/nonuniform
bases open, so there is no quantifier leak on this point.

Finally, \(p^2<N<2p^2\), so \(p=2^{\Theta(n)}\). A polynomial number of
fixed-menu, direct-gcd, exact-collision, or all-pairs local-collision trials
therefore has total probability \(2^{-\Omega(n)}\). This conclusion is
symbolic and does not use the finite scans.

## 4. Hidden bands and the P51 boundary

A centered band of radius \(B<p/2\) modulo \(p\) contains at most \(2B+1\)
residues. Summing the local point bound proves

\[
\Pr(\|Z/p\|\le B/p)
 \le\frac{2(2B+1)}{q-1}
 =O(B/p+1/p)
\]

under fixed balance. The symmetric \(q\)-bound is also correct.

Put \(\epsilon=B/p=2^{-(1+\eta)\sqrt n}\). Since
\(1/p=2^{-\Theta(n)}\), one iid raw draw hits the necessary \(p\)-band with
probability \(\rho=O(2^{-(1+\eta)\sqrt n})\). Even a perfect recognizer
cannot increase that hit probability. The expected number of iid draws
needed to collect \(m=\Theta(\sqrt n)\) hits is
\(m/\rho=2^{\Omega(\sqrt n)}\), with infinity allowed if \(\rho=0\).
Band membership is only necessary for P51: the conditional quotients must
additionally have P51's fresh independent uniform law. Thus the lower bound
is conservative, not an accidental claim that every band hit satisfies the
P51 promise.

At \(\epsilon=n^{-c}\), P51 proves only that its displayed ordinary-LLL
worst-case certificate is noninformative for every dimension. The candidate
preserves that exact method boundary and does not claim that LLL or another
ACD decoder fails.

## 5. Reflection, mean, and the half-threshold statistic

For odd \(N\), local Teichmuller lifts are odd, hence

\[
T_N(N-x)\equiv-T_N(x)\pmod {N^2}.
\]

If \(T_N(x)=x+Nh(x)\) is canonical and nonzero, then

\[
N^2-T_N(x)=(N-x)+N(N-1-h(x)).
\]

This proves \(h(N-x)=N-1-h(x)\). The involution has no fixed unit. Pairing
its orbits gives

\[
\mathbb E h=(N-1)/2
\]

and zero expectation for every \(f\) with
\(f(N-1-z)=-f(z)\), including all odd centered moments.

Let \(c=\Pr(h=(N-1)/2)\). Every noncentral reflected pair contributes one
value below \(N/2\), while a central value is also below \(N/2\). Therefore

\[
\Pr(h<N/2)=\frac{1+c}{2}.
\]

The uniform \(N\)-point grid gives \((N+1)/(2N)\), and the point-mass bound
gives \(c\le1/(p-1)\). Hence (6.4) follows exactly and is
\(2^{-\Omega(n)}\). The proof concerns this one half-threshold statistic of
\(h\); it does not cover shifted intervals, nonsymmetric intervals, or an
analogous reflection claim for \(\lambda\).

## 6. Parseval and the precise random-frequency conclusion

With
\(\widehat\mu_Z(k)=\sum_z\mu_Z(z)e_N(kz)\), finite-group Parseval gives

\[
\sum_{k\bmod N}|\widehat\mu_Z(k)|^2
 =N\sum_z\mu_Z(z)^2
 \le N\max_z\mu_Z(z)
 \le\frac{N}{p-1}.
\]

Markov counting therefore gives at most
\(N/((p-1)\delta^2)\) frequencies of magnitude at least \(\delta\). For
distinct odd primes,

\[
\frac N{\varphi(N)}
=\frac p{p-1}\frac q{q-1}<2,
\]

so a uniform unit frequency \(K\) satisfies

\[
\Pr(|\widehat\mu_Z(K)|\ge\delta)
 \le\frac2{(p-1)\delta^2}.
\]

For \(\delta=n^{-c}\), a union bound over any polynomial number of
independently uniform unit frequencies is \(2^{-\Omega(n)}\). Independence
between the frequencies is not needed for that union bound; uniform
conditional marginals suffice.

The local-character statement is exact. A nonzero \(p\)-local character is

\[
e_p(rZ)=e_N(qrZ),\qquad1\le r<p,
\]

and \(\gcd(qr,N)=q\). The symmetric \(q\)-local character has a frequency
whose gcd with \(N\) is \(p\). An explicitly supplied exactly local-isolating
frequency therefore already supplies a factor.

For iid \(X_j=e_N(kZ_j)\), direct expansion gives

\[
\mathbb E|\overline X_m-\theta|^2
 =\frac{\mathbb E|X-\theta|^2}{m}
 =\frac{1-|\theta|^2}{m}.
\]

Thus (7.1)--(7.4) are all correct. What does not follow is the candidate's
unqualified sentence that these equations "close random frequency probing."
There are two exact gaps:

1. The Parseval count rules out frequent inverse-polynomial-heavy modes under
   a uniform unit-frequency draw. It says nothing about whether an
   exponentially small coefficient can be evaluated exactly in polynomial
   bit complexity and converted into a factor.
2. The MSE identity describes the raw empirical mean. By itself it is not an
   information-theoretic lower bound for every estimator, nor even a
   fixed-confidence lower bound for that estimator. Such a conclusion needs
   an additional anti-concentration or testing argument. P49 carefully made
   this distinction and explicitly retained exact symbolic amplification of
   tiny biases as open.

The candidate correctly says that it is not a distributional or factoring
lower bound. But Section 9 calls its reopen list exact and closes
"independently random public Fourier probes" without the necessary heavy-mode
and empirical-estimator qualifications. Those words are broader than the
proved equations.

## 7. Uniform bit cost and absence of hidden factor access

A uniform residue modulo \(N\) is obtained from \(n\) random bits with
constant expected rejection overhead. On this promise,

\[
\frac{\varphi(N)}N=(1-1/p)(1-1/q)\ge\frac8{15},
\]

so gcd screening also has constant expected overhead. A nontrivial screen is
already a verified factor; zero or another full-gcd residue is rejected.
Random-bit generation and a schoolbook gcd cost \(O(n^2)\) or less per
accepted trial.

Binary exponentiation by the \(O(n)\)-bit exponent \(N\), modulo the
\(O(n)\)-bit modulus \(N^2\), uses \(O(n)\) schoolbook modular
multiplications, each \(O(n^2)\). It therefore costs \(O(n^3)\) bit
operations. Canonical reduction, exact division by \(N\), and inversion of
the unit \(x\bmod N\) cost \(O(n^2)\). The candidate's one-sample
\(O(n^3)\) bound includes all dominant arithmetic and needs no factor.

The proofs use \(p,q\) only to analyze the law. The public sampler uses only
\(N\), random bits, gcd, modular exponentiation, division, and an
extended-Euclidean inverse. The finite diagnostic programs do use their
listed \(p,q\), but they are explicitly not proposed factoring algorithms.

## 8. Audit of the five computations and provenance

I recomputed every hash in the manifest. All twenty source, wrapper, output,
and log hashes match exactly. Each JSON's embedded source hash also matches
the source on disk. The wrappers are executable, use `set -eu`, record a UTC
start, Python version, the 180-second timeout, and append `EXIT 0` only after
the timed command succeeds. The retained logs record Python 3.14.5; D05's
JSON additionally records NumPy 2.4.6.

I independently reran all five named scripts under the same 180-second
limit, writing only to `/tmp`. Every regenerated JSON was byte-identical to
the retained output. This checks deterministic reproducibility. The retained
timestamps and hashes are an internally consistent provenance record, not an
external timestamp attestation.

| Run | Static and regenerated-output audit | Manifest hashes |
| --- | --- | --- |
| F51-D01 | Correctly enumerates the twelve listed unit groups; checks the local Teichmuller lift, normalized digit, injective joint graph, and power-map permutation; exact integer fibre, collision, gcd, TV, and discrepancy formulas are correct. The last proper-gcd probability is `0.009202059202059201`, and the last TV values are about `0.372665` and `0.371985`, as reported. | Source `0251538673176a946e707d9c324b560a9b8414a0a515577e7d59ba6d950e2cdc`; wrapper `29b6c5f6ef8fd22e359049d06c632c0342048dc01ef890ac074e7ad876e94e50`; output `6609560ccc9f5e63314f03a4f39eae63d499bbdc1d94803851b27f6a9e91648c`; log `396142a1d278cd4f9fd4a4372415aeddee660ee040ec8c2ebef71f2407c2d605`. |
| F51-D02 | Correctly reparametrizes by uniform \(x\) using the inverse exponent; asserts all four carry laws and the conditional fibre maxima. The last maxima are `0.0084486214` for \(h\) and `0.0028057263` for \(\lambda\), consistent with the prose. Floating Fourier values are finite diagnostics only. | Source `fd923f8c40dea8fddcde7c304231c8e5635d3ccfb782bbe1559f460f09e9bc32`; wrapper `784fbf3de90067fbae76954b2e644537bcb7b335d339f4853e19a95bb8eb5408`; output `6cec6da477328b3f70530e394f8dbe3f67607a003e808a85354aeb19caea7a47`; log `eeb57c7fd578fdd7a490a85a1a5d3e99d3aa055d5b060652b3f2657670c469b7`. |
| F51-D03 | Correctly asserts the \(h\)-reflection law and records exact rational means, variances, and five threshold masses. All twelve \(h\)-means equal \((N-1)/2\). The script also records \(\lambda\) statistics but does not use \(h\)'s reflection theorem for \(\lambda\). | Source `211e0c155eae77fd5befba89d69644db22bd2f07ecd73bb42d16bb42aacb22d0`; wrapper `06fd58926a61f9e9234fd7eea6e58b8f32af8dbbdfb15075189d38a333b5a674`; output `96a69a52659c247f9c35f5ad908e4ff92a080fb9aa58d2e5808b4b75427cbfc8`; log `5322af88174fed8f0f381f02e99f21878cbf54af7d3644afc0060f0c9d08c5af`. |
| F51-D04 | Its elementary primality loop produces every balanced odd-prime pair with \(p\le101\), exactly 233 rows. The star-discrepancy formula is correct. The retained maxima are `1.6826185937` at \((71,79)\) for \(h\) and `1.9094524594` at \((47,71)\) for \(\lambda\). They are explicitly finite observations. | Source `4b1fe71c6af85a26a88028bc55a6f1f75931479e710e1a91133045657d8bd5e4`; wrapper `3be7f298bc1a7b5481ef0ce029f251395c4b929ef619a6bc1dc27f16a47c2046`; output `afc427706f51bf6a6b750c70553f4747c4091d83f7c1a8fc2ca466a06d3a01b5`; log `e66aedcd0a92ef882a4f2fd0b0870af863aad0d06b8d22517e200cbeffe845d9`. |
| F51-D05 | Correctly constructs full histograms, takes the complete finite FFT, ignores the zero frequency, and partitions every remaining frequency by gcd \(1,p,q\). FFT sign does not affect magnitudes. At \((211,223)\), the gcd-free maxima are `0.0404783896` and `0.0498581771`, as reported. | Source `31c7bd02cbfb10f808916ead868bd63ed40eb8fa5167349e0fa0ba901a3148a1`; wrapper `b52f80ba0879dc9b1794cbddcc183ff9b045fc0618738c483d3b5b467e8da71f`; output `48c961afbb11c646e052fc15ac7157a1780c86f0ae0f2342e1f67e2d182892bd`; log `df4c2f37a2958b4a067eb43889839aad92f60af96166ca37c96b5801c99a3e34`. |

The imports confirm that D01--D04 use only the standard library and D05 uses
NumPy. The output schema marks every run as finite discovery/certificate
evidence only. D01--D03 contain exact integer or rational checks where
claimed. D02, D04, and D05 use floating values only for explicitly finite
descriptive Fourier/discrepancy observations.

No asymptotic statement depends on a fitted trend or on the largest scanned
prime. Anti-concentration uses exact carry counts; the band result uses exact
residue cardinality; reflection is an exact involution; and frequency rarity
is an exact Parseval count. The relation \(p=2^{\Theta(n)}\) supplies the
asymptotic conversion.

## 9. Smallest exact correction and resulting scope

No counterexample exists to the displayed algebra or probability bounds. The
failure is the unsupported scope inference after them. The smallest repair
is textual and does not change a formula:

1. Replace the last paragraph of Section 7 beginning "Equations
   (7.1)--(7.4) close random frequency probing" with:

   > Equations (7.1)--(7.3) show that polynomially many independently uniform
   > unit frequencies have exponentially small probability of finding an
   > inverse-polynomial-heavy coefficient. Equation (7.4) is the exact MSE of
   > the raw empirical mean. These statements do not rule out deterministic
   > exceptional frequencies, adaptive frequency recovery, other estimators,
   > or exact symbolic evaluation or amplification of exponentially small
   > coefficients.

2. In Section 9, replace "independently random public Fourier probes" by
   "independently uniform public frequencies searched for
   inverse-polynomial-heavy coefficients by raw empirical means", and add
   "exact symbolic evaluation or amplification of small Fourier
   coefficients or interval biases" to the open/reopen list.

After that amendment, the candidate proves a sound narrow source-side
obstruction. It closes fixed or past-adaptive menus applied to fresh iid
samples, direct and pairwise gcd events for \(h\) and \(\lambda\), P51-thin
band collection from this iid source, the reflected \(h\)-statistics, and
uniform random searches for heavy Fourier modes. It does not close
current-sample joint rules, nonuniform/adaptive base sources, deterministic
coarse intervals, exact tiny-bias computation, nonlinear joint processing,
new approximate-common-divisor decoders, or all-input factoring.

FAIL AS WRITTEN
