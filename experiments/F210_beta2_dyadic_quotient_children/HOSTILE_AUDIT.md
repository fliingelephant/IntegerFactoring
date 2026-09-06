# Fresh hostile audit of F210

## Strict verdict

**FAIL.** The frozen packet is authentic, and almost all of its algebraic,
order-theoretic, and recursion claims reconstruct correctly. However, Theorem
2 contains a false integral-orientation claim. The false child can contain the
trivial oriented factor pair \((1,N)\). This also invalidates the stated
orientation conclusion in a coalesced state.

The local repair is to require a nontrivial factor pair, for example

\[
1<X<\sqrt N<Y<N,
\qquad XY=N,
\]

or equivalently to require positive quotient coordinates after the lift. The
frozen version does not contain this restriction, so it must fail rather than
receive a scope-only PASS.

No experimental mathematical computation or randomized evidence was used.

## 1. Frozen-input authentication

I opened `MANIFEST.md` first. Before reading the statement, proof, or
self-audit, I recomputed every frozen hash. All three matched:

```text
77fea55ce6600f149a636aed9d2bc2ce788deaba47bbcec95a03e24a39430cd9  STATEMENT.md
c754a738c21ce89f0c43ecfa5b9a96554b4b64bc23991b3258ee7fe2a885c0ea  PROOF.md
a00f07120dcda12447e556fe4529a7c1b9d9766c5bef5188a8b9ccd05f7eda28  SELF_AUDIT.md
```

The manifest does not freeze itself. Its observed SHA-256 is

```text
d9f3e38e4d9ad09b63487f8d503655638eca5b82cb6d347b0a66ef9a1c24debd  MANIFEST.md
```

The manifest explicitly requires the named promoted interfaces P172, P179,
and P183. I therefore inspected only those named sections in `PROVED.md`.
The promoted labels are not the same as the experiment directory numbers:
P172 comes from F195 V2, P179 from F203, and P183 from F207. Their interfaces
agree with the imports stated in F210.

## 2. P179 lift relation, integrality, positivity, and coprimality

Write

\[
p=r+mP,
\qquad q=c+mQ.
\]

Because \(r,c\) are odd and \(m\) is even,

\[
K=rQ+cP+mPQ\equiv P+Q\pmod2.
\]

If \(a=P\bmod2\) and \(b=Q\bmod2\), this gives exactly

\[
b=a\mathbin{\mathsf{xor}}(K\bmod2).
\]

For either legal pair,

\[
N-r_ac_a=m(K-ac-b_ar-ab_am),
\]

and the parenthesized integer is even. Thus \(K_a\) is integral. The strict
assumption \(2m<p\) gives

\[
0<r_a,c_a<2m<p,
\qquad r_ac_a<p^2<N.
\]

It follows that

\[
0<K_a<\frac N{2m}.
\]

Also, \(2m\) is coprime to odd \(N\), and neither \(r_a\) nor \(c_a\) is
divisible by \(p\) or \(q\). Therefore

\[
\gcd(K_a,N)
=\gcd(N-r_ac_a,N)=1.
\]

These claims pass independently of the supplied proof.

Minor domain clarification: the use of an even \(m\), the canonical set
\(\{1,3,\ldots,m-1\}\), and the declared first stage \(m=2\) implicitly
require \(t\ge1\). Stating this explicitly would remove an avoidable endpoint
ambiguity. It is not the reason for the FAIL because the existence of the
declared canonical residues already excludes \(m=1\).

## 3. Child tables, sign, coalescence, and bounds

When \(\delta=0\), \(b_a=a\), so

\[
K_0=K/2,
\qquad
K_1=(K-r-c-m)/2.
\]

When \(\delta=1\), \(b_a=1-a\), so

\[
K_0=(K-r)/2,
\qquad
K_1=(K-c)/2.
\]

The two displayed child tables are therefore correct. With the convention
\(D=K_0-K_1\), the signs are exactly

