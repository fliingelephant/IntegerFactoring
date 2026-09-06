# F230 blind reconstruction

## Verdict

**PASS, for the favorable-state theorem as stated.**  The zero-defect
classification, odd projection, exact local probabilities, bank dichotomy,
stripping certificate, constants `2/3` and `4/9`, history-uniform drift,
random-source rates, and sparse-source upper bound all follow from the stated
premises.

This is not a pass for an all-input factoring algorithm.  The theorem assumes
the beta-two residue, the capacity condition, the small-residual condition, a
complete factorization of `H`, and a dispatcher that can deal with the
recursive child.  None of those missing global coverage obligations follows
from F230.

I verified before reading that the SHA-256 of `STATEMENT.md` was

```text
96edf9b0eb183364ce9178385e289e8e7c5dc967d32f74912aaff7548ba5999f
```

This reconstruction used only the workspace `PROMPT.md` and the hashed F230
`STATEMENT.md`.  It used no numerical experiment.

## 1. Zero defect

Put `m=floor(n/2)`, so `B=2^m`.  Because `u`, `N`, and hence `uN` are odd,
the remainder of `uN` modulo `B` is nonzero.  Thus the specified remainder
really lies in `1,...,B-1`.

Suppose first that `1<=u<B` and

\[
E_{u,c}=u-R_u+cB=0.
\]

Then `R_u=u+cB`, so `R_u` is congruent to `u` modulo `B`.  On the other hand,
`R_u` is congruent to `uN` modulo `B`.  Hence

\[
u(N-1)\equiv0\pmod B.
\]

The odd integer `u` is a unit modulo the power of two `B`, so `B|(N-1)`.
Now `R_u` and `u` both lie strictly between zero and `B` and are congruent
modulo `B`; consequently `R_u=u`, and then `c=0`.  Conversely, if
`B|(N-1)`, then `uN` is congruent to `u` modulo `B`.  The same range argument
gives `R_u=u`, and `c=0` gives zero defect.  This proves (1).

Writing `N=BH+1` in this branch gives

\[
uN=(uH)B+u,
\]

so uniqueness of quotient and remainder gives (3).

For the extension, write `u=v+kB` with `0<v<B`.  Zero defect gives

\[
R_u=v+(k+c)B.
\]

The allowed range for `R_u` forces `R_u=v` and `c=-k`.  The congruence
argument again gives `B|(N-1)`.  Conversely,

\[
uN=(uH+k)B+v,
\]

so `Q_u=uH+k`, `c=-k`, and `A_{u,c}=uH`.  This proves the stated general
extension (with Euclidean quotient and remainder understood for the extended
range of `u`).

Finally, `N<2^n`, and therefore

\[
H={N-1\over 2^{\lfloor n/2\rfloor}}
  <2^{\lceil n/2\rceil}.
\]

Thus `H` has at most `ceil(n/2)` bits.  If `H` is completely factored, a
sieve through a numerical-quasipolynomial bound `U` completely factors all
public `u<=U`; merging those prime multiplicities with those of `H` factors
every `uH`.  The number of sieve entries and their total bit cost remain
numerical-quasipolynomial.

## 2. Common odd part and odd projection

Let `p-1=2^r P` and `q-1=2^s Q`, with `P,Q` odd.  Since `B` is a power of two,
it is coprime to both `P` and `Q`.  In the zero-defect branch,

\[
\begin{aligned}
\gcd(H,P)
 &=\gcd(BH,P)\\
 &=\gcd(N-1,P)\\
 &=\gcd(q-1,P)\\
 &=\gcd(2^sQ,P)=\gcd(P,Q)=D.
\end{aligned}
\]

The third equality uses `p=1 mod P`.  Interchanging `p` and `q` proves
`gcd(H,Q)=D`.  In particular `D|H`.  If `H=Dh`, then
`gcd(h,s_p)=gcd(h,s_q)=1`.  Also

\[
\gcd(s_p,s_q)=1,
\qquad
S=\operatorname{lcm}(s_p,s_q)=s_ps_q.
\]

Since `P=D s_p` and `Q=D s_q`, both divide `HS`.  Thus `HS` annihilates both
odd projected subgroups.  This observation does not make `S` public or
small.

By the Chinese remainder theorem, a uniform unit `x mod N` has independent
uniform coordinates in the cyclic groups of orders `p-1` and `q-1`.
Raising a cyclic group of order `2^rP` to `2^n` maps it uniformly onto its
unique subgroup of order `P`: here `n>r` because `2^r<=p-1<N<2^n`.
The same holds on the `q` side.  Therefore `a=x^(2^n)` has independent,
uniform coordinates in cyclic groups of orders `P` and `Q`.

