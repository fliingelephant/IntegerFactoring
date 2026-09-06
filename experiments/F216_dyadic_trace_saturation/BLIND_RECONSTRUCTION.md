# F216 dyadic trace saturation: statement-only blind reconstruction

## Integrity, verdict, and scope

The pre-read SHA-256 digest of `STATEMENT.md` was

```text
fdc4a78e1189b4e733edf5a8d07549c459c3dbabf096ecf445a94acdc0f1df59
```

It matches the preregistered digest exactly.

**Verdict: PASS within the statement's named-model scope.** All four
normalized images, their exact cardinalities, the public scaling identity,
the uniform density bound, and the long-interval consequence follow
symbolically. No finite verification or other mathematical computation is
used.

The statement does not explicitly incorporate `INTERVAL_COROLLARY.md`.
Therefore that file was not opened or hashed. The interval consequence
below is reconstructed directly from the theorem and periodicity.

This result is not a factoring algorithm. It is also not a lower bound on a
decoder that retains the inverse parameter, or on any attack outside the
explicitly identified trace-list model.

## 1. Definitions and the factor trace

Let \(N\) be odd and let \(t\ge5\). Define

\[
W_t(N)=\{u+Nu^{-1}\pmod{2^t}:u\in U(2^t)\}. \tag{1}
\]

The map in (1) is orientation-free: replacing \(u\) by \(Nu^{-1}\)
does not change its value.

If \(N=pq\) is an odd semiprime, then \(p\in U(2^t)\), and

\[
p+Np^{-1}\equiv p+q\pmod{2^t}.
\]

Thus the factor trace \(p+q\pmod{2^t}\) belongs to \(W_t(N)\). This
membership statement needs neither balanced factors nor distinct factors.

## 2. Two lifting lemmas

### 2.1 Odd square classes modulo powers of two

For \(t\ge3\), an odd residue is a square modulo \(2^t\) if and only if it
is \(1\pmod8\).

Necessity follows because every odd square is \(1\pmod8\). For sufficiency,
start with a square root modulo \(8\). Suppose an odd \(x\) satisfies

\[
x^2\equiv R\pmod{2^j},\qquad j\ge3.
\]

The two choices

\[
x' = x+\epsilon 2^{j-1},\qquad \epsilon\in\{0,1\},
\]

still have the same square modulo \(2^j\), while

