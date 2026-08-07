# F62 hostile audit — cross-relation block feedback

**Candidate audited:**
`experiments/F62_cross_relation_feedback_kill/RESULT.md`

**Verified candidate SHA-256:**
`b18f37b176eb697e039946c713c8e20c38e7f2f5f97e2b463436b78719cce67e`

**Verdict:** **PASS, with required scope corrections.**

The quotient law, both stated witness calculations, the infinite
family, the overlap law, and the bit-complexity boundary are correct. The
mechanism is genuinely outside P69: it can feed a product or power of several
available block occurrences, and the aggregate quotient is reduced modulo
that selected product.

The pass is narrow. It proves a new operation relative to P69 and P66. It does
not prove a uniform selector, an all-input success law, a polynomial-time
factoring algorithm, or publication-level novelty.

Four corrections are required:

1. Formalize the exponent budget that makes a block product available.
2. Describe repeated equal relations as deliberate exponentiation, not as
   independent source information or as a distinct-relation witness.
3. Restrict the first `N=21` no-factor statement to its square-kernel decoder.
   An optional direct `g-1` gcd already factors that example.
4. State the remaining source target only after even-input and perfect-power
   preprocessing. Odd prime powers have no non-global square root of one.

No research computation was run for this audit. All additional checks below
are exact hand calculations.

## 1. Exact quotient law — PASS

Let

\[
P_S=\prod_{i\in S}(1+k_iN)=1+K_SN,
\]

and let `1<g<N` divide `P_S`. Since `P_S` is coprime to `N`, so is `g`.
Put `h=P_S/g`. If `w` is the canonical inverse of `g` modulo `N`, then

\[
h=w+tN
\]

for one integer `t>=0`. Therefore

\[
1+K_SN=P_S=g(w+tN)=1+\bigl(k(g)+gt\bigr)N,
\]

so

\[
K_S=k(g)+gt.
\]

The endpoint bounds `1<=w<N` and `1<g<N` give

\[
0<k(g)<g.
\]

The lower bound is strict because `gw>1`. Thus

\[
\boxed{k(g)=K_S\bmod g}
\]

with a nonzero least residue. There is no missing zero-residue case and no
hidden choice of inverse representative.

This proof applies to any positive divisor `g` in the stated range. It does
not require `g` to be prime.

## 2. Exact availability condition — PASS after formalization

The phrase “available whole block powers” must mean the following.

Let `q_1,...,q_r` be the current pairwise-coprime gcd-free blocks. Retain an
exact exponent vector for every endpoint:

\[
x_i=\prod_jq_j^{a_{ij}},
\qquad
y_i=\prod_jq_j^{b_{ij}}.
\]

For an indexed subset `S`, define its total exponent budget

\[
E_j(S)=\sum_{i\in S}(a_{ij}+b_{ij}).
\]

An available product is exactly

\[
g=\prod_jq_j^{c_j},
\qquad
0\le c_j\le E_j(S),
\qquad
1<g<N.
\]

This condition proves `g|P_S`. It also prevents the selector from using an
unknown proper divisor of a composite block. The construction needs no prime
factorization. It uses the exact exponent data already required by P69.

Different endpoint presentations must enter this accounting before equal
decoder columns are removed. Decoder-column deduplication and source exponent
accounting are separate operations.

## 3. Distinct-relation `N=21` witness — arithmetic PASS, wording correction

The candidate uses

\[
22=2\cdot11=1+21,
\qquad
85=5\cdot17=1+4\cdot21.
\]

The two square-class columns have disjoint nonzero supports, so their seed
kernel is zero. The available cross product is

\[
g=2\cdot5=10,
\qquad
22\cdot85=1870=1+89\cdot21.
\]

The quotient law gives `k(10)=89 mod 10=9`. Also

\[
1870/10=187\equiv19\pmod {21},
\qquad
10\cdot19=190=1+9\cdot21.
\]

