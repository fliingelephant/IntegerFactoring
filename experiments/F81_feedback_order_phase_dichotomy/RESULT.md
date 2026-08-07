# F81 — feedback subgroup gain has an order branch and a phase branch

**Status:** proof-only candidate. No research computation was run. This is an
exact one-block classification and a polynomial smooth-order decoder. It is
not an all-input feedback law or a factoring algorithm.

## 1. Closest prior result and material difference

P84 gives the exact projection-kernel gate after subgroup expansion, but its
useful cancellation word remains hidden. F80 shows one fixed case in which a
feedback descendant is exposed by a smooth power. F79 shows that fixed mixed
word menus can miss a maximal abstract expansion.

The present result separates two mechanisms that require different
algorithms:

1. **order mismatch:** the new block alone has different orders in the two
   hidden fields, so some pure power exposes a factor;
2. **phase mismatch:** the two local orders agree, so every pure power is
   synchronized, although a word mixing the new block with the old subgroup
   can still expose a factor.

It also gives a polynomial exponent bank that is complete for the first
branch whenever at least one local order has polynomially bounded full
prime-power divisors.

## 2. Exact pure-power gate and density

Let

\[
N=pq
\]

for distinct odd primes, let \(u\in(\mathbb Z/N\mathbb Z)^\times\), and put

\[
r_p=\operatorname{ord}_p(u),
\qquad
r_q=\operatorname{ord}_q(u),
\qquad
r=\operatorname{lcm}(r_p,r_q)=|\langle u\rangle|.
\]

### Theorem 1

The cyclic subgroup \(\langle u\rangle\) contains a positive separator if
and only if

\[
\boxed{r_p\ne r_q}.
\]

Its exact positive-separator count and uniform density are

\[
\boxed{\frac r{r_p}+\frac r{r_q}-2},
\qquad
\boxed{\frac1{r_p}+\frac1{r_q}-\frac2r}.
\]

For every public exponent \(E\ge1\),

\[
\boxed{
1<\gcd(u^E-1,N)<N
\iff
(r_p\mid E)\mathbin{\mathrm{xor}}(r_q\mid E).
}
\tag{1}
\]

If \(r_p=r_q\), pure powers also synchronize the negative sign: \(u^E=-1\)
in one hidden field exactly when it is \(-1\) in the other. Thus neither
direct sign gcd can succeed on any pure power.

### Proof

The exponents are residues modulo \(r\). The \(p\)-identity kernel has
\(r/r_p\) exponents, the \(q\)-identity kernel has \(r/r_q\), and their
intersection is the one global-identity exponent. Their symmetric difference
has the displayed size.

If \(r_p=r_q\), the two kernels coincide. If the orders differ, one of the
two order values is not divisible by the other or is a proper divisor of the
other. Taking the appropriate one as an exponent gives identity in exactly
one component. This also proves (1).

When the common order is even, the unique exponent giving local \(-1\) is
the common residue \(r_p/2=r_q/2\); when it is odd, neither local cyclic
subgroup contains \(-1\). Hence the negative signs also synchronize.
\(\square\)

## 3. A complete polynomial bank for the smooth part of the order branch

For a positive integer \(a\), define its largest prime-power divisor by

\[
\sigma(a)
=
\max_{\ell^e\mid a}\ell^e,
\]

where \(\ell\) ranges over primes, \(e\ge1\), and set \(\sigma(1)=1\).
Let

\[
M_B=\operatorname{lcm}(1,\ldots,B).
\]

Then

\[
\boxed{a\mid M_B\iff \sigma(a)\le B.}
\tag{2}
\]

The single smooth ladder \(M_B\) is not complete for unequal smooth orders.
For example, orders \(5\) and \(10\) have the same threshold
\(\sigma=5\): \(M_B\) kills neither before \(B=5\), then kills both.

Define the punctured lcm bank

\[
\mathcal E_B
=
\{M_B\}
\cup
\left\{
\frac{M_B}{\ell^j}:
\ell\le B\text{ prime},\
1\le j\le\lfloor\log_\ell B\rfloor
\right\}.
\tag{3}
\]

### Theorem 2

There is an exponent \(E\in\mathcal E_B\) for which (1) succeeds if and only
if

\[
\boxed{
r_p\ne r_q
\quad\text{and}\quad
\min\{\sigma(r_p),\sigma(r_q)\}\le B.
}
\tag{4}
\]

