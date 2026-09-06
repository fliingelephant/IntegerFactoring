# F248 V2 — Blind statement-only reconstruction

## Verdict

**PASS.** The claims in `V2_STATEMENT.md` follow from the arguments below.
Before reading it, I authenticated the statement at SHA-256
`57ea62c39ce0e04b4a271135e613eabdcf79a32dd5df85dc692effb6dc8d8504`,
which matched the required digest.
This reconstruction used only that statement, the root prompt, and the root
agent instructions. It used no numerical experiment.

Throughout, write \(U_m=(\mathbb Z/m\mathbb Z)^\times\). All probabilities
are with respect to the distributions specified in the statement.

## Preliminary facts

### Power maps

For an odd prime \(r\), the group \(U_{r^2}\) is cyclic of order
\(r(r-1)\). Since \(\gcd(E,r)=1\), the kernel of the \(E\)-power map on
\(U_{r^2}\) has size

\[
\gcd(E,r(r-1))=\gcd(E,r-1)=g_r.
\]

The Chinese remainder theorem therefore gives

\[
\left|\ker(z\mapsto z^E\text{ on }U_{N^2})\right|=g_pg_q=K.
\]

Every nonempty fibre of a group homomorphism is a coset of its kernel. Thus
the \(E\)-power image in \(U_{N^2}\) has size

\[
\frac{\varphi(N^2)}K=\frac{N\varphi(N)}K,
\]

and a uniform input induces the uniform distribution on this image.

### Mixed roots split \(N\)

If \(u^2\equiv1\pmod N\), its two local values modulo \(p,q\) are each
\(1\) or \(-1\). If the signs are mixed, exactly one of \(p,q\) divides
\(u-1\), and the other divides \(u+1\). Consequently, if \(s^2\equiv
x^2\pmod N\) and \(s/x\) is mixed, then

\[
\gcd(s-x,N),\qquad \gcd(s+x,N)
\]

are the two nontrivial complementary prime factors. For global signs the
same gcds are trivial and \(N\), in some order.

### A uniform divisor bound

If positive integers \(m_n\) satisfy \(m_n\le 2^{cn}\) for a fixed \(c\),
then

\[
\tau(m_n)=2^{o(n)}
\]

uniformly in the choice of \(m_n\). To see this, fix \(\epsilon>0\) and
factor \(m=\prod \ell^{a_\ell}\). Choose a constant prime threshold so
large that, above it,

\[
a+1\le 2^a\le \ell^{\epsilon a/(2c)}.
\]

The contribution from primes above the threshold is at most
\(m^{\epsilon/(2c)}\le2^{\epsilon n/2}\). There are only a fixed number
of primes below the threshold, and each corresponding \(a+1\) is
\(O(n)\). Their product is polynomial in \(n\), with a degree depending
only on \(\epsilon,c\), and is at most \(2^{\epsilon n/2}\) for all
sufficiently large \(n\). Since \(\epsilon\) was arbitrary, the claim
follows.

## Reconstruction of Theorem A

An exact-square value \(L=s^2\) in \(\{1,\ldots,N^2-1\}\) has
\(1\le s<N\). Since \(L\) is a unit, \(s\) is a unit modulo \(N\). There
are exactly \(\varphi(N)\) possible such integers \(s\). The output is
uniform on an image of size \(N\varphi(N)/K\), so

\[
\Pr[L\text{ is an integer square}]
 \le \frac{\varphi(N)}{N\varphi(N)/K}
 =\frac KN.
\]

Now fix a square output \(s^2\) that lies in the image, and fix one of its
preimages \(A_0\). Conditioned on this output, \(A\) is uniform on
\(A_0\ker(z\mapsto z^E)\). Hence the supplied roots are uniform on the
coset

\[
A_0^{E/2}\,
\operatorname{im}\left(
 z\mapsto z^{E/2}\pmod N,
 \ z\in\ker(z\mapsto z^E\pmod {N^2})
\right).
\]

