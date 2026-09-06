# F252 proof — Pell polynomial independence and resultant localization

## 1. Setup and the supplied modular roots

For one row, write

\[
f(X)=1+D(T-kX)^2
=Dk^2X^2-2DTkX+(1+DT^2).
\]

The Pell identity gives

\[
1+DT^2=S^2.
\]

At \(X=N\), with \(y=T-kN\), one has

\[
a=f(N)=1+Dy^2
\equiv1+DT^2=S^2\pmod N.
\]

Thus \(S\bmod N\) is the supplied square root. Moreover,
\(\gcd(S,N)=1\) if and only if \(\gcd(a,N)=1\), because a prime divides
\(S\) and \(N\) exactly when it divides \(S^2\equiv a\pmod N\). The
normalized-root statements are made only on this clean unit branch.

## 2. Exact content and irreducibility

If \(k=0\), then \(f=S^2\), so the row is a constant integer square.

Assume \(k\ne0\). Its coefficient content is initially

\[
c=\gcd(Dk^2,2DTk,S^2).
\]

The Pell identity implies

\[
\gcd(S,D)=1,
\qquad
\gcd(S,T)=1.
\]

Indeed, a common prime in either pair would divide
\(S^2-DT^2=1\). Every prime that divides \(c\) divides \(S\), and at every
such prime both \(D\) and \(T\) are units. Taking valuations therefore gives

\[
v_p(c)
=
\min\{2v_p(S),2v_p(k),v_p(2k)\}.
\]

This is exactly the valuation formula for

\[
\boxed{c=\gcd(S^2,k^2,2k)}.
\]

This content need not be one. For example, the Pell solution
\(99^2-2\cdot70^2=1\) and \(k=3\) give content \(3\). Dividing by \(c\)
is therefore necessary before invoking primitivity.

The discriminant of \(f\) is

\[
(-2DTk)^2-4(Dk^2)(S^2)
=4Dk^2(DT^2-S^2)
=-4Dk^2.
\]

After division by the content, the primitive quadratic has discriminant

\[
-\frac{4Dk^2}{c^2}<0.
\]

A quadratic over \(\mathbb Q\) is reducible exactly when its discriminant is
a square in \(\mathbb Q\). A negative rational number is not such a square.
Hence every post-wrap primitive part is irreducible over \(\mathbb Q\).
Multiplication by the nonzero rational content does not change the
irreducible polynomial class.

## 3. Exact pairwise resultant

Let

\[
f(X)=1+D(T-kX)^2,
\qquad
g(X)=1+E(U-\ell X)^2,
\]

with \(k\ell\ne0\), and set

\[
\Delta=T\ell-Uk.
\]

The two complex roots of \(f\) are

\[
\alpha_\pm=\frac{T}{k}\pm \frac{i}{k\sqrt D}.
\]

Since the leading coefficient of \(f\) is \(Dk^2\), the root formula for the
resultant gives

\[
\operatorname{Res}_X(f,g)
=(Dk^2)^2g(\alpha_+)g(\alpha_-).
\]

At these roots,

\[
U-\ell\alpha_\pm
=-\frac{\Delta}{k}\mp \frac{i\ell}{k\sqrt D}.
\]

The two values of \(g\) are complex conjugates. Multiplying them and then
clearing the factor \((Dk^2)^2\) gives

\[
\operatorname{Res}_X(f,g)
=
(Dk^2+DE\Delta^2-E\ell^2)^2
+4DE^2\Delta^2\ell^2.
\]

Put

\[
A=Dk^2,\qquad B=E\ell^2,\qquad C=DE\Delta^2.
\]

The elementary identity

\[
(A+C-B)^2+4BC=(A+B+C)^2-4AB
\]

now yields

\[
\boxed{
\operatorname{Res}_X(f,g)
=
[DE\Delta^2+E\ell^2+Dk^2]^2-4DEk^2\ell^2.
}
\]

When \(D=E\), direct difference-of-squares factorization gives

\[
\begin{aligned}
\operatorname{Res}_X(f,g)
&=D^2[(D\Delta^2+k^2+\ell^2)^2-4k^2\ell^2]\\
&=D^2[D\Delta^2+(k-\ell)^2]
       [D\Delta^2+(k+\ell)^2].
\end{aligned}
\]

The formula is asserted only when both displayed polynomials are quadratics.
The degree-drop case \(k=0\) or \(\ell=0\) was already separated as a
constant-square row.

