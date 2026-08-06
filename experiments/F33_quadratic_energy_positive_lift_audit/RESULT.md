# Hostile audit of F33 — quadratic-energy positive lift

**Artifact audited:** experiments/F33_quadratic_energy_positive_lift_kill/RESULT.md.

**Protocol:** fresh proof-only hostile audit. No computation was used. I read
PROMPT.md, promoted P41 for the F32 dependency, promoted P38 for the matching
dependency, and only the narrow F30 audit material needed to check whether its
mention was being used as a premise.

## Verdict

> **FAILED AS WRITTEN, WITH THE CORE THEOREMS INTACT.**

The exact positive marginal, the count of non-factor-bearing pairs, the
universal \(1/3\) useful-pair mass, prime-square sharpness, distinct-semiprime
formulas, conditional all-input Las Vegas reduction, and coordinate
heat-bath hitting and mixing lower bounds are correct.

Three corrections are required before this exact version can pass:

1. The claim after (1.2) that the lifted state space “literally consists
   locally of two coordinate axes” is false for prime-power CRT components.
2. The positive-matching bridge does not explicitly require a uniformly
   polynomial-time decoder on every required modulus. A merely total decoder
   is insufficient for the algorithmic reduction.
3. The closing statement that the named chains are simply “covered” is
   broader than the proved start and kernel quantifiers. The report proves
   worst-start slow mixing for one exact heat-bath kernel and a hitting bound
   from \((1,0)\), immediately extensible to starts concentrated on \(A_N\).
   It does not rule out a new efficiently generated warm start or a modified
   coordinate-update scheme.

The first is a false structural interpretation, the second a missing
complexity quantifier, and the third a route-closing overstatement. None
invalidates equations (0.1)–(0.7).

## 1. Exact lift, count, and marginal

Fix \(k\bmod N\), put \(d=\gcd(k,N)\), and write \(k=dk_0\) and
\(N=dN_0\). Then

\[
kx\equiv0\pmod N
\iff N_0\mid k_0x
\iff N_0\mid x,
\]

because \(\gcd(k_0,N_0)=1\). The solutions are exactly

\[
x=jN_0,\qquad 0\le j<d.
\]

Thus the fibre over \(k\) has size \(\gcd(k,N)\), including \(k=0\).
Consequently

\[
|\Omega_N|=\sum_{k\bmod N}\gcd(k,N)=S(N),
\qquad
\Pr(k)=\frac{\gcd(k,N)}{S(N)}.
\]

For odd \(N\), promoted P41 proves

\[
\left|\sum_{y\bmod N}e^{2\pi i k y^2/N}\right|^2
=N\gcd(k,N),
\]

so the marginal is exactly the normalized quadratic Fourier-energy law.
The lift and fibre count themselves hold for even \(N\) as well.

CRT correctly gives

\[
\Omega_N\cong\prod_{p^e\parallel N}\Omega_{p^e},
\]

and for a prime \(p\),

\[
\Omega_p=(\mathbb F_p\times\{0\})
\cup(\{0\}\times\mathbb F_p),
\qquad |\Omega_p|=2p-1.
\]

### Required correction: prime-power geometry

The following two-axis interpretation is not valid for \(\Omega_{p^e}\)
when \(e\ge2\). For example,

\[
(p,p^{e-1})\in\Omega_{p^e},
\]

although both coordinates are nonzero modulo \(p^e\). In particular
\((p,p)\in\Omega_{p^2}\) is off both coordinate axes and both gcds reveal
\(p\). In general, \(\Omega_{p^e}\) has valuation strata
\(v_p(k)+v_p(x)\ge e\).

The report must restrict the literal two-axis picture to field components,
and its axis-switching interpretation to the distinct squarefree semiprime
case where the later lower bound actually uses it. Prime-power useful states
also arise from intermediate valuations, not from disagreement between
different prime CRT axes.

## 2. Pairs for which neither coordinate reveals a factor

For a residue \(y\bmod N\), \(\gcd(y,N)=1\) exactly when \(y\) is a unit,
and \(\gcd(y,N)=N\) exactly when \(y=0\bmod N\). Two units cannot have
zero product. A unit in either coordinate therefore forces the other
coordinate to be zero. Hence, for every composite \(N\),

\[
A_N=
\bigl((\mathbb Z/N\mathbb Z)^\times\times\{0\}\bigr)
\mathbin{\dot\cup}
\bigl(\{0\}\times(\mathbb Z/N\mathbb Z)^\times\bigr)
\mathbin{\dot\cup}\{(0,0)\},
\]

and

\[
|A_N|=2\varphi(N)+1.
\]

This is exact for prime powers, repeated factors, and arbitrary composites.
Its complement is precisely the event that at least one coordinate has gcd
strictly between \(1\) and \(N\).

