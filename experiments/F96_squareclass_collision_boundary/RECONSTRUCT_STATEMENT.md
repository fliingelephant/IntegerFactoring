# F96 proof-blind reconstruction statement

Read only this file. Reconstruct every claim from first principles. You may
write and run independent code. Do not inspect any other F96 artifact.
Write a self-contained strict PASS or FAIL report to
RECONSTRUCT_RESULT.md.

## Part I. General square-class theorem

Let \(N\) be odd. Let

\[
P_i=g_iw_i\equiv1\pmod N
\]

be positive canonical-inverse relation values, and assume neither \(P_i\)
is an integer square.

Prove that the following are equivalent:

1. \(P_1\) and \(P_2\) have the same nonzero class in
   \(\mathbb Q_{>0}^{\times}/(\mathbb Q_{>0}^{\times})^2\).
2. \(P_1P_2\) is an exact integer square.
3. If \(D=\gcd(P_1,P_2)\), then there are coprime positive integers \(A,B\)
   such that

   \[
   P_1=DA^2,\qquad P_2=DB^2,
   \]

   and \(D\) is not a square.

Prove that \(D,A,B\) are units modulo \(N\), that

\[
A^2\equiv B^2\pmod N,
\qquad
R=\sqrt{P_1P_2}=DAB,
\qquad
R^2\equiv1\pmod N,
\]

and that

\[
\gcd(R-1,N)=\gcd(A-B,N),
\qquad
\gcd(R+1,N)=\gcd(A+B,N).
\]

Conclude that for odd \(N\) this collision factors \(N\) exactly when
\(R\not\equiv\pm1\pmod N\), equivalently when
\(A\not\equiv\pm B\pmod N\) globally.

Check the counterexample

\[
N=143=11\cdot13,
\]

\[
102\cdot136=13{,}872=3\cdot68^2=1+97N,
\]

\[
125\cdot135=16{,}875=3\cdot75^2=1+118N.
\]

Here \(68+75=N\), so the induced root is global \(-1\) and gives no proper
factor.

## Part II. First public state at \(N=2773\)

Let

\[
N=2773
\]

and start with

\[
P_1=3\cdot1849=3\cdot43^2=5547=1+2N.
\]

The public square-normalized blocks are \(3\) and \(43\). Put

\[
H=\langle3,43\rangle\subseteq(\mathbb Z/N\mathbb Z)^\times.
\]

Check

\[
3\cdot43^2\equiv1\pmod N,
\qquad
\operatorname{ord}_N(3)=667,
\qquad
\operatorname{ord}_N(43)=1334,
\qquad
|H|=1334.
\]

The target endpoints from F95 are \(842\) and \(2526=842^{-1}\bmod N\).
Prove their nonmembership in \(H\) from the short certificate

\[
43^{667}\equiv-1\pmod N,
\]

\[
t=842\cdot43^{-1}\equiv471\pmod N,
\qquad
t^2\equiv1\pmod N,
\qquad
t\not\equiv\pm1\pmod N.
\]

Use the fact that a cyclic group has at most one element of order two.

## Part III. Alternative canonical presentation inside \(H\)

Check the public word and canonical inverse

\[
c=[3^{99}43]_N=1263,
\qquad
w=c^{-1}_{\rm can}=1684.
\]

Then check

\[
cw=2{,}126{,}892=1+767N=3\cdot842^2.
\]

Thus \(c,w\in H\), even though \(842,2526\notin H\), and the relation value
is the same as the F95 value

\[
P_2=842\cdot2526.
\]

Check that

\[
\sqrt{P_1P_2}=108{,}618,
\]

\[
\gcd(108{,}618-1,N)=47,
\qquad
\gcd(108{,}618+1,N)=59.
\]

This is a representation-level gain inside an unchanged residue subgroup.

## Part IV. Bounded public selector

Let

\[
n=\lceil\log_2N\rceil=12.
\]

Define a public menu of exponent pairs

\[
0\le a,b\le n^2=144.
\]

Order pairs by increasing \(a+b\), then increasing \(a\). For each pair,
compute

\[
c_{a,b}=3^a43^b\bmod N,
\qquad
w_{a,b}=c_{a,b}^{-1}\bmod N,
\qquad
P_{a,b}=c_{a,b}w_{a,b}.
\]

Skip a residue after its first occurrence. Test whether
\(P_1P_{a,b}\) is an exact square. If so, test the two induced-root gcds.

This menu uses only \(N\), the first public blocks \(3,43\), modular
arithmetic, exact square tests, and gcd. It does not receive \(842\),
\(P_2\), \(47\), or \(59\).

Independently verify:

- there are \(145^2=21{,}025\) exponent pairs;
- there are five same-class hits: four reproduce the old exact relation
  value \(P_1\), and one has a distinct useful relation value;
- the first distinct and useful square-class collision is
  \((a,b)=(99,1)\);
- it is one-based pair ordinal 5150 and one-based unique-residue ordinal
  299;
- it gives \(c=1263,w=1684,P=P_2\);
- the smaller menu \(0\le a,b\le n\) has four same-class hits, all of which
  reproduce \(P_1\), and has no distinct or useful hit;
- all nonnegative raw integer monomials \(3^a43^b<N\), other than one,
  number 12; four reproduce \(P_1\), and none gives a distinct useful
  canonical-relation collision with \(P_1\).

You may also independently verify that the complete subgroup \(H\) has six
same-class residues. Four reproduce \(P_1\). Exactly two useful new
residues, \(1263\) and \(1684\), form one inverse pair and one distinct
relation value. The total same-class density is \(3/667\), and the useful
new density is \(1/667\).

## Scope

Part I is a general elementary theorem. Parts II–IV are exact fixed-instance
claims. The \(n^2\) menu is a genuine public polynomial-size selector for
this instance. Its bound was found after a complete finite subgroup scan,
so the instance is post-selected evidence.

Nothing here proves that a polynomial exponent menu succeeds on other
inputs, that closing words have inverse-polynomial density, or that an
all-input polynomial-time factoring algorithm exists. The mechanism is
still congruence-of-squares decoding; the new fixed-instance fact is that
canonical residue reduction finds a useful alternative relation
presentation inside the old subgroup when every raw integer product fails
to give a distinct useful relation.
