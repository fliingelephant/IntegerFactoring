# F203 blind reconstruction

## Audit basis and verdict

The SHA-256 digest of the statement, checked before it was opened, is

    10481fa918cffefe71eee3dee08ad23b7b837d685c899a23e5c03a2a74aa9b4f

This reconstruction uses only PROMPT.md and the frozen STATEMENT.md.

**Verdict.** The residue identities, all three sign cases, factor extraction,
Lambert-series identity, \(m=2\) specialization, quotient-child formulas,
positivity and coprimality claims, and exact coalescence criterion are correct.
The displayed recurrence

\[
\mathcal T(n)\leq \mathcal T(n-1)+\operatorname{QP}(n)
\]

is quasipolynomial. There is one necessary scope qualification: the fact that
there is at most one recursive call *per selector stage* does not by itself
show that a complete multi-stage factoring procedure has this recurrence. A
future construction must also show that the whole parent computation makes
only one recursive call along a nested chain, or must otherwise amortize or
reuse calls. The statement supplies no such construction and explicitly makes
no complete factoring claim. Likewise, equality of the two quotient children
defeats selection by comparing those children, but it is not a lower bound
against a new decoder that uses the factorization of the common child together
with \(N\). With these narrow readings, the self-contained mathematical claims
pass reconstruction. The historical claims about P165 and P175 cannot be
checked from the permitted sources and are not used below.

Consequently, F203 does **not** meet the top-level success criterion in
PROMPT.md: it gives neither an evaluator for the displayed coefficient nor an
algorithm for unrestricted integer factorization.

## 1. Canonical residues and the balanced interval

Because \(p\) is odd and \(m\) is a power of two, \(p\), and hence its inverse
\(u\), is a unit modulo \(m\). Therefore

\[
r\equiv u^{-1}\equiv p\pmod m,
\qquad
c\equiv Nu\equiv pqp^{-1}\equiv q\pmod m.
\]

Their canonical representatives are odd and lie between \(1\) and \(m-1\).

Since \(p<q\),

\[
p<\sqrt{pq}<q.
\]

The square root is not an integer because \(p\ne q\), so
\(p\leq B<q\). It remains to check the strict lower endpoint in the definition
of the children. Since \(q<2p\) and \(q\) is an integer, \(q\leq2p-1\). For
the odd prime \(p\geq3\),

\[
(2p-2)^2-p(2p-1)=2p^2-7p+4>0;
\]

the case \(p=3\) gives \(1\), and for \(p\geq5\) positivity is immediate.
Thus \(\sqrt N<2p-2\), so \(B\leq2p-3\), and hence

\[
\left\lceil\frac B2\right\rceil\leq p-1<p.
\]

Therefore \(p\) lies in the stated interval. The congruence class \(r\bmod m\)
splits disjointly into the classes \(r\) and \(r+m\bmod 2m\), so exactly one
of \(J_+\) and \(J_-\) contains \(p\). If

\[
p\equiv r+am\pmod{2m},\qquad a\in\{0,1\},
\]

then

\[
\epsilon=w_{m,r}(p)=(-1)^a.
\]

## 2. Relation between the factor orientations

Let \(v\equiv r^{-1}\pmod{2m}\). Both \(v\) and \(q\) are odd. Using the bit
\(a\) above gives

\[
c_0\equiv Nv\equiv(r+am)qv
       \equiv q+amqv\equiv q+am\pmod{2m}.
\]

The last congruence uses \(mqv\equiv m\pmod{2m}\). Equivalently,

\[
q\equiv c_0+am\pmod{2m}.
\]

Reduction modulo \(m\) also shows \(c_0\equiv c\pmod m\). If \(c\ne r\),
then \(q\not\equiv r\pmod m\), and the definition gives
\(w_{m,r}(q)=0\).

Now suppose \(c=r\). There is a unique \(\ell\in\{0,1\}\) such that

\[
c_0\equiv r+\ell m\pmod{2m}.
\]

