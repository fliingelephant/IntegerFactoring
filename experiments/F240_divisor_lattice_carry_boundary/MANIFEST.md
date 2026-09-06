# F240 frozen manifest

## Packet

- Experiment: `F240_divisor_lattice_carry_boundary`.
- Type: proof-only candidate.
- Status: self-audited; hostile audit and blind reconstruction pending.
- Numerical computation: none.
- Durable ledger edits: none.

## Frozen artifacts

| Artifact | SHA-256 |
|---|---|
| `STATEMENT.md` | `a9e57ccf65bcc793bccf844fb74216742acaecabe77d4e34ec9946ffb98015b9` |
| `PROOF.md` | `d8a1df081ee5c8c52a4515c1f0370486a8546a3a4589dce3bd76732fa0a76015` |
| `SELF_AUDIT.md` | `a7ac335219c52fb61f881eddfbc26fde16f2f7bff32fa5cd2a968b46fa8e24c2` |
| `PROVENANCE.md` | `521b31b7e210516311427ada75b6a719997ca76df9c71d9f35a8d990bc097361` |

## Exact claim boundary

1. Every divisor `B | N-1` supports the displayed exact centered-carry and
   weighted-trace identities.
2. The hidden divisor `d=gcd(p-1,q-1)` gives carry zero.  Round-half-up gives
   centers `(s_p,s_q)` for `d>=4` and `(s_p+1,s_q+1)` for `d=2`.
3. In the explicitly narrow divisor-only multiplicative grammar, `(N-1)^n`
   achieves the smallest possible P205 residual support.  Factoring
   `(N-1)/2` adds no prime support in this grammar.
4. An additive carry escape still requires a center/residue selector or a
   new additive word law.  Complete factorization does not justify complete
   divisor enumeration.

The packet proves no all-input factoring algorithm and no lower bound
outside its stated grammar.
