# F35 amended hostile re-audit: the factor-or-invariant theorem passes

**Verdict: PASS AS WRITTEN.**

The amended artifact survives a fresh end-to-end hostile audit. The local
CRT theorem, coefficient extractor, invariant, unconditional factor-or-TV
inequality, and uniform expected-cost reduction are all correct in the exact
model stated. I found no new counterexample inside that model.

The earlier
experiments/F35_low_degree_zero_product_bijection_audit/RESULT.md verdict
remains the correct historical verdict on the superseded version. The
current file has made the substantive repair that audit required: it proves a
factor-or-TV reduction and no longer treats the factor-visible branch as a
contradiction to existence of an accurate sampler.

**Audited artifact:**
experiments/F35_low_degree_zero_product_bijection_kill/RESULT.md in its
complete current form.

**Comparison material checked:** PROMPT.md; the complete prior failed audit;
the F34 candidate and reconstruction; and P40 as recorded in PROVED.md. No
mathematical computation or finite experiment was used, and the candidate
was not edited.

## 1. CRT decomposition and local bijectivity: pass

For \(N=pq\) with distinct primes,

\[
R\simeq \mathbb F_p\times\mathbb F_q
\]

coordinatewise, so the equation \(kx=0\) gives the exact set decomposition

\[
\Omega_N\simeq\Omega_p\times\Omega_q,
\qquad
\Omega_r=\{(a,b)\in\mathbb F_r^2:ab=0\}.
\]

Polynomial evaluation over a product ring is componentwise. Thus a fixed
global polynomial map is exactly \(T_p\times T_q\), not a correlated map
between the two CRT components. Every local zero-product point can be paired
with the origin in the other component and lifted, proving that each \(T_r\)
maps \(\Omega_r\) into itself. A collision or omitted point in either local
map would give a collision or omitted point globally. Hence global
bijectivity implies both local maps are bijections. No coordinate-ring
automorphism assumption is being imported here.

## 2. Root counting and the preserve/swap classification: pass

On either source axis over \(\mathbb F_r\), let \(f,g\) be the two coordinate
restrictions. The image condition gives

\[
f(t)g(t)=0\qquad(t\in\mathbb F_r).
\]

Both restrictions have degree at most \(D\), so
\(\deg(fg)\le 2D<r\). A polynomial of degree below \(r\) with all \(r\)
field elements as roots is formally zero. Since
\(\mathbb F_r[Z]\) is a domain, \(f=0\) or \(g=0\). Each entire source axis
therefore enters one target axis.

Injectivity rules out sending a source axis to the origin. The two source
axes cannot both enter one target axis, since their union is all of the
\((2r-1)\)-point set \(\Omega_r\), whereas one target axis has \(r\) points.
They consequently enter different target axes. Their common origin must map
to the intersection of those target axes, so it maps to the origin. Each
axis restriction is then an injection between two \(r\)-element sets and is
a bijection; nonzero axis points map to nonzero axis points. This proves
exactly the claimed local preserve/swap orientation without assuming that
the one-variable permutations are linear.

The strict degree threshold is essential. For example,
\(1-Z^{r-1}\) and \(Z^{r-1}\) are both formally nonzero but have pointwise
zero product over \(\mathbb F_r\). This lies outside \(2D<r\), as the
candidate says, and is not a counterexample.

## 3. Mixed orientation is coefficient-visible: pass

If the \(p\)-map preserves and the \(q\)-map swaps, the four formal axis
restrictions have the support pattern

\[
\begin{array}{c|cccc}
&F(K,0)&G(K,0)&F(0,X)&G(0,X)\\ \hline
\bmod p&\ne0&0&0&\ne0\\
\bmod q&0&\ne0&\ne0&0.
\end{array}
\]

For example, every coefficient of \(F(K,0)\) vanishes modulo \(q\), while at
least one is nonzero modulo \(p\). That coefficient has gcd exactly \(q\)
with \(N\). The reverse mismatch exchanges \(p\) and \(q\). Thus every
mixed orientation exposes a proper factor in a collected coefficient.

