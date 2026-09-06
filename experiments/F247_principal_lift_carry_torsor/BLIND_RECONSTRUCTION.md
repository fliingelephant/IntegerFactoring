# F247 blind reconstruction — principal-lift carry torsor

## Authentication, evidence boundary, and verdict

Authenticated statement SHA-256:

```text
7009dcdd153e327f32f0a09d94298d0ff4b79c7196a2228e345f442d2c356d1b
```

This reconstruction uses only the root instructions and the authenticated
`STATEMENT.md`. It does not use any proof, audit, provenance, manifest, or
other F247 artifact.

**Verdict: PASS**, with one explicit scope qualification. Equations
(1)--(22), including their conditional-history forms, reconstruct from
elementary algebra and counting. The final application to the named F244
family is conditional on the F244 interface stated in Section 8 below. No
F244 result is needed for the internal F247 theorem.

Throughout, (N) is odd and

\[
\langle z\rangle_N\in\{0,\ldots,N-1\}
\]

is the least nonnegative residue of (z) modulo (N).

## 1. Ordinary lifts

Let (a\in(\mathbb Z/N\mathbb Z)^\times), let (E\geq 1), and assume

\[
\gcd(E,N)=1.
\]

For (t\in\mathbb Z/N\mathbb Z), set (a_t=a+Nt\pmod {N^2}), and put

\[
x=\langle a^E\rangle_N.
\]

There is a unique (K_t\in\mathbb Z/N\mathbb Z) such that

\[
a_t^E\equiv x+NK_t\pmod {N^2}.
\tag{1}
\]

The binomial expansion modulo (N^2) gives

\[
(a+Nt)^E\equiv a^E+NEa^{E-1}t\pmod {N^2}.
\]

Since (a^E\equiv x+NK_0\pmod {N^2}), comparison with (1) proves

\[
\boxed{K_t=K_0+Ea^{E-1}t\pmod N.}
\tag{2}
\]

Both (E) and (a) are units modulo (N). Hence
(Ea^{E-1}\) is a unit, so (2) is a permutation of
(\mathbb Z/N\mathbb Z).

Here is the precise conditional-history statement. Let
(\mathcal H\) be the complete history before the fresh choice of (t).
Assume that (a) and (E) are (\mathcal H)-measurable and that

\[
\Pr(t=u\mid\mathcal H)=\frac1N
\quad\text{for every }u\in\mathbb Z/N\mathbb Z.
\]

Let (\mathcal T) be any transcript computed from (a_t) only through
arithmetic modulo (N), with all other choices already in
(\mathcal H). Conditional on (\mathcal H), the value
(a_t\bmod N=a\bmod N) is constant in (t); consequently
(\mathcal T) is also constant in (t). Thus

\[
\Pr(K_t=k\mid\mathcal H,\mathcal T)=\frac1N
\quad\text{for every }k\in\mathbb Z/N\mathbb Z.
\]

This is the exact sense in which fixing a complete modulo-(N) order
transcript does not bias a fresh lift carry. It does not apply if the
conditioning information depends on the high digit itself.

If a signed return is written

\[
a_t^E\equiv\sigma+NC_t\pmod {N^2},
\qquad \sigma\in\{1,-1\},
\]

the same expansion gives

\[
C_t=C_0+Ea^{E-1}t\pmod N.
\tag{3}
\]

For (\sigma=-1), the least residue modulo (N) is (N-1). Comparing
(-1+NC_t) with (N-1+NK_t) gives

\[
C_t=K_t+1\pmod N.
\]

## 2. Exact scalar probability laws

Assume in this section that (N=pq), where (p\neq q) are odd primes,
and let (K) be uniform on (\{0,\ldots,N-1\}).

There are ((p-1)(q-1)=\varphi(N)) units, so

\[
\Pr(\gcd(K,N)=1)=\frac{\varphi(N)}N.
\tag{4}
\]

The residues divisible by (p) but not (q) number (q-1); those
divisible by (q) but not (p) number (p-1). Therefore

