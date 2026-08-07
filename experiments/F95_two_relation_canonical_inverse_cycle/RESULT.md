# F95 — a two-relation canonical-inverse cycle at the stable modulus 2773

**Status:** candidate finite witness, self-checked. The computation found an
exact certificate. It has not received the hostile-audit and independent
reconstruction cadence. It is not theorem evidence or a factoring
algorithm.

## 1. Result

The preferred stable semiprime already contains the requested cycle:

\[
N=2773=47\cdot59.
\]

It is a P98 stable-core witness because

\[
\gcd(47-1,59-1)=2,\qquad
A=23,\qquad B=29,\qquad
\gcd(AB,N-1)=1.
\]

Two distinct canonical-inverse relation values are

\[
\begin{aligned}
P_1
&=3\cdot1849
=5547
=1+2N
=3\cdot43^2,\\
P_2
&=842\cdot2526
=2{,}126{,}892
=1+767N
=2^2\cdot3\cdot421^2.
\end{aligned}
\tag{1}
\]

All four endpoints satisfy

\[
1<g_i,w_i<N.
\]

Because each product is one modulo \(N\), and each displayed \(w_i\) lies
in \(\{1,\ldots,N-1\}\), \(w_i\) is the least positive inverse of \(g_i\).

The two columns are individually nonclosing modulo \(2\). After the first
is retained, the second closes. Their induced exact square root gives both
factors of \(N\).

## 2. Exact gcd-free column certificate

A public gcd-free refinement does not need the prime factorizations. First,

\[
\gcd(P_1,P_2)=3.
\]

Exact division and square tests give

\[
\frac{P_1}{3}=1849=43^2,
\qquad
\frac{P_2}{3}=708{,}964=842^2.
\]

Taking the two public exact square roots gives the pairwise-coprime basis

\[
(3,43,842).
\]

The two integer exponent columns are

\[
\begin{pmatrix}1\\2\\0\end{pmatrix},
\qquad
\begin{pmatrix}1\\0\\2\end{pmatrix}.
\]

Modulo \(2\), these are the same nonzero column

\[
\begin{pmatrix}1\\0\\0\end{pmatrix}.
\]

This is the complete public square-normalized certificate. It uses one gcd,
two exact divisions, and two exact square-root tests. It does not factor
\(842\).

For an optional fully expanded certificate, factor the small displayed
values further to the pairwise-coprime prime basis

\[
(2,3,43,421).
\]

Its two integer exponent columns are

\[
u_1=
\begin{pmatrix}
0\\1\\2\\0
\end{pmatrix},
\qquad
u_2=
\begin{pmatrix}
2\\1\\0\\2
\end{pmatrix}.
\tag{2}
\]

Modulo \(2\),

\[
\bar u_1=\bar u_2=
\begin{pmatrix}
0\\1\\0\\0
\end{pmatrix}
\ne0.
\tag{3}
\]

With no old relation, either column alone increases column rank from zero
to one. Its one-column kernel is zero, so it is individually nonclosing.

After retaining \(u_1\), the second column lies in its span. The two-column
matrix still has rank one, while its kernel has dimension one:

\[
\ker[\bar u_1\mid\bar u_2]
=
\left\langle
\begin{pmatrix}1\\1\end{pmatrix}
\right\rangle.
\tag{4}
\]

This is the requested two-relation 2-saturation closure.

## 3. The induced root factors

The kernel vector in (4) gives

\[
\begin{aligned}
R
&=\sqrt{P_1P_2}\\
&=2\cdot3\cdot43\cdot421\\
&=108{,}618.
\end{aligned}
\tag{5}
\]

Thus

\[
R^2=P_1P_2
\qquad\text{and}\qquad
R^2\equiv1\pmod N.
\]

Its canonical residue is

\[
R\equiv471\pmod{2773}.
\]

The public gcd tests give

\[
\gcd(R-1,N)=47,
\qquad
\gcd(R+1,N)=59.
\tag{6}
\]

Both outputs are prime and multiply to \(2773\). The induced root is
therefore a nontrivial square root of one and yields a proper factor.

## 4. Deleting the first relation loses the closure

If \(u_1\) is discarded, the remaining column is

\[
\bar u_2=(0,1,0,0)^T\ne0.
\]

Relative to the empty retained relation list, it is again nonclosing.
Therefore deleting the first relation loses exactly the earlier column
needed for the second closure. Retaining only abstract subgroup information
does not preserve this presentation event.

## 5. Exact finite search and minimality

The named source exhausts every \(g\) in

\[
2\le g\le2772.
\]

It uses only public gcds and canonical modular inverses. Exact relation
values are deduplicated, sorted by \((P,g,w)\), and tested in nested
lexicographic pair order.

The closure test used during search is factor-free with respect to the
relation values:

- \(P_i\) nonsquare means its parity column is nonzero;
- \(P_1P_2\) square means their complete prime-parity columns are equal; and
- the induced-root gcd publicly verifies usefulness.

The source found 634 unique values and tested 934 eligible pairs. The
displayed witness was the first successful pair. It has relation indices
1 and 306 in the declared sorted list. Hence it is the smallest witness
under the exact declared order for the full nontrivial residue range at
\(N=2773\).

The prime factorization of \(P_1,P_2\) in (1) was computed only after the
public square-product test found the pair. It is an extra certificate; it
was not a search oracle and is not needed for the public basis above.

## 6. Exact relation to a square-root collision

The first relation publicly gives

\[
3\cdot43^2\equiv1\pmod N.
\]

The second relation gives

\[
3\cdot842^2\equiv1\pmod N.
\]

Hence \(43\) and \(842\) are two square roots of the same unit. Their direct
comparison already gives

\[
\gcd(842-43,N)=47,
\qquad
\gcd(842+43,N)=59.
\]

Thus the two-column closure is an exact congruence-of-squares collision in
presentation form. The new fact is the existence of this literal
canonical-inverse witness on the stable test modulus. The witness does not
make the second square root easy to find.

## 7. What this establishes

This is a genuine positive mechanism witness:

\[
\text{first nonclosing relation}
\longrightarrow
\text{parity reuse}
\longrightarrow
\text{second relation closes}
\longrightarrow
\text{induced root factors}.
\]

It shows that amortized canonical-inverse relations can do more than repeat
one scalar gcd. The useful information is the shared relation parity and
the retained first column.

The finite search does not explain how to select \(g_2=842\) in work
polynomial in \(\log N\). Selecting it is exactly the missing second-root
problem in this certificate. The run enumerates a range of size \(N-2\).
It gives no all-input density, feedback-generation law, polynomial-time
relation selector, or complete factoring algorithm. The stable powered-core
obstruction is not contradicted: this witness uses unpowered exact integer
relations and a saturation root.

Full machine evidence and exact run bounds are in OUTPUT.json, RUN.log, and
RUN_MANIFEST.md.
