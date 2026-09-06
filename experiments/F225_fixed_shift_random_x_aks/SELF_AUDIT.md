# F225 self-audit

## Verdict

PASS as a proof-only obstruction for the stated scalar channel.

## Algebra checks

1. The two Frobenius reductions hold for all residues, including `0` and
   `-1`.
2. Since `p,q` are odd, `c=2p-q` is odd.  On the constructed family,
   `c>=3`, so `k=c-2>=1` and `s=(c+1)/2>=2` are integers.
3. The `p`-side reciprocal step excludes exactly `0,-1` before clearing
   denominators.  Both excluded points are restored as genuine roots.
4. `P_k` is nonzero and has degree exactly `2k` because its degree-`2k`
   coefficient is `-1`.
5. The four `q`-side character cells are disjoint.  The two opposite-sign
   polynomials have degree `s`; the two same-sign polynomials have degree
   `s-1`.
6. The coefficients `2` and `s` used in the degree check are nonzero
   modulo `q`, since `q` is odd and `2<=s<q`.

## Probability checks

1. A proper gcd is the XOR of the two local zero events.  The displayed
   CRT formulas are exact.
2. Restricting to units removes `0` and no other local residue.  Therefore
   the unit root counts are exactly `A_p-1` and `A_q-1`.
3. Dropping the nonzero-event factors gives an upper bound, which is the
   direction required for an obstruction.
4. Gcd-screening a uniform residue adds only an `O(1/p)` direct-factor
   event.  This is absorbed by `O(c/p)` because `c>=3`.

## Infinite-family checks

1. Baker--Harman--Pintz is applied at
   `X_p=2p-floor(p^(3/5))`, not at `2p`.  Thus `c` is bounded below by
   `p^(3/5)+O(1)` and the exceptional case `c=1` cannot occur.
2. The BHP interval lies strictly above `p` for all large `p` and its upper
   endpoint is strictly below `2p`.
3. Its width is `O(p^0.525)=o(p^(3/5))`, so
   `c=Theta(p^(3/5))` and `d=p-Theta(p^(3/5))`.
4. Since `N=Theta(p^2)`, the one-trial bound `O(p^(-2/5))` is
   `2^(-Omega(n))`.  Multiplication by a numerical-QP trial count does not
   change that conclusion.

## Scope checks

1. No claim is made for biased or carry-correlated points.
2. No claim is made for joint processing of nonzero values.
3. No claim is made for a variable shift, coefficient vector, resultant,
   or quotient-ring computation.
4. The family has no promised residue class modulo `4`; the theorem does
   not assert one.
5. The proof does not rely on the optional local numerical check.  That
   check did not run because the selected Python runtime lacked SymPy.
