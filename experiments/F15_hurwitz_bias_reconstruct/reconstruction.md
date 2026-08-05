# Proof-blind reconstruction: the corrected nonuniform-Hurwitz statements

## Result and scope

All five corrected claims in the assignment are true, with the qualifications stated there. The sampling algorithm is an exact sampler but costs square-root time in \(N\), the menu argument obstructs only selectors that choose one of the stated fixed transforms, and the unit-orbit construction is only a conditional extractor: its success probability can be zero.

I use the following already-promoted P25 dictionary. For every odd prime \(r\mid N\), reduction through a splitting

\[
\mathcal H/r\mathcal H\simeq M_2(\mathbb F_r)
\]

sends a norm-\(N\) element to a nonzero rank-one matrix. Its row and image lines are denoted by \(R_r\) and \(I_r\). Left-unit orbits in \(S_N\) are exactly the fibers of

\[
(R_p,R_q):S_N\longrightarrow
\mathbf P^1(\mathbb F_p)\times\mathbf P^1(\mathbb F_q),
\]

and right-unit orbits are exactly the fibers of \((I_p,I_q)\). Both unit actions are free. A greatest common right divisor is defined by

\[
\mathcal Hx+\mathcal Hy=\mathcal H d_R
\]

and obeys

\[
r\mid\operatorname{nrd}(d_R)
\quad\Longleftrightarrow\quad
R_r(x)=R_r(y).                                      \tag{0.1}
\]

The analogous left gcd is controlled by image lines. These are the orientation and handedness conventions used below.

## 1. Exactly eight integer-coordinate elements per unit orbit

The Hurwitz order and its units have the disjoint decompositions

\[
\mathcal H=\mathbb Z^4\;\sqcup\;(\mathbb Z+\tfrac12)^4,
\]

\[
\mathcal H^\times
=Q_8\;\sqcup\;
\left\{
\frac{s_0+s_1i+s_2j+s_3k}{2}:s_0,s_1,s_2,s_3\in\{\pm1\}
\right\},                                            \tag{1.1}
\]

where \(Q_8=\{\pm1,\pm i,\pm j,\pm k\}\). Thus there are eight integral units and sixteen all-half-integral units.

### Integral input

Let \(x=a+bi+cj+dk\in\mathbb Z^4\) have odd norm. Modulo \(2\),

\[
a+b+c+d\equiv a^2+b^2+c^2+d^2\equiv1.
\]

For \(u=(s_0+s_1i+s_2j+s_3k)/2\), the four coordinate numerators of \(ux\) are

\[
\begin{split}
&s_0a-s_1b-s_2c-s_3d,\qquad
s_0b+s_1a+s_2d-s_3c,\\
&s_0c-s_1d+s_2a+s_3b,\qquad
s_0d+s_1c-s_2b+s_3a .
\end{split}
\]

The right product has the same signed-sum property. Every numerator contains \(a,b,c,d\) once, so its parity is \(a+b+c+d\), hence odd. Therefore all sixteen half-integral units send \(x\) to the all-half-integral coset, while the eight units in \(Q_8\) keep it in \(\mathbb Z^4\). There are exactly eight integer-coordinate products on either side.

### Half-integral input

Now write

\[
x=\frac{A+Bi+Cj+Dk}{2},
\qquad A,B,C,D\text{ odd}.
\]

Indeed every such Hurwitz element has odd norm, because each odd square is \(1\) modulo \(8\), and hence

\[
\operatorname{nrd}(x)=\frac{A^2+B^2+C^2+D^2}{4}
\equiv1\pmod2.
\]

The eight integral units preserve the all-half-integral coset. For a half-integral unit

\[
u=\frac{s_0+s_1i+s_2j+s_3k}{2},
\]

the real coordinate of both \(ux\) and \(xu\) is

\[
\frac{s_0A-s_1B-s_2C-s_3D}{4}.                       \tag{1.2}
\]

For fixed odd \(A,B,C,D\), varying the four signs makes the four summands in the numerator independently equal to \(+1\) or \(-1\) modulo \(4\). If \(m\) of their residues are \(+1\), their sum is \(2m-4\) modulo \(4\), so it vanishes modulo \(4\) exactly when \(m\) is even. There are

\[
\binom40+\binom42+\binom44=8                         \tag{1.3}
\]

