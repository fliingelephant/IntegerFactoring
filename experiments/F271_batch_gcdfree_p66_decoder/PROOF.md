# F271 proof — batch gcd-free P66 decoder

## 1. Saturation is exact

Let `u,v>1`, put `L=bitlen(u)`, and fix a rational prime `p`. Reduction
modulo `u` does not change a gcd with `u`, so

\[
 v_p(\operatorname{Sat}(u;v))
 =\min(v_p(u),L v_p(v)).
\]

If `p` does not divide `v`, this is zero. If `p` divides `v`, then

\[
 v_p(u)\le\lfloor\log_2u\rfloor<L\le Lv_p(v),
\]

so the valuation is exactly `v_p(u)`. This proves

\[
 \operatorname{Sat}(u;v)
 =\prod_{p\mid v}p^{v_p(u)}.
\]

In particular, `u/Sat(u;v)` is coprime to `v`.

## 2. Equal-support recursion

Suppose `x,y` have equal prime support. For one prime in that support, write

\[
 r=v_p(x),\qquad s=v_p(y).
\]

Let `d=gcd(x,y)`, `x_0=x/d`, and `y_0=y/d`. Their valuations are

\[
 v_p(d)=\min(r,s),
\]

\[
 v_p(x_0)=\max(r-s,0),
 \qquad
 v_p(y_0)=\max(s-r,0).
\]

Also `gcd(x_0,y_0)=1`. Therefore no prime can enter both saturation branches.
The saturation lemma gives three exact cases.

- If `r>s`, the complete `p`-part of `d` enters `A`, and the recursion sees
  exponent pair `(r-s,s)`.
- If `s>r`, it enters `B`, and the recursion sees `(s-r,r)` before the
  displayed coordinate swap.
- If `r=s`, it enters `C` and terminates with local coordinates `(1,1)`.

Because the original supports agree, `x_0>1` implies `A>1`, and their prime
supports agree. The same statement holds for `y_0,B`. Thus every recursive
call satisfies the equal-support premise. The supports of the first branch,
second branch, and `C` are pairwise disjoint.

For a first-branch block with exponents `(u,v)` relative to `(x_0,A)`, its
exponent in `x=d x_0` is `u+v`, and its exponent in `y=d y_0` is `v`.
This proves the map `(u,v)->(u+v,v)`. The second map follows symmetrically.
The retained `C` divides `d` once in both inputs.

Induction on `r+s`, simultaneously for every prime in a recursion node,
proves that the returned blocks are pairwise coprime and reconstruct both
inputs exactly.

## 3. Arbitrary overlapping pair

Let `x,y>1` and `d=gcd(x,y)>1`. By saturation,

\[
 x_s=\operatorname{Sat}(x;y)
\]

contains the complete primary part of `x` at exactly the primes shared with
`y`. The symmetric statement holds for `y_s`. Hence

\[
 \operatorname{rad}(x_s)=\operatorname{rad}(y_s),
 \qquad
 \gcd(x_s,y_s)=\gcd(x,y)=d.
\]

Furthermore,

\[
 \gcd(x/x_s,y)=1,
 \qquad
 \gcd(y/y_s,x)=1.
\]

The exclusive quotients are therefore coprime to the equal-support output
and to each other. Section 2 proves that `TWO_BASE` is exact.

This covers the degenerate arithmetic cases without exceptions.

- If `x=y`, both exclusive quotients are one, and the recursion returns the
  shared blocks with equal exponent coordinates.
- If `x` divides `y`, the recursion still separates any unequal primary
  multiplicities.
- A composite block and a prime power use the same valuation proof.
- No returned unit is stored.

## 4. Incremental invariant

Assume the maintained old blocks are pairwise coprime and reconstruct every
processed row. Let a new residual `y` overlap an old leaf `b`.

`TWO_BASE(b,y)` returns pairwise-coprime blocks. Every output with positive
local `b` exponent has prime support inside `b`. It is therefore coprime to
every untouched old block. Every output with zero local `b` exponent is
coprime to the replacement outputs. Multiplying those `y`-only outputs to
their local exponents reconstructs the remaining part of `y`.

If the old block exponent vector is `w`, the identity

\[
 b=\prod_jq_j^{u_j},
 \qquad
 y=\prod_jq_j^{v_j}
\]

shows that the new exponent vector of `q_j` is

\[
 u_jw+v_je_i.
\]

Thus all old reconstructions and the new-row reconstruction remain exact.
All shared primary parts of `y` supported on `b` enter replacement blocks.
The new residual is coprime to them, so the same old leaf is not touched
again during this row insertion.

