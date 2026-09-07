# Independent reconstruction of the exact count and path-coordinate claims

## Audit boundary and input

This reconstruction used exactly one local mathematical input:

- experiments/F330_short_path_conditions/STATEMENT_ONLY.md
  — SHA256
  a1b1b87a5b3d4ea524a24ec6bcfb3c24b666fdaace6ab115830d912a1ebd67bc.

The hash matches the expected hash. I did not use
experiments/F326_direct_gauss_pairing/STATEMENT.md, because the F330 input
restates every P246 definition needed below. I did not read a candidate proof,
rational-path note, report, design file, implementation, numerical output, or
shared ledger.

## Setup

Let $N=2h+1>1$ be odd. For a nonzero residue, write
$\langle x\rangle_N\in\{1,\ldots,N-1\}$ for its ordinary representative and
$\operatorname{rep}(x)\in[-h,h]$ for its signed representative. Let $a$ be a
unit modulo $N$, let $b=a^{-1}$, and put

$$
Q(t)=\#\{1\le y\le t:\langle ay\rangle_N\le h\},
\qquad 0\le t\le h.
$$

When $\operatorname{Jacobi}(a,N)=1$, use the involution $F$, its domain $D$,
and the rank map $R$ stated in the input. Put $L=Q(h)$ and $d=L+h+1$. The
only path facts used below are the stated P246 facts:

1. $d$ is odd.
2. The reflection and adjacent rank involutions each have sole fixed rank
   $L$.
3. Starting at coordinate $0$, alternating $F$ and the selected auxiliary
   reaches an $F$-fixed endpoint after at most $d\le N$ evaluations of $F$.
4. The $F$-fixed test occurs before the next auxiliary move, and the
   nonterminal open path does not repeat a coordinate.

No shorter path estimate is assumed.

## 1. Count reciprocity

Fix $1\le t\le h$. Multiplication by $a$ is injective modulo $N$. Thus

$$
S_{t-1}=\{\langle ay\rangle_N:1\le y\le t-1\}
$$

has $t-1$ elements. Define $\chi(k)=1$ for $1\le k\le h$, and
$\chi(k)=0$ for $h+1\le k\le N-1$. Pair $y$ with $t-y$. If
$k=\langle ay\rangle_N$, then

$$
2Q(t)=2\chi(\langle at\rangle_N)
+\sum_{k\in S_{t-1}}
  \bigl(\chi(k)+\chi(\langle at-k\rangle_N)\bigr). \tag{1}
$$

The signed remainder $r=\operatorname{rep}(at)$ is nonzero. If it were zero,
the fact that $a$ is a unit would give $t\equiv0\pmod N$, contrary to
$1\le t<N$.

### Positive remainder

Suppose $1\le r\le h$. For $k\ne r$, split $1,\ldots,N-1$ at
$r,h,h+r$. This gives

$$
\chi(k)+\chi(\langle r-k\rangle_N)
=1+\mathbf 1_{[1,r-1]}(k)-\mathbf 1_{[h+1,h+r]}(k). \tag{2}
$$

The set $S_{t-1}$ does not contain $r$, because $r\equiv at$ and the images
of $1,\ldots,t$ are distinct. Also,
$\chi(\langle at\rangle_N)=1$. For an integer interval $I=[u,v]$, the number
of elements of $S_{t-1}$ in $I$ is exactly

$$
C_t(u,v)=\#\{k\in I:1\le\langle bk\rangle_N\le t-1\}.
$$

Substitute (2) into (1):

$$
2Q(t)=t+1+C_t(1,r-1)-C_t(h+1,h+r). \tag{3}
$$

### Negative remainder

Write $r=-s$, where $1\le s\le h$. The ordinary representative of $at$ is
$N-s$, and this endpoint contributes zero to (1). For $k\ne N-s$, split at
$h+1-s,h,N-s$. This gives

$$
\chi(k)+\chi(\langle-s-k\rangle_N)
=1+\mathbf 1_{[h+1-s,h]}(k)
   -\mathbf 1_{[N-s+1,N-1]}(k). \tag{4}
$$

