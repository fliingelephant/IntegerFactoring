# F190 statement-only blind reconstruction

## Input and independence record

I reconstructed this candidate using only `PROMPT.md` and the frozen
`STATEMENT.md`. I did not read any other F190 artifact or any durable ledger.
No mathematical computation was used.

The independently measured SHA-256 of `STATEMENT.md` is

`78e8cfd74e5ed824e6bb74c3aacbef0e9af6c67746373aa6e478a77ed9930b38`.

## Verdict

**PASS.** Every exact algebraic, probabilistic, coding, and QP claim in the
statement follows from first principles in its named model. The result is a
boundary, not an unconditional factoring algorithm.

Two scope qualifications are essential:

1. The adaptive-scalar simulator statement applies to P53's explicit
   correlation observation model, with a QP-size expansion and QP
   coefficient `l1` norm. Total shift support alone would not control an
   arbitrary succinct scalar with an uncontrolled Walsh expansion. The
   statement expressly leaves that case open.
2. Exponential Fourier support and recurrence order do not imply an
   exponential sparse-description lower bound. The statement limits the
   conclusion to dense reconstruction, explicit enumeration, and
   materialized rank.

## Reconstruction

### 1. Scale and screened shifts

From

\[
 n=\lceil\log_2(N+1)\rceil
\]

one obtains `2^(n-1) <= N < 2^n`, including the endpoint case
`N=2^j-1`. If

\[
 \mathcal Q(n)=2^{C(\log_2(n+1))^k}
\]

with fixed `C,k`, then `log_2 Q(n)=o(n)`. Thus `Q(n)=2^{o(n)}`. A fixed
product of such envelopes adds only a fixed number of polylogarithmic
exponents, so it remains QP.

For `N=pq` and `p<q<2p`, multiplication and squaring give

\[
 \sqrt{N/2}<p<\sqrt N<q<\sqrt{2N}.
\]

In particular `p,q=2^{n/2+O(1)}`. Every fixed QP quantity is therefore
`o(p)` and `o(q)`.

After reduction and deduplication modulo `N`, a nonzero shift difference is
not divisible by both `p` and `q`. If it vanishes modulo exactly one hidden
prime, its gcd with `N` is proper. On the no-factor branch every difference
is a unit modulo `N`, so all shifts are distinct modulo each hidden prime.

### 2. Retained-source decoding is factoring-equivalent

Assume the decoder in Section 1. The following gives a splitter, and hence
complete factorization.

First remove the factor two. Use deterministic primality testing and exact
perfect-power detection. A prime is terminal. If `M=A^e` with `e>1`, factor
the strictly shorter integer `A` and multiply all returned exponents by
`e`.

For a remaining odd composite of bit length `k`, enumerate the primes up to

\[
 B=4m(k)k
\]

and divide out their full powers. This costs QP bit operations because `B`
is a fixed numerical QP bound and all operands have `O(k)` bits. Reapply
the prime and perfect-power tests to the residual.

Suppose the residual is composite and not a perfect power. Every one of its
prime divisors now exceeds `B`. There are fewer than `k` distinct prime
divisors. For a uniform source modulo `M`, at most `m(k)` residue classes
modulo each hidden prime make one of the consecutive shifted entries a
nonunit. A union bound gives

\[
 \Pr[\text{row rejected}]
 \le \sum_{r\mid M}{m(k)\over r}
 < {k m(k)\over4k m(k)}={1\over4}.
\]

Repeated prime powers do not add new forbidden residue classes. Rejection
sampling consequently produces independent uniform accepted sources with
constant expected overhead. Their QP many Jacobi entries and the gcd
acceptance screens are computable in QP bit time.

Invoke the decoder on `L(k)` rows. Verify every returned candidate by
primality testing and exact division into `M`; divide out its full power.
If a call fails to return a verified prime, use fresh randomness and retry.
An inverse-QP success probability gives QP expected trials and almost-sure
termination. Recursive subproblems strictly decrease, and a complete factor
tree has only `O(k)` prime occurrences and internal splits. A polynomial
number of fixed-QP calls remains QP. This handles even inputs, primes,
perfect powers, repeated factors, and arbitrary composites.

