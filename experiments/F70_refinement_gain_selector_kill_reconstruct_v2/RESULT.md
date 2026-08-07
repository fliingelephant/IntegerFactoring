# Verification result: PASS

Every asserted claim in the narrow result follows from the statement. The proof is below.

## 1. Refinement accounting

For each old block (q), let (d_q\geq 1) be its number of nontrivial final descendants. Distinct old blocks are coprime, so their descendant sets are disjoint. Every final block is either a descendant of exactly one old block or divides no old block. Hence

\[
r'=\sum_{q\in Q}d_q+\nu
   =r+\sum_{q\in Q}(d_q-1)+\nu
   =r+\sigma+\nu.
\]

This proves (A1).

For an endpoint (x), let (m_x) be the number of distinct final blocks that divide it. The blocks are nontrivial and pairwise coprime, so

\[
2^{m_x}\leq \prod_{q\mid x}q\leq x.
\]

Every final block occurs in some endpoint. Therefore

\[
R\leq\sum_xm_x
 \leq\sum_x\left\lceil\log_2(x+1)\right\rceil=L.
\]

Applying (A1) at each refinement and telescoping gives

\[
\sum_t(\sigma_t+\nu_t)=R-r_0\leq L-r_0.
\]

This is only a post-hoc bound for a fixed finite transcript. In an adaptive run, new endpoints make (L) grow, there is no stated polynomial bound on that growth in terms of the original input, and steps with \(\sigma_t+\nu_t=0\) are not counted. Thus (A2) does not give a polynomial stopping bound.

## 2. The separator-free old subgroup

The arithmetic is

\[
37\cdot109=4033,
\qquad
\Phi_{36}(2)=2^{12}-2^6+1=4096-64+1=4033.
\]

Modulo (37),

\[
2^6=27,qquad 2^{12}=27^2=26,qquad
2^{18}=26\cdot27=-1.
\]

Modulo (109),

\[
2^6=64,qquad 2^{12}=4096=63,qquad
2^{18}=63\cdot64=-1.
\]

In either field, (2^{36}=1) but (2^{18}\ne1), so the order divides (36) and does not divide (18). The only divisors of (36) with that property are (4,12,36). Since (2^{12}\ne1) in both fields, the order is (36) modulo both primes.

Consequently, for every integer (j), (2^j=1) in either component exactly when (j=0\pmod {36}), and (2^j=-1) exactly when (j=18\pmod {36}). The two CRT components therefore acquire either sign simultaneously. An element of (H_0=\langle2\rangle) cannot equal (1), or equal (-1), in exactly one component. Thus every \(\gcd(h\pm1,4033)\) is trivial or global, never a proper factor.

## 3. Infinite immediate-square family

Put

\[
a=2s-1,qquad b=\frac{2s+1}{3}.
\]

The assumption (s=1\pmod3) makes (b) integral. Both (a) and (b) are odd and greater than one. If (d\mid a,b), then (d\mid(2s-1)) and (d\mid(2s+1)), hence (d\mid2); as (d) is odd, (d=1). Therefore

\[
N_s=ab=\frac{4s^2-1}{3}
\]

is a product of coprime proper odd factors. Also

\[
N_s+1=\frac{4s^2+2}{3}
       =2\frac{2s^2+1}{3}.
\]

The second factor here is odd, so the block (2) occurs to exponent one in each indexed copy. The two square-class rows are the same nonzero parity vector. Their kernel is therefore exactly \(\{(0,0),(1,1)\}\). The sole nonzero dependency is the duplicate dependency, whose product is \((N_s+1)^2\). Its root is (N_s+1=1\pmod {N_s}), with the same sign in every CRT component, so it is global.

The two occurrences of (2) authorize (g=4). Since

\[
N_s-s^2=\frac{s^2-1}{3}>0
\]

and

\[
4s^2=1+3N_s,
\]

the canonical inverse is (w=s^2), and the product is the exact square \((2s)^2\). Moreover,

