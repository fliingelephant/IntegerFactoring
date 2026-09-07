# Independent reconstruction: uniform-source count-descent mass

Input: `STATEMENT_ONLY.md`

SHA256 of the input used here:

    75c092beacf63c7dda9681be4fd54ae208d2fc0188586a80e6b2ab3b69d9e6c9

Correction recorded after the first reconstruction pass: the empty color
class at `c=1` and the zero-error induction base require weak inequalities.
The proof below uses those weak inequalities and gives an explicit bound for
both screened children before applying the final `5A^2` estimate.

This proof uses no number-theoretic input beyond the Rosser--Schoenfeld
inequality explicitly allowed in the statement.

## 1. Continued fractions, discrepancy, and parameter mass

Write the Euclidean algorithm and the convergent denominators as

    r_{-1}=N,  r_0=a,
    r_{i-2}=b_i r_{i-1}+r_i,

and

    q_{-1}=0,  q_0=1,
    q_i=b_i q_{i-1}+q_{i-2}.

Thus `r_m=0`, `r_{m-1}=1`, and `q_m=N`. The standard determinant
identities, proved directly by induction, give

    N=q_i r_{i-1}+q_{i-1}r_i,                                      (1)
    q_{i-1}a == (-1)^{i-1}r_{i-1} (mod N).                          (2)

### The three symmetries of `S`

Let `x=[0;b_1,...,b_m]`. If `b_1>=2`, then

    1-x=[0;1,b_1-1,b_2,...,b_m].

If `b_1=1`, then

    1-x=[0;b_2+1,b_3,...,b_m].

The only possible noncanonical terminal digit in the first formula is
normalized by `[...,c,1]=[...,c+1]`. Each operation preserves the sum of
the digits. Hence

    S(N-a,N)=S(a,N).                                                (3)

The determinant identity for the last two convergents says

    a q_{m-1} == (-1)^{m-1} (mod N).

Moreover,

    q_{m-1}/N=[0;b_m,b_{m-1},...,b_1],

after the same sum-preserving normalization if the last displayed digit is
`1`. Thus `S(q_{m-1},N)=S(a,N)`. According to the sign in the congruence,
the inverse of `a` is either `q_{m-1}` or `N-q_{m-1}`. Equation (3) now
gives

    S(a,N)=S(N-a,N)=S(a^{-1} mod N,N).                              (4)

### A block discrepancy lemma

Put `alpha=a/N`, and on the circle put

    f(x)=1  if 0<x<1/2,
         =-1 if 1/2<x<1.

No point `ya/N`, `1<=y<N`, is an endpoint. Hence

    E_a(t)=sum_{y=1}^t f({y alpha}).                                (5)

We need the following elementary continued-fraction estimate.

**Lemma 1.** For each convergent denominator `q_i<N` and every consecutive
block of `q_i` terms of the rotation by `alpha`, the absolute value of the
sum of `f` over that block is at most `10`.

**Proof.** The case `q_i=1` is immediate. Otherwise let `p_i/q_i` be the
corresponding convergent. Then

    |alpha-p_i/q_i| <= 1/(q_i q_{i+1}) <= 1/q_i^2.

Compare a translated block of `q_i` orbit points with the translated grid
of the `q_i` points `k p_i/q_i`. The latter is a permutation of the grid
with spacing `1/q_i`. Every orbit point moves from its paired grid point in
one common circular direction by less than one grid spacing. A membership
change for the half-circle can occur only next to one of its two endpoints.
Allowing endpoint coincidences, at most four paired grid points can change
membership. The grid itself differs from half of `q_i` by at most one
point. Therefore its count in the half-circle differs from `q_i/2` by at
most five after the perturbation. Multiplication by two gives the asserted
bound for the sum of `f`. \(\square\)

Every integer `0<=t<q_m=N` has a greedy Ostrowski expansion

    t=sum_{i=0}^{m-1} c_i q_i,  0<=c_i<=b_{i+1}.                    (6)

