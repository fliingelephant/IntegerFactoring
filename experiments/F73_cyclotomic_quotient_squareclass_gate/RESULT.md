# F73 — quotient promotion has separate subgroup and square-class gates

## Status

Proof-only candidate. No research computation was used. This artifact has not
passed hostile audit or proof-blind reconstruction.

## 1. Setup

Let \(c\) be an odd prime and let

\[
N=c^2+c+1
\]

be composite with \(3\nmid N\). The seed inverse relation is

\[
A_0=c\cdot c^2=c^3=1+(c-1)N. \tag{1}
\]

The endpoint-only subgroup is

\[
H_0=\langle c\rangle=\{1,c,c^2\}\pmod N,
\]

because \(c\) has exact order three in every prime-power component of \(N\).
The sole old relation has rational square class \([c]\).

Since \(c>3\) and \(3\nmid N\), one has \(c\equiv2\pmod3\). Define

\[
b=\frac{c+1}{3}.
\]

## 2. Quotient promotion always expands the subgroup

The public quotient of (1) is

\[
g=c-1.
\]

Its canonical inverse is

\[
w=\frac{c^2-1}{3}=gb,
\]

and the promoted relation is

\[
A_1=gw=g^2b=1+\frac{c-2}{3}N. \tag{2}
\]

The state \(g\) is strictly outside \(H_0\). Indeed,

\[
1<g=c-1<c,
\]

while the canonical representatives of \(H_0\) are \(1,c,c^2\).
Complete gcd refinement of the new endpoints produces blocks whose product is
\(g\). Therefore the refined block-generated subgroup contains \(g\) and
strictly contains \(H_0\).

This subgroup expansion holds whether or not the new square-class column
closes.

## 3. Exact immediate-closure gate

Modulo rational squares,

\[
[A_0]=[c],
\qquad
[A_1]=[b]. \tag{3}
\]

Also

\[
\gcd(c,b)=1.
\]

Because \(c\) is prime, \([b]\ne[c]\): equality would make the positive
integer \(bc\) a rational square, hence an integer square, although its
\(c\)-adic valuation is one.

It follows that the two-column square-class matrix has this exact behavior:

- if \(b\) is an integer square, the new column is zero and adds one
  singleton dependency;
- if \(b\) is not an integer square, the two columns \([c]\) and \([b]\)
  are independent and no new dependency exists.

Thus

\[
\boxed{\text{the quotient-fed column closes immediately}
\iff \frac{c+1}{3}\text{ is an integer square}.} \tag{4}
\]

This is the complete \(2\)-saturation gate for the two displayed relation
values. Strict subgroup expansion alone does not imply closure.

## 4. A closing column is factor-bearing

Suppose \(b=s^2\). Then

\[
c=3s^2-1.
\]

Since \(c\) is odd, \(s\) is even. The exact positive root of (2) is

\[
R=gs=s(c-1).
\]

Put

\[
A=3s^2-3s+1,
\qquad
B=3s^2+3s+1.
\]

Then

\[
N=AB,
\qquad
\gcd(A,B)=1,
\]

and

\[
R-1=(s-1)B,
\qquad
R+1=(s+1)A.
\]

Moreover,

\[
\gcd(s-1,A)=\gcd(s+1,B)=1.
\]

Therefore the new singleton dependency has a non-global root and gives

\[
\boxed{\gcd(R-1,N)=B,\qquad\gcd(R+1,N)=A.} \tag{5}
\]

For \(c=11\), one has \(b=4\), \(N=133=7\cdot19\), and
\(R=20\).

## 5. Meaning and scope

The quotient causes two mathematically different state changes:

1. it always leaves the old endpoint subgroup;
2. it creates a decoder dependency only when its new square class cancels.

In this family, the cancellation is exactly the public metric condition that
\((c+1)/3\) is a square. When it occurs, the square root supplies the
orientation that the odd-order endpoint subgroup lacks.

The theorem covers only the seed (1) and the first promoted quotient. It gives
no frequency law for the square condition. Infinitely many primes of the form
\(3s^2-1\) are not proved here. It gives no general quotient sampler,
all-input success theorem, publication-level novelty claim, or unrestricted
factoring algorithm.
