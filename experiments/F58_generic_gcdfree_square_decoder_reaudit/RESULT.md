# F58 fresh hostile whole-artifact re-audit

## Artifact and verdict

**Candidate:**
`experiments/F58_generic_gcdfree_square_decoder_kill/RESULT.md`

**Pinned SHA-256:**
`a103f1d42350e67ccda23792fc72b2d84beee2436c920678e3cfb83e5c03520c`

**Verdict: PASS.**

The corrected artifact is mathematically sound and promotion-ready for the
next required step, a strict proof-blind reconstruction. The multiset
refinement computes a gcd-free basis in deterministic polynomial bit
complexity without factoring its blocks. One square/nonsquare flag per
pairwise-coprime block gives an exact square-subset kernel. The new unit
congruence-pair version of Theorem 3 has valid overlap identities, a defined
normalized-root homomorphism, complete arbitrary-basis testing, and correct
factor extraction for every odd, possibly nonsquarefree, modulus.

The two defects in the first audit are repaired. The candidate now attributes
gcd-free bases as known infrastructure and identifies F56/P65 as the closest
project result. It also measures total decoder complexity in $L+n$, where
$n=\lceil\log_2(N+1)\rceil$. The explicit $x_i$ residues add at most
$O(mn)$ encoded bits and operations, which is polynomial in $L+n$ because
$m\le L$.

No research computation was used in this audit.

## 1. The refinement invariant passes, including degenerate pairs

The multiset initially contains $(a_i,\mathbf e_i)$ for every $a_i>1$.
For each coordinate $i$, it represents

\[
a_i=\prod_{(b,w)}b^{w_i}.
\]

Take two distinct multiset occurrences $(x,\alpha)$ and $(y,\beta)$ and put
$d=\gcd(x,y)>1$. Replacing them by the nonunit members of

\[
(d,\alpha+\beta),\qquad(x/d,\alpha),\qquad(y/d,\beta)
\]

preserves every coordinate because

\[
d^{\alpha_i+\beta_i}(x/d)^{\alpha_i}(y/d)^{\beta_i}
=x^{\alpha_i}y^{\beta_i}.
\]

This remains exact in the two risky cases:

- If $x=y$, both quotients are $1$, and the retained entry
  $(x,\alpha+\beta)$ merges the two occurrences.
- If $x\mid y$, the retained entries are
  $(x,\alpha+\beta)$ and $(y/x,\beta)$. If they still overlap, a later
  refinement handles that overlap.

Two output entries can have the same integer part. They remain two multiset
occurrences until a later iteration merges them. Dropping an integer part
equal to $1$ changes no represented value.

At termination no two distinct remaining entries have gcd larger than $1$.
Their integer parts are therefore pairwise coprime and their stored columns
give all exponents $e_{ij}$.

## 2. The valuation potential proves polynomial termination without an oracle

For proof only, define

\[
\Phi=\sum_p\sum_{(b,w)}v_p(b)^2.
\]

The algorithm never evaluates $\Phi$ and never asks for any $v_p(b)$.

For a prime dividing the selected gcd, let the selected valuations be
$r\ge s>0$. Before refinement their contribution is $r^2+s^2$. Afterwards
it is

\[
s^2+(r-s)^2.
\]

The decrease is

\[
r^2+s^2-s^2-(r-s)^2=s(2r-s)\ge1.
\]

A prime outside the gcd has valuation zero in at least one selected entry and
its contribution does not change. Thus every performed refinement decreases
the nonnegative integer $\Phi$ by at least one.

Initially,

\[
\sum_pv_p(a_i)^2
\le\left(\sum_pv_p(a_i)\right)^2
\le(\log_2a_i)^2.
\]

With

\[
L=m+\sum_i\left\lceil\log_2(a_i+1)\right\rceil,
\]

this gives $\Phi_0\le L^2$. Hence at most $L^2$ refinements occur. Unknown
prime valuations appear only in this termination proof; the executable loop
uses ordinary gcd tests.

## 3. All refinement storage and bit bounds pass

Each refinement removes two entries and inserts at most three, so at most
$m+L^2$ entries ever exist. Each new integer part is a divisor of one of the
selected integer parts. Basis integers never grow and have at most $L$ bits.

For every stored $(b,w)$ and coordinate $i$, positivity and the invariant show
that $b^{w_i}$ divides $a_i$. Since $b\ge2$,

\[
0\le w_i\le\log_2a_i.
\]

There are $O(L^3)$ exponent entries and each has $O(\log L)$ bits. A full
pair scan has $O(L^4)$ gcd tests. At most $O(L^2)$ scans are needed, including
the final terminating scan. The stated $O(L^6)$ gcd-test count follows. Gcd,
exact division, comparisons, and $m$-coordinate exponent additions on these
bounded values give a fixed polynomial bit cost. The candidate's conservative
$O(L^{10})$ bound is safe.

## 4. Composite coprime blocks need only one square/nonsquare flag

