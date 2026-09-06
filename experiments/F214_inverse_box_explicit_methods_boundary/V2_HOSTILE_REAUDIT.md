# F214 V2 hostile re-audit

## Verdict

**PASS.** Every frozen V2 claim survives hostile reconstruction at its stated
scope.

V2 repairs the fatal V1 recursion error. The size bounds for
\(K=(N-1)/2\) and \(E=N-\lfloor\sqrt N\rfloor^2\) are now local facts only.
The P183 recurrence is conditional on a separately granted correct recursive
factoring dispatch on all positive integer inputs, with the stated call bounds
at every node. The balanced-semiprime selector supplies only local work after
that dispatch has factored \(K\). It supplies neither correctness nor recursive
closure.

V2 also repairs the V1 manifest summary. Each interval scan has
\(\Theta(\sqrt N)\) candidates. The unit scan has exactly \(\varphi(K)\)
candidates. The packet proves only

\[
\varphi(K)\geq\sqrt{K/2}=\frac12\sqrt{N-1}.
\]

This PASS is not a numerical-QP inverse-box algorithm, an all-input factoring
algorithm, or a lower bound against implicit or new methods. It validates only
the frozen conditional theorem and the named explicit-representation
boundaries.

## Frozen-input integrity

I read `AGENTS.md` first. I then read `V2_MANIFEST.md` and computed the four
frozen V2 content hashes before reading any mathematical content in those
files. All four hashes match. I also authenticated the preserved V1 hostile
audit before reading it.

| File | Expected SHA-256 | Observed SHA-256 | Result |
|---|---|---|---:|
| `V2_STATEMENT.md` | `3aa3260154c8f0f7848b5fd5f8f427de41be07c986c044ad3141e32bc1928e97` | `3aa3260154c8f0f7848b5fd5f8f427de41be07c986c044ad3141e32bc1928e97` | PASS |
| `V2_PROOF.md` | `a7209b215d5d5b5d3c72e73a577a50a541b413dc3ed3e31a4772235dbe5d97b3` | `a7209b215d5d5b5d3c72e73a577a50a541b413dc3ed3e31a4772235dbe5d97b3` | PASS |
| `V2_SELF_AUDIT.md` | `23dbfe04020c8c28a36ebfa90837855e4ac8223012ca8673f7961790d4c0e4e3` | `23dbfe04020c8c28a36ebfa90837855e4ac8223012ca8673f7961790d4c0e4e3` | PASS |
| `V2_PROVENANCE.md` | `9f5bbe761c03b33c873230bde82741d6ef465264996b631dff037deb0aa07e74` | `9f5bbe761c03b33c873230bde82741d6ef465264996b631dff037deb0aa07e74` | PASS |

The manifest is intentionally not self-hashed. Its observed SHA-256 is
`eee12bd685e2f3618292983d5e65a81e620f75ac1cdba9abd3724e5598f0fe70`.

The preserved `HOSTILE_AUDIT.md` has expected and observed SHA-256
`fee67cd69879e271b23626b5f636ee172765799e65c9fb1612b93d1814b6fc2b`.
It is unchanged.

## 1. Strict full-\(K\) collapse

Take any integer point in the continuous box. Positivity and the four strict
box inequalities give

\[
\frac{N}{\sqrt2}<XY<\sqrt2N.
\]

For \(D=XY-N\), this is

\[
-\left(1-\frac1{\sqrt2}\right)N
<D<
(\sqrt2-1)N.
\]

The positive endpoint is below \(K=(N-1)/2\) when

\[
\left(\frac32-\sqrt2\right)N>\frac12,
\]

which holds for integer \(N\geq7\). The negative endpoint has magnitude below
\(K\) when

\[
\left(\frac1{\sqrt2}-\frac12\right)N>\frac12,
\]

which holds for integer \(N\geq3\). A balanced product of distinct odd primes
has \(N\geq15\). Thus both comparisons have strict slack. There is no open-end
or rounding exception.

The congruence gives \(K\mid D\). Since \(-K<D<K\), one gets \(D=0\), hence
\(XY=N\). The positive divisors of \(pq\) are \(1,p,q,N\), and the ordering
\(X<\sqrt N<Y\) forces \((X,Y)=(p,q)\).

