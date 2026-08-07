# Result: PASS

The statement has SHA-256
218244fb1c1532df0e9f3bbbc836e1e6e0d607f49517ca9d82901ef8211df5f3,
as required.

All numerical constants, algebraic claims, and quantified assertions are
correct. One scope convention is necessary because “useful mass” is not
separately defined in the setup: the zero-useful-mass conclusion means zero
mass for the four direct endpoint tickets
\(\gcd(g\pm1,N),\gcd(h\pm1,N)\) and the stated discriminant ticket. It cannot
mean failure of every conceivable computation on the public data. That
restricted meaning is also required by the final scope paragraph.

## 1. Magnitude boundary

For a balanced-canonical split, \(g\) and \(h\) are positive integers at most
\(N-1\), and \(A=gh\). Hence

\[
A\leq(N-1)^2=N^2-2N+1=1+(N-2)N.
\]

Since \(A=1+kN\), this gives \(k\leq N-2\). Equality in the product bound
requires equality in both bounds \(g\leq N-1\) and \(h\leq N-1\), so
\(g=h=N-1\). This is the global self-inverse root modulo \(N\). Under the
premise that a split exists, no other endpoint pair can occur at equality.

Now consider

\[
P=\prod_i(1+k_iN).
\]

Each occurrence with \(k_i\geq1\) is at least \(N+1\). Thus two such
occurrences imply

\[
P\geq(N+1)^2>(N-1)^2.
\]

If \(1<g<N\) divides \(P\), then \(g\leq N-1\), and therefore

\[
\frac Pg\geq\frac{(N+1)^2}{N-1}
=N+3+\frac4{N-1}>N.
\]

In particular, no factor pair of \(P\) can have both members below \(N\).
Also \(P\equiv1\pmod N\), and every divisor of \(P\) is coprime to \(N\).
Consequently the canonical inverse of \(g\) is the unique representative

\[
w\equiv P/g\pmod N,\qquad 1\leq w<N.
\]

The raw complement \(P/g>N\) and its residue \(w\) can have unrelated
ordinary magnitudes. This proves the claimed separation between integer
partition balance and canonical inverse balance.

## 2. One-relation whole-block redundancy

For one retained relation,

\[
g(c)h(c)
=\prod_jq_j^{c_j}\prod_jq_j^{E_j-c_j}
=\prod_jq_j^{E_j}=A.
\]

Thus the selected inverse relation has exactly the old integer value.
Both endpoints use only the old bases \(q_j\), with exponent vectors \(c\)
and \(E-c\).

More explicitly, the gcd of any two products of these pairwise-coprime
bases has the form

\[
\gcd\!\left(\prod_jq_j^{a_j},\prod_jq_j^{b_j}\right)
=\prod_jq_j^{\min(a_j,b_j)}.
\]

It can expose powers of an existing whole block, but it cannot split a
composite \(q_j\) internally or create a new coprime base. Hence complete
joint gcd refinement changes no block information.

The parity vector of the selected relation is

\[
c+(E-c)\equiv E\pmod2,
\]

which is the old square-class column. If an indexed duplicate is appended,
the two equal columns form the duplicate dependency. The corresponding
integer product is \(A^2\), whose positive square root is

\[
A\equiv1\pmod N.
\]

It therefore supplies only the global root class; the negative choice is
the other global class. Subject to failed public screens and a fixed
occurrence capacity, the value set, block set, and allowed occurrence box
are unchanged. Counting the duplicate as an additional occurrence changes
that last premise: it deliberately enlarges the source multiplicity, rather
than extracting new information from balance.

## 3. Required logarithmic precision

Assume \(g\leq h\). Since \(A=gh\),

\[
\beta
=\frac12(\log h-\log g)
=\frac12\log(h/g).
\]

Solving the two equations \(\log g+\log h=\log A\) and
\(\log h-\log g=2\beta\) gives

\[
g=\sqrt A\,e^{-\beta},
\qquad
h=\sqrt A\,e^\beta.
\]

Therefore

\[
\delta=h-g
=\sqrt A(e^\beta-e^{-\beta})
=2\sqrt A\,\sinh\beta.
\]

Since \(\sinh\) is strictly increasing on the nonnegative reals,

