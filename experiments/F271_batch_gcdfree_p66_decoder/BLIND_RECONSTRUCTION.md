# F271 blind reconstruction

## Authentication and verdict

The only mathematical source used for this reconstruction was `STATEMENT.md`,
authenticated before inspection as

```text
19b288038c4f9e339d3f56e51fb1c6d7277fd9e322e486f2339edd0c68bf64ba
```

I also read only the root `PROMPT.md` and `AGENTS.md` for task and workspace
rules. I did not inspect a proof, self-audit, provenance file, manifest,
checker, history, or another reconstruction.

**Verdict: PASS.** The saturation identity, exact two-base recursion, global
invariant, termination, gcd count, verification tree, square-kernel closure,
root homomorphism, peel distinction, asymptotic bounds, and all stated F265
constants reconstruct from first principles. The theorem is a conditional
decoder theorem. It does not supply the F265 bank or assert that a useful
relation exists.

## 1. Saturation

Let (L=\operatorname{bitlen}(u)). For each prime power (p^a\Vert u),
(a\le L), because (2^a\le p^a\le u<2^L). If (p\mid v), then
(p^a\mid v^L), so the (p)-primary part of
(\gcd(u,v^L\bmod u)) is (p^a). If (p\nmid v), then (v^L) is a unit
modulo (p), so the gcd has no factor (p). Therefore

\[
 \operatorname{Sat}(u;v)=\prod_{p\mid v}p^{v_p(u)}.
\]

Computing (v^L\bmod u) by repeated squaring never materializes (v^L).
This operation uses modular powering and one integer gcd, not rational-prime
factorization.

## 2. Exact refinement of two integers

### Equal support

Write, for one prime in the common support,

\[
 \alpha=v_p(x),\qquad \beta=v_p(y),\qquad
 \delta=\min(\alpha,\beta).
\]

Then the exponents in (x_0=x/d) and (y_0=y/d) are respectively
((\alpha-\beta)_+) and ((\beta-\alpha)_+). Thus their supports are
disjoint. Saturation gives the following exhaustive, disjoint cases:

\[
\begin{array}{c|ccc}
 &A&B&C\\ \hline
\alpha>\beta&p^\beta&1&1\\
\alpha<\beta&1&p^\alpha&1\\
\alpha=\beta&1&1&p^\alpha.
\end{array}
\]

Consequently (A,B,C) are pairwise coprime, (AB\mid d), and each
recursive pair has equal nonempty prime support. If a child block has
exponents ((u,v)) in ((x_0,A)), then its contributions to ((x,y)) are
((u+v,v)). For a child from ((y_0,B)), they are ((v,u+v)). A factor of
(C) has coordinates ((1,1)). These are exactly the displayed coordinate
maps.

For termination, at every prime a recursive step replaces a positive pair
((\alpha,\beta)) by either ((\alpha-\beta,\beta)) or
((\beta-\alpha,\alpha)), unless the exponents are equal and the prime stops
in (C). The sum of the two positive exponents strictly decreases along
every continuing prime path. Hence every path and the finite recursion tree
terminate. Disjoint support among the two children and (C), followed by
induction, proves that all returned blocks are pairwise coprime and reconstruct
both inputs exactly.

### Arbitrary overlap

For (x_s=\operatorname{Sat}(x;y)), a prime occurs exactly when it divides
both (x) and (y), and then it occurs to its full exponent in (x).
The analogous statement holds for (y_s). Hence

\[
 \operatorname{supp}(x_s)=\operatorname{supp}(y_s),\qquad
 \gcd(x_s,y_s)=\gcd(x,y)=d.
\]

The quotients (x/x_s) and (y/y_s) contain only the two exclusive prime
supports. They are coprime to each other and to every shared output. Appending
them with coordinates ((1,0)) and ((0,1)) proves the full `TWO_BASE`
contract.

## 3. Global insertion and its invariant

Before a row is inserted, the blocks are pairwise coprime and their exponent
vectors reconstruct all earlier rows. During insertion, include the current
row coordinate in blocks already absorbed and maintain

\[
 a_i=(\text{absorbed block powers})\,y.
\]

If (\gcd(y,P)=1), the residual is coprime to every leaf and can be inserted.
Otherwise, tree descent finds an overlapping leaf (b). On a left branch the
new gcd is computed. On a right branch the carried gcd remains exact: the
left and right subtree products are coprime, and the left gcd was one.

`TWO_BASE(b,y)` replaces (b) by its pieces with local (b)-exponent
(u>0). If the old coordinate vector was (w), the exact new vector is

\[
 uw+ve_i,
\]

