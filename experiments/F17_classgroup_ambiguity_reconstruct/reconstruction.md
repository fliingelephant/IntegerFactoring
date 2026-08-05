# Independent reconstruction: ambiguous classes and collision sampling

Let \(D=|\Delta|\). All form equivalences below are proper equivalences. Since
\(N=pq\ge 15\), none of the exceptional discriminants \(-3,-4\) occurs. I use
the convention that a reduced positive form satisfies

\[
 |b|\le a\le c,
\]

and that \(b\ge 0\) if either \(|b|=a\) or \(a=c\).

## 1. The ambiguous classes

### Boundary criterion

Inversion sends the class of \([a,b,c]\) to the class of \([a,-b,c]\). Away
from the boundary of the reduced region, both forms are canonical reduced
forms, and uniqueness of the canonical reduced representative says that they
represent the same class only when \(b=0\). On the boundary there are two
further equivalences:

\[
 [a,-a,c]\sim[a,a,c],\qquad [a,-b,a]\sim[a,b,a].
\]

The first follows by the substitution \(x\mapsto x+y\), and the second by the
determinant-one substitution \((x,y)\mapsto(-y,x)\). The sign convention
excludes \(b=-a\) as a canonical boundary representative. Consequently

\[
 C=C^{-1}\quad\Longleftrightarrow\quad
 b=0,\qquad b=a,\qquad\text{or}\qquad a=c.
\tag{1}
\]

Thus the forms in (1) represent exactly \(T=G[2]\).

### The case \(\Delta=-N\)

Here \(N\equiv3\pmod 4\), so \(p,q\) have opposite residues modulo \(4\).
The case \(b=0\) is impossible because then the discriminant is divisible by
\(4\).

If \(b=a\), then

\[
 N=a(4c-a).
\tag{2}
\]

Writing \(d=4c-a\), reducedness \(a\le c\) is equivalent to \(d\ge3a\).
The factor pairs of \(N\) therefore give the principal form

\[
 P=[1,1,(N+1)/4]
\]

and, precisely when \(q>3p\),

\[
 [p,p,(p+q)/4].
\tag{3}
\]

If \(a=c\), the boundary sign rule gives \(0\le b\le a\), and

\[
 N=(2a-b)(2a+b).
\tag{4}
\]

Writing \(r=2a-b\le s=2a+b\), the condition \(b\le a\) is exactly
\(s\le3r\). The pair \((1,N)\) cannot satisfy it, while \((p,q)\) does
precisely when \(q<3p\). It gives

\[
 [(p+q)/4,(q-p)/2,(p+q)/4].
\tag{5}
\]

All displayed coefficients are integral because \(p,q\) have opposite
residues modulo \(4\). The form in (3) is primitive since
\(p\nmid(p+q)/4\). In (5), \(b=(q-p)/2\) is odd. A common divisor of \(a,b\)
would therefore be odd and would divide both \(p+q\) and \(q-p\), hence both
\(2p\) and \(2q\); it is \(1\). This proves primitivity of (5).
The reducedness inequalities were exactly the inequalities used above, and
the positive boundary signs make the forms canonical.

Equations (2) and (4) are extraction identities. The principal form gives
the pair \(1,N\); either (3) or (5) gives \(p,q\). The enumeration also proves
exhaustiveness. Hence \(t=2\), with one useless and one factor-exposing
ambiguous class.

### The case \(\Delta=-4N\)

Here \(N\equiv1\pmod 4\), so \(p,q\) have the same residue modulo \(4\).
For \(b=0\), the equation \(ac=N\), together with \(a\le c\), gives exactly

\[
 P=[1,0,N],\qquad F_0=[p,0,q].
\tag{6}
\]

For \(b=a\), put \(d=4c-a\). Then \(ad=4N\) and \(a+d=4c\). Because
\(v_2(a)+v_2(d)=2\), the divisibility \(4\mid a+d\) is impossible when one
of \(a,d\) is odd and forces \(v_2(a)=v_2(d)=1\). Thus

\[
 a=2r,\qquad d=2s,\qquad rs=N.
\]

Reducedness is \(s\ge3r\). This boundary gives

\[
 E=[2,2,(N+1)/2]
\tag{7}
\]

and, when \(q>3p\),

