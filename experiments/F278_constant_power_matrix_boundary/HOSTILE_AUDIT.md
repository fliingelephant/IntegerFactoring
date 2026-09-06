# F278 fresh hostile audit — PASS WITH SCOPE QUALIFICATIONS

## Frozen authentication

I authenticated the packet before reading any theorem, proof, self-audit,
provenance claim, or manifest claim. The required and observed SHA-256 of
`FROZEN.sha256` is

`cfeb683b75c36129da0623a0a4172fb7c1b23dd50f6c3af5e8176af1591045a8`.

All five frozen entries match:

| Artifact | SHA-256 |
|---|---|
| `STATEMENT.md` | `4232a1007700802b25acafed944f7b5adc227a913af26aec8ab6b17a7bdba0fa` |
| `PROOF.md` | `194461e35d35a82ccea95df3c99ffb76cc414af5852c5fff7c917409a9403073` |
| `SELF_AUDIT.md` | `e38766d07d42cbf7ee60ae3a1762f7e86362c220420bec5026f4ed1a4bc41829` |
| `PROVENANCE.md` | `1e1938fb9c49c45e1fdb496f4cef75479c45be7ec2a938e3214e42a6001c3cea` |
| `MANIFEST.md` | `9e475d6892725119aeeceebd7ce2d34233b543c9167483662420f8470494416e` |

I did not modify a frozen file or a durable ledger.

## Verdict

**PASS as a narrow theorem packet, with the scope qualifications below.**
The explicit-power cost, every boxed Jordan equivalence, the semisimple
collision equivalence, the clean quadratic companion law, and the
Cayley--Hamilton recurrence reduction are correct under their stated
hypotheses. I found no bad endpoint, invalid modular division, missing
split type, or false all-input factor claim.

Four interpretation limits are mandatory:

1. The Jordan result is exact for the displayed Jordan coefficients and
   their falling products. It is not a classification of every function of
   the powered block. Entrywise gcd behavior is also not invariant under an
   arbitrary change of basis. A unit conjugator must be public if the
   algorithm is to conjugate back and expose the displayed coefficients.
2. The collision theorem and the clean companion coordinate do not classify
   every two-mode coordinate. Additive cancellation outside the named
   mechanisms already occurs in dimension two. Thus `d>=3` is an explicitly
   open class, not the first dimension in which an unclassified coordinate
   can occur.
3. The Frobenius section proves nonconstruction and lack of an automatic
   implication. It does not prove that an ordinary matrix power can never
   coincide with a local Frobenius operator. The exact nonclaims preserve
   this distinction.
4. The no-search text is a packet disposition, not a theorem. The exact
   reductions make an undirected search inside the three named mechanisms
   unnecessary. They do not show that a targeted finite exploration cannot
   discover a law, candidate, or counterexample in an open coordinate or
   semilinear lane. An all-input law is required for a proof, not logically
   required before exploratory computation.

If the phrases "exactly a direct scan," "does not supply Frobenius," or
"requires" an exact signal before search are read without these scopes, the
packet overreaches its proofs. The exact nonclaims and the repeated
named-mechanism restrictions support the narrow reading used for this pass.

## 1. Balanced range and explicit endpoint

From `p<q`,

\[
 p<\sqrt{pq}<q.
\]

Taking the floor gives `p<=B<q`. The balance condition gives `B<2p`, so
there is a unique `s` with

\[
 B=p+s,\qquad 0\le s<p.
\]

The larger prime cannot divide `B`. In `[p,2p)`, the only multiple of `p`
is `p`. Therefore

\[
 \gcd(B,N)=p\iff B=p\iff s=0.
\]

On the unresolved branch, `s>=1` and `B` is a unit in both local fields.
These conclusions include the floor endpoint `B=p`.

Let `n=ceil(log_2 N)`. Binary powering uses `O(log B)=O(n)` matrix
products. Naive multiplication costs `O(d^3)` ring operations. A modular
ring operation has polynomial bit cost in `n`. Hence the total cost is

\[
 T_{\rm construct}+O(d^3n)\operatorname{poly}(n)
 =\exp((\log n)^{O(1)}).
\]

A constant number of explicit matrices uses `O(d^2n)` bits. The output
itself has this order of size. Thus both time and space are numerical
quasipolynomial. This is only an evaluation result. No factor observable
follows from the cost calculation.

