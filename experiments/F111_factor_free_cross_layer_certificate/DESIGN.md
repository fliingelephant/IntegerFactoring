# F111 — factor-free replay of one F110 cross-layer certificate

## Question

Can the strongest small F110 cross-layer witness be verified using only
public integer arithmetic and an explicit dependency-index certificate?

## Public inputs

- `N = 3241632473`;
- the declared frozen-layer plus appended-pair source;
- the 363 public relation indices in `CERTIFICATE.json`.

The index list is a certificate, not a selector.  It was found by the
factor-assisted F110 discovery run.  Verification must not read `p`, `q`, an
endpoint factorization, or a prime-parity matrix.

## Replay

1. Generate initial seeds `2..n` and apply every direct screen.
2. Compute the seed endpoint basis by gcd splitting and exact perfect-power
   extraction only.
3. Generate the complete frozen layer.
4. Append `(2,3)` and then `(2,4)` until the public stop count.
5. Select the certified relation indices, multiply their exact relation
   values, and test whether the product is a square.
6. Reduce its positive square root modulo `N` and apply the two extraction
   gcds.

## Scope

A pass proves one explicit public cross-layer relation.  It does not show how
to select the dependency on another input and does not prove all-input
factoring.
