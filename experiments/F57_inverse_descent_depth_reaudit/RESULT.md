# Fresh hostile re-audit of corrected F57

## Disposition

I audited the complete corrected artifact
`experiments/F57_inverse_descent_depth_kill/RESULT.md` at SHA-256

```text
e65df85135f4793096d49147ba066682c9afd134b7e166e5386bc1898698b05f
```

I re-derived every claim from the definitions and compared the claimed
improvement with F43/P62. This was a proof-only audit. I ran no computation
and used no public search.

**Verdict: PASS.** The corrected artifact is promotion-ready as a narrow
structural theorem. The zero-transition case, terminal-nonunit scope,
ordered Farey determinant, unit-state wording, Fermat-easy boundary, and
sublogarithmic contraction quantifiers are now correct. I found no remaining
mathematical or scope defect.

This pass certifies only the claims in the artifact. It does not give a
bit-polynomial depth bound, a success law, or a factoring algorithm.

## 1. One-step law and endpoint scope

For each source unit $u_i>1$, let $v_i$ be its canonical inverse modulo $N$
and let

\[
u_{i+1}=\frac{u_iv_i-1}{N},\qquad
r_i=u_i-u_{i+1},\qquad t_i=N-v_i.
\]

Direct subtraction gives

\[
Nr_i=N u_i-(u_iv_i-1)=u_i(N-v_i)+1=u_it_i+1.
\tag{R1}
\]

Because $1\le v_i<N$, one has $1\le t_i<N$. The positive product $u_iv_i$
is $1$ modulo $N$. It cannot equal $1$ when $u_i>1$, so
$u_iv_i\ge N+1$ and $u_{i+1}\ge1$. Equation (R1) then gives
$1\le r_i<u_i<N$. Thus $r_i$ is the canonical inverse of $N$ modulo
$u_i$, and every defined transition strictly decreases the positive integer
state.

Nothing in this argument requires $u_{i+1}$ to be a unit. Therefore the last
transition into a proper nonunit is covered. The corrected proof separately
disposes of $L=0$, so it does not apply a false strict inequality to an empty
trajectory.

## 2. Uniform depth bound

Assume $L\ge1$. Equation (R1) gives

\[
\frac{r_i}{u_i}=\frac{t_i}{N}+\frac1{Nu_i}>\frac{t_i}{N}.
\]

Since $0<r_i/u_i<1$,

\[
\log\frac{u_i}{u_{i+1}}
=-\log\!\left(1-\frac{r_i}{u_i}\right)
\ge\frac{r_i}{u_i}>\frac{t_i}{N}.
\]

The sum telescopes, and $u_0<N$, $u_L\ge1$, so

\[
\sum_{i=0}^{L-1}t_i
<N\log\frac{u_0}{u_L}<N\log N.
\tag{R2}
\]

Only source states enter the distinctness argument. All
$u_0,\ldots,u_{L-1}$ are units and are distinct because the state decreases.
Inversion permutes the unit residues, so the corresponding $v_i$ are
distinct. Hence the positive integers $t_i=N-v_i$ are distinct even when
$u_L$ is a nonunit. Therefore

\[
\sum_{i=0}^{L-1}t_i\ge\frac{L(L+1)}2.
\]

Combining this with (R2) proves

\[
\frac{L(L+1)}2<N\log N,
\qquad
L<\sqrt{2N\log N}.
\]

This is uniform in $N$ and in the terminal type. It genuinely removes the
maximal-divisor factor used in P62. It remains exponential in the binary
input length, exactly as the candidate states.

## 3. Adjacent-step identities

Suppose $u_{i+1}$ is a unit. Write
$u=u_i$, $r=r_i$, $t=t_i$, $r'=r_{i+1}$, and $t'=t_{i+1}$. Then

\[
Nr=ut+1,
\qquad
Nr'=(u-r)t'+1.
\tag{R3}
\]

With $\delta=rt'-r't$, eliminating the two occurrences of $N$ gives

