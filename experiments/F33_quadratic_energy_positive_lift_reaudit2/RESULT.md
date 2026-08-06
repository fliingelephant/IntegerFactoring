# Second hostile re-audit of amended F33: quadratic-energy positive lift

**Artifact audited:**
`experiments/F33_quadratic_energy_positive_lift_kill/RESULT.md`, including the
live amendments replacing the residual hidden-axis wording by exact local-type
wording.

**Historical material read in full:** both prior failed audits,
`experiments/F33_quadratic_energy_positive_lift_audit/RESULT.md` and
`experiments/F33_quadratic_energy_positive_lift_reaudit/RESULT.md`.

**Protocol:** hostile proof-only audit of the entire current artifact from the
definitions.  I also checked the imported P38 and P41 interfaces in
`PROVED.md`.  No computation was used.

## Verdict

> **PASS AS WRITTEN.**

The current artifact repairs both rounds of prior objections.  In particular:

- the literal two-axis description is restricted to prime-field CRT
  components and explicitly excludes prime-power valuation strata;
- the new \(H/V/O\) criterion is exact in every case, including cases where
  either or both local components are origins;
- no surviving axis wording assigns an axis choice to an origin or is used as
  an equivalence with factor exposure;
- the matching bridge now requires a uniform polynomial-time decoder with
  ordinary short residue outputs;
- fair-bit annihilator rejection is explicitly stated to terminate almost
  surely and to have expected, rather than worst-case, polynomial bit cost;
  and
- the lower-bound conclusion is restricted to the exact starts and kernels
  actually analyzed, while new warm starts and modified kernels remain open.

I found no new counterexample or unsupported substantive claim.  This pass is
for the current version only; the two failures remain valid historical
verdicts on their respective older versions.

F33 remains a positive representation, a conditional factoring reduction,
and a lower bound for one sampler.  It does not construct the missing sampler
or matching graph and therefore does not by itself solve the top-level
factoring problem.

## 1. Exact positive lift and Fourier identification

Let

\[
\Omega_N=\{(k,x)\in(\mathbb Z/N\mathbb Z)^2:kx=0\}.
\]

For fixed \(k\), put \(d=\gcd(k,N)\), \(k=dk_0\), and \(N=dN_0\).  This
also covers \(k=0\), when \(d=N\) and \(N_0=1\).  Then

\[
kx=0\pmod N
\iff N_0\mid k_0x
\iff N_0\mid x,
\]

because \(\gcd(k_0,N_0)=1\).  The solutions are precisely

\[
x=jN_0,\qquad 0\le j<d.
\]

They are distinct modulo \(N\), so the fibre has exactly \(d=\gcd(k,N)\)
members.  Therefore

\[
|\Omega_N|=S(N):=\sum_{k\bmod N}\gcd(k,N),
\qquad
\Pr(k)=\frac{\gcd(k,N)}{S(N)}
\]

under the uniform pair law.  This proof is valid for every positive \(N\),
including even integers and prime powers.

For odd \(N\), if

\[
G_N(k)=\sum_{y\bmod N}e^{2\pi i k y^2/N},
\]

then the change of variables \(u=y-z,\ v=y+z\) is invertible modulo \(N\).
Consequently

\[
|G_N(k)|^2
=\sum_{u,v\bmod N}e^{2\pi i kuv/N}
=N\,\#\{u:ku=0\pmod N\}
=N\gcd(k,N).
\]

Thus the first marginal is exactly the normalized quadratic Fourier-energy
law.  The candidate correctly confines oddness to this Fourier
identification; the positive lift itself has no oddness restriction.

CRT acts componentwise on both coordinates and on multiplication, giving

\[
\Omega_N\cong\prod_{r^e\parallel N}\Omega_{r^e}.
\]

For a prime \(r\), zero product in the field forces one coordinate to vanish,
so

\[
\Omega_r=(\mathbb F_r\times\{0\})
\cup(\{0\}\times\mathbb F_r),
\qquad |\Omega_r|=2r-1.
\]

The text now calls these literal coordinate axes only at prime-field
components and says that their common origin has no intrinsic axis choice.
It separately records the prime-power condition
\(v_r(k)+v_r(x)\ge e\), including intermediate strata such as
\((r,r^{e-1})\).  Hence the prime-power counterexample from the first audit is
now handled rather than silently forced into an axis picture.

## 2. The \(H/V/O\) criterion is exact, including origins

For \(N=pq\) with distinct primes, every local zero-product pair has exactly
one of the disjoint types

\[
H=\mathbb F_r^\times\times\{0\},\qquad
V=\{0\}\times\mathbb F_r^\times,\qquad
O=\{(0,0)\}.
\]

The disjointness is essential: the origin is type \(O\), not an arbitrarily
chosen copy of \(H\) or \(V\).

