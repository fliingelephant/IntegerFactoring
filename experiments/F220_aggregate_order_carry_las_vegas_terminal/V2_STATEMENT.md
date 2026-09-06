# F220 V2 candidate — aggregate order/carry terminal and exact Las Vegas progress law

## Status and repair boundary

This is a self-audited, proof-only V2 candidate. V1 and its hostile FAIL are
preserved. V2 repairs exactly the two hostile-audit defects:

1. the actual integer Gao--Feng--Hu--Pan threshold is separated from its
   dyadic upper envelope, and every terminal-obstruction claim uses the
   actual threshold; and
2. the cyclic-direction no-splitting model assumes \(\gcd(c,N)=1\), so its
   torsion injects into every residue field even when \(N\) has repeated
   rational-prime powers.

No promotion is claimed. The surviving V1 claims are restated so V2 can be
audited as a complete packet.

Throughout,

\[
n=\lceil\log_2(N+1)\rceil,
\]

and numerical QP means \(2^{(\log n)^{O(1)}}\), with fixed constants.

## Theorem A — primary certificates without whole-order equality

Let \(N>1\) be odd. Let

\[
A=\prod_\ell \ell^{e_\ell}
\tag{A0}
\]

be supplied with its complete certified factorization, and suppose

\[
a^A\equiv1\pmod N.
\tag{A1}
\]

For every \(\ell^{e_\ell}\parallel A\), put

\[
g_\ell=\gcd(a^{A/\ell}-1,N).
\tag{A2}
\]

If \(1<g_\ell<N\), it is a proper factor. If \(g_\ell=1\), then

\[
\boxed{\ell^{e_\ell}\mid r-1
\quad\text{for every rational prime }r\mid N.}
\tag{A3}
\]

Consequently, unless a proper factor is returned,

\[
c(A,a)=
\prod_{\substack{\ell^{e_\ell}\parallel A\\g_\ell=1}}
\ell^{e_\ell}
\tag{A4}
\]

is publicly certified and satisfies

\[
c(A,a)\mid r-1\qquad(r\mid N).
\tag{A5}
\]

No equality of complete hidden local orders is asserted. For any collection
of certified blocks \(c_i\),

\[
M=\operatorname{lcm}_i c_i
\tag{A6}
\]

also divides every \(r-1\).

## Theorem B — aggregate generalized-CRT terminal

Assume

\[
N=pq,\qquad p<q<2p,
\tag{B1}
\]

where \(p,q\) are distinct odd primes. Suppose a certified value

\[
b=p\bmod2^t,\qquad1\le t\le n,
\tag{B2}
\]

is supplied, and let \(M\) be any aggregate satisfying (A5). Put

\[
L=\operatorname{lcm}(2^t,M).
\tag{B3}
\]

The congruences

\[
x\equiv b\pmod{2^t},
\qquad
x\equiv1\pmod M
\tag{B4}
\]

are compatible and determine one residue \(s\pmod L\). Generalized CRT
computes it in polynomial bit complexity, and

\[
\boxed{p\equiv s\pmod L,\qquad\gcd(L,N)=1.}
\tag{B5}
\]

Choose \(0\le s<L\). It is nonzero. First compute \(\gcd(s,N)\). If it
is nontrivial, it factors \(N\). Otherwise \(L<p<N\), so the imported
Gao--Feng--Hu--Pan arithmetic-progression terminal applies.

Fix a positive numerical-QP function \(S(n)\ge1\), and define the real and
integer thresholds

\[
T_{\rm G}=\frac{N^{1/4}}{S(n)},
\qquad
J_{\rm G}=\lceil T_{\rm G}\rceil.
\tag{B6}
\]

Because \(L\) is an integer,

\[
\boxed{L\ge T_{\rm G}\quad\Longleftrightarrow\quad L\ge J_{\rm G}.}
\tag{B7}
\]

Either condition makes the GFHP cost numerical QP and therefore factors
\(N\) deterministically in numerical-QP bit complexity.

