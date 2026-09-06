# F252 hostile audit

## Verdict

**PASS.** All four supplied SHA-256 digests match. The content formula,
primitive irreducibility, pairwise resultant, zero-resultant classification,
complete generic kernel, integral generic root, resultant saturation, private
parity pivots, and explicit-input bit-complexity claim all reconstruct from
the stated hypotheses.

The result is only a localization theorem. It does not prove that the
specialized numerical kernel is zero. It does not prove that a retained row
has a nonsquare private residual. It gives no probability bound and no
factoring algorithm.

## Authentication

I computed the hashes before reading the frozen mathematical content. The
task labels `SELF` and `MANIFEST` refer to `SELF_AUDIT.md` and `MANIFEST.md`.

| File | Supplied and computed SHA-256 | Result |
|---|---|---|
| `STATEMENT.md` | `cf49a2ea6ef9158f7ed60e79385b5aad5f28bd7583e9404216eadadf30457cf7` | match |
| `PROOF.md` | `acf073dc3c5c402eca8b5c9769ce14cc357d5c13ff74caa02c633ce5ac47c130` | match |
| `SELF_AUDIT.md` | `ac52eddb4ea9bd560007097dc22cadf88ecf0e7d6f9c0027c262bb10ef9e43c9` | match |
| `MANIFEST.md` | `c77c93f95f5f4264319c6e9ad852b2c4cc076f823ce57186184f3d09e273a58e` | match |

The self-audit was not used as mathematical evidence.

## Independent reconstruction

### 1. Content, primitive part, and irreducibility

For `k != 0`, the coefficient content of

\[
f(X)=Dk^2X^2-2DTkX+S^2
\]

is initially `gcd(Dk^2,2DTk,S^2)`. The Pell identity gives
`gcd(S,D)=gcd(S,T)=1`. At every prime which can divide the content, `D` and
`T` are therefore units, and

\[
v_p(\operatorname{cont}(f))
=\min\{2v_p(S),2v_p(k),v_p(2k)\}.
\]

Thus

\[
\operatorname{cont}(f)=\gcd(S^2,k^2,2k).
\]

The original discriminant is `-4Dk^2`. Division by the content divides the
discriminant by its square, so the primitive quadratic has negative
discriminant

\[
-4Dk^2/\operatorname{cont}(f)^2.
\]

It is irreducible over `Q`. No squarefree condition on `D` is needed. When
`k=0`, the polynomial is the separately removed constant square `S^2`.

### 2. Full resultant and duplicate criterion

For

\[
f=1+D(T-kX)^2,\qquad g=1+E(U-\ell X)^2,
\quad \Delta=T\ell-Uk,
\]

evaluation of `g` at the two roots
`T/k +/- i/(k sqrt(D))` of `f` gives

\[
\operatorname{Res}_X(f,g)
=(Dk^2+DE\Delta^2-E\ell^2)^2
+4DE^2\Delta^2\ell^2.
\]

Writing `A=Dk^2`, `B=E ell^2`, and `C=DE Delta^2`, the identity

\[
(A+C-B)^2+4BC=(A+B+C)^2-4AB
\]

gives exactly

\[
\operatorname{Res}_X(f,g)
=\bigl(DE\Delta^2+E\ell^2+Dk^2\bigr)^2
-4DEk^2\ell^2.
\]

For `D=E`, difference of squares gives the two displayed factors in the
statement. For positive `D,E`, vanishing requires

\[
A+B+C=2\sqrt{AB}.
\]

The arithmetic-geometric mean inequality and `C >= 0` make this equivalent
to `A=B` and `C=0`, hence

\[
Dk^2=E\ell^2,\qquad \Delta=0.
\]

These conditions give a common center and a common positive quadratic
coefficient, so they give literal equality of the two integer polynomials.
The converse is immediate. Thus association over `Q`, zero resultant, and
exact polynomial equality coincide. If `D,E` are squarefree and `k,ell` are
positive, the conditions reduce further to `D=E`, `k=ell`, and `T=U`.

### 3. Complete generic kernel and normalized root

After division by content, every post-wrap row has one irreducible quadratic
factor. Two such factors are associates exactly when the original
polynomials are equal. Unique factorization in `Q[X]` therefore says that a
binary product is a rational-function square exactly when every exact
polynomial-equality class is selected an even number of times. Constant rows
impose no condition because they are already integer squares.

There is no omitted rational scalar condition. Once every class count is
even, the product is visibly a square of the original integer polynomials,
including their contents. Conversely, an odd class count leaves an odd
valuation at its distinct irreducible quadratic.

