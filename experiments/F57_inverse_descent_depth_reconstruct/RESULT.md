# Inverse-descent depth: proof-blind reconstruction

Let
\[
u_0,u_1,\ldots,u_L
\]
be a trajectory with (L) transitions. Thus, for (0\le i<L), the state (u_i) is a unit with (1<u_i<N), (v_i\in\{1,\ldots,N-1\}) is its least positive inverse modulo (N), and
\[
u_{i+1}=\frac{u_i v_i-1}{N}.
\]
The last state is either (1) or a proper nonunit. Define
\[
r_i=u_i-u_{i+1},\qquad t_i=N-v_i.
\]
All logarithms below can use any fixed base. Natural logarithms are used in the formulas.

## 1. The descent identity and the global length bound

Because (v_i=N-t_i),
\[
N u_{i+1}=u_i(N-t_i)-1.
\]
Consequently,
\[
\boxed{N r_i=u_i t_i+1}. \tag{1}
\]
Here (t_i\ge1). Also (u_{i+1}\ge1), so (1) shows that every transition is a strict descent and
\[
1\le r_i<u_i.
\]

The values (t_0,\ldots,t_{L-1}) are distinct. Indeed,
\[
u_i t_i\equiv-1\pmod N,
\]
so (t_i) is a unit modulo (N), and the map (u_i\mapsto t_i\equiv-u_i^{-1}\pmod N) is injective on the representatives (1,\ldots,N-1). The states (u_i) are distinct because they strictly decrease. Hence
\[
\sum_{i=0}^{L-1}t_i\ge 1+2+\cdots+L=\frac{L(L+1)}2. \tag{2}
\]

For (L\ge1), divide (1) by (Nu_i) and use (0<r_i/u_i<1):
\[
\frac{t_i}{N}<\frac{r_i}{u_i}
   <-\log\!\left(1-\frac{r_i}{u_i}\right)
   =\log\frac{u_i}{u_{i+1}}.
\]
Summation and telescoping give
\[
\frac{L(L+1)}{2N}
\le \frac1N\sum_{i=0}^{L-1}t_i
<\sum_{i=0}^{L-1}\frac{r_i}{u_i}
<\log\frac{u_0}{u_L}
<\log N.
\]
Therefore
\[
\boxed{\frac{L(L+1)}2<N\log N},
\qquad
\boxed{L<\sqrt{2N\log N}}. \tag{3}
\]

If (L=0), both conclusions hold directly because (N>1). If (u_L) is a proper nonunit, the proof is unchanged: it uses only (u_L\ge1), and it never assigns an inverse to the terminal state.

## 2. Consecutive transitions and the exact local obstruction

