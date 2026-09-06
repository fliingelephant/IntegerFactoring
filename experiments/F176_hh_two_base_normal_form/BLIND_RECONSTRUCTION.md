# F176 V3 blind reconstruction

## Integrity and verdict

- Source read: `STATEMENT.md` only.
- Frozen statement SHA256: `c7c4c9963c078dc1ba4d68a86a81fa4cd9e46626ab6fa9d8645779b92d6b4b1f`.
- Verdict: **PASS**.
- Counterexample found: none.

The verdict uses the standard operational meaning of *factor-first divisor stripping*: every stripping gcd is classified as (1), (N), or a proper divisor, and a proper divisor is returned immediately. That meaning is necessary; silently discarding a proper gcd would invalidate the theorem.

## Reconstruction

### 1. Size bounds and fixed caps

From (n=\lceil\log_2(N+1)\rceil), oddness gives

\[
2^{n-1}<N<2^n.
\]

For any fixed cap schedule (B=2^{(\log n)^{O(1)}}), one has (\log B=o(n)), hence (B<N-1) for all sufficiently large (N). The finitely many exceptions can be absorbed into one absolute trial-division threshold. The assumptions (B\ge n) and (C\ge n) are numerical and do not depend on the hidden factors.

### 2. Absolute screen, including prime powers

Write (r_j=\operatorname{ord}_{R_j}(2)). If (\sigma(r_j)\le B), every primary divisor (\ell^{v_\ell(r_j)}) occurs in (\Lambda_B), so (r_j\mid\Lambda_B). Thus (R_j\mid 2^{\Lambda_B}-1). Consequently:

- (1<A<N) is a verified proper factor, even when it cuts through a prime power;
- (A=N) is a common annihilator case;
- (A=1) implies (r_j\nmid\Lambda_B), hence (\sigma(r_j)>B), for every (j).

No squarefree assumption is used. A partial (p)-adic gcd is progress, not a failure of the classification.

For stripping, maintain a factored common annihilator (E). For each prime (q\mid E), test

\[
D=\gcd(2^{E/q}-1,N).
\]

If (D=N), replace (E) by (E/q) and repeat. If (1<D<N), return the factor. If (D=1), the (q)-part cannot be removed from any local order. In a no-factor run, this proves equality of every prime valuation, so all local orders equal the final (E=m), whose factorization is retained.

This stripping also proves (\gcd(m,N)=1). Otherwise take (p\mid m,N) and the component (p^a\parallel N). Since (\operatorname{ord}_p(2)\mid p-1), it divides (m/p), while (\operatorname{ord}_{p^a}(2)=m\nmid m/p). The relevant gcd is therefore divisible by (p) but not by (p^a), so it is proper. That contradicts a no-factor return. This is the required factor-first guarantee for Outcome B.

### 3. Every absolute common return is progress

If stripping returns (m>n), then ((2,m)) has exact order (m) in every (R_j), its factorization is known, and the preceding lemma gives (\gcd(m,N)=1). This includes the entire range (n<m\le B); Outcome B does not require (m>B).

Now suppose (m\le n). Since (N\mid 2^m-1), the size bound excludes (m<n), so (m=n). If (N) were a proper divisor of (2^n-1), its odd cofactor would be at least (3), giving (N\le(2^n-1)/3<2^{n-1}), impossible. Hence (N=2^n-1).

If (n) is composite and (\ell\mid n) is prime, then (2^{n/\ell}-1) is a nontrivial proper divisor of (N). If (n) is prime, the composite-input promise excludes (n=2), so (n) is odd. In each component, (2) has odd order (n); therefore ((-2)^n=-1), and (-2) has exact order (2n). Its factorization is known. Also (\gcd(2n,N)=1), either by the stripping lemma and oddness of (N), or directly from (N=2^n-1\equiv1\pmod n). Thus ((-2,2n)) is Outcome B.

### 4. Relative first return against \(\langle-1\rangle\)

For an odd prime power, the only square roots of (1) are (\pm1). Hence

\[
R_j\mid 2^{2e}-1
\quad\Longleftrightarrow\quad
2^e\in\langle-1\rangle
\quad\Longleftrightarrow\quad
e_j\mid e.
\]

Suppose the first nontrivial scan result is (G_e=N). Then every (e_j\mid e). If some (e_j<e), the earlier value (G_{e_j}) would have been nontrivial: either proper or (N). Both contradict first return. Therefore every (e_j=e).

The factored number (2e) annihilates (2) in every component. Factor-first stripping either factors (N) or returns one exact common ordinary order (m), with (\gcd(m,N)=1). For an odd prime power,

\[
e=\begin{cases}
m/2,&m\text{ even},\\
m,&m\text{ odd},
\end{cases}
\]

because the cyclic group \(\langle2\rangle\) contains (-1) exactly when (m) is even. Thus (L=\operatorname{lcm}(2,m)=2e). If (m) is even, (h=2) has order (L=m). If (m) is odd, (h=-2) has order (L=2m). Since the absolute screen already proved (\sigma(m)>B), one has (L\ge m>B\ge n). Finally, (N) is odd and (\gcd(m,N)=1), so (\gcd(L,N)=1). This reconstructs the exact, factored Outcome B state.

### 5. Outcome C is componentwise

If every (G_e=1) for (1\le e\le C), no (e_j\le C): otherwise (R_j\mid G_{e_j}). Combined with (A=1), the public transcript certifies, for every hidden component,

\[
\sigma(r_j)>B,
\qquad
e_j>C.
\]

Since quotient order never exceeds ordinary order, (r_j>C) also follows. The surviving state is exactly the already public common state ((-1,2)) with block (2). No assertion that this branch is impossible has been smuggled in.

### 6. Bit cost

A sieve through (B) gives the prime-power factorization of (\Lambda_B). The crude bound

\[
\log \Lambda_B\le\sum_{k\le B}\log k=O(B\log B)
\]

is sufficient. Construction, modular exponentiation by this exponent, and at most (O(\log\Lambda_B)) stripping tests have QP bit cost. The relative scan has (C) modular powers and gcds. Trial division of (e\le C), stripping from (2e), and encoding the result remain QP. Testing or trial-factoring the exponent (n) in the Mersenne branch costs polynomial time in the original input length (n). Products and polynomially many repetitions of fixed QP bounds are still QP. The algorithm is uniform and deterministic once the fixed cap schedules are fixed.

### 7. Full recursion count

On every factor result, recurse on the two proper factors after deterministic primality testing. If a complete factor tree has (t) prime leaves, counted with multiplicity, then (2^t\le N<2^n), so (t<n). A full binary tree has (2t-1<2n) nodes. Repeated prime factors are already counted in (t). Every child has at most (n) bits, so fewer than (2n) QP calls plus polynomial primality tests preserve the QP bound. A state or hard-block result terminates that branch; the theorem does not claim that all branches factor.

## Hostile conclusion

All advertised branches are exhaustive. Prime-power leakage becomes a proper gcd. Every no-factor exact order is automatically coprime to (N). The dangerous interval (n<m\le B) is correctly classified as Outcome B. The relative scan proves exact common quotient order only because it stops at the first nontrivial gcd. The small common-return branch is forced to the Mersenne case. The fixed-cap, finite-threshold, bit-cost, and recursion claims all follow with fixed hidden QP constants. Outcome C remains genuine missing progress, exactly as stated.

Report SHA256 (computed after replacing the 64 hexadecimal digits in this field by 64 zeroes): `37b834bd1fddffc25657a67ae809752edb559d689a9036fbb27f3f4f31da6df4`
