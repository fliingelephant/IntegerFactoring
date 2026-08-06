# Research Progress

This is working state for nontrivial intermediate statements and the current synthesis. Every statement must list precise assumptions, proof or certificate, literal status label, and exact remaining gap. Only verifier-backed results may be promoted to `PROVED.md`.

## Current synthesis

The source material has been read in full. Twenty-five approach families have been opened, primarily from materially different mechanisms in `notes/Inspirations.md` with additional factor-trace, noncommutative, hidden-modulus metric, non-gcd tensor-contraction, joint-amortization, positive-sampling, and dissipative-dynamics routes; promoted narrow results and exact open gaps are tracked below and in the registry. The current frontier is a factor-free sampler for the quadratic-energy/zero-product law, a genuinely joint decoder using typical nonzero relation data, a fine manufactured metric hint, a useful class-group/isogeny orientation, or an exactly contractible positive factor-witness network beyond the proved local wiring boundaries. `notes/Zhihu.md` supplies background and motivation only.

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
