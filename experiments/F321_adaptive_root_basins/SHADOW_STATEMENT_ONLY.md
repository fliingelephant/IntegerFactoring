# Statement-only task: the radical shadow of adaptive root sampling

Let N be an odd integer with at least two distinct prime divisors. Define
R=rad(N), the product of those distinct primes. R is used for analysis only
and is not supplied to the algorithm. Fix an integer probe cap B>=1.

An attempt modulo an integer m starts with H(X)=X, represented by an empty
parameter list. Each probe draws an independent uniform X in Z/mZ and
evaluates Y=H(X) modulo m. If 1<gcd(Y,m)<m, it returns that verified divisor.
If gcd(Y,m)=1, append A=Y and update H(X) to H(X)(H(X)-A) modulo m.
If gcd(Y,m)=m, leave the parameter list unchanged. After B probes without
success return failure. All randomness is from exact uniform sampling.

Claim 1. There is a coupling between attempts modulo N and modulo R, using
the same cap B, such that success modulo R by any probe implies success
modulo N by that probe. Hence the capped success probability modulo N is
at least that modulo R. No factorization is used by either sampler's public
steps. In particular, the comparison includes products with unequal repeated
prime exponents; it is not restricted to perfect powers or balanced inputs.

Optional extension. The same comparison holds with any fixed integer guard
length K>=0: after obtaining a proposed unit A, make up to K further probes
of independent H(X)-A, counting every such evaluation against the total cap.
Return proper gcds, reject A without an update on a full-zero gcd, and append
A only after K unit guard outcomes. The same guard and cap are used in both
coupled attempts. A cap reached mid-guard returns failure.

Claim 2. Suppose nondecreasing public functions B(n),Q(n) are bounded by
fixed quasipolynomials and, for every odd squarefree composite R of binary
length n, the unguarded attempt with cap B(n) succeeds with probability at
least 1/Q(n). Then there is an all-input classical Las Vegas factoring
algorithm of expected quasipolynomial bit complexity. Use Claim 1, independent
attempts, exact divisor verification, and a complete recursion argument.
The actual algorithm must not compute rad(N). Explain why the input-length
change from R to N does not require an unstated promise, and include the
cost of evaluating the growing circuit and uniform sampling.

For Claim 2 only, the declared standard dependencies are deterministic
polynomial-bit primality testing and exact integer-root/perfect-power tests.
No such dependency is needed for Claim 1. A nontrivial perfect-power root
may itself be composite and must be recursively factored.

No success lower bound B,Q for this adaptive process is claimed here.
Claim 2 is conditional, not a completed factoring algorithm.