Suppose both transitions (i) and (i+1) exist. Write temporarily
\[
u=u_i,\quad r=r_i,\quad t=t_i,\quad r'=r_{i+1},\quad s=t_{i+1}.
\]
Then
\[
\delta_i=rs-r't
\]
is an integer. From (1) at the two consecutive sources,
\[
ut=Nr-1,
\qquad
Nr'=(u-r)s+1.
\]
It follows that
\[
\begin{aligned}
u\delta_i
 &=ur s-r'(Nr-1)\\
 &=r(us-Nr')+r'\\
 &=r(rs-1)+r'\\
 &=r^2s+r'-r,
\end{aligned}
\]
and
\[
\begin{aligned}
N\delta_i
 &=(ut+1)s-\bigl((u-r)s+1\bigr)t\\
 &=rts+s-t.
\end{aligned}
\]
Thus, in the original notation,
\[
\boxed{\delta_i u_i=r_i^2t_{i+1}+r_{i+1}-r_i}, \tag{4}
\]
\[
\boxed{N\delta_i=r_it_it_{i+1}+t_{i+1}-t_i}. \tag{5}
\]
Moreover,
\[
r_i(r_i t_{i+1}-1)+r_{i+1}>0,
\]
so (4) implies (delta_i>0). Hence
\[
\boxed{\delta_i\in\mathbb Z_{\ge1}}. \tag{6}
\]

Equations (4)--(6) give the exact local inequalities
\[
r_i^2t_{i+1}+r_{i+1}-r_i\ge u_i,
\qquad
r_it_it_{i+1}+t_{i+1}-t_i\ge N, \tag{7}
\]
with equality in either inequality exactly when (delta_i=1).

They also give clean integer cube-root obstructions. Set
\[
P_i=\max\{r_i,r_{i+1},t_{i+1}\},
\qquad
Q_i=\max\{r_i,t_i,t_{i+1}\}.
\]
For positive integers bounded by (P_i), the expression on the left of the first inequality in (7) is at most (P_i^3): the upper bound
\[
P_i r_i^2+P_i-r_i
\]
increases with (r_i\le P_i) and equals (P_i^3) at (r_i=P_i). Similarly,
\[
\begin{aligned}
r_it_it_{i+1}+t_{i+1}-t_i
&\le Q_i t_i t_{i+1}+t_{i+1}-t_i\\
&=t_i(Q_i t_{i+1}-1)+t_{i+1}\\
&\le Q_i(Q_i t_{i+1}-1)+t_{i+1}\\
&\le Q_i^3.
\end{aligned}
\]
Therefore the exact integer size consequences are
\[
\boxed{P_i\ge\left\lceil u_i^{1/3}\right\rceil},
\qquad
\boxed{Q_i\ge\left\lceil N^{1/3}\right\rceil}. \tag{8}
\]
In particular, every pair of consecutive unit transitions contains, among (r_i,t_i,t_{i+1}), a quantity at least (lceil N^{1/3}\rceil).

## 3. The local Farey decomposition

At one transition, abbreviate (u'=u_{i+1}), (r=r_i), (t=t_i), and (v=v_i). The defining sums are
\[
t+v=N,
\qquad
r+u'=u.
\]
Also,
\[
rv-tu'=r(N-t)-t(u-r)=Nr-tu=1. \tag{9}
\]
Thus (t/r) and (v/u') are reduced Farey neighbors, in this orientation. Their mediant is
\[
\frac{t+v}{r+u'}=\frac Nu.
\]
Equivalently, the two one-sided determinant identities are
\[
Nr-ut=1,
\qquad
uv-Nu'=1,
\]
so the orientation is exactly
\[
\boxed{\frac{t_i}{r_i}<\frac N{u_i}<\frac{v_i}{u_{i+1}}}. \tag{10}
\]
Hence these are the left and right Farey parents of (N/u_i).

This structure is local. The right parent at step (i) has numerator (v_i) and denominator (u_{i+1}), but the fraction decomposed at step (i+1) is
\[
\frac N{u_{i+1}},
\]
not (v_i/u_{i+1}). The denominator carries over, while the numerator resets to the fixed value (N). Therefore the local parent decompositions do not concatenate into one ordinary Farey or Stern--Brocot path.

## 4. An exact logarithmic-depth family

Fix a positive integer (L), and set
\[
M=\operatorname{lcm}(2,3,\ldots,L+1),
\qquad
A=M^2+M+1,
\qquad
B=(M+1)^2,
\qquad
N=AB.
\]
Expansion gives
\[
N=M^4+3M^3+4M^2+3M+1,
\]
and hence
\[
N-1=M(M^3+3M^2+4M+3). \tag{11}
\]
For each (k\in\{2,\ldots,L+1\}), one has (k\mid M), so (11) gives (N\equiv1\pmod k). In particular, (k) is a unit modulo (N). Define
\[
v_k=N-\frac{N-1}{k}.
\]
This is an integer in ({1,\ldots,N-1}), and
\[
kv_k=kN-(N-1)=N(k-1)+1.
\]
It is therefore the least positive inverse of (k) modulo (N), and
\[
D_N(k)=k-1. \tag{12}
\]
Also (L+1\le M<N). Thus all source states are in the required range, and (12) proves the exact all-unit trajectory
\[
\boxed{L+1\longrightarrow L\longrightarrow\cdots\longrightarrow2\longrightarrow1}, \tag{13}
\]
with exactly (L) transitions.

### Arithmetic shape and immediate Fermat factorization

Both (A) and (B) exceed (1), so (N) is composite. Furthermore,
\[
M^2<A<(M+1)^2=B.
\]
Thus (A) is not a square. Since (B) is a square, (N=AB) is not a square either.

The factors satisfy
\[
B-A=M>0,
\qquad
2A-B=M^2+1>0,
\]
and therefore
\[
\boxed{1<\frac BA<2}. \tag{14}
\]

Because (L\ge1), (M) is even, so (A) and (B) are odd. Put
\[
x=\frac{A+B}{2}=M^2+\frac{3M}{2}+1,
\qquad
y=\frac{B-A}{2}=\frac M2.
\]
Then (x^2-N=y^2). Moreover,
\[
N-(x-1)^2=2x-1-y^2
=\frac{7M^2}{4}+3M+1>0.
\]
Since (N) is nonsquare, this proves
\[
x-1<\sqrt N<x,
\qquad
x=\lceil\sqrt N\rceil.
\]
Therefore the first square test in Fermat's method finds (y^2=x^2-N) and returns
\[
x-y=A,
\qquad
x+y=B. \tag{15}
\]

### Proof that \(\log N=\Theta(L)\)

For completeness, no prime-number theorem is needed. Let
\[
M_n=\operatorname{lcm}(1,2,\ldots,n).
\]
If (m\ge1), then
\[
\binom{2m}{m}\mid M_{2m}.
\]
Indeed, for each prime (p), Legendre's formula writes the valuation of the binomial coefficient as a sum of terms
\[
\left\lfloor\frac{2m}{p^a}\right\rfloor
-2\left\lfloor\frac m{p^a}\right\rfloor\in\{0,1\},
\]
and there are at most (lfloor\log_p(2m)\rfloor=v_p(M_{2m})) nonzero terms. Since the central binomial coefficient is the largest of the (2m+1) coefficients in ((1+1)^{2m}),
\[
M_{2m}\ge\binom{2m}{m}\ge\frac{2^{2m}}{2m+1}. \tag{16}
\]

For the reverse bound,
\[
M_{2m}\mid M_m\binom{2m}{m}. \tag{17}
\]
To see this prime by prime, the exponent of (p) in (M_{2m}) exceeds its exponent in (M_m) by at most one. If it exceeds it, the new power (p^a) lies in ((m,2m]), and the (p^a)-term in Legendre's formula for the binomial coefficient is (1). Hence (17), and therefore
\[
M_{2m}\le M_m4^m. \tag{18}
\]
Iteration of (18) at powers of two, followed by monotonicity, gives
\[
\log M_n<4n\log2.
\]
Taking (m=\lfloor n/2\rfloor) in (16) gives
\[
\log M_n\ge2m\log2-\log(2m+1).
\]
Thus
\[
\log M_n=\Theta(n). \tag{19}
\]
Here (M=M_{L+1}). Finally, for (M\ge1),
\[
M^4<N\le12M^4,
\]
so
\[
4\log M<\log N\le4\log M+\log12.
\]
Together with (19), this proves
\[
\boxed{\log N=\Theta(L)}. \tag{20}
\]

### Exact obstruction to sublogarithmic contraction

Write the member of the family associated with (L) as (N_L), and start it at (u_0=L+1). From (13), for every integer (j\) with (0\le j\le L),
\[
D_{N_L}^{,j}(u_0)=L+1-j. \tag{21}
\]
Let (h) be any nonnegative integer-valued function such that
\[
h(N_L)=o(\log N_L).
\]
By (20), (h(N_L)=o(L)); hence (h(N_L)\le L) for all sufficiently large (L). Substitution into (21) gives the exact ratio
\[
\frac{D_{N_L}^{,h(N_L)}(L+1)}{L+1}
=1-\frac{h(N_L)}{L+1}
\longrightarrow1. \tag{22}
\]
Consequently, for every fixed contraction factor (c\in(0,1)),
\[
D_{N_L}^{,h(N_L)}(L+1)>c(L+1)
\]
for all sufficiently large (L). Thus no uniform theorem can force a fixed multiplicative contraction of every unit source after (o(\log N)) transitions.

## 5. Exact scope of the conclusions

All four stated claims are true, with the local size consequence made explicit in (7) and (8). Their limits are important.

1. The family gives a worst-case depth lower bound of order (log N). It does **not** disprove a universal (operatorname{poly}(\log N)) depth upper bound. Its depth is itself logarithmic.
2. The family is slow only in the precise contraction sense of (22). It is not a hard factoring family: its factors are part of the construction, and Fermat's method recovers them on its first test.
3. No probability distribution has been specified or analyzed. Therefore there is no success probability, density statement, or success law for general inputs or starting states.
4. The identities and bounds do not constitute a general factoring algorithm. A terminal proper nonunit would expose a factor through its gcd with (N), but no result here guarantees such a terminal state; the explicit family instead terminates at (1).

The proven universal upper bound is (3), the constructed lower bound is (Theta(\log N)), and the gap between them remains open within this reconstruction.
