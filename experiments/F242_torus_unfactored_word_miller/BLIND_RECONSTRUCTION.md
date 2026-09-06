# Blind reconstruction of the F242 statement

## Authentication and verdict

The SHA-256 digest of the supplied `STATEMENT.md` was checked before it was
read. It is

```text
e3364b88dbf11b4a1b53daeeaa629e6c22d97de58615a146a671c616ac2c7123
```

**Strict statement-only verdict: FAIL.** The torus sampler, the shifted-gcd
identity, the exact Miller law, the four-orientation average, and the stated
conditional complexity bound all reconstruct from first principles. The final
claim about the named “P158/F172 family” does not. The statement gives neither
the definition of that family nor the size relation between its two primes.
Those data are necessary to prove the claimed exponential residual size. This
is a self-containment failure, not a defect in the reconstructed boxed formulas.

The reconstruction below uses only the definitions in the supplied statement.

## 1. The local tori

Fix one of the primes \(\ell\in\{p,q\}\), and write

\[
 \epsilon_\ell=\left(\frac D\ell\right),\qquad
 B_\ell=\mathbb F_\ell[w]/(w^2-D).
\]

Since \(D\) is a unit and \(\ell\) is odd, \(B_\ell\) is an etale quadratic
algebra. Conjugation is \(\overline{x_0+x_1w}=x_0-x_1w\), and

\[
 \operatorname N(x_0+x_1w)=x_0^2-Dx_1^2.
\]

If \(\epsilon_\ell=+1\), choose \(t^2=D\) in \(\mathbb F_\ell\). The map

\[
 x_0+x_1w\longmapsto (x_0+t x_1,x_0-t x_1)
\]

identifies \(B_\ell\) with \(\mathbb F_\ell\times\mathbb F_\ell\), identifies
conjugation with swapping the two factors, and identifies the norm with their
product. Hence the norm-one group is

\[
 \{(z,z^{-1}):z\in\mathbb F_\ell^\times\}\cong
 \mathbb F_\ell^\times.
\]

It is cyclic of order \(\ell-1\).

If \(\epsilon_\ell=-1\), then \(B_\ell=\mathbb F_{\ell^2}\). Its unit group is
cyclic of order \(\ell^2-1\). The norm onto \(\mathbb F_\ell^\times\) is
surjective, so its kernel is cyclic of order

\[
 \frac{\ell^2-1}{\ell-1}=\ell+1.
\]

Thus in both cases the local norm-one torus \(T_\ell\) is cyclic of order

\[
 m_\ell=\ell-\epsilon_\ell.
\]

This also proves the claimed local torus orders.

## 2. The shifted-gcd identity and the powered kernels

The key integer identity has two symmetric forms:

\[
 N-J=q(p-\epsilon_p)+\epsilon_p(q-\epsilon_q)
     =q m_p+\epsilon_p m_q,
\]

\[
 N-J=p(q-\epsilon_q)+\epsilon_q(p-\epsilon_p)
     =p m_q+\epsilon_q m_p.
\]

Since each \(\epsilon_i\) is a unit in \(\mathbb Z\), these identities give

\[
 \gcd(m_p,N-J)=\gcd(m_p,m_q)=d,
 \qquad
 \gcd(m_q,N-J)=d.
\]

Write \(m_i=d s_i\). Then \(\gcd(s_p,s_q)=1\). Also, if
\(N-J=d t_i\), the preceding gcd equality gives \(\gcd(s_i,t_i)=1\).
Therefore, for \(E=(N-J)W\),

\[
 \gcd(m_i,E)
 =d\gcd(s_i,t_iW)
 =d\gcd(s_i,W).
\]

In a cyclic group of order \(m\), the kernel of \(x\mapsto x^E\) has
\(\gcd(m,E)\) elements. A uniform local torus point consequently satisfies

\[
 \Pr(U_i^E=1)
 =\frac{\gcd(m_i,E)}{m_i}
 =\frac{\gcd(s_i,W)}{s_i}
 =\frac1{r_i}=\alpha_i.
\]

This proves the shifted-gcd reduction and both exact probabilities in (5).
The algorithm never needs the factorization of \(W\), or even the values
\(r_i\). They occur only in the analysis.

## 3. Exact Hilbert-90 sampling

For a local unit \(z\in B_\ell^\times\), define

\[
 \phi_\ell(z)=z/\bar z.
\]

Its image has norm one. Its kernel is the group of conjugation-fixed units,
which is \(\mathbb F_\ell^\times\) and has \(\ell-1\) elements. In the split
case,

\[
 \frac{|B_\ell^\times|}{\ell-1}
 =\frac{(\ell-1)^2}{\ell-1}=\ell-1=|T_\ell|.
\]

