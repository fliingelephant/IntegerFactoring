# Proof of F210 V2

## 1. The two legal lift pairs

Throughout, \(m=2^t\) with \(t\ge1\). In particular, \(m\) is even.
Write the hidden factors as

\[
p=r+mP,
\qquad
q=c+mQ
\tag{45}
\]

for nonnegative integers \(P,Q\). Expanding their product gives

\[
N=rc+m(rQ+cP)+m^2PQ
\tag{46}
\]

and hence

\[
K=rQ+cP+mPQ.
\tag{47}
\]

Let \(a=P\bmod2\) and \(b=Q\bmod2\). Since \(r,c\) are odd and \(m\)
is even,

\[
\delta\equiv K\equiv P+Q\equiv a+b\pmod2.
\tag{48}
\]

For bits, equation (48) is exactly

\[
b=a\mathbin{\mathsf{xor}}\delta.
\tag{49}
\]

This proves that (7) lists the two legal lift pairs and that the true next
bit is one of them. The value \(a=P\bmod2\) is unique.

For either legal pair, expansion gives

\[
\begin{aligned}
N-r_ac_a
&=N-(r+am)(c+b_am)\\
&=m(K-ac-b_ar-ab_am).
\end{aligned}
\tag{50}
\]

The integer in parentheses is even by (48)--(49), so \(K_a\) is integral.
Also

\[
0<r_a,c_a<2m<p.
\tag{51}
\]

Therefore \(r_ac_a<p^2<N\), proving

\[
0<K_a={N-r_ac_a\over2m}<{N\over2m}.
\tag{52}
\]

Because \(2m\) is coprime to the odd number \(N\),

\[
\begin{aligned}
\gcd(K_a,N)
&=\gcd(2mK_a,N)\\
&=\gcd(N-r_ac_a,N)\\
&=\gcd(r_ac_a,N)=1.
\end{aligned}
\tag{53}
\]

The final equality uses (51): neither positive factor can be divisible by
\(p\) or \(q\). This proves (9).

## 2. Exact formulas and common support

If \(\delta=0\), equation (49) gives \(b_a=a\). Substitution into (50)
gives

\[
K_0={K\over2},
\qquad
K_1={K-r-c-m\over2}.
\tag{54}
\]

If \(\delta=1\), then \(b_a=1-a\), so

\[
K_0={K-r\over2},
\qquad
K_1={K-c\over2}.
\tag{55}
\]

The residue entries in (10)--(11) follow directly from (7). Subtracting
(54) or (55) proves (13).

For \(\delta=0\), the difference is strictly positive. For \(\delta=1\),
it vanishes exactly when \(r=c\). This proves (14). At the first permitted
stage \(t=1\), one has \(m=2\), and the only canonical odd residue is one.
If \(N\equiv3\pmod4\), then

\[
K={N-1\over2}\equiv1\pmod2.
\]

Equation (55) then gives (15).

Outside coalescence, the elementary identity

\[
\gcd(A,B)=\gcd(A,A-B)=\gcd(B,A-B)
\tag{56}
\]

proves (17). Since \(1\le r,c\le m-1\),

\[
0<{r+c+m\over2}\le{3m-2\over2}<{3m\over2}.
\tag{57}
\]

When \(r\ne c\), both are odd, so \(|r-c|\le m-2\), giving

\[
0<{|c-r|\over2}\le{m-2\over2}<{m\over2}.
\tag{58}
\]

Equations (57)--(58) prove (18). Finally, for any two positive integers,

\[
\gcd(K_0,K_1)\operatorname{lcm}(K_0,K_1)=K_0K_1,
\]

which proves (19), including the coalesced case.

## 3. Half-translation identity

From (7),

\[
r_1-r_0=m={h\over2}.
\tag{59}
\]

For the second coordinate,

\[
c_1-c_0=
\begin{cases}
m,&\delta=0,\\
-m,&\delta=1,
\end{cases}
=\sigma{h\over2}.
\tag{60}
\]

The difference formulas also give the uniform identity

\[
K_0-K_1
={c_1\over2}+{\sigma r_1\over2}-{\sigma h\over4}.
\tag{61}
\]

For \(\delta=0\), the right side is
\((c+m+r+m-m)/2=(r+c+m)/2\). For \(\delta=1\), it is
\((c-r-m+m)/2=(c-r)/2\). Thus (61) is exactly (13) in both cases.

