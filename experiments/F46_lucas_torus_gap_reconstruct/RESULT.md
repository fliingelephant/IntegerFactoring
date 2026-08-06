# Fresh reconstruction for F27/F46

## Verification disposition: PASS

This is an independent reconstruction from the bare theorem package.  Throughout,

\[
N=pq,\qquad 3\leq p<q,
\]

where (p,q) are distinct odd primes, and
(n=\lceil\log _2(N+1)\rceil).  Write \(\chi_r\) for the Legendre
character on \(\mathbb F_r^*\).  The notation \((+,-)\) means
\(\chi_p(D)=+1,\chi_q(D)=-1\), and \((-,+)\) has the opposite
meaning.

## 1. The quadratic algebra and the Cayley element

Let (R=\mathbb Z/N\mathbb Z), let (D\in R^*\), and set

\[
A_D=R[w]/(w^2-D).
\]

Every element has a unique expression (a+bw).  Multiplication,
conjugation, and norm are

\[
(a+bw)(c+dw)=ac+Dbd+(ad+bc)w,
\]
\[
\overline{a+bw}=a-bw,
\qquad
\operatorname {Nm}(a+bw)=(a+bw)(a-bw)=a^2-Db^2.
\]

Conjugation is an (R)-algebra involution, and the norm is
multiplicative.  For every \(\alpha\in A_D\),

\[
\alpha\in A_D^*quad\Longleftrightarrow\quad
\operatorname {Nm}(\alpha)\in R^*.
\]

Indeed, a unit has unit norm by multiplicativity.  Conversely, if the
norm is a unit, then
\(\alpha^{-1}=\bar\alpha\operatorname {Nm}(\alpha)^{-1}\).
In particular, every norm-one element is a unit and has inverse equal
to its conjugate.

For (t\in R\), put (z_D(t)=1-Dt^2\).  Both (1-tw) and (1+tw)
have norm (z_D(t)), so, exactly when (z_D(t)) is a unit, both are
units and

\[
(1-tw)^{-1}=(1+tw)z_D(t)^{-1},
\qquad
(1+tw)^{-1}=(1-tw)z_D(t)^{-1}.
\]

Thus the clean Cayley element is

\[
\begin{aligned}
U_D(t)
  &=(1+tw)(1-tw)^{-1}\\
  &=\frac{(1+tw)^2}{1-Dt^2}\\
  &=\frac{1+Dt^2}{1-Dt^2}
    +\frac{2t}{1-Dt^2}w .
\end{aligned}
\]

Its conjugate is (U_D(-t)=U_D(t)^{-1}), and

\[
\operatorname {Nm}(U_D(t))
=\frac{\operatorname {Nm}(1+tw)}
       {\operatorname {Nm}(1-tw)}=1.
\]

These statements are ring statements; no division by a nonunit has
been used.

## 2. The exact finite-field Cayley parametrization

Let (r) be an odd prime, (D\in\mathbb F_r^*\), and

\[
T_D(\mathbb F_r)=
\{x+yw:x^2-Dy^2=1\}.
\]

This is the norm-one subgroup of (A_D^*).  The map

\[
c_D:\{t\in\mathbb F_r:1-Dt^2\ne0\}
\longrightarrow T_D(\mathbb F_r)\setminus\{-1\},
\qquad t\longmapsto U_D(t),
\]

is a bijection.  The displayed coefficient formula proves that its
image lies in the torus.  Its first coordinate (x) satisfies

\[
x+1=\frac{2}{1-Dt^2}\ne0,
\]

so (-1=(-1,0)) is not in the image.  Conversely, if
(x+yw\in T_D(\mathbb F_r)) is not (-1), then (x+1\ne0): if
(x=-1), the norm equation and (D\ne0) force (y=0).  Define

\[
t=\frac{y}{x+1}.
\]

Using (Dy^2=x^2-1), one gets

\[
Dt^2=\frac{x-1}{x+1},
\qquad
1-Dt^2=\frac{2}{x+1}\ne0.
\]

Substitution into the coefficient formula gives back (x+yw), and
also shows directly that the inverse is unique.

The torus order is exactly

\[
|T_D(\mathbb F_r)|=r-\chi_r(D).
\]

If (D=\delta^2\), the isomorphism

\[
a+bw\longmapsto(a+b\delta,a-b\delta)
\]

