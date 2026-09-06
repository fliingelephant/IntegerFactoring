# F226 candidate — exact random binary banks and the compatible-support sampling boundary

## Status

This is a frozen, self-audited theorem candidate with preregistered finite
discovery scans.  It is not a factoring algorithm.

The positive result removes two source-level difficulties.  Binary integer
structure gives an exact-uniform, refreshable, recursively factorable bank
of auxiliary primes in numerical quasipolynomial cost.  A capped divisor
enumeration then converts any sufficiently large compatible part of a
polylogarithmic block into a genuine Las Vegas factoring attempt, without
being told which auxiliary primes are compatible.

The negative result identifies the remaining all-input difficulty.  The
complete multiplier ensemble is independent of `N`.  It samples a hidden
compatible prime `ell` with probability essentially `1/ell`.  Every
compatible exponent class is supported on the prime divisors of one hidden
integer `N^i-p`.  There is no all-input lower bound here for the required
harmonic prime-factor mass.  In fact, any nonnegligible support-discovery
probability from the random bank is, up to an arbitrarily chosen inverse-QP
tail, already concentrated on a QP-enumerable deterministic prime bank.

Throughout, numerical QP means

\[
2^{(\log n)^{O(1)}},
\qquad n=\lceil\log_2(N+1)\rceil.
\]

## Theorem A — the top-bit child and its exact local orbit

Let `N` be odd, put `k=n-1`, and define

\[
A=N-2^k.
\tag{A1}
\]

Then

\[
0<A<N/2,
\qquad
\gcd(A,N)=1.
\tag{A2}
\]

Thus `A` is one valid fixed-ratio recursive child.  For every prime
`ell|A`,

\[
N\equiv2^k\pmod\ell.
\tag{A3}
\]

Write

\[
d_\ell=\operatorname{ord}_\ell(2),
\qquad
h_\ell=\operatorname{ord}_\ell(N)
=\frac{d_\ell}{\gcd(d_\ell,k)}.
\tag{A4}
\]

Now assume `N=pq`, where `p,q` are distinct odd primes.  The two hidden
residues satisfy

\[
p\in\langle N\rangle\pmod\ell
\quad\Longleftrightarrow\quad
q\in\langle N\rangle\pmod\ell.
\tag{A5}
\]

When they belong, there is a unique class

\[
i_\ell(p)\pmod {h_\ell}
\tag{A6}
\]

such that

\[
p\equiv N^{i_\ell(p)},
\qquad
q\equiv N^{1-i_\ell(p)}
\pmod\ell.
\tag{A7}
\]

For a finite bank of such primes, one exponent works for `p` across the
whole bank if and only if

\[
i_\ell(p)\equiv i_r(p)
\pmod{\gcd(h_\ell,h_r)}
\tag{A8}
\]

for every pair `ell,r`.  Factoring `A` makes `ell` and `h_ell` public after
factoring `ell-1`; it does not prove (A5), reveal (A6), or make (A8)
automatic.

## Theorem B — a recursion-safe exact-uniform random bank

Let

\[
m=\lfloor n/2\rfloor.
\tag{B1}
\]

Choose `u` uniformly from the odd residue classes modulo `2^m`.  For
`2<=j<=m`, let

\[
R_j(u)=uN\bmod2^j,
\qquad 1\le R_j(u)<2^j,
\tag{B2}
\]

using the canonical integer representative.  Gcd-screen every distinct
`R_j(u)` against `N`.  A nontrivial gcd is a verified factor.  On the
remaining branch, all prime divisors of every child are auxiliary primes
coprime to `N`.

The following statements are exact.

1. `R_m(u)` is uniform over the odd integers in `[1,2^m)`.
2. Consecutive prefixes obey
   \[
   R_{j+1}(u)\in\{R_j(u),R_j(u)+2^j\}.
   \tag{B3}
   \]
   In the second case, the two consecutive values are coprime.  Arbitrary
   nonconsecutive prefixes need not be coprime; repeated auxiliary primes
   are deduplicated.
3. Every child and every integer `ell-1` needed to compute an auxiliary
   order has at most `m` bits.
4. One bank has at most `m` distinct children, total encoded child
   bit-length `O(n^2)`, and at most `O(n^2)` prime occurrences and
   prime-minus-one descendants.

