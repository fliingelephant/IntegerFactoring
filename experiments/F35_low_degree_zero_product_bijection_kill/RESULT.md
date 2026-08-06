# F35 kill-first: low-degree finite-set bijections cannot desynchronize zero-product axes without exposing a factor

**Status:** promoted as P45 after the original sampler-impossibility version
failed hostile audit, the amended factor-or-TV theorem passed a fresh
whole-artifact hostile re-audit, and a context-free proof-blind
reconstruction succeeded.

**Family:** F23.

**Closest prior route and material difference.**  F34 classifies algebraic
automorphisms of the nodal coordinate ring

\[
(\mathbb Z/N\mathbb Z)[K,X]/(KX).
\]

F34 accepts submitted circuit or polynomial representatives of arbitrarily
large formal degree, then proves that their semantic point actions are exact
linear scalings or swaps.  It deliberately does not cover a polynomial map
which is merely a permutation of the finite zero-product point set.  The
present route covers that larger semantic class: it assumes only that the
induced point map is a bijection.  In exchange, its submitted exact formal
outputs must have a public low-degree cap so their complete axis restrictions
can be extracted.  The representation-level scopes are therefore
incomparable rather than restatements.  P40 is the other nearby
low-degree boundary, but it bounds the probability that products of tests
vanish on fresh full-affine samples.  Here the zero-product identity holds
at every point of an axis, and bijectivity converts that identity into an
orbit classification; there is no rare-ticket union bound.

**Classification.**  This is an exact factor-or-invariant reduction for
low-formal-degree polynomial permutation moves on the finite zero-product
set.  It rules out only a **factor-free** sampler confined to those moves;
an accurate sampler may instead expose a factor, which is success rather than
a contradiction.  The theorem does not cover characteristic-scale degree,
noninvertible or stochastic moves, auxiliary state, rational/branching/opaque
maps, or positive matching samplers.

No computation was used.

## Outcome

Let

\[
N=pq,
\qquad
R=\mathbb Z/N\mathbb Z,
\qquad
\Omega_N=\{(k,x)\in R^2:kx=0\},
\tag{0.1}
\]

where \(p\ne q\) are primes.  Let

\[
T=(F,G):\Omega_N\longrightarrow\Omega_N
\tag{0.2}
\]

be induced by two polynomials \(F,G\in R[K,X]\) of total degree at most
\(D\), and suppose that \(T\) is a bijection of the finite set \(\Omega_N\).
If

\[
2D<\min(p,q),
\tag{0.3}
\]

then, over each local field, \(T\) either preserves the two coordinate axes
or swaps them.  If the choices over \(\mathbb F_p\) and \(\mathbb F_q\)
differ, a coefficient of one of the four public univariate restrictions

\[
F(K,0),\quad G(K,0),\quad F(0,X),\quad G(0,X)
\tag{0.4}
\]

has a proper gcd with \(N\).  If no such coefficient reveals a factor, the
two local orientations synchronize.

Consequently the no-factor branch preserves

\[
\mathcal A_N
=(R^\times\times\{0\})
\mathbin{\dot\cup}(\{0\}\times R^\times)
\mathbin{\dot\cup}\{(0,0)\}.
\tag{0.5}
\]

For an adaptive or randomized run, inspect both initializer-coordinate gcds
and the four coefficient lists before each realized move.  Let \(H\) be the
event that one of these checks returns a proper factor, and put

\[
B_N=\Omega_N\setminus\mathcal A_N.
\]

On \(H^c\), the initializer lies in \(\mathcal A_N\) and every move
synchronizes, so every later state lies in \(\mathcal A_N\).  Hence, for
every finite or almost-surely finite stopping rule,

\[
\{Z_{\rm out}\in B_N\}\subseteq H.
\tag{0.6}
\]

The uniform law \(\pi_N\) on \(\Omega_N\) satisfies

\[
\rho_N:=\pi_N(B_N)
=\frac{2N-2}{(2p-1)(2q-1)}>\frac12.
\tag{0.7}
\]

If \(\mu\) is the **unconditional** terminal law, then (0.6) gives the
quantitative factor-or-TV dichotomy

\[
\Pr(H)\ge \mu(B_N)
\ge \rho_N-\|\mu-\pi_N\|_{\rm TV}.
\tag{0.8}
\]

Thus a genuinely factor-free run is more than \(1/2\) from uniform, whereas
a sampler of TV error \(\delta<1/2\) exposes a factor with probability at
least \(\rho_N-\delta>1/2-\delta\).  This is a factoring reduction, not a
nonexistence proof for accurate samplers.

