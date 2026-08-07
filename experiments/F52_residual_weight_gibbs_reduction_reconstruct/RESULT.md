# Independent reconstruction

**Status: succeeds.** The square-root endpoint needs the explicit rate
\(\theta_{w_N}=O(\operatorname{poly}(\log N)/\sqrt N)\). Mere negligibility as a
function of the input length implies a superpolynomial refresh lower bound, but
does not by itself imply a square-root lower bound. Both conclusions are stated
precisely below.

## Setup

Represent each element of \(R=\mathbb Z/N\mathbb Z\) by its member of
\(\{0,\ldots,N-1\}\), and use this representative in a gcd. Put

\[
 \Omega_N=\{(k,x)\in R^2:kx=0\},\qquad
 Z_w=\sum_{(k,x)\in R^2}w(kx),
\]

and let

\[
 \pi_w(k,x)=\frac{w(kx)}{Z_w}.
\]

These quantities are well-defined: \(W\geq w(0)>0\), and
\(Z_w\geq Nw(0)>0\). For every held value \(b\), the Gibbs denominator is also
positive because its \(y=0\) term is \(w(0)\).

The residues split into the disjoint sets

\[
 R=R^\times\ \dot\cup\ H_N\ \dot\cup\ \{0\}.
\]

Indeed, a residue outside \(H_N\) has gcd either \(1\) or \(N\), and the latter
case is only the zero residue.

## 1. The zero-residual conditional target

Every pair in \(\Omega_N\) has the same unnormalized weight \(w(0)\). Hence,
for each \((k,x)\in R^2\),

\[
 \Pr_{\pi_w}[(K,X)=(k,x)\mid KX=0]
 =
 \begin{cases}
  1/|\Omega_N|,&(k,x)\in\Omega_N,\\
  0,&(k,x)\notin\Omega_N.
 \end{cases}
\]

Thus the conditional target is exactly uniform on \(\Omega_N\). The event being
conditioned on has positive probability because \(w(0)>0\).

For completeness, fixing the second coordinate \(b\) gives exactly
\(\gcd(b,N)\) choices of the first coordinate with \(ab=0\). Therefore

\[
 |\Omega_N|=\sum_{b\in R}\gcd(b,N)
 =\sum_{g\mid N}g\,\varphi(N/g).
\]

No regularity or positivity away from zero is needed.

## 2. The two elementary refresh laws

Let \(b\in R^\times\). Multiplication by \(b\) is a permutation of \(R\), so

\[
 \sum_{y\in R}w(yb)=\sum_{d\in R}w(d)=W.
\]

If \(A\sim Q_{b,w}\) and \(D=Ab\), then, for each \(d\in R\), there is one
possible value \(A=db^{-1}\), and

\[
 \Pr[D=d]=Q_{b,w}(db^{-1})=\frac{w(d)}{W}=\nu_w(d).
\]

Thus a refresh opposite a held unit makes the new residual have law \(\nu_w\).

If \(b=0\), then every candidate has residual zero and

\[
 Q_{0,w}(a)=\frac{w(0)}{\sum_{y\in R}w(0)}
 =\frac1N.
\]

Thus a refresh opposite a held zero makes the refreshed coordinate uniform on
\(R\), while the residual stays zero.

## 3. A useful exact residual sampler already factors directly

Here is the fully uniform formulation of the hypothesis. Let \(\mathcal N\) be
the promised family of composite inputs, and let
\(\lambda=\lceil\log_2N\rceil\). Suppose there are fixed polynomials \(P,p\) and
one public probabilistic algorithm, with no advice depending on \(N\), such that
for every \(N\in\mathcal N\):

1. On the binary input \(N\), it constructs a description of \(w_N\) of at most
   \(P(\lambda)\) bits.
2. From that description it samples exactly from \(Q_{1,w_N}\).
3. The expected construction cost and each expected sampling cost, counting all
   bit operations and all requested independent fair bits, are at most
   \(P(\lambda)\). The same fixed polynomial works for all inputs.
4. \(\theta_{w_N}\geq 1/p(\lambda)\).

The exact representation of the weights and the work needed to sample from them
are part of this hypothesis; they are not free oracles.

