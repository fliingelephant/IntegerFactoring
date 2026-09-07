# Independent reconstruction: orbit precision

## Result

The value-precision claim and the stated floor corollary both follow from the given assumptions. No proof gap was found.

Put

\[
q=2^{p-2}.
\]

Since \(p\geq 3\), \(q\) is even, and the requested modulus is

\[
2^p=4q.
\]

## The orbit structure

Every odd residue is a unit modulo \(M\). Thus \(w^{-1}\) exists for every \(w\in U\), and an arbitrary odd integer \(\epsilon\), including a negative one, defines a unit modulo \(M\). Hence \(i\) maps \(U\) to itself.

As maps on canonical representatives,

\[
s^2=i^2=1,\qquad i\circ s=s\circ i.
\]

Indeed,

\[
i(i(w))\equiv \epsilon(\epsilon w^{-1})^{-1}\equiv w\pmod M
\]

and

\[
i(s(w))\equiv \epsilon(-w)^{-1}\equiv-\epsilon w^{-1}\equiv s(i(w))\pmod M.
\]

Canonical representatives make these congruences equalities of maps on \(U\). Also, \(s\) has no fixed point in \(U\): a fixed point would be \(w=M/2\), which is even. Therefore, the commuting involutions \(s\) and \(i\) split \(U\) into exactly the following orbit types:

1. An inversion-fixed pair \(\{u,s(u)\}\), where \(i(u)=u\). Equivalently, \(u^2\equiv\epsilon\pmod M\).
2. A sign-inversion pair \(\{u,s(u)\}\), where \(i(u)=s(u)\). Equivalently, \(u^2\equiv-\epsilon\pmod M\).
3. A four-point orbit \(\{u,s(u),v,s(v)\}\), where \(v=i(u)\) is distinct from both \(u\) and \(s(u)\).

The first two cases include all exceptional roots of \(\epsilon\) and \(-\epsilon\). They cannot occur simultaneously at one point because \(s\) has no fixed point.

## Contribution of one orbit

For an antisymmetric integer-valued function \(x\), let

\[
Q_O(x)=\sum_{w\in O}\bigl(x(w)x(i(w))-x(w)^2\bigr)
\]

be the contribution of an orbit \(O\) to \(Q_\epsilon(x)\).

On an inversion-fixed pair, write \(x(u)=a\), so \(x(s(u))=-a\). The map \(i\) fixes both points. Consequently,

\[
Q_O(x)=0.
\]

On a sign-inversion pair, \(i\) swaps the two points. Thus

\[
Q_O(x)=-4a^2.
\]

On a four-point orbit, put \(x(u)=a\) and \(x(v)=b\). Antisymmetry gives values \(-a\) and \(-b\) at the other two points, while \(i\) swaps \(u,v\) and swaps \(s(u),s(v)\). Hence

\[
Q_O(x)=4ab-2a^2-2b^2=-2(a-b)^2.
\]

## Precision on every orbit

Assume that \(r\) and \(g\) satisfy the hypotheses. Consider the same orbit for both functions.

For an inversion-fixed pair, both orbit contributions are zero.

For a sign-inversion pair, write \(r(u)=\alpha\) and \(g(u)=a\). The congruence hypothesis gives an integer \(m\) with \(\alpha-a=qm\). Therefore

\[
Q_O(r)-Q_O(g)
=-4(\alpha^2-a^2)
=-4qm(\alpha+a),
\]

which is divisible by \(4q\).

For a four-point orbit, write

\[
r(u)=\alpha,\quad r(v)=\beta,\quad
g(u)=a,\quad g(v)=b,
\]

and set \(d=\alpha-\beta\), \(e=a-b\). Pointwise congruence gives \(d-e=qm\) for some integer \(m\). Since \(q\) is even, \(d\) and \(e\) have the same parity. Thus \(d+e=2n\) for some integer \(n\). It follows that

\[
Q_O(r)-Q_O(g)
=-2(d^2-e^2)
=-2(qm)(2n)
=-4qmn.
\]

This is also divisible by \(4q\). Summing the orbit contributions gives

\[
Q_\epsilon(r)\equiv Q_\epsilon(g)\pmod{4q},
\]

or, since \(4q=2^p\),

\[
Q_\epsilon(r)\equiv Q_\epsilon(g)\pmod{2^p}.
\]

This argument includes \(p=3\): then \(q=2\), and the parity step still supplies the additional factor of \(2\).

All quotients introduced above are integers. The quotient by \(q\) comes directly from the pointwise congruence, and the quotient by \(2\) comes from the established parity. No division in the residue ring is used except inversion of the odd unit \(w\).

## Floor corollary

Let \(A\) be canonical and odd, with \(0<A<M\), and put

\[
f(w)=\left\lfloor\frac{Aw}{M}\right\rfloor,
\qquad h=\frac{A-1}{2},
\qquad r(w)=f(w)-h.
\]

The integer \(h\) is well-defined because \(A\) is odd. For every \(w\in U\), the product \(Aw\) is odd and therefore is not divisible by the even integer \(M\). Thus \(Aw/M\) is not an integer. Using \(\lfloor-x\rfloor=-\lfloor x\rfloor-1\) for nonintegral \(x\), one obtains

\[
\begin{aligned}
f(s(w))
&=\left\lfloor\frac{A(M-w)}M\right\rfloor\\
&=A-1-\left\lfloor\frac{Aw}M\right\rfloor
=A-1-f(w).
\end{aligned}
\]

Since \(A-1=2h\), this gives

\[
r(s(w))=-r(w).
\]

The map \(s\) pairs the odd elements below \(M/2\) with those above \(M/2\); there is no odd element at \(M/2\). On the lower half, the canonical residue defining \(g\) is an integer in \(\{0,\ldots,q-1\}\) and is congruent to \(r(w)\) modulo \(q\). The antisymmetric extension is unambiguous. If \(w=s(v)\) is in the upper half, then

\[
g(w)=-g(v)\equiv-r(v)=r(w)\pmod q.
\]

Thus \(r\) and \(g\) satisfy all hypotheses of the value-precision claim.

It remains to relate \(r\) to \(f\). For any integer-valued function \(x\) on \(U\) and any integer constant \(c\), the fact that \(i\) is a permutation gives

\[
H_\epsilon(x+c)
=H_\epsilon(x)+2c\sum_{w\in U}x(w)+|U|c^2,
\]

while

\[
U2(x+c)
=U2(x)+2c\sum_{w\in U}x(w)+|U|c^2.
\]

Hence \(Q_\epsilon(x+c)=Q_\epsilon(x)\) exactly. Since \(f=r+h\),

\[
Q_\epsilon(f)=Q_\epsilon(r)\equiv Q_\epsilon(g)\pmod{2^p}.
\]

Expanding \(Q_\epsilon\) and rearranging proves

\[
H_\epsilon(f)
\equiv U2(f)+H_\epsilon(g)-U2(g)
\pmod{2^p}.
\]

When \(p=3\), one has \(q=2\). The lower-half canonical residues are \(0\) and \(1\), and their antisymmetric upper-half values are \(0\) and \(-1\). Therefore \(g(U)\subseteq\{-1,0,1\}\).

## Gap and scope report

No gap was found. The proof uses only elementary integer and modular arithmetic under the stated guards. It proves value-alphabet compression at the same graph modulus, summand count, and output precision. It does not evaluate \(H_\epsilon(g)\), assert a binary-overlap evaluator, reduce a runtime, or imply a factoring theorem.
