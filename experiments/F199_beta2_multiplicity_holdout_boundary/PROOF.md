# Proof of F199

## 1. Imported range and precision

The balanced semiprime promise gives

\[
p<\sqrt N<q,
\qquad p\le B<q.
\tag{38}
\]

P171 proves

\[
A=(-1)^B\binom{N-1}{B}\equiv1-q\pmod N,
\tag{39}
\]

so (3) is integral. P173 computes \(A\bmod2^n\) in polynomial bit time,
and P175 proves

\[
h-z\equiv p^{-1}\pmod {2^t}
\tag{40}
\]

and the numerical-QP terminal at (6). F199 uses these promoted facts and
adds no new literature premise.

Because \(L(n)=n^{o(1)}\) while
\(k=\Theta(n)\), equation (6) gives

\[
t=\Theta(n),
\qquad m=t-1=\Theta(n)
\tag{41}
\]

after a finite input prefix. All exact finite inequalities below are stated
separately, so no asymptotic estimate is used as an identity.

## 2. The solution torsor

Let \(u\in R^\times\) and define (8). The first two equations of (9) are
definitions. They imply

\[
P_uQ_u=u^{-1}Nu=N.
\tag{42}
\]

The definition of \(z\) says

\[
Nz=A-1\quad\text{in }R.
\tag{43}
\]

Therefore

\[
NH_u=N(z+u)=A-1+Nu=A-1+Q_u,
\tag{44}
\]

which proves (9).

Conversely, \(PU=1\) forces \(U\) to be a unit and \(P=U^{-1}\). The
other two equations force \(Q=NU\) and \(H=z+U\). This proves the pointwise
parameterization.

The same substitutions define mutually inverse ring homomorphisms between
the two rings in (11): send \(P,Q,H\) to
\(U^{-1},NU,z+U\), and send \(U\) to its residue class in the quotient.
Thus (11) holds.

For the ordered equations

\[
F_1=PU-1,
\qquad F_2=Q-NU,
\qquad F_3=H-z-U,
\tag{45}
\]

the Jacobian columns indexed by \((P,Q,H)\) form the diagonal matrix

\[
\begin{pmatrix}
U&0&0\\
0&1&0\\
0&0&1
\end{pmatrix}.
\tag{46}
\]

Its determinant \(U\) is a unit at every solution. Equivalently, (11)
identifies the solution scheme with the multiplicative group over \(R\).
No solution is distinguished by singularity or local multiplicity.

The target substitution

\[
u=p^{-1},
\qquad P=p,
\qquad Q=q,
\qquad H=h
\tag{47}
\]

is valid by (40) and \(N=pq\). It is one of all
\(|R^\times|=2^{t-1}\) solutions.

## 3. The public recurrence and the missing error word

Given a public index \(i\le B\), apply the power-of-two binomial routine
used in P173 with modulus parameter \(T=n\), upper index \(P=N-1\), and
lower index \(Q=i\). Its published range applies because
\(0\le i\le N-1<2^n\). It returns \(A_i\bmod 2^n\) in polynomial bit
time; reduction modulo \(2^t\), subtraction, and multiplication by
\(N^{-1}\bmod2^t\) compute \(z_i\). This proves the pointwise
computability claim without materializing the exponentially long word.

The adjacent-binomial identity gives the exact integer recurrence

\[
(i+1)(A_{i+1}-A_i)=-NA_i.
\tag{48}
\]

In \(R\), the definition of \(z_i\) gives

\[
A_i=1+Nz_i.
\tag{49}
\]

Substitute (49) into (48):

\[
(i+1)N(z_{i+1}-z_i)=-N(1+Nz_i).
\tag{50}
\]

The odd integer \(N\) is a unit in \(R\), so cancellation proves (14).

Expanding (15) gives

\[
\mathcal R_N=(K+1)Y+(N-K-1)X+1.
\tag{51}
\]

The two Hasse derivatives in (16) are therefore its displayed linear
coefficients. Since

\[
(N-K-1)+(K+1)=N
\tag{52}
\]

is odd, at least one is a unit modulo \(2\). This holds at every edge,
including \(K=p-1\). The remaining nonzero higher Hasse derivatives of
\(\mathcal R_N\) are the public mixed coefficients from the terms \(KY\)
and \(-KX\); they do not create a special multiplicity at \(p-1\).

For \(i<p\), P171 gives \(A_i\equiv1\pmod N\), so the first quotient in
(17) is integral and

\[
H_i\equiv N^{-1}(A_i-1)=z_i\pmod {2^t}.
\tag{53}
\]

