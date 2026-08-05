# F15 follow-up — hostile audit of Hurwitz coordinate bias

**Audit verdict:** the mathematical core survives, but only with explicit
wording and quantifier corrections.  The integer-coordinate fibre theorem, the
rejection sampler, the iid finite-menu bound, and the right-unit stabilizer
formula are correct for \(N=pq\) with distinct odd primes.  The retained finite
scan is not exhaustive through \(300\): it covers 31 of the 53 distinct odd
semiprimes in that range.  An independent complete scan preserves the claimed
first zero at \(N=39\).

This remains a narrow method failure and conditional extractor, not a factoring
algorithm.  No factor-free expected-polynomial method is given for producing an
\(\alpha\) whose two local stabilizers differ with inverse-polynomial
probability.  The result also does not address even inputs, prime powers,
general composites, unrestricted nonlinear transforms, or non-collision
quaternion invariants.

Because this is only the hostile-audit step, the corrected result is not yet
verifier-backed under the project's vocabulary.  A fresh proof-blind
reconstruction is still required.

## Corrections required

1. **Complete the all-half-to-integral argument.**  It is true that every
   left- and right-unit orbit of odd norm meets the Lipschitz slice, but the
   candidate only asserts the key step.  A four-line congruence proof is given
   below.

2. **State the finite-menu quantifiers in the headline.**  Equations (6)--(8)
   use a memoryless selector applied independently to each iid raw sample.  They
   do not literally prove the displayed \(C/(r+1)\) collision bound for a
   selector that jointly inspects all \(K\) raw samples or shares state across
   outputs.  The broader conclusion still holds with \(C^2/(r+1)\), proved
   below.  Neither theorem covers transforms that combine several raw samples
   into one output.

3. **Define unit sampling in \(\mathcal H^\times\), not in its quotient.**  The
   expression \(\alpha u\) is not defined for
   \(u\in G=\mathcal H^\times/\{\pm1\}\).  Draw actual units
   \(U,V\in\mathcal H^\times\), or choose a section of the quotient.  The gcd
   norm is sign-invariant, so the resulting probability still has denominator
   12.

4. **Qualify “generic stabilizer” in small characteristics.**  The projective
   \(A_4\) action is faithful for every odd prime, including \(3\).  Every
   nonidentity element therefore fixes at most two rational projective lines.
   Thus at most 22 lines have nontrivial stabilizer.  This does not imply that a
   trivial-stabilizer line exists when \(r+1\le22\); at \(r=3\), the faithful
   \(A_4\simeq PSL_2(\mathbb F_3)\) action is transitive on four lines and every
   stabilizer has order 3.

5. **Separate trials from bit running time.**  The outer rejection count is
   \(\Theta(\sqrt N)\) on balanced semiprimes.  The specified exact interval
   draws use \(\Theta(\log N)\) expected random bits per trial, so their total is
   \(\Theta(\sqrt N\log N)\); total bit time is
   \(\sqrt N\operatorname{polylog}N\), not literally \(\Theta(\sqrt N)\).
   The candidate's intended conclusion—exponential in the input length caused
   by the \(\Theta(\sqrt N)\) acceptance loss—is correct.

6. **Correct the scan description.**  The retained source restricts both prime
   factors to be below 32.  Its 31-case set is
   
   \[
   \{(p,q):3\le p<q<32,\ p,q\text{ prime},\ pq\le300\},
   \]
   
   not all distinct odd semiprimes through 300.  There are 53 in the complete
   set.  “First” is defensible only after naming the retained subset, although
   the independent complete scan confirms that the first zero by increasing
   \(N\) is still \(39\).

7. **Narrow the provenance claim.**  The current hashes all match, and the JSON
   embeds the current source hash.  This establishes current source/output
   consistency.  It does not cryptographically prove that the wrapper was never
   edited, that no unretained failed run existed, or that every listed background
   file was read.  The experiment directory is untracked, so there is no commit
   history providing that attestation.

8. **Describe the Q8 finite check accurately.**  The retained small cases do
   compute the canonicalized distributions, but the asserted atom-bound checks
   are numerically vacuous there: \(128/(r+1)>1\) for every tested local prime.
   The bound is established by the symbolic proof, not by those assertions.

There is also a harmless typesetting error in (11): `,quad` should be
`,\quad`.

## 1. Independent proof of the eight-element fibre theorem

