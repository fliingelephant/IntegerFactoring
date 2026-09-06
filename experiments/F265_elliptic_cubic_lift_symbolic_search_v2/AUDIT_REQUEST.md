# F265-D02 independent hostile audit request

Audit this packet statically before any target command. Authenticate every
entry in `FROZEN.sha256`. Do not compile, execute the runner, generate inputs,
or inspect a corpus.

The audit must reconstruct and check:

1. the exact cubic row, carry, square-product, supplied-root, normalized-root,
   and signed-gcd laws;
2. the exact `POWER` source at `s=N-1` and every other frozen family;
3. the two-complete-curve rule, all affine exits, `BANK_SKIP`, direct factors,
   and the prohibition on partial eligible or strict banks;
4. singleton, coordinate, signed-root, equal/inverse, square-multiple, chord,
   tangent, and discriminant controls;
5. gcd-free block refinement, exact exponent reconstruction, parity matrix,
   kernel verification, integer-square verification, and every emitted
   `UNKNOWN_NOT_NEEDED` block record;
6. chord-support refinement, third-root tests, the six exact index predicates,
   aggregate counters, deterministic witness cap, and resource rejection;
7. the public `Case`/private `FactorLabel` separation, factor-free worker
   closure, public cohort schema, post-evaluation labels, and
   discovery-to-heldout byte firewall;
8. bounded prime, case, curve, residue, gcd-free, pattern, row, block,
   certificate, worker, wall, memory, disk, load, and output paths;
9. generation/evaluation/output preflight timing, CPU/RSS/counter accounting,
   work and generation ratios, and projected time/output gates; and
10. exact selection, held-out labels, output-set gates, P20 self-test scope,
    and finite-only interpretation.

Give one strict `PASS` or `FAIL`. A PASS authorizes only the frozen target
validation sequence after F258-D01 ends. It does not authorize a corpus after
any failed validation gate.
