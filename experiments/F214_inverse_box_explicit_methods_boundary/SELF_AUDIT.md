# F214 self-audit

## Status discipline

1. The packet is labeled frozen, self-audited, and proof-only.
2. It has not passed a fresh hostile audit or a strict statement-only
   reconstruction.
3. It does not claim a numerical-QP inverse-box algorithm.
4. It does not claim a lower bound for the inverse-box problem, integer
   factoring, arithmetic circuits, arbitrary lattices, arbitrary
   continued-fraction algorithms, implicit CRT, implicit MCSS, or compressed
   harmonic analysis.
5. Every negative conclusion is restricted to a named explicit
   representation or to failure of a published sufficient theorem range.

## Assumptions and quantifiers

6. The exact collapse assumes a balanced semiprime
   \(N=pq\) with distinct odd primes and \(p<q<2p\).
7. The theorem does not extend the uniqueness conclusion to arbitrary
   composites, prime powers, or unbalanced semiprimes.
8. The full factorization of \(K=(N-1)/2\) is granted. No hidden
   factorization of \(N\) is used.
9. The full-\(K\) collapse itself does not use the factorization of \(K\);
   it states what any proposed algorithm must locate after that grant.
10. The notation “representative in \(Q\)” is explicitly noncanonical.
11. The arithmetic-progression terminal separately assumes
    \(1<m<N\), \(\gcd(m,N)=1\), and a list containing the true residue.

## Full-\(K\) collapse

12. Balancedness gives the strict inclusions
    \(p\in(\sqrt{N/2},\sqrt N)\) and
    \(q\in(\sqrt N,\sqrt{2N})\).
13. For every point in the continuous box,
    \(D=XY-N\) lies strictly between
    \(-(1-1/\sqrt2)N\) and \((\sqrt2-1)N\).
14. Both absolute endpoints are below \(K=(N-1)/2\) for the relevant
    \(N\geq15\). The proof records stronger safe thresholds.
15. Since \(K\mid D\), the strict interval \((-K,K)\) forces \(D=0\).
16. Semiprimality and the ordering around \(\sqrt N\) then force
    \((X,Y)=(p,q)\).
17. The argument verifies \(\gcd(N,K)=1\), so the congruence and inverse
    formulations are equivalent.
18. Oddness and the endpoint product test are not needed for this collapse.

## Singleton and recursion checks

19. Two odd representatives in the same class modulo \(m\) differ by a
    multiple of \(\operatorname{lcm}(2,m)\), including when \(m\) is even.
20. Strictly exceeding each interval diameter therefore makes each
    progression a singleton.
21. The endpoint predicate on two singletons is exactly \(XY=N\).
22. The singleton theorem does not assert that a live branch can be found
    efficiently.
23. \(K<2^{n-1}\), so only the \(K\)-factorization is on a possible
    one-bit decrement spine.
24. \(E<2\sqrt N+1\), so \(E\) and comparable auxiliary children have
    \(n/2+O(1)\) bits.
25. The recurrence has one \(T(n-1)\) term. It does not contain two
    independent near-size children.
26. The P183 consequence is conditional on a uniform numerical-QP
    selector. The packet does not construct that selector.
27. The Gao--Feng--Hu--Pan call is made only after a true factor residue is
    present in a numerical-QP-size list. Exact division verifies output.

## Scan and CRT cardinalities

28. Odd-integer density contributes the factor \(1/2\) in both interval
    counts.
29. The proof of \(\varphi(r)^2\geq r/2\) is prime-power local. The only
    factor below one is a single \(2^1\) component.
30. The paired-CRT lower bound assumes all local unit assignments are
    explicitly split and materialized in two lists.
31. Since the list-size product is \(\varphi(K)\), one list has at least
    \(\sqrt{\varphi(K)}\) elements. No time lower bound is inferred for an
    implicit data structure.

## Sum-fiber bound

32. A fiber of \(u+u^{-1}\) is exactly the root set of
    \(z^2-sz+1\) modulo \(K\).
33. For odd \(\ell^a\), completing the square is bijective because two is
    a unit.
