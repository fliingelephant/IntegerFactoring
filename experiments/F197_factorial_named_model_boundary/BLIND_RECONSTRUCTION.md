# F197 blind reconstruction

Statement SHA-256:
`774ce7c5496c28942d6cb11814b95cc2487ae10477127d40d8609332090e49c3`.

## Verdict

**PASS.** Every internal deduction in the statement follows under its stated
scope. The Bostan--Gaudry--Schost and Costa--Harvey claims are used only as
the published algorithmic premises identified in the statement. They give
upper bounds for those named constructions. They do not give lower bounds
for other factorial, holonomic, arithmetic-circuit, residue-only, or
factoring algorithms.

## Preliminary size relations

From

\[
n=\lceil\log_2(N+1)\rceil
\]

and the integrality of \(N\),

\[
2^{n-1}\le N<2^n.
\tag{A1}
\]

Also, \(B=\lfloor\sqrt N\rfloor=\Theta(\sqrt N)\). Consequently,

\[
B=2^{\Theta(n)},\qquad \sqrt B=2^{\Theta(n)},
\qquad \log B=\Theta(n).
\tag{A2}
\]

The floor in the definition of \(B\) changes only constant factors here.

## 1. Balance, valuations, and the product \(D\)

Because \(p<q\),

\[
p<\sqrt{pq}<q.
\]

The left strict inequality and the integrality of \(p\) give \(p\le B\),
while the right inequality gives \(B<q\). Moreover, \(q<2p\) gives

\[
B\le\sqrt{pq}<\sqrt2\,p<2p.
\tag{A3}
\]

Thus the only multiple of \(p\) in \(1,\ldots,B\) is \(p\). Since
\(p\ge3\) and \(B<2p<p^2\), Legendre's valuation formula gives

\[
v_p(B!)=1.
\]

There is no multiple of \(q\) in the same interval, so \(v_q(B!)=0\).
As \(N=pq\) is squarefree,

\[
\gcd(F,N)=p,
\qquad
\gcd(F,N^2)=p.
\tag{A4}
\]

The product identity follows directly from the binomial coefficient:

\[
\binom{N-1}{B}
=\frac{(N-1)(N-2)\cdots(N-B)}{B!},
\]

hence

\[
D=F\binom{N-1}{B}.
\tag{A5}
\]

The valuations of \(D\) need a separate check; the identity alone would not
exclude extra \(p\)-factors. For \(r\in\{p,q\}\),

\[
r\mid N-j \quad\Longleftrightarrow\quad r\mid j.
\tag{A6}
\]

There is no qualifying \(j\) for \(r=q\), because \(B<q\). For \(r=p\),
the sole qualifying index is \(j=p\), and

\[
N-p=p(q-1).
\]

Distinct odd primes with \(p<q\) satisfy \(q\ge p+2\). Therefore
\(p<q-1<2p\), so \(p\nmid q-1\). It follows that

\[
v_p(D)=1,qquad v_q(D)=0,
\]

and hence

\[
\gcd(D,N)=p,
\qquad
\gcd(D,N^2)=p.
\tag{A7}
\]

For any integer \(x\) and modulus \(M\), replacing \(x\) by its canonical
residue modulo \(M\) does not change \(\gcd(x,M)\). Thus the exact value of
\(F\) or \(D\), its canonical residue modulo \(N\), or its canonical
residue modulo \(N^2\), makes the corresponding factor-bearing gcd
available before the exact quotient \(D/F\) is formed. This inference is
specific to routes that materialize one of those values.

## 2. Explicit dense one-width blocks

The dense coefficient vector of the degree-\(u\) polynomial

\[
P_u(X)=\prod_{j=1}^u(X+j)
\]

has \(u+1\) nonzero entries. Even if one fixed position is discarded from
the count, the explicit representation has at least \(u\) coefficient
positions. Blocks of width at most \(u\) require at least
\(\lceil B/u\rceil\) consecutive block values to cover \(1,\ldots,B\).
The stipulated representation therefore materializes at least

\[
u+\left\lceil\frac Bu\right\rceil
\ge u+\frac Bu
\ge 2\sqrt B,
\tag{A8}
\]

where the last inequality is AM--GM. A sequential explicit
materialization must touch at least this many positions before any cost for
forming or evaluating the polynomial is added. By (A2), this count is
exponential in \(n\). The argument concerns only this dense
coefficient-and-block-value representation; it says nothing about a
compressed representation or an arithmetic circuit.

## 3. Scale of the named published algorithms

The recurrence

\[
U_0=1,\qquad U_k=kU_{k-1}
\]

