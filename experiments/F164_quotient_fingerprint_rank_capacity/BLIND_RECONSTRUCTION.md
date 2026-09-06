# F164 blind reconstruction

## Audit result

**Statement SHA-256:**
`b45b07e7f97aad53d4a3fa15ce795db4a7bdf659f371bb70857668dae816af83`

**Verdict:** **FAIL as a literal, self-contained statement.** The fingerprint,
capacity, layer, rank, full-rank closure, and obstruction theorems reconstruct
correctly. The literal statement has two material scope defects:

1. The three conditions in Section 8 are alternative ways to obtain progress.
   They are not mathematically equivalent.
2. A cap on bank cardinality does not by itself give an end-to-end
   quasipolynomial bound for a repeated run. A collision-heavy run can keep the
   bank fixed while the number of blocks, relations, and provenance records
   grows without a bound in `n`.

The `N=341` arithmetic certificate is valid. The words “canonical-inverse”,
“legal”, and “joint gcd-free refinement” are not defined in the statement.
Their provenance semantics therefore cannot be proved from this statement
alone. The displayed integer identities and all group-theoretic properties
needed by F164 do verify directly.

Under these corrections, the central theorem passes.

## 1. Fingerprint equivalence

Fix a hidden component `R_j=p_j^{alpha_j}`. Its unit group `U_j` is cyclic
because `p_j` is odd. Its order is divisible by `M`, since `g` has order `M`.
In a cyclic group, the kernel of the map

\[
q_M:U_j\longrightarrow U_j,\qquad y\longmapsto y^M
\]

has size

\[
|\ker q_M|=\gcd(M,|U_j|)=M.
\]

The cyclic group `U_j` has one subgroup of order `M`. Hence

\[
\ker q_M=\langle g\bmod R_j\rangle=H_j.
\]

For public exponent vectors `u,v`, all words are units, so

\[
\begin{aligned}
F(u)=F(v)\pmod {R_j}
&\iff (d^u)^M(d^v)^{-M}=1\pmod {R_j}\\
&\iff (d^{u-v})^M=1\pmod {R_j}\\
&\iff d^{u-v}\in H_j.
\end{aligned}
\]

Thus equality of fingerprints modulo `R_j` is exactly equality of quotient
cosets modulo `H_j`. Negative exponents cause no issue because every `d_i` is
a unit.

## 2. Factor-first equality partitions

For one pair, put `Delta=F(u)-F(v)` and compute `gcd(Delta,N)`.

- If the gcd is `N`, the fingerprints agree modulo every `R_j`.
- If the gcd is `1`, `Delta` is nonzero modulo every hidden prime `p_j`.
  It is therefore nonzero modulo every `R_j`.
- Any other gcd is a proper divisor of `N`. This includes partial agreement
  modulo a prime or a prime power.

Consequently, after every proper gcd has been returned, any two fingerprints
are either equal modulo all hidden components or unequal modulo all hidden
components. This proves the claimed synchronized equality partition.

## 3. Finite-bank capacity

Let

\[
K_j=\langle H_j,d_1,\ldots,d_t\rangle\le U_j.
\]

On the no-factor branch, the `kappa(S)` distinct public fingerprints give
`kappa(S)` distinct elements of `K_j/H_j` for every `j`. Therefore

\[
|K_j/H_j|\ge \kappa(S)
\]

and

\[
|K_j|=|H_j|\,|K_j/H_j|\ge M\kappa(S).
\]

If `S` grows by inclusion, its set of fingerprint values can only grow.
Thus `kappa(S)` and the lower bound are public and monotone.

## 4. One-block layer updater

Let `T` contain one representative of each old fingerprint. For words
`w,w'` in `T`, commutativity gives

