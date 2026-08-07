# F97 — the \(n^2\) canonical-residue menu fails at \(N=253\)

**Status:** exact bounded counterexample. It is not audited or promoted.
It does not rule out feedback in general.

## 1. Result

The F96 success does not extend across the square-inverse seed family.

For odd \(x\), define

\[
N_x=\frac{3x^2-1}{2}.
\]

Then

\[
3x^2=1+2N_x,
\]

so the public seed \(3\) has canonical inverse \(x^2\). An exact square-root
test gives the public normalized blocks \(3,x\).

The first retained stable semiprime in the declared increasing search is

\[
x=13,
\qquad
N_{13}=253=11\cdot23.
\]

For this input, the complete target-free menu

\[
0\le a,b\le n^2,
\qquad
n=\lceil\log_2(N+1)\rceil=8,
\qquad
n^2=64,
\]

finds no distinct canonical-inverse relation in the seed's nonzero square
class. It therefore finds no useful same-class closure.

This is an exact counterexample to the proposed instance law

\[
\text{stable square-inverse seed}
\Longrightarrow
\text{useful closure in the two-block }n^2\text{ menu}.
\]

## 2. Stable-input certificate

For \(N=253\),

\[
p=11,
\qquad
q=23,
\qquad
g=\gcd(p-1,q-1)=2.
\]

Therefore

\[
A=\frac{p-1}{g}=5,
\qquad
B=\frac{q-1}{g}=11,
\]

and

\[
\gcd(AB,N-1)=\gcd(55,252)=1.
\]

Thus \(253\) satisfies the requested P98 stable condition.

This factorization selects and certifies the test input only. The
per-input menu does not receive \(p\) or \(q\).

## 3. Public seed and exact menu

The public seed relation is

\[
3^{-1}_{\rm can}=169=13^2,
\]

\[
P_1=3\cdot169=507=1+2N=3\cdot13^2.
\]

The menu processes

\[
c_{a,b}=[3^a13^b]_N
\]

in increasing \(a+b\), then increasing \(a\). It skips a residue after its
first occurrence. For each new residue, it computes

\[
w_{a,b}=c_{a,b}^{-1}_{\rm can},
\qquad
P_{a,b}=c_{a,b}w_{a,b}.
\]

It accepts only if

\[
P_{a,b}\ne P_1,
\qquad
P_1P_{a,b}\text{ is an exact square},
\]

and the induced-root gcd is proper.

The exact null result is:

- exponent pairs examined: \(65^2=4225\);
- distinct residues examined: \(110\);
- distinct same-class relations: \(0\);
- global-sign collisions: \(0\);
- useful collisions: \(0\).

The selector receives only \(N\), the public blocks \(3,13\), the exponent
bound, and the fixed order. It receives no endpoint, relation, word, or
factor target.

## 4. The menu already covers the entire old subgroup

The seed identity gives

\[
3=13^{-2}\pmod N.
\]

Hence

\[
H=\langle3,13\rangle=\langle13\rangle.
\]

The public order computation gives

\[
\operatorname{ord}_{253}(13)=110.
\]

The menu visits exactly \(110\) distinct residues. Therefore it covers all
of \(H\).

This strengthens the finite null result:

\[
\boxed{
\text{no residue in }H\text{ has a distinct same-class canonical-inverse
relation.}
}
\]

For this seed state, a larger exponent bound cannot repair the one-step
canonical-residue closure. A later block refinement or a different source
operation could still change the state.

## 5. Positive control

The same source separately reruns the F96 control:

\[
x=43,
\qquad
N_{43}=2773=47\cdot59.
\]

It recovers

\[
[3^{99}43]_{2773}=1263,
\qquad
1263^{-1}_{\rm can}=1684,
\]

and

\[
1263\cdot1684=2{,}126{,}892.
\]

This closes with the seed relation and gives

\[
\gcd(108{,}618-1,2773)=47,
\qquad
\gcd(108{,}618+1,2773)=59.
\]

The control appears at exponent-pair ordinal \(5150\), as in F96. Thus the
F97 null is not an implementation failure or a changed menu.

## 6. Increasing-family order

The declared search examines odd \(x\) from \(3\) through \(2001\), and
stops at the first retained counterexample.

Before \(x=13\), the family gives

\[
\begin{array}{c|c}
x & N_x\\
\hline
3 & 13\\
5 & 37\\
7 & 73\\
9 & 121=11^2\\
11 & 181
\end{array}
\]

The four other values are prime. None is a distinct odd semiprime. Thus
\(x=13\) is the first selected stable semiprime in the declared order, and
it is already a counterexample.

## 7. Scope

F97 kills one precise proposal:

> From the two blocks exposed by every stable square-inverse seed, enumerate
> all nonnegative exponent pairs up to \(n^2\). A useful same-class relation
> will always occur.

That proposal is false. On \(N=253\), even the complete old subgroup has no
such relation.

F97 does not kill:

- feedback that first creates or splits another integer block;
- multi-round feedback with a changed block presentation;
- relations that close through more than one retained nonzero class;
- a different public source outside the first subgroup; or
- a different factoring screen.

The result is finite. It proves the displayed counterexample and nothing
about the frequency of failures in the family.

Also, \(253\) is not a hard factoring input: trial division finds the
factor \(11\), and \(11<n^2=64\). The example refutes the isolated
one-step closure law. It does not refute a hybrid algorithm that first
removes polynomially bounded small factors.
