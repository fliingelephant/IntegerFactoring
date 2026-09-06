# F277 — integer-valued finite differences expose remote binomial and Stirling gates

## Status and scope

This is a proof-only candidate. It addresses the integer-valued-polynomial
seam left open by P224/F274. It proves exact identities for three named
families:

1. the binomial-basis action of a high forward difference;
2. the shifted-binomial family from P215/F249; and
3. two normalized monomial differences on the balanced semiprime promise.

The normalized monomial differences give new exact central-Stirling
congruences, but no numerical-quasipolynomial evaluator. Either one can
return a saturated gcd, and this packet proves no joint nonvanishing
theorem. It proves no lower bound for general integer-valued-polynomial
circuits, canonical-division algorithms, or remote-coefficient evaluators.

No C++ search, dataset, or empirical claim belongs to this packet.

## 1. Balanced notation

Let

\[
 N=pq,\qquad p<q<2p,
\tag{1}
\]

where \(p,q\) are distinct odd primes. Put

\[
 B=\lfloor\sqrt N\rfloor,\qquad s=B-p,\qquad d=q-p.
\tag{2}
\]

Then

\[
 0\le s<(\sqrt2-1)p,\qquad p\le B<q.
\tag{3}
\]

If \(s=0\), the public gcd \(\gcd(B,N)=p\) already factors \(N\).
On the unresolved branch \(s>0\),

\[
 \boxed{d\ge2s+2,\qquad q-B=d-s\ge s+2,\qquad 2s+1<p.}
\tag{4}
\]

## 2. Exact binomial-basis action

Let

\[
 \operatorname{Int}(\mathbb Z)
 =\{f\in\mathbb Q[X]:f(\mathbb Z)\subseteq\mathbb Z\},
\]

and let \(\Delta f(X)=f(X+1)-f(X)\).

### Theorem 1 — the high difference is a coefficient shift

Every \(f\in\operatorname{Int}(\mathbb Z)\) of degree at most \(D\)
has the unique Newton expansion

\[
 \boxed{
 f(X)=\sum_{j=0}^{D}a_j\binom Xj,
 \qquad a_j=\Delta^jf(0)\in\mathbb Z.}
\tag{5}
\]

For every integer \(a\) and \(0\le k\le D\),

\[
 \boxed{
 \Delta^kf(a)=\sum_{j=k}^{D}a_j\binom a{j-k}.}
\tag{6}
\]

Thus integer-valued normalization removes the universal \(k!\) from
P224, but it does not automatically evaluate the result. It shifts the
problem to Newton coefficients and residual binomial values. A sparse
monomial description can have a remote Newton coefficient: for example,

\[
 \boxed{
 {\Delta^B X^m(0)\over B!}
 =\left\{\begin{matrix}m\\B\end{matrix}\right\},}
\tag{7}
\]

where the right side is a Stirling number of the second kind.

## 3. The shifted-binomial difference is the same hidden threshold

For an integer \(c\), put

\[
 F(c)=\binom{N+c-1}{B}.
\tag{8}
\]

### Theorem 2 — exact difference phase transition

For \(0\le k\le B\),

\[
 \boxed{\Delta_c^kF(c)=\binom{N+c-1}{B-k}.}
\tag{9}
\]

If \(1\le c<p\), then modulo \(N\),

\[
 \boxed{
 \Delta_c^kF(c)\equiv
 \begin{cases}
 q\binom{c-1}{s-k},&0\le k\le s,\\[4pt]
 \binom{c-1}{B-k},&s<k\le B.
 \end{cases}}
\tag{10}
\]

The second line has the same residue in both hidden components. It has
lost the \(p/q\) asymmetry, although evaluating a large public binomial
can remain a remote-coefficient problem.

At the fixed endpoint \(c=1\), equation (10) becomes the exact spike

\[
 \boxed{
 \Delta_c^kF(1)\equiv
 \begin{cases}
 q,&k=s,\\
 1,&k=B,\\
 0,&0\le k<B,\ k\ne s
 \end{cases}
 \pmod N.}
\tag{11}
\]

Finite differences therefore translate the hidden singular index; they
do not locate it. Taking an order beyond the hidden threshold removes the
asymmetry.

## 4. Short binomial quotients are factor-first

### Theorem 3 — short-side Kummer carries are direct numerator gcds

Let \(U\ge V\ge0\) be public integers and

\[
 w=\min(V,U-V).
\]

Suppose \(w<p\). Then

\[
 \binom UV
 =\frac{\prod_{i=1}^{w}(U-w+i)}{w!},
\tag{12}
\]

and \(w!\) is a unit modulo \(N\). Hence the coefficient modulo \(N\)
is evaluated by \(w\) public numerator factors and one unit inversion.
For either hidden prime \(r\in\{p,q\}\),

