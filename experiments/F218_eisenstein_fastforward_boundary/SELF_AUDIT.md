# F218 self-audit

## Verdict

The proof-only claims pass this self-audit.  F218 is a named-model boundary
and an exact auxiliary counterexample.  It does not produce the required
coefficient evaluator or a top-level factoring algorithm.

## Theorem A

1. `K` is odd and greater than one in the declared branch, so
   `lambda(K)` and every permitted `Lambda` are even.  The weight
   `Lambda+2` is valid and at least four.
2. `lambda(ell^e)=phi(ell^e)` for odd prime powers and divides
   `lambda(K)`.
3. The inequality `phi(ell^e)>=e` makes every divisor containing `ell`
   vanish modulo `ell^e` after exponentiation.  This valuation step is not
   replaced by Euler's theorem on a nonunit.
4. Divisors not containing `ell` are units modulo `ell^e`, so Carmichael
   reduction is legal.
5. The depleted divisor identity is exact over the integers.  It is not
   merely a coefficient congruence.
6. The rational constant of `H_ell` is never reduced modulo `ell^e`.
   Positive coefficients are integral.
7. At `m=N`, `(N,K)=1` is proved from `N=2K+1`; CRT then gives the full
   residue modulo `K`.

## Theorem B

1. The binomial expansion is coefficientwise modulo `r^2` and every fixed
   coefficient receives finitely many product contributions.
2. Cross terms contain `r^2` and vanish.
3. At an index divisible by `r`, the contributing cofactor, not the
   divisor, must be an `r`-adic unit.  Writing `m=r^v u` accounts for this
   exactly.
4. The displayed division by `r` occurs only after the congruence proves
   coefficient divisibility.
5. At `N=2r+1`, `N^(-1)=1 mod r`; no hidden inverse is used.

## Theorem C

1. Addition and multiplication of big-Witt vectors are coordinatewise on
   ghosts, so they do not convolve indices.
2. Frobenius multiplies and Verschiebung conditionally divides an inward
   dependency index.  Both preserve the prime-to-`K` rough part when their
   parameter is `K`-supported.
3. Fan-out, reuse, constants, and arbitrary circuit depth do not change
   the invariant.
4. The theorem does not allow an `N`-supported Frobenius to masquerade as
   evaluation.  `F_N` at coordinate one merely names the unknown target.
5. Ordinary `q`-series multiplication, Cartier operators, and nonlinear
   coefficient encodings are explicitly outside the model.

## Theorem D

1. The theta convention uses `q^(a^2)`, so its square has
   `R_2(1)=R_2(2)=4`.
2. `N=2r+1` has exactly three possible quotient exponents `0,r,2r` in the
   Frobenius product.
3. The odd-index Eisenstein coefficient uses only the `E_(2k)(tau)`
   degeneracy component.  Its coefficient follows from the stated cusp
   constant match.
4. Since `r-1` does not divide `r+1` for `r>3`, Kummer congruence is used
   in its regular case.  `B_(r+1)` has `r`-integral denominator.
5. Fermat reduction of `sigma_r(N)` is legal because `r` does not divide
   `N` or any divisor of `N`.
6. The witness `35=5*7` satisfies `5<7<10`, so it lies in the balanced
   branch.  The smaller branch input `r=7, N=15` has zero difference, so
   the stated minimality is exact.  Every residue in the final calculation
   is explicit.
7. The nonzero cusp coefficient refutes theta isolation only.  It is not a
   lower bound against a computable cusp projector.

## Theorem E

1. Dirichlet's theorem is used only in its standard form: a reduced residue
   class `1 mod rT` contains infinitely many primes.
2. `j_a` is integral because `ell=1 mod r`, and consecutive `j_a` have the
   same residue modulo `T` because `(ell-1)/r` is divisible by `T`.
3. The prime-power inputs `ell^a` are exact values of `rj_a+1`; no density
   or independence assumption is used.
4. Since `ell=1 mod r`, the divisor sum is `a+1 mod r`, so consecutive
   exponents always give different residues.
5. An affine finite-order recurrence is converted to a finite-state update
   by adjoining a constant coordinate.  Over a finite field its output is
   eventually periodic.
6. The theorem concerns a recurrence valid throughout the Cartier section.
   It does not refute a formula declared only at `j=2` on a sparse family
   of varying primes `r`.

## Computation and evidence

The mathematical claims above need no numerical experiment.  The separate
F218-D01 run is preregistered only to test bounded affine Cartier laws and
to extend the exact witness table.  Its failed first launch is preserved
under `failed_run_01`; it produced no mathematical output.

No durable registry, proved ledger, failed ledger, progress ledger,
statement ledger, inspiration file, or process-lessons file is edited by
this subagent.
