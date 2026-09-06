# Self-audit of F224

## Verdict

The proof is internally consistent at candidate level.  It is not
verifier-backed.  The result is a gap-dependent terminal plus a scoped
source obstruction, not an all-input factoring algorithm.

## Checks

1. **No hidden trace.**  The AP-Fermat class uses only `N,L,s`.  The
   cofactor residue is `Ns^(-1) mod L`; the exact trace is not assumed.
2. **Division by two.**  Solving `2A=c mod L` yields one class modulo
   `L/gcd(2,L)`, not necessarily modulo `L`.  This loss is included in the
   factor `4` in the scan bound.
3. **Exact gap.**  The identity
   `A_*-sqrt(N)=d^2/[2(sqrt(p)+sqrt(q))^2]` gives the stated strict upper
   bound `d^2/(8p)`.
4. **Cell injection.**  Under `q<2p`, the diameter of the public balanced
   interval is less than `(sqrt(2)-1)p`, so distinct integer shifts remain
   distinct modulo both hidden primes.
5. **Nonunits.**  The only nonunit in the cell is the exact point `p`.
   It is separated before importing P193's unit-shift root counts.
6. **Root accounting.**  The four P193 local bounds sum to
   `rd + rd(r+1) + rd + 2rd = rd(r+5)`.  This is an upper bound; common
   roots and improper gcds can only reduce useful success.
7. **Adaptivity.**  The probability statement requires the modulus and
   sampling law to be fixed before the fresh shift.  It does not cover a
   modulus chosen after seeing that shift.
8. **Two-thirds crossover.**  On a failed Fermat branch,
   `L=O(d^2/(p Q_F))`.  Substitution into the AP root bound gives
   `QP*d^3/p^2`, which is exponentially small for
   `d<=p^(2/3-epsilon)`.
9. **P193 premises.**  Failure of a cap at least two forces `d>sqrt(p)`.
   Numerical-QP moduli are eventually below `d` and below both hidden
   primes.
10. **Numerics.**  D01 produced no mathematical rows.  No empirical claim
    appears in the theorem.

## Highest-risk point for a hostile audit

Check the pullback of all four P193 bad-shift sets to the integer cell,
including the q-side denominator exceptions and the separation of `x=p`.
Then check the direction of the implication from a failed capped Fermat
scan to the upper bound on `L`.
