# F132 statement — kill-first audit of quasipolynomial unary all-block feedback

## Status

This is a proof-only kill-first result. It proves that the proposed source has
quasipolynomial cost. It also gives the exact row-reuse law and two arithmetic
counterexamples to stronger progress claims. It is not an all-input factoring
theorem.

Put

\[
n=\lceil\log _2(N+1)\rceil,
\qquad
L=\lceil\log _2(n+1)\rceil,
\qquad
E=2^{L^2},
\qquad
T=L^2.
\]

The conditional standalone form takes an explicit ordered list of at most
\(E\) screened canonical-inverse unit pairs. The uniform composed form starts
on the no-factor branch after the complete F130 transcript. Completely refine
all endpoints into one pairwise-coprime gcd-free basis. At each of \(T\) frozen
rounds, for every current block \(q\) and every \(1\le e\le E\), compute

\[
c_{q,e}=[q^e]_N,
\qquad
w_{q,e}=c_{q,e}^{-1}{}_{\rm can}\pmod N,
\qquad
P_{q,e}=c_{q,e}w_{q,e}.
\]

Run the direct sign screens, retain every first exact value, retain all
endpoint presentations, and batch-refine all accumulated endpoints into the
next all-block basis. After round \(T\), run the complete P66 decoder.

## Theorem 1 — the full state and decoder stay quasipolynomial

The algorithm above has deterministic bit complexity

\[
\boxed{2^{O((\log n)^4)}}.
\]

This includes every generated residue, endpoint, exact value, all gcd-free
refinements, and the final complete P66 decode. Admitting novel endpoint
blocks does not cause super-quasipolynomial state growth during the declared
\(T=L^2\) rounds.

The fixed round cap is material. This theorem does not bound an iteration
that continues until the all-block basis reaches a fixed point.

### Exact composition with F130

The same bound holds if the initial state is the **entire final F130
transcript**, not only the seed endpoints. F130 has

\[
2^{O((\log n)^4)}
\]

total endpoint and relation bits. Completely refine all of its endpoints,
retain every resulting block, and then run the \(T=L^2\) unary rounds above.
The composed algorithm still costs

\[
\boxed{2^{O((\log n)^4)}}.
\]

This composition permanently names terminal blocks supported only on novel
probe cofactors. F130 discards those blocks from its named generator basis.
Thus the new rule has a strictly larger declared generator state whenever
such a cofactor exists. It retains every F130 screen and relation before it
adds unary probes. This is a real source-operation change, but it does not
prove that any added probe is useful.

## Theorem 2 — exact base-block feedback accounting

For a unit \(c\in\{1,\ldots,N-1\}\), write

\[
P_N(c)=c\,\iota_N(c)=1+\kappa_N(c)N,
\]

where \(\iota_N(c)\) is the least positive inverse.

Let \(q\) be a current gcd-free block. Since \(q\) divides an old endpoint,
it divides at least one old exact value

\[
P_0=1+kN.
\]

Then:

1. If \(q>k\), unary feedback at exponent one is an exact duplicate:
   \[
   P_N(q)=P_0,
   \qquad
   \iota_N(q)=P_0/q.
   \]
2. If \(P_N(q)\) is new, then \(q\le k\) for every old exact value
   \(1+kN\) that contains \(q\).
3. If \(P_N(q)\) is a duplicate, the duplicate decoder direction has
   normalized root \(+1\). Its endpoint pair cannot refine the current
   all-block basis. Its new endpoint presentation can still give a proper
   direct sign gcd before it is discarded.
4. If \(P_N(q)\) is new, it does **not** necessarily reuse the old parity
   rows inside \(q\). For every prime \(r\), its exact new row entry is
   \[
   v_r(q)+v_r(\iota_N(q))\pmod2.
   \]

Thus the exhaustive exponent-one branch is:

1. a proper sign gcd returns a factor;
2. otherwise, a new exact value is retained; or
3. otherwise, the duplicate changes neither the all-block basis nor the
   normalized-root image and can be discarded.

It is not valid to call a duplicate inert before its new endpoint sign
screens run. Canonical inversion can also cancel a prime row of the fed block.

For \(e\ge2\), the claim is weaker still. After modular reduction,
\([q^e]_N\) need not be divisible by any prime divisor of the integer \(q\).
No row-reuse conclusion follows from the word provenance alone.

## Theorem 3 — exact private-row splice law

Embed all old and new columns in their common union of prime rows. Let an old
binary parity matrix have a row \(r\) supported only on old column \(v\).
Delete row \(r\) from \(v\) to get \(\widehat v\), and let \(\widehat M\) be
all other old columns with row \(r\) deleted. Append a new distinct column
\(u\), and write \(\widehat u\) for its other coordinates.

