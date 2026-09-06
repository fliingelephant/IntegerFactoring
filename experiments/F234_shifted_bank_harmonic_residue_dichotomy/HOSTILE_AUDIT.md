# F234 hostile audit

## Verdict

**FAIL.**  The arbitrary-bank residual identities, the iid specialization,
the conditional residue-row theorem, and the harmonic-surplus probability
bound survive reconstruction.  Promotion is blocked by two operational
quantifier defects in the frozen packet.

1. The arbitrary-bank hit indicator in Theorem A is not the same as the
   eligible-row indicator used by Theorem B and by the stated algorithm.
   A residual prime can be captured only through a pair with `ell|u`; the
   word then saturates that hidden primary, but the operational enumeration
   explicitly skips the prime because it divides `uB`.  Thus the final claim
   that every positive summand in (17) uses a Theorem-B row is false for the
   declared arbitrary bank.
2. The full visible-list procedure invokes the deterministic known-residue
   routine on every row with `L<N`.  It does not first require the public
   terminal condition `L>=J`.  The imported terminal has numerical-QP cost
   only at that threshold.  A QP number of subthreshold calls need not have
   QP cost.

Both defects have direct repairs.  Neither refutes the exact log-mass law or
the conditional progress inequality.  I edited no frozen input and ran no
unregistered computation.  I wrote only this audit.

## Frozen-input authentication

I enumerated the directory and computed all content hashes before reading
the packet.  Every frozen content hash matched `MANIFEST.md`.

| File | Expected and observed SHA-256 |
|---|---|
| `STATEMENT.md` | `2429f9845ba515bebd0e7cf7312e7dce4e387b599a347956f609f66e30bdd172` |
| `PROOF.md` | `fbbb4fa2e5ceb93b82d9d8b94b6cc32144fc88fcc409d993b2fad4e29ff3457a` |
| `SELF_AUDIT.md` | `28bc361469f89fd8c5e407537d8e38878158b3a6e71734f88df406cc498a9548` |
| `PROVENANCE.md` | `4cd73c676f7325a20cb6486479795879a42235ad7b437585c956934ffb356c01` |

The observed SHA-256 of `MANIFEST.md` is
`c13f0f90590eb829a8612263a234042c10ec3346fa0253c8bbbc2a3519e513c4`.

## 1. The exact arbitrary-bank identities survive

Fix one outcome of the complete planned bank.  If
`ell^e || S_p`, then `ell^e<N`; hence `e<n`.  A hit contributes
`ell^n` through `rad(uH+c)^n` and therefore removes the entire remaining
`ell`-primary part.  A miss contributes no new `ell`-power, leaving exactly
the primary already present in `S_p`.  This proves

\[
r_p=\prod_{\ell^e\parallel S_p}\ell^{e(1-I_\ell)},
\]

and the `q` identity is identical.  This argument correctly distinguishes
the observed valuation of a child from the possibly larger hidden residual
valuation: one observed rational-prime occurrence is enough because the
word deliberately raises that prime to exponent `n`.

Taking logarithms and applying linearity of expectation proves (8).  No
independence between primes, children, or adaptive decisions is used.  An
adaptive finite bank has one joint law after its random tape is fixed.  It
can be extended arbitrarily after an operational direct-factor stop.  On
such an outcome the factor is already a success; on a no-direct-factor
outcome the whole planned bank is operationally available.  Therefore this
planned-law convention does not condition or renormalize the identities.

For `K` independent draws from `mu`, a fixed prime is missed precisely when
all draws avoid its incidence set.  The miss probability is
`(1-h_ell)^K`, so (10) is exact.  It does not imply independence between the
hit indicators for two different primes, and the packet does not use such
independence.

The lcm word also has acceptable conditional size.  Its extra logarithmic
height is at most `n` times the aggregate child logarithmic height.  Thus a
bank of numerical-QP total encoding length still gives a numerical-QP word,
conditional on the declared correct recursive child-factorization
dispatcher.

## 2. Promotion blocker: the two hit indicators differ

Theorem B is correct under its displayed assumption `ell` not dividing
`HuB`.  From `ell|uH+c`, multiplication by `B` gives

\[
u(N-1)+cB\equiv0\pmod\ell.
\]

Since `u` is then invertible, this yields

\[
N\equiv1-cBu^{-1}=z_\ell\pmod\ell.
\]

If `ell|S_p`, then `p=1 mod ell` and `q=z_ell mod ell`; the `S_q`
case reverses the two residues.  If `z_ell=1`, both hidden primes are one
modulo `ell`, so `ell|D|H`, contradicting the hypothesis.  The same
`ell`-not-dividing-`H` hypothesis gives `ell` not dividing `D`; hence it is
coprime to `L_0=lcm(2^t,M)` when `M|D`.  The prime-power statement through
`j<=min(e,f)` is also correct because `u` remains invertible modulo
`ell^j`.

This conditional theorem does not identify every Theorem-A hit.  The
zero-defect example already recorded in the promoted frontier makes the
failure explicit:

\[
N=2881=43\cdot67,\qquad B=64,\qquad H=45,
\]

