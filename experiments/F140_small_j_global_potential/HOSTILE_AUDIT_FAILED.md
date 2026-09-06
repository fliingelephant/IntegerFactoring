# F140 hostile audit — FAIL

## Verdict

**FAIL.** The frozen statement and proof do not establish the advertised
selected path through the existing gcd-free all-block anchored source.

The exact integer identity

\[
\gcd(V_i,B_{i+1})=q_{i+1}
\]

is correct. It does not imply that complete gcd-free endpoint refinement
keeps the generally composite integer \(q_{i+1}\) as one current block. An
exact instance of the frozen construction at \(t=100\) has an earlier
selected endpoint whose gcd with \(q_{23}\) is the proper factor \(107\).
Thus complete refinement splits \(q_{23}\) before the construction tries to
use it as one anchored state.

The headline infinite-family statement is therefore **unproved**, not
disproved. The counterexample below refutes the construction's claimed
arbitrary-target block path and exposes a missing invariant. A different
source that explicitly retains and feeds public gcd aggregates might support
the arithmetic path, but that is a multi-block/aggregate grammar change. It
is not the frozen theorem's claimed gcd-free-block operation.

Audited frozen hashes:

- `STATEMENT.md`:
  `bd376737c22afae36c635005f3c187f7650594d0b21c99dddf0bd44916a09a29`
- `PROOF.md`:
  `0fe94581593a8ea2818ab574a1da6aa9eb3f9f107ad430057a2676abfce64388`

No `HOSTILE_AUDIT.md` pass report was created.

## 1. Fatal defect: the public gcd is not necessarily one current block

For any selected carry \(x\), write

\[
A_x=1+xN.
\]

The CRT condition at \(q_i\) gives \(q_i\mid B_i=1+k_iN\), and
\(\gcd(q_i,N)=1\). Consequently the exact incidence law is

