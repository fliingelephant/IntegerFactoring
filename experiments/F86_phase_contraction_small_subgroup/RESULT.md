# F86 — power contraction makes a bounded pure-phase expansion enumerable

**Status:** proof-only candidate. No research computation was run. This is a
conditional deterministic post-feedback algorithm, not an all-input source
law or a factoring algorithm.

## 1. Material difference

P87 proves that pure powers of a new block cannot handle an equal-order phase
branch. P88 gives a literal canonical-integer phase witness. P84 shows that
uniform sampling from a large enlarged subgroup can remain exponentially
sparse.

The present result applies the power to the **whole enlarged subgroup**, not
only to the new block. In a pure phase expansion, a punctured lcm exponent can
contract the old synchronized graph while preserving one phase component.
Under an exact full-prime-power bound, the resulting factor-bearing subgroup
has polynomial size and can be enumerated completely. No hidden cancellation
word is needed.

## 2. Pure phase extensions are cyclic over the old graph

Let \(N=pq\) for distinct odd primes. Let

\[
H\le(\mathbb Z/N\mathbb Z)^\times
\]

be a diagonal graph state. Thus both local projections are isomorphisms and

\[
H=\{(x,\varphi(x)):x\in H_p\}
\]

for an isomorphism \(\varphi:H_p\to H_q\). Put

\[
h=|H|.
\]

Because \(H_p\) is a subgroup of the cyclic group
\(\mathbb F_p^\times\), the groups \(H_p,H_q,H\) are cyclic of order
\(h\).

Let \(K\ge H\) be a strict **pure phase extension**:

\[
K_p=H_p,
\qquad
K_q=H_q,
\qquad
K\ne H.
\tag{1}
\]

Put \(c=[K:H]\).

### Lemma 1

The quotient \(K/H\) is cyclic and

\[
\boxed{c\mid h.}
\tag{2}
\]

After identifying the old graph, there is a cyclic subgroup
\(D\le H_q\) of order \(c\) such that

\[
\boxed{
K=H\cdot(\{1\}\times D)
}
\tag{3}
\]

with trivial intersection between the two factors.

### Proof

For \(k=(x,y)\in K\), condition (1) gives \(x\in H_p\). There is a unique
old element \(h_x=(x,\varphi(x))\in H\). Thus

\[
kh_x^{-1}=(1,y\varphi(x)^{-1})
\]

lies in \(K\cap(\{1\}\times H_q)\). This gives an isomorphism

\[
K/H\cong D:=K\cap(\{1\}\times H_q).
\]

The group \(D\) is a subgroup of the cyclic group \(H_q\), so it is cyclic
and its order \(c\) divides \(h\). The graph intersects the vertical subgroup
only in the identity, proving (3). \(\square\)

## 3. Exact effect of a whole-subgroup power

For an integer \(M\ge1\), put

\[
H^M=\{x^M:x\in H\},
\qquad
K^M=\{x^M:x\in K\}.
\]

Define

\[
h_M=\frac{h}{\gcd(h,M)},
\qquad
c_M=\frac{c}{\gcd(c,M)}.
\tag{4}
\]

### Lemma 2

The powered old group \(H^M\) is again a graph, of order \(h_M\). The
powered enlarged group again has the same two local images as the powered
old graph; it can become equal to that graph when \(c_M=1\). It satisfies

\[
\boxed{
K^M=H^M\cdot(\{1\}\times D^M),
\qquad
|K^M|=h_Mc_M.
}
\tag{5}
\]

Its local images are exactly \(H_p^M,H_q^M\), both of order \(h_M\). If
\(c_M>1\), the exact number and density of positive separators in \(K^M\)
are

\[
\boxed{2c_M-2},
\qquad
\boxed{
\frac{2(c_M-1)}{c_Mh_M}.
}
\tag{6}
\]

### Proof

Powering commutes with the graph isomorphism, so \(H^M\) is a graph of
order \(h_M\). Equation (3) and commutativity give

\[
K^M=H^M(\{1\}\times D^M).
\]

The group \(D^M\) has order \(c_M\). It lies inside \(H_q^M\), because
\(D\le H_q\). The graph and the vertical factor still intersect trivially,
which proves (5) and the local-image statement.

Relative to the old graph \(H^M\), both local projection indices are one
and the global index is \(c_M\). The quotient-kernel formula therefore gives
\((c_M-1)+(c_M-1)\) positive separators. Division by (5) gives the density.
\(\square\)

## 4. Punctured contraction theorem

For a positive integer \(a\), let

