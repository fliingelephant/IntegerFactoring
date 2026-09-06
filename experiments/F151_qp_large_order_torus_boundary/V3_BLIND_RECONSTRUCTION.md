# F151 V3 statement-only blind reconstruction

## Source integrity and scope

The sole source for this reconstruction was `V3_STATEMENT.md`. Its verified
SHA-256 digest is

```text
73c8e7a8c58fd3fd40f56f3128ded748313a98cd9b76ec663bee9ec55ba50b98
```

The cited papers were not consulted. The HH and Pilatte results below are
therefore explicit premises. All other claims are reconstructed directly
from the statement.

This is a conditional boundary theorem. It is not a factoring algorithm.

## 1. Arithmetic and complexity interfaces

Let \(N\geq 3\), and set

\[
n=\lceil \log _2(N+1)\rceil .
\]

Let \(B\) be an integer such that

\[
4\leq B<N-1,
\qquad
B=2^{(\log n)^{O(1)}}.
\]

Thus \(B\), any polynomial in \(B\), and \(B\) times a polynomial in \(n\)
are quasipolynomial in the input length. Here quasipolynomial time means
\(2^{(\log n)^{O(1)}}\) bit operations. The base used for an unadorned
logarithm does not affect any asymptotic conclusion.

For every integer \(a\), define its canonical residue by

\[
[a]_N\in\{0,1,\ldots,N-1\},
\qquad
[a]_N\equiv a\pmod N.
\]

If \(c\in\{1,\ldots,N-1\}\) is a unit modulo \(N\), define the canonical
inverse

\[
\iota_N(c)=[c^{-1}]_N.
\]

It lies in \(\{1,\ldots,N-1\}\), and
\(c\iota_N(c)\equiv1\pmod N\). For a unit \(u\) modulo \(m\),
\(\operatorname{ord}_m(u)\) is the least positive \(t\) for which
\(u^t\equiv1\pmod m\).

Throughout, a proper divisor of \(N\) means an integer \(D\) with
\(1<D<N\).

## 2. External premises

### 2.1 HH premise

The statement attributes this premise to Harvey and Hittmeir,
*Deterministic methods for finding elements of large multiplicative order*,
arXiv:2601.11131v2, Theorem 1.1.

For \(N\geq3\) and \(1\leq B<N-1\), assume a deterministic algorithm that
returns either a proper divisor of \(N\), or a unit
\(\alpha\in(\mathbb Z/N\mathbb Z)^\times\) satisfying

\[
\operatorname{ord}_N(\alpha)>B.
\]

Its stated bit cost is

\[
O\!\left(
 \frac{B^{1/2}\log B}{(\log\log B)^{1/2}}\log N
\right),
\]

subject to the cited result's small-parameter convention. This premise is
used as a black box. Its displayed cost is quasipolynomial for the stated
size of \(B\).

### 2.2 Pilatte premise

The statement attributes this premise to Pilatte, *Unconditional
correctness of recent quantum algorithms for factoring and computing
discrete logarithms*, arXiv:2404.16450v2, Corollaries 1.4--1.5 and Theorem
3.18.

Put

\[
d=\lceil\sqrt{\log N}\rceil,
\qquad
X=d^{1000d}.
\]

Since \(d=\Theta(\sqrt n)\),
\(\log X=1000d\log d=O(\sqrt n\log n)\). Thus \(X\), and each sampled
generator below it, has a polynomial-size binary representation. The range
of possible values up to \(X\) is much larger than quasipolynomial, so this
observation does not justify enumerating that range.

For the stated experiment consisting of \(d\) independent random
small-prime generators from the eligible set bounded by \(X\), assume that,
with high probability, the full relation lattice has a basis all of whose
vectors have Euclidean norm

\[
\exp(O(d)).
\]

Only the ambient dimension, the probability qualifier, and this norm bound
are used. In particular, this premise supplies neither a classical basis
algorithm nor a support bound.

## 3. Exact-value decoder

### 3.1 Input normalization

The input is an ordered finite list of exact positive integers

\[
P_1,\ldots,P_s,
\qquad
P_i\equiv1\pmod N.
\]

Discard every occurrence of \(1\). Among repeated exact integer values,
retain only the first occurrence. Denote the resulting ordered list by

\[
A_1,\ldots,A_m.
\]

This rule depends on exact values, not on the endpoint expressions that
produced them. A removed \(1\) has no effect on a product or its root. An
extra copy of an exact value can only contribute an even copy, whose square
root contains a factor \(A_i\equiv1\pmod N\), or an odd copy equivalent to
the retained copy. Thus the normalization removes presentation artifacts.

