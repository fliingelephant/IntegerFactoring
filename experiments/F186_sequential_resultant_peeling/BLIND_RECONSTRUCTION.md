# F186 statement-only blind reconstruction

## Source restriction, hash, and verdict

The SHA-256 digest of `STATEMENT.md` is

```text
a23b980441b75afc10dd21e82582be5a53afa1c3da0555cf71a91feb2110bacc
```

This reconstruction uses only that statement within the F186 directory.

**Verdict: VERIFIED.** The general sequential peeling theorem, its exact
order-stripping conclusion, the one-child recurrence, and the cross-resultant
corollary are all valid as stated. The recursive conclusion is conditional on
the stated enclosing complete procedure having no additional recursion-tree
volume outside the bound.

## 1. Prime-power and exponent bounds

Write the pairwise coprime hidden components as

\[
R_j=p_j^{\alpha_j}.
\]

For a unit modulo \(R_j\), its order is at most
\(\varphi(R_j)<R_j\le N\). Hence every stated local order satisfies

\[
1<g_j<N<2^n.
\]

If \(\ell^a\mid g_j\), then \(2^a\le\ell^a<2^n\), so
\(a<n\). In particular, whenever \(\ell\mid A_i\),

\[
v_\ell(A_i^n)\ge n>v_\ell(g_j).
\tag{R1}
\]

Thus the exponent \(A_i^n\) removes the complete \(\ell\)-primary part of
any current local order, not only one copy of \(\ell\).

Nothing here assumes that a component is a field or that its unit group is
cyclic. The proof uses only element orders, the strict inequality
\(\operatorname{ord}_{R_j}(x)<R_j\), gcds, and CRT across the pairwise
coprime prime powers. It therefore applies unchanged to arbitrary exponents
\(\alpha_j\), including a single repeated-prime component.

The bit-length convention also gives a strict recursive decrease. If
\(A_i>1\) and

\[
\operatorname{bitlen}(A_i)=\lceil\log_2(A_i+1)\rceil\le n-1,
\]

then \(A_i+1\le2^{n-1}<N+1\), and in fact \(A_i<N\). Thus a recursive call
on \(A_i\) has input measure at most \(n-1\). After the prescribed gcd,
\(\gcd(A_i,N)=N\) is impossible, while any value strictly between one and
`N` is already a proper factor.

## 2. Sequential support peeling

Treat a skipped value \(A_i=1\) as leaving the current element unchanged.
For the other indices, define the cumulative exponent

\[
E_i=\prod_{\substack{1\le h\le i\\A_h>1}}A_h^n.
\]

Induction in (6) gives

\[
v_i=w^{E_i}\pmod N.
\tag{R2}
\]

For any finite-order group element `x`,

\[
\operatorname{ord}(x^e)
=\frac{\operatorname{ord}(x)}
{\gcd(\operatorname{ord}(x),e)}.
\tag{R3}
\]

Consequently each step deletes exactly the prime-power parts of the current
local orders supported on \(A_i\). All surviving order primes remain primes
of the original \(g_j\), so the current orders remain coprime to `N` and
`T`-rough whenever they are nontrivial.

By list coverage, for every \(\ell^a\parallel g_j\), some \(A_i\) is
divisible by \(\ell\). Equation (R1) then shows

\[
g_j\mid E_B.
\]

Thus \(v_B=1\pmod {R_j}\) for every `j`, and therefore
\(v_B=1\pmod N\). The process must encounter an index with \(H_i=N\) by
the end of the list unless a proper factor was already returned.

The gcd test has its intended factor-first meaning even for prime powers. If
\(v_i=1\pmod {R_j}\) for some complete components but not all, then
\(\gcd(v_i-1,N)\) is proper. If a difference is divisible by only an
intermediate power of some \(p_j\), that gcd is also proper. Hence on a
no-factor branch the only remaining values are:

- \(H_i=1\), which implies \(v_i\ne1\pmod {p_j}\), and hence
  \(v_i\ne1\pmod {R_j}\), for every `j`;
- \(H_i=N\), which is equivalent to \(v_i=1\pmod N\).

Therefore every retained element before the first global return has a
nontrivial local order in every component.

## 3. Why the first global return needs only one child

Let `i` be the first index with \(H_i=N\), and put \(x=v_{i-1}\). By the
definition of the update,

\[
x^{A_i^n}=v_i=1\pmod N.
\tag{R4}
\]

Thus, for every hidden component,

\[
d_j:=\operatorname{ord}_{R_j}(x)\mid A_i^n.
\tag{R5}
\]

This is the decisive sequential point. Earlier values \(A_h\) have already
acted on `x`; they need not be included in a final annihilator and need not
be factored. The one current integer \(A_i\) is sufficient.

