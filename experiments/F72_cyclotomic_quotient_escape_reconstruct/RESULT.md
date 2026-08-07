# Verdict: PASS

All claims follow for the declared operation set. The source boundary is important: a screen may evaluate a gcd such as \(\gcd(x-1,N)\), but its failed operand \(x-1\) does not become an authorized state. Quotient promotion adds precisely that missing retention operation.

## 1. The family

Put

\[
c=3s^2-1,\qquad N=c^2+c+1,
\]

and

\[
A=3s^2-3s+1,\qquad B=3s^2+3s+1.
\]

Then

\[
N=9s^4-3s^2+1
\]

and

\[
AB=(3s^2+1-3s)(3s^2+1+3s)
=(3s^2+1)^2-9s^2
=9s^4-3s^2+1=N.
\]

If a positive integer divides both \(A\) and \(B\), it divides
\(B-A=6s\). But \(A\equiv B\equiv1\pmod s\), both are odd, and both
are \(1\pmod3\). Thus no prime divisor of \(6s\) can divide either one,
and

\[
\gcd(A,B)=1.
\]

Because \(s\) is even, \(A\) and \(B\) are odd. For \(s\ge2\),
\(A\ge7\) and \(B\ge19\), so they are proper nontrivial factors of
\(N=AB\). Finally, \(c\equiv-1\pmod3\), and hence

\[
N=c^2+c+1\equiv1\pmod3.
\]

Therefore \(3\nmid N\).

## 2. Endpoint subgroup and direct signs

The identity

\[
c^3=1+(c-1)N
\]

gives \(c^3\equiv1\pmod {p^a}\) for every \(p^a\Vert N\). Also
\(\gcd(c,N)=1\), since \(N\equiv1\pmod c\). The order of \(c\) modulo
\(p^a\) therefore divides three. It cannot be one: indeed,

\[
N=(c+2)(c-1)+3,
\]

so a common prime divisor of \(c-1\) and \(N\) would be \(3\), while
\(3\nmid N\). Thus the order is exactly three at every prime-power
component, and also modulo \(N\). Consequently

\[
\langle c\rangle=\{1,c,c^2\}\pmod N.
\]

There is no proper direct-sign gcd on this subgroup. The required gcds are

\[
\begin{array}{c|cc}
x&\gcd(x-1,N)&\gcd(x+1,N)\\ \hline
1&N&1\\
c&1&1\\
c^2&1&1.
\end{array}
\]

Here \(N\) is odd,
\(\gcd(c-1,N)=\gcd(c-1,3)=1\),
\(N-c(c+1)=1\),
\(c^2-1=(c-1)(c+1)\), and
\(c^2+1=N-c\). Thus each output is either \(1\) or \(N\), never a
proper factor.

## 3. Closure of the endpoint-only source

Every authorized raw occurrence is a power \(c^k\). Products and powers
preserve this form, and canonical reduction depends only on \(k\bmod3\).
The canonical inverse is the unique member \(c^r\), with
\(r\in\{0,1,2\}\), for which \(k+r\equiv0\pmod3\). Appending that inverse
therefore gives the raw relation value

\[
c^{k+r}=c^{3t}.
\]

Products and powers of such relations have the same form. Integer gcd
refinement of powers of \(c\) only returns powers of \(c\), and exact
perfect-power extraction only lowers their exponents. Since \(c\) itself is
not a perfect power, the terminal gcd-free basis is the single, possibly
composite block \(c\).

The other declared screens do not split \(N\). An inverse pair has residues
either \((1,1)\) or \((c,c^2)\), up to order. In the first case its
difference is \(0\pmod N\), so the difference gcd is the trivial value
\(N\), while its discriminant is \(4\), a unit modulo the odd number \(N\).
In the second case

\[
c-c^2=c(1-c)
\]

is a unit modulo \(N\), and

\[
(c-c^2)^2+4\equiv(c+c^2)^2\equiv1\pmod N.
\]

Thus the inverse-pair difference and discriminant screens also return no
proper factor.

