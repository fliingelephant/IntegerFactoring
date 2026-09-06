# F144 V2 proof — residual cycles and the square-root-scale obstruction

## 1. One legal bridge

For one legal P128 squared-anchor word, put

\[
U=qa^2,
\qquad
c=[U]_N,
\qquad
w=\iota_N(c),
\qquad
U=c+tN.
\]

P128 retains the actual relation values

\[
C=cw,
\qquad
L=Uw.
\]

Their product satisfies

\[
CL=Uc\,w^2.
\tag{1}
\]

If another current named block \(r\ne q\) divides \(c\), write

\[
c=rT.
\tag{2}
\]

This gives a directed containment edge \(q\to r\), with anchor \(a\) and
residual \(T\).  Every displayed integer is a unit modulo \(N\).

## 2. One directed cycle

Let \(\mathcal C\) be a directed containment cycle.  Define

\[
Q_{\rm tail}=\prod_{e\in\mathcal C}q_e,
\qquad
Q_{\rm head}=\prod_{e\in\mathcal C}r_e,
\]

\[
A_{\mathcal C}=\prod_{e\in\mathcal C}a_e,
\qquad
T_{\mathcal C}=\prod_{e\in\mathcal C}T_e.
\]

The tail and head vertex multisets are equal around a directed cycle, so

\[
Q_{\rm tail}=Q_{\rm head}=:Q_{\mathcal C}.
\tag{3}
\]

The raw and reduced endpoint products are therefore

\[
\prod_{e\in\mathcal C}U_e
=Q_{\mathcal C}A_{\mathcal C}^{\,2},
\qquad
\prod_{e\in\mathcal C}c_e
=Q_{\mathcal C}T_{\mathcal C}.
\tag{4}
\]

Each \(U_e\equiv c_e\pmod N\).  Multiplication and cancellation of the unit
\(Q_{\mathcal C}\) modulo \(N\) give

\[
A_{\mathcal C}^{\,2}\equiv T_{\mathcal C}\pmod N.
\tag{5}
\]

This proves

\[
N\mid A_{\mathcal C}^{\,2}-T_{\mathcal C}.
\tag{6}
\]

Every canonical reduction satisfies \(U_e=c_e+t_eN\ge c_e\).  Hence (4)
gives

\[
A_{\mathcal C}^{\,2}\ge T_{\mathcal C}.
\tag{7}
\]

Equality in a product of positive termwise inequalities holds exactly when
every \(t_e=0\).  If at least one edge wraps, (7) is strict.  The positive
integer in (6) is then at least \(N\):

\[
A_{\mathcal C}^{\,2}-T_{\mathcal C}\ge N.
\tag{8}
\]

Since \(T_{\mathcal C}\ge1\),

\[
A_{\mathcal C}^{\,2}\ge N+T_{\mathcal C}>N,
\qquad
A_{\mathcal C}>\sqrt N.
\tag{9}
\]

This proves the square-root-scale obstruction without a residual-square
assumption.

## 3. A collection of cycles and its exact root

Select a nonempty indexed collection of directed cycles.  Products below
count logical edge occurrences, including an edge shared by two cycles.
Put

\[
Q_{\rm tail}=\prod_eq_e,
\qquad
Q_{\rm head}=\prod_er_e,
\qquad
\mathcal A=\prod_ea_e,
\qquad
\mathcal T=\prod_eT_e,
\qquad
W=\prod_ew_e.
\]

Every cycle balances its tail and head multiset.  Thus

\[
Q_{\rm tail}=Q_{\rm head}=:Q.
\tag{10}
\]

Also

\[
\prod_ec_e=Q\mathcal T.
\tag{11}
\]

Suppose \(\mathcal T=S^2\).  Multiply (1) over all occurrences and use
(10)--(11):

\[
\prod_eC_eL_e
=Q^2\mathcal A^2S^2W^2
=(Q\mathcal A S W)^2.
\tag{12}
\]

The actual P128 relation values therefore have the positive exact root

\[
R_0=Q\mathcal A S W.
\tag{13}
\]

Since \(w_e\equiv c_e^{-1}\pmod N\), equation (11) gives

\[
W\equiv(QS^2)^{-1}\pmod N.
\]

Substitute this in (13):

\[
R_0\equiv\mathcal A S^{-1}\pmod N.
\tag{14}
\]

Squaring gives

\[
\mathcal A^2\equiv S^2\pmod N.
\tag{15}
\]

If at least one selected occurrence wraps, termwise product comparison gives

\[
Q\mathcal A^2
=\prod_eU_e
>
\prod_ec_e
=QS^2.
\]

Thus \(\mathcal A>S\).  Equations (15) and positivity give

