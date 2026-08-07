# F78 — feedback expansion has an exact projection-kernel gate and a permanent uniform-density ceiling

**Status:** proof-only candidate. No research computation was run. This is an
exact theorem about direct sign-gcd sampling after monotone block refinement.
It is not a factoring algorithm, a hardness theorem, or a theorem about the
square-class decoder.

## 1. Closest prior result and material difference

P83 gives the exact sign-separator density of one public subgroup and shows
that near-uniform sampling from that subgroup is easy. P78 shows that an
integer endpoint split can enlarge a separator-free old subgroup and place a
factor-bearing element in the enlarged subgroup.

The present candidate conditions on that actual monotone enlargement. It
identifies the exact event created by a split, counts the new positive
separators, and proves a ceiling that applies to **every** later supergroup.
It also covers adaptive near-uniform sampling and pairwise amortization. Thus
it tests the proposed feedback-saturation route at the point where subgroup
growth is supposed to become a factoring signal.

## 2. Setup

Let

\[
N=pq
\]

for distinct odd primes, and identify

\[
G=(\mathbb Z/N\mathbb Z)^\times
  \cong G_p\times G_q.
\]

For a subgroup \(J\le G\), write \(J_p,J_q\) for its two projection
images. A **positive separator** is an element of \(J\) that is \(1\) in
exactly one CRT component. Its canonical integer representative exposes a
proper factor through \(\gcd(x-1,N)\).

Assume that the old block-generated subgroup \(H\le G\) contains no positive
separator, and put \(h=|H|\).

## 3. A separator-free subgroup is a graph

### Lemma 1

Both projection maps

\[
H\longrightarrow H_p,
\qquad
H\longrightarrow H_q
\]

are isomorphisms. In particular,

\[
|H|=|H_p|=|H_q|=h.
\tag{1}
\]

### Proof

The kernel of \(H\to H_p\) consists of the identity and the elements that
are \(1\) modulo \(p\) but not modulo \(q\). The latter elements are exactly
positive separators. The kernel is therefore trivial. The same argument
applies to the other projection. Each projection is surjective onto its
defined image, so both maps are isomorphisms. \(\square\)

Thus \(H\) is the graph of an isomorphism between its two local images. The
old state can be large, while its two hidden components remain perfectly
synchronized.

## 4. Exact transition under an arbitrary monotone enlargement

Let \(K\) be any subgroup with \(H\le K\le G\). Define the three indices

\[
c=[K:H],
\qquad
a=[K_p:H_p],
\qquad
b=[K_q:H_q].
\tag{2}
\]

The projection maps induce surjections

\[
K/H\longrightarrow K_p/H_p,
\qquad
K/H\longrightarrow K_q/H_q.
\]

Consequently, \(a\mid c\) and \(b\mid c\).

### Theorem 2 — exact projection-kernel gate

The number of positive separators in \(K\) is exactly

\[
\boxed{
\frac ca+\frac cb-2.
}
\tag{3}
\]

For uniform \(X\in K\), their exact density is

\[
\boxed{
\delta_+(K)
=\frac{c/a+c/b-2}{ch}
=\frac1{ah}+\frac1{bh}-\frac2{ch}.
}
\tag{4}
\]

In particular, \(K\) contains a positive separator if and only if

\[
\boxed{c>a\quad\text{or}\quad c>b.}
\tag{5}
\]

Strict subgroup expansion \(c>1\) is not sufficient.

### Proof

By (1) and (2),

\[
|K|=ch,
\qquad
|K_p|=ah,
\qquad
|K_q|=bh.
\]

The kernel of \(K\to K_p\) has size \(c/a\), and the kernel of
\(K\to K_q\) has size \(c/b\). Remove the identity from both kernels. The
remaining elements are the two disjoint types of positive separator. This
gives (3). Division by \(|K|=ch\) gives (4). Since \(a,b\mid c\), the count
is positive exactly under (5). \(\square\)

The meaningful event is therefore not growth of \(K/H\). It is a nontrivial
kernel in at least one of the two hidden quotient projections.

## 5. One integer block split is a cyclic instance

Suppose one old unit block \(B\) is split exactly as

\[
B=uv,
\]

where the residue of \(B\) lies in \(H\). Preserving all old blocks through
their descendants gives

\[
K=\langle H,u,v\rangle=\langle H,u\rangle,
\tag{6}
\]

because \(v=Bu^{-1}\) modulo \(N\). Hence \(K/H\) is cyclic. In (2),

* \(c\) is the order of \(uH\) in \(K/H\);
* \(a\) is the order of \(u_pH_p\) in \(K_p/H_p\);
* \(b\) is the order of \(u_qH_q\) in \(K_q/H_q\).

Every element of \(K\) has a unique representation

\[
u^t z,
\qquad
0\le t<c,
\qquad
z\in H.
\tag{7}
\]

For the \(p\)-side kernel, one must have \(a\mid t\). Lemma 1 then gives a
unique old element \(z\in H\) that cancels \(u_p^t\). There are \(c/a\)
such kernel elements, including the identity. The same statement with
\(b\) holds on the \(q\) side.

This gives an exact description of the missing word: a power of the newly
exposed block must be cancelled by one uniquely determined old-subgroup
element in one hidden component. The theorem does not give a public method to
find that power or cancellation word.

