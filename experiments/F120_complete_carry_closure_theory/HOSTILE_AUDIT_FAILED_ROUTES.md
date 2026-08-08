# F120 fresh hostile-audit rejected attacks and extensions

No new computation was run. These are proof attacks that do not invalidate
the stated F120 theorem, plus extensions that remain unproved.

## 1. Count every inverse orbit after an exact-product collision

For `N=11`, product `12` comes from orbits `{2,6}` and `{3,4}`. Counting both
orbits would make an endpoint argument about raw representations, not about
the globally deduplicated exact-value matrix. F120 counts product columns.
Choose one witness orbit per distinct product. Witnesses for different
products are disjoint, so the degree proof survives.

## 2. Assume exact-value privacy gives representation privacy

It does not. A later residue can give the same exact product through another
inverse orbit. Exact-value projection discards the extra column, but an
adaptive algorithm can still use its endpoints or provenance as named
integer data. F120 does not rule out that feedback mechanism.

## 3. Apply the degree bound to a raw residue matrix

The bound can fail for raw multiplicity. Both orientations of one inverse
orbit already repeat one exact product. Several distinct inverse orbits can
repeat it again. The theorem requires global exact-value deduplication.

## 4. Derive complete full rank from one private row

A private row forces one column coefficient to zero. The remaining columns
can still contain dependencies. Peeling is an exact reduction, not a proof
that the core is empty.

## 5. Derive `ROOT` from `CLOSE`

A square dependency can have only a global positive root modulo `N`. Kernel
nullity and normalized-root image are separate invariants.

## 6. Use Dirichlet to make `2q-1` a semiprime

Dirichlet proves infinitely many primes `q=1 mod 30`. It does not prescribe
the factorization of `2q-1`. The missing semiprime statement `(SPS)` remains
an additional number-theory requirement.

## 7. Promote one finite search result to an infinite family

The ordinal-23 instance falsifies a universal all-semiprime `REUSE` claim.
It gives no asymptotic density and no infinite family.

## 8. Use only carry congruence to count feasible columns

A congruent carry is necessary for a prime incidence. It does not ensure
that `1+kN` is a product of two canonical endpoints below `N`. Endpoint
feasibility is what gives the sharper degree theorem.

## 9. Treat a failed environment run as negative evidence

The first Sage run failed during import, before it tested a candidate. Its
empty output has no mathematical content. Only the approved retry and the
independent verifier support the finite claim.

## 10. Infer source failure from the private seed column

Dependencies can avoid the peeled seed column and use other columns. F120 did
not enumerate or decode the rest of the finite input's complete source.

## 11. Ignore the `c=1` inverse notation boundary

The carry range remains valid at `c=1`, with `w=1` and `kappa=0`. To avoid
conventions about inversion modulo one, state the modular-inverse formula for
`c>1` and handle `c=1` directly. This is not a counterexample. Exact-value
projection removes `P=1`.
