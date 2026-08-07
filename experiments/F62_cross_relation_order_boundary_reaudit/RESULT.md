# Fresh hostile re-audit — F62 exact order and HSP boundary

## Disposition

I audited the complete corrected artifact
`experiments/F62_cross_relation_order_boundary/RESULT.md` at SHA-256

```text
b0d19ae14669dbe1330fafd22447919368149b497accf870387abbda1e891bae
```

I used the preserved failed audit only as a repair checklist. That audit is
`experiments/F62_cross_relation_order_boundary_audit/RESULT.md` at SHA-256

```text
862c5dc768cee9a91933f9acfe5bdfdd9d4554eda81b3e2ded48a2bcb6d60289
```

It audited the superseded candidate at SHA-256

```text
bc5419bb224cb95eb26e9b42bb786b0b193c2782552a835aa5cf72065abedf18
```

**Verdict: PASS.** All ten objections in the failed audit are genuinely
repaired. I then re-derived the corrected theorem without treating that audit
as evidence. I found no new mathematical, source-scope, or complexity gap
inside the corrected artifact's stated boundary.

The result is a boundary theorem, not a factoring theorem. It proves exact
statements about the self-inverse subtarget, order finding, supplied relation
lattices, finite legal source boxes, and two explicit witnesses. It correctly
leaves the all-input direct-separator law open.

No research computation was run. The checks below are symbolic derivations
and read-only artifact inspection. Hashing was used only to identify the
audited files.

## 1. Full direct screening and the self-inverse subtarget

For a selected occurrence set, write

\[
E=\sum_i c_i\lambda_i,
\qquad
g=q^v,
\qquad
h=q^{E-v}.
\]

Since every selected relation is $1$ modulo $N$,

\[
gh=q^E\equiv1\pmod N.
\]

Thus $h\equiv g^{-1}\pmod N$. It follows exactly that

\[
g\equiv h
\Longleftrightarrow
g^2\equiv1\pmod N
\Longleftrightarrow
2v\in\Lambda_N.
\]

For odd $N$, a self-inverse unit is one of the two signs on each
prime-power CRT component. If it is neither global sign, both signs occur.
Consequently both

\[
\gcd(g-1,N),\qquad \gcd(g+1,N)
\]

are nontrivial and proper. Conversely, either global sign makes one gcd
$N$ and the other $1$. The corrected self-inverse theorem is exact.

The artifact no longer claims that this characterizes the full F62 screen.
That screen only asks whether either displayed gcd is proper. For squarefree
$N$, if

\[
S_\epsilon=\{p\mid N:g\equiv\epsilon\pmod p\},
\qquad \epsilon\in\{1,-1\},
\]

then the $\epsilon$-screen succeeds exactly when $S_\epsilon$ is nonempty
and proper. Components outside $S_\epsilon$ need not carry the opposite
sign, or any sign. For prime powers, a positive proper valuation of
$g-\epsilon$ can also split $N$. This is strictly broader than
$2v\in\Lambda_N$.

The corrected $N=21,g=10$ example establishes the strictness:

\[
10^2\equiv16\not\equiv1\pmod {21},
\qquad
\gcd(10-1,21)=3.
\]

The iterative-endpoint sentence is also scoped correctly. A non-self-inverse
separator or miss can create an inverse endpoint for a later round without
turning the intermediate selection into a 2-torsion search.

## 2. Finite capacities, legal boxes, and integer magnitude

The source is now a finite indexed occurrence list. Equal presentations stay
as separate indices, and each occurrence has

\[
c_i\in\{0,1\}.
\]

Deliberate amplification first adds explicit occurrences. The alternative
row-type formulation is stated only with finite capacities
$0\le c_i\le\mu_i$. There is no remaining implicit unlimited reuse.

For a chosen list, the exact source box is

\[
0\le v\le E.
\]

This makes $q^v$ an integer whole-block divisor of the selected aggregate.
The additional condition

\[
1<q^v<N
\]

is kept as an integer condition. The artifact does not replace an oversized
product by its residue while retaining the legal-divisor claim.

