# F212 manifest

## Family

F212: exact F209 square-root phase transition and QP-list terminal.

F211 remains reserved for the dyadic quotient experiment.

## Namespace check

Before the directory was created, a repository-wide search found no F212
entry in the durable ledgers, notes, or experiment tree.

## Frozen candidate files

- STATEMENT.md
  - SHA-256:
    f02027e683c21e7ca83082ac62d57b3d8df87e99f9e1ac0344ca98c6cd0a4400
- PROOF.md
  - SHA-256:
    bd91b0b05203aa4814e32970e3619def8066afd5081d9727e6c88ae1b392b878
- SELF_AUDIT.md
  - SHA-256:
    69973aa7217e5a798d8944c49a2ad86f9a62ba34b665d4aa43588804e397065c
- PROVENANCE.md
  - SHA-256:
    70a6165e013b95824428d8dbb2d860ef9df881e98ad6a4b324b9e23de6cb96bd

## Evidence class

Frozen self-audited proof-only candidate. No mathematical computation was
run. Existing F209-D01 rows were not used as proof evidence. Hashing was used
only to freeze the text.

No durable registry, proved ledger, failed ledger, progress ledger, or
inspiration ledger was changed.

## Claims frozen for audit

1. If \(N\geq1024\) and
   \(\operatorname{lcm}(2,m)\leq\sqrt N/8\), the exact F209 relaxed frontier
   is all of \(U(m)\).
2. If the odd-representative step exceeds both balanced interval spans, each
   progression is singleton and the endpoint product predicate is exactly
   \(XY=N\).
3. At the fully factored modulus \(K=(N-1)/2\), the modular-hyperbola
   condition in the balanced box is exactly the divisor-jump sum.
4. A QP-size list containing \(p\bmod m\) or \(q\bmod m\), with
   \(m\geq N^{1/4+\varepsilon}\), terminates by the proved univariate
   unknown-divisor Coppersmith theorem.
5. The incomplete-Kloosterman and adaptive-order conclusions are named
   representation boundaries only, not lower bounds.

## Highest-risk points

1. Recheck the \(1/8\), \(1024\), and interval-span constants exactly.
2. Verify that multiplication by the F207 root maps the \(u\)-frontier
   bijectively to the stated \(x\)-frontier.
3. Reconstruct the exact \(N-K<XY<N+K\) argument at \(m=K\).
4. Verify that every divisor in \([L,B]\) has its complement in \(Q\).
5. Audit the precise unknown-divisor Coppersmith theorem, including monicity,
   the hidden-divisor exponent, and the common margin for \(p\) and \(q\).
6. Reject any interpretation as a lower bound against an implicit exact
   Kloosterman evaluator, a compressed CRT state, or a new factoring method.

## Required fresh reviews

1. Recompute all four frozen content hashes before reading the packet.
2. Run a hostile audit against the statement and proof.
3. If it passes, run a strict statement-only reconstruction.
4. Promote only after both reviews pass and the frozen hashes are rechecked.
