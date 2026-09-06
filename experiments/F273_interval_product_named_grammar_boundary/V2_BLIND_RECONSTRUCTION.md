# F273 V2 — strict statement-only blind reconstruction

## Authentication and isolation

The sole substantive input was `V2_STATEMENT.md`.

- Required SHA-256: `95cf55e02dd02322de2c78f95dfa6ddecae7c783fd152f7c00a64de511bf96b4`
- Observed SHA-256: `95cf55e02dd02322de2c78f95dfa6ddecae7c783fd152f7c00a64de511bf96b4`
- Authentication: **MATCH**

No base statement, V2 proof, self-audit, provenance file, manifest, audit,
history, registry, or message was read before this reconstruction was sealed.
No empirical or research computation was used. All checks below are symbolic
derivations from the authenticated statement.

## Verdict

**PASS.** Every theorem, recurrence, terminal value, and exact state count
asserted as part of F273 V2 reconstructs from the stated definitions and
hypotheses. No counterexample or exactness defect was found.

The imported carry results in Section 5 are hashes and boundary declarations,
not results reproved by F273 V2. They were not independently checked because
their source files were outside the permitted input.

## 1. Child-product coordinate ring

Write (F) as a polynomial in (e_0):

\[
F=F_0(o_0,z)+e_0F_1(e_0,o_0,z).
\]

The identity (F(0,o_0,z)=0) says that (F_0) is the zero polynomial.
Therefore (e_0\mid F).

If also (F(e_0,0,z)=0), write (F=e_0K). Specialization at (o_0=0)
gives

\[
e_0K(e_0,0,z)=0.
\]

The polynomial ring over the integral domain (A) is an integral domain, so
(K(e_0,0,z)=0). Applying the first argument with (o_0) in place of (e_0)
gives (o_0\mid K), hence

\[
e_0o_0\mid F.
\]

For (F=G/H), a denominator whose restriction to each generic axis is
defined and nonzero cannot cause an identically zero restriction. Thus a
zero restriction of (G/H) forces the corresponding restriction of (G)
to be the zero polynomial. The same numerator divisibility follows. If the
denominator vanishes on an axis, this inference is unavailable, exactly as
excluded in the statement.

### Corollary 1.1

Let (U) be the union of the leaf supports of the (K) summaries. Then

\[
|U|\leq Kq_0.
\]

An expression that accesses leaves only through these summaries is independent
of every (y_j\notin U). The polynomial \(\prod_{j=0}^{M-1}y_j\) depends
nontrivially on every one of the (M) algebraically independent leaves.
Consequently (U) must contain all leaves, so (M\leq Kq_0). This proves the
formal dependency bound and also shows why specialization to (y_j=x+j) is
outside the argument.

## 2. Smith determinantal divisors

Rank (m-1) over \(\mathbb F_p\) has two consequences:

1. the determinant is zero modulo (p), so (p\mid\Delta_m(M));
2. for each (k<m), some (k\times k) minor is nonzero modulo (p), so
   (p\nmid\Delta_k(M)).

Full rank over \(\mathbb F_q\) implies that, for every (k\leq m), some
(k\times k) minor is nonzero modulo (q). Hence
(q\nmid\Delta_k(M)) for all (k\leq m). Since (N=pq), these facts give

\[
\gcd(\Delta_k(M),N)=1\quad(0\leq k<m),
\qquad
\gcd(\Delta_m(M),N)=p.
\]

Because \(\Delta_{m-1}\mid\Delta_m\), the last Smith invariant is an integer.
The denominator \(\Delta_{m-1}\) contains neither (p) nor (q); the numerator
contains (p) but not (q). Therefore

\[
\gcd(d_m(M),N)=p.
\]

### The balanced diagonal matrix

From (p<q<2p),

\[
p<\sqrt{pq}<q,
\qquad
\sqrt{pq}<\sqrt2,p<2p.
\]

Thus (p\leq B<q) and (B<2p). The interval (1,\ldots,B) contains exactly
one multiple of (p), namely (p), and no multiple of (q). This gives the
claimed ranks of (A_B\bmod p) and (A_B\bmod q).

The only nonzero (B\times B) minor is the determinant, so

\[
\Delta_B(A_B)=B!.
\]

The nonzero \((B-1)\times(B-1)\) minors are exactly (B!/i) for
(1\leq i\leq B). For every prime \(\ell\),

\[
v_\ell\!\left(\gcd_{1\leq i\leq B}\frac{B!}{i}\right)
=v_\ell(B!)-\max_{1\leq i\leq B}v_\ell(i)
=v_\ell\!\left(\frac{B!}{\operatorname{lcm}(1,\ldots,B)}\right).
\]

Therefore

\[
\Delta_{B-1}(A_B)=\frac{B!}{\operatorname{lcm}(1,\ldots,B)},
\qquad
d_B(A_B)=\operatorname{lcm}(1,\ldots,B).
\]

Both (B!) and the lcm contain (p), while neither contains (q>B). Hence
both terminal gcds with (N) equal (p). This also confirms that the last
determinantal divisor and the last Smith invariant are distinct gates; the
statement does not identify them.

## 3. Full derivative resultant

The roots of (P_m) are (-1,\ldots,-m). For a monic polynomial with distinct
roots, the absolute derivative resultant is the squared product of all pairwise
root differences. A distance (d\in\{1,\ldots,m-1\}) occurs for exactly
(m-d) unordered pairs. Thus

\[
D_m=\prod_{d=1}^{m-1}d^{2(m-d)}.
\]

In \(\prod_{k=1}^{m-1}k!\), the factor (d) occurs in the factorials
(d!,\ldots,(m-1)!), exactly (m-d) times. Therefore