\[
\sigma(a)=\max_{\ell^e\mid a}\ell^e,
\qquad
\sigma(1)=1,
\]

be its largest full prime-power divisor. Let

\[
M_B=\operatorname{lcm}(1,\ldots,B)
\]

and use the punctured bank

\[
\mathcal E_B
=
\{M_B\}
\cup
\left\{
\frac{M_B}{\ell^j}:
\ell\le B\text{ prime},\
1\le j\le\lfloor\log_\ell B\rfloor
\right\}.
\tag{7}
\]

### Theorem 3

Assume

\[
K\ne H
\qquad\text{and}\qquad
\sigma(h)\le B.
\tag{8}
\]

Then some exponent \(E\in\mathcal E_B\) satisfies

\[
\boxed{
c_E=\ell,
\qquad
h_E\le B,
\qquad
|K^E|\le B^2
}
\tag{9}
\]

for a prime \(\ell\mid c\). The group \(K^E\) contains exactly
\(2\ell-2\) positive separators, with density at least \(1/B\).

### Proof

Condition \(\sigma(h)\le B\) is equivalent to \(h\mid M_B\). Choose any
prime \(\ell\mid c\), and write

\[
H_\ell=v_\ell(h),
\qquad
C_\ell=v_\ell(c),
\qquad
e=v_\ell(M_B).
\]

By (2),

\[
1\le C_\ell\le H_\ell\le e.
\]

Set

\[
j=e-C_\ell+1,
\qquad
E=\frac{M_B}{\ell^j}.
\tag{10}
\]

This exponent belongs to (7), and

\[
v_\ell(E)=C_\ell-1.
\]

Every other prime-power component of \(h\), and hence of \(c\), divides
\(E\). Therefore

\[
c_E=\ell,
\qquad
h_E=\ell^{H_\ell-C_\ell+1}.
\]

The full prime power \(\ell^{H_\ell}\) is at most \(B\), so

\[
h_E\le B,
\qquad
\ell\le B.
\]

Lemma 2 gives \(|K^E|=\ell h_E\le B^2\), separator count
\(2\ell-2\), and density

\[
\frac{2(\ell-1)}{\ell h_E}
\ge\frac1{h_E}
\ge\frac1B.
\]

This proves (9). \(\square\)

## 5. A deterministic factor-free decoder

Assume public generators for \(K\) are available. For every
\(E\in\mathcal E_B\):

1. raise every generator to \(E\) modulo \(N\);
2. enumerate the generated subgroup by breadth-first closure under these
   powered generators;
3. stop this exponent as soon as more than \(B^2\) distinct residues appear;
4. for every residue \(x\) found, test \(\gcd(x-1,N)\).

For the exponent guaranteed by Theorem 3, the enumeration completes within
the cap and contains a proper factor witness. Wrong exponents can exceed the
cap but cannot exceed the declared work.

The bank has at most \(B+1\) exponents and every exponent has
\(O(B\log B)\) bits. If \(B\), the number of public generators, and their
encodings are polynomial in \(\log N\), the complete capped enumeration uses
deterministic polynomial bit complexity and storage. It uses only public
modular powers, equality tests, multiplication, and gcd. No hidden order,
prime \(\ell\), index, local projection, or cancellation word is executable
input.

Thus (8) gives a deterministic polynomial-time post-feedback factorer for
the pure phase branch.

## 6. The F82 witness is completed by whole-subgroup contraction

For the P88 state at

\[
N=2047,
\qquad
H=\langle11\rangle,
\qquad
K=\langle11,2\rangle,
\]

one has

\[
h=22,
\qquad
c=11,
\qquad
\sigma(h)=11.
\]

Take \(B=11\). The bank contains

\[
E=M_{11}/11=2520.
\]

Then

\[
h_E=11,
\qquad
c_E=11,
\qquad
|K^E|=121.
\]

The contracted subgroup contains 20 positive separators. This succeeds even
though every pure power of the exposed block 2 fails. It answers the exact
scope left by P88: powers of arbitrary mixed elements, implemented here by
powering and enumerating the whole public subgroup, are strictly stronger
than powers of the new block alone.

## 7. Scope

The theorem removes the hidden mixed-word selector only for a pure phase
extension whose old graph order has polynomially bounded full prime-power
components. It does not detect that branch, prove \(\sigma(h)\le B\), or
show that canonical feedback creates such an extension on every input.

If \(h\) contains a prime-power component larger than every polynomial
bound, the bank theorem gives no small subgroup. General order/phase mixtures
with growing local projection images also need separate analysis. No
all-input probability law, complete factoring algorithm, computational lower
bound, or literature novelty is proved.
