# Hostile audit of F173 high order with constant common capacity

## Verdict

**PASS for the stated narrow interface obstruction.**

The construction, length estimate, four shifted-gcd identities, ordinary
screens, two torus orientations, quotient-capacity branches, density bounds,
and exact-order contrast are mathematically valid. The result proves only
that the displayed order and capacity facts do not logically force a useful
exact common-order modulus. It does not constrain the residue selected by the
deterministic Harvey--Hittmeir algorithm.

## Repair re-audit

**Final repair verdict: PASS.**

The four specification defects from the first audit are now closed.

1. The statement and proof define the integer cap
   $T(n)=\lfloor Q(n)\rfloor$. Every lcm, scan, short bank, multiplier range,
   and capacity count uses $T(n)$. The first repair pass left one literal
   `$Q+1$` in `SELF_AUDIT.md`; that intermediate repair check failed. The
   final self-audit now correctly says `$T(n)+1$`.
2. The Harvey--Hittmeir target is explicitly $D=T(n)$ in both the statement
   and proof.
3. The statement and proof explicitly restrict every torus equality and
   signed-identity claim to the F170 joint-coordinate gcd. They expressly
   exclude one-coordinate nullity.
4. Every display delimiter in the revised statement, proof, and self-audit
   is balanced.

I re-read all three revised files. The repairs change only notation and
scope wording. They do not change the CRT construction, any order, any gcd
screen, any density, or any quantifier. No new mathematical claim or defect
was introduced.

## Frozen material audited

I read the full F173 statement, proof, self-audit, and manifest. I also read
the full F172 statement and proof that F173 strengthens. No experiment or
factor-assisted computation was run.

The final repaired F173 source hashes are:

- F173 `STATEMENT.md`:
  `0dd00f380a3aa5ddf83dbbedbe10942565b0da2ef786223c80a1fe9c08c60296`
- F173 `PROOF.md`:
  `7c5d192e49f8334cfbabe4355e2a404fbdffe103b803936a0330fa271562cdd6`
- F173 `SELF_AUDIT.md`:
  `91778d744ddd0299cca0444ae8cf9b00afe1cb925e2f02d08bbf068ec92e43c4`

The unchanged F172 inputs were:

- F172 `STATEMENT.md`:
  `d2ff244f1fb28e00ba262fdb89cd5a23b7b75954586bfb998ffd188db4a8ed9f`
- F172 `PROOF.md`:
  `b23989a19a23653dab9946dca55888384a2c4493184878a3dfac68ec9c067a21`

## 1. Attack on the two CRT classes

Take an odd prime (r>3), and let (r<u<2r) be prime. The three moduli
(3,r,u) are pairwise coprime. The residues (1,1,-1) are units in their
respective moduli. Thus the first CRT class is reduced modulo (3ru), and
Linnik applies.

The selected prime (p) is larger than both (r) and (u). If (0<p<r)
and (p\equiv1\pmod r), then (p=1). If (0<p<u) and
(p\equiv-1\pmod u), then (p=u-1), an even integer larger than two.
Neither is prime. Hence the divisibilities

\[
r\mid p-1,
\qquad
u\mid p+1
\]

are genuine large proper divisors.

For the second class, write

\[
p^2-1=2^a3^bM,
\qquad \gcd(M,6)=1.
\]

Because (p\equiv1\pmod3), one has (b\ge1). The moduli
(8,p,3^b,M) are pairwise coprime, and the residues (3,1,4,2) are units.
Thus the inherited F172 class (a_p\pmod H) is reduced. The Bertrand primes
(s,t) satisfy

\[
H<s<2H< t<4H,
\]

so they are distinct and coprime to (H). The extra residues (1\pmod s)
and (-1\pmod t) are units. Therefore the extended class modulo (Hst) is
also reduced, and Linnik applies a second time.

The condition (q\equiv1\pmod p) gives (q=1+vp). Values (v=0) and
(v=1) give (1) and the even composite (p+1>2), respectively. Hence
(v\ge2) and (q>2p). Similarly, the added residues force (q>s,t): the
only positive representative below (s) congruent to (1\pmod s) is one,
and the only one below (t) congruent to (-1\pmod t) is the even integer
(t-1>2).

No compatibility condition was smuggled in. The second CRT construction is
performed only after (p,s,t) are fixed, and all its moduli are coprime.

## 2. Attack on the four shifted gcds

