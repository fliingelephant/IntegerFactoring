# F317: interpolation Cauchy products and the moving block carry

**Family:** route:F31

Family: route:F31. Status: author-derived identities and exact bounded
checks; unpromoted. No restricted-moment or factoring algorithm is supplied.

## Question and closest prior

The question is whether F314's restricted Hadamard moments admit a fast
whole-prefix sum through normalized Cauchy products and dyadic blocks.
C261 and experiment:F300_salie_cauchy were inspected through the Rust reader
and its scoped packet. Their denominators are Fourier Cauchy denominators;
complete Gauss summation retains a position-sensitive quadratic digit.
Here the kernel is a rational interpolation Cauchy kernel. Its individual
products do have a polynomial-bit evaluator, but block summation retains the
explicit moving quotient below. This does not invoke a special-function
identity or claim external novelty. P240's bounded-degree moments of one
canonical map do not provide the carry histogram used here.

## Exact kernel, including its apparent poles

Let L=2^s, d=L-1, s>=1, and let
g=[[alpha,beta],[gamma,delta]], with alpha and delta odd, gamma even, and
Delta=alpha*delta-beta*gamma odd. Let R be F314's node interpolation matrix.
For 0<=i,j<L set

    B(i,j)=alpha*i+beta-(gamma*i+delta)*j,
    p_i=(-1)^(d-i)*i!*(d-i)!.

Lagrange interpolation and the adjugate formula give the cancellation-free
identity over the rationals

    z_ij=R_ij*(R^-1)_ji
        =(-Delta)^(-d)
          * product_(r!=j) B(i,r) * product_(r!=i) B(r,j)/(p_i*p_j). (1)

Thus, when B(i,j)!=0, (1) is the proposed product-of-row-and-column
formula divided by B(i,j)^2. All slopes in either direction are odd and
nonzero. If B(i,j)=0, then T(i)=j exactly. R_ij=(gamma*i+delta)^d, and the
inverse entry is its reciprocal, because

    (gamma*i+delta)*(alpha-gamma*j)=Delta.

Consequently z_ij=1 exactly at every apparent pole. Every other entry of
that row of z is zero. The same holds for its column. If another factor
in either complete product vanishes while B(i,j)!=0, the value is zero.
There is no undefined division in these cases.

For d=2^s-1, complementary binary digits give

    v2(p_i)=i-popcount(i)+(d-i)-popcount(d-i)=d-s.

Every nonzero complete odd-slope progression of length L has at least
L/2^k factors divisible by 2^k for each 1<=k<=s. Its product therefore
has valuation at least d. More precisely, if w is the valuation of its
unique factor divisible by L, its valuation is d-s+w. Therefore, for a
nonmatching pair (B(i,j) not divisible by L),

    v2(z_ij)>=2*(s-v2(B(i,j))).                              (2)

Zero entries satisfy the bound with infinite valuation. For the kth
Hadamard moment modulo 2^p, the only possible surviving columns in a row
are in the single congruence class

    j=T(i) mod 2^(s-t),  t=min(s,floor((p-1)/(2k))).          (3)

It has 2^t representatives. This yields a literal bound of |I|*2^t entry
calls, not a uniform small aggregate. At trace precision p=2 it reduces to
the canonical graph itself. Those individual graph entries were already
easy to compute.

## Complete progression products without long factorials

There is a useful positive implementation fact: z_ij modulo 2^p can be
evaluated in polynomial bit cost in s, p, and the coefficient bit length
tau. No O(L)-bit factorial precision guard is needed.

For c odd and step even,

    product_(0<=t<m)(c+step*t)
      = c^m * sum_(0<=k<p) e_k(0,...,m-1)*(step/c)^k mod 2^p, (4)

with e_k=0 for k>m. Every omitted term has valuation at least p.
Power sums S_j=sum_(t<m)t^j follow from telescoping powers:

    S_0=m,
    S_j=(m^(j+1)-sum_(a<j) binom(j+1,a)*S_a)/(j+1).

Newton identities then compute

    e_0=1,
    e_k=(sum_(j=1..k)(-1)^(j-1)*e_(k-j)*S_j)/k.

These divisions are exact integer divisions before modular reduction.
Both the power sums and elementary symmetric coefficients have
O(p*(log(m+1)+1)) bits, up to logarithmic bookkeeping terms. Hence (4)
uses O(p^2) operations on polynomial-size integers, followed by modular
unit inversions and exponentiation.

