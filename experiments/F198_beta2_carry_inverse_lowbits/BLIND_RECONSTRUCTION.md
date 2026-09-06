# Blind reconstruction of F198

Statement SHA-256, recorded before reading the statement:

`244e44b2d93fe6f62ef2ceb161b67132a12d3741a54a6ff80a2930e438dce0bb`

## Verdict

**PASS.** I found no internal mathematical error, subject to the required convention that the three explicitly named literature results are granted with the exact interfaces quoted in the statement. In particular, the Coppersmith interface must include the stated floor-level low-bit threshold, not only an informal asymptotic phrase such as “one quarter of the bits.” The uniform promise-function reduction also inherits the statement's earlier requirement that the precision schedule is public and polynomial-time computable; if a precision (t) is supplied with the residue, the terminal itself does not need to evaluate (L).

## 1. The balanced binomial congruence

The inequalities (p<q) give

\[
p<\sqrt{pq}<q.
\]

Consequently,

\[
p\le B<q<2p.
\]

Write

\[
B=p+b,
\qquad 0\le b<p,
\]

and, using that distinct odd primes differ by at least two, write

\[
q=p+c+1,
\qquad 1\le c\le p-2.
\]

Modulo (q), every integer (1,\ldots,B) is invertible because (B<q). Thus

\[
\binom{N-1}{B}
=\prod_{i=1}^{B}\frac{N-i}{i}
\equiv(-1)^B\pmod q.
\]

It follows that (A\equiv1\equiv1-q\pmod q).

For completeness, the needed special case of the base-(p) binomial congruence can be derived without taking any nonunit denominator. We have

\[
N-1=pq-1=p^2+cp+(p-1).
\]

Over \(\mathbf F_p[x]\), Frobenius gives

\[
(1+x)^{N-1}
=(1+x)^{p^2}(1+x)^{cp}(1+x)^{p-1}
\equiv(1+x^{p^2})(1+x^p)^c(1+x)^{p-1}.
\]

Because (p+b<p^2), the coefficient of (x^{p+b}) on the right can only be obtained by selecting (x^p) once from ((1+x^p)^c) and (x^b) from the last factor. Therefore

\[
C\equiv c\binom{p-1}{b}\equiv c(-1)^b\pmod p.
\]

Since (p) is odd, (B=p+b) has sign

\[
(-1)^B=-(-1)^b.
\]

Hence

\[
A\equiv-c\equiv1-q\pmod p.
\]

The same congruence holds modulo both coprime primes (p) and (q), so the Chinese remainder theorem gives

\[
A\equiv1-q\pmod{pq}=\pmod N.
\]

Thus (h=(A-(1-q))/N) is an integer. This proof also covers the edge case (B=p), where (b=0).

## 2. Public computation of (z_t)

The stated corrected Andreica interface computes

\[
\binom{N-1}{B}\bmod 2^n
\]

in time polynomial in the bit length and the requested precision. Its main-range condition is met at precision (n): from the definition of (n),

\[
N+1\le2^n,
\qquad N-1<2^n,
\]

and (0\le B\le N-1). This is why computing first at precision (n), rather than invoking a range-restricted theorem directly at a smaller (t), is sufficient.

The algorithm computes (B) by integer square root, applies the known sign ((-1)^B), reduces modulo (2^t), subtracts (1), and multiplies by (N^{-1}\bmod2^t). The inverse exists because (N) is odd. Integer square root, reduction, and extended-Euclidean inversion all use polynomial bit complexity on (O(n))-bit operands. Therefore (z_t) is public and polynomial-time computable. At no point does this calculation divide (A-1) by (N) as an integer.

## 3. The hidden-inverse identity

The definition of (h) is the exact integer equality

\[
A=1-q+Nh.
\]

It follows that

\[
A-1=Nh-q.
\]

Reducing modulo (2^t) and multiplying by the inverse of (N=pq) gives

\[
z_t\equiv h-N^{-1}q
\equiv h-p^{-1}\pmod{2^t}.
\]