Conversely, an all-input Las Vegas QP factorer can ignore the supplied rows
and factor `M`. A non-perfect-power integer has at least one odd prime
exponent: if every exponent were even, it would be a square. The factorer
can therefore return a numerical prime having odd exponent. This is a
retained-source decoder with success probability one. The equivalence is
exact when the decoder's requested output is a numerical hidden prime.

### 3. Fourier support, recurrence order, and Hankel rank

Use CRT to identify a residue modulo `N` with a pair modulo `p` and `q`.
The additive character in the Fourier transform factors into two local
additive characters, up to multiplication of each local frequency by a
unit. Thus

\[
 \widehat s(a)=G_p(a_p)G_q(a_q),
\]

where `G_r(0)=sum_x chi_r(x)=0`, while for a nonzero local frequency the
quadratic Gauss sum has magnitude `sqrt(r)`. A local frequency is zero
exactly when the corresponding prime divides `a`. Hence

\[
 \widehat s(a)=0\iff\gcd(a,N)>1,
 \qquad
 |\widehat s(a)|=\sqrt N\iff\gcd(a,N)=1.
\]

There are exactly `phi(N)=(p-1)(q-1)` unit frequencies. Balancedness gives

\[
 \varphi(N)=N-p-q+1=N-O(\sqrt N)=2^{\Theta(n)}.
\]

A periodic complex sequence is a sum of the Fourier exponentials in its
support. Distinct exponentials are linearly independent. A
constant-coefficient annihilator must vanish at every active Fourier root,
and their product supplies an annihilator. The minimal recurrence order is
therefore exactly the number of active modes, namely `phi(N)`.

The periodic Hankel matrix has the factorization

\[
 H=V\,\operatorname{diag}(c_a)\,V^{\mathsf T}
\]

over the active Fourier modes, where `V` is the invertible full Fourier
matrix and `c_a` is the corresponding nonzero Fourier coefficient, up to a
nonzero normalization and reversal convention. Its rank is therefore also
the Fourier-support size `phi(N)`.

Thus a dense Prony or Pade model, an explicit list of all frequencies, or a
materialized rank-`phi(N)` representation has exponential scalar dimension.
This says nothing about a sparse high-degree formula, implicit determinant,
or arithmetic algorithm, exactly as stated.

### 4. Autocorrelation and raw sample complexity

For an odd prime `r`, quadratic-character autocorrelation is

\[
 \sum_{x\bmod r}\chi_r(x)\chi_r(x+d)
 =\begin{cases}r-1,&d=0,\\-1,&d\ne0.\end{cases}
\]

The nonzero case follows after scaling by `d` from the fact that
`sum_x chi_r(x(x+1))=-1`. CRT multiplies the two local correlations. This
gives exactly

\[
 C_N(d)=\varphi(N),\ 1-p,\ 1-q,\ 1
\]

in the four divisibility cases listed in the statement. A factor-sensitive
nonzero difference has a proper gcd with `N`; after difference screening,
every nontrivial complete pair correlation is the public value one.

For a uniform `t mod N`, define the raw Fourier summand
`Z=s(t)zeta_N^(-at)`. At a unit frequency,

\[
 |E Z|^2={1\over N},
 \qquad
 E|Z|^2={\varphi(N)\over N}.
\]

The relative mean-square error of the average of `R` independent samples is

\[
 {\operatorname{Var}Z\over R|EZ|^2}
 ={\varphi(N)-1\over R}.
\]

Relative root-mean-square error at most `eta` therefore requires
`R >= (phi(N)-1)/eta^2` for this empirical estimator.

For unit `d`, put `W=s(t)s(t+d)`. Its mean is `1/N`. Its square is one
exactly when neither local coordinate of `t` or `t+d` is zero. Hence

\[
 E W^2=(1-2/p)(1-2/q)=\rho_d.
\]

The same variance calculation gives the exact empirical requirement

\[
 R\ge{N^2\rho_d-1\over\eta^2}.
\]

For fixed nontrivial relative accuracy, both sample counts are exponential
in `n`. These are claims about the raw empirical means, not universal
statistical lower bounds.

### 5. Explicit low-order correlations at QP scale