For a numerical-quasipolynomial dimension, `d<p` holds eventually because
`p` is exponential in `n` on balanced semiprimes, while
`d=exp(poly(log n))`. The Jordan theorem correctly states `d<p` as an input
hypothesis instead of using this asymptotic fact on exceptional inputs.

## 2. Jordan coefficients, direct products, and local rank

Since `J_h^h=0` and `J_h` commutes with the scalar matrix,

\[
 (\alpha I+J_h)^B
 =\sum_{j=0}^{h-1}\binom Bj\alpha^{B-j}J_h^j.
\]

Fix `1<=j<h`. The hypotheses imply `j<p`. The base-`p` digits of `B` are
`(1,s)`, while those of `j` are `(0,j)`. Lucas gives

\[
 \binom Bj\equiv\binom10\binom sj=\binom sj\pmod p.
\]

For `j<=s`, this is nonzero because `s<p`. For `j>s`, it is zero. At the
larger prime, `j<=B<q`, so every factor in the numerator and denominator of
the factorial formula is nonzero modulo `q`. Thus

\[
 \gcd\!\left(\binom Bj\alpha^{B-j},N\right)
 =\begin{cases}1,&j\le s,\\p,&j>s.\end{cases}
\]

The unit hypothesis on `alpha` is essential here.

The factors of

\[
 D_j=B(B-1)\cdots(B-j+1)
\]

form an interval below `q` of length `j<p`. It contains `p` exactly when
`B-j+1<=p`, or equivalently `j>s`. It contains no multiple of `q` and no
second multiple of `p`. This independently gives the same two gcd values.
Equivalently, `j!` is a unit modulo `N`, so the falling product and binomial
coefficient have the same local divisibility.

There is some successful `j` in `1,...,h-1` exactly when `s<h-1`. The union
of the tested numerator intervals is precisely the direct scan

\[
 B,B-1,\ldots,B-h+2.
\]

The empty endpoint `h=1`, the one-entry endpoint `h=2`, and the already
factored endpoint `s=0` all agree with the formula.

After the boundary gcd screen, fix either local characteristic `r`. For a
nonzero eigenvalue,

\[
 (\alpha I+J)^B-\alpha^BI
 =JQ(J),\qquad Q(0)=B\alpha^{B-1}\ne0\pmod r.
\]

Therefore `Q(J)` is invertible and commutes with `J`. For every `k`,

\[
 \ker((JQ(J))^k)=\ker(J^k).
\]

The complete nilpotent Jordan type is preserved. This remains true for each
individual block even if two distinct eigenvalues acquire the same powered
eigenvalue; a collision merges eigenvalue labels but does not merge Jordan
blocks. For eigenvalue zero, `J_h^B=0` because `h<=B`.

If a zero eigenvalue exists at only one hidden prime, `det(C)` already has a
proper gcd with `N`. Thus killing a zero block is not a new clean powered
signal. If it exists in both local components, both blocks are killed.

The coefficient gcd conclusion lives in a Jordan basis. If
`C=P(\alpha I+J)P^{-1}`, a public unit `P` lets one compute
`P^{-1}C^BP` and recover the coefficients. Without that operation,
conjugation can mix the scalar and nilpotent coefficients, and individual
entries of `C^B` need not have the displayed gcds. The packet's warning
about a hidden local basis is therefore substantive.

## 3. Semisimple collisions and an omitted two-mode lane

Over an algebraic closure of `F_r`, semisimplicity gives a diagonal form.
Invertibility makes every eigenvalue nonzero. Hence

\[
 \alpha_i^B=\alpha_j^B
 \iff (\alpha_i/\alpha_j)^B=1.
\]

If `chi_C` is separable, all its roots are distinct before powering. The
discriminant of `chi_(C^B)` is then zero exactly when at least one pair has
collided. This proves the ratio-torsion characterization. The assumptions
on `det(C)` and `Disc(chi_C)` also correctly separate proper input gcds from
the clean powered branch.

This argument classifies collision and the displayed discriminant. It does
not classify an arbitrary coordinate of `C^B`. In particular, the open
coordinate lane is not confined to three or more modes.

Also, `C^B` itself cannot lose rank under Theorem C because `C` is
invertible. The statement's phrase "rank losses caused by those collisions"
is safe only for an auxiliary collision-sensitive matrix, such as a
Vandermonde-type construction, whose rank criterion has separately been
proved equivalent to repeated powered eigenvalues. F278 defines no general
rank observable and proves no broader rank-loss theorem.