\[
 F_1=[2p,2p,(p+q)/2].
\tag{8}
\]

The middle coefficient in an \(a=c\) form is even. On writing

\[
 u=a-b/2,\qquad v=a+b/2,
\]

the discriminant equation becomes \(uv=N\). The inequalities are
\(u\le v\le3u\). The pair \((1,N)\) again fails, while \((p,q)\) gives,
when \(q<3p\),

\[
 F_1=[(p+q)/2,q-p,(p+q)/2].
\tag{9}
\]

The numbers \((N+1)/2\) and \((p+q)/2\) are odd. Thus (7) is primitive, and
(8) is primitive because \(p\nmid(p+q)/2\). In (9), \(a\) is odd; a common
divisor of \(a,b\) would divide \(p+q\) and \(q-p\), and hence would be \(1\).
This proves primitivity. The derivation already checked reducedness, and a
direct substitution checks every discriminant.

The extraction identities in this case are

\[
 \begin{array}{ll}
 b=0:&N=ac,\\[2mm]
 b=a:&N=(a/2)(2c-a/2),\\[2mm]
 a=c:&N=(a-b/2)(a+b/2).
 \end{array}
\tag{10}
\]

They return \(1,N\) on \(P,E\) and \(p,q\) on \(F_0,F_1\). In particular,
\(E\) is a public nonprincipal decoy: it is computable from \(N\), and it is
not principal because (6) and (7) are distinct canonical reduced forms.
The boundary enumeration proves that these four forms are exhaustive, so
\(t=4\).

The apparent equality case \(q=3p\) never occurs: \(p\ge3\) and \(q=3p\)
would make \(q\) composite. Formally, in that case the two formulas in each
branch coalesce to \([p,p,p]\) for discriminant \(-3p^2\), or to
\([2p,2p,2p]\) for discriminant \(-12p^2\); both are imprimitive and lie
outside the stated squarefree semiprime setup. Thus no equality case is
missing.

Let \(U\subset T\) denote the factor-exposing forms and let
\(T_0=T\setminus U\). For \(\Delta=-N\), \(T_0=\{P\}\). For
\(\Delta=-4N\), \(T_0=\{P,E\}\). Every ambiguous class squares to \(P\), and
\(E\ne P\), so \(\{P,E\}\) is an order-two subgroup. Hence in both cases
\(T_0\le T\), \([T:T_0]=2\), and \(U\) is its other coset. Exactly half of
\(T\) exposes the two factors through (2), (4), or (10).

## 2. Exact-uniform sampling and square collisions

Assume in this section, as an oracle premise, that
\(X_1,X_2,\ldots\) are iid exact-uniform elements of \(G\). A direct sample
is useful with probability

\[
 \Pr(X\in U)=\frac{|U|}{h}=\frac{t}{2h}.
\tag{11}
\]

Thus direct sampling has geometric expectation \(2h/t\).

An ordinary collision modulo inversion has either \(X_i=X_j\), which is a
duplicate, or \(X_j=X_i^{-1}\). In the latter case
\(X_iX_j^{-1}=X_i^2\), so the only possible factor-exposing element obtained
this way is already available by squaring one sample. The square map has
kernel \(T\), so every element of \(G^2\) has exactly \(t\) square roots. It
follows exactly that

\[
 \Pr(X^2\in U)=\frac{t\,|U\cap G^2|}{h}
 \le \frac{t^2}{2h}.
\tag{12}
\]

This need not vanish. For example, the reduced forms of discriminant
\(-39\) are

\[
 [1,1,10],\quad[2,1,5],\quad[2,-1,5],\quad[3,3,4].
\]

The reduction bound \(a\le\sqrt{39/3}\) makes this list exhaustive. Hence
the class group has order \(4\) and exactly two elements of order dividing
\(2\), so it is cyclic of order \(4\). Its unique nonidentity element of
\(T\), the useful form \([3,3,4]\), is therefore a square.

For a specified pair of distinct samples, \(Q=X_iX_j^{-1}\) is uniform on
\(G\). Moreover \(X_i^2=X_j^2\) exactly when \(Q\in T\). Therefore

\[
 \Pr\bigl(X_i^2=X_j^2\ \text{and}\ Q\in U\bigr)
 =\frac{|U|}{h}=\frac{t}{2h}.
\tag{13}
\]

