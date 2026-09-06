# F242 V2 blind reconstruction

## Verdict

**PASS for the theorem exactly as scoped.**  All of the stated algebraic and
probabilistic laws follow from the definitions.  Equation (9) is an exact law
for the experiment that first fixes a uniform unit discriminant and then
obtains a clean point while retaining that discriminant.  In the executable
sampler, a proper gcd can terminate before that clean point is obtained; this
only changes the equality into a lower bound for the complete trial, because
that termination has already factored \(N\).

This is not a pass for the root factoring statement.  The result assumes a
distinct odd semiprime, and it neither constructs the required word \(W\) nor
proves that any one of its four residual interfaces is small.

The authenticated SHA-256 of `V2_STATEMENT.md` is

```text
4ec456a0aa8794e36497a663b14747eba15dcaebd7984a923b53169969c1bfbd
```

## 1. The shifted common-capacity identity

Fix signs

\[
 \epsilon_p,\epsilon_q\in\{+1,-1\},\qquad
 J=\epsilon_p\epsilon_q,
\]

and put

\[
 m_p=p-\epsilon_p,qquad m_q=q-\epsilon_q,qquad
 d=\gcd(m_p,m_q),\qquad m_i=d s_i.
\]

By the definition of \(d\),

\[
 \gcd(s_p,s_q)=1.
\]

Substitute \(p=\epsilon_p+m_p\) and
\(q=\epsilon_q+m_q\).  This gives

\[
\begin{aligned}
 N-J
 &= (\epsilon_p+m_p)(\epsilon_q+m_q)
       -\epsilon_p\epsilon_q\\
 &= \epsilon_p m_q+\epsilon_q m_p+m_pm_q\\
 &=dK,
\end{aligned}
\]

where

\[
 K=\epsilon_p s_q+\epsilon_q s_p+d s_ps_q.
\]

Reduction modulo the two coprime residuals gives

\[
 K\equiv\epsilon_p s_q\pmod {s_p},\qquad
 K\equiv\epsilon_q s_p\pmod {s_q}.
\]

Consequently,

\[
 \gcd(K,s_p)=\gcd(K,s_q)=1.
\]

For \(E=(N-J)W=dKW\), it follows that

\[
\begin{aligned}
 \gcd(m_i,E)
 &=\gcd(d s_i,dKW)\\
 &=d\gcd(s_i,W).
                                                        \tag{10}
\end{aligned}
\]

In particular, \(\gcd(m_i,N-J)=d\).  Thus \(N-J\) supplies exactly the
common capacity \(d\); multiplication by \(W\) supplies only the part of
the coprime residual \(s_i\) that \(W\) contains.  If

\[
 r_i=\frac{s_i}{\gcd(s_i,W)},
\]

then (10) is equivalently

\[
 \frac{\gcd(m_i,E)}{m_i}=\frac1{r_i}.                 \tag{11}
\]

No quantity on the left side of the analysis other than \(E\) has to be
computed by the algorithm.  In particular, the algorithm does not know
\(p,q,d,s_i,r_i\), or the factorization of \(W\).

Because an odd prime minus either sign is even, both \(m_i\) are even.
Also \(N-J\) is even.  Hence \(e_i=v_2(m_i)\ge1\),
\(v=v_2(E)\ge1\), and

\[
 h_i=v_2(\gcd(m_i,E))=\min(e_i,v)\ge1.               \tag{12}
\]

## 2. The two local norm-one tori

For an odd prime \(\ell\in\{p,q\}\), reduce the quadratic algebra modulo
\(\ell\):

\[
 B_{\ell,D}=\mathbb F_\ell[w]/(w^2-D).
\]

The unit assumption on \(D\) makes this a quadratic etale algebra.

If \(\epsilon_\ell=(D/\ell)=+1\), then

\[
 B_{\ell,D}\simeq\mathbb F_\ell\times\mathbb F_\ell,
\]

conjugation exchanges the two coordinates, and the norm-one group is

\[
 \{(t,t^{-1}):t\in\mathbb F_\ell^\times\}
 \simeq\mathbb F_\ell^\times.
\]

