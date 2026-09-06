# Proof of F168

## 1. QP arithmetic closure

Write

\[
\mathcal Q(n)=2^{(\log_2(n+1))^{O(1)}}.
\]

The product of any fixed number of \(\mathcal Q(n)\) bounds is again
\(\mathcal Q(n)\). The same is true after multiplication by a polynomial in
\(n\), or after raising a \(\mathcal Q(n)\) bound to a fixed power. Therefore
all finitely many caps in one algorithm can be dominated by one fixed QP
bound after increasing its constants.

Let \(B\le\mathcal Q(n)\). Since

\[
M_B=\operatorname{lcm}(1,\ldots,B)\le B!,
\]

one has

\[
\operatorname{bitlen}(M_B)=O(B\log B)=\mathcal Q(n).
\tag{1}
\]

There are at most \(B\) prime powers at most \(B\). Hence the bank

\[
\{M_B\}\cup
\{M_B/\ell^j:\ell\le B\text{ prime},\ 1\le j\le\lfloor\log_\ell B\rfloor\}
\tag{2}
\]

has at most \(B+1\) members. A sieve through \(B\), incremental lcm
construction, exact division, and storage of all bank members use a fixed
polynomial in \(B\), \(\log B\), and \(n\). By (1), this is QP bit
complexity and space. Binary modular exponentiation is polynomial in \(n\)
and the exponent bit length, so all bank powers are QP too.

Let a subgroup be supplied by \(s\le\mathcal Q(n)\) residue generators, with
total explicit encoding length at most \(\mathcal Q(n)\). Breadth-first
closure through a cap \(T\le\mathcal Q(n)\) performs at most
\((T+1)s\) generator multiplications. A deterministic balanced search tree
can handle residue equality in \(\mathcal Q(n)\) time; even pairwise lookup
adds only another factor \(T\). Thus capped enumeration, gcd testing, and
storage remain QP.

For scans based on \(N-1\), no full factorization of \(N-1\) is needed.
Sieve the candidate primes only through the public QP bound, test
divisibility, and divide repeatedly to obtain the valuation. There are at
most \(n\) puncture depths per prime. Every puncture of \(N-1\) has \(O(n)\)
bits. Hence a QP prime scan, QP generator list, and QP image cap still give
QP total work.

Finally, suppose every randomized trial has work at most \(W(n)\) on every
transcript, returns only a verified factor or failure, and succeeds with
probability at least \(1/R(n)\) on a promised transcript, where \(W,R\) are
QP. Independent trials stop almost surely, their expected count is at most
\(R(n)\), and their expected work is at most \(W(n)R(n)=\mathcal Q(n)\).
This proves Part I.

## 2. P87 and P92–P96

The mathematical proofs of P87 and P92–P96 do not use that their caps are
polynomial. They use only the exact inequalities displayed in their
statements and a complete public scan through those caps.

For P87, \(\sigma(r)\le B\) is equivalent to \(r\mid M_B\). If exactly one
local order divides \(M_B\), the unpunctured exponent separates it. If both
divide \(M_B\) but differ, deleting the correct power of a prime at which
their valuations differ separates them. Section 1 proves that the complete
bank is executable in deterministic QP time for QP \(B\).

P92 and P93 raise every public generator by every bank exponent and stop a
wrong subgroup enumeration at its declared cap. Their useful images have at
most \(B^2\) elements. With \(B\), the generator count, and the total
encoding all QP, Section 1 makes the complete deterministic scan QP.

P94 and P96 scan primes only through \(L\), at most \(n\) public puncture
depths per prime, and at most \(S\) or \(T\) subgroup elements per trial.
Section 1 shows that QP choices of \(L,S,T\) give deterministic QP work. The
promises remain the full image-size inequalities

\[
\ell^{H_\ell-C_\ell+2}\le S
\quad\text{and}\quad
\ell^{2(H-C+1)}\le T,
\]

not merely small valuation gaps.