Conditional on a square collision, its quotient is useful with probability
\(1/2\).

Put

\[
 H=\frac ht=|G^2|.
\]

Each square fiber is a coset \(xT\), and it splits into the two equal halves
\(xT_0\) and \(xuT_0\), where \(u\in U\). Quotients of two points in the same
half lie in \(T_0\); quotients of points in opposite halves lie in \(U\).
Thus every sample projects uniformly onto one of \(H\) fiber labels and one
of two colors.

Failure after \(m\) samples means that every occupied fiber has only one
color. If exactly \(k\) fibers are occupied, choose the fibers in
\(\binom Hk\) ways, their one allowed color in \(2^k\) ways, and a surjection
of the \(m\) labeled samples onto them in \(k!S(m,k)\) ways. Consequently the
exact success probability for finding at least one useful square-collision
quotient is

\[
 1-\frac{1}{(2H)^m}
 \sum_{k=0}^{\min(m,H)}\binom Hk2^k k!S(m,k).
\tag{14}
\]

Here \(S(m,k)\) is a Stirling number of the second kind. Formula (14) is for
the square-collision event; it does not also fold in direct hits from (11).

For the scale, (13) and a union bound give

\[
 \Pr(\text{success by time }m)\le
 \frac{\binom m2}{2H}=\frac{m(m-1)}{4H}.
\tag{15}
\]

Hence \(o(\sqrt H)\) samples have success probability \(o(1)\). Conversely,
ignore the colors and consider the ordinary birthday collision among the
\(H\) fiber labels. For \(m\le H\), its probability is at least

\[
 1-\exp\!\left(-\frac{m(m-1)}{2H}\right).
\]

After the fiber labels are fixed, select the first colliding pair by a rule
depending only on those labels. Its two independent colors differ with
probability \(1/2\). A block of \(\lceil2\sqrt H\rceil\) samples therefore
has a useful collision with an absolute positive probability (small \(H\)
can be absorbed into the constant). Independent fresh blocks give an
\(O(\sqrt H)\) expected stopping time. On the other hand, taking
\(m=\lfloor\sqrt H\rfloor\) in (15) leaves probability at least \(3/4\) of
not having stopped, proving an \(\Omega(\sqrt H)\) expectation. Thus both
the constant-success sample scale and the expected stopping scale are

\[
 \Theta(\sqrt H).
\tag{16}
\]

This is a sample-complexity statement under the exact sampler premise. In
bit complexity, a reduced form has \(O(\log D)\) bits per coefficient, and
composition and reduction take polynomial time in \(\log D\). Store one
representative for each observed canonical square in an exact balanced
dictionary. A later point in the same fiber is compared with that
representative; a same-color point changes nothing, while an opposite-color
point succeeds. Thus \(m\) samples require

\[
 O\bigl(m\log m\,\operatorname{poly}(\log D)\bigr)
\]

bit operations and \(O(m\log D)\) bits of storage, excluding the explicitly
granted sampler. At the stopping scale this is
\(O(\sqrt H\log H\,\operatorname{poly}(\log D))\). The procedure need not
know \(H\): it simply continues until a useful quotient occurs. These costs
are not polynomial in the input length when \(H\) is exponentially large.

## 3. The unconditional analytic obstruction to polynomial sampling

The discriminants here are negative fundamental discriminants. Since
\(\Delta<-4\), the analytic class-number formula is

\[
 h(\Delta)=\frac{\sqrt D}{\pi}L(1,\chi_\Delta).
\tag{17}
\]

Siegel's unconditional theorem says that for every fixed
\(\varepsilon>0\) there is a constant \(c_\varepsilon>0\) such that

\[
 L(1,\chi_\Delta)\ge c_\varepsilon D^{-\varepsilon}.
\tag{18}
\]

The constant in (18), and hence any threshold derived from it, is
ineffective. This does not affect the unconditional asymptotic conclusion.
Taking \(\varepsilon=1/4\), there is an ineffective \(C>0\) with

\[
 h\ge C D^{1/4},\qquad H\ge (C/4)D^{1/4},
\tag{19}
\]

where the second inequality uses \(t\le4\).

Let \(M(n)\) be any fixed polynomial number of exact-iid samples. A union
bound using (11) gives

