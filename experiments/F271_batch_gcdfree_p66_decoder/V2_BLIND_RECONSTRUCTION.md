# F271 V2 blind reconstruction

## Verdict and sealed input

**Verdict: reconstructed.** I found no mathematical or complexity defect in
F271 V2 under its stated input contract. The two V2 changes repair the two
boundary cases they name. The canonical-residue clause bounds the supplied
root encoding. The explicit `S=0` branch removes every empty-tree operation.

This is only a verdict on the conditional decoder theorem. It is not a verdict
that the main integer-factoring statement has been proved. F271 supplies none
of the source results that would produce a complete F265 bank, a residual core
of the stated size, a nonzero square kernel, or a non-global normalized root.

This reconstruction used exactly these two F271 mathematical inputs:

1. `STATEMENT.md`, SHA-256
   `19b288038c4f9e339d3f56e51fb1c6d7277fd9e322e486f2339edd0c68bf64ba`;
2. `V2_STATEMENT.md`, SHA-256
   `29fd1a79e569c2e4da72d3489e7385de4123e6b299241bfe46defb421c84b82c`.

Both hashes matched before reconstruction. I did not read an F271 proof,
self-audit, hostile audit, earlier reconstruction, provenance file, manifest,
sanity source or output, registry entry, history, or message about the
mathematics before sealing this file.

Write

\[
 L=\operatorname{bitlen}(N),\qquad B=R+L.
\]

All asymptotic logarithms below can be read as `log(R+2)` at the empty and
one-bit boundaries.

## 1. Canonical supplied residues

For a valid V2 row,

\[
 0\leq v_i<N,qquad \gcd(v_i,N)=1.
\]

In fact `v_i` is nonzero because `N>1`. Hence

\[
 \operatorname{bitlen}(v_i)\leq \operatorname{bitlen}(N)=L.
\]

Every positive `a_i` has bit length at least one. Thus `m<=R`, and all
supplied roots together use at most

\[
 mL\leq RL\leq \frac{(R+L)^2}{4}=O(B^2)
\]

bits. Reading them is therefore covered by an `O(B^4)` decoder bound. Their
modular products, congruence checks, unit checks, and inversions also have
operands of at most `L` bits.

The clause changes representation, not the modular premise. Every residue
class has one representative in `[0,N)`, and reduction modulo `N` preserves
both the square congruence and the gcd with `N`. An arbitrarily long spelling
would, however, make a running-time bound independent of its length false.
V2 correctly excludes that spelling instead of silently ignoring its input
cost.

## 2. Saturation

Let

\[
 u=\prod_p p^{\alpha_p},\qquad v=\prod_p p^{\beta_p},
 \qquad \ell=\operatorname{bitlen}(u).
\]

If `p|v`, then `beta_p>=1`. Also

\[
 \alpha_p\leq \log_2 u<\ell,
\]

so `ell*beta_p>=alpha_p`. If `p` does not divide `v`, no power of `v`
is divisible by `p`. Consequently

\[
 \gcd(u,v^\ell)
 =\prod_{p\mid v}p^{\alpha_p}.
\]

Replacing `v^ell` by its residue modulo `u` does not change this gcd. This
proves the stated saturation identity. Modular exponentiation materializes
only residues modulo `u`; it never materializes `v^ell` and never factors an
integer.

## 3. Equal-support refinement

Suppose `x` and `y` have the same rational-prime support. Fix a prime in that
support and write its exponents in `(x,y)` as `(alpha,beta)`. At one recursion
node, `d=gcd(x,y)` has exponent `min(alpha,beta)`.

- If `alpha>beta`, the prime occurs in `A` and the first child with exponent
  pair `(alpha-beta,beta)`.
- If `beta>alpha`, it occurs in `B` and the second child with exponent pair
  `(beta-alpha,alpha)`, in that child's coordinate order.
- If `alpha=beta`, it occurs in `C` and terminates at this node.

