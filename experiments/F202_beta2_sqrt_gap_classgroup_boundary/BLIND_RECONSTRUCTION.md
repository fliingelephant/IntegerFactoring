# F202 blind reconstruction

## Source restriction, hash, and verdict

Before opening the frozen statement, I obtained the SHA-256 digest

    266e527434b5c6b9f3a680b0ea31498cd8f55411d1ec75a459f4d8bd21587719

which matches the required value. This reconstruction uses only the root
PROMPT.md and the frozen F202 STATEMENT.md. It uses no numerical search.

**Verdict: pass for all self-contained numbered mathematical claims, with
the scope qualifications already stated by F202.** In particular:

- The square-gap identities, bounds, gcd branch, mixed-root equivalence,
  factor-supported congruence identity, proper ideal-class calculation, and
  the complete \(N=2627\) certificate all reconstruct exactly.
- The ideal argument remains valid when
  \(\mathbb Z[\sqrt{-E}]\) is nonmaximal. The key point is that \(p\) and
  \(q\) are coprime to the order discriminant, and hence to the conductor;
  the prime ideals used in the argument are therefore proper and invertible.
- The recursion estimate is valid provided there is a recursive factoring
  routine whose domain includes the arbitrary smaller integer \(E\). The
  promised-semiprime postprocessor alone does not define such a routine on
  arbitrary \(E\), so this is recursion accounting, not a standalone
  factoring algorithm.
- The references to what P175 proves cannot be independently checked from
  the permitted sources. They are not needed for Theorems 1--5.
- The final list of four gates is valid as a list of exact interfaces or
  possible routes. It is not proved to be an exhaustive classification of
  the internal operation of every possible postprocessor. Extensionally,
  however, any successful factorer can compute both the correct \(d\) and a
  mixed root after it has obtained \(p,q\).

Thus F202 is a rigorous boundary theorem on its stated promise. It does not
supply the unrestricted quasipolynomial factoring algorithm required by
PROMPT.md.

## 1. Exact square-gap coordinates

Let

\[
a=B-p,\qquad c=q-B,\qquad d=c-a=p+q-2B.
\]

Because \(p<\sqrt{pq}<q\) and \(\sqrt{pq}\) is not an integer,

\[
p\leq B<q.
\]

Consequently \(a\geq0\) and \(c>0\). The arithmetic-geometric mean
inequality is strict because \(p\ne q\):

\[
p+q>2\sqrt{pq}\geq2B.
\]

Hence \(d>0\). Both \(p+q\) and \(2B\) are even, so \(d\) is an even
integer; in fact \(d\geq2\).

Using \(p=B-a\), \(q=B+c\), and \(d=c-a\), direct expansion gives

\[
\begin{aligned}
E
 &=pq-B^2\\
 &=(B-a)(B+c)-B^2\\
 &=B(c-a)-ac\\
 &=Bd-ac.
\end{aligned}
\]

The other two identities follow without approximation:

\[
\begin{aligned}
a^2+E
 &=(B-p)^2+pq-B^2\\
 &=p(p+q-2B)=pd,
\\[2mm]
c^2+E
 &=(q-B)^2+pq-B^2\\
 &=q(p+q-2B)=qd.
\end{aligned}
\]

Finally,

\[
\begin{aligned}
d^2+4Bd-4E
 &=(d+2B)^2-4(B^2+E)\\
 &=(p+q)^2-4pq\\
 &=(q-p)^2.
\end{aligned}
\]

The bounds are also exact. Since \(B\geq p\),

\[
d=p+q-2B\leq q-p.
\]

The balance condition gives \(q-p<p\). Positivity gives
\(1\leq d\), with the stronger bound \(2\leq d\). Since

\[
B^2<N<(B+1)^2,
\]

\[
1\leq E=N-B^2<2B+1,
\]

and integrality yields \(E\leq2B\).

If the correct \(d\) is known, set

\[
s=2B+d=p+q,\qquad
\Delta=d^2+4Bd-4E.
\]

The square test gives \(\sqrt\Delta=q-p\), and then

