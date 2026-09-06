# F168 hostile audit — PASS

## Frozen inputs and scope

I read the complete frozen statement and proof. Their SHA-256 hashes matched
the requested values before this audit:

- `STATEMENT.md`:
  `a30c71c6bf8d6b715b84e4abb78cc5c47681e1c7f95971e85e610606176dade0`;
- `PROOF.md`:
  `2b580ac93b52cbea6cf1a42d57cb0c74de52072c04326a62cf641de304f6d38f`.

I also checked the closest promoted interfaces P83, P87, and P92--P99 in
`PROVED.md`, plus the density and stable-state boundaries X67--X68 in
`FAILED.md`. I did not modify a frozen input or a durable ledger. I ran no
research computation and used no external source.

## Verdict

**PASS.** The QP rescalings preserve the exact hypotheses of P87 and
P92--P97/P99, the bare-`N` probability calculation is correct, and the new
infinite stable family follows from the stated Bertrand, CRT, and Linnik
construction. I found no missing factorization oracle, hidden branch test,
probability amplification error, input-scope expansion, or quantifier
reversal.

The important construction checks pass. Linnik's prime `q` must be larger
than `p`, not merely bounded above: every positive integer in its CRT class
already satisfies `q >= 1+2s > p`. Also, `q = 2 modulo rad(A)` excludes
every prime divisor of `A` from `B=(q-1)/2`. This proves `gcd(A,B)=1`, and
the displayed identity for `(N-1)/2` then proves
`gcd(AB,N-1)=1`.

## 1. QP bit costs close under every operation used

Write a fixed QP bound as

\[
Q(n)=2^{C(\log_2(n+1))^k}.
\]

A fixed product or fixed power of such bounds is another bound of this
form. Multiplication by a polynomial in `n`, `log Q`, or another fixed QP
cap does not leave the class. This is enough for all algorithms here; none
performs a QP-depth iteration of a QP-cost routine.

For numerical `B <= Q(n)`, the binary length of

\[
M_B=\operatorname{lcm}(1,\ldots,B)
\]

is at most `log_2(B!) = O(B log B)`, hence QP. Incremental lcm construction
uses `B` arithmetic operations on integers of that bit length. Sieving all
integers through `B` is also QP in time and space.

The punctured bank has one member for each prime power `ell^j <= B`, plus
`M_B`. There are at most `B` such prime powers, because they are distinct
integers in `[2,B]`. Thus both the number of exponents and their total
encoded size are QP. Binary modular exponentiation is polynomial in `n`
and the exponent bit length, so applying the complete bank to a QP-size
generator list remains QP.

For a cap `T` and `s` supplied generators, breadth-first closure needs at
most `(T+1)s` generator multiplications before either completion or the
first over-cap element. A discovered proper subset cannot be closed under
all generators of a finite generated group. Pairwise equality lookup, even
without the proposed balanced tree, adds only a factor polynomial in `T`.
All residues and gcd operands have QP bit length. Therefore equality,
multiplication, storage, and gcd work remain QP.

For punctures of `N-1`, factoring all of `N-1` is unnecessary. A scan only
tests candidate primes through the public QP cap. If `ell | N-1`, then
`v_ell(N-1) <= n`, so there are at most `n` depths. Every resulting
exponent has `O(n)` bits. This validates the P94/P96 scan costs.

Finally, a verified trial with worst-case work `W(n)` and success at least
`1/R(n)` has expected work at most `W(n)R(n)`. Both factors are fixed QP
bounds, and verification prevents a false terminal output. Independent
repetition therefore gives the claimed Las Vegas expected-QP bound on the
promised inputs.

## 2. The imported decoder promises were not weakened

The rescaling changes only the numerical caps and corresponding running
time. It does not change the algebraic gates.

- P87 still requires unequal local orders and a complete full-prime-power
  bound on at least one local order. If `sigma(r) <= B`, then `r | M_B`.
  The unpunctured member handles the one-divides/one-does-not case, and a
  puncture at a differing valuation handles the case in which both orders
  divide `M_B`.
- P92 and P93 retain, respectively, the strict pure-phase plus bounded-old-
  order promise and the supplied-separator plus bounded-exponent promise.
  Their useful powered images have size at most `B^2`; replacing polynomial
  `B` by fixed QP `B` makes complete enumeration QP.
