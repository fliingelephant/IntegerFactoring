# F277 fresh hostile audit — PASS

## Frozen authentication

I authenticated the packet before reading any theorem, proof, self-audit,
provenance claim, or manifest claim. The required and observed SHA-256 of
`FROZEN.sha256` is

`5c7d3bb9fb87971342c0023cfb270ce88d81deb2151d220123a7f587a6178cc0`.

All five frozen entries match:

| Artifact | SHA-256 |
|---|---|
| `STATEMENT.md` | `1f4c3226ddabfc231f37f4da4b6f9ac410e225f646e82a54cbc29b845bed381a` |
| `PROOF.md` | `03eb08846cf696c064cf6c878cf12387800d821d68d9fccd884f446fa407c01a` |
| `SELF_AUDIT.md` | `ad4782161f5c8af0614e4c45e727de60dcbce5acc343ed981930e4ec5eff05f2` |
| `PROVENANCE.md` | `e0edf86c420bfe10bfbe466e6533ab7f2217d37a37d4180a86773bd62d35670f` |
| `MANIFEST.md` | `e183e65eb0d4a82e3ce11f2c808afc6e34c4ec345b98fbdf26a5ace9b9eb9e63` |

I did not modify a frozen file or a durable ledger.

## Verdict

**PASS under the literal balanced-semiprime hypotheses, named families,
and exact exclusions in `STATEMENT.md`.**

I independently reconstructed every displayed finite-difference law, both
Lucas phases, the short-side valuation screen, the central-binomial control,
both local central-Stirling congruences, the saturated examples, and the
representation-cost boundary. I found no false identity, endpoint omission
inside the stated domain, invalid modular division, missing orbit type, or
unsupported factorer claim.

Three interpretation limits must remain attached to this verdict:

1. In (7), \({m\brace B}\) is the normalized monomial difference
   \(\Delta^B X^m(0)/B!\). The literal Newton coefficient of \(X^m\) in
   the basis \(\binom Xj\) is \(B!{m\brace B}\). The boxed equation and
   every later use are correct; only the nearby phrase "Newton coefficient"
   must not erase this distinction.
2. Theorem 3 is a direct gcd **screen** and a modular evaluator. It does not
   guarantee a proper factor. A numerator product, and even one individual
   numerator factor, can have gcd \(N\). The exact edge \(U=N,V=1\) has
   \(w=1<p\) and \(\gcd(\binom N1,N)=N\).
3. The no-search conclusion is a scoped evidence disposition. It says that
   more finite hit rates do not supply the missing evaluator or a universal
   theorem. It is not a logical prohibition on a targeted exploratory search,
   and it is not an impossibility theorem for a different operational grammar.

## 1. Balanced range and hostile endpoints

Write \(q=p+d\) and \(B=p+s\). From \(p<q<2p\),

\[
 p<\sqrt{pq}<\sqrt2p<q,
\]

so \(p\le B<q\) and \(0\le s<(\sqrt2-1)p\). If \(s=0\), then
\(B=p\) and the public gcd \(\gcd(B,N)\) factors \(N\).

On \(s>0\), the inequality \(B^2\le N\) gives

\[
 p d\ge 2ps+s^2>2ps.
\]

The gap \(d\) is even, hence \(d\ge2s+2\), and therefore

\[
 q-B=d-s\ge s+2.
\]

The only possible odd primes below seven, \(p=3,5\), give \(s=0\).
Thus \(s>0\) implies \(p\ge7\), and

\[
 2s+1<2(\sqrt2-1)p+1<p,
 \qquad p-s>3.
\]

These strict inequalities are not cosmetic. The first controls the
base-\(p\) carry and the block count. The second excludes the all-fixed
block case for \(T_1\). Also \(q-B\ge3\) makes the reduced \(T_1\)
exponent strictly smaller than \(B\).

The separation of \(s=0\) is essential. For example, \(p=3,q=5\) gives
\(B=3,s=0\), but

\[
 {7\brace3}=301\equiv1\pmod5.
\]

Thus the claimed \(q\)-vanishing of \(T_1\) would be false on that
excluded branch. The public gcd has already resolved it.

## 2. Newton and binomial finite differences

For every polynomial of degree at most \(D\), interpolation at
\(0,1,\ldots,D\) gives the triangular identity

\[
 f(X)=\sum_{j=0}^D \Delta^j f(0)\binom Xj.
\]

If \(f\) is integer-valued on all integers, each iterated difference at
zero is an integer. Conversely, every integer linear combination of the
binomial polynomials is integer-valued. The different degrees make the
expansion unique.

Pascal's identity is the polynomial identity

\[
 \Delta\binom Xj=\binom X{j-1}.
\]

After \(k\) iterations, terms with \(j<k\) vanish and

\[
 \Delta^k f(a)=\sum_{j=k}^D \Delta^j f(0)\binom a{j-k}
\]

for every integer \(a\), including negative \(a\) under the standard
polynomial definition of \(\binom an\). The endpoints are correct:
\(k=0\) recovers \(f(a)\), while \(k=D\) leaves only the leading Newton
coefficient.

