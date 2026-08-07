# PASS

The SHA-256 digest of the reconstruction statement is

~~~text
aafa64e607c6cd108b08b43d3084a91ca388930792c569db083c4b9d9e58fabe
~~~

It matches the pinned digest. Every mathematical claim is correct.

The source statement has two form-feed control characters in the displayed
density where the TeX command for a fraction should begin. The count
immediately before it determines the intended and mathematically correct
formula:

\[
\frac1A+\frac1B-\frac2{AB}.
\]

This is a mechanical presentation defect, not a mathematical counterexample.

## 1. Prime-by-prime coprimality

Fix a prime \(\ell\), and put

\[
\alpha=v_\ell(m_p),\qquad
\beta=v_\ell(m_q),\qquad
a=v_\ell(p-1),\qquad
b=v_\ell(q-1),\qquad
e=v_\ell(N-1).
\]

Since \(K_p\le\mathbb F_p^\times\) and
\(K_q\le\mathbb F_q^\times\),

\[
\alpha\le a,\qquad \beta\le b.
\]

Let \(t=\min(a,b)\). Both \(p\) and \(q\) are \(1\) modulo \(\ell^t\), so

\[
pq\equiv1\pmod{\ell^t}.
\]

Therefore

\[
e=v_\ell(pq-1)\ge\min(a,b). \tag{1}
\]

The powered local orders have valuations

\[
v_\ell(A)=\max(\alpha-e,0),
\qquad
v_\ell(B)=\max(\beta-e,0). \tag{2}
\]

If both were positive, then

\[
a\ge\alpha>e,\qquad b\ge\beta>e,
\]

contradicting (1). No prime divides both \(A\) and \(B\), and hence

\[
\gcd(A,B)=1.
\]

### Valuation edge cases

The proof includes \(\ell=2\). Since \(p,q\) are odd, both
\(v_2(p-1)\) and \(v_2(q-1)\) are positive, and (1) applies without any
odd-prime exception.

If \(a=b\), then \(e\ge a=b\), so the \(\ell\)-part is removed from both
powered local images. If \(a<b\), then \(e\ge a\), so it is certainly
removed from the \(p\)-side, although a higher \(\ell\)-power can remain on
the \(q\)-side. If one of \(a,b\) is zero, only the other local group can
have an \(\ell\)-part in the first place. These are all possibilities.

## 2. The powered subgroup is the full rectangle

The projection of \(S=K^E\) onto the \(p\)-component is exactly

\[
K_p^E.
\]

Indeed, projection commutes with powering, and every element of \(K_p\) is
the projection of some element of \(K\). Since \(K_p\) is cyclic of order
\(m_p\), its power image has order

\[
\frac{m_p}{\gcd(m_p,E)}=A.
\]

The \(q\)-projection is similarly \(K_q^E\), of order \(B\).

Thus \(S\) is a subgroup of

\[
K_p^E\times K_q^E
\]

which surjects onto each factor. Each of \(A\) and \(B\) divides \(|S|\)
by the homomorphism theorem. Since they are coprime, \(AB\mid |S|\).
On the other hand,

\[
|S|\le |K_p^E\times K_q^E|=AB.
\]

Consequently

\[
|S|=AB
\]

and the subgroup inclusion is equality:

\[
S=K_p^E\times K_q^E.
\]

No cyclicity of \(K\), graph subgroup, or irredundant generator list was
used. Only the two local images are cyclic, as every subgroup of a
finite-field multiplicative group is.

## 3. Exact separator count and density

In the full product, positive separators of the first type are

\[
(1,y),\qquad y\in K_q^E\setminus\{1\},
\]

of which there are \(B-1\). The second type contributes the
\(A-1\) elements

\[
(x,1),\qquad x\in K_p^E\setminus\{1\}.
\]

The two sets are disjoint. Therefore the exact count is

\[
A+B-2,
\]

and uniform density is

\[
\delta_+(S)
=\frac{A+B-2}{AB}
=\frac1A+\frac1B-\frac2{AB}. \tag{3}
\]

If \(A,B\ge2\), assume without loss of generality that \(A\le B\). Then

\[
\delta_+(S)\ge\frac1A
\iff
A+B-2\ge B
\iff
A\ge2.
\]

Thus

\[
\delta_+(S)\ge\frac1{\min\{A,B\}}.
\]

If \(A=1<B\), every nonidentity element of
\(\{1\}\times K_q^E\) is a separator, and

\[
\delta_+(S)=1-\frac1B.
\]

The case \(B=1<A\) is symmetric. If \(A=B=1\), then \(S=\{1\}\), the count
and density are both zero, and no separator exists.

Because \(\gcd(A,B)=1\), the case \(A=B>1\) cannot occur.

## 4. A public near-uniform sampler

Let the public generators of \(K\) be \(g_1,\ldots,g_k\), and compute

\[
y_i=g_i^{N-1}\pmod N.
\]

The power map is a homomorphism in this abelian group, so

\[
S=\langle y_1,\ldots,y_k\rangle. \tag{4}
\]

