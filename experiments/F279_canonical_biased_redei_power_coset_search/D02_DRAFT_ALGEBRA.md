# F279-D02 draft algebra — canonical biased Rédei power-coset sources

## Status, ancestry, and exact scope

F279-D02 is an unfrozen theory successor. It does not authorize source-code
creation, compilation, fixture creation, a benchmark, an experiment, remote
access, or a ledger change.

The immutable D01 inputs were:

```text
DRAFT_ALGEBRA.md
SHA-256 328c8c26d5c06e3033300539fd5900f7ddcb55f253b75fae851c58db47eea424

DRAFT_PREREGISTRATION.md
SHA-256 4498a4f3e2404297d6eda58036fc45e097915a13d73077dc9511dea4e6cb7e7e
```

D02 preserves the sound two-mode algebra. It changes the evidence language
and the operational realization of uniform controls. In particular, D02 does
not call a finite decoy screen exhaustive.

The endpoint is

\[
N=pq,\qquad p<q<2p,\qquad B=\lfloor\sqrt N\rfloor=p+s,
\tag{1}
\]

where `p` and `q` are distinct odd primes. Put

\[
h=q-B.
\tag{2}
\]

If `s=0`, then `gcd(B,N)=p`. The remaining branch has `s>0`, `h>0`,
and `B` is a unit modulo both factors.

## 1. General homogeneous two-mode normal form

Let

\[
C\in M_2(\mathbb Z/N\mathbb Z)
\]

be public. Let `L` be a public scalar linear functional. Define

\[
t=\operatorname{tr}C,\qquad
\delta=\det C,\qquad
\eta=t^2-4\delta,
\tag{3}
\]

and

\[
A=L(C),\qquad e=L(I),\qquad
H=A^2-Aet+e^2\delta.
\tag{4}
\]

The coefficient invariant is

\[
H=\det(AI-eC).
\tag{5}
\]

A clean local two-mode interpretation requires `2`, `delta`, `eta`, and
`H` to be units. For the affine chart it also requires `e` to be a unit.
A proper gcd of any required unit with `N` is already a factor. A value
that vanishes modulo both factors is a degenerate branch. The global
`e=0` branch is treated separately in Section 2.

Work in

\[
E_N=(\mathbb Z/N\mathbb Z)[w]/(w^2-\eta).
\tag{6}
\]

When `2 delta eta` is a unit, the characteristic roots are

\[
\alpha={t+w\over2},\qquad \beta={t-w\over2}.
\tag{7}
\]

For every integer `k>=0`, define `P_k,Q_k` by

\[
(t+w)^k=P_k+Q_kw.
\tag{8}
\]

They can be evaluated without division. Their recurrence is

\[
\begin{pmatrix}P_{k+1}\\Q_{k+1}\end{pmatrix}
=
\begin{pmatrix}t&\eta\\1&t\end{pmatrix}
\begin{pmatrix}P_k\\Q_k\end{pmatrix},
\qquad (P_0,Q_0)=(1,0).
\tag{9}
\]

Binary pair powering evaluates `(P_B,Q_B)` in `O(log B)` modular
multiplications.

Define the homogeneous target

\[
V=et-2A,\qquad W=e.
\tag{10}
\]

Then

\[
V^2-\eta W^2=4H.
\tag{11}
\]

Thus the target avoids both local eigenlines exactly when `H` is a unit.

### Theorem 1 — exact scalar endpoint

On the clean branch,

\[
\boxed{L(C^B)=2^{-B}(WP_B-VQ_B).}
\tag{12}
\]

The two-root interpolation identity is

\[
L(C^B)=
{(A-e\beta)\alpha^B-(A-e\alpha)\beta^B\over\alpha-\beta}.
\tag{13}
\]

Substitution of (7), (8), and (10) makes its numerator

\[
2^{-B}w(WP_B-VQ_B).
\tag{14}
\]

Since `alpha-beta=w`, equation (12) follows. The executable expression in
(12) does not divide by a zero divisor.

## 2. The homogeneous `e=0` branch

If `e=0`, then `W=0`, `V=-2A`, and (12) becomes