\[
\mathcal A^2-S^2=mN
\tag{16}
\]

for an integer \(m\ge1\).  Therefore

\[
\mathcal A^2\ge N+S^2>N,
\qquad
\mathcal A>\sqrt{N+S^2}>\sqrt N.
\tag{17}
\]

If no selected occurrence wraps, the product comparison is an equality,
so \(\mathcal A=S\), and (14) is the global root \(+1\).

For later use, apply Section 2 to each indexed cycle separately.  An
unwrapped cycle has

\[
T_{\mathcal C}=A_{\mathcal C}^{\,2}.
\tag{17a}
\]

It therefore contributes a square residual and normalized root \(+1\).
If two indexed cycles \(\mathcal C_1,\mathcal C_2\) each contain a wrapped
edge, (9) gives

\[
A_{\mathcal C_1}>\sqrt N,
\qquad
A_{\mathcal C_2}>\sqrt N.
\]

The total logical anchor product of any collection containing both satisfies

\[
\mathcal A
\ge A_{\mathcal C_1}A_{\mathcal C_2}
>N.
\tag{17b}
\]

It cannot meet \(2\mathcal A<N\).

Now suppose exactly one selected cycle \(\mathcal C_0\) is wrapped.  The
product of all unwrapped residuals is the square
\(\prod_{\mathcal C\ne\mathcal C_0}A_{\mathcal C}^2\).  Hence the combined
residual is a square if and only if \(T_{\mathcal C_0}\) is a square.
When \(T_{\mathcal C_0}=S_0^2\), the combined formula (14) reduces to

\[
\frac{
A_{\mathcal C_0}\prod_{\mathcal C\ne\mathcal C_0}A_{\mathcal C}
}{
S_0\prod_{\mathcal C\ne\mathcal C_0}A_{\mathcal C}
}
\equiv A_{\mathcal C_0}S_0^{-1}\pmod N.
\tag{17c}
\]

Thus unwrapped cycles provide neither residual closure nor a new root for
one wrapped cycle.  A combination of two or more wrapped cycles remains a
valid P66 possibility, but this metric argument cannot certify it.

## 4. The useful metric interval

Assume the wrapped case and also \(2\mathcal A<N\).  Then

\[
0<\mathcal A-S<\mathcal A+S<2\mathcal A<N.
\tag{18}
\]

Equation (15) says that \(N\) divides
\((\mathcal A-S)(\mathcal A+S)\).  Neither factor in (18) is divisible by
\(N\).  If one factor were a unit modulo \(N\), the other would be zero
modulo \(N\), also impossible by (18).  Hence

\[
1<\gcd(\mathcal A-S,N)<N,
\qquad
1<\gcd(\mathcal A+S,N)<N.
\tag{19}
\]

This proves the exact factor conclusion.  Combining (17) and the added
bound gives the nonempty possible interval

\[
\sqrt N<\mathcal A<N/2.
\]

## 5. Global exact-value deletion

The logical bridge selection restores the actual canonical and lifted
values before deduplication.  If one exact integer \(P\) occurs twice,
remove those two occurrences.  The selected product is divided by the
square \(P^2\), so it remains an exact square.  Its positive root is divided
by \(P\equiv1\pmod N\), and its residue is unchanged.

Repeat until each exact value has multiplicity zero or one.  Use the
globally retained representative for every odd multiplicity.  This produces
a legal dependency in the deduplicated P128 ledger with the same normalized
root (14).  Under (17)--(19), it cannot be the zero dependency.

## 6. Parameter consequences

If one directed cycle has length \(k\) and every anchor is at most \(H\),
then

\[
A_{\mathcal C}\le H^k.
\]

The wrapped-cycle bound (9) therefore requires

\[
H^k>\sqrt N,
\qquad
k>{\log N\over2\log H}.
\tag{20}
\]

Now let \(n=\lceil\log_2(N+1)\rceil\).  If the total raw anchor product is
at most

\[
2^{(\log n)^d}
\]

for one fixed \(d\), then its base-two logarithm is
\((\log n)^d=o(n)\).  Meanwhile
\(\log_2\sqrt N=\Theta(n)\).  Thus (9) fails for all sufficiently large
\(n\), and no wrapped positive cycle exists in that family.

For anchors \(a\le n^3\), inequality (20) only gives the lower bound

\[
k>{\log_2N\over6\log_2n}.
\tag{21}
\]

This is \(\Omega(n/\log n)\), which is polynomial in \(n\).  Constructing
and testing one specified path of this length uses polynomially many
positions.  The theorem does not provide such a path or show that exhaustive
path search is quasipolynomial.