## 3. Universal \(1/3\) useful-pair mass

Write

\[
N=\prod_{i=1}^t p_i^{e_i},
\qquad b_i=1-\frac1{p_i}.
\]

Promoted P41 supplies, and prime-power counting directly confirms,

\[
\frac{S(N)}N=\prod_i(1+e_i b_i),
\qquad
\frac{\varphi(N)}N=\prod_i b_i.
\]

Therefore the non-useful mass is

\[
\frac{|A_N|}{|\Omega_N|}
=\frac{2\varphi(N)+1}{S(N)}.
\]

### 3.1 Every odd prime power

If \(N=p^e\), \(p\ge3\), \(e\ge2\), and \(b=1-1/p\), this ratio is

\[
R_e=\frac{2b+p^{-e}}{1+eb}.
\]

The inequality \(R_e\le2/3\) is equivalent to

\[
2+(2e-6)b-3p^{-e}\ge0.
\]

For \(e=2\), the left side is \((2p-3)/p^2>0\). For \(e=3\), it is
\(2-3p^{-3}>0\). For \(e\ge4\), it only increases with \(e\).
Thus all odd prime powers are covered.

The candidate’s phrase that omitted factors “decrease”
\(\varphi(N)/N\) should say “do not increase”: increasing a prime exponent
leaves that ratio unchanged. This wording does not affect the proof.

Along \(N=p^2\),

\[
1-R_2
=1-\frac{2(1-1/p)+p^{-2}}{3-2/p}
\longrightarrow\frac13,
\]

so the constant \(1/3\) is asymptotically sharp.

### 3.2 At least two distinct odd primes

Choose two distinct prime factors and order their \(b\)-values so that

\[
b_1\ge\frac23,\qquad b_2\ge\frac45.
\]

Extra distinct primes multiply \(\varphi(N)/N\) by numbers below one, extra
exponents leave it unchanged, and all extras increase \(S(N)/N\). Also

\[
\frac1N\le(1-b_1)(1-b_2).
\]

It follows that

\[
\frac{2\varphi(N)+1}{S(N)}
\le
\frac{2b_1b_2+(1-b_1)(1-b_2)}
{(1+b_1)(1+b_2)}.
\]

After clearing the positive denominator, the assertion that the right side
is at most \(2/3\) is

\[
1-5b_1-5b_2+7b_1b_2\le0.
\]

The left side is bilinear and is negative at all four corners of
\([2/3,1]\times[4/5,1]\), so it is nonpositive throughout. Therefore,
for every odd composite,

\[
\Pr_{\mathrm{Unif}(\Omega_N)}
(\Omega_N\setminus A_N)\ge\frac13.
\]

No squarefreeness, balance, or number-of-prime-factors promise is hidden in
this inequality.

## 4. Distinct-semiprime formulas

For \(N=pq\), with \(p\ne q\) odd primes,

\[
S(N)=(2p-1)(2q-1),
\qquad
|A_N|=2(p-1)(q-1)+1.
\]

Moreover

\[
S(N)-2|A_N|=2p+2q-5>0.
\]

Hence

\[
\Pr(\Omega_N\setminus A_N)
=1-\frac{2(p-1)(q-1)+1}{(2p-1)(2q-1)}
>\frac12.
\]

The formulas and strict constant are exact.

## 5. TV error and all-input Las Vegas recursion

Assume the pair sampler exists uniformly for every odd modulus, always
returns a member of \(\Omega_M\), has TV error \(\delta\), terminates almost
surely, uses fresh independent fair-bit streams on fresh invocations, and
has one fixed expected polynomial bit and fair-bit bound in
\(\log M+\log\delta^{-1}\).

On an odd composite, with \(\delta=1/12\), total variation applied to the
factor-bearing event gives

\[
\Pr(\text{verified proper gcd})
\ge\frac13-\frac1{12}=\frac14.
\]

Runtime/output correlation within one call causes no gap. If \(C_i\) is the
cost of fresh call \(i\), the event that call \(i\) is reached depends only
on earlier independent call streams. Conditional on the current modulus,

\[
\mathbb E\!\left[
\sum_{i\ge1}\mathbf1_{\{i\text{ reached}\}}C_i
\right]
\le
\sum_{i\ge1}(3/4)^{i-1}\mathbb E C_i
\le4P(\log M+O(1)).
\]

The same argument separately bounds fair random bits; it never assumes that
a call’s own runtime is independent of its own success.

Deterministic primality testing prevents calls on primes. Even factors are
split directly. Every accepted gcd is checked to be strictly between \(1\)
and \(M\), and exact division produces the children. This handles prime
powers, repeated factors, unbalanced composites, and arbitrary inputs.

