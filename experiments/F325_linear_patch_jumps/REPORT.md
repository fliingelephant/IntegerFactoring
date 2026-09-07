# F325: changing the parity pairing to permit exact linear jumps

**Family:** route:F31

The contracted chains retain the inverse and sign-selected modular path of
F322, so they belong to the retained modular-hyperbola family.

Status: candidate exact construction and cost analysis. Independent verification and finite implementation results are separate. No quasipolynomial bound is established.

## Material change from F324

F324 kept Jeřábek's involution unchanged. A translation block could contain a fixed nonunit vertex, so jumping over it could silently miss the endpoint that justifies the path. This construction changes the involution on an explicit negation-closed set before jumping. The formerly fixed vertices in that set are paired off. The resulting graph has its own valid endpoint guarantee.

Let N>1 be odd, h=(N-1)/2, and a,b be units modulo N. Centered representatives lie in [-h,h]. Write t=b^-1 modulo N, and let

\[
 D^*=\{(1,x):x\ne0,\quad
 \operatorname{sgn}(x),\operatorname{sgn}(\operatorname{rep}(ax)),
 \operatorname{sgn}(\operatorname{rep}(tx))\text{ are not all equal}\}.
\]

This definition deliberately includes nonunits x. Define r* to send (1,x) to (1,-x) on D*, and to agree with the F322 source involution r elsewhere.

## Pairing and endpoint proof

Multiplication by a unit does not send a nonzero residue to zero. Negating x therefore reverses all three signs in the definition of D*, so D* is closed under negation and has no fixed point under it. On unit coordinates, r already agrees with negation throughout D*. On nonunit coordinates, the old r fixes every vertex, so D* is also closed under the old r. Its complement is consequently r-invariant. Replacing r on D* by its fixed-point-free negation pairing yields an involution on all 3N vertices.

Every r*-fixed vertex is an original r-fixed vertex outside D*. The original verified divisor-or-root decoder applies unchanged. This statement deletes endpoints; it does not assert that the modified path reaches the same endpoint as the original path.

Use the common-one reflection matching from F324. It acts by
\[
 s(e,x)=(e,\operatorname{rep}(1-x))
\]
except that its fixed points at (0,-h) and (1,-h) are paired together. Its sole fixed point is (2,-h). Starting there and alternating r* then s reaches an r*-fixed endpoint in at most 3N r* calls, by the usual two-matchings path argument. No general graph oracle is used.

## Exact first-exit primitive

At (1,x) in D*, except x=h, one complete r*-then-s step is
\[
 (1,x)\longmapsto(1,x+1).
\]
For x=h, r* reaches (1,-h), whose auxiliary s-edge goes to (0,-h). This port step must be handled explicitly. At x=0 the D* rule does not apply.

For positive x<h in D*, let z be the minimum integer larger than x for which both residues az mod N and tz mod N lie in [1,h], or h if there is no earlier such integer. Then all source coordinates x,...,z-1 belong to D*, and their r*-then-s transitions are exactly the translation segment ending at (1,z). This segment represents z-x calls to r*.

For negative x in D*, let z be the minimum integer larger than x for which both residues lie in [h+1,N-1], or 0 if there is no earlier such integer. The same conclusion holds for x,...,z-1. A nonunit in this skipped interior is not an endpoint of r*: its negation partner was installed by the construction. This is why no interior gcd search is necessary.

The positive first-exit problem is integer optimization in the three variables z,k,l:
\[
 \begin{aligned}
  x+1\le z\le h,\\
  1\le az-Nk\le h,\\
  1\le tz-Nl\le h,
 \end{aligned}
 \qquad\text{minimize }z.
\]
If infeasible, return h. Including h as a feasible exit or using it as the fallback has the same result. The negative problem replaces the z interval by [x+1,-1] and both residue intervals by [h+1,N-1]; if infeasible, return zero. Coefficients a,t are chosen in [1,N-1]. Every input coefficient has O(log N) bits. There are three integer variables and six linear inequalities. Lower-dimensional or empty feasible sets cause no mathematical exception.

Exact fixed-dimensional integer feasibility is polynomial in the binary input length. Binary search on an added upper bound for z, with O(log N) feasibility calls, therefore supplies the exact first exit in polynomial bit complexity. This is a consequence of Lenstra's fixed-variable integer-programming algorithm; it is not an exact-counting assumption. See H. W. Lenstra Jr., *Integer programming with a fixed number of variables*, Mathematics of Operations Research 8 (1983), 538–548, introduction and §1, especially the witness statement at the end of §1. The author-hosted [primary paper](https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1983i/art.pdf) was inspected; its proof explicitly handles lower-dimensional sets in §2. Source caching is delegated separately through the repository's reference workflow.

Gurobi's finite optimization output is not identified with this exact bit-complexity algorithm. Exact candidate checks only prove feasibility. The finite experiment must separately compare the returned first exit against exhaustive integer search before treating its jump as validated. An arbitrary feasible later candidate does not certify an actual path contraction.

## Global elimination gives an ordered-subset matching

