# F156 hostile audit — PASS

## Frozen inputs

I read the complete frozen statement and proof. Their SHA-256 hashes matched
the expected values before this audit:

- `STATEMENT.md`:
  `d426df6c293fd835c85260b14fb6ddd57a99ff812a4c7b9a74b084318ed34527`;
- `PROOF.md`:
  `4024a5d8732ffec5dea0711498bf77e0accfc079868fecc82ace56c91243169d`.

I also checked the relevant promoted boundaries P118, P120, and P138, and
the statement, proof, hostile audit, and blind reconstruction of F154. I did
not modify a frozen input or a durable ledger. I ran no research
computation.

## Verdict

**PASS.** The declared source is deterministic and has bit complexity

\[
2^{O((\log n)^6)}.
\]

The sparse decorated products are public. The two dense-squareclass screen
identities are exact. The descendant-only named update gives a valid stage
bound. Excluding feedback-ledger records from every later section basis
prevents the relation-rank recurrence that would otherwise defeat the cost
proof.

The source is materially different from P118 and P120 as a declared
grammar. It is not proved to contain a semantically new residue, a forced
block split, a useful dependency, or a factor. The frozen statement says
this correctly.

Three implementation conventions are necessary and are supported by the
frozen proof:

1. represent every second coordinate `z_S` by its least positive residue
   before it becomes an integer endpoint;
2. preserve source-layer membership and all endpoint presentations when an
   exact value is deleted;
3. form the section basis only after the ordinary P118 scan of the same
   frozen named stage is complete.

Without these conventions, the size, ledger, or endpoint claims would be
ambiguous. With them, I found no counterexample to a frozen theorem.

## 1. The base section is public and correctly scoped

Every base canonical-inverse value satisfies

\[
A_i\equiv1\pmod N.
\]

Therefore it and each integer block dividing it are units modulo `N`.
Complete gcd-free refinement followed by perfect-power extraction gives
pairwise-coprime nonsquare blocks and an exact representation

\[
A_i=t_i^2Q(v_i).
\]

The supplied modular square root is `1`. Removing the exact square part
therefore gives the public decorated lift

\[
(v_i,t_i^{-1}).
\]

On the no-factor branch, P138 says that all base lifts induce one quotient
section over their parity span. Choosing actual lifts of parity-basis
records and taking their star-products is valid because the decorated group
is an elementary abelian 2-group. No factor of `N`, CRT orientation, or
hidden square root is used.

The basis must be selected from the complete base ledger available at that
stage. The natural and cost-preserving order is:

1. freeze the named basis;
2. finish the ordinary P118 word scan and append its base records;
3. refine the accumulated base exact values for decoder coordinates;
4. run P138 and choose the first-occurrence parity basis;
5. run the section-feedback scan;
6. apply the frozen endpoint batch.

This is the order used by the statement when Sections 2 and 4 are read
together. It should be retained in any implementation.

## 2. The sparse lift and dense screen are exact

For a nonempty basis subset `S`, the product

\[
e_S=(v_S,z_S)
\]

is public and satisfies

\[
z_S^2\equiv Q(v_S)\pmod N.
\]

Take `z_S` as its representative in `{1,...,N-1}` and let
`w_S=iota_N(z_S)`. Both are units below `N`, and

\[
1\le z_Sw_S<N^2,
\qquad
z_Sw_S\equiv1\pmod N.
\]

Multiplication by the unit `z_S` preserves gcd with `N`. Hence

\[
\begin{aligned}
\gcd(z_S-w_S,N)
 &=\gcd(z_S^2-1,N)
  =\gcd(Q(v_S)-1,N),\\
\gcd(z_S+w_S,N)
 &=\gcd(z_S^2+1,N)
  =\gcd(Q(v_S)+1,N).
\end{aligned}
\]

These are congruence identities inside a gcd. They do not assert exact
integer equality with the potentially large `Q(v_S)`. Thus a modular
evaluation through `z_S^2` is sufficient.

The screen is independent of the sign chosen for a basis lift. The endpoint
pair can depend on that sign through canonical representation, which is
allowed and public.

## 3. Exact-value deletion does not lose endpoint or root data

The feedback relation

\[
F_S=z_Sw_S=1+\kappa_SN
\]

has supplied modular root `1`. Two copies of the same exact integer have the
same rational squareclass vector and the same supplied root. Their duplicate
kernel direction has positive integer root equal to that exact value, which
is `1 modulo N`. It is therefore a global `+1` direction and can be deleted
from the algebraic decoder.

Exact equality does not imply equal endpoint presentations. The P120
certificate `64=8\cdot8=2\cdot32` is the standard warning. F156 avoids this
error by exposing every endpoint pair and retaining every source occurrence
before algebraic deletion.

The same rule must preserve ledger membership. If a value first occurs in
the feedback source and later occurs in the P118 source, the retained value
must acquire a base-source occurrence and become eligible for the base
section. Conversely, a feedback occurrence alone must not enter a later
section basis. This is an implementation consequence of the two-ledger
definition, not an extra mathematical assumption.

