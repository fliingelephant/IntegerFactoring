# F89 — powering by N−1 removes every shared local-order component

**Status:** proof-only candidate. The fixed arithmetic examples reuse
previously verified certificates. No search or research computation was run.
This is a public subgroup transformation and a conditional decoder, not an
all-input subgroup source or factoring algorithm.

## 1. Material difference

P94 uses the public multiple \(N-1\) to contract a supplied pure phase
extension. The present result does not assume a graph subgroup, a pure phase
branch, or a known old order.

For every public subgroup modulo a squarefree semiprime, the single public
power \(N-1\) removes all order components that can occur at both hidden
primes. The remaining subgroup is the full direct product of two cyclic
groups of coprime orders. Thus it contains no residual cross-field graph
correlation.

This operation directly completes the known \(N=4033\) feedback chain with
exponent \(N-1=4032\). It kills the \(N=2047\) pure phase state completely,
which explains why P94 must puncture \(N-1\) there.

## 2. Exact rectangularization theorem

Let

\[
N=pq
\]

for distinct odd primes, and let

\[
K\le(\mathbb Z/N\mathbb Z)^\times
\cong\mathbb F_p^\times\times\mathbb F_q^\times
\]

be given by public generators. Put

\[
E=N-1,
\qquad
S=K^E=\{x^E:x\in K\}.
\]

Let

\[
m_p=|K_p|,
\qquad
m_q=|K_q|,
\]

and define the hidden image orders

\[
A=\frac{m_p}{\gcd(m_p,E)},
\qquad
B=\frac{m_q}{\gcd(m_q,E)}.
\tag{1}
\]

### Theorem 1

The two integers in (1) are coprime:

\[
\boxed{\gcd(A,B)=1.}
\tag{2}
\]

Moreover,

