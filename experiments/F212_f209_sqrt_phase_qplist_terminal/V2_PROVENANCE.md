# F212 V2 provenance

## Preserved V1

V2 does not modify or supersede the frozen bytes of any V1 artifact. At V2
creation time their hashes were:

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

The V1 audit is a self-hostile FAIL. It is preserved as historical evidence
and does not transfer as an audit of V2.

## Exact repair

The V1 failed audit found one fatal defect. V1 assumed that a public
procedure outputs a QP-size correct residue list, but did not bound that
procedure's runtime and did not explicitly treat the list as auxiliary
input. Its proof counted only list postprocessing.

V2 separates the two valid interfaces:

1. **Theorem 4A:** \(N\) and the explicit QP-size residue list are inputs.
   The theorem proves only deterministic numerical-QP postprocessing.
2. **Corollary 4B:** an end-to-end factoring conclusion additionally assumes
   a deterministic public numerical-QP list generator.

V2 also applies the V1 audit's nonfatal cleanup by changing \(m\geq1\) to
\(m\geq2\), avoiding a convention-dependent unit group modulo one.

## Bit-complexity repair

The list interface fixes an integer constant \(C\) with

\[
m_j\leq N^C.
\]

Thus each modulus and residue has \(O_C(n)\) bits. The fixed rational
\(\varepsilon\) also makes both modulus-bound comparisons exact
polynomial-bit computations. V2 explicitly counts:

- serialization and reading of at most \(Q(n)\) entries;
- syntax, count, bit-length, size, residue-range, and gcd validation;
- modular inverses and polynomial construction;
- fixed-parameter univariate Coppersmith calls;
- multiplication and proper-gcd verification; and
- the list generator itself in the end-to-end corollary.

No cost of constructing a granted auxiliary list is charged to Theorem 4A.

## Unchanged mathematical content

V2 retains V1's:

1. uniform full-torsor theorem with
   \(N\geq1024\) and
   \(\operatorname{lcm}(2,m)\leq\sqrt N/8\);
2. singleton-progression theorem;
3. exact \(K=(N-1)/2\) divisor-spike identity;
4. \(N^{1/4+\varepsilon}\) unknown-divisor Coppersmith threshold; and
5. narrowly scoped incomplete-Kloosterman and CRT-order boundaries.

The V1 self-hostile audit found these mathematical parts sound. That finding
is motivation only; V2 still requires a fresh auditor.

## Evidence and workflow

No mathematical computation, search, sampling, remote run, or web lookup was
performed for V2. Hashing is used only to freeze text.

By root-agent instruction, the author did not perform a V2 self-audit or
hostile audit. V2 must receive a fresh hostile audit. If that passes, it must
receive a separate strict statement-only reconstruction.

No durable registry, proved ledger, failed ledger, progress ledger, or
inspiration ledger was edited.
