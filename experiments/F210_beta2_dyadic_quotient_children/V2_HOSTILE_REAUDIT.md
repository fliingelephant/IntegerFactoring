# Fresh hostile re-audit of F210 V2

## Strict verdict

**PASS.** F210 V2 repairs the exact defect that forced the V1 hostile FAIL,
states the dyadic domain \(t\ge1\), and preserves all limitations of V1. Every
required manifest check passes. No new theorem-level error, quantifier slip,
or scope inflation was found.

This is a proof-only PASS relative to the named promoted P172, P179, and P183
interfaces. It is not a factoring algorithm and not a general lower bound for
child-factor statistics or arithmetic circuits.

No experimental mathematical computation, randomized evidence, or web search
was used.

## 1. V2 and V1 authentication

I opened `V2_MANIFEST.md` first. Before reading any V2 packet input, I
recomputed all four frozen hashes. They matched:

```text
d71fadf26f194f067647d7cee3ac8bcdfbc2d84c1d518d356f0df0c1e1268fa0  V2_STATEMENT.md
b53f7fd20fc71f3495dc04893d3ab7101db710256b751ac9948c40299faca0f9  V2_PROOF.md
27020049113063d9f39b4d3aea3f77c1c3ef34defa3d138d4e355e74e2c77ffc  V2_SELF_AUDIT.md
02f36349f62f6a4706c66c2761fdb0d28415ee8099c6281b029dfd96aa623be5  V2_PROVENANCE.md
```

The manifest does not freeze itself. Its observed SHA-256 is

```text
a931979b76412e22d1ac18f91026b56b92d029ca3cf501ddb025144065439345  V2_MANIFEST.md
```

I then read only the authenticated provenance file. Before reading a V1
artifact, I checked every V1 hash recorded there. All matched:

```text
77fea55ce6600f149a636aed9d2bc2ce788deaba47bbcec95a03e24a39430cd9  STATEMENT.md
c754a738c21ce89f0c43ecfa5b9a96554b4b64bc23991b3258ee7fe2a885c0ea  PROOF.md
a00f07120dcda12447e556fe4529a7c1b9d9766c5bef5188a8b9ccd05f7eda28  SELF_AUDIT.md
d9f3e38e4d9ad09b63487f8d503655638eca5b82cb6d347b0a66ef9a1c24debd  MANIFEST.md
0385546d865c4cbec55adec59fe33c92ac06c64749adf9a2de773b0557563a35  HOSTILE_AUDIT.md
```

Thus V1, including its strict FAIL, is preserved byte-for-byte. The V1 audit
remains evidence about V1 only. It is not reused as verification of V2.

A direct V1-to-V2 comparison confirms that the mathematical changes are the
explicit \(t\ge1\) domain, the repaired nontrivial balanced-point statement
and proof, and matching scope clarifications. The other mechanisms were not
silently strengthened.

## 2. Dyadic domain and P179 lift reconstruction

V2 now assumes

\[
m=2^t,
\qquad t\ge1,
\qquad2m<p.
\]

Therefore \(m\) is an even integer. The canonical odd residues exist, the
first permitted stage is \(t=1,m=2\), the modulus
\(h=2m=2^{t+1}\) has the stated form, and every later parity and lift count
uses a valid domain.

Write

\[
p=r+mP,
\qquad q=c+mQ.
\]

Expanding \(N=pq\) gives

\[
K=rQ+cP+mPQ.
\]

Since \(r,c\) are odd and \(m\) is even,

\[
K\equiv P+Q\pmod2.
\]

For \(a=P\bmod2\) and \(b=Q\bmod2\), this is exactly

\[
b=a\mathbin{\mathsf{xor}}(K\bmod2).
\]

For either legal pair,

\[
N-r_ac_a=m(K-ac-b_ar-ab_am),
\]

and the parenthesized integer is even. Hence \(K_a\) is integral. Also

\[
0<r_a,c_a<2m<p,
\qquad r_ac_a<p^2<N.
\]