Let \(n_i=\operatorname{ord}(y_i)\), used only in the proof. If
\(U_i\) were exactly uniform modulo \(n_i\), then the vector
\((U_1,\ldots,U_k)\) would be uniform in
\(\prod_i\mathbb Z/n_i\mathbb Z\). Its product map onto \(S\) is a
surjective homomorphism, so equal fiber sizes would make

\[
\prod_i y_i^{U_i}
\]

exactly uniform on \(S\).

The orders \(n_i\) need not be known. Choose a public range length

\[
R\ge4kN^2,
\]

and sample independent integers \(T_i\) uniformly from
\(\{0,\ldots,R-1\}\). Reduction of \(T_i\) modulo \(n_i\) is within total
variation at most \(n_i/R\) of uniform, because every residue has either
\(\lfloor R/n_i\rfloor\) or \(\lceil R/n_i\rceil\) preimages. Since
\(n_i<N\), the joint exponent law is within

\[
\sum_i\frac{n_i}{R}
<\frac{kN}{R}
\le\frac1{4N}
\]

of the uniform product law. Total variation cannot increase under the
public product map, so the sampled residue

\[
Y=\prod_i y_i^{T_i}\pmod N
\]

is within \(1/(4N)\) of uniform on \(S\).

The range \(R\) can be replaced by the least convenient power of two above
the displayed bound. Its bit length is
\(O(\log k+\log N)\), so random generation and repeated-squaring
exponentiation remain polynomial-time operations.

### Success probability and Las Vegas verification

Assume \(S\ne1\). Formula (3) gives positive uniform success probability.
Indeed, \(|S|=AB\le\varphi(N)<N\), so even the crude bound is

\[
\delta_+(S)\ge\frac1{|S|}>\frac1N.
\]

The near-uniform trial therefore succeeds with probability at least

\[
\delta_+(S)-\frac1{4N}
>\frac34\,\delta_+(S). \tag{5}
\]

If one of \(A,B\) is numerically polynomial in \(\log N\), then their
minimum is polynomial. If the minimum is at least \(2\), Section 3 gives
inverse-polynomial density. If the minimum is \(1\), the other is at least
\(2\) because \(S\ne1\), and the density is at least \(1/2\). Thus (5) is
inverse-polynomial in all promised cases.

Repeat independent trials and compute

\[
d=\gcd(Y-1,N).
\]

Return only after publicly verifying \(1<d<N\). Every returned answer is a
genuine factor, and the expected number of trials is polynomial under the
promise. The procedure is therefore Las Vegas. It uses neither the unknown
orders \(n_i\) nor any of \(p,q,m_p,m_q,A,B\).

## 5. Deterministic capped enumeration

Use the same powered generators \(y_i\). Starting from the identity,
breadth-first multiply each discovered residue by every \(y_i\), storing
canonical residues in a deterministic balanced search tree and a queue.

Explicit inverses are unnecessary. In a finite group the inverse of every
generator is a positive power of that generator, so forward multiplication
generates the whole subgroup in (4).

If a \((T+1)\)-st distinct residue appears, stop this enumeration. Before
that point, at most \(T+1\) residues are stored, and each processed residue
causes \(k\) modular multiplications. If the queue empties with at most
\(T\) residues, closure is complete.

When

\[
1<AB=|S|\le T,
\]

the enumeration completes and, by Section 3, visits at least one positive
separator. Testing \(\gcd(x-1,N)\) for every discovered \(x\) returns a
proper factor. If \(|S|>T\), closure cannot finish below the cap, so the
extra residue is eventually found and the declared work bound is respected.
If \(S=1\), enumeration ends without a factor; this case is outside the
success promise.

The initial powers use the \(O(\log N)\)-bit exponent \(N-1\). With
\(T\), the generator count, and their encodings polynomial in \(\log N\),
the algorithm performs \(O(kT)\) modular multiplications and deterministic
lookup operations on \(O(\log N)\)-bit residues. Gcd tests and storage are
also polynomial.

The executable algorithm uses only \(N\), the public cap \(T\), and the
public generators. It does not use any hidden local order, factor, or
projection.

## 6. A graph subgroup is killed abstractly

Suppose \(H\le K\) is a graph of an isomorphism between its two local
images. Since \(H_p\le\mathbb F_p^\times\) and
\(H_q\le\mathbb F_q^\times\),

\[
|H|\mid p-1,
\qquad
|H|\mid q-1.
\]

It follows that

\[
p\equiv q\equiv1\pmod{|H|}
\]

and hence

\[
N-1=pq-1\equiv0\pmod{|H|}.
\]

Thus \(|H|\mid N-1\). In particular every element of \(H\) is killed by the
\((N-1)\)-power map.

The homomorphism

\[
\psi:K\longrightarrow S,\qquad k\longmapsto k^{N-1}
\]

therefore has \(H\) in its kernel. Since the ambient group is abelian,
\(H\) is normal, and \(\psi\) factors through an abstract surjection

\[
\overline\psi:K/H\longrightarrow S,
\qquad
kH\longmapsto k^{N-1}.
\]

The homomorphism theorem gives the stronger divisibility

