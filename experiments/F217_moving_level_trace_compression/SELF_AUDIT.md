# F217 self-audit

## Verdict

Self-audit passes for the frozen proof-only candidate. The exact
identities, conditional decoders, and named-model state counts are proved
under their stated premises. No missing coefficient evaluator is promoted
to an algorithm. No general lower bound is claimed.

## Setup, coprimality, and range audit

1. The scope is restricted to distinct balanced odd semiprimes
   \(N=pq\equiv3\pmod4\), with \(p<q<2p\).
2. From \(2K=pq-1\), reduction modulo either hidden prime gives
   \(2K\equiv-1\). Thus \((p,K)=(q,K)=1\).
3. Hence every divisor of \(N\) is a unit modulo \(K\), and
   \(q\equiv p^{-1}\pmod K\).
4. The inequalities

   \[
   2(K-q)=q(p-2)-1>0
   \]

   and \(p<q\) prove \(p,q<K\) on every allowed input, including
   \(N=15\).
5. The stronger range \(p+q<K\) has exactly one exception. If \(p=3\),
   balance forces \(q=5\). If \(p\ge5\), then

   \[
   2(K-p-q)=(p-2)(q-2)-5\ge10.
   \]

   No other small case is omitted.
6. \(N=15\) satisfies the branch congruence and is explicitly handled by
   trial division by three. The residue decoder is not falsely applied to
   it.
7. \(N\equiv3\pmod4\) makes \(K\) odd. The semiprime lower bound
   \(N\ge15\) gives \(K>1\).

## Trace-decoder premise audit

1. The theorem assumes a certified cyclic isomorphism in both directions.
   It does not infer a generator, invariant-factor decomposition, inverse
   coordinate map, or discrete logarithm from
   \(\operatorname{factor}(K)\).
2. The theorem separately assumes succinct coordinate-character
   encodings and a certified divisor-coefficient evaluator. Ordinary
   evaluation of \(\chi(a)\) at a known residue is not confused with
   evaluation of \(\sum_{d\mid N}\chi(d)\).
3. The complete divisor expansion is exactly

   \[
   D_N(\chi)=2+\chi(p)+\chi(p)^{-1}.
   \]

   It uses \(\chi(N)=1\), which is valid because \(N\equiv1\pmod K\).
4. One coordinate trace determines \(a_i\) only modulo the involution
   \(a_i\mapsto-a_i\). The proof does not claim more.
5. The cosine separation formula is a product of two sine factors. If
   the two coordinates are not inverse-equivalent, both factors are
   nonzero and the gap is at least \(16/m_i^2\).
6. Binary search on the monotone half-interval uses \(O(\log m_i)\)
   comparisons. It does not enumerate a group of numeric size \(m_i\).
7. An active anchor is required only when at least two sign choices exist.
   A cross trace distinguishes the two relative alignments by a gap at
   least \(16/(m_{i_0}m_i)\).
8. Self-inverse coordinates have no sign to align. If all coordinates are
   self-inverse, no anchor or cross query is needed.
9. There are \(r\) coordinate queries and at most \(r-1\) cross queries.
   Since \(2^r\le|G|<2^n\), the bound
   \(2r-1\le2n-1\) is valid.
10. Every trace gap is larger than \(2^{4-2n}\). The requested
    \(2^{-4n-20}\) absolute precision is more than sufficient after
    charging candidate-value precision and interval comparisons.
11. The supplied forward coordinate map reconstructs exactly two global
    inverse residues. The proof uses \(p,q<K\) to identify them with the
    integer factors and verifies their product.
12. The theorem removes exponential Fourier-table output and decoding as
    obstacles. It does not remove the coefficient-evaluation obstacle.

## Ring-valued target audit

1. The tautological map \(G\to(\mathbb Z/K\mathbb Z)^\times\) is a
   group homomorphism, so its linear extension is a ring map from
   \(\mathbb Z[G]\).
2. The group-algebra coefficient is

   \[
   2[1]+[p]+[p^{-1}],
   \]

   and its specialization is \(\sigma_1(N)\bmod K\).
3. This construction uses a ring-valued character, not a classical
   complex scalar Dirichlet character. It directly addresses the concern
   that generic ring operations can carry more information than scalar
   reciprocity.
