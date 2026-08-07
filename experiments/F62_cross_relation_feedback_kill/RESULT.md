# F62 — cross-relation block feedback kill-first result

**Status:** the proposed mechanism survives the algebraic kill test, but no
all-input sampler law follows.

No research computation was run. All witnesses below are exact
hand calculations.

## 1. Setup

Let $N\ge 3$. Every seed relation has canonical unit endpoints

\[
A_i=x_i y_i=1+k_iN,\qquad 1\le x_i,y_i<N.
\]

For a nonempty indexed subset $S$, including distinct indices that can carry
equal relation values, put

\[
P_S=\prod_{i\in S}A_i=1+K_SN.
\]

Let $q_1,\ldots,q_r$ be the current pairwise-coprime gcd-free blocks. Retain
the exact endpoint exponent vectors

\[
x_i=\prod_jq_j^{a_{ij}},\qquad y_i=\prod_jq_j^{b_{ij}}.
\]

For the indexed subset $S$, put

\[
E_j(S)=\sum_{i\in S}(a_{ij}+b_{ij}).
\]

An available block product is exactly

\[
g=\prod_jq_j^{c_j},\qquad 0\le c_j\le E_j(S).
\]

This exponent budget proves $g\mid P_S$ without using a proper factor of an
unfactored block. Endpoint presentations and full exponents must be retained
for this source operation before any equal decoder columns are removed.
Assume

\[
1<g<N.
\]

Every endpoint and every block is coprime to $N$. Hence $g$ is a unit modulo
$N$ and has a canonical inverse state.

## 2. Exact quotient law

### Lemma 1

Let $w$ be the least positive inverse of $g$ modulo $N$, and write

\[
gw=1+k(g)N.
\]

Then

\[
\boxed{k(g)=K_S\bmod g,}
\]

where the residue is in $\{1,\ldots,g-1\}$.

### Proof

Write

\[
h=P_S/g.
\]

Since $gh=P_S\equiv1\pmod N$, the canonical inverse $w$ is the least positive
residue of $h$ modulo $N$. Thus $h=w+tN$ for an integer $t\ge0$. Therefore

\[
P_S=g(w+tN)=1+N(k(g)+gt).
\]

Comparison with $P_S=1+K_SN$ gives

\[
K_S=k(g)+gt.
\]

Also $0\le k(g)<g$. The value cannot be zero because $g>1$ and
$gw=1+k(g)N>1$. Hence $k(g)$ is exactly the least positive residue of $K_S$
modulo $g$. $\square$

This is the point where the F61 single-relation stagnation proof stops
applying. The subset quotient $K_S$ can be much larger than every $k_i$, so a
block product $g$ larger than every seed quotient can still produce a new
residue.

## 3. A distinct-relation witness that creates a new value and block

Take

\[
N=21.
\]

Use the two canonical inverse relations

\[
2\cdot11=22=1+1\cdot21,
\qquad
5\cdot17=85=1+4\cdot21.
\]

Their complete gcd-free blocks are

\[
2,\ 5,\ 11,\ 17.
\]

Neither relation is a square, the two values are coprime, and the exact
square-class kernel of the seed list is zero.

Select both relations. Then

\[
P_S=22\cdot85=1870=1+89\cdot21.
\]

Choose the genuinely cross-relation divisor

\[
g=2\cdot5=10.
\]

It divides $P_S$, but it divides neither seed relation by itself. Lemma 1
gives

\[
k(10)=89\bmod10=9.
\]

Indeed,

\[
P_S/g=187\equiv19\pmod {21},
\qquad
10\cdot19=190=1+9\cdot21.
\]

The feedback step has therefore created the new relation value $190$. It has
also created the new gcd-free block $19$, which divides no seed value.

This refutes a general claim that cross-relation feedback is only the old
complete decoder in another form. The old seed kernel is zero, while the
feedback list contains a new integer and a new prime block. The new
three-column list still has full square-class rank, so its square-kernel
decoder has no relation to test. However, the selected state already factors
under an opportunistic direct screen:

\[
\gcd(10-1,21)=3.
\]

Thus this witness is both a new-value example and a successful one-step
selector example. Its new three-column *square kernel* remains empty.

## 4. A distinct-relation useful square-root witness

The phenomenon does not depend on repeated equal relations. Take

\[
N=55
\]

and the two distinct canonical relations

\[
2\cdot28=56=1+55,
\qquad
3\cdot37=111=1+2\cdot55.
\]

Complete refinement gives the blocks $2,3,7,37$. The two seed square-class
columns are independent. Select one block from each relation:

\[
g=3\cdot7=21.
\]

Then

\[
56\cdot111=6216=1+113\cdot55,
\qquad
113\bmod21=8.
\]

The complementary endpoint is

\[
6216/21=296\equiv21\pmod {55}.
\]

Hence the selected state is self-inverse:

\[
21^2=441=1+8\cdot55.
\]

It gives both proper factors,

\[
\gcd(21-1,55)=5,
\qquad
\gcd(21+1,55)=11.
\]

The old seed kernel is zero. This is therefore a genuinely cross-relation
useful state, not a power of one repeated relation.

## 5. A useful power-feedback witness

The treatment of equal relation values is decisive.

Again take $N=21$, but deliberately authorize three indexed uses of

\[
A=2\cdot11=22=1+21.
\]

The seed square kernel consists of the even-cardinality subsets. Each such
subset has exact positive root $22^j\equiv1\pmod {21}$. Thus the complete old
decoder has only global roots and returns no factor.

The block $2$ occurs once in each indexed copy. For the subset of all three
copies,

\[
P_S=22^3=1+507\cdot21.
\]

Choose the available whole block power

\[
g=2^3=8<21.
\]

Lemma 1 gives

\[
k(8)=507\bmod8=3.
\]

The canonical inverse of $8$ modulo $21$ is $8$, so the new relation is

\[
8^2=64=1+3\cdot21.
\]

Its exact root is non-global:

\[
\gcd(8-1,21)=7,
\qquad
\gcd(8+1,21)=3.
\]

Thus power feedback can create a useful square relation even when
the complete decoder on the seed multiset has no useful root.

In this witness the factor is available as soon as the selected state is
known: $g$ is self-inverse, so direct screens of $\gcd(g-1,N)$ and
$\gcd(g+1,N)$ give the same factors before the relation is inserted into a
batch decoder. The algorithmic credit therefore belongs to the cross-relation
subset/block selector, not to a stronger final decoder.

This witness depends essentially on an explicit exponent budget. Three equal
entries are not three independent observations. A uniform algorithm can
deliberately reuse the relation three times, or equivalently authorize the
third power of its known block. Deduplicating equal $k$ or equal $A$ before
block-power formation destroys this source operation. P66's rule that
duplicate columns can be removed without changing the old normalized-root
image remains correct for decoding; it does not preserve the exponent budget
of this different feedback source.

## 6. An infinite exact power-feedback family

The preceding example is the first member of an unbounded family.

Let $t\ge3$ be odd and put

\[
g=2^t,
\qquad
N=\frac{g^2-1}{3}
  =(g-1)\frac{g+1}{3}.
\]

Because $t$ is odd, $g+1$ is divisible by $3$. Both displayed factors of $N$
are odd, greater than one, and coprime. Moreover,

\[
g\equiv1\pmod {g-1},
\qquad
g\equiv-1\pmod {(g+1)/3}.
\]

Hence $g$ is a non-global square root of one modulo $N$. Also $g<N$.

The public state $2$ gives

\[
A=N+1=2\cdot\frac{N+1}{2}=1+N.
\]

Since

\[
N+1=\frac{g^2+2}{3}
\]

has exactly one factor of $2$, $A$ is not a square and its gcd-free
decomposition contains one copy of the block $2$.

Take $t$ indexed copies of this seed relation. Their old square kernel
contains exactly the even-cardinality subsets, and every old kernel root is a
power of $A\equiv1\pmod N$. The old decoder is therefore factoring-empty.

