# Provenance for F248

## Internal interfaces used

- **P66** supplies the complete factor-free exact-square parity decoder and
  its normalized-root factor screen.  F248 uses only its one-row and explicit
  two-row specializations.
- **P106** identifies the gcd-free refinement matrix with the exact hidden
  integer-prime parity core.  It is used only to explain why the general
  nonduplicate multirow problem is not controlled by source-group orders.
- **P208** supplies the exact uniform norm-one torus sampler, the cyclic local
  torus orders, and the powered residual-image interface.
- **P209 / F244** supplies the infinite four-marker family and the fact that
  the relevant P208 residual image on each hidden side retains an
  exponential marker for the square exponent, and more generally for its
  covered numerical-QP signed-power grammar.
- **P211 / F247** supplies the affine principal-lift carry law.  F248 adds the
  exact four-square and two-useful-square classification of a complete
  principal fibre.

## New proof content in this packet

The packet proves and collects the following exact special-source laws:

1. the full-lift exact-square upper bound \(K/N\) and the local two-adic
   criterion for the conditional half-factor law;
2. the exact \(4/N\) square and \(2/N\) useful-square laws in one principal
   fibre, the fixed-past \(2/N\) useful-closure bound, and the
   second-square-root equivalence;
3. the canonical scalar duplicate bound;
4. the modulo-\(N^2\) reciprocal-output divisor bound;
5. the raw and powered torus Pell, duplicate, and inverse-point bounds.

These are proof-only source boundaries.  They are not a complete lower bound
for P66 and do not establish an all-input algorithm.

## Classical facts used

The proofs use only standard facts:

- cyclicity of unit groups modulo odd prime powers;
- CRT and the four square roots of one modulo a two-prime modulus;
- the classical parametrization and growth of solutions to Pell's equation;
- the standard divisor bound
  \(\tau(m)=\exp(O(\log m/\log\log m))\).

No external literature search was run for F248.  No publication-level
novelty claim is made.

## Deliberately excluded transfer

The reciprocal-output theorem concerns

\[
v=[u^{-1}]_{N^2}.
\]

It does not concern the value obtained by taking the canonical inverse base
modulo \(N\) and applying the scalar lift source again.  Those values can
differ by a principal-lift carry.

Likewise, the P209 marker argument controls the sizes of specified powered
torus image groups.  It does not control the ordinary integer-prime parity
of products of distinct source rows.