If the final factorization has \(r\) prime leaves counted with multiplicity,
then \(2^r\le N\), so \(r\le\log_2N<n\). The binary recursion tree has fewer
than \(2n-1\) nodes; every intermediate integer has at most \(n\) bits.
Gcd, division, verification, primality testing, and output bookkeeping are
polynomial-bit operations. A deterministically bounded finite collection of
almost-sure retry loops terminates almost surely. Summing conditional
expectations gives one fixed polynomial in \(n\).

Thus the conditional pair-sampler-to-complete-factoring theorem has the
claimed all-input, expected-bit, expected-fair-bit, and almost-sure
termination quantifiers.

## 6. Equal-fibre positive-matching bridge

Let \(\mathcal M(G_N)\) be the perfect matchings and let
\(D_N:\mathcal M(G_N)\to\Omega_N\) be a deterministic decoder. If every
pair has exactly \(c_N>0\) preimages, then

\[
|\mathcal M(G_N)|=c_N|\Omega_N|,
\]

so the uniform matching law pushes forward exactly to uniform on
\(\Omega_N\). The value \(c_N\) need not be known. Total variation contracts
under \(D_N\), so a matching law within \(1/12\) of uniform yields a pair law
within \(1/12\) of uniform. Promoted P38 supplies an actual almost-uniform
perfect matching, almost-sure termination, and expected polynomial bit and
fair-bit cost for a polynomial-size unweighted bipartite graph.

### Required correction: decoder complexity and domain

The candidate says only that a polynomial-time builder returns a graph “and
a total decoder.” Totality does not bound evaluation time. The reduction
needs the following explicit hypothesis:

> For every required odd modulus \(N\ge3\), one uniform algorithm constructs
> \(G_N\) in time polynomial in \(\log N\), and one uniform deterministic
> algorithm computes \(D_N(M)=(k,x)\) from \(N\) and an explicit perfect
> matching \(M\) in time polynomial in \(\log N+|G_N|\). The graph has size
> polynomial in \(\log N\), the decoded residues have ordinary
> \(O(\log N)\)-bit representations and lie in \(\Omega_N\), and all fibres
> have the same positive size \(c_N\).

A total but exponentially expensive decoder does not give polynomial-time
factoring. If “returns a decoder” was meant to imply an efficient circuit or
algorithm, that intent must be explicit. With this repair, P38 and TV
contraction prove the conditional bridge.

No such graph or decoder is constructed in F33. This remains a conditional
reduction, not a factoring algorithm.

## 7. Heat-bath stationarity, connectivity, and implementation

For \(y\bmod N\), let

\[
\operatorname{Ann}_N(y)=\{z:zy=0\bmod N\}.
\]

Under uniform measure on \(\Omega_N\), one coordinate conditioned on the
other is uniform on this annihilator. The proposed update is therefore the
exact random-scan Gibbs sampler.

If two distinct states differ only in \(k\), their transition probability in
either direction is

\[
\frac1{2|\operatorname{Ann}_N(x)|}.
\]

The symmetric statement holds for an \(x\)-update; states differing in both
coordinates have zero one-step probability in both directions. Detailed
balance with the uniform law follows.

The chain is irreducible. From \((k,x)\), update \(k\) to \(0\), update \(x\)
from \(\operatorname{Ann}_N(0)=\mathbb Z/N\mathbb Z\) to any desired \(x'\),
then update \(k\) to any desired
\(k'\in\operatorname{Ann}_N(x')\). Every move has positive probability.
Every state has a positive self-loop because its current coordinate belongs
to the relevant annihilator. The finite chain is therefore aperiodic, and
the uniform stationary law is unique.

With \(g=\gcd(y,N)\),

\[
\operatorname{Ann}_N(y)
=\left\{j\frac Ng:0\le j<g\right\}.
\]

Literal enumeration can be exponential in \(\log N\), so “can be listed” is
not the right complexity statement. Enumeration is unnecessary: compute
\(g\) by Euclid, draw uniform \(j\in\{0,\ldots,g-1\}\) by fair-bit rejection,
and output \(j(N/g)\bmod N\). This terminates almost surely, uses expected
\(O(\log N)\) fair bits, and has polynomial bit cost per transition. The
coordinate choice uses one fair bit.

If \(1<g<N\), the gcd has already produced the desired factor. If \(g=1\),
the update is forced to zero; if \(g=N\), the conditioning coordinate is zero
and the update is an ordinary uniform residue. Thus, up to the first
factor-bearing state on a semiprime, no factorization, CRT decomposition,
normalizer, or order-finding oracle is hidden in a transition. Replace the
misleading enumeration wording with this direct sampler.

## 8. Exit hazard and hitting time

Let \(N=pq\) for distinct odd primes and

\[
h_N=N-\varphi(N)-1=p+q-2.
\]

This is exactly the number of proper-gcd residues. Here \(A_N\) is the two
unit axes plus the origin, and its complement is exactly factor-bearing.