It remains to determine the local image. Put \(a=v_2(E)\ge1\). On the
\(r\)-side every kernel element \(z\) satisfies
\((z^{E/2})^2=1\), so the image is contained in \(\{1,-1\}\). If
\(2^a\mid r-1\), the kernel contains an element of order \(2^a\); its
\(E/2\)-th power is \(-1\), because the odd part of \(E\) does not change
the unique element of order two. Thus the image is \(\{1,-1\}\). If
\(2^a\nmid r-1\), the full 2-primary part of the kernel has order at most
\(2^{a-1}\), while its odd part divides the odd part of \(E\). The exponent
\(E/2\) kills both parts, so the image is \(\{1\}\). Therefore

\[
\operatorname{im}_r=\{1,-1\}
\quad\Longleftrightarrow\quad
v_2(E)\le v_2(r-1).
\]

After division by \(s\), the possible supplied roots form a coset inside
the four CRT sign vectors. The kernel and its image split as products of
the two local kernels and images. If at least one local image is
\(\{1,-1\}\), the relevant coset either varies one sign or varies both
signs independently. In either case exactly half of its elements have
mixed signs. A homomorphism has equal-size fibres over its image, so exactly
half of the original preimages yield a mixed normalized root. The gcd
argument above then factors \(N\).

## Reconstruction of Theorem B

The binomial theorem modulo \(N^2\) gives

\[
(a_0+tN)^E\equiv a_0^E+Ea_0^{E-1}tN\pmod {N^2}.
\]

After writing the least representative as \(r+Nh_t\), this becomes

\[
h_t\equiv h_0+Ea^{E-1}t\pmod N.
\]

The coefficient is a unit modulo \(N\), because both \(E\) and \(a\) are
units. Hence \(t\mapsto h_t\) is a bijection of the \(N\) residue classes.
The values \(r+Nh_t\) consequently run once through all integers in
\(\{1,\ldots,N^2-1\}\) that are congruent to \(r\) modulo \(N\).

Since \(r\equiv x^2\pmod N\) and \(x\) is a unit, the congruence
\(s^2\equiv r\pmod N\) has exactly four solutions: choose either sign of
\(x\) independently modulo \(p\) and modulo \(q\). Each has a unique
representative \(s\in\{1,\ldots,N-1\}\). Its integer square is
\(r+Nh\) for a unique \(h\in\{0,\ldots,N-1\}\). Conversely, every exact
square in the fibre arises in this way. Thus exactly four \(t\)'s give an
exact square. Of the four normalized roots \(s/x\), two are mixed and two
are global. This proves the probabilities \(4/N\) and \(2/N\).

The asserted polynomial equivalence is explicit. From a useful digit
\(h\), compute the integer square root of \(r+Nh\); its residue is a mixed
second square root of \(r\). Conversely, from a mixed square root
\(s\bmod N\), take its representative in \(\{1,\ldots,N-1\}\), compute

\[
h=\frac{s^2-r}{N},
\qquad
t\equiv (Ea^{E-1})^{-1}(h-h_0)\pmod N.
\]

All of these are polynomial-time integer operations. Given \(p,q\), CRT
combines opposite local signs of \(x\) to construct the two mixed roots;
the displayed formulas then construct both useful digits and lift
coordinates.

### Fixed-past extension

Write the fixed positive integer \(P\) uniquely as

\[
P=c^2d,
\]

where \(d\) is squarefree. If \(PB_t=s^2\), then \(c\mid s\). Writing
\(s=cz\) gives \(dB_t=z^2\). Squarefreeness of \(d\) then gives
\(z=dv\), and hence

\[
B_t=dv^2,\qquad s=cdv.
\]

Because \(B_t<N^2\), every such \(v\) satisfies \(0<v<N/\sqrt d\le N\).
As \(\gcd(P,N)=1\), both \(c\) and \(d\) are units modulo \(N\). Put
\(Y=Xc^{-1}\pmod N\); then \(Y^2\equiv d\pmod N\). The normalized root is

