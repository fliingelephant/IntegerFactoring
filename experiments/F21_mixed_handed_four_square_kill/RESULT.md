# F21 candidate: mixed-handed independent outputs are diffuse, but one fibre is a projective graph

**Status:** candidate kill-first result. The symbolic statements below have not
had a hostile audit or proof-blind reconstruction.

**Family:** F14, Hurwitz one-sided gcds.

**Closest prior route and material difference.** P25/X19 proves the birthday
obstruction for uniform norm-shell samples. P28/X22 treats the integral slice,
fixed transform menus, and a matched-handed unit-stabilizer survivor. P30 proves
that the Pollack--Treviño residual-only four-square source is exactly diffuse for
the row of a greatest common right divisor and, separately, for the image of a
greatest common left divisor. The present note studies the two orientations that
P30 deliberately leaves uncontrolled: the image of the right-gcd output and the
row of the left-gcd output. It proves a normalization-independent atom bound,
closes independent-output mixed-handed lotteries and the wrong-hand
unit-stabilizer menu, then derives the exact same-source row--image coupling and
exhibits a residual-compatible counterexample to the most natural 12-unit cross
menu. It does not close joint decoding of many coupled samples.

The primary four-square source is Paul Pollack and Enrique Treviño,
[*Finding the Four Squares in Lagrange's Theorem*](https://pollack.uga.edu/finding4squares.pdf),
INTEGERS 18A (2018). The source/interface and its expected bit complexity are
already checked in P30; this note uses that promoted result.

## 1. Conditional product uniformity

Let \(n=pq\), where \(p\ne q\) are odd primes. Let \(M\) be an odd
squarefree multiple of \(n\), let \(x,y\) initially be uniform modulo \(M\), and
put

\[
R=-x^2-y^2\pmod M.
\]

Assume acceptance and completion depend on \((x,y)\) only through \(R\) and
fresh randomness, every accepted \(R\) is a unit, completion returns \(z,w\)
with \(z^2+w^2\equiv R\pmod M\), and

\[
\beta=x+yi+zj+wk
\]

is primitive. This is the P30 interface and includes the reduced
distinct-prime-semiprime branch of Pollack--Treviño.

For \(r\in\{p,q\}\), put

\[
\chi_r=\left(\frac{-1}{r}\right),\qquad
S_r=\{[u:v]\in\mathbf P^1(\mathbf F_r):u^2+v^2\ne0\},
\qquad s_r=|S_r|=r-\chi_r.
\]

P30 states the individual uniform marginals. In fact the stronger pair law is
immediate from the same proof:

> **Product-uniform fibre lemma.** Conditional on a fixed accepted residual and
> fixed completion randomness, the pair
> \((\operatorname{row}_p(\beta),\operatorname{row}_q(\beta))\) is exactly
> uniform on \(S_p\times S_q\). Separately, the image pair is exactly uniform on
> \(S_p\times S_q\).

Indeed, conditional on \(R=R_0\), the full fibre is the CRT product

\[
\prod_{\ell\mid M}
\{(x_\ell,y_\ell):x_\ell^2+y_\ell^2=-R_0\}.
\]

It is uniform, and a residual-only acceptance/completion kernel multiplies
every member by the same weight. Projection to the \(p\)- and \(q\)-factors is
therefore the independent uniform product of the two local conics. P30's local
conic-to-line maps are bijections onto \(S_p\) and \(S_q\), proving the row
claim. Its image bijections prove the second claim. This is conditional
independence of the two unknown-prime components; it is not independence of the
row and image of one local matrix.

## 2. Arbitrary normalization cannot concentrate the wrong orientation much

Let \(D_R\) be any greatest common right divisor of \(n\) and \(\beta\). It has
norm \(n\) and its local row pair equals that of \(\beta\). The algorithm that
returns it may use arbitrary deterministic or random Euclidean quotient ties,
may inspect the entire transcript, and may choose any left-unit normalization.

For a row pair \(a\in S_p\times S_q\), let \(O_a\) be the corresponding
left-unit orbit in the norm-\(n\) shell. P25 gives

\[
|O_a|=24,
\]

and different row pairs give disjoint orbits. Conditional on the fixed
residual/completion, the row pair \(a\) is uniform. Given \(a\), the most
general output rule is an arbitrary probability kernel supported on \(O_a\).

Now multiply the returned output by an independent uniform actual left unit
\(U\). The left-unit action on \(O_a\) is free and transitive, so \(UD_R\) is
uniform on \(O_a\), independently of the original normalization kernel. Thus
\(UD_R\) is uniform on the union of the \(s_ps_q\) allowed orbits.

The full norm-\(n\) shell has \(24(p+1)(q+1)\) elements. By P25, exactly
\(24(q+1)\) of them have any specified image line modulo \(p\). Therefore, for
every line \(L\in\mathbf P^1(\mathbf F_p)\),

\[
\Pr(\operatorname{im}_p(UD_R)=L)
\le \frac{q+1}{s_ps_q}.                                      \tag{1}
\]

The two units \(U=\pm1\) preserve the original image line. Hence the left side
of (1) is at least one twelfth of the corresponding atom before randomization:

\[
\boxed{
\Pr(\operatorname{im}_p(D_R)=L)
\le \frac{12(q+1)}{s_ps_q}
\le \frac{27}{p+1}.}                                        \tag{2}
\]

The last inequality uses

\[
\frac{s_r}{r+1}\ge\frac23
\]

for every odd prime \(r\): equality can only be approached in the split case,
whose smallest prime is \(5\). Symmetrically,

\[
\Pr(\operatorname{im}_q(D_R)=L)\le\frac{27}{q+1}.             \tag{3}
\]

The same proof with handedness reversed gives, for an arbitrarily
right-normalized greatest common left divisor \(D_L\),

\[
\Pr(\operatorname{row}_r(D_L)=L)\le\frac{27}{r+1}.            \tag{4}
\]

These bounds hold conditional on every residual and completion outcome and are
therefore preserved under mixing. They are independent of Euclidean quotient
and tie choices. This is the strongest normalization-independent conclusion:
the uncontrolled orientation need not be exactly uniform, but none of its
atoms can have inverse-polynomial mass on a balanced semiprime.

## 3. Consequences for independent outputs and wrong-hand unit orbits

Let two finder executions be independent; their residuals and completions may
have arbitrary, unequal distributions.

* Two right-gcd outputs tested by a greatest common **left** divisor collide at
  a fixed \(r\) with probability at most \(27/(r+1)\), by (2)--(3).
* Two left-gcd outputs tested by a greatest common **right** divisor obey the
  same bound, by (4).
* A right-gcd output and a left-gcd output from independent executions obey the
  same bound in either comparison hand: one controlled orientation is uniform,
  while the other has maximum atom (2) or (4).

In every case, a proper one-sided gcd requires a local equality at \(p\) or at
\(q\). No independence between those two events is needed, so one comparison
has proper-event probability at most

\[
27\left(\frac1{p+1}+\frac1{q+1}\right).                       \tag{5}
\]

For \(K\) independent outputs, every-pair testing multiplies (5) by
\(\binom K2\). A fixed menu of projective unit transforms only applies
projective bijections to the lines, so a union bound adds the number of tested
relative classes. The same is true for any polynomial menu of separate fixed
transforms whose local actions are projective bijections. Along \(p<q<2p\),
fixed polynomial \(K\) and menu size give

\[
\operatorname{poly}(\log n)/\sqrt n,
\]

which is exponentially small in the input bit length.

There is also a same-output consequence. Let

\[
G=\mathcal H^\times/\{\pm1\}\simeq A_4
\]

act on the image line of \(D_R\) by left multiplication. P30's unit analysis
shows that at most fourteen lines in \(\mathbf P^1(\mathbf F_r)\) have a
nontrivial stabilizer. Equations (2)--(3) give

\[
\Pr(\operatorname{Stab}_G(\operatorname{im}_rD_R)\ne1)
\le \min\left(1,\frac{378}{r+1}\right).                       \tag{6}
\]

Enumerating the twelve projective left-unit classes can produce a proper
left gcd within one \(D_R\)-orbit only if the two local image stabilizers
differ. Without local independence, (6) bounds that mismatch by

\[
378\left(\frac1{p+1}+\frac1{q+1}\right).                      \tag{7}
\]

The dual statement holds for the row stabilizers of one \(D_L\) under right
units. Thus the normalization ambiguity does not rescue the wrong-hand
single-orbit stabilizer mechanism.

These are ordinary union-of-rare-event bounds. They do not cover a statistic
that combines partial information from many samples before asking for any
individual line equality.

## 4. The exact same-source row--image graph

The same source is different because its row and image are maximally coupled.
Use P30's local split

\[
i\mapsto I=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
j\mapsto J=\begin{pmatrix}s&t\\t&-s\end{pmatrix},
\qquad s^2+t^2=-1.
\]

Put

\[
A=zs+wt,\qquad B=zt-ws,\qquad
J_C=\begin{pmatrix}A&B\\B&-A\end{pmatrix},
\]

where \(C=zj+wk\). Then

\[
J_C^2=(A^2+B^2)I_2=-(z^2+w^2)I_2,
\]

so \(J_C\) is invertible at every accepted local prime and preserves \(S_r\).
For every point of the residual conic, including the exceptional zero-first-row
and zero-first-column points in P30,

\[
\boxed{
\operatorname{im}_r(\beta)
=J_C\,\operatorname{row}_r(\beta).}                           \tag{8}
\]

For a nonexceptional row \([u:v]\), the conic equation gives the scale

\[
\lambda=\frac{2(Au+Bv)}{u^2+v^2}.
\]

The first-column image becomes

\[
[\lambda u:-\lambda v+2B]
=[Au+Bv:Bu-Av]
=J_C[u:v].
\]

At \([u:v]=[0:1]\), the first column may vanish, but the second column gives
\([B:-A]=J_C[0:1]\). At the exceptional row \([B:-A]\), the matrix has zero
first row and image \([0:1]=J_C[B:-A]\). Hence (8) is a total projective
identity, not a generic-point formula.

Combining Section 1 and (8), conditional on a fixed completion the complete
local law is

\[
(L_p,L_q)\sim\operatorname{Unif}(S_p\times S_q),\qquad
(I_p,I_q)=(J_{C,p}L_p,J_{C,q}L_q).                             \tag{9}
\]

Thus the row pair is product-uniform, but the image is a deterministic graph
over it. Equation (8) concerns the raw \(\beta\). A right-gcd output preserves
the row but its left cofactor and left normalization change the image; a
left-gcd output preserves the image but its right cofactor and right
normalization change the row. No image formula for \(D_R\) follows from (8).

## 5. A split-free same-source coefficient transcript

Let \(D_R\) and \(D_L\) be respectively right- and left-gcd outputs from the
same \(\beta\). Then

\[
\operatorname{row}_r(D_R)=\operatorname{row}_r(\beta),\qquad
\operatorname{im}_r(D_L)=\operatorname{im}_r(\beta).
\]

For a projective Hurwitz unit \(U\), a right-gcd comparison of \(D_R\) with
\(D_LU\) succeeds locally exactly when

\[
\operatorname{row}_r(D_LU)=\operatorname{row}_r(D_R).
\]

By (8), this is equivalent to

\[
\operatorname{im}_r(D_LU)=J_C\operatorname{row}_r(D_LU).
\]

A rank-one matrix \(X\) has
\(\operatorname{im}(X)=J_C\operatorname{row}(X)\) exactly when
\(J_C^{-1}X\) is symmetric. In the displayed quaternion split, the matrices of
\(1,j,k\) are symmetric and that of \(i\) is skew-symmetric. Since the matrix of
\(\bar C\) is a nonzero scalar multiple of \(J_C^{-1}\), the condition is

\[
\boxed{
[i](\bar C D_LU)\equiv0\pmod r,}                              \tag{10}
\]

where \([i](Q)\) denotes the \(i\)-coordinate of \(Q\). This statement is
split-free: \(C=zj+wk\), \(D_L\), \(U\), and the coordinate are global Hurwitz
data. For half-integral coordinates, use the doubled integer numerator; odd
\(r\) makes the zero condition identical.

Consequently the natural 12-unit same-source cross test is exactly the public
integer transcript

\[
c_U=2[i](\bar C D_LU),\qquad
\gcd(n,c_U),\qquad U\in G.                                   \tag{11}
\]

A nontrivial gcd in (11) is precisely a proper mixed-handed collision. The
quaternion gcd returns the same prime as its norm; (11) shows that this
particular apparent escape can also be written as twelve exact public
integer-coordinate computations ending in gcds. The analogous left-gcd
comparison of \(UD_R\) with \(D_L\) uses \(2[i](\bar CUD_R)\).

## 6. A residual-compatible exact failure of all twelve cross tests

The menu (11) has no pointwise guarantee, even for the most direct canonical
normalization.

Take

\[
n=91=7\cdot13,\qquad M=\operatorname{lcm}(91,3)=273,
\]

and the valid residual-fibre point

\[
(x,y,z,w)=(172,82,0,1).
\]

Indeed,

\[
172^2+82^2+1=36309=133\cdot273,
\]

so the least residual is \(R=1\), it is a unit and \(1\pmod4\), completion is
\(1=0^2+1^2\), and the four coordinates are primitive.

Normalize a Hurwitz quaternion by choosing the lexicographically least doubled
coordinate tuple in its appropriate unit orbit. The corresponding one-sided
generators are

\[
D_R=\frac{-19+i+j+k}{2},\qquad
D_L=\frac{-19+i-j+k}{2}.                                     \tag{12}
\]

They are certified without factoring or a line computation:

\[
91=\bar D_RD_R=D_L\bar D_L,
\]

and, with \(\beta=172+82i+k\),

\[
\beta=\frac{-35-19i-j-3k}{2}\,D_R
=D_L\,\frac{-35-19i+j-3k}{2}.                                \tag{13}
\]

Both \(D_R,D_L\) have norm \(91\); the primitive-gcd lemma therefore makes
them greatest common one-sided divisors. In each relevant unit orbit the scalar
coordinate \(-19/2\) is uniquely minimal: pure units can only select a signed
coordinate, while a half unit gives half a signed coordinate sum, whose
absolute value is at most \(11/2\). Thus (12) is exactly the stated
lexicographic normalization.

Here \(C=k\), and

\[
\bar C D_L=-kD_L=\frac{1-i-j+19k}{2}.
\]

Order the twelve projective units as

\[
1,i,j,k,
\frac{1+\epsilon_i i+\epsilon_j j+\epsilon_k k}{2}
\quad(\epsilon_i,\epsilon_j,\epsilon_k)
=(-,-,-),(-,-,+),(-,+,-),(-,+,+),(+,-,-),(+,-,+),(+,+,-),(+,+,+).
\]

The doubled \(i\)-coordinates in (11) are

\[
(-1,1,-19,-1,9,8,-10,-11,10,9,-9,-10).                       \tag{14}
\]

Every entry in (14) is coprime to \(91\). Hence none of the twelve right-unit
cross comparisons even collides at one local prime; every resulting right gcd
has \(n\)-part \(1\). This is an exact counterexample to a universal
constant-success claim for the canonical 12-unit same-source menu. It does not
show that its success probability tends to zero over the random row fibre.

The authorized finite run F14-M02 enumerates the same
certificate. Its structured output records doubled tuples

\[
D_R=(-19,1,1,1),\qquad D_L=(-19,1,-1,1)
\]

and twelve coefficient gcds all equal to \(1\). It also checks the local
projective/coefficient dictionary on fourteen small distinct odd semiprimes.
The finite scan is not used for any unbounded statement.

## 7. What varying graph constraints do and do not provide

For independent samples, retaining many equations (8) does not change the
proved atom bounds for testing individual pairs: all-pairs and fixed-menu
testing is still only a union of the rare events bounded in Section 3.

For a same-source sample, (9) is genuine retained structure. Across samples
\(t\), one obtains known global quaternions

\[
C_t=z_tj+w_tk
\]

and exact local graph equations

\[
I_{t,r}=J_{C_t,r}L_{t,r}.
\]

The matrices \(J_{C_t,r}\) require a local split to display, but (10)--(11)
show how every single cross-unit incidence is evaluated without a split. What
is missing is a joint decoder that combines several nonvanishing coefficient
vectors without first winning one local equality. If every \(c_{t,U}\) is a
unit modulo \(n\), an individual transcript records no public partial factor;
if it vanishes modulo both primes, it records only a trivial equality. The
present proof supplies no operation on many such transcripts that is guaranteed
to separate their two CRT components.

In particular, the atom theorem does **not** cover:

* an adaptive invariant combining several \(D_{R,t},D_{L,t},C_t\) before any
  pairwise gcd;
* a polynomial system, resultant, or noncommutative product retaining weak
  constraints from every graph;
* a spectral/discrepancy theorem for the same-source section incidence
  \(\operatorname{row}(D_L)\in J_C^{-1}\operatorname{im}(D_L)G\);
* a completion-dependent normalization deliberately designed around several
  samples.

No inverse-polynomial all-semiprime success bound and no asymptotic obstruction
is proved for those genuinely sample-combining mechanisms.

## 8. Bit complexity and scope

The Pollack--Treviño call has expected polynomial bit complexity by P30. A
one-sided Hurwitz gcd has \(O(\log n)\) norm-contracting divisions on
\(O(\log n)\)-bit coordinates. Enumerating 24 actual units for lexicographic
normalization and the twelve projective classes in (11) is constant work.
Since \(z^2+w^2=R<M=n^{O(1)}\) and \(D_L\) has norm \(n\), all coordinates in
\(\bar C D_LU\) have \(O(\log n)\) bits. Integer coordinate extraction and gcd
therefore have deterministic polynomial bit complexity. For polynomially many
independent calls, every-pair comparisons and fixed polynomial menus remain
polynomial in number and bit cost.

The exact lemmas apply to every distinct-odd-prime semiprime satisfying the P30
residual-only interface, with no balance assumption. The exponential failure
consequence from (5) and (7) is only along an infinite balanced family. The
counterexample is one exact interface-compatible fibre at \(n=91\). Nothing
here treats the ramified prime \(2\), repeated primes, deeper local ideal types,
arbitrary composites, or a completion that examines the particular preimage
\((x,y)\). This is a method obstruction and a survivor map, not an all-input
factoring algorithm.

## 9. Computation provenance

F14-M01 is preserved but **non-authoritative/excluded**: it was run before a
canonical computation-ledger row existed. No claim relies on it.

F14-M02 was pre-registered in the canonical ledger and then run under its
120-second hard timeout. The exact source, dependency, command, hashes, exit
status, duration, log, and output are recorded in `RUN_MANIFEST.md`. Its role is
only to certify the finite \(n=91\) witness and to test finite dictionaries; the
product law, atom theorem, graph identity, coefficient equivalence, and
asymptotic bounds are symbolic proofs.

## Candidate theorem and retry criterion

> **Mixed-handed residual-fibre boundary.** For a distinct-odd-semiprime
> residual-only four-square source, the row pair of a right-gcd output is
> conditionally product-uniform on \(S_p\times S_q\). Under arbitrary
> transcript-dependent left normalization, each local image atom is at most
> \(27/(r+1)\). Dually, every local row atom of an arbitrarily right-normalized
> left-gcd output is at most \(27/(r+1)\). Hence polynomially many independent
> outputs, every-pair comparisons in either hand, fixed polynomial transform
> menus, and wrong-hand single-output unit-stabilizer tests have exponentially
> small success on an infinite balanced family. For a same-source pair, the raw
> quaternion obeys the exact graph
> \(\operatorname{im}_r\beta=J_{C,r}\operatorname{row}_r\beta\), and every
> 12-unit cross incidence is the split-free congruence
> \(2[i](\bar C D_LU)=0\pmod r\). The lexicographically normalized
> \(n=91,R=1\) fibre above makes all twelve coefficients coprime to \(n\), so
> this menu has no pointwise guarantee. The theorem does not bound a joint
> decoder that combines many same-source graph constraints.

A materially new retry must do one of two things:

1. give a factor-free joint decoder for polynomially many
   \((C_t,D_{R,t},D_{L,t})\) with a symbolic inverse-polynomial separation bound
   for every relevant semiprime and account for all bit complexity; or
2. prove a uniform discrepancy/spectral bound for the same-source graph-section
   incidence, valid for arbitrary completion outcomes and normalization
   kernels, strong enough to make every polynomial joint decoder or a precisely
   named subclass exponentially unlikely.

Another independent sample, all-pairs search, separate fixed-unit menu, or
single-coordinate gcd is already covered and is not a materially new retry.