identifies the algebra with \(\mathbb F_r\times\mathbb F_r\), the norm
with coordinate product, and the torus with
(u\mapsto(u,u^{-1})) for (u\in\mathbb F_r^*\).  Its order is
(r-1).  If (D) is a nonsquare, the algebra is
\(\mathbb F_{r^2}\).  Euler's criterion gives
\(w^r=wD^{(r-1)/2}=-w\), so the displayed conjugation is precisely
Frobenius and the displayed norm is (a\mapsto a^{r+1}\).  On the
cyclic group of order (r^2-1), that power map has kernel of order
\(\gcd(r^2-1,r+1)=r+1\).  This proves the formula in both cases.

All exceptional points are now explicit.  In the split case the two
distinct poles are

\[
t=\delta^{-1}\quad\hbox{and}\quad t=-\delta^{-1};
\]

there are no poles in the nonsplit case.  The finite value (t=0)
maps to (1).  The single torus point (-1) is the missing point of
the affine Cayley chart.  There are no other omissions.  Thus the
domain sizes are (r-2) in the split case and (r) in the nonsplit
case, matching \(|T_D|-1\).  This is a parametrization of every listed
point, not a generator claim; in particular, nothing here assumes a
sampled point generates the torus.

## 3. The exact (D)-first distribution and gcd laws

### Orientation and discriminant gcd

For a unit (D\bmod N),

\[
\left(\frac DN\right)=\chi_p(D)\chi_q(D).
\]

Consequently, Jacobi symbol (-1) permits exactly the two orientations
((+,-)) and ((-,+)\).  CRT and the fact that exactly half of the
nonzero residues modulo each prime are squares give

\[
\#\{D:(\chi_p(D),\chi_q(D))=(+,-)\}
=\#\{D:(\chi_p(D),\chi_q(D))=(-,+)\}
=\frac{(p-1)(q-1)}4.
\]

Thus a uniform unit (D) of Jacobi symbol (-1) has a fair
orientation.  Fresh independent choices of (D) give independent
fair orientation bits.  Conditional on ((+,-)), (D_p) is uniform
among nonzero squares, (D_q) is uniform among nonsquares, and those
two local choices are independent; the analogous statement holds for
((-,+)\).

The polynomial (X^2-D) has discriminant (4D).  Since (N) is odd,

\[
\gcd(4D,N)=\gcd(D,N).
\]

For an arbitrary candidate residue (D), this gcd is (p) exactly
when (D_p=0,D_q\ne0), is (q) exactly when
(D_q=0,D_p\ne0), is (N) exactly when (D=0\bmod N), and is (1)
exactly when (D) is a unit.  Hence every proper discriminant gcd is
already an exact prime factor.

### Denominator gcd

Fix a retained unit (D) of Jacobi symbol (-1), let (t) be uniform
modulo (N), and put (z=1-Dt^2).  In orientation ((+,-)), choose
(\delta_p^2=D_p).  The exact law is

\[
\gcd(z,N)=
\begin{cases}
p,&t_p=\delta_p^{-1}\text{ or }t_p=-\delta_p^{-1},\\
1,&\text{otherwise}.
\end{cases}
\]

There are no (q)-local zeros because (D_q) is a nonsquare.  Thus
the two probabilities are (2/p) and (1-2/p), respectively.  In
orientation ((-,+)\), choosing (\delta_q^2=D_q), the exact law is

\[
\gcd(z,N)=
\begin{cases}
q,&t_q=\delta_q^{-1}\text{ or }t_q=-\delta_q^{-1},\\
1,&\text{otherwise},
\end{cases}
\]

with probabilities (2/q) and (1-2/q).  A denominator gcd of (N)
is impossible after such a (D) is retained, because one local
factor is nonsplit and therefore has no pole.

### Choose (D) first

The ideal clean sampler is the following.

1. Draw uniform residues (D\bmod N) until (D) is a unit with
   Jacobi symbol (-1), and retain that (D).
2. Keeping this same (D), draw uniform (t\bmod N) until
   (1-Dt^2) is a unit.
3. Return ((D,U_D(t),U_D(t)^{N-1})).

Rejection from a uniform finite set makes the retained (D) uniform
on the required Jacobi class.  Given (D), CRT makes (t_p,t_q)
independent and uniform.  Conditioning on cleanliness is conditioning
on a Cartesian product of local allowed sets.  Hence the two local
variables remain independent: at the split prime, (t_r) is uniform
on \(\mathbb F_r\) minus its two poles, while at the nonsplit prime it
is uniform on all of \(\mathbb F_r\).  By the bijection in Section 2,
in either case (U_r) is uniform on

