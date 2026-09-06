# Proof of the F202 candidate

## 1. Square-gap algebra

Since \(p<\sqrt N<q\),

\[
p\leq B<q.
\tag{1}
\]

Thus \(a=B-p\geq0\) and \(c=q-B>0\).  Expanding
\(N=(B-a)(B+c)\) gives

\[
N=B^2+B(c-a)-ac,
\]

and hence

\[
E=Bd-ac.
\tag{2}
\]

Using \(p=B-a\), equation (2) gives

\[
a^2+E
=a^2+Bd-ac
=(B-a)d
=pd.
\tag{3}
\]

Similarly, since \(q=B+c\),

\[
c^2+E
=c^2+Bd-ac
=(B+c)d
=qd.
\tag{4}
\]

Also,

\[
d=c-a=p+q-2B.
\tag{5}
\]

The strict AM--GM inequality for the distinct primes gives

\[
p+q>2\sqrt{pq}\geq2B,
\]

so \(d>0\).  The numbers \(p,q\) are odd, so \(d\) is even.  From
\(B\geq p\),

\[
d=p+q-2B\leq q-p<p,
\tag{6}
\]

where the last inequality is the balance condition \(q<2p\).

Substituting (5) and \(E=N-B^2\) gives

\[
\begin{aligned}
d^2+4Bd-4E
&=(p+q-2B)^2+4B(p+q-2B)-4(N-B^2)\\
&=(p+q)^2-4pq\\
&=(q-p)^2.
\end{aligned}
\tag{7}
\]

Thus, given \(d\), square-test the left side of (7), call its nonnegative
square root \(s\), and recover

\[
p={2B+d-s\over2},
\qquad
q={2B+d+s\over2}.
\tag{8}
\]

Exact multiplication verifies the result.

## 2. Child size and recursive cost

The definition of \(B\) gives

\[
B^2<N<(B+1)^2.
\]

Since \(N\) is an integer,

\[
1\leq E=N-B^2\leq2B.
\tag{9}
\]

The promised semiprime has \(N\geq15\), hence \(n\geq4\).  Since
\(N<2^n\),

\[
E\leq2B<2\sqrt N<2^{n/2+1}\leq2^{n-1}.
\tag{10}
\]

Therefore the bit length of \(E\) is at most \(n-1\).

Furthermore,

\[
\gcd(E,N)
=\gcd(N-B^2,N)
=\gcd(B^2,N).
\tag{11}
\]

Because \(0<B^2<N\), a value larger than one in (11) is proper.  On the
remaining branch, squarefreeness of \(N\) gives

\[
\gcd(B,N)=\gcd(E,N)=1.
\tag{12}
\]

Now suppose, conditionally, that a postprocessor with cost \(Q(n)\) factors
every promised \(N\) from the complete factorization of \(E\).  Make one
recursive complete-factorization call on \(E\), then invoke the
postprocessor.  With a monotone worst-case running-time envelope,

\[
T(n)\leq T(n-1)+Q(n).
\tag{13}
\]

Iteration gives

\[
T(n)\leq T(3)+\sum_{j=4}^{n}Q(j)
\leq T(3)+nQ(n).
\tag{14}
\]

Multiplication by \(n\) is absorbed into the exponent of a numerical-QP
bound.  This proves only that the proposed one-child recursion is
complexity-safe.

## 3. Mixed roots and principal norms

On branch (12), \(B\) is a unit modulo both \(p\) and \(q\).  The congruence

\[
B^2\equiv-E\pmod N
\tag{15}
\]

has two sign choices in each prime field and hence four CRT roots.  The
equal-sign choices are \(B\) and \(-B\).  For a mixed root \(r\), exactly one
of \(p,q\) divides \(r-B\), while the other divides \(r+B\).  Neither
difference is zero modulo both primes.  Therefore

\[
\{\gcd(r-B,N),\gcd(r+B,N)\}=\{p,q\}.
\tag{16}
\]

Conversely, knowing \(p,q\) lets one choose opposite signs modulo the two
primes and combine them by CRT.  This proves the exact equivalence.

Suppose next that

\[
x^2+Ey^2=N.
\tag{17}
\]

If \(p\mid y\), then (17) gives \(p\mid x\), which would make \(p^2\mid N\).
This contradicts squarefreeness.  The same holds for \(q\), so
\(\gcd(y,N)=1\).  Set \(r=xy^{-1}\pmod N\).  Equation (17) gives

\[
r^2\equiv-E\pmod N.
\tag{18}
\]

If this is a mixed root, (16) factors.  If it is \(\pm B\), the
representation gives no new CRT orientation.

## 4. Moduli supported on the child

Let \(m\mid E\).  Equation (12) and

\[
\gcd(B,E)=\gcd(B,N-B^2)=\gcd(B,N)
\]

show that \(B\) is a unit modulo \(m\).  Also,

\[
N\equiv B^2\pmod m.
\tag{19}
\]

For an arbitrary unit \(x\pmod m\), set \(y=Nx^{-1}\).  The identity

\[
(x+y)^2-4xy=(x-y)^2
\tag{20}
\]

proves the trace-discriminant assertion.  With

\[
d_x=x+N x^{-1}-2B,
\]

equation (19) yields

\[
d_x=x+B^2x^{-1}-2B={(x-B)^2\over x}\pmod m
\tag{21}
\]

and

\[
d_x+4B={(x+B)^2\over x}\pmod m.
\tag{22}
\]

