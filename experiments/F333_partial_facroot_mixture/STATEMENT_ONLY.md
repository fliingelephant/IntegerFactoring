# A two-source reduction for a partial FacRoot procedure

**Family:** route:F31

Status: statement for independent reconstruction. No candidate proof is
included in this document.

Let N be odd with at least two distinct prime divisors, with arbitrary positive
exponents. Let U be its unit group, J={a in U: Jacobi(a,N)=+1}, and S={r^2:r
in U}. A single public randomized procedure A receives only N,a and independent
coins. It may return a verified proper divisor of N, a verified square root of
a, or failure. The same procedure and coin law are used in both modes below;
the mode and any hidden root are not passed to A. Invalid outputs are treated
as failures, with verification cost charged.

## Bounded-call claim

Fix a deterministic bit-operation cap B for each call of A, including output
verification. On uniform a in J let f_J and r_J be the probabilities of a
verified divisor and a verified root, respectively, under a fixed priority
that makes these outcomes disjoint. Set delta_J=f_J+r_J.

Consider the following independent attempt:

1. Choose one of the two modes with probability 1/2 each.
2. In J mode, sample a uniformly in J and call capped A. Accept a verified
   divisor; a returned square root ends this attempt with failure.
3. In S mode, sample a private uniform r in U and set a=r^2. Call the same
   capped A with only N,a. Accept a verified divisor. For a verified root y,
   compute gcd(y-r,N) and accept it exactly when it is proper.

The proposed factor-success lower bound is delta_J/2. Neither a lower bound
on success for every a, nor a cost bound for an uncapped call on S, is assumed.
The conditional parameter distribution on J given membership in S is uniform
on S. The sampling routines must be implemented without factoring N.

For an actual implementation, draw uniform nonzero residues from 1,...,N-1.
Return any proper generation gcd as an immediate factor. In J mode otherwise
reject only Jacobi-negative units; in S mode use the first unit draw as r.
Include all draws and generation successes in the attempt. The claims are that
this implementation preserves the same lower bound and that generation has
expected polynomial bit and fair-bit cost.

## Expected-cost transfer

Now remove the per-call cap. For each fixed N, let tau_J(N)>=1 be the finite
expected bit cost of A, including verification, and let delta_J(N)>0 be its
valid-output probability on uniform a in J. Suppose an explicit computable
integer-valued quasipolynomial envelope Q(n)>=1 is known, where n is the input
bit length, such that

    tau_J(N)/delta_J(N) <= Q(n)

uniformly for all such N. The constants in Q are independent of N and its
factors. No separate bound on the conditional mean cost over S is assumed.

Cap both modes at B=ceil(2*Q(n)) bit operations and use independent retries.
The proposed bounds are valid-output probability at least delta_J(N)/2 for
the capped J call, actual factor success at least delta_J(N)/4 per attempt,
and expected restart cost O(Q(n)^2+poly(n)*Q(n)). Thus an all-input classical
Las Vegas factoring algorithm of expected quasipolynomial bit complexity
follows after primality, even-number and perfect-power preprocessing and
recursive verified splitting. The preprocessing and recursion costs must be
accounted for; a uniform bound over different N is not replaced by input
averaging.

## Uncapped dovetail alternative

The same expected-cost hypothesis also permits an algorithm that does not
know Q, tau_J or delta_J. Run two independent retry engines: one repeatedly
uses uncapped J-mode calls and accepts only factors; the other repeatedly
uses uncapped S-mode calls and the hidden-root decoder. Interleave one bit
operation of each engine and stop when either returns a verified factor.
This is ordinary classical dovetailing of two fixed machines.

If g(n) is a uniform polynomial upper bound on expected generation and outer
verification cost per attempt, the proposed total expected bit cost is at most
6*(g(n)+tau_J(N))/delta_J(N), up to constant machine-simulation overhead.
Either retry engine may never succeed by itself. No worst-case call bound or
separate conditional-square mean-cost bound is assumed. If tau_J/delta_J has
the stated quasipolynomial bound, this alternative also solves the all-input
target after the same preprocessing and recursion.

Permitted dependencies: elementary finite abelian groups, CRT, polynomial-bit
Jacobi/gcd/modular arithmetic and integer roots/primality testing, and P02's
conditional hidden-root success probability 1-2^(1-s) for s distinct odd prime
divisors. This is a conditional reduction, not a construction of an A satisfying
the stated quasipolynomial contract, and not an external novelty claim.
