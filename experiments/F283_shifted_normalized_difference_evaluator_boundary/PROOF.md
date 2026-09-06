# Proof of F283

## 1. Generalized-Stirling identities

For distinct nodes \(x_0,\ldots,x_k\), the monomial divided-difference
identity is

\[
 [x_0,\ldots,x_k]X^n=h_{n-k}(x_0,\ldots,x_k).
\tag{33}
\]

Apply (33) to \(x_j=a+j\). Newton interpolation in the basis

\[
 (X-a)_{\underline{k}}=\prod_{j=0}^{k-1}(X-a-j)
\]

gives

\[
 X^n=\sum_{k=0}^n[a,a+1,\ldots,a+k]X^n
                   (X-a)_{\underline{k}}.
\]

This proves (3) and (5). The identity

\[
 X(X-a)_{\underline{k}}
 =(X-a)_{\underline{k+1}}+(a+k)(X-a)_{\underline{k}}
\]

then gives (6) by comparing coefficients after multiplying (5) by \(X\).
Equation (4) is (3) at \((n,k)=(2B,B)\).

For nonnegative \(r\), the same connection coefficients are the standard
\(r\)-Stirling numbers with the first \(r\) elements required to lie in
different blocks. Equivalently, this follows from their exponential
generating function

\[
 \sum_{n\ge k}
 \left\{\begin{matrix}n+r\\k+r\end{matrix}\right\}_r
 \frac{z^n}{n!}
 =\frac1{k!}e^{rz}(e^z-1)^k.
\]

This proves (7) and (8). Finally, (33) directly gives

\[
 G_a(B+d,B)=h_d(a,a+1,\ldots,a+B).
\]

The ordinary generating function for complete homogeneous polynomials is

\[
 \sum_{d\ge0}h_d(x_0,\ldots,x_B)t^d
 =\prod_{j=0}^B(1-x_jt)^{-1}.
\]

Substitution of \(x_j=a+j\) proves (9).

## 2. Distinct poles and the canonical linear realization

Over \(K=\mathbb Q(a)\), the elements

\[
 a,a+1,\ldots,a+B
\]

are distinct. Thus the denominator in (10) is a product of \(B+1\)
distinct linear factors. Its numerator is one, so none can cancel.

A homogeneous constant-coefficient recurrence of order \(d\) for a scalar
sequence over a field gives a rational generating function whose reduced
denominator has degree at most \(d\). Conversely, the reduced denominator
is the characteristic polynomial of the minimal recurrence, written in
reciprocal form. Since (10) has reduced denominator degree \(B+1\), every
such recurrence has order at least \(B+1\). The same argument applies if
the recurrence starts only after finitely many terms: changing a finite
prefix changes the generating function by a polynomial and cannot remove
one of its poles.

A \(d\)-dimensional linear constant-matrix realization has generating
function denominator dividing \(\det(I-tM)\), of degree at most \(d\).
Therefore any realization of the full sequence in (10) has
\(d\ge B+1\).

For the decimation claim, partial fractions over \(K\) give

\[
 u_d=\sum_{j=0}^{B}A_j(a+j)^d,
 \qquad
 A_j=\frac{(a+j)^B}
 {\prod_{0\le i\le B,\ i\ne j}((a+j)-(a+i))}.
\tag{34}
\]

Every \(A_j\) is nonzero in \(K\). For fixed \(r\ge1\) and \(c\ge0\),

\[
 u_{rd+c}=\sum_{j=0}^{B}
 A_j(a+j)^c\bigl((a+j)^r\bigr)^d.
\tag{35}
\]

The \(B+1\) rational functions \((a+j)^r\) are pairwise distinct, and
all displayed coefficients are nonzero in \(K\). Hence the decimated
sequence has \(B+1\) distinct uncancelled modes. Its minimal
constant-coefficient recurrence again has order \(B+1\).

For the explicit matrix (12), let \(v_n\) have coordinates
\(v_n(k)=G_a(n,k)\), with \(G_a(n,k)=0\) outside \(0\le k\le n\). Equation
(6) says exactly that

\[
 v_{n+1}=M_B(a)v_n,
 \qquad v_0=e_0.
\]

Taking coordinate \(B\) at time \(2B\) proves (13). This construction
matches the lower bound because its dimension is \(B+1\).

The proof used the entire sequence in the excess index \(d\), or the entire
generalized-Stirling trajectory. It did not prove that one isolated endpoint
cannot have a different succinct circuit.

## 3. Translation and interval splits

For variables \(x_0,\ldots,x_B\), put

\[
 H_x(t)=\prod_{i=0}^{B}(1-x_it)^{-1}.
\]

After translating every variable by \(c\),

\[
 \begin{aligned}
 H_{x+c}(t)
 &=\prod_{i=0}^{B}(1-(x_i+c)t)^{-1}\\
 &=(1-ct)^{-(B+1)}
   H_x\!\left(\frac{t}{1-ct}\right)\\
 &=\sum_{j\ge0}h_j(x)t^j(1-ct)^{-(B+1+j)}.
 \end{aligned}
\]

