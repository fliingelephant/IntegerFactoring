# F200 V2 statement-only blind reconstruction

## Input discipline and verdict

Before reading the statement, I obtained

```text
1edaedf1e0121e4603b8502cfb2473de250366cdc4b35acb216c3be314c8b7e5  V2_STATEMENT.md
```

which equals the expected frozen hash. I then read only `PROMPT.md` and
that frozen statement. I did not inspect a proof, audit, provenance file,
manifest, V1 file, message about F200, or durable ledger.

**Verdict: PASS.** All algebraic claims reconstruct. The uses of P173 and
P160--P161 are valid from the precise imported interfaces stated in V2.
The Fourier-density sentence uses nonzero cyclic shifts; the zero shift is
the identically zero difference. The displayed autocorrelation uses the
unnormalized cyclic convention. With the normalized convention it acquires
the harmless factor (1/M).

## 1. Location of the exceptional denominator

The promise gives

\[
p<\sqrt N<q,
\qquad p\le B<q.
\tag{1}
\]

Moreover, (q<2p) gives (N<2p^2), hence

\[
B<\sqrt2p<2p.
\tag{2}
\]

The adjacent-binomial identity is

\[
j\binom{N-1}{j}=(N-j)\binom{N-1}{j-1}.
\]

After inserting the alternating signs, this becomes

\[
jA_j=-(N-j)A_{j-1}.
\]

Therefore

\[
j(A_j-A_{j-1})=-NA_{j-1}
\tag{3}
\]

and

\[
x_j={A_{j-1}\over j}={A_{j-1}-A_j\over N}.
\tag{4}
\]

It remains to determine the last quotient modulo one. I reconstruct the
needed congruence without importing it.

For (0\le k<q), reduction modulo (q) is allowed in every denominator
of

\[
A_k=\prod_{r=1}^k{r-N\over r}.
\]

Thus

\[
A_k\equiv1\pmod q
\qquad(0\le k\le B).
\tag{5}
\]

The same argument modulo (p) gives

\[
A_k\equiv1\pmod p
\qquad(0\le k<p).
\tag{6}
\]

For the remaining indices, write

\[
q=p+d,
\qquad 1\le d<p,
\qquad k=p+r,
\qquad0\le r<p.
\]

In base (p),

\[
N-1=p^2+(d-1)p+(p-1).
\]

The Frobenius identity in \(\mathbb F_p[X]\) gives the special Lucas
coefficient directly:

\[
\begin{aligned}
(1+X)^{N-1}
&\equiv
(1+X^{p^2})(1+X^p)^{d-1}(1+X)^{p-1}\pmod p,\\
\binom{N-1}{p+r}
&\equiv(d-1)\binom{p-1}{r}
\equiv(d-1)(-1)^r\pmod p.
\end{aligned}
\tag{7}
\]

Because (p) is odd,

\[
(-1)^{p+r}=-(-1)^r.
\]

Consequently

\[
A_{p+r}\equiv1-d\equiv1-q\pmod p.
\tag{8}
\]

Equations (5) and (8) agree with (1-q) modulo both (p) and (q).
The Chinese remainder theorem yields

\[
A_k\equiv
\begin{cases}
1\pmod N,&0\le k<p,\\
1-q\pmod N,&p\le k\le B.
\end{cases}
\tag{9}
\]

For (j\ne p), the two adjacent values in (9) are equal modulo (N).
Equation (4) then shows that (x_j\) is an integer. At the transition,

\[
A_{p-1}-A_p\equiv q\pmod N,
\]

so

\[
x_p={A_{p-1}-A_p\over N}\in\mathbb Z+{q\over N}
=\mathbb Z+{1\over p}.
\tag{10}
\]

This proves, with the positive sign,

\[
\bar x_j={1\over p}\mathbf1_{j=p}
\quad\text{in }\mathbb Q/\mathbb Z.
\tag{11}
\]

The quotient is used only additively. No multiplication in
\(\mathbb Q/\mathbb Z\) is required.

## 2. Subset tests and telescoping

For a subset (I\), equation (4) gives

\[
D_I=NS_I=\sum_{j\in I}(A_{j-1}-A_j)\in\mathbb Z.
\tag{12}
\]

If (p\notin I\), equation (11) says (S_I\in\mathbb Z\). Hence