It is cyclic of order \(\ell-1\).

If \(\epsilon_\ell=-1\), then

\[
 B_{\ell,D}\simeq\mathbb F_{\ell^2}.
\]

Its multiplicative group is cyclic of order \(\ell^2-1\).  The norm map
onto \(\mathbb F_\ell^\times\) has a cyclic kernel of order

\[
 \frac{\ell^2-1}{\ell-1}=\ell+1.
\]

Thus in both cases the local torus \(T_\ell\) is cyclic and

\[
 |T_\ell|=\ell-\epsilon_\ell.                        \tag{13}
\]

This proves the asserted orders \(m_p,m_q\).

## 3. Exact Hilbert--90 fibres and the clean sampler

Write \(z=A+Bw\).  In either local algebra, consider

\[
 \Phi_\ell:B_{\ell,D}^{\times}\longrightarrow T_\ell,
 \qquad z\longmapsto z/\bar z.
\]

Its kernel consists exactly of the nonzero elements fixed by conjugation,
namely \(\mathbb F_\ell^\times\).  Hence every fibre has size \(\ell-1\).
The image lies in the norm-one group.  Moreover,

\[
 |B_{\ell,D}^{\times}|
 =\begin{cases}
   (\ell-1)^2,&\epsilon_\ell=+1,\\
   \ell^2-1,&\epsilon_\ell=-1,
  \end{cases}
 =(\ell-1)(\ell-\epsilon_\ell).
\]

The image therefore has size \(\ell-\epsilon_\ell=|T_\ell|\), so
\(\Phi_\ell\) is onto.  This proves both surjectivity and the exact fibre
law.

The norm of \(z\) is

\[
 \nu=A^2-DB^2.
\]

Locally, \(z\) is a unit exactly when its norm is nonzero.  The exact local
clean density is consequently

\[
 c_\ell(\epsilon_\ell)
 =\frac{|B_{\ell,D}^{\times}|}{\ell^2}
 =\frac{(\ell-1)(\ell-\epsilon_\ell)}{\ell^2}.       \tag{14}
\]

For every odd \(\ell\), this is at least \(4/9\): the smaller case is the
split density \((1-1/\ell)^2\), minimized at \(\ell=3\).  CRT makes the
coefficient pairs modulo \(p\) and \(q\) independent.  Therefore one
uniform pair modulo \(N\) is clean with exact probability

\[
 c_p(\epsilon_p)c_q(\epsilon_q)\ge\frac{16}{81}.     \tag{15}
\]

Conditioning on cleanliness imposes one independent local unit condition
at each prime.  The constant-fibre calculation then shows that \(U_p\)
and \(U_q\) are independent and uniform on their complete tori.  Globally,
each pair \((U_p,U_q)\) has exactly \((p-1)(q-1)\) clean coefficient-pair
preimages.  The points \(+1\) and \(-1\) are present: \(z=1\) maps to
\(+1\), and \(z=w\) maps to \(-1\).  Thus this is not a Cayley chart with
an omitted endpoint.

The gcd screens have exact meanings.  If

\[
 c=\gcd(N,A,B)
\]

is proper, it is a verified factor.  If \(c=N\), the coefficient pair is
zero modulo both primes and can be rejected.  Similarly,
\(g_\nu=\gcd(\nu,N)\) is proper exactly when the norm vanishes at one prime
but not the other.  The case \(g_\nu=N\) is nonclean at both primes and is
rejected, while \(g_\nu=1\) certifies that the denominator is invertible.
Repeated independent pairs need at most \(81/16\) attempts in expectation
to reach a clean pair in the shadow experiment.  The actual sampler can
only stop sooner by finding a proper gcd.

After the unit certificate,

\[
 (A-Bw)^{-1}=\frac{A+Bw}{A^2-DB^2},
\]

so

\[
 U=\frac{A+Bw}{A-Bw}
  =\frac{A^2+DB^2}{\nu}+\frac{2AB}{\nu}w.
\]

This is the only required division.  All later arithmetic follows by
expanding \(w^2=D\):