For a uniform element of a cyclic group of order `T`, the fraction killed by
an exponent `e` is `gcd(e,T)/T`.  Indeed, the kernel of the endomorphism
`z -> z^e` has exactly `gcd(e,T)` elements.  For `e=uH`,

\[
\gcd(uH,P)=D\gcd(u,s_p),
\]

because `H=Dh` and `h` is coprime to `s_p`.  Division by `P=D s_p` gives
the first formula in (7), and the second is identical.

Let `X_p` and `X_q` be the two local-return events.  Their independence gives

\[
\Pr(X_p\mathbin\triangle X_q)
=\alpha_p(1-\alpha_q)+\alpha_q(1-\alpha_p)
=\alpha_p+\alpha_q-2\alpha_p\alpha_q,
\]

which is exactly the probability of a proper gcd.  Their intersection has
probability `alpha_p alpha_q`, proving (8) and (9).  The cyclic-kernel count
uses full prime-power multiplicities, so no squarefreeness of `P`, `Q`, or
their common part has been assumed.

Sampling `x` uniformly from `1,...,N-1` does not alter these conclusions.
A nonunit gives an immediate proper gcd.  Conditional on being a unit, `x`
is uniform on the unit group, so every lower bound proved for a uniform unit
continues to hold for the whole sampling step.

## 3. What stripping must do

The stripping claim is valid with the following explicit procedure.  Suppose
`a^A=1 mod N`, where the complete factorization of `A=uH` is known.  Maintain
an exponent `e|A` that still annihilates both CRT coordinates; initially
`e=A`.  For each prime `ell|e`, test

\[
g_\ell=\gcd(a^{e/\ell}-1,N).
\]

There are only three cases.

1. If `g_ell=N`, replace `e` by `e/ell` and repeat.
2. If `g_ell` is proper, return it.
3. If `g_ell=1`, do not divide `e` by `ell`; move to another prime.

Let `r_p,r_q` be the two local orders.  At every test they divide `e`.  Put
`j_p=v_ell(r_p)`, `j_q=v_ell(r_q)`, and `d=v_ell(e)`.  A coordinate returns
after the puncture precisely when its `j` is at most `d-1`.  Thus case 1
means both valuations are below `d`; case 2 means exactly one equals `d`;
and case 3 means

\[
j_p=j_q=d.
\]

In case 3, `ell^d` divides both `P` and `Q`, hence it divides `D`.  It is
therefore a sound certified common primary block.  Continuing to strip all
other primes is safe because the maintained exponent still annihilates both
coordinates.  Taking the least common multiple of all certified blocks and
the previous `M` preserves `M|D`.  A block not already contained in `M`
makes `M` grow strictly.  This procedure also explains why a repeated global
return that yields only blocks already in `M` must not stop a stage.

## 4. The favorable bank and its constants

Assume `min(s_p,s_q)<=U` and first suppose `(s_p,s_q)!=(1,1)`.  One of the
two residual orders itself occurs as an odd bank entry.  For example, if
`s_p<=U`, choose `u=s_p`.  Then

\[
\alpha_p=1,
\qquad
\alpha_q={\gcd(s_p,s_q)\over s_q}={1\over s_q}.
\]

If `s_q>1`, it is odd and hence at least three, so the direct-factor
probability is

\[
1-{1\over s_q}\ge {2\over3}.
\]

If `s_q=1`, then choosing `u=s_q=1` instead annihilates the `q` side and
gives `1-1/s_p>=2/3`.  The symmetric argument handles the case in which
`s_q<=U`.  Thus every nontrivial residual pair has a bank entry with direct
factor probability at least `2/3`.  The bank need not know which entry it
is.  If its public gcd screen has already found a factor, the conclusion is
only stronger.

Now suppose `s_p=s_q=1`.  Then

\[
P=Q=D,
\]

and `H` annihilates both complete odd subgroups.  Because `M|D` and both are
odd,

\[
L=\operatorname{lcm}(2^t,M)=2^tM,
\qquad
\operatorname{lcm}(2^t,D)=2^tD.
\]

If the latter is at least `J` while `L<J`, then `M` is a strict divisor of
`D`.  Hence some odd prime `ell` satisfies `v_ell(M)<v_ell(D)`.  Set

