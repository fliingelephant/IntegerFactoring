# F214 hostile audit

## Verdict

**FAIL.** Parts 1, 2, and 4--9 of the frozen theorem survive hostile
reconstruction at their stated narrow scope. The first paragraph of Part 3
does not. A balanced-semiprime full-\(K\) selector does not justify the claimed
recursive factoring recurrence, because the child \(K=(N-1)/2\) need not be a
balanced semiprime, or even a semiprime. The promise is not hereditary.

This is a failure of the stated recursive consequence. It is not a
counterexample to the full-\(K\) collapse, the singleton theorem, the
Gao--Feng--Hu--Pan terminal, or any of the explicit-representation bounds.

The repair would require a new premise. For example, the theorem could assume
a correct all-input recursive factorer whose complete call tree has at most one
near-size child at every node. Alternatively, it could state only the local
bit-size bookkeeping at one balanced node. Neither premise appears in the
frozen statement, so this audit does not make that repair.

## Frozen-input integrity

I computed all four required hashes before reading the mathematical contents.
They match exactly.

| File | Expected SHA-256 | Observed SHA-256 | Result |
|---|---|---|---:|
| `STATEMENT.md` | `4254fce5cbd941e92328af90ae13adc8bd896e0559cdb5bff7bf92c12705d26f` | `4254fce5cbd941e92328af90ae13adc8bd896e0559cdb5bff7bf92c12705d26f` | PASS |
| `PROOF.md` | `47709b22bd4d53a7e4a2be48c092f53be6a369add17007a547672db603b80eee` | `47709b22bd4d53a7e4a2be48c092f53be6a369add17007a547672db603b80eee` | PASS |
| `SELF_AUDIT.md` | `7964f48d43e34f853dd3b965a393ed42e395426277550de071004be154157f4f` | `7964f48d43e34f853dd3b965a393ed42e395426277550de071004be154157f4f` | PASS |
| `PROVENANCE.md` | `fe22a4be53d8603736d462488fc4dd8480dc9305aa098d74dd24c72ff84085e2` | `fe22a4be53d8603736d462488fc4dd8480dc9305aa098d74dd24c72ff84085e2` | PASS |

The manifest is intentionally not self-hashed. Its observed SHA-256 is
`939cb1ae1e9fe840c0dc96ef024d3489516ec2d1963a7146c9e7e81d7b8e0465`.

I did not edit a frozen input or a durable ledger.

## 1. Full-\(K\) product window

The strict product-window argument is correct.

For every integer point in the continuous box,

\[
\frac{N}{\sqrt 2}<XY<\sqrt 2N.
\]

Thus, for \(D=XY-N\),

\[
-\left(1-\frac1{\sqrt2}\right)N
<D<(\sqrt2-1)N.
\]

The positive endpoint is below \(K=(N-1)/2\) as soon as

\[
\left(\frac32-\sqrt2\right)N>\frac12,
\]

which holds for integer \(N\ge 7\). The negative endpoint has magnitude below
\(K\) as soon as

\[
\left(\frac1{\sqrt2}-\frac12\right)N>\frac12,
\]

which holds for integer \(N\ge 3\). A balanced product of distinct odd primes
has \(N\ge15\), so both inequalities have strict slack. There is no endpoint
equality problem.

Since \(K\mid D\) and \(-K<D<K\), one gets \(D=0\). Positivity,
semiprimality, and \(X<\sqrt N<Y\) then force \((X,Y)=(p,q)\). Also

\[
\gcd(N,K)=\gcd\left(N,\frac{N-1}{2}\right)=1.
\]

Any congruent \(X\) in a box point is consequently a unit modulo \(K\), so
the congruence and inverse formulations have the same points. Oddness and the
endpoint predicate are indeed unused.

**Attack result: PASS.** Claims (2) and (3), including their strict endpoint
conventions, are correct.

## 2. Singleton threshold

If \(X_1,X_2\) are odd and congruent modulo \(m\), then \(X_1-X_2\) is
divisible by both \(2\) and \(m\), hence by
\(s_m=\operatorname{lcm}(2,m)\). A nonzero such difference has magnitude at
least \(s_m\). The strict diameter bound in (4) therefore permits at most one
representative in each of \(P_m(a)\) and \(Q_m(a)\).

When both sets are the singletons \(\{X\}\) and \(\{Y\}\), the two endpoint
products in (1) are the same. The predicate becomes

\[
XY\le N\le XY,
\]

