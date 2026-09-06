# Proof of F273

## 1. Child-zero ideals

Write \(F\) as a polynomial in \(e_0\):

\[
 F=\sum_{i\geq0}e_0^iF_i(o_0,z),
 \qquad
 F_i\in A[o_0,z_1,\ldots,z_r].
\tag{27}
\]

Substitution \(e_0=0\) gives \(F_0(o_0,z)\). Therefore
\(F(0,o_0,z)=0\) as a polynomial if and only if \(F_0=0\), which is
equivalent to \(e_0\mid F\). This proves (2).

If the second identity in (3) also holds, expand \(F\) jointly:

\[
 F=\sum_{i,j\geq0}e_0^io_0^jF_{i,j}(z).
\tag{28}
\]

The first axis identity removes every term with \(i=0\). The second removes
every term with \(j=0\). Every remaining monomial is divisible by
\(e_0o_0\), proving (4). This direct coefficient argument does not require
a Bézout identity.

For a rational observable \(G/H\) defined on a generic axis, equality to
zero in the corresponding rational function field forces the specialized
numerator \(G\) to be zero. Applying the polynomial argument to \(G\)
proves the stated numerator divisibility. If the denominator vanishes on
an axis, the rational expression is not a total observable there and the
claim deliberately does not apply.

The argument treats the \(z_i\) as independent variables. A relation among
actual affine jets can identify a smaller quotient ring in which the
intersection of the two specialized ideals behaves differently. Likewise,
a polynomial identity true only in a fixed finite characteristic need not
lift to (1). These are exclusions, not consequences of the theorem.

For Corollary 1.1, let \(U\) be the union of the leaf sets on which the
\(K\) base summaries depend. Every arithmetic expression built from those
summaries and public leaf-independent descriptors lies in

\[
 A[y_j:j\in U]
\tag{29}
\]

or its rational function field. If some \(y_h\) is absent from \(U\), that
expression is independent of \(y_h\), whereas the target in (5) has
positive degree one in \(y_h\). Equality is impossible. Hence \(U\)
contains all \(M\) leaves. Since each summary contains at most \(q_0\)
leaves,

\[
 M\leq |U|\leq Kq_0,
\]

which proves (6). The same proof applies to every fixed truncated jet
because a jet of a block depends only on the leaves in that block.

## 2. Determinantal divisors

For a matrix over a field, rank at least \(k\) is equivalent to the
existence of a nonzero \(k\times k\) minor.

Fix \(k<m\). The first rank hypothesis in (7) supplies a \(k\)-minor not
divisible by \(p\). Therefore \(p\nmid\Delta_k(M)\). The second rank
hypothesis supplies a possibly different \(k\)-minor not divisible by
\(q\). Therefore \(q\nmid\Delta_k(M)\). Since \(N=pq\),

\[
 \gcd(\Delta_k(M),N)=1.
\tag{30}
\]

For \(k=m\), the only minor is the determinant. Rank \(m-1\) modulo \(p\)
gives \(p\mid\det M\), while full rank modulo \(q\) gives
\(q\nmid\det M\). Hence

\[
 \gcd(\Delta_m(M),N)
=\gcd(|\det M|,pq)=p.
\tag{31}
\]

This proves (8).

For the integer Smith normal form, the invariant factors are

\[
 d_k=\Delta_k/\Delta_{k-1}.
\tag{32}
\]

Equation (30) says that \(p\) divides none of
\(\Delta_1,\ldots,\Delta_{m-1}\), while (31) says that \(p\) divides
\(\Delta_m\). Thus the guaranteed \(p\)-support first occurs in \(d_m\).

Now assume (9). The standard inequalities give

\[
 p\leq B<q,\qquad B<2p.
\tag{33}
\]

Among \(1,\ldots,B\), exactly the entry \(p\) vanishes modulo \(p\), and
none vanishes modulo \(q\). The diagonal matrix (10) consequently has
ranks \(B-1\) and \(B\) in the two fields. Its determinant is \(B!\).
Theorem 2 applies exactly as stated.

