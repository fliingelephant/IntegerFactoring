# F126 hostile audit

**Verdict:** pass.

The audit independently checked the row combination, the sign, the
determinant scaling, cancellation, gcd equality, F123 specialization, and
quasipolynomial operation count.

Three implementation corrections are part of the frozen theorem:

1. Run rectangles before exact-value deduplication and retain \(P=1\)
   vertices.
2. Test prefactor components separately. A combined gcd can hide two proper
   factor hits.
3. Treat different integer presentations separately from this canonical
   residue theorem.

The auditor also mentioned an unregistered finite sweep. It is excluded from
the evidence and is not used for promotion. F126 is proof-only.