For a nonnegative monomial exponent \(m\), inclusion-exclusion over maps
onto \(B\) labelled targets gives

\[
 \Delta^B X^m(0)
 =\sum_{j=0}^B(-1)^{B-j}\binom Bj j^m
 =B!{m\brace B}.
\]

This is exact integer division, including the zero case \(m<B\). It does
not authorize inversion of \(B!\) modulo \(N\).

## 3. Complete shifted-binomial phase law

For

\[
 F(c)=\binom{N+c-1}{B},
\]

Pascal's identity in the upper argument gives, as an exact polynomial
identity,

\[
 \Delta_c^k F(c)=\binom{N+c-1}{B-k},\qquad 0\le k\le B.
\]

Fix \(1\le c<p\) and put \(m=B-k\). If \(k\le s\), then
\(m=p+(s-k)<q\). Modulo \(q\), the upper low digit is \(c-1\), while
\(m\ge p>c-1\), so Lucas gives zero. Modulo \(p\), the lower digits are
\((1,s-k)\), while division of \(N+c-1\) by \(p\) leaves quotient \(q\)
and remainder \(c-1\). Thus

\[
 \binom{N+c-1}{m}
 \equiv q\binom{c-1}{s-k}\pmod p.
\]

The integer on the right is also zero modulo \(q\), so CRT gives the first
line of (10).

If \(k>s\), then \(0\le m<p<q\). Lucas at either hidden prime reduces
the same coefficient to

\[
 \binom{c-1}{m}=\binom{c-1}{B-k}.
\]

Hence the second phase really has identical local residues. The transition
endpoints are exact: \(k=s\) is still in the asymmetric phase and has
residue \(q\) when \(c=1\); \(k=s+1\) is already in the common phase;
and \(k=B\) gives one. Therefore

\[
 \Delta_c^kF(1)\equiv
 \begin{cases}
 q,&k=s,\\
 1,&k=B,\\
 0,&0\le k<B,\ k\ne s
 \end{cases}
 \pmod N.
\]

This locates the spike only if the hidden value \(s\) is already known.
Taking differences past it removes the local asymmetry.

## 4. Short-side quotient, gcd screen, and central control

By symmetry choose \(w=\min(V,U-V)\). Then

\[
 \binom UV=\frac{P}{w!},
 \qquad
 P=\prod_{i=1}^w(U-w+i).
\]

If \(w<p\), then \(w<q\) as well. Thus \(w!\) is a unit modulo \(N\),
and for either \(r\in\{p,q\}\),

\[
 v_r\binom UV
 =\sum_{i=1}^w v_r(U-w+i).
\]

Consequently, \(r\) divides the binomial coefficient exactly when it
divides a displayed numerator factor. This is the same event that Kummer
describes by a carry, but no computation in a hidden base is needed.

Computing \(\gcd(P,N)\) can return \(1,p,q\), or \(N\). If different
numerator factors carry the two primes, individual gcds separate them. If
one factor is a multiple of \(N\), the individual screen can remain
saturated. In all cases, the coefficient modulo \(N\) is still obtained
from \(P(w!)^{-1}\). The numerical-QP cost statement also requires the
public endpoints to have numerical-QP bit length; interpreted as part of
the input length, this is automatic.

For the exact control,

\[
 \Delta^B\binom X{2B}\bigg|_{X=2B}=\binom{2B}{B}.
\]

In base \(p\), \(B=p+s\) has digits \((1,s)\), and \(2s<p\) prevents a
carry in \(B+B\). In base \(q\),

\[
 B<q<2p\le2B<2q,
\]

so the sum has exactly one carry. Kummer therefore gives

\[
 v_p\binom{2B}{B}=0,
 \qquad
 v_q\binom{2B}{B}=1,
\]

and the gcd with the squarefree modulus is exactly \(q\). This is an exact
gate presentation, not an evaluator for a remote central coefficient.

## 5. The two local central-Stirling laws

### The \(q\)-components

Let

\[
 e_0=2B-q+1,
 \qquad e_1=2B-q+2.
\]

Since \(q<2p\le2B\), both exponents are positive. Since
\(q-B\ge s+2\ge3\),

\[
 e_0<e_1<B.
\]

The positivity avoids a hidden \(0^0\) endpoint. Fermat gives, for every
integer \(j\),

\[
 j^{2B}\equiv j^{e_0},
 \qquad
 j^{2B+1}\equiv j^{e_1}pmod q.
\]

Insert these congruences into the finite-difference numerator. Since
\(e_i<B\), the corresponding \(B\)-th differences are exactly zero.
Also \(B<q\), so \(B!\) is invertible modulo \(q\). Hence

\[
 {2B\brace B}\equiv {2B+1\brace B}\equiv0\pmod q.
\]

### The \(p\)-components

Let a cyclic group of order \(p\) act on the element set through two
disjoint \(p\)-cycles. Use \(2s\) additional fixed points for \(T_0\),
and \(2s+1\) for \(T_1\). Nonfixed orbits of set partitions have size
\(p\), so only invariant partitions contribute modulo \(p\).

