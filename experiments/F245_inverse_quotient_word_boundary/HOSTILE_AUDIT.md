# Hostile audit of F245

## Authentication

The audited inputs matched the required SHA-256 digests before they were
read:

- `STATEMENT.md`:
  `c12d744be03815b942010c13637225a9d889f7724f1f5c95c4e5dc35d2a05a21`
- `PROOF.md`:
  `4d1580cebb9bdfcd82a6db332a9cc5e146cc2e68b91bd63c6057898c92c8b30a`
- `SELF_AUDIT.md`:
  `e15ac05a5de7f070000299afe6d7f06bf5f988f9ed52834affc8e1a9cb0d2256`
- `PROVENANCE.md`:
  `c0448f5aa54999c0b55086fa890f28dcfc662032186756c15f3d88990b9e2b7f`
- `MANIFEST.md`:
  `3d129d3ed943e93342273ff5ce3db7de97d5259fb7cc0b1bcc314f001851f5fa`

## Verdict

**PASS, for the stated scoped boundary and conditional on the exact imported
F244/P208 interfaces.** I found no error in the new inverse-quotient atom
bound, the history-wise adaptive union bound, the numerical-QP asymptotics,
or the signed/noncanonical Hilbert--90 identities. Equations (5)--(6) do not
inherit the uniform inverse-seed probability bound, and the packet correctly
does not claim that they do.

This audit does not independently certify the upstream construction of the
four F244 markers, its incidental-exit estimate, its common-order capacity,
or the clean P208 interface. Those facts are imported by provenance and are
not proved in this F245-only packet. The F245 deduction from them is valid.

## 1. Inverse-quotient fibres and constants

If (K(u)=k), then (uv=Nk+1). Conversely, if
(u\mid Nk+1) and (k<u<N), then

\[
v={Nk+1\over u}
\]

is a positive integer smaller than (N). Also
(gcd(u,N)=1), since a common prime divisor would divide both (Nk) and
(Nk+1). Thus (v) is the canonical inverse of (u), and

\[
K^{-1}(k)=\{u:k<u<N,\ u\mid Nk+1\}.
\]

For (0\le k<N), one has (Nk+1<N^2), so each fibre has size at most
(Delta_N). Uniformity on the (arphi(N)) units gives the claimed atom
bound.

The only solution of (K(u)=0) is (u=v=1). Replacing (0) by (1)
merges the atoms at (0) and (1), and no others. Therefore the safe bound
(2Delta_N/\varphi(N)) for every atom of (widehat K) is correct.

There are at most (lceil N/\ell\rceil) representatives from
({0,\ldots,N-1\}) in one residue class. For distinct odd primes (p,q),

\[
{N\over\varphi(N)}={p\over p-1}{q\over q-1}\le {15\over8},
\]

with the maximum attained at (3,5). Since (ell<N),
(lceil N/\ell\rceil<2N/\ell). Hence

\[
{2\lceil N/\ell\rceil\Delta_N\over\varphi(N)}
< {4N\Delta_N\over\ell\varphi(N)}
\le {15\Delta_N\over2\ell}
< {8\Delta_N\over\ell}.
\]

All constants in (1) are therefore safe.

For two quotient values, residue masses (ho_r) satisfy

\[
\Pr(K_i\equiv K_j\pmod\ell)=\sum_r\rho_r^2
\le\max_r\rho_r\le\beta_{N,\ell}.
\]

When (K_i=K_j), the difference factor is set to (1), so that event is
deleted rather than added. This proves both bounds in (2), with slack in the
difference bound because (eta_{N,\ell}) includes the zero-to-one factor
of two.

## 2. Adaptive conditional uniformity

The adaptive quantifier is strong enough. If, after every full prior
transcript (H_{j-1}), the next seed satisfies

\[
\Pr(U_j=u\mid H_{j-1})={1\over\varphi(N)}
\]

for every canonical unit (u), then its quotient has the same fixed law
after conditioning on any history. For a pair (i<j), condition on the
history through seed (i). The earlier quotient is then fixed, while the
later quotient retains the residue-mass bound. Thus

\[
\Pr(\ell\mid\Gamma_{ij}\mid H_{j-1})\le\beta_{N,\ell}.
\]

Marginal uniformity would not suffice, but the statement explicitly uses
conditional uniformity after the complete past.

Post-transcript selection causes no postselection gap. Pathwise, if a prime
divides the selected positive product, it already divides at least one of
the at most (Q) quotient factors or ({Q\choose2}) unequal-difference
factors in the full available bank. A union bound over the full bank proves
(3), even if the final subset and its positive exponents are chosen after
all values are known.

The same proof covers an adaptive stopping rule with at most (Q) seeds:
for the (j)-th possible seed or pair, multiply its conditional incidence
bound by the indicator that the seed is actually requested, then take
expectations. No independence between bank-incidence events is needed.

## 3. Divisor maximum and marker incidence

The standard maximal-order estimate gives

\[
\log\Delta_N=O\!\left({\log N\over\log\log N}\right),
\qquad
\Delta_N=2^{O(n/\log n)}=2^{o(n)}.
\]

The strict range (m<N^2) in the definition of (Delta_N) covers every
(Nk+1) used by the fibre argument. There is no hidden replacement of a
subexponential bound by a polynomial one.

