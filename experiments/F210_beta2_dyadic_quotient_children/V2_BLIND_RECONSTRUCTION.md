# F210 V2 blind reconstruction

## Verdict

**STRICT PASS within the declared scope.** Starting only from PROMPT.md and
V2_STATEMENT.md, I reconstructed every displayed identity and every
non-imported implication. I found no false formula, sign error, parity
error, missing coalescence case, invalid lift count, order-stripping gap, or
recursion overclaim.

The result is not a solution of the top-level factoring prompt. It assumes a
balanced distinct-semiprime input, grants a correct reciprocal prefix, and
uses complete child factorizations only conditionally. The statement says
all three things explicitly.

The interfaces attributed to P179, P183, and P172 are imports. Under the
blind-review restriction, I did not inspect their proofs. This
reconstruction verifies that the F210 V2 conclusions follow from the
imported interfaces exactly as stated. It does not independently reverify
the imported results.

## Source boundary and integrity

Before reading V2_STATEMENT.md, I computed its SHA-256:

d71fadf26f194f067647d7cee3ac8bcdfbc2d84c1d518d356f0df0c1e1268fa0.

It matches the supplied expected hash exactly. I then read only the
workspace PROMPT.md and V2_STATEMENT.md. I did not inspect a proof, audit,
manifest, provenance file, ledger, or prior reconstruction.

## 1. Reconstruction of the dyadic state

Because

\[
r\equiv p\pmod m,\qquad c\equiv q\pmod m,
\]

there are positive integers \(P,Q\) such that

\[
p=r+mP,\qquad q=c+mQ.
\]

They are positive because \(0<r,c<m<p<q\). Expanding \(N=pq\) gives

\[
N=rc+m(cP+rQ+mPQ),
\]

and hence

\[
K=\frac{N-rc}{m}=cP+rQ+mPQ.
\tag{R1}
\]

In particular, \(K\) is an integer. Since \(m\) is even and \(r,c\) are
odd,

\[
\delta\equiv K\equiv P+Q\pmod2.
\tag{R2}
\]

Let \(a=P\bmod2\). This is the unique next binary lift of \(p\), since the
two lifts of \(r\bmod m\) modulo \(2m\) are \(r\) and \(r+m\). If
\(b=Q\bmod2\), then (R2) gives

\[
b=a\mathbin{\mathsf{xor}}\delta.
\]

Thus the definition of \(b_a\) is forced, not assumed. For the true value
of \(a\),

\[
p=r_a+h\frac{P-a}{2},\qquad
q=c_a+h\frac{Q-b_a}{2}.
\tag{R3}
\]

This also establishes directly why that chart contains \((p,q)\).

All quantities defining either child are public. Moreover,

\[
0<r_a,c_a<2m<p.
\]

Therefore

\[
0<r_ac_a<p^2<pq=N.
\]

It follows that both \(K_a=(N-r_ac_a)/(2m)\) are positive and satisfy

\[
K_a<\frac{N}{2m}.
\tag{R4}
\]

Their integrality follows either from the parity formulas below or from the
lift relation

\[
N\equiv r_ac_a\pmod {2m}.
\]

Finally, suppose \(p\mid K_a\). Since \(p\nmid2m\), the identity

\[
2mK_a=N-r_ac_a
\]

would imply \(p\mid r_ac_a\). This is impossible because both factors are
strictly between zero and \(p\). The same argument for \(q\) is even
stronger, since \(r_a,c_a<p<q\). Hence

\[
\gcd(K_a,N)=1.
\tag{R5}
\]

This reconstructs the positivity and coprimality properties used later.

## 2. Exact child formulas, difference, and coalescence

If \(\delta=0\), then \(b_0=0\) and \(b_1=1\). Using \(N-rc=mK\),

\[
K_0=\frac{N-rc}{2m}=\frac K2,
\]

and

\[
\begin{aligned}
K_1
&=\frac{N-(r+m)(c+m)}{2m}\\
&=\frac{mK-m(r+c+m)}{2m}\\
&=\frac{K-r-c-m}{2}.
\end{aligned}
\]