Again $N-s\notin S_{t-1}$. Equations (1) and (4) give

$$
2Q(t)=t-1+C_t(h+1-s,h)-C_t(N-s+1,N-1). \tag{5}
$$

Empty intervals contribute zero.

### Bound and the remainders 1 and -1

In (3), the positive correction interval has length $r-1$, and the negative
correction interval has length $r$. Hence

$$
1-r\le 2Q(t)-t\le r.
$$

In (5), the corresponding lengths are $s$ and $s-1$, so

$$
-s\le 2Q(t)-t\le s-1.
$$

Therefore

$$
|2Q(t)-t|\le |r|. \tag{6}
$$

If $r=1$, then $b\equiv t\pmod N$. The only possible correction in (3) is
the singleton $k=h+1\equiv2^{-1}\pmod N$. Its inverse image is

$$
\langle t(h+1)\rangle_N=
\begin{cases}
t/2,&t\text{ even},\\
(t+N)/2,&t\text{ odd}.
\end{cases}
$$

It lies in $[1,t-1]$ exactly when $t$ is even. Thus (3) gives
$2Q(t)=t$ for even $t$ and $2Q(t)=t+1$ for odd $t$. Hence

$$
Q(t)=\lceil t/2\rceil.
$$

If $r=-1$, then $b\equiv-t\pmod N$. The only possible correction in (5) is
the singleton $k=h\equiv-2^{-1}\pmod N$. Its inverse image is again the
displayed representative of $t/2$. It is counted exactly when $t$ is even.
Thus $2Q(t)=t$ for even $t$ and $2Q(t)=t-1$ for odd $t$, so

$$
Q(t)=\lfloor t/2\rfloor.
$$

The two correction intervals in either (3) or (5) have total length
$2|r|-1$. After computing $b$, direct evaluation uses at most $2|r|-1$
tests of whether $1\le\langle bk\rangle_N\le t-1$. Each test has polynomial
bit cost in $\log N$. The full cost is
$O((1+|r|)\operatorname{poly}(\log N))$. It improves on a general
polylogarithmic floor-sum evaluation only when $|r|$ is suitably small.

## 2. Exact reflection defects

Assume $\operatorname{Jacobi}(a,N)=1$. Let

$$
A(i)=(2L-i)\bmod d,
\qquad B=R^{-1}AR,
$$

where residues modulo $d$ are in $\{0,\ldots,d-1\}$.

Let $y$ be accepted, meaning $\operatorname{rep}(ay)>0$, and put $q=Q(y)$.
Then $1\le q\le L$ and

$$
R(-y)=L-q,\qquad A(L-q)=L+q.
$$

The last rank is the rank of the nonnegative coordinate $q$. Hence

$$
B(-y)=q=\frac{y+E(y)}2,
\qquad E(y)=2Q(y)-y. \tag{7}
$$

For a positive coordinate $z$, $R(z)=L+z$. If $1\le z\le L$, then

$$
A(L+z)=L-z<L.
$$

The inverse-rank rule selects the least $y>0$ with $Q(y)\ge z$ and returns
$-y$. At this first crossing, $y$ is accepted and $Q(y)=z$, because $Q$
increases only by zero or one. Therefore

$$
B(z)=-y=-2z+E(y). \tag{8}
$$

If $L<z\le h$, reduction modulo $d$ gives

$$
A(L+z)=L-z+d.
$$

This rank is at least $L$. Its nonnegative coordinate is

$$
B(z)=(L-z+d)-L=d-z. \tag{9}
$$

Finally, $A(L)=L$, so $B(0)=0$. Equations (7)-(9) are identities for the
actual rank reflection. They do not bound $E$, and they do not imply a short
orbit.

## 3. Constant matrices for a = -1

Assume $N\equiv1\pmod4$ and $a=N-1\equiv-1\pmod N$. The Jacobi symbol is one.
For every $1\le y\le h$, $\operatorname{rep}(-y)=-y<0$. Consequently

$$
L=0,\qquad d=h+1=(N+1)/2,\qquad D=\{0,1,\ldots,h\}.
$$

