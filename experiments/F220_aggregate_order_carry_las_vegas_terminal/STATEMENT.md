# F220 candidate — aggregate order/carry terminal and exact Las Vegas progress law

## Status and scope

This is a frozen, self-audited, proof-only candidate. It proves:

1. a primary-level certificate that a prime power divides every
   rational-prime predecessor (r-1) for (r\mid N), without requiring
   equality of complete local orders;
2. an aggregate generalized-CRT transition from such certificates and a
   supplied dyadic factor residue to the Gao--Feng--Hu--Pan terminal;
3. an exact additive-drift condition sufficient for Las Vegas numerical-QP
   acquisition;
4. the exact primary-level probability law for a uniform unit and one
   factored annihilator; and
5. attainability, bounded-gap, and cyclic-direction obstructions to proving
   that progress condition from generic witnesses.

It does not compute the dyadic carry residue, construct a witness source
with the required progress law, or give an all-input factoring algorithm.
Its use of the arithmetic-progression terminal is conditional on the audited
Gao--Feng--Hu--Pan interface imported by P175.

Throughout,

\[
n=\lceil\log_2(N+1)\rceil,
\]

and numerical QP means (2^{(\log n)^{O(1)}}), with fixed constants.

## Theorem A — primary certificates need no whole-order equality

Let (N>1) be odd. Let

\[
A=\prod_{\ell}\ell^{e_\ell}
\]

be supplied with its complete certified factorization, and suppose

\[
a^A\equiv1\pmod N.
\]

For every \(\ell^{e_\ell}\parallel A\), put

\[
g_\ell=\gcd(a^{A/\ell}-1,N).
\]

If (1<g_\ell<N), it is a proper factor. If (g_\ell=1), then

\[
\boxed{\ell^{e_\ell}\mid r-1\quad\text{for every rational prime }r\mid N.}
\tag{A1}
\]

Consequently, unless a proper factor is returned,

\[
c(A,a)=
\prod_{\substack{\ell^{e_\ell}\parallel A\\g_\ell=1}}
\ell^{e_\ell}
\tag{A2}
\]

is a publicly certified integer satisfying

\[
\boxed{c(A,a)\mid r-1\quad(r\mid N).}
\tag{A3}
\]

No assertion is made that the complete orders of (a) in the hidden local
groups are equal. The certificate consists only of the factored (A), the
global identity, and the displayed gcd-one tests.

For any collection of certified blocks (c_i), their aggregate

\[
M=\operatorname{lcm}_i c_i
\tag{A4}
\]

also divides every (r-1).

## Theorem B — aggregate generalized-CRT terminal

Assume now

\[
N=pq,\qquad p<q<2p,
\tag{B1}
\]

where (p,q) are distinct odd primes. Suppose a certified value

\[
b=p\bmod2^t,\qquad 1\le t\le n,
\tag{B2}
\]

is supplied, and let (M) be any aggregate satisfying (A3). Put

\[
L=\operatorname{lcm}(2^t,M).
\tag{B3}
\]

The two congruences

\[
x\equiv b\pmod{2^t},
\qquad
x\equiv1\pmod M
\tag{B4}
\]

are compatible and determine one residue (s\pmod L). It is computable in
polynomial bit complexity by generalized CRT, and

\[
\boxed{p\equiv s\pmod L,\qquad \gcd(L,N)=1.}
\tag{B5}
\]

Use the canonical (0\le s<L). It is nonzero. First compute
\(\gcd(s,N)\). If this is nontrivial, it is the desired factor. Otherwise
(L<p<N), so (1\le s<L<N), and the arithmetic-progression terminal
applies.

For every fixed numerical-QP function (S(n)\ge1), if

\[
\boxed{
L\ge\frac{N^{1/4}}{S(n)},}
\tag{B6}
\]

then this terminal factors (N) deterministically in numerical-QP bit
complexity. Only new prime-power support counts:

\[
\frac{\operatorname{lcm}(L,c)}L
=\prod_\ell
\ell^{\max\{v_\ell(c)-v_\ell(L),0\}}.
\tag{B7}
\]

In particular, growth of (M) that is already contained in the dyadic
modulus does not enlarge (L).

## Theorem C — exact Las Vegas drift criterion

Fix (S(n)) as in Theorem B and put

\[
H=max\left\{0,
\left\lceil
\log_2\left(\frac{N^{1/4}}{S(n)}\right)
\right\rceil
\right\},
\qquad R_*=2^H.
\tag{C1}
\]

For a current aggregate modulus (L\), define

\[
\Phi(L)=\max\{0,H-\lfloor\log_2L\rfloor\}.
\tag{C2}
\]

A factor is assigned potential zero. A witness stage either returns a
verified factor or a certified block (c), after which

\[
L'=\operatorname{lcm}(L,c).
\tag{C3}
\]

Suppose each stage has numerical-QP bit cost and, for every nonterminal
history \(\mathcal F_k\),

\[
\boxed{
\mathbb E[\Phi_k-\Phi_{k+1}\mid\mathcal F_k]
\ge\frac1{Q(n)}}
\tag{C4}
\]

for one fixed numerical-QP function (Q). Then the procedure reaches a
factor or (L\ge R_*\) almost surely, in expected numerical-QP total bit
complexity. It then factors (N) by Theorem B.

A simpler sufficient condition is

\[
\boxed{
\Pr(\text{factor or }c\nmid L\mid\mathcal F_k)
\ge\frac1{Q(n)}.}
\tag{C5}
\]

Conversely, (C4) implies (C5) with (Q) enlarged by only an (O(n))
factor. Thus conditional inverse-QP mass of a factor or genuinely new
primary support is equivalent, at numerical-QP scale, to this uniform
first-moment per-stage drift condition. Among conditions that use only one
uniform conditional first-moment bound at every nonterminal history, no
independence or tail hypothesis is needed. The condition is not claimed to
be necessary for every source with QP expected stopping time; rare histories
can violate a uniform bound.

For iid witnesses with distribution \(\mu\), the exact useful-event law at
state (L) is

\[
\pi_\mu(L)=
\mu\{\text{proper factor or }c(A,a)\nmid L\}.
\tag{C6}
\]

While failures leave (L) fixed, the waiting time for the next useful
event is geometric with mean (1/\pi_\mu(L)).

## Theorem D — exact primary-level uniform law

Let

\[
N=\prod_{j=1}^{\nu}R_j,
\qquad R_j=r_j^{f_j},
\tag{D1}
\]

be the hidden decomposition into powers of distinct odd rational primes.
Fix a completely factored (A) with

\[
\gcd(A,N)=1,
\tag{D2}
\]

and sample (a) uniformly from \((\mathbb Z/N\mathbb Z)^\times\). Put

\[
h_j=\varphi(R_j),
\qquad
d_j=\gcd(A,h_j)=\gcd(A,r_j-1),
\tag{D3}
\]

\[
B=\prod_{j=1}^{\nu}
\left(1-\frac{d_j}{r_j-1}\right),
\qquad
\Gamma=\prod_{j=1}^{\nu}\frac{d_j}{h_j}.
\tag{D4}
\]

First compute

\[
G_0=\gcd(a^A-1,N).
\tag{D5}
\]

Then

\[
\Pr(G_0=1)=B,
\qquad
\Pr(G_0=N)=\Gamma.
\tag{D6}
\]

Every other outcome is a proper factor. Only when (G_0=N), run every
primary test from Theorem A.

For \(\ell^{e_\ell}\parallel A\), define

\[
c_\ell=
\#\{j:v_\ell(d_j)=e_\ell\}.
\tag{D7}
\]

For a current aggregate modulus (L), put