The coefficient of \(t^B\) is

\[
 \sum_{j=0}^{B}
 h_j(x)c^{B-j}
 \binom{(B+1+j)+(B-j)-1}{B-j}
 =\sum_{j=0}^{B}\binom{2B}{B-j}c^{B-j}h_j(x).
\]

Taking \(x_j=a+j\) proves (14). In characteristic zero, every binomial
coefficient displayed here is nonzero, and each \(h_j(a,\ldots,a+B)\) is a
nonzero polynomial. This is the stated full-width property of the literal
translation formula.

The multiset of nodes at shift \(-B-a\) is the negative of the original
multiset, in reverse order. Complete homogeneous degree \(B\) is homogeneous
of total degree \(B\), so

\[
 F_B(-B-a)=(-1)^BF_B(a).
\]

Also,

\[
 \begin{aligned}
 F_B(a+1)-F_B(a)
 &=\frac{\Delta^{B+1}X^{2B}|_{X=a}}{B!}\\
 &=(B+1)h_{B-1}(a,a+1,\ldots,a+B+1).
 \end{aligned}
\]

These prove the two shorter shift laws. Multiplication by a public unit and
translation are bijections of \(\mathbb Z/N\mathbb Z\), which proves the
sampling statement.

The displayed rising-factorial identity follows by factoring \(-t^{-1}\)
from every term of
\((a-t^{-1})^{\overline{L+1}}\). Its usual even--odd multiplication formula
is obtained by separating the factors with even and odd offsets, exactly as
in the next paragraph.

Equation (16) follows by partitioning one consecutive set of factors into
two consecutive blocks. Coefficient extraction from a product gives (17).
No term vanishes as a formal polynomial for a nonempty split.

For the parity split, the even nodes in \(a,a+1,\ldots,a+2m\) are

\[
 a+2j=2(a/2+j),\qquad 0\le j\le m,
\]

and the odd nodes are

\[
 a+2j+1=2((a+1)/2+j),\qquad 0\le j<m.
\]

Replacing \(t\) by \(2t\) gives (18). For \(2m+1\), both parity classes
have \(m+1\) nodes, which gives (19). The two factors have different affine
shifts. Recursing literally therefore evaluates two distinct children at
each balanced level. Its recurrence is \(T(L)=2T(L/2)+O(1)\), before the
coefficient-convolution work is charged, and hence has linear leaf count.
This is an accounting statement for this recursion, not a lower bound for a
different representation.

## 4. The unavoidable nonunit in monotone divided-power composition

The forward differences commute, and

\[
 \Delta^m\Delta^n=\Delta^{m+n}.
\]

Therefore

\[
 \mathcal D_m\mathcal D_n
 =\frac{\Delta^{m+n}}{m!n!}
 =\binom{m+n}{m}\frac{\Delta^{m+n}}{(m+n)!},
\]

which proves (20).

Now take a monotone binary addition chain from one to \(B\), and let \(k\)
be its first generated index at least \(p\). Its parent indices \(m,n\) are
positive and below \(p\), while

\[
 p\le k=m+n\le B<q<2p.
\]

Thus

\[
 v_p(k!)=1,
 \qquad v_p(m!)=v_p(n!)=0,
\]

and

\[
 v_q(k!)=v_q(m!)=v_q(n!)=0.
\]

It follows that

\[
 v_p\binom{k}{m}=1,
 \qquad v_q\binom{k}{m}=0,
\]

which proves (21). For a finite-arity composition with positive inputs
\(m_1,\ldots,m_r<p\) and first-crossing sum \(k\), the same valuation
calculation applied to

\[
 \binom{k}{m_1,\ldots,m_r}=\frac{k!}{m_1!\cdots m_r!}
\]

gives the stated extension.

On the P230 branch, \(B!\) contains \(p\) exactly once and no \(q\), while
\(q\mid F_B(a)\). Hence \(N\mid B!F_B(a)\), which proves (22). A
fraction-free implementation of the displayed operator product preserves
that raw multiple; it does not by itself recover the normalized residue.

## 5. Coefficients and universal interval content

Expand the monomial before applying the difference operator:

\[
 (X+a)^{2B}=\sum_{k=0}^{2B}\binom{2B}{k}a^kX^{2B-k}.
\]

The standard normalized monomial difference is

\[
 \frac{\Delta^BX^m|_{X=0}}{B!}
 =\left\{\begin{matrix}m\\B\end{matrix}\right\}.
\]

It vanishes for \(m<B\). Applying it term by term proves (23), including
(24).

Fix a prime \(r\) with \(B+1<r<2B\). The \(B+1\) nodes
\(a,a+1,\ldots,a+B\) are distinct modulo \(r\). Let \(E\) be this set in
\(\mathbb F_r\), and let \(C=\mathbb F_r\setminus E\). Then

\[
 |C|=r-B-1<B.
\]

The full-field product identity gives

\[
 \prod_{x\in E}(1-xt)^{-1}
 =\frac{\prod_{c\in C}(1-ct)}{1-t^{r-1}}.
\tag{36}
\]

