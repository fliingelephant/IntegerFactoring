# Finite-field models of the original ring-inverse phase

**Family:** route:F31

**Status:** exact exploratory models, certificates, and a scoped algebraic
exclusion. No uniform low-genus model, selected-window evaluator, or
factoring algorithm is established.

## Mechanism and original-input coupling

The candidate was a finite-field rational trace for the complete period of
F310's ring-inverse phase, followed by algebraic point counting. It was
stated before primary-source checks. A total-sum bound was tested first;
failed elliptic models were followed by higher-pole fits and explicit
nonlinear coordinate changes.

Let M=2^k, L=M/2=2^s, q=L/2=2^m, so m=k-2. For odd N define

    f_N(x)=((N-1)/2-x)/(1+2x) mod L,
    phi_N(x)=top(x) xor top(f_N(x)).

The phase is periodic under x->x+L/2. On 0<=x<q, top(x)=0, so the
retained Boolean table is top(f_N(x)), and

    S_N=sum_(0<=x<q)(-1)^phi_N(x),
    halfbox_count=(q+S_N)/2.                               (1)

Every pilot input has N=8M+r with odd 1<=r<M/2. Thus M is the largest
power of two at most N/8. Changing N by M/2 complements every phase bit,
which the pilot checks exactly. Exhausting these r covers all original
residue phases up to complementation. No factors are supplied.

## 1. The first elliptic identification fails, including its pole correction

For a finite field F_q, the model

    phi(X)=Tr(aX+b/X)+epsilon

has two simple poles at zero and infinity when a,b are nonzero. Giving
the missing X=0 term either sign changes the complete nonzero-field sum
by only one. The genus-one Hasse bound therefore requires

    |S_N| <= 2 sqrt(q)+1.                                  (2)

The genus and Hasse ingredients are documented in PRIMARY_SOURCES.md.
The trace-to-point-count relation follows directly by counting the zero or
two solutions of Y squared+Y=R(X) at each nonpole.

For the actual input N=527, M=64, q=16, the phase has S_N=12 and truth
table hexadecimal 0x1008 in ordinary binary coordinates. This exceeds
the bound 9 in (2). Even allowing an elliptic Artin-Schreier description
with two finite rational poles and regular infinity gives at most three
exceptional signs, hence the weaker bound 11. The same witness exceeds it.
Constant or affine Boolean phases are treated separately; their degenerate
trace presentations must not be subjected to a connected-curve bound.

This excludes the proposed elliptic realization of that complete phase,
not higher genus or a different algebraic summation mechanism.

## 2. Walsh spectra give a stronger, carefully scoped discriminator

For a rational trace with fixed poles zero and infinity of odd orders at
most d,e, adding any linear Boolean mask is the same as adding Tr(aX).
It does not increase the genus g=(d+e)/2. Thus all Walsh coefficients
obey

    |W(ell)| <= 2g sqrt(q)+1.                               (3)

The same envelope applies under any affine F_2 coordinate change: it
permutes the Walsh magnitudes. It therefore tests more than one choice
of polynomial basis for the specified pole-at-infinity family.

This is NOT a blanket Walsh bound for arbitrary pole locations. If a model
has regular infinity, adding a linear term may create a new pole and raise
its genus. The output field `two_pole_genus_lower_bound` refers specifically
to (3), including its single filled finite pole. No general genus bound
from that field is claimed.

At q=128 and q=256, every exhaustively tested ordinary-coordinate phase
fails the genus-one envelope (3). The maximum observed magnitudes and
the resulting lower bounds within this two-pole family are:

| q | Ordinary maximum Walsh magnitude | Required genus from (3) |
|---:|---:|---:|
| 64 | 36 | 3 |
| 128 | 48 | 3 |
| 256 | 96 | 3 |
| 4096 | 416 | 4 |

The first three rows exhaust input residues up to complement; q=4096 is
a seeded sample. These finite numbers are not extrapolated to a genus
growth theorem.

## 3. Corrected model: explicit genus two at the failed elliptic input

The first corrected coordinate system uses the ring unit-group isomorphism

    u=(-1)^epsilon 5^t mod L,
    x=(u-1)/2, epsilon in {0,1}, 0<=t<q/2.

The m-bit label z=epsilon+2t gives a bijection of the same period domain.
Forward evaluation uses one modular power; no N or phase is changed.
The pilot calls this `sign_log`. It is a nonlinear coordinate change in
the ordinary binary bits, and its Walsh spectrum is therefore tested
separately. It does not turn integer interval masks into field intervals.

For N=527 this correction gives an exact genus-two representation. Use
F_16=F_2[alpha]/(alpha^4+alpha+1), and identify the bits of z with its
polynomial-basis field element X. At X other than zero and one,

    phi_N(x(z))=Tr(alpha^3+(1+alpha)X
                            +alpha^2/[X(X+1)]).             (4)

At zero and one the actual phase is zero. Equation (4) has simple poles
at zero, one, and infinity, so its smooth Artin-Schreier curve has genus
two. The curve has 27 rational points, independently counted in the pilot;
its Frobenius trace is -10. The two filled phase signs are both +1, so
the complete phase total is 10+2=12, exactly the original S_N.

