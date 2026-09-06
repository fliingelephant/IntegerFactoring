# F177 candidate — one exact common order lifts to a square-modulus terminal screen

## Status and scope

This is a proof-only positive theorem for balanced squarefree semiprimes. It
improves the terminal threshold for one exact ordinary or one oriented
quadratic-torus common order. It is not an all-input source theorem and is
not a factoring algorithm by itself.

Let

\[
N=pq,
\qquad p<q<2p,
\qquad
n=\lceil\log_2(N+1)\rceil,
\tag{1}
\]

where \(p,q\) are distinct odd primes.

## 1. Ordinary common-order lift

Suppose a public certified ordinary state has exact order \(M\) modulo both
hidden primes. Then

\[
M\mid p-1,
\qquad
M\mid q-1,
\tag{2}
\]

and therefore

\[
\boxed{p+q\equiv N+1\pmod{M^2}.}
\tag{3}
\]

The true sum lies in the public interval

\[
2\sqrt N<p+q<\frac{3}{\sqrt2}\sqrt N.
\tag{4}
\]

Enumerate the integers \(S\) in (4) that satisfy

\[
S\equiv N+1\pmod{M^2}.
\tag{5}
\]

For each one, test whether

\[
\Delta=S^2-4N
\tag{6}
\]

is a square and whether \(S\pm\sqrt\Delta\) are even. The true sum occurs
in the list and gives

\[
p=\frac{S-\sqrt\Delta}{2},
\qquad
q=\frac{S+\sqrt\Delta}{2}.
\tag{7}
\]

The number of candidates is at most

\[
1+\left(\frac{3}{\sqrt2}-2\right)\frac{\sqrt N}{M^2}.
\tag{8}
\]

Consequently, for any fixed quasipolynomial numerical bound \(Q(n)\), the
factorization is deterministic QP whenever

\[
\boxed{
M^2\ge
\left(\frac{3}{\sqrt2}-2\right)\frac{\sqrt N}{Q(n)}.
}
\tag{9}
\]

Up to the fixed balanced-interval constant, the individual common-order
threshold is

\[
M\ge \frac{N^{1/4}}{\sqrt{Q(n)}}.
\tag{10}
\]

## 2. Oriented torus common-order lift

Fix \(\epsilon\in\{+1,-1\}\). Suppose a certified common order \(B\)
divides the two local norm-one group orders

\[
B\mid p-\epsilon,
\qquad
B\mid q+\epsilon.
\tag{11}
\]

Put \(D=q-p\). Then

\[
(p-\epsilon)(q+\epsilon)
=N-1-\epsilon D,
\]

so

\[
\boxed{D\equiv\epsilon(N-1)\pmod{B^2}.}
\tag{12}
\]

Balance gives

\[
0<D<\frac{1}{\sqrt2}\sqrt N.
\tag{13}
\]

Enumerate the integers \(D\) in (13) satisfying (12). For each candidate,
test whether

\[
S^2=D^2+4N
\tag{14}
\]

is an integer square and use (7). The list has at most

\[
1+\frac{\sqrt N}{\sqrt2 B^2}
\tag{15}
\]

candidates. Hence this oriented torus channel is deterministic QP whenever

\[
\boxed{B^2\ge\frac{\sqrt N}{\sqrt2 Q(n)}.}
\tag{16}
\]

## 3. Complexity

The residue classes modulo \(M^2\) or \(B^2\), integer square roots, parity
tests, and trial divisions in (7) have bit complexity polynomial in \(n\)
per candidate. Thus a QP candidate bound gives deterministic QP total bit
cost. No hidden factor, hidden orientation, or unfactored group order is
used by the scan.

## 4. Exact boundary

F177 improves the terminal use of one already certified common order. It
does not provide that order. In particular, it does not contradict the F172
and F173 families, where every available ordinary and quadratic-torus common
order is bounded by an absolute constant.

F177 does not prove any of the following.

- A QP source reaches the threshold (9) or (16) on every input.
- A local-capacity certificate can replace an exact common order.
- The orientation in (11) is available without a certified torus state.
- The theorem handles unbalanced semiprimes, repeated prime factors, or more
  than two distinct prime factors without a separate reduction.
- Integer factoring is in deterministic or Las Vegas QP time.