## 4. Vanishing and duplicates

Continue with \(D,E>0\) and \(k\ell\ne0\). In the notation above,

\[
\operatorname{Res}(f,g)=0
\iff
A+B+C=2\sqrt{AB}.
\]

But

\[
A+B\ge2\sqrt{AB},
\qquad C\ge0.
\]

Equality is possible exactly when

\[
A=B,\qquad C=0.
\]

Since \(D,E>0\), these conditions are precisely

\[
Dk^2=E\ell^2,
\qquad
\Delta=0.
\]

They also imply equality of the polynomials. Indeed,
\(\Delta=0\) gives \(T/k=U/\ell\), while \(Dk^2=E\ell^2\) gives a common
positive number \(A\). Therefore

\[
f(X)=1+A\left(X-\frac{T}{k}\right)^2
=1+A\left(X-\frac{U}{\ell}\right)^2=g(X).
\]

The converse is immediate. Thus zero resultant, association over
\(\mathbb Q\), and literal polynomial equality are equivalent for these
rows.

If \(D\) and \(E\) are squarefree positive integers, equality
\(Dk^2=E\ell^2\) forces \(D=E\): both sides have the same squarefree kernel.
For positive \(k,\ell\), it then forces \(k=\ell\), and \(\Delta=0\) forces
\(T=U\). When the discriminants are not squarefree, the two displayed
conditions are the correct scaled-duplicate classification.

## 5. Complete generic square kernel

Let \(I_0\) be the constant-square indices. For every post-wrap polynomial,
divide by its positive content and regard its primitive irreducible part in
\(\mathbb Q[X]\). Section 4 shows that two such irreducible parts are
associates exactly when the original Pell polynomials are equal.

Unique factorization in \(\mathbb Q[X]\) now gives the complete criterion.
In a product

\[
F_c(X)=\prod_i f_i(X)^{c_i},
\qquad c_i\in\{0,1\},
\]

the valuation at the irreducible part belonging to an equality class \(C\)
is

\[
\sum_{i\in C}c_i.
\]

The product is a square in \(\mathbb Q(X)\) only if every such valuation is
even. Conversely, if all those sums are even, each post-wrap equality-class
product is an even power of one polynomial, and every index in \(I_0\)
contributes the square \(S_i^2\). Hence the product is a square. This proves

\[
c\in K_{\rm gen}
\iff
\sum_{i\in C}c_i=0\pmod2
\quad\text{for every post-wrap equality class }C.
\]

After deleting the constant rows and retaining one representative per class,
each class has one coordinate. The criterion forces every coordinate to
zero, so the cleaned generic kernel is zero.

## 6. Integral generic roots and global signs

The preceding classification gives an integral square root directly. For a
generic-kernel vector \(c\), let

\[
r_C=\sum_{i\in C}c_i,
\]

which is even, and let \(f_C\) be the common polynomial in class \(C\).
Define

\[
H_c(X)
=
\prod_{\substack{i\in I_0\\c_i=1}}S_i
\prod_C f_C(X)^{r_C/2}.
\]

Then \(H_c\in\mathbb Z[X]\) and

\[
H_c(X)^2=\prod_i f_i(X)^{c_i}.
\]

If \(i,j\) lie in one equality class, then evaluation at zero gives
\(S_i^2=f_i(0)=f_j(0)=S_j^2\). Since all \(S_i\) are positive, \(S_i=S_j\).
It follows that

\[
H_c(0)=\prod_i S_i^{c_i}.
\]

At \(X=N\), the positive integer root of the specialized product is

\[
R_c=|H_c(N)|.
\]

Because \(H_c\) is an integer polynomial,

\[
H_c(N)\equiv H_c(0)\pmod N.
\]

The absolute value can change only the global sign, so, with
\(x_i=S_i\bmod N\),

\[
R_c\equiv\pm\prod_i x_i^{c_i}\pmod N.
\]

On the unit branch, the normalized root is therefore \(+1\) or \(-1\).
There is no denominator condition: the classification itself constructed
\(H_c\) in \(\mathbb Z[X]\).

## 7. Shared specialization primes divide resultants

