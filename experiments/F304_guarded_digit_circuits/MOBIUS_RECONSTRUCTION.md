# Blind reconstruction of the canonical Möbius moment bank

## Result

The claim is reconstructible. The algorithm below is uniform, deterministic,
uses only explicitly guarded arithmetic, and does not enumerate the `L`
arguments or image values. I found no unresolved mathematical step.

Throughout, write

\[
 D_x=B+Cx,\qquad T_x=\frac{n-Ax}{D_x},\qquad
 u_x=\frac{q_x}{D_x}.
\]

The definition of `q_x` uses the full integer `n`. It gives the exact identity
in \(\mathbb Z_2\)

\[
 y_x=T_x+Lu_x. \tag{1}
\]

No reduced representative of `n` is substituted into this identity.

## 1. The canonical residues form a permutation

Every \(D_x\) is odd. Thus, \(T_x\) is defined in \(\mathbb Z_2\), and
\(D_xy_x\equiv n-Ax\pmod L\). This proves that `q_x` is an integer and that
\(u_x\in\mathbb Z_2\).

If \(T_{x_1}\equiv T_{x_2}\pmod L\), cross multiplication gives

\[
 (AB+Cn)(x_2-x_1)\equiv0\pmod L.
\]

The coefficient \(K=AB+Cn\) is odd. Hence \(x_1\equiv x_2\pmod L\).
The inputs both lie in \([0,L)\), so they are equal. Therefore, the canonical
values \(y_x=T_x\bmod L\) are a permutation of

\[
 Y=\{0,1,\ldots,L-1\}. \tag{2}
\]

Only the oddness of `K` is used. Its factors are not used.

## 2. Power sums without argument enumeration

Let

\[
 \Pi_m(L)=\sum_{x=0}^{L-1}x^m.
\]

Compute these integers from

\[
 \Pi_m(L)=\sum_{k=0}^{m}
 \left\{\begin{matrix}m\\k\end{matrix}\right\}k!
 \binom{L}{k+1}, \tag{3}
\]

where a binomial coefficient is zero when \(k+1>L\). This includes
\(\Pi_0(L)=L\). Stirling numbers and binomial coefficients follow their
ordinary integer recurrences. All divisions in those recurrences are exact
integer divisions. Formula (3) has a number of terms controlled by the
requested degrees, not by a loop over the arguments `x`.

For \(r\geq1\) and any bit precision \(P\), put
\(z_B=CB^{-1}\pmod {2^P}\). Since `B` is odd and `C` is even,
\(v_2(z_B)\geq1\). The negative-binomial series therefore gives

\[
\begin{aligned}
 p_r&:=\sum_{x=0}^{L-1}T_x^r\\
 &\equiv B^{-r}\sum_{a=0}^{r}\binom ra n^{r-a}(-A)^a
 \sum_{h=0}^{P-1}(-1)^h
 \binom{r+h-1}{h}z_B^h\Pi_{a+h}(L)
 \pmod {2^P}. \tag{4}
\end{aligned}
\]

Every omitted term has a factor \(z_B^h\) with \(h\geq P\), so it is zero
modulo \(2^P\). This is a uniform truncation. The only modular inverse in
(4) is that of the odd integer `B`.

## 3. Recovering all required carry moments

The mixed canonical moments will require carry moments of degree higher than
the output bound. Define

\[
 J=\begin{cases}
 0,&d=0,\\
 2d+s-2,&d\geq1,
 \end{cases}
 \qquad H=J+1,\qquad E=\min(H,L). \tag{5}
\]

It is enough to construct \(Q_0,\ldots,Q_J\). Let \(e_k^T\) be the `k`-th
elementary symmetric function of the `L` values \(T_x\), and let \(e_k^Y\)
be the same function of the fixed set `Y`. Set \(e_0^T=e_0^Y=1\), and set
both functions to zero for \(k>L\).

Compute \(e_k^Y\), for \(k\leq E\), exactly from the exact power sums (3)
and Newton's recurrence. For \(e_k^T\), even divisions need guards. Let

\[
 P_*=2s+v_2(E!). \tag{6}
\]

Compute \(p_1,\ldots,p_E\) modulo \(2^{P_*}\) with (4). In