For the subset containing all $t$ copies, the block power $2^t=g$ divides
$P_S=A^t$. Feeding it gives

\[
g^2=1+3N.
\]

The two proper gcds are

\[
\gcd(g-1,N)=g-1,
\qquad
\gcd(g+1,N)=\frac{g+1}{3}.
\]

Here $t=\Theta(\log N)$, so the seed list and the integer $g$ have polynomial
bit size. Yet $g=\Theta(\sqrt N)$ is exponentially larger than the seed
quotient $1$. This rules out domination by the F61 direct scan up to the
largest seed quotient.

The family is easy and proves no all-input success law. Its purpose is to
show that the new operation is genuinely stronger than the old finite-list
decoder and the small-quotient feedback rule.

## 7. Subset overlap and shared divisors

The same block product $g$ can divide several subset products, but it cannot
produce conflicting quotient residues. If

\[
g\mid P_S,\qquad g\mid P_T,
\]

then, because $\gcd(g,N)=1$,

\[
K_S\equiv K_T\equiv-N^{-1}\pmod g.
\]

Thus Lemma 1 assigns the unique canonical quotient $k(g)$ in every case.
Different subset certificates for the same $g$ are provenance duplicates, not
different new states.

Subset overlap must nevertheless retain full integer exponents. Parity data
is enough for the square decoder but not for divisor feedback. The useful
$N=21$ witness fails if the three occurrences of block $2$ are reduced
modulo two or if equal relations are deduplicated.

## 8. The restriction $g<N$ is essential

If a selected divisor $G$ is larger than $N$, it is not a canonical state.
Let

\[
G=a+sN,\qquad P_S/G=b+tN,
\qquad 1\le a,b<N.
\]

Then $a$ and $b$ are inverse residues and

\[
K_S=k(a)+at+bs+stN.
\]

There is no general law $k(a)=K_S\bmod G$. Replacing $G$ by its residue
$a=G\bmod N$ is a different feedback rule. It can discard the whole-block
divisor structure that selected $G$.

The case $G=N$ cannot occur because every divisor of $P_S\equiv1\pmod N$ is
coprime to $N$.

## 9. Iteration

Write

\[
P_S/g=w+tN,\qquad 1\le w<N.
\]

The fed relation has endpoints $g,w$. The endpoint $g$ is assembled from old
blocks, but $w$ need not be. In the first $N=21$ witness,

\[
w=19,
\]

which is a new block. Later rounds can therefore expand the block basis and
create new admissible products. There is no one-round fixed-point theorem like
F61.

Selecting the same state $g$ again only reproduces its unique relation.
Feeding its inverse $w$ also reproduces that relation. This removes immediate
two-state duplication, but it does not control combinations of the new block
with blocks from other relations.

There is no proved monotone depth measure. Under a polynomial cap, each
chosen product, division, reduction, and modular inverse has polynomial bit
cost, because a product of polynomially many explicit relation values has
polynomial summed bit length. But the number of subsets and block-power
divisors can be exponential. Exhaustively enumerating them is not a
polynomial-time sampler.

## 10. Disposition

The mechanism **survives** the requested kill-first test:

- the exact quotient law holds;
- cross-relation reduction can create a new relation value;
- its complementary residue can create a new gcd-free block;
- both distinct-relation products and deliberate power feedback can create a
  non-global square root that the complete old decoder cannot see; and
- the new state can be exponentially larger than every seed quotient while
  retaining polynomial bit length.

The remaining gap is source selection. First handle even inputs and perfect
powers by standard polynomial-time preprocessing. On every remaining odd
composite, one must give a uniform rule that chooses only polynomially many
subsets and block powers and prove that a direct factor or a non-global root
occurs with inverse-polynomial probability. Odd prime powers themselves have
no non-global square root of one, which is why the perfect-power preprocessing
is part of the correct target. The witnesses above establish algebraic novelty
relative to P69, not that selection law and not an all-input factoring
algorithm. Every selected state should be screened directly before it is
added; a self-inverse useful state needs no later square-kernel computation.
