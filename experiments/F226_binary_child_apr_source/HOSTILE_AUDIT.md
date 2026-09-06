# F226 hostile audit

## Verdict

**PASS, at the exact conditional scope stated by the packet.** I found no
false uniformity law, prefix claim, incidence count, support identity,
probability inequality, cap argument, public-parameter quantifier, or
numerical-QP bit-cost conclusion.

This verdict has four strict scope guards.

1. The usual factoring domain `N >= 3` is required. The literal input `N=1`
   is odd but gives `A=0`, contrary to (A2). Every semiprime application in
   the packet already excludes this endpoint.
2. The random-bank recurrence is a cost and size theorem. It is conditional
   on a correct factoring dispatcher for every reachable half-size integer.
   A random child need not be balanced, semiprime, or odd after an
   `ell-1` call. The packet states this condition in Theorem G and again in
   the self-audit. It does not prove that dispatcher.
3. The one top-bit child is safe as one coefficient-one recursive call. The
   packet does not prove that recursively factoring all of its possible
   near-size `ell-1` descendants is QP. The positive recursively factorable
   bank is the half-bit bank of Theorem B.
4. The scalar-rejection obstruction concerns the named product-only affine
   torsor transcript. It is not a lower bound against a non-scalar APR/CL
   identity, an Archimedean computation, or a computation that already
   separates the rational CRT components.

Under these readings, the candidate proves a source construction and a
boundary. It does not prove an all-input factoring algorithm. I did not edit
a frozen input or a durable ledger. I wrote only this audit.

## Frozen-input integrity

I enumerated the directory names, hashed the five supplied frozen files, and
did not read their contents until every supplied hash matched.

| File | Expected and observed SHA-256 | Result |
|---|---|---|
| `STATEMENT.md` | `204b34f248610717000bc7d90dc80836125b78844fb23e6142412e0652ea6d40` | match |
| `PROOF.md` | `534f0a8fe8c0464678bb7e854ffd341a490e8a293b1559574eb2db374406c65f` | match |
| `SELF_AUDIT.md` | `798cad888cd3a4be8594acdc57023502be8382d9c55184f19a0e6f342fd8211e` | match |
| `PROVENANCE.md` | `1bab749b7f15894b1e04d5849314cf76fbd237e2cc51d76cce859f9cff18ed5a` | match |
| `RESULT.md` | `b6775817f0f6b79750fded1b716cb46e463c0349cd53943581895dfdb6ab38ca` | match |

The observed SHA-256 of `MANIFEST.md` is
`58365fb66feb86db00a948a0910db093faf79a67cf207874279091fbde24bed9`.
All path-addressable manifest entries match. The historical D01
pre-repair source digest has no separate pathname in the packet and cannot
be rehashed as a distinct artifact. Decompressing `D04_OUTPUT.json.gz`
gives the declared original-byte hash
`7e46cb0696fb6398e5120aa5b060bc4bf0c915d3898e0e4be9fbcf77ffd57a53`.

## 1. Top-bit child and local compatibility

For `N >= 3` odd with `n` bits,

\[
2^{n-1}<N<2^n.
\]

Thus `A=N-2^(n-1)` is positive and

\[
A<N/2 \iff N<2^n.
\]

Also

\[
\gcd(A,N)=\gcd(2^{n-1},N)=1.
\]

If `ell|A`, then `N=2^k mod ell`. The order formula

\[
\operatorname{ord}_\ell(N)
=\frac{\operatorname{ord}_\ell(2)}
       {\gcd(\operatorname{ord}_\ell(2),k)}
\]

is exact. Since `q=Np^-1`, membership of `p` in `<N>` is equivalent to
membership of `q`. The exponent of `p` is unique modulo `h_ell`, and the
pairwise conditions in (A8) are exactly the generalized-CRT conditions for
one exponent across all selected primes.

Nothing here forces local membership or cross-prime compatibility. The
packet does not claim otherwise. It also does not attach the half-size
recurrence of Theorem B to all order computations arising from `A`.

## 2. Exact-uniform bank and distinct prefixes

