# Proof of the F230 zero-defect odd-projection candidate

## 1. Zero-defect classification

Assume `1<=u<B` is odd.  If `E_{u,c}=0`, then

\[
R_u=u+cB.
\]

Both `R_u` and `u` lie strictly between zero and `B`.  Hence `c=0` and
`R_u=u`.  Reducing the defining division `uN=Q_uB+R_u` modulo `B` gives

\[
u(N-1)=0\pmod B.
\]

The odd integer `u` is a unit modulo the power of two `B`, so `B|(N-1)`.
This proves the forward implication in (1).

Conversely, if `B|(N-1)`, write `N=BH+1`.  Then

\[
uN=uHB+u.
\]

Because `0<u<B`, uniqueness of Euclidean division gives `Q_u=uH` and
`R_u=u`.  Thus `E_{u,0}=0`, proving (1)--(3).

For general odd `u=v+kB` with `0<v<B`, the same congruence argument shows
that zero defect requires `B|(N-1)`.  In that branch `R_u=v`, so

\[
E_{u,c}=(k+c)B.
\]

It vanishes exactly at `c=-k`.  Multiplying the F228 identity

\[
BA_{u,c}=uN-R_u+cB
\]

and substituting zero defect gives

\[
BA_{u,c}=u(N-1)=uBH,
\]

so `A_{u,c}=uH` in the general branch as well.

Finally,

\[
H={N-1\over B}<2^{n-\lfloor n/2\rfloor}=2^{\lceil n/2\rceil}.
\]

This proves the size claim.  A sieve through a numerical-QP value `U`
factors every multiplier in numerical-QP work.  The factorization of `H`
then gives the factorization of every `uH` without another same-size
factoring call.

## 2. Odd common part and projection

The identity

\[
N-1=q(p-1)+(q-1)
\]

gives

\[
\gcd(N-1,p-1)=\gcd(q-1,p-1).
\tag{P1}
\]

Because `B` is a power of two, division by `B` does not change any odd
valuation of `N-1`.  Taking odd parts in (P1) proves

\[
\gcd(H,P)=D.
\]

The symmetric identity proves `gcd(H,Q)=D`.  This is (5).  Dividing `P`
and `Q` by their full gcd proves `gcd(s_p,s_q)=1`, and hence
`S=s_ps_q`.  Equations (5) and (P2) also show that `P|SH` and `Q|SH`.
Thus `SH` annihilates the projected odd subgroup.  This is an analysis
identity only: `S` depends on the hidden factors and is not available to the
algorithm.

The groups modulo `p` and `q` are cyclic of orders

\[
p-1=2^{e_p}P,
\qquad q-1=2^{e_q}Q.
\]

Both `e_p` and `e_q` are less than `n`.  Raising a uniform local unit to
`2^n` kills its two-primary coordinate.  On the odd coordinate it is an
automorphism because `2^n` is coprime to `P` and `Q`.  Therefore the image
is uniform in the odd-order subgroup.  CRT makes the two images independent.

In a cyclic group of order `P`, the equation

\[
y^{uH}=1
\]

has exactly `gcd(uH,P)` solutions.  Equation (5), prime by prime, gives

\[
\gcd(uH,P)=D\gcd(u,s_p).
\tag{P2}
\]

Indeed, if a prime has positive valuation in `s_p`, then (5) says that `H`
contains exactly its `D`-valuation; if it has no valuation in `s_p`, both
sides of (P2) are already saturated.  Dividing (P2) by `P=Ds_p` proves the
first formula in (7).  The second is identical.

The local return events are independent.  Exactly one return gives a proper
gcd, and two returns give a global return.  This proves (8) and (9).

## 3. Certified prime-power stripping

Let a completely factored exponent `A` satisfy `a^A=1 mod N`.  Maintain a
current annihilator `E`, initially `A`.  For a prime `ell|E`, compute

\[
g=\gcd(a^{E/\ell}-1,N).
\tag{P3}
\]

- If `g=N`, both local orders divide `E/ell`.  Replace `E` by `E/ell` and
  repeat.
- If `1<g<N`, return the factor.
- If `g=1`, neither local order divides `E/ell`, while both divide `E`.
  Hence

  \[
  v_\ell(\operatorname{ord}_p(a))
  =v_\ell(\operatorname{ord}_q(a))
  =v_\ell(E).
  \]

  The primary `ell^v_ell(E)` is therefore certified to divide both `p-1`
  and `q-1`.

Process every prime of the current factored annihilator.  Reductions at one
prime preserve the annihilator property and do not alter an already proved
valuation at another prime.  Thus the procedure is valid for arbitrary
prime powers and returns a factor or a certified common order block.

