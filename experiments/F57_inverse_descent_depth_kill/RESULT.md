# F57 inverse-descent depth kill

**Status:** promoted as P67/X60 after a failed first hostile audit, a passing
fresh whole-artifact re-audit, and strict proof-blind reconstruction. The first
audit found a Farey-orientation sign error, a zero-transition proof edge case,
and an understated description of the slow family's factoring difficulty. All
are repaired below. No computation was run.

The closest prior route is F43/P62. It proved the exact divisor fibres, the
bound $N^{1/2+o(1)}$, a logarithmic slow-chain family, and the failure of a
two-step halving rule. This report differs materially in three ways:

1. it gives an elementary bound $L<\sqrt{2N\log N}$ with no divisor-function
   factor;
2. it gives an exact law joining every two consecutive steps;
3. it puts the logarithmic slow chain on nonsquare composite inputs with two
   balanced explicit factor blocks.

It does **not** prove or refute a $\operatorname{poly}(\log N)$ depth bound.
It also does not give a factoring algorithm.

## 1. Setup

Let $u_0,u_1,\ldots,u_L$ be a trajectory. Each source state
$u_i$, for $0\le i<L$, is a unit modulo $N$, and

\[
u_{i+1}=D_N(u_i)=\frac{u_i v_i-1}{N},
\]

where $v_i$ is the canonical inverse of $u_i$ in
$\{1,\ldots,N-1\}$. Stop when the trajectory reaches $1$ or a proper
nonunit. Put

\[
r_i=u_i-u_{i+1},
\qquad
t_i=N-v_i.
\]

The one-step identity is

\[
\boxed{N r_i=u_i t_i+1.}
\tag{1}
\]

Thus $r_i$ is the canonical inverse of $N$ modulo $u_i$. Both $r_i$ and
$t_i$ are in $\{1,\ldots,N-1\}$.

## 2. A sharper unconditional depth bound

### Theorem

Every such trajectory satisfies

\[
\boxed{\frac{L(L+1)}2<N\log N.}
\tag{2}
\]

In particular,

\[
\boxed{L<\sqrt{2N\log N}.}
\tag{3}
\]

This theorem applies whether the last state is $1$ or a proper nonunit.

### Proof

The case $L=0$ is immediate. Assume $L\ge1$.

Equation (1) gives

\[
\frac{r_i}{u_i}
=\frac{t_i}{N}+\frac1{Nu_i}.
\tag{4}
\]

Since $u_{i+1}=u_i-r_i$ and $0<r_i/u_i<1$,

\[
\log\frac{u_i}{u_{i+1}}
=-\log\left(1-\frac{r_i}{u_i}\right)
\ge \frac{r_i}{u_i}
>\frac{t_i}{N}.
\]

The logarithms telescope. Therefore

\[
\sum_{i=0}^{L-1}t_i
<N\log\frac{u_0}{u_L}
<N\log N.
\tag{5}
\]

The values $t_i$ are distinct. Indeed, inversion permutes the units modulo
$N$, the states $u_i$ are distinct, and $t_i=N-v_i$. Hence the sum of the
$L$ positive distinct integers $t_i$ is at least $1+2+\cdots+L$. Combining
this with (5) proves (2) and (3). $\square$

This removes the maximal-divisor factor from P62. It is still exponential in
the binary input length.

## 3. Exact law for adjacent steps

Assume that $u_{i+1}$ is also a unit, so the next transition exists. Write
$r=r_i$, $t=t_i$, $r'=r_{i+1}$, and $t'=t_{i+1}$. Define

\[
\delta_i=r t'-r't.
\]

Then

\[
\boxed{\delta_i\in\mathbb Z_{>0},}
\tag{6}
\]

and the following two exact identities hold:

\[
\boxed{
\delta_i u_i=r^2t'+r'-r,
}
\tag{7}
\]

\[
\boxed{
N\delta_i=rtt'+t'-t.
}
\tag{8}
\]

### Proof

The two step equations are

\[
Nr=u_i t+1,
\qquad
Nr'=(u_i-r)t'+1.
\]

Cross-multiplication gives (7). Its right side is positive because

