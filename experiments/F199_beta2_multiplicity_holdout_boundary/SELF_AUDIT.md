# F199 self-audit

## Promise and imported facts

1. The promise is exactly the P175 balanced squarefree semiprime promise:
   \(N=pq\) with distinct odd primes \(p<q<2p\).
2. The terminal precision is exactly
   \(t=\lfloor(\log_2N)/4\rfloor-L(n)\), with one fixed
   \(L(n)=(\log n)^{O(1)}\) and \(t\ge2\).
3. F199 imports the integrality of \(h\), polynomial-time computability of
   \(z\), the identity \(h-z=p^{-1}\bmod2^t\), and the P175 terminal. It
   adds no new literature claim.
4. The expression \(z=N^{-1}(A-1)\bmod2^t\) is modular multiplication by
   an inverse. It does not assert \(N\mid A-1\) in \(\mathbb Z\).

## Smooth torsor

5. For every odd candidate \(u\), the definitions
   \(P=u^{-1},Q=Nu,H=z+u\) satisfy every displayed congruence. No hidden
   factor is used in this construction.
6. The converse uses \(PU=1\), so it covers exactly unit candidates and no
   zero-divisor branch is omitted.
7. The quotient-ring isomorphism is explicit. The Jacobian minor has unit
   determinant \(U\), so the smoothness claim is valid over
   \(\mathbb Z/2^t\mathbb Z\), not only over its residue field.
8. Smoothness proves only that the target is not a singular or
   higher-multiplicity point of the named congruence scheme. It does not
   prove that no factor-correlated polynomial can distinguish the target.

## Public recurrence

9. The recurrence for \(z_i\) is obtained by cancelling the odd unit \(N\)
   modulo \(2^t\). It never divides by \(i+1\).
9a. Pointwise computation of \(z_i\) runs the same power-of-two binomial
    routine used in P173 with modulus parameter \(n\), not \(t\). Thus the
    large upper index remains inside the cited range.
10. The two displayed first derivatives sum to \(N\), so one is odd at
    every edge. This includes both parities of \(i+1\).
11. At \(i=p-1\), the derivative in the next-state coordinate is \(p\), an
    odd unit. The transition is not silently assumed singular.
12. The one-spike difference uses the unavailable integral quotients
    \(H_i\). F199 does not claim that these labels are public or QP
    computable.
13. A QP list of public indices containing \(p-1\) would already factor by
    \(\gcd(i+1,N)\); no source theorem for such a list is assumed.

## Reed--Muller and Hasse boundaries

14. The Boolean cube has \(m=t-1\) free bits because the low bit of every
    reciprocal candidate is fixed to one.
15. The support bound is proved for the unique multilinear representative
    over \(\mathbb F_2\). It is not asserted for arbitrary integer-valued
    circuits or nonlinear feature embeddings.
16. The induction handles both \(J=0\) and \(J\ne0\). The singleton bound
    is sharp through the exact delta polynomial.
17. The feature-span statement follows from injectivity of evaluation on
    the complement. It is not a heuristic dimension count.
18. Hasse order below \(s\) includes the order-zero evaluation. The Taylor
    formula therefore really implies Hamming-ball vanishing.
19. The order-at-least-two singleton contradiction uses a neighbor of the
    target. It applies to multilinear Hasse features on the full candidate
    cube, not to an arbitrary sparse high-degree circuit representation.
20. The QP ball-volume statement is a union bound. It does not assume the
    balls are disjoint.
21. The univariate degree bound uses distinct field points and exact Hasse
    multiplicity. It does not apply after a noninjective scalar encoding.

## Explicit clouds and lift pairing

22. A QP list containing \(p^{-1}\bmod2^t\) is terminal only because the
    precision is the exact P175 precision. Every returned divisor is still
    verified by exact division.
23. The bounded-preimage extension applies only when those preimages can be
    publicly enumerated in QP total work. It does not cover aggregate cells
    with exponential preimages.
24. In the lift proof, \(j\ge1\) is needed for
    \(2^{2j}\equiv0\pmod {2^{j+1}}\).
25. The formulas for \(P_1,Q_1\) are congruences modulo \(2^{j+1}\), not
    unwrapped integer equalities.
26. The balance-range representatives exist because the intervals have
    length \(2^{j+1}\) and \(\sqrt N\) is nonintegral. Their residues are
    odd because the modulus is even.
27. Those representatives are not claimed prime and are not claimed to
    multiply to \(N\). The lemma closes only pruning by standalone size and
    balance inequalities.

## Surviving adaptive route and nonclaims

28. A prefix cell of codimension \(\ell\) has a degree-\(\ell\) indicator.
    Therefore the Reed--Muller result does not obstruct selecting one
    polylogarithmic block per stage.
29. A one-child chain with polynomially many QP stages is explicitly
    accepted as QP. No fixed-ratio contraction requirement is inserted.
30. F199 supplies no adaptive cell syndrome and proves no lower bound
    against one.
31. F199 proves no lower bound against nonlocal canonical-integer features,
    Euclidean quotient bits, aggregate interval statistics, nonlinear
    target-correlated embeddings, sparse high-degree circuits, or different
    factoring algorithms.
32. No experimental computation, randomized evidence, or durable-ledger
    edit supports this packet.