Indeed mixed low-degree bijections exist.  If \(e_p,e_q\in R\) are the
complementary CRT idempotents, then

\[
(K,X)\longmapsto
(e_pK+e_qX,\ e_pX+e_qK)
\tag{0.9}
\]

preserves axes modulo \(p\), swaps them modulo \(q\), and is a degree-one
bijection of \(\Omega_N\).  Its coefficients expose both factors.  Equation
(0.9) is an existence witness using the hidden CRT split, not a factor-free
construction; it shows exactly why the monitored branch is success rather
than contradiction.

For the uniform algorithmic interpretation, write
\(n=\lceil\log_2(N+1)\rceil\).  Require one fixed polynomial \(P\) and one
public numeric bound \(D_N\le P(n)\), independent of the history, random
seed, move, and stopping time.  Every materialized circuit must compute exact
formal outputs of total degree at most \(D_N\) and must itself induce a
global bijection of \(\Omega_N\); these are semantic promises supplied by
the proposed sampler, not properties certified here.  The coefficient lists
are accessible by evaluating the circuit's four axis restrictions in
\(R[Z]/(Z^{D_N+1})\), at \(O(D_N^2)\) ring operations per multiplication
gate.  If the expected total encoded length of all realized circuits is
polynomial in \(n\), including constants and stopping time, then the total
expected monitoring overhead is polynomial too: if
\(\mathbb E\sum_i L_i\le Q(n)\), then \(g_i\le L_i\) and the expected number
of ring operations is at most \(P(n)^2Q(n)\), up to a fixed constant.  A
one-time scan through \(2D_N\) either finds a small factor or certifies
(0.3) for every move.

## 1. Local maps are bijections

CRT identifies

\[
\Omega_N\cong\Omega_p\times\Omega_q,
\qquad
\Omega_r=\{(a,b)\in\mathbb F_r^2:ab=0\}.
\tag{1.1}
\]

Reduction of the two public polynomials gives maps

\[
T_r=(F_r,G_r):\Omega_r\longrightarrow\Omega_r
\qquad(r=p,q).
\tag{1.2}
\]

To see that each reduction maps into \(\Omega_r\), take any local
zero-product point, complete it by the origin in the other CRT component,
and lift the pair to \(\Omega_N\).  Its global image has zero product, so its
chosen local component does too.

The global point map is exactly the Cartesian product \(T_p\times T_q\).
If one local map were not injective, holding the other component fixed would
give a global collision.  If one were not surjective, the Cartesian product
would not be surjective.  Hence the assumed global bijection makes both
\(T_p\) and \(T_q\) bijections.

This step uses only polynomial evaluation and CRT.  It does not assume that
\(T\) is an automorphism of a coordinate ring.

## 2. Root counting forces one target axis per source axis

Fix \(r\in\{p,q\}\).  On the first source axis define

\[
f_1(Z)=F_r(Z,0),
\qquad
g_1(Z)=G_r(Z,0).
\tag{2.1}
\]

The image lies in \(\Omega_r\), so

\[
f_1(t)g_1(t)=0
\qquad\text{for every }t\in\mathbb F_r.
\tag{2.2}
\]

The product polynomial has degree at most \(2D<r\).  It has \(r\) roots,
so it is the zero polynomial.  Since \(\mathbb F_r[Z]\) is an integral
domain,

\[
f_1=0\quad\text{or}\quad g_1=0
\tag{2.3}
\]

as a formal polynomial.  Therefore the entire first source axis maps into
one target axis.  The same argument for

\[
f_2(Z)=F_r(0,Z),
\qquad
g_2(Z)=G_r(0,Z)
\tag{2.4}
\]

puts the second source axis inside one target axis.

Neither source axis can collapse to the origin, because \(T_r\) is
injective.  Nor can both source axes map into the same target axis: their
union is all \(\Omega_r\), whereas one target axis has \(r\) points and

\[
|\Omega_r|=2r-1>r.
\]

Thus the two source axes map to the two different target axes.  Their common
point must map into the intersection of those target axes, so

\[
T_r(0,0)=(0,0).
\tag{2.5}
\]

The restriction from either source axis to its target axis is an injection
between two \(r\)-element sets, hence a bijection.  In particular its one
nonzero coordinate maps nonzero inputs to nonzero outputs.  This proves the
local preserve/swap classification without classifying the one-variable
permutation polynomial along either axis.

## 3. Mixed local orientation is coefficient-visible

Reduce the four polynomials in (0.4) modulo each unknown prime.  Suppose for
concreteness that \(T_p\) preserves the axes and \(T_q\) swaps them.  Then

