# F265-D11 fresh hostile theory audit — PASS

## Verdict

**PASS.** I found no composition defect, false workload count, missing rate
denominator, projection error, firewall conflict, or theorem overclaim in the
authenticated D09+D10+D11 composition.

This verdict authorizes only C++17 evaluator-source drafting. It does not
authorize runner drafting, freezing, compilation, preflight, local or remote
execution, result release, or a ledger edit. Dynamic containment remains a hard
pending gate.

## Authenticated primary bytes

| Artifact | SHA-256 |
|---|---|
| `D09_DRAFT_ALGEBRA.md` | `93ee6021b969a3624cf499df5e18ea9c262e2a095a6b0634644cc1d69ee8030d` |
| `D09_DRAFT_PREREGISTRATION.md` | `3b499578678a0f71c75f52608e53f2fba7f390fb5a09a95bc20c61d09fe1c0a4` |
| `D10_DRAFT_ALGEBRA.md` | `aab2397c601b645f71da0bc79a8f58ed9ef79ea984fa7f7458ab2a49582a17a7` |
| `D10_DRAFT_PREREGISTRATION.md` | `be7e2a05a1eac6659000cdfe71469697d76b867b42cb60c1c244b06ec63afb6e` |
| `D11_DRAFT_ALGEBRA.md` | `a177438e425a20550342e7efa94ec1f70d30f40fe204640f983435dc36554f27` |
| `D11_DRAFT_PREREGISTRATION.md` | `9b477799e006a9b2bb49eebcf062917f1a3c91a9852ce8fbe825fcea1a1df23e` |

All six hashes matched the files reviewed. I read all six bytes in full.

## Audited import chain

D11 composes only the authenticated D09 and D10 bytes above. D11 replaces the
orphan D10 P222 sentence. No P222 artifact, theorem, rule, or transitive
composition remains. Earlier F265 drafts remain provenance only. They are not
composed directly. F271 V2 is the sole imported decoder theorem.

I authenticated and read the normative F271 theorem chain:

| Artifact | SHA-256 |
|---|---|
| F271 V2 `V2_FROZEN.sha256` | `5e396f4e20f54ee37ed70b19ed85a82e483247b10423a7ce58e7081e961c7a15` |
| F271 V2 `V2_MANIFEST.md` | `4057129cdb495656a63c7aa792253edf8c9fd93c476e7309b9787685813c0584` |
| F271 V2 `V2_STATEMENT.md` | `29fd1a79e569c2e4da72d3489e7385de4123e6b299241bfe46defb421c84b82c` |
| F271 V2 `V2_PROOF.md` | `5371d049eecb2451f073edb96d5bf36f99ab7be662fb48c5d8de2b2d93f10b51` |
| F271 V1 `STATEMENT.md` | `19b288038c4f9e339d3f56e51fb1c6d7277fd9e322e486f2339edd0c68bf64ba` |
| F271 V1 `PROOF.md` | `f65e65cd649d3e787fc452abf270142e9c790d424328c52b6e3d678fc7e77b24` |
| F271 `sanity_check.cpp` | `70bb7398fe927c270f30f3961d72f8af408e845e784b06b3da113d94466a2c19` |

The V2 canonical-residue repair and the `S=0`, `S=1`, and `S>=2` terminal
cases close the imported theorem boundaries used by D10 and D11. The per-bank
`91,111` scalar-gcd theorem bound remains scoped to refinement plus terminal
coprimality verification. Relation inversions and signed gcds remain separate.

I also authenticated and read the two public corpus bytes used by the finite
experiment:

| Artifact | SHA-256 | Data rows |
|---|---|---:|
| F268-D04 discovery public corpus | `8b6f8dbe4eae9aa10c042928fc19fbe20a0015487340e7478135ce6f37b5adb5` | 188 |
| F268-D04 heldout public corpus | `b4a4c976013dd62c58376b948c51a1c5c380265a46fbf932a5e0972fb6c389d5` | 296 |

Their eight marker rows per split leave exactly 180 discovery and 288 heldout
banks. I did not open either private-label file.

## Hostile audit scope

### Composition and chronology

- The D11 replacement targets close cleanly over D09 and D10. Unnamed clauses
  survive literally.
- `SOURCE_CHRONO320` preserves the production order: finish `U`, then finish
  `POWER`, then peel the complete tagged 320-row bank.
- Its proposal tape makes exactly 128 entered sampler calls, 128 accepted
  iterations, 256 limb draws, 64 proposal screens, and 64 discriminant gcds.
- The accepted curves are valid and distinct. The `U` doubling returns
  `(6,15)`. The `POWER` doubling uses the stated `5/2` slope and yields the
  displayed formula. Every admitted row root is a nonzero unit.