\[
\gcd(2s-1,N_s)=a,
\qquad
\gcd(2s+1,N_s)=b.
\]

For the second equality, (2s+1=3b), \(\gcd(a,b)=1\), and (a=1\pmod3). Both gcds are proper, so (2s) is a non-global square root and splits (N_s).

Now suppose (s=55\pmod {1530}). Then

\[
s=1\pmod9,qquad s=0\pmod5,qquad s=4\pmod {17}.
\]

These imply (N_s=1\pmod3), (5\nmid N_s), and (17\nmid N_s). The first two immediate gcds are consequently

\[
\gcd(g-1,N_s)=\gcd(3,N_s)=1,
\qquad
\gcd(g+1,N_s)=\gcd(5,N_s)=1.
\]

If (d\mid N_s) and (d\mid(g-w)=4-s^2), then

\[
d\mid 3N_s-4(s^2-4)=15.
\]

As (N_s) is coprime to (15), the third gcd is one. For

\[
D=(g-w)^2+4=s^4-8s^2+20,
\]

any (d\mid D,N_s) satisfies (4s^2=1\pmod d), and hence

\[
16D=(4s^2)^2-32(4s^2)+320=289\pmod d.
\]

Thus (d\mid17^2); since (17\nmid N_s), the fourth gcd is also one. All four gcd screens fail, while (gw=(2s)^2) makes the exact-square screen succeed with the non-global root proved above.

At (s=55),

\[
N_s=\frac{4\cdot55^2-1}{3}=4033,qquad
g=4,qquad w=55^2=3025.
\]

Here (N+1=2\cdot2017). The new (g) only reuses the complete old block (2), and

\[
3025=2017+1008,qquad 2017=2\cdot1008+1,
\]

so (w) is coprime to (2017). No old block splits, and therefore \(\sigma=0\). The endpoint (w) nevertheless contributes private block data (one private gcd-free type in this refinement), so the total gain is not zero. The successful square feedback therefore needs no positive old-block splitting.

## 4. Strict expansion at (4033)

The three relations check directly:

\[
2\cdot2017=4034=1+N,
\]

\[
64\cdot3970=254080=1+63N,
\qquad
8\cdot3529=28232=1+7N.
\]

Their endpoints decompose as

\[
64=2^6,qquad3970=2\cdot1985,qquad8=2^3.
\]

All odd pairs in \(\{2017,1985,3529\}\) are coprime, as witnessed by

\[
\begin{aligned}
2017&=1985+32, &1985&=62\cdot32+1,\\
3529&=2017+1512, &2017&=1512+505,\\
1512&=2\cdot505+502, &505&=502+3, &502&=167\cdot3+1,\\
3529&=1985+1544, &1985&=1544+441,\\
1544&=3\cdot441+221, &441&=221+220, &221&=220+1.
\end{aligned}
\]

Thus complete gcd refinement gives

\[
Q_0=\{2,2017,1985,3529\}.
\]

Modulo (N), the relations give

\[
2017=2^{-1}=2^{35},qquad
1985=2^{-7}=2^{29},qquad
3529=2^{-3}=2^{33},
\]

where exponents are reduced using the order (36). Since (2\in Q_0), this proves

\[
H(Q_0)=\langle2\rangle=H_0.
\]

The occurrences of (2) have total exponent

\[
1+6+1+3=11,
\]

from (2,64,3970,8), respectively. Hence (g=2^{11}=2048<4033) is legal. Direct multiplication gives

\[
2048\cdot3905=7{,}997{,}440
                 =1+1983\cdot4033.
\]

Since (0<3905<4033), this proves that (w=3905) is the canonical inverse.

For the gcd screens, the CRT residues are

\[
(g\bmod37,g\bmod109)=(13,86),
\qquad
(w\bmod37,w\bmod109)=(20,90).
\]

Thus the residues of (g-1,g+1,g-w) are, respectively,

