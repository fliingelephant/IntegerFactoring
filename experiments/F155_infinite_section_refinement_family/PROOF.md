# Proof of the F155 infinite section-refinement family

## 1. Integrality, canonical representatives, and units

The modulus \(M=23400\) is divisible by \(4,6,9,25,\) and \(13\).
Condition \(N\equiv77\pmod M\) gives

\[
N\equiv1\pmod4,
\qquad
N\equiv5\pmod6,
\qquad
N\equiv5\pmod9,
\qquad
N\equiv2\pmod{25},
\qquad
N\equiv12\pmod{13}.
\tag{21}
\]

Hence all three quantities in (3) are integers. For \(N>13\), they lie
strictly between \(0\) and \(N\).

Since

\[
2z=N-3,
\qquad
3s=N-2,
\qquad
4a=3N+9,
\]

any common divisor of \(z,N\) divides \(3\), any common divisor of \(s,N\)
divides \(2\), and any common divisor of \(a,N\) divides \(9\). The residue
conditions in (21) therefore make all three units modulo \(N\).

Direct expansion gives

\[
zs
=
\frac{(N-3)(N-2)}6
=
1+\frac{N-5}{6}N,
\tag{22}
\]

and

\[
z^2-a
=
\frac{N(N-9)}4.
\tag{23}
\]

The quotients are integers by (21). Also \(0<a<N\), so \(a\) is the least
positive residue of \(z^2\), and \(0<s<N\), so \(s=\iota_N(z)\).

## 2. Direct screens

Exact subtraction and addition give

\[
z-s=\frac{N-5}{6},
\qquad
z+s=\frac{5N-13}{6}.
\tag{24}
\]

Because \(\gcd(6,N)=1\),

\[
\gcd(z-s,N)=\gcd(5,N)=1,
\]

and

\[
\gcd(z+s,N)=\gcd(13,N)=1.
\]

The last equalities use \(N\equiv2\pmod5\) and
\(N\equiv12\pmod{13}\). Multiplication by the unit \(z\) also gives

\[
\gcd(z-s,N)=\gcd(z^2-1,N)=\gcd(a-1,N)
\]

and the analogous plus identity. This proves (5) and (6).

## 3. Exact forced split

Write \(N=77+23400t\). Then

\[
s=25+7800t=25(1+312t),
\]

\[
a=60+17550t=5(12+3510t).
\]

The second parenthesis is \(2\pmod5\), so \(v_5(a)=1\). In particular,
\(a\) is not a perfect power.

Furthermore,

\[
4a-9s=15.
\]

Every common divisor of \(a,s\) divides \(15\). The integer \(s\) is
\(1\pmod3\), so \(3\nmid s\), while both integers are divisible by \(5\).
Thus their gcd is exactly \(5\). Since \(v_5(a)=1\), the two descendants
\(5\) and \(a/5\) are coprime. This proves the complete claimed refinement.

## 4. Infinite balanced semiprimes

The residue classes \(7\) and \(11\) are reduced modulo \(M\). By the prime
number theorem in fixed arithmetic progressions, every sufficiently large
interval \([X,2X]\) contains a prime \(P\equiv7\pmod M\) and a prime
\(R\equiv11\pmod M\). Their classes differ, so \(P\ne R\).

Choose such pairs along disjoint intervals with \(X\) tending to infinity.
Then

\[
X^2\le N=PR\le4X^2,
\]

so the factors are balanced and

\[
n=\lceil\log_2(N+1)\rceil=2\log_2X+O(1).
\]

For all sufficiently large \(X\), both factors exceed \(n^2\). This gives
infinitely many balanced trial-hard distinct-prime semiprimes. Their product
class is

\[
PR\equiv7\cdot11\equiv77\pmod M.
\]

## 5. The old subgroup contains both feedback endpoints

Modulo either hidden prime \(L\), equation (3) gives

\[
z\equiv-3\cdot2^{-1}.
\]

Its Legendre symbol equals \(\left(\frac{-6}{L}\right)\), because
multiplication by \(2^2\) does not change a square class.

For \(P\equiv7\pmod{24}\),

\[
\left(\frac{-1}{P}\right)=-1,
\qquad
\left(\frac2P\right)=1,
\qquad
\left(\frac3P\right)=-1.
\]

For \(R\equiv11\pmod{24}\),

\[
\left(\frac{-1}{R}\right)=-1,
\qquad
\left(\frac2R\right)=-1,
\qquad
\left(\frac3R\right)=1.
\]

In both cases the product is \(+1\), proving (15). Thus \(z\) lies in the
local square subgroup.

Both hidden primes are \(3\pmod4\), so each square subgroup has odd order
\((L-1)/2\). The local order of \(z\) is therefore odd. Squaring is an
automorphism on an odd-order cyclic group, hence
\(\langle z^2\rangle=\langle z\rangle\) locally. CRT gives the same equality
modulo \(N\). Since \(a\equiv z^2\), both \(z\) and \(z^{-1}=s\) lie in
\(H=\langle a\rangle\).

## 6. Strict subgroup expansion

Because \(5\equiv1\pmod4\), quadratic reciprocity gives

\[
\left(\frac5P\right)=\left(\frac P5\right).
\]

The class \(P\equiv7\pmod M\) gives \(P\equiv2\pmod5\), and \(2\) is a
quadratic nonresidue modulo \(5\). Hence
\(\left(\frac5P\right)=-1\).

Every power of \(a=z^2\) is a square modulo \(P\), so no element of \(H\)
can reduce to the nonresidue \(5\). Thus \(5\notin H\).

After refinement, both \(5\) and \(a/5\) are named. Their product is the old
atom \(a\), so the new generated subgroup contains \(H\). It also contains
\(5\notin H\), which proves strict containment (20).

## 7. Scope

The proof gives an exact public refinement and strict subgroup expansion on
an infinite balanced trial-hard family. It supplies no public exponent that
isolates one hidden prime in the enlarged subgroup. It also uses the fixed
congruence family \(N\equiv77\pmod{23400}\); it is not a density or
all-input theorem.