The same distinction is present in the one-block order paragraph. A capacity
$M$ only makes the least involutory exponent available when $r/2\le M$.
Legality also needs $a^{r/2}<N$, and factoring needs a non-global residue.
Pure modular exponentiation is explicitly identified as another operation.

These statements also charge amplification correctly. In the multiplicity
family, $t$ copies are present in the input transcript; they are not free
uses of one occurrence.

## 3. Exact old-decoder residue image

Let

\[
L_0=\langle\lambda_1,\ldots,\lambda_m\rangle_{\mathbb Z}
\subseteq\Lambda_N.
\]

The claimed equality is

\[
R_{\rm old}
=
\{\Phi_N(v):v\in\mathbb Z^s,\ 2v\in L_0\}.
\]

The forward inclusion is immediate. For the converse, write

\[
2v=\sum_i z_i\lambda_i.
\]

Choose $c_i\in\{0,1\}$ with $c_i\equiv z_i\pmod2$, including for
negative $z_i$. Then $z=c+2w$ for $w\in\mathbb Z^m$, and

\[
v=
\frac12\sum_i c_i\lambda_i+
\sum_i w_i\lambda_i.
\]

The first term is integral. The second lies in $L_0\subseteq\ker\Phi_N$.
It can therefore change the exponent representative but not its modular
residue. This proves the equality even with negative lattice coefficients.

The artifact consistently labels this as a modular residue-image theorem.
It does not infer that a right-hand representative is nonnegative, lies in a
current box, or gives an integer below $N$.

The quotient formulation is also exact. With

\[
Q_0=\mathbb Z^s/L_0,
\qquad
K=\Lambda_N/L_0,
\]

the generated subgroup is $Q_0/K$, and the old image is the image of
$Q_0[2]$. A class gives a nonidentity involution precisely when

\[
x\notin K,
\qquad
2x\in K.
\]

The corrected artifact does not call these abstract conditions a legal F62
root. It separately requires a non-global residue outside the old image, a
representative in a finite occurrence box, and $1<q^v<N$.

## 4. Exact cyclic order boundary

Let $r=\operatorname{ord}_N(a)$. The requested exponent satisfies

\[
r\mid2e,
\qquad
r\nmid e.
\]

There is no solution for odd $r$. For even $r$, all and only the solutions
are

\[
e=\frac r2(2j+1),
\qquad j\ge0.
\]

Hence the least answer is $r/2$, and all answers produce the same
involution $a^{r/2}$. This proves the stated equivalence on the even-order
promise. It does not equate an arbitrary successful exponent with the order.

The total-oracle reduction for odd order is also correct. If the least-answer
oracle returns `NONE` on $a$, then $r$ is odd. Since $N$ is odd,
$-1$ has order $2$, and

\[
(-a)^r=-1,
\qquad
(-a)^{2r}=1.
\]

Thus $-a$ has exact order $2r$, and its least answer is $r$. The two
directions give the claimed abstract Turing equivalence with modular order
finding. The artifact correctly says that the $-a$ query need not preserve
an F62 source box. It also correctly distinguishes a least nonidentity
involutory-power oracle from the weaker least factoring-useful-power oracle.

The example modulo $21$ confirms why leastness matters: exponent $3$ is
valid for both the order-$6$ element $2$ and the order-$2$ element $8$,
and both yield $8$.

Finally, for one generator the kernel is exactly

\[
\Lambda_N=r\mathbb Z.
\]

Full relation-lattice recovery therefore contains unrestricted exact order
finding, without relying on the even-order promise.

## 5. The two finite witnesses

### The $N=65$ cross-block witness

The two relations factor as

\[
66=2\cdot3\cdot11,
\qquad
651=3\cdot7\cdot31.
\]

Their exponent rows on $(2,3,7,11,31)$ are

\[
(1,1,0,1,0),
\qquad
(0,1,1,0,1).
\]

They are independent modulo $2$, so the two-occurrence old parity decoder
has no nonzero dependency. The cross choice gives

\[
g=2\cdot7=14<65,
\qquad
14^2=196=1+3\cdot65,
\]