Use the exact normalization

\[
\mathcal H=
\mathbb Z^4\ \sqcup\ (\mathbb Z+\tfrac12)^4
\]

inside the Hamilton quaternions.  Its 24 norm-one units are the eight
Lipschitz units

\[
Q_8=\{\pm1,\pm i,\pm j,\pm k\}
\]

and the sixteen units

\[
\frac{\pm1\pm i\pm j\pm k}{2}.
\]

Let \(x=a+bi+cj+dk\in\mathbb Z^4\) have odd norm.  An odd number of
\(a,b,c,d\) is odd.  Multiplying \(x\) on either side by any half-integral unit
gives doubled coordinates that are signed sums of all four coordinates.  Every
such sum is odd.  Hence all sixteen half-integral units send \(x\) outside
\(\mathbb Z^4\), while the eight elements of \(Q_8\) preserve
\(\mathbb Z^4\).  Unit actions are free on nonzero quaternions, so an orbit
containing \(x\) contains exactly eight integral elements.

It remains to prove that every odd-norm orbit contains such an \(x\).  Write an
all-half-integral element as

\[
z=\frac{a+bi+cj+dk}{2},\qquad a,b,c,d\text{ odd}.
\]

For

\[
u=\frac{s_0+s_1i+s_2j+s_3k}{2},\qquad s_t\in\{\pm1\},
\]

the real coordinate of \(uz\) has numerator

\[
s_0a-s_1b-s_2c-s_3d
\]

over 4.  Choose the four signs so that each of the four displayed signed odd
terms is \(1\pmod4\).  The numerator is then \(0\pmod4\), so the real
coordinate is integral.  Since \(uz\in\mathcal H\) and all four coordinates of
a Hurwitz element have the same fractional part, all coordinates are integral.
The identical real-coordinate argument works for \(zu\).  Thus every left- and
right-unit orbit of odd norm has exactly eight Lipschitz elements.

Promoted result P25 supplies the already-verified bijections

\[
\mathcal H^\times\backslash S_N
\simeq\mathbf P^1(\mathbb F_p)\times\mathbf P^1(\mathbb F_q)
\]

by row lines and, for right-unit orbits, the analogous bijection by image lines.
Intersecting each 24-element orbit with \(L_N\) therefore gives exactly eight
preimages of every row pair and exactly eight preimages of every image pair.
Consequently uniform \(L_N\) has independent uniform local row coordinates,
and separately independent uniform local image coordinates.  This asserts no
row/image independence within one sample.

Jacobi's formula gives

\[
|L_N|=r_4(N)=8\sigma(N)=8(p+1)(q+1),
\]

consistent with the fibre count.  The candidate's strict slice really is one
third of \(S_N\), but quotienting by either relevant unit action removes the
bias completely.

## 2. Handedness, exact gcd law, and union bound

For a greatest common right divisor \(d_R\), the defining ideal identity is

\[
\mathcal H\alpha+\mathcal H\beta=\mathcal H d_R.
\]

Modulo an odd prime \(r\mid N\), the left ideal generated by a nonzero rank-one
matrix consists of matrices whose rows lie in its row line.  Hence

\[
r\mid\operatorname{nrd}(d_R)
\quad\Longleftrightarrow\quad
R_r(\alpha)=R_r(\beta).                         \tag{A1}
\]

Thus rows control **right** divisors; images control left divisors.  For iid
uniform \(L_N\) samples, the two CRT row coordinates are independent, so (A1)
gives

\[
\Pr(\operatorname{nrd}d_R=1,p,q,N)
=\frac{(pq,q,p,1)}{(p+1)(q+1)}.                \tag{A2}
\]

Squarefreeness is essential to the four possible norm values.  A proper event
has probability

\[
\delta_{p,q}=\frac{p+q}{(p+1)(q+1)}.           \tag{A3}
\]

For \(K\) iid samples, a union bound over unordered pairs gives

\[
\Pr(\text{some proper right gcd})
\le {K\choose2}\delta_{p,q}.                   \tag{A4}
\]

If \(p<q<2p\), then \(p=\Theta(\sqrt N)\), so (A4) is
\(O(K^2/\sqrt N)\).  The orientation, handedness, norm labels, and union-bound
directions in the candidate are correct.

## 3. Exact rejection sampling, including \(d=0\)