## 3. The derivative resultant

The roots of \(P_m\) are the distinct integers

\[
 -1,-2,\ldots,-m.
\]

For a monic polynomial, the absolute value of the resultant with its
derivative is the product of squared pairwise root differences. Therefore

\[
 D_m
=\prod_{1\leq i<j\leq m}(j-i)^2.
\tag{34}
\]

For a fixed difference \(d=j-i\), there are exactly \(m-d\) pairs.
Grouping (34) by differences gives

\[
 D_m=\prod_{d=1}^{m-1}d^{2(m-d)}.
\tag{35}
\]

In the product

\[
 \prod_{k=1}^{m-1}k!,
\]

the integer \(d\) occurs in the factorials \(d!,\ldots,(m-1)!\), exactly
\(m-d\) times. Squaring proves the second identity in (13).

Replacing \(m\) by \(m+1\) in (35) gives

\[
 \frac{D_{m+1}}{D_m}
=\prod_{d=1}^{m}d^2
=(m!)^2,
\tag{36}
\]

which proves (14) as an identity of positive integers. No modular division
is used.

For the size upper bound,

\[
 \log_2D_m
=2\sum_{d=1}^{m-1}(m-d)\log_2d
\leq2m^2\log_2m.
\tag{37}
\]

For \(m\geq8\), restrict the sum to
\(\lceil m/4\rceil\leq d\leq\lfloor m/2\rfloor\). There are
\(\Omega(m)\) terms, each has \(m-d\geq m/2\) and
\(\log_2d=\Omega(\log m)\). Hence

\[
 \log_2D_m=\Omega(m^2\log m).
\tag{38}
\]

The finitely many smaller \(m\) are absorbed into the constants, and
\(\operatorname{bitlen}(D_m)=\lfloor\log_2D_m\rfloor+1\) proves (15).

Return to (9). If \(\gcd(B,N)>1\), then (33) makes it a proper divisor and
the cleanup exits. On the unresolved branch, \(B\ne p\). Since \(p\leq B\),
one has

\[
 p\leq B-1<q.
\tag{39}
\]

The base \(d=p\) occurs in (35) with positive exponent
\(2(B-p)\), so \(p\mid D_B\). Every base \(d\) in (35) is smaller than
\(q\), so \(q\nmid D_B\). Because \(N=pq\), equation (16) follows.

Equivalently, modulo \(p\) the roots of \(P_B\) have a collision separated
by \(p\), while modulo \(q\) all \(B\) roots remain distinct. This is the
same discriminant calculation, not an evaluator.

## 4. Cross-resultant recursion

The roots of \(P_{0,m}\) are \(-i\) for \(0\leq i<m\). Evaluating the
second monic polynomial at those roots gives

\[
 \operatorname{Res}(P_{0,m},P_{cm,m})
=\prod_{i=0}^{m-1}\prod_{j=0}^{m-1}(cm+j-i).
\tag{40}
\]

For \(c\geq1\), the smallest factor is
\((c-1)m+1>0\), proving (18) without a sign ambiguity.

Split each length-\(2m\) block into its two length-\(m\) children:

\[
 P_{0,2m}=P_{0,m}P_{m,m},
\qquad
 P_{2cm,2m}=P_{2cm,m}P_{(2c+1)m,m}.
\tag{41}
\]

The resultant is multiplicative in each polynomial. The four child pairs
have normalized separations

\[
 2c,\qquad 2c+1,\qquad 2c-1,\qquad 2c.
\]

Multiplying their resultants proves (19).

Let \(C_t\) be the set of offsets present after \(t\) complete expansions
starting from \(c=1\). Equation (19) gives

\[
 C_{t+1}
=\bigcup_{c\in C_t}\{2c-1,2c,2c+1\}.
\tag{42}
\]