If \(\delta=1\), then \(b_0=1\) and \(b_1=0\), so

\[
K_0=\frac{N-r(c+m)}{2m}=\frac{K-r}{2},
\]

and

\[
K_1=\frac{N-(r+m)c}{2m}=\frac{K-c}{2}.
\]

The numerators have the required parity: \(K\) is even in the first case,
while \(K,r,c\) are odd in the second case.

Subtracting gives

\[
D=K_0-K_1=
\begin{cases}
(r+c+m)/2,&\delta=0,\\
(c-r)/2,&\delta=1.
\end{cases}
\tag{R6}
\]

When \(\delta=0\), the first expression is strictly positive. When
\(\delta=1\), it vanishes exactly when \(r=c\). Therefore

\[
K_0=K_1
\iff \delta=1\ \text{and}\ r=c.
\tag{R7}
\]

At \(t=1\), \(m=2\), the only canonical odd residue is \(1\), so \(r=c=1\).
If \(N\equiv3\pmod4\), then

\[
K=\frac{N-1}{2}
\]

is odd. Thus this is the coalesced branch and

\[
K_0=K_1=\frac{K-1}{2}=\frac{N-3}{4}.
\]

Outside coalescence, the Euclidean gcd identity gives

\[
\gcd(K_0,K_1)
=\gcd(K_0,K_0-K_1)
=\gcd(K_0,|D|)
=\gcd(K_1,|D|).
\tag{R8}
\]

Thus every prime power dividing both children divides the public
difference. The size bounds follow only from
\(1\leq r,c\leq m-1\):

\[
0<D=\frac{r+c+m}{2}
\leq\frac{3m-2}{2}<\frac{3m}{2}
\quad(\delta=0),
\]

and, outside coalescence,

\[
0<|D|=\frac{|c-r|}{2}
\leq\frac{m-2}{2}<\frac m2
\quad(\delta=1).
\]

For positive integers, the standard product formula then gives

\[
\operatorname{lcm}(K_0,K_1)
=\frac{K_0K_1}{\gcd(K_0,K_1)}
=\frac{K_0K_1}{g}.
\tag{R9}
\]

Nothing in (R8) or (R9) removes the prime-power support private to one
child. The statement correctly avoids that stronger conclusion.

## 3. Reconstruction of the half-translation

Put \(\sigma=(-1)^\delta\). The two charts always satisfy

\[
r_1=r_0+m,\qquad c_1=c_0+\sigma m.
\tag{R10}
\]

Also, the two cases of (R6) can be written uniformly as

\[
K_0-K_1=\frac{\sigma(r_0+m)+c_0}{2}.
\tag{R11}
\]

Expand the claimed translate:

\[
\begin{aligned}
F_1(P-\tfrac12,Q-\tfrac{\sigma}{2})
={}&hPQ+
\left(c_1-\frac{\sigma h}{2}\right)P+
\left(r_1-\frac h2\right)Q\\
&+\frac{\sigma h}{4}
-\frac{c_1}{2}
-\frac{\sigma r_1}{2}
-K_1.
\end{aligned}
\]

Since \(h=2m\), (R10) makes the two linear coefficients \(c_0,r_0\).
The constant term simplifies, using (R10) and (R11), to \(-K_0\).
Consequently,

\[
F_1(P-\tfrac12,Q-\tfrac{\sigma}{2})=F_0(P,Q).
\tag{R12}
\]

This is an identity over \(\mathbb Z[1/2]\). It does not assert an integral
translation.

For the matrix form, direct multiplication gives

\[
\begin{pmatrix}1&0\\ \sigma/2&1\end{pmatrix}
\begin{pmatrix}r_0&h\\-K_0&c_0\end{pmatrix}
\begin{pmatrix}1&0\\1/2&1\end{pmatrix}
=
\begin{pmatrix}r_0+m&h\\-K_1&c_0+\sigma m\end{pmatrix},
\]

where the lower-left entry is again (R11). This is \(A_1\). In addition,

