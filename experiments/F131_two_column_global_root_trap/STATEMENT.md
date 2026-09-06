# F131 statement — two-column global-root trap

## Status and purpose

This is a proof-only candidate. It refutes one proposed auxiliary statement for
the F26-Q retained-relation route. It is not a counterexample to the complete
F26-Q source or decoder.

Let $N>1$ be odd and composite. For a canonical unit endpoint
$c\in\{1,\ldots,N-1\}$, let

\[
w=[c^{-1}]_N\in\{1,\ldots,N-1\},
\qquad
P=cw=1+kN.
\]

An endpoint sign screen is *nonproper* when

\[
\gcd(c-w,N),\ \gcd(c+w,N)\in\{1,N\}.
\]

## False auxiliary statement

The following statement is false:

> If two distinct canonical exact values $P_1,P_2>1$ have square product
> and all four endpoint sign screens are nonproper, then the exact square root
> of $P_1P_2$ is non-global modulo $N$.

It remains false if all four endpoint gcds are required to equal $1$, and if
both individual exact values are required to be nonsquares.

## Sharp two-column classification

Let

\[
P_i=c_iw_i=1+k_iN>1,
\qquad i\in\{1,2\},
\]

be distinct canonical exact values, and suppose $P_1P_2=R^2$, where
$R>0$. There are unique positive integers $a,b$ and one squarefree positive
integer $s$ such that

\[
P_1=sa^2,
\qquad
P_2=sb^2,
\qquad
R=sab.
\]

Then

\[
R\equiv 1\pmod N
\quad\Longleftrightarrow\quad
a=b,
\]

and

\[
R\equiv -1\pmod N
\quad\Longleftrightarrow\quad
a+b=N.
\]

Since $P_1\ne P_2$, the first case cannot occur. Therefore

\[
\boxed{
R\text{ is global modulo }N
\quad\Longleftrightarrow\quad
a+b=N,
}
\]

and every global root in the distinct-value case is $-1\pmod N$.

The canonical endpoint bounds imply $a,b<N/\sqrt{s}$. Consequently,

\[
a+b=N\quad\Longrightarrow\quad s<4.
\]

Thus only $s\in\{1,2,3\}$ can give a global two-column root. In particular,

\[
\boxed{s\ge5\quad\Longrightarrow\quad R\not\equiv\pm1\pmod N.}
\]

No endpoint-screen hypothesis is used in this classification.

## Strict finite certificate

Take

\[
N=9407=23\cdot409
\]

and the two canonical inverse pairs

\[
(c_1,w_1)=(9025,4802),
\qquad
(c_2,w_2)=(6534,6912).
\]

Their exact values are

\[
\begin{aligned}
P_1&=9025\cdot4802
     =43\,338\,050
     =1+4607N
     =2\cdot4655^2,\\
P_2&=6534\cdot6912
     =45\,163\,008
     =1+4801N
     =2\cdot4752^2.
\end{aligned}
\]

All four endpoint screens equal $1$:

\[
\begin{aligned}
\gcd(9025-4802,N)&=\gcd(4223,N)=1,\\
\gcd(9025+4802,N)&=\gcd(13827,N)=1,\\
\gcd(6534-6912,N)&=\gcd(-378,N)=1,\\
\gcd(6534+6912,N)&=\gcd(13446,N)=1.
\end{aligned}
\]

However,

\[
R=2\cdot4655\cdot4752
 =44\,241\,120
 =4703N-1.
\]

Hence $P_1P_2=R^2$ but $R\equiv-1\pmod N$. Each $P_i$ has squarefree
kernel $2$, so neither exact value is an individual square.

## Unconditional infinite nonsquarefree family

Put

\[
C=119\cdot17\cdot4559\cdot5233,
\qquad
M=6\cdot529\cdot C,
\]

and, for every integer $m\ge0$, define

\[
t=373+mM,
\qquad
N=t^2-2.
\]

Set

\[
a={N-t\over2}={(t-2)(t+1)\over2},
\qquad
b={N+t\over2}={(t+2)(t-1)\over2},
\]

and

\[
\begin{aligned}
c_1&=(t-2)^2,
&w_1&={(t+1)^2\over2},\\
c_2&={2(t+2)^2\over3},
&w_2&={3(t-1)^2\over4}.
\end{aligned}
\]

For every $m\ge0$:

1. $N$ is an odd nonsquarefree composite and $23^2\mid N$.
2. All four endpoints are integers in $\{1,\ldots,N-1\}$.
3. The pairs are canonical inverse pairs and

   \[
   c_1w_1=2a^2=1+{N-2t+1\over2}N,
   \qquad
   c_2w_2=2b^2=1+{N+2t+1\over2}N.
   \]

4. Both exact values are distinct nonsquares with common squarefree kernel
   $2$.
5. All four endpoint sign gcds equal $1$.
6. Their joint exact root is global:

   \[
   \sqrt{(c_1w_1)(c_2w_2)}
   =2ab
   ={N(N-1)\over2}-1
   \equiv-1\pmod N.
   \]

The first member, $m=0$, is the exact nonsquarefree certificate

\[
N=139127=23^2\cdot263.
\]

## Scope

The infinite family has the fixed visible divisor $23^2$. It makes no claim
about balanced semiprimes, trial-hard inputs, or the success density of F26-Q.
It proves only that exact two-column closure and endpoint-screen failure do not
determine the normalized-root label. Other retained columns or dependencies
can still factor the same input.
