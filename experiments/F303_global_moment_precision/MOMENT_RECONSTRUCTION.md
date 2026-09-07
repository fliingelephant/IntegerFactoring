# Blind reconstruction of the mixed-moment algorithm

inputhash: sha256:568441f2eebe3f519c356a4d0fe3cf43ac7243ede4a0e229f18683862f1f5b95

status: Complete. The residue algorithm follows from the explicit recurrences
below. I found no gap at the stated scope.

Put $h=M/2=2^{k-1}$, and write $\nu_2$ for the 2-adic valuation. Every
series below is a formal series at $T=0$ with coefficients in $\mathbb Z_2$.
No Archimedean evaluation is used.

## 1. Inverse power sums without unit enumeration

For $s\geq 3$, let

$$
U_s=\{1,3,\ldots,2^s-1\},\qquad
H_r^{(s)}=\sum_{u\in U_s}u^{-r}\in\mathbb Z_2\quad(r\geq1).
$$

Since $U_{s+1}=U_s\mathbin{\dot\cup}(U_s+2^s)$, the formal binomial
series gives

$$
H_r^{(s+1)}
=2H_r^{(s)}
 +\sum_{t\geq1}(-1)^t {r+t-1\choose t}2^{st}H_{r+t}^{(s)}. \tag{1}
$$

Modulo $2^W$, only $1\leq t\leq\lfloor(W-1)/s\rfloor$ can contribute.
The four base terms in $U_3=\{1,3,5,7\}$ are computed modulo $2^W$.
To obtain $H_1^{(s)},\ldots,H_R^{(s)}$, define backwards

$$
R_s=R,\qquad
R_\ell=R_{\ell+1}+\lfloor(W-1)/\ell\rfloor
\quad(\ell=s-1,\ldots,3).
$$

Compute the base sums through $R_3$, then apply (1) forwards, retaining
indices through $R_{\ell+1}$. Each requested term then has every dependency
available. Since $R_3\leq R+(s-3)W$, this costs polynomially many operations
in $s,R,W$. All arithmetic is reduced modulo $2^W$.

An odd inverse can be computed internally: start with the inverse modulo 2
and iterate $x\leftarrow x(2-ax)$. Each iteration doubles the number of
correct 2-adic bits. Powers of the four base inverses are then obtained by
successive multiplication. Thus (1) uses no external algorithm and does
not list $U_s$.

## 2. Newton identities with nonunit divisors

For a finite family $x_i\in\mathbb Z_2$, put
$p_j=\sum_i x_i^j$, and let $e_t$ be its elementary symmetric functions.
Newton's identity is

$$
t e_t=\sum_{j=1}^t(-1)^{j-1}e_{t-j}p_j. \tag{2}
$$

Suppose $e_1,\ldots,e_T$ are wanted modulo $2^L$. Obtain every $p_j$
modulo $2^{L+\nu_2(T!)}$, and compute $e_t$ successively at precision

$$
\lambda_t=L+\nu_2(T!/t!)\qquad(0\leq t\leq T).
$$

At step $t$, the right side of (2) is needed modulo

$$
2^{\lambda_t+\nu_2(t)}=2^{\lambda_{t-1}}.
$$

Every earlier $e_{t-j}$ is known to at least this precision. Write
$t=2^v o$ with $o$ odd. The canonical residue of the right side modulo
$2^{\lambda_t+v}$ is divisible by $2^v$, because the exact identity (2)
is. Divide this representative by $2^v$, then multiply by $o^{-1}$ modulo
$2^{\lambda_t}$. This determines $e_t$ uniquely. An even Newton divisor is
therefore never inverted modulo a power of two. The guard is
$\nu_2(T!)\leq T$. For $T=0$, the procedure does no work and $e_0=1$.

## 3. The unit-product primitive at arbitrary precision

Let $G_s=\prod_{u\in U_s}u$. Splitting the two lifts of each odd residue
gives the exact identity in $\mathbb Z_2$

$$
G_{s+1}=G_s^2 C_s,\qquad
C_s=\prod_{u\in U_s}(1+2^s/u). \tag{3}
$$