\[
 \Pr(\text{a direct hit})\le\frac{M(n)}{2H}
 \le \frac{2M(n)}{C D^{1/4}},
\tag{20}
\]

and (13) gives

\[
 \Pr(\text{a useful square collision})
 \le\frac{\binom{M(n)}2}{2H}
 \le\frac{2\binom{M(n)}2}{C D^{1/4}}.
\tag{21}
\]

For \(n=\lceil\log_2(N+1)\rceil\), one has
\(D\ge N\ge2^{n-2}\). Polynomial factors are \(2^{o(n)}\), so (20) and
(21) are \(2^{-\Omega(n)}\). For example, each is at most \(2^{-n/8}\) for
all sufficiently large \(n\), but the starting threshold is ineffective
because \(C\) is ineffective.

This conclusion is not an artifact of extremely unbalanced factors. The
prime number theorem in the progressions \(1,3\pmod4\) implies that, for all
sufficiently large \(X\), each fixed relative interval contains primes in
either progression. Choose

\[
 p\in(X,1.05X),\qquad q\in(1.10X,1.15X).
\]

Taking \(p\equiv1\pmod4,q\equiv3\pmod4\) produces infinitely many balanced
\(N\equiv3\pmod4\); taking both congruent to \(1\pmod4\) produces infinitely
many balanced \(N\equiv1\pmod4\). In both families \(1<q/p<1.15\), and the
same exponential bounds apply. No finite-range or undefined approximate
sampling assertion is used here.

## 4. Genus information

For a discriminantal factorization \(\Delta=d_1d_2\), a genus character can
be evaluated on a class by choosing an integer \(r\), coprime to \(\Delta\),
represented primitively by a form in that class and setting

\[
 \chi_{d_1}(C)=\left(\frac{d_1}{r}\right).
\]

Such an \(r\) can be made the leading coefficient of an equivalent form, so

\[
 \Delta\equiv b^2\pmod{4r},
\]

and therefore

\[
 \left(\frac{\Delta}{r}\right)=1.
\tag{22}
\]

For \(\Delta=-4N\), the public factorization of the discriminant

\[
 \Delta=(-4)N
\]

is available without knowing \(p,q\). Multiplicativity and (22) give

\[
 \chi_{-4}(C)\chi_N(C)=1,
 \qquad\text{hence}\qquad
 \chi_{-4}(C)=\chi_N(C).
\tag{23}
\]

The value \(\chi_{-4}\) is determined just by \(r\bmod4\), and
\((N/r)\) is likewise a Jacobi-symbol computation using public \(N\).
Thus it is false that every individual genus character requires either
factor \(p\) or \(q\).

Equation (22) is only an aggregate splitting condition. It says that the
product of the constituent character values is \(+1\); it does not say that
each value is \(+1\), identify the genus, or reveal \(p,q\). For example,
at \(\Delta=-84\), the decoy form \([2,2,11]\) represents \(r=11\), and both
\((-4/11)\) and \((21/11)\) are \(-1\), while their product is \(+1\).

Genus theory gives

\[
 |G/G^2|=t,
\]

so every genus has \(H=h/t\) classes. Even grant an oracle that reveals all
genus labels, identifies the best genus, and samples exactly uniformly from
any chosen genus. Its direct useful probability is at most

\[
 \frac{|U|}{H}=\frac{t^2}{2h},
\tag{24}
\]

only a factor \(t\le4\) above (11). More generally, the quotient of
independent uniform samples from two chosen genera is uniform on their
quotient genus. Its useful probability is also at most (24). Thus even
complete chosen-genus access changes useful mass by at most the constant
\(t\), and changes a birthday scale by at most a constant factor.

## 5. What the two displayed powering rules do

Write

\[
 \lambda(G)=2^a m_{\rm odd}.
\]

The odd-primary subgroup is killed by exponentiation to
\(\lambda(G)/2\). On the Sylow \(2\)-subgroup, the odd multiplier
\(m_{\rm odd}\) is an automorphism, so the image is the image of the
\(2^{a-1}\)-power map.

If \(t=2\), the Sylow \(2\)-subgroup has rank one and is cyclic,
\(C_{2^a}\). The image of \(X\mapsto X^{\lambda(G)/2}\) is exactly \(T\).
For uniform \(X\), the image is uniform on \(T\).

