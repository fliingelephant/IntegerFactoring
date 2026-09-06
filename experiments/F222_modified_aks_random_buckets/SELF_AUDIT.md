# F222 self-audit

## Verdict

The candidate passes self-audit within its exact observation models. It
does not close arbitrary AKS coefficient processing or construct a biased
shift sampler.

## Algebra checks

1. The modified constant is `-a^N`. This makes the error homogeneous and
   distinguishes F222 from P11/P14/P18/P24.
2. The local identity is `E=h_(N/ell,a)^ell`, not the standard local error
   with constant `-a`.
3. Frobenius preserves support and nullity only because `gcd(r,N)=1` is
   explicit.
4. Scaling by `a` is used only for unit shifts.
5. The exact image-count formula allows roots in the algebraic closure. It
   does not incorrectly count only base-field roots.

## Probability checks

1. `X^r-1` has exactly `r` distinct roots because the local characteristic
   does not divide `r`.
2. On the `p` side, the two extreme coefficients prove that the degree-`d`
   polynomial cannot vanish identically. The hypothesis `p>d^2+1` is
   sufficient and holds eventually on the fixed-gap family.
3. On the `q` side, multiplication can introduce the one exceptional value
   `a=-xi`. It is added explicitly. The leading coefficient of the cleared
   polynomial is nonzero.
4. The resultant factor event and common-annihilation event are both subsets
   of the union of local-nullity events, so the upper bound applies to both.
5. Adaptive `r` is covered only when it is fixed before a fresh independent
   shift is sampled. Same-shift adaptive selection and biased shifts are
   excluded.
6. The infinite family uses only the bounded-gap family already invoked in
   promoted P165 plus finite pigeonhole. No twin-prime conjecture is used.

## Coefficient checks

1. The local support bound is before and after cyclic reduction; reduction
   can merge terms but cannot create support.
2. Absence of a proper coefficient gcd forces equality of the two local
   zero patterns, including coefficients zero modulo both primes.
3. The sparse outcome is not mislabeled as an annihilator or factor.
4. The condition `r>2d` is necessary for the support statement to guarantee
   a zero bucket. When `d>=r/2`, no coefficient conclusion is claimed.
5. The close-gap comparison charges the same-node Fermat scan. It does not
   use recursion or a contraction objection.

## Complexity and scope

A dense coefficient or resultant call costs polynomial in the numerical
modulus `r` and the input bit length. Therefore it is QP only for numerical-
QP `r`. An implicitly represented exponential `r` is outside the claim.
No computation or external citation is used.