The last step is valid because (p,q), and (N) are all units modulo (2^t). Rearranging proves

\[
h-z_t\equiv p^{-1}\pmod{2^t}.
\]

This also shows that no unknown factor is used to compute (z_t); (q) occurs only in the correctness proof.

## 4. Reductions in both directions

Suppose an oracle returns the canonical residue (H=h\bmod2^t). Publicly compute (z_t), form

\[
u=(H-z_t)\bmod2^t,
\]

and invert (u). The identity above says (u=p^{-1}\bmod2^t), so (u) is odd and

\[
u^{-1}=p\bmod2^t.
\]

Conversely, if the canonical residue (P=p\bmod2^t) is supplied, it is odd and hence invertible, and

\[
H=(z_t+P^{-1})\bmod2^t.
\]

Each direction makes one query and otherwise performs polynomially many bit operations. This is uniform when (t=t(N)) is a public polynomial-time computable function, as required in the statement.

## 5. Exact recovery at half precision

From (n=\lceil\log_2(N+1)\rceil) we have (N<2^n). Since (p<q),

\[
p<\sqrt N<2^{n/2}\le2^{\lceil n/2\rceil}.
\]

At (t_0=\lceil n/2\rceil), the canonical residue (p\bmod2^{t_0}) is therefore the integer (p), with no lift ambiguity. The preceding reduction recovers it from one carry residue. Exact division verifies (p\mid N) and returns (q=N/p). All numbers involved have (O(n)) bits, so this is polynomial time.

In the reverse direction, an exact factorization gives (p), and the public formula

\[
h\equiv z_{t_0}+p^{-1}\pmod{2^{t_0}}
\]

computes the requested carry residue in polynomial time. Thus the claimed half-precision equivalence is exact on the stated promise.

## 6. Bit-length and floor conventions

Let \(\lambda=\lfloor\log_2N\rfloor\). The odd integer (N>1) is not a power of two, so

\[
2^\lambda<N<2^{\lambda+1}.
\]

Since (N) is integral, (N+1\le2^{\lambda+1}), while (N+1>2^\lambda). Hence

\[
n=\lambda+1.
\]

Write \(\log_2N=\lambda+\delta\) with (0<\delta<1), and write \(\lambda=4a+r\), where (0\le r\le3). Then

\[
\left\lfloor\frac{\log_2N}{4}\right\rfloor
=a
=\left\lfloor\frac{\lambda}{4}\right\rfloor
=\left\lfloor\frac{n-1}{4}\right\rfloor,
\]

because (0<r+\delta<4). Thus the two definitions of (k) agree exactly, including when (\lambda\equiv3\pmod4).

## 7. Gao--Feng--Hu--Pan terminal

Let (t=k-L\ge1), (m=2^t), and let (s=p\bmod m) be the canonical residue recovered from the carry. The exposed hypotheses of the cited theorem hold:

- (m) is a unit modulo odd (N);
- (s) is odd, so (1\le s<m);
- (m\le2^k\le N^{1/4}<N);
- (p) is a prime divisor of (N), has the stated residue (p\equiv s\pmod m), and occurs to the first power because (p\ne q).

Thus the granted (r=1) interface finds (p) in

\[
O\!\left(\left\lceil\frac{N^{1/4}}{2^t}\right\rceil
\log^{7+3\epsilon}N\right)
\]

bit operations for fixed (\epsilon>0). Put

\[
\rho=\frac{\log_2N}{4}-k,
\qquad0\le\rho<1.
\]

Then

\[
\frac{N^{1/4}}{2^t}=2^{\rho+L}<2^{L+1}.
\]

Since (L) is integer-valued, the ceiling is at most (2^{L+1}). This proves the displayed numerical-QP cost and does not enumerate the missing lifts.

## 8. Coppersmith extension terminal

Because (k=t+L), the integers

\[
p_{0,j}=p_t+j2^t,
\qquad0\le j<2^L,
\]

are precisely the representatives in ([0,2^k)) congruent to (p_t\) modulo (2^t). If (r_k=p\bmod2^k), then