If the two CRT components have types \((H,H)\), then \(k\) is a unit and
\(x=0\pmod N\).  For \((V,V)\), \(k=0\pmod N\) and \(x\) is a unit.  For
\((O,O)\), both coordinates are zero.  In all three equal-type cases, both
gcds belong to \(\{1,N\}\), so neither exposes a proper factor.

Every unequal-type case exposes a proper factor:

- for \((H,V)\) or \((V,H)\), both coordinates vanish at exactly one of
  \(p,q\), so both gcds are proper;
- for \((H,O)\) or \((O,H)\), \(k\) vanishes at exactly one prime while
  \(x=0\pmod N\), so \(k\) exposes a proper gcd; and
- for \((V,O)\) or \((O,V)\), the symmetric statement holds for \(x\).

This exhausts all nine ordered type pairs.  It also disposes of the prior
counterexample: if locally one sees \((0,0)\) at one prime and
\((1,0)\) at the other, the types are \(O,H\), not two artificially
horizontal choices, and the criterion correctly predicts a proper gcd.
The global origin has types \((O,O)\) and correctly predicts no proper gcd.

The remaining uses of “axis” do not revive the error.  “Unit axis” in the
heat-bath proof denotes the literal global states \((u,0)\) or \((0,u)\).
The open-route bullet about an augmented space joining local axes is
explicitly hypothetical and refers to the literal prime-field coordinate
sets; it neither labels an origin nor states a factor-exposure equivalence.
The substantive obstruction and the closing summary now use unequal
\(H/V/O\) types.  There is no residual axis-choice overclaim.

## 3. Exact non-factor-bearing set and useful mass

For every composite \(N\), a residue has gcd \(1\) with \(N\) exactly when
it is a unit and gcd \(N\) exactly when it is zero modulo \(N\).  A unit in
one coordinate of a zero-product pair forces the other coordinate to be
zero.  Therefore the set on which neither coordinate exposes a proper gcd is
exactly

\[
A_N=
((\mathbb Z/N\mathbb Z)^\times\times\{0\})
\mathbin{\dot\cup}
(\{0\}\times(\mathbb Z/N\mathbb Z)^\times)
\mathbin{\dot\cup}\{(0,0)\},
\]

and

\[
|A_N|=2\varphi(N)+1.
\]

This identity does not assume squarefreeness and is valid for prime powers,
repeated factors, and arbitrary composites.

Writing

\[
N=\prod_i p_i^{e_i},\qquad b_i=1-\frac1{p_i},
\]

prime-power counting gives

\[
\frac{S(N)}N=\prod_i(1+e_i b_i),
\qquad
\frac{\varphi(N)}N=\prod_i b_i.
\]

For an odd prime power \(N=p^e\), \(e\ge2\), the non-useful mass is

\[
R_e=\frac{2b+p^{-e}}{1+eb}.
\]

The inequality \(R_e\le2/3\) is equivalent to

\[
(6-2e)b+3p^{-e}\le2.
\]

For \(e=2\) this is
\(2(1-1/p)+3/p^2\le2\); for \(e=3\) it is
\(3/p^3\le2\); and the left side decreases thereafter.  Thus the
prime-power case is complete.  Along \(p^2\), \(R_2\to2/3\), so the
useful \(1/3\) bound is asymptotically sharp.

If there are at least two distinct odd prime factors, choose two and order
their values so that

\[
b_1\ge\frac23,\qquad b_2\ge\frac45.
\]

Extra exponents increase \(S(N)/N\) and leave \(\varphi(N)/N\) unchanged;
extra distinct primes increase the former and decrease the latter.  Also
\(1/N\le(1-b_1)(1-b_2)\).  Hence

\[
\frac{2\varphi(N)+1}{S(N)}
\le
\frac{2b_1b_2+(1-b_1)(1-b_2)}
{(1+b_1)(1+b_2)}.
\]

The right side is at most \(2/3\) exactly when

\[
1-5b_1-5b_2+7b_1b_2\le0.
\]

This bilinear function is negative at all four corners of
\([2/3,1]\times[4/5,1]\), so it is nonpositive throughout.  Therefore

\[
\Pr_{\mathrm{Unif}(\Omega_N)}
(\Omega_N\setminus A_N)\ge\frac13
\]

for every odd composite, with no balance, squarefreeness, or smoothness
promise.

For \(N=pq\), multiplicativity and the exact \(A_N\) count give

\[
S(N)=(2p-1)(2q-1),\qquad
|A_N|=2(p-1)(q-1)+1.
\]

Moreover \(S(N)-2|A_N|=2p+2q-5>0\), so the useful mass is strictly greater
than \(1/2\).  All mass claims in the candidate are correct.

## 4. Conditional pair sampler gives all-input Las Vegas factoring

Assume the stated uniform sampler.  On an odd composite, total variation
with \(\delta=1/12\) gives