For product_(k<length)(a+b*k) with b odd, first detect an exact zero by
integer divisibility and interval membership. Split k by parity. The odd
factors use (4). Divide all even factors by two and recurse on their
odd-slope progression. Add their count to the valuation. There are
O(s+tau+1) levels for the progressions in (1), including a possible final
singleton with high valuation. Keep the exact total valuation and the odd
part modulo 2^p separately. Evaluate the four factorials the same way.
Subtract valuations and invert only odd parts. This computes (1) with p
unit bits; no lost valuation must be restored as a precision guard.

For H=s+tau+p+1, straightforward schoolbook arithmetic gives a conservative
O(H^8) bit bound and O(H^3) live space for one entry. This includes power
sums, exact divisions, modular powers/inversions, valuation arithmetic,
and all product levels. The code is intentionally an entry primitive,
not a claim of efficient whole-prefix summation.

## What a residue block actually retains

Write M=2^h, L=M*2^t. For each base residue 0<=i0<M define

    D0=gamma*i0+delta,
    y0=T(i0) mod M in [0,M),
    E0=alpha-gamma*y0,
    q0=(alpha*i0+beta-D0*y0)/M.

The last expression is an exact integer, not an unspecified error term.
Direct substitution gives

    T(i0+M*u)=y0+M*(q0+E0*u)/(D0+gamma*M*u).              (5)

In particular, if h>=t, the high-coordinate permutation is affine:

    v=(D0^-1*q0 + D0^-1*E0*u) mod 2^t.                  (6)

Its odd slope is Delta*D0^-2 modulo 2^t, since
D0*E0=Delta+gamma*M*q0. The slope depends only on i0 modulo 2^t.
Its intercept is the moving quotient D0^-1*q0 modulo 2^t.

For a prefix I=[0,H), the allowed high coordinates in this block are
0<=u<U_H(i0), where

    U_H(i0)=max(0,min(2^t,ceil((H-i0)/M))).

For J=[0,K), the analogous endpoint is U_K(y0). Thus summing each affine
block still requires the histogram of its moving intercept, slope, and
these two endpoints as i0 varies. Computing that histogram is the actual
remaining operation; simply counting its possible state labels does not
compute their multiplicities.

Already t=1, h=s-1, H=K=M gives the exact residual

    count([0,M),[0,M)) = #{0<=i0<M : q0(i0) is even}.     (7)

Both high coordinates must be zero, and D0 is odd. Therefore the strongest
local affine simplification still retains a specific top inverse digit.
This is a carry overlap of the kind already present in the project, not
a new solution to it.

The exact bit-extension state transition makes the issue explicit. For
u in {0,1}, select v=(q0+E0*u) mod 2 and put

    q1=(q0+E0*u-D0*v-gamma*M*u*v)/2,
    D1=D0+gamma*M*u,  E1=E0-gamma*M*v.

Knowing (D0,E0,q0) modulo 2^r supplies the next state only modulo 2^(r-1)
through this formula. A fixed-precision truncation is not automatically a
closed recurrence. A bounded witness uses g=[[-3,7],[2,5]], M=8:
i0=3 gives (D0,E0,q0)=(11,-7,-3); i0=5 gives (15,-3,-1).
Both states reduce to (1,1,1) modulo two. Under u=0 both choose v=1,
but their next q bits are 1 and 0. This excludes only that one-bit state
compression. It proves no general lower bound on scalar summation or on
another possible state representation.

## Evidence and restart

The resource check found load 2.31/2.24/2.23, zero swap activity, and one
suggestd process occupying a CPU. Process inspection used an approved
read-only escalation after the sandbox rejected ps. No large research
process appeared in the inspected top processes. The pilot has a 30-second
alarm and an estimated peak below 256 MiB; it checks progression products,
exact rational kernel entries, singular cases, valuation bounds, local
affine charts, and the state collision. Full case counts, timing, and RSS
are in pilot.json and pilot.log. Two nonenumerating entry pilots use
L=2^40,p=12 and L=2^80,p=20. They certify only the listed evaluations.

The concrete missing operation is a uniform aggregate of the quotient
q0(i0) with both inherited endpoints, or an alternative direct contraction
of the normalized Cauchy products that avoids this histogram. No such
operation was found. The exact per-entry evaluator and local affine charts
are retained unpromoted because they do not change the aggregate interface.
