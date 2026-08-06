# Hostile re-audit of amended F33: quadratic-energy positive lift

**Artifact audited:**
`experiments/F33_quadratic_energy_positive_lift_kill/RESULT.md`.

**Prior audit read:**
`experiments/F33_quadratic_energy_positive_lift_audit/RESULT.md`.

**Protocol:** proof-only hostile re-audit from the definitions.  I checked the
whole amended artifact, not just the three repairs requested by the prior
audit.  No computation was used.

## Verdict

> **FAIL AS WRITTEN.**

The amendments correctly repair the prime-power overstatement, the missing
uniform polynomial-time decoder hypothesis, and the final start/kernel scope.
The formal positive-lift theorem, proper-factor mass bound, conditional
all-input Las Vegas reduction, matching reduction, exact annihilator sampler,
and random-scan hitting and mixing lower bounds all survive reconstruction.

One false structural equivalence remains.  Section 1 says that for a distinct
squarefree semiprime, factoring is *precisely* sampling a state whose “chosen
prime-field axes do not agree” across the two CRT components.  The origin is
on both axes, so an element of \(\Omega_N\) does not determine such a choice.
Under the natural common-axis interpretation, the claim is false; under a
labelled-axis interpretation, the labels are extra data not present in
\(\Omega_N\).  An exact counterexample and correction appear below.

This defect is interpretive and is not used in any count, reduction, or Markov
chain bound.  It nevertheless prevents a pass of the entire artifact as
written, just as a false prime-power geometry statement did in the prior
version.

## Required corrections

1. Replace the “chosen axes do not agree” equivalence, and soften the related
   “switching between ... axes” summary, by the exact three-type statement:

   > For \(N=pq\), define the local type at \(r\in\{p,q\}\) to be
   > \(H\) when \((k_r,x_r)\in\mathbb F_r^\times\times\{0\}\),
   > \(V\) when
   > \((k_r,x_r)\in\{0\}\times\mathbb F_r^\times\), and \(O\) when
   > \((k_r,x_r)=(0,0)\).  Then neither coordinate has a proper gcd
   > exactly when the two local types agree; a proper gcd is exposed exactly
   > when they differ.

   This is the precise squarefree field-component interpretation actually
   compatible with \(A_N\).

2. For exact bit-complexity wording, say that fair-bit rejection for the
   annihilator **terminates almost surely and has expected** polynomial bit
   cost.  Its runtime is not deterministically bounded because the rejection
   loop has unbounded support.  The underlying algorithm already has the
   required Las Vegas bound, so this is a quantifier clarification rather
   than a new mathematical obstruction.

No other correction was found.

## 1. Exact positive lift and its scope

Let

\[
\Omega_N=\{(k,x)\in(\mathbb Z/N\mathbb Z)^2:kx=0\}.
\]

For a fixed residue \(k\), put \(d=\gcd(k,N)\), \(k=dk_0\), and
\(N=dN_0\).  This also covers \(k=0\), for which \(d=N\) and
\(N_0=1\).  Then

\[
kx=0\pmod N
\iff N_0\mid k_0x
\iff N_0\mid x,
\]

because \(\gcd(k_0,N_0)=1\).  The solutions are precisely

\[
x=jN_0,\qquad 0\le j<d.
\]

Thus the fibre has size \(\gcd(k,N)\), and therefore

\[
|\Omega_N|=S(N):=\sum_{k\bmod N}\gcd(k,N),
\qquad
\Pr(k)=\frac{\gcd(k,N)}{S(N)}
\]

under the uniform law on \(\Omega_N\).  This part holds for every positive
\(N\), including even integers and prime powers.

For odd \(N\), the change of variables
\((y,z)\mapsto(u,v)=(y-z,y+z)\) is bijective modulo \(N\), and hence

\[
\left|\sum_{y\bmod N}e^{2\pi i k y^2/N}\right|^2
=\sum_{u,v\bmod N}e^{2\pi i kuv/N}
=N\gcd(k,N).
\]

The marginal is consequently the normalized quadratic Fourier-energy law.
The oddness restriction belongs only to this Fourier identification, not to
the positive fibre count.

CRT gives the structural bijection

\[
\Omega_N\cong\prod_{r^e\parallel N}\Omega_{r^e}.
\]

For a field component,

