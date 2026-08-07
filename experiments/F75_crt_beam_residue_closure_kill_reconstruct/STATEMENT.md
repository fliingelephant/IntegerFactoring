# Proof-blind reconstruction statement: CRT scores and canonical-residue closure

Work only from this statement. Do not read any F75 candidate, audit, durable
ledger, or proof. Do not run computation. Reconstruct every claim below from
first principles and return a self-contained PASS proof or the first exact
failure.

## 1. CRT state

Let \(N\ge3\), \(1<g<N\), and \(\gcd(g,N)=1\). Define \(\rho_g\) as the
least positive solution of

\[
N\rho_g\equiv-1\pmod g,
\]

and put

\[
w_g=\frac{1+N\rho_g}{g}.
\]

Prove that \(1\le w_g<N\), that \(w_g\) is the canonical inverse of \(g\),
and that \(\rho_g\) is its canonical inverse quotient. If

\[
g\mid P=1+KN,
\]

prove \(\rho_g=K\bmod g\) in the least-positive range.

If \(b\) is coprime to \(gN\), define

\[
t=(\rho_b-\rho_g)g^{-1}\bmod b,
\qquad 0\le t<b.
\]

Prove

\[
\rho_{gb}=\rho_g+gt,
\qquad
w_{gb}=\frac{w_g+Nt}{b}
=[w_gw_b]_N.
\]

Explain why this displayed update does not add a repeated block already in
\(g\), does not accept an overlapping macroblock, and does not by itself
certify retained-product provenance.

Also prove

\[
\gcd(g-w_g,N)=\gcd(g^2-1,N),
\]

and explain why both sign screens remain necessary for a non-global square
root of one.

## 2. Scalar score orders are not extension-monotone

Verify all tables below at \(N=55\). Every common extension must be legal and
coprime.

### Canonical-inverse score

For prefixes \(g=8,7\), extended by \(b=3\), verify

\[
\begin{array}{c|cc|cc}
g&\rho_g&w_g&\rho_{3g}&w_{3g}\\ \hline
8&1&7&17&39\\
7&1&8&8&21.
\end{array}
\]

### Quotient score

For prefixes \(g=13,23\), extended by \(b=2\), verify

\[
\begin{array}{c|cc|cc}
g&\rho_g&w_g&\rho_{2g}&w_{2g}\\ \hline
13&4&17&17&36\\
23&5&12&5&6.
\end{array}
\]

### Inverse-distance score

For prefixes \(g=7,17\), extended by \(b=2\), verify

\[
\begin{array}{c|cc|c}
g&w_g&|g-w_g|&|2g-w_{2g}|\\ \hline
7&8&1&10\\
17&13&4&0.
\end{array}
\]

### Refinement gain

With current blocks \(\{13,3,28\}\), verify

\[
\gcd(17,28)=1,
\qquad
\gcd(24,28)=4,
\]

where \(17\) is the inverse of \(13\) and \(24\) is the inverse of \(39\).
With blocks \(\{17,3,26\}\), verify

\[
\gcd(13,26)=13,
\qquad
\gcd(41,26)=1,
\]

where \(13\) is the inverse of \(17\) and \(41\) is the inverse of \(51\).

Conclude only that the current values of the named scalar scores are not
extension-monotone dominance certificates. Do not infer failure of every
polynomial-width beam, a large Pareto frontier, or even a failed run of a
factorer that applies all mandatory screens before extension.

## 3. Canonical-residue closure

Let current refined blocks generate

\[
H=\langle q_1,\ldots,q_m\rangle
\subseteq(\mathbb Z/N\mathbb Z)^\times.
\]

For a public exponent vector \(e\), define

\[
c=\left[\prod_jq_j^{e_j}\right]_N,
\qquad
w=[c^{-1}]_N,
\qquad
cw=1+kN.
\]

Prove that \(c,w\in H\), so this operation does not enlarge \(H\). Explain
why it is nevertheless a genuine source change when the raw positive product
is at least \(N\), uses negative exponents, or lies outside occurrence
capacities. Explain how gcd-free refinement of the new canonical integers can
expose individual block residues outside \(H\), even though their products
remain in \(H\).

Prove polynomial bit cost for one vector and for exhaustive fixed support over
a polynomial exponent menu. State why exhaustive dense vectors remain
exponential and why a random or capped search needs a separate success law.

## 4. Exact post-refinement witness

Take

\[
N=4033=37\cdot109,
\qquad
H_1=\langle2,5\rangle.
\]

Verify

\[
5\cdot2^{13}=40960=10N+630,
\]

\[
630\cdot3220=1+503N,
\]

and

\[
\gcd(630-1,N)=\gcd(630-3220,N)=37.
\]

Thus canonical reduction makes the previously oversized raw word a legal
factor-bearing representative.

Now let \(n=\lceil\log_2N\rceil=12\). Verify that exponents \(2,8\) belong
to the literal menu \(\{1,\ldots,n\}\), and verify

\[
5^2 2^8=6400=N+2367,
\]

\[
2367\cdot443=1+260N,
\]

and

\[
\gcd(2367+1,N)=\gcd(2367-443,N)=37.
\]

Conclude that an exhaustive support-two canonical-residue scan over this
menu factors this fixed post-refinement state.

## Required scope

The CRT update is exact bookkeeping, not a new source. The score examples
prove scalar non-extension-monotonicity only. Canonical-residue closure is a
real operation change and closes the finite-positive-box caveat on the fixed
\(N=4033\) state. No proof shows how every input reaches such a refined state,
that every useful subgroup has a polynomial-menu separator, or that a random
sample hits one with inverse-polynomial probability. No factoring algorithm
is claimed.