## 6. Permanent coset-density ceiling

A probability law on \(G\) is **\(H\)-invariant** if it is constant on every
coset of \(H\). Equivalently, it is an arbitrary mixture of uniform laws on
\(H\)-cosets.

### Theorem 3 — uniform blinding by the old graph stays sparse

Every coset \(yH\) contains at most two positive separators and at most two
negative separators. Therefore every \(H\)-invariant law \(\mu\) satisfies

\[
\boxed{
\Pr_{X\sim\mu}\bigl(
  1<\gcd(X-1,N)<N
  \ \text{or}\
  1<\gcd(X+1,N)<N
\bigr)
\le\frac4h.
}
\tag{8}
\]

### Proof

Fix a coset \(yH\). For each sign \(s\in\{1,-1\}\), the equation

\[
(yx)_p=s,
\qquad x\in H,
\]

has at most one solution because \(H\to H_p\) is injective. The analogous
equation modulo \(q\) also has at most one solution. Thus the union of the
four local sign equations contains at most four points of \(yH\). Some of
these points can coincide or give a global sign, so four is an upper bound
on the proper direct-sign successes. A uniform point of the coset succeeds
with probability at most \(4/h\). Averaging over an arbitrary mixture of
cosets proves (8). \(\square\)

Uniform sampling from every supergroup \(K\ge H\) is \(H\)-invariant. More
precisely, (4) gives

\[
\boxed{\delta_+(K)\le\frac2h.}
\tag{9}
\]

P83's negative-sign formula and \(|K_p|,|K_q|\ge h\) similarly give

\[
\boxed{\delta_-(K)\le\frac2h.}
\tag{10}
\]

This ceiling is permanent. It does not depend on how large \(K/H\) becomes.
If \(h\) is exponential in \(\log N\), every \(H\)-invariant sampler remains
exponentially sparse for the two direct sign tests.

## 7. Adaptive near-invariant sampling and amortization

Consider an adaptive sequence. At trial \(t\), conditional on the full prior
transcript, suppose the sample law is within total-variation distance
\(\varepsilon_t\) of some \(H\)-invariant law. Then

\[
\Pr(\text{a sign gcd succeeds at trial }t\mid\text{history})
\le \frac4h+\varepsilon_t.
\tag{11}
\]

For \(T\) trials, with arbitrary dependence through the transcript,

\[
\boxed{
\Pr(\text{some sign gcd succeeds})
\le \frac{4T}{h}+\sum_{t=1}^T\varepsilon_t.
}
\tag{12}
\]

This follows from Theorem 3, the defining event bound for total variation,
conditional expectation, and a union bound.

Pairwise amortization is a special case. If \(X\) is uniform on \(H\),
and \(Y\) is any independent group-valued random variable, then every law of
\(X^{\pm1}Y^{\pm1}\) is \(H\)-invariant. If \(Y\) is uniform on a
supergroup \(K\ge H\), these laws are uniform on \(K\). Ratios of two
independent uniform \(K\)-samples are also uniform on \(K\). Testing
a fixed or predictable polynomial list of such pairs, or all distinct pairs
from a polynomial-size independent pool, only multiplies the ceiling by the
number of tested pairs. An arbitrary value-dependent pair selector is outside
this statement because conditioning can change the pair law.

## 8. Sharp abstract family

For \(L>2\), write the cyclic group \(C_L\) additively and let

\[
H=\{(t,t):t\in C_L\}\le C_L\times C_L.
\]

Then \(H\) is separator-free and \(|H|=L\). Choose nonzero \(u,v\in C_L\)
such that \(v-u\) generates \(C_L\), and adjoin

\[
z=(u,v).
\]

The element \(z\) is not itself a separator, but

\[
K=\langle H,z\rangle=C_L\times C_L.
\]

Here

\[
c=L,
\qquad
a=b=1,
\]

so the expansion is maximal while

\[
\delta_+(K)=\frac{2L-2}{L^2}=\Theta(1/L).
\tag{13}
\]

The explicit cancellation is

\[
z+(-u,-u)=(0,v-u).
\]

This is an abstract group example. It is not asserted to arise from a
canonical-inverse block split on an infinite integer family, and it proves no
computational lower bound.

## 9. Algorithmic consequence and remaining gap

The theorem changes the interpretation of feedback saturation.

* Raw block growth, relation-lattice growth, and subgroup growth are not the
  correct progress measures.
* The exact group event is kernel growth in a hidden quotient projection:
  \(c/a>1\) or \(c/b>1\).
* Even maximal kernel growth can leave uniform success density exponential
  because the old synchronized subgroup contributes the denominator \(h\).
* A dense random-exponent sampler and polynomially many pairwise relations do
  not repair that density.

Feedback remains live through operations outside this ceiling: a public
nonuniform rule that targets the cancellation word in (7), a direct integer
overlap that factors before subgroup sampling, a new square-class closure
with a non-global root, or further refinement that exposes a short public
separator. P81's fixed \(N=4033\) support-two word is an example of targeted
access, not evidence for a uniform-density theorem.

No public algorithm is known here for computing the hidden indices
\(a,b,c\), locating their kernel words, or proving that canonical feedback
creates accessible words on every composite input. The feedback route is not
closed, and no classical polynomial-time factoring algorithm follows.