\[
\Omega_r=(\mathbb F_r\times\{0\})
\cup(\{0\}\times\mathbb F_r),
\]

with intersection \(\{(0,0)\}\), so \(|\Omega_r|=2r-1\).  The amendment
correctly warns that this literal two-axis description fails over
\(\mathbb Z/r^e\mathbb Z\) for \(e\ge2\): with the usual convention for
the valuation of zero, the condition is
\(v_r(k)+v_r(x)\ge e\), and for example
\((r,r^{e-1})\in\Omega_{r^e}\) has both coordinates nonzero.

### Residual squarefree-axis counterexample

Let \(N=pq\) with distinct primes.  Choose \(k\) by CRT so that

\[
k\equiv0\pmod p,
\qquad
k\equiv1\pmod q,
\]

and take \(x=0\).  Then \((k,0)\in\Omega_N\) and
\(\gcd(k,N)=p\), so the state exposes a factor.  Locally, however, the two
components are

\[
(k_p,x_p)=(0,0),
\qquad
(k_q,x_q)=(1,0).
\]

Both lie on the horizontal axis; the first lies on both axes.  Thus factor
exposure does not force disagreement under a common-axis interpretation.
If one instead arbitrarily labels the origin as horizontal or vertical, that
label is not part of the sampled state.  Indeed the global state \((0,0)\),
which exposes no proper gcd, could be assigned different labels at \(p\) and
\(q\).  Therefore the word “precisely” cannot be retained with “chosen
axes.”

The three local types \(H,V,O\) remove the ambiguity.  The non-factor-bearing
states have types \((H,H)\), \((V,V)\), or \((O,O)\); every unequal pair of
types exposes at least one proper gcd.  No later proof relies on the flawed
axis wording.

## 2. Exact non-factor-bearing set

For every composite \(N\), define

\[
A_N=\{(k,x)\in\Omega_N:
\gcd(k,N),\gcd(x,N)\in\{1,N\}\}.
\]

A residue has gcd \(1\) exactly when it is a unit and gcd \(N\) exactly
when it is zero modulo \(N\).  Since a product of two units is a unit, two
units cannot have zero product.  A unit in one coordinate forces the other
coordinate to be zero.  Hence the disjoint decomposition

\[
A_N=
((\mathbb Z/N\mathbb Z)^\times\times\{0\})
\mathbin{\dot\cup}
(\{0\}\times(\mathbb Z/N\mathbb Z)^\times)
\mathbin{\dot\cup}\{(0,0)\}
\]

is exact, and

\[
|A_N|=2\varphi(N)+1.
\]

Its complement is exactly the event that inspection of one of the two gcds
returns a divisor strictly between \(1\) and \(N\).  This statement includes
prime powers, repeated factors, and nonsquarefree composites.

## 3. Proper-factor mass for every odd composite

Write

\[
N=\prod_{i=1}^t p_i^{e_i},
\qquad b_i=1-\frac1{p_i}.
\]

Prime-power counting and multiplicativity give

\[
\frac{S(N)}N=\prod_i(1+e_i b_i),
\qquad
\frac{\varphi(N)}N=\prod_i b_i.
\]

The useful mass is at least \(1/3\) exactly when

\[
\frac{2\varphi(N)+1}{S(N)}\le\frac23.
\]

### 3.1 Odd prime powers

For \(N=p^e\), \(p\ge3\), \(e\ge2\), and \(b=1-1/p\), the
non-useful mass is

\[
R_e=\frac{2b+p^{-e}}{1+eb}.
\]

The inequality \(R_e\le2/3\) is equivalent to

\[
2+(2e-6)b-3p^{-e}\ge0.
\]

For \(e=2\), the left side is \((2p-3)/p^2>0\).  For \(e=3\), it
is \(2-3p^{-3}>0\).  For \(e\ge4\), it increases with \(e\).  Thus no
prime-power promise is hidden.  Along \(p^2\), the useful mass tends to
\(1/3\), so the constant is asymptotically sharp.

### 3.2 At least two distinct odd primes

Choose two distinct prime divisors and order their values so that

\[
b_1\ge\frac23,
\qquad
b_2\ge\frac45.
\]

Extra exponents increase \(S(N)/N\) and leave \(\varphi(N)/N\)
unchanged; extra distinct primes increase the former and decrease the latter.
Also