\[
 k e_k^T=\sum_{r=1}^{k}(-1)^{r-1}e_{k-r}^T p_r, \tag{7}
\]

the following precision schedule is sufficient. At step `k`, calculate the
right side modulo

\[
 2^{P_*-v_2((k-1)!)}.
\]

It is exactly divisible in \(\mathbb Z_2\) by \(2^{v_2(k)}\). Divide by that
power of two, using the displayed guard bits, and multiply by the inverse of
the odd part of `k`. The result determines

\[
 e_k^T\pmod {2^{P_*-v_2(k!)}}. \tag{8}
\]

Induction proves this precision statement: every previously computed
\(e_{k-r}^T\) is known to at least the numerator precision in (7), and the
division loses exactly \(v_2(k)\) bits. Since \(k\leq E\), (8) always leaves
at least `2s` bits. Thus every required \(e_k^T\) is known modulo \(L^2\).
No even residue is inverted.

Now expand an elementary symmetric function using (1). For
\(0\leq m<L\),

\[
 e_{m+1}^T\equiv e_{m+1}^Y
 -L\sum_x u_x e_m(Y\setminus\{y_x\})\pmod {L^2}. \tag{9}
\]

Consequently, define

\[
 H_m=\frac{e_{m+1}^Y-e_{m+1}^T}{L}\pmod L
 \quad(0\leq m<L), \tag{10}
\]

and define \(H_m=0\) for \(m\geq L\). The division in (10) is an exact
division of a difference known modulo \(L^2\). The quotient is therefore
well defined modulo `L`; it is not a modular inverse of `L`. For
\(m\geq L\), both the relevant elementary symmetric function and
\(e_m(Y\setminus\{y\})\) vanish, which justifies the zero definition.

For every \(m\geq0\), with \(e_k^Y=0\) when \(k>L\),

\[
 e_m(Y\setminus\{y\})
 =\sum_{r=0}^{m}(-1)^r e_{m-r}^Y y^r. \tag{11}
\]

Put \(U_r=\sum_xu_xy_x^r\pmod L\). Equations (9)--(11) give the triangular
system

\[
 H_m=\sum_{r=0}^{m}(-1)^r e_{m-r}^Y U_r\pmod L. \tag{12}
\]

Its diagonal coefficient is \((-1)^m\), a unit. Hence compute successively

\[
 U_m=(-1)^m\left(
 H_m-\sum_{r=0}^{m-1}(-1)^r e_{m-r}^Y U_r
 \right)\pmod L. \tag{13}
\]

Since \(T_x\equiv y_x\pmod L\),

\[
 Q_r=\sum_xu_xT_x^r\equiv U_r\pmod L. \tag{14}
\]

This obtains all carry moments through degree `J`. When `J` exceeds `L-1`,
(13) continues as the characteristic-polynomial recurrence of the fixed set
`Y`; no additional roots or arguments are enumerated.

## 4. Constructing the canonical mixed moments

First compute the rational mixed moments

\[
 R_{ij}=\sum_{x=0}^{L-1}x^iT_x^j\pmod {L^2}.
\]

For \(j=0\), use \(R_{i0}=\Pi_i(L)\). For \(j\geq1\), the same expansion as
(4), now at precision `2s`, gives

\[
\begin{aligned}
 R_{ij}\equiv B^{-j}\sum_{a=0}^{j}\binom ja n^{j-a}(-A)^a
 \sum_{h=0}^{2s-1}(-1)^h\binom{j+h-1}{h}
 (CB^{-1})^h\Pi_{i+a+h}(L)
 \pmod {L^2}. \tag{15}
\end{aligned}
\]

Again, the omitted terms vanish because `C` is even.

For the canonical correction, solve the Möbius equation for `x`:

\[
 x=\frac{n-BT_x}{A+CT_x}. \tag{16}
\]

The denominator is odd in \(\mathbb Z_2\). For \(i\geq1\) and \(k\geq0\),
define the polynomial modulo `L`

\[
\begin{aligned}
 G_{ik}(t)={}&A^{-i}t^k
 \left(\sum_{a=0}^{i}\binom ia n^{i-a}(-B)^a t^a\right)\\
 &\mathrel{}\cdot
 \left(\sum_{h=0}^{s-1}(-1)^h\binom{i+h-1}{h}
 (CA^{-1})^h t^h\right)\pmod L. \tag{17}
\end{aligned}
\]

