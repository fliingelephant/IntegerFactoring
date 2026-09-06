# F213 hostile audit

## Verdict

**PASS.** All frozen hashes match. I found no false quantified claim,
construction failure, parity-kernel gap, root-image error, size-bound
failure, or recursion overclaim. The theorem is valid as an existential
obstruction for the declared rational-prime valuation-parity method.

There is one harmless precision note. For an odd sign-free subset, the
normalized root of \(-1\) is

\[
s^k=(-1)^{(k-1)/2}s,
\]

so it is \(s\) or \(-s\), rather than always literally \(s\). Both signs
are public and both give trivial gcds. This does not affect any displayed
kernel theorem or the obstruction.

I did not edit a frozen input or a durable ledger. I ran no mathematical
search or experiment.

## 1. Frozen-input integrity

I read MANIFEST.md first. Before opening the mathematical packet, I
recomputed the four declared SHA-256 hashes. Every value matched:

- STATEMENT.md:
  9e74427637283e893c5a91bc5d0d24d7a4040526dbe5cf2e1599971474081fff;
- PROOF.md:
  ac83b7fa190b16226b69d7f2604fe6a0aa684e8594251dbe702aa5f780a43b35;
- SELF_AUDIT.md:
  a600e744634740f39839a982bc76ee5ea4e9de7c049b3cf5c6f023fc23e37bfd;
- PROVENANCE.md:
  da8e68c689eba36ba3c2e7348c3f13e510582e77694eec8f976dd0750cb9ce37.

The manifest does not declare a self-hash. Its observed SHA-256 is

9c5705bae3416c9f677355b4e4e4664d498a6faa96efce4f5c760e02cf1ccf8d.

## 2. Existence of the odd composite CRT family

Fix \(M\geq2\) and define

\[
R=\operatorname{rad}\left(\prod_{a=1}^M a(a^2+1)\right).
\]

The \(a=1\) factor contains \(2\), so \(R\) is even. Hence \(R^2+1>1\)
is odd and has an odd prime divisor \(d\). Also \(d\nmid R\), and

\[
R^2\equiv-1\pmod d.
\]

Thus \(-1\) is a quadratic residue modulo the odd prime \(d\), which forces

\[
d\equiv1\pmod4.
\]

The construction sets

\[
H=\max\{R^2+1,M(M^2+1)\}.
\]

Bertrand gives

\[
H<\ell_1<2H.
\]

Applying Bertrand successively to \(2\ell_a\) gives

\[
2\ell_a<\ell_{a+1}<4\ell_a.
\tag{A1}
\]

Therefore the \(\ell_a\)'s are distinct and each satisfies

\[
\ell_a>H\geq R^2+1\geq d.
\tag{A2}
\]

Every prime factor of \(R\) is at most \(R<R^2+1<\ell_a\). Consequently

\[
R,\quad d^2,\quad \ell_1^2,\ldots,\ell_M^2
\]

are pairwise coprime. No prime-density assertion beyond Bertrand is hidden
here.

For

\[
g_a(U)=2aU+1-a^2,
\]

the coefficient \(2a\) is a unit modulo \(\ell_a\), because
\(\ell_a>H\geq M(M^2+1)>2a\). The polynomial has one root class modulo
\(\ell_a\). Every one of its \(\ell_a\) lifts modulo \(\ell_a^2\) remains a
root modulo \(\ell_a\), while exactly one is a root modulo
\(\ell_a^2\). Any other lift \(u_a\) therefore satisfies

\[
v_{\ell_a}(g_a(u_a))=1.
\tag{A3}
\]

For the compositeness prime, \(R\bmod d\) is a simple root of
\(U^2+1\), since \(d\nmid2R\). Exactly one of its \(d\) lifts is a root
modulo \(d^2\). A different lift \(v\) satisfies

\[
v_d(v^2+1)=1.
\tag{A4}
\]

CRT now supplies a residue modulo

\[
\mathcal L=Rd^2\prod_{a=1}^M\ell_a^2
\]

that is zero modulo \(R\), equal to \(v\) modulo \(d^2\), and equal to
\(u_a\) modulo each \(\ell_a^2\). If \(x_0\) is its least nonnegative
representative and

\[
s=x_0+\mathcal L,
\]

then

