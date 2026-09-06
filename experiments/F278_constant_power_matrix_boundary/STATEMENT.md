# F278 statement — explicit constant-power matrix boundary

## Status and scope

F278 is a proof-only candidate. It studies one public matrix

\[
 C_N\in M_{d(N)}(\mathbb Z/N\mathbb Z)
\]

and the ordinary power

\[
 C_N^B,\qquad B=\lfloor\sqrt N\rfloor.
\tag{1}
\]

The entries and the dimension may depend on `N`. The matrix is **explicit**:
all `d(N)^2` entries can be constructed in numerical quasipolynomial time,
and `d(N)` is numerical quasipolynomial in the bit length of `N`. Fixed
dimension is included.

The packet proves five narrow facts.

1. Evaluation of the full explicit power is automatic in numerical
   quasipolynomial time.
2. A quasipolynomial-width Jordan block gives exactly a direct near-square
   scan. It gives no wider threshold window.
3. A clean semisimple collision under powering is exactly a multiplicative
   ratio-torsion event.
4. A clean quadratic companion coordinate is exactly an ordinary unit-group
   or norm-one-torus order residual.
5. Ordinary matrix powering does not supply a genuine hidden local
   Frobenius operator. Higher-dimensional additive cancellations remain
   outside the proved boundary.

F278 proves no universal lower bound for recurrences, matrices, arithmetic
circuits, or factoring algorithms. It does not classify arbitrary additive
cancellation among three or more exponential modes.

## 1. Balanced semiprime notation

For the signal statements, let

\[
 N=pq,qquad p<q<2p
\tag{2}
\]

with distinct odd primes. Then

\[
 p\leq B<q<2p.
\tag{3}
\]

Write

\[
 B=p+s,qquad 0\leq s<p.
\tag{4}
\]

The boundary gcd

\[
 g_B=\gcd(B,N)
\tag{5}
\]

equals `p` exactly when `s=0`; otherwise it equals one. After this direct
screen, `1<=s<p` and neither hidden prime divides `B`.

Whenever a local Jordan statement below uses a block of size `h`, it assumes

\[
 1\leq h\leq d\leq B,qquad d<p.
\tag{6}
\]

For numerical-quasipolynomial `d(N)`, the inequality `d<p` holds for all
sufficiently large balanced semiprimes. The theorem states it explicitly and
makes no claim for an exceptional input that violates it.

## Theorem A — the explicit endpoint is automatic

Let `n=ceil(log_2 N)`. Suppose

\[
 d(N)\leq \exp((\log n)^{O(1)})
\tag{7}
\]

and construction of all entries of `C_N` has the same time bound. Then the
full matrix `C_N^B mod N` is computable in numerical quasipolynomial time and
space.

Binary powering uses `O(log B)=O(n)` matrix multiplications. Naive matrix
multiplication uses `O(d^3)` ring operations and stores `O(d^2)` residues.
Thus fixed dimension and explicit quasipolynomial dimension both pass the
`STATE` and `ENDPOINT` gates automatically.

The theorem supplies evaluation only. It does not supply a factor-bearing
observable.

## Theorem B — a Jordan window is a direct near-square window

Let `J_h` be the nilpotent Jordan shift of size `h`. Let `alpha` be a public
residue with

\[
 \gcd(\alpha,N)=1,
\]

and put

\[
 C=\alpha I+J_h.
\tag{8}
\]

Then

\[
 C^B=\sum_{j=0}^{h-1}\binom Bj\alpha^{B-j}J_h^j.
\tag{9}
\]

For every `1<=j<h`, define the direct falling product

\[
 D_j=\prod_{t=0}^{j-1}(B-t).
\tag{10}
\]

Under (2), (4), and (6),

\[
 \boxed{
 \gcd\!\left(\binom Bj\alpha^{B-j},N\right)=p
 \iff j>s
 \iff \gcd(D_j,N)=p.
 }
\tag{11}
\]

If `j<=s`, both gcds are one. Consequently, the first `h-1` nontrivial
Jordan diagonals contain a proper factor if and only if

\[
 s<h-1.
\tag{12}
\]

This is exactly the direct test of the consecutive integers

\[
 B, B-1,\ldots,B-h+2.
\tag{13}
\]

An explicit quasipolynomial-width Jordan block therefore detects only a
quasipolynomial near-square gap. It does not compress a longer hidden
threshold window.

After the screen (5), a nonzero local Jordan block also keeps its block size
under `X -> X^B`, unless its eigenvalue collides with another powered
eigenvalue. A zero-eigenvalue block of size at most `B` is killed modulo both
hidden primes. These facts create no separate one-prime signal.

The theorem applies to a literal block, or to a change of basis whose
determinant and all represented denominators are units modulo `N`. It does
not assert that a hidden local Jordan basis can be constructed publicly.

## Theorem C — clean semisimple collision equals ratio torsion

Let `r` be either hidden prime. Suppose `C mod r` is invertible and
semisimple. Let

\[
 \alpha_1,\ldots,\alpha_m
\]

be its distinct eigenvalues in an algebraic closure of `F_r`. Then the
distinct eigenvalues `alpha_i` and `alpha_j` collide in `C^B` exactly when

\[
 \boxed{(\alpha_i/\alpha_j)^B=1.}
\tag{14}
\]

If the characteristic polynomial of `C` is separable modulo `r`, then

\[
 \operatorname{Disc}(\chi_{C^B})=0\pmod r
\tag{15}
\]

exactly when at least one distinct eigenvalue ratio is `B`-torsion.
Therefore a clean discriminant or collision factor from `C^B` is an exact
multiplicative order signal in a finite extension field. It is not a new
kind of characteristic threshold.

