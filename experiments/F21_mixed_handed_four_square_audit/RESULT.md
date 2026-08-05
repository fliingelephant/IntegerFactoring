# F21 hostile audit: the independent-output boundary survives, and the same-source graph remains open

**Status:** hostile audit of
`experiments/F21_mixed_handed_four_square_kill/RESULT.md`.

**Verdict:** **passes with scope corrections and two proof-only
strengthenings.** I found no counterexample to the product-fibre theorem, the
normalization-independent atom bound, the raw row--image graph, either
split-free coefficient criterion, or the \(N=91\) certificate. The candidate
does not factor integers and does not obstruct an adaptive nonlinear joint
decoder. A proof-blind reconstruction of the corrected theorem is warranted.

This audit was proof-only. I ran no fresh mathematical computation. Read-only
hash and filesystem-metadata checks were used only to audit the preserved
F14-M02 provenance.

## 1. Material corrections and qualifications

### 1.1 What “fixed polynomial menu” may mean

The independent-output menu bound is valid only for a polynomially bounded
number of **separate fixed transforms** whose actions at both unknown primes
are projective bijections, with every tested transform pair counted in the
union bound. It covers a fixed menu depending publicly on \(n\), and it also
covers choosing from that menu by simply union-bounding over every possible
tested choice.

It does not cover:

* a transform that combines two or more samples;
* a transform singular at one unknown prime;
* an exponentially large menu selected implicitly;
* a map manufactured from the sampled coefficients with no prior polynomial
  list of possible projective actions.

Accordingly, “every-pair comparisons” means pairs coming from independent
finder executions. A right-gcd and left-gcd derived from the same \(\beta\)
are not independent and belong to the graph analysis.

### 1.2 The constant 14 is deliberate

For the uncontrolled image of a right-gcd output, or the uncontrolled row of a
left-gcd output, the line need not lie in the support \(S_r\). Therefore one
must not substitute P30's supported-line count \(e_r\le 12\) into the
wrong-hand stabilizer argument. On all of
\(\mathbf P^1(\mathbf F_r)\), the safe count is fourteen:

* the three projective involutions have at most two fixed lines each;
* the four order-three subgroups have at most two fixed lines each.

Faithfulness for every odd \(r\), including \(r=3\), ensures that none of these
nonidentity classes becomes scalar. Thus the candidate's constants \(378=14
\cdot 27\) and the resulting asymptotic bound are correct. The bound is loose
at small primes but still valid.

### 1.3 The finite output stores the \(n\)-local point, not its full \(M\)-lift

F14-M02 records

\[
(x,y,z,w)\bmod n=(81,82,0,1),
\]

whereas the report's full residual-compatible lift is
\((172,82,0,1)\) modulo \(M=273\). The driver checks the conic modulo
\(n\); it does not itself store or check the chosen residue modulo the
auxiliary prime \(3\). This is not a mathematical defect in the certificate:
\(172\equiv81\pmod {91}\), and the full \(M\)-congruence is verified by
hand in Section 8 below. More generally CRT supplies such an auxiliary-prime
lift. The phrase “the structured output records the same certificate” should
be read as “records its \(n\)-local core.”

### 1.4 Provenance is internally consistent, with one sealing limitation

All three recorded SHA-256 values match the present bytes, and the log, output,
driver, dependency, ledger row, and manifest agree on the family, inputs,
paths, and timeout command. The root execution transcript and filesystem times
place the working-tree ledger row before M02. However:

* the computation-ledger row and F21 directory are not in a checkpoint commit,
  so immutable Git history does not independently prove temporal
  preregistration;

The root execution transcript records shell exit status zero. Since the
recorded command ran under `timeout 120s`, rather than returning timeout status
124, this certifies completion before 120 seconds. The “approximately 30.0
seconds” duration is only an observed approximation; no exact elapsed time was
captured in a sealed artifact. These provenance qualifications do not affect
the theorem: the finite witness is checked directly below, and no unbounded
statement depends on the run.

## 2. Exact conditional product law

