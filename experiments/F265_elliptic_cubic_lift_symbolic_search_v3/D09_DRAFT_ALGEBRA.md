# F265-D09 draft algebra — one-round peeled mixed elliptic cubic-row kernel

## Status and authenticated boundary

This is an unfrozen theory-only draft. It has no source, runner, manifest,
freeze, compilation, preflight, local execution, remote execution, discovery
result, or heldout result. A hostile theory pass would authorize only source
drafting.

D09 is standalone. The files below are authenticated provenance and theorem
imports; no predecessor version name is rebound and no implicit composition
rule survives.

| Imported artifact | SHA-256 |
|---|---|
| `D05_DRAFT_ALGEBRA.md` | `e3cbefeb597f263501d327f15f9dd4c7b78ee37d37178135ab1c0a5ff73e9fd3` |
| `D05_DRAFT_PREREGISTRATION.md` | `a62dcb0f7d501778ef1f6092468d38a6ee15c794ec5b609bf145a3d7bf345a35` |
| `D06_DRAFT_ALGEBRA.md` | `e79ea109a9cd8141dd27c4fc99cc7ec2957c454619b0e015802ab4eff5c45f74` |
| `D06_DRAFT_PREREGISTRATION.md` | `67aa6011accffedbed24d0be95614e481f006b80f163a6b5e831dc4fafef6754` |
| `D07_DRAFT_ALGEBRA.md` | `fbc4831cb4f11f849a779bf165cbedf2e6a3e8140228ba40b0d01ec103a2abbf` |
| `D07_DRAFT_PREREGISTRATION.md` | `2151d3549be3322de14d6e787f87a210bb6c0721c9fedfcc8397457a7d0c4fc1` |
| `D08_DRAFT_ALGEBRA.md` | `3af4a847ab65f9acde05ffd2ea98f4d5cee143c0162f915284b599e8fe007839` |
| `D08_DRAFT_PREREGISTRATION.md` | `11e5a77f2c61c1f936bec775f86d0083e3fa05c2e0cf8c1420df9920a7f34b58` |
| D02 `FROZEN.sha256` | `26f7940244242edc549a2612fc08120372e0f8fab64a2dca154b69ed02d55d6a` |
| D02 `ALGEBRA.md` | `d20b5271bb4441fe7d280e35e09a73ff5b0142abf2ed6d3e9839fe22ff4914c4` |
| D02 `PREREGISTRATION.md` | `8e3c90420014939ba3ae58490bac2e85fc0a7a45523e12d332cadb5e1f6b384f` |
| D02 `search.cpp` | `eeceba4db014346cc78dae3cbae29a65fb32946163becc5d9f5617fc465a7957` |
| D02 `HOSTILE_PRERUN_AUDIT.md` | `ac991ea84c453531262d0982774027190d592eb5042202d145c1c91e98ea9199` |
| F271 V1 `STATEMENT.md` | `19b288038c4f9e339d3f56e51fb1c6d7277fd9e322e486f2339edd0c68bf64ba` |
| F271 V1 `PROOF.md` | `f65e65cd649d3e787fc452abf270142e9c790d424328c52b6e3d678fc7e77b24` |
| F271 V2 `V2_FROZEN.sha256` | `5e396f4e20f54ee37ed70b19ed85a82e483247b10423a7ce58e7081e961c7a15` |
| F271 V2 `V2_MANIFEST.md` | `4057129cdb495656a63c7aa792253edf8c9fd93c476e7309b9787685813c0584` |
| F271 V2 `V2_STATEMENT.md` | `29fd1a79e569c2e4da72d3489e7385de4123e6b299241bfe46defb421c84b82c` |
| F271 V2 `V2_PROOF.md` | `5371d049eecb2451f073edb96d5bf36f99ab7be662fb48c5d8de2b2d93f10b51` |
| F271 V2 `V2_SELF_AUDIT.md` | `3eea92643a38ad3a4893ac9f181a31feba258da82782c53ee61aecdc939e1539` |
| F271 V2 `V2_HOSTILE_AUDIT.md` | `5827e5a5a80a052b486259a7994b69f00c18b0a3e07a91fc0038dd1e08f9acec` |
| F271 V2 `V2_BLIND_RECONSTRUCTION.md` | `21c8784eb36fb477cad4944df7216c6897151ab1fa4608a6c9dbb3f2f90c78f1` |
| F271 `sanity_check.cpp` | `70bb7398fe927c270f30f3961d72f8af408e845e784b06b3da113d94466a2c19` |

