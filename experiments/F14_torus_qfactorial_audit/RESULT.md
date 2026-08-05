# Hostile audit of F14: torus q-factorial evaluator obstructions

## Verdict

The main F14 result survives after two scope corrections and two wording
qualifications.

1. The exact all-finite-field threshold-binomial theorem is correct.  The
   exponents strictly above `M/2` must occur literally, not merely through
   larger multiples, because the same hypothesis first forces every exponent
   to be at most `M`.  The lower bound is `ceil(M/2)` distinct exponents and is
   sharp within this product model.
2. `P_M` and `S_m` have the same prime support modulo an arbitrary `N`, but
   they need not produce the same gcd when `N` is not squarefree.  The useful
   exact statement is a valuation inequality: `gcd(P_M(a),N)` divides
   `gcd(S_m(a),N)`.  Thus `P_M` is at least as good as `S_m` for obtaining a
   proper gcd, but it is not an equivalent residue or an identical gcd
   observable.
3. The equal-floor group count is valid.  Variation of the weights proves
   only that the unweighted product of a group is insufficient; it does not
   prove that every weighted group aggregate has large circuit size or takes
   many operations.
4. The dense coefficient counts are formal counts over `Z[a]`.  They lower
   bound a dense symbolic materialization, not a specialized sparse state
   after evaluating `a` modulo a particular modulus.

With those corrections, the q-Pochhammer addition laws, the `M=4` lcm
counterexample, the equal-floor count, and the characteristic-zero degree
bound are correct.  None supplies an arithmetic-circuit lower bound, and F14
does not close the missing evaluator in P20.

## 1. Prime support: corrected exact statement

Let `M=m-1` and

\[
P_M(a)=\prod_{d=1}^{M}(1-a^d),\qquad
S_m(a)=\prod_{d=1}^{M}(1-a^d)^{m-d}.
\]

For every prime `p`,

\[
p\mid P_M(a)\quad\Longleftrightarrow\quad p\mid S_m(a),
\]

because all weights `m-d` are positive and a product in `F_p` is zero if and
only if one of its factors is zero.  Moreover,

\[
v_p(P_M(a))
=\sum_{d=1}^{M}v_p(1-a^d)
\le
\sum_{d=1}^{M}(m-d)v_p(1-a^d)
=v_p(S_m(a)).
\]

Consequently

\[
\gcd(P_M(a),N)\mid\gcd(S_m(a),N).
\]

The two gcds have the same set of prime divisors, but their prime-power
valuations can differ.  For example, take

\[
N=875=5^3\cdot7,\qquad a=631,\qquad m=3.
\]

Here `a-1=630` has valuation one at both 5 and 7, and `a+1=632` is a unit at
both.  Hence `v_5(P_2)=2`, while `v_5(S_3)=3`; both products vanish modulo 7.
Therefore

\[
\gcd(P_2(a),875)=175,
\qquad
\gcd(S_3(a),875)=875.
\]

So "same prime support" must not be promoted to "same gcd".  Operationally,
the valuation inequality is favorable: if the `S_m` gcd is proper and
nontrivial, then the `P_M` gcd is also proper and nontrivial, while `P_M` can
occasionally split when `S_m` saturates `N`.  This does not make `P_M` an
evaluator for the requested residue `S_m`.

When `a` is a unit in a field and has order `t`, both products vanish exactly
when `t<=M`.  If `a` is not a unit modulo a prime, every factor is one modulo
that prime and neither product vanishes there.

## 2. Exact threshold-binomial theorem

### Corrected theorem

Fix `M>=2`.  Let

\[
F(a)=\prod_{h=1}^{r}(1-a^{L_h})^{w_h},
\]

where all `L_h` and `w_h` are positive integers.  Suppose that for every
finite field `K` and every `a in K^times`,

\[
F(a)=0\quad\Longleftrightarrow\quad \operatorname{ord}(a)\le M.
\]

Then the set of distinct exponents among the `L_h` contains

\[
\{\lfloor M/2\rfloor+1,\ldots,M\}.
\]

It therefore contains at least

\[
M-\lfloor M/2\rfloor=\lceil M/2\rceil
\]

distinct exponents.

### Hostile checks

First, every `L_h<=M`.  If `L_h>M`, choose a finite field containing an
element of order exactly `L_h`; that factor vanishes although the order is
above the threshold.

Now take any integer `t` with `M/2<t<=M` and an element of exact order `t`.
The product can vanish only if `t` divides at least one `L_h`.  This is where
mere divisibility, rather than equality, is initially all that follows.  But
the first step gives

\[
t\mid L_h,\qquad t\le L_h\le M<2t,
\]

so `L_h=t`.  Repeated exponents do not alter the count.  Positive weights do
not alter the zero set, even when a characteristic divides a weight.  Zero
weights would simply be deleted and are correctly excluded by the theorem.

The exact-order witnesses exist for every positive `t`: choose a prime `q`
not dividing `t`.  Euler's theorem gives

\[
t\mid q^{\varphi(t)}-1,
\]