\[
|S|\mid[K:H],
\]

and therefore

\[
AB=|S|\le[K:H].
\]

This factorization is only an abstract proof object. The public generator
list for \(K\) does not by itself supply generators for \(H\), a membership
test for \(H\), quotient coordinates, or an efficient representation of
\(K/H\). Neither decoder attempts to compute that quotient.

## 7. Fixed specialization at \(N=4033\)

The factorization is

\[
4033=37\cdot109.
\]

The supplied orders give

\[
\operatorname{ord}_{37}(5)=36,
\qquad
\operatorname{ord}_{109}(5)=27.
\]

Modulo \(37\), the exponent \(4032\) is a multiple of \(36\), so

\[
5^{4032}\equiv1\pmod{37}.
\]

Modulo \(109\),

\[
4032\equiv9\pmod{27}.
\]

Also,

\[
5^3\equiv16,\qquad
5^9\equiv16^3\equiv63\pmod{109}.
\]

The integer \(3442\) satisfies

\[
3442=37\cdot93+1,
\qquad
3442=109\cdot31+63.
\]

CRT therefore gives

\[
5^{4032}\equiv3442\pmod{4033}.
\]

The residue \(63\) has exact order \(3\) modulo \(109\):

\[
63^2\equiv45,\qquad
63^3\equiv1,\qquad
63\ne1\pmod{109}.
\]

Thus the powered element has local orders \(1\) and \(3\). It follows
immediately that

\[
\gcd(5^{4032}-1,4033)=37.
\]

For the local image sizes of \(K=\langle2,5\rangle\), the \(37\)-side is
already full because \(5\) has order \(36\):

\[
m_p=36.
\]

On the \(109\)-side, one has

\[
2^9\equiv76,\qquad
2^{18}\equiv-1,\qquad
2^{12}\equiv63\ne1\pmod{109}.
\]

Hence \(\operatorname{ord}_{109}(2)=36\). Together with the order \(27\)
of \(5\), this generates the full cyclic group of order

\[
m_q=\operatorname{lcm}(36,27)=108.
\]

Finally,

\[
\gcd(36,4032)=36,
\qquad
\gcd(108,4032)=36.
\]

Therefore

\[
A=1,\qquad B=3.
\]

All claims in the first fixed example are correct.

## 8. Fixed specialization at \(N=2047\)

The supplied subgroup exponent is

\[
\exp(K)=22.
\]

Since

\[
2046=22\cdot93,
\]

every \(k\in K\) satisfies \(k^{2046}=1\). Thus

\[
K^{2046}=\{1\}
\]

and the unpunctured image contains no separator.

For completeness, the supplied punctured claim can be checked from the
local structure. One has

\[
2047=23\cdot89.
\]

Modulo \(23\),

\[
11^2\equiv6,\qquad
11^8\equiv8,\qquad
11^{10}\equiv2,\qquad
11^{11}\equiv-1.
\]

Modulo \(89\),

\[
11^2\equiv32,\qquad
11^4\equiv45,\qquad
11^8\equiv67,\qquad
11^{10}\equiv8,\qquad
11^{11}\equiv-1.
\]

Thus \(11\) has order \(22\) modulo both primes. The element \(2\) has
order \(11\) modulo both because

\[
2^{11}=2048\equiv1\pmod{2047}.
\]

The subgroup \(H=\langle11\rangle\) is a graph of order \(22\). The element
\(2\) is not in it: \(2\cdot11=22\) is \(-1\) modulo \(23\), but not modulo
\(89\). Its coset has order \(11\).

Adjoining \(2\) does not enlarge either local image. The \(23\)-projection
of \(H\) is already the full order-\(22\) group. The \(89\)-projection has
order \(22\) and contains the unique subgroup of order \(11\), hence it
contains \(2\). Thus \(K/H\) is a pure phase group of order \(11\).

For the punctured exponent \(186\),

\[
\gcd(22,186)=2,
\qquad
\gcd(11,186)=1.
\]

It contracts the graph from order \(22\) to order \(11\) and preserves the
phase quotient of order \(11\). The powered group therefore has order

\[
11\cdot11=121.
\]

Both local images have order \(11\), while the global group has order
\(121\). The two projection kernels each have order \(11\) and intersect
only in the identity. Hence the exact positive-separator count is

\[
(11-1)+(11-1)=20.
\]

There is no contradiction. The unpunctured exponent \(2046\) is divisible
by \(11\) and kills the phase quotient; the punctured exponent \(186\) is
coprime to \(11\) and preserves it.

## 9. Scope

The theorem gives a public rectangularization identity and two conditional
decoders. It does not prove that a supplied feedback subgroup has a
nontrivial \(N-1\) image, that either local powered image has polynomial
order, or that the full powered image is polynomially enumerable.

When both coprime local orders are large, the stated sampler can have
negligible separator density and the capped enumeration can stop before
closure. No decoder for that regime is proved.

The valuation and rectangle arguments use exactly two distinct prime CRT
components. They are not asserted for arbitrary composites. No all-input
factoring algorithm follows.
