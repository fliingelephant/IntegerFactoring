# Proof of the F231 smooth-word zero-defect candidate

## 1. Imported zero-defect identities

The F230 zero-defect classification gives `N=BH+1`.  The identity

\[
N-1=q(p-1)+(q-1)
\]

implies

\[
\gcd(N-1,p-1)=\gcd(p-1,q-1).
\]

Division by the power of two `B` does not change a gcd with the odd number
`P`.  Taking odd parts therefore gives

\[
\gcd(H,P)=D.
\]

The symmetric argument gives `gcd(H,Q)=D`.  Dividing `P` and `Q` by their
full gcd gives `gcd(s_p,s_q)=1`.  In particular, `D|H`, so every maintained
`M|D` also divides every exponent `WH`.

## 2. Return kernels for an arbitrary factored word

The two unit groups modulo `p` and `q` are cyclic of orders

\[
p-1=2^{e_p}P,
\qquad q-1=2^{e_q}Q,
\]

where `e_p,e_q<n`.  Raising a uniform unit to `2^n` kills the two-primary
coordinates and acts as an automorphism on the odd-primary coordinates.
Thus the two CRT coordinates of `a` are independent and uniform in cyclic
groups of orders `P` and `Q`.

We claim

\[
\gcd(WH,P)=D\gcd(W,s_p)={P\over r_p(W)}.
\tag{P1}
\]

Check one odd prime `ell`.  Write

\[
v_\ell(P)=d+e,
\qquad d=v_\ell(D),
\qquad e=v_\ell(s_p).
\]

If `e>0`, `gcd(H,P)=D` forces `v_ell(H)=d`; hence the valuation on the
left of (P1) is `d+min(v_ell(W),e)`.  If `e=0`, the left side is already
saturated at `d`.  This proves (P1) prime by prime.  The proof for `Q` is
identical.

Because `r_p|s_p`, `r_q|s_q`, and `gcd(s_p,s_q)=1`, the two residuals are
coprime.

In a cyclic group of order `P`, the equation `z^(WH)=1` has exactly
`gcd(WH,P)=P/r_p` solutions.  Division by `P` proves the first formula in
(6); the second and their independence follow in the same way.

## 3. Exact classification of no-progress samples

Let

\[
o_p=\operatorname{ord}_p(a),
\qquad o_q=\operatorname{ord}_q(a).
\]

If exactly one of `o_p,o_q` divides `A=WH`, the initial gcd is a proper
factor.  If neither divides `A`, neither order can divide any punctured
divisor of `A`, so the declared decoder makes no progress.

Suppose both orders divide `A`.  The initial gcd is `N`.  Complete
factor-first stripping has the following exact behavior.  At a prime
`ell`, remove redundant copies of `ell` from the exponent until the next
removal would cross at least one local order valuation.  If the two local
valuations differ, that removal gives a proper gcd.  If they agree, it
certifies their common valuation.  Processing every prime therefore gives
a factor unless `o_p=o_q`; in the equal case it returns their exact common
order.

Consequently, a global return is stale exactly when

\[
o_p=o_q=d
\quad\hbox{for some }d\mid M.
\tag{P2}
\]

A cyclic group has exactly `phi(d)` elements of exact order `d` for every
`d` dividing its order.  Since `M|D|P,Q`, the events in (P2) have total
unconditional probability

