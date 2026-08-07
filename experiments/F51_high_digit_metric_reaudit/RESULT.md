# F51 canonical high-digit metric: fresh whole-artifact re-audit

## Artifact, method, and verdict

I audited `experiments/F51_high_digit_metric_kill/RESULT.md` at the requested
SHA-256
`2a1e111ffdbc20e76582201cb6f7fab24669cb0609711e030cf6c88e95828f90`.
The hash matches the file on disk. I also audited `RUN_MANIFEST.md` at
SHA-256
`b3fd206c0edba6903ad79444cf5a380207b970eff9b2a8eb80aed1da7cd5e8a1`.

I read `AGENTS.md`, `PROMPT.md`, P22, P49, P51, P56, X16, X43, X45,
X50, the full candidate and manifest, all five sources, all five wrappers,
all five logs, all five JSON outputs, and the preserved first hostile audit.
The preserved audit has SHA-256
`5328f85e14f624fcead3e5f3f3c3967e67df5c6060a9272631de686825ef9ca3`
and records the failure of the former candidate at SHA-256
`957fcfaa65003d40609986b1e8c9ae2d2b71627a28b2d5d9f80ae7c8b0b3f67b`.
I used no web source. I reconstructed the unbounded arguments independently
and treated every finite run only as finite evidence.

**Verdict: PASS AS WRITTEN.** Every displayed identity, counting bound,
probability claim, asymptotic conversion, and bit-cost claim is correct under
the stated distinct balanced odd-semiprime and independent-uniform-source
hypotheses. The manifest is internally consistent, and all five retained
outputs reproduce byte for byte.

The prior Fourier objection is fully repaired. The amended artifact closes
only independently uniform searches for inverse-polynomial-heavy modes, with
the empirical discussion restricted to the raw sample mean. It expressly
leaves deterministic or adaptive frequency recovery, other estimators, and
exact symbolic evaluation or amplification of small coefficients and biases
open. It makes no estimator-independent detection lower bound.

## 1. Uniform source, simultaneous section, and sample cost

Let \(N=pq\), where \(p<q<2p\) are distinct odd primes. On

\[
G_N\simeq C_{p-1}\times C_{q-1},
\]

the map \(a\mapsto x=a^N\bmod N\) is the \(N\)-th power map. The prime
\(q\) divides neither \(p-1\) nor \(q-1\). If \(p\mid q-1\), balance gives
\(q-1=p\), which is impossible because two odd primes cannot differ by one.
Therefore

\[
\gcd\!\left(N,\operatorname{lcm}(p-1,q-1)\right)=1.
\]

The power map is an automorphism, so a uniform unit \(a\) produces a uniform
unit \(x\).

Locally modulo \(p^2\), write a unit as \(a=\omega(1+pt)\), where
\(\omega\) is Teichmuller. Then

\[
a^{pq}\equiv\omega^{pq}=\omega^q\pmod {p^2}.
\]

This is the unique Teichmuller lift of \(a^q=x\bmod p\). The symmetric
argument holds modulo \(q^2\). CRT consequently gives

\[
A(a)=a^N\equiv[x\bmod p]_p\pmod {p^2},\qquad
A(a)\equiv[x\bmod q]_q\pmod {q^2}.
\]

Thus the law is equivalently uniform \(x\in G_N\) followed by its unique
simultaneous Teichmuller lift \(T_N(x)\). This agrees with the squarefree odd
descent case in P56 and does not assume access to either factor.

A uniform residue modulo \(N\) needs constant expected rejection overhead
from \(n=\lceil\log_2(N+1)\rceil\) random bits. For this promise,

\[
\frac{\varphi(N)}N=(1-1/p)(1-1/q)\ge\frac8{15},
\]

so gcd screening also has constant expected overhead. A proper gcd found by
the screen is already a factor; otherwise nonunits can be rejected. Binary
exponentiation uses \(O(n)\) modular multiplications on \(O(n)\)-bit values.
Schoolbook arithmetic therefore gives the claimed \(O(n^3)\) bit cost per
accepted source value. Extraction of \(h\), inversion of \(x\bmod N\), and
canonical reduction are lower-order \(O(n^2)\) operations.

