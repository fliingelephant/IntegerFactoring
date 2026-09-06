# F164 hostile audit — PASS

## Frozen inputs

I read the complete frozen statement, proof, and manifest. All requested
SHA-256 hashes matched before the audit:

- `STATEMENT.md`:
  `b45b07e7f97aad53d4a3fa15ce795db4a7bdf659f371bb70857668dae816af83`;
- `PROOF.md`:
  `ccfe1f918bb4bba86ffefe72a4678ef18785e54788cff5cb49946d2186696187`;
- `MANIFEST.md`:
  `8003d58aba572fd48078b5631fa89f6901bfd2c472d56deec2666072773b4f02`.

I also checked the promoted F161 factor-first alignment interface on which
F164 depends. I did not modify a frozen input or a durable ledger.

## Verdict

**PASS.** The finite-bank theorem, the triangular rank--capacity law, the
conditional index closure, and the `N=341` obstruction are correct under
the stated common-order and unit hypotheses. They remain correct for an
arbitrary odd composite with prime-power CRT components.

I found no false quotient-fingerprint equivalence, unsynchronized equality
partition, unjustified relation independence, incorrect subgroup-size
bound, bad Smith-normal-form conclusion, or hidden super-quasipolynomial
operation in a quasipolynomial-size encoded transcript.

The result is only a decoder and an accounting theorem. It does not show
that public blocks give independent quotient directions. It does not force
the index equality `D=M*kappa`. It is not a factoring algorithm. The frozen
files state these limits correctly.

Two wording points need the exact interpretations in Section 7 below. They
do not change the theorem or the verdict.

## 1. Quotient fingerprints are exact

Fix one hidden component

\[
R_j=p_j^{\alpha_j}.
\]

Its unit group is cyclic because `p_j` is odd. Let its order be `q_j`.
The certified element `g` has exact order `M`, so `M` divides `q_j`. The
kernel of the `M`-th-power map therefore has size

\[
\gcd(M,q_j)=M.
\]

It is the unique subgroup of order `M`, namely `H_j=<g>`. Hence

\[
F(u)=F(v)\pmod {R_j}
\iff
(d^{u-v})^M=1\pmod {R_j}
\iff
d^{u-v}\in H_j.
\]

This argument does not replace a prime power by its prime field. It covers
one component, several components, and repeated prime powers.

For any pair of public fingerprints, put

\[
G=\gcd(F(u)-F(v),N).
\]

If `G=1`, the two values differ modulo every residue prime and therefore
modulo every full prime-power component. If `G=N`, they are equal modulo
`N` and every component. Any partial prime-power divisibility, or equality
in only some components, gives a proper divisor and terminates the run.

Thus, on the no-factor branch, exact public equality gives the same
equivalence relation in every hidden quotient. After exact deduplication,
the bank represents `kappa` different cosets of the order-`M` group `H_j`
in every component. Therefore

\[
|\langle H_j,d_1,\ldots,d_t\rangle|\ge M\kappa.
\]

This is a count of represented cosets. It is not a claim that the named
blocks are independent generators.

## 2. The layer updater is exhaustive

Inside one layer `T_e=d^eT`, every fingerprint is multiplied by the same
unit `d^(eM)`. This preserves equality and all gcd outcomes. Each layer
therefore has exactly `kappa` represented quotient cosets on a no-factor
run.

If `e` is the first layer that meets an earlier layer, then
`T_0,...,T_(e-1)` are pairwise disjoint. They contain exactly `e*kappa`
represented cosets in every component. A collision gives

\[
x=d^{e-f}ww'^{-1},
\qquad x^M=1\pmod N.
\]

The promoted F161 digit calculation applies to this public `x`. It either
finds a hidden-log mismatch and factors `N`, or gives one aligned `a mod M`
with `x=g^a mod N`.

The resulting relation has coefficient `e-f`, with `1<=e-f<=B`, in the
new block coordinate. Every old relation has zero in that coordinate.
The first collision row for this block is therefore rationally independent
of all earlier rows. No independence claim is made for later collision
rows.

If no layer through `B` meets an earlier layer, the `B+1` layers are
pairwise disjoint in every component. The represented-coset count is then
exactly `(B+1)kappa`.

For `T={1}`, a collision between layers `e` and `f` is equivalent to
`d^(e-f) in H_j`. Therefore local relative order above `B` in every
component forces the no-collision outcome for the first block. It does not
force this outcome after earlier blocks have enlarged the quotient bank.

## 3. The `(B+1)^delta` law is exact but limited

Introduce one new coordinate per call and keep only the first collision row
for the triangular accounting. Each collision call increases both `t` and
the certified relation rank `r` by one. Its retained layers multiply the
bank by `e>=1`. Each no-collision call increases only `t` and multiplies
the bank by `B+1`.

Starting from `{1}`, exactly `delta=t-r` calls are no-collision calls.
Consequently

\[
\kappa\ge(B+1)^{t-r}.
\]

This is a lower bound on the size of one explicit bank. It does not show
that each released block multiplies the abstract subgroup order. Collision
calls can express many blocks through one old unresolved direction. The
frozen candidate makes this distinction.

## 4. Full-rank index closure is correct