\[
 (x_0+x_1w)(y_0+y_1w)
 =(x_0y_0+Dx_1y_1)+(x_0y_1+x_1y_0)w\pmod N.          \tag{16}
\]

Thus powering and the Miller chain are division-free.

## 4. Exact local returns

In a cyclic group of order \(m_i\), the equation \(x^E=1\) has exactly
\(\gcd(m_i,E)\) solutions.  Uniformity of \(U_i\), followed by (11), gives

\[
 \Pr(U_i^E=1)
 =\frac{\gcd(m_i,E)}{m_i}
 =\frac1{r_i}=\alpha_i.                              \tag{17}
\]

The two events are independent.

For any represented element \(Y=(y_0,y_1)\), reduction modulo a prime
\(\ell\mid N\) equals \(+1\) exactly when both
\(y_0-1\equiv0\) and \(y_1\equiv0\pmod\ell\).  It equals \(-1\) exactly
when both \(y_0+1\equiv0\) and \(y_1\equiv0\pmod\ell\).  Hence \(G_+(Y)\)
and \(G_-(Y)\) are respectively the products of the local primes at which
those signs occur.  For a distinct semiprime, each screen is in
\(\{1,p,q,N\}\), and every proper value is a verified factor.

For \(V=U^E\), the first \(G_+\) screen therefore returns a factor exactly
when one local component returns to the identity and the other does not.
This has probability

\[
 \alpha_p(1-\alpha_q)+(1-\alpha_p)\alpha_q
 =\alpha_p+\alpha_q-2\alpha_p\alpha_q.               \tag{18}
\]

If neither returns, the screen is \(1\) and the prescribed trial is null.
If both return, it is \(N\), and the two-primary chain applies.

## 5. The exact two-primary Miller law

Condition on the global return \(U_p^E=U_q^E=1\).  The two local points
remain independent and are uniform in the kernels of the \(E\)-power
maps.  Write \(E=2^v u\), with \(u\) odd.  The kernel at \(i\) has
two-primary part of order \(2^{h_i}\), by (12), and an odd part whose
order divides \(u\).  Raising to \(u\) kills the odd part and permutes the
two-primary part.  Thus

\[
 Y_{i,0}=U_i^u
\]

is uniform in a cyclic group of order \(2^{h_i}\), independently for the
two primes.

For a uniform element in a cyclic group of order \(2^h\), let \(T\) be
the base-two logarithm of its order.  Then

\[
 \Pr(T=0)=2^{-h},\qquad
 \Pr(T=t)=\frac{2^{t-1}}{2^h}\quad(1\le t\le h).     \tag{19}
\]

Along successive squarings, an element with \(T=t\ge1\) first reaches
\(-1\) after \(t-1\) squarings and \(+1\) after \(t\) squarings.  An
identity element has \(T=0\).  Therefore the joint \(G_+\) and \(G_-\)
screens find a proper factor if and only if \(T_p\ne T_q\): unequal
orders make one local sign occur before the corresponding sign at the
other prime, while equal orders synchronize every occurrence of
\(-1\) and \(+1\).

Let \(a=\min(h_p,h_q)\) and \(b=\max(h_p,h_q)\).  From (19),

\[
\begin{aligned}
 \Pr(T_p=T_q)
 &=2^{-a-b}\left(1+\sum_{t=1}^{a}2^{2t-2}\right)\\
 &=\frac{4^a+2}{3\,2^{a+b}}.
\end{aligned}
\]

The exact conditional chain success probability is hence

\[
 \mu_{a,b}=1-\frac{4^a+2}{3\,2^{a+b}}.              \tag{20}
\]

Since \(b\ge a\ge1\),

\[
 \frac{4^a+2}{3\,2^{a+b}}
 \le\frac{4^a+2}{3\,4^a}\le\frac12,
\]

and therefore \(\mu_{a,b}\ge1/2\).

Combining (18) with the both-return branch gives the exact clean powered
success law

\[
\begin{aligned}
 S
 &=\alpha_p+\alpha_q-2\alpha_p\alpha_q
   +\mu_{a,b}\alpha_p\alpha_q\\
 &=\alpha_p+\alpha_q-(2-\mu_{a,b})\alpha_p\alpha_q. \tag{21}
\end{aligned}
\]

