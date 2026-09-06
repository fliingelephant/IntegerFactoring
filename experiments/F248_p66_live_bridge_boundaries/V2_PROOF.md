# Proofs for F248 V2

## 1. Elementary facts and the normalized-root screen

CRT gives

\[
(\mathbb Z/N^2\mathbb Z)^\times
\cong
(\mathbb Z/p^2\mathbb Z)^\times
\times
(\mathbb Z/q^2\mathbb Z)^\times.
\]

The two local groups are cyclic of orders \(p(p-1)\) and \(q(q-1)\).
Because \(\gcd(E,N)=1\), the local kernels of the \(E\)-power map have
orders

\[
\gcd(E,p(p-1))=g_p,
\qquad
\gcd(E,q(q-1))=g_q.
\]

Thus the global kernel has order \(K=g_pg_q\).

A unit square modulo \(N=pq\) has four roots. Relative to any fixed root,
the four normalized roots have CRT signs

\[
(1,1),\quad(-1,-1),\quad(1,-1),\quad(-1,1).
\]

For an exact integer square \(V=s^2\) with supplied unit root \(x\bmod N\),

\[
z=sx^{-1}\pmod N
\]

is one of these roots of one. The two global cases make both
\(\gcd(s-x,N)\) and \(\gcd(s+x,N)\) trivial or equal to \(N\). Each mixed
case makes one of them \(p\) and the other \(q\). This proves the screen used
throughout.

We also record two asymptotic facts. First,

\[
\varphi(N)=N(1-1/p)(1-1/q)=2^{n+O(1)}.
\]

Indeed, \(2^{n-1}<N<2^n\), and the two Euler factors are bounded below by a
positive absolute constant for distinct odd primes. Second, if a positive
integer \(m\) has \(O(n)\) bits, then

\[
\tau(m)=2^{o(n)}.
\]

For completeness, fix \(\epsilon>0\). For every sufficiently large prime
\(\ell\) and every \(a\ge1\), one has
\(a+1\le\ell^{\epsilon a}\). The finitely many smaller primes contribute a
constant \(C_\epsilon\) after maximizing
\((a+1)/\ell^{\epsilon a}\). Multiplication over the prime-power
factorization of \(m\) gives \(\tau(m)\le C_\epsilon m^\epsilon\). Since
\(\epsilon\) is arbitrary and \(\log m=O(n)\), the displayed subexponential
bound follows.

## 2. Uniform full scalar lifts

Let

\[
G=(\mathbb Z/N^2\mathbb Z)^\times.
\]

The image of the \(E\)-power map has size

\[
\frac{|G|}{K}
=\frac{\varphi(N^2)}K
=\frac{N\varphi(N)}K.
\]

A uniform input maps uniformly onto this image.

Every positive unit square below \(N^2\) is \(s^2\) for a unique unit
\(s\in\{1,\ldots,N-1\}\). There are \(\varphi(N)\) such integer squares.
Intersecting them with the power-map image can only decrease this number.
Therefore

\[
\Pr([A^E]_{N^2}\text{ is an exact square})
\le
\frac{\varphi(N)}{N\varphi(N)/K}
=\frac KN.
\]

### 2.1 The supplied roots in one output fibre

Fix a reached square output and one preimage \(A_0\). Every preimage is
\(A_0z\), with \(z\) in the \(E\)-power kernel. Its supplied root differs
from the root of \(A_0\) by

\[
z^{E/2}\pmod N.
\]

Consider one local side \(r\in\{p,q\}\). Its kernel modulo \(r^2\) is cyclic
of order \(g_r=\gcd(E,r-1)\). Reduction modulo \(r\) is injective on this
kernel: the kernel of reduction has order \(r\), while \(g_r\mid r-1\).
The image of the \(E/2\)-power map on the local kernel therefore has size

\[
\frac{g_r}{\gcd(g_r,E/2)}.
\]

Put \(e=v_2(E)\) and \(t=v_2(r-1)\). The odd part of \(g_r\) divides
\(E/2\). Hence the quotient is two when \(e\le t\), and one when \(e>t\).
Every image element squares to one. The image is therefore \(\{1,-1\}\) in
the first case and \(\{1\}\) in the second.

If one or both local images are active, translation by the resulting sign
subgroup pairs every global normalized root with a mixed one. Thus every
coset contains equally many global and mixed roots. Uniformity on the input
fibre proves the conditional one-half law.

## 3. A complete principal-lift fibre

