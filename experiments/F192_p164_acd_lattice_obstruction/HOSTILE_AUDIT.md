# F192 hostile audit

## Verdict

**PASS.** The frozen statement and proof are correct in their stated narrow
scope. I found no mathematical error, missing endpoint condition, reversed
prime label, or unsupported complexity conclusion.

This is a proof-only audit. I used no mathematical computation, literature,
or community claim. Hashing was the only computation. I did not modify the
frozen candidate files or a durable ledger.

## Frozen inputs and authoritative premise

I read `STATEMENT.md`, `PROOF.md`, and `SELF_AUDIT.md` in full. Their current
SHA-256 hashes are:

- `STATEMENT.md`:
  `23834b7193ce2f3e8e32a3277832fab633c2b7a701bd74591087b3d30ab57cb8`;
- `PROOF.md`:
  `73c520f978b47c7a937a5169456e8303818f69f6123a59ba5758ba4f9684e1f4`;
- `SELF_AUDIT.md`:
  `f86a9a7d30bcb4a68d85b86f168135d1db35bf46af5b19c4c581510026b05564`.

All three hashes match `MANIFEST.md`. The manifest itself has SHA-256
`eb9d7d3fb0060ae5107a5b76af35b0e17ace15f52f95ab82db0cfc4f66244e35`.

I also read the authoritative P164 entry in `PROVED.md`, including lines
17522--17590 and the rest of the P164 statement. The full `PROVED.md` hash is
`30cfe89dabddb9193197f1e58e6071720daf4203c91f4f662a7735e672f75b5d`.
The exact byte stream produced by lines 17522--17590 plus their terminating
newlines has SHA-256
`d611a7b833057403322c54d76f911f2954dc2cd2b28c108681c6b1a7aa1eaedb`.

P164 expressly says that every prime in every final local order sees every
selected base as a unit of multiplicative order greater than `K`. Selecting
one such base gives exactly F192 condition (3) for both final local orders.
F192 does not infer independent action directions. Its P164 premise is valid.

## 1. Simultaneous local distinctness

Suppose two word entries with `0 <= i < j <= K` agree modulo a hidden prime
`S`. Their exponent difference is

\[
 a^j-a^i=a^i(a^{j-i}-1).
\]

The local order `g_S` divides this difference. Every prime divisor of `g_S`
is coprime to `a`, so `gcd(a,g_S)=1`. Thus `g_S` divides
`a^(j-i)-1`. For any prime `ell|g_S`, this forces
`ord_ell(a)|(j-i)`, while `1 <= j-i <= K`. This contradicts the P164
order bound. The same public word and the same premise apply to both `P` and
`Q`. There is no hidden choice that makes distinctness hold at only one
factor.

The endpoint `R=K+1` is exact: the largest difference between labels in
`0,...,R-1` is `K`. Local distinctness also implies `R<=P` and `R<=Q`.

## 2. Circular cluster and unit differences

The `R` positive cyclic gaps modulo `S` sum to `S`. Each gap occurs in
exactly `m` of the `R` arcs made of `m` successive gaps. One such arc has
length at most `mS/R`. Each partial arc from its first label is positive and
no longer than the full arc. Its integer residue `r_i` therefore satisfies

\[
 0<r_i\le mS/R\le\lceil mS/R\rceil.
\]

This argument remains valid when the chosen arc crosses zero. Reducing the
global least-nonnegative difference modulo `N` and then modulo `S` gives the
same clockwise residue because `S|N`. Hence `z_i=St_i+r_i` for an integer
`t_i`.

The two labels are distinct modulo both hidden primes, not only modulo the
prime used to define the arc. Thus neither prime divides `z_i`, and every
`z_i` is a unit modulo `N`. There is no circularity: local distinctness is
proved before the cluster is chosen, and unit status uses the independent
distinctness statement at both factors.

The indices remain hidden. The proof does not claim that distinctness or the
gap average identifies them publicly.

## 3. Public balance bound and ceiling

From `P/Q<=C` and `N=PQ`, one has `P<=sqrt(CN)`. Therefore

\[
 \widehat B_{\rm pub}=\left\lceil{m\sqrt{CN}\over R}\right\rceil
\]

dominates `ceil(mP/R)`. The ceiling contributes less than one and causes no
asymptotic defect. In particular,

\[
 {\widehat B_{\rm pub}\over P}
 \le {m\over R}\sqrt{CQ/P}+{1\over P}
 \le (\sqrt C+1){m\over R},
\]

where `1/P<=m/R` follows from `R<=P` and `m>=1`. Likewise,

\[
 {\widehat B_{\rm pub}\over Q}\le C{m\over R}+{1\over Q}.
\]

Thus a fixed sufficiently small upper bound on `m/R`, followed by
sufficiently large input size, gives the required strict inequality
`widehat B<Q`. The theorem separately assumes this strict inequality. It
does not silently derive it for every cluster size.

## 4. Determinant, factor vector, and prime orientation

The displayed row basis is triangular. Its determinant is exactly
`widehat B*N^m`, and every lattice vector has the stated coefficient form.

The cluster must be taken modulo the larger prime `P`. Multiplying
`z_i=Pt_i+r_i` by the complementary, smaller prime `Q` gives the literal
lattice vector

\[
 (Q\widehat B,Qr_1,\ldots,Qr_m).
\]

Its first coordinate is `Q*widehat B`, and all its coordinates have absolute
value at most this number. The norm bounds follow. Raising the determinant
ratio to the power `D=m+1` gives

