# F245 V2 hostile re-audit

## Authentication

I authenticated every frozen input before reading it.  The five V2 values
were:

- `V2_STATEMENT.md`:
  `ad4ff2a363de6e30c12245a7ecaefa7990dc560893e3ddebb68bfb14d8338440`
- `V2_PROOF.md`:
  `a3da0fcb8a97425f289846e1f824e40f7e227395c230664c95f79c42ed40a92c`
- `V2_SELF_AUDIT.md`:
  `a467c9ac9de50511efc0a638bca79e5b3f8eb5474f7c236258585a9863993ce3`
- `V2_PROVENANCE.md`:
  `a67635a0575becf346cb037355b09350b8675ce4df88213dbb24482646d0e2ce`
- `V2_MANIFEST.md`:
  `66e8b484a93ae425994dba4e968c5ba4de29b84506388ac44ddd2286b305bf35`

After authenticating and reading `V2_MANIFEST.md`, I authenticated its seven
preserved V1 inputs:

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
- `HOSTILE_AUDIT.md`:
  `4a628b36faa03ea665a4e6e95ce12379eab8a8e0f4ab7249b3ff9b35329ec561`
- `BLIND_RECONSTRUCTION.md`:
  `c59bce6b5c92d139d65015eedd99e524f1c6e300d5dce5ac090efc9d3ea4b2c4`

I then read the root `PROMPT.md` and `AGENTS.md`, the complete V2 packet,
and the preserved V1 audits.  I used no numerical experiment.

## Verdict

**PASS, for the exact restricted grammar in `V2_STATEMENT.md`.**

The sequential CRT--Linnik construction is consistent and gives the claimed
absolute marker/input-length constant.  The primitive marker argument, the
history-wise inverse-quotient bounds, both torus probability upper bounds,
the common-order bound, the Markov truncation, and the carry identities all
survive hostile reconstruction.

This is not a factoring algorithm and not a general factoring lower bound.
In particular, the PASS does not extend the result to a powered exponent
chosen from its current torus point, biased inverse seeds, nonlinear carries,
or a decoder outside the stated product-word grammar.

## 1. Sequential CRT--Linnik family

Take four distinct odd marker primes in fixed comparable intervals above a
parameter `X`.  The first CRT modulus is

\[
 M_1=24\lambda_+\lambda_-\rho_+\rho_-=O(X^4).
\]

The residue for `p` is reduced modulo every factor of `M_1`: `13` is a unit
modulo `24`, the two lambda residues are signs, and the two rho residues are
primitive roots.  Linnik therefore gives a prime

\[
 X<p\le M_1^{O(1)}=X^{O(1)}.
\]

The congruence `p = 13 (mod 24)` gives

\[
 v_2(p^2-1)=3,
 \qquad e=v_3(p^2-1)\ge1.
\]

Because `p` is primitive modulo each rho marker and the markers are larger
than `3`, neither rho marker divides `p^2-1`.  Thus all moduli in the second
CRT are coprime.  At every prime `s>=5` in the support of `p^2-1`, a unit
which is not either sign exists.  At a lambda marker, a lift whose reduction
is primitive is such a unit.  Hence the second CRT residue is reduced.

If

\[
 P=\prod_{s\ge5}s^{e_s},
\]

then its modulus satisfies

\[
 M_2=8\,3^{\max(e,2)}P\rho_+\rho_-
 \le 3(p^2-1)\rho_+\rho_-
 =O(p^2X^2).
\]

The second Linnik application gives a prime `q=X^{O(1)}`.  Also `q>X`
because `q=1 (mod rho_+)`.  The primes are distinct because
`p=5 (mod 8)` and `q=3 (mod 8)`.

The local congruences give exactly

\[
 \gcd(p^2-1,q^2-1)=24.
\]

Indeed, both square-minus-one values have 2-adic valuation `3`; the
3-adic valuation on the `q` side is exactly `1`; and every prime at least
`5` in the support on the `p` side was excluded from the `q` side.  The
four shifted gcds are consequently

\[
 2,12,2,2
\]

in the displayed order of V2 equation (7).

Finally `p,q>X` while `p,q=X^{O(1)}`.  Therefore

\[
 n=\Theta(\log X).
\]

After decreasing one absolute constant if necessary, every marker greater
than `X` is greater than `2^{cn}`.  Taking `X` unbounded gives infinitely
many distinct semiprimes.  No simultaneous or circular use of Linnik is
hidden here: the second reduced class is chosen only after `p` and the full
support of `p^2-1` are fixed.

## 2. Primitive marker support