Let

\[
a_i=\prod_jg_j^{e_{ij}}
\]

be the output representation, and for a binary subset $c$ put

\[
E_j=\sum_ic_ie_{ij}.
\]

If $g_j$ is a square, then $g_j^{E_j}$ is a square for every $E_j$. If
$g_j$ is not a square, some prime has odd valuation in $g_j$, so
$g_j^{E_j}$ is a square exactly when $E_j$ is even. Pairwise coprimality
ensures that no other block can correct that odd valuation.

Therefore the matrix with rows

\[
M_{ji}=e_{ij}\bmod2
\]

for nonsquare blocks has

\[
Mc=0
\quad\Longleftrightarrow\quad
\prod_ia_i^{c_i}\text{ is an integer square}.
\]

The internal prime factors of a nonsquare composite block are not needed.
An exact integer square test of the complete block supplies all information
required for subset parity.

## 5. Exact positive roots are computable with bounded intermediates

For $c\in\ker M$, each $E_j$ belonging to a nonsquare block is even. If
$h_j=\sqrt{g_j}$ for a square block, then

\[
R(c)=
\prod_{j\notin J}h_j^{E_j}
\prod_{j\in J}g_j^{E_j/2}
\]

is exactly the positive integer root of the selected product. This formula
requires no prime factorization.

The selected product has at most the sum of the input-integer bit lengths.
Every power in the displayed formula divides its positive final root. Binary
exponentiation and monotone multiplication therefore keep all exact
intermediates at $O(L)$ bits. Computing roots for at most $m$ kernel-basis
vectors remains polynomial.

## 6. The generalized overlap identities pass exactly

Theorem 3 assumes a known unit residue $x_i\bmod N$ with

\[
x_i^2\equiv a_i\pmod N.
\]

Thus every $a_i$ is also a unit modulo $N$. For binary vectors define

\[
X(c)=\prod_ix_i^{c_i}\pmod N.
\]

For kernel vectors $c,d$, the indices selected twice form an overlap set
$I=\{i:c_i=d_i=1\}$. Positivity gives the exact integer identity

\[
R(c)R(d)=R(c\oplus d)\prod_{i\in I}a_i.
\]

The modular witnesses give

\[
X(c)X(d)
\equiv X(c\oplus d)\prod_{i\in I}x_i^2
\equiv X(c\oplus d)\prod_{i\in I}a_i
\pmod N.
\]

Every overlap factor is a unit, so the common overlap product can be
cancelled modulo $N$. Also

\[
R(c)^2=\prod_ia_i^{c_i}\equiv X(c)^2\pmod N.
\]

The product $X(c)$ is a unit, and its inverse exists. Hence

\[
\rho(c)=R(c)X(c)^{-1}\pmod N
\]

is defined, satisfies $\rho(c)^2=1$, and obeys

\[
\rho(c)\rho(d)=\rho(c\oplus d).
\]

Thus the normalized exact-root map is a genuine group homomorphism from the
complete parity kernel to the roots of $1$ modulo $N$.

## 7. Testing any kernel basis is complete

Let $B$ be an arbitrary binary basis of $\ker M$. If every $b\in B$ maps
under $\rho$ to $1$ or $-1$, then every product of basis images also belongs
to the subgroup $\{1,-1\}$. Since $B$ generates the kernel, every kernel
vector would then have a global normalized root.

The contrapositive is exact. If any square subset $c$ has

\[
R(c)\not\equiv\pm X(c)\pmod N,
\]

then every basis of $\ker M$ includes at least one vector with a non-global
normalized root. The decoder need not enumerate exponentially many kernel
vectors.

This conclusion also covers bases containing singleton or duplicate-input
relations. It depends on the unit hypothesis; the candidate states that
hypothesis explicitly.

## 8. The gcd extraction covers arbitrary odd nonsquarefree $N$

Write

\[
N=\prod_tp_t^{\alpha_t}
\]

with distinct odd primes $p_t$. A root $z$ of $1$ modulo one component
$p_t^{\alpha_t}$ is $1$ or $-1$. Indeed, the prime power divides
$(z-1)(z+1)$, while $\gcd(z-1,z+1)$ divides $2$. Since $p_t$ is odd, the
whole prime power divides one factor.

For a basis vector with non-global $\rho$, both sign classes of prime-power
components are nonempty. Because $X$ is a unit,

\[
R-X\equiv X(\rho-1),
\qquad
R+X\equiv X(\rho+1)\pmod N.
\]

On a plus component, the first difference is divisible by the complete prime
power and the second is a unit. On a minus component, the roles reverse.
Consequently the two gcds are exactly the products of the two nonempty proper
sets of complete prime-power components. Both are proper nontrivial divisors.

Repeated factors cause no gap. For an odd prime or odd prime power, no
non-global root exists, so the implication has a false premise and cannot
return a false factor.

## 9. The full encoded-input and operation bounds pass

