# F15 follow-up — nonuniform Hurwitz coordinate slices and adaptive unit bias

**Status:** candidate, kill-first follow-up.  No hostile audit or proof-blind
reconstruction has run.

**Verdict:** the first concrete nonuniform sampler is killed twice.  Uniform
sampling from the integer-coordinate third of the norm shell still gives exactly
uniform local projective orientations, while its natural exact rejection sampler
needs \(\Theta(\sqrt N)\) trials on balanced semiprimes.  Moreover, an arbitrary
sample-dependent choice among a fixed polynomial-size menu of unit/conjugation
transforms cannot raise the one-sided-gcd collision probability above
\(\operatorname{poly}(\log N)/\sqrt N\).

One narrow survivor remains.  Starting from a single, possibly very biased,
norm-\(N\) quaternion \(\alpha\), randomizing only by the 24 right Hurwitz units
has an exact constant-success criterion: the two local \(A_4\)-stabilizers of
the row lines must differ.  This happens at \(N=15\) for one canonical
representation, but it already fails at \(N=39\).  No factor-free
expected-polynomial sampler is proved to land in the stabilizer-mismatch stratum
with inverse-polynomial probability.

## Prior-route check and material difference

The corrected F15 hostile audit and proof-blind reconstruction establish an
\(\Omega(N^{1/4})\) birthday scale for iid exact-uniform Hurwitz orientations.
They explicitly leave nonuniform samplers and sample-dependent transforms open.
This follow-up addresses that boundary rather than repeating the uniform-shell
calculation:

1. it replaces the full Hurwitz shell by a strict coordinate slice;
2. it specifies an exact factor-free sampler and audits its random-bit cost;
3. it permits the transform to depend arbitrarily on the sampled quaternion,
   provided it is selected from a bounded public menu; and
4. it isolates the exact finite-group criterion for the most concentrated
   same-source distribution, a single right-unit orbit.

No canonical file was edited.  The closest other routes in `FAILED.md` are F09,
which concerns cyclotomic orientation, and F12, which bounds fixed high-digit
probes.  Neither contains the integer-shell fibre theorem or the adaptive
finite-menu bound below.

## 1. The integer-coordinate shell is nonuniform but not orientation-biased

Let \(N=pq\), where \(p\ne q\) are odd primes, and use the corrected
normalization

\[
\mathcal H=\mathbb Z[i,j,(1+i+j+k)/2].
\]

Write

\[
S_N=\{\alpha\in\mathcal H:\operatorname{nrd}(\alpha)=N\},\qquad
L_N=S_N\cap(\mathbb Z+\mathbb Zi+\mathbb Zj+\mathbb Zk).
\]

Thus \(L_N\) is the integer-coordinate or Lipschitz slice.  Jacobi's formula
gives

\[
|L_N|=r_4(N)=8\sigma(N)=8(p+1)(q+1),
\]

whereas the corrected F15 count is

\[
|S_N|=24(p+1)(q+1).
\]

So this sampler is genuinely nonuniform on \(S_N\): it assigns zero mass to
two thirds of the shell.

### Exact fibre theorem

Nevertheless, uniform \(\alpha\in L_N\) has exactly uniform row-orientation
pair

\[
(R_p(\alpha),R_q(\alpha))\sim
\operatorname{Unif}(\mathbf P^1(\mathbb F_p)\times
                     \mathbf P^1(\mathbb F_q)).                 \tag{1}
\]

The same statement holds for image orientations.

To prove (1), start with the corrected F15 bijection between left-unit orbits in
\(S_N\) and projective-line pairs.  Every orbit has 24 elements.  It has exactly
eight elements in \(L_N\):

* at least one orbit member is integral, because an all-half-integral Hurwitz
  element of odd norm can be multiplied by a norm-one half-unit to make all four
  coordinates integral;
* the eight Lipschitz units
  \(Q_8=\{\pm1,\pm i,\pm j,\pm k\}\) preserve integrality and act freely; and
* if \(a+bi+cj+dk\) has odd norm, an odd number of \(a,b,c,d\) are odd.  On
  multiplying by any of the sixteen half-integral units, every resulting doubled
  coordinate is a signed sum of \(a,b,c,d\), hence odd.  The result is
  half-integral, not integral.

Each projective pair therefore has exactly eight preimages in \(L_N\), proving
(1).  The right-unit version proves the image assertion.

For two iid samples from this strict coordinate slice, a greatest common right
divisor consequently has exactly the same norm law as in corrected F15:

\[
\Pr(\operatorname{nrd}d_R=1,p,q,N)
=\frac{(pq,q,p,1)}{(p+1)(q+1)}.                 \tag{2}
\]

In particular, one pair succeeds with probability

