# Proof of F277

## 1. Balanced inequalities

From \(p<q<2p\),

\[
 p<\sqrt{pq}<\sqrt2p<q.
\]

Therefore \(p\le B<q\) and

\[
 0\le s=B-p<(\sqrt2-1)p.
\]

If \(s=0\), then \(B=p\) and \(\gcd(B,N)=p\).

Assume \(s>0\). The lower floor-square inequality gives

\[
 (p+s)^2=B^2\le p(p+d),
\]

so

\[
 pd\ge2ps+s^2>2ps.
\]

The prime gap \(d=q-p\) is even. Hence \(d\ge2s+2\), and

\[
 q-B=d-s\ge s+2.
\]

The cases \(p=3,5\) have \(s=0\), so \(s>0\) implies \(p\ge7\). Since
\(s<(\sqrt2-1)p\),

\[
 2s+1<2(\sqrt2-1)p+1<p
\]

for \(p\ge7\). This proves (3)--(4). The same estimate gives
\(p-s>3\), which will exclude an all-fixed-block case below.

## 2. Newton expansion and coefficient shift

For a polynomial \(f\) of degree at most \(D\), Newton interpolation at
the consecutive integers gives

\[
 f(X)=\sum_{j=0}^{D}\Delta^jf(0)\binom Xj.
\tag{27}
\]

If \(f\) is integer-valued, every iterated difference of its integer
values is an integer, so \(\Delta^jf(0)\in\mathbb Z\). Conversely, every
integer combination of the binomial polynomials is integer-valued. The
Newton interpolation is unique because the \(j\)-th term has degree \(j\)
with nonzero leading coefficient. This proves (5).

Pascal's identity gives

\[
 \Delta\binom Xj=\binom X{j-1}.
\tag{28}
\]

Iterating (28), substituting (5), and evaluating at \(a\) proves (6).

For a monomial, the ordinary finite-difference formula is

\[
 \Delta^BX^m(0)
 =\sum_{j=0}^{B}(-1)^{B-j}\binom Bj j^m.
\tag{29}
\]

The right side counts surjections from an \(m\)-element labelled set to a
\(B\)-element labelled set. It is therefore

\[
 B!\left\{\begin{matrix}m\\B\end{matrix}\right\}.
\]

This proves (7) and (25).

## 3. Shifted-binomial differences

Pascal's identity in the upper argument gives

\[
 \Delta_c\binom{N+c-1}{m}=\binom{N+c-1}{m-1}.
\]

Iterating with \(m=B\) proves (9).

Fix \(1\le c<p\), and put \(m=B-k\). First suppose \(0\le k\le s\),
so

\[
 m=p+(s-k).
\]

Modulo \(q\), the low base-\(q\) digit of the upper argument
\(N+c-1\) is \(c-1\). Since \(m\ge p>c-1\) and \(m<q\), Lucas's theorem
gives zero.

Modulo \(p\), the low digits of the upper and lower arguments are
respectively \(c-1\) and \(s-k\); after removing those digits the lower
argument is one and the upper argument is \(q\). Recursive Lucas expansion
therefore gives

\[
 \binom{N+c-1}{m}
 \equiv q\binom{c-1}{s-k}\pmod p.
\tag{30}
\]

The integer on the right of (30) is zero modulo \(q\), so CRT proves the
first line of (10).

Now suppose \(k>s\), so \(0\le m<p<q\). Lucas's theorem at either hidden
prime has lower high digit zero and gives

\[
 \binom{N+c-1}{m}\equiv\binom{c-1}{m}.
\]

CRT proves the second line of (10). Setting \(c=1\) uses
\(\binom00=1\) and \(\binom0t=0\) for \(t>0\), which proves (11).

## 4. Short-side quotient and Kummer boundary

By binomial symmetry, choose the side \(w=\min(V,U-V)\). The exact product
formula is (12). Since \(w<p<q\), no hidden prime divides \(w!\); it is a
unit modulo \(N\).

For \(r\in\{p,q\}\), the denominator has zero \(r\)-adic valuation, so

\[
 v_r\binom UV
 =\sum_{i=1}^{w}v_r(U-w+i).
\]

This is positive exactly when at least one numerator factor is divisible
by \(r\). This proves (13). Kummer's theorem identifies the same event as
a base-\(r\) carry, but no hidden-base computation is needed in the short
range: the numerator product and all its factors are public.

For the control (14), use (28). To prove (15), write \(B=p+s\). Equation
(4) gives \(2s<p\), so adding \(B+B\) in base \(p\) creates no carry. On
the other hand \(B<q<2p\le2B<2q\), so adding \(B+B\) in base \(q\)
creates exactly one carry. Kummer's theorem gives

\[
 v_p\binom{2B}{B}=0,
 \qquad
 v_q\binom{2B}{B}=1.
\]

This proves (15).

## 5. The q-components of the central Stirling pair