The bank has at most \(B+1\) exponents. For
\(B=\operatorname{poly}(\log N)\), constructing the bank, performing all
modular powers, and taking all gcds has deterministic polynomial bit
complexity.

### Proof

Every member of \(\mathcal E_B\) divides \(M_B\). If neither local order
divides \(M_B\), neither can divide any bank exponent. If the orders are
equal, no exponent separates them. This proves necessity.

For sufficiency, first suppose exactly one order divides \(M_B\). Then
\(E=M_B\) succeeds. Otherwise both orders divide \(M_B\) and are unequal.
Choose a prime \(\ell\) at which their valuations differ, say

\[
v_\ell(r_p)=a<b=v_\ell(r_q).
\]

Put \(e=v_\ell(M_B)=\lfloor\log_\ell B\rfloor\). Since
\(b\le e\), the bank contains

\[
E=M_B/\ell^{e-a}.
\]

Its \(\ell\)-valuation is \(a\), while every other prime valuation remains
that of \(M_B\). Hence \(r_p\mid E\) and \(r_q\nmid E\), so (1) succeeds.

The number of pairs \((\ell,j)\) in (3) is the number of prime powers at
most \(B\), which is at most \(B\). Also \(M_B\le B!\), so its bit length is
\(O(B\log B)\). Elementary prime enumeration, lcm construction, division,
modular exponentiation, and gcd evaluation are polynomial in \(B\) and
\(\log N\). \(\square\)

For the F80 descendant \(u=5\) at

\[
N=4033=37\cdot109,
\]

the exact local orders are

\[
r_{37}=36,
\qquad
r_{109}=27.
\]

Indeed, P78 gives \(5=2^{23}\pmod{37}\) with
\(\operatorname{ord}_{37}(2)=36\), so the first order is \(36\). Modulo
\(109\),

\[
5^9=63\ne1,
\qquad
5^{27}=63^3=1,
\]

so the second order is \(27\). Therefore

\[
\sigma(36)=9,
\qquad
\sigma(27)=27.
\]

The unpunctured member \(M_9=2520\) already separates them, exactly as in
F80.

## 4. Maximal expansion can be purely phase-based

The order branch does not cover all useful feedback expansion. Let \(L>2\)
be prime and work additively in

\[
C_L\times C_L=\mathbb F_L^2.
\]

Put

\[
g=(1,1),
\qquad
H=\langle g\rangle,
\qquad
z=(a,b),
\]

where \(a,b\) are distinct and nonzero.

Both local coordinates of \(z\) have exact order \(L\). Therefore every pure
power \(Az=(Aa,Ab)\) has either two zero coordinates or none. No pure power
is a separator, even with an unbounded or adaptive exponent schedule.

Nevertheless,

\[
\det
\begin{pmatrix}
1&a\\
1&b
\end{pmatrix}
=b-a\ne0,
\]

so

\[
\langle H,z\rangle=\mathbb F_L^2.
\]

The mixed cancellation word

\[
z-ag=(0,b-a)
\]

is a separator. In an odd-order local realization, \(-1\) is outside the
modeled subgroup, so the negative sign gives no hidden pure-power escape.

This is a maximal **phase-only** expansion: subgroup gain is real, but local
order data of the new generator is perfectly synchronized. The needed
operation is a mixed word that cancels the old subgroup coordinate, not a
power contraction.

## 5. Algorithmic consequence and remaining gap

After a feedback split exposes a new public block \(u\), the next operation
must branch.

- If its hidden local orders differ and at least one satisfies
  \(\sigma(r)\le B\) for polynomial \(B\), the factor-free bank (3) is
  complete.
- If its local orders agree, no pure-power method can work. Any success in
  the enlarged subgroup must use an old-subgroup cancellation word or a
  different integer-refinement or square-class operation.

The first condition is executable but hidden. Feedback has not been proved
to produce a block satisfying it with inverse-polynomial probability. The
second branch contains a hidden phase or discrete-log alignment, and no
public polynomial selector is known.

The phase example is abstract. It is not a canonical-inverse integer family
and proves no computational lower bound. The punctured bank is a
Pollard-style prime-power-bounded order decoder, not a new source of such
orders. Thus the result changes the correct post-feedback algorithm, but it
does not give an all-input polynomial-time factorer.