\[
\mathcal L\leq s<2\mathcal L.
\tag{A5}
\]

Both \(x_0\) and \(\mathcal L\) are even because \(R\) is even, so \(s\) is
even and \(N=s^2+1\) is odd. Congruence (A4) is preserved modulo \(d^2\),
and hence

\[
d\parallel N.
\tag{A6}
\]

Moreover,

\[
1<d<\mathcal L\leq s<s^2+1=N.
\]

Thus \(d\) is a proper divisor and \(N\) is composite. Finally,
\(\mathcal L>\ell_1>H>M\), so \(s>M\). This proves the required
\(\forall M\geq2\ \exists s,N,\ell_1,\ldots,\ell_M\) quantifier without
assuming semiprimality, balance, squarefreeness, or efficient generation.

## 3. Floor root and exact norm identities

For \(N=s^2+1\),

\[
\sqrt N-s=\frac1{\sqrt N+s}.
\]

For every \(1\leq a\leq M<s\),

\[
0<a(\sqrt N-s)=\frac a{\sqrt N+s}<1.
\]

Therefore there is no carry:

\[
r_a=\lfloor a\sqrt N\rfloor=as.
\tag{A7}
\]

Direct substitution gives

\[
E_a=a^2(s^2+1)-a^2s^2=a^2
\tag{A8}
\]

and

\[
F_a=(as+1)^2-a^2(s^2+1)=2as+1-a^2.
\tag{A9}
\]

The size claims are strict. Since \(a<s\),

\[
0<a^2<N,
\]

and

\[
F_a=a(2s-a)+1>0.
\]

Also

\[
N-F_a=(s-a)^2>0.
\tag{A10}
\]

Thus every displayed child is a positive integer strictly below \(N\).

## 4. Direct gcd screening

If a prime \(h\) divided both \(a\) and \(N\), then \(h\mid R\) and the
CRT congruence \(s\equiv0\pmod R\) would give

\[
N=s^2+1\equiv1\pmod h,
\]

a contradiction. Hence

\[
\gcd(a,N)=1.
\tag{A11}
\]

Since \(\gcd(s,s^2+1)=1\), (A7) and (A11) imply

\[
\gcd(r_a,N)=1.
\tag{A12}
\]

Suppose a prime \(h\) divided \(as+1=r_a+1\) and \(N\). It cannot divide
\(a\). From

\[
as\equiv-1,\qquad s^2\equiv-1\pmod h
\]

one gets

\[
a^2\equiv-1\pmod h.
\]

Thus \(h\mid a^2+1\), so \(h\mid R\). The CRT congruence again gives
\(N\equiv1\pmod h\), a contradiction. Therefore

\[
\gcd(r_a+1,N)=1.
\tag{A13}
\]

If \(h\mid F_a,N\), then the exact relation

\[
(as+1)^2-F_a=a^2N
\]

forces \(h\mid as+1\), contradicting (A13). Hence

\[
\gcd(F_a,N)=1.
\tag{A14}
\]

Finally, \(E_a=a^2\) and (A11) give

\[
\gcd(E_a,N)=1.
\tag{A15}
\]

All bases and normalization denominators are therefore units. In
particular, the private factors inserted into the \(F_a\)'s cannot also be
factors of \(N\).

## 5. Private prime rows and pairwise exclusion

The congruence \(s\equiv u_a\pmod{\ell_a^2}\), together with (A3) and
(A9), gives

\[
v_{\ell_a}(F_a)=1.
\tag{A16}
\]

For distinct \(a,b\), expansion verifies the exact cross identity

\[
\begin{aligned}
bF_a-aF_b
&=b(2as+1-a^2)-a(2bs+1-b^2)\\
&=(b-a)(1+ab).
\end{aligned}
\tag{A17}
\]

The right side is nonzero and obeys the strict bound

\[
|(b-a)(1+ab)|
<M(M^2+1)
<\ell_a.
\tag{A18}
\]

Indeed, \(|b-a|<M\) and \(1+ab<M^2+1\).

If \(\ell_a\mid F_b\), then (A16) and (A17) would make
\(\ell_a\) divide the nonzero integer in (A18), which is impossible.
Thus

\[
\ell_a\nmid F_b\qquad(b\ne a).
\tag{A19}
\]

Also \(\ell_a>M\geq b\), so

