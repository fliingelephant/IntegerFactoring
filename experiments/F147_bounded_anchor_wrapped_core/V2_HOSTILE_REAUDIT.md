# F147 V2 hostile re-audit — PASS

## Frozen inputs

I read the following artifacts in full before reaching a verdict:

- `V2_STATEMENT.md`;
- the reused `PROOF.md`;
- the frozen V1 `STATEMENT.md`;
- `HOSTILE_AUDIT.md`;
- the failed `BLIND_RECONSTRUCTION.md`; and
- `MANIFEST.md`.

The two required hashes matched before the audit:

- `V2_STATEMENT.md`:
  `a65034746ef11b0165ee4c0591c68107997e14d7234df1a4c1a45482b905d87b`;
- `PROOF.md`:
  `6868737e521dcaa64473bc105d9fa85e1458947b5aa312bc98f3771e141577ad`.

The preserved V1 statement, hostile audit, and failed blind reconstruction
also matched the hashes recorded in the manifest. I did not modify any
frozen artifact or durable ledger.

## Verdict

**PASS.** V2 repairs the only defect found by the blind reconstruction. I
found no remaining false implication, decoder gap, source-legality change,
rank overclaim, or quasipolynomial cost overclaim within the stated frozen
P128 scope.

F147 V2 remains conditional. It contains every already-existing wrapped
cycle in an enumerable large core and completely decodes the standalone
bridge kernel on that core. It does not prove that the core has an edge, a
cycle, a nonzero kernel, a dependency that survives exact-value deletion,
or a non-global root.

## 1. The V2 length implication is exact

For a wrapped directed cycle, P131 gives

\[
A=\prod_{e=1}^{L}a_e>\sqrt N.
\]

The bound `a_e <= H` gives only `A <= H^L`. Since a cycle position has
`a_e>1`, one has `H>1`, so taking logarithms is valid. Therefore

\[
\sqrt N<A\le H^L
\quad\Longrightarrow\quad
L>\frac{\log N}{2\log H}.
\]

For integral `L`, this is equivalent to

\[
L\ge
\left\lfloor\frac{\log N}{2\log H}\right\rfloor+1.
\]

The strict inequality remains strict even when the quotient is an integer.
V2 does not reverse this implication. It explicitly says that the bound
does not supply legal anchors or an upper bound on the cycle length. Thus
the V1 counterexample `N=81`, `H=3` no longer attacks the statement: V2
does not claim that length two reaches the P131 scale.

The reused proof is compatible with this repair. It never uses the false V1
converse, and its final section already treats square-root-scale reach as a
necessary magnitude condition only.

## 2. Mixed cycles are impossible under `H^4 <= N`

Any directed cycle containing both edge types has an unwrapped-to-wrapped
transition. Write the last unwrapped edge and the next wrapped edge as

\[
qa^2=rT,
\qquad
rb^2>N.
\]

The endpoints `q` and `r` are distinct pairwise-coprime named blocks. Hence
`r | a^2`, so `r <= a^2`. It follows that

\[
a^2b^2\ge rb^2>N.
\]

But `a,b <= H` and `H^4 <= N`, so `a^2b^2 <= N`. This is a contradiction.
The strict inequality from wrapping also covers the boundary `H^4=N`.
Therefore a directed cycle with one wrapped edge has only wrapped edges.

## 3. Every wrapped cycle lies in the stated large core

For every legal position,

\[
t=\left\lfloor\frac{qa^2}{N}\right\rfloor<a^2\le H^2,
\]

because `q<N`. A wrapped position therefore has `1 <= t < H^2`.

For a wrapped cycle edge, `qa^2>N`, so

\[
q>\frac{N}{a^2}\ge\frac{N}{H^2}.
\]

Its target is the source of the next cycle edge. Section 2 makes that edge
wrapped, so the same bound holds for `r`. Since `c=rT<N`,

\[
1\le T<\frac Nr<H^2.
\]

This proves all four strict bounds in (5).

If two distinct named blocks `r,s>N/H^2` divided one residue `c<N`, their
pairwise coprimality would give `rs | c`. But

\[
rs>\frac{N^2}{H^4}\ge N>c,
\]

which is impossible. Thus uniqueness is exact per word position. It does
not assert one outgoing edge per vertex. Scanning all explicit positions
with large sources, keeping only wrapped positions with their unique large
target, retains every edge of every wrapped cycle. Conversely, every
retained core edge has both endpoints large, so its residual is below
`H^2`; its carry is below `H^2` for the position-level reason above.

## 4. The bridge square-class decoder is exact

For a retained edge,

\[
D=Uc=(qa^2)(rT)=qra^2T,
\qquad
D\equiv c^2\pmod N.
\]

The anchor is an explicit exact square. Complete multiplicity-aware
gcd-free refinement of all named centers and residuals, followed by maximal
perfect-power extraction, therefore gives the exact parity column of `D`.
After extraction, each pairwise-coprime decoder base is not a perfect power.
An odd total exponent on such a base leaves at least one odd rational-prime
valuation, while an even total exponent gives a square. Hence the kernel of
`M_H` is exactly the family of edge subsets with square bridge product.

