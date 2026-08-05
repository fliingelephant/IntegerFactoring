# F22 — hostile audit of the real-quadratic infrastructure metric boundary

**Status:** corrected hostile audit.  No computation was run.  This report uses
only exact symbolic calculations and the cited primary papers.

## Verdict

The central counterexample is correct after narrowing:

- for

  \[
  a=6t+1,\qquad N=a^2+2,\qquad \Delta=4N,
  \]

  the ordinary continued fraction of \(\sqrt N\) has period
  \([\overline{a,2a}]\);
- in the Gower--Wagstaff reduction convention, the complete reduced proper
  principal-form cycle of discriminant \(4N\) is exactly

  \[
  F_+=(1,2a,-2),\qquad F_-=(-2,2a,1);
  \]

- the only SQUFOF square encountered is the right coefficient \(1=1^2\)
  of \(F_-\), and the queue/list test certifies it as improper; hence the
  entire unmultiplied principal cycle contains no proper SQUFOF square;
- every coefficient of either reduced endpoint is coprime to \(N\).

This is a genuine counterexample to the exact auxiliary assertion that every
composite input has a useful proper square on its unmultiplied principal
cycle.  It is not an obstruction for a factoring driver, a metric joint
decoder, or even the richer transcript on this family: every member has the
public factor \(3\), and the same period-two condition is immediately
recognizable from the input.

The infrastructure facts also survive with two qualifications.  Reduction
does not preserve a doubled distance by itself: the reducing multiplier must
be retained.  And the Buchmann--Vollmer bound is a bit-time and bit-space
upper bound for their particular algorithms with a power-product output,
where \(R\) is the *numeric regulator*, not its bit length and not a supplied
search bound.

The exact SQUFOF iteration cap in the candidate is misstated by floors and
constants, and the displayed symmetry identity is not by itself always an
integer factorization without the parity normalization in the algorithm.
Neither error affects the \(\Theta(N^{1/4})\) versus polylogarithmic
distinction.

The corrected theorem merits proof-blind reconstruction, but the reconstruction
should be asked to recover only the exact two-form/no-proper-square theorem,
the precisely qualified infrastructure facts, and the heuristic scope.  It
should not be asked to reconstruct a lower bound for intermediate transcripts
or arbitrary real-quadratic algorithms, because no such result has been
proved.

## 1. Sources and conventions checked

The audit checked the claims against:

1. Jason E. Gower and Samuel S. Wagstaff, Jr., [*Square Form
   Factorization*](https://homes.cerias.purdue.edu/~ssw/squfof.pdf),
   Sections 2--5, especially Sections 3.1--3.3, 4.2--4.6, and 5:
   reduction equation (2.1), continued-fraction equations
   (2.2)--(2.4), the exact algorithm in Section 3.3, Assumptions 4.5,
   4.11--4.19 and 4.23, and the multiplier hypotheses in Propositions
   5.1, 5.6 and Theorems 5.4, 5.8;
2. Johannes Buchmann and Ulrich Vollmer, [*A Terr algorithm for
   computations in the infrastructure of real-quadratic number
   fields*](https://doi.org/10.5802/jtnb.558),
   Propositions 2.2--2.3, Lemmas 3.2 and 3.4, Proposition 4.1,
   power-product formula (12), and Proposition 7.1.

The McMath--Crabbe--Joyner paper is not needed for any corrected complexity
claim below.  Its form normalization differs from the ordinary
\(\sqrt N\) recurrence used here, so it should not be used silently to bridge
the two conventions.

## 2. Exact arithmetic of the counterfamily

### 2.1 Input properties, including repeated factors

For \(t\ge1\), \(a=6t+1\) is odd and

\[
N=a^2+2
 =36t^2+12t+3
 =3(12t^2+4t+1).
\]

The second factor is greater than one, so \(N\) is composite.  Also
\(N\equiv3\pmod4\), and

\[
a^2<N<a^2+2a+1=(a+1)^2,
\]

so \(N\) is not a square and \(\lfloor\sqrt N\rfloor=a\).

The family is not uniformly squarefree.  For \(t=1\),

\[
N=51=3\cdot17
\]

is squarefree and \(\Delta=204\) is fundamental.  If
\(t\equiv2\pmod3\), then

\[
12t^2+4t+1\equiv t+1\equiv0\pmod3,
\]

so \(9\mid N\); for example \(t=2\) gives
\(N=171=3^2\cdot19\).  The recurrence and primitive-form proof below
remain valid for these nonfundamental discriminants.  The statistical
analysis in Gower--Wagstaff does not: its Assumption 4.5 explicitly requires
a squarefree \(N\) with distinct large odd prime factors.

Most importantly, \(3\mid N\) is visible without any infrastructure
arithmetic.  A standard factoring driver that trial-divides by fixed small
primes never sends this family to SQUFOF.  Even without that preprocessing,
the condition

\[
N-\lfloor\sqrt N\rfloor^2=2,\qquad
\lfloor\sqrt N\rfloor\not\equiv0\pmod3
\]

immediately proves \(3\mid N\).  Thus the family cannot witness that a
negative cycle transcript is factor-free.

### 2.2 Continued-fraction recurrence

Starting from

\[
(P_0,Q_0,q_0)=(0,1,a),
\]

the exact recurrence gives

\[
P_1=a,\quad Q_1=N-a^2=2,\quad
q_1=\left\lfloor\frac{a+P_1}{Q_1}\right\rfloor=a,
\]

and then

\[
P_2=a,\quad Q_2=\frac{N-a^2}{2}=1,\quad
q_2=2a.
\]

The next state is \((P_3,Q_3)=(a,2)\), so the two noninitial states
repeat.  Equivalently,

\[
\sqrt N=[a;\overline{a,2a}].
\]

This calculation is valid for every \(t\ge1\) and does not assume
squarefreeness.

### 2.3 Direct bridge to the complete proper principal cycle

It is safer to check the Gower--Wagstaff reduction map directly than to infer
a form-cycle length from a continued-fraction slogan.  Their equation (2.1)
is

\[
\rho(A,B,C)=
\left(C,r(-B,C),\frac{r(-B,C)^2-\Delta}{4C}\right),
\]

where \(r(-B,C)\) is the unique congruent middle coefficient in the
specified reduction interval.

Both displayed forms are primitive and have discriminant \(4N\).  For
\(F_+\), the unique middle coefficient is \(r=2a\), because

\[
r+2a\equiv0\pmod{-4},\qquad
2\sqrt N-4<2a<2\sqrt N.
\]

Therefore

\[
\rho(F_+)
=\left(-2,2a,\frac{4a^2-4N}{-8}\right)
=(-2,2a,1)=F_-.
\]

For \(F_-\), again \(r=2a\), now because it is even and

\[
2\sqrt N-2<2a<2\sqrt N.
\]

Consequently

\[
\rho(F_-)
=\left(1,2a,\frac{4a^2-4N}{4}\right)
=(1,2a,-2)=F_+.
\]

The form \(F_+\) is the reduced principal form: it is the unique reduced
form with leading coefficient \(1\) in this convention.  Since \(\rho\)
moves to the unique adjacent reduced form within the same proper-equivalence
class, and \(\rho\) swaps the two forms, these are all reduced forms in the
proper principal cycle.  This proves the convention bridge exactly, including
orientation and signs.

The coefficient-gcd claim is also exact:

\[
\gcd(a,N)=\gcd(a,a^2+2)=\gcd(a,2)=1,
\]

and \(N\) is odd.  Hence

\[
\gcd(c,N)=1
\quad\text{for every }c\in
\{\pm1,\pm2,\pm2a\}.
\]

## 3. Which SQUFOF square is tested

For \(N\equiv3\pmod4\), the continued-fraction and binary-form versions
of Gower--Wagstaff agree at discriminant \(\Delta=4N\).  The relevant
square form has a *positive right coefficient* \(C=c^2\), and only the
appropriate parity of the cycle index is tested.

Here \(F_+\) has right coefficient \(-2\), whereas

\[
F_-=(-2,2a,1^2)
\]

is the only oriented square occurrence.  This is the same occurrence as the
leading coefficient \(1\) of the associated orientation; it is not a second
proper square.

The exact queue test makes its impropriety transparent.  Initially the
continued-fraction state has \(Q=2\), so Step 2b enqueues

\[
(Q/2,P\bmod(Q/2))=(1,0).
\]

At the next even square test, the new denominator is \(1\), its positive
square root is \(r=1\), and the queued pair \((1,0)\) satisfies the
congruence test.  Step 2d then declares that the whole principal period has
been traversed without a proper square.  The binary-form version says the
same thing: the initial sufficient list contains \(1\), and encountering
\(C=1\) stops the cycle as improper.

Thus full traversal really contains no proper SQUFOF square.  This is stronger
than missing the square within a query cap, but it is only a statement about
this exact standard trigger.

The candidate's factorization identity needs a parity qualification.  At the
reverse-cycle symmetry one has

\[
N=S_m\left(S_{m-1}+S_m\frac{t_m^2}{4}\right),
\]

but the displayed parenthesized quantities need not both be integers.  When
the relevant output coefficient is even, Gower--Wagstaff divides it by two
before output.  On the present improper square, \(t_m=a\) is odd and the
unadjusted display visibly contains a half-integer.  The algorithm's
parity-normalized coefficient is the candidate divisor.  Independently
checking \(1<d<N\) and \(d\mid N\), or applying \(\gcd(d,N)\), remains
a sound verification wrapper.

## 4. Reduced endpoints do not audit richer transcripts

The endpoint statement is valid: proper composition stays in the proper ideal
class, and complete reduction of any principal-class result must end at
\(F_+\) or \(F_-\).  It follows that no endpoint coefficient-gcd test
produces a nontrivial divisor on this family.

The ordinary sequential recurrence is also transparent.  Its values lie in

\[
P_i=a,\qquad Q_i\in\{1,2\},\qquad
q_i\in\{a,2a\}.
\]

In the direct \(\rho\) calculations, the selected middle coefficient is
\(2a\), and the numerator \(r^2-\Delta\) is \(-8\).  All gcds of
these individual quantities with odd \(N\) are \(1\), except that an
implementation may materialize \(N\) itself, whose gcd is the trivial full
modulus.

This does not prove that arbitrary composition intermediates are harmless.
For example, a generalized composition of \(F_-\) with itself may first
produce an unreduced principal form such as \((1,0,-N)\) before reduction.
Different exact composition algorithms expose different extended-gcd
coefficients, quotients, and relative generators.  The two-element reduced
endpoint set does not constrain all arithmetic functions of that transcript.
Nor does it constrain a joint decoder combining several power products or
distance relations.

There is no factor-revealing arithmetic *failure* in the displayed standard
recurrence: every asserted division is exact and both forms are primitive.
But the negative event “the period is this two-cycle” is itself useful on this
manufactured family, because it identifies \(N=a^2+2\) and hence the public
factor \(3\).  Therefore this family cannot support any claim that failure
events, intermediate data, or the full transcript contain no efficiently
decodable factor information.

The candidate correctly flags this gap in its hostile-audit targets.  Its
classification must retain that exclusion.  What is closed is only:

> reduced-endpoint localization by a proper-square/single-form trigger on the
> unmultiplied principal cycle.

Composition/reduction transcript decoders remain materially open.

## 5. Infrastructure distance audit

### 5.1 Definition and injectivity

For a principal fractional ideal \(\mathfrak a=(\alpha)\), the convention

\[
d(\mathcal O_\Delta,\mathfrak a)
=\frac12\log\left|
\frac{\sigma(\alpha)}{\alpha}
\right|\pmod R
\]

is well-defined, since changing \(\alpha\) by a power of a fundamental unit
changes the value by an integer multiple of \(R\).  It is a homomorphism on
principal ideals.  Buchmann--Vollmer explicitly prove that its restriction to
the reduced principal ideals is injective in \(\mathbb R/R\mathbb Z\).

All these ideals map to the identity in the ordinary ideal class group, so
ordinary class arithmetic indeed forgets their positions.  Proper binary-form
equivalence corresponds to the narrow convention; this distinction does not
invalidate the statement that the displayed principal-cycle ideals are
ordinary-principal, but the two class notions should not be silently
identified.

### 5.2 Reduction corrections are essential

If \(\mathfrak a\) and \(\mathfrak b\) are principal, then

\[
d(\mathfrak a\mathfrak b)
=d(\mathfrak a)+d(\mathfrak b)\pmod R.
\]

If their product is reduced by

\[
\mathfrak c=\delta\mathfrak a\mathfrak b,
\]

then

\[
d(\mathfrak c)
=d(\mathfrak a)+d(\mathfrak b)
 + \tfrac12\log|\sigma(\delta)/\delta|
 \pmod R.
\]

Thus a reduced endpoint alone does not carry the exact sum.  Infrastructure
arithmetic retains it by also storing the reducing multiplier, normally as a
power product or straight-line representation.  Repeated squaring doubles
the unreduced ideal's distance; after each reduction, its correction must be
included.  The candidate's “repeated squaring doubles a known distance” is
valid only with this tracked correction.

### 5.3 Gap and precision statements

Buchmann--Vollmer Lemma 3.2 gives, for consecutive reducing numbers,

\[
\frac1{\sqrt\Delta}<\delta_i
 <\frac12\log\Delta,
\qquad
\delta_i+\delta_{i+1}>\log2.
\]

The first lower bound shows that a certified absolute approximation with
\(O(\log\Delta)\) binary fractional bits can separate adjacent positions.
The second bound does *not* say that every single gap is bounded below by a
positive constant; only every pair is.

If approximate distances are doubled \(K\) times, errors can magnify by
\(2^K\), so one needs \(K+O(\log\Delta)\) guard bits, not merely a
fixed \(O(\log\Delta)\) precision independent of the operation count.
For \(K=\operatorname{poly}(\log\Delta)\), this is still polynomial
precision.  Exact ideal encodings and exact power products avoid using a
floating comparison as the equality certificate.

### 5.4 Power-product sizes

A reduced ideal has \(O(\log\Delta)\)-bit coefficients.  In the
Buchmann--Vollmer construction, each stored reduction multiplier has
\(O((\log\Delta)^2)\) bits in their representation, and the output
relative generator is the power product in their equation (12).  A run with
\(K\) multiplication/reduction nodes therefore has a straight-line or
power-product representation of size \(K\operatorname{poly}(\log\Delta)\);
binary exponents created by \(K\) repeated squarings have only \(O(K)\)
bits.

This does not make a full regulator run polynomial.  TerrUnit stores
\(O(\log\Delta+\sqrt R)\) reduced ideals and multipliers.  Expanding the
fundamental unit would require \(\Theta(R)\) output bits in general, so the
power-product output convention is essential.

### 5.5 This family has a small regulator

The period-two continued fraction gives the Pell unit

\[
\varepsilon=(a^2+1)+a\sqrt N=(N-1)+a\sqrt N,
\]

because

\[
(a^2+1)^2-N a^2=1.
\]

It is the fundamental positive unit supplied by the period-two continued
fraction.  Hence

\[
R=\log\bigl((N-1)+a\sqrt N\bigr)=\Theta(\log N).
\]

So on the counterfamily itself, the Terr search bound is polynomial in
\(\log N\).  The counterfamily witnesses absence of a proper-square target,
not a large-regulator or precision obstruction.

## 6. What the Terr bound actually proves

Buchmann--Vollmer Proposition 7.1 states

\[
O\left((\log\Delta+\sqrt R)(\log\Delta)^2\right)
\]

time **and space** for TerrUnit and, for reduced input ideals, TerrEquivalent.
Their analysis counts bit-sized ideal operations: reduction is quadratic in
\(\log\Delta\), table lookup costs \(O(\log\Delta)\), and each stored
multiplier has polynomial bit size.

Here \(R=\log\varepsilon\) is the numeric regulator.  Thus
\(\sqrt R\) means the square root of that real number, not the square root
of the bit length of \(R\), and not an externally supplied upper bound.
In the worst case the paper rewrites the result as
\(|\Delta|^{1/4+o(1)}\), which is exponential in the binary input length.

TerrEquivalent as first presented uses a previously computed approximation to
\(R\) to set a stopping value, but the paper explains a two-giant-sequence
variant that avoids that precomputation and retains the same asymptotic bound.
The extended discrete-logarithm discussion in Section 8 has an additional
group-order parameter and should not be summarized as having exactly the
same \(\sqrt R\) bound.

Accordingly:

- it is correct that coefficient expansion and floating-point precision are
  not automatic obstructions to a polynomial number of infrastructure
  operations;
- it is correct that the cited exact regulator/equivalence algorithms have a
  potentially exponential \(\sqrt R\) search term;
- this is only an upper bound for specified algorithms, never a lower bound
  for all infrastructure algorithms.

## 7. SQUFOF time, heuristics, and multiplier scope

### 7.1 Exact cap

For the continued-fraction algorithm with \(N\equiv2,3\pmod4\),
Gower--Wagstaff set

\[
L=\left\lfloor2\sqrt{2\sqrt N}\right\rfloor,
\qquad B=2L.
\]

Since \(\Delta=4N\), this is

\[
B=2\left\lfloor2\Delta^{1/4}\right\rfloor,
\]

not \(4\lfloor\Delta^{1/4}\rfloor\).  In the separate binary-form
description they set \(d=\lfloor\sqrt\Delta\rfloor\),
\(L=\lfloor\sqrt d\rfloor\), and \(\mathrm{Bound}=4L\).
Both are \(\Theta(\Delta^{1/4})\), so both configured caps are exponential
in \(\log N\).

This is an exponential worst-case cap/upper bound, not an exponential lower
bound on the number of steps of every successful run.  In fact the displayed
counterfamily terminates its unmultiplied failure after a constant-size cycle.

### 7.2 Heuristic assumptions

The paper explicitly says its complexity calculation is heuristic and omits
inputs whose principal cycle has no proper square.  For fixed numbers of
distinct large prime factors, the \(\Theta(N^{1/4})\) average prediction
uses more than the four assumptions listed in the candidate.  It includes:

- squarefreeness and the “large odd prime factors” regime (Assumption 4.5);
- averaging assumptions that distribute reduced forms and square forms among
  narrow cycles and genera (Assumptions 4.11--4.16);
- the ratio-of-averages spacing rule (Assumption 4.17);
- uniform landing among the reduced ambiguous forms after inverse square root
  (Assumption 4.19);
- for queue space, the queue-density model (Assumption 4.23).

The exponential/memoryless law used to explain racing multipliers is stated
later as a conjecture supported by experiments.  It is not a per-input theorem
and is not part of an all-input Las Vegas analysis.

Thus Gower--Wagstaff supplies neither a uniform inverse-polynomial probability
of a useful square nor a polylogarithmic expected-work theorem.

### 7.3 Multipliers

The multiplier analysis assumes:

- squarefree \(N\) with distinct large odd prime factors;
- a squarefree product of distinct known small odd primes, each coprime to
  \(N\) and smaller than every unknown prime factor;
- explicit size inequalities on the multiplier in Proposition 5.6;
- the same heuristic averaging assumptions used in the unmultiplied analysis.

The algorithm removes known multiplier factors from the extracted coefficient:
in the continued-fraction version it replaces \(Q\) by
\(Q/\gcd(Q,2m)\) before output.  For an arbitrary experimental multiplier,
one should first compute \(\gcd(m,N)\), then apply the universally safe
wrapper \(\gcd(d,N)\) to any extracted candidate and return only a verified
proper divisor.  Those checks prove correctness of a returned answer, but
they supply no success probability and do not extend the paper's average
formulas to repeated factors, arbitrary multipliers, or adversarial inputs.

The candidate is therefore right that racing multipliers has no required
worst-case probability theorem.  It should cite the full hypothesis list
rather than treating the paper's “optimal multiplier” calculation as a
general extraction result.

## 8. Shifted-marker lemma

The generic lemma is correct exactly as stated.  Fix the random coins and
follow the all-negative transcript.  The adaptive queries are then fixed
positions \(x_1,\ldots,x_T\).  A first positive answer can occur only for

\[
\tau\in\bigcup_{i=1}^T(x_i-M),
\]

whose cardinality is at most \(Ts\).  Averaging over the coins gives
\(\Pr(\mathrm{success})\le\min(1,Ts/L)\).  If only \(K^2\) pair
relations are explicitly tested, substitute \(T\le K^2\).

No infrastructure lower bound follows.  The real infrastructure is not a
finite cyclic group with a uniformly translated hidden marker set; its
coefficients, reducing multipliers, and gaps depend arithmetically on the
discriminant.  A joint decoder may learn from negative answers or from
unmarked coefficients without ever making a positive membership query, which
is explicitly forbidden in the lemma's oracle model.

The lemma therefore distinguishes “pool more membership lotteries” from “use
a joint arithmetic decoder,” but it does not show that the latter is
impossible or expensive.  The candidate's caveat is essential and survives.

## 9. Strongest corrected theorem

**Theorem (corrected F22 boundary).**  Let \(t\ge1\),
\(a=6t+1\), \(N=a^2+2\), and \(\Delta=4N\).  Then:

1. \(N\) is an odd nonsquare composite, \(N\equiv3\pmod4\), and
   \(3\mid N\).  The case \(t=1\) is squarefree; some other cases have
   repeated factors.
2. The exact complete-denominator recurrence for \(\sqrt N\) has
   \(P_i=a\) for \(i\ge1\), alternating
   \(Q_i\in\{2,1\}\), and partial quotients alternating
   \(a,2a\).  Hence
   \(\sqrt N=[a;\overline{a,2a}]\).
3. Under the Gower--Wagstaff \(\rho\)-reduction and sign convention, the
   complete reduced proper principal cycle of primitive forms of
   discriminant \(4N\) is

   \[
   (1,2a,-2)\longleftrightarrow(-2,2a,1).
   \]

4. The only oriented positive right square coefficient on that cycle is
   \(1\).  The exact queue/list criterion marks it improper and recognizes
   completion of the period.  Therefore the unmultiplied cycle contains no
   proper SQUFOF square.
5. Every coefficient of either reduced endpoint is coprime to \(N\).
   Consequently, complete traversal, arbitrary jumping whose only observed
   output is a reduced endpoint, and the standard single-form
   coefficient-gcd/proper-square trigger cannot reveal a nontrivial factor on
   this family.

This theorem does not cover:

- any factoring driver that notices the public factor \(3\);
- multiplier changes or another discriminant;
- unreduced composition coefficients, reduction quotients, relative
  generators, distance power products, or failure-event decoders;
- joint arithmetic relations among polynomially many forms;
- a different factor-bearing observable in the real infrastructure;
- a worst-case lower bound for sequential SQUFOF, Terr's algorithm, or any
  other real-quadratic method.

## 10. Promotion recommendation

**Verdict:** the candidate contains a real, exact, and materially new
counterexample, but several surrounding sentences must be narrowed as above.
The exact iteration cap, parity wording, reduction-distance correction, Terr
parameter interpretation, and heuristic hypothesis list should be corrected
before promotion.

**Blind reconstruction:** yes.  Give a fresh agent only the corrected theorem
in Section 9 plus these key ideas:

- derive the period from \(N=a^2+2\);
- apply the published \(\rho\) map directly to both forms;
- audit the queue/list handling of \(Q=1\);
- distinguish reduced endpoints from intermediate transcripts;
- verify the Buchmann--Vollmer distance/gap/power-product/Terr statements
  with \(R\) interpreted as the numeric regulator;
- recover the public-factor and repeated-factor exclusions.

No cross-family audit has run.
