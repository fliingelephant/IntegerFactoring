# Proof of the F226 binary-child APR-source candidate

## 1. The top-bit child

For odd `N` of bit length `n`,

\[
2^{n-1}<N<2^n.
\]

The left inequality is strict because `N` is odd and hence is not the power
of two `2^(n-1)`.  Therefore `A=N-2^(n-1)` is positive.  Moreover

\[
A<N/2
\iff N<2^n,
\]

which holds.  Finally,

\[
\gcd(A,N)=\gcd(2^{n-1},N)=1.
\]

If `ell|A`, then `N=2^k mod ell`.  Let the order of `2` modulo `ell` be
`d`.  The order of its `k`th power is `d/gcd(d,k)`, proving (A4).

In the cyclic group `(Z/ell Z)^times`, let `H=<N>`.  Since `N=pq`,

\[
q=Np^{-1}.
\]

If `p in H`, then `q in H`; the converse is symmetric.  If
`p=N^i`, then `q=N^(1-i)`.  The exponent class is unique modulo
`h=ord_ell(N)`.  A system of residue classes `i_ell mod h_ell` has a common
solution exactly under the generalized-CRT conditions (A8).  None of these
conditions follows merely from knowing that `ell|A`.

## 2. Exact-uniform random prefixes

The odd residue classes modulo `2^m` form a group.  Since `N` is odd,
multiplication by `N` permutes this group.  Thus uniform odd `u` makes
`R_m=uN mod 2^m` exactly uniform over the odd canonical representatives.

The next binary prefix either retains the old value or adds the new bit:

\[
R_{j+1}=R_j
\quad\text{or}\quad
R_{j+1}=R_j+2^j.
\]

In the second case,

\[
\gcd(R_j,R_{j+1})=\gcd(R_j,2^j)=1
\]

because `R_j` is odd.  This proves (B3).  It does not extend to arbitrary
nonconsecutive prefixes: for example the prefixes `3` and `15` have gcd
three.  Auxiliary primes are therefore deduplicated before forming `S`.

Every `R_j` is below `2^j<=2^m`.  Every auxiliary prime `ell` is no larger
than its child, so `ell-1<2^m`.  There are at most `m` distinct children.
The sum of their bit lengths is at most `m^2`, and the number of prime
occurrences in their complete factorizations is also `O(m^2)` because each
occurrence contributes at least one bit to a child's logarithm.

After gcd screening, an auxiliary prime cannot divide `N`.  Factoring
`ell-1` and stripping exponents computes `ord_ell(N)` exactly.

Let

\[
K(x)\le 2^{C(\log(x+1))^a}
\]

bound the number of banks and let the polynomial child multiplicity be
absorbed into the same form.  At recursion depth `r`, all inputs have at
most `ceil(n/2^r)` bits.  The logarithm of the product of all branching
factors is at most

\[
O\!\left(
\sum_{r=0}^{\lceil\log_2n\rceil}
(\log(n/2^r+1))^a
\log n
\right)
=(\log n)^{O(1)}.
\]

Exponentiating proves (B5).  Arithmetic, random bits, gcds, factor
validation, order stripping, and stored output have numerical-QP total
size and cost.

In contrast, `c(n)` calls on `(n-1)`-bit integers give
`T(n)<=c(n)T(n-1)+...`.  Even polynomial `c(n)>1` multiplies across `Theta(n)`
levels and is not covered by the preceding half-size recurrence.  One
top-bit child has coefficient one and is safe; many such children are not
justified.

## 3. The conditional residue bridge

For every accepted auxiliary prime, Section 1 gives one exponent class.
Pairwise generalized-CRT compatibility is equivalent to a common exponent
class modulo

\[
H=\operatorname{lcm} h_\ell.
\]

When `H<=T(n)`, enumerate a complete residue system modulo `H`.  Modular
exponentiation gives each candidate `N^i mod S`.  The true residue of `p`
is among them.  Generalized CRT combines these residues with the certified
residue modulo `L_0`.  The known-residue arithmetic-progression factorer has
QP cost at threshold (C4).  Every candidate factor is gcd-screened and
verified, so this bridge is deterministic conditional on the certificate.

## 4. Affine inversion and scalar closure

For each unit `x mod S`, there is exactly one `y` with `xy=N`, namely
`y=Nx^-1`.  Conversely every ordered factorization has this form.  This
proves (D1).  Applying a multiplicative character gives

\[
\chi(y)=\chi(N)\chi(x)^{-1},
\]

which proves (D2).  Any product-only local scalar transcript is therefore
constant on the torsor parameter `x`.  Adaptive choices based only on such
products remain constant by induction on the transcript length.  This does
not discard the public integer children or claim that every possible
computation on them is scalar.