This follows inductively from
`q_{i+1}=b_{i+1}q_i+q_{i-1}`. In particular,

    sum_i c_i <= sum_i b_i=S(a,N).                                 (7)

Partition the first `t` terms in (5) into the consecutive blocks prescribed
by (6). Lemma 1 and (7) give

    |E_a(t)| <= 10 S(a,N).                                         (8)

This also covers `t=0`.

### Counting large partial quotients

Fix `B>=1`. If the occurrence `b_i>=B` is present, set

    x=q_{i-1},  y=r_{i-1},  epsilon=(-1)^{i-1}.

By (1),

    Bxy <= q_i r_{i-1} <= N,                                      (9)

and by (2),

    xa == epsilon y (mod N).                                      (10)

For a fixed `a`, the denominators `q_{i-1}` increase strictly, except that
the first two can both equal `1` when `b_1=1`; those two occurrences have
opposite signs. Consequently a fixed triple `(a,x,epsilon)` receives at
most one occurrence.

Fix `x` and one sign, and put `d=gcd(x,N)`. In (10), `y` is a positive
multiple of `d`. There are at most

    floor(N/(Bxd))

such `y` allowed by (9). After division by `d`, (10) fixes `a` modulo
`N/d`, so it has at most `d` lifts modulo `N`, even before the unit
condition is imposed. Thus the number of occurrences with this `x` and
this sign is at most

    d floor(N/(Bxd)) <= N/(Bx).

Summing over both signs and over `1<=x<=floor(N/B)` proves

    sum_{a in U_N} #{i:b_i>=B}
      <= (2N/B) H_floor(N/B).                                      (11)

Every partial quotient is at most `N`. Summing (11) over its level sets
therefore gives

    sum_{a in U_N} S(a,N)
      =sum_{B=1}^N sum_{a in U_N} #{i:b_i>=B}
      <=2N sum_{B=1}^N H_floor(N/B)/B
      <=2N H_N^2.                                                   (12)

The Jacobi symbol is a homomorphism from `U_N` to `{+1,-1}`. Its positive
fiber is all of `U_N` when the character is trivial and has half of
`U_N` otherwise. Hence `|J_N|>=phi(N)/2`, and (12) yields

    E_{a uniform J_N} S(a,N) <= 4N H_N^2/phi(N)=M_N.                (13)

For completeness, if `omega(N)` is the number of distinct prime divisors,
ordering those divisors increasingly and inducting gives

    N/phi(N)=product_{p|N} p/(p-1) <= omega(N)+1.

Indeed the `j`-th distinct prime is at least `j+1`. Also
`2^omega(N)<=N`, while `H_N<=1+ln N`. Therefore

    M_N <=4(1+log_2 N)(1+ln N)^2.                                  (14)

Markov's inequality applied to (13)--(14) shows that the cutoff

    S<=8(1+log_2 N)(1+ln N)^2

retains at least half of `J_N`. All estimates above are pointwise in `N`.

## 2. Fixed-start geometry and balanced cofactors

At any query the two children are

    (t+E_a(t))/2  and  (t-E_a(t))/2.

Start with `t_0=h`. If every queried discrepancy has absolute value at most
`D`, induction gives, for either child at depth `j+1`,

    |t-h/2^{j+1}| <= D(1-2^{-(j+1)}) <D.                           (15)

Thus every positive screened child lies in `W(N,D)`, with scale
`k=j+2`. This proof uses only the discrepancy at the current query, so the
multipliers may vary. Also a common divisor of `h=(N-1)/2` and `N` divides
`N-1`, so `gcd(h,N)=1`.

Now fix an odd `p in [H,2H]`. Suppose that, for `M=2^k`, `k>=2`, and some
positive integer `n`,

    |np-(pq-1)/M| <=D.                                             (16)

Since `n>=1`, (16) and `D<=p/4` imply `q/M>=1-D/p>=3/4`; hence

    M<4H.                                                          (17)

After multiplication by `M`, the integer `Mn-q` is nonzero because `Mn`
is even and `q` is odd. Therefore

    MD >= |p(Mn-q)+1| >=p-1>=H-1,