\[
D_m=\left(\prod_{k=1}^{m-1}k!\right)^2.
\]

Appending the final factorial immediately gives

\[
\frac{D_{m+1}}{D_m}=(m!)^2.
\]

For the bit length,

\[
\log D_m=2\sum_{d=1}^{m-1}(m-d)\log d.
\]

The upper bound is (O(m^2\log(m+1))). Restricting the sum, for sufficiently
large (m), to (m/4\leq d\leq m/2) gives
\(\Omega(m^2\log m)\). The finitely many small values only change constants.
Hence

\[
\operatorname{bitlen}(D_m)=\Theta(m^2\log(m+1)).
\]

On the balanced promise, (B\geq p). If (B=p), then
(\gcd(B,N)=p), so the preliminary gcd resolves the input. On the unresolved
branch, (B>p), and the factor (p) occurs among the bases
(1,\ldots,B-1) in (D_B). Since (B<q), (q) does not occur. Therefore

\[
\gcd(D_B,N)=p.
\]

## 4. Literal cross-resultant closure

Split each length-(2m) block into two length-(m) blocks. Multiplicativity
of the resultant in each argument produces four pairings. After translating
both blocks in a pairing by the same amount, their offsets are

\[
2c,quad 2c+1,quad 2c-1,quad 2c.
\]

All defining factors are positive for (c\geq1), so no sign correction is
needed. Hence

\[
R_c(2m)=R_{2c-1}(m)R_{2c}(m)^2R_{2c+1}(m).
\]

### Frontier and full-DAG counts

At level zero the offset set is (C_0=\{1\}). If
(C_s=\{1,\ldots,L\}), the next frontier is

\[
\bigcup_{c=1}^{L}\{2c-1,2c,2c+1\}=\{1,\ldots,2L+1\}.
\]

Starting with (L=1), induction gives

\[
C_s=\{1,\ldots,2^{s+1}-1\}.
\]

After (t) expansions, the base frontier therefore has exactly

\[
|C_t|=2^{t+1}-1
\]

distinct offsets. Lengths at distinct levels differ, and the DAG key contains
both length and offset. Its complete number of distinct cross-resultant states
is consequently

\[
\sum_{s=0}^{t}(2^{s+1}-1)
=2(2^{t+1}-1)-(t+1)
=2^{t+2}-t-3.
\]

This confirms that the frontier count is not the full-DAG count.

### Telescoping

For fixed (i), the inner product in (R_c(m)) is a quotient of factorials.
Multiplying over (i=0,\ldots,m-1) gives

\[
R_c(m)
=\frac{\prod_{r=cm}^{(c+1)m-1}r!}
       {\prod_{r=(c-1)m}^{cm-1}r!}.
\]

Since \(\prod_{r=a}^{b}r!=S(b+1)/S(a)\), this becomes

\[
R_c(m)=\frac{S((c+1)m)S((c-1)m)}{S(cm)^2}.
\]

The convention (S(0)=S(1)=1) covers (c=1). From the definition,

\[
S(m+1)/S(m)=m!,
\]

and the already reconstructed superfactorial formula gives

\[
D_m=S(m)^2.
\]

The identity for (R_c(m)) is over the integers. It does not imply that the
displayed denominator is invertible modulo a composite modulus.

On the unresolved balanced branch, (B>p), so (p!\) is one of the factors
in (S(B)=\prod_{r=1}^{B-1}r!\). Thus (p\mid S(B)). Every factorial argument
is less than (B<q), so (q\nmid S(B)). It follows that

\[
\gcd(S(B),N)=p.
\]

### Remote-length resource counts

Let (M=2^tq_0). Then (2^t=M/q_0). A fixed numerical
quasipolynomial is (2^{o(n)}); with (q_0\leq Q(n)) and
(M=2^{\Theta(n)}), this yields

\[
M/q_0=2^{\Theta(n)}.
\]

Substitution of (2^t=M/q_0) into the reconstructed frontier and DAG formulas
gives, for a standalone (R_1(M)), exactly

\[
2M/q_0-1
\]

base offsets and

\[
4M/q_0-t-3
\]

cross-resultant states.

For completeness, multiplicativity of discriminants for a product of two
adjacent monic blocks gives

\[
D_{2m}=D_m^2R_1(m)^2.
\]

If (t\geq1), the top cross term has length (M/2=2^{t-1}q_0). Applying the
standalone formulas with expansion depth (t-1) gives exactly

\[
2^t-1=M/q_0-1
\]

base offsets and

\[
2^{t+1}-t-2=2M/q_0-t-2
\]

cross-resultant DAG states. At every lower length its frontier contains offset
one. Therefore every lower discriminant cross term (R_1(M/2^j)) is already
a state in the top cross-resultant DAG.

There are (t+1) discriminant states, one at each length
(M,M/2,\ldots,q_0). The complete literal discriminant/resultant DAG thus has

\[
(2M/q_0-t-2)+(t+1)=2M/q_0-1
\]

states. For (t=0), there is one discriminant state and no cross-resultant
state, and the same formula gives (2M/q_0-1=1).

Finally, the full state count is \(\Theta(M/q_0)\). One residue modulo an
(n)-bit modulus per state uses \(\Theta((M/q_0)n)\) bits. Any literal
streaming evaluation that visits all distinct keyed states performs at least
\(\Omega(M/q_0)\) state operations. These conclusions remain confined to the
literal recursion stated in F273 V2.

## Boundary check

The proofs above use exactly the named hypotheses: algebraically independent
child coordinates, ordinary integer Smith data, the full derivative
resultant, and literal dyadic cross-resultant expansion or its explicit
superfactorial telescope. They do not imply any of the general lower bounds,
gate equivalences, evaluators, or factoring algorithms listed under the exact
exclusions.