For completeness, consider every rational-square combination available to
the decoder, including ratios of products of relation values. It has the
form \(c^{3T}\) for some \(T\in\mathbb Z\). Write
\(c=\prod p^{e_p}\). Since \(c\) is not a perfect power,
\(\gcd_p e_p=1\), so at least one \(e_p\) is odd. If \(c^{3T}\) is a
rational square, all exponents \(3Te_p\) are even; hence \(T\) is even. Its
positive rational square root is then

\[
c^{3T/2}\equiv1\pmod N.
\]

Its sign gcds are again only \(N\) and \(1\). This proves the trap even
after arbitrary occurrence amplification and the complete rational-square
decoder.

The public coefficient

\[
q_0=\frac{c^3-1}{N}=c-1
\]

is not a retained endpoint state. The retained multiplicative basis contains
only powers of \(c\), and \(1<c-1<c\). None of the declared retention
operations extracts a relation quotient or retains a failed screen operand.
Thus making \(q_0\) a state is a genuine promotion, although its value is
public in the displayed relation.

## 4. Quotient promotion and the square

Promote

\[
g=c-1.
\]

Since \(c+1=3s^2\),

\[
w=\frac{c^2-1}{3}
=\frac{(c-1)(c+1)}3
=s^2g.
\]

This integer satisfies \(0<w<N\). Moreover,

\[
gw=s^2(c-1)^2.
\]

Writing \(x=s^2\), the two sides of

\[
gw=1+(s^2-1)N
\]

both equal \(9x^3-12x^2+4x\). Hence \(gw\equiv1\pmod N\), and the range
condition proves that \(w\) is the canonical inverse of \(g\).

Set

\[
R=s(c-1).
\]

Then

\[
gw=R^2=1+(s^2-1)N.
\]

Direct expansion gives

\[
R-1=(s-1)(3s^2+3s+1)=(s-1)B
\]

and

\[
R+1=(s+1)(3s^2-3s+1)=(s+1)A.
\]

Also

\[
A=3s(s-1)+1,\qquad B=3s(s+1)+1.
\]

Using \(N=AB\) and \(\gcd(A,B)=1\), these identities imply

\[
\gcd(R-1,N)
=B\,\gcd(s-1,A)=B
\]

and

\[
\gcd(R+1,N)
=A\,\gcd(s+1,B)=A.
\]

The exact-square relation therefore factors \(N\).

## 5. All earlier promoted-state screens fail

Assume that no prime at most \(13\) divides \(N\). Since
\(c=g+1\),

\[
N=g^2+3g+3=(g-1)(g+4)+7.
\]

Thus \(\gcd(g-1,N)\mid7\), and the hypothesis makes this gcd one. Also
\(g+1=c\) is a unit modulo \(N\), so

\[
\gcd(g\pm1,N)=1.
\]

Because \(gw\equiv1\pmod N\), multiplication by the unit \(g\) gives

\[
g(w-1)\equiv1-g,\qquad g(w+1)\equiv1+g\pmod N.
\]

Therefore

\[
\gcd(w\pm1,N)=1.
\]

For \(d=g-w\),

\[
gd=g^2-gw\equiv g^2-1=(g-1)(g+1)\pmod N.
\]

The right-hand side is a unit, so \(d\) is a unit and
\(\gcd(d,N)=1\).

Finally,

\[
d^2+4=(g-w)^2+4\equiv(g+w)^2\pmod N
\]

and, exactly,

\[
g+w=g(s^2+1).
\]

If \(m\mid s^2+1\) and \(m\mid N\), then \(s^2\equiv-1\pmod m\) and
\(s^4\equiv1\pmod m\). Since \(N=9s^4-3s^2+1\), this gives

\[
0\equiv N\equiv9+3+1=13\pmod m.
\]

Hence

\[
\gcd(s^2+1,N)\mid13.
\]

The hypothesis makes this gcd one. Since \(g\) is a unit, \(g+w\) is a
unit, and therefore

\[
\gcd(d^2+4,N)=1.
\]