Suppose `ell^k|D`.  In a cyclic local odd subgroup whose `ell`-valuation is
`e>=k`, a uniform element has order divisible by `ell^k` with exact
probability

\[
1-\ell^{k-1-e}
=1-\ell^{-(e-k+1)}.
\tag{P4}
\]

For the two independent coordinates, multiplication gives (13).  On this
event, the stripping loop at `ell` reaches one of two outcomes.  Unequal
local order valuations give a proper gcd at the first unequal puncture.
Equal valuations give `g=1` and certify their common value, which is at
least `k`.  No hidden primary selector is used by the algorithm; the proof
may choose any primary missing from the current public `M`.

## 4. Favorable-state progress

First suppose `(s_p,s_q)!=(1,1)` and `min(s_p,s_q)<=U`.  Because the two
residuals are coprime and odd, the bank contains a residual `w` whose other
residual `z` is greater than one:

- if both exceed one, take whichever is at most `U`;
- if one equals one, take that one, whose counterpart exceeds one.

Assume for notation that `w=s_p` and `z=s_q`; the other orientation is
identical.  At the bank entry `u=w`, equation (7) gives

\[
\alpha_p=1,
\qquad \alpha_q={1\over z},
\]

because `gcd(w,z)=1`.  Hence (8) gives the exact proper-factor probability

\[
1-{1\over z}\ge {2\over3},
\tag{P5}
\]

as every odd `z>1` is at least three.

The bank must continue after a stale earlier global return.  Its declared
algorithm does so.  Therefore no earlier entry can suppress the useful
entry `u=w`.

Now suppose `s_p=s_q=1`.  Then `P=Q=D`, and `u=1` makes `H` an annihilator
of every projected base.  Since `M|D`, preterminality together with (11)
implies that some odd primary of `D` is missing from `M`.  Put

\[
k=v_\ell(M)+1\le v_\ell(D).
\]

Section 3 and (P4) give factor-or-growth probability at least `4/9` at the
entry `u=1`.  Combining this with (P5) proves (12).

The sample `x` can be taken uniformly from `1,...,N-1` without a unit
oracle.  A nonunit has a proper gcd with the semiprime and is already a
success.  Conditional on no such factor, `x` is exactly uniform among the
units, so the lower bounds above remain valid unconditionally.

Each successful nonterminal stage decreases the integer potential `Phi` by
at least one.  A factor sets it to zero.  Thus its conditional expected
decrease is at least `4/9`.  Since `Phi<=n`, direct telescoping gives at most
`9n/4` expected stages.

One stage has numerical-QP cost: there are numerical-QP many multipliers,
every exponent has `n/2+polylog(n)` bits, modular powering is polynomial in
the exponent bit length and `n`, and stripping uses at most the total number
of prime occurrences in the factored exponents.  The one recursive input
`H` has at most half as many bits.  This proves the stated conditional cost.

The true factor residue modulo `2^t` and the certified congruence

\[
p\equiv1\pmod M
\]

combine modulo `lcm(2^t,M)`.  When it reaches `J`, the P175/P197
known-residue terminal costs numerical-QP.  This proves the beta-two/lcm
conclusion.

## 5. Random multiplier and random shift

In the proof of Section 4, one specific odd `w<=U` has conditional
factor-or-growth probability at least `4/9`.  A uniform odd multiplier hits
it with exact probability `1/O_U`.  This proves (15).  The algorithm does
not know `w`; it samples from the public full range.

For `u<B`, Theorem A says zero defect occurs at exactly one shift, `c=0`.
A uniform set of `W` consecutive shifts containing zero selects it with
probability `1/W`.  Multiplying the independent probabilities proves (16).
Events at nonzero shifts can only add success and were not counted.

## 6. Sparse-source upper law

Fix a screened multiplier `u`.  If neither local coordinate satisfies
`a^(uH)=1`, then no exponent dividing `uH` can annihilate either coordinate.
Thus the initial gcd and every possible puncture of this same exponent are
useless.  A factor or certificate requires the union of the two local
return events.  Independence and (7) give its exact probability

\[
\alpha_p+\alpha_q-\alpha_p\alpha_q,
\]

which proves (17).

For `u<=U`,

\[
\alpha_p={\gcd(u,s_p)\over s_p}\le {U\over s_p},
\qquad
\alpha_q\le {U\over s_q}.
\]

Dropping the negative product proves (18).  The inequality is conditional
on every earlier history, provided the next base is a fresh uniform odd
projection and the adaptive multiplier remains in `[1,U]`.  A union bound
proves (19).  The same union bound applies to a fixed bank on one projection
without an independence assumption.  This argument says nothing about a
nonuniform or carry-correlated base or multiplier, so the stated scope is
exact.
