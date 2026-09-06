# F214 V2 frozen manifest

## Status

Frozen, self-audited, proof-only V2 candidate. V2 has not passed a fresh
hostile audit or a strict statement-only reconstruction. V1 and its hostile
FAIL are preserved as historical evidence only.

## Frozen V2 hashes

- V2_STATEMENT.md:
  3aa3260154c8f0f7848b5fd5f8f427de41be07c986c044ad3141e32bc1928e97
- V2_PROOF.md:
  a7209b215d5d5b5d3c72e73a577a50a541b413dc3ed3e31a4772235dbe5d97b3
- V2_SELF_AUDIT.md:
  23dbfe04020c8c28a36ebfa90837855e4ac8223012ca8673f7961790d4c0e4e3
- V2_PROVENANCE.md:
  9f5bbe761c03b33c873230bde82741d6ef465264996b631dff037deb0aa07e74

This manifest does not hash itself. Its observed SHA-256 must be reported
separately.

## Preserved V1 hashes

- STATEMENT.md:
  4254fce5cbd941e92328af90ae13adc8bd896e0559cdb5bff7bf92c12705d26f
- PROOF.md:
  47709b22bd4d53a7e4a2be48c092f53be6a369add17007a547672db603b80eee
- SELF_AUDIT.md:
  7964f48d43e34f853dd3b965a393ed42e395426277550de071004be154157f4f
- PROVENANCE.md:
  fe22a4be53d8603736d462488fc4dd8480dc9305aa098d74dd24c72ff84085e2
- MANIFEST.md:
  939cb1ae1e9fe840c0dc96ef024d3489516ec2d1963a7146c9e7e81d7b8e0465
- HOSTILE_AUDIT.md:
  fee67cd69879e271b23626b5f636ee172765799e65c9fb1612b93d1814b6fc2b

## Exact V2 repair

The V1 hostile audit found one fatal theorem-scope error. V1 inferred a
recursive factoring recurrence from a selector whose correctness was proved
only for balanced semiprimes. The child

\[
K=(N-1)/2
\]

need not satisfy that promise. For example,
\(247=13\cdot19\) is balanced, while
\(K=123=3\cdot41\) is not.

V2 repairs the theorem as follows:

1. The bounds
   \(\operatorname{bits}(K)\leq n-1\) and
   \(\operatorname{bits}(E)\leq n/2+O(1)\) are local facts at the current
   balanced node only.
2. The P183 recurrence is stated only after separately granting a correct
   all-input recursive dispatch whose immediate calls satisfy the declared
   size and count bounds at every node.
3. A hypothetical balanced-node selector contributes only to the local
   numerical-QP work term after that independent all-input dispatch has
   factored \(K\). The selector does not supply recursive closure.

The V1 audit also found one manifest-only summary error. V2 states the scan
counts exactly:

1. each balanced interval scan has \(\Theta(\sqrt N)\) candidates;
2. the full unit scan has exactly \(\varphi(K)\) candidates; and
3. the proved finite lower bound is
   \[
   \varphi(K)\geq\sqrt{K/2}=\frac12\sqrt{N-1}.
   \]

V2 does not claim that the unit scan has \(\Theta(\sqrt N)\) candidates.

## Claims frozen for review

1. For a balanced odd semiprime, every integer point in the full balanced
   box satisfying \(XY\equiv N\pmod{(N-1)/2}\) is exactly \((p,q)\).
2. If \(\operatorname{lcm}(2,m)\) exceeds both balanced interval diameters,
   every nonempty odd representative progression is a singleton, and the
   F209 endpoint predicate is exactly \(XY=N\).
3. At one balanced node, \(K\) is an at-most-\((n-1)\)-bit child and \(E\)
   is an \(n/2+O(1)\)-bit child. No recursive closure follows from these
   local facts.
4. Conditional on a separately correct all-input dispatch with at most one
   one-bit-decrement child and a numerical-QP number of half-size children
   at every node, P183 gives numerical-QP accounting.
5. A numerical-QP list containing a true factor residue at modulus
   \(m\geq N^{1/4}/2^{(\log n)^{O(1)}}\) is terminal through the
   Gao--Feng--Hu--Pan theorem cited by P175.
6. The two interval scans have \(\Theta(\sqrt N)\) candidates. The unit
   scan has exactly \(\varphi(K)\) candidates and only the explicit lower
   bound above. Explicit paired-CRT half lists have size at least
   \((K/2)^{1/4}\).
7. Every fiber of \(u\mapsto u+u^{-1}\) modulo \(K\) has at most
   \(4\,2^{\omega(K_{\rm odd})}\sqrt K\) elements. Hence the global sum
   image has the finite lower bound in (12), and an explicit CRT-MCSS
   half-list has size \(K^{1/4-o(1)}\).
8. The determinant-one completion \(XY-2K=1\) is exactly divisor selection,
   not an independent continued-fraction approximation.
9. The direct bivariate polynomial has \(AC=\Theta(W)\), outside the proved
   \(AC<W^{2/3}\) sufficient range. This is theorem-range nonapplicability
   only.
10. On odd \(K\), each balanced odd interval has
    \(K-\gcd(K,L)+1=K-o(K)\) nonzero Fourier modes. This obstructs only
    termwise materialization.
11. None of the named-model statements is a lower bound against a
    compressed exact counter, implicit CRT or MCSS, non-termwise harmonic
    evaluator, nonstandard lattice, or new integer-specific selector.

## Evidence and ledger policy

No mathematical computation, finite search, random sampling, local
experiment, remote experiment, or new public-source search was used for the
V2 repair. Hashing was used only to freeze the text.

No durable registry, proved ledger, failed ledger, progress ledger,
statement ledger, process ledger, or inspiration file was edited.

## Required fresh reviews

1. Recompute the four V2 content hashes before reading.
2. Verify the strict full-\(K\) product window and singleton quantifiers.
3. Confirm that the recursion theorem separately grants correctness and
   closure on every input and does not derive them from the balanced
   selector.
4. Check the exact interval, unit, paired-CRT, and CRT-MCSS cardinalities.
5. Reconstruct the prime-power square-root counts and the global sum-fiber
   bound.
6. Check the scaled-height convention and corrected bivariate Coppersmith
   theorem interface.
7. Check the odd-\(K\) Fourier support hypotheses.
8. Reject every universal lower-bound reading.
9. If the hostile review passes, give a different fresh agent only
   V2_STATEMENT.md and require a strict end-to-end reconstruction.