If `X` is uniform among the `phi(S)` units, exactly
`|{N^i:i in I}|` values satisfy the orbit condition.  This proves (D3).

For odd squarefree `S`,

\[
\frac{\varphi(S)^2}{S}
=\prod_{\ell\mid S}\frac{(\ell-1)^2}{\ell}.
\]

Every factor on the right is greater than one because `ell>=3`.  Hence
`phi(S)>sqrt(S)` unless `S=1`, proving (D4).  Combining (D3), a QP bound on
`|I|`, and (D5) gives

\[
\Pr\le
\frac{\operatorname{QP}(n)}{\sqrt{N^{1/4}/\operatorname{QP}(n)}}
=2^{-n/8+(\log n)^{O(1)}}
=2^{-\Omega(n)}.
\]

Finally, if one exponent `i` works modulo every prime in squarefree `S`,
then `p=N^i mod ell` for every `ell|S`.  CRT gives
`p=N^i mod S`, equivalently `S|(N^i-p)`.  This is (D7).

## 5. Ensemble, support, and capped-divisor proofs

Before the finite checks, we prove the ensemble, support, and Las Vegas
claims added after the first source audit.

### 5.1. Multiplier ensemble and prime incidence

Multiplication by odd `N` permutes the odd residues modulo `B`.  Put
`v=uN mod B`.  Every shorter child is the canonical reduction
`R_j=v mod 2^j`.  This proves the vector identity (E0).  Projecting to one
coordinate shows that every odd residue modulo `2^j` occurs exactly
`2^(m-j)` times as `R_j(u)`.  Multiplication of these canonical
representatives proves (E1)--(E3).

An odd multiple of an odd prime `ell` is `ell` times an odd integer.  The
number of such multiples below `B` is

\[
\left\lceil{1\over2}\left\lfloor{B-1\over\ell}\right\rfloor\right\rceil.
\]

Dividing by `B/2` proves (E4), including its upper bound.

For a prefix of length `j`, the same calculation gives probability at most

\[
{1\over\ell}+2^{1-j}.
\]

There is no possible incidence until `2^j>ell`.  Summing over the remaining
prefix lengths and using

\[
\sum_{j\ge\lceil\log_2(\ell+1)\rceil}2^{1-j}< {4\over\ell}
\]

proves (E5).  A union bound over independent banks proves (E6).  No
independence between the prefixes of one bank is asserted or needed.

### 5.2. Hidden accepted support and its potential

The group `(Z/ell Z)^times` is cyclic.  Its unique subgroup of order
`h_ell` is both `<N>` and the set of roots of `X^(h_ell)-1`.  Hence

\[
p\in\langle N\rangle
\iff p^{h_\ell}=1.
\]

Since `q=Np^-1` and `N^(h_ell)=1`, this is also equivalent to
`q^(h_ell)=1`.  This proves (F1) and (F2).

If `ell` belongs to `mathcal G_i`, then `ell|(N^i-p)`.  This integer is
nonzero: `p>1` for `i=0`, `N>p` for `i=1`, and `N^i>p` for `i>1`.  The
squarefree product of the primes in `mathcal G_i` divides its absolute
value.  For `i=0` this value is below `N`; for `i>=1` it is below `N^i`.
This proves (F5).

A fixed prime is captured by at least one of `s` independent full children
with probability `1-(1-pi_ell)^s`.  Summing the weighted indicator
expectations proves (F6); no independence between different prime
indicators is used.  Finally `0<=X_i<=L_i`.  If
`P=Pr(X_i>=theta)`, then

\[
\mathbb E X_i\le\theta(1-P)+L_iP.
\]

Rearrangement proves (F7).

### 5.3. Capped subset enumeration

After the full children are factored, `W` and all of its prime factors are
public.  When `2^omega(W)<=D`, every squarefree divisor is explicitly
enumerated.  If (G2) holds, `C_i` appears in that list and satisfies the
true congruence `p=N^i mod C_i`.  Generalized CRT with `L_0`, followed by
the verified known-residue terminal, therefore returns a proper factor.
Every output is gcd-checked, so wrong exponents and wrong divisors only
cost time; they cannot create an incorrect output.

For every positive integer `r`,

\[
2^{\omega(r)}
=\sum_{\substack{d\mid r\\d\text{ squarefree}}}1.
\]

Average this identity over the `B/2` odd integers below `B`.  For each odd
squarefree `d<B`, the number of odd multiples is at most `B/(2d)+1`.
The harmonic-sum bound and the fact that there are at most `B/2` odd `d`
give

\[
\mathbb E2^{\omega(R_m)}
\le\sum_{d<B}{1\over d}+1
\le2+\log B.
\]

For a block, every prime of `W` occurs in at least one child, so

\[
2^{\omega(W)}\le\prod_{r=1}^s2^{\omega(R_m^{(r)})}.
\]

