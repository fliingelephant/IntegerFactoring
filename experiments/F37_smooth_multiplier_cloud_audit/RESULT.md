# F37 hostile audit: smooth multiplier clouds

**Candidate audited:** experiments/F37_smooth_multiplier_cloud_kill/RESULT.md.

**Context checked in full:** AGENTS.md, PROMPT.md, the F15 row of REGISTRY.md,
P26 in PROVED.md, and X20 in FAILED.md.

**Computation:** none. This audit is entirely symbolic.

## Verdict

> **PASS WITH AMENDMENTS.**

The mathematical core survives hostile reconstruction:

1. the useful/unsplit factor-pair classification, multiplier-gcd preprocessing,
   and all parity cases are correct for a distinct odd semiprime;
2. the exact Fermat index and logarithmic-window formula are correct, including
   the constant \(2\sqrt2\);
3. the continuous divisor-cloud measure bound and its constants are correct;
4. the uniform divisor bound makes the total continuous coverage exponentially
   small even when multipliers have arbitrary encoded size;
5. the LCM cloud is arithmetically valid and has only an \(O(1/m)\) guaranteed
   log mesh while its multiplier penalty is exponential in \(m\); and
6. the de la Vallée Poussin construction gives one infinite balanced
   semiprime family on which every coprime multiplier with
   \(o(\sqrt n)\) bits misses every useful pair through any fixed polynomial
   Fermat scan, uniformly even under input-dependent selection.

I found no counterexample and no missing theorem-strength lemma. The candidate
also correctly refuses to transfer its continuous measure theorem to discrete
prime ratios after the multiplier is allowed to depend on the input.

The amendments below are statement and quantifier repairs. They do not change
either proved obstruction, but they should be made before proof-blind
reconstruction because the current wording occasionally calls a continuous
surrogate a literal scan and slightly overcompresses bit-model and asymptotic
quantifiers.

## Required amendments

### A1. Define Theorem 1's continuous surrogate

The phrase “the set covered by all scans” is not literally defined for a
continuum of \(x=\log r\) at one fixed product \(S\): most real ratios do not
come from integer factors of the integer \(S\), and the theorem currently
allows arbitrary real \(S>0\). The proof bounds the explicitly defined union

\[
\mathcal C=
\bigcup_{i=1}^m\ \bigcup_{c\mid k_i}
\left[
  2\log c-\log k_i-R_i,\,
  2\log c-\log k_i+R_i
\right],
\]

where

\[
R_i=2\sqrt2\,\frac{\sqrt{T_i+1}}{(k_iS)^{1/4}}.
\]

The theorem should define this surrogate set and assert

\[
\operatorname{meas}(I\cap\mathcal C)
\le 4\sqrt2 S^{-1/4}
\sum_i\tau(k_i)k_i^{-1/4}\sqrt{T_i+1}.
\]

Every actual parity-compatible useful factor pair of an integer \(S=N\) found
through index \(T_i\) lies in this set by (4), so the intended necessary-cover
conclusion follows. Alternatively, require \(S\) and all \(k_i,T_i\) to be
positive/nonnegative integers and explicitly say that “covered” means the
necessary logarithmic windows, not that every real point represents a literal
integer factorization. This removes a definitional ambiguity without changing
the proof or constant.

### A2. Make the polynomial and independence quantifiers uniform

After (9), replace “\(m\) and every \(T_i\) are polynomial” by a uniform
statement: there are fixed constants \(C,D\), independent of \(n,i,S\), with

\[
m(n)\le Cn^D,\qquad
0\le T_i(n)\le Cn^D\quad(1\le i\le m(n)).
\]

For the all-ratio covering assertion at fixed \(S\), the list
\(k_1,\ldots,k_m\) must be chosen independently of the particular point
\(x\in I\) it is supposed to cover. It may depend on \(S\) and \(n\). Without
this quantifier, “uniform all-ratio cover” could be misread as permitting a
different cloud for each target ratio, which the measure argument does not
address. The candidate later gives the right adaptive/discrete warning; the
theorem statement should carry it too.

No encoded-length bound on the \(k_i\) is needed for the geometric inequality:

\[
\tau(k_i)k_i^{-1/4}\le C_{1/8}
\]

holds for every positive integer \(k_i\). Polynomial encoded length is needed
only when interpreting the represented scans as a polynomial-bit algorithm.

### A3. Qualify the shorthand in (11)

The exact first expression in (11) is correct. The shorthand

\[
\frac{\ell^2\sqrt{kS}}{32\tau(k)^2}
=\sqrt S\,k^{1/2-o(1)}
\]

is asymptotic as \(k\to\infty\), with the fixed factor \(\ell^2/32\)
suppressed. It should say so, or use equality up to a fixed positive
multiplicative factor. For bounded \(k\), retain the exact formula. This does
not affect the polynomial-list conclusion, which follows directly from (9)
and (10).