In the nonsplit case,

\[
 \frac{|B_\ell^\times|}{\ell-1}
 =\frac{\ell^2-1}{\ell-1}=\ell+1=|T_\ell|.
\]

Thus \(\phi_\ell\) is onto in both cases, and every torus point has exactly
\(\ell-1\) preimages. A uniform local algebra unit therefore maps to a uniform
point of the full torus. In particular, the fibre calculation includes both
\(+1\) and \(-1\); it is not a Cayley chart with a missing point.

Now choose \((A,B)\) uniformly modulo \(N\), and put \(z=A+Bw\). By the
Chinese remainder theorem, its reductions \(z_p,z_q\) are independent and
uniform in their two local algebras. The condition

\[
 \nu=A^2-DB^2\in(\mathbb Z/N\mathbb Z)^\times
\]

is exactly the product of the two local conditions \(z_i\in B_i^\times\).
Conditioning on this product event preserves independence. The exact-fibre
result then shows that \(U_p,U_q\) are independent uniform points of their full
local tori.

For completeness, the local clean probability is also exact. If
\(\epsilon_\ell=+1\), the displayed split-algebra isomorphism is an invertible
linear change of the two coefficients. The norm is nonzero exactly when both
resulting coordinates are nonzero. Hence

\[
 \rho_\ell(+)=\left(1-\frac1\ell\right)^2.
\]

If \(\epsilon_\ell=-1\), the local algebra is a field, so the norm vanishes
only at zero. Hence

\[
 \rho_\ell(-)=1-\frac1{\ell^2}.
\]

For every odd \(\ell\), both quantities are at least \(4/9\). The two-prime
clean probability is therefore at least \(16/81\). Repeated independent
coefficient sampling needs at most \(81/16\) pairs in expectation before a
clean pair, unless a proper gcd ends the procedure sooner.

The coefficient screen is sound because a prime \(\ell\mid N\) divides
\(\gcd(N,A,B)\) exactly when both local coefficients vanish. The norm screen is
sound because \(\ell\mid\gcd(\nu,N)\) exactly when the local algebra element is
not a unit. Since \(N=pq\), a gcd equal to \(p\) or \(q\) is a verified proper
factor. A gcd equal to \(N\) is only a rejection. A clean norm gcd also implies
that the optional coefficient gcd is one.

## 4. Global torus arithmetic and identity screens

In \(A_D\),

\[
 (A-Bw)^{-1}=\frac{A+Bw}{A^2-DB^2}
\]

whenever the denominator is a unit. Thus the norm-gcd certification justifies
the only inversion, and

\[
 \frac{A+Bw}{A-Bw}
 =\frac{(A+Bw)^2}{A^2-DB^2}
 =\frac{A^2+DB^2}{\nu}+\frac{2AB}{\nu}w.
\]

This point has norm one. All later products use the polynomial quotient rule

\[
 (x_0+x_1w)(y_0+y_1w)
 =(x_0y_0+Dx_1y_1)+(x_0y_1+x_1y_0)w,
\]

so later multiplication, squaring, and powering need no division. Conjugation
negates the second coefficient, and the norm \(x_0^2-Dx_1^2\) is
multiplicative.

For any pair \(Y=(y_0,y_1)\) and either prime \(\ell\mid N\),

\[
 \ell\mid G_+(Y)\quad\Longleftrightarrow\quad Y_\ell=+1,
\]

\[
 \ell\mid G_-(Y)\quad\Longleftrightarrow\quad Y_\ell=-1.
\]

Thus either screen is proper exactly when its indicated sign occurs at one
local prime but not the other. Every returned value is therefore a verified
factor.

## 5. The conditional Miller mismatch law

Let

\[
 R_i=\{U_i^E=1\}.
\]

The local points are independent, and each event depends on only one point.
Conditional on \(R_p\cap R_q\), the two points remain independent and are
uniform in their respective power-map kernels.

Write \(m_i=2^{e_i}o_i\), \(E=2^v u\), with \(o_i,u\) odd. The kernel at
prime \(i\) has 2-primary order

\[
 2^{h_i},\qquad h_i=\min(e_i,v).
\]

Its odd-primary order divides \(u\). Raising a conditional kernel point to
the power \(u\) kills its odd-primary component and permutes its 2-primary
component, because \(u\) is odd. Hence

\[
 Y_{0,i}=U_i^u
\]

is uniform in a cyclic group of order \(2^{h_i}\), independently for the two
primes.

For a uniform element of \(C_{2^h}\), let \(T\) be the base-two logarithm of
its order. Thus \(T=0\) for the identity. The exact distribution is