The supports of `x/d` and `y/d` are disjoint. Therefore `A` and `B` are
coprime divisors of `d`; `C=d/(AB)` is an integer; and the three branch
supports are disjoint. Each nonempty child again has equal support.

Along each prime, the positive exponent sum strictly decreases until the two
exponents are equal. This is the subtractive Euclidean algorithm. It proves
termination. Induction over the recursion tree proves that all emitted
blocks are pairwise coprime.

For a first-child block, suppose its local exponents relative to `(x/d,A)`
are `(u,v)`. Its exponent in `x` is `u+v`, and its exponent in `y` is `v`.
This gives `(u+v,v)`. The same calculation gives `(v,u+v)` for the second
child. A `C` block occurs once in each input. Thus the displayed coordinate
maps reconstruct `x` and `y` exactly.

Equivalently, for each rational prime, the final block on its path contains
that prime to exponent `gcd(alpha,beta)`, while the local output exponents are
`alpha/gcd(alpha,beta)` and `beta/gcd(alpha,beta)`. Different primes can stay
in one block exactly while their recursion paths agree. No prime
factorization is needed to obtain that grouping.

## 4. Arbitrary overlapping inputs and `TWO_BASE`

For arbitrary overlapping `x,y`, saturation gives

\[
 x_s=\prod_{p\mid y}p^{v_p(x)},\qquad
 y_s=\prod_{p\mid x}p^{v_p(y)}.
\]

They have the same support, namely `supp(x) intersect supp(y)`, and

\[
 \gcd(x_s,y_s)=\gcd(x,y)=d.
\]

The residuals `x/x_s` and `y/y_s` use, respectively, primes private to `x`
and primes private to `y`. They are coprime to each other and to every shared
output. Combining these two residuals with the equal-support output gives a
pairwise-coprime list and the exact identities

\[
 x=\prod_jq_j^{u_j},\qquad y=\prod_jq_j^{v_j}.
\]

The supplied leaf gcd is exact, so the root equal-support call needs no new
gcd.

### Exact refinement gcd accounting

Let `T` be the number of `TWO_BASE` calls and `E` the total number of
`SAME_SUPPORT` nodes in their recursion forest.

- The two initial saturations in each `TWO_BASE` use `2T` gcds.
- Every nonroot equal-support node computes its gcd. This uses `E-T` gcds.
- A nontrivial `A` or `B` creates exactly one child. Conversely every
  nonroot node has exactly one such parent saturation. These saturations use
  another `E-T` gcds.

Thus exact two-integer refinement uses

\[
 2T+(E-T)+(E-T)=2E
\]

scalar gcd calls. This explains the `2E` term; it is not a hidden estimate.

Passing a `2 by 2` transform down each recursion edge and applying the
composed transform only at a leaf emits each block once. It avoids repeated
copying of descendant lists.

## 5. Incremental global insertion

At a loop boundary for row `i`, use this invariant:

1. the tree blocks are pairwise coprime;
2. all completed rows reconstruct exactly;
3. for the active row,

   \[
   a_i=y\prod_jq_j^{e_{ji}};
   \]

4. `y` is coprime to every block produced by an earlier touch in this row.

It holds initially with an empty tree and `y=a_i`.

If `gcd(y,P)=1`, inserting `y` preserves pairwise coprimality and finishes
the row. Otherwise, descent finds a leaf that overlaps `y`. At a node, the
left gcd is computed. If it is nontrivial, it is the exact gcd carried to
the left child. If it is one, the previously carried gcd equals the gcd with
the right child, so no right gcd is needed. One gcd per level therefore
suffices.

Let the chosen old block have exponent vector `w`. `TWO_BASE(b,y,g_b)`
returns local triples `(q,u,v)`. For `u>0`, assigning

\[
 uw+v e_i
\]

is exact: for an old row it supplies the `u` part of `b`, and for the active
row it also supplies the `v` part of `y`. Outputs with `u=0` contain only
primes of the unabsorbed part of `y`, so their powered product is the new
residual. Outputs with `u>0` have support inside the old block and are
coprime to every other old block. This proves all four invariant clauses
after the replacement.

