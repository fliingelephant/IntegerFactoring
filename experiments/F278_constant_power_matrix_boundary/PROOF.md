# Proof of F278

## 1. Balanced inequalities and the boundary screen

Since `p<q`,

\[
 p<\sqrt{pq}<q.
\]

Both primes are integers. Therefore

\[
 p\leq B=\lfloor\sqrt{pq}\rfloor<q.
\]

The balance condition also gives `B<q<2p`. Hence `B=p+s` for one integer
`s` with `0<=s<p`.

The prime `q` cannot divide `B` because `0<B<q`. The only multiple of `p`
in `[p,2p)` is `p`. Thus

\[
 \gcd(B,N)=p\iff B=p\iff s=0.
\]

This proves (3)-(5).

## 2. Cost of explicit powering

Write `B` in binary. Repeated squaring computes `C_N^B` with at most
`floor(log_2 B)` squarings and at most the same number of accumulator
multiplications. Each multiplication of two explicit `d by d` matrices uses
`O(d^3)` additions and multiplications modulo `N`. Each residue uses `O(n)`
bits, and standard integer arithmetic has polynomial cost in `n`.

Therefore the time is

\[
 O(d^3 n)\operatorname{poly}(n)
 =\exp((\log n)^{O(1)}),
\]

and the working matrix storage is `O(d^2 n)` bits, up to a constant number
of matrices. Construction of the explicit input matrix has the assumed
bound. This proves Theorem A.

## 3. Jordan coefficients and direct products

The matrices `alpha I` and `J_h` commute, and `J_h^h=0`. The binomial
theorem gives

\[
 (\alpha I+J_h)^B
 =\sum_{j=0}^{h-1}\binom Bj\alpha^{B-j}J_h^j.
\]

Fix `1<=j<h`. Because `j<p` and `B=p+s<2p`, Lucas's theorem gives

\[
 \binom Bj\equiv \binom10\binom sj=\binom sj\pmod p.
\tag{29}
\]

Thus the binomial coefficient is zero modulo `p` exactly when `j>s`.

At the larger prime, `0<=j<=B<q`. The factorial identity

\[
 \binom Bj=\frac{B(B-1)\cdots(B-j+1)}{j!}
\tag{30}
\]

uses only nonzero residues modulo `q`. It follows that
`binom(B,j)` is nonzero modulo `q`.

The factor `alpha^(B-j)` is a unit modulo both primes. Hence the first
equivalence in (11) follows.

Now consider `D_j`. Its factors form the interval

\[
 [B-j+1,B].
\]

This interval has length `j<p` and lies below `q`. It contains `p` exactly
when

\[
 B-j+1\leq p,
\]

which is equivalent to `j>s`. It contains no multiple of `q`, and it cannot
contain two multiples of `p`. Therefore

\[
 \gcd(D_j,N)=p\iff j>s.
\]

This also follows directly from (30), because `j!` is a unit modulo `N`.
Taking the union over `1<=j<h` proves (12) and the direct-window
equivalence.

After the boundary screen, neither `p` nor `q` divides `B`. Work over an
algebraic closure of either local field and let `J=J_h`. For a nonzero
eigenvalue `alpha`,

\[
 (\alpha I+J)^B-\alpha^BI
 =J\left(B\alpha^{B-1}I+\binom B2\alpha^{B-2}J+\cdots\right).
\tag{31}
\]

The constant term of the parenthesized polynomial is nonzero. That
polynomial in `J` is therefore invertible and commutes with `J`. Its powers
have the same kernels as the corresponding powers of `J`. The nilpotent
Jordan block size is unchanged. For eigenvalue zero, `J_h^B=0` because
`h<=B`. This proves the final local statements of Theorem B.

## 4. Semisimple collisions

Over an algebraic closure of `F_r`, a semisimple matrix is diagonalizable.
Choose a basis in which

\[
 C=\operatorname{diag}(\alpha_1,\ldots,\alpha_d).
\]

Then

\[
 C^B=\operatorname{diag}(\alpha_1^B,\ldots,\alpha_d^B).
\]