The orders \(d_j\) are nontrivial. For \(i=1\), this is an initial
hypothesis. For \(i>1\), first-global-return and the absence of a prior
factor give \(H_{i-1}=1\), which rules out \(x=1\) in every hidden
component. Each \(d_j\) divides the original \(g_j\), so it is coprime to
`N`, is `T`-rough, and is greater than `T`.

Recursively factoring the single smaller integer \(A_i\) supplies the
complete factorization of

\[
M=A_i^n.
\]

Equation (R5) is now a public, fully factored common multiple of all current
local orders.

## 4. Exact factor-first order stripping

Start with the pair `(x,M)`. For every rational prime \(r\mid M\), repeatedly
compute, while \(r\mid M\),

\[
G=\gcd\bigl(x^{M/r}-1,N\bigr).
\tag{R6}
\]

There are three cases.

1. If \(1<G<N\), return the proper factor.
2. If \(G=N\), then \(x^{M/r}=1\pmod {R_j}\) for every `j`; hence every
   \(d_j\mid M/r\). Replace \(M\) by \(M/r\) and continue.
3. If \(G=1\), then no \(d_j\) divides \(M/r\). Indeed, divisibility for
   one `j` would give equality modulo the complete \(R_j\), causing
   \(p_j\mid G\). Since every \(d_j\mid M\), it follows that
   \[
   v_r(d_j)=v_r(M)
   \qquad\text{for every }j.
   \tag{R7}
   \]
   Stop stripping this prime.

The invariant \(d_j\mid M\) is preserved whenever case 2 changes `M`.
After all primes are processed, (R7), together with complete removal of any
superfluous prime powers through case 2, proves

\[
d_j=M\qquad(1\le j\le s).
\]

Thus the surviving value of `M` is one exact common local order. It is
greater than `T` because it is one of the nontrivial `T`-rough current
orders. This proves the alternative in (7).

Partial equality inside a prime-power component never creates an erroneous
stripping decision: it produces a proper gcd and takes the factor branch.
Only gcd `N` authorizes a division of `M`, and only gcd one authorizes the
common valuation conclusion.

## 5. One-bit, one-child recursion

The procedure stops immediately after invoking the recursive factorization
of the first global-return value. Hence it creates at most one direct
recursive child. Its input measure is

\[
n_i=\operatorname{bitlen}(A_i)\le n-1.
\]

Under the stated enclosing-procedure condition, worst-case cost therefore
satisfies

\[
\mathcal T(n)\le\mathcal T(n-1)+Q(n).
\]

Iterating to the finite recursion base and using that `Q` is nondecreasing
gives

\[
\mathcal T(n)
\le\mathcal T(n_0)+\sum_{r=n_0+1}^{n}Q(r)
\le\mathcal T(n_0)+nQ(n).
\tag{R8}
\]

If

\[
Q(n)\le2^{C(\log_2(n+1))^d}
\]

for fixed constants, then

\[
nQ(n)
=2^{\log_2n+C(\log_2(n+1))^d}
=2^{(\log n)^{O(1)}}.
\]

Thus losing only one input bit is harmless when there is only one recursive
child per node. The same inequality would not control a recursion tree with
additional uncompensated children, exactly as the statement warns.

## 6. Cross-resultants are nonzero

Let

\[
d=\epsilon-\delta.
\]

The separated menus give

\[
3\le d\le2L+1,
\qquad d+1\le2L+2\le2^\lambda.
\tag{R9}
\]

Translate the variable by \(Y=X+\delta\). The two cross polynomials become
one of

\[
Y,\quad Y^k-1,
\qquad
Y+d,\quad (Y+d)^l-1.
\]

They have no common complex root in all four index cases.

- For \(k=l=0\), their roots differ by `d`.
- For \(k=0,l\ge1\), a common root would give \(d^l=1\), impossible for
  \(d\ge3\). The case \(k\ge1,l=0\) is symmetric up to sign.
- For \(k,l\ge1\), a common root would give complex numbers `Y` and
  \(Y+d\), both of absolute value one. Their distance would be `d`, but two
  points on the unit circle have distance at most two.

The polynomials are monic integer polynomials. Absence of a common complex
root makes every resultant a nonzero integer, and taking its absolute value
makes every listed value positive. This also proves that a zero resultant
cannot enter the peeling list.

## 7. Exact resultant bit bound

Put

\[
S=K(1+K\lambda).
\]

We prove \(0<A_i<2^S\), which implies
\(\operatorname{bitlen}(A_i)\le S\).

For \(k=l=0\), the resultant has absolute value `d`, which is less than
\(2^\lambda\) and hence less than \(2^S\).

For \(k=0,l\ge1\), evaluation at the root `Y=0` gives

\[
A_i=d^l-1<2^{l\lambda}\le2^S.
\]

For \(k\ge1,l=0\), evaluation, or the product over the `k`-th roots of
unity, gives an absolute value at most \(d^k+1\). Since \(d<2^\lambda\),

\[
d^k+1<2^{1+k\lambda}\le2^S.
\]

