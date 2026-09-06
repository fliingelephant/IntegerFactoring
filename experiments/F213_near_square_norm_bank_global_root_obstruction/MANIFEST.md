# F213 manifest

## Family

F213: near-square norm-bank global-root obstruction.

## Namespace check

Before the directory was created, a repository-wide search found no F213
entry in the durable ledgers, notes, or experiment tree.

## Status

Frozen, self-audited, proof-only candidate. It has not passed a fresh hostile
audit or a strict statement-only reconstruction.

## Frozen candidate files

- `STATEMENT.md`
  - SHA-256:
    `9e74427637283e893c5a91bc5d0d24d7a4040526dbe5cf2e1599971474081fff`
- `PROOF.md`
  - SHA-256:
    `ac83b7fa190b16226b69d7f2604fe6a0aa684e8594251dbe702aa5f780a43b35`
- `SELF_AUDIT.md`
  - SHA-256:
    `a600e744634740f39839a982bc76ee5ea4e9de7c049b3cf5c6f023fc23e37bfd`
- `PROVENANCE.md`
  - SHA-256:
    `da8e68c689eba36ba3c2e7348c3f13e510582e77694eec8f976dd0750cb9ce37`

The manifest does not hash itself. Its observed SHA-256 must be reported
separately with the frozen packet.

## Evidence class

No mathematical computation, finite search, random sampling, local
experiment, or remote experiment was run. Hashing was used only to freeze
the text.

No durable registry, proved ledger, failed ledger, progress ledger,
statement ledger, or inspiration file was changed.

## Claims frozen for audit

1. For every \(M\geq2\), there is an even \(s>M\) for which
   \(N=s^2+1\) is odd and composite and the first \(M\) near-square norms
   satisfy \(r_a=as\), \(E_a=a^2\), and
   \(F_a=2as+1-a^2\).
2. Every relation base and norm is a unit modulo \(N\), so the displayed
   bank has no direct gcd exit.
3. A CRT construction gives each \(F_a\) a distinct valuation-one prime row
   that occurs in no other \(E_b\) or \(F_b\) column.
4. The complete sign-and-prime parity kernel excludes all \(F_a\)'s and is
   exactly the even-subset space on the \(E_a\)'s.
5. Every dependency in that kernel has normalized root
   \(s^k=(-1)^{k/2}\), so its two standard gcds are \(1\) and \(N\).
6. Repeated Bertrand intervals give the safe size bounds
   \(\Omega(M^2)\leq n\leq O(M^2\log M)\), hence
   \(M=n^{1/2+o(1)}\). No short-interval prime-density claim is used.
7. The public subbank \(a\leq\lfloor n^{1/3}\rfloor\) inherits the same
   obstruction for all sufficiently large constructed inputs.
8. The \(F_a\)'s have \((1/2+o(1))n\) bits and the \(E_a\)'s are smaller,
   so complete recursive factorization is valid fixed-ratio accounting under
   P183, including in the presence of one separate one-bit spine.

## Highest-risk points

1. Verify that choosing a non-Hensel lift modulo \(d^2\) proves
   \(d\parallel N\) and that \(d<N\).
2. Check every CRT modulus is pairwise coprime. In particular, use
   \(\ell_a>R^2+1\geq d\), not an unstated prime-distribution fact.
3. Re-derive the repeated-Bertrand upper and lower bit-length bounds and the
   conclusion \(M=n^{1/2+o(1)}\).
4. Check the exact cross identity
   \(bF_a-aF_b=(b-a)(1+ab)\) and its strict magnitude bound.
5. Reconstruct the full parity kernel with the sign row included.
6. Verify that every normalization denominator is a unit and that the image
   consists only of global roots.
7. Reject any interpretation that asserts semiprimality, balanced factors,
   efficient generation of the witness family, failure of arbitrary
   nonlinear postprocessing, or failure of every larger QP schedule.

## Required fresh reviews

1. Recompute all four frozen content hashes before reading the packet.
2. Run a hostile audit against the frozen statement and proof.
3. If it passes, give a fresh agent only `STATEMENT.md` and the key ideas
   “no-carry square family, CRT private adjacent rows, repeated Bertrand
   sizing,” and require a strict end-to-end reconstruction.
4. Promote only after both reviews pass and the frozen hashes are rechecked.
