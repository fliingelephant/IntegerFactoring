# Proof-blind reconstruction: swap-invariant phase labels

## Scope and notation

Let \(\ell\) be prime, let \(V=\mathbf F_\ell^2\) be additive, and let
\(s(x,y)=(y,x)\).  Fix a primitive \(\ell\)-th root of unity \(\zeta\), so
that exponents identify \(\mu_\ell\) with the additive group
\(\mathbf F_\ell\).  Define

\[
q(x,y)=x+y,\qquad A=\ker q=\{(t,-t):t\in\mathbf F_\ell\}.
\]

Here “rank” means rank over \(\mathbf F_\ell\) after taking exponents.  A
statement that a transcript cannot reveal the anti-diagonal means the strong,
prior-free statement that it is identical at \(v\) and \(v+a\) for every
\(a\in A\).  It does not deny correlations introduced by an external prior.

## 1. Exact character classification and joint kernel

Every group character \(\chi:V\to\mu_\ell\) has a unique form

\[
\chi_{u,v}(x,y)=\zeta^{ux+vy},\qquad (u,v)\in\mathbf F_\ell^2.
\]

The condition \(\chi\circ s=\chi\) is equivalent to

\[
uy+vx=ux+vy\quad\hbox{for every }x,y,
\]

hence to \(u=v\).  Thus the complete list is

\[
\chi_c(x,y)=\zeta^{c(x+y)}=\zeta^{cq(x,y)},\qquad c\in\mathbf F_\ell.
\]

For an arbitrary family \((\chi_{c_i})_{i\in I}\), including an empty or
infinite family, the joint exponent map is

\[
V\longrightarrow\mathbf F_\ell^I,qquad
(x,y)\longmapsto (c_iq(x,y))_{i\in I}.
\]

Therefore its exact rank and kernel are

\[
\begin{array}{c|c|c|c}
\text{condition}&\text{rank}&\text{kernel}&\text{image size}\\ \hline
c_i=0\text{ for every }i&0&V&1\\
c_i\ne0\text{ for some }i&1&A&\ell.
\end{array}
\]

In particular, adding more individually invariant scalar characters never
raises the rank from one to two.

## 2. Closure under the listed operations

The useful invariant is stronger than swap symmetry: every admissible scalar
label factors through the quotient \(q:V\to V/A\cong\mathbf F_\ell\).

Suppose a protocol, possibly with public randomness, works as follows.  At
each step it chooses an individually swap-invariant scalar character using
only public data, public randomness, and earlier admissible labels; it may
multiply the returned character value by a fixed public phase.  Then, for each
fixed public random seed, its entire variable-length transcript \(T\) obeys

\[
T(v+a)=T(v)\qquad(v\in V, a\in A).
\]

This follows by induction.  Earlier transcripts agree at \(v\) and \(v+a\),
so the protocol makes the same next choice, and the next chosen character also
agrees because it factors through \(q\).  The same proof covers adaptive
stopping.

Concretely:

- A fixed public phase or a fixed additive twist contributes only a known
  constant: \(\chi_c(v+w)=\chi_c(w)\chi_c(v)\).
- A common public unit scaling gives
  \(\chi_c(uv)=\zeta^{cuq(v)}\).
- Integer powers replace \(c\) by \(nc\), modulo \(\ell\).
- Multiplication and division add and subtract the coefficients \(c\).
- Any adaptive choice based only on previous admissible labels remains
  constant on every coset of \(A\).
- A postselection event defined solely from the transcript is a union of
  whole \(A\)-cosets.  Conditioning on it cannot split a fixed \(q\)-fiber.

Thus none of these operations reveals an anti-diagonal component.  The exact
claim is fiberwise indistinguishability.  If a prior correlates \(q(v)\) with
the anti-diagonal coordinate, observing \(q(v)\) can of course change a
Bayesian posterior; that information came from the prior, not from a
refinement of the character fibers.

“Fixed public unit twist” needs the admissibility qualifier.  Independently
scaling the two factors gives \(c(ux+vy)\), which is swap-invariant only when
\(u=v\) (or \(c=0\)).  Unequal factorwise twists can sense the anti-diagonal,
but they have left the stated class of labels.  For example, at odd \(\ell\),
applying the twist \((x,y)\mapsto(x,-y)\) before \(\chi_1\) returns
\(\zeta^{x-y}\) directly.

## 3. Quantifier leaks and explicit counterexamples

Coordinatewise invariance cannot be replaced by equivariance or by invariance
of an aggregate object.

1. The ordered vector
   \[
   F(x,y)=(\zeta^x,\zeta^y)
   \]
   is swap-equivariant: \(F(s(x,y))\) swaps its two coordinates.  It is a
   faithful rank-two group homomorphism with kernel zero.  Its two scalar
   coordinates are not individually swap-invariant.

2. The multiset
   \[
   M(x,y)=\{\zeta^x,\zeta^y\}
   \]
   is genuinely swap-invariant, but it is not a group character and it does
   not factor through \(q\).  For odd \(\ell\), write \(d=x-y\).  The pair
   \((q,d)\) recovers \((x,y)\), while the multiset identifies only
   \(d\sim-d\).  Consequently there are \((\ell+1)/2\) distinct multiset
   labels on each fixed-\(q\) fiber.  For example, \((0,0)\) and
   \((1,-1)\) have the same sum but different multisets.

