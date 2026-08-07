# PASS

The SHA-256 of RECONSTRUCT_STATEMENT.md is
dee4543c9f3eed076446c789c64dd2055fb0e9612302d44473c948a5cac0426c,
as required. Every mathematical claim is correct with the phase-only scope
stated precisely in Section 8.

## 1. The modulus and the initial identities

The factorization is exact:

\[
23\cdot89=23(90-1)=2070-23=2047.
\]

The only primes not exceeding \(\sqrt{23}<5\) are \(2,3\), and neither
divides \(23\). The primes not exceeding \(\sqrt{89}<10\) are
\(2,3,5,7\); none divides \(89\), with \(89=7\cdot12+5\). Hence \(23\)
and \(89\) are distinct odd primes.

The integer identities are

\[
11\cdot1861=20471=1+10\cdot2047
\]

and

\[
312\cdot269=83928=1+41\cdot2047.
\]

Also,

\[
11^4=14641=7\cdot2047+312,
\]

so \(11^4\equiv312\pmod N\). The second product identity shows that \(269\)
is the inverse of \(312\) modulo \(N\). Therefore

\[
11^{-4}\equiv269\pmod N.
\]

## 2. The four old endpoints

The integer \(11\) is prime, and

\[
312=2^3\cdot3\cdot13.
\]

For \(269\), one has \(16^2<269<17^2\). It is not divisible by
\(2,3,5\), and

\[
269\bmod7=3,\qquad
269\bmod11=5,\qquad
269\bmod13=9.
\]

Thus \(269\) is prime.

For \(1861\), one has \(43^2<1861<44^2\). It is not divisible by
\(2,3,5\). The remaining prime-divisor checks through \(43\) are

\[
\begin{array}{c|rrrrrrrrrrr}
\ell&7&11&13&17&19&23&29&31&37&41&43\\ \hline
1861\bmod\ell&6&2&2&8&18&21&5&1&11&16&12.
\end{array}
\]

Hence \(1861\) is prime.

The four values \(11,1861,312,269\) are visibly distinct and greater than
one. Three are distinct primes. The prime factors of \(312\) are only
\(2,3,13\), none of which is one of those three primes. The four values are
therefore pairwise coprime.

A positive integer is a nontrivial perfect power only if the exponents in
its prime factorization have a common divisor greater than one. A prime is
not a nontrivial perfect power, and the factorization
\(312=2^3 3^1 13^1\) has exponent gcd one. Thus none of the four endpoints
is a nontrivial integer perfect power.

Modulo \(N\), the four endpoints are

\[
11,\qquad 11^{-1},\qquad 11^4,\qquad 11^{-4}.
\]

They all lie in \(H_0=\langle11\rangle\), while the first endpoint itself
generates \(H_0\). Their residues consequently generate exactly \(H_0\).

## 3. The local order of \(11\) and the old sign obstruction

Modulo \(23\),

\[
11^2\equiv6,\quad
11^4\equiv13,\quad
11^5\equiv5,\quad
11^{10}\equiv2,\quad
11^{11}\equiv-1.
\]

Modulo \(89\),

\[
11^2\equiv32,\quad
11^4\equiv45,\quad
11^5\equiv50,\quad
11^{10}\equiv8,\quad
11^{11}\equiv-1.
\]

Thus \(11^{22}\equiv1\) in both fields. In either field, the order cannot
divide \(11\), because the eleventh power is \(-1\), and it cannot be \(2\),
because \(11\) is not the local element \(-1\). Since the order divides
\(22\), it is exactly

\[
\operatorname{ord}_{23}(11)
=\operatorname{ord}_{89}(11)
=22.
\]

Every \(h\in H_0\) has the form \(h=11^k\). It is locally \(1\) exactly
when \(k\equiv0\pmod{22}\), at both primes. Since \(11^{11}=-1\) locally
and the local order is \(22\), it is locally \(-1\) exactly when
\(k\equiv11\pmod{22}\), again at both primes. Therefore the identity and
negative-identity statuses are synchronized.

It follows that \(\gcd(h-1,N)\) is \(N\) when both coordinates are \(1\)
and is \(1\) otherwise. Likewise, \(\gcd(h+1,N)\) is \(N\) when both
coordinates are \(-1\) and is \(1\) otherwise. No direct sign gcd from
\(H_0\) is a proper divisor.

## 4. The canonical feedback pair

Starting from \(11^4\equiv312\pmod N\),

\[
\begin{aligned}
11^5&\equiv3432\equiv1385\pmod N,\\
11^6&\equiv15235\equiv906\pmod N,\\
11^7&\equiv9966\equiv1778\pmod N.
\end{aligned}
\]

Thus \(g=[11^7]_N=1778\). The inverse identity is exact:

\[
1778\cdot1735=3{,}084{,}830
\]

and

\[
1+1507\cdot2047=1+3{,}084{,}829=3{,}084{,}830.
\]

