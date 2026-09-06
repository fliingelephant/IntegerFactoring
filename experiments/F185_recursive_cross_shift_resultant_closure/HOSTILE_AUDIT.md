# F185 hostile proof audit

## Protocol and frozen inputs

The frozen hashes match the manifest exactly:

```text
STATEMENT.md   f4fca86df79a72d473cc3e8dd943140978d1422efb6b2f2af324bd94076a555b
PROOF.md       98c4ad7dc7fafb7466bf1a6e2384c20ec86f4d6f29c4c8394749bcc9c5583491
SELF_AUDIT.md  c49347914d99db86cbd60a5727b63411876dc7b30d946dfae54e348ff248ec54
```

All three frozen files were read in full. The external interface inspection
was limited to the promoted P161 section and the F182 statement. The F182
statement hash is

```text
e17ae1948b92ee09f83423919b3bd9ef641077e1014421b04036189e93611502
```

and matches its registered hash. No mathematical computation or checker was
run. No frozen file or durable ledger was edited.

## Verdict

**PASS, with scope qualifications rather than a mathematical repair.** The
fixed-contraction double-extinction closure is correct as a conditional
strong-induction transition. The proof covers the index-zero resultant
cases, arbitrary order multiplicity, arbitrary hidden prime powers, all
cross-menu extinction patterns, and exact factor-first order stripping.
The recurrence counts all QP-many siblings at every contracted level and
still has numerical-QP total cost.

This is not a standalone recursive factoring algorithm. Its recursive cost
theorem assumes an enclosing complete procedure whose every recursive call
has the stated fixed contraction and branching bounds. F185 does not resolve
its returned wide-shift-hard descendant and therefore does not instantiate
that premise. The inverse-carry lemma is also only a correctness observation:
its carry can be almost as large as the parent, so it supplies no fixed-
contraction QP recursion.

## 1. Resultant nonvanishing, including every index-zero case

For cross-menu shifts put (D=\epsilon-\delta). The menu endpoints give

\[
3\le D\le 2L+1.
\]

The three cases involving an index-zero polynomial are exact:

\[
\left|\operatorname{Res}(X+\delta,X+\epsilon)\right|=D,
\]

\[
\left|\operatorname{Res}(X+\delta,(X+\epsilon)^l-1)\right|
=D^l-1,
\]

and

\[
\left|\operatorname{Res}((X+\delta)^k-1,X+\epsilon)\right|
=|(-D)^k-1|.
\]

The last expression is (D^k-1) for even (k) and (D^k+1) for odd
(k). All three expressions are positive because (D\ge3). In particular,
the proof does not incorrectly interpret index zero as the constant
polynomial (1-1); (F_{\delta,0}=X+\delta) is monic of degree one.

For (k,l\ge1), the roots of the two polynomials lie on unit circles with
centers (-\delta) and (-\epsilon). A common complex root would force the
center distance to be at most two, contrary to (D\ge3). Thus no integer
resultant is zero. Inseparability or repeated roots after reduction modulo a
prime do not affect this integer nonvanishing argument.

## 2. Uniform resultant size and exact contraction

Let

\[
\lambda=\left\lceil\log_2(2L+2)\right\rceil,
\qquad E=K(1+K\lambda).
\]

Since (D+1\le2L+2\le2^\lambda), the index-zero values satisfy

\[
D<2^E,
\qquad
D^l-1<2^{l\lambda}\le2^E,
\]

and

\[
|(-D)^k-1|<2^{1+k\lambda}\le2^E.
\]

The final inequality also holds in the edge case (K=k=1), where
(E=1+\lambda).

For (k,l\ge1), evaluating the second polynomial on the (k)-th roots of
unity gives

\[
R_{\delta,\epsilon;k,l}
=\prod_{u^k=1}|(D+u)^l-1|
<\bigl(2(D+1)^l\bigr)^k
\le2^{k(1+l\lambda)}
\le2^E.
\]

Thus every positive integer resultant has bit length at most (E). Under
(E\le\lfloor\rho n\rfloor), this is at most (n-1). From
(n=\lceil\log_2(N+1)\rceil), one has (N\ge2^{n-1}), while such a
resultant is at most (2^{n-1}-1). Every recursive input is therefore
strictly below (N), with the claimed fixed bit contraction. A resultant
equal to one is harmless and is skipped.

