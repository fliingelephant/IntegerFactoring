# F196: the beta-two coefficient is easy and its quotient carry is factoring-equivalent

Status: frozen literature-dependent proof-only candidate.

## Scope and notation

Let

\[
N=pq,
\qquad p<q<2p,
\]

where \(p\) and \(q\) are distinct odd primes. Define

\[
n=\left\lceil\log _2(N+1)\right\rceil,
\qquad B=\lfloor\sqrt N\rfloor,
\qquad C=\binom{N-1}{B},
\qquad A=(-1)^B C.
\tag{1}
\]

As in F194, the balanced-prime identity is

\[
A\equiv 1-q\pmod N.
\tag{2}
\]

It makes the signed quotient

\[
h=\frac{A-(1-q)}N
\tag{3}
\]

an integer and gives

\[
q=1+hN-A.
\tag{4}
\]

All complexity claims use the deterministic classical bit model. A polynomial
bound is, in particular, a numerical quasipolynomial bound.

## Theorem 1: the first residue is polynomial-time computable

There is a deterministic algorithm that, from \(N\), computes

\[
C_n=C\bmod 2^n
\tag{5}
\]

in time polynomial in \(n\).

The external premise is Andreica's 2013 algorithm for binomial coefficients
modulo powers of two. For modulus \(2^T\), it has preprocessing time

\[
O\!\left(T^3\mathsf M(T)+T^4\right)
\tag{6}
\]

and, after preprocessing, evaluates one \(\binom P Q\bmod 2^T\), for
\(0\le Q\le P\le 2^T-1\), in

\[
O\!\left(T^2\log T\,\mathsf M(T)\right),
\tag{7}
\]

where \(\mathsf M(T)\) is the bit cost of multiplying two \(T\)-bit
integers.

For (5), take \(T=n\), \(P=N-1\), and \(Q=B\). The main parameter range of
the published algorithm applies directly; no large-index extension is used.

## Theorem 2: the carry is exactly factoring-equivalent

On the stated promise, define the two function problems

\[
\mathcal F(N)=q,
\qquad
\mathcal H(N)=h\bmod 2^n,
\tag{8}
\]

where residues modulo \(2^n\) use their canonical representatives.
Then \(\mathcal F\) and \(\mathcal H\) are interreducible by deterministic
polynomial-time, one-query reductions.

In particular, a numerical-QP evaluator for \(h\bmod2^n\) exists if and only
if a numerical-QP factoring algorithm exists for this balanced-semiprime
promise. The joint residue problem

\[
\left(C\bmod2^n,\ h\bmod2^n\right)
\tag{9}
\]

has the same equivalence because its first coordinate is already in
deterministic polynomial time by Theorem 1.

## Theorem 3: exact signed base conversion

Use Euclidean division for signed \(A\):

\[
A=N\left\lfloor\frac AN\right\rfloor+(A\bmod N),
\qquad 0\le A\bmod N<N.
\tag{10}
\]

Then

\[
\left\lfloor\frac AN\right\rfloor=h-1,
\qquad
A\bmod N=N+1-q.
\tag{11}
\]

For any \(t\ge1\), let

\[
a_t=A\bmod (N2^t),
\qquad 0\le a_t<N2^t.
\tag{12}
\]

The low base-\(N\) quotient digit is

\[
h\equiv 1+\left\lfloor\frac{a_t}{N}\right\rfloor\pmod{2^t},
\tag{13}
\]

while the same mixed-modulus residue already exposes the factor:

\[
q=N+1-(a_t\bmod N).
\tag{14}
\]

Consequently, computing \(A\bmod(N2^n)\) is also polynomial-time
equivalent to factoring on the promise.

## Exact boundary

The positive result is integer-specific: reduction modulo a power of two
compresses the remote binomial coefficient in polynomial bit time. It does
not evaluate the mixed-modulus carry. A rewrite using odd factorials,
\(2\)-adic gamma values, Kummer carries, product trees, or exact base
conversion is an algorithm for the core gate only if it returns the residue
in (8), or equivalently the mixed residue in (12). By Theorems 2 and 3, such
an algorithm already factors the promised input.

This is a reduction, not a lower bound against a new factoring algorithm.
Materializing the exact integer \(C\) has exponential output length in
\(n\), but that output-size obstruction does not apply to a hypothetical
succinct modular evaluator.