For a nonspecial unit $x\in D$, put $w=\operatorname{rep}(x^{-1})$. If
$w>0$, the first branch of $F$ returns $w$. If $w<0$, the scaled-inverse
branch applies because $\operatorname{rep}(-x)<0$, and it returns
$\operatorname{rep}(-w)=-w$. Thus

$$
F(x)=|w|. \tag{10}
$$

This formula is used only after the special 0/1, nonunit, and unit-fixed
guards. A nonzero nonunit is already an $F$-fixed endpoint. A nonspecial unit
fixed with $w>0$ supplies the proper divisor $\gcd(x-1,N)$. A unit fixed with
$w<0$ satisfies $x^2\equiv-1\pmod N$ and supplies the stated square-root
endpoint.

### Reflection auxiliary

Because $L=0$, coordinate rank is the coordinate itself. Reflection is
$B(0)=0$ and $B(y)=d-y$ for $1\le y\le h$. The first stage is

$$
0\xrightarrow{F}1\xrightarrow{B}d-1=h.
$$

Every later valid moving stage has

$$
x'=d-|\operatorname{rep}(x^{-1})|. \tag{11}
$$

Set $z=2x-1$ and

$$
\sigma=-\operatorname{sign}(\operatorname{rep}(x^{-1})).
$$

Since $|w|\equiv\operatorname{sign}(w)x^{-1}\pmod N$, equation (11) gives

$$
z'=2x'-1\equiv-2|w|
=\frac{2\sigma}{x}
=\frac{4\sigma}{z+1}\pmod N. \tag{12}
$$

The corresponding matrix is

$$
M_\sigma=\begin{pmatrix}0&4\sigma\\1&1\end{pmatrix}.
$$

Its characteristic polynomial is $\lambda^2-\lambda-4\sigma$. Its
discriminant is $17$ for $\sigma=1$ and $-15$ for $\sigma=-1$.

After the first stage, $x=h$, so $z=N-2\equiv-2\pmod N$. Choose the integer
lift $(U,V)=(-2,1)$. Matrix multiplication gives

$$
(U,V)\longmapsto(4\sigma V,U+V). \tag{13}
$$

The pair remains primitive. Initially $U$ is even and $V$ is odd. The same
parity pattern survives (13). Also

$$
\gcd(4V,U+V)=1,
$$

because $U+V$ is odd and $\gcd(V,U+V)=\gcd(V,U)=1$.

The coordinate represented by a lift is

$$
x\equiv\frac{U+V}{2V}\pmod N. \tag{14}
$$

Starting from $V=1$, if the current $x$ is a unit, then (14) shows that
$U+V$ is a unit. This is the next denominator in (13). Thus every denominator
needed by a valid next move is a unit. If a resulting current $x$ is a
nonunit while $V$ is still a unit, (14) gives

$$
\gcd(U+V,N)=\gcd(x,N). \tag{15}
$$

For the height $H=\max(|U|,|V|)$, equation (13) gives $H'\le4H$. Since the
initial height is 2, after $T$ updates

$$
H\le2\cdot4^T.
$$

This controls stored lift size. It gives no bound on $T$.

### Adjacent auxiliary

Delete rank 0. A positive rank $y$ has compressed index $j=y-1$. Pairing $j$
with $j\mathbin{\mathrm{XOR}}1$ sends

$$
J(y)=y+(-1)^{y+1}. \tag{16}
$$

Here $h$ is even, so all positive ranks occur in these adjacent pairs. At a
nonspecial, nonterminal unit stage, let

$$
w=\operatorname{rep}(x^{-1}),\qquad
s=\operatorname{sign}(w),\qquad
\epsilon=(-1)^{|w|+1}.
$$

Equations (10) and (16) give

$$
x'=\epsilon+|w|
\equiv\epsilon+\frac{s}{x}\pmod N. \tag{17}
$$

Thus

$$
C_{\epsilon,s}=
\begin{pmatrix}\epsilon&s\\1&0\end{pmatrix}.
$$

When $s=-1$, direct multiplication gives

$$
C_{\epsilon,-1}^{\,3}=-\epsilon I. \tag{18}
$$

