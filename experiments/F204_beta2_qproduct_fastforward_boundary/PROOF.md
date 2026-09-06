# Proof of F204

## 1. Lambert series and the binary norm

Formal expansion gives

\[
 \sum_{a\geq1}\frac{a\chi(a)q^a}{1-q^a}
 =\sum_{a\geq1}\sum_{j\geq1}a\chi(a)q^{aj}.
\]

The coefficient of `q^n` is

\[
 \sum_{a\mid n}a\chi(a)=A(n).
\]

Also,

\[
 q\frac{d}{dq}\log(1-q^a)
 =-\frac{aq^a}{1-q^a}.
\]

Since

\[
 P(q)=\prod_{a\geq1}(1-q^a)^{\chi(a)},
\]

coefficientwise formal differentiation proves

\[
 L(q)=-q\frac{d}{dq}\log P(q).
\]

Only odd `a` occur. Therefore

\[
 \begin{aligned}
 P(q)P(-q)
 &=\prod_{a\text{ odd}}
   \bigl((1-q^a)(1+q^a)\bigr)^{\chi(a)}\\
 &=\prod_{a\text{ odd}}(1-q^{2a})^{\chi(a)}\\
 &=P(q^2).
 \end{aligned}
\]

Applying `-q d/dq` to the logarithm gives

\[
 L(q)+L(-q)=2L(q^2).
\]

At `q^(2n)` this says `2A(2n)=2A(n)`. At every odd power, the
left side cancels and the right side is zero. Thus the identity is exactly
`A(2n)=A(n)` and contains no odd-index equation.

For the stronger formal statement, logarithms are defined because
`G(0)=1`. The norm is equivalent to

\[
 \sum_{n\geq1}g_nq^n
 +\sum_{n\geq1}(-1)^ng_nq^n
 =\sum_{n\geq1}g_nq^{2n}.
\]

Odd powers give the tautology zero equals zero. At `q^(2n)` one gets

\[
 2g_{2n}=g_n.
\]

Conversely, these coefficient relations imply the logarithmic identity and
hence the norm after exponentiation. Iteration gives
`g_(2^v r)=2^(-v)g_r`. The odd coefficients are unrestricted.

## 2. Radial asymptotics of the q-product

Let `q=e^(-t)` and `Q=q^4=e^(-4t)`. The q-gamma function satisfies

\[
 \Gamma_Q(x)
 =(1-Q)^{1-x}\frac{(Q;Q)_\infty}{(Q^x;Q)_\infty}.
\]

Solving this formula for the two q-Pochhammer symbols gives

\[
 P(e^{-t})
 =\frac{(Q^{1/4};Q)_\infty}{(Q^{3/4};Q)_\infty}
 =(1-Q)^{1/2}
   \frac{\Gamma_Q(3/4)}{\Gamma_Q(1/4)}.
\]

The standard limit `Gamma_Q(x) -> Gamma(x)` as `Q -> 1` and
`1-Q ~ 4t` give

\[
 \boxed{
 P(e^{-t})
 \sim C\sqrt t,
 \qquad
 C=2\frac{\Gamma(3/4)}{\Gamma(1/4)}>0.}
\]

The exact binary norm now gives

\[
 P(-e^{-t})
 =\frac{P(e^{-2t})}{P(e^{-t})}
 \longrightarrow\sqrt2.
\]

These limits also show directly that no zero or pole at either cusp is being
hidden in an exponentially small term.

## 3. The scalar modularity boundary

Let `q=e^(2 pi i tau)` and first approach the cusp zero along
`tau=iy`, so `t=2 pi y`. The preceding limits give

\[
 |F_{a,b,\alpha}(iy)|
 \sim C_0 y^{a/2}
\]

with `C_0` finite and nonzero. The normalization
`e^(2 pi i alpha tau)` tends to one.

Next approach the cusp one-half along `tau=1/2+iy`. Then
`q=-e^(-2 pi y)`, so the two product factors exchange roles. Hence

\[
 |F_{a,b,\alpha}(1/2+iy)|
 \sim C_{1/2}y^{b/2},
\]