\[
D_I\equiv0\pmod N,
\qquad \gcd(D_I,N)=N.
\tag{13}
\]

If (p\in I\), then (S_I=m+1/p\) for some (m\in\mathbb Z\). Thus

\[
D_I=Nm+q\equiv q\pmod N,
\qquad \gcd(D_I,N)=q.
\tag{14}
\]

The product test has the complementary factor. By (1), no index at most
(B\) is divisible by (q\). By (2), the only index at most (B\) divisible
by (p\) is (p\) itself. Since (N\) is squarefree,

\[
\gcd\!\left(N,\prod_{j\in I}j\right)
=\begin{cases}
1,&p\notin I,\\
p,&p\in I.
\end{cases}
\tag{15}
\]

Thus all four named tests detect the same membership event. For an interval,
equation (4) telescopes without any congruence:

\[
S_{[a,b]}
={1\over N}\sum_{j=a}^b(A_{j-1}-A_j)
={A_{a-1}-A_b\over N}.
\tag{16}
\]

This reconstructs Theorem 1.

## 3. The sign of the Archimedean floor

Since (A_0=1\), equation (16) over the root interval gives

\[
\sum_{j=1}^B x_j={1-A_B\over N}.
\tag{17}
\]

Writing (A=A_B\) and using

\[
h={A-1+q\over N}
\]

gives

\[
{1-A\over N}={q\over N}-h={1\over p}-h.
\tag{18}
\]

Here (h\) is an integer and (0<1/p<1\). Therefore

\[
\left\lfloor\sum_{j=1}^B x_j\right\rfloor=-h,
\qquad
h=-\left\lfloor\sum_{j=1}^B{A_{j-1}\over j}\right\rfloor.
\tag{19}
\]

The same argument applied to (11) gives

\[
p\in I\Longrightarrow
S_I=\lfloor S_I\rfloor+{1\over p}.
\tag{20}
\]

Since (p\) is odd, (1/p\) lies in \(\mathbb Z_2\), and its reduction
modulo (2^t\) is exactly (p^{-1}\bmod2^t\). An evaluation in
\(\mathbb Z_2\) retains the sum of the integer part and this unit. It does
not recover the Archimedean floor. This proves Theorem 2.

## 4. Walsh, Fourier, Haar, and differences

Let

\[
a={1\over p}+\mathbb Z\in\mathbb Q/\mathbb Z.
\]

After zero padding, equation (11) is the additive delta

\[
f(j)=a\,\mathbf1_{j=p}
\qquad(1\le j\le M).
\tag{21}
\]

### Walsh transform

For every Walsh character \(\chi\),

\[
\widehat f(\chi)=\sum_j\chi(j)f(j)=\chi(p)a\in\{a,-a\}.
\tag{22}
\]

The element (a\) is nonzero because (1/p\notin\mathbb Z\). Therefore
every Walsh coefficient is nonzero.

### Fourier transform

Let \(K=\mathbb Q(\zeta_M)\). With the negative-exponent convention,

\[
\widehat f(s)={\zeta_M^{-sp}\over p}+\mathcal O_K.
\tag{23}
\]

Changing the convention changes only the sign of the exponent. This class
is nonzero. Indeed, \(\zeta_M\) is a unit of \(\mathcal O_K\), and
\(\zeta_M^{-sp}/p\in\mathcal O_K\) would imply (1/p\in\mathcal O_K\).
But a rational algebraic integer is an integer. Thus the Fourier support is
full in the additive quotient (K/\mathcal O_K\).

### Haar transform

Use the unnormalized Haar coefficient at an internal node: the sum over
its left child minus the sum over its right child. At each depth, exactly
one node contains (p\). Its coefficient is (+a\) or (-a\), according to
which child contains (p\). Every other node has coefficient zero. Hence
there is exactly one nonzero wavelet at every scale, and these nodes are the
unique root-to-leaf path ending at (p\). The root scaling coefficient is
also (a\), but it is not a wavelet coefficient.

### Cyclic differences

For a rational lift (g(j)=p^{-1}\mathbf1_{j=p}\), define, for example,

\[
(\Delta_hg)(j)=g(j+h)-g(j).
\]

The cyclic Fourier transform gives