\[
j_*=(r_k-p_t)/2^t
\]

is an integer in ([0,2^L)), so the enumeration contains the unique correct extension.

Every (p_{0,j}) is odd, hence invertible modulo (2^k). For the correct extension,

\[
q_{0,j_*}
=Np_{0,j_*}^{-1}
\equiv Np^{-1}
\equiv q\pmod{2^k}.
\]

Therefore the correct iteration supplies the exact low-order data required by the granted Coppersmith 1997 Theorem 5 interface. The balance promise (p<q<2p) supplies its factor-size hypothesis. That iteration returns the factorization in deterministic polynomial time. Iterations with an incorrect extension need not satisfy the mathematical promise, but the bounded deterministic procedure can still be run; every alleged output is checked by exact division, and only the correct extension needs a success guarantee.

There are exactly (2^L) iterations. Modular inversion, construction of each residue, the cited algorithm, and exact verification each use polynomial bit complexity on (O(n))-bit integers. Hence the total cost is

\[
2^L\operatorname{poly}(n).
\]

This route is independent of the Gao--Feng--Hu--Pan terminal once the stated Coppersmith interface is granted.

## 9. Uniform numerical-QP accounting and small inputs

The meaning (L(n)=(\log n)^{O(1)}) gives fixed constants (D,a) and a fixed threshold such that

\[
L(n)\le D(\log_2(n+1))^a
\]

beyond that threshold. For any fixed polynomial exponent (c),

\[
2^{L(n)+1}n^c
\le
2^{D(\log_2(n+1))^a+O(\log_2(n+1))}
\le
2^{C(\log_2(n+1))^K}
\]

for fixed (C) and (K=\max\{a,1\}). The same estimate covers the extension terminal. Public computation of (z_t), modular inversion, output verification, and exact division are polynomial and are absorbed in the same bound. A numerical-QP carry evaluator is invoked only once, so adding its fixed numerical-QP bound preserves numerical-QP time. There is no random step.

Since every fixed polylogarithm is (o(n)), while (k=\lfloor(n-1)/4\rfloor), the inequality (k-L(n)\ge1) fails for only finitely many input lengths. A single uniform algorithm can use ordinary deterministic trial division on those lengths. Its maximum cost over this finite set is a constant relative to the asymptotic variable and can be absorbed by increasing (C). This does not use a table of factorizations. To implement the branch as a reduction that chooses its own query precision, the fixed schedule (L(n)), equivalently (t(N)), must be publicly computable. If (t) accompanies the supplied carry residue, the algorithm instead recovers (L=k-t) directly.

## 10. Refutation checks and exact scope

I specifically checked the following possible failure points:

- The denominator product modulo (p) is not inverted; the coefficient argument handles (B\ge p).
- The case (B=p) is included.
- (A-1) is never claimed divisible by (N).
- All inverses modulo (2^t) exist for parity reasons.
- The residue (s) cannot be zero because (p) is odd and (t\ge1).
- Computing the binomial at precision (n) satisfies the quoted upper-index range even when (t\ll n).
- The equalities involving (n), \(\lfloor\log_2N\rfloor\), and (k) survive all floor cases.
- The correct Coppersmith lift is present exactly once, and invalid lifts cannot cause an incorrect accepted result because exact division is required.
- Polynomial factors in (n), all (O(n))-bit arithmetic, the (2^L) loop, and the finite exceptional lengths are all absorbed by one fixed numerical-QP bound.

The result remains strictly promise-scoped. It applies only to (N=pq) with distinct odd primes satisfying (p<q<2p). It does not handle arbitrary composites, prime powers, even inputs, or unbalanced factors, and therefore does not by itself resolve general integer factoring. It does not evaluate any bit of (h); it proves what follows if the specified carry residue is available. It supplies no selector for the correct bit-by-bit lift. Finally, this reconstruction verifies the reductions conditional on the exact Andreica, Gao--Feng--Hu--Pan, and Coppersmith interfaces stated in the candidate; it does not independently verify those literature theorems or their bibliographic attribution.
