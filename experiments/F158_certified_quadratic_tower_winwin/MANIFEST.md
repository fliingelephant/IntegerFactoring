# F158 manifest

- Date: 2026-08-11
- Type: proof-only decoder/progress candidate
- Computation: none
- Durable ledgers: not edited
- Closest results: P138, F154 V3, P139
- Main result: an explicit quadratic lift gives factor, inert membership, or
  index-two growth in both hidden components
- Compact result: a coprime quadratic lift over a certified common-order
  generator gives factor, inert membership, or a new generator of exactly
  twice the common local order
- Universal start: every odd input has the certified pair `(-1,2)`
- Capacity result: a supplied chain reaches the public square-root cutoff in
  `O(n)` compact steps
- Missing theorem: a uniform source must supply a non-inert coprime lift at
  every surviving level
- Explicit nonclaim: no source for the required non-inert lift chain and no
  factoring algorithm is proved
- Hostile audit: PASS
- `HOSTILE_AUDIT.md` SHA-256:
  `fd96fa54727beab048c380bc2673600c907ceeafb52613c748b9966c2e392170`
- Independent statement-only reconstruction: conditional theorem verified
- `BLIND_RECONSTRUCTION.md` SHA-256:
  `8b8e1213e2a054c2a4ca1481d76365e9e70ad77e20d475d11ae41093d844e837`
- Review qualification: `(-1,2)` is a universal certificate but not a
  universal viable lift state. A square root of `-1` can fail to exist, and
  the factor-or-lift source must return a factor when the next lift does not
  exist.
