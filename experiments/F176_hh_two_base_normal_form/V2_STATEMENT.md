# F176 V2 candidate — every surviving F174 hard escape is base two

## Status and scope

This is a proof-only strengthening of F174. It isolates the first
Harvey--Hittmeir source integer and no longer needs the later HH loop, the
F174 smooth-prefix cutoff, or the F176 V1 three-smooth collision bank.

For every odd composite input, the exact output is

\[
\boxed{
\text{factor}
\quad\lor\quad
\text{factored exact common-order state above }n
\quad\lor\quad
\text{one normalized hard base-two block}.
}
\tag{1}
\]

Here

\[
n=\lceil\log_2(N+1)\rceil.
\tag{2}
\]

The hard base-two branch remains genuine missing progress. F176 V2 is not
a factoring algorithm.

## 1. Parameters and hidden notation

Let \(N\ge3\) be odd and composite. Inputs below one fixed absolute
threshold are factored by direct trial division. For the proof only, write

\[
N=\prod_{j=1}^s R_j,
\qquad
R_j=p_j^{a_j},
\tag{3}
\]

where the \(p_j\) are distinct odd primes.

Choose

\[
C\ge n,
\qquad
C=2^{(\log n)^{O(1)}}.
\tag{4}
\]

For an integer \(r\ge1\), put

\[
\sigma(r)=\max_{\ell^a\parallel r}\ell^a,
\qquad
\sigma(1)=1.
\tag{5}
\]

The public pair \((-1,2)\) is an exact common-order state in every hidden
odd prime-power component.

## 2. Absolute factor-first screen for base two

Put

\[
\Lambda_n=\operatorname{lcm}(1,2,\ldots,n)
\tag{6}
\]

and compute

\[
A=\gcd(2^{\Lambda_n}-1,N).
\tag{7}
\]

Exactly one of the following occurs.

1. If \(1<A<N\), then \(A\) is a proper factor.
2. If \(A=N\), use the known factorization of \(\Lambda_n\) for
   factor-first divisor stripping. This either factors \(N\), or returns
   the exact order

   \[
   m=\operatorname{ord}_{R_j}(2)
   \qquad(1\le j\le s)
   \tag{8}
   \]

   with its complete factorization.
3. If \(A=1\), then

   \[
   \boxed{
   \sigma(\operatorname{ord}_{R_j}(2))>n
   \qquad(1\le j\le s).
   }
   \tag{9}
   \]

## 3. Every common base-two return gives progress

Suppose (8) is obtained.

If \(m>n\), then \((2,m)\) is already the required exact common-order
state.

Suppose \(m\le n\). Since \(2^m=1\pmod N\),

\[
N\mid2^m-1.
\tag{10}
\]

The definition of \(n\) gives \(N>2^{n-1}\). Hence (10) forces

\[
m=n,
\qquad
N=2^n-1.
\tag{11}
\]

If \(n\) is composite, any prime \(\ell\mid n\) gives the proper factor

\[
2^{n/\ell}-1.
\tag{12}
\]

If \(n\) is prime, the composite-input promise excludes \(n=2\), so \(n\)
is odd. Then the public element \(-2\) has exact order \(2n\) in every
hidden prime-power component. Thus

\[
\boxed{(-2,2n)}
\tag{13}
\]

is a factored exact common-order state above \(n\).

Consequently a common base-two return never leaves a hard branch.

## 4. Relative screen against the normalized sign state

Only the branch \(A=1\) remains. For every hidden component, define

\[
e_j=
\operatorname{ord}_{(\mathbb Z/R_j\mathbb Z)^\times/\langle-1\rangle}
(2\langle-1\rangle).
\tag{14}
\]

For \(e=1,2,\ldots,C\), compute

\[
G_e=\gcd(2^{2e}-1,N).
\tag{15}
\]

Exactly one of the following occurs.

1. A proper \(G_e\) factors \(N\).
2. A first global return \(G_e=N\) gives

   \[
   e_j=e
   \qquad(1\le j\le s).
   \tag{16}
   \]

   Use the known factored multiple \(2e\) for factor-first divisor
   stripping. This either factors \(N\), or certifies the exact common local
   order \(m\) of \(2\). Put

   \[
   L=\operatorname{lcm}(2,m)=2e.
   \tag{17}
   \]

   If \(m\) is even, take \(h=2\). If \(m\) is odd, take \(h=-2\). Then
   \(h\) has exact order \(L\) in every hidden component. Equation (9)
   implies

   \[
   L\ge m>n.
   \tag{18}
   \]

3. If every \(G_e=1\), then

   \[
   \boxed{e_j>C\qquad(1\le j\le s).}
   \tag{19}
   \]

## 5. Final trichotomy

The complete procedure returns exactly one of the following.

### Outcome A — factor

A verified proper divisor of \(N\).

### Outcome B — exact common state above the input length

A public pair \((h,L)\), with the complete factorization of \(L\), such
that

\[
\gcd(L,N)=1,
\qquad
\operatorname{ord}_{R_j}(h)=L>n
\quad(1\le j\le s).
\tag{20}
\]

### Outcome C — normalized hard base two

The public state \((-1,2)\) and block \(2\), with

\[
\boxed{
\sigma(\operatorname{ord}_{R_j}(2))>n,
\qquad
e_j>C
\quad(1\le j\le s).
}
\tag{21}
\]

In particular, every local absolute order of \(2\) also exceeds \(C\).
If this procedure is viewed inside the F174 transcript with target
\(D=n\), Outcome C is exactly the first line-13 escape \(\beta=2\).
No later hard escape can survive.

## 6. Complexity and complete-factor recursion

The integer \(\Lambda_n\) and its complete factorization are constructed by
a sieve through \(n\). Its bit length is polynomial in \(n\). Absolute
divisor stripping uses polynomially many modular powers and gcds.

The relative scan uses \(C\) modular powers and gcds. Trial division of a
first return \(e\le C\), divisor stripping from \(2e\), and all state
encodings have QP bit cost. The Mersenne exponent screen has polynomial
cost. Thus the full trichotomy has uniform deterministic QP bit cost.

Every factor exit supports complete-factor recursion. A complete binary
factor tree has at most \(\lfloor\log_2N\rfloor<n\) prime leaves, counted
with multiplicity, and fewer than \(2n\) total nodes. Deterministic
primality testing and the polynomial number of QP calls preserve the QP
bound, including for repeated prime factors.

## 7. Exact exclusions

F176 V2 does not prove any of the following.

- Outcome C is impossible.
- Unequal hidden local orders of \(2\) can be localized in QP time.
- A QP bank of exponents \(N^k\pm1\) contains a multiple of one hidden
  order but not another.
- Large absolute primary order or large quotient order yields an exact
  common order.
- Ordinary hard order transfers to a nonsplit quadratic torus.
- Integer factoring is in deterministic or Las Vegas QP time.

The remaining order-only question is now singular: force progress from the
normalized hard base-two block.
