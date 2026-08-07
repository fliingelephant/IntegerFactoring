# PASS

The SHA-256 of `STATEMENT.md` is

```text
331d9571034b8894d92ca9e1cb5834e65243dc7b8ca2ffefc3e75cfc681ed3e4
```

It matches the required digest. I used only the statement. The verification
below is an independent reconstruction.

## 1. CRT state

The congruence defining \(\rho_g\) has one residue class modulo \(g\), since
\(N\) is a unit modulo \(g\). That class is not zero because the right-hand
side is \(-1\), and \(g>1\). Hence its least positive representative satisfies

\[
1\leq \rho_g\leq g-1.
\]

The definition gives

\[
g w_g=1+N\rho_g.
\]

Thus \(w_g\) is a positive integer and \(gw_g\equiv1\pmod N\). Moreover,

\[
w_g\leq\frac{1+N(g-1)}g
=N-\frac{N-1}{g}<N.
\]

Therefore \(1\leq w_g<N\), so \(w_g\) is the canonical inverse of \(g\)
modulo \(N\). Also

\[
\rho_g=\frac{gw_g-1}{N}
\]

is the corresponding canonical inverse quotient.

If \(g\mid1+KN\), then \(KN\equiv-1\pmod g\). Thus \(K\) and \(\rho_g\)
are in the same residue class modulo \(g\). This class is nonzero. Hence
\(\rho_g\) is exactly `K mod g` represented in \(\{1,\ldots,g-1\}\).

For a legal extension \(b\), let

\[
r=\rho_g+gt.
\]

Modulo \(g\), \(r\equiv\rho_g\). Modulo \(b\), the definition of \(t\)
gives

\[
r\equiv \rho_g+g(\rho_b-\rho_g)g^{-1}
\equiv\rho_b\pmod b.
\]

Consequently \(Nr\equiv-1\) modulo both \(g\) and \(b\). Since
\(\gcd(g,b)=1\), it holds modulo \(gb\). Also

\[
1\leq r\leq(g-1)+g(b-1)=gb-1.
\]

It follows that

\[
\rho_{gb}=\rho_g+gt.
\]

Substitution gives

\[
w_{gb}
=\frac{1+N(\rho_g+gt)}{gb}
=\frac{w_g+Nt}{b}.
\]

Both \(w_{gb}\) and \([w_gw_b]_N\) are in \(\{1,\ldots,N-1\}\), and both
are inverses of \(gb\) modulo \(N\). Uniqueness of the canonical inverse
therefore gives

\[
w_{gb}=[w_gw_b]_N.
\]

Here and below, an extension is understood to be in the domain of the stated
CRT state. In particular, \(b>1\); if the retained state is required to be
less than \(N\), legality also includes \(gb<N\). The algebra above needs
only \(b>1\) and \(\gcd(b,gN)=1\).

The condition \(\gcd(b,g)=1\) rejects an identical block already occurring
as a factor of \(g\). It also rejects a macroblock that shares any existing
nontrivial integer block factor with \(g\). This is only an arithmetic
non-overlap check. The pair \((\rho_g,w_g)\), and the update itself, do not
record source occurrences, capacities, or a derivation of the retained
product. Provenance must be maintained separately.

Multiplication by \(g\) preserves a gcd with \(N\), because \(g\) is a unit
modulo \(N\). Also \(gw_g=1+N\rho_g\). Hence

\[
\begin{aligned}
\gcd(g-w_g,N)
&=\gcd(g(g-w_g),N)\\
&=\gcd(g^2-gw_g,N)\\
&=\gcd(g^2-1,N).
\end{aligned}
\]

The last gcd combines the two local possibilities \(g\equiv1\) and
\(g\equiv-1\). Neither sign screen can replace the other for a root that
exists only on a proper CRT component. For example, at \(N=55\), \(g=6\)
has \(\gcd(g-1,N)=5\) but \(\gcd(g+1,N)=1\), while \(g=4\) has
\(\gcd(g+1,N)=5\) but \(\gcd(g-1,N)=1\). In both cases
\(g^2\equiv1\pmod5\), but not modulo all of \(55\). Thus both signs must
remain available. If \(g^2\equiv1\pmod N\) globally, then
\(\gcd(g-w_g,N)=N\); the two sign gcds are also what separate the CRT signs
of a nontrivial global square root.

## 2. The scalar orders reverse

