# F231 blind reconstruction

## Authentication and isolation

The authenticated statement has SHA-256

```text
f7503be5f8db21697157bc6f267b5719e656d55b395f8d8d524c5a0661d1dd56
```

This reconstruction used only the repository-root `PROMPT.md` and the
authenticated F231 `STATEMENT.md`. It did not inspect any proof, audit,
provenance, manifest, ledger, message, or other F231 work product. No
numerical experiment was used.

## Verdict

**PASS for the internal, conditional F231 theorem.** Equations (3)--(22),
the exact stale-return law, the smooth-word progress theorem, its Las Vegas
stage bound, the word-size claims, and the rough-residual boundary all admit
independent proofs from the declared hypotheses.

This verdict has three scope qualifications.

1. F231 is only a favorable-state semiprime theorem. It assumes the balanced
   zero-defect branch, a correctly factored half-size child `H`, and a smooth
   or otherwise absorbed hidden residual. It does not supply the all-input
   dispatcher required by the root prompt.
2. The beta-two terminal uses the standard small-root theorem for a known
   residue of a balanced factor. A QP-safe reduction to that theorem is given
   below. Thus “immediately” means “without another random word stage, in
   numerical-QP bit complexity,” not constant time.
3. The historical assertions about F230, P161, and P197 are not verifiable
   from the permitted sources. None is needed for the internal proof below.

## 1. Arithmetic forced by the zero-defect branch

Write

\[
p-1=2^\alpha P,\qquad q-1=2^\beta Q,
\]

where `P,Q` are odd and `alpha,beta >= 1`. Since `B` is a power of two and
`P,Q` are odd,

\[
\gcd(H,P)=\gcd(N-1,P).
\]

Modulo `P`, one has `p=1`, and hence `N-1=pq-1=q-1`. Therefore

\[
\gcd(H,P)=\gcd(P,q-1)=\gcd(P,2^\beta Q)=\gcd(P,Q)=D.
\]

The same argument with `p,q` exchanged gives `gcd(H,Q)=D`. Also

\[
\gcd(s_p,s_q)
=\gcd(P/D,Q/D)=1.
\]

In particular, `D` divides `H`. Every maintained certificate `M|D` therefore
also divides `H`.

The child is genuinely half-size. If `m=floor(n/2)`, then

\[
H=(N-1)/2^m<2^{n-m}=2^{\lceil n/2\rceil}.
\]

This proves only the size reduction. The existence and correctness of a
dispatcher that factors this child remain external assumptions of F231.

## 2. Projected distribution and exact return kernels

By CRT, a uniform unit `x mod N` has independent uniform coordinates in
`F_p^*` and `F_q^*`. The first group has order `2^alpha P`. Since
`p-1<2^n`, raising to `2^n` kills its complete two-primary component. On
its odd component it is an automorphism. Thus the `p`-coordinate of

\[
a=x^{2^n}\pmod N
\]

is uniform in the unique subgroup of order `P`. The `q`-coordinate is
independently uniform in the subgroup of order `Q`.

For a uniform element of a cyclic group of order `P`, the probability of
being killed by exponent `A` is `gcd(P,A)/P`. It remains to evaluate this
gcd for `A=WH`. Fix an odd prime `ell` and put

\[
e=v_\ell(P),\quad f=v_\ell(Q),\quad h=v_\ell(H),
\quad w=v_\ell(W),\quad d=\min(e,f).
\]

The identity `gcd(H,P)=D` says `min(h,e)=d`. If `e=d`, both sides below
have valuation `e`. If `e>d`, then necessarily `h=d`, and

\[
v_\ell(\gcd(P,WH))
=\min(e,d+w)
=d+\min(e-d,w).
\]

Consequently

\[
\gcd(P,WH)=D\gcd(s_p,W),
\]

including the case where `D` and `s_p` share a prime. Hence

\[
\Pr(a^A=1\bmod p)
=\frac{D\gcd(s_p,W)}{P}
=\frac1{r_p(W)}.
\]

The proof for `q` is identical. The two return events are independent. The
residuals are odd and coprime because they divide the coprime integers
`s_p,s_q`.

The probability statement must be read conditionally on the current history:
`M` and `W` are fixed, and then a fresh unit is sampled. After a specific unit
has been sampled, the event itself is deterministic.

## 3. The return-and-puncture decoder

Let `o_p,o_q` be the exact local orders of `a`. If exactly one divides `A`,
then `gcd(a^A-1,N)` is immediately `p` or `q`. If neither divides `A`, that
gcd is one. Suppose both divide `A`, so the initial gcd is `N`.