Conversely, if none of the four coefficient lists contains a proper-gcd
coefficient, mixed orientation is impossible. This implication does not
assert the false converse: a synchronized map can also contain a
factor-visible coefficient. The candidate needs only, and states only, the
no-factor implication.

## 4. The mixed-idempotent witness: pass

Label the complementary CRT idempotents so that

\[
e_p\equiv1\pmod p,\quad e_p\equiv0\pmod q,
\qquad
e_q\equiv0\pmod p,\quad e_q\equiv1\pmod q.
\]

Then

\[
(K,X)\longmapsto
(e_pK+e_qX,\ e_pX+e_qK)
\]

is the identity locally modulo \(p\) and the coordinate swap locally modulo
\(q\). It is its own inverse, so it is a degree-one bijection of
\(\Omega_N\). Moreover
\(\gcd(e_p,N)=q\) and \(\gcd(e_q,N)=p\), up to the harmless exchange caused
by the opposite naming convention. The example therefore proves precisely
what it is used for: mixed low-degree bijections exist, but their explicit
coefficients already encode the CRT split.

## 5. The invariant and exact factor-or-TV statement: pass

For a residue modulo a distinct semiprime, a coordinate gcd is not proper
exactly when the residue is a unit or zero. If a point of \(\Omega_N\) has
this property in both coordinates, the zero-product equation rules out two
units. Hence it lies in

\[
\mathcal A_N=
(R^\times\times\{0\})\mathbin{\dot\cup}
(\{0\}\times R^\times)\mathbin{\dot\cup}\{(0,0)\}.
\]

Conversely, every point outside \(\mathcal A_N\) has a proper coordinate
gcd. Thus checking both initializer coordinates detects the outside event
exactly.

When the two local orientations synchronize, a unit-axis point has a
nonzero output on the same selected local target axis in both CRT fields.
Its recombined nonzero coordinate is therefore a unit; the other coordinate
is zero. The origin is fixed. Hence every synchronized move preserves
\(\mathcal A_N\).

Let \(H\) be the union of all proper-gcd detections at initialization and in
all materialized coefficient lists. Pathwise, on \(H^c\), the initializer
is in \(\mathcal A_N\), every realized move is synchronized, and induction
keeps every state in \(\mathcal A_N\). This remains valid for an arbitrary
finite or almost-surely finite stopping rule, so

\[
\{Z_{\rm out}\in B_N\}\subseteq H,
\qquad B_N=\Omega_N\setminus\mathcal A_N.
\]

Crucially, the candidate now takes \(\mu\) to be the **unconditional**
terminal law. On the same underlying run,

\[
\Pr(H)\ge \mu(B_N)
\ge \pi_N(B_N)-\|\mu-\pi_N\|_{\rm TV}.
\]

This is the exact event inclusion and variational inequality. There is no
conditioning-on-a-null-event error and no inference that an accurate sampler
cannot exist. An accurate sampler can satisfy the inequality by producing a
factor-visible move, which the candidate explicitly credits as success.

## 6. Cardinalities, strict TV gap, and characteristic two: pass

Each local zero-product set consists of two \(r\)-point axes meeting once,
so

\[
|\Omega_N|=(2p-1)(2q-1).
\]

The invariant region has

\[
|\mathcal A_N|=2(p-1)(q-1)+1,
\]

and subtraction gives

\[
|B_N|=2pq-2=2N-2.
\]

The claimed strict half-mass calculation is exact:

\[
2|B_N|-|\Omega_N|=2p+2q-5>0.
\]

It includes \(\{p,q\}=\{2,3\}\), the smallest distinct-prime case. Therefore

\[
\rho_N=\frac{2N-2}{(2p-1)(2q-1)}>\frac12,
\]

and an \(\mathcal A_N\)-supported law has TV distance at least
\(\rho_N>1/2\) from uniform.

