# Generic specialization decoys

## Theorem

Let \(N\ge 3\) be odd. Let \(A_1(T),\ldots,A_m(T)\in\mathbb Q[T]\setminus\{0\}\) satisfy

\[
A_i(0)=1,
\qquad
a_i:=A_i(N)\in\mathbb Z_{>0},
\qquad
a_i\equiv1\pmod N.
\]

For \(c\in\mathbb F_2^m\), put

\[
A_c(T)=\prod_i A_i(T)^{c_i},
\qquad
a_c=\prod_i a_i^{c_i}.
\]

Define

\[
K_{\mathrm{gen}}
=\{c:A_c(T)\text{ is a square in }\mathbb Q(T)\}
\]

and

\[
K_N
=\{c:a_c\text{ is a square in }\mathbb Z\}.
\]

Let \(D_i\) be the least positive coefficient denominator of \(A_i\). For \(c\in K_{\mathrm{gen}}\), let \(d_c\) be the least positive coefficient denominator of either polynomial square root of \(A_c\), and define

\[
U_N=\{c\in K_{\mathrm{gen}}:\gcd(d_c,N)=1\}.
\]

Both are binary linear spaces. The following claims hold.

1. \(K_{\mathrm{gen}}\subseteq K_N\).
2. If \(c\in K_{\mathrm{gen}}\), write \(A_c(T)=S_c(T)^2\), and let \(d_c\) be the least positive integer for which \(d_cS_c(T)\in\mathbb Z[T]\). If \(\gcd(d_c,N)=1\), then the positive numeric root
   \[
   R_N(c)=\sqrt{a_c}
   \]
   satisfies \(R_N(c)\equiv\pm1\pmod N\).
3. The exact denominator identity is
   \[
   d_c^2=\prod_iD_i^{c_i}\qquad(c\in K_{\mathrm{gen}}).
   \]
   Hence \(U_N\) is a computable binary subspace. The numeric-root map, after quotienting its image by the global signs \(\{\pm1\}\), factors through \(K_N/U_N\).
4. If some basis of the complete numeric kernel \(K_N\) lies in \(U_N\), then every numeric square relation has root \(\pm1\pmod N\). Thus every numeric relation is a global decoy.
5. The denominator hypothesis is necessary. For \(N=15\), a one-polynomial example with denominator \(5\) has a generic square whose positive numeric root is neither global sign.

The quotient \(K_N/U_N\) is the exact quotient forced by generic unit-denominator information. It is not necessarily the exact factor-bearing quotient: additional global decoys can lie outside \(U_N\). The exact root-image quotient is \(K_N/\ker(\bar\rho_N)\), defined below.

Here “global decoy” means that comparison with the known square root \(1\) of every \(a_i\bmod N\) produces only the two global roots \(\pm1\), and hence no proper gcd split.

## 1. A rational-function square root is a polynomial

Suppose \(F(T)\in\mathbb Q[T]\setminus\{0\}\) and \(F=S^2\) in \(\mathbb Q(T)\). Write \(S=P/Q\) with coprime \(P,Q\in\mathbb Q[T]\). Then

\[
P^2=FQ^2.
\]

If a nonconstant irreducible polynomial divided \(Q\), unique factorization in \(\mathbb Q[T]\) would force it to divide \(P^2\), hence \(P\), contrary to coprimality. Therefore \(Q\) is a unit and

\[
S\in\mathbb Q[T].
\]

This removes possible poles at \(T=N\). It also makes the coefficient denominator \(d_c\) well-defined. Replacing \(S_c\) by \(-S_c\) does not change \(d_c\).

## 2. Generic relations specialize to integer-square relations

Take \(c\in K_{\mathrm{gen}}\), and choose \(S_c\in\mathbb Q[T]\) with \(S_c^2=A_c\). Evaluation at \(N\) gives

\[
S_c(N)^2=A_c(N)=a_c\in\mathbb Z_{>0}.
\]

A rational number whose square is an integer is itself an integer. Indeed, if \(p/q\) is in lowest terms and \((p/q)^2\in\mathbb Z\), then \(q^2\mid p^2\), so \(q=1\). Consequently,

