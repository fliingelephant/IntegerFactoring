# Proof of the F247 principal-lift carry torsor

## 1. Ordinary lift action

Modulo \(N^2\), the binomial theorem gives

\[
(a+Nt)^E
\equiv a^E+NEa^{E-1}t.
\tag{1}
\]

Subtract the fixed least residue \(x=\langle a^E\rangle_N\), divide the
remaining congruence by \(N\), and reduce modulo \(N\). This gives

\[
K_t=K_0+Ea^{E-1}t\pmod N.
\]

Because both \(E\) and \(a\) are units modulo \(N\), its slope is a unit.
The affine map is therefore a permutation of \(\mathbb Z/N\mathbb Z\).
All lifts reduce to the same \(a\), so every calculation performed only in
\(\mathbb Z/N\mathbb Z\) has exactly the same transcript. Uniformity after
conditioning follows from the permutation law. Replacing the fixed section
\(x\) by the signed section \(\sigma\) changes only the intercept, which
proves (3).

## 2. Exact probability counts

Among the \(N=pq\) residue classes, exactly \(q-1\) are divisible by \(p\)
but not \(q\), and exactly \(p-1\) are divisible by \(q\) but not \(p\).
The zero class is the unique class divisible by both. The remaining
\((p-1)(q-1)\) classes are units. This proves (4)--(6).

For every fixed \(L\), translation by \(-L\) permutes the residue classes
modulo \(N\). Thus \(K-L\bmod N\) is uniform, even after a prior history
has fixed \(L\). This proves (7) in its history-wise form. If \(L\) is also
uniform, each difference value has exactly \(N\) ordered preimages. Exact
equality then has probability \(1/N\). Replacing this value by one does not
change the proper gcd event.

For an exterior prime \(\ell\), the count of multiples of \(\ell\) in
\(\{0,\ldots,N-1\}\) is \(\lceil N/\ell\rceil\). Removing zero leaves
\(\lfloor(N-1)/\ell\rfloor\) positive multiples. This proves (8)--(9).

When \(N=s\ell+r\), there are

\[
s+1\quad\text{representatives in }r\text{ residue classes}
\]

and

\[
s\quad\text{representatives in }\ell-r\text{ residue classes}.
\]

Therefore

\[
\Pr(K\equiv L\pmod\ell)
={r(s+1)^2+(\ell-r)s^2\over N^2}.
\]

Subtracting the exact-equality probability \(1/N\) gives

\[
{\ell s(s-1)+2rs\over N^2}.
\]

To verify the upper bound in (10), multiply the numerator by \(\ell\).
The difference from \(N^2\) is

\[
\ell^2s+r^2\ge0.
\]

For the history-wise form, condition on the fixed value \(L\). Exactly
\(c_\ell(L)\) possible values of the new uniform \(K\) share its residue
class modulo \(\ell\). One is \(K=L\). Hence the unequal-collision
probability is exactly \((c_\ell(L)-1)/N\). Since

\[
c_\ell(L)-1\le\lfloor N/\ell\rfloor,
\]

this probability is at most \(1/\ell\). This proves (11).

## 3. Signed return and local order lifting

Fix \(r\in\{p,q\}\). Since \(N/r\) is a unit modulo \(r\),

\[
r\mid C
\quad\Longleftrightarrow\quad
NC=0\pmod {r^2}.
\]

This proves (12).

Let \(m=\operatorname{ord}_r(a)\). The kernel of reduction from units
modulo \(r^2\) to units modulo \(r\) has order \(r\). Hence the order of
the chosen lift modulo \(r^2\) is either \(m\) or \(rm\).

If the order is \(m\), then \(a^E=1\) modulo \(r^2\) for a positive
return. For a negative return, \(m\) is even and
\(E=m/2\pmod m\). The unique element of order two modulo the odd prime
square is \(-1\), so the signed return also lifts.

Conversely, suppose the order is \(rm\). A positive lifted return would
give \(rm\mid E\). A negative lifted return would give
\(E=rm/2\pmod {rm}\). Either condition implies \(r\mid E\), contrary to
the assumption. This proves (13).