This is a faithful corrected nonlinear model for one actual input, not
a fitted total alone. CERTIFICATES_output.json retains the field
coefficients, pole signs, truth-table equality, and direct curve count.
The same three-simple-pole fitting family does not extend uniformly:
it fits no tested ordinary or sign/log input at q=64,128,256. Even the
structured continuation r=q-1 fails this fixed genus-two model from q=32.

## 4. Higher rational trace fits and an exact nonmembership certificate

Over an explicitly verified polynomial-basis F_(2^m), the pilot fits

    epsilon + Tr(sum_(j odd<=D) a_j X^j+b_j X^(-j))

with a freely filled zero-pole value. This is a linear system over F_2 in
the coefficient bits. Every positive fit is checked against the complete
truth table. The search also separately tests pole orders (3,1), (1,3),
and three simple poles at zero, one, infinity.

At q=32 all ordinary phases fit the symmetric order-five family. At
q=64 their first fits require order11 or21; at q=128 they require21.
At q=256 none of the 512 ordinary/sign-log tables fits symmetric odd
orders through31. These are fixed-coordinate, fixed-pole statements;
arbitrary pole sets, further coordinate changes, and other rational trace
families remain untested.

For N=8193, M=1024, ordinary coordinates, CERTIFICATES_output.json gives
a 256-bit dual vector. It annihilates all258 coefficient columns of the
order31 family but pairs to one with the target table. The column rank is
210. This is an exact replayable nonmembership certificate for that family,
not a scalar-summation lower bound. At smaller fields a large fitting space
can fill the entire truth-table space, so a successful high-order fit alone
is not evidence of compression.

## 5. Another nonlinear correction: quadratic pullbacks

The second correction tests the explicit bijections X->X^(-1)+a in the
finite field, defining inverse zero to be zero. Its search menu is a=0,1
everywhere and every center a for a bounded subset at q<=64, in both prior
encodings. A search stops when it finds a quadratic model; the output
records only the centers actually visited.
If the pulled-back phase is Boolean quadratic, its total is evaluated by
exact quadratic elimination rather than enumerating its signs:

    sum_(u,v in F_2)(-1)^(uv+uA+vB+R)=2(-1)^(AB+R).

Repeating this identity has polynomial cost in m when the quadratic
coefficients are supplied. The implemented evaluator matches all found
quadratic pullbacks. At q=16, four ordinary-coordinate inputs have such
models, including N=513 with total -4. No tested pullback is quadratic
at q=32,64,128,256. Many totals also violate the necessary weight spectrum
of any quadratic Boolean function: a nonzero quadratic total is a signed
power of two of magnitude at least 2^ceil(m/2). This latter check is invariant
under every permutation, but is only a quadratic-model exclusion.

Thus the cycle does not stop at the first Hasse failure: it constructs a
corrected genus-two model, tests larger rational families, and implements
a different nonlinear reduction with a genuine fast terminal evaluator.
None supplies a uniform small description of the required phases.

### A single free pole value cannot repair a failed quadratic pullback

For q>=8, every original S_N is divisible by four. Indeed, the halfbox
set is invariant under u->N/u modulo M. Its nonfixed points occur in pairs.
If square roots of N exist modulo M, exactly two of the four odd roots lie
below M/2; otherwise there are no diagonal points. Thus halfbox_count is
even, and (1) gives S_N=0 modulo 4.

Every quadratic Boolean sum on m>=3 bits is also divisible by four:
its nonzero magnitude is at least 2^ceil(m/2). A coordinate bijection
preserves S_N. Consequently a pulled-back phase that differs from a
quadratic Boolean function at just one point is impossible: the two totals
would differ by exactly plus or minus two. Agreement away from that point
therefore forces agreement at the point as well.

This also covers a possible free value at the finite pole in the tested
inverse-coordinate models. After X->X^(-1)+a, a rational trace whose
only pole is the finite point a, of order at most five, becomes the trace of a
polynomial of degree at most five away from zero. All exponents from one
to five have binary weight at most two, so this is Boolean quadratic.
Allowing the original pole its freely filled bit cannot rescue a failed
full quadratic fit. This consequence applies only to the centers and
encodings actually tested; it does not exclude other nonlinear changes or
multiple-pole models.

## 6. Cost and scope of the research result

The first pilot took 1.028 seconds and 20,365,312 peak RSS bytes. It
exhausted m=3 through8 up to complementary N, and sampled m=9 through12.
The final quadratic-pullback pilot took 0.150 seconds and 22,773,760 bytes.
The certificate pilot used about0.04seconds and23MiB. All identities,
fits, ranks, and curve-point checks use exact finite arithmetic.

The pilots enumerate truth tables and field coefficient columns. That
discovery work is exponential in m and is not the proposed evaluator.
Even an efficiently constructed model for this one complete halfbox phase
would not yet implement P239. Arbitrary interval indicators or Walsh masks
must be transported through each coordinate change and integrated at
controlled cost. They are not discarded or replaced by the complete sum.

The next concrete opening is a uniform rational trace model with moving
poles or another nonlinear normal form whose coefficients and retained
masks can be computed from N in small complexity. The data do not establish
that such a model exists, nor do they exclude it.