Thus all stated direct-sign, inverse-difference, and discriminant screens
fail. The next declared screen recognizes \(gw=R^2\), and its root-sign gcds
return the proper factors \(B\) and \(A\). It is the first successful screen
in the declared sequence.

## 6. Infinite robust subfamilies

First, a suitable prime \(\ell\) exists for every \(H\ge13\). One elementary
construction is to put \(X=M_H\) and choose any prime divisor \(\ell\) of

\[
\Phi_{12}(X)=X^4-X^2+1>1.
\]

No prime at most \(H\) divides this value, because every such prime divides
\(X\) and the displayed value is then \(1\) modulo that prime. Hence
\(\ell>H\). Also

\[
(X^2+1)\Phi_{12}(X)=X^6+1,
\]

so \(X^6\equiv-1\pmod\ell\) and \(X^{12}\equiv1\pmod\ell\). The order of
\(X\) modulo \(\ell\) is either \(4\) or \(12\). Order \(4\) would give
\(X^2\equiv-1\), whence
\(\Phi_{12}(X)\equiv3\pmod\ell\), forcing \(\ell=3\), impossible. The
order is therefore \(12\), so \(12\mid\ell-1\). Thus

\[
\ell>H,\qquad \ell\equiv1\pmod {12}.
\]

For every prime \(\ell\equiv1\pmod {12}\), quadratic reciprocity gives
\((3/\ell)=1\). Hence there is a nonzero residue \(r\pmod\ell\) with
\(3r^2-1\equiv0\pmod\ell\). Its \(\ell\) lifts modulo \(\ell^2\) are
\(r+k\ell\). If \(3r^2-1=\ell u\), then

\[
3(r+k\ell)^2-1\equiv\ell(u+6rk)\pmod {\ell^2}.
\]

Because \(6r\not\equiv0\pmod\ell\), exactly one value of \(k\pmod\ell\)
is a root modulo \(\ell^2\). Choose any other lift and call it \(a\). Then

\[
3a^2-1\equiv0\pmod\ell,
\qquad
3a^2-1\not\equiv0\pmod {\ell^2}.
\]

Since \(\gcd(M_H,\ell^2)=1\), CRT gives one residue class modulo
\(M_H\ell^2\) satisfying

\[
s\equiv0\pmod {M_H},\qquad s\equiv a\pmod {\ell^2}.
\]

It contains infinitely many positive integers. Each is even because
\(2\mid M_H\). It is nonzero, so it is at least two.

For every prime \(p\le H\), the first congruence gives

\[
c\equiv-1\pmod p,
\qquad
A\equiv B\equiv1\pmod p.
\]

Thus every prime factor of \(c,A,B\), and of \(N=AB\), exceeds \(H\).
The second congruence gives

\[
c=3s^2-1\equiv3a^2-1\pmod {\ell^2},
\]

so \(v_\ell(c)=1\). A perfect power has every prime valuation divisible by
an exponent greater than one. Hence \(c\) is not a perfect power.

Trial division through \(H\) therefore refines neither the endpoint block
nor \(N\), and perfect-power preprocessing does not refine \(c\). The
endpoint closure proof in Section 3 still applies. The quotient-promotion
identities in Sections 4 and 5 apply to every one of these even values of
\(s\), so promotion still returns \(A\) and \(B\). Since the CRT progression
is unbounded and \(N=9s^4-3s^2+1\) is strictly increasing for positive
\(s\), it gives infinitely many distinct inputs.

## 7. Classification and scope

This proves the stated narrow operation-set separation. Multiplicative
endpoint feedback can remain trapped both at the complete order-three
subgroup level and under the complete rational-square decoder. Retaining the
public relation quotient \(q_0=c-1\) as a new state creates the exact square
\(gw=R^2\), whose two sign gcds factor \(N\), on an infinite robust
subfamily.

The quotient is public in the original relation. The family is deliberately
manufactured by explicit congruence conditions and is recognizable. Nothing
here proves a general quotient bias, an all-input sampler, an
inverse-polynomial success law, publication-level novelty, or an unrestricted
factoring algorithm.
