# Hostile audit of F201

## Verdict

**PASS.** All four supplied frozen hashes match. I found no false inequality,
endpoint error, support error, quotient or remainder error, size error, gamma
error, axes error, or recursion overclaim. The result is valid only in its
declared narrow scope: the unresolved paired node, the ordinary first
Euclidean remainder, explicit integer materialization, and fixed public
linear forms. It is not a lower bound for implicit product evaluation,
adaptive nonlinear selectors, later Euclidean remainders, or factoring.

## 1. Frozen integrity

I computed the hashes before reading any packet file. The observed values
are exactly the expected values:

- `STATEMENT.md`:
  `4915cbeea9e258524ece5dcf21e115f1a6c8ef0775dd0d1b926b94cdcbda8d41`;
- `PROOF.md`:
  `56dce149bdd39b545b35e695108aa8a1dd3fa0bb8cc891aaf437a95d03e82e17`;
- `SELF_AUDIT.md`:
  `ca4dce01e8a1e1ed257ef560394f9151400e4da1d2f1d7975351c2fb188a72ab`;
- observed `MANIFEST.md`:
  `c1d056d40162be671f7bc0092a8cfb7b628edf2c91fd2e8590e4bde8e6a37193`.

## 2. Balanced interval and prefix interface

The endpoint derivation is exact. Since $p<q$,

\[
p^2<pq<q^2,
\]

so $p<\sqrt N<q$, hence $p\le B<q$. Since $B<q<2p$ and all
quantities are integers,

\[
B\le q-1\le 2p-2.
\]

Therefore

\[
\left\lceil\frac B2\right\rceil\le p-1<p,
\]

which puts $p$ inside the half-open interval $I_B$. Also $q>B$ and
$2p>B$. Every element of $I_B$ is positive and below both $q$ and
$2p$. Thus its only possible positive multiple of either hidden prime is
the single integer $p$. This proves the claimed uniqueness, including the
cases $p=B$ and $B=2p-2$.

For $m=2^t$, $t\ge1$, every relevant residue is odd and is a unit modulo
both $m$ and $2m$. Reduction modulo $m$ commutes with inversion. The
two odd lifts of a reciprocal residue modulo $m$ are permuted by inversion
into the two lifts of $p\bmod m$ modulo $2m$. Listing a parent as
$x_j=c+mj$ identifies these two lifts with even and odd $j$. This uses
no knowledge of which lift is correct.

## 3. Unequal children, cleanup, endpoints, and product support

If $L=2s+1$, the even-index child has $s+1$ entries and the odd-index
child has $s$. Its only unpaired entry is the public upper endpoint
$x_{2s}$. Interval uniqueness gives

\[
\gcd(N,x_{2s})=p\quad\Longleftrightarrow\quad x_{2s}=p,
\]

and otherwise the gcd is one. In the first case the computation has already
factored $N$. In the second case, deleting the upper endpoint preserves
$p$ and leaves the consecutive AP $x_0,\ldots,x_{2s-1}$. If $L=1$,
the sole entry must be $p$, so every unresolved paired node has $s\ge1$.

After cleanup, both children have $s$ entries. Direct substitution gives

\[
e_i=c+2mi,
\qquad
o_i=e_i+m,
\qquad
e_{i+1}=o_i+m.
\]

Thus

\[
\left\lceil\frac B2\right\rceil<e_i<o_i\le B,
\qquad
e_i<o_i<e_{i+1}.
\]

Exactly one child contains the unique term $p$. Primality implies that
exactly one of $E,O$ is divisible by $p$. No term can be divisible by
$q$, because every term is positive and below $q$. No other term can be
divisible by $p$, because every term is below $2p$. Hence

\[
\{\gcd(E,N),\gcd(O,N)\}=\{1,p\}.
\]

Computing either product modulo $N$, followed by its gcd with $N$,
therefore selects the correct parity child. The theorem does not provide
that modular-product computation.

Explicit endpoint probes agree with the proof:

- $p=11,q=13,B=11,m=2$ gives the cell $[7,9,11]$. The extra endpoint
  is $p=B$, so its gcd terminates with a factor.
- $p=11,q=17,B=13,m=2$ gives $[9,11,13]$. Before cleanup the children
  are $[9,13]$ and $[11]$. The endpoint $13$ has gcd one, and cleanup
  leaves the paired children $[9]$ and $[11]$.
- $p=7,q=13,B=9,m=2$ gives $[7,9]$, with $p$ at the lower parent
  endpoint. $p=7,q=11,B=8,m=2$ gives $[5,7]$, with $p$ at the upper
  parent endpoint. Both orientations satisfy the same support claims.