\[
\delta_{p,q}=\frac{p+q}{(p+1)(q+1)},             \tag{3}
\]

and \(K\) samples with all-pairs testing succeed with probability at most
\(\binom K2\delta_{p,q}\).  On \(p<q<2p\), this is
\(O(K^2/\sqrt N)\).  Restricting to integral coordinates has manufactured no
useful orientation bias.

## 2. An exact factor-free sampler, with rebuilt random-bit cost

The following sampler uses only bare \(N\); no factors, exact-uniform-shell
oracle, or cited four-square algorithm are assumed.

Let \(B=\lfloor\sqrt N\rfloor\) and \(M=2B+1\).  Repeat:

1. draw \(a,b,c\) independently and exactly uniformly from \([-B,B]\);
2. compute \(h=N-a^2-b^2-c^2\), rejecting unless \(h=d_0^2\ge0\);
3. draw a fair bit.  If \(d_0>0\), use it to choose \(d=\pm d_0\).  If
   \(d_0=0\), accept on one bit value and reject on the other.

Every element of \(L_N\) is emitted with probability exactly
\(1/(2M^3)\) per trial.  Hence this is a Las Vegas exact-uniform sampler on
\(L_N\), and its expected number of trials is

\[
\frac{2M^3}{|L_N|}
=\frac{M^3}{4(p+1)(q+1)}.                       \tag{4}
\]

For balanced semiprimes, \(M=\Theta(\sqrt N)\) and
\((p+1)(q+1)=\Theta(N)\), so (4) is \(\Theta(\sqrt N)\).  This is exponential
in the input length.

The random-bit accounting does not hide another cost.  An exact uniform integer
in an interval of length \(M\) is obtained by rejection from
\(\lceil\log_2M\rceil\) fair bits with expected fewer than two bit blocks.
Each trial therefore uses \(O(\log N)\) expected random bits.  Squaring,
addition, comparison, and an integer-square-root test all have polynomial bit
cost on \(O(\log N)\)-bit operands.  Thus the exponential expected runtime is
precisely the \(\Theta(\sqrt N)\) acceptance loss, not an arithmetic-model
artifact.

This kills the displayed coordinate-slice sampler even before (3) is applied;
granting its samples for free still leaves the collision obstruction.

## 3. Sample-dependent selection from a bounded transform menu still fails

The previous F15 result treated fixed transforms and left arbitrary
sample-dependent selection open.  A useful part of that opening can be closed.

Let \(X\) be uniform on \(L_N\).  Let \(\mathcal T\) be any public family of
\(C\) maps, each of the form

\[
X\longmapsto aXb\quad\text{or}\quad X\longmapsto a\bar Xb,       \tag{5}
\]

where every fixed map is a bijection of \(L_N\) and induces a projective
bijection locally.  A selector may inspect all of \(X\) and choose
\(T_X\in\mathcal T\) arbitrarily; put \(Y=T_X(X)\).  Then for every local line
\(L\),

\[
\Pr(R_r(Y)=L)
\le \sum_{T\in\mathcal T}\Pr(R_r(TX)=L)
=\frac{C}{r+1}.                                  \tag{6}
\]

For unbarred maps, the equality uses uniform row orientation and a projective
right action; for barred maps it uses the corresponding uniform image
orientation.  No independence between the selector and \(X\) is assumed.