\[
S_c(N)\in\mathbb Z,
\qquad
a_c=S_c(N)^2,
\]

and \(c\in K_N\). This proves

\[
\boxed{K_{\mathrm{gen}}\subseteq K_N.}
\]

The positivity of the \(a_i\) ensures that the positive root is

\[
R_N(c)=|S_c(N)|.
\]

## 3. A unit coefficient denominator forces a global sign

Since every \(A_i(0)=1\),

\[
S_c(0)^2=A_c(0)=1.
\]

Thus \(S_c(0)=\varepsilon_c\) for some \(\varepsilon_c\in\{1,-1\}\).

Let

\[
P_c(T)=d_cS_c(T)\in\mathbb Z[T].
\]

Evaluation of an integer polynomial at \(N\) is congruent to its constant term, so

\[
d_cS_c(N)=P_c(N)
\equiv P_c(0)
=d_c\varepsilon_c
\pmod N.
\]

If \(\gcd(d_c,N)=1\), cancellation modulo \(N\) is valid and gives

\[
S_c(N)\equiv\varepsilon_c\pmod N.
\]

Taking the absolute value can change only the global sign. Therefore

\[
\boxed{R_N(c)\equiv\pm1\pmod N.}
\]

The use of the *least* denominator matters. An arbitrary nonleast multiple of \(d_c\) could introduce a spurious common factor with \(N\).

## 4. Exact denominator arithmetic

For a nonzero rational polynomial

\[
F(T)=\sum_j f_jT^j
\]

and a rational prime \(p\), define the coefficient valuation

\[
\mu_p(F)=\min_j v_p(f_j).
\]

Gauss's lemma in valuation form gives

\[
\mu_p(FG)=\mu_p(F)+\mu_p(G).
\]

One direct proof is to scale each polynomial so that its minimum coefficient valuation is zero. Each scaled polynomial then has a nonzero reduction in \(\mathbb F_p[T]\). Their product is nonzero because \(\mathbb F_p[T]\) is a domain, so the product also has minimum valuation zero.

If \(F(0)=\pm1\), then \(\mu_p(F)\le0\), and the exponent of \(p\) in the least coefficient denominator \(D(F)\) is exactly

\[
v_p(D(F))=-\mu_p(F).
\]

Every \(A_i\), every product \(A_c\), and every symbolic root \(S_c\) has constant term \(1\) or \(\pm1\). Therefore

\[
D(A_c)=\prod_iD_i^{c_i}
\]

and

\[
D(S_c^2)=D(S_c)^2=d_c^2.
\]

Since \(A_c=S_c^2\), these are the same denominator. Hence

\[
\boxed{d_c^2=\prod_iD_i^{c_i}.}
\]

There is no hidden coefficient cancellation in this identity. The constant-term-one hypothesis is what converts the additive Gauss valuations into multiplicative positive denominators.

Let

\[
B_N=\{i:\gcd(D_i,N)>1\}.
\]

The denominator identity gives

\[
\gcd(d_c,N)=1
\quad\Longleftrightarrow\quad
c_i=0\text{ for every }i\in B_N.
\]

Consequently,

\[
\boxed{
U_N=K_{\mathrm{gen}}\cap
\{c\in\mathbb F_2^m:c_i=0\text{ for all }i\in B_N\}.
}
\]

Thus \(U_N\) is a binary subspace, not merely a set whose span must later be taken.

It is also computable from the exact input. Compute each \(D_i\) as the least common multiple of the reduced coefficient denominators and compute \(\gcd(D_i,N)\). Compute \(K_{\mathrm{gen}}\) by a gcd-free refinement in \(\mathbb Q[T]\), normalize every block to have value one at \(T=0\), remove polynomial-square powers, and apply binary linear algebra to the remaining block exponents. Equivalently, one can factor the polynomials over \(\mathbb Q\) and record irreducible-factor parities. Intersect that kernel with the coordinate equations \(c_i=0\) for \(i\in B_N\). This computation does not require factoring \(N\).

## 5. The numeric-root homomorphism

Let

