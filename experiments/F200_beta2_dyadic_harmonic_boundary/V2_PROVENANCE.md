# F200 V2 provenance

## V1 preservation

V2 was created alongside V1.  None of the following V1 files was edited
during the V2 repair:

- STATEMENT.md
- PROOF.md
- SELF_AUDIT.md
- MANIFEST.md
- HOSTILE_AUDIT.md
- BLIND_RECONSTRUCTION.md

Their observed SHA-256 hashes at the start of the repair were:

- STATEMENT.md:
  e6516eb85462f577d899bb4bfe50fd62b6ceea58e5752bb2c806208b42440713
- PROOF.md:
  0e6010f2a78e2867bb3ed37c0e4c5b0484acc698cedbd976436944fb38ef1b8b
- SELF_AUDIT.md:
  a26c2a174a9278f9a8e51059869af04a24e9658fd6f080d69b230f7ea1a8d398
- MANIFEST.md:
  329b3acdb7b78ad40966a4e6dc882524b4f1a4953fdb73d423322a85b98402df
- HOSTILE_AUDIT.md:
  24e36e3e2e5d0fee70b1d60b85678786254824b36240bbf351529a936fd8ad92
- BLIND_RECONSTRUCTION.md:
  c0e54bece3833914dbf996cbadcc8a5532b38bb2809db2995fb6512a7e63e6ed

## V1 post-freeze failure

The preserved V1 manifest declared these frozen hashes:

- STATEMENT.md:
  9277582c6c39d48f4fd2555a1797e09bb84d1ad8411a8ac8fa1c5f5d8b5535a0
- PROOF.md:
  cefcb6f82c5a74bfed67623eadb42eeb04f2309c3a577ccc3824ee50bbb48f5f
- SELF_AUDIT.md:
  a26c2a174a9278f9a8e51059869af04a24e9658fd6f080d69b230f7ea1a8d398

After that manifest was written, the statement and proof received material
additions about cyclic differences, autocorrelation, cell nonemptiness,
sampling, and auxiliary residue rings.  Their observed hashes therefore no
longer matched the frozen hashes.  The V1 hostile audit correctly returned
FAIL on this provenance defect.

The same hostile audit found one mathematical scope defect in the optional
cyclotomic corollary.  P161 has several exits.  Its rough local-order
conclusion applies only on the surviving
\(H=\gcd(w-1,N)=1\) branch.  Also, excluding a proposed extension-degree
cap \(D(n)\) requires choosing P161's roughness parameter
\(T\geq D(n)\).  V1 stated neither condition explicitly enough.

The V1 blind reconstruction read the observed V1 statement with hash
e6516eb85462f577d899bb4bfe50fd62b6ceea58e5752bb2c806208b42440713 and
returned PASS relative to its named imported interfaces.  It does not
override the hostile FAIL, authenticate the stale manifest, or count as a
V2 reconstruction.

## V2 construction and repair

V2_STATEMENT.md and V2_PROOF.md began as exact copies of the observed V1
statement and proof, not as copies of the stale-manifest versions.  V2 then
made only these mathematical changes:

1. It fixes a public integer-valued numerical-QP extension-degree cap
   \(D(n)\).
2. It invokes P160--P161 with a roughness parameter \(T\geq D(n)\).
3. It keeps the factor and factored exact common-order outcomes as separate
   exits.
4. It conditions the cyclotomic conclusion only on P161's surviving
   \(H=\gcd(w-1,N)=1\) branch.
5. It applies the local-order conclusion at the same hidden rational prime
   \(p\), and uses
   \(\operatorname{ord}_p(w)\mid\operatorname{ord}_p(2)\).

The remaining edits identify the packet as V2 and update its self-audit.
No mathematical computation, web search, new external source, or durable
ledger edit was used.

## Verification status

V2 is a frozen proof-only candidate after V2_MANIFEST.md is written.  The
V1 hostile audit and V1 blind reconstruction do not transfer.  V2 requires
a fresh hostile audit followed by a fresh statement-only reconstruction.
