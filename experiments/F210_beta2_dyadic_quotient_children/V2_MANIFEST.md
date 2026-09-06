# F210 V2 manifest

Status: frozen proof-only candidate, pending a fresh hostile audit.

## Frozen V2 inputs

- `V2_STATEMENT.md`:
  `d71fadf26f194f067647d7cee3ac8bcdfbc2d84c1d518d356f0df0c1e1268fa0`
- `V2_PROOF.md`:
  `b53f7fd20fc71f3495dc04893d3ab7101db710256b751ac9948c40299faca0f9`
- `V2_SELF_AUDIT.md`:
  `27020049113063d9f39b4d3aea3f77c1c3ef34defa3d138d4e355e74e2c77ffc`
- `V2_PROVENANCE.md`:
  `02f36349f62f6a4706c66c2761fdb0d28415ee8099c6281b029dfd96aa623be5`

## Historical V1 evidence

`V2_PROVENANCE.md` authenticates the unchanged V1 files and the failed V1
hostile audit. A V2 auditor must treat `HOSTILE_AUDIT.md` as evidence about
V1 only. It is not a hostile audit of V2.

## Required fresh hostile audit before promotion

1. Open this manifest first and verify every frozen V2 hash before reading
   the frozen files.
2. Verify the V1 and V1-hostile-audit hashes recorded in
   `V2_PROVENANCE.md`. Confirm that V1 was preserved byte-for-byte.
3. Check that the domain \(m=2^t\) has \(t\ge1\) wherever evenness of
   \(m\), the first stage, finite \(2\)-adic lifts, or recursion bounds use
   it.
4. Reconstruct the P179 lift relation
   \(b=a\mathsf{xor}(K\bmod2)\), integrality, positivity, and coprimality
   without using `V2_PROOF.md`.
5. Check both child tables, the sign of \(D=K_0-K_1\), exact coalescence,
   the first \(t=1,m=2,N\equiv3\pmod4\) case, every bound in (18), common
   prime-power support, and the lcm formula in coalescence.
6. Expand the half-translation (22) and matrix identity (24), including the
   \(\delta=1\) sign. Verify \(XY-N=hF_a\).
7. Check the exact scope of odd-local path blindness. Reject any reading
   that equates raw Jacobi, higher-residue, exact-order, smoothness, or
   prime-support statistics of the two child factorizations.
8. Verify the character identity, the scaling in the public square root,
   and the absence of an unscaled-root claim.
9. Count the finite \(2\)-adic lifts independently for \(t\ge1\) and
   \(s\ge t+1\).
10. Reconstruct the repaired integer theorem from the divisor list of
    \(N=pq\). Confirm that
    \(1<X<\sqrt N<Y<N\), \(XY=N\), forces \((X,Y)=(p,q)\), and that only
    the true residue chart contains this point.
11. Recheck the V1 counterexamples \(N=77,m=2\) and \(N=91,m=2\) against
    the exact V2 wording. Confirm that V2 neither excludes trivial endpoints
    from false charts in general nor claims uniqueness under the old
    endpoint-free orientation condition.
12. In coalescence, verify that the other chart contains \((q,p)\), that
    this point reverses the strict balanced orientation, and that this fact
    is not extended to all integer points of that chart.
13. Reconstruct the simultaneous-return bridge, factor-first stripping, the
    proof of a common exact order, its coprimality with \(N\), and every P172
    hypothesis.
14. Verify the exponent-polynomial gcd and distinguish it from the
    identically zero ordinary resultant.
15. Reconstruct the late-stage bit-length bound and apply P183 only to one
    decrement spine plus fixed-ratio side calls. Confirm that early
    \(n-o(n)\)-bit sibling recursion is excluded and that the valid
    single-chain recurrence \(T(n)\le T(n-1)+Q(n)\) is preserved.
16. Audit every nonclaim. In particular, F210 V2 supplies neither a
    guaranteed selector, an efficient balanced-point test, nor a
    construction of the granted reciprocal prefix.

## Evidence class

No experimental mathematical computation or randomized evidence was used.
Hashing and formatting checks only froze the text. No durable registry,
proved ledger, failed ledger, or progress ledger was edited.

The manifest does not hash itself. Its observed SHA-256 must be reported
with the frozen packet.

