# F226 blind reconstruction

## Protocol and verdict

Required statement SHA-256:

`204b34f248610717000bc7d90dc80836125b78844fb23e6142412e0652ea6d40`

Observed statement SHA-256:

`204b34f248610717000bc7d90dc80836125b78844fb23e6142412e0652ea6d40`

The hashes agree. I reconstructed the claims from `STATEMENT.md` without
reading any proof, audit, provenance, result, manifest, ledger, script, or
output. The named `PROMPT.md` was not present at the specified experiment
path, so it supplied no information.

**Verdict: PASS**, for the intended factoring domain of positive odd
integers greater than one and with the stated conditional terminal and
recursive-dispatch hypotheses. The random bank does not prove an all-input
factoring transition. The statement correctly isolates that missing step.

There are three scope qualifications, none of which changes the main
result.

1. Read literally for every odd integer, Theorem A needs `N>1`; `N=1`
   gives `A=0`. This is automatic in the factoring and semiprime domain.
2. The prose part of Theorem D is an invariance result only for a transcript
   that consists of scalar character-product data. It is not an
   impossibility theorem for non-scalar identities, quotient/carry data, or
   the full child integers.
3. Formula (H5) is rigorously an upper bound on the exponential scale. A
   matching lower bound needs `P,Q<B`, exclusion from `L_0`, and the usual
   nonsaturation conditions. The obstruction uses only the upper bound.

The finite aggregate scan counts are discovery evidence, not a theorem I
can independently certify under the blind-file restriction. The displayed
small witness itself checks directly.

## A. Top-bit child and local orbit

Let `k=n-1`. For a positive odd `N>1`, its bit-length convention gives

\[
2^k<N<2^{k+1}.
\]

The left inequality is strict because `2^k` is even. Hence

\[
A=N-2^k>0,
\qquad
A<N/2 \iff N<2^{k+1}.
\]

Also

\[
\gcd(A,N)=\gcd(2^k,N)=1.
\]

If `ell|A`, then `N=2^k (mod ell)`. With
`d=ord_ell(2)`, the standard order-of-a-power identity gives

\[
\operatorname{ord}_\ell(N)
=\operatorname{ord}_\ell(2^k)
=\frac d{\gcd(d,k)}.
\]

Now let `N=pq`. In the unit group modulo `ell`,

\[
q=Np^{-1}.
\]

Thus `p` belongs to `<N>` if and only if `q` does. If it does, the map
`i mod h_ell -> N^i` is a bijection from `Z/h_ell Z` to `<N>`. This gives
the unique class `i_ell(p)`, and multiplication by `q` yields

\[
p=N^{i_\ell(p)},
\qquad
q=N^{1-i_\ell(p)}\pmod\ell.
\]

A simultaneous exponent is precisely a solution of

\[
i=i_\ell(p)\pmod {h_\ell}
\]

for all bank primes. Generalized CRT says that this system is soluble if
and only if every pair of residues agrees modulo the gcd of its two
moduli. This is (A8). Factoring the public integers supplies the moduli
`ell` and, after factoring `ell-1`, the orders. It supplies neither the
hidden residue class nor CRT compatibility.

Attempted refutation: nonconsecutive local orders can share arbitrary
factors, but generalized CRT already accounts for this through the gcd in
(A8). No pairwise-coprimality assumption is used.

## B. Exact-uniform bank and recursive cost

Multiplication by odd `N` is a permutation of the odd residue classes
modulo `B=2^m`. Therefore

\[
R_m(u)=uN\bmod B
\]

is exactly uniform over the odd integers in `[1,B)`. Reduction from
`2^{j+1}` to `2^j` proves

\[
R_{j+1}=R_j\quad\hbox{or}\quad R_j+2^j.
\]

In the second case,

\[
\gcd(R_j,R_j+2^j)=\gcd(R_j,2^j)=1,
\]

because `R_j` is odd. This says nothing about nonconsecutive prefixes, so
deduplication is necessary.

There are fewer than `m` children. Their total bit-length is bounded by
`sum_{j<=m} j=O(m^2)=O(n^2)`. For an integer of `j` bits, the number of
prime factors counted with multiplicity is at most `j`; summing over the
children gives `O(n^2)` prime occurrences. Every child prime `ell` is less
than `2^m`, so `ell-1` also has at most `m` bits. Thus the immediate child
and order-factorization dispatch per bank has the claimed size.