## 2. Fermat-quotient and carry laws

Write

\[
T_N(x)=x+Nh,\qquad \lambda=h x^{-1}\pmod N.
\]

Since \(h\equiv x\lambda\pmod N\),

\[
T_N(x)\equiv x(1+N\lambda)\pmod {N^2}.
\]

Modulo \(p^2\), the Teichmuller lift has \((p-1)\)-st power one. With

\[
Q_p(x)=\frac{x^{p-1}-1}{p}\pmod p,
\]

the first-order expansion gives

\[
1\equiv(1+pQ_p(x))(1+pq(p-1)\lambda)
 \equiv1+p(Q_p(x)-q\lambda)\pmod {p^2}.
\]

Hence

\[
q\lambda\equiv Q_p(x)\pmod p,
\qquad qh\equiv xQ_p(x)\pmod p.
\]

The \(q\)-side gives

\[
p\lambda\equiv Q_q(x)\pmod q,
\qquad ph\equiv xQ_q(x)\pmod q.
\]

All signs and cross-prime multipliers in (3.3)--(3.4) are therefore correct.

For the carry form, write \(x=u+pk\), with \(1\le u<p\) and
\(0\le k<q\). Exactly one \(k\) is omitted because it makes \(x\) divisible
by \(q\). Since the local lift is \(u^p\bmod p^2\),

\[
pqh\equiv u^p-u-pk\pmod {p^2}.
\]

After division by \(p\), this becomes

\[
qh\equiv d_p(u)-k,
\qquad qu\lambda\equiv d_p(u)-k\pmod p,
\]

where \(d_p(u)=(u^p-u)/p\pmod p\). Writing \(x=v+q\ell\) gives the two
symmetric equations modulo \(q\). This reconstructs (3.5)--(3.6), including
their representative-dependent carry terms.

## 3. Anti-concentration, collisions, and direct gcds

There are \((p-1)(q-1)\) equally likely unit values of \(x\). Fix a residue
\(c\bmod p\). For each of the \(p-1\) choices of \(u\), either carry equation
selects one class of \(k\bmod p\). The range \(0\le k<q<2p\) contains at
most two representatives of that class. Therefore, for
\(Z\in\{h,\lambda\}\),

\[
\Pr(Z\equiv c\pmod p)\le\frac2{q-1}.
\]

On the other side, \(0\le\ell<p<q\), so the selected class modulo \(q\)
has at most one representative for each of the \(q-1\) choices of \(v\).
Thus

\[
\Pr(Z\equiv c\pmod q)\le\frac1{p-1}.
\]

A full value fixes its residue modulo \(q\), which proves

\[
\max_z\Pr(Z=z)\le\frac1{p-1},
\qquad
\Pr(Z\in S)\le\frac{|S|}{p-1}
\]

for every fixed named set \(S\). The same bound applies conditionally when a
past-measurable menu is tested on a fresh independent sample. It does not
apply to a target chosen from the current sample's full joint data, and the
candidate does not claim that it does.

For two independent samples,

\[
\Pr(Z_1=Z_2)=\sum_z\Pr(Z=z)^2\le\frac1{p-1}.
\]

Applying the same argument to the two local marginal laws gives

\[
\Pr(Z_1\equiv Z_2\pmod p)\le\frac2{q-1},\qquad
\Pr(Z_1\equiv Z_2\pmod q)\le\frac1{p-1}.
\]

A proper gcd of a pairwise difference requires at least one of these local
collisions. A union bound over \(m\) independent samples gives exactly

\[
{m\choose2}\left(\frac2{q-1}+\frac1{p-1}\right).
\]

Also, \(h\equiv x\lambda\pmod N\) and \(x\) is a unit, so

\[
\gcd(h,N)=\gcd(\lambda,N).
\]

The two zero-residue bounds imply the stated direct proper-gcd bound. Since
\(p^2<N<2p^2\), one has \(p=2^{\Theta(n)}\). Consequently any fixed
polynomial-size menu or iid sample schedule makes all displayed menu,
collision, all-pairs, and direct-gcd probabilities \(2^{-\Omega(n)}\).
No independence between different pair events is used.