\[
\boxed{
\Pr(1<\gcd(K,N)<N)=\frac{p+q-2}{N}.
}
\tag{5}
\]

Only (K=0) has gcd (N), and hence

\[
\Pr(\gcd(K,N)=N)=\frac1N.
\tag{6}
\]

For any fixed (L\in\mathbb Z/N\mathbb Z), translation by (L) is a
permutation. Thus

\[
\boxed{
\Pr(1<\gcd(K-L,N)<N)=\frac{p+q-2}{N}.
}
\tag{7}
\]

The same equality holds conditionally whenever a past sigma-field fixes
(L) and the new (K) is conditionally uniform given that past. Replacing
the zero residue (K-L=0) by (1) changes a gcd-(N) outcome into a
gcd-(1) outcome, so it does not change the proper-factor event in (7).

Now fix a prime (\ell), called exterior only to distinguish it from the
hidden factors, and write

\[
N=s\ell+r,\qquad 0\leq r<\ell.
\]

The multiples of (\ell) in (\{0,\ldots,N-1\}) are
(0,\ell,\ldots,\lfloor(N-1)/\ell\rfloor\ell). Their count is
(\lceil N/\ell\rceil), so

\[
\Pr(\ell\mid K)=\frac{\lceil N/\ell\rceil}{N}.
\tag{8}
\]

Define (\widehat K=K) for (K>0), and (\widehat K=1) for (K=0).
The surviving divisible values are the positive multiples of (\ell)
below (N). Consequently

\[
\Pr(\ell\mid\widehat K)
=\frac{\lfloor(N-1)/\ell\rfloor}{N}
<\frac1\ell.
\tag{9}
\]

For independent uniform (K,L), each of the first (r) residue classes
modulo (\ell) has (s+1) representatives in
(\{0,\ldots,N-1\}), and each of the other (\ell-r) classes has (s).
The number of ordered, unequal pairs in a common class is therefore

\[
r(s+1)s+(\ell-r)s(s-1)
=\ell s(s-1)+2rs.
\]

It follows that

\[
\boxed{
\Pr(K\ne L,\ K\equiv L\pmod\ell)
=\frac{\ell s(s-1)+2rs}{N^2}
\leq\frac1\ell.
}
\tag{10}
\]

Indeed,

\[
N^2-\ell\bigl(\ell s(s-1)+2rs\bigr)
=\ell^2s+r^2\geq0.
\]

Independence is unnecessary in the history-wise version. Let
(\mathcal H) fix (L\in\{0,\ldots,N-1\}), and suppose
(K\mid\mathcal H) is uniform. With

\[
c_\ell(L)=\#\{0\leq z<N:z\equiv L\pmod\ell\},
\]

exactly (c_\ell(L)-1) allowed values of (K) collide with (L) but are
not equal to it. Hence, almost surely with respect to the past,

\[
\boxed{
\Pr(K\ne L,\ K\equiv L\pmod\ell\mid\mathcal H)
=\frac{c_\ell(L)-1}{N}
\leq\frac1\ell.
}
\tag{11}
\]

For (r>0), one has (c_\ell(L)-1\leq s\leq N/\ell); for (r=0),
one has (c_\ell(L)-1=s-1<N/\ell). This proves the last inequality.

Equations (5), (7), and (9)--(11) show exactly what uniformity does and
does not provide: a modulo-(N) transcript cannot amplify factor or
exterior-marker incidence when the only new object is a fresh affine lift
coordinate.

## 3. What a signed carry detects

Let (r\in\{p,q\}), and write (N=rr'), where (r'\) is the other prime.
Suppose

\[
a^E\equiv\sigma\pmod r,
\qquad
a^E\equiv\sigma+NC\pmod {N^2},
\qquad \sigma\in\{1,-1\}.
\]

Reducing the second congruence modulo (r^2) gives

\[
a^E-\sigma\equiv rr'C\pmod {r^2}.
\]

