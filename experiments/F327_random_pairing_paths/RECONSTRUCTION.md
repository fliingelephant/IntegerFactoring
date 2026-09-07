# Independent reconstruction of F327

## Audit boundary and inputs

This reconstruction used exactly the following input files:

| Input | SHA256 |
|---|---|
| `experiments/F327_random_pairing_paths/STATEMENT_ONLY.md` | `46a229a44bf590989a00cabdadeb22e72b96bb90134a720222e352d3463e06a0` |
| `experiments/F326_direct_gauss_pairing/STATEMENT.md` | `d672ba5f54f299aeb169692ebdcbd6e13f3690a600ec2d303344bd12a200dfa8` |

The other declared dependency is the P02 consequence that comparison with an
independent uniform hidden square root succeeds with probability
`1-2^(1-s)`. No P02 file or shared ledger was read. The needed CRT fact is also
proved below, so the probability calculation is self-contained. No candidate
report, experiment design, implementation, proof, or shared record was read.

## 1. Structure of the involution

Let (Q=\{x\in V:F(x)=x\}), so (|Q|=q). Every nonfixed orbit of an
involution has two elements. Hence

\[
d=q+2m,\qquad m=(d-q)/2.
\]

In particular, (q\equiv d\pmod 2). Since (d) is odd, (q) is odd and
positive. Thus the process always has a fixed vertex at which it can stop.

## 2. Lazy generation of the random matching

Condition on the initially selected vertex (j). A uniform perfect matching
on (V\setminus\{j\}) has the following exposure rule: for any currently
unmatched vertex (y), its mate is uniform among all other unmatched vertices.
After exposing that pair, the restriction to the remaining vertices is again a
uniform perfect matching. This follows either by counting completions, since
every possible mate leaves the same number of completions, or by induction on
the number of remaining pairs.

Write (X_0=j). If (X_k) is nonfixed, write (Y_k=F(X_k)). All earlier
failures removed complete nonfixed (F)-orbits. Therefore (Y_k) has not been
used before. The lazy algorithm removes (Y_k), chooses (X_{k+1}) uniformly
from the remaining unmatched vertices, and exposes
(A(Y_k)=X_{k+1}). This is exactly the uniform-matching exposure rule above.
Induction proves that every exposed (A)-edge has the same joint law as it has
under a uniform perfect matching of (V\setminus\{j\}). If a full matching is
required, completing the still-unmatched vertices uniformly gives exactly that
law. The algorithm need not generate the unused completion.

For the pool implementation, keep an active prefix of a conceptual array and
two sparse maps: position to value and value to position. Missing map entries
mean the identity. To delete a specified value, use the inverse map to find its
position, swap in the value at the last active position, update a constant
number of map entries, and shorten the prefix. Uniform deletion first samples a
uniform active position and then performs the same swap. Obsolete entries, and
entries equal to their identity defaults, can be erased. Each deletion therefore
uses (O(1)) balanced-tree operations. There are (O(T)) deletions through
(T) evaluations, so the maps contain (O(T)) words. If later oracle queries
must reproduce exposed matching edges, storing both directions of each exposed
pair also takes (O(T)) words. Every key, value, and counter is below (d), so a
word has (O(\log d)) bits.

For an active pool of size (n>1), draw
(\ell=\lceil\log_2 n\rceil) fair bits and reject the resulting integer when
it is at least (n). The acceptance probability is
(n/2^\ell>1/2), independently of how depleted the pool is. Thus fewer than
two trials are needed in expectation, and the expected number of fair bits is
(O(\log d)) per sample. Balanced-tree height is (O(\log d)), so the expected
matching overhead per evaluation is polynomial in (\log d).

There is one necessary wording qualification. Fair-bit rejection has no finite
deterministic worst-case running time: an arbitrarily long sequence of rejected
draws has positive probability. Thus claim 1 is correct as an expected-cost
claim. A literal deterministic or per-outcome polynomial bound on its random
running time would be false.