- P94 retains both conditions `ell <= L` and
  `ell^(H_ell-C_ell+2) <= S`. P96 likewise retains the public-annihilator
  test, a positive separator, a scanned prime, and the full bound
  `ell^(2(H-C+1)) <= T`. Neither corollary substitutes a small valuation
  gap for the required full image bound.
- P95 retains `1 < AB <= T` for deterministic enumeration. Its randomized
  branch retains `S != 1` and `min(A,B) <= Q`.

For the P95 sampling branch, the P83 sampler can be lengthened until its
total-variation error is at most `1/(2Q)`. With `s` generators, it suffices
to use exponent bit length

\[
O(n+\log s+\log Q).
\]

This costs QP even when `s` is QP. Uniform separator density is at least
`1/min(A,B)` when both orders exceed one. If the smaller order is one and
`S` is nontrivial, the density is `1-1/max(A,B) >= 1/2`. After taking
`Q >= 2`, total variation leaves success at least `1/(2Q)`. Thus the
amplification premise is valid in every promised case.

P97 supplies a generating powered pair with probability at least
`6/pi^2`, conditioned on the two accepted units. A raw nonunit already
returns a verified proper factor, and unit acceptance is greater than one
half. Requiring QP bounded work on every pair is essential because the
generation event is not public; F168 states this requirement.

P99 similarly supplies either a factor or a full-unit-group generating
list with an absolute constant probability. An inverse-QP localizer on
every promised full-group list, with QP work on every list, therefore gives
an expected-QP splitter for each composite. Verified recursion does not
hide a super-QP cost: a factorization tree has fewer than `n` internal
nodes, every child has bit length at most `n`, and a polynomial factor times
one fixed QP bound is QP. The result remains conditional on the missing
localizer.

Exact rejection sampling of a uniform interval has an unbounded random-bit
transcript, as P99 already records, but only polynomial expected cost with
an exponential tail. This does not create a composition gap. Independent
batches have finite polynomial mean cost, so summing their costs up to a
geometric success time gives that mean divided by the per-batch success
probability. Equivalently, one can truncate the exponential tail at a
polynomial cap, count a timeout as failure, and retain an absolute-constant
source probability. The every-transcript QP hypothesis is therefore met by
the localizer and, if desired, by the truncated composite trial.

## 3. The bare-`N` promise probability is exact

For distinct odd primes, the P97 image is

\[
S_N\cong C_A\times C_B,
\qquad \gcd(A,B)=1,
\]

and a uniform accepted unit powers to an exact uniform element of this
image. If `m=min(A,B)` and `M=max(A,B)`, its positive-separator density is

\[
\delta_N=\frac1m+\frac{m-2}{mM}.
\]

For `m >= 2`, this is at least `1/m`; for `m=1`, distinctness gives
`M >= 2` and the density is `1-1/M >= 1/2`. A raw sample from
`1,...,N-1` is a unit with probability

\[
\frac{(p-1)(q-1)}{pq-1}>\frac12,
\]

while a nonunit already exposes a proper factor. Hence the promise
`m <= Q(n)` gives at least `1/(2Q(n))` success per trial after harmlessly
enlarging `Q` to be at least two. Each trial uses polynomial bit work, so
verified repetition has expected QP cost. The algorithm need not recognize
the hidden promise and F168 does not claim success outside it.

## 4. The Linnik and CRT construction forces `p < q`

For an arbitrarily large odd prime `r`, the class

\[
1+2r\pmod {4r}
\]

is reduced: its representative is odd and coprime to `r`. It is also the
least positive representative, so Linnik's prime satisfies

\[
2r<p\le C_0(4r)^L.
\]

The congruence makes `p = 3 modulo 4`, so `A=(p-1)/2` is odd and contains
the prime divisor `r`.

Bertrand gives a prime `s` with `p<s<2p`. For
`R=rad(A)`, one has `R <= A < p < s`, so `gcd(s,R)=1`. The moduli `4s`
and `R` are coprime, and both prescribed residues

\[
1+2s\pmod {4s},\qquad 2\pmod R
\]

are units in their respective modulus. The resulting CRT class modulo
`4sR` is therefore reduced and Linnik applies.

