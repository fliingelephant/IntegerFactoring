# Proof of the F201 candidate

## 1. The balanced interval and the correct parent cell

Because \(p<q\),

\[
p^2<N<q^2.
\]

Thus

\[
p\leq B<q.
\tag{1}
\]

Also \(q<2p\) and \(B<q\) imply \(B\leq2p-2\), since all quantities are
integers.  Hence

\[
\lceil B/2\rceil\leq p-1,
\tag{2}
\]

so \(p\in I_B\).  Equations (1)--(2) also give \(q>B\) and \(2p>B\).
Every positive multiple of either hidden prime in \(I_B\) is therefore
equal to \(p\).  This proves the uniqueness assertion.

For \(m=2^t\) with \(t\geq1\), inversion permutes the odd residue classes
modulo \(m\) and modulo \(2m\).  The two lifts of a known odd reciprocal
class modulo \(m\) therefore correspond, after inversion, to the two lifts
of \(a\) modulo \(2m\).  If any consecutive parent AP is listed as

\[
x_j=c+mj,
\]

these two child classes are exactly the even and odd values of \(j\).

## 2. Endpoint cleanup and the sibling products

If \(L=2s+1\), parity splitting leaves \(x_{2s}\) as the sole unpaired
term.  It belongs to \(I_B\), so the uniqueness proved above gives

\[
\gcd(N,x_{2s})=
\begin{cases}
p,&x_{2s}=p,\\
1,&x_{2s}\neq p.
\end{cases}
\tag{3}
\]

The first case factors \(N\).  In the second case, removal of \(x_{2s}\)
does not remove \(p\).  If \(L=1\), the assumption \(p\in S\) forces
the first case of (3), so every unresolved case has \(s\geq1\).

After cleanup, or immediately when \(L=2s\), define

\[
e_i=x_{2i}=c+2mi,
\qquad
o_i=x_{2i+1}=e_i+m.
\tag{4}
\]

The ordering of the parent cell gives

\[
\lceil B/2\rceil<e_i<o_i\leq B,
\qquad
e_i<o_i<e_{i+1}\quad(i<s-1).
\tag{5}
\]

The correct parent contains \(p\), and endpoint cleanup did not remove it.
Exactly one list in (4) therefore contains \(p\).  No listed integer is
divisible by \(q\), and no listed integer other than \(p\) is divisible by
\(p\).  Primality now gives

\[
\{\gcd(E,N),\gcd(O,N)\}=\{1,p\}.
\tag{6}
\]

## 3. Interlacing fixes the Euclidean quotient

Termwise comparison in (5) gives \(O>E\).  For \(s\geq2\), the strict
interlacing also gives

\[
\prod_{i=0}^{s-2}o_i
<\prod_{i=1}^{s-1}e_i.
\tag{7}
\]

Cancelling positive factors yields

\[
\frac OE
=\frac{o_{s-1}}{e_0}
 \frac{\prod_{i=0}^{s-2}o_i}
      {\prod_{i=1}^{s-1}e_i}
<\frac{o_{s-1}}{e_0}
<\frac{B}{B/2}=2.
\tag{8}
\]

For \(s=1\), the same last inequality follows directly from
\(O/E=o_0/e_0\).  Hence the Euclidean quotient of \(O\) by \(E\) is one,
and

\[
D=O-E,
\qquad 0<D<E.
\tag{9}
\]

If \(p\mid E\), equation (6) gives \(p\nmid O\), so

\[
D\equiv O\not\equiv0\pmod p.
\]

If \(p\mid O\), then similarly

\[
D\equiv-E\not\equiv0\pmod p.
\]

Thus \(p\nmid D\) in either orientation.  Nothing in this calculation
controls \(D\bmod q\), so \(q\mid D\) remains possible.  Since \(E<O\),
division in the reverse direction has quotient zero and remainder \(E\).

Finally, the Pochhammer identities follow by extracting \(2m\) from each
factor in (4).  Applying \((z)_s=\Gamma(z+s)/\Gamma(z)\) gives the displayed
gamma ratio.  These identities describe exactly the same rational number
\(O/E\), so they do not alter (8)--(9).

## 4. Explicit size of the remainder

Use \(o_i=e_i+m\) and expand:

