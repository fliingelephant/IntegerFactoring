# Blind reconstruction of F254

## Statement authentication

Before reading the statement, its SHA-256 digest was checked to be

\[
\texttt{25d20381188d0ffe5e7d9b87331c3921b0f78dd9344d73628ca33e1f1201e190}.
\]

This reconstruction uses only that authenticated statement, `PROMPT.md`, and
`AGENTS.md`.

## 1. The tailored row

Assume that (N) is odd and

\[
b^2-2y^2=-1,\qquad 1<y<N.
\]

Set

\[
T=N+y,\qquad D=T^2-2,\qquad S=T^2-1,
\qquad A=1+Dy^2.
\]

Since (T\ge 2),

\[
(T-1)^2<T^2-2<T^2.
\]

Thus (D) is positive and is not a square. Direct expansion gives

\[
S^2-DT^2=(T^2-1)^2-(T^2-2)T^2=1.
\]

Also,

\[
S\equiv y^2-1\pmod N
\]

and

\[
A\equiv 1+(y^2-2)y^2=(y^2-1)^2\pmod N.
\]

Therefore (S\bmod N) is a publicly known square root of (A\bmod N).

The Pell equation implies that (b) is odd. Reducing
(b^2+1=2y^2) modulo (8) then shows that (y) is odd. Hence

\[
u=\frac{b-1}{2},\qquad v=\frac{b+1}{2}
\]

are integers. They satisfy

\[
u^2+v^2=\frac{b^2+1}{2}=y^2,
\qquad
2uv=\frac{b^2-1}{2}=y^2-1.
\]

It follows that

\[
\begin{aligned}
(yN+2u^2)(yN+2v^2)
 &=y^2N^2+2yN(u^2+v^2)+4u^2v^2\\
 &=y^2N^2+2y^3N+(y^2-1)^2\\
 &=1+\bigl((N+y)^2-2\bigr)y^2=A.
\end{aligned}
\]

Thus the exact public factorization is

\[
A=F_-(N)F_+(N),\qquad
F_-(X)=yX+2u^2,\quad F_+(X)=yX+2v^2.
\]

## 2. Modular roots and the even-component decoder

Write any component as

\[
C_i=F_i(N)=y_iN+2w_i^2.
\]

Then (C_i\equiv2w_i^2\pmod N). For a component subset (I) of even
size (|I|=2m), define

\[
R_I=2^m\prod_{i\in I}w_i\pmod N.
\]

This is a public decoder because

\[
R_I^2\equiv 2^{2m}\prod_{i\in I}w_i^2
       \equiv\prod_{i\in I}C_i\pmod N.
\]

For the two components from one Pell row, this decoder gives

\[
R=2uv=y^2-1\equiv S\pmod N,
\]

so it extends the supplied root of the original row. If an even component
subset also had an exact product (X^2=\prod_{i\in I}C_i), then
(X^2\equiv R_I^2\pmod N), and the usual gcd comparisons with
(X-R_I) and (X+R_I) would be available. The counterexample below shows
that this source need not supply any nonempty exact-square subset at all.

## 3. Determinant localization

For

\[
F_i(X)=y_iX+2w_i^2,\qquad F_j(X)=y_jX+2w_j^2,
\]

the linear-polynomial resultant is

\[
\operatorname{Res}(F_i,F_j)
=2(y_iw_j^2-y_jw_i^2).
\]

If a rational prime (q) divides both (F_i(N)) and (F_j(N)), then it
divides

\[
y_jF_i(N)-y_iF_j(N)
=2(y_jw_i^2-y_iw_j^2)
=-\operatorname{Res}(F_i,F_j).
\]

Thus every prime reused by two specialized components is supported by this
public determinant. Over $\mathbb{Q}[X]$, distinct nonassociate linear
forms are distinct irreducibles. Unique factorization therefore rules out a
nonempty square product in which each such form occurs once. Consequently,
cross-component square-class reuse is caused by arithmetic specialization,
not by a generic polynomial square identity.

## 4. Completeness of the admissible Pell window for (N=143)

Take

\[
N=143=11\cdot13.
\]

All positive solutions of (b^2-2y^2=-1) are generated from ((1,1)) by

\[
b'+y'\sqrt2=(3+2\sqrt2)(b+y\sqrt2),
\]

or equivalently

\[
b'=3b+4y,\qquad y'=2b+3y.
\]

For completeness, this follows by descent. If (y>1), then (y) is odd,
so (y\ge3). From (b^2=2y^2-1),

\[
\frac{4y}{3}<b<\frac{3y}{2}.
\]

Hence multiplication by (3-2\sqrt2) gives another positive integral
solution

\[
(3b-4y)+(3y-2b)\sqrt2,
\]

whose second coordinate is smaller because (b>y). Repetition terminates
at (y=1), where (b=1). Reversing the descent proves that the recurrence
lists every positive solution.