The extra congruences modulo (s,t) leave (q\equiv a_p\pmod H) unchanged.
The full F172 calculation therefore survives, but it can also be checked
directly.

- If an odd prime (ell\ge5) divides either (p-1) or (p+1), then
  (ell\mid M), so (q\equiv2\pmod\ell). This excludes (ell) from the
  appropriate (q-1) or (q+1) cross-shift.
- All of the (3)-part of (p^2-1) lies in (p-1). The residue
  (q\equiv4\pmod{3^b}) makes the common (3)-part of (p-1,q-1) exactly
  (3), and (3) divides neither (p+1) nor (q+1).
- The residue (q\equiv3\pmod8) gives
  (v_2(q-1)=1) and (v_2(q+1)=2).

Consequently,

\[
\gcd(p-1,q-1)=6,
\]

\[
\gcd(p-1,q+1)\in\{2,4\},
\qquad
\gcd(p+1,q-1)=2,
\]

and

\[
\gcd(p+1,q+1)\in\{2,4\}.
\]

At the same time, the new conditions give (s\mid q-1) and
(t\mid q+1). Since (r,u<p<H<s<t), the four selected primes are distinct.

## 3. Attack on the Linnik-to-input-length link

Linnik gives, with absolute constants,

\[
p\le C_0(3ru)^{L_0}=r^{O(1)}
\]

because (r<u<2r). The reverse bound (p>r) was proved above. Also,

\[
H=8p3^bM<8p^3,
\qquad
s,t=O(H),
\]

and the second Linnik application gives

\[
q\le C_1(Hst)^{L_0}=p^{O(1)}.
\]

Together with (r<p<q), these estimates imply

\[
\log N=\Theta(\log r).
\]

All implied constants are absolute. Thus one fixed (c>0) works for the
whole constructed family:

\[
r,u,s,t\ge 2^{cn}
\]

after a finite prefix. There is no circular choice involving the eventual
bit length (n). Since

\[
\log_2 Q(n)=C(\log_2(n+1))^k=o(n),
\]

all four selected primes eventually exceed (4Q(n)). The same comparison
shows (p,q>n^A) for every fixed (A), so the trial-hard claim is correct.

The family is infinite. The free primes (r) are unbounded, while every
corresponding (p) is larger than (r). Hence the resulting (p), and
therefore (N=pq), cannot remain in a finite set.

This reasoning supplies no balance bound. F173 correctly states that the
family is unbalanced.

## 4. Attack on the ordinary common-order and decoder claims

The two local unit groups are cyclic of orders (p-1) and (q-1). Any
element with the same exact local order (A) therefore has

\[
A\mid\gcd(p-1,q-1)=6.
\]

Conversely, CRT combines local elements of exact order six. Thus the granted
state ((g,6)) exists and is maximal.

CRT also combines local primitive roots into the supplied witness (a).
Let

\[
A_p=(p-1)/6,
\qquad
A_q=(q-1)/6.
\]

The odd primes (r,s) survive division by six, so (r\mid A_p) and
(s\mid A_q).

### Absolute and relative screens

Since (r,s>Q), neither selected prime divides
(Lambda_Q=\operatorname{lcm}\{1,\ldots,\lfloor Q\rfloor\}). Therefore
neither local primitive order divides (Lambda_Q), and

\[
\gcd(a^{\Lambda_Q}-1,N)=1.
\]

The local order of (a^6) is exactly (A_p) and (A_q), respectively.
For every integer (1\le e\le Q), neither order divides (e), since it
contains a prime larger than (Q). Hence (a^{6e}) is nonidentity in both
fields, and every relative-return gcd is one.

### Quotient fingerprints

In each cyclic local group, the order-six subgroup is unique. The image of a
primitive generator in the quotient by that subgroup has order the ambient
order divided by six. Equivalently, its P154 fingerprint (a^6) has exact
orders (A_p,A_q). Its first (lfloor Q\rfloor+1) powers are distinct in
both fields. Every P154 pair comparison is therefore one, and a one-generator
table with that cap reaches only the capacity branch. The certified local
sizes are at least (6(\lfloor Q\rfloor+1)); no exact quotient size follows.

### Short signed comparisons

Every equality or inverse equality among (a^i,a^j), with
(|i|,|j|\le Q), asks whether (a^h=1) for a sum or difference (h) with
(|h|\le2Q). An unsigned nonliteral hit would make (r) or (s) divide a
nonzero integer of magnitude below the selected prime.

