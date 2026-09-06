# F162 V2 blind reconstruction

## Protocol and verdict

The SHA-256 of the only source read for this reconstruction,
`V2_STATEMENT.md`, is

```text
89eb6821c394e70b779a014212a1d5ac50f3658ccfe6ffd21248a27f244b4899
```

It matches the required hash. No proof, audit, manifest, F157 artifact, or
other F162 file was read. No experiment or mathematical computation script
was run.

**Core verdict: proved.** The signed pair-product detector, derivative
deflation, duplicate handling, monic composite-ring evaluation, and
localization are correct for every `N >= 2` under the stated hypothesis that
the input values are units. The shared-block application is correct whenever
the source supplies the invertibility and multiplicative set identity used by
its displayed formulas.

**Evidence verdict: conditional.** The inventory of 65 F157 occurrences,
their grouping, and the count of empty intersections are finite-data claims.
They cannot be independently recovered from the statement alone. Their
arithmetic consequences and the use of the displayed empty-intersection
witness can be checked from the statement and are correct.

## 1. Pair-product detector

Use canonical representatives in `[0,N-1]`. Deduplicate the position list to
the set `A`, and form

\[
P(X)=\prod_{b\in A}(X-b)\quad\text{in }(\mathbb Z/N\mathbb Z)[X].
\]

For a fixed `a in A` and sign `epsilon`, let

\[
x=\epsilon a^{-1}\pmod N.
\]

For every divisor `d` of `N`, multiplication by `a` is invertible modulo
`d`. Hence

\[
d\mid ab-\epsilon
\quad\Longleftrightarrow\quad
d\mid b-x,
\]

and consequently

\[
\gcd(ab-\epsilon,N)=\gcd(b-x,N).
\tag{1}
\]

Suppose distinct source positions contain values `a` and `b` and satisfy

\[
1<\gcd(ab-\epsilon,N)<N.
\tag{2}
\]

First assume `a != b` as canonical residues. Equation (2) also implies
`b != x`: equality would give `ab = epsilon mod N` and gcd `N`.

If `x` is not in `A`, the factor `x-b` occurs in `P(x)`. If `x` is in `A`,
the same factor occurs in `P'(x)` after the exact root at `x` is removed, as
proved in the next section. Thus, in either case, every divisor in (2)
divides `H_{a,epsilon}`. Therefore

\[
\gcd(H_{a,\epsilon},N)>1.
\]

If this gcd is less than `N`, it is already a proper factor. If it is `N`,
the scalar descent in Section 4 returns a proper factor. This proves the
detector implication for unequal values.

The proof uses only divisibility and unit multiplication. It does not assume
that `N` is squarefree, odd, or a product of two primes. It works for prime
powers and composites with any number of prime-power components. For prime
`N`, condition (2) is impossible, so the implication is vacuous. For `N=2`,
the two signs coincide, which only duplicates a query.

## 2. Exact-global-partner derivative deflation

Assume `x in A`. Since `A` contains distinct canonical residues, write

\[
P(X)=(X-x)R(X),
\qquad
R(X)=\prod_{b\in A,\ b\ne x}(X-b).
\]

Formal differentiation is valid over every commutative ring:

\[
P'(X)=R(X)+(X-x)R'(X).
\]

Evaluation at `x` gives the exact identity

\[
P'(x)=R(x)=\prod_{b\in A,\ b\ne x}(x-b).
\tag{3}
\]

No division by `X-x`, by `P'(x)`, or by a residue occurs. Ordinary evaluation
would be zero modulo all of `N` because it contains the factor `x-x`.
Equation (3) deletes exactly that one distinct global root and retains every
other value, including every value responsible for a proper collision.

Deduplication is essential to the clean identity. If the polynomial retained
the source multiplicity of `x`, its derivative could retain another factor
`x-x`. Deduplicating first turns all exact global partners with the same value
into one polynomial root; removing that value is sufficient because an exact
partner alone has gcd `N`, not a proper gcd.

## 3. Equal-value positions and self screens

If the two distinct source positions have the same canonical value `a`, their
pair screen is exactly

\[
\gcd(a^2-\epsilon,N).
\]

Testing this expression for both signs and every distinct `a` therefore
recovers every proper collision lost by position deduplication. The test can
also return a proper factor when `a` occurs only once. That is harmless: the
returned gcd is still a public proper divisor of `N`; the theorem does not
require every returned factor to have a distinct-position provenance.

If a self screen is `1`, it gives nothing. If it is `N`, it is an exact global
self relation and gives no proper factor. It can simply be ignored. A
collision between `a` and some other value remains in the derivative or
ordinary product evaluation.

Because every self screen is run unconditionally, multiplicity counters are
not needed for correctness. A duplicate bit per distinct value is sufficient
if duplicate provenance is desired; even that bit is unnecessary for the
factor detector itself. Exact counters are a valid optional representation
and use at most `O(m log(r+1))` bits.

## 4. Composite-ring evaluation and localization

### Monic product and remainder trees