Let \(R_0\) be a fixed accepted unit residual. Since the original \((x,y)\)
is uniform modulo the squarefree \(M\), conditioning on \(R=R_0\) gives the
uniform distribution on

\[
\mathcal F(R_0)=
\{(x,y)\bmod M:x^2+y^2=-R_0\}.
\]

CRT is an actual bijection

\[
\mathcal F(R_0)\simeq
\prod_{\ell\mid M}
\{(x_\ell,y_\ell)\in\mathbf F_\ell^2:
  x_\ell^2+y_\ell^2=-R_0\}.
\]

Every point of a fixed residual fibre receives the same acceptance weight. If
the completion coins, or any positive-probability completion outcome, are also
fixed, their conditional law still depends only on \(R_0\), so they do not
reweight the fibre. The local factors are consequently independent and
uniform.

At \(r=p,q\), P30's conic-to-row map is a bijection onto

\[
S_r=\{[u:v]:u^2+v^2\ne0\},\qquad
s_r=|S_r|=r-\left(\frac{-1}{r}\right).
\]

Its conic-to-image map is separately a bijection onto the same set. Therefore,
conditional on every fixed residual/completion outcome of positive
probability,

\[
(\operatorname{row}_p\beta,\operatorname{row}_q\beta)
 \sim \operatorname{Unif}(S_p\times S_q),
\]

and, separately,

\[
(\operatorname{im}_p\beta,\operatorname{im}_q\beta)
 \sim \operatorname{Unif}(S_p\times S_q).
\]

This proves independence of the two unknown-prime components. It proves no
independence between row and image at one prime.

## 3. The 24-element orbit argument and exact atom constants

Fix a row pair \(a\in S_p\times S_q\). Every greatest common right divisor
\(D_R\) of \(n\) and \(\beta\) has norm \(n\), has local row pair \(a\), and
lies in the unique left-unit orbit \(O_a\) with those rows. P25 gives

\[
|O_a|=24.
\]

The action is free: \(UD=D\) in the quaternion division algebra implies
\(U=1\). Hence it is regular. This remains true when the Euclidean transcript
and normalization inspect all of \((x,y,z,w)\): after conditioning on \(a\),
the output is merely an arbitrary probability kernel supported on \(O_a\).

Now independently draw an actual Hurwitz unit \(U\) uniformly from the 24
units. Conditional on any returned \(D_R\in O_a\), \(UD_R\) is uniform on
\(O_a\). Since \(a\) itself is product-uniform, \(UD_R\) is uniform on the
disjoint union of the \(s_ps_q\) allowed row orbits, a set of size
\(24s_ps_q\).

P25's right-unit quotient by the image pair gives the exact full-shell count

\[
#\{D:\operatorname{nrd}D=n,
       \operatorname{im}_pD=L\}=24(q+1)
\]

for every specified \(L\in\mathbf P^1(\mathbf F_p)\). Therefore

\[
\Pr(\operatorname{im}_p(UD_R)=L)
\le \frac{q+1}{s_ps_q}.                                      \tag{1}
\]

If the unrandomized output already has image \(L\), the two actual units
\(\pm1\) preserve it. Thus

\[
\Pr(\operatorname{im}_p(UD_R)=L)
\ge \frac2{24}
\Pr(\operatorname{im}_pD_R=L).
\]

Combining this with (1) proves the exact candidate bound

\[
\Pr(\operatorname{im}_pD_R=L)
\le \frac{12(q+1)}{s_ps_q}.                                  \tag{2}
\]

For every odd prime,

\[
\frac{s_r}{r+1}=
\begin{cases}
1,&r\equiv3\pmod4,\\
(r-1)/(r+1),&r\equiv1\pmod4,
\end{cases}
\quad\ge\frac23.
\]

The minimum is attained at the smallest split prime \(r=5\); at \(r=3\) the
ratio is one. Hence

\[
\Pr(\operatorname{im}_pD_R=L)
\le \frac{27}{p+1}.                                          \tag{3}
\]

