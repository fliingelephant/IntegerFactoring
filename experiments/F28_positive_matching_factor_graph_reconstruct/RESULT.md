# Independent reconstruction: positive matching factor graphs

## Decision

**RECONSTRUCTED.**

Statement A follows, conditionally, from the stated builder/decoder hypotheses and the Jerrum--Sinclair--Vigoda (JSV) almost-uniform sampler.  Statement B is an unconditional support obstruction for terminal-deletion signatures.

There are two important traps, but neither is a gap after the constructions below.

1. Giving every nonedge activity \(1/m!\) does **not** make the total weight of bogus perfect matchings negligible.  It only makes that weight at most \(1\), hence makes a genuine perfect matching occur with probability at least \(1/2\).  Sending one bogus sample to a fixed matching could therefore be far from uniform.  The sampler below instead performs a bounded conditioning/rejection step and uses the fixed matching only on the low-probability no-acceptance event.
2. A small-probability bad empirical estimate cannot be ignored in an expected-time proof: on such a path the nominal rapid-mixing hypothesis may fail.  Every chain is therefore run for a predetermined polynomial number of steps, zero empirical counts cause an immediate detectable fallback, and positive but inaccurate estimates are charged to one global event \(E\).  Thus even paths in \(E\) have polynomial expected cost.

The only imported theorem is the standard JSV rapid-mixing theorem for its perfect/near-perfect matching chain.  No factoring claim is imported.  A primary reference is M. Jerrum, A. Sinclair, and E. Vigoda, *A polynomial-time approximation algorithm for the permanent of a matrix with non-negative entries*, J. ACM 51 (2004), 671--697.

---

## A. From an equal-fiber matching representation to Las Vegas factoring

### A.1 The effective JSV lemma needed here

The following is the precise standard consequence of the JSV chain that will be used.

**Lemma 1 (effective fair-bit JSV sampler).**  Let \(G=(L,R,E)\) be an unweighted bipartite graph with \(|L|=|R|=m\), and suppose that \(G\) has a perfect matching.  There is a randomized algorithm using only fair random bits which:

* always returns a perfect matching consisting only of edges of \(G\);
* has output law \(Q_G\) satisfying

  \[
  d_{\mathrm{TV}}(Q_G,U_G)\leq \frac1{12},
  \]

  where \(U_G\) is uniform on the perfect matchings of \(G\);
* terminates almost surely; and
* has expected fair-bit use and expected bit complexity bounded by fixed polynomials in \(m\).

Here is a complete implementation audit of this lemma, including the failure paths that are often suppressed in presentations of JSV.

#### The weighted chain

Work temporarily in the complete bipartite graph \(K_{m,m}\).  Give every edge a positive rational activity \(\lambda(e)\).  Let \(\mathcal P\) be its perfect matchings and let \(\mathcal N(u,v)\) be its near-perfect matchings whose uncovered vertices are \(u\in L\) and \(v\in R\).  Put

\[
Z_P=\sum_{M\in\mathcal P}\prod_{e\in M}\lambda(e),\qquad
Z_{uv}=\sum_{M\in\mathcal N(u,v)}\prod_{e\in M}\lambda(e).
\]

All activities are positive, so every \(Z_{uv}\) is positive.  The ideal hole activity is

\[
h^*_{uv}=\frac{Z_P}{Z_{uv}}.
\]

For positive rational hole activities \(h_{uv}\), give a perfect matching \(M\) weight

\[
\Gamma(M)=\prod_{e\in M}\lambda(e)
\]

and a near-perfect matching \(M\in\mathcal N(u,v)\) weight

\[
\Gamma(M)=h_{uv}\prod_{e\in M}\lambda(e).
\]

The JSV chain is the lazy Metropolis chain on

\[
\Omega=\mathcal P\mathbin{\dot\cup}\bigcup_{u,v}\mathcal N(u,v).
\]

From a perfect matching it proposes deleting a uniformly selected matched edge.  From a near-perfect matching it chooses a uniformly selected vertex and proposes either filling the two holes or moving one hole by the usual one-edge exchange.  The proposal probabilities in opposite directions agree; the proposal is accepted with probability

