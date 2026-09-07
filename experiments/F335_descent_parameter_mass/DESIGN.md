# Count-descent parameter mass

**Family:** route:F31

Status: author-derived analysis and bounded exact checks. No external novelty
claim. This packet extends F330's dyadic-menu observation by counting useful
parameter mass, rather than proving the window recurrence again.

## Question

For the literal policy which starts at `h=(N-1)/2`, screens `t,Q_a(t),t-Q_a(t)`,
and continues at their smaller positive child, can uniformly sampled
Jacobi-positive multipliers have enough useful mass? Does an inverse or uniform
start change the answer? Which deliberately large-continued-fraction inputs
escape the fixed-window argument?

The root independently studies other count sources. F334 supplies the actual
descent comparison. This packet does not repeat that pilot or change it.

## Bounded Sol checks

Run only after F334 releases the single local numerical slot. Use one named
Python source, a resource preflight, a timeout of 30 seconds, a log, a JSON
output, and hashes. Estimated peak memory below 100 MB. Start with odd N<=51;
then use odd N<=301 if the pilot is comfortably within budget. Store aggregate
counts and the first failed witness, not every successful tuple. No factors
may guide an operational descent; trial division is permitted only as an
offline label and exact check.

1. For every unit 1<=a<N, calculate the canonical finite continued fraction
   `[0;b1,...,bm]`, final term at least two, and S=sum(bi). Check
   `S(a,N)=S(N-a,N)=S(a^(-1) mod N,N)`.
2. Retain the Euclidean digit triples `(b,q,r)` with convergent denominator q
   immediately before that digit and positive remainder
   `r=abs(a*q-N*p)`. Check `b*q*r<=N`; the signed congruence must hold. For
   every B<=N, count all digit occurrences with b>=B and verify the stronger
   elementary bound `count<=2*N*H_floor(N/B)/B` using rational arithmetic.
   Check `sum_a S(a,N)<=2*N*H_N^2`, and check every prefix discrepancy
   `abs(2*Q_a(t)-t)<=10*S` for 0<=t<N.
3. For each small N and each A<=min((N-1)/2,12) coprime to N, run the literal
   fixed-h count descent using exact direct prefix counts. At each query put
   `k=floor(A*t/N)`, `r=A*t-k*N`, `I=1 if r<=h else 0`, and
   `e=2*A*Q-I*2*A*t-c*N`, where the exact integer c is `-k` when I=1 and
   `k+1` when I=0. Thus subtract `c*N`, not a centered representative.
   Check `abs(e)<=2*A*(k+1)` and `k_next<=floor(k/2)` on continuations.
   Starting R=-A, assign child residuals `R_q=I*R+e` and
   `R_other=(1-I)*R-e`; check their congruences to `2*A*child mod N`.
   Every positive screened child has `0<abs(R_child)<=5*A*A`, including
   zero/full-count terminal queries. Check that no factor is returned if the
   offline least prime divisor exceeds `5*A*A`. Also check that a=N-A has
   exactly the same unordered child counts and descended t sequence.
4. For H in {16,32,64,128}, enumerate primes p,q in [H,2H], allowing p=q as a
   control. For D in {1,2,4,8} with D<H/2, enumerate the direct asymmetric
   menu `[ (N-1)/2^k-D, (N-1)/2^k+D/2 ]` for k>=2 and positive integers.
   Stop k when its upper endpoint is below H. Let r=q mod 2^k. A p-multiple
   is eligible exactly if either (i) q>=2^k and p*r-1<=2^k*D, or (ii)
   `2*p*(2^k-r)+2<=2^k*D`. Verify this against direct menu gcds. Retain the
   number of prime pairs with any factor-bearing menu, and maximal eligible
   integer cofactor counts per fixed p (enumerating all integer q in [H,2H]).

The checks test formulas and finite counts. They do not establish an
asymptotic success law. Do not run larger numerical searches without a new
mathematical question.
