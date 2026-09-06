# F202 candidate: the factored square-gap child leaves a principal-genus orientation gate

## Status and scope

Candidate, proof-only, and not yet independently checked.  This theorem is
for balanced squarefree semiprimes.  It proves that recursively factoring the
canonical child

\[
E=N-\lfloor\sqrt N\rfloor^2
\]

is a valid one-child recursion.  It also proves exact boundaries for the
literal factor-supported congruence sieve, a second-principal-norm attack,
and the genus or ramified-form information canonically supplied by the
factorization of \(E\).

It is not a lower bound against arbitrary uses of `factor(E)`.  In
particular, it does not exclude nonlocal auxiliary moduli, a compressed
principal-genus algorithm, an integer-size statistic, or direct selection of
the P175 reciprocal prefix.  It is not a factoring algorithm.

Assume

\[
N=pq,
\qquad p<q<2p,
\qquad B=\lfloor\sqrt N\rfloor,
\qquad E=N-B^2,
\]

where \(p,q\) are distinct odd primes.  Let

\[
n=\lceil\log_2(N+1)\rceil.
\]

## Theorem 1: exact square-gap coordinates and valid recursion

Put

\[
a=B-p,
\qquad c=q-B,
\qquad d=c-a=p+q-2B.
\]

Then \(a\geq0\), \(c>0\), and \(d\) is a positive even integer.  Moreover,

\[
\boxed{E=Bd-ac,}
\]

\[
\boxed{a^2+E=pd,\qquad c^2+E=qd,}
\]

and

\[
\boxed{d^2+4Bd-4E=(q-p)^2.}
\]

The range is

\[
1\leq d\leq q-p<p,
\qquad
1\leq E\leq2B.
\]

Thus a correct \(d\) gives \(p,q\) by one square test and the quadratic
formula.

Also,

\[
\gcd(E,N)=\gcd(B^2,N).
\]

A nontrivial value is already a proper factor.  On the remaining branch,

\[
\gcd(E,N)=\gcd(B,N)=1.
\]

The integer \(E\) has at most \(n-1\) bits.  Consequently, if a uniform
numerical-QP postprocessor factors every promised \(N\) from \(N\) and the
complete prime factorization of \(E\), then recursive computation of that
factorization obeys

\[
T(n)\leq T(n-1)+Q(n).
\]

Iteration multiplies a nondecreasing numerical-QP bound by at most \(n\),
which is still numerical QP.  Hence the one-child recursion is valid; the
missing step is the postprocessor, not the recursion accounting.

## Theorem 2: mixed-root and norm interfaces

On the coprime branch, \(B\) is a unit modulo \(N\) and

\[
B^2\equiv-E\pmod N.
\]

There are four CRT roots of \(X^2\equiv-E\pmod N\).  The two public roots
are \(\pm B\).  If \(r\not\equiv\pm B\pmod N\) is either mixed root, then

\[
\boxed{
1<\gcd(r-B,N)<N,
\qquad
1<\gcd(r+B,N)<N.}
\]

The two gcds are \(p,q\), in some order.  Conversely, \(p,q\) construct a
mixed root by CRT.  Exact mixed-root construction is therefore
deterministically polynomial-time equivalent to factoring on this promise.

If

\[
N=x^2+Ey^2,
\]

then \(y\) is a unit modulo \(N\), and

\[
r=xy^{-1}\pmod N
\]

is a root of \(-E\).  The representation factors \(N\) exactly when this
root is mixed.  A second factor-bearing principal norm representation would
therefore be sufficient.  Such a representation need not exist.

## Theorem 3: the literal factor-supported residue test is path-blind

Let \(m\mid E\).  On the coprime branch, \(B\) is a unit modulo \(m\) and

\[
N\equiv B^2\pmod m.
\]

For every candidate unit \(x\in(\mathbb Z/m\mathbb Z)^\times\), put

\[
y=Nx^{-1},
\qquad
t_x=x+y,
\qquad
d_x=t_x-2B.
\]

Then

\[
t_x^2-4N=(x-y)^2\pmod m,
\]

