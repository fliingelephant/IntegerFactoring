# F271 statement — batch gcd-free P66 decoder

## Status and scope

F271 is a deterministic proof-only decoder theorem. It replaces the
quadratic block-pair scans and support-two arithmetic in the proposed F265
terminal decoder. It uses no rational-prime factorization.

F271 proves no elliptic source theorem. It does not prove that an F265 bank
is complete, that its residual core has at most 64 rows, that its square
kernel is nonzero, or that a non-global normalized root exists. A future
F265 version must specify and audit its own source, evidence, resource, and
byte contracts.

## 1. Input

Let

\[
 a_1,\ldots,a_m\in\mathbb Z_{>0}
\]

and let every row have a supplied residue `v_i` such that

\[
 v_i^2\equiv a_i\pmod N,
 \qquad \gcd(v_i,N)=1,
\]

where `N>=3` is odd. Put

\[
 R=\sum_i\operatorname{bitlen}(a_i),
 \qquad
 r=\max_i\operatorname{bitlen}(a_i),
\]

\[
 V=\sum_{p}\sum_i v_p(a_i),
 \qquad
 I=\sum_i\omega(a_i),
\]

where `omega` counts distinct rational-prime divisors. The algorithm never
computes `V`, `I`, or a rational-prime valuation. They are proof measures.

An integer input equal to one is legal. Integer zero is not legal. A zero or
nonunit supplied residue does not enter the decoder.

## 2. Saturation primitive

For `u>1` and `v>1`, define

\[
 \operatorname{Sat}(u;v)
 =\gcd\left(u,v^{\operatorname{bitlen}(u)}\bmod u\right).
\]

It is the complete product of the primary parts of `u` whose rational primes
divide `v`:

\[
 \operatorname{Sat}(u;v)
 =\prod_{p\mid v}p^{v_p(u)}.
\]

The power is computed modulo `u`. It is not materialized.

## 3. Exact two-integer refinement

### 3.1 Equal-support recursion

Suppose `x,y>1` have the same set of rational-prime divisors, and suppose
`d=gcd(x,y)` is supplied or computed. Set

\[
 x_0=x/d,
 \qquad y_0=y/d,
\]

\[
 A=\operatorname{Sat}(d;x_0),
 \qquad B=\operatorname{Sat}(d;y_0),
 \qquad C=d/(AB),
\]

where `A=1` when `x_0=1` and `B=1` when `y_0=1`.

Recursively refine `(x_0,A)` when `A>1`, and refine `(y_0,B)` when
`B>1`. Retain `C` when `C>1`. The two recursive pairs again have equal
prime support.

If one returned block has local exponents `(u,v)` relative to `(x_0,A)`,
map them to

\[
 (u+v,v)
\]

relative to `(x,y)`. For the second recursion, map `(u,v)` to

\[
 (v,u+v).
\]

The block `C` has local exponents `(1,1)`.

### 3.2 Arbitrary overlapping pair

For arbitrary `x,y>1` with a supplied nontrivial overlap `d=gcd(x,y)>1`, first
compute

\[
 x_s=\operatorname{Sat}(x;y),
 \qquad y_s=\operatorname{Sat}(y;x).
\]

Then `x_s` and `y_s` have equal prime support and

\[
 \gcd(x_s,y_s)=d.
\]

Apply the equal-support recursion with this supplied root gcd. Retain
`x/x_s` with local exponents `(1,0)` and `y/y_s` with local exponents
`(0,1)` when they exceed one.

The result is a pairwise-coprime list `(q_j,u_j,v_j)` satisfying

\[
 x=\prod_jq_j^{u_j},
 \qquad y=\prod_jq_j^{v_j}.
\]

### 3.3 Pseudocode

```text
SAME_SUPPORT(x, y, supplied_d):
    d = supplied_d if present else gcd(x, y)
    x0 = x / d
    y0 = y / d
    A = 1 if x0 = 1 else Sat(d; x0)
    B = 1 if y0 = 1 else Sat(d; y0)
    C = d / (A * B)

    out = []
    if A > 1:
        for (q,u,v) in SAME_SUPPORT(x0, A, absent):
            append (q,u+v,v)
    if B > 1:
        for (q,u,v) in SAME_SUPPORT(y0, B, absent):
            append (q,v,u+v)
    if C > 1:
        append (C,1,1)
    return out

TWO_BASE(x, y, supplied_d):
    xs = Sat(x; y)
    ys = Sat(y; x)
    out = SAME_SUPPORT(xs, ys, supplied_d)
    if x/xs > 1: append (x/xs,1,0)
    if y/ys > 1: append (y/ys,0,1)
    return out
```

## 4. Incremental global decoder

Maintain a pairwise-coprime block list. Every block stores its exact exponent
vector over the processed rows. Store the block products in a fixed balanced
product tree whose empty leaves have value one. A factor-free universal
choice is the next power of two at least `max(1,R)` leaves. A sharper proved
cap can replace it.

To insert row `a_i`, set `y=a_i` and give it the unit exponent vector at row
`i`. While `y>1`:

1. compute `g=gcd(y,P)`, where `P` is the root product of all current blocks;
2. if `g=1`, insert `y` and finish the row;
3. otherwise descend the product tree to the first leaf `b` that overlaps
   `y`, carrying the exact gcd at every chosen node;
4. call `TWO_BASE(b,y,g_b)`, where `g_b=gcd(b,y)` is the carried leaf gcd;
5. replace `b` by every output with positive local `b` exponent; and
6. multiply every output with zero local `b` exponent, to its local `y`
   exponent, into the new residual `y`.

Sort the replacement blocks by integer value. Put the least one in `b`'s
old slot and put the rest in the lowest vacant slots. Put a final coprime
residual in the lowest vacant slot. This fixes the dynamic-tree layout
without rebuilding or re-sorting the full tree.

For an output with local exponents `(u,v)`, if the old block exponent vector
is `w`, its new global exponent vector is

\[
 uw+v e_i.
\]

Use fixed row order, left-first tree descent, fixed branch order, and final
integer-value sorting. These rules make the result deterministic.

The displayed returned-list coordinate maps are mathematical notation. An
implementation carries their `2 by 2` integer transforms down the recursion
and emits each terminal block once. It does not repeatedly copy every
descendant list.

The final blocks `q_1,...,q_S` are pairwise coprime and

\[
 a_i=\prod_{j=1}^S q_j^{e_{ji}}
\]

for every input row.

### 4.1 Global pseudocode

```text
INSERT_ROW(i):
    y = a[i]
    while y > 1:
        g = gcd(y, PRODUCT_TREE.root)
        if g = 1:
            put (y, exponent_vector=e_i) in the lowest vacant leaf
            update its root path
            return

        node = root; h = g
        while node is not a leaf:
            h_left = gcd(y, node.left.product)
            if h_left > 1: node = node.left; h = h_left
            else:          node = node.right

        b = node.value; w = node.exponent_vector
        pieces = TWO_BASE(b, y, h)
        old = sort by q every (q,u,v) with u > 0
        y = product of q^v over every (q,0,v)

        assign (q, u*w + v*e_i) for old to the old slot and then
            the lowest vacant slots
        update exactly the changed root paths
```

At the start and end of every loop, the tree blocks are pairwise coprime,
they reconstruct all completed rows, and the current residual contains
exactly the still-unabsorbed part of row `i`. It is coprime to every block
created by an earlier touch in this row. This is the global invariant.

## 5. Independent terminal verification

Verify every row reconstruction. Put

\[
 P=\prod_jq_j,
 \qquad
 t_j={P\bmod q_j^2\over q_j}.
\]

The numerator is exactly divisible by `q_j`, and

\[
 \gcd(q_j,t_j)
 =\gcd\left(q_j,\prod_{k\ne j}q_k\right).
\]

One product/remainder tree and exactly `S` gcd calls therefore verify all
pairwise-coprimality claims. There is no final unordered-pair scan.

## 6. Exact square matrix and low-support closure

Integer-square-test each block. For each nonsquare block form the binary row

\[
 (e_{j1},\ldots,e_{jm})\bmod2.
\]

Let `sigma_i` be matrix column `i`. Then

\[
 e_i\text{ is a square relation}\iff\sigma_i=0,
\]

and, for distinct `i,j`,

\[
 e_i+e_j\text{ is a square relation}
 \iff\sigma_i=\sigma_j.
\]

Let `Z` be the zero-signature class. For every nonzero signature class `C`,
let `r_C` be its least row. A basis of the complete support-at-most-two span
is

\[
 \{e_i:i\in Z\}
 \cup
 \{e_{r_C}+e_i:C\ne Z,\ i\in C\setminus\{r_C\}\}.
\]

The exact singleton and support-two hit counts are

\[
 |Z|
\]

and

\[
 \binom{|Z|}{2}
 +\sum_{C\ne Z}\binom{|C|}{2}.
\]

No row-pair gcd, exact division, or square test is needed for these counts or
for this span.

Compute a canonical full-kernel basis by binary elimination. Reduce it
against the low basis to obtain a canonical structural complement. Their
dimensions sum to the kernel dimension and are at most `m`.

### 6.1 Closure and complement pseudocode

```text
A = rows (e[j,1],...,e[j,m]) mod 2 for nonsquare q[j]
sigma[i] = column i of A

L = every e_i with sigma[i]=0
for each nonzero equal-signature class C in lexicographic order:
    r = least index in C
    append e_r + e_i for i in C minus {r}, in increasing order
L = canonical_RREF(L)

K = canonical_nullspace_basis(A), with columns ordered 1,...,m
C = empty canonical RREF
for k in K in canonical order:
    z = normal_form(k modulo L)
    if z is nonzero and independent of C: insert z into C

classify every vector in the bases L and C by the root procedure below
```

The normal form subtracts pivot rows of `L` in pivot order. Thus every
retained `z` is still in the square kernel, `span(L)` intersects `span(C)`
only at zero, and their sum is the full kernel.

## 7. Exact roots and factor classification

For a kernel vector `c`, put

\[
 E_j=\sum_i c_i e_{ji}.
\]

If `q_j` is square, let `h_j=sqrt(q_j)`. The exact positive root is

