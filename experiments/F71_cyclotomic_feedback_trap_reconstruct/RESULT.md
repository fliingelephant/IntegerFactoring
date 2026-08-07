# Proof-blind reconstruction report: PASS

## Verdict

**PASS.** Every claim in the stated narrow theorem follows. The conclusion is
uniform over all finite endpoint-only transcripts, with no bound on their
length or on the powers used. The source restriction is essential: throughout
this report, a raw relation value is the multiplicative value \(Gw\). The
quotient \((Gw-1)/N\), such as \(c-1\), is outside the declared source, exactly
as required by the final scope statement.

## 1. Local order and the subgroup

First,

\[
N=(c-1)(c+2)+3,
\]

so every common divisor of \(N\) and \(c-1\) divides \(3\). Since
\(3\nmid N\),

\[
\gcd(N,c-1)=1. \tag{2}
\]

Also \(N\equiv1\pmod c\), so \(c\) is a unit modulo \(N\) and modulo every
prime power dividing \(N\). Equation (1) gives \(c^3\equiv1\pmod{p^a}\) for
each \(p^a\Vert N\). Thus the order of \(c\) modulo \(p^a\) divides \(3\).
It cannot be \(1\), since that would give \(p\mid c-1\), contrary to (2).
Therefore

\[
\operatorname{ord}_{p^a}(c)=3
\]

for every \(p^a\Vert N\). The same argument also shows that the reduction of
\(c\) modulo each prime \(p\mid N\) has exact order three.

Since \(1<c<c^2<N\), the least nonnegative representatives of the generated
subgroup are exactly

\[
H=\{1,c,c^2\}\pmod N.
\]

They are distinct and \(c^{-1}=c^2\), \((c^2)^{-1}=c\). Notice also that
\(N\) is odd because \(c\) is odd.

There is no direct sign separator. At any \(p\mid N\), a nonidentity member
of \(H\) has order three, so it is neither \(1\) nor \(-1\) modulo \(p\).
Consequently, for \(h=c,c^2\), both \(\gcd(h-1,N)\) and
\(\gcd(h+1,N)\) equal \(1\). For \(h=1\), the minus sign gives \(N\)
and the plus sign gives \(\gcd(2,N)=1\). Thus a direct sign gcd is always
trivial or global, never a proper factor.

## 2. Closure of every endpoint-only transcript

Suppose a current raw endpoint is \(G=c^e\), with \(e\geq0\). Let
\(r\in\{0,1,2\}\) be \(e\bmod3\). Canonical reduction gives exactly
\(c^r\), because \(c^r\) is already one of the displayed canonical
representatives. Its canonical inverse is \(w=c^k\), where

\[
k\in\{0,1,2\},\qquad k\equiv-e\pmod3.
\]

It follows that

\[
Gw=c^{e+k}=c^{3t},\qquad t=(e+k)/3. \tag{3}
\]

For a canonically reduced endpoint, the identity state gives only
\(1\cdot1=1\). A rule requiring \(1<g<N\) discards it. Each nonidentity
state gives either \(c\cdot c^2\) or \(c^2\cdot c\), hence repeats exactly
\(c^3\). If a positive oversized raw power is kept, (3) gives a positive
\(t\); the only \(t=0\) case is the identity value.

This proves the transcript invariant by induction. Products and positive
powers add or multiply nonnegative \(c\)-exponents. Canonical reduction and
canonical inversion return one of \(1,c,c^2\). Each appended raw relation
value has the form (3). Exact gcd refinement cannot introduce new prime
support, because

\[
\gcd(c^u,c^v)=c^{\min(u,v)},
\]

and the complementary exact quotients are also powers of \(c\). Finally, if
an exact positive integer \(d\)-th root of \(c^u\) exists, unique
factorization gives \(d\mid u\) and the root is \(c^{u/d}\). Hence every
endpoint, raw relation value, gcd component, quotient component, and exact
perfect-power root remains a power of \(c\). There is never a second
nonunit block coprime to the first.

## 3. All stated screens

Let \(G\) be any raw or reduced endpoint, let \(w\) be its canonical
inverse, and write its residue as \(h\in H\). The direct sign result above
depends only on \(h\), so it applies to all such endpoints.

For the inverse-pair difference, if \(h=1\), then
\(G-w\equiv0\pmod N\), so the gcd is global. If \(h\neq1\) and some
\(p\mid N\) divided \(G-w\), then \(h=h^{-1}\pmod p\), hence
\(h^2=1\pmod p\). Together with \(h^3=1\pmod p\), this would force
\(h=1\pmod p\), contradicting its exact order three. Thus the gcd is \(1\)
in every nonidentity case.

For the discriminant screen, \(Gw\equiv1\pmod N\) gives the required
identity

\[
(G+w)^2-\bigl((G-w)^2+4\bigr)=4(Gw-1)\equiv0\pmod N,
\]

or equivalently

\[
(G-w)^2+4\equiv(G+w)^2\pmod N. \tag{4}
\]

