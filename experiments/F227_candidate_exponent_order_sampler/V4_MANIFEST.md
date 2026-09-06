# F227 V4 frozen manifest

## Family and status

F227 V4: factor-cell exponents, AP return-probability mean, QP-diffuse
fresh-base obstruction, fixed-base residual-order progress, and an explicit
all-input-oracle current-node cost.

Frozen, self-audited, proof-only V4 candidate. **Do not promote.** No fresh
hostile re-audit, blind statement reconstruction, cross-family audit, or
human audit has run on V4.

V1, V2, V3, and all three hostile FAILs remain unchanged. V4 does not revise
any historical artifact.

## Frozen V4 candidate files and SHA-256 hashes

- `V4_STATEMENT.md`
  - `5a7b0aa093af31417ff6db68a77bd5938d6675a7f583a7c4940c9b8e9a9ab1ff`
- `V4_PROOF.md`
  - `02086d1f796594594fe378f045478cfc7b230aef052fdb38338e361fdecd7f23`
- `V4_SELF_AUDIT.md`
  - `1d7be7c40f9bedc3d1c90838acffec822e357ce9233c37ffb0a956a60210989d`
- `V4_PROVENANCE.md`
  - `c16a796a2aa275cd366d47b126361ef968faf0526cb02be4f22726ec9f7d00ce`

## Authenticated V1 identities

- `STATEMENT.md`: `2d62d7fdad17f58f4cc6963f6b3f5345effcf70a0e38544ab1e19db08783c7a5`
- `PROOF.md`: `16faaa4592a368724f6948c2b19deff5711a134080dbf5c1b17e5ca99c9b6afe`
- `SELF_AUDIT.md`: `824e1dc642fd817e8c1ed7ba9bfde36859d7de3ac284df4f500d97d10ab5eeaa`
- `PROVENANCE.md`: `a89429adcf4e01b00436b2473de8a07a9bbaf7b1fd2ec7dcc95caed2674d7c39`
- `MANIFEST.md`: `8996c5da21be1d3ba4beac30e5ecd7a73ac6a901b46e82e6f80635090a85c244`
- `HOSTILE_AUDIT.md`: `4f63552d96acb0d2de9e2e6da7ee27677ba76fcc21ae1090de63e9f40ce46db5`

## Authenticated V2 identities

- `V2_STATEMENT.md`: `dd905a434ed69fe0fcca5b034666e46444381cf2313176c48d42b38f76e3ad57`
- `V2_PROOF.md`: `a660128940d0d2b02907ff5ef476432b06d45d3098b35426a3a19564870a3da5`
- `V2_SELF_AUDIT.md`: `78d6f17310b23306bce3392916ccf08519b4fe0d057e522a968fda343d516e4e`
- `V2_PROVENANCE.md`: `f492d02486ee670e3fb143d469610a5970c8b7f318ad2677d773b64b821d0548`
- `V2_MANIFEST.md`: `523c97d11d6d9161404f3a013f1564131b59e9b4c42e20a75eb0fbab590b072d`
- `V2_HOSTILE_REAUDIT.md`: `f7276481a7e9c9320d67d079e74d8fc695bce0a1fe08d9b93c3d5d194d5e033f`

## Authenticated V3 identities

- `V3_STATEMENT.md`: `2030573691879933e7819d6d34278dfa1b4d0aa3d2378ae3dd29845c6da5ec29`
- `V3_PROOF.md`: `758296a586c1b6e24eab1e25a455e12947f91ff1d099d6421995caf8497247e3`
- `V3_SELF_AUDIT.md`: `c31e8a7b85d74c10935a7a7db0cc4c3323dff5defb0aba076805aecf9a696d76`
- `V3_PROVENANCE.md`: `97ce5e4224c48ee844fd30c5ad2961f77bf5ba26be218e550ac505737c092ad5`
- `V3_MANIFEST.md`: `8a9daa113a30ba730f428393ab9fc3f6fddf9cd002d77f9e25395035abb5eb35`
- `V3_HOSTILE_REAUDIT.md`: `b3fe84af1ee9e6dcf50ae251e4c6c50a7167f8a6bb97828714001e81b6051d1f`

All eighteen predecessor hashes were recomputed and matched before V4 was
written.

## Frozen material claims

1. The AP gcd mean (A3)--(A4).
2. The exact one-trial bound and QP-diffuse fresh-base obstruction
   (B1)--(B6).
3. The exact fixed-base progression and nonstale success law (C1)--(C3).
4. The geometric one-state cost and exact same-size potential
   (C4)--(C8).
5. The oracle-relative balanced-node cost (C9), with an external all-input
   `FactorAll` cost `F_all`.
6. The P161 rough residual dichotomy (D1)--(D2).

## Exact oracle boundary

The frozen cost statement is

\[
\begin{aligned}
\mathbb E[\operatorname{NodeCost}(N,L_0;\mathrm{FactorAll})]
\le R_N(L_0)\bigl[&2Q(n)F_{\rm all}(n/2+C_0)\\
&+2Q(n)P_{\rm tr}(n)+P_{\rm st}(n)\bigr]+G(n).
\end{aligned}
\]

`FactorAll` is a separately supplied correct Las Vegas factorer for every
positive integer. F227 does not construct it, bound it, or prove that its
cost satisfies the F227 balanced-node estimate. The displayed inequality is
not a recurrence. V4 states no numerical-QP recursion theorem.

## Exact scope exclusions

V4 does not:

- produce a suitable nonstale fixed base;
- convert an inverse-QP randomized base source into an always-supplied base;
- factor arbitrary even candidate exponents without `FactorAll`;
- process fresh-base nonreturns jointly;
- cover heavy candidate laws, candidate/base coupling, or integer-biased
  bases; or
- prove the complete factoring theorem.

## Highest-risk points for fresh hostile re-audit

1. Authenticate all eighteen predecessors and all four V4 content files
   before reading V4.
2. Reconstruct the AP mean and the fixed-envelope asymptotic quantifiers.
3. Verify the exact fixed-base progression and stale classification.
4. Check the geometric reach-tail calculation without success-cost
   independence.
5. Check that the exact potential counts the final same-size state.
6. Confirm that every child-oracle call and every public cost has the right
   multiplicity.
7. Reject any implicit substitution of the balanced-node cost for `F_all`.
8. Regress the P161 corollary only on its named rough-descendant branch.

## Required next reviews

1. Recompute all four V4 content hashes before reading them.
2. Run a fresh hostile re-audit of V4.
3. If and only if V4 passes, run a strict statement-only reconstruction by a
   fresh agent.
4. Do not promote before both reviews pass and every frozen hash is checked.

## Evidence and ledger policy

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, web search, or numerical fit was performed. Hashing
was used only to authenticate predecessors and freeze V4.

No durable registry, proved ledger, failed ledger, progress ledger,
statement ledger, inspiration file, process-lessons file, or other durable
ledger was edited.