\[
\widehat{\Delta_{h_1}\cdots\Delta_{h_r}g}(s)
={\zeta_M^{-sp}\over p}
\prod_{i=1}^r(\zeta_M^{s h_i}-1),
\tag{24}
\]

up to the two simultaneous sign conventions. If (M\) is dyadic and (h)
is odd, then

\[
\zeta_M^{sh}=1
\Longleftrightarrow M\mid sh
\Longleftrightarrow M\mid s.
\tag{25}
\]

Thus one odd difference removes only frequency zero. More generally, for
nonzero shifts modulo (M=2^r\), the zero sets of the multipliers are
nested dyadic subgroups. Their union has at most (M/2\) elements, so an
iterated nontrivial difference still has at least (M/2\) nonzero
frequencies. A shift congruent to zero is the trivial zero operator and is
not a sparsification mechanism.

For the unnormalized cyclic autocorrelation,

\[
R(h)=\sum_{j\bmod M}g(j)g(j+h)
={1\over p^2}\mathbf1_{h=0}.
\tag{26}
\]

It has lost the location (p\). If “average” includes division by (M\),
the right side is divided by (M\); the location-independence is unchanged.

### Reciprocal-prefix cells

Inversion permutes the odd residue classes modulo (2^t\). The only
nonzero entry of (21) belongs to the cell with label

\[
a=p^{-1}\pmod{2^t}.
\]

Hence the vector of cell sums is itself a delta. Under any bijective Boolean
labelling of the odd residue classes, every Walsh coefficient is again
(\pm1/p\), and the support is full. The inverse image of label (a\) is
exactly

\[
j\equiv a^{-1}\pmod{2^t}.
\tag{27}
\]

This completes Theorem 3.

## 5. The additive tree gauge

Equations (10)--(11) show that every (x_j\) belongs to
\(\mathbb Z[1/p]\subset\mathbb Z_2\). Thus every node sum has a
well-defined residue modulo (2^t\), even though the unreduced presentation
(A_{j-1}/j\) can display an even denominator before cancellation.

If (v=v_0\sqcup v_1\), then

\[
s_v=s_{v_0}+s_{v_1}\pmod{2^t}.
\tag{28}
\]

Fix an arbitrary proposed leaf \(\ell\) and residue (u\). Exactly one child
of a node containing \(ell\) contains \(ell\), while neither child of a
node not containing it does. Therefore

\[
\begin{aligned}
c_{v_0}^{(\ell,u)}+c_{v_1}^{(\ell,u)}
&=s_{v_0}+s_{v_1}
-u\bigl(\mathbf1_{\ell\in v_0}+\mathbf1_{\ell\in v_1}\bigr)\\
&=s_v-u\mathbf1_{\ell\in v}
=c_v^{(\ell,u)}\pmod{2^t}.
\end{aligned}
\tag{29}
\]

This identity holds for every proposal, not only the true one. Each residue
has an integer lift. In fact, one may lift the leaf residues arbitrarily and
define every parent lift as the sum of its child lifts, so even exact
additivity of some integer representatives supplies no selector.

For the true proposal, write

\[
S_v=\sum_{j\in v}x_j.
\]

If (p\notin v\), then (S_v\) is an integer. If (p\in v\), then

\[
S_v=\lfloor S_v\rfloor+{1\over p}.
\]

It follows that

\[
c_v^{(p,p^{-1})}\equiv\lfloor S_v\rfloor\pmod{2^t}.
\tag{30}
\]

These true floor lifts add exactly because at most one child contains (p\).
Their special status is Archimedean, not a consequence of the finite
additive equations.

For the reciprocal-prefix tree, each of the two lifts at the next precision
corresponds, after inversion, to one odd residue class modulo (2^{t+1}\).
The least positive representative of every such class is below (2^{t+1}\).
In the P175 sub-quarter range,

\[
2^{t+1}=O(N^{1/4}2^{-(\log n)^{O(1)}})=o(B).
\tag{31}
\]

Even without using the displayed deficit, (2^{t+1}=O(N^{1/4})=o(B)\).
Thus both child classes contain an index at most (B\) for all sufficiently
large inputs. Equation (29) gives the same additive feasibility to both.

Haar and Walsh transforms are invertible linear changes of the same node or
leaf data. They preserve this family of gauge-equivalent corrections. A
selector must use information outside finite linear additivity. This proves
Theorem 4 with its stated scope.

