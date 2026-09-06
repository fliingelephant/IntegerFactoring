# Blind reconstruction of the modular-rectangle factoring reduction

## Scope and status

- Mathematical input read: RECTANGLE_STATEMENT_ONLY.md only.
- Verified SHA256: e6a68b51f1dc7f0820741b290c916f4318a126d4932ae3a12da3cab28777623d.
- Status: the stated conditional reduction reconstructs completely. No gap was found.
- Scope of the conclusion: this proves a reduction from integer factorization to the stated succinct modular rectangle-emptiness oracle. It does not construct that oracle or claim that its bound \(T\) is efficient.

Let the original input be \(N_0\ge 2\), with bit length \(n\). Write \(K\) for the integer at one recursive node and \(m\le n\) for its bit length. An oracle query below contains only \(K,M\), and four integer endpoints. It never contains a factorization of \(K\).

## Algorithm

Define \(\mathsf{Factor}(K)\) as follows.

1. Check the six fixed primes

   \[
   S=\{2,3,5,7,11,13\}.
   \]

   If \(K=p\in S\), return \(p\). If some \(p\in S\) properly divides \(K\), return \(p\) together with \(\mathsf{Factor}(K/p)\). Thus the rectangle stage is reached only when \(K\ge17\) and no member of \(S\) divides \(K\).

2. Let \(M\) be the largest power of two with \(M\le K/8\). Put

   \[
   R=\frac{17}{16},\qquad L_j=16R^j.
   \]

   For every \(j\ge0\) with \(L_j\le\sqrt K\), form

   \[
   \begin{aligned}
   I_j&=[\max(17,\lceil L_j\rceil),
          \min(\lfloor\sqrt K\rfloor,\lfloor RL_j\rfloor)],\\
   J_j&=[\max(1,\lceil K/(RL_j)\rceil),
          \min(M-1,\lfloor K/L_j\rfloor)].
   \end{aligned}
   \]

   Omit a pair if either integer interval is empty. All comparisons and roundings use exact rational numerators and denominators.

3. If no pair remains, return \(K\) as prime. Otherwise query

   \[
   \operatorname{Empty}(K,M,I_j,J_j)
   \]

   for the remaining pairs. If every pair is empty, return \(K\) as prime.

4. Choose a pair \(I=[A,B]\), \(J=[C,D]\) reported nonempty. Maintain a nonempty current interval \([a,b]\subseteq I\), initially \([A,B]\), while keeping \(J\) fixed. If \(a<b\), let \(h=\lfloor(a+b)/2\rfloor\) and query the left subrectangle \([a,h]\times J\). Keep \([a,h]\) if it is nonempty; otherwise keep \([h+1,b]\). The latter is nonempty because the old rectangle was nonempty and the two parts partition it. Continue until \(a=b=x\).

5. The proof below shows that \(x\) is a proper divisor of \(K\). Return \(\mathsf{Factor}(x)\) together with \(\mathsf{Factor}(K/x)\).

The returned list can be sorted if a canonical output order is wanted.

## The modulus and valid oracle endpoints

For \(K\ge17\), \(K/8\ge2\), so \(M\) exists and \(M\ge2\). Maximality among powers of two gives

\[
M\le\frac K8<2M,
\qquad\text{hence}\qquad
\frac K{16}<M\le\frac K8. \tag{1}
\]

Every retained \(I_j\) has lower endpoint at least \(17\). Its existence therefore implies

\[
17\le\lfloor\sqrt K\rfloor,
\]

so \(K\ge289>256\). Consequently

\[
\sqrt K<\frac K{16}<M. \tag{2}
\]

Thus both endpoints of every retained \(I_j\) lie in \([1,M-1]\). A retained \(J_j\) has lower endpoint at least \(1\), upper endpoint at most \(M-1\), and lower endpoint no larger than its upper endpoint. Its endpoints also lie in \([1,M-1]\). Every later bisection interval is a nonempty subinterval of \(I_j\), so all later queries satisfy the same endpoint requirement. The algorithm never sends an empty or out-of-range interval to the oracle.

## A modular witness in a box is an exact factor pair

Take any integers \(x\in I_j\) and \(y\in J_j\). The definitions imply

\[
L_j\le x\le RL_j,
\qquad
\frac K{RL_j}\le y\le\frac K{L_j}.
\]