\[
 \Pr(T=0)=2^{-h},
 \qquad
 \Pr(T=t)=\frac{2^{t-1}}{2^h}\quad(1\le t\le h),
\]

because \(C_{2^h}\) has \(2^{t-1}\) elements of exact order \(2^t\).

The sign pattern along repeated squaring is determined by \(T\). If \(T=0\),
the element is always \(+1\). If \(T\ge1\), the element is neither sign before
step \(T-1\), is \(-1\) at step \(T-1\), and is \(+1\) from step \(T\)
onward. The unique element of order two is the scalar \(-1\).

It follows that the two sign screens find no proper gcd at any step exactly
when the two order exponents are equal. If the exponents differ, the two local
sign patterns differ at some step, and one of the gcds is proper. Put
\(a=\min(h_p,h_q)\) and \(b=\max(h_p,h_q)\). The exact conditional failure
probability is

\[
\begin{aligned}
 \Pr(T_p=T_q)
 &=\frac{1}{2^{a+b}}
   \left(1+\sum_{t=1}^{a}2^{2t-2}\right)\\
 &=\frac{1}{2^{a+b}}
   \left(1+\frac{4^a-1}{3}\right)\\
 &=\frac{4^a+2}{3\,2^{a+b}}.
\end{aligned}
\]

The exact conditional success probability is therefore

\[
 \mu_{a,b}=1-\frac{4^a+2}{3\,2^{a+b}}.
\]

All \(m_i\) and \(N-J\) are even, so \(e_i,v,h_i\ge1\). Since \(b\ge a\),

\[
 \frac{4^a+2}{3\,2^{a+b}}
 \le \frac{4^a+2}{3\,4^a}
 \le\frac12.
\]

Hence \(\mu_{a,b}\ge1/2\).

The chain only needs the steps \(Y_0,Y_0^2,\ldots,Y_0^{2^v}=U^E\). Since
\(h_i\le v\), both local components have reached \(+1\) by the final step.

## 6. The exact powered success probability

The first \(+1\) screen on \(V=U^E\) has three cases.

1. Exactly one of \(R_p,R_q\) occurs. Then \(G_+(V)\) is a proper factor.
2. Neither event occurs. Then \(G_+(V)=1\), and the specified trial is null.
3. Both events occur. Then \(G_+(V)=N\), and the square chain succeeds with
   conditional probability \(\mu_{a,b}\).

Using independence and \(\Pr(R_i)=\alpha_i\) gives

\[
\begin{aligned}
 S
 &=\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p)
   +\mu_{a,b}\alpha_p\alpha_q\\
 &=\alpha_p+\alpha_q-(2-\mu_{a,b})\alpha_p\alpha_q.
\end{aligned}
\]

This proves (6) exactly for the specified powered phase. The phase
intentionally declares the “neither returns” case null; possible extra screens
outside that specification are not included in \(S\).

To prove (7), let

\[
 x=\max(\alpha_p,\alpha_q)=\frac1{\min(r_p,r_q)},
 \qquad y=\min(\alpha_p,\alpha_q).
\]

Since \(2-\mu_{a,b}\le3/2\),

\[
 S\ge x+y-\frac32xy.
\]

If \(x\le2/3\), the last expression is at least \(x\). If \(x\ge2/3\), then
\(y\le x\) and the coefficient of \(y\) is nonpositive, so

\[
 S\ge x+x-\frac32x^2\ge\frac x2,
\]

where the final difference is \(\tfrac32x(1-x)\ge0\). Thus in all cases

\[
 S\ge\frac1{2\min(r_p,r_q)}.
\]

If \(\min(r_p,r_q)\le R\), independent clean trials have success probability
at least \(1/(2R)\). Their stopping time is geometric, is finite almost surely,
and has expectation at most \(2R\). A sampler gcd can only replace a clean
powered attempt by an earlier verified factor. More explicitly, for each fixed
orientation, if a raw coefficient draw has probabilities \(f,c,r\) of a
proper-factor exit, a clean point, and a rejection, then repetition on the
rejection has total success probability

\[
 \frac{f+cS}{f+c}\ge S.
\]

This justifies the claim that sampler gcd exits cannot reduce success.

## 7. Four orientations

A uniform unit \(D\bmod N\) has independent uniform reductions in
\(\mathbb F_p^\times\) and \(\mathbb F_q^\times\). For an odd prime, exactly
half of the nonzero residues are squares. Therefore

\[
 (\epsilon_p,\epsilon_q)\in\{(+,+),(+,-),(-,+),(-,-)\}
\]

