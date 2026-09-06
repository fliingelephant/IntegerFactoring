# F198 manifest

Status: frozen literature-dependent proof-only candidate.

Frozen inputs:

- `STATEMENT.md`:
  `244e44b2d93fe6f62ef2ceb161b67132a12d3741a54a6ff80a2930e438dce0bb`
- `PROOF.md`:
  `7bde29f9c62ab8fa357f7103615a8c5a45db5a38ddb4e94a9bc576bde5bba12a`
- `SELF_AUDIT.md`:
  `3b5403d564b2e10565cab184c753fa6a956cdcdc609872bad4d0026cb77669d4`
- `PROVENANCE.md`:
  `9b22d615ea4cca619b8ae5085800eefb1194ddde976b745bf564a0cf9ef0b32e`

Required review before promotion:

1. verify every frozen hash;
2. reconstruct the balanced-prime congruence and the identity
   \(h-z_t=p^{-1}\bmod2^t\) independently;
3. inspect the Andreica 2013 primary source and the four forced errata
   inherited from the P173 source-level audit;
4. verify that Andreica is called at precision \(n\), not \(t\), before
   reducing the public coefficient;
5. inspect Gao--Feng--Hu--Pan 2025, Theorem 3.1, in the primary source and
   check \(m=2^t,s=p\bmod2^t,r=1\), every input hypothesis, and the bound
   \(N^{1/4}/2^t<2^{L+1}\);
6. inspect Coppersmith 1997, Theorem 5, in the primary source and verify the
   exact low-order threshold
   \(k=\lfloor(\log_2N)/4\rfloor=\lfloor(n-1)/4\rfloor\);
7. check canonical residues, modular inversions, the half-precision exact
   recovery, all \(2^L\) independent Coppersmith extensions, and candidate
   verification;
8. preserve the distinction between a carry-to-factoring reduction and an
   algorithm that evaluates the carry.

The manifest does not hash itself. Its observed SHA-256 must be reported
with the frozen packet. No experimental mathematical computation or
durable-ledger edit was used.