There is no characteristic-two exception in the field argument. If one
factor is \(2\) and \(D_N\ge1\), the public scan reaches \(2\) and returns
that factor. If \(D_N=0\), the strict root-count condition is automatic;
moreover no constant polynomial point map could be a bijection of the
non-singleton \(\Omega_N\). The candidate's handling is complete.

## 7. Exact formal outputs, extraction, and uniform cost: pass

The representation promise is stated at the correct level. Each submitted
division-free circuit must compute exact formal output polynomials of total
degree at most the public cap. Merely computing a finite-set function that
has some unexhibited low-degree representative would not suffice, and the
candidate explicitly excludes that substitution.

For either axis substitution, circuit evaluation in

\[
R[Z]/(Z^{D+1})
\]

is sound because quotient projection is a ring homomorphism. High-degree
intermediate terms and later cancellations cannot alter the retained low
coefficients. Since the exact final restriction has degree at most \(D\),
its truncated image is its complete coefficient list.

The complexity accounting distinguishes gate count \(g\) from total encoded
length \(L\), including constant bit strings. Ordinary truncated convolution
costs \(O(D^2)\) ring operations per multiplication gate in the nonvacuous
\(D\ge1\) bijection case, and both substitutions cost \(O(gD^2)\) up to a
fixed factor. Stored residues always have \(O(\log N)\) bits. The
\(4(D+1)\) coefficient gcds and the one-time \(O(D_N)\) small-factor scan are
also polynomial-bit operations.

The numeric quantifiers are uniform: there is one fixed polynomial \(P\)
and one public cap \(D_N\le P(n)\), independent of random seed, history,
move, and stopping time. The scan of \(2,\ldots,2D_N\) either finds a proper
factor or proves \(p,q>2D_N\), so the strict degree hypothesis then holds for
every realized move.

For an adaptive run, if \(L_i\) and \(g_i\) are the realized encoding length
and gate count, then \(g_i\le L_i\) for an explicit circuit encoding and

\[
\mathbb E\!\left[\sum_i g_iD_N^2\right]
\le P(n)^2\mathbb E\!\left[\sum_i L_i\right]
\le P(n)^2Q(n).
\]

The number of realized circuits and their coefficient scans are likewise
charged by their nonempty encodings, so the gcd overhead is polynomial as
well. Modular ring-operation bit costs contribute another fixed polynomial
factor in \(n\). Together with the sampler's separately assumed expected
bit and fair-bit bound, this proves total expected monitoring cost, not just
a per-move estimate.

## 8. Semantic promises and adaptive scope: pass

The artifact does not pretend to certify either hard semantic property. It
requires the proposed sampler to justify that every materialized circuit:

1. has exact formal outputs under the public degree cap; and
2. itself induces a global bijection of all \(\Omega_N\).

The theorem is then applied after freezing each realized history and its
explicit circuit. The selector may depend on the current state, the full
transcript, and fresh randomness; independence, stationarity, reversibility,
and time homogeneity are unnecessary because the invariant is pathwise.

The model boundary is also explicit. A state-dependent selector among
materialized global bijections is covered. A stitched map
\(z\mapsto T_z(z)\) whose individual branch \(T_z\) is not itself a promised
global bijection, or whose realized global circuit is never exposed, is not
covered. The proof makes no claim about such piecewise or opaque maps.

## 9. Warm starts and stopped repetition: pass

For an \(\Omega_N\)-valued initializer, outside mass
\(\varepsilon_N\) is exactly the probability that the two coordinate gcd
checks expose a factor. Fresh independent invocations with expected
polynomial cost and one uniform inverse-polynomial lower bound on
\(\varepsilon_N\) therefore give a verified Las Vegas splitter on the
**distinct-semiprime subfamily**. The candidate explicitly says this is not
yet complete all-input factoring.

For a sampler with TV error \(\delta<1/2\), the amended inequality gives

\[
s_N:=\Pr(H)\ge\rho_N-\delta>\frac12-\delta.
\]