- The body makes 318 affine additions, 320 row-root gcds, 320 renderings, 319
  product multiplications, and all 320 peel cells.
- The positive square tape has the registered 361-bit maximum row width. It is
  fixture-only and cannot enter evaluation.

### Terminal-body separation

The terminal fixtures are below the shared production bodies and outside the
bank driver. One terminal result therefore cannot censor a later fixture call.
The exact witnesses are valid:

- `(0,1)+(0,34)` gives global infinity;
- `(0,1)+(0,6)` reaches the minus-side factor `5`;
- `(0,1)+(7,1)` reaches denominator factor `7`;
- row root `5` gives factor `5`; and
- row root `0` gives full-gcd `BANK_SKIP`.

Event-journal rendering remains charged by `rho_factor`. It is not silently
inserted into either terminal-body timer.

### Twelve added rate fixtures

Every fixture has a deterministic operand/result stream, an exact operation
counter, and a literal nonzero denominator:

| Rate | Exact denominator |
|---|---:|
| `rho_node` | 65,536 recursion nodes |
| `rho_touch` | 65,536 touches |
| `rho_leaf` | 262,144 leaf assignments |
| `rho_exp` | 262,144 coordinate updates |
| `rho_parity` | 262,144 parity cells |
| `rho_gf2` | 524,288 GF(2) word operations |
| `rho_exact_product` | 65,536 exact-product multiplications |
| `rho_mod_product` | 262,144 modular-product multiplications |
| `rho_isqrt` | 256 integer square roots |
| `rho_inverse` | 262,144 modular inversions |
| `rho_signed` | 262,144 signed gcds |
| `rho_basis_record` | 65,536 rendered records |

The fixed semantic witnesses are consistent. In particular, the exponent
outputs sum to `93,061,120` and xor to zero; every parity mask is
`6666666666666666`; dense elimination has rank 63 and all-ones kernel; inverse
results are `4`; and signed results alternate `3,5`.

The LF-terminated TSV rules, integer encodings, fixed-width masks, FNV-1a-64
rule, and SHA-256 rule make the expected result bytes materializable. The
future source packet must freeze every operand stream and every literal
checksum and digest. It must also give exact file widths and prove that the
preflight category remains within 67,108,864 bytes. A later source audit must
authenticate those bytes. No trace expectation is inferred from a timed run.

### Projection, resources, labels, and firewall

The repaired source projection is coefficient-consistent:

\[
T_{\rm source}=468(T_{\rm source\_chrono320}
+T_{\rm source\_affine\_stop3}
+T_{\rm source\_row\_stop2})+59{,}904T_{\rm rbelow128}.
\]

The factor `468` charges each registered bank for the chronological maximum
body and every separated terminal body. The sampler coefficient is exactly
`468*128=59,904`. The retained decoder coefficients match the one-pass D10
counter caps and the twelve rate denominators. The factor two still charges
evaluation and replay. The single 900-second diagnostic allowance, 1.75
projection multiplier, hard common deadline, 300-second finalization reserve,
and deliberate double charges remain explicit.

The added immutable fixtures remain conditional on a future exact-width proof.
D09's 210,632,704-byte output bound, 128 MiB per-file cap, 294,006,784-byte
directory peak, counted arenas, packet reservation ledger, sticky factor
journal, eligibility floors, and failure precedence remain consistent.

The discovery/heldout process firewall remains nonadaptive. Evaluation,
replay, and diagnostics receive public bytes only. Private bytes are staged
only after all evaluator processes exit and the public decision is sealed. The
label auditor cannot write or signal back to the evaluator. A private audit or
packaging failure releases no finite label.

### Theorem and result scope

The one-round valuation proof gives a kernel isomorphism only after
simultaneous deletion against the original row set. F271 V2 then gives a
complete decoder only for an admitted residual of at most 64 positive,
at-most-361-bit rows with canonical unit supplied roots.

The composition proves no source law, residual-size law, nonzero-kernel law,
non-global-root law, success probability, all-input factoring theorem, or
asymptotic experiment running time. A positive certificate factors only its
displayed modulus. A finite null closes only the authenticated reused corpus,
fixed mixed source, resource rules, and coverage floors. The omitted all-bank
pair controls remain omitted, so a hit remains `decoder_strict`, not globally
control-strict.

## Review boundary

I used read-only inspection and SHA-256 authentication. I did not compile or
run project code, invoke a local or remote evaluator, use a remote host, draft
source or a runner, freeze a byte, perform preflight, edit a ledger, or inspect
private heldout labels. I modified no draft, predecessor, source, runner, or
ledger while producing this report.

This audit file is outside the normative draft composition. Its SHA-256 is
reported after sealing; embedding a conventional self-hash would change the
bytes being hashed.