\[
p=\frac{s-\sqrt\Delta}{2},
\qquad
q=\frac{s+\sqrt\Delta}{2}.
\]

Equivalently, these are the roots of \(X^2-sX+N\). Thus the correct \(d\)
is an exact factoring primitive.

### Gcd branch

Euclid's identity gives

\[
\gcd(E,N)
 =\gcd(N-B^2,N)
 =\gcd(B^2,N).
\]

Since \(0<E<N\), any value strictly larger than \(1\) is a proper divisor
of \(N\). On the other branch, \(\gcd(E,N)=1\), and the displayed equality
implies \(\gcd(B^2,N)=1\), hence \(\gcd(B,N)=1\).

### Bit contraction

It remains to justify the full one-bit decrease, rather than merely
\(E=O(\sqrt N)\). If \(p=3\), the promise forces \(q=5\), and
\((N,B,E)=(15,3,6)\), so \(E\) has three bits while \(N\) has four.
If \(p\geq5\), then \(B\geq5\), and

\[
E\leq2B<\frac{B^2}{2}\leq\frac N2.
\]

For the defined input length, \(N<2^n\); hence in every case
\[
E<2^{n-1}.
\]
Therefore \(E\) has at most \(n-1\) bits.

Suppose an overall recursive routine can factor this arbitrary child and a
uniform postprocessor then costs

\[
Q(n)=2^{C(\log_2(n+1))^k}
\]

for fixed \(C>0\), \(k\geq1\). If its cost satisfies

\[
T(n)\leq T(n-1)+Q(n),
\]

then monotonicity of \(Q\) gives

\[
T(n)\leq T(n_0)+nQ(n).
\]

Writing \(L=\log_2(n+1)\), one has
\(n\leq2^L\leq2^{L^k}\) for \(L\geq1\). Thus the extra factor \(n\) can be
absorbed by increasing the fixed constant in the exponent, and \(T\) is
numerical QP.

This proves the accounting implication. It does not create a recursive
algorithm on all inputs: \(E\) need not itself be a balanced squarefree
semiprime. A complete use of this recurrence must supply a factoring routine
defined on such arbitrary smaller children, or an explicit general-to-promise
reduction.

## 2. Mixed-root and norm interfaces

On the coprime branch, \(\gcd(B,N)=1\), and the definition of \(E\) gives

\[
B^2\equiv-E\pmod N.
\]

Modulo each of the odd primes \(\ell=p,q\), \(B\) is nonzero. Therefore
\[
X^2\equiv B^2\pmod\ell
\]
has exactly the two distinct roots \(B\) and \(-B\). CRT consequently gives
exactly four roots modulo \(N\), indexed by independent sign choices modulo
\(p\) and \(q\). Equal signs give the public roots \(\pm B\). A root which
is not congruent to either public root has opposite signs at the two primes.

For example, if

\[
r\equiv B\pmod p,\qquad r\equiv-B\pmod q,
\]

then

\[
\gcd(r-B,N)=p,\qquad \gcd(r+B,N)=q.
\]

The other mixed sign choice exchanges \(p\) and \(q\). The factors are
proper because \(2B\) is nonzero modulo either odd prime. Conversely, given
\(p,q\), CRT constructs either mixed sign choice. CRT, gcd, and modular
arithmetic all have polynomial bit complexity. Mixed-root construction and
factoring are therefore deterministically polynomial-time equivalent on this
promise.

Now suppose

\[
N=x^2+Ey^2.
\]

If \(p\mid y\), reduction modulo \(p\) gives \(p\mid x\), so \(p^2\) divides
the left side and hence \(N\), contrary to \(N=pq\) with \(p\ne q\). The
same argument applies to \(q\). Thus \(\gcd(y,N)=1\), and

\[
r\equiv xy^{-1}\pmod N
\]

is defined. Dividing the norm equation by \(y^2\) gives

\[
r^2\equiv-E\pmod N.
\]