This proof does not cover a correlated or nonuniform base source. Those
sources are explicitly left open.

## 4. Hidden residue bands and the P51 boundary

Summing the local point bounds over arbitrary residue sets gives

\[
\Pr(Z\bmod p\in R_p)\le\frac{2|R_p|}{q-1},\qquad
\Pr(Z\bmod q\in R_q)\le\frac{|R_q|}{p-1}.
\]

A centered radius-\(B\) band modulo \(p\), with \(B<p/2\), contains at most
\(2B+1\) residues. Hence

\[
\Pr(\|Z/p\|_{\mathbb R/\mathbb Z}\le B/p)
 \le\frac{2(2B+1)}{q-1}
 =O(B/p+1/p).
\]

The symmetric \(q\)-bound is also correct. The constants are uniform on the
stated fixed-balance family.

Put \(B/p=2^{-(1+\eta)\sqrt n}\). One raw iid draw then hits the necessary
\(p\)-band with probability at most \(O(2^{-(1+\eta)\sqrt n})\). Even a
perfect recognizer needs expected at least \(m/\rho=2^{\Omega(\sqrt n)}\)
draws to collect \(m=\Theta(\sqrt n)\) band hits, with infinite expectation
allowed if the actual hit probability \(\rho\) is zero.

Band membership is only necessary for the P51 promise. P51 also requires
fresh independent uniform hidden quotients, which the conditional F51 hits
are not claimed to have. Thus the raw-source lower bound is conservative and
does not manufacture a P51 source. At inverse-polynomial relative width,
P51 says only that its displayed ordinary worst-case LLL certificate is
noninformative in every dimension. The candidate correctly leaves other
decoders, favorable error laws, and partial-inlier methods open.

## 5. Reflection and the central half interval

For odd local primes, Teichmuller lifting commutes with negation. Therefore

\[
T_N(N-x)\equiv-T_N(x)\pmod {N^2}.
\]

The canonical representative \(T_N(x)=x+Nh(x)\) is nonzero. Taking the
canonical representative of its negative gives

\[
N^2-(x+Nh(x))=(N-x)+N(N-1-h(x)),
\]

and hence

\[
h(N-x)=N-1-h(x).
\]

The involution \(x\mapsto N-x\) has no fixed unit because \(2\) is a unit
modulo odd \(N\). Pairing its orbits proves

\[
\mathbb Eh=\frac{N-1}{2}
\]

and zero expectation for every statistic antisymmetric about
\((N-1)/2\), including all odd centered moments.

Let \(c=\Pr(h=(N-1)/2)\). Each noncentral reflected pair contributes one
point below \(N/2\), while the central point is also below that half-integer
threshold. Therefore

\[
\Pr(h<N/2)=\frac{1+c}{2}.
\]

The uniform \(N\)-point grid has mass \((N+1)/(2N)\), and the full-value
point bound gives \(c\le1/(p-1)\). The candidate's bound

\[
\left|\Pr(h<N/2)-\frac{N+1}{2N}\right|
\le\frac1{2(p-1)}+\frac1{2N}
\]

follows. It is exponentially small in \(n\). The argument is specific to
this reflected half interval and antisymmetric \(h\)-statistics; it does not
control arbitrary shifted intervals or assert a reflection theorem for
\(\lambda\).

## 6. Fourier proof and the corrected exact scope

Let

\[
\widehat\mu_Z(k)=\mathbb E e_N(kZ).
\]

Finite-group Parseval and the point-mass bound give

\[
\sum_{k\bmod N}|\widehat\mu_Z(k)|^2
=N\sum_z\Pr(Z=z)^2
\le\frac N{p-1}.
\]

Thus the number of frequencies with coefficient magnitude at least
\(\delta\) is at most

\[
\frac{N}{(p-1)\delta^2}.
\]

If \(K\) is a uniform unit frequency, then

\[
\Pr(|\widehat\mu_Z(K)|\ge\delta)
\le\frac{N}{\varphi(N)(p-1)\delta^2}
<\frac2{(p-1)\delta^2}.
\]