All root polynomials `X-b` and all query polynomials `X-x` are monic.
Polynomial division by a monic polynomial is exact over any commutative
coefficient ring: the leading term is cancelled using the coefficient `1`,
so no coefficient inverse is required. Equivalently, fast reversed-polynomial
division only inverts a power series with constant term `1`. Thus balanced
product and remainder trees evaluate `P` and `P'` at all query points over
`Z/NZ` without knowing a factor of `N` and without assuming that a
data-dependent residue is a unit. At a leaf,

\[
F(X)\bmod (X-x)=F(x).
\]

Repeated query points do not invalidate this procedure; they only repeat an
evaluation.

The only residue inverses used by the general algorithm are the declared
input-unit inverses `a^{-1}`. Extended Euclid computes them without a
factorization of `N`.

### Scalar localization when the product gcd is `N`

For a fixed query, make a scalar product tree whose leaves are the integer
differences

\[
\ell_b=x-b,
\]

excluding `b=x` in the derivative case. Store node products modulo `N`.
If the root gcd is `N`, at least one child product has gcd greater than `1`;
otherwise both children would be units and so would their product. Choose a
child with gcd greater than `1` and continue. A proper child gcd can be
returned immediately, or descent can continue until a leaf while preserving
the invariant that the chosen node has nontrivial gcd with `N`.

At a leaf, `x` and `b` are distinct canonical representatives. Therefore

\[
0<|x-b|<N.
\]

Its gcd with `N` cannot be `N`. The invariant says that it is greater than
`1`, so it is a proper factor. This argument remains valid when prime-power
valuations are split among several leaves: an internal node may then have gcd
`N` although no leaf does, and the descent finds a proper nonunit leaf or an
earlier proper child product.

This proves both correctness and termination of localization over arbitrary
composite rings.

## 5. Bit cost and storage

Let `n=ceil(log2(N+1))`. With the normal explicit-residue encoding, each
position occupies `O(n)` bits.

* Reading the `r` positions costs `Omega(rn)` and `O(rn)`. Canonical modular
  reduction is soft-linear in the same input size. A deterministic comparison
  sort costs `O(rn log r)` bit operations, and a deterministic radix sort can
  avoid the comparison factor. Either is `tilde O(rn)`, so the first term in
  (7) correctly pays for reading, canonicalization, and deduplication. If the
  source instead permits representatives with more than `O(n)` encoded bits,
  their actual encoded length must replace `rn`.

* Balanced multiplication of degree-`k` polynomials with `n`-bit modular
  coefficients can be reduced to integer multiplication on
  `O(k(n+log k))` bits. Summed over product and remainder tree levels, building
  `P`, building the query trees, and evaluating `P` and `P'` cost

  \[
  \widetilde O\!\left((m(n+\log m))^{1+o(1)}\right).
  \]

* There are `O(m)` inversions, terminal gcds, and self gcds. The safe bound

  \[
  \widetilde O\!\left(m\,\mathsf M(n)\log n\right)
  \]

  covers them. At most one scalar localization is needed before the algorithm
  returns, and its product and gcd work is also covered.

These parts give (7). A balanced tree has `O(m)` coefficients at each level,
so post-normalization working storage is `tilde O(mn)` bits. Resident input
storage is `O(rn)` bits. Optional exact multiplicities use the stated
`O(m log(r+1))` bits.

The precise conclusion is that the detector removes the `Theta(r^2)` pair
enumeration and is quasi-linear, up to coefficient arithmetic and soft
factors, in the encoded explicit list. The phrase “subquadratic in the list
length” is correct in this input-size sense, or as dependence on `r` with
coefficient size accounted for separately. It is not a uniform `o(r^2)` bit
bound as a function of `r` alone if `n` is allowed to grow faster than `r`,
because merely reading `r` residues then costs more than `r^2` bits.

If `r` is quasipolynomial in `n`, then `m <= r`, `log m` is polylogarithmic,
and every term in (7) is quasipolynomial in `n`. Thus the stated general
quasipolynomial conclusion follows.

## 6. Shared-block normalization

The application uses two source-interface facts that are implicit in (9) and
(12): every required `C_T` and normalized value is a unit modulo `N`, and
`Q` obeys the multiplicative set identity

\[
Q(U\mathbin\triangle V)
=Q(U)Q(V)Q(U\cap V)^{-2}.
\tag{4}
\]

For the usual definition of `Q` as a product of the block values, (4) follows
by writing the two sets as their intersection and two disjoint remainders.
If the source does not guarantee these unit conditions, (9) may be undefined
and the general theorem cannot be invoked as written. A nonunit block or
root with a proper gcd would itself reveal a factor, but that boundary case
is separate from the displayed normalization.

Let `v_i intersect v_j=T`. Applying (4) and the definition of `C_T` gives

\[
Q(v_i\mathbin\triangle v_j)
=q_iq_jC_T^{-2}
=(q_iC_T^{-1})(q_jC_T^{-1})
=a_{i,T}a_{j,T}\pmod N.
\]