For `u` distinct screened shifts, a nonconstant local shifted-character
moment is a complete character sum of a squarefree polynomial of degree at
most `u`. The Weil bound gives magnitude at most `(u-1)sqrt(r)` over each
hidden prime. CRT multiplication and normalization by `N` therefore give

\[
 O(u^2/\sqrt N)
\]

for the nonconstant global drift. Terms that reduce to the constant-one
baseline differ only at punctures, whose density is also bounded at this
scale. If `u<=Q(n)`, this is

\[
 2^{-n/2+o(n)}.
\]

An explicitly expanded QP list with QP coefficient `l1` norm changes the
bound by only another fixed-QP factor. A hybrid argument also permits
past-adaptive selection when each observation uses a fresh independent
source: condition on the past, apply the same uniform moment bound to the
next explicit scalar, and add the QP many conditional total-variation
errors.

This reconstruction uses the statement's explicit-observation scope. An
arbitrary succinct scalar on one row can have a non-QP Walsh expansion even
when its raw shift support is QP. Neither the moment-to-variation step nor
the claimed simulator bound applies to that excluded case. Retaining the
source or row, making several correlated decisions on one row, and implicit
high-degree statistics remain open.

### 6. Local puncture moments and list sizes

For `S` empty, the accepted local domain has `r-m` points, so
`B_r(empty)=r-m`. For nonempty `S`, the polynomial

\[
 f_S(X)=\prod_{j\in S}(X+a_j)
\]

is squarefree because the shifts are distinct. Its complete quadratic
character sum has magnitude at most `(|S|-1)sqrt(r)`. Passing from the full
field to the accepted domain removes `m-|S|` nonzero terms of magnitude one;
the roots indexed by `S` already contribute zero. Therefore

\[
 |B_r(S)|
 \le(|S|-1)\sqrt r+(m-|S|)
 \le(m-1)\sqrt r.
\]

On the accepted domain, the indicator of the local word `epsilon` is

\[
 2^{-m}\prod_{j=1}^m(1+\epsilon_j\chi_r(x+a_j)).
\]

Expanding and summing proves the exact Walsh formula for `L_r(epsilon)`.
The triangle inequality over the nonempty subsets proves its stated error
bound.

For a pair `(x,z)` over `F_p x F_q`, the indicator that the coordinatewise
product word equals `y` is

\[
 2^{-m}\prod_{j=1}^m
 (1+y_j\chi_p(x+a_j)\chi_q(z+a_j)).
\]

Expansion separates the two local sums and gives equation (18). The empty
subset is `(p-m)(q-m)/2^m`; every nonempty term has magnitude at most
`(m-1)^2 sqrt(N)`. Averaging fewer than `2^m` such terms proves (19).

If `m <= (1/2-delta)log_2 N`, the relative error is at most

\[
 O\!\left({m^2 2^m\over\sqrt N}\right)
 =O(m^2N^{-\delta})=o(1),
\]

uniformly in `y`; also `(p-m)(q-m)=N(1+o(1))`. This proves (21).

The condition `2^m` QP is equivalent to `m=(log n)^{O(1)}`. Such `m` is
`o(log N)`, so the preceding asymptotic applies, and

\[
 F_y={N\over2^m}(1+o(1))=2^{n-o(n)}.
\]

Conversely, making the quotient `N/2^m` QP forces

\[
 m\ge\log_2N-(\log n)^{O(1)}
 =n-(\log n)^{O(1)}.
\]

A literal enumeration of all `2^m` local sign splittings is then
`2^{Theta(n)}`. This count forgets the retained integer source. Given that
source, the local pair must be its CRT reduction, so the row-only count is
not a source-aware decoding obstruction.

### 7. Long-word distance

Fix distinct local sources `x,z`. Excluding shifts `-x,-z` leaves `r-2`
positions. At a remaining shift, agreement minus disagreement is the
quadratic-character correlation

\[
 \sum_a\chi_r(a+x)\chi_r(a+z)=-1.
\]

If `A` and `D` denote the numbers of agreements and disagreements, then

\[
 A+D=r-2,
 \qquad A-D=-1,
\]

so `D=(r-1)/2` exactly.

