# Proof of the F236 centered-carry theorem

## 1. Balanced size and nearest quotients

Since `q<2p`, one has `N=pq<2p^2`, hence `p>sqrt(N/2)`.  If `n=2m`, then
`N>=2^{2m-1}=B^2/2`, so `p>B/2`.  If `n=2m+1`, then `N>=2^{2m}=B^2`, so
again `p>B/sqrt(2)>B/2`.

Dyadic half-ties can occur.  The declared floor formulas break every tie
upward and give unique residues in `[-B/2,B/2)`.  Since `p>B/2`, both
quotients are positive.  Also `p<sqrt N` and `q<2sqrt N`.  If `n` is even,
then `sqrt N<B`; if `n` is odd, then `sqrt N<sqrt(2)B`.  Hence always
`p,q<3B`, and the round-half-up quotients satisfy

\[
1\le K_p,K_q\le3u.
\]

## 2. Carry integrality

Expand the centered product:

\[
u^2N=(K_pB+x)(K_qB+y).
\]

Zero defect gives `N=1+BH`.  Reducing both sides modulo `B` yields

\[
xy\equiv u^2N\equiv u^2\pmod B.
\]

Therefore `c=(xy-u^2)/B` is an integer.

## 3. Weighted trace identity

Divide the full expansion by `B` and substitute `xy=u^2+cB`:

\[
u^2H=K_pK_qB+K_py+K_qx+c.                             \tag{P1}
\]

On the other hand,

\[
\begin{aligned}
u(K_pq+K_qp)
 &=K_p(K_qB+y)+K_q(K_pB+x)\\
 &=2K_pK_qB+K_py+K_qx.
\end{aligned}
\]

Using (P1) gives

\[
u(K_pq+K_qp)=u^2H+K_pK_qB-c,
\]

which proves (2), including its divisibility assertion.

## 4. Quadratic recovery

Since `q=N/p`, the identity `T=K_pq+K_qp` gives

\[
K_qp^2-Tp+K_pN=0.
\]

Its discriminant is

\[
\begin{aligned}
T^2-4K_pK_qN
 &=(K_pq+K_qp)^2-4K_pK_qpq\\
 &=(K_pq-K_qp)^2.
\end{aligned}
\]

The quadratic formula therefore recovers the two oriented candidates.  An
exact divisor check rejects every false result.

## 5. Bank cost

For each `u`, there are `O(u^2)` positive quotient pairs and `2C+1`
candidate carries.  Summing through `U` gives

\[
O\!\left(C\sum_{u\le U}u^2\right)=O(CU^3).
\]

Every numerator has `O(n+log U+log C)` bits.  Integer division, square
testing, multiplication, and exact verification are polynomial in that
length.  Numerical-QP value caps therefore give numerical-QP total cost.

## 6. Generic Dirichlet scale

Use the standard simultaneous Dirichlet lemma in dimension two on
`p/B,q/B`.  For a cap `U`, after harmless constant rounding of the usual
parameter, some `1<=u<=U` has centered errors

\[
|x|,|y|=O(B/\sqrt U).
\]

Then

\[
|c|\le {|xy|+u^2\over B}
=O(B/U+U^2/B).
\]

This proves only the generic bound stated.  It supplies no numerical-QP
carry for polynomial `U`.

## 7. Separation from computation

No numerical output is used in Sections 1--6.  The finite claims in the
statement are direct summaries of separately preregistered exhaustive
scans.  They are evidence and named finite counterexamples only.
