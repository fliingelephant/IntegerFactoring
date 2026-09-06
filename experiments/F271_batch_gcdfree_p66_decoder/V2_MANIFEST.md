# F271 V2 manifest — narrow additive repair candidate

## Status

F271 V2 repairs only the two boundary defects recorded by the frozen V1
hostile audit. It does not alter any V1 byte. It imports the complete V1
statement and proof by hash, requires canonical supplied modular roots
`0<=v_i<N`, and totalizes the terminal-tree operation counts at `S=0` and
`S=1`.

The core decoder theorem, exact gcd-call formula, F265 constants, scope, and
novelty boundary are unchanged. V2 has only its author self-audit. The pinned
V1 hostile and blind reports are not V2 audits. Fresh V2 hostile review and
fresh V2 proof-blind reconstruction are required.

## V2 files

| File | SHA-256 | Role |
|---|---|---|
| `V2_STATEMENT.md` | `29fd1a79e569c2e4da72d3489e7385de4123e6b299241bfe46defb421c84b82c` | Normative additive statement and unchanged-scope boundary |
| `V2_PROOF.md` | `5371d049eecb2451f073edb96d5bf36f99ab7be662fb48c5d8de2b2d93f10b51` | Exact `S=0`, `S=1`, `S>=2` counts and canonical-residue complexity proof |
| `V2_SELF_AUDIT.md` | `3eea92643a38ad3a4893ac9f181a31feba258da82782c53ee61aecdc939e1539` | Author delta audit |
| `V2_PROVENANCE.md` | `c795f9959d75e42dcd3928ce49f5294717c5cd6ec695448a3a18e4c2b48ad404` | Immutable V1 base, pinned V1 reports, and repair history |

## Imported immutable anchors

| File | SHA-256 | Imported status |
|---|---|---|
| `FROZEN.sha256` | `bf3905d8ee94b8c4841eb60e4bcd2790090c30c0b5532c96d2f5f38fea68fb7b` | Complete V1 freeze root |
| `HOSTILE_AUDIT.md` | `9e8279e7814fe184b2effb950af8be48959d1c415bb7d7e58536fc8f168331be` | V1 hostile verdict: FAIL as written |
| `BLIND_RECONSTRUCTION.md` | `059b07104df60baa6f4590488a67ccdd20212827907733015c86e0e65ed21313` | V1 proof-blind verdict: PASS |

The V1 freeze root transitively authenticates `MANIFEST.md`, `STATEMENT.md`,
`PROOF.md`, `SELF_AUDIT.md`, `PROVENANCE.md`, and `sanity_check.cpp` at the
hashes recorded in `V2_PROVENANCE.md`.

## Exact repair

Put

\[
 \delta_S=\max(S-1,0).
\]

The terminal verifier uses exactly `S` block squarings, `delta_S` internal
modulus-tree multiplications, `2delta_S` remainder divisions, `S` final
exact divisions, and `S` terminal gcds. Its terminal bit-operation term is

\[
 [S+\delta_S]M(2R)+2\delta_SQ(2R)+SQ(2r)+SG(r).
\]

This is zero at `S=0` and is exactly the V1 expression at every `S>=1`.

Every supplied modular root is the canonical representative in `[0,N)`.
Its encoding has at most `bitlen(N)` bits. Because `m<=R`, all supplied-root
input bytes and arithmetic remain inside the unchanged
`O((R+bitlen(N))^4)` complete-decoder bound.

## Preserved claims

The following values and claims are unchanged:

1. saturation isolates complete primary parts without rational-prime
   factorization;
2. `TWO_BASE` and global insertion reconstruct exact pairwise-coprime blocks;
3. `T<=I`, `E<=V`, and `S<=I`;
4. refinement plus terminal coprimality uses at most
   `(D+1)T+m+2E+S` scalar gcd calls;
5. signature grouping and the canonical complement classify the full
   normalized-root image in at most `m` relation-root checks;
6. D05 positive-support peeling and P106 parity-degree-one peeling remain
   distinct; and
7. the maximum F265 caps remain `91,111` gcd calls per bank and
   `69,973,248` calls across 768 banks.

## Evidence boundary

No V2 checker, source implementation, corpus, remote run, ledger edit, or
production authorization is created by this packet. The unchanged V1
checker remains finite sanity evidence for the unchanged arithmetic core.
V2 is a proof-only candidate.
