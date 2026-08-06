# Verdict: RECONSTRUCTED

This is a proof-blind reconstruction from the theorem package in the assignment.  No
candidate proof, audit report, or pre-existing `F33*` artifact was consulted.  The
factorization and perfect-matching statements below are conditional implications:
they do not assert that the required sampler or graph representation has been
constructed.

## 1. The positive lift and the quadratic Fourier energy

Write \(\mathbb Z_N=\mathbb Z/N\mathbb Z\), and, for \(N\geq 1\), put

\[
 \Omega_N=\{(k,x)\in\mathbb Z_N^2:kx=0\}.
\]

For a fixed \(k\), let \(d=(k,N)\).  Write \(k=dk_0\) and
\(N=dN_0\), where \((k_0,N_0)=1\).  Then

\[
 kx=0\pmod N\quad\Longleftrightarrow\quad N_0\mid x.
\]

There are exactly \(d\) such residue classes \(x\pmod N\), namely
\(x=jN_0\) for \(0\leq j<d\).  Consequently

\[
 |\Omega_N|=S(N):=\sum_{k\bmod N}(k,N),
 \qquad
 \Pr_{\operatorname{Unif}(\Omega_N)}[K=k]=\frac{(k,N)}{S(N)}.       \tag{1}
\]

For odd \(N\), define

\[
 G_N(k)=\sum_{y\bmod N}\exp(2\pi i k y^2/N).
\]

Because \(2\) is invertible modulo \(N\), the change of variables
\((u,v)=(y-z,y+z)\) is a bijection of \(\mathbb Z_N^2\).  Additive-character
orthogonality therefore gives

\[
\begin{aligned}
 |G_N(k)|^2
 &=\sum_{y,z\bmod N}\exp(2\pi i k(y^2-z^2)/N)\\
 &=\sum_{u,v\bmod N}\exp(2\pi i kuv/N)\\
 &=N\,|\{u\bmod N:ku=0\}|\\
 &=N(k,N).                                                    \tag{2}
\end{aligned}
\]

Thus \(\sum_k|G_N(k)|^2=NS(N)\), and the normalized Fourier-energy
distribution is exactly the first marginal in (1).

## 2. Proper-gcd probability for every odd composite

Call \((k,x)\in\Omega_N\) **useful** when

\[
 1<(k,N)<N\quad\text{or}\quad 1<(x,N)<N.
\]

If a point is not useful, each coordinate is either a unit or zero.  Two units
cannot have product zero modulo \(N>1\).  Hence the non-useful set is exactly the
disjoint union

\[
 (\mathbb Z_N^\times\times\{0\})\ \dot\cup\
 (\{0\}\times\mathbb Z_N^\times)\ \dot\cup\ \{(0,0)\},       \tag{3}
\]

and has size \(2\varphi(N)+1\).

We now prove, separately for the two possible kinds of odd composite, the
inequality needed for a constant useful mass.  The identity

\[
 (k,N)=\sum_{d\mid(k,N)}\varphi(d)
\]

implies

\[
 S(N)=\sum_{d\mid N}\frac Nd\varphi(d).                       \tag{4}
\]

In particular, \(S\) is multiplicative, and

\[
 S(p^a)=p^a+a p^{a-1}(p-1)
       =p^{a-1}((a+1)p-a).                                    \tag{5}
\]

*Prime powers.*  Let \(N=p^a\), where \(p\) is odd and \(a\geq2\).  From
(5),

\[
\begin{aligned}
 S(p^a)-3\varphi(p^a)
 &=p^{a-1}\bigl((a-2)(p-1)+1\bigr)\\
 &\geq p^{a-1}\geq3.                                         \tag{6}
\end{aligned}
\]

*At least two distinct prime divisors.*  For every \(a\geq1\),

\[
 \frac{S(p^a)}{\varphi(p^a)}=a+\frac p{p-1}>2.                \tag{7}
\]

If \(N\) has at least two distinct prime divisors, multiplicativity makes
\(S(N)/\varphi(N)>4\).  Here \(\varphi(N)\geq2\) (indeed it is at least
\(8\) for an odd number with two distinct prime divisors), so in particular
\(S(N)\geq3\varphi(N)+2\).

Both cases imply

\[
 2S(N)\geq6\varphi(N)+3.
\]