If \(h=1\), then \(h+h^{-1}=2\), which is a unit modulo the odd number
\(N\). If \(h\neq1\), the inverse pair is \(c,c^2\), and

\[
h+h^{-1}\equiv c+c^2\equiv-1\pmod N.
\]

Thus \(G+w\) is a unit modulo every prime divisor of \(N\). By (4), the
discriminant has gcd \(1\) with \(N\). Therefore every direct-sign,
inverse-difference, and discriminant screen is trivial or global.

## 4. Complete square decoder

Take any finite list of nonidentity raw relation values

\[
R_i=c^{3t_i},\qquad t_i\in\mathbb Z_{>0}.
\]

Identity relations may be included by allowing \(t_i=0\); they change
nothing. Allow arbitrary integer relation coefficients
\(z=(z_1,\ldots,z_m)\in\mathbb Z^m\), including repetitions and inverses.
Then

\[
P(z)=\prod_i R_i^{z_i}=c^{3T},
\qquad T=\sum_i z_i t_i. \tag{5}
\]

Since \(c\) is prime, a positive rational number of the form (5) is a
rational square if and only if its \(c\)-valuation \(3T\) is even. Since
\(3\) is odd, this is equivalent to

\[
\sum_i z_i t_i\equiv0\pmod2. \tag{6}
\]

This characterizes every rational-square product, not only binary subset
products. Its unique positive rational root is

\[
\sqrt{P(z)}=c^{3T/2}. \tag{7}
\]

It is an integer exactly when \(T\geq0\); negative \(T\) gives a rational
root whose denominator is invertible modulo \(N\). In either case, (6)
makes the exponent in (7) a multiple of three, so

\[
\sqrt{P(z)}\equiv1\pmod N. \tag{8}
\]

For completeness, repeated square extraction does not enlarge the image.
Let \(d=\gcd(t_1,\ldots,t_m)\), omit identity entries, and write
\(d=2^s d_{\mathrm{odd}}\). The exponent lattice of the multiplicative
group generated by the relations is

\[
\Gamma=3d\mathbb Z.
\]

Its complete \(2\)-saturation in the integer exponent group is

\[
\operatorname{Sat}_2(\Gamma)
=\{e\in\mathbb Z:2^k e\in\Gamma\text{ for some }k\geq0\}
=3d_{\mathrm{odd}}\mathbb Z. \tag{9}
\]

Indeed, \(3d\mid2^k e\) implies
\(3d_{\mathrm{odd}}\mid e\), since the latter number is odd; the converse
follows after multiplying by a sufficiently large power of two. If the list
contains only identities, both the original and saturated exponent lattices
are \(\{0\}\). Formula (9) shows that arbitrary products, inverses, exact
square roots, and repeated square roots never remove the factor \(3\) from
the exponent. Hence every exact positive output of the completely saturated
square decoder is \(1\pmod N\). The unit product supplies the residue \(1\),
so the full decoder image is exactly \(\{1\}\).

## 5. Perfect powers and the public square

The perfect-power argument in Section 2 shows that roots of authorized
endpoint values stay in the sole \(c\)-block. A root can have residue
\(1,c\), or \(c^2\), but every one of the stated screens remains trivial or
global, and feeding the root back produces another relation of the form
\(c^{3t}\). Perfect-power extraction therefore neither splits \(N\) nor
creates an independent gcd-free block. An arbitrary \(d\)-th root is not part
of the square decoder's \(2\)-saturation unless \(d\) is a power of two; the
separate endpoint invariant covers the other exact roots.

Direct expansion gives

\[
4N-3=4c^2+4c+1=(2c+1)^2. \tag{10}
\]

Writing \(s=2c+1\),

\[
\gcd(s,N)\mid\gcd(s^2,N)
=\gcd(4N-3,N)=\gcd(3,N)=1,
\]

because \(s^2=4N-3\). Also

\[
\gcd(s-1,N)=\gcd(2c,N)=1,
\qquad
\gcd(s+1,N)=\gcd(2(c+1),N)=1,
\]

where \(N=c(c+1)+1\). Thus the displayed exact square itself gives no
proper gcd. Its two sign roots also give only a trivial/global comparison.

The radicand in (10) uses multiplication and subtraction on the non-endpoint
integer \(N\). It is not a positive product or power of authorized endpoint
occurrences. Its root is likewise not generated by the endpoint invariant:
for the present composite setup \(c\geq5\), and
\(c<2c+1<c^2\), so it is not any nonnegative integral power of \(c\).
Therefore (10) is public but outside the declared endpoint-only source. Using
it as a new block would be an independent, non-endpoint seed and is not an
escape produced by the allowed operations.

## 6. Infinite robust family

Fix any \(B\geq3\), and put \(f(x)=x^2+x+1\). Dirichlet's theorem supplies
infinitely many primes congruent to \(1\pmod3\), so choose distinct
\(\ell_1,\ell_2>B\) of that form. The cyclic group
\(\mathbb F_{\ell_i}^{\times}\) has an element \(r_i\) of exact order
three. It is a nontrivial cube root of unity and therefore

