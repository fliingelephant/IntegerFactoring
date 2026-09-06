# F159 V2 statement-only blind reconstruction

## Verdict

**PASS.**

The only F159 source inspected for this reconstruction was
`V2_STATEMENT.md`. Its SHA-256 was verified before inspection as

```text
53584b0152b3eeca7dd37ded6707596ee763e48d7d6c55bb4b335a1ef4c8415f
```

The explicit-layer theorem, the compact theorem, the odd-order
qualification, the post-refinement classification, the finite certificate,
and the stated complexity and scope all hold.

## 1. Local lemma behind root-layer saturation

For (r\in\{p,q\}), write

\[
G_r=(\mathbf Z/r\mathbf Z)^\times
\quad\text{and}\quad
H_r=\pi_r(H).
\]

The group (G_r) is cyclic. Hence (G_r/H_r) is cyclic. If a unit (y)
satisfies (y^2\in H_r), then the coset (yH_r) has order at most two in
(G_r/H_r). A cyclic group has at most one nonidentity element of order
two. Consequently, for any two elements (x,x_0\notin H_r) whose squares
belong to (H_r),

\[
xH_r=x_0H_r,
\qquad x\in x_0H_r.
\tag{A}
\]

This is the only group-theoretic saturation fact needed below.

## 2. Reconstruction of the explicit-list theorem

For a comparison with (h\in H),

\[
\gcd(x-h,N)=
\begin{cases}
N,&x=h\pmod N,\\
p\text{ or }q,&x=h\text{ in exactly one hidden field},\\
1,&x\ne h\text{ in both hidden fields}.
\end{cases}
\]

Suppose no proper gcd occurs. Before the first external root, a root is
therefore either an element of (H), or it lies outside both (H_p) and
(H_q). Indeed, if (x_r\in H_r), completeness of the list (H) supplies
an (h\in H) with (x_r=h_r); that comparison cannot have gcd one.

Let (x_0) be the first external root. Then (x_0\notin H) and
(x_0^2\in H), so

\[
K=\langle H,x_0\rangle=H\sqcup x_0H,
\qquad |K|=2|H|.
\tag{B}
\]

Moreover, (x_{0,r}\notin H_r) and (x_{0,r}^2\in H_r) for both hidden
primes. Thus

\[
[K_r:H_r]=2
\qquad(r=p,q).
\tag{C}
\]

Now take a later root (x). Its local coset has order at most two. By (A),
at each prime it is either (H_r) or (x_{0,r}H_r). Hence (x_r\in K_r)
for both (r). For each prime, some member of the complete list (K)
therefore agrees with (x) locally. Its gcd comparison is nontrivial. On a
no-proper-factor branch it must be (N), so (x\in K) globally. Thus no
later root can add another coset without first exposing (p) or (q).

It follows exactly that

\[
\text{proper factor}
\quad\lor\quad
\langle H,X\rangle=H
\quad\lor\quad
[\langle H,X\rangle:H]=2.
\]

In the last case, (C) proves that both hidden images have index two. This
also shows why the conclusion is stronger than a mere global size bound:
an external root cannot be internal at one hidden prime on the no-factor
branch.

If the first external root is in position (j), the scan makes at most

\[
j|H|+2(|X|-j)|H|\le 2|H||X|
\]

gcd calls. If no external root exists, it makes only (|H||X|). Constructing
(K) takes (|H|) modular multiplications. A gcd and a modular
multiplication have polynomial bit cost in (log N). Therefore the stated
procedure has quasipolynomial bit cost whenever both explicit list sizes
are quasipolynomial in the input length.

## 3. Reconstruction of compact cyclic alignment

The common-order hypothesis gives

\[
|\langle g_r\rangle|=M
\qquad(r=p,q),
\]

and exponents in each local copy of (langle g\rangle) are unique modulo
(M). A root (x_i) is locally internal exactly when

\[
x_{i,r}=g_r^k
\quad\text{for some }k,
\]

in which case squaring gives

\[
2k\equiv a_i\pmod M.
\tag{D}
\]

A linear congruence with coefficient two has zero, one, or two residue
class solutions. Testing every solution of (D) therefore finds every
possible local internal match. If the two primes select different
solutions, or only one prime has a match, one of the tested gcds is a
proper factor. Hence, on a no-factor branch, (x_i) is either globally a
tested power of (g), or it is external in both hidden fields.

Let (x_0) be a first external root, and let (x_i) be another external
root. The local lemma gives

\[
x_{i,r}x_{0,r}^{-1}\in\langle g_r\rangle.
\]

Thus (x_{i,r}=x_{0,r}g_r^{k_r}), and squaring yields

