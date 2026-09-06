# Blind reconstruction of F155

## Audit boundary and verdict

I verified the SHA-256 digest of `STATEMENT.md` before reading it:

```text
b42079fcb9b0d09a16483fffd8ee41d24f3fc6c3ac6bddc4495af6fa09298998
```

This reconstruction uses only that statement. I did not read another F155
file, proof, audit, manifest, or ledger.

All displayed arithmetic, congruence, existence, Legendre-symbol, order, and
subgroup-inclusion claims are correct. The strict subgroup growth is a
statement about a specified named-block ledger whose old generator list is
exactly \(\{a\}\). It is not the release of previously hidden public data:
the integer \(5\) is already a public constant, and \(s\) and \(a/5\) are
computable directly from \(N\). This distinction is essential.

## 1. Public relation and endpoint screens

Factor

\[
M=23{,}400=2^3 3^2 5^2 13.
\]

If \(N\equiv77\pmod M\), then

\[
N\equiv1\pmod4,\qquad N\equiv2\pmod3,
\qquad N\equiv2\pmod5,\qquad N\equiv-1\pmod{13}.
\]

These congruences prove that \(z=(N-3)/2\), \(s=(N-2)/3\), and
\(a=(3N+9)/4\) are integers. For \(N>13\), they are positive and less than
\(N\); the only non-immediate upper bound is

\[
a<N \iff 3N+9<4N,
\]

which follows from \(N>9\).

They are units modulo \(N\). Since \(N\) is coprime to \(2,3,4\),

\[
\begin{aligned}
\gcd(z,N)&=\gcd(N-3,N)=\gcd(3,N)=1,\\
\gcd(s,N)&=\gcd(N-2,N)=\gcd(2,N)=1,\\
\gcd(a,N)&=\gcd(3N+9,N)=\gcd(9,N)=1,
\end{aligned}
\]

where multiplication by the relevant denominator does not change a gcd with
\(N\).

The modular relations follow from the stronger exact identities

\[
z^2-a=\frac{N(N-9)}4,
\qquad
zs-1=\frac{N(N-5)}6.
\]

The quotients are integers under the stated congruence. Hence
\(z^2\equiv a\pmod N\) and \(zs\equiv1\pmod N\). Since \(0<s<N\), \(s\)
is the least positive representative of \(z^{-1}\).

The endpoint differences have exact forms

\[
z-s=\frac{N-5}{6},
\qquad
z+s=\frac{5N-13}{6}.
\]

Because \(\gcd(6,N)=1\),

\[
\gcd(z-s,N)=\gcd(5,N)=1,
\qquad
\gcd(z+s,N)=\gcd(13,N)=1.
\]

Here \(N\equiv2\pmod5\) and \(N\equiv-1\pmod{13}\). This proves both null
screens directly. It also proves the claimed equivalent screens, since

\[
4(a-1)=3N+5,
\qquad
4(a+1)=3N+13,
\]

so \(\gcd(a-1,N)=1\) and \(\gcd(a+1,N)=1\). Conceptually, the equivalence
also follows from

\[
z(z-s)\equiv a-1\pmod N,
\qquad
z(z+s)\equiv a+1\pmod N,
\]

because \(z\) is a unit.

## 2. Forced integer refinement

Write \(N=77+23{,}400t\). The conditions \(N>13\) and the congruence imply
\(t\geq0\). Direct substitution gives

\[
s=25+7800t,
\qquad
a=60+17550t.
\]

Also,

\[
4a-9s=(3N+9)-3(N-2)=15.
\]

Thus \(g=\gcd(a,s)\) divides \(15\). Both displayed expressions are
divisible by \(5\), so \(5\mid g\). But

\[
s\equiv25\equiv1\pmod3,
\]

so \(3\nmid g\). Consequently

\[
\gcd(a,s)=5.
\]

Moreover,

\[
a=60+17550t\equiv10\pmod{25},
\]

and hence \(v_5(a)=1\). Therefore \(5\) and \(a/5\) are coprime. If
\(a=b^k\) for some integer \(b\) and \(k\geq2\), then
\(v_5(a)=k v_5(b)\), contradicting \(v_5(a)=1\). Thus \(a\) is not a
perfect power and, in particular, is not a square.

The gcd against \(s\) therefore refines the old integer block \(a\) exactly
as

\[
a=5(a/5),
\qquad
\gcd(5,a/5)=1.
\]

Both factors are units modulo \(N\), since \(5\nmid N\) and \(a\) is a
unit. No continued retention of \(s\) is needed to retain this split.

## 3. Infinitely many balanced trial-hard semiprimes

The residue classes \(7\) and \(11\) are both coprime to \(M\). The prime
number theorem in arithmetic progressions implies, for either
\(c\in\{7,11\}\),

\[
\pi(5X/4;M,c)-\pi(X;M,c)
\sim \frac{X}{4\varphi(M)\log X}>0.
\]

Thus, for every sufficiently large \(X\), there is a prime congruent to
\(7\pmod M\) and a prime congruent to \(11\pmod M\), both in
\((X,5X/4)\). Taking a sequence of disjoint such intervals, for example with
\(X=2^j\), gives infinitely many pairs \((P,R)\). They are distinct because
their residue classes modulo \(M\) differ, and

\[
\frac45<\frac PR<\frac54,
\]

which is stronger than the stated \(1/2<P/R<2\). Also

\[
PR\equiv7\cdot11\equiv77\pmod M.
\]

Let \(N=PR\). The weaker stated balance bound already gives

\[
P>\sqrt{N/2},
\qquad
R>\sqrt{N/2}.
\]

If \(n=\lceil\log_2(N+1)\rceil\), then

\[
n\leq\log_2(N+1)+1
\]

and

