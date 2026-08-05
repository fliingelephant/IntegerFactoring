# Research Progress

This is working state for nontrivial intermediate statements and the current synthesis. Every statement must list precise assumptions, proof or certificate, literal status label, and exact remaining gap. Only verifier-backed results may be promoted to `PROVED.md`.

## Current synthesis

The source material has been read in full. Nine approach families have been opened, primarily from materially different mechanisms in `notes/Inspirations.md`; promoted narrow results and exact open gaps are tracked below and in the registry. `notes/Zhihu.md` supplies background and motivation only.

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

**Status:** candidate from the mandatory F09 kill test; hostile audit and proof-blind reconstruction pending.

**Claim.** X10 proves, for a precisely defined multiplicative scalar carrier class, that factor-swap invariance forces every local phase functional through \(u_p+u_q\); twists and \(+/-\) combining retain the anti-diagonal kernel. An exact cubic example shows a canceled global phase with neither local phase canceled. The fully Galois-symmetric odd-power residue-symbol product is trivial, while nontrivial symbols require a cyclotomic orientation.

**Exact remaining gap.** The carrier-class quantifiers, postselection claim, cyclotomic Galois product, and orientation formulation require hostile audit and proof-blind reconstruction. Even if verified, vector/ring-valued, factor-oriented, additive, and other higher-residue carriers remain open; no factoring-equivalence claim for one orientation is made.
