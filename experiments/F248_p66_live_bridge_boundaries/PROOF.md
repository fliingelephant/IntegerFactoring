# Proofs for F248

## 1. P66 normalization

Suppose a positive exact integer value \(V\) has a supplied unit root
\(x\bmod N\), so that

\[
x^2\equiv V\pmod N.
\]

If \(V=s^2\) as an exact integer, then

\[
z=sx^{-1}\pmod N
\]

satisfies \(z^2=1\bmod N\).  For \(N=pq\), the four roots are the two global
roots \(\pm1\) and the two mixed CRT roots.  The usual gcd screens

\[
\gcd(s-x,N),\qquad \gcd(s+x,N)
\]

factor \(N\) exactly in the mixed cases.  This is the one-row specialization
of the P66 normalized-root decoder.

## 2. Uniform full scalar lifts

Let

\[
G=(\mathbb Z/N^2\mathbb Z)^\times.
\]

The local groups modulo \(p^2\) and \(q^2\) are cyclic of orders
\(p(p-1)\) and \(q(q-1)\).  Since \(\gcd(E,N)=1\),

\[
\gcd(E,p(p-1))=\gcd(E,p-1)=g_p
\]

and similarly on the \(q\)-side.  Therefore the kernel of the \(E\)-power
map on \(G\) has size

\[
K=g_pg_q,
\]

and its image has size

\[
|G^E|=\frac{\varphi(N^2)}K
=\frac{N\varphi(N)}K.
\]

A uniform input gives a uniform output on this image.

Every positive unit integer square below \(N^2\) is \(s^2\) for a unique unit
\(s\in\{1,\ldots,N-1\}\).  There are \(\varphi(N)\) such squares.  Some can
lie outside \(G^E\), so

\[
\Pr([A^E]_{N^2}\text{ is an exact square})
\le
\frac{\varphi(N)}{N\varphi(N)/K}
=\frac KN.
\]

### 2.1 Supplied roots inside one output fibre

Fix a square output \(s^2\).  Its preimages form one coset of the kernel of
the \(E\)-power map.  Changing a preimage by \(z\) in that kernel changes the
supplied root by

\[
\theta(z)=z^{E/2}\pmod N.
\]

On a local cyclic group of order \(r(r-1)\), the kernel has order
\(g_r=\gcd(E,r-1)\).  The size of its image under the \(E/2\)-power map is

\[
\frac{g_r}{\gcd(g_r,E/2)}.
\]

This quotient is two exactly when

\[
v_2(g_r)=v_2(E),
\]

which is equivalent to

\[
v_2(E)\le v_2(r-1).
\]

Otherwise the quotient is one.  Thus the local image is \(\{\pm1\}\) in the
first case and \(\{1\}\) in the second.

If at least one local side has image \(\{\pm1\}\), every coset of the global
image contains equally many global and mixed roots.  Exactly one half of the
preimages therefore factor through the P66 screen.

### 2.2 P209 specializations

The P209 family has

\[
\gcd(p-1,q-1)=2,
\quad
\gcd(p-1,q+1)=12,
\quad
\gcd(p+1,q-1)=2,
\quad
\gcd(p+1,q+1)=2.
\]

For \(E=N-1\), reduction modulo \(p-1\) and \(q-1\) gives

\[
g_p=g_q=2.
\]

Moreover \(N\equiv7\pmod8\), so \(v_2(E)=1\).  The family has
\(v_2(p-1)=2\) and \(v_2(q-1)=1\).  Both local sides are active.  The square
probability is at most \(4/N\), and its conditional factor probability is
exactly one half.

For \(E=N^2-1\),

\[
g_p=\gcd(p-1,q^2-1)=12,
\qquad
g_q=\gcd(q-1,p^2-1)=2.
\]

Thus the square probability is at most \(24/N\).  Here \(v_2(E)\ge4\), while
the two local valuations of \(r-1\) are two and one.  Both local images of
\(\theta\) are trivial, so the conditional half law must not be asserted.

## 3. The principal-lift fibre

Fix a unit residue \(a\bmod N\) and one lift \(a_0\).  The binomial theorem
modulo \(N^2\) gives

\[
(a_0+tN)^E
\equiv
a_0^E+Ea_0^{E-1}tN
\pmod{N^2}.
\]

If

\[
[A_t^E]_{N^2}=r+Nh_t,
\qquad r=[a^E]_N,
\]

then

\[
h_t=h_0+Ea^{E-1}t\pmod N.
\]

The coefficient \(Ea^{E-1}\) is a unit modulo \(N\), so this affine map
permutes all \(N\) lift digits.

Let

\[
x=[a^{E/2}]_N.
\]

The congruence