The direct residual route is also complete. If `T<H^2`, trial division by
all primes through `H`, with multiplicity, leaves at most one prime cofactor.
A composite remainder would contain two prime factors larger than `H` and
would exceed `H^2`.

For `x in ker(M_H)`, write

\[
Y_x^2=\prod_{e:x_e=1}D_e,
\qquad
C_x=\prod_{e:x_e=1}c_e.
\]

All factors are units on the no-earlier-factor branch. Since each
`D_e = c_e^2 (mod N)`,

\[
\rho_x=Y_xC_x^{-1}\pmod N
\]

satisfies `rho_x^2=1 (mod N)`. The legal actual P128 pair satisfies

\[
C_eL_e=(c_ew_e)(U_ew_e)=D_ew_e^2.
\]

Its positive root is larger by `w_e`, and `w_e=c_e^{-1} (mod N)`. Thus the
actual-ledger selection and the conceptual bridge have the same normalized
root. This proves completeness for standalone bridge dependencies supported
on `G_H`. The statement does not claim completeness for arbitrary mixtures
with outside old columns.

## 5. Global exact-value deletion preserves every useful root

Map each selected actual `C_e,L_e` to its global exact-integer equality
class and take class multiplicities modulo two. Cancelling an equal pair
divides the positive square root by that common exact value. Every actual
P128 relation value is positive and congruent to one modulo `N`, so this
operation leaves the root modulo `N` unchanged.

If a bridge-kernel vector maps to zero, every selected actual value occurs
an even number of times. Its positive root is then a product of actual
relation values and is `+1 (mod N)`. Therefore the normalized-root
homomorphism is trivial on the deletion kernel and descends to the image in
the globally deduplicated ledger. In particular, a non-global root cannot
vanish under deletion.

Both the bridge selection map and the root map are homomorphisms under
binary addition. A basis of the exact-value image with tracked preimages is
therefore sufficient. If every basis root is `+1` or `-1`, every generated
root is global. If one basis root is non-global, then
`gcd(rho_x-1,N)` is nontrivial and proper: it is less than `N` because
`rho_x != 1`, and it cannot be one because
`(rho_x-1)(rho_x+1)=0 (mod N)` would then force `rho_x=-1 (mod N)`.

This cancellation uses equality of the legal actual values, not equality of
conceptual bridges. It does not violate P129's requirement to preserve
indexed supplied roots for equal bridge integers.

## 6. The edge-surplus bound is valid

In rational-prime parity space, every bridge column has the form

\[
v(q)+v(r)+v(T_e).
\]

All center terms lie in the span of the `m` named-block vectors. All
residual terms lie in the span of the `R_H` rational-prime unit vectors that
occur in residuals. Therefore

\[
\operatorname{rank}(M_H)\le m+R_H
\]

and rank-nullity gives

\[
\dim\ker(M_H)\ge E_H-m-R_H.
\]

The same count is visible in gcd-free refinement: each residual prime can
add or split off at most one decoder base, and multiplicity adds no row.
Every residual prime is strictly below `H^2`, so
`R_H <= pi(H^2)`. Thus both inequalities in (9) are correct.

The criterion `E_H>m+R_H` forces only a conceptual bridge dependency. V2
correctly leaves exact-value survival and root asymmetry as separate gates.

## 7. Source legality and quasipolynomial cost survive

The construction scans only the explicit legal positions already present
in the frozen P128 source. It retains each position's original word
provenance. Residues, residuals, and gcd-refined blocks are decoder data;
none becomes a new named generator or a new source position. This keeps the
theorem separate from an adaptive aggregate-feedback grammar.

There are at most `Q` positions and named blocks, so testing every possible
target needs at most `Q^2` exact divisions. Core integers have
`O(n+log H)` bits. There are at most `Q` core edges. Residual trial division
costs `O(QH)` divisions, and the parity, image, and tracked-preimage matrices
have dimensions polynomial in `Q`. Products used for a basis root have at
most `O(Q(n+log H))` bits. Gcd-free refinement, perfect-power extraction,
exact equality handling, binary elimination, exact square roots, modular
inverses, and final gcds are polynomial in the explicit transcript.

The complete outside ledger used for global equality classes retains the
inherited compact P128 representation bounds. Thus, within the declared
frozen-P128 scope, its comparison cost is also polynomial in the displayed
source parameters. The claim would need an explicit bit-length parameter if
detached from that source and applied to arbitrary huge ledger entries; V2
does not make that detached claim.

Substituting

\[
Q,H=2^{(\log n)^{O(1)}}
\]

makes every displayed polynomial cost quasipolynomial in `n`. Also
`4 log H=polylog(n)=o(n)`, while `log N=Theta(n)`, so `H^4<=N` holds for all
sufficiently large inputs. The stated finite preprocessing covers only the
finite exceptional prefix.

## Final scope

F147 V2 proves a bounded-anchor large-core reduction and a complete
standalone bridge decoder for one explicit frozen P128 source. It supplies
no all-input cycle, kernel, survival, density, or non-global-root theorem.
The strict necessary length statement now matches P131 exactly. The repaired
candidate is eligible for a fresh V2 statement-only blind reconstruction.