or

    M >=(H-1)/D.                                                   (18)

The ratio between the endpoints in (17)--(18) is less than `8D`.
Consequently at most

    K(D)=1+floor(log_2(8D))                                        (19)

powers of two can occur.

For one such `M`, (16) implies

    |q-Mn| <=R,  R=(MD+1)/p.

Here `2R<M`, because `D/p<=1/4`, `p>=5`, and `M>=4`. The possible `n`
number at most `H/M+2`, and for each `n` the interval for `q` contains at
most `2MD/p+1` integers. Using (17)--(18),

    (H/M+2)(2MD/p+1)
      =2HD/p+H/M+4MD/p+2
      <2D+(4/3)D+16D+2D
      <32D.                                                        (20)

This bounds all integer `q`, so it also bounds odd `q`. Equations
(17)--(20) prove both the scale assertion and the bound `32D K(D)`.

For `N=pq`, every positive proper nonunit in `W(N,D)` is divisible by `p`
or by `q`. Sum (20) over the `R_H` choices of the named divisor and then
over the two choices of divisor. The number of bad ordered distinct-prime
pairs is at most

    64 R_H D K(D).                                                 (21)

### The asymmetric interval

Write `q=Ms+r`, where `0<r<M`; this holds because `q` is odd and `M` is
even. The center of the asymmetric interval is

    (pq-1)/M=ps+(pr-1)/M,

strictly between `ps` and `p(s+1)`. If any positive `p`-multiple is in the
interval, then one of these two nearest multiples is in it. The lower one
is positive exactly when `q>=M`, and it lies above the lower endpoint
exactly when

    pr-1<=MD.

The upper one lies below the upper endpoint exactly when

    p(M-r)+1<=MD/2,

or

    2p(M-r)+2<=MD.

These are precisely the two asserted conditions, and either condition is
plainly sufficient.

## 3. Uniform sources and all rare events

Assume first that the start is `h` and that `W(N,D)` contains no proper
nonunit. By (15), an attempt whose queried discrepancies all have absolute
value at most `D` cannot return a factor: the initial value is coprime to
`N`, and every later positive screened value is a unit. Hence success with
one retained multiplier implies

    S(a,N)>D/10

by (8). Markov's inequality and (13) give

    P(success) <=10M_N/D.                                         (22)

No attempt has been conditioned away in this argument; in particular,
all large-defect attempts are exactly the event used on the right side.

With fresh independent uniform multipliers, condition on the complete past
at each query. At most `L_N` conditional Markov bounds, followed by a union
bound, give

    P(success) <=10L_N M_N/D.                                     (23)

### Counting exceptional variable starts

Fix `v` equal to `p` or `q`, and let `T` be uniform on `{1,...,h}`. If the
window around `T/2^j` contains a positive multiple of `v`, then

    2^j <=h/(v-D).

It is therefore enough to consider `1<=j<=ell_v`.

For such a `j`, put `s=2^jv` and `R=2^jD`. Since `D<v/2`, the intervals
of radius `R` around the positive multiples of `s` are disjoint. The
multiples with center at most `h` contribute at most

    floor(h/s)(2R+1)

integers `T`; at most one next interval meets `{1,...,h}`, and it contributes
at most `R` integers. Thus

    P(exists n>=1: |T/2^j-nv|<=D)
      <=2D/v+1/(2^jv)+2^jD/h.                                     (24)

Summing (24), using `D>=1`, and using
`2^ell_v<=h/(v-D)` when `ell_v>0`, gives

    sum_{j=1}^{ell_v} P(window event at j)
      < D(2ell_v+5)/v.                                             (25)

The event `v|T` has probability at most `1/v<=D/v`. Thus, also when
`ell_v=0`,

    P(T or one of its windows contains a positive v-multiple)
      <=D(4ell_v+9)/v.                                             (26)

A union bound over `v=p,q` proves the bound `V(N,D)`.

