# F126 proof-blind reconstruction

**Verdict:** pass.

The reconstructor received only the statement and the row-combination idea.
It independently recovered:

- the coefficient vector
  \((\alpha-\beta,\alpha\beta-1,1-\alpha\beta,\beta-\alpha)\);
- the three vanishing columns and the exact residual;
- the Vandermonde minor, sign, and unit cancellation;
- the gcd equality;
- the F123 consecutive-power specialization; and
- the \(Q^3\) deterministic quasipolynomial rectangle scan.

It also independently identified the separate prefactor screens and the
unsafe exact-value deduplication rule. It found no all-input success law.