\[
T_D(\mathbb F_r)\setminus\{-1\}.
\]

This is the exact conditional local point law.  It includes all
non-generators.  With fresh randomness, different clean triples,
including their retained (D)'s and local points, are independent.

The expected number of (t)-draws for fixed orientation is exactly

\[
\mathbb E[T_t\mid(+,-)]=\frac p{p-2},
\qquad
\mathbb E[T_t\mid(-,+)]=\frac q{q-2}.
\]

Each is at most (3).  Redrawing the whole pair ((D,t)) after a pole
would not implement this law: its two orientation acceptance weights
would be (1-2/p) and (1-2/q).  In particular,

\[
\Pr((+,-)\mid\text{whole-pair acceptance})
=\frac{1-2/p}{(1-2/p)+(1-2/q)},
\]

which is not (1/2) because (p\ne q).  Keeping (D) while retrying
(t) is therefore essential.

### Exact random-bit and bit-operation costs

There is an exact uniform-residue implementation which uses no
factoring information.  Draw an (n)-bit integer (X) and accept it
as a residue exactly when (0\le X<N).  A uniform residue then costs
exactly

\[
B_N=\frac{n2^n}{N}
\]

expected unbiased random bits.  The ideal (D)-stage accepts a
uniform residue with probability

\[
\frac{\varphi(N)}{2N}
=\frac{(p-1)(q-1)}{2pq}.
\]

It therefore uses exactly (2N/\varphi(N)) expected residue draws and

\[
\frac{2n2^n}{\varphi(N)}
\]

expected random bits.  Conditional on orientation, the (t)-stage
uses exactly

\[
B_N\frac p{p-2}\quad\hbox{or}\quad
B_N\frac q{q-2}
\]

expected bits.  Averaging over the fair orientation, one ideal clean
triple therefore has the exact expectations

\[
\mathbb E[\text{residue draws}]
=\frac{2N}{\varphi(N)}
 +\frac12\left(\frac p{p-2}+\frac q{q-2}\right),
\]

\[
\mathbb E[\text{random bits}]
=B_N\left[
\frac{2N}{\varphi(N)}
 +\frac12\left(\frac p{p-2}+\frac q{q-2}\right)
\right].
\]

For distinct odd (p<q), the bracket is at most (73/12), attained
at the extremal pair (p=3,q=5); in particular it is an absolute
constant.  For (K) independent triples, these sampler expectations
are multiplied by (K).

All tested integers and all reduced algebra coefficients have
(O(n)) bits.  Uniform-residue rejection, gcd, Jacobi-symbol
evaluation, modular inversion, and the displayed coefficient
arithmetic all have polynomial bit cost.  With schoolbook arithmetic,
one may safely bound each gcd/Jacobi/inversion by (O(n^3)), each
modular algebra multiplication by (O(n^2)), and binary powering to
the (n)-bit exponent (N-1) by (O(n^3)).  Thus an ideal triple has
expected (O(n^3)) bit cost and (K=\operatorname {poly}(n)) triples
have expected polynomial bit cost.  No arithmetic-operation count is
being substituted for bit complexity, and modular reduction keeps all
intermediate stored operands polynomially bounded.

### Early gcd returns: the required coupling

An implementation should compute every candidate discriminant gcd and
every denominator gcd.  It may return immediately on a proper gcd.
The decoder guarantee below must not be justified by claiming that
orientations remain fair after conditioning on no such return.

Instead couple a real sampler (R) to the ideal sampler (I) on one
infinite random tape.  On a candidate (D) with proper
(\gcd(4D,N)), (R) returns the factor while (I) merely rejects the
candidate and continues.  A gcd of (N) is rejected by both.  On a
retained (D), if a candidate (t) has a proper denominator gcd,
(R) returns it while (I) rejects that (t) and continues.  If no
early return occurs while (K) triples are built, the triples built by
(R) are literally the first (K) triples built by (I).

Let (E) be the event of an early proper gcd, and let (B) be the
event that the decoder succeeds on the counterfactual full ideal
sample on the same tape.  The real procedure succeeds on

\[
E\ \cup\ (E^c\cap B)=E\cup B,
\]

so its success probability is at least \(\Pr(B)\), the promised ideal
probability.  This coupling, rather than a generally false
conditional-fairness assertion, is what preserves the decoder
guarantee.

