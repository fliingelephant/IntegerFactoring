# F164 V2 blind reconstruction

## Source and verdict

The SHA-256 digest of `V2_STATEMENT.md` is

```text
8e47a9e249ff7f6fd7996664daddbbd53ace7dafd1e85b159ad20502a6d6fa19
```

This reconstruction uses only that statement within F164.

**Verdict: VERIFIED.** All stated mathematical claims are valid. The layer
trichotomy is an operational, factor-first trichotomy: all proper gcds at the
current layer take priority over declaring a collision. The rank--capacity
formula uses the stated one-at-a-time initialization with no introduced
blocks. With these conventions, which are already implicit in the statement,
no repair is needed.

## 1. Quotient fingerprints

Fix a hidden component

\[
R_j=p_j^{\alpha_j},\qquad U_j=(\mathbf Z/R_j\mathbf Z)^\times .
\]

Because `N` is odd, `U_j` is cyclic. Write its order as
\(m_j=p_j^{\alpha_j-1}(p_j-1)\). The common-order certificate gives an
element \(g\) of order \(M\), so \(M\mid m_j\). In a cyclic group, the kernel
of the endomorphism

\[
\psi_M:U_j\longrightarrow U_j,\qquad y\longmapsto y^M
\]

has order \(\gcd(M,m_j)=M\). A cyclic group has one subgroup of each order
dividing its group order. Hence

\[
\ker\psi_M=\langle g\bmod R_j\rangle=H_j.
\]

For exponent vectors \(u,v\), commutativity gives

\[
F(u)F(v)^{-1}=(d^{u-v})^M\pmod {R_j}.
\]

Therefore

\[
F(u)=F(v)\pmod {R_j}
\iff (d^{u-v})^M=1\pmod {R_j}
\iff d^{u-v}\in H_j.
\]

Thus the fingerprint is constant on a quotient coset and separates distinct
cosets exactly. Negative exponents cause no issue because every named block
is a unit.

This proof uses only cyclicity of the unit group of an odd prime power. It
does not use squarefreeness of `N`.

## 2. The factor-first gcd dichotomy and finite-bank capacity

Take two canonical fingerprint residues \(A=F(u)\) and \(C=F(v)\), and put
\(G=\gcd(A-C,N)\). If \(A=C\pmod {R_j}\) for some but not all hidden
components, then the complete factor \(R_j\) divides \(G\), while at least
one other prime-power component does not divide \(G\). Hence
\(1<G<N\). If a difference is divisible by only a proper power of some
\(p_j\), its gcd is also proper. Consequently, after all proper gcds have
been returned, only two possibilities remain:

- \(G=N\), in which case the fingerprints are equal modulo every \(R_j\)
  and modulo `N`;
- \(G=1\), in which case \(p_j\nmid A-C\) for every `j`, so the fingerprints
  differ modulo every \(R_j\).

Delete equal fingerprints modulo `N`. On the no-factor branch, the retained
\(\kappa(S)\) values remain pairwise distinct in every hidden component.
By the fingerprint equivalence, they represent \(\kappa(S)\) distinct
\(H_j\)-cosets. All these cosets lie in

\[
K_j=\langle H_j,d_1,\ldots,d_t\rangle,
\]

and every coset has \(|H_j|=M\) elements. They are disjoint, so

\[
|K_j|\ge M\kappa(S).
\]

Enlarging `S` cannot reduce the number of distinct public residues. This
proves both the capacity bound and its monotonicity.

## 3. One-block layers

Let `T` contain one word for every old fingerprint. On the no-factor branch,
its \(\kappa\) quotient cosets are distinct in each component. For fixed
`e`, multiplication by \(d^e\) is a bijection, so the same holds inside
\(T_e=d^eT\). More explicitly,

\[
F(d^ew)-F(d^ew')\equiv (d^e)^M\bigl(F(w)-F(w')\bigr)\pmod N,
\]

and \((d^e)^M\) is a unit. Hence internal gcd behavior is exactly the old
gcd behavior.