Since \(0<1735<N\), this proves that \(w=1735\) is the canonical inverse
of \(g\). Hence

\[
g=11^7\in H_0,\qquad
w=g^{-1}=11^{-7}\in H_0.
\]

Adjoining either feedback residue as a modular generator adds no new element
to \(H_0\).

## 5. Immediate tests, integer powers, and refinement

The local residues are

\[
\begin{array}{c|cc}
&\bmod 23&\bmod 89\\ \hline
1778&7&87=-2\\
1735&10&44.
\end{array}
\]

Neither entry in either row is \(1\) or \(-1\). Therefore

\[
\gcd(1778-1,N)
=\gcd(1778+1,N)
=\gcd(1735-1,N)
=\gcd(1735+1,N)
=1.
\]

Also \(1778-1735=43\), which is divisible by neither \(23\) nor \(89\).
Thus

\[
\gcd(1778-1735,N)=1.
\]

The exact prime factorizations are

\[
1778=2\cdot7\cdot127,
\qquad
1735=5\cdot347.
\]

The number \(127\) has no prime divisor among \(2,3,5,7,11\), the primes
not exceeding its square root. The number \(347\) has no prime divisor among
\(2,3,5,7,11,13,17\): its remainders for \(7,11,13,17\) are respectively
\(4,6,9,7\), and divisibility by \(2,3,5\) is immediate to exclude. Hence
\(127\) and \(347\) are prime. Every exponent in each displayed
factorization is one, so neither \(1778\) nor \(1735\) is a nontrivial
integer perfect power.

Using \(312=2^3\cdot3\cdot13\) and
\(1778=2\cdot7\cdot127\) gives

\[
\gcd(312,1778)=2.
\]

This is an integer refinement, not a modular subgroup operation.

To prove \(2\notin H_0\), suppose \(2\equiv11^k\pmod N\). The earlier
power table gives \(11^{10}\equiv2\pmod{23}\). Since \(11\) has order \(22\)
modulo \(23\), the assumed equality forces

\[
k\equiv10\pmod{22}.
\]

But modulo \(89\), it would then give

\[
2\equiv11^k\equiv11^{10}\equiv8\pmod{89},
\]

a contradiction. Hence \(2\notin H_0\), and
\(\langle H_0,2\rangle\) strictly contains \(H_0\). The modular feedback
residues stayed in \(H_0\), but their canonical integer representatives
enabled a gcd refinement that exposed an outside block.

## 6. Pure powers of the new block

The stated integer identity is

\[
2^{11}=2048=1+2047=1+N.
\]

Thus the order of \(2\) divides \(11\) modulo both \(23\) and \(89\). Since
\(11\) is prime and \(2\not\equiv1\) in either field, the order is exactly

\[
\operatorname{ord}_{23}(2)
=\operatorname{ord}_{89}(2)
=11.
\]

For every \(e\geq0\), \(2^e\) is locally \(1\) exactly when \(11\mid e\),
simultaneously at both primes. The subgroup generated by \(2\) has odd order
\(11\), so it contains no element of order \(2\). Since local \(-1\) has
order \(2\), no power of \(2\) is locally \(-1\) at either prime.

Consequently,

\[
\gcd(2^e-1,N)=
\begin{cases}
N,&11\mid e,\\
1,&11\nmid e,
\end{cases}
\]

including \(e=0\), and

\[
\gcd(2^e+1,N)=1
\]

for every integer \(e\geq0\). This proves the full phase-only failure, not
only a bounded exponent search.

## 7. The mixed word

The mixed word is

\[
2\cdot11=22.
\]

It satisfies

\[
22\equiv-1\pmod{23},
\qquad
22\not\equiv-1\pmod{89}.
\]

Therefore

\[
\gcd(22+1,2047)
=\gcd(23,23\cdot89)
=23.
\]

The new block alone has no successful pure-power phase, while one word that
mixes it with the old generator succeeds immediately.

## 8. Exact scope

This is one fixed canonical-integer realization. It proves the following
narrow separation: a universal post-split policy that discards the old
generators and tests only pure powers of the newly exposed block cannot
replace mixed-word processing after every split. This instance defeats that
policy, because every power of \(2\) fails while \(2\cdot11\) succeeds.

The witness does not show that all possible powering operations on arbitrary
elements of the expanded subgroup fail. In particular, it does not justify a
broader lower bound against algorithms that choose mixed elements and then
power them. This is the required phase-only scope qualification.

The construction is a single existential witness. It gives no all-input
choice rule for a canonical word, no detector for which refinement branch is
useful, no frequency or density theorem, no infinite hard family, and no
general factoring algorithm.

Finally, \(312\) is even, so trial division of the old endpoint exposes
\(2\) without the feedback relation. The unit \(2\) is also an ordinary
small public base that can be tried independently. Thus feedback is not
necessary to factor this fixed \(N\) when stronger preprocessing or
unrestricted factoring methods are allowed.
