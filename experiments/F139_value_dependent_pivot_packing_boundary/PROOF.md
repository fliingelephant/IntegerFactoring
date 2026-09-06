# F139 proof — value-dependent pivot packing boundary

## 1. Canonical anchored values

Let \(A=A_\ell\). Since \(\ell\le B\) and \(q<N/B\),

\[
1\le \ell q<N.
\]

Also \(0\le A<\ell\), so

\[
0<w+NA<N+N(\ell-1)=N\ell.
\]

Hence \(z_\ell=(w+NA)/\ell\) is an integer in
\(\{1,\ldots,N-1\}\). From \(qw\equiv1\pmod N\),

\[
(\ell q)z_\ell=q(w+NA)\equiv1\pmod N.
\]

Thus \(z_\ell=\iota_N(\ell q)\), and

\[
q(w+NA)=qw+qNA=1+(k+qA)N.
\]

## 2. Simultaneous preservation

Fix \(r\in\mathcal R_B(q)\). Since \(q\) is a unit modulo \(N\),
\(r\nmid N\). Therefore

\[
w+NA\equiv0\pmod r
\]

has exactly one residue class \(A\pmod r\). Every digit in \(D\) lies in
\([1,B-1]\), and \(r>B\). Thus at most one digit in \(D\) can have
positive \(r\)-valuation in \(H_A\). All other digits have valuation zero,
which is even. Marking the possible exceptional digit bad even when its
positive valuation happens to be even is conservative.

Take the union of these exceptional digit sets over
\(r\in\mathcal R_B(q)\). Its size is at most
\(|\mathcal R_B(q)|\). Every digit outside the union is common-good. This
proves the first bound.

The distinct-prime product

\[
\prod_{r\in\mathcal R_B(q)}r
\]

divides the squarefree kernel of \(q\), so it is at most \(q\). Every
factor is strictly larger than \(B\). Hence

\[
B^{|\mathcal R_B(q)|}<q,
\]

which gives

\[
|\mathcal R_B(q)|<\frac{\log q}{\log B}.
\]

## 3. Global deduplication

Let \(r_1,r_2\) be globally private in distinct old columns
\(C_1,C_2\). A common-good value \(V_A=qH_A\) has odd valuation in both
rows. If it equaled an old exact value \(C\), then \(C\) would contain both
rows. Global privacy forces \(C=C_1\) from row \(r_1\) and \(C=C_2\) from
row \(r_2\), contradicting \(C_1\ne C_2\). Thus \(V_A\) is new.

For \(A\ne A'\),

\[
V_A-V_{A'}=qN(A-A')\ne0,
\]

so different digits give different exact values.

For the factor-free corollary, a nonsquare \(B\)-rough block contains at
least one prime larger than \(B\) to odd valuation. Pairwise-coprime basis
blocks give different hidden primes. Since the block parity row is globally
degree one, every hidden prime with odd internal valuation is also globally
private to that owner. The product word \(q\) contains all these primes to
odd valuation. The preceding argument applies.

Privacy only in a peeled residual is insufficient. Peeling deletes columns,
not their permanent exact values. A row can occur in a deleted old column
and become degree one later. Such a row does not prevent a later generated
integer from duplicating the deleted value.

## 4. Public packing cost

The product of all primes at most \(B\) has \(O(B\log B)\) bits by the
elementary bound that it is at most \(B^B\). It and the list
of its prime factors are computable deterministically in time polynomial in
\(B\). Complete gcd refinement against this product splits every public
small-prime part from the old factor-free blocks. Exact square tests discard
residual blocks that have no odd prime row.

The explicit parity matrix identifies globally degree-one rows and their
owners. Replacing several candidates of one owner by its smallest candidate
cannot reduce the number of owners that fit under the product limit. After
this replacement, the product of the \(s\) smallest blocks is no larger than
the product of any \(s\) listed blocks. Therefore the longest prefix with
\(Bq<N\) has maximum cardinality.

The ledger has quasipolynomial length. The scan uses sorting and a linear
number of multiplications of \(O(n)\)-bit integers before the product limit
is reached. Together with the known polynomial-time gcd-free refinement,
the packed base inverse and sign screens, and the explicit anchor scan, this
has quasipolynomial cost in \(n\). Nothing in this argument gives a lower
bound on the returned prefix length.

## 5. Multi-pivot splice law

Let \(\alpha_i\) be the coefficient of owner column \(v_i\), let
\(\beta_j\) be the coefficient of new column \(u_j\), and let \(\gamma\)
contain the coefficients of \(W\). Put

\[
s=\sum_j\beta_j.
\]

In private row \(p_i\), the dependency equation is

\[
\alpha_i+s=0.
\]

Thus \(\alpha_i=s\) for every \(i\). Delete the pivot rows. The remaining
dependency equation is

\[
\widehat W\gamma
+s\sum_i\widehat v_i
+\sum_j\beta_j\widehat u_j=0.
\]

Since \(s=\sum_j\beta_j\), this is equivalent to

\[
\sum_j\beta_j
\left(\widehat u_j+\sum_i\widehat v_i\right)
\in\operatorname{colspan}(\widehat W).
\]

Conversely, any such membership supplies \(\gamma\); setting every
\(\alpha_i=s\) reconstructs a full dependency. If the old columns are
independent, a new dependency must have \(\beta\ne0\). This proves the exact
criterion.

## 6. Abstract peelable incidence system

In the stated abstract matrix, row \(h_j\) occurs only in column \(u_j\).
Any kernel vector therefore has coefficient zero on every \(u_j\). Row
\(p_i\) then forces the coefficient of \(v_i\) to be zero. The columns are
independent.

Degree-one peeling first removes all \(u_j\) through their \(h_j\) rows.
It then removes every \(v_i\) through its \(p_i\) row. Every new column had
all old pivot rows before peeling, so simultaneous preservation and high old
row degree do not alter this conclusion.

## 7. The \(N=989\) certificate

The registered Sage verifier checks the complete arithmetic. The identities
can also be read directly:

\[
989=23\cdot43,
\]

\[
2\cdot495=990=1+989,
\qquad
16\cdot680=10880=1+11\cdot989,
\]

and

\[
187\cdot238=44506=1+45\cdot989.
\]

The packed endpoint sign screens are both one. For
\(\ell=1,2,3,4,5\), the equations

\[
238+989A_\ell\equiv0\pmod\ell
\]

give

\[
(A_1,A_2,A_3,A_4,A_5)=(0,0,1,2,3).
\]

The endpoint divisions are

\[
238,
\quad
\frac{238}{2}=119,
\quad
\frac{238+989}{3}=409,
\quad
\frac{238+2\cdot989}{4}=554,
\quad
\frac{238+3\cdot989}{5}=641.
\]

The corresponding left endpoints are

\[
187,374,561,748,935.
\]

All endpoints lie strictly between zero and \(989\). Multiplication gives
the exact values and carries in the statement. Their factorizations give the
displayed parity matrix.

Rows \(7,3,277,641\) first remove columns \(V_0,V_1,V_2,V_3\).
After those removals, rows \(11,17\) remove columns
\(P_N(2),P_N(16)\). This proves full column rank and gives a complete
peeling order. The verifier also checks the packed base screen, every
eligible integer-anchor position and sign screen, selected-ledger
exact-value deduplication, and the common-good parity of rows \(11\) and
\(17\) in every nonzero-digit column.