### 3.2 Factor-free refinement

Starting with the \(A_i\), repeatedly split overlapping bases by integer
gcd and exact division. If two current bases \(g,h\) overlap, replacing them
by suitable factors formed from

\[
\gcd(g,h),
\qquad
g/\gcd(g,h),
\qquad
h/\gcd(g,h)
\]

preserves exact exponent coordinates. Continue until the nontrivial bases
are pairwise coprime. For each remaining base, use exact integer-root tests
to extract its maximal perfect-power exponent. This gives integers

\[
g_1,\ldots,g_t>1
\]

that are pairwise coprime and are not perfect powers, together with
nonnegative integers \(E_{ji}\) satisfying

\[
A_i=\prod_{j=1}^t g_j^{E_{ji}}.
\]

Gcd, exact division, and perfect-power detection do not require a
rational-prime factorization. Standard finite gcd refinement terminates
because each nontrivial split strictly refines the finite collection of
prime supports. All operations are polynomial in the total exact input
length.

Form the binary matrix

\[
M=(E_{ji}\bmod2)_{j,i}.
\]

### 3.3 Exact square criterion

For \(z\in\mathbb F_2^m\), use its \(0/1\) representatives and define

\[
Q_z=\prod_{i:z_i=1}A_i.
\]

Writing

\[
F_j=\sum_i E_{ji}z_i
\]

gives \(Q_z=\prod_jg_j^{F_j}\). If \(Mz=0\), every \(F_j\) is even, so
\(Q_z\) is a square.

Conversely, because \(g_j\) is not a perfect power, the gcd of the
exponents in its rational-prime factorization is \(1\); in particular,
some prime occurs in \(g_j\) to an odd exponent. Pairwise coprimality means
that this prime occurs in no other \(g_k\). If \(Q_z\) is a square, its
valuation at that prime is even, so \(F_j\) is even. This holds for every
\(j\). Hence

\[
\boxed{
Mz=0
\quad\Longleftrightarrow\quad
Q_z\text{ is an integer square}.
}
\]

A nonzero vector in \(K=\ker_{\mathbb F_2}M\) is therefore an exact-value
closure. For each closure, its positive exact square root

\[
R_z=\sqrt{Q_z}>0
\]

is computable without any choice of sign.

### 3.4 Root homomorphism and basis sufficiency

Every \(A_i\equiv1\pmod N\), so

\[
R_z^2=Q_z\equiv1\pmod N.
\]

The map

\[
\rho:K\longrightarrow
\{u\in(\mathbb Z/N\mathbb Z)^\times:u^2=1\},
\qquad
\rho(z)=R_z\bmod N,
\]

