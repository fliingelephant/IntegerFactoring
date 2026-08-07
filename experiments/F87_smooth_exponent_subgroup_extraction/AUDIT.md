# F87 hostile proof audit

## Verdict: PASS

I audited `RESULT.md` at the pinned SHA-256

```text
978447b8d1cfcc67beae9446c74168f8636dbc0faa6976285f005bbce5f0fc20
```

The hash matches. I ran no search, replay, or research computation. I found
no counterexample to the punctured-exponent construction, the rank-two size
bound, the capped enumeration, or the fixed \(N=2047\) specialization.

The pass has the candidate's stated scope. This is a conditional decoder for
a supplied subgroup of the unit group of a squarefree semiprime. It neither
creates that subgroup nor proves its exponent smooth. In particular,
\(\sigma(\exp K)\le B\) is a promise used by the proof. The public procedure
does not test it. The phrase “complete executable condition” is correct only
in this promise-problem sense.

## 1. The smoothness condition is exactly the divisibility used

Write

\[
\lambda=\prod_r r^{H_r}.
\]

By definition, \(\sigma(\lambda)\le B\) says that every full prime power
\(r^{H_r}\) occurring in \(\lambda\) is at most \(B\). This is equivalent to

\[
H_r\le \lfloor\log_r B\rfloor=v_r(M_B)
\]

for every \(r\mid\lambda\), and hence to

\[
\lambda\mid M_B.
\]

Thus the hypothesis supplies exactly the divisibility claimed in the proof.
It is sufficient for this bank construction. It is not claimed, and need not
be, a necessary condition for some other exponent or decoder to work.

## 2. The punctured exponent is present and has the required valuations

Let \(x\) be a positive separator. Choose any prime
\(\ell\mid\operatorname{ord}(x)\), and set

\[
C=v_\ell(\operatorname{ord}(x)),\qquad
H=v_\ell(\lambda),\qquad
e=v_\ell(M_B).
\]

Because \(\operatorname{ord}(x)\mid\lambda\mid M_B\),

\[
1\le C\le H\le e.
\]

Therefore \(j=e-C+1\) is an integer in the declared range \(1\le j\le e\),
and

\[
E=M_B/\ell^j
\]

is a bank member. Its valuations are

\[
v_\ell(E)=C-1,
\qquad
v_r(E)=v_r(M_B)\ge v_r(\lambda)\quad(r\ne\ell).
\]

No local order or factor is needed to execute this choice: the algorithm
tries the whole public bank. The separator and \(\ell,C,H\) are only witnesses
that one bank member succeeds.

## 3. The separator survives with exact order \(\ell\)

For a finite-order element,

\[
\operatorname{ord}(x^E)
=
\frac{\operatorname{ord}(x)}
{\gcd(\operatorname{ord}(x),E)}.
\]

The exponent \(E\) contains every non-\(\ell\) primary part of
\(\operatorname{ord}(x)\), while its \(\ell\)-adic valuation is exactly
\(C-1\). Hence

\[
\operatorname{ord}(x^E)=\ell.
\]

If \(x=(1,a)\) in CRT coordinates, then \(x^E=(1,a^E)\). The second
coordinate cannot also be \(1\), because the full element has order
\(\ell>1\). The same argument applies when the identity coordinate is the
second one. Thus \(x^E\) remains a positive separator.

This also covers a separator whose order has several prime factors. The
puncture keeps one order-\(\ell\) component and kills the others. It also
covers \(\ell=2\); no oddness of \(\ell\) is used.

## 4. The whole image is a small \(\ell\)-group

Because \(K\) is abelian, \(y\mapsto y^E\) is a homomorphism and \(K^E\) is
its image. For each \(r\ne\ell\), \(E\) contains the complete \(r\)-primary
part of \(\lambda\), so the map kills the \(r\)-primary component of \(K\).
On the \(\ell\)-primary component, the \(\ell\)-free part of \(E\) is an
automorphism, while multiplication of exponents by \(\ell^{C-1}\) leaves
image exponent at most

\[
L=\ell^{H-C+1}.
\]

This calculation remains valid when \(C<H\). Since
\(\ell^H\le\sigma(\lambda)\le B\), it gives \(L\le B\).

