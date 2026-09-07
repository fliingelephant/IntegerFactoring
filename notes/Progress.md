# Research Progress

This is working state for nontrivial intermediate statements and the current synthesis. Every statement must list precise assumptions, proof or certificate, literal status label, and exact remaining gap. Only verifier-backed results may be promoted to `PROVED.md`.

## Current synthesis

The direct-factor core is no longer confined to beta-two zero defect. The
exact quarter-bit carry terminal remains available: a residue of one hidden
factor modulo

\[
L=\operatorname{lcm}(2^t,M)
\]

factors once \(L\ge N^{1/4}/\operatorname{QP}(n)\), where unrelated
certified common primary blocks may accumulate in \(M\). Random uniform
orders, APR rows, modified-AKS shifts, diffuse candidate exponents, and
small-integer words all have exact sparse counterfamilies. Randomness helps
only after an integer-derived source has created factor-correlated support.

P205 gives the sharpest current positive interface for every odd semiprime.
Put

\[
d=\gcd(p-1,q-1),\qquad s_p=(p-1)/d,\qquad s_q=(q-1)/d.
\]

The public exponent \(N-1\) automatically contains the full hidden common
divisor \(d\). For any public QP-bit word \(W\), no factorization of \(W\)
is needed. Testing a uniform unit at exponent \((N-1)W\), then using a
Miller square chain on a verified global return, factors with probability at
least

\[
{1\over2\min(r_p,r_q)},
\qquad
r_j={s_j\over\gcd(s_j,W)}.
\]

Thus one coprime residual need only be reduced to numerical QP. It need not
be fully absorbed, converted into a factored exact order, or passed through
a recursively factored half-size child. This strictly generalizes P204 and
locates the useful role of randomness: after an integer word has made
deterministic residual progress. For

\[
W_K=\prod_{k\le K}(N^k-1),
\]

the sufficient condition is a QP bound on one residual meta-order. No such
all-input bound is known. F237 gives a finite exact warning: on one 129-bit
zero-defect semiprime, both meta-orders exceed \(2^{61}\), and every
\(K\le2^{57}\) leaves a residual above \(2^{58}\). This is not an
asymptotic counterexample.

P206 identifies the exact Las Vegas statistic for integer difference
words. The baseline \((N-1)^n\) removes every residual primary supported on
\(N-1\). For fresh integer samples \(Z,Z'\), the word
\(|Z-Z'|^n\) removes a hidden primary exactly through a collision of two
distinct integers modulo its rational prime. Uniform divisors of a factored
\(N-1\) give a constant-success word when their generated subgroups are
QP-small in every prime of one exterior residual; a prime-power divisor
lattice can instead have zero collision energy. The source target is
therefore inverse-QP distinct-integer aliasing, not a large random support.

P207 closes the complete divisor-only multiplicative grammar. Every
divisor \(B\mid N-1\) has an exact centered-carry identity, and the hidden
common divisor \(d\) is a carry-zero lattice point. Its hidden center
indices are precisely \(s_p,s_q\), up to the forced \(d=2\) half-tie.
But any word made only by multiplicatively reusing divisors of \(N-1\)
has exactly the same possible prime support as \((N-1)^n\). Factoring
\((N-1)/2\) cannot improve P205 inside that grammar. A real gain must use
an additive divisor difference, signed centered residue, or carry selector.

P203 gives the matching integer boundary for the natural shifted-quotient
word bank. A residual prime is hit exactly when the actual gap ratio
\((q-p)B^{-1}\) lies in a small public projective rectangle. Universal
coverage reaches only the already affordable smooth-prime scale; large rough
progress requires a real theorem about the hidden integer gap ratios. The
current target is therefore precise: construct a public QP-bit word that
reduces one coprime residual to QP on every semiprime, or prove an inverse-QP
distribution law for an adaptive integer-word schedule. Centered carries
give an exact conditional decoder, but standard simultaneous approximation
only yields the generic \(B/U\) scale. Generic ring operations are no longer
the issue. The missing information is integer quotient/gap coupling.
`notes/Zhihu.md` supplies background only.

## Working claims

### C00 — divisor-to-complete-factorization reduction

**Status:** promoted as P04 in `PROVED.md`.

**Assumptions.** Write \(\ell(x)=\lceil\log_2(x+1)\rceil\). There is one uniform randomized machine `Split` such that, on every composite \(M\), an invocation using a fresh random tape halts almost surely, returns only a canonically encoded \(d\) with \(1<d<M\) and \(d\mid M\), and has expected bit cost at most a fixed nondecreasing polynomial \(Q(\ell(M))\), including randomness and all internal work. A uniform deterministic primality decider has worst-case bit cost at most a fixed nondecreasing polynomial \(A(\ell(M))\).

**Construction.** Maintain a stack initially containing \(N\). Pop \(M\), test primality, and append prime occurrences to a leaf list. On a composite, invoke `Split(M)`, verify \(1<d<M\) and exact divisibility, and push \(d,M/d\). Once the stack is empty, sort and group equal prime leaves. Under the assumption, the invalid-return branch is unreachable; if invalid candidates were permitted, verification alone would be insufficient without a separate polynomial expected waiting-time bound.

**Correctness and finite-call bound.** At every state boundary, the product of all stack and leaf occurrences is \(N\), and every occurrence is at least 2. If there are \(k\) occurrences, then \(2^k\le N\), so \(k\le\lfloor\log_2N\rfloor=n-1\). Initially \(k=1\); a prime move preserves \(k\), while each successful split raises it by one. Thus at most \(n-2\) splits occur, and at most \(2n-3\) tree nodes are created and primality-tested. This does not presuppose termination and counts repeated factors separately. At termination all leaves are certified prime and their product is \(N\), so grouping yields the unique complete factorization.

**Expected bit complexity.** Index the at most \(n-2\) possible split invocations and assign cost zero if an invocation is absent. Conditional on the full history before a reached call, its input is a fixed composite of at most \(n\) bits; fresh coins give conditional expected cost at most \(Q(n)\). The tower property and linearity of expectation therefore give total split cost at most \((n-2)Q(n)\), without requiring mutual independence between different calls. Primality tests cost at most \((2n-3)A(n)\). Validation, schoolbook exact division, stack/list operations, comparison sorting, grouping, exponent encoding, and output cost at most \(Kn^3\) for a fixed implementation constant \(K\). Hence

\[
\mathbb E[T(N)]\le (n-2)Q(n)+(2n-3)A(n)+Kn^3.
\]

There are finitely many reached randomized calls, each conditionally terminating almost surely, so their finite union terminates almost surely. Prime inputs invoke no split; prime powers and repeated factors become repeated leaves; even composites are covered by the all-composite premise.

**Verification result and remaining gap.** A proof-blind reconstruction recovered the corrected live-invariant, adaptive-expectation, bit-cost, and edge-case arguments. No qualifying `Split` procedure has been proved.

### C01 — exact linear square-class sketches cannot generically compress

**Status:** promoted as P01 in `PROVED.md`.

**Assumptions.** The sketch is homogeneous and linear over \(\mathbb F_2\), acts on arbitrary positive-integer square classes, and every vector in its kernel must be sound as an integer square-product relation.

**Claim and proof.** With notation as in X01 of `FAILED.md`, soundness gives \(\ker E\subseteq\ker V\), hence \(\operatorname{rank}E\ge\operatorname{rank}V\). Distinct prime inputs make the latter rank equal to the number of samples. Thus no dimension reduction can universally force a relation.

**Certificate for a truncated-moment failure.** In \(\mathbb F_7\), \(1+2=4+6=3\), while \(1\cdot2=2\) is a square and \(4\cdot6=3\) is a nonsquare.

**Hostile-audit result.** The core argument survived. The audit narrowed its scope: it does not cover lossy sketches followed by verification, Monte Carlo hashing with Las Vegas rejection, nonlinear/adaptive encodings, or special low-rank generators. The \(\mathbb F_7\) certificate concerns one moment only; sufficiently many moments can determine a multiset via Newton identities under the usual characteristic assumptions.

**Verification result and remaining gap.** A proof-blind reconstruction recovered the complete argument and its scope. F01 as a whole remains open because P01 does not address lossy verified sketches, nonlinear/adaptive encodings, or structured low-rank sample families.

### C02 — hidden modular-square-root reduction

**Status:** promoted as P02 in `PROVED.md`.

**Claim.** Let \(N=pq\) for distinct odd primes. Choose \(x\) uniformly in \((\mathbb Z/N\mathbb Z)^\times\), hide it from a routine, and give the routine only \((N,a=x^2)\). If it returns any \(y\) with \(y^2=a\pmod N\), then \(\gcd(x-y,N)\) is a proper factor with probability exactly \(1/2\), irrespective of the routine's root-selection distribution. Conditional on \(a\), the hidden \(x\) is uniform among four CRT roots; two are \(\pm y\), and the other two have mixed signs and split \(N\). For an odd integer with \(r\ge2\) distinct prime divisors the analogous success probability is \(1-2^{1-r}\ge1/2\); for a prime power it is zero. If a routine directly guarantees \(y\ne\pm x\), the gcd splits deterministically.

**Verification result and remaining gap.** A proof-blind reconstruction recovered the full CRT proof, including prime powers. No square-root routine meeting the independence and polynomial-time conditions is known; this is a reduction, not progress toward constructing `Split`.

### C03 — synchronized duplication-Lattès collision obstruction

**Status:** promoted as P03 in `PROVED.md`.

**Claim and certificate.** X02 in `FAILED.md` gives an explicit good-reduction curve over \(\mathbb Z/15\mathbb Z\) for which every affine point seed has identical local \(x\)-orbit collision threshold 4. Consequently all collision-discriminant gcds are trivial. A focused hostile audit independently checked the discriminant, point tables, duplication formula, unit denominators, exact period, and CRT product.

**Verification result and remaining gap.** A proof-blind reconstruction recovered all curve, group, denominator, and CRT steps. The hostile audit exhibited the same rational map separating at the non-curve residue seed \(x=2\), so P03 is strictly fixed-instance evidence and does not close F02 or even all seeds for this map.

### C04 — unequal local polynomial-gcd degrees expose a factor

**Status:** promoted as P05 in `PROVED.md`.

**Assumptions and claim.** Let \(N=pq\) for distinct primes, and let densely represented \(A,B\in(\mathbb Z/N\mathbb Z)[X]\) have degrees at most \(D\) and unit leading coefficients (monicity suffices). If

\[
d_p=\deg\gcd(A\bmod p,B\bmod p)\ne
d_q=\deg\gcd(A\bmod q,B\bmod q),
\]

then a nontrivial factor of \(N\) is recoverable deterministically in \(\operatorname{poly}(D,\log N)\) bit operations.

**Proof.** Swap the polynomials so their degrees are \(m\ge n\), and compute principal subresultant coefficients \(s_j\) for \(0\le j<n\) division-free modulo \(N\). If \(d_p\ne d_q\), then \(j=\min(d_p,d_q)<n\); over a field \(s_0=\cdots=s_{d_r-1}=0\) and \(s_{d_r}\ne0\). Thus \(s_j\) is zero in exactly one CRT component, and its gcd with \(N\) is a prime factor. Scanning all \(j\) avoids knowing the local degrees. Each \(s_j\) is a determinant of dimension at most \(2D\); Berkowitz computes it division-free over any commutative ring. Computing all coefficients conservatively uses \(O(D^5)\) ring operations, with reduction keeping residues at \(O(\log N)\) bits.

**Verification result and remaining gap.** A proof-blind reconstruction recovered the determinant definition, field lemma, extraction scan, and bit bound. F03 has not supplied \(A,B\) with the required mismatch without circular access to local characteristics or an exponentially unlikely probe.

### C05 — limits of naive cycle-type extraction

**Status:** promoted as P06–P08 in `PROVED.md`.

**Certificate and claim.** X03 records exact \(N=15\) and \(N=10\) witnesses for the naive global-exponent substitution. For uniformly random monic quadratics modulo \(N=pq\) with distinct odd primes, conditional on local squarefreeness, the split/irreducible bits are independent and fair, hence disagree with probability \(1/2\); their disagreement makes the unit discriminant's Jacobi symbol \(-1\). The resulting Jacobi-minus-one promise is Las Vegas randomized-polynomial-time equivalent to factoring this restricted semiprime class. This does not rule out richer coefficient invariants.

**Verification result and remaining gap.** A proof-blind reconstruction recovered both certificates, the exact discriminant distribution, both reduction directions and expected trials, and the linear-probe probability. No richer Galois invariant has been ruled out.

### C06 — blind Hasse–Witt substitution erases a local rank mismatch

**Status:** promoted as P09 in `PROVED.md`.

**Claim and certificate.** X04 gives a good-reduction elliptic curve over \(\mathbb Z/15\mathbb Z\) whose true one-dimensional Hasse–Witt matrices have ranks 0 and 1 modulo 3 and 5, while replacing the local characteristic by \(N\) in the coefficient formula produces zero in both components.

**Verification result and remaining gap.** Every arithmetic step and rank convention survived hostile audit, and a proof-blind reconstruction recovered the complete certificate. “Circularity” applies only to the factor-first CRT recipe; direct uniform computation of the correct combined entry remains a legitimate target. No genuinely global geometric operator has been addressed.

### C07 — the standard AKS coefficient scan need not localize

**Status:** promoted as P11 in `PROVED.md`.

**Claim and certificate.** X05 records a hard-regime distinct-prime semiprime for which the actual minimal-\(r\) AKS polynomial stage has no local pass/fail mismatch and no coefficient zero divisor across all standard shifts and all coefficients. The exact Frobenius reduction makes the finite scan feasible without changing the tested object.

**Verification result and remaining gap.** A fresh hostile implementation proved the factor/primality and minimal-\(r\) parameters, independently rescanned all positions with zero zeros in each field, and directly cross-checked localized versus exponent-\(N\) errors. A proof-blind reconstruction independently recovered the argument and reran all \(17{,}375{,}452\) local coefficient checks under a matching named source and timeout. Only the standard minimal-\(r\) pass/fail and individual coefficient scan is addressed; richer rank/minor or nonstandard group-algebra certificates remain open.

### C08 — scalar carry is not a sufficient factor-DP state

**Status:** promoted as P10 in `PROVED.md`.

**Claim and certificate.** X06 records an agent-invented bit-column mechanism absent from the source notes and an exact \(N=55\) collision in which a live and dead factor prefix have the same carry. The hostile audit verified the recurrence, carry bound, canonical-search failure, and qualified minimality. It corrected the exponential statement: \(2^{a-2}\) counts raw compatible low-prefix histories, and the exact restart probability applies only to globally uniform history sampling, not one-per-carry selection.

**Verification result and remaining gap.** A proof-blind reconstruction independently recovered the recurrence, carry bound, \(N=55\) collision, qualified first-column minimality, exact raw-history count, global-uniform restart probability, Bertrand family, and the \(N=187\) carry-class contrast. Other representative rules and richer polynomial-size carry/convolution summaries remain open; P10 supplies no state-complexity or factoring lower bound.

### C09 — natural multiplication-spectrum probes can have exponential support

**Status:** promoted as P12 in `PROVED.md`.

**Claim.** X07 gives an exact orbit-stratified characteristic polynomial and trace formula, plus an unconditional family of synchronized local orders \(\ell=2^{\Theta(n)}\). Every nonzero basis-point sequence has ordinary denominator degree \(\ell\) over every field; the exact integer trace sequence has degree \(\ell\) over characteristic zero and takes only the values 1 and \(N\). The family is uniformly enumerable in \(2^{O(n)}\) time, not known polynomial-time generable, and supplies bad fixed pairs rather than density over random bases.

**Verification result and remaining gap.** The exact orbit, trace, bit-cost, Linnik, synchronization, and characteristic-zero no-cancellation arguments survived after correcting the \(x=0\), orbit-state, effectivity, coefficient-field, query-model, and random-base scopes. A proof-blind reconstruction independently recovered the corrected theorem. P12 closes only the universal low-effective-frequency premise for standard point/trace probes and dense consecutive reconstruction. F07 and B4 remain open to sparse/adaptive, other-probe, and resampling mechanisms.

### C10 — natural automorphism-count interpolation hides a factor oracle

**Status:** promoted as P13 in `PROVED.md`.

**Claim.** X08 derives exact automorphism counts for dual numbers, a rank-3 square-zero algebra, odd quadratic monogenic algebras, and all fixed-rank étale algebras. The informative non-étale counts are \(\varphi(N)\)- or factoring-equivalent on semiprimes, while fixed-rank étale counts depend only on a bounded decomposition partition. Easy globally synchronized automorphisms need not separate CRT components.

**Verification result and remaining gap.** The audit confirmed every algebraic classification after correcting that the full rank-3 cubic—not its last linear factor—is increasing, noting quadratic count collisions, and bounding the étale count by \(d!\). A proof-blind reconstruction independently recovered the corrected theorem and its non-impossibility scope. P13 blocks only the tested natural magnitude-count mechanism: an explicit factor-free counting algorithm would itself solve the target problem and has not been ruled out.

### C11 — standard AKS annihilator ranks can agree everywhere

**Status:** promoted as P14 in `PROVED.md`.

**Claim.** X09 gives the analytic witness \(N=79403=271\cdot293\), standard \(r=269\), for which the local multiplication nullities of every standard AKS error \(H_a\), \(1\le a\le266\), are both zero. A degree-23 common obstruction polynomial cannot contain the nontrivial cyclotomic factors of degrees 268 and 67; the only linear-root exceptions occur at shifts outside the scan.

**Verification result and remaining gap.** The exact parameters, nullity–gcd identity, two local reductions, factor degrees, degree-23 obstruction, and exceptional shifts survived an independent proof and full local-residue A02 run. A proof-blind reconstruction recovered the complete corrected theorem. P14 applies only to the nullity/gcd-degree invariant: equal full ranks do not rule out every intermediate minor or elimination transcript. The discovery manifest's missing exact commands and R04's binary64 minimality claim remain disqualified. Nonstandard moduli, richer joint invariants, and asymptotic randomized-shift theorems remain open.

### C12 — scalar symmetric higher-residue carriers collapse to the diagonal

**Status:** promoted as P15 after hostile audit and proof-blind reconstruction.

**Claim.** X10 proves that if each individual multiplicative scalar label is factor-swap invariant, then every label factors through \(u_p+u_q\), so a nontrivial family has the anti-diagonal kernel. Fixed public unit twists, integer powers, transcript-internal adaptivity, multiplication/division, and label-only postselection preserve that quotient. An exact cubic example shows a canceled global phase with neither local phase canceled. For rational numerators coprime to the split prime, the fully Galois-symmetric odd-power residue-symbol product is trivial; a conventional nontrivial one-valued ideal-symbol evaluation must supply or compute an orientation, possibly implicitly.

**Verification result and remaining gap.** The hostile audit independently proved the rank-at-most-one statement, adaptive transcript factorization, corrected coprime Galois-product proposition, and exact \(N=91\) certificate. The proof-blind reconstruction recovered all of these and sharpened the boundary: a swap-invariant multiset can reveal the anti-diagonal up to sign, while a nonlinear symmetric scalar can reveal its magnitude. P15 therefore applies only to individually invariant scalar characters. It makes no hardness, noncanonicity, or one-root factoring inference about orientation. Vector/ring-valued, factor-oriented, additive/nonmultiplicative, externally informed, and other higher-residue carriers remain open.

### C13 — P14's full-rank witness is not a canonical-PSC witness

**Status:** promoted as P16 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** The closest route is X09/P14, which proves equality of the two local nullity/gcd-degree invariants for every standard shift. Canonical intermediate principal Sylvester determinants are materially different because they need not be invariant under the component-dependent cyclic substitutions used in P14's local reduction.

**Claim.** Fix the determinant convention in `experiments/F04_psckill/RESULT.md` for the principal coefficient \(D_j(P,Q)\) of \(P=X^{269}-1\) and the globally formed AKS error \(Q=H_a\). At \(N=79403=271\cdot293\), the first shift \(a=1\) has \(\deg H_1=268\) globally but local degrees 46 and 268. Direct defining matrices give no zero mismatch for \(0\le j\le46\), while

\[
D_{47}\equiv0\pmod{271},\qquad D_{47}\equiv173\pmod{293}.
\]

The factor-free global determinant is \(30352\pmod{79403}\), whose gcd with \(N\) is 271. Its matrix dimension is 443. Division-free determinant computation makes every such fixed coefficient polynomial-time computable when the AKS parameters are polynomial in \(\log N\).

**Verification result and remaining gap.** A hostile implementation literally reduced one saved global \(H_1\), directly checked all 269 determinant pairs, matched the PRS masks and padding formula, and independently discovered the first nontrivial gcd at \(j=47\) without factor literals or a supplied index. A proof-blind reconstruction then rebuilt the global scan from only the numerical statement, rediscovered the same first determinant separator, and independently reconstructed every local reduction. It also found the stronger limitation \([X^0]H_1=36585\) with gcd 271; 246 of the 269 raw coefficients already separate. An early preselected-index reconstruction probe was deleted without durable records, then restored and replayed; it is explicitly disqualified, and authoritative R01--R03 do not depend on it. P16 therefore only shows that P14 cannot refute PSC refinement. The decisive family-level test on P11's coefficient-hard witness remains under audit; any finite outcome will still lack a uniform separation theorem.

### C14 — cubic order-filtered automorphism search hides the split

**Status:** promoted as P17 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** The closest route is X08/P13, which blocks automorphism-**count** interpolation in natural fixed-degree families. C14 instead exploits a constant-probability mismatch in the **existence and construction** of order-2 or order-3 automorphisms of squarefree cubic algebras.

**Claim.** For a monic squarefree cubic over \(\mathbb F_\ell\), the factorization types \((111),(12),(3)\) have automorphism groups \(S_3,C_2,C_3\) and exact conditional probabilities

\[
\frac{\ell-2}{6\ell},\qquad \frac12,\qquad \frac{\ell+1}{3\ell}.
\]

For independently sampled reductions modulo distinct odd primes \(p,q\), order-3 existence differs with conditional probability \(1/2\), exactly when the unit discriminant has Jacobi symbol \(-1\). Raw random monic cubics reach this promise with probability \((p-1)(q-1)/(2pq)\), so rejection sampling costs at most \(15/4\) trials in expectation.

Under that promise, the \((12)\) component has no nonidentity cube-torsion automorphism. Hence every globally nonidentity \(\sigma\) with \(\sigma^3=1\), written \(\sigma(X)=a+bX+cX^2\), is identity in exactly that component, and one of

\[
\gcd(a,N),\qquad \gcd(b-1,N),\qquad \gcd(c,N)
\]

is a proper factor. Conversely, known factors construct such a map by using identity on the \((12)\) side, Frobenius on a \((3)\) side, or an interpolated root 3-cycle on a \((111)\) side, then CRT-lifting. Thus a uniform solver for this Jacobi-recognizable order-3 promise is Las Vegas polynomial-time equivalent to factoring distinct odd semiprimes. For an already-promised order-2 mismatch, any valid nonidentity involution similarly factors the instance and known factors construct one; constant mismatch density alone does not give a reduction to a promise-only solver because the order-2 predicate is not Jacobi-recognizable and off-promise behavior is uncontrolled.

**Verification, descent obstruction, and scope.** The hostile audit independently checked all equations, exact probabilities including characteristic 3, both gcd directions, reverse constructions, and the \(N=15,35\) certificates. A proof-blind reconstruction recovered those results and supplied a concrete order-2 failure: for \(N=15\), \(f=X^3+10X^2+6X+10\) has unit discriminant of Jacobi symbol \(-1\), but the involution \(X\mapsto2+3X+8X^2\) is nonidentity in both components and all three coefficient gcds are 1. The order-dividing-3 automorphism scheme has geometric rank 3 for every type: its rational-point counts are 3 for \((111),(3)\) but 1 for \((12)\). The order-dividing-2 locus has geometric rank 4 with rational-point counts 4, 2, 1. Invariants depending only on geometric nonemptiness or full geometric rank cannot localize the mismatch; no universal claim about every projection, resultant, or elimination invariant follows. The explicit promised certificate \(N=35,f=X^3+2\) has types \((12)/(3)\), with \(X\mapsto11X,16X\) exposing 5. This blocks only the natural cubic order-filter construction, not all B1 rings or canonization mechanisms.

### C15 — the coefficient-hard AKS witness is also canonical-PSC-hard

**Status:** promoted as P18 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** The closest results are P11, which makes every standard AKS error coefficient a unit, and C13, whose canonical PSC separates P14 only because a raw leading coefficient already separates. C15 tests the strictly richer canonical determinant family on P11's coefficient-hard witness.

**Degree-sequence lemma.** For polynomials \(F,G\) of degrees \(m>n\) over a field, let \(D_j\) use C13's fixed principal Sylvester determinant convention. If the ordinary Euclidean remainder degrees are

\[
m=d_0>d_1=n>d_2>\cdots>d_s=\deg\gcd(F,G),
\]

then

\[
D_j(F,G)\ne0
\quad\Longleftrightarrow\quad
j\in\{d_1,\ldots,d_s\}
\qquad(0\le j\le n).
\]

The hostile audit replaced the candidate's informal PRS block-scaling step by a direct kernel proof. The defining matrix is singular exactly when a nonzero bounded pair \((U,V)\) makes \(UF+VG\) have degree below \(j\). Extended-Euclidean cofactors supply such a pair inside every gap and below the gcd degree. At a remainder degree \(j=d_i\), the identity

\[
V R_i-T_i(UF+VG)=(VS_i-T_iU)F
\]

and the cofactor degree bounds force \((U,V)\) to be a polynomial multiple of \((S_i,T_i)\), which cannot lower \(R_i\)'s degree unless the pair is zero. This also covers positive gcd; at the top index \(D_n=\operatorname{lc}(G)^{m-n}\). An exhaustive stress test checked 17,556 defining determinants, including abnormal gaps and positive gcds, without a counterexample. Generic Sage `subresultants()` output is sparse on some inputs, so no proof relies on dense list indexing.

**Finite obstruction.** On

\[
N=20000000499999937
=100000007\cdot199999991,\qquad r=2953,
\]

for every standard shift \(1\le a\le2942\), the globally formed error has degree 2952 and unit coefficients, and both local Euclidean chains are exactly

\[
2953,2952,\ldots,1,0.
\]

The lemma therefore makes all \(2942\cdot2953=8{,}687{,}726\) canonical PSCs nonzero in each field, so every global PSC is a unit. The hostile A04 independently formed every global coefficient vector before local reduction, exhausted the entire range under a 900-second timeout, and checked 8,687,726 unit coefficients and 17,375,452 nonzero local determinant statuses. A05 matched all 2,942 fresh row hashes and both complete endpoint residue vectors against the discovery artifacts.

**Verification result and remaining gap.** The proof-blind reconstruction recovered the determinant theorem from the defining kernel map, exhaustively checked 231,494 small-field determinants, materialized all 8,687,726 global coefficients independently, verified both complete local chains, and reconciled all 17,375,452 determinant statuses. It used a separate direct-composite exponentiation spot audit and generic FLINT remainder checks; its incidental pre-source diagnostic, failed build launch, and self-referential manifest failure are disclosed and non-authoritative. P18 refutes universal localization only for the fixed canonical PSCs in the standard minimal-\(r\), standard-shift AKS scan. It does not cover arbitrary Sylvester minors, other elimination transcripts, nonstandard moduli/shifts, joint-shift column matroids, or other group-algebra elements, and finite exhaustion supplies no top-level factoring theorem.

### C16 — an exact multiplication-CVP reduction misses the tractable lattice classes

**Status:** promoted as P19 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** The closest route is F06/P10, which compresses low-to-high multiplication histories by scalar carry. C16 instead retains the full Boolean multiplication CSP, converts its affine integer solution set to a lattice, and asks for an exact closest vector.

**Verified reduction.** For each of \(O(n)\) feasible factor-bit length pairs, introduce factor bits, one-hot truth-table variables for every product bit pair, and binary carry digits. The affine equations enforce marginal consistency and every schoolbook multiplication column, including the essential final carry equation. With \(M=O(n^2)\) integer coordinates, the affine solution lattice and an integral particular solution are computable by polynomial-bit HNF/SNF. The all-\(1/2\) target has squared distance at least \(M/4\) from every integer point, with equality exactly at binary points. Hence a valid factor witness gives optimum \(M/4\), while an affine system with no binary witness has optimum at least \(M/4+2\). An exact search-CVP answer at the baseline decodes and verifies a factor; rational targets can be scaled to an integer target, and embedded- or full-rank conventions have polynomial-size normalizations. The relative gap is only \(1+\Theta(1/M)\).

**Verified structural boundary.** The exact constraint-incidence graph contains internally disjoint paths from every factor bit \(x_i\) to every factor bit \(y_j\), hence a subdivision of \(K_{a,b}\) and treewidth at least \(\min(a,b)\). The disjoint one-hot equations give codimension at least \(ab\). Dropping the truth-table consistency leaves a Toeplitz-like convolution system but loses Boolean rank one: for \(N=25\), the true outer-product matrix and a binary rank-3 matrix have identical anti-diagonal sums and carry sequence, so both attain the absolute half-target minimum. This only proves that not every relaxed closest matrix is itself a factor outer product. It does not rule out postprocessing that matrix—the displayed convolution polynomial actually retains the factor—or prove high width for every alternative rank-one encoding. The exact reduction therefore does not yet land in a class with a proved polynomial-time exact-CVP algorithm.

### C17 — elliptic collision synchronization and the surviving torus evaluator target

**Status:** promoted as P20 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** P03 synchronizes one fixed duplication-Lattès orbit. C17 analyzes the general cleared \(x\)-collision product of consecutive multiples, proves a universal good-curve obstruction on one balanced input, and isolates a different multiplicative dynamic whose separation theorem survives.

**Elliptic result.** Standard division-polynomial identities give

\[
C_m(P)=\prod_{1\le i<j\le m}\psi_{i+j}(P)\psi_{j-i}(P).
\]

For \(m\ge3\) and an affine point of order \(t\), this is zero exactly when \(t\le2m-1\), while every denominator through \(m\) is nonzero exactly when \(t>m\). At \(N=101\cdot103\) and \(m=101\), Hasse bounds every local point order by 122 or 124. Hence the product is zero modulo both factors for every curve good at both primes and every affine seed. The checked curve \(y^2=x^3+x+5\) and point \((5461,5889)\) have local orders 112 and 106, so this universal synchronization persists with all denominators through \(m\) nonzero.

**Torus result and gap.** For

\[
S_m(a)=\prod_{d=1}^{m-1}(1-a^d)^{m-d},
\]

local vanishing is exactly the order test \(\operatorname{ord}(a)\le m-1\). If \(S_m(a)\bmod N\) had a uniform exact evaluator polynomial in \(\log N+\log m\), scanning exact integer-root thresholds and sampling a residue primitive modulo the largest unknown prime would split every non-perfect-power composite with inverse-polynomial probability. Perfect-power handling and recursion then give complete Las Vegas factoring in expected \(O(n^3T(O(n))+\operatorname{poly}(n))\) bit operations. The known recurrence is linear in \(m\), and the cyclotomic identity merely redisplays \(m-1\) factors; the polylogarithmic evaluator remains missing. The hostile audit and proof-blind reconstruction verified this exact conditional boundary.

### C18 — natural torus-product compressions fail narrowly, not generally

**Status:** promoted as P21 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** C17/P20 makes a polylogarithmic evaluator for the weighted torus product sufficient for complete factoring. C18 tests concrete fixed-binomial, lcm, recursive-block, and equal-floor compression mechanisms without assuming a general circuit lower bound.

**Verified result.** A positive product \(\prod_h(1-a^{L_h})^{w_h}\) with the exact all-finite-field order-threshold zero set must literally contain every exponent in \((M/2,M]\), so it has at least \(\lceil M/2\rceil\) distinct exponents. The one-lcm version has an order-12 false positive at \(M=4\) over \(\mathbb F_{13}\). The exact shifted \(Q/T\) addition identities create \(M\) leaves only for their literal two-child evaluator. Equal-floor grouping has \(\Omega(\sqrt M)\) groups, and explicit characteristic-zero root-set polynomials have large degree; neither statement is a general circuit lower bound.

The unweighted and weighted products have identical prime support but not identical prime-power gcds: for \(N=875,a=631,m=3\), they yield gcds 175 and 875. Thus the unweighted product can be a better splitter but is not an evaluator for the weighted residue. P20's general evaluator gap remains open.

### C19 — exponent-\(N\) lifts erase input principal digits; fixed output digits are rare separators

**Status:** promoted as P22 after hostile audit and proof-blind reconstruction.

**Closest prior routes and material difference.** F07/P12 concerns scalar order-spectrum reconstruction, and F04 concerns Frobenius errors modulo \(N\). C19 instead tests Teichmüller and principal-adic information created by \(a\mapsto a^N\bmod N^2\).

**Verified structure.** The map kills the entire principal kernel \(\{1+kN\}\) and locally equals \(([a]_p^q,[a]_q^p)\). Its quotient power map is invertible exactly when \(\gcd(N,\operatorname{lcm}(p-1,q-1))=1\), but the displayed inverse is factor-aware. The identity \(A^{N+1}=A^{p+q}\) on the image is only an order congruence. Consecutive image iterates have no valuation-one local differences, and the additive carrier has an exact valuation-category formula, including the corrected exceptional twin \((3,5)\).

For canonical high digits \(H_r\), every odd balanced pair \(p<q<2p\), uniform unit base, and fixed nonadaptive set of \(K\) iterates satisfies

\[
\Pr(\exists r:\ 1<\gcd(H_r,N)<N)\le\frac{3K}{p-1}.
\]

Thus \(K=\operatorname{poly}(\log N)\) has exponentially small success on the infinite balanced family supplied by Bertrand. Adaptive/engineered nonuniform bases, cross-base constructions, and other \(N^2\)-adic observables remain open.

### C20 — a small affine base does not give a small explicit action

**Status:** promoted as P23 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** F07/P12 blocks natural dense order-spectrum reconstructions. C20 instead tests the B7 affine/nonabelian lift through faithful permutation degree and ordinary stabilizer chains.

**Verified theorem.** For \(N=\prod\ell^e\ge2\),

\[
\mu\!\left(\operatorname{AGL}_1(\mathbb Z/N\mathbb Z)\right)
=\sum_{\ell^e\parallel N}\ell^e.
\]

The cyclic translation gives the lower bound, and factor-aware disjoint CRT actions give the upper bound. Thus a balanced semiprime needs explicit degree \(p+q=2^{\Theta(\log N)}\), even though the natural local affine action has base size 2 for odd primes. Ordinary explicit-permutation stabilizer chains remain exponential-size in the input bit length.

The \(2\times2\) matrix action remains succinct. For \(M_a=\operatorname{diag}(a,1)\), however, the literal-vector stabilizer of \((1,0)^T\) is exactly \(\operatorname{ord}_N(a)\mathbb Z\). A materially new retry needs a factor-sufficient quotient, a justified succinct-action algorithm, or a different matrix/module stabilizer; none is ruled out by the degree theorem.

### C21 — joint AKS prefix invariants fail, but a full-column separator survives

**Status:** promoted as P24 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** P18 exhausts the canonical principal Sylvester coefficients of each standard AKS error on the coefficient-hard P11 input. C21 instead stacks all standard errors and tests dependence across shifts. It distinguishes the row matroid and polynomial-size prefix summaries from the exponentially richer full column matroid.

**Verified boundary.** On P11, the first 2942 columns form a basis in both local fields. Hence both row matroids are free, all row-prefix and full-row column-prefix ranks agree, both lexicographic bases are the same, the canonical base determinant is a unit, and every raw matrix entry is a unit. These joint summaries therefore fail. However, removing base columns \(423,2336\) and adding global columns \(2944,2948\) gives local determinants \(15564403\) and \(0\); the CRT determinant has gcd \(199999991\) with \(N\). An exhaustive exact scan found no one-tail mismatch and exactly two two-tail mismatches.

**Verification result and remaining gap.** The hostile audit independently rebuilt and hashed the global matrices, solved both local systems, scanned all 237,941,605 two-tail exchanges, directly checked the separator, and audited every retained artifact. A proof-blind reconstruction recovered the analytic P14 ranks, the P11 row/prefix obstruction, the exchange identity and sign, all finite counts, and a division-free polynomial-bit evaluation bound, while disclosing every failed or interrupted run. The surviving determinant is globally computable once specified, but its discovery used the factors. No factor-free uniform selector, mismatch theorem, or all-input factoring algorithm follows.

### C22 — uniform Hurwitz orientations miss the noncommutative gcd birthday scale

**Status:** promoted as P25 after hostile audit and proof-blind reconstruction.

**Closest prior routes and material difference.** F03 and F09 use commutative polynomial or cyclotomic ideal localization. C22 uses the two-sided Euclidean Hurwitz order, where a greatest common one-sided divisor can return norm \(p\) or \(q\) directly rather than merely producing a public residue for a final integer gcd.

**Verified theorem.** For \(N=pq\) with distinct odd primes, the shell \(S_N\) has \(24(p+1)(q+1)\) elements and uniform row- or image-orientation pairs in \(\mathbf P^1(\mathbb F_p)\times\mathbf P^1(\mathbb F_q)\). Right gcds are controlled by row equality and left gcds by image equality. Their exact norm law is \((pq,q,p,1)/((p+1)(q+1))\) on \((1,p,q,N)\), so proper success is \((p+q)/((p+1)(q+1))\). All-pairs testing on \(K\) samples has probability \(O(K^2/\sqrt N)\) on balanced inputs and therefore needs the \(N^{1/4}\) birthday scale.

**Verification result and remaining gap.** The hostile audit corrected normalization, handedness, relative transform order, multiplier-norm contamination, local-versus-integral ideal scope, and the exact sampling quantifiers, then passed a complete \(N=15\) enumeration and symbolic edge checks. The proof-blind reconstruction independently rebuilt the ideal-orbit proof and every corrected core claim. Exact-uniform sampling is only a granted premise, not an algorithm. The theorem leaves open precisely the useful next branch: a factor-free nonuniform/adaptive sampler with asymmetric local collision energy, or a non-collision quaternion invariant.

### C23 — bounded scaled Fermat and literal trace wheels do not manufacture a fine metric hint

**Status:** promoted as P26 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** F11 encodes an exact factor witness in a lattice. C23 instead asks whether bare \(N=pq\) can manufacture an additive polynomial-width approximation to \(p+q\), from which discriminant square-testing factors deterministically.

**Verified boundary.** Every fixed polynomial numerical multiplier range and Fermat-step cap fails on an infinite balanced family with \(q/p\) inverse-polylogarithmically close to \(\sqrt2\). Literal CRT square-residue wheels have \(|W_\ell|=(\ell+(N/\ell))/2\), so materializing states, uniformly sampling them, or explicitly visiting interval lifts costs \(L^{1-o(1)}\) for trace-interval length \(L=\Theta(\sqrt N)\) in the appropriate modulus regimes.

**Verification result and remaining gap.** The hostile audit and blind reconstruction verified all allocations, parity cases, quantifiers, and wheel regimes, and supplied counterexamples to broader interpretations. Exponentially large encoded multipliers, compressed/adaptive character solvers, interval-conditioned distributions, and other metric observables remain open.

### C24 — exact-iid imaginary-class ambiguity has a class-number barrier

**Status:** promoted as P27 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** F14 uses noncommutative one-sided quaternion gcds. C24 uses canonical reduced imaginary-quadratic forms, whose useful ambiguous coefficients reveal the factors directly.

**Verified boundary.** The ambiguous classes for the fundamental discriminants \(-N\) and \(-4N\) are completely classified, with exactly half useful. For class number \(h\) and \(t=|G[2]|\in\{2,4\}\), direct exact-uniform success is \(t/(2h)\), and square collisions have exact occupancy law and scale \(\Theta(\sqrt{h/t})\). Siegel's bound makes polynomial sampling exponentially sparse. Public genus labels improve mass only by a constant; ordinary inverse collisions retain only a bounded \(4\)-torsion channel.

**Verification result and remaining gap.** The hostile audit corrected the public even-discriminant genus character, inverse-orbit and powering claims, and split-prime root count; a proof-blind reconstruction recovered the corrected theorem. Designed nonuniform split-prime walks, computable order/exponent surrogates, real infrastructure, and other composition failures remain open.

### C25 — the Lipschitz slice stays uniform, but one Hurwitz unit orbit has a stabilizer separator

**Status:** promoted as P28 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** P25 grants iid uniform full-shell samples. C25 tests the strict integral-coordinate slice, an explicit factor-free sampler, adaptive fixed transform menus, and finally correlated samples from one right-unit orbit.

**Verified boundary.** Every left- and right-unit orbit of odd norm contains exactly eight integral elements, so the Lipschitz slice is still uniform on each row quotient and separately on each image quotient. Its exact coordinate-triple sampler needs \(\Theta(\sqrt N)\) trials on balanced semiprimes. A polynomial fixed menu remains sparse even under joint/stateful selection. For fixed \(\alpha\), however, two random actual right units have exact proper-gcd probability

\[
|H_p(\alpha)\triangle H_q(\alpha)|/12.
\]

This gives conditional expected-polynomial direct prime extraction whenever the stabilizers differ, but the probability is \(1/4\) at \(N=15,\alpha=1+i+2j+3k\) and \(0\) at \(N=39,\alpha=1+i+j+6k\).

**Verification result and remaining gap.** The hostile audit corrected selector quantifiers, actual-versus-projective unit sampling, characteristic-\(3\) language, scan scope, and random-bit cost; the proof-blind reconstruction recovered the entire corrected theorem and both certificates. No factor-free expected-polynomial sampler is known to reach the mismatch stratum with inverse-polynomial probability. Mixed-handed four-square-finder output, sample-combining maps, and non-collision invariants remain open.

### C26 — the exact level-two Eisenstein metric oracle is just the divisor-sum trace

**Status:** promoted as P29 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** P26 studies explicit numerical searches for an Archimedean approximation to \(p+q\). C26 instead asks for a fixed modular-form coefficient at the binary-encoded index \(N\), including exact, sufficiently large modular, and known additive-polynomial interfaces.

**Verified boundary.** The fixed form

\[
2E_2(2z)-E_2(z)=1+24\sum_{m\ge1}\sigma_1(m_{\rm odd})q^m
\]

lies in \(M_2(\Gamma_0(2))\). For distinct odd \(N=pq\), its arithmetic Hecke coefficient is \(b_N=N+p+q+1\). Exact \(b_N\), \(24b_N\) modulo a caller-supplied \(O(\log N)\)-bit modulus, or a known additive polynomial approximation therefore recovers \(p+q\) and factors by the integer discriminant in deterministic polynomial bit complexity. Conversely, the factors compute every such output.

**Verification result and remaining gap.** The hostile audit checked modularity at both cusps, normalization, decoding inequalities, promise scope, and bit lengths; the proof-blind reconstruction independently recovered the complete proof. The result constructs no evaluator and is false as stated for repeated or even semiprimes. Coarse or fixed-small-modulus data, cusp forms, twists, other levels and weights, Brandt or modular-symbol invariants, and any genuinely different metric information remain open.

### C27 — an unconditional four-square finder remains diffuse in both matched hands

**Status:** promoted as P30 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** P25 assumes exact-uniform full-shell samples and P28 studies the Lipschitz slice. C27 analyzes the actual unconditional Pollack--Treviño finder. Its outputs are not asserted to be shell-uniform; instead, the accepted residual conic maps exactly and bijectively to the supported projective row and image lines.

**Verified boundary.** Conditional on the residual and fresh completion data, both local lines are uniform on \(\mathcal S_r=\{[u:v]:u^2+v^2\ne0\}\), of size \(r-(-1/r)\). A left-normalized gcrd inherits the row, and a separately computed right-normalized gcld inherits the image. Polynomially many matched-handed pair tests, all fixed unit translates, and the matched within-output stabilizer test therefore have exponentially small success on an infinite balanced family. The exact auxiliary modulus \(M=nP/\gcd(n,P)\), primitivity argument, rejection distribution, and expected bit/random-bit complexity all survive audit and blind reconstruction.

**Verification result and remaining gap.** The theorem deliberately does not identify the image of a gcrd output or the row of a gcld output. Mixed-handed tests, nonlinear combinations of multiple samples, fibre-point-dependent completions, even or repeated-prime norms, and non-collision invariants remain open. This is also the precise place to test whether “many lucky relations” means only a union of rare events, already blocked, or a genuinely joint decoder that accumulates partial constraints.

### C28 — mixed-handed independent tickets are sparse, but their same-source graph is exact

**Status:** promoted as P31 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** C27 controls matched hands and local marginals. C28 proves conditional product-uniformity across the two CRT primes, permits arbitrary transcript-dependent one-sided normalization, covers every independent comparison hand and product order, and then retains the exact row--image dependence within one raw output.

**Verified boundary.** Every wrong orientation of an arbitrarily normalized one-sided divisor has local atom at most

\[
\frac{12(r'+1)}{s_rs_{r'}}\le\frac{27}{r+1}.
\]

Polynomial independent calls, fixed projective menus, all pairwise one-sided gcds, both product orders, and wrong-hand unit stabilizers are therefore exponentially sparse on balanced semiprimes. For one source, however,

\[
\operatorname{im}_r\beta=J_{C,r}\operatorname{row}_r\beta,
\]

and both mixed hands have exact split-free coefficient criteria. A complete \(N=91\) certificate makes all twelve coefficients in both menus coprime to \(91\). The orbit blocks \(Q_tM_2\) pool to dimension two iff their hidden lines coincide and dimension four otherwise.

**Verification result and remaining gap.** Audit and blind reconstruction recovered every constant, hand, exceptional point, factorization, and quantifier. The result closes only unions of independent tickets and fixed dimension-only subset profiles. Adaptive/implicit subsets, exact row spaces, coefficient/pivot/minor systems, resultants, noncommutative products, spectral statistics, nonlinear joint decoders, and fibre-point bias remain open.

### C29 — a two-form real-infrastructure endpoint cycle need not localize a factor

**Status:** promoted as P32 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** P27 treats unordered imaginary-class ambiguity. C29 studies an ordered real principal infrastructure, its exact metric, and the SQUFOF proper-square localization rule.

**Verified boundary.** For \(a=6t+1\), \(N=a^2+2\), and \(\Delta=4N\),

\[
\sqrt N=[a;\overline{a,2a}],
\qquad
(1,2a,-2)\xleftrightarrow{\rho}(-2,2a,1).
\]

All endpoint coefficients are coprime to \(N\); the only positive right square \(1\) is improper period completion. The two endpoints lie at \(0,R/2\), with fundamental unit \((N-1)+a\sqrt N\) and \(R=\Theta(\log N)\). Exact reduction corrections, gap/precision bounds, compact encodings, and the Terr upper bound were reconstructed with their proper scope.

**Verification result and remaining gap.** The family has the public factor \(3\), admits repeated factors, and has small regulator. It obstructs only unmultiplied endpoint-only coefficient gcd/proper-square extraction. Multipliers, other discriminants, intermediate transcripts, relative generators, failure events, and joint metric decoders remain open; no infrastructure lower bound is claimed.

### C30 — fine two-isogeny orientation is the factor, while coarse orientation is missing

**Status:** promoted as P33 after hostile audit and proof-blind reconstruction.

**Closest prior route and material difference.** P09 studies a blindly substituted Frobenius rank. C30 asks instead for a canonical isogeny neighbor and separates the coarse modular-polynomial target from the fine descended kernel.

**Verified boundary.** At \(j=1728\),

\[
\Phi_2(1728,Y)=(Y-1728)(Y-287496)^2.
\]

The double coarse root can be rational even when neither nonpublic two-torsion kernel descends from the fixed twist. On a distinct odd semiprime with \(A\) a unit and \(\left(\frac{-A}{N}\right)=-1\), an exposed selective rank-two kernel is exactly

\[
u(u^2+A)\equiv0\pmod N,
\qquad u\not\equiv0\pmod N,
\]

and its two complementary gcds are \(p,q\). Random \(A\) reaches the promise with probability at least \(4/15\); known factors construct the section by a local square root and CRT.

**Verification result and remaining gap.** The hostile audit and blind reconstruction checked the modular-polynomial constants, descent distinction, subgroup-scheme equivalence, exact probability and bit complexity, \(N=143,A=1,u=44\) certificate, global-power synchronization, and narrow irreducibility/discriminant/CM bounds. No fine selector was constructed. \(N\)-dependent, higher-CM-with-embeddings, vertical, and supersingular mechanisms remain open.

### C31 — exponentially many Boolean relations have constant pooled mass but no polylogarithmic evaluator

**Status:** promoted as P34 after a corrected hostile audit and proof-blind
reconstruction.

**Closest prior route and material difference.** P21 blocks several literal
compressions of a torus threshold product. C31 studies the product of every
nonempty Boolean subset sum. It is also F02-adjacent, but its local event is a
genuine constant-mass pool of pairwise-independent tickets rather than a
polynomial union of rare comparisons. Optional Hurwitz provenance is
dispensable.

**Verified boundary.** On \(N=pq\) with
\(53\le p<q<2p\), choose
\(K=\lfloor\log_2\lfloor\sqrt N\rfloor\rfloor-3\) uniform residues and
multiply their \(2^K-1\) nonempty subset sums. The product vanishes in
exactly one field component with probability at least

\[
\frac{2}{32\sqrt2+1}
\left(1-\frac{\sqrt2}{8}\right).
\]

Therefore a polylogarithmic exact evaluator would give a constant-trial
Las Vegas splitter on the promise. The exact meet-in-the-middle identity,
monic product/remainder trees, and carry-safe Kronecker multiplication give
only \(N^{1/4+o(1)}\) bit time and space; direct Gray-code evaluation gives
\(N^{1/2+o(1)}\) bit time and polynomial space.

**Verification result and remaining gap.** The hostile audit and blind
reconstruction checked the floors, probability, componentwise-OR scope,
resultant signs, composite-ring division, bit complexity, cube-tree identity,
and formal degree limitations. No polynomial evaluator, general circuit
lower bound, unbalanced/repeated-factor theorem, recursion, or all-input
factoring algorithm is known.

### C32 — public zero-syndrome lattices lose the proposed high-dimensional amortization

**Status:** promoted as P35 after a corrected hostile re-audit and proof-blind
reconstruction.

**Closest prior route and material difference.** P19 is an exact
multiplication-CVP reduction whose tractable-class landing fails. P30/P31
control pairwise projective events. C32 instead analyzes the hidden-modulus
Construction-A, coefficient/Gram, Hurwitz block, and graph lattices proposed
for jointly decoding many local relations.

**Verified boundary.** For an integer map \(A\), the public modular kernel is
exactly \(K_p(A)\cap K_q(A)\). Unequal local ranks factor immediately through
SNF minors. In the equal-rank case, the desired symmetric difference is not a
lattice, fixed-output concatenation adds a primitive exact rational kernel,
and quotienting leaves rank at most four for one quaternion output. CVP
subtraction in the public intersection preserves both local syndromes.

For norm-\(N\) Hurwitz multiplication, the intrinsic local ideals have exact
shortest lengths \(\sqrt p\) and \(\sqrt q\), while their public intersection
has exact shortest length \(\sqrt N\) and is a fixed-shape similarity. Direct
sums do not improve these scales. The displayed unshifted graph regime below
local residual length \(r\) selects only the public intersection.

**Verification result and remaining gap.** The corrected audit and blind
reconstruction verified all determinant, projection, handedness, minimum,
CVP, graph, and bit-complexity claims. They explicitly leave open the public
output lattice \(A\mathbb Z^d+N\mathbb Z^t\), the scaled dual
\(N\mathbb Z^d+A^{\mathsf T}\mathbb Z^t\), a faithful fixed-rank metric
decoder, biased affine targets, and nonlinear combinations. No every-input
sampler or factor-extraction law is known.

### C33 — exact pinned multiplication counts factor directly, while the
separated COPY--AND matchgate landing fails

**Status:** promoted as P36 after a corrected hostile re-audit and
proof-blind reconstruction.

**Closest prior route and material difference.** P10 compresses multiplication
histories by scalar carry, P19 encodes them as exact CVP, and P29 studies an
already factor-sufficient trace oracle. C33 instead uses the complete Boolean
multiplication witness as a tensor-network count and recovers a factor by
prefix self-reduction rather than by a terminal gcd.

**Verified conditional reduction.** If every original and
\(x\)-prefix-pinned multiplication-witness network can be contracted exactly
in bit time polynomial in \(\log N\), subtract the two public witnesses
\(x=1,N\). The remaining positive counts partition at every next bit, so a
nontrivial divisor is recovered directly. Exact division, deterministic
primality testing, and recursion give complete deterministic polynomial-time
factorization for every input.

**Verified local obstruction.** Ordinary contraction requires
\((T^{-1})^{\mathsf T}\) on the endpoint opposite \(T\). Every invertible
basis making ternary COPY parity-pure gives an alternating dual column ratio
\(r(-1)^b\). With independent input-role bases and arbitrary output action,
the transformed AND parity equations force both \(x=y\) and \(x=-y\), or
force \(xy=0\) in a zero-coordinate case. An explicit padded bipartite
ternary-fanout construction realizes the directly adjacent leaf-COPY/AND
pair without changing witness multiplicity.

**Verification result and remaining gap.** A fresh hostile re-audit checked
the corrected transpose-dual convention, all parity and topology-scope cases,
the exact witness count, recursion, and bit complexity. A proof-blind
reconstruction recovered the theorem through an independent slice-pencil
argument. This closes only the separated common-role-basis matchgate route.
Fused cells, high-arity equality, edge-dependent gauges, other Pfaffian
identities, and non-matchgate exact contractions remain open.

### C34 — output/dual faithful quotients have only public scale

**Status:** promoted as P37 after a corrected hostile re-audit and a fresh
proof-blind reconstruction.

**Closest prior route and material difference.** C32/P35 closes the public
zero-syndrome and shared-output Gram constructions but leaves the output
lattice, scaled dual, and their metric quotients open. C34 treats those
objects and the explicit fixed-completion cyclic tail.

**Verified boundary.** For any integer matrix, Smith form either exposes a
proper factor or leaves \(1\)- and \(N\)-gcd blocks. The common primitive
\(1\)-block is public; orthogonal projection off it makes each output and
transpose-side local lattice exactly \(p\), \(q\), or \(N\) times one
public projected ambient lattice. This does not orthogonally split the
original full lattice.

For a shared-completion batch satisfying the maximal-minor surjectivity
criterion, the nontrivial output tail is cyclic. On its unfactored branch it
is \(\mathbb ZC_0+N\mathbb ZD\), its faithful quotient is rank one, and
its scaled rank-two dual is only a rotation. Coordinate-gcd extraction from
\(aC_0+NbD\) is exactly the public scalar ticket \(\gcd(N,a)\).
Uniform cyclic targets and marginally uniform completion lines give only
\(1/p+1/q-2/N\) and \(O(1/p+1/q)\) one-factor events.

**Verification result and remaining gap.** The first blind reconstruction
correctly rejected an accidentally over-strengthened Smith statement; the
failed attempt is preserved. A new blind agent reconstructed the exact
\(1\)-/\(N\)-block theorem and every cyclic identity independently. Biased
completions/targets, nonlinear combinations, and metric coordinate-gcd
selection in the original full lattice remain open in general. P39/C36 closes
only the independent uniform fixed-local-rank subspace model.

### C35 — positive matching sampling is sufficient, but direct deletion signatures are subcubes

**Status:** promoted as P38 after four hostile audit rounds and a strict
proof-blind reconstruction.

**Closest prior route and material difference.** C33/P36 uses exact
contraction and prefix self-reduction. C35 instead asks for a positive
bipartite graph whose individual almost-uniformly sampled matchings decode
directly to ordered divisor witnesses with equal multiplicity.

**Verified conditional reduction.** Under that graph hypothesis, uniform
matchings push forward to uniform positive divisors. Every composite has at
least one third nontrivial ordered-divisor mass; total-variation error
\(1/12\) leaves success at least \(1/4\). A total rational JSV
implementation, exact fair-bit coins, bounded terminal conditioning,
all-estimate failure accounting, deterministic verification, primality
testing, and a recursion tree of at most \(2n-1\) nodes give a complete
all-input Las Vegas expected-polynomial factoring algorithm. No such graph
has been constructed.

**Verified local obstruction.** Perfect-matching deletion supports have fixed
parity, bipartite charge, and symmetric exchange. Exact nonempty one-hot
dual-rail support is therefore a family of matroid bases and its logical
relation is a subcube. Direct single-rail and exact one-hot dual-rail
COPY\(_3\), AND\(_3\), full addition, and the fused multiplier/addition
cell all fail. Aggregate cancellation/modular/interpolation permanent
reductions do not give the required positive individual-matching semantics.

**Remaining gap.** Closed internal-edge decoding, off-code filtering, block
codes, assignment-dependent auxiliary states, global multiplicity balancing,
and one globally interleaved multiplication graph remain open. F30 now tests
the first clean composition mechanism without transferring P38 beyond
terminal signatures.

### C36 — independent uniform full-lattice relations do not win exact SVP

**Status:** promoted as P39 after a corrected hostile audit, clean re-audit,
and strict proof-blind reconstruction.

**Closest prior route and material difference.** C32/P35 closes the public
zero-syndrome relation lattice, and C34/P37 closes projected output/dual scale
and the fixed-completion cyclic tail. C36 keeps the original full
nonorthogonally coupled lattice but specializes its hidden local codes to
independent uniform fixed-rank subspaces.

**Verified boundary.** The full CRT lattice has determinant \(N^{m-u}\);
its proper-factor coordinate slices are exactly \(pL_q\) and \(qL_p\).
Minkowski and the public vectors \(Ne_i\) bound every shortest vector by
\(\min(R_M,N)\). Each divided candidate pays the exact uniform-code
incidence probability, and a tie-independent eligible-point union bound
controls all shortest vectors simultaneously.

For fixed local rank \(u\), balance constant \(\kappa\), and dimension
exponent \(K\), uniformly over

\[
p\le q\le\kappa p,\qquad u<m\le(\log N)^K,
\]

the probability that any shortest vector has proper coordinate gcd is
\(N^{-u/2+o(1)}\). The small range \(u<m<2u\) is eventually empty by
the exact nonzero lattice-point count; the cube relaxation itself is not
claimed sharp there. The two Minkowski/public-radius branches handle every
remaining dimension and every shortest-vector tie.

**Remaining gap.** This is neither an SVP hardness theorem nor an arithmetic
source theorem. Biased/dependent local subspaces, growing local rank, affine
targets, CVP/LLL, nonshortest observables, and nonlinear decoding remain
open. A retry must specify and analyze one of those mechanisms rather than
reuse independent uniform fixed-rank exact SVP.

### C37 — low-degree product pooling is local OR/CRT XOR, not joint decoding

**Status:** promoted as P40 after the amended theorem passed a clean hostile
audit and a fresh context-free proof-blind reconstruction.

**Closest prior route and material difference.** P08/P31 bound linear or
enumerated equality tickets, while P35/P39 treat relation lattices. C37 lets
every polynomial depend on every coordinate of one full-affine CRT batch and
allows all zero tests to share variables before one terminal product gcd.

**Verified boundary.** For nonzero local formal reductions, the exact
proper-gcd law is \(\alpha_p+\alpha_q-2\alpha_p\alpha_q\), with
\(\alpha_r\le\min(1,\Delta_r/r)\) at the actual reduced degree. The sharp
box envelope is \(\max\{u_p,u_q,u_p+u_q-2u_pu_q\}\). Random coefficients
must be conditioned on, adaptive use requires a fresh batch, and local formal
zeros obey the four-case content table. Formal zero functions and
characteristic-scale degree are not silently treated as low degree.

**Remaining gap.** A product only ORs rare zeros locally. C37 does not touch
a decoder that combines typical nonzero values, a nonuniform or metric
source, or a succinct characteristic-scale product with a proved evaluator
and XOR mass. Sparse/circuit size is not actual degree.

### C38 — quadratic Fourier energy pools constant factor mass

**Status:** promoted as P41 after a strengthened hostile re-audit and a fresh
context-free proof-blind reconstruction.

**Closest prior route and material difference.** P12 studies order-spectrum
moment reconstruction. C38 instead takes the additive Fourier energy of the
square pushforward and obtains an explicit positive target distribution.

**Verified boundary.** For odd \(N\), the energy is exactly
\(N\gcd(k,N)\), and its normalized law has factor-revealing mass at least
\(2/7\) on every odd composite. An explicit all-input sampler within TV
\(1/28\), with almost-sure termination and expected polynomial bit/fair-bit
cost, would give complete all-input Las Vegas factoring.

Uniform rejection costs \(\Theta(N)\) proposals and direct uniform-gcd
discovery \(\Theta(\sqrt N)\) on balanced semiprimes. The lazy
uniform-proposal Metropolis chain has exact eigenvalue
\(1-S(N)/(2N^2)\), hence worst-start \(\Omega(N)\) semiprime mixing; a
zero-mass-corrected initializer with negligible factor-class mass still has
an \(\Omega(\sqrt N)\) hitting obstruction.

**Remaining gap.** No factor-free polynomial-time sampler is known. F33
has now become P43, promoting the uniform zero-product lift and closing its
exact coordinate heat bath. F34 has become P44, closing factor-free explicit
algebra-automorphism proposals. F35 tests low-degree finite-set bijections.
Augmented, nonlocal, nonreversible, positive-matching, and other direct
samplers remain open.

### C39 — closed matching logic survives, but its clean occurrence wire fails

**Status:** promoted as P42 after a clean hostile audit and a fresh
context-free proof-blind reconstruction.

**Closest prior route and material difference.** C35/P38 closes direct
terminal-deletion encodings. C39 reads ordinary internal edges of completed
matchings and therefore tests a survivor that P38 explicitly left open.

**Verified boundary.** Two six-vertex bipartite graphs realize AND and
COPY\(_3\) exactly from marked internal-edge occupancies, with one matching
per truth word. A universal connector equating two occurrence edges on four
distinct ports would need raw deletion support
\(\{\varnothing,B\}\). Matching symmetric exchange forces a feasible
two-port set, even with arbitrary auxiliary vertices and nonnegative weights.

**Remaining gap.** The theorem closes only context-independent clean
composition. Contextual suppression of off-code states, projected auxiliary
states, block/heterogeneous codes, fused or identified ports, global
multiplicity balancing, and one multiplication-specific interleaved graph
remain open.

### C40 — quadratic energy has an exact positive lift, but coordinate heat bath is cold-start slow

**Status:** promoted as P43 after two corrected historical failures, a clean
whole-artifact hostile re-audit, and a fresh context-free proof-blind
reconstruction.

**Closest prior route and material difference.** C38/P41 identifies the
one-coordinate quadratic-energy target but leaves its sampler abstract. C40
lifts the target to the uniform positive relation \(kx=0\), allows both
coordinates to be inspected, and tests the exact random-scan conditional
sampler on that relation.

**Verified boundary.** The uniform zero-product marginal is
\(\gcd(k,N)/S(N)\), and the pair has proper-coordinate-gcd mass at least
\(1/3\) on every odd composite. A uniform TV-\(1/12\) explicit pair sampler
therefore gives complete all-input Las Vegas factoring. A fully uniform
equal-positive-fibre matching graph and efficient short-output decoder would
suffice, but no such graph is known.

For a semiprime, exact local types are \(H,V,O\); useful pairs are precisely
unequal CRT types, including cases with a local origin. The exact
one-coordinate heat bath is implementable by fair-bit annihilator sampling,
yet from \((1,0)\) its hitting expectation is \(\Omega(N/(p+q))\) and its
worst-start mixing time is at least
\(\lfloor N/(8(p+q-2))\rfloor\). Both are
\(\Omega(\sqrt N)\) on balanced families.

**Remaining gap.** Efficient warm starts, block/nonlocal/nonreversible or
augmented kernels, positive matching encodings, and direct spectral samplers
remain open. Prime-power geometry has valuation strata and is not collapsed
to an axis label.

### C41 — zero-product scheme automorphisms give a factor-or-invariant dichotomy

**Status:** promoted as P44 after an amendment-verified hostile audit and a
fresh context-free proof-blind reconstruction.

**Closest prior route and material difference.** C40 studies local
conditional updates. C41 allows arbitrary nonlocal adaptive compositions,
but restricts each move to an explicit automorphism of the nodal coordinate
algebra.

**Verified boundary.** Over a field every node automorphism is a unit
scaling with a preserve/swap axis bit. Over
\(\mathbb Z/pq\mathbb Z\), differing local bits make an intrinsic first-jet
entry a selective zero divisor, which is extracted from a division-free
circuit and gcd-factored in polynomial time. If no entry factors, the
orientations synchronize and the exact factor-free region is invariant
pathwise under every adaptive mixture. Uniform zero-product pairs put more
than one-half mass outside that region.

**Remaining gap.** P45 now closes the low-formal-degree finite-set
permutation escape. Characteristic-scale permutations, endomorphisms,
noninvertible/stochastic or auxiliary/lifted kernels, accessible piecewise or
rational models, useful warm starts, and nonsquarefree bases remain open.

### C42 — low-degree finite-set bijections give a quantitative factor-or-invariant boundary

**Status:** promoted as P45 after the original overclaim failed hostile audit,
the amended whole artifact passed a fresh hostile re-audit, and a context-free
proof-blind reconstruction succeeded.

**Closest prior route and material difference.** C41/P44 classifies
coordinate-ring automorphisms and reads only their intrinsic first jet. C42
allows the semantically larger class of polynomial-induced bijections of the
finite zero-product point set, but requires a public cap on the submitted
exact formal degree so every axis restriction is accessible.

**Verified boundary.** On a distinct semiprime, \(2D<\min(p,q)\) forces each
local source axis wholly onto one target axis. Differing local orientations
make an axis-restriction coefficient expose a factor; on the no-factor branch
the orientations synchronize and preserve the exact factor-free region.
For the unconditional terminal law of any uniformly bounded adaptive
explicit-circuit run,

\[
\Pr(H)\ge
\frac{2N-2}{(2p-1)(2q-1)}
-d_{\rm TV}(\mu,\pi_N).
\]

The circuit monitor has expected polynomial overhead under one fixed degree
cap and one fixed expected total encoding-length bound. A uniform or
inverse-polynomial TV gap below \(1/2\) yields a Las Vegas
distinct-semiprime splitter; pointwise \(\delta_N<1/2\) does not suffice.

**Remaining gap.** Characteristic-scale succinct point permutations,
noninvertible/stochastic or auxiliary/lifted kernels, accessible rational or
piecewise maps, positive matching encodings, direct samplers, warm starts,
and nonsquarefree geometry remain open. P45 supplies no complete all-input
factoring algorithm.

### C43 — the natural propagated multiplier cell has a rank-12 matchgate obstruction

**Status:** promoted as P46 after a clean hostile audit and a fresh
context-free proof-blind reconstruction.

**Closest prior route and material difference.** C33/P36 obstructs the
separated COPY\(_3\)--AND\(_3\) gate set. C43 fuses factor propagation,
partial multiplication, accumulator update, and carry into the smallest
natural eight-leg scalar-Boolean schoolbook tile and permits an independent
invertible basis on every leg.

**Verified boundary.** The cell tiles an exact planar shifted-add multiplier
whose target and prefix constraints are boundary unaries and whose ordered
factor witnesses have multiplicity one. In its actual planar rotation, the
incoming and outgoing legs are complementary contiguous arcs. The
corresponding flattening consists of four rank-three full-adder blocks, hence
has rank \(12\). Every nonzero matchgate/pure-spinor signature has rank
\(2^r\) across a contiguous cyclic split, including odd signatures and
degenerate charts; particle-hole Clifford maps reduce to the vacuum
Pfaffian chart without changing rank. Arbitrary independent leg gauges
therefore cannot make this cell a matchgate.

**Remaining gap.** This is a cell/order obstruction, not a contraction lower
bound. F38 tests horizontal strip fusions. General two-dimensional blocks,
other planar rotations, packed/projected/auxiliary encodings, global
Pfaffian identities, modular constructions with exact recovery, and
non-matchgate polynomial contractions remain open. P46 supplies no factoring
algorithm.

### C44 — smooth multiplier clouds lose to the Fermat resolution they create

**Status:** promoted as P47 after a historical amendment audit, a clean fresh
whole-artifact re-audit, and a context-free proof-blind reconstruction.

**Closest prior route and material difference.** C20/P26 enumerates only
numerical multipliers \(k\le\operatorname{poly}(n)\). C44 permits a
polynomial-bit known-factorization multiplier whose potentially exponentially
many allocations \(k=cd\) are all pooled by one ordinary Fermat scan. This is
the explicit metric/allocation-cloud version of amortizing many lucky
relations.

**Verified boundary.** A useful allocation has exact gap

\[
\sqrt{kN}\!\left(
\cosh\!\left(\tfrac12\log\frac{c/d}{q/p}\right)-1
\right),
\]

so a polynomial scan requires log-ratio error
\(O((kN)^{-1/4}\sqrt T)\). Summing all divisor windows and using
\(\tau(k)=k^{o(1)}\) proves that no target-independent polynomial list covers
a fixed positive-length ratio interval, regardless of multiplier magnitude.
On an infinite balanced-semiprime family with \(q/p\) exponentially close to
\(\sqrt2\), quadratic irrationality gives gap \(>p/(432k^3)\) uniformly for
every coprime adaptive \(o(\sqrt n)\)-bit multiplier, so direct
useful-square/gcd extraction misses through every fixed polynomial cap.

**Remaining gap.** P47 does not address adaptive \(\Omega(\sqrt n)\)-bit
multipliers concentrated on the actual prime ratio, joint decoding of
nonsquare residues or complete scan transcripts, other metric observables,
non-gcd extraction, or an all-input splitter. The continuous theorem must not
be inflated into an adaptive discrete lower bound.

### C45 — every horizontal propagated-cell strip retains a matchgate rank obstruction

**Status:** promoted as P48 after a historical amendment audit, a clean fresh
whole-artifact re-audit, and a context-free proof-blind reconstruction.

**Closest prior route and material difference.** C43/P46 treats one natural
eight-leg propagated multiplier cell. C45 contracts the shared (y) and
ripple-carry legs of an arbitrary length-(L) row, so it tests whether fusion
removes the single-cell obstruction rather than merely repeating it.

**Verified boundary.** The fused tensor is exactly the multiplicity-one
relation

\[
x_i^-=x_i^+,\qquad y_0=y_L,\qquad
A+y_0X+c_0=S+2^Lc_L.
\]

An explicit two-lane planar embedding puts all incoming and outgoing legs on
complementary contiguous cyclic arcs. Across that cut propagation gives
(2^{L+1}) blocks, and each arithmetic block has rank (2^L+1). Hence the
exact rank is

\[
2^{L+1}(2^L+1),
\]

which is never a power of two for (L\ge1). The P46 all-chart pure-spinor
lemma and invariance under arbitrary independent leg gauges therefore exclude
every finite horizontal strip in its inherited characteristic-zero matchgate
orbit.

**Remaining gap.** This closes only horizontal scalar-cell fusion in one port
order. Genuinely two-dimensional blocks, alternate rotations or encodings,
auxiliary/projection schemes, global Pfaffian identities, modular recovery,
and non-matchgate contraction remain open. P48 supplies no factoring
algorithm.

### C46 — the easy inverse graph has no polynomial-sample sparse Fourier signal

**Status:** promoted as P49 after a scope-amended hostile audit and a fresh
context-free proof-blind reconstruction.

**Closest prior route and material difference.** C37--C42 study a desired
quadratic-energy law whose sampler is missing. C46 instead starts from an
expected-constant-time source available from bare \(N\): uniform units and
their exact modular inverses. It tests lossy Fourier and rectangular metric
statistics rather than a local-zero target law.

**Verified boundary.** Exact CRT twists factor every inverse-graph Fourier
coefficient into prime Kloosterman sums. Every nonzero mode with
\(\gcd(a,b,N)=1\) has magnitude at most
\(4\sqrt N/\varphi(N)\). The larger \(N^{-1/4+o(1)}\) modes are real but
require both coordinates to share a hidden prime, so the proposed frequency
already carries a public factor. After explicitly summing those hidden
frequency sublattices, two-dimensional Erdős--Turán--Koksma gives
\(D_N^*=O(N^{-1/2}\log^2N)\). Ordinary empirical Fourier means and regular
raw bin counts therefore need \(N^{1-o(1)}\) samples for relative accuracy,
with the high-confidence statement restricted to the constants actually
delivered by Paley--Zygmund.

**Remaining gap.** P49 is neither a factoring lower bound nor a general
source-side no-bias theorem. Nonlinear or Fourier-dense processing, implicit
hidden-frequency search, correlated/nonuniform sources, canonical metric
branching, curved bins, exact amplification, noisy ACD/HNP/Coppersmith
decoding, and dissipative dynamics remain open.

### C47 — bounded-degree actual-fibre bias has a sharp diffuse/constant boundary

**Status:** promoted as P50 after the original hostile audit found a
mathematical gap, a corrected fresh whole-artifact re-audit passed, and a
context-free proof-blind reconstruction recovered the amended result.

**Closest prior route and material difference.** C27--C29/P28--P31 restrict
quaternion completions to residual-only rules or fixed menus. C47 allows the
completion to inspect the actual uniformly sampled conic point and may use a
bounded-degree rational branch or algebraic graph component. It therefore
tests a genuine source-side bias rather than another independent collision
ticket.

**Verified boundary.** On the projective source conic, a degree-\(D\)
completion produces a map into the rank-one Segre quadric. The pullback
degrees of its image and row factors sum to at most \(2(D+1)\). Every
locally nonconstant line branch consequently has fixed-line fibres of size
at most \(2(D+1)\), and a \(B\)-branch selector has unconditional no-factor
output subprobability at most

\[
 {2B(D+1)\over r-\chi_r}.
\]

The normalized-graph version uses the corresponding
\(\mathcal O(1,1)\)-degree. Explicit binary forms of unequal reduced local
degree reveal a factor through subresultants, and one public conic point gives
an exact same-fibre uniform sampler with its full gcd trichotomy.

The boundary is attained by a real degeneration. From a public pair set
\(h=u_0^{-1}c_0\). Then \(c=uh\) gives a constant row at both hidden
fields, while \(c=h\bar u\) gives a constant image at both. The synchronized
degree-zero behavior need not expose a coefficient factor; the \(N=21\)
matrix certificate has constant row \([0:1]\) modulo both primes.

**Remaining gap.** P50 controls fixed/past-measurable targets on fresh calls,
not equality of two maps on the same source. The explicit constant family may
still carry a factor-asymmetric metric or nonlinear signal in its varying
quaternion values. Implicit graphs, adaptive coefficient/minor systems,
characteristic-scale degree, and piecewise, stochastic, canonical-metric, or
dissipative completions remain open. Synchronized bias alone is not yet a
useful manufactured hint.

### C48 — ordinary LLL needs \(2^{-\sqrt n}\)-scale relative ACD precision

**Status:** promoted as P51 after a failed first hostile audit, substantive
amendment, clean fresh whole-artifact re-audit, and context-free proof-blind
reconstruction.

**Closest prior route and material difference.** C46/P49 starts from the
available but Fourier-flat inverse graph. C48 grants a much stronger
factor-correlated source \(z_i=pt_i+r_i\), with uniform hidden quotients and
one-sided bounded errors, and asks what a standard polynomial-time lattice
decoder can actually certify. P39 treats a different full-lattice uniform
subspace model.

**Verified boundary.** The natural lattice has factor vector
\((qB,qr_1,\ldots,qr_m)\). Simultaneous Dirichlet approximation gives an
exact shorter-competitor condition, while a random-quotient union bound gives
the corresponding approximation-isolation upper regime. Ordinary LLL has
success at least \(1-2A\theta^m\), uniformly even when the errors are a
joint function of all quotients. At
\(B/p\le2^{-(1+\eta)\sqrt n}\) and \(m=\Theta(\sqrt n)\), failure is
\(2^{-\Omega_\eta(n)}\) and all bit complexity is polynomial.

At \(B/p=1/\operatorname{poly}(n)\), no dimension makes this proved
worst-case LLL certificate nontrivial: the isolation dimension is coarsely
\(n/\log n\) and the \(2^{m/2}\) approximation loss overwhelms the
polynomial precision. This is not an ACD or decoder hardness theorem.

**Remaining gap.** No bare-\(N\) source with either precision is known.
Different lattice bases, distribution-specific reduction, nonlinear or
spectral decoders, helpful correlated errors, robust partial-inlier
aggregation, and inverse-cloud metric statistics remain open. The positive
theorem is conditional and semiprime-only, not progress on the all-input
source requirement by itself.

### C49 — modular Newton attraction collapses to projective squaring

**Status:** promoted as P52 after a clean hostile audit and a context-free
proof-blind reconstruction.

**Closest prior route and material difference.** P44/P45 treats explicit
automorphisms and low-degree bijections of the zero-product scheme. C49
tests a degree-two noninvertible rational map and therefore directly probes
the proposed dissipative escape. P22's \(N^2\)-adic carrier is unrelated to
finite-field basin dynamics.

**Verified boundary.** The Möbius coordinate
\(z=(x-s)/(x+s)\) globally conjugates
\(T(x)=(x^2+s^2)/(2x)\) to \(z\mapsto z^2\), including every projective
exception. Exact roots have no preimages beyond themselves. On primes
\(3\bmod4\), nonzero orbits also never hit the affine pole. Thus all named
denominator, numerator, residual, and \(x_k\mp s\) gcd tickets are fixed at
time zero.

For \(N=pq\) with both primes \(3\bmod4\), the accepted-unit and full raw-
sampler success probabilities are exactly

\[
 {2p+2q-10\over(p-1)(q-1)},
 \qquad
 {3p+3q-12\over pq-1}.
\]

An infinite balanced PNT-in-AP family makes both \(O(N^{-1/2})\), so
polynomial restarts are negligible and repeat-until-success is exponential
in the input length.

**Remaining gap.** Cross-iterate collision/order tests, arbitrary nonlinear
orbit transcripts, primes \(1\bmod4\), other maps, p-adic lifts, correlated
starts, and stochastic, piecewise, ordered, or canonical-metric dynamics are
outside P52. F26 now tests a genuinely decreasing integer inverse-quotient
map rather than another finite-field basin metaphor.

### C50 — shifted-Jacobi scalar correlations have a public fair-sign simulator

**Status:** promoted as P53 after a clean hostile audit and a fresh
context-free proof-blind reconstruction.

**Closest prior routes and material difference.** P15 closes only
factor-swap-invariant multiplicative scalar phase labels. P49 treats sparse
additive Fourier statistics of the inverse graph. C50 instead allows
nonlinear products of many publicly shifted Jacobi symbols, repeated shifts,
and fresh past-adaptive query menus, then asks whether their empirical
correlations manufacture a factor-asymmetric bias.

**Verified boundary.** Difference screening makes every distinct shift
injective in both hidden fields. CRT factors each product mean into two
complete character sums. A nonempty odd-multiplicity support has mean at most
\((s-1)^2/\sqrt N\) by the correctly centered odd/even hyperelliptic bounds;
the all-even branch has exact mean \((1-s/p)(1-s/q)\). The complete
three-point law shows that learning either the small odd mean or the
informative all-even deviation takes exponentially many raw samples for
polynomial \(s\).

For one hidden-source scalar per fresh call, sequential maximal coupling
compares every adaptive transcript of total support \(T\) with a public
fair-sign/constant-one process within
\((2\Lambda T+T^2/2)/\sqrt N\). Explicit polynomial lists with polynomial
coefficient \(\ell_1\)-norm likewise have only polynomial-over-\(\sqrt N\)
mean drift.

**Remaining gap.** The theorem intentionally hides the sampled residue and
compresses all shifted symbols to one product. Per-shift vectors, gcd labels,
several correlations sharing one source, same-source adaptation, exact
symbolic sums, succinct dense statistics, and nonlinear joint decoders are
open. Thus C50 is a sharp scalar-channel boundary, not a generic Jacobi
indistinguishability claim.

### C51 — Hadamard--Paley relation pooling is low-degree-hard but high-order-open

**Status:** promoted as P54 after a clean hostile audit and a fresh
context-free proof-blind reconstruction.

**Closest prior routes and material difference.** C50/P53 controls a scalar
product or a polynomial-\(\ell_1\) combination from each fresh hidden source.
C51 retains \(m=\Theta(n)\) shifted signs jointly and allows one arbitrary
bounded decision rule with superpolynomial Fourier support. The only
restriction is its Walsh degree, so this is a genuine amortization test rather
than another single-invariant gcd.

**Verified boundary.** Difference screening makes the local shift polynomials
squarefree. Independent zero filling and CRT give the exact Walsh coefficient
\(c_S=A_p(S)A_q(S)/N\); degrees one and two are exactly \(0\) and \(1/N\),
and higher coefficients are at most \((|S|-1)^2/\sqrt N\). Parseval then
controls every bounded rule of degree
\(D\le n/(20\log_2n)\) by
\(2^{-9n/20+O_C(\log n)}\) after the exact accepted-word conditioning
penalty. Past-adaptive use remains covered only when each fresh source and row
is immediately compressed to one released bit and discarded.

The raw sampler's accepted, full-gcd rejection, and proper-gcd success
probabilities are known exactly. The whole filled word is not claimed
pseudorandom: its support is below \(4N\), and the public pair \((X,W)\) is
outside the marginal theorem.

**Remaining gap.** Retained sources, full-row release, same-row reuse, high or
characteristic-order processing, exact transforms, and genuine
Hadamard--Paley/product-code list recovery remain open. A precise HP-LR
decoder hypothesis has an all-input Las Vegas reduction with complete
prime-power and recursion bookkeeping, but the hypothesis itself already
requires inverse-polynomial-probability recovery of a numerical odd-exponent
prime factor. It is the missing algorithm, not a consequence of the
low-degree theorem.

### C52 — Lucas-torus relations carry the exact signed factor gap, but opaque pooling remains generic

**Status:** promoted as P55 after a clean hostile audit and a fresh
context-free proof-blind reconstruction.

**Closest prior routes and material difference.** P20--P21 asks for a
succinct evaluator of an exponentially long torus order-threshold product,
and P12 studies dense moments of one modular-multiplication spectrum. C52
instead evaluates only ordinary powers and exposes polynomially many
ubiquitous nonzero equations with one common hidden exponent magnitude.

**Verified positive mechanism.** For \(N=pq\) with distinct odd primes, the
Cayley chart of \(A_D=(\mathbb Z/N\mathbb Z)[w]/(w^2-D)\) is exact away from
\(-1\), and its local torus has order \(r-(D/r)\). A unit \(D\) chosen first
conditional on Jacobi symbol \(-1\) has a fair split/nonsplit orientation.
Keeping that \(D\) while resampling a pole-free \(t\) preserves fairness;
every pole itself returns the unique split prime. Pointwise for every
norm-one element,

\[
U^{N-1}=U^{q-p}\quad(+,-),\qquad
U^{N-1}=U^{p-q}\quad(-,+).
\]

The triples are generated in expected polynomial bit and fair-random-bit
cost. A uniform inverse-polynomial-success decoder for the integer magnitude
\(q-p\) would factor the distinct-odd-semiprime promise through the exact
test \((q-p)^2+4N=(p+q)^2\). Early denominator or discriminant gcds can only
help, by an exact same-tape coupling to the ideal clean sampler.

**Verified generic boundary.** In \(K\) independently random-encoded tagged
cyclic groups of common prime order \(\ell\), with the signs granted and at
most \(Q\) generic actions, affine symbolic exponents give

\[
\Pr(\widehat e=e)\le
\min\left\{1,{1\over\ell}+
{\binom{Q+3}{2}+3(K-1)\over\ell}\right\}.
\]

The subset, list, and nonuniform-prior variants have the corresponding
collision-count numerators. This closes relation-count amortization only in
the opaque common-prime-order abstraction.

**Remaining gap.** Actual Lucas elements share explicit composite-ring
coordinates, have unequal composite orders and non-generators, admit
cross-discriminant algebra and zero-divisor gcds, and carry a deterministic
worst-case gap. A coordinate-specific polynomial-time decoder remains open,
as do interval methods and nonuniform sampling. Even after such a decoder,
prime powers, multifactor and even inputs, arbitrary composites, recursion,
and complete factorization require a separate extension. P55 is therefore
not the all-input theorem.

### C53 — multiplicative Teichmüller high digits have one global carry cocycle

**Status:** promoted as P56 after a clean hostile audit and a fresh
context-free proof-blind reconstruction.

**Closest prior route and material difference.** C19/P22 bounds direct gcds
of a fixed polynomial-size collection of canonical high digits from one
uniform base. C53 permits arbitrary finite collections of engineered,
adaptive, or nonuniform unit bases linked by genuine multiplicative
relations, and tests whether many cycles can expose incompatible local
cocycles.

**Verified boundary.** For every \(N\ge2\),

\[
A(a)=a^N\bmod N^2=x(a)+Nh(a)
\]

is a well-defined homomorphism. With canonical carry

\[
c(x,y)=\frac{xy-\langle xy\rangle_N}{N},
\qquad
\lambda=h x^{-1},
\qquad
\kappa=c(x,y)\langle xy\rangle_N^{-1},
\]

one has

\[
\lambda(ab)=\lambda(a)+\lambda(b)+\kappa(x(a),x(b))\pmod N.
\]

Every occurrence-labelled multiplicative graph therefore satisfies one
global public system \(B\lambda=\kappa\). Edge residuals, arbitrary
ring-linear pools, cycle/left-syzygy syndromes, and augmented-consistency
failures vanish modulo every divisor. This does not equalize coefficient
ranks across CRT fields or control minors, Smith data, nonlinear eliminants,
or the quotient of an integer residual after division by \(N\).

The exact collision/descent classification is

\[
A\text{ is determined by }x\text{ on all units}
\iff N_{\rm odd}\text{ is squarefree and }8\nmid N.
\]

Repeated odd primes retain a principal-unit coordinate in \(A\) that \(x\)
erases; \(1\) and \(1+p\) witness it, including \(p=3\). For
\(2^e\), \(e\ge3\), the signless principal coordinate survives and
\(1,5\) witness the failure already at \(e=3\). Thus occurrence labels are
mandatory outside the exact descent range. The whole transcript is computed
in \(O(Vn^3+En^2)\) schoolbook bit operations.

**Remaining gap.** Additive or nonmultiplicative relations, coefficient-rank
or minor/Smith selectors not equivalent to augmented consistency, nonlinear
whole-graph processing, a canonically useful higher integer quotient,
power-map inversion, noncanonical or higher lifts, and engineered base laws
with inverse-polynomial all-input separation remain open. P56 is a method
failure for multiplicative linear-cocycle inconsistency pooling, not a broad
\(N^2\)-adic obstruction and not a factoring algorithm.

### C54 — ordinary Dickson traces have an exact four-alias boundary

**Status:** promoted as P57 after a clean hostile audit and a fresh
context-free proof-blind reconstruction.

**Closest prior routes and material difference.** C52/P55 uses
discriminant-dependent norm-one tori and closes only independently encoded
generic shared exponents. C09/P12 treats spectral moment support. C54 uses
the ordinary unit group, no auxiliary discriminant, and exact numerical ring
coordinates; trace symmetrization exposes two globally valid
factor-determining representatives.

**Verified boundary.** For \(N=pq\) with distinct odd primes, put

\[
 e=N-1,\qquad t=p+q-2,\qquad g=q-p,
\qquad L=\operatorname{lcm}(p-1,q-1).
\]

For every unit trace \(T(a)=a+a^{-1}\),

\[
 D_e(T(a))=D_t(T(a))=D_g(T(a)).
\]

The complete function alias class is

\[
 D_m(T(a))=D_e(T(a))\text{ for all units }a
 \iff m\equiv\pm t,\pm g\pmod L.
\]

Both exact positive representatives factor through polynomial-bit verified
integer discriminants. Powers, products, repeated bases, Dickson
composition/addition, and adaptive trace-interface expressions are exact
functorial consequences of the same function and cannot select one
representative. In the quotient-by-inversion random-encoding model,
polynomially many tags and calls retain only an
\(O((M+Q^2+K)/\ell)\) list-recovery probability; the theorem is explicitly
nontransferable to numerical \(\mathbb Z/N\mathbb Z\) coordinates.

**Constructive survivor.** The shifted public values
\(D_{e+k}(x),D_{e-k}(x)\) are two known roots of a public quadratic, while
\(D_{g+k}(x),D_{g-k}(x)\) are its coherently CRT-mixed roots. After
screening the known-root difference, producing one mixed root factors by one
comparison gcd. Thus the symmetry has been localized to a concrete
root-orientation problem rather than eliminated. Formal derivatives and
modulo-\(N^2\) discrepancies are additional information, not consequences
of the value aliases; the latter involve a lift-dependent Euler quotient.
Lucky shifted/root gcds remain open because no inverse-polynomial all-input
probability bound was proved.

**Remaining gap.** Characterize and attack the coherent root-selection
system across many bases and shifts; construct a public derivative,
resultant, minor, or lift statistic; manufacture a polynomial-size metric
candidate set; or prove a useful non-generator/order distribution. Any
promise decoder must then be extended to prime powers, repeated factors,
even and multifactor inputs, recursion, and one uniform Las Vegas expected
bit bound. P57 is a narrow method classification, not a factoring algorithm.

### C55 — coherent Dickson-root relations reduce to one binary switch

**Status:** verifier-backed and promoted as P58/X52. Two earlier mathematical
versions failed hostile audit. The twice-corrected artifact passed a fresh
whole-proof audit and a strict proof-blind reconstruction. No cross-family audit
has run.

**Verified boundary.** For a distinct odd semiprime, first use gcd screens and
linear equations to remove known constant roots, then simplify all repeated and
constant-position relations. On each proved connected component of the remaining
orientation graph, all coherent root choices share one idempotent switch, with
coordinate algebra

\[
  (\mathbb Z/N\mathbb Z)[f]/(f^2-f).
\]

An explicit public polynomial relation on that one component has only three
relevant
outcomes: it accepts both public synchronized choices; one endpoint evaluation
already exposes a factor; or it asks for a mixed choice whose production is the
original factoring problem. The claim does not cover arbitrary couplings between
independent components, auxiliary existential variables, metric order, random
root samplers, derivatives, or lifts.

**Algorithmic consequence.** This is not the next factoring algorithm. It proves
that more equations inside the same component do not create more information.
A retry must add a genuinely different operation: metric order, nonlocal or
stochastic sampling, derivatives/lifts, or a joint decoder across structures not
covered by the one-idempotent algebra.

### C56 — one-defect Gibbs crosses the public axes but not the factor barrier

**Status:** verifier-backed and promoted as P59/X53. The first hostile audit
found two scope errors. The corrected theorem passed a fresh whole-proof audit
and a strict proof-blind reconstruction. No cross-family audit has run.

**Verified boundary.** The sampler records (d=kx), gives (d=0) and
(d\ne0) different scalar weights, and refreshes one of the two free
coordinates exactly. It is stochastic, leaves the zero-product set, and can
cross between the two public unit axes. Nevertheless, before success, a local
refresh can create a proper nonunit only at its raw density. This forces
\(\Omega(\sqrt N)\) hitting and fixed-threshold mixing time on balanced
semiprimes and prime squares, for every positive scalar activity.

**Algorithmic consequence.** The defect idea is not closed, but the algorithm
must now change its move. A useful retry needs a joint block move, interacting
defects, valuation amplification, a nonuniform arithmetic proposal, or a
factor-correlated warm start. Another scalar reweighting of the same local
refresh cannot help.

### C57 — the canonical high digit is structured but its easy metric signals are thin

**Status:** verifier-backed and promoted as P60/X54. The first hostile audit
rejected an overbroad Fourier claim. The corrected theorem passed a fresh audit,
all five computations reproduced exactly, and a strict proof-blind
reconstruction succeeded. No cross-family audit has run.

**Verified boundary.** For balanced distinct odd semiprimes, the high digit of
(a^N\bmod N^2) has exact local Fermat-quotient laws and visible nonuniform
structure. This is genuine factor-dependent arithmetic, not a uniform-output
fiction. However, every exact value and hidden local residue has only
(O(1/\sqrt N)) mass. Fixed sparse menus, collisions, direct gcds, thin bands,
the central-half bias, and uniform searches for large Fourier modes therefore
need exponentially many samples.

**Algorithmic consequence.** The source is not dead. A retry must use the
whole structured graph rather than wait for a rare value. The open operations
are exact small-bias amplification, adaptive exceptional-frequency recovery,
dense nonlinear processing, or a deliberately correlated base source.

### C58 — arbitrary residual weights do not make the local sampler an amplifier

**Status:** verifier-backed and promoted as P61/X55. Two hostile audits found
seven real scope or interface errors. The twice-corrected theorem passed a
fresh whole-proof audit and a strict proof-blind reconstruction. No cross-family
audit has run.

**Verified boundary.** Give a pair \((k,x)\) any nonnegative weight that
depends only on its product \(kx\), and refresh one coordinate exactly. At a
held unit, the new product has exactly the chosen residual law. At a held zero,
the new coordinate is uniform. These are the only cases before a gcd finds a
factor. Thus the local wrapper cannot raise the per-step success chance above
the larger of the residual law's existing factor mass and the raw density of
proper nonunits.

If a useful residual law and its exact sampler can be built uniformly from
bare \(N\) in expected polynomial time, that sampler already factors directly.
The wrapper adds no amplification. If its factor mass is small, polynomially
many local refreshes remain ineffective on balanced semiprimes and prime
squares.

**Algorithmic consequence.** We are not waiting for a better scalar weight.
A real sampler retry must change an operation: update both coordinates jointly,
couple several residuals, use a lift, or decode a whole trajectory. P61 does not
rule out a direct factor-correlated residual source; it says that finding one
would already be the main algorithmic breakthrough.

### C59 — inverse-quotient descent is real dissipation, but its fast decoder is missing

**Status:** verifier-backed and promoted as P62/X56. The first hostile audit
found a reverse-fibre error and several scope or provenance errors. A fresh
re-audit found one stale manifest statement. The corrected artifact then passed
a second fresh whole-artifact audit and a strict proof-blind reconstruction. No
cross-family audit has run.

**Verified boundary.** For a unit $u<N$, multiply it by its canonical
inverse modulo $N$, subtract one, and divide exactly by $N$. The result is

\[
D_N(u)=u-r_u,
\]

where $r_u$ is the canonical inverse of $N\bmod u$. The state therefore
strictly decreases. Its reverse fibre consists exactly of complementary factors
of $Nk+1$. Grouping steps by their decrement gives the unbounded depth bound
$N^{1/2+o(1)}$, while an explicit square family has trajectories linear in
its bit length. A universal two-step halving rule is false even for a balanced
semiprime.

**Algorithmic consequence.** This mechanism does move away from “compute one
ring scalar and take one gcd.” It keeps an ordered integer state and creates a
sequence of exact factorizations $u_i v_i=N u_{i+1}+1$. However, the proved
depth is still exponential in the input length, and no useful hit probability
is known. The next test must use the whole sequence. A parity, lattice,
continued-fraction, or other joint decoder must extract more than the union of
rare coordinate gcd events. F26 remains open.

### C60 — formal degree is not real basin mass

**Status:** verifier-backed and promoted as P63/X57. The candidate passed a
fresh hostile whole-artifact audit and a strict proof-blind reconstruction. No
cross-family audit has run.

**Verified boundary.** The noninvertible map $x(x-1)$ appears to branch
backward. But when $5$ is a non-square modulo a hidden prime, the first new
branch does not exist. The complete basin of its two public roots then stays at
two points for all time. Unit scaling and affine relabeling only rename the
same process. Infinitely many balanced semiprimes have this obstruction on
both prime sides, so all root-ticket restarts remain a square-root-scale search.

For a general map, target-ticket success is at most the sum of the two local
backward-basin densities. This gives a clean test for future dynamic samplers.

**Algorithmic consequence.** Iteration and exponential composed degree do not
manufacture information by themselves. A retry must prove that actual local
preimages occupy inverse-polynomial density for every hidden-prime family. Or
it must use a different output, such as a full-orbit period, collision,
valuation, or joint transcript decoder. General polynomial dynamics remain
open.

### C61 — label parity is empty, arithmetic parity is the real decoder

**Status:** verifier-backed and promoted as P64/X58. The first hostile audit
found two real overclaims. The corrected proof passed a fresh whole-proof audit
and a strict proof-blind reconstruction. No cross-family audit has run.

**Verified boundary.** Pooling inverse pairs by repeated public endpoint names
does not help. Every nonloop parity cycle contributes $1\bmod N$. Self-loop
roots can make new root values when multiplied, but each nontrivial loop already
factors under a direct screen. After those screens, the whole formal parity
kernel gives only $\pm1$.

This does not close true integer square relations. Distinct labels can share
prime factors. The pair $(2,8)$ modulo $15$ already gives the square $16$
and the factor $3$, even though neither label repeats.

**Algorithmic consequence.** Whole-batch decoding remains live, but its matrix
must record arithmetic prime-valuation parity or another real relation. A graph
whose vertices are only exact endpoint names discards that information. The
next candidate uses the public quotient indices $k$ and the fact that common
factors of $Nk_i+1,Nk_j+1$ divide $k_i-k_j$.

### C62 — bare $N$ makes completion bias, but factor correlation is unproved

**Status:** verifier-backed and promoted as P65/X59. The first hostile audit
found a real duplicate-handling bug and an overstrong equivalence claim. The
corrected theorem passed a fresh whole-artifact re-audit and strict proof-blind
reconstruction. No cross-family audit has run.

**Verified boundary.** A uniform unit $U$ does not give a uniform quotient.
The output $k=D_N(U)$ has probability proportional to the number of divisor
completions of $Nk+1$ that fit inside the canonical range. This is an exact
implicit sampler. It uses only bare $N$ and does not evaluate those weights.

The bias is diffuse. Polynomially many independent outputs almost never
collide or enter one polynomial-width interval on balanced semiprimes. Inside
any interval that is available, common prime factors of two relation values are
confined to the public index differences. This gives a complete arithmetic
square-relation decoder for that interval.

**Algorithmic consequence.** The route now has three different operations:
canonical metric sampling, ordered descent, and batch parity decoding. It is no
longer only one scalar identity followed by one gcd. The missing theorem is
source-side: prove that some polynomial-time source from bare $N$ creates a
squareclass dependency whose root is non-global often enough. Completion bias
alone is not yet factor bias, and P65 is not a factoring algorithm.

### C63 — exact batch decoding is complete; the missing object is the useful list

**Status:** verifier-backed and promoted as P66. The first hostile audit found
a false novelty boundary and an incomplete complexity parameter. The corrected
and strengthened theorem passed a fresh whole-artifact re-audit and strict
proof-blind reconstruction. No cross-family or human audit has run.

**Verified boundary.** We do not need a short interval, small factors, or the
prime factorization of the relation values to decode exact square relations.
Ordinary gcd refinement splits any explicit polynomial-size list into
pairwise-coprime blocks. One square test per block and binary linear algebra
then describe every square subset exactly. Testing one basis of those subsets
cannot miss a factor-bearing normalized root.

The gcd-free basis is known technology. The useful project result is the clean
separation it gives us: decoder difficulty is finished for exact relations of
polynomial total size. The decoder keeps the full true rank. It does not create
a relation and does not compress the hard information.

**Algorithmic consequence.** The target is now precise. A source from bare $N$
must make a polynomial-size list with two properties: its integer square
classes must have a dependency, and at least one dependency must compare two
different local square roots. The second property matters. A list can contain
many exact square relations and still give only global $+1$ or $-1$ roots.

### C64 — descent has more structure, but its runtime gap remains exponential

**Status:** verifier-backed and promoted as P67/X60 after a failed first audit,
a passing fresh whole-artifact re-audit, and strict proof-blind reconstruction.
No computation, cross-family audit, or human audit ran.

**Verified boundary.** Distinct inverse labels improve the unconditional
trajectory bound to

\[
L<\sqrt{2N\log N}.
\]

Two adjacent steps also satisfy exact positive determinant identities. Each
step is a Farey decomposition, but the next step resets the numerator. This is
why the local continued-fraction picture does not become an ordinary Euclidean
descent.

An explicit nonsquare balanced composite family moves only from $u$ to $u-1$
for logarithmically many steps. This rules out every fixed contraction within
$o(\log N)$ steps. The family is factored by the first Fermat test, so it says
nothing about hard factoring inputs.

**Algorithmic consequence.** A polynomial depth theorem is still possible,
but it must use a cumulative invariant rather than a fixed local contraction.
Even such a theorem would only make the transcript cheap. P66 shows that a
separate non-global relation law is still necessary.

### C65 — generic relations split into certified decoys and an unresolved residue

**Status:** verifier-backed and promoted as P68 after one failed theorem
version, a passing fresh hostile re-audit, and strict proof-blind
reconstruction. No cross-family or human audit has run.

**Verified boundary.** A symbolic square relation is forced to give only the
global roots $\pm1$ when the least denominator of its symbolic root is
coprime to $N$. All such relations form a computable subspace $U_N$. Its
exact description uses only rational-polynomial factorization, coefficient
denominators, gcds with $N$, and binary linear algebra.

The condition is sharp. A generic relation with a denominator that shares a
factor with $N$ can be useful. If the denominator gcd equals all of $N$, it
can be either useful or another decoy. Therefore “generic” does not mean
“harmless.” Only the unit-denominator subspace is certified harmless.

**Algorithmic consequence.** The decoder now removes a whole proved-decoy
subspace before it tests roots. The remaining quotient is smaller and is the
right place to search, but it can still contain decoys. For every tested F59
offset batch, the entire complete kernel was removed. The next sampler must
create a relation outside $U_N$ and give it a non-global root. Merely creating
more symbolic identities does not help.

### C66 — feeding one gcd-free block is adaptive only in appearance

**Status:** verifier-backed and promoted as P69/X62 after hostile audit and
proof-blind reconstruction. The reconstruction forced exact source-size and
seed-scope wording. No computation, cross-family audit, or human audit ran.

**Verified boundary.** After a complete gcd-free refinement, feed one current
block into the inverse map. The block has only two outcomes. It is small enough
that the quotient-bounded direct scan already used it, or its inverse relation
is exactly one old relation value. Its new endpoint presentation is made only
of whole old blocks, so it cannot expose a finer block.

This stays true after any number of repeats. For a polynomial-size seed list
whose quotients are polynomial in $\log N$, one short nonadaptive saturation
dominates the whole adaptive loop.

**Algorithmic consequence.** This specific feedback loop adds bookkeeping but
no source power. A real retry must combine several blocks or relations, use a
different representative, or otherwise change the relation value. This leaves
the cross-relation product mechanism open.

### C67 — cross-relation products are a real new source operation

**Status:** verifier-backed and promoted as P70. The theorem passed a hostile
audit with required scope corrections and a proof-blind reconstruction. No
cross-family or human audit ran.

**Verified boundary.** Combine several inverse relations and select a legal
product of their gcd-free blocks. If their product is $1+KN$, the selected
state's new quotient is exactly $K\bmod g$. This can create a new relation
and a new block, and it can expose a factor even when the old exact
square-relation kernel is empty.

The operation is not limited to square roots of one. At $N=21$, the selected
state $10$ is not self-inverse, but $10-1$ already exposes $3$. At
$N=55$, blocks from two independent relations form the self-inverse state
$21$, which exposes both factors. Deliberate polynomial relation reuse also
creates a family whose useful selected state is near $\sqrt N$, far above
the seed quotient.

**Algorithmic consequence.** P69's one-block fixed point does not extend to
cross products. The decoder must preserve exact block occurrences and allow
new candidate construction. The remaining hard step is now the selector:
produce only polynomially many block products and prove that one is $+1$ or
$-1$ in a proper hidden component on every required input. Exhaustive
selection is exponential, so P70 is not yet a factoring algorithm.

### C68 — the self-inverse selector has an exact order/HSP boundary

**Status:** verifier-backed and promoted as P71 after a failed first hostile
audit, a corrected fresh re-audit, and a proof-blind reconstruction. No
computation, cross-family audit, or human audit ran.

**Verified boundary.** The public block map has a hidden integer relation
lattice. A legal selected block product is self-inverse exactly when twice its
exponent vector lies in that lattice. The old square decoder sees exactly the
2-saturation of the known relation lattice, but only as modular residues; this
does not give a representative in the finite occurrence box.

For one generator, the least nonidentity involutory exponent is half the exact
order, and a total least-answer oracle is order-equivalent. Recovering the full
relation lattice therefore contains modular order finding. A supplied lattice
basis makes the remaining 2-torsion postprocessing polynomial, but does not
solve lattice recovery or legal selection.

The finite distinction is real. At $N=187$, no legal state in the one-copy
box passes even the broader direct screen, although the unbounded subgroup
contains a useful involution. An odd-$t$ family requires $t=\Theta(\log N)$
explicit occurrences before its first legal self-inverse state appears. This
is a multiplicity boundary, not a support or full-screen lower bound.

**Algorithmic consequence.** Shor/HSP language identifies the hidden object
but does not supply its classical recovery. The live route must be narrower:
use the integer block presentation to find a legal direct CRT separator without
recovering the full hidden lattice. P71 supplies no such all-input selector.

### C69 — fixed orientations do not create factor bias

**Status:** verifier-backed and promoted as P72 after a failed first hostile
audit, a corrected fresh re-audit, and a proof-blind reconstruction. No
computation, cross-family audit, or human audit ran.

**Verified boundary.** Any fixed nonzero signed product of independent uniform
units is exactly uniform. On a balanced semiprime, a polynomial fixed menu has
only an exponentially small direct-screen probability. The same conclusion
holds adaptively when every trial retains a unit pivot that is uniform
conditional on the complete past and chosen before it is observed.

The first audit corrected an important overclaim. Reusing units across fixed
menu entries remains covered, but a rule chosen after observing a residue can
destroy uniformity without using integer presentation data. Correlated and
nonuniform states are also outside the theorem.

**Algorithmic consequence.** Cross-relation multiplication alone does not
manufacture a sampler. A useful selector must exploit a real operation change:
observed integer blocks or magnitudes, correlated/nonuniform states, or
adaptive refinement without a fresh-uniform mask. P72 does not show that any
such escape succeeds.

### C70 — feedback dependencies require square-class closure

**Status:** promoted as P73 after a failed first proof-blind reconstruction,
a corrected fresh hostile re-audit, and a corrected proof-blind
reconstruction. No computation, cross-family audit, or human audit ran.

**Verified boundary.** Complete gcd-free refinement gives the exact square
relation space. After one indexed feedback value is appended, nullity grows
exactly when its refined parity column is already in the old column span. A
private new-only nonsquare block prevents immediate closure. Over many rounds,
each new square class raises rank, while each closure raises nullity.

A canonical self-inverse state is the strongest immediate closure: it adds a
zero column. For odd $N$, it reveals factors exactly when it is a non-global
square root of one. Equal values count as separate dependencies only when they
remain separate indexed columns.

**Algorithmic consequence.** A new quotient or block is not enough. A useful
feedback sampler must first create closure and must then make the decoded root
non-global. P73 proves the first event's exact accounting, but supplies neither
its frequency nor the second event. It therefore sharpens the selector target
without giving a factoring algorithm.

### C71 — a closure contributes one canonical root coset

**Status:** promoted as P74 after hostile audit and strict proof-blind
reconstruction. No computation, cross-family audit, or human audit ran.

**Verified boundary.** A closing feedback column adds exactly one new kernel
direction. Its literal root depends on the chosen linear lift, but only by an
old decoder root. The canonical new information is therefore one coset modulo
the old root image.

After the old kernel basis has been screened without success, the old image
contains only the two global signs. The new closure is factor-bearing exactly
when one induced root is non-global. One new root test is then complete for
the enlarged decoder, including for odd nonsquarefree inputs.

**Algorithmic consequence.** Feedback has two separate gates: square-class
closure and a non-global root label. P74 makes the second gate exact and cheap
after closure. It does not make either gate frequent. The remaining work is
still source-side: generate polynomially many additions for which both gates
occur with an all-input inverse-polynomial law.

### C72 — the inverse-diagonal target has signal but no simple access

**Status:** promoted as P75 after hostile audit, two audit-directed precision
corrections, and fresh proof-blind reconstruction. No computation,
cross-family audit, or human audit ran.

**Verified boundary.** Weighting a unit by the inverse of one plus its
distance from its canonical inverse puts $\Omega(1/\log N)$ mass on the two
factor-revealing roots for a distinct-prime semiprime. Each signed-distance
fibre has at most four states. Thus the target distribution is strong enough
for polynomial factoring if it can be sampled accurately.

Uniform rejection and independent uniform-proposal Metropolis sampling need
$\Omega(N/\log N)$ time. Nearest-neighbor descent has a clean distance-one
trap, first occurring at $N=209$. These are access obstructions, not a general
lower bound for metric sampling.

**Algorithmic consequence.** Bare $N$ can define a public metric target with
inverse-polynomial factor mass. The unresolved step is to access that target
without already locating its sparse high-weight states. Block-guided or
correlated proposals remain open; the three simplest mechanisms do not work.

### C73 — endpoint refinement can change the generated search space

**Status:** promoted as P76 after a failed first hostile audit, a corrected
passing re-audit, and strict proof-blind reconstruction. No cross-family or
human audit has run.

**Verified boundary.** The distance between a residue and its canonical
inverse only reorders familiar square-root tickets. Small distance does not
move monotonically toward a factor, and equal distances can have different
square-closure behavior.

The adaptive operation itself survives. At \(N=209\), the selected endpoints
\(80\) and \(81\) are both in the subgroup generated by the old blocks.
Their integer factorizations overlap with an old composite block. Exact gcd
refinement exposes the new separate blocks \(2\) and \(5\). Their product
\(10\) lies outside the old block-generated subgroup and reveals \(11\).
Thus feedback can change the next candidate set even when its endpoint
residues contain no new subgroup element.

**Algorithmic consequence.** This is a real change in the algorithm, not only
a new identity followed by the same gcd. However, the example proves no
all-input selection law. The old subgroup at \(N=209\) also contains a
different separator outside the declared small menu. The next question is
therefore precise: can a public polynomial rule predict which endpoint
overlaps will strictly refine the blocks and then pass either a direct screen
or P74's two closure gates?

### C74 — exact balance is the wrong universal guide

**Status:** promoted as P77 after hostile audit and strict proof-blind
reconstruction. No research computation, cross-family audit, or human audit
has run.

**Verified boundary.** Balancing two sides of one exact relation only changes
where its existing blocks appear. It does not add a new relation value, a new
block, or a new root label. Combining two nontrivial relation values makes the
raw complementary side larger than \(N\), so ordinary number partitioning no
longer targets the canonical modular inverse.

Exact closeness is also not monotone toward a factor. At \(N=209\), the
closest pair \(80,81\) fails while a farther pair \(45,144\) reveals \(11\).
An infinite balanced family has only one allowed pair, at distance one, and
that pair fails every declared direct, discriminant, and square screen.

**Algorithmic consequence.** Do not spend the next round on a generic
balanced-partition solver or on more precise log balancing. The live feature
is the change in integer block structure after canonical endpoint feedback.
We must predict refinement gain or a non-global closure, not closeness by
itself.

### C75 — refinement can escape a separator-free old subgroup

**Status:** verifier-backed and promoted as P78. A first hostile audit found
five scope errors. The corrected theorem passed re-audit. A first proof-blind
statement then exposed undefined screens, an ambiguous overlap claim, and
missing domain assumptions. The final exact candidate passed a new hostile
audit and fresh proof-blind reconstruction. No research computation,
cross-family audit, human audit, or literature audit ran.

**Verified boundary.** At \(N=4033=37\cdot109\), the old block subgroup
\(\langle2\rangle\) has no direct separator. Canonical feedback can still
split an old composite block and expose \(5\notin\langle2\rangle\). The
refined subgroup contains \(630\), and
\(\gcd(630-1,4033)=37\). Both feedback endpoint residues were already in the
old subgroup.

The representative \(630\) is not in the current positive whole-block
occurrence box. Thus strict subgroup growth is real but does not supply a
legal selector. A separate infinite family gives immediate useful square
closure with zero old-block splitting. Conversely, the strict-expansion
witness has positive splitting but no immediate closure. Raw split count is
therefore not a stand-alone certificate.

**Algorithmic consequence.** Feedback has changed the algorithmic search
space, not only one scalar gcd input. The missing step is still access: a
public polynomial rule must produce an immediate separator, a non-global
closure, or a reachable factor-bearing representative with an all-input
inverse-polynomial law.

### C76 — endpoint powers can be trapped, but a relation quotient is a real operation change

**Status:** verifier-backed and promoted as P79. The endpoint trap, infinite
quotient escape, and exact square-class gate each passed a fresh hostile audit
and proof-blind reconstruction. No research computation, cross-family audit,
human audit, or literature audit ran.

**Verified boundary.** For

\[
N=c^2+c+1,
\]

with prime \(c\), endpoint powers remain in the order-three subgroup
\(\{1,c,c^2\}\). Arbitrary occurrence amplification, gcd refinement, exact
perfect-power extraction, direct screens, and complete \(2\)-saturation
produce no second block and only the global decoder root. An infinite
large-factor family proves that this is not a bounded trial-division artifact.

Promoting the public relation quotient \(g=c-1\) is a genuine state change.
It always lies outside the old subgroup. Put \(b=(c+1)/3\). The new relation
has square class \([b]\), while the old class is \([c]\). Therefore subgroup
expansion always occurs, but immediate decoder closure occurs exactly when
\(b\) is an integer square. When \(b=s^2\), the root
\(s(c-1)\) factors \(N\). A separate infinite robust family with
\(c=3s^2-1\) proves the same trap-and-escape separation for a composite
non-perfect-power old block.

**Algorithmic consequence.** This is the clearest current framework result.
It separates three events: enlarge the subgroup, cancel a square class, and
obtain a non-global root. A useful sampler must cause all needed events. More
relations or more generators alone are insufficient. The quotient is public,
so this is an operation-set distinction, not hidden side information or a
general factoring algorithm.

### C77 — quotient fibres can be inverted exactly

**Status:** verifier-backed and promoted as P80 after a failed first scope
audit, corrected proof-only re-audit, and proof-blind reconstruction. No
authoritative research computation, cross-family audit, human audit, or
literature audit ran.

For retained values \(A_i=1+k_iN\) and
\(P=\prod_iA_i=1+KN\), every supported feedback candidate with target
quotient \(r\) lies in

\[
D_r=\gcd(P,1+rN)
=\gcd\!\left(1+rN,\prod_i(k_i-r)\right).
\]

Conversely, every divisor \(g\mid D_r\) with \(r<g<N\) has quotient \(r\).
If \(N>r^2\), the fibre is nonempty exactly when \(D_r>r\), and one legal
member is constructed greedily after gcd-free refinement. This is the exact
target-first dual of selecting a block product and computing its CRT quotient.

The first audit found the decisive limit. If all old and target quotients are
at most \(B=\operatorname{poly}(n)\), a state scan through \(B^2\) already
recovers the same relation, aggregate divisor, and endpoint provenance. Thus
the exact sieve is new only with large correlated old quotient differences.

**Algorithmic consequence.** The exponential subset scan is removed inside a
declared quotient fibre. The missing source theorem is now sharper: adaptive
feedback must create large correlated quotients, and some polynomially
scanned fibre must then make direct, refinement, or decoder progress.

### C78 — canonical residues complete the fixed refinement chain

**Status:** verifier-backed and promoted as P81 after a proof-only re-audit
and proof-blind reconstruction. No research computation, cross-family audit,
human audit, or literature audit ran.

CRT updates of \(\rho(g)=(-N^{-1})\bmod g\) are exact bookkeeping for
coprime block extensions. The proposed inverse-size, quotient-size,
inverse-distance, and current-refinement scores are not extension-monotone.
This refutes them only as scalar dominance certificates, not as heuristics or
all possible polynomial beams.

Canonical-residue closure is the real operation change. It evaluates a public
block word modulo \(N\) before gcd refinement. The result stays in the old
residue subgroup but can use an integer representative outside the old
positive occurrence box.

At the post-P78 state \(N=4033\), \(H_1=\langle2,5\rangle\), the literal
support-two menu contains

\[
5^2 2^8\bmod4033=2367,
\qquad
\gcd(2367+1,4033)=37.
\]

Thus the fixed chain is now complete: cross-feedback refines a
separator-free subgroup and exposes \(5\); a small canonical word in the
refined subgroup then factors \(N\). The unsolved part is an all-input sparse
word or density theorem.

### C79 — independent uniform seeds do not feed the hard collision regime

**Status:** verifier-backed and promoted as P82 after a failed prime-scope
audit, corrected proof-only re-audit, and proof-blind reconstruction. No
research computation, cross-family audit, human audit, or literature audit
ran.

After polynomial trial division through \(B\), take \(m\) uniform inverse
relations and scan \(R\) targets. The probability that any collision divisor
contains a prime larger than \(B\) is at most

\[
\frac{2e\,mR\bigl(n+\lceil\log_2(R+1)\rceil+1\bigr)}B.
\]

Independence is unnecessary; uniform marginals suffice, and the union already
covers adaptive target selection inside the declared range. By choosing a
larger polynomial \(B\), every collision divisor is polynomial-smooth with
overwhelming probability and is fully exposed by trial division.

**Algorithmic consequence.** Large random quotients do not supply the missing
hard overlap. The live feedback source must be adaptive and structured. This
supports the composition

\[
\text{integer refinement}
\to\text{canonical residue words}
\to\text{correlated quotients}
\to\text{exact target-fibre scan},
\]

but no theorem yet proves the required correlation or factor-bearing density.

### C80 — subgroup sampling is solved; factor-bearing density is not

**Status:** verifier-backed and promoted as P83 after a proof-only hostile
audit and proof-blind reconstruction. No research computation, cross-family
audit, human audit, or literature audit ran.

Given public generators of any subgroup \(H\le(\mathbb Z/N\mathbb Z)^\times\),
independent random exponents from a sufficiently long public interval give a
distribution within \(2^{-2n}\) of uniform on \(H\). This uses no factor,
order, or subgroup-size oracle and has polynomial bit complexity.

For \(N=pq\), the exact density of elements that expose a factor through
\(\gcd(X-1,N)\) is

\[
\delta_+=\frac1{|H_p|}+\frac1{|H_q|}-\frac2{|H|},
\]

with the analogous exact formula for \(X+1\). If either density is inverse
polynomial, uniform subgroup sampling is already a Las Vegas
polynomial-time decoder.

But the existence of one separator does not imply useful density. An
abstract subgroup can contain a separator with density \(1/L\), where \(L\)
is exponential in the input length.

**Algorithmic consequence.** The missing object is not a generic dense
sampler. Feedback must force inverse-polynomial factor-bearing density, make
a rare separator accessible by a polynomial sparse-word menu, or continue
integer refinement until one of these conditions holds.

### C81 — feedback expansion has a hidden projection-kernel gate and an old-subgroup density ceiling

**Status:** verifier-backed and promoted as P84 after a hostile proof-only
audit and a proof-blind reconstruction. The only post-audit edits make the
pair-selection and \(L>2\) scope explicit. No research computation,
cross-family audit, human audit, or literature audit ran.

For \(N=pq\), let an old block subgroup \(H\) contain no positive sign
separator. Then both hidden projections of \(H\) are injective, so \(H\) is
the graph of an isomorphism and

\[
|H|=|H_p|=|H_q|=:h.
\]

For any later subgroup \(K\ge H\), put

\[
c=[K:H],\qquad a=[K_p:H_p],\qquad b=[K_q:H_q].
\]

The exact number of positive separators created in \(K\) is

\[
\frac ca+\frac cb-2.
\]

Thus subgroup growth \(c>1\) is not the gate. The gate is a nontrivial
kernel in one hidden quotient projection: \(c>a\) or \(c>b\). A single old
integer block split is the cyclic case, and every useful word is a power of
the new block cancelled by one unique old-subgroup element in one hidden
component.

More strongly, every coset of \(H\) contains at most four elements that can
pass either sign gcd. Hence every \(H\)-invariant law, including uniform
sampling from any later supergroup, has total direct-sign success at most

\[
\frac4h.
\]

The same ceiling survives adaptive mixtures, negligible sampling error, and
polynomially many pairwise products that retain one independent uniform
\(H\)-mask. If \(h\) is exponential in the input length, no amount of raw
subgroup expansion makes such sampling efficient.

**Algorithmic consequence.** Dense random exponent sampling is not the
feedback theorem to seek in the large synchronized regime. The live targets
are a public nonuniform cancellation-word selector, a direct integer overlap,
or P74's separate square-class closure plus non-global-root gate. The hidden
indices and cancellation word are not yet publicly computable, so no
factoring algorithm follows.

### C82 — a predeclared sparse word menu can miss a maximal diagonal escape

**Status:** verifier-backed and promoted as P85 after a hostile proof-only
audit and a proof-blind reconstruction. No research computation,
cross-family audit, human audit, or literature audit ran.

Let \(L>2\) be prime and let
\(S\subseteq\mathbb F_L^2\) be any exponent menu with
\(|S|\le L-3\), fixed before the new generator is chosen. In the diagonal
model

\[
g=(1,1),
\qquad
H=\langle g\rangle\le\mathbb F_L^2,
\]

there are distinct nonzero \(r,s\) such that \(z=(r,s)\) is not a separator,
\(\langle H,z\rangle=\mathbb F_L^2\), but no prescribed word

\[
Az+Bg,
\qquad
(A,B)\in S,
\]

is a separator. The proof avoids the at most \(|S|\) forbidden ratios
\(-B/A\); the determinant \(s-r\) then gives maximal expansion.

**Algorithmic consequence.** A fixed polynomial catalogue of bounded,
power-of-two, or least-common-multiple exponent pairs cannot be a universal
group-theoretic explanation for P81's small fixed witness. The theorem does
not cover a menu chosen from the numerical value of the new block, an
adaptive CRT beam, quotient-fibre targeting, integer refinement, or
square-class decoding.

### C83 — feedback can expose a base for smooth order contraction

**Status:** verifier-backed and promoted as P86 after a hostile proof-only
audit and a corrected proof-blind reconstruction. The first reconstruction
statement omitted one plus sign and correctly failed; both failed artifacts
remain preserved. No research computation, cross-family audit, human audit,
or literature audit ran.

For uniform \(X\) in a finite subgroup \(K\), the power \(X^M\) is uniform
on the image subgroup \(K^M\). This operation can contract the old subgroup,
so P84's old-coset ceiling does not apply. For one block \(u\) on
\(N=pq\),

\[
1<\gcd(u^M-1,N)<N
\]

holds exactly when \(M\) is divisible by one, but not both, of the two local
orders of \(u\).

The P78 feedback witness gives an exact positive instance. Before feedback,
\(H_0=\langle2\rangle\) has order \(36\) in both hidden components. Feedback
splits an old block and exposes \(u=5\). With

\[
M=\operatorname{lcm}(1,\ldots,9)=2520,
\]

one has

\[
5^M\equiv1\pmod{37},
\qquad
5^M\equiv63\pmod{109},
\]

so the public modular power and gcd return \(37\). Every old
\(h\in H_0\) instead has \(h^M=1\) globally. Thus the new block is essential
for this declared power-contraction channel.

**Algorithmic consequence.** After a split, a smooth power ladder is a real
alternative to uniform subgroup sampling or a cancellation-word search.
The missing all-input theorem must prove that feedback creates a block with a
polynomial-bit local order-divisibility mismatch. No such smoothness law is
known.

### C84 — feedback subgroup gain splits into order and phase branches

**Status:** verifier-backed and promoted as P87 after a corrected hostile
proof-only audit and a proof-blind reconstruction. The first audit correctly
rejected standard smoothness terminology; the corrected theorem uses the
exact full-prime-power bound. No research computation, cross-family audit,
human audit, or literature audit ran.

For a public block \(u\) on \(N=pq\), let its two hidden local orders be
\(r_p,r_q\). A pure power of \(u\) can expose a factor if and only if

\[
r_p\ne r_q.
\]

For

\[
\sigma(r)=\max_{\ell^e\mid r}\ell^e,
\qquad
M_B=\operatorname{lcm}(1,\ldots,B),
\]

the polynomial punctured-lcm bank

\[
\{M_B\}
\cup
\{M_B/\ell^j:\ell^j\le B\}
\]

is complete exactly when the orders differ and

\[
\min\{\sigma(r_p),\sigma(r_q)\}\le B.
\]

This condition is stronger than ordinary \(B\)-smoothness.

Equal local orders define a different branch. Every pure power has
synchronized \(+1\) and \(-1\) status, yet a mixed word with the old
subgroup can still factor. The diagonal \(C_L\times C_L\) construction gives
a maximal abstract example.

**Algorithmic consequence.** Run the punctured power bank after every
feedback split, but do not treat its failure as evidence that subgroup growth
was useless. A phase branch requires a mixed cancellation selector,
additional integer refinement, or a different closure operation. No public
branch detector or all-input source law is proved.

### C85 — redundant canonical residues can cause a literal phase-only expansion

**Status:** verifier-backed and promoted as P88 after a hostile whole-proof
and provenance audit and a proof-blind reconstruction. The finite search is
authenticated discovery evidence only. No cross-family audit, human audit,
or literature audit ran.

At \(N=2047=23\cdot89\), the old canonical endpoint blocks generate
\(H_0=\langle11\rangle\), and 11 has order 22 in both hidden fields. The
feedback pair for \([11^7]_N=1778\) stays inside \(H_0\), and all immediate
sign and difference screens fail. Its integer representative nevertheless
overlaps the old endpoint 312:

\[
\gcd(312,1778)=2.
\]

This exposes a block outside \(H_0\). The block 2 has order 11 in both
hidden fields, so every pure direct-sign power fails. The mixed word succeeds:

\[
\gcd(2\cdot11+1,2047)=23.
\]

**Algorithmic consequence.** Canonical feedback can change the available
subgroup without adding a new residue, and the change can be phase-only. A
power bank on the new block is not a complete post-split policy. This fixed
witness is not hard: trial division of 312 already exposes 2, and no general
mixed-word selector is proved.

### C86 — 2-saturation is only one case of a complete prime-root decoder

**Status:** verifier-backed and promoted as P89 after a hostile proof-only
audit and a proof-blind reconstruction. No research computation,
cross-family audit, human audit, or literature audit ran.

For any public prime \(\ell\), reduce the explicit relation exponent matrix
modulo \(\ell\). Each kernel vector gives an exact \(\ell\)-th root of one
modulo \(N\). Its two hidden identity kernels are linear subspaces. A proper
factor exists exactly when those kernels differ.

For any public kernel basis, all basis vectors and all support-two
combinations form a complete deterministic menu. Its size is

\[
D+(\ell-1)\binom D2.
\]

For a numerically polynomial-size prime, the full decoder has polynomial bit
complexity. At \(N=215\), 3-saturation gives the useful cube root 6 while the
2-saturation relation space is zero. The endpoint sum also factors that
fixed witness, so it proves only an operation separation.

**Algorithmic consequence.** Run small-prime saturation, not only
2-saturation, after relation refinement. The decoder is complete once the
local identity kernels differ. The unsolved source question is whether bare
\(N\) and feedback can make that difference with inverse-polynomial
probability.

### C87 — exhaustive failure is a graph state, and feedback breaks it through a quotient kernel

**Status:** verifier-backed and promoted as P90 after a hostile proof-only
audit and a proof-blind reconstruction. No research computation,
cross-family audit, human audit, or literature audit ran.

A subgroup in which every direct sign test fails is exactly the graph of an
isomorphism between its two hidden projection images. Every element then has
the same order in both fields. Negative signs and all prime-saturation
identity kernels synchronize automatically.

Residue-neutral feedback can still change the state. Its integer endpoints
can split an old integer block and expose factor blocks outside the old
subgroup. For old graph \(H\) and refined subgroup \(K\), put

\[
c=[K:H],\qquad a=[K_p:H_p],\qquad b=[K_q:H_q].
\]

The refined subgroup has exactly

\[
\frac ca+\frac cb-2
\]

positive separators. The graph breaks exactly when \(c>a\) or \(c>b\).
At \(N=2047\), feedback gives \(c=11\) and \(a=b=1\): no local image grows,
but 20 separators appear.

**Algorithmic consequence.** The new information is not a new residue. It
is a new factorization of an integer representative, which changes the
available generators and their cross-field pairing. The hidden quotient
indices do not yet give a public selector or source law.

### C88 — one closing relation adds one prime-root coset

**Status:** verifier-backed and promoted as P91 after a hostile proof-only
audit with scope corrections and a proof-blind reconstruction. No research
computation, cross-family audit, human audit, or literature audit ran.

For a public prime \(\ell\), one appended relation column either leaves the
old relation kernel unchanged or adds exactly one new kernel direction. In
the second case, the new \(\ell\)-th roots form one coset of the old root
image.

After the complete old decoder fails, this whole new coset has a short
complete public test. If the old root image is trivial, test one induced
root. Otherwise, choose any public nonidentity old basis root \(h\) and test

\[
\{s h^t:0\le t<\ell\}.
\]

If the coset leaves the old graph, exactly two of these roots expose a
factor. If it does not, none do.

**Algorithmic consequence.** After each new relation, update every relevant
small-prime saturation decoder incrementally. At most \(\ell\) new gcd tests
are needed. The result does not make a relation close or make its root coset
leave the graph.

### C89 — whole-subgroup contraction solves the bounded pure-phase branch

**Status:** verifier-backed and promoted as P92 after a hostile proof-only
audit and a proof-blind reconstruction. No research computation,
cross-family audit, human audit, or literature audit ran.

For a pure phase extension \(K\) of an old graph \(H\), the quotient
\(K/H\) is cyclic and its order divides \(|H|\). If every full prime-power
component of \(|H|\) is at most \(B\), one punctured least-common-multiple
exponent contracts the full public subgroup to at most \(B^2\) elements and
keeps a factor-bearing phase component.

A public algorithm powers every generator, enumerates each contracted image
with a \(B^2\) cap, and gcd-tests every element. It needs no branch detector
or mixed-word selector. At \(N=2047\), exponent 2520 gives an image of order
121 with 20 positive separators, although every pure power of the new block
2 fails.

**Algorithmic consequence.** The phase route now has a real subgroup-wide
algorithm under an exact bounded-order promise. The remaining gap is to
prove that feedback creates this promise on every input or with useful
probability.

### C90 — bounded subgroup exponent unifies the order and phase decoders

**Status:** verifier-backed and promoted as P93 after a hostile proof-only
audit and a proof-blind reconstruction. No research computation,
cross-family audit, human audit, or literature audit ran.

Let a public subgroup of a two-field unit group contain any positive
separator. If every full prime-power component of its exponent is at most
\(B\), a punctured least-common-multiple power keeps a separator and shrinks
the full image to at most \(B^2\) elements.

The same capped subgroup enumeration therefore handles both unequal-order
and equal-order phase cases. It does not need to know which branch occurred,
which word separates, or the subgroup exponent.

**Algorithmic consequence.** The decoder problem is solved under the
bounded-exponent promise. The open problem is now sharply source-side: bare
\(N\) and feedback must create a factor-bearing subgroup with an accessible
primary component. No all-input law is known.

### C91 — N−1 is a public annihilator for every synchronized graph state

**Status:** verifier-backed and promoted as P94 after a hostile proof-only
audit and a proof-blind reconstruction. No research computation,
cross-family audit, human audit, or literature audit ran.

For a pure phase extension of a graph subgroup of order \(h\), one always
has

\[
h\mid N-1.
\]

Thus the algorithm does not need a smooth old subgroup order. It scans small
primes dividing the public number \(N-1\), removes one controlled prime power,
and enumerates the contracted subgroup with a public cap. For a phase prime
\(\ell\), the exact residual size is

\[
\ell^{H_\ell-C_\ell+2}.
\]

If this size is polynomial, the scan is a deterministic polynomial-time
factor extractor. At \(N=2047\), the public exponent 186 produces an image
of order 121 with 20 separators.

**Algorithmic consequence.** This removes the global smoothness promise from
the pure phase route. The remaining source theorem must show that feedback
creates a strict phase quotient with a small enough prime component and
residual image. This condition is not yet proved for general inputs.

### C92 — N−1 removes every shared local-order component

**Status:** verifier-backed and promoted as P95 after a hostile proof-only
audit and a proof-blind reconstruction. No research computation,
cross-family audit, human audit, or literature audit ran.

For any supplied public subgroup modulo \(N=pq\), power every generator by
\(N-1\). The remaining two hidden projection orders are coprime, and the
powered subgroup is their full direct product. All shared order and graph
correlation disappear.

The image has orders \(A,B\), size \(AB\), and exactly \(A+B-2\) positive
separators. Sampling works when one order is small. Complete enumeration
works when the full image is small.

At \(N=4033\), the exponent \(N-1=4032\) sends the feedback block 5 to an
element with local orders one and three, and one gcd returns 37. At
\(N=2047\), the special phase subgroup is killed, so its puncture 186 is the
correct branch.

**Algorithmic consequence.** The public power gives a canonical normal form
for every post-feedback subgroup. The unresolved case is a full rectangle
whose two coprime hidden orders are both large.

### C93 — if N−1 kills the supplied subgroup, primary punctures are complete under a cap

**Status:** verifier-backed and promoted as P96 after a hostile proof-only
audit and a proof-blind reconstruction. No research computation,
cross-family audit, human audit, or literature audit ran.

The public test that every generator satisfies \(g^{N-1}=1\) is equivalent
to the whole subgroup exponent dividing \(N-1\). If that subgroup contains
a separator, removing one prime power from \(N-1\) preserves an order-prime
separator and kills all other primary components.

For a separator with prime valuation \(C\) inside a subgroup exponent with
valuation \(H\), the surviving group has exponent
\(\ell^{H-C+1}\) and at most \(\ell^{2(H-C+1)}\) elements. A public scan of
small primes and capped subgroup enumeration is therefore complete whenever
that full bound is polynomial.

**Algorithmic consequence.** The algorithm does not need to detect a phase
branch. The remaining gap is to create a separator with a small accessible
primary image. The annihilator test alone does not do this.

### C94 — bare N already supplies the full powered rectangle with constant probability

**Status:** verifier-backed and promoted as P97 after a hostile proof-only
audit and a proof-blind reconstruction. No research computation,
cross-family audit, human audit, or literature audit ran.

For every distinct odd semiprime \(N=pq\), write

\[
g=\gcd(p-1,q-1),
\qquad
A=(p-1)/g,
\qquad
B=(q-1)/g.
\]

The full unit-group image under the public power \(N-1\) is the nontrivial
cyclic rectangle \(C_A\times C_B\cong C_{AB}\), with \(\gcd(A,B)=1\).
A fresh accepted unit maps exactly uniformly to this rectangle. Two
independent samples generate the complete rectangle with probability

\[
\prod_{\ell\mid AB}(1-\ell^{-2})\ge6/\pi^2.
\]

Thus bare \(N\) gives a constant-size public generator source for a
guaranteed factor-bearing subgroup. If a polynomial-time decoder can
localize either hidden axis from any generating list with
inverse-polynomial probability, verified fresh batches give a classical Las
Vegas factorer for distinct odd semiprimes.

**Algorithmic consequence.** The sampler question is solved at the subgroup
source level for this input class. The exact remaining problem is axis
localization when both coprime hidden orders are large, or a feedback step
that exposes an axis before stable normalization. The result does not supply that decoder, handle
other composite forms, or prove a factoring algorithm.

### C95 — repeated N−1 normalization erases feedback outside one stable core

**Status:** verifier-backed and promoted as P98 after a hostile proof-only
audit and a proof-blind reconstruction. No research computation,
cross-family audit, human audit, or literature audit ran.

For a distinct odd semiprime, let \(S=G^{N-1}\) be the full P97 powered
rectangle and let

\[
g=\gcd(p-1,q-1).
\]

Then

\[
G/S\cong C_g\times C_g,
\qquad
g\mid N-1.
\]

Thus every feedback supergroup \(S\le K\le G\) adds only a quotient killed
by the public exponent \(N-1\). After at most
\(n=\lceil\log_2(N+1)\rceil\) repeated powers, every such \(K\) has the same
image

\[
T\cong C_{A_*}\times C_{B_*},
\]

where \(A_*,B_*\) are the parts of the P97 local orders coprime to \(N-1\).
Every exponent whose prime divisors occur in \(N-1\) is an automorphism on
\(T\) and preserves both hidden identity tests.

There are distinct-prime semiprimes with both stable orders arbitrarily
large. When \(\gcd(AB,g)=1\), one \(N-1\) power already sends every
feedback supergroup back to the original rectangle \(S\).

**Algorithmic consequence.** The \(4033\) and \(2047\) witnesses use
transient components. They do not test the stable hard case. A feedback
algorithm must factor before the transient part dies, use canonical integer
information without only \(N-1\)-smooth powers, or add a non-power axis
decoder. This is a proved boundary, not a factoring result.

The final candidate, hostile audit, proof-blind statement, and proof-blind
reconstruction have SHA-256 hashes
`6c9d9166ca335d115fab18bef6c7c7d90a4bafd7aee3789a071618f6a3f918c0`,
`b64ae5e9d2365002d55571b17578a93e75a88a836ee7bd9f983b75e837ac739b`,
`fa3b1b9f81e14b8c054a0b8b9b0f589781f46615277cf12adc25da98ee5a6cc7`,
and
`1e5ddb53a9b14e3bd020d55ad5771e672cc10a0f0b03f624bc055edaed21df17`.

### C96 — bare N already supplies full unit-group generators

**Status:** verifier-backed and promoted as P99 after a hostile proof-only
audit and a proof-blind reconstruction. The final candidate includes the
audit's two wording corrections. No research computation, cross-family
audit, human audit, or literature audit ran.

For every \(N\), a batch of
\(n=\lceil\log_2(N+1)\rceil\) exact uniform nonzero residues has probability
at least one absolute constant of either finding a proper factor by gcd or
generating the complete unit group \(G_N\). For a distinct odd semiprime,
three raw units generate \(G_N\) with probability at least
\(1/(\zeta(2)\zeta(3))\).

The complete unit group contains a factor-revealing element for every
composite \(N\). However, the generator batch does not give a public word
for such an element. Conditioned on full generation, later multiplicative
feedback cannot enlarge the abstract subgroup. Its possible gain is to
make one already-contained residue usable as a named integer, block, or
known relation.

**Algorithmic consequence.** The missing result is not a novel generic
subgroup sampler. It is a polynomial-time factor localizer on a generating
list, or a feedback progress law that creates public representation access
with inverse-polynomial probability. P99 supplies neither and does not prove
a factoring algorithm.

The final candidate, hostile audit, proof-blind statement, and proof-blind
reconstruction have SHA-256 hashes
`90a4a39313544a554201a463066f539c16f2f2dc09aef4e2dbfb135c5e42bb34`,
`7d98b6232cbd5dc89271e53b87f526623d39c40dfd54af546e14f99aac014c4f`,
`a9ddb299aee512ec028cd8ed52c631f86675e2d134b2aa1e3c8b2c80c1f387bb`,
and
`6857799dc1aa91aeb87336a8586ae9eeb074ee6d64c162348aee7ac1c1e80030`.

### C97 — feedback progress has two exact presentation gates

**Status:** verifier-backed and promoted as P100. Two earlier versions
failed hostile audit. The corrected theorem passed a fresh hostile audit
and a proof-blind reconstruction. No research computation, cross-family
audit, human audit, or literature audit ran.

Let \(E\) be the known relation matrix, and let \(\Delta\) be the exact
exponent map after block refinement. Modulo a prime \(\ell\), refinement
creates a new known saturation dependency exactly when

\[
\operatorname{im}E\cap\ker\Delta\ne0.
\]

After this update, a new relation column \(u\) creates one new dependency
exactly when \(u\) is in the old column span. A fresh cofactor with exponent
one prevents closure for every prime on that step. Many relations with
distinct stable private rows still create no dependency. They help only
after a later relation reuses a row, or a refinement opens the multiplicity
gate.

On P99's full-group source event, feedback cannot enlarge the abstract
subgroup. Its possible value is the new public presentation: named blocks,
block splits, and known relation cycles. A nonclosing relation cannot always
be discarded, because it can be the first half of a later closure.

**Algorithmic consequence.** A feedback algorithm must track exponent
refinement and relation incidence. It must prove an inverse-polynomial law
for a multiplicity event or a closing cycle. Counting relations, sampling
the already-full subgroup, or applying one final gcd is not enough. Even a
closing cycle gives only a candidate root coset; it need not give a factor.

The corrected candidate, final hostile audit, proof-blind statement, and
proof-blind reconstruction have SHA-256 hashes
`1992f91ad7a4d3dce8dd51836098f0f7dce2411dc043a055fa7f1363463af2d1`,
`77559859ca5a1f642a3101d531b770955beb68871aeb7df3a2cb1a8931265664`,
`69229c3b4e2590812dc8bf45aa536f8837b337107957f3ac2914956879067def`,
and
`2f4a28fa711707c7767ce1d13bf5a197eeb830d64c64a6ef44cbe02f6ae6894b`.

### C98 — a retained relation cycle factors the stable input 2773

**Status:** verifier-backed and promoted as P101 after hostile audit and
proof-blind reconstruction. No cross-family audit, human audit, or literature
audit ran.

At \(N=2773=47\cdot59\), the two canonical-inverse relations

\[
P_1=3\cdot43^2,
\qquad
P_2=3\cdot842^2
\]

have the same nonzero square class. Each relation is nonclosing by itself.
After the first is retained, the second closes. Their exact root gives the
two factors. If the first relation is deleted as an unsuccessful probe, the
cycle is lost.

This proves that amortized relation state can do more than one local scalar
test. The exhaustive discovery scan costs order \(N\), so it does not give a
polynomial selector for the second relation.

### C99 — canonical reduction changes relation access without adding a modular element

**Status:** verifier-backed and promoted as P102 after two failed wording or
counting rounds, a fresh hostile re-audit, and proof-blind reconstruction. No
cross-family audit, human audit, or literature audit ran.

For the first \(2773\) relation, the public subgroup is
\(H=\langle3,43\rangle\). The useful endpoint \(842\) is outside \(H\), but
the canonical word

\[
[3^{99}43]_N=1263
\]

and its inverse \(1684\) both lie in \(H\), while their integer product is the
same useful relation \(3\cdot842^2\). Thus the residue subgroup does not gain
a new element. The algorithm gains a new integer presentation and a new
decoder relation.

A target-free \(145^2\)-word menu finds this presentation on the fixed input.
Raw products below \(N\) do not. This is the first exact witness where
canonical presentation feedback makes the relevant algorithmic difference
inside the old subgroup. The \(n^2\) bound was post-selected after a full
subgroup scan, so the all-input progress law remains open.

### C100 — the one-seed presentation rule fails even on its full old subgroup

**Status:** verifier-backed and promoted as X68 after hostile audit and
proof-blind reconstruction. No cross-family audit, human audit, or literature
audit ran.

The F96 \(n^2\) selector is not an all-input rule. At the stable semiprime

\[
N=253=11\cdot23,
\]

the public seed \(3\cdot13^2=1+2N\) gives
\(H=\langle3,13\rangle\) of order 110. The declared \(65^2\) word menu covers
all of \(H\), not only a small part. No residue in \(H\) gives a distinct
canonical relation in the seed's square class.

This kills exponent-bound inflation as the repair. The input has the small
factor \(11<n^2\), so it does not kill a trial-division hybrid. The next
materially new test must use more than one seed or square class, or must first
change the integer block presentation.

### C101 — a public feedback batch can factor only after a 166-value joint decode

**Status:** verifier-backed and promoted as P103 after hostile audit and
proof-blind reconstruction. No cross-family audit, human audit, or literature
audit ran.

At the stable trial-hard input

\[
N=202{,}537{,}109=10{,}267\cdot19{,}727,
\]

one public one-round rule starts from seeds 2 through 28 and processes 27
canonical two-block trajectories. It receives only \(N\). All 12,549
individual canonical-inverse sign screens fail.

After exact-value deduplication and factor-free gcd refinement, the retained
9,414 relation values have binary rank 8,926 and kernel dimension 488. A
public kernel-basis vector with 166 distinct values gives a mixed square root
and the two factors. An independent online replay first finds a useful
166-value dependency at occurrence 5,616. No useful support-one, -two, or
-three dependency occurs in that prefix.

**Algorithmic consequence.** This is the first stable witness here where the
successful operation is genuinely amortized. No new scalar works alone. The
algorithm keeps many failed integer presentations and jointly closes their
square classes. The missing result is an all-input law that forces such a
non-global circuit in polynomial work.

### C102 — canonical power trajectories have duplicate-root and private-row traps

**Status:** verifier-backed and promoted as P104/X69 after a corrected hostile
re-audit and proof-blind reconstruction. No cross-family audit, human audit,
or literature audit ran.

If \(N=(a^m-1)/k\), the canonical pairs
\(a^r,a^{m-r}\) can all have the identical exact value \(a^m=1+kN\).
For odd \(m\), duplicate dependencies then have root \(+1\). The stable
input \((3^{17}-1)/2\) gives an exact trial-hard example with a complete
\(n^2\)-range seed trajectory and no direct factor or block split.

An infinite CRT family shows the opposite trap. It gives
\(\Theta(\sqrt{\log N})\) consecutive canonical relations whose columns all
have private odd-prime rows. They are independent.

**Algorithmic consequence.** Do not count records or raw nullity. Count
distinct exact values, refined rank closure, and non-global root image. The
live question is whether the actual multi-seed feedback source closes private
rows with an inverse-polynomial all-input law.

### C103 — the 166-value F98 certificate is one indivisible cross-trajectory circuit

**Status:** verifier-backed and promoted as P105 after two failed wording
audits, a final hostile re-audit, and proof-blind reconstruction. No
cross-family audit, human audit, or literature audit ran.

The 166 selected F98 relation values have a 230-by-166 prime-parity matrix of
rank 165. All 166 columns give the unique nonzero dependency. Removing any
one value destroys it. The shared-prime graph is connected, even without
the prime-2 row. The values come from one seed relation and 165 feedback
relations across five active-pair families and eight oriented trajectories.

**Algorithmic consequence.** The successful event is not one lucky identity.
It is a joint circuit made from many individually useless presentations. The
next theorem must force a polynomial-size parity core and then prove that its
root is not globally \(\pm1\). The fixed input does not provide that theorem.

### C104 — the factor-free decoder exposes the exact hidden-prime core

**Status:** verifier-backed and promoted as P106 after hostile audit, a
wording correction, fresh re-audit, and proof-blind reconstruction. No
cross-family audit, human audit, or literature audit ran.

For any frozen finite endpoint batch, P66 gcd refinement preserves every
hidden prime-parity row. At pairwise-coprime termination, the public masks of
the nonsquare blocks are exactly the distinct nonzero hidden prime rows.
Thus public and factor-assisted matrices have the same rank, kernel,
degree-one core columns, and column components.

Degree-one peeling preserves the complete kernel and has one
order-independent terminal core. It is not safe as permanent online
deletion, because a later relation can reuse a current private row.

On the F98 batch, public peeling compresses 9,414 columns to 1,781 without
losing any of the 488 dependencies. The 166-value factor certificate remains
inside the core.

**Algorithmic consequence.** The decoder side is complete and factor-free.
The only decisive gap is now the source: force a rank-deficient core and a
non-global root on every input in polynomial work.

### C105 — raw carry coverage is public, but carry frequency is not progress

**Status:** verifier-backed and promoted as P107 after hostile audit, corrected
re-audit, proof-blind reconstruction, and an amended-boundary proof-blind
re-audit. No cross-family audit, human audit, or literature audit ran.

For any frozen endpoint batch and any explicit exposure product \(E\), gcd
saturation of the P106 terminal blocks recovers exactly the distinct hidden
prime-parity masks whose primes divide (E). No endpoint factorization is
needed.

On the F98 circuit, raw carry exposures from the full generated batch already
span rank 165, equal to the complete circuit. Carry edges internal to the 166
selected columns have rank only 54. Thus the useful coverage is a batch
reservoir effect, not a local edge explanation.

The F99 private-row family has a zero carry at every step but exposes only the
prime 2. Its private rows remain full rank. Carry frequency alone therefore
forces neither a dependency nor a non-global root.

**Algorithmic consequence.** Carry coverage can now be measured publicly.
The source theorem must force full coverage, rank defect, and mixed root signs.
Counting zero carries does none of these.

### C106 — two useless layers can create a useful root only together

**Status:** verifier-backed and promoted as P108 after a hostile factor-free
audit and an independent proof-blind reconstruction. No cross-family audit,
human audit, or literature audit ran.

At \(N=3{,}241{,}632{,}473\), the frozen relation layer has seven
dependencies and all of their roots are global $+1$. The appended layer is
independent when decoded alone. After global exact-value deduplication, their
union gains 11 dependency directions that cannot come from either layer by
itself. The normalized root image of this cross-layer quotient has rank one.

A factor-free hostile verifier found a useful 363-value dependency. A
proof-blind decoder independently found a different 367-value dependency.
Both give the same non-global root and the factors 79,043 and 41,011. Every
direct endpoint screen before the joint decode is nonproper.

**Algorithmic consequence.** This is a genuine stateful gain. The appended
records do not add a useful scalar and do not enlarge the abstract unit group.
They change the square-root directions that the retained relation state can
decode. The missing theorem is still source-side: force a nonzero normalized
root image on every input in polynomial work.

### C107 — a complete fixed source removes the hidden stop and support choices

**Status:** verifier-backed and promoted as P109 after a hostile monotonicity
audit and an isolated proof-blind full-source reconstruction. No cross-family
audit, human audit, or literature audit ran.

First-occurrence exact-value coordinates are append-only. An old dependency
extends by zeros and keeps the same exact root. The normalized root class is a
linear map on the binary kernel. Therefore any complete kernel basis must show
a useful class when one exists.

For $N=3{,}241{,}632{,}473$, an independent decoder ran every position in
the fixed source. It used no success stop and no advised dependency. It kept
12,962 distinct nonunit values, found rank 12,923 and nullity 39, and tested
all 39 basis roots. Eleven roots factored $N$ into 41,011 and 79,043.

**Algorithmic consequence.** The earlier F111 success was not caused by a
hidden stopping rule or a supplied support. The remaining postselection is
the source design itself: the fixed pair $(2,4)$ was chosen after earlier
experiments. We still need an input-independent reason that a polynomial
source creates a nonzero normalized root image.

### C108 — live candidate: feedback changes the future source grammar

**Status:** open algorithm candidate. It is not a proved progress law. The two
GPT Pro comments supplied useful prompts, but this version keeps only claims
that survive P100 and the new audits.

The proposed 2-saturation decoder is not the missing component. For square
roots, P66 already computes the equivalent complete parity kernel without
factoring endpoints. The open problem is the adaptive source that feeds it.
The proposed CRT beam can order probes, but its score pruning has no lossless
dominance theorem. It remains a heuristic search tool, not an algorithm proof.

Maintain three forms of public state:

1. pairwise-coprime integer blocks that can be used as named word generators;
2. every distinct retained exact relation, with its source record;
3. the complete factor-free square-class kernel and normalized-root image.

For a fixed polynomial menu, form short words in the current blocks. Reduce a
word modulo $N$, take its canonical inverse, and run the direct gcd screens.
Use gcd refinement to split old blocks. A split changes the generators that
future words can use, even when the selected residue was already in the old
abstract modular subgroup. Retain every new exact relation. Do not delete it
only because it fails to close now; P100 proves that a later column can close
against it. After each split or new column, update the complete decoder.

A split alone cannot improve the decode of the old frozen columns. P106
already computes their complete kernel. The split matters only when it changes
which future relations the algorithm can generate. This is the exact boundary
between a cosmetic refinement and real feedback.

This is an algorithm-level change, not a new scalar identity. A block split
changes the next source menu. A retained relation changes the later
cross-layer kernel. The 4033 witness proves the first effect on a fixed state.
P108 proves the second effect on a fixed state.

The candidate has polynomial explicit cost when word support, exponent range,
round count, block count, and retained relation count have fixed polynomial
caps. The missing theorem is not the cost bound. It is the progress law:
before a factor is found, some polynomial menu must cause a useful block split
or a new nonzero normalized-root direction with inverse-polynomial frequency.
No such law is known. F118 first seeks a larger input where the complete
nonadaptive all-pairs source is null. Only such a null can show whether the
recursive block update adds a new capability rather than rediscovering an
ordinary relation-collection success.

### C109 — the fresh 54-bit success does not need a hidden stop or support

**Status:** verifier-backed and promoted as P110 after a hostile exact-value
audit and an isolated proof-blind reconstruction. No cross-family audit,
human audit, or literature audit ran.

For $N=12{,}800{,}004{,}879{,}996{,}637$, the fixed complete source has
8,348,507 positions and receives only $N$. An isolated replay regenerated an
initial prefix of 1,336,218 positions. It retained 771,082 first residues and
projected them to 622,151 distinct nonunit exact values. A 6,486-value exact
dependency gives a non-global root and the factors 80,000,059 and 159,999,943.

First-occurrence projection and append monotonicity prove that the dependency
persists to the end of the fixed source. A complete factor-free decoder must
find some useful basis vector. Thus the no-stop, no-support algorithm is
certified for this one input, although the full source and decoder were not
executed.

**Algorithmic consequence.** The 54-bit certificate is not an artifact of an
advised stopping position or supplied support. The unresolved issue is still
uniform source progress. Six registered 54-bit cases are positive finite
controls, but no theorem says that the same fixed source works on every
non-perfect-power input.

### C110 — four harder 58-bit frozen-global cases close only after cross-pair accumulation

**Status:** preregistered factor-assisted finite evidence. The run is not a
factor-free certificate and is not promoted to `PROVED.md`.

F118 selected the first four 58-bit distinct semiprimes in its frozen corpus
whose old source had positive kernel nullity but zero normalized-root image.
The four frozen kernels already had 9,031 to 20,903 dependency directions, all
with global roots. The fixed all-pairs continuation then found the first
non-global basis root after 2.10 to 2.14 million source attempts, at pairs
$(6,44)$, $(6,47)$, $(6,49)$, and $(6,50)$. No direct residue or endpoint gcd
gave a factor.

At the successful positions, the retained relation counts were 1.36 to 1.41
million and the kernel nullities were 304,372 to 316,596. In each case, every
earlier fundamental root was global and the next root was non-global. This
shows again that large nullity alone is not useful progress.

**Algorithmic consequence.** The registered 58-bit corpus produced no
complete-source null, so its feedback gate did not open. Running feedback on
these positive cases would not test whether feedback adds an algorithmic
capability. The finite result supports cross-pair accumulation, but it gives
no all-input law and no public dependency support.

### C111 — cross-pair words can retain a large independent private-row block

**Status:** verifier-backed and promoted as P111/X71 after one scope
correction, a clean hostile re-audit, and a proof-blind reconstruction by a
different construction. No cross-family audit, human audit, or literature
audit ran.

Prime incidence in canonical-inverse values is exactly carry congruence. Two
values with carries $k\ne\ell$ can share a prime only if that prime divides
$k-\ell$. This gives exact row-degree and private-row tests.

An infinite trial-hard distinct-semiprime family contains
$\Theta(n/\log n)$ genuine exponent-two cross-pair exact values whose columns
each have a different private valuation-one prime. The selected columns are
independent. Exact-value deduplication preserves them. Null sign screens are
proved for each named residue, not for a different earlier residue with the
same exact value.

**Algorithmic consequence.** Cross-pair provenance and polynomial relation
count do not force closure. This does not refute the complete fixed source:
unselected carries can reuse the protected rows. The exact remaining gates
are stable full-source privacy on the negative side, or rank closure followed
by a non-global root on the positive side.

### C112 — one canonical prime row can stay private in the complete universe

**Status:** verifier-backed and promoted as P112/X72 after a fresh hostile
audit and a proof-blind reconstruction. The reconstruction passed with two
notation and definition corrections. No cross-family audit, human audit, or
publication-level literature review ran.

After global exact-value deduplication, a prime row $r$ has degree at most

\[
\left\lfloor\frac{N-1}{r}\right\rfloor.
\]

The proof assigns each distinct $r$-divisible exact value to a different
endpoint below $N$ that is divisible by $r$. Thus every present row with
$r>(N-1)/2$ is permanently private inside the complete canonical universe.

The trial-hard distinct semiprime

\[
N=2{,}000{,}887{,}089{,}301
=1{,}000{,}289\cdot2{,}000{,}309
\]

has the certified prime

\[
r=(N+1)/2=1{,}000{,}443{,}544{,}651.
\]

Seed $2$ has inverse $r$ and exact value $N+1=2r$. Its $r$ row is
private against every canonical exact-value column. Both direct sign screens
are null.

**Algorithmic consequence.** A complete canonical source does not force
every relation row to be reused. This does not prove source failure. A private
row and its column peel away exactly. All dependencies and useful roots on the
remaining columns stay unchanged. Feedback through a different named integer
representation also remains outside this theorem.

### C113 — the 4033 feedback witness changes names, not the complete relation set

**Status:** exact F121 candidate result. It is not promoted because no fresh
hostile audit or proof-blind reconstruction ran.

At $N=4033$, the restricted P78 state makes feedback look useful: endpoint
refinement exposes a new named block. The complete fixed static source removes
that advantage. It already contains the same exact relation values. Adding the
hypothetical feedback block produces 50 new residue presentations but zero new
exact-value columns. The static source also has the square
$12100=110^2$, and its sign gcds expose 109 and 37.

**Algorithmic consequence.** The small witness proves that feedback can change
the next word grammar relative to a restricted state. It does not prove that
feedback adds a capability beyond the complete static source. This is the
correct limit of the 4033 example.

### C114 — a private row can coexist with an early public static factor

**Status:** registered F122 prefix evidence. It is not promoted as a completed
source run. The first run was interrupted. The retry was stopped at about
993 MB of memory, and both partial runs are preserved.

On the P112 semiprime, the complete static source still contains the private
seed row. Every observed dependency excludes that column, as P112 requires.
However, a fixed public word already gives a direct factor at attempt 166,901:
pair $(2,12)$, exponent 1012, and orientation
$[2\cdot12^{1012}]_N$. Its two canonical endpoints have difference gcd
$1{,}000{,}289$ with $N$. The append-only source therefore succeeds even
though the terminal enumeration was stopped.

**Algorithmic consequence.** Stable privacy defeats universal row reuse, not
factoring. It also closes the feedback gate on this input: feedback cannot be
called a rescue when the static source already succeeds. A valid feedback
test still needs a trial-hard input on which the complete static source is
null.

### C115 — four canonical carries can form a CRT rank-mismatch splitter

**Status:** self-audited F123 candidate. The result was supplied after a GPT
Pro brainstorm and registered retrospectively. The exact supplied verifier
passes. The root agent also checked the determinant identity and gcd equality
on 3,571 small cases. No fresh hostile audit, proof-blind reconstruction,
cross-family audit, human audit, or publication-level literature audit ran.

For a public unit \(a\bmod N\), let

\[
c_j=[a^j]_N,\qquad
w_j=[c_j^{-1}]_N,\qquad
\kappa_j=(c_jw_j-1)/N
\]

for \(1\le j\le4\). Define

\[
\Omega_N(a)=
\kappa_4-\kappa_1+(1+a+w_1)(\kappa_2-\kappa_3).
\]

The determinant of the four rows

\[
(1,c_j,w_j,\kappa_j)
\]

satisfies

\[
\det L_N(a)\equiv
(a-1)^3(a+1)w_1^2\Omega_N(a)\pmod N.
\]

Hence, when \(\gcd(a(a^2-1),N)=1\),

\[
\gcd(\det L_N(a),N)=\gcd(\Omega_N(a),N).
\]

The proof is the order-three recurrence shared modulo \(N\) by
\(1,a^j,a^{-j}\), followed by one determinant-preserving row elimination.
The argument does not need the source note’s squarefree restriction.

The exact finite certificate is

\[
N=4{,}840{,}987=1{,}847\cdot2{,}621.
\]

On the public source \(2\le a\le92,\ 1\le j\le4\), all 364 direct
canonical-inverse screens are null. Exact-value deduplication leaves 240
columns. Their gcd-free parity matrix has rank 240 and zero kernel. At
\(a=68\),

\[
\Omega_N(68)=-16{,}803{,}964{,}880,
\qquad
\gcd(\Omega_N(68),N)=2{,}621.
\]

The corresponding local matrix ranks are four modulo 1,847 and three modulo
2,621.

**Algorithmic consequence.** This is a real finite separation from the named
direct and exact-square channels. It is not a feedback-state transition. It
uses the same canonical \((c,w,\kappa)\) data, but it creates no block split,
new named generator, later source menu, or cross-layer relation. The
determinantal language is a valid GCT-inspired analogy, but the proof is an
elementary recurrence, determinant, and gcd. F03, F04, and Inspiration A2
already contain the broader CRT rank-mismatch template.

**Exact remaining gap.** One of the 91 displayed seeds succeeds. This can be
consistent with accidental divisibility at the small certificate scale. No
theorem gives inverse-polynomial asymmetric vanishing, an infinite successful
family, or a public weight selector. The next valid test must freeze the seed
and weight menus before a balanced corpus and compare against a matched random
scalar baseline. A feedback-specific claim additionally needs a first
successful determinant that depends essentially on a feedback-created block
or trajectory.

### C116 — quasipolynomial time permits complete polylog-support word closure

**Status:** candidate cost lemma after a kill-first review. No all-input source
theorem or registered expanded-source run exists.

Let \(n=\lceil\log_2(N+1)\rceil\). Start from the canonical inverse relations
for the public seeds \(2,\ldots,n\), after the usual direct gcd checks. Refine
all integer endpoints into a pairwise-coprime, perfect-power-free public block
basis \(q_1,\ldots,q_M\). Their total endpoint bit length is \(O(n^2)\), so
\(M=O(n^2)\).

Set

\[
B_q=(n^2+1)\lceil\log_2 n\rceil,
\qquad
d=2\lceil\log_2(n+1)\rceil.
\]

Enumerate every residue

\[
c=\left[\prod_{j=1}^{M}q_j^{e_j}\right]_N,
\qquad
0\le e_j\le B_q,
\qquad
|\{j:e_j\ne0\}|\le d.
\]

For each distinct residue, compute its least positive inverse \(w\), screen
\(\gcd(c-w,N)\) and \(\gcd(c+w,N)\), retain the distinct exact values
\(P(c)=cw\), and run the complete P66 factor-free square decoder.

The source size satisfies

\[
\sum_{s=0}^{d}\binom Ms(B_q+1)^s
\le (d+1)(M(B_q+1))^d
=2^{O((\log n)^2)}.
\]

Each retained exact value has \(O(n)\) bits. P66 is polynomial in the explicit
list size. The full construction and decode therefore have deterministic
quasipolynomial bit complexity.

The support cap contains each prior small-seed-pair word because an integer
at most \(n\) uses at most \(\log_2 n\) nontrivial blocks. The coordinate cap
contains its expanded exponents through the old \(n^2\) trajectory bound. It
also contains the prior initial-basis support-two trajectories. The earlier
proposal \(e_j\le n^2\) did not contain all expanded small-seed-pair records;
the factor \(\lceil\log_2 n\rceil\) is necessary for that stated inclusion.

**Non-trivial point.** Quasipolynomial time permits lossless enumeration of
all polylog-support words and lossless retention of a dense final relation.
The final dependency can use quasipolynomially many columns; the algorithm
finds it by linear algebra and does not enumerate dependency subsets.

**Exact remaining gap.** No theorem shows that the retained matrix closes.
If it closes, no theorem shows that its normalized-root image is non-global.
Generic counting cannot prove either gate because a quasipolynomial list is
still much smaller than a hidden group of size \(2^{\Theta(n)}\), and exact
values can carry private prime rows. The next decisive result is an actual-
\(N\) complete-source null, or a carry-reuse theorem that forces both rank
closure and a non-global root.

### C117 — the rational-prime endpoint supergroup is too coarse for the first kill

**Status:** completed registered F124-D01 finite evidence. No hostile replay
or proof-blind reconstruction ran because the decisive decoder gate was empty.

F124 enlarged the initial public block subgroup to the group generated by
every rational prime divisor of every seed endpoint. A null for this
factor-assisted supergroup would have refuted every static support and
exponent cap on the same input.

The fixed scan processed 69,060 balanced, trial-hard semiprimes. No supergroup
met the preregistered size cap 32,768. The smallest size was 75,900. Of all
cases, 69,032 supergroups were the full unit group and 28 had index two. Thus
no full subgroup or P66 decode ran.

**Exact consequence.** The test found no source null. Splitting every public
block into its unknown rational prime factors usually expands the state to the
full unit group, so this supergroup is not a useful small-state diagnostic on
the declared corpus. A retry must use the exact public gcd-free blocks, an
algebraic direct-null test that does not enumerate the group, or a different
source obstruction. Raising only the enumeration cap does not address the
main loss of structure.

### C118 — fixed seed carries can be programmed independently

**Status:** promoted as P113 after a hostile audit and independent proof-blind
reconstruction. No cross-family or human audit ran.

For any fixed finite list of distinct prime seeds \(g_i\) and admissible
carries \(1\le k_i<g_i\), CRT and primes in fixed arithmetic progressions
give infinitely many balanced semiprimes \(N=pq\) with \(p,q>n^2\) for which

\[
g_i^{-1}{}_{\rm can}={1+k_iN\over g_i}.
\]

All direct endpoint signs can remain null. If the carries are distinct, each
selected exact value can also receive a prescribed valuation-one prime row
that is private among the selected columns.

**Exact consequence.** Seed status and canonical inversion impose no
universal identity or reuse law on a fixed handful of carries. A positive
F26-Q theorem must use a source whose size grows with \(n\), interactions
between multiplicative words, or later canonical refinement. P113 does not
control the growing word source, and its private rows can be reused by other
columns.

### C119 — multiplicative rectangles give a new carry-rank decoder

**Status:** promoted as P114 after a hostile audit and independent proof-blind
reconstruction. Proof-only; no finite sweep is used as evidence. No
cross-family or human audit ran.

For a multiplicative rectangle

\[
x_{ij}=[u\alpha^i\beta^j]_N,
\qquad i,j\in\{0,1\},
\]

let \(y_{ij}\) be the canonical inverse and \(\kappa_{ij}\) its carry. Define

\[
\Omega_{\square}
=(\beta-\alpha)(\kappa_{11}-\kappa_{00})
+(\alpha\beta-1)(\kappa_{10}-\kappa_{01}).
\]

Under the explicit unit conditions, the determinant of the four rows
\((1,x_{ij},y_{ij},\kappa_{ij})\) is a unit multiple of
\(\Omega_{\square}\) modulo \(N\). Their gcds with \(N\) are equal. F123 is
the slice \(u=\alpha=t,\ \beta=[t^2]_N\).

If F26-Q has \(Q\) canonical word residues, all ordered triples and their
four corners cost \(Q^3\), still quasipolynomial. This adds a real cross-word
decoder to the candidate algorithm. It must run before exact-value
deduplication.

**Exact remaining gap.** No theorem gives one asymmetric local-rank rectangle
on every input, or with inverse-quasipolynomial probability. The determinant
bypasses the P66 rank and root gates only when its gcd succeeds. A
feedback-specific result still needs a rectangle that essentially uses a
feedback-created block after the full static rectangle source is null.

### C120 — small unreduced rectangles and fixed banks are exact traps

**Status:** promoted as P115 after a corrected hostile audit and a fresh
proof-blind reconstruction. The false V1 endpoint extension and the first
under-specified V2 reconstruction are preserved. No cross-family or human
audit ran.

For an unreduced rectangle \((u,ua,ub,uab)\), divisibility compatibility of
the canonical carries reduces all four carries to three nested digits
\(A,B,T\). The P114 residual becomes

\[
\Omega_{\square}
=u[(b-a)T+(ab-1)(A-B)],
\]

and

\[
|\Omega_{\square}|<2uab\max(a,b).
\]

Thus a residual built from numerically quasipolynomial-size unreduced
operands is eventually too small to contain either hidden factor of a
balanced semiprime. The endpoint signs need the separate bound
\(h>R^6+1\). Under it, all endpoint, prefactor, and residual gcds are null or
global. The original use of \(2R^4<h\) for endpoints was false; the exact
counterexample has \(N=577\cdot587\), corner \(24\), and
\(24^2+1=577\).

For a \(Q\)-entry menu, if \(T_R\) entries exceed \(R\), the raw fraction of
ordered triples that can escape the small residual/prefactor obstruction is
at most \(3T_R/Q\). A stronger threshold gives the same full-channel bound.
Two infinite balanced semiprime families realize \(\Omega=1\) and
\(\Omega=0\). Every fixed literal bank of unreduced rectangles therefore
fails on all sufficiently large balanced inputs.

**Exact consequence.** P114 cannot get an all-input law from small integer
rectangles, a fixed bank, or visible unreduced carry algebra. A surviving
selector must use numerically large or wrapped representatives, or it must
gain from retained multi-relation decoding. The theorem does not bound that
large tail and does not address an adaptive selector or P66.

### C121 — wrapped rectangles contain only floor-curvature information

**Status:** promoted as P116 after hostile audit and fresh proof-blind
reconstruction of a self-contained statement. No cross-family or human audit
ran.

Every wrapped P114 rectangle is the reduction of four raw endpoint products
that are exactly equal. Writing the six direct and inverse floor quotients
explicitly gives

\[
\Omega_{\square}
=N(ab-1)(AR_a-BR_b)+u\Phi_y+z\Phi_x.
\]

The first term is irrelevant modulo \(N\). Thus a local rank mismatch is
exactly an asymmetric vanishing of

\[
u\Phi_y+z\Phi_x.
\]

For fixed small \(a,b\) and uniform \(u\), the floor pattern has at most
\(a^4b^4\) cases. Each non-global case reduces to a quadratic with at most
two roots modulo each hidden prime. Its proper-hit probability is

\[
O(a^4b^4/p)
\]

on \(N=pq\), \(p<q\). Quasipolynomially many uniform samples remain
insufficient when the multipliers have quasipolynomial numerical magnitude.
This does not cover an adaptive selector.

Large canonical representatives near \(N\) can still be signed-small. After
multiplication by \(L=sa_0b_0\), their residual becomes one explicit integer
of magnitude polynomial in \(s,a_0,b_0\). The same bound kills the endpoint
and prefactor screens. There is also an infinite fully wrapped family with
\(u=N-s\), \(N\equiv-1\pmod{sab}\), and \(\Omega=0\) exactly.

**Exact consequence.** Visible wrap and canonical magnitude are not source
progress. The surviving determinant route needs genuinely large least-signed
multipliers, plus a law that makes their two floor curvatures vanish on only
one hidden CRT axis. No such law is known. This strengthens the decision to
keep retained cross-relation decoding as the main route and P114 as a side
channel.

### C122 — support-layer progress has two separate gates

**Status:** promoted as P117 after a corrected hostile audit and a fresh
proof-blind reconstruction. No cross-family or human audit ran.

Intrinsic support must be assigned to an exact value by minimizing over all
declared presentations of both endpoints before exact-value deletion. With
that definition, the dependencies that first require layer (s) form

\[
C_s\simeq
\operatorname{im}U_{s-1}\cap\operatorname{im}A_s.
\]

Their root information is not an absolute map in general. It is the exact
relative quotient

\[
\operatorname{im}\bar\rho_s
=H_{\le s}/(H_{\le s-1}+H_s).
\]

Therefore permanent retention and a positive cross-quotient dimension are
not enough. A successful support layer must pass two independent tests:

1. old and new columns must reuse parity rows and create a dependency; and
2. the new pure or relative root image must be non-global.

A shared row forces a carry collision modulo that row prime, but the
collision is only necessary. An explicit noncanonical construction has
arbitrarily large cross quotient while every root remains global. This makes
the live F26-Q target precise: canonical carry arithmetic must force both
reuse and sign asymmetry. The theorem localizes that task; it does not solve
it.

### C123 — the adaptive qpoly closure is now one exact finite algorithm

**Status:** promoted as P118 after a hostile audit and a proof-blind
reconstruction. No cross-family or human audit ran.

The static sparse-word proposal has been replaced by a precise adaptive
closure. It keeps two bases separate. The named basis contains only
descendants of the fixed initial endpoint product. The final decoder basis
can contain every novel factor-free block found in the retained exact
relations.

Each stage freezes the named basis, exhausts all support-(L^2) words with
exponents at most (2^{L^2}), inserts all canonical endpoint pairs, retains
all distinct exact values, and only then refines the named basis. A strict
refinement increases the number of descendants of the fixed initial product.
This gives a finite fixed point and the exact bit bound

\[
2^{O((\log n)^4)}.
\]

This is a framework-level algorithm change. Feedback can alter the future
integer grammar, while old relations remain available to later support
layers. It is not only a larger static list or one scalar followed by one
gcd.

**Exact remaining gap.** No theorem forces a split, a parity dependency, or
a non-global root at the terminal state. P117 shows why relation count is not
enough: the terminal source must pass both the row-reuse gate and the
normalized-root gate. A complete terminal null would refute this exact
candidate. An all-input direct-or-root law would complete its splitter proof.

### C124 — a two-relation dependency has only one small-kernel root trap

**Status:** promoted as P119 after a corrected hostile audit and a fresh
proof-blind reconstruction. F131-D01 checks the displayed finite arithmetic.
No cross-family or human audit ran.

For two distinct exact values with square product, write

\[
P_1=sa^2,qquad P_2=sb^2
\]

with common squarefree kernel (s). Their joint root is global exactly when
(a+b=N). This forces (s\in\{1,2,3\}). Therefore a weight-two parity
closure with (s\ge5) always gives a factor.

The endpoint screens do not exclude the trap. The exact input
(N=9407=23\cdot409) has two nonsquare values with common kernel (2), all
four endpoint gcds equal to one, and joint root (-1\). An unconditional
nonsquarefree arithmetic-progression family has the same behavior.

**Exact consequence.** At weight two, the P117 root gate is almost solved:
only three public squarefree kernels can synchronize globally. The main hard
gate remains creation of a duplicate parity column. If closure lands in one
of the three small kernels, the algorithm needs another feedback step or a
larger dependency.

### C125 — all-block unary feedback is affordable, but reuse is not closure

**Status:** promoted as P120 after a preserved failed hostile audit, a fresh
hostile re-audit, and an independent proof-blind reconstruction. No
cross-family or human audit ran.

After the complete P118 transcript, permanently name every factor-free block
from every endpoint. For \(L^2\) rounds, feed every current block power through
canonical inversion, keep every endpoint presentation and first exact value,
then refine in one batch. The accumulated state and the final P66 decode cost

\[
2^{O((\log n)^4)}.
\]

This is a real algorithm change. A probe-only cofactor that was not a P118
generator can become a generator in a later round.

The exact exponent-one accounting is less positive. If a block \(q\) divides
an old value \(1+kN\) and \(q>k\), feeding \(q\) reproduces that old exact
value. A duplicate can still factor through its new endpoint signs, so signs
must run before deduplication. A genuinely new value can cancel the fed row.
Even when it reuses that row, fresh private rows can peel both columns.

The exact splice law says that reuse of a private row only replaces the old
and new parity columns by their symmetric difference. That difference must
still lie in the span of the other columns. Also, a prime row larger than
\((N-1)/2\) is private in the complete canonical universe and cannot be
rescued by any unary schedule.

**Exact consequence.** P120 validates bounded recursive feedback as a
quasipolynomial source operation. It does not validate feedback as progress.
The next source theorem must force reuse at scale and then control the fresh
rows well enough to produce a 2-core or a dependency. P119 handles most of
the root gate only after a weight-two dependency exists.

### C126 — public anchors force polynomial reuse of a covered large row

**Status:** promoted as P121 after an independent hostile audit and an
independent proof-blind reconstruction. No cross-family or human audit ran.

Let \(q<N/n^3\) be a current unit block. If a prime \(r>n^3\) occurs oddly
in \(q\), scan the public prime anchors \(\ell\le n^3\). Their canonical
relations have the exact form

\[
P_N(\ell q)=q(w+NA_\ell),
\qquad w=\iota_N(q).
\]

A primorial and carry-bucket argument proves that either a declared gcd screen
already factors \(N\), or more than

\[
{n^2\over4}
\]

distinct retained exact values have odd valuation in row \(r\). Global
exact-value deduplication cannot remove them. The full anchored all-block
source, including the final P66 decode, still costs

\[
2^{O((\log n)^4)}.
\]

This is the first general positive source-side theorem for the feedback route.
It proves that canonical integer carries from bare \(N\) can force actual
prime-row reuse. It is stronger than a finite witness, abstract subgroup
growth, or a count of generated relations.

**Exact remaining gap.** The new columns can form a star: they share row
\(r\), but each can have a different fresh private row. Such a matrix still
has zero kernel after peeling. The next theorem must force overlap among the
fresh arm rows, release small factors that can become new anchors, or prove a
direct cross-layer closure. P119 controls most of the root gate only after
such closure exists.

### C127 — one star reuses the old row but separates its fresh large rows

**Status:** promoted as P122 after an independent hostile audit and an
independent proof-blind reconstruction. No cross-family or human audit ran.

For one fixed anchor \(q\), write its fresh cofactors as

\[
H_A=w+NA.
\]

Two distinct carry digits satisfy

\[
\gcd(H_A,H_{A'})\le |A-A'|\le B.
\]

Thus primes larger than the anchor range cannot occur in two different fresh
cofactors. In an even star-only dependency, every selected fresh cofactor must
have a \(B\)-smooth squarefree kernel. The full star kernel has at most one
extra odd coset, where the large parity can cancel against the common anchor
\(q\).

This result explains why P121 does not yet give a dependency. P121 forces
many columns to share an old row inside \(q\). P122 proves that the unrelated
fresh large rows on those columns do not share each other inside the same
star. A wide star can therefore peel completely.

The theorem does not kill feedback. An old retained column can close a fresh
row; a private cofactor can become a later generator; and two different stars
do not satisfy the same gcd bound. Exact certificates at \(N=143\) and
\(N=49\) show both escapes.

**Exact consequence.** The next proof must be cross-layer or multi-round.
Within-star amortization is closed. The live target is a forced old/new match,
a same-digit refinement that releases a smaller block, or a cross-star cycle.

### C128 — full-endpoint feedback cuts off; release or width remains

**Status:** promoted as P123 after a passing hostile re-audit and a fresh
statement-only blind reconstruction. Three earlier failed reviews are
preserved. No cross-family or human audit ran.

For a small block \(q<N/B\), an anchored nonzero-digit relation has a new
reciprocal endpoint \(z>N/B\). Feeding the complete \(z\) back through
canonical inversion returns the same exact value. Thus direct endpoint
reversal does not start another small-block generation.

The endpoint presentations still give one real alternative. A heavy
same-digit anchor bucket either releases a proper reciprocal-side block below
\(N/B\), or exhausts that residual into anchor-prime powers. If no bucket is
heavy and \(B=n^3\), one covered old large-prime row occurs in
\(\Omega(n^3/\log n)\) distinct retained values.

This does not prove closure. An explicit quasipolynomial rooted-tree matrix
has the same local width, full column rank, and a complete peeling order. A
selected canonical CRT family realizes two such generations. It does not
control the complete source.

**Exact consequence.** The next theorem must use a proper released block,
retained old/new overlap, different-star overlap, a wrapped or multi-block
operation, or another invariant that forces a rank defect. It must then prove
that the resulting square root is non-global.

### C129 — a released block recenters the parent or becomes smaller

**Status:** promoted as P124 after a passing hostile re-audit and a fresh
statement-only blind reconstruction. The first failed hostile audit is
preserved. No cross-family or human audit ran.

Suppose one feedback relation releases a proper block \(r<N/C\). In the next
anchored star at \(r\), the old parent relation is exactly one virtual digit
\(j\).

- If \(j<C\), every different observed child digit shares no prime larger
  than \(C\) with the old complement.
- If \(j\ge C\), then \(r<q\).
- Two consecutive large-\(j\) transitions contract the active block by
  \(C/(C+1)\).

This is a genuine cross-star theorem. It controls one adaptive generation and
an uninterrupted descent path. It does not bound small-\(j\) interruptions,
branching, non-parent old columns, final rank, or the root image.

**Exact consequence.** Parent-to-child reuse alone is now accounted for. A
positive proof must use non-parent cross-layer overlap, collisions between
different stars, a global potential that limits recentering, or a controlled
multi-block operation.

### C130 — row reuse has an exact carry gate and is weaker than rank closure

**Status:** promoted as P125 after a full artifact hostile audit and an
independent result-only blind reconstruction. The registered Sage verifiers
were reproduced. No cross-family or human audit ran.

Two exact values can share a prime row \(r\) only when their public carries
are equal modulo \(r\). For two stars, this becomes an affine congruence
between their base carries and digits. The present adaptive source has no
theorem that forces these hidden carry-class hits.

The universal version is false. F138 gives 400-bit balanced-semiprime
certificates with a row above \((N-1)/2\) that is private in the complete
canonical-inverse universe. The strongest certificate is already an earlier
F130 word, so it does not refute a globally-new-F133 claim or the complete
source.

Even complete displayed row reuse is not enough. A four-column canonical
matrix at \(N=161\) has no degree-one row but has full column rank.

**Exact consequence.** The target is no longer “reuse all pivots.” It is:
force the required carry collisions, prove a final rank defect after fresh
rows are added, and prove that its normalized root is non-global.

### C131 — linear anchors already force covered-row reuse

**Status:** promoted as P126 after a final hostile re-audit and a fresh blind
reconstruction. This is an exact source-side improvement, not a factoring
algorithm.

The anchor cutoff can be reduced from \(n^3\) to

\[
B=\lceil12n\rceil.
\]

For every current unit block \(q<N/B\) and every odd prime row \(r>B\)
inside \(q\), the complete public anchor scan either returns a factor or
leaves at least two distinct retained values odd in row \(r\). Thus a linear
anchor bank already removes privacy throughout the larger block region
\(q<N/(12n)\).

The endpoint data also gives a sharp three-way outcome. A heavy carry bucket
releases a reciprocal-side block below \(N/B\), exhausts that residual, or
the scan creates more than

\[
\frac{37n}{50\log(13n)}
\]

nonzero carry classes. All but at most one reuse each fixed covered row.
This complete subbank fits inside the existing deterministic
\(2^{O((\log n)^4)}\) source.

The remaining problem did not change: the new columns can still end in fresh
private rows and peel completely. The next result must concern final rank,
not row count.

### C132 — one packed relation can preserve several old rows

**Status:** promoted as P127/X78 after a final hostile re-audit, a fresh
blind reconstruction, and an exact registered certificate.

Value-dependent packing is a real source change. If a public product
\(q<N/B\) contains several large odd rows, all but at most

\[
|\mathcal R_B(q)|<\frac{\log q}{\log B}
\]

occupied carry digits preserve all those rows at once. With two rows globally
private to different old owners, the resulting exact values also survive
global deduplication.

The exact rank test is now known. Cancelling all packed owner pivots reduces
closure to one shifted residual-span condition. Packing does not force it.
At \(N=989\), three nonzero arms preserve both selected rows \(11,17\), but
the full six-column matrix has rank six and peels completely.

Two gaps remain. A suitable multi-owner product below \(N/B\) need not exist.
Even when it exists, fresh inverse-side rows can keep the matrix independent.
The next source change must remove the size gate or force arithmetic overlap
among those fresh residuals.

### C133 — the frozen long small-quotient path fails at the block boundary

**Status:** rejected after hostile audit and recorded as X79. This is a
construction failure, not a theorem that small-quotient paths are short.

F140 programmed exact aggregate gcds and quotient-one transitions. The
integer identities survived. The operational claim did not. At target depth
100, an earlier retained reciprocal endpoint satisfies

\[
\gcd(q_{23},z_{16})=107.
\]

Complete gcd-free refinement therefore splits the proposed future aggregate
`q_23` before it can become one current anchored block. The current source
can feed the terminal factors, but it cannot silently feed their product as
one generator. The audit also found that the label exclusions omitted prime
divisors of the programmed carries.

**Exact consequence.** P124's small-quotient interruption problem remains
open. A materially new retry needs a declared aggregate-feedback operation
with a proved quasipolynomial transcript bound and an invariant that survives
all earlier endpoint refinements. The frozen F140 proof supplies neither.

### C134 — unreduced presentations add a real quasipolynomial relation source

**Status:** promoted as P128 after hostile audit, blind reconstruction, and a
registered replay.

F130 kept only the canonical residue of a sparse word. P128 also keeps the
word's exact factored presentation. For `U=c mod N` and
`w=iota_N(c)`, it retains both `cw` and `Uw`. This does not change the direct
screen, but it can change the exact square-class ledger.

The complete decoder remains deterministic

\[
2^{O((\log n)^4)}.
\]

Algebraically, the new source is exactly the old canonical source plus the
factored square congruences `Uc=c^2 mod N`. This is a strict source expansion
and a standard square-relation decoder.

The large-block theorem is uniform. For every named unit block
`q>=N/(12n)`, squared prime anchors through `n^3` leave more than `n^2/5`
distinct good lifted values that preserve every odd row of `q`, unless an
earlier declared gcd already factors `N` or splits `q`. Together with P126,
the old row-reuse objection is now covered on both sides of the size cutoff.

**Exact remaining gap.** The fresh inverse or residue endpoint rows can keep
the matrix full rank. P128 proves no dependency and no all-input non-global
root.

### C135 — the lifted source has an exact bridge-cycle interpretation

**Status:** promoted as P129 after hostile audit and blind reconstruction.

After the matched canonical column is retained, one squared-anchor lift adds
exactly the bridge square class

\[
[q]+[c_\ell].
\]

The relative closure test is

\[
\Gamma x+(\mathbf1^{\mathsf T}x)[q]
\in\operatorname{colspan}(M_0).
\]

Thus many reused `q` rows can still form a full-rank star or forest. If an
exact endpoint cycle does occur, its normalized root is the product of its
public anchors. A squareclass cycle has the corresponding explicit ratio
correction.

**Exact consequence.** The next theorem must force a cycle or hypercycle in
quasipolynomial work and must make its root non-global. Relation count and
row multiplicity no longer describe the missing step accurately.

### C136 — ordinary bridge cycles reduce to public half-order search

**Status:** promoted as P130 after hostile audit and blind reconstruction.

For a formal squared-action cycle, the signed generator displacement
`delta` satisfies `2 delta in Lambda`, and its normalized root is exactly
`Phi(delta)`. The cycle itself exposes the same public collision. Therefore
formal cycle search does not add a new factor signal. The automatic
commutation cycles have root `+1`, and a useful cycle is the bounded
half-order target already isolated by P71.

Inside one fixed squared-anchor star, carry elimination gives a second exact
boundary. After removing primes through the fourth power of the anchor cap,
the wrapped residue endpoints are pairwise coprime. A bridge-only dependency
can use one only when its remaining cofactor is a square. This condition is
publicly testable in quasipolynomial time.

**Exact remaining gap.** The only unreduced bridge mechanism is now an
arithmetic hypercycle: different endpoint integers, usually from different
stars or older retained columns, must cancel through their actual prime
factors without being a formal modular cycle. A positive theorem must force
such a short hypercycle and a non-global root. P130 proves neither.

### C137 — a wrapped positive cycle must reach the square-root scale

**Status:** the F144 short-cycle surplus claim failed hostile audit and is
recorded as X80. Its general residual-cycle identity survived and is being
re-stated separately.

For every directed containment cycle,

\[
N\mid\left(\prod a_e\right)^2-\prod T_e.
\]

If any edge wraps, the left square is strictly larger than the residual
product. Therefore the anchor product is larger than \(\sqrt N\). This
directly contradicts the frozen F144 short-cycle size bound. Its claimed
cycle-surplus regime is empty.

**Exact consequence.** Positive-direction cycles are not a small local
closure mechanism. A useful retry must construct or select a path long
enough for its anchor product to cross the square-root scale, while avoiding
exhaustive branching. Polynomial path length is still compatible with the
quasipolynomial time target, so X80 does not close a deterministic path
selector or a different arithmetic hypercycle.

### C138 — positive containment cycles are characteristic-scale objects

**Status:** promoted as P131 after F144 V3 passed a fresh hostile audit and
an independent statement-only blind reconstruction. The failed V1 surplus
claim and the corrected V2 strictness error remain preserved.

For each directed containment cycle, the product of the public anchors and
the product of the residual cofactors satisfy

\[
N\mid A_{\mathcal C}^2-T_{\mathcal C}.
\]

One wrapped edge forces \(A_{\mathcal C}>\sqrt N\), even before asking that
the residual be a square. Therefore no cycle with total numerical anchor
product \(2^{\operatorname{polylog}n}=2^{o(n)}\) can be the asymptotic
solution.

If several cycles have combined residual \(S^2\), their exact normalized
root is \(A/S\). In the useful metric window
\(\sqrt{N+S^2}\le A<N/2\), both signs expose proper factors. Unwrapped cycles
have root \(+1\), and two wrapped cycles already overshoot the window.

**Exact remaining gap.** Quasipolynomial time still permits one selected
polynomial-length path or one compact large anchor. It does not permit an
exponential branch search. The live theorem must select such a path and
force its residual product to be a square, or force a different arithmetic
hypercycle through actual cross-star or old-column prime overlap.

### C139 — quasipolynomial finite-algebra probes remain below the local scale

**Status:** promoted as P132 after F145 V2 passed a fresh hostile audit and
an independent statement-only blind reconstruction.

Uniform nonunit tests and generic Krylov-rank tests in explicit
quasipolynomial-rank finite algebras still hit with exponentially small
probability on balanced semiprimes, even after quasipolynomially many fresh
probes. Nilpotents do not improve the nonunit rate for a fixed semisimple
quotient.

A genuine CRT-glued local Frobenius would expose different factor-degree
partitions, but constructing it already contains factor information on that
promise. Public monomial substitutes reduce to hidden order congruences.
Low Hasse-jet orders stay synchronized until the unknown least factor.

**Exact consequence.** The QP allowance does not revive generic finite-
algebra sampling. A useful retry needs a factor-correlated source, a joint
decoder for typical nonzero values, a succinct nonmonomial map, or a
compressed characteristic-scale computation.

### C140 — local AKS exchange scans have an exact quasipolynomial boundary

**Status:** promoted as P133 after F146 V2 passed a fresh hostile re-audit
and an independent statement-only blind reconstruction.

Scanning all base exchanges of polylogarithmic support has exact
quasipolynomial cost. It is complete when the matrix tail is
polylogarithmic. On squarefree inputs, the first proper-gcd exchange equals
the first local column-matroid disagreement; prime-power valuations can add
earlier successes on general composites.

An explicit balanced CRT/Vandermonde family delays the first local matroid
disagreement beyond every fixed polylogarithmic exchange radius, even after
padding to near-square AKS-scale dimensions. This is a generic matrix
boundary, not an AKS counterexample.

**Exact consequence.** P11's two-tail hit does not justify a universal
small-exchange law. A positive F04 result must use the arithmetic form of the
AKS coefficient matrix, force a polylogarithmic tail through a suitable
modulus, or replace local exchange enumeration with another selector.

### C141 — two feedback cycles can close through a residual cross ratio

**Status:** promoted as P134 after F148 passed hostile audit and independent
statement-only reconstruction.

Two directed feedback cycles need not close separately. If their residual
products have one rational square class,
(T_i=d s_i^2) and (T_j=d s_j^2), their union is an exact square relation.
Its factor test reduces to the two small public integers

\[
\alpha_i s_j-\alpha_j s_i,
\qquad
\alpha_i s_j+\alpha_j s_i.
\]

If the slopes differ and their positive sum is below (N), both gcds are
proper. This survives the point where P131's product-of-anchor-products test
has become too large.

**Exact remaining gap.** The decoder is no longer the main issue. The source
must force enough column-disjoint cycles with small residual products and
different slopes. More than (R) such cycles with residuals at most (R)
would suffice in quasipolynomial time, but no current theorem supplies them.
The (N=745) certificate checks the mechanism but is not isolated from a
simpler cross-centre congruence of squares.

### C142 — compact raw-anchor magnitude is not a new singleton signal

**Status:** promoted as P135 after F149 V2 passed fresh hostile audit and
independent statement-only reconstruction.

For a squared anchor with any compact integer presentation, the canonical
endpoint and every containment residual depend only on its residue modulo
\(N\). Its exact squared mass also vanishes from the lifted parity class.
The canonical-plus-lifted singleton closes exactly when

\[
q[q\alpha^2]_N=s^2,
\]

and its factor test is the ordinary congruence of squares between
\(s\) and \(q\alpha\).

For a fixed centre on an odd semiprime, only \(O(\sqrt N)\) of the
\(\Theta(N)\) anchor residues are useful. Quasipolynomially many uniform
trials therefore remain exponentially unlikely to hit.

**Exact consequence.** Compact representation lets the source reach
numerically large residues cheaply, but raw anchor magnitude itself adds no
factor signal. The remaining live possibilities are a factor-correlated
nonuniform residue source or a multi-relation arithmetic closure.

### C143 — bounded-anchor wrapped cycles do not require path guessing

**Status:** promoted as P136 after F147 V2 passed fresh hostile re-audit and
independent statement-only reconstruction.

For one frozen squared-anchor source with \(H^4\le N\), every wrapped
containment cycle lies entirely among named blocks above \(N/H^2\). Its
carries and residuals are below \(H^2\), and one word position has at most
one large target.

The complete large core can therefore be scanned and decoded in
quasipolynomial time when the source and \(H\) are quasipolynomial. This
removes exponential path branching as the gate inside one frozen source.

**Exact remaining gap.** The theorem does not force one core edge, a cycle,
a surviving parity dependency, or a non-global root. The source must still
create enough arithmetic overlap. The strict lower bound
\(L>\log N/(2\log H)\) is necessary only; it is not a path selector.

### C144 — the natural reciprocal metric cycle is a root-\(+1\) decoy

**Status:** promoted as P137 after F150 V2 passed fresh hostile re-audit and
independent statement-only reconstruction.

If the edge \(x\to y\) uses anchor \(y\), and the reverse edge uses anchor
\(x\), both residuals must equal the same public residue
\(h=[xy]_N\). Their bridge product is an exact square, but its positive and
supplied roots agree modulo \(N\). The normalized root is always \(+1\).

The ceiling selector \(q=\lceil N/a\rceil\) constructs this pattern cheaply,
but therefore supplies no factor signal.

**Exact consequence.** Metric near-reciprocity alone is not the needed
feedback law. A useful source must use nonreciprocal cycles, longer cycles,
old-column overlap, or another arithmetic hypercycle.

### C145 — the many-relation decoder is exactly a consistency test

**Status:** promoted as P138 after F152 V2 passed fresh hostile re-audit and
independent statement-only reconstruction.

Each retained square relation carries two linked data items: its integer
square class and its supplied modular root. Put these together in one
public group. Then the complete decoder has only two outcomes:

- a relation circuit breaks consistency and gives a factor; or
- every observed relation follows one consistent public rule over the
  parity space, up to the two global signs.

This rule can be maintained online in time polynomial in the retained
transcript. Thus decoder cost is not the QP barrier.

For two source layers that fail alone, their union succeeds exactly when
their rules disagree on a shared parity class. The (N=3{,}241{,}632{,}473)
cross-layer witness is the finite model of this event. One source can also
break its own rule through an internal circuit.

**Exact remaining gap.** The extension always permits an abstract consistent
rule. Therefore many parity relations, high row reuse, or small doubling do
not force a factor. The source must force a lift disagreement, or show that
persistent agreement creates another public restriction that cannot hold for
all inputs.

### C146 — high order cleans the source but does not correlate it with the factors

**Status:** promoted as P139 after fresh hostile audit and independent
statement-only reconstruction.

A deterministic quasipolynomial preprocessing step can now return a factor
or certify one public element whose order exceeds a quasipolynomial bound in
every hidden prime component. This removes all short collisions, inverse
collisions, and endpoint sign hits in its displayed power window.

The certificate does not control the canonical integer representatives.
Their exact products can still repeat or form a useful square relation. The
\(N=391\) certificate gives such a useful closure even though both local
orders exceed the certified bound.

Pilatte's short relation basis does not enter the QP catalogue by direct
enumeration: its dimension is about \(\sqrt n\), its theorem gives no sparse
support, and the full bounded-norm ball is exponential. The direct fixed
Jacobi-torus coordinate also loses the promised local orientation.

**Exact remaining gap.** High order is useful preprocessing, not a source
theorem. A positive route must exploit canonical carries, find a structured
classical sampler for the relation lattice, use a different torus
coordinate, or prove that persistent source agreement creates a monotone
public restriction.

### C147 — Jacobi gives a real hidden asymmetry, but the direct torus maps do not extract it

**Status:** promoted as P140 after fresh hostile audit and independent
statement-only reconstruction.

A Jacobi-minus-one discriminant guarantees opposite quadratic behavior at
the two hidden primes. This is genuine factor-correlated information from
bare \(N\).

The obvious extraction steps do not use it. Multiplicative discriminant
words carry only one hidden quadratic character. Global Cayley square-root
branches differ by a global sign. Cross-discriminant isomorphisms require
the missing square root. Direct biquadratic norms return squares or one.
Ordinary high order cannot pass homomorphically into the nonsplit torus with
order above two. The fixed Kummer trace removes the discriminant label.

The product of two discriminants does give one exact sum-type torus
identity, but its hidden sign and exponent are not public.

**Exact remaining gap.** Forced local asymmetry is not enough. The source
must create two incompatible coordinate lifts, or use a non-norm invariant,
a nonhomomorphic map with a proved order law, or a torus-native feedback
rule that breaks the common decorated section.

### C148 — feedback subgroup expansion is real, but named-state growth can be bookkeeping only

**Status:** promoted as P141 after hostile audit and independent
statement-only reconstruction.

An unconditional infinite balanced-semiprime family now shows the exact
feedback phenomenon. A canonical inverse endpoint stays inside the old
modular subgroup, but its integer overlap splits the old named block. The
refined blocks generate a strictly larger subgroup than the frozen
one-block state.

This validates the framework-level distinction between modular information
and integer presentation. It also exposes the trap: in this family the new
block is the public constant \(5\). A complete initial source can name it
without feedback.

**Exact remaining gap.** We need an operational expansion relative to the
complete declared source, followed by a forced section disagreement or
another verified factor test. Expansion relative to an artificially coarse
ledger is not enough.

### C149 — full section completion is algebraically inert but can unlock a later grammar

**Status:** promoted as P142 after F154 V3 passed fresh hostile re-audit and
independent statement-only reconstruction.

When the retained many-relation decoder fails in polylogarithmic parity
dimension, its complete public section can be generated in quasipolynomial
time. Every manufactured square dependency has normalized root \(+1\), and
mixing it with old relations cannot add a useful root. Thus completion does
not improve the current decoder.

Its canonical integer endpoints can still split old named blocks. On the
\(N=77\) witness, the split \(4706=26\cdot181\) enlarges the subgroup that a
restricted named-block grammar may use. A later power test, or even the
simpler screen \(\gcd(181+1,77)\), then factors the input.

This is a real algorithm-state change, but not new information: \(26\) was
already the public inverse of the supplied root \(3\). The example proves
finite capability only.

**Exact remaining gap.** Force an operational new block relative to the
complete declared source, and then force a later section disagreement or a
separate factor test. Merely completing a consistent section cannot do it.

### C150 — sparse relation products give a complete QP feedback grammar

**Status:** promoted as P143 after F156 V2 passed fresh hostile re-audit and
independent statement-only reconstruction.

The new source uses sparse products of retained relation-basis lifts, not
sparse products of named integer blocks. One basis relation can be dense in
the old block coordinates. This gives a genuine grammar-level enlargement.

The schedule is exact: complete the ordinary frozen scan, build one actual
section basis, enumerate support at most \((\log n)^2\), expose canonical
inverse endpoints, jointly refine once, and let only descendants of the
fixed initial product become future named blocks. Feedback relations never
become later section generators. The total deterministic cost is

\[
2^{O((\log n)^6)}.
\]

If the basis dimension is at most the support cap, this scans the entire
nonidentity section and contains every P142 refinement opportunity.

**Exact remaining gap.** The source can still stop with no factor and a
globally consistent final section. The missing theorem must force a direct
screen, a useful refinement chain, or a non-global root. Cost and source
coverage are no longer the immediate obstacle.

### C151 — a supplied quadratic lift has a strict monotone outcome

**Status:** promoted as P144 after hostile audit and independent
statement-only reconstruction.

For an explicitly listed public subgroup, any supplied element whose square
is old gives one of three exact outcomes: a factor, confirmed membership, or
an index-two expansion in both hidden components. With a certified
common-order generator, the same test is compact. A genuine expansion
doubles the exact common local order.

This is the first clean monotone capacity law on the feedback route. A chain
of valid external lifts cannot continue beyond the smaller hidden group
order. The decoder and the number of levels are polynomial.

The source problem remains the hard part. The universal certificate
\((-1,2)\) does not give a square root of \(-1\). Such a root can fail to
exist at the first level, and later roots can fail far below the
\(\sqrt N\) outer bound.

**Exact remaining gap.** Construct, in polynomial or quasipolynomial time, a
factor or one external coprime quadratic lift over each surviving certified
state. Merely listing many relations or proving subgroup growth without a
known common order does not meet this condition.

### C152 — a primitive lift always gives factor-or-double after a public sign choice

**Status:** promoted as P145 after hostile audit and independent
statement-only reconstruction.

For a certified common-order state, any supplied square root of a primitive
power now has only two outcomes: a factor or exact doubling of the common
local order. If the order is odd, compare with the public internal root and
choose the opposite global sign. If the order is even, every root already
has twice the order. The former inert branch is gone.

This also sharpens the many-relation target. A decorated section hit gives
the needed root directly, so it is sufficient. But the hit condition is
root-equivalent to the original scalar problem; it is not a source theorem.

Jacobi information gives a precise boundary at even order. A negative
Jacobi symbol proves that only one hidden field admits the next root. A
positive symbol merges the both-admit and neither-admits cases. Pairing two
negative-Jacobi discriminants only re-encodes the same missing root.

**Exact remaining gap.** At every surviving even common-order state, force a
factor or one primitive section square-class hit in quasipolynomial work.
Externality is no longer part of this gate; root production is the whole
gate.

### C153 — integer refinement can escape a saturated modular root layer

**Status:** promoted as P146 after fresh hostile re-audit and independent
statement-only reconstruction.

One fixed layer of square roots can add at most one modular coset. At odd
common order, even that coset is generated by the public element \(-1\).
This closes the idea that many roots alone can keep expanding the modular
state.

Canonical integer encoding behaves differently. A root that is already an
old modular power can split an old integer block. The released factors need
not belong to the old subgroup. The \(N=341\) certificate proves this
strictly: a modularly inert root splits \(70\) into \(14\) and \(5\), grows
the named subgroup from size \(5\) to \(75\), and then
\(\gcd(14^5-1,341)=11\).

The screen \(\gcd(d^M-1,N)\) now classifies every released block: factor,
membership in both old local groups, or strict growth in both. This is a
real algorithm-state change, not only a new scalar identity.

**Exact remaining gap.** Force useful refinement on every stalled source,
then turn the released blocks into a compact certified common-order
extension or another monotone restriction. One finite refinement does not
give recursion.

### C154 — sparse section feedback has one public QP success beyond a frozen null layer

**Status:** promoted as P147 after the registered computation, corrected
fresh hostile re-audit, and independent blind reconstruction.

The F111 frozen layer for \(N=3{,}241{,}632{,}473\) has null direct screens
and only global normalized roots. Support-one F156 feedback also misses. A
support-two decorated product gives the public inverse pair

\[
(z,w)=(3{,}183{,}314{,}832, 205{,}056)
\]

and \(\gcd(z-w,N)=41{,}011\).

This is not only a factor-assisted discovery. F156 already declares every
support-two pair, and its basis has quasipolynomial size. A factor-free
lexicographic pair scan therefore locates the certificate in
quasipolynomial time on this fixed input. The disclosed factors only made the
complete five-input experiment fit its 900-second limit.

Four frozen 58-bit controls have no support-at-most-two hit. They do not
close larger support or later feedback. The positive witness proves real
source capability, but no density or all-input progress law.

**Exact remaining gap.** Prove that some bounded support layer succeeds or
causes monotone progress on every input. A single public QP locator on one
fixed input does not provide this theorem.

### C155 — a released block now has a compact factor-or-grow updater

**Status:** promoted as P148 after hostile audit and independent
statement-only reconstruction.

Start from a certified common-order state \((g,M)\). For one released unit
block \(d\), scan \(\gcd(d^{eM}-1,N)\) through the QP cap. A proper value
factors \(N\). A first global return proves that every hidden relative order
is the same \(e\). All-one output proves that every hidden relative order is
above the cap.

The equal-order branch needs one further check. Hidden discrete logarithms
can disagree even when the relative indices agree. A factor-first
Pohlig--Hellman calculation either finds this disagreement as a factor or
aligns one relation \(d^e=g^a\). After alignment, a two-dimensional Smith
calculation gives an explicit public generator of exact common order \(Me\).
Thus every successful update strictly multiplies a certified common order,
and fewer than \(n\) such updates can occur.

This closes the decoder problem left by C153. It does not close the source
problem. Feedback can still return old-subgroup blocks or blocks with
relative order above every QP cap.

**Exact remaining gap.** Prove that the public feedback source cannot remain
in the inert and above-cap branches. A useful theorem must either force a
bounded relative-order hit or make repeated above-cap certificates
accumulate into a contradiction.

### C156 — pure PFR on the decorated decoder adds no information

**Status:** promoted as P149 after hostile audit and independent
statement-only reconstruction.

After the P138 consistency test fails to factor \(N\), the decorated subgroup
generated by the retained relations is exactly the graph of the public parity
section. Projection to parity is an isomorphism. It preserves every iterated
sumset, additive relation, affine subspace, and intrinsic coset cover.

This closes the direct Babai/PFR splice. Large doubling can occur while the
generated subgroup is already fixed and root-global. Doubling one can occur
inside a root-global subspace or affine coset. Neither PFR branch forces a
new root direction.

The obstruction is narrow. Integer representatives, canonical carries,
block incidences, sizes, and provenance are not preserved by this
isomorphism. Those are still live inputs to a richer split-or-structure
argument.

**Exact remaining gap.** Force two public source mechanisms to choose
incompatible lifts on one shared parity vector, or prove that a
section-consistent additive cell must cause a bounded integer refinement or
relative-order update. Pure decorated additive structure cannot do this.

### C157 — common-order growth and relation recovery are separate tasks

**Status:** promoted as P150 after a clean proof-only hostile audit and an
independent statement-only reconstruction.

After an F161 common return, exact order reduction on the released block
either factors \(N\) or certifies one common local order \(m\). Local
cyclicity then gives

\[
\operatorname{lcm}(M,m)=Me.
\]

A public product of the required prime-primary parts of \(g\) and \(d\)
has exact common order \(Me\). Hidden-log alignment is not needed for this
state update.

Alignment still has real value. It can expose a factor when hidden phases
differ. It also gives the exact relation needed by the F164 lattice. The
\(N=341\) certificate separates these outputs: the lcm word has common
order ten, while the full named subgroup has order fifty and the alignment
gcd gives the factor eleven.

The clean design is now: use the lcm word as the next common-order state,
retain all old generators and provenance, and run alignment only when an
exact relation, global compression, or its factor channel is needed.

**Exact remaining gap.** The source must still supply a released block with
a bounded common relative order, or turn the inert and above-cap branches
into quasipolynomial progress. This correction simplifies the decoder but
does not solve the source problem.

### C158 — beyond-cap blocks now have exact public rank–capacity accounting

**Status:** promoted as P151 after a fresh hostile re-audit and an independent
statement-only reconstruction.

The \(M\)-th power of a public word is an exact fingerprint of its coset
modulo the current common-order subgroup. A mismatch between hidden
components factors \(N\). On the synchronized branch, \(\kappa\) distinct
fingerprints certify local subgroup size at least \(M\kappa\).

For one new block, a first collision gives one independent aligned relation.
No collision through exponent \(B\) multiplies the certified capacity by
\(B+1\). After \(t\) blocks and \(r\) retained collision rows,

\[
\kappa\ge(B+1)^{t-r}.
\]

If the complete relation lattice has full rank and index
\(D=M\kappa\), Smith normal form produces the next exact common-order state.
The equality is the gate. Rank alone is not enough.

The \(N=341\) certificate shows the obstruction. Two blocks can each have
relative order above the cap while remaining powers of one synchronized
hidden quotient direction. The second block then adds a relation, not
capacity or a factor.

**Exact remaining gap.** Force disjoint quotient layers, exact index closure,
or a bounded relative-order procedure against the full accumulated subgroup.
Individual above-cap certificates and block count do not force any of them.

### C159 — an existing signed pair collision no longer needs a quadratic scan

**Status:** promoted as P152 after a fresh hostile re-audit and an independent
statement-only reconstruction.

For a public unit list, one product polynomial and one derivative evaluation
batch detect every proper signed product \(ab\equiv\pm1\) on only part of the
hidden CRT decomposition. Exact global partners are removed by the derivative.
Equal-value positions use self screens. If an aggregate gcd is \(N\), a
scalar subproduct tree localizes a proper factor.

The method is near-linear in the encoded explicit list, up to polynomial
coefficient arithmetic. It works over arbitrary composite moduli because all
tree divisors are monic. A quasipolynomial list stays quasipolynomial.

This replaces the support-two pair scan on the fixed F157 witness: one raw
empty-intersection batch finds factor \(41{,}011\). It does not create the
collision and does not imply a non-global root.

**Exact remaining gap.** Prove that a public source supplies at least one
proper signed collision, or combine this locator with a source-side
rank/capacity law. Faster localization does not change a null source.

### C160 — QP rescaling preserves the order decoders, not their promises

**Status:** promoted as P153 after hostile audit and independent
statement-only reconstruction.

Every existing smooth-order, punctured-bank, bounded-image, and capped-
subgroup decoder in P87 and P92--P99 remains QP when all numerical caps and
the complete encoded state are QP. The large numerical lcm is not a cost
problem because its bit length is only \(O(B\log B)\).

This gives a real bare-\(N\) promise algorithm. If the smaller coprime local
order \(\min(A,B)\) of the \((N-1)\)-power rectangle is QP, direct uniform
sampling and verified repetition split the semiprime in expected QP time.

The new stable family shows why this does not close the route. Infinitely
many inputs have \(\gcd(p-1,q-1)=2\), exponentially large prime components
in both local powered orders, and

\[
\gcd(AB,N-1)=1.
\]

Every \(N-1\)-supported power is then an automorphism of the same rectangle,
and direct uniform success is \(2^{-\Omega(n)}\). QP repetition and a larger
smooth-order bank remain insufficient.

**Exact remaining gap.** Use value-dependent feedback or accumulated
relations to escape the synchronized large cyclic core. The route needs a
forced bounded quotient, an independent capacity increase, an aligned
lattice closure, or a non-global root. QP rescaling alone supplies none of
these events.

### C161 — a frozen feedback block list now has a complete quotient updater

**Status:** promoted as P154 after hostile audit and independent
statement-only reconstruction.

For each released unit, one lcm screen and one bounded relative-order scan
give an exact factor-first classification: factor, common-order growth, or a
certificate that both its absolute primary component and its relative order
exceed the QP cap.

The full frozen list can now be treated jointly. Enumerate the subgroup
generated by the \(M\)-th-power fingerprints. A hidden equality mismatch
factors \(N\). If the table closes at size \(\kappa\), it gives the exact
common local quotient order and a new certified state of order

\[
M\kappa.
\]

If the table exceeds the cap \(C\), it certifies local subgroup capacity at
least \(M(C+1)\). This is the Harvey--Hittmeir-style win--win that survives
for the current feedback objects.

The updater also fixes the bookkeeping. State growth resets fingerprints,
but it does not delete exact relations or endpoint presentations. These need
separate persistent ledgers.

**Exact remaining gap.** The source can still land in one synchronized cyclic
quotient whose order exceeds every tested QP cap. We must force small closure,
force enough independent capacity increases, close the aligned relation
lattice at its exact index, or obtain a non-global root. P154 proves the
outcome logic after such an event. It does not force the event.

### C162 — fixed-depth exact-value feedback is QP, but observed structure growth is not progress

**Status:** promoted as P155 after exact finite reconstruction, hostile proof
audit, and fresh statement-only reconstruction.

For a QP base transcript, polylogarithmic source support, and any fixed number
of layers, the complete workflow remains QP. This includes all attempted and
duplicate values, exact-value retention, multiplicity-aware factor-free
refinement, perfect-power extraction, dense parity elimination, a complete
kernel basis, normalized exact roots, signed gcd screens, zero columns, and
compact provenance.

The verified depth-two corpus separates syntactic growth from semantic
progress. Across the 63 base-null inputs, both feedback levels added hundreds
of strict exact values, increased rank on almost every input, and split many
old integer blocks. They produced no direct factor and no non-global kernel
root. The single factor in the 64-input corpus was already the base square
$N+1=10008^2$.

**Exact remaining gap.** Fixed-depth cost is no longer an issue. A positive
route must prove that some QP-bounded layer forces a factor-bearing mismatch,
bounded quotient closure, exact lattice closure, or non-global normalized
root. More records, more rank, and more factor-free refinement are not such a
law. Growing recursion also needs a separate uniform QP bound.

### C163 — ordinary and torus exact orders give a dual CRT progress potential

**Status:** promoted as P156 after hostile audit and independent
statement-only reconstruction.

An ordinary common order divides $N-1$. A Jacobi-minus-one torus common order
divides $N+1$. Starting both states at order two makes their gcd exactly two,
so every strict exact update multiplies their lcm rather than merely enlarging
one already-covered primary part.

Once this lcm reaches $\sqrt N/Q(n)$, two CRT classes enumerate the smaller
factor in QP time. On balanced semiprimes, one orientation-free sum class and
the narrower $(3/\sqrt2-2)\sqrt N$ interval suffice. The torus also admits
the complete P154 factor/closure/capacity updater through joint-coordinate
gcd comparisons.

**Exact remaining gap.** No source forces a strict ordinary or torus closure.
Capacity is not an order modulus. The theorem is useful only if factor-first
processing supplies repeated exact growth while the complete transcript stays
QP.

### C164 — carry difference covers solve location, not source closure

**Status:** promoted as P157 after hostile audit and independent
statement-only reconstruction.

The carry row $r$ occupies the unique class $-N^{-1}\bmod r$, and useful
parity reuse also requires odd valuation. Even satisfying both conditions for
every prime through $R=\Theta(n/\log n)$ does not force a dependency: P157's
polynomial canonical bank has two valuation-one hits in every such row and a
private-prime identity submatrix on all columns.

**Exact remaining gap.** A complete adaptive grammar must prove that it
reuses every surviving private row and creates a final rank defect, then still
prove a non-global root. Difference coverage and faster pair location supply
none of these events.

### C165 — exact common-order growth is not a universal terminal potential

**Status:** promoted as P158 after hostile audit and fresh statement-only
reconstruction.

F172 constructs infinitely many trial-hard semiprimes with

\[
\gcd(p-1,q-1)=6
\]

and every other shifted gcd $\gcd(p\pm1,q\pm1)$ bounded by four. Therefore
the maximal ordinary exact common order, every quadratic-torus exact common
order, and their combined lcm are bounded by twelve, even with perfect source
access. Since both factors are exponential in the actual input length, this
constant never reaches the P156 terminal threshold $\sqrt N/Q(n)$.

**Strategic update.** Common-order accumulation is no longer the primary
source target. The positive route must exploit unequal local orders or
fingerprints as a factor signal, or return to a non-order root/relation
decoder. Large local capacity by itself is not progress.

**Exact remaining gap.** Prove that a QP public source forces a detectable
ordinary/torus mismatch on every constant-common-capacity input, or find a
different pooled observable with a QP evaluator and an all-input reduction.

### C166 — the unresolved ordinary source is one normalized base-two branch

**Status:** promoted as P159 after fresh hostile re-audit and independent
statement-only reconstruction.

For arbitrary odd composites and arbitrary fixed QP caps \(B,C\), one
absolute lcm screen and one relative sign-quotient scan now give a complete
factor-first trichotomy. The output is a factor, a factored exact
common-order state above the input length, or the single public hard block
\(2\). In the hard branch every local order of \(2\) has a prime-power
component above \(B\), and every local order modulo \(\langle-1\rangle\)
exceeds \(C\). The Mersenne edge case is constructive: it either gives an
explicit factor or the exact common state \((-2,2n)\).

**Strategic update.** Repeated source generation is not needed to define the
ordinary hard case. The next theorem should operate directly on base two.
The live constructive refinement raises \(4\) to \(N^n\), which removes all
order-primary factors supported on hidden primes. This appears to reduce the
remaining obstruction to unequal coprime local orders.

**Exact remaining gap.** Prove a QP factor-or-progress transition for that
coprime-order branch. A common annihilator is useful only if its factorization
or a hidden-component mismatch can be recovered in QP time; an unfactored
cyclotomic block alone is not an exact common-order state.

### C167 — hidden-prime order support is no longer part of the hard case

**Status:** promoted as P160 after hostile audit and independent
statement-only reconstruction.

Raise the P159 base-two square to \(N^n\). This removes the complete primary
part of every local order supported on any rational prime dividing \(N\).
An identity branch factors through the least hidden prime. A second
factor-first lcm screen then gives a factor, an exact common-order state above
the input length, or one public unit whose local orders are all nontrivial,
coprime to \(N\), and have a prime-power component above an arbitrary fixed
QP cap. Their sign-quotient orders also stay above the chosen cap.

**Strategic update.** Repeated prime factors no longer create a separate
order-support escape. The remaining ordinary branch is a clean hidden-order
problem in cyclic groups of order coprime to the input.

**Exact remaining gap.** Local orders can still be unequal and exponentially
large. QP scans can expose a short action-period mismatch, but an unfactored
annihilator such as \(N^k-1\) is not yet an exact common-order certificate.

### C168 — all small prime support can be removed from the local orders

**Status:** promoted as P161 after hostile audit and independent
statement-only reconstruction.

Raise the P160 unit to
\(\operatorname{lcm}(1,\ldots,T)^n\), where \(T\) is any fixed numerical
QP cap. This deletes every local-order primary supported on a prime at most
\(T\), with full multiplicity. A proper identity gcd factors. Global
identity gives a fully factored annihilator and hence a factor or one exact
common order above \(T\). The surviving unit has nontrivial local orders
whose every prime divisor exceeds \(T\).

**Strategic update.** Smooth and partly smooth local orders are no longer a
separate hard case. F183 further gives a fully factored small-base action
filter. The sharper live candidate F184 uses root counting instead of
factoring the action annihilators, and therefore permits an arbitrary
numerical-QP action-period cap.

**Exact remaining gap.** Large rough local orders can remain unequal. Long
actions of many public bases do not yet prove independent automorphism-group
growth, an exact common order, or a factor.

### C169 — cross-resultants close synchronized extinction, with recursion shape tracked correctly

**Status:** promoted as P162 after hostile audit and independent
statement-only reconstruction.

Two separated shift menus turn global extinction into a QP list of smaller
cross-resultants. Under a fixed bit-length contraction, recursively factoring
all of them gives a fully factored common annihilator. Factor-first stripping
then returns a factor or one exact common local order. This closes the
synchronized-extinction branch of the P161 action filter.

**Recursion correction.** A fixed contraction is sufficient for this
many-child recursion. It is not necessary for a unique recursive chain. If
one canonical child loses at least one bit, then

\[
T(n)\le T(n-1)+\operatorname{QP}(n)
\]

is still quasipolynomial. The correct cost invariant is the total recursion
tree volume, not a fixed contraction at every edge.

**Strategic update.** The base-two carry, centered-resultant, and
nearest-remainder candidates now fail for a different reason. Their recursive
factorizations do not lift to a factor of \(N\), an exact common order, or a
non-global root. On the normalized base-two branch, the first carry is one,
short normalized Hankel resultants are a known small word times an already
named power of two, and factoring \((N-1)/2\) yields only the same global
inverse relation.

**Exact remaining gap.** Resolve the wide-shift-hard descendant, or construct
one canonical smaller auxiliary whose complete factorization has a proved
lift to a factor, a certified common-order state, or a non-global root. A
one-bit decrease is enough if only one child survives.

### C170 — sequential peeling converts the synchronized branch to one child

**Status:** promoted as P163 after hostile audit and independent
statement-only reconstruction.

The corrected recursion observation is operational, not only editorial.
Given a QP list whose prime support covers every current local order, process
the entries as exponent filters. Earlier entries need no factorization. At
the first global identity, the current element is annihilated by the final
entry alone. Recursively factor only that one integer, then use factor-first
stripping.

For the P162 cross-resultant list, this removes the QP-many-child recursion.
The child may have \(n-1\) bits:

\[
T(n)\le T(n-1)+\operatorname{QP}(n)
\]

still has QP total cost. The cross-resultant size condition is correspondingly
relaxed from a fixed \(\rho n\) contraction to a one-bit contraction.

**Strategic update.** A public support-covering list plus an identity test is
enough to select one recursive child with a valid lift. This is the precise
form in which integer recursion improves the ring-only route. It does not
help when the source supplies only long actions and no support cover.

**Exact remaining gap.** The only P162/P163 output not closed by this method
is the wide-shift-hard rough descendant. We need to force an extinction cover,
or obtain a factor, exact common order, or non-global root directly from the
simultaneous long-action state.

### C171 — root counting hardens every surviving order prime against a QP-wide action bank

**Status:** promoted as P164 after a fresh hostile re-audit and an independent
statement-only reconstruction.

For arbitrary fixed numerical-QP caps (K) and (M), use (M) disjoint
blocks of (D+1) consecutive bases, where

\[
D=1+K(K+1)/2.
\]

The bad-base condition for an order prime is the zero set of the monic
degree-(D) polynomial

\[
X\prod_{k=1}^K(X^k-1).
\]

Therefore one base in every block survives or a gcd factors (N). After
(M) stages, every surviving order prime sees all (M) selected public
bases as units of multiplicative order above (K). The construction and
all exponent bit lengths remain QP, and arbitrary hidden prime powers are
handled exactly.

**Strategic update.** A fixed polylogarithmic action cap is no longer the
boundary. Any pre-registered QP number of adaptive public actions can be
made simultaneously long on every surviving order prime. Hence a terminal
argument must use a structural relation among those long actions, a support
cover compatible with P163, or a genuinely integer-specific lift. It cannot
rely only on testing more small action periods.

**Exact remaining gap.** The selected actions can all lie in one large
cyclic direction. QP-wide long action does not yet force an extinction
cover, a factor, an exact common local order, or a non-global root.

### C172 — complete \(N-1\) factorization removes decoding ambiguity, not rare return

**Status:** promoted as P165 after hostile audit and independent
statement-only reconstruction.

Recursively factoring \((N-1)/2\) is a valid one-child QP step. Once the
factorization of \(N-1\) is known, every full-return base can be stripped to
a proper factor or one fully factored exact common local order, including for
repeated prime powers. The exact random-base law is now known.

On infinitely many bounded-gap balanced semiprimes, however, the local
\((N-1)\)-root groups have constant size. An independent uniform base enters
at least one return group with probability only \(2^{-n/2+O(1)}\), and all
synchronized common orders remain bounded. A QP sample bank therefore has
negligible success.

**Strategic update.** The corrected one-child recurrence fully validates the
preprocessing cost. It does not rescue the route because the obstruction is
rare entry, not recursion or order stripping. Adaptive bases and other
exponent families remain open.

**Exact remaining gap.** Continue from P164's wide-action state. We need a
source-correlated support cover, a direct separator, or a high-order
decomposition. Independent sampling from a factored \(N-1\) exponent family
does not supply it.

### C173 — segment zero isolates the missing affine prefix-OR evaluator

**Status:** promoted as P166 after hostile audit and independent
statement-only reconstruction.

A QP segment-Jacobi zero oracle would be enough on balanced semiprimes.
The affine source \(U+tV\) supplies a useful local zero with constant
probability at interval length \(\Theta(\sqrt N)\), and binary isolation
retains only one child per level. The recursion cost is therefore QP.

The exact totalized reciprocity identity shows that ordinary Jacobi
compression removes the signs but leaves the gcd correction unchanged. The
zero mask has exponential explicit Fourier support, linear-recurrence order,
and deterministic residue-state complexity. Its factorial form is a carry
in the hidden base. These are representation boundaries, not a general
lower bound.

**Strategic update.** The source probability is not the obstacle. The exact
missing operation is a succinct prefix-OR over \(\Theta(\sqrt N)\) affine
integer events. One-child isolation helps only after that OR can be evaluated.

### C174 — long retained Paley words remain information-rich but modulus-blind

**Status:** promoted as P167 after hostile audit and independent
statement-only reconstruction.

Dense spectral reconstruction, explicit low-order correlations, short
row-only list recovery, and QP coordinate collisions all remain insufficient
at QP scale. However, \(O(n)\) columns can give a local Paley code constant
distance. The long-word channel is therefore not killed by entropy or code
distance.

**Strategic update.** The live P54 operation is high-order and source-aware:
decompose the retained public Jacobi word as the Hadamard product of two
unknown-modulus Paley words and return a zero divisor. Naming an oracle that
already returns a hidden prime merely restates QP factoring. A useful next
step must expose a smaller structural output or a succinct arithmetic
cancellation invariant.

**Exact remaining gap.** Reconcile P164's long-action state with P167's
long-word information. Either construct a source-correlated support cover for
P163, or turn a high-order retained-word statistic into a verifiable zero
divisor without evaluating an exponential prefix product.

### C175 — one-bit recursion still needs support-preserving size localization

**Status:** promoted as P168 after F191 V2 passed a fresh hostile re-audit
and a strict statement-only reconstruction. F191 V1's failed direct handoff
is preserved as X81.

For \(\ell\mid X\) and \(X=QD+R\), an \(\ell\)-free divisor \(D\) gives

\[
\ell\mid R\iff\ell\mid Q.
\]

Centering a huge supported integer therefore does not create a supported
small child. A universal \(X=N+c\) example loses the support in both valid
children. Even a QP bank of equidistributed exact multiples can lose the
same prime in every centered quotient and remainder.

**Strategic update.** The corrected one-child recurrence remains valid.
The missing premise is stronger than “some recursively factorable integer
is divisible by the target prime.” The selected integer must be nonzero,
have fewer bits than \(N\), and retain the required support. Otherwise the
recursion has no mathematical lift.

**Exact remaining gap.** Prove an \(N,w\)-correlated quotient or carry
concentration theorem, construct another support-preserving localization
operation, or bypass P163 with a direct separator. Generic Euclidean
normalization is now closed.

### C176 — the standard P164 ACD row lattice selects coprime decoys

**Status:** promoted as P169 after hostile audit and independent
statement-only reconstruction.

One retained P164 base gives a public power word that is pairwise distinct
modulo every hidden prime. Circular pigeonholing therefore supplies a hidden
cluster of approximate multiples for each factor. This is a genuine
integer-specific source beyond arbitrary ring expressions.

The natural standard row lattice nevertheless fails in its easiest promised
form. Even after granting the correct larger-prime cluster and its error
bound, simultaneous Dirichlet approximation gives a vector strictly shorter
than every factor-bearing coefficient. Every exact shortest vector then has
only unit coordinates modulo \(N\). Exact SVP plus coordinate gcd tests
cannot extract the factor.

**Recursion correction retained.** This result does not use fixed-ratio
contraction. A single auxiliary chain with

\[
T(n)\le T(n-1)+\operatorname{QP}(n)
\]

is QP. The failure is the missing mathematical lift from the selected short
vector, not its size. Complete factorization still needs separate accounting
if the enclosing routine also recursively factors both children of later
splits.

**Strategic update.** A predeclared order-oblivious subset bank becomes
exponential at the ACD-informative cluster dimension. This count does not
cover a selector that exploits the recurrence \(x_{j+1}=x_j^a\). The live
P164-to-P163 route is now narrower: use the recurrence or another
factor-asymmetric invariant to locate a local cluster, then decode it with a
method that proves support rather than merely shortness.

**Exact remaining gap.** Construct that source-aware selector/decoder, or
bypass support localization through a direct separator or the high-order
Paley-word interface of P167.

### C177 — explicit separating representations do not orient the hidden factors for free

**Status:** promoted as P170 after the repaired F193 V3 passed hostile audit
and statement-only reconstruction.

Sparse modular-symbol endpoints either expose a factor through their
denominator gcd or remain on the two global cusps. Good Hecke and Fricke do
not create the missing local orientation. A uniform small-modulus bank for
\(\sigma_1(N)\) is already enough to reconstruct that coefficient and factor;
twists of one fixed coefficient add only public scalar multiples. A globally
descended elliptic endomorphism likewise has compatible good-torsion action
in both hidden fibers.

**Strategic update.** These explicit representation routes do not replace
the core beta-two task. Any useful representation-theoretic step must compute
characteristic-dependent Frobenius data, work in a genuinely succinct
boundary-zero object, or produce a new arithmetic cancellation invariant.

**Exact remaining gap.** The active core remains the beta-two branch: turn
its integer representatives, carries, or a non-polynomial threshold
functional into a factor or a sufficiently large exact common order.

### C178 — beta two is a hidden exact-division jump in a succinct binomial circuit

**Status:** promoted as P171 after F194 V3 passed focused hostile review and
strict statement-only reconstruction. The failed V1 mathematics and failed
V2 metadata package remain preserved.

For balanced \(N=pq\), \(B=\lfloor\sqrt N\rfloor\), the word

\[
A_k=(-1)^k\binom{N-1}{k}\pmod N
\]

is exactly \(1\) before \(k=p\) and exactly \(1-q\) from \(p\) through
\(B\). Hence

\[
\gcd\!\left(N,(-1)^B\binom{N-1}{B}-1\right)=q.
\]

The discontinuity is caused by exact cancellation of the hidden nonunit
index \(p\) in

\[
(k+1)(A_{k+1}-A_k)=-NA_k.
\]

This is the integer-specific structure that generic ring operations erase.
Equivalently, the logarithmic-size circuit
\((1+X)^N-1-X^N\) has hidden local \(X\)-adic orders \(p\) and \(q\).

**Boundary update.** Polynomial index moments collapse to the ordinary
Fermat scalar. Small cyclic sketches have full Boolean support in both
components unless the prime gap is already QP-enumerable. Neither statement
is a general circuit lower bound. Coefficient-sensitive cancellation remains
open.

**Recursion correction retained.** A one-child recurrence losing only one
bit is still QP. The present obstruction is not insufficient contraction.
It is that no QP procedure is known to compute the remote binomial residue,
the corresponding signed base-\(N\) carry, or the local valuation of the
succinct circuit.

**Exact remaining gap.** Build one of those three evaluators, or prove an
equivalent integer threshold/exact-division transition. This is now the
central beta-two task.

### C179 — the latest order algorithms sharpen the terminal but stop at beta two

**Status:** promoted as P172 after F195 V2 passed a primary-source hostile
re-audit and a strict statement-only reconstruction.

A fully known exact common local order \(M\), coprime to \(N\), forces every
hidden prime into the progression \(1\bmod M\). The 2025
Gao--Feng--Hu--Pan terminal then costs \(N^{1/4}/M\), up to logarithmic
factors. It is QP once that ratio is QP.

This does not solve the P159 branch. The 2026 Harvey--Hittmeir routine exits
at beta two before its smooth-number stage whenever the certified order of
2 exceeds the chosen QP cap. Its bounded-order work is a same-node cost, so
the valid recurrence \(T(n)\le T(n-1)+\operatorname{QP}(n)\) does not
accelerate an exponential choice of the order cap. The direct 2025
rank-three list also remains at least \(N^{1/8}\).

**Strategic update.** The useful integer-specific fork is now exact. If all
small rational primes have synchronized low order, their lcm is large by
smooth-number counting and the progression terminal factors. Otherwise the
branch contains small ordinary high-order bases, starting with 2. Generic
group elements are no longer the right source model.

**Exact remaining gap.** Resolve the mixed high-order small-integer branch.
The active subproblem remains P171's hidden quotient/carry operation for the
beta-two binomial or factorial, not another generic ring-order scan.

### C180 — the beta-two pair collapses to one quotient digit

**Status:** promoted as P173 after F196 passed a source-level hostile audit
and a strict statement-only reconstruction.

For \(B=\lfloor\sqrt N\rfloor\), the residue

\[
\binom{N-1}{B}\bmod2^n
\]

is deterministic polynomial-time computable through the corrected 2013
power-of-two binomial algorithm. It is not the missing beta-two information.
The signed base-\(N\) quotient carry \(h\bmod2^n\) alone recovers \(q\),
and \(q\) conversely recovers that carry. A residue modulo \(N2^n\) exposes
the same quotient digit and already exposes \(q\) through its remainder.

**Strategic update.** The live primitive is not a generic ring operation and
not a two-coordinate joint observable. It is one integer base-conversion
operation on an exponentially large but succinct binomial. Exact-output
materialization is exponential, while standard modular reduction loses the
quotient. A one-child recurrence would be QP after such a digit or a
supported smaller child exists; it does not compute either object.

**Exact remaining gap.** Compute the low base-\(N\) quotient block of the
remote binomial or an equivalent factorial quotient block in QP time, or
find another integer-specific operation that releases the hidden exact
division at \(p\).

### C181 — factorial recursion is allowed; the quotient digit is still missing

**Status:** promoted as P174 after F197 passed a primary-source hostile audit
and a strict statement-only reconstruction.

For \(B=\lfloor\sqrt N\rfloor\), the factorial \(B!\) contains \(p\)
exactly once and no factor \(q\). Thus its residue modulo \(N\) is already a
factor-bearing object. Explicit dense blocks and the published
Bostan--Gaudry--Schost/Costa--Harvey methods reach it at the
\(N^{1/4+o(1)}\) scale. Modular lifting to \(N^2\) retains a nontrivial
division kernel, and its low base-\(N\) digit already factors.

The low bits of \(Q=\lfloor B!/N\rfloor\) are a sufficient alternative:
they recover the exact remainder \(B!\bmod N\) because
\(B!\bmod2^n\) is easy. This is the factorial version of P173's binomial
quotient carry.

**Recursion correction.** A unique child with only one fewer input bit gives
\(T(n)\le T(n-1)+\operatorname{QP}(n)\), which is QP. This is fully
accepted. The present methods do not become QP because they spend
\(N^{1/4+o(1)}\) work before producing any child. The defect is same-node
evaluation, not contraction.

**Exact remaining gap.** Compute a sufficient block of the factorial or
binomial Euclidean quotient, produce an \(N^{1/4}\)-accurate approximation
to a hidden factor, or construct another support-bearing smaller child in
QP time. Standard product blocks and modular lifts do not do so.

### C182 — the hard carry is a hidden reciprocal, and one quarter is enough

**Status:** promoted as P175 after F198 passed a primary-source hostile audit
and a strict statement-only reconstruction.

Let \(A=(-1)^B\binom{N-1}{B}\), let
\(h=(A-(1-q))/N\), and define the public polynomial-time residue

\[
z_t=N^{-1}(A-1)\pmod{2^t}.
\]

The exact missing coordinate is

\[
h-z_t\equiv p^{-1}\pmod{2^t}.
\]

Thus the beta-two quotient carry is not an opaque block of an exponentially
large integer. After subtracting a public value, it is exactly the low
2-adic block of the smaller prime, written reciprocally.

Half precision recovers \(p\) outright. More importantly, precision

\[
t=\left\lfloor\frac14\log_2N\right\rfloor-(\log n)^{O(1)}
\]

already factors deterministically in numerical-QP time. One can invoke the
2025 known-residue-class terminal directly with modulus \(2^t\), or extend
the polylogarithmic deficit and invoke Coppersmith's low-bit theorem.

**Strategic update.** The core target is now a quarter-length integer carry
or a QP chain that selects its bits. Generic ring operations cannot expose
this datum merely by rewriting the coefficient. The promising operations
must use integer order, Euclidean quotient, carries, or exact nonunit
division at the hidden index \(p\).

**Exact remaining gap.** Compute
\(p^{-1}\bmod2^{\lfloor(\log_2N)/4\rfloor-(\log n)^{O(1)}}\), or an
equivalent carry prefix, from \(N\) in QP time. F198 is a terminal reduction,
not an evaluator.

### C183 — the reciprocal congruence space is smooth; the live selector is integer and adaptive

**Status:** promoted as P176 after F199 passed a fresh hostile audit and a
strict statement-only reconstruction.

The direct multiplicity idea does not identify the P175 reciprocal. Every
odd residue (u\bmod2^t) extends to a public solution

\[
P=u^{-1},\qquad Q=Nu,\qquad H=z+u,
\]

and the resulting solution scheme is the smooth unit torsor
((\mathbb Z/2^t)[U,U^{-1}]). The true (p^{-1}) is one ordinary point
among (2^{t-1}) candidates. The public coefficient offsets also satisfy an
everywhere-smooth recurrence, including at the hidden transition (p-1).
Only the unavailable integer quotient word contains the one-spike error.

Low-degree Boolean holdout does not repair this. A nonzero degree-(d)
multilinear function on the (m=t-1) candidate bits has support at least
(2^{m-d}), while order-two Hasse vanishing at every candidate except one
already forces vanishing at that candidate through a neighbor. Both binary
lifts also satisfy every current congruence and the standalone balance
inequalities.

**Important surviving route.** This does not obstruct an adaptive chain.
A polylogarithmic prefix cell has a QP-size feature representation, and a
polynomial number of one-child stages remains QP. The missing object is now
precise: a nonlocal integer syndrome that selects the correct prefix cell.
It must use canonical representatives, exact divisibility, Euclidean
quotients, carries, or another genuinely integer operation. Generic local
ring jets cannot supply it.

### C184 — the missing carry is a one-denominator delta; Haar finds a path but cannot orient it

**Status:** promoted as P177 after F200 V2 passed a fresh hostile re-audit
and a strict statement-only reconstruction. The failed V1 packet remains
preserved.

The exact rational word

\[
x_j=\frac{(-1)^{j-1}\binom{N-1}{j-1}}j
\]

is integral at every (1\le j\le B\) except (j=p), where its fractional
part is (1/p). Therefore (x\bmod\mathbb Z) is exactly a point mass at
(p). The P175 carry is the negative ordinary floor of the root sum.

This makes the harmonic picture precise. Walsh and Fourier are dense. Haar
is maximally sparse: one coefficient per scale, on the root-to-(p) path.
But every proposed path admits the same finite (2)-adic additive correction.
Only the actual Archimedean floors distinguish the true path.

**Exact remaining gate.** For a proposed reciprocal-prefix cell, decide in
QP time whether its arithmetic progression contains (p). Exact rational
integrality, an endpoint gcd, an index-product gcd, and exact high-order phase
support all implement this selector, but each is already factor-bearing.
Literal endpoint materialization and uniform sampling cost
(N^{1/4+o(1)}). A nonlinear statistic of the actual integer parts or an
implicit exact phase evaluator remains open.

### C185 — gamma duplication has the right one-child tree but its first remainder drops the factor

**Status:** promoted as P178 after F201 passed a fresh hostile audit and a
strict statement-only reconstruction.

Split one dyadic arithmetic-progression cell containing \(p\) into its two
interlaced children and remove at most one public extra endpoint by a gcd.
If \(E\) and \(O\) are the equal-size sibling products, then exactly one is
divisible by \(p\), but interlacing gives

\[
1<O/E<2.
\]

The exact Euclidean quotient is therefore one. Its first remainder
\(D=O-E\) is not divisible by \(p\) in either orientation. Reversing the
division returns the original exponential child. Rising-factorial and gamma
duplication formulas represent the same pair and do not change this loss.
At P175 precision, explicitly writing \(D\) already needs
\(2^{\Theta(n)}\) bits.

**Recursion correction retained.** The dyadic tree itself is valid: a QP
selector would follow one child for only \(O(n)\) stages, and a unique
\(n-1\)-bit child remains QP. The failure is not weak contraction. It is the
loss of guaranteed factor support before a smaller child exists. The live
route is an implicit modular AP-product evaluator, a nonlinear
Archimedean/carry syndrome, or a different support-preserving child.

### C186 — a twisted divisor coefficient is the exact beta-two orientation bit

**Status:** promoted as P179 after F203 passed a fresh hostile audit and a
strict statement-only reconstruction.

Given a correct prefix \(p^{-1}\bmod m\), define the signed two-lift weight
\(w_{m,r}\) on the two residue classes above \(r=p\bmod m\). The exact
coefficient

\[
S_{m,r}(N)=\sum_{d\mid N}d\,w_{m,r}(d)
=[X^N]\sum_{a\ge1}\frac{a w_{m,r}(a)X^a}{1-X^a}
\]

has only three possible corrected values: a signed \(p\), \(p+q\), or
\(p-q\). It therefore selects the next reciprocal bit and factors. At the
first stage it is the fixed \(\chi_4\)-twisted divisor sum. This is the first
exact nonlocal integer coefficient known to retain the orientation that the
ring congruences and AP sibling remainder lose.

The natural smaller quotient \(K=(N-rc)/m\) is a unit and has fewer bits,
but its two next states coalesce exactly when the factors occupy opposite
sibling classes in the same parent. In particular, they coalesce at the
first stage for every \(N\equiv3\pmod4\). Thus safe contraction does not
imply a usable lift.

**Recursion qualification.** A globally nested one-child construction would
still be QP. The theorem does not construct it. One call per local selector
stage is not enough unless the complete recursion tree is also shown to be a
single nested chain or is otherwise amortized.

**Exact remaining gap.** Evaluate the twisted divisor coefficient in QP,
or extract only its sign through a nonlinear integer statistic. The active
subroutes are the associated \(q\)-product coefficient, joint use of the
factored children \((N-1)/2\) and
\(N-\lfloor\sqrt N\rfloor^2\), and a direct adaptive reciprocal-prefix
syndrome.

### C187 — the factored square gap exposes a mixed class but not its orientation

**Status:** promoted as P180 after F202 passed a fresh hostile audit and a
strict statement-only reconstruction.

The canonical child

\[
E=N-\lfloor\sqrt N\rfloor^2
\]

has roughly half the input bits and is safe to factor recursively inside an
already correct all-input routine. Exact square-gap coordinates reduce the
parent to an even offset \(d\), a mixed square root of \(-E\bmod N\), or a
specific square \(C^2\) in the proper class group of discriminant \(-4E\).

The literal information supplied by \(\operatorname{factor}(E)\) does not
select that object. Every unit candidate factor residue passes product and
discriminant-square consistency modulo every divisor of \(E\). The desired
mixed class lies in the principal genus, so all genus characters are
trivial on it. The exact instance \(N=2627,E=26\) has neither a second
factor-bearing principal norm nor a mixed class in the subgroup generated by
the ramified two-torsion classes.

**Recursion qualification.** The child need not be a balanced semiprime.
Thus the cost statement assumes an all-input factor routine on arbitrary
smaller integers. The promise-specific postprocessor alone does not define
the recursion.

**Exact remaining gap.** Test whether joint access to the factorizations of
\((N-1)/2\) and \(E\) supplies a new nonlocal orientation. The recurrence
with one near-size spine and fixed-ratio side children can still be QP, so
this combined route cannot be dismissed by contraction accounting.

### C188 — the binary q-product norm modularizes only by deleting the selector

**Status:** promoted as P181 after F204 passed a fresh hostile audit and a
strict statement-only reconstruction.

For the first P179 coefficient

\[
A(n)=\sum_{d\mid n}d\chi_4(d),
\]

the natural product \(P=(q;q^4)_\infty/(q^3;q^4)_\infty\) satisfies
\(P(q)P(-q)=P(q^2)\). Its logarithmic derivative yields only
\(A(2n)=A(n)\); every odd logarithmic coefficient is a free parameter of
the norm equation.

Inside the binary monomial orbit \(P(q)^aP(-q)^b\), the necessary scalar
cusp powers force \(a=b\), while the odd target coefficient is
\((a-b)A(N)\). Thus scalar modularization loses the selector exactly.
The mod-two coefficient sequence has an infinite two-kernel, excluding a
fixed linear binary Mahler equation, and fixed odd-prime root norms reproduce
only the usual divisor-sum recurrence.

**Exact remaining gap.** The source is still live outside these named
models. Test a genuinely vector-valued or nonholomorphic transformation only
if it returns a smaller arithmetic state, and prioritize the joint factored
children and adaptive integer-prefix routes. A restatement that outputs the
coefficient itself is factoring-equivalent and is not progress.

### C189 — the natural vector completion moves the selector but does not contract it

**Status:** promoted as P182 after F206 passed a fresh hostile audit and a
strict statement-only reconstruction.

The first twisted divisor coefficient has a natural two-kernel Mellin
completion, but it does not yield a smaller coefficient. The product and
Lambert series have incompatible polynomial powers at cusps \(0\) and
\(1/2\), excluding fixed projections of ordinary finite-dimensional
semisimple meromorphic vector modular forms. The pure two-kernel reflection
contains unavoidable \(\tan(\pi s/2)\) and \(\cot(\pi s/2)\) factors; finite
rational or Eichler repairs cannot cancel their infinite pole-zero pattern.

A Whittaker correction can absorb the archimedean factor, but its companion
coefficient is

\[
A^\vee(N)=\chi_4(N)A(N)
\]

for odd \(N\). Thus the hard amplitude remains at index \(N\), up to a
public sign. The completion supplies no one-child arithmetic contraction.

**Exact remaining gap.** Continue only with a completion carrying genuinely
new arithmetic coefficients and an explicit smaller state, or with the
integer-specific adaptive selector. Nonsemisimple/logarithmic data,
new mock shadows, QP-growing state, nonlinear identities, and adaptive
integer decoders remain open.

### C190 — one-bit recursion is legal; joint child congruences remain inversion-blind

**Status:** promoted as P183 after F207 passed a fresh hostile audit and a
strict statement-only reconstruction.

The corrected recurrence is now explicit. If \(Q\) is numerical QP and

\[
T(n)\le T(n-1)+Q(n)T(\rho n+O(1))+Q(n),\qquad 0<\rho<1,
\]

then \(T\) is numerical QP. The decrement spine costs one extra power of
\(\log n\) in the exponent; fixed-ratio side calls occur at only
\(O(\log n)\) scales. A weak one-bit contraction is therefore fully valid.

Factoring both \(K=(N-1)/2\) and the half-size square gap
\(E=N-\lfloor\sqrt N\rfloor^2\) is also complexity-safe on the balanced
branch. Their joint congruence state constructs \(M=\operatorname{lcm}(K,E)\)
and \(R^2=N\pmod M\), but every candidate pair is

\[
(Ru,Ru^{-1}),\qquad u\in U(M).
\]

The torsor has exponentially many points and factor swap is inversion.
Symmetric, quadratic, Jacobi, and genus data cannot orient it.

**Exact remaining gap.** Use the valid recursion with a genuinely
nonsymmetric integer statistic: Archimedean size, exact division, a
nonquadratic operation, or an adaptive reciprocal-prefix syndrome.

### C191 — floor and representation transforms expose the divisor spike but do not compress it

**Status:** promoted as P184 after F208 passed a fresh hostile audit and a
strict statement-only reconstruction.

For the twisted coefficient

\[
A(N)=\sum_{d\mid N}d\chi_4(d),
\]

the hidden orientation is exactly

\[
\chi_4(p)=\sum_{2\le d\le\lfloor\sqrt N\rfloor}
\chi_4(d)\left(
\left\lfloor\frac Nd\right\rfloor-
\left\lfloor\frac{N-1}{d}\right\rfloor
\right).
\]

Totalized floor reciprocity has correction
\((\gcd(d,N)-1)/2\), so its promised contraction is the hidden gcd spike
itself. Dedekind/cotangent reduction, HNF shells, diagonal forms,
pair-symmetric representation totals, and exact magnitude all relocate or
erase the same event; none evaluates it more cheaply.

**Exact remaining gap.** The core is a nonlinear compressed signed divisor
OR, or an equivalent adaptive integer-prefix selector. This is where new
integer-specific structure must enter.

### C192 — the joint-child CRT torsor becomes geometrically rigid before full disclosure

**Status:** preregistered remote experiment F209-D01 completed with the
predeclared `strong_finite_geometry_lead` verdict. This is finite evidence,
not a promoted theorem.

After factoring (K=(N-1)/2) and
(E=N-\lfloor\sqrt N\rfloor^2), F209 revealed the prime-power components of
(M=\operatorname{lcm}(K,E)) in a fixed public order. At each prefix modulus
it constructed every product-consistent residue pair that still had
representatives in the two balanced factor intervals. Hidden factors were
used only for audit labels.

Across 5,858 primary rows, the public frontier always oriented and decoded
the true pair. Every holdout row decoded before the last CRT component. The
largest frontier was 209,664 and the largest generator count was 1,642,142,
both below the frozen (n^4) proxy on the tested range. The median decoding
modulus had about (0.568\log_2N) bits, and the holdout retained one to four
unrevealed components at decode.

The experiment did **not** produce a QP algorithm. In 5,840 of the 5,858
primary rows, construction still enumerated the full
(\Theta(\sqrt N)) balanced interval. The geometry prunes and orients after
the candidates exist; the current generator is exponential in the input bit
length.

**Exact remaining gap.** Given factored (m\mid\operatorname{lcm}(K,E)),
find, count, or isolate without interval enumeration a solution of

\[
x\in(\sqrt{N/2},\sqrt N),\qquad
Nx^{-1}\bmod m\in(\sqrt N,\sqrt{2N}),
\]

subject to the balanced product range. The useful structure is integer and
Archimedean; a generic ring-torsor operation does not see it.

### C193 — complete dyadic quotient-child factorizations do not orient in the frozen bank

**Status:** preregistered remote experiment F210-D01 completed as a
fixed-family null. This is finite evidence, not a theorem.

At every granted P175 reciprocal-prefix stage, the experiment constructed
the two compatible quotient children and the two crossed quotient children,
factored all four completely, and ran a frozen branch-equivariant menu of
integer statistics and modular actions. It separated early near-size rows
from the P183-safe late cohort before fitting any rule.

On the disjoint holdout, the late-safe selected rule had balanced accuracy
(0.478791), with 2,112 errors among 4,036 surviving rows. Its direct public
action bank factored only (79/4,115=1.9198\%\) of the late rows and has
explicit failures. The early cohort was likewise null. Literal compatible-
child coalescence occurred often, but the crossed children never coalesced;
their additional factorizations still did not orient under the frozen menu.

**Exact remaining gap.** This rejects only the tested child statistics and
action schedule. A theorem can still use a new nonlinear relation among the
four children, a different recursive invariant, or an implicit
Archimedean selector. The valid one-bit recursion correction remains fully
in force.

### C194 — dyadic quotient siblings are locally identical; the balanced integer point is the distinction

**Status:** promoted as P185 after F210 V2 passed a fresh hostile re-audit
and a strict statement-only reconstruction.

Given a correct reciprocal prefix modulo \(m=2^t\), the two legal quotient
children have exact public formulas, coalesce exactly in the
\(\delta=1,r=c\) case, and share prime support only through a small public
difference. Their quotient curves are related over \(\mathbb Z[1/2]\) by
the half-translation

\[
F_1(P-1/2,Q-(-1)^\delta/2)=F_0(P,Q).
\]

After physical-coordinate alignment both are simply \(XY=N\). Odd-local
point counts, Frobenius data, genus data, aligned eliminants, and finite
two-adic lift multiplicities therefore do not select the next bit. The true
chart is distinguished by the nontrivial balanced integer point
\(1<X<\sqrt N<Y<N\), not by local existence.

Factoring both children can conditionally yield a factor or a fully known
common local order through simultaneous exponent return. It is recursion-safe
at the P175 late precision because both calls have fixed-ratio size. The
theorem does not force return, order growth, or a child choice.

**Exact remaining gap.** Construct an implicit Archimedean test for the
balanced point, a guaranteed asymmetric support/action transition, or a
globally nested one-spine selector. Early two-near-size branching remains
outside P183; one-bit single-child descent remains valid.

### C195 — the F209 frontier is either the full torsor or the divisor spike outside square-root scale

**Status:** promoted as P186 after F212 V2 passed a fresh hostile audit and
a strict statement-only reconstruction.

The balanced interval frontier has an exact phase transition. If
\(\operatorname{lcm}(2,m)\le\sqrt N/8\), every unit residue survives. If
the progression step exceeds both interval widths, every progression is a
singleton and survival is exact divisibility. In particular, at
\(K=(N-1)/2\), the modular hyperbola-in-a-box is exactly the unique factor
pair; its count is the hidden floor-difference divisor spike.

A QP-size list containing a factor residue modulo some
\(m\ge N^{1/4+\varepsilon}\) is sufficient for deterministic QP
postprocessing by Coppersmith. The list itself must be generated in QP time;
its output-size bound alone is not an algorithm.

**Exact remaining gap.** Generate such a large-modulus residue list without
enumerating the torsor, or solve the implicit modular box at
\(m=\Theta(\sqrt N)\). Below that scale the declared geometry supplies no
pruning; above it the predicate has already become exact divisibility.

### C196 — higher scalar reciprocity preserves the inverse torsor; additive trace is the missing object

**Status:** promoted as P187 after F215 passed a fresh hostile audit and a
strict statement-only reconstruction.

For every (d\mid K=(N-1)/2), the beta-two factors satisfy
(q\equiv p^{-1}\pmod d). Their cyclotomic Frobenius elements are inverse,
their decomposition subgroups agree, genus values coincide, and every
declared scalar Artin, ray, residue-symbol, or Hilbert product is public.
Adaptive use of such scalar products eliminates no candidate in the
inverse torsor.

A coherent ring-valued element with different full rational cyclotomic
components would already factor (N) by coefficient-content gcd. Additive
character traces separate inversion orbits, but their required values are
exactly the unevaluated divisor coefficients

\[
\sum_{d\mid N}\chi(d)=2+\chi(p)+\chi(p)^{-1}.
\]

**Exact remaining gap.** Evaluate and decode a QP separating trace bank,
construct a coherent non-diagonal carrier without already exposing a
coefficient zero divisor, or use nonabelian/Archimedean structure. More
scalar reciprocity identities only re-express the public product.

### C197 — recursively factored near-square norm banks can still have only global roots

**Status:** promoted as P188 after F213 passed a fresh hostile audit and a
strict statement-only reconstruction.

There is an explicit composite family (N=s^2+1) with a polynomial public
bank for which

\[
r_a=as,\qquad E_a=a^2,
\qquad F_a=2as+1-a^2.
\]

Every direct gcd is trivial. Each (F_a) has its own valuation-one private
prime row, so every parity dependency excludes all adjacent norms and uses
an even subset of the square (E_a) columns. Its normalized root is always
(s^k=(-1)^{k/2}\), hence global. Odd sign-free subsets recover only the
public root (\pm s) of (-1).

The children have fixed-ratio bit length and the bank is polynomial, so
complete recursive factorization fits P183. The obstruction is therefore
the private-row/global-root image, not weak contraction.

**Exact remaining gap.** A useful near-square route needs an arithmetic law
that defeats private rows, or a nonlinear/Archimedean decoder. Cardinality,
small children, complete child factorization, and parity nullity alone do
not suffice.

### C198 — the full inverse box is exact factor recovery, not a weaker intermediate

**Status:** promoted as P189 after F214 V2 passed a fresh hostile re-audit
and a strict statement-only reconstruction.

For balanced \(N=pq\), the full modulus \(K=(N-1)/2\) rigidifies the
modular hyperbola completely. Any

\[
\sqrt{N/2}<X<\sqrt N<Y<\sqrt{2N},\qquad XY\equiv N\pmod K
\]

has \(|XY-N|<K\), hence \(XY=N\) and \((X,Y)=(p,q)\). The product-range
predicate is redundant at full disclosure.

Literal interval and unit scans, explicit paired CRT, explicit CRT-MCSS
half lists, direct determinant/continued-fraction completion, the published
direct bivariate Coppersmith range, and termwise Fourier expansion all stay
exponential for exact, separately proved reasons. These conclusions apply
only to those named explicit representations.

The recursion correction is preserved. The local child \(K\) loses one bit,
but it need not inherit the balanced promise. QP accounting follows only
inside an independently correct all-input dispatch satisfying P183; the
balanced selector alone does not close recursion.

**Exact remaining gap.** Find an implicit exact counter or locator for the
unique modular-hyperbola point, a compressed CRT/MCSS decoder, a nontermwise
harmonic evaluator, or another integer-specific Archimedean selector. The
full-box equivalence itself gives no algorithm.

### C199 — deep dyadic trace lifting keeps constant-density ambiguity

**Status:** promoted as P190 after F216 passed a fresh hostile audit and a
strict statement-only reconstruction. The remote finite check is only a
cross-check because its preregistration timing lacks immutable provenance.

For every odd \(N\), the trace image

\[
W_t(N)=\{u+Nu^{-1}\pmod{2^t}:u\in U(2^t)\}
\]

reduces by public square-class scaling to \(N\bmod8\). The normalized
classes \(3\) and \(7\) are complete progressions modulo eight, class \(5\)
is two progressions modulo 32, and class \(1\) has an exact valuation-stratum
decomposition. Uniformly,

\[
|W_t(N)|\ge2^t/48.
\]

At quarter-bit precision, explicit trace materialization is still
exponential. This is not a generic ring obstruction: it is the exact
integer-specific behavior of the dyadic reciprocal trace.

**Exact remaining gap.** Keep the oriented inverse parameter, combine odd
moduli, or find an implicit Archimedean/interval statistic. A projected
trace alone discards almost every reciprocal-prefix bit.

### C200 — the trace bank compresses to one integer divisor coefficient

**Status:** promoted as P191 after F217 passed a fresh hostile audit and a
strict statement-only reconstruction.

On the balanced \(N\equiv3\pmod4\) branch with
\(K=(N-1)/2\), the full scalar-character bank is not the core output-size
problem. Conditional on separately supplied cyclic coordinates and a trace
evaluator, at most \(2r-1\) character traces recover \(p\) up to inversion.
More directly, the tautological group-ring map gives

\[
\sigma_1(N)\equiv2+p+q\pmod K.
\]

Except for \(N=15\), this residue is the exact integer \(2+p+q\) and
therefore factors \(N\). The same target is a binary-described high-weight
level-one Eisenstein coefficient modulo \(K\), and for prime \(K\) it is the
first \(K\)-adic coefficient of an explicit eta quotient.

All standard implementations still materialize numeric weight, numeric
level, \(N\) coefficient positions, or the Ramanujan term at \(m=p\). These
are named-model boundaries, not a lower bound on compressed evaluation.

**Exact remaining gap.** Evaluate \(\sigma_1(N)\bmod K\), exactly or through
a verifiable Las Vegas observable with inverse-QP success; equivalently,
construct a compressed Hecke/Eisenstein/eta coefficient evaluator. Randomness
must enter the integer coefficient or its hidden carry. A generic random
group element need not have inverse-QP return probability.

### C201 — standard moving-weight fast-forward preserves the affine target

**Status:** promoted as P192 after F218 passed a fresh hostile audit and a
strict statement-only reconstruction. Its frozen remote run failed before
Python started and is not evidence.

Modulo each prime power of the factored \(K\), the binary high-weight
coefficient from P191 is exactly the corresponding \(\ell\)-depleted
weight-two Eisenstein coefficient. The prime-level eta quotient has the same
first \(r\)-adic coefficient. Thus neither construction produces a second
observable.

The standard big-Witt \(K\)-supported operations preserve the rough part of
the coefficient index and cannot turn \(N=2K+1\) into a smaller index.
Frobenius compression of a theta power retains a nonzero cusp contaminant.
The affine coefficient sequence \(\sigma_s(rj+1)\bmod r\) is not eventually
periodic for any prime \(r\) and positive \(s\), excluding every fixed
finite linear Cartier recurrence.

**Exact remaining gap.** Use nonlinear or QP-growing state, an exact cusp
projector, additive index mixing, or a randomized integer observable with a
verifiable inverse-QP success event. Fixed linear state and multiplicative
index motion do not reach the affine divisor coefficient.

### C202 — uniform modified-AKS shifts do not supply Las Vegas progress

**Status:** promoted as P193 after F222 V2 passed a fresh hostile audit and a
strict statement-only reconstruction. Its preregistered remote run is finite
guidance only.

For

\[
E_a(X)=(X+a)^N-X^N-a^N\pmod{X^r-1,N},
\qquad N=pq,\quad d=q-p,
\]

the hidden gap controls the exact polynomial degrees. In the regime
(r<d<p-1), a complete raw coefficient scan and the full
resultant/local-nullity channel for a fresh uniform unit shift have combined
success probability at most

\[
{2rd\over p-1}+{rd(r+3)\over q-1}.
\]

Baker--Harman--Pintz supplies infinitely many balanced pairs with
(d=\Theta(p^{3/5})). Even an adaptive numerical-QP bank, provided it fixes
each (r) before drawing that fresh shift, therefore succeeds with total
probability only (2^{-\Omega(n)}).

This is integer-specific: it uses both local Frobenius collapses, the actual
factor gap, and exact polynomial root counts. Randomness alone does not turn
the modified AKS error into a dense source.

**Exact remaining gap.** Bias the integer shift using carry or interval
information, choose a verifiably useful distribution, process the typical
nonzero coefficient vector jointly, or construct another integer observable
with an inverse-QP certified-progress law. A modulus selected after seeing
the same shift and multi-shift elimination also remain open.

### C203 — the certified factor AP has a Fermat terminal, not a useful uniform AKS sampler

**Status:** promoted as P194 after F224 passed a fresh hostile audit and a
strict statement-only reconstruction. The approved D02 remote run is finite
guidance only; the preserved D01 wrapper failure produced no mathematical
work.

If (p\equiv s\pmod L), then
(q\equiv Ns^{-1}\pmod L). The Fermat midpoint ((p+q)/2) therefore lies
in one public class modulo (L/\gcd(2,L)). Scanning this AP from
(sqrt N) reaches the midpoint in fewer than

\[
1+{(q-p)^2\over4pL}
\]

square tests. Thus the certified residue is already a deterministic QP
terminal whenever ((q-p)^2/(pL)=\operatorname{QP}(n)). This combines
directly with (L=\operatorname{lcm}(2^t,M)); it needs no single element
whose exact order is (M).

On the other hand, let (H) be the size of the balanced factor cell. For
(r<q-p<p-1), at most (r(q-p)(r+5)) off-target cell integers activate
the complete P193 coefficient or resultant/nullity channels. A uniform
shift succeeds with probability at most

\[
{1+r(q-p)(r+5)\over H}.
\]

For every fixed (epsilon>0) and gap
(q-p\le p^{2/3-\epsilon}), the two scales meet exactly: either capped
AP--Fermat factors, or every numerical-QP adaptive bank of fresh uniform AP
shifts has total success (2^{-\Omega(n)}).

**Exact remaining gap.** Obtain a nonuniform integer law with a proved
useful heavy atom, process the full nonzero coefficient transcript, enlarge
the accumulated common modulus (M), or reveal the next dyadic carry bit.
The large-gap regime (q-p\ge p^{2/3-o(1)}) also remains outside this
phase theorem.

### C204 — a fixed AKS shift with a random point is sparse even for a linear-size gap

**Status:** promoted as P195 after F225 passed a fresh hostile audit and a
strict statement-only reconstruction. No computation was used.

For

\[
H_N(x)=(x+1)^N-x^N-1,qquad c=2p-q\ge3,
\]

the exact local Frobenius reductions give at most (2c-2) roots modulo
(p) and at most (2c+2) roots modulo (q). The latter count uses four
quadratic-character cells; the former uses a degree (2(c-2)) reciprocal
polynomial. Therefore a fresh uniform unit point yields a proper gcd with
probability at most

\[
{4c-2\over p-1}.
\]

Baker--Harman--Pintz supplies infinitely many balanced pairs with

\[
q-p=\Theta(p),\qquad 2p-q=\Theta(p^{3/5}).
\]

On this family, even a numerical-QP adaptive bank of fresh uniform points
has total success (2^{-\Omega(n)}). Large gap alone therefore does not
repair the scalar random-evaluation channel left outside C203.

**Exact remaining gap.** The point law must use factor-correlated integer
bias, or the decoder must use joint nonzero data. Variable shifts,
coefficient/rank observables, same-value adaptivity, and certified growth of
the accumulated modulus (M) remain live.

### C205 — APR/CL contributes only after its local exponents are globally compatible

**Status:** promoted as P196 after F223 V2 passed a fresh hostile re-audit
and a strict statement-only reconstruction.

At one auxiliary prime (q), all character equations share an exponent if
and only if the hidden factor lies in (\langle N\rangle\bmod q). Across
several rows, these exponent classes must also satisfy generalized-CRT
compatibility. Cohen--Lenstra condition (6.4), not independent local
acceptance, supplies the shared primary exponents needed for this step.

Once a compatible certificate gives

\[
r\equiv N^i\pmod S
\]

for each hidden prime and one of QP-many public exponents, it combines
cleanly with the beta-two low bits and the aggregate divisibility
certificate (M\mid r-1). The resulting modulus

\[
L=\operatorname{lcm}(2^\tau,M,S)
\]

feeds the known-residue terminal at
(L\ge N^{1/4}/\operatorname{QP}(n)). No single common-order generator is
needed.

Fixed finite banks have infinite balanced counterfamilies, generic
independent-residue tails are only a model, and the uniform primary-2 anchor
is exponentially sparse on bounded-gap pairs. The exact witness
(1088340091=32987\cdot32993) has a standard auxiliary product above
(\sqrt N) but only the vacuous row 2 is locally accepted.

**Exact remaining gap.** Produce an adaptive integer-derived compatible
orbit certificate, or prove inverse-QP drift for accumulated primary support.
Rejected APR/CL rows and typical nonzero transcripts remain possible joint
sources; they cannot be replaced by unrelated local exponents.

### C206 — the Las Vegas target is lcm-potential drift, not one common-order generator

**Status:** promoted as P197 after F220 V2 passed a fresh hostile re-audit
and a strict statement-only reconstruction.

For a factored annihilator (A), each test

\[
\gcd(a^{A/\ell}-1,N)=1
\]

certifies the full primary power (\ell^{v_\ell(A)}) in every hidden
(r-1). These blocks can come from unrelated witnesses and accumulate by
lcm. Combining their modulus (M) with the beta-two residue gives

\[
L=\operatorname{lcm}(2^t,M),
\]

and the exact terminal target is
(J_{\rm G}=\lceil N^{1/4}/\operatorname{QP}(n)\rceil).

The potential

\[
\Phi(L)=\max\{0,\lceil\log_2(J_{\rm G}/L)\rceil\}
\]

has only (O(n)) levels. A uniform inverse-QP conditional probability of a
factor or a block not already dividing (L) gives an expected-QP Las Vegas
algorithm for this conditional terminal. F220 gives the exact primary-level
probability law for a uniform unit and arbitrary odd prime powers.

The hidden ceiling is
(D_N=\gcd_{r\mid N}(r-1)). Bounded gaps can keep both the ceiling and the
uniform useful probability tiny. A synchronized cyclic source can fill its
available primary support quickly but cannot escape its direction.

**Exact remaining gap.** Construct an integer-derived witness schedule with
inverse-QP conditional new-support mass before the actual threshold. The
condition must hold for every reached state and include the full per-stage
bit cost. Randomness is useful after a dense source exists; uniformity alone
does not create that source.

### C207 — exact-uniform half-size integer children remove hidden subset selection, not harmonic-support scarcity

**Status:** promoted as P198 after F226 passed a fresh hostile audit and a
strict statement-only reconstruction.

For \(m=\lfloor n/2\rfloor\), a uniform odd multiplier makes

\[
R_m=uN\bmod 2^m
\]

exactly uniform over the odd half-size integers. Its binary prefixes form a
QP-size bank of half-size recursive children. QP many such banks have a QP
recursion tree, conditional on a correct all-input dispatcher for the
arbitrary children. The full child-value ensemble is independent of \(N\),
and a fixed auxiliary prime \(\ell\) is sampled with probability essentially
\(1/\ell\).

For \(N=pq\), an auxiliary prime compatible with exponent \(i\) divides the
hidden integer \(N^i-p\). A polylogarithmic block can factor its sampled
children and enumerate every squarefree divisor below a public QP cap. This
removes the oracle that would otherwise have to identify the compatible
subset. If a sampled compatible subproduct closes the beta-two residue
threshold, the verified known-residue terminal factors \(N\).

In the strongest unconditional favorable state, if a hidden odd squarefree
\(d\le Q(n)\) divides \(p-1\) or \(q-1\), already closes the terminal gap,
and \(4d\le2^m\), a public cap gives success probability at least
\(1/(4Q(n))\) without knowing \(d\).

**Exact remaining gap.** Prove that every preterminal input has inverse-QP
harmonic mass in some compatible support, or extract progress from the
integer multiplier/quotient labels that the \(N\)-independent child-value
ensemble discards. Uniform auxiliary values alone cannot prove this: support
above a chosen QP cutoff has only QP-over-cutoff expected log weight, and a
single terminal-size small-order prime is exponentially sparse.

### C208 — Las Vegas small-integer sampling needs an intermediate nonuniform word law

**Status:** promoted as P199 after F229 passed a fresh hostile audit and a
strict statement-only reconstruction.

On one infinite fixed-gap family \(q=p+d\), the \((N-1)\)-annihilator stage
collapses exactly to the degree-\(d\) integer:

\[
\gcd(X^{N-1}-1,N)=\gcd(X^d-1,N).
\]

Every global-return local order and every certified common primary block
divides the fixed \(d\), so lcm accumulation from this source never exceeds
\(d\). Every fixed numerical-QP-value integer is too small even to wrap.
A fresh uniform integer from an arbitrary history-selected initial interval
has only exponentially small useful probability. At the other extreme,
even a granted exact-uniform element of the full subgroup generated by all
small rational primes has exponentially sparse \(d\)-torsion, because the
projected subgroup contains \(p^{1-o(1)}\) distinct smooth residues.

**Exact remaining gap.** Construct a long, nonuniform integer word whose
quotient or carry in \(X^d-1\) is factor-correlated and has inverse-QP
history-wise factor/new-block mass. The law must sit between the two failed
extremes: before factor-scale wrap there is no event, while complete mixing
dilutes the target torsion. This is the precise Las Vegas source problem;
randomness alone is not the missing ingredient.

### C209 — zero carry defect turns quotient sampling into an odd-order residual test

**Status:** promoted as P200 after F230 passed a fresh hostile audit and a
strict statement-only reconstruction.

For the half-size radix \(B=2^{\lfloor n/2\rfloor}\), a quotient carry
defect can vanish only when \(B\mid N-1\). Then every shifted quotient child
in the zero branch is

\[
A_u=uH,
\qquad H=(N-1)/B.
\]

Writing the odd local orders as \(P=Ds_p\), \(Q=Ds_q\), with coprime
residuals, a uniform unit projected to odd order has exact return
probabilities

\[
{\gcd(u,s_p)\over s_p},
\qquad
{\gcd(u,s_q)\over s_q}.
\]

If one residual is at most a public numerical-QP bound \(U\), scanning odd
\(u\le U\) gives a factor or strict common-primary growth with conditional
probability at least \(4/9\) at every preterminal history, provided the full
odd common capacity \(D\), together with the beta-two bits, reaches the
quarter-bit terminal. One random multiplier loses only a factor
\(O(U)\). If both residuals are exponential, the same bounded uniform source
has exponentially small mass.

**Exact remaining gap.** Force one residual odd order to be QP-small, or
replace the bounded multiplier by a QP-bit long integer word that absorbs
the residual smooth support. The zero branch also still relies on a correct
all-input dispatcher to factor the arbitrary half-size integer \(H\).

### C210 — Las Vegas exponent sampling needs integer-biased bases, not diffuse candidates

**Status:** promoted as P201 after F227 V5 passed a fresh hostile re-audit
and a strict statement-only reconstruction.

Inside the balanced beta-two factor cell, the average local return mass of
the candidate exponents \(x-1\) is controlled by an exact arithmetic-
progression gcd mean. Even after granting the complete factorization of
every candidate exponent, a numerical-QP diffuse candidate law followed by
a fresh independent uniform unit has exponentially small total factor or
new-common-block probability throughout the preterminal range.

For a fixed public base, the law changes completely. If

\[
u_p={\operatorname{ord}_p(a)\over
\gcd(\operatorname{ord}_p(a),L)},
\]

then returning candidates form one exact progression of density \(1/u_p\).
A nonstale base with \(u_p\le\operatorname{QP}(n)\) therefore gives
inverse-QP verified progress. P161 roughness forces this favorable regime to
be \(u_p=1\), so the base must have local order already dividing \(L\) on
one side without being synchronized and stale on both.

**Exact remaining gap.** Construct that nonstale integer-biased base with
inverse-QP conditional probability at every state. The theorem's child
factorization cost is only oracle-relative because \(x-1\) is an arbitrary
even integer; a correct all-input dispatcher remains independently missing.

### C211 — a smooth QP-bit word gives constant Las Vegas drift after one residual saturates

**Status:** promoted as P202 after F231 passed a frozen hostile re-audit and
a strict statement-only reconstruction.

In the zero-defect branch \(B\mid N-1\), write the odd local orders as
\(P=Ds_p\), \(Q=Ds_q\), with coprime residuals. For any public completely
factored word \(W\), a fresh uniform unit projected to odd order and tested
at exponent \(WH\) has exact local return probabilities

\[
1/r_p,
\qquad 1/r_q,
\qquad
r_j=s_j/\gcd(s_j,W).
\]

Complete factor-first stripping gives the exact factor-or-new-block law

\[
{1\over r_p}+{1\over r_q}-{1\over r_pr_q}
-{1\over PQ}\sum_{d\mid M}\varphi(d)^2.
\]

The last term is precisely the simultaneous stale atom. This is the quantity
that a Las Vegas source must control; marginal return probability alone is
not progress.

The word \(U_Y=\operatorname{lcm}(1,\ldots,Y)^n\) has numerical-QP bit
length for numerical-QP \(Y\) and absorbs every \(Y\)-smooth residual,
regardless of its numerical value. The complete factorization of the
half-size child \(H\) allows the word to absorb every residual prime also
occurring in \(H\), at only \(O(n^2)\) extra bits. If one residual is fully
absorbed, every history has factor-or-strict-lcm-growth probability at least
\(2/3\); the equal-residual edge is impossible in this branch. The process
therefore factors in at most \(3n/2\) expected stages, or reaches the
beta-two/aggregate-order terminal sooner.

**Exact remaining gap.** Produce such a QP-height residual-saturating word
on every input. After enriching by the primes of \(H\), the unresolved
support consists exactly of large primes \(\ell>Y\) with \(\ell\nmid H\).
The theorem also remains conditional on a correct all-input dispatcher for
the arbitrary half-size child \(H\).

### C212 — shifted quotient support is a projective cover of the hidden gap

**Status:** promoted as P203 after F233 passed a fresh hostile audit and a
strict statement-only reconstruction.

In the zero-defect branch, every shifted quotient child is

\[
A_{u,c}=uH+c.
\]

For an exclusive residual prime \(\ell\nmid H\), divisibility by one child
is exactly membership of the hidden ratio

\[
\rho_\ell=(q-p)B^{-1}\pmod\ell
\]

in the finite projective cover

\[
\{cu^{-1}:1\le u\le U,\ 1\le|c|\le C\}.
\]

The cover has at most \(2CU\) residues. It covers every nonzero residue only
at the small-prime scale, and a prime above \(2UC\) cannot occur at two
distinct rational slopes. Hence every residue-independent coverage guarantee
is already absorbed by a numerical-QP smooth word. This is an exact
integer-gap theorem, not a generic ring argument.

**Exact remaining gap.** Prove that the actual gap ratios hit enough large
rough residual support on every input, or replace the rectangular bank by a
different QP-bit integer word. Generic projective coverage and repeated lcm
aggregation do not provide this input-dependent law.

### C213 — Miller amplification removes word factorization and the half-child dispatcher

**Status:** promoted as P204 after F235 passed a fresh hostile audit and a
strict statement-only reconstruction.

For any public QP-bit integer word \(W\), put

\[
E=(N-1)W,
\qquad
r_j={s_j\over\gcd(s_j,W)}.
\]

One uniform-unit return test followed by a Miller square chain on the
verified global-return branch has exact factor probability

\[
{1\over r_p}+{1\over r_q}
-\left(2-{2\over3}(1-4^{-e})\right){1\over r_pr_q},
\]

where zero defect forces
\(e=v_2(p-1)=v_2(q-1)\ge1\). In particular,

\[
\Pr(\text{factor})\ge{1\over2\min(r_p,r_q)}.
\]

The word need not be factored. A global return does not become stale: its
independent local two-Sylow coordinates split with probability at least
one-half. Public child values can therefore be multiplied directly into
\(W\), and neither their factorizations nor the factorization of \(H\) is
needed for this direct-factor route.

**Exact remaining gap.** Construct a public QP-bit \(W\) that makes
\(\min(r_p,r_q)\) numerical QP for every zero-defect input. The meta-order
word \(\prod_{k\le K}(N^k-1)\) works when one residual order of \(N\) is
QP, but no all-input bound on that smaller meta-order is known.

### C214 — the unfactored-word Miller law holds for every odd semiprime

**Status:** promoted as P205 after F238 V2 passed a fresh hostile audit and
a strict statement-only reconstruction.

For arbitrary distinct odd primes (p,q), put

\[
d=\gcd(p-1,q-1),\qquad s_p=(p-1)/d,\qquad s_q=(q-1)/d.
\]

The public exponent (N-1) already contains exactly the full common factor
(d) of both local group orders. For any public unfactored word (W), the
exact local returns have probabilities

\[
1/r_p,\qquad1/r_q,qquad
r_i=s_i/\gcd(s_i,W).
\]

On a verified global return, the possibly unequal local two-primary kernels
remain independent. Their Miller mismatch probability is

\[
1-{4^a+2\over3\,2^{a+b}}\ge1/2.
\]

Therefore one trial factors with probability at least

\[
{1\over2\min(r_p,r_q)}.
\]

This removes balance and zero defect from P204. It also shows that a single
common-order generator or factored accumulated modulus is unnecessary on
the direct-factor branch: (N-1) exploits the complete hidden common
capacity automatically.

**Exact remaining gap.** Construct a public QP-bit integer word that reduces
one of the coprime quotients ((p-1)/d,(q-1)/d) to numerical QP on every
input. Randomness amplifies deterministic integer progress; it does not
create that progress.

### C215 — collision energy is the exact difference-word source

**Status:** promoted as P206 after F241 passed a fresh hostile audit and a
strict statement-only reconstruction.

The deterministic word \((N-1)^n\) leaves exactly the parts
\(s_p^\perp,s_q^\perp\) supported on primes outside \(N-1\). For iid
public integer samples, put \(\Delta=|Z-Z'|\) when the integers differ and
\(\Delta=1\) otherwise. If
\(s=\prod_{\ell\in\mathcal P}\ell^{e_\ell}<N\), then

\[
\mathbb E{\gcd(s,\Delta^n)\over s}
={1\over s}\left[1+
\sum_{\varnothing\ne S\subseteq\mathcal P}
\prod_{\ell\in S}(\ell^{e_\ell}-1)
\Pr\left(Z\ne Z',\ Z\equiv Z'
\pmod {\prod_{\ell\in S}\ell}\right)\right].
\]

P205 turns half the larger of the two expected reciprocal residuals into
factor probability. Uniform divisors of a factored \(N-1\) give a
constant-success QP word under a QP subgroup-image condition. The exact
prime-power formula shows that this collision energy can also be zero.

**Exact remaining gap.** Prove inverse-QP modular collisions between
distinct public integers, with enough primary weight in one exterior
residual, for every input. Support size and exact sampling do not suffice.

### C216 — the divisor lattice is support-saturated before it is factored

**Status:** promoted as P207 after F240 V2 passed a fresh hostile re-audit
and a strict statement-only reconstruction.

For every divisor \(B\mid N-1\), centered residues
\(x=up-aB,y=uq-bB\) satisfy

\[
c={xy-u^2\over B}\in\mathbb Z,
\qquad
aq+bp={u^2(N-1)/B+abB-c\over u}.
\]

The associated quadratic recovers a factor from a correct nondegenerate
tuple. At the guaranteed divisor \(B=d=\gcd(p-1,q-1)\), the carry is zero,
but the hidden centers are the P205 residuals themselves (plus one only in
the \(d=2\) tie case).

Inside the grammar generated by divisors of \(N-1\) using multiplication,
powers, gcd, lcm, and exact division, no word can absorb a residual prime
outside \(N-1\). The word \((N-1)^n\) already saturates every primary
inside that support. Complete factorization of the divisor lattice adds no
P205 power there.

**Exact remaining gap.** Use additive carry data to select a true signed
residue or construct new exterior prime support. Factoring a carry product
does not by itself select its hidden signed divisor.

### C217 — quadratic tori turn all four shifted residuals into exact Las Vegas interfaces

**Status:** promoted as P208 after F242 V2 passed a fresh hostile re-audit
and a strict statement-only reconstruction.

For a public unit discriminant \(D\), let

\[
\epsilon_i=\left({D\over i}\right),\qquad
J=\epsilon_p\epsilon_q,qquad
m_i=i-\epsilon_i.
\]

The public exponent \((N-J)W\) contains exactly the common shifted factor
\(d=\gcd(m_p,m_q)\). For the coprime shifted residuals

\[
s_i=m_i/d,qquad r_i=s_i/\gcd(s_i,W),
\]

a factor-free Hilbert--90 sampler produces independent uniform points on
the two full local norm-one tori. The local return probabilities are
exactly \(1/r_p,1/r_q\). Joint-coordinate Miller screens turn a simultaneous
return into a factor with probability at least one half. Hence one powered
trial succeeds with probability at least

\[
{1\over2\min(r_p,r_q)}.
\]

Uniform unit discriminants expose the four sign orientations equally. If
the same \(D\) is retained while nonclean coefficient pairs are resampled,
the complete factor-first trial has probability at least

\[
{1\over8\min_\epsilon R_\epsilon}.
\]

This extends P205 from \((p-1,q-1)\) to all four pairs made from
\(p\pm1,q\pm1\), at constant overhead. The word remains unfactored.

**Exact remaining gap.** Construct a public QP-bit word that leaves one
shifted residual QP-small on every input, or prove an inverse-QP expected
law for a randomized integer word. Four exact interfaces do not by
themselves make one interface small.

### C218 — one square exponent unifies the four interfaces, but signed powers can miss all of them

**Status:** promoted as P209 after F244 passed a fresh hostile audit and a
strict statement-only reconstruction.

For (A=p^2-1), (B=q^2-1), and (G=\gcd(A,B)), the four shifted common
capacities have lcm (G/2). The four residuals left by the square exponent
(N^2-1) are pairwise coprime and have product

\[
{AB\over2^\delta G^2},
\qquad
\delta=\mathbf 1_{v_2(A)\ne v_2(B)}.
\]

Choosing (W_J=N+J) in P208 makes every torus orientation use this one
public exponent. The resulting clean factor probability is exactly
controlled by the four reciprocal residuals, but the unconditional bound
is only of square-root scale.

An unconditional infinite family has shifted common-capacity table
((2,12,2,2)) and one exponentially large marker prime in each of
(p\pm1,q\pm1). Every numerical-QP-bit product of signed powers
(N^k\pm1) misses all four markers, even under adaptive selection. The
total common-order lcm is only (12), so accumulated order certificates
enlarge the beta-two dyadic modulus by at most a constant factor there.

**Exact remaining gap.** Find an all-input nonlinear integer source outside
the signed-power grammar. Difference, carry, quotient, and
discriminant-dependent words remain live.

### C219 — the square baseline isolates exterior support, and collision energy is the exact next gate

**Status:** promoted as P210 after F243 passed a fresh hostile audit and a
strict statement-only reconstruction.

The single word ((N^2-1)^n) strips every prime power that any shifted order
shares with either opposite sign. What remains in each P208 orientation is
exactly the exterior support absent from both opposite shifted orders.

If an exact public integer law has inverse-QP distinct-integer collision
probability modulo every prime in one exterior residual, QP many difference
words absorb that residual. Uniform orientation sampling and P208 then give
factor probability at least (1/16). Uniform divisors of a granted
factorization of (N^2-1) realize this under a QP subgroup-image condition.

The obvious factor-free replacements do not. Canonical torus coordinates,
raw discriminants, quadratic norm/trace collisions, and
(\gcd(X,N^2-1)) stay at (O(\operatorname{poly}(n)/\ell)) for a large
exterior prime. Pell trace collisions occur exactly when a public torus
element has small meta-order, which a deterministic word already detects.

**Exact remaining gap.** Find nonlinear cross-coordinate or carry aliasing
with inverse-QP mass on one exterior residual. Ordinary coordinate
randomness is not enough.

### C220 — random lift gauges are affine and generic; only the canonical section remains live

**Status:** promoted as P211 after F247 passed a fresh hostile audit and a
strict statement-only reconstruction.

For an ordinary lift (a_t=a+Ntpmod {N^2}), with (a) and the exponent
(E) units modulo (N), the high digit satisfies

\[
K_t=K_0+Ea^{E-1}t\pmod N.
\]

The exact norm-one torus fibre has the parallel form
(U_t=U(1+Ntw)), and its normalized carry is
(C_t=C_0+Etw). Thus a fresh uniform gauge parameter gives a uniform free
carry coordinate, even after the complete modulo-(N) transcript is fixed.
For a balanced semiprime, its direct-factor probability is only
((p+q-2)/N), and every exterior-prime atom or distinct collision has
probability at most (1/\ell).

Carries from one power chain are affine functions of the first carry, not
independent samples. An adaptive numerical-QP bank of fresh lift carries and
pair differences hits an exponential P209 marker only with probability
(2^{-\Omega(n)}).

**Exact remaining gap.** The canonical integer section is not random in its
lift fibre. Its high digit, nonlinear cross-base relations, exact squares,
determinants, and quotient carries remain possible integer-specific Las
Vegas sources.

### C221 — the fresh inverse-quotient and feedback-free torus grammar is now closed

**Status:** promoted as P212 after F245 V3 passed a fresh hostile audit and a
strict statement-only reconstruction. V1 and V2 remain preserved with their
failed statement-only reconstructions.

For a fresh exact uniform unit (u), the canonical inverse quotient

\[
K(u)={u\langle u^{-1}\rangle_N-1\over N}
\]

has fibres contained in the divisors of (Nk+1). Consequently, one residue
class modulo (ell) has mass (O(\Delta_N/\ell)), and the same
history-wise bound holds for pair differences. Adaptive later products do
not create new prime support.

On a self-contained infinite four-marker family, every numerical-QP-bit
signed-power word misses all four exponential markers and every accumulated
common-order lcm divides (12). After defining every permitted random draw,
gcd screen, torus endpoint, Miller-chain exit, and the chronology that fixes
the exponent before a fresh Hilbert--90 point, the complete cutoff bound is

\[
48\left(B+{B\choose2}\right){\Delta_N\over L}
+4B\left({1\over p}+{1\over q}\right)
+{2B\over L}.
\]

It is exponentially small for every numerical-QP cutoff (B). Therefore
no Las Vegas factorer confined to this grammar has expected numerical-QP
time on the family.

**Exact remaining gap.** The theorem does not touch the integer mechanisms
that matter most now: canonical lift digits, nonlinear quotient or norm
carries, biased sources, retained-point feedback, and complete square or
relation decoders. Those mechanisms must be analyzed directly rather than
treated as more fresh uniform atoms.

### C222 — rigid exact-square events are sparse; retrospective multirow parity remains live

**Status:** promoted as P213 after F248 V2 passed a fresh hostile re-audit
and a strict statement-only reconstruction. F248 V1 remains preserved with
its strict blind failure.

Uniform full scalar lifts are square with probability at most (K/N), where
(K=\gcd(E,p-1)\gcd(E,q-1)). A complete principal lift fibre contains
exactly four square outputs and exactly two mixed roots. More strongly, for
one past product fixed before a fresh principal coordinate, at most two of
the (N) coordinates close it to a useful exact square.

Canonical duplicates, reciprocal outputs, raw or powered torus singletons,
torus duplicates, and inverse-point pairs all have exact or
subexponential-over-exponential probability bounds in their displayed clean
source sizes. Thus numerical-QP banks of these rigid events are negligible
under the packet's explicit kernel and image-size hypotheses.

**Exact remaining gap.** P66 may select a product retrospectively from an
exponential family of past subsets. P213 does not control a general
nonduplicate multirow dependency, a mixed scalar--torus relation, or the
fixed canonical scalar section. Those are now the principal live
exact-square channels.

### C223 — fixed-past Pell closures have a uniform logarithmic count

**Status:** promoted as P214 after F251 passed a fresh hostile audit and a
strict statement-only reconstruction.

For (A_y=1+Dy^2), and for every positive integer (P) fixed before the
fresh coordinate (y), the number of coordinates below (Y) for which
(P A_y) is an exact square is at most

\[
1+\left\lfloor
{\log(1+2Y\sqrt D)\over\log(2+\sqrt2)}
\right\rfloor.
\]

The count is uniform in the size and squarefree kernel of (P). It gives a
history-wise fresh-row bound and a quadratic union bound for all pairs in an
independent torus bank. Thus one-row, duplicate, inverse-pair, fixed-past,
and now arbitrary independent pair closures are all sparse at an
exponential-size clean source.

**Exact remaining gap.** The complete P66 decoder may choose one of
exponentially many past subset products after it sees a row. The fixed-past
count does not union-bound that adaptive retrospective choice. A genuine
multirow square-class theorem or source remains necessary.

### C228 — signed Pell resultants isolate a one-sided Las Vegas ticket

**Status:** promoted as P219 after F257 passed a fresh hostile audit and a
strict statement-only reconstruction.

For two same-discriminant Pell rows, every odd shared prime power has one
public coordinate sign. The minus and plus parts divide the two explicit
resultant norms

\[
Q_\pm=D\Delta^2+(k_i\pm k_j)^2.
\]

If \((-D/N)=-1\) and the corresponding nonzero carry combination is less
than \(\sqrt{N/2}\), a gcd of \(Q_\pm\) with \(N\) is either one or the
unique hidden prime where \(-D\) splits. It can never be \(N\). This is an
exact Las Vegas ticket with no false factor output.

**Exact remaining gap.** No all-input or inverse-QP law forces a ticket in
a numerical-QP bank. The signed coordinate label also does not determine
whether a resultant-supported P66 dependency has a global or non-global
root. F258 is the preregistered large-scale search for the direct-ticket
frequency; F255 and F259 test broader unfactored-word and symbolic sources.

### C229 — the fixed Pell/resultant/carry word grammar is null on the safe-safe tail

**Status:** hostile-audited finite evidence from F255. This is not an
unbounded theorem or a factoring lower bound.

F255 tested ten public unfactored words built from eight Pell orbits:
specialized rows, same- and cross-discriminant resultants, hash-paired
resultants, the two signed norm factors, odd-multiple carries, and their
combined product. Each word was raised to the input bit length and scored by
the exact P205 residual fraction.

The preserved TSV contains 50,304 labelled balanced semiprimes and every
gcd pair. On every safe-safe input at factor sizes 32, 40, 48, 56, and 60,
all nine nonbaseline candidates are exactly equal to the \(N-1\) baseline,
row by row. There are no improvements and no saturated residuals. The worst
combined \(-\log_2 H\) grows linearly across those sizes. Random inputs show
many improvements, but their worst tail also grows linearly, so they do not
meet the frozen useful-lead criterion.

The hostile audit independently verified all 50,304 rows, all 200 JSON
summaries, the reaggregated global totals, and 400 reconstructed gcds. The
scope qualifications are explicit: the two 12-bit cohorts overlap on 22
moduli; the JSON omitted global per-word aggregates; self-test stdout, peak
RSS, the Boost-install transcript, and launch ownership are unavailable.
None affects the safe-safe 32--60 rowwise null.

**Search consequence.** Do not enlarge this grammar only by multiplying
more of the same support factors. A materially new search must use a new
integer coordinate, such as the full Pell lift quotients, nonlinear
principal digits, adaptive feedback, or a direct signed ticket, and must
retain a hostile safe-safe tail.

### C227 — fixed-past fibre bounds do not control the retrospective span; clean Pell multiples are decoys

**Status:** promoted as P218 after F253 V2 passed a fresh hostile re-audit
and a strict statement-only reconstruction. V1 remains preserved with its
blind failure on the missing distinct-row condition.

P214 bounds each rational square-class fibre in a finite Pell bank. It
therefore gives a logarithmic lower bound on the bank rank and exact upper
bounds on fixed-size and uniform-subset square probabilities. An abstract
bank with repeated copies of all nonzero binary vectors attains the rank
loss. No ordering, greedy pivot, or circuit pivot turns this information
alone into an inverse-QP retrospective bound.

The first systematic same-orbit dependencies are exact decoys. Every clean
odd-multiple pair of distinct retained rows has the same exact square class,
but its positive integer root matches the supplied root modulo (N). The
whole span of these pair vectors has normalized root (+1). A frozen
(N=4331) example at indices (17,51) certifies the phenomenon.

**Exact remaining gap.** Canonical-wrap carries break the polynomial
identity by an explicit multiple of (N). Carried and other
resultant-supported arithmetic specializations are the live Pell/P66 core.

**Finite follow-up.** F256 tested the exact carried two-row criterion on
2,311,478 retained pairs from disjoint train and held-out cohorts. Although
923,599 pairs shared a nontrivial gcd, neither required gcd quotient was ever
a square, so the scan found zero two-row dependencies and zero non-global
roots. The hostile audit authenticated this finite null with a protocol
qualification: some preregistered cleanup/resource aggregates were omitted.
No asymptotic conclusion follows.

### C226 — generic Pell dependencies vanish after cleanup; only the resultant core remains

**Status:** promoted as P217 after F252 passed a fresh hostile audit and a
strict statement-only reconstruction.

Every post-wrap Pell row is an irreducible quadratic over (mathbf Q).
Two such polynomials share a generic factor exactly when their closed
pairwise resultant vanishes, and that occurs exactly when the integer
polynomials are equal. Therefore constant-square and duplicate cleanup makes
the generic square-class kernel zero. All pre-cleanup generic relations have
integral roots and global normalized signs.

At the numerical specialization, powering the product of pairwise
resultants and taking one gcd with each row separates a private cofactor.
A nonsquare private cofactor is a parity pivot; a square private cofactor is
discardable. The entire surviving P66 problem is supported on the explicit
resultants in factor-free polynomial time.

**Exact remaining gap.** Specialization can still create relations wholly
inside this resultant-supported core. P217 gives no all-input private-pivot
law, inverse-QP event bound, or non-global-root theorem for that core.

### C225 — the tailored negative-Pell component source is not universal

**Status:** promoted as P216 after F254 passed a fresh hostile audit and a
strict statement-only reconstruction.

Every tailored negative-Pell row splits publicly into two affine components,
each twice a square modulo (N). This enlarges the original-row P66 bank:
every even component subset has a known modular root. Shared specialized
prime support is localized by explicit pairwise affine resultants.

The complete source can nevertheless have zero kernel. For
(N=143=11\cdot13), the only admissible nontrivial negative-Pell
coordinates below (N) are (5) and (29). Their four component columns
have private parity pivots (733,83,17,47), so the component matrix has
full rank four. All direct gcd screens are inert.

**Exact remaining gap.** This is one exact counterexample, not a density
bound. Randomized discriminants and the general retrospective multirow P66
source remain live. The audited F252 and F253 candidates further localize
generic Pell relations and clean odd-multiple decoys, but they await strict
statement-only reconstruction before promotion.

### C224 — the shifted binomial threshold is the complementary central-coefficient gate

**Status:** promoted as P215 after F249 passed a fresh hostile audit and a
strict statement-only reconstruction.

For (B=\lfloor\sqrt N\rfloor), (H=\lfloor B/2\rfloor), and
(s=B-p), the complete shifted family satisfies

\[
\binom{rN+c-1}{B}
\equiv rq\binom{c-1}{s}\pmod N.
\]

The coefficient gcd is (N) for (c\le s) and (q) for (c>s).
Since (s<H), the single public endpoint (c=H) always factors if its
residue modulo (N) is available. The adjacent recurrence has one hidden
nonunit denominator at (c=s).

This is not a new source. The ordinary central coefficient satisfies

\[
\gcd\!\left(N,\binom BH\right)=p,
\]

so the shifted endpoint only returns the complementary prime. The literal
recurrence, factorial, interval product, Vandermonde, and standard
holonomic routes all return to the same exponential product gate.

**Exact remaining gap.** Evaluate one remote central or shifted binomial
coefficient modulo the unfactored composite modulus in numerical-QP time by
a representation that does not first form the factor-bearing interval.

### C230 — every F263 shifted symbolic lead is a public query-boundary decoy

**Status:** promoted as P220 after F267 passed a fresh hostile audit and a
strict statement-only reconstruction. F263 is hostile-audited finite
evidence; F267 is the proof-only explanation.

The frozen F263 C++ search tested 148 hypergeometric block summaries on
2,000 discovery and held-out rows. Its held-out nonconsecutive cohorts had
zero nondirect hits. The complete nondirect union contained 67
consecutive-prime rows and 136 incidences from only six shifted candidates.

F267 gives closed integer formulas for those six candidates. At the public
left and right query edges, rising-factorial reflection forces their zeros
only at the displayed offsets

\[
s=B-p\in\{L-1,L,L+1,L+2\}.
\]

The boundary condition itself makes \(p=B-s\) directly testable. Under the
sufficient condition \(s^2<p\), the floor-square inequalities further force

\[
q-p=2(s+1),\qquad B+1={p+q\over2},
\]

so the first Fermat trial factors \(N\). This explains every authenticated
F263 nondirect incidence without creating a new source.

**Exact remaining gap.** The theorem does not classify every zero of the six
polynomials and does not bound other symbolic grammars. A materially new
remote-coefficient search must avoid public block-edge reflection, enforce
nonconsecutive held-out leads, and show a QP construction cost rather than
only a factor-bearing value.

### C231 — separate canonical scalar-section banks have row-private parity pivots

**Status:** hostile-audited finite evidence from F268-D04. This is not an
all-input rank theorem or a factoring lower bound.

F268 placed the canonical integers

\[
U_E(a)=[a^E]_{N^2},
\qquad
E\in\{N-1,N+1,N^2-1,2(N-1),2(N+1)\},
\]

into complete factor-free P66 decoders. Twelve frozen source families covered
independent bases, complements, products, power chains, inverses, affine
tuples, mixed exponents, and two-seed orbits. Direct carry and gcd channels,
singletons, and every support-two square-class relation were screened first.

Every eligible bank had full column rank. The discovery stage had zero useful
low or residual relation across 2,256 banks. The held-out stage had zero factor
at every direct stage and zero relation across 1,184 banks. The strict finite
lead was null.

The independent result audit found a stronger finite explanation. Every row
had at least one nonsquare opaque block whose parity support contained only
that row: all 53,392 discovery rows, all 55,944 held-out rows, and all 2,292
preflight rows were privately pivoted. Minimum and maximum per-bank coverage
were both 100 percent. No tested row needed a non-private block combination to
prove independence.

**Search consequence.** Do not enlarge one scalar-section family in isolation.
The only immediate P66 escape suggested by this experiment is to unite
different families on the same modulus and recompute the entire gcd-free block
system. A block private inside one bank can become shared after the union.
Discovery ROW records permit an exact post-hoc all-twelve-family union, but
that would be hypothesis generation only. Any evidentiary held-out test needs a
new frozen C++ packet and disjoint cohorts. It must perform saturated
private-primary peeling before the complete residual decoder.

### C232 — explicit divisor covers cannot reach quasipolynomial scale by increasing rank

**Status:** promoted as P221 after corrected F272 V2 passed a fresh hostile
audit and strict statement-only reconstruction. No computation ran.

Let \(D\) be the set of nonzero absolute differences from finite integer
sets \(S,T\). If every \(m\le X\) divides one \(d\in D\), and every
difference has at most \(L\) bits, then

\[
\vartheta_2(X)
\le\sum_{d\in D}\log_2d
<|D|L
\le|S||T|L.
\]

The proof only assigns each prime \(p\le X\) to a difference divisible by
it and charges the product of distinct assigned primes to that difference.
It is independent of arithmetic-progression or generalized-progression rank,
and duplicate pairs, signs, and multisets do not help. Complete explicit
factor output has the same aggregate lower bound even when each huge
difference has a short circuit description.

For the scaling \(|S|,|T|\le X^{\beta+o(1)}\) and
\(\log\max(S\cup T)\le X^{\alpha+o(1)}\), necessary conditions are

\[
\alpha+2\beta\ge1,
\qquad
\alpha+\beta\ge\tfrac12.
\]

Only the first is saturated at the one-third point. A successful higher-rank
one-third cover would still give \(N^{1/6+o(1)}\), not quasipolynomial
factoring. Therefore a large symbolic search over explicit rank-two through
rank-six covers is not justified for this goal.

**Search consequence.** The obstruction does not cover succinct modular
evaluation. A uniform QP evaluator for an interval product

\[
\prod_{j=a}^{b}j\pmod d
\]

would factor by one-path binary gcd splitting, so it is a precise
factoring-hard target. Future work should look for a genuinely compressed
evaluator or a different adaptive product hierarchy, not another explicit
cover or prefactored separator. P221 neither constructs this evaluator nor
claims it is the unique possible escape.

### C233 — batch gcd-free refinement removes the quadratic P66 decoder bottleneck

**Status:** promoted as P222 after corrected F271 V2 passed a fresh hostile
audit and strict reconstruction from its authenticated base and V2
statements. This is a decoder theorem, not a source or factoring theorem.

For positive rows with canonical unit modular roots, F271 constructs a
pairwise-coprime opaque block basis without rational-prime factorization.
Saturation isolates complete primary support. Equal-support refinement is a
subtractive Euclidean recursion, and a balanced product tree inserts all
rows while preserving exact exponent vectors.

If \(T\) old blocks are touched, \(E\) recursion nodes occur, \(S\) blocks
remain, and the tree has depth \(D\), refinement plus terminal coprimality
verification needs at most

\[
(D+1)T+m+2E+S
\]

scalar gcd calls. One product/remainder tree verifies all final block pairs
with exactly \(S\) gcds. The corrected V2 empty-tree rule makes every
operation count zero when \(S=0\), and canonical supplied roots keep their
encoding inside the polynomial bit bound.

The parity decoder also avoids row-pair arithmetic. Singleton relations are
the zero matrix columns; support-two relations are pairs of equal columns.
Signature classes give a basis of their entire span. A canonical kernel
complement and the normalized-root homomorphism then make at most \(m\)
basis classifications complete.

For an F265 residual bank with at most 64 rows of at most 361 bits, the exact
cap is 91,111 refinement/terminal gcd calls per bank and 69,973,248 across
768 maximum banks. This is about 103.02 times below the abandoned D08 call
envelope. Operand widths still require a real target benchmark.

**Search consequence.** An elliptic cubic-lift retry may now be resource
credible, but only after a new source packet imports P222 exactly, removes
the obsolete all-pair decoder, caps actual batch work, and passes a
cap-complete target preflight. P222 does not predict that any residual core
or non-global relation exists.

### C234 — fixed child-state and literal resultant grammars do not compress the interval gate

**Status:** promoted as P223 after corrected F273 V2 passed a fresh hostile
audit and strict statement-only reconstruction. No computation ran.

Four exact boundaries now separate useful symbolic exploration from literal
repackaging of the remote interval product.

1. In a polynomial ring with algebraically independent child coordinates,
   a scalar that vanishes on one child-product axis contains that child
   product. Vanishing on both axes forces the parent product
   \(e_0o_0\). This is not a circuit lower bound after affine or
   characteristic-specific specialization.
2. With one local rank defect, all proper Smith determinantal divisors are
   units modulo \(N\); only the terminal invariant is guaranteed to carry
   the factor. For \(\operatorname{diag}(1,\ldots,B)\), the determinant is
   \(B!\), while the last Smith invariant is
   \(\operatorname{lcm}(1,\ldots,B)\). Both are factor-bearing gates, but
   they are different evaluation problems.
3. The full derivative resultant of a rising factorial is the square of a
   superfactorial. Its gcd with \(N\) is the hidden prime on the unresolved
   balanced branch, but its bit length is \(\Theta(B^2\log B)\).
4. Literal dyadic cross-resultant recursion from length \(2^tq_0\) has
   \(2^{t+1}-1\) base offsets and \(2^{t+2}-t-3\) keyed states. Telescoping
   replaces them by the same factor-bearing weighted product rather than a
   modular evaluator.

**Search consequence.** Do not launch a larger C++ search over fixed-order
jets, literal Smith summaries, full discriminants, or this named resultant
recursion. A new interval-product experiment first needs a finite transition
with independently quasipolynomially evaluable coefficients outside the
P223 hypotheses. Affine-specific identities, nonlinear carries, adaptive
algorithms, and the general succinct evaluator remain open.

### C235 — the regular characteristic-shift separator cannot survive an explicit QP-dimensional shift quotient

**Status:** promoted as P224 after F274 passed a fresh hostile audit and a
strict statement-only reconstruction. No computation ran.

On the full function space over \(\mathbb F_r\), cyclic translation has
\((T-I)\)-nilpotency index exactly \(r\). Thus the balanced threshold
\(p\le B<q\) gives \(\Delta_p^B=0\) but \(\Delta_q^B\ne0\). Every
\(d\)-dimensional shift-stable subquotient instead has nilpotency index at
most \(d\). When \(d\le B\), both local \(B\)-th differences vanish, so an
explicit numerical-QP-dimensional regular-shift state loses this particular
signal.

Ordinary \(B\)-th differences of integer polynomials are all divisible by
\(B!\), sharply so for \(X^B\). This repackages the factorial gate rather
than normalizing it. Rational scalar shift gauges exist exactly when their
irreducible valuations balance on every translation orbit and their value at
infinity is one; when they exist, the product is an endpoint telescope. A
rational matrix gauge inherits the same necessary determinant condition.

**Search consequence.** Do not search the exact regular-shift nilpotency,
integer-polynomial-difference, or rational-gauge grammars further. This is
only a named-model decision. Other invariants of a small state, nonlinear or
semilinear states, implicit representations, determinant-one cocycles,
integer-valued-polynomial mechanisms, and adaptive algorithms remain open.
Any future run must first state its asymmetric local law and independently
QP-evaluable transition outside P224.

### C236 — inherited monomial sharing cannot manufacture a new P66 root image

**Status:** promoted as P225 after corrected F275 V2 passed a fresh hostile
audit and strict reconstruction from its two authenticated statements. No
computation ran.

For exact monomial rows with multiplicatively inherited supplied roots, every
new exact square relation pulls back through the parity-incidence matrix to
an old relation, and its normalized root is the old normalized root up to a
global sign. Structural incidence cycles therefore have only global roots;
useful old arithmetic relations can be retained but not manufactured.

For an inverse-square graph source, an even cycle's normalized root is the
ratio of the alternating products of its public edge labels. Its two P66 gcds
are exactly the two alternating-label gcds, so a useful cycle factors before
the parity decoder. V2 repairs the sole V1 defect by requiring the explicit
carrier in the sub-\(N^2\) construction to satisfy \(1\le d<N\).

**Search consequence.** Do not build a large graph or product-circuit search
whose only pivot-sharing mechanism is exact inherited multiplication. The
F270 all-family union remains justified because it recomputes numerical
cross-family block sharing. Canonically reduced complement products also lie
outside P225, but reduction removes the promised support-sharing mechanism;
they need a separate positive event law before a production search.

### C237 — determinant one removes scalar product gates only by moving them into denominators, large states, constant powers, or an affine continuant

**Status:** promoted as P226 after corrected F276 V2 passed fresh hostile and
strict statement-only audits. No computation ran.

A rational two-endpoint matrix law is exactly a gauge telescope. A separable
finite-dimensional length state is a rational gauge times a constant matrix
power. Polynomial unimodular direct-summand lines carry only unit
multipliers, and integer unimodular transport preserves the coordinate ideal
of a whole state.

Every affine \(\operatorname{SL}_2\) step is a constant matrix times one
nilpotent shear. After rational conjugacy its generic scalar coordinate is the
continuant

\[
y_{k+2}=(ck+a+c+d)y_{k+1}-y_k.
\]

The \(c=0\) branch reduces to constant powering and weighted sums; it is not
proved signal-free. The \(c\ne0\) branch has neither a proved remote endpoint
evaluator nor a proved hidden-prime signal.

**Search consequence.** A coefficient scan of the generic affine recurrence
would measure sequential finite coincidences without testing the missing QP
endpoint operation, so it is not yet resource-justified. A new determinant-one
experiment must first supply either a separately audited constant-power signal
or a genuine fast endpoint law for the continuant, and must pass denominator,
state-size, and asymmetric-signal gates.

### C238 — integer-valued high differences expose exact Stirling signals but not their remote evaluator

**Status:** promoted as P227 after F277 passed fresh hostile and strict
statement-only audits. No production computation ran.

The Newton-binomial basis makes a high difference an exact coefficient shift.
For the F249 shifted-binomial family, every difference order is now
classified: the hidden spike moves from order zero to order \(s=B-p\), and
the first order beyond \(s\) already has the same residue in both CRT
components. A binomial with a QP-short complementary side has a unit
denominator, so every Kummer carry is already a displayed numerator gcd;
that screen can still saturate.

The normalized monomial differences give the exact new laws

\[
 \left\{\begin{matrix}2B\\B\end{matrix}\right\}
 \equiv2\left\{\begin{matrix}2s+1\\s\end{matrix}\right\}\pmod p,
 \qquad
 \left\{\begin{matrix}2B+1\\B\end{matrix}\right\}
 \equiv2\left\{\begin{matrix}2s+2\\s\end{matrix}\right\}\pmod p,
\]

while both vanish modulo \(q\). Each scalar can saturate. Joint saturation
is the explicit adjacent central-Stirling divisibility condition left open by
P227.

**Search consequence.** Do not spend a large C++ run on more finite
differences of these same binomial or monomial families. The missing objects
are a numerical-QP modular evaluator for the remote central-Stirling
coefficient and an all-input dispatcher, not another hit-rate table. Other
integer-valued circuits and succinct remote-coefficient algorithms remain
open because P227 proves no general evaluator lower bound.

### C239 — explicit constant powers make the endpoint cheap but leave power-coset cancellation open

**Status:** promoted as P228 after F278 passed fresh hostile and strict
statement-only audits. No computation ran.

An explicit numerical-QP-dimensional matrix (C_N\) can be powered to
(B=\lfloor\sqrt N\rfloor\) in numerical quasipolynomial time. A literal
Jordan block adds no hidden compression: its (j)-th coefficient factors
exactly when the direct interval (B-j+1,\ldots,B\) contains the smaller
prime. Clean spectral collisions are exactly eigenvalue-ratio (B)-torsion,
and a clean quadratic companion coordinate is exactly an ordinary-group or
norm-one-torus residual with smaller-prime exponent (s+1\) or (s-1\).
Constant-in-index recurrences are the same public state-space endpoint.

**Search consequence.** Do not search Jordan coefficients, powered spectral
collisions, or the companion (U_B\) coordinate again. A targeted matrix
search is justified only in the unresolved additive lane, beginning already
with two modes:

\[
 a\alpha^B+b\beta^B=0
 \iff (\alpha/\beta)^B=-b/a.
\]

Before any large run, the grammar must remove public input gcds, near-square
windows, eigenvalue collisions, ordinary/torus order tickets, and directly
visible power-coset targets. A surviving experiment may discover a candidate
law, but finite hits cannot prove an all-input signal. Higher-mode sums,
semilinear actions, and arbitrary (N\)-dependent coefficient constructions
also remain outside P228.

### C240 — bounded global order can be upgraded to all-local order, but no useful word follows

**Status:** promoted as P229 after F280 V2 passed an independent
primary-source hostile audit and a strict statement-only reconstruction. No
numerical search ran.

Given a unit \(a\bmod N\) with global order greater than \(D\), the explicit
scan

\[
 \gcd(a^e-1,N),\qquad 1\le e\le D,
\]

either factors \(N\) or certifies order greater than \(D\) at every rational
prime divisor of \(N\). A saturated gcd cannot occur because it contradicts
the source order. With Nir Proposition 1.2, this gives a bounded ordinary
representative \(2\le a\le D^2+D\); with Harvey--Hittmeir, it gives the
faster global source plus an explicit linear local scan. Numerical-QP \(D\)
therefore stays numerical-QP.

This closes the global-to-local source gap, not the factoring-transfer gap.
A bare high global order can hide a small local order, and synchronized
screened orders divide every \(p-1\), so their lcm contributes no new
prime-power capacity beyond the registered \((N-1)^n\) baseline. The source
does not produce a rough residual, P205 word, carry, quotient, determinant,
or asymmetric CRT signal.

**Search consequence.** Do not spend a large run on finding merely larger
ordinary orders. A justified successor must state the exact transfer from an
all-local-order element to a new factor-bearing integer word before it asks
for numerical evidence.

### C241 — a random shift solves normalized central saturation, leaving only the remote evaluator

**Status:** promoted as P230 after F282 passed a fresh hostile proof audit and
a strict statement-only reconstruction. The theorem is conditional; no
evaluator or factoring run exists.

For a balanced distinct odd semiprime, put \(B=\lfloor\sqrt N\rfloor\) and

\[
 F_B(a)=\frac{\Delta^B X^{2B}|_{X=a}}{B!}
       =h_B(a,a+1,\ldots,a+B).
\]

After the direct \(\gcd(B,N)\) screen, write \(B=p+s\) and \(q=B+h\).
Then \(h\ge s+2\) and \(p\ge2s+3\). The normalized scalar is zero modulo
\(q\) for every shift, while modulo \(p\) it is the nonzero degree-\(s+1\)
polynomial

\[
 2h_{s+1}(a,a+1,\ldots,a+s).
\]

A uniform public shift therefore gives \(q\) by one gcd with probability
strictly greater than one half. This replaces F281's proposed deterministic
two-scalar saturation test by an exact constant-success dispatcher.

**Search consequence.** Do not run the F281 saturation cohort. A useful next
experiment must target the exact normalized evaluator. It must exhibit a
QP-depth endpoint or divide-and-conquer law for \(F_B(a)\bmod N\), preserve
the exact integer division, and reject any representation that merely
computes the raw difference: the raw difference is identically zero modulo
\(N\). Sequential Stirling tables, \(B+1\)-term sums, characteristic-size
coefficient vectors, factorial inversion, and exact exponential-size
materialization are controls, not candidates. Finite identity synthesis can
guide this search, but only an exact uniform fast-forward with unit-safe
operations can close the theorem.

### C242 — the natural normalized-difference evaluator grammars collapse to width or factor gates

**Status:** promoted as P231 after F283 passed a fresh hostile proof audit and
a strict statement-only reconstruction. No computation ran.

The P230 scalar is a generalized-Stirling endpoint. Its canonical linear
coefficient sequence has exactly \(B+1\) uncancelled modes, including after
fixed-radix decimation. Translation and interval/parity composition retain a
full central convolution. A monotone normalized divided-power chain meets a
binomial coefficient whose gcd with \(N\) is \(p\); the unnormalized chain
ends at zero modulo \(N\).

The guaranteed \(q\)-zero is also the universal content contributed by
primes in \((B+1,2B)\). Explicit content, interval-primorial, or leading
coefficient evaluation factors directly. Removing the content removes the
guaranteed zero. Dividing the raw value by \(N\) after an \(N^2\) lift leaves
a product with no promised factor.

**Search consequence.** Do not synthesize another full Stirling vector,
literal block convolution, monotone divided-power chain, canonical linear
matrix, explicit content product, or immediate \(N^2\) quotient. Before any
new run, exhibit a different numerical-QP transition for an arbitrary public
shift. It must avoid nonunit normalization or return its gcd, and its endpoint
must retain the P230 asymmetry. Tailored nonlinear, adaptive, branching,
higher-lift, and other noncanonical evaluators remain open; P231 does not
give a general evaluator or circuit lower bound.

### C243 -- Short q-binomial jets are computable, but their useful scalar is missing

**Status:** research synthesis; the precise jet and uniform-index statements are P234.

**Scope:** normalized Taylor coefficients, selected moment determinants, and the
specific finite examples in F284. No general factoring or novelty claim.

**Discussion.**

F284 computes 13 exact coefficients for B=2^512+12345 in about two local Sage
seconds without constructing an enormous Gaussian polynomial. This is a real
compressed evaluator outside F14's full coefficient-state model. Its normalization
removes the central-binomial factor that previously guaranteed a q-zero.
Sage also exposed explicit polynomial factors in moment determinants. For
N=247,B=15, H_3 finds 13 through 5B+3; this is a small linear relation in B,
not a new generic source law. Uniform coefficient gcd probes obey P234's
sparse-root bound, which does not cover deterministic B or other decoders.

Next question: preserve a factor-asymmetric scalar or find a different decoder
with a proved useful law while retaining the compact representation. Compare
the exact cumulant formula with the Billey--Swanson paper before making any
novelty claim. An August 2026 mod-phi paper is a recorded reading lead only.
Evidence: `experiments/F284_cyclotomic_binomial_search/RESULT.md`, its
`RECONSTRUCTION.md`, `output/D05.json`, and `output/S01.txt`.

### C244 -- Public matrix-power derivative rank measures power collisions

**Status:** P232 is independently reconstructed; the separate two-dimensional
sampling probabilities remain author-derived candidates with exact finite checks.

**Scope:** the squarefree branch and individual operator ranks, not joint decoders.

**Discussion.**

F285 starts with a genuinely public, logarithmic-exponent circuit for D(A^N).
P232 identifies its kernel as Cent(A^N). Outside at most D(D+1) exceptional
balanced prime partners, every such operator of dimension<=D has synchronized
ranks, simultaneously even under adaptive matrix choices. Thus sampling more
individual ranks cannot change this particular obstruction. The information
needed by a different decoder could lie in coordinates, combined operators,
or a different function; P232 does not exclude these.

Next question: identify a joint observable that contains information beyond
the individual power-collision ranks, before generating another matrix menu.
Evidence: `experiments/F285_finite_algebra_operator_search/DIMENSION_EXTENSION.md`,
`RECONSTRUCTION.md`, and `general_dimension_results.json` (112 exact cases).

### C245 -- Constraint propagation gains pruning but can hide a numerical scan

**Status:** the global-cut survival theorem is P233. Iterated fixed-point,
iteration-cost, and fast-forward analyses remain author-derived candidates.

**Scope:** the explicitly retained real arcs and linear-form congruence cuts in F286.

**Discussion.**

Global tangent cuts leave all early branches by P233. Recomputing minima on
retained arcs does produce additional pruning: one finite case reached two
states in eight sweeps, while a larger case retained all sixteen after 24.
The exact fixed-point construction is promising as a correctness mechanism,
but its iteration cost still needs a numerical-scale analysis.

The ordered forms (1,1),(1,2) reveal the issue precisely: their rounded
composition advances the sum threshold by exactly M until a factor point.
A safe coordinate-block jump exists, but one regime becomes residue-strided
trial division. These observations redirect the search toward joint interval
certificates rather than simply increasing the number of sweeps.
Evidence: `experiments/F286_diophantine_constraint_search/RESULT.md`,
`RECONSTRUCTION.md`, `ITERATED_RESULT.md`, `ITERATED_output.json`, and `FAST_FORWARD.md`.

### C246 -- Joint derivative products expose a scalar collision without a success law

**Status:** candidate synthesis. The F287 identities and counts are author-derived;
independent statement-only reconstruction is pending.

**Scope:** the fixed three-by-three matrix families, witnesses at \(N=77,187\),
and exact root counts for the 16 listed prime pairs in F287. No general
joint-operator or all-input claim.

**Discussion.**

P232 leaves combined operators open. F287 derives a deficient triple product
whose derivative rank depends on a weighted pairing that individual and adjacent
ranks do not determine. For its fixed public family, the rank-drop condition is
the scalar

\[
F_N(t)=t^{2N-1}+3t^N-3t^{N-1}-1.
\]

The public gcd test evaluates this scalar with polynomial bit cost per sample.
Exact witnesses at \(N=77\) and \(N=187\) split the input while the individual
and adjacent ranks agree. The follow-up gives reciprocal identities, exact local
root counts on a fixed list of 16 prime pairs, and special coefficient families.
Many pairs have no roots, and the positive twin-prime cases have density of order
\(1/p\). No uniform inverse-quasipolynomial success bound or covering list is
known. The isolated coefficient-three family also has a stated Carmichael
limitation. These claims still require independent proof reconstruction.

Evidence: `experiments/F287_joint_power_operators/REPORT.md`,
`experiments/F287_joint_power_operators/SUCCESS_LAW.md`,
`experiments/F287_joint_power_operators/pilot.json`, and
`experiments/F287_joint_power_operators/counts.json`.

### C247 -- Hyperbola support geometry overlaps known work and self-normal descent stalls

**Status:** candidate proof and literature synthesis with exact finite evidence.
Independent reconstruction and verification of the derived support reduction are pending.

**Scope:** the positive hyperbola over one lattice translate, six exact boxed
examples, and the full-text comparison in F288. No all-input success law.

**Discussion.**

F288 gives a self-contained reflection argument that every unboxed hull vertex
is the unique minimizer of its own normal, and an elementary exposure interval
for an exact factor point in one residue coset. Its six boxed examples contain
strict nonfactor fixed points; self-normal descent did not increase factor-fan
mass. These are finite observations, not a basin theorem.

The literature comparison limits novelty. Alcantara--Blanco--Criado--Santos
already give the integer-hyperbola hull, identify factor points as vertices, and
give efficient access to individual vertices. Balog--Barany use the same central
reflection body. The self-normal statement was not found verbatim, but it is an
elementary consequence of that argument, not a substantially new geometric
principle. The factor exposure interval is new to this repository; external
novelty is unestablished.

The cited SEEK and NEXT interfaces support a candidate polynomial-cost unboxed
support reduction after full bit accounting. That reduction still needs
verification. Box truncation, residue-coset unions, and a useful probability law
need separate arguments; the F288 pilot uses enumeration linear in the numerical
box width.

Evidence: `experiments/F288_integer_hyperbola_support/RESULT.md`,
`experiments/F288_integer_hyperbola_support/LITERATURE.md`,
`experiments/F288_integer_hyperbola_support/RECONSTRUCTION_STATEMENT.md`, and
`experiments/F288_integer_hyperbola_support/output.json`.

### C248 -- Modular support unions permit finite descent without a general oracle law

**Status:** exact finite observation from F289. Independent verification is pending.

**Scope:** 35 labelled cases with
\(B\in\{2^8,2^{10},2^{12},2^{14},2^{16}\}\),
\(M\in\{1,2,4,8,16,64,256\}\), and the three displayed certificates at
\(N=147053\). No asymptotic descent or factoring claim.

**Discussion.**

The product-congruence set is a union of residue cosets, so reflection can leave
the set even when positivity and the product bound survive. F289 records exact
move certificates for \(M=16,64,256\). All vertices were self-fixed in the 20
cases with \(M\leq8\). Every one of the 15 cases with \(M\geq16\) had a move,
but only seven increased the measured proper-factor basin and no path used more
than three moves. Movement therefore does not establish a uniform success law.

The exact pilot enumerates points up to a numerical cutoff and costs linear work
in that cutoff. It supplies no quasipolynomial-bit support oracle for the modular
union. Both the finite implementation and any generalization remain independently
unchecked.

Evidence: `experiments/F289_modular_support_union/RESULT.md`,
`experiments/F289_modular_support_union/output.json`,
`experiments/F289_modular_support_union/run.log`, and
`experiments/F289_modular_support_union/RESOURCE_ESTIMATE.md`.

### C249 -- Compressed rational degree resolves into collision gates without a uniform basin law

**Status:** author-derived identities and exact finite observations. These
dynamics are not independently reconstructed or promoted.

**Scope:** the fixed \(R_h\) families, listed finite fields, two iterated
equalities, pole events, and the three-base batch in F287. No arbitrary-map
or all-input density claim.

**Discussion.**

F287 found local root counts \(0,2,\ldots,10\) across 24,790 finite-field
instances, refuting the earlier finite count-four pattern. For \(h=2\), the
map \(R_h(v)=v(h-v)/(hv-1)\) is Möbius-conjugate to inverse squaring, but the
public \(N\)-th power remains in the original coordinate. Its large iterated
collision sets are exactly controlled by the 2-primary part of a split or
norm-one torus and are not uniform across prime factors.

For arbitrary \(h\), the exact identity

\[
 R_h(x)-R_h(y)
 =\frac{(x-y)(x+y-hxy-h)}{(hx-1)(hy-1)}
\]

shows that an iterated equality is a union of same-time collision gates,
rather than \(2^j\) independent tests. The \(h=3\) pilots exhibited some
collision and pole-tree growth, but a quadratic-character obstruction can
also stop the pole tree immediately. The three-base \(h=2\) orbit gives an
exact finite batching gain from two modular powers, not a density theorem.

The missing result is a public non-group family with a provably large
asymmetric collision or pole basin after quasipolynomially many cheap steps.
Evidence:
experiments/F287_joint_power_operators/DYNAMICS_FOLLOWUP.md,
ITERATION_REPORT.md, extended_counts.json, and iteration_counts.json.

### C250 -- Modular hyperbola support has exact finite shortcuts but retains a numerical-power class count

**Status:** synthesis of P235 with author-derived algorithms and exact finite
audits. Only P235's cover, higher differences, and conditional reduction are
promoted.

**Scope:** the F288 one-patch and cap-line prototypes, F289 hierarchy and
scaling runs, and their stated finite input families. No QP node bound.

**Discussion.**

The one-patch F288 support adapter passed bounded exhaustive checks, and the
F289 affine hierarchy matched 455 full-enumeration support queries. At
\(M=\Theta(N)\), the retained final scaling run completed 16 of 24 queries;
8 exhausted their soft time budgets. One incomplete query had already
returned a verified factor point, which separates early factor detection from
exact support termination. An earlier 15/9 run summary survives, but its full
JSON was overwritten and was not reconstructed.

The grouped cap-line operation replaces many patch optimizations by exact
quadratic line equations. Its seeded random and high-residue audit completed
30 queries through 57--58 input bits. An explicit last-subtree family forced
first discovery to the final visited node, correcting the original low-bit
input bias. Complete trees still used about 45,000 nodes and 90,000 line
equations at the largest scale. The candidate analysis gives an
\(O(N^{1/3}\operatorname{polylog}N)\) upper mechanism for a fixed line cap,
not quasipolynomial cost in \(\log N\).

The actual gap is to group or eliminate enough coarse residue classes to
obtain a succinct 1.01-feasible support procedure with uniform QP bit cost.
First-factor timings and one-patch polynomial cost do not resolve that gap.
Evidence: experiments/F288_integer_hyperbola_support/PATCH_SUPPORT.md and
CAP_LINES.md; experiments/F289_modular_support_union/BRANCH_SUPPORT_RESULT.md,
SCALING_RESULT.md, and scaling_output.json.

### C251 -- Dyadic objective histograms compress, while joint placement remains a signed carry

**Status:** author-derived identities and exact finite certificates.
Independent reconstruction is pending.

**Scope:** complete dyadic objective histograms, fixed-degree prefix weights,
the four-child carry, stated counterexamples, and the public normal menus in
F290. No localized support algorithm.

**Discussion.**

F290 gives an \(O(k)\)-residue-class signed description of the complete
histogram

\[
 Q_M(s)=\#\{u\ {\rm odd}\bmod M:au+bN/u\equiv s\pmod M\}.
\]

The source checked 1,008 exact interval and weighted-prefix identities.
Modular interval counts and fixed-degree weighted prefixes are therefore
compact in this candidate derivation. A zero count certifies an empty
geometric cap, but a positive count does not place representatives.

The obstruction is exact for the fixed normal \(a=b=1\): at \(M=1024\), two
inputs with the same complete objective histogram and cap bounds have
respectively two and zero cap points. The four-child lift recurrence isolates
the missing information as a signed carry

\[
 \chi(u)=(-1)^{(N-u(N/u\bmod L))/L},
\]

which also has a multiplicative-character representation. A direct shifted
stationary-root treatment already has \(\sqrt M/4\) distinct roots on one
ray. This rules out histogram-only localization and direct common-root reuse,
not other joint geometric algorithms.

The public odd-weight menu

\[
 a_j=2^{j+3}+(N\bmod8),\qquad b_j=65
\]

retains stationary roots at every dyadic depth and preserves the sufficient
factor-ratio cover. Mixed-parity dyadic normals instead have uniform complete
histograms. These unpromoted corollaries passed 288 exact histogram checks and
8,128 labelled factor-margin checks; neither supplies unwrapped localization.

The next operation is a polynomial or quasipolynomial evaluation or sharp
bound for the geometrically truncated signed carry. Evidence:
experiments/F290_dyadic_fourier_support/REPORT.md, NORMALS.md,
weighted_prefix.py/json, carry_rectangle.py/json, and
normal_grid_check.py/json/log.

### C252 -- Direction dominance removes exact families but not the high-stride phase catalogue

**Status:** author-derived proofs and exact finite pilots. Independent
reconstruction is pending.

**Scope:** the F291 dyadic inverse-patch directions, strict dominance
certificate, three low-stride families, and stated random/late controls. No
quasipolynomial catalogue bound.

**Discussion.**

For a primitive direction \((A,B)\) on a depth-\(r\) patch, F291 derives the
exact stride

\[
 g_u(A,B)=2^r\gcd(A+B\,d(u),2^{r+1}).
\]

For \(r\geq3\) and odd \(B\), maximal stride selects at most two inverse
classes and fixes their phases up to sign. A strict score improvement at the
direction's maximal shear certifies
domination at every shear. Separately, the three constant low-stride
categories \(v_2(A-NB)=0,1,2\) reduce to three exact two-dimensional CVP
representatives.

The pilots checked 59,904 global-dominance comparisons and 58,240 bounded
low-layer comparisons without failure. They also show the residual problem:
at 57--58 bits, roughly 30,000 direction/stride/phase keys remained. Reusing
a direction without its translated line phase gives little saving.

The next operation must enumerate or reject high-stride directions in whole
coefficient regions without first visiting their roots or primitive pairs.
Evidence: experiments/F291_direction_class_aggregation/RESULT.md,
direction_reuse.py/output.json, global_dominance.py/dominance_output.json,
and low_layers.py/low_layers_output.json.

### C253 -- Localized-character descent reaches a verified scalar kernel but leaves the outer cut phases

**Status:** synthesis of one promoted primitive with author-derived
transformations and exact finite checks. Only the single-kernel result P236
is promoted.

**Scope:** F292 paired-bit frontiers, fixed-conductor lift, Cochrane and
inverse reciprocity, and one rational-root quadratic-Gauss/Cauchy kernel. No
outer-sum or support algorithm.

**Discussion.**

The generic paired-bit linear representation has candidate rank at least
\(\sqrt M/8\). A short cap evades that rank bound because it has few high
blocks, but discovering the contributing low rows remains numerical. The
fixed-conductor lift keeps the cap and introduces linear additive phases; its
direct jump still has \(H=O(\sqrt M)\) character states. Sparse carry moments
give a formal recurrence only after their support or moments are already
known.

The inverse-Bernoulli target is a Cochrane sum. Phase-sensitive character
orthogonality produces two Gauss factors and a Kloosterman difference.
Elementary inverse reciprocity decreases a modulus but exposes explicit
divisor boundary terms and does not contract the number of smaller calls.
The odd-prime-power Kloosterman paper is a precise source lead, not a dyadic
theorem used here.

P236 removes one scalar obligation: at one rational root of unity, one
quadratic-Gauss/Cauchy kernel, including Taylor/Laurent coefficients and
exact removability, has output-sensitive polynomial bit cost. Evaluating
\(B_0\) distinct outer indices still costs \(B_0\) such calls. Several
denominators, arbitrary interior parameters, and the cut-phase family remain
outside the verified result.

The next step must aggregate the outer geometry coefficients before applying
the scalar primitive separately. Evidence:
experiments/F292_localized_character/REPORT.md, TWISTED_RECURRENCE.md,
RECIPROCITY.md, KERNEL_PRIMITIVE.md, KERNEL_RECONSTRUCTION.md, and their
exact JSON certificates.

### C254 -- Canonical half-square counts are a phase-sensitive numerical convolution

**Status:** root-derived identities and exact finite experiments.
Independent reconstruction is pending.

**Scope:** the F293 canonical half-square count, its sign word, complementary
lift, character square, and the specified finite recurrence screens. No short
coefficient evaluator.

**Discussion.**

Writing every unit modulo \(2^k\) as \(\pm5^t\) turns the exact half-square
correlation into one coefficient of a cyclic square \(P_k(z)^2\). This
retains canonical placement, but \(P_k\) has \(2^{k-2}\) signs. Reflection
halves the direct work again without changing its numerical scale.

The count obeys an exact mod-four orbit law and the complementary lift

\[
 C_M(N+M/2)=M/4-C_M(N).
\]

Its character expansion contains \(B(\chi)^2\), not
\(\lvert B(\chi)\rvert^2\); replacing it by an autocorrelation loses the
phase. The exact Rust trace evaluated more than 6.4 billion sign products
through \(k=34\) with constant memory. Fixed constant-coefficient
recurrences through order ten failed the retained Hankel and holdout tests.
These are finite exclusions, not a lower bound against nonlinear or
Euclidean contraction.

The missing object is a succinct reciprocal coefficient evaluator that
retains both square phase and window placement. Evidence:
experiments/F293_carry_convolution/RESULT.md, convolution.json,
reciprocal_trace.jsonl, recurrence_check.json, and word_moments.json.

### C255 -- Near-affine descent preserves both windows but leaves an unmatched kernel family

**Status:** author-derived identities and exact finite validations, including
a separate root-supplied identity check. No recursive closure or
quasipolynomial bound is promoted.

**Scope:** F294 near-affine counts, fixed-geometry slope blocks, faithful
inverse charts, formal-group/Gauss descent, and the tested reciprocal
recombination. P236 applies only to each individual scalar kernel.

**Discussion.**

F294 evaluates special near-affine half-window counts and large
fixed-geometry slope blocks in polynomial bit work. Actual inverse charts do
not hold that geometry fixed: changing origins couples the slope, constant,
and input window. The faithful normalization instead produces two
multiplicatively wrapped windows.

The formal-group coordinate and exact Gauss support reduce a modulus
\(q=m^2\) count to an \(m\)-term affine-window/carry kernel. Separate
coefficient-array and cyclotomic checks passed 17,872 Gauss cases, six direct
window counts, and 76 high-lift Cauchy identities. The Euclidean floor
recurrence then exposes floor-indexed incomplete Gauss moments and,
termwise, up to three Cauchy denominators with resonance derivatives.

Full child recombination cancels one apparent added denominator and collapses
some reciprocal phase orbits. Exact \(q=64,256\) checks still leave nonzero
unmatched cut-phase coefficients after every tested frame and pole term is
retained. P236 evaluates each such scalar kernel, but no operation aggregates
their outer coefficient family without numerical enumeration.

The concrete remaining task is geometry-aware outer cut-phase aggregation,
not another individual kernel formula. Evidence:
experiments/F294_near_affine_quadratic/RESULT.md, FORMAL_DESCENT.md,
RECOMBINATION.md, ROOT_GAUSS_WINDOW.md, and their exact outputs.

### C256 -- Auxiliary Gauss coordinates leave a quadratic half-window moment

**Status:** author-derived exact identities and finite symbolic validation.
Independent reconstruction is pending.

**Scope:** the F295 adjacent-ray coordinate transform, exact axis sums,
retained third denominator, joint-quadratic ansatz, and one literal residue
repair. No general lower bound or recursive evaluator.

**Discussion.**

Undoing the complete Gauss sum before separating cone terms lets adjacent
Euclidean rays become coordinate axes while retaining the full window
polynomial. Each pole-excluded axis transform then has an elementary
Bernoulli or half-window value. Expanding the remaining odd-\(b\) denominator
leaves an exact two-variable quadratic half-window/Bernoulli moment under a
unit-Jacobian polynomial map.

The remaining half-window is essential: completing that coordinate makes the
tested moment zero, while a retained q=64 component is \(-4\). The proposed
jointly quadratic closure fails by a nonzero mixed third difference. The
literal repair that stratifies the auxiliary \(x\) coordinate needs
\(2^{\lceil(r-2)/2\rceil}\) classes. This is an exact count for that repair,
not a bound on other contractions.

Seven complete-window checks, 256 auxiliary-Gauss identities, seven axis
moments, and 3,584 repaired phase identities passed. The next object is the
retained quadratic window moment, not a complete quadratic Gauss sum.
Evidence: experiments/F295_auxiliary_gauss_coordinates/RESULT.md,
auxiliary_coordinates.py, output.json, and run.log.

### C257 -- Fixed-frame theta reciprocity shortens the bulk and exposes two boundary families

**Status:** author-derived identities, exact algebraic checks, and
high-precision finite comparisons. Independent reconstruction is pending.

**Scope:** within one fixed F294 outer frequency \(b_0\), the F296 family of
sharp floor-indexed theta prefixes, its shorter bulk, exact mod-\(a\)
correction, centered Mordell endpoints, and retained source-formula
discrepancy. No aggregation over the odd \(b_0\) family and no completed
recursive cost bound.

**Discussion.**

Applying finite-theta reciprocity to all sharp prefixes in that fixed frame
contracts their common bulk from length \(m\) to at most
\(p+2\leq m/2+2\). A nested floor is removed exactly as a linear-floor bulk
plus a residue-inequality correction modulo \(a\). The old root-of-unity cut
weight remains. A second boundary family consists of centered Mordell
\(h\)-values with explicit endpoint phases.

The frame data \(A=b_0\beta\bmod m\), \(B=-b_0d_1\bmod m\), and
\(Z=e_m(-b_0)\), as well as the normalized child parameter \(p=2A\), depend
on \(b_0\). Thus this transformation does not sum the original odd
frequencies.

The cached Kuznetsov arXiv PDF visibly prints coefficient \(-1/2\) in
equation (7), while the derivation from its equations (16)--(17) gives
\(-i/2\). F296 retains the PDF hash, extracted image, failed printed-formula
run, and an exact nonzero difference witness. It uses the derived coefficient
without editing the source. Six 45-digit checks differed from the derived
formula by less than \(2\cdot10^{-42}\); they are numerical evidence, not
interval proofs.

The shorter fixed-frame bulk alone does not contract the two boundary
families or the original \(b_0\) family. A recurrence must retain the exact
mod-\(a\) cut and completed Mordell endpoints, and a separate grouping must
avoid per-\(b_0\) evaluation. Evidence:
experiments/F296_outer_reciprocity/REPORT.md, SOURCE_FORMULA.md,
outer_mordell.py/json/log, and outer_mordell_setup.log.

### C258 -- Uncentered completed prefixes absorb the fixed-frame cut into four endpoint families

**Status:** root-derived exact identities, a uniform analytic bound, and
finite exact/numerical checks. The same-cycle Astra worker checked the signs,
analytic domain, and cancellation collaboratively; this is not a fresh
statement-only reconstruction or a promotion.

**Scope:** within one fixed F294 outer frequency \(b_0\), the F297 centered
and uncentered completed-prefix formulas, four explicit Fresnel endpoints,
the regular Mordell remainder, and its coefficient construction. No endpoint
or moment-family evaluator, aggregation over odd \(b_0\), or factoring bound.

**Discussion.**

F296 writes its centered endpoint as \(r_j=R_j-\delta_j\), where \(R_j\) is
a simple linear-floor endpoint and \(\delta_j\in\{0,1\}\). Choosing
\(R=R_j\) directly gives \(-1\leq d<1\) and
\(-3/2\leq z=d-1/2<1/2\). The exact completed prefix then has four
erfc/Fresnel endpoint families. Its endpoint-shift identity cancels the
added dual-prefix term exactly when \(\delta_j=1\), so no separate indicator
family remains.

For \(\lvert z\rvert\leq3/2\), the regular remainder has the uniform
expansion

\[
 R_2(z,t)=\sum_{j\geq0}c_j^{(2)}(t)(2z)^{2j},\qquad
 |c_j^{(2)}(t)|\leq\frac4{5^{2j+1}},\qquad
 \left|R_2-\sum_{j<K}c_j^{(2)}(t)(2z)^{2j}\right|
 \leq\frac54\left(\frac9{25}\right)^K.
\]

Its coefficients have a constructive polynomial-bit approximation
procedure. The unresolved fixed-frame work is the total evaluation of the
four Fresnel families and the uniformly short list of polynomial moments in
the fractional parts of their actual linear expressions. This does not group
the original odd frequencies: \(A\), \(B\), \(Z\), and the normalized child
\(p\) still depend on \(b_0\).

Sixteen faithful q=64 and q=256 prefixes, including the q=256 cut positions
\(j=2,6\), agree with direct sums to at most \(3.30\cdot10^{-41}\). That run
took 0.984 seconds and 31.9 MB peak RSS. The packet also retains 6,072 exact
endpoint-phase checks, the earlier centered and remainder comparisons, and
the cached-source coefficient discrepancy. Evidence:
experiments/F297_mordell_boundary/RESULT.md, uncentered_prefix.py/json/log,
boundary_moments.py/json/log, completed_prefix.py/json/log, and their status
files.

### C259 -- A global parity recurrence closes its family but not its state count

**Status:** author-derived exact recurrence and finite verification.
Independent reconstruction is pending.

**Scope:** the F298 global rank-one quadratic two-window moment, its parity
symmetries, four-child recurrence, exact single-window corrections, and
signed state merging. No quasipolynomial state bound, arbitrary short-window
closure, inverse-chart union, or factoring algorithm.

**Discussion.** F298 adds one even linear parameter \(v\) and retains both
wrapped constants. Exact shifts reduce the complete domain to
\(0\leq x,t<m/2\). Splitting \(x=2X+e\), \(t=2T+f\) produces four children
of the same nonlinear family with

\[
 \gamma'\equiv2\gamma\pmod{m/2},\qquad
 v'\equiv v+2\gamma e\pmod{m/2},
\]

and exactly updated constants. The only extra terms are single-window
quadratic moments. Their complete dyadic strata leave at most two top atoms,
each evaluated by an affine half-window floor sum in polynomial bit work.

Identical signed child states can be canonicalized and merged exactly.
Nevertheless, an initially odd \(\gamma\) can branch for
\(\lceil r/2\rceil\) levels before it vanishes. The retained terminal-state
counts grow from 40 at \(r=6\) to 28,692 at \(r=16\) in the random control;
no polynomial or quasipolynomial bound on the whole child bank is proved.
The recurrence remains within one F294 chart and does not aggregate its
original \(u_0\) classes or replace the factor-isolating rectangles.

The pilot passed 192 pointwise parity checks, 24 one-step global
recurrences, 96 independent boundary-correction checks, and four full small
recursions against direct double sums. Evidence:
experiments/F298_global_quadratic_window/RESULT.md, parity_descent.py,
output.json, and run.log.

### C260 -- F299's faithful affine classes are exactly the P235 cover

**Status:** root-derived exact equivalence, worker algebra check, and finite
integer certificates. Independent reconstruction is pending.

**Scope:** the F299 all-frequency common-conductor identity within one F294
chart, its halfbox residue classes, their affine collapse, and the faithful
identification with P235. No faster class aggregation, original chart-union
evaluation, or factor-isolating rectangle interface.

**Discussion.** F299 groups every odd Fourier frequency in one chart before
any frequency-dependent theta normalization. With
\(m=2^k\), \(r=2^{\lfloor k/2\rfloor}\), and \(L=m/r\), its positive
halfbox expression first splits into \(r\) residue classes. For each class,
the change \(t=x+Lv\) is a bijection and turns the three-variable strip into
one ordinary affine half-window of modulus \(T=mL\). Two Euclidean floor
sums evaluate that class, so the proposed Barvinok step is unnecessary.

On a faithful inverse chart with original modulus \(M=m^3\), put
\(S=mr=2^{\lfloor(\log_2M)/2\rfloor}\). As the chart base \(u_0\) and
residue \(i_0\) vary, \(U_0=u_0+mi_0\) runs through every odd residue below
\(S\). The resulting lattice base and finite difference are exactly

\[
 (U_0,NU_0^{-1})+
 \mathbb Z\bigl(S,N((U_0+S)^{-1}-U_0^{-1})\bigr)+
 \mathbb Z(0,M),
\]

which is P235's affine cover, with exactly \(S/2\) classes. Reorganizing
those classes through F299 therefore supplies no new asymptotic mechanism.
The arbitrary-endpoint reduced interface does not itself assemble the
faithful chart union or the public short rectangles.

The packet checked 129 frequency-coset identities, 10,896 floor
flattenings, 5,728 affine-class points, 22 arbitrary windows, 288 abstract
collapse points, and 100 faithful inverse points from 20 classes. Evidence:
experiments/F299_global_covariance/REPORT.md, AFFINE_EQUIVALENCE.md,
global_covariance.py/json/log, and affine_equivalence.py/json/log.

### C261 -- Complete Salié summation leaves a Cauchy-weighted quadratic digit

**Status:** root-derived identities and exact finite checks. Independent
reconstruction is pending.

**Scope:** the F300 complete Gauss-weighted dyadic sum, its one- and
two-Cauchy-denominator variants, the parity filter, and the F294-to-P235
scope audit. No fast mixed Cauchy evaluator, original chart union, public
short-window reduction, or factoring bound.

**Discussion.** Completing the Gauss square and summing every odd frequency
reduces the denominator-free sum to two power-of-two square-root congruence
classes, whose progression sums have a polynomial-bit evaluation. This is a
complete Salié-type calculation with no sharp window.

One Cauchy denominator instead leaves the Fourier transform

\[
 \sum_{x\bmod m}e_m(2wx)\,
 \epsilon_m\!\left(d^{-1}(\gamma x^2+V)\right),
\]

and two denominators leave the same linear Fourier phase weighted by
\(W_{-d,m}(\gamma x^2+V)-m/4\). Thus summing all frequencies preserves a
canonical, position-sensitive quadratic digit; an unweighted quadratic
histogram does not replace it. An exact parity filter gives an
\(m\mapsto m/4\) descent for even \(w\), while odd \(w\) retains a
triangular-digit transform with no supplied fast aggregate.

The scope audit fixes the outer geometry. F294's original inverse modulus is
\(m^3\); its \(q=m^2\) calculation is internal to one of \(m/2\) odd
\(u_0\)-charts. Even a complete internal frequency sum leaves that chart
union and the change from full chart half-windows to P237's short public
rectangles. The inspected complete Salié formulas and complete
Fourier--Dedekind Cauchy algorithms treat separate structures.

The exact coefficient-array pilot passed 72 complete identities, 72
one-denominator identities, nine two-denominator identities, and 60 parity
filters for \(m=8,\ldots,256\). Evidence:
experiments/F300_salie_cauchy/RESULT.md, SCOPE_MAP.md, SOURCE_LEADS.md,
salie_digits.py/json/log, and salie_digits.status.json.

### C262 -- Bounded rational windows reduce rectangle emptiness to a global mixed Cauchy resolvent

**Status:** root-derived construction and bit-cost arguments, with exact
integer and certified interval checks. Independent statement-only
reconstruction is pending. This claim is not promoted by P237.

**Scope:** the F301 public reference implementation, bounded-degree rational
interval filters, their pole representation and error budget, and the
resulting whole-graph mixed resolvent. No fast resolvent evaluator or
unconditional factoring algorithm.

**Discussion.** For \(M=2^k\), F301 builds an odd rational sign
approximation from the dyadic scales \(2^j\), repeated by an even
\(s\) with \(3^s\geq32M\). Its degree is
\(D=s(k+2)=O((\log M)^2)\), and its coefficient bit lengths are
\(O((\log M)^3)\). Multiplying two shifted steps gives a public interval
filter \(\Phi_I\) with pointwise error at most \(2\cdot3^{-s}\). Hence its
whole inverse-graph sum differs from the exact rectangle count by at most
\(1/8\); another absolute \(1/8\) evaluation error permits exact recovery
by rounding.

All poles of the odd step are simple and purely imaginary, with positive
residues. After shifting to an interval, their real coordinates are the
exact half-integers \(A-1/2\) and \(B+1/2\); the two pole sets are separated.
The filter has at most \(2D\) ordinary Cauchy poles with explicit
polynomial-size conditioning and coefficient bounds.

The remaining mixed kernel is

\[
 Z_{N,M}(z,w)=
 \sum_{\substack{1\leq u<M\\u\ {\rm odd}}}
 \frac{1}{(u-z)((Nu^{-1}\bmod M)-w)}.
\]

Substitution of the pole expansions uses \(O(D^2)=O((\log M)^4)\)
well-conditioned calls per rectangle, plus directly computable one-variable
marginals. Combined with P237, a uniform quasipolynomial-bit evaluator for
these calls at the stated precision would use \(O(n^6)\) mixed calls for
complete factorization, up to fixed polynomial factors. No such evaluator is
given. P236 has an exponential root-of-unity denominator and does not apply
to this ordinary-coordinate kernel without a new proof.

The public reference wrapper matched trial division for all 4,095 inputs
through 4096 and 120 seeded inputs through 24 bits; 40 labelled pairs at
32--512 bits passed public-box coverage with no large oracle call. The filter
checks comprise 131,064 exact integer inequalities and 67
interval-certified original rectangles. The pole pilot isolated 93 positive
roots and passed 24 partial-fraction checks; its repaired numeric-parent
comparison and first failed log are retained. Evidence:
experiments/F301_factor_rectangles/REPORT.md, RATIONAL_FILTERS.md,
factor_rectangles.py, output.json, run.log, rational_filters.py/json/log,
rational_filters.status.json, rational_poles.py/json,
rational_poles_fixed.log, and rational_poles_fixed.status.json.

### C263 -- The ordinary-resolvent lift gives a Taylor bank but retains the selected half-count

**Status:** root-derived exact lift, certified rational error bounds, and
finite exact checks. Independent reconstruction is pending.

**Scope:** the F302 original dyadic inverse graph, its ordinary Cauchy
resolvent lift to half modulus, the far-pole Taylor bank, and the first
retained signed and unsigned moments. No constructor for the local moment
banks, public near-pole evaluator, global resolvent, or factoring algorithm.

**Discussion.** Write \(M=2L\), with \(L\) even. For each odd
\(1\leq a<L\), let \(b=Na^{-1}\bmod L\) and
\(c=(N-ab)/L\bmod2\). The two lifts to the graph modulo \(M\) are

\[
 (a+Lr,\ b+L(r\mathbin{\mathsf{xor}}c)),\qquad r\in\{0,1\}.
\]

With \(\sigma=(-1)^c\),

\[
 S_z(a)=\frac1{a-z}+\frac1{a+L-z},\qquad
 D_z(a)=\frac1{a-z}-\frac1{a+L-z},
\]

the original ordinary-coordinate resolvent satisfies

\[
 Z_{N,2L}(z,w)
 =\frac12\sum_a
 \left(S_z(a)S_w(b)+\sigma D_z(a)D_w(b)\right). \tag{1}
\]

Thus the lift produces four ordinary and four signed lower-modulus
resolvents. The signed object keeps \(N\bmod2L\); lowering only the point
coordinates to modulus \(L\) does not remove the carry character.

Center the lower coordinates at \(L/2\), with radius \(R=L/2\). If the
imaginary pole heights satisfy \(y_z,y_w>R\), a \(K\)-term reciprocal
expansion has errors

\[
 E_z=\frac{(R/y_z)^K}{y_z(1-R/y_z)},\qquad
 E_w=\frac{(R/y_w)^K}{y_w(1-R/y_w)}.
\]

The complete lifted resolvent error is at most

\[
 B_K=L\left(\frac{E_z}{y_w}
 +\frac{E_w}{y_z(1-R/y_z)}\right). \tag{2}
\]

Consequently, heights at least \(M\) and \(K=O(\log M)\) reduce the
evaluation to \(2K^2\) ordinary and signed scalar moments. This is an
evaluation statement given those moments. It does not construct them.
The public F301 poles also have heights of order \(1/\log M\), where this
global expansion does not contract. Local geometric partitions restore
Taylor convergence, but their zeroth joint moments are the original
inverse-graph rectangle counts.

The first signed moment already retains the selected half-count:

\[
 \tau_{00}=2C_M(N)-L/2. \tag{3}
\]

The first uncentered unsigned mixed moment retains the same count:

\[
 \mu_{11}(M)=2\mu_{11}(L)+L^3/2+L^2C_M(N). \tag{4}
\]

For \(M=32\), the inputs \(N=481\) and \(N=497\) have identical lower
graphs but selected counts \(6\) and \(2\), giving
\(\tau_{00}=4\) and \(-4\). This is the remaining operation in this
specific Taylor-bank lift, not a lower bound on other global methods.

The exact pilot passed 12 lift identities and eight far-pole
\(M^{-6}\) bounds. Its four probes of F301 pole intervals retain exact
rational midpoints; they do not identify those midpoints with the
algebraic poles. Evidence:
experiments/F302_resolvent_lift/RESULT.md, pilot.py, output.json, run.log,
and RESOURCE.md.

### C264 -- Global residue formulas expose a separate third-digit carry bank

**Status:** P238 promotes only the reconstructed modulo-\(M^2\) constructor.
The closed forms, higher-precision identities, finite Mahler separation,
and exponent-derivative dependency below are root-derived exact results or
finite evidence and are not part of that promotion.

**Scope:** F303 on the global canonical inverse graph for \(M=2^k\),
\(k\geq3\), and positive odd \(N\). This note records the direct
modulo-\(M^2\) formulas, the next \(Q_{j,2}/2\) precision bank, two tested
ways that do not recover it, and the primary-source overlap. No ordinary
Cauchy-resolvent accuracy, rectangle count, or factoring algorithm.

**Discussion.** Put

\[
 A_j=\sum_{u\ {\rm odd}<M}u^j,\quad
 \Pi_M=\prod_{u\ {\rm odd}<M}u,\quad
 q_u=\frac{u(Nu^{-1}\bmod M)-N}{M}.
\]

The full integer \(N\) is retained in \(q_u\). Replacing \(N\) by
\(N-cM\) leaves the canonical inverse points and every \(S_{ab}\)
unchanged, but sends \(q_u\) to \(q_u+c\) and changes the carry moments.

P238 uses the reconstructed truncated-product proof. A separate
simplification gives direct formulas. For \(a>b\geq0\), \(j=a-b\),

\[
 S_{ab}=
 \frac{aN^bA_j-bN^aA_{-j}}{j}\pmod {M^2}, \tag{1}
\]

where the numerator must be computed modulo
\(2^{2k+\nu_2(j)}\) before exact division by the 2-part of \(j\).
For \(a=b=t\geq0\),

\[
 S_{tt}=(M/2-t)N^t+t\Pi_M^2N^{t-M/2}\pmod {M^2}. \tag{2}
\]

These formulas use the same universal unit power sums and unit product.
They do not supply higher digits.

For \(a\geq b\geq1\), \(j=a-b\), the exact next correction is

\[
 S_{ab}=N^bA_j+bMN^{b-1}L_j
 +\frac{abM^2}{2}N^{b-2}Q_{j,2}\pmod {M^3}, \tag{3}
\]

where \(Q_{j,2}=\sum_u u^jq_u^2\) is even. When \(ab\) is odd, the
needed datum is \(Q_{j,2}/2\bmod M\), equivalently
\(Q_{j,2}\bmod2M\). Knowing only \(Q_{j,2}\bmod M\) loses one bit.
For \(S_{11}\), this correction would give the full residue modulo
\(M^3\); since \(0\leq S_{11}<M^3/2\), that residue would determine
\(S_{11}\) exactly. This single exact moment is still not the whole
ordinary Cauchy kernel or its required absolute-accuracy evaluation.

For a power of two \(R\), the exact high-input average

\[
 \sum_{t=0}^{R-1}S_{11}(MR,N+Mt)
 =R^2S_{11}(M,N)+M^3R^2(R^2-1)/8 \tag{4}
\]

does not gain a base-\(M\) digit: reduction modulo \((MR)^2\), correction,
and division by \(R^2\) return only \(S_{11}\bmod M^2\).

The retained input-Mahler test also does not justify a fixed cutoff. At
\(M=4096\), the order-64 coefficients of \(E_2\) and the normalized
residual have 2-adic valuation \(1\), so truncation at order 63 fails even
modulo 4 at the tested next input. This is a finite separation for that
cutoff, not a lower bound on other representations.

The exponent variation supplies no independent quadratic-carry equation.
With the 2-adic unit logarithm, \(\lambda=\log_{\rm adic}(N)\), the
computable family obeys

\[
 L(-t)=\exp(-t\lambda)L(t),\qquad
 L'(0)=\frac{\lambda}{2}L(0). \tag{5}
\]

All 16 guarded finite-difference checks passed while
\(Q_{0,2}/2\bmod M\) and \(e_2\bmod M\) were nonzero on 15 inputs.
For \(M=32,N=289\), the derivative residual is zero, but
\(Q_{0,1}=2\), \(Q_{0,2}=1090\), \(e_2=1\bmod32\), and
\(S_{11}=4688\).
Dropping the quadratic correction gives 3664; its contribution 1024
recovers 4688.

Andreica, *The Scientific World Journal* (2013), Article 751358, already
gives a non-enumerative power-sum/Newton algorithm for the odd unit product
in its stated precision range. F303 makes no novelty claim for that
primitive or for its mixed-moment identities. The checked Cochrane and
higher-Wilson sources identify related congruences but do not state P238's
full uniform mixed-moment algorithm.

Evidence:
experiments/F303_global_moment_precision/REPORT.md, CLOSED_FORM.md,
UNIT_PRODUCTS.md, EXPONENT_DERIVATIVE.md, SOURCE_LEADS.md,
MOMENT_RECONSTRUCTION.md, moment_precision.py/json/log,
closed_form_controls.py/json/log, and
exponent_derivative.py/json/log/status.

### C265 -- Guarded selectors close pointwise but leave a growing Möbius family

**Status:** F304 exact mechanisms and finite controls outside P240. P240
promotes only the reconstructed one-map moment constructor.

**Scope and mechanism.** Newton's parity lift satisfies, exactly,

\[
 E(a)=3a^2-2a^3=a+(1-2a)(a^2-a),\qquad
 E(a)^2-E(a)=(a^2-a)^2(4(a^2-a)-3).
\]

The error valuation doubles. Moments weighted by powers of the error and
by \(1,a\) form a finite triangular bank at fixed precision; the
two-coordinate bank has the four sectors \(1,a,b,ab\). With exact guarded
division by two after each recovered bit, this gives a canonical dyadic
interval-indicator circuit with \(O(k\log k)\) gates and \(2k\) working
bits for output modulo \(2^k\). Composing two indicators with \(u\) and
\(N/u\) is a faithful pointwise rectangle selector. No polynomial-cost
whole-graph trace of that circuit is known, and P240's numerical monomial
bank does not supply one.

Exact quotient branches stay in the P240 Möbius form. Splitting
\(x=e+2X\), \(y=f+2Y\), with \(f=n-e\bmod2\), gives

\[
 A'=A+Cf,\quad B'=B+Ce,\quad C'=2C,\quad
 n'=(n-Cef-Ae-Bf)/2.
\]

The determinant remains \(AB+Cn\), but each level has two actual maps.
For original patches with \(C=2^r\), three map values recover the distinct
odd residue \(B\bmod2^r\) when \(k\geq3r+1\). Hence the literal map
representation has \(\Theta(2^{k/3})\) states at
\(r=\lfloor(k-1)/3\rfloor\). This is not a lower bound against a different
aggregation.

**Finite evidence.** At \(k=7,10,13,16,19\), the tested patch counts were
\(2,4,8,16,32\). The distinct degree-two mixed-moment bank counts were
\(2,2,8,16,32\), while the carry-bank counts were \(2,4,8,16,32\).
The first repeated moment bank prevents promotion of map distinctness as a
claim about every truncated bank. Separate controls passed 73,696 digit
checks, 32 rectangles, and 780 one-map moment and carry checks.

The concrete missing step is a faithful non-enumerative aggregation over
the correlated map family, such as the shifted statistic in P239.

Evidence:
experiments/F304_guarded_digit_circuits/RESULT.md, ERROR_BANK.md,
MOBIUS_BRANCHES.py, MOBIUS_BRANCHES_output.json, MOBIUS_BRANCHES_run.log,
MOBIUS_BANK_GROWTH.py, MOBIUS_BANK_GROWTH_output.json,
MOBIUS_BANK_GROWTH_run.log, pilot.py, output.json, run.log, and RESOURCE.md.

### C266 -- Fixed-measure floor transport separates computable marginals from the window term

**Status:** F305 exact identities, a polynomial-bit marginal constructor,
and finite controls. No evaluator for the carry-weighted floor transform or
the shifted binomial statistic is supplied.

**Scope and mechanism.** For \(M=2^k\), canonical odd \(w\), and canonical
odd \(0<N<M\), put

\[
 u=w^{-1}\bmod M,\quad q_1=(uw-1)/M,\quad
 \mu_M(w)=u q_1(w),\quad
 f_{N,d}(w)=\left\lfloor\frac{Nw-d}{M}\right\rfloor.
\]

The output-shifted carry is

\[
 q_{0d}=Nq_1-u f_{N,d}.
\]

Thus all inputs use the fixed \(N=1\) measure, while the unresolved term is

\[
 T_0(N,d)=\sum_w\mu_M(w)f_{N,d}(w)\pmod M. \tag{1}
\]

In contrast, F305 constructs in polynomial bit cost the actual marginals

\[
 R_1^*(N,d)=\sum_ww^{-1}f_{N,d}(w),\qquad
 R_2(N,d)=\sum_ww^{-2}f_{N,d}(w)^2\pmod {2M}. \tag{2}
\]

A finite reciprocal expansion on \(w=1,3\bmod4\), followed by a
degree-preserving Euclidean floor recurrence, uses
\(O(D^2\log M)\) memoized states for total degree \(D\). All Faulhaber
divisions are exact rational arithmetic. This computes (2); it does not
integrate the measure in (1).

For an input cut \(c\), put \(x_c=u+M\mathbf 1_{u<c}\),
\(q_c=(x_cw-1)/M\), and \(\mu_c=x_cq_c\bmod M\). Define
\(H_c=\sum_wq_c\bmod M\), \(B_{c0}(1)=\sum_w\binom{q_c}{2}\bmod M\),
and \(T_c(N,d)=\sum_w\mu_c(w)f_{N,d}(w)\bmod M\).
The exact shifted transport is

\[
 B_{cd}(N)=N^2B_{c0}(1)+\binom N2H_c
 +\frac{R_2(N,d)+R_1^*(N,d)}2
 +(M/2-N)T_c(N,d)\pmod M. \tag{3}
\]

The numerator \(R_2+R_1^*\) is retained modulo \(2M\) and is even before
division. The computable terms cancel in the mixed window difference,
while

\[
 \Delta_c\Delta_dT_c=-C(c,d),\qquad
 \Delta_c\Delta_dB_{cd}=(N-M/2)C(c,d)\pmod M.
\]

Thus the carry/window term contains exactly the rectangle information that
the marginal bank lacks.

**Full input and remaining scope.** If \(N=\eta+tM\), with canonical
\(0<\eta<M\), then FULL_INPUT.md proves

\[
 B_{cd}(N)=B_{cd}(\eta)-tH_{cd}(\eta)
 +(M/2)\binom{t+1}{2}\pmod M.
\]

The first-carry correction \(H_{cd}\) is computable from P238 and reciprocal
prefixes, and it cancels from the four-corner difference. Individual
\(B\)-values still change; replacing the full input by its residue without
this correction is wrong. A dyadic reflection exposes a smaller inverse
graph but also a carry-bit weighted floor term at the original output
precision. No closed total-state recursion is known for those surviving
terms.

The retained pilot passed 11,352 pointwise transports, 150 shifted
binomial identities, 450 marginal values, and 25 reflection identities.
The non-enumerative \(M=2^{32}\) marginal run used 15,442 Euclidean states
and about 0.36 seconds. These checks support the identities and marginal
constructor only.

Evidence:
experiments/F305_input_carry_transport/REPORT.md, FULL_INPUT.md,
FLOOR_MARGINALS.md, input_transport.py, input_transport.json,
input_transport.log, and
input_transport_setup.log.

### C267 -- Whole-family norms expose one higher carry digit without contracting precision

**Status:** F307 author-derived exact identities and finite controls. No
complete claim received a fresh statement-only reconstruction, so no P record
is promoted.

**Scope.** Let \(M=2^k\), \(H=M/2\), and use P239's shifted representatives
with carry \(q=(xy-N)/M\). Put \(Q=\sum q\), \(B=\sum\binom q2\), and let
\(P_c,P_d\) be the two shifted odd progression products. The exact norm

\[
 R_{cd}=\frac{P_cP_d}{N^H}
       =\prod_{u\ {\rm odd}<M}\left(1+\frac MNq_u\right)
\]

is computable modulo \(M^3\) in polynomial bit cost from ordinary power sums
and a truncated progression product, without enumerating graph points or
Möbius branches.

Let \(\bar Q=Q\bmod M\) be recovered from the linear term, put
\(h=(Q-\bar Q)/M\), and let \(E_{cd}\) be the computable second residual
obtained after subtracting the \(\bar Q\) terms and exactly dividing by
\(M^2\). Expansion gives

\[
 E_{cd}=(N-M/2)h-B,\qquad B=(N-M/2)h-E_{cd}\pmod M. \tag{1}
\]

Thus the global norm removes explicit quadratic cross-branch sums, but
retains one higher digit of the total linear carry. Its four-corner
difference contains the rectangle count; it is not a marginal correction.

For \(f(x)=(ax+b)/(cx+d)\) and
\(g(y)=(ey+f_0)/(\ell y+i)\), with even \(c,\ell\) and odd
\(a,d,e,i\), exact carry composition is

\[
 q_{g\circ f}=(cx+d)q_g+(e-\ell z)q_f. \tag{2}
\]

Consequently \(\binom{q_{g\circ f}}2\) contains two weighted binomial sums,
two weighted linear sums, and the unit-weighted cross term
\((cx+d)(e-\ell z)q_fq_g\). The retained controls show that this summed cross
term need not vanish.

For \(h_c(x)=x/(1+cx)\) on \(0\leq x<L=2^s\), let
\(q_c=((1+cx)h_c(x)-x)/L\), \(S_c=\sum_xxh_c(x)\),
\(Q_c=\sum_xq_c\), and \(B_c=\sum_x\binom{q_c}{2}\), using canonical
\(h_c(x)\bmod L\). Summed doubling simplifies exactly to

\[
 Q_{2c}-2Q_c=\frac{2c}{L}(S_{2c}-S_c). \tag{3}
\]

At P240's \(L^2\) precision this is the same information as
\(Q_c=cS_c/L\); backwards doubling supplies no independent digit. A separate
non-enumerative norm for \(c=2^r\), \(1\leq r\leq s\), computes a
residual \(E_c\). With \(\bar S_c=S_c\bmod L^2\) canonical, however,

\[
 B_c=-t_c-E_c\pmod L,\qquad
 t_c=(S_c-\bar S_c)/L^2,
\]

still needs the third \(L\)-adic digit of \(S_c\). Dropping \(t_c\) failed
all 52 retained controls. These results reject this precision-contraction
ansatz, not composition or aggregate functionals in general.

Evidence:
experiments/F307_global_second_product/RESULT.md,
experiments/F307_global_second_product/COMPOSITION.md,
experiments/F307_global_second_product/pilot.py,
experiments/F307_global_second_product/output.json,
experiments/F307_global_second_product/run.log,
experiments/F307_global_second_product/H_C_NORM.py,
experiments/F307_global_second_product/H_C_NORM_output.json,
experiments/F307_global_second_product/H_C_NORM_run.log,
experiments/F307_global_second_product/COMPOSITION.py,
experiments/F307_global_second_product/COMPOSITION_output.json,
experiments/F307_global_second_product/COMPOSITION_run.log,
experiments/F307_global_second_product/EXPLORATORY.py,
experiments/F307_global_second_product/EXPLORATORY_output.json,
experiments/F307_global_second_product/EXPLORATORY_run.log,
experiments/F307_global_second_product/RESOURCE.md, and
experiments/F307_global_second_product/COMPOSITION_RESOURCE.md.

### C268 -- Three reciprocal-square marginals evaluate the full ordinary cocycle remainder

**Status:** F308 author and root-derived exact identities with finite controls.
The general ordinary remainder is constructed, but the inverse-floor and
input-cut terms remain. No P record is promoted.

**Scope and cocycle.** For \(k\geq3\) and odd canonical \(w<M=2^k\), let
\(u=w^{-1}\bmod M\), \(\mu(w)=u(uw-1)/M\), and
\(f_{A,d}(w)=\lfloor(Aw-d)/M\rfloor\). Define

\[
\begin{aligned}
T(A,d)&=\sum_w\mu(w)f_{A,d}(w),\\
K_d(A,B)&=\sum_w f_{A,d}(w)f_B(w^{-1}\bmod M),\\
R_d(A,B)&=\sum_wu^2f_B(w)f_{A,d}(Bw\bmod M).
\end{aligned}
\]

For raw positive odd \(A,B\), signed \(d\), and
\(b=B^{-1}\bmod M\), exact transport gives

\[
 T(AB,d)=BT(A,d)+AT(B,0)-K_d(A,B)+bR_d(A,B)\pmod M. \tag{1}
\]

The shifted measure adds the explicit affine-window pullback
\[
 C_{c,d}(A,B)=
 \sum_w\bigl(\mathbf1_{Bu\bmod M<c}-B\mathbf1_{u<c}\bigr)f_{A,d}(w).
\]

**Positive construction.** Put

\[
 V(A,d)=\sum_{w\ {\rm odd}<M}w^{-2}f_{A,d}(w)^2\pmod {2M}.
\]

Squaring the exact floor composition and retaining the inverse-square lift
modulo \(2M\) proves

\[
 2A R_d(A,B)=V(AB,d)-A^2V(B,0)-B^2V(A,d)\pmod {2M}. \tag{2}
\]

The right side is even. Divide its even canonical residue by two in the
integers, then invert the odd \(A\) modulo \(M\). Thus three calls to F305's
polynomial-bit \(V\) evaluator compute the general \(R_d\bmod M\), with no
unit enumeration. This removes the ordinary remainder completely.

For \(d=0\), set
\[
 W(A)=A^{-1}V(A,0)/2,\qquad S(A)=T(A,0)-W(A).
\]
The corrected cocycle is
\[
 S(AB)=BS(A)+AS(B)-K_0(A,B)\pmod M. \tag{3}
\]

For canonical odd \(0<A<M\) and square input \(N=A^2\bmod M\),
sign and inversion orbits give
\[
 K_0(A,A)=2\left\lfloor\frac{A(M/2-1)}M\right\rfloor\pmod4.
\]
Together with an exact ordinary floor-square identity, this constructs
\(T(N,0)\bmod4\) for \(N=1\bmod8\). It does not give \(T\bmod M\).

The remaining unknowns are \(K_d(A,B)\) and, with an input cut, the affine
pullback \(C_{c,d}(A,B)\). No closed descent for either is proved.

The retained small refinement checked 84 full \(R_d\) residues and 28
corrected \(S\) cocycles. A non-enumerative \(k=64\) general \(R_d\) case
used three banks of at most 11,596 states and 1.55 seconds. The balanced
\(k=128\) attempt reached the 30-second timeout before producing a result;
its empty named log is preserved and no value is claimed. Separately, the
square-input modulo-four evaluator completed through \(k=128\).

Evidence:
experiments/F308_carry_floor_cocycle/REPORT.md,
experiments/F308_carry_floor_cocycle/FULL_R.md,
experiments/F308_carry_floor_cocycle/pilot.py,
experiments/F308_carry_floor_cocycle/pilot.json,
experiments/F308_carry_floor_cocycle/pilot.log,
experiments/F308_carry_floor_cocycle/refinement.py,
experiments/F308_carry_floor_cocycle/refinement_small.json,
experiments/F308_carry_floor_cocycle/refinement_small.log,
experiments/F308_carry_floor_cocycle/refinement_k64.json,
experiments/F308_carry_floor_cocycle/refinement_k64.log,
experiments/F308_carry_floor_cocycle/refinement_k128.log, and
experiments/F308_carry_floor_cocycle/PREFLIGHT.md.

### C269 -- Complete dyadic pair products collapse to powers of one band

**Status:** F309 root-derived exact identity and non-enumerative constructor.
It is not a shifted carry evaluator and received no independent complete
reconstruction.

**Scope.** For a P240 Möbius map modulo \(L=2^s\) with \(s\geq2\), put
\(K=AB+Cn\). For cuts \(c,d\in[0,L]\), set \(x_i=c+i\),
\(0\leq i<L\), and let \(y_i\) be the representative of \(T(x_i)\bmod L\)
in \([d,d+L)\). For \(1\leq r\leq s\), let

\[
 V_r(c,d)=
 \prod_{\substack{i<j\\v_2(j-i)=s-r}}
 \frac{y_j-y_i}{T(x_j)-T(x_i)}.
\]

The map is a 2-adic isometry, so each quotient is a unit after cancelling
the common power of two. If
\(\Pi_D(c)=\prod_{i=0}^{L-1}(B+C(c+i))\), then

\[
\begin{aligned}
V_1(c,d)&=
 \frac{\sigma(c,d)\Pi_D(c)}{(-K)^{L/2}},\\
V_r(c,d)&=V_1(c,d)^{\,2^{r-1}}\quad(r\geq2),\\
\sigma(c,d)&=(-1)^{n+c+d+(-K-1)/2+C/2}. \tag{1}
\end{aligned}
\]

The progression product \(\Pi_D(c)\) has a uniformly truncated
power-sum/Newton constructor at any requested precision. Hence every band
product is computable in polynomial bit cost without enumerating pairs or
graph points. All bands are powers of the first value and supply no
independent parameters.

For any two source and target cuts, equation (1) gives identically

\[
 \frac{V_r(b,d)V_r(a,c)}{V_r(a,d)V_r(b,c)}=1. \tag{2}
\]

The source progression factor and separable target sign cancel. Thus this
complete unweighted pair product loses the mixed window contrast and cannot
replace P239's shifted binomial statistic. Weighted or restricted products
remain outside this result.

The pilot passed 324 exact band comparisons on 72 maps and 129,528 reference
pairs. All mixed contrasts were one on test rectangles with counts 1, 0, and
16. A correctly coupled \(M=2^{65}\), \(L=2^{64}\) case computed all 64
bands at 128-bit precision in 0.062 seconds without graph enumeration; its
large values were not independently pair-enumerated.

Evidence:
experiments/F309_pair_product_scales/REPORT.md,
experiments/F309_pair_product_scales/pilot.py,
experiments/F309_pair_product_scales/output.json,
experiments/F309_pair_product_scales/run.log,
experiments/F309_pair_product_scales/status.json, and
experiments/F309_pair_product_scales/RESOURCE.md.

### C270 -- Fixed-order Walsh phase matrices have high finite rank but may have easy totals

**Status:** F310 exact finite rank and nullspace evidence. No asymptotic rank
formula, scalar-summation lower bound, or promoted theorem.

**Scope.** For odd \(N\), \(M=2L\), and \(L=2^s\) with \(s\geq1\), define
\[
 F_N(x)=\frac{(N-1)/2-x}{1+2x}\pmod L,\qquad
 \epsilon_N(x)=(-1)^{\operatorname{bit}_{s-1}(x)+
 \operatorname{bit}_{s-1}(F_N(x))}.
\]
Exactly \(\epsilon_N(x+L/2)=\epsilon_N(x)\). With
\(r=\lfloor(s-1)/2\rfloor\), F310 tests the single ordering
\[
 A[a,b]=\epsilon_N(a+2^rb),\quad
 0\leq a<2^r,\quad 0\leq b<2^{s-1-r}.
\]

Over \(\mathbb F_{65521}\), the structured inputs \(N=9M+1\) had ranks
\(R-3\) for matrix orders \(R=8,16,32,64,128,256\). Inputs \(9M+3\) and
\(9M+5\) had rank \(R-2\) for the tested orders 64, 128, and 256; seeded
inputs had varied deficiencies. Every rank has retained independent rows,
pivot columns, and a nonzero full-rank minor certificate.

A nonzero minor modulo 65521 is nonzero over characteristic zero. For
\(N=9M+1\), direct rational nullspaces at orders 8, 16, 32, and 64 also had
nullity three. Therefore a fixed-cut decomposition
\[
 A[a,b]=\sum_{j=1}^t p_j(a)q_j(b)
\]
over characteristic zero needs \(t\) at least the displayed finite rank.
This constrains this variable order and linear signed-state representation.

It does not bound the cost of the scalar sum. The Hadamard matrix
\((-1)^{a\cdot b}\) has full rank but total sum \(2^r\) by character
cancellation. Thus the practical conclusion is only that this fixed
low/high linear separation does not show a small state in the tested range;
nonlinear, algebraic, or direct total-sum mechanisms remain open.

The 18 finite-field cases took 0.366 seconds at 258,392,064 bytes peak RSS.
The four rational nullspaces took 0.0354 seconds at 257,556,480 bytes.
All complete vectors, supports, minors, the setup-failure note, timeout
controls, and resource records are retained.

Evidence:
experiments/F310_walsh_phase_rank/RESULT.md,
experiments/F310_walsh_phase_rank/NULLSPACE_RESULT.md,
experiments/F310_walsh_phase_rank/walsh_phase_rank.sage,
experiments/F310_walsh_phase_rank/walsh_phase_rank.json,
experiments/F310_walsh_phase_rank/walsh_phase_rank.log,
experiments/F310_walsh_phase_rank/walsh_phase_nullspace.sage,
experiments/F310_walsh_phase_rank/walsh_phase_nullspace.json,
experiments/F310_walsh_phase_rank/walsh_phase_nullspace.log,
experiments/F310_walsh_phase_rank/RESOURCE.md,
experiments/F310_walsh_phase_rank/NULLSPACE_RESOURCE.md, and
experiments/F310_walsh_phase_rank/SOURCE_LEADS.md.

### C271 -- Finite-field phase models give exact small cases and scoped exclusions

**Status:** F311 exact exploratory constructions and nonmembership
certificates. They do not give a uniform selected-window evaluator or a
factoring algorithm.

For the complete ring-inverse half-period phase, with
\(M=2^k\), \(L=M/2\), and \(q=L/2\), F311 first tested Artin--Schreier
trace models over \(\mathbb F_q\). The input \(N=527\), \(M=64\),
\(q=16\) has complete signed total 12. This exceeds the genus-one bound
\(2\sqrt q+1=9\) for \(\operatorname{Tr}(aX+b/X)+\epsilon\), and also
the bound 11 after allowing two filled finite poles and regular infinity.
In sign/log coordinates the same phase nevertheless has the exact
genus-two model
\[
 \operatorname{Tr}\!\left(\alpha^3+(1+\alpha)X+
       \frac{\alpha^2}{X(X+1)}\right),
 \qquad \alpha^4+\alpha+1=0,
\]
away from \(X=0,1\), with both actual pole bits zero. Its smooth curve has
27 points and Frobenius trace \(-10\), giving the required total 12 after
the two filled values.

For fixed poles at zero and infinity of prescribed odd orders, every Walsh
coefficient obeys the corresponding \(2g\sqrt q+1\) envelope, including
one filled finite-pole value. This is only a discriminator for that fixed
pole family. At \(N=8193\), \(M=1024\), ordinary coordinates, a retained
256-bit dual vector annihilates all 258 columns of the symmetric order-31
family but pairs to one with the target; the column rank is 210. This is an
exact nonmembership certificate for that finite family, not a lower bound
for scalar summation.

The nonlinear bijections \(X\mapsto X^{-1}+a\), with inverse zero defined
as zero, make four tested ordinary-coordinate phases at \(q=16\) exactly
quadratic. Their totals are then computed by exact quadratic elimination;
no tested case at \(q\geq32\) became quadratic. These bounded coordinate
pullbacks do not transport integer interval masks for free.

A final bounded moving-pole search tested
\[
 \epsilon+\operatorname{Tr}\!\left(aX+\frac b{X-r}+
                                      \frac c{X-s}\right),
 \quad r\ne s,\quad b,c\ne0,
\]
with both pole bits freely filled. The exact prescreen rejects this
at-most-genus-two family when
\(W_{\max}>2\) and \((W_{\max}-2)^2>16q\). Coverage at
\(q=32,64,128\) is exhaustive over original residues up to complement in
both ordinary and sign/log coordinates. At \(q=32\), 18 of 64 targets
fit, with 20 complete models retained. At \(q=64\), all 128 targets were
covered by 12 prescreen rejections and 116 full searches, with no model;
at \(q=128\), the corresponding counts were 74 and 182 among 256 targets,
again with no model. At \(q=256\) only 16 seeded original residues in each
of the two encodings were tested: 17 were rejected and 15 fully searched,
with no model. The \(q=256\) result is not exhaustive.

All searches enumerate finite truth tables or coefficient families. Even a
complete scalar phase model would not implement P239's arbitrary cuts.

Evidence:
experiments/F311_finite_field_phase/RESULT.md,
experiments/F311_finite_field_phase/PRIMARY_SOURCES.md,
experiments/F311_finite_field_phase/pilot.py,
experiments/F311_finite_field_phase/output.json,
experiments/F311_finite_field_phase/run.log,
experiments/F311_finite_field_phase/CERTIFICATES.py,
experiments/F311_finite_field_phase/CERTIFICATES_output.json,
experiments/F311_finite_field_phase/CERTIFICATES_run.log,
experiments/F311_finite_field_phase/QUADRATIC_PULLBACK.py,
experiments/F311_finite_field_phase/QUADRATIC_PULLBACK_output.json,
experiments/F311_finite_field_phase/QUADRATIC_PULLBACK_run.log,
experiments/F311_finite_field_phase/MOVING_POLES.py,
experiments/F311_finite_field_phase/MOVING_POLES_output.json,
experiments/F311_finite_field_phase/MOVING_POLES_run.log,
experiments/F311_finite_field_phase/MOVING_POLES.md,
experiments/F311_finite_field_phase/MOVING_POLES_RESOURCE.md, and
experiments/F311_finite_field_phase/RESOURCE.md.

### C272 -- Orbit precision leaves a signed binary overlap and exact cut terms

**Status:** F312 author-derived identities with exact finite controls. The
core value-precision theorem is separately promoted as P241; this record
does not construct the remaining overlap.

For \(k\geq3\), canonical odd \(0<A<M=2^k\), and odd \(\epsilon\), let
\(i(w)=\epsilon w^{-1}\bmod M\),
\(H_\epsilon(f)=\sum_w f(w)f(i(w))\), and
\(U(f)=\sum_w f(w)^2\) over odd \(w<M=2^k\). Applying F312's two-bit value
compression to the centered floor \(f(w)=\lfloor Aw/M\rfloor\) reduces the
modulo-eight correction to a signed one-bit function. Equivalently, with
\(a(w)=f(w)\bmod2\), \(h=(A-1)/2\),
\(C_\epsilon=\sum_w a(w)a(i(w))\), and
\(n_a=\sum_w a(w)\),
\[
 H_\epsilon(f)=U(f)-n_a+C_\epsilon
 -4\!\sum_{\substack{w<M/2\\w^2=-\epsilon\ (\bmod M)}}
          (f(w)-h\bmod2) \pmod8. \tag{1}
\]
The ordinary terms and the at most four exceptional roots have
polynomial-bit dyadic constructors. The root sum is empty for
\(\epsilon=1,3,5\) and must be retained for \(\epsilon=7\). The binary
overlap \(C_\epsilon\bmod8\) remains unknown.

Half-translation does not add automatic orbit-size divisibility. With
\(L=M/2\), \(h_M(w)=w+L\bmod M\), and
\(f_{A,d}(w)=\lfloor(Aw-d)/M\rfloor\) for integer \(d\),
the exact increment, including both boundaries, is
\[
 f_{A,d}(h_M(w))-f_{A,d}(w)=\frac{A-1}{2}
 +\mathbf1_{(Aw-d)\bmod M\geq L}-A\mathbf1_{w\geq L}. \tag{2}
\]
On a generic eight-element sign/inversion/translation orbit, put
\(\delta=f(w)-f(i(w))\) and
\(e=f(h_M(w))-f(w)-f(h_M(i(w)))+f(i(w))\).
Its contribution to \(H-U\) is
\(-2[\delta^2+(\delta+e)^2]\), hence modulo eight it is
\(-2[(\delta\bmod2)+((\delta+e)\bmod2)]\). On the same orbit modulo 32,
the tested floors with \(A=3\) and \(A=5\) contribute respectively 4 and
6 modulo eight. Thus generic orbits need not vanish; bounded exceptional
orbits do not remove the remaining generic binary weights.

The exact quotient by the two lifts retains intercepts and interval masks.
For odd \(a<L\), put \(b=\epsilon a^{-1}\bmod L\) and
\(c=(\epsilon-ab)/L\bmod2\). The inverse pairs are
\((a,b+Lc)\) and \((a+L,b+L(1-c))\). For arbitrary functions \(x,y\),
define \(P_x(a)=x(a)+x(a+L)\) and
\(Q_x(a)=x(a)-x(a+L)\). Their contribution is exactly
\[
 \frac{P_x(a)P_y(b)+(-1)^cQ_x(a)Q_y(b)}2. \tag{3}
\]
For \(x(w)=\lfloor(Aw-d)/M\rfloor\),
\[
 P_x(a)=\left\lfloor\frac{Aa-d}{L}\right\rfloor+\frac{A-1}{2},
 \qquad
 Q_x(a)=-\frac{A-1}{2}-\mathbf1_{(Aa-d)\bmod M\geq L}. \tag{4}
\]
Multiply each lift value by its actual source or image mask before forming
\(P\) and \(Q\). To recover a result modulo \(2^p\), the numerator in (3) must be retained modulo
\(2^{p+1}\), proved even, and divided in the integers. This halves the
inverse-graph modulus but does not lower the requested output precision;
it leaves a carry-signed product. Literal orbit enumeration remains
exponential.

The pilot checked 43 ordinary dyadic quotients, 43 with both cuts, 43
parity reductions, 172 square-class formulas, 716 precision-compression
instances, and 538 complete orbits. It retains the nonzero generic norms
and a shifted-cut counterexample where the actual value is 6 modulo eight
but the boundary-free parity formula gives 2.

Evidence:
experiments/F312_orbit_precision/REPORT.md,
experiments/F312_orbit_precision/pilot.py,
experiments/F312_orbit_precision/pilot.json, and
experiments/F312_orbit_precision/pilot.log.

### C273 -- Integral symmetric powers give mod-four cut traces but leave restricted Hadamard sums

**Status:** F314 author-derived identities and bounded exact certificates.
No independent reconstruction or promoted algorithm is claimed.

Let \(L=2^s\), \(d=L-1\), and let \(V\) be the degree-at-most-\(d\)
polynomials over \(\mathbb Q_2\) that map \(\mathbb Z_2\) into itself.
The binomial polynomials \(\binom{X}{j}\), \(0\leq j<L\), form an integral
basis. For the P240 Möbius matrix \(g\), weighted substitution
\[
 \rho(g)f(X)=(B+CX)^d f\!\left(\frac{n-AX}{B+CX}\right)
\]
and its inverse preserve this lattice. Evaluation on \(0,\ldots,L-1\)
therefore gives an invertible integral matrix \(R\) whose reduction modulo
two is the canonical permutation matrix \(U\).

For arbitrary node subsets \(I,J\),
\[
 H(I,J)=\operatorname{tr}(D_I R D_J R^{-1})
\]
equals the canonical rectangle count modulo four. Off-permutation products
are divisible by four, while \(RR^{-1}=1\) makes each on-permutation
product one modulo four. This statement holds for every invertible integral
lift of a permutation. It fails modulo eight for the displayed weighted
lift: at \(L=8,A=3,B=5,C=2,n=7\), \(I=[0,2)\), \(J=[0,1)\), the count is
zero but \(H=4\bmod8\); the exact odd-denominator rational value is retained.

For requested precision \(p\), put \(m=\lceil p/2\rceil\) and
\[
 F_m(z)=\sum_{t=m}^{2m-1}\binom{2m-1}{t}z^t(1-z)^{2m-1-t}.
\]
This degree-\(O(p)\) integer polynomial sends each entry product
\(z_{ij}=R_{ij}R^{-1}_{ji}\) to its permutation bit modulo \(2^p\).
It is an exact idempotent lift with no nonunit divisions or extra precision.
Summing it still requires \(O(p)\) cut-restricted Hadamard moments, however;
ordinary tensor characters do not supply the equal-index projector, and
literal evaluation retains \(L^2\) pairs.

Pascal tensor structure makes each prefix cut compact and gives its
coefficient-basis projector an explicit diagonally scaled Cauchy block, but
no polylogarithmic trace contraction follows. Two narrower substitutions
are excluded exactly. Reducing the ordinary symmetric power modulo two sees
only \(g\bmod2\) and a monomial-to-binomial conversion incurs the factorial
guard \(v_2((L-1)!)=L-1-s\). Also, the integral group algebra of the
lattice-preserving Möbius operators sends the all-ones node vector only to
constant vectors, so it cannot contain a proper nonempty cut projector.
These exclusions do not cover rational even-denominator combinations,
mixed identities, or nonlinear direct scalar methods.

The pilot checked 21,447 exact assertions for 12 maps through \(L=16\),
including every prefix pair, both inverses, the projector formula, the
modulo-eight witness, and precision lifts through \(p=12\). It took 0.074
seconds at 17,481,728 bytes peak RSS. The unresolved operation is a uniform
evaluator for the restricted Hadamard moments or an equivalent rational
cut-character identity with explicit denominator control.

Evidence:
experiments/F314_integer_valued_representation/RESULT.md,
experiments/F314_integer_valued_representation/pilot.py,
experiments/F314_integer_valued_representation/pilot.json, and
experiments/F314_integer_valued_representation/pilot.log.

### C274 -- Exact bulk transport spectra are dense finite data, including a fast control bit

**Status:** F315 exact enumerative discovery with bounded resource controls.
No asymptotic degree statement, complexity lower bound, or promoted
algorithm is claimed.

For \(M=2^k\), \(R=M/4\), and the unit coordinates
\(w=(-1)^\epsilon5^j\), F315 forms
\[
 b(w)=w,\qquad a(w)=\mu(w^{-1})\bmod16.
\]
Four exact Sage/FLINT integer-polynomial cyclic convolutions on
\(C_2\times C_R\) compute
\(C_r=\sum_w(\mu(w)\bmod16)(rw\bmod M)\) for every odd \(r\). With
\(A_\mu=\sum_w(\mu(w)\bmod16)w\), exact integer division gives
\[
 T(8M+r)=\frac{(8M+r)A_\mu-C_r}{M}\pmod {16}. \tag{1}
\]
The full input keeps \(M\) as the public power selected from \(N/8\).
Every divisibility guard and the raw/canonical correction were checked.

The three Boolean bits of \(T(8M+r)/2\bmod8\) were transformed exactly to
algebraic normal form in ordinary \(r=1+2x\) and sign/log
\(r=(-1)^\epsilon5^j\) coordinates for \(k=8,10,12,14,16,18\). At
\(k=18\), the ordinary degrees and monomial counts were
\((15,65081),(15,65838),(16,65462)\); sign/log gave
\((15,32685),(15,32696),(16,65620)\). The degree-one variation at
\(k=12,18\), all counts by degree, and the square/nonsquare restrictions
are retained as finite data only.

The first displayed bit is a positive control: P242 already computes that
scalar total in polynomial bit cost, although its tested ANF is dense and
has high degree. Therefore ANF density or degree is not evidence that the
next scalar bits are hard, and no lower bound is inferred.

All odd residues through \(M=128\) and eight residues at each larger scale
were checked by direct summation. The identity
\(t_0(-r)=t_0(-1)+t_0(r)\) held on every complete table. Truth tables and
dense ANFs are packed with SHA-256 hashes; sparse ANFs retain exact masks.
The pilot took 0.618 seconds at 257,392,640 bytes peak RSS, and the scale run
took 1.637 seconds at 309,329,920 bytes. The four convolutions enumerate the
finite group and are a discovery method, not a quasipolynomial constructor.

Evidence:
experiments/F315_bulk_carry_spectrum/REPORT.md,
experiments/F315_bulk_carry_spectrum/bulk_carry_spectrum.py,
experiments/F315_bulk_carry_spectrum/pilot_output.json,
experiments/F315_bulk_carry_spectrum/pilot_run.log,
experiments/F315_bulk_carry_spectrum/pilot_status.json,
experiments/F315_bulk_carry_spectrum/scale_output.json,
experiments/F315_bulk_carry_spectrum/scale_run.log,
experiments/F315_bulk_carry_spectrum/scale_status.json,
experiments/F315_bulk_carry_spectrum/RESOURCE.md, and
experiments/F315_bulk_carry_spectrum/SHA256SUMS.txt.

### C275 -- A guarded half-modulus section transform leaves one mixed correlation

**Status:** F316 author-derived identities and bounded exact checks. No
constructor for \(K\bmod8\), \(T\bmod8\), or a shifted cut is promoted.

Let \(M=2^k\), \(T=M/4\), and
\[
 e_j=\left\lfloor\frac{5^j\bmod4M}{M}\right\rfloor\in\{0,1,2,3\},
 \qquad S_M(r)=[z^r]\left(\sum_{j<T}e_jz^j\right)^2\pmod4.
\]
For \(k\geq4\), the unsigned canonical carry for \(A=5^a\bmod M\) is
\[
 C_a(j)=3\left\lfloor\frac{a+j}{T}\right\rfloor
        -e_a-e_j+e_{a+j\bmod T}\pmod4. \tag{1}
\]
Its complete inverse-paired product reduces to four \(S_M\) values, an
ordinary overlap, a linear prefix correction, and point terms. Writing
\(e=\eta+2\xi\) gives \(e^2=\eta^2\pmod4\), but the off-diagonal products
and the linear correction remain. Dropping the latter already fails at
\(M=16,a=b=1\).

For the genuine half-modulus step, assume \(k\geq5\), put \(H=T/2\), and
for \(0\leq j<H\) define
\[
 s_j=\left\lfloor\frac{5^j\bmod M}{M/2}\right\rfloor,
 \quad B_j=1-s_j,\quad P_j=e_j\bmod2.
\]
The lift satisfies
\(e_{j+H}=e_j-B_j-2(j\bmod2)\pmod4\). The cyclic and negacyclic
projections determine only the sum and difference of
\(S_M(r),S_M(r+H)\bmod4\); dividing those residues loses one bit. Retaining
the projections modulo eight and dividing in the integers gives exactly
\[
 S_M(r)=\sum_{j=0}^{r}B_jB_{r-j}
       +2\bigl([z^r]P^2-[z^r]PB\bigr)\pmod4,
 \qquad 0\leq r<H. \tag{2}
\]
The first term is a truncated ordinary convolution. The point-value term
\([z^r]P^2\bmod2\) is easy, while the remaining correction is
\[
 [z^r]PB=\sum_{j<H}
 \operatorname{highbit}_M(5^j\bmod2M)
 \left[1-\operatorname{highbit}_{M/2}
   (5^{r-j\bmod H}\bmod M)\right]\pmod2. \tag{3}
\]
It is a mixed high/low-section correlation, not the complete square that
collapses in P242. At \(M=32,r=0\), omitting (3) returns 1 instead of the
correct \(S_M(0)=3\bmod4\).

F316 also derives the exact unsigned diagnostic
\[
 \frac{T(A,0)}{2}=2a+L_a+S_M(0)-S_M(a)+R_0-R_a-\frac{A-1}{2}\pmod4,
\]
but does not aggregate its surviving correlations. Repeating (2) has no
proved polynomial-size closed bank because (3) keeps a digit from the
larger lift and the first term keeps an endpoint. Arbitrary cuts add further
nonconstant masks.

The pilot checked 6,048 carry digits, 144 paired products, 144 transport
identities, 252 square replacements, and 124 guarded half-modulus cases.
Both omitted-linear and unguarded-division failures are retained. Runtime
was 0.010 seconds at 17,612,800 bytes peak RSS.

Evidence:
experiments/F316_cocycle_precision/REPORT.md,
experiments/F316_cocycle_precision/pilot.py,
experiments/F316_cocycle_precision/pilot.json, and
experiments/F316_cocycle_precision/pilot.log.

### C276 -- Normalized Cauchy entries are efficient but their moving quotient is not aggregated

**Status:** F317 author-derived identities, exact bounded checks, and two
large entry pilots. No restricted-moment or factoring algorithm is promoted.

Let \(L=2^s\), \(d=L-1\), and let \(R\) be F314's interpolation matrix
for \(g=\left[\begin{smallmatrix}\alpha&\beta\\\gamma&\delta\end{smallmatrix}\right]\),
where \(\alpha,\delta\) and
\(\Delta=\alpha\delta-\beta\gamma\) are odd and \(\gamma\) is even. Put
\[
 B(i,j)=\alpha i+\beta-(\gamma i+\delta)j,
 \qquad p_i=(-1)^{d-i}i!(d-i)!.
\]
Exact Lagrange cancellation gives
\[
 R_{ij}R^{-1}_{ji}=(-\Delta)^{-d}
 \frac{\prod_{r\ne j}B(i,r)\prod_{r\ne i}B(r,j)}{p_ip_j}. \tag{1}
\]
If \(B(i,j)=0\), the apparent pole is a graph match and the value is exactly
one; every other entry in that row and column is zero. Other zero factors
also give zero, so (1) requires no undefined division.

For a nonmatching pair,
\[
 v_2(R_{ij}R^{-1}_{ji})\geq2\bigl(s-v_2(B(i,j))\bigr). \tag{2}
\]
Thus at Hadamard power \(h\) and precision \(2^p\), only one residue class
of at most \(2^t\) columns can survive in each row, where
\(t=\min(s,\lfloor(p-1)/(2h)\rfloor)\). This is still a literal
\(|I|2^t\) entry bound.

Each individual value in (1) is nevertheless computable in polynomial bit
cost. Odd-step progressions are split by parity; even factors are divided by
two recursively, while valuations and odd parts are tracked separately.
Even-step odd progressions use truncated elementary symmetric functions,
with exact Newton divisions. This avoids an \(O(L)\)-bit factorial guard and
gives the conservative per-entry bound \(O(H^8)\) bit operations and
\(O(H^3)\) live space for \(H=s+p+\tau+1\).

The unresolved block aggregation is explicit. With \(M=2^m\),
\(L=M2^t\), and a base residue \(i_0<M\), define
\[
 D_0=\gamma i_0+\delta,\quad y_0=T(i_0)\bmod M,
 \quad E_0=\alpha-\gamma y_0,
 \quad q_0=\frac{\alpha i_0+\beta-D_0y_0}{M}.
\]
Then
\[
 T(i_0+Mu)=y_0+M\frac{q_0+E_0u}{D_0+\gamma Mu}, \tag{3}
\]
and, when \(m\geq t\), the high coordinate is the affine permutation
\[
 v=D_0^{-1}(q_0+E_0u)\pmod {2^t}. \tag{4}
\]
Its intercept \(D_0^{-1}q_0\), slope, and both inherited prefix endpoints
move with \(i_0\). Their histogram is not constructed. Already at \(t=1\),
the half-box count is exactly \(\#\{i_0<M:q_0(i_0)\text{ is even}\}\).

The exact next-bit transition loses one precision bit. A retained pair of
states for \(g=[[-3,7],[2,5]]\), \(M=8\), agrees modulo two but produces
different next \(q\) bits. This excludes only that one-bit state truncation;
it is not a lower bound for another aggregation.

The pilot passed 4,028 kernel checks and 5,208 block checks in 0.115 seconds
at 17,383,424 bytes peak RSS. Nonenumerative single-entry pilots completed
at \(L=2^{40},p=12\) and \(L=2^{80},p=20\). The remaining operation is a
uniform aggregate of \(q_0(i_0)\) with both endpoints, or an equivalent
direct contraction of (1).

Evidence:
experiments/F317_cut_cauchy/RESULT.md,
experiments/F317_cut_cauchy/pilot.py,
experiments/F317_cut_cauchy/pilot.json, and
experiments/F317_cut_cauchy/pilot.log.

### C277 -- Exact support is implemented locally, while proposal reweighting does not change first discovery

**Status:** F319 author-derived implementation, source comparison, and
censored finite trials. P244 separately promotes only the normal-cone theorem
and its probability conditional on exact SUPPORT.

F319 implements integer SUPPORT for
\(S_N=\{(x,y)>0:xy\geq N\}\) using the exact RAYCAST and NEXTPT operations of
Alcántara--Blanco--Criado--Santos. SEEK reaches a certified hull vertex near
an integer coordinate cutoff, and a binary search over \([1,N]\) uses
monotone adjacent-edge objective signs. The claimed bounds are
\(O(\log^3N)\) arithmetic operations and a conservative \(O(n^6)\)
schoolbook bit cost for \(O(n)\)-bit normals. This implementation and
source-based cost proof were not independently reconstructed or promoted.

The implementation passed 126 exact checks. Two nonenumerating calls at
\(N=10^{24}+39\) and \(10^{48}+151\) took 0.077 and 0.460 seconds. Combined
with P244 it gives an elementary \(O(n^7N^{1/3})\)-expected-bit Las Vegas
route, still exponential in the input length.

Every returned coordinate is gcd-screened before any state update. This can
accept a proper divisor even when \(xy\ne N\): for
\(N=101000303\), exact product-only factor-vertex mass is 0.00106, while
coordinate gcd acceptance is 0.00989. Restricting acceptance to exact
products would discard this verified one-sided gain.

For independent proposals from one fixed normal law, residual Metropolis or
rejection reweighting cannot change the first generated successful
candidate. Counting every rejected proposal leaves the same discovery time.
This identity does not cover state-dependent proposal distributions.

Three public adaptive normal rules retained a one-quarter global proposal
component and used residual-dependent local perturbations. No tested rule
improved the independent source on the small uncensored cases; larger trials
were often censored at 3,000 queries. Those capped means are not estimates of
uncapped expectations. The remaining operation is a different public normal
source with a proved all-input candidate-cost/success ratio.

Evidence:
experiments/F319_random_support_hull/RESULT.md,
experiments/F319_random_support_hull/support.py,
experiments/F319_random_support_hull/pilot.py,
experiments/F319_random_support_hull/pilot.json,
experiments/F319_random_support_hull/pilot.log, and
experiments/F319_random_support_hull/pilot.status.json.

### C278 -- Energy controls and a pair bank retain square-root least-factor work

**Status:** F320 author-derived exact identities and finite checks. The
decoder is existing P34/F162 arithmetic; no novelty, quasipolynomial bound,
or result promotion is claimed.

For odd \(N\), define the public nonnegative residual
\[
 h(k)=\gcd(k,N)-1-(N-1)\mathbf1_{k=0}.
\]
It vanishes on units and zero, and every positive observation is already a
verified factor. For uniform \(K\bmod N\),
\[
\begin{aligned}
 \mu&=\mathbb Eh(K)=\frac{S(N)-2N+1}{N},\\
 \mathbb Eh(K)^2&=\frac1N
 \sum_{\substack{1<d<N\\d\mid N}}(d-1)^2\varphi(N/d).
\end{aligned}
\]
For \(N=pq\), the exact relative variance is
\[
 \frac{\operatorname{Var}(h)}{\mu^2}
 =\frac{N(p+q-2)}{4(p-1)(q-1)}-1.
\]
Thus this exact control still needs \(\Theta(p+q)\) iid gcd probes for
constant relative RMS on large semiprimes. A cyclic block of \(B\) explicitly
probed residues has useful-hit probability at most
\(B(N-\varphi(N)-1)/N\). These are restrictions on the named estimators,
not on implicit or correlated sources.

For a genuinely joint source, draw independent banks
\(A_1,\ldots,A_m,B_1,\ldots,B_m\) and test all differences \(A_i-B_j\).
Distinct differences are pairwise independent, even when one endpoint is
shared. If \(\alpha\) is the useful-gcd density and
\(Z\) counts useful differences, then
\[
 \mathbb EZ=m^2\alpha,\quad
 \operatorname{Var}(Z)=m^2\alpha(1-\alpha),\quad
 \Pr(Z>0)\geq\frac{m^2\alpha}{m^2\alpha+1-\alpha}. \tag{1}
\]
For least prime divisor \(p_{\min}\),
\(\alpha\geq1/(2p_{\min})\), so \(m\geq\sqrt{2p_{\min}}\) gives probability
at least one half.

P34's monic product/remainder tree evaluates one bank against the other.
F162's derivative substitution deletes exact equalities, and one scalar
product-tree descent localizes any full gcd. The work is soft-linear in
\(m\) times polynomial factors in \(n\). Doubling \(m\) and retrying gives
an actual verified Las Vegas algorithm with expected
\(\sqrt{p_{\min}}\,\operatorname{poly}(n)\) cost, which is \(N^{1/4}\)
scale on balanced inputs and not quasipolynomial.

The checker verified the energy, cyclic variance, and pair-bank second
moment on 11 inputs and exhausted all \(m=2\) banks for \(N=9,15\). It took
0.049 seconds. The remaining question is a compact correlated source with
more useful relations per stored value, together with a cheap decoder.

Evidence:
experiments/F320_approximate_energy_sampler/REPORT.md,
experiments/F320_approximate_energy_sampler/STATUS.md,
experiments/F320_approximate_energy_sampler/check.py,
experiments/F320_approximate_energy_sampler/output.json, and
experiments/F320_approximate_energy_sampler/run.log.

### C279 -- Output-selected roots show finite cubic-stage behavior but lack a uniform hazard bound

**Status:** F321 exact public experiments, conditional field diagnostics,
and root-derived identities. P245 separately promotes the radical-shadow
reduction; no squarefree quasipolynomial success bound is established.

The public attempt starts with \(H_0(x)=x\). On each uniform probe it
evaluates the current straight-line program, gcd-screens
\(y=H(x)\), and, only when the gcd is one, appends the public output
\(a=y\) and updates
\[
 H_{\rm next}(x)=H(x)(H(x)-a)\pmod N.
\]
A proper gcd is verified and returned; a full gcd makes no update. With
public cap \(B\), one attempt uses at most \(B(B-1)/2\) modular
multiplications and \(B\) gcds.

For a field image law \(\mu\), zero mass \(\alpha\), nonzero energy
\(\beta=\sum_{x\ne0}\mu(x)^2\), and
\(C(a)=\sum_x\mu(x)\mu(a-x)\), the exact collision identity is
\[
 Q_{\rm next}=Q+C(a)-\mu(a/2)^2.
\]
The corresponding \(\beta\)-increment retains an additive-triple term,
the midpoint correction, and the removed cubic mass \(\mu(a)^3\). Formal
degree growth alone supplies no positive drift theorem.

For semiprime zero masses \(a,b\), a raw probe has
\[
 u=(1-a)(1-b),\quad z=ab,\quad f=a+b-2ab.
\]
After full-zero retries the factor hazard is
\(h=f/(1-z)\geq\max(a,b)\), but surviving histories are reweighted by the
product of prior no-factor probabilities. With \(K\) raw probes at one
stage, the exact advance, factor, and reset probabilities are respectively
\[
 \frac{u(1-z^K)}{1-z},\qquad
 \frac{f(1-z^K)}{1-z},\qquad z^K.
\]

A sufficient unproved cumulative-hazard contract is: on a forced-chain
event of probability \(\delta\), if
\(\sum_{j<T}h_j\geq\lambda\) and \(z_j\leq1-\epsilon\), then the capped
public success probability is at least
\[
 \delta(1-e^{-\lambda})-T(1-\epsilon)^K. \tag{1}
\]
The attempt cost is \(O(KT^2\operatorname{poly}(n))\). No such uniform
squarefree contract is proved. The field collision identity remains invalid
as stated over prime-power rings, but P245 shows that this protocol needs no
separate prime-power valuation analysis once a squarefree contract is known:
its full-input process pathwise dominates the radical shadow, and exact
perfect-power preprocessing handles the one-prime case.

The selected-fiber guard tests \(K\) fresh differences before accepting a
root. At a fixed field state its accepted local law is proportional to
\(\mu(a)(1-\mu(a))^K\). It suppresses heavy fibers conditionally, but can
make acceptance rare. Multiplying \(H\) and every selected root by public
units preserves all gcd classifications, including guard decisions; unit
normalization is therefore the same process, not a new sampler.

The first raw probe alone gives a weak Las Vegas wrapper on promised
composite \(N\): if \(p\) is the least prime divisor, success is at least
\(1/(2p)\). Independent capped retries have finite expected cost
\(O(pB^2\operatorname{poly}(n))\). The unresolved requirement is a much
stronger cost/success ratio, not almost-sure termination.

Public finite data gave 128/128 initial and 256/256 larger adaptive
successes. On six preselected balanced scale inputs, descriptive log slopes
were 0.325342 for gcd stages and 0.654607 for modular multiplications;
work-matched rho gave 0.502728. These are finite fits only. Work-matched rho
also succeeded 256/256 and used fewer multiplications but more gcds in every
row. Guard \(K=2\) succeeded 64/64; guard \(K=8\) succeeded 52/64 with 12
censors. No global-equality rejection occurred, so the guard did not
validate beneficial overshoot.

The conditional field process reached whole-field zero by 29--139 updates
for \(p\leq4099\), but it samples by current image multiplicity conditioned
on nonzero output. It is not the law of surviving public runs without the
missing survival weighting. The original scaling-summary run failed its
six-case label assertion and is retained; the corrected run and its source
completed separately.

Evidence:
experiments/F321_adaptive_root_basins/REPORT.md,
experiments/F321_adaptive_root_basins/ANALYSIS.md,
experiments/F321_adaptive_root_basins/ROOT_NOTES.md,
experiments/F321_adaptive_root_basins/RADICAL_SHADOW.md,
experiments/F321_adaptive_root_basins/SHADOW_STATEMENT_ONLY.md,
experiments/F321_adaptive_root_basins/SHADOW_RECONSTRUCTION.md,
experiments/F321_adaptive_root_basins/SOURCE_LEADS.md,
experiments/F321_adaptive_root_basins/SCALE_REPORT.md,
experiments/F321_adaptive_root_basins/FIBER_GUARD_REPORT.md,
experiments/F321_adaptive_root_basins/RHO_WORK_REPORT.md,
experiments/F321_adaptive_root_basins/SHA256SUMS.txt,
experiments/F321_adaptive_root_basins/SCALE_SHA256SUMS.txt, and
experiments/F321_adaptive_root_basins/SUPPLEMENTAL_MANIFEST.md.
