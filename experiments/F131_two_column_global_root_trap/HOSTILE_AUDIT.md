# F131 fresh hostile re-audit — PASS

The corrected candidate passed a fresh hostile audit. No remaining defect
was found.

The audit independently checked the following claims.

1. For canonical endpoints, two exact values with square product have one
   common squarefree kernel. The bounds (0<a,b<N) are strict for every odd
   composite, including nonsquarefree inputs.
2. The joint root is (ba^{-1}\bmod N). It is (+1) exactly when the two
   exact values are equal, and it is (-1) exactly when (a+b=N).
3. If (a+b=N), the endpoint bounds force (s<4). Thus only the
   squarefree kernels (1,2,3) can give a global root for distinct values.
4. Every product, inverse, sign gcd, and root identity in the (N=9407) and
   (N=139127) certificates was recomputed.
5. The four resultant bounds are valid without a squarefree hypothesis. The
   arithmetic progression fixes (23^2\mid N) and keeps (N) coprime to
   every resultant constant, so all four endpoint gcds are one.

As an extra finite hostile check, the auditor scanned every odd composite
(N\le501). It found 816 distinct-value common-kernel pairs, including
nonsquarefree inputs, and no mismatch in the root classification or the
(s<4) boundary.

Verdict: **PASS**. This is a two-column classification and an auxiliary
counterexample. It is not a null for the complete retained source.

