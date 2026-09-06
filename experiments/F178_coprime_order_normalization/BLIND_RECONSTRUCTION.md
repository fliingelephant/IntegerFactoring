# Blind reconstruction of F178

## Isolation and verdict

The only candidate source used for this reconstruction was `STATEMENT.md`.
Its SHA-256 digest is

```text
8a7cfbc7ea7d3fd2d0df3c31bbd540b9c3ae7a7b62dde2997b143135e5ae6ca4
```

This matches the required digest.

**Verdict: PASS.** The postprocessor and all of its local mathematical
claims reconstruct from first principles for arbitrary odd composites,
including nonsquarefree inputs. The QP claim is valid under the standard
meaning of a QP cap: (T\le \exp((\log n)^{O(1)})), uniformly in the input.
The last statement about preserving P159's named recursion bound is
necessarily conditional on that external bound, which is not specified in
the frozen statement. Structurally, this postprocessor adds only QP work at
an invocation and returns either a proper split or a terminal state, so it
does not introduce another kind of recursion.

No mathematical computation was used.

## 1. Order after the exponent (E=N^n)

Write the hidden prime-power decomposition as

\[
N=\prod_{j=1}^s R_j,
\qquad R_j=p_j^{a_j},
\qquad e_j=\operatorname{ord}_{R_j}(4).
\]

For any finite-order group element (g) of order (e),

\[
\operatorname{ord}(g^E)=\frac{e}{\gcd(e,E)}.
\]

Consequently, for (E=N^n) and (y=4^E\bmod N),

\[
f_j:=\operatorname{ord}_{R_j}(y)
=\frac{e_j}{\gcd(e_j,E)}.
\tag{1}
\]

This formula does not require a squarefree modulus.

### Every input-supported primary part is removed

Fix a rational prime (q=p_i\mid N). Since

\[
e_j\mid \varphi(p_j^{a_j})=p_j^{a_j-1}(p_j-1),
\]

there are two cases.

If (q=p_j), then

\[
v_q(e_j)\le a_j-1 < n a_j=v_q(E).
\]

If (q\ne p_j), then

\[
v_q(e_j)\le v_q(p_j-1)<n.
\]

Indeed, (q^{v_q(p_j-1)}\le p_j-1<N+1\), whereas
(q^n\ge 2^n\ge N+1). Also

\[
v_q(E)=n a_i\ge n.
\]

Thus (v_q(e_j)\le v_q(E)) for every (q\mid N). Equation (1) then gives

\[
\gcd(f_j,N)=1
\qquad(1\le j\le s).
\tag{2}
\]

This proves the coprime-order claim simultaneously for repeated prime
factors and for order factors caused by another hidden rational prime.

We will also use the following consequence. If a unit modulo (p^a) has
order (f) with (p\nmid f), then its reduction modulo (p) also has
order (f). The reduction kernel is a (p)-group, so the quotient between
the two orders is a power of (p); it must be one when (p\nmid f).

## 2. The (H=\gcd(y-1,N)) screen

If (1<H<N), then (H) is already a nontrivial proper divisor.

Suppose (H=N). Then (y=1\bmod R_j), hence (f_j=1), for every hidden
component. Let (p) be the least rational prime divisor of (N), and let
(p^a) be its component. From (f=1) and (1), its order
(e=\operatorname{ord}_{p^a}(4)) divides (E). Therefore
(d=\operatorname{ord}_p(4)) also divides (E).

But (d\mid p-1). Every prime divisor of a nontrivial (d) would be less
than (p). By the minimality of (p), no such prime divides (N), while
(E=N^n) has exactly the same rational-prime support as (N). Hence
(d=1). It follows that (p\mid 4-1=3), so (p=3). Since (N) is
composite,

\[
\gcd(3,N)=3
\]

is proper. Thus the (H=N) branch also returns a factor.

The only surviving case is (H=1). In that case no (f_j) can be one,
because (f_j=1) would imply (R_j\mid H). Together with (2), this gives

\[
f_j>1,
\qquad \gcd(f_j,N)=1
\quad\text{for every }j.
\tag{3}
\]

## 3. The lcm screen

Let

\[
\Lambda_T=\operatorname{lcm}(1,2,\ldots,T),
\qquad
J=\gcd(y^{\Lambda_T}-1,N).
\]

For a positive integer (r), define

\[
\sigma(r)=\max_{\ell\mid r}\ell^{v_\ell(r)}.
\]

The explicit factorization

\[
\Lambda_T=\prod_{\ell\le T\atop \ell\ {m prime}}
\ell^{\lfloor\log_\ell T\rfloor}
\tag{4}
\]

shows that

\[
r\mid\Lambda_T
\quad\Longleftrightarrow\quad
\sigma(r)\le T.
\tag{5}
\]

If (1<J<N), the gcd is a proper factor.

If (J=1), then no (f_j) divides (Lambda_T): otherwise
(y^{\Lambda_T}=1\bmod R_j), which would force (R_j\mid J). Equation
(5) therefore gives

\[
\sigma(f_j)>T
\qquad(1\le j\le s).
\tag{6}
\]