\[
f(r_i)=0\pmod{\ell_i}.
\]

This root is simple. If both \(f(r_i)=0\) and
\(f'(r_i)=2r_i+1=0\pmod{\ell_i}\), then multiplying
\(f(-1/2)\) by four would give \(3=0\pmod{\ell_i}\), impossible because
\(\ell_i>3\).

There are \(\ell_i\) lifts \(r_i+k\ell_i\pmod{\ell_i^2}\). If an integer
representative satisfies \(f(r_i)=m_i\ell_i\), Taylor expansion modulo
\(\ell_i^2\) gives

\[
f(r_i+k\ell_i)\equiv
\ell_i\bigl(m_i+k f'(r_i)\bigr)\pmod{\ell_i^2}.
\]

Since \(f'(r_i)\) is nonzero modulo \(\ell_i\), exactly one value of
\(k\pmod{\ell_i}\) is a root modulo \(\ell_i^2\). Choose any of the other
\(\ell_i-1\) lifts as \(a_i\). Then

\[
\ell_i\mid f(a_i),\qquad \ell_i^2\nmid f(a_i). \tag{11}
\]

Now use the pairwise coprime moduli

\[
\ell_1^2,\ \ell_2^2,\ 2,\ 3,
\quad\text{and all primes }q\text{ with }5\leq q\leq B.
\]

They are pairwise coprime because the \(\ell_i\) are distinct and exceed
\(B\). CRT gives one residue class \(A\pmod M\) satisfying all the stated
congruences. It is a reduced residue class: \(A\equiv1\pmod2\),
\(A\equiv2\pmod3\), \(A\equiv1\pmod q\), and
\(A\equiv r_i\not\equiv0\pmod{\ell_i}\). Hence \(\gcd(A,M)=1\).
Dirichlet's theorem now gives infinitely many primes

\[
c\equiv A\pmod M.
\]

Every such \(c\) is odd. Its number \(N=f(c)\) has all the required
properties:

1. From (11) and polynomial congruence modulo \(\ell_i^2\),
   \(\ell_i\mid N\) but \(\ell_i^2\nmid N\). Thus
   \(v_{\ell_i}(N)=1\) for both \(i\).
2. The two distinct primes \(\ell_1,\ell_2\) divide \(N\), so \(N\) is
   composite and has at least two distinct prime divisors.
3. Since \(c\equiv2\pmod3\),
   \(N\equiv2^2+2+1\equiv1\pmod3\). Hence \(3\nmid N\).
4. The prime \(2\) does not divide \(N\), because \(c\) is odd. For every
   prime \(q\) with \(5\leq q\leq B\),
   \(c\equiv1\pmod q\) gives \(N\equiv3\not\equiv0\pmod q\). Together
   with the preceding exclusion of \(2\) and \(3\), every prime divisor of
   \(N\) is greater than \(B\).
5. If \(N=x^k\) for some integers \(x>1\) and \(k>1\), every prime
   valuation of \(N\) would be divisible by \(k\). The valuations
   \(v_{\ell_1}(N)=v_{\ell_2}(N)=1\) contradict this. Thus \(N\) is not a
   perfect power.

All compatibility, simple-root, exact-valuation, small-prime, and
non-perfect-power assertions therefore hold for infinitely many odd prime
values of \(c\).

## 7. Witness

For \(c=11\),

\[
N=11^2+11+1=133=7\cdot19,
\qquad
11^3=1331=1+10\cdot133.
\]

Modulo \(7\), \(11\equiv4\) and \(4^3\equiv1\), while \(4\neq1\).
Modulo \(19\), \(11^2\equiv7\) and \(11^3\equiv1\), while
\(11\neq1\). Thus the local orders are three, and the canonical subgroup is
\(\{1,11,121\}\pmod{133}\).

Two duplicate raw relations \(R_1=R_2=11^3\) give

\[
R_1R_2=11^6=(11^3)^2.
\]

The exact positive decoded root is \(11^3=1331\equiv1\pmod{133}\). Hence

\[
\gcd(1331-1,133)=133,
\qquad
\gcd(1331+1,133)=1,
\]

which is the asserted global/trivial outcome rather than a split.

## 8. Exact scope of the conclusion

The induction covers every finite transcript and permits arbitrarily many
occurrences and arbitrarily large powers. Canonical residues traverse the full
three-element subgroup, gcd refinement preserves the one-prime support, and
the complete \(2\)-saturated square decoder has image \(\{1\}\). Therefore
the proof establishes the stated narrow classification:

> Unlimited occurrence amplification inside one endpoint block can be
> trapped at the full subgroup level, even after exact gcd refinement and
> complete square decoding.

Here “unlimited” means that no finite bound is imposed: each transcript is
finite, but the theorem is uniform over all such transcripts.

The proof does **not** cover the quotient
\((c^{3t}-1)/N\), in particular \((c^3-1)/N=c-1\); an independent seed or
block; non-endpoint integer data; additive operations; order or period
methods; arbitrary algorithms; or general factoring. Allowing any of those
would change the source algebra and is not justified by this invariant.