For the recursive bound, suppose uniformly that

\[
K(x)\le 2^{C(\log x)^c}.
\]

Then `B(x)=K(x)O(x^2)` has

\[
\log_2 B(x)=O((\log x)^{c'}),
\qquad c'=\max(c,1).
\]

At depth `r`, the bit size is at most `ceil(n/2^r)`, and there are
`O(log n)` levels. Consequently

\[
\begin{aligned}
\log_2\prod_r B(\lceil n/2^r\rceil)
&=\sum_r O\!\left((\log\lceil n/2^r\rceil)^{c'}\right)\\
&=O((\log n)^{c'+1}).
\end{aligned}
\]

Exponentiation proves (B5). Polynomial local work and the sum over levels
do not change this class. By contrast, branching `Theta(n)` ways while
decreasing the size by only one bit produces a factor comparable to `n!`,
whose logarithm is `Theta(n log n)`, not `poly(log n)`.

Attempted refutation: the recurrence establishes cost, not correctness of
factoring arbitrary children. The statement preserves this distinction and
later makes the all-input recursive-dispatch assumption explicit.

## C. Conditional residue terminal

Compatible local exponent congruences have a solution class modulo

\[
H=\operatorname{lcm}_{\ell\in Q}h_\ell.
\]

The powers of `N` modulo `S` are periodic with a period dividing `H`.
Therefore, if `H<=T`, at most `H`, hence at most `T`, public exponent
representatives need inspection. Each certified representative gives a
true congruence `p=N^i (mod S)`.

Combining a true residue modulo `S` and a true residue modulo `L_0` is a
generalized-CRT operation. Overlap between the moduli is harmless: truth
of both congruences supplies consistency, and the resulting modulus is
their lcm.

The slack in (C4) is compatible with the standard known-residue terminal.
If the available modulus is `R>=N^{1/4}/Q(n)`, enumerate at most `Q(n)`
extensions of the residue to a modulus at least `N^{1/4}`, then apply the
balanced-semiprime known-residue terminal. Numerical-QP slack therefore
costs only numerical QP. Theorem C remains conditional on both the common
exponent certificate and that terminal; it does not manufacture the
certificate.

## D. Affine torsor and the exact scope of scalar rejection

For every unit `x mod S`, there is exactly one unit `y` with `xy=N`, namely
`y=Nx^{-1}`. This proves (D1). Applying a multiplicative character gives

\[
(\chi(x),\chi(y))=(z,\chi(N)z^{-1}),
\qquad z=\chi(x),
\]

which proves (D2). A transcript containing only these scalar product
relations is invariant as `x` moves through the torsor. Such a transcript
fixes the product `chi(N)` and cannot choose `z` or orient `x,y`.

This is the exact limit of the rejection. The torsor calculation does not
show that the actual integer factors are uniformly distributed. It also
does not cover a relation that depends on the two components separately,
an APR/CL identity with more structure, the multiplier label, a quotient
or carry, or an Archimedean constraint on the full integers.

The named probability model is exact. Uniform `X` in the unit group maps
bijectionally to a uniform point `(X,NX^{-1})` of the torsor. Hence, for a
public exponent set `I`,

\[
\Pr(X\in\{N^i:i\in I\})
=\frac{|\{N^i\bmod S:i\in I\}|}{\varphi(S)}
\le\frac{|I|}{\varphi(S)}.
\]

For every odd prime `ell`, `(ell-1)^2>=ell`. Squarefreeness therefore gives

\[
\varphi(S)=\prod_{\ell\mid S}(\ell-1)
\ge\prod_{\ell\mid S}\sqrt\ell=\sqrt S.
\]

If `S>=N^{1/4}/QP(n)` and `|I|=QP(n)`, then, using
`N>=2^{n-1}`,

\[
\frac{|I|}{\sqrt S}
\le 2^{-n/8+(\log n)^{O(1)}}
=2^{-\Omega(n)}.
\]

This exponential probability belongs only to the named torsor model.
Applying it as a distribution law for adversarial factors or for random
`u` would be invalid, and the statement does not do so.

Finally, if a single exponent works for every prime in squarefree `S`,
then each such prime divides `N^i-p`; their product therefore divides it.
This proves (D7) and identifies the hidden integer support that a positive
random-bank theorem would have to hit.

## E. Ensemble identities and incidence bounds

Set `v=uN mod B`. Odd multiplication permutes the odd residues modulo
`B`. Also

\[
R_j(u)=v\bmod 2^j.
\]

Thus the complete child-vector multiset is exactly the prefix-vector
multiset of uniform odd `v`, proving (E0). The quotient and the original
label are lost in the substitution `u -> v`, so the independence claim
correctly excludes them.

At level `m`, every odd integer below `B` occurs once, proving (E1). At
level `j`, every odd residue below `2^j` has exactly `2^{m-j}` lifts,
proving (E2). Multiplying over `j` proves (E3). Prime factorization of the
same integer multiset preserves this independence, including
multiplicity.

For a fixed odd prime `ell<B`, an odd multiple of `ell` below `B` is
`ell t` with `t` odd and

\[
1\le t\le M:=\left\lfloor\frac{B-1}{\ell}\right\rfloor.
\]

There are `ceil(M/2)` such values. Division by `B/2` gives the equality in
(E4), and

\[
\pi_\ell
\le \frac{M+1}{B}
\le\frac1\ell+\frac1B
\le\frac1\ell+\frac2B.
\]

For prefixes with `2^j<=ell`, incidence is impossible. Let `j_0` be the
first index with `2^{j_0}>ell`. A union bound and (E4) give

\[
\begin{aligned}
\Pr(\ell\mid R_j\text{ for some }j)
&\le\sum_{j=j_0}^m\left(\frac1\ell+\frac2{2^j}\right)\\
&<\frac m\ell+\frac4\ell
=\frac{m+4}{\ell}.
\end{aligned}
\]

Capping by one proves (E5). A second union bound over `K` independent
banks proves (E6). Independence is not needed for this upper bound, though
it is present.

Attempted refutation: prefixes within one bank are highly correlated.
Nothing here treats them as independent; (E5) is only a union bound.

## F. Hidden cyclotomic support and the bounded-variable inequality

Let `h=ord_ell(N)`. In the cyclic group modulo `ell`, the roots of
`z^h=1` form the unique subgroup of order `h`, namely `<N>`. Thus

\[
p\in\langle N\rangle
\iff p^h=1.
\]

Since `q=Np^{-1}` and `N^h=1`, this is also equivalent to `q^h=1`. This
proves (F1). Adding the exact-order condition proves that the accepted
primes of order `h` are exactly the primes dividing
`gcd(p^h-1,q^h-1)`, as in (F2).

For `ell in G_i`, the congruence defining `G_i` says
`ell|(N^i-p)`. The difference is nonzero for every `i>=0` when `N=pq`
with nontrivial distinct primes. The squarefree support product therefore
divides `|N^i-p|`. For `i=0`, this is `p-1<N`; for `i=1`, it is
`N-p<N`; and for `i>=2`, it is less than `N^i`. Consequently

\[
L_i< n\max(1,i)\le nT.
\]

This bound is on total logarithmic support. It gives no lower bound on
that support or on its sampling probability.

For a fixed support prime, independence of the `s` full-child samples gives
capture probability `1-(1-pi_ell)^s`. Writing `X_i` as the weighted sum of
the prime-capture indicators and using linearity of expectation proves
(F6); independence among different primes is neither true nor needed.

The direction of (F7) follows only from boundedness. Since
`0<=X_i<=L_i`,

\[
\mathbb E X_i
\le \theta+(L_i-\theta)\Pr(X_i\ge\theta).
\]

Rearrangement gives (F7). This implication requires an expectation
surplus as a hypothesis. It cannot be reversed into a lower bound on the
expectation. In particular, support logarithm concentrated on primes of
size `2^{Theta(n)}` has incidence only `2^{-Theta(n)}` per QP number of
samples.

## G. Subset-complete Las Vegas bridge and public cap

The squarefree product `W` makes every captured compatible product `C_i`
a squarefree divisor of `W`. When `2^{omega(W)}<=D`, exhaustive divisor
enumeration therefore includes the hidden `C_i`. Exhaustive enumeration
of `i<T` includes its exponent. If (G2) holds, generalized CRT supplies the
true residue at terminal size. Any output is verified by a gcd, so false
candidates affect time only. This proves the Las Vegas and
subset-completeness claims without an APR oracle.

For an odd integer `r`,

\[
2^{\omega(r)}=\sum_{d\mid r}\mu^2(d).
\]

Average this over uniform odd `r<B`. For every odd squarefree `d<B`, the
probability that `d|r` is at most `1/d+2/B`. Therefore

\[
\begin{aligned}
\mathbb E 2^{\omega(R_m)}
&\le\sum_{d<B}\frac1d
   +\frac2B\#\{d<B:d\text{ odd squarefree}\}\\
&\le (1+\log B)+1
=2+\log B,
\end{aligned}
\]

which proves (G3). Because the prime set of `W` is the union of the prime
sets of the children,

\[
2^{\omega(W)}\le\prod_{r=1}^s2^{\omega(R_m^{(r)})}.
\]

The children are independent, so expectations factor. Markov's inequality
then proves (G4).

The definition of `G_i` makes `C_i` coprime to `L_0`. Hence (G2) is exactly
the event `X_i>=theta`. Combining (F7) with the union bound

\[
\Pr(X_i\ge\theta\text{ and no discard})
\ge\Pr(X_i\ge\theta)-\Pr(\text{discard})
\]

proves (G5). No independence between progress and cap survival is assumed.

If `s<=(log n)^a`, then

\[
\log D
=s\log(2+\log B)+\log P(n)
=(\log n)^{O(1)}.
\]

Thus the cap, the divisor enumeration, the exponent enumeration, and a QP
number of blocks all remain numerical QP. All recursive arguments have at
most half the parent bit-length, so the recurrence from B applies. This is
cost accounting conditional on a factorization dispatch that works for
arbitrary child shapes; random children do not inherit balancedness.

For the concrete exponents,

\[
p\equiv1\pmod\ell \Rightarrow \ell\mid p-1,
\]

and

\[
p\equiv N=pq\pmod\ell,
\quad \ell\nmid p
\Rightarrow \ell\mid q-1.
\]

This proves (G6).

The favorable-state corollary also checks. Let `d` be odd with `4d<=B`.
For uniform odd `v<B`, the number of multiples `dt` with odd `t` is

\[
\left\lceil\frac12
\left\lfloor\frac{B-1}{d}\right\rfloor\right\rceil,
\]

which is at least `B/(4d)`. After division by `B/2`,

\[
\Pr(d\mid R_m)\ge\frac1{2d}\ge\frac1{2Q(n)}.
\]

With the public cap `D=4Q(n)(2+log B)`, (G4) for one child gives discard
probability at most `1/(4Q(n))`. On divisibility by `d`, either gcd
screening already finds a factor of `N`, or every prime of `d` enters `W`.
The appropriate candidate is `i=0` when `d|p-1` and `i=1` when
`d|q-1`. Therefore

\[
\Pr(\text{verified success})
\ge\frac1{2Q(n)}-\frac1{4Q(n)}
=\frac1{4Q(n)}.
\]

The cap is public because it depends on the public upper bound `Q`, not on
the hidden favorable divisor. This is essential. Choosing a cap from the
unknown `d` would not define an algorithm.

Attempted refutation: enumerating all subsets of a large deterministic
prime bank would not be QP. G does not do that. It enumerates subsets only
of the sampled `W`, and abandons precisely when their count exceeds the
public cap.

## H. High-prime tail, deterministic cutoff, and safe-prime shift

For `ell>Y`, (E6) gives hit probability at most
`K(m+4)/ell<=K(m+4)/Y`. Hence

\[
\mathbb E Z_i(Y)
\le\frac{K(m+4)}Y
\sum_{\ell\in\mathcal G_i}\log_2\ell
\le\frac{K(m+4)L_i}{Y}.
\]

Moreover,

\[
\sum_{i=0}^{T-1}L_i
<n\sum_{i=0}^{T-1}\max(1,i)
\le nT^2.
\]

Summation proves (H1). If some `Z_i(Y)>=Delta`, then their nonnegative sum
is at least `Delta`; Markov's inequality proves (H2).

The tail direction is important. Given an asserted success probability
`rho` and progress amount `Delta`, both inverse QP, take for example

\[
Y>\frac{2K(m+4)nT^2}{\rho\Delta}.
\]

This `Y` is numerical QP and makes the probability of high-prime progress
`Delta` less than `rho/2`. Equivalently, if a route supplies inverse-QP
progress with inverse-QP probability, then after replacing `Delta` by a
constant fraction as needed, an inverse-QP part of that event is carried
by primes at most `Y`. A deterministic sieve lists all such prime values in
numerical-QP time.

This conclusion does not reveal which listed primes are compatible. It
does not permit enumeration of all subsets of the list. It also does not
reproduce the useful random grouping into a small `W`, the multiplier
quotient, or any non-scalar calculation on a child. Thus the deterministic
cutoff dominates prime-value discovery only, exactly as claimed.

For (H3), every prime with `ord_ell(N)=h<=T` divides `N^h-1`. If there are
`M` such primes at least `X`, then

\[
X^M
\le \prod_{h=1}^T(N^h-1)
<N^{T(T+1)/2}.
\]

Taking binary logarithms and using `log_2 N<n` proves

\[
M<\frac{nT(T+1)}{2\log_2X}.
\]

At `X=N^{1/4}/QP(n)`, this count is QP, while (E6) makes the hit probability
for each such prime at most

\[
\frac{K(m+4)}X
=2^{-n/4+(\log n)^{O(1)}}.
\]

A union bound remains `2^{-Omega(n)}`. One terminal-size small-order prime
therefore cannot yield the desired inverse-QP transition through these
banks.

In the conditional safe-prime-shift model,

\[
p-1=2P,
\qquad q-1=2Q.
\]

The only possible odd compatible prime for `i=0` is `P`, and the only one
for `i=1` is `Q`, subject to the defining cutoff and exclusions in
`G_i`. If `P,Q` are of size `Theta(sqrt N)`, (E6) and a union bound give

\[
\Pr(\text{hit }P\text{ or }Q)
\le K(m+4)\left(\frac1P+\frac1Q\right)
=2^{-n/2+(\log n)^{O(1)}}.
\]

If either prime is outside the child range or excluded by `L_0`, its hit
probability is zero, which only strengthens the upper bound. No assertion
about infinitely many such balanced safe-prime pairs is needed. The model
shows why a uniform smoothness or harmonic-mass theorem is genuinely new
input rather than a consequence of exact-uniform child sampling.

## Exact displayed witness

The arithmetic identity is

\[
563\cdot593=333859.
\]

This integer has `n=19` and `m=9`. For the unmultiplied lower-half prefix
bank, reduction modulo `2^j`, `2<=j<=9`, gives only `3` and `35`; the odd
auxiliary primes are `3,5,7`. Directly,

\[
\begin{array}{c|c|c}
\ell&333859\bmod\ell&563\bmod\ell\\ \hline
3&1&2\\
5&4&3\\
7&1&3
\end{array}
\]

Modulo `3` and `7`, `<N>={1}`. Modulo `5`, `<N>=<4>={1,4}`. In all three
cases `563` lies outside the subgroup, so the zero-acceptance conclusion
for this displayed bank is exact.

## Final logical boundary

The reconstruction proves exact uniformity of the integer ensemble,
upper incidence laws, a conditional bounded-variable progress lemma, and
a QP-safe subset enumeration. None supplies the missing lower bound

\[
\sum_{\ell\mid N^i-p}
\log\ell\,[1-(1-\pi_\ell)^s]
\ge \theta+1/\operatorname{QP}(n)
\]

for some QP-bounded `i`, uniformly over all inputs and histories. The high
tail bound goes in the opposite direction: beyond a QP cutoff, it makes
random support discovery negligible. The safe-prime-shift model shows an
exact shape in which the guaranteed classes have only exponentially large
odd support. Therefore the advertised remaining alternative is correct:
one needs a new all-input harmonic/smooth-support theorem or a verified
non-scalar factor/carry transition on rejection.
