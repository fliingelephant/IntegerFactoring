# Corrected proof-blind reconstruction result

## Verdict: PASS

All six claims follow from exact square-class accounting, with the following
scope made explicit.

- The proper-factor statement uses the usual factoring domain: $N$ is an
  odd positive integer greater than $1$.
- A canonical endpoint is the unique chosen integer representative of its
  residue class. Thus equal residue classes have equal canonical endpoints.
- A non-global square root of one is a unit $g$ with
  $g^2\equiv1\pmod N$ but $g\not\equiv 1,-1\pmod N$.
- A square dependency is an indexed exponent-parity vector. Arbitrary integer
  multiplicities reduce to such a vector after even multiplicities are
  removed.

The square-class and rank arguments themselves do not use that $N$ is odd.
Oddness is relevant to the stated direct gcd screens. Coprimality with $N$
puts the relation values in the modular unit group, but it is not needed for
the rational square-class lemma.

## 1. The refined rows are independent square classes

Let $Q_1,\ldots,Q_r$ be positive, pairwise-coprime, nonsquare blocks. Their
classes in

\[
\mathbb Q_{>0}^{\times}/(\mathbb Q^{\times})^2
\]

are linearly independent over $\mathbb F_2$. Indeed, suppose that for a
subset $S$,

\[
\prod_{j\in S}Q_j
\]

is a rational square. A rational number whose square is an integer is an
integer, so every prime valuation of this product is even. Fix
$j\in S$. Because $Q_j$ is nonsquare, some prime has odd valuation in
$Q_j$. Pairwise coprimality means that this prime occurs in no other
$Q_k$. Its valuation in the displayed product is therefore odd, a
contradiction. Hence $S$ is empty.

This proof does not require a block to be prime or squarefree. It applies to
composite blocks and to nonsquare prime powers.

Write the exact refined decompositions in the form

\[
B_i=S_i^2\prod_{j=1}^r Q_j^{a_{ji}},
\]

where factors already known to be squares can be absorbed into the exact
square part. The parity matrix has entries
$M_{ji}=a_{ji}\bmod 2$. For $x\in\mathbb F_2^m$, the selected indexed
product is a square exactly when

\[
\prod_i B_i^{x_i}
\]

has even exponent on every $Q_j$. By the independence lemma, this is
equivalent to $Mx=0$. Thus

\[
\ker M
=
\{x\in\mathbb F_2^m:\prod_i B_i^{x_i}\text{ is an exact square}\}.
\]

Perfect-square blocks contribute the zero square class, so omitting their
rows does not change this kernel. Their exact exponent data is still needed
to construct the integer square root.

## 2. Exact refinement preserves the old kernel

Define the intrinsic map

\[
\Phi:\mathbb F_2^m\longrightarrow
\mathbb Q_{>0}^{\times}/(\mathbb Q^{\times})^2,
\qquad e_i\longmapsto[B_i].
\]

Both the matrix before refinement and the matrix after refinement are exact
coordinate representations of this same map. Splitting a block changes its
coordinates. It does not change any $B_i$ or its rational square class.
Consequently both matrices have kernel $\ker\Phi$. In particular, a later
split caused by a new relation cannot create or destroy a dependency among
the old indexed values.

## 3. The one-column rank rule

After refining old and new values together, compare $M$ and
$[M\ b]$. There are exactly two cases.

If $b\in\operatorname{colspan}(M)$, then

\[
\operatorname{rank}[M\ b]=\operatorname{rank}M.
\]

The column count increases by one, so rank-nullity shows that nullity
increases by one. If $b\notin\operatorname{colspan}(M)$, rank and column
count both increase by one, so nullity is unchanged.

Now let a row be zero on all old columns and one in $b$. Every vector in
the old column span is zero on that row. Hence $b$ is not in the old span,
and the append creates no immediate new dependency.

This is a parity statement. The corresponding integer block can occur in an
old value with a positive even exponent while its old matrix entry remains
zero.

## 4. The arithmetic witness, and why it is not necessary

For a fully refined block $Q$, let $v_Q(X)$ denote its exact block
multiplicity in $X$. If

\[
v_Q(gw)=v_Q(g)+v_Q(w)
\]

is odd, the $Q$-entry of $b$ is one. If every old $v_Q(B_i)$ is even,
the old parity row is zero. This is precisely the new-only row from the
previous section, so it proves $b\notin\operatorname{colspan}(M)$.

The phrase “total multiplicity in $gw$” is essential. An odd occurrence in
$w$ alone is not a witness if $g$ supplies another odd occurrence and
cancels it in square class.

In the “component of $w$” formulation, read component in the final exact
refinement. A nonsquare component coprime to every old block has a zero old
row. If its total multiplicity in $gw$ is odd, it has a one in $b$. More
generally, if “component” denotes an aggregate of final blocks with nonzero
total square class in $gw$, at least one constituent nonsquare block has
odd total multiplicity and supplies the required row.

The witness is not necessary for independence. For an explicit feedback-form
example, take $N=21$, old value $B_1=110$, and inverse endpoints
$g=2,w=11$, so the appended value is $B_2=gw=22\equiv1\pmod{21}$.
The joint exact refinement has coprime nonsquare blocks $22$ and $5$, with

\[
M=\begin{pmatrix}1\\1\end{pmatrix},
\qquad
b=\begin{pmatrix}1\\0\end{pmatrix}.
\]

