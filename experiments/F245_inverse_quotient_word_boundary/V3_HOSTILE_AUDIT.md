# F245 V3 hostile audit

## Authentication and verdict

I computed the hashes before reading any packet file.  Every assigned V3
hash matched:

| File | SHA-256 |
|---|---|
| `V3_STATEMENT.md` | `2120f53ec1762cd6b90236eb165d59368f9e0aad4750dcb3a5afadf3508d2c8b` |
| `V3_PROOF.md` | `52e7b9391d8d4f36d4653b016f58805776655f732d3a398f9e753c9f14205e7d` |
| `V3_SELF_AUDIT.md` | `ca19b956247c986fe30f69633b71f37b90894133c1fd83bf617dfa89d9376f3f` |
| `V3_PROVENANCE.md` | `b15f8b84842dbf5c663162b1e7793ff29ae9a5e138071665e8f98fd06d865981` |
| `V3_MANIFEST.md` | `6b35eab4e6c56db6f71b36e3423d376f6b04f17fadc91ff30cbe00873b22d8ed` |

I also authenticated the preserved packet before reading the V2 blind
report.  In particular, `V2_BLIND_RECONSTRUCTION.md` had SHA-256
`74a29858458cb25354baf945795a6907c92fa86fa61239ed46a367ffc39ddb65`,
and its strict verdict was **FAIL** because V2 did not define the machine
grammar or exhaust its torus factor exits.

**V3 verdict: PASS, for exactly the restricted grammar in
`V3_STATEMENT.md`.**

V3 repairs the V2 self-containment failure.  The statement itself now
defines the filtration, all fresh conditional laws, the chronology of the
exponent and torus point, every legal integer source, every gcd screen, and
the exhaustive output rule.  I found no missing factor exit in equation
(38), no algebraic error, and no optional-stopping or Markov quantifier
error.

This PASS is not an all-input factoring algorithm or a general factoring
lower bound.  It does not cover current-point feedback, biased sources,
canonical high digits, nonlinear carry words, or an unrestricted relation
decoder.

## 1. The V2 exhaustiveness defect is closed

The factor-return paths can be reconstructed from the V3 statement alone:

1. a proper gcd from a raw unit draw;
2. a proper gcd from a legal bank entry, signed-power product, full word,
   common-order lcm, or final exponent;
3. a proper gcd from a raw discriminant draw;
4. a proper coefficient gcd `gcd(N,A,B)`;
5. a proper norm gcd `gcd(N,A^2-DB^2)`;
6. a proper endpoint screen `G_+(U^E)`;
7. a proper `G_+` or `G_-` screen in the two-primary chain.

The statement says that rejection and null branches do not return factors,
that a common-order token has no separate exit, and that no other gcd
argument or decoder is legal.  Hence this list is pathwise exhaustive, not
an interpretation imported from P208 or P209.

The chronology is also explicit.  The complete past is in the filtration;
`D` can be retained; the integer `E=(N-J)W` is fixed from that past before
the fresh coefficient pair; and the only later information released from
the current point is through the listed screens and a valid common-order
token.  Thus no clean-trial bound silently conditions on an exponent chosen
from the point it powers.

## 2. Inverse-quotient fibres and adaptive bank

For `0<=k<N`, the exact fibre is

\[
 K^{-1}(k)=\{u:k<u<N,\ u\mid Nk+1\}.
\]

If `K(u)=k`, then `uv=Nk+1`; the condition `v<N` gives `u>k`.  Conversely,
such a divisor gives `v=(Nk+1)/u<N`.  Any common divisor of `u` and `N`
would divide both `Nk` and `Nk+1`, so `u` is a unit and `v` is its canonical
inverse.  Since `Nk+1<N^2`, each fibre has at most `Delta_N` elements.

Replacing the sole zero quotient by `1` merges at most two atoms.  One
residue class modulo `ell` meets the support in at most `ceil(N/ell)`
integers.  For distinct odd primes,

\[
 {N\over\varphi(N)}\le {15\over8},
 \qquad
 \left\lceil{N\over\ell}\right\rceil<{2N\over\ell},
\]

so the stated bound

\[
 \beta_{N,\ell}
 ={2\lceil N/\ell\rceil\Delta_N\over\varphi(N)}
 <{8\Delta_N\over\ell}
\]

is valid.

For a pair `i<j`, condition immediately before the fresh accepted seed `j`.
The older `K_i` is fixed, while `K_j` keeps the same residue-mass bound.
The event `ell | Gamma_ij` is an unequal residue collision; replacing exact
equality by `1` removes that incidence.  Multiplying by the indicator that
seed `j` is actually requested handles an adaptive stopping rule.  With at
most `B` accepted seeds, a union bound over the `B+binom(B,2)` available
entries proves (22).  Later selection, repetition, and positive powers
cannot add prime support.

The raw sampler also has the stated conditional law.  Before screening,
every residue has mass `1/N`; after conditioning on gcd one, all canonical
units have equal mass.  A proper raw unit gcd occurs with probability

