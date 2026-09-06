# Frozen V2 screen-free Pell-orbit circuit search

Use exactly the source, range, cleanup, factorization, ordering, and resource
limits in the frozen V1 preregistration with SHA-256
`d30118370efb835b4585743499c72629641e74cba5205d8da6d002b9eb7a3f65`.

The sole changed selection rule is this: discard a modulus from the circuit
search if any proper factor was found by any root, singleton-square, or
duplicate-coordinate cleanup gcd in its complete `0 <= j <= 4n` window.
Among moduli with no such cleanup factor, report the lexicographically first
dependent retained column.  Verify its exact square product and normalized
root gcds.  If there is no such dependency, report null over the frozen
range.  Do not extend the prime cap, Pell window, or discriminant menu after
viewing output.

This is finite discovery evidence only.
