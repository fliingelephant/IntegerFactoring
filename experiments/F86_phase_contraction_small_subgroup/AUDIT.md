# PASS

The audited candidate has SHA-256

~~~text
c54aaf5c96abf1546150597251972521a81605e29bbb4fd13df87f5819ceae23
~~~

which matches the pinned digest.

I found no mathematical or complexity defect. The pure-phase
decomposition, powered-image formulas, punctured exponent, capped
enumeration, and fixed \(2047\) specialization are all correct. Two wording
details are noted at the end, but neither changes a theorem.

## 1. Pure-phase decomposition and the divisibility \(c\mid h\)

Let

\[
H=\{(x,\varphi(x)):x\in H_p\}
\]

and suppose

\[
K_p=H_p,\qquad K_q=H_q.
\]

Define

\[
\Delta:K\longrightarrow H_q,\qquad
\Delta(x,y)=y\varphi(x)^{-1}.
\]

The map is a homomorphism. Its kernel is exactly the old graph \(H\).
Its image is

\[
D=K\cap(\{1\}\times H_q),
\]

because multiplying \((x,y)\) by the unique old element
\((x,\varphi(x))^{-1}\) gives \((1,\Delta(x,y))\), and every vertical
element of \(K\) is obtained in this way. Thus

\[
K/H\cong D.
\]

Every subgroup of the cyclic group \(H_q\) is cyclic. Therefore \(D\) and
\(K/H\) are cyclic, and

\[
c=|D|\mid |H_q|=h.
\]

The intersection of \(H\) with \(\{1\}\times D\) is the identity, since the
old graph has injective \(p\)-projection. Every \(k\in K\) has the displayed
old-graph times vertical decomposition, so

\[
K=H\cdot(\{1\}\times D)
\]

is an internal direct product. Lemma 1 is exact.

### The edge case \(h=1\)

If \(h=1\), then \(D\le H_q=\{1\}\), so \(c=1\) and \(K=H\). A strict pure
phase extension cannot exist. The hypotheses of Theorem 3 are therefore
inconsistent in this edge case, making its conclusion vacuous rather than
false.

## 2. Whole-subgroup powering

For a cyclic group of order \(n\), the image of the \(M\)-power map has
order

\[
\frac n{\gcd(n,M)}.
\]

Hence

\[
|H^M|=h_M,\qquad |D^M|=c_M.
\]

The graph isomorphism induces

\[
\varphi_M:H_p^M\longrightarrow H_q^M,\qquad
\varphi_M(x^M)=\varphi(x)^M.
\]