To prove the residual lower bound, let

\[
 x=\max(\alpha_p,\alpha_q)=\frac1{\min(r_p,r_q)},
 \qquad y=\min(\alpha_p,\alpha_q).
\]

Then \(0<y\le x\le1\).  In fact \(S\ge\mu x\).  If
\(1-(2-\mu)x\ge0\), this follows immediately from

\[
 S-\mu x=x(1-\mu)+y[1-(2-\mu)x].
\]

If that bracket is negative, use \(y\le x\) to obtain

\[
 S-\mu x
 \ge x(1-\mu)+x[1-(2-\mu)x]
 =x(2-\mu)(1-x)\ge0.
\]

Together with \(\mu\ge1/2\), this proves

\[
 S\ge\frac1{2\min(r_p,r_q)}.                        \tag{22}
\]

If \(\min(r_p,r_q)\le R\), independent clean powered trials have success
probability at least \(1/(2R)\).  Their count is stochastically bounded by
a geometric variable of mean \(2R\), and failure forever has probability
zero.  Proper sampler gcd exits only shorten this process.

## 6. Four orientations and the rejection distinction

For a uniform unit \(D\bmod N\), CRT makes its reductions uniform and
independent in \(\mathbb F_p^\times\) and
\(\mathbb F_q^\times\).  Exactly half of the nonzero elements in each
field have each Legendre sign.  Consequently

\[
 (\epsilon_p,\epsilon_q)
 \in\{(+,+),(+,-),(-,+),(-,-)\}
\]

is uniform on the four possibilities.  The actual value of \(D\) within
a sign class does not affect the group order, the constant-fibre uniform
law, or the powered probability.  For fixed \(W\), those laws therefore
depend only on the orientation.

The clean density does depend on the orientation.  From (14), it is

\[
 C_\epsilon
 =\frac{(p-1)(p-\epsilon_p)}{p^2}
  \frac{(q-1)(q-\epsilon_q)}{q^2}.                   \tag{23}
\]

Thus drawing a new \(D\) whenever a coefficient pair is nonclean and then
conditioning on a clean triple would give

\[
 \Pr(\epsilon\mid\text{clean})
 =\frac{C_\epsilon}{\sum_\eta C_\eta},              \tag{24}
\]

not \(1/4\).  Nonsplit algebras have more units than split algebras, so
this is a real bias.

The correct clean-point experiment is:

1. choose one uniform unit \(D\), and
2. retain it while independently resampling only \((A,B)\) until a clean
   pair is obtained.

Every retained \(D\) eventually obtains a clean pair with probability one,
so its original orientation remains uniform.  Let \(S_\epsilon\) be (21)
for that orientation and \(R_\epsilon=\min(r_p,r_q)\).  The exact powered
law in this experiment is

\[
 \Pr(\text{powered factor})
 =\frac14\sum_\epsilon S_\epsilon.                  \tag{25}
\]

If the executable sampler returns a proper gcd before reaching the shadow
clean point, it has already succeeded.  More explicitly, for a fixed
orientation let one coefficient draw have probabilities \(P,C,Z\) of a
proper gcd, a clean point, and a rejection.  Repeating only after \(Z\)
gives total trial success

\[
 \frac{P+C S_\epsilon}{P+C}\ge S_\epsilon.          \tag{26}
\]

This proves that (25) is a lower bound for the complete executable trial,
even though the orientation distribution conditional on actually reaching
the powered phase can be biased by early successful gcd exits.

Let

\[
 R_*=\min_\epsilon R_\epsilon.
\]

Choose an orientation attaining \(R_*\).  Equations (22) and (25) give

\[
 \frac14\sum_\epsilon S_\epsilon
 \ge\frac1{8R_*}.                                   \tag{27}
\]

The four order pairs are exactly

\[
 (p-1,q-1),\quad(p-1,q+1),\quad
 (p+1,q-1),\quad(p+1,q+1).
\]

The first is the unshifted interface; the other three are its shifted
interfaces.  Repeating different discriminants inside one orientation
does not create another residual law when \(W\) is fixed.