Fresh repetition terminates almost surely and has expected at most
\((1/2-\delta)^{-1}\) runs. Correlation between a run's success and its own
cost does not invalidate the expected-cost bound. If \((C_i,H_i)\) are
fresh identically distributed run-cost/success pairs, the event that run
\(i\) is reached depends only on earlier pairs and is independent of \(C_i\).
Consequently

\[
\mathbb E\!\left[\sum_{i\text{ reached}}C_i\right]
=\sum_{i\ge1}(1-s_N)^{i-1}\mathbb E[C_1]
=\frac{\mathbb E[C_1]}{s_N}.
\]

Every returned gcd is verified to lie strictly between \(1\) and \(N\), so
the splitter is Las Vegas. The artifact correctly limits this conclusion to
distinct semiprimes and correctly reserves the nonexistence statement for a
genuinely factor-free all-input sampler confined to the stated move model.

## 10. F34 and P40 comparison: pass

F34 concerns the narrower semantic class of coordinate-ring automorphisms of
\(R[K,X]/(KX)\). Its local maps are exactly linear scalings or swaps, and its
intrinsic first-jet extraction tolerates submitted representatives and
intermediate circuits of arbitrarily high formal degree. F35 instead allows
arbitrary finite-set polynomial bijections, including nonlinear
one-variable permutation polynomials along axes, but requires the submitted
exact formal outputs themselves to have a public low-degree cap. One route
is semantically narrower and representation-tolerant; the other is
semantically broader and representation-restricted. Calling their scopes
incomparable is accurate.

P40 bounds local zero probabilities for products of nonzero polynomial tests
on fresh full-affine samples and turns the two CRT-local OR events into an
XOR. F35 starts from a pointwise zero-product identity on every point of an
axis and uses low degree plus bijectivity to classify whole-axis orbits.
There is no appeal to P40, no fresh-sample conditioning issue, and no
rare-ticket union bound. The stated comparison is exact and does not claim
that P40 can extract coefficients from arbitrary high-degree circuits.

## 11. Counterexample and boundary audit

I specifically tested the following possible failure modes.

- A finite-field function can split one source axis between target axes at
  characteristic-scale degree. This does not meet \(2D<r\) and is explicitly
  left open.
- A low-degree axis permutation need not be a linear scaling. The proof never
  requires linearity and the artifact says so.
- A synchronized map can still contain a one-sided coefficient. The monitor
  then factors \(N\); the no-factor implication remains valid.
- Adaptive state-dependent choice can make the stitched aggregate map
  nonbijective even when every selected branch is a global bijection. Each
  branch still preserves \(\mathcal A_N\), so the pathwise proof survives.
- If the individual state branch is only locally defined or only the stitched
  aggregate is bijective, the theorem cannot be applied. This is expressly
  outside scope.
- Prime powers, nonsquarefree bases beyond the distinct-semiprime theorem,
  stochastic or noninvertible kernels, auxiliary state, rational/division
  circuits, and opaque evaluators are not silently claimed.
- The factor event may have probability one, including through the explicit
  mixed-idempotent map. The amended conclusion treats that as successful
  factor extraction rather than a sampler contradiction.

None is a counterexample to the theorem actually stated.

## 12. Notation, equation references, and prose sweep: pass

All displayed counts and inequalities recompute correctly. References to
(0.3), (0.4), (0.5), (0.6), (0.7), (0.8), (0.9), (3.1), and (7.1) point to
the intended statements. The references to Sections 2 and 3 and to the
Outcome are accurate. Gate count and encoding length use distinct symbols;
the malformed equation and extra parenthesis identified by the historical
audit are gone. I found no remaining broken equation reference,
quantifier-changing typo, or contradictory scope sentence.

The amended artifact therefore merits **PASS AS WRITTEN** at this hostile
re-audit stage. Its status should not advance beyond the verification
cadence until the required fresh proof-blind reconstruction also succeeds.
