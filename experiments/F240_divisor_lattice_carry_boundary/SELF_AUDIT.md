# Self-audit of F240

## Verdict

**SELF-AUDITED PASS at the stated proof-only scope.**

This is not verifier-backed.  No hostile audit or proof-blind
reconstruction has run.  No computation was used.

## Algebra checks

1. **Carry sign.**  Expanding
   `(aB+x)(bB+y)=u^2(1+BH_B)` and substituting
   `xy=u^2+cB` gives

   \[
   u^2H_B=abB+ay+bx+c.
   \]

   Therefore

   \[
   u(aq+bp)=u^2H_B+abB-c.
   \]

   The minus sign on `c` in the trace formula is correct.

2. **Quadratic orientation.**  With `T=aq+bp`, multiplication by `p`
   gives `bp^2-Tp+aN=0`.  The discriminant is
   `(aq-bp)^2`.  The coefficient order in the statement is correct.

3. **Round-half-up range.**  The definition gives
   `-B/2 <= x < B/2`.  A positive half-tie maps to the negative endpoint.
   This matters only in the displayed `d=2` specialization.

4. **The `d=2` offset.**  If `p=2s_p+1`, then
   `round_half_up(p/2)=s_p+1`, so `x=-1`, not `+1`.  Both local residues are
   `-1`, their product is `1`, and `c=0`.  For even `d>=4`, `1/d<1/2`, so
   the centers are exactly `s_p,s_q` and both residues are `+1`.

5. **Degenerate centers.**  For an arbitrary large divisor `B`, `a` or
   `b` can be zero.  The statement does not apply a quadratic denominator
   in that case; it explicitly treats (3) as linear and makes no bank-success
   claim for a degenerate tuple.  At `B=d`, both centers are positive.

## P205 support checks

6. **Exterior support.**  From

   \[
   M=d(s_p+s_q+ds_ps_q)
   \]

   and coprimality of `s_p,s_q`, the cofactor `M/d` is coprime to each
   residual.  Hence a residual prime lies in `M` exactly when it lies in
   `d`.  No stronger valuation equality than the proved one is assumed.

7. **Saturation exponent.**  Since `s_i<N<2^n`, every primary valuation
   `v_ell(s_i)` is strictly below `n`.  If `ell | M`, then
   `v_ell(M^n)>=n`.  Thus `M^n` really absorbs the complete supported
   primary part of both residuals.

8. **Word length.**  The bit length of `M^n` is `O(n^2)`, not its numerical
   value.  It therefore qualifies as a polynomial-bit, hence
   numerical-quasipolynomial-bit, P205 word.

9. **Grammar qualification.**  The theorem is only about words whose
   prime support comes from divisors of `M`, formed multiplicatively.  It
   does not cover `B+c`, `B_1-B_2`, `u^2+cB`, resultants, modularly selected
   words, or adaptive integer presentations.  The conclusion is not a
   lower bound for factoring with a factored `N-1`.

10. **Baseline qualification.**  The optional `L` extension is also only a
    prime-support statement.  `(ML)^n` has quasipolynomial bit length only
    when `L` does.  For `L=R!`, this holds when the numerical value `R` is
    numerical quasipolynomial in `n`.

## Selector and window checks

11. **Short offset versus short carry.**  The proof uses
    `|y|<=B/2`, so (5) is valid.  The converse only bounds the smaller of
    `|x|,|y|` at square-root scale.  It does not identify which residue is
    smaller or supply its sign.

12. **Correct P205 word once selected.**  The integer
    `aB+x-u=u(p-1)` is positive and contains `s_p` completely.  Including it
    in `W` is sufficient even if `u` is not factored.  The argument does not
    claim that `x` is public before a selector is supplied.

13. **Factoring versus divisor enumeration.**  The primorial example proves
    only that naive complete enumeration can exceed quasipolynomial time.
    It does not prove selection hard and is labelled accordingly.

    The selector claim applies to nonzero `u^2+cB` and factors its absolute
    value.  A zero product is publicly visible and is not used as an
    enumeration obstruction.

14. **Window direction.**  The statement proves
    `s_p<=R => d` lies in the interval and, contrapositively, absence of all
    divisors from the interval implies `s_p>R`.  It does not assert the false
    converse from an arbitrary nearby divisor.

15. **Literal near-factor case.**  When `u=a=1`, a public signed scan of
    `x=p-B` directly tests the candidate `B+x`.  The statement does not
    portray this already-factor-sized information as a new carry gain.

## Complexity and top-level scope

16. Complete recursive factorization of `K` is granted as input to the
    boundary.  The packet does not silently count it as free in a complete
    factoring algorithm.

17. No theorem here constructs a useful additive word on every semiprime.
    No all-input success probability, almost-sure termination proof, or
    complete-factorization recurrence follows.  The root prompt remains
    unresolved.

## Highest-risk points for a fresh audit

1. Reconstruct the `d=2` round-half-up centers independently.
2. Check that the support-optimality claim never escapes its explicit
   multiplicative grammar.
3. Check that the optional baseline statement saturates valuations without
   assuming factorization of `L`.
4. Check that the carry-child divisor-count discussion is not read as a
   computational lower bound.
5. Check every implication direction in the divisor-window statement.