\[
L(C^B)=A\,2^{1-B}Q_B.
\tag{15}
\]

If `A` is a unit, cancellation is exactly `Q_B=0`. If `A` has a proper
gcd with `N`, that gcd is already a factor. If `A=0 mod N`, the observable
is degenerate on the two-dimensional Cayley-Hamilton span. Therefore the
clean `e=0` branch is the ordinary powered-collision target. No ranked D02
candidate uses it.

## 3. Rédei power-coset form

Fix a local factor `r` in `{p,q}`. Define

\[
z_r={t+w\over t-w}
\tag{16}
\]

and, for a clean homogeneous target `[V:W]`,

\[
\lambda_r={V+Ww\over V-Ww}.
\tag{17}
\]

The denominator norms are `t^2-eta=4 delta` and
`V^2-eta W^2=4H`, so both denominators are units. Equation (8) gives

\[
z_r^B={P_B+Q_Bw\over P_B-Q_Bw}.
\tag{18}
\]

Cross multiplication gives

\[
\boxed{WP_B-VQ_B=0\pmod r\iff z_r^B=\lambda_r.}
\tag{19}
\]

Conjugation sends `w` to `-w` and sends both `z_r` and `lambda_r` to
their inverses. Thus

\[
y_r=z_r^B\lambda_r^{-1}
\tag{20}
\]

is a norm-one-torus word, and local cancellation is `y_r=1`.

## 4. Exact local residual exponents

Let

\[
\chi_r=\left({\eta\over r}\right)\in\{1,-1\}.
\tag{21}
\]

The local norm-one torus is cyclic of order

\[
m_r=r-\chi_r.
\tag{22}
\]

The Frobenius law is

\[
z_r^r=z_r^{\chi_r}.
\tag{23}
\]

At the smaller factor, `B=p+s`, so

\[
\boxed{z_p^B=\lambda_p
\iff z_p^{s+\chi_p}=\lambda_p.}
\tag{24}
\]

At the larger factor, `B=q-h`, so

\[
\boxed{z_q^B=\lambda_q
\iff z_q^{\chi_q-h}=\lambda_q.}
\tag{25}
\]

For a negative exponent `-k`, the division-free pair is `(P_k,-Q_k)`.
For exponent zero it is `(1,0)`. These conventions make both residual
checks executable without local division.

## 5. Complete affine diagonal chart

Assume `e` is a unit. Scale the target to `[v:1]`, where

\[
v=V/W=t-2A/e.
\tag{26}
\]

Every clean triple `(t,eta,v)` is realized by

\[
C(t,\eta,v)=
\begin{pmatrix}
(t-v)/2&1\\
(\eta-v^2)/4&(t+v)/2
\end{pmatrix}.
\tag{27}
\]

It satisfies

\[
\operatorname{tr}C=t,\qquad
\det C={t^2-\eta\over4},\qquad
\operatorname{Disc}(\chi_C)=\eta.
\tag{28}
\]

For `L(X)=X_11`, one has `A=(t-v)/2`, `e=1`, and

\[
\boxed{(C(t,\eta,v)^B)_{11}=2^{-B}(P_B-vQ_B).}
\tag{29}
\]

The coefficient invariant is

\[
H={v^2-\eta\over4}.
\tag{30}
\]

Conversely, for

\[
C=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]

the upper-left coordinate has

\[
t=a+d,\qquad v=d-a,\qquad
\eta=(a-d)^2+4bc,\qquad H=-bc.
\tag{31}
\]

On the clean branch, `b` and `c` are units. Diagonal conjugation by
`diag(b,1)` changes the upper-right entry to `1`, the lower-left entry to
`bc=(eta-v^2)/4`, and preserves every upper-left matrix-power coordinate.
Thus (27) is a converse realization, not only an example.

## 6. Division-free orbit and phase relations

For fixed `eta`, define

\[
(R,S)\star(R',S')
=(RR'+\eta SS',\ RS'+SR').
\tag{32}
\]

The pair `(R,S)` represents

\[
\Phi(R,S)={R+Sw\over R-Sw}.
\tag{33}
\]

For clean represented elements,