The complete factorization of `A` permits the following stripping argument.
Start with `C=A`. For each prime `ell|C`, repeatedly evaluate

\[
g=\gcd(a^{C/\ell}-1,N).
\]

If `g=N`, replace `C` by `C/ell`. If `1<g<N`, return `g`. If `g=1`, stop
stripping that prime. Throughout this process `C` is a multiple of both
local orders. At a fixed prime, stripping continues until its exponent in
`C` reaches `max(v_ell(o_p),v_ell(o_q))`. The next puncture has these exact
outcomes:

- unequal local valuations give a nontrivial gcd;
- equal positive valuations give gcd one;
- a prime absent from both orders is stripped completely.

It follows that unequal local orders always expose a factor. If no factor is
exposed, the final `C` is exactly `o_p=o_q=d`. Since `d` divides both `P`
and `Q`, it divides `D`; its primary blocks can therefore be added safely to
`M` by lcm.

The only non-useful outcome among samples for which at least one coordinate
returns is now

\[
o_p=o_q=d\quad\text{for some }d\mid M.
\]

Every such `d` divides `H`, so it does cause a global return. A cyclic group
of order `P` has exactly `phi(d)` elements of exact order `d` for every
`d|P`. Independence of the two coordinates therefore gives the exact stale
probability

\[
\Pr(\text{stale})
=\frac1{PQ}\sum_{d\mid M}\varphi(d)^2.
\]

The probability that at least one coordinate returns is

\[
\frac1{r_p}+\frac1{r_q}-\frac1{r_pr_q}.
\]

Subtracting the stale atom proves (7) exactly. This also handles order one,
because `d=1` is included and is always stale.

The standard identity `sum_{d|M} phi(d)=M` and nonnegativity imply

\[
\sum_{d\mid M}\varphi(d)^2
\leq\left(\sum_{d\mid M}\varphi(d)\right)^2=M^2.
\]

Since `PQ=D^2s_ps_q`, this proves (8).

The direct-factor event is the exclusive-or of the two returns, so its exact
probability is

\[
\frac1{r_p}+\frac1{r_q}-\frac2{r_pr_q}.
\]

If, without loss of generality, `r_p<=r_q` and both residuals exceed one,
then the odd integer `r_p` is at least three, and

\[
\left(\frac1{r_p}+\frac1{r_q}-\frac2{r_pr_q}\right)-\frac1{r_p}
=\frac{r_p-2}{r_pr_q}\geq0.
\]

This proves (9).

Uniform unit sampling does not require knowledge of the factors. Sample
uniformly from `1,...,N-1`, using ordinary rejection from random bits, and
first compute `gcd(x,N)`. A nonunit gives `p` or `q`; conditional on being a
unit, the distribution above is exact. The unconditional useful-event
probability is therefore at least the conditional one.

## 4. Smooth words and constant progress

Every prime `ell<=Y` occurs in `Lambda_Y`. If an integer `z<N` has only such
prime divisors and `ell^e|z`, then

\[
2^e\leq\ell^e<N<2^n,
\]

so `e<n`. The exponent of `ell` in `U_Y=Lambda_Y^n` is at least `n`.
Thus every `Y`-smooth integer below `N` divides `U_Y`. Since
`s_p,s_q<N`, this proves the equivalence in (11), including arbitrary
prime-power exponents. It also explains why the unpowered lcm is not enough.

It remains to prove that `s_p=s_q=1` cannot occur. Under that assumption
`P=Q=D`. Write

\[
p=1+2^\alpha D,\qquad q=1+2^\beta D.
\]

Since `p<q`, one has `alpha<beta`. The inequality `q<2p` rules out
`beta>=alpha+2`, so `beta=alpha+1`. Then

\[
N-1
=2^\alpha D\bigl(3+2^{\alpha+1}D\bigr),
\]

whose parenthesized factor is odd. Hence `v_2(N-1)=alpha`. On the other
hand, `N>2^{2alpha+1}`, so `n>=2alpha+2` and
`floor(n/2)>=alpha+1`. This contradicts `B|N-1`. Therefore
`s_ps_q>1`; since the product is odd, it is at least three.

If one residual for `W=U_Y` equals one, at least one coordinate returns
with probability one. Formula (7) and (8), for every current `M|D`, give

\[
\Pr(\text{factor or strict growth})
=1-\Pr(\text{stale})
\geq1-\frac1{s_ps_q}\geq\frac23.
\]

This proves (13), even if both residuals equal one. When `M=D`, strict growth
is impossible, so every useful event is a factor.