Then \(\lambda=(-1)^\ell\), while

\[
q\equiv r+(\ell+a)m\pmod{2m}
\]

with the coefficient of \(m\) read modulo \(2\). Therefore

\[
w_{m,r}(q)=(-1)^{\ell+a}=\lambda\epsilon.
\]

All quantities defining \(\lambda\) are public, so this proves the claimed
public sibling relation without revealing \(a\).

## 3. The selector and every sign case

The positive divisors of the distinct semiprime \(N\) are exactly
\(1,p,q,N\). After removing the two public terms,

\[
T=pw_{m,r}(p)+qw_{m,r}(q).
\]

The preceding section gives the exhaustive table

\[
\begin{array}{c|c|c}
\text{condition}&T&T/\epsilon\\ \hline
c\ne r&\epsilon p&p\\
c=r,\ \lambda=+1&\epsilon(p+q)&p+q\\
c=r,\ \lambda=-1&\epsilon(p-q)&p-q.
\end{array}
\]

The first two entries in the last column are positive. The third is negative
because \(p<q\). None is zero. It follows that

\[
\epsilon=\operatorname{sgn}(T)
\]

in the first two cases, and

\[
\epsilon=-\operatorname{sgn}(T)
\]

in the last case. This proves both the selector and all sign conventions.

## 4. Exact factor extraction and equivalence on the promise

If \(c\ne r\), then \(|T|=p\), so a nontrivial factor is already explicit.

If \(c=r\) and \(\lambda=+1\), put \(s=|T|=p+q\). Then

\[
s^2-4N=(q-p)^2,
\]

and, with \(h=\sqrt{s^2-4N}=q-p\),

\[
p=\frac{s-h}{2},\qquad q=\frac{s+h}{2}.
\]

If \(c=r\) and \(\lambda=-1\), put \(d=|T|=q-p\). Then

\[
d^2+4N=(p+q)^2.
\]

Thus \(s=\sqrt{T^2+4N}=p+q\), after which the same two formulas recover
\(p,q\).

The integers involved have \(O(n)\) bits: in particular, the coefficient and
\(T\) are bounded in magnitude by the sum of the four divisors. Integer square
root, multiplication, addition, and exact division on such integers all have
deterministic polynomial bit complexity. Thus an exact value of the
coefficient factors every instance of the stated promise in deterministic
polynomial time.

Conversely, after factoring a promised \(N\), its four divisors are known and
the four terms in \(S_{m,r}(N)\) can be evaluated directly using modular
reduction. This also has polynomial bit complexity. Hence the equivalence is
valid on the distinct-semiprime promise. It makes no assertion about the cost
of enumerating divisors of an unrestricted integer.

## 5. Lambert series and the \(m=2\) specialization

In the ring of formal power series,

\[
\frac{X^a}{1-X^a}=\sum_{k\geq1}X^{ak}.
\]

For a fixed coefficient \(X^N\), only the finitely many pairs with \(ak=N\)
contribute. Therefore

\[
\begin{aligned}
[X^N]\sum_{a\geq1}\frac{a w_{m,r}(a)X^a}{1-X^a}
 &=\sum_{a\mid N}a w_{m,r}(a)\\
 &=S_{m,r}(N).
\end{aligned}
\]

This is an exact formal identity. It is not an efficient coefficient
algorithm.

For \(m=2,r=1\), the three cases in the definition of the weight are exactly

\[
w_{2,1}(d)=
\begin{cases}
1,&d\equiv1\pmod4,\\
-1,&d\equiv3\pmod4,\\
0,&d\equiv0\pmod2,
\end{cases}
\]

so \(w_{2,1}=\chi_4\). For every distinct odd semiprime, write

\[
T=S_{2,1}(N)-1-N\chi_4(N).
\]

If \(N\equiv1\pmod4\), the factors have the same \(\chi_4\)-value and

\[
T=\chi_4(p)(p+q).
\]

If \(N\equiv3\pmod4\), they have opposite values and