The normative D09 mathematics is only the materialized text below. D09
imports the proved F271 V2 decoder theorem exactly. It does not import the
D08 fixed-round gcd method, the D05 repeated peel, the D05 all-pair controls,
or any predecessor runtime formula.

## 1. Public mixed bank

Let `N>=3` be odd and put

\[
 n=\lceil\log_2(N+1)\rceil=\operatorname{bitlen}(N),
 \qquad K=\min(2n,160).
\]

A bank contains exactly two attempted short-Weierstrass curve streams in
this order:

1. curve zero uses mode `U`;
2. curve one uses mode `POWER`.

For `U`, choose `A` in `{1,...,N-1}` and `x_0,y_0` in `{0,...,N-1}`.
For `POWER`, choose `s` in `{1,...,N-1}` and set

\[
 x_0=s^2\bmod N,
 \qquad y_0=s^3\bmod N,
 \qquad A=s+1\bmod N.
\]

In both modes set

\[
 B=y_0^2-x_0^3-Ax_0\bmod N,
 \qquad 0\le B<N.
\]

Put `delta=4A^3+27B^2` as a nonnegative integer; do not first reduce it
modulo `N`. The exact deterministic draws, attempt rules, and disjoint
stream keys are fixed in the preregistration. For every proposal, first
compute `d=gcd(delta,N)`. If `1<d<N`, journal `d` as a sticky terminal
generation factor and stop the bank. If `d=N`, reject the degenerate
proposal and consume its attempt. Only when `d=1` test `B=0`; if so, reject
the inadmissible proposal and consume its attempt. Curve one then also
rejects a clean tuple `(A,B,x_0,y_0)` equal to the accepted curve-zero
tuple. This is the sole duplicate rule and is local to one bank. The first
proposal that passes these ordered proposal screens is accepted
irrevocably. A later orbit exception skips or stops the bank; it does not
reopen the proposal loop.

For an accepted proposal, use

\[
 E_N:y^2=x^3+Ax+B\pmod N.
\]

The exact factor-first addition of affine operands `P=(x_1,y_1)` and
`Q=(x_2,y_2)` is as follows. All input and returned coordinates are the
canonical residues in `[0,N)`.

1. If `x_1=x_2` and `y_1+y_2=0 mod N`, return the global point at infinity.
2. If `x_1=x_2` but `y_1!=y_2` as canonical integers, compute
   `gcd(y_1-y_2,N)` and then, only if needed, `gcd(y_1+y_2,N)`. Return the
   first proper gcd. If neither is proper, return an unresolved global
   equal-`x` exception.
3. If the canonical points are equal, use numerator `3x_1^2+A` and
   denominator `2y_1`. Otherwise use numerator `y_2-y_1` and denominator
   `x_2-x_1`.
4. Reduce the denominator modulo `N` and compute its gcd with `N`. A proper
   gcd is a factor. A full gcd returns global infinity only for doubling
   with `y_1=0 mod N`; every other full gcd is an unresolved global
   denominator exception. For a unit gcd, invert the denominator and use
   the standard affine formulas modulo `N`.

The orbit starts at the base and repeatedly adds the base, so row `k` is
the returned affine point `kP`. A proper gcd stops the bank. A global point
at infinity or unresolved global exception before scalar `K` makes the bank
incomplete. No partial orbit enters the peel.

For every scalar `k=1,...,K`, the complete affine point is represented
canonically as

\[
 P_k=(u_k,v_k),\qquad0\le u_k,v_k<N.
\]

Before admitting it, compute `gcd(v_k,N)`. A proper gcd is a factor and stops
the bank. A full gcd makes the bank incomplete. Define the positive integer

\[
 a_k=u_k^3+A u_k+B.
\]

Then

\[
 a_k\equiv v_k^2\pmod N,
 \qquad \gcd(v_k,N)=1.
\]

Store the exact signed carry

\[
 c_k=(a_k-v_k^2)/N.
\]

It is an integer fixed by the public row and is used only for validation and
symbolic diagnostics; it is not a decoder input.

The two curves contribute all their scalar indices. Original row order is
curve zero in increasing scalar order, then curve one in increasing scalar
order. Thus the bank has `m=2K<=320` rows. In the registered corpus
`N<2^120`, so

\[
 0<a_k<2N^3<2^{361}.
\]

