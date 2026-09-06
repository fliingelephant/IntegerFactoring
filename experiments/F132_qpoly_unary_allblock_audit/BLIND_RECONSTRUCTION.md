# Blind reconstruction of F132

## Audit protocol and verdict

I read exactly one repository file:

`experiments/F132_qpoly_unary_allblock_audit/STATEMENT.md`

Its SHA-256 hash is
`41331f37531a2303dc7c372cbabe49110450b4b2e080800c842c62fb84d79a64`.
I did not read `PROOF.md`, `MANIFEST.md`, `HOSTILE_AUDIT_FAILED.md`, or any
other F132 artifact. The arithmetic checks below were derived independently
from the statement.

**Verdict: PASS.** The fixed-round source has deterministic bit complexity

\[
2^{O((\log n)^4)}.
\]

The feedback identities, private-row splice, universe-private theorem, and
four certificates are correct. This verdict does not make the source an
all-input factoring algorithm. The missing item is still a bounded-round
progress theorem.

Throughout, put

\[
n=\lceil\log _2(N+1)\rceil,\qquad
L=\lceil\log _2(n+1)\rceil,\qquad
E=2^{L^2},\qquad T=L^2.
\]

All logarithms in cost estimates can be changed between fixed bases at a
constant-factor cost.

## 1. Quasipolynomial state and time

### 1.1 A size lemma for a complete gcd-free basis

Let the accumulated endpoints be (x_1,\ldots,x_s<N), and let
(b_1,\ldots,b_m>1) be their pairwise-coprime gcd-free basis. Every (b_j)
divides at least one endpoint. Assign it to one such endpoint. The product of
all basis blocks assigned to (x_i) divides (x_i), because those blocks are
pairwise coprime. Hence

\[
\sum_{j=1}^m\log _2 b_j
 \le \sum_{i=1}^s\log _2 x_i<sn.
\]

In particular, (m\le sn). More generally, (m) is at most the accumulated
endpoint bit length. This remains true when a new endpoint splits an old
block or introduces a block supported only on a novel cofactor.

Every current block is a divisor of an endpoint less than (N), so it is
itself less than (N). Since all endpoints are units modulo (N), every
block is also a unit. Thus all requested canonical inverses exist.

### 1.2 The raw-state recurrence

Let (U_t\ge1) be the total explicit bit length of all accumulated endpoint
records immediately before round (t). Include a fixed polynomial amount of
record data for the source block, exponent, residue, inverse, product, and
screen result. The basis lemma gives (m_t\le U_t) current blocks.

Round (t) produces at most (E m_t\le E U_t) pairs. For each pair,

\[
1\le c,w<N,\qquad P=cw<N^2,
\]

so these integers have (O(n)) bits. The exponent has (L^2) bits or fewer,
and all remaining record data has size polynomial in (n). For a fixed
constant (d), therefore,

\[
U_{t+1}\le U_t\bigl(1+CEn^d\bigr).
\]

Consequently,

\[
\begin{aligned}
\log _2 U_T
&\le \log _2 U_0
  +T\log _2(1+CEn^d)\\
&\le \log _2 U_0
  +L^2\bigl(L^2+O(\log n)\bigr)\\
&=\log _2 U_0+L^4+O(L^3).
\end{aligned}
\]

For the standalone source, at most (E) initial pairs give

\[
U_0=E\,\operatorname{poly}(n)=2^{O(L^2)}.
\]

It follows that

\[
U_T=2^{O(L^4)}=2^{O((\log n)^4)}.
\]

This recurrence counts all presentations, including presentations whose
exact product duplicates an earlier product. Exact-value deduplication can
only reduce the number of decoder columns.

### 1.3 Refinement and generation cost

A gcd-free basis can be computed by repeated gcd splitting and exact
division. Each nontrivial split increases the number of pairwise-coprime
pieces, whose number is bounded by the endpoint-bit lemma. Thus complete
refinement, including endpoint exponent records, takes a fixed polynomial in
the accumulated input length. One can recompute it from the raw transcript
at each round. Derived basis data therefore does not feed back into the raw
recurrence above.