\[
\boxed{
\gcd(q_i,A_x)=\gcd(q_i,x-k_i).
}
\tag{1}

For another base carry \(x=k_j\), the right side is one when \(j\ne i\):
every prime divisor of \(|j-i|\) divides \(D_t\), whereas \(q_i\) is one
modulo every prime divisor of \(D_t\). The proof checks this part only
implicitly.

The selected anchored carries \(K_j\) are different. For \(j<i-1\), put

\[
d=i-j-1.
\]

Direct substitution gives

\[
\boxed{
2^d(K_j-k_i)=q_i-\bigl(1+2^d(d-1)\bigr).
}
\tag{2}

The definition of \(D_t\) does not exclude common prime factors of \(q_i\)
and \(1+2^d(d-1)\). Such a factor occurs in the frozen construction.

### Exact causal counterexample at \(t=100\)

Recompute the proof's exact

\[
D_{100}=103\operatorname{rad}\!\left(
\prod_{i=0}^{100}(i+2)
\prod_{d=1}^{100}(2^d-1)
\right).
\]

It is already even. Exact Sage arithmetic gives

\[
D_{100}\equiv34\pmod {107},
\qquad
2^{23}\equiv22\pmod {107}.
\]

Hence

\[
q_{23}=2^{23}D_{100}+1
\equiv22\cdot34+1
=749
\equiv0\pmod {107}.
\tag{3}

Take the earlier selected carry \(K_{16}\). Here \(d=23-16-1=6\), so
(2) gives

\[
2^6(K_{16}-k_{23})=q_{23}-321,
\qquad
321=3\cdot107.
\]

Also \(q_{23}\equiv1\pmod3\), because \(3\mid D_{100}\). Since \(q_{23}\)
is odd, multiplication by \(2^6\) is invertible modulo \(q_{23}\). Therefore

\[
\boxed{
\gcd(q_{23},K_{16}-k_{23})
=\gcd(q_{23},321)
=107.
}
\tag{4}

Equation (1) now gives

\[
\boxed{
\gcd(q_{23},V_{16})=107.
}
\tag{5}

This is endpoint-level, not only value-level, incidence. The retained
presentation of \(V_{16}\) is

\[
V_{16}=(\lambda_{16}q_{16})z_{16}.
\]

The label conditions make \(\lambda_{16}\) coprime to every \(q_i\), and
the \(q_i\) are pairwise coprime. Thus

\[
\gcd(q_{23},\lambda_{16}q_{16})=1,
\]

so (5) forces

\[
\boxed{
\gcd(q_{23},z_{16})=107.
}
\tag{6}

The integer \(q_{23}\) has 3064 bits, so \(1<107<q_{23}\). The endpoint
\(z_{16}\) is retained before transition 22 releases \(q_{23}\) from
\(V_{22}\) and \(B_{23}\). Complete joint endpoint refinement must therefore
separate the 107 part of \(q_{23}\) from its remaining part. If the claimed
path fails before producing \(V_{16}\), it has already failed; otherwise
(6) makes it fail no later than the attempted state \(q_{23}\).

This calculation is independent of the later choice of \(P,Q\) and of the
allowed label assignment. It uses only the frozen \(D_{100}\), carry
formulas, CRT residue at \(q_{23}\), and label coprimality.

### Why the aggregate does not repair the frozen claim

The exact gcd of \(V_{22}\) and \(B_{23}\) can still return the public
integer \(q_{23}\). After complete refinement, however, that integer is a
product of two or more current pairwise-coprime blocks. It is not one current
block.

The established source distinguishes these operations:

- P118's named generator basis consists of terminal gcd-free blocks.
- P120 applies unary powers to each current block.
- P121 applies the anchor bank to each current all-block generator.
- P70 treats a selected product of current blocks as a strictly stronger
  multi-block operation.

Therefore the current anchored source cannot feed the aggregate
\(q_{23}\) merely because its product is publicly known. One can define a new
rule that permanently names every chosen public gcd aggregate and anchors
that aggregate. Such a rule is factor-free and this example uses only one
aggregate per transition, but it changes the source grammar and the meaning
of “unit block.” The frozen statement and proof do not declare or analyze
that rule.

The proof would instead need an incidence invariant of the form

\[
\gcd(q_i,e)\in\{1,q_i\}
\]

for every endpoint \(e\) retained before state \(q_i\), including every
selected earlier endpoint and, for a complete-source claim, every unselected
endpoint. Pairwise coprimality of the \(q_i\) does not provide this
invariant.

## 2. Independent CRT gap for the anchor labels

The label construction excludes prime divisors of the \(q_i\), of 2, and of
nonzero differences between selected carries. It does not exclude prime
divisors of the carries \(K_i\) themselves. Section 3 nevertheless chooses
\(b_i\) from

\[
K_i b_i\equiv-1\pmod {\lambda_i^2},
\]

which requires \(\lambda_i\nmid K_i\).

The stated exclusions do not imply this, even at unbounded target sizes.
Whenever \(p=t+3\) is prime, the proof's \(D_t\) is divisible by \(p\), so

\[
q_i\equiv1\pmod p
\qquad(0\le i\le t).
\]

For the last anchored carry,

\[
K_{t-1}=k_{t-1}+2q_{t-1}
\equiv(t+1)+2
\equiv0\pmod p.
\]

No base carry is zero modulo \(p\). For \(j<t-1\), one has
\(K_j\equiv j+4\in\{4,\ldots,t+2\}\pmod p\), so no other selected carry is
zero modulo \(p\). Therefore \(p\) divides no nonzero difference between two
selected carries. It also divides no \(q_i\), and it exceeds \(t+2\).
Thus \(p\) is an allowed label under the frozen rule, but assigning
\(\lambda_{t-1}=p\) makes the displayed inverse congruence insoluble. For
the same \(t=100\) used above, this allowed bad label is \(p=103\).

This gap is easy to repair mathematically: also exclude prime divisors of
all \(K_i\). Their total bit length is \(O(t^3)\), so the
\(O(t^4\log t)\) label bound is unchanged. The repair is absent from the
frozen files.

## 3. Checks that pass independently of the block defect

### Block arithmetic and label supply

- The proof correctly shows \(\gcd(k_i,q_i)=1\).
- The Mersenne factors in \(D_t\) correctly force the \(q_i\) to be
  pairwise coprime.
- The carries \(k_i,K_i\) are distinct.
- Excluding the stated prime divisors leaves enough label primes of size
  \(O(t^4\log t)\). Adding the missing \(K_i\) exclusions would preserve
  this bound.

These facts do not imply that a composite \(q_i\) remains one block after
joint endpoint refinement.

### Semiprime construction and size

The Linnik--Bertrand construction is sound.

1. The CRT class \(N_0\bmod R\) is reduced whenever the displayed inverses
   exist.
2. A prime \(P\equiv1\pmod R\) satisfies \(P>R\) and
   \(P=R^{O(1)}\).
3. The chosen composite \(b\) is reduced modulo \(R\), is congruent to
   \(N_0\), and has size \(R^{O(1)}\).
4. Bertrand supplies \(h>\max(P,b)\). Thus \(b\) is a reduced composite
   residue below \(Rh\).
5. Linnik applied modulo \(Rh\) gives
   \(Q\equiv b\pmod {Rh}\), with \(Q>Rh>P\) and
   \(Q=R^{O(1)}\).
6. Hence \(N=PQ\) is an odd distinct semiprime in the required CRT class,
   and \(\log N=O(\log R)=O(t^3)\).

Also \(N>R^2\), while \(R\) contains \(\prod_iq_i\). This gives
\(n=\Omega(t^2)\), the label cap \(C_t<n^3\), and
\(q_i<N/n^3\) for all sufficiently large \(t\). Together with
\(n=O(t^3)\), it gives the advertised numerical relation
\(t=\Omega(n^{1/3})\) for the constructed semiprime sizes. These size facts
do not create the missing path.

### Quantitative screen bound

The comparison

\[
\sum_i\log q_i
\;>\;4\log(C_tq_t)
\]

holds for all sufficiently large \(t\), so
\(R>(C_tq_t)^4\) is valid. For every selected canonical pair \((c,z)\), one
can orient it with \(c\le C_tq_t\). If \(p\in\{P,Q\}\) divided \(c-z\) or
\(c+z\), then \(cz\equiv1\pmod p\) would give
\(p\mid c^4-1\), impossible because \(p>R>c^4\). Thus the selected seed,
selected anchored, and named duplicate-base sign screens are null.

This argument intentionally does not cover all unselected complete-source
presentations, and the statement's scope permits an unselected presentation
to factor \(N\).

### Canonical endpoints, quotient one, and selected rank

Conditional on a valid CRT label assignment:

- \((\sigma_i,B_i/\sigma_i)\) is canonical because
  \(\sigma_i>k_i\).
- \((q_i,B_i/q_i)\) is canonical because \(q_i>k_i\).
- \((\lambda_iq_i,V_i/(\lambda_iq_i))\) is canonical because
  \(\lambda_i>2\), \(N>C_tq_t\), and the induced digit is exactly 2.
- The recurrence \(K_i=q_{i+1}+k_{i+1}\) makes
  \(\gcd(V_i,B_{i+1})=q_{i+1}\) and gives the formal P124 quotient
  \(j_i=1\).
- The selected exact values are mutually distinct because their carries are
  distinct.
- The valuation-one \(\sigma_i\) and \(\lambda_i\) rows are private in the
  selected column set, so that selected set has full binary column rank.

The first four bullets are integer facts about a public aggregate. They do
not prove that the next aggregate is one terminal gcd-free generator. The
private-row claim is also only for the selected submatrix. The frozen scope
correctly admits that unselected columns can reuse those rows or factor
\(N\).

## 4. Selected-path versus complete-source scope

The proof is appropriately explicit that it does not establish a
complete-source null, a universal selector lower bound, or a factoring
algorithm. The private-row and screen conclusions are selected-path
conclusions only.

Two phrases nevertheless need correction in any retry.

1. “Gcd-free refinement publicly names the next unit block” is false by
   (3)--(6). The accurate conclusion is that a public gcd computes the next
   **aggregate integer**.
2. If “the canonical-inverse anchored source” means the existing P120/P121
   complete source, that source freezes a block basis per round and has only
   \(T=L^2\) all-block rounds. A newly refined block is not anchored until a
   later round. Since here \(t\) grows polynomially while
   \(L^2=O((\log t)^2)\), containment in that fixed source is not proved.
   If F140 instead means a new path-specific, immediate-refinement schedule,
   the schedule and its aggregate admission rule must be stated as a new
   source.

Similarly, distinct carries prove novelty only inside the displayed
\(B_i,V_i\) set. They do not prove that an unselected complete-source
presentation did not already retain the same exact value. This does not harm
the narrow selected-submatrix arithmetic, but it prevents reading “new” as
global first occurrence.

## 5. Preserved discovery record

All manifest-listed hashes for `DISCOVERY_PLAN.md`, `search_paths.sage`, and
the four failed-run records match. `RUN.log` is empty. `OUTPUT.json` is the
preserved invalid Sage-preparser output and has the hash stated in
`RUN_LOGICAL_FAILED.md`; its embedded source hash is not the final registered
source hash. The manifest and timeout record say this explicitly. No finite
search result was used in this audit.

## Required repair boundary

A new frozen candidate must take one of two materially different routes.

1. Prove an endpoint-incidence invariant that keeps every \(q_i\) as one
   terminal block until it is used. The invariant must cover all earlier
   retained endpoints in the claimed source. The exact \(t=100\) collision
   must then be excluded by a changed construction.
2. Define a source that admits selected public gcd aggregates as generator
   states even after gcd-free refinement splits them. State its schedule,
   deduplication semantics, selector information, and cost. Do not call the
   aggregate one gcd-free block.

Either retry must also require \(\lambda_i\nmid K_i\) (or strengthen the
label exclusion set), and must distinguish selected-set novelty from global
first occurrence. It needs new statement/proof hashes and a fresh hostile
audit.