is the scalar first-order holonomic presentation of the factorial
sequence. Grant the stated Bostan--Gaudry--Schost premise: at length \(L\),
their baby-step/giant-step construction uses

\[
O\!\left(\mathsf M_R(\sqrt L)\log L\right)
\]

ring operations, with the stated refinements under their own hypotheses.
For \(R=\mathbb Z/N\mathbb Z\), fast polynomial and integer arithmetic turn
this displayed bound at \(L=B\) into

\[
B^{1/2+o(1)}\operatorname{poly}(n)
\tag{A9}
\]

bit operations. The factor \(\log B=O(n)\) is absorbed by the polynomial
factor. Since \(B=\Theta(N^{1/2})\), and since
\(\operatorname{poly}(n)=N^{o(1)}\), (A9) has scale

\[
N^{1/4+o(1)}=2^{\Theta(n)}.
\tag{A10}
\]

Thus this published guarantee is exponential, rather than numerical
quasipolynomial, as a function of the input bit length \(n\). Granting the
stated Costa--Harvey premise places the construction in the required
multitape bit model. Dividing a complete factorization bound by
\(\sqrt{\log\log N}=N^{o(1)}\) does not change its power of \(N\).

These are evaluations of named published upper bounds. An exponential
upper bound is not a lower bound on the best possible implementation, and
it cannot exclude a different holonomic or factorial algorithm.

## 4. Nonunit division modulo \(N\) and \(N^2\)

Write \(F=pU\). The valuations from Section 1 imply

\[
\gcd(U,N)=1.
\tag{A11}
\]

For arbitrary integers \(x,y\), put \(\delta=x-y\). Then

\[
\begin{aligned}
Fx\equiv Fy\pmod N
&\Longleftrightarrow pq\mid pU\delta\\
&\Longleftrightarrow q\mid\delta,
\end{aligned}
\tag{A12}
\]

because \(U\) is a unit modulo \(q\). Hence multiplication by \(F\) modulo
\(N\) forgets exactly the \(p\)-component. Its kernel consists of the
\(p\) residue classes

\[
0,q,2q,\ldots,(p-1)q.
\]

Similarly,

\[
\begin{aligned}
Fx\equiv Fy\pmod {N^2}
&\Longleftrightarrow p^2q^2\mid pU\delta\\
&\Longleftrightarrow pq^2\mid\delta.
\end{aligned}
\tag{A13}
\]

Modulo \(p^2q^2\), there are exactly
\(p^2q^2/(pq^2)=p\) multiples of \(pq^2\), so this kernel also has size
\(p\). If \(0\le x,y<N\), then \(|x-y|<N=pq<pq^2\). Condition (A13) can
then hold only when \(x=y\), proving injectivity on the stated canonical
domain.

At neither modulus is \(F\) a unit, so ordinary inverse-based division by
\(F\) is unavailable. Furthermore, a materialized denominator residue
reveals \(p\) through (A4). Injectivity on the restricted domain does not
rule out a custom restricted-domain decoder, so no such lower bound
follows.

Now write

\[
F=NQ+R,qquad 0\le R<N.
\]

Euclid's identity gives

\[
\gcd(R,N)=\gcd(F,N)=p.
\tag{A14}
\]

In particular, \(R\ne0\). If \(Q=Nk+s\) with
\(s=Q\bmod N\in[0,N)\), then

\[
F=N^2k+Ns+R.
\]

The integer \(Ns+R\) lies in \([0,N^2)\). Therefore it is the canonical
residue \(a_2=F\bmod N^2\), and its exact base-\(N\) digits are

\[
a_2=R+N(Q\bmod N),
\quad
a_2\bmod N=R,
\quad
\left\lfloor\frac{a_2}{N}\right\rfloor=Q\bmod N.
\tag{A15}
\]

The high digit is a quotient digit, but the low digit already has gcd
\(p\) with \(N\).

## 5. Exact-output size and the quotient-residue gate

For all sufficiently large \(B\), elementary product bounds give

\[
(B/2)^{\lfloor B/2\rfloor}\le B!\le B^B.
\]

Thus

\[
\log_2 F=\Theta(B\log B).
\tag{A16}
\]

Also, \(B\le\sqrt N\le N/2\) for the relevant nontrivial inputs. Hence
every factor of \(D\) lies between \(N/2\) and \(N\), and

\[
(N/2)^B\le D<N^B,
\qquad
\log_2 D=\Theta(B\log N)=\Theta(B\log B).
\tag{A17}
\]

Finally, \(F/N\) tends to infinity. Outside finitely many small inputs,
\(F/N\ge2\), and therefore

\[
\frac{F}{2N}\le Q=\left\lfloor\frac FN\right\rfloor\le\frac FN.
\]