For \(i=0\), set \(G_{0k}(t)=t^k\). The tail in (17) has a factor
\((CA^{-1})^h\), so it vanishes modulo `L` for \(h\geq s\). Thus (16)
proves

\[
 G_{ik}(T_x)\equiv x^iT_x^k\pmod L. \tag{18}
\]

If \(G_{ik}(t)=\sum_rg_{ik,r}t^r\), set

\[
 W_{ik}=\sum_r g_{ik,r}Q_r\pmod L. \tag{19}
\]

Then \(W_{ik}=\sum_xx^iu_xT_x^k\pmod L\). The largest needed degree in
(17), for \(i,j\leq d\) and \(k=j-1\), is

\[
 (j-1)+i+(s-1)\leq2d+s-2=J,
\]

which explains the internal carry bound (5).

Finally, (1) gives, without division,

\[
 y_x^j\equiv T_x^j+jLu_xT_x^{j-1}\pmod {L^2}
 \quad(j\geq1). \tag{20}
\]

Therefore output

\[
 S_{i0}=R_{i0},\qquad
 S_{ij}=R_{ij}+jL W_{i,j-1}\pmod {L^2}\quad(j\geq1), \tag{21}
\]

and output the first \(d+1\) values from (14).

## 5. Boundary conventions and guards

- The case \(d=0\) is nonempty. Formula (5) sets `J=0`. The algorithm
  computes \(Q_0=(e_1^Y-e_1^T)/L\pmod L\) and
  \(S_{00}=\Pi_0(L)=L\pmod {L^2}\).
- The convention \(0^0=1\) is implemented by \(\Pi_0(L)=L\),
  \(T_x^0=1\), and the separate `j=0` branch in (15) and (21).
- `A` and `B` may be negative odd integers, and `n` may be any signed
  integer. Their residues are reduced only after the exact algebraic
  identities have been established. Odd residues still have unique inverses
  modulo every required power of two.
- The full `n` occurs in (1), (4), (15), and (17). In particular, `q_x` is
  never formed from `n mod L`.
- The only modular inverses are those of `A`, `B`, odd parts of Newton
  indices, and odd denominators implicit in \(\mathbb Z_2\). The divisions
  by powers of two in (7) and (10) use exact divisibility and the stated
  guard precision. No residue is normalized by dividing by an unguarded
  even index.
- The use of the exact set `Y` in (2), (9), and (10) preserves the canonical
  graph coordinates. Formula (21) is modulo \(L^2\), not only modulo `L`,
  and it does not replace `y_x` by `T_x`.

## 6. Bit cost and non-enumeration

The values `J`, `H`, `E`, and \(P_*\) are explicit functions of `s` and the
numerical bound `d`. Since \(v_2(E!)<E\), all modular precisions are
\(O(s+d)\) bits. Every power-sum index used in (4), (15), or (17) is also
\(O(s+d)\).

Formula (3) computes all needed integer power sums by degree recurrences.
Their bit lengths, and the bit lengths of the exact \(e_k^Y\), are
polynomial in `s+d`. All other quantities can be reduced at once modulo the
displayed power of two. The nested sums, Newton recurrences, triangular
solve, and the \((d+1)^2\) mixed outputs use a polynomial number of
arithmetic operations on polynomial-bit integers. Reducing the signed input
integers and taking their bounded-degree powers is polynomial in their
binary lengths as well.

No step loops over \(x=0,\ldots,L-1\), materializes the permutation, asks for
factors of `K`, or uses a supplied magnitude or precision bound. A loop can
have length comparable with `L` only when the numerical degree `d` is itself
at least comparable with `L`; it is still a degree recurrence and does not
enumerate graph coordinates. Thus the cost is polynomial in `s`, numerical
`d`, and the input bit lengths, as claimed. It is not asserted to be
polynomial in the binary length of `d`.

## Independent checks

I also checked the symmetric-function signs, the characteristic recurrence
past degree `L-1`, the guarded Newton schedule, and the mixed correction on
small exact rational instances with positive and negative odd `A` and `B`.
These checks support the derivation but are not used as proof and are not
part of the constructor.