\[
P_{\rm stale}={1\over PQ}\sum_{d\mid M}\varphi(d)^2.
\tag{P3}

The probability that neither coordinate returns is

\[
\left(1-{1\over r_p}\right)
\left(1-{1\over r_q}\right).
\tag{P4}
\]

The no-progress events (P2) and (P4) are disjoint and exhaustive.  Subtracting
them from one proves (7).

The standard identity

\[
\sum_{d\mid M}\varphi(d)=M
\]

and nonnegativity give

\[
\sum_{d\mid M}\varphi(d)^2
\le\left(\sum_{d\mid M}\varphi(d)\right)^2=M^2.
\]

Using `PQ=D^2s_ps_q` proves (8).

If `r_p,r_q>1`, both are odd and therefore at least three.  Assume without
loss that `r_p<=r_q`.  The direct-factor probability is

\[
{1\over r_p}+{1\over r_q}-{2\over r_pr_q}
={1\over r_p}+{r_p-2\over r_pr_q}
\ge {1\over r_p},
\]

which proves (9).

## 4. The saturating smooth word

Let `Lambda_Y=lcm(1,...,Y)` and `U_Y=Lambda_Y^n`.  For every prime
`ell<=Y`, the valuation of `U_Y` is at least `n`.  Every prime-power
valuation in an integer below `N` is less than `n`.  Therefore every
`Y`-smooth integer below `N` divides `U_Y`, including arbitrary powers of
its small primes.  This proves the equivalence in (11) and the exact
factorizations in (21).

First exclude the equal-residual edge.  If `s_p=s_q=1`, then `P=Q=D`.
Write

\[
p=2^eD+1,
\qquad q=2^fD+1,
\]

with `e,f>=1`.  Since `p<q`, one has `f>e`.  Since `q<2p`, one cannot have
`f>=e+2`; hence `f=e+1`.  Direct expansion gives

\[
N-1=2^eD\left(2^{e+1}D+3\right).
\tag{P5}
\]

The parenthesized factor is odd, so `v_2(N-1)=e`.  On the other hand,

\[
N>2^{2e+1}D^2\ge2^{2e+1}.
\]

Therefore `n=ceil(log_2(N+1))>=2e+2`, so
`floor(n/2)>=e+1`.  This contradicts
`B=2^floor(n/2)|N-1`.  Thus `s_ps_q>1`, proving (12).

Now assume `r_p=1`; the other orientation is symmetric.  The `p` coordinate
returns for every sample, so the union of the two local-return events has
probability one.  Formula (7) reduces to

\[
\Pr(\text{factor or growth})=1-P_{\rm stale}.
\tag{P6}
\]

If `s_ps_q>1`, it is an odd integer and is at least three.  Since `M<=D`,
(8) and (P6) give (13).  This remains true at `M=D`; a nonstale sample must
then be a factor because no larger common block exists.

Before `M=D`, each nonfactor useful event strictly enlarges the divisor
`M|D`, so there are at most `log_2 D` such events.  Since
`D<p<sqrt(N)<2^(n/2)`, these growth events together with the final factor
number fewer than `n`.  Each fresh stage has
conditional useful probability at least `2/3`.  Summing the geometric
waiting times gives at most `3n/2` expected stages through the final factor,
and also gives almost-sure termination on this favorable branch.

Fresh unit samples make the conditional bound valid after every earlier
history; no independence between stages is needed.  A beta-two residue
modulo `2^t` combines with the updated certificate `p=1 mod M` modulo the
lcm in (14).  Reaching `L>=J` invokes the P197 known-residue terminal and
can only stop earlier.  No terminal-capacity assumption is needed because
the smooth-word stages otherwise continue through `M=D` until a factor.

For the integer-enriched word, the supplied factorization of `H` lists every
prime in `rad(H)`.  Giving each listed prime exponent `n` absorbs its entire
primary part in any integer below `N`.  Combining this list with the smooth
list proves (15)--(16).  Its logarithmic height is

\[
n\log_2\operatorname{rad}(H)\le n\log_2H=O(n^2),
\]

so the enrichment does not change the numerical-QP cost.

## 5. Bit cost and word aggregation

The factored form of `Lambda_Y` is obtained by a sieve through `Y`.  Since
`Lambda_Y|Y!`, inequality (17) follows.  Numerical-QP functions are closed
under multiplication by `n`, `Y`, and `log Y`, after enlarging their fixed
envelope.  Binary powering by the exponent `U_YH` costs a polynomial in
`n+log U_Y`, hence numerical-QP bit operations.  Factor-first stripping
uses the known prime list of `H` together with the sieve factorization of
`U_Y` and makes only numerical-QP many modular-power and gcd calls.

For factored words `W_i`, the lcm factorization takes the maximum recorded
valuation at each listed prime.  Its logarithmic height is no more than the
sum of the input logarithmic heights, and its factor-list size is no more
than the sum of the input list sizes.  This proves Theorem C.  A compact
binary encoding of an astronomically large exponent valuation is not being
mistaken for the binary length of the resulting word.

If `W_i|W_*`, then each return probability `1/r_p`, `1/r_q` weakly
increases.  The union expression

\[
\alpha_p+\alpha_q-\alpha_p\alpha_q
\]

is weakly increasing in each variable on `[0,1]`, while the exact stale term
in (7) is independent of `W`.  This proves the monotonicity claim (20).

For unrelated witnesses, every certified common block divides both `P`
and `Q`, hence divides `D`.  Their lcm remains a certified divisor of `D`.
The exact stale formula depends only on this aggregate `M`; it never assumes
that one witness realizes the full lcm as its order.

## 6. Failure branch and the remaining source

Equation (21) is immediate because `U_Y` contains every full primary part
with prime at most `Y` and contains no prime greater than `Y`.  If both
residuals are nontrivial, (9) is the exact direct-factor lower bound.

Any declared factor or certificate requires at least one local return.
The union bound and (6) therefore give (22).  If both residuals are
`2^{Omega(n)}`, this is `2^{-Omega(n)}`.  The conclusion cannot be inferred
from `Y`-roughness alone because the least prime above a numerical-QP `Y`
can itself still have numerical-QP size.

For an arbitrary factored `W`, Theorem A gives inverse-QP direct-factor
probability whenever both residuals are nontrivial and their minimum is
numerical-QP.  If one residual is one, Theorem B gives constant progress,
and the equal-group case is impossible here.  These are precisely
the two uniform-projection ways to close the source through a factored
word.  Producing such a word on every input remains the missing
integer-specific step.  For correlated sources, one-coordinate identity
mass is not enough: the identity events may all be simultaneous stale
returns.  Such a source must instead lower-bound exactly-one return or
nonstale-global-return mass, equivalently factor-or-growth mass for this
decoder.
