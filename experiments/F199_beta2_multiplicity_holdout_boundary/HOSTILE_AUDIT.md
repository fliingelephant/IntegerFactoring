# Hostile audit of F199

## Verdict

**PASS.** I found no mathematical error, quantifier slip, hidden factoring
oracle, complexity inflation, or overclaim in the frozen F199 packet. The
results are narrow representation boundaries. They do not claim an
adaptive or nonlocal selector lower bound.

One editorial defect is non-mathematical: equation (19) in `STATEMENT.md`
prints `pmod` instead of `\pmod`. The intended congruence is unambiguous and
is written and proved correctly in the surrounding text.

## 1. Frozen hashes

I computed the hashes before reading the frozen files. They are

- `STATEMENT.md`:
  `04c309ece29db251826247c6cfee7481b9e0b1a4e17c2ef5839ee06ac73be38c`;
- `PROOF.md`:
  `5324fe02ed675f4aedb5925559fa4a7cbc8d42295bbe41d33a775810d479c8f9`;
- `SELF_AUDIT.md`:
  `990e2428d767a1aa6d6714a6a10f19fe975729864fba0a52c439c8719222926b`;
- observed `MANIFEST.md`:
  `50cee28ef6fdf21ca2fb0d4f82dc5fd7fd18ffe558dfc0dc90ee4d0243dbf491`.

The three frozen-input hashes agree exactly with the manifest.

## 2. Imported P175 interface

The packet retains the exact promoted promise

\[
N=pq,\qquad p<q<2p,
\]

for distinct odd primes. It uses

\[
t=\left\lfloor\frac{\log_2N}{4}\right\rfloor-L(n)\ge2
\]

for one fixed public (L(n)=(\log n)^{O(1)}). It does not replace this by a
smaller precision or a broader input class.

At the true reciprocal (u=p^{-1}\bmod 2^t), inversion gives
(p\bmod2^t). P175's direct progression terminal has cost

\[
O\!\left(\left\lceil\frac{N^{1/4}}{2^t}\right\rceil
\operatorname{poly}(n)\right)
=2^{L(n)}\operatorname{poly}(n),
\]

up to the imported logarithmic exponent. Equivalently, its Coppersmith
route enumerates only the (2^{L(n)}) missing extensions. Both are
numerical QP. F199 uses this only in the explicit-cloud terminal.

The definition

\[
z=N^{-1}(A-1)\pmod{2^t}
\]

is correctly treated as multiplication by the inverse of odd (N). No
integer divisibility (N\mid A-1) is asserted.

## 3. Unit torsor, quotient ring, and Jacobian

For every (u\in R^\times), where (R=\mathbb Z/2^t\mathbb Z), the
definitions

\[
P=u^{-1},\qquad Q=Nu,\qquad H=z+u
\]

give

\[
Pu=1,\quad Q=Nu,\quad PQ=N,
\quad NH=Nz+Nu=A-1+Q.
\]

Conversely, (PU=1) forces (U) to be a unit and uniquely forces
(P=U^{-1}); the other equations uniquely force (Q=NU) and (H=z+U).
The two explicit substitutions therefore prove

\[
R[U,P,Q,H]/(PU-1,Q-NU,H-z-U)\cong R[U,U^{-1}].
\]

For the three displayed generators, the minor in columns ((P,Q,H)) is

\[
\operatorname{diag}(U,1,1),
\]

whose determinant is the unit (U). The explicit isomorphism to
\(\mathbb G_{m,R}\), not merely a field-valued Jacobian heuristic,
justifies relative smoothness over the nonreduced base ring (R). There
are exactly (2^{t-1}) unit residues. The target is one smooth section;
the theorem does not claim that arbitrary (N)-dependent coefficients
cannot orient those sections.

## 4. Public recurrence and smoothness at the hidden edge

The exact identity

\[
(i+1)(A_{i+1}-A_i)=-NA_i
\]

and (A_i=1+Nz_i) in (R) give

\[
(i+1)(z_{i+1}-z_i)+1+Nz_i=0.
\]

Only the odd unit (N) is cancelled. The proof never divides by (i+1),
so even indices cause no omitted zero-divisor case.

For each supplied index (i\le B), the imported P173 routine is invoked
at modulus parameter (T=n), upper index (N-1<2^n), and lower index
(i\). Thus pointwise computation is polynomial in (n); no claim is made
that the exponentially long transcript is materialized.

For

\[
\mathcal R_N=(K+1)(Y-X)+1+NX,
\]

the (X,Y) Hasse derivatives are (N-K-1) and (K+1). Their sum is odd
(N), so at least one is a unit in (R) at every edge. At (K=p-1), the
(Y)-derivative is (p), explicitly an odd unit. The mixed (KX) and
(KY) Hasse coefficients are constant public units and do not create a
hidden-edge multiplicity.

## 5. Location of the one-spike word

P171's two exact residue regimes give

\[
H_i-z_i\equiv
\begin{cases}
0,&i<p,\\
p^{-1},&i\ge p,
\end{cases}
\pmod{2^t}.
\]

Taking adjacent differences produces one spike at (i=p-1). This uses the
integral quotient labels (H_i). The public labels (z_i) instead obey
the smooth recurrence at every edge. The packet never labels (H_i) as
public or computable. A public QP index list containing (p-1) would
already factor through \(\gcd(i+1,N)\), and no such list is assumed.

## 6. Reed--Muller support and column-span claim