Now expand the left side of (22):

\[
\begin{aligned}
F_1(P-1/2,Q-\sigma/2)
={}&hPQ+(c_1-\sigma h/2)P+(r_1-h/2)Q\\
&+{\sigma h\over4}-{c_1\over2}
-{\sigma r_1\over2}-K_1.
\end{aligned}
\tag{62}
\]

Equations (59)--(61) reduce (62) to

\[
hPQ+c_0P+r_0Q-K_0=F_0(P,Q),
\]

which proves (22).

Direct matrix multiplication in (24) gives first row

\[
(r_0+h/2,h)=(r_1,h),
\]

and second row

\[
\left(-K_0+{c_0+\sigma r_0\over2}+{\sigma h\over4},
c_0+{\sigma h\over2}\right)=(-K_1,c_1),
\]

where the first coordinate again uses (61). Thus (24) holds. Moreover,

\[
\det A_a=r_ac_a+hK_a=N,
\tag{63}
\]

which proves (23).

For the physical coordinates (25), direct expansion gives the polynomial
identity

\[
XY-N=hF_a(P,Q).
\tag{64}
\]

Over \(\mathbb Z[1/2]\), the power \(h=2^{t+1}\) is a unit. The coordinate
change (25) is therefore invertible, and (64) identifies both quotient
curves with the same hyperbola \(XY=N\). Over an odd modulus, both \(2\)
and \(h\) are units. This proves the claimed bijections and every
coordinate-invariant consequence listed after (26). In particular, an
aligned elimination calculation receives the same equation on both sides;
it cannot distinguish their original labels.

This argument deliberately does not compare statistics tied to the two
different integral coefficient lists or to the two different sets of prime
divisors of \(K_a\). Such statistics are not invariants under (22).

## 4. What a child prime power supplies

Let \(\ell^e\mid K_a\) with \(\ell\) odd. Equation (53) shows that
\(\ell\nmid N\). Reducing (8) gives

\[
N\equiv r_ac_a\pmod {\ell^e}.
\tag{65}
\]

The right side is a unit, so both \(r_a,c_a\) are units. Applying a
multiplicative character to (65) proves (28). Multiplying (65) by
\(r_ac_a^{-1}\) gives

\[
Nr_ac_a^{-1}\equiv r_a^2\pmod {\ell^e},
\]

which proves (29). This is a scaled root forced by the product congruence;
it says nothing by itself about whether \(N\) is a square modulo
\(\ell^e\).

## 5. Equal finite 2-adic lift counts and the exact integer distinction

Fix \(s\ge t+1\), with \(t\ge1\) as in (3). There are exactly

\[
2^{s-(t+1)}=2^{s-t-1}
\tag{66}
\]

residues \(X\bmod2^s\) satisfying \(X\equiv r_a\pmod h\). Every one is
odd, hence a unit. For each such \(X\), define the unique residue

\[
Y=NX^{-1}\pmod {2^s}.
\tag{67}
\]

Reduction modulo \(h\) and the legal-lift congruence

\[
r_ac_a\equiv N\pmod h
\tag{68}
\]

give

\[
Y\equiv Nr_a^{-1}\equiv c_a\pmod h.
\tag{69}
\]

Conversely, every pair in \(\mathcal S_a(s)\) arises from exactly one such
\(X\). Equations (66)--(69) prove (31).

We now prove the repaired integral statement. Suppose an integer point in
one chart has physical coordinates satisfying

\[
1<X<\sqrt N<Y<N,
\qquad XY=N.
\tag{70}
\]

The positive divisors of the promised squarefree semiprime \(N=pq\) are
exactly \(1,p,q,N\). Since \(p<q\), one has
\(p<\sqrt N<q\). The inequalities in (70) therefore force

\[
(X,Y)=(p,q).
\tag{71}
\]

The residues of \((p,q)\) modulo \(h=2m\) are exactly the unique true
next-lift pair \((r_a,c_a)\), so (71) occurs in the true chart. The two
candidate pairs have distinct first residues modulo \(h\), because
\(r_1-r_0=m\not\equiv0\pmod h\). Hence the false chart cannot contain
\((p,q)\). This proves that the true chart is the unique chart satisfying
(70).

In coalescence, \(\delta=1\) and \(r=c\). The two residue pairs are then

\[
(r_0,c_0)=(r,r+m),
\qquad
(r_1,c_1)=(r+m,r).
\tag{72}
\]