\[
2k_r\equiv a_i-a_0\pmod M.
\tag{E}
\]

Equation (E) is always soluble. If (M) is odd, two is invertible modulo
(M). If (M) is even, both (a_i) and (a_0) are odd because each is
coprime to (M), so their difference is even. The number of solutions is
(gcd(2,M)\le2). The gcd tests against all candidates
(x_0g^k) detect different hidden choices as a proper factor. With no such
factor, one candidate agrees at both primes, and

\[
x_i=x_0g^k\pmod N.
\tag{F}
\]

It remains to verify the order and the claimed cyclic equality. Since
(x_{0,r}^2=g_r^{a_0}) and (gcd(a_0,M)=1), the square (x_{0,r}^2) has
order (M). If (n_r=\operatorname{ord}_r(x_0)), then

\[
\frac{n_r}{\gcd(n_r,2)}=M.
\]

The alternative (n_r=M) can occur only when (M) is odd, but then
(langle x_{0,r}\rangle=langle x_{0,r}^2\rangle=langle g_r\rangle),
contrary to externality. Therefore (n_r=2M) for both primes. If
(b a_0\equiv1\pmod M), then

\[
x_0^{2b}=g^{a_0b}=g\pmod N.
\]

Thus

\[
\langle g,x_0\rangle=langle x_0\rangle,
\qquad
\operatorname{ord}_p(x_0)=\operatorname{ord}_q(x_0)=2M.
\]

Together with (F), this proves compact alignment and the same index-at-most-
two saturation as the explicit-list theorem.

The initial classification uses at most two gcds and modular powers per
root. The later alignment uses at most two more per external root. Solving
the linear congruences is polynomial-time arithmetic. The total is
(O(s)) gcds and modular exponentiations. The certified common order and
the supplied factorization of (M) are premises; this cost statement does
not charge the procedure with discovering or certifying them.

### Odd (M)

When (M) is odd, squaring is an automorphism of (langle g\rangle). The
unique internal root of (g^{a_i}) is

\[
g^{k_i},
\qquad
k_i\equiv 2^{-1}a_i\pmod M,
\]

which is public. Over either odd prime, the two field roots are exactly
(g_r^{k_i}) and (-g_r^{k_i}). A mixed hidden sign gives a proper gcd in
the internal-root test. Hence every external root on a no-factor branch is
globally

\[
x_i=-g^{k_i}.
\]

If any such root occurs, it generates (-1) together with (H), and all
roots lie in the already public group (langle g,-1\rangle). This proves
the odd-order public-root qualification. It does not constrain the integer
representatives used to encode those public residues.

## 4. Integer refinement and the exact post-refinement screen

If a named integer block (b) represents a unit modulo (N), every integer
divisor of (b) is also a unit modulo (N). For

\[
d=\gcd(b,x),
\qquad 1<d<b,
\]

the refinement releases the two unit residues (d) and (b/d), with only
the multiplicative constraint

\[
d(b/d)=b\in H.
\]

Membership of a product in (H) does not imply membership of either
factor. Root-layer saturation controls the residues used as roots; it says
nothing about integer divisors of the chosen representatives. The
(N=341) certificate below realizes a global index (15), so in particular
there is no inherited index-two bound and the local indices need not agree.

For the post-refinement screen, the subgroup (H_r=langle g_r\rangle) has
order (M). Since (G_r) is cyclic and (M\mid(r-1)), it is the unique
subgroup of order (M), and it is exactly the solution set of

\[
y^M=1\quad\text{in }G_r.
\]

Therefore

\[
r\mid d^M-1
\quad\Longleftrightarrow\quad
d_r\in H_r.
\tag{G}
\]

As (N=pq), (G) proves the complete classification

\[
\gcd(d^M-1,N)=
\begin{cases}
N,&d_p\in H_p\text{ and }d_q\in H_q,\\
p\text{ or }q,&d\text{ is locally internal at exactly one prime},\\
1,&d_p\notin H_p\text{ and }d_q\notin H_q.
\end{cases}
\]

The middle case is a factor. In the last case, adjoining (d_r) strictly
enlarges each local subgroup. In the first case, the screen checks only
local membership. It does not compare the two local exponents. For example,
when (M>1), CRT can choose (d_p=1) and (d_q=g_q); then (d^M=1) at
both primes but (d\notinlangle g\rangle) globally. The screen costs one
modular exponentiation and one gcd, as stated.

## 5. Independent reconstruction of the (N=341) certificate

All calculations in this section were recomputed from the displayed
integers.

### Old group and transcript

Successive powers of (70) modulo (341) are

\[
1,70,126,295,190,1.
\]