For \(p\le i\le B\), P171 gives
\(A_i\equiv1-q\pmod N\), so the second quotient is integral and

\[
H_i
\equiv N^{-1}(A_i-1)+N^{-1}q
\equiv z_i+p^{-1}pmod {2^t}.
\tag{54}
\]

Equations (53)--(54) prove (18). Taking adjacent differences proves (19).
Thus a sparse-error decoder would need access to the \(H_i\) labels; the
public labels alone satisfy the everywhere-smooth recurrence (14).

## 4. Reed--Muller support bound

We prove (21) by induction on \(m\). For \(m=0\), the only nonzero function
has support one and degree zero.

For \(m\ge1\), write the unique multilinear decomposition

\[
F(x_1,\ldots,x_m)
=G(x_1,\ldots,x_{m-1})
+x_mJ(x_1,\ldots,x_{m-1}),
\tag{55}
\]

where

\[
\deg G\le d,
\qquad
\deg J\le d-1.
\tag{56}
\]

On the two halves of the cube, the evaluation words are \(G\) and
\(G+J\).

If \(J=0\), then \(G\ne0\), and induction gives

\[
\operatorname{wt}(F)
=2\operatorname{wt}(G)
\ge2\cdot2^{m-1-d}
=2^{m-d}.
\tag{57}
\]

If \(J\ne0\), then at every point where \(J=1\), exactly one of
\(G,G+J\) is one. Hence

\[
\operatorname{wt}(F)
=\operatorname{wt}(G)+\operatorname{wt}(G+J)
\ge\operatorname{wt}(J)
\ge2^{(m-1)-(d-1)}
=2^{m-d}.
\tag{58}
\]

This proves (21).

If \(F\) vanishes outside \(S\), its nonempty support is contained in
\(S\). Equations (21)--(22) follow. In particular, singleton support needs
\(d\ge m\). The usual multilinear delta function

\[
\delta_a(x)
=\prod_{r:a_r=1}x_r
 \prod_{r:a_r=0}(1+x_r)
\tag{59}
\]

has degree \(m\), so the bound is sharp.

Let \(V_{m,d}\) be the coefficient space of multilinear polynomials of
degree at most \(d\). If evaluation on \(\Omega\setminus S\) had a
nonzero kernel, one kernel element would contradict (22) whenever
\(|S|<2^{m-d}\). Thus the restricted map is injective.

The full evaluation map on \(\Omega\) is injective, so its transpose has
column span of dimension

\[
\dim V_{m,d}=\sum_{r=0}^d\binom mr.
\tag{60}
\]

The same rank after deleting \(S\) proves the feature-column formulation.

For fixed \(d=(\log n)^{O(1)}\), equation (60) is numerical QP because

\[
\sum_{r=0}^d\binom mr
\le(d+1)m^d
=2^{(\log n)^{O(1)}}.
\tag{61}
\]

But by (41),

\[
2^{m-d}=2^{\Theta(n)}
\tag{62}
\]

up to a sublinear polylogarithmic term in the exponent. It exceeds every
fixed numerical-QP holdout size after a finite prefix.

## 5. Hasse balls and scalar multiplicity

The Hasse expansion of a multilinear polynomial is

\[
F(x+y)=\sum_{S\subseteq[m]}D_SF(x)y_S.
\tag{63}
\]

For \(y=\mathbf1_T\), a monomial \(y_S\) is one exactly when
\(S\subseteq T\), proving (23).

If every \(D_SF(x)\) with \(|S|<s\) vanishes, then (23) gives
\(F(x+\mathbf1_T)=0\) for \(|T|<s\). Conversely, the equations for
\(|T|<s\) form the triangular Boolean zeta transform of the derivatives.
Möbius inversion on the subset lattice recovers
\(D_SF(x)=0\) for \(|S|<s\). This proves the equivalence.

Now suppose the order-\(s\) conditions hold at every point except \(u\),
where \(s\ge2\). Choose any coordinate \(r\) and put

\[
x=u+e_r.
\tag{64}
\]

Then \(x\ne u\), so the condition at \(x\) applies. Since \(u\) is in the
radius-one ball about \(x\), it forces \(F(u)=0\). This proves (25).

One Hamming ball has volume

\[
V(m,s-1)=\sum_{j=0}^{s-1}\binom mj.
\tag{65}
\]

The union bound proves (26). If \(C\) and \(s\) are numerical QP and
polylogarithmic as stated, then

\[
C V(m,s-1)
\le C s m^{s-1}
=2^{(\log n)^{O(1)}}.
\tag{66}
\]