A signed hit asks whether (a^h=-1). Since (a) is locally primitive, this
would imply that the local order divides (2h). But
(|2h|\le4Q<r,s). The same argument applies to
(a^ia^j=\pm1). Thus the natural P152-style signed pair-product screens are
one, except for the declared literal global identity.

This argument covers only the stated two-term bank. It does not cover an
arbitrary adaptive word or exponent grammar, and F173 does not claim that it
does.

## 5. Attack on every ordinary (j(N\pm1)) reduction

For (1\le j\le Q), reduction modulo the two primitive local orders gives

\[
\begin{array}{c|cc}
&N-1&N+1\\ \hline
p\text{-side}&q-1&q+1\\
q\text{-side}&p-1&p+1.
\end{array}
\]

On the (p)-side, (r\mid p-1), while the first two shifted-gcd identities
show (r\nmid q-1,q+1). On the (q)-side, (s\mid q-1), while the relevant
shifted-gcd identities show (s\nmid p-1,p+1). Also (r,s\nmid2j).
Therefore none of the four multiplied exponents is zero or a half-order in
its local cyclic group. This proves both signs of every gcd in statement
equation (12), not only the identity sign.

## 6. Attack on both torus orientations

For each (epsilon\in\{+1,-1\}), CRT supplies a unit (D_\epsilon) whose
Legendre symbols are (epsilon) at (p) and (-\epsilon) at (q). Its
Jacobi symbol is minus one. The two local norm-one groups are cyclic of orders

\[
R_{p,\epsilon}=p-\epsilon,
\qquad
R_{q,\epsilon}=q+\epsilon.
\]

Local primitive points exist, and coordinate-wise CRT gives a global point
(U_\epsilon) with both exact local orders. The maximum possible exact
common order is

\[
b_+=\gcd(p-1,q+1)\in\{2,4\},
\qquad
b_-=\gcd(p+1,q-1)=2.
\]

Local cyclicity and coordinate CRT also construct a valid common state of
that exact order. Thus the granted states are both existent and maximal.

The relevant selected primes are

\[
\begin{array}{c|cc}
&p\text{-side}&q\text{-side}\\ \hline
\epsilon=+1&r&t\\
\epsilon=-1&u&s.
\end{array}
\]

They are odd and larger than (4Q), so they survive division by
(b_\epsilon\le4). It follows that the two local orders of
(U_\epsilon^{b_\epsilon}) exceed (Q). This proves the torus absolute,
relative, fingerprint-distinctness, short-power, and capacity claims by the
same divisibility argument as in the ordinary channel.

For precision, the equality gcd here must be the F170 test

\[
\gcd(N,y_0-z_0,y_1-z_1).
\]

It returns a proper factor exactly when the two points are equal in one local
torus and unequal in the other. Nonidentity in both local tori makes the
identity comparison equal to one. F173 does not rule out a factor from a
stronger test that takes separate gcds of individual coordinate differences.

## 7. Attack on all eight torus public-exponent cases

Reduction modulo the corresponding local torus order gives exactly the
table in the proof:

\[
\begin{array}{c|cc}
&N-1&N+1\\ \hline
\epsilon=+1, p\text{-side}&q-1&q+1\\
\epsilon=+1, q\text{-side}&-(p+1)&-(p-1)\\
\epsilon=-1, p\text{-side}&-(q+1)&-(q-1)\\
\epsilon=-1, q\text{-side}&p-1&p+1.
\end{array}
\]

For example, on the (q)-side with (epsilon=+1), one reduces modulo
(q+1), so (q\equiv-1) and (pq\mp1\equiv-p\mp1). The other rows follow
in the same way.

In each row, the selected prime in the preceding table divides the local
torus order and divides neither displayed cross-shift. The exact shifted-gcd
identities prove this. It also divides neither (j) nor (2j). Thus no
multiplied exponent is zero or half the local order. Every F170
joint-coordinate screen against (+1) or (-1) is one in all eight cases.

## 8. Attack on residual coprimality and density

Writing (p-1=6A_p) and (q-1=6A_q), exact equality
(gcd(p-1,q-1)=6) gives (gcd(A_p,A_q)=1). Moreover,

\[
\operatorname{ord}_p(a^{N-1})
=\frac{p-1}{\gcd(p-1,N-1)}=A_p,
\]

and similarly the (q)-side order is (A_q).

