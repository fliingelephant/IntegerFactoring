# F190 candidate — retained-source Hadamard--Paley words at QP scale

## Status and scope

This is a proof-only candidate. It audits the surviving full-word channel of
P54 after polynomial resource bounds are replaced by quasipolynomial (QP)
bounds. No computation is used.

All logarithms are base two unless `ln` is written. Put

\[
n=\lceil\log_2(N+1)\rceil,
\qquad 2^{n-1}\le N<2^n.
\tag{1}
\]

A **fixed QP envelope** means

\[
\mathcal Q(n)=2^{C(\log_2(n+1))^k}
\tag{2}
\]

for constants \(C>0\) and integer \(k\ge1\). In particular,
\(\mathcal Q(n)=2^{o(n)}\). A product of a fixed number of fixed QP
envelopes is again QP.

The Fourier, Hankel, autocorrelation, puncture-list, distance, and collision
claims use a squarefree balanced semiprime

\[
N=pq,\qquad p<q<2p,
\tag{3}
\]

with distinct odd primes. Hence

\[
\sqrt{N/2}<p<\sqrt N<q<\sqrt{2N}.
\tag{4}
\]

Every public shift family is reduced modulo \(N\), deduplicated, and
difference-screened. Thus either a difference gcd factors \(N\), or its
shifts are distinct modulo both hidden primes. Since every fixed QP quantity
is \(o(p)\) on (3), all QP-size shift families below have size less than
\(p\) and \(q\) for all sufficiently large \(n\).

The result is a boundary, not a factoring algorithm. It closes explicit
low-order correlation, dense spectral/Hankel reconstruction, row-only short
puncture list recovery, and local-collision mechanisms. It does not close a
source-aware high-order decomposition that uses the arithmetic relation
between \(N\), the retained sources, and the full rows.

## 1. The retained transcript and factoring are QP-equivalent

For an odd integer \(M\), public distinct shifts \(a_1,\ldots,a_m\), and a
source \(X\bmod M\), an accepted row is

\[
Y(X)=\left(\left({X+a_j\over M}\right)\right)_{j=1}^m
\in\{-1,1\}^m,
\qquad
\gcd\!\left(\prod_j(X+a_j),M\right)=1.
\tag{5}
\]

Every entry and the acceptance event are deterministic public functions of
\((M,X,a_1,\ldots,a_m)\), computable in QP time for QP many entries.

Fix QP bounds for the number \(m(k)\) of consecutive shifts, the number
\(L(k)\) of independent accepted rows, the decoder time, and the inverse of
its success probability. Consider the following **retained-source HP
decoder**: on every odd composite non-perfect-power \(M\) of bit length
\(k\), after all primes at most \(4m(k)k\) have been removed, it receives
\(L(k)\) accepted rows and their sources and returns, with inverse-QP
probability, a numerical prime \(r\mid M\) whose exponent in \(M\) is odd.

Then:

1. such a decoder gives an all-input classical Las Vegas QP factoring
   algorithm;
2. an all-input classical Las Vegas QP factoring algorithm gives such a
   decoder, which may ignore the transcript.

Thus a retained-source decoder whose required output is a numerical hidden
prime is QP-equivalent to factoring. Calling it list recovery does not make
it a smaller auxiliary theorem.

## 2. Exact Fourier support and Hankel rank

Let

\[
s(t)=\left({t\over N}\right)=\chi_p(t)\chi_q(t),
\qquad t\in\mathbb Z/N\mathbb Z,
\tag{6}
\]

where every quadratic character is extended by zero. With
\(\zeta_N=e^{2\pi i/N}\), define

\[
\widehat s(a)=\sum_{t\bmod N}s(t)\zeta_N^{-at}.
\tag{7}
\]

Then

\[
\widehat s(a)=0\quad\Longleftrightarrow\quad \gcd(a,N)>1,
\qquad
|\widehat s(a)|=\sqrt N\quad\Longleftrightarrow\quad\gcd(a,N)=1.
\tag{8}
\]

Consequently, the complete Jacobi sequence has exactly

\[
\varphi(N)=(p-1)(q-1)=N-p-q+1=N-O(\sqrt N)=2^{\Theta(n)}
\tag{9}
\]

nonzero complex Fourier modes. Its minimal nonzero constant-coefficient
complex recurrence has order exactly \(\varphi(N)\), and its \(N\)-by-\(N\)
periodic Hankel matrix