\[
\frac1N\le(1-b_1)(1-b_2).
\]

Consequently

\[
\frac{2\varphi(N)+1}{S(N)}
\le
\frac{2b_1b_2+(1-b_1)(1-b_2)}
{(1+b_1)(1+b_2)}.
\]

After clearing the positive denominator, the right side is at most \(2/3\)
exactly when

\[
f(b_1,b_2):=1-5b_1-5b_2+7b_1b_2\le0.
\]

This bilinear function attains its maximum on the rectangle at a corner.  Its
four corner values are \(-13/5,-8/3,-12/5,-2\), all negative.  The
claimed universal \(1/3\) useful mass follows.

For \(N=pq\), \(p\ne q\), the exact formulas are

\[
S(N)=(2p-1)(2q-1),
\qquad
|A_N|=2(p-1)(q-1)+1,
\]

and

\[
S(N)-2|A_N|=2p+2q-5>0.
\]

Thus the useful mass is strictly greater than \(1/2\), as claimed.

## 4. Conditional all-input Las Vegas reduction

Assume one uniform sampler which, on every odd modulus \(M\ge3\) and
rational \(\delta>0\), always outputs an actual member of \(\Omega_M\),
has output law within total variation \(\delta\) of uniform, terminates
almost surely, and has one fixed expected polynomial bit and fair-bit bound
in \(\log M+\log\delta^{-1}\).

On an odd composite, use \(\delta=1/12\).  Total variation applied to the
factor-bearing event gives

\[
\Pr(\text{proper gcd})
\ge\frac13-\frac1{12}=\frac14.
\]

Both gcds are computed and any result is accepted only after checking
\(1<d<M\).  Hence every returned split is correct.

Fresh sampler invocations use fresh fair-bit streams.  If \(C_i\) is the
cost of call \(i\), then the event that call \(i\) is reached depends only
on earlier streams and is independent of \(C_i\).  It is not necessary for
one call's runtime to be independent of that same call's success.  If
\(P(n)\) bounds one call, then, conditionally on the current modulus,

\[
\mathbb E\!\left[\sum_{i\ge1}
\mathbf 1_{\{i\text{ reached}\}}C_i\right]
\le
\sum_{i\ge1}(3/4)^{i-1}P(n)
=4P(n).
\]

The same calculation bounds fair random bits, and the geometric success
bound gives almost-sure termination of each retry loop.

Deterministic primality testing handles prime nodes.  An even composite is
split directly by \(2\); an odd composite uses the retry loop; exact division
creates its two children.  If the final factorization has \(r\) prime leaves
counted with multiplicity, then \(2^r\le N\), so \(r< n\), and the binary
factor tree has at most \(2n-1\) nodes.  Every intermediate integer has at
most \(n\) bits.  Summing the uniform conditional bound over this
deterministically bounded number of nodes, together with polynomial-bit gcd,
division, primality testing, and bookkeeping, gives one fixed polynomial in
\(n\).  A finite collection of almost-sure loops terminates almost surely.

This correctly covers primes, powers of two, odd prime powers, repeated
factors, unbalanced composites, and arbitrary mixed inputs.

## 5. Equal-fibre perfect-matching hypothesis

The amended hypothesis now has the algorithmic quantifiers needed by the
reduction:

- one uniform polynomial-time builder outputs a polynomial-size unweighted
  bipartite graph \(G_N\) from the binary representation of every required
  modulus;
- one uniform deterministic decoder takes \(N\) and an explicit perfect
  matching and runs in time polynomial in \(\log N+|G_N|\);
- it outputs ordinary \(O(\log N)\)-bit residues forming a member of
  \(\Omega_N\); and
- every pair in \(\Omega_N\) has the same positive number \(c_N\) of
  matching preimages.

If \(U_N\) is uniform on the perfect matchings and \(D_N\) is the decoder,
then

\[
\Pr(D_N(U_N)=\omega)
=\frac{c_N}{c_N|\Omega_N|}
=\frac1{|\Omega_N|}.
\]

The value \(c_N\) need not be known or computed.  Total variation contracts
under a deterministic map, so a matching sample within \(1/12\) of uniform
decodes to a pair sample within \(1/12\) of uniform.  The promoted P38
interface supplies an actual perfect matching, almost-sure termination, and
expected polynomial bit and fair-bit cost for a polynomial-size bipartite
graph.  Composing the builder, matching sampler, and amended decoder therefore
meets the sampler hypothesis in Section 4.

