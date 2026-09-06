# F221 self-audit

## Verdict

PASS at self-audited candidate status, with the exact scope in the frozen
statement.

## Checks

1. **Local exponent.**  Modulo `p`, `y^(pq)=y^q`; modulo `q`, it is `y^p`.
   No replacement by a globally computable local exponent is made in the
   algorithm.  These identities occur only in the proof of the distribution.
2. **Affine factor.**  Substitution `x=ac` gives
   `a(a^(q-1)D_(q,p)(c)-1)`, including `c=-1`.  Since `a` is a unit, it
   creates no extra zero.
3. **Coset size.**  In the cyclic group of order `p-1`, every nonempty fibre
   of `z -> z^(q-1)` has exactly `gcd(p-1,q-1)=d` elements.  The proof does
   not confuse image size and kernel size.
4. **CRT law.**  For fixed `c`, the local scale coordinates are independent.
   For independent uniform `(a,x)`, the bijection `(a,c) -> (a,ac)` also
   preserves uniformity and CRT independence.
5. **Gcd event.**  Neither local zero gives gcd one; both give gcd `N`;
   exactly one gives a proper factor.  Formula (3) is the exact XOR law.
6. **Adaptivity.**  The sequential bound conditions on the full past before
   drawing a fresh uniform scale.  It does not require independent choices
   of the normalized points.
7. **Expected time.**  A uniform conditional upper bound `epsilon` on each
   hit gives survival at least `(1-epsilon)^m` and hence expectation at
   least `1/epsilon`.  This is a lower bound for this named retry rule, not a
   factoring lower bound.
8. **Hard family.**  Only P165's already promoted infinite bounded-gap
   family is imported.  F221 does not claim this family has `N=3 mod 4`.
9. **QP comparison.**  Numerical QP is `2^((log n)^O(1))=2^o(n)`, so its
   product with `2^(-n/2+O(1))` remains `2^(-Omega(n))`.
10. **Sampling.**  Exact unit rejection is constant expected cost on odd
    semiprimes.  A rejected nonunit is a verified factor and has only
    square-root-scale probability on the balanced hard family.
11. **F220 interface.**  An affine AKS zero is not mislabeled as a factored
    annihilator or a primary certificate.
12. **Open channels.**  Fixed shift, biased scales, full coefficient data,
    joint nonzero-value processing, randomized carries, and other integer
    observables remain explicit.

## Computation scope

F221-D01 explored only the fixed-shift channel that the proof leaves open.
It is not used in any theorem.  The finite data showed nontrivial and varying
root fractions, which is consistent with keeping that channel open.
