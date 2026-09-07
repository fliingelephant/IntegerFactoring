# Half-box count modulo eight: statement for blind reconstruction

Use only this statement and its declared dependencies. Do not read the
candidate report, implementation, or earlier carry-transport proofs.

Let k >= 3, R = 2^k, phi = R/2, and let N be any positive odd integer.
Write N = nu + R ell, where 1 <= nu < R is odd and ell >= 0. Define

    C(N,2R) = #{odd u in [1,R): (N/u modulo 2R) lies in [1,R)}.

In the smaller modulus R, put v_u = nu/u modulo R in [1,R) and
q_N(u) = (u*v_u - N)/R. Define exact integer sums

    H_N = sum_u q_N(u),
    B_N = sum_u binom(q_N(u),2),
    A_N = sum_u binom(q_N(u),3).

Binomial polynomials are evaluated on all integers, including negative ones.
Let P_R be the product of the positive odd integers below R.

Declared algorithmic dependencies:

1. P238 computes P_R modulo a requested power of two in polynomial bit
   complexity in k and that precision. Its internal proof need not be read.
2. P242 computes T_R(nu) modulo four in polynomial bit complexity, where
   w is canonical odd, u_w = w^(-1) modulo R, and

       q_1(w) = (w*u_w - 1)/R,
       T_R(nu) = sum_w u_w*q_1(w)*floor(nu*w/R).

   This black box covers every canonical odd nu. It does not compute a cut.
3. Ordinary degree-two floor sums may be computed by an explicitly justified
   Euclidean recurrence in polynomial bit complexity; state the required
   moments and precision, or derive the recurrence.

Claims to reconstruct:

(a) H_1 = 2 modulo four and B_1 = 2 modulo four for every k >= 3.
    A_N = 1 modulo two if N = 1 modulo eight, and A_N = 0 modulo two
    otherwise.

(b) For f(w) = floor(nu*w/R), let

       J_nu = sum_w (f(w)^2 + w*f(w)) modulo eight.

    This residue is even. With a guarded division J_nu/2 modulo four,

       b_nu = 2 + nu*(nu-1) + J_nu/2 - nu*T_R(nu) modulo four

    equals B_nu modulo four. Moreover,

       B_N = b_nu - ell*H_N modulo four.

(c) Compute the residue H_N modulo eight by

       H_N = ((P_R^2 - N^phi modulo 8R)/R) * N^(1-phi) modulo eight.

    The numerator uses its canonical residue modulo 8R and is divisible by
    R before division. The exponent with negative sign uses an odd inverse.
    Then

       C(N,2R) = phi - H_N + 2*(b_nu - ell*H_N)
                 - 4*1_(N = 1 modulo eight)             modulo eight.

(d) Together these are a uniform deterministic polynomial-bit algorithm
    for the stated half-box count modulo eight. The algorithm does not
    enumerate R/2 graph points. Explain all guards, input sizes, and calls.

No arbitrary interval count, exact count, emptiness oracle, or factoring
algorithm is claimed.