If `det(C)` or `Disc(chi_C)` has a proper gcd with `N`, that input invariant
already supplies a factor before powering. The clean theorem assumes these
input invariants are units in both CRT components.

Theorem C covers eigenvalue collisions and the rank losses caused by those
collisions. It does not cover cancellation in an arbitrary coordinate that
adds three or more distinct powered eigenmodes.

## Theorem D — a clean quadratic companion is an ordinary/torus residual

Let

\[
 C=\begin{pmatrix}t&-\delta\\1&0\end{pmatrix},
 \qquad
 \Delta=t^2-4\delta,
\tag{16}
\]

and assume

\[
 \gcd(\delta\Delta,N)=1.
\tag{17}
\]

Define

\[
 U_0=0,\quad U_1=1,\quad
 U_{k+1}=tU_k-\delta U_{k-1}.
\tag{18}
\]

Then

\[
 C^B=U_BC-\delta U_{B-1}I,
 \qquad (C^B)_{2,1}=U_B.
\tag{19}
\]

Fix `r` in `{p,q}`. Let `alpha,beta` be the two distinct roots of
`X^2-tX+delta` in the quadratic etale algebra over `F_r`, and set

\[
 z_r=\alpha/\beta.
\tag{20}
\]

Then

\[
 \boxed{U_B=0\pmod r\iff z_r^B=1.}
\tag{21}
\]

There are exactly two clean local cases.

1. If the polynomial splits over `F_r`, then `z_r` lies in
   `F_r^*`, so its order divides `r-1`.
2. If the polynomial is irreducible over `F_r`, then
   `z_r^r=z_r^{-1}`. Thus `z_r` lies in the norm-one torus and its order
   divides `r+1`.

At the smaller prime, `B=p+s`, so (21) becomes

\[
 z_p^{s+1}=1
 \quad\text{in the split case},
\tag{22}
\]

or

\[
 z_p^{s-1}=1
 \quad\text{in the irreducible case}.
\tag{23}
\]

Hence the exact factor condition is

\[
 \gcd(U_B,N)=p
\tag{24}
\]

if and only if the applicable residual law (22) or (23) holds modulo `p`
and `z_q^B!=1`. The analogous statement with `p` and `q` exchanged also
holds.

Thus a clean quadratic companion gives an ordinary multiplicative-group
residual or a norm-one-torus residual. It supplies no all-input guarantee
that the two hidden local residuals differ.

## Theorem E — `N`-dependent coefficients remain ordinary recurrences

For each fixed input `N`, write

\[
 \chi_{C_N}(X)=X^d+c_{d-1}(N)X^{d-1}+\cdots+c_0(N).
\tag{25}
\]

Cayley-Hamilton gives

\[
 C_N^{k+d}+c_{d-1}(N)C_N^{k+d-1}
 +\cdots+c_0(N)C_N^k=0
\tag{26}
\]

for every `k>=0`. Every selected entry of `C_N^k` is therefore a scalar
linear recurrence of order at most `d`. Its coefficients can depend on `N`,
but they are constant in the exponent index `k` for that input.

Conversely, every public homogeneous scalar recurrence of order `d` with
coefficients fixed in `k` is represented by a public `d by d` companion
matrix. Thus ordinary explicit matrix powering and ordinary public
constant-coefficient recurrences are the same endpoint model for this
purpose.

This equivalence is not a recurrence lower bound. Arbitrary
numerical-quasipolynomial coefficient functions of `N` are too broad for
such a conclusion. They may encode unrelated public computations. F278
classifies only the Jordan, collision, and clean quadratic mechanisms above.

## 2. Frobenius and higher-dimensional exclusions

In a splitting field of characteristic `r`, ordinary powering sends each
eigenvalue of `C` to its `r`-th power in `C^r`. This observation does not
construct the genuine local Frobenius operator on a CRT-glued finite
algebra. That operator depends on the hidden local characteristic and its
local algebra. Supplying it as one public operator is a different,
factor-bearing interface.

Moreover,

\[
 C^B=C^{p+s}=C^pC^s
\tag{27}
\]

at the smaller prime. The unknown residual power `C^s` remains. Equations
(14), (22), and (23) give the exact reductions in the semisimple and
quadratic cases. They do not turn (27) into a genuine hidden Frobenius map.

For `d>=3`, a coordinate can have the form

\[
 a_1(N)\alpha_1^B+\cdots+a_m(N)\alpha_m^B,
 \qquad m\geq3.
\tag{28}
\]

Such an additive cancellation need not arise from an eigenvalue collision.
F278 proves no impossibility theorem for (28), especially when the public
coefficients depend on `N`. It also supplies no exact all-input factor law
for this class.

## 3. Narrow search disposition

No C++ or numerical search follows from this packet.

- Jordan coefficients reproduce the direct near-square scan (13).
- Clean semisimple collisions reproduce ratio-order tests (14).
- The clean quadratic companion reproduces ordinary or norm-one-torus
  residuals (22)-(23).

A future search in the constant-power lane requires a specified exact
signal outside those three named mechanisms. In particular, a proposed
higher-dimensional additive cancellation must first state an all-input
local law and a public coefficient construction. F278 does not use finite
samples as a substitute for that law.

## 4. Exact nonclaims

F278 proves no:

1. universal lower bound for matrix-power entries or linear recurrences;
2. classification of arbitrary `d>=3` additive exponential sums;
3. impossibility result for `N`-dependent public coefficients;
4. impossibility result for nonlinear, semilinear, adaptive, digit, or
   implicit-state algorithms;
5. construction of a genuine CRT-glued local Frobenius operator;
6. all-input integer-factoring algorithm; or
7. computational or empirical result.