Because \(B<q\), the denominator \(B!\) in (25) is a unit modulo \(q\).
For every integer \(j\), Fermat's identity \(j^q\equiv j\pmod q\) gives

\[
 j^{2B}\equiv j^{2B-q+1}\pmod q,
\qquad
 j^{2B+1}\equiv j^{2B-q+2}\pmod q.
\tag{31}
\]

Equation (4) gives

\[
 0<2B-q+1< B,
 \qquad
 0<2B-q+2< B.
\tag{32}
\]

Apply (25) with the two smaller exponents in (32). A Stirling number with
upper argument below its lower argument is zero. Since \(B!\) is invertible
modulo \(q\), equations (31)--(32) prove (17).

## 6. The p-components by a cyclic orbit count

We count set partitions modulo \(p\). Every nonfixed orbit of a cyclic
group of order \(p\) has size \(p\), so only invariant partitions
contribute.

### 6.1 The scalar T0

Let \(C_p\) act on a \(2B=2p+2s\)-element set as two disjoint \(p\)-cycles
and \(2s\) fixed points. An invariant partition into \(B=p+s\) blocks has
an induced action on its blocks. Since \(p+s<2p\), the block action has
either:

1. \(p+s\) fixed blocks; or
2. one orbit of \(p\) blocks and \(s\) fixed blocks.

In the first case, each element \(p\)-cycle is an indivisible atom. There
are only \(2s+2\) atoms. The inequality \(p-s>3\) gives
\(p+s>2s+2\), so this case is impossible.

In the second case, a globally fixed point cannot lie in a moving block:
its translates would place the same point in \(p\) disjoint blocks. Each
element \(p\)-cycle is therefore either split with one point in every
moving block or retained whole inside a fixed block.

If exactly one element cycle is split, there are two choices. The other
cycle is one atom, and together with the \(2s\) fixed points there are
\(2s+1\) atoms to partition into the \(s\) fixed blocks. This contributes

\[
 2\left\{\begin{matrix}2s+1\\s\end{matrix}\right\}.
\]

If both cycles are split, their relative phase has \(p\) choices. This
contribution is divisible by \(p\). Therefore the invariant-partition
count modulo \(p\) is exactly (18).

### 6.2 The scalar T1

For \(2B+1=2p+2s+1\) elements, use two \(p\)-cycles and \(2s+1\) fixed
points. The all-fixed-block case has only \(2s+3\) atoms and is impossible
because \(p-s>3\). If exactly one element cycle is split, the intact cycle
and the fixed points give \(2s+2\) atoms for the \(s\) fixed blocks. The
two choices of split cycle contribute

\[
 2\left\{\begin{matrix}2s+2\\s\end{matrix}\right\}.
\]

If both cycles are split, relative phase again supplies a factor \(p\).
This proves (19).

Combining (17)--(19) proves (20).

For (21),

\[
 \left\{\begin{matrix}9\\4\end{matrix}\right\}=7770,
 \qquad 2\cdot7770=37\cdot420.
\]

Also \(37\cdot47=1739\), \(41^2<1739<42^2\), so \(B=41\) and
\(s=4\). Thus both hidden components of \(T_0\) vanish.

For (22),

\[
 \left\{\begin{matrix}10\\4\end{matrix}\right\}=34105,
 \qquad 2\cdot34105=19\cdot3590.
\]

Also \(19\cdot29=551\), \(23^2<551<24^2\), so \(B=23\) and \(s=4\).
Thus both hidden components of \(T_1\) vanish.

Finally, the recurrence

\[
 \left\{\begin{matrix}2s+2\\s\end{matrix}\right\}
 =s\left\{\begin{matrix}2s+1\\s\end{matrix}\right\}
 +\left\{\begin{matrix}2s+1\\s-1\end{matrix}\right\}
\]

and \(s<p\) prove the equivalence of (23) and (24). No step proves that
this simultaneous divisibility is impossible.

## 7. Exact-size and operational boundaries

The number of partitions of \(2B\) into \(B\) pairs is

\[
 \frac{(2B)!}{2^BB!},
\]

so

\[
 T_0\ge\frac{(2B)!}{2^BB!}.
\]

Trivially, labelled assignments to \(B\) blocks give \(T_0\le B^{2B}\).
Stirling's elementary factorial bounds, or direct logarithms of these
products, show

\[
 \log_2T_0=\Theta(B\log(B+1)).
\]

The same conclusion for \(T_1\) follows by adding one element to a
partition and by the bound \(T_1\le B^{2B+1}\). On balanced inputs,
\(B=2^{\Theta(\log N)}\), so exact materialization has exponential output
length.

Equation (25) has \(B+1\) literal summands. Its denominator satisfies

\[
 \gcd(B!,N)=p
\]

because \(p\le B<q<2p\). Thus inverse-based modular division is invalid,
and materializing the denominator residue already reaches a proper gcd.
Equation (26) avoids division but its literal index range reaches \(B\).

These facts establish only the named-representation boundary in the
statement. They do not exclude a different succinct modular evaluator.