The two gcds above factor \(N\) exactly when the induced root is mixed. If
the root is \(\pm B\), they are instead \(1,N\) in some order. Thus a second
principal norm representation is useful precisely when it is
factor-bearing, and Theorem 5 below proves that such a second representation
need not exist.

## 3. The factor-supported residue test

First note that

\[
\gcd(B,E)=\gcd(B,N-B^2)=\gcd(B,N)=1.
\]

Hence \(B\) is a unit modulo every \(m\mid E\). Also

\[
N=B^2+E\equiv B^2\pmod m.
\]

Let \(x\) be any unit modulo \(m\), define

\[
y=Nx^{-1},\qquad t_x=x+y,\qquad d_x=t_x-2B.
\]

Because \(xy\equiv N\pmod m\),

\[
t_x^2-4N
 =(x+y)^2-4xy
 =(x-y)^2\pmod m.
\]

Substitution of \(N\equiv B^2\pmod m\) gives

\[
\begin{aligned}
d_x
 &\equiv x+B^2x^{-1}-2B
  =\frac{(x-B)^2}{x},
\\
d_x+4B
 &\equiv x+B^2x^{-1}+2B
  =\frac{(x+B)^2}{x}.
\end{aligned}
\]

Since \(E\equiv0\pmod m\),

\[
\begin{aligned}
d_x^2+4Bd_x-4E
 &\equiv d_x(d_x+4B)\\
 &\equiv
 \frac{(x-B)^2(x+B)^2}{x^2}\\
 &=\left(\frac{x^2-B^2}{x}\right)^2
 \pmod m.
\end{aligned}
\]

Thus every unit \(x\), not only either true factor residue, automatically
passes both the imposed product relation and this discriminant-square test.
The same proof applies to each prime-power divisor of \(E\), and CRT does
not restore information which is absent in every component. This proves the
literal path-blindness claim. It does not cover nonunits, arbitrary wheel
tests in \(d\), higher prime powers not dividing \(E\), or moduli with an
additional nonlocal relation.

## 4. The proper ideal-class calculation, including nonmaximal orders

Put

\[
s=\sqrt{-E},\qquad
\mathcal O=\mathbb Z[s],\qquad
\alpha=B+s.
\]

The discriminant of the basis \(1,s\) is \(-4E\), whether or not this order
is maximal, and

\[
\operatorname N(\alpha)=(B+s)(B-s)=B^2+E=N.
\]

The conductor of a quadratic order has no prime divisor outside its
discriminant. On the coprime branch,

\[
\gcd(N,2E)=1
\]

because \(N\) is odd and \(\gcd(N,E)=1\). Hence \(p,q\) are coprime to the
conductor. Ideals above them are therefore proper invertible ideals of
\(\mathcal O\); this is the point which prevents nonmaximality from
invalidating the class-group argument.

For \(\ell=p,q\), define the prime ideal selected by \(\alpha\) as

\[
\mathfrak l=(\ell,B+s).
\]

The map

\[
\mathcal O\longrightarrow\mathbb F_\ell,\qquad s\longmapsto-B
\]

is well-defined because \(B^2+E=N\equiv0\pmod\ell\). Its kernel is
\(\mathfrak l\), so \(\mathfrak l\) is prime of norm \(\ell\). Since
\(\alpha\) belongs to both \(\mathfrak p\) and \(\mathfrak q\),

\[
(\alpha)\subseteq\mathfrak p\cap\mathfrak q
 =\mathfrak p\mathfrak q.
\]

The last equality uses coprimality of ideals over the distinct rational
primes. Both sides have norm \(pq=N\), so

\[
(\alpha)=\mathfrak p\mathfrak q.
\]

Let \(C=[\mathfrak p]\) in the proper invertible ideal class group. Taking
classes in the preceding equality gives

\[
[\mathfrak q]=C^{-1}.
\]

### Root ideals and the square class

For a root \(r^2\equiv-E\pmod N\), define

\[
\mathfrak a_r=(N,r+s).
\]

The quotient map \(s\mapsto-r\pmod N\) shows that this ideal has norm \(N\).
It is proper and invertible because \(N\) is coprime to the conductor. CRT
decomposes it according to the signs of \(r\) modulo \(p,q\). If, for
example,