Put `B=2^m`. Multiplication by odd `N` is a permutation of the odd residue
classes modulo `B`. Therefore

\[
v=uN\bmod B
\]

is exactly uniform odd, and every shorter child is the deterministic prefix
`v mod 2^j`. This proves both the full-child uniformity and the vector
multiset identity (E0). It is stronger than a marginal heuristic.

Canonical binary reduction gives

\[
R_{j+1}=R_j\quad\hbox{or}\quad R_j+2^j.
\]

In the changed case,

\[
\gcd(R_j,R_j+2^j)=1
\]

because `R_j` is odd. Equal prefixes are evaluated once. Nonconsecutive
distinct prefixes can share primes. The packet explicitly gives `3,15` as
a counterexample and deduplicates shared auxiliary primes. No false
pairwise-coprimality assumption remains.

Gcd screening is in the correct place. Each child is screened before its
prime factors are treated as units modulo `N`. Since a child is smaller
than `N`, a nontrivial gcd is a proper verified factor.

## 3. Recursion and all bit costs

Every prefix child and every required `ell-1` has at most `m` bits. One bank
has at most `m-1` prefix positions. Its total child encoding is

\[
\sum_{j=2}^m O(j)=O(m^2)=O(n^2).
\]

The total number of prime occurrences is also `O(n^2)`, because each
occurrence consumes at least one bit of the logarithm of its child. Thus the
child calls and the `ell-1` calls fit in `K(n)O(n^2)` half-size calls per
node.

If

\[
K(x)\le 2^{C(\log(x+1))^a},
\]

then the logarithm of the product of branching factors over the
`O(log n)` halving levels is `(log n)^{O(1)}`. Hence the complete recursion
tree has numerical-QP size. Ceilings at the final levels only change a
constant-size base range.

The remaining local costs also fit this bound.

- Sampling an odd multiplier uses `m-1=O(n)` random bits.
- Multiplication, reduction, gcd, primality validation, order stripping,
  and modular exponentiation use operands of QP-bounded bit length.
- For a block of `s` full children,
  `log_2 W <= sm=O(n(log n)^a)`. Every enumerated divisor has polynomial
  bit length even when the number of divisors is numerical QP.
- The exponent cap is numeric: `0<=i<T`. Enumerating all `T` exponents is
  QP, and each exponent itself has only `log T=(log n)^{O(1)}` bits.
- QP many candidates times a QP known-residue terminal cost is still QP.
- A sieve through a numerical-QP cutoff `Y` has numerical-QP time, memory,
  and output size.
- The complete double-factorial ensemble is used only as an identity. The
  procedure never materializes it.

These facts prove recursion safety, not recursive correctness. Correctness
at arbitrary children is an explicit hypothesis. Treating Theorem B as an
unconditional arbitrary-integer factorer would be false, but the packet
does not make that promotion.

## 4. Ensemble products and fixed-prime incidence

The map `u -> v=uN mod B` proves that the complete vector multiset depends
only on the odd `v<B`. Therefore every statistic of the child integers is
independent of `N`. This includes the products (E1)--(E3) and prime
multiplicities. It does not include the multiplier labels or the quotients
`floor(uN/B)`. The exclusions in the statement are necessary and correct.

For a fixed odd prime `ell<B`, the odd multiples below `B` are `ell` times
the odd integers up to `floor((B-1)/ell)`. Their exact number is

\[
\left\lceil\frac12
\left\lfloor\frac{B-1}{\ell}\right\rfloor\right\rceil.
\]

Division by `B/2` proves (E4). At prefix length `j`, the same count is at
most `1/ell+2^(1-j)`. There is no incidence until `2^j>ell`. Summing only
those possible lengths gives

\[
\Pr(\ell\mid R_j\text{ for some }j)
\le \min(1,(m+4)/\ell).
\]

A union bound over `K` banks proves (E6). The proof uses no independence
between prefixes.

## 5. Accepted support and compatible-support algebra

For `h=ord_ell(N)`, the subgroup `<N>` is the unique order-`h` subgroup of
the cyclic group modulo `ell`. Hence