Therefore

\[
\frac K R=\frac{16K}{17}
\le xy\le
RK=\frac{17K}{16}. \tag{3}
\]

Equivalently,

\[
-\frac K{17}\le xy-K\le\frac K{16}.
\]

By (1), this entire interval lies strictly inside \((-M,M)\), including at the upper endpoint because \(K/16<M\). If \(xy\equiv K\pmod M\), then \(xy-K\) is a multiple of \(M\); the only such multiple in \((-M,M)\) is zero. Hence

\[
xy\equiv K\pmod M
\quad\Longleftrightarrow\quad
xy=K. \tag{4}
\]

This holds for every generated box and every subrectangle used in bisection. The reverse implication is immediate. It explicitly excludes \(K+M\), \(K-M\), and every more distant congruent value.

## Every surviving composite produces a nonempty box

Suppose the rectangle stage receives a composite \(K\). Let \(x\) be its least prime divisor and let \(y=K/x\). No fixed prime divides \(K\), so

\[
17\le x\le\sqrt K. \tag{5}
\]

The increasing sequence \(L_j\) starts at \(16\le x\). Choose the largest \(j\) such that \(L_j\le x\). Then

\[
L_j\le x<L_{j+1}=RL_j,
\]

and \(L_j\le x\le\sqrt K\), so this \(j\) is among those enumerated. Exact ceiling and floor operations put \(x\) in \(I_j\), including when \(x\), \(L_j\), \(RL_j\), or \(\sqrt K\) is an endpoint.

The same inequalities give

\[
\frac K{RL_j}<y\le\frac K{L_j}.
\]

Moreover, by (1) and \(x\ge17\),

\[
1\le y=\frac Kx\le\frac K{17}<\frac K{16}<M. \tag{6}
\]

Since \(y\) is an integer, (6) gives \(y\le M-1\). Exact ceiling and floor operations therefore put \(y\) in \(J_j\). Neither interval is omitted, and \((x,y)\) is an exact, hence modular, witness in that box.

This proves both completeness statements needed by the algorithm:

- A surviving composite cannot produce no boxes.
- A surviving composite cannot have all generated boxes reported empty.

## Prime recognition and correctness of recursion

The members of \(S\) are fixed known primes. Any integer from \(2\) through \(16\) is either in \(S\) or has a proper divisor in \(S\), so only \(K\ge17\) can reach the rectangle stage.

If that stage declares \(K\) prime because no boxes remain or because all boxes are empty, the completeness result shows that \(K\) cannot be composite. Conversely, if a generated box for a prime \(K\) were nonempty, (4) would give \(xy=K\) with \(17\le x\le\sqrt K<K\), a proper factorization. Thus the boxes for a prime really are empty. This is a complete primality decision inside the reduction. It uses no external primality oracle or primality algorithm.

When bisection ends at \(x\), the maintained singleton rectangle is nonempty. Some \(y\in J\) therefore satisfies the modular relation. By (4), \(xy=K\). Also \(17\le x\le\sqrt K<K\), so \(x\) and \(K/x\) are integers strictly between \(1\) and \(K\). The recursive split is correct and strictly decreases its arguments. Recursion terminates and its leaves are primes by the preceding paragraph. Their product is \(N_0\).

This reasoning covers all multiplicities. A prime power is repeatedly split until each copy of its prime is a leaf; the argument does not require the first recovered divisor to be prime. It also covers very unbalanced composites: their least prime divisor supplies \(x\), while (6) puts even a very large cofactor below \(M\).

## Box count and representation size

Before empty intervals are omitted, the number of indices is at most

\[
1+\left\lfloor\log_R\left(\frac{\sqrt K}{16}\right)\right\rfloor
\]

when \(\sqrt K\ge16\), and is zero otherwise. Since \(R=17/16\) is fixed, this is \(O(\log K)=O(m)\).

An exact unreduced representation is

\[
L_j=\frac{16\cdot17^j}{16^j}.
\]

The index bound is \(j=O(m)\), so its numerator and denominator, those for \(RL_j\), and those obtained after combining them with \(K\) all have \(O(m)\) bits with an absolute fixed constant. Exact comparisons, ceilings, and floors are therefore polynomial-time integer operations. The integer endpoints sent to the oracle are even smaller: \(K\) has \(m\) bits, while \(M\) and every endpoint are less than \(K\). Thus every oracle input in the entire recursion has \(O(n)\) bits with one uniform fixed constant. The rectangles remain succinct; their points are never enumerated.