Three consecutive valid moves with the same pair $(\epsilon,-1)$ would return
to the same projective coordinate. That would repeat a coordinate on the
nonterminal open path. The P246 no-repeat property excludes such a triple.

The initial special stage is $0\to1\to2$. Start the adjacent lift at
$(U,V)=(2,1)$. Equation (17) gives

$$
(U,V)\longmapsto(\epsilon U+sV,U). \tag{19}
$$

The update matrix has determinant $-s\in\{1,-1\}$, so it preserves a primitive
integer pair. It also gives $H'\le2H$. Hence

$$
H\le2^{T+1}
$$

after $T$ updates. As for reflection, all special and terminal guards apply
before (19), and the height estimate does not shorten the path.

## 4. Even residues, positive blocks, and the one-inverse kernel

Continue with $N\equiv1\pmod4$ and $a=-1$. Define

$$
\phi(x)=
\begin{cases}
x,&x\text{ even},\\
N-x,&x\text{ odd},
\end{cases}
\qquad 1\le x\le h.
$$

This is a bijection from $1,\ldots,h$ to the even ordinary residues
$2,4,\ldots,N-1$. If $J$ is the adjacent auxiliary in (16), then a check of
the two parities of $x$ gives

$$
\phi(J(x))=N+1-\phi(x). \tag{20}
$$

Write $u=\phi(x)$, and let $v=\langle u^{-1}\rangle_N$. The unsigned
representative in (10) is $\min(v,N-v)$. Applying (20) after $F$ gives the
complete moving rule away from a special or terminal state:

$$
u'=
\begin{cases}
1+v,&v\text{ odd}\quad(\text{plus}),\\
N+1-v,&v\text{ even}\quad(\text{minus}).
\end{cases} \tag{21}
$$

If $v$ is odd, the even-residue image of $\min(v,N-v)$ is $N-v$, and (20)
returns $1+v$. If $v$ is even, that image is $v$, and (20) returns $N+1-v$.

After the initial $0\to1\to2$ stage,

$$
u=2,\qquad v=(N+1)/2.
$$

Since $N\equiv1\pmod4$, $v$ is odd. More generally, consider a reached block
start with $u$ even, $v$ odd, and $uv\equiv1\pmod N$. The first move is plus.
Before using the next inverse, test

$$
g=\gcd(u+1,N). \tag{22}
$$

Because $u$ is a unit,

$$
\gcd(v+1,N)=\gcd(u(v+1),N)=\gcd(u+1,N). \tag{23}
$$

Thus (22) detects exactly when the plus endpoint $v+1$ is a nonunit. Assume
no factor was returned, and let

$$
z=\langle(u+1)^{-1}\rangle_N.
$$

The inverse of the plus endpoint is

$$
\langle(v+1)^{-1}\rangle_N=N+1-z, \tag{24}
$$

because $(v+1)^{-1}\equiv u/(u+1)\equiv1-z\pmod N$. The case $z=1$ would
imply $u=0\pmod N$, so the displayed ordinary representative is valid.

If $z$ is odd, (24) is odd. The next block starts after one plus move, with

$$
(u,v)\longmapsto(v+1,N+1-z). \tag{25}
$$

This is a $P$ block. If $z$ is even, (24) is even, so (21) forces one minus
move. It sends the even residue to $z$, whose ordinary inverse is $u+1$.
Thus

$$
(u,v)\longmapsto(z,u+1). \tag{26}
$$

This is a $Q$ block. Its new inverse is odd, so another minus cannot follow.
The moving word before termination consists only of plus and plus-minus
blocks. In particular, plus-minus-minus cannot occur.

As fractional transformations, the two blocks are

$$
P=\begin{pmatrix}1&1\\1&0\end{pmatrix},
\quad u\longmapsto\frac{u+1}{u},
\qquad
Q=\begin{pmatrix}0&1\\1&1\end{pmatrix},
\quad u\longmapsto\frac1{u+1}. \tag{27}
$$

Starting with the positive lift $(U,V)=(2,1)$, they act by

