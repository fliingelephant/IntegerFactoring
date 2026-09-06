# F154 manifest

- Date: 2026-08-11
- Type: proof-only V3 candidate
- Computation: exact finite witness arithmetic only; no search
- Durable ledgers: not edited
- Closest results: P66, P128, P129, F152 V2
- Main positive result: a polylog-dimensional failed decoder has an explicit
  quasipolynomial section completion
- Main negative result: all completion dependencies have normalized root
  \(+1\)
- Feedback boundary: integer refinement can change a later source grammar,
  but only under the stated refinement-mediated interface
- Exact witness: for \(N=77\), completion exposes the split
  \(4706=26\cdot181\), and the named-block-generated subgroup grows from
  order \(15\) to order \(30\); the current completion decoder and endpoint
  gcd screens do not factor \(77\), but the later test \(26^{15}\) produces
  the non-global root \(34\) and factors \(77\)
- Explicit nonclaim: no forced refinement, later disagreement, termination
  law, all-input exponent or order selection, or all-input factoring
  algorithm

## Frozen V1 history

- `STATEMENT.md`:
  `0b516d4b195a1a90283b6d45bccdeb9df8f23e7f3fca49765d1ec16e250de807`
- `PROOF.md`:
  `9ed20153e83b3405a0681d822b96d21f186bebd0bae85a72f530741c99db9ca8`
- `HOSTILE_AUDIT.md`:
  `dac8ba63474c264ba877f30631f54eb73ecceb7632a170d482ce55ce574fb51b`
- Hostile verdict: PASS under the narrow named-refinement interpretation.
- `BLIND_RECONSTRUCTION.md`:
  `18357fdbc649249f7d00809cd64cc195352e7a6a515c65576ab0069b48719377`
- Blind verdict: all algebra and quasipolynomial bounds pass, but the final
  claim of full future-grammar inertness is too broad.
- Frozen V1 files remain byte-identical.

## Frozen V2 repair and review history

- `V2_STATEMENT.md`:
  `8c75dd708a4c7bbd99e593e92474b266fb38c2b9ff8c07b3f17d0645583566c6`
- `V2_PROOF.md`:
  `08ef5ebd3428d93a8c6b0203667b3387e0d3367ceb8e2c182968c0a84e4b39b1`
- Repair: the later grammar can observe completion only through blocks newly
  named by joint gcd-free refinement. Under that interface, only the
  refinement-mediated feedback channel is inert when there is no admitted
  new block.
- V2 makes no claim about an arbitrary grammar that reads raw \(s_v\), raw
  \(P_v\), record count, or provenance.
- `V2_HOSTILE_REAUDIT.md`:
  `d70282b9c84de916f0626986c387fa3ee1d55fbc461739e08978db14f35a8e42`
- Hostile re-audit verdict: PASS. It accepted the repaired interface,
  algebra, cost, refinement, and subgroup claims, and read the witness as
  not factoring \(77\).
- `V2_BLIND_RECONSTRUCTION.md`:
  `bef53b27be6ceeae2dba83919f1b7035188ee50fa4ff686e8bb3506ff6034133`
- Fresh statement-only blind verdict: pass with qualifications. It verified
  all algebra, cost, and interface-restricted claims, but showed that the
  unrestricted sentence “the witness does not factor \(77\)” is false once
  the stated order is used:
  \(26^{15}\equiv34\pmod{77}\),
  \(\gcd(34-1,77)=11\), and
  \(\gcd(34+1,77)=7\).
- Frozen V2 files and both V2 reviews remain byte-identical.

## V3 repair

- `V3_STATEMENT.md`:
  `7021a1b9c509460606ea1168dc0f782e25cfa1461639ae256f41caf6147c1ef3`
- `V3_PROOF.md`:
  `b9842a0d05893360af75a4571f46738a69ca9de624ab35b64adc75ae602b13ad`
- Repair: the current completion decoder and displayed endpoint gcd screens
  do not factor \(77\). A later grammar that admits the newly named block
  \(26\) through the restricted interface can factor this finite input with
  the exponent-\(15\) power test.
- This later capability is not new modular information because
  \(26=\iota_{77}(3)\) was publicly computable before completion.
- V3 preserves the decorated-group algebra, exact inertness, distinctness,
  triple identity, quasipolynomial cost, interface restriction, and all
  no-forcing claims.
- V3 gives no all-input exponent-selection, order-finding, progress, or
  factoring law.
- `V3_HOSTILE_REAUDIT.md`:
  `d3a2ed6abe1f27bc2fe395307b30101c975e9ecd28f8cb137cc560a5ca9741f1`
- `V3_BLIND_RECONSTRUCTION.md`:
  `fa070e5d5dd4fa76e5b300f1d65ee3389c72492252f060290780dfc5f7f8f666`
- V3 review status: hostile re-audit passed and the independent
  statement-only reconstruction gave a qualified pass. The reconstruction
  notes that the newly named block `181` already has
  `gcd(181+1,77)=7`; this strengthens the finite later-capability claim and
  does not change its all-input nonclaim.
