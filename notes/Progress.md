# Research Progress

This is working state for nontrivial intermediate statements and the current synthesis. Every statement must list precise assumptions, proof or certificate, literal status label, and exact remaining gap. Only verifier-backed results may be promoted to `PROVED.md`.

## Current synthesis

The source material has been read in full. No mathematical approach has yet been selected or evaluated. `notes/Inspirations.md` is the primary seed portfolio; `notes/Zhihu.md` supplies background and motivation only.

## Working claims

### C00 — divisor-to-complete-factorization reduction

**Status:** promoted as P01 in `PROVED.md`.

**Assumptions.** There is a uniform classical Las Vegas procedure `Split(M)` which, on every composite integer \(M\) of bit length \(m\), returns a divisor \(d\) with \(1<d<M\), returns no incorrect value, terminates almost surely, and has expected bit cost at most a fixed polynomial \(Q(m)\). Use any fixed deterministic polynomial-time primality test with bit-cost polynomial \(A(m)\).

**Construction.** Maintain a stack initially containing \(N\). Pop \(M\). If the deterministic test says prime, append \(M\) to the leaf list. Otherwise call `Split(M)`, verify \(1<d<M\) and \(d\mid M\), and push \(d\) and \(M/d\). At the end, sort equal leaves and output their multiplicities.

**Proof.** Every split replaces \(M\) by two integers at least \(2\) whose product is \(M\), so the invariant that the product of the stack and finished leaves equals \(N\) is preserved. All finished leaves are certified prime. Thus termination produces exactly the complete prime factorization, including prime powers and repeated factors. If the final multiset has \(L\) prime leaves counted with multiplicity, then \(2^L\le N\), hence \(L\le \log_2N<n\). The binary split tree therefore has at most \(L-1<n\) internal nodes and at most \(2L-1<2n\) total nodes. This deterministic bound holds regardless of the random choices made by `Split`.

Every subproblem has bit length at most \(n\). By linearity of expectation, without any independence assumption, all split calls cost in expectation at most \((n-1)Q(n)\); all primality calls cost at most \((2n-1)A(n)\). Divisibility verification, exact division, stack storage, and sorting operate on fewer than \(2n\) integers of at most \(n\) bits and therefore cost at most \(C n^3\) under schoolbook arithmetic for a fixed implementation-dependent constant \(C\). Consequently

\[
\mathbb E[T(N)]\le (n-1)Q(n)+(2n-1)A(n)+Cn^3,
\]

a fixed polynomial independent of \(N\) and its factors. There are fewer than \(n\) randomized calls, each of which terminates almost surely, so all calls terminate almost surely; every returned divisor is checked, so every output is correct.

**Exact remaining gap.** This reduction itself still needs the mandated hostile audit and blind reconstruction. More importantly, no qualifying `Split` procedure has been proved.

### C01 — exact linear square-class sketches cannot generically compress

**Status:** candidate.

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

**Status:** candidate.

**Claim and certificate.** X02 in `FAILED.md` gives an explicit good-reduction curve over \(\mathbb Z/15\mathbb Z\) for which every affine point seed has identical local \(x\)-orbit collision threshold 4. Consequently all collision-discriminant gcds are trivial.

**Exact remaining gap.** The curve enumeration, duplication formula, denominator argument, CRT conclusion, and minimality claim require hostile audit, followed by blind reconstruction. The example closes only this standard candidate, not F02 as a family.

### C04 — unequal local polynomial-gcd degrees expose a factor

**Status:** candidate.

**Assumptions and claim.** Let \(N=pq\) for distinct primes, and let monic \(A,B\in(\mathbb Z/N\mathbb Z)[X]\) have degrees at most \(D\). If

\[
d_p=\deg\gcd(A\bmod p,B\bmod p)\ne
d_q=\deg\gcd(A\bmod q,B\bmod q),
\]

then a nontrivial factor of \(N\) is recoverable deterministically in \(\operatorname{poly}(D,\log N)\) bit operations.

**Proof.** Compute the principal subresultant coefficients \(s_j(A,B)\) division-free modulo \(N\). Over a field, \(s_0=\cdots=s_{d_r-1}=0\) and \(s_{d_r}\ne0\). If \(d_p<d_q\), then \(s_{d_p}\) is nonzero modulo \(p\) and zero modulo \(q\), so \(\gcd(s_{d_p},N)=q\). Sylvester/subresultant matrices have dimension \(O(D)\), and division-free determinant algorithms use polynomially many operations on \(O(\log N)\)-bit residues.

**Exact remaining gap.** Hostile audit and blind reconstruction are pending. More importantly, F03 has not supplied \(A,B\) with the required mismatch without circular access to the local characteristics.

### C05 — cycle-type mismatch is not a zero-divisor certificate

**Status:** candidate.

**Certificate and claim.** X03 records the exact \(N=15,f=X^2+1\) witness. It also claims that for uniformly random monic quadratics modulo an odd semiprime, conditional on local squarefreeness, the two split/irreducible bits are independent and fair, hence disagree with probability \(1/2\); their disagreement gives \((\Delta/N)=-1\) but no nonunit. The resulting Jacobi-minus-one promise is randomized-polynomial-time equivalent to semiprime factoring.

**Exact remaining gap.** Every algebraic identity, probability, and reduction direction requires hostile audit, then blind reconstruction. No richer Galois invariant has been ruled out.