\[
 v_r\!\binom UV>0
 \quad\Longleftrightarrow\quad
 r\mid U-w+i\text{ for some }1\le i\le w.
\tag{13}

Thus every Kummer carry in this short-side range is already exposed by a
gcd of the short numerator product, or by the individual numerator gcds.
If \(w\) is numerical quasipolynomial in the input bit length, this is a
numerical-QP factor-first computation.

The theorem says nothing when both sides of the binomial coefficient are
long. That is exactly the remote factorial/carry range of P171, P215, and
P224.

An exact control is

\[
 \Delta^B\binom X{2B}\bigg|_{X=2B}
 =\binom{2B}{B}.
\tag{14}
\]

On (1), Kummer's theorem gives no base-\(p\) carry and one base-\(q\)
carry, so

\[
 \gcd\!\left(\binom{2B}{B},N\right)=q.
\tag{15}
\]

Equation (14) is an integer-valued finite-difference presentation of the
known central-binomial gate, not a new evaluator.

## 5. Two central-Stirling congruences

Write

\[
 \left\{\begin{matrix}n\\k\end{matrix}\right\}
\]

for the number of set partitions of an \(n\)-element set into \(k\)
nonempty blocks. On the unresolved branch \(s>0\), define

\[
 T_0=\frac{\Delta^BX^{2B}(0)}{B!}
 =\left\{\begin{matrix}2B\\B\end{matrix}\right\},
\qquad
 T_1=\frac{\Delta^BX^{2B+1}(0)}{B!}
 =\left\{\begin{matrix}2B+1\\B\end{matrix}\right\}.
\tag{16}
\]

### Theorem 4 — exact local laws

The \(q\)-components vanish:

\[
 \boxed{T_0\equiv T_1\equiv0\pmod q.}
\tag{17}
\]

The \(p\)-components are

\[
 \boxed{
 T_0\equiv
 2\left\{\begin{matrix}2s+1\\s\end{matrix}\right\}\pmod p,}
\tag{18}
\]

and

\[
 \boxed{
 T_1\equiv
 2\left\{\begin{matrix}2s+2\\s\end{matrix}\right\}\pmod p.}
\tag{19}
\]

Consequently,

\[
 \gcd(T_i,N)=
 \begin{cases}
 q,&p\nmid T_i,\\
 N,&p\mid T_i,
 \end{cases}
\qquad i\in\{0,1\}.
\tag{20}
\]

Neither scalar is an all-input factor oracle. Exact saturated examples are

\[
 37\cdot47,\quad B=41,\quad s=4,
 \quad 37\mid2\left\{\begin{matrix}9\\4\end{matrix}\right\},
\tag{21}
\]

for \(T_0\), and

\[
 19\cdot29,\quad B=23,\quad s=4,
 \quad 19\mid2\left\{\begin{matrix}10\\4\end{matrix}\right\},
\tag{22}
\]

for \(T_1\).

The pair is simultaneously saturated exactly when

\[
 p\mid
 \gcd\!\left(
 \left\{\begin{matrix}2s+1\\s\end{matrix}\right\},
 \left\{\begin{matrix}2s+2\\s\end{matrix}\right\}
 \right).
\tag{23}
\]

Using the Stirling recurrence, this is equivalent to divisibility of both

\[
 \left\{\begin{matrix}2s+1\\s\end{matrix}\right\},
 \qquad
 \left\{\begin{matrix}2s+1\\s-1\end{matrix}\right\}
\tag{24}
\]

by \(p\). F277 proves no impossibility of (23), no all-input pair theorem,
and no probability law for these residues.

## 6. Evaluator boundary

The identities above do not evaluate \(T_0\) or \(T_1\) modulo \(N\) in
numerical-QP time.

1. Inclusion-exclusion gives

   \[
   B!\left\{\begin{matrix}m\\B\end{matrix}\right\}
   =\sum_{j=0}^{B}(-1)^{B-j}\binom Bj j^m.
   \tag{25}
   \]

   This has \(B+1\) literal terms. Moreover
   \(\gcd(B!,N)=p\), so division by \(B!\) modulo \(N\) is invalid and
   the denominator gcd already factors.

2. The ordinary recurrence

   \[
   \left\{\begin{matrix}m+1\\k\end{matrix}\right\}
   =k\left\{\begin{matrix}m\\k\end{matrix}\right\}
   +\left\{\begin{matrix}m\\k-1\end{matrix}\right\}
   \tag{26}
   \]

   is division-free, but its literal table or row computation has a
   characteristic-size index range.

3. The exact integers \(T_0,T_1\) have
   \(\Theta(B\log(B+1))\) bits. Exact materialization is exponential in
   the bit length of \(N\).

These are named-representation costs, not an arithmetic-circuit lower
bound. A succinct modular central-Stirling evaluator remains outside the
packet. Such an evaluator, together with a proved joint nonvanishing or a
different all-input dispatcher, would be genuinely new.

## 7. Search decision

No larger C++ search is justified for the exact families above.

- The shifted-binomial differences are completely classified by (10).
- QP-short binomial quotients reduce to the direct factor-first screen in
  Theorem 3.
- The central-Stirling local laws are exact, while their unresolved step is
  an operational remote-coefficient evaluator and, for the pair, the
  number-theoretic condition (23).

A future symbolic search becomes materially new only after it specifies an
operational grammar that can fast-forward (25) or (26) with numerical-QP
work, without a nonunit inverse, a factor as advice, or a remote block as an
oracle. Finite hit rates or guessed recurrences without such an evaluator
do not pass this theory gate.

## Exact exclusions

F277 proves no:

1. numerical-QP evaluator for a remote binomial or Stirling coefficient;
2. all-input factor oracle from \(T_0\), \(T_1\), or their pair;
3. nonvanishing theorem for (23);
4. lower bound for integer-valued-polynomial, canonical-division,
   arithmetic, algebraic, or Boolean circuits;
5. general classification of Lucas or Kummer constructions;
6. all-input integer-factoring algorithm; or
7. empirical result.