\[
k=v_\ell(M)+1.
\]

For a uniform element of a cyclic group whose order has `ell`-adic
valuation `d`, the probability that the element's order has valuation at
least `k` is

\[
1-\ell^{-(d-k+1)}.
\]

To see this, project to the cyclic `ell`-primary component of order
`ell^d`.  Exactly `ell^(k-1)` of its `ell^d` elements have order dividing
`ell^(k-1)`.  Applying this independently to the two CRT coordinates gives
the exact product in (13).

On this event both local `ell`-order valuations are at least `k`.  During
stripping at `u=1`, redundant `ell` powers of `H` are first removed.  If the
two local valuations differ, the first puncture that separates them gives a
proper factor.  If they are equal, the first puncture below that common
valuation gives gcd one and certifies an `ell`-primary block of exponent at
least `k`, which is strictly beyond `M`.  Since `ell>=3` and both exponents
`d-k+1` are at least one,

\[
\left(1-\ell^{-(d_p-k+1)}\right)
\left(1-\ell^{-(d_q-k+1)}\right)
\ge (1-1/3)^2={4\over9}.
\]

This proves the second half of the dichotomy.  Combining it with the
`2/3` direct-factor case proves the claimed stage lower bound `4/9`.
Crucially, the missing prime and the favorable residual order are witnesses
for the proof; the algorithm finds them by scanning and never needs to name
them.

The lower bound is uniform over prior completed stages.  Given any such
history, `M` is fixed and still divides `D`, while the next sampled unit has
fresh independent uniform CRT coordinates.  The witness just constructed
therefore has the same conditional probability.  No independence between
different entries of one bank is needed: the occurrence of the favorable
entry's direct event is already sufficient, and any earlier factor or strict
growth is also success for the stage.

## 5. Lcm drift, termination, and cost

If a certified block makes `M` grow, then, because all blocks are odd,

\[
{L'\over L}={M'\over M}\ge3.
\]

Consequently, whenever the process remains preterminal,