Modulo `lambda_a`, one has `N=aq`; modulo `rho_b`, one has `N=bp`.
If a marker `ell` divides one factor `|N^k-sigma|`, squaring gives

\[
 q^{2k}=1\pmod\ell
 \quad\hbox{or}\quad
 p^{2k}=1\pmod\ell.
\]

The relevant cross residue is primitive, so `ell-1` divides `2k` and
`k>=(ell-1)/2`.  For positive `k` and either sign,

\[
 \operatorname{bitlen}(|N^k-\sigma|)=\Omega(kn)=\Omega(n\ell).
\]

This is `2^{Omega(n)}` when `ell>2^{cn}` and exceeds every fixed numerical
quasipolynomial.  A positive product cannot cancel this size.  Positive
outer exponents introduce no new prime support.  Thus every allowed
numerical-QP-bit signed-power word misses every marker.

The same argument covers `(N^2-1)^n`.  Separately,

\[
 \gcd(N-ab,p-a)=\gcd(q-b,p-a)
\]

and its `q`-side analogue.  Equation (7), or directly the primitive
cross residue, shows that neither relevant marker divides the base exponent
`N-ab`.

## 3. Exact inverse quotients

For `0<=k<N`, the fibre identity is exact:

\[
 K^{-1}(k)=\{u:k<u<N,\ u\mid Nk+1\}.
\]

For the converse direction, `v=(Nk+1)/u` is positive and less than `N`
exactly because `u>k`; also any common divisor of `u` and `N` would divide
both `Nk` and `Nk+1`.  Thus `u` is a unit and `v` is its canonical inverse.
Every fibre is therefore bounded by `Delta_N`.

The only zero quotient is `u=v=1`.  Replacing zero by one merges at most
the zero and one atoms, so the factor `2` in the atom bound is safe.  One
residue class modulo `ell` meets the support in at most `ceil(N/ell)`
integers.  Since

\[
 {N\over\varphi(N)}\le {15\over8},
 \qquad
 \lceil N/\ell\rceil<2N/\ell,
\]

the strict constant `8` in equation (1) is valid.

For two fresh values, if `rho_r` is the residue mass of the unmodified
quotient, then

\[
 \Pr(K_i=K_j\pmod\ell)=\sum_r\rho_r^2
 \le\max_r\rho_r\le\beta_{N,\ell}.
\]

Replacing an exact zero difference by `1` removes an odd-marker incidence.
This proves equation (2).

## 4. History-wise and adaptive law

Exact conditional uniformity is sufficient and necessary for the stated
argument.  For a possible pair `i<j`, condition just before drawing seed
`j`.  The earlier quotient is fixed and the new quotient retains its fixed
residue-mass bound.  Multiplying by the indicator that seed `j` is actually
requested also covers a stopping time.

After all requested seeds are drawn, marker divisibility of any selected
positive product is contained pathwise in the union of the incidences of
the complete bank.  Post-transcript selection and positive powers cannot
enlarge that union.  There are at most

\[
 Q+{Q\choose2}
\]

bank entries, so equation (3) follows without independence among the bank
events.  Uniform marginals without conditional uniformity would not prove
this result; V2 explicitly requires the stronger history-wise law.

The maximal-order divisor estimate gives

\[
 \Delta_N=2^{O(n/\log n)}=2^{o(n)}.
\]

Since a fixed numerical-QP count and its square are also `2^{o(n)}`, the
complete bank hits any one marker with probability `2^{-Omega(n)}`.  A
union bound over four markers proves equation (12).

## 5. Clean and nonclean torus bounds

For a uniform clean Hilbert--90 sample, the local map

\[
 z\longmapsto z/\bar z
\]

has equal-size fibres onto the local norm-one torus.  CRT makes the two
local points independent.  This reconstructs the stated independent
uniform law in the cyclic groups of orders `m_p=p-a` and `m_q=q-b`.

For a fixed public exponent `E`, the kernel of the `E`-power map on a
cyclic group of order `m` has size `gcd(E,m)`.  Hence the return probability
is exactly `gcd(E,m)/m`.  The joint-coordinate identity screen can split
only when exactly one local point returns.  The associated two-primary
chain is entered only on a global return, so every clean factor event is
contained in the union of the two local return events.  The clean success
probability is therefore at most their sum.

The nonclean estimate does not assume a split type.  For one local prime
`r`, a split norm-zero locus is the union of two lines and contains
`2r-1` coefficient pairs; a nonsplit norm vanishes only at the zero pair.
Thus a uniform raw coefficient pair has local norm-zero probability less
than `2/r`.  A union bound over `p` and `q` proves the stated

