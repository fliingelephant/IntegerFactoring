# F274 fresh hostile audit — PASS

## Frozen authentication

I authenticated the packet before reading any theorem or proof. The
required and observed SHA-256 of FROZEN.sha256 is

b7a307fcc0aa0f818e250775499d355fd07396da22bebb4f74e1f5e5b5ebab86.

Every frozen entry matches:

| Artifact | SHA-256 |
|---|---|
| STATEMENT.md | 22674281efe2fc593ef8b657bc4782f1892e118a2a193c6f5028d514a245ce47 |
| PROOF.md | 0077b4d4bea0ceed8d4771b78d02a48f67b446af7358a86273145f3215866d0b |
| SELF_AUDIT.md | 6da33d3be00a7953d5ddf2ce7a3c48a2fea5c32e943e5447731f4d3668c98b66 |
| PROVENANCE.md | e9a0203e80b2b21e16298c6dbbf02b39f71c94d8c0ce19fdf34263ee6d79a2c5 |
| MANIFEST.md | cec0a9c37ce539456fe2cb393689040b9aa932694d41050b0c6a319f185b0d73 |

I did not modify a frozen file or a durable ledger.

## Verdict

**PASS under the literal named-model hypotheses and exclusions in
STATEMENT.md.**

I found no false identity, endpoint error, missing characteristic case,
invalid rational cancellation, or determinant overclaim. The regular-state
separator, dimension bound, factorial divisibility, scalar coboundary
criterion, and matrix determinant obstruction all reconstruct from first
principles.

Two scope conditions must remain attached to this verdict:

1. The dimension theorem kills the specific \(\overline\Delta^B\)
   nilpotency asymmetry. It does not prove that every other invariant of a
   low-dimensional shift subquotient is identical in the two CRT
   components. In particular, a locally different dimension or rank is a
   separate possible signal, although constructing or reading such a drop
   can itself be factor-bearing.
2. The search disposition is justified only for the displayed regular
   nilpotency, entrywise integer-polynomial difference, and rational-gauge
   fast-forward mechanisms. It is not an impossibility theorem for every
   search using the same ambient words. The packet's repeated named-model
   scope and exact exclusions preserve this interpretation.

## 1. Balanced threshold and full regular translation

From \(p<q\),

\[
 p<\sqrt{pq}<q,
\]

so the integer \(B=\lfloor\sqrt N\rfloor\) satisfies \(p\leq B<q\).
No use of the upper balance bound is hidden in this step.

On the delta-function basis of
\(V_r=\{f:\mathbb F_r\to\mathbb F_r\}\), translation is one cycle of
length \(r\). The delta function at zero is cyclic, so the minimal
polynomial of \(T_r\) has degree \(r\). Since \(T_r^r=I\),

\[
 \mu_{T_r}(Z)=Z^r-1.
\]

In characteristic \(r\), this is \((Z-1)^r\). Translating the operator
variable therefore gives

\[
 \mu_{\Delta_r}(Z)=Z^r.
\]

The nilpotency index is exactly \(r\): \(\Delta_r^k=0\) precisely for
\(k\geq r\). Hence

\[
 \Delta_p^B=0,\qquad \Delta_q^B\ne0.
\]

The second statement is operator nonzeroness. It does not produce a public
probe outside the kernel, and the packet expressly makes no such claim.
The full local spaces also have different hidden dimensions; F274 does not
claim to construct one public global state realizing them.

## 2. Linear shift subquotients and explicit dimension

Every stable subspace and every quotient inherits
\((T_r-I)^r=0\). Thus the induced difference on any subquotient is
nilpotent. A nilpotent endomorphism of a \(d_r\)-dimensional space has
nilpotency index at most \(d_r\), including the zero-dimensional case.
Therefore

\[
 \overline\Delta_r^{\,d_r}=0.
\]

If both local dimensions are at most \(d\leq B\), their \(B\)-th powers
are both zero. This proves loss of the exact full-state asymmetry above. A
local rank drop cannot restore nonzeroness of the \(B\)-th power, although
the rank drop itself is not proved information-free.

Balance gives

\[
 \sqrt{N/2}<p<\sqrt N,
\]

so \(\log_2p=\Theta(n)\). For every fixed numerical quasipolynomial,
the logarithm of its value is \(O((\log n)^k)=o(n)\). Consequently it is
smaller than \(p\) and hence than \(B\) for all sufficiently large balanced
inputs. This comparison is correctly asymptotic and does not cover the
finite initial range.

The conclusion requires an explicit finite-dimensional
\(T_r\)-subquotient. An implicit regular representation, a nonlinear or
semilinear state, or an arbitrary matrix sequence need not satisfy the
same operational boundary.

## 3. Integer-polynomial forward differences

For the ordinary noncyclic difference
\(\delta F(X)=F(X+1)-F(X)\),

\[
 \delta^kX^t(0)
 =\sum_{j=0}^{k}(-1)^{k-j}\binom kjj^t
 =k!S(t,k).
\]

