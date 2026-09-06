# F234 candidate — residual log mass and residue rows share exact hit indicators

## Status and boundary

This is a proof-only candidate.  It gives the exact expected residual
logarithmic mass for an arbitrary public random bank of factored shifted
quotient children.  It also proves a single-large-prime dichotomy: every
captured exclusive residual prime already supplies a two-orientation known
residue row, so a terminal-size prime needs no projected-word sampling.
The multiplier word remains useful for combining several subterminal rows
without enumerating all orientations and for saturating a hidden high
primary power after only its rational prime support is exposed.

The closest prior routes are F228, P197, P202, and F233.  F228 gives the
inverse-lift residue identity but no exact random-bank log law.  P197 gives
the beta-two/common-modulus terminal.  P202 gives the projected return law
once a residual becomes small.  F233 identifies deterministic rectangular
banks as projective gap-ratio covers.  F234 differs materially by allowing
an arbitrary public joint distribution on the complete bank and by proving
that saturated order shrink and exposed known-residue support use the same
prime-by-prime hit indicators.  Their logarithmic weights need not agree
when a hidden residual contains a high prime power.

Use the P202 balanced zero-defect state

\[
N=pq,\qquad p<q<2p,\qquad
B=2^{\lfloor n/2\rfloor},\qquad
H={N-1\over B},
\tag{1}
\]

with distinct odd primes.  Put

\[
P=(p-1)_{\rm odd},\quad Q=(q-1)_{\rm odd},\quad
D=\gcd(P,Q),\quad s_p=P/D,\quad s_q=Q/D.
\tag{2}
\]

Let `W_0` be any public completely factored baseline word.  Define

\[
S_p={s_p\over\gcd(s_p,W_0)},\qquad
S_q={s_q\over\gcd(s_q,W_0)}.
\tag{3}
\]

In the main application, `W_0` is the P202 smooth and `H`-supported word,
so every prime in `S_pS_q` is large, exclusive, and coprime to `H`.

Let `mathscr B` be any public random finite multiset of pairs `(u,c)` for
which

\[
A_{u,c}=uH+c>0.
\tag{4}
\]

The law may have arbitrary dependence between pairs and may be selected
adaptively from previous public child values and their complete
factorizations.  It must not use `p`, `q`, their orders, or an equivalent
hidden oracle.  Directly screen every child against `N`.

For the identities below, regard the complete random bank as planned before
the screens.  Its support variables remain mathematically defined on an
outcome with a proper direct gcd, although the actual algorithm stops there.
Thus direct-factor outcomes can only improve the later success bounds; the
log identities do not condition or renormalize the bank law.

## Theorem A — exact arbitrary-bank residual log law

For every prime power `ell^e || S_pS_q`, define

\[
I_\ell(\mathscr B)
=\mathbf1\{\exists (u,c)\in\mathscr B:\ \ell\mid uH+c\},
\qquad
\pi_\ell=\Pr(I_\ell=1).
\tag{5}
\]

Give every exposed child prime the saturating exponent `n` and form

\[
W(\mathscr B)=\operatorname{lcm}\left(
W_0,
\{\operatorname{rad}(uH+c)^n:(u,c)\in\mathscr B\}
\right).
\tag{6}
\]

The two algebraic residuals of the planned saturated word are

\[
\boxed{
r_p(\mathscr B)
=\prod_{\ell^e\parallel S_p}\ell^{e(1-I_\ell)},
\qquad
r_q(\mathscr B)
=\prod_{\ell^e\parallel S_q}\ell^{e(1-I_\ell)}.
}
\tag{7}
\]

No independence between different primes or different children is needed.
Consequently,

\[
\boxed{
\begin{aligned}
\mathbb E\log_2 r_p
&=\log_2S_p-
\sum_{\ell^e\parallel S_p}e\log_2\ell\,\pi_\ell,\\
\mathbb E\log_2 r_q
&=\log_2S_q-
\sum_{\ell^e\parallel S_q}e\log_2\ell\,\pi_\ell.
\end{aligned}}
\tag{8}
\]

For `K` independent draws from one public distribution `mu` on pairs, put

\[
h_\ell
=\sum_{u,c}\mu(u,c)\,
\mathbf1_{\ell\mid uH+c}.
\tag{9}
\]

Then

\[
\boxed{\pi_\ell=1-(1-h_\ell)^K.}
\tag{10}
\]

Equations (8)--(10), not a generic smoothness heuristic, are the exact
expected residual log-mass law.

## Theorem B — every captured exclusive prime is already a residue row

Let `ell` be a prime in `S_pS_q` captured by one pair `(u,c)`, and assume
`ell` divides neither `H` nor `uB`.  This is the large exclusive survivor
of the P202 smooth and `H`-supported baseline; it holds in particular when
the multiplier bank is below the rough-prime cutoff.  Define

\[
z_\ell=1-cB u^{-1}\pmod\ell.
\tag{11}
\]

Child divisibility gives the public identity

\[
\boxed{N\equiv z_\ell\pmod\ell.}
\tag{12}
\]