\[
\mathcal T_N
=\{u\in(\mathbb Z/N\mathbb Z)^\times:u^2=1\}.
\]

For \(c\in K_N\), define

\[
\rho_N(c)=R_N(c)\pmod N.
\]

This lies in \(\mathcal T_N\), because

\[
R_N(c)^2=a_c\equiv1\pmod N.
\]

It is a homomorphism. For \(c,e\in K_N\), let \(c\oplus e\) be binary addition and put

\[
J(c,e)=\prod_{i:c_i=e_i=1}a_i.
\]

There is an exact identity

\[
a_ca_e=a_{c\oplus e}J(c,e)^2.
\]

All terms are positive squares, so their positive roots satisfy

\[
R_N(c)R_N(e)=R_N(c\oplus e)J(c,e).
\]

But every \(a_i\equiv1\pmod N\), hence \(J(c,e)\equiv1\pmod N\). It follows that

\[
\rho_N(c\oplus e)=\rho_N(c)\rho_N(e).
\]

This is the specialization version of the normalized-root homomorphism: the usual intersection correction disappears modulo \(N\) because all source values specialize to one.

Since \(N\) is odd, \(\{1,-1\}\) is a two-element subgroup of \(\mathcal T_N\). Let

\[
q:\mathcal T_N\longrightarrow \mathcal T_N/\{\pm1\}
\]

be the quotient map. The unit-denominator result says that \(q\circ\rho_N\) kills every vector of \(U_N\). By the universal property of a quotient, there is a unique homomorphism

\[
\widetilde\rho_N:K_N/U_N\longrightarrow\mathcal T_N/\{\pm1\}
\]

such that

\[
q\circ\rho_N=\widetilde\rho_N\circ\pi,
\]

where \(\pi:K_N\to K_N/U_N\) is the projection. This proves the forced factorization claim.

If a basis of \(K_N\) lies in \(U_N\), then \(U_N=K_N\). The quotient is zero, so \(q\circ\rho_N\) is trivial on every numeric relation. Equivalently,

\[
R_N(c)\equiv\pm1\pmod N
\qquad(c\in K_N).
\]

This conclusion uses a basis of the *complete* numeric kernel. A basis of only \(K_{\mathrm{gen}}\), or an incomplete list of numeric relations, is not sufficient.

There is an important distinction between a quotient through which the signal map factors and the exact signal quotient. Put

\[
Z_N=\ker(q\circ\rho_N)
=\{c\in K_N:R_N(c)\equiv\pm1\pmod N\}.
\]

Then \(U_N\subseteq Z_N\), but equality need not hold. The exact quotient that classifies distinct factor-bearing root images is

\[
\boxed{K_N/Z_N\cong\operatorname{im}(q\circ\rho_N).}
\]

The quotient \(K_N/U_N\) is a computable residual search space certified by generic specialization. It can still contain nonzero classes that map to the identity and are therefore global decoys.

## 6. Why a nonunit denominator cannot be omitted

Take

\[
N=15,
\qquad
S(T)=1+\frac{T}{5},
\qquad
A(T)=S(T)^2.
\]

Then

\[
A(0)=1,
\qquad
A(15)=4^2=16>0,
\qquad
16\equiv1\pmod {15}.
\]

Thus the singleton vector lies in both \(K_{\mathrm{gen}}\) and \(K_{15}\). Its positive numeric root is

\[
R_{15}=4,
\]

which is neither \(1\) nor \(-1\equiv14\pmod {15}\). Indeed,

\[
\gcd(4-1,15)=3,
\qquad
\gcd(4+1,15)=5.
\]

The least coefficient denominator is \(d=5\), and \(\gcd(d,15)=5\). The failed step is exactly cancellation of \(d\) modulo \(N\). The denominator condition therefore cannot be deleted.

In this example the nonunit denominator itself exposes a factor. In general, \(1<\gcd(d_c,N)<N\) is already useful, while \(\gcd(d_c,N)=N\) is still enough to invalidate modular cancellation but need not directly give a proper divisor.

The inclusion \(U_N\subseteq Z_N\) can be strict even for one source. Still with \(N=15\), take