There is no new-only row on which $b$ is one: the $22$-row is already one
on the old column. Nevertheless $b$ is not in the span of the sole old
column. Thus the append is independent without the sufficient witness.

## 5. A canonical self-inverse endpoint

Let $w$ be the canonical representative of the inverse residue of $g$.
If $g^{-1}\equiv g\pmod N$, that inverse residue is the residue already
represented canonically by $g$. Uniqueness of the canonical representative
therefore gives $w=g$ as integers. The new exact relation value is $g^2$,
so its square-class column is zero. Hence

\[
\ker[M\ 0]=\ker M\times\mathbb F_2.
\]

Nullity increases by exactly one, and the new independent direction can be
taken to be the singleton vector selecting only the new indexed column.

For the direct screens, put

\[
d_- = \gcd(g-1,N),\qquad d_+ = \gcd(g+1,N).
\]

Because $g$ is a unit and is self-inverse,
$g^2\equiv1\pmod N$. Also

\[
\gcd(g-1,g+1)\mid 2.
\]

Since $N$ is odd, no prime dividing $N$ divides both $g-1$ and
$g+1$. Every full prime-power divisor of $N$ must divide one of them,
because $N\mid(g-1)(g+1)$. Therefore

\[
\gcd(d_-,d_+)=1,
\qquad d_-d_+=N.
\]

If $g\not\equiv\pm1\pmod N$, neither gcd equals $N$. Their product is
$N>1$, so both lie strictly between $1$ and $N$: both are proper
nontrivial factors. Conversely, if both screens are proper, then neither
congruence $g\equiv1\pmod N$ nor $g\equiv-1\pmod N$ can hold. Thus the
two screens are proper exactly for a non-global square root of one.

Running these gcd screens before dependency decoding is sound: in the
non-global case they already return factors. This ordering statement does not
claim that every decoded exact square dependency returns a nontrivial factor.

## 6. A finite sequence of additions

At time $t$, let $n_t$ be the number of indexed columns and $r_t$ their
square-class rank. Then

\[
d_t=n_t-r_t=\dim\ker M_t.
\]

Exact refinement leaves the intrinsic kernel unchanged, so it leaves $d_t$
unchanged. At an append, the column count rises by one. The rank rises by one
when the new column is outside the current span and rises by zero when it is
inside. Thus $d_t$ respectively stays fixed or rises by one.

If every appended column has a new-only nonsquare row with entry one at its
insertion time, every append is outside the then-current span. Induction over
any finite prefix gives

\[
d_t=d_0.
\]

This preserves initial nullity; it does not assert absolute independence
unless the initial family was independent. If $d_0>0$, those old
dependencies remain. If $d_0=0$, every finite prefix has zero kernel.

A row that is private at one insertion need not stay private. For example,
starting with square classes $[P]$, then appending $[Q]$, makes $Q$ a
private row at that time. A later column $[PQ]=[P]+[Q]$ reuses it and closes
a dependency. This does not contradict the finite-prefix criterion, because
that later column has no private new-only row.

## Indexed and deduplicated semantics

The domain of the square-class map has one basis vector per appended index.
If two equal relation values are both appended, their columns are equal and
the sum of their two index vectors is a dependency; their selected exact
product is the square $B^2$. If the second value is deduplicated before
append, there is no second basis vector and no nullity change. Likewise, an
appended exact square has a zero column and adds a singleton dependency.

These statements count every exact subset-square relation, including ones
that produce only a global modular root and hence no factor. For example, a
self-inverse square $g^2$ with $g\equiv\pm1\pmod N$ still adds its exact
singleton dependency, although its gcd screens are trivial.

The blocks are only coordinates for rational square classes. They can be
composite, can be prime powers, and can split under later exact refinement.
Nothing here gives a smoothness distribution or a fixed prime factor base.
The result is exact linear accounting only. It makes no probability,
selection, runtime, or guaranteed-factoring claim.

## Finite checks

For $N=21$, jointly refine

\[
22=2\cdot11,\qquad 85=5\cdot17,\qquad 190=2\cdot5\cdot19.
\]

In row order $2,11,5,17,19$, the three columns are

\[
\begin{pmatrix}1\\1\\0\\0\\0\end{pmatrix},\quad
\begin{pmatrix}0\\0\\1\\1\\0\end{pmatrix},\quad
\begin{pmatrix}1\\0\\1\\0\\1\end{pmatrix}.
\]

In any linear combination equal to zero, the $19$-row first forces the
third coefficient to zero; then the $11$- and $17$-rows force the first
and second coefficients to zero. The columns are independent. Separately,
$\gcd(10-1,21)=\gcd(9,21)=3$, so the direct screen already factors $21$.

For $N=55$, use rows $2,7,3,37$. The old columns for
$56=2^3\cdot7$ and $111=3\cdot37$ are

\[
\begin{pmatrix}1\\1\\0\\0\end{pmatrix},\qquad
\begin{pmatrix}0\\0\\1\\1\end{pmatrix},
\]

and are independent. Since

\[
21^2=441=3^2\cdot7^2=1+8\cdot55,
\]

its appended parity column is zero. It adds one singleton dependency. The
two screens give

\[
\gcd(21-1,55)=5,\qquad \gcd(21+1,55)=11.
\]

Both finite checks therefore agree with the general claims.
