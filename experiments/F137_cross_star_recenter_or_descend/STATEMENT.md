# F137 statement — cross-star recenter-or-descend law

## Status and material change

This is a proof-only candidate. It is not a closure theorem, a complete-source
obstruction, or an integer-factoring algorithm.

The closest prior boundaries are X73/P120, X74/P122, and X64/P80. P120 shows
that unary feedback can be new without reusing a fed row, or can reuse a row
without closing it. P122 controls overlaps only inside one anchored star.
P80 closes scans in which both the old and target carries are bounded.

P70/P80 already give the divisor-carry remainder law. The material change
here is narrower: one canonically generated arm is followed through a
released small block into its next canonically generated star. The parent
recenters as one virtual child digit, or the released block strictly
decreases. Two consecutive decrease steps have a quantitative contraction.

## Setup

Let

\[
N\ge3,
\qquad
n=\lceil\log_2(N+1)\rceil.
\]

Let \(C\ge2\) be an integer, and let

\[
1<q<\frac NC,
\qquad
\gcd(q,N)=1,
\qquad
w=\iota_N(q),
\qquad
qw=1+kN.
\tag{1}
\]

Choose an eligible parent anchor \(\ell\) and its induced digit \(A\):

\[
2\le\ell\le C,
\qquad
\gcd(\ell,Nq)=1,
\qquad
0\le A<\ell,
\qquad
w+NA\equiv0\pmod\ell.
\]

Put \(H=w+NA\). Then \((\ell q,H/\ell)\) is a canonical endpoint
presentation of \(V=qH\). Suppose complete endpoint refinement names a unit
block \(r\mid H\) such that

\[
H=Sr,
\qquad
1<r<\frac NC,
\qquad
S\ge1.
\tag{2}
\]

Put

\[
V=qSr=1+KN,
\qquad
K=k+Aq.
\tag{3}
\]

Write the exact Euclidean division

\[
qS=jN+t,
\qquad
j\ge0,
\qquad
1\le t<N.
\tag{4}
\]

## Theorem 1 — divisor carry and exact recentering

The remainder in (4) is the canonical inverse of the released block:

\[
\boxed{t=\iota_N(r).}
\tag{5}
\]

If

\[
P_N(r)=rt=1+k_rN,
\]

then

\[
\boxed{
K=jr+k_r,
\qquad
k_r=K\bmod r,
\qquad
1\le k_r<r.
}
\tag{6}
\]

For any integer \(b\ge0\), define the formal cofactor in the next star by

\[
H'_b=t+bN.
\tag{7}
\]

The old complement is exactly the virtual digit-\(j\) cofactor:

\[
\boxed{qS=H'_j.}
\tag{8}
\]

For every \(b\ne j\),

\[
\boxed{
\gcd(qS,H'_b)
=\gcd(qS,b-j)
\le |b-j|.
}
\tag{9}
\]

Thus this is not only a congruence between modular words. It identifies the
old exact integer relation as one exact presentation in the coordinate
system of the next star.

For every eligible child anchor

\[
2\le a\le C,
\qquad
\gcd(a,Nr)=1,
\]

let \(b_a\in\{0,\ldots,a-1\}\) be the unique digit with

\[
t+b_aN\equiv0\pmod a.
\]

Then the actual child endpoints

\[
ar,
\qquad
\frac{H'_{b_a}}a
\]

both lie in \(\{1,\ldots,N-1\}\). Thus every such observed child digit is a
canonical source position. The formal digit \(j\) need not be observed by a
child anchor.

## Theorem 2 — the recenter-or-descend split

Consider the actually observed child digits \(b_a<C\).

1. If \(j<C\), then the parent relation is the virtual digit-\(j\) arm of
   the child star. If an actual child anchor has \(b_a=j\), its endpoints
   give the old exact value \(V\). Its direct endpoint screens must run
   before exact-value deduplication. For every genuinely different observed
   digit \(b_a\ne j\),

   \[
   \boxed{\gcd(qS,H'_{b_a})<C.}
   \tag{10}
   \]

   Therefore no prime larger than \(C\) in the old complement \(qS\) can
   reappear in a different observed child cofactor.

2. If \(j\ge C\), then

   \[
   \boxed{r<q.}
   \tag{11}
   \]

The first branch extends the one-star P122 obstruction through one adaptive
release. The second branch gives a genuine monotone block-size step.

## Theorem 3 — two consecutive descents contract quantitatively

Apply the same construction for two consecutive transitions

\[
(q_0,k_0)\longrightarrow(q_1,k_1)
\longrightarrow(q_2,k_2),
\]

using canonical anchors through \(C\), with every released next block below
\(N/C\). Let their Euclidean quotients be \(j_0,j_1\).
If

\[
j_0\ge C,
\qquad
j_1\ge C,
\]

then

\[
\boxed{
q_2<\frac{C}{C+1}q_0.
}
\tag{12}
\]

Consequently, a path made only of consecutive large-quotient transitions has
length \(O(C\log N)\). For \(C=n^3\), this is \(O(n^4)\).

This path bound does not bound the full branching transcript. Small-quotient
recenter steps can interrupt every descent pair.

## Exact certificate

Take

\[
N=143,
\qquad
q=28,
\qquad
w=46,
\qquad
k=9,
\qquad
C=5.
\]

For parent anchor \(\ell=3\), the induced digit is \(A=1\), and

\[
H=189=27\cdot7,
\qquad
K=37,
\]

and releasing \(r=7\) gives

\[
qS=28\cdot27=756=5N+41.
\]

Thus \(j=5\ge C\), \(t=41=\iota_N(7)\), and

\[
k_r=2=37\bmod7,
\qquad
7<28.
\]

For parent anchor \(\ell=5\), the induced digit is \(A=3\), and

\[
H=475=25\cdot19,
\qquad
K=93,
\]

and releasing \(r=19\) gives

\[
qS=28\cdot25=700=4N+128.
\]

Thus \(j=4<C\), \(t=128=\iota_N(19)\), and

\[
H'_4=128+4N=700.
\]

The virtual digit \(4\) returns the old exact value

\[
19\cdot700=13300=1+93N.
\]

It is actually observed by child anchor \(a=5\), with canonical endpoints
\((95,140)\). Its endpoint screens are null on this certificate.

## Exact remaining gate

One local cross-star overlap mechanism is now exact. On the no-factor branch,
a small quotient keeps every different observed large fresh row disjoint from
the parent complement. A large quotient pays block-size descent. The descent
law is only pathwise, and another old column or star can still close a row.

A complete proof still needs one of the following:

1. a bound on how often small-quotient recentering can interrupt descent;
2. a non-parent old column or a different star that cancels a fresh pivot;
3. a controlled multi-block operation that closes a cycle; or
4. a direct normalized-root law that bypasses parity closure.

Even a block-incidence cycle is insufficient by itself: the remaining
cofactor labels must also have even valuation parity, and the resulting root
must be non-global.
