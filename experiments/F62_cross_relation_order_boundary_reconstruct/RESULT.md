# Proof-blind reconstruction result — exact order and HSP boundary

## Verdict

**PASS, with one terminology clarification.** All six structural claims and all
three finite claims hold. In Claim 3, the conditions

\[
x\notin K,\qquad 2x\in K
\]

characterize a nonidentity involution in the generated residue group. They do
not, by themselves, say that its residue is outside the old decoder image. The
statement correctly lists that as an additional requirement in its next
sentence. If the word “new” were instead intended to mean “outside the old
image,” the additional exact condition is \(2x\notin 2K\).

The conclusions below are algebraic and output-sensitive. They do not produce
an all-input classical selector, an efficient infinite-domain HSP algorithm, or
a positive divisor in a finite occurrence box unless that property is proved
separately.

## 1. Endpoints, involutions, and the direct screen

Write

\[
X=\Phi_N(v),\qquad Y=\Phi_N(E-v).
\]

Every selected relation row is in \(\Lambda_N\), so \(E\in\Lambda_N\) and
\(\Phi_N(E)=1\). Hence

\[
Y=\Phi_N(E)\Phi_N(v)^{-1}=X^{-1}.
\]

Consequently,

\[
X=Y
\iff X^2=1
\iff \Phi_N(2v)=1
\iff 2v\in\Lambda_N.
\]

Now let \(x\) be self-inverse modulo odd \(N\). For each prime power
\(p^e\mid N\),

\[
p^e\mid (x-1)(x+1).
\]

The two factors have gcd dividing \(2\). Since \(p\) is odd, the whole power
\(p^e\) divides exactly one of \(x-1\) and \(x+1\). Thus every prime-power
component assigns one of the two signs. If \(x\not\equiv 1,-1\pmod N\), both
signs occur. It follows that

\[
1<\gcd(x-1,N)<N,
\qquad
1<\gcd(x+1,N)<N.
\]

Self-inversion is not necessary for the direct \(\gcd(x-1,N)\) or
\(\gcd(x+1,N)\) screen. For example, take \(N=21\), one generator \(q=4\),
one relation row \(E=3\), and \(v=1\). The order of \(4\) modulo \(21\) is
\(3\), so \(E\in\Lambda_N\), but \(2v=2\notin\Lambda_N\). Nevertheless,

\[
\gcd(4-1,21)=3.
\]

This proves the stated strict separation between the full direct screen and
the self-inverse subtarget.

## 2. Exact residue image of the old decoder

Let

\[
A:\mathbb Z^m\to\mathbb Z^s,
\qquad
Az=\sum_i z_i\lambda_i.
\]

The old parity decoder chooses \(c\in\{0,1\}^m\) for which \(Ac\) is even and
outputs the residue \(\Phi_N(Ac/2)\). Such an output plainly belongs to

\[
\{\Phi_N(v):2v\in L_0\}.
\]

For the reverse inclusion, suppose \(2v=Az\) for some \(z\in\mathbb Z^m\).
Reduce every coordinate of \(z\) modulo \(2\): write

\[
z=c+2k,
\qquad c\in\{0,1\}^m,quad k\in\mathbb Z^m.
\]

Then

\[
Ac=2(v-Ak).
\]

Thus \(c\) is an old parity dependency. Moreover, \(Ak\in L_0\subseteq
\Lambda_N\), so

\[
\Phi_N(Ac/2)=\Phi_N(v-Ak)=\Phi_N(v).
\]

Therefore the exact residue image is

\[
R_{\rm old}=\{\Phi_N(v):v\in\mathbb Z^s,\ 2v\in L_0\}.
\]

The reduction \(z\mapsto c\) is coordinatewise, so it remains valid when
equal rows are distinct indexed occurrences.

This is only equality in the modular image. A signed exponent representing a
residue need not be nonnegative. Neither this equality nor the lattice
condition proves \(0\leq v\leq E\), and it does not prove the integer bound
\(1<q^v<N\).

