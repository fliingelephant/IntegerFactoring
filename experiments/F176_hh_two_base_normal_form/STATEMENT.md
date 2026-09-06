# F176 V3 candidate — every surviving QP-hard source is normalized base two

## Status and scope

This is a standalone proof-only QP source theorem for arbitrary odd
composites. It strengthens F176 V2 by using an arbitrary fixed numerical QP
absolute cap \(B\), not only the input length.

Let

\[
n=\lceil\log_2(N+1)\rceil.
\tag{1}
\]

The exact output is

\[
\boxed{
\text{factor}
\quad\lor\quad
\text{factored exact common-order state above }n
\quad\lor\quad
\text{one normalized QP-hard base-two block}.
}
\tag{2}
\]

The last branch remains genuine missing progress. F176 V3 is not a
factoring algorithm.

## 1. Parameters and hidden notation

Let \(N\ge3\) be odd and composite. Inputs below one fixed absolute
threshold are factored by direct trial division. Choose integers

\[
n\le B<N-1,
\qquad
C\ge n,
\qquad
B,C=2^{(\log n)^{O(1)}}.
\tag{3}
\]

The constants hidden in the QP bounds are fixed independently of \(N\).
For the proof only, write

\[
N=\prod_{j=1}^s R_j,
\qquad
R_j=p_j^{a_j},
\tag{4}
\]

where the \(p_j\) are distinct odd primes. Define

\[
\sigma(r)=\max_{\ell^a\parallel r}\ell^a,
\qquad
\sigma(1)=1.
\tag{5}
\]

The public pair \((-1,2)\) is an exact common-order state in every hidden
component.

## 2. Absolute factor-first screen

Put

\[
\Lambda_B=\operatorname{lcm}(1,2,\ldots,B)
\tag{6}
\]

and compute

\[
A=\gcd(2^{\Lambda_B}-1,N).
\tag{7}
\]

Exactly one of the following occurs.

1. If \(1<A<N\), then \(A\) is a proper factor.
2. If \(A=N\), use the known factorization of \(\Lambda_B\) for
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
   \sigma(\operatorname{ord}_{R_j}(2))>B
   \qquad(1\le j\le s).
   }
   \tag{9}

Only case 3 reaches the relative screen.

## 3. Every common base-two return gives progress

Suppose (8) is obtained. If \(m>n\), then \((2,m)\) is already Outcome B.
This includes the full intermediate range

\[
n<m\le B.
\tag{10}
\]

Suppose \(m\le n\). Since \(N\mid2^m-1\) and \(N>2^{n-1}\), one must have

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

If \(n\) is prime, the composite-input promise makes \(n\) odd. The public
element \(-2\) then has exact order \(2n\) in every hidden prime-power
component. Thus

\[
\boxed{(-2,2n)}
\tag{13}
\]

is a factored exact common-order state above \(n\).

Consequently a common return never leaves a hard branch, even when its
order is at most the larger cap \(B\).

## 4. Relative screen against the sign state

Assume \(A=1\). Define

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

   Factor the known annihilating multiple \(2e\) and apply factor-first
   divisor stripping. This either factors \(N\), or certifies one exact
   common local order \(m\) for \(2\). Put

   \[
   L=\operatorname{lcm}(2,m)=2e.
   \tag{17}
   \]

   If \(m\) is even, take \(h=2\). If \(m\) is odd, take \(h=-2\). Then
   \(h\) has exact order \(L\) in every hidden component. Equation (9)
   gives

   \[
   L\ge m>B\ge n.
   \tag{18}
   \]

3. If every \(G_e=1\), then

   \[
   \boxed{e_j>C\qquad(1\le j\le s).}
   \tag{19}

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

The theorem does not require \(L>B\).

### Outcome C — normalized QP-hard base two

The public state \((-1,2)\) and block \(2\), with

\[
\boxed{
\sigma(\operatorname{ord}_{R_j}(2))>B,
\qquad
e_j>C
\quad(1\le j\le s).
}
\tag{21}
\]

In particular, every local absolute order of \(2\) exceeds \(C\). If the
procedure is inserted before the F174 source loop, Outcome C is its first
possible hard source. No later source is needed for this trichotomy.

## 6. Complexity and complete-factor recursion

The sieve through \(B\) constructs \(\Lambda_B\) and its complete
factorization. Its bit length is \(O(B\log B)\), hence QP. Absolute divisor
stripping uses QP many modular powers and gcds.

The relative scan uses \(C\) modular powers and gcds. Trial division of a
first return \(e\le C\), stripping from \(2e\), and all state encodings have
QP bit cost. The Mersenne exponent screen has polynomial cost. The full
trichotomy therefore has uniform deterministic QP bit cost.

Every factor exit supports complete-factor recursion. A complete binary
factor tree has fewer than \(2n\) total nodes. Deterministic primality
testing and the polynomial number of QP calls preserve the QP bound,
including for repeated prime factors.

## 7. Exact exclusions

F176 V3 does not prove any of the following.

- Outcome C is impossible.
- Unequal hidden local orders of \(2\) can be localized in QP time.
- A QP bank of exponents \(N^k\pm1\) separates the hidden orders.
- A common cross-orbit period yields a factored ordinary order.
- Large absolute primary order or large quotient order yields an exact
  common order.
- Ordinary hard order transfers to a nonsplit quadratic torus.
- Integer factoring is in deterministic or Las Vegas QP time.

The remaining order-only question is singular: force progress from the
normalized base-two block after both pre-registered QP caps have failed.