The induced action on the \(B=p+s<2p\) blocks has either no moving block
orbit or exactly one orbit of \(p\) blocks. If all blocks are fixed, each
element \(p\)-cycle is one indivisible atom. The maximum atom counts are
\(2s+2\) for \(T_0\) and \(2s+3\) for \(T_1\). The inequalities above
make both counts smaller than \(p+s\), so this case is impossible.

Suppose there is one moving orbit and \(s\) fixed blocks. A globally fixed
element cannot lie in a moving block because it would then lie in every
translate of that block. Each element \(p\)-cycle is therefore either
intact in a fixed block or split with exactly one point in each moving
block.

For \(T_0\), splitting exactly one element cycle gives two choices. The
intact cycle and \(2s\) fixed points form \(2s+1\) atoms for the \(s\)
fixed blocks. Splitting both cycles gives \(p\) relative phases, followed
by a partition of the \(2s\) fixed points. Thus the exact invariant count
is

\[
 2{2s+1\brace s}+p{2s\brace s},
\]

which proves

\[
 T_0\equiv2{2s+1\brace s}\pmod p.
\]

For \(T_1\), the same classification gives the exact invariant count

\[
 2{2s+2\brace s}+p{2s+1\brace s},
\]

and hence

\[
 T_1\equiv2{2s+2\brace s}\pmod p.
\]

No invariant-partition type is missing. In particular, at least one
element cycle must split to populate the moving blocks, and the relative
phase in the two-split case is precisely the factor \(p\).

Because \(q\mid T_i\) and \(N=pq\), each gcd is \(q\) or \(N\) according
as its displayed \(p\)-residue is nonzero or zero. Since \(p\) is odd,
the pair is simultaneously saturated exactly when

\[
 p\mid{2s+1\brace s}
 \quad\text{and}\quad
 p\mid{2s+2\brace s}.
\]

The recurrence

\[
 {2s+2\brace s}
 =s{2s+1\brace s}+{2s+1\brace{s-1}}
\]

gives exactly the equivalent condition (24). It supplies no nonvanishing
theorem.

## 6. Saturated examples

For \(p=37,q=47\),

\[
 N=1739,qquad 41^2=1681<N<1764=42^2,
\]

so \(B=41,s=4\). Also

\[
 {9\brace4}=7770,
 \qquad 2\cdot7770=37\cdot420.
\]

The local \(p\)-residue of \(T_0\) vanishes, and its \(q\)-residue always
vanishes, so \(\gcd(T_0,N)=N\).

For \(p=19,q=29\),

\[
 N=551,qquad 23^2=529<N<576=24^2,
\]

so \(B=23,s=4\). Also

\[
 {10\brace4}=34105,
 \qquad 2\cdot34105=19\cdot3590.
\]

Thus \(\gcd(T_1,N)=N\). The four displayed factors are primes, and both
pairs obey \(p<q<2p\). These examples refute either scalar as an all-input
factor oracle. They say nothing about simultaneous saturation.

## 7. Evaluator and search boundary

The exact identities do not supply a numerical-QP evaluator for \(T_0\)
or \(T_1\):

1. Literal inclusion-exclusion has \(B+1\) summands. Its division by
   \(B!\) cannot be performed by modular inversion because
   \(\gcd(B!,N)=p\), using \(p\le B<q\).
2. The ordinary division-free Stirling recurrence has a literal index
   range reaching \(B\).
3. Pair partitions give
   \({2B\brace B}\ge(2B)!/(2^BB!)\), while labelled assignments give
   \({2B\brace B}\le B^{2B}\). Hence its bit length is
   \(\Theta(B\log(B+1))\). Injecting a partition by adjoining one element
   to the block that contains element 1 gives the same lower order for
   \({2B+1\brace B}\), and \(B^{2B+1}\) is an upper bound.

Since \(B\) is exponential in \(\log N\), these literal procedures are
not numerical-QP. None of these observations excludes a different succinct
modular algorithm. In particular, a nonunit denominator is not evidence
that every division-free or circuit representation must be large.

The exact shifted law and the short-side screen do make more finite hit-rate
searches over those same presentations redundant. For the central pair,
finite nonvanishing data cannot prove the universal condition, and neither
positive nor negative hit rates construct the missing remote evaluator.
Accordingly, the packet's no-search decision is supported as a disposition
for promotion evidence. It must retain the explicit exclusions: no general
circuit lower bound, evaluator, joint nonvanishing theorem, probability law,
factor oracle, or integer-factoring algorithm follows.

## 8. Small exact counterexample checks

As audit-only sanity checks, I enumerated the 427 unresolved balanced pairs
with odd primes \(p,q\le211\). For every pair I checked both Stirling local
laws, the central-binomial gcd, and (for every allowed \(c,k\)) the complete
shifted-binomial congruence. I also exhaustively checked the short-side
divisibility equivalence for \(0\le U\le3N\) at \((p,q)=(7,11)\) and
\((19,29)\). All checks passed.

No simultaneous \(T_0,T_1\) saturation occurred in that small range. This
absence is not proof, probability evidence, or support for joint
nonvanishing. The \(s=0\) example and the saturated short-numerator example
above confirm that the packet's branch and gcd-screen qualifications are
necessary.