\[
 { (Q\widehat B)^D\over \widehat B(PQ)^m}
 =Q(\widehat B/P)^m,
\]

so formula (13) is exact.

The choice `P>=Q` is essential and is made explicitly. If the construction
were instead clustered modulo `Q`, a coefficient divisible by the smaller
prime could evade the first-coordinate threshold. F192 makes no such
claim.

## 5. Simultaneous Dirichlet constant and integer `A`

For integer `A>=2^m`, let `H=floor(A^(1/m))`. Since `A^(1/m)>=2`,
`H>=A^(1/m)/2`. The `H^m+1` torus points occupy `H^m` half-open boxes.
Subtracting two indices gives a nonzero integer

\[
 1\le c\le H^m\le A
\]

and simultaneous torus errors at most
`1/H<=2A^(-1/m)`. The factor two and the upper bound on `c` are both exact.
No distribution assumption enters.

The theorem assumes an integer `A` in the open interval. Its lower strict
inequality gives each residual coordinate absolute value strictly below
`Q*widehat B/sqrt(D)`. Its upper strict inequality gives the same bound for
the first coordinate. The resulting nonzero vector therefore has Euclidean
norm strictly below `Q*widehat B`.

There is no omitted integer-existence step in the asymptotic corollary. The
logarithm of the lower endpoint is `o(n)`, while the logarithm of the upper
endpoint is `n/2-o(n)`. Their ratio tends to infinity exponentially, so the
open interval contains an integer for all sufficiently large `n`. Also,
because `widehat B<Q<=P`, one has `epsilon<1`; hence the lower endpoint is
strictly greater than `2^m`. Any integer above it satisfies `A>=2^m`.

## 6. Every exact shortest vector has only unit coordinates

The constructed vector proves `lambda_1(L)<Q*widehat B`. Now take any exact
shortest nonzero vector and write its leading coefficient as `c`.

If `c=0`, some other coordinate is a nonzero multiple of `N`, so the norm is
at least `N`. But

\[
 Q\widehat B<Q^2\le PQ=N.
\]

Thus `c` cannot be zero. If `gcd(c,N)>1`, then `|c|>=Q`, because `Q` is the
smaller hidden prime. The first coordinate alone then has absolute value at
least `Q*widehat B`, again contradicting the strict shortest-vector bound.
Therefore `c` is a unit modulo `N`.

The inequality `0<widehat B<Q<=P` also makes `widehat B` a unit modulo `N`.
The first coordinate is therefore a unit. Each residual coordinate is
congruent to `c*z_i` modulo each hidden prime. Both factors are units, so
every residual coordinate is a unit as well. This applies to every exact
shortest vector, including either sign and all ties.

The conclusion concerns gcd tests of `c` and individual output coordinates.
It does not exclude a different postprocessor that combines coordinates.

## 7. Fixed-balance numerical-QP/polylogarithmic corollary

Fixed balance gives `log_2 Q=n/2+O(1)`. Equation (8) gives
`epsilon>=m/R`, while the natural-scale assumption gives
`epsilon=O(m/R)`. For numerical-QP `R`, `log R=(log n)^{O(1)}`. For
polylogarithmic `m`,

\[
 m\log_2(2\sqrt D/\epsilon)=(\log n)^{O(1)}=o(n).
\]

Also `log D=o(n)`, so
`log_2(Q/sqrt(D))=n/2-o(n)`. This proves the claimed eventual interval and
does not rely on a heuristic determinant estimate. The corollary continues
to require `m<R`, the valid cluster bound, and `widehat B<Q`. It says nothing
about larger dimensions or another lattice.

## 8. Oriented cyclic-order subset-bank count

There are `(R-1)!` oriented cyclic orders of `R` labels. For a fixed proper
`s`-subset, collapsing a consecutive occurrence to one object gives
`(R-s)!` oriented cyclic orders of the collapsed objects and `s!` internal
orders. Thus the subset is consecutive in exactly `s!(R-s)!` cyclic orders,
a fraction

\[
 {s!(R-s)!\over(R-1)!}={R\over\binom Rs}.
\]

A family that covers every oriented cyclic order must therefore have size at
least `binom(R,s)/R` by the union bound. The range `2<=s<R` removes the only
degenerate full-cycle case. Rotation conventions and reversal do not change
the incidence fraction; the proof consistently uses oriented orders.

This count is only a necessary condition. A consecutive block need not be
the short block supplied by the gap average, so the count is not a
sufficiency theorem or a tight lower bound for finding the short cluster.
Any bank guaranteed to contain a short cluster must at least meet this weaker
consecutive-block condition, which is the exact property stated in Section
4. The proof also does not claim that every cyclic order is realizable by a
P164 power word.

## Scope guardrails

The following restrictions are necessary and correctly stated:

1. The lattice theorem is conditional on the correct larger-prime cluster
   and a valid integer bound `widehat B<Q` being supplied.
2. The negative result covers only the row lattice in equation (9), exact
   Euclidean SVP, and gcd tests of the coefficient or individual coordinates.
3. It is not a lower bound for other lattices, approximate or robust ACD
   decoders, affine targets, polynomial methods, or integer factoring.
4. It does not obstruct a selector that uses the public power recurrence or
   another factor-asymmetric invariant.
5. The subset-bank count concerns fixed, order-oblivious banks over all
   oriented cyclic label orders. It does not assert P164 realizability of all
   orders and does not identify the metrically short block.
6. Unit coordinates modulo `N` have no automatic implication about prime
   support in the hidden local orders. F192 makes no such implication.

No correction to the frozen candidate is required.