The first four solutions are

\[
(1,1),\quad(7,5),\quad(41,29),\quad(239,169).
\]

The recurrence makes (y) strictly increase. Therefore the complete window
(1<y<143) consists exactly of (y=5) and (y=29). Changing the sign of
(b) only swaps the squares (u^2) and (v^2), so it produces no new
components.

## 5. Exact arithmetic and square classes

For ((b,y)=(7,5)),

\[
(u,v,T,D,S)=(3,4,148,21902,21903),
\]

and

\[
\begin{aligned}
F_-(143)&=5\cdot143+2\cdot3^2=733,\\
F_+(143)&=5\cdot143+2\cdot4^2=747=3^2\cdot83,\\
A&=1+21902\cdot5^2=547551=733\cdot747,\\
S&\equiv24\pmod{143}.
\end{aligned}
\]

For ((b,y)=(41,29)),

\[
(u,v,T,D,S)=(20,21,172,29582,29583),
\]

and

\[
\begin{aligned}
F_-(143)&=29\cdot143+2\cdot20^2=4947
          =3\cdot17\cdot97,\\
F_+(143)&=29\cdot143+2\cdot21^2=5029
          =47\cdot107,\\
A&=1+29582\cdot29^2=24878463=4947\cdot5029,\\
S&\equiv125\pmod{143}.
\end{aligned}
\]

The displayed factors (733,83,17,97,47,107) are prime. This is certified
by trial division by the primes no larger than their square roots; for the
largest one, (733), these are
(2,3,5,7,11,13,17,19,23), none of which divides it.

After exponents are reduced modulo (2), the four component columns are

\[
733,\qquad 83,\qquad 3\cdot17\cdot97,
\qquad47\cdot107.
\]

Prime (733) occurs with odd exponent only in column 1, prime (83) only
in column 2, prime (17) only in column 3, and prime (47) only in column
4. These are four private pivot rows. Looking at them successively shows
that any zero linear combination of the four parity columns has all four
coefficients zero. The parity matrix therefore has rank four. No nonempty
component subset has an exact-square product, even without the decoder's
even-cardinality restriction.

For the two original rows, the first row has private odd prime (733), and
the second has private odd prime (17). Their two parity columns are thus
independent, so the original-row matrix has rank two as well.

## 6. Direct screens

Because (143=11\cdot13), an integer is coprime to (143) exactly when its
residues modulo both 11 and 13 are nonzero. The following table checks every
displayed row parameter, component, and supplied root.

| row | value | mod 11 | mod 13 |
|---|---:|---:|---:|
| (y=5) | (b=7) | 7 | 7 |
| | (y=5) | 5 | 5 |
| | (u=3) | 3 | 3 |
| | (v=4) | 4 | 4 |
| | (T=148) | 5 | 5 |
| | (D=21902) | 1 | 10 |
| | (S=21903\equiv24\pmod{143}) | 2 | 11 |
| | (F_-(143)=733) | 7 | 5 |
| | (F_+(143)=747) | 10 | 6 |
| (y=29) | (b=41) | 8 | 2 |
| | (y=29) | 7 | 3 |
| | (u=20) | 9 | 7 |
| | (v=21) | 10 | 8 |
| | (T=172) | 7 | 3 |
| | (D=29582) | 3 | 7 |
| | (S=29583\equiv125\pmod{143}) | 4 | 8 |
| | (F_-(143)=4947) | 8 | 7 |
| | (F_+(143)=5029) | 2 | 11 |

Label the four forms by their ((y,w)) pairs:

\[
(5,3),\quad(5,4),\quad(29,20),\quad(29,21).
\]

Their six pairwise resultants and residues are

| pair | resultant | mod 11 | mod 13 |
|---|---:|---:|---:|
| (1,2) | (70) | 4 | 5 |
| (1,3) | (3478) | 2 | 7 |
| (1,4) | (3888) | 5 | 1 |
| (2,3) | (3072) | 3 | 4 |
| (2,4) | (3482) | 6 | 11 |
| (3,4) | (2378) | 2 | 12 |

Every entry is nonzero modulo both prime factors of (143). Thus all these
gcd screens return 1. The supplied congruences also check directly:

\[
24^2=576\equiv4\equiv547551\pmod{143},
\]

\[
125^2=15625\equiv38\equiv24878463\pmod{143}.
\]

Hence neither admissible row gives a factor through the listed direct
screens, and neither the original-row bank nor the component bank gives an
exact-square dependency.

## 7. Scope

This is a counterexample only to the universal claim that this tailored
negative-Pell construction, using its complete window (1<y<N), must
produce a direct factor or an exact-square dependency. It gives no bound on
the success probability of randomized choices of (D), row index, window,
or mixed source. It is not an obstruction to integer factoring, and it does
not refute a general retrospective multirow square-dependency channel.
