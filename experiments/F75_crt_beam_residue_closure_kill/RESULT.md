# F75 CRT-beam and canonical-residue closure kill-first review

## Status

Corrected proof-only review after a passing audit requested a stricter scope
sentence. No research computation was used. All numerical examples below are
direct arithmetic certificates. This note is not a factoring theorem and the
corrected version requires a fresh audit.

## 1. Conclusions

1. The CRT update for
   \(\rho(g)=(-N^{-1})\bmod g\) is exact when the added modulus is coprime to
   the current product. For a legal P70 product, \(\rho(g)\) is exactly P70's
   feedback quotient. Thus the update is an efficient reparameterization, not
   a new source of factor information.
2. None of the three numerical beam scores has the optimal-substructure
   property needed for safe pruning. The refinement score is also
   nonmonotone. A polynomial beam width proves a polynomial running time, but
   it gives no success probability.
3. Canonical-residue closure is a genuine operation change. It searches
   modular words and then chooses their canonical integer representatives. It
   therefore removes P70--P71's positive-product and finite-occurrence-box
   restrictions.
4. On the post-refinement \(N=4033\) state of P78, this operation does more
   than expose the already displayed residue \(630\). A support-two word with
   exponents in the proposed small menu gives a factor immediately. This
   closes the finite-box caveat for that fixed state. It does not explain how
   to reach such a state or why a comparable short word exists for every
   composite.

## 2. Exact meaning of the CRT state

Let \(1<g<N\) and \(\gcd(g,N)=1\). Take \(\rho_g\) to be the least residue in
\(\{1,\ldots,g-1\}\) satisfying

\[
N\rho_g\equiv-1\pmod g.
\]

Then

\[
w_g=\frac{1+N\rho_g}{g}
\]

is an integer in \(\{1,\ldots,N-1\}\), and

\[
gw_g=1+\rho_gN.
\tag{1}
\]

Thus \(w_g\) is exactly the canonical inverse of \(g\), and \(\rho_g\) is
exactly the quotient of its canonical inverse relation.

If \(g\) is a legal divisor of a retained P70 relation product

\[
P=1+KN,
\]

then P70 gives \(k(g)=K\bmod g\) in the same least-positive range. Since
\(KN\equiv-1\pmod g\),

\[
\boxed{\rho_g=k(g).}
\tag{2}
\]

The proposed CRT state therefore does not enlarge P70's candidate set. It
only computes the same quotient without rebuilding the full relation product.

Now let \(b\) be coprime to \(gN\), and let \(\rho_b\) be defined in the same
way. If

\[
t=(\rho_b-\rho_g)g^{-1}\pmod b,
\qquad 0\le t<b,
\]

then

\[
\rho_{gb}=\rho_g+gt,
\qquad
w_{gb}=\frac{w_g+Nt}{b}.
\tag{3}
\]

This is the unique CRT lift in \([0,gb)\). Equivalently,

\[
w_{gb}=[w_gw_b]_N,
\tag{4}
\]

where the right side is the canonical nonzero residue modulo \(N\).

There is one necessary decoder correction. Since \(g\) is a unit,

\[
\gcd(g-w_g,N)=\gcd(g^2-1,N).
\]

A proper value gives a factor. But if \(g\) is a non-global square root of
one, this gcd is the unhelpful value \(N\), while
\(\gcd(g-1,N)\) and \(\gcd(g+1,N)\) are the two proper factors. Therefore the
beam must retain both sign screens; the difference screen does not replace
them.

The coprimality condition is essential. Formula (3) cannot add another copy
of a block already dividing \(g\), and it cannot add an overlapping macroblock.
Repeated powers can be offered as separate atomic choices, or handled by a
different prime-power lift, but the displayed CRT update does not itself cover
that case. Provenance and occurrence capacities also remain necessary. A CRT
triple \((g,\rho_g,w_g)\) does not certify that \(g\) is an authorized P70
product.

## 3. The proposed scores do not support exact beam pruning

All examples in this section use \(N=55\). Every displayed integer is a unit
modulo \(55\), every extension remains below \(55\), and each stated set of
blocks is pairwise coprime.

### 3.1 Minimum canonical inverse

For the two prefixes \(g=8,7\), followed by the same new block \(b=3\),

\[
\begin{array}{c|cc|cc}
g&\rho_g&w_g&\rho_{3g}&w_{3g}\\ \hline
8&1&7&17&39\\
7&1&8&8&21
\end{array}
\]

The first prefix wins because \(7<8\), but its extension loses because
\(39>21\).

### 3.2 Minimum quotient

For prefixes \(g=13,23\), followed by \(b=2\),

\[
\begin{array}{c|cc|cc}
g&\rho_g&w_g&\rho_{2g}&w_{2g}\\ \hline
13&4&17&17&36\\
23&5&12&5&6
\end{array}
\]

The quotient order reverses: \(4<5\), but \(17>5\).

### 3.3 Minimum distance from the inverse

For prefixes \(g=7,17\), followed by \(b=2\),

\[
\begin{array}{c|cc|c}
g&w_g&|g-w_g|&|2g-w_{2g}|\\ \hline
7&8&1&|14-4|=10\\
17&13&4&|34-34|=0
\end{array}
\]