such sign choices. Since the product belongs to \(\mathcal H=\mathbb Z^4\sqcup(\mathbb Z+\tfrac12)^4\), an integral real coordinate forces all four coordinates to be integral; otherwise all four are half-integral. Hence exactly eight of the sixteen half-integral units give integer-coordinate products. Formula (1.2) is the same on the left and the right, so this proves both handednesses.

The unit actions are free: if \(ux=vx\), or \(xu=xv\), cancellation in the rational quaternion division algebra gives \(u=v\). Every left- and every right-unit orbit therefore has 24 elements, exactly 8 of which lie in \(L_N\).

By the P25 orbit dictionary, there is one left-unit orbit for every row-line pair and one right-unit orbit for every image-line pair. Consequently

\[
|L_N|=8\,|\mathbf P^1(\mathbb F_p)|\,
          |\mathbf P^1(\mathbb F_q)|
=8(p+1)(q+1).                                        \tag{1.4}
\]

Every row-pair fiber in \(L_N\) has size eight. Thus a uniform element of \(L_N\) has a uniform pair \((R_p,R_q)\), which is the product of the uniform laws on the two projective lines. In particular \(R_p\) and \(R_q\) are independent. Applying the right-orbit statement gives the same conclusion separately for \((I_p,I_q)\). This does **not** assert that the row and image line of one element are independent.

## 2. The explicit rejection sampler

Put

\[
B=\lfloor\sqrt N\rfloor,\qquad M=2B+1.
\]

One outer trial does the following.

1. Draw \(a,b,c\) independently and uniformly from the \(M\) integers in \([-B,B]\), and draw an independent fair bit \(\epsilon\).
2. Set \(h=N-a^2-b^2-c^2\). Reject unless \(h=d_0^2\ge0\) for an integer \(d_0\ge0\).
3. If \(d_0>0\), output \(a+bi+cj+(-1)^\epsilon d_0k\). If \(d_0=0\), output only when \(\epsilon=0\); reject when \(\epsilon=1\).

Every integer-coordinate representation of \(N\) has each coordinate of absolute value at most \(B\). A representation whose last coordinate is nonzero is produced by exactly one triple and one bit value. A representation whose last coordinate is zero is likewise produced by exactly one triple and the sole accepted bit value. Thus every \(x\in L_N\) is produced in one outer trial with the same probability

\[
\frac1{2M^3}.                                        \tag{2.1}
\]

It follows from (1.4) that

\[
P_{\rm acc}=\frac{|L_N|}{2M^3}
=\frac{4(p+1)(q+1)}{M^3},                            \tag{2.2}
\]

and the output conditional on acceptance is exactly uniform on \(L_N\). The number \(T\) of outer trials is geometric, so termination is almost sure and

\[
\mathbb E T=\frac{M^3}{4(p+1)(q+1)}.                 \tag{2.3}
\]

Since \(M=\Theta(\sqrt N)\) and

\[
N\le(p+1)(q+1)=N+p+q+1\le2N
\]

for distinct odd primes, (2.3) is \(\Theta(\sqrt N)\). In particular this holds on the balanced family \(p<q<2p\).

For an exact random-bit implementation, let \(\ell=\lceil\log_2M\rceil\), draw \(\ell\)-bit integers until the value is below \(M\), and translate it to \([-B,B]\). One such draw uses an expected

\[
\ell\frac{2^\ell}{M}\in[\ell,2\ell)
\]

bits. Its number of rejected blocks is independent of its final uniform value, so the random-bit cost of a trial is independent of the trial's acceptance event. Including the sign bit, Wald's identity (or direct conditioning) gives

\[
\mathbb E[\text{random bits}]
=\mathbb ET\left(3\ell\frac{2^\ell}{M}+1\right)
=\Theta(\sqrt N\log N).                              \tag{2.4}
\]

All operands have \(O(\log N)\) bits. Three squarings, additions, and an exact integer-square-root test take \(\operatorname{poly}(\log N)\) bit operations per trial; for example, schoolbook arithmetic gives such a bound directly. Hence the expected bit time is

\[
O\!\left(\sqrt N\,\operatorname{polylog}N\right).    \tag{2.5}
\]

It is important not to abbreviate (2.5) as literal \(\Theta(\sqrt N)\): random-bit generation alone costs \(\Theta(\sqrt N\log N)\) in this implementation.

## 3. Fixed-menu selectors

