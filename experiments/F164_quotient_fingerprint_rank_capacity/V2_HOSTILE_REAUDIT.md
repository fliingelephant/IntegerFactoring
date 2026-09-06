# F164 V2 hostile re-audit — PASS

## Frozen inputs

I read the preserved V1 statement, proof, manifest, hostile audit, and blind
reconstruction in full. I then read the V2 statement, proof, and manifest in
full. I did not modify a frozen artifact or a durable ledger.

The requested V2 SHA-256 hashes match:

- `V2_STATEMENT.md`:
  `8e47a9e249ff7f6fd7996664daddbbd53ace7dafd1e85b159ad20502a6d6fa19`;
- `V2_PROOF.md`:
  `53488652f65c7138412389a584e6a4dd7fa5a9367191c8d5bbc1558f7a4bf2bb`;
- `V2_MANIFEST.md`:
  `08e5e867a5ad5f2b901fb270da5bf343d017f2ce39e29d3a25aa7399ae6d61ab`.

## Verdict

**PASS.** V2 repairs all four defects from the blind reconstruction. The
quotient-fingerprint equivalence, factor-first comparison, finite-bank
capacity bound, layer updater, triangular rank--capacity law, conditional
rank--volume closure, and synchronized cyclic obstruction remain correct.
The cost claim is correct under the new cap on the complete encoded
transcript.

This remains a conditional decoder and accounting theorem. It does not force
new quotient directions, the equality `D=M*kappa`, or a factor. It is not a
quasipolynomial factoring algorithm.

## 1. The four V2 repairs are exact

### 1.1 Alternatives, not equivalence

Section 8 now calls the three missing progress mechanisms alternatives and
explicitly says that they are not claimed to be equivalent. The proof repeats
this limitation. This repairs the first blind defect without adding an
unsupported implication.

### 1.2 The cap covers the full encoded transcript

The V2 statement now caps the total bit length of:

- all named blocks;
- the explicit retained bank;
- all retained relations;
- all word and occurrence provenance; and
- every exponent and coefficient.

It also says that a cap on `kappa` or bank cardinality alone is insufficient.
This is the necessary correction. A sequence of first-layer collisions can
keep `kappa` fixed while adding arbitrarily many coordinates, relations, and
provenance records.

### 1.3 The `N=341` provenance is self-contained

V2 defines a canonical-inverse endpoint relation and the complete joint
gcd-free refinement used in the certificate. It gives the endpoint
factorizations

\[
337=337,
\quad 85=5\cdot17,
\quad 325=5^2\cdot13,
\quad 277=277.
\]

The exact identities show that both displayed endpoint pairs are inverse
pairs modulo `341`. All endpoints lie strictly between zero and `341`, so the
second endpoint in each pair is the least positive inverse. The refined
distinct blocks `337,5,17,13,277` are pairwise coprime. Thus `337` and `277`
are legitimate public unit blocks with retained endpoint provenance.

### 1.4 The next F161 cap is updated

V2 sets

\[
B'=\max(B,\kappa).
\]

Under `D=M*kappa`, every prime divisor of `D` divides `M` or `kappa`.
Therefore it is at most `B'`. Since the explicit bank and its full transcript
are quasipolynomially bounded, `kappa` and `B'` are also quasipolynomially
bounded. This repairs the fourth blind defect.

## 2. Quotient fingerprints remain exact

Fix one hidden odd prime-power component `R_j`. Its unit group is cyclic.
Because `g` has exact order `M`, the component group order is divisible by
`M`. The kernel of the `M`-th-power map has size

\[
\gcd(M,|U_j|)=M.
\]

A cyclic group has one subgroup of each possible order. Hence this kernel is
exactly `H_j=<g>`. Therefore

\[
F(u)=F(v)\pmod {R_j}
\iff
d^{u-v}\in H_j.
\]

For a public difference of two fingerprint residues:

- gcd one means inequality modulo every hidden prime, and thus every full
  prime-power component;
- gcd `N` means equality modulo all of `N`; and
- every intermediate gcd is a proper factor.

Thus a no-factor run has one synchronized equality partition in every hidden
quotient. If the bank has `kappa` public fingerprint values, it represents
`kappa` different cosets of an order-`M` subgroup in each component. This
proves the lower bound `M*kappa`.

## 3. The one-block updater is sound

Within the layer `T_e=d^eT`, all fingerprints are multiplied by the unit
`d^(eM)`. This preserves equality and gcd outcomes. Each layer therefore has
exactly `kappa` represented quotient cosets on a no-factor run.

If layer `e` is the first layer to meet an earlier layer `f`, then layers
zero through `e-1` are pairwise disjoint. They contain exactly `e*kappa`
cosets. The collision gives

\[
x=d^{e-f}ww'^{-1},
\qquad x^M=1\pmod N.
\]

The factor-first digit calculation either finds a proper factor or returns
one global exponent `a mod M` with `x=g^a mod N`. The resulting relation has
new-block coefficient `e-f`, which is nonzero. Every earlier relation has
zero in that coordinate. The new row is therefore independent over the
rationals from all earlier rows.

If no layer through `B` meets an earlier layer, all `B+1` layers are
disjoint. The retained capacity grows by exactly `B+1`.

The three displayed outcomes are best read as a sequential procedure: a
proper gcd or alignment mismatch returns the factor; otherwise a first
collision returns an aligned relation; otherwise the bank grows. The nested
wording in item 2 does not create a mathematical ambiguity.

