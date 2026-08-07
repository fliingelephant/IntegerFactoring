# F71 — cyclotomic order-three endpoint-feedback trap

## Status

Proof-only candidate. No research computation was used. This corrected version
has not yet passed a fresh hostile audit or proof-blind reconstruction.

## 1. Result

Let \(c\) be an odd prime and put

\[
N=c^2+c+1.
\]

Assume that \(N\) is composite and \(3\nmid N\). Start from the canonical
inverse relation

\[
c\cdot c^2=c^3=1+(c-1)N. \tag{1}
\]

Its complete gcd-free endpoint presentation has one prime block, \(c\). The
following endpoint-only feedback system is trapped:

1. form any product or power of authorized occurrences of the current block;
2. optionally reduce it modulo \(N\);
3. take its canonical inverse;
4. append the inverse relation;
5. apply exact integer gcd refinement, perfect-power extraction, direct sign,
   inverse-pair difference and discriminant screens, and the complete rational-
   square decoder.

Every finite transcript remains in the monoid of powers of \(c\). It creates
no second gcd-free block. Every proper direct screen fails. Every decoded
square root is the global identity modulo \(N\).

This is a method obstruction. It is not a factoring algorithm or a general
factoring lower bound.

## 2. The full generated subgroup is closed

For every prime power \(p^a\Vert N\), the residue of \(c\) has exact order
three. Equation (1) gives \(c^3\equiv1\pmod {p^a}\), so the order divides
three. If it were one, then \(c\equiv1\pmod p\), and substitution into
\(c^2+c+1\equiv0\pmod p\) would give \(p=3\). This contradicts
\(3\nmid N\).

Therefore

\[
H=\langle c\rangle=\{1,c,c^2\}\pmod N. \tag{2}
\]

The displayed integers are their canonical representatives because
\(1<c<c^2<N\). Each positive divisor of a representative is a power of the
prime \(c\). Thus complete integer gcd refinement of these representatives
cannot create a new block.

The subgroup contains no direct sign separator. In every prime-power
component, \(c\) and \(c^2\) have order three, so

\[
\gcd(c\pm1,N)=\gcd(c^2\pm1,N)=1. \tag{3}
\]

This is an unbounded subgroup statement, not only a finite-occurrence-box
statement.

## 3. Canonical feedback is a fixed point

Under the original legal-divisor rule, a selected integer must satisfy
\(1<g<N\). Since \(c^3>N\), the only legal positive powers are \(c\) and
\(c^2\). They are canonical inverses of one another. Either orientation
appends the same relation (1).

Now allow arbitrary occurrence multiplicity followed by canonical reduction.
Exact order three gives

\[
c^e\bmod N=
\begin{cases}
1,&e\equiv0\pmod3,\\
c,&e\equiv1\pmod3,\\
c^2,&e\equiv2\pmod3.
\end{cases} \tag{4}
\]

The first state is not legal because \(g=1\). If it is retained, it adds only
the trivial relation \(1\cdot1=1\). The other states append (1). Hence the
nontrivial endpoint set remains \(\{c,c^2\}\), the nontrivial relation-value
set remains \(\{c^3\}\), and the sole block remains \(c\).

## 4. Retaining oversized raw powers also remains trapped

A larger rule can retain a raw integer \(G=c^e\ge N\) instead of replacing it
by its canonical residue. Let \(w=c^j\), with \(j\in\{0,1,2\}\), be the
canonical inverse of that residue. Then \(e+j\equiv0\pmod3\), and the new
relation value is

\[
Gw=c^{e+j}=c^{3t} \tag{5}
\]

for some \(t\ge1\). It need not equal \(c^3\), but it is still a pure power
of the old prime block. Exact gcd refinement still creates no new block.

The direct screens give no proper factor. A nonidentity residue is \(c\) or
\(c^2\), so (3) applies. An identity residue makes the minus screen return
\(N\) and the plus screen return \(1\).

For the inverse-pair discriminant, put \(d=G-w\). Since \(Gw\equiv1\pmod N\),

\[
d^2+4\equiv(G+w)^2\pmod N. \tag{6}
\]

For a nontrivial orientation, \(G+w\equiv c+c^2\equiv-1\pmod N\). For the
identity orientation, \(G+w\equiv2\pmod N\). As \(N\) is odd,
\(\gcd(d^2+4,N)=1\) in both cases. The difference screen is also trivial or
global.

## 5. The complete square decoder gives only the identity

Under canonical reduction, every nontrivial indexed relation value is \(c^3\).
The parity matrix has one row and an entry \(1\) in each column. Its kernel is
the even-weight subspace. A dependency of weight \(2m\) has exact positive
root

\[
\sqrt{(c^3)^{2m}}=c^{3m}\equiv1\pmod N. \tag{7}
\]