\[
\boxed{
S=K_p^E\times K_q^E,
\qquad
|S|=AB.
}
\tag{3}

Thus \(S\) is cyclic. Its two hidden projection orders are \(A\) and \(B\),
and every prime divisor of its exponent occurs on exactly one side.

### Proof

The local groups \(K_p,K_q\) are cyclic, so their power-image orders are
exactly the two values in (1).

Suppose that a prime \(\ell\) divides both \(A\) and \(B\). Put

\[
e=v_\ell(N-1).
\]

Then

\[
v_\ell(m_p)>e,
\qquad
v_\ell(m_q)>e.
\]

Since \(m_p\mid p-1\) and \(m_q\mid q-1\), this gives

\[
p\equiv q\equiv1\pmod{\ell^{e+1}}.
\]

Therefore

\[
N=pq\equiv1\pmod{\ell^{e+1}},
\]

contrary to the definition of \(e\). This proves (2), including
\(\ell=2\).

Projection commutes with powering, so the two projections of \(S\) have
orders \(A\) and \(B\). Both projection maps are surjective. Hence \(|S|\)
is divisible by both \(A\) and \(B\). Coprimality makes it divisible by
\(AB\). But \(S\) is a subgroup of the product of order \(AB\), so equality
holds and \(S\) is the full product. A product of cyclic groups of coprime
orders is cyclic. \(\square\)

## 3. Exact separator law

The positive separators in the full product (3) are the nonidentity points
on its two coordinate axes. Therefore their exact number and uniform density
are

\[
\boxed{A+B-2},
\qquad
\boxed{
\delta_E
=
\frac1A+\frac1B-\frac2{AB}.
}
\tag{4}

If \(A=1<B\) or \(B=1<A\), every nonidentity element of \(S\) is a
separator. If \(A,B\ge2\) and

\[
\min\{A,B\}\le P,
\]

then

\[
\delta_E\ge\frac1P.
\tag{5}

Thus near-uniform public sampling from \(S\), followed by
\(\gcd(x-1,N)\), is a Las Vegas polynomial-time factor extractor whenever
\(S\ne1\) and one hidden image order is polynomially bounded. The sampler
does not need to know \(A\), \(B\), or which side is small. As in P83, choose
independent public exponent ranges large enough that reduction modulo every
generator order is within inverse-polynomial total variation of uniform.

There is also a deterministic condition. Power the public generators by
\(N-1\), enumerate their subgroup by breadth-first multiplication, and stop
after a public cap \(T\). If

\[
\boxed{1<AB\le T,}
\tag{6}

then complete enumeration finds a separator. For
\(P,T=\operatorname{poly}(\log N)\), both procedures have polynomial bit
complexity.

The density statement is not an all-input bound. Both \(A\) and \(B\) can
be exponential in \(\log N\), and (4) can then be exponentially small.

## 4. Relation to a synchronized old subgroup

Suppose \(K\) contains a diagonal graph subgroup \(H\) of order \(h\). P94
gives

\[
h\mid N-1.
\]

Therefore the \((N-1)\)-power map kills \(H\) and factors through the
abstract quotient:

\[
K\longrightarrow K/H\longrightarrow S.
\]

In particular,

\[
|S|=AB\le[K:H].
\tag{7}

Equation (3) shows exactly what survives: only local-order components that
cannot occur on the other hidden side. All synchronized old order and all
pure phase information disappear.

This gives two complementary post-feedback branches.

1. If \(S\ne1\), the public power \(N-1\) has exposed a rectangular
   coprime-order state. Conditions (5) or (6), or a further suitable power
   decoder, can extract a factor.
2. If \(S=1\), every local order in the supplied subgroup divides \(N-1\).
   Pure phase growth can still exist. P94's punctures
   \((N-1)/\ell^j\) are then the correct operation.

The test \(S=1\) is public: power every supplied generator by \(N-1\) and
check whether all results equal one modulo \(N\).

## 5. The two fixed feedback witnesses split cleanly

### The 4033 order-growth witness

For

\[
N=4033=37\cdot109,
\qquad
K=\langle2,5\rangle,
\]

the verified local orders of 5 are

\[
\operatorname{ord}_{37}(5)=36,
\qquad
\operatorname{ord}_{109}(5)=27.
\]

Because

\[
N-1=4032,
\qquad
36\mid4032,
\qquad
\gcd(27,4032)=9,
\]

the public power has local orders one and three. Hence

\[
\boxed{
\gcd(5^{4032}-1,4033)=37.
}
\tag{8}

Indeed, \(5^{4032}\equiv3442\pmod{4033}\). Here

\[
A=1,
\qquad
B=3,
\qquad
|S|=3.
\]

This is shorter and more canonical than the earlier exponent 2520. It uses
the feedback-exposed block 5, but it remains only a fixed mechanism witness:
5 is also a small ordinary public base.

### The 2047 pure phase witness

For

\[
N=2047,
\qquad
K=\langle11,2\rangle,
\]

the subgroup exponent is 22 and

\[
22\mid2046=N-1.
\]

Thus

\[
K^{N-1}=1,
\qquad
A=B=1.
\]

The rectangular state is trivial and contains no separator. P94 instead
uses the puncture \((N-1)/11=186\), producing a group of order 121 with 20
separators. The two examples therefore exercise different branches of the
same public \(N-1\) bank.

## 6. Exact scope

The theorem supplies a new canonical post-feedback normalization. It does
not prove that feedback creates a nontrivial image \(S\), that one of
\(A,B\) is small, that \(AB\) fits a polynomial cap, or that the remaining
coprime-order cyclic state can be decoded in polynomial time when both local
orders are large.

If \(S=1\), P94 still needs a small phase prime and a polynomial residual
image. Thus the source problem is narrower but not solved: feedback must
create either an accessible asymmetric-order image after the \(N-1\) power,
or an accessible phase component after a puncture. No all-input probability
law, arbitrary-composite reduction, computational lower bound, complete
factoring algorithm, or literature novelty is proved.
