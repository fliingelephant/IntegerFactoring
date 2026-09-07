# Rectangle counts from shifted binomial carries

**Family:** route:F31

**Status:** root-derived exact bridge, independently reconstructed from the
statement alone and checked by the root. No fast carry-sum algorithm is
supplied.

The next target can be a single modular statistic rather than every high
mixed moment or an ordinary Cauchy kernel. Four evaluations of a shifted
binomial-carry sum modulo M give an exact original rectangle count.

## Definition and derivation

Let M=2^k, k>=2, and N be any positive odd integer. Let u range over the
canonical odd units and put v=N/u mod M in [0,M). For cuts c,d in [0,M],
use the shifted representatives

    x_c=u+M*1_(u<c), y_d=v+M*1_(v<d),
    q_cd=(x_c*y_d-N)/M,
    B(c,d)=sum_u binom(q_cd,2) mod M.

Here binom(q,2)=q(q-1)/2 is an integer even for negative q. This retains
the full input N. The shifted x and y sets are the odd representatives in
[c,c+M) and [d,d+M), respectively. The shifts change the lifts, not the
original graph or the tested windows.

For a rectangle [a,b) times [c,d), take the mixed difference of B at its
four corners. A point contributes zero unless both u and v lie in the
respective intervals. At a point in both intervals, put
q=(uv-N)/M. The four carries are q, q+v, q+u, and q+u+v+M. Their
binomial mixed difference is

    uv + M(q+u+v) + (M^2-M)/2
      = N + M(2q+u+v) + (M^2-M)/2
      = N-M/2 mod M.                                  (1)

The cuts at the lower rectangle corners can already have shifted a point
outside its tested intervals, but such a point has zero mixed difference.
For a point inside both intervals the lower lifts are the canonical u,v,
so the four carries above apply directly. This includes empty intervals
and cuts at 0 or M.

Consequently

    C([a,b),[c,d)) = (N-M/2)^(-1)
       * [B(b,d)-B(a,d)-B(b,c)+B(a,c)] mod M.           (2)

The multiplier is odd, and the count lies in [0,M/2], so its canonical
residue is the exact nonnegative count. No Archimedean approximation or
enumeration is needed by this reduction; enumeration in the pilot is only
the reference implementation of the still-missing B oracle.

The correction -M/2 in (1) cannot be dropped. Also, shifted carry-square
sums need not be even. Computing B from sum(q^2)-sum(q) requires both
numerators modulo 2M before exact division by two. A datum
sum(q^2)/2 mod M is not defined for every shifted domain.

## End-to-end scope

P237 supplies O(n^2) public rectangle-emptiness calls for complete
all-input factoring. Inclusive integer intervals [A,B] are passed to (2)
as [A,B+1). Four correct B residues therefore replace each Empty call.
All coordinates have O(n) bits. A uniform deterministic or Las Vegas B
evaluator of expected cost T(n) gives expected total cost
O(n^2 T(n)+poly(n)); fresh randomness and the deterministic call bound
give the conditional expectation bound also for adaptive calls. Small
constant inputs are handled directly as in P237.

This is a sharper sufficient operation than a complete ordinary resolvent
evaluator, but remains conditional. It does not establish that the B
statistic is computationally easier than counting. Indeed (2) shows that
its dependence on both shifted domains already contains every rectangle.

## Relation to the current mechanisms

Reader searches for "binomial carry" and "fundamental domain" found no
matching catalog entries. The closest records are P237's actual-input rectangle interface and
P238/C264's unshifted modular moment and quadratic-carry constructions.
F302 preserves a selected half-count in its signed lift. The present
operation retains arbitrary original windows by changing fundamental-domain
lifts and taking mixed differences. It uses only one binomial statistic
modulo M, including when the carry-square sum is odd. It does not infer a
fast shifted evaluator from P238's unshifted two-digit moment theorem.

F305's new floor transport is a possible construction path for this B
statistic. Its computable marginal terms must be distinguished from its
unresolved carry-weighted floor transform. The direct identity (1) does
not use that transport or any external result. No novelty claim is made.

## Evidence

STATEMENT_ONLY.md gives the exact independent reconstruction input, without
this derivation. The pilot passed 1,200 general rectangle checks through
M=2048, including zero and full endpoints and large full N with negative
carries. It passed 175 public factor-rectangle checks. Its enumerated B
oracle also completed 21 inputs through the existing P237 reference
reduction, using 620 B calls and matching independent trial factorization.

For N=289, M=32, and the singleton factor rectangle [17,18)^2, the four
B residues at (17,17), (17,18), (18,17), (18,18) are 8,16,16,9. Their
mixed difference is 17 modulo 32. Multiplication by (N-M/2)^(-1) gives
the correct count 1; incorrectly using N^(-1) gives 17. At the shifted
domain c=2,d=0 the carry-square sum is 1073, so it cannot be divided by two
as an integer. These are exact guards, not numerical conditioning tests.

The run took 0.246 seconds and used 22,331,392 bytes peak RSS under a 30-second
alarm. Source, output, log, timeout status and preflight are retained.

Independent input SHA-256:
463bec85607b7bbaac1dcdb04c79b4210041285288c2b79603d2dbaade827e2a.
Reconstruction SHA-256:
36851132bf7d7ce095fac6979f36482c47b3ddc41645c909c1eb9b2e8444f187.
The independent argument additionally makes explicit that each summand
needs q modulo 2M, equivalently its original numerator modulo 2M^2.

The reference enumerates graph points. Its successful execution is not
evidence for a quasipolynomial B evaluator. The concrete remaining problem
is to evaluate B(c,d) modulo M with a proved total cost in the bit length,
while retaining both cut coordinates.