It follows that

\[
0<K_a<\frac N{2m}.
\]

Because \(2m\) is coprime to odd \(N\), and neither \(r_a\) nor \(c_a\)
can be divisible by \(p\) or \(q\),

\[
\gcd(K_a,N)
=\gcd(N-r_ac_a,N)=1.
\]

This independently reconstructs the imported P179 state used by V2.

## 3. Child tables, coalescence, difference bounds, and lcm

If \(\delta=0\), then \(b_a=a\), and

\[
K_0=K/2,
\qquad
K_1=(K-r-c-m)/2.
\]

If \(\delta=1\), then \(b_a=1-a\), and

\[
K_0=(K-r)/2,
\qquad
K_1=(K-c)/2.
\]

The two child tables are correct. Under the convention \(D=K_0-K_1\),

\[
D=(r+c+m)/2\quad(\delta=0),
\qquad
D=(c-r)/2\quad(\delta=1).
\]

The first value is strictly positive. The second vanishes exactly when
\(r=c\). Thus coalescence is exactly \(\delta=1,r=c\).

At the first permitted stage, \(t=1,m=2\) and \(r=c=1\). If
\(N\equiv3\pmod4\), then \(K=(N-1)/2\) is odd, so

\[
K_0=K_1=(N-3)/4.
\]

This is correctly stated as an included first-stage case.

The endpoint bounds are exact. In the \(\delta=0\) case,

\[
0<D\le(3m-2)/2<3m/2.
\]

Outside coalescence in the \(\delta=1\) case, \(r,c\) are distinct odd
integers in \([1,m-1]\), so

\[
0<|D|\le(m-2)/2<m/2.
\]

When \(D\ne0\), the difference identity gives

\[
g=\gcd(K_0,K_1)
=\gcd(K_0,|D|)
=\gcd(K_1,|D|).
\]

Therefore every full common prime power divides \(|D|\). No conclusion is
drawn about private support. Finally,

\[
\operatorname{lcm}(K_0,K_1)=K_0K_1/g
\]

holds for all positive children. In coalescence it reduces correctly to the
common child value.

## 4. Half-translation, matrix identity, and physical coordinates

With \(\sigma=(-1)^\delta\),

\[
r_1-r_0=h/2,
\qquad c_1-c_0=\sigma h/2.
\]

Direct expansion gives

\[
\begin{aligned}
F_1(P-1/2,Q-\sigma/2)
={}&hPQ+(c_1-\sigma h/2)P+(r_1-h/2)Q\\
&+\sigma h/4-c_1/2-\sigma r_1/2-K_1.
\end{aligned}
\]

The difference formula is equivalently

\[
K_0-K_1=c_1/2+\sigma r_1/2-\sigma h/4.
\]

The expansion therefore equals \(F_0(P,Q)\). When \(\delta=1\),
\(\sigma=-1\), so the second translated argument is \(Q+1/2\). The
sign is correct.

Multiplying the two shear matrices in (24) with \(A_0\) yields first row
\((r_0+h/2,h)=(r_1,h)\) and second row

\[
\left(
-K_0+(c_0+\sigma r_0)/2+\sigma h/4,
c_0+\sigma h/2
\right)
=(-K_1,c_1).
\]

Thus the matrix identity is exact, and

\[
\det A_a=r_ac_a+hK_a=N.
\]

For \(X=hP+r_a\) and \(Y=hQ+c_a\), direct multiplication gives

\[
XY-N=hF_a(P,Q).
\]

In any ring where two is a unit, \(h\) is a unit. Both charts are therefore
affinely isomorphic to the same equation \(XY=N\).

## 5. Exact odd-local scope and child-prime information

The affine isomorphism equates only data intrinsic to the aligned odd-local
solution scheme. Point counts, multiplicity and singularity data,
coordinate-free Frobenius data, and invariants of the same abstract split
curve consequently agree.