Since \(\log N=\Theta(\log B)\), this yields

\[
\log_2 Q=\Theta(B\log B).
\tag{A18}
\]

By (A2), the bit lengths in (A16)--(A18) are
\(2^{\Theta(n)}\). A sequential multitape algorithm needs at least one
step per output bit, so explicitly materializing any one of \(F,D,Q\)
takes exponential time. This output argument does not apply to a short
residue.

### Polynomial-time computation of \(F\bmod 2^n\)

The valuation case split is essential. Compute

\[
s=v_2(B!)=\sum_{k\ge1}\left\lfloor\frac{B}{2^k}\right\rfloor.
\tag{A19}
\]

There are only \(O(\log B)=O(n)\) nonzero terms, and \(B\) itself is
computable by integer square root in polynomial bit time.

If \(s\ge n\), then \(2^n\mid F\), so

\[
f_2=F\bmod2^n=0.
\]

If \(s<n\), then (A19) gives

\[
\left\lfloor\frac B2\right\rfloor\le s<n,
\]

so \(B\le2n-1\). In this case, multiply the at most \(2n-1\) factors
\(1,\ldots,B\), reducing modulo \(2^n\) after each multiplication. This
uses polynomially many operations on \(n\)-bit integers. Both cases are
therefore deterministic polynomial time.

### Recovery from \(Q\bmod2^n\)

Let \(Q_2=Q\bmod2^n\). From \(F=NQ+R\),

\[
f_2-NQ_2\equiv R\pmod{2^n}.
\tag{A20}
\]

Equation (A1) and (A14) give

\[
0<R<N<2^n.
\]

Therefore the canonical residue of the left side of (A20) is the exact
integer \(R\), not merely a congruence class. Computing its gcd with \(N\)
returns \(p\). Thus an algorithm for the single \(n\)-bit value \(Q_2\),
together with polynomial-time overhead, is a sufficient factoring
primitive.

For the equivalent lift, write \(Q=2^nk+Q_2\). Then

\[
F=(N2^n)k+NQ_2+R.
\]

Because \(0\le Q_2<2^n\) and \(0<R<N\),

\[
0<NQ_2+R<N2^n.
\]

Hence, for the canonical residue \(a=F\bmod(N2^n)\),

\[
a=R+NQ_2,
\qquad
\left\lfloor\frac aN\right\rfloor=Q_2.
\tag{A21}
\]

This proves sufficiency only. It does not construct \(Q_2\) from a factor
of \(N\), and it does not prove that factoring implies a numerical-QP
algorithm for \(Q_2\).

## 6. One-child recurrence

Let the per-level quasipolynomial term have a monotone envelope

\[
q(k)\le 2^{C(\log(k+2))^c}
\]

for fixed constants \(C,c\). Unrolling a one-child recurrence gives

\[
\begin{aligned}
T(m)
&\le T(0)+\sum_{k=1}^m q(k)\\
&\le T(0)+m\,2^{C(\log(m+2))^c},
\end{aligned}
\tag{A22}
\]

which is quasipolynomial in \(m\). A fixed-ratio decrease is therefore not
needed for one surviving chain.

This recurrence fact does not remove work already present at the root of a
named construction. The explicit dense block representation has the root
position count (A8), and the named published BGS/Costa--Harvey guarantees
have the root scale (A10). Conversely, (A22) leaves open a different
one-child method whose per-node primitive is quasipolynomial.

## Strict claim audit

| Claim | Result | Reason |
|---|---:|---|
| Factorial valuations and gcds | PASS | Exactly one \(p\)-factor and no \(q\)-factor occur. |
| Product \(D\) and its gcds | PASS | The only \(p\)-divisible term is \(N-p\), with valuation one. |
| Explicit dense block balance | PASS | The stipulated positions total at least \(2\sqrt B\). |
| Named published upper-bound scale | PASS | Substitution gives \(N^{1/4+o(1)}\), used only as an upper bound. |
| Division kernels modulo \(N,N^2\) | PASS | Their defining congruences give kernels of size \(p\). |
| Base-\(N\) lift digits | PASS | Canonical-range bounds make both digits exact. |
| Exact-output sizes | PASS | Each relevant bit length is \(\Theta(B\log B)=2^{\Theta(n)}\). |
| Computation of \(F\bmod2^n\) | PASS | If the 2-adic valuation is small, then \(B<2n\); otherwise the residue is zero. |
| Quotient-bit recovery | PASS | The recovered canonical residue is the exact \(R\). |
| Sufficiency-only scope | PASS | No converse reduction or general lower bound is inferred. |
| One-child recurrence | PASS | A sum of \(m\) quasipolynomial terms is quasipolynomial. |