The binomial theorem modulo \(N^2\) gives

\[
(a_0+tN)^E
\equiv
a_0^E+Ea_0^{E-1}tN
\pmod{N^2}.
\]

After separating the fixed residue \(r=[a^E]_N\), this becomes

\[
h_t=h_0+Ea^{E-1}t\pmod N.
\]

The slope is a unit because \(a\) and \(E\) are units modulo \(N\). Hence
\(t\mapsto h_t\) permutes all \(N\) digits.

Put \(x=[a^{E/2}]_N\). The congruence

\[
s^2\equiv r=x^2\pmod N
\]

has four roots \(s\in\{1,\ldots,N-1\}\). Their four integer squares are
distinct, are below \(N^2\), and have residue \(r\bmod N\). Conversely, every
exact square below \(N^2\) with residue \(r\) arises from one of these four
roots. The digit permutation therefore reaches exactly four exact squares.

As \(s\) runs through the roots, \(s/x\bmod N\) runs through all four roots
of one. Exactly two are mixed. This proves the exact \(4/N\) and \(2/N\)
laws.

If one useful square is located, its positive root \(s<N\) is a mixed second
root of \(r\bmod N\), and a signed gcd factors \(N\). Conversely, if \(p\)
and \(q\) are known, CRT combines opposite local signs of \(x\) to construct
the two mixed roots. For either root \(s\), compute

\[
h_s=\frac{s^2-r}{N},
\qquad
t=(h_s-h_0)(Ea^{E-1})^{-1}\pmod N.
\]

These are the two useful lift digits. All operations have bit complexity
polynomial in the public input length.

### 3.1 One fixed past product and one fresh lift

Write the positive integer \(P\) uniquely as

\[
P=du^2,
\]

where \(d\) is positive and squarefree. This decomposition is used only in
the proof.

Let \(B_t=[A_t^E]_{N^2}\). If \(PB_t\) is an exact square, parity of every
ordinary prime valuation forces

\[
B_t=dv^2
\]

for a positive integer \(v\). Since \(B_t<N^2\),

\[
0<v<\frac N{\sqrt d}\le N.
\]

All of \(d,u,v,X,x\) are units modulo \(N\) in this event. Reduction modulo
\(N\) gives

\[
dv^2\equiv x^2\pmod N.
\]

Also \(X^2\equiv du^2\pmod N\), so \(d\) is a square on both local sides.
The congruence for \(v\) therefore has exactly four CRT residue classes.
The interval \(0<v<N\) contains at most one representative of each class.

The positive exact root of \(PB_t\) is \(S=duv\), and its normalized root is

\[
w=S(Xx)^{-1}=duv(Xx)^{-1}\pmod N.
\]

Multiplication by the fixed unit \(du(Xx)^{-1}\) injects the four possible
\(v\)-classes into the four roots of one. At most two images are mixed. Each
surviving integer \(v\) fixes \(B_t=dv^2\), hence one digit \(h_t\), hence
one value of \(t\). At most two fresh coordinates are useful. Uniform
sampling gives the conditional \(2/N\) bound.

The argument uses one product \(P\) fixed before \(t\) is sampled. It gives
no union bound over exponentially many products selected after \(B_t\) is
visible.

## 4. Canonical scalar duplicates

For a fixed canonical unit \(b\), equality

\[
[a^E]_{N^2}=[b^E]_{N^2}
\]

places \(a\) in one fibre of the \(E\)-power map on the full unit group
modulo \(N^2\). That fibre has \(K\) members. Its intersection with the
canonical set \(\{1,\ldots,N-1\}\) has at most \(K\) members. Thus

\[
\Pr[u(a)=u(b)]\le\frac K{\varphi(N)}.
\]

For a duplicate, the supplied roots square to the same residue modulo \(N\).
Their ratio is a root of one, and Section 1 gives the factor criterion.

## 5. Reciprocal scalar outputs

Let \(u=[a^E]_M\) and \(v=[u^{-1}]_M\). If

\[
uv=R^2
\]

as positive integers, then \(uv\equiv1\pmod M\). Also \(u,v<M\), so
\(0<R<M\). Therefore \(R\in\mathcal R_M\). CRT gives exactly four such
roots.

For a fixed \(R\in\mathcal R_M\), the exact identity forces

\[
u\mid R^2,
\qquad
v=R^2/u.
\]

