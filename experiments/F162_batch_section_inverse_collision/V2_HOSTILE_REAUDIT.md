# F162 V2 hostile re-audit — pass

## Verdict

**PASS.** V2 exactly repairs the V1 explicit-list input-cost defect. I found
no new mathematical, completeness, or quasipolynomial-cost defect.

The three frozen V2 hashes match the audit assignment:

```text
V2_STATEMENT.md  89eb6821c394e70b779a014212a1d5ac50f3658ccfe6ffd21248a27f244b4899
V2_PROOF.md      582c100d7e39f85bd1cd4c154e77d6dea9de98d91581db4a6a1771f7ec3cfaa1
V2_MANIFEST.md   c696512e238a0951b92e2616dce45daf0e6d29a3a302b1d4d328c9bd8acb4910
```

The preserved V1 files and failed audit also match the hashes pinned in the
V2 manifest:

```text
STATEMENT.md              0cbc91e95b6068674f04d96b7af281b5cb9a28505bbcede043f284a15f3ca89e
PROOF.md                  a4f1767cf71d1eeeec8334ae6e293143e8c4ed886b828d99e90d07ee3134dbc9
MANIFEST.md               451f164f5d46197192c977a3ae98093ccd11a7194d0acaa72d8db97b7ca9dde1
HOSTILE_AUDIT_FAILED.md   a22f1f0f5d12fdb3c96804b32b85f0adf79d374b2902830f84998f9e7213ea76
```

No frozen candidate file was changed.

## 1. The V1 defect is exactly repaired

The input is an explicit list of `r` positions. V1 incorrectly gave a total
cost that depended only on the number `m` of distinct residues. V2 adds

\[
\widetilde O(rn)
\]

for reading, canonicalizing, sorting, and deduplicating the list. This term
is necessary and sufficient at the declared soft-bit-complexity precision.
It also absorbs the polylogarithmic overhead of deterministic comparison
sorting and, if needed, unit gcd checks on the input positions.

V2 also separates all relevant storage terms:

- the resident explicit input uses `O(rn)` bits;
- the polynomial trees use soft-linear storage in `mn`;
- exact multiplicity counters use `O(m log(r+1))` bits;
- the detector can use one duplicate flag per value, and in fact its
  unconditional self screens do not require exact counts.

Thus the repaired total bound

\[
\widetilde O\!\left(
rn+(m(n+\log m))^{1+o(1)}
+m\,\mathsf M(n)\log n
\right)
\]

now covers the complete explicit-list detector. The repair does not alter
the detector or weaken its conclusion.

## 2. Product-polynomial algebra and derivative deflation pass

Fix a distinct list value `a` and a sign `epsilon`, and put

\[
x=\epsilon a^{-1}\pmod N.
\]

For each distinct value `b`,

\[
x-b=a^{-1}(\epsilon-ab)\pmod N.
\]

If `x` is absent from the distinct set, `P(x)` contains every possible
partner factor. If `x` is present, it is the unique distinct canonical
residue satisfying `ab=epsilon mod N`. That pair has gcd `N`, not a proper
factor. The exact composite-ring identity

\[
P'(x)=\prod_{b\ne x}(x-b)
\]

removes precisely this one globally improper partner. It remains true in
`Z/NZ` even when other differences are zero divisors. It uses no division
by a point difference.

Consequently, every proper distinct-value pair contributes a nonunit factor
to one tested aggregate. Both signs are handled symmetrically.

## 3. Duplicate positions and self screens pass

If two different input positions have the same residue `a`, their pair test
is

\[
\gcd(a^2-\epsilon,N).
\]

V2 tests both self signs for every distinct residue. Therefore
deduplication cannot lose a useful duplicate-position pair. Testing the same
scalar when the residue occurs once can only produce an additional correct
factor. It does not create a false output.

An exact global inverse partner can occur at many positions. Removing its
one distinct residue from the derivative product is still correct because
all pairs between `a` and that residue have the same improper gcd `N`.

## 4. Aggregate localization passes for arbitrary composites

If an aggregate gcd is proper, the algorithm returns it. If it equals `N`,
the scalar subproduct tree has leaves `x-b`, with the exact global partner
omitted. Every leaf is a nonzero difference of distinct canonical residues,
so

\[
0<|x-b|<N.
\]