Solving (\lambda K^2+K\le m) gives the displayed positive root and its
floor. The admissible range is nonempty exactly when (m\ge1+\lambda).
Because a fixed numerical-QP (L) has
(\lambda=(\log n)^{O(1)}=o(n)), the eventual nonemptiness and the stated
largest-(K) asymptotic are correct.

## 3. Exact primary filtering and multiplicity annihilation

Fix (R_j=p_j^{e_j}) and (\ell^a\parallel g_j). For any exponent (Q),

\[
\operatorname{ord}_{R_j}(w^Q)=\frac{g_j}{\gcd(g_j,Q)}.
\]

For one shift, (\ell\mid C_\delta) exactly when either
(\ell\mid N+\delta), or (N+\delta) is a unit modulo (\ell) and its
multiplicative order is at most (K). The linear factor handles the first
case without assigning an order to a nonunit. The factors for all
(1\le k\le K) handle the second case in both directions.

The order satisfies (g_j<R_j\le N<2^n). Hence
(\ell^a\le g_j) implies (a<n). If (\ell) occurs even once in
(P_\mathcal S), its valuation in (P_\mathcal S^n) is at least (n>a),
so the complete (\ell^a)-part is deleted. If it does not occur, the
complete primary part is retained. Formula (12) is therefore exact even
for nonsquarefree local orders.

All factors used to construct (P_\mathcal S) are positive. In particular,
(N+\delta>1) and ((N+\delta)^k-1>0), so no accidental zero exponent is
present.

## 4. Arbitrary hidden prime powers

Every filtered order divides (g_j), and P161 supplies
(\gcd(g_j,N)=1). Thus the order of the generated cyclic subgroup modulo
(p_j^{e_j}) is coprime to (p_j). The kernel of reduction

\[
(\mathbb Z/p_j^{e_j}\mathbb Z)^\times
\longrightarrow(\mathbb Z/p_j\mathbb Z)^\times
\]

is a (p_j)-group, so its intersection with that cyclic subgroup is
trivial. Identity modulo (p_j) is therefore equivalent to identity modulo
the full (p_j^{e_j}).

Consequently every identity gcd selects either all or none of each hidden
prime power. It cannot return a partial power. This validates the trichotomy
(1), a proper divisor, or (N) for arbitrary repeated factors. For a
prime-power input there is only one hidden component, so the gcd branches
are (1) or (N); the double-extinction branch still constructs a common
multiple of the one local order, and stripping recovers that exact order.

Extra primes in the resultants, including primes dividing (N), do not
break stripping. They are absent from every (g_j), so all their copies are
deleted by global-identity tests. They may also expose a factor of (N)
earlier, which only strengthens the output.

## 5. Double-extinction covering is complete

Assume both filters give global identity. Since both act on the same
original (w), for each (\ell^a\parallel g_j),

\[
g_j\mid P_\mathcal A^n
\quad\text{and}\quad
g_j\mid P_\mathcal B^n.
\]

Thus (\ell) divides some filter factor in each menu. This supplies
(\delta\in\mathcal A), (\epsilon\in\mathcal B), and
(0\le k,l\le K) such that

\[
F_{\delta,k}(N)=F_{\epsilon,l}(N)=0\pmod\ell.
\]

All four easy/easy combinations are covered:

1. two nonunits use the linear-linear resultant (D);
2. a nonunit followed by a short unit action uses (D^l-1);
3. a short unit action followed by a nonunit uses
   (|(-D)^k-1|);
4. two short unit actions use the nonlinear resultant.

Each polynomial is monic and remains nonzero modulo (\ell). Their shared
root (N\bmod\ell) makes the corresponding integer resultant divisible by
(\ell). A relevant resultant cannot equal one. Therefore every rational
prime supporting any (g_j) divides (U) at least once. Raising (U) to
the (n)-th power supplies every exponent (a<n), so (g_j\mid U^n) for
all components. No squarefreeness assumption is used.

Using the original (w) in both filters is essential and is done correctly.
If the second filter acted on the first descendant, global extinction would
not imply both vanishings for every original order prime.

