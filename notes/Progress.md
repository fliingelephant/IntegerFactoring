# Research Progress

This is working state for nontrivial intermediate statements and the current synthesis. Every statement must list precise assumptions, proof or certificate, literal status label, and exact remaining gap. Only verifier-backed results may be promoted to `PROVED.md`.

## Current synthesis

The source material has been read in full. Ten approach families have been opened, primarily from materially different mechanisms in `notes/Inspirations.md`; promoted narrow results and exact open gaps are tracked below and in the registry. `notes/Zhihu.md` supplies background and motivation only.

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

**Status:** candidate from the mandatory follow-up F04 kill test; hostile audit and proof-blind reconstruction pending.

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

The candidate proof identifies \(D_j\) with the principal coefficient of the \(j\)-th subresultant and inducts through the Euclidean remainder chain, including the positive-gcd and top-index cases. This convention-sensitive lemma requires hostile verification.

**Finite obstruction.** On

\[
N=20000000499999937
=100000007\cdot199999991,\qquad r=2953,
\]

for every standard shift \(1\le a\le2942\), the globally formed error has degree 2952 and unit coefficients, and both local Euclidean chains are exactly

\[
2953,2952,\ldots,1,0.
\]

The lemma therefore makes all \(2942\cdot2953=8{,}687{,}726\) canonical PSCs nonzero in each field, so every global PSC is a unit. R08 completed the entire standard range under a 900-second timeout; exact full PSC residues at shifts 1 and 2942 and R10's artifact audit cross-check the shortcut.

**Exact remaining gap.** If verified, this refutes universal localization only for the fixed canonical PSCs in the standard minimal-\(r\), standard-shift AKS scan. It does not cover arbitrary Sylvester minors, other elimination transcripts, nonstandard moduli/shifts, or other group-algebra elements, and finite exhaustion supplies no top-level factoring theorem.
