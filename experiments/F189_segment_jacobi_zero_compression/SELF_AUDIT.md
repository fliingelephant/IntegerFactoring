# F189 candidate self-audit

## Verdict

The proof packet is internally consistent as a proof-only conditional result
and a set of named-model boundaries. It does not contain the missing QP
segment-zero evaluator. Fresh hostile audit and statement-only reconstruction
are required before any promotion.

## Kill-first checks

1. **Repeated prime factors.** Equation (2) is valid for every odd \(N\).
   Even if a prime occurs to an even exponent in the Jacobi symbol, a
   numerator divisible by that prime gives a zero Legendre factor. The
   square is one exactly on units and zero exactly on nonunits.

2. **Gauss identity without coprimality.** Equation (5) does not invoke
   Eisenstein's lemma off the unit group. It follows from a direct rectangle
   count. The equality line has exactly \((g-1)/2\) points for odd
   \(g=\gcd(x,N)\).

3. **Parity and integrality.** For odd \(x,N,g\), both
   \((x-1)(N-1)/4\) and \((g-1)/2\) are integers. Multiplying (5) by two
   gives equation (8) with no half-integral remainder.

4. **Sign versus zero.** The parity \((-1)^{F(x,N)}\) is used only when
   \(x\) is a unit. Off the units it cannot represent zero. The proof keeps
   the full floor sums only to identify the missing gcd correction.

5. **Even segment members.** Since \(N\) is odd, removing powers of two
   preserves every gcd hit. For the stated range below \(2N\), there are
   only \(O(n)\) valuation strata. A literal zero integer is public and is
   treated separately.

6. **Weighted count versus root count.** \(G_N\) is not the number of
   nonunit positions. It weights a hit by \(\gcd(x,N)-1\). The only claimed
   equivalence is its zero test: \(G_N=0\) if and only if there is no hit.

7. **One-child recursion.** At each split, only the left child is queried.
   A nonzero left answer and a zero parent logically force the right child
   to be zero. The query count is \(O(\log L)\), not the size of a full
   binary tree.

8. **Improper global zero.** Binary isolation guarantees a proper factor
   only when the retained segment contains no multiple of \(N\). The source
   theorem identifies and subtracts the exact probability of this sole bad
   case; a run that reaches gcd \(N\) is restarted.

9. **Affine normalization.** The identity
   \(U+tV=V(a+t)\) is used only after \(V\) is certified a unit. Conditional
   on independent uniform units \(U,V\), the quotient \(a=UV^{-1}\) is
   uniform in the global unit group.

10. **Source root law.** Conditioning \(a\) to be a global unit excludes
    root position zero. Each local root is therefore uniform among
    \(1,\ldots,r-1\), and CRT makes the two roots independent. This gives
    \((T-1)/(r-1)\), not \(T/r\).

11. **Exact bad-case probability.** Because \(T<p,q\), each prime has at
    most one root position. The only way a zero singleton has gcd \(N\) is
    alignment of those positions. There are exactly \(T-1\) aligned unit
    classes out of \((p-1)(q-1)\).

12. **P34 scale.** The scale inequality in Proof Section 5 follows from the
    power-of-two definition of \(T\). The promise \(q<2p\) gives \(T<p\).
    The lower bound \(1/40\) uses only \(p\ge53\) and is weaker than the
    displayed exact probability.

13. **Arbitrary-\(N\) Fourier scope.** The period and recurrence order are
    \(\operatorname{rad}(N)\), not \(N\), when repeated factors occur. The
    full Fourier-support proof uses the fact that the radical is squarefree.

14. **Semiprime correction.** The order \(p+q-1\) applies only after
    specializing to squarefree \(N=pq\) and adding the publicly detectable
    spike \(\mathbf1_{N\mid x}\). No corresponding formula is claimed for
    arbitrary composites.

15. **DFA scope.** The exact \(\operatorname{rad}(N)\)-state theorem is for
    explicit deterministic finite automata reading binary values with
    leading zeros allowed. It is not a time lower bound for arithmetic
    algorithms with registers.

16. **Kummer scope.** The carry equivalence for a hidden prime \(r\) assumes
    \(L<r\), so \(L!\) is an \(r\)-adic unit and \(L\) has one base-\(r\)
    digit. No carry statement is extrapolated past that range.

17. **QP accounting.** A polynomial number of calls to a fixed
    quasipolynomial oracle remains quasipolynomial. The packet does not
    assume that \(\sqrt N\) calls, states, or Fourier modes are QP.

18. **No general lower bound.** The Fourier, recurrence, and automaton
    theorems exclude only their named explicit models. They do not exclude a
    determinant, nonlinear modular algorithm, implicit state, or new
    zero-only observable.

19. **Approximation threshold.** On \(p<q<2p\), one has
    \(p>\sqrt{N/2}\). Hence a nonzero weighted hit count is larger than
    \(\sqrt{N/2}-1\), while a zero count is exactly zero. The final
    half-gap threshold is conditional and does not assert an approximation
    algorithm.

20. **Relation to P34.** The affine two-seed pool reuses P34's numerical
    value of \(T\), not its independent Boolean source. The packet neither
    computes nor narrows the general evaluator for \(Q_K\).

## Required external checks

A hostile auditor should independently reconstruct the half-rectangle
identity, verify the exact conditioned-unit probability including the
aligned global zero, rederive both recurrence orders, and attack the
Myhill--Nerode state proof. A blind reconstruction should then recover the
conditional one-child algorithm without using 'PROOF.md'.

## Computation and ledgers

No mathematical computation was run. No durable proof or failure ledger was
edited by this candidate.