\[
\det A_a=r_ac_a+hK_a=N.
\tag{R13}
\]

Both translating matrices have determinant one.

In physical coordinates,

\[
\begin{aligned}
XY
&=(hP+r_a)(hQ+c_a)\\
&=h(hPQ+c_aP+r_aQ)+r_ac_a.
\end{aligned}
\]

Thus \(F_a(P,Q)=0\) is equivalent to

\[
XY=hK_a+r_ac_a=N.
\tag{R14}
\]

The half-translation aligns the physical coordinates exactly. Indeed, if
\[
P_1=P_0-\frac12,\qquad Q_1=Q_0-\frac{\sigma}{2},
\]
then

\[
hP_1+r_1=hP_0+r_0,\qquad
hQ_1+c_1=hQ_0+c_0.
\tag{R15}
\]

Over any ring where \(2\) is a unit, the translation has a public inverse.
It therefore gives an affine isomorphism of the two solution schemes. For
every odd modulus, it in particular gives a bijection of congruence
solutions. Any datum that genuinely depends only on that isomorphism class
must agree: point counts, scheme-theoretic singularity and multiplicity
data, coordinate-free Frobenius data where defined, and genus or class data
of the same abstract split curve. Once coordinates are aligned, the two
equations are literally (R14), so aligned elimination invariants agree as
well.

This argument does not identify statistics evaluated on the two unaligned
and differently factored child integers. The statement correctly excludes
raw Jacobi and higher-residue comparisons from the conclusion.

## 4. Information from a factored child

Let an odd prime power \(\ell^e\) divide \(K_a\). By (R5), \(N\) is a unit
modulo \(\ell^e\). Reducing

\[
N-r_ac_a=hK_a
\]

gives

\[
N\equiv r_ac_a\pmod{\ell^e}.
\tag{R16}
\]

The product on the right is a unit in the local ring, so both \(r_a\) and
\(c_a\) are units. Every multiplicative character therefore satisfies

\[
\chi(N)=\chi(r_a)\chi(c_a).
\tag{R17}
\]

Multiplying (R16) by \(r_ac_a^{-1}\) gives the public scaled square:

\[
Nr_ac_a^{-1}\equiv r_a^2\pmod{\ell^e}.
\tag{R18}
\]

This is not an unscaled square root of \(N\). Removing the scale would
require additional information about \(r_ac_a^{-1}\). Thus (R16)--(R18)
hold for each child separately without proving that asymmetric
factorization statistics agree.

## 5. Exact finite \(2\)-adic lift count

Fix \(s\geq t+1\). There are exactly

\[
\frac{2^s}{h}=2^{s-t-1}
\tag{R19}
\]

residue classes \(X\bmod2^s\) satisfying
\(X\equiv r_a\pmod h\). Every such \(X\) is odd, hence a unit modulo
\(2^s\). It determines exactly one

\[
Y\equiv NX^{-1}\pmod{2^s}.
\]

Reducing this relation modulo \(h\), and using
\(N\equiv r_ac_a\pmod h\), gives

\[
Y\equiv Nr_a^{-1}\equiv c_a\pmod h.
\]

Conversely, every pair in \(\mathcal S_a(s)\) arises from its first
coordinate in this way. Therefore

\[
|\mathcal S_a(s)|=2^{s-t-1}
\]

for each \(a\). Existence and multiplicity at every finite \(2\)-adic level
are identical, so neither can select the true child.

## 6. The nontrivial balanced integer point

For the true lift bit, (R3) gives an integral chart point with physical
coordinates \((p,q)\). It satisfies

\[
1<p<\sqrt{pq}<q<pq,
\]

and hence the displayed strict condition

\[
1<X<\sqrt N<Y<N,\qquad XY=N.
\tag{R20}
\]

Conversely, a positive integer solution of \(XY=pq\) satisfying (R20) must
have \(X\) equal to a nontrivial divisor below \(\sqrt N\). The only such
divisor is \(p\), and then \(Y=q\). Therefore (R20) identifies the ordered
pair \((p,q)\) uniquely. Only the true residue chart contains it.

