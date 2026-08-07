# Proof-blind statement — root-labelled feedback closure

Reconstruct or refute all claims below from this file only. Do not read the
candidate, its audit, any ledgers, or prior proof records. Give a
self-contained PASS/FAIL verdict, and identify every needed hypothesis.

## Setup

Let $N>1$ be odd. Let $A_1,\ldots,A_m$ be indexed positive integers with

\[
A_i\equiv1\pmod N.
\]

After complete exact gcd-free refinement, let

\[
M\in\mathbb F_2^{r\times m}
\]

represent their rational square classes on pairwise-coprime nonsquare blocks,
and put $K=\ker M$. For $x\in K$, define

\[
Q(x)=\prod_iA_i^{x_i}=R(x)^2,
\qquad
\psi(x)=R(x)\pmod N,
\]

where $R(x)>0$ is the exact integer square root. Put

\[
\mu_2(N)=\{z\in(\mathbb Z/N\mathbb Z)^\times:z^2=1\},
\qquad H=\psi(K).
\]

Append a separate indexed positive value $A_{m+1}\equiv1\pmod N$. Jointly
refine all values. Write the new parity matrix as $[M\mid b]$; exact
refinement preserves the intrinsic old kernel.

## Claims

### 1. Positive-root homomorphism

The map

\[
\psi:K\to\mu_2(N)
\]

is a group homomorphism. For $x,y\in K$, the exact identity behind this is

\[
R(x)R(y)=R(x+y)\prod_{i:x_i=y_i=1}A_i.
\]

The hypothesis $A_i\equiv1\pmod N$ is essential for this literal root map.

### 2. One closure adds one root coset

If $b\notin\operatorname{colspan}(M)$, then

\[
\ker[M\mid b]=K\times\{0\};
\]

there is no new square-dependency direction.

If $b\in\operatorname{colspan}(M)$, choose any
$c\in\mathbb F_2^m$ with $Mc=b$ and put $z_c=(c,1)$. Then

\[
K'=\ker[M\mid b]
=(K\times\{0\})\oplus\langle z_c\rangle.
\]

Define

\[
s_c=sqrt{A_{m+1}\prod_iA_i^{c_i}}\pmod N.
\]

The new complete root image is

\[
H'=\langle H,s_c\rangle.
\]

If $c'$ is another solution, then $c'+c\in K$ and

\[
s_{c'}=s_c\psi(c'+c).
\]

Thus the literal root can depend on the lift, but the coset

\[
s_cH\in\mu_2(N)/H
\]

is canonical.

### 3. One new test is complete after an unsuccessful old decode

Let $G=\{1,-1\}\le\mu_2(N)$. Suppose that both sign gcds of every vector in
one basis of $K$ have been tested and no proper factor was found. Then

\[
H\subseteq G.
\]

For the next append:

- if $b$ is outside the old column span, there is no new decoder output;
- if $b$ closes, compute any one solution $Mc=b$ and the induced root $s_c$;
- the enlarged complete decoder has a factor-bearing dependency if and only
  if $s_c\notin G$.

In the closure case, $s_cG\in\mu_2(N)/G$ is independent of the chosen lift.
Testing this one induced root, together with the already screened old basis,
is complete. The statement is about the two sign gcd screens on exact-root
labels; it does not exclude unrelated factoring routes.

Prove the inference for arbitrary odd $N$, including nonsquarefree inputs.

### 4. Indexed semantics and finite boundaries

Equal relation values count as two columns only if the algorithm appends two
separate indices. Deduplication creates no second coordinate.

For $N=21$, an old value $22$ and an indexed duplicate $22$ close, but the
induced exact root is $22\equiv1\pmod{21}$, so the new dependency is a global
decoy.

For $N=55$, appending $21^2$ gives a zero column. The lift $c=0$ has induced
root $21$, and

\[
\gcd(20,55)=5,
\qquad
\gcd(22,55)=11.
\]

Thus closure and factor usefulness are separate gates.

## Scope

The result is exact incremental decoding. It gives no distribution for
closure, no factor-correlation law for the induced root, no feedback selector,
and no factoring algorithm. Exact square roots and linear solves are measured
in the total explicit input length; the result does not promise that a
feedback process keeps that length polynomial in $\log N$.
