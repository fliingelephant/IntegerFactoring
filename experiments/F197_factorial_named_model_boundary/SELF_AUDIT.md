# F197 self-audit

## Promise and algebra

1. The promise is only a balanced product of two distinct odd primes.
2. The inequality \(B<2p\) is used to prove \(v_p(B!)=1\), not merely
   \(v_p(B!)\ge1\).
3. Oddness is needed in the proof that \(q=p+1\) is impossible. The
   power-of-two quotient identity itself uses only Euclidean division and
   \(0<R<N<2^n\).
4. Both \(B!\) and the interval numerator have gcd exactly \(p\), not just a
   nontrivial divisor.
5. Modulo \(N^2\), multiplication by \(B!\) is not injective on the whole
   ring. It is injective only after restricting inputs to \([0,N)\).

## Named-model limits

6. The \(u+\lceil B/u\rceil\) lower bound applies only when the dense block
   coefficient vector and every block value are explicitly materialized.
7. No arithmetic-circuit, straight-line-program, generic-ring, or general
   modular-product lower bound is claimed.
8. The BGS and Costa--Harvey complexities are upper bounds for published
   algorithms. Their exponential numerical value is not evidence that a
   different algorithm cannot be QP.
9. The arbitrary-ring BGS factorial bound and the sharper recurrence result
   have different invertibility hypotheses. The proof uses the safe
   arbitrary-ring square-root scale and does not silently erase those
   hypotheses.

## Lift, output, and quotient checks

10. Computing a residue modulo \(N^2\) includes its reduction modulo \(N\),
    which already exposes the factorial gcd.
11. Exact output size obstructs only materialization of the full integers.
    It says nothing about \(O(n)\)-bit residues.
12. The residue \(B!\bmod2^n\) is proved polynomial-time computable even in
    the small cases where it is nonzero.
13. The quotient-bit theorem is one-way sufficiency. F197 does not claim a
    QP reverse reduction from a known factor to \(Q\bmod2^n\).
14. The mixed modulus in (19) is \(N2^n\), not \(N^2\); the two lifts encode
    quotient digits in bases \(2^n\) and \(N\), respectively.

## Recursion and evidence

15. A one-child \(m\mapsto m-1\) recursion with QP node cost is explicitly
    accepted as QP. No fixed-ratio contraction premise is inserted.
16. The failure of the named factorial bounds to be QP occurs already at
    one root node and is not attributed to recursion branching.
17. No experimental computation, verifier output, or durable-ledger edit
    supports this packet.