\[
T=\chi_4(p)(p-q).
\]

Thus the sum or difference extraction in the preceding section factors \(N\).
This argument does not use balance; in the exceptional balanced case with
\(p=3\), where the earlier technical condition \(2m<p\) fails for \(m=2\),
the fixed-character factor-extraction identity still remains valid.

For comparison, the unweighted character sum is

\[
\sum_{d\mid N}\chi_4(d)
 =(1+\chi_4(p))(1+\chi_4(q)).
\]

When \(N\equiv3\pmod4\), this is zero for both possible assignments of the two
opposite character values to the smaller and larger factors. Hence that
unweighted statistic need not reveal the smaller factor's orientation. This
justifies “the factor \(d\) is essential” for this universal orientation
selector; it is not a claim that every conceivable method must use that exact
weight.

## 6. The first contracted quotient

Because \(N\equiv rc\pmod m\), \(K=(N-rc)/m\) is an integer. Also
\(1\leq r,c<m\), while \(p>2m\) and \(q>p\), so

\[
rc<m^2<4m^2<N.
\]

Thus \(K>0\). If \(m=2\), then \(r=c=1\) and

\[
K=\frac{N-1}{2}<\frac N2.
\]

If \(m\geq4\), then \(K<N/m\leq N/4<N/2\). Hence \(0<K<N/2\) in all
cases.

No prime factor of \(N\) divides \(K\). Indeed, if
\(\ell\in\{p,q\}\) divided \(K\), reduction of

\[
mK=N-rc
\]

modulo \(\ell\) would give \(\ell\mid rc\). But \(r,c\) are positive and
strictly smaller than \(m<\ell\), which is impossible because \(\ell\) is
prime. Thus \(\gcd(K,N)=1\).

If \(N\) has \(n\) bits, then \(K<N/2<2^{n-1}\), so \(K\) has at most
\(n-1\) bits. This proves the stated one-bit contraction.

## 7. Lift parity and the two \(K'\)-children

For suitable integers \(x,y\), write

\[
p=r+m(a+2x),\qquad q=c+m(b+2y).
\]

Expansion and division by \(m\) give

\[
K=c(a+2x)+r(b+2y)+m(a+2x)(b+2y).
\]

Since \(r,c\) are odd and \(m\) is even,

\[
\delta\equiv K\equiv a+b\pmod2.
\]

For bits, this is exactly \(b=a\mathbin{\mathsf{xor}}\delta\).

Now fix either candidate \(a\), define \(b\) by that public parity relation,
and put

\[
R_a=r+am,\qquad C_a=c+bm.
\]

Direct expansion gives

\[
\frac{N-R_aC_a}{2m}
 =\frac{K-ac-br-abm}{2}=K'_a.
\]

The numerator in the last expression is even, because modulo \(2\) it is

\[
\delta-a-b=0.
\]

Thus both candidate values are integers.

Moreover, \(1\leq R_a,C_a<2m<p<q\), and

\[
R_aC_a<(2m)^2<N.
\]

Consequently

\[
0<K'_a<\frac{N}{2m}.
\]