$$
P:(U,V)\mapsto(U+V,U),
\qquad
Q:(U,V)\mapsto(V,U+V). \tag{28}
$$

Both matrices are unimodular and have nonnegative entries. They preserve
positive primitive integer pairs.

### Exact guards in the kernel

At every nonterminal block start, $u$ is even, $v$ is odd,
$uv\equiv1\pmod N$, and $u,v\in[1,N-1]$.

First, a unit block-start coordinate cannot satisfy $u^2\equiv1\pmod N$:
its ordinary inverse would then be $u$, which is even, contrary to the odd
$v$ invariant. A unit $F$-fixed endpoint at a block start must therefore come
from $u^2\equiv-1\pmod N$. The explicit square-root check catches it.

Second, (23) proves that the gcd check catches a nonunit plus endpoint before
the $F$ call that would fix that endpoint. If $1<g<N$, it is a verified proper
divisor. The case $g=N$ would require $u=N-1$, which corresponds under $\phi$
to the special coordinate $x=1$. It is not the initial block start. If it
were reached later, $F(1)=0$, and the adjacent auxiliary fixes 0. The path
would return to its starting coordinate without an intervening $F$-fixed
endpoint. This contradicts the stated open-path guarantee. Thus the continuing
case has $g=1$, and $z$ exists.

A $Q$ block suppresses the explicit terminal test at its intermediate plus
coordinate $u_1=v+1$, so this point needs a separate audit. It is a unit after
the gcd guard, and its ordinary inverse is the even number $N+1-z$. If
$u_1^2\equiv-1\pmod N$, its inverse would be $N-u_1$, which is odd. This is
impossible. If $u_1^2\equiv1\pmod N$, then

$$
(v+1)^2\equiv1
\quad\Longrightarrow\quad
v(v+2)\equiv0
\quad\Longrightarrow\quad
v\equiv-2\pmod N,
$$

because $v$ is a unit. Hence $u=h$ and $u_1=N-1$, the special coordinate
$x=1$, rather than a nontrivial unit fixed point. The same open-path argument
excludes reaching $u=h$ before termination: its plus move would reach that
special point and then force a return to 0. Therefore a $Q$ block skips no
nontrivial fixed endpoint and no reachable special endpoint.

These facts give the exact kernel:

    u=2; v=(N+1)/2
    repeat:
        if u*u mod N == N-1: return the square root u of -1
        g=gcd(u+1,N)
        if 1<g<N: return g
        z=(u+1)^(-1) mod N, using its ordinary representative
        if z even: (u,v)=(z,u+1)          # Q, using old u and v
        else:      (u,v)=(v+1,N+1-z)     # P, using old u and v

Each continuing iteration computes one modular inverse, regardless of whether
the block contains one or two fine $F$-moves. All other work in the iteration
has polynomial bit cost in $\log N$. Each block advances by at least one
$F$-move. The P246 bound therefore gives $O(N)$ blocks and polynomial bit cost
per block. A terminal gcd branch can return before computing that iteration's
inverse.

For the lift in (28), both $U$ and $V$ are units before every test. This is
true initially. If no gcd is returned, $U+V$ is a unit because

$$
\gcd(U+V,N)=\gcd(u+1,N)
$$

when $V$ is a unit. Either update in (28) preserves the claim. The two terminal
predicates become exactly

$$
\gcd(U+V,N)>1,
\qquad
U^2+V^2\equiv0\pmod N. \tag{29}
$$

The first is equivalent to the gcd guard, and the second is equivalent to
$u^2\equiv-1\pmod N$. If $N$ has a prime divisor $p\equiv3\pmod4$, the second
predicate is impossible, because reduction modulo $p$ would give a square
root of $-1$ in $\mathbb F_p$.

## 5. Translation runs and inverse parity

At any reached block start, $u$ is even and its ordinary inverse is odd. A
$Q$ block is selected exactly when

$$
\langle(u+1)^{-1}\rangle_N\text{ is even}.
$$

It ends at

$$
q=\langle(u+1)^{-1}\rangle_N,
\qquad q^{-1}=u+1,
$$

