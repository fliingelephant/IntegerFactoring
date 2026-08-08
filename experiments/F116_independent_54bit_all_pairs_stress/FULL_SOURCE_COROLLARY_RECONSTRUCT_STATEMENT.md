# Proof-blind reconstruction: F116 full-source success corollary

## Isolation

Read only this statement and `RECONSTRUCT_INPUT.json`. Do not read another
F116 file, any F111 file, `PROVED.md`, or a candidate implementation. Do not
use a known factor of `N`, integer factorization, or a primality routine.

Write only new files whose names start with
`FULL_SOURCE_COROLLARY_RECONSTRUCT_`. Preserve every failed attempt. Use a
named hard timeout. Pin every input, source, output, log, failure, and report
with SHA-256.

## Public source prefix

The input supplies `N`, `n`, `B=n^2`, one retained-record prefix length, and
one advised raw dependency support. Use the advice only to prove that a useful
dependency exists on this fixed input.

Independently regenerate this ordered source through the supplied prefix:

1. Test `gcd(t,N)` for every `2 <= t <= B`.
2. Retain seeds `2,3,...,n` by first canonical residue.
3. Build a deterministic factor-free gcd basis of all seed endpoints. Extract
   maximal exact perfect powers. Split overlaps by gcd and exact division.
   Verify pairwise coprimality and exact endpoint reconstruction.
4. For each seed relation, use the two smallest basis blocks in either
   endpoint. Use `(u,1)` when only one block occurs.
5. Run both orientations of every frozen pair for every exponent `0..B`.
6. Then run every unordered seed pair `2 <= u < v <= n` in lexicographic
   order. For one pair, run `[u^e v]_N` and `[u v^e]_N` for every `e=0..B`.
7. Use one global first-residue set. For each newly retained residue `c`,
   compute its least positive inverse `w`, test `gcd(c-w,N)` and
   `gcd(c+w,N)`, and retain the exact value `P=c*w`.
8. Stop source regeneration only when the supplied retained-record prefix is
   reached. Verify all counts and every advised raw record.

Replay the advised raw support by exact integer multiplication. Prove that its
product is a square, that its positive root is non-global modulo `N`, and that
the two terminal gcds are proper. Do not read a supplied factor.

## Exact-value projection

Independently apply global first-occurrence exact-value deduplication to the
regenerated prefix. Delete `P=1`.

Prove the following facts, not only the final gcd:

- A raw unit column maps to zero and has global root `+1`.
- Two raw columns with the same exact value differ by a kernel direction with
  exact positive root equal to that value, hence root `+1` modulo `N`.
- These directions generate the raw-to-exact projection kernel.
- The advised raw dependency projects to a nonzero exact-value dependency
  with the same normalized root class.
- State whether every selected value is a distinct nonunit and whether its
  selected raw record is its global first occurrence.

## Full-source no-stop and no-support corollary

The actual fixed algorithm does not receive the prefix length or support. It
runs the complete source:

1. seeds and all frozen pairs as above;
2. all unordered seed pairs in lexicographic order;
3. first-residue retention and global first-exact-value deduplication;
4. a complete factor-free exact square-class decoder;
5. both terminal gcds for every vector in a complete binary kernel basis.

Reconstruct the factor-free decoder theorem. Gcd refinement of endpoint-mask
entries must produce the same exact square-class kernel as hidden prime parity
without factoring an endpoint. Prove append monotonicity for first-occurrence
exact values. Prove that the normalized root map is a homomorphism on the
kernel. Therefore, if the verified prefix has a useful projected dependency,
the complete source still has one and every complete kernel basis detects a
useful class.

This is an existence proof for the complete fixed algorithm. Do not claim that
the full source or decoder was executed unless you execute it. Clearly
separate the advised prefix verification from the no-advice algorithm whose
success it certifies.

## Complexity and boundary

Give a uniform polynomial bit-cost bound for the complete source and decoder.
Count source positions, relation-value bits, factor-free refinement size,
matrix dimensions, dependency-product bits, and all basis-root tests.

The required conclusion is only for the supplied `N`. Do not claim success on
another input, a success density, a probability law, or a factoring algorithm
for arbitrary integers. State that the certificate advice is used in the
proof, while the certified complete algorithm itself uses only `N`.
