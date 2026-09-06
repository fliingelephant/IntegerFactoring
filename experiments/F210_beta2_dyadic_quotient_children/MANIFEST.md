# F210 manifest

Status: frozen proof-only candidate.

## Frozen inputs

- `STATEMENT.md`:
  `77fea55ce6600f149a636aed9d2bc2ce788deaba47bbcec95a03e24a39430cd9`
- `PROOF.md`:
  `c754a738c21ce89f0c43ecfa5b9a96554b4b64bc23991b3258ee7fe2a885c0ea`
- `SELF_AUDIT.md`:
  `a00f07120dcda12447e556fe4529a7c1b9d9766c5bef5188a8b9ccd05f7eda28`

## Required fresh hostile audit before promotion

1. Verify every frozen hash.
2. Reconstruct the P179 lift relation
   (b=a\mathsf{xor}(K\bmod2)), positivity, and coprimality without using
   the proof.
3. Check both child tables, the sign of (D=K_0-K_1), exact coalescence,
   the first (N\equiv3\pmod4) stage, and every bound in (18).
4. Verify that common prime-power support lies in (|D|) only outside
   coalescence and that the lcm formula remains valid in coalescence.
5. Expand the half-translation (22) and matrix identity (24), including the
   (delta=1) sign.
6. Check the exact scope of odd-local path blindness. Reject any reading
   that equates raw Jacobi, higher-residue, exact-order, smoothness, or
   prime-support statistics of the two child factorizations.
7. Verify the character identity, the scaling in the public square root,
   and the absence of an unscaled-root claim.
8. Count the finite (2)-adic lifts independently. Check the oriented
   integer point and the swapped point in a coalesced state.
9. Reconstruct the simultaneous-return bridge, factor-first stripping, the
   proof of a common exact order, its coprimality with (N), and every P172
   hypothesis.
10. Verify the exponent-polynomial gcd and distinguish it from the
    identically zero ordinary resultant.
11. Reconstruct the late-stage bit-length bound and apply P183 only to one
    decrement spine plus fixed-ratio side calls. Confirm that early
    (n-o(n))-bit sibling recursion is excluded.
12. Audit every nonclaim. In particular, F210 supplies neither a guaranteed
    selector nor a construction of the granted reciprocal prefix.

## Evidence class

No experimental mathematical computation or randomized evidence was used.
Hashing and formatting checks only froze the text. No durable registry,
proved ledger, failed ledger, or progress ledger was edited.

The manifest does not hash itself. Its observed SHA-256 must be reported
with the frozen packet.
