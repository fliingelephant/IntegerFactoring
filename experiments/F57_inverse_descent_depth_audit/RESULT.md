# Hostile audit of F57: inverse-descent depth

## Disposition

I audited
`experiments/F57_inverse_descent_depth_kill/RESULT.md` at SHA-256

```text
a5e9c5111021e5c8dbd69573003ece2df9f73de0a3b1e4676916058c4c6695bf
```

I compared it with the full F43 candidate and promoted P62. This was a
proof-only audit. I ran no computation and used no public search.

**Verdict: FAIL AS WRITTEN, with the central results intact.** The uniform
depth bound, both adjacent-step identities, the Farey-parent relation, and the
nonsquare balanced slow family are correct. The submitted version has one
exact orientation error: in the order in which it lists the two Farey-parent
vectors, their determinant is $-1$, not $1$. Its strict telescoping line also
fails for the allowed zero-transition case, although the theorem is then
trivial. These are local repairs, but the current exact version should not
advance to reconstruction.

The revision should also replace “factor-free” by the precise statement
“all displayed states are units modulo $N_L$.” The family is exceptionally
easy even when only $N_L$ is given: Fermat's method finds the displayed
factor blocks on its first square test. Thus “factor-free” must not suggest a
hard family or a transcript with no usable information.

## 1. One-step setup and terminal states

For a source state $u_i>1$, let $v_i$ be its canonical inverse modulo $N$,
let $u_{i+1}=(u_iv_i-1)/N$, and put

\[
r_i=u_i-u_{i+1},\qquad t_i=N-v_i.
\]

Then

\[
Nr_i=N u_i-(u_iv_i-1)=u_i(N-v_i)+1=u_it_i+1.
\tag{A1}
\]

Because $1\le v_i<N$, one has $1\le t_i<N$. Also $u_iv_i$ is a positive
integer congruent to $1$ modulo $N$. It cannot equal $1$ when $u_i>1$, so
$u_iv_i\ge N+1$ and $u_{i+1}\ge1$. Equation (A1) then gives
$1\le r_i<u_i<N$. Hence $r_i$ is exactly the canonical inverse of $N$
modulo $u_i$, as claimed.

This argument still works for the last transition when $u_{i+1}$ is a proper
nonunit. The proof does not apply inversion to that terminal state. Thus a
nonunit endpoint causes no hidden gap.

There is one edge case to state separately. The setup permits $L=0$, for
example when $u_0=1$. In that case the theorem is immediate, but the draft's
line

\[
0=\sum_i t_i<N\log(u_0/u_L)=0
\]

is false. The proof should begin, “The case $L=0$ is immediate; assume
$L\ge1$.” No theorem statement needs to change.

## 2. The depth bound is correct and uniform

For $L\ge1$, (A1) gives

\[
\frac{r_i}{u_i}=\frac{t_i}{N}+\frac1{Nu_i}>\frac{t_i}{N}.
\]

Since $0<r_i/u_i<1$,

\[
\log\frac{u_i}{u_{i+1}}
=-\log\!\left(1-\frac{r_i}{u_i}\right)
\ge\frac{r_i}{u_i}>\frac{t_i}{N}.
\]

Summing over the source states gives

\[
\sum_{i=0}^{L-1}t_i
<N\log\frac{u_0}{u_L}<N\log N.
\tag{A2}
\]

The second strict inequality follows from $u_0<N$ and $u_L\ge1$.

The distinctness argument remains valid when the trajectory ends at a
nonunit. Every source $u_0,\ldots,u_{L-1}$ is a unit. These source states are
distinct because they strictly decrease. Inversion is a permutation of the
unit residues, so the $v_i$ are distinct, and therefore the $t_i=N-v_i$ are
distinct. They are positive integers, hence

\[
\sum_{i=0}^{L-1}t_i\ge1+2+\cdots+L=\frac{L(L+1)}2.
\]

Combining this with (A2) proves

\[
\frac{L(L+1)}2<N\log N,
\qquad
L<\sqrt{2N\log N}.
\]

This is a genuine all-input improvement over the P62 derivation. P62 groups
equal decrements and pays a maximal-divisor factor. F57 instead uses the
distinct inverse labels $t_i$ and removes that factor. The result is still
exponential in the bit length, so the draft correctly denies a polynomial
runtime conclusion.

## 3. Both adjacent identities and positivity are correct

Write $u=u_i$, $r=r_i$, $t=t_i$, $r'=r_{i+1}$, and $t'=t_{i+1}$.
When $u-r=u_{i+1}$ is also a unit, the two equations are

\[
Nr=ut+1,
\qquad
Nr'=(u-r)t'+1.
\tag{A3}
\]

For $\delta=rt'-r't$, direct elimination gives

\[
\begin{aligned}
u\delta
&=urt'-ur't\\
&=r^2t'+r'-r,
\end{aligned}
\tag{A4}
\]

and

\[
\begin{aligned}
N\delta
&=(ut+1)t'-((u-r)t'+1)t\\
&=rtt'+t'-t.
\end{aligned}
\tag{A5}
\]

The right side of (A4) is