\[
\delta\leq D
\quad\Longleftrightarrow\quad
\beta\leq\operatorname{arsinh}\!\left(\frac D{2\sqrt A}\right).
\]

If \(A=\Theta(N^2)\) and \(D=O((\log N)^C)\) for a fixed \(C\), then
\(D/(2\sqrt A)=O((\log N)^C/N)=o(1)\). Since
\(\operatorname{arsinh}x=\Theta(x)\) as \(x\to0\), the required tolerance is

\[
\beta=O\!\left(\frac{(\log N)^C}{N}\right)
=2^{-\Omega(\log N)}.
\]

Thus invoking an FPTAS at a relative or log tolerance
\(\varepsilon=O(D/\sqrt A)\) makes \(1/\varepsilon\) exponential in the bit
length \(\Theta(\log N)\). A running-time guarantee polynomial in
\(1/\varepsilon\) consequently gives no bit-polynomial guarantee at this
scale. This is only a precision barrier for that invocation; it proves no
NP-hardness statement.

## 4. The exact finite examples

For the first family, use the one-block presentation

\[
q_1=N-1,\qquad E_1=2.
\]

It is valid because \(\gcd(N-1,N)=1\), and
\[
q_1^{E_1}=(N-1)^2=1+(N-2)N.
\]
The choices \(c_1=0,2\) have an endpoint equal to \(1\). The only admissible
choice is \(c_1=1\), which gives \(g=h=N-1\).

For this endpoint, the direct screens return only

\[
\gcd(N-2,N)=1,\qquad \gcd(N,N)=N,
\]

with repetitions for the two equal endpoints. The signed difference is
zero, so its discriminant is \(4\), coprime to odd \(N\). Thus every named
screen is trivial for every odd composite \(N\).

For the second example,

\[
209=11\cdot19,\qquad
6480=1+31\cdot209=2^4 3^4 5.
\]

The strict inequalities

\[
80^2=6400<6480<6561=81^2
\]

show that \(\sqrt{6480}\) lies strictly between \(80\) and \(81\). In every
unordered factor pair, the smaller factor is an integer at most \(80\).
Because \(80\mid6480\), it is the largest possible smaller factor and gives
the unique closest pair \(80\cdot81\). No divisor enumeration is needed.

The four endpoint quantities are \(79,81,80,82\). None is divisible by
\(11\) or \(19\), so all four endpoint gcds are \(1\). The endpoint
difference is one, and

\[
\gcd(1^2+4,209)=\gcd(5,209)=1.
\]

Thus the unique closest pair survives the stated screens.

The same exponent box also permits

\[
45=3^2\cdot5,\qquad
144=2^4\cdot3^2,\qquad
45\cdot144=6480.
\]

This farther pair exposes

\[
\gcd(45-1,209)=\gcd(44,209)=11.
\]

Hence improving the exact multiplicative balance can change a
factor-revealing split into a non-revealing split. Factor usefulness is not
monotone in closeness.

## 5. Infinite family

Let \(t\geq5\) be any integer divisible by \(5\), and set

\[
a=t^2+t-1,\qquad b=t^2+3t+1.
\]

Both numbers exceed \(1\). The products \(t(t+1)\) and \(t(t+3)\) are even,
so \(a\) and \(b\) are odd. Moreover,

\[
b-a=2(t+1),
\qquad
a\equiv-1\pmod{t+1}.
\]

Thus \(\gcd(a,t+1)=1\). Since \(a\) is odd,

\[
\gcd(a,b)=\gcd(a,2(t+1))=1.
\]

Both \(a\) and \(b\) are \(t^2(1+O(1/t))\), so \(b/a\to1\). Finally,
\(t\equiv0\pmod5\) gives

\[
a\equiv-1\pmod5,\qquad b\equiv1\pmod5.
\]

Therefore \(N=ab\) is odd, has the two nontrivial coprime factors \(a,b\),
is balanced in the asserted asymptotic sense, and satisfies
\(\gcd(N,5)=1\).

Let \(u\in\{0,\ldots,N-1\}\) be the CRT solution from the statement. Because
polynomial evaluation respects congruences,