\[
r\equiv B\pmod p,\qquad r\equiv-B\pmod q,
\]

then

\[
\mathfrak a_r=\mathfrak p\,\overline{\mathfrak q}.
\]

For a proper invertible ideal, conjugation induces inversion in the class
group. Consequently

\[
[\mathfrak a_r]
 =[\mathfrak p]\,[\overline{\mathfrak q}]
 =C\,[\mathfrak q]^{-1}
 =C^2.
\]

The opposite mixed signs give

\[
\overline{\mathfrak p}\,\mathfrak q
\quad\text{of class}\quad C^{-2}.
\]

This derivation used only ideals prime to the conductor, so it applies
unchanged to the potentially nonmaximal order \(\mathcal O\).

Every genus character is multiplicative with values in
\(\{\pm1\}\). Therefore, for every such character \(\chi\),

\[
\chi(C^2)=\chi(C)^2=1.
\]

Thus every square lies in the principal genus for the purpose needed here:
all genus labels place a mixed-root class with the identity and cannot
distinguish the two.

### When the mixed ideal is a principal norm

The ideal \(\mathfrak a_r\) is principal if and only if \(C^2=1\). If
\(\mathfrak a_r=(x+ys)\), equality of ideal norms gives

\[
x^2+Ey^2=N.
\]

Membership of the generator in \((N,r+s)\), reduced in the quotient
\(s=-r\), gives

\[
x-yr\equiv0\pmod N.
\]

Theorem 2 shows that \(y\) is a unit modulo \(N\), so the representation
induces \(r\equiv xy^{-1}\pmod N\). Conversely, a representation inducing
that root supplies an element of norm \(N\) in \(\mathfrak a_r\); its
principal ideal is contained in \(\mathfrak a_r\) and has the same norm, so
the two ideals are equal. Hence a mixed-root factor-bearing representation
exists exactly when \(C^2=1\).

If an invertible class is ambiguous, conjugation fixes it. Since conjugation
also inverts it, its square is the identity. An invertible ramified prime
ideal likewise has square equal to the corresponding principal rational
prime ideal, so its class has order at most two. (A conductor prime can
instead give a noninvertible ideal and then supplies no class in this proper
invertible class group.) Because the class group is abelian, the subgroup
generated by all available invertible ambiguous or ramified classes has
exponent at most two. There is no group-theoretic reason it must contain a
given nontrivial square \(C^2\), and Theorem 5 supplies an exact instance
where it does not.

## 5. Exact finite certificate for \(N=2627\)

First,

\[
37\cdot71=2627.
\]

The prime \(37\) has no prime divisor at most \(\sqrt{37}<7\), and \(71\)
has none at most \(\sqrt{71}<9\), so both are prime. Also

\[
37<71<74=2\cdot37.
\]

Since

\[
51^2=2601<2627<2704=52^2,
\]

\[
B=51,\qquad E=2627-2601=26=2\cdot13.
\]

The coordinates are

\[
a=51-37=14,\qquad
c=71-51=20,\qquad
d=20-14=6.
\]

For \(r=162\),

\[
162^2+26=26270=10\cdot2627.
\]

Moreover,

\[
r-B=111=3\cdot37,\qquad
r+B=213=3\cdot71,
\]

so

\[
\gcd(r-B,N)=37,\qquad
\gcd(r+B,N)=71.
\]

This verifies the mixed-root certificate by exact identities.

### Exhaustion of the principal norm equation

Suppose

\[
x^2+26y^2=2627.
\]

Reduction modulo \(13\) gives

\[
x^2\equiv1\pmod{13},
\]

so \(x\equiv\pm1\pmod{13}\). Also \(|x|\leq51\), and parity of the
equation forces \(x\) to be odd. Up to sign, the only possibilities are

\[
x\in\{1,25,27,51\}.
\]

The corresponding necessary values of \(y^2\) are

\[
\frac{2627-x^2}{26}
\in\{101,77,73,1\}.
\]