The constant \(12\) comes exactly from \(24/2\), and \(27\) comes exactly from
\(12/(2/3)^2\). Both include all odd small primes. Interchanging \(p,q\) gives
the other image bound. Reversing handedness gives, for an arbitrarily
right-normalized greatest common left divisor,

\[
\Pr(\operatorname{row}_rD_L=L)
\le \min\left(1,\frac{27}{r+1}\right).                       \tag{4}
\]

All bounds hold conditionally on every residual/completion outcome and survive
mixing. No Euclidean quotient or tie convention appears in the proof.

## 4. Every independent-output comparison hand

For one execution:

* \(D_R\) has a controlled uniform row and an image satisfying (3);
* \(D_L\) has a controlled uniform image and a row satisfying (4).

For two independent executions, the collision probability of any two local
lines is at most \(27/(r+1)\) whenever each line is one of these four
orientations. Indeed, a controlled line is uniform on \(S_r\), while for two
uncontrolled laws \(\mu,\nu\),

\[
\sum_L\mu(L)\nu(L)
\le\min(\|\mu\|_\infty,\|\nu\|_\infty).
\]

This proves all four one-sided-gcd cases:

1. right/right compared by a right gcd (controlled rows);
2. right/right compared by a left gcd (uncontrolled images);
3. left/left compared by a left gcd (controlled images);
4. left/left compared by a right gcd (uncontrolled rows);

and both mixed output types in either comparison hand.

It also covers either product order. For local nonzero rank-one matrices,

\[
AB=0\iff\operatorname{im}(B)=\ker(A),
\]

and \(\ker(A)\) is a fixed projective bijection of the row line of \(A\).

A proper one-sided gcd, or a product zero at exactly one unknown prime, is
contained in the union of the two local equality events. Thus one specified
independent-output comparison has probability at most

\[
27\left(\frac1{p+1}+\frac1{q+1}\right).                      \tag{5}
\]

If \(J\) transformed comparisons are actually tested, with every transform a
separate fixed projective bijection locally, the right side is multiplied by
\(J\). In particular, \(K\) independent calls and fixed menus of polynomial
size give only

\[
\operatorname{poly}(\log n)/\sqrt n
\]

on \(p<q<2p\). This is exponentially small in the binary input length. The
proof uses a union bound, not local \(p,q\) independence.

## 5. Wrong-hand single-output unit orbits

Let \(G=\mathcal H^\times/\{\pm1\}\simeq A_4\). A line with nontrivial
\(G\)-stabilizer is fixed by a nonidentity projective unit. The full-projective
count in Section 1.2 is at most fourteen. Therefore

\[
\Pr(\operatorname{Stab}_G(\operatorname{im}_rD_R)\ne1)
\le \min\left(1,\frac{378}{r+1}\right).                      \tag{6}
\]

For the twelve projective left-unit classes in one \(D_R\)-orbit, a proper left
gcd exists if and only if the two local image stabilizers differ. A mismatch
implies that at least one is nontrivial, so

\[
\Pr(H_p\ne H_q)
\le378\left(\frac1{p+1}+\frac1{q+1}\right).                  \tag{7}
\]

The dual statement holds for the row of \(D_L\) under right units. This proof
covers the twelve Hurwitz projective classes. It is not a theorem about an
arbitrary transcript-generated same-output transform family.

## 6. The total raw row--image graph

Under P30's split, put

\[
J_C=
\begin{pmatrix}A&B\\B&-A\end{pmatrix},
\qquad A=zs+wt,\quad B=zt-ws.
\]

Then

\[
J_C^2=(A^2+B^2)I=-(z^2+w^2)I,
\]

so \(J_C\) is invertible at every accepted local prime. Moreover

\[
(J_C[u:v])_1^2+(J_C[u:v])_2^2
=(A^2+B^2)(u^2+v^2),
\]

so it preserves \(S_r\).

For an arbitrary row representative \([u:v]\in S_r\), write

\[
\lambda=\frac{2(Au+Bv)}{u^2+v^2},\qquad
x=\lambda u-A,\quad y=\lambda v-B.
\]