so \(XY=N\). The interval ordering then selects the nontrivial factor pair.
This argument also works when \(m\) is even. It does not assume that
\(\gcd(m,N)=1\).

**Attack result: PASS.** The theorem does not claim an efficient way to find
the live branch, and no such claim is implicit in this proof.

## 3. Recursive consequence: material failure

The size calculations at one balanced node are correct:

\[
K=(N-1)/2<2^{n-1}
\]

makes \(K\) an at-most-\((n-1)\)-bit child, and

\[
0<E=N-B^2<2B+1<2\sqrt N+1
\]

makes \(E\) an \(n/2+O(1)\)-bit child. P183 also correctly proves that an
*already justified* recurrence

\[
T(n)\le T(n-1)+Q(n)T(n/2+O(1))+Q(n)
\]

is numerical QP.

The missing step is correctness and closure of the \(T(n-1)\) call. The only
new algorithmic premise in F214 is a uniform subroutine that returns the point
in (3). Equation (3) is guaranteed to contain \((p,q)\) only under F214's
balanced, distinct-odd-semiprime setup. A promise algorithm on that setup may
do anything on an arbitrary child \(K\). Uniformity does not extend its
promise.

A concrete counterexample to closure is

\[
N=247=13\cdot19,
\qquad 13<19<2\cdot13.
\]

Here

\[
K=(247-1)/2=123=3\cdot41.
\]

The child is unbalanced because \(41>2\cdot3\). Its own balanced sets are

\[
P=\{9,11\},\qquad Q=\{13,15\}.
\]

With the child's full modulus \((123-1)/2=61\), there is no pair in
\(P\times Q\) whose product is congruent to \(123\pmod {61}\). Equivalently,
the child's version of (3) is empty. In particular, the proposed selector
cannot be invoked recursively to recover \(3\) and \(41\).

This is exactly the nonhereditary-promise issue guarded in the hostile audit
of F207/P183: balancedness at a parent does not imply balancedness at its
decrement child. P183 proves the complexity of a recurrence. It does not
construct an all-input factorer or prove that F214's selector induces that
recurrence.

The statements that there is only one *possible* near-size child at the
current balanced node, and that all declared side children are half-size, are
valid local bookkeeping. The stronger frozen sentence that the “resulting
accounting has the P183 form” and is numerical QP does not follow from the
selector premise.

The disclaimer that F214 is “not an all-input factoring algorithm” does not
repair the implication. It instead confirms that the required all-input
premise is absent. `SELF_AUDIT.md` items 23--26 likewise check sizes and the
number of near-size terms but do not check closure of the recursive domain.

**Attack result: FAIL.** Part 3 must either add a recursive-closure premise or
be weakened to a one-node size statement.

## 4. Gao--Feng--Hu--Pan terminal

