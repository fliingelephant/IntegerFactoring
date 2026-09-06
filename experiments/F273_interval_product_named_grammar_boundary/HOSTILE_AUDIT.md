# F273 fresh hostile audit — PASS

## Frozen authentication

I authenticated the packet before inspecting its claims. The SHA-256 of
`FROZEN.sha256` is

```text
bbfce77ead51db2d540d665ed620840894a317f1c96102c62a5ef8315e6df88c
```

Every entry in that freeze list matches:

| File | SHA-256 |
|---|---|
| `STATEMENT.md` | `cdc099e0a74b5d2510ac4d9b88cf965f0ef797e6bcc428ac855c3f74daec5079` |
| `PROOF.md` | `09978512f2e66768628df481380e059e3d6c90fc0010e5007db249322b723dc2` |
| `SELF_AUDIT.md` | `66218b417fa92037526d4d7b9b40a06638fd7ae7f578d5ec3176d886039a49dd` |
| `PROVENANCE.md` | `4595033097f3b66b3b1a12e4fce1dc339bf58fbc8f1e31bcbd40cf21c34a784c` |
| `MANIFEST.md` | `2b33fdd0d8921bccf613ef360e92dd7a604b06133de09bf8c91d944678e41786` |

I did not modify a frozen file or a durable ledger.

## Verdict

**PASS under the literal hypotheses and exclusions in `STATEMENT.md`.** I
found no false theorem, missing case, invalid cancellation, or scope upgrade.
The child-zero result is only a coordinate-ring statement; the Smith result
is only for one local rank defect; and the state lower bound is only for the
displayed literal recursion. None is a general arithmetic-circuit lower
bound.

Two interpretation boundaries must remain attached to this verdict:

1. In the rational extension, “nonzero on a generic axis” means that the
   specialized denominator is a nonzero polynomial, so the specialization
   exists in the corresponding rational function field. It does not mean
   that the denominator is pointwise nonzero everywhere on the axis.
2. The `Theta((M/q_0)n)` storage statement assumes one explicit fixed-width
   residue word for every keyed offset. The unconditional conclusion inside
   the literal grammar is the `Theta(M/q_0)` distinct-offset closure and its
   corresponding explicit state-processing count. The packet states both
   restrictions, so neither is a defect.

## 1. Child-zero ideal and rational denominator — pass

Evaluation at `e_0=0` deletes exactly the positive-`e_0` terms and retains
the coefficient of `e_0^0`. Its kernel is therefore `(e_0)`. Applying the
same coefficient argument in both variables leaves only monomials with
positive `e_0`- and `o_0`-degree, hence the intersection is `(e_0o_0)`.
No Bezout or coprimality step is hidden here.

The proof in fact works over every integral domain; characteristic zero is
not needed. Thus the packet's characteristic-zero consequence is safe, not
an unsupported strengthening.

For `G/H`, let `H(0,o_0,z)` be nonzero in `A[o_0,z]`. If the specialized
rational function is zero, domain cancellation gives
`G(0,o_0,z)=0`; the polynomial kernel argument then gives `e_0 | G`.
The other axis gives `o_0 | G`. This does not apply if either denominator
specialization is the zero polynomial. It also proves numerator
divisibility for the displayed admissible representation, not a claim that
every representation is axis-total. These are exactly the packet's stated
limits.

For Corollary 1.1, the union of the leaf sets of the `K` summaries has size
at most `Kq_0`. If one formal leaf is absent, every expression in those
summaries is independent of it, while the target product has degree one in
it. Therefore all `M` leaves occur and `Kq_0 >= M`. This argument does not
survive the affine specialization `y_j=x+j`; the packet expressly excludes
that specialization from the conclusion.

## 2. One local Smith rank defect — pass

For each `k<m`, rank `m-1` modulo `p` supplies a `k`-minor not divisible by
`p`, and full rank modulo `q` supplies a possibly different `k`-minor not
divisible by `q`. Hence neither prime divides the gcd of all `k`-minors. At
`k=m`, the sole minor is the determinant: it is divisible by `p` and not by
`q`. Since `N=pq` with distinct primes, the displayed gcds follow exactly.

Because `Delta_k` is the product of the first `k` Smith invariant factors,
absence of `p` from every `Delta_k` for `k<m` and presence in `Delta_m`
puts its first support in the last invariant factor. No valuation-one claim
is needed.