Hence at most \(\tau(R^2)\) output values \(u\) can work for this \(R\), and
at most \(S_M\) outputs work in total. Each fixed output has at most \(K\)
canonical base preimages by the same full-fibre argument as in Section 4.
Division by the \(\varphi(N)\) possible canonical bases proves

\[
\Pr[uv\text{ is square}]\le\frac{KS_M}{\varphi(N)}.
\]

Since \(R^2<M^2=N^4\), every argument of \(\tau\) has \(O(n)\) bits.
Section 1 gives \(S_M=2^{o(n)}\).

The supplied roots of \(u\) and \(v\) can be taken as \(x\) and \(x^{-1}\),
so their product root is one. The exact root \(R\bmod N\) factors precisely
when mixed. This proof uses the reciprocal output modulo \(N^2\). A canonical
integer representative of \(a^{-1}\bmod N\) need not be the reciprocal of
\(a\bmod N^2\), so its powered output is outside the theorem.

## 6. Raw norm-one torus rows

Over \(\mathbb F_r\), the norm-one torus has order

\[
m_r=r-\left(\frac Dr\right).
\]

If \(D\) is a square, the coordinates \(x-dy,x+dy\) identify the group with
\(\mathbb F_r^\times\), of order \(r-1\). If \(D\) is a nonsquare, it is the
norm-one kernel in \(\mathbb F_{r^2}^\times\), of order \(r+1\). Points with
\(x=0\) solve \(-Dy^2=1\), so their number is

\[
z_r=1+\left(\frac{-D}{r}\right)\in\{0,2\}.
\]

CRT now gives \(H=(m_p-z_p)(m_q-z_q)\) clean global points. For every
admitted canonical \(y\), the equation

\[
x^2=1+Dy^2
\]

has two nonzero roots on each local side. Thus every admitted global \(y\)
has exactly four clean points.

### 6.1 Pell count

An exact-square row satisfies

\[
R^2-D_0y^2=1.
\]

If \(D_0=d^2\) is an integer square, then

\[
(R-dy)(R+dy)=1.
\]

Both factors are nonnegative integers. Hence \(R=1\) and \(y=0\).

Suppose \(D_0\) is nonsquare. Let

\[
\epsilon=R_1+y_1\sqrt{D_0}
\]

be the least positive Pell unit above one. The positive Pell solutions are
its powers. Moreover,

\[
\epsilon
=R_1+y_1\sqrt{D_0}
>2y_1\sqrt{D_0}
\ge2\sqrt{D_0}.
\]

For \(0<y<N\),

\[
R+y\sqrt{D_0}<2N\sqrt{D_0}+1.
\]

The number of positive-\(y\) solutions is therefore at most

\[
\left\lfloor
\frac{\log(2N\sqrt{D_0}+1)}{\log(2\sqrt{D_0})}
\right\rfloor.
\]

Adding \(y=0\) proves the definition and bound \(B_D(N)\). The denominator
is bounded below by a positive constant in the nonsquare case, while the
numerator is \(O(\log N)\), so \(B_D(N)=O(n)\) uniformly.

At most \(B_D(N)\) admitted \(y\)-values are exact-square rows. Each has four
points. This proves the probability \(4B_D(N)/H\).

### 6.2 Raw duplicates

Because \(D_0>0\) and canonical \(y\)-coordinates are nonnegative,

\[
A_{y_1}=A_{y_2}\quad\Longleftrightarrow\quad y_1=y_2.
\]

There are \(H/4\) admitted \(y\)-values, each with four points. Two
independent uniform points therefore have duplicate probability

\[
\frac H4\left(\frac4H\right)^2=\frac4H.
\]

For each first point, exactly two of the four points in its \(y\)-fibre
change the local sign on one prime side and not the other. These are the
mixed root ratios. Hence the useful-duplicate probability is \(2/H\).

## 7. Powered torus rows

On a local cyclic torus of order \(m_r\), the \(W\)-power image has order

\[
\rho_r=\frac{m_r}{\gcd(m_r,W)}.
\]

