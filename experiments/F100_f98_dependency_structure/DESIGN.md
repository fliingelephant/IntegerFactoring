# F100 — internal structure of the F98 dependency

## Question

The F98 public decoder found one 166-value binary dependency. Determine
whether this dependency is only an opaque high-dimensional event or has a
simple shared-factor incidence structure that can guide an unbounded theorem.

## Factor-assisted diagnostic

Read the frozen public F98 certificate. Factor only its 166 exact relation
values for diagnosis. Build the prime-valuation parity matrix and report:

- its rank and nullity;
- whether the selected set is a binary matroid circuit;
- parity-prime row-degree and relation-column-degree distributions;
- connected components under shared odd-valuation prime support;
- the fraction of rows of degree two; and
- exact provenance counts.

This computation is not part of the public factoring algorithm. It can use
Sage factorization. It supports only a structural diagnosis of the fixed F98
certificate.