and, using \(N\equiv B^2\pmod m\),

\[
d_x={ (x-B)^2\over x},
\qquad
d_x+4B={ (x+B)^2\over x}
\pmod m.
\]

Therefore

\[
\boxed{
d_x^2+4Bd_x-4E
=\left({x^2-B^2\over x}\right)^2\pmod m.}
\]

Thus product consistency plus a discriminant-square test modulo any modulus
supported on \(E\) accepts every unit candidate factor residue.  Combining
all prime-power factors of \(E\) does not orient \(p\) against \(q\), and it
does not select the P175 reciprocal path.

This is deliberately narrow.  A wheel in the \(d\)-coordinate can reject
some arbitrary residue classes, and a nonlocal modulus derived from more
than the support relation \(m\mid E\) is outside the claim.  No general
congruence-sieve lower bound is asserted.

## Theorem 4: the desired class is a square inside the principal genus

Let

\[
\mathcal O=\mathbb Z[\sqrt{-E}],
\qquad \operatorname{disc}(\mathcal O)=-4E,
\qquad
\alpha=B+\sqrt{-E}.
\]

On the coprime branch, the prime ideals over \(p,q\) selected by \(\alpha\)
are invertible and

\[
(\alpha)=\mathfrak p\mathfrak q.
\]

Writing \(C=[\mathfrak p]\) in the proper ideal class group gives

\[
[\mathfrak q]=C^{-1}.
\]

The ideal attached to one mixed root has class

\[
\boxed{C^2,}
\]

and the other has class \(C^{-2}\).  Hence every genus character takes the
value \(+1\) on the mixed-root class.  Genus labels cannot distinguish it
from the identity class.

The mixed root supplies a factor-bearing representation

\[
N=x^2+Ey^2
\]

if and only if \(C^2=1\).  The complete factorization of \(E\) does not
force this condition.  Canonical invertible ambiguous or ramified classes
built from discriminant factors have exponent at most two; their subgroup
need not contain the nontrivial square \(C^2\).

This is a boundary for the named genus and ramified-form mechanisms.  It is
not a lower bound against computing in the full proper class group.

## Theorem 5: explicit obstruction at \(N=2627\)

Take

\[
N=2627=37\cdot71,
\qquad B=51,
\qquad E=26=2\cdot13.
\]

Then \(37<71<2\cdot37\), and

\[
a=14,
\qquad c=20,
\qquad d=6.
\]

The mixed root

\[
r=162
\]

satisfies

\[
r^2+26=10N,
\qquad
\gcd(r-51,N)=37,
\qquad
\gcd(r+51,N)=71.
\]

Nevertheless, the only integer solutions of

\[
x^2+26y^2=2627
\]

are

\[
(x,y)=(\pm51,\pm1).
\]

Thus the public principal representation has no second factor-bearing
companion.

The mixed-root form is

\[
[2627,324,10]
\sim[3,-2,9]
\]

of discriminant \(-104\).  It is nonprincipal.  The ramified forms supplied
by \(2\) and \(13\) generate only

\[
\{[1,0,26],[2,0,13]\}.
\]

They do not reach \([3,-2,9]\).  Also \(d=6\) contains the prime \(3\),
which is absent from \(2E=52\).  Thus the identities in Theorem 1 do not
give a divisor or prime-support cover of \(d\) from `factor(E)`.

## Exact remaining gate

After the valid recursive factorization of \(E\), a successful
postprocessor must still do at least one of the following:

1. find the correct even \(d\) for which
   \(d^2+4Bd-4E\) is an integer square;
2. construct a mixed CRT root of \(-E\bmod N\);
3. select the P175 prefix \(p^{-1}\bmod2^t\) at quarter-minus-polylog
   precision; or
4. navigate the specific square \(C^2\) inside the principal genus by a
   QP method that does not merely compose the factor-supported ambiguous
   classes.

The first two are exact factoring primitives.  P175 makes the third a QP
factoring primitive, but a new prefix statistic could still be materially
different from exact root construction.  The fourth is an exact class-group
form of the same unresolved orientation problem.