## 3. The quotient criterion and the old-image boundary

Because \(L_0\subseteq\Lambda_N\), the subgroup

\[
K=\Lambda_N/L_0
\]

is well-defined in \(Q_0=\mathbb Z^s/L_0\). The generated residue group is

\[
H=\operatorname{im}\Phi_N
\cong \mathbb Z^s/\Lambda_N
\cong Q_0/K.
\]

Let \(x=v+L_0\in Q_0\). Its image in \(H\) is the identity exactly when
\(x\in K\), and its square is the identity exactly when \(2x\in K\).
Therefore it has exact order \(2\) exactly when

\[
x\notin K,
\qquad
2x\in K.
\]

For completeness, the old image has the quotient description

\[
R_{\rm old}=\operatorname{image}\bigl(Q_0[2]\longrightarrow Q_0/K\bigr),
\qquad
Q_0[2]=\{y\in Q_0:2y=0\}.
\]

For a class satisfying the involution conditions,

\[
x+K\in R_{\rm old}
\iff \exists k\in K:\ 2(x+k)=0
\iff 2x\in 2K.
\]

Hence an exact-order-two residue outside the old image is characterized by

\[
x\notin K,
\qquad
2x\in K\setminus 2K.
\]

Even that is still an abstract modular class. A useful F62 state additionally
needs a representative in an actual selected occurrence box, the integer
magnitude bound, and a residue other than the two global signs \(1\) and
\(-1\).

## 4. Least involutory exponent and exact order

Let \(a\) have exact order \(r\). The two conditions on \(e\) are

\[
a^{2e}=1\iff r\mid 2e,
\qquad
a^e\ne1\iff r\nmid e.
\]

If \(r\) is odd, the first divisibility implies \(r\mid e\), so no such
\(e\) exists. If \(r=2u\), then \(e=u\) satisfies both conditions. Every
positive solution has \(u\mid e\), so the least one is

\[
e=r/2.
\]

Thus exact order immediately implements the total least-answer oracle. In the
other direction, query the least-answer oracle on \(a\). If it returns \(e\),
then \(r=2e\). If it returns `NONE`, then \(r\) is odd. In that case \(-a\)
has order \(2r\): an odd-order cyclic subgroup cannot contain the order-two
element \(-1\), and the commuting factors \(-1\) and \(a\) have coprime
orders \(2\) and \(r\). One additional query on \(-a\) therefore returns
\(r\). This gives polynomial-time Turing reductions in both directions, with
at most two least-answer queries.

This equivalence uses the least positive answer and the explicit `NONE`
answer. It makes no assertion about an oracle that returns an arbitrary
factoring-useful power.

For one generator, the homomorphism is \(n\mapsto a^n\), and

\[
\ker\Phi_N=\{n:a^n=1\}=r\mathbb Z.
\]

Thus exact recovery of the kernel lattice recovers \(r\), up to the harmless
sign of a one-dimensional lattice basis.

## 5. Smith normal form and screening 2-torsion

The kernel of a homomorphism from \(\mathbb Z^s\) to a finite group has finite
index, so a supplied basis matrix for \(\Lambda_N\) has full rank. Smith
normal form gives

\[
\mathbb Z^s/\Lambda_N\cong
\bigoplus_{i=1}^s\mathbb Z/d_i\mathbb Z.
\]

In an invariant-factor coordinate, the 2-torsion contributes nothing when
\(d_i\) is odd and contributes the class \(d_i/2\) when \(d_i\) is even.
Pulling these classes back through the unimodular Smith transformations gives
an \(\mathbb F_2\)-basis of \(H[2]\) with at most \(s\) elements.