\[
(12,85),qquad(14,87),qquad(-7,-4),
\]

and those of \((g-w)^2+4\) are \((16,20)\). None is zero in either component, so all four gcds equal one. Finally,

\[
2827^2=7{,}991{,}929
<gw=7{,}997{,}440
<7{,}997{,}584=2828^2,
\]

so the exact-square screen also fails.

The new endpoint (g=2^{11}) reuses block (2) whole. For (w), the overlap gcds with (2,2017,1985,3529) are

\[
1,quad1,quad5,quad1,
\]

respectively. In particular,

\[
1985=5\cdot397,qquad3905=5\cdot781,
\]

and \(\gcd(397,781)=1\). Hence

\[
Q_1=\{2,2017,5,397,3529,781\}.
\]

Exactly one old block, (1985), has two descendants, so \(\sigma=1\). Exactly one final block, (781), divides no old block, so \(\nu=1\). This also checks (A1) numerically: (6=4+1+1).

Block (781) occurs to exponent one in (w=5\cdot781), and it occurs in no old relation. Its parity column is therefore zero on every old row and one on the appended row. No square-class dependency can include the appended row, so the new column does not close.

Both feedback residues are in (H_0): (g=2^{11}), and (w=g^{-1}=2^{-11}). Also (1985\in H_0) and (w\in H_0). Therefore

\[
397=1985\cdot5^{-1}\in\langle H_0,5\rangle,
\qquad
781=w\cdot5^{-1}\in\langle H_0,5\rangle.
\]

Together with (2,5\in Q_1), this proves

\[
H(Q_1)=\langle H_0,5\rangle.
\]

The claimed residue certificate is

\[
2^{23}=2^{12}2^{11}=26\cdot13=5\pmod {37},
\]

but

\[
2^{23}=63\cdot86=77\ne5\pmod {109}.
\]

If (5\) belonged to (H_0), its exponent would have to be (23\pmod {36}) in the first component, which would force residue (77) in the second. Thus (5\notin H_0), and the containment is strict.

Since (2) has order (36),

\[
5\cdot2^{-23}=5\cdot2^{13}=630\pmod {4033}.
\]

Indeed (5\cdot2^{13}=40960=10\cdot4033+630). Writing (x=630),

\[
x-1=629=17\cdot37,qquad4033=109\cdot37,
\]

so

\[
\gcd(x-1,4033)=37.
\]

After the appended relation, the exact occurrence bounds are

\[
E_2=22,quad E_{2017}=1,quad E_5=2,quad
E_{397}=E_{3529}=E_{781}=1.
\]

Thus the positive whole-block box is

\[
\left\{
2^a2017^b5^c397^d3529^e781^f<4033:
\begin{array}{l}
0\le a\le22,\ 0\le b\le1,\ 0\le c\le2,\\
0\le d,e,f\le1
\end{array}
\right\}.
\]

If a product in this box equalled (630=2\cdot3^2\cdot5\cdot7), the exponents of (2017,397,3529,781) would all be zero, since none of those blocks divides (630). The remaining product (2^a5^c) cannot equal (630). Hence the box does not contain the canonical representative (630).

Although the occurrences permit (5\cdot2^{13}), its positive integer value is (40960>N), so it is excluded from the box. Obtaining (630) subtracts (10N); that is multiplication followed by modular reduction in the generated subgroup, not whole-block occurrence selection below (N).

## 5. Classification and scope

The construction proves the stated narrow existential result. The old subgroup (H_0) is separator-free. Both feedback endpoint residues (g,w) lie in (H_0). Integer endpoint gcd refinement nevertheless exposes (5\notin H_0), strictly enlarges the subgroup, and the enlarged subgroup contains (630), for which \(\gcd(630-1,4033)=37\).

Nothing in the proof supplies a uniform sampler, a polynomial stopping bound, an all-input success theorem, a stand-alone ranking law for \(\sigma\), or a factoring algorithm. Those claims are outside the proved scope.