For iid outputs \(Y,Y'\), (6) gives

\[
\Pr(R_r(Y)=R_r(Y'))
=\sum_L\Pr(R_r(Y)=L)^2
\le \min\!\left(1,\frac{C}{r+1}\right).          \tag{7}
\]

Consequently a proper right gcd has probability at most

\[
\min\!\left(1,\frac{C}{p+1}\right)
+\min\!\left(1,\frac{C}{q+1}\right).            \tag{8}
\]

The all-pairs bound multiplies (8) by \(\binom K2\).  If both \(C\) and \(K\)
are polynomial in \(\log N\), the result remains exponentially small on an
infinite balanced family.

A concrete nonlinear example is **Q8 canonicalization**: choose the
lexicographically least coordinate tuple among

\[
\{uXv,\ u\bar Xv:u,v\in Q_8\}.                   \tag{9}
\]

The raw menu in (9) has \(C=128\) entries (at most 64 distinct maps).  The
choice depends on the complete sample and substantially concentrates the output,
yet (8) applies.  This is a method failure for bounded-menu adaptive bias, not for
arbitrary nonlinear maps or a menu whose size is exponential.

## 4. A single right-unit orbit: exact survivor criterion

There is a sharper genuinely nonuniform construction that the preceding theorem
does not dismiss.  Fix one \(\alpha\in L_N\), let

\[
G=\mathcal H^\times/\{\pm1\}\simeq A_4,
\]

and sample \(Y=\alpha u\) for uniform \(u\in G\).  This distribution has at
most twelve orientations, however large \(N\) is.

For \(r=p,q\), define the subgroup

\[
H_r(\alpha)=\operatorname{Stab}_G(R_r(\alpha)).
\]

For two independent units \(u,v\), the corrected relative right action is
\(uv^{-1}\), which is uniform on \(G\).  Therefore

\[
\boxed{\Pr(1<\operatorname{nrd}\operatorname{gcrd}(\alpha u,\alpha v)<N)
=\frac{|H_p(\alpha)\triangle H_q(\alpha)|}{12}.} \tag{10}
\]

This is an exact factor-free postprocessing theorem.  If the stabilizers differ,
a constant number of right-unit samples and Hurwitz Euclidean gcds returns norm
\(p\) or \(q\) with constant probability.  It is not a hidden uniform
\(\mathbb Z/N\mathbb Z\) polynomial computation: the returned object is a
one-sided quaternion divisor, and its reduced norm is already the factor.

But (10) moves the entire difficulty into producing \(\alpha\) in the mismatch
stratum.  A generic local line has trivial \(A_4\)-stabilizer; only the finitely
many eigenlines of nonidentity projective units are special.  Under the uniform
integer-shell law, averaging (10) is again \(O(1/p+1/q)\).  More importantly,
there is no pointwise guarantee: equal local stabilizer subgroups make (10)
exactly zero.

The deliberately simple canonical rule “take the lexicographically first
nonnegative sorted four-square tuple” illustrates both sides.  Exact enumeration
finds

\[
N=15,\quad \alpha=1+i+2j+3k,quad \Pr(\text{proper})=\frac14,
\]

but at

\[
N=39=3\cdot13,\quad \alpha=1+i+j+6k,quad \Pr(\text{proper})=0.  \tag{11}
\]

The latter is the first zero case among the 31 distinct odd semiprimes through
300 in the retained scan.  The displayed lexicographic finder itself enumerates
coordinate triples and is exponential in \(\log N\); no claim is made that the
same canonical representation cannot be found faster by another method.

## 5. Small exact checks

Run F15-B01 independently reconstructed the odd-prime matrix splittings and
checked:

* all \(192=8(3+1)(5+1)\) integer representations at the smallest odd edge
  \(N=15\), with exactly eight elements in every one of the 24 orientation
  fibres;
* the same fibre theorem and exact norm table on seven semiprimes through
  \(N=143\);
* the output distributions after the nonlinear Q8 canonicalization (9);
* the stabilizer formula (10) by all 144 ordered projective-unit pairs; and
* the lexicographic scan quoted in (11).

At \(N=15\), Q8 canonicalization collapses the 192 integer representations to
three outputs of equal weight and synchronizes all local collisions: its proper
probability is exactly zero, despite the uncanonicalized integer shell having
proper probability \(1/3\).  This is the smallest distinct odd semiprime and a
useful warning that “more concentrated” does not mean “asymmetrically
concentrated.”  Finite computation checks only the displayed instances; the
unbounded claims are the proofs above.

## Exact obstruction and next missing lemma

The exact obstruction is now sharper than “uniform samples fail”:

* the most natural strict coordinate slice is still exactly uniform after
  quotienting by the relevant unit action;
* its rebuilt exact sampler costs \(\Theta(\sqrt N)\) trials;
* even arbitrary sample-dependent selection among polynomially many fixed
  unit/conjugation transforms has exponentially small collision probability on
  balanced inputs; and
* a maximally concentrated twelve-point unit orbit can be perfectly synchronized,
  as (11) shows.

A materially new retry must prove all of the following for a sampler defined from
bare \(N\):

1. unconditional expected polynomial bit cost, including exact random-bit and
   rejection bounds rather than a citation to a find-one routine;
2. inverse-polynomial probability that the output satisfies
   \(H_p(\alpha)\ne H_q(\alpha)\), or another explicitly stated asymmetric
   collision-energy inequality; and
3. robustness on a balanced worst-case family, not just small or metrically close
   factors.

Coordinate caps, arithmetic four-square finders, and unrestricted adaptive
Euclidean-remainder maps remain open because their output distributions were not
silently replaced by uniform ones here.  The missing lemma is a distribution
theorem tying a fully specified factor-free find-one algorithm to asymmetric
local stabilizer strata.  Without it, (10) is a useful exact conditional
extractor, not a factoring algorithm.

## Computation

The named source, family ID, hard timeout, log, output, exact invocation, and
hashes are in `RUN_MANIFEST.md`.  No failed or timed-out run occurred.
