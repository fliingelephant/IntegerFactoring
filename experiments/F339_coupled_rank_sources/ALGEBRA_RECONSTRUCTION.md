# Independent reconstruction of the N-linked rank jump

Input: `ALGEBRA_STATEMENT_ONLY.md`

Input SHA-256: `afc08f373adabe1f79314fa1d15666ac0d553e4226748d8b2ca6cf67d9ac4df6`

This reconstruction uses only the definitions and declared dependencies in
the input. All residues modulo (L) below are represented in
\(\{0,\ldots,L-1\}\).

## 1. Two rotation-counting observations

Let

\[
T(x)=x+u\pmod L.
\]

Since (L=u+v) and \(\gcd(u,v)=1\), both (u) and (v) are invertible
modulo (L). Thus (T) is one cycle of length (L), and

\[
T^{-1}(x)=x+v\pmod L.
\]

For the rotation (R_h(x)=x+h\pmod L), the number of wraparounds in
(n) steps from (x\in\{0,\ldots,L-1\}) is

\[
\left\lfloor\frac{x+nh}{L}\right\rfloor
   \leq \left\lceil\frac{nh}{L}\right\rceil.
\tag{1}
\]

A step of (T) wraps exactly when its starting point is in
\([v,L-1]\), because (L-u=v). Since (v<m),

\[
B=[m,L-1]\subseteq[v,L-1].
\tag{2}
\]

A step of (T^{-1}) wraps exactly when its starting point is in
\([u,L-1]\). Since (u<m),

\[
B\subseteq[u,L-1].
\tag{3}
\]

Consequently, the number of visits to (B) in any (n)-step forward
(T)-arc is at most \(\lceil nu/L\rceil\). The analogous count in a
forward (T^{-1})-arc is at most \(\lceil nv/L\rceil\).

If a forward (T)-arc of length (n) has both endpoints in (A), its
starting-point list is

\[
x,T(x),\ldots,T^{n-1}(x).
\]

The reverse arc has starting-point list

\[
T^n(x),T^{n-1}(x),\ldots,T(x).
\]

These lists differ only by exchanging the two endpoints, both of which
are in (A). They therefore contain the same number of points of (B).
This permits either (2) or (3) to be used for the same arc.

## 2. Reconstruction of Claim A

From the declared identity \(N=\alpha v+\beta u\),

\[
N=\alpha(u+v)+(\beta-\alpha)u=\alpha L+bu.
\]

Hence

\[
bu\equiv N\pmod L.
\]

As (u) is invertible modulo (L), this proves

\[
q=b\bmod L=Nu^{-1}\bmod L.
\tag{4}
\]

This derivation uses the multiplier \(u^{-1}\); it does not replace the
jump by the generally different residue (N\bmod L). If (q=0), the
specified source returns failure, and no subsequent assertion about an
accepted pair is needed.

Assume (q\ne0). For every sampled (k\in A),

\[
k'=(k+qu)\bmod L=T^q(k).
\]

When both endpoints are in (A), the ordering rule in the statement
always gives

\[
k_1=T^s(k_0),\qquad s=\min(q,L-q),\qquad 1\leq s<L.
\tag{5}
\]

