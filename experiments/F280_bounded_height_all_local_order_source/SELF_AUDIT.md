# F280 author self-audit

## Status

This is the author's own audit. It is not a hostile audit, an independent
statement-only reconstruction, an outside-family review, or a computational
experiment.

## Primary-source checks

1. The Harvey--Hittmeir citation is arXiv:2601.11131v2, dated 5 June 2026.
   Theorem 1.1 is on PDF pages 3--4. Lemmas 2.1--2.3 are on pages 5--7.
   Algorithm 3.1 and its proof are on pages 7--11.

2. The exact Harvey--Hittmeir time bound contains one factor \(\log N\)
   and one factor \(\log D\). It is the revised v2 bound. The packet does
   not substitute the older \(\log^2N\) bound.

3. The Nir citation is arXiv:2605.09592v1, dated 10 May 2026. Theorem 1.1
   is on PDF page 2. Proposition 1.2 and its proof are on pages 3--5.
   Algorithm 1 and its proof are on pages 5--8.

4. Nir Proposition 1.2 scans through \(D^2+D\). Its stated cost is
   \(O(D^{5/2+o(1)}\operatorname{polylog}N)\). No stronger bound is
   attributed to it.

5. Nir Theorem 1.1 requires
   \(D>\exp\sqrt{2\log N\log\log N}\). The packet does not treat this as a
   numerical-QP threshold.

## Local-scan checks

6. A saturated gcd \(g_e=N\) would give
   \(\operatorname{ord}_N(a)\leq e\leq D\). It is impossible after either
   source returns global order greater than \(D\).

7. If one rational-prime local order is at most \(D\), its exact order is
   one of the scanned exponents. The corresponding gcd is not one. Thus all
   gcds equal to one prove the all-local predicate.

8. The proof does not assume that \(N\) is squarefree. A partial
   prime-power gcd is a proper factor. The certified orders in the theorem
   are orders modulo rational primes.

9. The postprocessor uses successive powers. It performs \(D\) modular
   multiplications and \(D\) gcds. The packet does not preserve the
   \(D^{1/2+o(1)}\) Harvey--Hittmeir time after local certification.

10. The Nir bound dominates the added linear scan under the stated
    arithmetic convention. The Harvey--Hittmeir all-local bound displays
    both terms instead of hiding the scan.

11. The certificate transcript has length \(D\). Calling it explicit does
    not call it succinct.

## Height and QP checks

12. Nir's high-order output is one of the ordinary integers it scans, so
    \(a\leq D^2+D\). The HH theorem can return an lcm-combined residue and
    has no theorem-wide \(D^{O(1)}\) height bound.

13. For every fixed numerical-QP \(D(n)\), both total algorithms and the
    Nir height bound remain numerical QP. The admissibility inequalities
    hold eventually because numerical QP is \(2^{o(n)}\).

14. At \(D=N^\delta\), the HH source cost is
    \(N^{\delta/2+o(1)}\), but the explicit local scan is
    \(N^{\delta+o(1)}\). Neither is stated as a lower bound.

## Common-capacity checks

15. The local-order gcd screens are applied only after an exact global
    order \(m\) has been found and factored. Passing them proves the same
    exact \(m\) in every rational-prime component.

16. Therefore every accepted \(m\), and their lcm \(M\), divides every
    \(p-1\). For \(N=pq\), this gives \(M\mid d\mid N-1\).

17. The packet does not call common capacity useless. A sufficiently large
    exact common order is a valid terminal input. The smooth-prefix branch
    also uses it in a direct progression scan.

18. The saturation comparison uses \((N-1)^n\), not bare \(N-1\).
    Equation (36) proves that this power contains the full local primary
    multiplicity for every prime already supported on \(N-1\).

## Counterexample and word checks

19. For \(N=77\), \(\operatorname{ord}_7(2)=3\),
    \(\operatorname{ord}_{11}(2)=10\), and
    \(\operatorname{ord}_{77}(2)=30\). With \(D=10\), the global predicate
    holds but locality, synchronization, and roughness fail.

20. In the same example, the P205 coprime residuals are \(3\) and \(5\).
    The bare word \(W=a=2\) absorbs neither.

21. The example refutes only automatic use of the returned base as the
    residual-absorbing word. The packet does not claim that every function
    of the source transcript fails.

22. The primary source interface contains no transfer map to a carry,
    quotient, determinant, or P205 word. Calling the direct composition
    ill-typed is not an impossibility theorem.

## Lane and evidence checks

23. P139 already contains the HH plus local-scan order property. F280's new
    source feature is Nir's bounded ordinary height.

24. Large order does not imply P161 roughness. It also supplies none of the
    support, recursion, evaluator, cluster, or orientation objects required
    by P162--P170 and P187.

25. The bounded base is biased and lies outside P212's declared
    fresh-uniform grammar. This does not contradict P212 and supplies no
    marker-hit probability.

26. An HH/Nir synchronized \(M\) adds no support beyond the saturated
    F259/F260 baseline. A high-order base has no proved transfer into their
    integer-word grammars.

27. No source code, generator, executable, benchmark, dataset, local
    research computation, remote computation, or durable-ledger edit was
    created.

28. The packet is ready only for a fresh hostile audit and an independent
    statement-only reconstruction. It is not promoted.

