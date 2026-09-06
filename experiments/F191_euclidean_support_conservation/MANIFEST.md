# F191 manifest

## Frozen candidate files

- `STATEMENT.md`
  - SHA-256: `6747d7c6b121565bb1cbabb0041f7f11cb1f2f3306eb27beb126f3e4714bb124`
- `PROOF.md`
  - SHA-256: `21dfd6a74efc318434f54f5c7575b10c9d299b8e315459d20fd9643410cef455`
- `SELF_AUDIT.md`
  - SHA-256: `1bd8c60477f4bb8ccba50923e129333c0b48c5bf23312a21ac7ea1457c7ab7a5`

## Evidence class

Proof-only candidate. No mathematical computation was run. Hashing was used
only to freeze the text. No durable proved/failed ledger was changed.

The support-conservation identity and canonical counterexample are elementary
integer congruences. The QP bank theorem uses an exact endpoint count and a
union bound. No external theorem is invoked.

## Exact scope

F191 closes the inference that Euclidean or centered normalization of a known
multiple of a hidden local-order prime automatically produces a smaller
integer with the same prime support. It also closes a QP bank of such
normalizations in the stated permutation/equidistribution model.

It does not close arbitrary floor circuits, nonpermutation correlated maps,
or a special \((N,w)\)-dependent theorem that forces a quotient or carry to
contain the hidden prime. It is not an integer-factoring lower bound and not
an all-input factoring algorithm.

## Required next reviews

1. Fresh hostile audit of the frozen statement and proof.
2. If the hostile audit passes, fresh statement-only blind reconstruction.
