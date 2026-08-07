# PASS

The SHA-256 digest of the reconstruction statement is

~~~text
f4647ddba86b2ff7ce85936f8fd977158f78ece9d2ef55692fac01213eb5494f
~~~

It matches the pinned digest. Every theorem, algorithmic claim, edge case,
and fixed \(N=2047\) specialization is correct.

## 1. Consequence of the full prime-power bound

For an integer \(a>1\), interpret

\[
\sigma(a)=\max_{r\mid a,\ r\ {\rm prime}}r^{v_r(a)}
\]

as its largest complete prime-power component. The condition

\[
\sigma(\lambda)\le B
\]

is equivalent to

\[
\lambda\mid M_B.
\]

Indeed,

\[
v_r(M_B)=\lfloor\log_rB\rfloor,
\]

so \(r^{v_r(\lambda)}\le B\) exactly when
\(v_r(\lambda)\le v_r(M_B)\), for every prime \(r\mid\lambda\).

Since \(K\) contains a positive separator, \(K\) and its exponent are
nontrivial.

## 2. The witness exponent

Choose a positive separator \(x\in K\). Its order

\[
d=\operatorname{ord}(x)
\]

is greater than \(1\) and divides \(\lambda\). Choose a prime
\(\ell\mid d\), and put

\[
C=v_\ell(d),\qquad
H=v_\ell(\lambda),\qquad
e=v_\ell(M_B).
\]

The divisibilities \(d\mid\lambda\mid M_B\) give

\[
1\le C\le H\le e.
\]

Set

\[
j=e-C+1,
\qquad
E=M_B/\ell^j.
\]

Then

\[
1\le j\le e=\lfloor\log_\ell B\rfloor.
\]

Also \(\ell\le B\), because
\(\ell^H\le\sigma(\lambda)\le B\). Thus \(E\) is one of the declared bank
exponents, and

\[
v_\ell(E)=C-1. \tag{1}
\]

For every prime \(r\ne\ell\), the exponent \(E\) retains the full
\(r\)-part of \(M_B\), so

\[
v_r(E)\ge v_r(\lambda)\ge v_r(d). \tag{2}
\]

The order of a power of a finite-order element is

\[
\operatorname{ord}(x^E)
=\frac d{\gcd(d,E)}.
\]

Equations (1) and (2) show that every prime component of \(d\) is killed
except for one factor \(\ell\). Therefore

\[
\operatorname{ord}(x^E)=\ell.
\]

If \(x=(1,x_q)\), then \(x^E=(1,x_q^E)\). The second component is
nonidentity because the global order is \(\ell\). Thus \(x^E\) is still a
positive separator. The case \(x=(x_p,1)\) is symmetric.

This proves that the witness exponent preserves a separator without needing
the separator to have prime-power order.

## 3. Structure and size of the powered image

For any \(y\in K\), its order divides \(\lambda\). Formula (2) kills every
prime component of \(\operatorname{ord}(y)\) other than \(\ell\).
At \(\ell\), equation (1) leaves at most

\[
\ell^{H-(C-1)}
=\ell^{H-C+1}.
\]

Hence \(K^E\) is an \(\ell\)-group with exponent at most

\[
L_\ell=\ell^{H-C+1}.
\]

Since \(H-C+1\le H\),

\[
L_\ell\le\ell^H\le B. \tag{3}
\]

This argument uses only the exponent of \(K\); it does not assume that
\(K\) is cyclic.

Each CRT projection of \(K^E\) is a subgroup of a finite-field
multiplicative group, hence cyclic. A cyclic group whose exponent is at most
\(L_\ell\) has order at most \(L_\ell\). Therefore

\[
|(K^E)_p|\le L_\ell,
\qquad
|(K^E)_q|\le L_\ell.
\]

CRT projection embeds \(K^E\) in the product of these two images, so