and hence factors $13$ and $5$. The aggregate quotient check is also
exact:

\[
\frac{66\cdot651-1}{65}=661\equiv3\pmod {14}.
\]

The selected constituents each have order $12$, with

\[
2^6\equiv7^6\equiv-1\pmod {65}.
\]

Their direct one-block screens are trivial. The correction now limits the
comparison to these two selected blocks. It expressly records that
$3^6\equiv14\pmod {65}$, and that $11$ and $31$ also have useful
half-order residues. It also acknowledges that the manufactured product
$14$ itself has order $2$. There is no remaining claim that all one-block
tests on the complete list fail.

The partial pair selector has the stated polynomial scope. On an explicit
polynomial-bit transcript, gcd-free refinement is polynomial, there are only
$O(s^2)$ block pairs, occurrence and capacity certificates are explicit,
and integer products are retained only below $N$. The artifact claims
success on this witness only, not on every input.

### The $N=187$ finite-box witness

The single relation is

\[
188=2\cdot94=2^2\cdot47.
\]

The box $0\le v\le(2,1)$ has exactly four proper legal products:

\[
2,\ 4,\ 47,\ 94.
\]

Their adjacent integers are respectively

\[
(1,3),\ (3,5),\ (46,48),\ (93,95).
\]

None has a factor $11$ or $17$, so every direct screen against
$187=11\cdot17$ is trivial.

On the other hand, $2^5\equiv-1\pmod {11}$, so the order modulo $11$ is
$10$. Also $2^4\equiv-1\pmod {17}$, so the order modulo $17$ is $8$.
Therefore

\[
\operatorname{ord}_{187}(2)=\operatorname{lcm}(10,8)=40.
\]

At the half order,

\[
2^{20}\equiv1\pmod {11},
\qquad
2^{20}\equiv-1\pmod {17}.
\]

This is a strict separation even for the full direct screen: the unbounded
generated subgroup has a non-global involution, while the finite one-copy box
has no direct separator of any kind. The failed $N=21$ comparator has been
fully replaced.

## 6. Exact self-inverse total-multiplicity hierarchy

For odd $t\ge3$, put

\[
G=2^t,
\qquad
N=\frac{G^2-1}{3},
\qquad
B=\frac{N+1}{2}.
\]

The relation $2B=N+1$ has coprime block types $2$ and $B$. If fewer
than $t$ explicit occurrences are selected, every legal divisor below
$N$ is either $B$ or $2^a$ with $1\le a<t$: a product containing
both blocks is at least $2B=N+1$, and $B^2>N$.

Neither type is self-inverse. From $2B\equiv1\pmod N$, the condition
$B^2\equiv1$ would imply $4\equiv1\pmod N$, impossible because $N>3$.
For $a<t$,

\[
0<2^{2a}-1<N,
\]

so $2^{2a}\not\equiv1\pmod N$.

With $t$ occurrences, $G<N$ and

\[
G^2=1+3N.
\]

Because $t$ is odd,

\[
N=(G-1)\frac{G+1}{3},
\]

where the two factors are coprime and proper. The residue $G$ has opposite
signs on them, so it is non-global. Every old-decoder dependency uses an even
number of identical rows and maps to a power of $N+1\equiv1$, so the old
image remains global.

The exact-order argument also closes. Modulo $G-1=2^t-1$, the order of
$2$ is exactly $t$, since no smaller positive $d<t$ can make
$2^d-1$ a positive multiple of $2^t-1$. Hence $t$ divides the order
modulo $N$. The relation $2^{2t}\equiv1\pmod N$ makes that order divide
$2t$, while $2^t\not\equiv1\pmod N$. Therefore

\[
\operatorname{ord}_N(2)=2t.
\]

The hierarchy is now named and scoped correctly. It lower-bounds total
selected occurrence multiplicity for a legal self-inverse divisor. It does
not lower-bound support: the winning vector has support one. It also does not
lower-bound the full direct screen. The artifact itself gives the $t=9$,
$g=8$ counterexample, where $7=g-1$ divides $N$ at multiplicity three.

