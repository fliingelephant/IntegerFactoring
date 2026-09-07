# Full-modulus polarization of the ordinary remainder

Status: root-derived refinement, reconstructed here and checked against full
residues. It is not promoted by this packet. The scope is the general R_d in
REPORT.md, including raw positive odd A,B and signed d. The inverse-floor
term K_d and the input-cut pullback C remain outside this evaluator.

## Exact guarded identity

Put

    V(A,d) = sum_(odd w<M) w^-2 floor((Aw-d)/M)^2 mod 2M.

This is precisely F305's ordinary reciprocal-square marginal. Its existing
Euclidean slope reduction accepts raw positive A, including AB, and its
intercept reduction accepts signed d.

Let u=w^-1 mod M and v=Bw mod M. The two relevant equalities hold at the
stronger precision 2M:

    u^2 = w^-2 mod 2M,
    u(w)^2 = B^2 u(v)^2 mod 2M.

Proof: two odd lifts agreeing modulo M have squares agreeing modulo 2M.
The difference of their squares is Mt(2x+Mt), divisible by 2M. This removes
the otherwise dangerous canonical-inverse ambiguity at the guard bit.

Now square the exact floor identity

    f_(AB,d)(w) = A f_B(w)+f_(A,d)(v).

Multiply by u(w)^2, sum, and change variables to v in the final square term.
The resulting identity is

    2A R_d(A,B) = V(AB,d)-A^2 V(B,0)-B^2 V(A,d) mod 2M.       (1)

The right side is even. Take its even canonical residue modulo 2M, divide
by 2 in the integers, and multiply by A^-1 modulo M. This computes R_d
modulo M from exactly three known marginal values. No division by an even
residue in Z/MZ is performed. In particular, signed d causes no problem,
although individual V(A,d) can be odd.

For bit lengths O(k) of A,B,d and M=2^k, each marginal has degree O(k),
O(k^3) Euclidean bank states, O(k^5) rational arithmetic operations, and
O(k^2)-bit operands by F305's explicit bounds. The three calls therefore
have polynomial bit complexity. For longer raw inputs, include their bit
lengths in the slope and operand bounds. There is no unit enumeration.

## Removing the ordinary term from the cocycle

For d=0, V(A,0) is even. Pair w with M-w: the inverse-square weights are
equal modulo 2M, and the two floor values have equal parity for odd A.
Define

    W(A) = A^-1 [V(A,0)/2] mod M,
    S(A) = T(A,0)-W(A) mod M.

All halves use the guarded V residue modulo 2M. Equation (1) gives

    B^-1 R_0(A,B) = W(AB)-A W(B)-B W(A) mod M.

Substitution in REPORT.md (2) therefore proves

    S(AB) = B S(A)+A S(B)-K(A,B) mod M.                         (2)

This is an exact simplification: the ordinary marginal is fully evaluated,
and the only remaining unshifted term is the symmetric inverse-floor sum K.
It does not evaluate that sum.

## Descent and surviving precision

Normalizing D(A)=A^-1 S(A), equation (2) becomes

    D(AB)=D(A)+D(B)-K(A,B)/(AB) mod M.

Thus iteration along powers of A gives a sum of normalized K values and a
multiple r D(A). The equation does not make those K values known. Summing
over the order of A in the dyadic unit group also introduces division by a
power of two. That loses the same number of precision bits; it is not an
invertible averaging operation modulo M. Raw-argument normalization must
also be kept before using a finite group relation.

The square-input modulo-4 operation in REPORT.md survives this refinement:
sign/inversion orbits evaluate the specific diagonal K modulo 4. At higher
precision, nonfixed paired-orbit contributions survive. For mixed cuts,
REPORT.md (3) additionally retains C_(c,d), even after R_d is evaluated.
No decreasing-modulus or polynomial-size closure for these families is
proved. This is a precise remaining task, not an impossibility statement.

An exact cross-check identifies a tempting tautology. If H(A)=S11(M,A mod M),
expansion of both floors gives

    M^2 K(A,B) = AB H(1)-A H(B)-B H(A)+H(AB).

This identity is compatible with (2), but requires the higher-precision H
values under investigation. It is not an independent constructor for K,
just as the first-floor J identity does not construct T.

## Implementation and resource evidence

`refinement.py` loads only the existing marginal_bank function definition
from F305/input_transport.py. It does not execute that packet's driver or
replace its algorithm. The named logs and JSON preserve all successful runs.

The small pilot checked 84 full residues of R_d for M=8 through 512, including
signed d, raw AB, and reproducible random A,B with seed 3082. Its 28 unshifted
cases also checked the S cocycle. It took 0.23 seconds at 20.6 MB peak RSS.

The nonenumerative k=64 run used A=6148914691236517205,
B=3689348814741910323, d=2635249153387078802. The three marginal calls used
at most 11,596 states each, degree 34, and 2,290-bit exact integers. They
returned R modulo M equal to 16063220329595935574 in 1.55 seconds at
27.1 MB peak RSS.

The balanced-slope k=128 run hit the retained 30-second alarm (exit 142)
before producing a result. Its empty named log is preserved as
refinement_k128.log; no k128 result is claimed. The alarm retained the small
resource budget. This implementation timing limits the demonstrated size;
it does not replace the stated polynomial bit bound with a timing claim.

The refinement preflight at approximately 09:40 on 2026-09-07 showed load
averages 1.96, 2.10, 2.08, a 16 GiB host, and no large research worker in the
busy-process snapshot. The successful k64 measurement justified attempting
one k128 run under the same alarm. No shared records or source files changed.