\[
|K^E|
\le |(K^E)_p|\,|(K^E)_q|
\le L_\ell^2
\le B^2.
\]

The image contains the positive separator \(x^E\). This proves the main
theorem.

## 4. Edge cases in the exponent argument

### Noncyclic \(K\) and redundant generators

Only element orders dividing \(\lambda\), cyclicity of the two local
images, and the injective CRT map are used. The global subgroup can be
noncyclic. Repeated or redundant public generators do not change \(K\), its
power image, or the proof.

### Mixed-order separators

The order \(d\) of \(x\) can contain arbitrarily many distinct primes.
The exponent \(E\) contains every non-\(\ell\) component of
\(\lambda\), and hence of \(d\). Those components all disappear from
\(x^E\); exactly one \(\ell\)-layer remains.

### The case \(C<H\)

Other elements of \(K^E\) can retain an \(\ell\)-power larger than
\(\ell\). The proof does not claim that the whole image has exponent
\(\ell\). It gives the exact upper bound

\[
\ell^{H-C+1}\le B,
\]

while the selected separator itself has exact order \(\ell\).

### The case \(\ell=2\)

The same valuation calculation leaves \(x^E\) of exact order \(2\). Its
identity component remains \(1\), and its other component is the unique
order-two element \(-1\) of the relevant odd prime field. It is still a
positive separator. The local cyclic-image and \(B^2\) bounds are
unchanged.

### The case \(B=1\)

A positive separator has order greater than \(1\), so
\(\lambda>1\) and \(\sigma(\lambda)\ge2\). The simultaneous promises
\(\sigma(\lambda)\le1\) and “\(K\) contains a separator” are impossible.
The theorem is vacuous for \(B=1\); there is no missing witness exponent.

### A bank prime equal to a hidden factor

It is possible that the selected order prime \(\ell\) equals one of
\(p,q\) while dividing the multiplicative order in the other field. The
group proof still works; the characteristic-\(\ell\) projection is then
trivial. Operationally, the public gcd \(\gcd(\ell,N)\) would already expose
that factor.

## 5. Completeness of the public capped enumeration

Let the public generators be \(g_1,\ldots,g_s\). The ambient unit group is
abelian, so the \(E\)-power map is a homomorphism and

\[
K^E=\langle g_1^E,\ldots,g_s^E\rangle. \tag{4}
\]

Thus powering the public generators gives a complete generator list for the
image.

For one bank exponent, start with the identity and repeatedly multiply each
visited residue by every powered generator. Maintain a queue and a
deterministic visited set. Inverses need not be explicit: in a finite group,
the inverse of each generator is a positive power of that generator, so
forward multiplication reaches the entire generated subgroup.

If the queue empties after at most \(B^2\) residues, the subgroup has been
enumerated completely. If the subgroup has more than \(B^2\) elements, the
queue cannot close below that size. A \((B^2+1)\)-st distinct residue is
eventually found, and the algorithm stops that exponent immediately.
Therefore a wrong exponent cannot force unbounded enumeration.

For the exponent proved in Sections 2--3, the subgroup has at most \(B^2\)
elements. Its enumeration completes, includes \(x^E\), and the public test

\[
\gcd(x^E-1,N)
\]

returns a proper factor. Since the algorithm tries the whole bank, it does
not need to know which separator, prime, or exponent the proof selected.

A wrong exponent with a small image but no separator is fully enumerated
and then rejected. A wrong exponent with a large image is stopped by the
cap. Either behavior is bounded.

## 6. Deterministic bit complexity

The pairs \((\ell,j)\) in the bank correspond to prime powers
\(\ell^j\le B\), so the bank has \(O(B)\) elements. Also,

\[
M_B\le B!,
\qquad
\log_2M_B=O(B\log B).
\]

All punctured exponents have at most this bit length. The lcm and the bank
can be constructed deterministically by polynomially many gcd, lcm, and
integer-division operations when the numerical value of
\(B\) is polynomial in \(\log N\).