The initial expansion gives \(C_1=\{1,2,3\}\). If

\[
 C_t=\{1,\ldots,2^{t+1}-1\},
\]

then the intervals contributed by consecutive \(c\) overlap at their
endpoints and their union is

\[
 \{1,\ldots,2^{t+2}-1\}.
\]

Induction proves (20) and the exact distinct-state count.

## 5. Superfactorial telescoping

For fixed \(i\), the inner product in (40) is

\[
 \prod_{j=0}^{m-1}(cm+j-i)
=\frac{((c+1)m-1-i)!}{(cm-1-i)!}.
\tag{43}
\]

Multiplying (43) over \(i=0,\ldots,m-1\) gives

\[
 R_c(m)
=
\frac{\displaystyle\prod_{r=cm}^{(c+1)m-1}r!}
     {\displaystyle\prod_{r=(c-1)m}^{cm-1}r!}.
\tag{44}
\]

With \(S\) from (21),

\[
 \prod_{r=u}^{v}r!=\frac{S(v+1)}{S(u)}
\tag{45}
\]

for the nonnegative endpoints occurring here. Substitution into (44)
proves (22). The convention \(S(0)=1\) treats the \(c=1\) lower endpoint.

The definition immediately gives

\[
 S(m+1)=S(m)m!.
\tag{46}
\]

The second form of (13) gives \(D_m=S(m)^2\). This proves (23).

Equation (22) is an exact quotient because it was derived from the integer
product (40). A modular algorithm cannot replace that exact cancellation
by inverse multiplication unless it first proves
\(\gcd(S(cm),N)=1\). On the balanced unresolved branch, (39) shows that
the factor \(p!\) occurs in \(S(B)\), while no integer at most \(B-1\)
contains \(q\) as a prime factor. Hence

\[
 p\mid S(B),\qquad q\nmid S(B),
\]

which proves (24).

Thus a literal use of (19) generates the stated offset family. Replacing
the family by (22) requires remote values of the weighted product \(S\).
No statement here excludes a third identity outside these presentations.

## 6. Literal resource count

Take \(M=2^tq_0\). Expanding \(R_1(M)\) down to length \(q_0\) applies
(19) exactly \(t\) levels and produces

\[
 2^{t+1}-1=\frac{2M}{q_0}-1
\tag{47}
\]

distinct base offsets.

For the discriminant, splitting roots into two adjacent equal blocks gives
the standard identity

\[
 D_{2m}=D_m^2R_1(m)^2.
\tag{48}
\]

Starting from \(D_M\), its top cross term is \(R_1(M/2)\). Expanding this
term down to \(q_0\) gives

\[
 \frac{M}{q_0}-1
\tag{49}
\]

distinct offsets when \(t\geq1\). This proves the
\(\Theta(M/q_0)\) count in the statement.

Let

\[
 Q(n)=2^{C(\log_2(n+1))^k}
\]

be fixed. Then \(\log_2Q(n)=o(n)\). If
\(M=2^{\Theta(n)}\) and \(q_0\leq Q(n)\),

\[
 \log_2(M/q_0)=\Theta(n)-o(n)=\Theta(n),
\]

which proves (25). A residue modulo an \(n\)-bit modulus takes
\(\Theta(n)\) bits in the literal state representation. The storage and
state-operation counts follow. They do not apply to a representation that
does not enumerate these states.

## 7. Imported carry boundaries and conclusion

No theorem above uses P173, P174, or P177 as a premise. Their hashes are
recorded only to distinguish the already promoted carry and finite-residue
routes from this packet. In particular, the ideal argument never treats a
floor as a polynomial, and the resultant argument never treats an exact
quotient as modular inversion.

The child-zero lemma closes only the independent-coordinate polynomial
handoff. The Smith theorem closes only one local rank defect. The
discriminant and cross-resultant theorems close only the displayed
weighted-product and literal-recursion presentations. The exact exclusions
in the statement therefore follow.
