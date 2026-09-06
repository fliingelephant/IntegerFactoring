# F257 proof — signed Pell-resultant refinement

## 1. Canonical identities

Substitution in \(T_h=y_h+k_hN\) gives

\[
\Delta=T_i k_j-T_j k_i
=y_i k_j-y_j k_i
={T_jy_i-T_iy_j\over N}.
\]

Also \(A_h\equiv S_h^2\pmod N\), so the stated root screen gives the
supplied unit roots.

## 2. Exact shared-gcd split

Put \(A=1+Dy_i^2\), \(u=y_i-y_j\), and \(v=y_i+y_j\). Since
\(\gcd(A,D)=1\) and \(A_j-A_i=-Duv\),

\[
d=\gcd(A_i,A_j)=\gcd(A,uv). \tag{2.1}
\]

The duplicate-coordinate cleanup makes \(u,v\ne0\), so all valuations below
are finite.

Moreover, \(d_-=\gcd(A,u)\) and \(d_+=\gcd(A,v)\) both divide \(d\).

Fix an odd prime \(\ell\mid A\), and write

\[
a=v_\ell(A),\qquad b=v_\ell(u),\qquad c=v_\ell(v).
\]

The relation \(\gcd(A,y_i)=1\) shows that \(\ell\) cannot divide both
\(u\) and \(v\), because then it would divide \(u+v=2y_i\). Thus
\(\min(b,c)=0\), and

\[
v_\ell(d)=\min(a,b+c)
=\min(a,b)+\min(a,c).
\]

This proves the exact, coprime odd-part product and unique coordinate sign.

At two, set \(a=v_2(A)\), \(b=v_2(u)\), and \(c=v_2(v)\). Then

\[
v_2(d)=\min(a,b+c),
\]

while

\[
v_2(\operatorname{lcm}(d_-,d_+))
=\max\{\min(a,b),\min(a,c)\}.
\]

If one of \(b,c\) is zero, these agree. If both are positive and
\(y_i,y_j\) are even, then \(a=0\), so they again agree. Otherwise
\(D,y_i,y_j\) are odd, exactly one of \(b,c\) equals \(1\), and the other
is at least \(2\). The displayed valuations differ by one exactly when
\(a\ge b+c=v_2(uv)\). This proves the formula for \(\eta\).

Finally,

\[
\gcd(d_-,d_+)=\gcd(A,u,v)
\]

divides \(2y_i\) and is coprime to \(y_i\), so it is \(1\) or \(2\).
For \(D=7,y_i=1,y_j=3\), the values are
\(d=8,d_-=2,d_+=4\), proving that the correction is necessary.

## 3. Signed resultant divisibility

P217 gives

\[
\operatorname{Res}(f_i,f_j)
=D^2Q_-Q_+.
\]

Let \(r=k_i-k_j\). Since \(\Delta=-y_i r+k_i u\),

\[
Q_-=A_i r^2+Dk_i u(k_i u-2y_i r). \tag{3.1}
\]

Hence \(d_-\mid Q_-\). Let \(s=k_i+k_j\). Since
\(\Delta=y_i s-k_i v\),

\[
Q_+=A_i s^2+Dk_i v(k_i v-2y_i s). \tag{3.2}
\]

Hence \(d_+\mid Q_+\). These are only containments: the other local linear
factor of either quadratic norm can vanish without a shared row prime.

For one Pell orbit with \(i<j\),

\[
S_iS_j-DT_iT_j=S_{j-i},\qquad
S_iS_j+DT_iT_j=S_{i+j}.
\]

Expanding \(Q_\pm\) and substituting these identities gives

\[
Q_-=(k_iS_j-k_jS_i)^2+2k_ik_j(S_{j-i}-1),
\]

\[
Q_+=(k_iS_j+k_jS_i)^2-2k_ik_j(S_{i+j}-1).
\]

## 4. One-sided hidden-prime gcd

Assume the balanced semiprime and Jacobi-minus-one hypotheses. At the
nonsplit hidden prime, a zero of

\[
Q_\sigma=a_\sigma^2+D\Delta^2
\]

would give \(a_\sigma^2=-D\Delta^2\). If \(\Delta\ne0\), this makes
\(-D\) a square, a contradiction. If \(\Delta=0\), it forces
\(a_\sigma=0\). Therefore a nonsplit zero requires

\[
a_\sigma\equiv\Delta\equiv0.
\]

Balancedness gives \(p,q>\sqrt{N/2}\). The public bound
\(0<|a_\sigma|<\sqrt{N/2}\) makes \(a_\sigma\) nonzero at both hidden
primes, so the nonsplit prime cannot divide \(Q_\sigma\). Consequently

\[
\gcd(Q_\sigma,N)\in\{1,r_{\rm sp}\}.
\]

At the split prime, choose \(w^2=-D\). Then

\[
Q_\sigma=(a_\sigma-w\Delta)(a_\sigma+w\Delta),
\]

which proves the two success branches. A proper gcd certifies every output.
The expected-time conclusion is conditional on the stated probability
lower bound; the proof supplies no such lower bound.

## 5. Signed refinement and root-sign boundary

Refining P66 fragments by gcd with every odd \(d_{ij,-}\) and
\(d_{ij,+}\) is factor-free and polynomial in the explicit bank length.
Section 2 gives every shared odd fragment a consistent pairwise coordinate
sign. The parity kernel remains the ordinary row-incidence kernel.

For odd \(h\), the Pell multiplication polynomials obey

\[
1+DF_{h,D}(Y)^2=(1+DY^2)G_{h,D}(Y)^2.
\]

If an odd prime \(\ell\mid1+Dy^2\), every term of \(F_{h,D}(y)\) except
the last contains \(1+Dy^2\). Hence

\[
F_{h,D}(y)\equiv D^{(h-1)/2}y^h
=(-1)^{(h-1)/2}y\pmod\ell.
\]

Thus an uncarried odd-multiple decoy is minus-labelled for
\(h\equiv1\pmod4\) and plus-labelled for \(h\equiv3\pmod4\), while P218
shows its normalized root is \(+1\).

For the exact global minus-channel certificate,

\[
19601^2-2\cdot13860^2=1,\qquad N=13859,
\]

so \(y_6=1\). Direct polynomial evaluation gives
\(F_{5,2}(1)=109\), \(G_{5,2}(1)=89\). Therefore

\[
A_6=3,\qquad A_{30}=1+2\cdot109^2=3\cdot89^2,
\]

and the positive product root \(267\) equals the supplied product modulo
\(N\). The shared factor \(3\mid1-109\) is minus-labelled.

The preserved F253 certificate has the same \(D,y_i,y_j,A_i,A_j\), but
\(N=143,x_i=17,x_j=5\). Its positive root is again \(267\), while

\[
\gcd(267-85,143)=13,\qquad
\gcd(267+85,143)=11.
\]

It is a non-global minus-channel relation. It had earlier cleanup factors
and is used only to prove that the coordinate label does not determine the
root sign.

All algorithms in the statement use exact arithmetic, gcds, Jacobi symbols,
and binary parity. No integer factorization or probability heuristic occurs
in the proof.