The local jumps have an exact global interpretation. Let
\[
 E=\{0\}\cup\{x\ne0:\text{the signs of }x,ax,tx\text{ are all equal}\},
 \qquad W=(\{0,2\}\times[-h,h])\cup(\{1\}\times E).
\]
All signs use centered representatives, and E includes qualifying nonunits. E is symmetric. Write its positive coordinates as e_1<...<e_m; this notation is for proof and does not require listing them. The restricted original involution r|W is well-defined because the removed set D* is r-invariant.

After deleting D* and contracting its alternating chains, the induced second matching on W has the following layer-1 edges:

\[
 (1,0)\leftrightarrow(1,e_1),\quad
 (1,-e_i)\leftrightarrow(1,e_{i+1})\ (1\le i<m),\quad
 (0,-h)\leftrightarrow(1,-e_m).
\]
When m=0 the only such edge is `(0,-h)<->(1,0)`. All other s edges on layers 0 and 2 remain unchanged. This is a matching with the same sole fixed point (2,-h).

For proof, start at (1,0) along its s edge toward coordinate 1. Every skipped positive coordinate y has r*-partner -y in D*, and the next s edge reaches y+1. The first retained positive coordinate is e_1. Starting at -e_i similarly advances through e_i+1,... until e_(i+1). After the largest e_m the chain reaches the auxiliary external port. Negation symmetry accounts for the reverse directions and ensures that every removed coordinate belongs to exactly one of these chains. There is no removed-only cycle.

Thus exact first-exit jumps realize a concrete compressed parity graph on 2N+2m+1 vertices. Its neighbor function is polynomial-bit using successor or predecessor queries on E, each reducible to the same three-variable integer program. The algorithm does not enumerate E or compute m. In particular, this construction is not conditional on a counting oracle.

The result identifies the surviving combinatorics: arithmetic inversion and decoding on W, coupled to an ordered-subset matching. Since 0<=m<=h, its universal state-count bound is still Theta(N). Better complexity requires control of the distinguished path in this compressed graph, not merely construction of its neighbor function.

## Special case a=-1: an entire layer contracts

If a=-1 modulo N, the signs of x and ax are opposite for every nonzero x. Thus D* consists of all nonzero layer-1 vertices, independently of b. Every positive D* run exits at h and every negative run at zero, with no optimization call.

There is a stronger graph description. All N layer-1 vertices form one alternating path between two external attachments:

- the s-edge `(0,-h) <-> (1,-h)`;
- the r*-edge `(0,1) <-> (1,0)`.

To see the second edge, (1,0) belongs to the B domain of the source pairing: f_(b^-1)(0)=1 and h(1)=(0,1). Inside layer 1, the r* edges pair x with -x for x!=0. The s edges reflect around 1/2, except its port. The negative-direction source sequence is -h,-h+1,...,-1,0; it encounters every layer-1 vertex on alternating r* and s edges. Consequently there are no additional internal cycles. This entire layer can be replaced by its known connector, retaining edge orientation at the two attachments.

For example, the oriented r*-then-s trajectory from (0,1) goes first to (1,1), then through the positive D* run and the port to (0,-h), using h+1 ordinary calls. If (0,1) is the current path source, it is not r*-fixed. This supplies one explicit O(log N)-bit connector computation replacing a linear number of steps. The reverse orientation is obtained by reversing the alternating path, not by asserting that the r*-then-s permutation is self-inverse.

The special choice a=-1 is not a uniform successful parameter source. It has Jacobi +1 only for N=1 mod 4, and it can be a square modulo all prime factors. The construction is useful on its stated promise class; general randomized factoring still requires a suitable public parameter distribution.

## Aggregate cost and success accounting

Let L be the number of ordinary r* calls of the full modified path. Partition its D* translations into J maximal contracted segments of lengths ell_1,...,ell_J. Let U count all remaining calls, including zero, port, inverse, and terminal steps. Then
\[
 L=U+\sum_{i=1}^J\ell_i,\qquad M=U+J.
\]
The accelerated algorithm has bit cost bounded by M times one fixed polynomial in log N, using exact first-exit optimization. The unaccelerated algorithm costs L times its smaller per-step polynomial. This is a certified reduction from expanded step count to boundary step count. The current universal bound is only M<=L<=3N.

For a=-1 the layer-1 connector can occur at most once along the undirected path, although its oriented source sequence must be counted correctly. Thus its elimination can save Theta(N) expanded steps on a path that uses it, while leaving the rest of the path unconstrained. In particular, the remaining two layers still have Theta(N) vertices. The connector identity alone gives no quasipolynomial bound on U or on the number of visits to other arithmetic branches.

For general a, repeated ILP jumps could save many linear transitions while inverse and other branches still dominate. No assertion is made that the boundary states are uniform, independent, or have factor density inherited from uniform residues. Their distribution is selected by the evolving arithmetic path.

There is a limited global endpoint-count guarantee. The original graph has 3(N-phi(N)-1) nonzero nonunit fixed vertices. Only layer-1 vertices can be removed, so at least 2(N-phi(N)-1) of them remain fixed. Thus at least two thirds of the original nonunit fixed-vertex mass survives. This count does not require computing phi(N) and is not used by the algorithm. It gives no bound on which endpoint the distinguished path reaches.