## 4. The gap exponent identity, pointwise

Put (g=q-p>0), and use coefficientwise CRT to view a clean norm-one
element as (U=(U_p,U_q)\).  In orientation ((+,-)), the two exact
ambient torus orders are (p-1) and (q+1).  The exponent congruences
are

\[
pq-1\equiv q-1\equiv q-p=g\pmod {p-1},
\]

\[
pq-1\equiv-p-1\equiv q-p=g\pmod {q+1}.
\]

Therefore (U^{N-1}=U^g).  In orientation ((-,+)\), the exact orders
are (p+1) and (q-1), and

\[
pq-1\equiv-q-1\equiv p-q=-g\pmod {p+1},
\]

\[
pq-1\equiv p-1\equiv p-q=-g\pmod {q-1}.
\]

Therefore (U^{N-1}=U^{-g}).  Exponent congruence modulo the order of
the ambient group implies equality for every group element.  The
argument neither replaces the ambient order by the element order nor
assumes that (U_p) or (U_q) is a generator, so the identities are
pointwise and include the identity and every proper-subgroup element.

## 5. Exact conditional reduction to factoring the promised inputs

Here is the premise with its quantifiers made explicit.  Suppose there
is one uniform classical decoder (\mathcal D), fixed independently
of (N,p,q), and fixed polynomials (K,P_{\rm dec},P_{\rm suc}), such
that for every product (N=pq) of distinct odd primes, on input (N)
and (K(n)) independent ideal clean triples from Section 3,
(\mathcal D)

* uses at most (P_{\rm dec}(n)) bit operations and random bits, and
* outputs the integer (g=q-p) with probability at least
  (1/P_{\rm suc}(n)).

The probability includes both the clean-triple randomness and any
decoder randomness.  Then the following is a classical Las Vegas
expected-polynomial factoring algorithm on precisely that promise.
Independently repeat:

1. Build (K(n)) triples, returning any proper discriminant or
   denominator gcd immediately as a factor.
2. Run (\mathcal D), obtaining a candidate integer (h).
3. Reject unless (h>0) and (h<N).
4. Compute \(\Delta=h^2+4N\), compute its integer square root (s),
   and reject unless (s^2=\Delta).
5. Reject unless (s\equiv h\pmod 2).  Set
   \(p'=(s-h)/2\), \(q'=(s+h)/2\).
6. Reject unless (1<p'<N), (1<q'<N), and (p'q'=N).  Otherwise
   return (p',q').

These are all integer checks.  In particular, checking merely a
floating-point square root would not suffice.  The true value (h=g)
passes because

\[
g^2+4N=(q-p)^2+4pq=(p+q)^2,
\]

and (p+q\) and (q-p) have the same (indeed even) parity.  It then
recovers (p'=p,q'=q).  Conversely, every decoder-based return has
been checked to be a nontrivial exact factor pair; every gcd-based
return is a checked proper divisor.  Hence every return is correct.
On the stated semiprime promise the quotient of a proper gcd is the
other prime.

By the coupling in Section 3, one outer trial succeeds with probability
at least

\[
\epsilon(n)=1/P_{\rm suc}(n),
\]

whether or not early gcd events themselves bias the surviving sample.
All inner rejection samplers terminate almost surely.  Fresh outer
random tapes make trials independent, so the probability of surviving
(m) trials is at most \((1-\epsilon(n))^m\), which tends to zero.
Thus termination is almost sure.

One trial has expected bit cost

\[
O(K(n)n^3+P_{\rm dec}(n)),
\]

including exact random sampling, algebra arithmetic, exponentiation,
the decoder, integer square root, and verification.  For example,
binary search using exact (O(n))-bit integer comparisons and
multiplications computes and certifies the square root in polynomial
bit time; no square-testing oracle is implicit.  If (T_j) is
the cost of trial (j), independence of a fresh trial from the event
that earlier trials failed and Tonelli's theorem give

\[
\mathbb E\!\left[\sum_{j=1}^{J}T_j\right]
=\frac{\mathbb E[T_1]}{\Pr(\text{one-trial success})}
\le P_{\rm suc}(n)\,O(K(n)n^3+P_{\rm dec}(n)),
\]

which is polynomial in the input bit length.  The same argument bounds
expected random bits by a polynomial.  This proves the exact
conditional Las Vegas reduction.