\[
\frac{\sqrt{N/2}}{(\log_2(N+1)+1)^2}\longrightarrow\infty.
\]

Hence \(P,R>n^2\) for all sufficiently large members. This proves the
claimed balance and the stated trial-division threshold unconditionally.
It does not prove general computational hardness of factoring these
semiprimes.

## 4. Endpoint membership in the old subgroup

Let \(L\) be either \(P\) or \(R\). Reduction modulo \(L\) gives

\[
z\equiv-\frac32\pmod L.
\]

For an odd prime \(L\nmid6\), the Legendre symbol of this residue is

\[
\left(\frac{z}{L}\right)
=\left(\frac{-3}{L}\right)
 \left(\frac{2^{-1}}{L}\right)
=\left(\frac{-6}{L}\right),
\]

because the Legendre symbol of \(2^{-1}\) equals that of \(2\). The standard
supplementary laws give the following table:

\[
\begin{array}{c|ccc|c}
L\bmod24 & (-1/L)&(2/L)&(3/L)&(-6/L)\\ \hline
7  &-1&+1&-1&+1\\
11 &-1&-1&+1&+1
\end{array}
\]

Since \(M\) is divisible by \(24\), the two hidden primes fall into these
two rows. Thus \(z\) is a quadratic residue modulo both primes.

Both primes are \(3\pmod4\). The subgroup of squares in
\((\mathbb Z/L\mathbb Z)^\times\) therefore has order \((L-1)/2\), which
is odd. The local order of \(z\) is consequently odd at both \(P\) and
\(R\). By the Chinese remainder theorem, the order

\[
d=\operatorname{ord}_N(z)
\]

is the least common multiple of those two local orders and is also odd.
Since \(a\equiv z^2\pmod N\),

\[
a^{(d+1)/2}\equiv z^{d+1}\equiv z\pmod N.
\]

It follows that

\[
\langle a\rangle=\langle z^2\rangle=\langle z\rangle.
\]

In particular, both \(z\) and \(s=z^{-1}\) belong to the old subgroup
\(H=\langle a\rangle\). Section completion therefore adds no residue class
outside \(H\).

## 5. Strict named-block subgroup expansion

Because \(P\equiv7\pmod M\) and \(5\mid M\), one has \(P\equiv2\pmod5\).
Quadratic reciprocity for the prime \(5\) gives

\[
\left(\frac5P\right)
=\left(\frac P5\right)
=\left(\frac25\right)
=-1.
\]

Every element of \(H=\langle z^2\rangle\) projects to a square modulo
\(P\), whereas \(5\) projects to a nonsquare. Hence \(5\notin H\).

Set

\[
G=\langle5,a/5\rangle.
\]

The exact integer identity \(a=5(a/5)\) shows that \(a\in G\), and hence
\(H\leq G\). But \(5\in G\setminus H\), so

\[
H<G.
\]

This proves strict expansion with no assumption about the unknown orders of
the generators. For context, \(R\equiv1\pmod5\), so \((5/R)=+1\); the new
generator has different quadratic characters in the two CRT components.
That observation does not by itself supply an efficiently usable exponent
that factors \(N\).

## 6. Source semantics and the public \(5\)

The modular source is genuinely uniform in bare \(N\): the exact identity

\[
z^2=a+N\frac{N-9}{4}
\]

is a public one-row square relation. But this same uniformity imposes a
strict limit on what the refinement demonstrates.

First, \(z\) is public, so its least positive inverse \(s\) is already
computable by the extended Euclidean algorithm. Here it is even given by
the public formula \((N-2)/3\). Section completion does not disclose a new
unknown integer.

Second, the released divisor is literally the fixed public integer \(5\).
Indeed, \(a\equiv10\pmod{25}\) publicly shows \(5\mid a\), and

\[
\frac a5=12+3510t=\frac{3N+9}{20}
\]

is directly computable from \(N\). The gcd with \(s\) certifies the same
split inside the formal refinement procedure, but it does not reveal a
previously hidden numerical factor.

Therefore there are two different, non-interchangeable readings:

1. Under the declared named-block ledger, the initial block list is exactly
   \(\{a\}\), so its subgroup is \(H=\langle a\rangle\). Replacing that
   formal atom by the coprime blocks \(5\) and \(a/5\) strictly enlarges the
   named-block-generated subgroup. This theorem is correct.
2. Under a knowledge semantics in which any public constant or any directly
   computable exact factor may be named at initialization, \(5\) and
   \(a/5\) were available before feedback. On that reading there is no new
   public information and no feedback-caused subgroup expansion.

Thus “atom” must mean an initially unsplit named block, not an integer whose
factor \(5\) is unknown. The result validates a representation-level ledger
transition. It does not establish hidden-factor discovery.

Finally, \(5\nmid N\), and the two stated endpoint gcd screens are null, so
none of these elementary operations returns \(P\) or \(R\). The inequality
\(P,R>n^2\) also defeats trial division only up to the stated project bound.
The phrase “the factors remain unknown” is consequently an input-model
condition, not an unconditional hardness theorem: the party that constructs
\(N=PR\) can know \(P,R\), and no general factoring lower bound is proved.
This is consistent with the statement's express disclaimer that it gives no
bounded-order separator or quasipolynomial selector.

## Conclusion

The construction proves an infinite family of balanced semiprimes for which
the endpoint gcd screens are null, both endpoint residues lie in the old
cyclic subgroup, the integer overlap with the inverse representative is
exactly \(5\), and splitting the formal old block makes the named-block
subgroup strictly larger. The proof is unconditional. Its scope is strictly
representation-level: the value \(5\) and the entire split are already
public from bare \(N\), and no factoring advantage beyond the stated ledger
phenomenon is proved.