\[
 R(c)=
 \prod_{q_j\text{ square}}h_j^{E_j}
 \prod_{q_j\text{ nonsquare}}q_j^{E_j/2}.
\]

The supplied modular root is

\[
 X(c)=\prod_iv_i^{c_i}\pmod N.
\]

The normalized-root map

\[
 \rho(c)=R(c)X(c)^{-1}\pmod N
\]

is a homomorphism from the square kernel to the roots of one modulo `N`.
Thus basis classification is complete. The low basis plus its structural
complement requires at most `m` root verifications, `m` inversions, and `2m`
signed gcds. No exponential relation enumeration is needed.

## 8. D05 and P106 peel boundaries

F271 does not identify the D05 saturated private-primary peel with the P106
parity-degree-one peel.

To reproduce D05 exactly after refinement, use positive exponent support. At
an active row set `S`, block `q_j` is private to row `i` exactly when

\[
 e_{ji}>0,
 \qquad
 e_{jk}=0\quad(k\in S\setminus\{i\}).
\]

Delete row `i` in that simultaneous round exactly when at least one such
`q_j` is nonsquare and `e_ji` is odd. Repeat by simultaneous rounds. This
uses no new integer gcd.

P106 parity-degree-one peeling instead uses the support of
`e_ji mod 2`. It is kernel-safe and can delete more rows. For example, one
prime with row valuations `(1,2)` is parity-private to the first row but is
not absent from the second row. A future experiment must choose one rule and
must not mix their counters or semantics.

## 9. General bounds

Let `T` be the number of old blocks touched during all insertions, let `E` be
the total number of equal-support recursion nodes, let `S` be the final block
count, and let

\[
 D=\lceil\log_2 S_{\max}\rceil
\]

be the fixed product-tree depth. Then

\[
 T\le I,
 \qquad E\le V,
 \qquad S\le I.
\]

The complete refinement plus independent coprimality-verification call bound
is

\[
 \boxed{(D+1)T+m+2E+S}
 \le
 \boxed{(D+1)T+m+2V+S}.
\]

This is `O(R log R)` scalar gcd calls and is subquadratic in the encoded
integer input size. It contains no hidden pairwise block work.

With schoolbook integer arithmetic and a dynamic product tree, the complete
gcd-free refinement has deterministic

\[
 O(R^3\log R)
\]

bit complexity. Including binary elimination, exact relation roots, modular
root products, inversions, and signed gcds gives a conservative

\[
 O((R+\operatorname{bitlen}N)^4)
\]

bit bound. Faster multiplication and remainder trees improve these bounds.

## 10. Exact F265 residual bounds

For `m<=64` and `r<=361`,

\[
 V\le64\cdot360=23{,}040.
\]

The product of the first 58 primes has 368 bits, so every 361-bit row has at
most 57 distinct rational-prime divisors. Hence

\[
 T\le63\cdot57=3{,}591.
\]

The exact finite primorial certificate in `sanity_check.cpp` gives

\[
 \operatorname{bitlen}(p_1\cdots p_{1875})=23{,}102,
\]

\[
 \operatorname{bitlen}(p_1\cdots p_{1876})=23{,}116.
\]

Since the product of 64 input rows is less than `2^23104`, the final basis
has

\[
 S\le1{,}875.
\]

A fixed 2,048-leaf tree therefore suffices and has `D=11`. The complete
registered maximum is

\[
\begin{aligned}
 &(11+1)\cdot3{,}591+64+2\cdot23{,}040+1{,}875\\
 &\qquad=\boxed{91{,}111\text{ gcd calls per bank}}.
\end{aligned}
\]

Across 768 maximum decoders this is

\[
 \boxed{69{,}973{,}248\text{ gcd calls}}.
\]

The D08 draft registered 7,208,878,080 fixed P66 gcd calls. F271 lowers that
cap by a factor of approximately 103.02. The comparison is a call-count
comparison, not a runtime projection: F271 has some wide-versus-narrow tree
gcds and must time its complete routine.

## 11. Prior art and novelty boundary

Gcd-free and coprime bases are established algorithms. Bernstein gives an
essentially linear algorithm for the natural coprime base and its exponent
factorizations. F271 does not claim a faster coprime-base theorem.

F271's project-level contribution is the auditable F265 specialization:

1. an explicit incremental refinement with exact call and operand bounds;
2. product-tree terminal verification instead of `binom(S,2)` gcds;
3. signature grouping instead of support-two arithmetic;
4. complete low-image and complement classification in at most `m` roots;
   and
5. an exact distinction between D05 positive-support peeling and P106 parity
   peeling.

No publication-level novelty is claimed.

## 12. Unavoidable output boundary

Decoder arithmetic has no unavoidable quadratic pair step. If an experiment
requires one serialized record for every support-two hit, then an all-square
bank has `binom(m,2)` such records. That output cost is unavoidable under
that record contract. Exact counts, span, existence of a useful low image,
and a factor certificate do not require those records.

F265's separate coordinate, signed-coordinate, and chord controls are also
outside F271. Their pair enumeration is not silently removed by this theorem.