For a generic-kernel vector `c`, let `r_C` be the even selected count in
class `C`. Then

\[
H_c(X)=
\prod_{i\in I_0,\ c_i=1}S_i
\prod_C f_C(X)^{r_C/2}
\]

is in `Z[X]` and squares to the selected product. Exact duplicates have the
same value at zero and all `S_i` are positive, so

\[
H_c(0)=\prod_i S_i^{c_i}.
\]

At `X=N`, the positive numerical root is `|H_c(N)|`. Since an integer
polynomial has `H_c(N) = H_c(0) (mod N)`, this root is congruent to one
global sign times the supplied-root product. On the unit branch, one of the
two standard gcds is therefore `N` and the other is `1`, because `N` is odd.
There is no coefficient-denominator exception. After constant rows and all
but one member of each equality class are deleted, the generic kernel is
zero.

### 4. Factor-free resultant saturation

After duplicate removal, all pairwise resultants are nonzero. If a prime `p`
divides both `f_i(N)` and `f_j(N)`, then `N mod p` is a common root of their
reductions. The Sylvester matrix is singular modulo `p`, so `p` divides the
integer resultant. This remains true when a leading coefficient vanishes
modulo `p`; no converse is used.

Let

\[
\mathcal R_i=\prod_{j\ne i}|\operatorname{Res}(f_i,f_j)|,
\quad e_i=\lceil\log_2(a_i+1)\rceil,
\quad g_i=\gcd(a_i,\mathcal R_i^{e_i}),
\quad b_i=a_i/g_i.
\]

For every prime `p` shared by `a_i` and another row, `p` divides
`mathcal R_i`, while

\[
v_p(a_i)\le \log_2 a_i<e_i.
\]

Consequently `mathcal R_i^{e_i}` contains more than enough copies of `p` for
the gcd to remove the full `p`-primary part of `a_i`. Hence

\[
\gcd(b_i,a_j)=1\quad(i\ne j).
\]

This is full saturation, not only squarefree support removal.

### 5. Private pivots and the remaining core

If `b_i` is nonsquare, it has a prime of odd valuation. That prime occurs in
no other full row, so its parity equation forces `c_i=0` in every numerical
square dependency. This is an exact private pivot.

If `b_i` is square, deleting it does not change the parity column of `a_i`.
Every prime remaining in `g_i` divides `mathcal R_i`. Thus, after forced rows
are removed, the complete remaining parity problem is supported on explicit
pairwise resultants. The support can still contain zero columns and
nontrivial dependencies. A specialization-only singleton square still needs
its supplied-root gcd screen; parity localization does not certify its root
as global.

All of this uses gcds, exponentiation, exact division, and integer square
tests. It does not require the prime factorization of a value or a
resultant.

### 6. Bit complexity

Let `L` be the total bit length of the explicit input list. Then `m <= L`.
Each coefficient, specialization, and pairwise resultant has bit length
polynomial in `L`. There are `O(m^2)` resultants, and the bit length of each
product `mathcal R_i` is the sum of the bit lengths of its factors. Also
`e_i=O(L)`, so the materialized power `mathcal R_i^{e_i}` still has
polynomial bit length. Standard integer arithmetic, Euclid's algorithm,
integer square testing, and binary linear algebra are polynomial in these
explicit sizes.

Thus the factor-free cleanup and saturation are deterministic polynomial
work in `L`. A materialized bank with quasipolynomial row count and
quasipolynomial coordinate lengths remains quasipolynomial. No conclusion is
made for a larger bank supplied only by an implicit rule.

### 7. P68 comparison and exact scope

The authoritative P68 result certifies the unit-denominator part of a generic
constant-term-one square kernel as global-root decoys. It neither generally
makes that generic kernel zero nor localizes specialization-only relations.
F252 does not use P68 as a proof premise. The Pell square constant terms and
the exact duplicate classification instead construct an integral root for
every generic vector directly. The family-specific gains are therefore
exactly the three claimed ones: zero cleaned generic kernel, no denominator
exception for generic roots, and localization of the full numerical parity
problem to private pivots plus pairwise-resultant support.

The packet does not promote the localized core to a source-success theorem.
It leaves open singleton specialization squares, numerical collisions,
multirow resultant-supported dependencies, and non-global roots arising from
such dependencies. Its P68 comparison and its exclusions are therefore
properly scoped.

## Final assessment

I found no counterexample, missing parity condition, hidden factorization
step, or asymptotic expansion beyond the explicit-input model. The frozen
statement and proof support the claimed conclusions.