A strict lcm growth replaces `M` by a strictly larger odd multiple of `M`
that still divides `D<N<2^n`. Each such growth multiplies `M` by at least
three. There are consequently fewer than `n` growth events before a factor.
At every adaptive history, a fresh stage has conditional progress probability
at least `2/3`. The expected waiting time for the next useful event is at most
`3/2`, without needing independence between different waiting intervals.
There are at most `n` useful events through the terminal factor. Thus the
expected number of stages is at most `3n/2`. The same conditional lower bound
also makes every waiting interval finite almost surely, which proves almost-
sure termination.

For the child-supported word, a prime exponent in either `s_p` or `s_q` is
strictly less than `n`, because that residual is below `N<2^n`. Therefore the
factor `ell^n` absorbs every primary block whose prime `ell` divides `H`.
Together with the small-prime absorption by `U_Y`, this proves (16) and the
broader version of Theorem B.

## 5. Composition with a known beta-two residue

Because `M|P|p-1`, one knows `p=1 mod M`. Combining this with the supplied
residue `p mod 2^t` by CRT gives `p mod L`, where

\[
L=\operatorname{lcm}(2^t,M)=2^tM.
\]

Here is a QP-safe reconstruction of the claimed terminal. Use the standard
degree-one Coppersmith divisor-root theorem: if an integer `N` has a divisor
at least `N^beta`, then all sufficiently small roots of a linear polynomial
modulo that divisor, up to `N^(beta^2-epsilon)`, can be recovered by lattice
reduction. Its bit cost is polynomial in the input and lattice dimensions;
allowing `1/epsilon` to be polynomial in `n` therefore remains numerical-QP.

Knowing a residue modulo exactly `N^(1/4)` sits at the boundary, so introduce
a harmless QP margin. Let

\[
R(n)=2^{(\log_2(n+1))^2+4},\qquad
k=\left\lceil\frac{R(n)N^{1/4}}{L}\right\rceil.
\]

If `L>=J=ceil(N^(1/4)/S_0(n))`, then
`k<=R(n)S_0(n)+1`, which is numerical-QP. Write the known residue as `r`
and enumerate `j=0,...,k-1`. For the correct `j`, writing `p=r+Lx` and
`x=j+kz` gives the stronger known congruence

\[
p\equiv r+Lj\pmod{Lk},\qquad Lk\geq R(n)N^{1/4},
\]

and

\[
0\leq z<\frac{p}{Lk}<\frac{N^{1/4}}{R(n)}.
\]

Balance gives `p>sqrt(N/2)`. Thus one may take
`beta=1/2-O(1/n)`. The QP factor `R(n)` supplies more than the
`N^epsilon` margin needed by the degree-one small-root theorem with
`epsilon=Theta((log R(n))/n)`; its reciprocal is polynomial in `n`.
If `gcd(Lk,N)>1`, that gcd already factors `N`. Otherwise make the linear
polynomial monic modulo `N`, recover `z`, and take the gcd of its evaluated
integer value with `N`. One of the QP-many guesses is correct. Small bounded
`n` can be handled by trial division.

Therefore `L>=J` gives a deterministic numerical-QP terminal. If this
terminal never fires, the smooth-word process still has the stage and
expectation bounds proved above. The CRT composition uses only `M|D`; it does
not require a single base whose order is `M`.

## 6. Bit complexity and accumulation of words

For `Y` bounded by a fixed numerical-QP function,

\[
\log_2U_Y
=n\log_2\Lambda_Y
\leq n\log_2(Y!)
\leq nY\log_2Y,
\]

which is numerical-QP. A sieve through the numerical value `Y` also has
numerical-QP time and space. It produces the factorization

\[
U_Y=\prod_{\ell\leq Y\atop \ell\text{ prime}}
\ell^{,n\lfloor\log_\ell Y\rfloor},
\]

whose entry count, prime encodings, and exponent encodings are all
numerical-QP.

The factorization of `A=U_YH` is obtained by merging two known factor lists.
Its bit length is numerical-QP. Binary modular powering costs a polynomial
in `n` times the exponent bit length. The stripping decoder performs at most

\[
\sum_{\ell\mid A}v_\ell(A)\leq\log_2A
\]

punctures. Even recomputing each power from scratch therefore has numerical-
QP bit cost. The expected `O(n)` stages, random-bit generation, gcds, lcm
updates, and output verification preserve the numerical-QP bound.

For the child-supported multiplier,

\[
\log_2\prod_{\ell\mid H}\ell^n
=n\log_2\operatorname{rad}(H)
\leq n\log_2H=O(n^2),
\]

which proves (18).

For general words, `W_i|W_*` implies

