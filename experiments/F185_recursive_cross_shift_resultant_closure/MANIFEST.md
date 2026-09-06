# F185 manifest

- ID: `F185`
- Family: strong-induction cross-shift resultant closure
- Status: proof-only candidate; fresh hostile audit pending
- Required promoted premise: P161 rough-order normalization
- Closest frozen candidates: F180, F182, F183, and F184
- Main claim: under a fixed bit-contraction hypothesis, double global
  extinction across two separated shift menus recursively yields a fully
  factored common annihilator, hence a factor or exact common order.
- Exact contraction: every recursive resultant has bit length at most
  `floor(rho*n)` for one fixed `0 < rho < 1`.
- Exact menu range: `L` is numerical QP and
  `K(1 + K*ceil(log2(2L+2))) <= floor(rho*n)`.
- Recursive cost: at most `L^2(K+1)^2` children per node; the full
  fixed-contraction tree has QP cost.
- Surviving boundary: one P161-rough descendant can remain long and unit
  for every shift in one complete menu.
- Carry boundary: only the narrow canonical inverse-carry coprimality lemma
  is included.
- Computation or checker: none
- Durable ledgers edited: none

## Frozen hostile-audit inputs

- `STATEMENT.md`:
  `f4fca86df79a72d473cc3e8dd943140978d1422efb6b2f2af324bd94076a555b`
- `PROOF.md`:
  `98c4ad7dc7fafb7466bf1a6e2384c20ec86f4d6f29c4c8394749bcc9c5583491`
- `SELF_AUDIT.md`:
  `c49347914d99db86cbd60a5727b63411876dc7b30d946dfae54e348ff248ec54`

The three files above are frozen as one candidate version. Any mathematical
change requires new hashes and a new hostile audit. `MANIFEST.md` records
the freeze but is not an input to the mathematical audit.