\[
F(u)\equiv F(t)=a\equiv0\pmod a,
\qquad
F(u)\equiv F(t+1)=b\equiv0\pmod b.
\]

Coprimality of \(a,b\) gives \(N\mid F(u)\). The four possible boundary
representatives have

\[
F(0)=-1,\quad F(1)=1,\quad
F(N-2)\equiv F(-2)=1\pmod N,\quad
F(N-1)\equiv F(-1)=-1\pmod N.
\]

None is divisible by \(N\). Hence

\[
2\leq u\leq N-3.
\]

In particular \(F(u)>0\). Thus

\[
F(u)=kN
\]

for an integer \(k\geq1\), and

\[
A=u(u+1)=F(u)+1=1+kN.
\]

The endpoints \(u,u+1\) both lie strictly between \(1\) and \(N\), and
\(u(u+1)\equiv1\pmod N\). They are therefore canonical inverse units.
They are consecutive, so the proposed blocks

\[
q_1=u,\qquad q_2=u+1,\qquad E=(1,1)
\]

are pairwise coprime. Their product being \(1\) modulo \(N\) also proves
that each block is individually coprime to \(N\).

There are only four exponent choices. Choices \((0,0)\) and \((1,1)\) put
\(1\) at one endpoint. Choices \((1,0)\) and \((0,1)\) give the same
unordered pair \(\{u,u+1\}\). Hence this pair is the unique admissible
unordered balanced-canonical split, and its distance is \(1\).

The two middle direct quantities \(u\) and \(u+1\) are units. If a prime
\(r\mid N\) also divided \(u-1\), substitution of \(u\equiv1\pmod r\) into
\(F(u)\equiv0\pmod r\) would give \(1\equiv0\pmod r\). If \(r\) divided
\(u+2\), substitution of \(u\equiv-2\pmod r\) would give the same
contradiction. Therefore

\[
\gcd(u-1,N)=\gcd(u,N)=\gcd(u+1,N)=\gcd(u+2,N)=1.
\]

These are precisely the four endpoint-\(\pm1\) screens for \(u,u+1\).
The signed difference is \(\pm1\), so its discriminant is \(5\), and
\(\gcd(5,N)=1\). For completeness, the alternative pair screens also give
\(\gcd((u+1)-u,N)=1\); and if a prime divisor of \(N\) divided \(2u+1\),
then

\[
(2u+1)^2=4F(u)+5
\]

would force that prime to divide \(5\), which is impossible.

For \(u\geq2\),

\[
u^2<u(u+1)<(u+1)^2.
\]

Thus \(A=u(u+1)\) is not an integer square.

The admissible split set of the fixed box \(E=(1,1)\) is a singleton, and
that singleton triggers none of the five named factor tickets. Appending
the same endpoint pair leaves its integer value, its two block values, and
that fixed-capacity split set unchanged. It changes multiplicity only if
the algorithm explicitly enlarges the occurrence capacity. Consequently,
every probability distribution on this admissible split set assigns
exactly zero mass to a split useful through the named screens.

Finally, at \(t=3\),

\[
a=F(3)=11,\qquad b=F(4)=19,\qquad N=209.
\]

The integer \(80\) satisfies

\[
80\equiv3\pmod{11},\qquad80\equiv4\pmod{19},
\]

so it is the stated CRT representative, and
\[
F(80)=6479=31\cdot209,\qquad80\cdot81=6480.
\]
This verifies the finite instance, while \(5\nmid3\) verifies that it lies
outside the quantified subfamily.

## Scope

The proofs show that raw multiplicative closeness alone cannot universally
guarantee one of the named factor tickets, even if an exact closest
partition is free. They do not show that partition approximation is hard,
that every statistic of the blocks is uninformative, or that the public
data admit no other factor screen. In particular, the infinite family is a
counterexample to the claimed balance-to-ticket implication, not an
information-theoretic or general computational lower bound. If the family
parameter \(t\) is supplied, for example,
\(\gcd(u-t,N)=a\): the difference is \(0\) modulo \(a\) and \(-1\) modulo
\(b\). Oversized cross-relation complements reduce modulo \(N\), and
internal block refinement changes the available information; none of these
mechanisms is covered by this result.