\[
r^2t'+r'-r=r(rt'-1)+r'>0.
\]

Thus $\delta_i$ is a positive integer. Multiplying the definition of
$\delta_i$ by $N$ and substituting the two step equations gives (8).
$\square$

Consequently, the reduced fractions

\[
\frac{t_0}{r_0},\frac{t_1}{r_1},\ldots
\]

strictly increase. Since $\delta_i\ge1$, equation (8) gives

\[
r_i t_i t_{i+1}+t_{i+1}\ge N+1.
\]

Thus, if $r_i,t_i,t_{i+1}\le B$, then $B^3+B\ge N+1$. This is a real local
restriction, but it has not yielded a bit-polynomial global count.

## 4. Exact Farey structure, and why it does not finish the proof

Equation (1) gives

\[
\frac{N}{u_i}-\frac{t_i}{r_i}=\frac1{u_i r_i}.
\]

Also, with $u_{i+1}=u_i-r_i$ and $v_i=N-t_i$,

\[
\frac{v_i}{u_{i+1}}-\frac{N}{u_i}
=\frac1{u_i u_{i+1}}.
\]

The vectors $(t_i,r_i)$ and $(v_i,u_{i+1})$ have absolute determinant one.
In left-parent/right-parent orientation,

\[
v_i r_i-t_i u_{i+1}=1.
\]

Their sum is $(N,u_i)$. Thus they are the two Farey parents of $N/u_i$.

This does not turn the trajectory into the Euclidean algorithm. A Farey or
continued-fraction descent would continue from
$v_i/u_{i+1}$. The actual next step resets the numerator and continues from
$N/u_{i+1}$. The reset is the missing point in a direct Euclidean-height
proof. No decrease of continued-fraction length follows from the parent
identity alone.

## 5. A nonsquare balanced composite slow family

Let

\[
M_L=\operatorname{lcm}(2,3,\ldots,L+1),
\]

and set

\[
A_L=M_L^2+M_L+1,
\qquad
B_L=(M_L+1)^2,
\qquad
N_L=A_LB_L.
\]

Both factors are $1$ modulo $M_L$, so $N_L\equiv1\pmod u$ for every
$2\le u\le L+1$. Therefore

\[
D_{N_L}(u)=u-1
\]

throughout the exact trajectory

\[
L+1\longrightarrow L\longrightarrow\cdots\longrightarrow2
\longrightarrow1.
\tag{9}
\]

Every displayed state is a unit modulo $N_L$ because
$N_L\equiv1\pmod u$.

These inputs are composite and nonsquare. Indeed,
$\gcd(A_L,B_L)=1$, while $A_L$ lies strictly between $M_L^2$ and
$(M_L+1)^2$, so $A_L$ is not a square. The two displayed factor blocks are
balanced:

\[
1<\frac{B_L}{A_L}<2.
\]

The standard estimate
$\log\operatorname{lcm}(1,\ldots,L+1)=\Theta(L)$ gives

\[
\log N_L=\Theta(L).
\]

Thus the worst-case unit-state depth is at least a constant times $\log N$,
even for nonsquare composite inputs with balanced factor blocks. These inputs
are exceptionally easy even when only $N_L$ is given. Since $M_L$ is even,
put

\[
x=\frac{A_L+B_L}{2},\qquad y=\frac{B_L-A_L}{2}=\frac{M_L}{2}.
\]

Then $N_L=x^2-y^2$ and $(x-1)^2<N_L<x^2$. Hence
$x=\lceil\sqrt{N_L}\rceil$, so the first square test in Fermat's method finds
$A_L=x-y$ and $B_L=x+y$. Also, $B_L$ contains a repeated factor. This is not
a hard semiprime family.

The same family rules out every uniform fixed-factor contraction over a
sublogarithmic block. More precisely, let $h(N)$ be any nonnegative
integer-valued function with $h(N)=o(\log N)$. Along (9), for all sufficiently
large $L$,

\[
\frac{u_{h(N_L)}}{u_0}
=\frac{L+1-h(N_L)}{L+1}\longrightarrow1.
\]

Therefore, for every fixed $c<1$, no theorem can guarantee
$u_{h(N)}\le c u_0$ after $h(N)=o(\log N)$ transitions on all inputs.

## 6. Verdict and open gap

### Proved here

- The depth is always less than $\sqrt{2N\log N}$.
- Consecutive steps satisfy the positive-determinant laws (7) and (8).
- The Farey-parent interpretation is exact, but the numerator reset prevents
  a direct Euclidean descent.
- Nonsquare balanced composite inputs can have unit-state depth
  $\Theta(\log N)$.

### Not proved

- No family with depth superpolynomial in $\log N$ is constructed.
- No $\operatorname{poly}(\log N)$ upper bound is proved.
- The adjacent determinant law has not been converted into a global potential.
- A depth theorem alone would only make the trajectory cheap to generate. It
  would not prove that the trajectory contains a factor-bearing event or a
  successful batch relation.

The surviving depth question is exact: either prove a global bit-polynomial
count, possibly by combining many identities (8) or by finding another
invariant, or construct one infinite family whose depth exceeds every fixed
polynomial in $\log N$. Reverse divisor fibres, finite depth data, and one-step
Farey structure do not settle this choice.