\[
D=(r+c+m)/2\quad(\delta=0),
\qquad
D=(c-r)/2\quad(\delta=1).
\]

The first quantity is positive. The second vanishes exactly when \(r=c\).
This proves the stated coalescence criterion.

At \(m=2\), one has \(r=c=1\). If \(N\equiv3\pmod4\), then
\(K=(N-1)/2\) is odd, and both children equal \((N-3)/4\). The statement
correctly presents this as an included first-stage case, not as a converse at
all later stages.

Since \(1\le r,c\le m-1\),

\[
0<D\le(3m-2)/2<3m/2
\]

in the even-\(K\) case. Outside coalescence, \(r,c\) are distinct odd
integers, so \(|r-c|\le m-2\), and

\[
0<|D|\le(m-2)/2<m/2.
\]

Every bound in (18) passes.

## 4. Common support and lcm, including coalescence

Outside coalescence, \(D\ne0\), and the elementary difference identity gives

\[
\gcd(K_0,K_1)=\gcd(K_0,|D|)=\gcd(K_1,|D|).
\]

Thus if a prime power divides both children, that full prime power divides
\(|D|\). The theorem makes no restriction on private prime-power support,
which is the correct scope.

For all positive children, including \(K_0=K_1\),

\[
\operatorname{lcm}(K_0,K_1)
=\frac{K_0K_1}{\gcd(K_0,K_1)}.
\]

In coalescence this reduces to \(K_0\), as it must. These claims pass.

## 5. Half-translation and matrix signs

Put \(\sigma=(-1)^\delta\). The child increments are

\[
r_1-r_0=h/2,
\qquad
c_1-c_0=\sigma h/2.
\]

Expanding the translated polynomial gives

\[
\begin{aligned}
F_1(P-1/2,Q-\sigma/2)
={}&hPQ+(c_1-\sigma h/2)P+(r_1-h/2)Q\\
&+\sigma h/4-c_1/2-\sigma r_1/2-K_1.
\end{aligned}
\]

The linear coefficients become \(c_0,r_0\), while

\[
K_0-K_1=c_1/2+\sigma r_1/2-\sigma h/4
\]

makes the constant term \(-K_0\). This proves (22). In particular, when
\(\delta=1\), \(\sigma=-1\), and the translated second coordinate is
\(Q+1/2\). The sign is correct.

Direct multiplication in (24) produces

\[
\begin{pmatrix}
r_0+h/2&h\\
-K_0+(c_0+\sigma r_0)/2+\sigma h/4&c_0+\sigma h/2
\end{pmatrix}
=A_1.
\]

Also \(\det A_a=r_ac_a+hK_a=N\). The matrix identity passes.

The physical substitution gives the exact identity

\[
XY-N=hF_a(P,Q).
\]

When two is a unit, so is \(h\), and both charts are affinely isomorphic to
the same curve \(XY=N\). The odd-local affine-invariant claims therefore
pass.

## 6. Exact scope of odd-local path blindness

The isomorphism proves equality only for data intrinsic to the solution
scheme after the public affine coordinate alignment. It supports point counts,
singularity and multiplicity data, coordinate-free Frobenius data, and
invariants of the same abstract split curve.

It does not identify the raw integral coefficient lists or the distinct
factorizations of \(K_0,K_1\). In particular, it does not equate prime
support, smoothness, Jacobi symbols, higher-residue symbols, or exact orders
computed at the different child prime powers. The statement explicitly keeps
such asymmetric statistics open. This scope passes and must be preserved in
any repaired version.

## 7. Character identity and the scaled square root

If \(\ell^e\mid K_a\), then \(\ell\nmid N\), and reduction of
\(hK_a=N-r_ac_a\) gives

\[
N\equiv r_ac_a\pmod{\ell^e}.
\]

The product is a unit, so both factors are units. Multiplicativity gives

