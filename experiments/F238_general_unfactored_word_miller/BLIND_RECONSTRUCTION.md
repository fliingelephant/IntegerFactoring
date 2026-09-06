# Blind reconstruction of F238

## Integrity and verdict

- Expected SHA-256 of `STATEMENT.md`:
  `4be9c61c28826701960cdebdf326638d04ae00ec5ffa5db279ca3a7b5b19d2d9`.
- Computed SHA-256 of `STATEMENT.md` before reading it:
  `4be9c61c28826701960cdebdf326638d04ae00ec5ffa5db279ca3a7b5b19d2d9`.
- Hash comparison: **MATCH**.
- Sources used: only the root `PROMPT.md` and this experiment's verified
  `STATEMENT.md`.

**Verdict on the claims at their stated scope: PASS.**  The local root
probabilities, the unequal-(2)-Sylow Miller formula, both lower bounds, the
two-adic specializations, and the extension to any number of distinct prime
supports with possible repeated prime powers all follow from the derivation
below.

**Verdict as a solution of the root factoring prompt: FAIL / incomplete.**
The statement explicitly leaves open the construction, from (N), of a
quasipolynomial-bit (W) with the required residual bound.  It also proves a
reduction only for odd squarefree semiprimes, with a natural trial analysis for
more general odd composites.  It therefore does not give the all-input
factoring algorithm required by the root prompt.

I interpret “square successively and test every gcd” as testing
(z_i=x^{2^i u}\bmod N) for (0\le i\le v), and then stopping.  This is a
finite, forced endpoint because (z_v=x^E=1\bmod N) when the chain is entered,
and all later values remain (1).  No claim below depends on testing after
that endpoint.

## 1. Exact local probabilities

Let (N=pq), where (p\ne q) are odd primes, and put

\[
d=\gcd(p-1,q-1),\qquad p-1=d s_p,\qquad q-1=d s_q.
\]

Dividing two integers by their gcd gives
(\gcd(s_p,s_q)=1).  Also

\[
\gcd(N-1,p-1)
=\gcd(pq-1,p-1)
=\gcd(q-1,p-1)=d.
\]

Consequently, if (A=(N-1)/d), then (\gcd(A,s_p)=1).  For
(E=(N-1)W=dAW),

\[
\gcd(E,p-1)
=d\gcd(AW,s_p)
=d\gcd(W,s_p).
\]

The group (\mathbb F_p^\times) is cyclic of order (p-1).  Hence the
fraction of its elements killed by exponent (E) is

\[
\frac{\gcd(E,p-1)}{p-1}
=\frac{\gcd(W,s_p)}{s_p}
=\frac1{r_p}=\alpha_p.
\]

The same argument gives probability (\alpha_q=1/r_q) modulo (q).
Uniform sampling from ((\mathbb Z/N\mathbb Z)^\times), followed by CRT,
makes the two local components independent.  This proves (2), including its
independence assertion.  It also shows that no factorization of (W), (E),
or (N-1) is used by the trial.

## 2. Conditional Miller law, including unequal Sylow sizes

Write (E=2^v u), with (u) odd.  Because (N) is odd, (v\ge1).  For
(\ell\in\{p,q\}), condition on (x^E=1\bmod\ell).  The conditioned local
component is uniform in the (E)-torsion subgroup of
(\mathbb F_\ell^\times).  The order of the two-primary part of this subgroup
is

\[
2^{h_\ell},\qquad h_\ell=\min(v_2(\ell-1),v).
\]

Its odd-order part has order dividing (u).  Thus raising (x) to (u)
kills that odd part, while raising to the odd exponent (u) permutes the
two-primary part.  Therefore

\[
z_0=x^u
\]

is uniform in a cyclic group of order (2^{h_\ell}).  Let (J_\ell) be the
integer such that (z_0\bmod\ell) has exact order (2^{J_\ell}).  In a cyclic
group of order (2^h), one element has order (1), and
(\varphi(2^j)=2^{j-1}) elements have exact order (2^j).  Hence

\[
\Pr(J_\ell=0)=2^{-h_\ell},\qquad
\Pr(J_\ell=j)=2^{j-1-h_\ell}\quad(1\le j\le h_\ell).
\]

These are exactly the distributions (P_{h_\ell}).  The two labels are
independent after conditioning on (g=N), because that event is the product
of the two independent local root conditions.

The chain succeeds exactly when (J_p\ne J_q).  Indeed, suppose
(J_p<J_q).  At index (i=J_p), the (p)-component of (z_i) is (1),
whereas the (q)-component still has order greater than (1).  Thus
(\gcd(z_i-1,N)=p).  The other strict inequality is symmetric.  If instead
(J_p=J_q=j), then before index (j-1) neither component is (1) or (-1);
at index (j-1) both are (-1) when (j\ge1); and from index (j) onward
both are (1).  For (j=0), both start at (1).  Every tested gcd is then
either (1) or (N), so there is no proper factor.

Put (a=\min(h_p,h_q)) and (b=\max(h_p,h_q)).  The conditional failure
probability is therefore