because (b=\prod q^u) and the current residual contributes
(y=\prod q^v). Pieces with (u=0) are precisely residual-only support.
Their product to the powers (v) is the new (y). Pairwise coprimality from
`TWO_BASE` and the old global coprimality prove the invariant after the
replacement. The residual is also coprime to every block touched earlier in
this row.

Every overlap removes at least one distinct prime from the residual support.
Thus a row causes at most (\omega(a_i)) touches, and the loop terminates.
Fixed row order, left-first descent, recursion branch order, integer sorting,
and lowest-vacancy placement make the algorithm deterministic.

At every intermediate time, the product of the distinct blocks divides the
product of the rows seen so far, including the absorbed part of the current
row. Since every block exceeds one, the number of live leaves is at most the
total input bit budget. Therefore the proposed power-of-two tree with at
least (R) leaves cannot overflow. At completion the invariant gives

\[
 a_i=\prod_{j=1}^S q_j^{e_{ji}}
\]

with pairwise-coprime (q_j>1).

## 4. Independent terminal verification

Let (P=\prod_jq_j=q_jM_j). Reduction modulo (q_j^2) gives

\[
 P\bmod q_j^2=q_j(M_j\bmod q_j).
\]

It is therefore exactly divisible by (q_j), and

\[
 \gcd\left(q_j,{P\bmod q_j^2\over q_j}\right)
 =\gcd(q_j,M_j).
\]

This gcd equals one exactly when (q_j) is coprime to every other block.
Computing all remainders with one remainder tree and taking one gcd per leaf
verifies the whole list in exactly (S) gcd calls. Exact reconstruction of
each input row is then a separate multiplication-and-equality check.

## 5. Square kernel and low-support closure

Because the (q_j) are pairwise coprime, a product
(\prod_jq_j^{E_j}) is square exactly when every nonsquare (q_j) has even
(E_j). A square block imposes no parity condition. Thus for a binary row
selector (c),

\[
 \prod_i a_i^{c_i}\text{ is square}
 \iff Ac=0,
\]

where (A) has one row for each nonsquare block and column (i) is
(\sigma_i).

It follows immediately that (e_i) is a relation exactly when
(\sigma_i=0), and (e_i+e_j) is a relation exactly when
(\sigma_i=\sigma_j). The zero-signature coordinates form a full coordinate
space with basis (\{e_i:i\in Z\}). Within a nonzero class (C), all
weight-two relations form its even-weight subspace, with star basis

\[
 \{e_{r_C}+e_i:i\in C\setminus\{r_C\}\}.
\]

Different classes have disjoint coordinate support. The displayed union is
therefore independent and is exactly the span of all kernel vectors of
support at most two. The exact weight-one and weight-two counts are

\[
 |Z|,qquad { |Z|\choose2}+\sum_{C\ne Z}{|C|\choose2}.
\]

For the complement, put the low basis (L) in canonical RREF. Normal form
modulo (L) clears its pivot columns. Images of a full kernel basis span the
quotient (\ker A/\operatorname{span}(L)); retaining an independent RREF
basis of those images gives (C). All vectors remain in the kernel, all
vectors in (C) have zero entries at the pivot columns of (L), and hence

\[
 \operatorname{span}(L)\cap\operatorname{span}(C)=0,
 \qquad
 \operatorname{span}(L)+\operatorname{span}(C)=\ker A.
\]

The two dimensions sum to (\dim\ker A\le m). The prescribed pivot and
ordering rules make both bases canonical.

## 6. Exact roots and complete basis classification

For (c\in\ker A), set (E_j=\sum_i c_i e_{ji}). The parity condition makes
(E_j/2) integral for nonsquare (q_j). For square (q_j=h_j^2), its root
contribution is (h_j^{E_j}). Therefore

\[
 R(c)=
 \prod_{q_j\text{ square}}h_j^{E_j}
 \prod_{q_j\text{ nonsquare}}q_j^{E_j/2}
\]

is the exact positive square root of (\prod_i a_i^{c_i}). The supplied
roots give

\[
 X(c)^2\equiv\prod_i a_i^{c_i}\equiv R(c)^2\pmod N.
\]

Every (v_i), hence (X(c)), is a unit modulo (N), so
(\rho(c)=R(c)X(c)^{-1}) is a root of one.

The group law on the binary kernel is xor. If both (c_i=d_i=1), then the
row (a_i) occurs twice in (R(c)R(d)), while (v_i^2\equiv a_i\pmod N)
occurs in (X(c)X(d)). These identical factors cancel in the ratio, proving

\[
 \rho(c\mathbin\oplus d)=\rho(c)\rho(d)\pmod N.
\]

