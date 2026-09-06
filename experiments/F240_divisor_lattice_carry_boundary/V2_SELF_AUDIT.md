# Self-audit of F240 V2

## Verdict

**SELF-AUDITED PASS at the corrected proof-only scope.**

V1 failed hostile audit because its direct factor-bank claim did not exclude
`(a,b)=(0,0)`.  V2 adds that gate to every decoder-success claim and
preserves the remaining theorem.  This V2 is not verifier-backed.  Fresh
hostile re-audit and proof-blind reconstruction have not run.  No computation
was used.

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
   This matters in the displayed `d=2` specialization and in the general
   endpoint check below.

4. **The `d=2` offset.**  If `p=2s_p+1`, then
   `round_half_up(p/2)=s_p+1`, so `x=-1`, not `+1`.  Both local residues are
   `-1`, their product is `1`, and `c=0`.  For even `d>=4`, `1/d<1/2`, so
   the centers are exactly `s_p,s_q` and both residues are `+1`.

5. **Complete center-index classification.**  True centers are
   nonnegative.  They satisfy

   \[
   a=0\Longleftrightarrow2up<B,\qquad
   b=0\Longleftrightarrow2uq<B.
   \]

   Since `p<q`, `b=0` implies `a=0`; a true `a>0,b=0` case is
   impossible.  Thus a true tuple is either degenerate with `a=b=0`, has
   `a=0<b`, or has both centers positive.

6. **Exact hostile endpoint.**  At `B=M,u=1`, strict inequalities
   `2p<M` and `2q<M` give `a=b=0`.  Then `c=1,T=0`, and (3) is
   `0=0`.  V2 explicitly skips this tuple and makes no success claim for
   it.

7. **One zero center.**  If `a=0<b`, the true polynomial is
   `bX(X-p)`.  Its candidates are `0,p`; the explicit guard
   `1<X<N`, followed by exact division, returns `p` only.

8. **Zero centered residues.**  Since `gcd(B,pq)=1`, `x=0` holds
   exactly when `B|u`, which also forces `y=0`.  With `u=tB`, the
   polynomial is `tq(X-p)^2`.  This nondegenerate repeated-root case is
   valid.

9. **Round-half-up endpoints.**  The only included residue endpoint is
   `-B/2`.  If it occurs for `x`, then `a>=1` and monotonicity gives
   `b>=a`; if it occurs for `y`, then `b>=1`.  Thus it never causes the
   skipped two-zero-center case.  The positive endpoint is excluded.

10. **Decoder branches.**  V2 first rejects negative guessed centers.  For
    `b>0`, V2 requires an integer
    quadratic-formula candidate in the proper range before exact division.
    For `b=0,a>0`, it requires `T!=0` and an integer linear candidate.
    A true tuple never needs the linear branch, but it makes false guesses
    harmless.  At `B=d`, both centers are positive.

## P205 support checks

11. **Exterior support.**  From

   \[
   M=d(s_p+s_q+ds_ps_q)
   \]

   and coprimality of `s_p,s_q`, the cofactor `M/d` is coprime to each
   residual.  Hence a residual prime lies in `M` exactly when it lies in
   `d`.  No stronger valuation equality than the proved one is assumed.

12. **Saturation exponent.**  Since `s_i<N<2^n`, every primary valuation
   `v_ell(s_i)` is strictly below `n`.  If `ell | M`, then
   `v_ell(M^n)>=n`.  Thus `M^n` really absorbs the complete supported
   primary part of both residuals.

13. **Word length.**  The bit length of `M^n` is `O(n^2)`, not its numerical
   value.  It therefore qualifies as a polynomial-bit, hence
   numerical-quasipolynomial-bit, P205 word.

14. **Grammar qualification.**  The theorem is only about words whose
   prime support comes from divisors of `M`, formed multiplicatively.  It
   does not cover `B+c`, `B_1-B_2`, `u^2+cB`, resultants, modularly selected
   words, or adaptive integer presentations.  The conclusion is not a
   lower bound for factoring with a factored `N-1`.

15. **Baseline qualification.**  The optional `L` extension is also only a
    prime-support statement.  `(ML)^n` has quasipolynomial bit length only
    when `L` does.  For `L=R!`, this holds when the numerical value `R` is
    numerical quasipolynomial in `n`.

## Selector and window checks

16. **Short offset versus short carry.**  The proof uses
    `|y|<=B/2`, so (5) is valid.  The converse only bounds the smaller of
    `|x|,|y|` at square-root scale.  It does not identify which residue is
    smaller or supply its sign.

17. **Correct P205 word once selected.**  The integer
    `aB+x-u=u(p-1)` is positive and contains `s_p` completely.  Including it
    in `W` is sufficient even if `u` is not factored.  The argument does not
    claim that `x` is public before a selector is supplied.

18. **Factoring versus divisor enumeration.**  The primorial example proves
    only that naive complete enumeration can exceed quasipolynomial time.
    It does not prove selection hard and is labelled accordingly.

    The selector claim applies to nonzero `u^2+cB` and factors its absolute
    value.  A zero product is publicly visible and is not used as an
    enumeration obstruction.

19. **Window direction.**  The statement proves
    `s_p<=R => d` lies in the interval and, contrapositively, absence of all
    divisors from the interval implies `s_p>R`.  It does not assert the false
    converse from an arbitrary nearby divisor.

20. **Literal near-factor case.**  When `u=a=1`, a public signed scan of
    `x=p-B` directly tests the candidate `B+x`.  The statement does not
    portray this already-factor-sized information as a new carry gain.

## Complexity and top-level scope

21. Complete recursive factorization of `K` is granted as input to the
    boundary.  The packet does not silently count it as free in a complete
    factoring algorithm.

22. No theorem here constructs a useful additive word on every semiprime.
    No all-input success probability, almost-sure termination proof, or
    complete-factorization recurrence follows.  The root prompt remains
    unresolved.

## Highest-risk points for a fresh audit

1. Reconstruct all true center-index cases and the exact `B=M,u=1`
   degeneration.
2. Verify that every direct factor-bank claim contains
   `(a,b)!=(0,0)`.
3. Reconstruct the `d=2` round-half-up centers independently.
4. Check that the support-optimality claim never escapes its explicit
   multiplicative grammar.
5. Check that the optional baseline statement saturates valuations without
   assuming factorization of `L`.
6. Check that the carry-child divisor-count discussion is not read as a
   computational lower bound.
7. Check every implication direction in the divisor-window statement.