There is no gap in the lower bound for `q`. Every positive integer
congruent to `1+2s modulo 4s` is at least `1+2s`: subtracting one modulus
already makes that representative negative. The CRT class is a subset of
this first class. Thus every positive prime in it, including the least
prime furnished by Linnik, obeys

\[
q\ge1+2s>p.
\]

The proof's phrase about the canonical CRT representative is not needed;
the preceding fact holds for every positive representative. The upper
bound also closes because `s<2p` and `R<p`:

\[
q\le C_0(4sR)^L<C_0(8p^2)^L.
\]

Hence `q` is bounded by a fixed power of `r`, despite the modulus containing
`rad(A)`.

## 5. Both gcd conclusions follow exactly

The first CRT congruence makes `q = 3 modulo 4`; thus
`B=(q-1)/2` is odd and `s | B`. For every prime `t | A`, one has `t | R`
and the second congruence gives

\[
2B=q-1=1\pmod t.
\]

Therefore `t` cannot divide `B`. This holds for every prime divisor of
`A`, including repeated prime-power components of `A`, so

\[
\gcd(A,B)=1.
\]

Since `p-1=2A` and `q-1=2B`, with `A,B` odd, it follows that
`gcd(p-1,q-1)=2`. Also

\[
\frac{N-1}{2}=2AB+A+B.
\]

Reduction modulo `A` gives `B`, and reduction modulo `B` gives `A`.
Consequently both `A` and `B` are coprime to `(N-1)/2`. Their mutual
coprimality gives `gcd(AB,(N-1)/2)=1`; their oddness also gives
`gcd(AB,2)=1`. Hence

\[
\gcd(AB,N-1)=1.
\]

No unsupported lift from radical coprimality to prime-power coprimality is
being made: excluding each common prime is exactly what ordinary gcd one
requires.

## 6. Input length, infinitude, stability, and density all close

The bounds above give absolute constants `C_1,D>0` with

\[
N=pq\le C_1r^D.
\]

The lower bounds `p>2r` and `q>p` give `N>4r^2`. Therefore, for
`n=ceil(log_2(N+1))`,

\[
n=\Theta(\log r).
\]

The upper inequality is the direction needed to obtain
`r >= 2^(cn)` for one absolute `c>0` after deleting finitely many initial
choices. Since `s>p>r`, the same bound holds for `s`. Unbounded choices of
the prime `r` force unbounded `N`, so the construction contains infinitely
many distinct semiprimes.

Because `r | A` and `s | B`, the largest full prime-power components obey

\[
\sigma(A)\ge r\ge2^{cn},\qquad
\sigma(B)\ge s\ge2^{cn}.
\]

Every fixed QP cap is `2^{o(n)}`, so both inequalities eventually exceed
that cap. The quantifier is the correct one: for each fixed QP cap, only a
finite initial part of the one constructed family can be exceptional.

The proved coprimality `gcd(AB,N-1)=1` makes the `(N-1)` power map an
automorphism on `C_A x C_B`. More generally, every positive exponent whose
prime support is contained in that of `N-1` is coprime to `AB`, so it too
acts as an automorphism and preserves both coordinate-identity tests. This
is precisely the immediate P98-stability conclusion; it does not constrain
nonmultiplicative information or states outside P98's retained-supergroup
scope.

Finally, `A>=r` and `B>=s` give

\[
0<\delta_N
=\frac1A+\frac1B-\frac2{AB}
\le\frac1r+\frac1s
=2^{-\Omega(n)}.
\]

A fixed QP number of direct exact-uniform samples is `2^{o(n)}`. The union
bound therefore leaves total success `2^{-Omega(n)}`. This proves only the
stated failure of QP repetition for direct uniform sampling. It is not a
lower bound for adaptive words, relation decoding, canonical integer
feedback, or general factoring, and the frozen statement preserves all of
those exclusions.

## 7. Remaining boundary

Parts I--III are complexity closure and promise reductions, not new
arithmetic mechanisms. Part IV is an existence theorem based on standard
prime-existence inputs; it is not an efficient public generator for the
family and does not need to factor `A` algorithmically. The theorem shows a
length-linked stable rectangle with two exponentially large local prime
components and exponentially sparse direct separators. It does not show
that capped enumeration cannot encounter a separator early, and it supplies
no all-input axis localizer or factoring algorithm.

A fresh proof-blind reconstruction is still required before promotion under
the project protocol.