\[
s^2\equiv r=x^2\pmod N
\]

has exactly four solutions \(s\in\{1,\ldots,N-1\}\).  Their four distinct
integer squares satisfy

\[
0<s^2<N^2,
\qquad
s^2=r+Nh_s
\]

for four distinct digits \(h_s\in\{0,\ldots,N-1\}\).  Since the lift digit
runs through every value, these are exactly the four square outputs in the
principal fibre.

Two roots are congruent to \(\pm x\) and give global normalized roots.  The
other two roots are mixed and factor \(N\).  Hence the exact probabilities
are \(4/N\) for an integer square and \(2/N\) for a factor-bearing square.

### 3.1 Exact second-root equivalence

If a successful digit is known, its square output gives a positive root
\(s<N\) with

\[
s^2\equiv x^2\pmod N,
\qquad
s\not\equiv\pm x\pmod N.
\]

Then \(\gcd(s-x,N)\) or \(\gcd(s+x,N)\) is a proper factor.

Conversely, given \(p,q\), CRT combines opposite local signs of \(x\) to
construct the two mixed roots.  Squaring their canonical representatives
constructs the two successful lift digits.  Thus finding a successful digit
and finding a mixed second square root are polynomial-time equivalent when
\(a,E\), and the fibre are public.

This proof uses all lift coordinates uniformly.  It says nothing about the
single canonical coordinate \(t=0\).  In particular, no uniformity argument
proves that the canonical section avoids or prefers a mixed digit.

### 3.2 A fixed past product and one fresh lift

Let \(P>0\) be fixed independently of the fresh lift coordinate, assume
\(\gcd(P,N)=1\), and suppose a unit supplied root \(X\) is known with

\[
X^2\equiv P\pmod N.
\]

Write the integer squarefree decomposition

\[
P=d u^2,
\]

where \(d\) is positive and squarefree.  This decomposition is used only in
the proof; the decoder need not compute it.

Put

\[
B_t=[A_t^E]_{N^2}=r+Nh_t,
\qquad
x=[a^{E/2}]_N.
\]

If \(PB_t\) is an exact integer square, parity of every ordinary prime
valuation forces

\[
B_t=dv^2
\]

for some positive integer \(v\).  Since \(0<B_t<N^2\),

\[
0<v<\frac N{\sqrt d}\le N.
\]

Reduction modulo \(N\) gives

\[
dv^2\equiv r\equiv x^2\pmod N.
\]

Because \(X^2\equiv du^2\pmod N\), the coefficient \(d\) is a quadratic
residue on both prime sides.  The last congruence therefore has exactly four
CRT residue classes for \(v\bmod N\).  The interval \(0<v<N\) contains at
most one representative of each class.

The positive exact root of \(PB_t\) is

\[
S=duv.
\]

Its normalized root is

\[
z=S(Xx)^{-1}=duv(Xx)^{-1}\pmod N.
\]

Multiplication by the fixed unit \(du(Xx)^{-1}\) is injective.  It maps the
four possible \(v\)-classes into the four square roots of one.  At most two
classes have mixed image.  Each surviving integer \(v\) fixes

\[
h_t=\frac{dv^2-r}{N},
\]

and the affine digit permutation fixes one value of \(t\).  Hence at most two
fresh lift parameters produce a useful square, proving the conditional
bound \(2/N\).

This result permits any one past product fixed before the fresh lift.  It
does not permit a union bound over all \(2^T\) subsets of a retained
\(T\)-row bank, and it does not control a dependency selected after the
fresh integer factorization pattern is visible.

## 4. Canonical scalar duplicates

Let \(a,b\) be independent uniform units modulo \(N\), represented
canonically below \(N\).  If

\[
[a^E]_{N^2}=[b^E]_{N^2},
\]

then reduction modulo \(N\) gives

\[
(ab^{-1})^E=1\pmod N.
\]

The \(E\)-power kernel on \((\mathbb Z/N\mathbb Z)^\times\) has size
\(g_pg_q=K\).  For each \(b\), at most \(K\) choices of \(a\) can pass this
necessary condition.  Therefore

\[
\Pr([a^E]_{N^2}=[b^E]_{N^2})
\le\frac K{\varphi(N)}.
\]

If equality occurs, the ratio of the two supplied roots squares to one.  Its
mixed cases factor \(N\).

For a bank of size \(T\), the union bound multiplies the per-pair estimate by
at most \(\binom T2\).  On P209, \(K\) is four or 24 for the two stated
exponents, while \(\varphi(N)=2^{n-o(n)}\).  Every quasipolynomial \(T\) is
\(2^{o(n)}\), so the duplicate probability is \(2^{-\Omega(n)}\).