\[
S_{\mathrm{dec}}(T)=1+T+\frac{T(T-15)}5
=1-2T+\frac{T^2}{5},
\qquad
A_{\mathrm{dec}}(T)=S_{\mathrm{dec}}(T)^2.
\]

Its least denominator is five, so the singleton generic relation is not in \(U_{15}\). But

\[
S_{\mathrm{dec}}(15)=16\equiv1\pmod {15}.
\]

Thus its nonzero class in \(K_{15}/U_{15}\) is still a global decoy. This proves that \(K_N/U_N\) need not be the exact factor-bearing quotient.

The case \(\gcd(d_c,N)=N\) has no uniform root conclusion. Two exact examples at \(N=15\) are

\[
S_-(T)=1+\frac{13T}{15},
\qquad
S_*(T)=1+\frac T5+\frac{T(T-15)}{15}
=1-\frac45T+\frac1{15}T^2.
\]

Both least denominators equal \(15\). Their squares have constant term one and specialize to positive integers congruent to one modulo \(15\). However,

\[
S_-(15)=14\equiv-1\pmod {15}
\]

is global, while

\[
S_*(15)=4\not\equiv\pm1\pmod {15}
\]

is factor-bearing. In both cases \(\gcd(d_c,N)=N\), which is not a proper divisor. Therefore this gcd case means only that denominator cancellation is unavailable; it predicts neither success nor failure.

## 7. Relation to gcd factoring

For odd \(N\), if \(r\in\mathcal T_N\) is not a global sign, then

\[
\gcd(r-1,N),\qquad \gcd(r+1,N)
\]

are complementary proper divisors. For each odd prime power dividing \(N\), the full prime power divides exactly one of \(r-1\) and \(r+1\). Thus the quotient by \(\{\pm1\}\) records exactly the possible non-global factoring signal.

If \(N\) is an odd prime power, \(\mathcal T_N=\{\pm1\}\), so every numeric relation is automatically global. Repeated prime factors do not affect any proof above.

## 8. Edge cases

- The zero vector belongs to both kernels. Its product and root are one, and its least denominator is one.
- A source value \(a_i=1\) is permitted. Its polynomial need not be the constant polynomial one.
- The polynomials can have negative values away from \(T=N\). Only their nonzero polynomial status, constant value one, and positive specialization are used.
- No evaluation pole can occur. The UFD argument first converts every rational-function square root into a polynomial.
- The two symbolic roots are \(S_c\) and \(-S_c\). They have the same least denominator and the same class modulo global signs.
- The theorem is a conditional decoy criterion. It does not assert that \(K_{\mathrm{gen}}=K_N\), that a generic basis spans the numeric kernel, or that non-global relations must exist.

## 9. Independent finite replay of F59-D02

### Scope and provenance lift

The only finite input used was

`experiments/F59_completion_bias_generic_decoder_scan/output/F59-D02.json`,

with SHA-256

`23c1272fdaebfd932fb727b75d73e47f46b34a0d468b761c39956b9075073b6e`.

No F59-D03 or F60 candidate/audit artifact was read.

For a recorded provenance branch with start offset \(c\), the numeric inverse-descent recurrence is

\[
u_0=N-c,
\qquad
v_j=u_j^{-1}\pmod N\quad(1\le v_j<N),
\qquad
k_j=\frac{u_jv_j-1}{N},
\qquad
u_{j+1}=k_j.
\]

The symbolic lift is forced step by step. Start with \(U_0(T)=T-c\). Given an affine \(U_j\) with \(q_j=U_j(0)\ne0\), let \(V_j\) be the unique affine polynomial satisfying

\[
V_j(0)=q_j^{-1},
\qquad
V_j(N)=v_j.
\]

Then

\[
K_j(T)=\frac{U_j(T)V_j(T)-1}{T}
\]

is affine, because the numerator has zero constant term, and

\[
K_j(N)=k_j.
\]

Set \(U_{j+1}=K_j\). Each selected relation therefore lifts to

\[
\mathcal A_j(T)=U_j(T)V_j(T)=1+T K_j(T),
\]

with