I checked the current primary PDF of Gao, Feng, Hu, and Pan,
[“On Factoring and Power Divisor Problems via Rank-3 Lattices and the Second
Vector”](https://eprint.iacr.org/2025/1004.pdf). The ePrint record identifies a
2025-11-11 revision. Its Theorem 3.1 takes natural \(N,s\), a modulus
\(m\in(\mathbb Z/N\mathbb Z)^*\), and \(s,m<N\). It finds all primes in the
selected class \(p\equiv s\pmod m\) with \(p^r\mid N\), within the stated
deterministic bit bound.

For F214, reduce each listed residue to \([0,m)\) and set \(r=1\). At the true
entry, \(p\equiv s\pmod m\). The premise \(\gcd(m,N)=1\) makes \(m\) a unit
modulo \(N\), and it also makes the true residue nonzero. The declared bounds
give \(s,m<N\). The source's cost becomes

\[
O\!\left(
\left\lceil\frac{N^{1/4}}m\right\rceil
\log^{7+3\epsilon}N
\right).
\]

Under (7), the ceiling is at most a numerical-QP factor, up to an inessential
additive one. A numerical-QP number of calls, exact divisions, and output
checks remain numerical QP. The theorem finds primes in one selected residue
class; F214 correctly uses Theorem 3.1 rather than the stronger-premise
Corollary 3.2.

The list-cardinality premise alone does not charge the cost of constructing
the list. F214's wording here claims only that applying the terminal to an
already produced list is numerical QP, so this is not a defect.

**Attack result: PASS.** Endpoint liveness alone is correctly excluded from
the terminal premise.

## 5. Direct scans and the totient bound

The two real interval lengths are

\[
\left(1-2^{-1/2}\right)\sqrt N,
\qquad
(\sqrt2-1)\sqrt N.
\]

Counting odd integers contributes density \(1/2\) and an \(O(1)\) endpoint
error. Equation (8) is correct.

For an odd prime power \(\ell^a\),

\[
\frac{\varphi(\ell^a)^2}{\ell^a}
=\ell^{a-2}(\ell-1)^2\ge1.
\]

For \(2^a\), the ratio is \(1/2\) at \(a=1\) and at least one at
\(a\ge2\). Multiplicativity gives

\[
\varphi(r)^2\ge r/2
\]

for every positive integer \(r\), and hence (9).

One wording defect occurs in `MANIFEST.md` claim 5. It says that “interval
and unit scans have \(\Theta(\sqrt N)\) candidates.” The theorem proves that
the two interval scans have \(\Theta(\sqrt N)\) candidates. The unit scan has
exactly \(\varphi(K)\) candidates and only the lower bound
\(\varphi(K)=\Omega(\sqrt N)\) is proved. The statement and proof themselves
use the correct formulation. The manifest should not summarize this as a
uniform \(\Theta(\sqrt N)\) claim.

**Attack result: PASS for equations (8) and (9); manifest summary requires
correction.** These are explicit enumeration counts, not implicit-algorithm
lower bounds.

## 6. Explicit paired CRT

CRT gives the exact product

\[
U(K)\cong\prod_i U(k_i).
\]

If every local unit coordinate is assigned to one of two blocks and every
assignment is materialized, the list sizes are

\[
A=\prod_{i\in I}\varphi(k_i),
\qquad
B=\prod_{i\notin I}\varphi(k_i).
\]

Thus \(AB=\varphi(K)\), including an empty block, and one list has size at
least \(\sqrt{\varphi(K)}\). Equation (9) then gives (10). The conversion

\[
(K/2)^{1/4}=N^{1/4+o(1)}
\]

is valid because \(K=(N-1)/2\).

**Attack result: PASS.** The conclusion is restricted to materialized
assignment lists. It says nothing about compressed or adaptive CRT methods.

## 7. Prime-power fibers of \(u+u^{-1}\)

A root of

\[
z^2-sz+1\equiv0\pmod K
\]

is automatically a unit modulo \(K\), because a prime common to \(z\) and
\(K\) would reduce the left side to one. The root set is therefore exactly
the fiber of \(z\mapsto z+z^{-1}\).

For an odd prime power \(\ell^a\), the change \(t=2z-s\) is bijective and
gives

\[
t^2\equiv s^2-4\pmod{\ell^a}.
\]

If the right side vanishes modulo \(\ell^a\), the number of roots is exactly
\(\ell^{\lfloor a/2\rfloor}\). Otherwise, a solution requires valuation
\(2h<a\). After \(t=\ell^h w\), the unit square congruence modulo
\(\ell^{a-2h}\) has at most two roots. Each has \(\ell^h\) lifts to the
required modulus for \(w\), so there are at most

\[
2\ell^h\le2\sqrt{\ell^a}
\]

roots. An odd valuation cannot occur for a square.

For \(2^a\), any nonempty image residue is even. Writing an even
representative as \(s=2h\) gives the exact translation

\[
(z-h)^2\equiv h^2-1\pmod{2^a}.
\]

The zero right side has \(2^{\lfloor a/2\rfloor}\) roots. In the nonzero
case, a solution again requires valuation \(2h_0<a\). The remaining odd unit
square congruence modulo \(2^{a-2h_0}\) has at most four roots, because the
kernel of squaring on \(U(2^b)\) has size at most four. Each root has
\(2^{h_0}\) relevant lifts. The local count is therefore at most

\[
4\,2^{h_0}\le4\sqrt{2^a}.
\]

CRT multiplies the local counts. If \(K_{\rm odd}\) has \(r\) distinct prime
divisors, this yields

\[
|\psi_K^{-1}(s)|
\le4\,2^r\sqrt K.
\]

The retained factor four is loose but valid when \(K\) is odd. Partitioning
all \(\varphi(K)\) units into fibers proves (12).

**Attack result: PASS.** Every valuation case and lift multiplicity in (11)
is correct.

## 8. Totient, omega, and explicit CRT-MCSS asymptotics

The Rosser--Schoenfeld primary paper,
[“Approximate Formulas for Some Functions of Prime
Numbers”](https://projecteuclid.org/journals/illinois-journal-of-mathematics/volume-6/issue-1/Approximate-formulas-for-some-functions-of-prime-numbers/10.1215/ijm/1255631807.full),
gives an explicit upper estimate for \(r/\varphi(r)\) of order
\(\log\log r\). It implies uniformly

\[
\varphi(r)\gg r/\log\log r,
\]

and hence \(\varphi(r)=r^{1-o(1)}\) in the logarithmic-exponent sense used in
the packet.

If \(j=\omega(r)\), the \(i\)-th prime is at least \(i+1\), so

\[
r\ge\prod_{i=1}^j p_i\ge(j+1)!.
\]

Stirling's elementary lower bound then gives

\[
j=O\!\left(\frac{\log r}{\log\log r}\right),
\qquad
2^{\omega(r)}=r^{o(1)}.
\]

These estimates are uniform. They do not assume smoothness or an average
factorization pattern. Equations (14) and (15) follow.

More explicitly, under CRT the map \(\psi_K\) acts coordinatewise, so

\[
\psi_K(U(K))
\cong
\prod_{\ell^a\parallel K}\psi_{\ell^a}(U(\ell^a)).
\]

A partial CRT sum supported on one block is injectively determined by its
coordinates in that block. Thus, when every local image choice is
materialized, the two half-list cardinalities have product equal to the
global image size. One list has at least its square root,
\(K^{1/4-o(1)}\).

I also checked the cited author preprint of Hittmeir,
[“Integer Factorization as Subset-Sum
Problem”](https://arxiv.org/abs/2205.10074). It supports the stated provenance
scope: CRT combines local modular-hyperbola sum choices; Section 5 gives the
MCSS formulation; the first relevant procedure is rigorous and
deterministic; and the two-list time-space procedure explicitly relies on a
heuristic asymptotic assumption and uses non-negligible space. F214 does not
attribute its own fiber lower bound to that source.

**Attack result: PASS.** This remains only an explicit half-list cardinality
bound. It is not a lower bound for an implicit MCSS solver.

## 9. Continued-fraction scope

At the full modulus, Section 1 has already proved \(XY=N=2K+1\). Therefore

\[
XY-2K=1
\]

and the displayed determinant is one. Conversely, every positive solution
of this identity has \(X\mid N\) and \(Y=N/X\). The balanced box selects the
nontrivial balanced divisor pair. The quotient

\[
\frac{XY-1}{K}=2
\]

is fixed and public on every such completion.

**Attack result: PASS at the declared scope.** This proves equivalence of the
direct determinant completion and divisor selection. It does not exclude a
continued-fraction algorithm that obtains additional information elsewhere,
and the packet expressly leaves that possibility open.

## 10. Direct bivariate Coppersmith range

The affine substitution is exact:

\[
(B-a)(B+c)=B^2+E
\iff
Bc-Ba-ac-E=0.
\]

The invertible affine change to \(UV-N\) proves irreducibility over
\(\mathbb Q\). On the full balanced box, bounds for \(|a|\) and \(|c|\) can
be chosen with

\[
A=\Theta(\sqrt N),
\qquad
C=\Theta(\sqrt N).
\]

The scaled coefficient magnitudes are \(BC,BA,AC,E\). The first three are
\(\Theta(N)\), while \(E=O(\sqrt N)\). Thus

\[
W=\Theta(N),
\qquad
AC=\Theta(N)=\Theta(W).
\]

I checked the official manuscript of Coron, Kirichenko, and Tibouchi,
[“A Note on the Bivariate Coppersmith
Theorem”](https://orbilu.uni.lu/bitstream/10993/12392/1/copnote.pdf). Its
corrected corollary uses

\[
XY\le W^{2/(3\delta)}
\]

for an irreducible polynomial of maximum degree \(\delta\) in each variable.
The underlying Coppersmith theorem has the stated strict epsilon-and-constant
version. Here \(\delta=1\), and \(AC=\Theta(W)\) is larger than
\(W^{2/3}\) by \(\Theta(N^{1/3})\). F214 is therefore outside both versions
of the sufficient range.

The Coppersmith primary paper is
[“Small Solutions to Polynomial Equations, and Low Exponent RSA
Vulnerabilities”](https://doi.org/10.1007/s001459900030). The separate Aono,
Agrawal, Satoh, and Watanabe source,
[“On the Optimality of Lattices for the Coppersmith
Technique”](https://eprint.iacr.org/2012/108.pdf), studies defined standard
lattice constructions and selected small-inverse equations. The provenance
correctly refuses to inflate that source into a universal lattice lower
bound for polynomial (18).

**Attack result: PASS.** This is nonapplicability of a sufficient theorem,
not impossibility of another lattice construction.

## 11. Fourier support

For odd \(K\), the step two is invertible modulo \(K\). The progression has
distinct elements when \(1\le L<K\). Its Fourier coefficient is

\[
e_K(ra)\sum_{j=0}^{L-1}e_K(2rj).
\]

For \(r\ne0\), the geometric-series denominator is nonzero. The numerator
vanishes exactly when \(K\mid rL\). There are \(\gcd(K,L)\) solutions to
that congruence, one of which is \(r=0\). Hence exactly
\(\gcd(K,L)-1\) coefficients vanish, and the support has size

\[
K-\gcd(K,L)+1\ge K-L+1.
\]

For the actual balanced odd intervals, \(L=\Theta(\sqrt N)\), while
\(K=\Theta(N)\). For \(N\ge15\), the progressions have no wraparound and
\(L<K\). Their support is therefore \(K-o(K)\).

**Attack result: PASS.** The conclusion concerns an implementation that
materializes and processes modes term by term. It does not rule out an
implicit transform, closed-form cancellation, or compressed Kloosterman
summation.

## 12. Literature-boundary checks

The cited primary source of Cilleruelo and Garaev,
[“Concentration Points on Two and Three Dimensional Modular Hyperbolas and
Applications”](https://arxiv.org/abs/1007.1526), studies upper bounds for
solutions of \(xy\equiv\lambda\pmod p\) in short boxes for a prime modulus
\(p\). It does not give an exact locator for the composite, fully factored
modulus in F214.

The Hittmeir, Coppersmith, Coron--Kirichenko--Tibouchi,
Aono--Agrawal--Satoh--Watanabe, Rosser--Schoenfeld, and
Cilleruelo--Garaev descriptions in `PROVENANCE.md` match the scopes of the
primary sources I checked. The Gao--Feng--Hu--Pan theorem interface also
matches its current primary revision.

The claim about binary subdivision is sound: an exact point-count oracle for
arbitrary subrectangles can isolate the unique full-box point with \(O(n)\)
binary splits. Knowing only that the full count is one does not identify its
coordinates.

**Attack result: PASS.** I found no citation inflation in Parts 4--11.

## 13. Supplemental finite attacks

Finite checks are not proof evidence for the theorem. I used them only to
search for counterexamples and indexing errors.

1. I exhaustively checked all 756 balanced products of distinct odd primes
   with the smaller prime below 200. Every full-\(K\) continuous-box
   congruence point was exactly \((p,q)\).
2. I enumerated every fiber of \(u\mapsto u+u^{-1}\) for every modulus
   \(1\le K\le500\). Every fiber satisfied (11).
3. I checked the Fourier support formula for every odd \(K\le299\) and every
   \(1\le L<K\). The exact support was always
   \(K-\gcd(K,L)+1\).
4. The same finite check exposed the recursive-domain counterexample
   \(247\mapsto123\) above. That counterexample illustrates the logical gap;
   the gap itself follows directly from the nonhereditary promise.

## Claim summary

| Frozen claim | Result | Reason |
|---|---:|---|
| Strict full-\(K\) collapse | PASS | Both product-window endpoints lie strictly inside \((-K,K)\). |
| Odd-step singleton threshold | PASS | Same-class odd representatives differ by a multiple of \(\operatorname{lcm}(2,m)\). |
| Recursive P183 consequence from the stated selector | **FAIL** | The child \(K\) is outside the balanced-semiprime promise in general. |
| P175/Gao--Feng--Hu--Pan terminal | PASS | Theorem number, unit premise, range, and bit bound match the current primary source. |
| Interval, unit, and paired-CRT counts | PASS | The finite inequalities are correct; the manifest overstates the unit scan as \(\Theta(\sqrt N)\). |
| Prime-power fibers and sum-image bound | PASS | All odd and 2-primary valuation and lift cases check. |
| Totient/omega and explicit CRT-MCSS asymptotics | PASS | Both estimates are uniform; the list conclusion is explicitly materialized only. |
| Direct continued-fraction completion | PASS | It is exactly divisor selection and makes no universal CF claim. |
| Direct bivariate Coppersmith range | PASS | \(AC=\Theta(W)\) lies outside the corrected \(W^{2/3}\) sufficient range. |
| Odd-modulus Fourier support | PASS | The exact geometric-series zero count is correct. |

The packet therefore cannot pass as frozen. The failed recursive implication
is a theorem-level defect, even though the main full-\(K\) collapse and every
named explicit-method boundary survive.