Keeping probe-only cofactors out of the named grammar is also consistent.
They remain present through their exact values and endpoint metadata for the
final decoder. The final global factor-free decode can rebuild one aligned
decoder basis from the union.

## 4. Indirect feedback does not invalidate the stage bound

Feedback can split an old named block. The resulting descendants alter the
next P118 word grammar, so the construction is adaptive. New P118 records
can then alter a later base section. This is an indirect feedback path, but
it does not cause an uncontrolled relation-rank recursion.

Let `A_0` be the fixed initial named endpoint product from P118. F156 admits
as future named generators only factors that occur in an old named block.
Thus every future named block is a divisor descendant of `A_0`. Complete
multiplicity-aware refinement is monotone: blocks split and never merge.
Every strict stage replaces at least one old block by at least two
pairwise-coprime nonunit descendants. Therefore the number of strict stages
is at most the number of prime factors of `A_0`, with multiplicity, and is
at most its bit length

\[
\Lambda_0=2^{O(L^2)}.
\]

Old endpoints need not be rescanned against later descendants. After a
complete earlier refinement, an old endpoint either contains an old block,
is coprime to it, or already split it. In the first two cases it cannot
later split a descendant; in the third case the split was already applied.

If a frozen stage gives no old-block split, the named basis is unchanged.
The ordinary base source is then unchanged, feedback records are forbidden
from the next section basis, and another stage would repeat the same menu.
Stopping is therefore valid.

The crucial restriction is not that feedback has no later effect. It is
that feedback exact values do not enlarge the relation pool from which the
next section basis is selected. If they did, a recurrence of the form
`R -> R^D` over quasipolynomially many named stages would not satisfy the
proved bound.

## 5. Every count and bit-length bound survives the augmented stages

The feedback-induced named stages still use descendants of the same
`A_0`. Hence their number of named blocks is at most
`2^{O(L^2)}`. At one stage, P118 scans at most

\[
(D+1)(ME)^D=2^{O(L^4)}
\]

base words. Multiplication by the stage count leaves

\[
R_0=2^{O(L^4)}
\]

base records over the complete run.

The base parity rank therefore satisfies `r <= R_0`. Since `D=L^2`, one
section scan has at most

\[
\sum_{j=1}^D\binom rj
\le(D+1)\max(1,r)^D
=2^{O(L^6)}
\]

candidates. The factor `2^{O(L^2)}` for all named stages does not change
the exponent.

Each modular coordinate and endpoint has `O(n)` bits. Each feedback exact
value has fewer than `2n` bits. Dense factor-free coordinates can have
quasipolynomial length, but multiplying this coordinate length by the
number of candidates is still `2^{O(L^6)}`. The same is true for basis
provenance and occurrence metadata.

Modular powering uses the bit length of an exponent. Thus the P118 bound
`e <= E=2^{L^2}` costs polynomial time in `L^2` per modular exponentiation;
it does not require `E` sequential multiplications. Gcd-free refinement,
perfect-power detection, binary elimination, modular inversion, and the
compact normalized-root decoder are polynomial in the explicit transcript
length. A polynomial in `2^{O(L^6)}` remains `2^{O(L^6)}`.

No hidden integer `Q(v_S)` expansion is needed for a direct screen. If its
factor presentation is retained, its total coordinate data is already
covered by the explicit transcript bound.

## 6. Relation to P118, P120, and F154

P118 enumerates sparse words in the current named integer generators. P120
feeds powers of one decoder block at a time for a bounded number of rounds.
F156 instead enumerates sparse products of actual relation-basis lifts. One
basis lift can contain a dense factor-free square part and a dense parity
vector. Its canonical endpoint can therefore depend on many decoder blocks,
including probe-only blocks that are not legal P118 named generators.

This is a real difference between the declared menus. The proof does not
show that every F156 residue is absent from the complete P118 residue set.
It also does not show that grammar enlargement implies better factoring
power. Calling the distinction syntactic, as the frozen statement does, is
the correct scope.

When `r <= D`, all nonzero vectors in the base span are scanned. This
exposes every nontrivial inverse representative `s_v` used by F154. The
identity representative `s_0=1` is omitted by the nonempty-subset rule, but
it cannot refine a block or create a nontrivial relation. F156 does not keep
all possible new probe-only blocks as future named generators, so it
captures F154's endpoint-refinement opportunity under its own stricter
descendant-only grammar, not every possible later grammar contemplated by
F154.

These qualifications do not weaken F156's proved source-and-cost theorem.

## 7. Exact remaining gap

The proof establishes a finite source, not a progress law. It gives no
lower bound for any of the following:

- the number of proper direct screens;
- the chance or inevitability of an old named block split;
- parity-kernel growth after the new canonical relations are retained;
- disagreement between the base section and the feedback section;
- the normalized-root image of the final union decoder.

The decisive missing statement is therefore exactly the frozen three-way
gate. A positive factoring result must force a proper screen, a productive
finite refinement chain, or a non-global final root on every surviving
input. F156 does not claim that result.