\[
H=(s(i+j\bmod N))_{0\le i,j<N}
\tag{10}
\]

has rank exactly \(\varphi(N)\).

Therefore dense Prony/Padé reconstruction, explicit frequency enumeration,
and a decoder that materializes the Hankel rank need
\(\Omega(\varphi(N))=2^{\Theta(n)}\) scalar output or degree in this named
model. This is exponential in \(n\), not polynomial and not QP. It is not a
lower bound for a succinct high-degree representation or an arithmetic
algorithm outside this model.

## 3. Exact autocorrelation and the QP explicit-correlation extension

For \(d\bmod N\), put

\[
C_N(d)=\sum_{t\bmod N}s(t)s(t+d).
\tag{11}
\]

Then

\[
C_N(d)=
\begin{cases}
\varphi(N),&N\mid d,\\
1-p,&p\mid d,\ q\nmid d,\\
1-q,&q\mid d,\ p\nmid d,\\
1,&\gcd(d,N)=1.
\end{cases}
\tag{12}
\]

Every factor-sensitive shift in (12) already returns that factor through
\(\gcd(d,N)\). On the difference-screened branch, every nontrivial complete
pair correlation is the public constant \(1\).

For a unit frequency \(a\), the raw normalized Fourier mean has magnitude
\(N^{-1/2}\). Its empirical average requires at least
\((\varphi(N)-1)/\eta^2\) independent samples for relative root-mean-square
error at most \(\eta\). For a unit difference \(d\), the raw normalized
autocorrelation mean is \(1/N\), and its empirical average requires
\((N^2\rho_d-1)/\eta^2\) samples, where

\[
\rho_d=(1-2/p)(1-2/q).
\tag{13}
\]

Both requirements are exponential in \(n\).

P53's explicit-correlation bound remains exponentially strong when every
polynomial bound in that observation model is replaced by a fixed QP bound.
For a screened shifted-Jacobi monomial with \(u\le\mathcal Q(n)\) distinct
shifts, its drift from the public fair-sign/constant-one baseline is at most

\[
O\!\left({u^2\over\sqrt N}\right)
=2^{-n/2+o(n)}.
\tag{14}
\]

An explicitly expanded QP list with QP coefficient \(\ell_1\)-norm has total
drift \(2^{-n/2+o(n)}\). Likewise, a past-adaptive sequence that releases
one scalar from each fresh hidden source and has QP total shift support is
within \(2^{-n/2+o(n)}\) total variation of P53's public simulator. This does
not cover retaining a source or row, several decisions on one row, or a
succinct statistic with non-QP Fourier expansion.

## 4. Exact short-puncture list sizes

Let \(r\) be an odd prime and let
\(A=(a_1,\ldots,a_m)\) be distinct modulo \(r\), with \(m<r\). For
\(S\subseteq[m]\), define the accepted local moment

\[
B_r(S)=\sum_{x\in\mathbb F_r\setminus\{-a_1,\ldots,-a_m\}}
\prod_{j\in S}\chi_r(x+a_j).
\tag{15}
\]

Then

\[
B_r(\varnothing)=r-m,
\qquad
|B_r(S)|\le(m-1)\sqrt r\quad(S\ne\varnothing).
\tag{16}
\]

For \(\epsilon\in\{-1,1\}^m\), the exact local list size is

\[
L_r(\epsilon)
=2^{-m}\sum_{S\subseteq[m]}\epsilon_S B_r(S),
\qquad
\left|L_r(\epsilon)-{r-m\over2^m}\right|
\le(m-1)\sqrt r.
\tag{17}
\]

For the balanced semiprime (3), let \(F_y\) be the number of accepted pairs
\((x,z)\in\mathbb F_p\times\mathbb F_q\) whose coordinatewise product of
the two local punctured Paley words equals
\(y\in\{-1,1\}^m\). Exactly,

\[
F_y=2^{-m}\sum_{S\subseteq[m]}y_S B_p(S)B_q(S),
\tag{18}
\]

and uniformly in \(y\),

\[
\left|F_y-{(p-m)(q-m)\over2^m}\right|
\le(m-1)^2\sqrt N.
\tag{19}
\]

For each fixed \(\delta>0\), if

\[
m\le(1/2-\delta)\log_2N,
\tag{20}
\]

then, uniformly over every product word,

\[
F_y={N\over2^m}(1+o(1)).
\tag{21}
\]