Each touch removes from `y` every prime shared with the selected old block.
The residual can never touch a block created by that touch. Hence the loop
terminates. A row equal to one takes no loop iteration.

The number of live blocks never exceeds the number of rational primes seen
in the rows. Since that number is at most `I<=R`, the next power of two at
least `max(1,R)` supplies enough leaves even during an insertion. Fixed row
order, left-first descent, fixed recursion branch order, sorting only the
replacement blocks, and lowest-vacant-slot placement make the output
deterministic without a global rebuild.

## 6. Terminal verification, including `S=0` and `S=1`

For `S=0`, set `P=1`. The empty product reconstructs a row only when that
row is one. Pairwise coprimality is vacuous. A correct implementation builds
no modulus tree and no remainder tree, and performs:

- zero modulus squarings or product multiplications;
- zero remainder divisions;
- zero terminal exact divisions;
- zero terminal gcds.

For `S>=1`, let `P=product(q_j)`, already available as the maintained block
tree root. A compact balanced binary tree with leaf moduli `q_j^2` has `S-1`
internal nodes. One exact implementation has these counts:

| case | leaf squarings | internal modulus products | remainder divisions | terminal exact divisions | terminal gcds |
|---|---:|---:|---:|---:|---:|
| `S=0` | 0 | 0 | 0 | 0 | 0 |
| `S=1` | 1 | 0 | 0 | 1 | 1 |
| `S>=2` | `S` | `S-1` | `2S-2` | `S` | `S` |

Here a leaf square counts as one multiplication. The root modulus is

\[
 \prod_jq_j^2=P^2.
\]

Since `1<=P<P^2`, the root remainder is `P` without a division. A compact
full binary tree has `2S-2` nonroot nodes, so one reduction on every
parent-to-child edge gives exactly `2S-2` remainder divisions. At each leaf,
one exact division by `q_j` forms `t_j`. If an implementation elects to
rebuild `P` instead of reusing the maintained root, it adds `S-1`
multiplications but changes no theorem or gcd count.

For every `j`, write `P=q_jA_j`, where

\[
 A_j=\prod_{k\ne j}q_k.
\]

Then

\[
 P\bmod q_j^2=q_j(A_j\bmod q_j),
\]

so the numerator is exactly divisible by `q_j` and

\[
 \gcd\left(q_j,{P\bmod q_j^2\over q_j}\right)
 =\gcd(q_j,A_j).
\]

For `S=1`, `A_1=1`, the remainder is `q_1`, the quotient is one, and the
single gcd is one. For `S>=2`, all terminal gcds equal one if and only if
every unordered pair of blocks is coprime. Thus exactly `S` gcd calls replace
the unordered-pair scan.

## 7. Square kernel and all support-at-most-two relations

Because the blocks are pairwise coprime, a product

\[
 \prod_jq_j^{E_j}
\]

is a square exactly when `E_j` is even for every nonsquare `q_j`. A square
block imposes no parity condition. Therefore the matrix `A` whose rows are
the parity exponent vectors of nonsquare blocks has

\[
 \ker A=\{c:\prod_i a_i^{c_i}\text{ is an integer square}\}.
\]

Let `sigma_i` be column `i`. Then

\[
 Ae_i=0\iff\sigma_i=0,
\]

and, for distinct indices,

\[
 A(e_i+e_j)=0\iff\sigma_i=\sigma_j.
\]

This proves the singleton and pair criteria.

For the zero-signature class `Z`, all coordinate vectors `e_i` are
independent low-support relations. Within a nonzero equal-signature class
`C`, the pair relations form the even-weight subspace on `C`; its star at
the least index `r_C` is a basis. Classes have disjoint coordinate support.
Hence

\[
 \{e_i:i\in Z\}\cup
 \{e_{r_C}+e_i:C\ne Z,\ i\in C\setminus\{r_C\}\}
\]

