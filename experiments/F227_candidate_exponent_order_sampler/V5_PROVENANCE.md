# F227 V5 provenance

## Version origin

F227 V1 introduced the AP local-return mean and fixed-base residual-order
criterion. Its hostile audit rejected missing length and uniform-envelope
quantifiers.

V2 repaired those quantifiers. Its hostile re-audit passed the probability
and local-order results, but rejected a cost equation that stopped after one
same-size progress transition and undercounted per-trial public work.

V3 repaired the same-size potential, geometric reach-tail accounting, and
public-work multiplicities. Its hostile re-audit passed those repairs but
found a promise-closure error: `A_x=x-1` is an arbitrary even integer, not a
new balanced-semiprime input.

V4 replaced the unsupported self-recursive cost with an explicit
all-input-oracle current-node cost. Its hostile re-audit passed every
substantive argument but found a new frozen-statement error in (B6). The
words “at most” and the inequality sign had been deleted, so the statement
asserted a false exact probability.

V5 makes the sole mathematical repair requested by that audit. It restores

\[
\Pr(\text{at least one useful trial})
\le Q(n)2^{-c_0n}=2^{-\Omega(n)}.
\]

The proof already established this upper bound and is mathematically
unchanged. All other V4 definitions, premises, claims, proofs, cost
multiplicities, oracle boundaries, exclusions, and remaining gaps are
unchanged.

## Authenticated predecessor identities

### V1

- `STATEMENT.md`: `2d62d7fdad17f58f4cc6963f6b3f5345effcf70a0e38544ab1e19db08783c7a5`
- `PROOF.md`: `16faaa4592a368724f6948c2b19deff5711a134080dbf5c1b17e5ca99c9b6afe`
- `SELF_AUDIT.md`: `824e1dc642fd817e8c1ed7ba9bfde36859d7de3ac284df4f500d97d10ab5eeaa`
- `PROVENANCE.md`: `a89429adcf4e01b00436b2473de8a07a9bbaf7b1fd2ec7dcc95caed2674d7c39`
- `MANIFEST.md`: `8996c5da21be1d3ba4beac30e5ecd7a73ac6a901b46e82e6f80635090a85c244`
- `HOSTILE_AUDIT.md`: `4f63552d96acb0d2de9e2e6da7ee27677ba76fcc21ae1090de63e9f40ce46db5`

### V2

- `V2_STATEMENT.md`: `dd905a434ed69fe0fcca5b034666e46444381cf2313176c48d42b38f76e3ad57`
- `V2_PROOF.md`: `a660128940d0d2b02907ff5ef476432b06d45d3098b35426a3a19564870a3da5`
- `V2_SELF_AUDIT.md`: `78d6f17310b23306bce3392916ccf08519b4fe0d057e522a968fda343d516e4e`
- `V2_PROVENANCE.md`: `f492d02486ee670e3fb143d469610a5970c8b7f318ad2677d773b64b821d0548`
- `V2_MANIFEST.md`: `523c97d11d6d9161404f3a013f1564131b59e9b4c42e20a75eb0fbab590b072d`
- `V2_HOSTILE_REAUDIT.md`: `f7276481a7e9c9320d67d079e74d8fc695bce0a1fe08d9b93c3d5d194d5e033f`

### V3

- `V3_STATEMENT.md`: `2030573691879933e7819d6d34278dfa1b4d0aa3d2378ae3dd29845c6da5ec29`
- `V3_PROOF.md`: `758296a586c1b6e24eab1e25a455e12947f91ff1d099d6421995caf8497247e3`
- `V3_SELF_AUDIT.md`: `c31e8a7b85d74c10935a7a7db0cc4c3323dff5defb0aba076805aecf9a696d76`
- `V3_PROVENANCE.md`: `97ce5e4224c48ee844fd30c5ad2961f77bf5ba26be218e550ac505737c092ad5`
- `V3_MANIFEST.md`: `8a9daa113a30ba730f428393ab9fc3f6fddf9cd002d77f9e25395035abb5eb35`
- `V3_HOSTILE_REAUDIT.md`: `b3fe84af1ee9e6dcf50ae251e4c6c50a7167f8a6bb97828714001e81b6051d1f`

### V4

- `V4_STATEMENT.md`: `5a7b0aa093af31417ff6db68a77bd5938d6675a7f583a7c4940c9b8e9a9ab1ff`
- `V4_PROOF.md`: `02086d1f796594594fe378f045478cfc7b230aef052fdb38338e361fdecd7f23`
- `V4_SELF_AUDIT.md`: `1d7be7c40f9bedc3d1c90838acffec822e357ce9233c37ffb0a956a60210989d`
- `V4_PROVENANCE.md`: `c16a796a2aa275cd366d47b126361ef968faf0526cb02be4f22726ec9f7d00ce`
- `V4_MANIFEST.md`: `8ba0c42fc0f9d836063eaebd3c16188da5441eefbdbc87599e9fd61391e2d559`
- `V4_HOSTILE_REAUDIT.md`: `9028c12394035c1334e7dc954900ea57a883bd526a95a6379c42671ae9eab6d4`

All twenty-four hashes were recomputed before V5 was written. Every
identity matched.

## Evidence and ledger policy

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, web search, or numerical fit was performed. Hashing
and textual comparison were used only to authenticate inputs and freeze V5.

No durable registry, proved ledger, failed ledger, progress ledger,
statement ledger, inspiration file, process-lessons file, or other durable
ledger was edited.
