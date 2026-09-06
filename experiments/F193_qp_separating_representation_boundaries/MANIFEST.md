# F193 manifest

## Frozen candidate files

- `STATEMENT.md`
  - SHA-256: `55968763e179387ff0db2bcb90a3740ffa36d982ab5f23e81b67d0fc6bae0f46`
- `PROOF.md`
  - SHA-256: `b9ce3e75679b8bc6e04d38236d3d57e7bb15de7d968b7183575c1c0a6c821f1f`
- `SELF_AUDIT.md`
  - SHA-256: `6644ad9d81ac31ea9052786ff0b37529176127c0e04a8c6d7830d38fd3f7f905`

## Evidence class

Proof-only candidate. No mathematical computation was run. Hashing was used
only to freeze the text. No durable proved/failed ledger was changed.

The candidate uses standard exact facts about squarefree `Gamma_0(N)` cusp
classification, modular-symbol boundaries, good-prime Hecke representatives,
Atkin--Lehner exact divisors, Dirichlet twists, finite etale torsion, and
geometric fiber transport. The CRT amplification and all bit bounds are
proved explicitly.

## Four independent claims

1. An explicitly listed rational endpoint at a factor-local cusp already
   exposes a factor through its denominator gcd. Good-prime Hecke branches
   preserve cusp type; Fricke preserves the global/hidden pair partition;
   standard selective Atkin--Lehner operators are labeled by a factor.
2. A uniform QP evaluator of P29's `b_N` over a growing bank of
   `O(log n)`-bit auxiliary primes reconstructs the exact coefficient by CRT
   and factors the promised semiprime.
3. Dirichlet twists of one form at the one index `N` are public scalar
   multiples of one coefficient.
4. One globally defined elliptic-curve endomorphism has conjugate actions on
   prime-to-characteristic torsion in any two good geometric fibers of its
   connected base.

## Exact non-implications

F193 is not a general modular-symbol, cusp-form, modular-form, etale-algebra,
or elliptic-torsion obstruction. It does not cover a boundary-zero cuspidal
quotient, metric information in a global boundary coefficient, a compressed
dense presentation, genuinely different forms, a new coefficient evaluator,
local Frobenius, reduction-only endomorphisms, or CRT-glued fine maps that do
not descend from one connected base.

## Required next reviews

1. Fresh hostile audit of the frozen statement and proof.
2. If the hostile audit passes, fresh statement-only blind reconstruction.