again with a finite nonzero constant. The exponential normalization tends in
modulus to one and only contributes a fixed phase.

For a nonzero scalar meromorphic modular form of weight `k` with the stated
cusp hypothesis, choose a scaling matrix at a rational cusp. If the leading
local Fourier exponent is nonzero, radial growth or decay is exponential in
`1/y`. If the leading exponent is zero, undoing the weight-`k` slash
operator gives a finite nonzero constant times `y^(-k)`. There is no third
polynomial exponent.

Our two asymptotics are polynomial and have nonzero leading constants, so
both cusp orders must be zero. At the cusp zero this forces

\[
 \frac a2=-k,
\]

while at the cusp one-half it forces

\[
 \frac b2=-k.
\]

Therefore `a=b`. Taking `(a,b)=(1,0)` proves the stated nonmodularity of
`P`.

Finally,

\[
 -q\frac{d}{dq}\log(P(q)^aP(-q)^b)
 =aL(q)+bL(-q).
\]

The coefficient at `q^N` is

\[
 aA(N)+b(-1)^NA(N).
\]

For odd `N` this is `(a-b)A(N)`. Thus `a=b` deletes the target, while
`a != b` violates the necessary scalar modularity condition.

This proof uses neither a converse nor a classification of modular units. It
does not cover sums or general rational functions of the orbit, vector-valued
objects, nonholomorphic completions, or transformation laws without ordinary
meromorphic cusp expansions.

## 4. The mod-two sequence has an infinite two-kernel

Modulo two, every odd divisor contributes one and every even divisor
contributes zero. Therefore

\[
 A(n)\equiv\#\{d:d\mid n,\ d\text{ odd}\}
 =\tau(\operatorname{oddpart}(n))\pmod2.
\]

The divisor-count function is odd exactly on squares. Hence, with

\[
 b(n)=A(n)\bmod2,
\]

one has

\[
 b(n)=1
 \iff \operatorname{oddpart}(n)\text{ is a square}.
\]

For every integer `e >= 2`, consider the two-kernel element

\[
 s_e(k)=b(2^ek+1).
\]

Set `k_e=2^e+2`. Then

\[
 2^ek_e+1=2^{2e}+2^{e+1}+1=(2^e+1)^2,
\]

so `s_e(k_e)=1`.

Let `f >= e+2` and put

\[
 M=2^fk_e+1.
\]

This integer is odd, and

\[
 v_2(M-1)
 =v_2\bigl(2^f(2^e+2)\bigr)
 =f+1,
\]

because `2^(e-1)+1` is odd. Suppose `M=x^2`. Then `x` is odd and

\[
 v_2((x-1)(x+1))=f+1.
\]

The two even neighbors `x-1,x+1` have greatest common divisor two. One has
two-adic valuation one, so the other has valuation `f`. Consequently

\[
 x\equiv1\pmod{2^f}
 \quad\text{or}\quad
 x\equiv-1\pmod{2^f}.
\]

But

\[
 M>1
\]

and

\[
 \begin{aligned}
 (2^f-1)^2-M
 &=2^{2f}-2^{f+1}+1
   -(2^{f+e}+2^{f+1}+1)\\
 &=2^f(2^f-2^e-4)>0,
 \end{aligned}
\]

where the last inequality uses `f >= e+2` and `e >= 2`. Thus

\[
 1<x<2^f-1,
\]

contradicting `x congruent to plus or minus 1 modulo 2^f`. Hence `M` is
not a square and `s_f(k_e)=0`.

Restricting to even values `e=2,4,6,...`, every later `f` satisfies
`f >= e+2`. The sequences `s_e` are therefore pairwise distinct. The
two-kernel of `b` is infinite. By the standard finite-kernel criterion, `b`
is not two-automatic.

## 5. Primitive reduction of a Mahler equation

Assume for contradiction that the following identity holds as a formal
Laurent series:

\[
 R_{-1}(q)+\sum_{i=0}^{s}R_i(q)L(q^{2^i})=0
\]

with rational-function coefficients and at least one nonzero coefficient of
a Mahler iterate.

