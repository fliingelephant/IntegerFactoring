# Hostile whole-artifact audit of F43 inverse-quotient descent

## Artifact and decision

I audited the complete candidate
`experiments/F43_inverse_quotient_descent_kill/RESULT.md` at SHA-256

`bab9cdfcb657d67c8a7043efdd0c02ab748f76ff00bd6a246bc5f473b03ec83e`

and its `RUN_MANIFEST.md` at SHA-256

`87c33325bd8a5fb6e5a3bd83ba49b334b76febd961518db3f7b2927ad0d0e6`.

Both pinned hashes match. I read the F26 registry entry, reconstructed every
unbounded argument, checked the endpoint cases, and independently replayed
F43-D01 through F43-D03. I treated the finite data only as finite data.

The central new mathematics survives. The one-step identity, strict descent,
near-square-root trajectory bound, and lcm-square slow chain are correct. They
are real unbounded results. They do not give a polynomial-time factoring
algorithm.

The artifact does not pass as written. One reverse characterization is
insufficient as typeset. The status text denies results that the artifact then
proves. The manifest has a stale status and a false retained-file hash. The
missing source snapshot for attempt 3 also breaks its exact provenance.

## 1. The forward identity is correct

For clarity, the artifact must first define its map. Let $v$ be the least
positive inverse of a unit $u\bmod N$, and put

\[
D_N(u)=\frac{uv-1}{N}.
\]

For $2\le u<N$, let $r$ be the least positive inverse of $N\bmod u$.
Write $Nr-1=tu$. The bounds $1\le r<u<N$ give $1\le t<N$. Hence
$v=N-t$ is in $\{1,\ldots,N-1\}$, and

\[
uv=N(u-r)+1.
\]

Therefore

\[
D_N(u)=u-r.
\]

The stated decrement characterization is also exact:

\[
D_N(u)=u-r
\quad\Longleftrightarrow\quad
u\mid Nr-1,qquad 1\le r<u.
\]

This proves $1\le D_N(u)<u$ at every nonterminal unit state. It uses
ordered representatives and integer division, not only arithmetic in
$\mathbb Z/N\mathbb Z$. This is the real algorithm-level difference from
the closed scalar-and-gcd routes.

## 2. The reverse factor-pair condition needs repair

The displayed condition

\[
Nk+1=uv,\qquad k<u,v<N
\]

is insufficient or, at best, ambiguous. Read literally as $k<u$ and
$v<N$, it admits factors outside the domain. For example,

\[
N=11,qquad k=1,qquad 12=12\cdot1.
\]

It satisfies the displayed inequalities, but $u=12$ is not a preimage of
$1$ under a map whose domain is $1\le u<N$.

The exact statement is

\[
D_N^{-1}(k)
=\left\{u:k<u<N, u\mid Nk+1\right\}.
\]

If $v=(Nk+1)/u$, these conditions automatically imply $k<v<N$. They
also imply $\gcd(u,N)=\gcd(v,N)=1$. Conversely, both $u$ and $v$ are
preimages of $k$. Thus non-square factor pairs do come in inverse pairs.
The candidate must state both factor bounds explicitly.

This repair does not affect the forward decrement identity or the depth
bound. Those arguments use only the correct forward condition.

## 3. The trajectory bound is correct

Let one trajectory have $L$ transitions, and stop at $1$ or at the first
proper nonunit. Put $r_i=u_i-u_{i+1}\ge1$. The total decrease is less than
$N$.

For a fixed integer $B$ with $1\le B<N$:

- Fewer than $N/B$ transitions can have $r_i>B$.
- For each fixed $1\le r\le B$, every corresponding current state is a
  distinct divisor of $Nr-1$.
- Since $Nr-1<N^2$, there are at most $\Delta_N$ such states, where
  $\Delta_N=\max_{m<N^2}\tau(m)$.

Therefore the safe displayed bound

\[
L\le \frac{N}{B}+B\Delta_N+1
\]

is valid. The standard maximal-order estimate for the divisor function gives
$\Delta_N=N^{o(1)}$. Choosing $B$ near
$\sqrt{N/\Delta_N}$ gives

\[
L\le N^{1/2+o(1)}.
\]

This is sublinear, but it is not a “sub-square-root” bound. The factor
$N^{o(1)}$ is on the upper side of $\sqrt N$. The section title must say
“near-square-root” or “sublinear.” The resulting step bound is still
exponential in the input bit length.

## 4. The lcm-square slow chain is correct

Let

\[
M_L=\operatorname{lcm}(2,3,\ldots,L+1),
\qquad N_L=(M_L+1)^2.
\]