For a uniform exponent modulo the resulting global period (A_pA_q), the
two coordinates are uniform on the full product because the local orders are
coprime. The probability that exactly one coordinate is identity is

\[
\frac1{A_p}+\frac1{A_q}-\frac2{A_pA_q}
\le \frac1r+\frac1s
=2^{-\Omega(n)}.
\]

For the plus torus orientation,

\[
\gcd(p-1,N+1)=\gcd(q+1,N+1)=b_+,
\]

where the second equality is read after reducing (N+1) modulo (q+1).
Thus (U_+^{N+1}) has local orders
((p-1)/b_+) and ((q+1)/b_+). They are coprime and retain (r,t).

For the minus orientation, the corresponding two gcds are both (2), so
(U_-^{N+1}) has local orders ((p+1)/2) and ((q-1)/2). They are coprime
and retain (u,s). The same product-uniform calculation gives an
exponentially small identity-axis density in each torus channel.

The word "uniform" should be read as uniform over the exact global cyclic
period. This is an abstract density statement, not a claim that a QP sampler
can enumerate or identify that period.

## 9. Attack on the common-order conclusion

Every ordinary exact common order divides six. Every plus-orientation torus
common order divides (b_+\mid4), and every minus-orientation one divides
two. Hence even maximal simultaneous states satisfy

\[
\operatorname{lcm}(A_{\rm ordinary},B_+,B_-)
\mid\operatorname{lcm}(6,4,2)=12.
\]

Since (sqrt N/Q(n)=2^{\Theta(n)}), this is far below the F170 terminal
threshold. In contrast, each primitive witness has a quotient order with an
exponential selected prime in every hidden component. This establishes the
claimed separation between local capacity and an exact common modulus.

No contradiction with F170 arises. F170 is a factor-or-update theorem when
closure occurs. F173 sends the named capped tables to the nonclosing capacity
branch.

## 10. Attack on the exact (m/r) screen

For the primitive ordinary witness,

\[
m=\operatorname{lcm}(p-1,q-1)
=\frac{(p-1)(q-1)}6.
\]

The prime (r>3) divides (p-1) and does not divide (q-1). Therefore
(q-1\mid m/r). The (r)-adic valuation of (m/r) is one smaller than
that of (p-1), so (p-1\nmid m/r), even if (r^2\mid p-1). Since (a)
is primitive in both fields,

\[
\gcd(a^{m/r}-1,N)=q.
\]

Thus a supplied exact global order with complete factorization exposes the
mismatch through a standard prime-divisor screen. The plus torus channel has
the same argument with (r\mid p-1), (r\nmid q+1); the minus channel uses
(u\mid p+1), (u\nmid q-1). The exact-order contrast is correct.

## 11. Precise Harvey--Hittmeir boundary

The Harvey--Hittmeir theorem guarantees that its deterministic procedure
returns a factor, a primality outcome in the relevant version, or one
**algorithm-selected** unit whose global order exceeds the requested target.
It does not say that this unit is the hidden-factor CRT combination chosen in
F173.

F173 supplies a primitive CRT witness only to realize the same coarse
interface facts: global order above any fixed QP target, local order above the
cap after the public factor-first scan, and quotient capacity above the cap.
This is enough to refute any deduction that uses only those facts. It is not
enough to refute a deduction that uses the Harvey--Hittmeir construction,
the actual returned residue, an annihilating exponent with known
factorization, or another source-specific invariant.

Accordingly, the phrases "does not make a claim about which element the
deterministic Harvey--Hittmeir algorithm returns" and "interface obstruction"
are essential. Removing either would make the result overclaim.

If an annihilating exponent with known factorization instead permits exact
order recovery, the P150 prime-divisor screens apply. F173 explicitly
demonstrates that this stronger branch factors its family; it does not call
that branch obstructed.

## 12. Final scope check

The proof establishes an infinite, unbalanced, trial-hard semiprime family
and three supplied primitive witnesses. It does not establish:

- an output law for Harvey--Hittmeir;
- a factor-free construction of the witnesses;
- nullity of one-coordinate torus gcds;
- nullity of every adaptive QP word or exponent menu;
- inertness of cross-discriminant or exact-integer relation decoders;
- a balanced obstruction;
- a factoring lower bound.

Those exclusions are all present in the frozen statement. Subject to the
four specification repairs listed with the verdict, the proof supports every
claim it actually makes.
