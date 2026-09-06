# Proof of F221

## 1. Integer-specific local collapse

Work first modulo `p`.  Since `N=pq`, Frobenius gives, for every field
element `y`,

\[
y^N=y^{pq}=(y^p)^q=y^q\pmod p.
\tag{1}
\]

For `x=ac`, with `a` a unit, this yields

\[
\begin{aligned}
H_a(ac)
&\equiv (a(c+1))^q-(ac)^q-a\\
&=a^q\bigl((c+1)^q-c^q\bigr)-a\\
&=a\left(a^{q-1}D_{q,p}(c)-1\right)
\pmod p.
\end{aligned}
\tag{2}
\]

The same calculation modulo `q` gives

\[
H_a(ac)
\equiv
a\left(a^{p-1}D_{p,q}(c)-1\right)
\pmod q.
\tag{3}
\]

These identities are where the factorization-specific information enters.

## 2. The exact root coset

The multiplicative group `F_p^times` is cyclic of order `p-1`.  The
homomorphism

\[
\psi_p:z\longmapsto z^{q-1}
\]

has kernel size

\[
|\ker\psi_p|=\gcd(p-1,q-1)=d.
\tag{4}
\]

Fix `c_p`.  Because `a` is a unit, (2) vanishes if and only if

\[
a^{q-1}D_{q,p}(c_p)=1.
\tag{5}
\]

If `D_(q,p)(c_p)=0`, there is no solution.  Otherwise (5) is

\[
\psi_p(a)=D_{q,p}(c_p)^{-1}.
\tag{6}
\]

Equation (6) has no solution when its right side is outside the image.  If
it has one solution `a_0`, its complete solution set is exactly

\[
a_0\ker\psi_p,
\]

and has `d` elements.  Hence the conditional local-zero probability is
exactly (2) of the statement.  Interchanging `p,q` proves the same assertion
modulo `q`.

For uniform `a mod N`, CRT makes `a mod p` and `a mod q` independent and
uniform.  Once the global value `c` is fixed, the two local conditions depend
on these separate coordinates.  Thus they are independent.  A gcd is proper
exactly when one local value is zero and the other is nonzero.  Its
probability is therefore

\[
\epsilon_p(1-\epsilon_q)+\epsilon_q(1-\epsilon_p)
=\epsilon_p+\epsilon_q-2\epsilon_p\epsilon_q,
\]

which proves (3).  Dropping the nonnegative final term and using
`epsilon_p <= d/(p-1)`, `epsilon_q <= d/(q-1)` proves (4).

## 3. Adaptive normalized points

Let a trial history be fixed.  The next normalized point `c` may be any
unit-valued function of that history, deterministic or randomized.  After
conditioning on the history and on `c`, a fresh uniform `a` still satisfies
the calculation above.  Thus the conditional chance of a proper individual
gcd is at most

\[
\varepsilon={d\over p-1}+{d\over q-1}.
\tag{7}
\]

For the first-hit time `tau`, a conditional union bound gives

\[
\Pr(\tau\le m)\le m\varepsilon.
\tag{8}
\]

More sharply, conditional survival at every stage is at least
`1-epsilon` when `epsilon < 1`, so induction gives

\[
\Pr(\tau>m)\ge(1-\varepsilon)^m.
\tag{9}
\]

Using the tail formula for a positive integer-valued stopping time,

\[
\mathbb E\tau
=\sum_{m\ge0}\Pr(\tau>m)
\ge\sum_{m\ge0}(1-\varepsilon)^m
=\varepsilon^{-1}.
\tag{10}
\]

If no successful point exists, the left side is infinite and the inequality
still holds.  If `epsilon >= 1`, the same claimed bound follows from
`tau >= 1 >= 1/epsilon`.  This proves Theorem A's sequential form.

## 4. Two independent uniform units

The map

\[
(a,c)\longmapsto(a,x=ac)
\]

is a bijection on the two-copy unit group.  Hence independent uniform
`(a,x)` is equivalent to independent uniform `(a,c)`.

For each of the `I_p` eligible values of `c_p`, Section 2 gives exactly `d`
values of `a_p`.  There are `(p-1)^2` local pairs, so

\[
\alpha_p={dI_p\over(p-1)^2}.
\tag{11}
\]

The formula for `alpha_q` is identical.  CRT now makes the complete local
pairs `(a_p,c_p)` and `(a_q,c_q)` independent.  Taking the XOR of their
zero events gives

\[
\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p)
=\alpha_p+\alpha_q-2\alpha_p\alpha_q.
\tag{12}
\]

This proves Theorem B.

## 5. Bounded-gap family

For any prime pair,

\[
d=\gcd(p-1,q-1)\mid(q-p).
\tag{13}
\]

P165 imports an infinite family with `q-p <= C` for one absolute constant
`C`.  On that family, (7) gives

\[
\varepsilon\le {C\over p-1}+{C\over q-1}.
\tag{14}
\]

Balance gives

\[
\sqrt{N/2}<p<\sqrt N,
\]

and therefore

\[
{1\over p-1}=2^{-n/2+O(1)}.
\tag{15}
\]

Equations (14)--(15) prove (8) of the statement.  A numerical-QP number of
trials is `2^{o(n)}`.  Combining this with (8) gives total success
probability `2^{-Omega(n)}`.  Equation (10) gives an exponential expected
trial count.  No assertion about the residue class of `N mod 4` is imported
from P165.

## 6. Uniform sampling and bit cost

One scalar evaluation uses binary modular exponentiation and has polynomial
bit complexity.  A uniform unit is sampled exactly by drawing a uniform
residue and gcd-screening it; a proper gcd is already a factor.  Conditional
on acceptance, the result is uniform in the unit group.  On distinct odd
semiprimes the acceptance probability is bounded below by an absolute
constant, so this preprocessing has polynomial expected bit and random-bit
cost.  Its rare direct factor event is also only `O(1/p+1/q)` on balanced
inputs and does not change the exponential bounded-gap conclusion.

## 7. Logical boundary

The root-coset theorem relies on a fresh uniform `a` after `c` is fixed.
For fixed `a=1`, the variable is instead a root of

\[
D_{q,p}(x)-1
\]

modulo `p`, and the kernel-size argument does not bound the number of such
`x`.  Likewise, typical nonzero values can contain joint information not
captured by their individual gcds.  No statement in this proof excludes
those channels.

F220's primary certificate also requires a public factored annihilator
`A` and a global identity `u^A=1 mod N`.  One zero of (1) is an affine
relation, not such an annihilator.  F221 therefore identifies a sparse
random source; it does not supply or refute F220's missing progress source.