If \(u_r=0\), the old private-column coefficient remains forced to zero. A
new dependency appears exactly when

\[
\widehat u\in\operatorname{colspan}(\widehat M).
\]

If \(u_r=1\), the row equation identifies the old and new coefficients. A new
dependency using that pair appears exactly when

\[
\boxed{
\widehat u+\widehat v
\in\operatorname{colspan}(\widehat M).
}
\]

Thus parity reuse only replaces the new column by the symmetric difference of
its support with the old private column. It does not force closure. Even when
closure occurs, it does not force a non-global normalized root; P119/F131
gives an exact distinct-value global-root trap.

For a raw duplicate \(u=v\), the symmetric difference is zero, so one
dependency appears. For equal exact canonical-inverse values, that dependency
has normalized root \(+1\), and exact-value deduplication removes it.

## Theorem 4 — universe-private rows remain private under every unary round

Let \(r>(N-1)/2\) be prime. Suppose one retained exact value has odd
\(r\)-adic valuation. After global exact-value deduplication, its \(r\)-row
has degree one in the complete canonical-inverse universe. In particular,
no number of unary block-power rounds can reuse this row.

For every generated power residue \(c=[r^e]_N\), exactly one of the following
happens:

1. \(P_N(c)\) is the already retained exact value from the inverse orbit of
   \(r\); or
2. \(v_r(P_N(c))=0\).

The old column therefore remains removable by lossless degree-one peeling.
This does not prevent another part of the final matrix from having a useful
dependency.

## Certificate A — a new column can cancel the fed old row

Take

\[
N=253=11\cdot23.
\]

The old relation is

\[
26\cdot146=3796=1+15N=2^2\cdot13\cdot73.
\]

Its two endpoints refine to the basis \(\{2,13,73\}\). The block \(q=13\)
has odd valuation in the old column. Its unary feedback is

\[
13\cdot39=507=1+2N=3\cdot13^2.
\]

This exact value is new, but its \(13\)-row is zero. All four endpoint sign
screens are null:

\[
\gcd(26\pm146,N)=1,
\qquad
\gcd(13\pm39,N)=1.
\]

The two parity-column supports are

\[
\{13,73\},
\qquad
\{3\}.
\]

They have full column rank and an empty degree-one core. This refutes
“new feedback value implies reuse of the fed row.”

## Certificate B — real reuse still need not enter the current 2-core

Take

\[
N=77=7\cdot11.
\]

The old relation is

\[
4\cdot58=232=1+3N=2^3\cdot29.
\]

Its endpoints refine to the basis \(\{2,29\}\). Feed \(q=2\):

\[
2\cdot39=78=1+N=2\cdot3\cdot13.
\]

The exact value is new relative to this one-column prefix, and the row \(2\)
is genuinely reused. All endpoint sign screens are null. However, the two
column supports are

\[
\{2,29\},
\qquad
\{2,3,13\}.
\]

Rows \(29\), \(3\), and \(13\) are private. Degree-one peeling removes both
columns, so this two-column prefix has an empty 2-core and zero kernel. Later
rounds can add columns and change that conclusion.

## Certificate C — the duplicate branch is fully inert

Take

\[
N=91=7\cdot13.
\]

The old relation

\[
2\cdot46=92=1+N=2^2\cdot23
\]

refines its endpoints to \(\{2,23\}\). Feeding \(q=23\) gives

\[
23\cdot4=92.
\]

The exact value is the old value. The alternative endpoints are monomials in
the old basis, the duplicate root is \(92\equiv1\pmod {91}\), and all endpoint
sign screens are null.

## Certificate D — a duplicate presentation can direct-factor

Take

\[
N=63=3^2\cdot7.
\]

The old canonical self-pairs

\[
(8,8),\qquad 8\cdot8=64=1+N,
\]

and

\[
(62,62),\qquad 62\cdot62=3844=1+61N
\]

have no proper endpoint sign gcd. Their complete refinement exposes the
block \(q=2\). Feeding it gives

\[
2\cdot32=64,
\]

which is an exact duplicate of the first value. The duplicate changes neither
the decoder image nor the all-block basis, but its new presentation gives

\[
\gcd(2-32,63)=3.
\]

Thus direct screens must run before exact-value deduplication.

## Exact remaining gate

The source, including its composition after the full F130 transcript, is a
valid deterministic quasipolynomial candidate. Its material algorithmic
difference from F130 is that novel endpoint cofactors become future
generators. The cost theorem permits this change.

No proved progress law follows. A factoring theorem still needs an all-input
statement that the bounded unary closure produces either a direct factor or
a final P66 dependency with non-global normalized root. Relation creation,
row reuse, and a nonempty 2-core are three different gates.
