# F287 third-cycle statement-only reconstruction input

Independently prove or refute the claims below. Do not read
DYNAMICS_FOLLOWUP.md or the new source scripts before reconstruction.

Let R_h(v)=v(h-v)/(hv-1). Over characteristic zero and h!=1,-1,
R_h is degree2, with fixed points0,1,infinity and multipliers
(-h,-h,2/(1-h)). The members Möbius-conjugate to z^2 or z^(-2) are
exactly h=0 and h=2. This assertion classifies conjugacy to those two
monomials only. At h=1 the map cancels to -v; at h=-1 to v.

In characteristic not2,3, choose distinct alpha,beta satisfying
x^2-x+1=0. For M(v)=(v-alpha)/(v-beta),
M(R_2(v))=M(v)^(-2). The equation t=R_2(t^N) consequently transforms
to M(t)=M(t^N)^(-2); it does not assert M(t^N)=M(t)^N.

For the matrix claim work over an odd field whose characteristic
divides N. Define L_T(H)=sum_{i=0}^{N-1}T^i H T^{N-1-i}.
Use the declared dependency that squarefree characteristic polynomial
and collision-free N-th-power eigenvalues imply
ker L_T=Cent(T), im L_T=Cent(T)^perp for pairing tr(XY).

Take A=[[0,1,1],[1,0,1],[1,2,0]], C=[[0,1,1],[1,0,1],[1,0,0]],
B=diag(0,1,t). Assume characteristic is not5 or13, A and C have
collision-free N-th-power eigenvalues, and t(t-1)(t^N-1)!=0.
Let u=t^(N-1), F_2=t u^2+2(t-1)u-1. Then all individual derivative
ranks are6, rank(L_A L_B)=rank(L_B L_C)=5, and
rank(L_A L_B L_C)=4 if F_2=0 and5 otherwise.

At N=187,t=5 the preceding hypotheses hold over F_11 and F_17;
the triple ranks are5 and4. Here u=60,F_2=153 modulo187.

R_2 commutes with both inversion and v ->1-v. Its associated six
Möbius orbit tests at an odd exponent reduce to three distinct bases
t,1-t,t/(t-1), up to inversion. Their N-th powers require only two
exponentiations: if a=t^N and b=(1-t)^N, the third is -a/b.
All divisions require units or a preceding gcd test.

For independent uniform CRT samples conditioned on a local screening
event at each field, record the three F_2 zero tests by a bit mask.
If c_p(m),c_q(m) are local mask counts and H_p,H_q total counts,
the probability that at least one of the three gcds splits is exactly
1-sum_m c_p(m)c_q(m)/(H_p H_q).

No asymptotic success bound or general classification of algebraic-group
constructions is part of these claims.