\[
 {p+q-2\over N}<{1\over p}+{1\over q},
\]

and the identical count applies to a raw discriminant.  Rejected raw draws
remain charged and do not alter these per-draw bounds.

## 3. Sequential marker family and deterministic exclusions

The first CRT modulus

\[
 24\lambda_+\lambda_-\rho_+\rho_-
\]

has a reduced residue class: the lambda residues are signs, the rho
residues are primitive, and `13` is a unit modulo `24`.  Linnik gives a
prime `p=X^{O(1)}` in this class.  Since `p` is primitive at both
rho-markers and those primes exceed `3`, neither rho-marker divides
`p^2-1`.

After factoring

\[
 p^2-1=2^3 3^e\prod_{s\ge5}s^{e_s},
\]

the second CRT system is pairwise coprime.  At every `s>=5`, a unit residue
different from both signs exists; at a lambda-marker it can be chosen
primitive.  The second modulus is

\[
 8\,3^{\max(e,2)}
 \left(\prod_{s\ge5}s^{e_s}\right)\rho_+\rho_-
 =O(p^2X^2),
\]

so a second Linnik application gives `q=X^{O(1)}`.  The congruences
`p=5 (mod 8)` and `q=3 (mod 8)` make the primes distinct.

The exact local valuations are

\[
 v_2(p-1),v_2(p+1),v_2(q-1),v_2(q+1)=2,1,1,2.
\]

The only 3-adic overlap is between `p-1` and `q+1`, with value `3`, and the
second CRT class excludes every prime at least `5` from both signs on the
`q` side.  Therefore the four shifted gcds are exactly

\[
 2,12,2,2,
\]

and `gcd(p^2-1,q^2-1)=24`.

Both hidden primes exceed the marker scale and are polynomial in it.  Thus
`n=Theta(log X)`, so one absolute `c_0>0` makes all four markers larger than
`2^{c_0n}` along an infinite subfamily.

At `lambda_a`, one has `N=aq`; at `rho_b`, one has `N=bp`.  If a marker
divides `N^k-sigma`, the primitive cross residue gives

\[
 \ell-1\mid2k,
 \qquad k\ge {\ell-1\over2}.
\]

That single explicit factor has `2^{Omega(n)}` bits.  A numerical-QP-bit
positive product cannot contain it.  The same calculation excludes every
marker from `N^2-1`.

Moreover,

\[
 \gcd(N-ab,p-a)=\gcd(q-b,p-a),
\]

and symmetrically on the `q` side.  The shifted-gcd table excludes the two
orientation markers from `N-ab`.  Finally, every valid common-order token
in orientation `(a,b)` divides `gcd(p-a,q-b)`.  Even after mixing all four
orientations,

\[
 M\mid\operatorname{lcm}(2,12,2,2)=12.
\]

The constructed hidden primes exceed `3`, so this token lcm is also
coprime to `N`.

## 4. Clean Hilbert--90 law and nonclean screens

For a hidden prime `r` and `epsilon=(D/r)`, the local quadratic algebra is
split when `epsilon=+1` and is `F_{r^2}` when `epsilon=-1`.  In both cases

\[
 z\longmapsto z/\bar z
\]

has constant fibres onto a cyclic norm-one group of order `r-epsilon`.
The norm screen certifies exactly that the denominator is a unit.  CRT and
the factorized unit condition leave the two local algebra units independent
and uniform, so the accepted torus reductions are independent uniform
elements of the two full local groups.  This includes both signed
identities.

The earlier coefficient screen does not bias this law: norm-unit status
already excludes `(A,B)=(0,0)` at either hidden prime, so every clean pair
necessarily has coefficient gcd one.

For the raw nonclean bound, a fixed unit `D` has `2r-1` norm-zero pairs
modulo `r` in the split case and one in the nonsplit case.  Therefore

\[
 \Pr(r\mid A^2-DB^2)<{2\over r}.
\]

A proper coefficient gcd is contained in the same local norm-zero event.
One raw coefficient pair can therefore return a factor through either
nonclean screen with probability less than

\[
 {2\over p}+{2\over q}.
\]

This is an unconditional raw-pair bound, so an arbitrary rejection tail is
handled by counting the actual raw draws before the cutoff.

## 5. Endpoint and exact two-primary chain

For a fresh uniform element of a cyclic group of order `m`, the exact
return probability under the fixed exponent `E` is `gcd(E,m)/m`.  The
endpoint `G_+` screen is proper only if exactly one local component returns.
The chain is entered only after both local components return under `E`.
Consequently every clean factor exit, including every minus screen, implies
at least one of the two local endpoint-return events.

The stronger chain formula also reconstructs.  Conditional on global
return, the local points are independent and uniform in their respective
`E`-power kernels.  After the odd part `e_0` is applied, the two-primary
coordinate is uniform in `C_{2^{h_i}}`, where

\[
 h_i=\min(v_2(m_i),v_2(E)).
\]