If a prime \(\ell\in\{p,q\}\) divided \(K'_a\), the identity

\[
2mK'_a=N-R_aC_a
\]

would imply \(\ell\mid R_aC_a\). Primality of \(\ell\) would then force it
to divide \(R_a\) or \(C_a\), impossible because both are positive and
smaller than \(\ell\). Hence \(\gcd(K'_a,N)=1\) for both candidates. For the
true bit, \(R_a\) and \(C_a\) are precisely the canonical residues of \(p\)
and \(q\) modulo \(2m\), so \(K'_a\) is exactly the quotient state at the
lifted modulus.

## 8. Separation and coalescence

Substitution of \(b=a\mathbin{\mathsf{xor}}\delta\) yields

\[
\begin{array}{c|c|c}
\delta&K'_0&K'_1\\ \hline
0&K/2&(K-r-c-m)/2\\
1&(K-r)/2&(K-c)/2.
\end{array}
\]

When \(\delta=0\), equality would require \(r+c+m=0\), impossible because
all three terms are positive. When \(\delta=1\), equality holds exactly when
\(r=c\). Therefore

\[
K'_0=K'_1\quad\Longleftrightarrow\quad \delta=1\text{ and }r=c.
\]

Here \(\delta=1\) says \(a\ne b\), so the factors occupy opposite classes
modulo \(2m\), while \(r=c\) says that they came from the same parent class
modulo \(m\). In that case the two candidate lifted residue products are the
same product with its two factors exchanged. The quotient construction is
therefore symmetric under exchanging which lift belongs to the smaller
factor.

At \(m=2\), the only canonical odd residue modulo \(m\) is \(1\), so
\(r=c=1\). If \(N\equiv3\pmod4\), then

\[
K=\frac{N-1}{2}\equiv1\pmod2,
\]

and the \(\delta=1\) row gives

\[
K'_0=K'_1=\frac{K-1}{2}=\frac{N-3}{4}.
\]

The bit \(a\) is the first nontrivial bit distinguishing \(p\equiv1\) from
\(p\equiv3\pmod4\). Since the two candidate child integers are identical,
their values, and their complete factorizations considered as candidate
labels, provide no direct comparison that selects \(a\). This proves exact
coalescence. It does not prove that an arbitrary algorithm given both \(N\)
and the factorization of the common integer cannot infer \(a\) by some new
adaptive relation; the statement correctly leaves that possibility open.

## 9. Recursion accounting and its exact scope

Let

\[
Q(n)=2^{C(\log_2(n+1))^k},\qquad C>0,\ k\geq1,
\]

and suppose an actual overall algorithm satisfies

\[
\mathcal T(n)\leq\mathcal T(n-1)+Q(n)
\]

above a fixed base size. Since \(Q\) is nondecreasing, iteration gives

\[
\mathcal T(n)\leq \mathcal T(n_0)+nQ(n).
\]

Writing \(L=\log_2(n+1)\geq1\), one has \(n\leq2^L\leq2^{L^k}\).
After absorbing the fixed base cost,

\[
\mathcal T(n)\leq2^{C'(\log_2(n+1))^k}
\]

for a fixed \(C'>C\). Thus the displayed one-child recurrence is numerical
QP, and a fixed-ratio size reduction is unnecessary; a one-bit reduction is
enough.

There is, however, a strict logical boundary. If a parent factorization needs
\(s(n)\) separate selector stages and each stage independently calls a
factorization routine on an \((n-1)\)-bit child, the resulting upper bound can
instead contain

\[
s(n)\mathcal T(n-1),
\]

which is not the displayed recurrence. Therefore “one recursive call per
stage” is not alone a global recursion proof. A future construction must show
that only one child call occurs for the whole parent computation, that the
stages form one shared nested chain, or that all additional calls are safely
amortized. F203 gives none of these, gives no rule selecting \(a\), and gives
no coefficient evaluator. Its valid recursion result is precisely the closure
of the displayed recurrence, not the existence of a factoring algorithm that
satisfies it.

## Final classification

- **Verified:** every self-contained algebraic identity and inequality in the
  statement, including all signs, extraction formulas, the \(m=2\) result,
  both quotient children, and exact coalescence.
- **Verified with narrow scope:** identical children cannot be distinguished
  by their child value or by treating their identical factorizations as two
  different candidate certificates. This gives no general adaptive lower
  bound.
- **Verified with necessary antecedent:** the displayed one-child recurrence
  is quasipolynomial if an overall algorithm actually satisfies it. Per-stage
  one-child behavior alone does not establish that antecedent.
- **Not independently checkable here:** the descriptive comparisons with P165
  and P175.
- **Not supplied:** a QP coefficient evaluator, a selector reduction, or an
  unrestricted classical Las Vegas QP factoring algorithm.