It is not an all-input reduction.  It gives no algorithm for prime
squares, general prime powers, products of three or more prime factors,
even composites, arbitrary composites, or complete recursive
factorization.  Nor does it supply a decoder.  Those cases and that
premise remain open within this package.

## 6. Generic shared-exponent theorem

### Model and statement

Let (\ell) be prime and (K\ge1).  Group (i) is a cyclic group of
order (\ell) represented by an independently uniform injective
encoding into a finite label set of size at least (\ell).  Handles
are tagged by their group, so handles of different tags are never the
same group element.  The algorithm receives, in group (i), handles
for the exponent expressions

\[
0,\qquad 1,\qquad \sigma_i e,
\qquad \sigma_i\in\{+1,-1\}
\]

relative to a fixed abstract generator; the signs and (\ell) are
public.  The secret (e) is uniform in \(\mathbb F_\ell\).  The
algorithm may adaptively request group addition, inversion, and
known-scalar multiplication, may compare any already obtained handles,
and may perform arbitrary ordinary computation on all tagged
transcripts.  It obtains at most (Q) oracle-operation output handles
in total.  It cannot submit fabricated labels as valid handles; if a
model permits successful guessing of unseen encodings, a separate
label-space guessing term is necessary.

Under exactly this handle model, its probability of outputting (e)
is at most

\[
\boxed{
\min\left\{1,\frac1\ell+
\frac{\binom{Q+3}{2}+3(K-1)}\ell\right\}.}
\]

### Symbolic simulation and adaptivity

Run a symbolic oracle without choosing (e).  Every handle in group
(i) carries a formal affine expression

\[
a+bX\in\mathbb F_\ell[X]
\]

of degree at most one.  Group operations, inversion, and
known-scalar multiplication preserve this form, even when the
operation, scalar, and group are selected adaptively from all earlier
labels.  Equal formal pairs ((a,b)) receive the same label.  A new
formal pair receives a fresh uniformly sampled unused label for that
tag.  Label samples for distinct tags are independent.  Thus repeated
formal expressions and every equality they cause are shown to the
algorithm exactly, rather than being counted as secret-dependent
collisions.

Fix the algorithm's random tape and all random labels in this symbolic
execution.  Its entire adaptive path, its final numerical guess (y),
and all formal expressions on that path are now fixed independently of
the secret.  For two formally distinct expressions in one tagged
group,

\[
(a+bX)-(c+dX)
\]

is a nonzero affine polynomial.  It vanishes at at most one
(e\in\mathbb F_\ell).  Let (B) be the union of these roots over all
within-tag pairs occurring on the symbolic path.  Cross-tag pairs are
not included: the encodings are independent and the tags are disjoint,
so even equality of two raw label payloads across tags supplies no
group equation.

If (e\notin B), all formally distinct expressions within each tag
evaluate to distinct group elements.  Assigning their labels without
replacement has exactly the marginal distribution induced by a
uniform random injective encoding.  Consequently the real execution
and symbolic execution have identical transcripts and output (y).
If (e\in B), the real algorithm may notice a label equality and take
a completely different adaptive path; charging the whole event
(e\in B) covers this behavior.  This first-divergence coupling treats
adaptive label choices and noticed equality without assuming a
nonadaptive query sequence.

Initial coincidences are included.  Within a group the three initial
formal expressions have three pairs.  The pair (0,1) never collides,
while (0,\sigma_iX) can collide at (e=0) and
(1,\sigma_iX) can collide at (e=\sigma_i).  Counting all three
pairs is a valid, slightly loose, uniform bound.  Repeated expressions
created later have zero formal difference and are canonicalized, so
they create no bad root.

### Exact collision count and success bound

Let (q_i\) be the number of operation-produced handles tagged by
group (i), so \(\sum_iq_i\le Q\).  There are at most (q_i+3)
handle occurrences in that group, hence at most
\(\binom{q_i+3}{2}\) relevant pairs.  Since the (q_i)'s are
nonnegative,

\[
\begin{aligned}
\sum_{i=1}^K\binom{q_i+3}{2}
&=\frac12\sum_i(q_i^2+5q_i+6)\\
&\le\frac12(Q^2+5Q+6K)\\
&=\binom{Q+3}{2}+3(K-1)=:C.
\end{aligned}
\]

Therefore \(|B|\le C\).  For each fixed symbolic execution, success
on a good secret requires (e=y), accounting for at most one secret,
while all bad secrets account for at most (C) more.  Averaging over
the symbolic labels and the algorithm's randomness gives

