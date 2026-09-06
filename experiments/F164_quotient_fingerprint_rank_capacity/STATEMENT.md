# F164 candidate — quotient fingerprints give a rank–capacity updater

## Status and scope

This is a proof-only candidate. It starts in the unresolved last branch of
F161: several public released unit blocks have local relative order larger
than the quasipolynomial scan cap against one certified common-order state.

The exact new result is a finite-bank state machine:

\[
\boxed{
\text{factor}
\quad\lor\quad
\text{multiplicative local-capacity growth}
\quad\lor\quad
\text{one new aligned integer relation}.}
\]

The capacity and relation rank are public and monotone. If their lower and
upper bounds meet, Smith normal form gives a larger certified common cyclic
subgroup. They need not meet. A synchronized cyclic quotient can absorb
arbitrarily many released blocks without further abstract subgroup growth.
Thus this candidate is not an all-input source theorem and not a factoring
algorithm.

## 1. Closest prior results and material difference

- P71 identifies full hidden relation-lattice recovery as an order-finding
  boundary. This candidate does not recover that lattice. It keeps only
  relations exposed by a finite public word bank.
- P138 and P143 construct and decode decorated section relations. This
  candidate starts after their integer refinement has released public unit
  blocks. It retains their exact word and occurrence provenance.
- P146/F159 proves that one released block can enlarge the named subgroup,
  and tests only `gcd(d^M-1,N)`.
- F161 scans the pure powers of one block through relative order `B`. This
  candidate scans cross words from several blocks, converts every common
  collision into an aligned relation, and compares the resulting relation
  index with a public quotient-capacity count.

## 2. Certified state and quotient fingerprints

Let `N>=3` be odd. For the proof only, write

\[
N=\prod_{j=1}^s R_j,
\qquad R_j=p_j^{\alpha_j},
\]

where the `p_j` are distinct odd primes. Let `(g,M)` satisfy the F161
common-order certificate. Thus the public factorization of `M` is known,
`gcd(M,N)=1`, and

\[
\operatorname{ord}_{R_j}(g)=M
\qquad(1\le j\le s).
\]

Put `n=ceil(log_2(N+1))`. Let `B>=2` satisfy

\[
B\le 2^{C(\log_2(n+1))^k}
\]

for fixed constants `C,k`, and assume every prime factor of `M` is at most
`B`, as in F161.

Put

\[
H_j=\langle g\bmod R_j\rangle.
\]

Let `d_1,...,d_t` be public units. For `v in Z^t`, define

\[
d^v=\prod_{i=1}^t d_i^{v_i}\pmod N,
\qquad
F(v)=(d^v)^M\pmod N.
\tag{1}
\]

Negative exponents use public modular inverses. For every component,

\[
F(u)=F(v)\pmod {R_j}
\quad\Longleftrightarrow\quad
d^{u-v}\in H_j.
\tag{2}
\]

Thus `F(v)` is an exact public fingerprint of the local quotient coset
`d^v H_j`.

## 3. Finite-bank capacity theorem

Let `S` be any finite public set of exponent vectors with full provenance.
Compute `F(v)` for every `v in S`. For every pair `u,v`, compute

\[
G_{u,v}=\gcd(F(u)-F(v),N).
\tag{3}
\]

If one value is proper, return it. On the no-factor branch, each pair of
fingerprints is either equal modulo `N` or different modulo every hidden
prime-power component.

Delete exact duplicate fingerprints and retain one provenance-bearing word
for each value. Let

\[
\kappa(S)=|\{F(v):v\in S\}|.
\tag{4}
\]

Then, for every hidden component,

\[
\left|\langle H_j,d_1,\ldots,d_t\rangle\right|
\ge M\kappa(S).
\tag{5}
\]

If `S` only grows, `kappa(S)` never decreases. Equation (5) is therefore a
public accumulated lower bound on every local generated subgroup.

## 4. One-block layer updater over an old bank

Let `T` contain one representative of each of `kappa` distinct quotient
fingerprints from the old blocks. Introduce one new public unit `d`. For
`e=0,1,...,B`, form the layer

\[
T_e=d^eT.
\tag{6}
\]

Process the layers in increasing `e`. Compare every new fingerprint with all
fingerprints in the earlier layers by (3). Internal differences inside a
layer inherit the old no-factor certificate.

Exactly one of the following happens.

1. **Factor.** A difference gcd is proper, or the alignment step below
   finds a hidden-component mismatch.
