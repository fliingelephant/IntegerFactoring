# PASS

The SHA-256 digest of the reconstruction statement is

~~~text
d65001d43a35c32ff826e6fa7cda54dbcaccf47cf9078c07111eb47b5aa005cf
~~~

It matches the pinned digest. Every algebraic, algorithmic, complexity,
edge-case, structural, and fixed-instance claim is correct.

## 1. The public annihilator equivalence

If

\[
\lambda\mid N-1,
\]

then every element of \(K\), and in particular every public generator,
satisfies \(g_i^{N-1}=1\).

Conversely, suppose

\[
g_i^{N-1}=1
\]

for every public generator. The ambient unit group is abelian, so for every

\[
k=\prod_i g_i^{a_i}\in K
\]

one has

\[
k^{N-1}=\prod_i(g_i^{N-1})^{a_i}=1.
\]

Thus \(N-1\) annihilates the whole subgroup. The exponent is the least
positive common multiple of all element orders, so

\[
\lambda\mid N-1.
\]

Redundant generators, identity generators, and a noncyclic subgroup do not
affect either implication.

## 2. The punctured witness

Assume the annihilator condition and let \(x\) be a positive separator.
Write

\[
d=\operatorname{ord}(x).
\]

Since \(d\mid\lambda\mid N-1\), for a chosen prime \(\ell\mid d\) the
valuations satisfy

\[
1\le C\le H\le e.
\]

Consequently

\[
j=e-C+1
\]

is an integer in the public range \(1\le j\le e\), and

\[
E=(N-1)/\ell^j
\]

satisfies

\[
v_\ell(E)=C-1. \tag{1}
\]

For every prime \(r\ne\ell\),

\[
v_r(E)=v_r(N-1)\ge v_r(\lambda)\ge v_r(d). \tag{2}
\]

The order-of-a-power formula gives

\[
\operatorname{ord}(x^E)
=\frac d{\gcd(d,E)}.
\]

Equations (1) and (2) kill every primary component of \(d\) except for one
factor \(\ell\). Therefore

\[
\operatorname{ord}(x^E)=\ell.
\]

The coordinate of \(x\) equal to \(1\) remains \(1\), while its other
coordinate remains nonidentity because \(x^E\) has order \(\ell\). Hence
\(x^E\) is a positive separator of exact order \(\ell\).

## 3. Exact exponent and size of \(K^E\)

For any \(y\in K\), its order divides \(\lambda\). Equations (1)--(2) show
that \(y^E\) has \(\ell\)-power order dividing

\[
\ell^{H-(C-1)}
=\ell^{H-C+1}.
\]

Every other prime component is killed. Thus \(K^E\) is an
\(\ell\)-group whose exponent is at most this value.

The upper bound is attained. By the definition of
\(H=v_\ell(\lambda)\), some element of the finite group \(K\) has order
whose \(\ell\)-part is \(\ell^H\); otherwise the \(\ell\)-part of the lcm of
all element orders would be smaller. Raising that element to \(E\) leaves
exact \(\ell\)-order

\[
\ell^{H-C+1}.
\]

Therefore

\[
\exp(K^E)=\ell^{H-C+1}
\]

exactly.

Each local projection of \(K^E\) is a cyclic \(\ell\)-subgroup of a
finite-field multiplicative group. Its order equals its exponent and is at
most \(\ell^{H-C+1}\). CRT embeds \(K^E\) into the product of the two local
images, so

\[
|K^E|
\le
\ell^{H-C+1}\ell^{H-C+1}
=\ell^{2(H-C+1)}.
\]

The generator-rank claim follows independently from projection. The
\(p\)-image is cyclic; lift one of its generators to \(K^E\). The kernel of
the \(p\)-projection is a subgroup of the cyclic \(q\)-field group, so it is
cyclic. A lift plus a kernel generator generates \(K^E\). If either group is
trivial, fewer generators suffice. Thus the generator rank is at most two.

## 4. Edge cases

### \(\ell=2\)