Let $n=\lceil\log_2(N+1)\rceil$. Represent each residue $x_i\bmod N$
canonically using $O(n)$ bits. The full pair list uses

\[
O(L+mn+n)
\]

bits. Since $m\le L$,

\[
mn\le (L+n)^2,
\]

so reading and storing all witnesses is polynomial in $L+n$.

The input premises can also be checked without factoring: reduce every
$x_i$, verify $x_i^2\equiv a_i\pmod N$, and verify
$\gcd(x_i,N)=1$. This costs $m$ modular squarings and gcds on $O(n)$-bit
values, plus reductions of the explicitly encoded $a_i$.

The gcd-free refinement and exact-root work are polynomial in $L$. The matrix
has at most $m+L^2$ rows and $m$ columns. Gaussian elimination is polynomial
in $L$. A kernel has dimension at most $m$. For each basis vector, computing
$X(c)$ takes at most $m$ modular multiplications, followed by two gcds on
$O(L+n)$-bit values. Thus all witness processing and the at most $2m$ final
gcds have fixed polynomial cost in $L+n$.

The earlier all-one counterexample to an $L$-only claim is now covered because
$n$ is explicit. No unknown factor, modular square-root routine, order finder,
or factoring oracle is invoked.

## 10. Adversarial edge cases pass

- **One:** If $a_i=1$, its matrix column is zero and its exact root is $1$.
  Its supplied $x_i$ can be any unit root of $1$. If the normalized singleton
  root is non-global, the basis test correctly factors $N$.
- **Duplicates:** Equal $a_i$ values remain distinct columns. Their known
  residues $x_i$ may also differ. The exact overlap identities use each
  occurrence and remain valid. A two-copy relation has exact root equal to
  the repeated integer, while its modular comparison root is $x_ix_j$.
- **Square inputs:** A square block contributes no parity row. Singleton
  square relations are retained, and the formula uses the exact positive
  square root.
- **Prime powers inside basis blocks:** A composite coprime block can be a
  prime power or contain several primes. Its perfect-square flag is sufficient
  by Section 4.
- **Zero:** Theorem 1 and the vector-space equivalence require positive inputs.
  The theorem states positivity. Unit congruence pairs also imply
  $\gcd(a_i,N)=1$.
- **Nonunit witnesses:** Theorem 3 does not admit them. A proper
  $\gcd(x_i,N)$ is already a factor; gcd $1$ verifies the theorem's premise;
  gcd $N$ is explicitly excluded from the homomorphism route. No invalid
  cancellation is performed.
- **Prime and prime-power $N$:** No non-global normalized root exists for odd
  prime powers. The decoder makes no improper factor claim.
- **Repeated factors and arbitrary odd composites:** The local sign proof uses
  complete prime-power components and therefore covers nonsquarefree $N$.
- **Large exact inputs:** The basis integers do not grow, and every exact root
  has at most the bit length of a selected input product. All lengths are
  included in $L+n$.

## 11. P01, prior art, and scope now pass

For each nonsquare basis block $g_j$, choose for proof a prime having odd
valuation in that block. Pairwise coprimality means the chosen prime occurs in
no other block. The nonsquare block classes are therefore independent in
$\mathbb Q^\times/(\mathbb Q^\times)^2$, and the columns of $M$ are exactly
the input square classes in this basis. Hence

\[
\operatorname{rank}M
=\operatorname{rank}([a_1],\ldots,[a_m]).
\]

F58 meets P01 with equality. It does not compress rank or create a relation.

The candidate now correctly separates the provenance:

- gcd-free or coprime bases are known infrastructure from Bach--Shallit and
  the earlier work cited there;
- Bernstein supplies a substantially faster known coprime-base algorithm;
- detecting multiplicative relations through such bases is standard;
- F56/P65 is the closest project decoder;
- F58's project-level contribution is the synthesis of a complete gcd-free
  coordinate system, block square tests, exact roots, and arbitrary-basis
  modular extraction;
- no publication-level novelty is claimed without a dedicated literature
  review.

This boundary is accurate and does not overstate the result.

## 12. Exact consequence and remaining gap

F58 strictly removes F56/P65's short-interval and small-prime decoder premise.
Any explicit list of polynomial total bit length can be passed to the gcd-free
decoder. The unit-pair theorem covers both the inverse-quotient special case
$a_i=Nk_i+1$, $x_i=1$, and ordinary unit congruence-of-squares pairs.

The theorem does not make a relation exist. It does not prove that any
polynomial-size list computable from bare $N$ contains a square subset. It
also does not prove that a dependency has a non-global normalized root or
that a useful list is produced with sufficient probability on every input.
The all-input useful-relation law remains the source-side missing theorem.

F58 is therefore a correct deterministic polynomial-time decoder and a
strict project-level simplification. It is not a factoring algorithm. Subject
to the required proof-blind reconstruction, the corrected artifact is ready
for promotion at this exact scope.
