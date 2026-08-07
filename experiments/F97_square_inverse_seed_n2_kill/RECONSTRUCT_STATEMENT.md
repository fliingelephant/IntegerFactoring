# F97 proof-blind reconstruction statement

Read only this file. Reconstruct the claims from first principles. You may
write and run independent code. Do not inspect any other F97 artifact.
Write a strict PASS or FAIL report to RECONSTRUCT_RESULT.md.

## Family and fixed counterexample

For odd \(x\), define

\[
N_x=\frac{3x^2-1}{2}.
\]

Then

\[
3x^2=1+2N_x,
\]

so the canonical inverse of the public seed \(3\) modulo \(N_x\) is \(x^2\)
whenever \(x^2<N_x\). An exact square-root test exposes the public blocks
\(3,x\).

At

\[
x=13,\qquad N=253=11\cdot23,
\]

check

\[
3^{-1}_{\rm can}=169=13^2,\qquad
P_1=3\cdot169=507=1+2N.
\]

For the P98 certificate, check

\[
g=\gcd(11-1,23-1)=2,\qquad
A=5,\qquad B=11,
\]

\[
\gcd(AB,N-1)=\gcd(55,252)=1.
\]

## Target-free menu

Let

\[
n=\lceil\log_2(N+1)\rceil=8,\qquad n^2=64.
\]

Enumerate every pair

\[
0\le a,b\le64
\]

by increasing \(a+b\), then increasing \(a\). For each first-occurrence
residue

\[
c=[3^a13^b]_N,
\]

compute its least positive inverse \(w\) and relation value \(P=cw\).
Ignore the repeated old value \(P=P_1\). For every distinct value, test
whether \(P_1P\) is an exact square and, if so, test the induced-root gcds.

Independently verify:

- the menu has \(65^2=4225\) exponent pairs;
- it visits exactly 110 distinct residues;
- \(\operatorname{ord}_{253}(13)=110\);
- \(3=13^{-2}\pmod N\), so
  \(H=\langle3,13\rangle=\langle13\rangle\);
- the menu therefore visits every element of \(H\);
- no residue in \(H\) gives a distinct canonical relation value in the
  nonzero square class of \(P_1\);
- consequently there is no global-sign or useful distinct closure.

Thus no larger exponent bound can repair this one-step rule without first
changing the presentation or source.

## Increasing-order and positive-control claims

For odd \(x=3,5,7,9,11,13\), check

\[
N_x=13,37,73,121,181,253.
\]

The first four other values are prime and \(121=11^2\). Hence \(x=13\) is
the first distinct odd semiprime in increasing odd-\(x\) order, and it
satisfies the stable condition above.

As a positive control, at

\[
x=43,\qquad N=2773,
\]

the same menu definition with \(n=12\) and bound \(144\) has its first
useful distinct hit at

\[
(a,b)=(99,1),
\]

\[
c=1263,\qquad w=1684,
\]

and the induced-root gcds are \(47\) and \(59\).

## Scope

The per-input menu receives only \(N\), the blocks \(3,x\), and the fixed
menu rule. The factorization is used only to select and certify the finite
test input.

This is an exact counterexample to the claim that every stable
square-inverse seed has a useful one-step closure in its two-block \(n^2\)
menu. It does not rule out later block refinement, multiple seeds, multiple
retained square classes, a source outside \(H\), or another decoder.

Also, \(253\) has the small factor \(11<n^2=64\). The example refutes the
isolated closure law, not a hybrid factoring algorithm that first removes
polynomially bounded small factors. It supplies no asymptotic failure
frequency or general lower bound.