The two local \(\ell\)-Sylow groups are cyclic. Hence \(K^E\) is a subgroup
of a product of two cyclic \(\ell\)-groups. Such a subgroup needs at most two
generators. Equivalently, its invariant-factor decomposition has at most two
nontrivial cyclic factors. Since each factor has order at most its exponent
\(L\),

\[
|K^E|\le L^2
\le \ell^{2H}
\le B^2.
\]

This argument does not assume that \(K\) is cyclic. Redundant public
generators do not change it.

## 5. Capped breadth-first enumeration is complete

If the public generators of \(K\) are \(g_1,\ldots,g_m\), then
\(g_1^E,\ldots,g_m^E\) generate \(K^E\). Breadth-first closure from \(1\)
under multiplication by these residues reaches the full subgroup. Although
inverse generators need not be listed, this causes no gap: in a finite
group, every inverse is a nonnegative power of the same generator.

For the successful \(E\), at most \(B^2\) residues exist. The rule that stops
only after the \((B^2+1)\)-st distinct residue therefore cannot interrupt
this enumeration. It reaches \(x^E\), and

\[
1<\gcd(x^E-1,N)<N.
\]

For every wrong exponent, immediate termination on insertion of the
\((B^2+1)\)-st residue caps the work even if the corresponding subgroup is
large. Testing a proper gcd before return prevents a false output.

The bank has at most \(B+1\) entries: its punctures are indexed by prime
powers at most \(B\). Thus it inserts \(O(B^3)\) residues in total and tests
at most \(O(mB^3)\) generator edges for \(m\) public generators. Modular
powering, group operations, gcd, and deterministic equality lookup all have
polynomial bit complexity when \(B\) and the generator list are polynomial
in \(\log N\). A balanced search tree gives deterministic lookup if hashing
is not assumed.

The algorithm never uses \(\lambda\), an element order, a local projection,
a factor of \(N\), or the identity of the successful exponent. Those values
occur only in the correctness proof.

## 6. Edge cases

- If \(B=1\), the promise forces \(\lambda=1\), so no positive separator can
  exist. The theorem is vacuous, not false.
- If \(C=H\), the image exponent is at most \(\ell\). If \(C<H\), the stated
  bound \(\ell^{H-C+1}\le B\) still holds.
- The proof works for \(\ell=2\).
- A mixed-order separator is reduced to an exact order-\(\ell\) separator.
- A noncyclic image is allowed; semiprime CRT rank gives the two-generator
  bound.
- Redundant or identity powered generators affect only the explicit public
  generator factor in the running time.
- Wrong bank exponents need no algebraic promise because their enumeration
  is capped.

## 7. The fixed \(N=2047\) instance is consistent

The retained F82/F86 certificate gives

\[
N=2047=23\cdot89,
\qquad
K=\langle11,2\rangle,
\qquad
\exp(K)=22.
\]

Here \(\sigma(22)=11\). For \(B=11\),

\[
M_{11}=27720,
\qquad
E=M_{11}/11=2520
\]

is in the bank. The earlier exact group certificate has an order-\(22\)
graph component and an independent order-\(11\) phase quotient. Powering by
\(2520\) removes the order-\(2\) component and preserves both order-\(11\)
directions because

\[
\gcd(22,2520)=2,
\qquad
\gcd(11,2520)=1.
\]

The image therefore has order \(11^2=121\). Its two local kernels each have
order \(11\), so their nonidentity elements give

\[
(11-1)+(11-1)=20
\]

positive separators. This is the claimed F82/P88 specialization.

## 8. Exact scope of the pass

The proof establishes a deterministic polynomial-time extraction procedure
under two promises:

1. a public generated subgroup \(K\le(\mathbb Z/N\mathbb Z)^\times\) already
   contains a positive separator; and
2. every full prime-power component of \(\exp(K)\) is at most the supplied
   polynomial bound \(B\).

It does not show how bare \(N\) creates such a subgroup, how to verify either
promise, or why a polynomial \(B\) works on all inputs. The \(B^2\) bound is
specific to the two cyclic local unit groups of a squarefree semiprime. No
all-input factoring algorithm or novelty claim follows from this audit.

Within those boundaries, the theorem and algorithm pass.
