# F04 canonical-PSC kill test: the P14 witness separates

**Status:** candidate finite construction.  This is a surviving separator,
not a counterexample and not a uniform factoring theorem.

## Fixed convention and factor extraction

Let $R_N=(\mathbb Z/N\mathbb Z)[X]$, let

\[
P=X^r-1,\qquad Q=H_a=(X+a)^N-X^N-a\pmod P,
\]

and let $m=\deg P=r$ and $n=\deg Q$, where $n$ is read directly from
the globally computed polynomial over $\mathbb Z/N\mathbb Z$.  For
$0\le j\le n$, define $D_j(P,Q)$ as follows.  Take the coefficient
matrix of

\[
(U,V)\longmapsto UP+VQ,
\qquad \deg U<n-j,\quad \deg V<m-j,
\]

project its output to coefficient degrees
$j,j+1,\ldots,m+n-j-1$, order all row degrees increasingly, and order the
columns as the increasing shifts of $P$ followed by the increasing shifts
of $Q$.  This is a square matrix of dimension $m+n-2j$; $D_j$ is its
determinant.  It is the determinant-form principal subresultant coefficient
up to the harmless sign differences among standard Sylvester conventions.
The definition above fixes even that sign.

Every matrix entry is a coefficient of the globally computable $P,Q$, and
the determinant is a polynomial with integer coefficients in those entries.
Thus $D_j\bmod N$ is computable without field division and without knowing
a factor.  Berkowitz gives a division-free circuit over any commutative
ring.  If $D_j=0\pmod p$ and $D_j\ne0\pmod q$ for $N=pq$, then

\[
1<\gcd(D_j,N)<N.
\]

The local reduced polynomials $h_{q,a}(X^p)$ and $h_{p,a}(X^q)$ are used
only to analyze reductions.  Intermediate PSCs are **not** invariant under
the two different cyclic-algebra substitutions.  Consequently it would be
invalid to compute PSCs of the unsubstituted local $h$'s and claim that
they are reductions of one factor-free global coefficient.  The computation
here instead reduces the same globally formed $H_a$ into both fields.

## Exact smallest witness

For the promoted P14 parameters

\[
N=79{,}403=271\cdot293,\qquad r=269,
\]

the first standard shift $a=1$ gives

\[
\deg H_1=268\quad\text{over }\mathbb Z/N\mathbb Z,
\]

while its reductions have degrees 46 modulo 271 and 268 modulo 293.  Direct
construction of every defining determinant through index 47 gives no zero
mismatch for $0\le j\le46$, followed by

\[
D_{47}\equiv0\pmod{271},\qquad
D_{47}\equiv173\pmod{293}.
\]

The global, factor-free computation gives

\[
D_{47}\equiv30352\pmod{79403},\qquad
\gcd(30352,79403)=271.
\]

The defining matrix has dimension
$269+268-2\cdot47=443$.  Its determinant from the canonical integer lifts
has 3907 bits.  Since $a=1$ is the first standard shift and indices
0 through 46 were directly checked, $(a,j)=(1,47)$ is the lexicographically
smallest separator under this convention.

There is also a structural explanation for the zero modulo 271.  If a local
reduction of $Q$ has degree $d$, then for every $j>d$ the unshifted
$Q$-column in the defining matrix is zero: all retained row degrees are at
least $j>d$.  Hence $D_j=0$ in that field.  Here $d=46$, so $D_{47}$
vanishes modulo 271.  The residue 173 modulo 293 is the exact direct
determinant certificate.

## Uniform bit cost of the coefficient computation

Suppose $r$ and the number $A$ of tested shifts are polynomial in
$L=\lceil\log_2(N+1)\rceil$, as for the standard AKS parameter bounds.
Binary powering of $X+a$ in
$(\mathbb Z/N\mathbb Z)[X]/(X^r-1)$ uses $O(\log N)$ cyclic polynomial
multiplications; even schoolbook multiplication uses
$O(r^2\log N)$ ring operations per shift, and reduction keeps every scalar
at $O(L)$ bits.  There are at most $r$ matrices, each of dimension at
most $2r$.  Computing each determinant by Berkowitz uses a polynomial
number of ring operations (conservatively $O(r^4)$ per determinant), so
forming and scanning all $D_j$ for all $A$ shifts has polynomial bit
cost.  Each final integer gcd is polynomial-time as well.  This proves only
that the proposed coefficients are uniformly and factor-free computable;
it does not prove that a separator exists on every input or with any stated
probability.

## Scope

This finite witness does **not** kill the PSC refinement.  It shows that the
P14 full-rank witness is insufficient as a counterexample: a canonical PSC
already splits it at the first shift.  In fact the same local degree drop
makes the ordinary leading coefficient split too:

\[
[X^{268}]H_1\equiv31978\pmod{79403},\qquad
\gcd(31978,79403)=271.
\]

Thus this example supplies no evidence that PSCs outperform the earlier
individual-coefficient scan.  It also says nothing about arbitrary
(exponentially many) Sylvester minors, pivot-dependent elimination
transcripts, nonstandard moduli, or a uniform inverse-polynomial separation
bound.  A materially stronger kill witness would have to defeat the
individual coefficients as well as the full-rank and canonical-PSC scans.

All exact commands, timeouts, failed attempts, logs, and outputs are in
`RUN_MANIFEST.md`; R05 is the factor-free witness and R06 is the direct
local-prefix certificate.