For fixed constants \(C,D\), taking
\(\delta\ge n^{-C}\) and at most \(n^D\) independently uniform unit
frequencies gives a total hit probability
\(2^{-\Omega(n)}\). Independence is more than the union bound needs;
uniform conditional marginals would suffice. This conclusion concerns the
rarity of inverse-polynomial-heavy modes under random uniform frequency
sampling. It says nothing about where exceptional deterministic modes are
or how an adaptive algorithm might find them.

The local-isolating statement is exact:

\[
e_p(rZ)=e_N(qrZ),\qquad1\le r<p,
\]

and \(\gcd(qr,N)=q\). The symmetric local frequencies are nonzero multiples
of \(p\). An explicitly supplied exactly local-isolating frequency therefore
already reveals a factor through its public gcd.

For a fixed frequency and iid samples \(X_j=e_N(kZ_j)\), direct expansion
gives

\[
\mathbb E|\overline X_m-\theta|^2
=\frac{1-|\theta|^2}{m}.
\]

This is only the exact MSE of the raw empirical mean. It is not a
fixed-confidence lower bound, an information-theoretic lower bound, or a
statement about every estimator.

The corrected candidate states precisely these limitations twice. Section 7
expressly leaves deterministic exceptional frequencies, adaptive recovery,
other estimators, exact symbolic evaluation or amplification of
exponentially small coefficients, and Fourier-dense nonlinear statistics
open. Section 9 closes only
"independently uniform public frequencies searched for
inverse-polynomial-heavy coefficients by raw empirical means" and lists
exact symbolic evaluation or amplification of small Fourier coefficients or
interval biases as a reopen condition. This is the exact correction required
by the first audit. No residual version of the former broad
"random-frequency probing" claim remains.

## 7. Relation to the promoted boundaries and final scope

The comparisons with the four promoted results are accurate.

- P22/X16 controls direct gcds of fixed polynomial-size canonical high-digit
  lists from uniform bases on an infinite balanced family. F51 derives finer
  one-point, local-residue, collision, interval, and spectral laws. It does
  not convert P22 into a general \(N^2\)-adic obstruction.
- P56/X50 closes genuine multiplicative linear-cocycle inconsistency. F51's
  one-point metric laws are outside that theorem, and F51 does not claim to
  close nonlinear, coefficient-rank, minor, Smith, additive, or higher-carry
  processing.
- P49/X43 is the correct cautionary comparison for sparse ordinary Fourier
  means and histograms. Unlike P49, F51 has no fourth-moment
  fixed-confidence lower bound, and the amended text does not claim one.
- P51/X45 supplies a conditional ordinary-LLL decoder and an exact failure
  of its proved certificate at inverse-polynomial relative error. F51 uses
  only the necessary band condition and does not claim that a band hit has
  P51's quotient law.

Accordingly, the artifact is a narrow source-side method obstruction on
distinct balanced odd semiprimes. It is not an all-input theorem, a factoring
lower bound, computational indistinguishability, or a factoring algorithm.
Its final open list correctly retains deterministic coarse intervals,
deterministic and adaptive heavy-frequency recovery, exact small-bias
evaluation or amplification, alternative estimators and decoders, nonlinear
joint processing, correlated/adaptive/nonuniform bases, and engineered
all-input separation laws.

## 8. Retained computations and provenance

I recomputed all twenty manifest hashes. Every source, wrapper, output, and
log hash matches the manifest. Each JSON's embedded source hash also matches
the source on disk.

