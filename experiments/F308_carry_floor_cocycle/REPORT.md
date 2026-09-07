# Global inverse-carry cocycle and square-input precision

**Family:** route:F31

Status: author-derived candidate with exact finite checks. This
packet uses the original global inverse graph, with no chart decomposition.
The root-derived refinement in [FULL_R.md](FULL_R.md) supplies a polynomial-bit
evaluator for the general R_d modulo M using three existing marginal calls.
This packet also supplies an operation for **unshifted T(N,0) modulo 4 when
N is a square unit modulo M**. It does not supply T modulo M, arbitrary
shifted binomial carries, rectangle counts, or factoring. No external novelty
claim is made.

## Proposed mechanism

Push the fixed inverse-carry measure through multiplication by an odd input,
including the canonical representative crossings. Integrate a second linear
floor. The resulting cocycle has an inverse-floor cross term; on its square
diagonal, sign and inversion symmetry evaluate that term modulo 4. A second
moment identity evaluates the remaining ordinary floor term. This is a
limited precision contraction, not a recurrence with an unproved free weight.

The closest inspected records are P238, P239, and F305/FLOOR_MARGINALS.md.
The derivation below is from finite identities. No new literature was fetched.

## Exact measure transport

Let M=2^k, k>=3. All sums run over odd canonical w in [0,M). Define

    u = w^-1 mod M,  q(w) = (uw-1)/M,  mu(w) = u q(w),
    f_(A,d)(w) = floor((Aw-d)/M),  f_A = f_(A,0),
    T(A,d) = sum mu(w) f_(A,d)(w) mod M.

Raw positive odd A is allowed; no reduction of A is implicit. For canonical
odd B, put b=B^-1 mod M, q_B=(Bb-1)/M, and v=Bw mod M. Then

    mu(v) = b mu(w) + b q_B u - floor(bu/M)
            - b^2 u^2 f_B(w)                         (mod M).       (1)

Proof: write v=Bw-Mf_B(w) and y=bu-M floor(bu/M), the inverse of v.
Expanding vy gives

    (vy-1)/M = q_B + Bb q(w) - Bw floor(bu/M)
               - bu f_B(w) + M f_B(w) floor(bu/M).

Multiply by y and reduce modulo M. Use y=bu modulo M, uw=1 modulo M,
and Bb=1 modulo M. This gives (1), including both canonical crossings.

## The integrated cocycle, with all cuts retained

Define

    K_d(A,B) = sum f_(A,d)(w) f_B(w^-1 mod M),
    R_d(A,B) = sum u^2 f_B(w) f_(A,d)(Bw mod M).

Then

    T(AB,d) = B T(A,d) + A T(B,0) - K_d(A,B)
              + b R_d(A,B)                           (mod M).       (2)

This identity holds for every integer d. To prove it, multiply (1) by
f_(A,d)(v) and sum. The identity

    f_(A,d)(Bw mod M) = f_(AB,d)(w) - A f_B(w)

handles the main term. In the two middle terms change variables to v and
write y=v^-1 mod M. Since u=By-Mf_B(y),

    floor(bu/M) = q_B y - b f_B(y).

The q_B terms cancel exactly modulo M. What remains is (2).

For the shifted measure of F305, mu_c(w)=mu(w)+1(u<c) modulo M, define T_c
using this measure. The complete shifted equation is

    T_c(AB,d) = B T_c(A,d) + A T_c(B,0) - K_d(A,B)
                + b R_d(A,B) + C_(c,d)(A,B)           (mod M),        (3)
    C_(c,d)(A,B) = sum [1(Bu mod M<c)-B*1(u<c)] f_(A,d)(w).

Thus the input cut is retained exactly. Its pullback is a modular affine
window, and is not silently replaced by an ordinary interval. Formula (3)
has no established polynomial-size repeated closure for arbitrary cuts.

The reciprocal weight in R is ordinary: u^2=w^-2 even modulo 2M. The
root-derived polarization in FULL_R.md now evaluates the general R modulo M
using three single-floor-square calls. Thus the earlier two-floor marginal
gap is removed. The next section retains the simpler degree-two construction
for the unshifted diagonal residue modulo 4.

## A polynomial-bit evaluator for square inputs modulo 4

First, T(A,0) is even for every odd A. Indeed, under w -> M-w,

    mu(w)+mu(M-w) = u^2+1 mod M,
    f_A(M-w) = A-1-f_A(w).

Both facts make each paired contribution even.

Next, take canonical odd 0<A<M and put K=K_0(A,A). Then

    K = 2 floor(A(M/2-1)/M)                           (mod 4).       (4)

