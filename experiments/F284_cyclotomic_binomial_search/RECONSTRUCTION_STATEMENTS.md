# F284 — Central normalized q-binomial jets

For an integer b>=0 let G_b(t)=[2b choose b]_t be the Gaussian binomial
polynomial, with G_0(t)=1. In Q[[z]] define

    R_b(z)=G_b(exp(z))/binom(2b,b),  c_j(b)=[z^j] R_b(z).

Reconstruct or refute the following claims from these definitions.

1. c_0=1. For each j>=1, c_j(b) is the restriction to nonnegative integers
   of a polynomial P_j in Q[b] of exact degree 2j with leading coefficient
   1/(2^j j!). Every prime appearing in its coefficient denominators is at
   most j+1.
2. Given b and J in binary, the first J+1 coefficients can be computed with
   bit complexity polynomial in J+log(b+1), without materializing G_b or
   binom(2b,b). This is polynomial in the OUTPUT COUNT J, not log J.
3. If N=pq for distinct primes p,q>J+1 and b is uniform in {0,...,N-1},
   reduce P_j(b) modulo N by inverting its rational denominator. Then

       Pr[exists 1<=j<=J with 1<gcd(P_j(b),N)<N]
         <= J(J+1)(1/p+1/q).

   This concerns only these coefficient probes under uniform indices. It says
   nothing about deterministic b=floor(sqrt(N)), selected moment determinants,
   adaptive index choices, or arbitrary polynomial/rational combinations.

Allowed standard tools: the Gaussian-binomial product formula, formal power
series, elementary Bernoulli/Faulhaber identities, elementary bit arithmetic,
and the root bound for a nonzero polynomial over a finite field. No supplied
log-jet formula, candidate proof, or numerical output may be consulted.
