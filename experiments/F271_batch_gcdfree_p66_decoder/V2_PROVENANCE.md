# F271 V2 provenance

## 1. Immutable V1 base

F271 V2 is an additive repair. It does not modify any V1 byte. Its immutable
base is:

| Artifact | SHA-256 |
|---|---|
| `FROZEN.sha256` | `bf3905d8ee94b8c4841eb60e4bcd2790090c30c0b5532c96d2f5f38fea68fb7b` |
| `MANIFEST.md` | `a0cf849a135252fcd16ccf2774402ff7492be07656186d2b572598d719f1e4b1` |
| `STATEMENT.md` | `19b288038c4f9e339d3f56e51fb1c6d7277fd9e322e486f2339edd0c68bf64ba` |
| `PROOF.md` | `f65e65cd649d3e787fc452abf270142e9c790d424328c52b6e3d678fc7e77b24` |
| `SELF_AUDIT.md` | `210157a033acf41c0a0dd7efdd24efb326553e6a1c862587b0e2bb4d8e6331ea` |
| `PROVENANCE.md` | `d4495b9bcad39897ec12d02d5cb85c34989416776c36a462bf1cd479a3645877` |
| `sanity_check.cpp` | `70bb7398fe927c270f30f3961d72f8af408e845e784b06b3da113d94466a2c19` |

## 2. Pinned V1 verification reports

The V1 hostile audit is

```text
HOSTILE_AUDIT.md
SHA-256 9e8279e7814fe184b2effb950af8be48959d1c415bb7d7e58536fc8f168331be
Verdict FAIL as written
```

It found two local boundary defects: negative terminal-tree coefficients at
the legal empty block list, and an unstated representation bound for supplied
modular roots. It passed the core decoder and the maximum F265 call cap.

The V1 proof-blind reconstruction is

```text
BLIND_RECONSTRUCTION.md
SHA-256 059b07104df60baa6f4590488a67ccdd20212827907733015c86e0e65ed21313
Verdict PASS
```

It reconstructed the theorem from `STATEMENT.md` alone and interpreted the
term “residue” as a canonical representative. It did not inspect the V1
proof containing the negative empty-tree coefficients.

These reports are preserved evidence about V1. They are not hostile or
blind verification of V2.

## 3. Exact V2 repair choice

V2 chooses canonical supplied roots `0<=v_i<N`. It does not introduce a new
input-length parameter. The empty terminal tree is handled by the exact case
`S=0`, with the uniform abbreviation `delta_S=max(S-1,0)`.

The corrected terminal contribution is

\[
 [S+\delta_S]M(2R)+2\delta_SQ(2R)+SQ(2r)+SG(r).
\]

This equals the V1 expression for every `S>=1` and is zero for `S=0`.

## 4. Unchanged evidence and scope

The checker, its GMP dependency, its expected output, the primorial
certificates, and every V1 theorem-level construction are unchanged. V2 did
not run local or remote computation and did not use a corpus. No source,
ledger, registry, progress file, proved-results file, failed-results file,
or predecessor artifact was edited.

V2 remains a proof-only decoder candidate. Fresh V2 hostile audit and fresh
V2 proof-blind reconstruction are required before its label can advance.
