# Statement-only reconstruction: mixed inverse moments modulo M squared

Read only this file for mathematical input. Do not read the author proof,
implementation, other research records, or inherited research history.
Reconstruct the claimed algorithm, not a different route.

Let k>=3, M=2^k, N>=1 be odd, and

    U_M={1,3,...,M-1}, v_N(u)=N*u^(-1) modM in[1,M-1],
    q_u=(u*v_N(u)-N)/M in Z,
    A_j=sum_(u in U_M)u^j,
    S_ab=sum_(u in U_M)u^a*v_N(u)^b,
    Q_j=sum_(u in U_M)u^j*q_u,
    Pi_M=product_(u in U_M)u.

For an integer D>=0, the claim is that every Q_j modulo M for0<=j<=D
and every S_ab modulo M^2 for0<=a,b<=D is deterministically computable
in bit complexity polynomial in k,D, and the ordinary binary length of N.
The cost is polynomial in the numerical degree D, not just logD. No factors
of N, inverse-graph enumeration, or numerical-length unit list is supplied.

A supporting claimed primitive is: Pi_M modulo2^P can be computed in
bit complexity polynomial in k and the numerical precision P>=1, without
enumerating M/2 units. Standard integer power-sum recurrences and Newton
identities may be derived and used, with exact division or precision guards.
No external algorithmic theorem is declared as a dependency.

The following identities are part of the exact claim to reconstruct.
As a formal rational function at T=0, put

    R(T)=Pi_M*product_(u in U_M)(T+u)
                      /product_(u in U_M)(N+T*u).

The denominator has odd constant term. Then

    R(T)=product_(u in U_M)(1+M*q_u/(N+T*u)),
    Q_j=(-1)^j N^(j+1) * ([T^j](R(T)-1)/M) modM.

Division by M means: compute the numerator coefficient modulo M^2,
prove it is divisible by M, divide an integer representative, then reduce
modulo M. It is not an inversion of M in a residue ring.

For a>=b>=1, j=a-b,

    S_ab=N^b*A_j+b*M*N^(b-1)*Q_j modM^2.

When b=0, S_a0=A_a; when a<b, interchange a,b by the inverse involution.
All products defining R must be truncated/evaluated in polynomial bit work;
explicitly multiplying its M/2 factors is not an algorithm for this claim.

Verify coefficients, the arbitrary full odd N (not necessarily N<M), all
degree-zero cases, formal-series division, nonunit Newton divisors, modular
precision, operand sizes, and uniform cost. The claim concerns only these
residues. It does not recover exact integer S_ab, ordinary complex Cauchy
resolvents, rectangle counts, or a factoring algorithm.