\[
\frac{s}{Xx}
 \equiv \frac{cdv}{cYx}
 \equiv \frac{Yv}{x}\pmod N,
\]

where \(d/Y\equiv Y\). Among the four residue classes of \(v\) satisfying
\(dv^2\equiv x^2\pmod N\), precisely two make \(Yv/x\) mixed. The interval
\(0<v<N/\sqrt d\) contains at most one representative of each residue
class modulo \(N\). Thus at most two values of \(v\), hence at most two
values of \(B_t\), occur. Since \(t\mapsto B_t\) is injective, at most two
fresh lift coordinates are useful. A uniform fresh \(t\) therefore has
conditional probability at most \(2/N\), for every fixed past.

This count fixes \(P\) before sampling \(t\). If a product can be selected
from exponentially many choices after the row is visible, there are
exponentially many possible \(P\)'s and the two-candidate count for one
fixed \(P\) gives no stated bound. Likewise, the proof uses a uniform
coordinate over the whole lift fibre. It says nothing probabilistic about
the single deterministic section \(t=0\).

## Reconstruction of Theorem C

Fix \(b\in U_N\). If \(u(a)=u(b)\), then in \(U_{N^2}\)

\[
(ab^{-1})^E=1.
\]

The kernel has \(K\) elements. For each kernel element there is at most one
integer \(a\in\{1,\ldots,N-1\}\) with the required residue modulo \(N^2\).
Thus at most \(K\) canonical values of \(a\) can collide with a fixed
\(b\). Averaging over the \(\varphi(N)\) possible \(b\)'s proves

\[
\Pr[u(a)=u(b)]\le\frac K{\varphi(N)}.
\]

For a collision, the displayed supplied-root ratio has square one modulo
\(N\). The preliminary gcd argument proves that it factors \(N\) exactly
when its CRT signs are mixed.

## Reconstruction of Theorem D

If \(uv=R^2\) as integers, then \(1\le R<N^2=M\), because \(u,v<M\).
Also \(uv\equiv1\pmod M\), so \(R\in\mathcal R_M\). For a fixed \(R\),
the integer \(u\) must divide \(R^2\); there are at most
\(\tau(R^2)\) possibilities. The total number of possible favorable output
values \(u\) is therefore at most

\[
S_M=\sum_{R\in\mathcal R_M}\tau(R^2).
\]

Each output of the \(E\)-power map has \(K\) preimages in all of
\(U_{N^2}\), and consequently at most \(K\) preimages in the smaller set of
canonical bases \(1\le a<N\). Hence

\[
\Pr[uv\text{ is an integer square}]
\le\frac{KS_M}{\varphi(N)}.
\]

For an odd prime power, the only square roots of one are \(1,-1\): from
\((R-1)(R+1)\equiv0\pmod{r^2}\) and
\(\gcd(R-1,R+1)\mid2\), all of \(r^2\) divides one factor. CRT therefore
gives four elements of \(\mathcal R_M\). Since every \(R^2<N^4\le2^{4n}\),
the uniform divisor bound gives \(\tau(R^2)=2^{o(n)}\), and a sum of four
such terms is still \(2^{o(n)}\).

The exact root \(R\), divided by the supplied product root \(1\pmod N\),
is itself a square root of one; it factors \(N\) exactly in the mixed case.
The argument used the identity \(v=[u^{-1}]_{N^2}\), which forces
\(uv\equiv1\pmod {N^2}\). If instead one first takes the canonical inverse
of \(a\) modulo \(N\) and powers that integer, its lift need not be the
inverse of \(a\) modulo \(N^2\). The forcing congruence can fail, so this
theorem does not cover that different pair.

## Torus facts

Over a prime field, identify a point \((x,y)\) with \(x+y\sqrt D\), and use
multiplication in the quadratic algebra. Its norm is \(x^2-Dy^2\), and
inversion on the norm-one group is

\[
(x,y)^{-1}=(x,-y).
\]

