# F271 manifest — frozen proof-only candidate

## Status

F271 is a proof-only candidate for a factor-free P66 terminal-decoder
redesign. It is not a source theorem, a production implementation, or a
factoring result. It edits no durable ledger and authorizes no F265 run.

The redesign is viable at theorem level. It removes the decoder's quadratic
block-pair and support-two arithmetic. Under the exact F265 residual boundary
`m<=64` and `bitlen(a_i)<=361`, the complete refinement and independent
terminal coprimality check use at most 91,111 gcd calls per bank and
69,973,248 calls across 768 maximum banks. The D08 cap was 7,208,878,080
calls. The reduction factor is approximately 103.02.

## Frozen candidate files

| File | SHA-256 | Role |
|---|---|---|
| `STATEMENT.md` | `19b288038c4f9e339d3f56e51fb1c6d7277fd9e322e486f2339edd0c68bf64ba` | Exact theorem, algorithms, bounds, edge cases, and novelty boundary |
| `PROOF.md` | `f65e65cd649d3e787fc452abf270142e9c790d424328c52b6e3d678fc7e77b24` | Completeness, termination, exact calls, and bit-operation proof |
| `SELF_AUDIT.md` | `210157a033acf41c0a0dd7efdd24efb326553e6a1c862587b0e2bb4d8e6331ea` | Author audit, disclosed count correction, and remaining attack surface |
| `PROVENANCE.md` | `d4495b9bcad39897ec12d02d5cb85c34989416776c36a462bf1cd479a3645877` | P66, P106, D05, D08, Bernstein, and checker provenance |
| `sanity_check.cpp` | `70bb7398fe927c270f30f3961d72f8af408e845e784b06b3da113d94466a2c19` | Deterministic finite arithmetic certificate |

`FROZEN.sha256` is the machine-readable freeze list. It includes this
manifest and every file in the table.

## Frozen claims

1. The two-sided saturation split and equal-support recursion compute exact
   pairwise-coprime blocks and exact exponent coordinates without rational-
   prime factorization.
2. Incremental insertion through a fixed dynamic product tree preserves the
   global reconstruction and coprimality invariant.
3. The recursion forest terminates and has at most
   `V=sum_{p,i} v_p(a_i)` nodes.
4. Complete refinement plus an independent terminal check uses at most
   `(D+1)T+m+2V+S` scalar gcd calls. No pairwise block scan is hidden.
5. Signature grouping computes every singleton and support-two relation,
   their exact counts, and a basis of their span without pair arithmetic.
6. A canonical structural complement plus the low basis classifies the full
   normalized-root image in at most `m` relation-root checks.
7. D05 positive-support peeling and P106 parity-degree-one peeling are
   distinct. F271 gives both rules and does not substitute one for the other.
8. Schoolbook bit complexity is `O(R^3 log R)` for refinement,
   reconstruction, and terminal verification, and conservatively
   `O((R+bitlen(N))^4)` for the complete decoder.
9. The only unavoidable quadratic decoder work is output serialization if a
   contract demands one record for every support-two hit. Separate F265
   coordinate and chord controls remain outside this redesign.

## Finite certificate

The frozen checker exhausts all 250,000 ordered pairs `1<=x,y<=500` and six
fixed large or composite edge pairs. It checks exact reconstruction,
pairwise coprimality, node charging, and internal gcd accounting. It also
checks the 58-, 1,875-, and 1,876-prime certificates and the final F265 cap
arithmetic.

The frozen command and dependency are in `PROVENANCE.md`. The run completed
with this exact output:

```text
PASS pairs=250000 max_exhaustive_pair_nodes=11 max_fixed_edge_nodes=360 p58=271 primorial58_bits=368 p1875=16103 primorial1875_bits=23102 p1876=16111 primorial1876_bits=23116 f265_gcd_calls_per_bank=91111 f265_gcd_calls_packet=69973248
```

The compiler emitted three deprecation warnings from the installed GMP
header's literal-operator declarations. It emitted no warning from the
candidate source. The checker is implementation sanity evidence, not the
general proof.

## Review boundary

Only the author's self-audit is valid evidence in this packet. A child began
to inspect mutable pre-freeze bytes and was interrupted before freeze. It
wrote no report and is not an audit. Fresh no-context review must start from
the hashes in `FROZEN.sha256`.

No remote host, random input, elliptic row, discovery corpus, held-out
corpus, production source, or production run was used. No ledger, registry,
proved-results file, failed-results file, progress file, or frozen
predecessor was edited.