Thus the new relation value `190` and the new block `19` are real. The three
relation values `22,85,190` have independent square classes, because the
blocks `11`, `17`, and `19` each occur in only one column. Hence the complete
square-kernel decoder on those three columns has no relation to test.

However, the unqualified sentence “this particular step does not yet factor
21” is false if direct screening includes arbitrary `g-1` and `g+1` gcds:

\[
\gcd(10-1,21)=3.
\]

The new inverse endpoint also has

\[
\gcd(19-1,21)=3.
\]

The candidate must say instead: **the new three-column square-kernel decoder
does not factor `21`**. It must also define whether “direct screen” means only
`gcd(g,N)`, or also the opportunistic tests `gcd(g-1,N)` and `gcd(g+1,N)`.
This issue does not
invalidate the new-value or new-block claim.

## 4. Repeated-copy `N=21` witness — PASS with source semantics

For three indexed copies of

\[
A=22=2\cdot11=1+21,
\]

the old square kernel contains exactly the even-cardinality subsets. Each
positive root is a power of `A`, hence is `1` modulo `21`. The old decoder is
therefore factoring-empty.

The full three-copy exponent budget contains `2^3`. For

\[
g=8,
\qquad
A^3=1+507\cdot21,
\]

the quotient law gives `k(8)=507 mod 8=3`. The canonical inverse of `8`
modulo `21` is `8`, and

\[
8^2=64=1+3\cdot21.
\]

Consequently

\[
\gcd(8-1,21)=7,
\qquad
\gcd(8+1,21)=3.
\]

All calculations pass.

The semantic limit is important. Three equal entries do not give three
independent observations. A uniform algorithm may deliberately materialize
three copies, or equivalently authorize the third power of one known block.
That is a legitimate polynomial-time source operation. It must be called
**power feedback** or **reuse of a relation occurrence**. It is not evidence
that three distinct seed relations correlate with the factors.

P66 remains correct when it removes duplicate decoder columns. F62 changes
the source rule: it retains or deliberately creates integer exponent budgets
before that removal.

## 5. Infinite family — PASS

Let odd `t>=3`, `g=2^t`, and

\[
N=\frac{g^2-1}{3}=(g-1)\frac{g+1}{3}.
\]

Because `t` is odd, `g=2 mod 3`. Hence `(g+1)/3` is an odd integer and
`3` does not divide `g-1`. Also

\[
\gcd\left(g-1,\frac{g+1}{3}\right)=1.
\]

Both factors are greater than one, and `g<N` for `g>=8`. The two congruences

\[
g=1\pmod {g-1},
\qquad
g=-1\pmod {(g+1)/3}
\]

show that `g` is a non-global square root of one modulo `N`.

The canonical state `2` gives

\[
A=N+1=2\frac{N+1}{2}.
\]

Moreover,

\[
N+1=\frac{2^{2t}+2}{3}
=2\frac{2^{2t-1}+1}{3},
\]

and the second factor is odd. Thus `A` has exactly one factor of `2` and is
not a square. For `t` indexed copies, all old even-subset roots are powers of
`A` and are global. The full exponent budget makes `2^t=g` available, and

\[
g^2=1+3N.
\]

Finally,

\[
\gcd(g-1,N)=g-1,
\qquad
\gcd(g+1,N)=\frac{g+1}{3}.
\]

The second equality uses `3` not dividing `g-1`. The family is exact.

Its explicit size is polynomial. Since `log N=Theta(t)`, the list has `t`
entries of `O(log N)` bits, so even a literal duplicate list has
`O((log N)^2)` bits. The selected `g` has `O(log N)` bits. The product
`A^t`, if formed, also has polynomial bit length. This validates the bit-cost
claim for the family.

The family is manufactured and easy. It gives no density, probability, or
all-input theorem.

## 6. A distinct-relation useful stress test

The candidate's useful stated witness uses repeated copies. The mechanism
also survives when equal-relation reuse is forbidden.

Take `N=55` and the two distinct canonical relations

\[
2\cdot28=56=1+55,
\qquad
3\cdot37=111=1+2\cdot55.
\]