In coalescence, \(\delta=1\) and \(r=c\). The two charts exchange their
physical residue classes:

\[
(r_0,c_0)=(r,r+m),\qquad
(r_1,c_1)=(r+m,r).
\]

Since the true lifts of \(p,q\) are opposite, the other chart contains
\((q,p)\). This point reverses the middle orientation in (R20). A chart may
also contain \((1,N)\) or \((N,1)\); the outer strict inequalities exclude
those endpoints. This explains why the valid claim is uniqueness of the
nontrivial oriented balanced point, not uniqueness of all integral points
or of a point satisfying only \(X<\sqrt N<Y\).

The half-translation is not integral, so the odd-local isomorphism does not
decide this bounded integral-point condition. The stated Archimedean
qualification is necessary.

## 7. Conditional common-order bridge

Given complete factorizations of \(K_0,K_1\), the factorizations of

\[
H_a=hK_a
\]

are known because \(h\) is a public power of two. Their gcd is

\[
G=\gcd(hK_0,hK_1)=h\gcd(K_0,K_1)=hg,
\tag{R21}
\]

and its complete factorization is known as well.

Let \(w\) be a unit modulo \(N\). A value

\[
d_a=\gcd(w^{H_a}-1,N)
\]

strictly between \(1\) and \(N\) is immediately a proper factor. If both
values equal \(N\), then \(w^{H_0}=w^{H_1}=1\pmod N\). Equivalently, both
local orders

\[
e_p=\operatorname{ord}_p(w),\qquad
e_q=\operatorname{ord}_q(w)
\]

divide \(H_0\) and \(H_1\), and hence divide \(G\). This also proves
\(w^G=1\pmod N\). The unit hypothesis is what permits the same conclusion
from a Bezout relation between the exponents.

Here is the exact factor-first stripping argument. Start with \(E=G\), for
which \(e_p,e_q\mid E\). For each known prime factor \(\ell\) of \(E\),
test

\[
\gcd(w^{E/\ell}-1,N).
\]

- A proper gcd factors \(N\).
- If the gcd is \(N\), both local orders divide \(E/\ell\), so replace
  \(E\) by \(E/\ell\) and repeat.
- If the gcd is \(1\), neither local order divides \(E/\ell\). Therefore
  both local orders have the full current \(\ell\)-adic valuation of \(E\),
  and this prime can no longer be stripped.

If no proper factor occurs, this procedure determines the same valuation
for \(e_p\) and \(e_q\) at every prime dividing \(G\). At termination,

\[
E=e_p=e_q=:e,
\qquad e\mid G.
\tag{R22}
\]

All tested exponents have \(O(n)\) bits because \(G\leq H_a<N\), and the
factorization of \(G\) is supplied. Thus the stripping itself has
polynomial bit cost.

The common order divides \(p-1\), so \(e<p<q\). It follows immediately that

\[
\gcd(e,N)=1.
\tag{R23}
\]

Under the imported P172 interface, the additional condition

\[
\frac{N^{1/4}}e\leq Q(n)
\]

then gives a numerical-QP factoring terminal. Nothing in the preceding
argument guarantees the simultaneous \(d_0=d_1=N\) branch or the required
lower bound on \(e\).

For the polynomial claim, cyclotomic factorization gives

\[
X^H-1=\prod_{d\mid H}\Phi_d(X).
\]

The common cyclotomic factors for exponents \(H_0,H_1\) are precisely those
with \(d\mid\gcd(H_0,H_1)=G\). With the monic gcd convention,

\[
\gcd_{\mathbb Z[X]}(X^{H_0}-1,X^{H_1}-1)=X^G-1.
\tag{R24}
\]

Both polynomials contain \(X-1\), so their ordinary resultant is zero.
Thus \(G\), rather than the zero resultant, is exactly the shared-root
exponent datum.

The cases \(d_0,d_1\in\{1,N\}\) not covered by simultaneous \(N\) remain
unresolved. In particular, an asymmetric pair exposes a public asymmetry
but the reconstruction supplies no theorem tying its direction to the true
lift bit. The statement does not claim one.