Also

\[
\gcd(N,K)=\gcd\left(N,\frac{N-1}{2}\right)=1.
\]

If \(XY\equiv N\pmod K\), any common divisor of \(X\) and \(K\) would divide
\(N\), so \(X\in U(K)\). The congruence and inverse formulations therefore
have the same points. Oddness and endpoint liveness are not used in this
collapse.

**Attack result: PASS.** The quantifier in (2) covers every integer point in
the full continuous box, not only odd points or endpoint-live branches.

## 2. Singleton threshold and endpoint predicate

If two odd integers are congruent modulo \(m\), their difference is divisible
by both \(2\) and \(m\), hence by
\(s_m=\operatorname{lcm}(2,m)\). This remains true when \(m\) is even. A
nonzero difference has magnitude at least \(s_m\).

Under the two strict diameter inequalities, each nonempty representative set
therefore has one element. If the two sets are \(\{X\}\) and \(\{Y\}\), the
endpoint predicate becomes

\[
XY\leq N\leq XY.
\]

Thus it is exactly \(XY=N\), and the balanced interval ordering gives the
nontrivial factor pair. The theorem does not claim that one can find a live
branch efficiently before this threshold.

**Attack result: PASS.** The strict threshold, odd-step period, even-modulus
case, and all nonempty-branch quantifiers are correct.

## 3. Local child sizes and the repaired recursion scope

The local size calculations are correct. Since \(N<2^n\),

\[
K=(N-1)/2<2^{n-1},
\]

so \(K\) has at most \(n-1\) bits. With
\(B=\lfloor\sqrt N\rfloor\),

\[
0<E=N-B^2<(B+1)^2-B^2=2B+1<2\sqrt N+1,
\]

so \(E\) has \(n/2+O(1)\) bits.

These inequalities do not transfer the balanced-semiprime promise. The V1
counterexample remains decisive:

\[
N=247=13\cdot19,
\qquad K=123=3\cdot41.
\]

The parent is balanced, while the child is not. V2 expressly states this and
does not invoke the balanced selector on \(K\).

The recurrence now starts from a separate premise. A correct recursive
factoring dispatch is granted on every positive integer. At every node it has
at most one \((r-1)\)-bit child, at most \(Q(r)\) children of at most
\(r/2+C\) bits, and at most \(Q(r)\) other bit operations. Maximizing over all
inputs of at most \(r\) bits gives

\[
T(r)\leq T(r-1)+Q(r)T(r/2+C)+Q(r).
\]

This is P183 with fixed ratio \(1/2\); the fixed additive constant affects
only the finite base range. P183 then gives numerical-QP time. The premise is
strong: it independently grants all-input correctness, termination, and call
tree closure. The packet does not derive any of them from local size facts.

At a balanced node, once that all-input dispatch has returned the complete
factorization of \(K\), a numerical-QP full-\(K\) selector is additional local
work. It can be absorbed into \(Q(r)\). This does not make the selector
recursively valid on \(K\), and V2 does not say that it does.

**Attack result: PASS.** The fatal V1 implication is absent. Part 3 is a
conditional accounting theorem, not a construction of either the selector or
the all-input dispatch.

## 4. Arithmetic-progression terminal

The current Gao--Feng--Hu--Pan Theorem 3.1 takes natural \(N,s\), a modulus
\(m\in(\mathbb Z/N\mathbb Z)^*\), and \(s,m<N\). With its parameter set to
\(r=1\), it finds the selected prime divisor in

\[
O\!\left(
\left\lceil\frac{N^{1/4}}m\right\rceil
\log^{7+3\epsilon}N
\right)
\]

deterministic bit operations for fixed \(\epsilon>0\).

Reduce each listed residue to its canonical class. A zero class can be
discarded: it cannot equal \(p\bmod m\) because \(\gcd(m,N)=1\). For the true
nonzero class, all theorem premises hold. Condition (7) makes the ceiling a
numerical-QP factor. A numerical-QP number of calls and exact-division checks
is still numerical QP.

An endpoint-live branch need not contain the true factor residue. V2 invokes
the terminal only after a numerical-QP list is guaranteed to contain that
residue, or after singleton equality has already factored \(N\).