## 4. The canonical order-two witness

For even \(E\), another binomial expansion gives

\[
(N-1)^E=(-1+N)^E\equiv1-EN\pmod {N^2}.
\]

This proves (14). Since \(-(N-1)W=W\pmod N\), equation (15) follows.
Every power of \(-1\) modulo \(N\) is the same global sign in every hidden
component. A gcd against either sign is therefore one or \(N\), never a
proper factor.

## 5. Exact norm-one lift fibre

Work in the quadratic algebra of the statement. Let \(V\) be another lift
of the same residue as \(U\). Since \(U\) is a unit, there are unique
\(c,d\in\mathbb Z/N\mathbb Z\) such that

\[
VU^{-1}=1+N(c+dw)\pmod {N^2}.
\]

Modulo \(N^2\),

\[
\operatorname{Nm}(1+N(c+dw))
=1+N\operatorname{Tr}(c+dw)
=1+2Nc.
\]

Both \(U\) and \(V\) have exact norm one if and only if \(2c=0\)
modulo \(N\). Because \(N\) is odd, this is equivalent to \(c=0\).
Thus (16) is the complete exact norm-one lift fibre.

Now

\[
(1+Ntw)^E=1+NEtw\pmod {N^2}.
\]

The algebra is commutative, so

\[
U_t^EX^{-1}
=U^EX^{-1}(1+NEtw)
=1+N(C_0+Etw)
\pmod {N^2}.
\]

This proves (18).

Take norms in (17). The first-order norm formula gives

\[
1=\operatorname{Nm}(U_t^E)
=\operatorname{Nm}(X)(1+N\operatorname{Tr}(C_t))
=1+N(h+\operatorname{Tr}(C_t))
\pmod {N^2}.
\]

Hence \(\operatorname{Tr}(C_t)=-h\), which is (19). The affine slope
\(E\) is a unit, so the \(w\)-coordinate is exactly uniform for uniform
\(t\). Without the norm condition, the same calculation with
\(c+dw\) gives the two-coordinate affine law stated in the packet.

## 6. Same-chain identities

For the ordinary source,

\[
(x+NK_E)^m
\equiv x^m+Nmx^{m-1}K_E
\pmod {N^2}.
\]

Substitute \(x^m=x_m+NQ_m\), compare the coefficient of \(N\), and
obtain (20).

For the torus source,

\[
U^{mE}=X_E^m(1+NmC_E)
\pmod {N^2}.
\]

Substitute

\[
X_E^m=X_{mE}(1+NQ_m)
\]

and discard the product of the two \(N\)-terms. This gives (21).

## 7. Conditional-history marker bound

At stage \(i\), fix the complete past. The chosen base, exponent, and every
earlier carry can depend on that past. By hypothesis, the new lift parameter
is uniform and its affine slope is a unit. Thus the new carry is exactly
uniform after this conditioning.

For its positive raw value, (9) gives a conditional probability less than
\(1/\ell\). For its unequal difference from any fixed earlier value, (11)
gives a conditional probability at most \(1/\ell\). Apply a union bound at
each stage, then average over the past. This proves (22) without an
independence assumption between the adaptively selected bases or exponents.

F244 supplies four exterior marker primes of size \(2^{\Omega(n)}\), while
every numerical-quasipolynomial \(T\) is \(2^{o(n)}\). Equation (22),
followed by a union bound over four markers, is \(2^{-\Omega(n)}\).
The markers divide \(p\pm1\) or \(q\pm1\), so \(p,q=2^{\Omega(n)}\) on
this family. Equations (5) and (7) show that all direct carry and difference
gcd exits also have total probability \(2^{-\Omega(n)}\) over a
quasipolynomial bank. When no marker is hit, the F244 P208 residual bound
remains exponential. Quasipolynomial repetition does not change that scale.

This argument uses only randomized lift coordinates. It says nothing about
the distinguished intercept \(K_0\), because the affine permutation law
does not imply that the intercept is uniform when the residue base varies.
This is the canonical-section gap.
