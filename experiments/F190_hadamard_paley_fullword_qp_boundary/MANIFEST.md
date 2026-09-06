# F190 manifest

## Frozen candidate files

- `STATEMENT.md`
  - SHA-256: `78e8cfd74e5ed824e6bb74c3aacbef0e9af6c67746373aa6e478a77ed9930b38`
- `PROOF.md`
  - SHA-256: `03a3a80387d43fd9a89e5c5453ac36af7c1dd09133f7029b419cdeacc4dd41bb`
- `SELF_AUDIT.md`
  - SHA-256: `4a542af975f48836fc168024bab8ce1b339c34d6154ba427d9d79051914e4724`

## Evidence class

Proof-only candidate. No mathematical computation was run. No durable
proved/failed ledger was changed by these candidate files.

The Fourier, Hankel, autocorrelation, list-size, code-distance, and collision
claims are elementary apart from the standard quadratic character-sum,
Gauss-sum, and hypergeometric Chernoff bounds stated in the proof. The
public-transcript equivalence uses standard deterministic primality and exact
perfect-power procedures.

## Exact scope

F190 closes these P54 submodels after polynomial resources become QP:

- explicit scalar shifted correlations with QP total support and QP
  coefficient norm;
- dense Fourier, Hankel, Prony, and Padé reconstruction;
- row-only exact list recovery from short punctures;
- direct sign-splitting enumeration;
- independent local-coordinate collisions;
- QP families of bounded-degree polynomially correlated equality tests.

It does not close retained-source, full-row, high-order modulus-blind
decomposition. A decoder specified to return a numerical prime with
inverse-QP probability is QP-equivalent to factoring and is not supplied.

## Required next reviews

1. Fresh hostile audit of the frozen statement and proof.
2. If the hostile audit passes, fresh statement-only blind reconstruction.