**Attack result: PASS.** The theorem number, unit condition, range, list
quantifier, and terminal scope are correct. Discarding a zero noncandidate is
only input normalization and changes no claim or complexity bound.

## 5. Exact direct-scan cardinalities

The two real interval lengths are

\[
\left(1-2^{-1/2}\right)\sqrt N,
\qquad
(\sqrt2-1)\sqrt N.
\]

Any real interval of length \(H\) contains \(H/2+O(1)\) odd integers. Hence

\[
|P|=\frac{1-2^{-1/2}}2\sqrt N+O(1),
\qquad
|Q|=\frac{\sqrt2-1}2\sqrt N+O(1).
\]

Each interval scan therefore has \(\Theta(\sqrt N)\) candidates.

The full inverse torsor is indexed by \(U(K)\), so its literal unit scan has
exactly \(\varphi(K)\) candidates. For an odd prime power \(\ell^a\),

\[
\frac{\varphi(\ell^a)^2}{\ell^a}
=\ell^{a-2}(\ell-1)^2\geq1.
\]

For \(2^a\), the ratio is \(1/2\) at \(a=1\) and at least one for
\(a\geq2\). Multiplication over prime powers yields

\[
\varphi(r)^2\geq r/2
\]

for every positive integer \(r\). Substitution of \(r=K\) proves (9).

**Attack result: PASS.** V2 does not claim
\(\varphi(K)=\Theta(\sqrt N)\). It gives the exact count and only the stated
lower bound. All scan statements concern literal enumeration, not implicit
selection.

## 6. Explicit paired CRT

For the prime-power factorization \(K=\prod_i k_i\), CRT gives

\[
U(K)\cong\prod_iU(k_i).
\]

If every local unit coordinate is assigned to one of two blocks and every
partial assignment is materialized, the two list sizes satisfy

\[
A=\prod_{i\in I}\varphi(k_i),
\qquad
B=\prod_{i\notin I}\varphi(k_i),
\qquad
AB=\varphi(K).
\]

This includes an empty block. Therefore

\[
\max(A,B)\geq\sqrt{\varphi(K)}
\geq(K/2)^{1/4}=N^{1/4+o(1)}.
\]

**Attack result: PASS.** The lower bound is for explicitly materialized
two-block assignment lists only. It makes no claim about compressed,
adaptive, or implicit CRT methods.

## 7. Sum fibers, image size, and explicit CRT-MCSS

A fiber of \(u\mapsto u+u^{-1}\) is the root set of

\[
z^2-sz+1\equiv0\pmod K.
\]

Every root is automatically a unit because the constant term is one.

For an odd prime power \(\ell^a\), the bijection \(t=2z-s\) changes the
congruence to

\[
t^2\equiv s^2-4\pmod{\ell^a}.
\]

If the right side is zero modulo \(\ell^a\), there are exactly
\(\ell^{\lfloor a/2\rfloor}\) roots. Otherwise a solution requires valuation
\(2h<a\). After writing \(t=\ell^h w\), the unit square congruence modulo
\(\ell^{a-2h}\) has at most two roots. Each has \(\ell^h\) relevant lifts
modulo \(\ell^a\). Thus the local count is at most

\[
2\ell^h\leq2\sqrt{\ell^a}.
\]

An odd valuation gives no root.

For \(2^a\), a nonempty image residue is even. Write \(s=2h\). Translation,
without division by two, gives

\[
(z-h)^2\equiv h^2-1\pmod{2^a}.
\]

The zero case has \(2^{\lfloor a/2\rfloor}\) roots. In a nonzero solvable
case the valuation is \(2h_0<a\). The remaining odd unit square congruence
has at most four roots, and each has \(2^{h_0}\) relevant lifts. Hence the
2-primary count is at most

\[
4\,2^{h_0}\leq4\sqrt{2^a}.
\]

CRT multiplies these local counts. If \(K_{\rm odd}\) has \(r\) distinct
prime factors, the global result is

\[
|\psi_K^{-1}(s)|
\leq4\,2^r\sqrt K
=4\,2^{\omega(K_{\rm odd})}\sqrt K.
\]