## 8. Child size and recursion accounting

The bit-length definition gives

\[
N<2^n.
\]

Combining this with (R4) and \(h=2^{t+1}\) yields

\[
K_a<\frac{N}{2^{t+1}}<2^{n-t-1}.
\tag{R25}
\]

Since \(K_a\) is a positive integer, its input bit length is at most
\(n-t-1\). If

\[
t\geq\eta n-C
\]

for a fixed constant \(C\), this is at most

\[
(1-\eta)n+C-1.
\tag{R26}
\]

Thus the two calls at such a stage are fixed-ratio side calls. A
numerical-QP number of them is absorbed into the coefficient \(Q(n)\) in

\[
T(n)\leq T(n-1)
+Q(n)T((1-\eta)n+O(1))+Q(n).
\tag{R27}
\]

For completeness, the numerical-QP closure can be seen directly. For
sufficiently large \(n\), absorb the additive constant in the side-child
argument into some fixed ratio \(\rho<1\). Unrolling the decrement spine
once gives a bound of the form

\[
T(n)\leq nQ(n)\bigl(T(\rho n)+1\bigr).
\tag{R28}
\]

Iterate (R28) through \(O(\log n)\) fixed-ratio levels. If

\[
Q(x)=2^{C(\log_2(x+1))^k},
\]

the logarithm of the accumulated product is bounded by

\[
O\left(
\sum_i(\log n_i)^k+\sum_i\log n_i
\right)
=O\bigl((\log n)^{k+1}+(\log n)^2\bigr),
\]

where \(n_i\asymp\rho^i n\). This is still
\(2^{(\log n)^{O(1)}}\). It reconstructs the P183-form accounting without
turning it into a correctness or selector claim.

At the stated P175 precision, write

\[
t=\left\lfloor\frac{\log_2N}{4}\right\rfloor-R(n),
\qquad R(n)=(\log n)^{O(1)}.
\]

Since \(\log_2N\geq n-1\), (R25) gives child bit length at most

\[
n-t-1
\leq \frac{3n}{4}+R(n)+O(1).
\tag{R29}
\]

For every fixed \(\rho>3/4\), the polylogarithmic excess in (R29) is less
than \((\rho-3/4)n\) for all sufficiently large \(n\). Hence both children
fit a \(\rho n\) side-call bound at those late stages.

This argument does not apply to branching at \(t=o(n)\). In that range,
\(h=2^{o(n)}\) and \(r_ac_a<h^2=2^{o(n)}\), while \(N=2^{\Theta(n)}\).
Thus both

\[
K_a=\frac{N-r_ac_a}{h}
\]

can have \(n-o(n)\) bits. Recursing on both at every early stage is not a
fixed-ratio side-child recurrence and can form an uncontrolled binary tree.
In contrast, one decrement spine satisfying
\[
T(n)\leq T(n-1)+Q(n)
\]
unrolls to \(T(n)\leq T(n_0)+nQ(n)\), which is numerical QP. The missing
work is exactly a rule that constructs that single chain and reaches the
late safe range.

## 9. Strict scope conclusion

The statement proves the following narrow facts:

1. the exact two child formulas and their only coalescence condition;
2. confinement of common child support to the public difference;
3. exact odd-local affine equivalence after half-translation;
4. equality of finite \(2\)-adic lift counts;
5. uniqueness of the nontrivial oriented balanced integer point;
6. a conditional factor-first bridge to a fully known common local order;
7. the exact common exponent polynomial \(X^G-1\); and
8. numerical-QP safety of both-child factorizations only after a
   fixed-ratio precision threshold.

It does not prove that complete factorizations of \(K_0,K_1\) select the
next bit. It does not construct the granted prefix, force a useful order
branch, test the balanced integral point efficiently, justify early
two-child recursion, or produce an all-input factoring algorithm.

Accordingly, F210 V2 passes as its stated conditional boundary result. It
does not satisfy the success criteria of PROMPT.md by itself, and it does
not claim to.
