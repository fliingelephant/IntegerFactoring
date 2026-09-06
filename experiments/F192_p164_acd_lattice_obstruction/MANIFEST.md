# F192 manifest

## Frozen candidate files

- STATEMENT.md
  - SHA-256: 23834b7193ce2f3e8e32a3277832fab633c2b7a701bd74591087b3d30ab57cb8
- PROOF.md
  - SHA-256: 73c520f978b47c7a937a5169456e8303818f69f6123a59ba5758ba4f9684e1f4
- SELF_AUDIT.md
  - SHA-256: f86a9a7d30bcb4a68d85b86f168135d1db35bf46af5b19c4c581510026b05564

## Evidence class

Proof-only candidate. No mathematical computation was run. Hashing was used
only to freeze the text. No durable proved/failed ledger was changed.

The proof uses elementary multiplicative-order divisibility, a circular
gap average, an exact triangular determinant, simultaneous Dirichlet
pigeonholing, coordinate divisibility, and a finite cyclic-order count. No
external theorem or heuristic is invoked.

## Exact scope

F192 proves that one P164 base yields a public power word that is distinct
modulo both hidden primes of a semiprime. It gives hidden approximate-multiple
clusters for each factor.

For the standard simultaneous-approximation row lattice, in the exact
parameter range stated in (14), every shortest vector has unit coefficient
and unit coordinates modulo \(N\). Exact SVP followed by coefficient or
coordinate gcd tests therefore returns no factor. The asymptotic corollary
applies to fixed-balance semiprimes, numerical-QP word length, and
polylogarithmic lattice dimension at the natural cluster error scale.

The cyclic-order theorem gives a necessary size lower bound only for a
predeclared subset bank that uses no information beyond the unknown local
cyclic order.

F192 is not a lower bound for other lattices, other postprocessors of an SVP
output, robust ACD, affine targets, multivariate polynomial methods,
source-aware use of the recurrence, integer factoring, or support-covering
selectors in general.

## Required next reviews

1. Fresh hostile audit of the frozen statement, proof, and self-audit.
2. If the hostile audit passes, fresh statement-only blind reconstruction.