Complete refinement gives blocks `2,3,7,37`. Their two square-class columns
are independent: the first has odd support on `2,7`, and the second on
`3,37`. Thus the seed square kernel is zero.

Select one block from each relation:

\[
g=3\cdot7=21.
\]

Then

\[
56\cdot111=6216=1+113\cdot55,
\qquad
6216/21=296\equiv21\pmod {55}.
\]

Therefore the canonical inverse of `21` is `21`, and

\[
21^2=441=1+8\cdot55.
\]

It gives

\[
\gcd(21-1,55)=5,
\qquad
\gcd(21+1,55)=11.
\]

This hand witness confirms that the surviving phenomenon is not an artifact
of arbitrary duplicate copies. It still proves only success on one input.

## 7. Shared divisors and duplicate certificates — PASS

If the same `g` divides both `P_S=1+K_SN` and `P_T=1+K_TN`, then `g` is a
unit modulo `N` and

\[
K_S\equiv K_T\equiv-N^{-1}\pmod g.
\]

Thus different subset certificates cannot assign different canonical
quotients to one selected state. They are provenance duplicates.

Full integer exponents remain necessary. Square-class parity cannot decide
whether `q_j^e` is an available divisor of a subset product.

## 8. States at or above `N` — PASS

For a selected divisor `G>N`, write

\[
G=a+sN,
\qquad
P_S/G=b+tN,
\qquad
1\le a,b<N.
\]

Then `b` is the canonical inverse of `a`, and direct expansion gives

\[
K_S=k(a)+at+bs+stN.
\]

Thus reduction of `G` modulo `N` is a different feedback operation. The law
`k(g)=K_S mod g` proved for `g<N` cannot be transferred to `G`.

The case `G=N` is impossible because `P_S=1 mod N` is coprime to `N`.

## 9. Iteration and complexity — PASS with an explicit cap

The complementary endpoint

\[
w=(P_S/g)\bmod N
\]

can contain a new block. The first `N=21` witness gives `w=19`. Therefore
P69's one-refinement fixed-point proof does not extend to this rule.

Immediate repetition of `g` or its inverse only reproduces one canonical
relation. This does not control later products that mix a new block with old
blocks. The candidate correctly proves no depth bound.

For a polynomial-size explicit transcript, every canonical relation value is
less than `N^2` and has `O(log N)` bits. A product of polynomially many such
values has polynomial bit length. Gcd-free refinement, exponent accounting,
division, modular reduction, inversion, and direct gcd screening therefore
have polynomial bit cost per polynomially bounded round.

This is not a polynomial-time enumeration theorem. The number of indexed
subsets and admissible exponent vectors can be exponential. A randomized
algorithm can sample a subset cheaply, but F62 gives no success probability
for such a sample.

## 10. Remaining algorithmic scope

The final source-selection sentence needs one correction. It cannot require a
non-global square root for every composite `N`. For an odd prime power, the
only square roots of one are the global roots `1` and `-1`.

The correct all-input target is:

- first handle even inputs and perfect powers by standard polynomial-time
  preprocessing; then
- for every remaining odd composite input, select only polynomially many
  admissible block products and prove that a direct gcd or a non-global root
  occurs with inverse-polynomial probability.

No such selector or probability theorem is in the candidate. The explicit
witnesses show only that the operation can change the relation list and can
sometimes expose a factor.

The phrase “algebraic novelty” must mean **new relative to the closed P69
operation in this project**. No literature review, cross-family audit, or
human audit has established publication-level novelty.

## 11. Final verdict

The mathematical mechanism passes hostile audit after the four stated scope
corrections. In particular, the exact quotient law is sound, endpoint-block
availability can be made exact without factoring the blocks, and both
duplicate-powered and genuinely distinct-relation useful witnesses exist.

The non-trivial surviving step is the selector, not the final gcd. F62 has
shown that a suitable product can exist and can be built from public block
data. It has not shown how to find such a product on every hard input in
polynomial time.