Consequently, a numerical-QP number `K(n)` of independent banks can be
fully factored, and all auxiliary orders can be computed, within a
numerical-QP recursive bit bound.  More precisely, if one level uses at
most

\[
B(n)=K(n)\,O(n^2)
\tag{B4}
\]

recursive calls on integers of at most `ceil(n/2)` bits, then the recursion
depth is `O(log n)` and

\[
\prod_{r\ge0} B(\lceil n/2^r\rceil)
=2^{(\log n)^{O(1)}}.
\tag{B5}
\]

This contrasts with factoring `O(n)` separate `(n-1)`-bit truncation
children.  The latter gives a multiplicative recurrence at every one-bit
level and has no QP proof.  Only one top-bit child, or QP many half-bit
children, is justified here.

## Theorem C — exact conditional bridge to a residue terminal

Let `Q` be any selected set of auxiliary primes produced by Theorem B.
Suppose an APR/Cohen--Lenstra-type calculation supplies a certified common
exponent class for `p` across `Q`.  Put

\[
S=\prod_{\ell\in Q}\ell,
\qquad
H=\operatorname{lcm}_{\ell\in Q}h_\ell.
\tag{C1}
\]

If `H<=T(n)` for a numerical-QP bound `T`, generalized CRT gives a public
set of at most `T` exponents and hence at most `T` certified residues

\[
p\equiv N^i\pmod S.
\tag{C2}
\]

Combine this with any certified low-bit/common-order modulus

\[
L_0=\operatorname{lcm}(2^t,M)
\tag{C3}
\]

by generalized CRT.  If

\[
\operatorname{lcm}(L_0,S)
\ge \frac{N^{1/4}}{\operatorname{QP}(n)},
\tag{C4}
\]

then enumeration followed by the known-residue arithmetic-progression
terminal factors the balanced semiprime in numerical-QP bit complexity.

Thus the random binary bank is a genuine source of public auxiliary
moduli.  The remaining source lemma is exactly a conditional inverse-QP
bound for certified orbit acceptance and common-exponent compatibility.

## Theorem D — the affine torsor survives all scalar bank data

Fix a squarefree odd auxiliary modulus `S` coprime to `N`.  All ordered
unit factorizations of `N mod S` form the affine inversion torsor

\[
\mathcal H_S
=\{(x,Nx^{-1}):x\in(\mathbb Z/S\mathbb Z)^\times\}.
\tag{D1}
\]

For every multiplicative character `chi modulo S`, writing `z=chi(x)`
gives

\[
(\chi(x),\chi(Nx^{-1}))
=(z,\chi(N)z^{-1}).
\tag{D2}
\]

After the public bank is fixed, its induced local scalar-character
constraints reveal only `chi(N)`.  Within this scalar transcript they do not
select `z`, orient the two hidden components, certify new common primary
support, or give a residue of `p`.  The full integer values of the children
remain available to a different non-scalar or Archimedean computation.  A
non-scalar APR/CL identity can also add information; Theorem D does not rule
either possibility out.

There is also an exact named probability model.  Draw `X` uniformly from
the unit group modulo `S` and put `Y=NX^{-1}`.  This is uniform on
`mathcal H_S`.  For every public exponent set `I`,

\[
\Pr\bigl[X\equiv N^i\pmod S
          \text{ for some }i\in I\bigr]
=\frac{|\{N^i\bmod S:i\in I\}|}{\varphi(S)}
\le\frac{|I|}{\varphi(S)}.
\tag{D3}
\]

Because `S` is odd and squarefree,

\[
\varphi(S)\ge\sqrt S.
\tag{D4}
\]

Therefore, if `|I|` is numerical QP and

\[
S\ge N^{1/4}/\operatorname{QP}(n),
\tag{D5}
\]

the probability in (D3) is

\[
2^{-\Omega(n)}.
\tag{D6}
\]

This is an exact obstruction to treating the hidden local orientation as
uniform and then claiming inverse-QP terminal acceptance.  It is a named
model, not a distribution theorem for adversarial integers and not a lower
bound against the random multiplier `u`.

Finally, every compatible bank with common exponent `i` obeys the exact
hidden divisibility relation