is uniform. The Jacobi symbol \(J=\epsilon_p\epsilon_q\) is computable without
knowing either factor. Within a fixed orientation, all local group orders,
sampler laws, and powered probabilities depend only on the two signs, not on
the particular unit \(D\).

The clean density does depend on the signs:

\[
 \rho_\ell(+)=\left(1-\frac1\ell\right)^2,
 \qquad
 \rho_\ell(-)=1-\frac1{\ell^2}.
\]

These values are unequal. If every failed coefficient pair caused \(D\) also
to be discarded, clean points would weight an orientation in proportion to
\(\rho_p(\epsilon_p)\rho_q(\epsilon_q)\), not by \(1/4\). Choosing \(D\) once
and resampling only \((A,B)\) preserves its original orientation. A proper gcd
still ends the procedure correctly.

Let \(R_\epsilon=\min(r_p,r_q)\) for orientation \(\epsilon\). For the ideal
experiment consisting of a uniform orientation and then an independent clean
point,

\[
 \Pr(\text{powered factor})
 =\frac14\sum_\epsilon S_\epsilon
 \ge\frac18\sum_\epsilon\frac1{R_\epsilon}
 \ge\frac1{8\min_\epsilon R_\epsilon}.
\]

Sampler factor exits preserve this as a lower bound for the full procedure.
This proves (9).

For orientation \((+,+)\), the residual source is formed from
\((p-1,q-1)\). For the other orientations, one or both entries are replaced by
\(p+1\) or \(q+1\). Thus the construction supplies four exact residual
interfaces and pays only the constant orientation factor. No argument above
shows that any one residual is small.

## 8. Bit complexity and exact scope

Let \(n\) be the bit length of \(N\), and let \(L\) be the bit length of
\(W\). The exponent \(E=(N-J)W\) has \(O(n+L)\) bits. Binary powering uses
\(O(n+L)\) ring multiplications. The square chain has at most
\(v_2(E)\le O(n+L)\) steps. Every ring coefficient remains reduced modulo
\(N\), so it has \(O(n)\) bits. Sampling, Jacobi symbols, modular arithmetic,
and gcds all have bit cost polynomial in their operand lengths. Random-bit
generation is also polynomial in the number of generated bits.

The sampler uses an expected constant number of coefficient pairs per clean
trial. Hence the expected cost under \(\min(r_p,r_q)\le R\) is bounded by

\[
 R\,\operatorname{poly}(n+L).
\]

If both the numerical value \(R\) and the length \(L=\log_2 W+O(1)\) are
quasipolynomial in \(n\), this product is quasipolynomial in \(n\). This counts
the stored exponent, all powering steps, the square chain, random bits, and gcd
verification. Sampling a uniform unit \(D\) by residue sampling and a gcd also
has constant expected overhead for distinct odd primes; a proper gcd again
finishes earlier.

This is only a conditional reduction for \(N=pq\) with distinct odd primes. It
does not construct a suitable word \(W\). It does not prove a small residual in
one of the four orientations. It does not cover prime inputs, prime powers,
even inputs, repeated factors, arbitrary composites, recursion to complete
factorization, or the cost of a new source that makes \(W\) depend materially
on the full value of \(D\). It therefore does not resolve the root factoring
objective.

## 9. The non-reconstructible family claim

The statement names an infinite “P158/F172 family” and asserts all of the
following for it:

- all four shifted common gcds are at most six;
- with \(W=1\), every \(R_\epsilon\) is \(2^{\Theta(\log N)}\);
- the incidental zero-divisor probability does not rescue a quasipolynomial
  number of bare trials.

The first item cannot be proved without a definition or construction of the
named family. The second item also needs a lower bound such as
\(\min(p,q)=N^{\Omega(1)}\). A bound \(d_\epsilon\le6\) alone only gives

\[
 R_\epsilon
 =\min\left(
 \frac{p-\epsilon_p}{d_\epsilon},
 \frac{q-\epsilon_q}{d_\epsilon}
 \right)
 \ge \frac{\min(p-1,q-1)}6,
\]

which need not be exponential in the input length when one prime is small.

The local zero-divisor estimate itself does reconstruct: its probability is
\(1-\rho_\ell(+)=2/\ell-1/\ell^2\) in the split case and
\(1-\rho_\ell(-)=1/\ell^2\) in the nonsplit case. Thus, if \(p\le q\), a
proper norm-gcd event in one constant-cost draw is \(O(1/p)\). To conclude that
quasipolynomially many such draws have negligible total success, one again
needs \(p=2^{\Omega(n)}\), or an equivalent size property of the named family.
That property is absent from the supplied statement.

Accordingly, the generic implication is proved, but the assertion that the
named family satisfies its hypotheses is not independently reconstructible.