For every fixed numerical quasipolynomial
(Q(n)=2^{C(\log_2(n+1))^k}), both (Q) and (Q^2) are (2^{o(n)}).
For a marker (ell>2^{cn}), (1)--(3) give

\[
\Pr(\ell\mid W_{\rm iq})
\le O(Q(n)^2){8\Delta_N\over\ell}
=2^{-cn+o(n)}=2^{-\Omega(n)}.
\]

A further union bound over four markers preserves the exponent and proves
(4). The quantifier must remain “for every fixed numerical-QP (Q)”; the
proof does not permit (C) or (k) to grow with (n), and the statement
does not do so.

## 4. Combination with the F244 markers

Assume the imported F244 facts exactly as cited: four distinct primes
(lambda_+,\lambda_-,\rho_+,\rho_->2^{cn}), pathwise avoidance by every
allowed numerical-QP-bit signed-power word, and total shifted common-order
lcm dividing (12).

The square baseline is itself the signed-power word

\[
(N^2-1)^n=|N^2-1|^n,
\]

with (k=2), sign (+1), and (O(n^2)) bits. Thus the imported avoidance
property makes every marker exterior to (N^2-1). For example, if
(lambda_a\mid p-a) also divided either (q-1) or (q+1), then it would
divide (N^2-1), a contradiction. Hence (lambda_a) survives the shifted
gcd on the (p)-side for every (q)-orientation; the analogous statement
holds for (ho_b) on the (q)-side.

On the event in which (W_{\rm iq}) captures none of the four markers,
the baseline, the signed-power word, and the inverse-quotient word all miss
the relevant marker on each side of every orientation. A clean uniform
local powered return has probability at most (1/\lambda_a) on one side
and (1/\rho_b) on the other, so a union bound gives

\[
{1\over\lambda_a}+{1\over\rho_b}=2^{-\Omega(n)}.
\]

Numerical-QP many trials preserve this exponential upper bound. An lcm
dividing (12) cannot absorb any exponential marker. This proves the F245
combination, conditional on the cited clean-trial and incidental-exit parts
of the F244/P208 interface.

For a formal expected-time Las Vegas reading, one additional sentence is
implicit but valid: an algorithm with expected numerical-QP time finishes
within twice that bound with probability at least (1/2) by Markov's
inequality. The uniform truncated transcript has numerical-QP many seeds,
trials, and output bits, contradicting the exponential success upper bound.
Thus an unbounded Las Vegas tail does not evade this scoped boundary.

## 5. Signed and noncanonical Hilbert--90 norm

No canonical or positivity assumption on the full integer (g) is needed.
Let (r\in\{1,\ldots,N-1\}) be the canonical residue of (g), and write

\[
g=r+tN,
\qquad t\in\mathbb Z.
\]

The inverse (v) in the statement is also the canonical inverse of (r),
so the signed quotient is

\[
\widetilde d={gv-1\over N}
={rv-1\over N}+tv
=K(r)+tv.
\]

It is integral for positive, negative, or noncanonical (g), but it need
not lie in the support or obey the distributional bound of the canonical
uniform variable (K(U)). This is exactly why no probability conclusion
may be transferred to (5)--(6).

From

\[
X=Av-Nq_A,qquad Y=Bv-Nq_B,qquad gv-1=N\widetilde d,
\]

direct expansion gives

\[
{gX-A\over N}=A\widetilde d-gq_A,
\qquad
{gY-B\over N}=B\widetilde d-gq_B.
\]

These remain valid when any displayed full integer is negative. Also

\[
A^2-DB^2
=(a^2+Db^2)^2-D(2ab)^2
=(a^2-Db^2)^2=g^2.
\]

Substituting (gX=A+Nk) and (gY=B+Nl) gives

\[
g^2(X^2-DY^2-1)
=2N(Ak-DBl)+N^2(k^2-Dl^2),
\]

and division by (Ng^2) proves (6). Since (gcd(g,N)=1), the modular
inverse exists; since (g\ne0), division by (g^2) is legitimate. The
left side is an integer because
(X^2-DY^2\equiv v^2(A^2-DB^2)\equiv1\pmod N).

Thus (5)--(6) are exact public algebraic reductions, including for signed
and noncanonical (g). They are not members of the multiplicative grammar
in (3): (t v,q_A,q_B), products, sums, and the norm expression can have
biased distributions. The stated open scope is necessary and correct.

## 6. Quantifier and interface qualifications

No item below changes the PASS verdict, but each is required for a literal
use of the result.

1. The signed-power grammar inherited from F244 must require positive
   integer (k_j,e_j) and nonzero positive factors. If (k_j=0) and
   (sigma_j=+1) were allowed, the factor would be zero and the avoidance
   assertion would be false. The F245 display does not restate these domains.
2. “Conditionally uniform” must mean exact uniformity after the entire
   filtration, not only uniform marginals. The proof uses the stronger and
   explicitly stated reading.
3. Polynomial bit cost for (5)--(6) is polynomial in the explicit encodings
   of (a,b,D,N). To place these formulas inside an (n)-QP algorithm, the
   public inputs must themselves have (n)-QP bit length.
4. The result is a product-word boundary. It does not bound biased seeds,
   nonlinear transforms, or a decoder that extracts information without
   first forcing a relevant prime into one of the bank factors. The final
   scope says this explicitly.

Subject to those exact interfaces, no hostile counterexample survives.
