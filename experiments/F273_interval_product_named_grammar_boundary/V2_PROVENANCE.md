# F273 V2 provenance and correction record

## Immutable V1 packet and audits

V2 is additive. It does not modify any V1 artifact.

| V1 artifact | SHA-256 |
|---|---|
| STATEMENT.md | cdc099e0a74b5d2510ac4d9b88cf965f0ef797e6bcc428ac855c3f74daec5079 |
| PROOF.md | 09978512f2e66768628df481380e059e3d6c90fc0010e5007db249322b723dc2 |
| SELF_AUDIT.md | 66218b417fa92037526d4d7b9b40a06638fd7ae7f578d5ec3176d886039a49dd |
| PROVENANCE.md | 4595033097f3b66b3b1a12e4fce1dc339bf58fbc8f1e31bcbd40cf21c34a784c |
| MANIFEST.md | 2b33fdd0d8921bccf613ef360e92dd7a604b06133de09bf8c91d944678e41786 |
| FROZEN.sha256 | bbfce77ead51db2d540d665ed620840894a317f1c96102c62a5ef8315e6df88c |
| HOSTILE_AUDIT.md | a8ff865f43d29e5af1c8956bd2c1bcb65fbf53f97339da024db4e8f2a35e0cb6 |
| BLIND_RECONSTRUCTION.md | 9bc7775fd05ec20c9f78923043857504a5795fef03966893d16535ae7a50cda9 |

The hostile V1 audit passed. The strict V1 statement-only reconstruction
failed as written while independently verifying the core boxed algebraic
identities.

## Exact V2 repairs

### Smith distinction

V1 correctly stated

\[
 \Delta_B(\operatorname{diag}(1,\ldots,B))=B!,
\]

but its prose treated that last determinantal divisor as if it were the
last Smith invariant. V2 computes

\[
 \Delta_{B-1}
 =\frac{B!}{\operatorname{lcm}(1,\ldots,B)}
\]

and therefore

\[
 d_B=\frac{\Delta_B}{\Delta_{B-1}}
 =\operatorname{lcm}(1,\ldots,B).
\]

Both \(B!\) and the lcm have gcd \(p\) with the balanced semiprime.
V2 calls them distinct factor-bearing gates and proves no evaluation
reduction between them.

### Recursion-count distinction

V1's number \(2^{t+1}-1\) is the correct base-frontier offset count.
V2 separately records the full memoized cross-resultant DAG count

\[
 \sum_{s=0}^{t}(2^{s+1}-1)=2^{t+2}-t-3.
\]

It propagates this distinction to the standalone \(R_1(M)\) expansion and
the full discriminant/resultant DAG. Every asymptotic remains
\(\Theta(M/q_0)\).

## Closest local routes

### P174/F197

F197's statement and proof hashes are

774ce7c5496c28942d6cb11814b95cc2487ae10477127d40d8609332090e49c3

and

6b30bd83a52b380c6f04e32c4839b924324b5e55688e48077265abd06e83bc84.

F197 supplies the balanced factorial gate. F273 V2 does not turn its
diagonal Smith invariant into that factorial. It records the determinant
as the factorial and the last invariant as the lcm.

### P215/F249

F249's statement and proof hashes are

2b6594484dcb394b58126398d9944ab3e6aa18f8bc2d62e462dcc6e3c18db825

and

8938898cf8118ddcee1b4831468c7f6a62a4928c35688abe61ace52ca8bd9865.

F249 identifies the remote central coefficient and upper-half
interval-product gate. F273 V2 proposes no evaluator for it.

### P178/F201

F201's statement and proof hashes are

4915cbeea9e258524ece5dcf21e115f1a6c8ef0775dd0d1b926b94cdcbda8d41

and

56dce149bdd39b545b35e695108aa8a1dd3fa0bb8cc891aaf437a95d03e82e17.

F201 proves a fixed-linear axes lemma. F273 V2's Theorem 1 is a
characteristic-zero independent-coordinate polynomial generalization. It
does not apply automatically to the actual affine jet variety.

### F263-D02 and P220/F267

The authenticated F263 V2 root, algebra, source, and result-audit hashes are

- root:
  2a41fb0ca76955522843fdc0b15c69b1b2d811a3ac79021b0518bf6da9224271;
- algebra:
  fdf72364070e5b0ded549be171afcf005dc063afe4d7179968aa58ffdbb318d6;
- source:
  05c0b87a453eb3c2c40c01bf058b0559a6ff2e9b943d16ddcf68d147b1f4c827;
- result audit:
  320427df65f9d45f63cfaf4ad93194fe7e09cc499b4bd6d86b9a5ad7fb92b976.

F273 V2 uses no F263 data. It explains why adding the full
rising-factorial discriminant alone reaches a superfactorial gate, not an
operational evaluator.

### P221/F272

The corrected F272 statement and proof hashes are

1b6c52624e5f957b2814f5e3e98572612e7cf9312b167ed117e01dddf0d4abb5

and

671c6810a753791fa7c08e3c8eec89b68a0b9fa64fc129d7263130a2b19b67d8.

P221 leaves a uniform succinct interval-product evaluator open. F273 V2
is deliberately not a lower bound for that interface.

## Imported carry boundaries

| Result | Statement SHA-256 | Proof SHA-256 |
|---|---|---|
| P173/F196 | 07d2bccb9f508248a44f39faba3bd13a87cc0b2a1bc3dafa1464c348ae871c5c | 9f6e71c1c69661ad62780f0864b8fa460bd43df9f262b2774b7d231d20bba19b |
| P174/F197 | 774ce7c5496c28942d6cb11814b95cc2487ae10477127d40d8609332090e49c3 | 6b30bd83a52b380c6f04e32c4839b924324b5e55688e48077265abd06e83bc84 |
| P177/F200 V2 | 1edaedf1e0121e4603b8502cfb2473de250366cdc4b35acb216c3be314c8b7e5 | b573b44d35d577e4c567448092997923c0a83cdeda8a1a1cb89ec9e1cf03e30b |

These results are context only. No F273 V2 theorem depends on them.

## Mathematical dependencies and exclusions

The proof uses polynomial coefficient comparison, the rank-by-minors
criterion, prime valuations of gcds and lcms, the root-difference formula
for discriminants, resultant multiplicativity, elementary factorial
telescoping, geometric sums, and the balanced-semiprime inequalities.

No external paper, web source, unproved conjecture, factor oracle, order
oracle, heuristic distribution, or research computation is used.

F273 V2 proves no general circuit lower bound, interval-product evaluator
lower bound, affine-identity lower bound, characteristic-specific lower
bound, succinct-matrix lower bound, equivalence of the factorial and lcm
gates, numerical-quasipolynomial evaluator, or integer-factoring algorithm.