### A4. Make the LCM mesh construction literal

The LCM arithmetic is correct, but “choose \(b\asymp m\)” should include one
choice that keeps the rounded numerator at most \(m\). On \(1\le r\le2\), for
example, take

\[
b=\left\lfloor\frac{m-2}{\sqrt2}\right\rfloor,\qquad
a=\operatorname{round}(b\sqrt r).
\]

For all sufficiently large \(m\), \(1\le a,b\le m\), and

\[
\left|2\log(a/b)-\log r\right|=O(1/m)
\]

uniformly on the interval. Also replace the phrase that (4) “demands a radius
containing \(k_m^{-1/4}\)” by the exact statement that success requires the
nearest-center error to be at most

\[
O\!\left(N^{-1/4}k_m^{-1/4}\sqrt{T+1}\right).
\]

For polynomial \(T\) and growing input scale this only strengthens the
exponential-in-\(m\) mismatch.

### A5. Fix the function conventions in Theorem 2

State that \(B:\mathbb N\to\mathbb R_{\ge0}\) is a fixed function satisfying
\(B(n)/\sqrt n\to0\), and that
\(T:\mathbb N\to\mathbb Z_{\ge0}\) is bounded above by one fixed polynomial.
The infinite family may depend on these fixed functions (the proof in fact
gives a family strong enough for all such eventual bounds). This makes
\(B(n)=o(\sqrt n)\), \(T(n)=\operatorname{poly}(n)\), and the simultaneous
quantifier over every \(k\) literal.

The theorem uses \(\log_2k\), not the conventional bit length
\(\lfloor\log_2k\rfloor+1\). Add that they differ by at most one and hence
define the same \(o(\sqrt n)\) regime.

### A6. Narrow the bit-complexity sentence to the represented scan

Section 5 correctly bounds every arithmetic operand, but “do give polynomial
bit complexity” should state all of the following:

* the list has uniformly polynomial cardinality;
* the total encoded length of each multiplier together with its supplied
  complete factorization is polynomial in \(n\);
* producing that represented list, if it is not supplied input, also costs
  polynomial time; and
* every scan has a uniformly polynomial increment cap.

Under these conditions, all multiplication, ceiling-square-root, subtraction,
exact-square testing, and gcd operations have polynomial total bit cost. The
candidate is right that divisor enumeration is unnecessary. Merely knowing the
values have polynomial bit length does not bound an unspecified rule that
manufactures their prime factorizations.

For the recursive all-input paragraph, either take \(P\) nondecreasing or
replace it by \(P^*(n)=\max_{s\le n}P(s)\). Then the conditional-expectation
bound is literally at most \((2n-1)P^*(n)\). Add that finitely many
almost-surely terminating splitter calls imply almost-sure termination of the
recursion. These are standard repairs, but PROMPT requires them explicitly
when the conditional reduction is retained.

### A7. Tie the final “killed” scope to direct useful-square extraction

Theorem 2 proves that no parity-compatible useful factor pair occurs in the
specified scan windows. It therefore kills a scheme whose success is finding
such a square and intersecting \(A-B\) or \(A+B\) with \(N\). It is not a
lower bound against an algorithm that combines nonsquare residues, combines
several scan transcripts by another relation, or otherwise uses the chosen
multipliers without requiring an individually useful factor pair. The final
boundary should say “the direct scaled-Fermat useful-pair/gcd method” rather
than the potentially broader “actual semiprime method.” This matches the
candidate's own surviving-gap paragraph and the broader many-relation idea
that motivated F37.

## Detailed proof audit

### 1. Factor allocations, gcd preprocessing, and parity

Assume \(N=pq\) with distinct odd primes and \(\gcd(k,N)=1\). Unique prime
factorization assigns each of \(p,q\) to exactly one side of \(XY=kN\).
If they are on opposite sides, absorbing all factors of \(k\) into \(c,d\)
gives, after a side exchange, \(X=cp,Y=dq,cd=k\), and the intersections with
\(N\) are \(p,q\). If they are on the same side, one obtains
\(X=cN,Y=d,cd=k\), whose intersections are \(N,1\). The cases are exhaustive.

For noncoprime \(k\), \(g=\gcd(k,N)\) is already a nontrivial split when
\(1<g<N\). If \(g=N\), the promised complete prime-factor list of \(k\)
contains both \(p\) and \(q\); testing its listed primes against \(N\) exposes
them. This depends essentially on the supplied prime factorization. Without
that list, \(N\mid k\) alone would not be a new factoring method.