Every source implementation must check this 361-bit boundary.

## 2. Exactly one saturated peel round

Let the complete mixed bank be indexed by `S={1,...,m}`. Form the full
product

\[
 P=\prod_{j\in S}a_j.
\]

For each row, using the same original set `S`, put

\[
 P_i=P/a_i,
 \qquad L_i=\operatorname{bitlen}(a_i),
\]

\[
 r_i=P_i^{L_i}\bmod a_i,
 \qquad g_i=\gcd(a_i,r_i),
 \qquad b_i=a_i/g_i.
\]

The large power is computed modulo `a_i`. It is not materialized. Delete
simultaneously exactly the rows for which `b_i` is not an integer square.
There is no second peel round in D09.

### One-round theorem

For a rational prime `ell`, write

\[
 e_i=v_\ell(a_i),
 \qquad E_i=\sum_{j\ne i}v_\ell(a_j).
\]

Reduction modulo `a_i` does not change the gcd, so

\[
 v_\ell(g_i)=\min(e_i,L_iE_i).
\]

If `E_i=0`, this is zero. If `E_i>0`, then

\[
 e_i\le\lfloor\log_2a_i\rfloor<L_i\le L_iE_i,
\]

and the value is `e_i`. Hence

\[
 b_i=\prod_{\ell:\,\ell\nmid P_i}\ell^{v_\ell(a_i)}.
\]

If `b_i` is nonsquare, a rational prime absent from every other row occurs
to odd exponent in `a_i`. Every square-product relation therefore has zero
in coordinate `i`. All deletions are certified against the same original
set, so simultaneous restriction gives a linear isomorphism

\[
 \boxed{\mathcal K(S)\simeq\mathcal K(S_1)},
\]

where `S_1` is the one-round survivor set and

\[
 \mathcal K(T)=\left\{c\in\mathbf F_2^T:
             \prod_{i\in T}a_i^{c_i}\text{ is an integer square}\right\}.
\]

The inverse inserts zeros at deleted coordinates. Exact positive roots,
supplied modular roots, and normalized roots are unchanged. Thus one round
is complete for D09's purpose: if at most 64 rows survive, a complete
decoder on those rows recovers the complete original-bank kernel. Repeating
the peel could reduce work further, but is not required for correctness and
is not part of this experiment.

## 3. F271 V2 on the residual core

If more than 64 rows survive, the bank is visibly
`RESOURCE_REJECT_RESIDUAL_CORE`. It contributes neither a null nor a
completed-kernel claim.

Otherwise run the exact F271 V2 incremental batch gcd-free decoder on the
surviving rows and their canonical supplied residues `0<=v_i<N`. This
includes:

- the F271 saturation primitive;
- `SAME_SUPPORT` and `TWO_BASE` with carried leaf gcds;
- the fixed 2,048-leaf dynamic product tree and left-first descent;
- exact exponent-vector propagation;
- exact row reconstruction;
- terminal product/remainder-tree coprimality verification, including the
  V2 `S=0` and `S=1` cases;
- the nonsquare-block parity matrix;
- canonical nullspace, low-basis, and structural-complement construction;
- exact relation roots and both normalized-root signed gcds.

No rational-prime factorization is used. The implementation may use a faster
integer library, but it may not replace any F271 arithmetic or verification
step by an oracle.

For `m_1<=64` surviving rows of at most 361 bits, F271 proves

\[
 V\le23{,}040,
 \quad T\le3{,}591,
 \quad S\le1{,}875,
 \quad D=11,
\]

and at most

\[
 (D+1)T+m_1+2V+S
 \le 12\cdot3{,}591+64+2\cdot23{,}040+1{,}875
 =\boxed{91{,}111}
\]

scalar gcd calls in refinement plus terminal coprimality verification.
Relation classification separately uses at most 64 modular inversions and
128 signed gcds.

## 4. Complete low-support and quotient classification

Let `sigma_i` be the column of row `i` in the F271 nonsquare-block parity
matrix. The singleton count is exactly the size of the zero-signature class
`Z`. The support-two count is exactly

\[
 \binom{|Z|}{2}+
 \sum_{C\ne Z}\binom{|C|}{2},
\]

where `C` runs over nonzero equal-signature classes.

A canonical basis of the complete support-at-most-two span is

\[
 \{e_i:i\in Z\}
 \cup
 \{e_{r_C}+e_i:C\ne Z,\ i\in C\setminus\{r_C\}\},
\]