The first is strictly between \(10^2\) and \(11^2\), and the next two are
strictly between \(8^2\) and \(9^2\). Only the last is a square. Therefore

\[
(x,y)=(\pm51,\pm1)
\]

are all the integer solutions. All four independent sign choices give only
the public roots \(\pm B\); there is no factor-bearing principal companion.

### The mixed form and its proper class

With the sign convention used in the statement, the form associated with
the chosen root is

\[
F=[N,2r,(r^2+E)/N]=[2627,324,10].
\]

Under the usual ideal-form correspondence this sign convention attaches the
form to \((N,-r+s)=\mathfrak a_{-r}\), rather than to
\(\mathfrak a_r\). Since \(-r\) is the other mixed root, this only exchanges
\(C^2\) and \(C^{-2}\); it has no effect on principality or on the
obstruction.

Its discriminant is

\[
324^2-4\cdot2627\cdot10=-104=-4E.
\]

The following is an explicit chain of proper equivalences:

\[
\begin{aligned}
[2627,324,10]
&\sim[10,-324,2627]\\
&\sim[10,-4,3]\\
&\sim[3,4,10]\\
&\sim[3,-2,9].
\end{aligned}
\]

The first and third steps use

\[
[A,b,c]\longmapsto[c,-b,A],
\]

induced by the determinant-one substitution
\((X,Y)\mapsto(-Y,X)\). The second uses
\((X,Y)\mapsto(X+16Y,Y)\), and the fourth uses
\((X,Y)\mapsto(X-Y,Y)\). Thus no class-group enumeration is hidden in the
claimed equivalence.

The principal form of discriminant \(-104\) is

\[
[1,0,26],
\]

which represents integers \(X^2+26Y^2\). The form \([3,-2,9]\) represents
\(3\) at \((1,0)\), whereas \(X^2+26Y^2=3\) has no integer solution:
\(|Y|\geq1\) is too large, and \(Y=0\) would require \(X^2=3\).
Properly equivalent forms represent the same integers, so
\([3,-2,9]\) is nonprincipal.

The ramified forms supplied by the two discriminant primes are

\[
[2,0,13]\quad\text{and}\quad[13,0,2].
\]

They are properly equivalent by the same determinant-one swap, so they
give one class \(R\). Since changing the middle coefficient's sign gives
the inverse class and the middle coefficient is zero,

\[
R^{-1}=R,\qquad R^2=1.
\]

The class is not principal: \([2,0,13]\) cannot represent \(1\).
Therefore the subgroup generated by both ramified forms is exactly

\[
\{[1,0,26],[2,0,13]\}.
\]

It does not contain \([3,-2,9]\). Indeed, the latter is nonprincipal, and
\([2,0,13]\) cannot represent \(3\), while \([3,-2,9]\) does. This is an
exact certificate that the nontrivial mixed square class is outside the
ramified subgroup.

Finally,

\[
d=6=2\cdot3,\qquad 2E=52=2^2\cdot13.
\]

The prime \(3\) in \(d\) is absent from the prime support of \(2E\). Hence
even in this small promised instance, the square-gap identities do not imply
that \(d\) divides a number supported on the known factors of \(E\).

## Exact remaining scope

The first two listed gates are exact equivalences already proved above:
the correct \(d\), or any mixed root, factors \(N\) in polynomial time.
The class calculation reformulates the mixed orientation as locating the
specific square \(C^2\), and it proves why genus labels alone lose that
orientation. The literal factor-supported sieve and the canonical ramified
subgroup also fail on their stated interfaces.

These facts do not rule out a nonlocal modulus, a new statistic, direct
prefix selection, or full class-group computation. The statement supplies
no QP method for any of them. The claim attributed to P175 about a reciprocal
prefix is external to the two allowed files and therefore remains
unverified in this blind reconstruction.

Accordingly, F202 establishes a valid one-child size contraction and precise
failures of three named postprocessing interfaces, but it does not establish
the required postprocessor or solve unrestricted integer factoring.
