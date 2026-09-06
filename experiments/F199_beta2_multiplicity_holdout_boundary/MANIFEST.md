# F199 manifest

Status: frozen proof-only candidate.

Frozen inputs:

- `STATEMENT.md`:
  `04c309ece29db251826247c6cfee7481b9e0b1a4e17c2ef5839ee06ac73be38c`
- `PROOF.md`:
  `5324fe02ed675f4aedb5925559fa4a7cbc8d42295bbe41d33a775810d479c8f9`
- `SELF_AUDIT.md`:
  `990e2428d767a1aa6d6714a6a10f19fe975729864fba0a52c439c8719222926b`

Required fresh hostile audit before promotion:

1. verify every frozen hash;
2. reconstruct the exact P175 balanced-semiprime promise, precision, and
   known-residue-class terminal without strengthening them;
3. verify the unit-candidate parameterization, quotient-ring isomorphism,
   and unit Jacobian minor over \(\mathbb Z/2^t\mathbb Z\);
4. derive the public \(z_i\) recurrence directly, verify pointwise
   computability uses P173 at modulus parameter \(n\), and check smoothness
   at the hidden edge \(i=p-1\);
5. verify that the one-spike difference belongs only to the unavailable
   quotient transcript \(H_i\);
6. reconstruct the Reed--Muller support induction, restricted-evaluation
   injectivity, and feature-column span conclusion;
7. verify the Hasse Taylor identity, its Hamming-ball equivalence, the
   missing-neighbor contradiction, the QP ball-volume bound, and the
   distinct-point univariate multiplicity bound;
8. check that an explicit QP list containing the reciprocal target is
   terminal only through P175, and that aggregate cells with exponential
   preimages are excluded;
9. derive the paired one-bit lift formulas and the balanced representative
   inequalities, while preserving the explicit absence of primality and
   exact-product claims;
10. verify the prefix-cell indicator and confirm that a one-child adaptive
    chain remains open and requires no fixed-ratio contraction; and
11. audit every nonclaim, especially the exclusions for nonlocal integer
    features, adaptive cell syndromes, nonlinear embeddings, and sparse
    high-degree circuits.

The manifest does not hash itself. Its observed SHA-256 must be reported
with the frozen packet. No experimental mathematical computation or
durable-ledger edit was used.