For the diagonal example, `p <= B < q` and `B < 2p`. Thus `1,...,B`
contains exactly one multiple of `p` and no multiple of `q`, including the
edge case `B=p`. The two ranks are `B-1` and `B`, and the last
determinantal divisor is the determinant `B!`. The argument says nothing
about larger nullity or another succinct matrix, as required.

## 3. Rising-factorial discriminant and gcd gate — pass

The roots are `-1,...,-m`. Taking the absolute derivative resultant gives
the squared product of their pairwise differences. Difference `d` occurs
`m-d` times, which proves

```text
D_m = product_{d=1}^{m-1} d^(2(m-d))
    = (product_{k=1}^{m-1} k!)^2.
```

The adjacent quotient is consequently `(m!)^2`. The upper size bound uses
all terms, and the lower bound uses `Theta(m)` differences of size
`Theta(m)`, each with weight `Theta(m)`. This gives
`bitlen(D_m)=Theta(m^2 log(m+1))`, including the small cases after changing
constants.

On the balanced branch, `p <= B < q`. If `gcd(B,N)` is not one, it is a
proper factor. Otherwise `B` is not `p`, so `p <= B-1 < q`. The base `p`
then occurs with positive exponent in `D_B`, while no base can be divisible
by `q`. Therefore `gcd(D_B,N)=p`. Cases with `B=p`, including the smallest
balanced examples, exit through the preliminary gcd. The formula identifies
a factor-bearing scalar but supplies no fast evaluator.

## 4. Cross-resultants, closure, and telescope — pass

Splitting each length-`2m` block into two length-`m` blocks gives normalized
separations `2c`, `2c+1`, `2c-1`, and `2c`. Resultant multiplicativity
therefore gives

```text
R_c(2m) = R_(2c-1)(m) R_(2c)(m)^2 R_(2c+1)(m).
```

All defining factors are positive because the smallest is `(c-1)m+1`.
There is no sign or zero-factor exception.

Starting from offset one, one expansion produces `{1,2,3}`. If a level
contains every offset through `2^(s+1)-1`, the overlapping child triples
contain every offset through `2^(s+2)-1`. Thus after `t` levels the keyed
base states are exactly the `2^(t+1)-1` offsets in the statement. Positive
multiplicities prevent cancellation. Numeric residues can collide, but that
does not merge the syntactic states of the stipulated literal recursion.

For fixed `i`, the inner product is the quotient of the two stated
factorials. Multiplying over `i` gives the two adjacent factorial ranges,
and prefixing them with `S(k)=1!2!...(k-1)!` yields

```text
R_c(m) = S((c+1)m) S((c-1)m) / S(cm)^2.
```

The `c=1` endpoint is valid because the extra `0!` is one and `S(0)=1`.
Also `S(m+1)/S(m)=m!` and `D_m=S(m)^2`. The quotient is an integer identity
derived before reduction; it gives no modular inverse when `S(cm)` is a
zero divisor.

On the unresolved balanced branch, `S(B)` contains `p!`, while every
factorial in it ends below `q`. Hence its gcd with `pq` is exactly `p`.
The telescope therefore reaches the weighted product instead of evaluating
it cheaply.

Finally, the top cross term in the recursion for `D_M` is `R_1(M/2)`.
Expanding it from `M/2` to `q_0` produces `M/q_0-1` base offsets. If
`M=2^Theta(n)` and `q_0` is bounded by a fixed quasipolynomial, then
`log q_0=o(n)` and `M/q_0=2^Theta(n)`. This proves the literal state count.

## 5. Exclusions and claimed boundary — pass

The proof never infers that an arithmetic circuit must materialize the
factors whose product divides a polynomial. It never treats algebraically
independent child coordinates as actual affine jets. It never infers a
succinct-matrix lower bound from the diagonal Smith example. It never turns
the exact superfactorial quotient into modular division. It also explicitly
leaves a third cross-resultant identity or an implicit state representation
open.

The imported carry results are provenance only and are not premises of any
F273 theorem. Consequently, their mathematical content need not be trusted
to validate Theorems 1 through 4. The packet proves a named-grammar boundary
only. It does not prove a general circuit lower bound, a uniform
interval-product lower bound, a quasipolynomial evaluator, or an integer
factoring algorithm.