Suppose `e` is the first layer index with a common collision against an
earlier layer. Before declaring that collision, process all relevant proper
gcds factor-first. On the surviving branch, no two words in
\(T_0,\ldots,T_{e-1}\) collide in any hidden quotient. Those `e` layers
therefore contain exactly \(e\kappa\) distinct public fingerprints and
exactly that many quotient cosets in every component. Retaining them
multiplies capacity by exactly `e`.

For a collision

\[
F(d^ew)=F(d^fw')\pmod N,\qquad f<e,
\]

put \(x=d^{e-f}ww'^{-1}\). Then

\[
x^M=F(d^ew)F(d^fw')^{-1}=1\pmod N.
\]

Locally, the kernel calculation shows \(x\in H_j\), so there is a unique
\(a_j\bmod M\) with

\[
x=g^{a_j}\pmod {R_j}.
\]

The next subsection proves that the public alignment either separates
components by a proper gcd or proves that all \(a_j\) are one common
\(a\bmod M\).

If no collision occurs for \(0\le e\le B\), the same argument shows that
all \((B+1)\kappa\) words have distinct fingerprints in every component.
The multiplier is exactly `B+1`.

Finally, assume the quotient order of \(dH_j\) is greater than `B` for every
component and start with \(T=\{1\}\). A collision between exponents
\(0\le f<e\le B\) would give \(d^{e-f}\in H_j\), with
\(1\le e-f\le B\), in every component. This contradicts the hypothesis.
Thus the first call must take the no-collision outcome. For a later block,
the relevant old quotient subgroup is larger than \(H_j\); individual order
against \(H_j\) does not prevent membership in that larger subgroup.

## 4. Factor-first synchronization of the local logarithms

Here is a self-contained reconstruction of the alignment step. Let
\(q^\beta\Vert M\). Define

\[
g_q=g^{M/q^\beta},\qquad x_q=x^{M/q^\beta}.
\]

In every hidden component, \(g_q\) has order \(q^\beta\) and
\(x_q=g_q^{a_j}\). Put

\[
\zeta_q=g_q^{q^{\beta-1}},
\]

which has order `q` in every component.

Recover the base-`q` digits of \(a_j\) from low to high. Suppose the already
recovered common prefix is

\[
A_\ell=c_0+c_1q+\cdots+c_{\ell-1}q^{\ell-1}.
\]

Form

\[
y_\ell=(x_qg_q^{-A_\ell})^{q^{\beta-1-\ell}}.
\]

In component `j`, this equals \(\zeta_q^{c_{j,\ell}}\), where
\(c_{j,\ell}\) is the next digit of \(a_j\). For each
\(c=0,\ldots,q-1\), compute

\[
\gcd(y_\ell-\zeta_q^c,N).
\]

If the local digits differ, choose a digit value attained by some but not
all components. The corresponding difference is zero modulo those complete
prime-power components and nonzero modulo at least one other component.
The gcd is proper. Partial divisibility by a mismatching component can only
produce a proper gcd earlier. If no proper gcd occurs, exactly one candidate
has gcd `N`, and it is the common digit in every component. This completes
the induction.

Repeat for every prime power in the supplied factorization of `M`, then use
the ordinary CRT on the coprime moduli \(q^\beta\). The result is one public
\(a\bmod M\) with

\[
x=g^a\pmod {R_j}
\]

for all `j`, hence modulo `N`. Every digit scan has length \(q\le B\). This
is the required factor-first Pohlig--Hellman synchronization.

The resulting equation

\[
d^{e-f}ww'^{-1}=g^a\pmod N
\]

is an exact public relation. In coordinates
\((z,v_1,\ldots,v_t)\), its row has `g`-coordinate \(-a\), the exponent
vector of \(d^{e-f}ww'^{-1}\), and new-block coefficient \(e-f\ne0\).
Every old relation has new-block coefficient zero. Thus this row is not in
the rational span of the old rows.

This also proves the layer trichotomy. A proper difference gcd or a local-log
mismatch is the factor outcome. Otherwise the first common collision gives
the aligned relation, or no common collision through `B` gives all
`B+1` disjoint layers. These branches are exclusive under factor-first
processing and exhaustive.

## 5. Rank--capacity accounting

Start before any block is introduced, with \(t=r=0\), \(\delta=0\), and
\(\kappa=1\). Introduce blocks one at a time and retain the first collision
row on collision calls.

The nonzero fresh coordinate proved above makes these retained rows
rationally independent in introduction order. Thus `r` is their rank, not
only their count. A collision call changes

\[
(t,r,\delta)\longmapsto(t+1,r+1,\delta),
\]

and changes \(\kappa\) by a factor \(e\ge1\). A no-collision call changes

\[
(t,r,\delta)\longmapsto(t+1,r,\delta+1)
\]

and changes \(\kappa\) by the factor `B+1`. Hence \(\delta\) is exactly the
number of no-collision calls. Multiplying all capacity factors gives

\[
\kappa\ge(B+1)^\delta.
\]

For a run started from a nontrivial pre-existing state, the precise shifted
invariant would be
\(\kappa/\kappa_0\ge(B+1)^{\delta-\delta_0}\). The boxed formula in the
statement is the canonical initialization just used.

The inequality supplies no mechanism that makes \(\delta\) decrease. A
collision preserves it, and a no-collision increases it. Thus it does not
claim eventual full rank.

## 6. Full-rank index closure

For each component define the surjective word map

\[
\Phi_j:\mathbf Z^{t+1}\longrightarrow
K_j=\langle g,d_1,\ldots,d_t\rangle_{R_j},
\qquad
(z,v)\longmapsto g^z d^v.
\]

The base row and every aligned row are genuine relations modulo `N`, so

\[
L\subseteq\ker\Phi_j
\]

for every `j`. If `L` has full rank, then

\[
A=\mathbf Z^{t+1}/L
\]

is a finite abelian group of order
\(D=[\mathbf Z^{t+1}:L]\). Each \(\Phi_j\) factors through a surjection

\[
A\twoheadrightarrow K_j.
\]

It follows that \(|K_j|\mid D\), in particular \(|K_j|\le D\). Combining
this with finite-bank capacity gives

\[
M\kappa(S)\le |K_j|\le D.
\]

If \(D=M\kappa(S)\), both inequalities are equalities. The displayed
surjection is then an isomorphism for every component. Each \(K_j\) is a
subgroup of the cyclic group \(U_j\), so it is cyclic. Therefore the one
public presentation `A` is cyclic.

Smith normal form both tests this fact and returns a generator class of
`A`. Choose a public integer representative \((z,v)\) of that class and
form

\[
h=g^z d^v\pmod N.
\]

Under every component isomorphism, the class maps to an element of exact
order `D`. Hence

\[
\operatorname{ord}_{R_j}(h)=D
\]

for every `j`, and the order modulo `N`, the least common multiple of these
local orders, is also `D`. Because the old generator's class is a fixed
power of the generator class in `A`, this construction also synchronizes
the embedding of the old cyclic state; it is not merely a collection of
unrelated local generators.

As an element order, `D` divides \(|U_j|\) for every `j`. In particular,

\[
v_{p_j}(D)\le \alpha_j-1<v_{p_j}(N).
\]

Thus \(\gcd(D,N)\) cannot equal `N`. If it is greater than one, it is a
proper factor. On the surviving branch it equals one, as required for the
next common-order certificate.

When equality holds, \(D=M\kappa(S)\). The factorization of `M` is supplied.
Since \(\kappa(S)\) is no larger than the explicit bank, trial division of
\(\kappa(S)\) costs at most quasipolynomially many divisions when that bank
has quasipolynomial size. Merging the two factorizations gives the complete
factorization of `D`. Every prime divisor of `D` is at most

\[
B'=\max(B,\kappa(S)),
\]

and `B'` is quasipolynomial under the stated bank bound. Thus `(h,D)` meets
all stated next-state conditions.

If `L` is not full rank, `A` is infinite and supplies no finite index upper
bound. If `L` is full rank but \(D>M\kappa(S)\), the finite maps can still
have nontrivial kernels of different allowed sizes. Neither row count nor
rank identifies those kernels. Therefore exact order is not certified in
either case.

## 7. Arbitrary odd prime powers

Every argument above remains valid for \(R_j=p_j^{\alpha_j}\) with arbitrary
\(\alpha_j\ge1\):

1. \((\mathbf Z/p_j^{\alpha_j}\mathbf Z)^\times\) is cyclic for odd
   \(p_j\), which proves the fingerprint kernel statement and cyclicity at
   closure.
2. Equality modulo a complete \(R_j\) makes the gcd divisible by that
   complete component. Divisibility by only part of a component already
   returns a nontrivial proper divisor and therefore cannot invalidate a
   no-factor inference.
3. The digit synchronization compares equalities modulo complete hidden
   components. It either aligns all local digits or exposes a proper gcd.
4. CRT across the pairwise coprime `R_j` converts simultaneous local
   equalities into equality modulo `N`.

No proof step replaces a prime power by its residue field, and no step
assumes that `N` is squarefree.

## 8. The `N=341` provenance-compatible boundary

The numerical certificate is exact:

\[
341=11\cdot31,
\]

and \(g=-1\) has order \(M=2\) modulo both components. Also
\(\gcd(2,341)=1\), the only prime divisor of `M` is at most \(B=2\), and

\[
337\cdot85=28645=1+84\cdot341,
\]

\[
325\cdot277=90025=1+264\cdot341.
\]

Thus `85` and `277` are the least positive inverses of `337` and `325`,
respectively. All four endpoints are units.

The only shared nontrivial block content among the displayed endpoint
decompositions is the factor `5` shared by `85` and `325`:

\[
85=5\cdot17,qquad 325=5^2\cdot13.
\]

Complete joint gcd refinement retains the value `5` with its multiplicity
and occurrence data, and it leaves `337` and `277` as distinct blocks.
Those retained distinct values are pairwise coprime to the other retained
values and are units modulo `N`. Therefore

\[
d_1=337=-4\pmod {341},\qquad d_2=277=-64\pmod {341}
\]

have the claimed direct endpoint-occurrence provenance. No informal or
post-hoc block source is needed.

Their powers through exponent five verify the local quotient orders. For
\(d_1\), the residues at exponents one through five are

\[
7,5,2,3,10\pmod {11}
\]

and

\[
27,16,29,8,30\pmod {31}.
\]

The fifth residue is `-1` and none of the first four is `+1` or `-1`. For
\(d_2\), the corresponding lists are

\[
2,4,8,5,10\pmod {11}
\]

and

\[
29,4,23,16,30\pmod {31}.
\]

Again, the first hit on \(H_j=\{1,-1\}\) is exponent five. Thus each block
individually has relative order five in both hidden quotients, and each
individual scan through `B=2` is beyond-cap.

Nevertheless,

\[
d_2d_1^2\equiv(-64)(-4)^2=-1024=-1-3\cdot341
\equiv-1=g\pmod {341}.
\]

After the first block has retained the three quotient cosets represented by
\(1,d_1,d_1^2\), the second block collides already at layer `e=1`:

\[
d_2d_1^2H_j=H_j.
\]

The relation is identical in both components, so alignment returns the
common relation rather than a factor. Since this first collision has
`e=1`, retaining the earlier layers multiplies capacity only by one. The
unseen order relation is

\[
d_1^5=(-4)^5=-1024\equiv g\pmod {341},
\]

whose quotient coefficient `5` exceeds the scan cap. With two block
coordinates and only the collision row, \(t=2,r=1,\delta=1\); the remaining
large cyclic direction is real. This proves the claimed boundary, including
the absence of a forced factor or second capacity multiplier.

## 9. General synchronized cyclic obstruction

Let two local quotient groups contain cyclic subgroups of the same prime
order \(R>B\). Identify them by an automorphism. Choose a quotient generator
`q` and assign every released block a nonzero power \(q^{a_i}\), using the
identified power in the other component. Each individual block has quotient
order `R`, because `R` is prime and \(a_i\ne0\). However, all blocks together
still generate only \(\langle q\rangle\), of order `R`.

For an exponent vector `v`, membership in the old subgroup and equality of
two quotient words are governed by linear congruences of the form

\[
\sum_i a_iv_i=0\pmod R.
\]

Applying an automorphism multiplies this expression by a unit modulo `R` and
does not change its kernel. Thus all membership and collision kernels are
synchronized across components, so the gcd mechanism has no mismatch to
factor. Such local data can be realized by choosing ambient cyclic unit
groups with the required subgroups and combining chosen local residues by
CRT. This gives the claimed abstract countermodel for arbitrarily many
named blocks.

It follows from first principles that individual beyond-cap order cannot
imply multiplicative capacity by block count. It also cannot imply relation
volume from provenance alone. The exact `341` construction shows that this
obstruction is compatible with the stated canonical-inverse and complete
joint-refinement provenance, not only with an abstract group model.

## 10. Quasipolynomial transcript condition

Let the complete encoded transcript have bit length
\(L\le 2^{\operatorname{poly}(\log n)}\). Then the number of blocks, bank
entries, relations, and provenance occurrences is at most `L`, and every
recorded exponent and coefficient has at most `L` bits.

- Modular multiplication, inversion, exponentiation, and gcd are polynomial
  in their operand bit lengths.
- The number of explicit pair comparisons is at most quadratic in the bank
  size.
- A Pohlig--Hellman digit scan has at most `q` candidates per digit, with
  \(q\le B\), and at most \(\log_2M\le n\) digits in total up to constant
  factors.
- Deterministic Hermite and Smith normal-form algorithms are polynomial in
  the matrix dimensions and coefficient bit lengths.
- At closure, \(\kappa(S)\) is at most the explicit bank size, so trial
  division up to \(\kappa(S)\) is quasipolynomial.

All these bounds are polynomial in quasipolynomial quantities, and hence
quasipolynomial in `n`.

A bound only on \(\kappa\), or only on retained-bank cardinality, does not
bound the transcript. Repeated first collisions with `e=1` can keep
\(\kappa\) fixed while adding a new block coordinate, an independent row,
word occurrences, and provenance. Coefficient and exponent encodings can
also grow. The full-encoding cap is therefore necessary for the stated
runtime conclusion. Nothing in the theorem supplies a compressed oracle
for an unencoded larger bank.

## 11. Remaining alternatives

The three final conditions target different missing inputs:

1. Frequent disjointness directly invokes the proven layer multiplier and
   grows the public lower bound.
2. Sufficient aligned collisions can make the relation lattice full rank;
   the additional equality \(D=M\kappa\) then invokes the proven exact
   closure.
3. Relative order against the subgroup generated by all earlier blocks
   tests the quantity that the individual order against `H_j` fails to
   control. An order greater than `B` gives disjoint current-subgroup layers;
   an order at most `B`, when supplied with its public membership witness,
   gives an aligned relation.

These mechanisms need not imply one another. The statement correctly lists
them as alternative possible source laws or procedures, not as equivalent
reformulations and not as consequences of the finite-bank theorem. The
legality wording of the `341` construction is also sufficient: it specifies
exact endpoint identities, least-positive inverse status, complete joint
gcd-free refinement, multiplicity, and occurrence provenance. Thus neither
the obstruction nor any progress alternative relies on unstated provenance.

## Final verdict

**VERIFIED — SHA-256
`8e47a9e249ff7f6fd7996664daddbbd53ace7dafd1e85b159ad20502a6d6fa19`.**

The fingerprint equivalence, factor-first synchronization, layer updater,
rank--capacity inequality, full-rank index closure, arbitrary odd
prime-power scope, quasipolynomial transcript condition, exact `N=341`
boundary, and the alternative/provenance wording all withstand independent
reconstruction. The theorem remains a finite-bank state theorem and does
not imply an all-input factoring algorithm.