\[
\begin{aligned}
\Pr(J_p=J_q)
&=2^{-a-b}+\sum_{j=1}^{a}2^{j-1-a}2^{j-1-b}\\
&=2^{-a-b}\left(1+\sum_{j=1}^{a}4^{j-1}\right)\\
&=\frac{4^a+2}{3\,2^{a+b}}.
\end{aligned}
\]

Thus the exact conditional success probability is

\[
\mu_{a,b}=1-\frac{4^a+2}{3\,2^{a+b}},
\]

which proves (1), including the unequal-Sylow case.  Since (a\ge1) and
(b\ge a),

\[
1-\mu_{a,b}
\le \frac{4^a+2}{3\,4^a}
=\frac13+\frac{2}{3\,4^a}
\le\frac12.
\]

This proves (4).

## 3. Complete semiprime trial

Let (A_p) and (A_q) be the two local root events.  If exactly one occurs,
the initial gcd is the associated prime.  If neither occurs, the gcd is
(1).  If both occur, the gcd is (N), and the conditional chain succeeds
with probability (\mu_{a,b}).  Therefore

\[
\begin{aligned}
\Pr(\text{factor})
&=\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p)
  +\mu_{a,b}\alpha_p\alpha_q\\
&=\alpha_p+\alpha_q-(2-\mu_{a,b})\alpha_p\alpha_q,
\end{aligned}
\]

which is (3).

Suppose, without loss of generality, that
(\alpha_p=\max(\alpha_p,\alpha_q)).  Retaining only the outcomes in which
(A_p) occurs gives

\[
\Pr(\text{factor})
\ge \alpha_p(1-\alpha_q)+\mu_{a,b}\alpha_p\alpha_q
=\alpha_p\bigl(1-(1-\mu_{a,b})\alpha_q\bigr)
\ge\mu_{a,b}\alpha_p.
\]

Together with (\mu_{a,b}\ge1/2) and

\[
\max(\alpha_p,\alpha_q)=\frac1{\min(r_p,r_q)},
\]

this proves (5).  If (\min(r_p,r_q)\le R), independent fresh trials have
success probability at least (1/(2R)).  Their stopping time is geometric,
so termination is almost sure and the expected number of trials is at most
(2R).  If either (s_p\mid W) or (s_q\mid W), the associated residual is
(1), and the expected number of trials is at most two.

Every returned value is explicitly checked to be a gcd strictly between
(1) and (N).  Thus the routine is Las Vegas: it never returns an incorrect
factor.

For completeness, exact uniform sampling from the unit group needs no
factorization.  Sample uniformly from (1,\ldots,N-1), compute the gcd with
(N), and reject nonunits.  For distinct odd primes,

\[
\frac{\varphi(N)}{N-1}=\frac{(p-1)(q-1)}{pq-1}\ge\frac12,
\]

because, after ordering (p\ge3,q\ge5),
(2(p-1)(q-1)-(pq-1)=(p-2)(q-2)-1\ge0).  Hence the expected sampling cost
is constant.  A nonunit gcd could instead be returned immediately, which can
only improve the algorithm, but rejection preserves the exact trial formula
above.

Let (L) be the bit length of (W).  Then (E) has (O(n+L)) bits.
Forming (E), counting its trailing zero bits, modular exponentiation by
square-and-multiply, the at most (v+1=O(n+L)) chain steps, all gcds, and all
random-bit generation take bit complexity polynomial in (n+L); modular
intermediates remain reduced modulo (N) and have (O(n)) bits.  If
(L\le Q_1(n)) and (R\le Q_2(n)) for fixed numerical quasipolynomial
bounds, then

\[
2R\,\operatorname{poly}(n+L)
\]

is again bounded by (2^{C(\log_2(n+1))^k}) for fixed (C,k).  This verifies
the claimed numerical-quasipolynomial Las Vegas reduction, conditional on
the stated (W) and residual bound.  It does not construct such a (W).

## 4. Two-adic specializations

If (e_p=e_q=e), write

\[
p=1+2^e A,\qquad q=1+2^e B
\]

with (A,B) odd.  Then

\[
N-1=2^e(A+B+2^eAB),
\]

and the parenthesized quantity is even.  Hence
(v_2(N-1)\ge e+1), so (v=v_2(E)\ge e+1) and
(h_p=h_q=e).  Substitution in the exact law gives

\[
\mu_{e,e}
=1-\frac{4^e+2}{3\,4^e}
=\frac23(1-4^{-e}),
\]

which proves (6).

If (e_p<e_q), write

\[
p=1+2^{e_p}A,\qquad q=1+2^{e_q}B
\]

with (A,B) odd.  Now

\[
N-1=2^{e_p}
\left(A+2^{e_q-e_p}B+2^{e_q}AB\right).
\]

The parenthesized quantity is odd, so
(v_2(N-1)=e_p).  With (w=v_2(W)), this yields

\[
v=e_p+w,\qquad h_p=e_p,\qquad
h_q=\min(e_q,e_p+w),
\]

which proves (7).  Here (h_q\ge e_p).  As (w) increases, (h_q) is
nondecreasing, while in

\[
\mu_{e_p,h_q}
=1-\frac{4^{e_p}+2}{3\,2^{e_p+h_q}}
\]

