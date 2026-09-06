# Hostile audit of F177 squared common-order terminal screen

## Verdict

**REPAIR REQUIRED before promotion.**

The ordinary theorem is correct as frozen.  The torus algebra, balanced gap
bound, one-orientation candidate count, recovery test, and QP bit-cost claim
are also correct.

The defect is an input-interface gap.  The scan in (12) needs the sign
\(\epsilon\).  A standard F170 Jacobi-minus-one torus state does not reveal
which hidden prime has which split/nonsplit orientation.  The frozen text
neither declares \(\epsilon\) to be an extra public input nor tells the scan
to enumerate both signs, yet Section 3 says that no hidden orientation is
used.  Thus the exact one-list algorithm and count (15) are not established
from the F170 public state.

This is a narrow repair, not a refutation of the QP terminal idea.  Either:

1. explicitly supply the correct orientation bit as an additional public
   promise, in which case (12), (15), and (16) hold exactly as written; or
2. enumerate both signs.  Then the total count is at most

   \[
   2+\frac{\sqrt{2N}}{B^2}.
   \]

   Condition (16) still gives a QP scan, because this is at most
   \(2Q(n)+2\).  Only the exact one-list count and constant-size accounting
   must change.

The frozen inputs have the required SHA-256 hashes:

- `STATEMENT.md`:
  `bc1ec03dd8f9ac47e90d7e0108f3188d9639f0bb4f3f36074be047ba37da4944`;
- `PROOF.md`:
  `82ec538a073e22566eb6e7429f03193b86fac119e24a551d144df89a33c73a09`.

I read both frozen files in full.  I also checked the promoted P156/F170
input and terminal interface.

## 1. Ordinary square-modulus identity

An ordinary element of exact common order \(M\) satisfies

\[
M\mid p-1,\qquad M\mid q-1.
\]

Writing \(p=1+aM\) and \(q=1+bM\) gives

\[
N+1-(p+q)=(p-1)(q-1)=abM^2.
\]

Hence

\[
p+q\equiv N+1\pmod{M^2}.
\]

No coprimality between \(a,b,M\) is needed.  Exactness is stronger than the
identity needs; a certified common divisor of both local group orders would
already suffice.

## 2. Balanced sum interval and candidate count

Put \(x=q/p\).  Under \(1<x<2\),

\[
\frac{p+q}{\sqrt N}=\sqrt{x}+\frac1{\sqrt{x}}.
\]

Its derivative is \((x-1)/(2x^{3/2})>0\).  The endpoint values are \(2\)
and \(3/\sqrt2\), so the strict interval (4) is exact.  Its length is

\[
c_0\sqrt N,\qquad c_0=\frac3{\sqrt2}-2.
\]

One residue class modulo \(M^2\) has at most

\[
1+\frac{c_0\sqrt N}{M^2}
\]

members in this interval.  Therefore (8) and the sufficient condition (9)
are correct.  The irrational endpoints cause no implementation problem:
for a positive integer \(S\), the two strict tests are exactly
\(S^2>4N\) and \(2S^2<9N\).

For the true sum,

\[
S^2-4N=(q-p)^2.
\]

The square and parity tests make the two roots integral.  Direct
multiplication or trial division verifies them, so a false candidate cannot
corrupt the output.

## 3. Torus square-modulus identity and gap bound

For one fixed orientation, the assumed divisibilities give

\[
B^2\mid(p-\epsilon)(q+\epsilon).
\]

Since \(D=q-p\),

\[
(p-\epsilon)(q+\epsilon)=N-1-\epsilon D.
\]

Thus

\[
D\equiv\epsilon(N-1)\pmod{B^2}.
\]

All signs in (11)--(12) are correct.  Also

\[
\frac{D}{\sqrt N}=\frac{x-1}{\sqrt x},
\]

whose derivative is \((x+1)/(2x^{3/2})>0\).  Its upper endpoint at \(x=2\)
is \(1/\sqrt2\).  This proves (13).  For a fixed known \(\epsilon\), the
count (15) follows by the same one-residue-class argument.

For every candidate \(D\), testing whether \(D^2+4N\) is a square recovers
the candidate sum \(S\).  The parity test and direct multiplication then
give a sound verifier.  The true gap is present.

## 4. Orientation attack against the F170 interface

F170 supplies a public Jacobi-minus-one discriminant and a public torus
point of exact common order.  It defines

\[
\epsilon=\left(\frac{D_0}{p}\right)
=-\left(\frac{D_0}{q}\right),
\]

but it treats this sign as hidden.  Its factor-residue decoder branches over
both signs, while its balanced sum congruence eliminates the sign.  F177's
gap congruence does neither in the frozen scan.

The distinction occurs on a concrete valid F170 state.  Take

\[
N=1147=31\cdot37,\qquad D_0=3.
\]

Here \((3/31)=-1\), \((3/37)=+1\), so \(\epsilon=-1\).  In
\((\mathbb Z/N\mathbb Z)[w]/(w^2-3)\), the public point

\[
G=1006w
\]

has norm one and exact order four modulo both hidden primes: its square is
\(-1\) in both components.  Thus \(B=4\) is a valid exact common torus
order.  The actual gap is six, and modulo \(B^2=16\),

\[
\epsilon(N-1)\equiv6,
\qquad
-\epsilon(N-1)\equiv10.
\]

Inside \(0<D<\sqrt{N/2}\), the correct branch contains \(6,22\), while
the other branch contains \(10\).  Thus an orientation-free scan must use
three candidates here.  The one-branch bound is approximately \(2.497\)
and cannot be presented as the total orientation-free count.

This example does not show that the two-branch algorithm is slow.  It shows
only that the frozen claim must distinguish an oriented input from the
ordinary F170 state.

## 5. Bit complexity

The supplied common orders satisfy \(M\le p-1\) and
\(B\le\min(p-\epsilon,q+\epsilon)\), so \(M^2\), \(B^2\), and all
candidates have \(O(n)\) bits.  Computing the first member of a residue
class in an interval, advancing by the modulus, exact square-root testing,
parity testing, multiplication, and division all take polynomial bit time
per candidate.  A QP number of candidates therefore gives deterministic QP
total bit cost.  Enumerating both torus signs changes this cost only by a
constant factor.

## 6. Exact scope relative to F170, F172, and F173

The ordinary branch is a genuine stronger terminal use of one existing
common-order state: it exploits a modulus \(M^2\), whereas direct factor or
sum residue enumeration uses only \(M\).

The torus branch gives the analogous square modulus for the factor gap.  As
frozen, its exact count is an oriented-input theorem.  With the two-sign
repair, it also applies to the standard F170 torus state with the same QP
threshold up to constants.

F177 does not supply either common order.  It does not force growth, handle
an F172/F173 constant-common-order family, cover unbalanced or nonsquarefree
inputs, or prove all-input QP factoring.  F170's combined ordinary/torus CRT
decoder remains a distinct terminal rule and can use two moderate channels
together.  No contradiction with the promoted interfaces was found.