The factor four is deliberately loose when \(K\) is odd. Replacing
\(\omega(K_{\rm odd})\) by \(\omega(K)\) only weakens the bound. Since the
fibers partition all \(\varphi(K)\) units,

\[
|\psi_K(U(K))|
\geq
\frac{\varphi(K)}{4\,2^{\omega(K)}\sqrt K}.
\]

The standard uniform estimate
\(\varphi(K)\gg K/\log\log K\) gives
\(\varphi(K)=K^{1-o(1)}\). If \(j=\omega(K)\), then

\[
K\geq2\cdot3\cdots(j+1)=(j+1)!,
\]

so \(j=O(\log K/\log\log K)\) and
\(2^{\omega(K)}=K^{o(1)}\). These facts turn the finite image bound into
\(K^{1/2-o(1)}\). They use no smoothness or average-case assumption.

The sum map is coordinatewise under CRT. Its global image is exactly the
Cartesian product of the local images. If all local image choices are split
between two explicit half lists, the product of the list sizes is the global
image size. One list therefore has at least \(K^{1/4-o(1)}\) elements.

**Attack result: PASS.** All valuation cases, lift multiplicities, global
quantifiers, finite constants, and asymptotic deductions are correct. The
MCSS conclusion covers explicit half-list materialization only.

## 8. Determinant-one and continued-fraction scope

The full-\(K\) collapse gives \(XY=N=2K+1\), so

\[
XY-2K=1.
\]

Conversely, any positive solution of this identity satisfies \(XY=N\), hence
comes from a divisor \(X\mid N\) and \(Y=N/X\). The balanced box selects the
nontrivial balanced divisor. The quotient \((XY-1)/K\) is always the public
integer two.

This proves equivalence of the displayed determinant completion and divisor
selection. It does not give a separate public rational approximation with a
hidden numerator or denominator in the range of the usual continued-fraction
criterion.

**Attack result: PASS.** V2 does not claim that every possible
continued-fraction algorithm must use this direct completion or cannot use
new information.

## 9. Direct bivariate Coppersmith range

With \(a=B-X\) and \(c=Y-B\), the factor equation is exactly

\[
f(a,c)=Bc-Ba-ac-E=0.
\]

The invertible affine change \((a,c)\mapsto(U,V)=(B-a,B+c)\) sends this to
\(UV-N\), which is irreducible over \(\mathbb Q\). On the complete balanced
box, valid bounds satisfy

\[
A=\Theta(\sqrt N),
\qquad C=\Theta(\sqrt N),
\qquad AC=\Theta(N).
\]

The coefficients of \(f(Ax,Cy)\) have magnitudes \(BC,BA,AC,E\). The first
three are \(\Theta(N)\), while \(E=O(\sqrt N)\). Therefore

\[
W=\|f(Ax,Cy)\|_\infty=\Theta(N),
\qquad AC=\Theta(W).
\]

The corrected direct bivariate theorem uses maximum separate degree
\(\delta\), this scaled coefficient height, and the sufficient product range
\(AC\leq W^{2/(3\delta)}\) in its corollary. Its underlying theorem has the
stated strict epsilon and constant slack. Here \(\delta=1\). The full box has
\(AC=\Theta(W)\), so it exceeds the \(W^{2/3}\) range by
\(\Theta(N^{1/3})\).

**Attack result: PASS.** The scaled-height convention and theorem interface
match. V2 concludes only that this published sufficient theorem cannot be
applied directly. It states no converse and no lattice lower bound.

## 10. Odd-\(K\) Fourier support

Assume \(K\) is odd and \(1\leq L<K\). For

\[
\mathcal A=\{a+2j:0\leq j<L\},
\]

the Fourier coefficient at \(r\bmod K\) is

\[
e_K(ra)\sum_{j=0}^{L-1}e_K(2rj).
\]

At \(r=0\) it is \(L\neq0\). For \(r\neq0\), oddness of \(K\) makes the
geometric-series denominator nonzero. The numerator vanishes exactly when

\[
K\mid2rL
\iff K\mid rL.
\]

There are \(\gcd(K,L)\) solutions for \(r\), including zero. Thus exactly
\(\gcd(K,L)-1\) nonzero-frequency coefficients vanish, and the support has
exact size