## 5. Reciprocal scalar outputs modulo \(N^2\)

Let

\[
u=[a^E]_{M},
\qquad
v=[u^{-1}]_M.
\]

If \(uv=R^2\) exactly, then

\[
R^2\equiv1\pmod M,
\qquad
0<R<M.
\]

There are exactly four canonical roots \(R\in\{1,\ldots,M-1\}\) of
\(1\bmod M\).  For a fixed such \(R\), the identity \(uv=R^2\) implies

\[
u\mid R^2,
\qquad
v=R^2/u.
\]

Thus the number of possible successful output values is at most

\[
\sum_{\substack{1\le R<M\\R^2\equiv1\ (\mathrm{mod}\ M)}}\tau(R^2).
\]

Since every \(R^2\) has \(O(n)\) bits, the standard divisor bound makes this
sum \(2^{o(n)}\).

For each fixed \(u\), equality \([a^E]_M=u\) implies a fixed \(E\)-power
residue modulo \(N\), and hence has at most \(K\) canonical base preimages.
On P209, \(K=O(1)\) and \(\varphi(N)=2^{n-o(n)}\).  The event probability is
therefore \(2^{-n+o(n)}\).

The supplied product root is one modulo \(N\).  Equivalently, any exact root
\(R\) is already a square root of one modulo \(N\).  A mixed \(R\) factors
through \(\gcd(R\pm1,N)\); a global \(R\) is a null relation.

This argument requires \(v\) to be the reciprocal of \(u\) modulo \(N^2\).
If \(b=[a^{-1}]_N\) is first chosen canonically and one instead uses
\([b^E]_{N^2}\), a principal-lift carry separates that output from
\([u^{-1}]_{N^2}\).  The bound above does not transfer to that pair.

## 6. Raw norm-one torus rows

The local norm-one torus over \(\mathbb F_r\) is cyclic of order

\[
m_r=r-\left(\frac Dr\right).
\]

Its points with \(x=0\) solve

\[
-Dy^2=1.
\]

Their number is

\[
z_r=1+\left(\frac{-D}{r}\right)\in\{0,2\}.
\]

After the unit-root screen, the global clean set is the product of the two
local clean sets and has size

\[
H=(m_p-z_p)(m_q-z_q).
\]

For every admitted local \(y\), the equation

\[
x^2=1+Dy^2
\]

has exactly two distinct nonzero roots \(\pm x\).  Therefore every admitted
global canonical \(y\) has exactly four clean global points.

### 6.1 Exact-square rows are Pell solutions

An exact square row satisfies

\[
1+D_0y^2=R^2,
\]

or

\[
R^2-D_0y^2=1.
\]

If \(D_0=d^2\), then

\[
(R-dy)(R+dy)=1.
\]

Both factors are positive integers, so both are one and \(y=0\).  Set
\(B_D(N)=1\) in this case.

Suppose \(D_0\) is nonsquare.  All nonnegative Pell solutions are powers of
the least positive unit

\[
\varepsilon=R_1+y_1\sqrt{D_0}>2\sqrt{D_0}.
\]

For \(0\le y<N\),

\[
R+y\sqrt{D_0}<2N\sqrt{D_0}+1.
\]

Consequently the number of possible \(y\)-values is at most

\[
B_D(N)=1+
\left\lfloor
\frac{\log(2N\sqrt{D_0}+1)}{\log(2\sqrt{D_0})}
\right\rfloor
=O(n).
\]

Each such \(y\) has four clean points, proving the probability bound
\(4B_D(N)/H\).

### 6.2 Duplicate raw rows

Since \(D_0>0\) and canonical \(y\)-coordinates are nonnegative,

\[
1+D_0y_1^2=1+D_0y_2^2
\quad\Longleftrightarrow\quad
y_1=y_2.
\]

There are \(H/4\) admitted global \(y\)-values, each with four points.  Two
independent uniform points therefore have equal rows with probability

\[
\frac{H}{4}\left(\frac4H\right)^2=\frac4H.
\]

For each first point in one four-point fibre, exactly two second points change
the local sign on one prime side and not the other.  These are exactly the
mixed normalized-root cases.  Hence the useful duplicate probability is

\[
\frac{(H/4)\cdot4\cdot2}{H^2}=\frac2H.
\]

## 7. Powered torus rows

Powering a uniform local cyclic torus maps it uniformly onto its image
subgroup.  Let the two image orders be \(r_p,r_q\), and suppose

\[
\gcd(r_p,r_q)=1.
\]

After deleting image points with \(x=0\), the clean image size is

\[
H'=(r_p-z'_p)(r_q-z'_q),
\qquad z'_p,z'_q\in\{0,2\}.
\]