Since \(E\equiv0\pmod m\), multiplication of (21)--(22) gives

\[
d_x^2+4Bd_x-4E
=\left({x^2-B^2\over x}\right)^2\pmod m.
\tag{23}
\]

Thus every unit candidate factor residue satisfies all of these local
conditions.  The proof does not say that every arbitrary \(d\pmod m\)
passes, and it does not analyze a modulus not supported on \(E\).

## 5. The proper ideal-class orientation

Let

\[
\mathcal O=\mathbb Z[\sqrt{-E}]
\]

and \(\alpha=B+\sqrt{-E}\).  Its norm is \(N\).  On (12), the primes \(p,q\)
are coprime to the discriminant and conductor of the order.  They split, and
the prime ideals selected by divisibility of \(\alpha\) satisfy

\[
(\alpha)=\mathfrak p\mathfrak q.
\tag{24}
\]

Taking proper ideal classes in (24) gives, with \(C=[\mathfrak p]\),

\[
[\mathfrak q]=C^{-1}.
\tag{25}
\]

For a root \(s\) of \(-E\pmod N\), use the proper ideal

\[
I_s=(N,s+\sqrt{-E}).
\tag{26}
\]

The public root \(s=B\) selects \(\mathfrak p\) and \(\mathfrak q\), so
\(I_B=(\alpha)\).  Choose the mixed root that keeps the \(B\)-sign modulo
\(p\) and reverses it modulo \(q\).  It selects
\(\mathfrak p\overline{\mathfrak q}\), and hence

\[
[I_s]
=[\mathfrak p][\overline{\mathfrak q}]
=C[\mathfrak q]^{-1}
=C^2.
\tag{27}
\]

The other mixed root gives \(C^{-2}\).

Every genus character is a homomorphism to \(\{\pm1\}\).  Therefore

\[
\chi(C^2)=\chi(C)^2=1.
\tag{28}
\]

The mixed class is in the principal genus, whether or not it is principal.

The ideal \(I_s\) has norm \(N\).  It is principal exactly when a generator
\(x+y\sqrt{-E}\) has norm

\[
x^2+Ey^2=N.
\]

Consequently a factor-bearing principal norm representation exists exactly
when \(C^2=1\).  Canonical invertible ambiguous classes arising from
ramified discriminant factors satisfy \(A=A^{-1}\), hence \(A^2=1\).  Their
compositions remain in a two-torsion subgroup, which need not contain a
nontrivial square such as \(C^2\).

## 6. The exact finite certificate

Direct multiplication gives

\[
37\cdot71=2627,
\qquad
51^2=2601,
\qquad
52^2=2704.
\]

Thus \(B=51\) and \(E=26=2\cdot13\).  The balance inequality is
\(71<74\).  The offsets are

\[
a=51-37=14,
\qquad
c=71-51=20,
\qquad
d=6.
\]

They give

\[
26=51\cdot6-14\cdot20,
\]

\[
14^2+26=37\cdot6,
\qquad
20^2+26=71\cdot6,
\]

and

\[
6^2+4\cdot51\cdot6-4\cdot26=34^2.
\]

For \(r=162\),

\[
r^2+26=26270=10\cdot2627.
\]

Also,

\[
r-51=111=3\cdot37,
\qquad
r+51=213=3\cdot71,
\]

which proves the two gcd claims.

It remains to exclude another principal norm representation.  If

\[
x^2+26y^2=2627,
\tag{29}
\]

then \(x\) is odd and \(x^2\equiv1\pmod {13}\).  Since \(|x|\leq51\),

\[
|x|\in\{1,25,27,51\}.
\]

Substitution in (29) gives

\[
y^2\in\{101,77,73,1\}.
\]

Only the last value is a square.  This proves that the only solutions are
\((\pm51,\pm1)\).

The form attached to \(r=162\) is

\[
F_r=[2627,324,10],
\]

whose discriminant is

\[
324^2-4\cdot2627\cdot10=-104.
\]

The following proper reductions are elementary swaps and shears:

\[
[2627,324,10]
\sim[10,-324,2627]
\sim[10,-4,3]
\sim[3,4,10]
\sim[3,-2,9].
\tag{30}
\]

The last form is reduced and is not the reduced principal form
\([1,0,26]\).  Hence it is nonprincipal.

For the fundamental discriminant \(-104=(-8)\cdot13\), the ramified prime
forms are represented by

\[
[2,0,13]
\quad\text{and}\quad
[13,0,2].
\]

They are properly equivalent.  The reduced form \([2,0,13]\) is
nonprincipal and ambiguous, so its class has order two.  Therefore the
subgroup generated by the factor-supported ramified classes is exactly

\[
\{[1,0,26],[2,0,13]\},
\]

which does not contain the reduced mixed form \([3,-2,9]\).  Finally,
\(d=6\) has the prime divisor \(3\nmid2E\), disproving a divisor-support
cover of \(d\) by the factors of \(E\).

## 7. Scope of the obstruction

The proof establishes three exact failures:

1. a second principal norm representation is not forced;
2. product and discriminant consistency modulo divisors of \(E\) do not
   reject any unit candidate factor residue; and
3. genus characters and compositions of the directly ramified ambiguous
   classes need not reach the mixed-root class.

It proves no time lower bound for a general postprocessor given
`factor(E)`.  The missing algorithm may use nonlocal auxiliary moduli, the
full proper class group without enumeration, Archimedean size information,
or a statistic that directly biases the P175 reciprocal lift.