The first-column image, when nonzero, is

\[
[\lambda u:-\lambda v+2B]
=[Au+Bv:Bu-Av]
=J_C[u:v].
\]

There are no omitted points:

* at \([u:v]=[0:1]\), the first column is zero and the second column gives
  \([B:-A]=J_C[0:1]\);
* at \([u:v]=[B:-A]\), equivalently the conic point
  \((x,y)=(-A,-B)\), the first row is zero, the image is \([0:1]\), and
  \(J_C[B:-A]=[0:A^2+B^2]=[0:1]\).

When \(B=0\), these descriptions meet at the same exceptional point and remain
valid. Thus, with the candidate's convention of writing a row line as a
column coordinate,

\[
\boxed{\operatorname{im}_r\beta
=J_{C,r}\operatorname{row}_r\beta}                           \tag{8}
\]

is a total projective identity. Its sign and scalar conventions are correct.
It is an identity for raw \(\beta\), not for the uncontrolled orientation of a
normalized one-sided gcd output.

## 7. Both split-free cross-hand coefficient criteria

Let \(L=\operatorname{row}_r\beta\). For a right-gcd output \(D_R\) and
left-gcd output \(D_L\) from the same \(\beta\),

\[
\operatorname{row}_rD_R=L,
\qquad
\operatorname{im}_rD_L=J_CL.
\]

For a projective right unit \(U\), a right-gcd comparison of \(D_R\) with
\(D_LU\) collides locally exactly when

\[
\operatorname{im}(D_LU)=J_C\operatorname{row}(D_LU).         \tag{9}
\]

If \(X\) is nonzero rank one, then

\[
\operatorname{im}X=J_C\operatorname{row}X
\iff J_C^{-1}X\text{ is symmetric}.                          \tag{10}
\]

To see this, write \(X=ab^T\). The left condition is
\(a\parallel J_Cb\), which is equivalent to
\(J_C^{-1}X\) being a scalar multiple of \(bb^T\). The converse follows from
the same rank-one argument.

The split matrices of \(1,j,k\) are symmetric, while the split matrix of
\(i\) is skew-symmetric. Also

\[
\operatorname{Mat}(\bar C)=-J_C
\]

is a nonzero scalar multiple of \(J_C^{-1}\). In odd characteristic,
symmetry is therefore exactly the vanishing of the \(i\)-coordinate:

\[
\operatorname{row}_r(D_LU)=\operatorname{row}_rD_R
\iff
2[i](\bar C D_LU)\equiv0\pmod r.                             \tag{11}
\]

The factor two merely clears Hurwitz half-integers and is invertible modulo
odd \(r\).

For the opposite hand, left multiplication preserves a matrix's row space.
Thus a left-gcd comparison of \(UD_R\) with \(D_L\) collides locally exactly
when

\[
\operatorname{im}(UD_R)=J_C\operatorname{row}(UD_R),
\]

and the identical argument gives

\[
\operatorname{im}_r(UD_R)=\operatorname{im}_rD_L
\iff
2[i](\bar CUD_R)\equiv0\pmod r.                              \tag{12}
\]

These equivalences are normalization-invariant as twelve-element menu
statements: replacing \(D_L\) by \(D_LV\), or \(D_R\) by \(VD_R\), merely
permutes the projective unit classes.

## 8. Complete hand audit of the \(N=91\) witness

Take

\[
n=91=7\cdot13,\qquad
M=\operatorname{lcm}(91,3)=273,
\]

and \((x,y,z,w)=(172,82,0,1)\). The exact arithmetic is

\[
172^2=29584,\qquad82^2=6724,
\]

and hence

\[
172^2+82^2+1=36309=133\cdot273.
\]

Therefore the least residual is \(R=1\); it is a unit modulo \(273\), is
\(1\pmod4\), and the Pollack--Treviño completion branch \(m=1\) accepts
\(1=0^2+1^2\). The coordinates are primitive because \(w=1\).

Let

\[
D_R=\frac{-19+i+j+k}{2},\qquad
D_L=\frac{-19+i-j+k}{2}.
\]