\[
(x')^2-x^2\equiv \epsilon 2^j x\pmod{2^{j+1}}.
\]

Because \(x\) is odd, exactly one choice of \(\epsilon\) matches the next
bit of \(R\). Induction constructs a root modulo \(2^t\). The same bit
lifting is a public deterministic algorithm using polynomially many bit
operations in \(t\).

### 2.2 A toggle-lifting criterion

We will repeatedly use the following elementary criterion. Let
\(H:\mathbb Z_2\to\mathbb Z_2\) satisfy

\[
v_2\bigl(H(x+2^j)-H(x)\bigr)=j
\quad\text{for every }x\in\mathbb Z_2\text{ and }j\ge0. \tag{2}
\]

Then \(H\) induces a bijection modulo \(2^r\) for every \(r\ge1\). For
\(r=1\), (2) with \(j=0\) says that the two input classes give the two
output classes. If an input solves \(H(x)=y\pmod{2^j}\), its two lifts are
\(x\) and \(x+2^j\). Equation (2) says their outputs differ in bit \(j\),
so exactly one lift solves the congruence modulo \(2^{j+1}\). This proves
the claim by induction.

## 3. Public reduction to four square classes

Let \(d\in\{1,3,5,7\}\) be the unique residue satisfying

\[
d\equiv N\pmod8.
\]

Then \(R=Nd^{-1}\pmod{2^t}\) is \(1\pmod8\). By the square-class lemma,
there is a publicly computable odd \(a\pmod{2^t}\) such that

\[
N\equiv da^2\pmod{2^t}. \tag{3}
\]

Multiplication by \(a\) permutes \(U(2^t)\). Substituting \(u=av\) in
(1) gives

\[
u+Nu^{-1}
\equiv av+da^2(av)^{-1}
=a(v+dv^{-1})\pmod{2^t}.
\]

Consequently,

\[
\boxed{W_t(N)=aW_t(d).} \tag{4}
\]

Multiplication by odd \(a\) is also a permutation of all residues modulo
\(2^t\). Hence

\[
|W_t(N)|=|W_t(d)|,
\]

so the cardinality depends only on \(N\pmod8\). The simple normalized
congruence descriptions below need not remain literally unchanged after
scaling, but their sizes and densities do.

## 4. The classes \(d=3\) and \(d=7\)

Write

\[
F_d(u)=u+du^{-1}.
\]

Every odd \(u\) satisfies \(u^{-1}\equiv u\pmod8\). Therefore

\[
F_3(u)\equiv4u\equiv4\pmod8,
\]

and

\[
F_7(u)\equiv8u\equiv0\pmod8. \tag{5}
\]

It remains to show that every residue in each indicated class occurs.
Restrict to \(u=1+4x\) and define the integral 2-adic functions

\[
H_3(x)=\frac{F_3(1+4x)-4}{8},
\qquad
H_7(x)=\frac{F_7(1+4x)}{8}. \tag{6}
\]

For either \(d=3\) or \(d=7\), put \(u=1+4x\) and let
\(\Delta=4\cdot2^j\). Direct subtraction gives

\[
F_d(u+\Delta)-F_d(u)
=\Delta\left(1-\frac{d}{u(u+\Delta)}\right). \tag{7}
\]

Here \(u(u+\Delta)\equiv1\pmod4\), while \(d\equiv3\pmod4\). The
parenthesis in (7) therefore has exact 2-adic valuation \(1\). After
division by \(8\),

\[
v_2\bigl(H_d(x+2^j)-H_d(x)\bigr)
=(j+2)+1-3=j. \tag{8}
\]

The toggle-lifting criterion shows that each \(H_d\) is bijective modulo
every power of two. Equations (5)--(8) prove the exact images

\[
\boxed{W_t(3)=\{s\pmod{2^t}:s\equiv4\pmod8\},} \tag{9}
\]

\[
\boxed{W_t(7)=\{s\pmod{2^t}:s\equiv0\pmod8\}.} \tag{10}
\]

Each is one complete residue class modulo \(8\), so

\[
\boxed{|W_t(3)|=|W_t(7)|=2^{t-3}.} \tag{11}
\]

## 5. The class \(d=5\)

First determine the necessary low bits. If \(u\) is replaced by
\(u+8z\), equation (7) with \(d=5\) shows that \(F_5(u)\pmod{32}\)
does not change: the increment has a factor \(8\), and
\(1-5u^{-2}\) is divisible by \(4\). It is therefore enough to use the
four odd residues modulo \(8\). Symbolically,

\[
u\equiv1,5\pmod8\quad\Longrightarrow\quad F_5(u)\equiv6\pmod{32},
\]

\[
u\equiv3,7\pmod8\quad\Longrightarrow\quad F_5(u)\equiv26\pmod{32}. \tag{12}
\]

For example, the inverses of \(1,3,5,7\) modulo \(32\) are respectively
\(1,11,13,23\), which proves (12) by exact modular arithmetic.

To prove sufficiency for the first class, restrict to \(u=1+8x\) and put

\[
H_5(x)=\frac{F_5(1+8x)-6}{32}. \tag{13}
\]

For an input increment \(2^j\), the corresponding increment of \(u\) is
\(\Delta=8\cdot2^j\). Now \(u(u+\Delta)\equiv1\pmod8\), so

\[
v_2\left(1-\frac5{u(u+\Delta)}\right)=2.
\]

Using (7) and dividing by \(32\) gives

\[
v_2\bigl(H_5(x+2^j)-H_5(x)\bigr)
=(j+3)+2-5=j. \tag{14}
\]

Thus \(H_5\) is bijective modulo every power of two and realizes every
residue \(6\pmod{32}\). Finally,

\[
F_5(-u)=-F_5(u),
\]

so the negatives realize every residue \(-6\equiv26\pmod{32}\). Together
with necessity (12), this gives

\[
\boxed{W_t(5)=
\{s\pmod{2^t}:s\equiv6\text{ or }26\pmod{32}\}.} \tag{15}
\]

The two classes are disjoint and each has \(2^{t-5}\) elements. Hence

\[
\boxed{|W_t(5)|=2^{t-4}.} \tag{16}
\]

## 6. The square class \(d=1\)

### 6.1 Valuation strata

Every odd \(u\) is either \(1\pmod4\) or its negative is \(1\pmod4\).
Since

\[
F_1(-u)=-F_1(u), \tag{17}
\]

it is enough first to determine the traces from \(u\equiv1\pmod4\).

For such a \(u\), write

\[
u=1+2^bz,qquad b=v_2(u-1)\ge2,qquad z\text{ odd}.
\]

The exact identity

\[
F_1(u)-2
=u+u^{-1}-2
=\frac{(u-1)^2}{u}
=2^{2b}\frac{z^2}{1+2^bz} \tag{18}
\]

governs the image. Put

\[
\Phi_b(z)=\frac{z^2}{1+2^bz}.
\]

This is an odd 2-adic unit. Since every odd square is \(1\pmod8\),

\[
\Phi_b(z)\equiv
\begin{cases}
5\pmod8,&b=2,\\
1\pmod8,&b\ge3.
\end{cases} \tag{19}
\]

For \(b=2\), the denominator is \(1+4z\equiv5\pmod8\), whose inverse is
also \(5\pmod8\). For \(b\ge3\), the denominator is \(1\pmod8\). This
proves (19).

The congruence restriction in (19) is also sufficient. Restrict further to
\(z=1+4x\), let

\[
c_b=\begin{cases}5,&b=2,\\1,&b\ge3,\end{cases}
\]

and define

\[
G_b(x)=\frac{\Phi_b(1+4x)-c_b}{8}. \tag{20}
\]

This is integral by (19). For \(z=1+4x\) and
\(\Delta=4\cdot2^j\), direct subtraction gives

\[
\Phi_b(z+\Delta)-\Phi_b(z)
=\Delta\,
\frac{2z+\Delta+2^bz(z+\Delta)}
{(1+2^bz)(1+2^b(z+\Delta))}. \tag{21}
\]

The denominator is odd. The numerator after \(\Delta\) is factored out is
twice

\[
z+\frac\Delta2+2^{b-1}z(z+\Delta),
\]

and the displayed quantity is odd because \(z\) is odd, while the other
two terms are even. Thus the right side of (21) has exact valuation
\(j+3\). Dividing by \(8\) yields

\[
v_2\bigl(G_b(x+2^j)-G_b(x)\bigr)=j. \tag{22}
\]

The toggle-lifting criterion now proves that \(G_b\) is bijective at every
precision. Therefore, modulo \(2^k\), the exact image of \(\Phi_b\) is

\[
\left\{w\in U(2^k):
w\equiv c_b\pmod{2^{\min(3,k)}}\right\}. \tag{23}
\]

The truncation in (23) handles \(k=1,2\); equivalently, lift the desired
low-precision unit to its specified class modulo \(8\), apply the 2-adic
surjectivity, and reduce again.

If \(2b\ge t\), equation (18) gives only the trace \(2\pmod{2^t}\). The
nonzero valuation strata therefore have

\[
2\le b\le\left\lfloor\frac{t-1}{2}\right\rfloor,
\qquad k=t-2b\ge1. \tag{24}
\]

Combining (18), (23), and (24), the positive half-image is exactly

\[
W_t^+(1)=\{2\}\cup
\bigcup_{b=2}^{\lfloor(t-1)/2\rfloor}
\left\{
2+2^{2b}w\pmod{2^t}:
w\in U(2^{t-2b}),\quad
w\equiv c_b\pmod{2^{\min(3,t-2b)}}
\right\}. \tag{25}
\]

Different sets in (25) are disjoint because their nonconstant members have
different exact values \(v_2(s-2)=2b\). Every member of \(W_t^+(1)\) is
\(2\pmod{16}\), while its negative is \(14\pmod{16}\). Hence, for
\(t\ge5\), the two halves are disjoint, and (17) proves

\[
\boxed{W_t(1)=W_t^+(1)\mathbin{\dot\cup}(-W_t^+(1)).} \tag{26}
\]

This also covers the edge case in which \(u-1\) has valuation at least
\(\lceil t/2\rceil\): all such inputs contribute the single residue \(2\),
not an additional stratum.

### 6.2 Exact cardinality

For \(k=t-2b\), the number of units in the specified truncated class in
(23) is

\[
2^{\max(k-3,0)}. \tag{27}
\]

Therefore

\[
|W_t^+(1)|
=1+\sum_{b=2}^{\lfloor(t-1)/2\rfloor}
2^{\max(t-2b-3,0)}. \tag{28}
\]

If \(t=2m\), the final stratum has \(k=2\), and the preceding exponents
are \(1,3,\ldots,2m-7\). Thus

\[
|W_t^+(1)|
=2+\sum_{j=0}^{m-4}2^{2j+1}
=\frac{2^{t-5}+4}{3}. \tag{29}
\]

The empty-sum interpretation makes (29) valid at \(t=6\).

If \(t=2m+1\ge7\), the strata with \(k=3\) and \(k=1\) each have size
one, and the other exponents are \(2,4,\ldots,2m-6\). The same
geometric-sum evaluation gives

\[
|W_t^+(1)|=\frac{2^{t-5}+5}{3}, \tag{30}
\]

At \(t=5\), (28) consists of the singleton trace and the one \(k=1\)
stratum, so its value is \(2\), which agrees with (30). Thus (30) includes
both edge cases \(t=5,7\).

Doubling (29) and (30) by the disjoint union (26) proves

\[
\boxed{
|W_t(1)|=
\begin{cases}
(2^{t-4}+8)/3,&t\text{ even},\\
(2^{t-4}+10)/3,&t\text{ odd}.
\end{cases}} \tag{31}
\]

In particular,

\[
\boxed{|W_t(1)|=2^t/48+O(1).} \tag{32}
\]

## 7. Density and literal-list consequence

The four normalized cardinalities are

\[
\begin{array}{c|c|c}
d& W_t(d)&|W_t(d)|\\ \hline
1&W_t^+(1)\mathbin{\dot\cup}(-W_t^+(1))
&\dfrac{2^{t-4}+8}{3}\text{ or }\dfrac{2^{t-4}+10}{3}\\[4pt]
3&4\pmod8&2^{t-3}\\
5&6\text{ or }26\pmod{32}&2^{t-4}\\
7&0\pmod8&2^{t-3}
\end{array}
\]

Equations (4), (11), (16), and (31) imply, uniformly for every odd \(N\)
and every \(t\ge5\),

\[
\boxed{|W_t(N)|\ge\frac{2^t}{48}.} \tag{33}
\]

At a partial-factor threshold

\[
t=n/4-\operatorname{polylog}(n),
\]

integer rounding changes only a constant factor, and

\[
|W_t(N)|
\ge2^{n/4-\operatorname{polylog}(n)-O(1)}
=2^{\Omega(n)}. \tag{34}
\]

Thus a literal materialization of the trace residues is exponentially
large in the input bit length, rather than numerical QP.

The exact images also explain why increasing \(t\) does not impose one new
independent trace bit at every lift:

1. For normalized classes \(3\) and \(7\), all conditions are the single
   fixed congruence modulo \(8\), with density \(1/8\).
2. For normalized class \(5\), all conditions are two fixed congruences
   modulo \(32\), with total density \(1/16\).
3. For normalized class \(1\), there are only \(O(t)\) valuation strata,
   and their union retains density \(1/48+O(2^{-t})\).

Public multiplication by \(a\) preserves each density even when it changes
the displayed normalized residue classes.

## 8. Interval consequence derivable from the statement

Let

\[
\widetilde W_t(N)=\{x\in\mathbb Z:x\bmod2^t\in W_t(N)\}.
\]

For any interval \(I\) of \(H\) consecutive integers, write
\(H=qL+r\), where \(q=2^t\), \(L=\lfloor H/q\rfloor\), and
\(0\le r<q\). Each consecutive block of \(q\) integers contains every
residue exactly once. Therefore

\[
L|W_t(N)|
\le |I\cap\widetilde W_t(N)|
\le (L+1)|W_t(N)|. \tag{35}
\]

Using (33), the lower bound becomes

\[
|I\cap\widetilde W_t(N)|
\ge\left\lfloor\frac{H}{2^t}\right\rfloor\frac{2^t}{48}
\ge\frac{H-2^t}{48}. \tag{36}
\]

Thus every interval spanning many full dyadic periods retains asymptotic
density at least \(1/48\). In particular, if \(H\ge2^{t+1}\), then

\[
|I\cap\widetilde W_t(N)|\ge H/96. \tag{37}
\]

This is the interval conclusion forced solely by the statement. It is
invariant under the public scaling because it uses complete periods and
cardinality only.

There is no corresponding uniform claim here for an interval shorter than
one period. Multiplication by the public odd \(a\) is a modular permutation,
not an order-preserving map, and cardinality alone does not control how its
image meets a short Archimedean interval. An implicit short-interval finder
therefore remains outside the proved boundary.

## 9. Exact attack boundary and edge cases

The proved obstruction applies to the following specific bridge:

1. discard the inverse parameter \(u\) and retain only the orientation-free
   trace \(u+Nu^{-1}\pmod{2^t}\);
2. replace many odd-prime trace conditions by one high-power dyadic trace
   condition; and
3. explicitly materialize the resulting trace-residue list.

That list has constant-order density and is exponential at the stated
threshold. The theorem does not rule out:

1. an implicit interval finder, especially inside less than one dyadic
   period;
2. a method that retains \(u\), its orientation, or reciprocal-prefix
   information;
3. a nonlinear integer statistic rather than the modular trace alone;
4. mixed odd moduli;
5. a direct reciprocal-prefix selector; or
6. any compressed algorithm that does not materialize \(W_t(N)\).

The exact mathematical domain is also important. The normalization theorem
assumes odd \(N\), and the displayed image formulas assume \(t\ge5\).
No formula here is asserted for even \(N\) or for \(t<5\). Semiprimality is
used only to identify the genuine factor trace as a member of the image;
the image and saturation theorems themselves hold for every odd \(N\).

Accordingly, F216 closes a named explicit representation, not the
all-input factoring task in `PROMPT.md` and not the inverse-box or
reciprocal-prefix problem as a whole.