\[
 {2\over p}+{2\over q}
\]

upper bound per pair.  The coefficient-zero screen is smaller still,
at most `1/p^2+1/q^2`.  These are raw-pair bounds, so repeated rejection
does not create a conditioning error when incidences are union-bounded over
the actual raw draws.

On the event that the word misses all markers, the full public exponent in
orientation `(a,b)` is not divisible by `lambda_a` or `rho_b`.  Therefore

\[
 {\gcd(E,m_p)\over m_p}\le {1\over\lambda_a},
 \qquad
 {\gcd(E,m_q)\over m_q}\le {1\over\rho_b}.
\]

Both the clean bound and the nonclean bound are `2^{-Omega(n)}` because
the marker incidences force `p,q>2^{cn}-1`.  A numerical-QP number of clean
trials and raw coefficient pairs preserves an exponential upper bound.

The word/exponent must be public before the fresh uniform torus point for
this kernel count.  This is the reading stated in V2.  Selecting an exponent
from the current point would be a feedback law and is outside the theorem.

## 6. Accumulated common orders

An exact order common to both local groups in orientation `(a,b)` divides

\[
 \gcd(p-a,q-b).
\]

The four possible gcds are `2,12,2,2`.  Hence the lcm of any number of such
common orders, even across all four hidden orientations, divides `12`.
It cannot absorb an odd exponential marker.  This claim is only about
orders certified as common; it does not assert a bound on arbitrary local
orders or arbitrary integer functions of an order transcript.

## 7. Markov truncation

Suppose a Las Vegas algorithm confined to this grammar had expected time at
most a fixed numerical-QP function `Q(n)`.  Markov gives

\[
 \Pr(T\le2Q(n))\ge {1\over2}.
\]

Abort the run after `2Q(n)` bit operations.  This pathwise cutoff permits
only a numerical-QP number of seeds, raw sampler draws, powered trials, and
explicitly processed word bits.  Enlarge `Q` by a fixed factor to cover
this transcript.  The complete inverse bank misses all markers except with
probability `2^{-Omega(n)}`; every allowed signed word misses them
deterministically for sufficiently large family members; all clean and
nonclean factor exits in the grammar have total probability
`2^{-Omega(n)}`; and the common-order lcm still divides `12`.

Thus the verified-factor probability before the cutoff is exponentially
small, contradicting the Markov lower bound of one half.  The cutoff also
handles unbounded rejection tails: it counts raw draws, not only accepted
trials.  The constants and exponent in `Q` must be fixed independently of
`N`; V2 has this quantifier order.

## 8. Carry identities

The definitions give

\[
 X=Av-Nq_A,\qquad Y=Bv-Nq_B,\qquad gv-1=N\widetilde d.
\]

Substitution proves

\[
 {gX-A\over N}=A\widetilde d-gq_A,
 \qquad
 {gY-B\over N}=B\widetilde d-gq_B.
\]

Also

\[
 A^2-DB^2=(a^2-Db^2)^2=g^2.
\]

Using `gX=A+Nk` and `gY=B+Nl`, expansion and division by `Ng^2` give
equation (16).  Division is valid because `g` is nonzero, and the norm
carry is integral because

\[
 X^2-DY^2\equiv v^2g^2\equiv1\pmod N.
\]

For a signed or noncanonical `g=r+tN`, with `r` its canonical unit residue,

\[
 \widetilde d=K(r)+tv.
\]

This confirms rather than removes the distributional obstruction: the
right-hand sides contain biased sums and products and do not inherit the
fresh canonical inverse-quotient law.

## 9. Scope and edge cases

- All marker primes are odd, distinct, less than `N`, and eventually larger
  than `3`; the residue and primitive-order arguments use only this range.
- `p` and `q` are distinct odd primes.  Prime powers, equal-prime products,
  even inputs, and general composites are not claimed.
- Empty selections have product `1`; exact quotient equality produces the
  factor `1`; all admitted word exponents are positive.  No zero-product
  exception remains.
- The theorem requires actual numerical-QP binary length for signed-power
  words.  It does not grant a succinct uncharged representation of a much
  larger exponent.
- Fresh means exact uniformity after the complete past.  Biased rejection,
  retained-current-sample feedback, cross-coordinate determinants, and
  nonlinear norm carries remain outside the probability grammar.
- The common-order conclusion applies only to exact orders present on both
  hidden sides.  It does not constrain an unrestricted transcript decoder.

These restrictions match the status and exact remaining-gap paragraphs.
No conclusion is transferred to the nonlinear carry identities.