\[
\Pr(\text{at least one verified proper gcd})
\ge\frac13-\frac1{12}=\frac14.
\]

Every accepted divisor is checked to satisfy \(1<d<M\), so every returned
split is correct.

Fresh invocations use fresh fair-bit streams.  If \(C_i\) is the cost of
call \(i\), the event that call \(i\) is reached depends only on earlier
streams and is therefore independent of \(C_i\); no independence between
\(C_i\) and call \(i\)'s own success is needed.  If \(P(n)\) bounds one
call, then

\[
\mathbb E\!\left[\sum_{i\ge1}
\mathbf1_{\{i\text{ reached}\}}C_i\right]
\le\sum_{i\ge1}(3/4)^{i-1}P(n)
=4P(n).
\]

The same argument bounds expected fair bits.  The geometric tail also proves
almost-sure termination of each retry loop.

Deterministic primality testing handles prime nodes, even composites split by
\(2\), and odd composites use the sampler.  Exact division creates the two
children.  If there are \(r\) prime leaves counted with multiplicity, then
\(2^r\le N\), so \(r<n\), and the binary factor tree has at most \(2n-1\)
nodes.  All intermediate integers have at most \(n\) bits.  Gcd, division,
primality testing, factor verification, collection of repeated leaves into
prime powers, and output bookkeeping are polynomial-bit operations.  A
deterministically bounded number of almost-sure loops is almost surely
finite, and summing their conditional expectations gives one fixed
polynomial in \(n\).

Thus the candidate's reduction covers primes, powers of two, odd prime
powers, repeated factors, unbalanced composites, and arbitrary mixed inputs,
with both expected bit/fair-bit cost and almost-sure termination.

## 5. Equal-fibre matching decoder

The amended matching hypothesis is sufficient.  One uniform polynomial-time
builder outputs a polynomial-size unweighted bipartite graph \(G_N\), and one
uniform deterministic algorithm decodes every explicit perfect matching in
time polynomial in \(\log N+|G_N|\) to two ordinary \(O(\log N)\)-bit
residues in \(\Omega_N\).  If every pair has the same positive number
\(c_N\) of preimages, then

\[
|\operatorname{PM}(G_N)|=c_N|\Omega_N|
\]

and uniform perfect matchings push forward exactly to uniform zero-product
pairs.  The value \(c_N\) need not be known.  Total variation contracts
under deterministic decoding, so an almost-uniform matching sample gives an
equally accurate pair sample.

The promoted P38 interface supplies, for a polynomial-size graph with a
perfect matching, an actual perfect matching within the needed total
variation error, with almost-sure termination and expected polynomial bit
and fair-bit cost.  Positive equal fibres ensure that such matchings exist.
Composing builder, sampler, and decoder therefore meets the fixed-accuracy
pair-sampling interface used by the factoring reduction.

The graph is only a hypothesis; no construction is claimed.  There is no
hidden decoder complexity, nonuniform advice, unknown normalizer, or implicit
factorization in this conditional bridge.

## 6. Heat bath, exact annihilator rejection, and kernel properties

For \(y\bmod N\), with \(g=\gcd(y,N)\), the same fibre argument gives

\[
\operatorname{Ann}_N(y)
=\left\{j\frac Ng:0\le j<g\right\}.
\]

These \(g\) residues are distinct.  For \(g\ge2\), set
\(\ell=\lceil\log_2g\rceil\), draw an \(\ell\)-bit integer, and reject it
when it is at least \(g\).  Each round succeeds with probability at least
\(1/2\), so the number of rounds is finite almost surely and has expectation
at most \(2\).  For \(g=1\), the unique value \(j=0\) is returned without
random bits.  Therefore annihilator sampling is exact, terminates almost
surely, uses expected \(O(\log N)\) fair bits, and has expected polynomial
bit cost.  Euclid, exact division, multiplication, and comparison operate on
\(O(\log N)\)-bit integers, with \(jN/g<N\).

This verifies the precise repair requested by the preceding re-audit: the
current candidate explicitly says “terminates almost surely,” “expected
\(O(\log N)\) fair bits,” and “expected polynomial bit time.”  It does not
claim a deterministic runtime bound for an unbounded rejection loop.

No factor oracle is hidden.  If \(1<g<N\), the ordinary gcd computation has
already found the desired factor.  Before a semiprime chain reaches a
factor-bearing state, every coordinate has gcd \(1\) or \(N\), so an update
is respectively forced to zero or is an ordinary exact uniform-residue
sample.

The random-scan update is the exact conditional heat bath for the uniform
law on \(\Omega_N\).  Two distinct states differing only in \(k\), with
common \(x\), have transition probability

\[
\frac1{2|\operatorname{Ann}_N(x)|}
\]