\[
\min\{1,\Gamma(M')/\Gamma(M)\},
\]

and an extra \(1/2\) holding probability makes the chain lazy.  Thus its stationary law is \(\pi(M)\propto\Gamma(M)\).

The JSV rapid-mixing theorem says that if

\[
\frac12h^*_{uv}\leq h_{uv}\leq2h^*_{uv}\quad\text{for every }u,v,
\tag{1}
\]

then, from a perfect matching of maximum edge activity, an endpoint within any prescribed TV error \(\delta>0\) is obtained in

\[
\operatorname{poly}\bigl(m,\log(1/\delta),\log(1/\pi(M_0))\bigr)
\tag{2}
\]

steps.  This is the sole substantive black-box theorem from JSV.

In every good phase used below, \(M_0\) has weight \(1\), while

\[
\sum_{M\in\Omega}\Gamma(M)\leq(1+2m^2)Z_P\leq(1+2m^2)m!.
\]

Thus \(\log(1/\pi(M_0))=O(m\log(m+1))\), so the last argument of the polynomial in (2) is harmless.

#### Cooling schedule and number of estimates

First find a perfect matching \(M_0\) of \(G\) deterministically by bipartite matching.  The hypothesis guarantees that this succeeds.  Give every edge of \(K_{m,m}\) activity \(1\), for which

\[
Z_P=m!,\qquad Z_{uv}=(m-1)!,\qquad h^*_{uv}=m.
\]

Initialize every \(h_{uv}\) to \(m\).  Leave original edges at activity \(1\).  Process nonedges one at a time.  For the currently selected nonedge, repeatedly multiply its activity by \(3/4\) while this stays at least \(1/m!\); on the last step set it exactly to \(1/m!\).  Every activity change is therefore by a factor

\[
r\in[3/4,1].
\]

There are at most \(m^2\) nonedges and

\[
O(\log(m!))=O(m\log m)
\]

changes per nonedge.  Hence the number \(L\) of cooling phases is

\[
L=O(m^3\log(m+1)).
\tag{3}
\]

Changing one edge activity by \(r\) multiplies the weight of each matching by either \(r\) or \(1\).  Consequently both \(Z_P\) and every \(Z_{uv}\) change by a factor in \([r,1]\), and each ideal ratio \(h^*_{uv}\) changes by a factor in \([r,1/r]\).

At the current activities, if (1) holds, sample endpoints of independent chain runs and count the perfect class and every hole class.  If their stationary probabilities are \(p_P,p_{uv}\), then

\[
\frac{h_{uv}}{h^*_{uv}}=\frac{p_{uv}}{p_P},
\qquad
h^*_{uv}=h_{uv}\frac{p_P}{p_{uv}}.
\tag{4}
\]

Use the corresponding empirical count ratio to replace \(h_{uv}\).  Fixed relative accuracy in all class counts gives, say,

\[
\frac56h^*_{uv}\leq \widehat h_{uv}\leq\frac65h^*_{uv}.
\tag{5}
\]

After the next \(3/4\)-or-milder activity change, the old refined estimate is still within factor

\[
\frac65\cdot\frac43=\frac85<2
\]

of the new ideal value, so the JSV mixing hypothesis propagates inductively.

There are \(m^2\) hole ratios to estimate in each of the \(L\) phases.  Thus there are

\[
O(m^5\log(m+1))
\tag{6}
\]

individual empirical estimates.  This is the requested estimate count.  A common sample of size

\[
S=O\bigl(m^2\log(L(m^2+1))\bigr)
\tag{7}
\]

per phase suffices for all of them.  Indeed, under (1), every perfect or specified hole class has stationary probability at least \(1/(6m^2)\) for \(m\geq2\).  Multiplicative Chernoff bounds and a union bound then give the fixed accuracy in (5).  Each endpoint sample is obtained from a fresh chain run, so the ideal comparison samples may be taken independent.  Taking the endpoint TV tolerance small enough to couple all endpoint samples simultaneously costs only an additional logarithmic factor in (2).

#### One global empirical failure event

Make the preceding statement explicit.  At every phase, conditional on all previous estimates being good, couple each approximate endpoint to an independent stationary endpoint.  Let \(E\) be the union of:

* any failure of any such coupling; and
* any failure of any required empirical class count to have its prescribed relative accuracy.

Choose the per-run mixing errors so that all coupling failures have total probability at most \(1/48\), and choose the Chernoff error budgets so that all count failures have total probability at most \(1/48\).  Conditional union bounds remain valid although the weights are chosen adaptively from earlier counts.  Therefore

\[
\Pr(E)\leq\frac1{24}.
\tag{8}
\]

If the observed perfect count or any observed hole count is zero, do not divide: immediately return \(M_0\).  On \(E^c\), the lower probability bound and relative-accuracy event imply that every one of these counts is positive, so every zero-count path is contained in \(E\).  If every count is positive but some estimate is inaccurate, the algorithm need not detect it; that entire path is also part of \(E\).  It nevertheless continues with positive rationals for only a predetermined number of phases and transitions.

This distinction is important.  On \(E\), rapid mixing is no longer asserted.  The algorithm's cost, however, is still polynomial because it never waits for a diagnostic or for convergence.

#### Obtaining an actual matching of \(G\)

At the terminal activities, original edges have activity \(1\) and nonedges have activity

\[
\varepsilon=\frac1{m!}.
\]

Conditional on being in the perfect class, the stationary law gives a perfect matching \(M\) weight \(\varepsilon^{b(M)}\), where \(b(M)\) is the number of nonedges in \(M\).  Genuine perfect matchings of \(G\) have weight \(1\).  Bogus perfect matchings have weight at most \(1/m!\), and there are at most \(m!\) perfect matchings of \(K_{m,m}\).  Hence

\[
\text{total bogus weight}\leq1,
\qquad
\text{total genuine weight}=\#\operatorname{PM}(G)\geq1.
\tag{9}
\]

Thus a stationary perfect-class sample is genuine with probability at least \(1/2\), and, conditional on being genuine, it is **exactly uniform** on \(\operatorname{PM}(G)\).

On \(E^c\), the final hole activities are within factor \(2\) of ideal.  Therefore the stationary probability of the perfect class is at least \(1/(1+2m^2)\).  Combining this with (9), one stationary endpoint is a genuine perfect matching with probability at least

\[
\alpha=\frac1{6m^2}.
\tag{10}
\]

Run

\[
R=\left\lceil6m^2\log96\right\rceil
\]

fresh terminal chains, each from \(M_0\), and accept the first endpoint that is a perfect matching using only original edges.  If none is accepted, return \(M_0\).  For exact stationary endpoints the no-acceptance probability is at most \(1/96\).  Run each terminal chain close enough to stationarity that all \(R\) endpoints can be coupled to exact stationary endpoints with total failure probability at most \(1/96\).  The first accepted exact endpoint is uniform on \(\operatorname{PM}(G)\); the fallback changes the law by at most \(1/96\), and the coupling changes it by at most another \(1/96\).  Thus for every history in \(E^c\), the final law is within \(1/48<1/24\) of \(U_G\).

For arbitrary histories in \(E\), the returned object is still either an explicitly checked genuine endpoint or \(M_0\).  By convexity of TV distance and (8),

\[
d_{\mathrm{TV}}(Q_G,U_G)
\leq \Pr(E)+\frac1{24}
\leq\frac1{12}.
\tag{11}
\]

The case \(m=1\) is handled directly by returning \(M_0\).

#### Exact rational transitions and fair-bit cost

No real-arithmetic oracle is hidden here.  All edge and hole activities are positive rationals.  For a rational Bernoulli probability \(A/B\in[0,1]\):

* if \(A=0\), return \(0\) deterministically;
* if \(A=B\), return \(1\) deterministically;
* otherwise let \(k=\lceil\log_2 B\rceil\), draw a \(k\)-bit uniform integer \(U\), reject and redraw when \(U\geq B\), and return \([U<A]\).

This coin is exact.  A draw is accepted with probability greater than \(1/2\), so it terminates almost surely and uses fewer than \(2k\) fair bits in expectation.  Uniform choices from \(m\) or \(2m\) possibilities use the same rejection construction.  Metropolis acceptance ratios are computed as exact rational ratios of \(\Gamma\)-weights.

Fraction reduction is unnecessary.  Each edge undergoes \(O(m\log m)\) multiplications by \(3/4\), and \(m!\) has \(O(m\log m)\) bits.  A hole activity starts at \(m\) and in each of \(L\) phases is multiplied by a ratio of two integers in \([1,S]\).  Even storing every fraction unreduced, its numerator and denominator therefore have

\[
O\bigl(m\log m+L\log S\bigr)=\operatorname{poly}(m)
\tag{12}
\]

bits.  This remains true on positive-but-inaccurate paths.  Local Metropolis ratios contain only polynomially many such factors.  Integer arithmetic on these representations has polynomial bit cost.

There are polynomially many phases, endpoint simulations, and predetermined chain transitions.  Each transition uses only a constant number of exact rational or uniform-choice coins of polynomial bit length.  Hence the sampler terminates almost surely and has one fixed polynomial bound \(J(m)\) on both expected fair-bit use and expected bit complexity.  Notice that this conclusion holds on \(E\) as well as on \(E^c\).  This proves Lemma 1.

### A.2 Equal multiplicity makes the decoded divisor uniform

Let

\[
n=\lceil\log_2(N+1)\rceil.
\]

By hypothesis, the uniform builder produces \(G_N\) with \(m\leq n^a\) vertices per side.  Let

\[
W_N=\{(x,y)\in\mathbb Z_{>0}^2:xy=N\}.
\]

There is one element \((x,N/x)\) of \(W_N\) for each positive divisor \(x\mid N\), so \(|W_N|=\tau(N)\).  The decoder is total on every perfect matching and every fiber has the same positive size \(c_N\).  Consequently

\[
\#\operatorname{PM}(G_N)=c_N\tau(N),
\]

and a uniform perfect matching decodes to the uniform law on \(W_N\).  Applying a deterministic map cannot increase TV distance.  Lemma 1 therefore gives a decoded pair whose law \(Q_N\) obeys

\[
d_{\mathrm{TV}}(Q_N,U_{W_N})\leq\frac1{12}.
\tag{13}
\]

The value \(c_N\) need never be known or computed.

If \(N\) is composite, \(\tau(N)\geq3\).  Exactly two ordered witnesses are trivial, namely \((1,N)\) and \((N,1)\).  Hence under the uniform law the probability of a nontrivial factor is

\[
1-\frac2{\tau(N)}\geq\frac13.
\]

By (13), one sampler invocation produces \(1<x<N\) with probability at least

\[
\frac13-\frac1{12}=\frac14.
\tag{14}
\]

This bound is independent of the sizes, balance, or multiplicities of the prime factors.

### A.3 The complete factoring algorithm

Use a deterministic polynomial-time primality test.  The recursive procedure on an integer \(z\geq1\) is:

1. If \(z=1\), return the empty factorization.
2. Remove the full power \(2^e\mid z\), record \(2^e\), and continue with the odd quotient.  If that quotient is \(1\), return.
3. Test the remaining \(z\) for primality.  If it is prime, return \(z\).
4. Build \(G_z\) once.  Repeatedly invoke Lemma 1 with fresh fair bits, decode the returned matching as \((x,y)\), and verify by exact integer arithmetic that \(x,y>0\), \(xy=z\), and \(1<x<z\).  Reject trivial pairs and repeat.  (Under the hypotheses, the product verification never fails; retaining it makes every accepted output visibly Las Vegas.)
5. Recursively factor \(x\) and \(y\), concatenate their prime lists, and merge equal primes into exponents.

Every accepted split is proper, so correctness follows by induction on \(z\).  Several edge cases deserve explicit mention.

* **Primes:** detected before the graph is built; there is no endless search for a nonexistent nontrivial divisor.
* **Prime powers:** for \(z=p^e\), \(e\geq2\), there are \(e+1\) ordered divisor witnesses and \(e-1\) are nontrivial.  The worst case \(p^2\) is exactly the lower bound in (14).  No perfect-power promise or perfect-power oracle is being used.
* **Repeated factors:** the two recursive branches may contain the same prime.  The final merge adds their exponents.
* **Even inputs:** all factors \(2\) are removed deterministically at each node.
* **Unbalanced or otherwise arbitrary composites:** (14) counts divisors, not their bit-length balance.  A divisor close to \(1\) or close to \(z\) is as usable as a balanced one.

### A.4 Almost-sure termination and one fixed expected polynomial

Fix a composite node \(z\).  Let \(C_i\) be the bit cost of its \(i\)-th independent sampler/decoder trial and let \(S_i\) be the event that this trial yields a proper factor.  The cost and success of the **same** trial may be correlated.  Let \(T=\min\{i:S_i\}\).  If \(Q(n)\) is a fixed polynomial bounding the expected cost of one trial for every node of bit length at most \(n\), then

\[
\begin{aligned}
\mathbb E\!\left[\sum_{i=1}^{T}C_i\right]
&=\sum_{i\geq1}\mathbb E[\mathbf1_{\{T\geq i\}}C_i]\\
&\leq\sum_{i\geq1}(3/4)^{i-1}Q(n)\\
&=4Q(n).
\end{aligned}
\tag{15}
\]

The only independence used in the second line is that the current fresh trial's cost \(C_i\) is independent of the failures of trials \(1,\ldots,i-1\).  No independence between \(C_i\) and \(S_i\) is assumed.  The identical calculation bounds expected fair-bit use.  Also

\[
\Pr(T>r)\leq(3/4)^r\longrightarrow0,
\]

so every composite node splits almost surely.

The recursive split tree has prime leaves whose product is \(N\).  Since every prime is at least \(2\), the number of leaves, counted with multiplicity, is at most \(\lfloor\log_2N\rfloor<n\); a full binary tree with that many leaves has fewer than \(2n\) nodes.  Thus the recursion has at most \(2n\) nodes on every execution, irrespective of how unbalanced its splits are.

For an explicit fixed-polynomial envelope, let \(B(n)\), \(D(n)\), and \(A(n)\) be fixed monotone polynomial bounds for the builder, decoder, and primality/arithmetic work, and let \(J(m)\) be the fixed polynomial from Lemma 1, enlarged to bound both expected bit operations and expected fair bits.  One valid common bound is

\[
P(n)=2n\Bigl(A(n)+B(n)+4\bigl(J(n^a)+D(n)+A(n)\bigr)\Bigr)+A(n)n^2.
\tag{16}
\]

The last term harmlessly covers merging and output bookkeeping.  This polynomial is fixed independently of \(N\), its unknown factors, \(c_N\), and all random outcomes.  Conditional expectation applied node by node, (15), and the deterministic \(2n\)-node bound show that both the expected total bit complexity and expected total number of fair random bits are at most \(P(n)\), after enlarging its constant once if necessary.  A finite recursion of almost-surely terminating nodes terminates almost surely.  This proves Statement A.

---

## B. The support boundary for deletion signatures

Let \(H=(V,E)\) be a finite graph with a designated terminal set \(T\subseteq V\), and define

\[
F_H(S)=\#\operatorname{PM}(H-S),\qquad S\subseteq T.
\]

Write

\[
\mathcal F_H=\{S\subseteq T:F_H(S)>0\}
\]

for its support.  Counts and multiplicities will not be needed in the structural argument; positivity is enough.

### B.1 Three matching invariants

**Fixed parity.**  If \(S\in\mathcal F_H\), then \(H-S\) has a perfect matching, and therefore

\[
|V|-|S|\equiv0\pmod2.
\]

Thus every supported \(S\) satisfies

\[
|S|\equiv|V|\pmod2.
\tag{17}
\]

**Bipartite charge.**  If \(H\) is bipartite with sides \(L,R\), a perfect matching of \(H-S\) forces the two remaining sides to have equal size.  Hence every supported \(S\) satisfies

\[
|L|-|S\cap L|=|R|-|S\cap R|,
\]

or equivalently

\[
|S\cap L|-|S\cap R|=|L|-|R|.
\tag{18}
\]

This is a fixed signed terminal charge, stronger than parity when the rail locations are known.

**Matching symmetric exchange.**  Take \(A,B\in\mathcal F_H\), and choose perfect matchings \(M_A\) of \(H-A\) and \(M_B\) of \(H-B\).  In the graph \(M_A\triangle M_B\), vertices outside \(A\triangle B\) have degree \(0\) or \(2\), while every vertex of \(A\triangle B\) has degree \(1\).  Its nontrivial components are therefore alternating cycles and alternating paths whose endpoints lie in \(A\triangle B\).

Fix \(e\in A\triangle B\).  The alternating path starting at \(e\) has another endpoint \(f\in A\triangle B\), with \(f\neq e\).  Toggle the edges of that path in \(M_A\).  Internal vertices remain matched once, while matching status at exactly the endpoints \(e,f\) is reversed.  The result is a perfect matching of

\[
H-(A\triangle\{e,f\}).
\]

Therefore

\[
\forall A,B\in\mathcal F_H\ \forall e\in A\triangle B\ \exists f\in A\triangle B:
A\triangle\{e,f\}\in\mathcal F_H.
\tag{19}
\]

When \(\mathcal F_H\neq\varnothing\), (19) is the symmetric exchange axiom for a delta-matroid, and (17) says all feasible sets have the same parity.  Thus \((T,\mathcal F_H)\) is an **even matching delta-matroid**.  Under the usual definition a delta-matroid must have nonempty feasible family, so no such label is assigned when \(\mathcal F_H=\varnothing\).

### B.2 Exact one-hot dual rail forces a subcube

Suppose \(q\) logical bits have terminal pairs

\[
\{t_i^0,t_i^1\},\qquad i=1,\ldots,q,
\]

and encode \(z\in\{0,1\}^q\) by the one-hot deletion set

\[
B_z=\{t_i^{z_i}:1\leq i\leq q\}.
\tag{20}
\]

Assume the encoding is exact and nonempty: for some nonempty relation \(R\subseteq\{0,1\}^q\),

\[
\mathcal F_H=\{B_z:z\in R\},
\tag{21}
\]

with no off-code supported sets.  Every supported set has size \(q\).  In any nonempty equicardinal delta-matroid, symmetric exchange becomes ordinary basis exchange.  Indeed, for \(A,B\in\mathcal F_H\) and \(e\in A\setminus B\), (19) gives \(f\in A\triangle B\).  Equal cardinality rules out \(f=e\) and rules out a second deletion \(f\in A\setminus B\), so necessarily

\[
f\in B\setminus A,\qquad A-e+f\in\mathcal F_H.
\tag{22}
\]

Thus the supported sets are the bases of a matroid on \(T\).

Now take \(u,v\in R\) and a coordinate \(i\) with \(u_i\neq v_i\).  Apply basis exchange to \(e=t_i^{u_i}\in B_u\setminus B_v\).  Exact one-hot support leaves only one possible exchange partner: \(t_i^{v_i}\).  Choosing a rail from a different coordinate would leave coordinate \(i\) empty and that other coordinate two-hot, contradicting (21).  Hence

\[
u\oplus e_i\in R
\quad\text{whenever }u,v\in R\text{ and }u_i\neq v_i.
\tag{23}
\]

Fix \(u\in R\) and let

\[
I=\{i:\exists v\in R,\ v_i\neq u_i\}.
\]

For any current word \(w\in R\) and any \(i\in I\), compare \(w\) either with \(u\) or with a witness \(v\) from the definition of \(I\); one of them differs from \(w\) in coordinate \(i\).  Equation (23) therefore shows that \(R\) is closed under flipping every coordinate in \(I\).  Coordinates outside \(I\) are fixed.  Consequently

\[
R=\{z\in\{0,1\}^q:z_i=u_i\text{ for every }i\notin I\},
\tag{24}
\]

so \(R\) is a subcube.  If the signature support is empty, (20)--(24) do not apply; the empty relation is the separate degenerate case.

### B.3 Four exact local signatures ruled out

For direct single-rail encoding, let bit \(z_i=1\) mean terminal \(t_i\) is deleted.  The complementary convention has the same parity obstruction.  Equation (17) says that all supported logical words must have the same Hamming-weight parity.  Each relation below contains displayed valid words of opposite parity:

* \(\mathrm{COPY3}=\{000,111\}\): weights \(0\) and \(3\).
* \(\mathrm{AND3}=\{(x,y,z):z=xy\}\): \(000\) and \(010\), of weights \(0\) and \(1\).
* The full-adder relation

  \[
  \mathrm{FA}=\{(a,b,c,s,d):a+b+c=s+2d\}
  \]

  contains \(00000\) and \(11001\), of weights \(0\) and \(3\).
* The fused relation

  \[
  \mathrm{FUS}=\{(a,c,x,y,s,d):a+c+xy=s+2d\}
  \]

  contains \(000000\) and \(001110\), of weights \(0\) and \(3\).

Thus no direct single-rail terminal-deletion signature has exactly any of these four supports.

For exact one-hot dual rail, (24) would require each nonempty relation to be a subcube.  Each fails the single-coordinate closure (23):

* In COPY3, \(000,111\) are valid, but flipping the first coordinate of \(000\) gives invalid \(100\).
* In AND3, \(000,111\) are valid, but flipping the output coordinate of \(000\) gives invalid \(001\).
* In the full-adder relation, \(00000,11001\) are valid, but flipping only \(a\) in \(00000\) gives invalid \(10000\).
* In the fused relation, \(000000,100010\) are valid (the latter has \(a=s=1\)), but flipping only \(a\) in \(000000\) gives invalid \(100000\).

Therefore none has an exact nonempty one-hot dual-rail deletion signature either.  This is a support-level impossibility; allowing different positive multiplicities on the valid codewords cannot repair it.

### B.4 Why Valiant's permanent gadgets do not provide the missing distribution

The requirement in Statement A is fiberwise and positive.  It asks for one unweighted graph and a map on **each individual** perfect matching such that every matching decodes to a valid witness and every witness has the same positive number of preimages.

Classical permanent-hardness constructions establish an equality, or a congruence/interpolation identity, for the **aggregate scalar** permanent.  Their algebraic gadget stages may use negative weights so that unwanted cycle covers cancel after summation; later stages may work modulo primes or recover an integer by interpolation while simulating weights with unweighted graphs.  None of these operations gives the required individual-matching semantics:

* a negative contribution is not a probability, and the two matchings that cancel are still two separate objects under sampling;
* equality modulo a prime controls only a residue, not a nonnegative fiber cardinality;
* interpolation combines totals from several instances, not samples from one graph; and
* an unweighted gadget that preserves only the final total need not provide a decoder, eliminate invalid matchings, or balance witness fibers.

Thus JSV sampling cannot be applied to those cancellations or congruences to obtain a positive readable witness distribution.  This does **not** prove that every possible positive construction is impossible; it states exactly why the classical hardness gadgets do not themselves satisfy Statement A's premise.

### B.5 Exact scope of the obstruction

The delta-matroid argument must not be extended beyond its hypotheses.  The following possibilities remain open here:

* **Off-code supported states:** exchange paths may pass through supported deletion patterns that are not logical codewords, so (21) fails and logical single-bit closure need not follow.
* **Closed internal-edge decoding:** a logical value may be read from which internal edges occur in a completed matching rather than solely from the terminal-deletion set.
* **Block codes:** a logical coordinate may use a larger terminal block or a non-one-hot code; basis exchange need not translate to a one-bit flip.
* **Global graphs:** constraints may be realized only by one global matching construction, with no exact local terminal signature to which the obstruction applies.
* **Global multiplicity balancing:** equal positive fibers may be achieved, if at all, by global replication or coupling even when no local gadget has the desired signature.

Accordingly, Statement B rules out the four named *direct* local encodings exactly as claimed, while preserving these other design spaces as open.  It neither constructs the builder assumed in Statement A nor proves that no such builder can exist.