\[
\Phi(R,S)=\Phi(R',S')
\iff RS'-SR'=0.
\tag{34}
\]

The source power `z^k` is represented by `(P_k(t,eta),Q_k(t,eta))`.
The affine target `lambda(v)` is represented by `(v,1)`.

For positive `e`,

\[
\lambda=z^e\iff P_e(t,\eta)-vQ_e(t,\eta)=0.
\tag{35}
\]

For negative `e`,

\[
\lambda=z^e\iff
P_{|e|}(t,\eta)+vQ_{|e|}(t,\eta)=0.
\tag{36}
\]

For target torsion,

\[
\lambda(v)^m=1\iff Q_m(v,\eta)=0.
\tag{37}
\]

More generally,

\[
\lambda=z^e\mu,\quad \mu^m=1
\iff \lambda^m=z^{em}.
\tag{38}
\]

Let `(R,S)=(P_m(v,eta),Q_m(v,eta))`. Let `(P,Q)` represent
`z^(em)`, using `(P_k,Q_k)` for a nonnegative exponent and `(P_k,-Q_k)`
for exponent `-k`. Then the exact public equality screen is

\[
Z_{e,m}=RQ-SP.
\tag{39}
\]

If the relation in (38) holds and the endpoint hits, then

\[
z^{B-e}=\mu,\qquad z^{m(B-e)}=1.
\tag{40}
\]

A proper gcd of an equality determinant is a direct factor. A global
equality can explain an endpoint as a registered order or finite-phase
decoy.

## 7. Honest finite decoy boundary

D02 registers one finite relation box:

```text
K = 16
M_source = {2,...,16}
E_orbit  = {-16,...,-1,1,...,16}
M_target = {2,...,16}
E_phase  = {-16,...,0,...,16}
M_phase  = {2,...,16}
```

The operational screen checks every member of these sets. It does not
check an orbit offset outside `E_orbit`, target torsion outside `M_target`,
or a mixed relation outside `E_phase x M_phase`.

The evidence label after all registered checks is
`box_unexplained_exclusive`. It means only:

1. the endpoint gcd is proper;
2. every registered public cleanup and invariant passed;
3. no proper or global relation in the registered box explains the hit;
4. the powered-collision and half-order screens did not explain it; and
5. exact replay passed.

It does not mean `free coset`, `relation-free`, `all phases removed`, or
`all Miller explanations removed`. A later relation outside the box can
reclassify the finite observation without contradicting D02.

The registered near-square cleanup is also finite. It consists only of
`gcd(B+j,N)` for `-64<=j<=64` and the 65 Fermat centers
`B+1,...,B+65`. D02 makes no exhaustive near-square claim beyond this
window.

## 8. Exact projective-uniform law

Fix a clean local source `(t,eta)`. The Cayley map

\[
[V:W]\longmapsto {V+Ww\over V-Ww}
\tag{41}
\]

is a bijection from clean projective target lines to the local norm-one
torus.

- If `eta` is nonsquare, all `r+1` projective lines are clean.
- If `eta` is square, the two eigenlines are removed and the remaining
  `r-1` lines are clean.

Therefore an independent uniform clean target line has exact local hit law

\[
\Pr(z_r^B=\lambda_r)={1\over r-\chi_r}.
\tag{42}
\]

For independent CRT-local target lines, the exact proper-gcd probability is

\[
{1\over m_p}+{1\over m_q}-{2\over m_pm_q}.
\tag{43}
\]

This is a theorem about a declared uniform sample space. It is not a theorem
about a compressed pseudorandom generator.

## 9. ExactTape256 operational realization

For each potential control and each registered attempt, D02 assigns one
distinct 256-bit tape block. The complete tape is sampled uniformly from
the Cartesian product of all block spaces. Equivalently, every block is an
independent uniform member of `{0,...,2^256-1}`. Once the tape bytes are
fixed, counter lookup and all later computation are deterministic.

For one modulus `N`, put

\[
M=N^2,\qquad L=\left\lfloor{2^{256}\over M}\right\rfloor M.
\tag{44}
\]

Interpret the assigned block as a big-endian integer `R`. Reject the attempt
if `R>=L`. Otherwise put

