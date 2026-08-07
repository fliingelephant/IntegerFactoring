# F67 hostile audit — metric-guided cross-feedback kill

## Verdict: FAIL

The audited candidate has SHA-256
16a36ed682f909781d4b9f213d80def41886aea22dd99a65fc32d7db39b5d27a.

The number-theoretic theorems and the displayed arithmetic examples are
correct in their squarefree-semiprime scope. The candidate nevertheless
fails as a fully specified result because it never defines the “signed
support-two menu.” Its claimed complete menu enumerations are true only for
one particular interpretation: exactly two distinct block indices, each
with exponent \(+1\) or \(-1\), with inverse residues grouped into one
orbit. Natural support-at-most-two and repeated-index interpretations produce
additional candidates. Those candidates change the \(N=77\) retry and the
\(N=209\) menu.

The candidate also needs to state whether appending the identity or a
duplicate relation changes an occurrence budget. Without this rule, the
claimed \(N=77\) “exact fixed point” is conditional rather than fully
defined. The instruction for this audit treats ambiguity as failure, so
these are fatal specification defects even though the intended arithmetic is
sound.

This audit does not use or certify the historical claims about F26, F65,
F66, or P70.

## 1. Fatal menu ambiguity

Let the current indexed block list be
\(B_1,\ldots,B_s\). The examples behave as if the menu were

\[
\mathcal M_{=2}(B)=
\left\{
\operatorname{can}\!\left(B_i^\epsilon B_j^\eta\bmod N\right):
1\le i<j\le s,\quad
\epsilon,\eta\in\{-1,1\}
\right\},
\]

followed by deduplication into unordered inverse orbits
\(\{u,u^{-1}\}\). This definition has all of the following features:

- exactly two block indices occur;
- the indices are distinct;
- each exponent is exactly \(+1\) or \(-1\);
- there is no independent global coefficient \(-1\);
- support-zero, support-one, and repeated-index candidates are excluded.

The candidate states none of these points. “Support two” can also naturally
mean support of size at most two. That interpretation includes
\(B_i^{\pm1}\). If the menu means two block selections rather than two
distinct support indices, it also includes \(B_i^{\pm2}\) and
\(B_iB_i^{-1}=1\). If a signed exponent box is intended, exponents other than
\(\pm1\) can occur. These interpretations give different menus.

### Concrete failure at \(N=77\)

The old blocks are \(2,39\), with \(2^{-1}=39\pmod{77}\). Under
\(\mathcal M_{=2}\), the candidate's two inverse orbits are exactly

\[
\{1\},\qquad \{4,58\}.
\]

Under support at most two, the support-one orbit

\[
\{2,39\}
\]

is also present. Its score is

\[
|2-39|=37,
\]

and it survives both tickets:

\[
\gcd(37,77)=1,\qquad
\gcd(37^2+4,77)=\gcd(1373,77)=1.
\]

This orbit has lower positive score than \(\{4,58\}\), whose score is
\(54\). Its exact inverse relation \(2\cdot39=78\) is already in the
transcript. Thus, after the global identity is removed, a support-at-most-two
ranker with \(K=1\) can select an already-present relation rather than the
candidate's claimed sole nontrivial orbit. Whether that selection is ignored,
is a no-op, or expands an occurrence budget is unspecified.

Therefore these candidate statements are not definition-independent:

- “the signed support-two pair menu has the following two inverse orbits”;
- discarding global residues removes the displayed fixed-point obstruction;
- a repeated ranked round is or is not new.

### Concrete failure at \(N=209\)

For old blocks \(\{3,31,70\}\), support-one candidates add the inverse
orbits

\[
\{27,31\}\quad(\delta=4),
\qquad
\{3,70\}\quad(\delta=67).
\]

Allowing the same block twice adds

\[
\{31^2,31^{-2}\}
=\{125,102\}\quad(\delta=23),
\]

because

\[
31^2\equiv125,\qquad 27^2\equiv102\pmod{209}.
\]

All three extra orbits survive both metric tickets:

\[
\begin{array}{c|c|c}
\delta&\gcd(\delta,209)&\gcd(\delta^2+4,209)\\ \hline
4&1&1\\
23&1&1\\
67&1&1
\end{array}
\]

The candidate's statement that, apart from the identity, the old menu has
only \(\{80,81\}\) and \(\{9,93\}\) is therefore false under these natural
menu meanings. The orbit \(\{80,81\}\) remains the unique score-one orbit,
but every claim about complete enumeration, truncation with \(K>1\), and
subsequent state evolution depends on the missing definition.

This ambiguity alone requires a FAIL verdict.

## 2. The two torsion identities

Within the declared setup \(N=pq\), with distinct odd primes, Theorem 1 is
correct.

Since \(w\equiv r^{-1}\pmod\ell\) for every prime \(\ell\mid N\),

\[
r(r-w)\equiv r^2-1\pmod\ell.
\]

The residue \(r\) is a unit, so

\[
\ell\mid r-w
\quad\Longleftrightarrow\quad
r^2\equiv1\pmod\ell.
\]

Also,