\[
\chi(N)=\chi(r_a)\chi(c_a).
\]

Multiplying by the public unit \(r_ac_a^{-1}\) gives

\[
Nr_ac_a^{-1}\equiv r_a^2\pmod{\ell^e}.
\]

This is a square root of the *scaled* value \(Nr_ac_a^{-1}\). It does not
say that \(N\) itself is a square modulo \(\ell^e\). The statement makes
this distinction correctly.

## 8. Finite 2-adic lift count and the fatal oriented-point defect

For \(s\ge t+1\), the fixed odd class
\(X\equiv r_a\pmod h\) has exactly

\[
2^{s-(t+1)}=2^{s-t-1}
\]

lifts modulo \(2^s\). Each is a unit and uniquely determines
\(Y=NX^{-1}\). Since \(r_ac_a\equiv N\pmod h\), that \(Y\) automatically
satisfies \(Y\equiv c_a\pmod h\). Conversely, every pair arises this way.
Thus the count (31) is exact for both children.

The next conclusion is false. The packet says that only the true chart has
an integer point satisfying

\[
X<\sqrt N<Y,
\qquad XY=N.
\]

It overlooks the trivial positive factor pair \((1,N)\).

A counterexample is

\[
N=77=7\cdot11,
\qquad m=2,
\qquad r=c=1,
\qquad K=38,
\qquad\delta=0.
\]

The children are

\[
(r_0,c_0,K_0)=(1,1,19),
\qquad
(r_1,c_1,K_1)=(3,3,17).
\]

Because \(p=7\equiv3\pmod4\), child \(a=1\) is the true child. Nevertheless,
the false child \(a=0\) contains

\[
(P,Q)=(0,19),
\qquad
(X,Y)=(4P+1,4Q+1)=(1,77).
\]

It satisfies \(F_0(P,Q)=0\), \(XY=N\), and
\(X<\sqrt N<Y\). This directly contradicts “the true chart, and only the
true chart.”

The coalesced wording also fails as written. Take

\[
N=91=7\cdot13,
\qquad m=2.
\]

Then \(r=c=1\), \(\delta=1\), and \(K_0=K_1=22\). The true chart is
\((r_1,c_1)=(3,1)\). The other chart \((1,3)\) contains both the swapped
point \((13,7)\), which reverses the orientation, and the trivial point
\((1,91)\), which satisfies the displayed orientation. Thus it is not true
that the other chart “fails this orientation.”

The exact repair is small but mathematical:

\[
1<X<\sqrt N<Y<N,
\qquad XY=N.
\]

Under this condition, the promised semiprime has only the nontrivial positive
factor pair \((p,q)\), so the true chart is unique. Requiring positive
quotient coordinates \(P,Q>0\) also excludes the trivial endpoints in this
setting. Either restriction must appear in the frozen theorem and proof.

## 9. Simultaneous-return bridge and every P172 hypothesis

Given complete factorizations of both \(K_a\), the integers
\(H_a=hK_a\) are fully factored. Their gcd is exactly

\[
G=\gcd(H_0,H_1)=h\gcd(K_0,K_1)=hg,
\]

also in coalescence.

If both gcd tests return \(N\), the two local orders of the public unit \(w\)
divide both \(H_0,H_1\), and hence divide \(G\). Thus \(w^G=1\pmod N\).

Start with the fully factored annihilator \(E=G\). For each prime
\(\ell\mid E\), test \(w^{E/\ell}\). A proper gcd factors \(N\). A gcd of
\(N\) permits removal of one copy of \(\ell\). A gcd of \(1\) means that
neither local order divides \(E/\ell\), so both local orders have the full
current \(\ell\)-adic valuation. Repeating this for every prime multiplicity
either factors or leaves

\[
e=\operatorname{ord}_p(w)=\operatorname{ord}_q(w)=E.
\]

Because each child and \(h\) are coprime to odd \(N\), one has
\(\gcd(G,N)=1\), and hence \(\gcd(e,N)=1\).

