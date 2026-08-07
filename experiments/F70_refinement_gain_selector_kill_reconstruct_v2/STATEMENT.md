# Proof-blind reconstruction target: refinement-created subgroup expansion

Read only this statement. Do not read any other F70 file, audit, reconstruction,
project theorem file, registry, progress note, or git history. Reconstruct all
claims independently. Report PASS only if every claim and scope boundary
follows.

## Definitions and accounting

All endpoints below are positive integers. A transcript has pairwise-coprime
nontrivial gcd-free blocks \(Q\). A legal whole-block occurrence product has
the form

\[
g=\prod_{q\in Q}q^{e_q},
\qquad
0\le e_q\le E_q,
\qquad
1<g<N,
\]

where \(E_q\) is the available occurrence exponent. Append the canonical
inverse relation \(gw=1+kN\), and jointly gcd-refine all old and new positive
endpoints.

Let \(\sigma\) be the sum, over old block types, of “number of nontrivial
descendants minus one.” Let \(\nu\) be the number of new refined block types
that divide no old block. If \(r,r'\) are the old and new block counts, prove

\[
r'=r+\sigma+\nu. \tag{A1}
\]

For a fixed finite transcript, assume every final block occurs in at least one
endpoint. Let \(R\) be its final number of distinct nontrivial blocks and

\[
L=\sum_x\left\lceil\log_2(x+1)\right\rceil
\]

over all positive endpoints. Prove

\[
R\le L,
\qquad
\sum_t(\sigma_t+\nu_t)=R-r_0\le L-r_0. \tag{A2}
\]

Explain why (A2) is not a polynomial stopping bound for an adaptive run.

For every inverse pair \(gw\equiv1\pmod N\), define the immediate screens as

\[
\gcd(g-1,N),\quad
\gcd(g+1,N),\quad
\gcd(g-w,N),\quad
\gcd((g-w)^2+4,N),
\]

plus the exact integer-square test on \(gw\). A screen succeeds only when it
returns a proper factor, or when the square test gives a non-global root.

## Separator-free subgroup at \(N=4033\)

Verify

\[
N=4033=37\cdot109=\Phi_{36}(2),
\]

\[
2^{18}=-1\pmod {37},\quad2^{12}=26\pmod {37},
\]

\[
2^{18}=-1\pmod {109},\quad2^{12}=63\pmod {109}.
\]

Prove that \(2\) has order \(36\) modulo both primes. Deduce that
\(H_0=\langle2\rangle\) has no element equal to one chosen sign in exactly
one CRT component, so no \(h\in H_0\) gives a proper
\(\gcd(h\pm1,N)\).

## Infinite immediate-square family

Let \(s>1\) be odd with \(s\equiv1\pmod3\), and put

\[
N_s=\frac{4s^2-1}{3}
=(2s-1)\frac{2s+1}{3}.
\]

Prove that the two factors are coprime odd integers greater than one. Verify

\[
N_s+1=2\frac{2s^2+1}{3}.
\]

Two indexed copies of the relation value \(N_s+1\) authorize two occurrences
of its block \(2\), hence the legal choice \(g=4\). Prove that the old
square-class kernel has only the duplicate dependency and that its root is
global. Then prove

\[
w=s^2,\qquad
gw=4s^2=1+3N_s=(2s)^2,
\]

and show that \(2s\) splits \(N_s\).

For \(s\equiv55\pmod {1530}\), verify that all four declared gcd screens fail
before the exact-square screen succeeds.

At \(s=55\), verify \(N=4033\), \(g=4\), \(w=3025\), and
\(\sigma=0\). The new endpoint supplies private block data, so do not claim
zero total gain. Prove only that positive old-block splitting is unnecessary
for immediate useful feedback.

## Strict expansion at \(N=4033\)

Start from

\[
2\cdot2017=1+N,
\quad
64\cdot3970=1+63N,
\quad
8\cdot3529=1+7N.
\]

Verify complete refinement and the old subgroup:

\[
Q_0=\{2,2017,1985,3529\},
\qquad
H(Q_0)=H_0=\langle2\rangle.
\]

The available occurrence exponents authorize

\[
g=2^{11}=2048<N.
\]

Verify that its canonical inverse is \(w=3905\) and

\[
gw=1+1983N.
\]

Prove that every declared immediate screen fails.

The containment \(\gcd(2,2048)=2\) reuses the whole old block and does not
split it. Prove that the only overlap that properly splits an old block is

\[
\gcd(1985,3905)=5.
\]

Verify

\[
1985=5\cdot397,\qquad3905=5\cdot781,
\]

\[
Q_1=\{2,2017,5,397,3529,781\},
\qquad
\sigma=1,\quad\nu=1.
\]

Show that private block \(781\) occurs oddly only in the appended relation,
so the new square-class column does not close.

Prove

\[
H(Q_1)=\langle H_0,5\rangle\supsetneq H_0
\]

from

\[
5=2^{23}\pmod {37},
\qquad
2^{23}=77\ne5\pmod {109}.
\]

Verify that the enlarged subgroup contains

\[
x=5\cdot2^{-23}=5\cdot2^{13}=630\pmod {4033},
\qquad
\gcd(x-1,4033)=37.
\]

Define the exact positive whole-block occurrence box as the products
\(\prod_{q\in Q_1}q^{e_q}\) with nonnegative exponents bounded by the
available occurrences and with value below \(N\). Prove that it cannot contain
the canonical representative \(630\). Explain why
\(5\cdot2^{13}\equiv630\pmod {4033}\) uses modular reduction and is a
different source operation.

## Classification

Decide whether the proof establishes this narrow result:

> Endpoint gcd refinement can expose a generator outside a separator-free old
> subgroup and enlarge it to a subgroup containing a factor-bearing element,
> although both feedback endpoint residues lie in the old subgroup.

State that it proves no uniform sampler, polynomial stopping bound, all-input
success theorem, stand-alone ranking law for \(\sigma\), or factoring
algorithm.