\[
\Pr(\widehat e=e)\le\frac{1+C}{\ell}.
\]

Taking the minimum with the trivial bound (1) proves the boxed
claim.

This also handles finite label spaces.  If (C+1\ge\ell), the stated
minimum is the trivial bound (1), so no fresh-label simulation is
needed.  If (C+1<\ell), no tag can contain more than \(\ell\)
distinct formal expressions: otherwise its pair count alone is at
least \(\binom{\ell+1}{2}\ge\ell>C\).  A label universe of size at
least \(\ell\) therefore always has enough labels for the symbolic
path.  More intrinsically, any path with more than \(\ell\) distinct
formal expressions in one tag has a collision for every secret by the
pigeonhole principle, which can occur only in the parameter range
where the displayed upper bound is already trivial.

### Three exact extensions

The same fixed-symbolic-transcript count gives the following, with the
same (C\).

* If (e) is uniform on a public set
  (S\subseteq\mathbb F_\ell) of size (H\), then
  \[
  \Pr(\widehat e=e)\le\min\{1,(1+C)/H\}.
  \]
  Each collision polynomial contributes at most one member of (S),
  and a fixed good-transcript guess contributes at most one.
* If (e) is uniform on \(\mathbb F_\ell\) and the algorithm outputs a
  list of at most (L) candidates, then
  \[
  \Pr(e\text{ is in the list})\le\min\{1,(L+C)/\ell\}.
  \]
* For an arbitrary public prior \(\mu\) on \(\mathbb F_\ell\), put
  \(\mu_*=\max_x\mu(x)\).  Then
  \[
  \Pr(\widehat e=e)\le\min\{1,(C+1)\mu_*\}.
  \]
  The union of at most (C) collision roots has mass at most
  (C\mu_*\), and the one fixed good-transcript guess has mass at most
  \(\mu_*\).

For each extension, if the nontrivial right-hand side is below (1),
its parameters imply (C<\ell), so the finite-label argument above
continues to apply.

## 7. Scope audit and the exact remaining gap

The theorem in Section 6 is only a generic, independently
random-encoded, tagged, common-prime-order handle theorem.  It is not a
lower bound for explicit Lucas coordinates over \(\mathbb Z/N\mathbb
Z\).  In particular, it does not cover or rule out:

* arithmetic relating coordinates from different discriminants,
  including resultants and gcds;
* unequal and generally composite local torus orders;
* non-generators and elements in proper subgroups of those composite
  tori;
* deterministic worst-case factor gaps rather than a secret sampled
  from the stated distributions;
* interval discrete-logarithm algorithms or other representation-aware
  algorithms;
* zero divisors, whose gcds can expose a factor;
* prime powers, multifactor composites, even inputs, or arbitrary
  composites.

It also says nothing about a model in which an algorithm exploits the
bit representation of explicit group elements or successfully guesses
previously unseen finite-space labels.  The prime-order, random-label,
tag-separation, handle-only, affine-operation, and (Q)-output
assumptions are all essential to the proved statement.

Conceptually, spectral/order routes try to extract information from
orders or exponent spectra, whereas succinct torus-product routes try
to combine many torus relations in a compact representation.  The
semiprime identities above expose a signed shared gap exponent, and
the generic theorem marks a boundary for one opaque-group
idealization.  These are comparisons of mechanisms only: none of the
three routes subsumes either of the others.

The exact remaining constructive gap is a uniform polynomial-bit
decoder with inverse-polynomial success under the clean (D)-first
law.  Even if that decoder were supplied, a further exact gap would be
the extension from distinct odd semiprimes to all integers and the
complete-recursion bit-complexity proof.  Therefore the identities and
generic boundary do not supply either the decoder or the top-level
factoring theorem required by `PROMPT.md`.

## Final checks

**Verification disposition: PASS.**  Every claim in the supplied bare
package has been reconstructed above with its quantifiers, exceptional
points, distribution, and bit-cost scope.  The conditional reduction
is deliberately labeled conditional and promise-only.

Proof provenance check: this reconstruction did not inspect either
prohibited F46 proof directory and did not use a candidate-proof
summary.  Proof-only check: no finite experiment or web search was
used.  Byte/presentation check: this file is plain UTF-8 Markdown with
balanced fenced structure (there are no code fences), balanced display
math delimiters, a literal PASS disposition, and no embedded binary or
NUL content.