If $e_t^{(s)}=e_t((u^{-1})_{u\in U_s})$, then modulo $2^P$

$$
C_s=\sum_{t=0}^{T_s}2^{st}e_t^{(s)},\qquad
T_s=\min\bigl(2^{s-1},\lfloor(P-1)/s\rfloor\bigr). \tag{4}
$$

Every omitted term contains $2^P$. Compute
$H_1^{(s)},\ldots,H_{T_s}^{(s)}$ from (1), to precision
$P+\nu_2(T_s!)$, and apply the guarded Newton procedure to (4). If
$T_s=0$, set $C_s=1$.

Starting from $G_3=1\cdot3\cdot5\cdot7=105$, equations (3)--(4) compute

$$
\Pi_M=G_k\pmod {2^P}
$$

for every $P\geq1$. Only the fixed four-element base is enumerated.
Here $T_s\leq P$, the guarded precision is at most $2P$, and the largest
index used in (1) is $O(P+sP)$. There are $O(k)$ modular squarings and at
most $O(\min(k,P))$ nontrivial corrections. The binomial coefficients in
(1) can be formed by Pascal addition; their indices and bit lengths are
polynomial in $k,P$. This proves the claimed uniform polynomial-bit
primitive without an external algorithmic dependency.

## 4. Ordinary power sums and product coefficients

For $n\geq1$, define $B_j(n)=\sum_{x=0}^{n-1}x^j$, with $B_0(n)=n$.
Telescoping $(x+1)^{j+1}-x^{j+1}$ gives

$$
B_j(n)=
\frac{n^{j+1}-\sum_{r=0}^{j-1}{j+1\choose r}B_r(n)}{j+1}. \tag{5}
$$

This division is exact over the integers. Therefore

$$
A_j=B_j(M)-2^jB_j(h) \tag{6}
$$

is computed exactly for $0\leq j\leq D$. In particular,
$A_0=M-h=h$. Applying (2) over the integers to the power sums $A_j$
computes exactly

$$
\alpha_t=e_t((u)_{u\in U_k}).
$$

All divisions in this computation are exact integer divisions. It is
enough to compute $0\leq t\leq E:=\min(D,h)$.

For the reciprocal coefficients, compute
$H_1^{(k)},\ldots,H_E^{(k)}$ from (1), at precision

$$
W=2k+\nu_2(E!),
$$

and use the guarded Newton procedure with target precision $2k$. This gives

$$
\beta_t=e_t((u^{-1})_{u\in U_k})\pmod {M^2}
\qquad(0\leq t\leq E).
$$

Set $\alpha_t=\beta_t=0$ for $t>h$, and
$\alpha_0=\beta_0=1$.

## 5. Truncated formal computation of $R(T)$

Regard $\eta=N^{-1}$ as a 2-adic integer, retaining it modulo $M^2$ after
reducing the full input integer $N$. This is valid for every positive odd
$N$, with no assumption that $N<M$. Use the unit-product primitive with
$P=2k$ to obtain $\pi=\Pi_M\pmod {M^2}$, and set

$$
c=\pi^2\eta^h\pmod {M^2},\qquad
X(T)=\sum_{t=0}^{E}\beta_tT^t,\qquad
Y(T)=\sum_{t=0}^{E}\alpha_t\eta^tT^t.
$$

In $\mathbb Z_2[T]$,

$$
\prod_{u\in U_M}(T+u)=\Pi_M\prod_u(1+T/u)
$$

and

$$
\prod_{u\in U_M}(N+Tu)=N^h\prod_u(1+\eta Tu).
$$

Consequently $R(T)=cX(T)/Y(T)$ modulo $M^2$. Since $Y(0)=1$, its
formal inverse exists. Coefficient comparison in $Y(T)R(T)=cX(T)$ gives
$r_n=[T^n]R(T)\pmod {M^2}$ through degree $D$:

$$
r_0=c,\qquad
r_n=c\beta_n-
\sum_{t=1}^{\min(n,E)}\alpha_t\eta^t r_{n-t}
\pmod {M^2}, \tag{7}
$$

where $\beta_n=0$ for $n>E$. This is a purely formal truncated division.
It uses polynomial work even when $D>h$.