Since (r'\) is a unit modulo (r), this proves

\[
\boxed{
r\mid C
\quad\Longleftrightarrow\quad
a^E\equiv\sigma\pmod {r^2}.
}
\tag{12}
\]

Let (m=\operatorname{ord}_r(a)) and
(d=\operatorname{ord}_{r^2}(a)). Reduction modulo (r) gives (m\mid d).
Also (a^m\equiv1\pmod r), so (a^m=1+ru\pmod {r^2}), and
((a^m)^r\equiv1\pmod {r^2}). Hence (d\mid rm). Since (r) is prime,

\[
d\in\{m,rm\}.
\]

Assume now that (r\nmid E). If (d=m), then a (+1) return modulo
(r) has (m\mid E) and is also (+1) modulo (r^2). For a (-1)
return, (m) is even and (E\equiv m/2\pmod m). The element
(a^{m/2}\) is the nontrivial square root of (1) modulo the odd prime
power (r^2), so it equals (-1). Thus the signed return also lifts.

If (d=rm), an equality (a^E=1\pmod {r^2}) implies (rm\mid E), hence
(r\mid E). An equality (a^E=-1\pmod {r^2}) implies
(E\equiv rm/2\pmod {rm}); here (m) is even, so again (r\mid E).
Both contradict the assumption. Combining this dichotomy with (12) yields

\[
\boxed{
r\mid C
\quad\Longleftrightarrow\quad
\operatorname{ord}_{r^2}(a)=m.
}
\tag{13}
\]

Thus a proper (\gcd(C,N)) is a genuine factor. Under a uniform lift its
probability is nevertheless exactly (5). If (p) and (q) are balanced,
that probability is (O(N^{-1/2})=2^{-\Omega(n)}). The channel tests local
order preservation from (r) to (r^2); it does not by itself insert new
prime support from (p\pm1) or (q\pm1) into a preselected exponent.

## 4. Canonical null witness

Take the fixed integer representative (a=N-1=-1+N). For even (E), the
binomial expansion gives

\[
(N-1)^E=(-1+N)^E\equiv1-EN\pmod {N^2}.
\]

The residue modulo (N) is (1), so its canonical carry is

\[
\boxed{K_0=-E\pmod N.}
\tag{14}
\]

If (E=(N-1)W), then (E) is even and

\[
K_0=-(N-1)W=W\pmod N.
\tag{15}
\]

Modulo every divisor of (N), the base is (-1). Thus every screen of
the form (\gcd(a^j\pm1,N)) is global: one sign gives gcd (N), and the
other gives gcd (1), because (N) is odd. With (W=1), one has
(E=N-1), a global return to (1), and canonical carry (K_0=1). This
proves that a genuine return alone does not force a useful canonical
carry.

## 5. The quadratic-torus lift fibre

Let

\[
\mathcal A_{N^2}=(\mathbb Z/N^2\mathbb Z)[w]/(w^2-D),
\]

with conjugation (\overline{x+yw}=x-yw), trace
(\operatorname{Tr}(Z)=Z+\overline Z), and norm
(\operatorname{Nm}(Z)=Z\overline Z). Let (U) be a unit satisfying

\[
\operatorname{Nm}(U)=1\pmod {N^2}.
\]

Any lift (V) of the same residue as (U) modulo (N) can be written
uniquely as

\[
V=U(1+NZ),\qquad Z=s+tw\in\mathcal A_N.
\]

For every (Z),

\[
\operatorname{Nm}(1+NZ)
\equiv1+N\operatorname{Tr}(Z)
\equiv1+2Ns\pmod {N^2}.
\]

Therefore (V) has exact norm one modulo (N^2) exactly when
(2s=0\pmod N). Because (N) is odd, this is exactly (s=0). Hence the
complete exact norm-one fibre is, uniquely,

\[
U_t=U(1+Ntw),
\qquad t\in\mathbb Z/N\mathbb Z.
\tag{16}
\]

Conversely, each displayed lift has norm
(1-N^2Dt^2\equiv1\pmod {N^2}), so no lift is missing.

Fix any public lift (X) of (U^E\bmod N), and define
(C_t\in\mathcal A_N) by

\[
U_t^E X^{-1}=1+NC_t\pmod {N^2}.
\tag{17}
\]

The binomial expansion in the commutative quadratic algebra gives

\[
(1+Ntw)^E\equiv1+NEtw\pmod {N^2}.
\]

Using (17) first at (t=0), one obtains

\[
U_t^EX^{-1}
\equiv(1+NC_0)(1+NEtw)
\equiv1+N(C_0+Etw)\pmod {N^2}.
\]

Thus

\[
\boxed{C_t=C_0+Etw.}
\tag{18}
\]

Write (C_t=c_{0,t}+c_{1,t}w), and suppose

\[
\operatorname{Nm}(X)=1+Nh\pmod {N^2}.
\]

The norm of the left side of (17) is
(\operatorname{Nm}(X)^{-1}\equiv1-Nh\pmod {N^2}), while

\[
\operatorname{Nm}(1+NC_t)
\equiv1+N\operatorname{Tr}(C_t)
\equiv1+2Nc_{0,t}\pmod {N^2}.
\]

Consequently

\[
2c_{0,t}=-h\pmod N.
\tag{19}
\]

The scalar coordinate is fixed, while (18) gives

\[
c_{1,t}=c_{1,0}+Et\pmod N.
\]

Since (E) is a unit, a conditionally uniform fresh (t) makes the free
tangent coordinate (c_{1,t}) conditionally uniform. The precise history
quantifier is the same as in Section 1: the base, exponent, and public
section choice are fixed by the prior history; (t) is uniform given that
history; and the appended transcript uses (U_t) only modulo (N). Such a
transcript is constant in (t). The scalar laws (5), (7), and (9)--(11)
therefore apply verbatim to (c_{1,t}).

If exact norm one is not required, no trace restriction is imposed. The
full lift fibre is

\[
U_{s,t}=U(1+N(s+tw)),
\qquad (s,t)\in(\mathbb Z/N\mathbb Z)^2,
\]

and the normalized carry changes by (E(s+tw)). Multiplication by the
unit (E) is a coordinatewise bijection, so independent uniform (s,t)
make both carry coordinates jointly uniform.

## 6. Carries on one multiplicative chain

For an ordinary source, suppose

\[
a^E\equiv x+NK_E\pmod {N^2},
\qquad x=\langle a^E\rangle_N.
\]

For (m\geq1), define

\[
x_m=\langle x^m\rangle_N,
\qquad
Q_m=\frac{x^m-x_m}{N}.
\]

Raising the first congruence to the (m)-th power gives

\[
a^{mE}\equiv x^m+Nmx^{m-1}K_E
\equiv x_m+N(Q_m+mx^{m-1}K_E)\pmod {N^2}.
\]

Therefore

\[
\boxed{K_{mE}=Q_m+mx^{m-1}K_E\pmod N.}
\tag{20}
\]

Once (K_E) is fixed, every later carry in this same power chain is fixed.
Repeated squaring does not create independent high digits.

For a torus source, let (S) be any fixed section from unit residues
modulo (N) to unit lifts modulo (N^2). Set

\[
X_E=S(U^E\bmod N),
\qquad
U^EX_E^{-1}=1+NC_E,
\]

and similarly define (X_{mE}) and (C_{mE}). Define the public section
cocycle (Q_m\in\mathcal A_N) by

\[
X_E^mX_{mE}^{-1}=1+NQ_m.
\]

Since the algebra is commutative,

\[
U^{mE}X_{mE}^{-1}
\equiv(1+NC_E)^mX_E^mX_{mE}^{-1}
\equiv1+N(mC_E+Q_m)\pmod {N^2}.
\]

Hence

\[
\boxed{C_{mE}=Q_m+mC_E.}
\tag{21}
\]

This is again an affine deterministic relation, not a source of independent
samples.

## 7. Adaptive bank and prime-support bound

The needed quantifiers can be stated with a filtration. For
(i=1,\ldots,T), let (\mathcal H_{i-1}) contain the complete prior
transcript and all earlier carries. Choose the (i)-th base and exponent as
(\mathcal H_{i-1})-measurable values, require
(\gcd(E_i,N)=1), and then choose the new lift parameter uniformly
conditional on (\mathcal H_{i-1}). By Sections 1 and 5, its selected free
carry coordinate (K_i) satisfies

\[
\Pr(K_i=k\mid\mathcal H_{i-1})=\frac1N
\quad\text{for all }k\in\mathbb Z/N\mathbb Z.
\]

This permits arbitrary adaptive choices based on the past. It does not
permit the current base or exponent to reveal information about the current
fresh parameter before the affine carry is formed.

Represent each (K_i) in (\{0,\ldots,N-1\}), replacing (0) by (1).
For each (j<i), represent (K_i-K_j\pmod N) in the same interval and
replace the exact zero difference by (1). Let (W_{\rm lift}) be any
product of these at most

\[
T+\binom T2
\]

positive atoms, with arbitrary positive powers. A prime divides this
product only if it divides at least one atom. For a fixed exterior prime
(\ell), (9) bounds each direct atom by (1/\ell). Conditional on
(\mathcal H_{i-1}), the earlier (K_j) is fixed, so (11) bounds each
difference atom by (1/\ell). Taking conditional expectations and then a
union bound gives, without any independence assumption,

\[
\boxed{
\Pr(\ell\mid W_{\rm lift})
\leq\frac{T+\binom T2}{\ell}.
}
\tag{22}
\]

The argument remains valid when later bases, exponents, and the choice of
which atoms or powers to retain depend on the complete prior history. The
two essential conditions are conditional uniformity of every new lift
parameter and invertibility of every selected exponent modulo (N).

## 8. Exact F244 interface and scoped consequence

The statement imports only the following external information for its
last application:

1. F244 supplies an input family with four relevant exterior marker primes.
2. Uniformly on that family, each marker (\ell) satisfies
   (\ell\geq2^{cn}) for some fixed (c>0) and all sufficiently large
   input lengths (n); this is the meaning of (2^{\Omega(n)}).
3. The claimed consequence for the F244 signed-power grammar uses marker
   prime support in the product word as its progress criterion. Thus the
   fresh-lift extension can help through this channel only if
   (W_{\rm lift}) is divisible by a relevant marker.

Items 1--3 are the exact external interface needed for the named-family
conclusion. They are not proved or independently checked here.

Assume that (T) is numerical-quasipolynomial:

\[
T\leq 2^{C(\log_2(n+1))^k}
\]

for fixed (C,k). Since
(T+\binom T2\leq T^2), (22) gives for each marker

\[
\Pr(\ell\mid W_{\rm lift})
\leq
2^{-cn+2C(\log_2(n+1))^k}
=2^{-\Omega(n)}.
\]

A union bound over the four markers preserves (2^{-\Omega(n)}). This is
much smaller than inverse quasipolynomial. Conditional on the imported
progress criterion, adjoining this bank to the F244 signed-power grammar
therefore does not provide inverse-quasipolynomial progress.

The affine laws, all exact probability laws, the torus-fibre result, the
same-chain laws, and bound (22) are fully reconstructible without F244.
Only the identification, size, and algorithmic role of the four markers are
external.

## 9. Scope and remaining gap

Uniformity here comes from moving randomly through a lift fibre. A
canonical integer or algebra section selects one fixed point of that fibre,
so none of the uniform laws implies that a canonical carry is unbiased.
The null witness in Section 4 shows only that a useful canonical carry is
not forced on every return; it does not rule out a bias on another family.

The product-support union bound also does not cover same-gauge nonlinear
functions, cross-base section identities, sums, determinants, Euclidean
quotients, retained exact relations, or decoders that use information other
than prime support in a product word. Same-chain carries are already
controlled separately by (20) and (21).

Accordingly, the surviving question is section-specific: one would need an
inverse-quasipolynomial divisibility or collision bias for a canonical high
digit, or for a nonlinear combination of canonical high digits, on enough
of a residual targeted by the underlying exponent construction. The affine
torsor theorem neither proves nor excludes such a result.