and the cyclic group `F_(q^{phi(t)})^times` contains an element of order `t`.
No prime-in-progression theorem is needed for the all-finite-field statement.
If the hypothesis is instead restricted to prime fields, the same argument
does require the existence of a prime congruent to 1 modulo `t` (for example,
Dirichlet's theorem).

The endpoint count is exact for both parities.  For `M=2k`, the forced set is
`k+1,...,2k` and has `k` members.  For `M=2k+1`, it is
`k+1,...,2k+1` and has `k+1` members.

The bound is also sharp within the stated binomial-product model.  The product

\[
\prod_{L=\lfloor M/2\rfloor+1}^{M}(1-a^L)
\]

has the exact threshold zero set: if `t<=M/2`, then
`floor(M/t)t` lies strictly above `M/2` and at most `M`; if `M/2<t<=M`, use
`L=t`; and an order above `M` divides none of the listed exponents.

This theorem applies only to a fixed product of binomials with positive
integer powers and an exact zero predicate over all finite fields.  It says
nothing about sums, rational functions, characteristic-dependent
representations, average-case predicates, or arbitrary arithmetic circuits.

## 3. The `M=4` single-lcm counterexample

This claim is correct.  The lcm is 12, and 2 has order 12 in `F_13`:

\[
2^2=4,\quad 2^3=8,\quad 2^4=3,\quad 2^6=-1\pmod {13}.
\]

Thus no power indexed by a proper divisor of 12 is one, while `2^12=1`.
The binomial `1-a^12` and the corresponding one-factor resultant vanish even
though `12>4`.  This refutes only the proposed single-lcm compression.

## 4. Addition laws and leaf accounting

The identities

\[
Q(s,n+k)=Q(s,n)Q(s+n,k)
\]

and

\[
T(s,n+k)=T(s,n)Q(s,n)^kT(s+n,k)
\]

are exact.  In the second identity, the first `n` factors gain weight `k`,
and the last `k` factors have the triangular weights of the shifted block.

For the literal syntax-directed evaluator that recursively obtains both
adjacent child states and then applies these identities, the work obeys

\[
W(2n)=2W(n)+\operatorname{poly}(\log n,\log N)
\]

and reaches `n` singleton leaves.  This is valid accounting for that
mechanism.  The identities alone do not prove that the right child cannot be
obtained by some different representation or algorithm, so the recurrence is
not a lower bound for all evaluators.

## 5. Dense shifted boundary coefficients

As formal polynomials in `Z[a][X]`,

\[
Q_n(X)=\prod_{d=1}^{n}(1-Xa^d)
\]

has degree `n` and exactly `n+1` nonzero coefficients.  Every contribution to
the coefficient of `X^k` has sign `(-1)^k` and a positive coefficient as a
polynomial in `a`, so it cannot cancel.  The identical sign argument applied
to repeated factors shows that

\[
T_n(X)=\prod_{d=1}^{n}(1-Xa^d)^{n+1-d}
\]

has degree `n(n+1)/2` and every coefficient in that range is nonzero.

Therefore a dense *formal* materialization needs `n+1` or
`n(n+1)/2+1` coefficient slots.  After specializing `a` and reducing modulo a
particular `N`, coefficients can cancel or vanish, and a sparse specialized
representation need not retain the formal count.  A factored expression or
an arithmetic DAG can also remain small.  The result closes only the dense
formal-boundary implementation.

## 6. Cyclotomic factorization and equal-floor groups

The factorization and weights are correct:

\[
S_m(a)=(-1)^{\binom m2}\prod_{e=1}^{M}\Phi_e(a)^{E_e},
\qquad
E_e=hm-e\frac{h(h+1)}2,
\quad h=\lfloor M/e\rfloor.
\]

Let `q=floor(sqrt(M))`.  The quotients for `e=1,...,q` are strictly
decreasing and at least `q`.  Every value `1,...,q` also occurs among all
quotients.  These two sets overlap in at most the value `q`, giving at least

\[
2q-1
\]

distinct quotient groups.  The bound is valid for small `M` as well, though
it is not always tight.

Within a group, `E_e` is affine and nonconstant in `e`.  Hence the unweighted
aggregate `prod_e Phi_e(a)` cannot by itself reconstruct the weighted group
contribution.  Rewriting a weighted product as a quotient is not a uniform
modular evaluation method because the denominator can be a nonunit modulo a
composite `N`.

The hostile scope correction is that nonconstant weights do not prove a
complexity lower bound for a division-free weighted aggregate: a different
factored identity or circuit might compute that aggregate succinctly.  What
is proved is narrower.  A literal method doing constant work per equal-floor
group already has `Omega(sqrt(M))` groups, and an unweighted product per group
loses required information.  No different fast cyclotomic evaluator is ruled
out.

## 7. Explicit characteristic-zero root polynomial

Add the word *nonzero* to the statement.  If a nonzero polynomial over a
characteristic-zero field vanishes at every root of unity of order at most
`M`, then all the distinct cyclotomic factors divide it, so its degree is at
least

\[
D_M=\sum_{t=1}^{M}\varphi(t).
\]

The elementary estimate in F14 is valid.  If `t` has `r` distinct prime
factors `p_1<...<p_r`, then `p_i>=i+1` and

\[
\frac{t}{\varphi(t)}
=\prod_i\frac{p_i}{p_i-1}
\le\prod_i\frac{i+1}{i}
=r+1
\le1+\log_2 t.
\]

For the at least `M/2` integers in `(M/2,M]`, this gives

\[
D_M\ge\frac{M^2}{4(1+\log_2 M)}.
\]

This is a degree lower bound for an explicitly materialized nonzero
root-set polynomial.  Degree is not circuit size: high-degree polynomials can
have short straight-line programs.

## 8. Final scope

The audit accepts F14 as a narrow method-failure result after the corrections
above.  It rules out polylogarithmically many fixed binomial factors for the
exact universal threshold predicate and refutes several literal proposed
implementations.  It does not establish an arithmetic-circuit lower bound,
an evaluation-time lower bound for `P_M` or `S_m`, or a classical
polylogarithmic evaluator.  P20's evaluator gap remains open.