Both norms are

\[
\frac{19^2+1+1+1}{4}=91.
\]

Direct multiplication gives

\[
\bar D_RD_R=91,\qquad D_L\bar D_L=91,
\]

and, for \(\beta=172+82i+k\),

\[
\frac{-35-19i-j-3k}{2}D_R=\beta,
\qquad
D_L\frac{-35-19i+j-3k}{2}=\beta.
\]

Thus \(D_R\) is a common right divisor and \(D_L\) a common left divisor of
\(91\) and \(\beta\). P30's primitive-gcd lemma says the greatest common
one-sided divisor has norm \(91\); these common divisors already have that
norm, so their handedness and gcd status are correct.

For lexicographic normalization, a pure unit can only place a signed existing
coordinate in the scalar slot. The unique minimum is \(-19/2\). A half unit
puts half a signed sum of the four coordinates in that slot, whose absolute
value is at most

\[
\frac12\left(\frac{19+1+1+1}{2}\right)=\frac{11}{2},
\]

strictly above \(-19/2\). Hence each displayed doubled tuple,

\[
D_R=(-19,1,1,1),\qquad D_L=(-19,1,-1,1),
\]

is exactly the lexicographically least member of its appropriate unit orbit.

Here \(C=k\), so

\[
\bar C D_L=-kD_L=\frac{1-i-j+19k}{2}.
\]

For the ordered projective units

\[
1,i,j,k,
\quad
\frac{1+\epsilon_i i+\epsilon_j j+\epsilon_k k}{2},
\]

with signs

\[
(---),(--+),(-+-),(-++),(+--),(+-+),(++-),(+++),
\]

the doubled \(i\)-coordinates of \(\bar C D_LU\) are exactly

\[
(-1,1,-19,-1,9,8,-10,-11,10,9,-9,-10).
\]

For a half unit the general entry is

\[
\frac{\epsilon_i-1-\epsilon_k-19\epsilon_j}{2},
\]

which reproduces the displayed order. None is divisible by \(7\) or \(13\),
so all twelve gcds with \(91\) equal one.

The analogous left-unit menu also fails for this same witness. A direct hand
calculation gives

\[
2[i](\bar CUD_R)=
(1,-1,-19,1,10,11,-9,-8,9,10,-10,-9)
\]

in the same unit order. Indeed, left multiplication by \(-k\) makes this
doubled \(i\)-coordinate the doubled \(j\)-coordinate of \(UD_R\); for a
half unit that coordinate is

\[
\frac{1-\epsilon_i-19\epsilon_j+\epsilon_k}{2}.
\]

The four pure-unit entries and the eight values of this formula give the
displayed list. They are again all coprime to \(91\). This strengthens, but is
not needed for, the candidate's pointwise counterexample. It still says
nothing about the menu's average success probability.

For completeness, the structured output's local data are consistent. Modulo
\(7\), its row/image pair is \(([0:1],[1:5])\); modulo \(13\), it is
\(([1:7],[1:6])\). With the driver's local choices, the graph parameters are
\([1:4]\) and \([1:0]\), and they carry those rows to those images.

## 9. Narrow linear-span consequence requested during audit

This consequence is valid, but it must not be overstated as a result about
nonlinear joint decoding.

Put

\[
Q_t=\bar C_tD_{L,t}.
\]

Locally, if \(L_t=\operatorname{row}_r\beta_t\), then by (8)

\[
\operatorname{im}_rQ_t
=(-J_{C_t})(J_{C_t}L_t)=L_t,
\]

because \(J_{C_t}^2\) is a nonzero scalar. The sign is immaterial.

The four matrices of \(1,i,j,k\) form a basis of
\(M_2(\mathbf F_r)\). Therefore

\[
\operatorname{span}\{Q_tU:U\in G\}
=Q_tM_2(\mathbf F_r)
=\{X:\operatorname{im}X\subseteq L_t\},
\]

a two-dimensional right ideal. For any nonempty index set \(T\),