The numerator degree is below \(B\), and \(r-1>B\). Thus the coefficient
of \(t^B\) in (36) is zero. This proves (26) for every residue \(a\pmod r\).

The polynomial \(F_B(a)\bmod r\) has degree at most \(B<r\) and vanishes
at all \(r\) field elements. It is therefore the zero polynomial. Every
integer coefficient is divisible by \(r\). Distinct primes in (25) are
coprime, so their product divides the content. This proves (27).

On the unresolved branch, (1) gives \(q>B+1\) and \(q<2B\), so \(q\) is
one factor of \(P_B\). The smaller prime \(p<B\) is not. Hence
\(\gcd(P_B,N)=q\).

For the central binomial coefficient, \(B=p+s\) and \(2s<p\). Legendre's
formula gives

\[
 v_p\binom{2B}{B}
 =\left\lfloor\frac{2B}{p}\right\rfloor
  -2\left\lfloor\frac Bp\right\rfloor
 =2-2=0,
\]

because \(2B=2p+2s<3p\). Also \(B<q<2B<2q\), so

\[
 v_q\binom{2B}{B}=1.
\]

There are no omitted higher terms in Legendre's formula. The primes are
odd, \(2B<3p\le p^2\), and \(2B<2q<q^2\).

This proves (28). Since the content divides every coefficient, it divides
the leading coefficient (24). Equation (27) puts \(q\) in the content,
while (28) excludes \(p\) and limits \(q\) to one copy. This proves (29).

Division by \(P_B\) is coefficientwise exact. Its quotient has leading
coefficient \(\binom{2B}{B}/P_B\), which is nonzero modulo \(q\). The same
is true after division by the full content, by the definition of content
and, more specifically, by the exact \(q\)-valuation just proved. Both
quotients are nonzero polynomials modulo \(q\), so neither vanishes for all
shifts. This proves the quotient boundary without asserting that either
quotient is easy to evaluate.

## 6. What the first \(N\)-adic quotient contains

The inequalities \(p<B<q<2p\) imply

\[
 B!=pU,\qquad \gcd(U,N)=1.
\]

Equation (27) and the inclusion of \(q\) in its interval show that
\(F_B(a)=qV_B(a)\) coefficientwise over \(\mathbb Z[a]\). Substitution
gives (31).

Since \(D_B(a)\) is an exact multiple of \(N\), its canonical residue
modulo \(N^2\) is also a multiple of \(N\). Dividing that residue by \(N\)
gives the canonical residue of \(UV_B(a)\) modulo \(N\). This proves (32).

Modulo \(p\), multiplication by \(q^{-1}\) gives

\[
 V_B(a)\equiv q^{-1}F_B(a)\pmod p.
\]

P230 proves that the induced residue function is represented by a nonzero
polynomial of degree \(s+1\). Thus it is not universally zero modulo \(p\).
Modulo \(q\), the leading
coefficient of \(V_B=F_B/q\) is

\[
 \frac1q\binom{2B}{B},
\]

which is a \(q\)-unit by (28). Thus \(V_B\) is not universally zero modulo
\(q\) either. Its degree is \(B<q\), so it has at most \(B\) roots there.
Each field has at least one residue on which \(V_B\) is nonzero. The Chinese
remainder theorem combines such residues into an
integer shift \(a\) for which

\[
 \gcd(UV_B(a),N)=1.
\]

Therefore the direct gcd after (32) has no all-shift factor guarantee. This
does not analyze extra information that a different decoder might retain
from still higher lifts.

For the literal faithful modulus, write \(F_B(a)=r+kN\) with
\(0\le r<N\). Then

\[
 D_B(a)=B!r+kNB!,
\]

so the canonical residue modulo \(NB!\) is \(B!r\). Exact division by
\(B!\) returns \(r=F_B(a)\bmod N\). The standard factorial bounds give
\(\log(B!)=\Theta(B\log B)\), so merely writing this modulus has
characteristic size. Finally, \(B!\) contains \(p\) exactly once and no
\(q\), hence \(\gcd(B!\bmod N,N)=p\). These facts classify only the
literal denominator-and-modulus route.

## 7. Why no finite synthesis run follows

The exact state costs now occur before any empirical question:

- (9) and (10) give a reduced denominator and canonical linear state of
  size \(B+1\);
- (14), (16), (18), and (19) require a full translation vector, a central
  convolution, or two distinct recursive children;
- (20) reaches a nonunit structure constant at the first hidden-prime
  crossing;
- fraction-free evaluation gives the zero in (22);
- (24)--(29) move the universal signal into the already factor-bearing
  interval-primorial or central-binomial content; and
- (32) removes that guaranteed signal instead of recovering it.

A bounded finite search over these displayed identities would test only
instances of an already classified representation. It would not test an
operation with a path to numerical-QP evaluation. This justifies the scoped
no-search disposition.

The distinct-pole proof is linear and canonical. It does not apply to a
nonlinear one-child map, an adaptive state, a relation only on the diagonal
\(d=B\), or a matrix whose entries already encode the hard endpoint. No
such candidate is known here, but absence of a candidate is not an
impossibility theorem.