Both owners occur in `I_T`. The general theorem therefore finds a factor
whenever this corrected pair product has a proper signed screen. This remains
true if the two normalized values are equal, because the unconditional self
screen handles their two distinct owner positions.

If the true intersection is `U` with `T` a strict subset of `U`, the batch
product is generally the star value multiplied by
`(C_U/C_T)^2`. It need not represent the corrected F156 pair. Nevertheless,
any gcd strictly between `1` and `N` is still a genuine factor. Such a pair
can create an extra output, but never an incorrect factor output.

For cap `t`, every exact intersection of size at most `t` is enumerated as a
subset for each of its two owners. Hence every corresponding support-two hit
is included. The total number of owner records presented to all lists is
exactly

\[
S_t=\sum_i\sum_{k=0}^{\min(t,|v_i|)}\binom{|v_i|}{k}.
\]

Consequently the sum of all per-list read and normalization terms is
`tilde O(S_t n)`, with the encoding cost of block-set keys included. The sum
of the polynomial costs is bounded by the same quasi-linear polynomial-tree
bound evaluated at total distinct size at most `S_t`; the gcd and coefficient
costs scale in the stated way. Subset products can be generated along the
subset enumeration tree, so their construction does not require a fresh
`|T|`-fold product for every incidence.

To check the quasipolynomial bound, let the encoded frozen transcript have
quasipolynomial size `L(n)`. Then the number of owners and every support size
are at most `L(n)`. For `t=polylog(n)`,

\[
S_t\le r(t+1)L(n)^t,
\]

and the logarithm of the right-hand side is still polylogarithmic in `n`.
Thus `S_t` and the combined capped detector are quasipolynomial.

For `T=emptyset`, `C_T=1`, all owners occur in one list, and
`a_{i,T}=q_i`. Exact disjointness makes `q_iq_j` the corrected star value, so
the batch detects every proper signed disjoint-support hit. Intersecting
supports can again create only an extra genuine factor screen.

## 7. Fixed F157 claims

The stated occurrence counts are internally consistent:

\[
25+27+4+2+2+2+2+1=65,
\qquad
63+2=65.
\]

If `w` is the canonical inverse associated with the unit `z`, equal `z`
does determine the same `w`, and the same triple `(q_mod_N,z,w)` determines
the same scalar test and feedback value. Under the stated exact-value deletion
rule, retaining one value per identical triple therefore collapses each group
to one value. This proves the logical compression from the asserted grouping;
it does not independently establish that the serialized data really has
those groups. The claims “eight groups,” “28 empty intersections,” and the
63-to-2 factor split require the omitted finite certificates for an
independent data audit.

The displayed empty-intersection witness is arithmetically sufficient. From
the statement,

\[
3{,}241{,}632{,}473=41{,}011\cdot79{,}043
\]

and

\[
2{,}922{,}074{,}762-1
=2{,}922{,}074{,}761
=41{,}011\cdot71{,}251.
\]

The Euclidean algorithm gives `gcd(71,251,79,043)=1`, so

\[
\gcd(2{,}922{,}074{,}762-1,3{,}241{,}632{,}473)=41{,}011,
\]

a proper factor. The basis indices are distinct and `C=1`. Conditional only
on the statement's assertion that this pair is present in the public owner
list, the general theorem proves that the single empty-block batch finds a
factor. The algorithm itself computes the terminal gcd and does not need the
displayed factorization of `N`; that factorization is used here only to check
the claimed arithmetic consequence.

The contextual claims about earlier numbered results and cross-layer rank
are not derivable from this statement-only source because those objects and
results are not defined here. They are not needed for the batch theorem or
the empty-block implication.

## 8. Remaining limitations

All essential limitations in the statement are real.

1. The theorem is conditional on an existing proper collision. Product and
   remainder trees aggregate tests; they do not prove that any test is
   nontrivial. No lower bound on collision count follows.

2. A cap `t` covers only pairs whose exact intersection has size at most
   `t`. Covering dense exact intersections by a pair scan can restore
   quadratic dependence on the owner count. If that owner count is
   quasipolynomial, its square is still quasipolynomial, so “loses the
   subquadratic advantage but remains quasipolynomial” is consistent. If one
   instead enumerates every subset using (13) with `t=max |v_i|`,
   quasipolynomial transcript size alone does not make that subset expansion
   quasipolynomial; one additionally needs polylogarithmic support size or a
   direct bound on the resulting `S_t`.

3. A negative result for corrected support-at-most-two star values does not
   decide the larger uncorrected channel. For true intersection `U`, an
   empty-block product differs from the star value by the unit square
   `C_U^2`. Multiplying by that square can change a signed congruence on a
   proper component of `N`. Thus an extra uncorrected hit is logically
   possible even when the corrected screen is absent.

4. The method selects one pair-product channel. It neither covers all
   intersection-corrected F156 pairs without sufficient intersection
   enumeration nor creates a normalized-root direction. Therefore it does
   not turn the fixed-input existence evidence into an all-input factoring
   algorithm.

In short, V2 validly removes the quadratic public scan from the stated
signed-inverse channel. It does not close the collision-existence gap.