No factorization, CRT decomposition, or normalizer is called by this
reduction.  The graph hypothesis is conditional and no such graph is
constructed in F33; consequently F33 is not an unconditional factoring
algorithm.  Uniformity of the builder and decoder is essential and is now
present.

## 6. Exact annihilator sampling and bit complexity

For \(y\bmod N\), let \(g=\gcd(y,N)\).  Writing \(N=gN_0\) shows

\[
\operatorname{Ann}_N(y)
=\{jN_0:0\le j<g\}.
\]

The displayed values are distinct modulo \(N\), so sampling a uniform
\(j\in\{0,\ldots,g-1\}\) samples the annihilator exactly; enumeration is
unnecessary.

For \(g=1\), output \(j=0\) without randomness.  For \(g\ge2\), let
\(\ell=\lceil\log_2 g\rceil\), draw an \(\ell\)-bit integer \(J\), and
accept exactly when \(J<g\).  Each round accepts with probability

\[
\frac{g}{2^\ell}\ge\frac12.
\]

The number of rounds is geometric, is finite almost surely, and has
expectation at most \(2\).  Thus the expected number of fair bits is at most
\(2\ell=O(\log N)\).  Each round uses an \(O(\log N)\)-bit comparison.
Euclid's algorithm, exact division \(N/g\), and multiplication by \(j\) all
have polynomial bit cost on \(O(\log N)\)-bit operands; in fact
\(j(N/g)<N\).  Including the coordinate-choice bit, one transition therefore
terminates almost surely and has expected polynomial bit and
\(O(\log N)\) fair-bit cost.

There is no hidden factoring call.  Computing \(g\) is an ordinary gcd.  If
\(1<g<N\), it is already the intended proper divisor.  Before a
factor-bearing state is reached, every inspected coordinate has gcd \(1\) or
\(N\), so its update is respectively forced to zero or is an ordinary exact
uniform-residue sample.  The unknown prime factors are not used to implement
the kernel.

The candidate's phrase “polynomial bit time” should be read and rewritten as
“expected polynomial bit time”; fair-bit rejection has no deterministic
worst-case round bound.

## 7. Random-scan heat-bath kernel

The audited kernel is exactly the following: choose one coordinate with
probability \(1/2\), then resample it uniformly from the annihilator of the
other coordinate.  Under the uniform law on \(\Omega_N\), this is the exact
conditional distribution of that coordinate.

For two distinct states differing only in \(k\), the transition probability
in either direction is

\[
\frac1{2|\operatorname{Ann}_N(x)|},
\]

and analogously for states differing only in \(x\).  States differing in
both coordinates have zero transition probability in both directions.
Detailed balance with the uniform law follows.

The chain is irreducible: from \((k,x)\), update \(k\) to zero, update
\(x\) arbitrarily from \(\operatorname{Ann}_N(0)\), and then update \(k\)
to any value compatible with the chosen \(x\).  Each move has positive
probability.  Every state has a self-loop because its current coordinate is
in the relevant annihilator.  Thus the chain is aperiodic and the uniform
stationary law is unique.

## 8. Exact semiprime hitting lower bound

Now restrict to \(N=pq\) for distinct odd primes and let

\[
h_N=N-\varphi(N)-1=p+q-2.
\]

This is exactly the number of nonzero nonunits, equivalently the number of
residues having a proper gcd with \(N\).  The complement of \(A_N\) is
exactly the factor-bearing set.

From \((u,0)\) with \(u\) a unit, an \(x\)-update is forced to remain zero,
whereas a \(k\)-update is uniform modulo \(N\).  The one-step exit
probability is therefore \(h_N/(2N)\).  The other unit axis is symmetric.
At \((0,0)\), either selected coordinate is uniform, so the exit probability
is \(h_N/N\).  Conditional on any history that has stayed in \(A_N\), the
next-step exit hazard is at most \(h_N/N\).

Start at the explicitly stated, factor-free state \((1,0)\), and put

\[
T=\min\{t\ge1:X_t\notin A_N\}.
\]

No independence is needed for the conditional union bound

\[
\Pr(T\le t)\le\frac{t h_N}{N}.
\]

With \(m=\lfloor N/(2h_N)\rfloor\),

