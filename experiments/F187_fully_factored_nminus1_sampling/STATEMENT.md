# F187 candidate — fully factored \(N-1\) random-base stripping

## Status and exact scope

This is a proof-only candidate about the following restricted route:

1. recursively obtain the complete prime factorization of
   \(A=(N-1)/2\);
2. use the resulting complete factorization of \(N-1\) for
   Pocklington/Lucas-style order stripping of independent uniform random
   bases.

The local stripping theorem and probability formulas below are elementary
and apply to every odd integer. The infinite hard family additionally invokes
the standard bounded-prime-gap theorem.

The conclusion is narrow. Fully factoring \(N-1\) removes hidden ambiguity
inside the common-return branch, but independent uniform bases can enter that
branch with exponentially small probability on an infinite balanced
semiprime family. This closes the claimed inverse-QP success bound for this
random-base route. It does not close deterministic or adaptive base choices,
other exponent families, or integer factoring itself.

Throughout,

\[
n=\left\lceil\log _2(N+1)\right\rceil,
\qquad m=N-1,
\qquad A=\frac{N-1}{2},
\tag{1}
\]

and \(N\) is odd. Perfect powers and nonunit sampled bases may be screened
before the order processing.

## 1. Exact order-stripping trichotomy

Write the hidden prime-power decomposition as

\[
N=\prod_{i=1}^{s}p_i^{e_i},
\qquad
h_i=\varphi(p_i^{e_i})=p_i^{e_i-1}(p_i-1).
\tag{2}
\]

Let \(a\in(\mathbb Z/N\mathbb Z)^\times\), and first compute

\[
G_0=\gcd(a^m-1,N).
\tag{3}
\]

There are three cases.

1. If \(1<G_0<N\), then \(G_0\) is a proper factor.
2. If \(G_0=1\), then for every \(k\mid m\),
   \[
   \gcd(a^k-1,N)=1.
   \tag{4}
   \]
   This base is a **complete nonreturn** for the factored exponent \(m\).
3. If \(G_0=N\), every local order divides \(m\). Initialize \(R=m\).
   For every rational prime \(q\mid R\), repeatedly compute
   \[
   G_q=\gcd(a^{R/q}-1,N).
   \tag{5}
   \]
   If \(G_q=N\), replace \(R\leftarrow R/q\). If
   \(1<G_q<N\), return the factor. If \(G_q=1\), retain that copy of
   \(q\) and continue with the next prime.

If case 3 produces no proper gcd, then

\[
\boxed{
\operatorname{ord}_{p_i^{e_i}}(a)=R
\quad(1\le i\le s).
}
\tag{6}
\]

The complete factorization of this exact common local order is known. A
public certificate consists of

\[
a^R=1\pmod N,
\qquad
\gcd(a^{R/q}-1,N)=1
\quad(q\mid R).
\tag{7}
\]

Thus one fully processed base returns exactly one of

\[
\boxed{
\text{proper factor}
\quad\lor\quad
\text{complete nonreturn}
\quad\lor\quad
\text{fully factored exact common local order}.}
\tag{8}
\]

For several bases, let \(C\) be the lcm of the exact common orders returned
without a factor. Every rational prime \(p_i\mid N\) satisfies

\[
C\mid p_i-1.
\tag{9}
\]

Consequently,

\[
\boxed{C>\sqrt N\quad\Longrightarrow\quad N\text{ is prime}.}
\tag{10}
\]

Equation (10) is the Pocklington/Lucas terminal for this route.

## 2. Exact uniform-random-base law

Assume now that \(a\) is uniform in
\((\mathbb Z/N\mathbb Z)^\times\). Define

\[
d_i=\gcd(m,h_i)=\gcd(m,p_i-1),
\tag{11}
\]

\[
\beta_i=1-\frac{d_i}{p_i-1},
\qquad
\gamma_i=\frac{d_i}{h_i},
\qquad
D=\gcd(d_1,\ldots,d_s).
\tag{12}
\]

Then the initial gcd has the exact distribution

\[
\Pr(G_0=1)=\prod_{i=1}^{s}\beta_i,
\qquad
\Pr(G_0=N)=\prod_{i=1}^{s}\gamma_i,
\tag{13}
\]

and

\[
\Pr(1<G_0<N)
=1-\prod_i\beta_i-\prod_i\gamma_i.
\tag{14}
\]

Conditioned on \(G_0=N\), the local residues are independent uniform
elements of cyclic groups of orders \(d_i\). Hence full stripping returns no
factor exactly when all local orders are equal, and

\[
\Pr(\text{no stripping factor}\mid G_0=N)
=
\frac{\displaystyle\sum_{r\mid D}\varphi(r)^s}
     {\displaystyle\prod_i d_i}.
\tag{15}
\]

More precisely, the unconditional probability that stripping returns the
exact common order \(r\mid D\) is

\[
\Pr(\text{common order }r)=
\frac{\varphi(r)^s}{\prod_i h_i}.
\tag{16}
\]

For a current accumulated state \(C\), the exact no-progress probability is

\[
\boxed{
\Pr(\text{no factor and no strict growth})
=
\prod_i\beta_i
+
\frac{\displaystyle
      \sum_{r\mid\gcd(D,C)}\varphi(r)^s}
     {\displaystyle\prod_i h_i}.}
\tag{17}
\]

The two terms in (17) are respectively complete nonreturn and synchronized
common return with \(r\mid C\). All other bases yield a proper factor or
strictly enlarge \(C\).

## 3. Exact squarefree-semiprime formula

Let \(N=pq\) for distinct odd primes \(p<q\), and put