For each component, the public word map

\[
\Psi_j:\mathbf Z^{t+1}\longrightarrow
(\mathbf Z/R_j\mathbf Z)^\times
\]

has image

\[
A_j=\langle g,d_1,\ldots,d_t\rangle.
\]

Every retained aligned row is an exact global modular relation. Thus
`L` is contained in every kernel. If `L` has full rank, the finite group

\[
P=\mathbf Z^{t+1}/L
\]

has order `D` and maps onto every `A_j`. Hence

\[
M\kappa\le |A_j|\le D.
\]

If `D=M*kappa`, both inequalities are equalities. Every map `P -> A_j`
is then an isomorphism. Since `A_j` lies in a cyclic odd-prime-power unit
group, `P` is cyclic. Its Smith form is

\[
\operatorname{diag}(1,\ldots,1,D).
\]

The associated column transformation gives a public exponent word `h`
whose class generates `P`. Its image has order `D` in every component.
The global CRT image also has order `D` because each component map is
injective.

The screen `gcd(D,N)` cannot equal `N` in this equality branch. Exact local
order gives `D<=phi(R_j)<R_j<=N`, so `D<N`. The screen therefore returns a
proper divisor or proves coprimality.

The equality is essential. Full rank alone only gives a finite cover of
the hidden local groups. If `D>M*kappa`, Smith normal form does not reveal
the hidden kernel index.

## 5. Quasipolynomial cost

Let the total encoded transcript be quasipolynomial in
`n=ceil(log_2(N+1))`. This includes:

- the number of retained fingerprints;
- the number of released-block coordinates and retained relations; and
- the bit lengths of all exponent vectors and matrix entries.

For bank cardinality `K`, one layer call creates at most `(B+1)K` values
and makes at most their squared number of gcd comparisons. Products and
squares of quasipolynomial bounds are quasipolynomial. Modular powering is
polynomial in the exponent bit length. HNF and SNF are polynomial in their
explicit dimensions and bit lengths. The F161 alignment is
quasipolynomial because the supplied factorization of `M` has all prime
factors at most the chosen cap.

When `D=M*kappa`, trial division through `sqrt(kappa)` is also
quasipolynomial because the explicit bank count `kappa` is
quasipolynomial. Combining this factorization with the supplied
factorization of `M` gives the complete factorization of `D`.

To call F161 again, choose a new cap

\[
B'=\max(B,\kappa).
\]

Then every prime factor of `D=M*kappa` is at most `B'`, and `B'` remains
quasipolynomial. The frozen statement does not say that the original cap
`B` remains valid.

There is no compressed evaluation theorem when the explicit bank or its
provenance exceeds quasipolynomial encoding size.

## 6. Independent `N=341` certificate check

I registered and ran `verify_audit.py` with no randomness. Its SHA-256 hash
is

`b166dc147077b012af3e36266a2162ad08c32e7ac34fa06b90edb086b26aaad1`.

It returned `ALL CHECKS PASSED`.

The two canonical-inverse identities are exact:

\[
337\cdot85=1+84\cdot341,
\qquad
325\cdot277=1+264\cdot341.
\]

All four endpoints are units. For each canonical pair, both
`gcd(c-w,N)` and `gcd(c+w,N)` equal one. Joint gcd-free refinement splits
the shared factor of `85` and `325`, and it retains the pairwise-coprime
unit blocks `337` and `277`.

The state `(g,M)=(-1,2)` passes its screens. For both released blocks, the
two F161 cap screens are

\[
[\gcd(d^2-1,N),\gcd(d^4-1,N)]=[1,1].
\]

Their local relative orders against `{+1,-1}` are `(5,5)` modulo the
components `(11,31)`. The direct screens

\[
\gcd(d\pm1,N),\qquad \gcd(d^2\pm1,N)
\]

are all one for both blocks.

The aligned relation is exact:

\[
277\cdot337^2\equiv-1\pmod {341}.
\]

For the old bank `{1,d_1,d_1^2}`, the fingerprint set is
`{1,16,256}`. Multiplication by `d_2` gives the shifted fingerprint set
`{1,4,64}`. Their intersection is exactly `{1}`. Thus the second block
gives a first-layer aligned collision. It does not give a second capacity
multiplier or a factor.

This certificate proves the intended obstruction: two distinct coprime
integer blocks can have the same beyond-cap cyclic quotient direction.

## 7. Exact scope notes

The proof's cost sentence correctly says **quasipolynomial transcript**.
A cardinality cap on `kappa` alone would not cap the number of `e=1`
collision calls, the number of coordinates, or the provenance bit length.
Therefore “explicit quasipolynomial bank” must mean its full encoded size,
or the algorithm must separately cap the complete transcript. This is a
necessary scope interpretation. It is not an algebraic defect.

Likewise, `(h,D)` can be reused by F161 with the enlarged cap `B'` above.
The old cap need not contain the prime factors of `kappa`.

Finally, the three items in Statement Section 8 are alternative forms of
needed source-side progress. They are not proved to be logically
equivalent. The proof and manifest use them only as alternatives.

Subject to these exact readings, the candidate passes. A fresh
statement-only blind reconstruction is still required before durable
promotion.