For each generated record, modular powering, canonical inversion by the
extended Euclidean algorithm, multiplication, comparison for exact-value
deduplication, and the two sign gcds take polynomial time in (n+\log E).
Sorting or otherwise deduplicating all exact products and doing all (T)
refinements takes

\[
T\,\operatorname{poly}(U_T,n)=2^{O(L^4)}
\]

bit operations. Any fixed polynomial-size incidence or exponent encoding is
also (2^{O(L^4)}).

### 1.4 Why the complete decoder is still polynomial

Let the retained distinct exact values be

\[
P_j=\prod_{i=1}^m b_i^{a_{ij}}\equiv1\pmod N,
\]

and let (A=(a_{ij}\bmod2)). For (z\in\ker_{\mathbf F_2}A), define the
normalized root

\[
S(z)=\prod_{i=1}^m
b_i^{\frac12\sum_j a_{ij}z_j}\pmod N.
\]

The exponents are integral and

\[
S(z)^2=\prod_{j:z_j=1}P_j\equiv1\pmod N.
\]

The map (S) is a homomorphism from the additive binary kernel to the
multiplicative square roots of (1). Indeed, if (z\oplus z') is binary
xor, then

\[
\frac{S(z)S(z')}{S(z\oplus z')}
=\prod_{j:z_j=z'_j=1}P_j\equiv1\pmod N.
\]

It is therefore enough to compute a kernel basis and evaluate (S) on that
basis. If one basis image is not (+1) or (-1), then

\[
1<\gcd(S(z)-1,N)<N

\]

(and the complementary sign also gives the corresponding split). If every
basis image is global, every kernel image is global. Gaussian elimination
and these modular evaluations are polynomial in the final transcript size.
This establishes the declared cost of the complete P66 decode without
enumerating all dependencies.

### 1.5 Composition with the full F130 transcript

In the composed form, the stated F130 endpoint-and-relation input has

\[
U_0=2^{O(L^4)}.
\]

The same recurrence gives

\[
\log _2 U_T=O(L^4)+L^4+O(L^3)=O(L^4).
\]

Thus retaining and refining the entire transcript, not only seed endpoints,
keeps both state and time at (2^{O(L^4)}).

The semantic change is real. The construction preserves every old screen
and relation, and its complete basis permanently names terminal blocks found
only in novel unary-probe cofactors. If F130 omitted such a cofactor from its
named generator basis, the declared generator set here is a strict
extension. This set inclusion says nothing about whether a new generator
creates a useful dependency.

The cap (T=L^2) is essential to this proof. The recurrence gives no bound
on how many rounds an iteration-to-fixed-point rule would take.

## 2. Exact exponent-one feedback law

For a unit (1\le c<N), let (\iota_N(c)) be its unique inverse in
\(\{1,\ldots,N-1\}\). Then

\[
P_N(c)=c\iota_N(c)=1+\kappa_N(c)N,
\qquad 0\le\kappa_N(c)\le N-2.
\]

The upper bound follows from (c\iota_N(c)\le(N-1)^2=1+(N-2)N).

Let a current block (q) divide an old endpoint. It then divides the old
exact value

\[
P_0=1+kN.
\]

Suppose (q>k), and put (s=P_0/q). It is a positive integer and
(qs\equiv1\pmod N). Also

\[
P_0=1+kN<qN,
\]

because (q-k\ge1) and (N>1). Hence (s<N), so uniqueness of the
canonical inverse gives

\[
\iota_N(q)=s=P_0/q,
\qquad P_N(q)=P_0.

\]

This proves the exact duplicate law. Its contrapositive gives the second
claim: if (P_N(q)) is new, then (q\le k) for every old exact value
(1+kN) containing (q).

If the product duplicates (P_0), both new endpoints are already monomials
in the current complete basis: (q) is a basis block and
(\iota_N(q)=P_0/q). The presentation cannot split or enlarge that basis.
If one temporarily keeps both equal exact columns, their binary difference
is a dependency and its normalized root is

\[
\sqrt{P_0P_0}=P_0\equiv+1\pmod N.
\]

Exact-value deduplication removes precisely this inert decoder direction.
The presentation is not inert before its sign screens: a proper
(\gcd(q\pm\iota_N(q),N)) can still factor (N).

If (P_N(q)) is new, its entry in prime row (r) is exactly

\[
v_r(P_N(q))\bmod2
=v_r(q)+v_r(\iota_N(q))\pmod2.

\]

Thus a prime occurring oddly in (q) can be cancelled by an odd occurrence
in its canonical inverse. The exponent-one branch is exhaustive:

1. a sign screen gives a proper factor;
2. no screen factors and the exact product is new, so it is retained; or
3. no screen factors and the product is a duplicate, so its basis and
   normalized-root effects are null and the presentation can be discarded.

For (e\ge2), even the integer divisibility premise disappears. If
(r\mid q) and

\[
c=[q^e]_N=q^e-aN,
\]

then (c\equiv-aN\pmod r). Since (r\nmid N), this need not vanish.
Word provenance therefore gives no row-reuse law after modular reduction.

## 3. Exact private-row splice

Work over \(\mathbf F_2\). Let row (r) occur in exactly one old column
(v), and let (M) denote the other old columns. Thus (v_r=1) and the
(r)-row of (M) is zero. Append a distinct column (u). A dependency that
uses the new column has the form

\[
\alpha v+M\beta+u=0.
\]

If (u_r=0), the row-(r) equation forces (\alpha=0). After deleting that
row, the remaining equation is solvable exactly when

\[
\widehat u\in\operatorname{colspan}(\widehat M).
\]

If (u_r=1), the row-(r) equation forces (\alpha=1). The remaining
equation is solvable exactly when

\[
\boxed{\widehat u+\widehat v
\in\operatorname{colspan}(\widehat M).}
\]

Thus reuse toggles the old private support; it does not by itself put the new
column in the old span. If (u=v) as a raw column, the symmetric difference
is zero and the pair gives one dependency. For equal exact values, its root
is (+1), as shown above.

Even a dependency between distinct exact values can have a global root.
Here is an independent exact check. For (N=623=7\cdot89), the two
canonical-inverse products

\[
299\cdot598=178802=1+287N=2\cdot13^2\cdot23^2,
\]

\[
432\cdot486=209952=1+337N=2^5\cdot3^8
\]

are distinct and both have parity support \(\{2\}\). Their dependency has

\[
\sqrt{178802\cdot209952}=193752=311N-1\equiv-1\pmod N.
\]

All four presentation screens are null:

\[
\gcd(299\pm598,623)=\gcd(432\pm486,623)=1.
\]

Hence parity closure does not imply a non-global normalized root.

## 4. Universe-private rows

Let (r>(N-1)/2) be prime. Among the integers (1,\ldots,N-1), the only
multiple of (r) is (r) itself. For every canonical-inverse pair
((c,\iota_N(c))), primality gives

\[
r\mid P_N(c)
\quad\Longrightarrow\quad
r\mid c\ \text{or}\ r\mid\iota_N(c).

\]

The range observation then gives

\[
c=r\quad\text{or}\quad\iota_N(c)=r.
\]

These are the two orientations of the same inverse orbit, and both have the
same exact value

\[
P_N(c)=P_N(r)=r\iota_N(r).
\]

Therefore the complete canonical-inverse universe contains at most one
distinct exact value divisible by (r). If that value has odd (r)-adic
valuation, global exact-value deduplication leaves one and only one column
with a (1) in row (r). The row has degree one.

This argument applies to every unit residue, so in particular to every
generated (c=[r^e]_N), and more strongly to a residue generated from any
block. Either (P_N(c)=P_N(r)), the retained inverse-orbit value, or
(v_r(P_N(c))=0). No finite or infinite number of unary rounds can create a
second distinct exact column on this row. Lossless degree-one peeling can
always remove the old column. This local fact does not constrain dependencies
in the rest of the matrix.

## 5. Arithmetic certificates

### Certificate A: canonical inversion cancels the fed row

Let (N=253=11\cdot23). Then

\[
26\cdot146=3796=1+15N=2^2\cdot13\cdot73.
\]

The endpoints refine to \(\{2,13,73\}\). For (q=13),

\[
\iota_N(13)=39,
\qquad13\cdot39=507=1+2N=3\cdot13^2.
\]

The product (507) is new, but its row (13) is even. Direct computation
gives

\[
\gcd(172,253)=\gcd(120,253)=\gcd(52,253)=\gcd(26,253)=1,
\]

which are exactly the old and new plus/minus screens. The parity supports are

\[
\{13,73\},\qquad\{3\}.
\]

The nonzero disjoint columns are independent. Every supported row initially
has degree one, so degree-one peeling deletes both columns and leaves an empty
2-core. This disproves “a new feedback value reuses the fed row.”

### Certificate B: real reuse need not survive peeling

Let (N=77=7\cdot11). Then

\[
4\cdot58=232=1+3N=2^3\cdot29,
\]

so the old support is \(\{2,29\}\) and the endpoint basis is
\(\{2,29\}\). Feeding (q=2) gives

\[
\iota_N(2)=39,
\qquad2\cdot39=78=1+N=2\cdot3\cdot13.
\]

This distinct product genuinely reuses row (2). The four screens are null:

\[
\gcd(62,77)=\gcd(54,77)=\gcd(41,77)=\gcd(37,77)=1.
\]

The column supports are

\[
\{2,29\},\qquad\{2,3,13\}.
\]

Rows (29,3,13) are private. Peeling either column through a private row and
then the other deletes the whole prefix. Equivalently, the two columns have
full column rank and zero kernel. Later columns could change this prefix
calculation, so it is not a statement about an unbounded future transcript.

### Certificate C: a screened exponent-one duplicate is inert

Let (N=91=7\cdot13). Then

\[
2\cdot46=92=1+N=2^2\cdot23,
\]

with endpoint basis \(\{2,23\}\). Feeding (q=23) gives

\[
\iota_N(23)=4,
\qquad23\cdot4=92.
\]

Both endpoints are monomials in the old basis, and the duplicate dependency
has normalized root (92\equiv1\pmod{91}). Its four screens are null:

\[
\gcd(48,91)=\gcd(44,91)=\gcd(27,91)=\gcd(19,91)=1.
\]

Thus, after screening, this duplicate changes neither basis nor decoder
image.

### Certificate D: a duplicate presentation can factor directly

Let (N=63=3^2\cdot7). The canonical self-pairs satisfy

\[
8^2=64=1+N,
\qquad62^2=3844=1+61N.
\]

Their sign gcds are either (1) or (N):

\[
\gcd(16,63)=1,\quad\gcd(0,63)=63,
\]

\[
\gcd(124,63)=1,\quad\gcd(0,63)=63.
\]

Since (8=2^3) and (62=2\cdot31), complete refinement exposes the block
(q=2). Its canonical inverse is (32), and

\[
2\cdot32=64,
\]

an exact duplicate of the first value. It adds no exact decoder column and
does not refine the basis, but its new presentation gives

\[
\gcd(2-32,63)=\gcd(30,63)=3.
\]

Therefore sign screens must precede exact-value deduplication.

## 6. Exact remaining gate

The bounded unary all-block source, including composition after the complete
F130 transcript, is a deterministic quasipolynomial candidate. Its new
operation is the permanent admission of endpoint cofactors as future blocks.
The proof above bounds that operation but proves no progress from it.

A factoring theorem still requires an all-input proof that within the stated
(T=L^2) rounds there is either a proper direct sign gcd or a final parity
dependency whose normalized root is not (+1) or (-1). A new relation, a
reused row, a nonempty 2-core, and a non-global decoder root are separate
conditions. None of the first three alone proves the fourth.