For a fixed pair that remains accepted under a uniformly chosen `m`-subset
of columns, conditioning on acceptance makes the columns a uniform sample
without replacement from these `r-2` positions. The disagreement fraction
is greater than one half. A hypergeometric Hoeffding or Chernoff bound gives

\[
 \Pr[\text{fewer than }m/6\text{ disagreements}]
 \le \exp(-\Omega(m)),
\]

with a constant much stronger than needed at `m>=96 ln r`. Union bounding
over fewer than `r^2/2` source pairs leaves failure probability at most
`r^{-2}`. Pairs not simultaneously accepted do not form two codewords and
need not be counted.

Thus `O(log r)=O(n)` columns can make all realized local codewords separated
by constant relative distance, so an exact received local word has at most
one local source. The finite small-prime cases can be absorbed into the
constant in the `O(log r)` existence statement. This removes distance and
row-only information as obstructions in the long-word regime, but it does
not reveal the unknown modulus defining either local code.

### 8. Accepted-source collision bounds

Conditioned on row acceptance, a local source is uniform on the complement
of the `m` forbidden residues. Sources from different accepted rows remain
independent. For two arguments from distinct rows, an equality modulo `p`
has probability at most `1/(p-m)`; the analogous bound holds modulo `q`.
Arguments within one row are already distinct by shift screening.

There are at most `binom(K,2)` argument pairs. A union bound therefore gives

\[
 \binom K2\left({1\over p-m}+{1\over q-m}\right).
\]

With `K=Rm` and both factors QP, this is `2^{-n/2+o(n)}`. An equality modulo
one hidden prime but not the other makes the gcd of the public argument
difference with `N` proper. Constant collision probability needs
`K=Theta(sqrt(p))=N^{1/4+o(1)}=2^{n/4+o(n)}`, outside QP.

### 9. Bounded-degree correlated fresh sources

Screening every coefficient has the claimed consequence. If all
coefficients vanish modulo both hidden primes, the polynomial is zero
modulo `N` and is discarded. If all coefficients vanish modulo one hidden
prime but not the other, any coefficient witnessing the latter has a
proper gcd with `N`. On the no-factor branch, every retained polynomial is
therefore a nonzero polynomial over both fields.

A nonzero degree-`D` polynomial over a field has at most `D` roots. For
uniform `Z mod N`, CRT and a union bound over `H` polynomials and two fields
give

\[
 \Pr[\text{some local root}]
 \le HD(1/p+1/q).
\]

Here `H,D` are fixed QP quantities and hence smaller than `p,q` for all
sufficiently large inputs. Balancedness turns the bound into
`2^{-n/2+o(n)}`.

For an acceptance event `A` with probability at least a fixed `c>0`,
`Pr(E|A)<=Pr(E)/c`, proving the conditioning statement. For a past-adaptive
menu evaluated at a fresh source, condition on the complete past; the menu
is then fixed and the same root bound applies. Differences `g_i-g_j` are
polynomials of the same bounded-degree type after coefficient screening,
so the result includes QP many such equality tests.

Exponential-degree succinct relations, rational relations with new
denominator behavior, and repeated high-order operations on one retained
source are not covered.

### 10. Surviving interface

The preceding results exclude only the named low-order and explicit routes:
dense Fourier or Hankel materialization, raw empirical correlation,
explicit controlled-Walsh observations, short row-only puncture lists,
ordinary local collisions, and bounded-degree fresh-source equalities.

Long words can already have good local distance. The unresolved task is not
decoding a known Paley code. It is to use the retained public integer source
and its Jacobi row to decompose a product of two codes whose moduli are the
unknown factors. A new route must do this with a high-order or succinct
operation, return a verifiable divisor, and avoid each exponential
materialization listed in Section 7.

If that interface is strengthened to promise a numerical hidden prime with
inverse-QP probability on every required residual, the reduction in
Section 2 shows that the promise is already QP-equivalent to factoring. The
candidate supplies no such decoder and therefore does not resolve the main
factoring goal.

## Reconstruction conclusion

All claims reconstruct. No computation, external theorem search, proof
packet, or durable ledger was used. The statement merits verifier-backed
status only if its separate hostile audit also passes.