Only new prime-power support enlarges the modulus:

\[
\frac{\operatorname{lcm}(L,c)}L
=\prod_\ell
\ell^{\max\{v_\ell(c)-v_\ell(L),0\}}.
\tag{B8}
\]

In particular, a primary power already contained in \(2^t\) gives no
growth of \(L\).

## Theorem C — exact-target Las Vegas drift criterion

Fix \(S\), \(T_{\rm G}\), and \(J_{\rm G}\) as in (B6). For comparison
only, define the dyadic upper envelope

\[
H=\lceil\log_2J_{\rm G}\rceil,
\qquad
R_*=2^H.
\tag{C1}
\]

Then

\[
J_{\rm G}\le R_*<2J_{\rm G}.
\tag{C2}
\]

The actual stopping target is \(J_{\rm G}\), not \(R_*\). For an
unfactored state with aggregate modulus \(L\), define

\[
\Phi(L)=
\max\left\{0,
\left\lceil\log_2\frac{J_{\rm G}}L\right\rceil
\right\}.
\tag{C3}
\]

A factor is assigned potential zero. Thus \(\Phi(L)=0\) exactly when the
actual integer GFHP threshold has been reached. A witness stage either
returns a verified factor or a certified block \(c\), after which

\[
L'=\operatorname{lcm}(L,c).
\tag{C4}
\]

Suppose every stage has numerical-QP bit cost and, for every nonterminal
history \(\mathcal F_k\),

\[
\boxed{
\mathbb E[\Phi_k-\Phi_{k+1}\mid\mathcal F_k]
\ge\frac1{Q(n)}}
\tag{C5}
\]

for one fixed numerical-QP function \(Q\). Then the procedure reaches a
factor or \(L\ge J_{\rm G}\) almost surely and has expected numerical-QP
total bit complexity. Theorem B then factors \(N\).

A simpler sufficient condition is

\[
\boxed{
\Pr(\text{factor or }c\nmid L\mid\mathcal F_k)
\ge\frac1{Q(n)}.}
\tag{C6}
\]

Conversely, (C5) implies (C6) after enlarging \(Q\) by only an \(O(n)\)
factor. Thus conditional inverse-QP mass of a factor or genuinely new
primary support is equivalent, at numerical-QP scale, to this uniform
one-step drift condition. Independence between stages is not required. A
uniform history-by-history condition is not claimed to be necessary for
every source with QP expected stopping time.

For iid witnesses with law \(\mu\), the exact useful-event probability at
state \(L\) is

\[
\pi_\mu(L)
=\mu\{\text{proper factor or }c(A,a)\nmid L\}.
\tag{C7}
\]

While failures leave \(L\) fixed, the waiting time for the next useful
event is geometric with mean \(1/\pi_\mu(L)\).

## Theorem D — exact primary-level CRT-uniform law

Let

\[
N=\prod_{j=1}^{\nu}R_j,
\qquad
R_j=r_j^{f_j},
\tag{D1}
\]

be the hidden decomposition into powers of distinct odd rational primes.
Fix a completely factored \(A\) with

\[
\gcd(A,N)=1,
\tag{D2}
\]

and sample \(a\) uniformly from \((\mathbb Z/N\mathbb Z)^\times\). Put

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

Every other outcome is a proper factor. Only when \(G_0=N\), run all
primary tests from Theorem A.

For \(\ell^{e_\ell}\parallel A\), define

\[
c_\ell=\#\{j:v_\ell(d_j)=e_\ell\}.
\tag{D7}
\]

For the current aggregate modulus \(L\), put

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
nor strict growth of \(L\) is

\[
\boxed{
P_{\rm np}(L)=B+\Gamma\prod_{\ell\mid A}f_\ell(L).}
\tag{D9}
\]

Hence

\[
\boxed{\pi_A(L)=1-P_{\rm np}(L).}
\tag{D10}
\]

Different witnesses may contribute different prime powers. No witness needs
equal complete local orders.