the failure term is nonincreasing.  Extra factors of two in (W) therefore
can only increase, in the non-strict sense, the conditional Miller success
probability.

## 5. Extension to several primes and repeated prime powers

Let

\[
N=\prod_{i=1}^k p_i^{c_i},\qquad k\ge2,
\]

be odd.  Uniform units modulo (N) have independent, uniform CRT components
in the groups ((\mathbb Z/p_i^{c_i}\mathbb Z)^\times).  Reduction of such a
component modulo (p_i) is uniform in (\mathbb F_{p_i}^\times).

Define (A_i) by (x^E=1\bmod p_i).  From

\[
d_i=\gcd(N-1,p_i-1),\qquad
\gcd\left(\frac{N-1}{d_i},\frac{p_i-1}{d_i}\right)=1,
\]

the same cyclic-group count as in Section 1 gives

\[
\Pr(A_i)=
\frac{\gcd(E,p_i-1)}{p_i-1}
=\frac{\gcd(W,s_i)}{s_i}
=\alpha_i.
\]

The events (A_i) are independent.

Condition now on (g=N).  This is exactly the condition
(x^E=1\bmod p_i^{c_i}) for every (i).  For odd (p_i), the unit group
modulo (p_i^{c_i}) is cyclic and has order
(p_i^{c_i-1}(p_i-1)).  Its two-primary part consequently has order
(2^{v_2(p_i-1)}).  Repeating the conditioned-torsion argument shows that
(z_0=x^u) has an independent order label (J_i) with distribution
(P_{h_i}), where

\[
h_i=\min(v_2(p_i-1),v_2(E)).
\]

Reduction modulo (p_i) is injective on two-power torsion because its kernel
has odd order.  Thus an element of two-power order is (1) or (-1) modulo
(p_i) exactly when it is (1) or (-1) modulo (p_i^{c_i}).  It follows
that a chain gcd contains the full prime power (p_i^{c_i}) precisely at the
corresponding (1) or (-1) stage.

If the labels (J_i) are not all equal, take their minimum (j).  At index
(j), every component with label (j) is (1), while every component with
larger label is not (1).  The minus gcd therefore contains a nonempty proper
subset of the prime-power components and is a proper factor.  If all labels
are equal, all local components encounter (-1) and then (1) simultaneously;
all tested gcds are (1) or (N).  Hence the exact conditional failure and
success probabilities are

\[
1-\mu_{\boldsymbol h}
=\sum_{j\ge0}\prod_{i=1}^kP_{h_i}(j),\qquad
\mu_{\boldsymbol h}
=1-\sum_{j\ge0}\prod_{i=1}^kP_{h_i}(j).
\]

For any two indices, the probability that all (k) labels agree is at most
the probability that those two labels agree.  The two-label computation in
Section 2 bounds the latter by (1/2).  Therefore
(\mu_{\boldsymbol h}\ge1/2), proving (8).

The probability that none of the (A_i) occurs is
(\prod_i(1-\alpha_i)), and the probability that all occur is
(\prod_i\alpha_i).  If a nonempty proper subset occurs, the initial gcd is
proper.  Conditional on all (A_i), repeated prime powers create two cases:
the initial gcd can already be proper because some congruence does not lift
to the full (p_i^{c_i}), or it equals (N), after which the chain succeeds
with exact conditional probability (\mu_{\boldsymbol h}).  The success
probability inside the all-(A_i) event is consequently at least
(\mu_{\boldsymbol h}).  This gives

\[
\Pr(\text{factor})
\ge 1-\prod_i(1-\alpha_i)
 -(1-\mu_{\boldsymbol h})\prod_i\alpha_i.
\]

If every (c_i=1), all (A_i) occur exactly when (g=N), so no early
partial-power success is possible and the displayed inequality is equality.

Finally, let (m=\max_i\alpha_i), attained at index (t), and put
(B=\prod_{i\ne t}\alpha_i).  Among the already counted successful events
are (A_t) together with not all other (A_i), and all (A_i) followed by
conditional Miller success.  Their total probability is

\[
m(1-B)+\mu_{\boldsymbol h}mB
=m\bigl(1-(1-\mu_{\boldsymbol h})B\bigr)
\ge \mu_{\boldsymbol h}m
\ge\frac12m.
\]

This proves the second inequality in (9).

## 6. Exact remaining obligation

For the semiprime reduction, the exact formula shows that the random trial
needs only

\[
\max(\alpha_p,\alpha_q)
=\frac1{\min(r_p,r_q)}
\]

to be inverse-quasipolynomial.  Thus divisibility (s_p\mid W) or
(s_q\mid W) is sufficient but not necessary; a quasipolynomial remaining
residual already suffices.  Conversely, the exact probability is at most
(\alpha_p+\alpha_q), so the Miller randomness does not remove the need for
deterministic progress encoded in these residuals.

What is not proved is an efficient, uniform construction of such a public
(W) for every input without knowing (p) or (q).  I read the phrase
“exact unresolved task” as the remaining source problem for this reduction,
not as a claim that every possible factoring algorithm must construct this
kind of word.