\[
(r-r^{-1})^2+4=(r+r^{-1})^2
\]

modulo \(\ell\). A square is zero in the field
\(\mathbb F_\ell\) exactly when its base is zero, giving

\[
\ell\mid (r-w)^2+4
\quad\Longleftrightarrow\quad
r^2\equiv-1\pmod\ell.
\]

Equal prime supports imply the two gcd identities because \(N\) is
squarefree. The first identity is actually valid for every modulus:

\[
\gcd(r-w,N)=\gcd(r^2-1,N),
\]

since multiplication by the unit \(r\) preserves a gcd and
\(r(r-w)\equiv r^2-1\pmod N\).

The squarefree hypothesis is essential for the second gcd identity. For
example, take

\[
N=25,\qquad r=2,\qquad w=13,\qquad d=-11.
\]

Then

\[
\gcd(d^2+4,25)=\gcd(125,25)=25,
\]

whereas

\[
\gcd(r^2+1,25)=\gcd(5,25)=5.
\]

Thus equation (3) must not be exported to arbitrary odd nonsquarefree
moduli. The candidate does not do so in its formal setup, but the
squarefree qualifier must remain attached to every later use.

Finally,

\[
\gcd\bigl(\gcd(d,N),\gcd(d^2+4,N)\bigr)=1
\]

because any common odd divisor would divide both \(d\) and \(4\). This part
is correct.

## 3. Direct screens and \(\gcd(\delta,N)\)

Corollary 1 is correct with its explicit exception \(\delta=0\).

If a proper \(r-1\) or \(r+1\) screen fires, some prime divisor of \(N\)
divides \(r^2-1\), and hence divides \(d\) and \(\delta\). Conversely, if
a prime divisor of \(N\) divides \(\delta\), Theorem 1 gives
\(r^2\equiv1\) at that prime, so \(r\equiv1\) or \(-1\) there and one direct
screen fires.

When \(\delta>0\), \(r\ne w\), so \(r^2\not\equiv1\pmod N\). A firing screen
cannot equal \(N\); it is proper. Also \(0<\delta<N\), so
\(\gcd(\delta,N)\ne N\). This proves the stated equivalence and makes
\(\gcd(\delta,N)\) itself a factor.

When \(\delta=0\), \(\gcd(\delta,N)=N\) regardless of whether the
self-inverse root is global or mixed-sign. The separate \(r\pm1\) screens
are therefore necessary. For \(N=pq\), the four CRT sign choices are exactly
the two global roots and two mixed roots.

A non-self-inverse direct separator has \(\delta\) divisible by \(p\) or
\(q\), and hence

\[
\delta\ge\min(p,q).
\]

The balanced-semiprime score-gap conclusion follows. The discriminant ticket
also has the stated meaning: it factors only when \(r^2=-1\) at one of the
two primes and not the other. Its prime support is disjoint from the nonzero
direct ticket because an odd prime cannot divide both \(d\) and \(d^2+4\).

Corollary 2 is also correct. Inversion fixes \(+1\) and \(-1\) modulo every
divisor of \(N\), so the direct gcds for \(r\) and \(w\) are identical.

## 4. The perfect-square endpoint lemma

Lemma 2 is correct. If \(rw=m^2\), then the inverse relation gives

\[
m^2\equiv1\pmod N.
\]

Distinct canonical endpoints satisfy

\[
1<rw\le(N-1)(N-2)<(N-1)^2.
\]

Since \(rw\) is a square, this implies

\[
2\le m\le N-2.
\]

The canonical representative \(m\) is therefore neither \(1\) nor \(N-1\).
It is a non-global square root of one. For a product of two distinct odd
primes, its CRT signs are mixed, and the two sign gcds return the two
factors.

The \(\delta=1\) addendum is also valid. Consecutive endpoints are coprime.
If their product were square, each endpoint would be square, but there are
no two consecutive positive squares.

## 5. The fibre bound

Lemma 3 is correct for \(N=pq\). For fixed signed \(d\), the congruence

\[
r^2-dr-1\equiv0\pmod N
\]

has at most two roots modulo each prime and therefore at most four CRT roots
modulo \(N\). There is one signed value \(d=0\) and two signed values for
each \(1\le |d|\le D\), giving at most

\[
4+8D
\]

oriented residues. Every nonzero-\(d\) inverse pair occurs in the two
orientations \(d\) and \(-d\), so there are at most

\[
4+4D
\]

unordered pairs. This count does not imply that any transcript-derived menu
contains a useful fibre, as the candidate states.

## 6. The \(N=77\) example

Under the intended exactly-two-distinct-block menu, all displayed arithmetic
is correct:

\[
2\cdot39\equiv1,\qquad
2\cdot39^{-1}\equiv4,\qquad
4^{-1}\equiv58\pmod{77}.
\]

The scores are \(0\) and \(54\), and

\[
\gcd(3,77)=\gcd(5,77)=\gcd(2920,77)=1.
\]

If the identity is retained, \(K=1\), and appending
\(1\cdot1=1\) changes neither the block state nor any occurrence state, the
same identity is selected forever. That is a genuine fixed point.