## 6. Recovery of the carry moments

For every odd $N$, multiplication by $N$ and inversion permute $U_M$.
Moreover, if $v_N(u)\equiv Nu^{-1}\pmod M$, then
$v_N(v_N(u))\equiv N(Nu^{-1})^{-1}\equiv u\pmod M$; equality holds for
the chosen representatives. Thus $u\mapsto v_N(u)$ is a permutation and
an involution. The definition of $q_u$ gives the exact factor identity

$$
1+\frac{Mq_u}{N+Tu}
=\frac{u(T+v_N(u))}{N+Tu}.
$$

Multiplication over $U_M$ proves the stated product identity for $R$.
Modulo $M^2$ in $\mathbb Z_2[[T]]$, all products of two correction terms
vanish:

$$
R(T)-1\equiv
M\sum_{u\in U_M}\frac{q_u}{N+Tu}\pmod {M^2}.
$$

Since

$$
(N+Tu)^{-1}
=\sum_{j\geq0}(-1)^ju^jN^{-j-1}T^j,
$$

we obtain

$$
\frac{[T^j](R(T)-1)}{M}
\equiv(-1)^jN^{-j-1}Q_j\pmod M. \tag{8}
$$

This also proves the required coefficient divisibility. Let

$$
d_0=(r_0-1)\bmod M^2,\qquad d_j=r_j\quad(j\geq1),
$$

using representatives in $[0,M^2-1]$. Each $d_j$ is an ordinary integer
multiple of $M$. Divide that representative exactly by $M$, reduce modulo
$M$, and set

$$
Q_j=(-1)^jN^{j+1}(d_j/M)\pmod M. \tag{9}
$$

No inverse of $M$ is used.

For $a\geq b\geq1$, put $j=a-b$. From
$uv_N(u)=N+Mq_u$, the integer binomial theorem gives

$$
u^av_N(u)^b
=u^j(N+Mq_u)^b
\equiv u^j\bigl(N^b+bMN^{b-1}q_u\bigr)\pmod {M^2}.
$$

After summation,

$$
S_{ab}=N^bA_j+bMN^{b-1}Q_j\pmod {M^2}. \tag{10}
$$

The involution gives $S_{ab}=S_{ba}$. For arbitrary $a,b$, let
$c_1=\max(a,b)$ and $d_1=\min(a,b)$. If $d_1=0$, use
$S_{ab}=A_{c_1}\pmod {M^2}$. If $d_1\geq1$, use (10) with
$b=d_1$ and $j=c_1-d_1$. In particular,

$$
S_{00}=A_0=h\pmod {M^2},\qquad
Q_0=N(d_0/M)\pmod M.
$$

Thus $D=0$ requires no positive-degree Newton or series step and is fully
covered.

## 7. Bit sizes, uniformity, and scope

The exact value $B_j(n)$ has $O((j+1)k)$ bits for
$n\in\{M,h\}$. Also $\alpha_t\leq h^tM^t$, so its bit length is
$O(tk)$. The exact recurrences (2), (5), and (6) therefore use
polynomial-size operands.

For the reciprocal calculation,
$W=2k+\nu_2(E!)\leq2k+E$, and the largest index needed by (1) is at most
$E+kW$. All modular operands, binomial indices, and loop counts are
polynomial in $k,D$. Equation (7) uses $O(D^2)$ modular operations, and all
requested entries in (10) take another $O(D^2)$ operations. The exponent
$h=2^{k-1}$ has $k$ bits, so $\eta^h$ takes $O(k)$ modular squarings.

The input $N$ is only reduced modulo $M^2$ (and modulo $M$ where needed).
Its inversion and powers use $O(k)$-bit residues after one pass over its
ordinary binary representation. Total bit complexity is therefore
polynomial in $k$, the numerical degree $D$, and the ordinary binary length
of $N$.

The construction does not enumerate the inverse graph, use factors of
$N$, receive a unit list, or enumerate $M/2$ units. It proves only
$Q_j\bmod M$ and $S_{ab}\bmod M^2$. It does not recover exact integer mixed
moments, complex Cauchy resolvents, rectangle counts, or a factoring
algorithm.
