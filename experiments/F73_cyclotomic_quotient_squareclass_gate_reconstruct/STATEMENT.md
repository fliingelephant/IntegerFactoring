# Proof-blind reconstruction target: separate subgroup and square-class gates

Read only this statement. Do not read any other F70--F73 artifact, audit,
reconstruction, theorem file, registry, progress note, or git history.
Reconstruct every proof independently. Report PASS only if all claims and
scope boundaries follow.

## Setup

Let \(c\) be an odd prime and let

\[
N=c^2+c+1
\]

be composite with \(3\nmid N\). Start from

\[
A_0=c^3=1+(c-1)N.
\]

Prove that \(c\) has exact order three in every prime-power component and that

\[
H_0=\langle c\rangle=\{1,c,c^2\}\pmod N.
\]

Show that \(c\equiv2\pmod3\), and put

\[
b=\frac{c+1}{3}.
\]

## Quotient promotion and subgroup gate

Promote the relation quotient

\[
g=c-1.
\]

Prove that its canonical inverse is

\[
w=\frac{c^2-1}{3}=gb
\]

and that

\[
A_1=gw=g^2b
=1+\frac{c-2}{3}N.
\]

Prove \(g\notin H_0\). Then prove that complete gcd refinement of all old and
new endpoints preserves generators for \(H_0\) and gives generators whose
product is \(g\). Deduce strict subgroup expansion independently of the square
class of \(b\).

## Exact square-class gate

Work in
\(\mathbb Q_{>0}^{\times}/(\mathbb Q_{>0}^{\times})^2\). Prove

\[
[A_0]=[c],
\qquad
[A_1]=[b],
\qquad
\gcd(c,b)=1,
\qquad
[b]\ne[c].
\]

Deduce the exact two-column gate:

\[
\boxed{\text{the new column closes immediately}
\iff b\text{ is an integer square}.}
\]

Prove that complete \(2\)-saturation adds no missed relation in the nonsquare
branch. In the square branch, show that its first new root is the one below
and that no further \(2\)-division changes the immediate gate.

## Root gate

If \(b=s^2\), prove that \(s\) is even and define

\[
R=s(c-1),
\]

\[
A=3s^2-3s+1,
\qquad
B=3s^2+3s+1.
\]

Verify

\[
N=AB,\quad \gcd(A,B)=1,
\]

\[
R-1=(s-1)B,\quad R+1=(s+1)A,
\]

and deduce

\[
\gcd(R-1,N)=B,\qquad\gcd(R+1,N)=A.
\]

Check \(c=11\), \(b=4\), \(N=133\), and \(R=20\).

## Classification

Decide whether this proves the narrow framework statement:

> Quotient promotion always passes the subgroup-expansion gate on this
> order-three source, but it passes the immediate complete-square-decoder gate
> exactly when its new square class cancels.

State that this covers only one seed and its first promoted quotient. It gives
no frequency or infinitude theorem for prime \(c=3s^2-1\), general quotient
sampler, all-input result, novelty claim, or unrestricted factoring algorithm.