### 7.1 Fibre size

For a local point \(U=(x,y)\), the other possible point with the same \(y\)
is

\[
(-x,y)=-U^{-1}.
\]

It belongs to the same cyclic image subgroup exactly when \(-1\) belongs to
that subgroup, which is exactly when its order is even.  Once \(x=0\) points
are removed, every admitted local \(y\)-fibre therefore has size two for even
image order and size one for odd image order.

The coprimality of \(r_p,r_q\) permits at most one even local order.  Every
global clean \(y\)-fibre has size at most two.  The Pell count from Section 6
therefore gives

\[
\Pr[A_y\text{ exact square}]\le\frac{2B_D(N)}{H'}.
\]

If both local orders are odd, equality of \(y\) means equality of the whole
point, so repeated rows give only the same supplied root.

If exactly one local order is even, every global \(y\)-fibre has size two.
The two distinct points differ by a sign only on that local side, so their
root ratio is mixed.  There are \(H'/2\) fibres and two ordered distinct pairs
per fibre.  Thus

\[
\Pr[\text{useful duplicate}]
=\frac{(H'/2)\cdot2}{(H')^2}
=\frac1{H'}.
\]

### 7.2 P209 size lower bound

For the P208/P209 square exponent \(N^2-1\), the powered residual orders in
each orientation are coprime.  Each local residual retains its corresponding
private P209 marker, and those markers have \(\Omega(n)\) bits.  P209 gives
the same marker retention for its covered numerical-QP signed-power grammar.
Deleting at most two points per side does not change the exponential scale.
Hence, in these stated cases,

\[
H'=2^{\Omega(n)}.
\]

The marker conclusion is not claimed for an arbitrary powering exponent.
The same exponential conclusion holds for the raw clean size \(H\).  A
quasipolynomial-size bank has \(2^{o(n)}\) rows and pairs, so all one-row and
duplicate bounds remain exponentially negligible after a union bound.

## 8. A torus point and its inverse

For \(1\le y<N\), the inverse torus point has coefficient \(-y\bmod N=N-y\).
Define

\[
A_y=1+D_0y^2,
\qquad
A_{N-y}=1+D_0(N-y)^2,
\qquad
C=1-D_0y(N-y).
\]

Direct expansion gives

\[
A_yA_{N-y}-C^2
=D_0\bigl(y+(N-y)\bigr)^2
=D_0N^2.
\]

Thus

\[
A_yA_{N-y}=C^2+D_0N^2.
\]

Also

\[
C\equiv1+D_0y^2\equiv x^2\pmod N.
\]

If the product is an exact square \(R^2\), then

\[
(R-C)(R+C)=D_0N^2.
\]

Because \(R^2-C^2>0\), both factors are positive.  Every solution therefore
gives a positive divisor pair of \(D_0N^2\).  There are at most
\(\tau(D_0N^2)\) such pairs.  Each resulting value of \(C\) gives at most two
integer solutions of

\[
C=1-D_0y(N-y).
\]

Hence at most \(2\tau(D_0N^2)\) canonical \(y\)-values can close this pair to
an exact square.

The raw torus has four points per admitted \(y\), which gives the bound

\[
\frac{8\tau(D_0N^2)}H.
\]

The powered coprime image has at most two points per admitted \(y\), which
gives

\[
\frac{4\tau(D_0N^2)}{H'}.
\]

Since \(D_0N^2<N^3\), the divisor bound gives

\[
\tau(D_0N^2)=2^{o(n)}.
\]

The raw probability is \(2^{-\Omega(n)}\) on P209.  The powered probability
has the same bound in the P208/P209 square-exponent and covered signed-power
cases from Section 7.2.

The supplied roots of the two rows multiply to \(x^2\), while
\(C\equiv x^2\pmod N\).  Therefore an exact root has normalized root

\[
RC^{-1}\pmod N.
\]

It is a square root of one.  The mixed cases factor; the global cases are
null.

## 9. Why the general P66 source remains open

The preceding arguments use one of three rigid features:

1. one row is forced to solve one Pell or square-root equation;
2. two rows are exactly equal;
3. two rows are linked by an explicit reciprocal or inverse-point identity.

A general P66 dependency instead asks whether a product of several distinct
integer rows is an exact square after gcd-free refinement.  The P209 private
markers describe orders in hidden local source groups.  They do not describe
the ordinary integer prime factors of the rows.  P106 decodes that integer
parity structure once it is present, but it does not supply a theorem that
connects it to the P209 order markers.

Therefore no argument in this packet bounds the normalized-root image of the
full nonduplicate multirow parity kernel.  Such dependencies, and a possible
bias in the fixed canonical scalar section, remain live.
