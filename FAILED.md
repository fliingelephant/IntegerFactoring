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

**Status:** promoted as P12 after a focused hostile audit with substantive scope corrections and a proof-blind reconstruction of the corrected theorem.

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

**Evidence.** A focused hostile audit found and corrected the zero-point, orbit-indicator, family-effectivity, coefficient-field, query-model, and random-base overclaims. A fresh proof-blind reconstruction then recovered the orbit stratification, trace and point formulas, quantified Linnik family, characteristic-zero and finite-field generating-function behavior, effectivity bound, and exact scope. The promoted statement is P12 in `PROVED.md`.

**What would make a retry materially new.** A probe family computable without factoring whose spectral measure is proved polynomially supported for every input and still determines enough local order information; a density theorem justifying resampling; or a non-Prony reconstruction exploiting sparse/arithmetic structure with a complete adaptive-query and bit-cost proof.

## X08 — natural fixed-degree automorphism-count magnitude interpolation

**Status:** promoted as P13 after the mandatory kill test, focused hostile audit, and proof-blind reconstruction of the corrected theorem.

**Family:** F08.

**Classification:** method failure for treating interpolation as the hard step in the canonical dual-number, square-zero, quadratic-monogenic, or fixed-degree étale families. Informative counts in the tested non-étale families are already factoring-equivalent; this is a theorem-strength blockage, not an impossibility theorem for all B12 constructions.

**Dual-number obstruction.** Let \(A=\mathbb Z/N\mathbb Z\) and \(R=A[\varepsilon]/(\varepsilon^2)\). An \(A\)-algebra automorphism has

\[
\varepsilon\longmapsto a+b\varepsilon,
\qquad b\in A^\times,\quad 2a=0,\quad a^2=0.
\]

The number of admissible \(a\) is 2 if \(4\mid N\) and 1 otherwise, so

\[
|\operatorname{Aut}_A R|=\delta(N)\varphi(N),
\qquad
\delta(N)=\begin{cases}2,&4\mid N,\\1,&4\nmid N.\end{cases}
\]

The known factor \(\delta(N)\) makes exact counting a \(\varphi(N)\) oracle. On \(N=pq\), it gives \(p+q=N+1-\varphi(N)\) and hence the factors. Augmentation-preserving automorphisms remove the translation and have count exactly \(\varphi(N)\).

**A richer rank-3 count.** For squarefree \(N=pq\), let \(S=A\oplus A^2\) with \((A^2)^2=0\). Its nilradical is \(A^2\), hence

\[
\operatorname{Aut}_A(S)=GL_2(A),
\quad
C=|GL_2(\mathbb F_p)|\,|GL_2(\mathbb F_q)|.
\]

Writing \(s=p+q\) and \(u=\varphi(N)=N+1-s\), direct multiplication gives

\[
C=N(N+1-s)^2(N+1+s)
=Nu^2\bigl(2(N+1)-u\bigr).
\]