\[
K-\gcd(K,L)+1\geq K-L+1.
\]

For the actual balanced odd intervals, \(L=\Theta(\sqrt N)<K\) and
\(K=\Theta(N)\). Each support therefore has \(K-o(K)\) modes.

**Attack result: PASS.** Every hypothesis is explicit: \(K\) is odd,
\(1\leq L<K\), and the conclusion concerns termwise materialization. It does
not cover implicit transforms, cancellation formulas, or compressed harmonic
evaluation.

## 11. Literature and universal-scope attacks

The primary-source interfaces used by the packet have the claimed narrow
scope:

1. Gao--Feng--Hu--Pan supplies the selected arithmetic-progression terminal,
   not construction of the residue list.
2. Hittmeir supplies the CRT sum-choice and MCSS formulation. The frozen list
   lower bounds are proved inside F214 and are not attributed to that paper.
3. Coppersmith and Coron--Kirichenko--Tibouchi supply a sufficient direct
   bivariate range, not a converse.
4. Aono--Agrawal--Satoh--Watanabe is used only to prevent a universal reading
   of construction-specific lattice optimality.
5. Cilleruelo--Garaev gives concentration bounds over prime moduli, not an
   exact locator for the composite modulus \(K\).

The exact subrectangle-count statement is also sound. Since the full box has
one point, an exact count oracle for arbitrary subrectangles can retain the
nonempty half at each binary split and isolate both coordinates in \(O(n)\)
calls. The already known total count of one contains no location data.

**Attack result: PASS.** No statement becomes a lower bound against a
compressed exact counter, implicit CRT or MCSS, non-termwise Fourier method,
nonstandard lattice, continued-fraction method with new data, or new
integer-specific selector.

## 12. Supplemental finite attacks

These searches were used only to look for counterexamples and indexing
errors. They are not proof evidence.

1. I checked all 117 balanced products of distinct odd primes with both
   primes at most 100. Every continuous full-\(K\) box had exactly the point
   \((p,q)\).
2. Across the same inputs, all 1,705 endpoint-live branches whose step
   exceeded both diameters were singleton branches with product \(N\).
3. I enumerated all fibers of \(u\mapsto u+u^{-1}\) for every
   \(1\leq K\leq1000\). Every fiber met (11). The finite totient bound also
   held for every modulus.
4. I checked all 62,750 pairs with odd \(3\leq K\leq501\) and
   \(1\leq L<K\). Every support count was
   \(K-\gcd(K,L)+1\).

## Claim summary

| Frozen V2 claim | Result | Hostile conclusion |
|---|---:|---|
| Strict full-\(K\) collapse | PASS | The full strict product window lies inside \((-K,K)\). |
| Singleton threshold | PASS | Same-class odd representatives differ by a multiple of \(\operatorname{lcm}(2,m)\). |
| Local child sizes | PASS | They are local only and do not imply promise inheritance. |
| Conditional P183 accounting | PASS | All-input correctness and closure are independent explicit premises at every node. |
| Arithmetic-progression terminal | PASS | A guaranteed true unit residue meets the cited theorem after canonical normalization. |
| Interval and unit scans | PASS | The intervals are \(\Theta(\sqrt N)\); the unit scan is exactly \(\varphi(K)\) with only the stated lower bound. |
| Explicit paired CRT | PASS | Materialized list sizes multiply to \(\varphi(K)\). |
| Sum fibers and CRT-MCSS | PASS | Prime-power counts, lifts, CRT multiplication, and explicit half-list scope all hold. |
| Continued-fraction completion | PASS | The direct determinant identity is exactly divisor selection. |
| Direct bivariate Coppersmith | PASS | \(AC=\Theta(W)\) lies outside the proved \(W^{2/3}\) sufficient range. |
| Odd-\(K\) Fourier support | PASS | The exact support is \(K-\gcd(K,L)+1\); only termwise materialization is covered. |
| Universal lower-bound reading | PASS | Every negative conclusion remains restricted to its named explicit model or theorem range. |

No frozen input or durable ledger was edited. This re-audit report does not
hash itself; its observed SHA-256 must be recorded after the file is frozen.