\[
\begin{array}{c|cccc}
&F(K,0)&G(K,0)&F(0,X)&G(0,X)\\ \hline
\bmod p&\ne0&0&0&\ne0\\
\bmod q&0&\ne0&\ne0&0.
\end{array}
\tag{3.1}
\]

Here \(0\) and \(\ne0\) mean zero or nonzero as a formal univariate
polynomial.  For example, every coefficient of \(F(K,0)\) vanishes modulo
\(q\), while at least one coefficient is nonzero modulo \(p\).  That public
coefficient \(c\in R\) satisfies

\[
\gcd(c,N)=q.
\tag{3.2}
\]

The reverse mixed orientation is identical with \(p,q\) interchanged.
Hence mixed orientation always exposes a factor among the coefficients in
(0.4).  This statement would fail without the degree bound: a nonzero
polynomial function can have a high-degree representative which vanishes at
every field point.

Conversely, if none of the coefficient gcds is proper, (3.1) rules out mixed
orientation.  The two local choices are both preserve or both swap.  No
claim is made that the surviving axis permutations are linear scalings;
they may be arbitrary low-degree one-variable permutation polynomials.

## 4. Exact coefficient extraction and bit complexity

Suppose \(F,G\) are supplied by a division-free straight-line circuit over
\(R\), using \(+,-,\times\) gates and explicitly encoded residue constants.
Assume the circuit's **exact formal output polynomials** have the promised
total-degree bound \(D\); it is not enough that the same finite-set function
has some unknown low-degree representative.  Let \(g\) be the gate count and
\(L\) the total encoded bit length, including every constant.
For each of the substitutions

\[
(K,X)=(Z,0),\qquad(K,X)=(0,Z),
\tag{4.1}
\]

evaluate every circuit gate in the truncated ring

\[
R[Z]/(Z^{D+1}).
\tag{4.2}
\]

An element is stored as \(D+1\) residues.  Addition and subtraction are
componentwise; a multiplication is an ordinary truncated convolution using
\(O(D^2)\) ring operations.  Because the final formal degrees are at most
\(D\), truncation loses no output coefficient.  The total cost is
\(O(gD^2)\) ring operations and bit time polynomial in

\[
L+D+\log N.
\tag{4.3}
\]

Take an integer gcd with \(N\) for each of the \(4(D+1)\) output
coefficients.

Condition (0.3) does not require knowing \(p,q\).  Scan the integers
\(2,3,\ldots,2D\) and compute their gcds with \(N\).  If a prime factor is at
most \(2D\), its own scan position returns that proper factor.  If the scan
finds none, then both prime factors exceed \(2D\), proving (0.3).  For
\(D=D_N\le P(n)\) under the fixed public numeric bound in the Outcome, this
scan and every coefficient extraction are polynomial in the input length.
It also disposes of characteristic two whenever \(D\ge1\).

Neither the global-bijection promise nor the exact formal-degree promise is
certified by this extractor.  A proposed sampler using such moves must prove
both semantic properties for its own circuits.  The theorem says that every
move which really has them is either factor-visible or
orientation-synchronized.

## 5. The synchronized branch preserves the factor-free region

Suppose the local orientations synchronize.  If the input is \((u,0)\)
with \(u\in R^\times\), both local inputs are nonzero points of the same
source axis.  Section 2 shows that both local outputs are nonzero points of
the same synchronized target axis.  CRT therefore makes the global output
either

\[
(u',0)\quad\text{or}\quad(0,u')
\]

