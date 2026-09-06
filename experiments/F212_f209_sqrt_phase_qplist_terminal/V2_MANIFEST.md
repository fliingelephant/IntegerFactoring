# F212 V2 frozen manifest

## Status

Frozen proof-only V2 candidate. No V2 self-audit, hostile audit, or blind
reconstruction has run. The author intentionally did not audit V2 after the
repair; a fresh auditor is required.

F211 remains reserved for the dyadic quotient experiment.

## Frozen V2 hashes

- V2_STATEMENT.md:
  69e0ca4f9cefb0ed41cbeaff25aa48b184d4039dffce11257baf787d8866dd99
- V2_PROOF.md:
  7cb6eb791cb05e2bb9139730bd188ca9566f890c7ce28d1f21f28e8c041708dc
- V2_PROVENANCE.md:
  8d98d62a81d5ec2290d98c8d38cb8a297dcb7734fe3bc020b2175d4fbe910096

## Preserved V1 hashes

- STATEMENT.md:
  f02027e683c21e7ca83082ac62d57b3d8df87e99f9e1ac0344ca98c6cd0a4400
- PROOF.md:
  bd91b0b05203aa4814e32970e3619def8066afd5081d9727e6c88ae1b392b878
- SELF_AUDIT.md:
  69973aa7217e5a798d8944c49a2ad86f9a62ba34b665d4aa43588804e397065c
- PROVENANCE.md:
  70a6165e013b95824428d8dbb2d860ef9df881e98ad6a4b324b9e23de6cb96bd
- MANIFEST.md:
  29efbe5eda6fda4bb7c6cc96079d02e51e055ff8091a2caaf4b35574fc083f08
- HOSTILE_AUDIT.md:
  e5ffa28f2d4f6f5b7f6621af5214b2a08ded069cd764304cd2a3d3d87595165c

The preserved V1 audit has verdict FAIL. It is historical evidence only and
does not audit V2.

## Exact V2 repair

V2 replaces the defective V1 terminal interface with:

1. a granted-auxiliary-list theorem proving only deterministic numerical-QP
   postprocessing; and
2. an end-to-end corollary which additionally requires a deterministic
   public numerical-QP list generator.

The explicit list has at most a numerical-QP number of pairs. Every modulus
satisfies \(m_j\leq N^C\) for one fixed integer \(C\), so every modulus and
residue has \(O_C(n)\) bits. The proof counts list construction in the
end-to-end interface, plus serialization, parsing, exact bound checks,
gcd-promise checks, modular inverses, polynomial construction, fixed-parameter
univariate Coppersmith calls, multiplication, and proper-gcd verification.

The granted-list theorem charges no unmentioned construction cost.

## Other V2 content

V2 also freezes:

1. the uniform full-torsor theorem for \(N\geq1024\) and
   \(\operatorname{lcm}(2,m)\leq\sqrt N/8\);
2. the exact singleton-progression theorem;
3. the exact \(K=(N-1)/2\) divisor-spike identity;
4. the \(N^{1/4+\varepsilon}\) univariate unknown-divisor Coppersmith
   threshold; and
5. incomplete-Kloosterman and adaptive-order statements scoped only as named
   method boundaries.

V2 sets \(m\geq2\) to remove V1's convention-dependent modulus-one edge.

## Evidence class and ledger policy

No mathematical computation, search, sampling, remote run, or web lookup was
used. Hashing was used only to freeze text.

No durable registry, proved ledger, failed ledger, progress ledger, or
inspiration ledger was edited.

## Required fresh review

1. Recompute the three V2 hashes before reading.
2. Verify that both list interfaces include exactly their proper costs.
3. Check all binary-length and exact-bound-comparison claims.
4. Recheck the standard degree-one unknown-divisor Coppersmith dependency.
5. Recheck the uniform constants, odd progression step, singleton criterion,
   and \(K\)-divisor identity.
6. Reject any reading of the named Kloosterman or CRT boundaries as lower
   bounds.
7. If the fresh hostile audit passes, assign a separate statement-only blind
   reconstruction.
