# Closed Routes

Record every closed route with what was tried, the exact obstruction, the evidence, and the condition that would make a retry materially new. A theorem-strength missing lemma is a blocked route, not near-completion.

## X01 — generic exact linear compression of arbitrary square classes

**Status:** promoted for the exact linear-rank obstruction and the resulting narrow method failure. The separate \(\mathbb F_7\) one-moment certificate remains candidate because its blind reconstruction has not run.

**Family:** F01.

**Classification:** method failure for the generic compression mechanism; this does not close special structured generators.

**What was tried.** Encode arbitrary positive-integer square classes \(v_i=[a_i]\in\mathbb Q^\times/(\mathbb Q^\times)^2\) by vectors \(e_i\in\mathbb F_2^d\), requiring every dependence in the sketch to be a sound square-product relation.

**Exact obstruction.** Let \(E,V\) be the linear maps from coefficient vectors in \(\mathbb F_2^m\) to the sketch space and the true square-class space. Soundness is \(\ker E\subseteq\ker V\), hence rank-nullity gives \(\operatorname{rank}E\ge\operatorname{rank}V\). For \(m\) distinct rational primes, \(\operatorname{rank}V=m\), so \(d\ge m\) and the sketch forces no nonzero dependence. A generic lower-dimensional exact linear sketch therefore cannot manufacture square relations.

A warning against a one-moment nonlinear slogan occurs in \(\mathbb F_7\): multisets \(\{1,2\}\) and \(\{4,6\}\) have the same first power sum \(3\), but products \(2\) and \(3\), respectively, have opposite quadratic character. (The entries are all distinct; no claim of minimal field size is made.)

**Evidence.** The rank-nullity argument survived a focused hostile audit and a proof-blind end-to-end reconstruction; it is P01 in `PROVED.md`. The explicit \(\mathbb F_7\) calculation passed hostile audit but has not independently been reconstructed.

**What would make a retry materially new.** An efficiently generatable special sample family whose true integer square-class span is proved polynomially bounded for structural reasons, together with a way to compute a nontrivial second modular square root that does not already perform factoring; or a nonlinear reconstruction theorem using enough explicitly bounded moments and surviving adversarial collisions.

## X02 — a fixed synchronized duplication-Lattès instance

**Status:** promoted as the exact fixed-instance obstruction P03. No broader family-level closure is claimed.

**Family:** F02.

**Classification:** evidence against the auxiliary principle that succinctness plus an addition law automatically gives local separation. It is only a fixed-instance obstruction for affine curve-point seeds, not a method failure for the duplication-Lattès family.

**What was tried.** Use the \(x\)-coordinate Lattès map induced by doubling on an elliptic curve, hoping that a succinct orbit-collision discriminant vanishes modulo one unknown prime before the other.

**Exact obstruction and certificate.** Set \(N=15\) and

\[
E:y^2=x^3+2x+1,
\qquad
F(X)=\frac{X^4-4X^2-8X+4}{4(X^3+2X+1)}.
\]