## 6. Endpoint evaluation and run accounting

Multiplying (4) by integer weights and summing gives

\[
N\sum_{j=1}^B w_jx_j
=\sum_{j=1}^B w_j(A_{j-1}-A_j).
\]

Collecting each (A_j\) yields

\[
N\sum_{j=1}^B w_jx_j
=w_1A_0
+\sum_{j=1}^{B-1}(w_{j+1}-w_j)A_j
-w_BA_B.
\tag{32}
\]

If exactly (R\) adjacent differences are nonzero, at most those (R\)
interior values and the two endpoints occur. This proves the (R+2\)
bound. The P173 interface stated in V2 evaluates each requested (A_j\)
modulo (2^t\) in polynomial time by running its power-of-two routine at
the full index-covering precision and then reducing. A QP number of calls,
together with arithmetic on QP-size public weights, remains QP. Multiplying
equation (32) by (N^{-1}\bmod2^t\) returns the finite node sum. It does not
return its ordinary floor.

An interval indicator has two boundary changes. An unnormalized Haar
wavelet has only the support boundaries and its midpoint sign change, so it
also has (O(1)) changes. But an exact support test asks whether its support
contains (p\). Equations (13)--(15) show that this is precisely the
factor-bearing event.

Let (m=2^t\). A fixed odd residue class modulo (m\), restricted to
\([1,B]\), contains

\[
{B\over m}+O(1)
\tag{33}
\]

indices. Since consecutive selected indices differ by (m\), these are
isolated runs. In the P175 range, write the fixed deficit as (L(n)). The
floor in (t\) changes powers of two by only a constant factor, so

\[
2^t=\Theta\!\left({N^{1/4}\over2^{L(n)}}\right),
\qquad
{B\over2^t}
=\Theta\!\left(N^{1/4}2^{L(n)}\right)
=N^{1/4}2^{(\log n)^{O(1)}}.
\tag{34}
\]

This is exponential in the input length because
(N^{1/4}=2^{\Theta(n)}\), whereas (2^{L(n)}\) is only numerical QP.
Literal endpoint materialization therefore has exponentially many runs.

Conditioned on sampling uniformly from the unique correct cell, only (p\)
is exceptional. Its hit probability is

\[
\left({B\over2^t}+O(1)\right)^{-1}
=\Theta\!\left({2^t\over B}\right)
=N^{-1/4}2^{-(\log n)^{O(1)}}.
\tag{35}
\]

Sampling a wrong cell has probability zero. These facts establish exactly
the named evaluator and sampler accounting, without a circuit lower bound.
This proves Theorem 5.

## 7. Factor-free finite residue rings

Let (M\) be public. If (1<\gcd(M,N)<N\), that gcd is already a factor.
On the branch \(\gcd(M,N)=1\), the image of (N\) is a unit, so the
universal property of localization gives

\[
\mathbb Z[1/N]\longrightarrow\mathbb Z/M\mathbb Z.
\tag{36}
\]

Since (1/p=q/N\), its image is (qN^{-1}\), which equals (p^{-1}\)
modulo (M\). The map from ordinary integers onto
\(\mathbb Z/M\mathbb Z\) is surjective. Hence every possible image of
(m+1/p\) is also the image of an ordinary integer. No predicate whose
entire input is this one residue can accept all integer values and reject
all values in \(\mathbb Z+1/p\).

For finitely many factor-free moduli, take their least common multiple
(L\). It is still coprime to (N\), and (p^{-1}\bmod L\) maps to the
compatible tuple of inverses in every component. Thus the same integer
imitates the entire residue tuple. Pairwise coprimality of the auxiliary
moduli is not required.

If (N\mid M\), then (N\) is not a unit and (36) does not exist. The
statement correctly excludes this composite-characteristic case.

The special finite 2-adic assertion follows either from this argument or
directly from the surjectivity

\[
\mathbb Z\twoheadrightarrow\mathbb Z/2^t\mathbb Z.
\]