Clear rational-function denominators, clear numerical denominators, clear
any common power of `q` caused by poles at zero, and divide the integer
content of all coefficient polynomials. This gives

\[
 P_{-1}(q)+\sum_{i=0}^{s}P_i(q)L(q^{2^i})=0,
 \qquad P_i(q)\in\mathbb Z[q],
\]

whose full family of integer coefficients has greatest common divisor one.
Reduction modulo two is therefore not identically zero.

If every multiplier `P_i` with `i >= 0` vanished modulo two, the reduced
identity would say that the nonzero polynomial `P_{-1}(q)` is zero. Thus at
least one Mahler multiplier remains nonzero modulo two.

Let

\[
 B(q)=\sum_{n\geq1}b(n)q^n\in\mathbb F_2[[q]].
\]

In characteristic two, Frobenius gives

\[
 B(q^{2^i})=B(q)^{2^i}.
\]

The reduced Mahler identity is therefore a nonzero polynomial equation

\[
 \overline P_{-1}(q)
 +\sum_{i=0}^{s}\overline P_i(q)B(q)^{2^i}=0
\]

over `F_2(q)`. The powers `1,X,X^2,X^4,...` are distinct, so the displayed
polynomial in `X` is nonzero. Hence `B(q)` is algebraic over `F_2(q)`.

Christol's theorem now says that `b(n)` is two-automatic. This contradicts
the infinite two-kernel proved above. No such linear Mahler equation exists.

## 6. Root norm at an odd prime

Let `ell` be an odd prime and `epsilon=chi(ell)`. For a fixed odd `a`,

\[
 \prod_{j=0}^{\ell-1}(1-\zeta^{ja}q^a)
 =\begin{cases}
  1-q^{a\ell},&\ell\nmid a,\\
  (1-q^a)^\ell,&\ell\mid a.
 \end{cases}
\]

Apply this factorwise to the product for `P`. The factors with
`ell` not dividing `a` give

\[
 \prod_{\ell\nmid a}(1-q^{\ell a})^{\chi(a)}
 =\frac{P(q^\ell)}{P(q^{\ell^2})^\epsilon},
\]

because the omitted indices have the form `a=ell d` and
`chi(ell d)=epsilon chi(d)`. The factors with `a=ell d` give

\[
 \prod_{d\text{ odd}}(1-q^{\ell d})^{\ell\epsilon\chi(d)}
 =P(q^\ell)^{\ell\epsilon}.
\]

Multiplication proves

\[
 \prod_{j=0}^{\ell-1}P(\zeta^jq)
 =\frac{P(q^\ell)^{1+\ell\epsilon}}
        {P(q^{\ell^2})^\epsilon}.
\]

Apply `-q d/dq`. The root-of-unity filter on the left is

\[
 \sum_{j=0}^{\ell-1}L(\zeta^jq)
 =\ell\sum_{k\geq1}A(\ell k)q^{\ell k}.
\]

The right side becomes

\[
 \ell(1+\ell\epsilon)L(q^\ell)
 -\epsilon\ell^2L(q^{\ell^2}).
\]

Comparing the coefficient of `q^(ell k)` and dividing by `ell` yields

\[
 A(\ell k)
 =(1+\ell\epsilon)A(k)
 -\epsilon\ell\,\mathbf1_{\ell\mid k}A(k/\ell).
\]

If `ell` divides the target `N`, its gcd with `N` is already a factor. If
not, the recurrence reads

\[
 A(\ell N)=(1+\ell\epsilon)A(N),
\]

which moves to a larger coefficient and does not create a recursive child.

## 7. Complexity and recursion scope

No step evaluates `A(N)`. Direct truncation of the displayed product or
Lambert series through degree `N` has an explicit degree parameter
exponential in the input length; no arithmetic-operation count for such a
truncation is used as a QP bound.

The proofs concern fixed finite identities at the same target node. They do
not object to a future one-child recursion. The recurrence

\[
 T(n)\leq T(n-1)+\operatorname{QP}(n)
\]

remains valid QP accounting.