Independence, followed by Markov's inequality, proves (G4).  The event in
(F7) forces (G2), while the cap-failure event has probability at most
(G4).  Subtracting the latter probability proves (G5).

If `s` is polylogarithmic, `(2+log B)^s` is numerical QP.  The cap makes
the divisor list QP, and multiplication by the QP exponent bank and terminal
cost remains QP.  QP many blocks contribute only QP many children of at most
half the parent bit length, exactly as in Section 2.  This proves the
claimed recursion accounting, conditional on recursive correctness for
arbitrary children.

For `i=0`, `D_i=1-p`, giving (G6)'s first divisibility.  For `i=1`, an
auxiliary prime in `mathcal G_1` divides

\[
N-p=p(q-1).
\]

It is coprime to `p`, so it divides `q-1`.  This proves the second.

For the favorable-state corollary, the number of odd multiples of an odd
`d` below `B` is

\[
\left\lceil{1\over2}
 \left\lfloor{B-1\over d}\right\rfloor
\right\rceil.
\]

If `B>=4d`, division by `B/2` shows that this is a probability of at least
`1/(2d)`.  On that event `d` is among the divisors enumerated by Theorem G,
and exponent zero or one supplies the true residue by (G6).  Equation (G4)
with the cap (G8) bounds the discarded part by `1/(4Q(n))`.  Since
`1/(2d)>=1/(2Q(n))`, subtraction proves the success probability
`1/(4Q(n))`.

### 5.4. Enumeration dominance and the rough model

For a prime `ell>Y` in `mathcal G_i`, (E6) bounds its capture probability
by `K(m+4)/ell`, hence by `K(m+4)/Y`.  Weighted linearity of expectation
and (F5) give

\[
\mathbb E Z_i(Y)
\le {K(m+4)L_i\over Y}.
\]

Summing the crude bound `L_i<=nT` over fewer than `T` exponent classes
proves (H1).  If some `Z_i` is at least `Delta`, their nonnegative sum is
at least `Delta`; Markov's inequality proves (H2).  Enlarging `Y` by any
fixed numerical-QP factor preserves numerical-QP enumeration cost and
makes the right side smaller by that factor.  A sieve lists every prime up
to `Y` in QP bit complexity.  This proves the stated prime-support-only
dominance, not a simulation of all integer data attached to a child.

If `ord_ell(N)=h<=T`, then `ell|(N^h-1)`.  Therefore all primes counted in
(H3) divide

\[
\prod_{h=1}^T(N^h-1),
\]

whose binary logarithm is less than

\[
n\sum_{h=1}^Th={nT(T+1)\over2}.
\]

Every counted prime contributes at least `log_2 X`, proving (H3).  Apply
(E6), then a union bound.  At `X=N^(1/4)/QP`, all remaining factors are
QP and the `1/X` term is `2^(-n/4+polylog(n))`, proving the exponential
claim.

In the named model (H4), the odd prime divisors of `p-1` and `q-1` are
exactly `P` and `Q`.  Equations (E6) and (G6) bound the chance of capturing
either by

\[
K(m+4)(P^{-1}+Q^{-1}).
\]

When `P,Q` have order `sqrt(N)`, this is (H5).  The calculation is exact
conditional on such an input; no infinitude assertion is used.

### 5.5. Rejection does not supply a scalar carry bit

Let `H=<N mod ell>`.  If `p` is outside `H`, then `q=Np^-1` is outside it
as well.  A character of the quotient group that detects the coset of `p`
has

\[
\psi(N)=1,
\qquad
(\psi(p),\psi(q))=(z,z^{-1}),
\qquad z\ne1.
\]

Thus the scalar product remains one on simultaneous rejection.  The public
integer identity `uN=bB+R_m` also remains fixed across this affine local
torsor.  Neither statement produces an oriented dyadic factor bit.  A
coherent ring element that vanished in exactly one rational CRT component
would instead be a rational factor transition by coefficient gcds, as in
P215.  Standard APR/CL failure supplies only compositeness, not such an
element.  This proves the claimed rejection boundary in the named scalar
model without ruling out a future non-scalar or Archimedean use of the
child.

## 6. Exact witness checks

The identity `333859=563*593` is direct.  Its bit length is 19 and `m=9`.
The distinct values of `N mod2^j` for `2<=j<=9` are `3` and `35`.

- Modulo 3, `N=1`, so `<N>={1}`, while `563=2`.
- Modulo 5, `N=4`, so `<N>={1,4}`, while `563=3`.
- Modulo 7, `N=1`, so `<N>={1}`, while `563=3`.

Thus every auxiliary prime in the deterministic bank rejects.  The larger
finite counts are reproduced by the frozen Sage sources and exact JSON
outputs in this packet.  They are not used in any unbounded proof.