is an independent basis of the complete span of singleton and support-two
relations. The exact hit counts are

\[
 |Z|,
 \qquad
 \binom{|Z|}{2}+\sum_{C\ne Z}\binom{|C|}{2}.
\]

They require signature grouping only. They require no pair gcd, division,
or square test.

Let `L` be this low basis in canonical RREF and `K` a canonical basis of the
full kernel. Reduction against the fixed pivots of `L` is a linear normal
form. The nonzero independent normal forms of the ordered vectors of `K`
span `K/L`. They are zero in every pivot coordinate of `L`, so their span
intersects `span(L)` only at zero. Canonical RREF insertion therefore gives
a deterministic complement `C` with

\[
 \ker A=\operatorname{span}(L)\oplus\operatorname{span}(C),
 \qquad \dim L+\dim C=\dim\ker A\leq m.
\]

## 8. Exact roots and complete image classification

For a kernel vector `c`, define

\[
 E_j=\sum_i c_i e_{ji}.
\]

For a nonsquare block, `E_j` is even by the kernel condition. For a square
block, write `q_j=h_j^2`. Therefore

\[
 R(c)=
 \prod_{q_j\text{ square}}h_j^{E_j}
 \prod_{q_j\text{ nonsquare}}q_j^{E_j/2}
\]

is an integer and

\[
 R(c)^2=\prod_i a_i^{c_i}.
\]

This proves that the displayed formula is the exact positive square root,
including the cases where a gcd-free block is composite or itself square.

The supplied value

\[
 X(c)=\prod_i v_i^{c_i}\pmod N
\]

is a unit and has the same square modulo `N`. Hence

\[
 \rho(c)=R(c)X(c)^{-1}\pmod N
\]

satisfies `rho(c)^2=1 mod N`.

To prove the homomorphism claim, let `c+d` mean binary addition. If both
vectors select row `i`, exact roots acquire one factor `a_i`, while modular
roots acquire `v_i^2`, which is congruent to `a_i`. These factors cancel in
the normalized quotient. Thus

\[
 \rho(c+d)=\rho(c)\rho(d).
\]

The combined low basis and complement has at most `m` vectors and spans the
full square kernel. If every basis image is in `{1,-1}`, every kernel image
is in that subgroup. Conversely, any non-global image forces at least one
basis vector to have a non-global image. This proves complete classification
without enumerating `2^dim(kernel)` relations.

For odd `N`, a non-global root of one gives a factor through the two signed
gcds with `rho-1` and `rho+1` (equivalently with `R-X` and `R+X`). Thus at
most `m` exact-root verifications, `m` inversions, and `2m` signed gcds
suffice. These signed classification gcds are separate from the refinement
and terminal-coprimality call cap in Sections 9 and 10.

## 9. The two peel rules are different

At an active row set, positive-support privacy means

\[
 e_{ji}>0,qquad e_{jk}=0\quad(k\ne i\text{ active}).
\]

If `q_j` is nonsquare and `e_ji` is odd, some rational prime has odd
valuation in `q_j^{e_ji}` and is absent from every other active row.
Conversely, any private rational prime of odd row valuation lies in one
gcd-free block for which the block is nonsquare and the row exponent is
odd. This proves the stated D05 rule. Simultaneous rounds are necessary
because deleting one layer can create privacy in the next. The exponent
table already contains all required information, so this peel needs no new
integer gcd.

Parity-degree-one peeling uses a different support: the nonzero entries of
the relevant nonsquare-block row modulo two. A parity row of degree one
forces that coordinate to be zero in every kernel vector, so deleting the
coordinate is kernel-safe. Every D05 deletion is a parity-degree-one
deletion, but the converse fails when another row has a positive even
exponent.

The example `(1,2)` for one prime is decisive. Positive support contains
both rows, so the prime is not private under D05. Parity support contains
only the first row, so parity peeling can remove that row. The two rules
must not share counters or semantics.

