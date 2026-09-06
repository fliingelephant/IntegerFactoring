# F263-D02 V2 algebra — block transfers for the beta-two binomial gate

## 1. Exact promised gate and both parities

Assume

\[
N=pq,\qquad p<q<2p,
\]

where `p` and `q` are distinct odd primes.  Put

\[
B=\lfloor\sqrt N\rfloor,\qquad H=\lfloor B/2\rfloor,
\qquad s=B-p.
\]

The balanced inequalities give

\[
0\le s<H<p<q,\qquad B<q,\qquad B<2p.
\tag{1}
\]

Let

\[
a_k=\binom{2k}{k}.
\]

Its exact first-order recurrence is

\[
(k+1)a_{k+1}=2(2k+1)a_k.
\tag{2}
\]

For `0 <= k < H`, every denominator `k+1` is below `p` and is a unit
modulo `N`.  The odd factors `2k+1` lie below `q` and below `2p`.
Equation (1) implies that the unique numerator factor divisible by a hidden
prime is

\[
2k+1=p,\qquad k=(p-1)/2.
\tag{3}
\]

For even `B=2H`, `p` cannot equal the even integer `B`, so `s>=1` and
`p<=2H-1`.  For odd `B=2H+1`, `s<H` gives `p>=H+2` and `p<=2H+1`;
on the unresolved branch `p!=B`, one again has `p<=2H-1`.  Thus (3) lies
inside `0,...,H-1` after the public `gcd(B,N)` screen.  No numerator is
divisible by `q`.  Therefore

\[
\gcd(a_H,N)=p.
\tag{4}
\]

Both parities are explicit.  If `B=2H`, then

\[
\binom BH=a_H.
\tag{5}
\]

If `B=2H+1`, then

\[
\binom BH={2H+1\over H+1}a_H.
\tag{6}
\]

Here `H+1<p`, so the denominator in (6) is a unit.  Its numerator is
`B<q` and can be a nonunit only when `B=p`, which the public screen already
detects.  Hence the multiplier in (6) is a public unit on the unresolved
branch.  Equations (4)--(6) are exactly the F249/P215 central-binomial gate.

The shifted recurrence is retained as a second orientation control.  For

\[
C_c=\binom{N+c-1}{B},\qquad 1\le c\le H,
\]

one has

\[
(N+c-B)C_{c+1}=(N+c)C_c.
\tag{7}
\]

Every numerator in (7) is a unit modulo `N`.  When `s>=1`, the unique
nonunit denominator is at `c=s`, since

\[
\gcd(N,N+c-B)=\gcd(N,B-c)
=\begin{cases}p,&c=s,\\1,&c\ne s.\end{cases}
\tag{8}
\]

When `s=0`, the singular edge is `c=0` and `gcd(B,N)=p` already exits.

## 2. Generic affine block state

The symbolic search works first with two generic affine factors

\[
u_k=\alpha k+\beta,\qquad v_k=\gamma k+\delta.
\]

For a half-open block `I=[l,l+m)`, define the two interval polynomials

\[
U_I(X)=\prod_{k\in I}(u_k+X),\qquad
V_I(X)=\prod_{k\in I}(v_k+X).
\]

Write `U_{I,j}=[X^j]U_I(X)` and `V_{I,j}=[X^j]V_I(X)` for
`j=0,1,2`.  These coefficients require no division, even when one affine
factor is a zero divisor.  For adjacent blocks `I=L dot-union R`, the
truncated jet obeys

\[
U_{I,j}=\sum_{h=0}^j U_{L,h}U_{R,j-h},\qquad
V_{I,j}=\sum_{h=0}^j V_{L,h}V_{R,j-h}.
\tag{9}
\]

The search also uses upper-triangular transfer matrices

\[
T_k(w)=
\begin{pmatrix}u_k&w_k\\0&v_k\end{pmatrix}.
\]

For three frozen public weights, `w_k=1`, `w_k=k+1`, and a fixed public
hash of `k`, it records products in both orders.  Matrix multiplication gives

\[
T_I=T_LT_R,
\qquad
(T_I)_{01}=(T_L)_{00}(T_R)_{01}+(T_L)_{01}(T_R)_{11}.
\tag{10}
\]

Equations (9) and (10) are positive controls.  They do not evaluate a root
block quickly.  A balanced binary tree has logarithmic depth but still has
`m` leaves and `m-1` internal merges.

For exact small synthetic blocks, the program also records the reduced pair

\[
\widehat U_I=U_{I,0}/g_I,\qquad
\widehat V_I=V_{I,0}/g_I,\qquad
g_I=\gcd(U_{I,0},V_{I,0}).
\tag{11}
\]

This is a control for exact cancellation.  Constructing (11) by first
forming both products touches the full block and is not a shortcut.

## 3. Adjacent-block and dyadic recurrence controls

For one affine product

\[
P(l,m)=\prod_{j=0}^{m-1}(\alpha(l+j)+\beta),
\]

the exact adjacent-shift recurrence is

\[
(\alpha l+\beta)P(l+1,m)
=(\alpha(l+m)+\beta)P(l,m).
\tag{12}
\]

