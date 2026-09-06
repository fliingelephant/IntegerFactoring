# Proof of the F224 AP bridge and obstruction

## 1. AP-Fermat terminal

Since `p` is a unit modulo `L`, so is its public residue `s`.  Hence
`s^(-1) mod L` is computable.  From `N=pq` and `p congruent s (mod L)`,

\[
q\equiv Ns^{-1}=:u\pmod L.
\tag{1}
\]

The true integer `A_*=(p+q)/2` satisfies

\[
2A_*\equiv s+u\pmod L.
\tag{2}
\]

Let `g=gcd(2,L)`.  Consistency of (2) is guaranteed by `A_*`.  Dividing
by `g` leaves a linear congruence with invertible coefficient modulo
`m=L/g`, so it gives exactly one computable class modulo `m`.

Let `A_0` be the least integer in this class with `A_0>=sqrt(N)`.  Enumerate

\[
A_0,A_0+m,A_0+2m,\ldots
\tag{3}
\]

and square-test `A^2-N`.  The true `A_*` occurs in (3).  At that point

\[
A_*^2-N=\left({q-p\over2}\right)^2,
\tag{4}
\]

so `A_*-(q-p)/2=p` and `A_*+(q-p)/2=q`.  Exact multiplication verifies
the output.

Put `Delta=A_*-sqrt(N)`.  The number of tested terms through `A_*` is at
most `1+Delta/m`.  The exact gap is

\[
\begin{aligned}
\Delta
&={p+q\over2}-\sqrt{pq}\\
&={ (\sqrt q-\sqrt p)^2\over2}\\
&={d^2\over2(\sqrt q+\sqrt p)^2}\\
&={d^2\over2(p+q+2\sqrt N)}
 <{d^2\over8p}.
\end{aligned}
\tag{5}
\]

Because `g<=2`, `m=L/g>=L/2`.  Combining this with (5) gives

\[
1+{\Delta\over m}<1+{d^2\over4pL}.
\tag{6}
\]

Each square test and factor verification uses polynomial bit complexity on
`O(n)`-bit operands.  This proves Theorem A.

## 2. Injection of the balanced integer cell

The balance assumption gives

\[
\sqrt{N/2}<p<\sqrt N<q.
\tag{7}
\]

The diameter of `I_N` is smaller than `p`.  Indeed,

\[
\sqrt N-\sqrt{N/2}
< (\sqrt2-1)p<p,
\tag{8}
\]

and the endpoint rounding does not reach `p` for odd `p>=3`.  It is also
smaller than `q` by (7).  Therefore reduction of `I_N` modulo either hidden
prime is injective.

The only nonunit in `I_N` is `p`: the interval lies below `q`, and its
upper endpoint is below `2p`.  Thus the initial integer gcd isolates the
one exact-candidate point and every other shift is a unit modulo `N`.

## 3. Pulling the P193 root counts back to the AP

P193 proves the following local counts for unit shifts under
`r<d<p-1`:

- at most `rd` shifts modulo `p` make some raw cyclic coefficient zero;
- at most `rd(r+1)` shifts modulo `q` make some raw cyclic coefficient
  zero;
- at most `rd` shifts modulo `p` have positive local nullity; and
- at most `2rd` shifts modulo `q` have positive local nullity.

These are not distributional estimates.  They are cardinality bounds for
the roots of explicit nonzero local polynomials.  By the injections in
Section 2, pulling any one of those root sets back to `I_N`, and then
restricting it to `C_(L,s)`, cannot increase its cardinality.  A union bound
therefore leaves at most

\[
rd+rd(r+1)+rd+2rd=rd(r+5)
\tag{9}
\]

off-target cell integers that activate a raw-coefficient or
resultant/local-nullity channel.

If the largest atom of a sampling law is `eta`, any set of `B` shifts has
mass at most `B eta`.  Adding the exact point `p` to (9) gives

\[
\Pr(\text{factor in one trial})
\le (1+rd(r+5))\eta.
\tag{10}
\]

Uniform sampling has `eta=1/H`.  If a stage fixes its modulus and law from
the previous transcript and only then draws a fresh shift, (10) applies
conditioned on that transcript.  Summing the conditional bounds proves the
adaptive-bank statement.

## 4. Combining the two scales

Fix `epsilon>0` and assume

\[
d\le p^{2/3-\epsilon}.
\tag{11}
\]

Uniform balance makes the interval length `Theta(p)`.  On the branch
relevant below, `L=o(p)`, so every residue class occurring in it has

\[
H=\Theta(p/L).
\tag{12}
\]

Let the AP-Fermat cap be a numerical-QP integer `Q_F(n)>=2`.  If the scan
does not reach `A_*` within that cap, (6) implies

\[
L<O\!\left({d^2\over pQ_F(n)}\right).
\tag{13}
\]

Let there be `T(n)` modified-AKS trials and let every `r_i` be bounded by
`R(n)`, with `T,R` numerical QP.  Failure of a cap `Q_F>=2` also gives
`d^2>4pL(Q_F-1)`, hence `d>sqrt(p)`.  Therefore, for all sufficiently
large inputs, every `r_i<d<p-1` and `gcd(r_i,N)=1`; these are exactly the
P193 hypotheses used in Theorem B.  Equations (10)--(13) give total success

\[
\begin{aligned}
O\!\left(
T(n)R(n)^2{dL\over p}
\right)
&=O\!\left(
{T(n)R(n)^2\over Q_F(n)}{d^3\over p^2}
\right)\\
&\le2^{o(n)}p^{-3\epsilon}\\
&=2^{-\Omega(n)}.
\end{aligned}
\tag{14}
\]

The exact-candidate contribution is smaller and is already included in
(10).  If (13) does not hold, the positive terminal reaches the factors.
This proves Theorem C.

P193 supplies an infinite family with `d=Theta(p^(3/5))`.  Taking
`epsilon=1/15` in (14) gives `d^3/p^2=Theta(p^(-1/5))`, which is the
stated concrete corollary.

## 5. The exact `N=187` certificate

For `N=11*17`, the balanced interval is `{10,11,12,13}`.  The odd residue
cell modulo two is `{11,13}`.  At `x=13`, reduce the shift to `2 mod 11`
and `13 mod 17`.

Modulo `11`, Frobenius reduces the error to `h_(17,2)`, without changing
parity positions.  Direct powering gives

\[
h_{17,2}(1)=1,
\qquad
h_{17,2}(-1)=6.
\]

Since two is invertible, the even and odd cyclic coefficients are

\[
((1+6)/2,(1-6)/2)=(9,3)\pmod {11}.
\]

Modulo `17`, the corresponding polynomial is `h_(11,13)`, and

\[
h_{11,13}(1)=5,
\qquad
h_{11,13}(-1)=3.
\]

Its cyclic coefficients are `(4,1) mod 17`.  All four displayed
coefficient residues and all four root evaluations are nonzero.  Therefore
no raw coefficient has a proper gcd and the resultant, whose local value is
the product of the two root evaluations up to a unit, is nonzero in both
hidden fields.  The only useful cell point is the separately screened exact
integer `x=11`.