From \((u,0)\), with \(u\) a unit, the \(x\)-update is forced while the
\(k\)-update is uniform. The one-step exit probability is \(h_N/(2N)\).
The same holds on the other unit axis. From \((0,0)\), either coordinate is
uniform, so the exit probability is \(h_N/N\). Conditional on any history
still in \(A_N\), the next-step hazard is therefore at most \(h_N/N\).

Starting from \((1,0)\), let \(T\) be first entrance into the complement.
Without any independence assumption, a conditional union bound gives

\[
\Pr(T\le t)\le\frac{t h_N}{N}
\]

for every integer \(t\ge0\). Put
\(m=\lfloor N/(2h_N)\rfloor\). Then

\[
\mathbb ET
=\sum_{t\ge0}\Pr(T>t)
\ge\sum_{t=0}^{m}\left(1-\frac{t h_N}{N}\right)
\ge\frac{m+1}{2}
\ge\frac{N}{4h_N}.
\]

Thus the claimed \(\Omega(N/(p+q))\) lower bound has an absolute constant.

## 9. Stationary mass, TV constants, and mixing

For a distinct semiprime,

\[
\pi_{\mathrm{stat}}(A_N)
=\frac{2(p-1)(q-1)+1}{(2p-1)(2q-1)}
<\frac12.
\]

If

\[
t\le L:=\left\lfloor\frac{N}{8h_N}\right\rfloor,
\]

the hitting bound gives \(\Pr(X_t\in A_N)\ge7/8\). Using \(A_N\) as a TV
witness,

\[
\|\mathcal L(X_t)-\pi_{\mathrm{stat}}\|_{\mathrm{TV}}
\ge
\Pr(X_t\in A_N)-\pi_{\mathrm{stat}}(A_N)
>\frac38.
\]

Hence the worst-start \(1/4\)-mixing time is greater than \(L\), and in
particular

\[
t_{\mathrm{mix}}(1/4)
\ge
\left\lfloor\frac{N}{8(p+q-2)}\right\rfloor.
\]

If \(p\le q\le\kappa p\), then
\(p+q-2=\Theta_\kappa(\sqrt N)\), so both lower bounds are
\(\Omega_\kappa(\sqrt N)\), exponential in the binary input length. The
hazard, union bound, stationary mass, TV constants, floor convention, and
balance quantifier are all correct.

## 10. Hidden factoring and dependency status

- \(S(N)\) is used only in proofs. P41 records that exact \(S(pq)\) reveals
  \(p+q\), so computing it would hide semiprime factoring.
- CRT and prime-power decompositions are structural only. No transition uses
  unknown CRT factors.
- Computing \(\gcd(y,N)\) is ordinary polynomial-time arithmetic. A proper
  result is the intended successful output, not an illicit oracle call.
- The matching construction is hypothetical. Under the corrected
  hypothesis, its builder and decoder take only public inputs.
- P41 and P38 are promoted dependencies. F30 is not promoted in the material
  examined. F33 labels its AND/COPY observations as candidates, and they are
  not needed: P38 itself already preserves closed internal-edge and globally
  filtered graphs. F30 must remain a nonessential scope illustration until
  it completes its own verification cadence.
- F33 constructs neither the missing pair sampler nor the matching graph. It
  does not resolve the top-level factoring prompt.

## 11. Exact scope and open routes

For an arbitrary initial law \(\nu\), the same hazard proof gives

\[
\Pr_\nu(T\le t)
\le
\nu(\Omega_N\setminus A_N)+\frac{t h_N}{N}.
\]

Thus the argument also obstructs initializers concentrated on \(A_N\). It
does not prove that every efficiently generated initializer is concentrated
there. An initializer with constant complement mass would itself give a
constant-success factor sample when inspected; constructing one is a
positive route still missing, not something the lower bound refutes.

The terminal sentence must therefore say that the exact random-scan kernel is
covered under the proved worst-start or \(A_N\)-concentrated-start
conditions. Likewise P41 covers its specifically defined lazy
uniform-proposal independence-Metropolis chain and stated initializer
conditions, not every modification bearing that broad name.

The following remain open:

- augmented-state or defect chains;
- block, nonlocal, state-dependent, or otherwise modified proposals;
- a genuinely new efficiently samplable warm start for the coordinate chain;
- a polynomial-size positive matching graph with an efficient equal-fibre
  decoder;
- globally filtered internal-edge, block-code, auxiliary-state, or one-piece
  multiplication-specific matching constructions;
- a direct classical sampler outside chains on \(\Omega_N\); and
- other phase families or positive lifts with different connectivity.

After the three required corrections and the transition-wording
clarification, the surviving result is an exact positive representation and
an exact obstruction to one local sampler—not a broader sampler
impossibility theorem.
