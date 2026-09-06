# Self-audit of F207

## Verdict

PASS at the self-audited proof-only label, with the scope restrictions below.
This is not independent verification.

## Checks performed

1. **Recursion quantifiers.** The constants `rho,c,C,k` are fixed and do not
   depend on `N`. The ceiling and additive constant are absorbed by a fixed
   `sigma<1` only above a fixed base range.
2. **QP exponent.** Unrolling the decrement spine contributes the factor
   `nQ(n)` once per geometric scale. There are `O(log n)` scales, so an
   exponent `O((log n)^(k+1))` is sufficient.
3. **Multiple children.** The theorem covers a fixed or QP number of
   fixed-ratio side children. It does not relabel a second near-size child as
   fixed-ratio work.
4. **Balanced output accounting.** `q^2<2N` follows from `q<2p`; hence both
   output factors and `E` have half-size plus a constant. This statement does
   not extend to unbalanced inputs.
5. **Coprimality.** `gcd(K,N)=1` is automatic. The torsor theorem explicitly
   screens `gcd(E,N)` before using unit inverses.
6. **Prime-power overlap.** On a prime power occurring equally in `K` and
   `E`, the construction chooses root 1. It is valid because the full prime
   power divides `K`. No consistency between roots 1 and `B` is assumed.
7. **The prime 2.** The CRT construction includes the 2-primary component.
   Since `N` is a unit modulo `M`, the constructed `R` is also a unit.
8. **Torsor count.** The parameterization is bijective. The elementary bound
   `phi(M)^2>=M/2` was checked prime-power by prime-power.
9. **No false size lower bound.** The exponential count is explicitly local.
   The theorem does not assert that exponentially many candidates survive
   balanced integer intervals or exact multiplication.
10. **Character scope.** The inversion claim is only for quadratic
    characters and symmetric expressions. Nonquadratic characters and
    integer representatives remain open.
11. **Jacobi reciprocity.** Every support prime is coprime to `N`. For a prime
    dividing `E`, `B` is nonzero modulo that prime on the screened branch.
12. **Class-group scope.** The last claim uses only genus characters. It does
    not say that a factored `K` child cannot help navigate the full class
    group.

## Highest-risk points for hostile review

1. Verify that the monotone-envelope unrolling proves the bound for the exact
   stated recurrence, including expected-time interpretations.
2. Verify the balanced complete-recursion application and its explicit
   exclusion of the unbalanced two-near-child case.
3. Verify that the local root construction remains valid at shared prime
   powers and at 2.
4. Check that no sentence turns the local inverse-torsor count into a general
   information or time lower bound.
