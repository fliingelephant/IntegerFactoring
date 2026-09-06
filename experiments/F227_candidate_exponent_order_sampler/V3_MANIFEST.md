# F227 V3 frozen manifest

## Family and status

F227 V3: factor-cell exponents, AP return-probability mean, uniform adaptive
obstruction, fixed-base residual-order criterion, and corrected complete-node
conditional recurrence.

Frozen, self-audited, proof-only V3 candidate. **Do not promote.** No fresh
hostile re-audit, blind statement reconstruction, cross-family audit, or
human audit has run on V3.

V1, V2, and both hostile FAILs remain unchanged. V3 does not revise any
historical artifact.

## Frozen V3 candidate files and SHA-256 hashes

- `V3_STATEMENT.md`
  - `2030573691879933e7819d6d34278dfa1b4d0aa3d2378ae3dd29845c6da5ec29`
- `V3_PROOF.md`
  - `758296a586c1b6e24eab1e25a455e12947f91ff1d099d6421995caf8497247e3`
- `V3_SELF_AUDIT.md`
  - `c31e8a7b85d74c10935a7a7db0cc4c3323dff5defb0aba076805aecf9a696d76`
- `V3_PROVENANCE.md`
  - `97ce5e4224c48ee844fd30c5ad2961f77bf5ba26be218e550ac505737c092ad5`

## Preserved V1 identities

- `STATEMENT.md`:
  `2d62d7fdad17f58f4cc6963f6b3f5345effcf70a0e38544ab1e19db08783c7a5`
- `PROOF.md`:
  `16faaa4592a368724f6948c2b19deff5711a134080dbf5c1b17e5ca99c9b6afe`
- `SELF_AUDIT.md`:
  `824e1dc642fd817e8c1ed7ba9bfde36859d7de3ac284df4f500d97d10ab5eeaa`
- `PROVENANCE.md`:
  `a89429adcf4e01b00436b2473de8a07a9bbaf7b1fd2ec7dcc95caed2674d7c39`
- `MANIFEST.md`:
  `8996c5da21be1d3ba4beac30e5ecd7a73ac6a901b46e82e6f80635090a85c244`
- `HOSTILE_AUDIT.md`:
  `4f63552d96acb0d2de9e2e6da7ee27677ba76fcc21ae1090de63e9f40ce46db5`

## Preserved V2 identities

- `V2_STATEMENT.md`:
  `dd905a434ed69fe0fcca5b034666e46444381cf2313176c48d42b38f76e3ad57`
- `V2_PROOF.md`:
  `a660128940d0d2b02907ff5ef476432b06d45d3098b35426a3a19564870a3da5`
- `V2_SELF_AUDIT.md`:
  `78d6f17310b23306bce3392916ccf08519b4fe0d057e522a968fda343d516e4e`
- `V2_PROVENANCE.md`:
  `f492d02486ee670e3fb143d469610a5970c8b7f318ad2677d773b64b821d0548`
- `V2_MANIFEST.md`:
  `523c97d11d6d9161404f3a013f1564131b59e9b4c42e20a75eb0fbab590b072d`
- `V2_HOSTILE_REAUDIT.md`:
  `f7276481a7e9c9320d67d079e74d8fc695bce0a1fe08d9b93c3d5d194d5e033f`

## Exact V3 repair

The following disjoint bounds replace the overloaded V2 public-cost term:

1. `F(n/2+C_0)`: recursive complete factorization of one candidate
   exponent;
2. `P_tr(n)`: public work once per candidate trial;
3. `P_st(n)`: public work once per same-size state; and
4. `G(n)`: terminal and verification work.

One state costs at most

\[
2Q(n)(F(n/2+C_0)+P_{\rm tr}(n))+P_{\rm st}(n).
\]

The exact terminal potential gives at most

\[
R_N(L_0)=\Phi_N(L_0)\le\lceil\log_2J_N\rceil=O(n)
\]

same-size progress states. Thus the repaired complete-node recurrence is

\[
F(n)
\le
R_N(L_0)\left[
2Q(n)F(n/2+C_0)
+2Q(n)P_{\rm tr}(n)
+P_{\rm st}(n)
\right]+G(n),
\]

and, under the one fixed envelope,

\[
F(n)
\le
C_2nQ(n)F(n/2+C_0)+C_2nQ(n)^2.
\]

Its unrolling over halved input sizes is numerical QP. This counts every
recursive candidate preprocessing call and every public trial once, and it
counts every later same-size aggregate-growth state.

## Frozen material claims

1. The AP gcd mean (A3)--(A4).
2. The exact one-trial probability bound and uniform adaptive obstruction
   (B1)--(B6).
3. The exact fixed-base progression and nonstale success law (C1)--(C3).
4. The corrected all-state conditional cost (C4)--(C11).
5. The P161 rough residual dichotomy (D1).

## Exact scope

V3 treats distinct odd balanced semiprimes and the declared F220-style
per-trial channel. The cost theorem is conditional on receiving a nonstale
base of residual order at most `Q(n)` at every same-size state and recursive
node. V3 does not construct that source, process nonreturns jointly, cover
heavy candidate laws or candidate/base coupling, handle arbitrary composites
by itself, or prove the complete factoring theorem.

## Highest-risk points for fresh hostile re-audit

1. Check that `P_tr`, `P_st`, recursive child cost, and terminal cost are
   disjoint and charged at the correct multiplicities.
2. Verify the geometric one-state expectation without assuming runtime and
   success independence.
3. Verify that strict lcm growth at least doubles `L` and lowers the exact
   terminal potential.
4. Check that the number of same-size states includes a final factor state
   and is still at most `Phi_N(L_0)`.
5. Reconstruct (C9) before applying the coarse fixed-envelope bounds.
6. Unroll (C10) over the actual halved-size sequence and verify the QP
   exponent.
7. Regress all V2 probability and local-order statements without weakening
   their scope exclusions.

## Required next reviews

1. Recompute all four V3 content hashes before reading them.
2. Run a fresh hostile re-audit of V3.
3. If and only if V3 passes, run a strict statement-only reconstruction by a
   fresh agent.
4. Do not promote before both reviews pass and every frozen hash is checked.

## Evidence and ledger policy

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, web search, or numerical fit was performed. Hashing
was used only to authenticate predecessors and freeze V3.

No durable registry, proved ledger, failed ledger, progress ledger,
statement ledger, inspiration file, process-lessons file, or other durable
ledger was changed.