Let \(B=\lfloor\sqrt N\rfloor\) and \(M=2B+1\).  A fixed triple
\((a,b,c)\in[-B,B]^3\) is drawn with probability \(M^{-3}\).  If
\(d_0>0\), each of its two completions has probability
\(1/(2M^3)\).  If \(d_0=0\), accepting on exactly one value of a fresh fair bit
also gives its unique completion probability \(1/(2M^3)\).  Every Lipschitz
representation occurs because each coordinate has absolute value at most \(B\).
Therefore every \(x\in L_N\) is emitted per outer trial with the same probability

\[
\frac1{2M^3},
\]

and the acceptance probability and expected trial count are

\[
\frac{|L_N|}{2M^3},\qquad
\frac{2M^3}{|L_N|}
=\frac{M^3}{4(p+1)(q+1)}.                      \tag{A5}
\]

The acceptance probability is positive, so termination is almost sure.  An
exact interval draw using \(k=\lceil\log_2M\rceil\) bits per block accepts a
block with probability \(M/2^k>1/2\).  It uses fewer than two expected blocks,
so an outer trial uses \(O(\log N)\) expected random bits.  Conversely three
independent uniform \(M\)-ary draws contain \(3\log_2M=\Theta(\log N)\) bits of
entropy.  Wald's identity applies to the iid outer trials, giving

\[
\Theta(\sqrt N\log N)
\]

expected random bits on balanced semiprimes.  All operands have
\(O(\log N)\) bits, so arithmetic contributes only a polynomial-logarithmic
factor per trial.  The sampler is exact and factor-free, but exponentially slow
in the binary input length.

The independent audit explicitly checked a case with \(d=0\): at \(N=21\), 48
of the 256 representations have last coordinate zero, and all 256 retain the
same per-trial probability \(1/1458\).

## 4. Correct finite-menu theorem

The needed hypothesis is most clearly stated at the orientation level.  For
each \(T\in\mathcal T\) and each \(r\in\{p,q\}\), require that
\(R_r(TX)\) be a fixed projective bijection either of \(R_r(X)\) or of
\(I_r(X)\).  Unit maps \(aXb\) and \(a\bar Xb\) that preserve \(L_N\) satisfy
this.  Since both relevant input marginals are uniform,

\[
\Pr(R_r(TX)=L)=\frac1{r+1}                     \tag{A6}
\]

for every fixed \(T,L\).

For the candidate's memoryless selector \(T_X\), put \(Y=T_X(X)\).  Then

\[
\begin{aligned}
\Pr(R_r(Y)=L)
&=\sum_T\Pr(T_X=T,\ R_r(TX)=L)\\
&\le\sum_T\Pr(R_r(TX)=L)
=\frac C{r+1}.                                 \tag{A7}
\end{aligned}
\]

No independence between \(T_X\) and \(X\) is used.  For two iid copies of this
entire output experiment,