\[
F(d^e w)-F(d^e w')
=d^{eM}\bigl(F(w)-F(w')\bigr)\pmod N.
\]

The multiplier is a unit. Hence every within-layer equality and gcd outcome
is the old one. Only comparisons between different layers are new.

Suppose the first cross-layer equality occurs between `d^e w` and `d^f w'`,
where `f<e`. Every pair in layers `0,...,e-1` was already tested. On the
no-factor branch those `e` layers are disjoint in every hidden quotient.
Each layer has `kappa` values, so their union has exactly `e*kappa` values.

The collision gives

\[
x=d^{e-f}ww'^{-1},\qquad x^M=1\pmod N.
\]

The fingerprint lemma implies `x in H_j` in every hidden component. Thus
there is a unique local exponent `a_j mod M` such that

\[
x=g^{a_j}\pmod {R_j}.
\]

### Factor-first alignment from the stated assumptions

The common exponent can be found without knowing the factorization of `N`.
Write the supplied factorization as

\[
M=\prod_\ell \ell^{q_\ell}.
\]

For one factor `ell^q`, project `x` and `g` to their `ell`-primary parts by
raising them to `M/ell^q`. Extract the base-`ell` digits of the discrete log.
At each digit there are `ell` public candidates. Compare the current target
with every candidate by a gcd with `N`.

If the local digit differs between hidden components, the candidate that
matches any nonempty proper set of components gives a proper gcd. If no
proper gcd occurs, one candidate agrees modulo all of `N` and gives the
common digit. Repeat for all digits and combine the primary logs by the
Chinese remainder theorem. The result is either a factor or one public
`a mod M` with

\[
x=g^a\pmod N.
\]

The resulting relation row has coefficient `e-f != 0` on the newly
introduced block. Every old row has coefficient zero there. The new row is
therefore rationally independent of all old rows.

If no cross-layer collision occurs through layer `B`, the `B+1` layers are
disjoint in every hidden quotient. Their union has exactly
`(B+1)*kappa` fingerprints.

For the first block, take `T={1}`. A collision between exponents `e>f`
would say `d^(e-f) in H_j`, with `1 <= e-f <= B`. A local relative order
larger than `B` rules this out in every component. The first block must
therefore take the no-collision branch. The same argument fails for later
blocks because `ww'^{-1}` can represent a nontrivial element generated by
old blocks.

The terminal trichotomy is best stated as follows: return a factor; else
return the first aligned relation; else retain all `B+1` layers. As written,
items 1 and 2 overlap syntactically because item 2 also lets its alignment
step return a factor. This is an editorial overlap, not an algebraic error.

## 5. Rank-capacity law

Start with the base row `(M,0,...,0)`, no blocks, and `kappa=1`. Process one
new block per call and stop if a factor appears. Retain the first collision
row from each collision call.

Each collision row is independent of all preceding rows because it is the
first row with a nonzero coefficient in its new coordinate. If `r` is the
number of such rows, their rank in addition to the base row is exactly `r`.

Let `c` be the number of no-collision calls. Then

\[
t=r+c,\qquad \delta=t-r=c.
\]

Every no-collision call multiplies `kappa` by `B+1`. A collision at first
index `e` multiplies it by `e >= 1` if the earlier layers are retained.
Induction gives

\[
\kappa\ge (B+1)^c=(B+1)^\delta.
\]

Thus every non-factor call either adds one independent exposed relation or
adds one factor of `B+1` to the certified quotient capacity. The result does
not imply `delta=0`. A first beyond-cap block gives at least one
no-collision call, so it creates an unresolved quotient direction.

For a preloaded state, the normalized form is

\[
\kappa/\kappa_0\ge
(B+1)^{(t-r)-(t_0-r_0)}.
\]

Equation (10) uses the base initialization above.

## 6. Full-rank index closure

For each component define the surjective homomorphism

\[
\phi_j:\mathbf Z^{t+1}\longrightarrow K_j,
\qquad
(z,v)\longmapsto g^z d^v\pmod {R_j}.
\]

Every retained row is an exact global relation. Therefore

\[
L\subseteq \ker\phi_j
\]

for every `j`. If `L` has full rank, set

\[
A=\mathbf Z^{t+1}/L,
\qquad |A|=D.
\]

The map `phi_j` factors as a surjection `A -> K_j`. Hence

\[
|K_j|\mid D,
\qquad |K_j|\le D.
\]

Combining this with the bank lower bound proves

\[
M\kappa(S)\le |K_j|\le D.
\]

If `D=M*kappa(S)`, both inequalities are equalities. Each map `A -> K_j`
is then an isomorphism. Since `K_j` is a subgroup of the cyclic group
`U_j`, it is cyclic. Thus `A` is cyclic of order `D`.

Smith normal form both verifies this cyclic invariant-factor shape and gives
an exponent vector whose class generates `A`. Evaluate that vector as a
public word `h`. Its image generates every `K_j`, so

\[
\operatorname{ord}_{R_j}(h)=D
\]

for every `j`. Its order modulo `N` is also `D` because it is the least
common multiple of identical local orders.

If `gcd(D,N)>1`, it is automatically a proper factor. Indeed, because
`D=|K_j|` divides

\[
\varphi(p_j^{\alpha_j})=p_j^{\alpha_j-1}(p_j-1),
\]

the `p_j`-adic exponent in `D` is at most `alpha_j-1`. Hence `N` cannot
divide `D`. On the no-factor branch, `gcd(D,N)=1`.

Also, `kappa(S) <= |S|`. If the explicit bank has quasipolynomial
cardinality, trial division through `sqrt(kappa(S))` is quasipolynomial in
`n`. It gives the complete factorization of `kappa(S)`. Combining it with
the supplied factorization of `M` gives the factorization of `D`.

If the next use requires every prime factor of the common order to be at
most its scan cap, the cap may need an update. A prime factor of `kappa`
can exceed the old `B`. Choosing a new cap at least the largest prime factor
of `kappa` preserves quasipolynomial size because that factor is at most
`kappa <= |S|`. The claim that `(h,D)` is a next state is valid with this
cap update, or if the state definition requires only an exactly factored
common order.

If `L` is not full rank, `A` is infinite and supplies no finite order upper
bound. If `L` is full rank but `D>M*kappa`, the surjections can have
nontrivial kernels. Neither case certifies the exact local subgroup order.

## 7. The `N=341` certificate

The stated inverse identities are exact:

\[
337\cdot85=28645=1+84\cdot341,
\]

\[
325\cdot277=90025=1+264\cdot341.
\]

Also,

\[
\gcd(337,341)=\gcd(277,341)=\gcd(337,277)=1.
\]

Thus `d_1=337=-4` and `d_2=277=-64` are pairwise-coprime units. The
undefined provenance vocabulary aside, the required arithmetic is valid.

For `g=-1` and `M=2`, `g` has exact order two modulo both 11 and 31. The
local powers through exponent five are:

| component | `d_1 mod p` | powers `1,...,5` | `d_2 mod p` | powers `1,...,5` |
|---|---:|---|---:|---|
| 11 | 7 | `7,5,2,3,10` | 2 | `2,4,8,5,10` |
| 31 | 27 | `27,16,29,8,30` | 29 | `29,4,23,16,30` |

The value at exponent five is `-1` in each case. No earlier value is
`+1` or `-1`. Hence both relative orders modulo `{+1,-1}` are exactly five.

The pure fingerprint scans through `B=2` have values

\[
d_1:\quad 1,16,256,
\qquad
d_2:\quad 1,4,16
\pmod {341}.
\]

Every within-list nonzero difference has gcd one with 341. Thus both scans
reach the beyond-cap branch without a factor.

Finally,

\[
d_2d_1^2=(-64)(-4)^2=-1024=-1-3\cdot341=g\pmod {341}.
\]

In fact `d_2=d_1^3` as integers and `d_1^5=g mod 341`. Therefore the two
blocks generate only one quotient direction of order five. With coordinates
`(z,v_1,v_2)`, the bank exposes the relation

\[
(-1,2,1),
\]

while the remaining order relation can be represented by

\[
(-1,5,0).
\]

Its coefficient five lies beyond `B=2`. This proves the advertised
obstruction. A larger bank can still fill previously unsampled cosets of
the same order-five quotient. What is not forced is a second independent
factor of quotient-subgroup growth.

## 8. General cyclic countermodel

Let both hidden quotient groups be copies of the cyclic group `C_R`, where
`R>B` is prime. Choose nonzero residues `a_1,...,a_t mod R`. Map the `i`th
block in the first quotient to `c^{a_i}`. In the second quotient, map it to
`c'^{lambda*a_i}`, where `lambda` is nonzero modulo `R`.

For an exponent vector `v`, quotient membership in the base subgroup is
equivalent to

\[
\sum_i a_i v_i=0\pmod R.
\]

The second component gives the same condition after multiplication by
`lambda`. Hence the two membership kernels, and therefore all quotient
collision kernels, are identical. Every named block has quotient order `R`
because every `a_i` is nonzero. The joint image is still only `C_R`,
independent of `t`.

This is a complete abstract countermodel to any conclusion that block count
alone forces quotient rank or multiplicative volume. It does not by itself
prove that every arbitrary external provenance system can realize every
such list of blocks. The `N=341` construction supplies one concrete
provenance-compatible two-block instance claimed by the statement, subject
to the imported meaning of “legal”.

## 9. Exact quasipolynomial scope

Let `K` be the bank cardinality. Let `E` be the total bit length of the bank,
the exponent vectors, the retained relation rows, and their provenance. Let
`t` be the number of block coordinates. The claimed cost follows when

\[
B,K,E,t\le 2^{(\log n)^{O(1)}}.
\]

The reasons are direct:

- There are `K^2` fingerprint comparisons.
- Modular powering costs a polynomial in `n` and in the exponent bit length.
- One factor-first alignment tests at most
  `sum_(ell^q || M) q*ell <= B*log_2(M) = O(Bn)` digit candidates.
- Deterministic Hermite and Smith algorithms are polynomial in matrix
  dimensions and coefficient bit lengths.
- Trial division of `kappa <= K` takes at most `sqrt(K)` divisions.

All these quantities remain quasipolynomial under the displayed total-input
bound.

Bank cardinality alone is not enough. Choose every later quotient block as
a power of the first quotient generator. Each call can collide at `e=1`,
add a new coordinate and a new independent cross relation, and leave
`kappa` unchanged. Thus an arbitrary number of calls can fit under a fixed
bank-cardinality cap. A repeated algorithm needs a quasipolynomial bound on
the number of calls, or equivalently on the total retained transcript and
provenance size, in addition to its bank cap.

The method explicitly evaluates the bank. Nothing in the argument gives a
compressed evaluator for a bank whose expanded size is super-quasipolynomial.

## 10. Remaining-condition claim

The obstruction is correctly identified: individual order larger than `B`
against `H_j` does not imply order larger than `B` against the quotient
subgroup generated by old blocks.

The final list should not call its three items equivalent.

- Frequent disjoint layers give capacity growth. They need not give full
  relation rank or `D=M*kappa`.
- Enough aligned collisions plus index equality give exact closure. They
  need not imply frequent disjoint layers.
- A procedure that determines relative order against the old generated
  quotient can decide which of these mechanisms is available. To produce
  an aligned relation on the membership branch, it must also return a public
  membership word or equivalent witness.

These are related alternative progress mechanisms. No implication in the
statement proves them equivalent. The word “smallest” also has no formal
meaning unless the statement defines an ordering on missing assumptions.

## Final classification

- **Fingerprint equivalence:** PASS.
- **Factor-first equality partition:** PASS.
- **Finite-bank capacity:** PASS.
- **One-block updater and independent relation:** PASS, with the trichotomy
  phrased disjointly.
- **Rank-capacity law:** PASS from the base initialization; use the normalized
  formula for a preloaded state.
- **Full-rank `D=M*kappa` closure and common-order SNF word:** PASS.
- **`N=341` arithmetic and group certificate:** PASS. Imported provenance
  legality is not self-contained.
- **General synchronized cyclic countermodel:** PASS as an abstract quotient
  model.
- **Quasipolynomial cost:** PASS only under a quasipolynomial total-encoding
  and run-length bound. A bank-cardinality cap alone is insufficient.
- **Three “equivalent” remaining conditions:** FAIL. They are alternatives,
  not equivalent propositions.

Therefore the central F164 result is sound, but the complete statement is
**FAIL** until its complexity scope and final equivalence wording are fixed.
