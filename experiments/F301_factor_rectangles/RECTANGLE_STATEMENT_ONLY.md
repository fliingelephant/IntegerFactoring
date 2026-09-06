# Statement-only reconstruction: a public rectangle interface for factoring

Read only this file for mathematical input. Do not read author derivations,
implementation, other records, or prior conversation. Reconstruct the exact
claim and its uniform bit cost. A failure to reconstruct is inconclusive.

For an input integer N>=2 with bit length n, consider the following oracle:

    Empty(N,M,[A,B],[C,D])

It correctly decides whether there exist integers x in[A,B], y in[C,D]
with xy=N modulo M. All endpoints lie in[1,M-1], and M is a power of two.
The oracle takes the succinct integer endpoints, not a list of points.
Suppose its uniform deterministic (or always-correct Las Vegas expected)
bit cost is at most T(n) when all input bit lengths are O(n), with a fixed
constant in this O(n). No factorization of N is given to the oracle.

Claim: an algorithm completely factors every N using O(n^2) oracle calls
on such inputs, plus polynomially many bit operations. It returns only
correct outputs and inherits almost-sure termination and the expected bound
O(n^2 T(n)+poly(n)) in the Las Vegas case. Thus a quasipolynomial T in n
would meet the all-input classical factoring target. No support optimizer,
prime-factor oracle, or external primality algorithm is needed for this
reduction.

Candidate public construction to reconstruct:

* First divide/check the fixed primes2,3,5,7,11,13. Equal prime inputs are
  handled as primes; proper divisors split the input.
* For a remaining integer N>=17, let M be the largest power of two at most
  N/8. Thus N/16<M<=N/8. When no boxes are generated, the proposed algorithm
  declares N prime.
* Set R=17/16 and L_j=16 R^j for j>=0 while L_j<=sqrt(N). Construct

      I_j=[max(17,ceil(L_j)), min(floor(sqrt(N)),floor(R L_j))],
      J_j=[max(1,ceil(N/(R L_j))), min(M-1,floor(N/L_j))].

  Omit empty intervals. Rational endpoints before rounding are represented
  exactly by integer numerators and denominators.
* Claim: there are O(n) such boxes, each with O(n)-bit integer/rational
  data. For every generated box, xy=N modM holds if and only if xy=N as
  integers. Every composite surviving the fixed trial division has a proper
  factor pair in at least one box.
* If every box is empty, declare N prime. Otherwise bisect the x interval
  of a nonempty box using further Empty queries on subrectangles, until it
  is a singleton. That x must be a proper divisor. Recurse to complete
  factorization, including multiplicities.

Verify all small, even, prime, prime-power, repeated-factor, unbalanced and
arbitrary composite cases, endpoint equalities, the x,y<M requirement, the
gap excluding N+/-M, count/size of boxes, adaptivity, and accumulated expected
bit cost. The oracle itself is deliberately NOT supplied or claimed here.