\[
\Pr(R_r(Y)=R_r(Y'))
=\sum_L\Pr(R_r(Y)=L)^2
\le\min\!\left(1,\frac C{r+1}\right).         \tag{A8}
\]

The candidate's equations (6)--(8) follow, as does the all-pairs union bound.

There is a useful stronger version that removes the hidden memorylessness.  Let
\(X_1,\ldots,X_K\) be independent uniform raw samples, but allow a joint or
stateful selector to inspect the whole tuple and choose
\(T_i\in\mathcal T\) for every \(i\).  For a fixed pair \(i,j\), a selected
local collision is contained in

\[
\bigcup_{T,S\in\mathcal T}
\{R_r(TX_i)=R_r(SX_j)\}.
\]

For fixed \(T,S\), the two lines are independent and uniform, whether each
comes from a row or an image marginal.  Therefore

\[
\Pr(R_r(T_iX_i)=R_r(T_jX_j))
\le\min\!\left(1,\frac{C^2}{r+1}\right).       \tag{A9}
\]

Combining the two local primes and all sample pairs gives

\[
{K\choose2}\left[
\min\!\left(1,\frac{C^2}{p+1}\right)
+\min\!\left(1,\frac{C^2}{q+1}\right)
\right].                                      \tag{A10}
\]

Thus the balanced-family obstruction survives even transcript-dependent menu
selection when \(C,K=\operatorname{poly}(\log N)\).  This is still only a
finite-menu theorem: it does not cover a transform that combines raw samples,
an exponential menu, or an unrestricted nonlinear map.

Q8 canonicalization is a valid instance.  Its 128 listed entries represent at
most 64 distinct maps, so either count gives the same asymptotic conclusion.

## 5. Correct \(A_4\) stabilizer theorem

Let \(U=\mathcal H^\times\).  The explicit unit list shows that

\[
G=U/\{\pm1\}
\]

has one identity, three nonidentity elements of order 2 coming from \(Q_8\), and
eight elements of order 3 coming from the half units.  Hence \(G\simeq A_4\).

For every odd prime \(r\), its action on \(\mathbf P^1(\mathbb F_r)\) is
faithful.  Indeed, a projectively trivial unit reduces to a scalar in
\(M_2(\mathbb F_r)\), so all three imaginary coordinates vanish modulo \(r\).
Inspection of the 24 units shows that this occurs only for \(\pm1\): an
integral noncentral unit has an imaginary coordinate \(\pm1\), and a half unit
has all three imaginary coordinates \(\pm1/2\), nonzero for odd \(r\).  This
also handles characteristic 3; order-3 elements become nonidentity unipotents,
not scalars.

Now draw actual units \(U_1,U_2\) independently and uniformly from \(U\), and
put

\[
Y_1=\alpha U_1,\qquad Y_2=\alpha U_2.
\]

For \(r=p,q\), let

\[
H_r(\alpha)=\operatorname{Stab}_G(R_r(\alpha)).
\]

The projective class

\[
g=\overline{U_1}\,\overline{U_2}^{-1}
\]

is uniform on \(G\).  Since right multiplication sends a row line \(L\) to
\(L\overline U\),

\[
R_r(Y_1)=R_r(Y_2)
\quad\Longleftrightarrow\quad
g\in H_r(\alpha).                              \tag{A11}
\]

Combining (A11) with (A1), a proper right gcd occurs exactly on the symmetric
difference of the two stabilizers.  Therefore

\[
\boxed{
\Pr(1<\operatorname{nrd}\operatorname{gcrd}(Y_1,Y_2)<N)
=\frac{|H_p(\alpha)\triangle H_q(\alpha)|}{12}.}
                                                               \tag{A12}
\]

This proof fixes both the action orientation and the relative order:
\(U_1U_2^{-1}\), not \(U_2^{-1}U_1\).  Faithfulness is not required for (A12)
itself, but it is required for the eigenline bound that follows.

Every nonidentity projective transformation has at most two fixed lines, so all
but at most 22 lines have trivial stabilizer.  The phrase “generic line” must be
read in precisely this bounded-exception sense.  Averaging over uniform
\(\alpha\in L_N\) gives the explicit estimate

\[
\begin{aligned}
\mathbb E_\alpha\Pr(\text{proper}\mid\alpha)
&\le \frac1{12}\sum_{g\ne1}
\left(
\frac{|\operatorname{Fix}_p(g)|}{p+1}
+\frac{|\operatorname{Fix}_q(g)|}{q+1}
\right)\\
&\le \frac{22}{12}
\left(\frac1{p+1}+\frac1{q+1}\right),         \tag{A13}
\end{aligned}
\]

which justifies the candidate's \(O(1/p+1/q)\) statement without any
large-characteristic assumption.

If \(H_p(\alpha)\ne H_q(\alpha)\), their symmetric difference is nonempty, so
one unit pair succeeds with probability at least \(1/12\).  This is genuinely
factor-free postprocessing once \(\alpha\) is supplied.  A Hurwitz Euclidean
step can choose a remainder of norm at most half the divisor norm, giving
\(O(\log N)\) divisions; nearest-lattice rounding checks only the two Hurwitz
cosets, and all coordinates have polynomial bit length.  Thus the conditional
gcd extraction has polynomial bit cost.

It does **not** merely repackage a terminal integer gcd.  On a proper event the
Hurwitz greatest common right divisor itself is computed, and its reduced norm
is \(p\) or \(q\).  An ordinary gcd with \(N\) may be used to verify or normalize
the returned integer, but it is not the source of the separation.  The local
splittings in the finite certificate do use the known factors to verify the
theorem; the actual unit sampling and Hurwitz gcd do not.

The unresolved step is upstream: no expected-polynomial, factor-free sampler is
proved to output a mismatch-stratum \(\alpha\) with inverse-polynomial
probability.  The lexicographic four-square enumeration is factor-free but
exponential in \(\log N\).

## 6. Independent finite audit

Run F15-BA01 was written independently and imports no candidate code.  It
passed all of the following:

- \(N=15\): 192 Lipschitz representations, 24 row fibres and 24 image fibres,
  each of size 8; every left- and right-unit orbit has exactly eight integral
  elements.
- \(N=39\): 448 Lipschitz representations, 56 row fibres and 56 image fibres,
  each of size 8; the same left/right orbit count holds.
- Direct enumeration of norm-\(r\) common right divisors agrees with row-line
  equality for every ordered actual-unit pair at \(N=15\) and \(N=39\).  This
  independently checks the collision-to-right-gcd direction rather than merely
  reusing the orientation formula.
- At \(N=15\), \(\alpha=(1,1,2,3)\) has stabilizer sizes 3 and 2, symmetric
  difference size 3, and proper probability \(3/12=1/4\).  The 144 ordered
  projective-unit pairs split as 96 neither, 24 \(p\)-only, 12 \(q\)-only, and
  12 both.
- At \(N=39\), \(\alpha=(1,1,1,6)\) has the same order-3 stabilizer at both
  primes.  The 144 pairs split as 108 neither and 36 both, giving proper
  probability zero.
- The 12 projective unit classes remain distinct for every odd prime occurring
  in the complete scan, including \(3\).
- At \(N=15\), Q8 canonicalization has three outputs of weight 64 and proper
  probability zero.
- The rejection probabilities agree at \(N=15\) and at the \(d=0\) edge
  \(N=21\).

The complete scan contains 53 distinct odd semiprimes \(pq\le300\), whereas the
candidate retains 31 and omits 22 pairs.  The independent complete ordering
still begins

\[
15,21,33,35,39,\ldots
\]

and \(39\) is still the first zero.  Thus the coordinates and probabilities in
(11) survive; only the claimed scan coverage needed correction.

The source, 120-second hard timeout, exact command, log, JSON, and hashes are in
`RUN_MANIFEST.md`.  The run finished in about two seconds.  It is a finite
certificate, not proof of any unbounded statement.

## 7. Candidate artifact and hash audit

The four hashes listed in the candidate manifest recompute exactly:

| Candidate artifact | Recomputed SHA-256 status |
| --- | --- |
| `scripts/F15_B01_coordinate_slice.py` | match |
| `run_F15_B01.sh` | match |
| `output/F15-B01.json` | match |
| `logs/F15-B01.log` | match |

The JSON's embedded source hash equals the current source hash, and the
independent audit records the candidate JSON hash
`7012ca1dde400acd50aef988dd2cb89820ba456d4f2f5c3823171f2b202110c1`.
The log names the run and family, records the 120-second limit and UTC times,
and ends in PASS.  The wrapper has `set -euo pipefail` and invokes the stated
hard timeout.

The limitations are provenance, not arithmetic consistency.  The log does not
echo the exact command or authenticate the wrapper bytes.  The manifest was
written after the run, its hashes are self-reported, and the directory is not
tracked by Git.  Therefore “current retained artifacts are mutually
consistent” is established; “neither source nor wrapper was edited after the
run” and “no unretained run occurred” are not independently attestable from
these files alone.

## Final classification

After the corrections above, the strongest justified result is:

- uniform sampling from the Lipschitz third of an odd squarefree two-prime
  Hurwitz shell is still exactly uniform in each relevant projective quotient;
- its explicit coordinate-triple rejection sampler needs
  \(\Theta(\sqrt N)\) trials on balanced semiprimes;
- independently selected adaptive transforms from a \(C\)-map menu obey the
  candidate's \(C/(r+1)\) collision bound, and even joint/stateful selection
  obeys the broader \(C^2/(r+1)\) bound; and
- a single right-unit orbit has exact proper-gcd probability
  \(|H_p\triangle H_q|/12\), with positive example \(N=15\) and zero example
  \(N=39\).

This closes the named coordinate-slice and polynomial finite-menu mechanisms on
balanced inputs.  It leaves open exactly the candidate's final missing lemma: a
fully specified, factor-free expected-polynomial sampler with provably
inverse-polynomial asymmetric local stabilizer behavior, or a genuinely
different non-collision quaternion mechanism.
