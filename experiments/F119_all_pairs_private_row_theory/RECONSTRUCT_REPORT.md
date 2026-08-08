# Proof-blind reconstruction report

## Exact verdict

`PASS` for claims A, B, and C, with no strengthened scope.

- Claim A follows from one subtraction identity and the unique carry residue
  class modulo a prime not dividing `N`.
- Claim B follows from an explicit CRT construction. It gives
  `t(t-1) = Theta(n/log n)` independent selected columns on infinitely many
  odd distinct semiprimes.
- Claim C is necessary. The construction protects rows only inside the
  selected submatrix and does not create a square dependency or a non-global
  root.

## Construction in one line

For the first `t` odd primes `a`, set `L` to the product of their squares and
force `N = 1 mod L`. The menu residue `c=a^2*b` then has carry `k=c-1`.
Give each carry a distinct prime `r` above the carry diameter and force

```text
N = (r-1)*k^(-1) mod r^2.
```

CRT combines these conditions. Linnik supplies two primes in classes whose
product has the prescribed residue. PNT gives the required modulus and bit
length estimates.

## Representative boundary

The named screen proof belongs to the named canonical residue `c` and its
least positive inverse.

- If `c` appeared earlier, its endpoints and screens are identical.
- If a different residue appeared earlier with the same exact integer value,
  the value column and its private valuation row are unchanged.
- The different residue can have different endpoint sign screens. No claim is
  made about them or about the absence of an earlier direct factor.

## Missing full-source conditions

Three additional facts would be required:

1. every protected row has degree one after all distinct source values are
   present;
2. the full exact parity matrix has nonzero kernel;
3. some kernel vector has normalized root outside the global signs.

These facts are logically separate. Stable private rows force dependencies to
avoid their columns. A dependency with global root still does not factor the
semiprime.

## Isolation and evidence

The only F119 input read was `RECONSTRUCT_STATEMENT.md`, whose verified
SHA-256 is
`4a4aaf43119609e7745b5f88623a3ea9fb3c72aac7d15b16062d1aef0e692986`.

No durable ledger or other F119 file was read. No project proof search was
performed. No computation was used. No durable ledger was edited.