## 3. Hazard, survival, and capped expectation

After (k) failures, exactly (k) nonfixed (F)-orbits have been removed.
Before selecting the next current vertex, the remaining set has size (d-2k),
contains all (q) fixed vertices, and the current vertex is uniform in that
set. Therefore, for (0\le k\le m),

\[
\lambda_k:=\Pr(H=k+1\mid H>k)=\frac{q}{d-2k}.
\]

At (k=m), this hazard is (q/q=1). Hence (H\le m+1). For an integer
(T) with (1\le T\le m+1), survival through the first (T) evaluations
requires a failure at each of hazards (0,\ldots,T-1), so

\[
S_T:=\Pr(H>T)
=\prod_{k=0}^{T-1}(1-\lambda_k)
=\prod_{k=0}^{T-1}\frac{d-q-2k}{d-2k}.
\]

The factor at (k=m) is zero. Thus (S_0=1) and setting (S_T=0) for
(T>m+1) agrees with the actual support. It follows directly that

\[
\Pr(H\le T)=1-S_T.
\]

For every positive integer-valued random variable,
(\min(H,T)=\sum_{k=0}^{T-1}{\bf 1}_{\{H>k\}}). Taking expectations gives

\[
\mathbb E\min(H,T)=\sum_{k=0}^{T-1}S_k.
\]

## 4. Uncapped mean and endpoint law

Let (e_m) be the mean when there are (m) nonfixed pairs and (q) fixed
vertices. The first evaluation is always paid. With probability
(2m/(q+2m)), it fails and leaves the same problem with (m-1) nonfixed
pairs. Therefore

\[
e_0=1,\qquad
e_m=1+\frac{2m}{q+2m}e_{m-1}.
\]

Induction gives

\[
e_m=1+\frac{2m}{q+2}=\frac{q+2m+2}{q+2}
=\frac{d+2}{q+2}.
\]

For endpoint uniformity, fix a particular (z\in Q). Conditional on any
history of (k) failures, no fixed vertex has been removed, and the next
current rank is uniform among (d-2k) ranks. Hence

\[
\Pr(H=k+1,\text{ endpoint}=z)=\frac{S_k}{d-2k},
\]

the same value for every (z\in Q). Summing over (k<T) shows that,
conditional on (H\le T), every fixed endpoint has probability (1/q).
This conditional statement is understood only when (T\ge1), for which the
conditioning event has positive probability.

## 5. Monotonicity of expected cost per capped success

Put

\[
a_T=\sum_{k=0}^{T-1}S_k=\mathbb E\min(H,T),\qquad
p_T=1-S_T=\Pr(H\le T).
\]

The hazards (lambda_k=q/(d-2k)) are nondecreasing. For (1\le T\le m),

\[
p_T=\sum_{k=0}^{T-1}S_k\lambda_k
\le \lambda_T\sum_{k=0}^{T-1}S_k
=\lambda_Ta_T.
\]

Also

\[
a_{T+1}=a_T+S_T,\qquad
p_{T+1}=p_T+S_T\lambda_T.
\]

Since all quantities are positive,

\[
\frac{a_{T+1}}{p_{T+1}}\le\frac{a_T}{p_T}
\quad\Longleftrightarrow\quad
p_T\le\lambda_Ta_T,
\]

which was just proved. At and beyond the maximum possible stopping time the
quantities are constant. Thus (a_T/p_T) is nonincreasing for all positive
integer caps.

If a fixed setup cost (c\ge0) is paid once per attempt, the corresponding
ratio is

\[
\frac{c+a_T}{p_T}=\frac{a_T}{p_T}+\frac{c}{p_T}.
\]

The first term is nonincreasing by the preceding argument, and the second is
nonincreasing because (p_T) is nondecreasing. This proves the setup-cost
extension. It uses one fixed pair ((d,q)); no step supports a comparison after
mixing different input-dependent pairs.