If (J=N), then (f_j\mid\Lambda_T) for every (j). The following
factor-first stripping procedure either exposes a factor or obtains the
exact common order.

Start with (M=\Lambda_T), retaining the factorization (4). For every prime
(ell\mid M), repeatedly compute

\[
G=\gcd(y^{M/\ell}-1,N).
\]

* If (G=N), replace (M) by (M/\ell).
* If (1<G<N), return (G).
* If (G=1), retain that copy of (ell) and continue with the next prime.

The invariant (f_j\mid M) holds for every component: a division is made
only when (y^{M/\ell}=1\bmod N). If no proper factor occurs, consider any
prime (ell\mid M) at termination. Its last failed removal had gcd one,
so no (f_j) divided the then-current (M/\ell). Later successful
divisions only make (M) smaller and do not alter the retained
(ell)-adic exponent. Since every (f_j\mid M), this forces

\[
v_\ell(f_j)=v_\ell(M)
\qquad\text{for every }j.
\]

This holds for every prime in (M), and an (f_j) has no prime outside
(M). Hence

\[
f_1=f_2=\cdots=f_s=M=:m.
\tag{7}
\]

The factorization of (m) is known because stripping only decrements the
known exponents in (4). Thus (m>n) gives the claimed factored exact
common-order state ((y,m)).

## 4. Why (m\le n) gives a factor

It remains to prove that

\[
D=\gcd(4^m-1,N)
\]

is proper when (7) holds and (m\le n).

Again choose the least rational prime divisor (p) of (N), and put
(d=\operatorname{ord}_p(4)). Since (d\mid p-1), every prime divisor of
(d) is smaller than (p) and therefore is absent from (N). Thus

\[
\gcd(d,E)=1,
\qquad
\operatorname{ord}_p(y)
=\operatorname{ord}_p(4^E)=d.
\]

On the other hand, the order of (y) modulo the component (p^a) is
(m), and (2) gives (p\nmid m). By the reduction-kernel observation in
Section 1, its order modulo (p) is also (m). Hence (d=m), so
(p\mid 4^m-1) and (D>1).

Also (e_j>C\ge n\ge m) for every hidden component. If (D=N), then
(4^m=1\bmod R_j) for every (j), which would imply (e_j\mid m), a
contradiction. Therefore

\[
1<D<N.
\tag{8}
\]

This proves the claimed factor exit, including when (N) is a single
nontrivial prime power.

## 5. Order modulo the sign subgroup

For an odd prime power (R_j), its unit group has a unique element of order
two, namely (-1). If (y) has order (f_j), its image in
(R_j^\times/\langle-1\rangle) therefore has order

\[
q_j=\frac{f_j}{\gcd(f_j,2)}.
\tag{9}
\]

Indeed, for odd (f_j), the cyclic group generated by (y) does not
contain (-1). For even (f_j), the element (y^{f_j/2}) is the unique
element of order two and equals (-1).

On the (J=1) branch, (6) and (T\ge2C) imply

\[
q_j\ge\frac{\sigma(f_j)}2
>\frac T2
\ge C.
\tag{10}
\]

Thus quotienting by sign cannot reduce a surviving local order to the old
cap (C).

## 6. Exhaustiveness of the output

The gcd (H) first returns a proper factor unless (H=1); its other
endpoint (H=N) returns the factor (3). On the (H=1) branch, the gcd
(J) has three exhaustive cases:

1. A proper (J) is a factor.
2. (J=N) leads, by factor-first stripping, either to a proper factor or
   to a factored common exact order (m). The case (m>n) returns that
   state, and (8) turns (m\le n) into a proper factor.
3. (J=1) gives, componentwise, (3), (6), and (10).

These are exactly the three stated output types. No step assumes that the
local orders are equal on the final hard branch.

## 7. Uniform deterministic QP cost

The input bit length is (\Theta(n)). Since

\[
\log_2 E=n\log_2N=O(n^2),
\]

the integer (E=N^n) has (O(n^2)) bits. It and
(y=4^E\bmod N) are computable with polynomially many bit operations by
binary powering and modular powering.

For a QP cap (T\le\exp((\log n)^{O(1)})), a deterministic sieve through
(T) costs a polynomial in (T) and gives (4) directly. No generic
integer-factorization call is involved. An elementary bound is

\[
\log_2\Lambda_T\le T\log_2T,
\]

so the exponent and its factored representation have QP size. Each modular
power and gcd costs a polynomial in (n) and in this exponent length. The
number of stripping trials is at most the total multiplicity in (4), which
is (O(T\log T)). Even the direct implementation is therefore polynomial
in (n,T,\log\Lambda_T), hence uniform deterministic QP in (n).

In the small-order exit, (m\le n), so (4^m-1) has (O(n)) bits. All
remaining arithmetic is polynomial time. The postprocessor therefore has
the claimed QP bit cost.

## 8. Exact boundary

The proof establishes only componentwise coprime local orders with a large
prime-power divisor on the (J=1) branch. It does not establish equality of
those orders, a QP-size common annihilator, a way to factor an unfactored
annihilator, or a factoring method for the final block. Accordingly, it does
not imply a deterministic or Las Vegas QP algorithm for general integer
factoring.