3. Even a scalar swap-invariant function need not obey the obstruction if the
   character hypothesis is dropped.  For odd \(\ell\),
   \(\zeta^{(x-y)^2}\) is swap-invariant and detects anti-diagonal magnitude,
   but it is not a character.

Hence a family stable under swapping its coordinates, an ordered
swap-equivariant transcript, an unordered multiset transcript, addition of
character values, or a general nonlinear symmetric statistic is outside the
rank-one theorem.  Likewise, adaptive choices using hidden factor identity or
other anti-diagonal side information are outside the label-only hypothesis.

## 4. Product over every prime above a rational prime

The proposed cyclotomic statement is true.

Let \(\ell\) be odd, \(K=\mathbf Q(\zeta_\ell)\), and let the rational prime
\(p\equiv1\pmod\ell\).  Let \(a\in\mathbf Q^\times\) have numerator and
denominator prime to \(p\); this includes every rational integer coprime to
\(p\).  For a prime ideal \(\mathfrak P\mid p\), use the convention

\[
\left(\frac a{\mathfrak P}\right)_\ell
\equiv a^{(p-1)/\ell}\pmod{\mathfrak P},
\qquad
\left(\frac a{\mathfrak P}\right)_\ell\in\mu_\ell.
\]

Because \(p\equiv1\pmod\ell\), it splits completely and
\(G=\operatorname{Gal}(K/\mathbf Q)\) acts simply transitively on the primes
above \(p\).  Fix \(\mathfrak P_0\) and put
\(\alpha=(a/\mathfrak P_0)_\ell\).  Since every \(\sigma\in G\) fixes the
rational number \(a\), applying \(\sigma\) to the defining congruence gives

\[
\left(\frac a{\sigma\mathfrak P_0}\right)_\ell=\sigma(\alpha).
\]

It follows that

\[
\prod_{\mathfrak P\mid p}
\left(\frac a{\mathfrak P}\right)_\ell
=\prod_{\sigma\in G}\sigma(\alpha)
=N_{K/\mathbf Q}(\alpha).
\]

Writing \(\alpha=\zeta_\ell^m\), this norm is

\[
\zeta_\ell^{m\sum_{k=1}^{\ell-1}k}
=\zeta_\ell^{m\ell(\ell-1)/2}=1,
\]

because \(\ell\) is odd.  The inverse residue-symbol convention gives the
inverse of the same norm and therefore the same result.

The quantifiers matter.  A single selected prime above \(p\), or a proper
subset of the primes above \(p\), need not give product one.  Rationality of
\(a\) is what makes the symbols a complete Galois orbit.  For \(\ell=2\) the
assertion fails in general: it reduces to a Legendre symbol.  If \(p\mid a\),
the symbol is zero or undefined rather than an element of \(\mu_\ell\).

There are small explicit counterexamples to the two tempting
generalizations.  For \(\ell=3,p=7\), at
\(\mathfrak P_{7,2}=(7,\zeta-2)\),
\((2/\mathfrak P_{7,2})_3=\zeta^2\ne1\), so a one-prime subproduct fails.  If
rationality is dropped and \(a=\zeta\), then at both primes above 7 the symbol
is \(\zeta^2\), so their product is \(\zeta\ne1\).

## 5. Complete finite certificate for \(\ell=3\), \(N=91\)

Write \(N=7\cdot13\), choose \(\rho=16\), and let
\(\Phi_3(X)=X^2+X+1\).  The reductions of \(\rho\) are

\[
r_7=2\pmod7,\qquad r_{13}=3\pmod{13}.
\]

For \(a\in(\mathbf Z/91\mathbf Z)^\times\), define
\(e_p(a)\in\mathbf F_3\) by

\[
a^{(p-1)/3}\equiv r_p^{e_p(a)}\pmod p,
\qquad p\in\{7,13\}.
\]

The requested values are:

\[
\begin{array}{c|c|c|c}
a&e_7(a)&e_{13}(a)&e_7(a)+e_{13}(a)\\ \hline
15&0&1&1\\
18&1&0&1\\
16&2&1&0
\end{array}
\]

The direct congruences are

\[
\begin{array}{c|c|c}
a&a^2\bmod7&a^4\bmod13\\ \hline
15&1=2^0&3=3^1\\
18&2=2^1&1=3^0\\
16&4=2^2&3=3^1.
\end{array}
\]

Thus \(15\) and \(18\) have the same scalar product phase but distinct,
swapped local pairs.  The value \(16\) has scalar product one while its local
pair is the nonzero anti-diagonal pair \((2,1)\).

The exponent pairs depend on the root, equivalently on the selected primes
and the convention for \(\zeta\).  For completeness, all four global roots
give:

\[
\begin{array}{c|ccc}
\rho&(e_7(15),e_{13}(15))&(e_7(18),e_{13}(18))&(e_7(16),e_{13}(16))\\ \hline
9 &(0,2)&(1,0)&(2,2)\\
16&(0,1)&(1,0)&(2,1)\\
74&(0,2)&(2,0)&(1,2)\\
81&(0,1)&(2,0)&(1,1).
\end{array}
\]

Replacing a root by its Galois conjugate negates both exponents.  Replacing
only one local CRT component negates only that component.  The fiber sizes
below are unchanged because these are bijections of \(\mathbf F_3^2\).

### Fiber sizes

The domain here is explicitly the 72-element unit group; power-residue phases
are not defined in \(\mu_3\) for nonunits.  CRT gives

\[
(\mathbf Z/91\mathbf Z)^\times\cong
\mathbf F_7^\times\times\mathbf F_{13}^\times.
\]

The two local cubic characters are surjective and have kernel sizes \(2\) and
\(4\).  Hence every ordered pair in \(\mathbf F_3^2\) has exactly
\(2\cdot4=8\) preimages.  Each scalar sum in \(\mathbf F_3\) combines three
ordered-pair fibers and has exactly 24 preimages.

For the unordered multiset \(\{e_7,e_{13}\}\), the exact fibers are

\[
\begin{array}{c|cccccc}
\text{multiset}&\{0,0\}&\{0,1\}&\{0,2\}&\{1,1\}&\{1,2\}&\{2,2\}\\ \hline
\text{size}&8&16&16&8&16&8.
\end{array}
\]

The off-diagonal sizes double because the multiset merges two ordered pairs.
This is the finite version of the multiset quantifier leak.

### All roots and their gcd relations

The roots of \(\Phi_3\) modulo 7 are \(2,4\), and those modulo 13 are
\(3,9\).  CRT gives exactly four roots modulo 91:

\[
\begin{array}{c|c|c}
\rho&\rho\bmod7&\rho\bmod13\\ \hline
9&2&9\\
16&2&3\\
74&4&9\\
81&4&3.
\end{array}
\]

Their pairwise difference gcds are

\[
\begin{array}{c|rrrr}
\gcd(|\rho-\rho'|,91)&9&16&74&81\\ \hline
9&-&7&13&1\\
16&&-&1&13\\
74&&&-&7\\
81&&&&-
\end{array}
\]

Two roots sharing exactly one local CRT component expose the corresponding
factor by their difference.  Roots differing at both components are Galois
conjugates in the pairs

\[
9^2\equiv81,qquad16^2\equiv74\pmod{91},
\]

and their difference gcd is one.

### What \(\rho\) and \((N,\zeta-\rho)\) mean

Let \(\mathcal O=\mathbf Z[\zeta]\), where \(\zeta^2+\zeta+1=0\), and put

\[
I_\rho=(N,\zeta-\rho)\subset\mathcal O.
\]

The root congruence makes evaluation well-defined:

\[
\mathcal O\longrightarrow\mathbf Z/N\mathbf Z,qquad
f(\zeta)\longmapsto f(\rho)\pmod N.
\]

This map is surjective, its kernel is exactly \(I_\rho\), and therefore

\[
\mathcal O/I_\rho\cong\mathbf Z/N\mathbf Z,
\qquad |\mathcal O/I_\rho|=N.
\]

So a root does define an integral ideal of norm \(N\).  Once the rational
factorization is known, it selects one prime above each rational factor.  With
\(\mathfrak P_{p,r}=(p,\zeta-r)\), for example,

\[
I_{16}=\mathfrak P_{7,2}\mathfrak P_{13,3},\qquad
I_{74}=\mathfrak P_{7,4}\mathfrak P_{13,9},\qquad
I_{16}I_{74}=(91).
\]

It does **not** make \(I_\rho\) prime when \(N\) is composite: its quotient is
\(\mathbf Z/91\mathbf Z\), not a field.  It is not a “prime above \(N\),” it
does not certify that \(N\) is prime, and it does not select all primes above
one rational prime.  Thus the theorem in Section 4 does not force the product
over the prime factors selected by \(I_\rho\) to be one.  For instance, the
selected product exponent for \(a=15\) is one.

A single root also need not expose a nontrivial rational factor through the
usual immediate gcds: for \(\rho=16\),
\(\gcd(\rho-1,91)=1\), while the cyclotomic congruence itself gives gcd 91.
Additional roots can expose factors through the difference table above.  The
ideal description records the CRT choices mathematically; it does not by
itself decode those choices without factoring or equivalent extra
information.

## 6. Finite counterexample search

The accompanying verifier exhaustively checked the character classification
for \(\ell=2,3,5,7,11\), checked the \(N=91\) certificate and every unit fiber,
and searched the cyclotomic product assertion for every odd prime
\(\ell<32\), every rational prime \(p<2000\) with
\(p\equiv1\pmod\ell\), and every \(1\le a<p\).  This covered 386 pairs
\((\ell,p)\), 357,334 values of \(a\), and 2,783,012 individual residue-symbol
evaluations, with no counterexample.  These computations corroborate but do
not replace the proofs above.

Reproduction details and hashes are in `RUN_MANIFEST.md`; the complete machine
output is in `certificate_output.json`.
