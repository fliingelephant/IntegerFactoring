# Guarded digit circuits on the original inverse graph

**Family:** route:F31

**Scope:** integer-valued rational circuits, dyadic interval indicators,
and whole-graph modular traces.

## Constructive result and remaining operation

A canonical dyadic interval indicator has a rational straight-line circuit
with O(k log k) arithmetic gates and 2k bits of modular working precision,
when its input is modulo M=2^k and its output is requested modulo M.
Two such circuits, composed with u and the 2-adic inverse N/u, give the
original rectangle count modulo M. Since the count is at most M/2, this
residue is its exact integer value.

This supplies a succinct positive selector, including guard bits and original
input coupling. It does not supply a polynomial-cost whole-graph trace of
that circuit. P238 supplies traces of a numerical degree bank of monomials
modulo M squared; its statement does not permit nonlinear circuit gates to
be moved through the trace. The exact Taylor calculation below identifies
why derivative flatness alone does not provide that extension.

## Mechanism, stated before record checks

The initial candidate was repeated parity extraction and exact division by
two. A power x^(2^P) would select parity modulo 2^P, but Newton lifting
gives a shorter circuit. Define

    E_0(X)=X,
    E_(t+1)(X)=3 E_t(X)^2 - 2 E_t(X)^3.

For an integer or 2-adic integer x, let epsilon be its parity in {0,1}.
If E_t(x)=epsilon mod 2^h, the next iterate is epsilon mod 2^(2h).
For epsilon=0 this follows from E_t squared; for epsilon=1 use

    E_(t+1)-1 = -(E_t-1)^2 (2E_t+1).

Thus E_t(x)=epsilon mod 2^(2^t). Let E[P] denote the iterate with
t=ceil(log2 P). It has O(log P) gates and degree 3^ceil(log2 P).
The polynomial (X-E[P](X))/2 is integer-valued, since its numerator is
even at every integer X. No inversion of two in a residue ring is used.

## Exact guard schedule

For an output precision p, start with X_0=x modulo 2^(p+k). At step j,
0<=j<k, use P_j=p+k-j and compute

    b_j = E[P_j](X_j) mod 2^P_j,
    X_(j+1) = ((X_j-b_j) mod 2^P_j)/2.

The division is exact on the even canonical representative. Induction gives

    X_j = floor(x/2^j) mod 2^(p+k-j),
    b_j = bit_j(x) mod 2^p.

Here floor uses any canonical representative of the original x; changing
x by a multiple of 2^(p+k) does not change any requested bit. The same
argument defines the bits of a 2-adic integer.

For I=[A,A+2^s), with 0<=A<M and A divisible by 2^s, form

    I_I(x) = product_(s<=j<k) [b_j if bit_j(A)=1, else 1-b_j].   (1)

Equation (1) equals the indicator of x mod M in I, modulo 2^p. The
integer-valued rational circuit is fixed by public A,s,k,p. It uses only
small constants, addition, multiplication, and the exact divisions above.
It has O(k log(p+k)) gates and O(p+k)-bit modular operands. Its bit cost
per input is O(k log(p+k)) modular multiplications plus polynomial overhead.
This is stronger than merely writing the degree-2^(k-1) Mahler selector.
It is standard Newton idempotent lifting applied with guard bits; no novelty
claim is made for Newton lifting or succinct bit extraction.

## Faithful inverse-graph coupling and exact count

For each odd u<M, compute U=u and V=N/u in Z_2 to precision p+k.
The canonical inverse coordinate v_N(u) is V modulo M. Therefore

    C_(I,J)(N,M)
      = sum_(u odd<M) I_I(u) I_J(N/u) mod 2^p.                 (2)

This identity uses the same original N and both original public windows;
there is no averaging over N, residue charts, or translated windows.
Taking p=k recovers C exactly because 0<=C<=M/2<M. The largest pointwise
precision is then 2k, numerically the precision of P238's moment residues.
This equality of precision counts does not identify their computational
interfaces: P238 evaluates linear combinations of monomial traces whose
division guards are supported by its proved precision, whereas (2) requests
the trace of a composed integer-valued circuit.