If the root gcd is one, the residual is coprime to every old block and can be
inserted. Induction over tree-leaf touches and then over rows proves the
global invariant and termination once the local recursion terminates.

## 5. Recursion-node bound

For positive exponents `r,s`, let `F(r,s)` be the number of equal-support
recursion nodes followed by one rational prime, including its equality node.
The gcd of the two exponents is invariant under a subtractive update. Put
`g=gcd(r,s)` and use the measure

\[
 \mu(r,s)=r+s-2g.
\]

At an unequal pair, one exponent is replaced by its positive difference from
the other. The sum decreases by at least `g`, and hence by at least one.
At equality the measure is zero. Therefore

\[
 F(r,s)\le r+s-2g+1.
\]

Now follow one rational prime through successive input rows in which it
occurs. Let `e_1,...,e_k` be its positive row valuations, and let

\[
 g_t=\gcd(e_1,\ldots,e_t).
\]

For the direct recursion, after processing row `t`, the integer exponent of
that prime inside its unique opaque block is exactly `g_t`. This follows by
induction from the subtractive-Euclid recursion and the equality terminal.
For `t>=2`,

\[
\begin{aligned}
 F(g_{t-1},e_t)
 &\le g_{t-1}+e_t-2g_t+1\\
 &= (g_{t-1}-g_t)+(e_t-g_t)+1\\
 &\le(g_{t-1}-g_t)+e_t.
\end{aligned}
\]

Summing telescopes:

\[
 \sum_{t=2}^kF(g_{t-1},e_t)
 \le e_1-g_k+\sum_{t=2}^ke_t
 <\sum_{t=1}^ke_t.
\]

At one recursion depth, different nodes have disjoint rational-prime
supports. Charge every recursion node to one prime that follows it. Summing
the last inequality over all primes proves

\[
 E\le V.
\]

## 6. Touched-leaf and block bounds

During insertion of row `a_i`, one touched old leaf consumes at least one
distinct prime divisor of that row. Since the residual loses the complete
primary part on every prime supported by that leaf, it cannot charge the same
prime to a later leaf. Hence

\[
 T\le\sum_{i=2}^m\omega(a_i)\le I.
\]

Final blocks are pairwise coprime and exceed one. Choose one rational prime
from each. The chosen primes are distinct and occur in the input product.
Therefore

\[
 S\le\omega\left(\prod_i a_i\right)\le I.
\]

The product of all final block values divides the product of the rows after
possibly lowering positive exponents to one. Its bit length is at most `R`.
Every individual block divides at least one row and has at most `r` bits.

## 7. Exact gcd-call count

Let a fixed product tree have depth `D`.

For every touched leaf:

- one root gcd is part of the insertion loop;
- at most `D` gcds locate a leaf, carrying the exact selected-subtree gcd;
- two saturation gcds isolate equal support; and
- if its equal-support recursion has `e` nodes, it has `e-1` recursive
  edges. Every edge uses one saturation gcd, and every nonroot node uses one
  ordinary gcd. This contributes `2(e-1)` more calls.

Thus the pair-refinement calls for that touch are exactly bounded by

\[
 2+2(e-1)=2e,
\]

in addition to the root and tree-location calls. Across row insertions, the
root loop executes at most `T+m` times: one for every touch and at most one
final coprime result per row. Independent terminal verification uses exactly
`S` calls. The total is therefore

\[
 (T+m)+DT+2E+S
 =(D+1)T+m+2E+S.
\]

There is no scan over unordered block pairs.

## 8. Terminal verification identity

Let `P=product(q_j)`. Since `q_j` divides `P`, there is an integer `U_j`
with

\[
 P\bmod q_j^2=q_jU_j,
 \qquad 0\le U_j<q_j.
\]

Writing `P=q_j Q_j` gives

\[
 U_j\equiv Q_j\pmod {q_j}.
\]

Consequently

\[
 \gcd(q_j,U_j)=\gcd(q_j,Q_j).
\]

All these gcds are one exactly when every `q_j` is coprime to the product of
the other blocks, which is equivalent to pairwise coprimality. A product tree
and remainder tree compute all residues without pair enumeration.

## 9. Square matrix and roots

For a binary selection vector `c`, define

\[
 E_j=\sum_i c_i e_{ji}.
\]

Pairwise coprimality means the selected product is square exactly when every
nonsquare block has even `E_j`. Indeed, a nonsquare block contains at least
one rational prime to odd valuation, while no other block contains that
prime. A square block is harmless for every `E_j`. This proves the parity
matrix equivalence.