An explicit hostile example is

\[
 N=187=11\cdot17,\qquad B=13,
\]

and

\[
 C=\begin{pmatrix}99&98\\98&99\end{pmatrix}
 =P\begin{pmatrix}10&0\\0&1\end{pmatrix}P^{-1}
 \pmod {187},
 \qquad
 P=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]

Here `det(P)=-2` is a unit. Direct powering gives

\[
 C^{13}=\begin{pmatrix}176&175\\175&176\end{pmatrix}\pmod {187},
 \qquad \gcd(176,187)=11.
\]

The input determinant is `10`, and its characteristic discriminant is
`81`; both are units modulo `187`. Modulo `11`, the powered eigenvalues are
`10` and `1`, so they do not collide. The diagonal entry vanishes because
it is `(10^13+1)/2`, a two-mode additive cancellation. Modulo `17`, it is
nonzero.

This is not a counterexample to Theorem C, which is explicitly about
collisions, or to Theorem D, which selects the companion lower-left
coordinate. It is a counterexample to any stronger reading that those two
theorems exhaust dimension two. A general two-mode coordinate has a law of
the form

\[
 a\alpha^B+b\beta^B=0
 \iff (\alpha/\beta)^B=-b/a
\]

when the displayed quantities are units. The target need not be one, so
this is not the ratio-torsion event proved in Theorem C.

## 4. Clean quadratic companion

Cayley--Hamilton gives `C^2=tC-delta I`. The recurrence then proves by
induction that

\[
 C^k=U_kC-\delta U_{k-1}I,
 \qquad (C^k)_{2,1}=U_k.
\]

For a hidden prime `r`, the condition `r` not dividing `delta Delta` makes
the two roots `alpha,beta` distinct and nonzero in the quadratic etale
algebra. Since `(alpha-beta)^2=Delta` is a unit,

\[
 U_B=\frac{\alpha^B-\beta^B}{\alpha-\beta},
 \qquad
 U_B=0\iff z_r^B=1,
 \quad z_r=\alpha/\beta.
\]

If the polynomial splits, `z_r` is in `F_r^*` and has order dividing
`r-1`. If it is irreducible, Frobenius exchanges the roots, so

\[
 z_r^r=z_r^{-1},\qquad z_r^{r+1}=1.
\]

These are the two quadratic etale types. No third clean local type is
missing.

At the smaller prime, `B=p+s`. Therefore

\[
 z_p^B=z_p^{s+1}\quad\hbox{in the split case},
 \qquad
 z_p^B=z_p^{s-1}\quad\hbox{in the irreducible case}.
\]

The exponent `s-1` is valid at both endpoints. For `s=0`, it is a negative
unit exponent and the preliminary gcd has already factored `N`. For `s=1`,
it is zero, so every clean irreducible local ratio satisfies the `p`-side
condition. A proper factor still requires failure of the `q`-side condition.

Because `N` is squarefree,

\[
 \gcd(U_B,N)=p
\]

holds exactly when the applicable `p`-side residual is one and
`z_q^B` is not one. The packet correctly makes no claim that these two local
events separate on every input.

## 5. Recurrence equivalence

Cayley--Hamilton is valid over the commutative ring `Z/NZ`. Multiplying the
characteristic identity by `C_N^k` gives the stated matrix recurrence, and
each entry inherits it. Dependence of the coefficients on `N` does not
change their constancy in the exponent index for that fixed input.

Conversely, an order-`d` homogeneous recurrence advances its `d`-term state
by a fixed companion matrix. The exact endpoint is `e_i^T A^k v`, so the
public initial state `v` and output coordinate are part of the recurrence
description. If "a coordinate of a matrix power" is intended to mean a
literal entry rather than a matrix-vector coordinate, one can use the
`(d+1)`-dimensional block matrix

\[
 \begin{pmatrix}A&v\\0&0\end{pmatrix};
\]

its upper-right block in the `k`-th power is `A^(k-1)v` for `k>=1`. This
constant dimension increment does not change the numerical-quasipolynomial
endpoint. It does show that the proof's `d by d` companion statement should
be read as state representation, not as a claim that every initialized
sequence is one literal entry of `A^k`.

Nothing here is a recurrence lower bound. Arbitrary public coefficient or
initial-state functions of `N` remain outside such a conclusion.