2. **First common collision.** For the first index `e<=B`, there are
   `f<e` and `w,w' in T` with

   \[
   F(d^e w)=F(d^f w')\pmod N.
   \tag{7}
   \]

   The earlier layers are pairwise disjoint, so retaining
   `T_0,...,T_{e-1}` multiplies the public capacity by exactly `e`.
   Put

   \[
   x=d^{e-f}ww'^{-1}.
   \tag{8}
   \]

   Then `x^M=1 mod N`. The factor-first Pohlig--Hellman alignment from F161
   returns a factor or one public `a mod M` such that

   \[
   d^{e-f}ww'^{-1}=g^a\pmod N.
   \tag{9}
   \]

   This is a new exact relation. Its coefficient on the new block is the
   nonzero integer `e-f`, so it is rationally independent of all old
   relations that do not use the new block.
3. **No collision through the cap.** All `B+1` layers are disjoint in every
   hidden quotient. Retaining them multiplies `kappa` and the lower bound
   (5) by exactly `B+1`.

If the new block has local relative order larger than `B` against the
original `H_j` in every component, the first call from `T={1}` must take
outcome 3. The same hypothesis for later blocks does not force later
outcome 3, because a later block can lie in the quotient subgroup generated
by earlier blocks.

## 5. Rank–capacity accounting

Use coordinates `(z,v_1,...,v_t)` for the public word

\[
g^z\prod_i d_i^{v_i}.
\]

Let `L` be the integer lattice generated by the base relation
`(M,0,...,0)` and all aligned relations from (9). Keep the actual words and
their provenance with every row.

When blocks are introduced one at a time, retain only the first collision
relation for the accounting below. Let `r` be the number of these rows,
excluding the base row, and let `delta=t-r`. Every collision call increases
both `t` and `r` by one. Every no-collision call increases `t` only and
multiplies `kappa` by `B+1`. Therefore

\[
\boxed{\kappa\ge(B+1)^\delta.}
\tag{10}
\]

Collision calls can increase `kappa` by the additional factor `e`, but this
is not needed in (10). The public state has an exact tradeoff: every new
block either increases the known relation rank or consumes multiplicative
local quotient capacity.

This law does not say that `delta` becomes zero. The first block in the
F161 beyond-cap branch creates at least one unresolved cyclic direction.

## 6. Exact rank–volume closure

Additional collision relations can be retained, not only the first one per
block. Suppose the complete retained lattice `L` has full rank `t+1`. Let

\[
D=[\mathbf Z^{t+1}:L],
\tag{11}
\]

computed by Hermite or Smith normal form. Then for every hidden component,

\[
M\kappa(S)
\le
|\langle g,d_1,\ldots,d_t\rangle_{R_j}|
\le D.
\tag{12}
\]

If the public lower and upper bounds meet,

\[
\boxed{D=M\kappa(S),}
\tag{13}
\]

then the presentation `Z^(t+1)/L` maps isomorphically to the generated
subgroup in every hidden component. Since each component unit group is
cyclic, the presentation is cyclic. Smith normal form returns one public
word `h` with exact common order `D` globally and in every component.

Compute `gcd(D,N)` first. A proper value is a factor. On the surviving
branch, factor `kappa(S)` by trial division and merge it with the supplied
factorization of `M`. When the explicit bank has quasipolynomial size, this
keeps a complete quasipolynomially obtainable factorization of `D`. Thus
`(h,D)` is a valid next F161 state.

If `L` is not full rank, or if `D>M kappa(S)`, the finite transcript does not
certify the exact subgroup order. Rank or many relations alone are not
enough.

## 7. Exact provenance-compatible obstruction

The individual beyond-cap condition does not multiply across distinct
gcd-free blocks. Take

\[
N=341=11\cdot31,
\qquad g=-1=340,
\qquad M=2,
\qquad B=2.
\]

The two canonical-inverse exact relations

\[
337\cdot85=1+84N,
\qquad
325\cdot277=1+264N
\tag{14}
\]

are legal. Joint gcd-free refinement includes the pairwise-coprime unit
blocks

\[
d_1=337=-4\pmod N,
\qquad
d_2=277=-64\pmod N.
\]

Both have local relative order five against `{+1,-1}` modulo both hidden
primes. Thus both F161 scans through `B=2` take the beyond-cap branch.
Nevertheless

\[
d_2d_1^2=-1=g\pmod N.
\tag{15}
\]

Therefore `d_2` adds no quotient subgroup after `d_1`. The F164 bank detects
the aligned relation (15), but the remaining one-dimensional order relation
has size five and is outside the cap. No factor or second multiplicative
gain is forced.

More generally, in two cyclic hidden quotients choose the same cyclic group
of prime order `R>B`, identify their generators by an automorphism, and map
every released block to a power of that one generator. Every individual
relative order can equal `R`; all membership and collision kernels are
synchronized; and the generated quotient order remains `R` no matter how
many blocks are named. This is the exact cyclic-group countermodel to a
rank-from-block-count or volume-from-provenance law.

## 8. Quasipolynomial cost and remaining condition

For an explicit bank of quasipolynomial size, all modular powers, pairwise
gcds, factor-first alignments, and integer normal forms take deterministic
quasipolynomial time in `n`. A repeated run must impose an explicit
quasipolynomial cap on the retained bank. The theorem does not give a
compressed evaluator for a larger bank.

The smallest exact missing condition is one of the following equivalent
forms of progress:

1. a source law makes the new quotient layers disjoint often enough to keep
   multiplying `kappa` within a quasipolynomial bank;
2. a source law supplies enough additional aligned collisions to make `L`
   full rank and force `D=M kappa`; or
3. a public procedure certifies relative order against the subgroup
   generated by all earlier blocks, not only against the original `H_j`.

Without one of these conditions, several beyond-cap blocks can encode only
one hidden large-order cyclic direction. F164 isolates and measures that
remaining obstruction but does not remove it.