Thus (\rho) is a homomorphism. The global roots (\{1,-1\}) form a
subgroup. If every vector of a basis maps into that subgroup, every kernel
vector does. Conversely, a non-global image of any basis vector is already
a certificate. For odd (N), every root of one is (+1) or (-1) modulo
each prime-power divisor of (N): the two factors (r-1,r+1) differ by two,
which is a unit at every odd prime. A non-global root has both signs among
the prime-power components, so each of

\[
 \gcd(r-1,N),\qquad \gcd(r+1,N)
\]

is nontrivial and proper. Hence classifying the low basis and its complement
is complete and uses at most (m) exact roots, (m) modular inversions, and
(2m) signed gcds. It does not enumerate all relations.

## 7. The two peel rules are different

On an active row set, positive-support privacy of (q_j) to row (i) is
exactly

\[
 e_{ji}>0,\qquad e_{jk}=0\quad(k\ne i\text{ active}).
\]

Such a block forces the active kernel coordinate (c_i) to zero precisely
when (q_j) is nonsquare and (e_{ji}) is odd. This proves the stated D05
deletion test. Simultaneous deletion is safe because every deleted coordinate
is forced to zero before the round; restricting the already known exponent
vectors and repeating needs no new gcd.

Parity-degree-one peeling asks only that (e_{ji}) be odd and all other
active (e_{jk}) be even. The corresponding matrix row is a unit vector, so
this rule is also kernel-safe. It contains the positive-support rule and can
be strictly stronger. The valuation vector ((1,2)) gives the stated strict
example: its parity support is only the first row, while its positive support
contains both rows. Therefore counters and semantics for these peels cannot
be interchanged.

## 8. Global resource and gcd bounds

The touch bound follows from the strict loss of residual prime support:

\[
 T\le\sum_i\omega(a_i)=I.
\]

For the recursion bound, follow one rational prime through an equal-support
tree. Let (f(\alpha,\beta)) be the number of recursion nodes on that prime's
path. Subtractive recursion and induction give

\[
 f(\alpha,\beta)\le
 \alpha+\beta-\gcd(\alpha,\beta).
\]

Indeed, equality of the arguments stops in one node, and if
(\alpha>\beta), the next pair is ((\alpha-\beta,\beta)); the induction
bound plus the current node is at most
(1+\alpha-\gcd(\alpha,\beta)\le
\alpha+\beta-\gcd(\alpha,\beta)).

For a fixed prime, let its positive input valuations, in row order, be
(\alpha_1,\ldots,\alpha_s), and let
(g_k=\gcd(\alpha_1,\ldots,\alpha_k)). Its base exponent before occurrence
(k) is (g_{k-1}), and afterward it is (g_k). Thus its total path-node
incidence is at most

\[
 \sum_{k=2}^s(g_{k-1}+\alpha_k-g_k)
 =g_1-g_s+\sum_{k=2}^s\alpha_k
 \le\sum_{k=1}^s\alpha_k.
\]

Every recursion node contains at least one prime and is counted by at least
one such path incidence. Summing over primes proves (E\le V).

Finally, each final block contains a prime that occurs in no other final
block. Hence

\[
 S\le\#\{p:p\mid\prod_i a_i\}\le I.
\]

Now count gcd calls. Each touch uses one root gcd and exactly one left-child
gcd at each of the (D) tree levels, giving ((D+1)T). There is at most one
final no-overlap root gcd per row, giving (m). Across the forest of
equal-support recursions, the (T) roots have supplied gcds. The other
(E-T) nodes compute a gcd, and exactly (E-T) child edges are created by
internal saturation calls. The two outer saturation calls in every
`TWO_BASE` contribute (2T). Hence all two-base refinement uses exactly

\[
 (E-T)+(E-T)+2T=2E
\]

gcd calls. Terminal coprimality verification adds (S). This proves

\[
 (D+1)T+m+2E+S
 \le (D+1)T+m+2V+S.
\]

Since (I,V,S,m\le R) and (D=O(\log R)), the scalar gcd count is
(O(R\log R)), which is subquadratic in (R).

## 9. Bit complexity

All exact block products and all residuals have (O(R)) bits. Exponent
coordinates are at most the corresponding input valuations and have
(O(\log R)) bits. There are (O(R)) recursion outputs and leaf changes.

With schoolbook arithmetic, a gcd on (O(R))-bit operands costs (O(R^2)).
The tree searches and updates therefore cost (O(R^3\log R)). There are
(O(R)) saturation calls. Each uses (O(\log R)) modular multiplications
on (O(R))-bit operands, so all saturation work is also
(O(R^3\log R)). Coordinate propagation, sorting, exact reconstruction,
and the product/remainder verification fit below the same conservative cap.
This reconstructs the stated deterministic refinement bound.

