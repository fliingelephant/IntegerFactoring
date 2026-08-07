# F90 — a public annihilator makes every bounded primary separator enumerable

**Status:** proof-only candidate. No research computation was run. This is a
conditional deterministic decoder for a supplied subgroup killed by
\(N-1\), not a separator source or an all-input factoring algorithm.

## 1. Material difference

P94 uses punctures of \(N-1\) for a strict pure phase extension and obtains
an exact small-image formula from that special structure. F89 shows that the
unpunctured power \(N-1\) sends every subgroup to a rectangular coprime-order
state.

The present result handles the complementary public branch

\[
K^{N-1}=1
\]

without assuming a graph subgroup, a pure phase extension, or a known old
order. In this branch, \(N-1\) is a public multiple of the entire subgroup
exponent. If the supplied subgroup contains any positive separator, one
prime-power puncture preserves a separator and kills every other primary
component. The surviving group has rank at most two and an exact public cap
condition.

## 2. Setup and public annihilator test

Let

\[
N=pq
\]

for distinct odd primes, and let

\[
K\le(\mathbb Z/N\mathbb Z)^\times
\]

be given by public generators \(g_1,\ldots,g_m\). Put

\[
\lambda=\exp(K).
\]

The condition

\[
g_i^{N-1}=1\pmod N
\qquad(1\le i\le m)
\tag{1}
\]

is public and is equivalent to

\[
\boxed{\lambda\mid N-1.}
\tag{2}

Indeed, (1) kills every word in the generators, while (2) kills every group
element.

Assume that \(K\) contains a positive separator \(x\): exactly one hidden
coordinate of \(x\) is one.

## 3. Primary puncture theorem

Choose a prime

\[
\ell\mid\operatorname{ord}(x),
\]

and put

\[
e=v_\ell(N-1),
\qquad
H=v_\ell(\lambda),
\qquad
C=v_\ell(\operatorname{ord}(x)).
\tag{3}

Condition (2) gives

\[
1\le C\le H\le e.
\]

Define

\[
j=e-C+1,
\qquad
E=\frac{N-1}{\ell^j}.
\tag{4}

### Theorem 1

The element \(x^E\) is a positive separator of exact order \(\ell\). The
powered subgroup \(K^E\) is an \(\ell\)-group of exponent

\[
\boxed{\ell^{H-C+1}.}
\tag{5}

It has generator rank at most two and therefore

\[
\boxed{|K^E|\le\ell^{2(H-C+1)}.}
\tag{6}

### Proof

Equation (4) gives

\[
v_\ell(E)=C-1.
\]

For every prime \(r\ne\ell\), the exponent \(E\) retains the full
\(r\)-valuation of \(N-1\), which is at least \(v_r(\lambda)\). Thus the
power kills every non-\(\ell\) component of \(K\).

On the \(\ell\)-primary component, the part of \(E\) coprime to \(\ell\)
acts as an automorphism, and the factor \(\ell^{C-1}\) lowers the subgroup
exponent from \(\ell^H\) to \(\ell^{H-C+1}\). The same calculation lowers
the \(\ell\)-part of \(x\)'s order from \(\ell^C\) to \(\ell\), while all
other parts of its order disappear. Powering preserves its identity
coordinate, so \(x^E\) remains a separator.

Each local unit group is cyclic. Hence every \(\ell\)-subgroup of their
product has generator rank at most two. A rank-at-most-two abelian group of
exponent \(\ell^{H-C+1}\) has order at most the square in (6). \(\square\)

The theorem includes \(\ell=2\), \(C<H\), redundant public generators, and
noncyclic \(K\).

## 4. Public deterministic decoder

Fix public numerical bounds \(L,T\). First test (1). If it fails, use the
rectangular branch of F89 or another decoder. If it holds, do the following.

For every prime \(\ell\le L\) dividing \(N-1\):

1. compute \(e=v_\ell(N-1)\);
2. for every \(1\le j\le e\), set
   \(E=(N-1)/\ell^j\);
3. power every generator of \(K\) by \(E\);
4. enumerate the generated subgroup by breadth-first multiplication;
5. gcd-test every visited residue minus one; and
6. stop the current enumeration after more than \(T\) distinct residues.

### Corollary 2

The scan deterministically factors \(N\) if \(K\) contains a positive
separator \(x\) and some prime \(\ell\mid\operatorname{ord}(x)\) satisfies

\[
\boxed{
\ell\le L,
\qquad
\ell^{2(H-C+1)}\le T,
}
\tag{7}

with \(H,C\) as in (3).

### Proof

The public loop includes the hidden witness depth \(j=e-C+1\). For this
depth, Theorem 1 gives a subgroup of at most \(T\) elements containing the
separator \(x^E\). The breadth-first queue therefore closes before the cap
and visits that separator. Its gcd returns a proper factor. Every wrong
trial is bounded by the same cap. \(\square\)

The algorithm does not know \(x,\ell,H,C,\lambda,p\), or \(q\). These
quantities only prove that one public trial succeeds. There are at most
\(L\) candidate integers and fewer than \(\log_2N\) punctures for each.
Every exponent has \(O(\log N)\) bits. For numerical
\(L,T=\operatorname{poly}(\log N)\), polynomially many public generators,
and polynomial generator encodings, the complete scan has deterministic
polynomial bit complexity and storage.

The cap condition in (7) concerns the full exponential expression. A raw
gap \(H-C\) that is only polynomial in \(\log N\) is not sufficient when
\(\ell\) is large.

## 5. The 2047 phase state needs no branch knowledge

For

\[
N=2047,
\qquad
K=\langle11,2\rangle,
\]

one has

\[
\lambda=22\mid2046=N-1.
\]

Thus the public annihilator test passes. The subgroup contains positive
separators of order 11. Choose such an \(x\). Then

\[
\ell=11,
\qquad
e=H=C=1,
\qquad
E=(N-1)/11=186.
\]

Theorem 1 gives

\[
|K^E|\le11^2=121.
\]

The retained exact phase calculation shows equality and 20 positive
separators. The public algorithm need not recognize that the state is pure
phase. It only checks that all supplied generators are killed by \(N-1\)
and runs the puncture scan.

P94 remains sharper when the pure phase structure is available for proof:
its exact size is \(\ell^{H_\ell-C_\ell+2}\), which can be smaller than the
general rank-two bound here.

## 6. Combined public normal form and remaining gap

Together, F89 and this theorem give a public first split for any supplied
subgroup \(K\).

1. If \(K^{N-1}\ne1\), then F89 proves that the powered subgroup is a full
   rectangle with coprime hidden projection orders and contains positive
   separators. It is efficiently decoded when one projection order or the
   full image is polynomially bounded.
2. If \(K^{N-1}=1\), then \(N-1\) is a public annihilator for all of \(K\).
   If \(K\) already contains a separator with a small accessible primary
   component, the puncture scan above finds it.

This is an algorithmic change from selecting one scalar identity. It powers
all public generators, transforms the full subgroup, and completely
enumerates bounded images.

The remaining gap is still source-side. Bare \(N\) and feedback must supply
a subgroup for which the rectangular image is accessible, or for which the
annihilated branch already contains a separator with a bounded primary
image. Neither event has an all-input inverse-polynomial law. No
arbitrary-composite reduction, complete factoring algorithm, lower bound,
or literature novelty is proved.