If \(t=4\), write the Sylow \(2\)-subgroup as

\[
 C_{2^a}\times C_{2^b},\qquad a\ge b\ge1.
\]

When \(a=b\), the image of the same map is all of \(T\). When \(a>b\),
\(2^{a-1}\) kills the second factor and leaves the top involution of the
first, so the image is an order-two subgroup of \(T\). Its nonidentity
element can be one of the two useful classes or the decoy \(E\). A uniform
input is uniform on the stated image.

For the order exponent, write \(G=S\times O\), with \(S\) the Sylow
\(2\)-subgroup and \(O\) of odd order. If \(t=2\), then
\(|S|=2^a\), and

\[
 X^{h/2}=X^{2^{a-1}|O|}
\]

is uniform on \(T\) for uniform \(X\). If \(t=4\), then
\(|S|=2^{a+b}\), and \(h/2\) is divisible by \(2^a\) because \(b\ge1\).
It kills both \(S\) and \(O\), so

\[
 X^{h/2}=1
\]

for every \(X\).

These particular rules require the exact values \(\lambda(G)\) or \(h\).
Neither value is supplied by the input or by the exact-sampling premise, so
the displayed rules alone are not an algorithm from \(N\). This observation
does not assert that every conceivable powering strategy requires order or
exponent data.

## 6. Forms from an auxiliary split prime

Let \(\ell\nmid\Delta\) be an odd prime with
\((\Delta/\ell)=1\). Modulo \(\ell\), the equation

\[
 b^2\equiv\Delta\pmod{4\ell}
\tag{25}
\]

has two choices, \(b\equiv\pm r\pmod\ell\). Modulo \(4\), it also has two
choices: \(b\equiv1,3\pmod4\) when \(\Delta\equiv1\pmod4\), and
\(b\equiv0,2\pmod4\) when \(\Delta\equiv0\pmod4\). The Chinese remainder
theorem therefore gives exactly four roots modulo \(4\ell\).

Reduction modulo \(2\ell\) identifies roots that differ by \(2\ell\), so
there are exactly two root classes modulo \(2\ell\). They are negatives of
one another. They are distinct because a self-negative class would be
divisible by \(\ell\), contradicting
\(b^2\equiv\Delta\not\equiv0\pmod\ell\). If the split prime is
\(\ell=2\), necessarily \(\Delta\equiv1\pmod8\); then all four odd residues
modulo \(8\) are roots and they again reduce to the two sign classes modulo
\(4\). Thus the same literal counts hold in that exceptional split case.

For either sign choose the centered representative \(-\ell<b<\ell\) and set

\[
 f_{\ell,b}=
 \left[\ell,b,\frac{b^2-\Delta}{4\ell}\right].
\tag{26}
\]

It is positive and primitive: for odd \(\ell\), one has \(\ell\nmid b\), and
for \(\ell=2\), \(b\) is odd. Replacing \(b\) by \(b+2k\ell\) gives a
properly equivalent form, by the substitution \(x\mapsto x+ky\).
Replacing \(b\) by \(-b\) gives the inverse form class. After canonical
reduction, the two signs therefore give inverse classes, possibly the same
class if that class is ambiguous.

This construction has a limited and exact sampling scope. Given a certified
split prime \(\ell\), a modular square root can be found by a Las Vegas
Tonelli--Shanks computation (the output is directly verified), followed by
CRT and standard polynomial-time form reduction. If

\[
 L=\lceil\log_2(\ell+1)\rceil,
\]

then the input and all output coefficients have \(O(n+L)\) bits. The modular
square-root component has, with schoolbook arithmetic, a crude expected
\(O(L^4)\) bit bound, and the whole construction costs
\((n+L)^{O(1)}\) bit operations. In particular it is polynomial in \(n\)
only when \(L=\operatorname{poly}(n)\). Generating or certifying \(\ell\), if
it is not supplied, is a separate cost.

Choosing the sign uniformly samples only the inverse pair arising from that
\(\ell\). Choosing primes from an interval gives the pushforward of that
specified prime distribution; it is not an exact-uniform sample from \(G\)
without an additional exact distribution theorem or sampler. No such
claim, and hence no factoring algorithm, follows from (26).