The first equality is the finite-difference formula. The second counts
surjections by inclusion-exclusion and is zero when \(t<k\).

Expanding

\[
 (a+X)^m=\sum_{t=0}^{m}\binom mt a^{m-t}X^t
\]

and applying the preceding identity gives exactly

\[
 \frac{\delta^kX^m(a)}{k!}
 =\sum_{t=k}^{m}\binom mt a^{m-t}S(t,k)\in\mathbb Z.
\]

Integer linearity proves the formula for every \(F\in\mathbb Z[X]\).
The edge \(k=0\) uses \(S(0,0)=1\), and the sharp control
\(\delta^kX^k(0)=k!\) is correct.

At \(k=B\), every integer-polynomial probe entry has a common \(B!\)
factor. Since \(p\leq B<q\), that factorial is divisible by \(p\) and not
by \(q\). The remaining integer multiplier can nevertheless vanish modulo
either component, so the theorem does not promise a separator for an
arbitrary probe.

Exact integer division by \(B!\) produces the normalized expression, but
modular inverse multiplication is invalid because \(B!\) is a zero
divisor modulo \(N\). The example \(\binom XB\), whose \(B\)-th
difference is one, confirms that the coefficient hypothesis cannot be
extended from \(\mathbb Z[X]\) to all integer-valued rational
polynomials.

## 4. Rational scalar shift gauges

Suppose

\[
 R(X)=\frac{h(X+1)}{h(X)}
\]

with \(h\in\mathbb Q(X)^*\). Every rational \(h\) has
\(h(X+1)/h(X)\to1\) at infinity.

Fix a translation orbit of monic irreducibles and index it by
\(P_{j+1}(X)=P_j(X+1)\). Characteristic zero makes the orbit infinite:
a nonconstant polynomial cannot be periodic under a nonzero integer
translation. If \(u_j=v_{P_j}(h)\), then

\[
 v_{P_j}(R)=u_{j-1}-u_j.
\]

The finite support of the divisor of \(h\) makes the orbit sum zero. This
proves necessity.

Conversely, let the finitely supported valuation sequence \(e_j\) on each
orbit have sum zero. The difference equation

\[
 u_{j-1}-u_j=e_j
\]

has a finitely supported integer solution obtained by cumulative sums.
The finite product of the \(P_j^{u_j}\) over all occupied orbits gives a
rational \(h_0\) whose shift quotient has the same divisor as \(R\).
Their quotient is a rational constant. Both functions tend to one, so that
constant is one. This proves sufficiency with no missing constant
condition.

Multiplication at \(X,\ldots,X+m-1\) gives the exact endpoints

\[
 \prod_{j=0}^{m-1}R(X+j)=\frac{h(X+m)}{h(X)}.
\]

The positive control \((X+1)/X\) uses \(h=X\). The negative control
\(R=X\) fails the required limit. A nonconstant polynomial, or any
positive-net-degree affine product, has the same failure.

This criterion is over \(\mathbb Q(X)\). Translation orbits can close in
finite characteristic, so characteristic-specific gauges are outside it.
After specialization modulo a composite, every endpoint denominator must
be a unit. A proper denominator gcd factors; a saturated gcd is not a
factor and does not authorize inversion.

## 5. Rational matrix gauges

Taking determinants in

\[
 G(X+1)=A(X)G(X)
\]

gives

\[
 \det A(X)=\frac{\det G(X+1)}{\det G(X)}.
\]

Thus the scalar criterion is a necessary condition for every rational
matrix gauge. If
\(\det A=X^eR_0\), where \(e\ne0\) and \(R_0\) is already a scalar
coboundary, a hypothetical gauge would make \(X^e\) a coboundary as well.
But \(X^e\) tends to infinity or zero, not one. The determinant obstruction
is therefore valid for positive and negative \(e\).

Iterating the gauge equation fixes the noncommutative order:

\[
 A(X+m-1)\cdots A(X)=G(X+m)G(X)^{-1}.
\]

This endpoint identity becomes an operational modular algorithm only after
the representation cost and every denominator unit condition are proved.

The determinant test is necessary, not sufficient. It is silent for
determinant-one systems and cannot see projective or off-diagonal
information. The displayed unipotent example is a valid telescope decoy,
not a classification of determinant-one systems.

## 6. Search and evidence boundary

The exact theorems justify rejecting a search that merely:

- truncates the regular shift and still tests \(\Delta^B\);
- applies \(\delta^B\) entrywise to integer-coefficient polynomial probes;
- asks for a rational scalar gauge without passing the orbit criterion; or
- asks for a rational matrix gauge whose determinant fails that criterion.

They do not reject another invariant of a shift subquotient, an implicit
full regular state, integer-valued polynomial machinery, a
characteristic-dependent or semilinear gauge, or a determinant-one
non-determinant mechanism. With this named-mechanism interpretation, the
statement's search decision and exact exclusions are supported.

No computation, empirical extrapolation, evaluator, factorer, or general
circuit lower bound is present.
