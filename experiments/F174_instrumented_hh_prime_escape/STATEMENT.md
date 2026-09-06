# F174 candidate — an instrumented large-order search gives an exact state or a polylog-small hard prime

## Status and scope

This is a proof-only candidate. It is a deterministic QP source and decoder
theorem for arbitrary odd composite inputs. It is not a factoring algorithm.

The theorem opens the transcript of Harvey--Hittmeir Algorithm 3.1 instead
of treating its output as a black-box large-order element. It combines that
transcript with the P150/P154 factor-first order screens.

The exact output is

\[
\boxed{
\text{factor}
\quad\lor\quad
\text{factored exact common-order state above }D
\quad\lor\quad
\text{one polylog-small prime hard block}.
}
\tag{1}
\]

The last branch is real missing progress. It has large order and large
quotient capacity in every hidden prime-power component, but no exact common
quotient order. F174 does not claim that this hard block factors the input.

## 1. Parameters

Let \(N\ge3\) be an odd composite, and put

\[
n=\lceil\log_2(N+1)\rceil.
\]

Let \(D,C\) be integers such that

\[
n\le D<N-1,
\qquad
D,C=2^{(\log n)^{O(1)}}.
\tag{2}
\]

The constants hidden in the QP bounds are fixed independently of \(N\).
Inputs below one absolute threshold are factored by a finite table or direct
trial division.

For the proof only, write the unknown CRT decomposition as

\[
N=\prod_{j=1}^s R_j,
\qquad
R_j=p_j^{a_j},
\]

where the \(p_j\) are distinct odd primes.

For an integer \(m\ge1\), define its largest primary component by

\[
\sigma(m)=\max_{\ell^a\parallel m}\ell^a,
\qquad
\sigma(1)=1.
\tag{3}
\]

## 2. External Harvey--Hittmeir premise

Use Algorithm 3.1 of Harvey and Hittmeir, *Deterministic methods for finding
elements of large multiplicative order*, arXiv:2601.11131v2:

<https://arxiv.org/html/2601.11131>

For target \(D\), its stated deterministic bit cost is

\[
O\!\left(
\frac{D^{1/2}\log D}{(\log\log D)^{1/2}}\log N
\right).
\tag{4}
\]

The proof uses these explicit transcript facts from that algorithm.

1. The early return \(2^D<N\) occurs before the main loop.
2. The main loop uses

   \[
   B=\lceil D^{1/3}\rceil
   \]

   and scans \(\beta=2,3,\ldots,B\).
3. On entry to each iteration, the algorithm stores a unit \(g\), its exact
   global order \(M\), and the complete factorization of \(M\).
4. If \(\beta^M\ne1\pmod N\), it searches for
   \(\operatorname{ord}_N(\beta)\) through \(D\).
5. If that order is found, it runs every prime-divisor gcd screen, merges the
   exact order into \(M\) by the Harvey--Hittmeir lcm construction, and
   returns when \(M>D\).
6. If the search does not find the order, line 13 returns \(\beta\) with

   \[
   \operatorname{ord}_N(\beta)>D.
   \tag{5}
   \]
7. If the loop finishes, the final arithmetic-progression scan finds a
   prime divisor of composite \(N\).

F174 intercepts only the line-13 return and adds the screens below. It does
not change the Harvey--Hittmeir order searches or their source order.

## 3. Exact common-order invariant

On every no-factor loop iteration, the transcript state satisfies

\[
g^M=1\pmod N,
\]

\[
\operatorname{ord}_{R_j}(g)=M
\qquad(1\le j\le s),
\tag{6}
\]

the complete factorization of \(M\) is known, and

\[
\gcd(M,N)=1.
\tag{7}
\]

Before a line-13 escape or the loop-end scan, one also has \(M\le D\).

Thus the internal pair \((g,M)\) is already a P150/P154 certified
common-order state, including for repeated odd prime powers.

## 4. A QP smooth-prefix cutoff

Define the exact integers

\[
L_D=\lceil\log_2(2D)\rceil,
\qquad
J_D=\lceil\log_2(L_D+1)\rceil,
\tag{8}
\]

and put

\[
H_D=8L_DJ_D,
\qquad
X_D=2^{H_D},
\qquad
Y_D=H_D^2.
\tag{9}
\]

Then

\[
\log_2 X_D=H_D=O(\log D\log\log D),
\qquad
Y_D=O((\log D\log\log D)^2).
\tag{10}
\]

Suppose line 13 is reached at \(\beta\). Every integer
\(1\le a<\beta\) then satisfies

\[
a^M=1\pmod N.
\tag{11}
\]

If

\[
\beta-1\ge Y_D,
\tag{12}
\]

then a deterministic scan of the numbers

\[
kM+1\le X_D
\tag{13}
\]

finds a proper factor of \(N\). The number of candidates and their total
bit cost are QP.

Therefore every no-factor line-13 escape satisfies

\[
\boxed{
2\le\beta\le Y_D
=(\log D)^{O(1)}.
}
\tag{14}
\]

Since \(D\) is QP in \(n\), this gives

\[
\boxed{\beta=(\log n)^{O(1)}.}
\tag{15}
\]

This cutoff is stronger than the literal
\(\beta\le\lceil D^{1/3}\rceil\) loop bound.

## 5. The escaped integer is a prime outside every old local subgroup

On the no-factor line-13 branch, \(\beta\) is prime. Moreover, every
integer \(a<\beta\) is a unit and lies in

\[
H_j=\langle g\bmod R_j\rangle
\qquad(1\le j\le s),
\tag{16}
\]