34. If the discriminant has valuation at least \(a\), there are
    \(\ell^{\lfloor a/2\rfloor}\) square roots. If its valuation is
    \(2h<a\), there are at most \(2\ell^h\). Odd valuation gives no root.
35. At \(2^a\), a nonempty sum residue is even. Writing \(s=2h\) completes
    the square by translation, without dividing by two modulo \(2^a\).
36. An odd unit has at most four square roots modulo \(2^b\). Accounting
    for valuation and lifts gives the safe local bound
    \(4\sqrt{2^a}\).
37. CRT multiplies local fiber sizes. The frozen global constant
    \(4\,2^{\omega(K_{\rm odd})}\sqrt K\) is deliberately loose when
    \(K\) is odd.
38. The finite image lower bound (12) follows by partitioning all
    \(\varphi(K)\) units into fibers.
39. The asymptotic \(\varphi(K)=K^{1-o(1)}\) is attributed to the standard
    Rosser--Schoenfeld lower estimate, not to average order.
40. The estimate \(2^{\omega(K)}=K^{o(1)}\) is derived uniformly from
    \(K\geq(\omega(K)+1)!\), not assumed from typical behavior.
41. The main finite claim remains (12). The little-\(o\) statements are
    only consequences as \(K\to\infty\).
42. The MCSS list conclusion assumes every local sum-image choice is
    explicitly materialized in one of two half lists. CRT makes the product
    of their sizes exactly the global image size.

## Continued fractions, lattices, and Fourier scope

43. The determinant identity is reversible:
    \(XY-2K=1\) if and only if \(XY=N\).
44. It includes the trivial divisor completions. The balanced box selects
    the nontrivial pair, which is exactly the factor-selection task.
45. No claim is made that all continued-fraction algorithms require the
    direct public approximation absent here.
46. The affine polynomial
    \(f(a,c)=Bc-Ba-ac-E\) is equivalent to \(UV-N\) and is irreducible.
47. On the full box, \(A,C=\Theta(\sqrt N)\),
    \(W=\Theta(N)\), and \(AC=\Theta(W)\).
48. The packet states only that the published direct bivariate Coppersmith
    sufficient range \(AC<W^{2/3}\) does not apply. It does not turn
    nonapplicability into an impossibility theorem.
49. The exact Fourier support proof assumes \(K\) odd and \(L<K\).
50. The geometric sum has \(\gcd(K,L)-1\) zero nonzero-frequency
    coefficients, so its support is \(K-\gcd(K,L)+1\).
51. The Fourier conclusion applies only to termwise materialization. It
    leaves compressed exact Kloosterman summation open.

## Literature and evidence checks

52. Hittmeir is used to identify the explicit CRT-to-MCSS formulation and
    the scope of its rigorous and heuristic algorithms, not as a lower
    bound.
53. Cilleruelo--Garaev is used only to distinguish distribution bounds from
    an exact localization algorithm.
54. Coppersmith and Coron--Kirichenko--Tibouchi are used for the direct
    bivariate sufficient range.
55. Aono--Agrawal--Satoh--Watanabe is cited only as a warning that named
    lattice-optimality results have construction-specific scope.
56. No mathematical computation, finite search, random sampling, local
    experiment, or remote experiment was run. Hashing freezes text only.
57. No durable registry, proved ledger, failed ledger, progress ledger,
    statement ledger, process ledger, or inspiration file was edited.

## Highest-risk points for a fresh hostile audit

1. Reconstruct both strict \(|XY-N|<K\) inequalities and check the endpoint
   conventions.
2. Reprove the \(2^a\) square-root count and every lift factor in the fiber
   bound.
3. Check that the Rosser--Schoenfeld consequence is uniform and that the
   elementary \(\omega(K)\) inversion justifies the stated little-\(o\).
4. Confirm that the CRT-MCSS statement is read only as an explicit
   half-list cardinality bound.
5. Verify the exact scaled-height convention and theorem range in the
   corrected bivariate Coppersmith source.
6. Reject any reading of the packet as a lower bound against an implicit
   exact counter, an arbitrary lattice, or a new factoring method.
