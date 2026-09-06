# F141 manifest — compact unreduced-presentation lift

## Frozen candidate

F141 retains \(Uw\equiv1\pmod N\) at each frozen F130 word position instead
of discarding the exact monomial \(U\) after modular reduction.  The
candidate proves:

- a factor-free exponent-vector decoder with the same deterministic
  \(2^{O((\log n)^4)}\) cost;
- an exact equivalence between canonical-plus-lifted columns and canonical
  columns plus the standard square congruences \(Uc\equiv c^2\pmod N\);
- the same-residue parity-collision lemma;
- a strict finite source-expansion certificate; and
- a distinct-residue squared-anchor theorem that gives more than \(n^2/5\)
  retained values preserving all odd rows of every named unit block
  \(q\ge N/(12n)\), on the direct/split-null branch.

It does not prove a rank defect, a non-global normalized root on every input,
or a factoring algorithm.  Fresh inverse-endpoint rows can still form a
full-rank peelable forest.

## Frozen hashes

| Artifact | SHA-256 |
|---|---|
| QUESTION.md | 0d1460de3c7f50fc221e6119cc4421996b9e3eba89f4ec8e1b5d3d6ae5a82583 |
| PREREGISTRATION.md | 63d4daa7917fad62c5b207a52c3e820016d03a59bf797315cf1917374c4cf02d |
| STATEMENT.md | 64bf45085bfef91190be4e23021e5e4bebbc6a9f48e03db56e49b087cf2b4bcf |
| PROOF.md | e0cea48fc14328f63c23d5ce56385cd6a216042da1f8e6c00bd2efe81914ae5a |
| search.py | 036e985399fd9e312a5f0f07de5dfe81400587ae56ce13833ad13fc77b306869 |
| RUN.log | c127a1a9c0a206aa7cc2d2d4285abb4791d37cf2ac8757b7b142a0ff42022ae3 |
| OUTPUT.json | c127a1a9c0a206aa7cc2d2d4285abb4791d37cf2ac8757b7b142a0ff42022ae3 |

The authoritative registered run has status PASS.  It verifies the fixed
123-bit order-collision certificate and exhausts the declared 903-input
small corpus.

## Preserved history

| Artifact | SHA-256 | Meaning |
|---|---|---|
| RUN_FAILED_SANDBOX.log | 770e06cc5187c8faab3d138bfe3d32a5c2918ea1489ff297013893db0efcf2e2 | First attempt failed before source execution because Sage could not write its default cache |
| RUN_FAILURE.md | a1afeee1921acffe646120410c0b9b483ab0acf79d905c5c0741c1c876bfd454 | Failure explanation and cache-only correction |
| RUN_V1.log | 63e762c245c62a1491a7f7c60c863a97f6e6a5e9a0d9a55a2363069753c820ad | First completed corpus run, before the all-distinct circuit condition |
| OUTPUT_V1.json | 63e762c245c62a1491a7f7c60c863a97f6e6a5e9a0d9a55a2363069753c820ad | Valid weaker output whose first all-distinct pair was a union of singleton squares |

## Verification state

The frozen candidate passed both required checks.

| Artifact | SHA-256 | Result |
|---|---|---|
| HOSTILE_AUDIT.md | d1a8f3b6f1b106452612f155d5e28ec311521b10a7459415f7b3e341587f6581 | PASS; registered replay was byte-identical and an independent implementation reproduced the corpus counts |
| BLIND_RECONSTRUCTION.md | 96199f72b55c82b79231df1202e20b13493abbc53c287b3a7dba1b1d667a9363 | PASS from the frozen statement only; inherited F130 interface assumptions were stated explicitly |

The result is verifier-backed and can be promoted. It has no cross-family,
human, or publication-level literature audit.