Locating a nonempty box uses \(O(m)\) queries. Bisection uses at most

\[
\lceil\log_2(B-A+1)\rceil\le\lceil\log_2 M\rceil=O(m)
\]

additional queries. Hence one rectangle-stage invocation uses \(O(m)\), and certainly \(O(n)\), oracle calls.

## Accumulated bit complexity

View every proper split as a binary factor tree whose leaves are the prime factors of \(N_0\), counted with multiplicity. If there are \(q\) leaves, then

\[
2^q\le N_0,
\qquad q\le\log_2N_0<n,
\]

and the tree has at most \(2q-1=O(n)\) nodes. This count includes repeated factors and fixed-prime splits. At most \(O(n)\) nodes can reach the rectangle stage, and each makes \(O(n)\) oracle calls. The total is therefore \(O(n^2)\).

All non-oracle work is polynomial in \(n\): fixed-prime divisibility tests, exact rational generation and comparison, integer square roots and roundings, bisection arithmetic, exact quotients, recursion bookkeeping, and output ordering. Only polynomially many operations are performed, and every operand has \(O(n)\) bits.

For a deterministic oracle of uniform cost at most \(T(n)\), the resulting deterministic bound is

\[
O\bigl(n^2T(n)+\operatorname{poly}(n)\bigr).
\]

For an always-correct Las Vegas oracle, run each invocation with fresh independent random bits. Because every answer is correct, the adaptive query sequence has a deterministic \(Q=O(n^2)\) call cap. Conditioned on the complete history before any next call, that call's input is fixed and its fresh random bits give conditional expected cost at most \(T(n)\). Set the cost of every unused position up to \(Q\) to zero. The tower property and linearity of expectation then give total expected oracle cost at most \(QT(n)=O(n^2T(n))\). Each actual call terminates almost surely, so the deterministically bounded finite computation terminates almost surely. Every returned factorization is correct.

Multiplying a quasipolynomial \(T(n)\) by \(n^2\) and adding a polynomial preserves quasipolynomial complexity. Therefore such an oracle bound would yield an all-input classical quasipolynomial factoring algorithm, conditionally on the oracle guarantee.

## Case and boundary audit

- **Small and even inputs:** Equality with a fixed prime is a prime leaf. A proper fixed-prime divisor is split off. This handles all inputs below \(17\), every even input, and every occurrence of \(3,5,7,11,\) or \(13\).
- **No generated boxes:** A composite with no fixed-prime divisor has least prime divisor at least \(17\), so it is at least \(17^2=289\) and has the box constructed above. Thus every surviving \(K<289\) is prime, and an empty retained-box list cannot cause a false prime declaration. This includes the cases in which no \(j\) is enumerated and those in which an enumerated pair has an empty integer interval and is omitted.
- **Prime inputs:** Fixed primes are recognized directly. A larger prime has no nonempty generated box by (4), so it is recognized without an external primality test.
- **Prime powers and repeated factors:** Each proper split preserves exact product, and recursion records every multiplicity.
- **Unbalanced and arbitrary composites:** The least prime divisor lies in \([17,\sqrt K]\). Its cofactor can be large but is strictly less than \(M\) by (6).
- **Perfect squares:** The value \(x=\sqrt K\) is retained by the closed upper endpoint \(\lfloor\sqrt K\rfloor\).
- **Grid and rounding equalities:** Closed intervals and exact ceilings and floors retain factors equal to a grid endpoint. Adjacent boxes may overlap at an endpoint; this is harmless.
- **Modulus endpoints:** All queried \(x,y\) lie in \([1,M-1]\). Equality \(y=M-1\) is allowed. Equality \(x=M\) or \(y=M\) cannot occur.
- **Congruence degeneracies:** Equation (3) and the strict inequality \(M>K/16\) exclude both neighboring values \(K-M,K+M\), even at the product-corridor endpoints. They therefore exclude all other congruent values as well.
- **Adaptivity:** Each bisection query is a valid subrectangle. Correct emptiness answers preserve the nonempty invariant, so no witness-returning or support-optimization oracle is needed.