\[
\Phi(L')
=\left\lceil\log_2{J\over L'}\right\rceil
\le \left\lceil\log_2{J\over L}\right\rceil-1.
\]

A factor is absorbing, and crossing `L>=J` sets the potential to zero.
At every positive-potential history a stage therefore either absorbs or
decreases the integer potential by at least one with conditional probability
at least `4/9`.  The usual conditional waiting-time argument, which does not
assume independent stages, gives

\[
\mathbb E[\text{stages}]
\le {\Phi(L_0)\over 4/9}.
\]

For the intended positive numerical-quasipolynomial scale `S_0(n)>=1`,
`J<=ceil(N^(1/4))<=N`, while `L_0>=1`.  Hence `Phi(L_0)<=n` and the displayed
bound is at most `9n/4`.  The same conditional bound implies almost-sure
termination: the probability of seeing infinitely many failures before any
one of the finitely many required potential decreases is zero.

Every certified `M` divides `D`, hence divides both `p-1` and `q-1`.  In
particular `p=1 mod M`.  Combining this with the supplied residue of `p`
modulo `2^t` gives `p` modulo `L=2^tM` by CRT.  At `L>=J`, the missing factor
between `L` and `N^(1/4)` is at most `S_0`.  One can make the invoked
known-residue reduction explicit as follows: choose a
numerical-quasipolynomial-size auxiliary modulus coprime to `L` that raises
the product modulus slightly above `N^(1/4)`, enumerate its possible residue
of `p`, combine each with the known residue modulo `L`, and apply the standard
deterministic small-root factorer for a divisor with at least one-half of the
input's bits.  Direct gcd screens handle an auxiliary modulus that meets a
factor, and every candidate divisor is verified by division.  The number of
residues is numerical-quasipolynomial.  This is precisely the external
known-residue lemma invoked in the statement; F230's new local argument does
not itself prove the underlying lattice small-root theorem.

A bank has `O(U)` entries.  Its sieve, modular exponentiations, gcds, and
punctures involve exponents of `O(n+log U)` bits and moduli of `n` bits.
There are at most `O(n+log U)` prime-power punctures per entry.  Thus one
bank, and then `O(n)` expected banks, have numerical-quasipolynomial bit
cost.  Uniform sampling by rejection, random-bit generation, CRT, and
candidate verification are polynomial and do not change that bound.

The factorization of `H` is a separate recursive obligation.  Its bit length
is at most `ceil(n/2)`, and it need be computed only once and cached before
the banks.  If a globally correct dispatcher covers every recursive child,
the favorable branch has a recurrence of the form

\[
T(n)\le T(\lceil n/2\rceil)+R(n)
\]

with numerical-quasipolynomial `R`; summing over the logarithmically many
halving levels remains numerical-quasipolynomial.  F230 supplies no route for
an arbitrary `H` that the dispatcher does not otherwise cover.  Assuming
such coverage is therefore not a proof of that coverage and cannot be used
to promote F230 to an all-input factoring result.

## 6. Random multiplier and shift rates

There are exactly `O_U=ceil(U/2)` odd integers in `[1,U]`.  In every
preterminal state, at least one of them is the witness constructed above,
and its conditional factor-or-growth probability is at least `4/9` (at
least `2/3` in the nontrivial-residual case).  A uniform odd choice therefore
has rate at least

\[
{4\over9O_U}\ge {4\over9U}.
\]

If an independent shift is uniform on `W` consecutive integers containing
zero, exactly one of those shifts is zero.  The event `c=0` has probability
`1/W`, so intersecting it with the favorable multiplier event gives

\[
{4\over9O_UW}.
\]

Other shifts can only add successes to this lower bound.  Once the public
test `B|(N-1)` succeeds, Section 1 shows that zero is the unique zero-defect
shift for `u<B`; randomizing it has no benefit and only dilutes this branch.

## 7. Sparse bounded-source law

Fix a screened multiplier `u` and put `A=uH`.  Every punctured exponent used
by the stripping procedure divides `A`.  A local return at a divisor of `A`
implies a local return at `A`.  A proper gcd at any puncture needs a return
on at least one side.  A nontrivial common-primary certificate from the
stripping procedure first needs a global annihilating exponent and hence
also needs a local return.  Thus every useful event in this source model is
contained in `X_p union X_q`, whose exact probability is

\[
\alpha_p+\alpha_q-\alpha_p\alpha_q.
\]

For `u<=U`,

\[
\alpha_p={\gcd(u,s_p)\over s_p}\le {u\over s_p}\le {U\over s_p},
\qquad
\alpha_q\le {U\over s_q}.
\]

Dropping the negative product proves (18).

For fresh projections and adaptive choices, the claim is valid in the
standard predictable sense: `u_i` may depend on all prior tests but is fixed
before the fresh independent projection `a_i` is sampled.  Conditioning on
the past then reduces to the fixed-`u_i` bound above.  A conditional union
bound over `K` tests proves (19).  For a fixed bank on one shared projection,
apply the ordinary union bound to the `K` individual local-return unions;
no within-bank independence is required.

If both residual orders are at least `2^(c n)` for some fixed `c>0`, while
`K` and `U` are numerical-quasipolynomial, then (19) is
`2^(-Omega(n)+polylog(n))`, hence exponentially small.  This conclusion is
only about bounded integer multipliers paired with uniform odd projections.
The proof says nothing about a source correlated with carries, a nonuniform
integer source, APR-style residue information, or a different exploitation
of the factorization of `H`.

## 8. Stated witness

For `N=2881`, one has `n=12`, `B=64`, and `N-1=64*45`, so `H=45`.
For `p=43` and `q=67`, the odd parts are `P=21` and `Q=33`; hence `D=3` and
the residuals are `7` and `11`.  At `u=7`, `A=uH=315`, and (7) gives
`alpha_p=1`, `alpha_q=1/11`.  Formula (8) therefore gives the claimed
`10/11` direct-factor probability.

## Qualifications

1. The exact `9n/4` display uses the intended convention `S_0(n)>=1`.  If
   “positive” were allowed to mean an arbitrarily tiny real-valued function,
   the proof would instead give `(9/4) Phi(L_0)` and would need an additional
   bound on `log(1/S_0)`.  A numerical-quasipolynomial search scale is
   naturally integer-valued and at least one.
2. “Adaptive” in Theorem D must mean that the multiplier is chosen before
   seeing its fresh projection.  If `u` can depend on the same fresh `a`, the
   fixed-`u` kernel count cannot simply be conditioned in the asserted way.
3. “Exponent puncture” must mean replacing a known global exponent by its
   divisors, as in Section 3.  The source-model upper bound does not claim to
   cover arbitrary exponents or other algebraic operations.
4. The beta-two residue and the known-residue small-root factorer are inputs
   to the final implication, not results proved by F230.  The recursive
   dispatcher is also a genuine global dependency.  These limitations agree
   with the statement's explicit favorable-state boundary.