\[
r_p(W_*)\mid r_p(W_i),\qquad r_q(W_*)\mid r_q(W_i).
\]

The union-return expression

\[
F(r,s)=\frac1r+\frac1s-\frac1{rs}
=1-(1-1/r)(1-1/s)
\]

is nondecreasing when either residual is replaced by a divisor. The stale
term depends only on `P,Q,M`, not on `W`. This proves (20). The lcm height is
at most the sum of the input heights, and its factor list is formed by taking
the largest supplied exponent for each prime, so both its construction and
encoding remain numerical-QP.

The certificate interpretation is also intrinsic: every no-factor global
return yields one exact common order `d|D`, while the maintained certificate
is `lcm` of all such orders. No individual order has to equal the accumulated
`M`. The words affect which orders return; they do not by themselves prove
that any prime power divides `D`.

The sentence that the lcm is the “only canonical aggregate effect” must be
read in this precise, narrow sense: it is the least word divisible by every
supplied word, and it proves (20). It cannot mean that every other arithmetic
combination has the same return kernel. For example, a product can add the
valuations of a prime repeated in two source words, whereas their lcm takes
only the maximum. No formal claim above needs that stronger interpretation.

## 7. Exact rough-residual boundary

The prime support of `U_Y` is exactly the set of primes at most `Y`, and its
exponent at each such prime is enough to absorb all of `s_p,s_q`. Therefore

\[
r_p(U_Y)=\prod_{\ell\mid s_p,\ \ell>Y}
\ell^{v_\ell(s_p)},\qquad
r_q(U_Y)=\prod_{\ell\mid s_q,\ \ell>Y}
\ell^{v_\ell(s_q)},
\]

which proves (21). A nontrivial residual is consequently `Y`-rough.

Any output of the declared decoder requires at least one local return. Thus,
when both residuals are nontrivial,

\[
\Pr(\text{factor or common-order certificate})
\leq\Pr(\text{at least one return})
\leq\frac1{r_p}+\frac1{r_q},
\]

which proves (22). If both residuals are `2^(Omega(n))`, this probability is
`2^(-Omega(n))`. Roughness alone is weaker: an integer can have no prime at
most `Y` while still having numerical-QP magnitude.

Finally, the proposed source condition is both sufficient and, up to a
factor two in the bound, necessary for this uniform decoder. If
`min(r_p,r_q)=1`, Section 4 gives constant progress. If both exceed one,
(9) gives progress at least `1/min(r_p,r_q)`. Conversely, (22) is at most
`2/min(r_p,r_q)`. Hence inverse-QP decoder progress is equivalent, at the
level of QP bounds, to producing a QP-size factored word with QP-bounded
minimum residual. This equivalence assumes that the word is fixed before the
fresh projected sample and can itself be produced in numerical-QP bit cost.

For a nonuniform or carry-correlated source, the independence calculation no
longer applies. The exact replacement condition is inverse-QP mass on the
useful partition: exactly one local return, or a global return whose two
orders differ or whose common order does not divide `M`. A distribution can
put all of its identity mass on `(1,1)`, whose common order one is stale, so
one-coordinate identity mass alone gives no progress guarantee.

## 8. Final quantifier and scope audit

- Arbitrary prime powers are covered by valuation arguments, not by a
  squarefree assumption.
- `M` may combine unrelated witnesses because only certified divisibility
  `M|D` is used. No generator of exact order `M` is assumed.
- Adaptivity is valid only in the order “choose `M,W` from the past, then
  draw a fresh sample.” This is the natural reading of “at every history.”
- The expected-stage proof includes stale and no-return trials and proves
  almost-sure termination on the declared smooth favorable state.
- The bit bound counts word construction, word encoding, modular powers,
  punctures, random sampling, gcd/lcm arithmetic, and repetitions. The cost
  of factoring `H` is conditional. If a correct uniform QP child dispatcher
  were supplied, the single-child recurrence would preserve QP complexity,
  but F231 does not supply that dispatcher.
- “Negligible” in the child-word discussion can only mean that the extra
  `O(n^2)` logarithmic height preserves the numerical-QP class. It need not
  be lower order than `log U_Y` when `Y` is fixed.
- The nonuniform-source boundary is for projected units. If the source also
  samples nonunits, inverse-QP mass on a nontrivial initial gcd is an
  additional useful event.
- Prime inputs, prime powers, repeated factors, unbalanced composites, and
  zero-defect failures lie outside F231. Therefore this theorem does not meet
  the root prompt's all-input success criterion, exactly as its own boundary
  states.

No internal mathematical obstruction or probability/complexity gap was
found beyond these declared scope limits and the unauthenticated historical
cross-references.
