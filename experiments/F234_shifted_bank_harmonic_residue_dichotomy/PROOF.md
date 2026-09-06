# Proof of the F234 harmonic-residue dichotomy

## 1. Saturated primary support

Fix an outcome of the random public bank.  Every primary exponent in
`S_pS_q<N` is less than `n`.  If a child `uH+c` contains a prime `ell`, the
factor `rad(uH+c)^n` in (6) contains the full `ell`-primary part of either
hidden residual.  If no child contains `ell`, the bank adds no copy of that
prime.  This proves (7) prime by prime.

Taking binary logarithms gives

\[
\log_2r_p
=\sum_{\ell^e\parallel S_p}
e\log_2\ell\,(1-I_\ell).
\]

Linearity of expectation proves the first identity in (8), with no
independence assumption.  The second is identical.

If a planned child has a proper gcd with `N`, the operational algorithm
stops before constructing the full word.  Keeping its indicator in the
planned-bank random variable does not condition the distribution and does
not remove a success.  On the complementary path all children are units
modulo `N` and the word is valid for the P202 stage.

For `K` independent draws from `mu`, a fixed prime is missed exactly when
all `K` draws avoid the incidence set in (9).  This has probability
`(1-h_ell)^K`, which proves (10).  Different prime-hit indicators can remain
arbitrarily dependent.

## 2. The residue row attached to every hit

If `ell|uH+c`, multiply by `B` and use `BH=N-1`:

\[
u(N-1)+cB\equiv0\pmod\ell.
\]

When `ell` does not divide `uB`, division by `u` gives

\[
N\equiv1-cBu^{-1}=z_\ell\pmod\ell,
\]

proving (12).

If `ell^f|uH+c`, the same calculation is valid modulo `ell^j` for every
`j<=f`, because `ell` does not divide `uB`.  If, in the `S_p` orientation,
`ell^e|s_p`, then `p=1 mod ell^j` for every `j<=e`; hence
`q=N mod ell^j` for every `j<=min(e,f)`.  The `S_q` orientation is
symmetric.  This proves the prime-power qualification without revealing the
hidden exponent `e`.

If `ell|S_p`, then `ell|s_p` and therefore `p=1 mod ell`.  The product
identity `pq=N` gives `q=N=z_ell mod ell`.  If `ell|S_q`, the roles reverse.
The prime cannot occur in both `S_p` and `S_q`, since `gcd(s_p,s_q)=1`.

It remains to show `z_ell!=1`.  If equality held in the `S_p` orientation,
then both `p` and `q` would be one modulo `ell`; hence `ell` would divide
both odd local orders and its complete shared minimum valuation would occur
in `D`.  Because `D|H`, that shared prime would divide `H`, contrary to the
explicit hypothesis of Theorem B.  The `S_q` orientation is symmetric.
This proves (13).

The current modulus `L_0` has only a two-primary part and odd primes from
`M|D`.  An exclusive prime in `S_pS_q` divides neither, so
`gcd(L_0,ell)=1`.  Generalized CRT therefore gives exactly one row modulo
`L_0 ell` for each alternative in (15).  One is the true residue of `p`.
When (16) holds, the verified P197 known-residue terminal applied to both
rows returns and verifies a factor on the correct row.  The wrong row cannot
create an incorrect output because every returned divisor is gcd-verified.

The operational algorithm does not test hidden membership in `S_pS_q`.
It enumerates every prime occurrence in the supplied child factorizations,
skips the publicly recognizable cases dividing `HuB` or `N`, and tries
every public valuation level and both orientations.  The sum of all child
prime exponents is at most the sum of their binary lengths, so the number of
rows is numerical QP whenever the bank representation is.  A false row is
handled by the same bounded deterministic routine and cannot return an
unverified divisor.

For a combined modulus `L`, reduce the row to its canonical residue `s`.
On the correct row, `p=s mod L`.  If `L>p`, then `s=p` and `gcd(s,N)`
factors; equality `L=p` is impossible because the residual prime and `L_0`
are units modulo `N`.  If the preliminary gcd is trivial, the correct row
has `L<p<N`, which is the P197 known-residue interface.  A false row with
`L>=N` is skipped after its trivial gcd; this avoids applying a promised
interface outside its declared modulus range.  This proves the QP and
verification claims for the full visible list, not only for hidden-positive
rows.

For `k` independent exclusive primes, the unordered rows allow up to `2^k`
orientations.  No QP bound follows from naive enumeration when `k` grows.
Moreover, observing `ell` in a child proves only the displayed row modulo
`ell`; it need not prove a row modulo the full hidden residual power
`ell^e`.  The P202 projected test raises exposed support to exponent `n` and
uses the lcm word without learning either the orientations or the hidden
valuations.  This proves the stated division of labor.

## 3. Harmonic surplus implies an inverse-QP favorable event

Equations (7) and (17) give

\[
0\le X_p\le L_p,
\qquad
r_p\le R\iff X_p\ge T_p
\]

when `S_p>R`.  Let

\[
\alpha=\Pr(X_p\ge T_p).
\]

On the complementary event, `X_p<T_p`, and on the favorable event
`X_p<=L_p`.  Hence

\[
\mathbb EX_p
\le T_p(1-\alpha)+L_p\alpha
=T_p+(L_p-T_p)\alpha.
\]

Combining with (19) gives the first bound in (20).  Since `S_p>R`,

\[
L_p-T_p=\log_2R.
\]

This proves the equality in (20).  Equivalently, (8), (17), and (19) give
(20a) directly; applying Markov to the nonnegative random variable
`log_2r_p` gives the same probability bound.  If `S_p<=R`, the favorable
event already has probability one and no surplus condition is needed.

Suppose now `min(r_p,r_q)<=R`.  If one residual is one, P202 gives
history-wise factor-or-growth probability at least `2/3`, which is at least
`1/R` for `R>=3`.  If both are nontrivial, they are odd and P202's exact
direct-factor term is at least the reciprocal of the smaller residual,
hence at least `1/R`.  Use a fresh projected unit after the bank, so this
conditional probability is valid for every no-direct-factor bank outcome.
A direct-factor outcome succeeds with probability one, also at least
`1/R`.  Multiplication by the favorable planned-bank probability in (20)
therefore proves (21) without conditioning away direct hits.

Finally, taking expectations in (17) reproduces the weighted sum in (8).
Thus (19) is precisely a lower bound on expected captured logarithmic
prime-power order mass.  Theorem B identifies the hit indicator of every
positive summand with an exposed two-orientation residue row modulo its
rational prime.  The weight can be larger than the log of that certified
row when a hidden primary valuation exceeds one.  No generic ring operation
creates an additional rational-prime support event.
