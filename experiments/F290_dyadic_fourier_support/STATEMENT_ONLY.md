# F290 statement-only reconstruction input

Please independently prove or refute these exact claims. Do not read
REPORT.md or the retained Python sources before reconstruction.

Let M=2^k, N,a,b odd integers, and
Q_M(s)=#{u odd modulo M : au+bN/u=s modulo M}.
For K=1,...,k put m=floor(K/2), l=ceil(K/2),
U_K={odd u modulo2^l : au^2=bN modulo2^m}, and
c_K(u)=au+bN/u modulo2^K. The modulus1 condition at K=1 is vacuous.

1. The exact histogram formula is

    2Q_M(s)=1+sum_K 2^floor(K/2) sum_{u in U_K}
      (1_{s=c_K(u) mod2^K}-1_{s=c_K(u)+2^(K-1) mod2^K}).

Each U_K has at most8 elements, obtainable in polynomial bit complexity
in k. Consequently sums of Q_M(s) on intervals, and sums weighted by
T+1-s on L<=s<=T, have polynomial bit complexity in k and the bit lengths
of the input bounds and coefficients, without listing Fourier modes.

2. For M=2L with L even, u odd in[0,L), v=N/u modulo L in[0,L), and
c=(N-uv)/L modulo2, the two inverse-graph lifts modulo M are
(u,v+cL) and(u+L,v+(1-c)L).
For any weight W and W_ij=W(u+iL,v+jL), the full weighted count equals

    (1/2)sum_u [W_00+W_01+W_10+W_11
                +(-1)^c(W_00+W_11-W_01-W_10)].

3. For a=b=1,N=3 mod8 and k>=3, Q_M(s)=4 on s=4 mod8 and0 elsewhere.
At M=16 the inputs N=3 and11 have lower-half-square counts4 and0,
despite the identical histograms.
At M=1024, interval227<=x+y<=228, the positive cap xy>=N with
xy=N modulo M has points(101,127),(127,101) for N=12827 and no points
for N=12851. These have identical complete dyadic histograms at every
modulus, identical interval bounds, and modular interval count4.
Both moduli satisfy N/16<M<N/8 and228^2<4(N+M).
This claim only refutes determination by the histograms and bounds;
it does not refute computation from N and additional data.

4. For L=2^m,m>=2, choose the multiplicative character modulo2L with
psi(-1)=1 and psi(5)=exp(2pi i/2^(m-1)). Then psi(1+L)=-1 and,
whenever uv=N modulo L, (-1)^((N-uv)/L)=psi(u)psi(v)/psi(N).

5. Let M=2^(2m),m>=5,N=1 mod8. In the shifted phases
r(u+N/u)+8u for odd r, the stationary-root conditions modulo2^m are
u^2=Nr/(r+8). As r varies there are exactly2^(m-4) distinct right-hand
sides and2^(m-2) distinct stationary roots. This counts the size of a
particular root-list representation, not a general evaluation lower bound.

No support-oracle implementation or all-input factoring success theorem
is part of the claims.