All listed prefixes are units modulo \(55\). The extensions by \(3\) obey

\[
\gcd(3,8\cdot55)=\gcd(3,7\cdot55)=1,
\quad 24,21<55,
\]

and the extensions by \(2\) obey

\[
\gcd(2,g\cdot55)=1
\quad(g=13,23,7,17),
\quad 26,46,14,34<55.
\]

Thus every tabulated common extension is legal and coprime.

For the canonical-inverse table, direct quotient identities give

\[
\begin{array}{c|cc|cc}
g&\rho_g&w_g&\rho_{3g}&w_{3g}\\ \hline
8&1&7&17&39\\
7&1&8&8&21
\end{array}
\]

because

\[
1+55=8\cdot7=7\cdot8,
\quad
1+55\cdot17=24\cdot39,
\quad
1+55\cdot8=21\cdot21.
\]

Thus the order \(7<8\) of the prefix inverses becomes \(39>21\) after the
same extension.

For the quotient table,

\[
\begin{array}{c|cc|cc}
g&\rho_g&w_g&\rho_{2g}&w_{2g}\\ \hline
13&4&17&17&36\\
23&5&12&5&6
\end{array}
\]

because

\[
1+55\cdot4=13\cdot17,
\quad
1+55\cdot17=26\cdot36,
\]

and

\[
1+55\cdot5=23\cdot12=46\cdot6.
\]

Thus \(4<5\) becomes \(17>5\).

For inverse distance, \(w_7=8\) and \(w_{17}=13\). Also

\[
14\cdot4=1+55,
\qquad
34\cdot34=1+21\cdot55.
\]

Therefore

\[
\begin{array}{c|cc|c}
g&w_g&|g-w_g|&|2g-w_{2g}|\\ \hline
7&8&1&10\\
17&13&4&0
\end{array}
\]

and \(1<4\) becomes \(10>0\).

For refinement gain,

\[
13\cdot17=1+4\cdot55,
\qquad
39\cdot24=1+17\cdot55.
\]

Hence \(17\) and \(24\) are the asserted inverses, and

\[
\gcd(17,28)=1,
\qquad
\gcd(24,28)=4.
\]

The extension \(13\mapsto39=3\cdot13\) is legal because
\(\gcd(3,13\cdot55)=1\) and \(39<55\).

Similarly,

\[
17\cdot13=1+4\cdot55,
\qquad
51\cdot41=2091=1+38\cdot55,
\]

so

\[
\gcd(13,26)=13,
\qquad
\gcd(41,26)=1.
\]

The extension \(17\mapsto51=3\cdot17\) is legal because
\(\gcd(3,17\cdot55)=1\) and \(51<55\). Thus the displayed refinement gcd
can increase under one legal extension and decrease under another.

These are order reversals for the current values of four named scalar
scores. They disprove extension-monotone dominance for those scalars only.
They give no lower bound on every polynomial-width beam, no Pareto-frontier
size bound, and no failed execution of a factorer that applies mandatory
screens before extension.

## 3. Canonical-residue closure

Every \(q_j\) is in the subgroup \(H\). A subgroup is closed under products
and inverses. Therefore an integer exponent, including a negative exponent,
keeps \(q_j^{e_j}\) in \(H\), and

\[
c=\left[\prod_jq_j^{e_j}\right]_N\in H.
\]

Since \(c\in H\), its inverse also lies in \(H\), so \(w=[c^{-1}]_N\in H\).
The equality \(cw=1+kN\) is the integer form of \(cw\equiv1\pmod N\).
Thus this operation creates no residue class outside \(H\).

It can still change the source grammar. If the raw positive product is at
least \(N\), the retained-product rule cannot retain that raw integer as a
state below \(N\), while canonical reduction supplies its representative.
A negative exponent uses a modular inverse rather than a positive source
occurrence. An exponent beyond an occurrence capacity also has no permitted
retained-product provenance. These statements concern how an integer
representative is sourced, not whether its residue belongs to \(H\).

Gcd-free refinement is integer-divisor refinement, and a subgroup need not
be closed under taking integer divisors of its canonical representatives.
For a concrete example, take \(N=13\) and

\[
H=\langle4\rangle=\{1,3,4,9,10,12\}.
\]

Here \(c=4^5\bmod13=10\), and its canonical inverse is \(w=4\), since
\(10\cdot4=1+3\cdot13\). Refining the integers \(10\) and \(4\) at their
gcd \(2\) exposes the coprime blocks \(2\) and \(5\):