Let (n_N=\operatorname{bitlen}N) and (L=R+n_N). The binary matrix has at
most (R) rows and columns, so elimination is (O(R^3)) bit operations.
There are at most (m\le R) basis vectors. For one exact relation root, the
sum of the output bit lengths of its prime-free block powers is (O(R));
schoolbook powering with geometrically growing operands and their product
cost (O(R^2)). Across all roots this is (O(R^3)). At most (R^2)
modular multiplications on (n_N)-bit residues suffice for all (X(c)),
which costs (O(R^2n_N^2)\subseteq O(L^4)). Inversions, signed gcds,
square tests, and verification are smaller. Also
(R^3\log R\subseteq O(L^4)). Thus the complete decoder has the claimed
conservative (O((R+n_N)^4)) bit bound.

Here a supplied residue is represented canonically modulo (N), as the term
“residue” requires. If an external format permits arbitrarily long, unreduced
integer spellings of the same residue, their read and reduction cost must be
added to that format's byte contract; it is not a decoder-arithmetic issue.

## 10. Independent reconstruction of the F265 constants

For a positive integer of bit length at most 361,

\[
 \sum_pv_p(a)\le\log_2a<361,
\]

so this integer-valued sum is at most 360. Therefore

\[
 V\le64\cdot360=23{,}040.
\]

An independent Eratosthenes sieve and exact integer multiplication give

\[
 p_{58}=271,\quad \operatorname{bitlen}(p_{58}\#)=368,
\]

\[
 p_{1875}=16103,\quad \operatorname{bitlen}(p_{1875}\#)=23{,}102,
\]

\[
 p_{1876}=16111,\quad \operatorname{bitlen}(p_{1876}\#)=23{,}116.
\]

These finite values were regenerated from the statement alone. For exact
result identification, the SHA-256 hashes of the unsigned big-endian
primorial integers at indices 58, 1875, and 1876 are respectively

```text
5f804dbb4e028f4df222ac360530bfdc512f1daf6fa133b848520effd946c2e1
44e0cbd9cc1efa9f4a076edc46b0a7be0c5d8c2fa8392cf615d6a3df1c268185
ac3ef668cee3d20890a623c05237798c19428e1fddb294b5fa1579948c72ded4
```

If a 361-bit row had 58 distinct prime divisors, it would be at least the
58th primorial, which is far larger than (2^{361}). Hence every row has at
most 57 distinct prime divisors. The first inserted row cannot touch an old
block, so

\[
 T\le(64-1)\cdot57=3{,}591.
\]

Moreover,

\[
 \prod_{i=1}^{64}a_i<2^{64\cdot361}=2^{23{,}104}.
\]

The product of the final pairwise-coprime blocks divides this row product.
The product of any (S) pairwise-coprime integers greater than one is at
least the (S)-th primorial: select one distinct prime divisor from each
block and minimize those primes. Since the 1876th primorial is at least
(2^{23{,}115}>2^{23{,}104}), (S\ge1876) is impossible. Therefore

\[
 S\le1875.
\]

The adjacent 1875th primorial has only 23,102 bits, so this exact adjacent
cutoff is consistent with the aggregate input-size bound. A 2,048-leaf tree
has depth (D=11) and suffices. Substitution gives

\[
 12\cdot3591+64+2\cdot23040+1875
 =43{,}092+64+46{,}080+1{,}875
 =91{,}111.
\]

Across 768 banks,

\[
 91{,}111\cdot768=69{,}973{,}248.
\]

Finally,

\[
 {7{,}208{,}878{,}080\over69{,}973{,}248}
 =103.02334\ldots,
\]

so the stated approximate factor (103.02) is correct. It is only a scalar
gcd-call comparison; operand widths differ, so it is not a runtime ratio.

## 11. Scope and unavoidable output

All decoder steps above use gcd, exact division, modular powering, integer
square root/testing, sorting, product/remainder trees, and binary elimination.
None requires rational-prime factorization. The elliptic source, F265 bank
completeness, the 64-row residual claim, existence of a nonzero square
kernel, existence of a non-global image, and the separate coordinate/chord
controls are not consequences of this decoder and remain outside the
theorem.

If every block is square, the parity matrix has no rows, every signature is
zero, and every one of the ({m\choose2}) row pairs is a support-two hit.
Any format requiring one serialized record per hit must therefore perform
(\Theta(m^2)) output work. The count, span, existence test, and factor
certificate do not require those records. This proves the stated output
boundary without reintroducing a quadratic arithmetic step.

The prior-art and novelty remarks are not premises of any proof above. The
verified claim is the explicit decoder theorem and its specialization, not a
publication-level novelty claim.