Now retain one representative of each post-wrap polynomial. For distinct
indices \(i,j\), the resultant is nonzero. If a rational prime \(p\) divides
both specialized values \(a_i=f_i(N)\) and \(a_j=f_j(N)\), then the reductions
of \(f_i\) and \(f_j\) modulo \(p\) have the common root \(N\bmod p\).
The Sylvester matrix is therefore singular modulo \(p\), so

\[
p\mid\operatorname{Res}_X(f_i,f_j).
\]

This implication remains valid if one polynomial loses degree or becomes
zero modulo \(p\). It is only a one-way implication: a prime divisor of the
resultant need not divide the two values at the chosen integer \(N\).

For each retained \(i\), let

\[
\mathcal R_i
=
\prod_{j\ne i}|\operatorname{Res}(f_i,f_j)|,
\quad
e_i=\lceil\log_2(a_i+1)\rceil,
\quad
g_i=\gcd(a_i,\mathcal R_i^{e_i}),
\quad
b_i=a_i/g_i.
\]

Suppose a prime \(p\) divides both \(a_i\) and some \(a_j\). Then
\(p\mid\mathcal R_i\). Also

\[
v_p(a_i)\le\log_2a_i<e_i.
\]

Therefore

\[
v_p(\mathcal R_i^{e_i})\ge e_i>v_p(a_i),
\]

and the gcd \(g_i\) contains the full \(p\)-primary part of \(a_i\). No such
prime remains in \(b_i\). Hence

\[
\boxed{\gcd(b_i,a_j)=1\quad(i\ne j).}
\]

If \(b_i\) is nonsquare, some prime has odd valuation in \(b_i\). This prime
appears in no other row. Its parity equation forces \(c_i=0\) in every
numerical square dependency.

If \(b_i\) is square, removing it does not change the rational-prime parity
column of \(a_i=b_ig_i\). Every prime in \(g_i\) divides
\(\mathcal R_i\) by construction. Thus, after private nonsquare rows are
eliminated, the complete numerical parity problem is supported on the
pairwise resultants. This proves the localization claim without asserting
that the localized kernel is zero.

An exact-square \(b_i\), including a specialization-only singleton square,
has zero parity column but can still have a supplied root that disagrees with
its positive integer root. The ordinary singleton root comparison remains a
separate public screen; the parity localization does not discard that screen.

## 8. Factor-free bit complexity

Let \(L\) be the total binary encoding length of \(N\) and all
\((D_i,S_i,T_i,k_i)\). Expanding every quadratic and evaluating it at \(N\)
uses integer arithmetic on operands of bit length polynomial in \(L\).
There are \(O(m^2)\) resultants. The closed formula uses a constant number of
additions, multiplications, and squarings for each pair, and the bit length of
each resultant is polynomial in the bit lengths of its two input rows.

The product \(\mathcal R_i\) has bit length equal to the sum of the bit
lengths of its factors, hence polynomial in \(L\). The exponent satisfies

\[
e_i=O(\log(a_i+1))=O(L).
\]

Consequently \(\mathcal R_i^{e_i}\) also has polynomial bit length. Binary
exponentiation, Euclid's algorithm, exact division, and integer square testing
all run in deterministic time polynomial in these explicit bit lengths.
No prime factorization is used.

If both the number of explicitly listed rows and their coordinate bit lengths
are quasipolynomial in \(n=\lceil\log_2(N+1)\rceil\), then their total explicit
length and every polynomial in that length are still quasipolynomial in
\(n\). The theorem makes no corresponding claim for an exponentially larger
bank given only by an implicit rule.

## 9. P68 comparison and remaining scope

P68 begins with general rational polynomials of constant term \(1\). It
computes a generic kernel and certifies its unit-denominator square roots as
global-root decoys. For the present rows, one could divide \(f_i\) by
\(S_i^2\) to force constant term \(1\), but that representation obscures the
stronger structure.

Here, direct content and irreducible-factor analysis proves that the cleaned
generic kernel itself is zero. Before cleanup, it constructs an integral
root for every generic vector, so no rational-denominator exception remains.
The pairwise resultant then localizes every prime interaction that exists
only after specialization. These are the gains specific to the Pell
polynomial family.

Nothing in the argument proves that each private residual \(b_i\) is
nonsquare. All nonsquare support of a row can, in principle, lie in its
resultant part \(g_i\). Several such columns can still close a parity relation
after specialization, and its normalized root need not be governed by the
generic-root proof. Controlling that explicit resultant-supported core is the
remaining problem.
