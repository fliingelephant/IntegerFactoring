# F227 hostile audit

## Authentication

I authenticated the frozen inputs before reading them.

- `STATEMENT.md`:
  `2d62d7fdad17f58f4cc6963f6b3f5345effcf70a0e38544ab1e19db08783c7a5`
- `PROOF.md`:
  `16faaa4592a368724f6948c2b19deff5711a134080dbf5c1b17e5ca99c9b6afe`
- `SELF_AUDIT.md`:
  `824e1dc642fd817e8c1ed7ba9bfde36859d7de3ac284df4f500d97d10ab5eeaa`
- `PROVENANCE.md`:
  `a89429adcf4e01b00436b2473de8a07a9bbaf7b1fd2ec7dcc95caed2674d7c39`

All four hashes matched. I then read all four files and `MANIFEST.md` in
full. I also checked the promoted F220 V2 and P161 source interfaces used by
the packet.

## Verdict

**FAIL, for one formal statement defect.** The AP estimate, the probability
upper bound, the fixed-base progression, the nonstale classification, and
the rough-residual dichotomy survive hostile review. However, the frozen
packet never defines `n` or `numerical-QP`. Its asymptotic probability and
recursive bit-cost conclusions therefore contain a free parameter and are
not closed theorem statements.

This is a narrow repair failure, not an algebraic counterexample. With the
usual explicit definition

\[
n=\lceil\log_2(N+1)\rceil
\]

and with one fixed numerical-QP envelope used uniformly over all adaptive
histories, I found no further defect.

## Promotion-blocking defect: undefined complexity parameter

The setup defines `N,p,q,I_N,L,s,C,H,A_x`, but it never defines `n`.
Nevertheless, Theorem B and Theorem C use all of the following:

- `S(n)` and `Q(n)`;
- `2^{(\log n)^{O(1)}}`;
- `2^{-\Omega(n)}`;
- “numerical-QP” and “QP-diffuse”;
- an `n/2+O(1)` recursive child size; and
- the recurrence `T(n)<=Q(n)T(n/2+O(1))+Q(n)`.

The proof sentence “Balance gives `q=Theta(p)` and `n=Theta(log p)`” does
not define `n`. It assumes the missing input-length definition. Nor does
the phrase “input bit length” in Theorem C bind the earlier occurrences of
`n`.

The adaptive-bank conclusion also needs “QP-diffuse” to mean that one fixed
numerical-QP function bounds `eta H` for every relevant history. Allowing
the hidden constants in `O(1)` to vary with the history would not give one
uniform `2^{-Omega(n)}` bound. This uniform reading is standard and makes
the argument work, but the frozen statement does not say it.

No frozen file may be repaired in place. A revised packet should define the
input length and numerical-QP convention before the theorems and bind one
fixed diffuseness/trial envelope for the adaptive assertion.

## Hostile mathematical checks

### Candidate cell, endpoints, and direct targets

From `p<q<2p`,

\[
\sqrt{N/2}<p<\sqrt N.
\]

Thus `p` is in the integer interval `I_N`. The upper endpoint is below `q`
and below `2p`, so `p` is the only member of `I_N` with nontrivial gcd with
`N`.

Because `L` is even and every candidate is congruent to the odd number `p`,
every candidate `x` is odd. Hence `A_x=x-1` is even. Also

\[
0<A_x<\sqrt N<q<2p.
\]

The only possible positive multiple of `p` in this range is `p`, and parity
excludes it. A multiple of `q` is impossible. Therefore
`gcd(A_x,N)=1` for every candidate. The only direct target is exactly
`x=p`; its mass is at most `eta`.

If `W=|I_N|`, then

\[
W\ge(1-2^{-1/2})p-2.
\]

A residue class in `W` consecutive integers occurs between
`floor(W/L)` and `ceil(W/L)` times. In the preterminal range
`L<N^{1/4}/S(n)<=N^{1/4}<2^{1/4}p^{1/2}`, this gives both

\[
H=\Omega(p/L)
\quad\text{and}\quad
H=O(p/L).
\]

The proof writes only the lower estimate explicitly, but the omitted upper
estimate is immediate and the claimed `Theta(p/L)` is correct.

### AP gcd mean and max-atom conversion

For each `d|m`, the congruence `c+jL=0 mod d` is either insoluble or one
class modulo `d/gcd(d,L)`. Its count in `H` consecutive indices is at most

\[
H\frac{\gcd(d,L)}d+1\le\frac{HL}{d}+1.
\]

Multiplication by the largest atom `eta`, followed by

\[
\gcd(A,m)=\sum_{d\mid\gcd(A,m)}\varphi(d),
\quad
\sum_{d\mid m}\varphi(d)=m,
\]

gives exactly Theorem A. Insoluble congruences, endpoint classes, and
nonuniform laws are all safely overcounted.

Applying the result for `m=p-1` and `m=q-1` contributes one additive
`eta` term for each field. Adding the direct `x=p` mass gives the stated
constant `3`. The conversion

\[
\eta[3+HL(R_p+R_q)]
=(\eta H)[3/H+L(R_p+R_q)]
\]