The factors in an integer difference of squares have the same parity. Since
\(p,q\) are odd, a split allocation is representable exactly when
\(c\equiv d\pmod2\). Thus odd \(k\) permits only odd/odd allocations,
\(v_2(k)=1\) permits none, and \(v_2(k)\ge2\) requires at least one factor of
2 on each side. Counting all \(c\mid k\) is therefore a valid upper bound.

### 2. Exact gap, index, and logarithmic window

For \(X=cp,Y=dq\) and \(r=q/p\),

\[
\frac XY=\frac{c/d}{r}=e^\lambda,\qquad XY=kN.
\]

Thus \(X=\sqrt{kN}e^{\lambda/2}\) and
\(Y=\sqrt{kN}e^{-\lambda/2}\), up to labeling. If the factors have the same
parity, \(A_*=(X+Y)/2\) is an integer and

\[
G=A_*-\sqrt{kN}
=\sqrt{kN}\bigl(\cosh(\lambda/2)-1\bigr)
=\frac{(X-Y)^2}{2(\sqrt X+\sqrt Y)^2}.
\]

With \(A_0=\lceil\sqrt{kN}\rceil\) and
\(\theta=A_0-\sqrt{kN}\in[0,1)\), the exact index is \(j=G-\theta\).
Since \(A_*\) is an integer at least \(\sqrt{kN}\), it is at least \(A_0\),
so no lower-index condition is missing. The condition \(j\le T\) is exactly
(3).

If \(x=\operatorname{arcosh}(1+u)\), then
\(1+u=\cosh x\ge1+x^2/2\), whence \(x\le\sqrt{2u}\). Applying this with
\(u=(T+\theta)/\sqrt{kN}\) yields exactly

\[
|\lambda|\le
2\sqrt2\,\frac{\sqrt{T+1}}{(kN)^{1/4}}.
\]

The direction is necessary, as used later; no converse is claimed after
replacing \(\theta\) by \(1\).

### 3. Measure, constants, and divisor uniformity

For fixed \(k_i\), every allocation has center
\(2\log c-\log k_i\), and distinct divisors \(c\mid k_i\) give exactly
\(\tau(k_i)\) centers. Each necessary interval has radius at most

\[
2\sqrt2\,(T_i+1)^{1/2}(k_iS)^{-1/4}.
\]

Twice this radius, summed over all centers and multipliers, is precisely the
right side of (5). Overlaps only reduce union measure. Squaring (6) under a
common cap gives \(32=(4\sqrt2)^2\) in (10), and one multiplier gives the
exact first expression in (11).

The supplied divisor-function proof is valid and uniform. For every fixed
\(\varepsilon>0\), large primes satisfy
\(e+1\le2^e\le p^{\varepsilon e}\), and each of the finitely many remaining
primes contributes a finite supremum
\(\sup_e(e+1)p^{-\varepsilon e}\). Hence one constant \(C_\varepsilon\),
independent of \(k\), works for all \(k\). Taking \(\varepsilon=1/8\) gives

\[
\tau(k)k^{-1/4}\le C_{1/8}k^{-1/8}\le C_{1/8}.
\]

Therefore a uniformly polynomial number of uniformly polynomial-radius scans
has total surrogate measure at most
\(\operatorname{poly}(n)S^{-1/4}=2^{-\Theta(n)}\) when
\(S=2^{\Theta(n)}\). This is independent of the numerical or encoded sizes of
the \(k_i\). It is only a continuous uniform-cover obstruction; it supplies no
density statement about adaptive discrete prime ratios, and the candidate
explicitly observes this limitation.

### 4. The LCM cloud

If \(L_m=\operatorname{lcm}(1,\ldots,m)\), then for \(a,b\le m\),

\[
c=a(L_m/b),\qquad d=b(L_m/a)
\]

are integers, \(cd=L_m^2\), and \(c/d=(a/b)^2\). The concrete rounding choice
in A4 proves the \(O(1/m)\) log mesh. Chebyshev's standard bounds give
\(\log L_m=\Theta(m)\), so
\(k_m^{-1/4}=L_m^{-1/2}=\exp(-\Theta(m))\). The full divisor set cannot evade
the aggregate bound because Theorem 1 already sums all \(\tau(k_m)\) centers.

### 5. Prime pairs near \(\sqrt2\) and adaptive short multipliers

Use natural logarithms in the PNT estimate. From

\[
\pi(x)=\operatorname{Li}(x)+O\!\left(xe^{-a\sqrt{\log x}}\right),
\]

choose \(0<b<a\) and put \(h=xe^{-b\sqrt{\log x}}\). Then

\[
\operatorname{Li}(x+h)-\operatorname{Li}(x-h)
\asymp \frac{h}{\log x},
\]

while the two endpoint errors are
\(O(xe^{-a\sqrt{\log x}})\). Their ratio to the main term tends to zero:

\[
\frac{x e^{-a\sqrt{\log x}}}
     {x e^{-b\sqrt{\log x}}/\log x}
=\log x\,e^{-(a-b)\sqrt{\log x}}\longrightarrow0.
\]

Thus the symmetric interval contains a prime for every sufficiently large
\(x\). Taking \(x=\sqrt2p\) along arbitrarily large primes \(p\) gives a prime
\(q\) with \(p<q<2p\) eventually. Moreover

\[
\left|q/p-\sqrt2\right|
\le \sqrt2 e^{-b\sqrt{\log(\sqrt2p)}}.
\]

Since

\[
n=\log_2(pq)+O(1)=2\log_2p+O(1),
\]

one may choose a fixed
\(0<\gamma<b\sqrt{(\log 2)/2}\), absorbing the leading constant, to obtain
(12) for all sufficiently large family members. This gives infinitely many
distinct odd balanced semiprimes.

Let \(K=2^{B(n)}\). Since \(B(n)=o(\sqrt n)\),

\[
\gamma\sqrt n-2(\log 2)B(n)\longrightarrow+\infty,
\]

so (12) implies (13), including \(1/6\), uniformly for every \(k\le K\).

For \(cd=k\), the integer \(c^2-2d^2\) is nonzero and
\(c+d\sqrt2<3k\). Therefore

\[
|c-d\sqrt2|>\frac1{3k}.
\]

Also

\[
d|r-\sqrt2|
\le \frac d{6K^2}
\le \frac k{6K^2}
\le \frac1{6k},
\]

where the last step is \(k^2\le K^2\). This proves (15). Exchanging \(c,d\)
gives \(|cr-d|>1/(6k)\), exactly what the swapped allocation
\(X=cq,Y=dp\) needs.

For either orientation,

\[
|X-Y|>\frac p{6k},\qquad
X+Y<3kp,\qquad
(\sqrt X+\sqrt Y)^2<6kp.
\]

Substitution in the exact gap identity gives

\[
G>\frac{p^2/(36k^2)}{12kp}
=\frac p{432k^3},
\]

so \(432\) is correct. Uniformly over all \(k\le K\),

\[
\log\frac p{432k^3}
\ge \frac{\log 2}{2}n-3(\log 2)B(n)-O(1)
=\Theta(n),
\]

which eventually exceeds the logarithm of any fixed polynomial \(T(n)+1\).
Since \(j=G-\theta>G-1\), \(G>T+1\) implies \(j>T\). This proves the
simultaneous quantifier over every deterministic or randomized input-dependent
choice in the allowed size range; a polynomial list is covered pointwise.

### 6. Bit sizes and all-input recursion

For a \(b\)-bit multiplier and polynomial scan cap, \(kN\), \(A\),
\(A^2-kN\), its integer square root, and the gcd operands have
\(O(n+b+\log(T+1))\) bits; squaring changes only the hidden constant. Standard
integer arithmetic makes each scan step polynomial in this length. With A6's
representation and generation qualifications, a polynomial list of
polynomially capped scans is polynomial-bit work.

The conditional all-input reduction is sound. Splitting until prime leaves
gives at most \(n\) leaves and \(n-1\) internal nodes because every leaf is at
least \(2\). Conditioning on each encountered composite and using a uniform
nondecreasing bound \(P^*(n)\) permits linearity of expectation even though the
recursion tree is random. Exact division, deterministic primality testing, and
final multiplication verification add polynomial cost. This handles even
inputs, repeated prime factors, prime powers, and arbitrary composites **if**
an every-composite splitter exists. F37 supplies only negative information on
a distinct-odd-semiprime family and does not supply such a splitter.

## Exact surviving boundary after audit

After the amendments, the result proves two narrow obstructions:

* a list fixed independently of the target ratio cannot cover a fixed
  positive-length continuum interval with polynomially many polynomial-length
  Fermat windows, regardless of multiplier magnitude; and
* on one infinite balanced semiprime family, every direct useful-pair Fermat
  scan using a coprime \(o(\sqrt n)\)-bit multiplier and a fixed polynomial
  number of increments fails, simultaneously over adaptive choices and lists.

It does **not** rule out:

* adaptive \(N\)-dependent multipliers of \(\Omega(\sqrt n)\), linear, or
  larger polynomial bit length;
* a theorem concentrating a cloud only on the actual discrete prime ratio;
* combining many nonterminal scan relations rather than demanding one useful
  factor pair;
* a different metric observable, non-Fermat decoder, residue mechanism, or
  non-gcd terminal extraction; or
* a complete all-input factoring algorithm.

The candidate remains at the hostile-audit stage. After incorporating the
listed amendments, it is suitable for a fresh proof-blind reconstruction.