The full cubic \(g(u)=u^2(2(N+1)-u)\) is strictly increasing for \(0<u<N+1\), since \(g'(u)=u(4(N+1)-3u)>0\). Thus binary search recovers \(u\) in polynomial bit complexity. (The linear factor \(2(N+1)-u\) itself decreases.) This count is again exactly factoring-equivalent despite not literally equaling \(\varphi(N)\).

**Quadratic and étale classifications.** For odd \(N=pq\) and

\[
B=A[X]/(X^2-uX+v),\qquad\Delta=u^2-4v,
\]

the local automorphism count over \(\mathbb F_\ell\) is 2 when \(\ell\nmid\Delta\) and \(\ell-1\) when \(\ell\mid\Delta\). Thus the global count is respectively 4, \(2(p-1)\), \(2(q-1)\), or \(\varphi(N)\), according as \(\gcd(\Delta,N)\) is \(1,p,q,N\). These numerical values can collide, so the count alone need not identify the case. The mixed cases were already factored by the known gcd; the deliberately everywhere-degenerate case hides \(\varphi(N)\); the étale case is constant.

More generally, a rank-\(d\) finite étale \(\mathbb F_p\)-algebra

\[
E\simeq\prod_e\mathbb F_{p^e}^{m_e},
\qquad\sum_e e m_e=d,
\]

has

\[
|\operatorname{Aut}_{\mathbb F_p}E|=\prod_e e^{m_e}m_e!,
\]

which for fixed \(d\) depends only on the decomposition partition and is at most \(d!\), independently of \(p\). Over a squarefree semiprime base the global count is at most \((d!)^2\). A parameterized sequence of factorization-type patterns could still support a different Frobenius separator; only growing field-size magnitude interpolation is absent.

**Counting versus finding.** At \(N=15\), \(\varepsilon\mapsto-\varepsilon\) is an easy nonidentity automorphism but \(\gcd(-2,15)=1\); the CRT-selective map \(\varepsilon\mapsto4\varepsilon\) gives \(\gcd(3,15)=3\). Finding some automorphism is therefore too weak, while finding a component-selective one is already a factor witness. All displayed fixed-degree counts have only \(O(\log N)\) output bits, so output size is not the gap.

**Evidence.** A focused hostile audit verified the arbitrary-\(N\) dual-number count, corrected the rank-3 monotonicity wording, noted collisions among quadratic case counts, proved the étale \(d!\) bound, and enforced the theorem-strength-blockage scope. A fresh proof-blind reconstruction independently recovered all formulas, semiprime reductions, bit-cost bounds, and limitations. The promoted theorem is P13 in `PROVED.md`.

**What would make a retry materially new.** An explicit fixed-degree family whose informative local counts admit a proved uniform factor-free \(\operatorname{poly}(\log N)\) counting algorithm, or a structural invariant computable without counting an already factoring-equivalent group. Merely postulating the count oracle, changing the interpolation basis, or producing an easy globally synchronized automorphism is not new.

## X09 — annihilator rank in the standard minimal-\(r\) AKS error family

**Status:** promoted as P14 after the mandatory kill test, focused hostile audit, and proof-blind reconstruction of the corrected theorem.

**Family:** F04.

**Classification:** evidence against the universal auxiliary claim that the standard AKS error must have unequal local annihilator ranks. It closes neither nonstandard moduli nor other group-algebra elements.

**Exact witness.** Let

\[
N=79{,}403=271\cdot293,
\qquad r=269.
\]

Exact integer inequalities give \(264<(\log_2N)^2<265\). Orders below \(r\) are excluded by totient bounds, while \(N\equiv48\pmod {269}\), \(48^{134}=-1\), and \(48^4=239\pmod {269}\), so \(r\) is the first AKS modulus and \(\operatorname{ord}_{269}(N)=268\). Moreover

\[
266<\sqrt{268}\log_2N<267,
\]

so the standard shift bound is 266; both factors exceed \(r\).

For \(h_{m,a}(Y)=(Y+a)^m-Y^m-a\), the two local multiplication nullities are

\[
\nu_{271}(a)=\deg\gcd(h_{293,a},Y^{269}-1),
\qquad
\nu_{293}(a)=\deg\gcd(h_{271,a},Y^{269}-1).
\]

The nontrivial irreducible factors of \(Y^{269}-1\) have degrees 268 over \(\mathbb F_{271}\) and 67 over \(\mathbb F_{293}\), because \(\operatorname{ord}_{269}(271)=268\) and \(\operatorname{ord}_{269}(293)=67\). For any nontrivial 269th root \(\zeta\), local vanishing implies

\[
G_a(\zeta)=0,
\qquad
G_a(Y)=(Y^2+a)(Y+a)^{22}-Y^{24}-a.
\]

For \(a\ne0\), the leading \(Y^{24}\) terms cancel and the \(Y^{23}\) coefficient is \(22a\), so \(G_a\) has degree 23 and cannot contain any nontrivial cyclotomic factor. At \(Y=1\), the local equations have only \(a=-1,0,-2\). Hence both local nullities are zero for every standard shift \(1\le a\le266\), and also for \(a=267\). Multiplication by every standard \(H_a\) is invertible in both local quotient algebras, so the local nullity/gcd-degree invariant supplies no separator. Equal full ranks alone do not show that every intermediate minor, principal subresultant coefficient, or elimination transcript is nonseparating.

**Evidence.** Named Sage runs R01–R07 and their dispositions are in `experiments/F04_rankkill/RUN_MANIFEST.md`. That discovery manifest did not retain exact command/environment strings despite previously implying it did, and R04 used binary64 thresholds for its “first in the box” ordering; neither is authoritative evidence for provenance or minimality. R05 directly checked the small witness and R07 matched the analytic distributions. A fresh hostile auditor independently proved the exact parameters and algebra and reran all local residues under the fully specified timeout-bounded A02 in `experiments/F04_rank_audit`. A proof-blind reconstruction then independently recovered the exact logarithmic bounds, minimal \(r\), shift bound, nullity identity, local factor degrees, degree-23 obstruction, and exceptional shifts without reading either experiment directory. The displayed algebra, not a finite-search minimality claim, is P14 in `PROVED.md`.

**PSC follow-up (promoted P16).** The mandatory canonical-PSC kill test did not extend this obstruction. With a fixed determinant convention applied to the same globally formed \(H_a\), P16 finds \(D_{47}=0\pmod{271}\) and \(173\pmod{293}\) already at \(a=1\). A hostile factor-free scan independently discovered the same first index and gcd, and a literal-reduction audit checked every local determinant. Proof-blind reconstruction recovered the certificate and found that the constant coefficient already separates: \([X^0]H_1=36585\) and \(\gcd(36585,79403)=271\). Thus this supplies no PSC advantage; it only confirms that equal full ranks do not control intermediate determinants. The reconstruction's provenance-defective early probe is disclosed and disqualified; authoritative runs R01--R03 support P16.

**What would make a retry materially new.** A proved choice of polynomially many nonstandard \(r\), a different group-algebra element or joint invariant, or an asymptotic shift distribution with inverse-polynomial mismatch probability that is not contradicted by this standard-parameter witness.

## X10 — factor-symmetric scalar higher-residue phase carriers

**Status:** promoted as P15 after a focused hostile audit and proof-blind end-to-end reconstruction.

**Family:** F09.

**Classification:** method failure for the precisely defined scalar, multiplicative carrier whose **individual scalar labels** are factor-swap invariant, with fixed public unit twists, integer powers, multiplicative/divisive combining, transcript-internal adaptivity, and label-only postselection. This does not close vector/multiset transcripts that are merely swap-equivariant, vector/ring-valued or factor-oriented labels, additive/nonmultiplicative queries, externally informed twists, or general higher-residue mechanisms.

**Diagonal quotient theorem.** Let \(\ell\) be an odd prime and \(N=pq\) with \(p,q\equiv1\pmod\ell\). Fix local order-\(\ell\) characters and write a unit's hidden exponent vector as

\[
u(a)=(u_p(a),u_q(a))\in\mathbb F_\ell^2.
\]

A multiplicative scalar character has exponent \(L(x,y)=\alpha x+\beta y\). Requiring that this individual scalar value be invariant under swapping the two unlabeled factors forces \(\alpha=\beta\), so every such carrier is a multiple of

\[
\Sigma(x,y)=x+y.
\]

A family of such labels has joint rank at most one. If at least one label is nontrivial, its common kernel is exactly \(\{(t,-t):t\in\mathbb F_\ell\}\); if all are trivial, the rank is zero. A fixed public unit twist \(a\mapsto t_j a^{k_j}\) only adds a constant and rescales \(\Sigma(u(a))\). Inductively, multiplication/division, choices based only on public randomness and earlier admissible labels, and postselection solely on those labels remain in this quotient. Thus an exposed zero phase does not certify either local phase is zero. Mere swap-equivariance of a vector or multiset transcript is insufficient: the unordered pair of coordinate characters is swap-equivariant and retains rank two.

**Exact cubic certificate.** For \(\ell=3\), \(N=91=7\cdot13\), choose primitive roots 3 modulo 7 and 2 modulo 13 and reduce their discrete-log exponents modulo 3. Then

\[
u(15)=(0,1),\qquad u(18)=(1,0),
\]

so both scalar sums equal 1, yet

\[
15/18=16\pmod {91},\qquad u(16)=(2,1).
\]

The combined scalar phase is zero while neither local phase is zero. All nine local pairs occur and each diagonal fiber contains 24 units.

**Cyclotomic orientation.** In \(K=\mathbb Q(\zeta_\ell)\), for odd \(\ell\), the product of the local \(\ell\)-th power-residue symbols over every prime ideal above a rational split prime \(p\) is trivial on rational numerators \(a\) with \(p\nmid a\): the Galois exponents sum to

\[
1+\cdots+(\ell-1)\equiv0\pmod\ell.
\]

A conventional nontrivial one-valued ideal-symbol evaluation therefore must supply or compute a choice of prime above each rational factor rather than take the fully symmetric product; this selection may be implicit. For \(\ell=3,N=91\), a root \(\rho\) of \(\Phi_3\) modulo \(N\) supplies such orientation data through the norm-\(N\) ideal \((N,\zeta-\rho)\). The four roots have CRT pairs

\[
(2,9),(2,3),(4,9),(4,3).
\]

Globally conjugate orientations have unit differences, while roots agreeing in exactly one component have difference gcd 7 or 13 with \(N\). Two roots from different global-conjugacy orbits can therefore factor this input. Existence of the ideal proves neither that an orientation is hard or noncanonical to compute from \(N\), nor that one orientation is factoring-equivalent.

**Evidence.** The exact enumeration and all failed-run dispositions are recorded in `experiments/F09_phasekill/RUN_MANIFEST.md`; R04 verifies all phase fibers and root-difference gcds. The hostile audit in `experiments/F09_phase_audit/RESULT.md` independently reproved the corrected theorem and reran the exact certificate: A01's mathematical assertions passed but its JSON serialization failed and is retained, while timeout-bounded A02 passed. A proof-blind reconstruction in `experiments/F09_phase_reconstruct/RESULT.md` independently recovered the theorem, adaptive closure, cyclotomic norm proof, orientation scope, and exact certificate; it additionally exhibited the rank-two ordered-vector and anti-diagonal-sensitive multiset boundaries. Finite computation certifies only the displayed examples. The corrected unbounded statements are P15 in `PROVED.md`.

**What would make a retry materially new.** A factor-free polynomial-time construction of a vector/ring-valued or consistently oriented carrier with more than diagonal rank, or a nonmultiplicative/additive probe with a proved combining law and inverse-polynomial separation probability. Merely adding scalar symmetric twists or postselection on their labels is not new.

## X11 — order-filtered automorphisms of squarefree cubic algebras

**Status:** promoted as P17 after hostile audit and proof-blind reconstruction.

**Family:** F10.

**Classification:** method failure for the natural cubic construction that asks for a globally nonidentity automorphism of order 2 or 3 when that order occurs in exactly one local automorphism group. This does not close other fixed-degree rings, richer local certificates, or canonization mechanisms.

**Exact local structure.** If \(f\) is a monic squarefree cubic over \(\mathbb F_\ell\), Frobenius has type \((111),(12)\), or \((3)\) on the three geometric roots, and

\[
\operatorname{Aut}_{\mathbb F_\ell}(\mathbb F_\ell[X]/(f))
=C_{S_3}(\operatorname{Frob})
=S_3,\ C_2,\ C_3
\]

respectively. The exact type counts are \(\binom{\ell}{3}\), \(\ell(\ell^2-\ell)/2\), and \((\ell^3-\ell)/3\), giving conditional probabilities \((\ell-2)/(6\ell),1/2,(\ell+1)/(3\ell)\). Thus order-3 existence differs across two independently sampled squarefree local cubics with probability \(1/2\). For odd characteristic, type \((12)\) is exactly the nonsquare-discriminant type, so the mismatch is the unit Jacobi-minus-one condition. A raw monic cubic reaches it with probability \((p-1)(q-1)/(2pq)\).

**Why construction is the factoring step.** On the order-3 mismatch promise, one local group is \(C_2\), whose only solution to \(\sigma^3=1\) is identity; the other local group has a nonidentity order-3 element. Therefore any globally nonidentity solution is identity in exactly one component. If \(\sigma(X)=a+bX+cX^2\), at least one of \(a,b-1,c\) is zero in exactly one component and its gcd with \(N\) splits the semiprime. Given the factors, fixed-degree finite-field factorization, Frobenius or root interpolation, and CRT construct such a solution in expected polynomial bit complexity. Rejection sampling plus this promise solver therefore factors every distinct odd semiprime; factoring trivially solves every promise instance.

**Order-2 qualification.** If exactly one local type is \((3)\), any valid globally nonidentity involution is component-selective and known factors construct one. Unlike the order-3 mismatch, this promise is not recognized by the discriminant/Jacobi bit. Its constant random density does not authorize calls to a solver with no guaranteed off-promise behavior. Concretely, \(N=15\), \(f=X^3+10X^2+6X+10\) has unit discriminant with Jacobi symbol \(-1\), types \((12)/(111)\), and the involution \(X\mapsto2+3X+8X^2\) is nonidentity on both sides while every coefficient gcd is 1. Thus the naive unconditional order-2 reduction is false, not merely unproved.

**Why full geometric rank does not fix it.** Geometrically, the order-dividing-3 locus is always the identity and two 3-cycles, hence rank 3. In types \((111),(3)\) all three descend, while in type \((12)\) the two nonidentity points form a quadratic orbit. The order-dividing-2 locus analogously has rank 4 in every type. Invariants depending only on geometric nonemptiness or full geometric rank see no type drop; rational-point descent or a mixed CRT choice is the hidden idempotent step. This does not rule out every coordinate projection, resultant, subresultant, or elimination invariant.

**Exact equations and evidence.** The coefficient equations for endomorphism, the unit Jacobian determinant, and \(\sigma^2=1,\sigma^3=1\) are derived in experiments/F10_autkill/REPORT.md. Named runs R01–R06 and every failure are in its manifest. The hostile audit in experiments/F10_aut_audit/RESULT.md independently derived every equation, checked the characteristic-3 schemes, exact counts, reductions, and reverse constructions, and reran both small examples; A01's serialization failure is retained and authoritative A04 passed. The proof-blind reconstruction in experiments/F10_aut_reconstruct/RESULT.md recovered the theorem, explicit complexity bounds, rational-descent scope, promised examples, and order-2 counterexample; its timeout-bounded exhaustive verifier passed. The \(N=35,f=X^3+2\) enumeration finds exactly six global automorphisms; the selective order-3 maps \(X\mapsto11X\) and \(X\mapsto16X\) both expose 5 through \(\gcd(b-1,35)\). Finite computation certifies only the examples. The corrected general statements are P17 in `PROVED.md`.

**What would make a retry materially new.** A fixed-degree family whose local certificate has a division-free geometric rank or determinant mismatch rather than only a rational-point-count mismatch, or a factor-free polynomial-time descent/canonization algorithm whose output is not already component-selective by definition. Merely shrinking the automorphism base does not address the \(N^3\)-sized image search.

## X12 — canonical PSC localization on the coefficient-hard AKS witness

**Status:** promoted as P18 after hostile audit and proof-blind reconstruction.

**Family:** F04.

**Classification:** method failure for the fixed canonical principal Sylvester coefficients of the standard AKS errors under the standard minimal-\(r\), standard-shift scan. This does not close arbitrary minors, pivot-dependent transcripts, nonstandard parameters, or other group-algebra invariants.

**Closest prior route and material difference.** P11 closes raw coefficient gcds on the same input. C13 shows a canonical PSC can separate P14, but only where a raw coefficient already does. X12 applies the richer determinant family to the genuinely coefficient-hard P11 witness.

**Hostile-audited theorem and certificate.** Under C13's fixed determinant convention, \(D_j(F,G)\) over a field is nonzero exactly when \(j\) occurs in the nonzero ordinary Euclidean remainder-degree sequence of \(F,G\), excluding the initial degree \(\deg F\) and including \(\deg G\) and the gcd degree. The audit replaced the discovery proof's unsupported informal PRS block-scaling step with a direct determinant-kernel and extended-Euclid argument, covering gaps, positive gcd, and \(D_{\deg G}=\operatorname{lc}(G)^{\deg F-\deg G}\). On

\[
N=20000000499999937
=100000007\cdot199999991,\qquad r=2953,
\]

every globally formed standard error \(H_a\), \(1\le a\le2942\), has degree 2952 and unit coefficients. In both local fields, every Euclidean degree chain is the complete sequence \(2953,2952,\ldots,0\). Hence all 8,687,726 canonical determinants per field are nonzero and every global gcd is 1.

**Evidence and scope.** Exact named R08 exhausts all shifts under a 900-second timeout; R05/R09 materialize all 2953 local PSC residues at the endpoint shifts, and R10 checks every row and artifact hash. The hostile audit's A03 checked 4,932 field pairs and 17,556 direct defining determinants; A04 independently reran every global coefficient and local degree chain; A05 passed every count/hash/endpoint/CRT check. The proof-blind reconstruction independently proved the theorem, checked 231,494 literal small-field determinants, materialized every global coefficient in a separate 69,513,632-byte artifact, verified both complete field chains, and reconciled every count and hash. All failed launches, source-retention limitations, sparse-Sage-list errors, the discovery's noncompliant X00, and the reconstruction's incidental pre-source diagnostic and packaging failure are disclosed and excluded. The corrected theorem and finite obstruction are P18 in `PROVED.md`. Finite computation refutes a universal auxiliary claim but proves no asymptotic factoring statement.

**What would make a retry materially new.** A specified noncanonical minor family or elimination invariant with polynomially many globally computable entries and a proved inverse-polynomial local mismatch probability; or a nonstandard AKS modulus/error family not covered by this exact witness.

## X13 — one-hot schoolbook multiplication as structured exact CVP

**Status:** promoted as P19 after hostile audit and proof-blind reconstruction.

**Family:** F11.

**Classification:** method failure for landing the natural exact multiplication-CSP lattice in bounded-treewidth, fixed/low-codimension, or the naive Toeplitz convolution class. The exact factoring-to-CVP reduction itself survives as promoted theorem P19, and no lower bound against all structured lattice encodings is claimed.

**Exact promoted reduction.** For each factor-length pair \(2\le a\le b\) with \(a+b\in\{n,n+1\}\), use factor bits, four one-hot tuple indicators for each \((i,j)\), and binary carry digits. Affine equations enforce tuple choice, shared marginals, all multiplication columns, and the final carry. Their binary solutions are exactly length-\((a,b)\) factorizations. If the system \(Az=d\) is integrally feasible, polynomial-bit HNF/SNF computes an integral point and a basis of \(\ker_{\mathbb Z}A\). In its \(M=O(n^2)\) integer coordinates, every point has squared distance at least \(M/4\) from the all-\(1/2\) target, with equality exactly for a binary solution; the next possible contribution raises squared distance by at least 2. Exact search CVP at the baseline therefore yields a verified factor, while prime, even, repeated-factor, prime-power, unbalanced, and arbitrary-composite handling and recursive cost are explicit. The approximation ratio tends to 1, so standard constant-factor approximation does not suffice.

**Why the proposed structure fails.** The exact incidence graph contains a subdivision of \(K_{a,b}\), giving treewidth at least \(\min(a,b)\), and \(ab\) linearly independent one-hot equations give codimension at least \(ab\). The linear convolution relaxation omits \(Z=xy^T\). At \(N=25,a=b=3\), the true matrix from \((1,0,1)^T(1,0,1)\) and

\[
\begin{pmatrix}1&0&1\\0&1&0\\0&0&1\end{pmatrix}
\]

have the same padded anti-diagonal sums \((1,0,2,0,1,0)\) and carry sequence \((0,0,0,1,0,0,0)\), while the second has determinant 1 and rank 3. Both are binary and tie at the absolute half-target minimum, so not every relaxed optimum is certified as a factor outer product. This does not prove that all postprocessing fails; in this example the shared convolution polynomial is \((1+T^2)^2\) and still exposes 5.

**Verification and exact remaining gap.** The hostile audit repaired the normal-form justification, fixed the scope to search CVP, and removed the two overclaims above. The proof-blind reconstruction independently recovered the final-carry convention, carry bound, polynomial-bit normal forms, embedded and full-rank CVP normalizations, gap, recursion, graph minor, codimension, and narrow \(N=25\) certificate. These corrected statements are P19 in `PROVED.md`. A polynomial-time exact-CVP algorithm for the high-width, high-codimension multiplication-gadget lattices would already imply arbitrary integer factoring through this reduction. A materially new retry needs an exact encoding that both preserves Boolean rank one and provably belongs to an independently tractable lattice class, or a new exact-CVP algorithm exploiting structure not captured by width or codimension.

## X14 — cleared elliptic \(x\)-collision products at the square-root threshold

**Status:** promoted as P20 after hostile audit and proof-blind reconstruction.

**Family:** F02.

**Classification:** method failure for the cleared product of pairwise \(x\)-coordinate differences among consecutive elliptic multiples at \(m=\lfloor\sqrt N\rfloor\). This does not close other dynamics, other elliptic observables, ECM-style denominator failures, or the multiplicative-torus specialization.

**Closest prior route and material difference.** P03 gives one synchronized orbit for a fixed duplication-Lattès map on \(N=15\). X14 treats general consecutive multiples on every good short Weierstrass curve and every affine seed for one balanced input, using division polynomials and Hasse's theorem rather than a hand-selected orbit.

**Exact obstruction.** For \(m\ge3\), standard division polynomials satisfy

\[
\phi_i\psi_j^2-\phi_j\psi_i^2=\psi_{i+j}\psi_{j-i}
\qquad(1\le i<j\le m).
\]

Consequently the cleared collision product

\[
C_m(P)=\prod_{i<j}(\phi_i\psi_j^2-\phi_j\psi_i^2)(P)
\]

vanishes at an affine point of order \(t\) exactly when \(t\le2m-1\); all denominators through \(m\) are nonzero exactly when \(t>m\). At

\[
N=10403=101\cdot103,\qquad m=101,
\]

the integral Hasse upper bounds are 122 and 124, both below \(2m-1=201\). Thus for every short Weierstrass curve good at both primes and every global affine point, \(C_m\) vanishes in both fields and \(\gcd(C_m,N)=N\). Randomizing the good curve or point cannot separate this input. A nonunit discriminant yields a factor only when its gcd is proper; a full gcd is a retry, not a split.

The denominator-clean certificate

\[
E:y^2=x^3+x+5,\qquad P=(5461,5889)\pmod N
\]

has local point orders 112 and 106, both strictly between 101 and 201. Its first lexicographic collisions are \((11,101)\) modulo 101 and \((5,101)\) modulo 103, so the simultaneous zero is genuinely caused by \(x(Q)=x(-Q)\), not by a denominator through \(m\).

**Surviving torus reduction.** The multiplicative analogue factors exactly as

\[
\prod_{0\le i<j<m}(a^i-a^j)
=a^{\binom m3}S_m(a),\qquad
S_m(a)=\prod_{d=1}^{m-1}(1-a^d)^{m-d}.
\]

For a unit modulo a prime, \(S_m(a)=0\) exactly when its order is at most \(m-1\). P20 proves that a uniform exact evaluator for \(S_m(a)\bmod N\) in time polynomial in \(\log N+\log m\) would yield complete classical Las Vegas polynomial-time factoring for every integer, including repeated prime factors and prime powers. The displayed recurrence still takes \(O(m)\) iterations, and the cyclotomic rewrite still has \(m-1\) displayed factors. Neither is the required evaluator or a lower bound against one.

**Evidence.** The discovery, all failed-run dispositions, and exact certificate are in `experiments/F12_elliptic_collision_kill`; the hostile audit in `experiments/F12_elliptic_collision_audit` corrected the real \(m\ge3\) restriction, the full-discriminant-gcd case, and the recursive complexity bound; the proof-blind reconstruction in `experiments/F12_elliptic_collision_reconstruct` independently recovered the identities, certificate, all-input conditional reduction, success bound, and complete recursion. The corrected theorem is P20 in `PROVED.md`. No cross-family audit has run.

**What would make a retry materially new.** A uniform factor-free polylogarithmic evaluator for the weighted torus product, or a different dynamical observable with both a proved polylogarithmic evaluation rule and inverse-polynomial asymmetric local behavior. Faster evaluation alone cannot repair the elliptic separator on the balanced obstruction.

## X15 — natural fixed-binomial compression of the torus threshold product

**Status:** promoted as P21 after hostile audit and proof-blind reconstruction.

**Family:** F02.

**Classification:** method failure for fixed positive-binomial/lcm compression, the literal two-child q-Pochhammer evaluator, and constant-work-per-equal-floor grouping. This is not evidence against every arithmetic circuit or exact evaluator for the torus product.

**Closest prior route and material difference.** X14/P20 isolates the weighted torus product as a sufficient evaluator target but supplies only a recurrence linear in the threshold. X15 tests several proposed ways to compress that exact product to polylogarithmic work.

**Exact obstruction.** Any positive binomial product whose zero set over every finite field is exactly the set of units of order at most \(M\) must contain every exponent strictly between \(M/2\) and \(M\), hence at least \(\lceil M/2\rceil\) distinct exponents. The one-lcm shortcut fails already for \(M=4\): 2 has order 12 modulo 13, so \(1-2^{12}=0\), while the true unweighted and weighted products are 3 and 7. The exact shifted addition law has two independent children and therefore \(M\) leaves in its literal recursive evaluator. Equal-floor cyclotomic grouping has at least \(2\lfloor\sqrt M\rfloor-1\) groups; an unweighted aggregate also loses the nonconstant weights. Explicit root-set polynomials have large degree, but none of these facts lower-bounds arbitrary circuit size.

The hostile audit also corrected the relationship between the unweighted and weighted products. They have the same prime support, and the unweighted gcd divides the weighted gcd, but the gcds can differ on prime powers: \(N=875,a=631,m=3\) gives 175 versus 875. The proof-blind reconstruction independently recovered the corrected theorem, counterexamples, recurrence identities, and all stated scope limits. The promoted statement is P21.

**What would make a retry materially new.** A shared division-free circuit, fast weighted interval-product identity, characteristic-sensitive representation, or other evaluator with a symbolic polylogarithmic bit-complexity proof. Repackaging the factors in a fixed binomial list, a literal two-child tree, or one unweighted aggregate per equal-floor group is not new.

## X16 — principal-unit and canonical-high-digit carriers from exponentiation by \(N\) modulo \(N^2\)

**Status:** promoted as P22 after hostile audit and proof-blind reconstruction.

**Family:** F12.

**Classification:** method failure for treating the principal input digit of \(a^N\bmod N^2\), direct gcds of a fixed polynomial-size collection of canonical output digits from a uniform base, and the displayed consecutive/additive defects as a universal separator. This is not evidence against every \(N^2\)-adic construction or deliberately engineered/adaptive bases.

**Closest prior routes and material difference.** F07/P12 encounters a scalar order-spectrum bottleneck, while F04 studies additive Frobenius errors modulo \(N\). X16 uses a materially different carrier: the principal \(p\)- and \(q\)-adic digits modulo \(N^2\), their exact valuations, and Teichmüller lifts.

**Exact obstruction.** The full principal reduction kernel is \(K=\{1+kN\}\), but exponentiation by \(N\) sends all of it to 1 and depends only on the residue modulo \(N\). Locally it is the twisted Teichmüller map \(([a]_p^q,[a]_q^p)\). Consecutive image iterates have no valuation-one local difference, so a quotient after a full gcd supplies no second stage. The additive defect has an exact three-category formula; for twins \(q=p+2\), \(p>3\), its success is \(4(p-2)/((p-1)(p+1))\) with no second-stage gain, while \((3,5)\) is the verified \(7/8\) exception.

The unconditional asymptotic obstruction concerns canonical output digits. For every odd balanced pair \(p<q<2p\), every fixed set of \(K\) iterate indices, and a uniform unit base,

\[
\Pr(\text{some direct high-digit gcd splits }N)
\le
K\left(\frac2{q-1}+\frac1{p-1}\right)
\le\frac{3K}{p-1}.
\]

Bertrand supplies an infinite balanced family, so polynomial \(K\) in the input length gives exponentially small success. The hostile audit corrected the twin theorem to require \(p>3\) and independently reproduced the formulas and fibre bound. The proof-blind reconstruction recovered the corrected structure, the exceptional twin, the exact carrier formulas, and the nonadaptive uniformity scope. The promoted theorem is P22.

**What would make a retry materially new.** A component-selective construction using engineered or adaptive nonuniform bases, cross-base relations, or a different \(N^2\)-adic operation with a proved inverse-polynomial success probability. Merely resampling uniform principal digits, taking more fixed iterates, or dividing a consecutive full-gcd difference by \(N\) is not new.

## X17 — ordinary affine stabilizer chains on a small base

**Status:** promoted as P23 after hostile audit and proof-blind reconstruction.

**Family:** F13.

**Classification:** method failure for converting the natural affine/nonabelian lift into an ordinary explicit-permutation Schreier–Sims or Luks computation merely because the action has a constant-size base. This does not close quotient certificates, succinct/circuit actions, direct matrix algorithms, or other nonabelian lifts.

**Closest prior route and material difference.** F07/P12 studies dense spectral and moment representations of modular multiplication. X17 instead embeds the period in an affine action and tests explicit faithful permutation degree and stabilizer-chain orbit size.

**Exact obstruction.** Although \(\operatorname{AGL}_1(\mathbb F_p)\) has natural base size 2 for \(p>2\) and 1 for \(p=2\), its minimum faithful permutation degree is \(p\). Every nontrivial normal subgroup contains the translation \(C_p\), so every nonfaithful local action kills all translations and a faithful diagonal local family must contain a faithful degree-\(p\) component. For arbitrary \(N=\prod\ell^e\),

\[
\mu\!\left(\operatorname{AGL}_1(\mathbb Z/N\mathbb Z)\right)
=\sum_{\ell^e\parallel N}\ell^e.
\]

In particular, the exact degree for a distinct semiprime is \(p+q\), exponential in the bit length on balanced inputs. The matching disjoint CRT action is factor-aware and proves no factor-free construction. The hostile audit corrected the \(p=2\) base sizes and homogeneous-vector conventions; the proof-blind reconstruction independently recovered the prime-power theorem, local normal-subgroup lemma, exact edge cases, and explicit-action scope.

The succinct \(2\times2\) affine representation is not excluded. Its most direct cyclic vector test has

\[
\operatorname{Stab}_{\mathbb Z}((1,0)^T)
=\operatorname{ord}_N(a)\mathbb Z
\]

under \(\operatorname{diag}(a,1)\), so asking for the least positive stabilizer is exactly order finding, not a new stabilizer algorithm.

**What would make a retry materially new.** A factor-sufficient quotient whose kernel may discard translations, a proved algorithm polynomial in a succinct action description rather than its expanded degree, or a factor-free matrix/module stabilizer whose computation is not merely modular order finding. Reusing an ordinary explicit permutation chain under the label "small base" is not new.

## X18 — joint AKS row matroids and one-axis prefix summaries

**Status:** promoted as P24 after hostile audit and proof-blind reconstruction.

**Family:** F04.

**Classification:** method failure for the complete row matroid on the standard shifts, all row prefixes, all full-row column prefixes, the lexicographically first column basis, raw-entry gcds, and the canonical first-\(A\)-column determinant. This is explicitly not a failure of the complete column matroid: the same witness has a verified two-tail column separator.

**Closest prior route and material difference.** P18 makes every fixed canonical principal Sylvester coefficient a unit on the coefficient-hard P11 input, shift by shift. X18 stacks every standard error into one global matrix and tests joint linear dependence across shifts. Row matroids and column matroids are different invariants and cannot be conflated.

**Exact obstruction.** For

\[
N=20000000499999937
=100000007\cdot199999991,
\qquad (A,r)=(2942,2953),
\]

the globally formed standard-shift matrix has an invertible first-2942-column block in both local fields, with determinants \(56136614\) and \(132391112\). Thus both row matroids are the same free matroid, every row-prefix rank is its length, every full-row column-prefix rank is \(\min(t,2942)\), and both greedy column scans select \(0,\ldots,2941\). The global base determinant is a unit, as are all raw entries. These polynomial-size joint summaries therefore do not universally localize the AKS failure.

**Surviving refinement.** The full column matroids are not equal. Removing base columns \(423,2336\) and adding global columns \(2944,2948\) gives determinant residues \(15564403\) and \(0\), whose global residue has gcd \(199999991\) with \(N\). Every one-tail exchange agrees, while an exhaustive scan finds exactly two mismatches among all 237,941,605 two-tail exchanges. The specified determinant is factor-free and division-free evaluable over \(\mathbb Z/N\mathbb Z\), but the successful exchange was discovered factor-assistively and no uniform selector or separation theorem is known.

**Evidence.** The two candidate studies retain global matrices, exact local ranks/solves, complete one-/two-tail zero-pattern scans, direct exchanged determinants, all commands, timeouts, logs, outputs, and failure dispositions. The hostile audit rebuilt every global entry, validated the large retained matrices, reproduced both exact local solves and the exhaustive scan, and passed A09; its A02 timeout and A03/A04 serialization failures are retained and excluded. The proof-blind reconstruction independently formed both instances, recomputed all 8,687,726 P11 entries through a separate FLINT implementation, recovered the analytic P14 proof and P11 exchange, and passed the final run-025 cross-audit. P24 records the corrected common theorem.

**What would make a retry materially new.** A globally specified polynomial-size minor family or factor-free adaptive rule with a proved inverse-polynomial chance of selecting a local support mismatch for every composite input; a nonstandard modulus/shift construction with such a theorem; or a nonlinear joint invariant whose selection cost and bit complexity are explicit. Another row-rank or one-axis prefix summary is covered by this obstruction.

## X19 — iid uniform Hurwitz one-sided-gcd collisions

**Status:** promoted as P25 after hostile audit and proof-blind reconstruction.

**Family:** F14.

**Classification:** evidence against the exact auxiliary mechanism of taking polynomially many iid uniformly oriented norm-\(N\) Hurwitz quaternions and using one-sided Euclidean gcds, product-zero incidences, or fixed local ideal-equality menus. This is not a lower bound against nonuniform/adaptive sampling or non-collision noncommutative methods.

**Closest prior route and material difference.** The nearest prior mechanisms are F03's commutative polynomial gcd localization and F09's cyclotomic ideal orientation. X19 instead uses a genuinely noncommutative order that is Euclidean on both sides. On a successful collision, the greatest common one-sided divisor itself has norm \(p\) or \(q\), so the mechanism need not end in a single integer gcd of a public \(\mathbb Z/N\mathbb Z\) computation.

**Exact obstruction.** For distinct odd primes \(N=pq\), the norm shell has

\[
|S_N|=24(p+1)(q+1),
\]

and its left-unit orbits are exactly the pairs of projective row lines over \(\mathbb F_p,\mathbb F_q\); right-unit orbits give image lines. For two iid uniform samples, a greatest common right divisor has norm distribution

\[
(1,p,q,N)
\quad\text{with probabilities}\quad
\frac{(pq,q,p,1)}{(p+1)(q+1)},
\]

and a left gcd has the same law. Hence proper success is only \((p+q)/((p+1)(q+1))\). With \(K\) samples, even every-pair testing has success at most

\[
\binom K2\frac{p+q}{(p+1)(q+1)}
=O(K^2/\sqrt N)
\]

on an infinite balanced family. Polynomially many samples in the input bit length are exponentially below the \(N^{1/4}\) birthday scale. Product-zero tests and fixed reduced-ideal sums/intersections/ranks depend on the same projective equality partitions.

**Corrections and evidence.** The hostile audit normalized the order, corrected the same-source right action to \(B_1B_2^{-1}\), restricted non-unit transforms to the \(N\)-part of the gcd norm, kept ideal-lattice claims local after reduction, separated row and image orientations of one sample, and weakened the necessary scale statement to \(\Omega(N^{1/4})\). Its timeout-bounded exact enumeration verified all \(576^2\) ordered pairs at \(N=15\), the proper probability \(1/3\), both handednesses, product incidences, and the failures at ramified 2 and repeated norm 9. The proof-blind reconstruction independently recovered the orbit/ideal proof, handedness dictionary, exact laws, corrected fixed transforms, and sampling boundary. P25 records only the corrected common theorem.

**Sampling and scope.** The theorem grants exact-uniform samples for free and still obtains the obstruction. It does not construct such a sampler. A find-one four-square algorithm is not an exact-uniform shell sampler, and unit multiplication does not change the large orientation orbit. Ramification at 2 and repeated prime powers lie outside the rank-one squarefree theorem. Adaptive or deliberately biased samplers, singular or sample-dependent transforms, integral invariants not controlled by reduced equality partitions, and other quaternion algorithms remain open.

**What would make a retry materially new.** A completely specified factor-free sampler from bare \(N\) with proved polynomial bit complexity and inverse-polynomial asymmetric local collision behavior; an adaptive/nonlinear transform whose success is not already a trace-free-coordinate gcd; or a non-collision quaternion invariant with a uniform all-input theorem.

## X20 — bounded numerical scaled-Fermat scans and literal CRT trace wheels

**Status:** promoted as P26 after hostile audit and proof-blind reconstruction.

**Family:** F15.

**Classification:** method failure for enumerating every numerical multiplier \(k\le\operatorname{poly}(\log N)\) with a polynomial Fermat scan, and for literal materialization, unconditioned uniform sampling, or explicit lift enumeration of square-residue CRT wheels. This is not evidence against large binary-encoded multipliers or implicit, adaptive, interval-conditioned, or biased metric decoders.

**Closest prior route and material difference.** F11/P19 encodes exact factors as a structured closest-vector target. X20 instead asks whether bare \(N\) can cheaply manufacture an Archimedean approximation to \(p+q\), and its terminal extraction is an integer discriminant rather than a residue-ring polynomial separator.

**Exact obstruction.** For each fixed polynomial pair \(K,T\), infinitely many balanced semiprimes have \(q/p\) sufficiently close to \(\sqrt2\) that every factor-revealing allocation of every \(k\le K(n)\) has scaled-Fermat threshold distance greater than

\[
\frac{p}{432K(n)^3}>T(n)+1.
\]

The family depends on \(K,T\), all allocations and parity cases are covered, and a factor of \(kN\) must be intersected with \(N\) to recover the unknown prime. Separately, each auxiliary prime accepts exactly \((\ell+(N/\ell))/2\) trace residues. A squarefree CRT wheel therefore has \(m^{1-o(1)}\) literal states; across a balanced trace interval of length \(L=\Theta(\sqrt N)\), the correct two-regime bound is \(L^{1-o(1)}\) materialized states/uniform trials when \(m\ge L\), or explicit accepted lifts when \(m\le L\).

**Corrections and evidence.** The hostile audit corrected the fixed-\(K,T\) quantifiers, factors-of-\(kN\) wording, allocation/parity certificate, and implicit-decoder scope. The proof-blind reconstruction independently recovered the complete proof and showed why broader claims are false: small fixed \(m\) has few states, and a huge tailored \(m>L\) can leave exactly one accepted interval lift. No computation supports the theorem; all three reports are proof-only. P26 records only their corrected common result.

**What would make a retry materially new.** A polynomial-size list of \(N\)-dependent exponentially large multipliers with a proved close allocation, a compressed character-condition interval solver, a biased trace sampler with inverse-polynomial target mass, or another factor-free metric observable. Merely enlarging the fixed numerical polynomial cap or explicitly adding more wheel primes is covered.

## X21 — exact-iid imaginary-quadratic ambiguity hunting

**Status:** promoted as P27 after hostile audit and proof-blind reconstruction.

**Family:** F16.

**Classification:** method failure for direct exact-uniform ambiguous-class hits, exact-iid square-collision birthday amplification, ordinary inverse-orbit collisions using only their group relations, free genus postselection of an otherwise uniform law, and the displayed \(\lambda/2\) and \(h/2\) powers without their missing data. This is not evidence against designed nonuniform class distributions, other powers, real infrastructure, or arbitrary class-group methods.

**Closest prior route and material difference.** F14/P25 uses noncommutative quaternion ideals and outputs a one-sided divisor norm. X21 uses canonical reduced imaginary-quadratic forms; a useful ambiguous form exposes \(p,q\) directly through its integer coefficients, without first constructing a zero divisor over \(\mathbb Z/N\mathbb Z\).

**Exact obstruction.** There are two ambiguous classes for \(\Delta=-N\) and four for \(\Delta=-4N\), exactly half useful. The public even-discriminant class

\[
[2,2,(N+1)/2]
\]

is a nonprincipal but useless counterexample to universal extraction. With class number \(h\) and \(t=|G[2]|\in\{2,4\}\), direct exact-uniform success is \(t/(2h)\). The complete square-collision scheme has exact occupancy formula P27 and birthday scale \(\Theta(\sqrt{h/t})\). Siegel's lower bound makes polynomially many samples exponentially unlikely on infinite balanced families.

Ordinary inverse-orbit collisions can retain \(X^2\); useful \(4\)-torsion occurs with probability at most \(t^2/(2h)\), so the original zero-contribution shorthand was false but no birthday gain results. For \(\Delta=-4N\), the public character \(\chi_{-4}=\chi_N\) disproves the claim that every individual genus character needs a hidden prime-discriminant factor. Complete chosen-genus access still improves useful mass by only \(t\le4\).

**Corrections and evidence.** The hostile audit corrected the public genus character, \(4\)-torsion channel, undefined near-uniform scope, four-versus-two split-prime root count, and universal powering overclaim. Its authoritative Sage A02 checked 630 semiprimes, 21 exact occupancy cases, and nine finite abelian powering groups; the cache failure, JSON failure, and noncompliant diagnostic are retained and excluded. The proof-blind reconstruction independently recovered the corrected classification, exact probabilities, asymptotics, genus and powering scope, and auxiliary-prime construction without computation. P27 records only the corrected common theorem.

**What would make a retry materially new.** A fully specified factor-free distribution on split-prime forms or a class-group walk with proved polynomial bit cost and inverse-polynomial useful mass; a computable order/exponent surrogate that makes a useful power without assuming the target data; a factor-revealing composition failure; or a real-quadratic/infrastructure mechanism. Merely resampling exact-uniform classes, adding inverse-orbit comparisons, or conditioning on the constant genus vector is covered.

## X22 — integer-coordinate and polynomial finite-menu Hurwitz bias

**Status:** promoted as P28 after hostile audit and proof-blind reconstruction.

**Family:** F14.

**Classification:** evidence against the exact auxiliary mechanisms of restricting the norm-\(N\) Hurwitz shell to integral coordinates, sampling that slice by direct coordinate rejection, and selecting from a polynomial fixed menu of unit/conjugation transforms. This does not close sample-combining nonlinear maps, a sampler designed around local stabilizer mismatch, mixed-handed invariants, or non-collision quaternion methods.

**Closest prior route and material difference.** X19/P25 treats ideal iid uniform sampling over the full Hurwitz shell and ordinary one-sided orientation collisions. X22 tests an explicit strict coordinate slice, its factor-free sampler, adaptive postselection from fixed transform menus, and the qualitatively different strategy of taking two points in one right-unit orbit.

**Exact obstruction.** Every left- and right-unit orbit of odd norm contains exactly eight integral-coordinate elements. Uniform sampling from the Lipschitz slice is therefore still exactly uniform on each local row quotient and, separately, on each local image quotient. Its ordinary one-sided-gcd collision probability is unchanged from P25. The explicit coordinate-triple rejection sampler is exact, but on balanced \(N=pq\) it takes \(\Theta(\sqrt N)\) trials, \(\Theta(\sqrt N\log N)\) expected random bits, and \(\sqrt N\operatorname{polylog}N\) expected bit time.

For a \(C\)-map menu whose local output orientation is a fixed projective bijection of an input row or image, a memoryless adaptive selector has local collision probability at most \(C/(r+1)\). Even a joint/stateful selector over all \(K\) raw samples has per-pair probability at most \(C^2/(r+1)\). Hence polynomial \(C,K\) still have exponentially small all-pairs success on balanced inputs. The theorem does not cover a map that combines the raw samples.

**Surviving conditional extractor.** For a fixed norm-\(N\) quaternion \(\alpha\), two independent uniform actual right units give exact proper-gcd probability

\[
\frac{|H_p(\alpha)\triangle H_q(\alpha)|}{12},
\]

where \(H_r(\alpha)\) is the stabilizer of its local row line under the faithful projective \(A_4\)-action. A mismatch yields a direct prime norm in conditional expected polynomial bit time. But the event is not automatic: \(\alpha=1+i+2j+3k\) at \(N=15\) succeeds with probability \(1/4\), while \(\alpha=1+i+j+6k\) at \(N=39\) succeeds with probability \(0\). No efficient factor-free method is known for manufacturing a favorable \(\alpha\).

**Evidence.** The hostile audit independently proved all orbit, sampling, menu, handedness, stabilizer, and complexity statements; corrected memoryless versus stateful quantifiers and small-characteristic wording; directly checked norm-\(r\) right divisors; and completed all 53 distinct odd semiprimes through 300. The proof-blind reconstruction recovered the corrected theorem and both hand certificates without seeing the proof. P28 records the common theorem.

**What would make a retry materially new.** A fully specified factor-free expected-polynomial sampler with a proved inverse-polynomial probability of \(H_p(\alpha)\ne H_q(\alpha)\); a transform that genuinely combines samples and comes with a distribution theorem; a mixed row/image or mixed-handed construction not controlled by the finite-menu bound; or a non-collision Hurwitz invariant. Another coordinate slice, coordinate rejection sampler, or polynomial menu of separate fixed transforms is covered by P28.

## X23 — the exact level-two Eisenstein coefficient as an independent metric primitive

**Status:** promoted as P29 after hostile audit and proof-blind reconstruction.

**Family:** F15.

**Classification:** factorization equivalence for the exact high-information interfaces \(b_N\), \(24b_N\), caller-supplied \(O(\log N)\)-bit modular output, and a known additive polynomial-width approximation on the distinct-odd-semiprime promise. This is not a failure of automorphic methods generally, nor of fixed-small-modulus, coarse, cuspidal, twisted, Brandt, or modular-symbol data.

**Closest prior route and material difference.** X20/P26 tests numerical scaled-Fermat scans and literal CRT trace wheels. X23 asks for a fixed modular-form coefficient at a binary-encoded index. Its terminal decoder is an exact discriminant computation and uses no gcd, but evaluating the coefficient is the entire missing problem.

**Exact obstruction.** For

\[
F(z)=2E_2(2z)-E_2(z)=1+24\sum_{m\ge1}b_mq^m\in M_2(\Gamma_0(2)),
\]

one has

\[
b_m=\sigma_1(m_{\rm odd}).
\]

Hence, for \(N=pq\) with distinct odd primes,

\[
b_N=N+p+q+1.
\]

Exact \(b_N\) reveals \(p+q\). So does \(24b_N\bmod 24\cdot2^n\), where \(n=\lceil\log_2(N+1)\rceil\), because \(0<p+q<2^n\). A known exactly encoded bound \(|h-b_N|\le K(n)\) with numerical polynomial \(K\) leaves only polynomially many trace candidates. In every case the discriminant \((p+q)^2-4N\) recovers and verifies the factors in deterministic polynomial bit complexity. Conversely, a complete factorization computes \(b_m\) multiplicatively.

The promise is essential: \(b_9=13\) and \(b_6=4\) do not obey the distinct-prime trace formula. The theorem packages the familiar divisor sum in an Eisenstein series; it supplies no factor-free evaluator and no lower bound.

**What would make a retry materially new.** A fixed-small-modulus or coarse-relative interface, a cusp form or nontrivial twist, another level or weight, low-index Hecke data, Brandt or modular-symbol data, or any automorphic observable with a proved polynomial evaluator and an information path not already equal to \(\sigma_1\). Re-presenting the exact divisor sum as a metric or spectral oracle is covered by P29.

## X24 — matched-handed collisions from a residual-only four-square finder

**Status:** promoted as P30 after hostile audit and proof-blind reconstruction.

**Family:** F14.

**Classification:** method failure for polynomially many independent outputs of the unconditional Pollack--Treviño residual-only four-square finder, tested by right gcds of right-gcd outputs, left gcds of separately computed left-gcd outputs, fixed projective unit translates, or within-output matched stabilizers. This does not cover mixed handedness, genuine sample-combining maps, or other completion laws.

**Closest prior route and material difference.** X19/P25 grants exact-uniform samples from the full Hurwitz norm shell, while X22/P28 tests the integral-coordinate slice and a direct rejection sampler. X24 uses an actual unconditional expected-polynomial four-square algorithm. Its conditional law is not full-shell uniform, but each residual conic fibre has an exact projective bijection.

**Exact obstruction.** Conditional on the accepted residual and fresh completion randomness, both the row and image of \(\beta\bmod r\) are uniform on

\[
\mathcal S_r=
\{[u:v]:u^2+v^2\ne0\},
\qquad
|\mathcal S_r|=r-\left(\frac{-1}{r}\right).
\]

A left-normalized gcrd inherits the row; a separately computed right-normalized gcld inherits the image. Thus \(K\) independent outputs have all-pairs proper collision probability at most

\[
\binom K2\left(
\frac1{p-(-1/p)}+\frac1{q-(-1/q)}
\right)
\]

per matched hand. All fixed unit classes add only a constant. Exact supported-line stabilizer counts bound the within-output survivor by \(O(1/p+1/q)\). The Pollack--Treviño modulus is exactly \(\operatorname{lcm}(n,P)\), its kernel has the required residual-only interface, and its expected bit and exact-random-bit costs are polynomial. Hence every named direct test is exponentially sparse on an infinite balanced family.

**What would make a retry materially new.** A mixed row/image or mixed-gcd construction with an exact law; a nonlinear map that combines several finder outputs and accumulates information jointly rather than unioning rare pair events; a completion allowed to depend on the fibre point with a proved useful bias; or a non-collision quaternion observable. Resampling the same finder and amortizing only by testing more independent matched-handed pairs is covered by P30.

## X25 — independent mixed-handed four-square menus and dimension-only pooling

**Status:** promoted as P31 after hostile audit and proof-blind reconstruction.

**Family:** F14.

**Classification:** method failure for polynomially many independent mixed-handed one-sided-gcd comparisons, both product orders, fixed projective transform menus, wrong-hand single-output stabilizer menus, and every fixed polynomial family of pooled orbit-span **dimensions**. This does not close a joint decoder that combines ubiquitous nonzero data.

**Closest prior route and material difference.** X24/P30 controls only matched handedness and separate local marginals. X25 proves the full conditional CRT product law, controls arbitrary transcript-dependent normalization, covers every independent hand and product order, and then uses the exact same-source row--image graph to test both cross hands.

**Exact obstruction.** With \(s_r=r-(-1/r)\), every wrong orientation of an arbitrarily normalized one-sided divisor has atom at most

\[
\frac{12(r'+1)}{s_rs_{r'}}\le\frac{27}{r+1}.
\]

Thus one fixed independent comparison succeeds properly with probability at most

\[
27\left(\frac1{p+1}+\frac1{q+1}\right),
\]

and polynomial calls, pairs, and fixed menus stay exponentially sparse on balanced semiprimes. The complete wrong-hand unit stabilizer menu has the analogous constant 378.

For the same raw output,

\[
\operatorname{im}_r\beta=J_{C,r}\operatorname{row}_r\beta,
\]

and the two exact split-free menus are \(2[i](\bar C D_LU)\) and \(2[i](\bar CUD_R)\). At \(N=91\), the certified \(M=273\) output makes all twelve entries in both menus coprime to 91, so there is no pointwise guarantee.

Finally, \(Q_t=\bar C_tD_{L,t}\) generates the two-dimensional right ideal of matrices with image in \(\operatorname{row}_r\beta_t\). A pooled subset has dimension two iff all those lines coincide and dimension four otherwise. Fixed dimension-only profiles therefore reduce to birthday equalities.

**What would make a retry materially new.** An adaptive or implicit subset rule, exact pooled row spaces, a coefficient/pivot/minor or resultant system, a noncommutative product, a spectral/discrepancy statistic, a genuinely nonlinear joint decoder, or a completion with proved fibre-point bias. Merely testing more independent relations or more fixed span-dimension subsets is covered by P31.

## X26 — unmultiplied endpoint-only SQUFOF localization

**Status:** promoted as P32 after hostile audit and proof-blind reconstruction.

**Family:** F17.

**Classification:** evidence against the exact auxiliary mechanism of discarding the infrastructure transcript and extracting only from one reduced endpoint by coefficient gcd or the standard proper-square test. This is not a failure of SQUFOF, infrastructure methods, metric decoders, or factoring.

**Closest prior route and material difference.** X21/P27 studies exact-uniform ambiguity hunting in imaginary class groups. X26 moves to the ordered real principal infrastructure and asks whether a complete cycle or exact endpoint position manufactures a factor-bearing form.

**Exact obstruction.** For

\[
a=6t+1,\qquad N=a^2+2,\qquad \Delta=4N,
\]

one has

\[
\sqrt N=[a;\overline{a,2a}],
\qquad
(1,2a,-2)\xleftrightarrow{\rho}(-2,2a,1).
\]

Every endpoint coefficient is coprime to \(N\), and the only positive right square is \(1\), already queued/listed as improper period completion. Sign and counter-parity qualifications do not create another square. Yet \(3\mid N\) publicly, repeated factors occur, and the regulator is only \(\Theta(\log N)\), so this is neither a hard family nor an infrastructure lower bound.

**What would make a retry materially new.** A multiplier or different discriminant, an intermediate composition/reduction coefficient, a relative generator or compact power product, a failure-event decoder, an adaptive distance/jump decoder, or any joint use of endpoints and transcripts. Another single-endpoint coefficient or an absolute-value square test is covered by P32.

## X27 — coarse canonical-isogeny neighbors without an exposed selective kernel

**Status:** promoted as P33 after hostile audit and proof-blind reconstruction.

**Family:** F18.

**Classification:** factorization equivalence for the fine selective-kernel task and method failure for returning an arbitrary coarse modular-polynomial root or an opaque isogeny certificate. This does not close \(N\)-dependent fine selectors, higher CM, vertical, or supersingular routes.

**Closest prior route and material difference.** X04/P09 studies blind characteristic substitution in a Frobenius/Hasse--Witt formula. X27 instead tries to orient CRT factors by selecting a canonical isogeny neighbor; the decisive distinction is coarse target versus recoverable kernel section.

**Exact obstruction.** At \(j=1728\),

\[
\Phi_2(1728,Y)=(Y-1728)(Y-287496)^2.
\]

The double coarse root is rational even over a finite field where \(-A\) is a nonsquare and neither nonpublic two-torsion kernel descends from the specified twist. Thus an arbitrary coarse root carries no selective orientation.

On \(N=pq\) with distinct odd primes, \(A\) a unit, and \(\left(\frac{-A}{N}\right)=-1\), an exposed finite étale rank-two subgroup is exactly a nonzero residue

\[
u(u^2+A)\equiv0\pmod N.
\]

It is mixed across the two CRT components, and \(\gcd(u,N)\) and \(\gcd(u^2+A,N)\) are the complementary factors. Uniform random \(A\) reaches the promise with probability at least \(4/15\). Hence constructing this fine object is already semiprime factoring; the missing selector has not been built.

**What would make a retry materially new.** An explicit \(N\)-dependent construction that returns a kernel polynomial, rational map, or other representation from which the selective nonidentity section is recoverable in polynomial time; compatible local CM embeddings; or a vertical/supersingular mechanism. Another public/coarse root, a target \(j\), an opaque certificate, or a universal rational-function selector is covered by P33.

## X28 — explicit evaluation of the Boolean many-relation product

**Status:** promoted as P34 after a corrected hostile audit and proof-blind
reconstruction.

**Family:** F02.  The optional Hurwitz provenance was removed because it is
mathematically dispensable.

**Classification:** evidence against the exact auxiliary mechanism of gaining
a polynomial-time algorithm merely by observing that exponentially many rare
subset relations have constant pooled mass.  This is not a circuit lower
bound and does not close implicit modular evaluators or other joint decoders.

**Closest prior route and material difference.** X15/P21 studies a torus
order-threshold product and blocks several literal compression schemes.  X28
uses a Boolean subset-sum product with pairwise-independent local tickets.
Unlike a polynomial union of birthday events, its pooled local zero event
has proved constant probability on balanced semiprimes.

**Exact boundary.** For \(N=pq\), \(53\le p<q<2p\), and

\[
K=\lfloor\log_2\lfloor\sqrt N\rfloor\rfloor-3,
\qquad
Q_K=\prod_{\varnothing\ne S\subseteq[K]}
\sum_{i\in S}a_i,
\]

uniform independent \(a_i\bmod N\) give

\[
\Pr(1<\gcd(Q_K,N)<N)
\ge
\frac{2}{32\sqrt2+1}
\left(1-\frac{\sqrt2}{8}\right).
\]

The OR statement is exact separately modulo \(p\) and \(q\), not globally
over \(\mathbb Z/N\mathbb Z\).  Thus a polylogarithmic exact evaluator would
give a constant-trial promised splitter.

The proved evaluator instead splits the variables in half and uses monic
product and remainder trees over the composite ring.  It has exact
\(N^{1/4+o(1)}\) bit time and space.  Direct Gray-code evaluation has
\(N^{1/2+o(1)}\) bit time and polynomial space.  The minimal-polynomial,
hyperplane-divisibility, cube-tree, and literal-support facts do not imply an
arithmetic-circuit or compressed-state lower bound.  No all-input factoring
algorithm follows.

**What would make a retry materially new.** A uniform division-free circuit
or other implicit evaluator with bit cost polynomial in \(\log N\), together
with a proved all-input or reducible promise theorem; a different pooled
observable whose joint decoder is genuinely polynomial; or a symbolic lower
bound in a precisely named model strong enough to exclude the missing
evaluator.  Re-enumerating the subsets, using the displayed meet-in-the-middle
tree, or quoting exponential formal degree is covered by P34.

## X29 — high-dimensional public zero-syndrome relation lattices

**Status:** promoted as P35 after a corrected hostile re-audit and proof-blind
reconstruction.

**Family:** F19.

**Classification:** method failure for the public zero-syndrome
Construction-A kernel, fixed-output coefficient/Gram high-dimensional
amortization, block-diagonal Hurwitz sums, CVP subtraction inside the public
intersection, and the displayed below-threshold graph slice.  This is not a
failure of the public output lattice, scaled dual, a faithful fixed-rank
metric decoder, biased targets, or nonlinear combinations.

**Closest prior route and material difference.** P19 encodes multiplication
as an exact but high-width CVP instance, while P30/P31 control projective
collision tickets from four-square outputs.  X29 instead asks whether many
locally low-rank algebraic samples create a public metric gap whose shortest
vector lies in exactly one hidden local kernel.

**Exact obstruction.** For

\[
K_r(A)=\{x\in\mathbb Z^d:Ax\equiv0\pmod r\},
\]

one has

\[
K_N=K_p\cap K_q,
\qquad
\det K_N=p^{s_p}q^{s_q}.
\]

Unequal local ranks already factor through an SNF determinantal divisor.
With equal ranks, the one-local-only disjunction is not a public subgroup.
The exact rational kernel of a fixed-output map is primitive and consumes
the apparent extra dimensions; after quotienting it, the faithful rank is at
most four for one quaternion output.  Subtracting any vector of \(K_N\)
preserves both local syndromes, so CVP in the public intersection cannot
create a local-zero event.

For norm-\(N\) Hurwitz multiplication, the local ideals have exact minima
\(\sqrt p,\sqrt q\), while the public intersection
\(\bar\alpha\mathcal H\) is an exact rotated \(\sqrt N\)-similarity of the
fixed Hurwitz lattice.  Direct sums retain those scales.  Below residual
length \(r\), the named graph embedding selects only the public
intersection.

P35 explicitly derives but does not close

\[
\Lambda_{\rm out}=A\mathbb Z^d+N\mathbb Z^t,
\qquad
\Lambda_{\rm dual}=N\mathbb Z^d+A^{\mathsf T}\mathbb Z^t.
\]

No shortest/closest-vector distribution or extraction theorem is known for
them or for the faithful fixed-rank quotient.

**What would make a retry materially new.** A completely specified output,
dual, quotient, affine-target, or nonlinear lattice construction with a
polynomial algorithm and inverse-polynomial factor-extraction law; or a new
exact obstruction for one of those explicitly open objects.  Adding more
samples to the same shared-output zero-syndrome/Gram map, or block-diagonalizing
the same Hurwitz multiplication maps, is covered by P35.

## X30 — common-basis holographic contraction of the separated
COPY--AND multiplier

**Status:** promoted as P36 after a corrected hostile re-audit and
proof-blind reconstruction.

**Family:** F20.

**Classification:** method failure for the explicit bipartite
ternary-fanout realization under one common basis per copied input role and
the required transpose-dual action on adjacent AND inputs.  This is not a
failure of fused cells, high-arity equality, edge-dependent gauges, other
gate sets, other Pfaffian identities, or non-matchgate exact contraction.

**Closest prior route and material difference.** P10 refutes scalar carry as
a sufficient exact multiplication state, P19 gives an exact multiplication
CVP reduction without a tractable landing, and P29 identifies a
factor-sufficient trace oracle without an evaluator.  X30 instead encodes
the complete multiplication witness as a tensor-network count.  An exact
polynomial contraction of every prefix-pinned network would output a divisor
by count self-reduction, without a terminal factor-extracting gcd.

**Exact obstruction.** Ordinary contraction pairs \(T\) with
\((T^{-1})^{\mathsf T}\), not \(T^{-1}\).  The complete basis
classification for parity-pure ternary COPY gives an alternating
original-one/original-zero coordinate ratio \(r(-1)^b\) under the correct
dual action.  With independent ratios \(x,y\) on the two AND inputs and
arbitrary independent output columns \(u,v\), every transformed output
slice has the form

\[
u(1+xs+yt)+vxy\,st.
\]

The forbidden-parity equations force \(x=y\) and \(x=-y\), while every
zero-coordinate escape forces \(xy=0\).  Hence AND cannot be a ternary
matchgate whenever the two directly adjacent leaf COPY tensors are
matchgates.

Complete padded ternary fanout trees, neutral unary legs, a common leaf
depth, and binary equality subdivisions realize that direct adjacency in a
literal bipartite polynomial-size network without changing witness counts.
The failure occurs before planarity or full-adder identities are relevant.

**What would make a retry materially new.** A fused multiplier-cell
signature satisfying all required matchgate identities; a globally
compatible edge-dependent gauge; a high-arity equality treatment not
reducible to the displayed ternary leaves; a different planar
Pfaffian/sub-Pfaffian construction with exact pinned counts and polynomial
bit growth; or a non-matchgate tractable tensor family containing the full
pinned multiplication network.  Reusing the separated COPY\(_3\)--AND\(_3\)
pair under a common role basis is covered by P36.

## X31 — public quotient-scale and uniform cyclic metric manufacture

**Status:** promoted as P37 after a corrected hostile re-audit and a fresh
proof-blind reconstruction.

**Family:** F19.

**Classification:** evidence against the exact auxiliary mechanism that the
public output lattice, scaled dual, their faithful orthogonal quotients, or
the fixed-completion cyclic tail automatically manufacture a hidden
\(p/q\) metric scale.  This is not a failure of full-lattice SVP/CVP,
biased arithmetic samples or targets, nonlinear combinations, or arbitrary
public lattices built from \(N\).

**Closest prior route and material difference.** X29/P35 closes the public
zero-syndrome kernel and shared-output high-dimensional Gram amortization,
but explicitly leaves the output and scaled-dual lattices open.  X31 treats
those objects, their public exact-direction quotients, and the smallest
fixed-completion output tail.

**Exact obstruction.** Smith form either exposes a proper factor or has only
\(1\)- and \(N\)-gcd blocks.  Removing the common public primitive
\(1\)-block orthogonally gives exactly \(p\), \(q\), and \(N\)
times one public projected lattice, on both output and transpose sides.
The original full lattice is not orthogonally split by this statement.

Under a shared completion and the explicit maximal-minor surjectivity
condition, the output tail is

\[
L_C=O_C=\mathbb ZC_0+N\mathbb ZD
\]

on the unfactored branch.  It has one public exact direction; its faithful
quotient is one-dimensional and its scaled rank-two dual is only a rotation.
Coordinate divisibility of
\(v=aC_0+NbD\) is exactly \(\gcd(N,a)\).  Uniform cyclic CVP targets
give probability \(1/p+1/q-2/N\), and marginally uniform nonisotropic
completion lines give only \(O(1/p+1/q)\) probability that any shortest
vector exposes a factor on balanced odd semiprimes.

**Verification caveat.** A first blind package falsely required every
nonzero Smith invariant to be coprime to \(N\); \(A=(N)\) refuted it.
That failed artifact is preserved and was replaced by a genuinely fresh
reconstruction of the exact effective-rank \(1\)-/\(N\)-block theorem.

**What would make a retry materially new.** A fully specified biased
completion or affine-target law; an inverse-polynomial coordinate-gcd theorem
for a polynomial-time optimizer in the original nonorthogonally coupled full
lattice; a batch without shared completion whose growing informative rank is
proved; or a nonlinear metric observable.  Reusing determinant, finite
quotient, projected shape, uniform cyclic targets, or uniform completion-line
SVP is covered by P37.

## X32 — direct positive terminal-deletion gadgets for factor-witness matching graphs

**Status:** promoted as P38 after four hostile audit rounds and a strict
proof-blind reconstruction.

**Family:** F21.

**Classification:** evidence against the exact auxiliary mechanism of
composing a positive matching representation from direct single-rail or exact
one-hot dual-rail terminal-deletion signatures.  This is not a method failure
for closed internal-edge decoders, off-code filtering, block codes, or one
global multiplication-specific graph.

**Closest prior route and material difference.** X30/P36 blocks a separated
COPY--AND landing in an exactly contractible matchgate basis.  X32 instead
uses ordinary unweighted bipartite perfect matchings and their
almost-uniform positive sampler.  A matching would decode directly to a
factor witness; no tensor contraction, prefix count, or terminal
factor-extracting gcd is used.

**Exact obstruction.** For

\[
\mathcal F_H=\{S:H-S\text{ has a perfect matching}\},
\]

all feasible sets have fixed parity and satisfy matching symmetric exchange.
In a bipartite graph they also have fixed left-minus-right boundary charge.
If nonempty support consists exactly of one-hot dual-rail codewords, its
sets are equicardinal delta-matroid feasible sets and hence matroid bases.
Basis exchange within an exact one-hot code can only swap the two rails of
one logical coordinate.  Every varying coordinate is therefore independently
flippable, so the logical relation is a subcube.

COPY\(_3\), AND\(_3\), full addition, and the fused
\(a+c+xy=s+2d\) relation all fail the direct single-rail parity test and
the exact one-hot subcube test.  Positive multiplicities and arbitrary
internal auxiliary vertices cannot change support.  Classical Valiant
gadgets use cancellation, congruences, or interpolation at the aggregate
permanent level and do not supply individual positive readable matchings with
equal witness fibers.

**Positive conditional boundary.** If a uniform polynomial-size bipartite
graph did have only readable factor witnesses with one positive multiplicity
per ordered divisor, JSV almost-uniform sampling would return a proper divisor
with probability at least \(1/4\) per fresh call.  Exact rational/fair-bit
implementation and recursion give complete all-input Las Vegas polynomial
factoring.  X32 closes a proposed landing, not this conditional theorem.

**What would make a retry materially new.** A closed graph decoded from
internal edges; a connector whose off-code states are proved globally
impossible; a block or heterogeneous occurrence code; an assignment-dependent
auxiliary-state projection; or a globally interleaved graph with a proved
matching-mass law.  Reusing direct single rail or exact one-hot dual rail is
covered by P38.

## X33 — exact SVP in the independent-uniform full CRT code lattice

**Status:** promoted as P39 after a corrected hostile audit, clean re-audit,
and strict proof-blind reconstruction.

**Family:** F19.

**Classification:** evidence against the exact auxiliary claim that a
polynomial batch of independent uniform local code relations makes a
factor-divisible slice win exact SVP in the original full lattice.  This is
not a method failure for biased or dependent arithmetic samples, affine
targets, CVP/LLL, nonshortest statistics, or nonlinear decoding.

**Closest prior route and material difference.** X29/P35 treats public
zero-syndrome and shared-output Gram/Hurwitz lattices. X31/P37 treats
output/dual quotients and a fixed-completion cyclic tail but leaves
nonorthogonal full-lattice coupling open. X33 analyzes that complete ambient
lattice in the clean random-code model without projecting its exact
directions away.

**Exact obstruction.** For independent uniform \(u\)-subspaces
\(C_p,C_q\) of \(\mathbb F_p^m,\mathbb F_q^m\), the full CRT lattice
has determinant \(N^{m-u}\), and its factor-divisible slices are exactly

\[
L\cap p\mathbb Z^m=pL_q,
\qquad
L\cap q\mathbb Z^m=qL_p.
\]

Every shortest vector lies below
\(\min(2v_m^{-1/m}N^{1-u/m},N)\).  Dividing a \(p\)-slice vector by
\(p\) leaves a fixed nonzero residue that enters \(C_q\) with probability
\((q^u-1)/(q^m-1)\), and symmetrically.  Exact eligible lattice-point
counts plus the unit-ball bound show that, for fixed \(u,\kappa,K\) and

\[
p\le q\le\kappa p,\qquad u<m\le(\log N)^K,
\]

the probability that **any** exact shortest vector has proper coordinate gcd
is \(N^{-u/2+o(1)}\).  When \(u<m<2u\), the actual event is eventually
empty; the looser cube-volume expression is not used for that exponent.

**What would make a retry materially new.** A public factor-free arithmetic
source whose local subspaces have a proved bias or dependence defeating the
incidence bound; a biased affine target with an inverse-polynomial CVP law; a
polynomial-time nonshortest/LLL statistic; growing informative local rank; or
a nonlinear full-lattice decoder.  Merely increasing the number of
independent uniform fixed-rank relations and asking exact SVP for a
coordinate-gcd vector is covered by P39.

## X34 — low-actual-degree products of full-affine CRT relations

**Status:** promoted as P40 after a corrected audit sequence, a clean final
hostile audit, and a fresh context-free proof-blind reconstruction.

**Family:** F22.

**Classification:** evidence against the exact auxiliary claim that feeding
all coordinates of polynomially many full-affine CRT samples into a product
of low-actual-degree polynomial tests creates genuine joint amortization.
This is not evidence against high-degree succinct evaluation, nonuniform or
correlated sources, metric tests, or a decoder using typical nonzero values.

**Exact obstruction.**  For \(N=pq\), local actual degree sums
\(\Delta_p,\Delta_q\), and nonzero formal reductions, the local product-zero
rates satisfy

\[
\alpha_r\le\min(1,\Delta_r/r),
\]

while the proper product-gcd probability is exactly

\[
\alpha_p+\alpha_q-2\alpha_p\alpha_q.
\]

The sharp envelope from the two local caps is
\(\max\{u_p,u_q,u_p+u_q-2u_pu_q\}\), and the simpler all-degree bound is

\[
\min\left\{1,\frac{\Delta_p}{p}+\frac{\Delta_q}{q}\right\}.
\]

Products over a field only OR their factors' zero sets; CRT then XORs the two
local OR events.  No independence among relations is used, but no information
from ubiquitous nonzero outputs is combined either.  On balanced semiprimes,
polynomial total actual degree gives exponentially small success and
inverse-polynomial success requires
\(\Omega(\sqrt N/\operatorname{poly}(\log N))\) actual degree.

Random coefficients require conditioning before CRT independence is used;
fresh-batch adaptation is valid but same-sample selection is not.  Formal
zero products obey the exact four-case table in P40, while explicit one-sided
coefficient content already factors.  Formal nonzero zero-functions and
polynomial-size sparse/circuit descriptions of exponential degree remain
outside the useful low-degree conclusion.

**What would make a retry materially new.** A succinct characteristic-scale
product with a proved inverse-polynomial local XOR law and factor-free
evaluator; a source with a proved nonuniform/conditioned metric law; or a
decoder that combines rank, kernel, resultant, spectral, or other information
from typical nonzero outputs.  Replacing polynomially many scalar zero tests
by their low-degree product, determinant, or another polynomial contraction
is covered by P40.

## X35 — obvious classical samplers for quadratic Fourier energy

**Status:** promoted as P41 after a clean initial audit, strengthening by
strict reconstruction, a fresh hostile re-audit, and a context-free final
reconstruction.

**Family:** F23.

**Classification:** method failure for uniform rejection, direct uniform-gcd
discovery, and the lazy uniform-proposal independence-Metropolis chain.  This
is not a failure of the quadratic-energy distribution itself or of all
classical samplers.

**Positive conditional boundary.**  For odd \(N\),

\[
\left|\sum_{x\bmod N}e^{2\pi i kx^2/N}\right|^2
=N\gcd(k,N).
\]

The normalized law \(\pi_N(k)=\gcd(k,N)/S(N)\) has factor-revealing mass at
least \(2/7\) on every odd composite, sharply at \(N=9\).  Therefore an
all-input explicit sampler within TV \(1/28\), with almost-sure termination
and expected polynomial bit/fair-bit cost, gives complete classical Las Vegas
factoring.  The sampler is the missing lemma.

**Exact obstruction.**  On balanced distinct semiprimes, uniform rejection
has \(\Theta(N)\) expected proposals and direct uniform proper-gcd discovery
has \(\Theta(\sqrt N)\) expected trials.  For lazy independence Metropolis,

\[
\mathbf1_{\{0\}}-N/S(N)
\]

is an exact eigenfunction with eigenvalue
\(1-S(N)/(2N^2)\).  Hence the gap is at most \(S(N)/(2N^2)\) and worst-start
mixing is \(\Omega(N)\) on distinct semiprimes.  Initializers that neutralize
the zero atom but place \(o(1)\) mass on factor classes still face an
\(\Omega(\sqrt N)\) uniform-proposal hitting bound.  Exact \(S(pq)\) reveals
\(p+q\), so normalization is not a free oracle.

**What would make a retry materially new.** A nonuniform, nonlocal,
nonreversible, auxiliary-variable, positive-combinatorial, or otherwise
factor-free sampler with a proved all-input stationary/output law and
polynomial bit/fair-bit cost.  P43 promotes the uniform zero-product lift and
closes its exact coordinate heat bath; P44 closes factor-free explicit
scheme-automorphism moves.  F35 tests low-degree finite-set bijections.
Reusing uniform proposals in rejection or independence Metropolis is covered
by P41.

## X36 — clean four-port composition of closed matching occurrences

**Status:** promoted as P42 after a clean hostile audit and a fresh
context-free proof-blind reconstruction.

**Family:** F21.

**Classification:** evidence against the exact auxiliary mechanism of wiring
closed internal-edge Boolean gadgets through a universal positive connector
whose raw boundary support contains only the two equal occupancy states.  It
is not a failure of closed decoding itself or of contextual/global/block
composition.

**Positive survivor.**  A \(3\times3\) bipartite graph with one missing edge
has four perfect matchings whose three marked internal-edge words are

\[
000,010,100,111,
\]

exactly AND.  A six-cycle has two perfect matchings with words \(000,111\),
exactly COPY\(_3\).  Each decoded word has multiplicity one.  Internal-edge
labels therefore escape P38's direct terminal parity/subcube theorem.

**Exact obstruction.**  An occurrence edge consumes two endpoints.  A clean
context-independent connector equating two occurrences on four distinct
ports would require deletion support \(\{\varnothing,B\}\), \(|B|=4\).
Every matching deletion family satisfies symmetric exchange, so applying it
to \(\varnothing,B\) forces an intermediate two-port state.  Arbitrary
auxiliary vertices and nonnegative weights do not alter positive support.

**What would make a retry materially new.** A concrete contextual connector
whose off-code states are proved globally unextendable; a projected auxiliary
or block/heterogeneous occurrence code; shared vertex identifications or
fused cells; or one globally interleaved multiplication graph with a proved
positive matching-mass law.  Reusing a raw universal four-distinct-port
equality wire is covered by P42.

## X37 — random-scan coordinate heat bath on the quadratic-energy positive lift

**Status:** promoted as P43 after two historical failed audits, a clean
whole-artifact hostile re-audit, and a fresh context-free proof-blind
reconstruction.

**Family:** F23.

**Classification:** method failure for the exact random-scan
one-coordinate heat-bath kernel from its stated cold start.  This is not a
failure of the positive zero-product representation, an efficiently
generated warm start, block/nonlocal/augmented kernels, positive matching
encodings, or direct spectral sampling.

**Positive survivor.**  Uniform sampling from

\[
\Omega_N=\{(k,x):kx=0\bmod N\}
\]

has first marginal \(\gcd(k,N)/S(N)\), exactly the normalized quadratic
Fourier-energy law for odd \(N\).  Inspecting both coordinates raises the
proper-gcd mass to at least \(1/3\) on every odd composite.  Therefore a
uniform TV-\(1/12\) expected-polylog pair sampler gives complete all-input
Las Vegas factoring.  A uniform polynomial-size equal-positive-fibre
perfect-matching representation with an efficient short-output decoder
would suffice; none is constructed.

**Exact obstruction.**  The coordinate heat bath is implementable exactly:
sample the updated coordinate uniformly from the other's annihilator.  For
\(N=pq\), distinct odd primes, \(h=p+q-2\), and start \((1,0)\), its
factor-bearing hitting expectation is \(\Omega(N/h)\), while

\[
t_{\rm mix}(1/4)\ge\left\lfloor\frac{N}{8h}\right\rfloor.
\]

Both are \(\Omega(\sqrt N)\) on balanced semiprimes.  The exact local
interpretation uses \(H,V,O\) types; origins have no artificial axis label,
and prime powers have separate valuation strata.

**What would make a retry materially new.** An efficiently generated warm
start with a proved law; a block, nonlocal, nonreversible, or augmented-state
kernel; a positive matching graph satisfying the full uniform
builder/decoder/multiplicity interface; or a direct sampler not using this
coordinate update.  Reusing the exact cold-start random-scan heat bath is
covered by P43.

## X38 — explicit zero-product scheme-automorphism proposals

**Status:** promoted as P44 after an amendment-verified hostile audit and a
fresh context-free proof-blind reconstruction.

**Family:** F23.

**Classification:** evidence against factor-free movement by adaptive
mixtures of explicit coordinate-algebra automorphisms of \(KX=0\) over a
distinct semiprime.  This is a factor-or-invariant dichotomy, not a
nonexistence theorem for a construction that deliberately exposes a factor.

**Exact obstruction.**  Over a field, every node automorphism is a unit
scaling of the two axes, with or without a swap.  Over
\(R=\mathbb Z/pq\mathbb Z\), different local preserve/swap orientations make
a first-jet coefficient vanish in exactly one component, and its gcd with
\(N\) factors.  If no jet coefficient factors, orientations synchronize,
the automorphism is globally a monomial unit scaling/swap, and it preserves

\[
(R^\times,0)\mathbin{\dot\cup}(0,R^\times)
\mathbin{\dot\cup}\{(0,0)\}.
\]

Uniform zero-product pairs put more than one-half mass outside this region.
The first jet is extracted intrinsically in polynomial time from a
division-free straight-line circuit by evaluation modulo \((K,X)^2\).

**What would make a retry materially new.** A noninvertible or stochastic
move, a finite-set-only permutation, a lifted/auxiliary kernel, an explicit
division/rational or piecewise model with a different extraction theorem, a
useful warm start, or a prime-power construction.  Merely composing or
adaptively choosing more accessible global node automorphisms is covered by
P44.

## X39 — low-formal-degree finite-set bijections of the zero-product locus

**Status:** promoted as P45 after the original sampler-impossibility version
failed hostile audit, a materially amended whole artifact passed fresh
hostile re-audit, and a context-free proof-blind reconstruction succeeded.

**Family:** F23.

**Classification:** evidence against factor-free movement by adaptive
mixtures of explicit low-formal-degree polynomial bijections of the finite
zero-product point set over a distinct semiprime.  This is a quantitative
factor-or-invariant dichotomy, not a proof that an accurate sampler cannot
exist.

**Exact obstruction.**  If \(T=(F,G)\) is a polynomial-induced bijection of
\(\Omega_N\), both exact formal outputs have degree at most \(D\), and
\(2D<\min(p,q)\), root counting forces each local source axis wholly onto one
target axis.  Mixed local preserve/swap orientations make an axis-restriction
coefficient selectively divisible and hence factor \(N\).  On the no-factor
branch the orientations synchronize and preserve

\[
\mathcal A_N=
(R^\times,0)\mathbin{\dot\cup}(0,R^\times)
\mathbin{\dot\cup}\{(0,0)\}.
\]

For an explicit uniformly bounded division-free circuit run, monitoring the
initializer and all materialized restriction coefficients gives

\[
\Pr(H)\ge
\frac{2N-2}{(2p-1)(2q-1)}
-d_{\rm TV}(\mu,\pi_N).
\]

Thus a factor-free run is more than \(1/2\) from uniform, while an accurate
sampler may legitimately succeed by exposing a factor.  A uniform or
inverse-polynomial TV gap below \(1/2\) gives only a repeatable
distinct-semiprime splitter, not complete all-input factoring.

**What would make a retry materially new.** A characteristic-scale succinct
finite-set permutation, a noninvertible or stochastic kernel, auxiliary or
lifted state, a rational/division/opaque or genuinely piecewise model, a
charged useful warm start, a positive-combinatorial sampler, or a theorem for
prime powers and nonsquarefree bases.  More factor-free synchronized
low-degree global bijections are covered by P45.

## X40 — cellwise matchgate landing of the propagated shifted-add multiplier

**Status:** promoted as P46 after a clean hostile audit and a fresh
context-free proof-blind reconstruction.

**Family:** F20.

**Classification:** evidence against the exact auxiliary mechanism which
turns each copy of the natural minimal scalar-Boolean propagated schoolbook
cell into a planar matchgate by invertible local leg gauges.  It is not a
tensor-contraction lower bound.

**Positive survivor.**  The eight-leg relation

\[
\mathbf 1[x_L=x_R]\mathbf 1[y_U=y_D]
\mathbf 1[a+c+x_Ly_U=s+2d]
\]

tiles a planar shifted-add multiplier.  Product bits and every factor-prefix
query are boundary unaries, and each ordered factor witness has exactly one
internal extension.  Thus the fusion genuinely escapes P36's separated
COPY\(_3\)--AND\(_3\) hypothesis.

**Exact obstruction.**  In the displayed planar rotation, the four incoming
legs and four outgoing legs form complementary contiguous boundary arcs.
Their flattening is a direct sum of four rank-three full-adder blocks and has
rank \(12\).  Every nonzero pure-spinor/matchgate signature, including odd
and degenerate charts, has power-of-two rank across a contiguous cyclic cut.
Independent \(\mathrm{GL}_2\) maps on all eight legs preserve the rank, so
even locally unconstrained gauges cannot make this cell a matchgate.

**What would make a retry materially new.**  A larger fused block passing all
contiguous-rank and matchgate-identity tests; an alternate planar rotation,
packed or projected encoding, or asymmetric tile set; a genuinely global
Pfaffian identity not decomposed into copies of this cell; a precise modular
construction with exact integer recovery; or a non-matchgate polynomial
contraction.  Merely replacing common bases by edge-dependent invertible
gauges is covered by P46.  F38 tests horizontal strip fusions and leaves
general two-dimensional blocks open.

## X41 — smooth-multiplier divisor clouds for direct scaled-Fermat extraction

**Status:** promoted as P47 after a historical amendment audit, a clean fresh
whole-artifact re-audit, and a context-free proof-blind reconstruction.

**Family:** F15.

**Classification:** method failure for target-independent divisor-ratio
clouds and, on one infinite balanced-semiprime family, every direct useful
Fermat-square/gcd scan using an adaptively selected coprime
\(o(\sqrt n)\)-bit multiplier.  This is not a factoring lower bound.

**Positive survivor.**  A polynomial-bit integer \(k\) with known
factorization can have exponentially many allocations \(k=cd\), and one
ordinary square scan of \(kN\) tests all of them without enumerating divisors.
All operands remain polynomial-bit when the represented list, its supplied
factorizations, and its scan caps are uniformly polynomial.

**Exact obstruction.**  Balancing \(cp\) and \(dq\) through \(T\) Fermat
increments requires log-ratio error

\[
O\!\left((kN)^{-1/4}\sqrt{T+1}\right).
\]

The aggregate necessary-window measure is at most

\[
4\sqrt2\,N^{-1/4}
\sum_i\tau(k_i)k_i^{-1/4}\sqrt{T_i+1},
\]

and \(\tau(k)=k^{o(1)}\), so a polynomial target-independent list cannot
cover any fixed ratio interval.  More strongly, primes with
\(q/p\) exponentially close in \(\sqrt n\) to \(\sqrt2\) form an infinite
balanced family on which quadratic irrationality gives useful Fermat gap
\(>p/(432k^3)\) simultaneously for every coprime
\(\log_2k=o(\sqrt n)\).  Polynomial scans miss them even when \(k\) is chosen
after seeing \(N\).

**What would make a retry materially new.**  An \(N\)-adaptive
\(\Omega(\sqrt n)\)-bit multiplier construction with proved concentration on
the actual discrete prime ratio; a joint decoder of multiple nonsquare
residues or full scan transcripts which does not require one useful factor
pair; a different metric observable; or non-gcd extraction.  Merely citing a
large divisor count or a uniformly dense smooth cloud is covered by P47.

## X42 — horizontal fusion of propagated multiplier cells

**Status:** promoted as P48 after a historical amendment audit, a clean fresh
whole-artifact re-audit, and a context-free proof-blind reconstruction.

**Family:** F20.

**Classification:** evidence against the exact auxiliary mechanism which
fuses any finite horizontal strip of the natural P46 scalar-Boolean cell,
contracts only its shared (y)-propagation and ripple-carry legs, and seeks a
characteristic-zero matchgate landing by invertible leg gauges.  This is not
a tensor-contraction lower bound.

**Positive survivor.**  The fusion is an exact multiplicity-one Boolean
tensor.  For local words (X,A,S), its support is

\[
x_i^-=x_i^+,\qquad y_0=y_L,\qquad
A+y_0X+c_0=S+2^Lc_L.
\]

The inherited planar drawing has a literal noncrossing two-lane realization,
and the input and output legs occupy complementary contiguous cyclic boundary
arcs.  Thus horizontal fusion genuinely escapes P46's single-cell scope.

**Exact obstruction.**  Across that cut the tensor is a direct sum of
(2^{L+1}) arithmetic blocks.  Each block contains exactly (2^L+1)
distinct standard basis rows, so

\[
\operatorname{rank}=2^{L+1}(2^L+1).
\]

For every (L\ge1), this has a nontrivial odd factor.  A nonzero
characteristic-zero matchgate/pure-spinor signature has power-of-two rank
across a contiguous cyclic cut, including odd and degenerate charts.
Independent external (\mathrm{GL}_2) gauges preserve the rank, while
compatible internal gauges cancel.  No finite strip in this exact family and
port order can therefore be a matchgate.

**What would make a retry materially new.**  A genuinely two-dimensional
fused block that also contracts vertical (x) or accumulator/sum interfaces;
an alternate rotation, packed/projected/auxiliary encoding, or asymmetric
tile; a global Pfaffian identity not decomposing into these strip signatures;
a separately proved finite-characteristic reconstruction; or a non-matchgate
polynomial contraction.  Another horizontal scalar-cell strip in the
inherited order is covered by P48.

## X43 — ordinary Fourier means and rectangular histograms of inverse-pair clouds

**Status:** promoted as P49 after a scope-amended hostile audit and a fresh
context-free proof-blind reconstruction.

**Family:** F24.

**Classification:** method failure for using polynomially many ordinary
empirical additive-Fourier means, polynomial-\(\ell^1\) linear combinations
of them, or a polynomial-size fixed axis-parallel rectangular histogram of
the easy inverse graph
\((u,u^{-1}\bmod N)\) as a factor-scale metric signal. This is not evidence
against nonlinear or Fourier-dense statistics, hidden-frequency recovery,
other arithmetic sources, or metric hints in general.

**Exact obstruction.** CRT factors every coefficient into two prime
Kloosterman sums. A nonzero common-gcd-free mode satisfies

\[
 |\widehat\mu_N(a,b)|\le\frac{4\sqrt N}{\varphi(N)}
 =N^{-1/2+o(1)}
\]

on balanced semiprimes. One-local-zero modes can genuinely reach
\(N^{-1/4+o(1)}\), but both frequency coordinates then share the hidden
prime and their public common gcd already factors \(N\). Erdős--Turán--
Koksma with the prime-divisible frequency sublattices included gives
\(D_N^*=O(N^{-1/2}\log^2N)\). The exact raw-mean MSE is
\((1-|\mu|^2)/m\), so relative RMSE needs \(N^{1-o(1)}\) samples; the
fourth-moment argument gives only the explicitly quantified
sufficiently-high-absolute-confidence analogue.

**What would make a retry materially new.** A factor-free nonlinear or
Fourier-dense observable with a proved inverse-polynomial signal; an implicit
decoder for the hidden prime-spaced spectral modes; an adaptive, correlated,
nonuniform, or dissipative source; a curved/diagonal metric statistic with a
new discrepancy theorem; exact symbolic amplification of the tiny bias; or
a quantitatively valid ACD/HNP/Coppersmith reduction. Merely adding
polynomially many raw means or rectangular bins is covered by P49.

## X44 — bounded-degree fibre-dependent completion is not uniformly diffuse or coefficient-visible

**Status:** promoted as P50 after the original hostile audit required a
mathematical amendment, a fresh whole-artifact re-audit passed, and a
context-free proof-blind reconstruction recovered the corrected theorem.

**Family:** F14.

**Classification:** counterexample to the proposed dichotomy that every
bounded-degree rational or algebraic completion depending on the actual conic
source point must either have \(O(D/r)\) row/image atoms or reveal a factor
through a visible local-degree discrepancy. This is not a lower bound for
fibre-dependent, metric, or nonlinear extraction.

**Positive survivor.** On every locally nonconstant degree-\(D\) rational
line branch, the Segre pullback degree gives the sharp usable bound

\[
 \Pr[\text{no factor and selected fixed line}]
 \le {2B(D+1)\over r-\chi_r}
\]

for a \(B\)-branch selector. The componentwise graph version replaces the
numerator by the sum of the relevant \(\mathcal O(1,1)\)-degrees. Unequal
local reduced degrees of explicitly supplied binary forms are publicly
visible through homogeneous subresultants. A public point also gives an
exact uniform conic sampler with direct-acceptance probability

\[
 \prod_{r\in\{p,q\}}{(r-1)(r-\chi_r)\over r^2}.
\]

**Exact obstruction.** Given one public source/completion pair, put
\(h=u_0^{-1}c_0\), so \(n(h)=-1\). The completion \(c=uh\) makes
\(u+cj=u(1+hj)\) have a constant row at both CRT primes; the dual completion
\(c=h\bar u\) makes \((1+hj)u\) have a constant image at both primes. Thus
maximal bias can live on a source-dominating constant graph component while
both local degrees agree at zero. The explicit \(N=21\) instance gives
matrix \(\left(\begin{smallmatrix}0&2y\\0&2x\end{smallmatrix}\right)\),
whose row is \([0:1]\) modulo both hidden primes.

**What would make a retry materially new.** A factor-asymmetric metric or
nonlinear use of this synchronized constant family; a same-source joint
algebraic detector proved directly rather than inferred from marginal atoms;
an implicit-graph invariant not reduced to the explicit binary-form theorem;
or a characteristic-scale, piecewise, stochastic, canonical-metric, or
dissipative completion. Another bounded-degree nonconstant branch followed
by a fixed/fresh target test is covered by P50.

## X45 — inverse-polynomial relative ACD noise is not certified by the natural ordinary-LLL decoder

**Status:** promoted as P51 after the original hostile audit found a false
“nonfactor” inference and an incomplete comparison theorem; the corrected
artifact passed a fresh whole-proof re-audit and a context-free proof-blind
reconstruction.

**Family:** F24.

**Classification:** method boundary for the explicit simultaneous-
approximation lattice and ordinary worst-case LLL guarantee on a granted
one-sided approximate-multiple source. This is neither an ACD hardness result
nor evidence that bare \(N\) cannot manufacture the source.

**Positive survivor.** For
\(z_i=pt_i+r_i\), independent uniform \(t_i\bmod q\), and errors jointly
adversarial after seeing all quotients, ordinary LLL has exact success lower
bound

\[
 1-2A\theta^m,\qquad
 A=2^{m/2}q\sqrt{m+1},\qquad
 \theta=\min\!\left(1,
 4\cdot2^{m/2}{B\over p}\sqrt{m+1}+{1\over q}\right).
\]

It is polynomial-time and succeeds with failure
\(2^{-\Omega_\eta(n)}\) when

\[
 {B\over p}\le2^{-(1+\eta)\sqrt n},\qquad
 m=\lfloor(1+\eta/2)\sqrt n\rfloor.
\]

A separate polynomial-time source with this law would therefore give a
conditional Las Vegas factorization on balanced semiprimes.

**Exact obstruction.** At \(B/p=n^{-c}\), approximation-denominator
isolation already needs coarse dimension \(\Theta(n/\log n)\), while
ordinary LLL pays \(2^{m/2}\). For every \(m\), the proved failure term
\(2A\theta^m\) exceeds one and is noninformative. The Dirichlet argument
shows the designated \(q\)-vector is not shortest under its exact condition;
only a strengthened size condition certifies a shorter unit coefficient,
and neither statement rules out gcd-of-SVP factoring.

**What would make a retry materially new.** Manufacture the source from bare
\(N\) at \(2^{-\sqrt n}\) precision; give a fully dimensioned decoder for
inverse-polynomial relative error that avoids the ordinary-LLL loss; prove a
helpful nonadversarial error law; or give a robust joint decoder for partial
inliers. Restating determinant heuristics or dropping the dimension-dependent
LLL factor is covered by P51.

## X46 — known-square finite-field Newton iteration has no enlarged root basins

**Status:** promoted as P52 after a clean hostile audit and a context-free
proof-blind reconstruction.

**Family:** F25.

**Classification:** method failure for the exact proposal that the modular
Newton map of a public square creates large independent \(\pm s\) attraction
basins whose denominator, residual, or root-difference gcds factor \(N\).
This is not evidence against other dissipative or cross-iterate mechanisms.

**Exact obstruction.** The projective Newton map

\[
 [X:Z]\mapsto[X^2+s^2Z^2:2XZ]
\]

is globally conjugate by \([X:Z]\mapsto[X-sZ:X+sZ]\) to projective
squaring. Hence each exact root basin is a singleton. For primes
\(r\equiv3\pmod4\), \(-s^2\) is a nonsquare, so a nonzero orbit never
hits the affine pole. Every named gcd ticket is time-invariant and depends
only on whether the initial coordinate equals \(\pm s\) locally.

On \(N=pq\), \(p,q\equiv3\pmod4\), exact accepted-unit success is

\[
 {2p+2q-10\over(p-1)(q-1)}.
\]

Including all raw residue-sampler gcd tickets raises it only to

\[
 {3p+3q-12\over pq-1}.
\]

PNT in arithmetic progressions supplies an infinite balanced family on which
both are \(O(N^{-1/2})\); more Newton iterations do not alter the event.

**What would make a retry materially new.** Use longer cross-iterate
collisions or orders, a different rational map, a p-adic lift, a nonuniform
correlated source with a proved law, or stochastic/piecewise/canonical metric
dynamics. More restarts or iterations of the same map followed only by the
audited denominator/numerator/residual/root-difference gcds are covered by
P52.

## X47 — fresh compressed shifted-Jacobi correlations do not yield a polynomial-sample factor signal

**Status:** promoted as P53 after a clean hostile audit and a fresh
context-free proof-blind reconstruction.

**Family:** F09.

**Classification:** method failure for polynomially many shifted Jacobi
products evaluated on fresh hidden uniform residues, including collected
repeated shifts, past-measurable adaptive menus, explicitly expanded
polynomial linear combinations, and raw empirical-correlation decoding.
This is not a lower bound for richer Jacobi transcripts or higher-residue
methods.

**Exact obstruction.** After every distinct shift difference is gcd-screened,
CRT factors the mean into two complete prime-field character sums. If some
shift has odd multiplicity, the centered Hasse--Weil bound gives

\[
 |\mathbb EY_H|\le{(s-1)^2\over\sqrt N}.
\]

The exact zero probability is \(s(p+q-s)/N\), while the probability that an
individual shift gcd is proper is \(s(p+q-s-1)/N\). Consequently a nonzero
odd-pattern mean needs \(\Omega(N/(\eta^2s^4))\) fresh samples for relative
RMSE \(\eta\). If all multiplicities are even, the exact mean contains
\(p+q\), but its informative deviation is only \(s(p+q-s)/N\) and requires
\(\Omega(\sqrt N/(\eta^2s))\) samples on fixed-balance families.

An explicitly expanded polynomial statistic with polynomial coefficient
\(\ell_1\)-norm has only polynomial-over-\(\sqrt N\) drift from its public
fair-sign baseline. More strongly, any adaptive transcript releasing one
such scalar per fresh hidden source and using total support \(T\) is within

\[
 {2\Lambda T+T^2/2\over\sqrt N}
\]

in total variation of a public factor-free simulator on a
\(\Lambda\)-balanced semiprime.

**What would make a retry materially new.** Retain the sampled \(x\); expose
the whole per-shift character vector or gcd labels; evaluate several
correlations on the same source; exploit same-source adaptation; compute an
exact symbolic sum; use a dense/succinct statistic outside polynomial
\(\ell_1\) expansion; or provide a genuinely nonlinear joint decoder. Those
channels were explicitly excluded from P53 and must not be dismissed by its
scalar marginal theorem.

## X48 — bounded low-Walsh-degree decisions cannot extract the hidden-source Hadamard--Paley word

**Status:** promoted as P54 after a clean hostile audit and a fresh
context-free proof-blind reconstruction.

**Family:** F09.

**Classification:** method failure for an immediate bounded
low-Walsh-degree decision on one fresh accepted hidden-source word, and for
past-adaptive sequences that release only one bit per fresh word before
discarding the source and row. This is not family closure for joint character
relations or amortized decoding.

**Exact obstruction.** Normalize and deduplicate the shift menu, then
gcd-screen every nonzero difference. For the independently zero-filled word
\(W\), every Walsh coefficient is exactly

\[
 c_S=\mathbb E\prod_{j\in S}W_j
 ={A_p(S)A_q(S)\over N}.
\]

Here \(c_S=0\) for \(|S|=1\), \(c_S=1/N\) for \(|S|=2\), and
\(|c_S|\le(|S|-1)^2/\sqrt N\) thereafter. Parseval gives the exact
chi-square identity. If \(f:\{-1,1\}^m\to[0,1]\) has degree at most \(D\),
accepted-word conditioning gives

\[
 \left|\mathbb E_{\mu_{\rm acc}}f-\mathbb E_{U_m}f\right|
 \le {m(p+q-m)\over N}+{1\over2}
 \left(\sum_{1\le|S|\le D}c_S^2\right)^{1/2}.
\]

For balanced \(N=pq\), \(m\le Cn\), and
\(D\le n/(20\log_2n)\), this is
\(2^{-9n/20+O_C(\log n)}\), without any Fourier-\(\ell_1\) or
support-size restriction. A kernel hybrid sums the same bound for
past-adaptive one-bit rules on independent accepted rows.

The obstruction stops exactly there. The full filled-word support is below
\(4N\), so no whole-word pseudorandomness follows; retaining the sampled
source also destroys the marginal comparison. The separately audited HP-LR
hypothesis would yield all-input Las Vegas factoring, but it already assumes
a uniform high-order decoder that returns a numerical prime factor with
inverse-polynomial probability.

**What would make a retry materially new.** Retain the source and full word;
reuse a row; use high or characteristic-order degree; perform an exact
symbolic transform; or supply a genuine Hadamard--Paley/product-code
list-recovery algorithm returning a verifiable integer factor. Repackaging
polynomially many fresh rows into bounded low-degree one-bit decisions is
covered by P54.

## X49 — opaque common-prime-order Lucas relations do not amortize past the generic collision scale

**Status:** promoted as the narrow generic-method boundary in P55 after a
clean hostile audit and a fresh context-free proof-blind reconstruction.

**Family:** F27.

**Classification:** method failure for the assertion that polynomially many
independently random-encoded, tagged, common-prime-order base/image relations
force polynomial-time recovery of a shared exponent merely by their number.
This is not a failure of the explicit Lucas-torus route.

**What was tried.** Replace each explicit Lucas torus by an independently
encoded cyclic group of common prime order \(\ell\), reveal handles for
\(0,1,\sigma_i e\) with the signs granted, and let an adaptive algorithm pool
all \(K\) transcripts using \(Q\) generic operations and equality tests.

**Exact obstruction.** Every generated handle has an affine formal exponent
\(a+bX\). Distinct affine expressions in one tagged group collide at at most
one secret value. If \(q_i\) handles are generated in group \(i\), the full
adaptive collision set has size at most

\[
C\le\sum_i\binom{q_i+3}{2}
\le\binom{Q+3}{2}+3(K-1).
\]

Outside this set, lazy random encodings couple the real transcript to one
independent of a uniform \(e\), so

\[
\Pr(\widehat e=e)
\le\min\left\{1,{1+C\over\ell}\right\}.
\]

The exact subset, list, and maximum-prior-mass variants are recorded in P55.
Thus constant recovery still needs the generic birthday scale.

**Evidence and surviving positive mechanism.** P55 also proves, independently
of this model, that the actual D-first Lucas sampler has exact fair hidden
orientations, denominator poles return factors, and every clean relation
satisfies \(V=U^{\pm(q-p)}\) pointwise. A decoder for the explicit
coordinates would factor distinct odd semiprimes after exact integer
verification. The hostile audit and blind reconstruction both passed, and
the early-gcd branch was validated by a coupling rather than a false
conditional-fairness claim.

**What would make a retry materially new.** Exploit public coordinate pairs
over \(\mathbb Z/N\mathbb Z\), cross-discriminant resultants or determinants,
unequal composite local orders, non-generator structure, zero divisors, a
proved short-interval algorithm, or a deliberately nonuniform factor-free
sample law. Any successful promise decoder must then be extended to prime
powers, multifactor composites, even inputs, and complete recursion. Another
opaque tagged prime-order pooling argument is covered by P55.

## X50 — multiplicative Teichmüller high-digit graphs have no linear cocycle inconsistency

**Status:** promoted as the narrow method classification P56 after a clean
hostile audit and a fresh context-free proof-blind reconstruction.

**Family:** F12.

**Classification:** method failure for every decoder whose signal is a
nonzero edge residual, ring-linear combination of residuals, left-syzygy or
cycle syndrome, or augmented-versus-coefficient inconsistency in a genuine
multiplicative graph of canonical exponent-\(N\) high digits. This does not
close coefficient-rank, minor/Smith, nonlinear, additive, or higher-carry
processing.

**What was tried.** Use many adaptively or nonuniformly chosen unit bases,
their canonical values

\[
A(a)=a^N\bmod N^2=x(a)+Nh(a),
\qquad
\lambda(a)=h(a)x(a)^{-1}\pmod N,
\]

and multiplicative triangles, paths, cycles, or larger relation graphs. The
intended signal was that the local Teichmüller corrections might satisfy
incompatible cocycles in different hidden CRT components, so pooling many
relations would reveal a factor even when no individual digit did.

**Exact obstruction.** The map \(A:G_N\to(\mathbb Z/N^2\mathbb Z)^\times\)
is a well-defined homomorphism for every \(N\ge2\). With canonical
representatives,

\[
c(x,y)=\frac{xy-\langle xy\rangle_N}{N},
\qquad
\kappa(x,y)=c(x,y)\langle xy\rangle_N^{-1},
\]

one has

\[
\lambda(ab)=\lambda(a)+\lambda(b)+\kappa(x(a),x(b))\pmod N.
\]

For every finite occurrence-labelled genuine multiplicative graph this is
one public global solution

\[
B\lambda=\kappa\quad\text{over }\mathbb Z/N\mathbb Z.
\]

Every edge residual, every adaptive ring-linear pooling of residuals, and
every linear path/cycle elimination is therefore zero modulo \(N\) and
modulo every divisor. For each \(p\mid N\),

\[
\operatorname{rank}_{\mathbb F_p}[B_p\mid\kappa_p]
=\operatorname{rank}_{\mathbb F_p}B_p.
\]

This is only augmented consistency. It neither equalizes
\(\operatorname{rank}B_p\) and \(\operatorname{rank}B_q\) nor controls
arbitrary minors, Smith data, nonlinear eliminants, or the quotient of an
integer residual after division by \(N\).

Occurrence labels cannot generally be discarded. The exact descent theorem
is

\[
A\text{ is determined by }x\text{ on all units}
\iff N_{\rm odd}\text{ is squarefree and }8\nmid N.
\]

At a repeated odd prime, \(1\) and \(1+p\) give the same local \(x\) but
different \(A\); at \(2^e\), \(e\ge3\), \(1\) and \(5\) do so. Odd and
\(2\)-adic logarithms prove that these are the exact retained principal-unit
coordinates, including \(p=3\) and the boundary \(e=3\).

**Evidence.** The complete proof, a hostile reconstruction of every sign and
prime-power case, and a proof-blind end-to-end reconstruction are preserved
under `experiments/F47_teichmuller_cocycle_pooling_kill`,
`experiments/F47_teichmuller_cocycle_pooling_audit`, and
`experiments/F47_teichmuller_cocycle_pooling_reconstruct`. They used no
finite mathematical computation. P56 records the common theorem and the
uniform \(O(Vn^3+En^2)\) bit bound.

**What would make a retry materially new.** Use additive or other
nonmultiplicative relations; a coefficient-rank, minor, Smith, or resultant
selector not equivalent to augmented consistency; a nonlinear whole-graph
statistic; a canonically useful integer quotient after a residual is known
divisible by \(N\); power-map inversion; noncanonical or higher lifts; or an
engineered base distribution with a proved inverse-polynomial all-input
separation law. Another multiplicative linear consistency or cycle-syndrome
decoder is covered by P56.

## X51 — ordinary Dickson trace identities do not localize a unique short index

**Status:** promoted as the narrow promise theorem and method classification
P57 after a clean hostile audit and a fresh context-free proof-blind
reconstruction.

**Family:** F28.

**Classification:** method failure for accumulating powers, products,
repeated bases, Dickson composition/addition identities, or opaque
prime-order trace-orbit relations until one symmetric integer index becomes
identifiable. This is not a failure of explicit-coordinate coherent-root,
derivative, resultant, lift, metric, or other joint decoders.

**What was tried.** For a distinct odd semiprime \(N=pq\), form polynomially
many public pairs

\[
 x=a+a^{-1},\qquad
 y=a^{N-1}+a^{1-N}=D_m(x)\pmod N
\]

and use structured choices of units and Dickson identities to recover the
factor-determining integer \(m=q-p\) or \(m=p+q-2\).

**Exact obstruction.** Put

\[
 e=N-1,\qquad t=p+q-2,\qquad g=q-p,
\qquad L=\operatorname{lcm}(p-1,q-1).
\]

For every unit, \(a^e=a^t\), while the trace also satisfies
\(F_e=F_g\). The complete function alias class is

\[
 F_m=F_e\text{ on }(\mathbb Z/N\mathbb Z)^\times
 \iff
 m\equiv\pm t,\pm g\pmod L.
\]

This follows from the exact one-prime theorem that
\(z^u+z^{-u}=z^v+z^{-v}\) on all nonzero field elements precisely when
\(u\equiv\pm v\pmod{r-1}\), including self-inverse classes. Both positive
representatives factor by a verified integer discriminant, but every
displayed power/product/composition/addition relation is a functorial
identity of the same trace function and cannot choose between them. Adaptive
trace-interface expressions inherit the same exact nonidentifiability.

Shifted traces expose rather than solve the missing orientation. The public
values \(D_{e+k}(x),D_{e-k}(x)\) are the two known roots of

\[
 Z^2-D_e(x)D_k(x)Z+
   (D_e(x)^2+D_k(x)^2-4).
\]

The values \(D_{g+k}(x),D_{g-k}(x)\) are the coherent CRT-mixed roots.
After the double-root gcd is screened, constructing either mixed root is
already factor-sufficient. Symmetric resultants therefore do not select it
for free, although a genuinely joint selector across many such quadratics
remains open.

In an independently random-encoded quotient-by-inversion group of prime
order \(\ell\), \(K\) tags, \(Q\) scalar/addition-pair calls, and an
\(M\)-element output list have success at most

\[
 \min\left(1,{2M+O(Q^2+K)\over\ell}\right).
\]

The exact constants are P57's (57.11)--(57.13). This closes only opaque
generic pooling. Explicit \(\mathbb Z/N\mathbb Z\) coordinates, unequal
composite local orders, non-generators, gcds, and algebraic processing lie
outside the model.

**Surviving data channels.** Formal derivative identities do not follow from
finite trace-function equality; the public \(D_e'\) supplies only a known
orientation, while a short-alias derivative or comparator is missing. The
first lift satisfies

\[
 T(\widetilde a^e)-T(\widetilde a^t)
 \equiv
 NQ_{\widetilde a}
 (\widetilde a^t-\widetilde a^{-t})\pmod{N^2},
\]

where \(Q_{\widetilde a}=(\widetilde a^{(p-1)(q-1)}-1)/N\) is
lift-dependent and not supplied. Lucky gcds such as those from
\(D_e(x)^2-4\), \(D_k(x)^2-4\), and shifted-root differences also remain
live because no uniform probability theorem was proved. Interval/BSGS
enumeration remains exponential absent an independently manufactured
polynomial-size metric candidate set.

**Evidence.** The proof-only candidate, hostile audit, and proof-blind
reconstruction are preserved under
`experiments/F48_dickson_trace_index_kill`,
`experiments/F48_dickson_trace_index_audit`, and
`experiments/F48_dickson_trace_index_reconstruct`, with hashes
`801f86d6acb3c5278ba5f5e1d0ba4db6349b4e9be3878727d29602991c5d6d61`,
`86d840259d1ae0f035f95d4d1785d2c68c6f0a30bcce556f5133aab6bb2ebbef`,
and `278ab46afc83ee25af883f8ef82016084d9b2cdf7f55f0e9d78ac5121ea5dc9a`.
No computation or cross-family audit was used.

**What would make a retry materially new.** A uniform explicit-coordinate
algorithm selecting a coherent mixed root from polynomially many shifted
quadratics; a publicly computable derivative/resultant/minor comparator; a
modulo-\(N^2\) pooling law controlling the lift-dependent quotient without
recovering \(\varphi(N)\); a factor-free metric/list shrinkage; a proved
useful non-generator or lucky-gcd distribution; or a promise decoder plus a
complete extension to prime powers, repeated factors, evens, multifactor
inputs, recursion, and uniform Las Vegas expected bit complexity. Another
collection of trace identities or opaque generic relations is covered by
P57.
