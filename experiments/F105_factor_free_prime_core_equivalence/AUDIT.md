# F105 hostile audit

## Verdict

**PASS for the advertised nonzero-row and core equivalence, for every finite
explicit batch.** No arithmetic or combinatorial counterexample exists under
the referenced complete P66 refinement.

Two conventions are necessary and must remain part of the theorem:

1. Refine only a pair whose gcd is greater than one. Continue until no such
   pair remains.
2. Compare matrices after zero rows are omitted. Equivalently, compare their
   distinct nonzero row supports before restoring multiplicities.

These conventions are consistent with “P66 gcd refinement” and with the
candidate's explicit nonzero-row statement. Without them, two stronger
literal readings fail:

- A rule that can keep selecting a coprime pair need not progress. The state
  `[(2, 001), (3, 010)]` reproduces itself.
- If all hidden zero rows are retained, the matrices can differ by zero rows
  as well as duplicate nonzero rows. For the one-entry batch `[(4, 001)]`,
  the hidden row for prime 2 is zero and the public matrix has no row.

These are definition boundaries. They do not affect rank, kernel, peeling, or
components. The sentence “They can differ only by duplicate rows” is exact
only after zero-row deletion.

## Candidate pin and audited scope

The complete candidate files read for this audit have SHA-256 hashes:

```text
b9b5da6a2c3d564b1df4470af7da31bfe5e9b86366a675104f70cb574f25a28e  DESIGN.md
441e01613248906462f223bfe7e2f2bd62ce7e96edc6e25cdc99192e6b2eafa2  RESULT.md
```

The PASS covers:

- every finite number of entries;
- every mask dimension, including dimension zero;
- zero masks, whether initial or created by xor;
- repeated integer entries and repeated masks;
- all equal and unequal prime valuations;
- every schedule of eligible gcd refinements;
- square and composite nonsquare terminal blocks;
- arbitrary hidden and public row multiplicities;
- every exhaustive degree-one peeling order; and
- full and peeled column-incidence components, including isolated columns.

The PASS does not add a source theorem, an online peeling theorem, a nonempty
core theorem, a rank-defect theorem, or a useful-root theorem.

## 1. Per-prime invariant — PASS

Let `E` be the current multiset of active entries. Entries of value one or
zero mask can be absent. For every prime \(p\), define

\[
H_p(E)=\sum_{(x,s)\in E}(v_p(x)\bmod 2)s.
\]

Select distinct active entries \((x,s)\) and \((y,t)\) with
\(d=\gcd(x,y)>1\). Put

\[
\alpha=v_p(x),\qquad \beta=v_p(y),\qquad
\gamma=v_p(d)=\min(\alpha,\beta).
\]

Their replacement contributes

\[
\gamma(s+t)+(\alpha-\gamma)s+(\beta-\gamma)t
=\alpha s+\beta t
\]

in the vector space over \(\mathbb F_2\). This identity does not assume
\(\alpha=\beta\). It includes the cases in which one valuation is zero and
the cases in which positive valuations are unequal.

An omitted value-one entry has every valuation zero. An omitted zero-mask
entry contributes zero at every prime. Thus each \(H_p\) is invariant after
all omissions. This also proves that dropping a zero-mask gcd “bridge” is
safe. The integer refinement can change, but the complete hidden parity data
cannot change.

Initially, \(H_p=r_p\). Therefore the candidate's hidden row is invariant for
every prime and every refinement schedule.

## 2. Termination and pairwise coprimality — PASS

For the proof only, let \(\Omega(x)\) count prime factors with multiplicity
and define the nonnegative integer potential

\[
P(E)=\sum_{(x,s)\in E}\Omega(x).
\]

Before any output omission, one eligible split replaces the selected
contribution by

\[
\begin{aligned}
\Omega(d)+\Omega(x/d)+\Omega(y/d)
&=\Omega(x)+\Omega(y)-\Omega(d)\\
&<\Omega(x)+\Omega(y).
\end{aligned}
\]

Omissions only decrease the new potential further. Hence every eligible step
strictly decreases \(P\), independently of the selection schedule. All
schedules terminate after at most
\(\sum_i\Omega(a_i)\leq\sum_i\log_2 a_i\) steps.

The complete rule stops exactly when no pair has gcd greater than one. The
remaining integers are therefore pairwise coprime. Repeated equal integers
cannot survive, because their gcd is the integer itself.

Selecting a gcd-one pair would not decrease this potential. This is why the
P66 eligibility condition is essential rather than cosmetic.

## 3. Exact terminal nonzero row set — PASS

Let the terminal entries be \((g_j,m_j)\). Every surviving mask is nonzero.
For a fixed prime \(p\), pairwise coprimality gives two cases:

- No \(g_j\) is divisible by \(p\). Invariance gives \(r_p=0\).
- Exactly one \(g_j\) is divisible by \(p\). If
  \(e=v_p(g_j)>0\), then invariance gives
  \(r_p=(e\bmod2)m_j\).