A uniform input maps uniformly onto this image. CRT makes the global image
the product of the two local images. Conditioning on \(x\) being a unit
therefore gives the uniform distribution on its \(H'\) clean points.

For a local point \(U=(x,y)\), the other point with the same \(y\) is

\[
(-x,y)=-U^{-1}.
\]

It belongs to the same image subgroup exactly when \(-1\) belongs to that
subgroup, which for a cyclic group is exactly when its order is even.
Removing \(x=0\) removes the fixed points of this involution. Thus every
clean local \(y\)-fibre has size two for even image order and one for odd
image order.

The coprimality \(\gcd(\rho_p,\rho_q)=1\) allows at most one even side.
Every clean global \(y\)-fibre has size at most two. Combining this with the
Pell count gives

\[
\Pr[A_y\text{ is square}]\le\frac{2B_D(N)}{H'}.
\]

If both local orders are odd, every global fibre is a singleton. Equal
\(y\)-coordinates then identify the same point and root. If exactly one
order is even, every global clean \(y\)-fibre has exactly two points. The
two points differ by one local sign, so their root ratio is mixed. There are
\(H'/2\) fibres and two ordered distinct pairs in each. Therefore

\[
\Pr[\text{useful duplicate}]
=\frac{(H'/2)\cdot2}{(H')^2}
=\frac1{H'}.
\]

The proof derives no lower bound for \(H'\). Such a bound must come from
separate information about \(m_p,m_q\), and \(W\).

## 8. A torus point and its inverse

For \(1\le y<N\), the inverse point has coefficient \(-y\bmod N=N-y\).
Direct expansion gives

\[
\begin{aligned}
A_yA_{N-y}
&=(1+D_0y^2)(1+D_0(N-y)^2)\\
&=(1-D_0y(N-y))^2+D_0N^2\\
&=C^2+D_0N^2.
\end{aligned}
\]

Also

\[
C\equiv1+D_0y^2\equiv x^2\pmod N.
\]

If the product is \(R^2\), then \(R>|C|\), and

\[
(R-C)(R+C)=D_0N^2.
\]

A positive divisor \(R-C\) of \(D_0N^2\) determines \(R+C\), hence \(C\).
There are at most \(\tau(D_0N^2)\) such choices. For each resulting \(C\),
the quadratic equation

\[
C=1-D_0y(N-y)
\]

has at most two integer roots. Thus at most
\(2\tau(D_0N^2)\) nonzero canonical \(y\)-values work.

Each raw \(y\)-fibre has four points, so the probability of the stated
nonzero event is at most

\[
\frac{8\tau(D_0N^2)}H.
\]

Under the powered coprime-image hypothesis, every fibre has at most two
points, giving

\[
\frac{4\tau(D_0N^2)}{H'}.
\]

Since \(D_0N^2<N^3\), its divisor count is \(2^{o(n)}\). The supplied roots
of the two rows multiply to \(x^2\equiv C\pmod N\). Hence an exact root
normalizes to \(R/C\bmod N\), a root of one. It factors exactly when mixed.
For \(y=0\), the point is its own inverse and the row product is the global
decoy one.

## 9. Conditional bank bounds

Apply the union bound to the one-row, duplicate, reciprocal, and inverse
events. This gives exactly the five displayed groups of estimates in the
conditional bank corollary. For the adaptive principal-lift claim, let
\(F_j\) be the useful event at stage \(j\). Conditional on every possible
past before the fresh coordinate,

\[
\Pr(F_j\mid\text{past})\le\frac2N.
\]

Taking expectations and summing gives

\[
\Pr\left(\bigcup_{j\le T}F_j\right)
\le\sum_{j\le T}\Pr(F_j)
\le\frac{2T}N.
\]

No independence is needed for this history-wise estimate.

Finally,

\[
T=2^{(\log n)^{O(1)}}=2^{o(n)},
\qquad
B_D(N)=2^{o(n)},
\qquad
S_M=2^{o(n)},
\qquad
\tau(D_0N^2)=2^{o(n)}.
\]

Also \(N,\varphi(N)=2^{n+O(1)}\). Thus \(K=2^{o(n)}\) makes each applicable
scalar numerator subexponential against an exponential denominator. The
explicit hypotheses \(H=2^{\Omega(n)}\) or \(H'=2^{\Omega(n)}\) do the same
for the torus bounds. Every applicable bank estimate is then
\(2^{-\Omega(n)}\).

## 10. Why the general multirow source remains open

Every proof above uses a rigid event: one row is a square, two rows are
equal, two scalar outputs are reciprocal modulo \(N^2\), a torus point is
paired with its inverse, or one fresh lift closes one product fixed in
advance. None of these arguments controls the ordinary integer prime-factor
parity of a product of unrelated distinct rows. The full nonduplicate
multirow problem, mixed-arm products, adaptive subset selection, and the
fixed canonical lift section therefore remain outside the theorem.