This is well-defined: if \(x^M=x'^M\), then
\(\varphi(xx'^{-1})^M=1\). Its inverse is induced by
\(\varphi^{-1}\). Thus \(H^M\) remains a graph of order \(h_M\).

Because the ambient group is abelian, the power map is a homomorphism.
Applying it to the direct product from Lemma 1 gives

\[
K^M=H^M\cdot(\{1\}\times D^M).
\]

Also \(D^M\le H_q^M\), since \(D\le H_q\). The graph \(H^M\) has no
nonidentity vertical element, so the displayed factors still intersect
trivially. It follows that

\[
|K^M|=h_Mc_M.
\]

The \(p\)-projection is \(H_p^M\). The \(q\)-projection is
\(H_q^M D^M=H_q^M\). Both have order \(h_M\), so the powered state has no
local-image growth.

The divisibility \(c_M\mid h_M\) also follows either from
\(D^M\le H_q^M\) or prime by prime from \(c\mid h\).

### Separator count

Relative to \(H^M\), the global index is \(c_M\), while both local indices
are \(1\). The exact quotient-kernel formula gives

\[
(c_M-1)+(c_M-1)=2c_M-2
\]

positive separators. Division by \(h_Mc_M\) gives

\[
\frac{2(c_M-1)}{c_Mh_M}.
\]

These formulas remain valid when \(c_M=1\), giving zero separators. The
candidate only invokes a positive count when \(c_M>1\).

An arbitrary or wrong exponent can kill the vertical phase group completely,
so \(K^M=H^M\). The phrase “again a pure phase extension” must therefore be
read in the non-strict sense of equal local images; it need not remain a
strict extension. The explicit \(c_M>1\) condition and all subsequent uses
already enforce this distinction.

## 3. The punctured-lcm construction

The condition

\[
\sigma(h)\le B
\]

means that every complete prime-power component
\(r^{v_r(h)}\) is at most \(B\). This is equivalent to

\[
h\mid M_B.
\]

Since the extension is strict, \(c>1\). Choose a prime
\(\ell\mid c\), and write

\[
H_\ell=v_\ell(h),\quad
C_\ell=v_\ell(c),\quad
e=v_\ell(M_B).
\]

The relation \(c\mid h\mid M_B\) gives

\[
1\le C_\ell\le H_\ell\le e.
\]

The candidate chooses

\[
j=e-C_\ell+1.
\]

This satisfies \(1\le j\le e=\lfloor\log_\ell B\rfloor\), so

\[
E=M_B/\ell^j
\]

is genuinely in the public bank. Its \(\ell\)-valuation is
\(C_\ell-1\). For every other prime, its valuation is still at least the
corresponding valuation of \(h\), and hence of \(c\).

It follows exactly that

\[
\begin{aligned}
c_E
&=\frac{c}{\gcd(c,E)}
=\ell,\\
h_E
&=\frac{h}{\gcd(h,E)}
=\ell^{H_\ell-C_\ell+1}.
\end{aligned}
\]

Since

\[
\ell^{H_\ell-C_\ell+1}\le\ell^{H_\ell}\le B
\quad\text{and}\quad
\ell\le B,
\]

one gets

\[
|K^E|=c_Eh_E=\ell h_E\le B^2.
\]

The exact separator count is \(2\ell-2\), and its density is

\[
\frac{2(\ell-1)}{\ell h_E}
\ge\frac1{h_E}
\ge\frac1B.
\]

The first inequality includes \(\ell=2\), where it is equality. Thus the
smallest-prime edge case is sound.

### Prime-power edge cases

The valuation proof does not assume that \(c\) or \(h/c\) is squarefree.
For example, if the entire \(r\)-part of \(c\) is \(r^C\), the puncture
leaves exponent valuation \(C-1\), so the powered quotient has order exactly
\(r\), irrespective of the larger \(r\)-power in \(h\). If \(C=H\), then
\(h_E=r\); if \(C=1\), then \(h_E=r^H\). Both are covered by the bound
\(h_E\le B\).

Other prime components of \(c\) and \(h\) are killed because they divide
\(E\). Multiple prime divisors of \(c\) therefore cause no problem.

The bank has at most one exponent for each prime power at most \(B\), plus
\(M_B\), so its size is at most \(B+1\). Also

\[
M_B\le B!,
\qquad
\log_2M_B=O(B\log B).
\]

Every punctured exponent has no greater bit length.

## 4. Completeness of the capped BFS

Let the public generators be \(g_1,\ldots,g_s\). Since the ambient unit
group is abelian, powering is a homomorphism and

\[
K^E=\langle g_1^E,\ldots,g_s^E\rangle.
\]

Thus the powered public generators generate exactly the desired image, not
merely a subset.

Starting from the identity and repeatedly multiplying by each powered
generator reaches the whole subgroup. Explicit inverse edges are not
needed: in a finite group, the inverse of each generator is a positive power
of that generator. Redundant generators, identity generators, and multiple
generators only add duplicate edges.

Maintain a queue and a deterministic visited set. Before a cap is exceeded,
at most \(B^2+1\) residues are stored or processed, and each processed
residue has \(s\) outgoing multiplications. If the queue empties with at
most \(B^2\) residues, closure is complete. If the true subgroup has more
than \(B^2\) elements, closure cannot occur below the cap, so an additional
residue is eventually discovered and this exponent stops. Hence a wrong
exponent cannot cause unbounded work.

For the exponent from Theorem 3, the subgroup has at most \(B^2\) elements.
The BFS therefore completes, visits every one of its
\(2\ell-2>0\) positive separators, and one of the public gcd tests returns a
proper factor.

### Bit complexity

There are \(O(B)\) bank exponents. Each has \(O(B\log B)\) bits. Repeated
squaring powers every one of the polynomially many public generators in
polynomial time. For each exponent, the capped BFS uses

\[
O(sB^2)
\]

modular multiplications and polynomially many deterministic equality or
ordered-set operations on \(O(\log N)\)-bit residues. Its storage is
\(O(B^2\log N)\) bits, plus the generator and exponent lists. Euclid's
algorithm tests every visited residue in polynomial bit complexity.

If the numerical value of \(B\), the generator count, and their total
encodings are polynomial in \(\log N\), multiplying these bounds by the
bank size remains deterministic polynomial total time and storage.

No hidden order or quotient index is needed: the algorithm tries the full
bank and recognizes success only through a public proper gcd. It is
conditional on the pure-phase and \(\sigma(h)\) hypotheses, but it need not
test those hypotheses.

## 5. Independent check of the \(N=2047\) instance

The factorization is

\[
2047=23\cdot89.
\]

Modulo both primes, \(11\) has order \(22\):

\[
11^{11}\equiv-1\pmod{23},
\qquad
11^{11}\equiv-1\pmod{89}.
\]

For example, modulo \(23\),

\[
11^2\equiv6,\quad
11^8\equiv8,\quad
11^{10}\equiv2,
\]

and modulo \(89\),

\[
11^2\equiv32,\quad
11^4\equiv45,\quad
11^8\equiv67,\quad
11^{10}\equiv8.
\]

Thus the old graph has

\[
h=22.
\]

Also,

\[
2^{11}=2048\equiv1\pmod{2047},
\]

and \(2\ne1\), so \(2\) has order \(11\) modulo each prime. It is not in the
old graph: \(2\cdot11=22\) is \(-1\) modulo \(23\) but not modulo \(89\).
Therefore the nontrivial coset \(2H\) has prime order

\[
c=11.
\]

The local images do not grow. Modulo \(23\), \(H_p\) is the full group of
order \(22\). Modulo \(89\), the order-\(22\) subgroup \(H_q\) contains the
unique order-\(11\) subgroup, and \(2\) lies in it. Hence this is indeed a
pure phase extension.

Since

\[
\sigma(22)=11,
\]

take \(B=11\). One has

\[
M_{11}
=2^3\cdot3^2\cdot5\cdot7\cdot11
=27720,
\]

so the bank contains

\[
E=M_{11}/11=2520.
\]

Directly,

\[
\gcd(22,2520)=2,
\qquad
\gcd(11,2520)=1.
\]

Therefore

\[
h_E=22/2=11,\qquad
c_E=11,\qquad
|K^E|=121.
\]

The exact positive-separator count is

\[
2c_E-2=20.
\]

Because the local order of \(2\) is the same odd number \(11\) at both
primes, every pure power of \(2\) has synchronized positive status, and
neither local subgroup contains \(-1\). Pure powers of \(2\) cannot give
either direct-sign factor, while complete enumeration of \(K^E\) does.

All fixed-instance claims are correct.

## 6. Scope and presentation notes

The result is conditional in all the necessary places. It does not provide
a public test for the pure-phase branch, prove the bound
\(\sigma(h)\le B\), or show that feedback creates such a state with useful
frequency. It gives a deterministic factorer only after those hypotheses
hold and public generators of \(K\) are supplied. It does not extend to
mixed expansions with growing local images.

Two presentation details do not affect the mathematics:

1. The phrase “again a pure phase extension” in Lemma 2 is non-strict when
   \(c_M=1\). If the earlier strict terminology is imported, it should read
   “a possibly trivial pure-phase extension.” The formulas and theorem
   already handle this edge case correctly.
2. The expression rendered as \(\ellmid c\) in Theorem 3 is an evident TeX
   typo for \(\ell\mid c\).

Subject to those readings, the proof and exact scope pass.