If \(r_p\ne0\), then \(e\) is odd. Thus \(g_j\) is nonsquare and its public
row is exactly \(m_j=r_p\). Conversely, a nonsquare \(g_j\) has at least one
prime divisor of odd valuation. For such a prime, the hidden row is the
nonzero mask \(m_j\).

Therefore

\[
\{r_p:r_p\ne0\}
=
\{m_j:g_j\text{ is nonsquare}\}
\]

as sets, for every terminal schedule. No unique integer block decomposition
is required.

This proof covers the edge cases directly:

- A terminal square block has only even valuations. It creates no hidden
  nonzero row and is correctly omitted publicly.
- A terminal composite nonsquare block has at least one odd valuation. That
  prime witnesses its public row.
- Several odd-valuation primes in one block can repeat one hidden row.
- Several coprime blocks can have equal masks and repeat one public row.
- Initial cancellations and zero masks can create hidden zero rows. They do
  not enter the nonzero-row set.

## 4. Rank and kernel — PASS

Deleting a zero row or retaining one copy of a repeated row does not change a
row span. The two matrices have the same distinct nonzero rows. Hence their
row spans, ranks, and kernels are identical.

This conclusion remains true if an implementation keeps hidden zero rows. In
that representation, the matrices differ by zero rows and duplicate rows,
not only by duplicate rows.

## 5. Degree-one peeling — PASS

For an active column set \(C\), the active degree of row \(r\) is
\(|\operatorname{supp}(r)\cap C|\). Equal rows have equal active support at
every stage. Their multiplicity cannot create or remove a degree-one event.
Zero rows always have degree zero.

If an active row has the unique active column \(c\), every kernel vector has
coordinate \(c=0\). Restriction to \(C\setminus\{c\}\) is a kernel
isomorphism. Its inverse inserts zero at coordinate \(c\). Thus every peel is
lossless.

The final column set is also independent of order. Call \(S\) stable if no
row meets \(S\) in exactly one column. Let \(S\) be any stable subset of the
current active set. If a peel deletes \(c\) using a row that meets the active
set only in \(c\), then \(c\notin S\); otherwise that row would meet \(S\)
only in \(c\). Every stable set therefore survives every peel. An exhaustive
terminal set is itself stable and contains every stable set. It is the unique
greatest stable set.

Because the public and hidden matrices have the same distinct nonzero rows,
they have the same peel transition at every active column set. They therefore
have the same unique relation-column core.

This argument requires a frozen batch. A later column can turn a current
singleton row into a row of degree two. The candidate makes no online claim.

## 6. Column components — PASS

The column graph has the mask coordinates as vertices. A nonzero row adds all
edges between columns in its support. Duplicate rows add no edge. Zero rows
add no edge. Equality of the distinct nonzero row sets therefore gives exact
equality of the graph, including isolated vertices and its connected
components.

After peeling, both presentations have the same surviving column set and the
same restricted distinct row supports. Their core graphs and core components
also agree.

## 7. Factor-free computability — PASS

The public construction needs gcd, exact division, an exact integer-square
test for each terminal block, bit operations on masks, and graph or peeling
operations. It does not need prime factorization. The \(\Omega\) function and
prime valuations occur only in the proof.

The potential bound also gives polynomially many refinement steps in the
explicit input bit length. A direct implementation can scan the finite active
list for an eligible pair. The matrix, peeling, and component computations are
polynomial in their explicit sizes.

## Exhaustive adversarial check

The bounded verifier is supplementary evidence, not a substitute for the
proof. It exhaustively checked:

- all 14,400 two-entry steps with values 2 through 16 and all masks in
  \(\mathbb F_2^3\);
- 3,200 prime cases with unequal positive valuations;
- all 121,485 multisets of at most three entries with values 2 through 12 and
  all masks in \(\mathbb F_2^3\), including zero and repeated masks; and
- all 125,321 distinct terminal-schedule outcomes reached by those batches.

For every outcome it checked pairwise coprimality, distinct nonzero row-set
equality, kernel equality with hidden zero and duplicate rows retained, all
peeling endpoints, and column components. Every batch had one peeling
endpoint. Some batches had four distinct terminal integer states, so this was
not only a single-schedule check.

The authoritative run exited zero in 1.67 seconds under a hard 120-second
timeout. The first run is preserved. It failed because the audit code copied
gcd-one entries twice in its one-step check. It was an audit implementation
failure, not a candidate counterexample.

## Independent cross-check

I derived the per-prime invariant, termination potential, terminal row-set
equivalence, and row-multiplicity argument before reading the F103 audit,
proof-blind report, or proof-blind output. I read those three permitted
artifacts only after the independent proof and bounded verifier passed. Their
arguments and finite F102/F103 core-hash comparison agree with this audit and
provide no contrary case. This F105 verdict does not rely on their fixed-input
replay.

Provenance caveat: while locating the exact P66 and degree-one definitions, I
had already opened F103's reconstruction statement. That statement restates
the theorem under audit. The proof above is self-contained and the exhaustive
verifier does not import F103, but this audit must not be described as a
strict proof-blind reconstruction.