Using (3), the useful probability under the uniform law on \(\Omega_N\) is

\[
 1-\frac{2\varphi(N)+1}{S(N)}\geq\frac13.                     \tag{8}
\]

This includes odd prime powers; squarefreeness is nowhere assumed.

## 3. The local \(H,V,O\) description for \(N=pq\)

In this section only, let \(p\ne q\) be primes and \(N=pq\).  CRT identifies
\(\Omega_N\) with \(\Omega_p\times\Omega_q\).  Over the field
\(\mathbb F_r\), every local point has exactly one of the types

\[
 H=(k_r\ne0,x_r=0),\qquad
 V=(k_r=0,x_r\ne0),\qquad
 O=(k_r=0,x_r=0).                                             \tag{9}
\]

For a global coordinate \(z\), its residues at \((p,q)\) determine its gcd:
nonzero/nonzero gives gcd \(1\), zero/zero gives gcd \(N\), and exactly one
zero gives the corresponding proper prime gcd.  It follows at once that the
global point is useful if and only if its two local types differ:

* \((H,H)\), \((V,V)\), and \((O,O)\) give respectively unit/zero,
  zero/unit, and the global origin, so none is useful;
* \((H,V)\) and \((V,H)\) expose both proper prime gcds;
* \((H,O)\) and \((O,H)\) expose a proper gcd through \(k\);
* \((V,O)\) and \((O,V)\) expose a proper gcd through \(x\).

Thus local origins are part of, rather than exceptions to, the mismatch rule.

There is an essential prime-power caveat.  This argument uses two distinct CRT
field components and does not apply with \(q=p\).  Reduction modulo the single
prime also loses valuation information: for \(a\geq2\), for example,
\((p,p^{a-1})\in\Omega_{p^a}\) reduces locally to \(O\), while both coordinates
have proper gcd with \(p^a\).  Prime powers are covered by the separate counting
argument (6), not by an \(H,V,O\) mismatch claim.

## 4. A TV-approximate positive-lift sampler implies Las Vegas factoring

Here is the precise conditional hypothesis.  There is one uniform randomized
algorithm \(A\) and one fixed polynomial \(P\) such that, for every odd
\(M\geq3\):

1. \(A(M)\) terminates almost surely and always returns an encoded pair in
   \(\Omega_M\);
2. its output law \(\mu_M\) satisfies
   \(\|\mu_M-\operatorname{Unif}(\Omega_M)\|_{\rm TV}\leq1/12\), where
   total variation is \(\sup_E|\mu_M(E)-\pi_M(E)|\);
3. its expected bit-operation cost and its expected number of independent fair
   bits are each at most \(P(\lceil\log_2(M+1)\rceil)\);
4. every invocation is a fresh instance using a random tape independent of all
   earlier invocations.

The last item can equivalently be replaced by the stronger condition that the
same three guarantees hold conditionally on every prior history.  A mere
one-call marginal guarantee with arbitrarily dependent retries would not imply
almost-sure success, so freshness is a necessary part of the reduction.

Let \(U_M\) be the useful event.  By (8) and the defining event inequality for
total variation,

\[
 \mu_M(U_M)\geq\frac13-\frac1{12}=\frac14.                    \tag{10}
\]

On an odd composite \(M\), repeatedly run a fresh copy of \(A(M)\).  Reduce and
range-check the returned residues, verify \(kx=0\pmod M\), compute
\((k,M)\) and \((x,M)\), and accept only a value \(d\) satisfying
\(1<d<M\) and \(d\mid M\).  Under the hypothesis the membership check always
passes; the other checks ensure that no incorrect divisor can ever be returned.
By (10), the number \(T\) of trials obeys

\[
 \Pr(T>t)\leq(3/4)^t,
\]

so it is finite almost surely and \(\mathbb E T\leq4\).

It remains important not to multiply expectations without justifying the
stopping.  Let \(C_i\) be the cost of the sampler and verification in trial
\(i\), and enlarge \(P\) by a fixed polynomial for modular multiplication and
Euclidean gcd.  The event \(\{T\geq i\}\) depends only on the first \(i-1\)
fresh tapes and is independent of \(C_i\).  Tonelli's theorem for nonnegative
costs gives