\[
\dim\sum_{t\in T}Q_tM_2(\mathbf F_r)
=2\dim\operatorname{span}\{L_t:t\in T\}.
\]

Since the ambient column space has dimension two, the pooled dimension is
exactly two if every \(L_t\) in the subset is equal, and exactly four
otherwise. There is no rank-three case.

This statement is unaffected by arbitrary right normalization:
\(D_{L,t}\mapsto D_{L,t}V_t\) changes \(Q_t\) to \(Q_tV_t\), but
\(Q_tV_tM_2=Q_tM_2\).

For a fixed subset of \(m\ge2\) independent executions, the local rank-two
probability is exactly \(s_r^{1-m}\). Hence a fixed full span, the \(K\)
prefix spans, all \({K\choose2}\) pair spans, or any other fixed polynomial
family of subsets has a separation probability bounded by the corresponding
polynomial union of

\[
s_p^{1-m}+s_q^{1-m}
\le \frac1{s_p}+\frac1{s_q}.
\]

Thus **local span-dimension profiles** of these orbit blocks reduce to the same
line-equality partition and inherit the birthday obstruction.

This does not cover an adaptively or implicitly chosen exponential subset
family, exact row spaces rather than their dimensions, pivot or minor values,
coefficient-level linear systems, resultants, nonlinear products, or any
algorithm that uses the sampled entries to manufacture a new combined
invariant. Those remain instances of the joint-decoder survivor.

## 10. Bit complexity and scope

The candidate's bit-complexity accounting is adequate for every operation it
actually claims:

* P30 supplies an expected-polynomial Pollack--Treviño call with
  \(O(\log n)\)-bit public moduli and \(n^{O(1)}\)-sized integer
  intermediates.
* Hurwitz Euclidean division contracts norm by a fixed factor, so a one-sided
  gcd uses \(O(\log n)\) divisions on polynomial-bit coordinates.
* The 24-unit normalization and 12-class cross menu are constant-sized.
* Since \(z^2+w^2=R<M=n^{O(1)}\) and
  \(\operatorname{nrd}D_L=n\), every coordinate of
  \(\bar C D_LU\) has \(O(\log n)\) bits.
* Polynomially many independent calls, pair comparisons, and explicitly
  polynomial fixed menus therefore have polynomial total bit cost.

These are costs of the tested mechanisms, not a success proof. The probability
obstruction is exponential only along an infinite balanced family
\(p<q<2p\). The exact structural lemmas assume distinct odd primes and the
residual-only interface. They do not cover even inputs, repeated primes,
arbitrary composites, deeper local ideals, or a completion that reads the
particular fibre point.

## 11. F14-M02 artifact audit

I read the complete M02 driver, its complete imported enumeration dependency,
the complete structured output, the log, the manifest, and the canonical
ledger row.

The present-byte hashes are:

\[
\begin{array}{c|c}
\text{artifact}&\text{SHA-256}\\ \hline
\text{F14\_M02\_exact\_sections.py}&
\texttt{c37e8a5d461dfa79c14a89e99b655f13613aec665333bb0481bf1c43a71ad03c}\\
\text{F14\_M01\_exact\_sections.py}&
\texttt{4002517d33241a8ebe3dddb2ed7e99dfe965ad8b83e8d79aad08d85d443ab9ef}\\
\text{F14\_M02.json}&
\texttt{b4b44bb61eeaae72a4e4fc50b66d4139f13f9220956a525dd2abfe0342eba211}
\end{array}
\]

They equal the manifest and self-recorded output values. The one-line log
reports completion on exactly the fourteen declared inputs. The output contains
exactly those fourteen result records, declares family F14 and run F14-M02,
and records the same normalization and dependency hash.

The imported dependency correctly:

* enumerates doubled Hurwitz coordinates with common parity;
* checks the shell size \(24(p+1)(q+1)\);
* constructs row and image fibres of size 24;
* uses the twelve projective unit representatives;
* reconstructs the graph completion parameter with the correct inverse
  \((z,w)=(-sA-tB,-tA+sB)\);