The valuation proof is unchanged. The surviving nonidentity component of
\(x^E\) has exact order \(2\), hence is \(-1\) in the relevant odd prime
field. The other component is \(1\), so it remains a positive separator.

### \(C<H\)

The selected separator has order exactly \(\ell\), but other elements can
retain order as large as

\[
\ell^{H-C+1}.
\]

The theorem correctly uses that full primary-image exponent in its size
bound.

### \(C=1\)

Here \(j=e\), so the puncture removes the complete \(\ell\)-part of
\(N-1\) from the exponent \(E\). Thus \(v_\ell(E)=0\), and the powered image
can retain the full \(\ell^H\)-part of \(K\). The stated bound becomes
\(\ell^{2H}\), as required.

### \(C=H=e\)

Here \(j=1\) and \(v_\ell(E)=H-1\). The whole image has exact exponent
\(\ell\), while the selected separator also has order \(\ell\).

### Noncyclic groups and redundant generators

The exact exponent argument uses only element orders and their lcm. The rank
and order bounds use only the two cyclic local projections. No global
cyclicity is assumed. Redundant public generators only create duplicate
edges in the later enumeration.

## 5. The public deterministic scan

The executable procedure first computes

\[
g_i^{N-1}\pmod N
\]

for every public generator. If all results are \(1\), Section 1 proves the
annihilator condition without computing \(\lambda\).

It then enumerates primes \(\ell\le L\), tests whether each divides
\(N-1\), computes

\[
e=v_\ell(N-1),
\]

and for every \(1\le j\le e\) forms

\[
E=(N-1)/\ell^j.
\]

For one exponent, power all public generators. Since the power map is a
homomorphism in this abelian group,

\[
K^E=\langle g_1^E,\ldots,g_m^E\rangle. \tag{3}
\]

Starting with the identity, breadth-first multiply every discovered residue
by all powered generators. Maintain a deterministic visited set and
gcd-test each discovered residue minus one.

### Completeness under the stated promise

Suppose a separator and prime satisfy

\[
\ell\le L,
\qquad
\ell^{2(H-C+1)}\le T.
\]

The selected prime divides

\[
\operatorname{ord}(x)\mid\lambda\mid N-1,
\]

so it appears in the public prime list. Its guaranteed puncture index

\[
j=e-C+1
\]

lies in \(1,\ldots,e\), so the algorithm tries the proof exponent. Sections
2--3 show that the corresponding image contains the separator \(x^E\) and
has at most \(T\) elements. The BFS completes and a public gcd returns a
proper factor.

The promise controls the full quantity

\[
\ell^{2(H-C+1)},
\]

not merely the integer gap \(H-C\). A polynomial bound on the gap alone
would not make this exponential group-size bound polynomial.

### Exact cap, wrong exponents, and inverse-free closure

Stop a trial only when a \((T+1)\)-st distinct residue is found. If the true
subgroup has exactly \(T\) elements, the queue empties after complete
enumeration and the trial is not stopped early.

If a wrong exponent has more than \(T\) image elements, closure cannot occur
within the first \(T\) residues. The extra residue is eventually discovered
and the trial stops. If its image has at most \(T\) elements, it is fully
enumerated and either produces a verified factor or the scan proceeds.

Explicit inverse edges are unnecessary. In a finite group, each inverse
generator is a positive power of that generator, so forward multiplication
reaches the entire subgroup in (3).

## 6. Deterministic bit complexity and information flow

The number of primes at most \(L\) is at most \(L\), and each valuation
\(v_\ell(N-1)\) is \(O(\log N)\). Thus there are

\[
O(L\log N)
\]

puncture trials. Primes through \(L\) can be generated deterministically,
and their valuations in the public integer \(N-1\) can be found by repeated
exact division.

Every exponent is at most \(N-1\), so it has \(O(\log N)\) bits. Repeated
squaring powers the polynomially many generators in polynomial time.

