# F129 proof-blind reconstruction — PASS

The verifier read only the corrected statement and independently
reconstructed every claim. It found no counterexample.

## Reconstructed core

For one support layer, write a cumulative dependency as \((x,y)\). The map

\[
(x,y)\longmapsto U_{s-1}x=A_sy
\]

is onto the old/new image intersection. Its kernel is exactly the direct sum
of the old and pure-new kernels. The first isomorphism theorem gives the
cross quotient and the telescoping dimension formula.

For parity dependencies, the exact positive roots satisfy

\[
R(x+y)=R(x)R(y)/\prod_{j:x_j=y_j=1}P_j.
\]

Every denominator is \(1\bmod N\). Thus the modular root assignment is a
homomorphism. Quotienting by the old and pure-new images makes the relative
cross-root map well-defined, with the stated image quotient. This also proves
the localization of the first useful support layer.

The shared-row bound follows because every common image vector is supported
only on rows present on both sides. A new private row forces its column
coefficient to zero. If a prime row divides two canonical values
\(1+\kappa N\) and \(1+\kappa'N\), reduction modulo that prime gives the
required carry congruence.

The support-two obstruction was reconstructed from an identity layer and
disjoint pair columns. Its cross quotient has arbitrary dimension, but each
kernel generator has root \(1\bmod N\). Its values violate the canonical
size constraints, so it is not claimed as an F26-Q counterexample.

The verifier also confirmed that P111's consequence is conditional on its
full-width private-row premise and applies only to the selected subsource.

Verdict: **PASS** as a decoder-accounting theorem. No source-success or
factoring claim follows.

