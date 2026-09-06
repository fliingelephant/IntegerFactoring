# F201 frozen manifest

Status: frozen proof-only candidate.  No hostile audit or blind
reconstruction has run.

Frozen SHA-256 hashes:

- `STATEMENT.md`:
  `4915cbeea9e258524ece5dcf21e115f1a6c8ef0775dd0d1b926b94cdcbda8d41`
- `PROOF.md`:
  `56dce149bdd39b545b35e695108aa8a1dd3fa0bb8cc891aaf437a95d03e82e17`
- `SELF_AUDIT.md`:
  `ca4dce01e8a1e1ed257ef560394f9151400e4da1d2f1d7975351c2fb188a72ab`

Imported promoted premise:

- P175: the balanced-squarefree-semiprime reciprocal-prefix interface and
  its quarter-minus-polylog terminal precision.

Verification requirements:

1. Recompute all three frozen hashes before reading the packet.
2. Reconstruct the balanced inequalities
   \(p\leq B<q\), \(B\leq2p-2\), and
   \(\lceil B/2\rceil<p\), including every interval endpoint.
3. Verify that inversion of the two reciprocal lifts gives the two parity
   children of the consecutive AP, without assuming the correct next bit.
4. Verify the odd-cardinality public-endpoint cleanup, including the
   \(L=1\) factor terminal and preservation of a consecutive AP.
5. Verify that exactly one paired child product contains \(p\), neither
   contains \(q\), and a modular product evaluator would select the next
   bit.
6. Verify the interlacing comparison, with equality in the middle bound
   only for \(s=1\), and derive the exact Euclidean quotient one and
   remainder \(D=O-E\).
7. Check both orientations modulo \(p\) and confirm \(p\nmid D\).  Reject
   every inference that \(q\nmid D\) or that \(\gcd(D,N)=1\); accidental
   \(q\)-support remains possible.
8. Verify that reverse division has quotient zero and unchanged remainder
   \(E\), and that the Pochhammer and gamma formulas represent the same
   ordered integer pair.
9. Recheck the positive-expansion lower bound for \(D\), including the
   equality case \(s=1\), and the separate explicit-size lower bound for
   \(E\).
10. Recheck the full-cell count \(s=B/(4m)+O(1)\), its persistence under
    repeated public endpoint cleanup, and the
    \(2^{\Theta(n)}\)-bit explicit size at P175 precision.
11. Reconstruct the two linear-axis equivalences and keep them limited to
    fixed public linear combinations.  Check public coefficient gcd
    screening and leave accidental \(q\)-support open.
12. Reject any reading as a lower bound against implicit modular AP-product
    algorithms, adaptive nonlinear integer selectors, nonlocal floors or
    carries, or different one-child auxiliaries.
13. Preserve the explicit opening: a QP next-bit selector gives an
    \(O(n)\)-stage unique-child chain.  Fixed-ratio contraction is not
    necessary, and \(T(n)\leq T(n-1)+\operatorname{QP}(n)\) is QP.

The manifest does not hash itself.  Its observed SHA-256 must be reported
with the frozen packet.

No mathematical computation or benchmark was used.  One broad web search
during the preceding exploration supplied no premise, citation, or claim to
this packet.  No durable-ledger file was edited.