Indeed, this is immediate when (q\leq L/2); when (q>L/2),
\(T^{L-q}(k')=k\), which proves it after reversing the pair.

The full (T)-cycle lists the points of (A), after deletion of the
points of (B), in increasing cyclic rank. Along the arc (5), exactly
(H) of the (s) starting points lie in (B). Therefore exactly
(s-H) of them lie in (A). This is the cyclic rank advance from
(k_0) to (k_1), so

\[
D=(\operatorname{rnk}(k_1)-\operatorname{rnk}(k_0))\bmod m=s-H.
\tag{6}
\]

The endpoints are distinct: (q\ne0) and (u) is invertible modulo
(L). Since both are in (A), the cyclic rank advance satisfies

\[
1\leq s-H\leq m-1.
\tag{7}
\]

The arc has no repeated point and (B) has (d) points, whence

\[
H\leq d.
\tag{8}
\]

It remains to prove the sharper bound involving (Q).

If (b>0), write (b=nL+q) with (n\geq0). Then

\[
Q=\left\lfloor\frac NL\right\rfloor
 =\alpha+nu+\left\lfloor\frac{qu}{L}\right\rfloor.
\]

Because (1\leq q<L) and \(\gcd(u,L)=1\), (qu/L) is not an integer.
Since \(\alpha\geq1\),

\[
Q\geq\left\lceil\frac{qu}{L}\right\rceil.
\]

Equations (1), (2), and (s\leq q) now give

\[
H\leq\left\lceil\frac{su}{L}\right\rceil
 \leq\left\lceil\frac{qu}{L}\right\rceil\leq Q.
\tag{9}
\]

If (b<0), put (c=-b>0). Since \(q=b\bmod L\), write

\[
c=nL+(L-q),\qquad n\geq0.
\]

The symmetric form of the declared identity is

\[
N=\beta L+cv.
\]

Thus

\[
Q=\beta+nv+\left\lfloor\frac{(L-q)v}{L}\right\rfloor
 \geq\left\lceil\frac{(L-q)v}{L}\right\rceil,
\]

where nonintegrality follows from \(1\leq L-q<L\) and
\(\gcd(v,L)=1\). Count (B)-visits on the reverse arc, as justified in
Section 1. Equations (1), (3), and (s\leq L-q) give

\[
H\leq\left\lceil\frac{sv}{L}\right\rceil
 \leq\left\lceil\frac{(L-q)v}{L}\right\rceil\leq Q.
\tag{10}
\]

The case (b=0\pmod L) is exactly the already excluded case (q=0).
Combining (8)--(10) proves

\[
0\leq H\leq\min(d,Q).
\tag{11}
\]

Let \(\delta=\operatorname{rnk}(k_1)-\operatorname{rnk}(k_0)\) as an
ordinary integer. If \(\delta>0\), then \(\delta=D\); if \(\delta<0\),
then \(\delta=D-m=-(m-D)\). Reversing the original sampled pair only
changes the sign. Hence the original gcd argument, up to sign, is one of

\[
D=s-H,\qquad m-D=m-s+H.
\]

It follows from (11) that

\[
M=\{s-h,m-s+h:0\leq h\leq\min(d,Q)\}
\tag{12}
\]

contains a gcd argument for every endpoint-valid coupled pair. It has at
most \(2(\min(d,Q)+1)\) entries. Duplicate entries may be deleted. By
(7), only candidates compatible with \(1\leq s-h<m\) can be realized;
the others may be omitted. As specified, a zero argument, gcd (1), or
gcd (N) is a failure.

For fixed (a,t), (12) is independent of (k). Therefore if any coupled
choice of (k) gives a proper factor, testing the complete menu finds a
proper factor. The converse need not hold because some listed values of
(h) need not occur for any (k). Thus complete-menu success is a
deterministic event for the fixed parameter, whereas the original
attempt has a probability over (k), including the probability that
(k'\notin A). No per-(k) probability formula or source-success lower
bound follows from menu dominance.

For (t=(N-1)/2),

\[
m=(N+1)/2>N/2,
\]

so (m\leq L\leq N) implies (Q=1). The menu has at most four entries.
For (t=\lfloor(N-1)/8\rfloor), whenever this value satisfies the global
premise (t\geq1),

\[
m=\left\lceil\frac N8\right\rceil>N/8
\]

because (N) is odd. Hence (L>N/8), (Q\leq7), and the menu has at
most sixteen entries. The argument is pointwise in (a,t); it uses no
small-(d), adjacency, or distributional hypothesis. Since (Q) is not
uniformly bounded for arbitrary (t), this establishes no uniform
small-menu cost outside the displayed windows.

The declared inverse, floor-sum rank formula, and extrema search make all
quantities in this argument public and exact. The sorted arrays define
the mathematical objects; the runtime sampler need not construct them.
The conclusion does not remove any of the declared charges for parameter
generation, setup, randomness, rejected endpoints, arithmetic, or gcd
verification.

## 3. Reconstruction of Claim B

Write (N=2t+1), so (m=t+1), and let

\[
h=a^{-1}\bmod N\in\{1,\ldots,N-1\},\qquad r=\min(h,N-h).
\]

Then (1\leq r\leq t) and (r) is a unit modulo (N). There are two
cases.

Suppose (ar\equiv1\pmod N). Then (z(r)=1), so

\[
\alpha=1,\qquad u=r.
\]

Put \(s_0=\lfloor t/r\rfloor\). For (1\leq j\leq s_0), the index
whose residue would be (N-j) is

\[
-rj\bmod N=N-rj\geq N-t=t+1,
\]

so it is outside the sampled index interval. On the other hand,

\[
t<r(s_0+1)\leq t+r\leq2t=N-1.
\]

Consequently

\[
v=N-(s_0+1)r\in[1,t],\qquad z(v)=N-(s_0+1),
\]

and no smaller positive deficiency from (N) occurs. Thus

\[
\beta=s_0+1,\qquad v=N-(s_0+1)r.
\tag{13}
\]

Suppose instead that (ar\equiv-1\pmod N). The same argument with the
two ends exchanged gives

\[
\beta=1,\qquad v=r,\qquad
\alpha=s_0+1,\qquad u=N-(s_0+1)r.
\tag{14}
\]

Both (13) and (14) give

\[
|\beta-\alpha|=s_0,\qquad L=N-s_0r.
\tag{15}
\]

Assume (r\geq2). Since (rs_0\leq t),

\[
2s_0\leq rs_0\leq t<L.
\]

Thus (s_0<L/2). From (b=\pm s_0), the two possible residues (q)
are (s_0) and (L-s_0), and the actual centered length is

\[
s=\min(q,L-q)=s_0.
\tag{16}
\]

Section 2 gives (Q=1) in the half-orbit window. Therefore the direct
menu is contained in

\[
\{s,s-1,m-s,m-s+1\}.
\]

Since (2m=N+1) and (N) is odd,

\[
\gcd(m-s,N)=\gcd(2s-1,N),
\]

and

\[
\gcd(m-s+1,N)=\gcd(2s-3,N).
\]

It follows that the four gcd arguments

\[
s,\qquad s-1,\qquad 2s-1,\qquad 2s-3
\tag{17}
\]

dominate the direct menu, including the case (d=0), when the direct
menu is smaller. They require (r) and (s=\lfloor t/r\rfloor), but no
extrema search.

Euclidean division gives

\[
N=2rs+R,
\]

where initially (1\leq R\leq2r). The left side is odd and (2rs) is
even, so (R) is odd; hence (R\ne2r), and

\[
1\leq R<2r.
\tag{18}
\]

Because (r) and (2r) are units modulo the odd integer (N),

\[
\begin{aligned}
\gcd(s,N)&=\gcd(R,N),\\
\gcd(s-1,N)&=\gcd(R+2r,N),\\
\gcd(2s-1,N)&=\gcd(R+r,N),\\
\gcd(2s-3,N)&=\gcd(R+3r,N).
\end{aligned}
\tag{19}
\]

For example, the first line follows by multiplying (s) by the unit
(2r) and using (2rs\equiv-R\pmod N); the other lines are identical.
Thus one modular inverse gives (r), one quotient gives (s), and four
verified gcds evaluate the dominating menu (17) on the (r\geq2)
branch.

If (r=1), then (a\equiv1) or (-1\pmod N). Here (s_0=t),

\[
L=N-t=t+1=m,\qquad q\in\{1,L-1\},\qquad s=1,\qquad d=0.
\]

The actual direct menu is \(\{1,m-1\}=\{1,t\}\), and

\[
\gcd(t,N)=\gcd(2t,N)=\gcd(N-1,N)=1.
\]

It has no proper gcd. Substitution of the raw quotient (s_0=t) into
(17) would instead test

\[
t,\qquad t-1,\qquad N-2,\qquad N-4.
\]

In particular,

\[
\gcd(t-1,N)=\gcd(N-3,N)=\gcd(3,N),
\]

where multiplication by (2) is harmless because (N) is odd. Thus
that substitution can expose a factor (3), but it is a different
source. Claims C and D below use the actual factor-free (r=1) branch
and use (17) only for (r\geq2).

## 4. Reconstruction of Claim C

Let (N=pq) for distinct odd primes (p\leq q), and fix
\(\ell\in\{p,q\}\). Only unit values of (r) arise from the stated
source. The (r=1) branch never succeeds, so assume (r\geq2).

Associate the four entries in (17), in their displayed order, with

\[
c=0,2,1,3.
\]

By (19), their gcds with (N) equal the gcds of

\[
E_c=R+cr=N-(2s-c)r
\tag{20}
\]

with (N). Suppose a particular entry accepts a proper divisor divisible
by \(\ell\). Then \(\ell\mid E_c\). Also

\[
0<E_c<(2+c)r\leq5r.
\]

Thus (E_c\geq\ell) and

\[
r>\ell/5.
\tag{21}
\]

Because this (r) is a unit, \(\ell\nmid r\). Reducing (20) modulo
(\ell) gives

\[
2s-c\equiv0\pmod\ell.
\tag{22}
\]

For an entry that accepts a proper divisor, (2s-c) is not zero. The
only zero possibility is (c=2,s=1), corresponding to the rejected gcd
of the zero entry (s-1) with (N). The possible negative value
\(c=3,s=1\) is \(-1\), which is not divisible by the odd prime \(\ell\).
Hence (22) implies

\[
2s-c\geq\ell,\qquad s\geq\ell/2.
\tag{23}
\]

For each fixed (c), equation (22) places (s) in one residue class
modulo \(\ell\), since \(2\) is invertible modulo \(\ell\). From (21),

\[
s=\left\lfloor\frac tr\right\rfloor
 <\frac{5t}{\ell}<\frac{5N}{2\ell}.
\]

The number of possible (s) in that one residue class is therefore at
most

\[
\left\lfloor\frac{5N}{2\ell^2}\right\rfloor+1.
\tag{24}
\]

For fixed (s), all integers (r) with \(\lfloor t/r\rfloor=s\) lie
in

\[
\frac{t}{s+1}<r\leq\frac ts.
\]

This interval has length (t/(s(s+1))). By (23), its number of integer
points is at most

\[
\left\lfloor\frac{2N}{\ell^2}\right\rfloor+1.
\tag{25}
\]

In (25) one may count nonunit (r)'s as well: (22) was derived for an
eligible successful unit, after which the whole quotient fiber is only a
counting superset.

Multiplying (24) and (25), then summing over the four possible entries,
proves the exact bound

\[
B_\ell=
4\left(\left\lfloor\frac{5N}{2\ell^2}\right\rfloor+1\right)
 \left(\left\lfloor\frac{2N}{\ell^2}\right\rfloor+1\right).
\tag{26}
\]

Inversion permutes the units modulo (N). Folding an inverse (h) to
\(r=\min(h,N-h)\) is exactly two-to-one: the two preimages of each unit
(r\in[1,t]) are (r) and (N-r). Therefore at most

\[
2(B_p+B_q)
\]

unit parameters (a) have a successful complete menu. A proper divisor
of the square-free semiprime (pq) is divisible by (p) or by (q), so
the union bound loses no other case. For uniform (a) on the units,

\[
\Pr(\text{the complete Claim B menu succeeds})
 \leq \min\left(1,\frac{2(B_p+B_q)}{\varphi(N)}\right).
\tag{27}
\]

If (q/p\leq C) for a fixed (C), then (N/p^2\leq C) and
(N/q^2\leq1). Thus (B_p+B_q) is bounded by a constant depending only
on (C). Also

\[
\varphi(N)=(p-1)(q-1)\geq\frac49N
\]

for odd primes. Equation (27) is consequently \(O_C(1/N)\).

This probability is over a uniform unit parameter (a) and concerns
success of its entire menu. It is not the per-\(k\) probability of the
coupling in Claim A. Screening a generated nonunit can itself reveal a
factor, but such generation-screen outputs are excluded by conditioning
on units. The cardinality argument gives no comparable probability bound
for an arbitrary biased law on the eligible parameters.

## 5. Reconstruction of Claim D

Let (N) be any odd composite integer with least prime divisor (P),
and suppose (5H\leq P). Since (N/P) has no prime divisor below (P),

\[
N\geq P^2\geq25H^2.
\tag{28}
\]

Let

\[
a=xy^{-1}\pmod N,\qquad 1\leq x,y\leq H,
\]

with (x,y) units. If (h=a^{-1}\bmod N), then

\[
xh\equiv y\pmod N.
\]

For (r=\min(h,N-h)), there are an integer (K\geq0) and a sign such
that

\[
xr=KN+y\quad\text{or}\quad xr=KN-y.
\tag{29}
\]

The minus sign has (K\geq1); when (K=0), only the plus sign is
possible.

If (r=1), the special branch in Section 3 has no proper gcd. Assume
(r\geq2).

First suppose (K=0). Then (29) says (xr=y), so (r\leq H). For each
(c\in\{0,1,2,3\}), (18) gives

\[
0<R+cr<5r\leq5H\leq P.
\]

Thus every residual in (19) is a positive integer smaller than the least
prime divisor of (N), and hence is coprime to (N). None of the four
menu entries has a proper gcd.

Now suppose (K\geq1). For the plus sign in (29),

\[
\frac Nr=\frac{x}{K}-\frac{y}{Kr}<\frac{x}{K}\leq x.
\tag{30}
\]

For the minus sign, (28) gives

\[
r=\frac{KN-y}{x}\geq\frac{N-H}{H}\geq25H-1>H\geq y/K.
\]

Therefore

\[
\frac Nr=\frac{x}{K}+\frac{y}{Kr}<\frac{x}{K}+1\leq x+1.
\tag{31}
\]

Since (s=\lfloor t/r\rfloor<N/(2r)), both (30) and (31) imply, using
integrality in the latter case,

\[
2s\leq x\leq H<P.
\tag{32}
\]

Every nonzero member of

\[
\{s,s-1,2s-1,2s-3\}
\]

then has absolute value below (P), so it is coprime to (N). The only
possible zero is (s-1) when (s=1), whose gcd is (N) and is rejected.
Thus the actual half-orbit menu has no proper factor in every case.

By the menu dominance proved in Section 2, a proper gcd from any
endpoint-valid half-orbit coupled pair would also occur in the Claim B
menu. Therefore the selected half-orbit coupling has no proper factor
either.

The quantifiers here cover every odd composite (N), including prime
powers and repeated factors, but only the stated unit branch and the
stated observable. Factors found while screening nonunit (x) or (y)
belong to source generation and are separate outputs. The unknown (P)
is used only in the proof; the runtime does not need it. Nothing in the
argument extends the conclusion to larger heights, different windows,
different jumps, or different observables.

## 6. Reconstruction result

All conclusions in Claims A--D follow from the stated definitions and
declared dependencies. No additional hypothesis, proof gap, or
counterexample was found. The (q=0) and (r=1) branches are essential:
the former is a stipulated failure, while replacing the latter's actual
centered length by the raw quotient changes the source and can introduce
the separate factor-\(3\) gcd.