More generally, if `ell^f|uH+c`, then the same identity holds modulo every
public level `ell^j`, `1<=j<=f`, with `u^{-1}` computed modulo `ell^j`.
If `ell^e` is the hidden residual primary, the unordered factor row below
is valid through every level `j<=min(e,f)`.  The algorithm need not know
`e`: it can try all public levels through `f` and verify every result.

Since `ell` is exclusive,

\[
\boxed{
\{p,q\}\equiv\{1,z_\ell\}\pmod\ell,
\qquad z_\ell\ne1.
}
\tag{13}
\]

Thus capture and known-residue exposure are the same rational-prime event.
The only orientation ambiguity modulo `ell` is the one bit that assigns
`ell` to `p-1` or `q-1`.  A single occurrence of `ell` in a child need not
certify a hidden higher congruence modulo `ell^e`, even though the multiplier
word can raise `ell` to exponent `n` and saturate that hidden primary order.

Operationally, factor every screened child and enumerate every distinct
prime `ell` in its factorization with `ell` dividing neither `HuB` nor `N`.
For each public child valuation `f`, enumerate `1<=j<=f` and the two rows
obtained by replacing `ell` with `ell^j` in (15).  This enumeration does not
assume that `ell` is residual-supported.  A nonresidual prime merely gives
false rows, whose terminal outputs are discarded unless a gcd verifies a
proper divisor.

Let the current beta-two/common-order state give a public residue

\[
p\equiv s_0\pmod {L_0},
\qquad L_0=\operatorname{lcm}(2^t,M),\quad M\mid D.
\tag{14}
\]

The exclusive prime is coprime to `L_0`.  Combine (14) with each of the two
possibilities

\[
p\equiv1\pmod\ell,
\qquad
p\equiv z_\ell\pmod\ell.
\tag{15}
\]

One CRT row is correct.  Therefore, if

\[
L_0\ell\ge
J=\left\lceil{N^{1/4}\over S_0(n)}\right\rceil
\tag{16}
\]

for the verified known-residue terminal and a fixed numerical-QP `S_0`,
trying both rows factors `N` deterministically in numerical-QP time.  No
projected random unit or common-order generator is needed for this
single-prime terminal.

If `K` children of numerical-QP total bit length are factored, the total
number of prime occurrences with multiplicity is at most that bit length.
The complete prime-power-level and two-orientation enumeration is therefore
numerical QP.  For each row, first reduce the CRT residue `s` modulo its
combined modulus `L`, compute `gcd(s,N)`, and return a proper gcd.  If
`L>=N` and the gcd is trivial, skip that false row.  Otherwise invoke the
deterministic known-residue routine and gcd-verify every returned candidate.
On the correct row, either `L>p` exposes `p` in the preliminary gcd, or
`L<p<N` satisfies the known-residue interface.  Thus nonresidual primes and
wrong orientations affect cost only by the QP enumeration factor.

For several subterminal captured primes, direct CRT enumeration has one
orientation bit per prime and can be exponential.  Also, one exposed small
prime can have a hidden high residual valuation that the modulus-`ell` row
does not certify.  The P202 multiplier word handles both cases: it uses the
same exposed rational-prime support, raises it to saturating valuation, and
changes the two local return kernels without choosing orientations.  These
are the exact surviving roles of the word route.

## Theorem C — a sufficient harmonic-mass condition

For one orientation, write

\[
L_p=\log_2S_p,
\qquad
X_p=\log_2{S_p\over r_p}
=\sum_{\ell^e\parallel S_p}e\log_2\ell\,I_\ell.
\tag{17}
\]

Fix a public numerical-QP residual target `R>=3` and put

\[
T_p=\max\{0,\log_2(S_p/R)\}.
\tag{18}
\]

If `S_p>R` and, at every reached history,

\[
\boxed{
\mathbb E X_p\ge T_p+\delta(n)
}
\tag{19}
\]

for a public `delta(n)>0`, then

\[
\mathbb E\log_2r_p\le\log_2R-\delta(n),
\tag{20a}
\]

and

\[
\boxed{
\Pr(r_p\le R)
\ge {\delta(n)\over L_p-T_p}
={\delta(n)\over\log_2R}.
}
\tag{20}
\]

The same statement holds with `q` in place of `p`.  Conditional on
`min(r_p,r_q)<=R`, the P202 projected stage has factor-or-growth probability
at least `1/R`: it is at least `2/3` if a residual is one, and the direct
factor term is at least `1/min(r_p,r_q)` when both are nontrivial.  Hence
(19) for either hidden orientation gives unconditional factor-or-growth
probability at least

\[
\boxed{{\delta(n)\over R\log_2R}.}
\tag{21}
\]

An inverse-QP `delta` and numerical-QP `R` therefore suffice for the P197
history-wise Las Vegas drift target, conditional on the same recursive
factoring dispatcher and per-bank QP bit cost as P202.

Equation (19) is an exact harmonic-support condition.  F234 does not prove
it for every input.  By Theorem B, every positive summand uses an exposed
residue-row prime.  Its weight `e log ell` is saturated order mass, not
necessarily certified known-residue modulus mass when `e>1`; there is no
second hidden rational-prime source.

If `S_p` is exponential while `R` is numerical QP, (19) says that the bank
must capture all but at most `log_2R-delta` of the expected weighted
residual log mass.  A small average fraction of hits is not sufficient.