where the last equality is as an ordinary representative. If the next block
is $P$, its endpoint is

$$
q^{-1}+1=u+2. \tag{30}
$$

The $P$ branch is selected exactly when the ordinary inverse of its endpoint
is odd, by (24)-(25). Hence a reached consecutive $Q,P$ pair is equivalent,
apart from earlier guards, to

$$
\operatorname{parity}(u^{-1},(u+1)^{-1},(u+2)^{-1})
  =(\mathrm{odd},\mathrm{even},\mathrm{odd}), \tag{31}
$$

and it translates $u$ to $u+2$. Repeated $Q,P$ pairs require the alternating
inverse-parity pattern on every consecutive integer in the covered interval.
Equation (30) is an equality of ordinary representatives only while the run
remains inside $[1,N-1]$; this range condition is part of the run.

The phrase “apart from earlier guards” is essential. A jump over one or more
such pairs must preserve the fine-path stopping order. It must:

1. stop on a nonunit before asking for its inverse; the kernel gcds at the
   relevant block starts are equivalent to the gcds of the consecutive
   integers in (31);
2. test the $u^2\equiv-1\pmod N$ fixed endpoint at every actual block start,
   including the intermediate $Q$ endpoint $q=(u+1)^{-1}$; equivalently,
   $q^2\equiv-1$ exactly when $(u+1)^2\equiv-1$;
3. preserve the special 0/1 exclusions and the $u=N-1$ range endpoint; the
   only potentially hidden $Q$-intermediate special point is the already
   excluded case arising from $u=h$; and
4. stop before crossing any earlier nonunit, fixed, special, or out-of-range
   point, even if later parity values fit the alternating pattern.

Finally, let $t$ be any unit and set $q=\langle t^{-1}\rangle_N$. Since
$2^{-1}\equiv h+1\pmod N$,

$$
\operatorname{rep}((2t)^{-1})=
\begin{cases}
q/2>0,&q\text{ even},\\
(q+N)/2-N<0,&q\text{ odd}.
\end{cases}
$$

Therefore

$$
\langle t^{-1}\rangle_N\text{ is even}
\quad\Longleftrightarrow\quad
\operatorname{rep}((2t)^{-1})>0. \tag{32}
$$

The parity predicate is exactly a half-interval predicate on the modular
inverse curve.

## Statement comparison and gap assessment

| Input item | Independently recovered result | Scope and guards |
|---|---|---|
| Claim 1 | Both signed-remainder identities, the bound, the $r=\pm1$ formulas, and the $2|r|-1$ test count | Needs only odd $N$, unit $a$, and $1\le t\le h$. It does not use the Jacobi condition or assume $t$ is a unit except where $r=\pm1$ forces it. |
| Claim 2 | All four formulas for $B$, including the least-crossing value $Q(y)=z$ | Uses the stated exact rank inverse. It gives no small-defect or short-orbit bound. |
| Claim 3 | Both constant matrix systems, discriminants, primitive lifts, denominator facts, the factor identity, the no-three-repeat identity, and both height bounds | Every recurrence is conditional on the special, nonunit, and fixed-point guards. Lift height bounds storage, not path length. |
| Claim 4 | The even-residue conjugacy, plus/minus dynamics, $P/Q$ blocks, positive primitive lifts, exact one-inverse kernel, and all intermediate guards | The $Q$ grouping skips no reachable terminal. The inherited traversal bound is only $O(N)$ blocks with polynomial bit cost per block. |
| Claim 5 | The $Q,P$ translation, the exact odd-even-odd condition, its longer alternating form, and the half-interval equivalence | A jump must certify all earlier gcd, root, special, and range guards. No first-mismatch algorithm or probability estimate follows from the identity. |

I found no substantive internal gap in the five stated claims. The exact
remaining gap toward a Las Vegas expected quasipolynomial result is the one
the input itself leaves open: an algorithm that locates or bypasses a first
inverse-parity mismatch while preserving every earlier terminal guard, plus
an expected-cost or probability argument for that algorithm. An expected
Las Vegas bound would suffice for that goal; these claims do not require a
deterministic short-path bound for every random outcome.