\[
\mathcal A_j(0)=1,
\qquad
\mathcal A_j(N)=u_jv_j=k_jN+1.
\]

The replay checked all 40 selected relations and all 61 recorded provenance branches, including duplicates. A duplicate quotient branch can use the same, reversed, or a distinct endpoint factorization. Every recorded duplicate nevertheless lifted to the same symbolic \(\mathcal A_j(T)\) as its selected primary branch.

### Five product identities and four arithmetic residual templates

Write every positive-at-\(N\) symbolic root as

\[
S(T)=\varepsilon+T H(T),
\qquad \varepsilon=S(0)\in\{\pm1\}.
\]

The 19 basis products use one formal endpoint identity and four distinct non-formal arithmetic identities.

The formal identity is

\[
(T^2-2T+1)=(T-1)^2,
\qquad
\varepsilon=-1,
\qquad
H_0(T)=1.
\]

The first arithmetic product is

\[
\begin{aligned}
&\left(\frac1{15}T^2-\frac8{15}T+1\right)
\left(\frac23T^2-\frac73T+1\right)
\left(\frac25T^2-\frac{11}5T+1\right)
=S_{15}(T)^2,\\
&S_{15}(T)=-1+T H_{15}(T),\\
&H_{15}(T)=\frac2{15}T^2-\frac{17}{15}T+\frac{38}{15}.
\end{aligned}
\]

Its least coefficient denominator is \(15\).

The second arithmetic product is

\[
\begin{aligned}
&\left(\frac1{230}T^2-\frac{33}{230}T+1\right)
\left(\frac7{10}T^2-\frac{71}{10}T+1\right)
\left(\frac7{23}T^2-\frac{162}{23}T+1\right)
=S_{230}(T)^2,\\
&S_{230}(T)=-1+T H_{230}(T),\\
&H_{230}(T)=\frac7{230}T^2-\frac{116}{115}T+\frac{1643}{230}.
\end{aligned}
\]

Its least coefficient denominator is \(230\).

The third arithmetic product is

\[
\begin{aligned}
&\left(\frac13T^2-\frac43T+1\right)
\left(\frac17T^2-\frac87T+1\right)
\left(\frac1{203}T^2-\frac{36}{203}T+1\right)\\
&\quad\cdot
\left(\frac{25}{29}T^2-\frac{726}{29}T+1\right)
\left(\frac1{111}T^2-\frac{40}{111}T+1\right)
\left(\frac{25}{37}T^2-\frac{926}{37}T+1\right)
=S_{22533}(T)^2,\\
&S_{22533}(T)=1+T H_{22533}(T),\\
&H_{22533}(T)=
\frac{25}{22533}T^5-\frac{642}{7511}T^4+\frac{45827}{22533}T^3
-\frac{12020}{777}T^2+\frac{293365}{7511}T-\frac{597974}{22533}.
\end{aligned}
\]

Its least coefficient denominator is \(22533\).

The fourth arithmetic product is

\[
\begin{aligned}
&\left(\frac12T^2-\frac32T+1\right)
\left(\frac16T^2-\frac56T+1\right)
\left(\frac1{120}T^2-\frac{23}{120}T+1\right)
\left(\frac23T^2-\frac73T+1\right)\\
&\quad\cdot
\left(\frac17T^2-\frac87T+1\right)
\left(\frac1{56}T^2-\frac{15}{56}T+1\right)
\left(\frac2{15}T^2-\frac{31}{15}T+1\right)
=S_{5040}(T)^2,\\
&S_{5040}(T)=-1+T H_{5040}(T),\\
&H_{5040}(T)=
\frac1{2520}T^6-\frac{73}{5040}T^5+\frac7{36}T^4-\frac{1549}{1260}T^3
+\frac{4871}{1260}T^2-\frac{4309}{720}T+\frac{1167}{280}.
\end{aligned}
\]

Its least coefficient denominator is \(5040\).

Thus there are five residual templates if the formal endpoint \(H_0\) is counted, and exactly four distinct arithmetic residual templates.

### All 19 basis certificates

The sign column is the constant \(\varepsilon=S(0)\), and it also equals the verified positive numeric root modulo \(N\). Every displayed denominator gcd is one.

