# Proof of the F232 symbolic candidate

## 1. Quotient and defect identities

In the zero-defect branch, F228 gives `R_u=u` and `Q_u=uH`.  Therefore its
shifted quotient and carry defect are exactly

\[
A_{u,c}=uH+c,\qquad E_{u,c}=cB.
\]

Every divisor of `s_p` is odd and divides `p-1`.  Multiplication of (3) by
the unit `B` gives

\[
BA_{u,c}=u(N-1)+cB.
\]

Modulo `s_p`, use `p=1` and hence `N=pq=q`.  This gives

\[
BA_{u,c}\equiv u(q-1)+cB\pmod {s_p}.
\]

Since `B` is a unit modulo `s_p`, taking gcds proves (4), with full
prime-power valuations.  Interchanging `p` and `q` proves (5).

Now assume `H>C`, let `ell>Y>=max(U,C)`, and assume `ell` does not divide
`H`.  Every declared shifted child is then positive.  The condition
`ell|uH+c` for one declared nonzero shift is equivalent to saying that the
least absolute residue of `uH` is at most `C`.  The residue cannot be zero:
`ell>u` and `ell` divides neither `u` nor `H`.  This proves (5a) in both
directions.  If `H` is instead sampled uniformly from
`F_ell^*`, multiplication by each fixed `u` is a permutation.  At most
`2C` nonzero residues have least absolute value at most `C`, and a union
bound over `ceil(U/2)` odd multipliers proves (5b).  No independence between
the multiplier events is asserted, and this model bound is not applied to
the actual factor-conditioned value of `H`.

For `c=0`, the integer `A_{u,0}=uH` has no prime support outside the union
of the supports of `u` and `H`.  For `c!=0`, equation (6) shows that every
odd defect prime divides `c`.  If `U,C<=Y`, both sources are already present
in the smooth and `H`-supported baseline.  No corresponding reduction
exists for the support of `uH+c` when `c!=0`; equations (4)--(5) show its
factor-correlated orientation exactly.

As a hostile specialization, let `q=p+g`.  If a prime power divides `s_p`,
then (4) reduces its quotient-child incidence to divisibility of

\[
ug+cB.
\]

For a prime power dividing `s_q`, equation (5) instead reduces incidence to
divisibility of

\[
-ug+cB.
\]

Thus, at fixed radix and gap, the bounded menu samples a fixed finite pool
of near-radix integers.  This is a sharp hostile structure, but no theorem
used here asserts an infinite prime family in the zero-defect branch with a
fixed gap.

## 2. Exact support saturation

Every prime-power valuation in an integer below `N` is less than `n`.
Consequently, if a prime `ell` occurs in any input to the lcm (7), its
valuation in `W_Q` is at least its complete valuation in `s_p` and `s_q`.
The surviving residuals are therefore exactly

\[
r_p=\prod_{\substack{\ell^e\parallel s_p\\
\ell>Y,\ \ell\nmid H,\
\ell\nmid A_{u,c}\ \text{for all }(u,c)}}\ell^e,
\tag{12}
\]

and the symmetric formula for `r_q`.  Terms from unshifted children and
defects are redundant under `U,C<=Y`; they remain in (7) to make the source
definition complete.

Let `K` be the number of quotient children.  The elementary bound

\[
\log_2 W_Q
\le \log_2U_Y+n\log_2H
+n\sum_{u,c}\log_2A_{u,c}
+n\sum_{u,c:E_{u,c}\ne0}\log_2|E_{u,c}|
\]

is numerical-QP when `K,Y,U,C` are numerical-QP.  The number of listed
prime occurrences is at most the same total logarithmic height.  Thus the
factored word, its binary exponent, modular powering, and every puncture
have numerical-QP bit cost, conditional on the declared recursive
factorizations.  Raising exposed radicals to `n` is an explicit word
operation; it is not a hidden factoring or order oracle.

## 3. Return and stale laws

The odd local unit subgroups have orders `P` and `Q`.  Raising a uniform
unit to `2^n` kills its two-primary coordinates and leaves independent
uniform points in those odd cyclic subgroups.

The zero-defect identities give

\[
\gcd(H,P)=\gcd(H,Q)=D.
\]

Primewise valuation then gives

\[
\gcd(W_QH,P)=D\gcd(W_Q,s_p)={P\over r_p},
\]

and symmetrically at `q`.  A cyclic group of order `P` has
`gcd(W_QH,P)` roots of `z^(W_QH)=1`.  Division by the group order proves
(10).

Exactly one local return makes the initial gcd proper.  On a global return,
complete prime-power stripping factors when the two exact local orders
differ.  If they agree, it recovers their common exact order.  A global
return is stale exactly when both local orders equal one divisor `d|M`.
A cyclic group has `phi(d)` elements of exact order `d`, so independence
gives stale probability

\[
{1\over PQ}\sum_{d\mid M}\varphi(d)^2.
\]

The probability of at least one local return is

\[
{1\over r_p}+{1\over r_q}-{1\over r_pr_q}.
\]

Subtracting the stale atom proves (11).  This completes the symbolic
audit.  It proves the exact target measured by D01, not a lower bound for
that target on all inputs.