The original randomized divisor-or-root reduction remains valid with r*: every endpoint still decodes to a divisor or a root of a,b,ab. On an odd composite that is not a perfect power, publicly sampling a uniformly with Jacobi +1 and b with Jacobi -1 makes a a quadratic nonresidue with probability at least 1/2, in which event all three root alternatives are impossible. Thus a complete path still forces a factor with constant probability. This is a statement about valid full endpoints, not their locations or their number of macro steps.

With a macro cap K, let p_K(N) be the actual factor probability per capped attempt, including generation and any separately allowed verified gcd checks at boundaries. A sufficient target contract is
\[
 \frac{K\operatorname{poly}(\log N)}{p_K(N)}
 \le 2^{C(\log\log(N+1))^k}
\]
for uniform constants, after all solver, randomness, restart, and verification costs are charged. If exact first-exit calls have heterogeneous costs, use their total expected cost in the numerator instead of K. Extra boundary gcds return only correct factors, but may end a path earlier, so endpoint equality with the no-extra-check version must not be claimed.

## Finite evidence

`linear_patch_jumps.py` compares the original r micro walk, the modified r* micro walk, and exact-checked jumps along the modified walk. The 16 base pairs per dataset are public parameter pairs retained from F324. Extra a=-1 controls use the public Jacobi condition. The pilot has nine queries each at N=209 and 1333; the scale has eight at 10807 and nine at 66013. No hidden factor label selects an algorithmic transition.

| Dataset | Original r calls / factor endpoints | Modified micro calls / factor endpoints | Modified macro explicit calls / factor endpoints | Additional ILP calls | Skipped D steps |
|---|---:|---:|---:|---:|---:|
| pilot | 294 / 18 | 443 / 17 | 282 / 17 | 13 | 161 |
| scale | 1,117 / 17 | 1,516 / 17 | 1,192 / 17 | 64 | 324 |

All 35 macro executions match the modified micro endpoint and expanded path length exactly. They have no censors or unresolved optimizer results. Every computed first exit was checked against brute integer search: the 77 Gurobi calls had 76 optimal and one infeasible status, with exact agreement in each case. A separate a=-1 jump needed no solver. There were 78 macro actions in total. The a=-1 control at N=209 used 114 modified micro calls versus 10 explicit calls after contraction. These are finite exact comparisons, not an exact-uniform implementation of Lenstra's algorithm.

The original and modified endpoint agree on only 27 of 35 inputs. The pilot includes one valid root endpoint after modification where the original walk gave a factor. All scale endpoints are factors. The micro controls observe 24 visits to D nonunit vertices that are legally no longer fixed. The small exhaustive control covers 4,016 unit-parameter pairings and 295,944 vertices at odd N<=31. It checks 4,350 removed D nonunit fixed vertices and 19,698 remaining fixed endpoints.

The separate `induced_matching_check.py` checks the global ordered-subset formula on the same 4,016 parameter pairings. It traces each induced partner through the deleted D chains and compares with the explicit formula. All 224,970 retained-vertex comparisons agree; r|W invariance passes everywhere, and every induced matching has exactly the specified single fixed vertex. The control removes 70,974 D vertices in total, with largest traced deleted chain 15. Its named output, status and log retain the exact scope. This independently implemented finite check does not replace unbounded proof reconstruction.

The numerical conclusion requires charging the graph change, not just its compression. The macro saves 485 calls relative to its own modified micro walk, but uses 1,474 explicit calls plus 77 ILP calls on the same input list where the original needed 1,411 calls. It produces 34 factors versus 35. Even excluding all solver cost, calls per observed factor are 16.59 versus 16.33 in the pilot and 70.12 versus 65.71 in the scale. These finite ratios show no proposal-cost improvement for this family. They are not estimates of an all-input expected bound.

The pilot completed in 0.422110 seconds with 62,586,880 peak RSS bytes. The scale completed in 0.043112 seconds with 60,964,864 peak RSS bytes. Both used one solver thread, an internal 28-second alarm, an external 30-second timeout, and a 512 MiB ceiling. The induced-matching control used 0.578811 seconds and 32,522,240 peak RSS bytes under the same timeout and memory limits. Brute scans and micro controls are retained as validation work and are charged in measured wall time; they are not part of the claimed polynomial-bit first-exit algorithm. `RESOURCE.md`, the named sources, JSON outputs, run logs and status files retain evidence. The mathematical construction does not depend on Gurobi's floating optimality certificate.

## Next discriminating variation

The global chain description permits a selective modification: choose entire D* chains by a public rule, and install the nonunit negation pairing only in those chains. Each such chain consists of paired positive and negative coordinate intervals, so its union is negation-closed. Leaving all other vertices unchanged still defines an involution with valid remaining endpoints. For example, a threshold on full chain length can retain short-chain nonunit endpoints while permitting jumps on long chains. Predecessor and successor queries on E determine that length without scanning.

This variation has not been implemented or independently reconstructed in this packet. It is motivated by the observed loss of useful original endpoints. Its total cost must charge chain classification as well as changed success probability. A long skipped block alone is not a factoring gain.