\[
f_\ell(L)=
\begin{cases}
1,
&c_\ell=0,\\[2mm]
\ell^{-c_\ell},
&0<c_\ell<\nu,\\[2mm]
\ell^{-\nu},
&c_\ell=\nu\text{ and }e_\ell>v_\ell(L),\\[2mm]
\ell^{-\nu}+(1-\ell^{-1})^\nu,
&c_\ell=\nu\text{ and }e_\ell\le v_\ell(L).
\end{cases}
\tag{D8}
\]

The exact probability that one uniform unit returns neither a proper factor
nor strict growth of (L) is

\[
\boxed{
P_{\rm np}(L)
=B+\Gamma\prod_{\ell\mid A}f_\ell(L).}
\tag{D9}
\]

Hence the exact useful-event probability is

\[
\boxed{\pi_A(L)=1-P_{\rm np}(L).}
\tag{D10}
\]

This law is primary-granular: different prime-power contributions may be
accumulated from different witnesses even when no witness has equal complete
local orders.

## Theorem E — attainability and two exact obstructions

Define the hidden common predecessor

\[
D_N=\gcd_{r\mid N}(r-1),
\tag{E1}
\]

where (r) ranges over the distinct rational prime divisors of (N).
Every aggregate built from Theorem A satisfies

\[
\boxed{
M\mid D_N,
\qquad
L\mid\operatorname{lcm}(2^t,D_N).}
\tag{E2}
\]

Thus

\[
\operatorname{lcm}(2^t,D_N)<R_*
\tag{E3}
\]

is an absolute obstruction to reaching the GFHP threshold by aggregate
growth. A factor gcd could still terminate the stage, but no witness choice
can make (M) cross this ceiling.

For a squarefree semiprime (N=pq),

\[
D_N=\gcd(p-1,q-1)\mid q-p.
\tag{E4}
\]

In the uniform (A=N-1) model of P165, write
\(d=D_N\). For every current state,

\[
\boxed{
\Pr(\text{factor or strict aggregate growth})
\le\frac d{p-1}+\frac d{q-1}.}
\tag{E5}
\]

Therefore a bounded gap (q-p\le C) makes (M\le C) and makes the
per-witness useful probability (2^{-\Omega(n)}) on balanced inputs. The
standard bounded-prime-gap theorem supplies an infinite family. Primary
granularity does not remove either obstruction.

There is also a cyclic-direction obstruction. Suppose the hidden local
components of every witness have the synchronized form

\[
(g_1^z,\ldots,g_\nu^z),
\qquad \operatorname{ord}(g_j)=c
\quad(1\le j\le\nu).
\tag{E6}
\]

Every complete local order is then

\[
c/\gcd(c,z),
\tag{E7}
\]

so stripping does not split the components and every accumulated order
divides (c). If the exponents (z) are independent uniform residues
modulo (c), then for every \(\ell\mid c\), the probability that the full
\(\ell\)-primary part of (c) is still absent after (k) witnesses is

\[
\boxed{\ell^{-k}.}
\tag{E8}
\]

Thus iid witnesses can fill one cyclic direction quickly but can never
leave it. If

\[
\operatorname{lcm}(2^t,c)<R_*,
\tag{E9}
\]

the terminal remains unreachable through those witnesses.

## Exact remaining scope

The deterministic aggregate terminal is complete once its premises are
supplied. The missing premise is the progress law.

P160 can feed the terminal on its factored exact-common-order exit, but its
surviving hard unit has large, possibly unequal local orders and supplies no
factored common annihilator or repeated acquisition law. P165 supplies the
uniform root-group data underlying Theorem D, but its bounded-gap family
violates every inverse-QP progress condition in Theorem C. Sampling
independent numerically small integers is outside P165's CRT-uniform law;
independence across trials alone supplies no lower bound on
\(\pi_\mu(L)\).

F220 does not rule out adaptive witnesses, a factor-biased small-integer
source, nonlinear aggregation, or another terminal statistic. Proving
inverse-QP conditional mass of a proper gcd or genuinely new certified
primary support remains the exact missing theorem.