## 4. Interlacing, quotient, both support orientations, and reverse division

Termwise comparison gives $O>E$. For $s\ge2$, interlacing gives

\[
\prod_{i=0}^{s-2}o_i<\prod_{i=1}^{s-1}e_i.
\]

Therefore

\[
\frac OE
=\frac{o_{s-1}}{e_0}
  \frac{\prod_{i=0}^{s-2}o_i}{\prod_{i=1}^{s-1}e_i}
<\frac{o_{s-1}}{e_0}
<\frac{B}{B/2}=2.
\]

For $s=1$, the middle comparison is equality because both omitted
products are empty, while $o_0/e_0<2$ still follows from
$o_0\le B$ and $e_0>B/2$. Thus in every unresolved case

\[
1<\frac OE<2.
\]

The ordinary Euclidean quotient of $O$ by $E$ is exactly one, and

\[
O=E+D,
\qquad
D=O-E,
\qquad
0<D<E.
\]

Both hidden-factor orientations were checked separately. If $p\mid E$,
then $D\equiv O\not\equiv0\pmod p$. If $p\mid O$, then
$D\equiv-E\not\equiv0\pmod p$. Hence $p\nmid D$ without an orientation
assumption.

There is no analogous conclusion modulo $q$. A concrete full-cell
counterexample is

\[
p=19,quad q=29,quad B=23,quad m=2,
\]

with paired cell

\[
[13,15,17,19,21,23].
\]

Here

\[
E=13\cdot17\cdot21=4641,
\qquad
O=15\cdot19\cdot23=6555,
\]

and

\[
D=1914=66\cdot29,
\qquad
\gcd(D,N)=29.
\]

This confirms that accidental $q$-support is real, not only a logical
possibility. The packet states the correct weaker result.

Reversing the two original operands means dividing $E$ by $O$. Since
$0<E<O$, its quotient is zero and its remainder is the unchanged integer
$E$. This operation does not produce a smaller auxiliary. The claim does
not cover the later division $E\bmod D$, and it must not be read as a
claim about a complete Euclidean remainder chain.

## 5. Rising factorial and gamma identity

Let

\[
z=\frac{c}{2m},
\qquad
w=\frac{c+m}{2m}.
\]

Then factor by factor,

\[
(2m)^s(z)_s
=\prod_{i=0}^{s-1}(c+2mi)=E,
\]

and

\[
(2m)^s(w)_s
=\prod_{i=0}^{s-1}(c+m+2mi)=O.
\]

All gamma arguments are positive, so there are no poles. Applying
$(u)_s=\Gamma(u+s)/\Gamma(u)$ and cancelling $(2m)^s$ gives exactly

\[
\frac OE=
\frac{\Gamma(w+s)\Gamma(z)}
     {\Gamma(w)\Gamma(z+s)}.
\]

This is an identity for the same ordered integer pair. It does not turn a
floating-point gamma approximation into an exact Euclidean computation,
and the packet makes no such claim.

## 6. Positive expansion and explicit bit size

Expanding

\[
D=\prod_{i=0}^{s-1}(e_i+m)-\prod_{i=0}^{s-1}e_i
\]

leaves one positive term for every nonempty choice of factors from which
$m$ is selected. Keeping only the term that selects $m$ at index zero
gives

\[
D\ge m\prod_{i=1}^{s-1}e_i
   \ge m(B/2)^{s-1}.
\]

For $s\ge2$, every $e_i>B/2$, so the final bound is strict. For
$s=1$, both products are empty and $D=m$, so equality is exact. Since
$\operatorname{bitlen}(D)=\lfloor\log_2D\rfloor+1>\log_2D$,

\[
\operatorname{bitlen}(D)>
\log_2m+(s-1)(\log_2B-1).
\]

The interval has exactly

\[
B-\left\lceil\frac B2\right\rceil
=\left\lfloor\frac B2\right\rfloor=:K
\]

integers. A residue class modulo $m$ occurs $K/m+\delta_0$ times with
$|\delta_0|<1$. Along any unresolved cleaned child chain,

\[
L_{r+1}=\left\lfloor\frac{L_r}{2}\right\rfloor,
\qquad
m_{r+1}=2m_r.
\]

Writing $L_r=K/m_r+\delta_r$ gives
$\delta_{r+1}=\delta_r/2-\varepsilon_r$, where
$0\le\varepsilon_r<1$. In particular, $-2<\delta_r<1$ uniformly.
This proves, with a depth-independent error,

