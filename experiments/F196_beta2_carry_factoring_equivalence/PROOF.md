# Proof of F196

## 1. The balanced-prime congruence

Because \(p<\sqrt N<q\), and \(p\) is an integer,

\[
p\le B<q.
\tag{15}
\]

The inequality \(q<2p\) also gives \(N<2p^2\), hence

\[
B<2p.
\tag{16}
\]

Write \(B=p+r\), where \(0\le r<p\).

Since \(B<q\), every \(1,\ldots,B\) is invertible modulo \(q\), and

\[
C
=\prod_{j=1}^{B}\frac{N-j}{j}
\equiv(-1)^B\pmod q.
\tag{17}
\]

Therefore \(A=(-1)^BC\equiv1\equiv1-q\pmod q\).

Write \(q=p+d\), where \(1\le d<p\). In base \(p\),

\[
N-1=p^2+(d-1)p+(p-1),
\qquad B=0\cdot p^2+1\cdot p+r.
\tag{18}
\]

Lucas' theorem gives

\[
C
\equiv \binom10\binom{d-1}{1}\binom{p-1}{r}
\equiv(d-1)(-1)^r
\equiv(q-1)(-1)^r
\pmod p.
\tag{19}
\]

Because \(p\) is odd, \((-1)^B=-(-1)^r\). Thus

\[
A\equiv-(q-1)=1-q\pmod p.
\tag{20}
\]

Equations (17) and (20), together with \(N=pq\), prove (2). They also prove
that (3) is an integer and that rearrangement (4) is exact.

## 2. Polynomial-time evaluation of \(C\bmod2^n\)

Andreica's published algorithm states the bounds (6) and (7) for
\(0\le Q\le P\le2^T-1\). Its preprocessing depends only on \(T\). It
computes odd factorial parts modulo \(2^T\), tracks the exponent of two in
the factorials, and combines the three factorial terms using inverses of
odd residues. In particular, the published bound is bit complexity, not a
count of unit-cost operations on exponentially long integers.

The public value \(n=\lceil\log_2(N+1)\rceil\) satisfies

\[
N+1\le2^n,
\qquad
N-1\le2^n-2<2^n.
\tag{21}
\]

Also \(0\le B\le N-1\). Therefore the substitution

\[
T=n,
\qquad P=N-1,
\qquad Q=B
\tag{22}
\]

is inside the main range of the external theorem. Computing \(n\) and the
exact integer square root \(B\) takes polynomial bit time. The total cost is

\[
O\!\left(n^3\mathsf M(n)+n^4
+n^2\log n\,\mathsf M(n)\right),
\tag{23}
\]

which is polynomial in \(n\) for any standard integer-multiplication
algorithm. This proves Theorem 1.

No Lucas-type extension for upper indices at least \(2^n\) is needed here.
That removes a possible ambiguity about the large-index part of the cited
paper.

## 3. Reducing factoring to the carry

Assume an oracle returns

\[
H=h\bmod2^n.
\tag{24}
\]

Compute \(C_n=C\bmod2^n\) by Theorem 1, and set

\[
Q_0=
\left(1+HN-(-1)^BC_n\right)\bmod2^n.
\tag{25}
\]

Equation (4) shows that \(Q_0\equiv q\pmod{2^n}\). Moreover,

\[
0<q<N<N+1\le2^n.
\tag{26}
\]

Hence the canonical residue in (25) is the exact integer \(q\). Division
verifies \(1<q<N\) and \(q\mid N\) in polynomial additional bit time. One
oracle call and polynomial work factor \(N\).

## 4. Reducing the carry to factoring

Conversely, suppose a factoring oracle returns the larger factor \(q\).
Compute \(C_n\) by Theorem 1. Since \(N\) is odd, it has an inverse modulo
\(2^n\). Reducing

\[
hN=q-1+(-1)^BC
\tag{27}
\]

modulo \(2^n\) gives

\[
h\equiv
N^{-1}\left(q-1+(-1)^BC_n\right)
\pmod{2^n}.
\tag{28}
\]

The inverse and all remaining arithmetic have polynomial bit cost. This is
the reverse one-query reduction and proves Theorem 2. It also proves the
same equivalence for the joint pair (9), because adjoining or deleting a
polynomial-time computable first coordinate changes neither reduction.

## 5. Signed Euclidean quotient and mixed modulus

The definition of \(h\) gives

\[
A=Nh+1-q=N(h-1)+(N+1-q).
\tag{29}
\]

The inequalities \(1<q<N\) imply

\[
0<N+1-q<N.
\tag{30}
\]

Thus (29) is the Euclidean division of \(A\) by \(N\), including when
\(B\) is odd and \(A<0\). This proves (11); no truncation-toward-zero
quotient convention is being used.

Let \(a_t\) be as in (12). There is an integer \(k\) such that

\[
A=a_t+kN2^t.
\tag{31}
\]

Dividing by positive \(N\) and taking floors gives

\[
\left\lfloor\frac AN\right\rfloor
=\left\lfloor\frac{a_t}{N}\right\rfloor+k2^t.
\tag{32}
\]

Combine (11) and (32) to obtain (13). Reducing (31) modulo \(N\) and using
(11) gives

\[
a_t\bmod N=N+1-q,
\tag{33}
\]

which proves (14).

For the reverse direction, a known \(q\), together with the polynomial-time
value \(C_n\), supplies

\[
A\equiv1-q\pmod N,
\qquad
A\equiv(-1)^BC_n\pmod{2^n}.
\tag{34}
\]

Because \(N\) is odd, the Chinese remainder theorem reconstructs the unique
\(A\bmod(N2^n)\) in polynomial bit time. Therefore the mixed-modulus
residue and factoring are polynomial-time interreducible. This proves
Theorem 3.

## 6. What the result does and does not block

The ordinary power-of-two residue in Theorem 1 is a genuine positive
algorithm. Kummer's carry count can also supply the public valuation
\(v_2(C)\), but the valuation is not needed for the reduction after
Andreica's full residue is available.

An odd-factorial or \(2\)-adic-gamma representation is not by itself an
algorithm for (24). Such formulas become relevant only if they also compute
the signed quotient digit in (13). Theorem 2 then converts that evaluator
into a factoring algorithm. Likewise, an explicit product tree for \(C\)
has \(B\) leaves, but this is only a barrier for that explicit
representation; Andreica's modular compression shows why it is not a
general lower bound.

Finally, exact materialization is intrinsically too large in the sequential
bit model. For \(1\le j\le B\),

\[
\frac{N-j}{j}\ge\frac{N-B}{B}\ge B-1,
\tag{35}
\]

because \(B^2\le N\). Hence

\[
C\ge(B-1)^B.
\tag{36}
\]

Here \(B=2^{\Theta(n)}\), so the exact output has \(2^{\Theta(n)}\) bits.
This output-size observation rules out algorithms that materialize \(C\) or
\(A\). It does not rule out a succinct modular algorithm for (24), and F196
claims no unconditional factoring lower bound.