A straightforward exact algorithm evaluates (1) point by point. Its bit
cost is O(M k log k) modular operations on O(k)-bit operands, including
polynomial-cost modular inversions. This is an explicit end-to-end count
bound, but it is exponential in k. A fast trace primitive for the particular
circuits (1), after the substitution V=N/u, is the remaining operation.

## Test of the derivative-flatness contraction

Consider only the top-bit selector, p=k, on the fixed odd class u=1+4t.
Let

    e = 2^ceil(log2(k+1)).

At the center t=0, all prior quotient circuits have constant term zero
after the first quotient, and their linear coefficients divide by two at
each step. The input to the last parity extractor consequently has linear
term 2^(3-k)t. Since E[ k+1 ](X) at zero has first nonzero term
3^(e-1) X^e, the exact rational Taylor series of the final selector has

    coefficient of t^j = 0, 0<=j<e,
    coefficient of t^e = 3^(e-1) / 2^((k-3)e).                (3)

This is a calculation on the full composed circuit, not on an isolated
intermediate denominator. For k>3 the Taylor polynomial through the first
nonzero term is nonintegral at t=1, although the full circuit is
integer-valued everywhere. Terms omitted from that truncation must cancel
its negative valuation. Vanishing low derivatives therefore does not justify
a low-index monomial truncation modulo 2^p.

The first coefficient alone would require moment numerator precision at
least p+(k-3)e before its division could be performed separately. This is
O(k squared), still polynomial, but it is outside the proved 2k-bit P238
interface and is not sufficient to justify discarding later coefficients.
No exponential precision lower bound is claimed. The issue is preservation
of integer-valued cancellation by a whole-circuit functional.

There is also a sharp limited polynomial comparison. On t=0,...,H, with
H=2^(k-3), the desired top bit is zero below H and one at H. For any
rational polynomial P integer-valued on these points and agreeing modulo
two, its H-th finite difference is odd. Thus deg P>=H. This excludes a
low-degree ordinary polynomial replacement on this class. It excludes
neither the succinct circuit above nor another compressed trace algorithm.

The concrete ansatz tested here is: "high derivative flatness permits
truncating the selector's ordinary Taylor series at its first surviving
polynomial-degree band and applying P238 termwise." Equation (3) gives an
exact counterexample to that ansatz. It does not refute circuit averaging.

## Prior comparison

Rust search and reads used P238, C264, P177, and
experiment:F200_beta2_dyadic_harmonic_boundary. P238 is explicitly scoped
to polynomial cost in the numerical degree and residues modulo M squared.
C264 records next carry corrections and the unproved higher-precision bank;
its huge-exponent refinements do not establish circuit closure. F303's
input-Mahler experiment concerns a carry correction as a function of N,
whereas (1) selects canonical coordinate bits at fixed N.

P177/F200 concern a rational harmonic defect whose ordinary integer part is
not selected by value-local residue tests. That statement is not an obstacle
to (1): the present input is a canonical residue u modulo M, so its requested
digit is specified by finite 2-adic data. The obstruction here is aggregate
evaluation cost, not nonexistence of a finite-precision selector.

## Finite evidence and next discriminating question

`pilot.py` tested 32 reproducibly randomized original-N dyadic rectangles
for k=3 through 10. Every N is odd and lies in [8M,16M), so M is the
largest power of two at most N/8. All 73,696 individual digit checks and
all rectangle totals matched exact canonical-inverse enumeration. The
second selector was evaluated at N/u modulo 2^(2k), not by supplying the
canonical v as its input. Factors were not used.

Exact rational Taylor jets for k=4 through 8 verified (3). The denominator
guard counts were 8,16,24,32,80; the corresponding P238 precision budgets
were 8,10,12,14,16. All tested first-band truncations were nonintegral.
Runtime was 0.036 seconds and peak RSS 17,563,648 bytes. This is finite
verification of the identities, not evidence for a fast trace.

The useful next question is whether the global modular functional can
accept Newton idempotent gates and exact divide-by-two gates together,
retaining their integer-valued cancellations, without expanding into a
numerical degree bank. A successful rule must handle the correlated pair
I_I(u) I_J(N/u), preserve precision under division, and supply a total
state bound. The pointwise circuit and the guard schedule above give a
concrete input class for that question.