For each trial, before completion or stopping, at most \(T+1\) residues are
stored and at most \(O(mT)\) generator edges are processed. A deterministic
balanced search tree gives polynomial lookup on canonical
\(O(\log N)\)-bit residues. Modular multiplication, equality, and Euclid's
algorithm all have polynomial bit complexity. Storage is
\(O(T\log N)\), apart from polynomial generator, queue, and tree overhead.

When the numerical values \(L,T\), the generator count, and all encodings
are polynomial in \(\log N\), multiplying by the trial count remains
deterministic polynomial total time and storage.

The executable scan uses only

\[
N,\quad L,\quad T,\quad g_1,\ldots,g_m.
\]

It does not use \(p,q,\lambda,x,\operatorname{ord}(x),H\), or \(C\).
Those quantities select one successful public trial only in the proof.

## 7. The \(N=2047\) specialization

The supplied exponent is

\[
\lambda=22.
\]

Since

\[
N-1=2046=22\cdot93,
\]

every public generator passes the annihilator test.

The supplied separator has order \(11\). Choose
\(\ell=11\). Then

\[
e=v_{11}(2046)=1,
\qquad
H=v_{11}(22)=1,
\qquad
C=v_{11}(11)=1.
\]

Thus

\[
j=e-C+1=1,
\qquad
E=2046/11=186.
\]

The general theorem gives

\[
|K^E|
\le 11^{2(1-1+1)}
=121.
\]

The supplied exact phase values can also be verified. One has

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

Thus \(11\) has order \(22\) modulo both primes, so
\(H_0=\langle11\rangle\) is a graph of order \(22\). Also

\[
2^{11}=2048\equiv1\pmod{2047},
\]

so \(2\) has order \(11\) modulo both primes. It is not in \(H_0\), because
\(2\cdot11=22\) is \(-1\) modulo \(23\) but not modulo \(89\). Its coset
therefore has order \(11\).

Adding \(2\) does not enlarge either local image. The \(23\)-image of
\(H_0\) is already the full group of order \(22\). The \(89\)-image has
order \(22\) and contains the unique order-\(11\) subgroup, hence contains
\(2\). Thus \(K/H_0\) is a pure phase group of order \(11\).

For \(E=186\),

\[
\gcd(22,186)=2,
\qquad
\gcd(11,186)=1.
\]

The old graph contracts to order \(11\), while the phase quotient remains
of order \(11\). Their powered factors intersect trivially, giving

\[
|K^E|=11\cdot11=121.
\]

Both local images have order \(11\), while the global group has order
\(121\). Each projection kernel has order \(11\), and their only common
element is the identity. Hence the exact positive-separator count is

\[
(11-1)+(11-1)=20.
\]

All supplied fixed-instance values are correct.

## 8. The public structural split using F89

The initial generator tests decide publicly whether

\[
K^{N-1}=1.
\]

If some generator has nonidentity \((N-1)\)-st power, then this image is
nontrivial. By the supplied F89 theorem, it is the full product of two
cyclic hidden projection images of coprime orders. Any nontrivial such
rectangle contains a positive separator.

This is structural existence, not automatic accessibility. If both local
image orders are large, uniform sampling can have negligible separator
density and complete enumeration can be too large. This branch still needs,
for example, a polynomial local-image bound for sampling or a polynomial
full-image cap for deterministic enumeration.

If every generator has identity \((N-1)\)-st power, then
\(\lambda\mid N-1\) and the puncture theorem applies structurally.
Nevertheless it still needs a supplied separator \(x\), a useful order
prime within the public range \(L\), and a polynomial bound on the complete
primary image size

\[
\ell^{2(H-C+1)}.
\]

The annihilator condition alone supplies none of these promises.

## 9. Scope

The result supplies a public conditional puncture decoder after the
annihilator test. It does not create a separator-bearing subgroup, prove a
bounded primary image on all inputs, or choose a successful prime within a
polynomial public range.

The rank-two and squared-size bounds use exactly two CRT prime components.
No arbitrary-composite reduction is proved. Combining the two structural
branches does not yield a complete factoring algorithm or an all-input
success law.