\[
d=\gcd(p-1,q-1).
\tag{18}
\]

Since \(m=pq-1\), both local root subgroups have order \(d\):

\[
\gcd(m,p-1)=\gcd(m,q-1)=d.
\tag{19}
\]

Starting from \(C=1\), a uniform unit base has exact success probability

\[
\boxed{
\Pr(\text{proper factor or strict common-order growth})
=
\frac d{p-1}+\frac d{q-1}
-\frac{d^2+1}{(p-1)(q-1)}.}
\tag{20}
\]

The two parts are

\[
\Pr(\text{proper factor})
=1-
\left(1-\frac d{p-1}\right)
\left(1-\frac d{q-1}\right)
-\frac{\displaystyle\sum_{r\mid d}\varphi(r)^2}
       {(p-1)(q-1)},
\tag{21}
\]

and

\[
\Pr(\text{strict common-order growth})
=
\frac{\displaystyle\sum_{\substack{r\mid d\\r>1}}
      \varphi(r)^2}
     {(p-1)(q-1)}.
\tag{22}
\]

The only no-progress events are complete nonreturn at both primes, or the
identity element in both local groups.

## 4. Elementary bounded-gap-pair obstruction

For any primes \(p<q\),

\[
d=\gcd(p-1,q-1)\mid q-p.
\tag{23}
\]

Therefore, if \(q-p\le H\), then every synchronized common order divides
\(d\le H\). No number of such common-order returns can make \(C>H\).
Moreover, for every current state \(C\), a fresh uniform unit base can factor
or grow the state only if at least one local component is an \(m\)-th root.
Thus

\[
\Pr(\text{factor or strict growth})
\le
\frac d{p-1}+\frac d{q-1}
=O_H(p^{-1}).
\tag{24}
\]

For balanced pairs \(q=p+O_H(1)\),

\[
p=2^{n/2+O_H(1)},
\qquad
\Pr(\text{success per base})
=2^{-n/2+O_H(1)}.
\tag{25}
\]

The same asymptotic upper bound holds when bases are sampled uniformly from
all residues and a nonunit gcd is counted as success. Hence any numerical-QP
number

\[
K(n)=2^{(\log n)^{O(1)}}
\tag{26}
\]

of independent uniform samples still has total success probability
\(2^{-\Omega(n)}\) on this family.

Equations (23)--(25) are elementary statements for every bounded-gap prime
pair. To obtain an infinite input family, invoke the standard
bounded-prime-gap theorem: there is an absolute constant \(H\) for which
infinitely many pairs of distinct primes satisfy \(q-p\le H\). This named
theorem is the only external ingredient in the infinite-family conclusion.

Thus the fully factored \(N-1\) route has no all-input inverse-QP success
lower bound for independent uniform random bases.

## 5. Prime, Carmichael, and prime-power contrasts

### Prime inputs

If \(N\) is prime, every unit returns and stripping gives its exact order in
the cyclic group of order \(m=N-1\). After \(k\) independent uniform bases,
let \(C_k\) be the lcm of their orders. For every rational prime \(q\mid m\),
the probability that the full \(q\)-part of \(m\) is absent from \(C_k\) is
\(q^{-k}\). Hence

\[
\Pr(C_k\ne m)
\le\sum_{q\mid m}q^{-k}
\le\omega(m)2^{-k}
<n2^{-k}.
\tag{27}
\]

Thus \(O(\log n)\) bases give a prime certificate with high probability.

### Squarefree Carmichael inputs

If \(N\) is squarefree Carmichael, Korselt's divisibility gives
\(p_i-1\mid N-1\) for every component. Every unit therefore enters the
full-return branch. Starting from \(C=1\), unequal local orders factor and a
common order greater than one grows \(C\). Only the CRT identity tuple makes
no progress, so

\[
\Pr(\text{factor or strict growth})=1-\frac1{\varphi(N)}.
\tag{28}
\]

### Odd prime powers

For \(N=p^e\), \(e\ge2\), one has

\[
d_1=p-1,
\qquad
\Pr(G_0=N)=p^{1-e},
\qquad
\Pr(1<G_0<N)=1-p^{1-e}.
\tag{29}
\]

There is no complete-nonreturn branch. Standard perfect-power detection
already resolves these inputs deterministically. Formulae (11)--(17) remain
valid without preprocessing and also cover composites with several repeated
prime-power components.

## 6. Exact recursive-cost scope

The complete factorization of \(A\) supplies that of \(m=2A\). Since

\[
\operatorname{bitlen}(A)\le n-1,
\tag{30}
\]

this is one smaller recursive child. A numerical-QP number of samples and
all associated modular powers, gcds, and order stripping cost numerical QP
in \(n\). Therefore, **if this is the only recursive call made by the
enclosing procedure**, its recurrence is

\[
\mathcal T(n)
\le \mathcal T(n-1)+Q(n)
\le nQ(n)
=2^{(\log n)^{O(1)}}.
\tag{31}
\]

No fixed-ratio contraction is required for this unique chain.

Equation (31) does not silently authorize recursive completion of every
factor subsequently returned. If a parent also recursively factors a split
\(N=uv\), the recurrence contains additional children:

\[
\mathcal F(N)
\le
\mathcal F((N-1)/2)+\mathcal F(u)+\mathcal F(v)+Q(n).
\tag{32}
\]

For an unbalanced split, both \((N-1)/2\) and the large cofactor can retain
\(n-O(1)\) bits. The one-child summation does not bound this recursion tree.
F187 therefore proves the QP cost of the isolated one-child preprocessing
and order-processing stage, conditional on its stated terminal interface.
It does not prove QP complete factorization.