is exact. No direct-target term is missing.

### Necessity of a local return for every declared F220 exit

For fixed `x`, a uniform unit has independent uniform reductions in
`F_p^*` and `F_q^*`, and therefore

\[
\Pr(a^{A_x}=1\bmod r)
=\frac{\gcd(A_x,r-1)}{r-1}.
\]

The imported F220 V2 channel has only these routes:

1. The initial gcd is proper. Then at least one, but not all, hidden local
   components return.
2. The initial gcd is `N`. Then all hidden components return, and only then
   are the primary tests run.
3. The initial gcd is one. F220 runs no primary test and certifies no block.

For the squarefree two-prime scope of F227, every factor or primary-support
exit is therefore contained in the union of the `p`-return and `q`-return
events, apart from `x=p`. This validates the union bound in equation (10).
It would not validate a claim about arbitrary processing of nonreturns, but
the statement explicitly leaves such processing outside scope.

### Preterminal scale, divisor bound, and exponential decay

The elementary divisor estimate in the proof is uniform:

\[
\tau(m)=\exp\!\left(O\left(\frac{\log m}{\log\log m}\right)\right)
=m^{o(1)}.
\]

Its small-prime and large-prime split accounts for all multiplicities.
Since `q=Theta(p)`, the two divisor terms are uniformly
`p^{-1/2+o(1)}` in the preterminal range. The direct term has the same
upper scale because `H=Omega(p/L)`.

After multiplying by a fixed numerical-QP bound on `eta H`, the result is
still `p^{-1/2+o(1)}`. Under the missing but intended input-length
definition, `n=Theta(log p)`, so this is `2^{-Omega(n)}`. A fixed
numerical-QP number of adaptive trials is `2^{o(n)}` and preserves that
exponential bound by a conditional union bound.

The conditioning is valid because the candidate and all its preprocessing
are fixed before the next base is sampled, and that base is stated to be a
fresh independent uniform unit. The theorem does not cover candidate/base
couplings, reuse of a conditioned base, or small-integer distributions.
Those exclusions are material and are stated.

### Fixed-base return progression and nonstale condition

The index of `p` supplies a solution of

\[
\operatorname{ord}_p(a)\mid x_j-1.
\]

After division by `gcd(o_p,L)`, the step is invertible modulo

\[
u_p=o_p/\gcd(o_p,L).
\]

Thus the returning indices form exactly one class modulo `u_p`, with at
least `floor(H/u_p)` members. The density bound in Theorem C is correct,
including all endpoint phases.

If a candidate returns only modulo `p`, its gcd is `p`. If it returns in
both fields, repeated prime-by-prime stripping has the following exhaustive
behavior:

- unequal local order valuations eventually give a proper gcd;
- equal valuations leave the exact common order `E=o_p=o_q`; and
- if this common order does not divide `L`, at least one certified primary
  power strictly enlarges `lcm(L,E)`.

Therefore a `p`-return can lack progress, other than the always-useful
direct candidate `x=p`, only when

\[
o_p=o_q\quad\text{and}\quad o_p\mid L.
\]

This is exactly the packet's stale condition. Staleness is not claimed to
make the direct candidate useless, and Theorem C uses nonstaleness only as
a sufficient condition. There is no missed equal-order or unequal-order
branch.

### P161 rough residual dichotomy

On P161's rough-descendant exit, every prime divisor of `o_p` exceeds the
chosen cap `T`. Every prime divisor of

\[
u_p=o_p/\gcd(o_p,L)
\]

is still a prime divisor of `o_p`. Hence either `u_p=1` or `u_p>T`.
For `Q<T`, the condition `u_p<=Q` forces `u_p=1`, equivalently
`o_p|L`. Then every candidate exponent returns modulo `p` because
`x` is congruent to `p` modulo `L`.

The corollary does not apply to P161's factor or exact-common-order exits.
Its premise and its “P161-normalized rough unit” wording correctly restrict
it to the rough descendant. It also does not confuse P161 roughness with
the weaker existence of one large primary component.

### Recursive and per-trial costs

After defining `n` as the input bit length, `A_x<sqrt(N)` gives a child of
at most `n/2+O(1)` bits. Sampling the candidate, modular powering, gcds,
and factor-first stripping have polynomial bit cost once the complete
factorization of `A_x` is supplied. A numerical-QP expected number of full
recursive child factorizations gives

\[
T(n)\le Q(n)T(n/2+O(1))+Q(n).
\]

Across `O(log n)` size halvings, the product of fixed numerical-QP factors
remains numerical QP. This is a valid expected-cost recurrence for a
recursive complete-factorization routine. It is not a construction of the
missing base source, and the statement does not claim that it is.

For the negative theorem, the complete factorization of every `A_x` is
explicitly granted for free, so no factoring-cost assumption can weaken the
upper bound.

## Final assessment

I found no counterexample to the mathematical inequalities or branch
classifications. The declared-channel scope is honest. The frozen packet
nevertheless fails as written because its complexity and exponential
claims use an undefined `n` and an unstated uniform adaptive QP envelope.
Those definitions require a revised frozen statement; they cannot be
supplied by interpretation during promotion.