The worse prefix becomes an exact self-inverse state. This example only
refutes score optimality; the competing state \(14\) also happens to expose a
factor of \(55\), so it is not claimed as a complete failure of that one beam
run.

### 3.4 Refinement gain can appear or disappear

With current blocks \(\{13,3,28\}\), the prefix \(g=13\) has canonical inverse
\(17\), so

\[
\gcd(17,28)=1.
\]

After adding block \(3\), \(g=39\) has canonical inverse \(24\), and

\[
\gcd(24,28)=4,
\]

which properly splits \(28=4\cdot7\).

The reverse behavior also occurs. With blocks \(\{17,3,26\}\), the prefix
\(g=17\) has inverse \(13\) and properly splits \(26=13\cdot2\). After adding
\(3\), \(g=51\) has inverse \(41\), and

\[
\gcd(41,26)=1.
\]

Therefore current overlap count and balance are progress tests, not lookahead
bounds. A zero-gain prefix can acquire gain, and existing gain can disappear
under the canonical modular multiplication in (4).

These reversals prove only that the current value of each named scalar score
is not an extension-monotone dominance certificate. They do not prove that a
polynomial-width beam fails, and they do not exhibit a failed run of a
factorer that applies every mandatory gcd screen before extension. Keeping
four capped beams proves polynomial running time, but no theorem shows that
every useful path has a prefix within polynomial width in one of them. The
true Pareto frontier is also not shown to have polynomial size.

## 4. Canonical-residue closure is a different source operation

Let the current refined blocks generate

\[
H=\langle q_1,\ldots,q_m\rangle
\subseteq(\mathbb Z/N\mathbb Z)^\times.
\]

For a public exponent vector \(e\), canonical-residue closure computes

\[
c=\left[\prod_jq_j^{e_j}\right]_N,
\qquad
w=[c^{-1}]_N,
\qquad
cw=1+kN.
\tag{5}
\]

If the raw positive product is an authorized integer below \(N\), this is
ordinary P70 feedback. If the raw product is at least \(N\), uses negative
exponents, or exceeds the occurrence capacities, (5) is a strictly different
operation. P70's divisor identity \(k(g)=K\bmod g\) does not transfer to this
new canonical representative.

At the residue level, (5) adds nothing:

\[
c,w\in H,
\qquad
\langle H,c,w\rangle=H.
\tag{6}
\]

The possible gain is entirely in the integer representation. Gcd-free
refinement of the canonical integers \(c,w\) can expose factors whose
individual residue classes lie outside \(H\), even though their products lie
in \(H\). This is exactly the representation-level phenomenon isolated by
P78.

For one selected exponent vector, (5), all direct gcd screens, and gcd-free
refinement have polynomial bit cost. Exhausting fixed support and a polynomial
exponent menu is also polynomial. Exhausting all dense vectors is exponential;
a polynomial random sample or capped beam needs a separate success law.

## 5. Exact effect on P78's \(N=4033\) state

After P78's feedback refinement,

\[
H_1=\langle2,5\rangle
\]

contains the displayed separator

\[
c=5\cdot2^{13}\bmod4033=630.
\]

Canonical-residue closure makes it a legal candidate. Its canonical inverse is

\[
w=3220,
\qquad
630\cdot3220=1+503\cdot4033.
\]

It factors immediately:

\[
\gcd(630-1,4033)=37,
\qquad
\gcd(630-3220,4033)=37.
\tag{7}
\]

The raw word \(5\cdot2^{13}=40960\) is above \(N\). Thus (7) directly removes
the finite-positive-box obstruction stated in P78 for this known word.

There is also a smaller certificate that lies in the proposal's literal
structured exponent menu. Since

\[
n=\lceil\log_2 4033\rceil=12,
\]

the support-two exponents \(2\) and \(8\) are allowed. They give

\[
c'=5^2 2^8\bmod4033=6400\bmod4033=2367,
\]

\[
w'=443,
\qquad
2367\cdot443=1+260\cdot4033,
\]

and

\[
\gcd(2367+1,4033)
=\gcd(2367-443,4033)
=37.
\tag{8}
\]

So a post-refinement exhaustive support-two scan over the advertised small
exponents factors this fixed witness. This is a real algorithmic difference
from the positive whole-block source: the raw product \(6400\) is too large,
but its canonical residue is useful.

## 6. What remains unproved

The fixed witness in (8) does not give an all-input result.

- The algorithm must first reach P78's special refinement state. The CRT beam
  supplies no theorem that it selects the required earlier product.
- No proof shows that every useful refined subgroup has a separator of fixed
  support with exponents in a polynomial menu, or that random dense vectors
  hit one with inverse-polynomial probability.
- Canonical reduction removes the finite-box restriction from P71, but it
  leaves the subgroup-word selection problem. In the one-generator
  self-inverse subtarget, this still contains the order-finding boundary from
  P71.
- P72 does not kill this adaptive structured source, because its fresh-uniform
  hypotheses do not apply. It also gives no positive support for the beam.

The defensible result is therefore narrow but nontrivial: CRT bookkeeping is
exact and useful for implementation, while canonical-residue closure is the
one genuine operation change. That operation provably converts P78's
post-refinement subgroup gain into an immediate factor on the fixed
\(4033\) witness. The missing object is still a uniform selector theorem.