\[
\begin{aligned}
 \mathbb E\!\left[\sum_{i=1}^{T}C_i\right]
 &=\sum_{i\geq1}\mathbb E[\mathbf1_{\{T\geq i\}}C_i]\\
 &\leq\sum_{i\geq1}(3/4)^{i-1}P(n)\\
 &\leq4P(n).                                                  \tag{11}
\end{aligned}
\]

The identical calculation applies to fair-bit cost.  It does not assume that
the cost and success of the *same* trial are independent.

For completeness, factor an arbitrary binary input \(N\geq2\) as follows.
First remove its exact power of two.  On every remaining factor \(m>1\), run a
deterministic polynomial-time primality test (for example AKS).  If it is prime,
record it.  If it is odd composite, obtain a verified proper divisor \(d\) by
the retry procedure and recurse exactly on \(d\) and \(m/d\).  Finally combine
equal prime leaves and their multiplicities.  This handles primes, even
integers, repeated prime factors, odd prime powers, and arbitrary composites.

Every integer in the recursion is a divisor of \(N\) and has at most \(n\)
bits.  If the prime leaves are counted with multiplicity, their number \(L\)
satisfies \(2^L\leq N\), hence \(L\leq n\).  A binary splitting tree has at most
\(L-1\) composite internal nodes and at most \(2L-1\) total nodes.  Thus there
are deterministically \(O(n)\) primality tests, gcds, exact divisions, and
sampler-based splits, all on \(O(n)\)-bit integers.

For an explicit stopped-cost argument over the adaptive recursion, traverse the
tree depth first and number its sampler nodes in order, padding with zero-cost
nodes up to \(n\).  Conditional on the complete history before any existing
node, its input is a fixed odd composite of at most \(n\) bits and (11) bounds
its expected cost by the same fixed polynomial \(4P(n)\).  The tower property
then bounds the total expected sampler cost by \(4nP(n)\); deterministic work
adds another fixed polynomial.  The fair-bit bound is the same.  Every retry
terminates almost surely, every retry sequence succeeds almost surely, and
there are at most \(n\) such sequences, so the whole recursion terminates almost
surely.  Every recorded leaf is certified prime and every split is an exact
divisor identity, proving both Las Vegas correctness and a fixed all-input
polynomial expected bit bound.

## 5. The equal-positive-fibre perfect-matching bridge

The following is the precise computational bridge; an existential encoding
alone is insufficient.  Suppose there are **uniform** deterministic algorithms
\(B,D\) with these properties for every odd \(M\):

* in time polynomial in \(\log M\), \(B(M)\) constructs an explicit bipartite
  graph \(G_M\) of size polynomial in \(\log M\);
* \(D(M,\mathcal M)\), on a standard encoding of any perfect matching
  \(\mathcal M\) of \(G_M\), runs in deterministic polynomial time and outputs
  an \(O(\log M)\)-bit pair in \(\Omega_M\);
* there is an integer \(c_M\geq1\) such that, for every
  \(\omega\in\Omega_M\),

  \[
   |\{\mathcal M\in\operatorname{PM}(G_M):D(M,\mathcal M)=\omega\}|=c_M.
                                                                    \tag{12}
  \]

Positivity in (12) implies that \(G_M\) has a perfect matching and that the
decoder is onto.  If \(\mathcal U_M\) is uniform on the perfect matchings, then

\[
 \Pr[D(M,\mathcal U_M)=\omega]
 =\frac{c_M}{c_M|\Omega_M|}=\frac1{|\Omega_M|}.                \tag{13}
\]

The standard uniform almost-uniform generator for perfect matchings of an
explicit bipartite graph (equivalently, the permanent FPRAS plus the usual
self-reduction) can, for fixed accuracy \(1/12\), produce a perfect matching
with law \(\nu_M\) satisfying
\(\|\nu_M-\mathcal U_M\|_{\rm TV}\leq1/12\), using a fixed polynomial number
of bit operations and fair random bits in the graph size.  It can first test
perfect-matching existence deterministically; here existence is already
guaranteed by (12).  This is a uniform randomized algorithm and terminates
almost surely (indeed, standard bounded-run implementations do).

Total variation cannot increase under a deterministic map: for every event
\(E\subseteq\Omega_M\), its decoded probability difference is the original
difference on \(D^{-1}(E)\).  Hence (13) gives