\[
S\mid N^i-p.
\tag{D7}
\]

Thus a proof for random binary banks must show, uniformly for every input
and conditional on the prior history, that their recursively exposed prime
factors capture enough compatible support from one of the hidden integers
`N^i-p`.  The uniformity of `R_m(u)` alone does not supply that theorem.

## Theorem E — exact multiplier-ensemble and prime-incidence laws

Put `B=2^m` and let `u` range over all `B/2` odd residues modulo `B`.
The entire child vector has the exact multiset identity

\[
\left\{(R_2(u),\ldots,R_m(u)):u\bmod B\text{ odd}\right\}
=\left\{(v\bmod2^2,\ldots,v\bmod2^m):
          1\le v<B,\ v\text{ odd}\right\}.
\tag{E0}
\]

Thus every statistic computed only from the child integers is independent
of `N`; the labels `u` and the quotients `floor(uN/B)` are not covered by
this statement.  The following product identities are immediate:

\[
\prod_{\substack{u\bmod B\\u\text{ odd}}}R_m(u)=(B-1)!!,
\tag{E1}
\]

\[
\prod_{\substack{u\bmod B\\u\text{ odd}}}R_j(u)
=\bigl((2^j-1)!!\bigr)^{2^{m-j}}
\qquad(2\le j\le m),
\tag{E2}
\]

and hence

\[
\prod_{\substack{u\bmod B\\u\text{ odd}}}\prod_{j=2}^mR_j(u)
=\prod_{j=2}^m
 \bigl((2^j-1)!!\bigr)^{2^{m-j}}.
\tag{E3}
\]

In particular, the complete multiset of child prime factors, including
multiplicity, is independent of `N`.

For a fixed odd prime `ell<B`, one full child has exact incidence
probability

\[
\pi_\ell
=\Pr(\ell\mid R_m)
=\frac{
 \left\lceil\frac12\left\lfloor\frac{B-1}{\ell}\right\rfloor\right\rceil
}{B/2}
\le {1\over\ell}+{2\over B}.
\tag{E4}
\]

If all prefixes in one bank are used, then

\[
\Pr\bigl(\ell\mid R_j\text{ for some }2\le j\le m\bigr)
\le\min\left(1,{m+4\over\ell}\right).
\tag{E5}
\]

Therefore `K` independent prefix banks expose a fixed prime `ell` with
probability at most

\[
\min\left(1,{K(m+4)\over\ell}\right).
\tag{E6}
\]

These are integer sampling laws, not generic-ring heuristics.

## Theorem F — accepted support is a hidden cyclotomic gcd

Assume again that `N=pq`.  For an auxiliary prime `ell` put

\[
h_\ell=\operatorname{ord}_\ell(N).
\]

Then

\[
p\in\langle N\rangle\pmod\ell
\quad\Longleftrightarrow\quad
p^{h_\ell}\equiv q^{h_\ell}\equiv1\pmod\ell.
\tag{F1}
\]

Consequently the locally accepted primes of exact local order `h` are
precisely the primes `ell` satisfying

\[
\operatorname{ord}_\ell(N)=h,
\qquad
\ell\mid\Gamma_h,
\qquad
\Gamma_h=\gcd(p^h-1,q^h-1).
\tag{F2}
\]

For a fixed nonnegative exponent `i`, define the compatible support

\[
\mathcal G_i=\left\{
 \ell<B:\ell\text{ odd prime},\ \ell\nmid NL_0,
 \ p\equiv N^i\pmod\ell
\right\}.
\tag{F3}
\]

Every member of `mathcal G_i` divides the nonzero hidden integer

\[
D_i=N^i-p.
\tag{F4}
\]

Thus, if `0<=i<T`, the squarefree product of the entire support has
binary logarithm

\[
L_i:=\sum_{\ell\in\mathcal G_i}\log_2\ell
< n\max(1,i)\le nT.
\tag{F5}
\]

Let `s` independent full children be sampled and let `C_i` be the product
of the primes in `mathcal G_i` that divide at least one child.  Put
`X_i=log_2 C_i`.  Then

\[
\mathbb E X_i
=\sum_{\ell\in\mathcal G_i}
 \log_2\ell\,[1-(1-\pi_\ell)^s].
\tag{F6}
\]