\[
\mathbb ET
=\sum_{t\ge0}\Pr(T>t)
\ge\sum_{t=0}^{m}\left(1-\frac{t h_N}{N}\right)
\ge\frac{m+1}{2}
>\frac{N}{4h_N}.
\]

Thus

\[
\mathbb ET=\Omega\!\left(\frac{N}{p+q}\right)
\]

with an absolute constant.  Neither \(p\), \(q\), nor \(h_N\) is used by
the transition algorithm; they occur only in the lower-bound analysis.

## 9. Exact mixing lower bound and its scope

For a distinct semiprime, stationarity gives

\[
\pi(A_N)
=\frac{2(p-1)(q-1)+1}{(2p-1)(2q-1)}
<\frac12.
\]

Let

\[
L=\left\lfloor\frac{N}{8h_N}\right\rfloor.
\]

For every \(t\le L\), the hitting bound implies

\[
\Pr_{(1,0)}(X_t\in A_N)
\ge\Pr(T>t)\ge\frac78.
\]

Using \(A_N\) as a total-variation witness,

\[
\|P^t((1,0),\cdot)-\pi\|_{\mathrm{TV}}
\ge\Pr(X_t\in A_N)-\pi(A_N)
>\frac38.
\]

Therefore the standard worst-start mixing time satisfies

\[
t_{\mathrm{mix}}(1/4)>L,
\]

which is stronger than the candidate's stated
\(t_{\mathrm{mix}}(1/4)\ge L\).  If
\(p\le q\le\kappa p\) for fixed \(\kappa\), then
\(h_N=\Theta_\kappa(\sqrt N)\); after the harmless floor for sufficiently
large family members, both hitting and mixing lower bounds are
\(\Omega_\kappa(\sqrt N)\), exponential in the binary input length.

The quantifiers are now correctly limited:

- the hitting theorem starts from \((1,0)\);
- the mixing theorem is a worst-start theorem witnessed by \((1,0)\);
- the kernel is the exact random-scan, one-coordinate heat bath above;
- the lower bound is proved for distinct odd semiprimes, with the exponential
  conclusion restricted to fixed-balance families; and
- it does not rule out an efficiently generated warm start, a block update,
  a nonlocal or state-dependent proposal, an augmented state space, or any
  modified kernel.

Thus the prior route-closing overstatement is repaired.

## 10. Hidden-assumption audit

- **No squarefree promise in the positive reduction.**  The useful-mass
  theorem treats odd prime powers separately and then all integers with at
  least two distinct odd primes.  Squarefreeness occurs only in the stated
  semiprime lower bound.
- **No factorization in CRT usage.**  CRT is used to describe the state space,
  not to implement the sampler or transition.
- **No hidden normalizer.**  \(S(N)\) occurs in counting and stationarity
  proofs.  Neither the annihilator transition nor the conditional matching
  sampler computes it.
- **No hidden factor in annihilator sampling.**  Only \(\gcd(y,N)\), exact
  division, multiplication, comparison, and fair-bit rejection are used.  A
  proper gcd is the desired success event.
- **No nonuniform matching advice.**  The amended hypothesis requires one
  uniform builder and one uniform efficient decoder.  Equal fibre size is a
  mathematical property, not an input supplied to the algorithm.
- **No independence error in stopped cost.**  Fresh-call cost is independent
  of the event that the call is reached; it need not be independent of its
  own output.
- **No all-input gap.**  Deterministic primality testing and even splitting,
  followed by verified recursive splits, cover primes, even inputs, prime
  powers, repeated factors, and arbitrary composites within \(O(n)\) tree
  nodes.
- **No broad sampler lower bound.**  Only the stated random-scan kernel and
  worst start are proved slow.  The amended open-route list respects this
  boundary.

## Final assessment

Equations (0.1)--(0.7) and every substantive algorithmic or probabilistic
claim supporting them are correct.  The matching result remains explicitly
conditional, so F33 does not itself solve factoring.  After replacing the
origin-ambiguous axis equivalence by the exact \(H/V/O\) type criterion and
making the rejection runtime's expectation/almost-sure quantifiers explicit,
the amended candidate would pass this re-audit.  The present text is
nevertheless **FAIL AS WRITTEN** because its claimed precise squarefree-axis
interpretation is false/undefined on states having a local origin.
