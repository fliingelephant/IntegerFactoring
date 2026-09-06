# Provenance for F249

## Internal interfaces used

- **F194 / P171** supplies the balanced beta-two one-jump binomial identity
  and the original hidden-cancellation viewpoint.
- **F197** supplies the explicit factorial, BGS/holonomic, nonunit-division,
  and output-size boundaries.
- **F198 / P175** supplies the fact that a quarter-minus-polylogarithmic
  carry prefix is a numerical-QP terminal statistic.
- **F200--F201** supply the harmonic delta and arithmetic-progression
  product formulation of the same hidden index.
- **F219** supplies the random-top-multiplier carry law and the aggregate
  common-order/Las Vegas context.

## New proof content

F249 proves:

1. the exact shifted congruence
   \(C_{r,c}\equiv rq\binom{c-1}{B-p}\pmod N\);
2. the exact threshold gcd law and the always-successful public endpoint;
3. the exact uniform-shift probability and its floor-safe \(1/3\) lower
   bound;
4. the unique singular denominator at \(c=B-p\);
5. the collapse of the endpoint to the complementary central-binomial
   factor gate;
6. the identity of the accumulated denominator with a factor-bearing
   upper-half interval product;
7. the fact that top-multiplier randomization only unit-scales the same
   threshold; and
8. the rank-one relation among the corresponding beta-two carry values.

## Evidence and exclusions

No computation was run.  A targeted external literature check used:

- Alin Bostan, Gilles Christol, and Philippe Dumas, *Fast Computation of the
  Nth Term of an Algebraic Series over a Finite Prime Field*, ISSAC 2016,
  arXiv:1602.00545.

That paper gives the prime-field algebraic-series method discussed in the
packet.  The standard characteristic-zero holonomic cost statement is also
imported from the already documented F197 boundary.

This is a proof-only packet.  It supplies no numerical-QP coefficient
evaluator, no all-input factorer, and no lower bound against a different
succinct method.  No durable ledger was edited.