Direct enumeration gives \(\#E(\mathbb F_3)=\#E(\mathbb F_5)=7\). Hence every affine local point is a nonidentity point of order 7. Modulo sign, \(1,2,4\) are distinct in \(\mathbb Z/7\mathbb Z\), while \(2^3=1\), so \(x(P),x(2P),x(4P)\) are distinct and \(x(8P)=x(P)\) in both local components. No local point has \(y=0\), so every duplication denominator \(4y^2\) is a unit. CRT therefore gives, for every affine \(P\in E(\mathbb Z/15\mathbb Z)\),

\[
\gcd(D_m(P),15)=1\quad(m\le3),\qquad
\gcd(D_m(P),15)=15\quad(m\ge4).
\]

Thus even a maximally succinct large-\(m\) collision product has zero separator probability for every distribution supported on the 36 affine points of this fixed CRT curve. Here iterates and differences are defined using stepwise inversion of unit denominators; the orbit repeats with period 3 in \(x\), so \(D_m\) is literally zero for \(m\ge4\). Clearing accumulated denominators changes the product only by a unit.

**Hostile-audit scope correction.** This fixed map can separate CRT components on residue seeds that are not curve points: \(x=2\) has orbit \(2\to9\to7\pmod {15}\), and \(D_3=70\) has gcd 5 with 15. The witness therefore cannot justify a family-level closure. Also, 15 is called smallest only within products of two distinct odd primes; no global minimality over all composite inputs or curves is claimed.

**What would make a retry materially new.** A distributional theorem over randomized curves/seeds proving inverse-polynomial local-threshold separation, together with a genuinely polylogarithmic product circuit; or a synchronized-family obstruction covering that distribution rather than one curve.

## X03 — naive global-\(N\) DDF substitution and uniform linear probes

**Status:** promoted as the exact narrow failures/certificates P06–P08. F03 remains open.

**Family:** F03.

**Classification:** method failure for substituting the global exponent \(N\) into local DDF powers, and evidence against uniform random linear probes. This does not close Berlekamp, resolvent, or Galois-certificate families.

**What was tried.** Generate a low-degree polynomial whose Frobenius cycle types differ modulo two unknown prime factors, then turn that difference into unequal polynomial-gcd degrees over \(\mathbb Z/N\mathbb Z\).

**Exact obstruction.** For \(N=15\) and \(f=X^2+1\), the reduction is irreducible modulo 3 and split modulo 5, and \(\operatorname{Res}(f,f')=4\) is a unit. Nevertheless, using the available exponent \(N\) in the usual DDF powers gives

\[
X^{15^i}-X\equiv -2X\pmod f\quad(i\text{ odd}),
\qquad
X^{15^i}-X\equiv0\pmod f\quad(i\text{ even}),
\]

in both CRT components, so every local gcd-degree profile matches and no zero divisor appears. The correct local tests require \(X^{3^i}-X\) and \(X^{5^i}-X\). At \(i=1\), their CRT-combined difference is \(10X\), whose coefficient has gcd 5 with 15. Thus the currently specified componentwise construction is circular: once that coefficientwise object is constructed, it performs the split. This is not a proof that no alternative global construction exists.

A smaller even witness is \(N=10\), \(f=X^2+9X+5\). It is irreducible modulo 2 and split modulo 5, has unit resultant, yet \(X^{10^i}-X\equiv0\pmod f\) in both components for every \(i\ge1\). Therefore 15 is minimal only after restricting to products of two distinct odd primes; degree 2 is minimal for a squarefree cycle mismatch.

**Cycle-sign limitation.** For a random squarefree quadratic over \(N=pq\) with distinct odd primes, local split/irreducible types disagree with probability \(1/2\), and the immediately available aggregate is a unit discriminant of Jacobi symbol \(-1\). The promise of such a unit is Las Vegas randomized-polynomial-time equivalent to factoring this restricted semiprime class: rejection sampling takes exactly two unit samples in expectation and at most \(15/4\) raw samples, while factoring solves the promise. This is not an information-theoretic assertion that every richer coefficient expression is a unit.

For a split quadratic modulo \(p\), an irreducible quadratic modulo \(q\), and uniform \(B=aX+b\), the exact probability of unequal local gcd degrees is

\[
\frac{2p-1}{p^2}+\frac{p-2}{pq^2}<\frac2p+\frac1{q^2}.
\]

This is exponentially small in the bit length for balanced factors. Conditional on unit \(a\) and monic normalization, the probability is exactly \(2/p\).

**What would make a retry materially new.** A polynomial-size invariant computable with the global input \(N\), not merely the substitution \(r=N\) or unknown component exponents, whose local ranks provably differ with inverse-polynomial probability and whose differing rank is division-free extractable; or a certificate using more than the product/Jacobi image of local cycle types.

## X04 — blind characteristic substitution in a Hasse–Witt formula

**Status:** promoted as P09. Only the exact blind-substitution method is closed.

**Family:** F05.

**Classification:** method failure for the blind substitution of \(N\) for the local characteristic in the genus-1 Hasse–Witt coefficient; genuinely global geometric invariants remain open.

**Exact certificate.** Let \(N=15\) and \(E:y^2=f(x)=x^3+x+1\). Its Weierstrass discriminant is \(-496\), a unit modulo 15. For an odd prime \(r\), the genus-1 Hasse–Witt entry (up to rank-preserving convention changes) is

\[
H_r=[x^{r-1}]f(x)^{(r-1)/2}.
\]

The true entries are \(H_3=[x^2]f=0\) and \(H_5=[x^4]f^2=2\), so their ranks differ. The blind substitution gives

\[
H_{15}^{\rm blind}=[x^{14}]f^7
=\frac{7!}{4!2!1!}=105\equiv0\pmod {15},
\]

so both reductions have blind rank zero. The CRT combination of the true entries is \(12\pmod {15}\), whose gcd with 15 is 3. Only the recipe “first determine \(p,q\), compute local entries, then CRT-combine” is circular. A direct uniform computation of 12 from the composite-ring curve would be a valid factoring mechanism, not a circular algorithm.

**What would make a retry materially new.** A geometric operator defined directly and uniformly over \(\mathbb Z/N\mathbb Z\), not by the refuted blind surrogate or by first selecting each CRT characteristic, together with an inverse-polynomial rank-separation probability and polynomial bit-cost construction.

## X05 — coefficient localization in the standard minimal-\(r\) AKS stage

**Status:** promoted as P11 after a focused hostile audit and proof-blind end-to-end reconstruction.

**Family:** F04.

**Classification:** method failure for the exact standard scan over the AKS-selected minimal \(r\), standard shift bound, whole-polynomial local pass/fail, and individual coefficient gcds. It does not close nonstandard \(r\) or richer rank/minor certificates.

**Exact claim refuted.** The claim that every non-prime-power composite surviving the AKS preliminary gcd stage has, within the standard polynomial-identity stage, either an identity that holds in some but not all prime components or an error coefficient divisible by some but not all components.

**Certificate.** Let

\[
N=20{,}000{,}000{,}499{,}999{,}937
=100{,}000{,}007\cdot199{,}999{,}991.
\]

The standard smallest \(r\) with \(\operatorname{ord}_r(N)>(\log_2N)^2\) is \(r=2953\), with order 2952 and \((\log_2N)^2\approx2932.3145\). Both prime factors exceed \(r\). The standard shift bound is

\[
A=\left\lfloor\sqrt{\varphi(r)}\log_2N\right\rfloor=2942.
\]

For every \(1\le a\le A\), reduce

\[
H_a=(X+a)^N-X^N-a\pmod {X^r-1}.
\]

An exhaustive exact finite-field scan of all \(A r=8{,}687{,}726\) coefficient positions found no zero coefficient modulo either factor. Thus both local errors are nonzero for every shift, and every global coefficient is a unit modulo \(N\).

The scanner uses the exact identity, for \(N=pq\),

\[
H_a\bmod p=h_{q,a}(X^p),
\qquad h_{q,a}(Y)=(Y+a)^q-Y^q-a,
\]

and its swapped analogue modulo \(q\). Because \(\gcd(pq,r)=1\), the substitutions permute coefficient positions modulo \(X^r-1\).

**Evidence and provenance.** Named source, timeout command, exhaustive output, and the manifest of every exploratory run are recorded in the F04 computation ledger. A fresh hostile auditor independently proved the parameters and factors, rescanned both full local families, and directly checked the Frobenius reduction at sample shifts. Its first run failed only during JSON serialization after the scans; a fully repeated second run passed. A proof-blind agent then reconstructed the parameters and algebra from the numerical statement and performed a fresh authoritative scan of all \(17{,}375{,}452\) local coefficients, again finding zero zeros. Its run manifest disqualifies three noncompliant diagnostic invocations; no claim relies on them, and the matching named source was rerun under timeout before promotion. The result is P11 in `PROVED.md`.

**What would make a retry materially new.** A proved reason to scan additional polynomially many nonstandard moduli \(r\), or a different invariant of the AKS error family such as a local rank/minor whose mismatch is not reducible to a coefficient zero and has a uniform polynomial extraction bound.

## X06 — scalar-carry quotient for binary multiplication

**Status:** promoted as P10. The corrected deterministic obstruction and its precisely scoped counting claim passed both verification stages.

**Family:** F06.

**Classification:** evidence that scalar carry is not a sufficient equivalence relation, and method failure for the largest-\(x\)-prefix representative rule under the canonical \(a\le b\) search. No broader lower bound against other selection rules or richer state summaries is claimed.

**Proposed mechanism.** For factor bits \(x_i,y_j\), process

\[
s_k=\sum_{i+j=k}x_i y_j,
\qquad
c_{k+1}=\frac{c_k+s_k-N_k}{2}
\]

column by column, accepting only integral nonnegative carries and eventually clearing the terminal carry, while keeping one partial assignment per scalar carry. For \(a\le b\), induction gives \(0\le c_k\le a-1\). This would be a polynomial-state dynamic program if future completability depended only on the carry.

**Exact obstruction.** For \(N=55=(110111)_2\) and factor lengths \((a,b)=(3,4)\), after columns 0 and 1 the partial assignments

\[
P:(x_0,x_1)=(1,0),\ (y_0,y_1)=(1,1),
\]

and

\[
Q:(x_0,x_1)=(1,1),\ (y_0,y_1)=(1,0)
\]

both have \(c_1=c_2=0\). Yet \(P\) completes to \(x=5,y=11\), whereas \(Q\) forces \(x=7\) and has no valid 4-bit continuation. A largest-\(x\)-prefix rule keeps \(Q\) and deletes the only factor path in the canonical \(a\le b\) search. If the redundant ordered pair \((4,3)\) is also searched, a swapped path survives; a smallest-prefix rule also survives. Thus the witness refutes scalar-carry sufficiency and this representative rule, not every rule.

Under the convention that equal-length swapped factorizations are both accepted, the smallest-first-column argument is: opposite second bits are necessary; \(a=2\) forces the second bit to be the leading bit; equal lengths preserve both swapped orientations; hence \(a\ge3,b\ge4\). The smallest live residues are 5 and 11, giving 55, while the opposite orientation begins at \(7\cdot9=63\). If a separate numerical constraint \(x\le y\) rejects the swapped equal-length path, 35 is already a counterexample.

**State-size and randomized scope.** After processing the low \(a\) columns with \(a<b\), every odd \(a\)-bit candidate \(x\) determines a unique compatible low prefix \(y=Nx^{-1}\pmod {2^a}\), yielding exactly \(2^{a-2}\) raw histories. Some fail to extend through the \(b\)-th column, so this is an explicit-enumeration count, not a state-complexity lower bound. A restart that samples one history uniformly from this entire depth-\(a\) set succeeds with exact probability \(2^{-(a-2)}\) on a semiprime with one \(a\)-bit factor; Bertrand gives families with \(a=\Theta(n)\). This is not the probability of choosing one representative per carry: that probability depends on the true history's carry-class size. At \(N=187=11\cdot17\), global uniform sampling succeeds with probability \(1/4\), while uniform selection in the true carry class succeeds with probability \(1/2\).

**Evidence.** A focused hostile audit corrected the scope of the restart probability and the minimality claim. A fresh proof-blind reconstruction then recovered the recurrence, carry bound, \(N=55\) live/dead collision, first-column minimality qualifications, the bijection giving exactly \(2^{a-2}\) raw histories, the global-uniform probability, the Bertrand family, and the \(N=187\) carry-class contrast. The promoted statement is P10 in `PROVED.md`.

**What would make a retry materially new.** A proved polynomial-size state invariant that retains the prefix-convolution information required by all future columns, or a universally correct polynomial-time representative rule. Raw-history enumeration, hardwired live-path selection, or an unsupported representative heuristic is insufficient.

## X07 — standard trace/point probes for Shor's multiplication spectrum

**Status:** candidate after focused hostile audit with substantive scope corrections; proof-blind reconstruction pending.

**Family:** F07.

**Classification:** method failure for the claim that the regular-representation trace or basis-point spectral measures have polynomially many effective frequencies on all factoring inputs. It is not a lower bound against adaptive exponentially indexed queries or different arithmetic probes.

**Exact spectral lemma.** For the permutation \(U_a:x\mapsto ax\pmod N\), with \(\gcd(a,N)=1\) and \(r_d=\operatorname{ord}_d(a)\),

\[
\chi_{U_a}(X)=\prod_{d\mid N}(X^{r_d}-1)^{\varphi(d)/r_d}.
\]

The residues of additive order \(d\) form \(\varphi(d)\) points in cycles of length \(r_d\). The unit stratum \(d=N\) therefore forces the spectral support to be exactly all \(r_N\)-th roots, of cardinality \(r_N\). Moreover,

\[
\operatorname{tr}(U_a^k)=\gcd(a^k-1,N).
\]

A trace strictly between 1 and \(N\) is already a factor. A point probe at \(x\) has a uniform complex spectral measure on the \(r_{N/\gcd(x,N)}\)-th roots. A nonzero nonunit point already exposes a proper gcd; \(x=0\) instead gives the trivial gcd \(N\) and constant moments, while a unit point retains all \(r_N\) frequencies. A normalized whole-orbit indicator has only eigenvalue 1 and discards the order; its unnormalized zeroth moment equals the orbit length. Only an explicit coefficient-list construction has a proved output-size lower bound—no generic obstruction to a succinct orbit representation follows.

**Exponential synchronized family.** Choose an \(m\)-bit prime \(\ell\). Effective Linnik bounds first give a prime \(p\equiv1\pmod\ell\), then a larger prime \(q\equiv1\pmod {p\ell}\), with \(p,q\le\ell^{O(1)}\). Choose local elements of exact order \(\ell\) and CRT-combine them to \(a\pmod {N=pq}\). Then every nonzero residue lies in an \(\ell\)-cycle,

\[
\chi_{U_a}(X)=(X-1)(X^\ell-1)^{(N-1)/\ell},
\qquad
\operatorname{tr}(U_a^k)=
\begin{cases}1,&\ell\nmid k,\\N,&\ell\mid k.\end{cases}
\]

The input length is \(n=\Theta(m)\), so \(\ell=2^{\Theta(n)}\). A uniform deterministic enumerator for the least primes takes only the Linnik-guaranteed \(\ell^{O(1)}=2^{O(m)}\) time; polynomial-time generation in \(m\) is not claimed. Every nonzero point sequence has reduced generating function \(1/(1-z^\ell)\) over every coefficient field. The exact integer trace sequence has, over characteristic zero,

\[
\frac1{1-z}+\frac{N-1}{1-z^\ell}
=\frac{N+z+\cdots+z^{\ell-1}}{1-z^\ell},
\]

with no cancellation and denominator degree \(\ell\). This trace claim is false uniformly over finite fields: modulo 2 the odd values 1 and \(N\) coincide, leaving denominator \(1-z\).

**Hostile-audit scope correction.** Denominator degree \(\ell\) obstructs consecutive-moment dense Padé/Prony reconstruction and explicit enumeration of all frequencies. It is not a lower bound for adaptively selected binary-encoded indices, sparse descriptions such as \(1-z^\ell\), finite-field trace reconstruction, arbitrary arithmetic/superposition probes, or algorithms exploiting \(N,a\) by another method. The family supplies bad fixed pairs \((N,a)\), not a density theorem for random \(a\), so it does not obstruct a factoring algorithm that resamples the base.

**What would make a retry materially new.** A probe family computable without factoring whose spectral measure is proved polynomially supported for every input and still determines enough local order information; a density theorem justifying resampling; or a non-Prony reconstruction exploiting sparse/arithmetic structure with a complete adaptive-query and bit-cost proof.