Since \(1\) is a unit, Section 2 gives

\[
 Q_{1,w_N}(a)=\nu_{w_N}(a).
\]

Construct the description once. Make independent sampler calls using fresh fair
bits. After each output \(A_i\), compute

\[
 g_i=\gcd(A_i,N).
\]

Stop when \(1<g_i<N\), and output \(g_i\). A trial succeeds exactly when
\(A_i\in H_N\), so its success probability is exactly \(\theta_{w_N}\). The
number \(T\) of trials is geometric and

\[
 \mathbb E T=\frac1{\theta_{w_N}}\leq p(\lambda).
\]

The Euclidean algorithm has polynomial bit cost in \(\lambda\). If \(C_i\) is
the sampling cost of trial \(i\), it may be correlated with that trial's output.
This causes no problem: the event \(\{T\geq i\}\) depends only on earlier trials
and is independent of \(C_i\). By Tonelli's theorem,

\[
 \mathbb E\!\left[\sum_{i=1}^{T}C_i\right]
 =\sum_{i\geq1}\Pr[T\geq i],\mathbb E C_i
 \leq \frac{P(\lambda)}{\theta_{w_N}}.
\]

The same calculation applies to the number of fair bits. Adding construction
and gcd costs leaves one fixed expected polynomial bound. This is a direct
randomized factoring reduction; it never initializes or runs a Gibbs chain.
For prime inputs the premise cannot hold because \(H_N=\varnothing\), so the
claim is naturally an implication on the promised composite family.

## 4. Per-refresh hazard under every allowed scan

Consider any one-coordinate Gibbs process \((K_t,X_t)_{t\geq0}\), and put
\(D_t=K_tX_t\). At refresh \(t\geq1\), a scan rule selects one coordinate, holds
the other coordinate \(b\), and samples the selected coordinate from
\(Q_{b,w}\).

The scan can be deterministic, randomly scheduled, or adaptive. Formally, its
choice at time \(t\) may have any distribution measurable with respect to the
past and any scan randomness revealed before the fresh Gibbs draw. It cannot
look at that fresh draw before choosing the coordinate.

Define the monitored hit time

\[
 \tau=\inf\{t\geq1:K_t\in H_N\ \text{or}\ X_t\in H_N\ \text{or}\ D_t\in H_N\},
\]

with \(\inf\varnothing=\infty\). A **safe start** means that the initial law is
supported on states for which none of \(K_0,X_0,D_0\) is in \(H_N\). The proof
allows every such initial law; any additional conventional warmness condition
is irrelevant.

Condition on the complete past, on the selected coordinate, and on
\(\{\tau>t-1\}\). The held value \(b\) is not in \(H_N\), so it is either a unit
or zero.

* If \(b\) is a unit, Section 2 says that the new residual has law \(\nu_w\).
  Also
  \(\gcd(ab,N)=\gcd(a,N)\), since multiplication by a unit preserves gcd with
  \(N\). The held coordinate is already safe. Consequently the new state is a
  hit exactly when the new residual (equivalently, the refreshed coordinate) is
  in \(H_N\). Its conditional probability is exactly \(\theta_w\).
* If \(b=0\), the new residual and held coordinate are both zero. The refreshed
  coordinate is uniform on \(R\), so the conditional hit probability is exactly
  \(h_N/N\).

Thus, for

\[
 \rho=\max\!\left(\theta_w,\frac{h_N}{N}\right),
\]

the hazard at every refresh before the first hit is at most \(\rho\), even after
conditioning on an arbitrary past-measurable scan decision. Randomizing that
decision only takes a mixture of the two displayed hazards.

Both terms are strictly below one. Indeed, \(H_N\) excludes zero, so
\(h_N\leq N-1\); and \(w(0)>0\) gives
\(\theta_w\leq1-w(0)/W<1\). It follows recursively that, for every integer
\(t\geq0\),

\[
 \Pr(\tau>t)\geq(1-\rho)^t.
\]

Therefore

\[
 \Pr(\tau\leq t)
 \leq 1-(1-\rho)^t
 \leq t\rho
\]