For the larger raw-power rule, let the indexed relation values be
\(c^{3t_i}\). A selected product is a rational square exactly when
\(\sum_i x_it_i\) is even. Its exact positive root is

\[
c^{\frac32\sum_i x_it_i}
=(c^3)^{\frac12\sum_i x_it_i}
\equiv1\pmod N. \tag{8}
\]

Thus the image of the full rational-square relation space is exactly
\(\{1\}\). Integer relation coefficients and complete \(2\)-saturation do not
change this conclusion.

## 6. Perfect-power checks do not escape

The public exact squares

\[
c^2=(c)^2,
\qquad
4N-3=(2c+1)^2 \tag{9}
\]

recover \(c\), a power of \(c\), or \(2c+1\). They do not split \(N\).
Likewise, extracting a perfect-power root from \(c^{3t}\) stays inside the
same one-block monoid.

The infinite construction below also forces two prime divisors of \(N\) to
have valuation one. Therefore \(N\) itself is not a perfect power.

## 7. Infinite family with growing least factor

### Theorem

For every integer \(B\ge3\), infinitely many odd primes \(c\) satisfy all of
the following conditions:

1. \(N=c^2+c+1\) is composite and \(3\nmid N\);
2. \(N\) has at least two distinct prime divisors;
3. every prime divisor of \(N\) is greater than \(B\);
4. two prime divisors occur to exact exponent one, so \(N\) is not a perfect
   power.

### Proof

Choose distinct primes

\[
\ell_1,\ell_2>B,
\qquad
\ell_i\equiv1\pmod3.
\]

For each \(i\), choose a nontrivial cube root \(r_i\pmod{\ell_i}\). It is a
root of \(F(X)=X^2+X+1\). The derivative \(F'(r_i)=2r_i+1\) is nonzero
modulo \(\ell_i\); otherwise \(r_i\equiv-1/2\) would force
\(\ell_i=3\). Exactly one lift of \(r_i\) modulo \(\ell_i^2\) is a root
modulo \(\ell_i^2\). Choose a different lift \(a_i\). Then

\[
F(a_i)\equiv0\pmod{\ell_i},
\qquad
F(a_i)\not\equiv0\pmod{\ell_i^2}. \tag{10}
\]

Impose

\[
\begin{aligned}
c&\equiv a_i &&\pmod{\ell_i^2},\quad i=1,2,\\
c&\equiv1 &&\pmod2,\\
c&\equiv2 &&\pmod3,\\
c&\equiv1 &&\pmod q
&&\text{for every prime }5\le q\le B.
\end{aligned} \tag{11}
\]

The moduli are pairwise coprime, and the prescribed class is a unit class.
The Chinese remainder theorem gives one reduced residue class. Dirichlet's
theorem gives infinitely many primes \(c\) in that class.

Equation (10) gives

\[
v_{\ell_1}(N)=v_{\ell_2}(N)=1. \tag{12}
\]

Thus \(N\) has at least two distinct prime factors and is not a perfect power.
No prime at most \(B\) divides \(N\): modulo \(3\), \(F(c)\equiv1\); modulo
each prime \(5\le q\le B\), \(F(c)\equiv F(1)=3\not\equiv0\); and \(N\)
is odd. This proves the theorem.

Taking \(B\to\infty\) gives a sequence whose least prime factor tends to
infinity. This construction does not claim that these inputs are hard. Their
special shape is recognizable from \(4N-3=(2c+1)^2\), which recovers \(c\)
but not a factor of \(N\).

## 8. Small witness

For \(c=11\),

\[
N=11^2+11+1=133=7\cdot19.
\]

The seed is \(11\cdot121=1331=1+10\cdot133\). The subgroup
\(\{1,11,121\}\) has order three modulo both factors. Two copies close the
square class, but their exact root is \(1331\equiv1\pmod{133}\).

## 9. Relation to the live route

P70 proves that cross-relation feedback can create a new relation and can use
repeated occurrences to reach a useful value near \(\sqrt N\). This theorem
shows that occurrence amplification is not a universal source mechanism. In
this family, the full old subgroup has odd order three and has no useful sign
element. It is stronger than P71's finite-box obstruction.

P73 square-class closure still occurs: two duplicate columns close. P74's
second gate then fails exactly because every induced root is the global
identity. P76's endpoint-refinement gain is absent because all endpoints are
powers of the same prime block.

The trap does not cover adding an independent seed relation or block. The
public quotient \(c-1\) in (1) is not an endpoint block. Feeding it is a
materially different source operation. Additive combinations, non-endpoint
integer data, order or period methods, and arbitrary algorithms also remain
outside the theorem.

**Classification:** candidate approach-family obstruction for sole-block
occurrence amplification. It is not an all-input source obstruction and not a
factoring algorithm.