## Theorem E — exact attainability and source obstructions

Define the hidden common predecessor

\[
D_N=\gcd_{r\mid N}(r-1),
\tag{E1}
\]

where \(r\) ranges over the distinct rational prime divisors of \(N\).
Every aggregate built from Theorem A satisfies

\[
\boxed{
M\mid D_N,
\qquad
L\mid C_N(t):=\operatorname{lcm}(2^t,D_N).}
\tag{E2}
\]

Therefore

\[
\boxed{C_N(t)<J_{\rm G}}
\tag{E3}
\]

is an absolute obstruction to reaching the actual GFHP threshold by
aggregate growth. A proper gcd can still terminate a stage. The weaker
inequality \(C_N(t)<R_*\) obstructs only the dyadic envelope. If

\[
J_{\rm G}\le C_N(t)<R_*,
\tag{E4}
\]

the GFHP threshold can still be attainable; no terminal obstruction is
claimed.

For a squarefree semiprime \(N=pq\),

\[
D_N=\gcd(p-1,q-1)\mid q-p.
\tag{E5}
\]

In the CRT-uniform \(A=N-1\) model of P165, write \(d=D_N\). At every
current state,

\[
\boxed{
\Pr(\text{factor or strict aggregate growth})
\le\frac d{p-1}+\frac d{q-1}.}
\tag{E6}
\]

Thus a bounded gap \(q-p\le C\) forces \(M\le C\) and makes the
per-witness useful probability \(2^{-\Omega(n)}\) on balanced inputs. The
standard bounded-prime-gap theorem supplies an infinite family. Primary
granularity does not remove either conclusion.

There is also a corrected cyclic-direction obstruction. Use the hidden
decomposition (D1). Let \(c\) be supplied with its complete factorization,
and assume

\[
\boxed{\gcd(c,N)=1.}
\tag{E7}
\]

Suppose every witness has synchronized hidden local components

\[
(g_1^z,\ldots,g_\nu^z),
\qquad
\operatorname{ord}_{R_j}(g_j)=c
\quad(1\le j\le\nu).
\tag{E8}
\]

Then every complete local order is

\[
m_z=\frac c{\gcd(c,z)}.
\tag{E9}
\]

Every gcd used by factor-first stripping is \(1\) or \(N\), including for
repeated rational-prime powers. Thus this source never splits \(N\), and
every accumulated exact order or certified primary block divides \(c\).

If the exponents \(z\) are independent uniform residues modulo \(c\), then
for each \(\ell\mid c\), the probability that the full \(\ell\)-primary
part of \(c\) is absent from the lcm after \(k\) witnesses is

\[
\boxed{\ell^{-k}.}
\tag{E10}
\]

This source can fill one cyclic direction quickly but cannot leave it. Put

\[
C_c(t)=\operatorname{lcm}(2^t,c).
\tag{E11}
\]

The condition

\[
\boxed{C_c(t)<J_{\rm G}}
\tag{E12}
\]

makes the actual GFHP threshold unreachable through this source. The
inequality \(C_c(t)<R_*\) alone obstructs only the dyadic envelope.

## Exact remaining scope

The deterministic aggregate terminal is complete once its premises are
supplied. The missing premise is the witness-source progress law.

P160 can feed the terminal on its factored exact-common-order exit. Its
hard-branch theorem does not supply a factored common annihilator or a
repeated acquisition law. P165 supplies the CRT-uniform root-group data
underlying Theorem D, but its bounded-gap family violates every inverse-QP
uniform progress condition in Theorem C. Independent numerically small
integers are outside P165's CRT-uniform law; independence across trials alone
gives no lower bound on \(\pi_\mu(L)\).

F220 V2 does not compute the dyadic carry residue, construct a source with
the required drift, handle arbitrary composites in the terminal, or supply
complete factoring recursion. It does not rule out adaptive witnesses,
factor-biased small-integer sources, nonlinear aggregation, or another
terminal statistic.