This is smaller than \(2^m-1\) for all sufficiently large inputs.

For the scalar statement, vanishing of the first \(s\) Hasse coefficients
at \(x_i\) is equivalent to

\[
(X-x_i)^s\mid f(X).
\tag{67}
\]

The factors for distinct \(x_i\) are pairwise coprime. If the conditions
hold at \(M-1\) points, their product of degree \(s(M-1)\) divides \(f\).
This proves (27).

## 6. An explicit target list is already a factorer

Assume an algorithm produces the list (28)--(29). For each listed \(u\),
modular inversion computes the odd canonical residue

\[
s=u^{-1}\pmod {2^t}.
\tag{68}
\]

At the true list entry, \(s=p\bmod2^t\). P175 proves that this residue at
precision (6) invokes a deterministic numerical-QP known-residue-class
factorer. Run that terminal on every list entry and accept a candidate only
after checking

\[
1<d<N,
\qquad d\mid N.
\tag{69}
\]

The correct list entry guarantees success. If the list size and each call
are bounded by
\(2^{(\log n)^{O(1)}}\), their product has the same form. A Las Vegas list
generator remains Las Vegas after deterministic verified postprocessing and
has the same expected-QP composition bound.

If one cloud column has an enumerable QP preimage list, enumerate it first;
the union over QP-many columns is still QP. If an explicit public index list
contains \(p\), exact gcd testing detects it directly. None of these
arguments applies to a column whose candidate preimage is exponentially
large and is not enumerated.

## 7. Paired one-bit lifts

Put

\[
M=2^{j+1},
\qquad a=2^j.
\tag{70}
\]

The two lifts are \(u_0=\bar u\) and \(u_1=\bar u+a\) modulo \(M\). Let
\(P_0=u_0^{-1}\pmod M\). Since both \(u_0\) and \(P_0\) are odd,
\(u_0+P_0\) is even. Also \(a^2\) is divisible by \(M\) because
\(j\ge1\). Hence

\[
(u_0+a)(P_0+a)
=u_0P_0+a(u_0+P_0)+a^2
\equiv1\pmod M.
\tag{71}
\]

Thus

\[
P_1\equiv P_0+a\pmod M.
\tag{72}
\]

Similarly, oddness of \(N\) gives

\[
Q_1=N(u_0+a)
\equiv Q_0+a\pmod M.
\tag{73}
\]

Equations (72)--(73) prove (33), and the definitions prove (34). Adding
\(a\) a second time is zero modulo \(M\), so the toggle is an involution.

It remains to prove the range statement. Since \(N=pq\) with \(p\ne q\),
\(\sqrt N\) is not an integer. Every interval of length \(M\) with
nonintegral endpoints contains exactly one representative of every residue
class modulo \(M\). Therefore the residue class \(P_b\) has an odd
representative

\[
\sqrt N-M<\widetilde P_b<\sqrt N,
\tag{74}
\]

and \(Q_b\) has an odd representative

\[
\sqrt N<\widetilde Q_b<\sqrt N+M.
\tag{75}
\]

The strict inequality \(3M<\sqrt N\) gives

\[
\sqrt N+M
<2(\sqrt N-M)
<2\widetilde P_b.
\tag{76}
\]

Combining (74)--(76) proves (36). If \(M\le N^{1/4}\), then
\(3M<\sqrt N\) follows once \(N^{1/4}>3\). This establishes the claimed
finite-prefix qualification.

The construction deliberately asserts neither primality nor the exact
product equation for these representatives. Adding either condition would
reintroduce the hidden integer factorization constraint.

## 8. Why adaptive prefix selection remains open

For one prescribed prefix \(a\), each factor in (37) is one exactly when
the corresponding bit agrees with \(a_r\). Their product is therefore the
indicator of the prefix cell. It has degree \(\ell\), and the remaining
\(m-\ell\) free bits give support size \(2^{m-\ell}\). This meets the
support bound (21) with equality.

For \(\ell=(\log n)^{O(1)}\), equation (61) shows that all degree-at-most-
\(\ell\) features can be represented in numerical-QP space. Selecting one
correct cell can therefore reveal a polylogarithmic block without any
dimension contradiction. Repeating for \(O(n/\ell)\) stages is one
sequential chain; a polynomial factor times a numerical-QP node bound is
still numerical QP.

F199 supplies no value that distinguishes the correct cell. The torsor in
Section 2 contains every candidate, the recurrence in Section 3 has no
transition jet, and Section 7 gives two valid congruence children at every
lift. A nonlocal integer cell syndrome would be a materially new operation
and remains outside the theorem.