No leaf gcd can equal `N`. At a node with gcd `N`, either a child has a
proper gcd, or one child still has gcd `N` and the descent continues. Two
unit children cannot have a nonunit product. The descent must therefore
return a proper divisor.

This argument tracks full prime-power divisibility. It does not assume that
`N` is squarefree or semiprime.

## 5. Composite-ring evaluation and cost pass

All product-tree and point-tree divisors are monic. Polynomial remainder
computation over `Z/NZ` therefore needs no inverse of a data-dependent
coefficient. Reversed fast division only inverts the constant coefficient
one. Repeated evaluation points are harmless because this is evaluation by
remainders, not interpolation.

The total degrees across each tree level are linear in `m`. Carry-safe
Kronecker multiplication gives the stated soft-linear cost in the
coefficient encoding. The inverse and gcd work fits the displayed
`m M(n) log n` term. Only one scalar localization is needed because a
successful localization terminates the algorithm.

The resulting cost is subquadratic in the explicit list length. If `r` is
quasipolynomial in the input bit length `n`, then `m<=r`, `log r` is
polylogarithmic, and every displayed time and storage term is also
quasipolynomial.

## 6. Shared-block normalization passes

For an owner subset `T`, the block product `C_T` is a public unit and

\[
a_{i,T}=q_iC_T^{-1}\pmod N
\]

is defined. If the exact parity-support intersection of records `i,j` is
`T`, the decorated product law gives

\[
a_{i,T}a_{j,T}
=q_iq_jC_T^{-2}
=Q(v_i\mathbin\triangle v_j)\pmod N.
\]

Thus the owner batch contains the literal F156 signed-product test. If the
true intersection is larger than `T`, the tested scalar is not that F156
star value, but a proper gcd of the public scalar is still a correct factor.
The larger owner list can add valid outputs but cannot add false outputs.

The incidence count `S_t` counts positions before each owner-list
deduplication. It therefore pays for the sum of all new `rn` normalization
terms. The sum of the post-deduplication list sizes is at most `S_t`, so the
product-tree and gcd work is soft-linear in the same total, with the stated
coefficient overhead. For a quasipolynomial explicit transcript and
polylogarithmic `t`, enumerating the subsets and all owner batches remains
quasipolynomial.

This proves only the bounded-intersection channel. V2 correctly makes no
claim that it compresses all dense intersections.

## 7. Frozen F157 evidence passes anew

Read-only inspection of the frozen F157 `OUTPUT.json` confirms all stated
counts for

\[
N=3{,}241{,}632{,}473=41{,}011\cdot79{,}043.
\]

- There are 65 serialized support-two hits.
- Their public `(q_mod_N,z,w)` values form eight groups with occurrence
  multiset `27,25,4,2,2,2,2,1`.
- All 65 plus-sign gcds are one.
- The minus-sign gcds expose `41011` in 63 records and `79043` in two.
- Exactly 28 records have both intersection support zero and `public_C=1`.
- The eight groups give eight distinct public adjusted scalars and eight
  distinct exact endpoint products.

For basis pair `(656,10097)`, the artifact gives

```text
public_C          = 1
q_i*q_j mod N     = 2922074762
gcd(q_i*q_j-1,N) = 41011
gcd(q_i*q_j+1,N) = 1
```

The recorded root data also satisfy

```text
z = 2907761921
w = 3157846
z^2 mod N = 2922074762
z*w mod N = 1
```

Therefore the empty-intersection owner list contains a useful signed pair.
The general theorem gives a public factor-free batch locator for this fixed
witness. The disclosed factors used by the registered discovery index are
not needed by this locator.

The grouping does not create new retained-relation rank. Equal public roots
have equal canonical inverses and equal exact endpoint products, so global
exact-value deduplication removes their occurrence multiplicity.

## 8. Scope and one presentation note

V2 proves a faster locator for an existing collision. It proves no collision
density, no all-input source law, no complete dense-intersection evaluator,
and no factoring algorithm. The four 58-bit controls constrain only the
adjusted support-at-most-two F156 channel, as stated.

There is one inherited Markdown typo in `V2_PROOF.md`: the display that ends
with `tag{20}` lacks its closing display delimiter. The intended formula and
all following reasoning are unambiguous. This is a presentation defect only;
it does not change the audit verdict.

The V2 theorem and its declared boundary pass hostile re-audit. An
independent statement-only reconstruction is still required before
promotion.