If \(D\) is a square modulo \(r\), the quadratic algebra splits and the
norm-one group is isomorphic to \(\mathbb F_r^\times\), of order \(r-1\).
If \(D\) is a nonsquare, it is \(\mathbb F_{r^2}\), and the kernel of the
field norm to \(\mathbb F_r^\times\) has order \(r+1\). These groups are
cyclic. In both cases the order is

\[
m_r=r-\left(\frac Dr\right).
\]

A local point fails cleanliness exactly when \(x=0\). Then
\(-Dy^2=1\), which has

\[
1+\left(\frac{-D}{r}\right)=z_r
\]

solutions. CRT makes the two local choices independent, so the number of
clean global points is

\[
H=(m_p-z_p)(m_q-z_q).
\]

For any clean point, the torus equation gives

\[
x^2\equiv 1+D_0y^2=A_y\pmod N.
\]

### Counting integer Pell rows

We next show that at most \(B_D(N)\) canonical values \(0\le y<N\) make
\(1+D_0y^2\) an integer square.

If \(D_0=d^2\) is an integer square, then

\[
s^2-d^2y^2=(s-dy)(s+dy)=1.
\]

Both factors are positive integers, so both equal one and \(y=0\). This
gives the stated value \(B_D(N)=1\).

Suppose \(D_0\) is not a square. For a positive solution \(y>0\), put

\[
\alpha=s+y\sqrt{D_0}.
\]

It has norm one. If \(\alpha_2>\alpha_1>1\) come from two solutions, then
\(\alpha_2/\alpha_1=a+b\sqrt{D_0}\), where \(a,b\) are integers, its norm
is one, and it is greater than one. Its conjugate is its reciprocal, so
\(a>0\) and \(b>0\). Hence

\[
\frac{\alpha_2}{\alpha_1}
=a+b\sqrt{D_0}>2b\sqrt{D_0}\ge2\sqrt{D_0}.
\]

The same lower bound holds for the first positive norm-one unit. On the
other hand, \(s<1+y\sqrt{D_0}\), and \(y<N\), so

\[
\alpha<1+2N\sqrt{D_0}.
\]

If there are \(k\) positive solutions ordered by \(\alpha\), then

\[
(2\sqrt{D_0})^k<1+2N\sqrt{D_0}.
\]

Thus \(k\) is at most the floor in the definition of \(B_D(N)\). Adding
the solution \(y=0\) proves the asserted count.

Finally, \(D_0<N\), the numerator in the defining logarithmic ratio is
\(O(\log N)\), and its denominator is at least the positive constant
\(log2\). Therefore \(B_D(N)=O(n)\), uniformly in \(D_0\).

## Reconstruction of Theorem E

For any fixed canonical \(y\) that occurs in a clean raw point,
\(x^2\equiv A_y\pmod N\) has two roots on each prime side. All four CRT
roots are units and give clean torus points. Thus every occurring \(y\) has
exactly four points above it.

There are at most \(B_D(N)\) integer-square \(y\)'s by the Pell count, so
there are at most \(4B_D(N)\) favorable clean points. This proves

\[
\Pr[A_y\text{ is an integer square}]\le\frac{4B_D(N)}H.
\]

Because \(D_0>0\) and both coordinates lie in \(\{0,\ldots,N-1\}\),
\(A_{y_1}=A_{y_2}\) as integers if and only if \(y_1=y_2\). If
\(\mathcal Y\) is the set of occurring \(y\)'s, then \(H=4|\mathcal Y|\).
For two independent points, the number of ordered duplicate pairs over
each \(y\) is \(4^2\), giving

\[
\Pr[A_{y_1}=A_{y_2}]
=\frac{|\mathcal Y|16}{H^2}=\frac4H.
\]

Fixing the first of the four roots, exactly two of the four choices for the
second have a mixed ratio. There are therefore \(4\cdot2=8\) useful
ordered pairs over each \(y\), and

\[
\Pr[\text{useful duplicate}]
=\frac{|\mathcal Y|8}{H^2}=\frac2H.
\]