4. The full group-algebra vector has \(|G|\) coordinates and is not
   claimed to be small. Only the requested specialization is one
   \(O(n)\)-bit residue.
5. The target is still a divisor sum with an unknown additive term. No
   algorithm for it is hidden in the definition of the ring map.

## Eisenstein normalization and congruence audit

1. The chosen weight is exactly

   \[
   k=\varphi(K)+2,
   \]

   as stated. It is not \(\varphi(K)+1\), and no Carmichael-exponent
   substitution is used.
2. Since \(K>1\) is odd, \(\varphi(K)\) is even and \(k\ge4\) is an
   allowed level-one holomorphic Eisenstein weight.
3. The normalization

   \[
   \mathcal G_k=-\frac{B_k}{2k}
   +\sum_{m\ge1}\sigma_{k-1}(m)q^m
   \]

   makes the positive-index coefficient exactly
   \(\sigma_{k-1}(m)\). It is
   \(-B_k/(2k)\) times the constant-one normalization \(E_k\).
4. The Bernoulli constant can have a denominator. The proof never reduces
   that constant modulo \(K\); only the integral positive-index
   coefficient is reduced.
5. For every \(d\mid N\), coprimality with \(K\) permits Euler's theorem:

   \[
   d^{k-1}=d^{\varphi(K)+1}\equiv d\pmod K.
   \]

6. Factorization of \(K\) computes \(\varphi(K)\) with polynomial-bit
   work. It does not evaluate the coefficient at index \(N\).
7. The elementary prime-power product proves
   \(\varphi(K)\ge\sqrt K\) for odd \(K\). Thus the numeric weight is
   exponential in \(n\), although its binary encoding is \(O(n)\).
8. The unrestricted coefficient has \(\Theta(kn)\) bits, while the
   requested residue has \(O(n)\) bits. These output notions are kept
   separate.
9. The exponential state assertion applies to standard dense
   weight-space and symmetric-power methods. It is not a lower bound
   against direct modular computation from a binary weight.

## Prime-level eta quotient audit

1. Prime \(K=r\) in the semiprime setup satisfies \(r\ge7\). The
   problematic primes \(2,3\) do not occur.
2. The eta powers cancel exactly:

   \[
   \eta(\tau)^r/\eta(r\tau)=P(q)^r/P(q^r).
   \]

3. The eta exponents \(r_1=r,r_r=-1\) give weight
   \((r-1)/2\).
4. Both transformation congruences are checked:

   \[
   r-r=0,\qquad r^2-1\equiv0\pmod{24}.
   \]

5. Holomorphy is not inferred from the congruences alone. The
   \(q\)-expansion has order zero at infinity, and the Fricke transform is
   proportional to
   \(\eta(r\tau)^r/\eta(\tau)\), with positive leading exponent
   \((r^2-1)/24\). Prime level has no other cusps.
6. The modularity claim is only on \(\Gamma_0(r)\), with the explicit
   quadratic character

   \[
   \chi_r(d)=
   \left(\frac{(-1)^{(r-1)/2}r}{d}\right).
   \]

   No trivial-character assertion is made.
7. The binomial congruence is coefficientwise modulo \(r^2\). Cross terms
   in the infinite product vanish modulo \(r^2\), and every fixed
   coefficient involves finitely many factors.
8. For \(r\nmid m\), each divisor \(a\mid m\) produces one residue
   \(j\equiv m/a\pmod r\). Summing \(j^{-1}\) gives
   \(m^{-1}\sigma_1(m)\).
9. The congruence first proves that \([q^m]F_r\) is divisible by \(r\).
   Its residue modulo \(r^2\) therefore determines the quotient modulo
   \(r\); no illegal modular division by \(r\) is used.
10. At \(m=N=2r+1\), both conditions \(r\nmid N\) and
    \(N^{-1}\equiv1\pmod r\) hold.
11. The logarithmic-derivative sign and chain-rule factor are exact:

    \[
    -r^{-1}q\,d\log F_r/dq=L(q)-L(q^r).
    \]

