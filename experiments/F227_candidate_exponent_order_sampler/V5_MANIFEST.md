# F227 V5 frozen manifest

## Family and status

F227 V5: factor-cell exponents, AP return-probability mean, QP-diffuse
fresh-base obstruction, fixed-base residual-order progress, and an explicit
all-input-oracle current-node cost.

Frozen, self-audited, proof-only V5 candidate. **Do not promote.** No fresh
hostile re-audit, blind statement reconstruction, cross-family audit, or
human audit has run on V5.

V1, V2, V3, V4, and all four hostile FAILs remain unchanged. V5 does not
revise any historical artifact.

## Frozen V5 candidate files and SHA-256 hashes

- `V5_STATEMENT.md`
  - `b4f1ad6826f867105cd4cafaaeaa02ea6914a92ff1986be1698f10a136a457c1`
- `V5_PROOF.md`
  - `92c1869539e78b247823d89ff29d2194c63368296b13bd10ca18b6b26810ee6f`
- `V5_SELF_AUDIT.md`
  - `c462efeed83d1ac9e05b152bdbcda938bd9aed5dbeaed05a4906453b2a395ddb`
- `V5_PROVENANCE.md`
  - `eed58eca89d0d6ac97b04d4c6fb18d054b49025d3d1da5d755cae0bf340c081b`

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

## Authenticated V4 identities

- `V4_STATEMENT.md`: `5a7b0aa093af31417ff6db68a77bd5938d6675a7f583a7c4940c9b8e9a9ab1ff`
- `V4_PROOF.md`: `02086d1f796594594fe378f045478cfc7b230aef052fdb38338e361fdecd7f23`
- `V4_SELF_AUDIT.md`: `1d7be7c40f9bedc3d1c90838acffec822e357ce9233c37ffb0a956a60210989d`
- `V4_PROVENANCE.md`: `c16a796a2aa275cd366d47b126361ef968faf0526cb02be4f22726ec9f7d00ce`
- `V4_MANIFEST.md`: `8ba0c42fc0f9d836063eaebd3c16188da5441eefbdbc87599e9fd61391e2d559`
- `V4_HOSTILE_REAUDIT.md`: `9028c12394035c1334e7dc954900ea57a883bd526a95a6379c42671ae9eab6d4`

All twenty-four predecessor hashes were recomputed and matched before V5
was written.

## Sole V5 repair

The V4 proof established a conditional union-bound upper bound, but the V4
statement accidentally asserted an exact probability in (B6). V5 restores
the intended claim:

\[
\Pr(\text{at least one useful trial})
\le Q(n)2^{-c_0n}=2^{-\Omega(n)}.
\]

The prose also restores “at most.” This is the only mathematical change.
The V5 proof is mathematically identical to V4. All other definitions,
premises, claims, proofs, oracle boundaries, exclusions, and remaining gaps
are unchanged.

## Frozen material claims

1. The AP gcd mean (A3)--(A4).
2. The exact one-trial bound and QP-diffuse fresh-base obstruction
   (B1)--(B6), with (B6) explicitly an upper bound.
3. The exact fixed-base progression and nonstale success law (C1)--(C3).
4. The geometric one-state cost and exact same-size potential (C4)--(C8).
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
not a recurrence. V5 states no numerical-QP recursion theorem.

## Exact scope exclusions

V5 does not:

- produce a suitable nonstale fixed base;
- convert an inverse-QP randomized base source into an always-supplied base;
- factor arbitrary even candidate exponents without `FactorAll`;
- process fresh-base nonreturns jointly;
- cover heavy candidate laws, candidate/base coupling, or integer-biased
  bases; or
- prove the complete factoring theorem.

## Highest-risk points for fresh hostile re-audit

1. Authenticate all twenty-four predecessors and all four V5 content files
   before reading V5.
2. Confirm that (B6) is now an upper bound in both prose and mathematics.
3. Reconstruct the AP mean and the fixed-envelope asymptotic quantifiers.
4. Verify the exact fixed-base progression and stale classification.
5. Check the geometric reach-tail calculation without success-cost
   independence.
6. Check that the exact potential counts the final same-size state.
7. Confirm that every child-oracle call and every public cost has the right
   multiplicity.
8. Reject any implicit substitution of the balanced-node cost for `F_all`.
9. Regress the P161 corollary only on its named rough-descendant branch.

## Required next reviews

1. Recompute all four V5 content hashes before reading them.
2. Run a fresh hostile re-audit of V5.
3. If and only if V5 passes, run a strict statement-only reconstruction by a
   fresh agent.
4. Do not promote before both reviews pass and every frozen hash is checked.

## Evidence and ledger policy

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, web search, or numerical fit was performed. Hashing
and textual comparison were used only to authenticate inputs and freeze V5.

No durable registry, proved ledger, failed ledger, progress ledger,
statement ledger, inspiration file, process-lessons file, or other durable
ledger was edited.