Modulo (11), (70=4) has order five. Modulo (31), (70=8) has order
five. Thus its order modulo (341) is five and the displayed list is the
complete old group.

With (t=467),

\[
t^2\cdot70=15{,}266{,}230
=1+44{,}769\cdot341
=2\cdot5\cdot7\cdot467^2.
\]

The single record therefore has the nonzero parity vector contributed by
(70=2\cdot5\cdot7). With only one record, the sole nonempty selection has
that nonzero parity, so there is no parity dependency. Also

\[
\gcd(467,70)=1,
\qquad
467\cdot295=1+109\cdot341.
\]

Hence the displayed decorated residue is ((1,295)), the old square part
does not split (70), and (z=295) is (t^{-1}) modulo (341). The least
positive residue of (t) is (s=126), and (zs\equiv1\pmod{341}).

Direct calculation gives

\[
295^2\equiv70,
\qquad
295\cdot126\equiv1,
\qquad
126^2\equiv190\equiv70^4
\pmod{341},
\]

and

\[
126^2\cdot70=1{,}111{,}320
=1+3{,}259\cdot341.
\]

The direct gcd screens are

\[
\gcd(295-126,341)=
\gcd(295+126,341)=
\gcd(70-1,341)=
\gcd(70+1,341)=1.
\]

Scanning the complete ordered group gives exactly

\[
(\gcd(126-h,341))_{h\in H}=(1,1,341,1,1),
\]

\[
(\gcd(295-h,341))_{h\in H}=(1,1,1,341,1).
\]

Equivalently, (126=70^2) and (295=70^3). Thus the root layer is wholly
internal and (langle H,126,295\rangle=H).

### Refinement and subgroup sizes

The canonical integer representative nevertheless gives

\[
\gcd(70,126)=14,
\qquad 70=14\cdot5.
\]

Both new blocks are units modulo (341). Their local generated groups can
be computed exactly.

Modulo (11), (70=4), (14=3=4^4), and (5=4^2). Hence

\[
|H_{11}|=|H'_{11}|=5.
\]

Modulo (31), (3) has order (30), and

\[
70=8=3^{12},
\qquad 14=3^{22},
\qquad 5=3^{20}.
\]

Therefore

\[
H'_{31}=\langle3^{22},3^{20}\rangle=\langle3^2\rangle,
\qquad |H'_{31}|=15,
\]

while (|H_{31}|=5).

It remains to check that the global group is the full product of these two
local images, rather than a smaller diagonal subgroup. Relative to
(C_5\times C_{15}), the generators (14) and (5) have exponent vectors

\[
a=(4,11),
\qquad b=(2,10).
\]

The element (b) has order (15), and

\[
a-2b=(0,6)
\]

has order (5). Their cyclic subgroups intersect trivially: a multiple of
(b) with first coordinate zero has second coordinate in
({0,5,10}), whereas a multiple of (6) in (C_{15}) lies in
({0,3,6,9,12}). Thus

\[
|H'|=15\cdot5=75.
\]

Since (70=14\cdot5), (H\le H'). The exact sizes and indices are therefore

\[
\begin{array}{c|ccc}
&\text{global}&\bmod 11&\bmod31\\ \hline
H&5&5&5\\
H'&75&5&15\\
[H':H]&15&1&3.
\end{array}
\]

Finally,

\[
\gcd(14\pm1,341)=\gcd(5\pm1,341)=1,
\]

but

\[
14^5\equiv67\pmod{341},
\qquad
\gcd(14^5-1,341)=\gcd(66,341)=11,
\qquad
\gcd(14^5+1,341)=1.
\]

This verifies every displayed certificate value. It also witnesses the
claimed separation: the modular roots add no element to (H), while the
integer refinement expands the named global subgroup by index (15) and
then exposes a factor through the already public exponent (M=5).

## 6. Consequence and scope

The section application uses only the stated boundary property
(s_v^2\in H). Once that property is available, every inverse section
representative is an input to the explicit theorem. The compact theorem is
applicable only when each tested root separately has a presentation
(s_v^2=g^{a_v}) with (gcd(a_v,M)=1), in addition to the certified
common-order hypotheses.

The conclusions are therefore exactly layer-local:

1. the frozen root residues either reveal a factor, add no coset, or add
   one common index-two coset; and
2. gcd-free integer refinement can independently release residues outside
   that root-generated subgroup.

The finite example is existential. It proves capability, not frequency or
necessity. Neither the general proof nor the example supplies a density of
useful refinements, a bound on repeated named-subgroup growth, an all-input
source, or a quasipolynomial factoring algorithm. Adaptive root layers,
forced hidden alignment disagreement, and refinement-created generators
remain possible ingredients for a later theorem; none is proved sufficient
here.