For a descent starting at `T`, the same induction as (15) says that every
positive descendant at depth `j` is in

    [T/2^j-D,T/2^j+D].                                             (27)

If neither the large-parameter event nor the exceptional-start event in
(26) occurs, no screened positive integer has a nontrivial gcd with `pq`.
The union bound uses only the two marginal laws. It does not use
independence. Therefore

    P(success) <=10M_N/D+V(N,D).                                  (28)

Now let

    T=min(a^{-1} mod N,N-a^{-1} mod N),  a uniform in J_N.

Inversion permutes `J_N`. Folding a residue together with its negative has
at most two preimages, while `|J_N|>=phi(N)/2`. Hence, for every
`A subseteq {1,...,h}`,

    P(T in A) <= 2|A|/|J_N| <=4|A|/phi(N)
              =(4h/phi(N)) P(T_uniform in A).                     (29)

Using (29) for the exceptional set counted above changes (28) to

    P(success) <=10M_N/D+(4h/phi(N))V(N,D).                        (30)

If fresh multipliers are conditionally uniform in `J_N` given the complete
past, the conditional form of (13) applies at every query. Thus (28) and
(30) remain valid with their first term replaced by
`10L_NM_N/D`. The stated marginal law of the start is all that is needed
for its rare-event term.

### Cost of rejection generation

In one raw draw from `{1,...,N-1}`, the number of nonunits is

    (N-1)-phi(N)=p+q-2.

Ignore Jacobi-negative unit draws, which merely restart the sampler. Among
the two decisive outcomes, namely a nonunit and an accepted member of
`J_N`, the chance that the nonunit appears first is at most

    (p+q-2)/|J_N|
      <=2(p+q-2)/((p-1)(q-1))
      =2/(p-1)+2/(q-1)
      <=4/(H-1).                                                    (31)

This is the entire extra factor probability created while generating one
uniform multiplier. A union bound over at most `L_N` generated multipliers
adds `4L_N/(H-1)`. With one retained generated multiplier it adds only
`4/(H-1)`.

### Asymptotics and the infinite fixed-start family

Take `D=floor(sqrt(H))`. For sufficiently large `H`, all hypotheses on
`D` hold. On a balanced semiprime,

    N/phi(N)=pq/((p-1)(q-1))=O(1),

so `M_N=O((log N)^2)` and `L_N=O(log N)`. Also
`ell_p,ell_q=O(log N)`, whence

    V(N,D)=O(log N/sqrt(H)),  4h/phi(N)=O(1).

The generation term is `O(log N/H)`. Therefore every variable-start bound
listed in the statement, including the fresh-multiplier versions, is

    O((log N)^3/sqrt(H)).                                          (32)

Let `R_H=pi(2H)-pi(H)`. The allowed Rosser--Schoenfeld inequality gives

    R_H>3H/(5 ln H),  H>=21.

Since `D K(D)=O(sqrt(H) log H)`, for every sufficiently large `H`,

    R_H-1>64D K(D).

There are `R_H(R_H-1)` ordered distinct-prime pairs, whereas (21) bounds
the bad ones by `64R_HD K(D)`. Hence a good pair exists for every
sufficiently large `H`. Taking an unbounded sequence of such `H` gives
infinitely many balanced distinct-prime inputs for which the fixed-start
bounds, including their fresh-source version, satisfy (32).

If the success probability of one of these exact attempts is `rho>0`,
independent repetition takes mean `1/rho` attempts. Equation (32) makes
this at least `sqrt(H)/poly(log N)`. If `rho=0`, repetition never succeeds.
This conclusion concerns only the source, starts, queries, screens, and
retry policy stated in the input.

## 4. The small-multiplier obstruction

For `A=min(a,N-a)`, multiplication by `N-A` swaps the lower and upper
halves of every nonzero residue. Therefore

    Q_{N-A}(t)=t-Q_A(t),                                           (33)

so the unordered children, the selected minima, and all later unordered
queries agree for `a` and `A`.