is a homomorphism. Indeed, if \(z,z'\in K\), exact multiplication gives

\[
Q_zQ_{z'}
=Q_{z+z'}
 \left(\prod_{i:z_i=z'_i=1}A_i\right)^2,
\]

where \(z+z'\) is binary addition. Positivity of all exact square roots
then gives

\[
R_zR_{z'}
=R_{z+z'}\prod_{i:z_i=z'_i=1}A_i.
\]

The last product is \(1\) modulo \(N\), proving the homomorphism claim.

Let \(b_1,\ldots,b_k\) be any complete binary basis of \(K\). If every
\(\rho(b_j)\) were \(1\) or \(-1\), then every product of basis images would
also be \(1\) or \(-1\). Therefore, if any closure has a non-global root,
meaning a root not congruent to \(1\) or \(-1\) modulo \(N\), some basis
vector has a non-global root.

For such a root \(R\), \(N\mid(R-1)(R+1)\), while neither \(R-1\) nor
\(R+1\) is divisible by \(N\). At least one of

\[
\gcd(R-1,N),
\qquad
\gcd(R+1,N)
\]

is therefore a proper divisor. Testing both gcds for each basis vector is
complete for detecting every non-global root available from the closure
space. The decoder reports progress only when one of these gcds is proper.

For the power-bank input below, there are \(O(B)\) values, each has
\(O(n)\) bits, and the exact refinement and binary linear algebra are
polynomial in that list size. Thus running this decoder on that bank is
also quasipolynomial. This complexity observation does not imply that the
kernel is nonzero or that any resulting root is useful.

## 4. Theorem 1: factor or large order in every prime component

Invoke the HH premise with target \(B\). If it returns a proper divisor,
return it. Otherwise it returns a unit \(\alpha\) with

\[
\operatorname{ord}_N(\alpha)>B.
\]

For every \(1\leq e\leq B\), compute

\[
D_e=\gcd(\alpha^e-1,N).
\]

Return \(D_e\) if it is proper. Suppose no scan value is proper. Let \(r\)
be any rational prime divisor of \(N\). If
\(t=\operatorname{ord}_r(\alpha)\leq B\), then \(r\mid D_t\), so
\(D_t>1\). It cannot equal \(N\), because that would give
\(\alpha^t\equiv1\pmod N\) and hence
\(\operatorname{ord}_N(\alpha)\leq t\leq B\), contrary to the HH output.
Thus \(D_t\) would be proper, contrary to the assumed scan outcome.
Consequently

\[
\boxed{
\operatorname{ord}_r(\alpha)>B
\quad\text{for every rational prime }r\mid N.
}
\]

The HH call is quasipolynomial. The scan can update the modular power
incrementally and uses \(B\) modular multiplications and gcds, so it is also
quasipolynomial. This proves the stated deterministic procedure.

The scan says nothing about correlations among distinct prime components
after exponent \(B\).

## 5. Theorem 2: nullness of every listed short-window screen

Assume the no-factor branch of Theorem 1 and put

\[
k=\lfloor B/4\rfloor.
\]

For \(1\leq e\leq k\), define

\[
c_e=[\alpha^e]_N,
\qquad
w_e=\iota_N(c_e).
\]

Modulo every prime \(r\mid N\), these satisfy

\[
c_e\equiv\alpha^e,
\qquad
w_e\equiv\alpha^{-e}.
\]

Fix such an \(r\), and take distinct eligible \(e,f\). Each possible zero
in a listed screen would force an order at most \(B\):

| screen zero modulo \(r\) | forced relation | resulting order bound |
| --- | --- | --- |
| \(c_e-c_f\) | \(\alpha^{|e-f|}=1\) | \(\operatorname{ord}_r(\alpha)\leq |e-f|<B\) |
| \(c_e+c_f\) | \(\alpha^{|e-f|}=-1\) | \(\operatorname{ord}_r(\alpha)\mid2|e-f|<B\) |
| \(c_ec_f-1\) | \(\alpha^{e+f}=1\) | \(\operatorname{ord}_r(\alpha)\leq e+f\leq2k\leq B/2\) |
| \(c_ec_f+1\) | \(\alpha^{e+f}=-1\) | \(\operatorname{ord}_r(\alpha)\mid2(e+f)\leq4k\leq B\) |
| \(c_e-w_e\) | \(\alpha^{2e}=1\) | \(\operatorname{ord}_r(\alpha)\leq2e\leq2k\leq B/2\) |
| \(c_e+w_e\) | \(\alpha^{2e}=-1\) | \(\operatorname{ord}_r(\alpha)\mid4e\leq4k\leq B\) |

Every bound contradicts
\(\operatorname{ord}_r(\alpha)>B\). No prime divisor of \(N\) divides any
screen value. Hence, for distinct eligible \(e,f\),

\[
\gcd(c_e-c_f,N)=
\gcd(c_e+c_f,N)=
\gcd(c_ec_f-1,N)=
\gcd(c_ec_f+1,N)=1,
\]

and, for every eligible \(e\),

\[
\boxed{
\gcd(c_e-w_e,N)=
\gcd(c_e+w_e,N)=1.
}
\]

Thus all listed positions are distinct, signed-distinct, inverse-distinct,
and signed-inverse-distinct in every hidden prime component.

### 5.1 Exact values remain unconstrained

Define

\[
P_e=c_ew_e.
\]

The canonical inverse property gives \(P_e\equiv1\pmod N\). Both factors
are positive. If \(P_e=1\), then \(c_e=w_e=1\), which would force
\(\alpha^e\equiv1\pmod r\) for every \(r\mid N\), contradicting
\(e\leq B\) and the component-order bound. Hence

\[
P_e=1+\kappa_eN
\qquad(\kappa_e\in\mathbb Z_{>0}).
\]

The modular screen proof contains no information about the ordinary
integer factorization of the \(P_e\). It therefore neither prevents exact
repetitions nor determines the parity kernel of their factor-free
refinement. In particular, it does not rule out a multi-column square whose
positive root is non-global modulo \(N\). Conversely, it does not guarantee
such a closure on every input.

### 5.2 Witness \(N=143\)

Take

\[
N=143=11\cdot13,
\qquad B=8,
\qquad \alpha=2.
\]

The component orders are

\[
\operatorname{ord}_{11}(2)=10,
\qquad
\operatorname{ord}_{13}(2)=12,
\]

so this is a certified window. Its two eligible exponents give

\[
(c_1,w_1)=(2,72),
\qquad
(c_2,w_2)=(4,36),
\]

and therefore

\[
P_1=P_2=144.
\]

The decoder's first-occurrence rule retains one value \(A_1=144\). A valid
factor-free refinement is \(144=12^2\), with \(12\) not a perfect power.
Thus the single column has zero parity and is a closure. Its exact root is
\(12\), and

\[
\gcd(12-1,143)=11,
\qquad
\gcd(12+1,143)=13.
\]

This example witnesses both an exact-value repetition and actual decoder
progress. It does not turn the capability into a universal claim.

### 5.3 Witness \(N=391\)

Take

\[
N=391=17\cdot23,
\qquad B=12,
\qquad \alpha=37.
\]

The component orders are

\[
\operatorname{ord}_{17}(37)=16,
\qquad
\operatorname{ord}_{23}(37)=22.
\]

The first two exact values are distinct:

\[
(c_1,w_1)=(37,74),
\qquad
P_1=2738,
\]

\[
(c_2,w_2)=(196,2),
\qquad
P_2=392.
\]

They satisfy

\[
P_1P_2=1{,}073{,}296=1036^2,
\]

so the vector selecting these two columns is an exact-value closure. For
example, the mathematical factor-free refinement

\[
2738=2\cdot37^2,
\qquad
392=2^3\cdot7^2
\]

has parity matrix, with rows \(2,37,7\),

\[
\begin{pmatrix}
1&1\\
0&0\\
0&0
\end{pmatrix}.
\]

This displayed rational-prime decomposition only verifies the closure; the
decoder need not find rational primes to obtain a valid factor-free
refinement. The useful root gives

\[
\gcd(1036-1,391)=23,
\qquad
\gcd(1036+1,391)=17.
\]

Again, this proves capability on one certified window, not success on every
window.

## 6. Theorem 3: the norm premise does not yield a QP full-ball catalogue

Since \(\log N=\Theta(n)\),

\[
d=\lceil\sqrt{\log N}\rceil=\Theta(\sqrt n).
\]

If a vector in \(\mathbb Z^d\) has norm at most \(\exp(Cd)\), each coordinate
has \(O(d)\) bits. All \(d\) coordinates therefore use \(O(d^2)=O(n)\)
bits. Thus every promised basis vector has a polynomial-size exact
description.

This fact does not imply sparse support. For example,
\((1,\ldots,1)\) uses all \(d\) coordinates and has norm \(\sqrt d\), well
inside \(\exp(Cd)\) for every fixed \(C>0\) and all sufficiently large
\(d\). A norm bound alone therefore cannot place a promised vector in a
polylogarithmic-support catalogue.

Now fix \(C>0\), set \(R=\exp(Cd)\), and let

\[
\mathcal B_d(R)=\{v\in\mathbb Z^d:\|v\|_2\leq R\}.
\]

The containing cube gives

\[
|\mathcal B_d(R)|\leq(2\lfloor R\rfloor+1)^d
=\exp(O(d^2)).
\]

For the reverse bound, put \(a=\lfloor R/\sqrt d\rfloor\). The cube
\([-a,a]^d\) lies in the radius-\(R\) ball, so

\[
|\mathcal B_d(R)|\geq(2a+1)^d.
\]

Its logarithm is

\[
d\bigl(Cd-\tfrac12\log d+O(1)\bigr)=\Theta(d^2).
\]

Consequently

\[
\boxed{
|\mathcal B_d(\exp(Cd))|
=\exp(\Theta(d^2))
=\exp(\Theta(n)).
}
\]

This is exponential, not quasipolynomial, in the input length \(n\).
Therefore the Pilatte norm premise supplies a high-probability existence
statement for short relations, but it does not by itself supply either a
polylogarithmic-support search or a quasipolynomial exhaustive catalogue of
the full norm ball.

This is an enumeration boundary, not a computational lower bound. A
classical structured sampler could avoid full-ball enumeration; the stated
premise neither supplies nor rules out such a sampler.

## 7. Theorem 4: obstruction to the direct fixed-coordinate torus splice

Now let

\[
N=pq
\]

for distinct odd primes \(p,q\). Let \(\Delta\) be a unit modulo \(N\) with
Jacobi symbol

\[
\left(\frac{\Delta}{N}\right)=-1.
\]

Because both local Legendre symbols are nonzero and their product is
\(-1\), exactly one of

\[
\left(\frac{\Delta}{p}\right),
\qquad
\left(\frac{\Delta}{q}\right)
\]

is \(1\), and the other is \(-1\). Call a component split in the first case
and nonsplit in the second.

Let \(\alpha\) satisfy the component-order conclusion of Theorem 1. Define
in \(\mathbb Z/N\mathbb Z\)

\[
x=\frac{\alpha+\alpha^{-1}}2,
\qquad
b=\Delta^{-1}(x^2-1).
\]

Division by \(2\) is valid because \(N\) is odd. Fix
\(r\in\{p,q\}\). In \(\mathbb F_r\),

\[
x^2-1
=\left(\frac{\alpha-\alpha^{-1}}2\right)^2.
\]

The square on the right is nonzero: otherwise \(\alpha^2=1\pmod r\),
which would give \(\operatorname{ord}_r(\alpha)\leq2<B\). Hence

\[
\begin{aligned}
\left(\frac br\right)
&=\left(\frac{\Delta^{-1}}r\right)
  \left(\frac{((\alpha-\alpha^{-1})/2)^2}r\right)\\
&=\left(\frac{\Delta}r\right).
\end{aligned}
\]

Therefore

\[
\boxed{
\left(\frac br\right)=\left(\frac\Delta r\right)
\quad(r=p,q).
}
\]

The equation

\[
x^2-\Delta y^2=1
\]

is equivalent locally to \(y^2=b\). It has a local \(y\) exactly in the
split component. Since the other component is nonsplit, the Chinese
remainder theorem shows that no global \(y\pmod N\) exists.

The usual split-coordinate map makes the obstruction explicit. If
\(\delta_r^2=\Delta\) in a split component, then

\[
y_r=\frac{\alpha-\alpha^{-1}}{2\delta_r}
\]

satisfies

\[
x+\delta_ry_r=\alpha,
\qquad
x-\delta_ry_r=\alpha^{-1},
\qquad
x^2-\Delta y_r^2=1.
\]

There is no corresponding square root \(\delta_r\) in the nonsplit base
field, and the fixed \(x\) admits no coefficient \(y_r\) there. Thus these
local formulas cannot be joined into one global torus point with this
fixed \(x\).

### 7.1 The fixed Kummer orbit forgets the orientation

Define

\[
T_0(X)=1,
\qquad
T_1(X)=X,
\qquad
T_{m+1}(X)=2XT_m(X)-T_{m-1}(X).
\]

Then, for every \(m\geq0\),

\[
\boxed{
T_m(x)=\frac{\alpha^m+\alpha^{-m}}2.
}
\]

The cases \(m=0,1\) are immediate. If the identity holds for \(m\) and
\(m-1\), substitution of \(2x=\alpha+\alpha^{-1}\) into the recurrence
cancels the two middle terms and gives the formula for \(m+1\).

The right-hand side contains no \(\Delta\). The scalar-to-\(x\) map and its
entire Chebyshev orbit therefore retain no information about which hidden
component is split. The only direct torus lift that would retain that
orientation requires the missing global \(y\).

This proves only the obstruction to the direct scalar-to-fixed-\(x\) Kummer
splice. It says nothing about other torus points, other coordinates,
multi-relation decoders tailored to a coordinate, or a new torus win--win
argument.

## 8. Reconstructed consequence and audit verdict

Conditional on the two explicit external premises, the statement proves:

1. A deterministic quasipolynomial procedure returns a factor or a unit
   whose order exceeds \(B\) in every prime component.
2. On the no-factor branch, every short-window modular collision,
   signed-collision, inverse-collision, and signed-inverse-collision listed
   in Theorem 2 is null.
3. These null screens do not control exact integer carries, repeated exact
   products, or the exact-value parity kernel. Both supplied witnesses
   demonstrate residual decoder capability.
4. The Pilatte norm bound permits polynomial-size witnesses but leaves an
   exponential-size full ball and gives no support bound.
5. The direct scalar-to-fixed-Kummer construction cannot combine the
   Jacobi split/nonsplit orientation into a global torus point, and its
   Chebyshev orbit is independent of that orientation.

No internal self-containment or implication defect was found in these
deductions. The HH theorem and the Pilatte relation-lattice assertion are
not proved by the statement; they are clearly declared external premises,
so the conclusions are conditional on them. The phrases "eligible set"
and "with high probability" inherit their detailed sampling semantics from
the Pilatte premise, so this reconstruction cannot attach a numerical
failure probability. That limits external verification, but none of the
elementary implications silently uses a stronger probability, support, or
algorithmic assertion.

In particular, the result does not provide a factor-correlated sampler and
does not claim a factoring algorithm. It also does not exclude larger
exponents, component-order mismatch beyond \(B\), integer carries,
structured relation sampling, exact-value closures, or other torus
coordinates.