It does not equate the raw coefficient lists or the factorizations of the two
different integers \(K_0,K_1\). In particular, V2 does not assert equality of
prime support, smoothness, Jacobi symbols, higher-residue symbols, or exact
orders computed at their different prime powers. It also leaves asymmetric
integral-order and class-group constructions open. This is the required
narrow reading.

If an odd prime power \(\ell^e\mid K_a\), then \(\ell\nmid N\), and

\[
N\equiv r_ac_a\pmod{\ell^e}.
\]

All three values are units. Thus every multiplicative character satisfies

\[
\chi(N)=\chi(r_a)\chi(c_a).
\]

Multiplication by \(r_ac_a^{-1}\) gives

\[
Nr_ac_a^{-1}\equiv r_a^2\pmod{\ell^e}.
\]

This is a public square root only after the displayed scaling. V2 makes no
unscaled square-root claim and derives no orientation from the character
identity.

## 6. Finite 2-adic lifts

Fix \(t\ge1\) and \(s\ge t+1\). The congruence
\(X\equiv r_a\pmod{h}\), with \(h=2^{t+1}\), has exactly

\[
2^{s-(t+1)}=2^{s-t-1}
\]

solutions modulo \(2^s\). Every solution is odd and hence invertible. It
determines a unique

\[
Y=NX^{-1}\pmod{2^s}.
\]

Because \(r_ac_a\equiv N\pmod h\), reduction modulo \(h\) forces
\(Y\equiv c_a\pmod h\). Conversely, every ordered pair in the declared set
comes from exactly one such \(X\). The count is therefore exact and equal for
the two children, including the endpoint \(s=t+1\), where both counts are
one.

## 7. Repaired nontrivial balanced-point theorem

Suppose an integer point satisfies

\[
1<X<\sqrt N<Y<N,
\qquad XY=N.
\]

The positive divisors of the promised squarefree semiprime are exactly
\(1,p,q,N\). Since \(p<q\), one has \(p<\sqrt N<q\). The strict endpoint and
orientation inequalities therefore force

\[
(X,Y)=(p,q).
\]

The residues of \((p,q)\) modulo \(h\) are the unique true next-lift pair.
The two charts have distinct first residue classes because

\[
r_1-r_0=m\not\equiv0\pmod{2m}.
\]

Therefore only the true chart contains \((p,q)\), and only the true chart has
a point in the repaired balanced box. No efficiency claim follows from this
existence and uniqueness proof.

The V1 counterexamples now test the scope rather than refute it:

- For \(N=77=7\cdot11\) and \(m=2\), the false chart contains \((1,77)\).
  This point violates both \(1<X\) and \(Y<N\). V2 explicitly permits it.
- For the coalesced state \(N=91=7\cdot13\), \(m=2\), the other chart
  contains \((1,91)\). It is again outside the repaired box.

V2 also explicitly disclaims uniqueness under the old condition
\(X<\sqrt N<Y\). The V1 failure is therefore preserved rather than erased by
reinterpretation.

In coalescence, \(\delta=1,r=c\), so the residue pairs are

\[
(r,r+m),
\qquad(r+m,r).
\]

If one contains \((p,q)\), the other contains \((q,p)\). The swapped point
has \(q>\sqrt N>p\), so it reverses the strict balanced orientation. V2 does
not extend this statement to all integer points in the other chart; it
expressly permits trivial endpoints and other points outside the box.

The V1 theorem defect is exactly repaired.

## 8. Conditional common-order bridge and P172

Complete factorizations of \(K_0,K_1\) give complete factorizations of

\[
H_a=hK_a
\]

and

\[
G=\gcd(H_0,H_1)=h\gcd(K_0,K_1)=hg.
\]

If both tests \(d_a=\gcd(w^{H_a}-1,N)\) return \(N\), both local orders
divide both exponents, and hence divide \(G\). Thus \(w^G=1\pmod N\).

