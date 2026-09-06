# F215 frozen manifest

## Family

F215: higher-reciprocity inversion boundary after recursively factoring
`K=(N-1)/2` on the balanced beta-two branch.

## Status

Frozen, self-audited, proof-only candidate. No hostile audit, blind
reconstruction, cross-family audit, or human audit has run. It is not a
factoring algorithm and is not a general lower bound against higher
reciprocity.

## Namespace check

Before the directory was created, a repository-wide search found no F215
entry in the durable ledgers, notes, or experiment tree.

## Frozen candidate files and SHA-256 hashes

- `STATEMENT.md`
  - `ef9c59a2cda7eb7a1341d7242aa432dd50a67ba5a85fe797b0343ade470c743e`
- `PROOF.md`
  - `e6c7d1cf668baac847bf98f14dc3eb1d9a9091bc93316f9892a9ace788e33b62`
- `SELF_AUDIT.md`
  - `50de8fe6e7be5b548e83c4a53a08194dc52d7a0881ed57421c5c2ddd685adaa0`
- `PROVENANCE.md`
  - `22a59163513ce2668dc543dd9ebab35fa49db1a14700b688f4d2698378e1305c`

## Evidence class

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, or numerical fit was performed. The exact 527 witness
is verified by displayed integer identities. Public web lookup was used only
to confirm primary literature and the hypotheses of named cyclotomic and
Jacobi-sum algorithms. Hashing was used only to freeze the packet.

No durable registry, proved ledger, failed ledger, progress ledger,
statement ledger, inspiration file, or process-lessons file was changed.

## Claims frozen for audit

1. For every divisor of `K`, the cyclotomic Frobenius elements of the two
   hidden factors are exact inverses. Their decomposition subgroups and
   residue degrees agree.
2. One-dimensional ray characters give inverse values, genus characters
   give equal values, and the composite character product is public.
3. Hilbert-symbol bilinearity gives only the product with `N`; at a known
   prime dividing `K` but not the symbol order, `N` is already a local
   power by Hensel's lemma.
4. Scalar abelian transcripts built only from these products remain
   invariant under adaptive factor swap and eliminate no inverse candidate.
5. On `N=527=17*31`, cubic, quartic, octic, and genus ray labels modulo
   `K=263` are trivial on both factors. Rational cubic, quartic, and octic
   residue symbols at every prime over 263 are also trivial.
6. Every rational base returning under exponent `N-1` on this input has
   local order at most two. Mixed signs factor; equal signs give no strict
   common-order growth.
7. A coherent non-diagonal cyclotomic element in both full rational CRT
   components deterministically factors by coefficient content when the
   root order is coprime to `N`.
8. A selected-prime-ideal value alone is insufficient for coefficient
   content. The norm variant requires an explicit no-collision condition at
   every prime above the other rational factor.
9. Character traces separate inversion orbits by Fourier inversion, and
   each hidden trace is an exact divisor coefficient. A numerical-QP
   separating bank, evaluator, and decoder would therefore be a positive
   factoring transition; none is constructed here.

## Highest-risk points

1. Recheck that the coefficient-content lemma uses congruence in the full
   algebras modulo the rational primes, not at selected prime ideals.
2. Reconstruct the proof that distinct powers of a primitive root have unit
   difference in every component when the residue characteristic does not
   divide the root order.
3. Check the selected-prime-ideal norm statement for hidden collisions at
   conjugate primes.
4. Verify the exact common-order and half-order gcd formulas on both
   possible mod-four orientations of the smaller factor.
5. Verify the eighth-power residue-symbol calculation at every prime over
   263.
6. Check that transcript closure never absorbs a nonlinear trace, ordered
   CRT vector, or externally supplied orientation.
7. Reject any reading of the fixed-order 527 witness as covering the
   available order-131 characters.
8. Reject any reading of the literature comparison as a lower bound against
   arbitrary Jacobi-sum or cyclotomic-ring algorithms.

## Required fresh reviews

1. Recompute the four frozen content hashes before reading the packet.
2. Run a hostile audit against the statement and proof.
3. If it passes, run a strict statement-only reconstruction by a fresh
   agent.
4. Promote only after both reviews pass and all frozen hashes are rechecked.