\[
 \|D_*\nu_M-\operatorname{Unif}(\Omega_M)\|_{\rm TV}\leq1/12. \tag{14}
\]

The graph has polynomial size, the matching has polynomial encoding length,
and the uniform deterministic decoder emits only the two \(O(\log M)\)-bit
residues.  Therefore the composed graph-builder/matching-sampler/decoder has
the exact uniformity, termination, fair-bit, and bit-complexity properties
required in Section 4.  Fresh independent runs of the matching sampler give
the required fresh-call condition.

This bridge is deliberately conditional on the uniform polynomial-time builder
and decoder.  Equal fibre cardinalities without algorithms, a graph of size
polynomial in \(M\) rather than \(\log M\), a nonuniform family, or a decoder
requiring unknown factors does not establish the factoring consequence.

## 6. Exact random-scan coordinate heat bath

For any \(N\geq2\) and \(a\in\mathbb Z_N\), write

\[
 \operatorname{Ann}(a)=\{z\in\mathbb Z_N:az=0\}.
\]

If \(d=(a,N)\), the fibre calculation in Section 1 gives

\[
 \operatorname{Ann}(a)=\{j(N/d):0\leq j<d\}.                  \tag{15}
\]

There is an exact efficient fair-bit sampler for (15).  If \(d=1\), return
\(j=0\).  Otherwise set \(\ell=\lceil\log_2 d\rceil\), read \(\ell\) fair bits
as a uniform integer \(J\in[0,2^\ell)\), accept when \(J<d\), and repeat on
rejection.  The acceptance probability is greater than \(1/2\), so the sampler
terminates almost surely, uses fewer than two attempts in expectation, and uses
fewer than \(2\ell\) fair bits in expectation.  Euclid's algorithm, exact
division, and the multiplication \(J(N/d)<N\) have polynomial bit cost in
\(\log N\).

The exact random-scan heat-bath chain on \(\Omega_N\) is:

* with probability \(1/2\), keep \(k\) and draw
  \(x'\sim\operatorname{Unif}(\operatorname{Ann}(k))\);
* with probability \(1/2\), keep \(x\) and draw
  \(k'\sim\operatorname{Unif}(\operatorname{Ann}(x))\).

One fair bit chooses the coordinate, and the sampler above performs the update
exactly with almost-sure termination and expected polynomial bit/fair-bit cost.

For two distinct states differing only in \(x\), the transition probability in
either direction is

\[
 \frac1{2|\operatorname{Ann}(k)|};
\]

the analogous equality holds for states differing only in \(k\), and states
differing in both coordinates have transition probability zero in both
directions.  Thus the transition matrix is symmetric.  Uniform measure on
\(\Omega_N\) satisfies detailed balance and is stationary.

The chain is irreducible: from any \((k,x)\) one can, with positive probability,
follow

\[
 (k,x)\longrightarrow(k,0)\longrightarrow(k',0)
             \longrightarrow(k',x')
\]

for any target \((k',x')\in\Omega_N\).  The middle update is possible because
\(\operatorname{Ann}(0)=\mathbb Z_N\), and the last because
\(x'\in\operatorname{Ann}(k')\).  Finally, every state has a positive self-loop:
choose either coordinate and resample its current value.  Hence the finite
chain is aperiodic.

## 7. Exact cold-start obstruction for \(N=pq\)

Let now \(p\ne q\) be odd primes, \(N=pq\), and

\[
 h=p+q-2,\qquad \varphi(N)=(p-1)(q-1)=N-h-1.                  \tag{16}
\]

Among residues modulo \(N\), the nonzero nonunits are the \(q-1\) nonzero
multiples of \(p\) and the \(p-1\) nonzero multiples of \(q\), a disjoint set
of size \(h\).  Let \(\mathcal B\) be the useful set and start the chain at
\((1,0)\).  Before hitting \(\mathcal B\), the state lies in one of the two
unit arms from (3), or at the origin.  From a unit arm, one coordinate update is
frozen and the other hits a nonzero nonunit with probability \(h/N\), so the
one-step hit probability is \(h/(2N)\).  At the origin, either chosen coordinate
is uniform modulo \(N\), so the one-step hit probability is \(h/N\).

The mean can be solved exactly.  Let \(E\) be the expected hitting time from
either unit arm and \(F\) that from the origin.  First-step analysis yields

\[
\begin{aligned}
 E&=1+\left(\frac12+\frac{\varphi(N)}{2N}\right)E
       +\frac1{2N}F,\\
 F&=1+\frac{\varphi(N)}N E+\frac1N F.
\end{aligned}                                                   \tag{17}
\]

Equivalently,

\[
 (h+1)E-F=2N,\qquad (N-1)F-\varphi(N)E=N.
\]

Since \((N-1)(h+1)-\varphi(N)=Nh\), solving gives

\[
 \mathbb E_{(1,0)}\tau_{\mathcal B}=E=\frac{2N-1}{h}
 \geq\frac Nh.                                                 \tag{18}
\]

In particular the factor-exposure hitting expectation is
\(\Omega(N/h)\).

For the mixing bound, multiplicativity gives

\[
 S(N)=(2p-1)(2q-1)=4N-2h-3.
\]

By (3), the useful set has size

\[
 S(N)-(2\varphi(N)+1)=2N-2,
\]

so its stationary mass is

\[
 \pi(\mathcal B)=\frac{2N-2}{4N-2h-3}>\frac12.                \tag{19}
\]

At every pre-hit state the conditional one-step hit probability is at most
\(h/N\).  Therefore, for every integer \(t\geq0\),

\[
 \Pr_{(1,0)}(\tau_{\mathcal B}\leq t)\leq \frac{th}{N}.       \tag{20}
\]

Put \(t_0=\lfloor N/(8h)\rfloor\).  Since being in \(\mathcal B\) at time
\(t_0\) requires having hit it,

\[
\begin{aligned}
 \|P^{t_0}((1,0),\cdot)-\pi\|_{\rm TV}
 &\geq \pi(\mathcal B)-\Pr_{(1,0)}(X_{t_0}\in\mathcal B)\\
 &>\frac12-\frac18=\frac38>\frac14.                           \tag{21}
\end{aligned}
\]

For the standard worst-start definition
\(t_{\rm mix}(1/4)=\min\{t:\max_z\|P^t(z,\cdot)-\pi\|_{\rm TV}\leq1/4\}\),
(21) proves (in fact slightly more than)

\[
 t_{\rm mix}(1/4)\geq\left\lfloor\frac{N}{8h}\right\rfloor. \tag{22}
\]

Along any balanced semiprime family, meaning \(p,q=\Theta(\sqrt N)\) (or,
equivalently, their ratio stays between two fixed positive constants),
\(h=\Theta(\sqrt N)\).  Equations (18) and (22) are then
\(\Omega(\sqrt N)\) lower bounds; the floor changes only finitely many small
members of such a family.

These are deliberately cold-start and kernel-specific statements.  They do not
give a lower bound from a warm start: stationarity itself is the extreme
counterexample, and the event estimate (20) uses the particular start
\((1,0)\).  Nor do they apply to a block update, a nonlocal move, a chain on an
augmented state space, a lifted or tempered chain, a systematic scan, or any
other modified transition kernel.  Such a kernel can cross CRT type sectors in
a way the exact single-coordinate random-scan chain cannot.  Finally, the
\(pq\) calculation assumes distinct primes and must not be transferred to
prime powers; Section 3 explains the valuation obstruction.

## 8. Edge and scope audit

* The Fourier identity needs odd \(N\) solely because the
  \((y-z,y+z)\) change of variables uses \(2^{-1}\); the positive lift itself
  and the heat-bath construction work for every \(N\).
* The \(1/3\) useful-mass bound was proved separately for odd prime powers and
  for composites with multiple distinct prime factors.
* The sampler loss is exactly \(1/12\) in total variation, leaving success
  probability \(1/4\); no pointwise approximation is assumed.
* Fresh independent random tapes are used exactly where the geometric tail and
  stopped-cost sum need them.  Runtime may remain correlated with success within
  a call.
* All sampler outputs are verified, every arithmetic operand has
  \(O(\log N)\) bits, recursion has \(O(\log N)\) nodes, and fair-bit costs are
  included.
* No finite computation, benchmark, unknown factor, or unproved mixing claim is
  used.
