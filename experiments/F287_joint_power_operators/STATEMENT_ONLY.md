# F287 statement-only reconstruction input

Please prove or refute the following exact claims independently. Do not
read REPORT.md or pilot.py before completing the reconstruction. No
asymptotic factoring success theorem is claimed.

Let N be odd and ell an odd prime divisor of N. Work on E=M_3(F_ell)
with pairing tr(XY). Define L_M(H)=sum_{i=0}^{N-1} M^i H M^{N-1-i},
ad_M(H)=MH-HM, C_M=Cent(M), and U_M=im ad_M.
Declared dependency: if M has squarefree characteristic polynomial and
distinct eigenvalues remain distinct under N-th powers, then
ker L_M=C_M, im L_M=U_M=C_M^perp. On this branch E=C_M direct-sum U_M.
Let P_M be projection onto U_M along C_M.

1. For arbitrary two such matrices of dimension d, the rank of L_M L_T
equals dim U_T minus dim(U_T intersect C_M). It is the same as the
rank of ad_M ad_T and of P_M P_T. If three maps have rank r and both
adjacent products have rank r, the triple product has rank r.

2. Let B be diagonal with distinct entries, V the off-diagonal matrices,
and C_A intersect V=span(K) with K nonzero. Assume A and B satisfy the
declared dependency's hypotheses. Then both adjacent derivative products
have rank 5. The rank of L_A L_B L_A is 4 if
tr(K ((L_B|V)^(-1)(K)))=0, and 5 otherwise.

3. Fix A=[[0,1,1],[1,0,1],[1,2,0]] and B=diag(0,1,t).
Assume ell!=13, A has collision-free N-th powers, and t(t-1)(t^N-1)
is nonzero in F_ell. Put u=t^(N-1) and
F=t u^2+3(t-1)u-1. Then both individual derivative ranks are 6,
both adjacent ranks are 5, and the triple rank is 4 exactly when F=0,
otherwise 5. In the same setting P_A P_B P_A always has rank 5 and
ad_A ad_B ad_A always has rank 4.

4. At N=77, t=3, the preceding hypotheses hold at ell=7 and 11.
The derivative triple ranks are respectively 5 and 4; u=25 and F=22
modulo 77. The scalar gcd test can therefore return 11 although the
individual and adjacent ranks synchronize.

5. For any odd N, computing u and gcd(F,N) has polynomial bit cost in
log N, independent of whether the matrix interpretation hypotheses hold.
It returns only verified divisors when a proper gcd occurs. If u=1
modulo an odd prime ell and t!=1 modulo ell, then F!=0 modulo ell.
Thus the unit-screened F test cannot split a Carmichael number. No
uniform success probability is asserted.
