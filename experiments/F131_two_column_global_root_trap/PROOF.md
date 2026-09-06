# F131 proof — two-column global-root trap

## 1. Common squarefree kernel

Suppose $P_1P_2$ is an integer square. The parity of every prime valuation in
$P_1$ equals its parity in $P_2$. Hence $P_1$ and $P_2$ have the same
squarefree kernel $s$, and there are unique positive integers $a,b$ such
that

\[
P_1=sa^2,
\qquad
P_2=sb^2.
\]

The positive exact square root is

\[
R=sab.
\]

Each canonical endpoint is at most $N-1$, so

\[
P_i=c_iw_i\le(N-1)^2<N^2.
\]

It follows that

\[
0<a,b<{N\over\sqrt{s}}\le N.
\]

Also $P_i\equiv1\pmod N$, so $s,a,b$ are all units modulo $N$.

## 2. Exact classification of the root label

Since $sa^2\equiv1\pmod N$,

\[
R=sab
  \equiv (sa^2)ba^{-1}
  \equiv ba^{-1}
  \pmod N.
\]

Therefore

\[
R\equiv1\pmod N
\quad\Longleftrightarrow\quad
b\equiv a\pmod N.
\]

Both $a$ and $b$ lie strictly between $0$ and $N$. Thus this congruence
is equivalent to $a=b$, which is equivalent to $P_1=P_2$. The assumed
distinctness excludes the $+1$ root.

Similarly,

\[
R\equiv-1\pmod N
\quad\Longleftrightarrow\quad
b\equiv-a\pmod N.
\]

Here $0<a+b<2N$. Hence the last congruence is equivalent to the exact
integer equality

\[
a+b=N.
\]

This proves the sharp classification. If $a+b=N$, then

\[
N=a+b<{2N\over\sqrt{s}},
\]

so $\sqrt{s}<2$ and $s<4$. Since $s$ is squarefree, only
$s=1,2,3$ remain.

The endpoint screens do not occur anywhere in the argument. In the global
case, one also has

\[
\gcd(a,b)=\gcd(a,N)=1
\]

and therefore

\[
\gcd(P_1,P_2)=s.
\]

Allowing a global endpoint gcd does not repair the false auxiliary. For
example, self-pairs $c=w$ make the difference gcd equal to $N$. More
importantly, the strict certificates below have all four endpoint gcds equal
to $1$, so they do not use this degeneracy.

## 3. The \(N=9407\) certificate

The factorization is

\[
9407=23\cdot409.
\]

The endpoint products are

\[
\begin{aligned}
9025\cdot4802
 &=43\,338\,050
  =1+4607\cdot9407
  =2\cdot4655^2,\\
6534\cdot6912
 &=45\,163\,008
  =1+4801\cdot9407
  =2\cdot4752^2.
\end{aligned}
\]

Every endpoint lies in $\{1,\ldots,9406\}$. Each product is congruent to
$1\pmod N$. Thus every endpoint is a unit, and uniqueness of the inverse in
that interval shows that $w_i$ is the canonical inverse of $c_i$.

For the four sign values, reduction modulo the two prime factors gives

\[
\begin{array}{c|cc}
\text{absolute sign value}&\bmod 23&\bmod409\\ \hline
4223&14&133\\
13827&4&330\\
378&10&378\\
13446&14&358
\end{array}
\]

No entry is zero in either prime column. Consequently,

\[
\gcd(4223,N)=
\gcd(13827,N)=
\gcd(378,N)=
\gcd(13446,N)=1.
\]

Finally,

\[
\begin{aligned}
R
 &=2\cdot4655\cdot4752\\
 &=44\,241\,120\\
 &=4703\cdot9407-1.
\end{aligned}
\]

Thus $P_1P_2=R^2$ and $R\equiv-1\pmod N$. Since their common squarefree
kernel is $2$, neither $P_i$ is a square.

## 4. Parametric construction

Let $t\ge11$ be odd and satisfy $t\equiv1\pmod3$. Put

\[
N=t^2-2,
\qquad
a={N-t\over2},
\qquad
b={N+t\over2}.
\]

Because $t$ and $N$ are odd, $a,b$ are positive integers. Direct
factorization gives

\[
a={(t-2)(t+1)\over2},
\qquad
b={(t+2)(t-1)\over2}.
\]

Define

\[
\begin{aligned}
c_1&=(t-2)^2,
&w_1&={(t+1)^2\over2},\\
c_2&={2(t+2)^2\over3},
&w_2&={3(t-1)^2\over4}.
\end{aligned}
\]

Oddness of $t$ makes $w_1,w_2$ integers. The congruence
$t\equiv1\pmod3$ makes $c_2$ an integer. All endpoints are positive.
The upper bounds follow from

\[
\begin{aligned}
(t-2)^2&<t^2-2,\\
{(t+1)^2\over2}&<t^2-2,\\
{2(t+2)^2\over3}&<t^2-2,\\
{3(t-1)^2\over4}&<t^2-2.
\end{aligned}
\]

For $t\ge11$, these reduce respectively to

\[
 t>{3\over2},
\quad
t^2-2t-5>0,
\quad
t^2-8t-14>0,
\quad
t^2+6t-11>0.
\]

The third inequality is already true for every integer $t\ge10$, so all
four bounds hold.

The exact products are