For each bank exponent, repeated squaring powers every public generator in
time polynomial in \(\log N\) and \(\log E\). Before stopping or completing,
the BFS stores at most \(B^2+1\) residues and processes at most that many
vertices. With \(s\) generators, it performs

\[
O(sB^2)
\]

modular multiplications per exponent. Deterministic membership lookup can
use a balanced search tree on canonical \(O(\log N)\)-bit residues. Every
visited residue is tested by Euclid's algorithm.

Multiplication by the \(O(B)\) bank size remains polynomial because \(B\),
the generator-list size, and the generator encodings are polynomial in
\(\log N\). Storage is polynomial as well.

The executable procedure uses only

\[
N,\quad B,\quad\text{and the public generator list}.
\]

It does not use \(\lambda\), the selected element \(x\), any element order,
the hidden primes, or either local projection. Those objects occur only in
the completeness proof.

## 7. Verification of the \(N=2047\) specialization

The factorization is

\[
2047=23\cdot89,
\]

with both factors prime.

Modulo \(23\),

\[
11^2\equiv6,\quad
11^8\equiv8,\quad
11^{10}\equiv2,\quad
11^{11}\equiv-1.
\]

Modulo \(89\),

\[
11^2\equiv32,\quad
11^4\equiv45,\quad
11^8\equiv67,\quad
11^{10}\equiv8,\quad
11^{11}\equiv-1.
\]

Thus \(11\) has order \(22\) modulo both primes and globally.

Also,

\[
2^{11}=2048\equiv1\pmod{2047},
\]

so \(2\) has order \(11\) modulo both primes. It is not in
\(H=\langle11\rangle\): the public word

\[
2\cdot11=22
\]

is \(-1\) modulo \(23\) but not modulo \(89\), whereas the old graph
synchronizes negative signs.

The local image of \(H\) modulo \(23\) is the full order-\(22\) group.
Modulo \(89\), its order-\(22\) image contains the unique subgroup of order
\(11\), which contains \(2\). Hence adjoining \(2\) changes neither local
image, while the nontrivial coset \(2H\) has order \(11\). Therefore

\[
|K:H|=11,
\qquad
|H|=22,
\qquad
|K|=242.
\]

Both local images have exponent \(22\), and \(K\) contains the element
\(11\) of order \(22\). Consequently

\[
\lambda=\exp(K)=22.
\]

Its complete prime-power components are \(2\) and \(11\), so

\[
\sigma(\lambda)=11.
\]

For \(B=11\),

\[
M_{11}
=2^3\cdot3^2\cdot5\cdot7\cdot11
=27720,
\qquad
E=M_{11}/11=2520.
\]

Powering the old graph gives

\[
|H^E|=\frac{22}{\gcd(22,2520)}=11.
\]

The phase quotient of order \(11\) is preserved because

\[
\gcd(11,2520)=1.
\]

The powered graph and powered phase subgroup intersect trivially, so

\[
|K^E|=11\cdot11=121.
\]

Both local projection images now have order \(11\), while the global group
has order \(121\). Each projection kernel has order \(11\). Removing the
shared identity from the two kernels yields

\[
(11-1)+(11-1)=20
\]

positive separators.

All fixed values and counts are correct.

## 8. Scope

The result is a deterministic decoder under two promises:

1. the supplied public subgroup already contains a positive separator; and
2. every complete prime-power component of its exponent is at most the
   declared polynomial bound \(B\).

It neither creates such a subgroup nor verifies either promise. It does not
prove that feedback supplies one with useful probability. The \(B^2\) bound
uses exactly two CRT components; with more components the direct product
bound changes. No all-input factoring algorithm follows.

Finally, \(\sigma(\lambda)\le B\) is sufficient for this punctured-lcm bank.
It is not claimed to be necessary for a different exponent family,
different decoder, or a particular favorable subgroup.