## 6. Fixed ranks in the arithmetic involution

Use the F326 definitions and conclusions as declared. In particular, (d) is
odd, the ranked map is an evaluable involution, and its stated decoders are
available. Write

\[
N=\prod_{i=1}^s p_i^{e_i}
\]

with distinct odd primes (p_i). Over each odd prime power, (u^2=1) has
exactly the two solutions (u=\pm1): the factors (u-1) and (u+1) have gcd
dividing (2), so the full prime power must divide one of them. CRT therefore
gives exactly (2^s) square roots of (1) modulo (N). If (a) is a unit
square and (r_0^2=a), multiplication by (r_0) bijects these roots with the
square roots of (a). Hence (a) also has exactly (2^s) roots.

Nonzero roots occur in pairs (z,-z). Since (N) is odd, exactly one balanced
representative of each pair is positive. Thus each root set has
(2^{s-1}) positive and (2^{s-1}) negative representatives.

For a unit (x\ne1), put (w=\operatorname{rep}(x^{-1})), as in F326.
In the first inverse branch, (x>0,w>0) and (F(x)=w). It is fixed exactly
when (x^2=1\pmod N). There are (2^{s-1}) positive representatives of such
roots, but (x=1) belongs to the special transposition (0\leftrightarrow1).
The first branch therefore has exactly

\[
2^{s-1}-1
\]

unit fixed ranks. Such an (x) is neither (1) nor (-1) modulo (N): the
first is excluded, and the balanced representative of the second is negative.
Its CRT sign vector is consequently mixed. Therefore
(\gcd(x-1,N)) contains some, but not all, prime-power factors of (N), and is
a proper nontrivial divisor.

In the scaled inverse branch, fixedness is equivalent to

\[
x=\operatorname{rep}(a^{-1}w)
\quad\Longleftrightarrow\quad
ax^2=1\pmod N.
\]

It then follows that (w=x^{-1}=ax\pmod N), so (w^2=a\pmod N). The branch
conditions require the balanced representative (w) to be negative.
Conversely, given any negative balanced root (w) of (a), let
(x=\operatorname{rep}(w^{-1})). Then
(\operatorname{rep}(ax)=w<0). If (x<0), writing (x=-y) gives
(\operatorname{rep}(ay)=-w>0), so (x) lies in the negative part of the F326
domain; if (x>0), it lies in its positive part. Thus it is a fixed point of
the scaled branch, and the correspondence is bijective. This gives exactly

\[
2^{s-1}
\]

scaled-branch unit fixed ranks, with decoded square root (w). The remaining
branch sends (x) to (-x) and has no nonzero unit fixed point. Hence the total
number of unit fixed ranks is

\[
(2^{s-1}-1)+2^{s-1}=2^s-1.
\]

Every nonunit fixed rank is represented by a nonzero (x) with
(|x|<N). Therefore (1<\gcd(x,N)<N), so its decoder returns a proper divisor.

## 7. Exact arithmetic success probability

Set (u=2^{s-1}), the number of root-producing fixed ranks. For completeness,
fix any decoded square root (w) of (a), and let the hidden root (r) be
uniform among all (2^s=2u) roots. The CRT signs of (r/w) determine whether
(r) equals (w) or (-w) at each prime-power component. A gcd comparison of
the two roots gives a proper divisor whenever those signs are mixed. It fails
exactly for the two global choices (r=w) and (r=-w). Thus its conditional
success probability is

\[
1-\frac{2}{2^s}=1-\frac1u=1-2^{1-s},
\]

which is the declared P02 probability.

Let (q) now denote the total number of fixed ranks, including nonunits. Of
these, (q-u) return a proper divisor directly, while (u) return a square root
and then succeed with probability (1-1/u). The endpoint is uniform among all
(q) fixed ranks conditional on stopping by the cap. The inner path uses only
(N,a) and matching coins, so it is independent of the hidden (r). Therefore
the conditional factor probability after reaching a fixed endpoint is exactly