If \(H[2]\) contains a non-global involution, at least one member of any such
basis is non-global. Indeed, the only global involutions are \(1\) and
\(-1\). A vector-space basis contains no identity, and distinct basis vectors
cannot all equal the single nonidentity global element \(-1\). If every basis
vector were global, its span could not contain a non-global element. Screening
the at most \(s\) basis residues with both gcds therefore finds a proper
factor whenever a non-global involution exists in \(H\).

Smith normal form, the unimodular transformations, modular exponentiation,
modular inversion, and gcd computation all have polynomial bit complexity in
their complete input and output encodings. Pulled-back exponent vectors can
have negative entries. Those entries are valid for modular evaluation because
the \(q_j\) are units, but they are not positive whole-block divisors and do
not establish finite-box legality.

## 6. Algebraic HSP identity and algorithmic boundary

For all \(v,w\in\mathbb Z^s\),

\[
\Phi_N(v)=\Phi_N(w)
\iff \Phi_N(v-w)=1
\iff v-w\in\Lambda_N.
\]

Thus the output fibers are exactly the cosets of \(\Lambda_N\). This is the
hidden-subgroup identity used in the one-dimensional order-finding setting.
It is not an algorithm on an infinite uniform superposition over
\(\mathbb Z^s\). A finite register and truncation range, an implementable
oracle circuit, Fourier precision, reconstruction, and a success-probability
analysis are extra requirements. The algebraic identity alone proves none of
them.

## 7. Check at \(N=65\)

Use coordinates \((2,3,7,11,31)\). The two relation rows are

\[
\lambda_1=(1,1,0,1,0),
\qquad
\lambda_2=(0,1,1,0,1).
\]

They are distinct nonzero binary vectors, hence independent over
\(\mathbb F_2\). Both relations are valid because \(66\equiv651\equiv1
\pmod{65}\).

Selecting both occurrences gives

\[
E=(1,2,1,1,1).
\]

The cross choice \(v=(1,0,1,0,0)\) is in the occurrence box and has integer
value

\[
g=2\cdot7=14<65.
\]

Also

\[
14^2=196=1+3\cdot65,
\]

so \(14\) is self-inverse and is neither \(1\) nor \(-1\) modulo \(65\).
The two screens give

\[
\gcd(14-1,65)=13,
\qquad
\gcd(14+1,65)=5.
\]

This check is specific to the selected blocks \(2\) and \(7\); it does not
assert uniqueness. For example, \(3\) has order
\(\operatorname{lcm}(4,3)=12\) modulo \(5\cdot13\), and
\(3^6=729\equiv14\pmod{65}\), so another block also has a useful half-order
residue.

## 8. Check at \(N=187\)

Here \(187=11\cdot17\), and \(188=2^2\cdot47\) gives the one-copy box
\(0\leq a\leq2\), \(0\leq b\leq1\). Its integer products strictly between
\(1\) and \(187\) are exactly

\[
2,\quad4,\quad47,\quad94.
\]

Their direct screens are:

| \(g\) | \(\gcd(g-1,187)\) | \(\gcd(g+1,187)\) |
|---:|---:|---:|
| 2 | 1 | 1 |
| 4 | 1 | 1 |
| 47 | 1 | 1 |
| 94 | 1 | 1 |

Modulo \(11\), \(2^5=-1\), so \(\operatorname{ord}_{11}(2)=10\). Modulo
\(17\), \(2^4=-1\), so \(\operatorname{ord}_{17}(2)=8\). Therefore

\[
\operatorname{ord}_{187}(2)=\operatorname{lcm}(10,8)=40.
\]

At the half order,

\[
2^{20}\equiv1\pmod{11},
\qquad
2^{20}\equiv-1\pmod{17}.
\]

In fact \(2^{20}\equiv67\pmod{187}\), and

\[
\gcd(67-1,187)=11,
\qquad
\gcd(67+1,187)=17.
\]

The exponent vector \((20,0)\) is in the unbounded exponent group but not in
the one-copy box. The complete enumeration above also shows that no equivalent
useful self-inverse state occurs inside that finite box.