If `theta<L_i` and the right side is at least `theta+delta`, then

\[
\Pr(X_i\ge\theta)
\ge {\delta\over L_i-\theta}.
\tag{F7}
\]

This is an exact inverse-QP progress criterion whenever `T,L_i` are QP
bounded and `delta` is inverse QP.  It is not an all-input lower bound:
the right side of (F6) can be exponentially small when the relevant
support is concentrated in large prime divisors of `D_i`.

## Theorem G — a concrete Las Vegas bridge removes hidden subset selection

Fix `s<=(log n)^a` and a numerical-QP exponent cap `T`.  In one block,
sample `s` independent full children `R_m`, gcd-screen them against `N`,
recursively factor the distinct children, and let `W` be the squarefree
product of all exposed odd primes.  Fix a divisor cap `D`.  If
`2^omega(W)>D`, abandon this block.  Otherwise enumerate every squarefree
divisor `d|W` and every `0<=i<T`.  For each pair, combine

\[
p\equiv N^i\pmod d
\tag{G1}
\]

with the existing residue modulo `L_0`, and run the verified known-residue
terminal whenever the combined modulus reaches its threshold.

This is a Las Vegas procedure: it outputs only a gcd-verified factor.  If
for some `i<T`

\[
\operatorname{lcm}(L_0,C_i)
\ge {N^{1/4}\over\operatorname{QP}(n)},
\tag{G2}
\]

and the divisor cap is not exceeded, then the procedure factors `N`, since
the hidden divisor `C_i` is one of the enumerated public candidates.
No APR oracle is needed to identify the compatible subset.

For a uniform odd full child,

\[
\mathbb E\,2^{\omega(R_m)}\le 2+\log B.
\tag{G3}
\]

Independence and `2^omega(W)<=prod_r 2^omega(R_m^{(r)})` give

\[
\Pr(2^{\omega(W)}>D)
\le{(2+\log B)^s\over D}.
\tag{G4}
\]

Because `C_i` is coprime to `L_0`, put

\[
\theta=\max\left(0,
 \log_2{N^{1/4}\over\operatorname{QP}(n)}-\log_2L_0
\right).
\]

If the expectation in (F6) is at least `theta+delta`, then one block has
the explicit success lower bound

\[
\Pr(\text{verified factor in the block})
\ge
{\delta\over L_i-\theta}
-{(2+\log B)^s\over D},
\tag{G5}
\]

whenever `theta<L_i`.  Thus a positive inverse-QP harmonic surplus gives a
positive inverse-QP Las Vegas transition after choosing the cap tail
smaller than the first term.

Choosing `D=(2+log B)^s P(n)` for any numerical-QP `P` keeps the
enumeration cost QP and makes the discard probability at most `1/P`.  A
numerical-QP number of independent blocks still makes only QP many half-size
recursive
calls at one node, so Theorem B's recurrence applies.  This accounting is
conditional on an all-input recursive factoring dispatch at every child;
balancedness is not inherited by the random child.

The particularly concrete exponents `i=0,1` target

\[
C_0\mid p-1,
\qquad
C_1\mid q-1,
\tag{G6}
\]

because auxiliary primes are coprime to `N`.  Thus G is a randomized,
subset-complete analogue of shifted-prime-factor methods, not a claim that
`p-1` or `q-1` is smooth.

There is an unconditional favorable-state corollary.  Fix a public
numerical-QP bound `Q(n)`.  Suppose an odd squarefree integer `d<=Q(n)`
satisfies

\[
d\mid p-1
\quad\text{or}\quad
d\mid q-1,
\qquad
\operatorname{lcm}(L_0,d)
\ge {N^{1/4}\over\operatorname{QP}(n)},
\tag{G7}
\]

and `4d<=B`.  One full child is divisible by `d` with probability at
least `1/(2d)`.  With the public one-child cap

\[
D=4Q(n)(2+\log B),
\tag{G8}
\]

the discard probability is at most `1/(4Q(n))`.  Since `d<=Q(n)`, the
verified Las Vegas attempt succeeds with probability at least `1/(4Q(n))`.
What is missing
on all inputs is precisely the existence of such a smooth shifted divisor,
or the more general harmonic surplus in (G5).