\[
L=\frac{K}{m}+O(1),
\qquad
s=\left\lfloor\frac L2\right\rfloor
 =\frac{B}{4m}+O(1).
\]

At the P175 schedule,

\[
m=2^{\lfloor(\log_2N)/4\rfloor-L_0(n)}
 =\Theta\!\left(N^{1/4}2^{-L_0(n)}\right),
\qquad
B=\Theta(N^{1/2}).
\]

Thus

\[
s=\Theta\!\left(N^{1/4}2^{L_0(n)}\right).
\]

Because $L_0(n)$ is a fixed polylogarithm, $L_0(n)=o(n)$, while
$\log_2N=\Theta(n)$. Hence $s=2^{\Theta(n)}$. The displayed lower
bound gives a $2^{\Theta(n)}$ bit-length lower bound. The upper bound
$D<O\le B^s$ gives the same class. Therefore

\[
\operatorname{bitlen}(D)=2^{\Theta(n)}.
\]

The reverse remainder satisfies

\[
E=\prod e_i>(B/2)^s,
\]

and $E\le B^s$, so it has the same explicit bit-length class at this
schedule.

Large $m$ creates no counterexample. For example,
$p=263,q=269,B=265,m=128$ gives the two-entry full cell
$[135,263]$, with $O/E=263/135<2$ and $D=128<135$. If $m>B$, a
correct full cell has only $[p]$, so the public endpoint gcd terminates.
The exponential statement concerns an unresolved node at the P175
schedule, where $m\ll B$, not an arbitrary short AP or a terminal node.

## 7. Linear axes and coefficient screening

Modulo $p$, if $p\mid E$ then $O$ is nonzero and

\[
F_{\alpha,\beta}\equiv\beta O\pmod p.
\]

Thus $p\mid F_{\alpha,\beta}$ exactly when $p\mid\beta$. On the other
axis, if $p\mid O$, then

\[
F_{\alpha,\beta}\equiv\alpha E\pmod p,
\]

so divisibility is equivalent to $p\mid\alpha$. Retaining $p$-support
for both possible orientations therefore requires $p$ to divide both
coefficients.

For a squarefree semiprime, the gcd of a public coefficient with $N$ is
one of $1,p,q,N$. A value $p$ or $q$ is already a factor. A value
$N$ means that the coefficient contributes zero modulo $N$. If both
coefficients are multiples of $N$, the form is the trivial zero. If both
are units modulo $N$, neither is zero modulo $p$, so neither axis has
guaranteed $p$-support. As before, reduction modulo $q$ is uncontrolled.
The conclusion is only about fixed public linear combinations.

## 8. Product identity, recursion, and surviving openings

After cleanup, $S'$ is the disjoint union of its even and odd children.
Therefore

\[
\prod_{J\in S'}J=EO
\]

exactly. A QP method that selects the factor-bearing child can follow one
child per lift. P175 starts at a quarter-minus-polylog precision, and at
most $O(n)$ one-bit lifts reach enough precision. Multiplying a QP
per-stage cost by $O(n)$ preserves QP. The same point applies to

\[
T(n)\le T(n-1)+\operatorname{QP}(n):
\]

iteration over at most $n$ sizes remains QP. A fixed-ratio contraction is
not necessary.

Nothing here constructs that selector. Nothing rules out a succinct
modular AP-product evaluator, an adaptive nonlinear or target-correlated
statistic, a nonlocal floor or carry, a later Euclidean remainder, or a
different one-child auxiliary. The proof establishes an explicit
same-node boundary, not a factoring lower bound.

## 9. Finite adversarial sweep

As corroboration, not proof, I exhaustively enumerated all 1,252 balanced
odd-prime pairs $p<q<2p$ with $p,q\le400$, every power-of-two modulus
$m=2^t$ with $1\le t\le\operatorname{bitlen}(B)+2$, and every consecutive
parent subcell containing $p$. The sweep checked 985,772 parents: 929,231
unresolved paired cases and 56,541 public endpoint terminals. It found no
violation of an endpoint, interlacing, quotient, support, reverse-division,
or exact expansion inequality. It found 3,144 cases with $q\mid D$,
including the explicit example above.

A separate exact chain sweep checked 12,617 full-cell starts and 16,535
correct-child lift steps. It verified the uniform bound

\[
-2<L-\frac{\lfloor B/2\rfloor}{m}<1
\]

at every visited node. These computations support the elementary proof but
are not used as premises for the verdict.