## 4. The rank--capacity accounting is exact

Start from the base row `(M,0,...,0)` and bank `{1}`. Each collision call
adds one coordinate and one independent selected relation. Each no-collision
call adds one coordinate and multiplies the bank by `B+1`.

If `t` blocks have been introduced and `r` selected collision rows have been
retained, exactly `delta=t-r` calls were no-collision calls. Collision calls
can add a factor `e>=1` to the retained bank, so discarding those factors
gives

\[
\kappa\ge (B+1)^{t-r}.
\]

This counts represented quotient cosets. It does not claim that the named
blocks are independent abstract generators.

## 5. The rank--volume closure is correct

For each hidden component, the public word map from `Z^(t+1)` has image

\[
A_j=\langle g,d_1,\ldots,d_t\rangle.
\]

Every retained aligned row is a global relation, so the retained lattice
`L` lies inside every local kernel. If `L` has full rank and index `D`, the
finite presentation `P=Z^(t+1)/L` has order `D` and maps onto every `A_j`.
Consequently,

\[
M\kappa\le |A_j|\le D.
\]

If `D=M*kappa`, each map is an isomorphism. Each `A_j` is cyclic because it
is a subgroup of an odd-prime-power unit group. Hence `P` is cyclic. Smith
normal form gives a public exponent word `h` that has exact order `D` in
every component and modulo `N`.

The screen `gcd(D,N)` cannot equal `N` in this equality branch. For every
component,

\[
D=|A_j|\le\varphi(R_j)<R_j\le N,
\]

so `D<N`. The screen therefore gives a proper factor or proves coprimality.

Factoring `kappa` by trial division is quasipolynomial because
`kappa` is at most the explicit quasipolynomial bank size. Merging that
factorization with the supplied factorization of `M` gives the complete
factorization of `D`. The corrected cap `B'` then makes `(h,D)` a valid next
F161 state.

## 6. The finite obstruction is valid

For `N=341=11*31`, `g=-1`, `M=2`, and `B=2`, the two exact endpoint
relations are

\[
337\cdot85=1+84\cdot341,
\qquad
325\cdot277=1+264\cdot341.
\]

Modulo `11` and `31`, both released blocks `337` and `277` first enter
`{+1,-1}` at exponent five. Thus each has local relative order five, above
the cap two, in both components. Direct arithmetic gives

\[
277\cdot337^2\equiv-1\pmod {341}.
\]

The second block therefore lies in the quotient direction already generated
by the first block. The aligned relation is real, but it does not force a
second capacity multiplier. This proves the claimed concrete obstruction.

The general cyclic model is also valid as an abstract obstruction. Mapping
all released blocks to powers of one prime-order quotient generator can keep
all local collision kernels synchronized while the generated quotient stays
one-dimensional. V2 does not claim that every such abstract list has
canonical-inverse provenance.

## 7. The quasipolynomial cost claim is now correctly scoped

Let the total encoded transcript have quasipolynomial bit length. Then its
bank size, coordinate count, relation count, coefficient sizes, exponent
sizes, and provenance size are all quasipolynomially bounded. The scan cap
`B` is also quasipolynomial by hypothesis.

One layer call creates at most `(B+1)K` fingerprints for old bank size `K`.
Even all pairwise comparisons remain quasipolynomial. Modular powering is
polynomial in the exponent bit length. The factor-first alignment is
quasipolynomial because all prime divisors of `M` are at most `B`. Standard
HNF and SNF algorithms are polynomial in the explicit matrix dimensions and
coefficient bit lengths.

No step in the stated algorithm hides a super-quasipolynomial expansion.
Conversely, V2 correctly makes no cost claim for a larger compressed bank.

## 8. Interaction with the proposed F161 common-order shortcut

The proposed shortcut is mathematically valid in the F161 common-return
branch. From the known multiple `eM` and its factorization, order-reduction
screens can either factor `N` or certify one common local order
`m=ord_N(d)`. In a cyclic component,

\[
|\langle g,d\rangle|
=\operatorname{lcm}(M,m)
=M e.
\]

A standard lcm-order construction can then produce a public element of
common order `Me` without first aligning the local exponents in
`d^e=g^a`. Thus alignment is not necessary if the only required output is a
larger certified common-order element.

This does not invalidate F164. Its collision word already satisfies
`x^M=1`, so `ord(x)` divides `M` in every component and
`lcm(M,ord(x))=M`. An lcm construction gives no order growth and does not
recover the exact lattice row. F164 uses alignment to obtain either a factor
or the global relation `x=g^a`, which is required for its relation-rank and
index calculations. The shortcut and F164 therefore supply different output
strengths.

## Final classification

- Four blind defects: **repaired**.
- Fingerprint kernel and synchronized partition: **PASS**.
- Finite-bank lower bound: **PASS**.
- Layer updater and relation independence: **PASS**.
- Rank--capacity law: **PASS**.
- Conditional `D=M*kappa` closure: **PASS**.
- `N=341` self-contained certificate: **PASS**.
- General cyclic obstruction: **PASS within its stated abstract scope**.
- Full-transcript quasipolynomial cost: **PASS**.
- F161 lcm shortcut interaction: **does not invalidate F164**.

**Overall verdict: PASS.** A fresh statement-only blind reconstruction is
still required before durable promotion.