## 10. Global bounds and valuation telescoping

### Touches

During one row insertion, different touches remove disjoint nonempty sets
of rational primes from the residual. Therefore that row has at most
`omega(a_i)` touches, and

\[
 T\leq I.
\]

### Equal-support nodes

Fix a rational prime `p`. Let `ell(alpha,beta)` be the number of
equal-support recursion nodes on its path for an exponent pair
`(alpha,beta)`, and put `g=gcd(alpha,beta)`. The subtractive recursion gives

\[
 \ell(\alpha,\beta)\leq \alpha+\beta-g.
\]

For `alpha=beta=g`, this is `1<=g`. Otherwise induction after replacing the
larger exponent by its difference proves the inequality.

Suppose `p` first occurs with row valuation `alpha_1`. Its current block then
contains `p` to exponent `c_1=alpha_1`. At the next occurrence with valuation
`alpha_s`, refinement changes the internal block exponent from `c_{s-1}` to

\[
 c_s=\gcd(c_{s-1},\alpha_s).
\]

The number of nodes containing `p` at this touch is at most

\[
 c_{s-1}+\alpha_s-c_s.
\]

Summing over occurrences telescopes to

\[
 c_1+\sum_{s\geq2}\alpha_s-c_t
 \leq\sum_s\alpha_s.
\]

Every equal-support node contains at least one rational prime. The number of
nodes is at most the total node-prime incidence count. Summing the last bound
over primes proves

\[
 E\leq\sum_p\sum_i v_p(a_i)=V.
\]

This is the required valuation telescope. It also handles an extreme pair
such as `(p^100,p)`: its long first refinement is charged to the 100 earlier
valuation units, and subsequent blocks contain only `p`.

### Final blocks

Final blocks have disjoint nonempty rational-prime supports. Selecting one
prime from each block injects the blocks into the prime occurrences counted
by `I`. Hence

\[
 S\leq I.
\]

Also `I<=R` and `V<=R`, since each distinct prime and each prime factor with
multiplicity costs at least one bit in a positive integer.

### Gcd calls

Every touch uses one root gcd and exactly `D` descent gcds. Each row uses at
most one additional root gcd when a nontrivial residual is finally found
coprime; a row that ends at residual one, or starts at one, uses no such
call. Refinement uses exactly `2E` gcds, and terminal verification uses
exactly `S`. Thus the actual total has the form

\[
 (D+1)T+F+2E+S,qquad 0\leq F\leq m,
\]

and consequently

\[
 (D+1)T+m+2E+S
 \leq (D+1)T+m+2V+S.
\]

With `D=O(log R)` and `T,E,S,m=O(R)`, this is `O(R log R)` scalar gcd calls.
It has no hidden unordered-pair term.

## 11. Bit complexity

All live block products divide the product of the processed rows. A product
tree node therefore has `O(R)` bits. A residual and an individual block have
at most `O(R)` bits. Every exact exponent is at most a row valuation and has
`O(log R)` bits.

There are `O(R log R)` tree/root gcd calls. Binary gcd with schoolbook
operations costs `O(R^2)` bits in this operand range. There are `O(R)`
saturations, and each modular power has exponent `bitlen(u)=O(R)`, whose
binary length is `O(log R)`; repeated squaring therefore costs
`O(R^2 log R)` per saturation. There are `O(R)` recursion nodes and emitted
pieces and `O(R log R)` changed tree paths. Schoolbook exact division,
powered-residual construction, and tree multiplication all fit inside

\[
 O(R^3\log R).
\]

The bound does not rely on repeatedly copying exponent-vector lists.

For the full decoder:

- there are at most `R` blocks and rows;
- binary elimination on the at-most-`R by R` matrix is polynomial within
  `O(B^4)`;
- exact relation roots have at most `R` bits;
- at most `m^2` supplied-root multiplications use `L`-bit modular operands,
  costing `O(m^2L^2)<=O(B^4)` with schoolbook arithmetic;
