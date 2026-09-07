# F304 source leads: fast finite 2-adic summation

Scope: algorithms that can plausibly sum a succinct function over odd residues modulo 2^k, with explicit complexity and analytic or recurrence hypotheses. These sources do not give a generic polynomial-time summation theorem for arbitrary arithmetic circuits. Each requires extra structure that F304 would have to prove. This is a scoped dependency finding, not an impossibility or novelty claim.

## 1. Roblot: finite-precision Mahler integration against a bounded measure

Xavier-François Roblot, “Computing p-adic L-functions of totally real number fields,” *Mathematics of Computation* 84 (2015), 831–874, [author PDF](https://math.univ-lyon1.fr/~roblot/resources/zetap.pdf), [DOI](https://doi.org/10.1090/S0025-5718-2014-02889-5), [arXiv:1110.0246](https://arxiv.org/abs/1110.0246).

- Section 5.1 defines N_f(M) as the first Mahler index after which every coefficient f_n has |f_n|_p <= p^-M. Algorithm 5.1 obtains the first N Mahler coefficients from f(0),...,f(N-1) mod p^M by finite differences. Lemma 5.2 gives bit cost

      O(N C + N^2 M log p)

  when one value of f at precision p^M costs O(C).

- Lemma 5.8 assumes f: Z_p -> Z_p is continuous, mu is a **bounded** Z_p-valued measure, and N >= N_f(M). Given the first N Mahler coefficients of f and the Amice transform F_mu modulo (p^M,T^N), it computes integral f dmu mod p^M in O~(N M log p) bit operations. Lemma 5.25 gives the matching finite quadrature criterion: under its norm-at-most-one hypotheses, if

      F_mu(T) = sum_(a in A) c_a (1+T)^a  (mod T^N),

  then integral f dmu = sum_(a in A) c_a f(a) (mod p^M).

- Section 5.2 defines local analyticity of order h by restricted power-series expansions on each disk a + p^h Z_p, with norm M_h(f). Amice’s Theorem 5.9 states that this is equivalent to

      f_n / floor(n/p^h)! -> 0,
      |f_n|_p <= M_h(f) |floor(n/p^h)!|_p.

  A polynomial Mahler cutoff therefore needs a bound on both h and M_h(f). The factorial valuation makes the displayed generic cutoff scale like p^h (M + log_p M_h(f)); this is exponential in k if h grows with k.

**F304 dependency.** An unnormalised odd-residue sum can be represented by a finite counting measure, but the theorem still needs a polynomial cutoff and the truncated Amice transform at guarded precision. A normalized 2^(1-k) average has measure norm 2^(k-1), so the norm-at-most-one precision result cannot be used without accounting for the lost k-1 bits. A small Newton-selector circuit supplies neither bound by itself.

## 2. Caruso–Mezzarobba–Takayama–Vaccon: quasi-linear evaluation with a certified D-finite system

Xavier Caruso, Marc Mezzarobba, Nobuki Takayama, and Tristan Vaccon, “Fast evaluation of some p-adic transcendental functions,” [arXiv:2106.09315](https://arxiv.org/abs/2106.09315), especially Section 4 and Propositions 4.4, 4.5, and 4.7.

- Section 4 starts with an order-r linear differential equation

      a_r(t)y^(r) + ... + a_0(t)y = 0,

  where the a_i have degree at most d and exact coefficient height at most ell; it sets s = r+d. Equations (7)–(9) turn the coefficient sequence into a fixed-size polynomial-coefficient recurrence. Section 4.1 assumes a_r(0) != 0.

- Proposition 4.4 proves that balanced binary splitting computes an N-term partial sum at an argument of height at most H, at precision sigma = O~(N), in

      O~(s^omega N (ell + H + s))

  bit operations. The cost is quasi-linear in N, so a flat prefix of length 2^k remains exponential unless convergence or another reduction makes N polynomial in the requested precision.

- Proposition 4.5 supplies a convergence certificate. If the normalized equation coefficients f_i lie in the analytic algebra A_rho, then the solution lies in A_tilde-rho, where

      tilde-rho = R_exp min(rho, min_(0 <= i < r) ||f_i||_rho^(1/(i-r))),
      R_exp = p^(-1/(p-1)),

  with the stated Gauss-norm bound from the initial derivatives.

- Proposition 4.7 assumes the leading coefficient is invertible in A_rho, the fundamental matrix entries lie in A_rho with Gauss norm at most M, and the endpoint and coefficients satisfy the paper’s height bounds. Its digit-burst algorithm computes the fundamental matrix modulo pi^sigma in

      O~(s^omega sigma (ell + s))

  bit operations.

**F304 dependency.** F304 would have to derive a fixed or polynomial-size D-finite system for the selector/inverse summand and certify its denominators, radius, Gauss norm, and guarded precision. Succinct circuit evaluation does not itself provide that system.

## 3. Bostan–Gaudry–Schost: baby-step/giant-step for polynomial-coefficient recurrences

Alin Bostan, Pierrick Gaudry, and Éric Schost, “Linear Recurrences with Polynomial Coefficients and Application to Integer Factorization and Cartier–Manin Operator,” *SIAM Journal on Computing* 36(6) (2007), 1777–1806, [author PDF](https://cs.uwaterloo.ca/~eschost/publications/pollard.pdf), [DOI](https://doi.org/10.1137/S0097539704443793).

- The paper treats U_(i+1) = M(i+1) U_i over a commutative ring, with M(X) an n by n matrix whose entries have degree at most one. Theorem 14, with s = floor(log_4 N), assumes that 2,...,2^s+1 and the stated products D(1,2^t,2^t) are units, with their inverses supplied. It computes U_N in

      O(MM(n) sqrt(N) + n^2 M(sqrt(N)))

  ring operations and O(n^2 sqrt(N)) space. The paper also gives effective-ring bit bounds. A running sum can be placed in an augmented fixed-dimensional state; that sentence is an implementation observation, not another theorem from the paper.

- Over Z/2^P Z, Theorem 14’s unit hypothesis fails already at 2. The paper’s arbitrary-ring bounds retain essentially sqrt(N) dependence, or 2^(k/2) for N = 2^k.

**F304 dependency.** This route requires a fixed-size polynomial-coefficient recurrence and a treatment of nonunit denominators at p=2. A short circuit for the u-th term does not imply such a recurrence.

## Concrete bridge still required

One of the following must be established before these sources yield a polynomial-k whole-graph sum:

1. A locally analytic extension on only polynomially many residue disks, with coefficient or derivative bounds that make N_f(P) polynomial, plus a guarded truncated Amice transform for the odd-residue functional.
2. A fixed or polynomial-size D-finite or polynomial-recurrence representation with certified radii and denominators.
3. A structured-circuit summation theorem whose hypotheses hold for the repeated Newton idempotents.

Large formal degree alone neither supplies nor rules out these structures. No knowledge-base or repository file was modified.