## Theorem H — QP enumeration dominates uniform prime-support discovery

Consider `K` independent prefix banks and all exponent classes
`0<=i<T`.  For a cutoff `Y`, let `Z_i(Y)` be the binary logarithm of the
product of captured primes in `mathcal G_i` that exceed `Y`.  Equations
(E6) and (F5) give

\[
\mathbb E\sum_{i<T}Z_i(Y)
\le {K(m+4)nT^2\over Y}.
\tag{H1}
\]

Hence, for every `Delta>0`,

\[
\Pr\bigl(Z_i(Y)\ge\Delta\text{ for some }i<T\bigr)
\le {K(m+4)nT^2\over Y\Delta}.
\tag{H2}
\]

For numerical-QP `K,T`, any claimed inverse-QP probability, and any
inverse-QP positive progress `Delta`, one may choose a numerical-QP cutoff
`Y` that makes (H2) smaller than that claim.  Every prime at most `Y` can
instead be generated by a deterministic QP sieve.  Therefore any
inverse-QP compatible log weight supplied by this route must, up to the
chosen tail, come from prime values in a deterministic QP-enumerable range.
This does not identify the compatible primes or remove the useful random
grouping exploited by Theorem G.  It also does not simulate the quotient
`floor(uN/B)` or a future non-scalar use of the complete child integer.

There is also a sharp large-prime corollary.  If `X>1`, the number of
primes `ell>=X` with `ord_ell(N)<=T` is at most

\[
{nT(T+1)\over2\log_2X},
\tag{H3}
\]

because all of them divide `prod_{h<=T}(N^h-1)`.  At
`X=N^{1/4}/QP(n)`, QP many prefix banks hit even one such prime with
probability `2^{-Omega(n)}`.  Thus one terminal-size, small-order auxiliary
prime cannot supply the desired Las Vegas law.

A named exact rough-support model shows why (F6) has no formal all-input
lower bound.  If

\[
p=2P+1,
\qquad q=2Q+1
\tag{H4}
\]

with `P,Q` prime and of order `sqrt(N)`, then the odd compatible supports
for the guaranteed classes `i=0,1` are only `P` and `Q`.  QP many prefix
banks hit either with probability

\[
2^{-n/2+(\log n)^{O(1)}}.
\tag{H5}
\]

This is a conditional safe-prime-shift model, not a claim that infinitely
many balanced pairs in (H4) are known.  It isolates the exact missing
integer theorem: one needs a uniform smooth/harmonic-mass result for some
hidden `N^i-p`, or a different factor/carry transition on rejection.

## Exact finite witnesses and discovery evidence

The recursion-safe deterministic lower-half bank was tested on 7,212
balanced semiprimes with 19–29 bits.  Even after granting the hidden local
orbit labels, 797 rows did not reach `ceil(N^(1/4))`, and 54 rows had no
accepted auxiliary prime.

The smallest zero-acceptance witness is

\[
\boxed{333859=563\cdot593.}
\tag{W1}
\]

For `m=9`, its distinct deterministic children are

\[
3,\qquad 35=5\cdot7.
\tag{W2}
\]

Modulo `3`, `5`, and `7`, the residue of `563` lies outside the subgroup
generated by `333859`.  Thus complete child factorization alone contributes
no local orbit modulus on this exact input.

For the 54 zero-acceptance deterministic witnesses, exhaustive enumeration
of every random odd multiplier gave ideal-oracle success fractions between

\[
\frac{330}{512}=0.64453125
\quad\text{and}\quad
0.951416015625,
\tag{W3}
\]

with mean `0.8218157733`.  This supports the random-bank construction as a
research direction.  It is not asymptotic evidence: at these sizes the cap
`n^4` exceeds nearly all auxiliary orders, while for large inputs the
condition `H<=QP(n)` is restrictive.  The scan also granted the unavailable
hidden local orbit labels.

## Remaining requirement

F226 leaves one precise all-input alternative:

> Prove an inverse-QP harmonic-mass lower bound strong enough to trigger
> Theorem G for some QP exponent, or turn scalar orbit/APR rejection into a
> verified factor, certified common primary support, or a new dyadic carry
> bit.

The ensemble and incidence identities show that uniform child-prime
discovery alone cannot prove this alternative.