\[
u\delta=r^2t'+r'-r
=r(rt'-1)+r'>0.
\tag{R4}
\]

The definition already makes $\delta$ an integer. Since $u>0$, (R4) proves
$\delta\in\mathbb Z_{>0}$. Multiplying the definition by $N$ and using
(R3) also gives

\[
N\delta=rtt'+t'-t.
\tag{R5}
\]

The determinant sign implies $t'/r'>t/r$. The fractions are reduced because
any common divisor of $r,t$ divides $Nr-ut=1$. Thus the candidate's
“reduced fractions strictly increase” statement is exact.

Finally, $\delta\ge1$ and $t\ge1$ turn (R5) into

\[
rtt'+t'=N\delta+t\ge N+1.
\]

If $r,t,t'\le B$, its left side is at most $B^3+B$. The displayed
consequence $B^3+B\ge N+1$ is therefore correct.

## 4. Farey orientation and numerator reset

Equation (R1), together with $u_{i+1}=u_i-r_i$ and $v_i=N-t_i$, gives

\[
\frac{N}{u_i}-\frac{t_i}{r_i}=\frac1{u_ir_i},
\qquad
\frac{v_i}{u_{i+1}}-\frac{N}{u_i}
=\frac1{u_i u_{i+1}}.
\]

Hence

\[
\frac{t_i}{r_i}<\frac{N}{u_i}<\frac{v_i}{u_{i+1}}.
\]

The corrected orientation is

\[
v_i r_i-t_i u_{i+1}=1,
\]

so the ordered vectors $(t_i,r_i),(v_i,u_{i+1})$ have determinant $-1$
and absolute determinant one. Their componentwise sum is $(N,u_i)$.
The parent fractions and $N/u_i$ are reduced: this follows from (R1), from
$u_iv_i-Nu_{i+1}=1$, and from $u_i$ being a unit modulo $N$. Therefore the
two fractions are exactly the left and right Farey parents of $N/u_i$.

The denominator $u_{i+1}$ belongs to the right parent
$v_i/u_{i+1}$, whereas the next trajectory center is $N/u_{i+1}$. This is
the stated numerator reset. The parent relation alone therefore does not
make the actual trajectory a continued-fraction descent. The candidate does
not claim a general impossibility theorem from this observation.

## 5. Nonsquare balanced slow family

Interpret the family parameter as a positive integer $L$, as required by the
displayed $L$-transition path. Put

\[
M=\operatorname{lcm}(2,\ldots,L+1),\quad
A=M^2+M+1,\quad B=(M+1)^2,\quad N=AB.
\]

Both $A$ and $B$ are $1$ modulo $M$. Thus $N\equiv1\pmod u$ for every
$2\le u\le L+1$. Each displayed state is consequently a unit modulo $N$,
the canonical inverse of $N$ modulo $u$ is $1$, and

\[
D_N(u)=u-1.
\]

This proves the exact trajectory $L+1\to L\to\cdots\to1$.

Also

\[
B-A=M,
\qquad
\gcd(A,B)=\gcd(A,M)=1.
\]

Since $M^2<A<(M+1)^2$, $A$ is not a square. If the coprime product $AB$
were a square, both factors would be squares, a contradiction. Hence $N$ is
nonsquare. It is composite because $A,B>1$. The balance claim follows from
$B>A$ and

\[
2A-B=M^2+1>0,
\]

so $1<B/A<2$.

The standard estimate
$\log\operatorname{lcm}(1,\ldots,L+1)=\Theta(L)$ applies, and
$A,B=\Theta(M^2)$. Hence

\[
\log N=\Theta(\log M)=\Theta(L).
\]

The family therefore supplies unit-state depth $L=\Theta(\log N)$ on
nonsquare composites with balanced explicit factor blocks.

## 6. The one-test Fermat claim

For $L\ge1$, $M$ is even. Thus

\[
x=\frac{A+B}{2},
\qquad
y=\frac{B-A}{2}=\frac M2
\]

are integers and $N=x^2-y^2$. Since $y>0$, $N<x^2$. For the other side,

\[
N-(x-1)^2=2x-1-y^2
=\frac74M^2+3M+1>0.
\]

Therefore $(x-1)^2<N<x^2$, so $x=\lceil\sqrt N\rceil$. The first Fermat
test computes $x^2-N=y^2$ and returns

\[
x-y=A,
\qquad
x+y=B.
\]

This uses only $N$, not the hidden construction parameter. The candidate
therefore states the family's extreme ease precisely and does not present it
as a hard semiprime family.

## 7. Quantified sublogarithmic obstruction

Let $h(N)$ be nonnegative and integer-valued with
$h(N)=o(\log N)$. Since $\log N_L=\Theta(L)$,

\[
h(N_L)=o(L).
\]

Thus $h(N_L)\le L$ for all sufficiently large $L$, so the referenced state
exists, and

\[
\frac{u_{h(N_L)}}{u_0}
=1-\frac{h(N_L)}{L+1}\longrightarrow1.
\]

For any fixed contraction factor $c<1$, the ratio exceeds $c$ for all
sufficiently large $L$. Hence no all-input theorem can promise
$u_{h(N)}\le c u_0$ after a sublogarithmic number of transitions. This
claim concerns only a uniform fixed-factor contraction rule. It does not
exclude a polynomial depth theorem based on another potential, and the
candidate now says so.

## 8. Promotion boundary

All four advertised positive results are proved at the stated scope:

1. the uniform $\sqrt{2N\log N}$ depth bound;
2. the positive adjacent determinant identities;
3. the exact Farey-parent structure with numerator reset; and
4. the nonsquare balanced $\Theta(\log N)$ unit-state family and its
   sublogarithmic fixed-contraction obstruction.

The artifact explicitly excludes every stronger inference that this audit
would reject. It proves no $\operatorname{poly}(\log N)$ upper bound, no
superpolynomial lower family, no factor-bearing trajectory event, no batch
success theorem, and no factoring algorithm. A proof-blind reconstruction is
warranted for the pinned corrected version.