For the infinite assertion, \(\mathbb Z\) is dense in \(\mathbb Z_2\).
If a continuous map (F:\mathbb Z_2\to Y\) into a Hausdorff space is
constant with value (c\) on \(\mathbb Z\), then for every
(z\in\mathbb Z_2\), a sequence of integers converging to (z\) gives
(F(z)=c\). Thus continuous value-local tests, including convergent Mahler
expansions and finite-precision characters, cannot realize the missing
integrality predicate. This says nothing about an algorithm that also reads
the rational presentation or applies an Archimedean operation.

## 8. Ordinary phases

From the subset dichotomy,

\[
e^{2\pi i mS_I}
=\begin{cases}
1,&p\notin I,\\
e^{2\pi i m/p},&p\in I.
\end{cases}
\tag{37}
\]

The elementary inequality \(|e^{iy}-1|\le|y|\) gives

\[
|e^{2\pi i m/p}-1|\le{2\pi|m|\over p}.
\tag{38}
\]

Balance implies (p>\sqrt{N/2}\). Also the input-length convention gives
(N\ge2^{n-1}\). Therefore

\[
\log_2p\ge{n-2\over2}.
\]

For every fixed numerical-QP (Q\),

\[
\log_2 Q(n)=O((\log n)^k)=o(n).
\]

Equations (38) and the last two bounds prove

\[
|e^{2\pi i m/p}-1|\le 2^{-\Omega(n)}
\qquad(|m|\le Q(n)).
\tag{39}
\]

Thus bounded-frequency smooth tests do not obtain inverse-QP separation.

If (m\) is uniform modulo (N=pq\), then (m\bmod p\) is uniform. A fixed
positive proportion of the (p)-th roots of unity have distance at least,
for example, one from (1\). Hence the random high-order phase has constant
separation with constant probability.

Equation (12) also gives

\[
e^{2\pi i mS_I}=e^{2\pi i mD_I/N}.
\tag{40}
\]

If \(\gcd(m,N)=1\), then in the active case this is
(e^{2\pi i m/p}\ne1\); in the inactive case it is one. Exact equality to
one is therefore equivalent to the support event. An exact phase evaluator
on dyadic intervals permits binary search for the unique index (p\) in
(O(\log B)=O(n)\) queries. Exact division then verifies the factor. This
establishes the phase boundary without assuming that such an evaluator
exists.

## 9. Conditional local cyclotomic degree

I use only the conditional P160--P161 interface stated in V2. On its named
surviving branch,

\[
\operatorname{ord}_p(w)>T,
\qquad T\ge D(n),
\tag{41}
\]

and (w\) is a power of two. Write (w=2^e\) in
\((\mathbb Z/p\mathbb Z)^\times\). In any finite group, the order of a
power divides the order of its base, so

\[
\operatorname{ord}_p(w)\mid\operatorname{ord}_p(2).
\]

Consequently

\[
\operatorname{ord}_p(2)>T\ge D(n).
\tag{42}
\]

Now let (K/\mathbb Q_2\) be a finite extension containing a primitive
(p)-th root of unity. Let its residue degree and ramification degree be
(f) and (e_K\). A root of unity of odd order reduces injectively into the
residue-field multiplicative group: the principal-unit group has no odd
torsion. The residue field has order (2^f\), hence

\[
p\mid 2^f-1,
\qquad
\operatorname{ord}_p(2)\mid f.
\tag{43}
\]

It follows that

\[
[K:\mathbb Q_2]=e_Kf\ge f\ge\operatorname{ord}_p(2)>D(n).
\tag{44}
\]

For \(\gcd(m,N)=1\), the active phase is a primitive (p)-th root, so no
extension of degree at most (D(n)\) contains it on this branch.

This implication uses neither earlier exit: a factor and a factored exact
common-order state remain separate outcomes. It also makes no statement
about complex approximations or implicit representations. Thus the repaired
cyclotomic claim is exactly conditional and reconstructs as stated.

## 10. Scope conclusion

The proofs establish the named boundary only. Linear transforms preserve
the delta or the tree gauge. Finite factor-free residues cannot recognize
the missing Archimedean integrality. Literal residue-cell endpoints and
uniform sampling have exponential cost. Bounded ordinary frequencies have
exponentially small separation, while exact high-order phase evaluation is
already a factoring interface.

None of these arguments excludes a QP nonlinear statistic of the specific
integer parts, a QP implicit high-order phase evaluator, a nonlocal
arithmetic circuit, or another factoring method. The exact remaining
opening in V2 is therefore preserved.
