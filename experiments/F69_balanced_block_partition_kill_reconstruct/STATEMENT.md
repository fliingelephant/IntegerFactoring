# Proof-blind statement — balanced-block partition boundary

Reconstruct or refute every claim below from this file only. Do not read the
candidate, its audit, any ledgers, or prior proof records. Give a
self-contained PASS/FAIL verdict with all necessary scope. Do not use
computational search as proof.

## Setup

Let $N\ge3$ be odd and let

\[
A=1+kN=\prod_{j=1}^s q_j^{E_j},
\]

where $q_j>1$ are public pairwise-coprime blocks, each coprime to $N$, and
the exponents are exact. For $0\le c_j\le E_j$, put

\[
g(c)=\prod_jq_j^{c_j},
\qquad
h(c)=\frac A{g(c)}.
\]

Call $c$ a balanced-canonical split if

\[
1<g(c)<N,
\qquad
1<h(c)<N.
\]

Then $h(c)$ is the canonical inverse of $g(c)$. Define

\[
\delta(c)=|g(c)-h(c)|,
\qquad
\beta(c)=\left|\log g(c)-\frac12\log A\right|.
\]

This model partitions whole current blocks. It does not factor a composite
block internally.

## Claims

### 1. Magnitude boundary

If a balanced-canonical split exists, then

\[
A\le(N-1)^2=1+(N-2)N,
\qquad k\le N-2.
\]

At equality, the only split is $g=h=N-1$, the global root.

If an aggregate

\[
P=\prod_{i\in S}(1+k_iN)
\]

contains at least two occurrences with $k_i\ge1$, then

\[
P\ge(N+1)^2>(N-1)^2.
\]

It has no complementary divisors both below $N$. For every divisor
$1<g<N$,

\[
\frac Pg\ge\frac{(N+1)^2}{N-1}
=N+3+\frac4{N-1}>N.
\]

Thus, after two relations are aggregated, ordinary number partition balances
$g$ against the oversized integer complement $P/g$. The canonical inverse is
instead

\[
w\equiv P/g\pmod N,
\qquad1\le w<N.
\]

The modular reduction is not controlled by the raw integer balance.

### 2. One-relation whole-block redundancy

For any balanced-canonical split of one already retained relation $A$:

1. the selected inverse relation is exactly the old value $gh=A$;
2. the endpoints use only the old whole blocks with exponent vectors $c$ and
   $E-c$, so complete joint gcd refinement introduces no new block and splits
   no old $q_j$;
3. its square-class column is the old column $E\bmod2$;
4. if it is appended as a second indexed copy, the duplicate dependency has
   positive root $A\equiv1\pmod N$, so it adds no new root class;
5. if direct and other public screens fail and occurrence capacity is fixed,
   the append is a no-op.

An algorithm can explicitly charge a duplicate as a new occurrence and gain
multiplicity. That is deliberate source amplification, not information
created by balance.

### 3. Log precision does not imply small additive distance

For $g\le h$ and

\[
\beta=\frac12\log(h/g),
\]

one has exactly

\[
g=\sqrt A e^{-\beta},
\qquad
h=\sqrt A e^\beta,
\qquad
\delta=2\sqrt A\sinh\beta.
\]

To guarantee $\delta\le D$ from a log-imbalance certificate alone requires

\[
\beta\le\operatorname{arsinh}\!\left(\frac D{2\sqrt A}\right).
\]

When $A=\Theta(N^2)$ and $D=\operatorname{poly}(\log N)$, this precision is
$2^{-\Omega(\log N)}$. An FPTAS polynomial in $1/\varepsilon$ is not
bit-polynomial at that requested additive scale. This is a precision
boundary, not an NP-hardness claim.

### 4. Exact counterexamples

For every odd composite $N$, the one-block relation

\[
A=(N-1)^2=1+(N-2)N
\]

has only the perfectly balanced split $g=h=N-1$. It is the global root and
all named gcd screens are trivial.

For

\[
N=209=11\cdot19,
\qquad
A=6480=1+31\cdot209=2^4 3^4 5,
\]

the unique closest unordered factor pair, even among all integer divisors, is

\[
80\cdot81=6480.
\]

It has distance one and survives the direct and discriminant screens. The
same block box contains the farther split

\[
45\cdot144=6480,
\]

and $\gcd(45-1,209)=11$. Hence exact closest-partition optimization is not
monotone toward a factor.

### 5. Infinite zero-useful-mass family

Let

\[
F(z)=z^2+z-1.
\]

For every positive multiple $t\ge5$ of $5$, put

\[
a=F(t)=t^2+t-1,
\qquad
b=F(t+1)=t^2+3t+1,
\qquad
N=ab.
\]

Then $a,b>1$ are odd, coprime, and asymptotically equal, and
$\gcd(N,5)=1$. Let $u\in\{0,\ldots,N-1\}$ be the CRT solution

\[
u\equiv t\pmod a,
\qquad
u\equiv t+1\pmod b.
\]

Prove all of the following:

- $F(u)=kN$ for an integer $k\ge1$;
- $2\le u\le N-3$;
- $A=u(u+1)=1+kN$ is a canonical inverse relation;
- with the two-block presentation $q_1=u,q_2=u+1,E=(1,1)$, the only
  admissible unordered balanced-canonical split is $\{u,u+1\}$;
- its distance is one;
- all four direct endpoint screens and the discriminant screen fail;
- $A$ is not an integer square;
- appending the same endpoint pair changes no value, block, or fixed
  occurrence box.

Therefore every distribution supported on the admissible splits of this box
has exactly zero useful mass. The finite $t=3$ instance gives
$N=11\cdot19=209$ and $u=80$, although it is outside the stated
$5\mid t$ subfamily.

## Scope

The result kills multiplicative balance as a universal factoring sampler,
even with a free exact optimizer. It does not deny a number-partition FPTAS,
rule out every block statistic, or give a general sampling lower bound.
Cross-relation feedback can still be useful through the canonical residue of
an oversized complement or through integer block refinement. Those require a
separate factor-correlation theorem.