- at most `m` inversions and `2m` signed gcds use `L`-bit operands;
- the complete supplied-root encoding has at most `RL=O(B^2)` bits.

Thus the conservative deterministic bound

\[
 O((R+\operatorname{bitlen}N)^4)
\]

is valid and includes the V2 representation boundary.

## 12. Exact conditional F265 cap

Assume `m<=64` and every row has bit length at most 361.

For each row,

\[
 \sum_pv_p(a_i)\leq360,
\]

because `a_i<2^361`. Therefore

\[
 V\leq64\cdot360=23,040.
\]

Independent exact integer multiplication of consecutive primes gives:

\[
\begin{array}{c|c|c}
\text{last prime} & \text{number of primes} & \text{primorial bit length}\\
\hline
271 & 58 & 368\\
16,103 & 1,875 & 23,102\\
16,111 & 1,876 & 23,116.
\end{array}
\]

The first line implies `omega(a_i)<=57`. The first inserted row touches no
old block, so the sharper touch bound is

\[
 T\leq(64-1)\cdot57=3,591.
\]

Furthermore,

\[
 \prod_i a_i<2^{64\cdot361}=2^{23,104}.
\]

Since every final block occurs positively in at least one row,
`P=product(q_j)` divides `product(a_i)`. If `S>=1,876`, pairwise
coprimality would make `P` at least the product of the first 1,876 primes,
which is at least `2^23,115`. This contradicts the preceding strict upper
bound. Hence

\[
 S\leq1,875.
\]

The 1,875-prime product has only 23,102 bits, so the adjacent primorial
certificate places the cutoff on the asserted side. A 2,048-leaf tree has
depth `D=11`. Substitution into the refinement-plus-terminal bound gives

\[
\begin{aligned}
 &(11+1)\cdot3,591+64+2\cdot23,040+1,875\\
 &=43,092+64+46,080+1,875\\
 &=91,111.
\end{aligned}
\]

Across 768 banks,

\[
 91,111\cdot768=69,973,248.
\]

Finally,

\[
 \frac{7,208,878,080}{69,973,248}
 =103.023345\ldots,
\]

so the stated factor `approximately 103.02` is correct.

The `91,111` figure is the registered worst-case upper bound for refinement
and independent terminal coprimality verification. It is not an assertion
that every bank attains all maxima simultaneously. It also does not include
the separately stated at-most-`2m` signed gcds used to classify normalized
roots. The comparison is a call-count comparison only; it does not compare
operand widths or running time.

## 13. Scope, output, and nonessential attribution

The construction uses gcd, modular powering, exact division, integer square
root, multiplication trees, remainder trees, and binary linear algebra. It
does not invoke rational-prime factorization, an order oracle, or an elliptic
source theorem.

If every block is square, every matrix column is zero. There are then exactly
`binom(m,2)` support-two hits. Serializing one record per hit necessarily
takes quadratic output size, but computing the count, span, low-image test,
or one factor certificate does not. Separate coordinate, signed-coordinate,
and chord record contracts remain outside this theorem.

The prior-art paragraph and the no-publication-novelty declaration are not
premises of any proof above. Under the sealed statement-only protocol I did
not inspect an external Bernstein source, so this reconstruction does not
act as a bibliographic audit. That limitation does not weaken the
self-contained decoder theorem.

## Final conclusion

Every mathematical dependency in the two-statement F271 V2 input
reconstructs from elementary valuation arithmetic, exact integer algebra,
and binary linear algebra. The empty terminal list, singleton terminal list,
canonical-root input length, saturation, two-base recursion, global
insertion invariant, valuation telescope, product/remainder verification,
low-support kernel basis, exact roots, normalized-root homomorphism, peel
distinction, bit bounds, and conditional F265 constants are consistent.

**No counterexample or theorem defect was found. F271 V2 survives this blind
reconstruction as a deterministic factor-free decoder theorem, and remains
explicitly insufficient by itself to solve the main integer-factoring
problem.**