For P95, deterministic enumeration through \(T\) remains QP when
\(1<AB\le T\). For sampling, choose the P83 exponent range so that its
total-variation error is at most \(1/(2Q(n))\). Its exponent bit length is
\(O(n+\log s+\log Q(n))\), and is therefore polynomial in \(n\) plus
polylogarithmic terms. If \(\min(A,B)\le Q(n)\), the uniform separator
density is at least \(1/Q(n)\), apart from the easier case in which one
order is one. The approximate sampler therefore succeeds with probability
at least \(1/(2Q(n))\). Section 1 gives expected QP work.

This proves the P87 and P92–P96 entries in Part II.

## 3. P97, the bare-N promise, and P99

Let \(N=pq\) for distinct odd primes and define

\[
g=\gcd(p-1,q-1),
\qquad
A=(p-1)/g,
\qquad
B=(q-1)/g.
\]

P97 proves that the \((N-1)\)-power image is

\[
S_N\cong C_A\times C_B,
\qquad
\gcd(A,B)=1,
\qquad
AB>1,
\tag{3}
\]

and that a unit sampled uniformly modulo \(N\), raised to \(N-1\), is
exactly uniform in \(S_N\). Its positive-separator density is

\[
\delta_N
=\frac1A+\frac1B-\frac2{AB}.
\tag{4}
\]

Let \(m=\min(A,B)\) and \(M=\max(A,B)\). If \(m\ge2\), then

\[
\delta_N
=\frac1m+\frac{m-2}{mM}
\ge\frac1m.
\tag{5}
\]

If \(m=1\), then \(M\ge2\) and

\[
\delta_N=1-1/M\ge1/2.
\tag{6}
\]

A raw sample from \(1,\ldots,N-1\) is a unit with probability greater than
one half. A nonunit already gives a proper factor. Thus, when
\(m\le Q(n)\), one raw trial followed by the \((N-1)\)-power gcd succeeds
with probability at least \(1/(2Q(n))\), after enlarging \(Q\) so that
\(Q\ge2\). Every returned divisor is verified. Independent repetition is
Las Vegas, has expected at most \(2Q(n)\) trials, and uses expected QP bit
complexity. This proves Part III.

P97 also proves that two accepted powered units generate all of \(S_N\) with
probability at least \(6/\pi^2\). Therefore a QP-bounded localizer that has
inverse-QP verified success on every generating pair gives a verified
success probability that is inverse QP per fresh batch. The localizer must
be QP-bounded on non-generating pairs because the generation event is not
publicly recognized. Section 1 gives the stated Las Vegas reduction.

P99 supplies, with an absolute constant probability, either a factor or a
list generating the full unit group of every \(N\). The same bounded-work
argument converts an inverse-QP full-group localizer into an expected-QP
splitter for every composite. After a verified proper split, recurse on the
two factors and use deterministic primality testing to stop. A complete
factorization tree has at most \(n-1\) internal split nodes. Every child has
bit length at most \(n\), so the total expected work is at most a polynomial
factor \(n\) times one QP bound. This remains QP and proves the P99 entry.

## 4. Construction of the length-linked stable family

We use two standard unconditional results.

1. **Bertrand.** For every integer \(x>1\), there is a prime strictly
   between \(x\) and \(2x\).
2. **Linnik.** There are absolute constants \(C_0,L>0\) such that, for every
   coprime residue class \(a\bmod m\), the least prime in that class is at
   most \(C_0m^L\).

Choose an arbitrarily large odd prime \(r\). The residue

\[
a_r=1+2r\pmod{4r}
\]

is reduced because \(\gcd(1+2r,4r)=1\). Linnik gives a prime \(p\) in this
class with

\[
2r<p\le C_0(4r)^L.
\tag{7}
\]

The lower bound holds because \(1+2r\) is the least positive integer in the
class. Also \(p\equiv3\pmod4\). Put

\[
A=(p-1)/2.
\]