For every $2\le u\le L+1$, one has $N_L\equiv1\pmod u$. Thus $u$
is a unit modulo $N_L$, the inverse of $N_L\bmod u$ is $1$, and

\[
D_{N_L}(u)=u-1.
\]

The trajectory from $L+1$ has exactly $L$ transitions before it reaches
$1$. Also,

\[
\log\operatorname{lcm}(1,\ldots,L+1)=\Theta(L),
\]

so the bit length of $N_L$ is $\Theta(L)$. This rules out a universal
$o(\log N)$ trajectory bound. It does not rule out polynomial time. The
moduli are easy perfect squares, as the candidate correctly says.

## 5. The two-step contraction counterexample is exact

For $N=11$ and $u=7$, the least positive inverse is $8$, so

\[
D_{11}(7)=5,\qquad D_{11}(5)=4,\qquad 2\cdot4>7.
\]

This disproves the universal two-step contraction claim. A counterexample
also exists inside the balanced distinct-semiprime regime that matters for
F26:

\[
N=35,\qquad 19\longmapsto13\longmapsto10,\qquad 2\cdot10>19.
\]

The candidate should add this second witness. The prime witness alone does
not show that a semiprime-only contraction theorem fails.

## 6. Independent replay of F43-D01 through F43-D03

I registered and ran F43-A01 with a 120-second timeout. It independently
reconstructed the finite calculations from the public recurrence. It did not
use any finite result as evidence for an infinite-family claim.

The replay passed all mathematical comparisons:

- All 96 D01 compact records and the global summary match exactly.
- The decompressed attempt-3 archive has the stated SHA-256, and every field
  retained in the compact attempt-4 certificate matches it.
- D01 has maximum depth 13 at $N=481$, minimum direct count $14/192$
  at $N=221$, minimum extended count $130/220$ at $N=253$, and no
  tested all-fail extended offset menu.
- Every D02 record matches, including the six rates, the 15 extended hits in
  50,000 draws on the largest input, zero extended hits in its 1,369-offset
  menu, and maximum sampled depth 46.
- The complete D03 summary, its first 100 stored violations, and every seeded
  per-bit record match. The total is 593,870 violations among 3,887,362
  eligible observations.

The audit run is recorded in `RUN_MANIFEST.md`. Its output is
`output/F43-A01.json` at SHA-256
`5e45881457725882193dc18fdfb059bbb6160baba704922f91e6827970f877ad`.

## 7. Provenance and scope corrections

The following corrections are mandatory.

1. `RESULT.md` says “No unbounded mathematical result is claimed.” This is
   false. Sections 1, 3, and 4 prove results for unbounded $N$ or $L$.
   Replace this with “No polynomial-time factoring result or unbounded success
   probability is claimed.”
2. `RUN_MANIFEST.md` still says the run stopped after two failures and has no
   successful authoritative run. Attempts 3 and 4 succeeded. The top status
   must name attempt 4 as the current authoritative compact D01 run.
3. The manifest states SHA-256
   `7a2c7e1df11985ae624a4806a2639c900b5440b5920a759c88115fb880945775`
   for `output/F43-D01-attempt2-partial.json`. The retained file has SHA-256
   `61a3dd7260425baabacf7a00687c7d6ff477e4c8b821904776a7a42452e67fc6`.
   Record the retained hash, or recover the file that has the stated hash.
4. The attempt-3 source at stated SHA-256
   `0664a9132fcdcdc67d69a6a2d83d7773eaba5129b1107050c390fce779985fc9`
   is not retained at a named path. The current source is the attempt-4
   compact version. Recover the exact attempt-3 source, or explicitly mark
   that historical run as non-reproducible and use attempt 4 as the sole
   authoritative D01 computation.
5. D02 used one deterministic Python PRNG stream per input. It did not
   independently seed each unit. Replace “independently seeded uniform units”
   with “seeded pseudorandom unit draws,” and record Python 3.14.5 for the
   retained replay environment.
6. The sentence that the gcd tickets “become sparse with growing balanced
   factors” reads as an asymptotic conclusion from six inputs. Replace it with
   the exact finite statement: they were sparse on the larger D02 inputs. No
   infinite-family hit bound is proved.
7. Define $D_N$ before the first theorem. Also repair the many bare
   parenthesized TeX fragments such as `(2\le u<N)` to use valid inline math
   delimiters.

The proposed joint transcript decoder is correctly left open. The finite
ticket decay does not rule it out. F26 is not yet a factoring algorithm.

**FAIL AS WRITTEN.**