## 9. The odd-\(t\) family

Let odd \(t\geq3\), \(G=2^t\),

\[
N=\frac{G^2-1}{3},
\qquad
B=\frac{N+1}{2}.
\]

Because \(G^2=4^t\equiv1\pmod3\), \(N\) is integral. Also

\[
N=1+4+\cdots+4^{t-1},
\]

which is odd because \(t\) is odd. The relation \(2B=N+1\) implies
\(B\equiv2^{-1}\pmod N\), so both blocks are units and one occurrence has
row \((1,1)\).

First determine the order of \(2\). The identity

\[
2^{2t}=G^2=1+3N
\]

shows that \(r=\operatorname{ord}_N(2)\) divides \(2t\). If \(r<2t\), then
as a proper divisor of \(2t\), \(r\leq t\). But then

\[
0<2^r-1\leq G-1<N,
\]

which is incompatible with \(N\mid 2^r-1\). Hence

\[
\operatorname{ord}_N(2)=2t.
\]

Now suppose the source has \(m<t\) indexed copies, and select any \(k\leq m\)
of them. Its box is \(0\leq a,b\leq k\). Since \(B\equiv2^{-1}\pmod N\),

\[
2^aB^b\equiv2^{a-b}\pmod N.
\]

If this residue is self-inverse, then

\[
2t\mid2(a-b),
\quad\text{so}\quad
t\mid a-b.
\]

But \(|a-b|\leq k<t\), hence \(a=b\). The corresponding integer is

\[
2^aB^a=(2B)^a=(N+1)^a.
\]

For \(a=0\) it equals the excluded endpoint \(1\); for \(a\geq1\) it is
larger than \(N\). Thus no legal divisor below \(N\) is self-inverse with
fewer than \(t\) copies.

With \(t\) copies, choose \((a,b)=(t,0)\). Its integer value is \(G\), and
for \(G\geq8\),

\[
1<G<N=\frac{G^2-1}{3}.
\]

It is self-inverse because \(G^2=1+3N\). It is non-global more explicitly
from

\[
N=(G-1)\frac{G+1}{3}.
\]

For odd \(t\), the two displayed factors are coprime and both exceed \(1\).
The residue \(G\) is \(+1\) modulo the first and \(-1\) modulo the second.
Thus it is a non-global involution (and its two gcds recover these two
factors).

For the old parity decoder, a subset containing \(k\) identical rows has
total row \((k,k)\). It is even only when \(k\) is even, and then its decoded
residue is

\[
2^{k/2}B^{k/2}=(2B)^{k/2}\equiv1\pmod N.
\]

Equivalently, \(L_0=\mathbb Z(1,1)\), and the formula for \(R_{\rm old}\)
also gives only the identity. Hence every old parity-decoder relation is
global.

Finally,

\[
\log_2 N
=2t-\log_2 3+\log_2(1-2^{-2t}),
\]

so \(t=\tfrac12\log_2N+O(1)=\Theta(\log N)\). The rows are identical, so the
argument is a lower bound on indexed occurrence multiplicity for the
self-inverse target. It is not a support lower bound. It is also not a lower
bound for the broader direct screen: already at \(t=3\), \(N=21\), and the
one-copy legal divisor \(2\) gives \(\gcd(2+1,21)=3\) even though it is not
self-inverse.

## Exact scope of the result

The reconstruction proves the modular identities, the exact-order oracle
equivalence, output-sensitive Smith postprocessing, and the stated finite
examples. It keeps three logically separate layers separate:

1. an element or lattice class in the unbounded modular group;
2. a representative inside a finite indexed-occurrence box;
3. a positive integer representative strictly between \(1\) and \(N\).

Passing from one layer to the next is not automatic. In particular, this
result gives no all-input classical method for selecting legal occurrences or
for factoring arbitrary \(N\).