Finally, $t=\Theta(\log N)$. Listing $t$ explicit copies, their rows, and
their relation values has polynomial total encoding. The hierarchy does not
hide an exponentially long source transcript.

## 7. Smith normal form and HSP wording

The kernel $\Lambda_N$ is full rank because every public generator has
finite order. If a basis is supplied, Smith normal form gives

\[
H=\mathbb Z^s/\Lambda_N
\cong\langle q_1,\ldots,q_s\rangle.
\]

For each even invariant factor $d_i$, multiplying its cyclic generator by
$d_i/2$ gives the unique order-two element in that cyclic factor. These
elements form an $\mathbb F_2$-basis of $H[2]$. The corrected artifact no
longer says to halve a group generator.

At most one nonzero element of $H[2]$ can be the ambient global residue
$-1$. If $H$ contains any non-global involution, then either its
2-torsion rank is one and the sole basis element is non-global, or its rank is
at least two and at least one basis element differs from $-1$. Screening at
most $s$ basis elements is therefore sufficient for the unbounded subgroup
target. No exponential enumeration of $H[2]$ is needed.

The transformed exponent representatives can be negative. The artifact uses
them only for modular products through inverses. It does not promote them to
positive legal divisors.

The HSP statement is now deliberately algebraic: output equality is exactly
coset equality modulo $\Lambda_N$. It does not claim that this identity is a
complete efficient quantum algorithm on the infinite domain
$\mathbb Z^s$. It lists the missing finite-domain, truncation, precision,
circuit, and success analyses.

The supplied-basis postprocessing claim is also input/output sensitive in the
right variables. It charges the encodings of $N$, the generators, the
lattice basis, Smith transformation data, and resulting exponent vectors.
Exact integer Smith algorithms and signed modular exponentiation are
polynomial in these bit lengths. The artifact makes no polynomial claim for
recovering the basis itself; the one-generator case already contains exact
order finding.

## 8. Prime powers, preprocessing, and final complexity scope

For an odd prime power $p^k$, the only square roots of one are the two
global signs. The corrected result does not demand a non-global involution on
that class. Its all-input theorem template first handles primality, even
inputs, and perfect powers in polynomial time. A remaining odd composite
that is not a perfect power has at least two distinct prime factors, so the
square-root subtarget is no longer impossible for this elementary reason.

The final target is split into two non-equivalent goals:

1. find any legal direct $g\pm1$ separator; or
2. find a legal bounded non-global involution.

The second is sufficient for the first and is the exact hidden-lattice
subproblem. It is not asserted to be necessary. No all-input selector for
either goal is claimed.

The polynomial-time checklist now charges all relevant data: occurrence and
block counts, complete relation and exponent encodings, finite capacities,
candidate count and exponent-vector sizes, adaptive rounds, random bits, and
all refinement, multiplication, modular, and gcd work. It also requires a
deterministic success theorem or inverse-polynomial randomized success with
Las Vegas verification on every remaining input. This repairs the earlier
candidate-count-only wording.

## 9. Repair ledger for the failed audit

Every required correction is present:

1. Full CRT-separator screening is separated from self-inverse 2-torsion.
2. Source occurrences and row-type capacities are finite and charged.
3. The old-decoder theorem remains a residue-image theorem only.
4. Quotient novelty separately requires a source-box representative and
   integer magnitude.
5. Least-power/order equivalence has the even-order promise and the explicit
   total-oracle $-a$ reduction.
6. The $N=65$ comparison is limited to blocks $2$ and $7$, with the
   successful other blocks disclosed.
7. The odd-$t$ family is a self-inverse total-multiplicity hierarchy, not a
   support or full-screen lower bound.
8. Smith postprocessing multiplies an invariant generator by $d_i/2$.
9. The invalid $N=21$ finite-box separation is replaced by the strict
   $N=187$ witness.
10. Prime, even, perfect-power, transcript-size, exponent-size, randomness,
    and adaptive-round scope is explicit.

The corrected conclusion is therefore promotion-ready at its stated narrow
scope.