## 6. Frobenius and additive-cancellation boundary

For a diagonalizable matrix in characteristic `r`, spectral mapping says
that `C^r` has eigenvalues `alpha_i^r`. This concerns the power of one
linear operator. The Frobenius of an algebra is the map that sends every
algebra element `x` to `x^r`. The spectral identity alone does not construct
one public CRT-glued matrix whose two reductions implement those two local
maps.

At the smaller prime,

\[
 C^B=C^{p+s}=C^pC^s.
\]

There is no general cancellation of `C^s`. The named semisimple and clean
quadratic observables reduce it to the exact residual conditions proved
above. The identity also does not force a sum of powered eigenmodes to
vanish. Thus the exclusion is valid as a statement of what F278 has not
constructed.

It is not an impossibility theorem. Special ordinary powers can equal a
Frobenius operator. For example, again take `N=187` and `B=13`, and consider

\[
 A=(\mathbb Z/187\mathbb Z)[x]/(x^2-6).
\]

The residue `6` is a nonsquare modulo both `11` and `17`. In the basis
`(1,x)`, the Frobenius in either local quadratic field is

\[
 F_r=\operatorname{diag}(1,-1),
\]

because `x^r=-x`. The public matrix `F=diag(1,-1)` satisfies `F^B=F`
because `B` is odd. Thus an ordinary power can coincide with both local
Frobenius maps in a special, non-factor-distinguishing case. This does not
supply the characteristic-dependent interface sought by the packet, but it
rules out an absolute reading of "ordinary powering does not supply
Frobenius."

Likewise, the displayed `m>=3` sums are genuinely unclassified, but the
dimension-two example in Section 3 shows that arbitrary additive
cancellation is not classified below that threshold either. The exact
nonclaims correctly rule out a general semilinear impossibility theorem and
a general higher-dimensional cancellation theorem.

## 7. Hostile finite checks and search disposition

The proofs above do not rely on computation. As a bounded counterexample
check, I separately enumerated all balanced odd-prime pairs with both primes
at most `199`, all admissible `h`, and all `1<=j<h`. All `2,277,181` Jordan
coefficient and falling-product gcd comparisons matched (11).

A second bounded check enumerated the quadratic local cases generated by
balanced pairs with smaller prime at most `43` and larger prime at most
`83`. It checked `202,408` admissible `(r,t,delta)` cases, including split
and irreducible quadratic algebras. Every root-ratio equivalence, torus law,
and smaller-prime residual exponent matched. These checks took seconds,
used negligible memory, created no artifact, and are corroboration only.

The exact reductions justify ending searches whose sole question is whether
the displayed Jordan coefficients, semisimple collisions, or companion
`U_B` coordinate are new signal types. They do not justify the stronger
claim that finite exploration can only rank coincidences. A targeted search
could still do at least three legitimate jobs:

1. falsify a proposed all-input law in the open two-mode or `m>=3` lane;
2. discover a candidate coefficient construction before its proof exists;
3. test when an ordinary power accidentally realizes a useful semilinear
   action.

Finite samples cannot replace an all-input theorem. The converse does not
follow: an all-input theorem need not exist before samples can guide its
discovery. Therefore the packet's no-search language is valid only as its
chosen resource disposition for the three closed named mechanisms.

## 8. Final scope checklist

The following boundaries are all necessary and were respected by the exact
proofs:

- `N=pq` has distinct odd primes with `p<q<2p` for the signal laws.
- The Jordan argument uses `1<=h<=d<=B`, `d<p`, and unit `alpha`.
- Jordan-type preservation is on the post-screen branch where neither local
  characteristic divides `B`.
- The semisimple collision law uses nonzero eigenvalues. The discriminant
  specialization also uses separability of the input characteristic
  polynomial.
- The quadratic law uses `gcd(delta Delta,N)=1` and the selected
  lower-left companion coordinate.
- The evaluator theorem uses an explicit numerical-quasipolynomial matrix,
  not an implicit exponentially large state.
- The recurrence converse includes a public initial state and output.
- No result classifies arbitrary coordinates, arbitrary `N`-dependent
  cancellations, semilinear or adaptive algorithms, or general factoring.

Subject to the four interpretation limits in the verdict, F278 is a correct
proof-only boundary for its named mechanisms. It is not a complete
constant-power classification and does not mathematically close the open
search lanes.