(and of course the right side can be replaced by \(\min(1,t\rho)\)). If
\(\rho>0\), the tail-sum identity for an extended nonnegative integer-valued
random variable gives

\[
 \mathbb E\tau
 =\sum_{t\geq0}\Pr(\tau>t)
 \geq\sum_{t\geq0}(1-\rho)^t
 =\frac1\rho.
\]

If \(\rho=0\), the same conditional argument gives \(\tau=\infty\) almost
surely. This covers the prime case, where \(H_N=\varnothing\).

## 5. Exact counts and asymptotic endpoints

Let \(N=pq\) for distinct primes. The elements of \(H_N\) are the nonzero
multiples of \(p\) and the nonzero multiples of \(q\). These two sets are
disjoint, with respective sizes \(q-1\) and \(p-1\). Hence

\[
 h_N=p+q-2,
 \qquad
 \frac{h_N}{N}=\frac1p+\frac1q-\frac2{pq}.
\]

For a balanced family, meaning that \(q/p\) is bounded above by one constant
after labeling \(p<q\), both primes are \(\Theta(\sqrt N)\). Thus

\[
 \frac{h_N}{N}=O(N^{-1/2}),
\]

with a constant uniform over that balanced family.

If \(N=p^2\), then

\[
 H_N=\{p,2p,\ldots,(p-1)p\},\qquad h_N=p-1,
\]

and therefore

\[
 \frac{h_N}{N}=\frac{p-1}{p^2}<\frac1p=N^{-1/2}.
\]

These counts yield two precise endpoint statements. Let
\(\lambda=\lceil\log_2N\rceil\), and consider either family above.

* **Negligible-hit endpoint.** The coordinate term \(h_N/N\) is negligible in
  \(\lambda\). If \(\theta_{w_N}\) is also negligible in \(\lambda\), then for
  every polynomial \(T\),
  \[
    \Pr(\tau\leq T(\lambda))
    \leq T(\lambda)\left(\theta_{w_N}+O(N^{-1/2})\right)
  \]
  is negligible. Also \(\mathbb E\tau\) is larger than every polynomial in
  \(\lambda\) (or is infinite).
* **Square-root endpoint.** If, for some fixed polynomial \(L\),
  \[
    \theta_{w_N}\leq \frac{L(\lambda)}{\sqrt N},
  \]
  then
  \[
    \rho=O\!\left(\frac{\operatorname{poly}(\lambda)}{\sqrt N}\right),
    \qquad
    \mathbb E\tau
    =\Omega\!\left(\frac{\sqrt N}{\operatorname{poly}(\log N)}\right).
  \]
  In particular, \(\theta_{w_N}=0\) gives the stronger
  \(\mathbb E\tau=\Omega(\sqrt N)\).

The rate condition in the second bullet is necessary for that particular
conclusion. For example, a function can be negligible in \(\lambda\) while
being much larger than \(2^{-\lambda/2}\). Negligibility alone then gives a
superpolynomial lower bound through \(1/\theta_{w_N}\), not necessarily a
\(\sqrt N/\operatorname{poly}(\log N)\) lower bound.

## 6. Scope of the reduction

For this local residual-only construction, there is no factor-mass
amplification. Before a hit, every refresh has one of only two factor hazards:
\(\theta_w\), which is exactly the mass already present in a direct residual
draw, or \(h_N/N\), which is the uniform-coordinate baseline. Repeated local
refreshes can repeat these opportunities, but cannot make either per-refresh
hazard larger. If the first hazard is uniformly useful and its exact sampler is
uniformly constructible, Section 3 uses it directly without the wrapper.

This statement does **not** cover, and therefore leaves open:

* moves that update both coordinates jointly;
* weights that depend jointly on more than the single residual \(kx\);
* systems with interacting residuals;
* lifts to a larger ring, integer space, or other augmented state space;
* decoders that use global trajectory information instead of the monitored gcd
  events; and
* the existence or construction of a public, uniform, efficient exact residual
  sampler with useful factor mass.

Finally, the hazard bound is a statement about this chain and this monitored hit
event. It is not a computational lower bound for arbitrary factoring
algorithms. In particular, it neither rules out other information in a
trajectory nor proves any general lower bound for integer factoring.
