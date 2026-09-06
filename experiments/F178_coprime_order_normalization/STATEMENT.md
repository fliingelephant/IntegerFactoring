# F178 candidate — hidden-prime order support can be removed in QP time

## Status and scope

This is a proof-only constructive postprocessor for P159. It applies to
arbitrary odd composites, including repeated prime factors. It is not an
all-input factoring algorithm.

Let

\[
n=\lceil\log_2(N+1)\rceil,
\qquad
N=\prod_{j=1}^s R_j,
\qquad
R_j=p_j^{a_j},
\tag{1}
\]

where the factorization is hidden. Suppose P159 reaches its normalized hard
branch. Thus, for one fixed QP cap \(C\ge n\),

\[
e_j:=\operatorname{ord}_{R_j}(4)>C
\qquad(1\le j\le s).
\tag{2}
\]

Choose any fixed numerical QP cap

\[
T\ge \max\{n,2C\}.
\tag{3}
\]

The postprocessor returns exactly one of

\[
\boxed{
\text{factor}
\quad\lor\quad
\text{factored exact common-order state above }n
\quad\lor\quad
\text{a componentwise coprime-order hard block}.
}
\tag{4}
\]

## 1. Remove every hidden-prime primary part

Put

\[
E=N^n,
\qquad
y=4^E\bmod N,
\tag{5}
\]

and, for the proof only, define

\[
f_j=\operatorname{ord}_{R_j}(y)
    =\frac{e_j}{\gcd(e_j,E)}.
\tag{6}
\]

Then

\[
\boxed{\gcd(f_j,N)=1\qquad(1\le j\le s).}
\tag{7}
\]

Compute

\[
H=\gcd(y-1,N).
\tag{8}
\]

A proper \(H\) factors \(N\). The case \(H=N\) also factors: if \(p\) is
the least rational prime divisor of \(N\), then \(f_p=1\) forces
\(\operatorname{ord}_p(4)=1\), hence \(p=3\), and \(\gcd(3,N)=3\) is
proper. Therefore the surviving branch has

\[
\boxed{H=1,\qquad f_j>1,\qquad \gcd(f_j,N)=1}
\tag{9}
\]

for every hidden component.

## 2. Factor-first lcm screen

Let

\[
\Lambda_T=\operatorname{lcm}(1,2,\ldots,T)
\tag{10}
\]

and compute

\[
J=\gcd(y^{\Lambda_T}-1,N).
\tag{11}
\]

Exactly one of the following occurs.

1. If \(1<J<N\), return \(J\).
2. If \(J=N\), factor-first divisor stripping with the known factorization
   of \(\Lambda_T\) either returns a proper factor or certifies one exact
   common order

   \[
   m=\operatorname{ord}_{R_j}(y)
   \qquad(1\le j\le s).
   \tag{12}
   \]

   If \(m>n\), return the state \((y,m)\). If \(m\le n\), the public gcd

   \[
   D=\gcd(4^m-1,N)
   \tag{13}
   \]

   is a proper factor.
3. If \(J=1\), then

   \[
   \boxed{\sigma(f_j)>T\qquad(1\le j\le s),}
   \tag{14}
   \]

   where \(\sigma(r)\) is the largest prime-power divisor of \(r\).

## 3. Final hard branch

In the only surviving branch, the public unit \(y\) satisfies, in every
hidden prime-power component,

\[
\boxed{
f_j>1,
\qquad
\gcd(f_j,N)=1,
\qquad
\sigma(f_j)>T.
}
\tag{15}
\]

Its order modulo the sign subgroup also remains large:

\[
\boxed{
\operatorname{ord}_{R_j^\times/\langle-1\rangle}
  (y\langle-1\rangle)>C.
}
\tag{16}
\]

Thus the remaining order obstruction is purely coprime to the input. It is
not caused by repeated prime factors or by order-primary factors supported on
the hidden rational primes.

## 4. Complexity and exact boundary

The exponent \(E=N^n\) has \(O(n^2)\) bits. The sieve through \(T\), the
construction and factorization of \(\Lambda_T\), all modular powers, gcds,
and divisor-stripping steps have uniform deterministic QP bit cost. Composing
this postprocessor with P159 preserves its complete-factor recursion bound.

F178 does not prove any of the following.

- The final local orders \(f_j\) are equal.
- A QP-size factored common annihilator of all \(f_j\) exists.
- An unfactored value such as \(N^k-1\) can be converted to an exact
  common-order state in QP time.
- The final hard block factors \(N\).
- Integer factoring is in deterministic or Las Vegas QP time.