In particular, if \(2^m\) is QP, equivalently
\(m=(\log n)^{O(1)}\), every row-only exact product-code list has

\[
F_y=2^{n-o(n)}
\tag{22}
\]

members. This is exponential in \(n\), not QP. To make the entropy quotient
\(N/2^m\) merely QP requires \(m\ge n-(\log n)^{O(1)}\); directly
enumerating the \(2^m\) sign splittings then costs \(2^{\Theta(n)}\).

This is a row-only product-code obstruction. The retained numerical source
distinguishes global sources and is not covered by (17)--(22). A source-aware
decoder must use the arithmetic relation between that source and the unknown
local moduli.

## 5. Long words can have good code distance

For a prime \(r\) and distinct sources \(x,z\in\mathbb F_r\), among the
\(r-2\) shifts for which both local symbols are nonzero, exactly
\((r-1)/2\) make the symbols disagree. Therefore, if \(m\) distinct shifts
are selected uniformly without replacement and

\[
m\ge96\ln r,
\tag{23}
\]

then with probability at least \(1-r^{-2}\), every pair of local source
words disagrees in at least \(m/6\) selected positions.

Thus \(m=O(\log r)=O(n)\) chosen columns can give constant relative distance
and singleton exact local lists. Code distance and information-theoretic list
size do not obstruct the long-word regime. The local modulus \(r\) is needed
to define that code, however. The public received word is already the Jacobi
word of the retained source. The required operation is a modulus-blind
decomposition into hidden \(p\)- and \(q\)-Paley components, not ordinary
decoding in a known code.

## 6. QP collision and bounded-degree correlated-source bounds

Take \(R\le\mathcal Q(n)\) independent accepted sources and
\(m\le\mathcal Q(n)\) screened shifts. Put \(K=Rm\). Within a row, local
collisions have already been removed by difference screening. Across rows,
the probability of any equality modulo \(p\) or modulo \(q\) among the
\(K\) arguments is at most

\[
\binom K2\left({1\over p-m}+{1\over q-m}\right)
=2^{-n/2+o(n)}.
\tag{24}
\]

Every local but nonglobal equality would already expose a factor by taking
the gcd of the public argument difference with \(N\). The birthday scale is
\(K=\Theta(\sqrt p)=N^{1/4+o(1)}=2^{n/4+o(n)}\), which is exponential in
\(n\), not QP.

More generally, let at most \(H\le\mathcal Q(n)\) public polynomials
\(P_\nu(Z)\in(\mathbb Z/N\mathbb Z)[Z]\) have degree at most
\(D\le\mathcal Q(n)\). Screen every coefficient gcd. If this gives no
factor, discard polynomials whose coefficients all vanish modulo \(N\).
Every remaining polynomial is nonzero modulo both \(p\) and \(q\). For a
fresh uniform \(Z\bmod N\),

\[
\Pr\left[\exists\nu:
P_\nu(Z)=0\pmod p\text{ or }P_\nu(Z)=0\pmod q\right]
\le HD\left({1\over p}+{1\over q}\right)
=2^{-n/2+o(n)}.
\tag{25}
\]

Conditioning on any public acceptance event of probability at least a fixed
constant changes (25) by at most that constant factor. The statement remains
valid for past-adaptive menus applied to a fresh source, by conditioning on
the past. Taking \(P_\nu=g_i-g_j\) covers QP many equality tests among
bounded-degree polynomially correlated coordinates.

This closes collision-based additive-combinatorial designs and bounded-degree
correlated-source equality tests. It does not cover a succinct polynomial or
rational relation of exponential degree, nor high-order reuse of the same
source.

## 7. Exact surviving interface

After these boundaries, a materially new P54 attack must provide a uniform
QP algorithm that:

1. uses retained numerical sources and full rows, with \(m\) potentially
   linear through QP in \(n\);
2. performs a genuinely source-aware, high-Walsh-degree or succinct
   characteristic-order operation;
3. separates an unknown Hadamard--Paley product code without knowing either
   local modulus;
4. returns a verifiable zero divisor or numerical factor;
5. does not enumerate \(2^m\) sign splittings, materialize
   \(\varphi(N)\) Fourier modes, or wait for a local-coordinate collision.

This interface is live. However, if its specification simply promises a
numerical prime with inverse-QP probability, Section 1 shows that the promise
is already QP-equivalent to the original factoring task.