\[
\ell_a\nmid E_b=b^2
\]

for every \(b\), including \(b=a\). Hence the valuation-parity row for
\(\ell_a\) has a one in exactly the \(F_a\) column. The proof establishes
prime-power valuation one, not merely support.

## 6. Full sign-and-prime parity kernel

Every prime valuation of

\[
E_a=a^2
\]

is even. Since the corresponding signed column is \(-E_a\), its vector is
exactly the sign-row unit vector.

Consider any binary dependency among all \(2M\) columns. For each \(a\),
the private \(\ell_a\)-row from Section 5 contains a one only in the
\(F_a\) column. Its parity equation forces the coefficient of \(F_a\) to
zero. This excludes every adjacent-norm column independently; no
combination of other rows can cancel a private pivot.

The remaining selected columns are copies of the sign vector. Their sum is
zero exactly when an even number are selected. Conversely, every even
subset of the \(E_a\)'s has even sign parity and even valuation at every
rational prime. Thus the complete kernel, rather than only a contained
subspace, is

\[
\{(x_1,0,\ldots,x_M,0):
x_1+\cdots+x_M=0\text{ in }\mathbb F_2\}.
\tag{A20}
\]

If the \(F_a\) columns are omitted, the same sign-row argument gives the
same even-subset kernel on the \(E_a\)'s.

## 7. Root image and the two gcds

Let \(S\) be an even subset, \(k=|S|\), and put

\[
X=\prod_{a\in S}r_a,\qquad
Y=\prod_{a\in S}a.
\]

Equation (A11) makes \(Y\) a unit modulo \(N\). The product of the
relations \(r_a^2\equiv-a^2\pmod N\) gives

\[
X^2\equiv(-1)^kY^2=Y^2\pmod N.
\]

Using \(r_a=as\),

\[
XY^{-1}\equiv s^k
=(s^2)^{k/2}
\equiv(-1)^{k/2}\in\{1,-1\}\pmod N.
\tag{A21}
\]

Therefore every dependency gives only a global root of one.

If the normalized root is \(1\), then

\[
\gcd(X-Y,N)=N,
\]

while

\[
\gcd(X+Y,N)=\gcd(2Y,N)=1
\]

because \(N\) is odd and \(Y\) is a unit. For normalized root \(-1\), the
two results swap. Thus the standard gcd pair is exactly \(\{1,N\}\), even
for the empty dependency.

If an implementation discards the sign row and accepts an odd subset, then

\[
XY^{-1}\equiv s^k
=(-1)^{(k-1)/2}s\in\{s,-s\}\pmod N.
\tag{A22}
\]

This is a public root of \(-1\), not a second root of \(1\). Both signs are
useless for the standard gcd attempt because

\[
\gcd(s-1,N)=\gcd(s+1,N)=1.
\tag{A23}
\]

Any common divisor in (A23) divides \(2\), and \(N\) is odd. Equation
(A22) is the precise version of the packet's informal phrase “obtains the
already public root \(s\).”

## 8. Repeated-Bertrand bit bounds

The radical is bounded by the product defining it:

\[
R\leq\prod_{a=1}^M a(a^2+1)
\leq(2M^3)^M.
\]

Hence

\[
\log R=O(M\log(M+1)).
\tag{A24}
\]

Since \(d\leq R^2+1\), and
\[
H=\max\{R^2+1,M(M^2+1)\},
\]

we also have

\[
\log d,\log H=O(M\log(M+1)).
\tag{A25}
\]

From the upper half of (A1),

\[
\ell_a<2H\,4^{a-1}.
\]

Therefore

\[
\begin{aligned}
\sum_{a=1}^M\log_2\ell_a
&<M\log_2(2H)+2\sum_{a=1}^M(a-1)\\
&=O(M^2\log(M+1)).
\end{aligned}
\tag{A26}
\]

Conversely, the lower half of (A1) gives

\[
\ell_a>2^{a-1}\ell_1,
\]

so

\[
\sum_{a=1}^M\log_2\ell_a
>\sum_{a=1}^M(a-1)
=\Omega(M^2).
\tag{A27}
\]

Since

\[
\log\mathcal L
=\log R+2\log d+2\sum_a\log\ell_a,
\]

equations (A24)--(A27) give