\[
P=21,\qquad Q=33,\qquad D=3,\qquad(s_p,s_q)=(7,11).
\]

Take any allowed baseline that does not contain `7`, for example the
smooth baseline at cutoff `5`, and take the one-pair deterministic bank

\[
(u,c)=(7,7),\qquad uH+c=322=2\cdot7\cdot23.
\]

The direct gcd with `N` is trivial.  The prime `7` lies in `S_p`, and
`I_7=1`, so (7) correctly saturates the complete hidden `7`-primary
residual and (17) receives the positive mass `log_2 7`.  But `7|uB`, so
the operational rule in lines 182--188 of `STATEMENT.md` skips this
occurrence.  With this one-pair bank there is no eligible Theorem-B hit for
`7`.

Therefore the frozen conclusions

- “capture and known-residue exposure are the same rational-prime event,”
- “every positive summand uses an exposed two-orientation residue row,” and
- the self-audit assertion that every exposed child prime is tried

do not follow at the declared arbitrary-bank quantifiers.

The cleanest repair is stronger than the current inverse-lift formula.
After any child factorization exposes a prime `ell` not dividing `N`, the
algorithm can directly compute `N mod ell` and try the unordered row
`{1,N mod ell}`.  No inverse of `u` is needed.  Alternatively, a repaired
statement can restrict the bank so that every surviving residual prime is
larger than every multiplier, or require `gcd(u,c)=1`, and can define its
row indicator using only eligible hits.  The frozen packet does none of
these.

## 3. Promotion blocker: subthreshold false rows are not QP-certified

For one eligible exposed prime, the CRT argument is correct.  One of

\[
p\equiv1\pmod\ell,
\qquad
p\equiv z_\ell\pmod\ell
\]

is compatible with the true residue modulo `L_0`.  Coprimality gives a row
modulo `L=L_0 ell`.  If `L>p`, its canonical true residue is exactly `p`
and the preliminary gcd factors `N`.  Equality `L=p` is impossible because
`gcd(L,N)=1`.  If `L<p` and `L>=J`, the imported verified known-residue
terminal applies.  False rows cannot produce a false factor because all
outputs are gcd-verified.

The aggregate number of exposed prime-power levels is at most the aggregate
child bit length, so enumerating the rows is QP.  That count does not make
every terminal call QP.  The frozen operational paragraph says to skip a
row only when `L>=N` and its preliminary gcd is trivial; it says to invoke
the deterministic known-residue routine otherwise.  For a public row with

\[
L<J=\left\lceil N^{1/4}/S_0(n)\right\rceil,
\]

the P197/GFHP numerical-QP guarantee is unavailable.  The proof's statement
that every false row is handled by the same bounded routine therefore does
not follow.

A repair must add the public guard `L>=J` before every terminal call.  Rows
below that threshold can be retained only as word support, or combined by a
separately certified orientation mechanism.  This guard preserves every
single-large-prime conclusion because (16) already assumes it.

## 4. The harmonic-surplus lemma survives

For `S_p>R`, write

\[
L_p=\log_2S_p,\qquad
X_p=\log_2(S_p/r_p),\qquad
T_p=\log_2(S_p/R).
\]

Then `0<=X_p<=L_p` and

\[
r_p\le R\iff X_p\ge T_p.
\]

If `alpha=Pr(X_p>=T_p)`, boundedness gives

\[
\mathbb E X_p
\le T_p(1-\alpha)+L_p\alpha.
\]

Thus `E X_p>=T_p+delta` implies

\[
\alpha\ge {\delta\over L_p-T_p}
={\delta\over\log_2R}.
\]

Equivalently, `E log_2 r_p<=log_2R-delta`, and Markov's inequality on the
nonnegative variable `log_2 r_p` gives the same bound.  If `S_p<=R`, the
favorable event is deterministic.  No hidden independence assumption is
present.

On a no-direct-factor bank outcome, sample a fresh independent projected
unit.  If one residual is one, the imported P202 factor-or-growth bound is
at least `2/3`.  If both residuals are nontrivial odd integers, the direct
proper-factor probability is

\[
{1\over r_p}+{1\over r_q}-{2\over r_pr_q}
\ge {1\over\min(r_p,r_q)}.
\]

Hence `min(r_p,r_q)<=R` gives conditional progress at least `1/R`.
Direct child-factor outcomes have success one, so including them in the
planned-bank favorable event can only increase the lower bound.  Multiplying
the history-wise bounds proves

\[
\Pr(\text{factor or growth})
\ge {\delta(n)\over R\log_2R}.
\]

This is inverse numerical QP when `delta` is inverse QP and `R` is
numerical QP.  F234 still supplies no all-input lower bound on `delta`; the
packet correctly disclaims that missing source theorem.

## Final decision

The mathematical core is useful and exact: saturated rational-prime support
has the claimed expected logarithmic mass, and a surplus of that mass gives
the claimed Las Vegas probability.  The frozen packet nevertheless equates
that support with a narrower operational row event and sends subthreshold
rows to a terminal outside its QP promise.  The strict verdict is therefore
**FAIL pending repair and refreezing**.