\[
p\in\langle N\rangle
\iff p^h=1
\iff q^h=1.
\]

The exact-order accepted primes are therefore the primes of order `h` that
divide

\[
\gcd(p^h-1,q^h-1).
\]

For one numeric exponent `i`, every prime in `G_i` divides the nonzero
integer `N^i-p`. Its squarefree product consequently has logarithm

\[
L_i<n\max(1,i).
\]

This is valid for `i=0` after taking the absolute value of `1-p`, and for
`i>=1` because `0<N^i-p<N^i`. It also explains why the cap must apply to
the numeric exponent value, not merely to its bit length.

The support sets and the integers `N^i-p` are analysis objects. The
procedure does not compute them and does not query `p` or `q`.

## 6. Harmonic expectation and tail direction

For `s` independent full children, a fixed support prime is captured with
probability `1-(1-pi_ell)^s`. Weighted linearity gives (F6) exactly. It does
not require independence between different prime-divisibility indicators.

The direction of (F7) is also correct. If
`P=Pr(X_i>=theta)` and `0<=X_i<=L_i`, then

\[
\mathbb E X_i
\le \theta(1-P)+L_iP.
\]

Thus `E X_i >= theta+delta` implies

\[
P\ge\frac{\delta}{L_i-\theta}.
\]

This is a lower bound from a bounded random variable, not a reversed
Markov inequality. The packet always requires `theta<L_i`. It never derives
the expectation surplus from uniformity alone. The missing all-input
harmonic-mass lower bound remains explicit.

## 7. Complete-divisor cap and success subtraction

For any positive integer `r`, `2^omega(r)` counts its squarefree divisors.
Averaging over the odd `r<B` gives

\[
\mathbb E 2^{\omega(R_m)}\le 2+\log B.
\]

For `s` independent children, the prime set of `W` is contained in the
union of their prime sets, so

\[
2^{\omega(W)}
\le\prod_{r=1}^s2^{\omega(R_m^{(r)})}.
\]

Independence followed by Markov proves (G4). With

\[
D=(2+\log B)^sP(n),
\]

the discard tail is at most `1/P(n)`. Since `s` is polylogarithmic, both
`D` and the complete divisor list are numerical QP.

On the event `X_i>=theta`, coprimality of `C_i` and `L_0` makes the terminal
modulus large enough. If the cap also holds, `C_i` is one of the enumerated
divisors. Therefore

\[
\Pr(\text{success})
\ge \Pr(X_i\ge\theta)-\Pr(\text{cap failure}),
\]

which is exactly (G5). No independence between progress and cap events is
assumed.

Gcd screening does not invalidate this unconditioned subtraction. If a
sampled child shares a factor with `N`, the algorithm has already
succeeded. On the remaining branch, all captured support primes are
exposed in `W`. One can bound the cap event using the original independent
unconditioned samples, which is at least as conservative.

Wrong divisors and wrong exponents only trigger verified terminal attempts.
They cannot produce a false factor.

## 8. Public `Q` quantifiers and the favorable state

Let the public numerical-QP function `Q(n)` be fixed before sampling. Let a
hidden odd squarefree `d<=Q(n)` satisfy the shifted-divisor and terminal-gap
conditions, with `4d<=B`. The number of odd multiples of `d` below `B`
gives

\[
\Pr(d\mid R_m)\ge\frac1{2d}\ge\frac1{2Q(n)}.
\]

For the public one-child cap

\[
D=4Q(n)(2+\log B),
\]

the discard probability is at most `1/(4Q(n))`. Subtraction, not an
independence claim, gives success at least `1/(4Q(n))`.

If `d|p-1`, exponent zero supplies `p=1 mod d`. If `d|q-1`, exponent one
supplies `p=N mod d`. The procedure can simply use the public constant cap
`T>=2`. The divisor `d` need not be public and need not be coprime to
`L_0`; complete enumeration tries it, and generalized CRT uses the lcm.
If `d` shares a factor with `N`, gcd screening succeeds earlier.

The quantifier order is therefore sound: the algorithm knows `Q`, not `d`.
The theorem remains conditional on the existence of such a `d` for the
given input.