| Run | Source | Wrapper | Output | Log |
| --- | --- | --- | --- | --- |
| F51-D01 | `0251538673176a946e707d9c324b560a9b8414a0a515577e7d59ba6d950e2cdc` | `29b6c5f6ef8fd22e359049d06c632c0342048dc01ef890ac074e7ad876e94e50` | `6609560ccc9f5e63314f03a4f39eae63d499bbdc1d94803851b27f6a9e91648c` | `396142a1d278cd4f9fd4a4372415aeddee660ee040ec8c2ebef71f2407c2d605` |
| F51-D02 | `fd923f8c40dea8fddcde7c304231c8e5635d3ccfb782bbe1559f460f09e9bc32` | `784fbf3de90067fbae76954b2e644537bcb7b335d339f4853e19a95bb8eb5408` | `6cec6da477328b3f70530e394f8dbe3f67607a003e808a85354aeb19caea7a47` | `eeb57c7fd578fdd7a490a85a1a5d3e99d3aa055d5b060652b3f2657670c469b7` |
| F51-D03 | `211e0c155eae77fd5befba89d69644db22bd2f07ecd73bb42d16bb42aacb22d0` | `06fd58926a61f9e9234fd7eea6e58b8f32af8dbbdfb15075189d38a333b5a674` | `96a69a52659c247f9c35f5ad908e4ff92a080fb9aa58d2e5808b4b75427cbfc8` | `5322af88174fed8f0f381f02e99f21878cbf54af7d3644afc0060f0c9d08c5af` |
| F51-D04 | `4b1fe71c6af85a26a88028bc55a6f1f75931479e710e1a91133045657d8bd5e4` | `3be7f298bc1a7b5481ef0ce029f251395c4b929ef619a6bc1dc27f16a47c2046` | `afc427706f51bf6a6b750c70553f4747c4091d83f7c1a8fc2ca466a06d3a01b5` | `e66aedcd0a92ef882a4f2fd0b0870af863aad0d06b8d22517e200cbeffe845d9` |
| F51-D05 | `31c7bd02cbfb10f808916ead868bd63ed40eb8fa5167349e0fa0ba901a3148a1` | `b52f80ba0879dc9b1794cbddcc183ff9b045fc0618738c483d3b5b467e8da71f` | `48c961afbb11c646e052fc15ac7157a1780c86f0ae0f2342e1f67e2d182892bd` | `df4c2f37a2958b4a067eb43889839aad92f60af96166ca37c96b5801c99a3e34` |

The wrappers use `set -eu`, named sources, a 180-second hard timeout, retained
logs, and retained output paths. The logs record Python 3.14.5, the timeout,
successful script completion, and `EXIT 0`. D01--D04 import only the standard
library. D05 records NumPy 2.4.6.

I reran all five scripts independently under the same 180-second limit,
writing only to temporary files. Every regenerated JSON was byte-identical
to its retained output. This verifies deterministic reproducibility; the
retained UTC timestamps remain internal provenance rather than external
timestamp attestation.

The finite claims also match the retained data:

- D01 enumerates the twelve listed balanced pairs. It verifies local lifts,
  the power-map permutation, normalized digits, and exact integer fibre,
  collision, gcd, total-variation, and discrepancy statistics. At
  \((211,223)\), the proper-gcd probability is
  `0.009202059202059201`, and the two total-variation values are about
  `0.372665` and `0.371985`.
- D02 checks all four carry laws and the conditional fibre maxima. At
  \((211,223)\), the largest local nonzero Fourier magnitudes are
  `0.0084486214` for \(h\) and `0.0028057263` for \(\lambda\).
- D03 checks the exact reflection law on all twelve pairs. Every recorded
  \(h\)-mean is exactly \((N-1)/2\). Its additional moment and threshold data
  are not used for an asymptotic theorem.
- D04 enumerates all 233 balanced odd-prime pairs with \(p\le101\). Its
  star-discrepancy formula is correct. The reported scaled maxima are
  `1.6826185937` for \(h\) at \((71,79)\) and `1.9094524594` for
  \(\lambda\) at \((47,71)\).
- D05 builds the full histograms, computes the complete finite FFT, removes
  the zero frequency, and partitions all remaining frequencies by gcd
  category. FFT sign is irrelevant to magnitude. At \((211,223)\), the
  largest gcd-free magnitudes are `0.0404783896` for \(h\) and
  `0.0498581771` for \(\lambda\).

All floating-point calculations are used only for finite descriptive
statistics. None supports an unbounded theorem. The unbounded conclusions
come from the exact carry count, exact involution, Parseval identity, and the
symbolic relation \(p=2^{\Theta(n)}\).

## 9. Final disposition

No correction is required. This pass applies only to the exact audited
artifact hash above. It advances the corrected candidate through this fresh
hostile-audit step; it does not itself supply the separate proof-blind
reconstruction or cross-family audit mentioned by the repository process.

PASS AS WRITTEN
