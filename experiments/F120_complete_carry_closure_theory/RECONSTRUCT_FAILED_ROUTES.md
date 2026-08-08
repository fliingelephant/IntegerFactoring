# Rejected routes and extensions

1. **Assuming one exact product per inverse orbit.** This premise is false.
   For `N=11`, both `{2,6}` and `{3,4}` give `P=12`. The proof instead maps
   each projected exact value to one divisible endpoint. Uniqueness of the
   inverse at that endpoint makes the map injective.

2. **Counting only the carry residue class.** If `r | P`, then
   `kappa=-N^(-1) mod r`, but counting every integer in that residue class
   can be too weak. For example, `N=13` and `r=7` allow the candidate carries
   `1` and `8` in `1,...,N-2`, while `floor(12/7)=1`. The second candidate
   does not come from endpoints below `N`. The endpoint injection retains
   this essential feasibility condition.

3. **Using duplicate removal without an explicit map.** It is true that
   projection cannot increase a count, but that sentence alone does not
   identify which pre-projection objects are being counted. The explicit
   endpoint injection proves the exact projected bound and handles
   cross-orbit duplicates.

4. **Using a probable-prime test for the finite witness.** A finite list of
   Miller--Rabin trials without a proved range theorem would not meet the
   deterministic requirement. The proof uses complete recursive Lucas
   certificates. Every operation is an exact factorization identity, modular
   power, or gcd.

5. **Promoting Dirichlet to a shifted-semiprime theorem.** Dirichlet proves
   that prime `q=1 mod 30` occur infinitely often. It does not control the
   factorization of `2q-1`. The missing infinite-family statement is isolated
   in the proof and is not asserted.

6. **Inferring full column rank from one private row.** A private row forces
   one coordinate to zero in every kernel vector. Other columns can still
   have dependencies. For example, the matrix with rows `(1,0,0)` and
   `(0,1,1)` has a private first row and kernel vector `(0,1,1)`.

7. **Inferring closure failure from the unusable column.** Deleting the
   private row and column preserves the entire kernel on the other
   coordinates. Closure can therefore succeed or fail independently on the
   surviving matrix.

8. **Inferring a nontrivial modular root from parity closure.** Closure gives
   an exact square and thus a square root of one modulo `N`. It does not show
   that the root differs from `+1` and `-1`. At `N=15`, the canonical squares
   `16=4^2` and `196=14^2` exhibit nontrivial and trivial root classes,
   respectively.

9. **Applying the inverse formula modulo one without a convention.** The
   carry at `c=1` is exactly zero, but standard modular-inverse notation is
   not defined modulo `1`. The proof treats this endpoint separately.

10. **Adding smoothness or random-matrix assumptions.** Neither is needed
    for the degree bound, the private-row result, the finite witness, or the
    kernel isomorphism. No heuristic conclusion is used.
