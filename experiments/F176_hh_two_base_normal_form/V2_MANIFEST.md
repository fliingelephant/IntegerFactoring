# F176 V2 manifest

## Approach-family ID

F176_hh_two_base_normal_form

## Artifact type

Proof-only candidate. No computation is used as evidence.

## Question

After specializing F174 to target \(D=n\), can every later hard source be
eliminated before it appears?

## Candidate answer

Yes. Base two alone returns a factor, an exact common-order state above
\(n\), or one normalized hard block. If its exact common order is at most
\(n\), the input is Mersenne. Composite exponent factors, and prime exponent
gives the source-free exact state \((-2,2n)\). Thus every surviving F174
hard escape is the first source integer two.

This is an exact QP source normal form. It does not factor the hard
base-two branch.

## V1 freeze

The superseded four-way theorem and its passing hostile audit are preserved
unchanged as:

- V1_STATEMENT.md:
  4258d94b09cd95dffa66a9cce67fe95b40a69706361a3ed855d7b2f7d3cf062b
- V1_PROOF.md:
  abf7ebcbf9366c49357010d464a9ce628c6796fc6d34ef058055018d963c9a72
- V1_SELF_AUDIT.md:
  21be2be518b0c61c3c2179a85ef3bcc0e54d1a25b24ee84ba24c0d75dc8ed026
- V1_MANIFEST.md:
  f043b6357292e2226c3ddbc566eb033010909f207662c20220e200f7bc809ae9
- V1_HOSTILE_AUDIT.md:
  93dc69e31c2ff313adfce55281e18db261ba32e75158dc41d413c37832d78317

## Current files

- STATEMENT.md: V2 theorem, exact outputs, QP cost, and exclusions.
- PROOF.md: stripping, Mersenne, sign-normalization, relative, and recursion
  proofs.
- SELF_AUDIT.md: scope, prime-power, cost, and V1-repair checks.

## Required next checks

1. Fresh hostile re-audit of V2.
2. Fresh statement-only reconstruction after a passing re-audit.
3. Recheck the arbitrary-prime-power order-stripping lemma.
4. Recheck the Mersenne size argument and the exact order of \(-2\).
5. Recheck the first common relative return and the identity \(L=2e\).

No durable proof ledger should be updated before those checks.