\[
\begin{aligned}
c_1w_1
 &={(t-2)^2(t+1)^2\over2}
  =2a^2,\\
c_2w_2
 &={(t+2)^2(t-1)^2\over2}
  =2b^2.
\end{aligned}
\]

Using $t^2=N+2$, one obtains

\[
2a^2-1={N(N-2t+1)\over2},
\qquad
2b^2-1={N(N+2t+1)\over2}.
\]

The two displayed quotients are positive integers. Hence both endpoint
products are $1\pmod N$. Together with the range bounds, this proves that
$w_i$ is the canonical inverse of $c_i$. Also $b-a=t>0$, so the exact
values are distinct. Each has squarefree kernel $2$.

Their positive joint root is

\[
\begin{aligned}
2ab
 &={(N-t)(N+t)\over2}\\
 &={N^2-t^2\over2}\\
 &={N^2-N-2\over2}\\
 &={N(N-1)\over2}-1.
\end{aligned}
\]

It is therefore $-1\pmod N$.

## 5. Endpoint resultants

The four endpoint signs reduce to linear functions of $t$ modulo $N$.
First,

\[
2(c_1-w_1)=t^2-10t+7\equiv-10t+9\pmod N.
\]

Since

\[
(10t-9)(10t+9)=100t^2-81\equiv119\pmod N,
\]

one has

\[
\gcd(c_1-w_1,N)\mid119.
\]

Next,

\[
2(c_1+w_1)=3t^2-6t+9\equiv-3(2t-5)\pmod N.
\]

Here $3\nmid N$, and

\[
(2t-5)(2t+5)=4t^2-25\equiv-17\pmod N.
\]

Thus

\[
\gcd(c_1+w_1,N)\mid17.
\]

For the second pair,

\[
12(c_2-w_2)
=-t^2+50t+23
\equiv50t+21\pmod N,
\]

and

\[
(50t+21)(50t-21)
=2500t^2-441
\equiv4559\pmod N.
\]

Therefore

\[
\gcd(c_2-w_2,N)\mid4559.
\]

Finally,

\[
12(c_2+w_2)
=17t^2+14t+41
\equiv14t+75\pmod N,
\]

while

\[
(14t+75)(14t-75)
=196t^2-5625
\equiv-5233\pmod N.
\]

Hence

\[
\gcd(c_2+w_2,N)\mid5233.
\]

The factors $2,3,12$ can be cancelled because $N$ is odd and
$N\equiv-1\pmod3$.

## 6. An explicit infinite nonsquarefree subfamily

Let

\[
C=119\cdot17\cdot4559\cdot5233,
\qquad
M=6\cdot529\cdot C,
\qquad
t=373+mM
\]

for any integer $m\ge0$. Since $373\equiv1\pmod6$, every such $t$ is
odd and is $1\pmod3$.

The base value satisfies

\[
373^2-2=139127=23^2\cdot263.
\]

Since $t\equiv373\pmod{529}$, every resulting $N=t^2-2$ is divisible
by $23^2$. It is greater than $529$, so it is an odd nonsquarefree
composite.

Also

\[
\gcd(139127,C)=1.
\]

Indeed, the prime factors of $139127$ are $23$ and $263$, and

\[
\begin{array}{c|rrrr}
&119&17&4559&5233\\ \hline
\bmod 23&4&17&5&12\\
\bmod263&119&17&88&236
\end{array}
\]

has no zero entry. Because $t\equiv373\pmod C$, one has

\[
N=t^2-2\equiv139127\pmod C.
\]

Therefore $\gcd(N,C)=1$ for every $m$. The four resultant divisibility
bounds from the previous section now force all four endpoint sign gcds to
equal $1$. This proves the unconditional infinite family.

## 7. The \(N=139127\) certificate

For $m=0$, $t=373$, and

\[
N=139127=23^2\cdot263,
\qquad
a=69377,
\qquad
b=69750.
\]

The endpoints are

\[
(c_1,w_1)=(137641,69938),
\qquad
(c_2,w_2)=(93750,103788).
\]

Their exact values are

\[
\begin{aligned}
c_1w_1
 &=9\,626\,336\,258
  =1+69191N
  =2\cdot69377^2,\\
c_2w_2
 &=9\,730\,125\,000
  =1+69937N
  =2\cdot69750^2.
\end{aligned}
\]

The four sign values and gcds are

\[
\begin{aligned}
\gcd(137641-69938,N)&=\gcd(67703,N)=1,\\
\gcd(137641+69938,N)&=\gcd(207579,N)=1,\\
\gcd(93750-103788,N)&=\gcd(-10038,N)=1,\\
\gcd(93750+103788,N)&=\gcd(197538,N)=1.
\end{aligned}
\]

For an explicit check, the absolute sign values reduce modulo the two prime
factors as

\[
\begin{array}{c|cc}
\text{absolute sign value}&\bmod23&\bmod263\\ \hline
67703&14&112\\
207579&4&72\\
10038&10&44\\
197538&14&25
\end{array}
\]

Finally,

\[
2ab
=9\,678\,091\,500
=69563N-1.
\]

Thus this nonsquarefree certificate also has two individually nonsquare exact
values, four strict-null endpoint screens, and a global joint root.

## 8. Scope

This proof separates exact square closure from the label of the resulting
modular square root. It does not show that the full retained-relation decoder
fails. The infinite family contains the fixed divisor $23^2$, so it is not
evidence against a trial-hard or balanced-input theorem.