Proof: quotient the units by sign. Write h=(A-1)/2. For the sign class
represented by w, its contribution to K/2 modulo 2 is

    f_A(w) f_A(u) - h[f_A(w)+f_A(u)].

This expression is invariant under inversion. Nonfixed sign classes cancel
in pairs modulo 2. Fixed sign classes satisfy w^2=1 or -1 modulo M. There
are no roots of -1 for k>=3. The roots of 1 give exactly the two sign classes
represented by 1 and M/2-1. The first contributes zero because A<M; the
second contributes f_A(M/2-1) modulo 2. This proves (4) for canonical A.

For the diagonal R, odd u satisfies u^2=1 modulo 4. Hence

    R_0(A,A) = Rordinary = sum f_A(w) f_A(Aw mod M)    (mod 4).

Let U(A)=sum f_A(w)^2 as an ordinary integer. Multiplication by A permutes
the odd units, and f_(A^2)=A f_A+f_A(Aw mod M). Squaring and summing gives
the **exact integer** formula

    Rordinary = [U(A^2)-(A^2+1)U(A)]/(2A).                         (5)

Both U values use degree-two ordinary Euclidean floor sums. This formula
requires no inverse graph or product-of-two-floor constructor.

Finally, let N=A^2 mod M and t=floor(A^2/M). Since

    T(A^2,0) = T(N,0)+t Q0 mod M,
    Q0 = sum q(w),

equations (2), (4), and the evenness of T(A,0) give

    T(N,0) = -2 floor(A(M/2-1)/M)
              + A^-1 Rordinary - t Q0                (mod 4).       (6)

P238 supplies Q0 modulo 4. Specifically, if P is the product of odd
canonical units, the exact product identity P^2=product(1+M q(w)) gives

    Q0 = (P^2-1)/M mod 4,

where P^2 is evaluated modulo 4M before exact division by M. This guard
precision is necessary. The implementation uses P238's uniformly truncated
unit-product expansion, not a scan of the unit group.

For an input N=1 modulo 8, a square root A can itself be constructed in
polynomial bit cost. Start with A=1 modulo 8. At each step from 2^j to
2^(j+1), adding 2^(j-1) toggles the next bit of A^2 and preserves its old
residue. This gives a canonical root without an exponentially branching
search. Formula (6) is independent of which root is used.

### Actual cost and precision

The degree-two Euclidean floor recurrence has O(k) memoized states and
operations on O(k)-bit integers/rationals, with absolute degree bounded by 2.
Raw A^2 has at most 2k bits, so it does not change this order. Formula (5)
may be computed exactly, as in the pilot, or modulo 8 with division by 2
followed by the inverse of odd A modulo 4.

The product evaluation uses O(k^2) exact integer operations on O(k^2)-bit
operands, truncation degree O(k), and O(k) stored coefficients. These bounds
give deterministic polynomial bit complexity for (6). No unit enumeration
occurs in this evaluator. Only the independent small verification scans
enumerate units.

This gives T modulo 4, not modulo M. It covers the unshifted square-input
class, not the four shifted values in P239. In particular, it is not an
Archimedean approximation or a claimed evaluator of all third base-M digits.

## What survives beyond these two bits

Equation (2) is a genuine global cocycle, with R now computed by FULL_R.md.
Its inverse-floor term K is
symmetric when d=0, but symmetry alone does not evaluate its full residue.
At modulus 4 the sign/inversion orbit argument discards all nonfixed
classes. At higher precision their doubled contributions survive. A
repeated orbit argument needs their weights, which are not constructed here.

For arbitrary c,d, (3) also retains the affine pullback C. The number of
literal interval pieces can grow with B. No bound is proved for a different
compressed representation, and no impossibility claim follows. These are
the precise surviving families if this cocycle is used for further descent.

## Retained experiment

`pilot.py`, `pilot.json`, and `pilot.log` preserve the source and output.
The pilot checks 5,416 point transports, 124 full cocycles, 124 shifted
cocycles, and 62 square-input precision identities for M=8 through 512.
It includes c=floor(M/3), d=0 and floor(M/3), and a reproducible random
family with seed 308. Both residues 0 and 2 occur in the square-input output.

The nonenumerative large controls use k=32,64,128. At k=128 the result is
T modulo 4 equal to 2, with 57 total floor states and about 0.017 seconds.
The full pilot took 0.039 seconds with peak RSS 18,415,616 bytes. These runs
support the finite formulas and implementation; the proofs and state counts
above supply the asymptotic claims. No failed mathematical cases were dropped.