The full F130 caps are wider still.  A word has at most
\(D=\lceil\log_2(n+1)\rceil^2\) named atoms, but its exponents can be as
large as \(E=2^D\).  A compactly represented raw square anchor can therefore
have quasipolynomial bit length and integer magnitude far above
\(\sqrt N\).  The cost theorem bounds representation length and arithmetic
work; it does not bound the represented integer by
\(2^{\operatorname{polylog}n}\).  Hence (9) does not close the complete
P128 source.

## 7. The \(N=35\) certificate

Take

\[
N=35,\quad q=13,\quad r=17,\quad a=2,\quad b=3.
\]

The two raw words reduce as

\[
13\cdot2^2=52=17+35,
\qquad
17\cdot3^2=153=13+4\cdot35.
\]

They give the directed cycle

\[
13\longrightarrow17\longrightarrow13
\]

with residuals \(1,1\).  The canonical inverses are

\[
\iota_{35}(17)=33,
\qquad
\iota_{35}(13)=27.
\]

The four actual relation values are

\[
C_1=17\cdot33=561,
\qquad
L_1=52\cdot33=1716,
\]

\[
C_2=13\cdot27=351,
\qquad
L_2=153\cdot27=4131.
\]

Direct multiplication gives

\[
C_1L_1C_2L_2=1181466^2.
\]

Here \(\mathcal A=2\cdot3=6\), \(S=1\), and

\[
1181466\equiv6\pmod{35}.
\]

Thus

\[
\gcd(6-1,35)=5,
\qquad
\gcd(6+1,35)=7.
\]

Also \(6^2-1=35\), so this certificate attains the minimum positive
multiple \(m=1\) in (16).

The blocks \(13,17\) are pairwise coprime units and the anchors \(2,3\) are
eligible primes.  Each word has support two and exponents \(1,2\).
Therefore the positions are legal conditional on \(13,17\) being current
blocks in one frozen P128 stage.  The certificate makes no claim that the
actual \(N=35\) preprocessing or P118 transcript reaches that basis.

## 8. Proportional carries give root \(+1\)

For two arbitrary cross-star endpoints, write

\[
c=qa^2-tN,
\qquad
d=rb^2-sN,
\]

and define

\[
\Delta=sc-td.
\]

Substitution gives

\[
\Delta=qa^2s-rb^2t.
\tag{22}
\]

If \(h=\gcd(c,d)\), then \(h\mid\Delta\).  The carry bounds

\[
0\le t<{qa^2\over N},
\qquad
0\le s<{rb^2\over N}
\]

give

\[
|\Delta|<{qr a^2b^2\over N}.
\tag{23}
\]

If \(\Delta=0\) and \(t=0\), then \(s=0\), and both bridges are individual
exact squares with root \(+1\).

Otherwise \(t,s>0\).  Put

\[
g=\gcd(t,s),
\qquad
t=g\tau,
\qquad
s=g\sigma,
\qquad
\gcd(\tau,\sigma)=1.
\]

The equation \(\Delta=0\) gives \(\sigma c=\tau d\).  Hence

\[
c=\tau z,
\qquad
d=\sigma z
\]

for one positive integer \(z\).  With \(Z=z+gN\),

\[
qa^2=\tau Z,
\qquad
rb^2=\sigma Z.
\]

The bridge product is

\[
(qa^2c)(rb^2d)=(\tau\sigma Zz)^2.
\]

Its supplied-root product is \(cd=\tau\sigma z^2\), so its normalized root
is

\[
Zz^{-1}\equiv1\pmod N.
\]

Thus a zero carry determinant is a global \(+1\) dependency.  Moreover,
if \(hN\ge qr a^2b^2\), then (23) gives
\(|\Delta|<h\); divisibility by \(h\) forces \(\Delta=0\).

## 9. P114 rectangle boundary

For two centers \(q,r\) and anchors \(a,b\), put

\[
x_{00}=[qa^2]_N,\quad
x_{10}=[ra^2]_N,\quad
x_{01}=[qb^2]_N,\quad
x_{11}=[rb^2]_N.
\]

Let

\[
u=x_{00},
\qquad
\alpha=[rq^{-1}]_N,
\qquad
\beta=[b^2a^{-2}]_N.
\]

Then

\[
[u\alpha]_N=x_{10},
\qquad
[u\beta]_N=x_{01},
\qquad
[u\alpha\beta]_N=x_{11}.
\]

These four endpoints are exactly one P114 multiplicative rectangle.  Its
inverse-carry determinant remains subject to P115--P116.  No density or
all-input hit claim follows from this embedding.

## 10. Remaining limitation

The proof gives no selector for a characteristic-scale anchor product, no
polynomial-length cycle-existence theorem, and no residual-square law at
that scale.  It also does not control arithmetic hypercycles outside stored
positive-direction containment cycles.