For its exact-order exponent `S`,

\[
 \Pr(S=0)=2^{-h_i},
 \qquad
 \Pr(S=j)=2^{j-1-h_i}\quad(1\le j\le h_i).
\]

The signed-identity chain separates the hidden primes exactly when the two
exact-order exponents differ.  If `a_2<=b_2`, their equality probability is

\[
 {1+\sum_{j=1}^{a_2}4^{j-1}\over2^{a_2+b_2}}
 ={4^{a_2}+2\over3\,2^{a_2+b_2}}.
\]

Both local group orders and `E` are even, so `a_2>=1`; hence the success
probability in (36) is at least `1/2`.  The obstruction proof uses only the
weaker local-return containment, not this lower bound on conditional chain
success.

On a history whose current bank misses the markers, every factor of `E`
other than `W_iq` is deterministically marker-free by the preceding
section.  Thus, for the actual orientation `(a,b)`,

\[
 {\gcd(E,p-a)\over p-a}\le {1\over\lambda_a},
 \qquad
 {\gcd(E,q-b)\over q-b}\le {1\over\rho_b}.
\]

The conditional factor probability of one clean trial is therefore at
most `2/L`.

## 6. Equation (38) is exhaustive

Let

\[
 \mathcal S=\{p,q,\lambda_+,\lambda_-,\rho_+,\rho_-\}.
\]

Every member of this set is below `N` and at least `L`: the four markers
are so by definition, while `lambda_+ | p-1` and `rho_+ | q-1` give
`p,q>L`.  Applying the adaptive bank bound to all six primes gives

\[
 \Pr(\text{some bank entry meets }\mathcal S)
 \le 6\cdot8H_B{\Delta_N\over L}
 =48H_B{\Delta_N\over L}.
\]

This same event covers every direct word gcd.  Modulo either hidden prime,
each signed-power factor is a sign and `N^2-1` is `-1`; `M|12` is a unit;
and `N-J` is a unit.  Hence a legal product or final exponent can share a
hidden prime with `N` only through an inverse-bank entry.

There are at most `B` raw unit draws and `B` raw discriminant draws, which
together contribute at most

\[
 2B\left({1\over p}+{1\over q}\right).
\]

There are at most `B` raw coefficient pairs, contributing at most the same
quantity.  This gives the second term of (38).  Before a bank incidence,
each of at most `B` clean trials has history-wise conditional factor
probability at most `2/L`, which gives the last term.  This argument stops
at the first bank incidence; it never conditions a torus draw on a future
bank value.

These three events cover, respectively, direct word exits, every nonclean
exit, and every clean endpoint or chain exit.  They therefore prove the
pathwise cutoff bound

\[
 48H_B{\Delta_N\over L}
 +4B\left({1\over p}+{1\over q}\right)
 +{2B\over L}.
\]

An explicit signed-power word present before the cutoff has at most `B`
bits because reading and materializing all bits is charged.  Thus the
deterministic marker exclusion applies whenever `B` is numerical-QP.  No
succinct long exponent escapes this accounting.

## 7. Divisor growth and Markov quantifiers

The standard maximum-order estimate gives

\[
 \Delta_N
 =\exp\!\left(O\!\left({\log N\over\log\log N}\right)\right)
 =2^{o(n)}.
\]

For numerical-QP `B`, both `B` and `H_B` are `2^{o(n)}`, while `L` and the
hidden primes are `2^{Omega(n)}`.  Every term in (38) is therefore
`2^{-Omega(n)}`.

The quantifier order in the final contradiction is correct.  Fix one
confined machine and its alleged expected numerical-QP bound `Q`.  Markov
gives

\[
 \Pr(T\le2Q(n))\ge {1\over2}
\]

on every input where the expected bound holds.  Apply the stopped-run
theorem with the fixed cutoff `B=2Q(n)`, then take a sufficiently large
member of the already constructed infinite family.  Equation (38) makes
the same probability exponentially small.  Almost-sure Las Vegas halting
turns `T<=B` into return of a verified proper factor, so this is a genuine
contradiction.

## 8. Carry identities and exact scope

From

\[
 gv=1+N\widetilde d,
 \quad A_0v=X+Nq_A,
 \quad B_0v=Y+Nq_B,
\]

direct substitution gives

\[
 k=A_0\widetilde d-gq_A,
 \qquad
 l=B_0\widetilde d-gq_B.
\]

The identity `A_0^2-DB_0^2=g^2`, together with
`gX=A_0+Nk` and `gY=B_0+Nl`, yields

\[
 {X^2-DY^2-1\over N}
 ={2(A_0k-DB_0l)+N(k^2-Dl^2)\over g^2}.
\]

The derivation is valid for signed and noncanonical nonzero `g`.  It gives
no atom or collision law for the nonlinear expressions on the right.  V3
correctly leaves those expressions, canonical lift digits, point-dependent
words, biased sources, and full-transcript decoders outside the theorem.

No numerical experiment or external search was used in this audit.