with `r_C` the least original row in class `C`. This computes exact counts
and the complete span without a row-pair gcd, division, square test, or
serialized pair list.

Call the canonical low basis `L`. Reduce the canonical full-kernel basis
against `L` and earlier complement pivots to obtain `Q`, with

\[
 \mathcal K(S_1)=L\oplus\operatorname{span}(Q).
\]

For a kernel vector `c`, F271 computes its exact positive root `R(c)`, its
supplied modular root

\[
 X(c)=\prod_i v_i^{c_i}\pmod N,
\]

and

\[
 \rho(c)=R(c)X(c)^{-1}\pmod N.
\]

The map `rho` is a homomorphism. A non-global value yields a proper factor
through `gcd(rho(c)-1,N)` and `gcd(rho(c)+1,N)`.

Every vector in `L` and `Q` is classified, even after an earlier relation
factor. If every vector of `L` is global, the quotient map modulo the global
root subgroup is defined and `Q` is its canonical complement basis. A
non-global vector in `Q` is a **decoder-strict structural hit** only when no
generation-stage factor occurred and every low-basis image is global.

If a low-basis image is non-global, record the factor and set
`quotient_defined=false`. The same canonical `Q` is still computed and its
vectors are classified as `STRUCTURAL_ONLY_LOW_IMAGE`; they cannot count as
decoder-strict structural hits.

This definition deliberately makes no claim about omitted all-bank
coordinate-pair screens. It is strict relative to generation safety and the
complete low-support image, not relative to an unexecuted quadratic control
menu.

## 5. Explicitly removed quadratic work

D09 does not execute any of the following over every unordered row pair:

- `gcd(u_i-u_j,N)`;
- `gcd(v_i-v_j,N)` or `gcd(v_i+v_j,N)`;
- `gcd(u_i^2+u_i u_j+u_j^2+A,N)`;
- `gcd(a_i,a_j)` followed by quotient square tests; or
- one detailed record per support-two hit.

None is needed to generate a valid congruence of squares or to classify the
complete low span and structural complement. Reintroducing any full-bank
pair loop is a new experiment version.

## 6. Post-commit relation-local diagnostics

Diagnostics run only after the arithmetic result and heldout label inputs
have been committed. They cannot change a row, peel decision, decoder state,
basis, normalized root, eligibility bit, factor event, or label.

Select the first eight canonical vectors of `Q` whose support is at most 16.
For every same-curve unordered pair in one selected support, cache

\[
 H_{ij}=u_i^2+u_i u_j+u_j^2+A,
\]

\[
 d_{ij,\rm tan}=\gcd(a_i,a_j,u_i-u_j),
\]

\[
 d_{ij,\rm chord}=\gcd(a_i,a_j,H_{ij}),
 \qquad
 d_{ij,\rm disc}=\gcd(a_i,a_j,4A^3+27B^2).
\]

The three-argument gcd means a left fold. Compute `h_ij=gcd(a_i,a_j)` once,
then compute each displayed value as one gcd against `h_ij`. Thus one pair
task uses exactly four scalar gcd calls.

For every same-curve unordered triple, evaluate all three pair anchors. For
an anchor `(i,j;k)` with `alpha<=beta` the two anchor scalar indices and
`gamma` the third, test

`alpha+beta=gamma`, `beta-alpha=gamma`, `2*alpha=beta`,
`3*alpha=beta`, `alpha*beta=gamma`, and
`v2(alpha)=v2(beta)`.

When `d_chord>1`, also test

\[
 u_i+u_j+u_k\equiv0\pmod {d_{ij,\rm chord}}.
\]

There are no cross-curve chord anchors. Cross-curve support counts and the
complete original-row mask remain in the basis record for later symbolic
analysis.

The maxima are 960 cached pair tasks and 13,440 anchored-third tasks per
bank. Truncating retained diagnostic details does not truncate the complete
counter or stream digest.

## 7. Exact scope

D09 is a finite source experiment. The one-round theorem and F271 V2 make
its completed kernel and root classification exact. They do not prove that
one mixed bank has at most 64 survivors, that its kernel is nonzero, that a
non-global root exists, or that any finite frequency persists.

The source is live because union can destroy private support. The source is
not proved successful. A positive certificate factors only its displayed
modulus. A finite null closes only the fixed mixed source, imported corpus,
and resource coverage rules in the preregistration. No all-input factoring
or asymptotic success claim follows.