For a singleton, the parity condition says precisely that its column is
zero. For a pair, binary addition says precisely that its two columns agree.
The proposed class basis spans all pairs inside every signature class: in a
nonzero class,

\[
 e_i+e_j=(e_r+e_i)+(e_r+e_j),
\]

and zero-class pairs are sums of zero-class unit vectors. Vectors from
different classes cannot be support-two relations. This proves completeness
of the low span and the displayed hit counts. The displayed generators are
independent: every zero-class generator has its own coordinate, and every
star generator has a unique nonrepresentative coordinate inside its class.
They are therefore a basis.

Canonical reduction of a full kernel basis modulo this low basis maps the
kernel onto a coordinate normal-form subspace. Its kernel is exactly the low
span. The nonzero independent normal forms therefore give a direct
complement, proving the dimension claim in the pseudocode.

For a kernel vector, nonsquare-block exponents are even, so

\[
 \prod_{q_j\text{ square}}\sqrt{q_j}^{E_j}
 \prod_{q_j\text{ nonsquare}}q_j^{E_j/2}
\]

is the exact positive integer root. It uses no rational-prime factorization.

P66's overlap identity applies because every supplied root is a unit. Thus
the normalized-root map is a homomorphism. If every vector in a basis maps
to the global subgroup `{+1,-1}`, the complete span does. Conversely, a
non-global image forces a non-global basis image. The direct-sum low basis
and structural complement have total dimension equal to the kernel
dimension, at most `m`. This proves the root-verification bound.

## 10. Exact D05 peel reconstruction

Fix an active row set. In a pairwise-coprime representation, all rational
primes inside one block `q_j` have the same positive row support, because

\[
 v_p(a_i)=v_p(q_j)e_{ji}
\]

for each prime `p` in that block. Therefore the complete primary part of row
`i` absent from every other active row is

\[
 b_i=\prod_{j:\ e_{ji}>0,\ e_{jk}=0\ (k\ne i)}q_j^{e_{ji}}.
\]

These factors are pairwise coprime. The product `b_i` is nonsquare exactly
when at least one participating block is nonsquare and has odd `e_ji`.
This is precisely the positive-support rule in the statement. Recomputing
active support counts after simultaneous deletions reproduces every D05
round without a new integer gcd.

Parity-degree-one peeling ignores positive even entries. With valuations
`(1,2)` at one rational prime, its parity row is `(1,0)`, but the prime is
not absent from row two. This proves that P106 peeling can be strictly
stronger and that the two semantics cannot be identified.

## 11. Bit complexity

Let `M(k)`, `G(k)`, and `Q(k)` be upper bounds for multiplication, gcd, and
division with remainder on operands of at most `k` bits. Put

\[
 L_r=\lfloor\log_2 r\rfloor,
\]

and define the following safe cost for one modular power whose modulus and
base have at most `r` bits and whose nonzero exponent is at most `r`:

\[
 \operatorname{PowMod}(r)
 =(2L_r+1)M(2r)+(2L_r+2)Q(2r).
\]

This includes the initial reduction, at most `L_r+1` selected
multiplications, at most `L_r` squarings, and every modular reduction.

The recursion forest has exactly `T` roots. It therefore has `E-T` edges.
The two general-support saturations at each root and one saturation at each
edge give exactly `E+T` modular powers and saturation gcds. The nonroot
ordinary gcds number `E-T`. Thus the local refinement has exactly `2E` gcds
on at most `r` bits, as Section 7 states.

Compute `C=d/(A*B)`. The forest then uses at most `E` extra
multiplications and exactly `2T+3E` exact divisions on at most `r` bits:
two exclusive-quotient divisions per touch, and the divisions for `x_0`,
`y_0`, and `C` at each node. A same-support tree emits at most one terminal
block per node. Replacing old leaves and inserting final row residuals thus
causes at most `E+T+m` leaf assignments. Each assignment changes at most
`D` product nodes of at most `R` bits.

Carry the displayed `2 by 2` exponent transforms down to terminal nodes.
This avoids returned-list copying. At most `E+T` old-supported outputs need
a global exponent vector. Their coordinates and vector entries have
`O(log r)` bits, so exact exponent propagation costs
`O(m(E+T)M(log r))` bit operations.

Let

\[
 H=|\{(j,i):e_{ji}>0\}|.
\]

Since every such incidence contributes at least one bit to its row product,
`H<=sum_i floor(log2(a_i))<=R`. Independent row reconstruction therefore
uses at most `H` exact powers with exponents at most `r` and at most `H`
product multiplications, all with intermediate values of at most `r` bits.
Its cost is at most