\[
\frac{q-u}{q}+\frac{u}{q}\left(1-\frac1u\right)
=1-\frac1q.
\]

Multiplying by the probability of reaching an endpoint by time (T) gives

\[
\Pr(\text{factor by cap }T)
=\left(1-\frac1q\right)(1-S_T).
\]

Neither this calculation nor the lazy traversal requires the algorithm to know
(q) or to enumerate the graph.

## 8. Public history-independent edge screen

Let (B) contain every fixed vertex and both vertices of every nonfixed
(F)-orbit whose public, history-independent screen returns a verified proper
divisor. Then (B) is a union of (F)-orbits. Its size has the form

\[
b=q+2e,
\]

so (b) is odd and (d-b) is even. Put (m_B=(d-b)/2).

On a failure to absorb, the current vertex lies outside (B), and its distinct
(F)-partner also lies outside (B). Removing that pair leaves every vertex of
(B) untouched. Consequently the proof of Sections 3 and 4 applies verbatim
with (b) in place of (q) and (m_B) in place of (m):

\[
S_T^{(B)}
=\prod_{k=0}^{T-1}\frac{d-b-2k}{d-2k},
\qquad
\mathbb E H_B=\frac{d+2}{b+2},
\]

with the same cap conventions, and the absorbing endpoint is uniform on (B)
conditional on absorption by time (T). Thus the (S_T) in claim 6 must be
read as the survival function recomputed with (b), exactly as directed by
“with (b) in place of (q).”

Let (c) be the number of the (u=2^{s-1}) root-producing fixed ranks that
remain root outputs under the stated decoder priority. A rank preempted by the
screen instead returns a verified factor, so (0\le c\le u). Every absorbing
rank outside those (c) ranks returns a factor with certainty. On each of the
(c) ranks, the independent-root comparison fails with probability (1/u).
Uniformity on (B) therefore gives

\[
\Pr(\text{no factor}\mid\text{absorption})
=\frac{c}{b}\frac1u\le\frac1b.
\]

It follows that

\[
\Pr(\text{factor by cap }T)
\ge\left(1-\frac1b\right)(1-S_T^{(B)}).
\]

If the screen does not preempt any root-producing fixed rank, then (c=u), so
the inequality is equality. The proof needs the screen to define a fixed public
set (B), which is precisely what history independence supplies. Membership is
tested locally from the current (F)-edge; neither (b) nor a full enumeration
of (B) is needed by the algorithm.

## Exact comparison with the six claims

| Claim | Result | Exact qualification |
|---|---|---|
| 1 | Verified only under the expected-time reading | Uniform matching law, (O(T)) words, (O(\log d))-bit words, and expected polylogarithmic overhead hold. Fair-bit rejection prevents a deterministic worst-case time bound. |
| 2 | Verified | The hazard, survival product, support convention, CDF, and capped-tail sum all follow exactly. |
| 3 | Verified | The mean is ((d+2)/(q+2)), and the endpoint is uniform for every positive-probability capped stopping event. |
| 4 | Verified | The ratio is nonincreasing for each fixed ((d,q)); adding a fixed nonnegative per-attempt cost preserves this. The proof gives no mixed-input monotonicity. |
| 5 | Verified | The two unit fixed-rank counts, all decoder outcomes, and the exact factor probability follow from F326, CRT, independence, and the declared P02 probability. |
| 6 | Verified | Replace (q,m,S_T) by (b,(d-b)/2,S_T^{(B)}). The lower bound and stated equality condition follow exactly for a public history-independent screen and the stated decoder priority. |

The only substantive wording issue is the missing word “expected” in claim 1's
per-evaluation random-time assertion. No other mathematical gap was found in
the stated scope. No conclusion here concerns structured auxiliary matchings,
history-dependent or cross-edge screens, compressed jumps, or external novelty.