The last condition is not presently specified. Earlier text permits an
“explicitly declared occurrence budget.” If every fresh indexed append,
including an identity or duplicate, changes such a budget, the next state
need not be identical. The fixed-point claim must therefore say explicitly
that identity appends are ignored by every state variable, or it must define
the budget and prove that the identity leaves it unchanged.

The minimality argument is arithmetically correct but its phrase
“nontrivial unit” should be replaced by the exact property proved:

> \(77\) is the smallest product \(pq\) of distinct odd primes for which
> there exists a unit \(r\not\equiv\pm1\pmod N\) such that both
> \(\gcd(d,N)=1\) and \(\gcd(d^2+4,N)=1\).

Indeed, every smaller such product has prime factor \(3\) or \(5\). Every
unit modulo \(3\) has square \(1\). Every unit modulo \(5\) has square
\(1\) or \(-1\). Hence at least one ticket has that local prime in its
support. At \(77\), \(r=4\) supplies the required survivor.

## 7. The monotonicity and \(N=143\) examples

The \(N=209\) monotonicity counterexample is correct:

\[
80\cdot81=1+31\cdot209,\qquad \delta=1,
\]

and both direct screens and the discriminant screen are \(1\). In contrast,

\[
10\cdot21=1+209,\qquad \delta=11,
\]

and \(\gcd(10+1,209)=11\). Thus score order alone is not monotone toward a
direct hit.

The \(N=143\) equal-score example is also correct. All four products are
\(1\) modulo \(143\), all four pairs have signed difference \(-7\), and

\[
\gcd(7,143)=\gcd(53,143)=1.
\]

The first product is \(144=12^2\), with sign screens \(11\) and \(13\).
The inequalities

\[
64^2<4148<65^2,\qquad
78^2<6150<79^2,\qquad
130^2<17018<131^2
\]

prove that the other three endpoint products are not squares. Equal score
and equal immediate torsion outcomes therefore do not determine singleton
square closure.

## 8. The genuinely adaptive \(N=209\) example

Under \(\mathcal M_{=2}\), the old-menu enumeration is correct. The old
relations imply

\[
70\equiv3^{-1},\qquad
31\equiv27^{-1}=3^{-3}\pmod{209}.
\]

Taking products of two distinct old blocks with exponents \(\pm1\) gives
exactly the identity orbit and

\[
\{9,93\},\qquad \{80,81\}.
\]

The latter is the unique positive-score-one orbit and survives both tickets.
Appending its exact relation introduces endpoints

\[
80=2^4\cdot5,\qquad81=3^4.
\]

Together with \(70=2\cdot5\cdot7\) and \(27=3^3\), complete gcd-free
refinement produces

\[
\{2,3,5,7,31\}.
\]

The next exactly-two-distinct-block menu contains \(2\cdot5=10\), and
\(\gcd(10+1,209)=11\). Thus the intended example is genuinely adaptive.

In fact, without a free global minus sign, \(10\) is not any monomial in the
old block residues, even if arbitrary exponents are allowed. All old blocks
are powers of \(3\). Modulo \(11\), \(3\) has order \(5\), so its subgroup
does not contain \(-1\equiv10\pmod{11}\). The residue \(10\) therefore
requires the newly split blocks under any ordinary monomial block menu.

This observation does not repair the missing definition. If “signed” allows
an independent global coefficient \(-1\) and a larger exponent box, then

\[
3^{20}\equiv-10\pmod{209},
\]

because \(3^5\equiv34\), \(3^{10}\equiv111\), and
\(3^{20}\equiv199=-10\pmod{209}\). Thus \(10\) can occur before refinement
as \(-3^{20}\). The candidate must say
whether such coefficients and powers are legal. Under support-at-most-two,
the additional orbits listed in Section 1 are present even though \(10\)
itself remains absent.

## 9. Required correction

To make the result pass, the candidate must add a definition equivalent to

\[
\mathcal O_t=
\left\{
\left\{u,u^{-1}\right\}:
u=\operatorname{can}
\left(B_i^\epsilon B_j^\eta\bmod N\right),
\quad i<j,
\epsilon,\eta\in\{-1,1\}
\right\},
\]

with duplicate orbits removed. It must explicitly state whether:

1. support-zero and support-one vectors are excluded;
2. repeated indices and exponents \(\pm2\) are excluded;
3. an independent global sign is excluded;
4. global orbits are removed before scoring;
5. an orbit already represented by an exact old relation is deduplicated;
6. appending an identical or identity relation changes any occurrence
   budget;
7. \(K\) counts inverse orbits after all of these filters.

If the intended menu instead has support at most two, the \(N=77\) and
\(N=209\) menu lists and every ranking-dependent conclusion must be
recomputed with the extra orbits.

The squarefree scope must remain explicit for
\(\gcd(d^2+4,N)=\gcd(r^2+1,N)\), and the \(N=77\) minimality sentence should
use the exact quantified property above. With those changes, the
number-theoretic kill argument and the three finite arithmetic mechanisms
are sound.