\[
r(rt'-1)+r'>0,
\]

because $r,t',r'$ are positive integers. Thus $\delta$ is a positive
integer. It follows that $t'/r'>t/r$, so the stated strict increase is
correct.

The phrase “cannot simultaneously have very small” is informal but has an
exact valid reading. Since $\delta\ge1$, (A5) implies

\[
rtt'+t'=N\delta+t\ge N+1.
\]

For example, if $r,t,t'\le B$, then $B^3+B\ge N+1$. A revision should use
this precise consequence if it wants that sentence to carry mathematical
weight.

## 4. Farey parents: conclusion correct, ordered determinant sign wrong

The two displayed difference identities are exact:

\[
\frac{N}{u}-\frac{t}{r}=\frac1{ur},
\qquad
\frac{v}{u-r}-\frac{N}{u}=\frac1{u(u-r)}.
\]

They show the orientation

\[
\frac tr<\frac Nu<\frac v{u-r}.
\]

Also

\[
(t,r)+(v,u-r)=(N,u).
\]

However, for the ordered vectors exactly as the draft lists them,

\[
\det\!\begin{pmatrix}t&v\\ r&u-r\end{pmatrix}
=t(u-r)-vr=-1,
\tag{A6}
\]

not $1$. Equivalently, in left-parent/right-parent orientation,

\[
vr-t(u-r)=1.
\]

Thus their absolute determinant is one, and they really are the two reduced
Farey parents of $N/u$. The parent theorem survives; only the submitted sign
claim fails. The clean replacement is: “They have absolute determinant one;
with the left parent first, $vr-t(u-r)=1$.”

The numerator-reset limitation is real. The parent with denominator
$u_{i+1}$ is $v_i/u_{i+1}$, but the next trajectory center is
$N/u_{i+1}$. Hence the next step does not continue down that Farey edge, and
the parent identity alone gives no continued-fraction-length decrease. The
draft should avoid implying that every continued-fraction algorithm must
select this parent, but its stated obstruction to this direct descent is
correct.

## 5. The nonsquare slow family is correct

Take an integer $L\ge1$ and put

\[
M=\operatorname{lcm}(2,\ldots,L+1),\quad
A=M^2+M+1,\quad B=(M+1)^2,\quad N=AB.
\]

Both $A$ and $B$ are $1$ modulo $M$. Hence $N\equiv1\pmod u$ for each
$2\le u\le L+1$. In particular, every such $u$ is a unit modulo $N$, the
canonical inverse of $N$ modulo $u$ is $1$, and

\[
D_N(u)=u-1.
\]

This proves the full $L$-transition path from $L+1$ to $1$. It also proves
the endpoint and unit claims without an unknown factor.

The factor-block assertions are exact:

\[
B-A=M,
\qquad
\gcd(A,B)=\gcd(A,M)=1,
\]

and $M^2<A<(M+1)^2$. Therefore $A$ is not a square. A coprime product can
be a square only when each factor is a square, so $N=AB$ is nonsquare. Also

\[
1<\frac BA<2.
\]

The standard estimate $\log M=\Theta(L)$ gives
$\log N=\Theta(L)$, and the exhibited depth is therefore
$\Theta(\log N)$.

The first small cases agree with every formula:

- $L=1$: $M=2$, $N=7\cdot9=63$, and $2\to1$.
- $L=2$: $M=6$, $N=43\cdot49=2107$, and $3\to2\to1$.

The family is not merely easy because its constructor displays $A$ and $B$.
It is an immediate Fermat instance from bare $N$. Since $M$ is even,

\[
x=\frac{A+B}{2},\qquad y=\frac{B-A}{2}=\frac M2
\]

are integers and $N=x^2-y^2$. Moreover,

\[
(x-1)^2<N<x^2,
\]

because $x^2-N=y^2$ and
$N-(x-1)^2=2x-1-y^2>0$. Thus $x=\lceil\sqrt N\rceil$, and Fermat's first
square test returns $A$ and $B$. This does not weaken the depth lower bound,
but it sharply limits what the family says about factoring difficulty.

Finally, if an integer-valued $h(L)=o(L)$ is used, then eventually
$0\le h(L)\le L$ and

\[
\frac{u_{h(L)}}{u_0}
=1-\frac{h(L)}{L+1}\longrightarrow1.
\]

Because $\log N_L=\Theta(L)$, this correctly rules out any uniform theorem
that promises a fixed contraction factor below one after
$o(\log N)$ transitions on every input. A revision should state the fixed
factor and the quantifier on $h$ explicitly.

## 6. Scope and required repairs

The candidate correctly says that it proves neither a bit-polynomial depth
bound nor a factoring algorithm. It also correctly says that a cheap
trajectory would still need a factor-bearing event or a successful joint
decoder.

Before a new audit, make these exact repairs:

1. Handle $L=0$ before using the strict telescoping inequality.
2. Replace the ordered determinant claim by (A6), or say “absolute
   determinant one” and give the left/right orientation.
3. Replace “factor-free state/depth” by “unit state/unit-state depth,” and
   state exactly that $\gcd(u_i,N_L)=1$ along the displayed path.
4. Quantify the contraction statement with a fixed constant $c<1$ and an
   integer-valued block length $h(N)=o(\log N)$.
5. Describe the family as an immediate Fermat family, not only as easy “by
   construction.”

The closing sentence should also not present identity (8) as the only
possible route to a polynomial depth proof. Its mathematical outcome split
is valid—either a uniform polynomial bound exists or depths outrun every
fixed polynomial on a sequence—but another invariant could prove the upper
bound without being phrased as a combination of (8).

After these repairs, the main theorem is suitable for a fresh hostile audit.
This report does not authorize reconstruction of the pinned version.
