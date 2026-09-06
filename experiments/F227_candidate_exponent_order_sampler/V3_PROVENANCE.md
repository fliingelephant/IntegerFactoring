# F227 V3 provenance

## Version origin

F227 V1 introduced the AP mean for local return probabilities and the
fixed-base residual-order criterion. Its hostile audit failed only because
`n`, numerical QP, and one uniform adaptive envelope were not defined.

F227 V2 repaired those quantifiers. Its hostile re-audit authenticated and
validated the following mathematical content:

- the AP divisor-average bound;
- the exact one-trial local-return upper bound;
- the fixed-envelope adaptive exponential obstruction;
- the exact fixed-base return progression and stale classification; and
- the P161 rough residual dichotomy.

The V2 re-audit returned **FAIL** only because equation (C4) counted one
progress transition as a complete current node. A useful transition can
strictly enlarge `L` without factoring, so later same-size states were
omitted. V2 also charged one copy of public work after allowing QP-many
trials.

Both failed packets and both audits remain unchanged. V3 is a new proof-only
packet.

## Exact V3 repair

V3 partitions work into:

1. recursive factorization of one half-size `A_x` per trial;
2. public work once per candidate trial;
3. public initialization once per same-size state; and
4. final terminal and verification work.

A strict lcm update at least doubles `L`. The exact terminal potential bounds
the number of same-size states by

\[
R_N(L_0)\le\lceil\log_2J_N\rceil=O(n).
\]

The repaired recurrence is

\[
F(n)
\le
R_N(L_0)\left[
2Q(n)F(n/2+C_0)
+2Q(n)P_{\rm tr}(n)
+P_{\rm st}(n)
\right]+G(n),
\]

and hence

\[
F(n)
\le
C_2nQ(n)F(n/2+C_0)+C_2nQ(n)^2.
\]

Unrolling over halved input sizes gives
`2^O((log(n+1))^(K+1))`. This is a conditional numerical-QP conclusion.
The missing nonstale-base source remains explicit.

## Preserved predecessor identities

- V1 `STATEMENT.md`:
  `2d62d7fdad17f58f4cc6963f6b3f5345effcf70a0e38544ab1e19db08783c7a5`
- V1 `PROOF.md`:
  `16faaa4592a368724f6948c2b19deff5711a134080dbf5c1b17e5ca99c9b6afe`
- V1 `SELF_AUDIT.md`:
  `824e1dc642fd817e8c1ed7ba9bfde36859d7de3ac284df4f500d97d10ab5eeaa`
- V1 `PROVENANCE.md`:
  `a89429adcf4e01b00436b2473de8a07a9bbaf7b1fd2ec7dcc95caed2674d7c39`
- V1 `MANIFEST.md`:
  `8996c5da21be1d3ba4beac30e5ecd7a73ac6a901b46e82e6f80635090a85c244`
- V1 `HOSTILE_AUDIT.md`:
  `4f63552d96acb0d2de9e2e6da7ee27677ba76fcc21ae1090de63e9f40ce46db5`
- V2 `V2_STATEMENT.md`:
  `dd905a434ed69fe0fcca5b034666e46444381cf2313176c48d42b38f76e3ad57`
- V2 `V2_PROOF.md`:
  `a660128940d0d2b02907ff5ef476432b06d45d3098b35426a3a19564870a3da5`
- V2 `V2_SELF_AUDIT.md`:
  `78d6f17310b23306bce3392916ccf08519b4fe0d057e522a968fda343d516e4e`
- V2 `V2_PROVENANCE.md`:
  `f492d02486ee670e3fb143d469610a5970c8b7f318ad2677d773b64b821d0548`
- V2 `V2_MANIFEST.md`:
  `523c97d11d6d9161404f3a013f1564131b59e9b4c42e20a75eb0fbab590b072d`
- V2 `V2_HOSTILE_REAUDIT.md`:
  `f7276481a7e9c9320d67d079e74d8fc695bce0a1fe08d9b93c3d5d194d5e033f`

## Evidence and ledger policy

No mathematical computation, scripted experiment, finite search, random
sampling, remote run, web search, or numerical fit was performed. Hashing is
used only to authenticate the preserved packets and freeze V3.

No durable registry, proved ledger, failed ledger, progress ledger,
statement ledger, inspiration file, or process-lessons file was edited.