For two distinct nonzero eigenvalues,

\[
 \alpha_i^B=\alpha_j^B
 \iff (\alpha_i/\alpha_j)^B=1.
\]

The discriminant of a monic polynomial over a field is zero exactly when
the polynomial has a repeated root in an algebraic closure. If `chi_C` is
separable, all original eigenvalues are distinct. Therefore the
discriminant of `chi_(C^B)` vanishes exactly when at least one distinct
ratio is `B`-torsion. This proves Theorem C.

If `det(C)` or `Disc(chi_C)` is nonzero in one CRT component and zero in the
other, its gcd with `N` already factors `N`. Requiring both to be units is
therefore the clean branch, not a loss of a hidden powered signal.

## 5. Quadratic companions

The characteristic polynomial of (16) is

\[
 X^2-tX+\delta.
\]

Cayley-Hamilton gives `C^2=tC-delta I`. Induction using (18) now gives

\[
 C^k=U_kC-\delta U_{k-1}I
\]

for every `k>=1`. The lower-left entry of `C` is one and that of `I` is
zero, so `(C^B)_(2,1)=U_B`.

Fix a hidden prime `r`. Assumption (17) makes the roots `alpha,beta`
distinct and nonzero in the quadratic etale algebra. The standard root
formula, proved by checking its first two values and recurrence, is

\[
 U_k=\frac{\alpha^k-\beta^k}{\alpha-\beta}.
\tag{32}
\]

The denominator is a unit because its square is `Delta`. Thus

\[
 U_B=0
 \iff \alpha^B=\beta^B
 \iff (\alpha/\beta)^B=1.
\]

If the polynomial splits, both roots lie in `F_r^*`, so their ratio has
order dividing `r-1`.

If it is irreducible, Frobenius interchanges the two roots:

\[
 \alpha^r=\beta,\qquad \beta^r=\alpha.
\]

Therefore

\[
 z_r^r=(\alpha/\beta)^r=\beta/\alpha=z_r^{-1},
\]

so `z_r^(r+1)=1`. This is the norm-one torus.

At `r=p`, use `B=p+s`. In the split case, `z_p^p=z_p`, so

\[
 z_p^B=z_p^{s+1}.
\]

In the irreducible case, `z_p^p=z_p^(-1)`, so

\[
 z_p^B=z_p^{s-1}.
\]

Finally, a residue has gcd `p` with the squarefree integer `N=pq` exactly
when it is zero modulo `p` and nonzero modulo `q`. This proves (22)-(24) and
Theorem D.

## 6. `N`-dependent recurrences

Cayley-Hamilton says

\[
 C_N^d+c_{d-1}(N)C_N^{d-1}+\cdots+c_0(N)I=0.
\]

Multiplication by `C_N^k` proves (26). Taking any fixed matrix entry gives
the same scalar recurrence.

Conversely, let

\[
 u_{k+d}+c_{d-1}(N)u_{k+d-1}+\cdots+c_0(N)u_k=0.
\]

The state `(u_(k+d-1),...,u_k)^T` advances by the usual companion matrix.
Thus its remote term is a coordinate of an ordinary constant matrix power.
The coefficients may change when `N` changes, but the transition is fixed
while `k` changes. This proves Theorem E. No lower-bound conclusion was used.

## 7. Frobenius and additive-cancellation boundary

If `C` is diagonalizable in characteristic `r`, the eigenvalues of `C^r`
are the Frobenius images `alpha_i^r`. This is an identity about one ordinary
power. It does not provide the characteristic-dependent linear operator
that maps every element of a CRT-glued extension algebra to its local
`r`-th power. Constructing one public operator with the two hidden local
actions is a separate interface.

At the smaller prime, associativity gives only

\[
 C^B=C^{p+s}=C^pC^s.
\]

The residual `C^s` is not removed. In the named semisimple mechanisms it
becomes the ratio conditions already proved. Nothing in these identities
forces a sum of three or more powered eigenmodes to vanish. This proves the
stated scope boundary and no more.