## Reconstruction of Theorem F

On a cyclic local torus group of order \(m_r\), the \(W\)-power image has
order

\[
\rho_r=\frac{m_r}{\gcd(m_r,W)}.
\]

A uniform input maps uniformly onto this subgroup. The points with \(x=0\)
in the subgroup come in inverse pairs \((0,y),(0,-y)\), so their number
\(z'_r\) is either zero or two. Conditioning the global image point on
cleanliness leaves the uniform distribution on the Cartesian product of
the two clean local image sets. Its size is

\[
H'=(\rho_p-z'_p)(\rho_q-z'_q).
\]

For a fixed clean local \(y\), the two possible points are
\(g=(x,y)\) and

\[
(-x,y)=(-1,0)g^{-1}.
\]

The second belongs to the image subgroup exactly when \((-1,0)\) belongs
to it. In a cyclic group this happens exactly when the subgroup order
\(\rho_r\) is even. Thus a clean local \(y\) has one image point above it
when \(\rho_r\) is odd and two when \(\rho_r\) is even. Since
\(\gcd(\rho_p,\rho_q)=1\), at most one local image order is even. Every
occurring global \(y\) consequently has at most two clean powered points
above it. Combining this with the Pell count gives

\[
\Pr[A_y\text{ is an integer square}]\le\frac{2B_D(N)}{H'}.
\]

If both local orders are odd, every global \(y\) has one powered point
above it. Equal coordinates then mean the two powered points are identical,
and the supplied-root ratio is the global root \(1\), not a second root.

If exactly one local order is even, every occurring global \(y\) has
exactly two powered points above it. They differ by the sign of \(x\) on
that one prime side and agree on the other, so the two distinct ordered
choices are useful. Writing \(|\mathcal Y'|=H'/2\), the useful-pair
probability is

\[
\frac{|\mathcal Y'|\,2}{H'^2}=\frac1{H'}.
\]

The formula for \(\rho_r\) itself shows why no lower bound on \(H'\) follows
for arbitrary \(W\): choosing \(W\) divisible by a local group order can
collapse that image to the identity subgroup. The identity is clean, but
the resulting clean image can be constant-sized.

## Reconstruction of Theorem G

The inverse of \((x,y)\) has coefficient \(-y\pmod N\), whose canonical
representative is \(N-y\) when \(1\le y<N\). Direct expansion gives

\[
(1+D_0y^2)(1+D_0(N-y)^2)
=\bigl(1-D_0y(N-y)\bigr)^2+D_0N^2.
\]

This proves the boxed identity with \(C=1-D_0y(N-y)\). Also

\[
C\equiv1+D_0y^2\equiv x^2\pmod N.
\]

If the product is \(R^2\), then \(R>|C|\), and therefore

\[
U=R-C>0,\qquad V=R+C>0,\qquad UV=D_0N^2.
\]

There are at most \(\tau(D_0N^2)\) ordered choices \((U,V)\), because \(U\)
determines \(V\). Each determines \(C=(V-U)/2\). The equation

\[
C=1-D_0y(N-y)
\]

is quadratic in \(y\), so it has at most two integer solutions. Hence at
most \(2\tau(D_0N^2)\) nonzero canonical \(y\)'s give an exact square.

In the raw torus every occurring clean \(y\) has four points above it, so
the probability is at most

\[
\frac{8\tau(D_0N^2)}H.
\]

Under the powered hypotheses, every occurring clean \(y\) has at most two
points above it, so the corresponding probability is at most

\[
\frac{4\tau(D_0N^2)}{H'}.
\]

Since \(D_0N^2<N^3\le2^{3n}\), the uniform divisor bound gives
\(\tau(D_0N^2)=2^{o(n)}\).

The two factors \(A_y,A_{N-y}\) have supplied roots \(x,x\), because group
inversion negates \(y\) but preserves \(x\). Their supplied product root is
\(x^2\equiv C\pmod N\), which is a unit by cleanliness. Thus \(R/C\) is a
square root of one modulo \(N\), and the preliminary gcd argument factors
\(N\) exactly when it is mixed. At \(y=0\), both rows are \(A_0=1\); the
exact root and supplied root are global. This is the excluded decoy.

## Reconstruction of the conditional bank corollary

Apply the union bound to the preceding one-row or one-pair estimates.

* Theorem A gives \(TK/N\) for \(T\) uniform full scalar lifts.
* At adaptive principal-lift stage \(j\), condition on the complete past.
  Its past product is then fixed before the fresh uniform coordinate, so
  the fixed-past extension gives conditional probability at most \(2/N\).
  Summing over stages gives \(2T/N\); no independence is needed.
* There are \(\binom T2\) pairs of independent canonical bases. Theorem C
  gives \(\binom T2K/\varphi(N)\). Applying Theorem D separately to each
  base gives \(TKS_M/\varphi(N)\) for reciprocal-output square pairs.
* For raw torus points, Theorems E and G give respectively
  \(4TB_D(N)/H\), \(2\binom T2/H\), and
  \(8T\tau(D_0N^2)/H\).
* Under the powered hypotheses, Theorems F and G give respectively
  \(2TB_D(N)/H'\), either zero or \(\binom T2/H'\), and
  \(4T\tau(D_0N^2)/H'\).

The inverse-pair bounds concern the nonzero, potentially useful case stated
in Theorem G; the omitted \(y=0\) case is the identified global decoy.

For the asymptotic conclusion, \(n=\lceil\log_2(N+1)\rceil\) implies
\(N\ge2^{n-1}\). Also

\[
\varphi(N)=N(1-1/p)(1-1/q)=2^{\Omega(n)}
\]

(indeed the product of the two parenthetical factors is bounded below by
an absolute positive constant for distinct odd primes). A quantity
\(T=2^{(\log n)^{O(1)}}\) satisfies \(T=2^{o(n)}\), as does \(T^2\).
Under the stated assumptions, \(K,S_M,\tau(D_0N^2)\), and \(B_D(N)\) are
all \(2^{o(n)}\). Dividing any applicable bank numerator by \(N\),
\(\varphi(N)\), or an assumed \(H,H'=2^{\Omega(n)}\) therefore gives

\[
2^{-\Omega(n)}.
\]

This is conditional: these arguments neither select an exponent with the
required image size nor construct a source family satisfying all needed
hypotheses.

## Reconstruction of the exact boundary

Each estimate uses a rigid equation that is absent outside its stated
event class:

1. A one-row estimate counts either power-map image values or integer Pell
   solutions.
2. A duplicate estimate uses literal equality, which collapses a pair to a
   kernel element or to one common \(y\)-coordinate.
3. The scalar reciprocal-output estimate uses \(uv\equiv1\pmod{N^2}\),
   forcing its integer square root into the four-element set
   \(\mathcal R_M\).
4. The torus inverse estimate uses the exact identity
   \(A_yA_{N-y}=C^2+D_0N^2\), which turns the event into a divisor-pair
   count.
5. The principal-lift extension fixes one past product before one fresh
   uniform lift coordinate, leaving at most two useful coordinates.

An unrelated nonduplicate pair has none of the equality, reciprocal, or
inverse equations. A mixed scalar–torus relation likewise has no equation
proved here. Selecting a subset after seeing many rows introduces as many
past products as there are selectable subsets, so the one-fixed-product
bound does not control that event. A general multirow integer-prime parity
dependency is not a union of the five rigid events above. The fixed
canonical lift \(t=0\) is not a uniform fibre sample. Finally, powering the
canonical inverse base modulo \(N\) is not the same operation as taking the
output inverse modulo \(N^2\).

The results are upper bounds for these specified mechanisms. They neither
show that some mechanism succeeds often enough to factor every input nor
exclude success through the uncontrolled relations. Consequently they give
no all-input factoring algorithm and no unconditional quasipolynomial
success or failure theorem.