\[
D=\prod_{i=0}^{s-1}(e_i+m)-\prod_{i=0}^{s-1}e_i.
\tag{10}
\]

Every surviving term after cancellation is positive.  The term obtained by
choosing \(m\) from the zeroth factor and \(e_i\) from every other factor
is

\[
m\prod_{i=1}^{s-1}e_i.
\]

Using \(e_i>B/2\) proves

\[
D\geq m\prod_{i=1}^{s-1}e_i
\geq m(B/2)^{s-1}.
\tag{11}
\]

The last inequality is strict for \(s\geq2\); when \(s=1\), both products
are empty and equality holds.

Taking logarithms, and using
\(\operatorname{bitlen}(D)=\lfloor\log_2D\rfloor+1>\log_2D\), gives the
claimed bit-length lower bound.

The interval \(I_B\) contains exactly \(\lfloor B/2\rfloor\) consecutive
integers.  The count of any fixed residue class modulo \(m\) in such an
interval differs from \(\lfloor B/2\rfloor/m\) by less than one.  Therefore

\[
L=\frac{\lfloor B/2\rfloor}{m}+O(1),
\qquad
s=\left\lfloor\frac L2\right\rfloor
=\frac{B}{4m}+O(1).
\tag{12}
\]

This estimate also persists down the declared cleanup chain.  If a parent
has \(L=\lfloor B/2\rfloor/m+O(1)\) terms, endpoint cleanup and parity
selection leave \(\lfloor L/2\rfloor\) terms at step \(2m\), which is
\(\lfloor B/2\rfloor/(2m)+O(1)\).  Induction keeps the error bounded.

At the stated P175 precision,

\[
m=2^t=\Theta\!\left(N^{1/4}2^{-L_0(n)}\right),
\qquad B=\Theta(N^{1/2}).
\tag{13}
\]

Substitution into (12) gives

\[
s=\Theta\!\left(N^{1/4}2^{L_0(n)}\right).
\tag{14}
\]

Because \(L_0(n)=o(n)\) for a fixed polylogarithm and
\(\log_2N=\Theta(n)\), equation (14) is \(2^{\Theta(n)}\).  Equation (11)
then gives \(\operatorname{bitlen}(D)=2^{\Theta(n)}\): the lower bound is
\(2^{\Theta(n)}\), while the elementary upper bound
\(D<O\leq B^s\) has the same exponential class.  This proves only the cost
of writing the exact ordinary integer.  The reverse remainder is not a
small input either: directly,

\[
E>(B/2)^s,
\]

so \(\operatorname{bitlen}(E)=2^{\Theta(n)}\) at the same schedule.

## 5. Linear axes

Reduce

\[
F_{\alpha,\beta}=\alpha E+\beta O
\tag{15}
\]

modulo \(p\).  On the axis \(E=0\), equation (6) says \(O\neq0\), and
(15) becomes \(F=\beta O\).  Hence \(F=0\) if and only if \(\beta=0\)
in \(\mathbb F_p\).  On the axis \(O=0\), the same argument gives
\(F=0\) if and only if \(\alpha=0\) in \(\mathbb F_p\).

If both coefficients are units modulo \(N\), neither is zero modulo \(p\),
so (15) loses \(p\)-support in either orientation.  Conversely, vanishing
on both possible axes requires \(p\mid\alpha\) and \(p\mid\beta\).
Screening either public coefficient by a gcd with \(N\) either finds a
proper factor or shows it is a unit or a multiple of \(N\).  Multiples of
\(N\) contribute zero terms modulo \(N\), and two such coefficients make
the whole form trivially zero.  Reduction modulo \(q\) was not constrained,
so accidental \(q\)-support is again possible.

## 6. Scope of the conclusion

The proof never creates a recursive child whose input has fewer bits.  It
shows instead that the first proposed auxiliary \(D\) has lost the known
factor \(p\), and that writing \(D\) is already exponentially expensive at
the current node.  This is independent of recursion depth.

If some other QP computation selects the correct child, only \(O(n)\)
successive lifts are needed.  A unique recursive chain may lose one bit at
each stage and remain QP.  No fixed-ratio contraction is assumed or needed.
The argument does not constrain implicit product evaluation, adaptive
nonlinear statistics, exact nonlocal carries or floors, or a different
one-child integer auxiliary.