The induction is valid. In the decomposition

\[
F=G+x_mJ,
\]

if (J=0), the two cube halves duplicate (G). If (J\ne0), every point
where (J=1) contributes exactly one nonzero evaluation among (G) and
(G+J). Induction gives in both cases

\[
\operatorname{wt}(F)\ge2^{m-d}.
\]

The degree-(m) delta function proves sharpness at singleton support. If
evaluation on the complement of (S) had a nonzero kernel, its support
would be contained in (S), contradicting the bound when
(|S|<2^{m-d}). Since full-cube evaluation is injective, the restricted
feature matrix retains full row rank; equivalently, deleting those columns
does not shrink their span.

Here (m=t-1=\Theta(n)), while both (d) and the logarithm of a QP
holdout size are polylogarithmic. Hence the asserted strict inequality
holds after a finite prefix. The theorem is explicitly restricted to the
unique multilinear Boolean representative and affine changes of its input
bits.

## 7. Hasse neighborhoods and scalar multiplicity

For multilinear (F), substitution of (y=\mathbf1_T) into the Hasse
expansion gives

\[
F(x+\mathbf1_T)=\sum_{S\subseteq T}D_SF(x).
\]

Vanishing of all derivatives with (|S|<s) therefore implies vanishing on
the radius-((s-1)) Hamming ball. Conversely, the Boolean subset-zeta
system is triangular with unit diagonal, so its equations invert and give
the derivative conditions. This remains valid in characteristic two.

Because (t\ge2), one has (m\ge1). If every point except (u) has
order at least two, choose a neighbor (x) of (u). Its radius-one ball
contains (u), forcing (F(u)=0). Thus the missing-neighbor contradiction
is exact and degree-independent within the declared multilinear model.

The union of (C) such balls contains at most

\[
C\sum_{j<s}\binom mj\le Cs m^{s-1}.
\]

For QP (C) and polylogarithmic (s), this is QP and is much smaller than
(2^m-1). Hence these directly covered balls cannot cover all candidates
except one. No disjointness is assumed.

For distinct field points, Hasse multiplicity (s) is equivalent to
((X-x_i)^s\mid f). The factors are pairwise coprime, so multiplicity at
(M-1) points forces degree at least (s(M-1)). The stated injectivity and
field hypotheses are necessary and are present.

## 8. Explicit QP clouds

For every listed unit (u), inversion is polynomial time. At the true list
entry it returns (p\bmod2^t), so P175 applies at exactly its promoted
precision. A QP number of bounded QP calls remains QP, and exact division
verifies every accepted factor. A Las Vegas list generator retains
almost-sure termination and expected-QP cost under this deterministic,
bounded postprocessing.

The bounded-preimage extension explicitly requires a QP number of columns
and a publicly enumerable QP-size preimage for each. The argument does not
apply to an aggregate prefix cell with exponentially many members.

## 9. Paired lifts and balanced representatives

Let (M=2^{j+1}) and (a=2^j). Since (u_0,P_0) are odd,
(a(u_0+P_0)\equiv0\pmod M). Since (j\ge1), also
(a^2\equiv0\pmod M). Therefore

\[
(u_0+a)(P_0+a)\equiv1\pmod M,
\]

so (P_1=P_0+a\pmod M). Oddness of (N) similarly gives
(Q_1=Q_0+a\pmod M). Both branches satisfy the full public congruence
system, and toggling twice adds (M\), hence is the identity.

Because \(\sqrt N\) is nonintegral, each open interval of length (M)
with endpoints \(\sqrt N-M,\sqrt N\), or
\(\sqrt N,\sqrt N+M\), contains exactly one representative of every
residue class modulo (M). These representatives remain odd. If
(3M<\sqrt N), then

\[
\sqrt N+M<2(\sqrt N-M)<2\widetilde P_b,
\]

which proves all strict balance inequalities. For (M\le N^{1/4}), the
condition follows after the finite range (N^{1/4}\le3). The packet
correctly denies primality and exact multiplication for these surrogate
representatives.

## 10. Prefix cells and recursion

Over \(\mathbb F_2\), each factor (1+x_r+a_r) equals one exactly when
(x_r=a_r). Their product is the exact prefix-cell indicator, of degree
(\ell) and support (2^{m-\ell}). For polylogarithmic \(\ell), the
degree-at-most-\(\ell) feature space has dimension at most

\[
(\ell+1)m^\ell=2^{(\log n)^{O(1)}}.
\]

A supplied QP syndrome could therefore select a polylogarithmic block, and
(O(n/\ell)) sequential stages preserve QP time. This is one surviving
child per stage; no fixed-ratio contraction is needed. F199 supplies no
such syndrome.

## 11. Scope and nonclaims

The statements consistently exclude:

- nonlocal features of canonical integer representatives;
- Euclidean quotient or carry bits;
- QP-evaluable aggregate interval or prefix-cell statistics;
- adaptive one-child syndromes;
- nonlinear target-correlated embeddings;
- sparse high-degree circuits;
- noninjective scalar encodings; and
- other factoring algorithms.

The support and Hasse arguments concern only their named direct feature
models. Smoothness says only that the target is not a singular point of the
public congruence scheme. The paired-lift result says only that congruences,
size, and balance alone do not prune a branch. None is presented as a
factoring lower bound.

No experimental mathematical computation or durable-ledger edit is used.

## Strict result

**PASS.**