Factor-first stripping starts from the fully factored annihilator \(E=G\).
For each prime \(\ell\mid E\), test \(w^{E/\ell}\). A proper gcd factors
\(N\). A gcd of \(N\) permits removal of one copy of \(\ell\). A gcd of
one means neither local order divides \(E/\ell\), so both orders contain the
full current \(\ell\)-adic valuation. Repetition over all prime
multiplicities either factors or proves

\[
e=\operatorname{ord}_p(w)=\operatorname{ord}_q(w)=E.
\]

Both children are coprime to \(N\), and \(h\) is coprime to odd \(N\).
Therefore \(G\), and every divisor \(e\), is coprime to \(N\).

The promoted P172 interface requires a public unit with one fully known exact
order in every hidden prime-power component, that order coprime to \(N\), and
\(N^{1/4}/e\) numerical QP. Here \(N=pq\) is squarefree, so the two local
orders above are exactly the two component orders. The stripping process
fully identifies and factors \(e\), coprimality is proved, and (38) is the
required numerical-QP threshold. Every P172 hypothesis is present.

The bridge remains conditional. V2 guarantees neither a proper initial gcd,
the simultaneous return, nor the large-order threshold. It proves no fixed
orientation rule from an asymmetric return.

## 9. Polynomial gcd and zero resultant

For positive integers \(A,B\), the monic polynomial gcd is

\[
\gcd_{\mathbb Z[X]}(X^A-1,X^B-1)
=X^{\gcd(A,B)}-1.
\]

Substituting \(H_0,H_1\) gives \(X^G-1\). By contrast, both polynomials
always contain \(X-1\), so their ordinary resultant is zero. V2 correctly
uses the polynomial gcd as the exact common-root content and infers nothing
from the identically zero scalar resultant.

## 10. Late recursion and exact P183 scope

The bit-length convention implies \(N<2^n\), so

\[
K_a<\frac N{2^{t+1}}<2^{n-t-1}.
\]

If \(t\ge\eta n-O(1)\) for fixed \(\eta>0\), each child has at most
\((1-\eta)n+O(1)\) bits. A numerical-QP number of these fixed-ratio side
calls, together with at most one \((n-1)\)-bit decrement-spine call, has

\[
T(n)\le T(n-1)+Q(n)T((1-\eta)n+O(1))+Q(n).
\]

This is exactly the promoted P183 recurrence.

At P175 precision,

\[
t=\left\lfloor\frac14\log_2N\right\rfloor-(\log n)^{O(1)},
\]

the child bound is

\[
\frac34n+(\log n)^{O(1)}.
\]

Any fixed \(\rho>3/4\) absorbs the additive term after a finite prefix.

V2 does not apply P183 to two independent early children. At \(t=o(n)\),
both may have \(n-o(n)\) bits, and a binary recursion tree is outside the
theorem. The safe single-chain recurrence

\[
T(n)\le T(n-1)+Q(n)
\]

is preserved, but V2 gives no selector or global nesting theorem that
constructs this chain.

## 11. Nonclaims and final scope

The hostile scope audit confirms all required limitations:

- The correct reciprocal prefix is granted. V2 does not construct it.
- V2 provides no guaranteed selector and no all-input factoring algorithm.
- The balanced-point theorem is exact but not an efficient bounded-point
  test.
- Common-support control does not restrict private child support.
- Odd-local affine invariance does not equate raw child-factor statistics.
- Equal finite 2-adic lift counts do not exclude a nonlinear or Archimedean
  selector.
- The order bridge has explicit, unguaranteed entry conditions.
- The exponent polynomials provide no common-root datum beyond \(G=hg\).
- Late sibling recursion is safe only as fixed-ratio side work on one
  decrement spine. Early two-child recursion remains excluded.
- Adaptive bases, asymmetric factor statistics, integral bounded-point
  algorithms, new integral orders, and a globally nested spine remain open.

## Result

**PASS.** The frozen V2 packet is authentic, V1 and its FAIL are preserved,
the nontrivial balanced-point and \(t\ge1\) repairs are exact, and every
remaining manifest check passes within the stated scope.