Then \(A\) is odd and \(r\mid A\).

By Bertrand, choose a prime \(s\) with

\[
p<s<2p.
\tag{8}
\]

Let \(R=\operatorname{rad}(A)\), the product of the distinct prime divisors
of \(A\). Since \(A\) is odd, \(R\) is odd. Since \(s>p>A\), one has
\(\gcd(s,R)=1\).

Use CRT to choose the unique residue class modulo

\[
m=4sR
\]

that satisfies

\[
q\equiv1+2s\pmod{4s},
\qquad
q\equiv2\pmod R.
\tag{9}
\]

This class is reduced: \(1+2s\) is coprime to \(4s\), the residue 2 is
coprime to the odd integer \(R\), and \(\gcd(4s,R)=1\). Linnik therefore
gives a prime \(q\) in the class with

\[
q\le C_0(4sR)^L<C_0(8p^2)^L.
\tag{10}
\]

The lower bound \(q>p\) is also public in the construction. Every positive
integer in the first congruence of (9) is at least its least positive
representative

\[
1+2s>p.
\tag{11}
\]

Thus the canonical positive representative of the CRT class, and hence the
prime \(q\) supplied by Linnik, is strictly larger than \(p\).

The first congruence in (9) also gives \(q\equiv3\pmod4\). Put

\[
B=(q-1)/2.
\]

Then \(B\) is odd and \(s\mid B\). For every prime \(t\mid A\), the second
congruence in (9) gives

\[
2B=q-1\equiv1\pmod t.
\]

As \(t\) is odd, this implies \(t\nmid B\). Therefore

\[
\gcd(A,B)=1.
\tag{12}
\]

Since \(p-1=2A\), \(q-1=2B\), and \(A,B\) are odd and coprime,

\[
\gcd(p-1,q-1)=2.
\tag{13}
\]

Let \(N=pq\) and \(E=N-1\). The P98 identity with \(g=2\) is

\[
E/2=2AB+A+B.
\tag{14}
\]

Modulo \(A\), the right side is \(B\); modulo \(B\), it is \(A\).
Equation (12) gives

\[
\gcd(A,E/2)=\gcd(B,E/2)=1.
\]

Both \(A\) and \(B\) are odd, so

\[
\boxed{\gcd(AB,E)=1.}
\tag{15}
\]

This proves immediate P98 stability.

It remains to link the large primes to the input length. Equations (7),
(8), and (10) give fixed constants \(C_1,D>0\) such that

\[
2r<p<q,
\qquad
N=pq\le C_1r^D.
\tag{16}
\]

The lower inequalities also give \(N>4r^2\). Hence

\[
n=\lceil\log_2(N+1)\rceil=\Theta(\log r).
\tag{17}
\]

After decreasing one absolute constant \(c>0\) and discarding finitely many
initial choices of \(r\), (17) gives

\[
r\ge2^{cn}.
\]

Since \(s>p>r\), the same bound holds for \(s\). Because \(r\mid A\) and
\(s\mid B\),

\[
\sigma(A)\ge r\ge2^{cn},
\qquad
\sigma(B)\ge s\ge2^{cn}.
\tag{18}
\]

Every fixed QP function is eventually smaller than \(2^{cn}\). Also
\(A\ge r\) and \(B\ge s\), so (4) gives

\[
0<\delta_N
\le\frac1r+\frac1s
=2^{-\Omega(n)}.
\tag{19}
\]

A QP number of exact uniform samples therefore has total success
\(2^{-\Omega(n)}\) by the union bound. Equation (15) makes every
\((N-1)\)-smooth power an automorphism of the P97 rectangle, as in P98.

This family only defeats the existing density guarantee and the displayed
bounded-prime-component hypotheses. It does not prove that a capped
enumeration cannot encounter a separator early, and it does not constrain
adaptive value-dependent words, integer presentations, or relation
decoders. This completes Part IV and the proof.
