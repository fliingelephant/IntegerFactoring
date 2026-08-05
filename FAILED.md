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

**Classification:** evidence against the exact auxiliary mechanisms of restricting the norm-(N) Hurwitz shell to integral coordinates, sampling that slice by direct coordinate rejection, and selecting from a polynomial fixed menu of unit/conjugation transforms. This does not close sample-combining nonlinear maps, a sampler designed around local stabilizer mismatch, mixed-handed invariants, or non-collision quaternion methods.

**Closest prior route and material difference.** X19/P25 treats ideal iid uniform sampling over the full Hurwitz shell and ordinary one-sided orientation collisions. X22 tests an explicit strict coordinate slice, its factor-free sampler, adaptive postselection from fixed transform menus, and the qualitatively different strategy of taking two points in one right-unit orbit.

**Exact obstruction.** Every left- and right-unit orbit of odd norm contains exactly eight integral-coordinate elements. Uniform sampling from the Lipschitz slice is therefore still exactly uniform on each local row quotient and, separately, on each local image quotient. Its ordinary one-sided-gcd collision probability is unchanged from P25. The explicit coordinate-triple rejection sampler is exact, but on balanced (N=pq) it takes (Theta(\sqrt N)) trials, (Theta(\sqrt N\log N)) expected random bits, and (sqrt N\operatorname{polylog}N) expected bit time.

For a (C)-map menu whose local output orientation is a fixed projective bijection of an input row or image, a memoryless adaptive selector has local collision probability at most (C/(r+1)). Even a joint/stateful selector over all (K) raw samples has per-pair probability at most (C^2/(r+1)). Hence polynomial (C,K) still have exponentially small all-pairs success on balanced inputs. The theorem does not cover a map that combines the raw samples.

**Surviving conditional extractor.** For a fixed norm-(N) quaternion (alpha), two independent uniform actual right units give exact proper-gcd probability

\[
\frac{|H_p(\alpha)\triangle H_q(\alpha)|}{12},
\]

where (H_r(\alpha)) is the stabilizer of its local row line under the faithful projective (A_4)-action. A mismatch yields a direct prime norm in conditional expected polynomial bit time. But the event is not automatic: (alpha=1+i+2j+3k) at (N=15) succeeds with probability (1/4), while (alpha=1+i+j+6k) at (N=39) succeeds with probability (0). No efficient factor-free method is known for manufacturing a favorable (alpha).

**Evidence.** The hostile audit independently proved all orbit, sampling, menu, handedness, stabilizer, and complexity statements; corrected memoryless versus stateful quantifiers and small-characteristic wording; directly checked norm-(r) right divisors; and completed all 53 distinct odd semiprimes through 300. The proof-blind reconstruction recovered the corrected theorem and both hand certificates without seeing the proof. P28 records the common theorem.

**What would make a retry materially new.** A fully specified factor-free expected-polynomial sampler with a proved inverse-polynomial probability of (H_p(\alpha)\ne H_q(\alpha)); a transform that genuinely combines samples and comes with a distribution theorem; a mixed row/image or mixed-handed construction not controlled by the finite-menu bound; or a non-collision Hurwitz invariant. Another coordinate slice, coordinate rejection sampler, or polynomial menu of separate fixed transforms is covered by P28.
