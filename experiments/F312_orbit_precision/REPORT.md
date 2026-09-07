# Sign, inversion and half-translation at the next precision layer

**Family:** route:F31

Author-derived candidate, with named exact finite checks. No
factoring algorithm, uniform K evaluator, or external novelty claim follows.

The useful result is a two-bit compression of the *values* in the nonuniform
quadratic correction. It works for every square class. At modulus 8, the
remaining weight is a signed one-bit selector. This does not decrease the
inverse-graph modulus. The faithful half-translation tests show that generic
eight-element orbits still contribute modulo 8; their size does not by itself
supply another three bits of divisibility.

## Concrete candidate and scope

The starting candidate was to sum exact sign/inversion/half-translation
orbits before constructing a recursively growing carry bank. The closest
records were F305's fixed carry measure and F308's full R polarization and
square-diagonal modulo-4 formula. No current literature was fetched. All
claims below follow from finite algebra; tests guided which cancellation to
retain.

Let M=2^k, k>=3, and let epsilon be an odd unit. Define

    i(w)=epsilon*w^-1 mod M,
    H_epsilon(f)=sum_(odd w<M) f(w) f(i(w)),
    U(f)=sum_(odd w<M) f(w)^2,
    Q_epsilon(f)=H_epsilon(f)-U(f).

The maps i and sign s(w)=M-w commute and are involutions. The target
K(A,A) of F308 is H_1(f) for f(w)=floor(Aw/M). Epsilon in {1,3,5,7}
keeps all four unit square classes visible. No mixed epsilon term is
assumed computable.

## Two-bit compression theorem

Suppose r and g are integer-valued functions satisfying

    r(-w)=-r(w),   g(-w)=-g(w),
    r(w)=g(w) mod 2^(p-2),   p>=3.

Then

    Q_epsilon(r)=Q_epsilon(g) mod 2^p.                         (1)

This is a value-precision statement, with no promise that g has a fast
global trace. It holds for arbitrary odd epsilon, including exceptional
roots of both epsilon and -epsilon.

Proof: put q=2^(p-2), r=g+qt. Then t is also antisymmetric under sign. Let

    D(g,t)=sum g(w)t(i(w))-sum g(w)t(w).

On a generic four-element orbit {w,-w,i(w),-i(w)}, D contributes
-2[g(w)-g(i(w))][t(w)-t(i(w))]. On an orbit where i(w)=-w it contributes
-4g(w)t(w); where i(w)=w it contributes zero. Hence D is even. The same
orbit argument shows Q_epsilon(t) is even. Expanding gives

    Q_epsilon(r)-Q_epsilon(g)=2q D(g,t)+q^2 Q_epsilon(t).

The first term is divisible by 4q=2^p. The second is divisible by
2q^2=2^(2p-3), which is at least 2^p for p>=3. This proves (1).

For odd canonical A, set

    f(w)=floor(Aw/M),  h=(A-1)/2,  r(w)=f(w)-h.

Because f(-w)=A-1-f(w), r is antisymmetric. For w<M/2 choose

    g(w)=(f(w)-h) mod 2^(p-2),
    g(M-w)=-g(w).

The subtraction of h changes H and U by the same amount. Thus

    H_epsilon(f)=U(f)+H_epsilon(g)-U(g) mod 2^p.                (2)

At p=3, g takes only 0,1,-1. The ordinary U(f) is a degree-two Euclidean
floor marginal. U(g) is also explicitly computable in this case:

    U(g)=2 sum_(odd w<M/2)
          [floor(Aw/M)-h-2 floor((Aw-Mh)/(2M))].

Only ordinary degree-one floor sums occur. The remaining H_epsilon(g) is
a signed binary overlap. It is not constructed here. For general p the
statement is the exact precision reduction (2); no separate fast evaluator
for its growing residue alphabet is asserted.

## An unsigned modulo-8 form and its exceptional roots

For the same unshifted f, put a(w)=f(w) mod 2, and

    C_epsilon=sum a(w)a(i(w)),  n_a=sum a(w).

Then

    H_epsilon(f)=U(f)-n_a+C_epsilon
       -4 sum_[w<M/2, w^2=-epsilon mod M] (f(w)-h mod 2)
                                                         (mod 8).   (3)

Proof: H-U=-1/2 sum [f(w)-f(i(w))]^2. On a generic sign/inversion orbit,
the contribution is -2 delta^2 modulo 8, determined only by delta parity.
The binary overlap gives that same contribution. Fixed inversion points
contribute zero. For i(w)=-w, delta=2(f(w)-h), and the two-element sign
orbit contributes the displayed exceptional correction. Each such sign
class is counted once by w<M/2.

The ordinary n_a equals

    sum floor(Aw/M)-2 sum floor(Aw/(2M)),

so it has a polynomial-bit ordinary floor evaluator. The at most four
exceptional roots are also computable by guarded dyadic square-root lifting.
For epsilon=1,3,5 the exceptional root family is empty. For epsilon=7 it
must be retained. The overlap C_epsilon modulo 8 remains unknown.