\[
U=R\bmod M,\qquad V=\lfloor U/N\rfloor,\qquad W=U\bmod N.
\tag{45}
\]

Then `(V,W)` is exactly uniform on `[0,N)^2`. Accept it only if

\[
\gcd(V,W,N)=1,
\qquad
\gcd(V^2-\eta W^2,N)=1.
\tag{46}
\]

Each clean local projective line has exactly `r-1` nonzero vector
representatives. The accepted vectors therefore induce independent uniform
clean projective lines modulo `p` and `q`. Disjoint tape-block sets make
different accepted controls independent. Conditioning on all registered
controls succeeding preserves this product law because each success event
depends only on that control's block set.

D02 uses exactly three assigned attempts per potential control. Failure of
all three is a declared `control_shortfall` and aborts the phase. No new
block is consumed, no counter shifts, and no substitute generator is used.

The probability statements above are with respect to the uniform tape state
space. A realized tape is one authenticated draw. D02 does not claim that
physical entropy can be proved from its bytes.

## 10. Fixed canonical biased grammar

Let

\[
\mathcal C=\{-4,-3,-2,-1,0,1,2,3,4\}.
\tag{47}
\]

For each `c`, define

\[
x_c=B+c,\qquad
d_c=\lfloor N/x_c\rfloor,\qquad
r_c=N-x_cd_c.
\tag{48}
\]

After `gcd(x_c,N)=1`, define the least positive inverse and exact inverse
quotient by

\[
1\le u_c<N,\qquad x_cu_c=1+k_cN.
\tag{49}
\]

Every nonzero integer atom `x_c,d_c,r_c,u_c,k_c` is gcd-screened before
use. A proper gcd is a public cleanup factor. A saturated atom aborts the
row.

The expression bank at anchor `c` is

\[
\mathcal E_c=
\{[+x_c]_N,[-x_c]_N,[+d_c]_N,[-d_c]_N,
[+r_c]_N,[-r_c]_N,[+u_c]_N,[-u_c]_N,
[+k_c]_N,[-k_c]_N\}.
\tag{50}
\]

Choose ordered `t,eta` from one source bank `E_c`. Choose `v` from `E_c'`
with `|c'-c|<=1`. This gives

\[
10^2(2\cdot20+7\cdot30)=25{,}000
\tag{51}
\]

named candidates and `9*10^2=900` named sources. Equal numerical values do
not merge syntax identities or scores. Arithmetic may be cached and fanned
back to every immutable syntax identity.

The grammar contains no factor label, local character, source power, or
endpoint value.

## 11. Elementary high-order diagnostic

Put

\[
D_0=n=\lceil\log_2(N+1)\rceil,
\qquad A_0=D_0^2+D_0.
\tag{52}
\]

For `2<=a<=A_0`, first screen `gcd(a,N)`. For a unit base, screen
`gcd(a^e-1,N)` for every integer `1<=e<=D_0`.

- A proper gcd is a direct diagnostic factor.
- A saturated gcd rejects the base.
- If all gcds are one, retain the first base `z`.
- If no base is retained, record `diagnostic_shortfall`.

For a retained base, neither local order divides an integer at most `D_0`.
Hence both local orders are greater than `D_0`. The split chart

\[
\eta=1,\qquad t={z+1\over z-1}\pmod N
\tag{53}
\]

satisfies

\[
{t+1\over t-1}=z.
\tag{54}
\]

This diagnostic is not ranked and gives no target-correlation claim.

## 12. Exact nonclaims

D02 can report only a finite `box_unexplained_exclusive` observation or a
finite null for its fixed grammar and fixed screens. It proves no:

1. inverse-quasipolynomial hit law;
2. all-input dispatcher or factoring algorithm;
3. sparsity theorem for deterministic biased targets;
4. exhaustive orbit, torsion, phase, Miller, or near-square classification;
5. relation between a realized exact tape and physical entropy; or
6. lower bound for other recurrences, matrices, higher modes, or semilinear
   actions.

No experiment may run from this algebra draft. Its exact D02 preregistration
must receive a separate fresh no-context theory audit with it.
