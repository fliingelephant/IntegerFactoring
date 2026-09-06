# F200 V2 frozen manifest

Status: frozen proof-only V2 candidate.  No V2 hostile audit or V2 blind
reconstruction has run.

Frozen SHA-256 hashes:

- V2_STATEMENT.md:
  1edaedf1e0121e4603b8502cfb2473de250366cdc4b35acb216c3be314c8b7e5
- V2_PROOF.md:
  b573b44d35d577e4c567448092997923c0a83cdeda8a1a1cb89ec9e1cf03e30b
- V2_SELF_AUDIT.md:
  5acac4d4bac434199b25f4e71674eb82308b3d03bbffb9af12f57968d62f1215
- V2_PROVENANCE.md:
  6a0dd42695efa1fb211094548c6452f7beeac815f3207aadb1b752568f22365b

Imported promoted premises:

- P171: the beta-two signed-binomial jump and adjacent recurrence.
- P173: QP evaluation of supplied signed-binomial endpoints modulo powers
  of two.
- P175: the reciprocal-prefix terminal precision.
- P160--P161: only the explicitly conditioned surviving
  \(H=\gcd(w-1,N)=1\) rough-local-order branch, after choosing
  \(T\geq D(n)\); all earlier exits remain separate.

Additional standard premise:

- Prime-to-two roots of unity in a finite extension of \(\mathbb Q_2\)
  reduce injectively into its residue field.

Verification requirements:

1. Recompute all four frozen hashes before reading the packet.
2. Recheck the one-denominator delta, gcd orientation, and floor sign.
3. Recheck the quotient-valued Walsh, Fourier, Haar, cyclic-difference,
   and autocorrelation claims.
4. Recheck the reciprocal-cell inversion, dyadic gauge symmetry, and
   nonempty-cell range.
5. Recheck endpoint accounting, residue-cell run count, and sampling
   probability.
6. Recheck the auxiliary-modulus, 2-adic density, Mahler, and phase-bias
   scopes.
7. Recheck the repaired P160--P161 branch condition, the coupling
   \(T\geq D(n)\), and the local cyclotomic degree conclusion.
8. Reject any reading as a general circuit lower bound or a factoring
   algorithm.

The preserved V1 hostile audit is a FAIL and does not transfer to V2.  The
preserved V1 blind reconstruction also does not transfer.  Their exact
hashes and the post-freeze history are recorded in V2_PROVENANCE.md.

No mathematical computation, web search, new external source, benchmark,
or durable-ledger edit was used.