in either direction; the \(x\)-case is symmetric.  Detailed balance with
uniform measure follows.  The chain is irreducible: set \(k\) to zero, sample
an arbitrary target \(x'\) from \(\operatorname{Ann}_N(0)\), then sample any
compatible target \(k'\).  Every state has a positive self-loop because its
current coordinate belongs to the relevant annihilator.  Hence the chain is
aperiodic and has the stated uniform stationary law.

## 7. Hitting and mixing lower bounds

Now let \(N=pq\) for distinct odd primes and

\[
h_N=N-\varphi(N)-1=p+q-2.
\]

This is exactly the number of nonzero nonunits, hence the number of residues
with a proper gcd.  From \((u,0)\), where \(u\) is a unit, the \(x\)-update
is forced and a \(k\)-update is uniform, so the one-step exit probability
from \(A_N\) is \(h_N/(2N)\).  The other unit axis is symmetric.  From
\((0,0)\), either chosen coordinate is uniform, giving exit probability
\(h_N/N\).  Thus, conditional on any entire history that has stayed in
\(A_N\), the next-step exit hazard is at most \(h_N/N\).

Starting from the explicit factor-free state \((1,0)\), let \(T\) be first
entrance into \(\Omega_N\setminus A_N\).  A conditional union bound, requiring
no independence between steps, yields

\[
\Pr(T\le t)\le\frac{t h_N}{N}.
\]

For \(m=\lfloor N/(2h_N)\rfloor\), every retained tail term is at least
\(1/2\), and

\[
\mathbb ET
\ge\sum_{t=0}^{m}\left(1-\frac{t h_N}{N}\right)
=\Omega\!\left(\frac N{h_N}\right)
=\Omega\!\left(\frac N{p+q}\right).
\]

For

\[
t\le L:=\left\lfloor\frac{N}{8h_N}\right\rfloor,
\]

the time-\(t\) law places at least \(7/8\) on \(A_N\), whereas stationarity
places strictly less than \(1/2\) there.  The set \(A_N\) therefore witnesses
total-variation distance greater than \(3/8\).  The standard worst-start
\(1/4\)-mixing time is in fact greater than \(L\), so the candidate's weaker
stated bound \(t_{\rm mix}(1/4)\ge L\) is valid, including its harmless
time-zero/floor convention.

If \(p\le q\le\kappa p\), then
\(h_N=\Theta_\kappa(\sqrt N)\), and both bounds are
\(\Omega_\kappa(\sqrt N)\), exponential in the binary input length.  The
balance assumption is used only for this final asymptotic conversion, not
for the exact semiprime hitting or mixing inequalities.

## 8. Hidden assumptions, scope, and counterexample search

- The positive lift and the \(A_N\) identity cover even integers and
  nonsquarefree moduli.  Oddness is used only for Fourier identification and
  for the sampler reduction after even splitting.
- Prime powers are handled in the mass theorem and all-input recursion.  They
  are expressly excluded from the literal local-axis geometry, where their
  intermediate valuation strata would be counterexamples.
- CRT is descriptive only.  Neither the pair reduction nor the heat-bath
  transition receives unknown prime factors or a CRT decomposition.
- \(S(N)\) and \(\varphi(N)\) appear only in proofs.  No algorithm computes a
  hidden normalizer.
- Every successful gcd is verified, and a proper gcd is the desired output,
  not an illicit factoring subroutine.
- The matching construction is explicitly conditional and uniformly
  algorithmic; the equal multiplicity is a property, not advice supplied to
  the sampler.
- The stopped-cost proof does not assume a call's cost is independent of its
  own output.
- The lower bound is for the exact random-scan one-coordinate heat bath,
  with hitting from \((1,0)\) and worst-start mixing witnessed there.  It is
  not asserted for block, nonlocal, augmented-state, or modified kernels, nor
  for a new efficiently generated warm start.
- The final route-closing sentence explicitly limits F32 and F33 to the exact
  rejection/Metropolis/heat-bath procedures and starts analyzed there, then
  states that new initial laws and modified coordinate kernels are not
  covered.

I retested the earlier origin witness, the global origin, all unequal pairs
involving one local origin, the intermediate prime-power valuation witness,
the annihilator endpoints \(g=1,N\), the time-zero mixing convention, and the
runtime/output-correlation case.  Each is now either handled exactly or
explicitly outside the relevant claim.  No fresh counterexample survives.

## Final assessment

Every substantive claim in the current candidate survives this hostile
reconstruction: the positive lift, Fourier marginal, \(H/V/O\) criterion,
proper-factor mass, conditional matching decoder, all-input Las Vegas
reduction, exact fair-bit annihilator sampler, heat-bath stationarity,
hitting and mixing lower bounds, prime-power treatment, and stated scope.

Accordingly, the complete current artifact is **PASS AS WRITTEN**.
