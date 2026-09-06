# Canonical half-square counts as a signed multiplicative convolution

**Family:** route:F31

**Status:** exploratory root derivation and planned exact coefficient pilot.
No fast single-coefficient evaluator or novelty claim.

For M=2^k, k>=2, let epsilon(u) be +1 for the canonical odd representative
u<M/2 and -1 otherwise. The half-square count is

    C_M(N) = #{0<u,v<M/2 : u,v odd, uv=N mod M}.

Since epsilon(-u)=-epsilon(u), write every unit uniquely as sigma*5^j,
where sigma in {+1,-1} and 0<=j<T=2^(k-2). Put a_j=epsilon(5^j mod M),
and P_k(z)=sum_j a_j*z^j. If N=sigma*5^t modulo M, then

    C_M(N) = M/8 + (sigma/2)*[z^t](P_k(z)^2 mod(z^T-1)).

This is an exact position-sensitive transform, unlike F290's complete
objective histogram. It is not yet a computational saving: P_k has T terms.
For k>=3 the known half-period unit gives a_(j+T/2)=-a_j.

Two concrete questions for the pilot are whether the single coefficient
has a useful precision recurrence, and whether the canonical high-bit word
has further exact factors or a short recurrence beyond its half-period sign.
The pilot computes exact integer convolutions, not rounded floating FFTs.
It also tests a specific 2-adic continuity guess on the half-square count;
a counterexample will be recorded with its exact scope.

Nearest records inspected: P56 concerns linear consistency of Teichmuller
carry cocycles at the input modulus, and P184 concerns a particular signed
divisor selector and named reciprocity transforms. This object instead uses
the full canonical half-square weight at a known dyadic auxiliary modulus.
Neither old result supplies its coefficient evaluator or excludes nonlinear
or precision-dependent computation.

Resource plan: one Sage process, 30-second source alarm, about 10 seconds and
at most 600 MB including Sage startup; exact polynomials through k=18.
At 02:44 on the 16 GB host, load was 2.45/2.24/2.13, memory available72%,
no swap I/O. The process snapshot showed suggestd on one core and no active
numerical search. No remote run is needed for this pilot.