\[
4=2^2,
\qquad
10=2\cdot5.
\]

Neither \(2\) nor \(5\) belongs to \(H\), although the represented products
\(4\) and \(10\) do. This proves the claimed possibility without claiming
that every refinement leaves \(H\).

Let \(\lambda=\lceil\log_2N\rceil\). For one explicitly represented vector,
binary modular exponentiation uses \(O(\log|e_j|)\) modular multiplications
per nonzero coordinate. Negative coordinates first use the extended Euclidean
algorithm to obtain a modular inverse. Modular multiplication, inversion,
canonical reduction, gcd, and exact division all have bit cost polynomial in
their operand lengths. Hence one vector has bit cost polynomial in
\(\lambda\), the number of stated coordinates, and the binary lengths of its
exponents. It is not necessary to construct an oversized raw product.

Suppose there are polynomially many generators and an exponent menu of
polynomial cardinality whose entries have polynomial bit length. For fixed
support size \(s=O(1)\), there are at most

\[
\binom ms |E|^s=O(m^s|E|^s)
\]

support-and-exponent choices. Thus exhaustive fixed-support evaluation and
polynomially many gcd refinements have polynomial bit cost. For a
predetermined support, the smaller bound is \(|E|^s\).

If support is dense and can grow with \(m\), the number of vectors is of
order \((|E|+1)^m\), so exhaustive enumeration is generally exponential.
Random or capped enumeration checks only a subset. Subgroup closure and the
existence of one separator give no lower bound on the separator density under
that sampling law. An inverse-polynomial hit probability therefore needs a
separate success theorem.

## 4. Exact witness at \(N=4033\)

First,

\[
37\cdot109=4033.
\]

Both \(2\) and \(5\) are units modulo \(4033\), so \(H_1=\langle2,5\rangle\)
is well-defined. The first raw word satisfies

\[
2^{13}=8192,
\qquad
5\cdot2^{13}=40960=10\cdot4033+630.
\]

Its canonical representative is therefore \(630\). Also

\[
630\cdot3220=2{,}028{,}600=1+503\cdot4033.
\]

Since \(1\leq3220<4033\), this proves that \(3220\) is the canonical inverse
of \(630\). The two gcds are exact because

\[
630-1=629=17\cdot37,
\qquad
630-3220=-2590=-70\cdot37,
\]

while \(4033=109\cdot37\), with
\(\gcd(17,109)=\gcd(70,109)=1\). Hence

\[
\gcd(630-1,4033)=\gcd(630-3220,4033)=37.
\]

The raw integer \(40960\) is larger than \(N\), but canonical reduction
produces the legal unit \(630<N\), and its screens expose the proper factor
\(37\).

Next,

\[
2^{11}=2048<4033<4096=2^{12},
\]

so \(n=\lceil\log_2N\rceil=12\). The exponents \(2\) and \(8\) both belong
to \(\{1,\ldots,12\}\). Their support-two word gives

\[
5^2 2^8=25\cdot256=6400=4033+2367.
\]

Further,

\[
2367\cdot443=1{,}048{,}581=1+260\cdot4033.
\]

Thus \(443\) is the canonical inverse of \(2367\). Finally,

\[
2367+1=2368=64\cdot37,
\qquad
2367-443=1924=52\cdot37.
\]

Since \(\gcd(64,109)=\gcd(52,109)=1\),

\[
\gcd(2367+1,4033)=\gcd(2367-443,4033)=37.
\]

An exhaustive support-two scan over the literal exponent menu necessarily
includes the assignment \(e_5=2\), \(e_2=8\). Its canonical representative
and inverse expose \(37\). Therefore that scan factors this fixed
post-refinement state.

## Scope

The CRT formulas are exact bookkeeping. They do not create a new source or
prove provenance. The finite examples establish only non-extension-monotonicity
of the named scalar scores. Canonical-residue closure is a genuine operation
change even though it stays inside \(H\), and the displayed support-two
certificate closes the finite-positive-box caveat for this fixed
\(N=4033\), \(H_1=\langle2,5\rangle\) state.

Nothing here proves that an arbitrary input reaches this state, that every
useful subgroup has a separator in a polynomial exponent menu, or that a
random or capped search finds a separator with inverse-polynomial
probability. The statement and certificates do not constitute a factoring
algorithm.
