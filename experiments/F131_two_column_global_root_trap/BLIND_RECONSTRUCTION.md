# F131 proof-blind reconstruction — PASS

The verifier read only the corrected statement and independently
reconstructed every claim.

For two values with square product, prime-valuation parity gives the unique
representation

\[
P_1=sa^2,qquad P_2=sb^2,qquad R=sab
\]

with squarefree (s). Since (P_i\equiv1\pmod N), one has

\[
R-P_1=sa(b-a),qquad R+P_1=sa(a+b).
\]

The factor (sa) is a unit. Canonical endpoint bounds give (0<a,b<N).
Therefore (R\equiv1) exactly when (a=b), and (R\equiv-1) exactly when
(a+b=N). Distinct values exclude the first case. If (a+b=N), then
(a,b<N/\sqrt s) forces (s<4).

The verifier recomputed every product, inverse, screen gcd, square root, and
factorization in the (N=9407) certificate. It also reconstructed the full
parametric construction. The parity and congruence conditions make every
endpoint integral and canonical. The four cleared endpoint signs reduce to
linear functions of (t), whose resultant constants are
(119,17,4559,5233). The arithmetic progression keeps (N) coprime to all
four constants while forcing (23^2\mid N). Hence all four endpoint gcds
are one for infinitely many odd nonsquarefree composites. The first member
is (139127=23^2\cdot263).

Verdict: **PASS**. The result classifies the root label of a two-column
dependency. It does not decide whether the complete retained source closes.