The recurrence miner must rediscover (12) for the central numerator
`(alpha,beta)=(4,2)`, the central denominator `(1,1)`, and the two literal
generic shifted fixtures `(1,1009)` and `(1,989)`.  The last two fixtures
authenticate the two unit-slope affine orientations without inserting a
labelled semiprime into symbolic discovery.  Equation (12) then applies to
the numerical shifted factors `(1,N)` and `(1,N-B)`.  This is a control.  It moves a block
only after one full block value is available.  Constructing that initial
value costs `m` factor evaluations, and walking a characteristic-size
interval costs characteristic-size work.

Separately, the program searches for fixed low-order polynomial-coefficient
recurrences in the dyadic-length sequence `P(l,2^j)`.  The discovery matrix
contains both `(4,2)` and `(1,1)` affine families.  It is built independently
modulo `1000000007` and `1000000009`.  Every rescaled basis candidate from
either nullspace must vanish in both modular matrices and on disjoint exact
held-back starts in both affine families.  A dyadic recurrence is operational
only when the coefficient of its highest shift is the literal constant
`+1` or `-1`; otherwise solving it needs an uncertified inverse and it stays
`oracle_block`.  An identity at finitely many indices is not an asymptotic
evaluator.

## 4. Frozen nonlinear observables

For the two quadratic jets

\[
U_{I,0}+U_{I,1}X+U_{I,2}X^2,
\qquad
V_{I,0}+V_{I,1}X+V_{I,2}X^2,
\]

the program forms all `2 x 2` jet minors and their `4 x 4` Sylvester
resultant.  It also forms differences across adjacent shifts, determinants
between adjacent block states, and the first two determinantal divisors of
the resulting public `2 x d` matrices.  Every determinant is evaluated
division-free over `Z/NZ`.  A Smith-style divisor is implemented only as a
gcd of `N` with a public list of entries or minors; no Smith decomposition
over a hidden field is used.

For fixed public seeds, a block vector `x_I` is compressed by

\[
h_\sigma(I)=\sum_j \lambda_{\sigma,j}(N,I)x_{I,j}\pmod N
\tag{13}
\]

and by the product hash

\[
g_\sigma(I)=\prod_j(1+\lambda_{\sigma,j}(N,I)x_{I,j})\pmod N.
\tag{14}
\]

All weights are derived from `N`, the public block coordinates, the syntax,
and the frozen seed.  They do not use `p`, `q`, or a local residue.  These
hashes can discover cancellation patterns, but their construction cost is
the construction cost of `x_I`.

## 5. Operational cost classification

Every expression carries one of these exact dependency classes.

1. `descriptor`: uses only block endpoints, length, `N`, and a fixed number
   of ring operations.
2. `short_scan`: scans at most `n^2` factors in each of a polynomial number
   of publicly chosen blocks.  This is polynomial in the input bit length.
3. `recursive_merge`: composes child states whose complete dependency cone
   has all leaves of the target block.  Its depth may be logarithmic, but its
   work and state construction are `Theta(m)`.
4. `oracle_block`: assumes a remote block value without an evaluator.
5. `full_scan`: explicitly touches `Theta(H)` recurrence factors.

Only classes 1 and 2 are operational candidates.  V2 stores, for every
symbolic column, its class, whether it is a parent target, its exact source
node count on that synthetic instance, and its named dependency-DAG nodes.
A mined identity is a candidate shortcut only when exactly one parent target
occurs, its coefficient is `+1` or `-1`, every remaining node is
`descriptor` or `short_scan`, and the sum of their expanded source-node
costs does not overflow.  The grammar has at most 70 terms.  Each
`short_scan` node costs at most `n^2`; thus an accepted DAG is polynomial and
hence numerical-QP.  A merge identity whose children recursively expand to
all leaves is tagged `recursive_merge` and cannot pass this test.

The five non-operational controls are explicit output records.  For a domain
of length `D` and singular index `z`, V2 records these exact counts:

```text
full root product:              D factor evaluations;
full product-tree preprocessing:D leaves, D-1 merges, 2D-1 state words;
oracle child search:            one oracle call per selected tree edge;
recomputed child search:        sum of the selected child lengths;
full shifted root product:      H-1 factor evaluations.
```

The oracle and recomputation counts follow the literal floor/ceiling binary
split containing `z`; they are not asymptotic estimates.  The recomputation
sum is less than `2D` but is still characteristic-size work.  Logarithmically
many gcd calls do not change that fact.

## 6. Evidence boundary

The hidden factors are never inputs to a syntax, block, projection, identity,
recurrence, canonicalization, or candidate order.  The query bank uses
`n=bitlength(N)` computed from the public modulus.  Public block evaluation
finishes before labels classify coverage or direct inclusion.  Labelled
factors are used only to verify a gcd, identify the true singular index,
classify whether a hit's recorded public support contains that index, measure
query coverage, and name hostile common-capacity cohorts.

Finite identities are accepted only after exact evaluation on disjoint
public synthetic inputs.  Finite semiprime rates are heuristic guidance.
They do not prove a numerical-quasipolynomial evaluator, an inverse-QP
success law, or an all-input factoring algorithm.