Fix an odd prime \(r\mid N\), a menu \(\mathcal T\) of \(C\) fixed unit/conjugation transforms, and one output marginal (row for a right-gcd test or image for a left-gcd test). The hypothesis on the menu says that, for each fixed \(t\in\mathcal T\), the output line \(F_{t,r}(X)\) is a projective bijective image of one of the uniform raw row/image marginals. Hence

\[
\Pr(F_{t,r}(X)=\lambda)=\frac1{r+1}                  \tag{3.1}
\]

for every \(\lambda\in\mathbf P^1(\mathbb F_r)\).

Let a memoryless selector choose \(t_X\in\mathcal T\) from the current sample \(X\), and put \(W_r=F_{t_X,r}(X)\). For every line \(\lambda\),

\[
\{W_r=\lambda\}
\subseteq\bigcup_{t\in\mathcal T}
\{F_{t,r}(X)=\lambda\}.
\]

The union bound and (3.1) give the general atom bound

\[
\max_\lambda\Pr(W_r=\lambda)
\le \min\left(1,\frac C{r+1}\right).                \tag{3.2}
\]

Outputs of the same memoryless rule on iid raw samples are iid. More generally, for two independent such outputs with atom laws \(a_\lambda,b_\lambda\), both satisfying (3.2),

\[
\Pr(W_r=W'_r)=\sum_\lambda a_\lambda b_\lambda
\le\max_\lambda a_\lambda
\le\min\left(1,\frac C{r+1}\right).                \tag{3.3}
\]

Now allow a joint or stateful selector to inspect all \(K\) iid raw samples \(X_1,\ldots,X_K\) before choosing one menu transform for each sample. For a fixed pair \(i<j\), equality of the two selected local lines implies

\[
F_{s,r}(X_i)=F_{t,r}(X_j)
\quad\text{for some }(s,t)\in\mathcal T^2.
\]

For each fixed transform pair, the two lines are independent and uniform, so their equality probability is \(1/(r+1)\). Therefore

\[
\Pr(W_{i,r}=W_{j,r})
\le\min\left(1,\frac{C^2}{r+1}\right).              \tag{3.4}
\]

This proof does not require the choices for different samples to be independent.

For all-pairs testing in one handedness, a proper gcd event is contained in the event that some pair collides at \(p\) or at \(q\). A second union bound yields

\[
\Pr(\text{some proper gcd})
\le \binom K2 C^2
\left(\frac1{p+1}+\frac1{q+1}\right),               \tag{3.5}
\]

capped, of course, at \(1\). On \(p<q<2p\), this is

\[
O\!\left(\frac{C^2K^2}{\sqrt N}\right).             \tag{3.6}
\]

Thus fixed \(C\) and polylogarithmic \(K\) cannot give constant all-pairs success on the balanced family; more generally (3.6) vanishes when \(CK=o(N^{1/4})\). Testing both handednesses changes only the constant in this union bound.

Nothing in this section covers a transform that combines two or more raw samples, nor an unrestricted nonlinear map outside the public finite menu.

## 4. The actual-unit orbit and its exact stabilizer law

Let \(U=\mathcal H^\times\), \(G=U/\{\pm1\}\cong A_4\), and fix \(\alpha\in S_N\). Reduction gives a right projective action of \(G\) on every \(\mathbf P^1(\mathbb F_r)\). Write

\[
H_r(\alpha)=\operatorname{Stab}_G(R_r(\alpha)).
\]

Draw actual units \(U_1,U_2\) independently and uniformly from the 24 elements of \(U\), and set \(Y_i=\alpha U_i\). With the convention \(L\cdot \bar u=R_r(xu)\) when \(L=R_r(x)\),

\[
R_r(\alpha U_1)=R_r(\alpha U_2)
\iff
R_r(\alpha)\cdot\overline{U_1U_2^{-1}}=R_r(\alpha). \tag{4.1}
\]

The order \(U_1U_2^{-1}\), rather than \(U_2^{-1}U_1\), follows by multiplying the equality of right-translated lines on the right by \(U_2^{-1}\).

The actual relative unit \(U_1U_2^{-1}\) is uniform on \(U\); quotienting by the two-element center makes

\[
g=\overline{U_1U_2^{-1}}
\]

uniform on the 12 elements of \(G\). By (0.1), the right gcd is proper exactly when the row lines agree at exactly one of \(p,q\), equivalently when \(g\) belongs to exactly one local stabilizer. Hence

\[
\boxed{
\Pr(\text{proper right gcd of }Y_1,Y_2)
=\frac{|H_p(\alpha)\mathbin\triangle H_q(\alpha)|}{12}.}
                                                               \tag{4.2}
\]

### Faithfulness, including characteristic \(3\)

For odd \(r\), the four elements \(1,i,j,k\) form an \(\mathbb F_r\)-basis after reduction, because \(2\) is invertible. Under any splitting to \(M_2(\mathbb F_r)\), a quaternion is projectively scalar exactly when its three imaginary coefficients vanish modulo \(r\).

Among the integral units, only \(\pm1\) have this property: each of \(\pm i,\pm j,\pm k\) has a nonzero imaginary coefficient \(\pm1\). Every half-integral unit has all three imaginary coefficients equal to \(\pm\tfrac12\), which are nonzero modulo every odd \(r\), including \(r=3\). Thus the kernel of

\[
U\longrightarrow\operatorname{PGL}_2(\mathbb F_r)
\]

is exactly \(\{\pm1\}\), and the induced action of \(G\) is faithful for every odd \(r\).

A nonidentity projective linear transformation fixes at most two projective lines (its fixed lines are its eigenlines; equivalently they solve a nonzero quadratic equation). The eleven nonidentity elements of \(G\) therefore have, in total, at most \(22\) fixed lines. Consequently

\[
\#\{L\in\mathbf P^1(\mathbb F_r):\operatorname{Stab}_G(L)\ne1\}
\le22.                                                   \tag{4.3}
\]

This is only a bounded-exception statement. It makes no assertion that a trivial-stabilizer line exists in any small characteristic; for example, the bound is vacuous on \(\mathbf P^1(\mathbb F_3)\).

### Direct extraction and bit complexity

If (4.1) holds at exactly one prime, the right gcd norm is divisible by that prime and not by the other. Since a right divisor \(d\) of a norm-\(N\) element has \(\operatorname{nrd}(d)\mid N\), squarefreeness restricts the right-gcd norm to \(1,p,q,N\). On the proper event it is therefore exactly \(p\) or \(q\). Computing \(\operatorname{nrd}(d_R)\) already returns the factor; a terminal integer \(\gcd(\operatorname{nrd}(d_R),N)\) is unnecessary.

For completeness, the right Euclidean algorithm is polynomial in \(\log N\) here. The following elementary covering estimate gives a quantitative contraction. For any point of \(\mathbb R^4\), round each coordinate to the nearest integer and let \(t_i\in[0,1/2]\) be the four absolute errors. Its squared distances to the integer and all-half-integer cosets are

\[
S_0=\sum_i t_i^2,
\qquad
S_1=\sum_i(\tfrac12-t_i)^2
=1-\sum_i(t_i-t_i^2).
\]

If \(S_0\le1/2\), use the integer point. Otherwise \(t_i-t_i^2\ge t_i^2\) gives \(S_1<1/2\), so use the half-integer point. Thus every real quaternion is within squared norm \(1/2\) of some Hurwitz integer.

Given \(a,b\in\mathcal H\), \(b\ne0\), apply this estimate to \(x=ab^{-1}\), choose \(q\in\mathcal H\) with \(\operatorname{nrd}(x-q)\le1/2\), and set

\[
a=qb+r.
\]

Then

\[
\operatorname{nrd}(r)
=\operatorname{nrd}(x-q)\operatorname{nrd}(b)
\le\tfrac12\operatorname{nrd}(b).                    \tag{4.4}
\]

The left-quotient Euclidean chain computes the greatest common right divisor and has \(O(\log N)\) divisions. Exact quotient rounding uses rational coordinates with \(O(\log N)\)-bit numerators and denominators; all remainders have norm at most \(N\). Multiplication by a unit is constant-size quaternion arithmetic. Therefore producing \(Y_1,Y_2\), computing \(d_R\), its norm, and checking \(1<\operatorname{nrd}(d_R)<N\) all take \(\operatorname{poly}(\log N)\) bit operations.

If \(|H_p(\alpha)\triangle H_q(\alpha)|>0\), independent pairs succeed with probability at least \(1/12\), so repetition takes at most 12 pairs in expectation and gives a conditional Las Vegas extractor with expected \(\operatorname{poly}(\log N)\) bit complexity. If the symmetric difference is empty, this orbit never succeeds. No method for finding a favorable \(\alpha\) in polynomial time is supplied, so this is not a top-level factoring algorithm.

## 5. Exact finite certificates

The two certificates can be checked without a search. For \(s,t\in\mathbb F_r\) satisfying \(s^2+t^2=-1\), use the splitting

\[
i\longmapsto
\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
j\longmapsto
\begin{pmatrix}s&t\\t&-s\end{pmatrix},
\qquad k\longmapsto ij.                               \tag{5.1}
\]

The two displayed matrices square to \(-I\) and anticommute; their four quaternion-basis images are linearly independent, so (5.1) is an algebra splitting.

Thus

\[
a+bi+cj+dk\longmapsto
\begin{pmatrix}
a+cs-dt&-b+ct+ds\\
b+ct+ds&a-cs+dt
\end{pmatrix}.                                        \tag{5.2}
\]

Represent the twelve elements of \(G\) by

\[
1,\ i,\ j,\ k,
\quad
h_{xyz}:=\frac{1+xi+yj+zk}{2}\quad(x,y,z\in\{\pm1\}). \tag{5.3}
\]

Multiplying a representative by the scalar \(2\) does not change its projective action.

### \(N=15\)

Let \(\alpha=1+i+2j+3k\); its norm is \(1+1+4+9=15\).

At \(r=3\), take \((s,t)=(1,1)\). Formula (5.2) gives

\[
\rho_3(\alpha)=\begin{pmatrix}0&1\\0&2\end{pmatrix},
\qquad R_3(\alpha)=\langle(0,1)\rangle.
\]

For \(u=e+fi+gj+hk\), this row is fixed exactly when the lower-left matrix entry \(f+g+h\) vanishes modulo \(3\). Checking (5.3) gives

\[
H_3(\alpha)=\{1,h_{+++},h_{---}\}.                   \tag{5.4}
\]

At \(r=5\), take \((s,t)=(0,2)\). Then

\[
\rho_5(\alpha)=\begin{pmatrix}0&3\\0&2\end{pmatrix},
\qquad R_5(\alpha)=\langle(0,1)\rangle.
\]

The stabilizer condition is now \(f+2g=0\pmod5\). It holds for \(1,k\), for neither \(i\) nor \(j\), and for no half-unit because \(x+2y\not\equiv0\pmod5\) for \(x,y\in\{\pm1\}\). Hence

\[
H_5(\alpha)=\{1,k\}.                                 \tag{5.5}
\]

The two stabilizers intersect only in the identity, so

\[
|H_3(\alpha)\triangle H_5(\alpha)|=3,
\qquad
\Pr(\text{proper right gcd})=\frac3{12}=\frac14.     \tag{5.6}
\]

### \(N=39\)

Let \(\alpha=1+i+j+6k\); its norm is \(1+1+1+36=39\).

At \(r=3\), again use \((s,t)=(1,1)\). Then

\[
\rho_3(\alpha)=\begin{pmatrix}2&0\\2&0\end{pmatrix},
\qquad R_3(\alpha)=\langle(1,0)\rangle.
\]

The stabilizer condition is the vanishing of the upper-right entry,

\[
-f+g+h=0\pmod3,
\]

which gives

\[
H_3(\alpha)=\{1,h_{-++},h_{+--}\}.                  \tag{5.7}
\]

At \(r=13\), choose \((s,t)=(3,4)\), since \(3^2+4^2=25\equiv-1\pmod{13}\). Formula (5.2) gives

\[
\rho_{13}(\alpha)=
\begin{pmatrix}6&8\\10&9\end{pmatrix},
\qquad R_{13}(\alpha)=\langle(1,10)\rangle.
\]

For a row \((1,\lambda)\), writing the unit matrix as

\[
\begin{pmatrix}P&Q\\R&S\end{pmatrix},
\]

the fixed-line condition is \(Q+\lambda(S-P)-\lambda^2R=0\). Substituting \(\lambda=10,s=3,t=4\) reduces it to

\[
3f-g+4h=0\pmod{13}.                                  \tag{5.8}
\]

None of \(i,j,k\) satisfies (5.8). Among the eight triples \((x,y,z)\in\{\pm1\}^3\), the only solutions of \(3x-y+4z=0\pmod{13}\) are

\[
(-1,+1,+1),\qquad(+1,-1,-1).
\]

Therefore

\[
H_{13}(\alpha)=\{1,h_{-++},h_{+--}\}=H_3(\alpha),   \tag{5.9}
\]

and (4.2) gives exact success probability \(0\).

These are finite examples only. They prove neither an asymptotic positive result nor an asymptotic obstruction for the unit-orbit extractor. No computational run was used in deriving these certificates.