It remains to prove the obstruction for `1<=A<=h`. If `N` is prime, the
claim is immediate. If `A=1`, then `Q_A(h)=h`, one child is zero, and the
initial `h` is coprime to `N`; the attempt fails. Assume henceforth that
`N` is composite and `A>=2`. Let `P` be the least prime divisor. The
hypothesis gives

    N>=P^2>25A^4.                                                   (34)

Set

    lambda=N/(2A),  n_c=floor(c lambda),  0<=c<=A.

None of the numbers `c lambda`, `1<=c<=A`, is an integer: coprimality would
force `A|c`, and `c=A` would then force the odd number `N` to be even.
In particular `n_A=h`.

The block `n_c<y<=n_{c+1}` has
`floor(2Ay/N)=c`. It belongs to the lower residue half exactly when `c` is
even. At the boundary `n_c`, summing the even and odd block lengths gives

    |Q_A(n_c)-ceil(c/2)lambda| <=ceil(c/2),
    |n_c-Q_A(n_c)-floor(c/2)lambda| <=floor(c/2).                   (35)

Indeed every selected block length differs from `lambda` by less than one.
After replacing the two real centers by `n_ceil(c/2)` and
`n_floor(c/2)`, respectively, the right sides in (35) increase by less
than one.

Suppose a queried value `t` satisfies `|t-n_c|<=e`. Counts of either color
change by at most `e` when the endpoint moves. Since replacing `d lambda`
by `n_d` costs strictly less than one, its two children lie within

    e+ceil(c/2)+1  and  e+floor(c/2)+1                             (36)

of the corresponding two boundary centers.

Here is the full simultaneous induction, including the ordering of the two
centers. Starting with `c_0=A`, put

    c_{j+1}=floor(c_j/2),
    e_j=sum_{r=1}^j(c_r+1),  e_0=0.

We claim that every selected query value that is reached satisfies

    |t_j-n_{c_j}| <=e_j.                                           (37)

The claim is exact at `j=0`, because `t_0=h=n_A`. Since
`c_{r-1}-c_r>=c_r`,

    sum_{r=1}^j c_r <=A-c_j,

and hence

    e_j <=A-c_j+j.                                                  (38)

Suppose `c_j>=1` and (37) holds. If `c_j=2m+1`, (36) and
`n_{m+1}-n_m>=lambda-1` show that the child centered at `n_{m+1}` minus
the child centered at `n_m` is at least

    lambda-2e_j-2m-4.

By (34), `lambda>(25/2)A^3`. Also (38), `j<=log_2 A<=A-1`, and
`2m<=A` make the last display positive. Thus the child centered at `n_m`
is indeed the smaller child. If `c_j` is even, both children have the same
center. In both cases the selected child has, by (36), error strictly less
than

    e_j+c_{j+1}+1=e_{j+1}.

This proves (37) at the next reached query.

The same calculation bounds both screened children, including the larger
one. For either child, (36), (38), and `j+1<=A` give

    error < e_j+ceil(c_j/2)+1
          <= A-c_j+j+ceil(c_j/2)+1
          <= 2A-c_j+ceil(c_j/2)
          <= 2A.                                                    (39)

While `c_j>=1`, (38) also gives `e_j<2A`. Once `c_j=0`, (37) gives
`t_j<=2A`; by (34), `At_j<h`, so `Q_A(t_j)=t_j` and the other child is
zero. The attempt stops.

It follows that every positive integer `x` screened during the attempt has
some `0<=d<=A` for which

    |2Ax-dN| <4A^2+2A <=5A^2.                                     (40)

The integer on the left of (40) is nonzero. Otherwise `N|2Ax`, and oddness
of `N` together with `gcd(A,N)=1` would give `N|x`, impossible because
`0<x<N`. If `x` had a nontrivial gcd with `N`, some prime divisor at least
`P` would divide this nonzero integer of magnitude less than `5A^2<P`, a
contradiction. Thus every positive screen is a unit, and the eventual zero
child makes the literal attempt fail. This proves the final assertion with
no source assumption.

No unresolved gap or counterexample was found.