## 9. Enumeration dominance and safe-prime-shift obstruction

For primes above `Y`, (E6) and the support-size bound give

\[
\mathbb E\sum_{i<T}Z_i(Y)
\le\frac{K(m+4)nT^2}{Y}.
\]

Markov applied to the nonnegative sum proves (H2). For QP `K,T`, an
inverse-QP target probability, and inverse-QP progress `Delta`, multiplying
`Y` by the required QP factors keeps `Y` numerical QP and makes this tail
smaller than the target. A deterministic QP sieve can list all smaller
prime values.

The packet does not overstate this conclusion. Listing those values does
not identify the compatible subset and does not reproduce the random
grouping used by Theorem G. It also does not simulate the quotient or a
future non-scalar use of a child.

Every prime of order at most `T` divides one of the integers `N^h-1` with
`h<=T`. The product of those integers has binary logarithm below

\[
\frac{nT(T+1)}2.
\]

This proves (H3). At the terminal-size cutoff, the candidate-prime count is
QP and each incidence probability is `2^(-Omega(n))`, so their union is
still exponentially small.

In the conditional safe-prime-shift model,

\[
p-1=2P,\qquad q-1=2Q,
\]

the only possible odd support primes for the guaranteed exponents zero and
one are `P` and `Q` (or a subset after the stated exclusions). Their sizes
are `Theta(sqrt(N))`, so (E6) gives

\[
2^{-n/2+(\log n)^{O(1)}}.
\]

This is an exact conditional obstruction for those two exponents. It is not
an infinitude claim and does not exclude useful support at larger exponents.

## 10. Scalar rejection and hidden-factor use

For squarefree odd `S` coprime to `N`, every ordered unit factorization is

\[
(x,Nx^{-1}).
\]

For a character `chi`, its values are `(z,chi(N)z^-1)`. The uniform torsor
model therefore gives the exact probability

\[
\frac{|\{N^i:i\in I\}|}{\varphi(S)}
\le\frac{|I|}{\varphi(S)}.
\]

Since `phi(S)>=sqrt(S)` for odd squarefree `S`, terminal-size `S` and QP
`I` give `2^(-Omega(n))`. This is a named formal model, not a distribution
theorem for the integer factors or the multiplier.

On local rejection, `p` and `q` lie in inverse nontrivial cosets of
`<N>`. A quotient character has values `(z,z^-1)` with product one. Thus a
product-only scalar transcript supplies no oriented carry bit. The public
identity `uN=bB+R_m` does not change this local torsor calculation. The
packet correctly leaves non-scalar and Archimedean transitions open.

The proofs use `p` and `q` only to state hidden support, prove conditional
success, or define the formal torsor. The executable Las Vegas procedure
enumerates public divisors and exponents and verifies every output. The
finite scans use the known `p` to grant ideal local labels, but they say so
explicitly.

## 11. Empirical evidence was not promoted

The D06 artifact reports exactly 7,212 tested rows, 6,415 ideal-oracle
terminal rows, 797 failures, and 54 zero-acceptance rows. Its smallest
zero-acceptance row is `333859=563*593`, with distinct children `3` and
`35`. The three local rejection checks in the proof are direct arithmetic.

The D08 artifact contains exactly the 54 D06 zero rows. Its minimum exact
fraction is `330/512`, and its displayed minimum, maximum, and mean agree
with `RESULT.md`. The D07 source explicitly uses the hidden `p` and exhausts
the finite odd-multiplier set. The D08 source changes only display-rate
postprocessing.

D04 is labeled recursion-unsafe. D05 is labeled invalid JSON. D06 and D08
are presented as finite discovery evidence. No unbounded theorem cites a
scan count as a premise, and no finite success rate is extrapolated to an
inverse-QP law.

## Conclusion

The exact source laws and the capped complete-divisor bridge survive this
audit. The packet also states the real gap correctly. It still needs either
an all-input inverse-QP harmonic-support theorem or a new verified
factor/carry transition on rejection, together with a correct arbitrary-
child factoring dispatcher. No empirical result supplies any of those
missing statements.