12. Standard \(q\)-series truncation to index \(N\) and standard dense
    moving-level or moving-weight state are exponential. A compressed
    random-access eta coefficient algorithm remains open.

## Twisted Ramanujan audit

1. The identity is stated first for \(\Re(s)>0\), where
   \(|c_m(n)|\le\sigma_1(n)\) proves absolute convergence.
2. Expanding the Ramanujan sum and setting \(m=ek\) gives the factor

   \[
   \sum_k\chi(k)\mu(k)k^{-s-1}=1/L(s+1,\chi)
   \]

   in its absolutely convergent half-plane. The normalization and
   \(L\)-factor are correct.
3. Subtraction of \(n=1\) uses \(c_m(1)=\mu(m)\).
4. For \(m<p\), \((m,N)=1\), so every such factor-sensitive difference
   is exactly zero.
5. At \(m=p\),

   \[
   c_p(N)=p-1,\qquad c_p(N)-\mu(p)=p.
   \]

   Also \(\chi(p)\ne0\) because \((p,K)=1\).
6. The first sensitive summand is therefore exactly
   \(\chi(p)p^{-s}\), not merely asymptotically located near \(p\).
7. The \(s=0\) statement for a nonprincipal character is only an Abel
   limit or analytic-continuation statement. Ordinary boundary
   convergence is not asserted. The principal-character pole is
   explicitly excluded from that statement.
8. The direct-term threshold does not rule out compressed summation,
   cancellation identities, or an unrelated coefficient evaluator.

## Named-model and representation audit

1. The direct Hecke correspondence has \(\sigma_1(N)\) standard
   upper-triangular representatives. This is a materialization count, not
   a lower bound for every Hecke algorithm.
2. The equality \(\langle N\rangle=\langle1\rangle\) concerns the
   diamond operator only. It is not substituted for \(T_N\).
3. The Manin-symbol count and symmetric-power dimension refer to standard
   dense presentations. A compressed quotient or oracle presentation is
   outside the claim.
4. A representation of the abelian quotient \(G\) satisfies the exact
   matrix divisor identity and decomposes into characters over a
   splitting field. This does not cover genuinely nonabelian
   representations that do not factor through \(G\).
5. The equality \((Km,N)=(m,N)\) is used only for explicit channels whose
   factor sensitivity enters through that gcd. It is not generalized to
   all Kloosterman, spectral, or trace-formula data.

## Recursive-cost audit

1. F217 does not repeat the false claim that every useful recursive child
   needs fixed-ratio contraction.
2. A single one-bit-shrinking chain has at most \(n\) nodes, so

   \[
   T(n)\le T(n-1)+\operatorname{QP}(n)
   \]

   remains QP.
3. The need for a contraction or another aggregate bound concerns
   branching recursion with many surviving children.
4. The packet grants \(\operatorname{factor}(K)\). It neither constructs
   that factorization nor treats it as the source of the missing character
   evaluator.

## Evidence and scope audit

1. No mathematical computation, finite search, random sampling, remote
   run, or numerical fit is used.
2. No public web source is needed for the proofs. The packet uses standard
   identities and targeted local predecessor retrieval only.
3. No durable registry, proved ledger, failed ledger, progress ledger,
   statement ledger, inspiration file, or process-lessons file is edited.
4. The remaining evaluator may use integer-specific order, positivity,
   size, carries, characteristic effects, or a nonabelian extension.
   F217 does not reduce the problem to generic ring operations as an
   impossibility claim.

## Required fresh reviews

1. Reconstruct the coordinate gap and sign-alignment proof from the
   statement alone.
2. Check that the certified cyclic-decomposition premise cannot be read as
   a consequence of \(\operatorname{factor}(K)\).
3. Recheck the exact \(p+q<K\) exception and the least-residue decoder.
4. Verify the Eisenstein normalization and every exponent modulo \(K\).
5. Re-derive the eta transformation at cusp zero and the coefficient
   congruence modulo \(r^2\).
6. Re-derive the twisted Ramanujan identity in its absolute-convergence
   half-plane and reject any stronger \(s=0\) convergence reading.
7. Reject all interpretations as an unconditional factoring algorithm or
   a general lower bound against compressed coefficient evaluation.
