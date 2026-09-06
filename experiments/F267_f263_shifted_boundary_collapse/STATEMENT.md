# F267 statement — F263 shifted-boundary collapse

## Status and scope

This is a proof-only explanation of the six non-direct shifted candidates
in the authenticated F263-D02 V2 held-out result. It proves exact formulas
for those candidates and identifies four public query-boundary mechanisms.

Every mechanism collapses before it can become a new factoring source:

1. its hypothesis writes a hidden factor as a public offset from
   `floor(sqrt(N))`; and
2. in the small-offset range `s^2 < p`, the modulus factors in the first
   Fermat trial.

The packet does not claim that these are all possible zeros of the six
polynomials. It explains every observed F263-D02 non-direct incidence and
proves that the same boundary mechanisms give no nonconsecutive advantage.
It makes no new computational claim.

## 1. Semiprime and shifted-block setup

Let

\[
 N=pq,\qquad p<q<2p,
\]

where `p` and `q` are distinct odd primes. Put

\[
 B=\lfloor\sqrt N\rfloor,\qquad H=\lfloor B/2\rfloor,
 \qquad s=B-p.
\]

Then

\[
 0\le s<H<p<q,\qquad B<q.
\tag{1}
\]

The case `s=0` is the public cleanup `gcd(B,N)=p`. On the unresolved
branch, `s>=1` and `B` is a unit modulo both hidden primes.

Let `L>=2` be even, and let the half-open shifted block

\[
 I=[a,a+L)\subseteq\{1,\ldots,H-1\}
\]

exclude the singular denominator index `s`. Define

\[
 R_L(X)=\prod_{j=0}^{L-1}(X+j).
\tag{2}
\]

The shifted F263 factors on this block are

\[
 u_c=c,\qquad v_c=c-B.
\]

## 2. Exact formulas for the six candidates

The first three product-jet coordinates are

\[
 \begin{aligned}
 u_0&=R_L(a),&u_1&=R_L'(a),&u_2&={R_L''(a)\over2},\\
 v_0&=R_L(a-B),&v_1&=R_L'(a-B),&v_2&={R_L''(a-B)\over2}.
 \end{aligned}
\tag{3}
\]

Consequently

\[
 \boxed{\operatorname{jet\_det02}
 ={R_L(a)R_L''(a-B)-R_L''(a)R_L(a-B)\over2}.}
\tag{4}
\]

For a weight sequence `w_c`, write `F_w` and `G_w` for the upper-right
entries of the forward and reverse products of

\[
 \begin{pmatrix}c&w_c\\0&c-B\end{pmatrix}
\]

over the block. For F263 weights `w_c=1` and `w_c=c+1`, write these as
`F_0,G_0,F_1,G_1`. Then

\[
 \boxed{B F_0=B G_0=R_L(a)-R_L(a-B).}
\tag{5}
\]

F263's `transfer_f0` and `transfer_r0` are `F_0` and `G_0`. Its forward
`transfer_det01` is

\[
 D_{01}=R_L(a)(F_1-F_0),
\]

and satisfies the division-free identity

\[
 \boxed{(B+1)D_{01}
 =R_L(a)\big((a+L)R_L(a)-aR_L(a-B)\big).}
\tag{6}
\]

Equations (3)--(6) are identities over the integers. They do not assume
that any recurrence factor is invertible.

## 3. Four exact boundary mechanisms

F263 always includes the left-edge block

\[
 E_L=[1,L+1)
\]

and the right-edge block

\[
 J_L=[H-L,H)
\]

for every registered query length `L` that fits its bank.

For an even `L`, the following implications hold.

| Candidate | Block | Exact boundary hypothesis | Forced hidden-prime zero |
|---|---|---|---|
| `shifted.jet_det02` | `E_L` | `s=L+1` | zero modulo `p` |
| `shifted.transfer_f0` | `E_L` | `s=L+1` | zero modulo `p` |
| `shifted.transfer_r0` | `E_L` | `s=L+1` | zero modulo `p` |
| `shifted.transfer_det01` | `E_L` | `s=L+2` | zero modulo `p` |
| `shifted.u1` | `J_L` | `s=L+1` or `s=L+2` | zero modulo `p` |
| `shifted.v1` | `J_L` | `s=L-1` or `s=L`, and `q=p+2(s+1)` | zero modulo `q` |

For `J_L` to be a non-direct F263 witness, also require

\[
 s<H-L.
\tag{7}
\]

This says that the right-edge support lies strictly to the right of the
singular index. The left-edge supports exclude `s` automatically in their
two listed cases.

The extra equation in the `v1` row is automatic under the mathematical
small-offset condition

\[
 \boxed{s^2<p.}
\tag{8}
\]

## 4. Near-square rigidity and one Fermat trial

Under (8), the floor-square inequalities force

\[
 \boxed{q-p=2(s+1),\qquad B+1={p+q\over2}.}
\tag{9}
\]

Because `N` is not a square, Fermat factorization starts at
`ceil(sqrt(N))=B+1`. Equation (9) gives

\[
 (B+1)^2-N=(s+1)^2,
\]

so its first trial returns

\[
 p=B-s,\qquad q=B+s+2.
\tag{10}
\]

Even without (8), every boundary row in the table already has the public
descriptor `p=B-s`, where `s` is one of `L-1,L,L+1,L+2`. Directly testing
these polynomially many public offsets is simpler than evaluating the
corresponding product jet or transfer.

## 5. Exact coverage of the authenticated F263 pattern

The authenticated F263-D02 V2 held-out result reports these complete
non-direct `s` sets:

| Candidate | Reported `s` values | Boundary explanation |
|---|---|---|
| `shifted.u1` | `9,10,17,18` | `L+1,L+2` for `L=8,16` |
| `shifted.v1` | `7,8,15,16,31,32,63,64` | `L-1,L` for `L=8,16,32,64` |
| `shifted.jet_det02` | `9,17` | `L+1` for `L=8,16` |
| `shifted.transfer_f0` | `9,17` | `L+1` for `L=8,16` |
| `shifted.transfer_r0` | `9,17` | `L+1` for `L=8,16` |
| `shifted.transfer_det01` | `10,18` | `L+2` for `L=8,16` |

Thus the identities explain every one of the 136 reported candidate-row
incidences, whose union has 67 rows. This is a statement about the frozen
query bank and authenticated output. It is not an exhaustiveness theorem
for zeros on other blocks or other moduli.

All 256 held-out consecutive-prime rows satisfy `s<=95` and
`p>=551426102609`, hence `s^2<p`. Therefore (9)--(10) prove that every one
of them, including the eight public-cleanup rows, is a one-Fermat-trial
modulus. The six non-direct families reveal only this public boundary.

## 6. Evidence boundary

This packet proves exact integer identities and conditional implications.
It uses the authenticated F263 output only to match the finite reported
sets and bounds. It does not prove that no other polynomial grammar can
evaluate the central-binomial block, that the six candidates have no other
zeros, or that a general factoring algorithm is impossible.