Finally take \(k,l\ge1\). For every \(k\)-th root of unity \(\zeta\),

\[
|\zeta+d|\le d+1\le2^\lambda
\]

and therefore

\[
| (\zeta+d)^l-1 |
<2(d+1)^l
\le2^{1+l\lambda}.
\]

The monic-root formula for the resultant gives

\[
A_i
=\prod_{\zeta^k=1}|(\zeta+d)^l-1|
<2^{k(1+l\lambda)}
\le2^{K(1+K\lambda)}=2^S.
\tag{R10}
\]

All inequalities are strict before the final power of two. Since \(A_i\)
is an integer, \(A_i<2^S\) implies \(A_i+1\le2^S\), giving the asserted
bit-length bound without a missing extra bit. Under (12), this is at most
`n-1`.

There are

\[
B=L^2(K+1)^2
\]

entries. The one-bit condition gives \(K\le n-1\), while numerical-QP `L`
has \(\lambda=(\log n)^{O(1)}\). Dense construction of each degree-at-most
`K` resultant has cost polynomial in `K` and its coefficient bit lengths.
Thus list size, total output length, and deterministic construction cost are
all numerical QP in `n`.

## 8. Double extinction gives exact support coverage

For a shift \(\delta\), define the integer filter value

\[
C_\delta
=\prod_{k=0}^{K}F_{\delta,k}(N)
=(N+\delta)\prod_{k=1}^{K}\bigl((N+\delta)^k-1\bigr).
\]

For a menu \(\mathcal S\), put

\[
P_\mathcal S=\prod_{\delta\in\mathcal S}C_\delta.
\]

If its filter is globally extinct on the original unit `w`, then

\[
w^{P_\mathcal S^n}=1\pmod {R_j},
\qquad g_j\mid P_\mathcal S^n
\tag{R11}
\]

for every `j`. Therefore every rational prime \(\ell\mid g_j\) divides
\(P_\mathcal S\). It follows that, for some menu shift and some
\(0\le k\le K\),

\[
F_{\delta,k}(N)=0\pmod\ell.
\tag{R12}
\]

Assume both separated menus are globally extinct on the same original unit.
For each \(\ell\mid g_j\), choose \((\delta,k)\) from the first menu and
\((\epsilon,l)\) from the second using (R12). The reduction of `N` modulo
\(\ell\) is then a common root of

\[
F_{\delta,k},\qquad F_{\epsilon,l}
\]

over \(\mathbb F_\ell\). Hence

\[
\ell\mid
\operatorname{Res}_X(F_{\delta,k},F_{\epsilon,l}).
\tag{R13}
\]

That resultant is nonzero by Section 6 and appears in the public list.
Thus the list covers every rational prime in every local order, exactly as
required by the general peeling theorem. The `k=0` entries are essential:
they include the cases where \(\ell\mid N+\delta\), before a multiplicative
order is defined.

The same calculation also gives the surviving wide-shift condition. For
\(\ell^a\parallel g_j\), exponentiation by \(P_\mathcal S^n\) deletes the
whole \(\ell^a\) part exactly when \(\ell\mid P_\mathcal S\). If it
survives, then for every \(\delta\in\mathcal S\),

\[
\ell\nmid N+\delta,
\qquad
\ell\nmid (N+\delta)^k-1\quad(1\le k\le K).
\]

Equivalently,

\[
\operatorname{ord}_\ell(N+\delta)>K.
\]

A filter gcd equal to one ensures that every hidden component retains a
nontrivial local order. Those orders remain divisors of the original
`T`-rough orders and remain coprime to `N`.

## 9. Corollary trichotomy

Run the first menu filter on `w`.

- A proper gcd returns a factor.
- Gcd one returns its wide-shift-hard rough descendant.
- Gcd `N` makes the first menu globally extinct, so run the second filter
  on the same original `w`.

The second filter again returns a factor or a wide-shift-hard descendant
unless it is also globally extinct. In the double-extinction case,
Sections 6--8 verify every hypothesis of the general peeling theorem. That
theorem returns a proper factor or one fully factored exact common order
above `T`, using at most one smaller recursive child.

These cases give exactly

\[
\text{factor}
\quad\lor\quad
\text{fully factored exact common order above }T
\quad\lor\quad
\text{wide-shift-hard rough descendant}.
\]

The proof supplies no reason that the last branch must disappear. It also
does not force a non-global root. Therefore the improved recursion interface
does not turn the transition into an all-input factoring algorithm.

## Final verdict

**VERIFIED — SHA-256
`a23b980441b75afc10dd21e82582be5a53afa1c3da0555cf71a91feb2110bacc`.**

The first-global-return invariant, the single final annihilator, exact
factor-first stripping, arbitrary-prime-power handling, one-bit one-child QP
recurrence, and all F185 cross-resultant coverage and size claims withstand
independent reconstruction.