while

\[
\beta^M\ne1\pmod N.
\tag{17}
\]

Thus \(\beta\) is the first positive integer in the HH source order that is
outside the current synchronized local cyclic layer.

## 6. Factor-first absolute-order classification

Put

\[
\Lambda_D=\operatorname{lcm}(1,2,\ldots,D)
\]

and compute

\[
A_\beta=\gcd(\beta^{\Lambda_D}-1,N).
\tag{18}
\]

Exactly one of the following happens.

1. A proper \(A_\beta\) factors \(N\).
2. If \(A_\beta=N\), divisor stripping from the known factored multiple
   \(\Lambda_D\) either factors \(N\), or returns the exact order \(m\) of
   \(\beta\) in every hidden component. In the latter case

   \[
   \boxed{m>D,}
   \tag{19}
   \]

   and \((\beta,m)\) is the required factored exact common-order state.
3. If \(A_\beta=1\), then

   \[
   \boxed{
   \sigma(\operatorname{ord}_{R_j}(\beta))>D
   \qquad(1\le j\le s).
   }
   \tag{20}
   \]

Only case 3 reaches the relative scan.

## 7. Factor-first relative-order classification

For \(e=1,2,\ldots,C\), compute

\[
G_e=\gcd(\beta^{eM}-1,N).
\tag{21}
\]

Let

\[
e_j=\operatorname{ord}_{(\mathbb Z/R_j\mathbb Z)^\times/H_j}
(\beta H_j).
\tag{22}
\]

Exactly one of the following happens.

1. A proper \(G_e\) factors \(N\).
2. A first global return \(G_e=N\) gives

   \[
   e_j=e
   \qquad(1\le j\le s).
   \tag{23}
   \]

   P150 factor-first certification either factors \(N\), or constructs a
   public element \(h\) of exact order

   \[
   L=Me=\operatorname{lcm}
   (M,\operatorname{ord}_N(\beta))
   \tag{24}
   \]

   in every hidden component. Its complete factorization is known, and

   \[
   \boxed{L>D.}
   \tag{25}
   \]

   Also \(e\ge2\), so this is strict common-order growth.
3. If every \(G_e=1\), then

   \[
   \boxed{e_j>C\qquad(1\le j\le s).}
   \tag{26}
   \]

   This is the hard-block branch.

## 8. Final trichotomy

The complete instrumented procedure returns exactly one of the following.

### Outcome A — factor

A verified proper divisor of \(N\).

### Outcome B — exact common state above the target

A public pair \((h,L)\), with the complete factorization of \(L\), such
that

\[
\gcd(L,N)=1,
\qquad
\operatorname{ord}_{R_j}(h)=L>D
\quad(1\le j\le s).
\tag{27}
\]

### Outcome C — polylog-small prime hard block

A public tuple \((g,M,\beta)\) such that

\[
\operatorname{ord}_{R_j}(g)=M\le D,
\]

\[
\beta\le Y_D=(\log D)^{O(1)},
\qquad
\beta\text{ is prime},
\tag{28}
\]

every smaller positive integer lies in every \(H_j\), and

\[
\sigma(\operatorname{ord}_{R_j}(\beta))>D,
\qquad
e_j>C
\quad(1\le j\le s).
\tag{29}
\]

Equivalently, the first \(C+1\) quotient fingerprints

\[
1,\beta^M,\beta^{2M},\ldots,\beta^{CM}
\tag{30}
\]

are distinct in every hidden component. A P154 table certifies

\[
|\langle g,\beta\rangle_{R_j}|
\ge M(C+1)
\qquad(1\le j\le s),
\tag{31}
\]

but it supplies no exact common quotient order.

## 9. Complexity

For QP \(D,C\), every step has deterministic QP bit cost.

- The HH call has cost (4).
- \(\Lambda_D\) has bit length \(O(D\log D)\). Its sieve, factorization,
  modular power, and divisor stripping are QP.
- The relative scan has \(C\) modular powers and gcds.
- \(X_D\) is a QP numerical bound because its binary logarithm is
  \(O(\log D\log\log D)=(\log n)^{O(1)}\).
- Every exact state and provenance word produced by the displayed
  prime-primary constructions has QP encoding length.

Thus (1) is a uniform deterministic QP theorem.

## 10. Consequence on a constant-common-capacity family

On the F172 family, every ordinary common order is at most six. Choose
\(D>6\). Outcome B is then impossible on a no-factor branch. Therefore the
instrumented deterministic HH source has the stronger family-specific
conclusion

\[
\boxed{
\text{factor}
\quad\lor\quad
\text{an algorithm-selected polylog-small prime hard block}.
}
\tag{32}
\]

This is an actual output law, unlike F173's supplied primitive witness. It
still does not locate the guaranteed hidden order mismatch in QP time.

## 11. Exact exclusions

F174 does not prove any of the following.

- Outcome C is impossible.
- Large absolute primary order or large quotient order yields a useful
  common order.
- A QP equality bank finds the unequal hidden local orders of \(\beta\).
- The small integer value of \(\beta\) creates a factor-correlated canonical
  inverse relation.
- The HH construction transfers high order into a Jacobi-minus-one torus.
- The F170 dual CRT threshold is reached.
- Integer factoring is in deterministic or Las Vegas QP time.

The surviving source question is now narrower: localize the unequal hidden
orders of one algorithm-selected prime \(\beta=(\log n)^{O(1)}\), or make
its retained integer presentation close a useful exact relation.
