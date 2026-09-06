# F162 hostile audit — failed on explicit-list input cost

## Verdict

**FAIL as frozen.** The signed-inverse product-polynomial theorem, derivative
deflation, factor localization, shared-block normalization, and frozen F157
consequence all pass. However, the displayed cost for the **complete**
detector depends only on the number `m` of distinct residues. It omits the
time needed to read and deduplicate the supplied list of `r` source
positions. This is false when the list has many duplicates.

The frozen inputs were verified before review:

- `STATEMENT.md`:
  `0cbc91e95b6068674f04d96b7af281b5cb9a28505bbcede043f284a15f3ca89e`;
- `PROOF.md`:
  `a4f1767cf71d1eeeec8334ae6e293143e8c4ed886b828d99e90d07ee3134dbc9`.

No frozen candidate file was changed.

## 1. Exact cost defect

The input is an explicit list

\[
a_1,\ldots,a_r.
\]

The algorithm first replaces this list by its distinct residue set `A`, of
size `m`. Equation (7) then claims that the complete detector costs

\[
\widetilde O\!\left((m(n+\log m))^{1+o(1)}
+m\,\mathsf M(n)\log n\right).
\]

This expression has no dependence on `r`. An algorithm cannot in general
deduplicate an explicit `r`-position list without reading its positions.
This is not only a representation objection. For example, fix `N=15` and
compare these lists:

```text
(1,1,...,1)
(1,1,...,1,4)
```

The last position in the second list creates the proper pair screen

\[
\gcd(1\cdot4-1,15)=3.
\]

The all-one list has no proper self screen. Thus a complete detector must
inspect the last position. The second list has only `m=2` distinct values,
so the frozen bound is constant in `r` for fixed `N`, while the required
input scan is linear in `r`.

The minimal repair is to add the normalization term

\[
\boxed{
\widetilde O\!\left(
rn+(m(n+\log m))^{1+o(1)}
+m\,\mathsf M(n)\log n
\right).
}
\]

Equivalently, the theorem can take a deduplicated set plus duplicate flags
as its input and state that the displayed bound starts after normalization.
If exact multiplicity counters are retained, their `O(m log r)` bits must
also be included in the storage statement. The proof does not use full
counts, so one duplicate flag per value is sufficient.

This repair preserves near-linear dependence on the explicit list size. It
also preserves the claimed subquadratic and quasipolynomial consequences.

## 2. General detector — algebra passes

For fixed `a` and sign `epsilon`, put

\[
x=\epsilon a^{-1}\pmod N.
\]

Then every distinct value `b` satisfies

\[
x-b=a^{-1}(\epsilon-ab)\pmod N.
\]

If `x` is not in `A`, ordinary evaluation includes every partner. If `x` is
in `A`, it is the unique distinct canonical value with
`ab=epsilon mod N`. It is a globally improper partner. The exact identity

\[
P'(x)=\prod_{b\in A,\ b\ne x}(x-b)
\]

removes only that value. It remains valid over `Z/NZ`, including when other
differences are zero divisors. No division by a point difference occurs.

Equal source positions are also handled correctly. If two positions have
the same residue `a`, their pair screen is `gcd(a^2-epsilon,N)`. Testing the
same scalar when `a` occurs once is an extra valid factor test. It cannot
produce an incorrect output. Both signs are treated symmetrically.

If an aggregate gcd equals `N`, the scalar product-tree descent is complete.
At a node, a child gcd is one, proper, or `N`. Two unit children cannot have
a nonunit product. A leaf is a nonzero canonical difference with absolute
value below `N`, so its gcd cannot equal `N`. The descent must therefore
encounter a proper factor. This proof works for arbitrary composites and
prime powers. It does not use a semiprime or squarefree assumption.

As a counterexample search, I checked every distinct unit set of size at
most four for every `2 <= N <= 35`, across both signs. All 111,223 sets
satisfied the claimed detection implication. This finite check supports the
proof; it is not used as proof.

## 3. Composite-ring evaluator — pass after input normalization

The product polynomial and point polynomials are monic. Polynomial division
by a monic divisor is valid over every commutative ring. Reversed Newton
division only needs the inverse of the constant coefficient `1`. Thus the
product and remainder trees do not invert a data-dependent residue.

Carry-safe Kronecker packing gives the stated soft-linear dependence on the
post-deduplication coefficient encoding. Formal differentiation is valid
over `Z/NZ`. Duplicate evaluation points also cause no problem because the
remainder tree does not use interpolation or divide by point differences.

The product-polynomial work, inverse computations, gcd tests, and the one
possible localization therefore fit the frozen `m`-dependent terms. Only
the omitted `r`-position normalization term fails.

## 4. Shared-block normalization — pass

For an owner subset `T`, every block product `C_T` is a unit modulo `N`.
The public normalized value

\[
a_{i,T}=q_iC_T^{-1}\pmod N
\]

is therefore defined. If

\[
v_i\cap v_j=T,
\]

then

\[
a_{i,T}a_{j,T}
=q_iq_jC_T^{-2}
=Q(v_i\mathbin\triangle v_j)\pmod N.
\]

Thus both F156 sign screens are exactly signed-inverse screens in the
`T` owner list. If the real intersection strictly contains `T`, the tested
scalar is not the adjusted F156 star value. A proper gcd of that public
scalar is still a valid factor. The statement correctly does not call such
an output an F156 pair hit.

The owner-incidence quantity `S_t` counts input positions before per-list
deduplication, so it already covers the duplicate-scan cost in this
specialization. For fixed polylogarithmic `t` and a quasipolynomial explicit
transcript, each binomial sum and their total remain quasipolynomial. The
bounded-intersection theorem is correct. It does not compress every dense
intersection.

## 5. Frozen F157 evidence — pass

Read-only regrouping of the frozen `OUTPUT.json` confirms:

- 65 successful support-two occurrences;
- eight distinct public `(q_mod_N,z,w)` triples, with occurrence multiset
  `27,25,4,2,2,2,2,1`;
- all 65 are minus-sign hits and all plus gcds are one;
- 63 hits expose `41011` and two expose `79043`;
- exactly 28 hits have empty intersection and `public_C=1`;
- basis pair `(656,10097)` has
  `q_i*q_j mod N = 2922074762`, and
  `gcd(2922074762-1,3241632473)=41011`.

The eight triples also give eight distinct exact products `zw`. Hence each
occurrence group collapses to one exact feedback value under the declared
global exact-value deletion rule.

Because one empty-intersection pair is useful, the single empty-owner batch
must return a public factor without disclosed factors. The corrected input
scan remains near-linear in the 11,874-position owner list, so the fixed
subquadratic locator claim survives.

The artifact also keeps the right boundaries. The repeated occurrences do
not become new P108 cross-layer directions after exact-value deduplication.
The four 58-bit controls exclude only adjusted F156 support-at-most-two hits.
They do not exclude extra hits in an uncorrected owner batch. No collision
density, all-input source law, or factoring algorithm is claimed.

## 6. Required next version

Freeze a V2 statement and proof that do one of the following:

1. include the `r`-position read and deduplication term in the total bit
   cost; or
2. define the detector input as an already normalized distinct set with the
   needed duplicate metadata, and state the separate normalization cost.

No algebraic, shared-block, or F157 certificate change is required. A fresh
hostile audit and a statement-only reconstruction are still required before
promotion.