with \(u'\in R^\times\).  The same holds from \((0,u)\), and the origin is
fixed locally and globally.  Thus every synchronized move maps
\(\mathcal A_N\) into itself.  Bijectivity gives equality, though forward
invariance is enough.

Now let a public adaptive selector use the current state, the whole previous
transcript, and fresh randomness.  At each realized history it must
**materialize an explicit circuit which is itself a promised global
bijection of all \(\Omega_N\)**.  Inspect that circuit's restrictions before
applying it.  A mixed orientation factors \(N\) by Section 3.  On the
no-factor branch it synchronizes and preserves \(\mathcal A_N\).  Induction
therefore proves the adaptive statement in the Outcome.  Independence,
stationarity, reversibility, and time homogeneity are not used.

This does not cover a stitched piecewise transformation
\(z\mapsto T_z(z)\) which is bijective only after combining its branches,
when an individual materialized branch \(T_z\) is not itself a promised
global bijection.  It also does not cover a selector that never exposes the
realized global circuit.

An initializer with probability \(\varepsilon_N\) outside
\(\mathcal A_N\) contributes exactly that probability to the monitored event
\(H\) when both coordinate gcds are checked.  If fresh independent
invocations of an expected-polynomial-cost initializer have one uniform
lower bound \(\varepsilon_N\ge1/P(n)\), verified repetition gives a Las Vegas
splitter on the distinct-semiprime subfamily.  It is not, without further
work, a complete all-input factoring theorem.  The fully quantitative
statement for arbitrary initializer and move contributions is (0.8).

## 6. Uniform target mass

At a prime \(r\), \(\Omega_r\) is the union of two \(r\)-point axes meeting
at the origin, so \(|\Omega_r|=2r-1\).  CRT gives

\[
|\Omega_N|=(2p-1)(2q-1).
\tag{6.1}
\]

The three disjoint pieces in (0.5) have total size

\[
|\mathcal A_N|=2\varphi(N)+1=2(p-1)(q-1)+1.
\tag{6.2}
\]

Subtracting yields

\[
|\Omega_N\setminus\mathcal A_N|=2N-2.
\tag{6.3}
\]

Finally,

\[
2(2N-2)-(2p-1)(2q-1)=2p+2q-5>0,
\tag{6.4}
\]

including \(p=2,q\ge3\).  This proves (0.7).  For any law \(\mu\) supported
on \(\mathcal A_N\), the event \(\Omega_N\setminus\mathcal A_N\) gives

\[
\|\mu-\pi_N\|_{\rm TV}
\ge\pi_N(\Omega_N\setminus\mathcal A_N)>\frac12.
\tag{6.5}
\]

## 7. Exact scope and reopen condition

Under one fixed public numeric bound \(D_N\le P(n)\), the small-factor scan
plus the theorem covers every distinct-semiprime input.  Suppose an
almost-surely terminating sampler uses only the covered materialized global
bijections, has unconditional terminal law \(\mu_N\), and has expected total
circuit encoding length at most one fixed polynomial \(Q(n)\).  Assume also
that the sampler's own bit and fair-bit costs have one fixed expected
polynomial bound.  Monitoring all coefficients adds expected polynomial bit
cost, and (0.8) gives

\[
\Pr(\text{a monitored check factors }N)
\ge \rho_N-\|\mu_N-\pi_N\|_{\rm TV}.
\tag{7.1}
\]

Thus a fixed TV error \(\delta<1/2\), together with fresh repeatable runs and
the stated uniform expected-cost bounds, gives a Las Vegas splitter on every
distinct semiprime with expected \(O((1/2-\delta)^{-1})\) runs.  This does
not refute the sampler: the sampler may succeed precisely by constructing a
factor-visible mixed-orientation move.  It also does not by itself give
complete all-input factoring.  As usual, one run's cost need not be
independent of its own success: with fresh streams, the event that run \(i\)
is reached depends only on earlier runs, so the expected stopped cost is the
geometric sum of unconditional one-run expectations.

A **factor-free** all-input sampler confined to this move model is ruled out,
because an all-input claim must in particular hold on every distinct
semiprime and then (7.1) forces TV error greater than \(1/2\).  No
classification over prime powers is needed for that narrow conclusion.

The following remain open:

1. characteristic-scale or succinctly high-degree finite-set permutation
   polynomials, where root counting no longer forces a polynomial identity;
2. noninvertible polynomial maps or stochastic kernels not decomposed into
   the promised bijections;
3. auxiliary variables, lifted chains, projections, tempering, and block or
   nonlocal updates outside this point-map model;
4. division/rational circuits, opaque evaluators, and stitched piecewise
   maps whose materialized branches are not themselves promised global
   bijections in the stated representation;
5. a repeatable warm-start construction with inverse-polynomial useful mass,
   which is credited directly as a distinct-semiprime splitter;
6. positive matching encodings or direct spectral samplers; and
7. prime-power geometry and nonsquarefree bases.

The degree threshold is a real algebraic boundary.  For example, over
\(\mathbb F_r\),

\[
f(Z)=1-Z^{r-1},
\qquad
g(Z)=Z^{r-1}
\]

have pointwise-zero product although neither is the zero polynomial.  This
does not itself construct a useful high-degree bijection, but it shows why
the proof cannot be extended merely by dropping (0.3).

A retry is materially new if it constructs one of the open mechanisms with a
proved stationary or target law and polynomial bit/fair-bit cost, proves a
wider orientation theorem in a precisely specified succinct model, or
actually produces factor-visible mixed low-degree bijections with a uniform
inverse-polynomial probability.  Composing more factor-free synchronized
low-degree bijections, changing their adaptive selection, or replacing
linear axis scalings by low-degree one-variable permutation polynomials
cannot leave the invariant region.