Swapping \((p,q)\) swaps these two residue pairs. Thus the other chart
contains \((q,p)\), but \(q>\sqrt N>p\), so it violates (70). A false
chart may also contain a trivial endpoint. For example, if its residue
classes admit \((1,N)\), then that point satisfies
\(X<\sqrt N<Y\) but violates both \(1<X\) and \(Y<N\). The proof therefore
makes no uniqueness claim after either endpoint restriction is removed.

This is the sharp distinction established here: finite congruence
feasibility is path-blind, while the nontrivial balanced integer point is
path-selective. F210 V2 gives no efficient algorithm for detecting that
point.

## 6. The conditional order bridge

Equation (32) and the supplied factorizations show that both \(H_a\) are
fully factored: append the known power of two \(h\) to the factorization of
\(K_a\). Their gcd is

\[
\gcd(hK_0,hK_1)=h\gcd(K_0,K_1)=hg,
\]

proving (33), including coalescence.

Let

\[
o_p=\operatorname{ord}_p(w),
\qquad
o_q=\operatorname{ord}_q(w).
\tag{73}
\]

If (35) holds, then both local orders divide both \(H_0,H_1\), and hence

\[
o_p\mid G,
\qquad
o_q\mid G.
\tag{74}
\]

The congruence \(w^G=1\pmod N\) also follows from Bezout applied to
\(H_0,H_1\), using \(w^{-1}\) because \(w\) is a unit.

For completeness, factor-first stripping works as follows. Start from the
fully factored annihilator \(E=G\). For every prime \(\ell\mid E\), test

\[
z=w^{E/\ell}\pmod N,
\qquad
d=\gcd(z-1,N).
\tag{75}
\]

If \(d=N\), replace \(E\) by \(E/\ell\) and repeat. A proper \(d\) factors
\(N\). If \(d=1\), retain that copy of \(\ell\) and proceed to the next
prime. Suppose no factor occurs. At termination, for every prime
\(\ell\mid E\), neither local order divides \(E/\ell\), while both divide
\(E\). Therefore the \(\ell\)-adic valuation of each local order equals
that of \(E\). This holds for every prime of \(E\), so

\[
o_p=o_q=E.
\tag{76}
\]

Set \(e=E\). This proves (36).

By (53), \(g\) is coprime to \(N\). The power of two \(h\) is also coprime
to odd \(N\), so

\[
\gcd(G,N)=1.
\]

Equation (37) follows from \(e\mid G\). The P172 interface applied under
(38) proves the terminal claim.

The standard cyclotomic identity

\[
\gcd_{\mathbb Z[X]}(X^A-1,X^B-1)
=X^{\gcd(A,B)}-1
\tag{77}
\]

with \(A=H_0,B=H_1\) proves (39). Since \(X-1\) is always a common factor,
the ordinary resultant of the two displayed polynomials is zero. Thus an
unaltered resultant does not improve on the common-factor calculation.

## 7. Recursion accounting

The bit-length convention gives

\[
N+1\le2^n,
\qquad N<2^n.
\tag{78}
\]

Together with (52), this yields, for every permitted \(t\ge1\),

\[
K_a<{N\over2^{t+1}}<2^{n-t-1},
\]

which is (40). If \(t\ge\eta n-C_0\) for one fixed \(C_0\), the input bit
length of \(K_a\) is at most

\[
n-t-1\le(1-\eta)n+C_0-1.
\tag{79}
\]

This proves (42).

A numerical-QP number of calls at the bound (79) is absorbed into the
coefficient \(Q(n)\). Together with at most one decrement-spine call, the
resulting recurrence is exactly (43), so P183 proves it numerical QP.

Finally,

\[
2^{n-1}<N+1\le2^n
\]

implies \(\log_2N=n+O(1)\). Substituting (44) into (40) gives child bit
length at most

\[
{3n\over4}+(\log n)^{O(1)}.
\tag{80}
\]

For every fixed \(\rho>3/4\), equation (80) is at most \(\rho n\) after a
finite prefix. This proves the P175-scale statement.

Nothing in this accounting constructs the prefix (4). At \(t=o(n)\), the
bound \(n-t-1\) is \(n-o(n)\), so two recursively factored children need
not be fixed-ratio side work. The valid single-chain recurrence remains
\(T(n)\le T(n-1)+Q(n)\); F210 V2 supplies no rule that realizes it.