For M=16,A=5, the actual K modulo 8 is 0 while U(f) modulo 8 is 2.
Thus the surviving binary contribution cannot simply be set to zero.

## Exact half-translation norm

Put L=M/2 and h_map(w)=w+L mod M. It commutes with sign and i. For general
integer d, the exact floor increment is

    f_(A,d)(h_map(w))-f_(A,d)(w)
      = (A-1)/2 + 1((Aw-d) mod M>=L)-A*1(w>=L).              (4)

The top bit and canonical-wrap term are both essential.

For the unshifted quadratic form, consider a generic eight-element orbit
under sign, i and h_map. Write

    delta=f(w)-f(i(w)),
    e=[f(h_map(w))-f(w)]-[f(h_map(i(w)))-f(i(w))].

Its exact contribution to H-U is

    -2[delta^2+(delta+e)^2].

Modulo 8 this is

    -2[(delta mod 2)+((delta+e) mod 2)].                       (5)

Consequently a translation parity change e=1 modulo 2 makes the norm equal
to 6 modulo 8; when e is even the norm is 0 or 4. The generic norm does
not vanish uniformly. Retained faithful examples use the same orbit

    M=32, orbit={3,5,11,13,19,21,27,29}.

For A=3 its contribution is 4 modulo 8; for A=5 it is 6. These separate
the proposed automatic orbit-size cancellation from the actual floor
family. They do not rule out aggregation of the surviving binary weights.

Exceptional orbits are controlled by the root families

    w^2 in {epsilon,-epsilon,epsilon-L,L-epsilon} mod M.

They have bounded size and can be handled separately. This does not
evaluate the growing family of generic orbit weights.

## Full intercepts and input cuts: exact dyadic quotient

The preceding antisymmetry is an unshifted condition, not a permission to
drop the cut. For a general two-function product, take a odd modulo L,
b=epsilon*a^-1 mod L, and

    c=(epsilon-ab)/L mod 2.

The two inverse lifts are (a,b+Lc) and (a+L,b+L(1-c)). For functions x,y
on canonical residues modulo M define

    P_x(a)=x(a)+x(a+L),  Q_x(a)=x(a)-x(a+L),

and similarly for y. Their exact contribution is

    [P_x(a)P_y(b)+(-1)^c Q_x(a)Q_y(b)]/2.                    (6)

For x(w)=floor((Aw-d)/M),

    P_x(a)=floor((Aa-d)/L)+(A-1)/2,
    Q_x(a)=-(A-1)/2-1((Aa-d) mod M>=L).                      (7)

These formulas allow signed d. To compute a target modulo 2^p, retain the
numerator modulo 2^(p+1), prove it is even, and divide in the integers.
Formula (6) halves the graph modulus but introduces a carry-signed product
of the two explicit Q weights; no closed total state bound is supplied.

Ordinary input/output intervals are retained by multiplying the two lift
values by their actual masks before forming P and Q. The F308 cut pullback
uses, on the inverse coordinate, the explicit function

    y(u)=1(Bu mod M<c0)-B*1(u<c0).

Its two values y(b),y(b+L) are handled by the same formula. Since B is odd,
the modular image also shifts by L; it is not constant on the two lifts.

The modulo-8 parity simplification must not be applied directly after
breaking sign antisymmetry. For M=16,A=3,d=2, the shifted quadratic sum is
6 modulo 8; the naive unsigned parity formula without a boundary correction
gives 2. This failed extension is preserved in the output. Formula (6)
continues to hold with both intercepts and both interval masks present.

## State accounting and what this cycle establishes

The successful step compresses a nonuniform quadratic correction from full
integer floor values to p-2 residue bits. At p=3 only one signed bit remains,
and all of the displayed non-overlap terms have polynomial-bit constructors.
The original graph still contains M/2 units. Literal sign/inversion quotient
enumeration has about M/8 generic classes; adding half-translation leaves
about M/16. These are exponential in k. Neither enumeration is proposed as
an efficient evaluator.

Repeated use of (6) has a decreasing modulus but retains a carry character
and sharp masks. This packet does not prove that its bank has polynomial or
quasipolynomial total size. The binary overlap in (2)/(3) and the signed
product in (6) are precise, tested remaining operations. The mathematical
gain is the exact value-precision compression and its boundary scope, not
another claimed complete K constructor.

## Experiment record

`pilot.py`, `pilot.json`, and `pilot.log` retain all source and output. The
seed is 312. For M=16 through 512, the pilot checked 43 general dyadic
quotients, 43 quotients with both interval cuts, 43 unshifted parity
reductions, 172 square-class forms of (3), 716 precision-compression
identities, and 538 complete sign/inversion/half-translation orbits. It also
retains nonzero generic norms, failed shifted extensions, and five explicit
eight-point translation carry truth tables.

The pilot took 0.020 seconds at 17,891,328 bytes peak RSS under a 30-second
alarm. Preflight at approximately 10:06 on 2026-09-07 found a 16 GiB host,
load averages 2.13,2.41,2.31, and no large active research job in the busy
process snapshot. The experiment estimate was below one second and 32 MiB.
No large benchmark or shared record was changed.