\[
 (2L_r+2)H M(r).
\]

For terminal coprimality verification, build the product tree of the
moduli `q_j^2`. This uses `S` squarings and at most `S-1`
multiplications on at most `2R` bits. Its remainder tree uses at most
`2S-2` divisions with remainder on at most `2R` bits. The final step uses
exactly `S` divisions on at most `2r` bits and exactly `S` gcds on at most
`r` bits.

Consequently, excluding only sorting comparisons, the refinement,
reconstruction, and independent terminal verification cost at most

\[
\begin{aligned}
 &((D+1)T+m)G(R)+2E G(r)+(E+T)\operatorname{PowMod}(r)\\
 &\quad +(2T+3E)Q(r)+E M(r)+D(E+T+m)M(R)\\
 &\quad +(2L_r+2)H M(r)+(2S-1)M(2R)\\
 &\quad +(2S-2)Q(2R)+S Q(2r)+S G(r)\\
 &\quad +O(m(E+T)M(\log r)).
\end{aligned}
\]

Replacement sorting and final integer-value sorting add
`O((E+T+S) log(E+T+S))` comparisons of at most `r` bits. Since
`T,E,S,m,r,H<=R` and `D=O(log R)`, schoolbook arithmetic gives

\[
 O(R^3\log R)
\]

bit operations for this complete phase. This bound includes row
reconstruction and terminal coprimality verification.

There are at most `m` classified basis vectors. For this bound, form each
selected row product and apply one exact integer square root; do not
separately exponentiate every block for every basis vector. There are at
most `m^2` row-factor multiplications on at most `R` bits. Binary matrix
elimination costs `O(Sm^2)` bit operations, and modular products, integer
roots, inversions, and signed gcds remain within the conservative

\[
 O((R+\operatorname{bitlen}N)^4)
\]

bound for the complete decoder. This is a deliberately loose fixed
polynomial. It is not a runtime projection.

Bernstein's natural-coprime-base algorithm improves the basis phase to
essentially linear time in `R`. F271 does not reprove that result and does
not rely on it for the displayed F265 call cap.

## 12. F265 constants

For one row of at most 361 bits,

\[
 \sum_pv_p(a_i)\le360.
\]

Hence `V<=23040`. The finite certificate verifies

\[
 p_{58}=271,
 \qquad
 \operatorname{bitlen}(p_1\cdots p_{58})=368.
\]

Thus `omega(a_i)<=57` and `T<=63*57=3591`.

For the sharper global block bound, any `S` pairwise-coprime nonunit blocks
select `S` distinct rational primes dividing the input product. The least
possible product of `S` distinct primes is the product of the first `S`
primes. The included deterministic sieve and exact GMP multiplication
verify

\[
 p_{1875}=16103,
 \quad
 \operatorname{bitlen}(p_1\cdots p_{1875})=23102,
\]

\[
 p_{1876}=16111,
 \quad
 \operatorname{bitlen}(p_1\cdots p_{1876})=23116.
\]

The product of 64 numbers below `2^361` is below `2^23104`. Thus `S<=1875`,
a 2,048-leaf tree has depth 11, and substitution in Section 7 gives

\[
 12(3591)+64+2(23040)+1875=91111.
\]

Multiplication by 768 gives `69,973,248`.

## 13. Edge cases

- **One.** It creates no block and gives a zero parity column with exact root
  one.
- **Zero integer.** It is excluded. Square-subset closure under symmetric
  difference fails when zero is admitted.
- **Zero modular residue.** It is nonunit and cannot enter the normalized-root
  premise.
- **Equal integer rows.** They remain separate columns. Their support-two
  relation has exact root equal to the repeated integer, even when their
  supplied modular roots differ.
- **Square integers and square blocks.** They are retained in exact exponent
  reconstruction and omitted only from the parity rows.
- **Prime powers and mixed composite blocks.** The valuation proof treats
  them without factorization.
- **Repeated prime factors of `N`.** P66's normalized-root proof works by
  complete odd prime-power components. F271 changes no part of it.
- **Exponent overflow.** If a block occurs in row `a_i`, its exponent is at
  most `floor(log2(a_i))<=360`. A 16-bit unsigned stored exponent is
  sufficient for the stated F265 domain, but the proof itself assumes exact
  nonnegative integers.
- **Full output requests.** Listing every support-two relation can require
  `binom(m,2)` records. This is an output requirement, not a decoder
  arithmetic requirement.