* asserts, at both local primes, the coefficient-zero/projective-incidence
  equivalence;
* records only \(1\) or \(n\) coefficient gcds when declaring a menu failure.

The exact manifest command names a 120-second
`/opt/homebrew/bin/timeout` wrapper and redirects both output streams to the
declared log. Subject to the sealing qualifications in Section 1.4, the
artifact provenance passes.

F14-M01 remains **excluded/non-authoritative**. Its source is read only because
M02 imports it; no claim is promoted from the unregistered M01 run, output, or
log.

## 12. Strongest corrected theorem

> **Corrected mixed-handed residual-fibre boundary.** Let \(n=pq\), where
> \(p\ne q\) are odd primes, and use a residual-only four-square source
> satisfying P30. Conditional on every positive-probability accepted residual
> and completion outcome, the local row pair of \(\beta\) is exactly uniform
> on \(S_p\times S_q\), and the image pair is separately exactly uniform on
> that product.
>
> For any greatest common right divisor \(D_R\) returned with an arbitrary
> transcript-dependent left normalization,
>
> \[
> \Pr(\operatorname{im}_rD_R=L)
> \le \min\left(1,\frac{12(r'+1)}{s_rs_{r'}}\right)
> \le \min\left(1,\frac{27}{r+1}\right),
> \]
>
> where \(\{r,r'\}=\{p,q\}\). Dually, every local row atom of an arbitrarily
> right-normalized greatest common left divisor obeys the same \(27/(r+1)\)
> bound.
>
> Consequently, polynomially many independent executions, all pairwise
> one-sided-gcd comparisons in either hand, either product order, and an
> explicitly polynomial number of separate fixed transforms acting
> projectively at both unknown primes have exponentially small success on an
> infinite balanced family. The wrong-hand twelve-unit single-output
> stabilizer tests obey the \(378\)-constant version of the same bound.
>
> For one raw source sample,
>
> \[
> \operatorname{im}_r\beta
> =J_{C,r}\operatorname{row}_r\beta
> \]
>
> at every supported point, including both exceptional descriptions. The two
> same-source cross hands are exactly the split-free tests
>
> \[
> 2[i](\bar C D_LU)\equiv0\pmod r,
> \qquad
> 2[i](\bar CUD_R)\equiv0\pmod r.
> \]
>
> The lexicographically normalized \(n=91,M=273,R=1\) source point
> \((172,82,0,1)\) makes all twelve coefficients in each of these two menus
> coprime to \(91\), so neither menu has a pointwise guarantee.
>
> Finally, \(Q_t=\bar C_tD_{L,t}\) satisfies
> \(Q_tM_2(\mathbf F_r)=\{X:\operatorname{im}X\subseteq
> \operatorname{row}_r\beta_t\}\). Therefore every fixed polynomial family of
> pooled **dimension-only** orbit-span tests reduces to equality of the
> corresponding row lines and has the same sparse bound.

## 13. Explicit survivor and final verdict

The following remain completely open:

* an adaptive invariant combining polynomially many
  \((C_t,D_{R,t},D_{L,t})\) before any individual collision;
* a coefficient-level linear system, pivot/minor scheme, resultant, or
  noncommutative product that retains nonvanishing local information;
* an implicit or adaptive subset selector not reducible to a fixed polynomial
  family of span-dimension tests;
* a spectral/discrepancy theorem for the graph-section incidence under
  arbitrary completion and normalization kernels;
* a completion that deliberately reads and biases the particular fibre point.

The jump from atom bounds to any of these would be invalid. In particular,
amortizing many coupled constraints is not refuted merely because every
individual gcd is trivial.

**Audit verdict:** the corrected theorem above survives hostile review. The
\(N=91\) point is a certified auxiliary counterexample to a universal
twelve-unit guarantee, not evidence for an asymptotic lower bound. The
independent-output obstruction and the narrow dimension-span strengthening are
ready for a fresh proof-blind reconstruction; the nonlinear joint decoder must
be preserved verbatim as the live survivor.
