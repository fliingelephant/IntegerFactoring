# F68 — root-labelled feedback closure

**Status:** candidate proof-only theorem. No research computation was run.

**Closest prior results:** P66 gives the complete factor-free decoder and its
root homomorphism. P73 gives the exact square-class closure criterion for an
appended feedback relation.

**Material difference:** P73 counts new dependencies but does not identify
the new factor-bearing root direction. This result describes that direction,
proves that its label is canonical modulo the old root image, and shows that
after an unsuccessful complete old decode exactly one new root test is both
necessary and sufficient at each closure.

**Kill-first boundary:** closure alone cannot imply a factor. At any odd
$N$, appending a second indexed copy of $N+1$ closes the duplicate columns,
but their exact product has positive root $N+1\equiv1\pmod N$. The theorem
must therefore keep square-class closure and root usefulness as separate
conditions.

## 1. Setup

Let $N>1$ be odd. Let

\[
A_1,\ldots,A_m
\]

be indexed positive integers with $A_i\equiv1\pmod N$. Complete gcd-free
refinement represents their rational square classes by

\[
M\in\mathbb F_2^{r\times m}.
\]

Thus

\[
K=\ker M
\]

is exactly the indexed subset-square relation space. For $x\in K$, define

\[
Q(x)=\prod_i A_i^{x_i}=R(x)^2,
\]

where $R(x)>0$ is the exact integer square root, and put

\[
\psi(x)=R(x)\bmod N.
\]

Since every $A_i\equiv1\pmod N$, every $\psi(x)$ is a square root of one
modulo $N$.

Append one indexed feedback relation

\[
A_{m+1}=gw\equiv1\pmod N.
\]

Jointly refine the old and new values. Write the refined parity matrix as
$[M\mid b]$; refinement preserves the old kernel.

## 2. The old root map is a homomorphism

### Lemma 1

The map

\[
\psi:K\longrightarrow\mu_2(N)
\]

is a group homomorphism, where $K$ is additive and
$\mu_2(N)=\{z\in(\mathbb Z/N\mathbb Z)^\times:z^2=1\}$ is multiplicative.

### Proof

For $x,y\in K$, binary addition cancels every index selected twice. Exact
positive roots therefore satisfy

\[
R(x)R(y)
=R(x+y)\prod_{i:x_i=y_i=1}A_i.
\]

The last product is $1$ modulo $N$. Hence

\[
\psi(x)\psi(y)=\psi(x+y).
\]

$\square$

Let

\[
H=\psi(K)\le\mu_2(N)
\]

be the complete old root image.

## 3. A closure has one canonical new root coset

### Theorem 2

If $b\notin\operatorname{colspan}(M)$, the appended list has no new square
dependency: its kernel is $K\times\{0\}$.

If $b\in\operatorname{colspan}(M)$, choose any $c\in\mathbb F_2^m$ with

\[
Mc=b
\]

and define the closure vector

\[
z_c=(c,1).
\]

Then

\[
K'=\ker[M\mid b]
=(K\times\{0\})\oplus\langle z_c\rangle.
\]

Its new root label is

\[
s_c
=\sqrt{A_{m+1}\prod_iA_i^{c_i}}\pmod N
\in\mu_2(N).
\]

Although $s_c$ can depend on the chosen solution $c$, its coset

\[
s_cH\in\mu_2(N)/H
\]

does not. The full new root image is

\[
H'=\langle H,s_c\rangle.
\]

### Proof

If a vector in the new kernel has last coordinate one, its first $m$
coordinates solve $Mx=b$. Thus no such vector exists when $b$ is outside the
old column span, and the kernel is unchanged.

Suppose $Mc=b$. The vector $z_c$ is in the new kernel. Every new kernel vector
with last coordinate zero lies in $K\times\{0\}$. If $(d,1)$ is in the new
kernel, then

\[
M(d+c)=b+b=0,
\]

so $(d,1)=z_c+(d+c,0)$ with $d+c\in K$. The last coordinate also shows that
$z_c$ is not in $K\times\{0\}$. This proves the direct-sum formula.

The appended list has the same root homomorphism as Lemma 1. Therefore the
direct-sum generators give $H'=\langle H,s_c\rangle$. If $c'$ is another
solution, then $c'+c\in K$, and

\[
s_{c'}=s_c\,\psi(c'+c).
\]

The multiplier lies in $H$, so $s_{c'}H=s_cH$. $\square$

The quotient label is the exact information added by one closure. It is more
precise than choosing an arbitrary dependency root, whose literal residue can
change when an old dependency is added to it.

## 4. Exact two-gate criterion after an unsuccessful decode

Let

\[
G=\{1,-1\}\le\mu_2(N)
\]

be the global-sign subgroup.

### Theorem 3

Suppose a basis of the old kernel $K$ has been completely screened and no
proper factor was found from either sign of any basis root. Then

\[
H\subseteq G.
\]

At the next append:

1. if $b\notin\operatorname{colspan}(M)$, there is no new decoder output;
2. if $b\in\operatorname{colspan}(M)$, compute one solution $Mc=b$ and its
   induced root $s_c$;
3. the enlarged complete decoder finds a factor if and only if
   $s_c\notin G$.

In the closure case, the class

\[
[s_c]\in\mu_2(N)/G
\]

is independent of the chosen solution $c$. Hence one induced root test,
together with the already screened old basis, is complete.

### Proof

For an odd modulus, a square root of one is either a global sign or has a
nontrivial CRT sign split. In the latter case both

\[
\gcd(r-1,N),\qquad\gcd(r+1,N)
\]

are proper. Thus failure on every old basis root means that every basis image
lies in $G$. Lemma 1 then gives $H\subseteq G$.

The no-closure case follows from Theorem 2. In the closure case,
$H'=\langle H,s_c\rangle$. If $s_c\in G$, then $H'\subseteq G$ and every new
dependency root is global. If $s_c\notin G$, the closure vector itself has a
non-global root and its two sign gcds expose proper factors. Since changing
$c$ multiplies $s_c$ by an element of $H\subseteq G$, global versus
non-global status is independent of the lift. $\square$

## 5. Finite witnesses

### Closure without usefulness

For $N=21$, take one old value $A_1=22=N+1$ and append an indexed duplicate
$A_2=22$. Their parity columns are equal, so $c=(1)$ closes the new column.
The induced exact square is

\[
A_1A_2=22^2,
\]

whose positive root is $22\equiv1\pmod{21}$. The closure is a global-root
decoy.

### Useful zero-column closure

For $N=55$, the canonical self-inverse state $g=w=21$ gives

\[
A_{m+1}=21^2.
\]

Its parity column is zero, so $c=0$ is a closure lift and the induced root is
$s_c=21$. It is non-global because

\[
\gcd(21-1,55)=5,
\qquad
\gcd(21+1,55)=11.
\]

## 6. Consequence and scope

A cross-feedback round now has two exact gates:

1. **square-class gate:** $b$ must close in the old span;
2. **root-sign gate:** its canonical quotient label must be non-global.

This removes an ambiguity in the selector objective. Optimizing only the
number of relations, the number of blocks, rank deficiency, or closure
frequency can still generate only global-root decoys. Conversely, after the
old complete decoder has failed, a useful closure needs only one new induced
root test; no exponential enumeration of the enlarged kernel is required.

The theorem gives exact incremental decoding. It supplies no distribution for
either gate, no method that makes the root label factor-correlated, and no
polynomial-time factoring algorithm. The unresolved source problem is to
produce, from bare $N$, polynomially many legal feedback additions for which
both gates occur with an inverse-polynomial all-input probability.