The promoted P172 interface requires a public unit with one fully known exact
order in every hidden prime-power component, that order coprime to \(N\), and
\(N^{1/4}/e\) numerical QP. Here \(N=pq\) is squarefree, so the two rational
prime orders are exactly the two hidden component orders. The stripping
process fully factors and identifies \(e\), (37) gives coprimality, and (38)
is the required terminal bound. Every P172 hypothesis is present. This bridge
passes and remains explicitly conditional on the simultaneous return and the
large-order threshold.

An asymmetric return is only a public feature. The packet correctly proves no
orientation rule from its direction.

## 10. Exponent-polynomial gcd versus resultant

For positive integers \(A,B\),

\[
\gcd_{\mathbb Z[X]}(X^A-1,X^B-1)
=X^{\gcd(A,B)}-1
\]

with the monic gcd convention. Substitution of \(H_0,H_1\) gives (39).

Both polynomials always contain \(X-1\), so their ordinary resultant is
identically zero. This zero contains no finer order information. The packet
correctly distinguishes the nonzero polynomial gcd from the zero scalar
resultant.

## 11. Late-stage bit length and P183 scope

The input convention gives \(N<2^n\). Hence

\[
K_a<\frac{N}{2^{t+1}}<2^{n-t-1}.
\]

If \(t\ge\eta n-O(1)\) for fixed \(\eta>0\), the child input length is at
most \((1-\eta)n+O(1)\). A numerical-QP number of such fixed-ratio side calls,
together with only one decrement-spine call, has recurrence

\[
T(n)\le T(n-1)+Q(n)T((1-\eta)n+O(1))+Q(n),
\]

which is exactly the promoted P183 interface.

At P175 precision,

\[
t=\frac14\log_2N-(\log n)^{O(1)}+O(1),
\]

so the child length is at most

\[
\frac34n+(\log n)^{O(1)}.
\]

Every fixed \(\rho>3/4\) absorbs the additive polylogarithmic term after a
finite prefix. This late-stage accounting passes.

The proof does not apply P183 to two independent early siblings. When
\(t=o(n)\), both children can have \(n-o(n)\) bits, and a binary recursion
tree is outside the promoted recurrence. The packet explicitly excludes that
use. It also correctly notes that a single decrement chain would be safe but
does not construct the chain.

## 12. Nonclaims and exact surviving scope

The following limitations are stated correctly and survive the audit:

- The reciprocal prefix is granted. F210 does not construct it.
- F210 gives no guaranteed child selector and no factoring algorithm.
- Common-support control concerns only support shared by both children and,
  outside coalescence, only through \(|D|\). Private support remains open.
- Odd-local affine invariants are path-blind. Raw factorization statistics are
  not asserted equal.
- The finite 2-adic theorem proves equal existence and multiplicity only. It
  does not exclude a non-additive integer selector.
- The order-stripping bridge is conditional on a proper gcd, simultaneous
  return, or a sufficiently large exact common order. None is guaranteed.
- The exponent-polynomial calculation gives no common-root information beyond
  \(G=hg\).
- Only late fixed-ratio sibling calls are recursion-safe under P183. A nested
  one-spine construction reaching that range remains open.

One nonclaim needs no change, but the orientation sentence cannot be defended
as a nonclaim: it is an explicit uniqueness assertion and is refuted above.

## Required correction and re-audit result

Replace the integral sentence in Theorem 2 by a statement about a
**nontrivial** oriented factor pair, for example:

> The true chart, and only the true chart, has an integer point with
> \(1<X<\sqrt N<Y<N\) and \(XY=N\). In a coalesced state the other chart
> contains the swapped nontrivial point \((q,p)\), which reverses this
> orientation.

Make the same change in the proof. It is also preferable to state \(t\ge1\)
explicitly. Freeze the repaired packet and run a new hostile audit.

**Strict result: FAIL.**