| Certificate | \(N\) | Support | Root family | \(\varepsilon\) | Least \(d\) | \(\gcd(d,N)\) | Root mod \(N\) |
|---|---:|---:|---|---:|---:|---:|---:|
| r00c00 | 1,120,697 | 1 | formal \(S_0=T-1\) | -1 | 1 | 1 | \(N-1\) |
| r01c00 | 1,423,811 | 1 | formal \(S_0\) | -1 | 1 | 1 | \(N-1\) |
| r02c00 | 1,867,141 | 1 | formal \(S_0\) | -1 | 1 | 1 | \(N-1\) |
| r03c00 | 282,909,229 | 1 | formal \(S_0\) | -1 | 1 | 1 | \(N-1\) |
| r04c00 | 359,286,023 | 1 | formal \(S_0\) | -1 | 1 | 1 | \(N-1\) |
| r04c01 | 359,286,023 | 3 | \(S_{15}\) | -1 | 15 | 1 | \(N-1\) |
| r04c02 | 359,286,023 | 3 | \(S_{230}\) | -1 | 230 | 1 | \(N-1\) |
| r05c00 | 471,373,153 | 1 | formal \(S_0\) | -1 | 1 | 1 | \(N-1\) |
| r06c00 | 72,159,369,661 | 1 | formal \(S_0\) | -1 | 1 | 1 | \(N-1\) |
| r06c01 | 72,159,369,661 | 6 | \(S_{22533}\) | +1 | 22,533 | 1 | 1 |
| r07c00 | 91,634,270,291 | 1 | formal \(S_0\) | -1 | 1 | 1 | \(N-1\) |
| r08c00 | 120,270,159,983 | 1 | formal \(S_0\) | -1 | 1 | 1 | \(N-1\) |
| r08c01 | 120,270,159,983 | 7 | \(S_{5040}\) | -1 | 5,040 | 1 | \(N-1\) |
| r08c02 | 120,270,159,983 | 3 | \(S_{15}\) | -1 | 15 | 1 | \(N-1\) |
| r09c00 | 18,471,978,008,993 | 1 | formal \(S_0\) | -1 | 1 | 1 | \(N-1\) |
| r09c01 | 18,471,978,008,993 | 3 | \(S_{15}\) | -1 | 15 | 1 | \(N-1\) |
| r10c00 | 23,456,464,765,403 | 1 | formal \(S_0\) | -1 | 1 | 1 | \(N-1\) |
| r10c01 | 23,456,464,765,403 | 3 | \(S_{15}\) | -1 | 15 | 1 | \(N-1\) |
| r11c00 | 30,786,599,256,649 | 1 | formal \(S_0\) | -1 | 1 | 1 | \(N-1\) |

For every row, the replay also multiplied the specialized integers, applied an exact integer square test, and checked that the positive exact root equals \(S(N)\) with the sign chosen in the table. It then matched the root residue recorded in the input artifact.

### Computation status

The successful registered run was `F60-RECON-D02-VERIFY-SAGE-04`. It used SageMath over \(\mathbb Q[T]\), a 120-second internal alarm, and an experiment-local `DOT_SAGE` path. It completed in 1.8 seconds wall time.

- Source SHA-256: `8e07adb983711b72f9b18d99546d6ae1c559b79d68568ee9ce8a9f786f3a0db6`
- Runner SHA-256: `a153f32c5bd43b4dcf82b7c0eaa518610720fdc995646122a4e4844a3e0e12c7`
- Log SHA-256: `23e356f14c59f97b1e380f817ebf34b6fc2227733629216ff8088bea25182ef7`
- Output SHA-256: `089a6efe9c9f5e259f46124d6d9bf353701d6044d769b0db46df2f0f752bff49`

The experiment-local `COMPUTATION_MANIFEST.md` preserves the preregistration and exact status of the failed system-Python/SymPy launch and the three failed Sage assertions that were corrected before the passing run. These failures made no positive certificate claim.

This D02 replay is a finite deterministic certificate only. It supports the 19 stated instances and makes no asymptotic factoring claim.