\[
\Omega(M^2)\leq\log\mathcal L
\leq O(M^2\log(M+1)).
\tag{A28}
\]

Equation (A5) gives \(\log s=\log\mathcal L+O(1)\), and
\(N=s^2+1\) gives

\[
n=\lceil\log_2(N+1)\rceil
=2\log_2s+O(1).
\]

Thus

\[
\Omega(M^2)\leq n\leq O(M^2\log(M+1)).
\tag{A29}
\]

Taking logarithms of (A29) yields

\[
2\log M+O(1)
\leq\log n
\leq2\log M+\log\log(M+1)+O(1).
\]

Therefore

\[
\log M=\left(\frac12+o(1)\right)\log n,
\qquad
M=n^{1/2+o(1)}.
\tag{A30}
\]

The bank has \(2M\) columns and is polynomial-sized. The derivation uses
only the repeated doubling and quadrupling bounds from Bertrand; no
short-interval prime count is present.

## 9. Public subbank

The upper bound in (A29) gives

\[
n^{1/3}
\leq O\!\left(
M^{2/3}(\log(M+1))^{1/3}
\right)
<M
\tag{A31}
\]

for all sufficiently large \(M\). Hence the schedule

\[
1\leq a\leq\lfloor n^{1/3}\rfloor
\]

is contained in the constructed bank and depends only on the public bit
length.

Restricting to this initial subbank preserves each selected \(F_a\)'s
private row because the original exclusion theorem was proved against all
indices \(1\leq b\leq M\). All selected \(E_a\)'s remain copies of the
sign vector, and the root calculation is unchanged. Therefore the public
subbank inherits the exact kernel and global-root obstruction. This claim
does not extend the private-row theorem to any index greater than \(M\).

## 10. Child bit lengths and recursive accounting

The square children satisfy

\[
\operatorname{bits}(E_a)=O(\log M)=o(n)
\]

uniformly.

The adjacent norms are strictly increasing in \(a\), because

\[
F_{a+1}-F_a=2s-(2a+1)>0
\]

for \(a<M<s\). In particular,

\[
s<F_a\leq2Ms+1.
\]

It follows that

\[
\operatorname{bits}(F_a)
=\log_2s+O(\log M)
=\frac n2+O(\log M)
=\left(\frac12+o(1)\right)n
\tag{A32}
\]

uniformly for \(1\leq a\leq M\). The lower bound in (A29) makes
\(\log M=o(n)\).

Consequently there is a fixed \(\rho<1\), for example \(\rho=2/3\), such
that every nontrivial child has at most \(\rho n\) bits for all sufficiently
large constructed inputs. Equation (A29) also gives \(M=O(\sqrt n)\), so
there are polynomially many children.

Independently of the imported P183 label, the stated recurrence form is
numerical-QP safe. If \(Q(n)\) is numerical QP, then

\[
T(n)\leq T(n-1)+Q(n)T(\rho n)+Q(n)
\tag{A33}
\]

can be unrolled along the decrement spine to

\[
T(n)\leq nQ(n)(T(\rho n)+1).
\]

Iterating through \(O(\log n)\) fixed-ratio levels multiplies
numerical-QP factors only \(O(\log n)\) times. Its logarithm remains
\((\log n)^{O(1)}\), so \(T(n)\) is numerical QP. This covers a
polynomial or numerical-QP collection of fixed-ratio side calls and one
separate one-bit spine.

The accounting is expressly conditional on an already correct all-input
recursive factorization routine. The children need not inherit the
near-square promise. F213 supplies neither that routine nor a top-level
algorithm.

## 11. Scope audit

The construction proves an exact counterexample to one inference:
polynomially many fully factored smaller near-square norms, together with
positive parity nullity, need not yield a non-global parity root.

It does not prove any of the following:

1. that arbitrary inputs, semiprimes, or balanced semiprimes have this
   kernel;
2. that the constructed \(N\) is a semiprime;
3. that the existential CRT family is generated efficiently;
4. that factoring or otherwise processing the \(F_a\)'s cannot reveal
   useful information outside valuation parity;
5. that private rows persist for multipliers beyond \(M\);
6. that every possible QP schedule fails; or
7. that the conditional recursion supplies a factorization algorithm.

The packet states all of these limitations. I found no sentence that turns
the named parity obstruction into a general lower bound or a factoring
claim.