## 7. Bit complexity

Let \(L=\lceil\log_2(N+1)\rceil\) and
\(L_W=\lceil\log_2(W+1)\rceil\).  The exponent has bit length

\[
 L_E=O(L+L_W).
\]

All algebra coefficients are reduced modulo \(N\), so they retain
\(O(L)\) bits.  Using even schoolbook integer arithmetic is sufficient for
the following bounds:

- one algebra multiplication or square in (16) costs a polynomial in
  \(L\);
- binary powering costs \(O(L_E)\) such operations;
- the second powering by \(u\) and at most \(v\le L_E\) chain squarings
  cost \(O(L_E)\) further algebra operations;
- every gcd, modular inverse, Jacobi-symbol computation, and returned-factor
  verification costs a polynomial in the involved bit lengths;
- sampling a uniform residue costs \(O(L)\) random bits in constant expected
  attempts, and (15) bounds clean coefficient sampling by a fixed constant
  in expectation; and
- constructing the explicit integer \(E=(N-J)W\), finding \(v_2(E)\), and
  reading its exponent bits cost a polynomial in \(L_E\).

Suppose \(L_W\) and the relevant trial bound \(R\) are each at most

\[
 2^{C(\log_2(L+1))^k}
\]

for fixed constants (allowing adjustment to a common \(C,k\)).  A clean
powered trial then has quasipolynomial bit cost, and multiplying it by the
expected \(2R\) fixed-orientation trials, or by the expected \(8R\)
four-orientation trials when \(R_*\le R\), remains quasipolynomial.
Intermediate storage is also quasipolynomial.  No factorization of \(E\)
or \(W\) is used: \(v_2(E)\) is obtained directly from the binary integer.

Sampling a unit \(D\) is also factor-free.  Draw a uniform residue and
compute \(\gcd(D,N)\).  A proper gcd is already a factor; zero is rejected;
conditional on gcd one, \(D\) is uniform in the unit group.  Its unit
density is at least \((1-1/3)^2=4/9\), so this adds only a constant expected
number of residue draws.  The signs themselves are never computed; only
their product \(J=(D/N)\) is needed, and the Jacobi symbol is public and
computable in polynomial time.

These bounds account only for the supplied word.  They do not account for
a procedure that discovers such a word, because none is given.

## 8. Exact remaining source

For a fixed supplied word, the torus theorem proves only the implication

\[
 R_*(p,q;W)
 :=\min_{(\epsilon_p,\epsilon_q)}
 \min\left(
 \frac{(p-\epsilon_p)/d_\epsilon}
      {\gcd((p-\epsilon_p)/d_\epsilon,W)},
 \frac{(q-\epsilon_q)/d_\epsilon}
      {\gcd((q-\epsilon_q)/d_\epsilon,W)}
 \right)
 \le R
 \Longrightarrow
 \Pr(\text{factor per orientation trial})\ge\frac1{8R},
\]

where

\[
 d_\epsilon=\gcd(p-\epsilon_p,q-\epsilon_q).
\]

It supplies no upper bound on \(R_*(p,q;W)\).

The missing integer-source theorem would have to construct, without
knowing \(p\) or \(q\), a word \(W=W(N)\) in quasipolynomial bit complexity
such that

1. \(\log W\) is quasipolynomial in \(L\), and
2. \(R_*(p,q;W)\) is quasipolynomial in \(L\) for every distinct odd
   semiprime \(N=pq\).

A randomized source would instead need a proved all-input expectation or
success law strong enough that the combined cost of generating words and
running the corresponding torus trials is quasipolynomial.  Allowing
\(W\) to depend materially on the full discriminant \(D\) changes the
source problem: values within one orientation can then have different
residuals, so the fixed-\(W\) four-term law alone gives no progress bound.
That dependence needs its own uniform all-input probability and bit-cost
proof.

Even such a source theorem would complete only the distinct-odd-semiprime
stage proved here.  A solution of the root statement must additionally
give and cost a correct reduction covering primes, prime powers, repeated
factors, even inputs, and arbitrary composites, followed by verified
recursive complete factorization.