## 6. Factor-first stripping gives an exact common order

Maintain the invariant (g_j\mid M) for every component. For a prime
(r\mid M), the gcd

\[
D_r=\gcd(w^{M/r}-1,N)
\]

selects exactly the hidden components whose local orders divide (M/r).
If (D_r=N), every local order still divides (M/r), so deleting one copy
of (r) preserves the invariant. A proper gcd is a valid factor.

If (D_r=1), no local order divides (M/r). Since all divide (M), every
one must use the full current (r)-adic valuation:

\[
v_r(g_j)=v_r(M)\qquad\text{for every }j.
\]

Repeating this for every prime in the dynamically reduced, fully factored
(M) proves (g_j=M) for all (j). A prime deleted completely is absent
from every (g_j) by the preserved invariant. Thus no prime support is
missed by discussing only primes in the final (M). P161 gives
(g_j>1) and (P^-(g_j)>T), hence the returned exact common order is
fully factored and exceeds (T).

## 7. Local work and the full QP recursion tree

One node has exactly (L^2(K+1)^2) resultant slots and no more recursive
calls than this. The filters, exact resultants, the product (U^n), and all
stripping exponents have numerical-QP encoded length. The total number of
prime-copy deletion attempts is at most the bit length of (U^n), so the
claimed local bound (A(n)) is valid.

For an enclosing complete procedure satisfying the stated hypotheses,

\[
\mathcal T(t)\le A(t)+B(t)\mathcal T(\lfloor\rho t\rfloor).
\]

The contraction gives (O(\log t)) depth. If a nondecreasing envelope
satisfies

\[
W(t)\le2^{C(\log(t+1))^d},
\]

then multiplying the QP branching over all levels gives at most

\[
W(t)^{O(\log t)}
=2^{O((\log(t+1))^{d+1})}.
\]

This counts every sibling, not only one branch. For Las Vegas calls,
linearity of expectation gives the same recurrence. The tree has
deterministically finite depth and finite branching, so almost-sure
termination of every call implies almost-sure termination of the whole
finite tree.

This complexity statement remains conditional. F185 returns an unresolved
wide-shift-hard descendant and therefore is not itself the complete
procedure used on the recursive resultants. Likewise, replacing the fixed
bit contraction by the bare inequality (R<N) would permit linear depth in
the bit length and would not prove a QP tree bound.

## 8. Canonical inverse-carry boundary

If (1\le x,y<N) and (xy=1+cN), then (c\ge0). For (c=0), positivity
forces (x=y=1). For (c>0),

\[
c=\frac{xy-1}{N}<\frac{xy}{N}<x
\]

because (y<N), and symmetrically (c<y). Hence

\[
0<c<\min(x,y)<N.
\]

Any common divisor of (c) and (x) divides both (cN) and (xy), hence
their difference (1). The same holds for (y), proving
(\gcd(c,xy)=1).

The claim must not be enlarged. The example (x=y=N-1) has carry
(c=N-2), so the carry need not have a fixed-factor bit contraction.
Also, a carry prime can divide (N) even though it divides neither endpoint;
for example (N=9), (x=4), (y=7) gives (c=3). Factoring the carry and
comparing its primes with (N) can therefore factor some inputs. F185
claims only endpoint coprimality and does not exclude this possibility, so
the stated narrow lemma is correct.

## 9. External-interface and scope audit

The P161 interface supplies exactly what F185 uses: a public unit whose
local orders are nontrivial, coprime to (N), and have least prime divisor
above the fixed numerical-QP cap. F185 does not assume that P161 localizes
unequal rough orders.

The F182 interface uses the same two original-state menus and the same
linear handling of nonunits. F182 rules out double extinction by placing
all cross-resultant primes below its roughness cap. F185 instead permits
double extinction, recursively factors the fixed-contraction resultants,
and constructs a common annihilator. It does not import F182's stronger
roughness-versus-resultant inequality or its polylogarithmic action cap.

The exact remaining branch is therefore stated honestly: one rough
descendant can retain long unit action for every shift in one complete
menu. Neither the resultant closure nor the recursion accounting resolves
that branch. No all-input factoring theorem follows from F185 alone.
