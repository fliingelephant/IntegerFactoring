# F176 candidate — the F174 hard escape reduces to base two or a prime-exponent Mersenne branch

## Status and scope

This is a proof-only refinement of F174. It preserves the complete F174
procedure and specializes its Harvey--Hittmeir target to the input length.
It then adds one polynomial-size collision screen.

For every odd composite input, the refined output is

\[
\boxed{
\begin{array}{c}
\text{factor}\quad\lor\quad
\text{factored exact common-order state above }n\\[2mm]
\lor\quad\text{hard base }2\\[1mm]
\lor\quad
\bigl(N=2^n-1,\ n\text{ prime, and hard base }3\bigr).
\end{array}}
\tag{1}
\]

Here

\[
n=\lceil\log_2(N+1)\rceil.
\tag{2}
\]

The two hard branches remain genuine missing progress. F176 is not a
factoring algorithm.

## 1. Procedure

Inputs below one fixed absolute threshold are factored by direct trial
division. On every other odd composite input, run the F174 instrumented
Harvey--Hittmeir procedure with

\[
D=n
\tag{3}
\]

and any fixed quasipolynomial relative cap

\[
C=2^{(\log n)^{O(1)}}.
\tag{4}

Keep every F174 factor and exact-state exit unchanged. Suppose its line-13
integer is the prime \(\beta\), its current exact common state is \((g,M)\),
and

\[
M\le n,
\qquad
a^M=1\pmod N\quad(1\le a<\beta).
\tag{5}

If \(\beta\ge5\), put

\[
t=\lceil\sqrt n\rceil,
\qquad
\mathcal S=\{2^u3^v:0\le u,v\le t\}.
\tag{6}

For every distinct pair \(x,y\in\mathcal S\), compute

\[
\gcd(|x-y|,N).
\tag{7}

This is the added collision screen. If it returns a factor, stop. If not,
continue with the unchanged F174 absolute- and relative-order screens.

## 2. The collision screen forces \(\beta\in\{2,3\}\)

For all inputs above the fixed threshold,

\[
|\mathcal S|=(t+1)^2>n\ge M
\tag{8}

and every member of \(\mathcal S\) is a distinct positive integer below
\(N\). If \(\beta\ge5\), both \(2\) and \(3\) occur before the escape, so

\[
x^M=1\pmod N
\qquad(x\in\mathcal S).
\tag{9}

Fix any rational prime \(p\mid N\). The polynomial \(X^M-1\) has at most
\(M\) roots in \(\mathbf F_p\). Thus two members \(x\ne y\) of
\(\mathcal S\) are congruent modulo \(p\). Because

\[
0<|x-y|<N,
\tag{10}

the corresponding gcd in (7) is a proper factor of \(N\). Consequently a
no-factor line-13 escape satisfies

\[
\boxed{\beta\in\{2,3\}.}
\tag{11}

This conclusion holds for squarefree inputs, repeated prime factors, and
prime powers.

## 3. Exact normal form of the base-two branch

If \(\beta=2\), the Harvey--Hittmeir state before the first loop integer is

\[
(g,M)=(1,1).
\tag{12}

After the unchanged F174 screens, the surviving hard output therefore
obeys, for every hidden prime-power component \(R_j\),

\[
\boxed{
\sigma(\operatorname{ord}_{R_j}(2))>n,
\qquad
\operatorname{ord}_{R_j}(2)>C.
}
\tag{13}

This is the generic hard branch.

## 4. Exact normal form of the base-three branch

Suppose \(\beta=3\) and no earlier factor or exact state was returned. The
only earlier nontrivial loop integer was \(2\). The Harvey--Hittmeir exact
order search and prime-divisor screens therefore certify

\[
\operatorname{ord}_{R_j}(2)=M
\qquad\text{for every }R_j,
\tag{14}

with \(M\le n\). Hence

\[
N\mid 2^M-1.
\tag{15}

The definition of \(n\) gives \(N>2^{n-1}\). Equation (15) first forces
\(M=n\), and then forces

\[
\boxed{N=2^n-1.}
\tag{16}

If \(n\) is composite, let \(\ell\mid n\) be a prime and put

\[
d=2^{n/\ell}-1.
\tag{17}

Then \(1<d<N\) and \(d\mid N\), so \(d\) is a proper factor. Thus a
surviving base-three branch has

\[
\boxed{N=2^n-1\text{ composite and }n\text{ prime}.}
\tag{18}

Its unchanged F174 hard certificate is

\[
\operatorname{ord}_{R_j}(2)=n,
\tag{19}

\[
\boxed{
\sigma(\operatorname{ord}_{R_j}(3))>n,
\qquad
\operatorname{ord}_{(\mathbb Z/R_j\mathbb Z)^\times/\langle2\rangle}
(3\langle2\rangle)>C
}
\tag{20}

for every hidden prime-power component.

## 5. Complete output theorem

The refined procedure returns exactly one of the following.

1. A verified proper divisor of \(N\).
2. A public pair \((h,L)\), with the complete factorization of \(L\), such
   that \(h\) has exact order \(L>n\) in every hidden prime-power component.
3. The hard base-two certificate (13).
4. The prime-exponent composite-Mersenne hard base-three certificate
   (18)--(20).

Every factor exit supports complete-factor recursion: recursively factor
the returned divisor and its complementary cofactor. Perfect powers and
the fixed finite input range are handled by standard integer root and trial
division routines. The recursion has depth at most \(n\), so a uniform QP
per-node bound remains QP overall.

## 6. Complexity

The F174 call with \(D=n\) has deterministic QP bit cost. The added set has
\(O(n)\) members and \(O(n^2)\) pairs. Every member has \(O(\sqrt n)\)
bits. Thus the collision screen has polynomial bit cost.

Factoring the exponent \(n\) by trial division and constructing (17) also
has polynomial bit cost. The full refinement therefore has uniform
deterministic QP bit cost.

## 7. Exact exclusions

F176 does not prove any of the following.

- The hard base-two branch is impossible.
- Unequal hidden orders of \(2\) can be localized in QP time.
- Every composite Mersenne number with prime exponent can be factored in QP
  time.
- Large absolute primary order or large quotient order gives an exact
  common order.
- Ordinary hard order transfers to a nonsplit quadratic torus.
- Integer factoring is in deterministic or Las Vegas QP time.

The remaining order-only problem is now explicit: factor the generic hard
base-two branch, or factor the exceptional prime-exponent Mersenne branch
with its hard base-three certificate.
