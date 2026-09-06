# F206 hostile audit

## Verdict

**PASS.** I found no false asymptotic, wrong residue, conductor error,
incorrect character identity, or scope overclaim under the packet's stated
hypotheses. The semisimple fixed-projection obstruction is valid. The two
Mellin transforms and their tangent/cotangent reflection are exact. A fixed
basis and the stated diagonal finite rational repairs cannot constantize the
pure exponential pair. The natural Bessel/Whittaker normalization retains
the same two arithmetic coefficient sequences, and at every odd index its
dual coefficient is the public sign multiple of the original one.

There is one proof-presentation caveat, not a counterexample. Nonconstancy of
the displayed matrix `J(s)` alone would not exclude a second constant-matrix
identity satisfied by the particular vector of Mellin transforms. Section 4
below supplies the missing uniqueness attack directly from the packet's
exact zeta/beta products. It rules out such a second identity. A standalone
revision should include that short argument.

I did not edit a frozen input or a durable ledger. I ran no numerical or
symbolic mathematical computation and no experimental search. The checks
below are direct algebra from the frozen packet and the named upstream F203
proof. Hashing was used only for integrity verification.

## 1. Frozen-packet integrity

I computed all hashes before reading the packet. They agree exactly with
`MANIFEST.md`.

| file | SHA-256 | result |
|---|---|---|
| `STATEMENT.md` | `a35bfc475cb068bab78cb3f12bae605492ab22f4b208b6c809f7692f1cd4805c` | match |
| `PROOF.md` | `e617d242fe213e9ea5ec691493e7694c2550ab6a559a7eaf4eeee1f8aa2464cc` | match |
| `SELF_AUDIT.md` | `18e5587a679fff757973472a981216c4840d52f3426c2d3b8d327f968342d413` | match |
| `PROVENANCE.md` | `1fc45be8d749462991ae699313c38d1555c073767cfe1241d6071d79223b7429` | match |

The manifest itself has SHA-256
`7f34a712e2b3686c09550e8bfd4f16c589c9151ad97e386ee00e6e13ee60c538`.

## 2. Product and Lambert cusp data

Put `Q=e^(-4t)`. Solving the defining q-gamma identity for the two
q-Pochhammer factors gives

\[
 \frac{(Q^{1/4};Q)_\infty}{(Q^{3/4};Q)_\infty}
 =(1-Q)^{1/2}\frac{\Gamma_Q(3/4)}{\Gamma_Q(1/4)}.
\]

Thus the power is `+1/2`, and

\[
 P(e^{-t})\sim
 2\frac{\Gamma(3/4)}{\Gamma(1/4)}\sqrt t.
\]

Only odd indices contribute to `P`. Therefore

\[
 P(q)P(-q)
 =\prod_{a\text{ odd}}(1-q^{2a})^{\chi_4(a)}
 =P(q^2).
\]

The quotient of the two positive radial asymptotics gives
`P(-e^(-t)) -> sqrt(2)`. There is no sign or branch ambiguity.

For the Lambert series, the Mellin integrand is

\[
 \Gamma(s)\zeta(s)\beta(s-1)t^{-s}.
\]

The attacked residues are:

| point | relevant data | contribution |
|---|---|---|
| `s=1` | `Res zeta(1)=1`, `beta(0)=1/2` | `1/(2t)` |
| `s=0` | `beta(-1)=0` cancels `Gamma` | no constant term |
| `s=-1` | `Res Gamma=-1`, `zeta(-1)=-1/12`, `beta(-2)=-1/2` | `-t/24` |
| `s=-2` | both `zeta(-2)` and `beta(-3)` vanish | no `t^2` term |

The next possible residue is at `s=-3`, so absorbing it in the remainder is
consistent with `O(t^3)`.

Logarithmic differentiation of the binary product identity gives

\[
 L(q)+L(-q)=2L(q^2).
\]

Consequently,

\[
 2L(e^{-2t})-L(e^{-t})
 =-\frac t8+O(t^3).
\]

The negative sign is necessary. Substitution `t=2 pi y` then gives exactly
the three two-cusp rows in the statement:

\[
\begin{array}{c|cc}
 &0&1/2\\ \hline
P&y^{1/2}&y^0\\
R&y^{1/2}&y^{-1/2}\\
L&y^{-1}&y^1
\end{array}
\]

All six leading constants are nonzero.

## 3. Semisimple fixed-projection lemma

Let a scaling matrix for the finite cusp `r=a/c` be

\[
 \sigma=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]

The radial point has the exact preimage

\[
 \sigma^{-1}(r+iy)=-\frac dc+\frac{i}{c^2y},
 \qquad
 c\sigma^{-1}(r+iy)+d=\frac{i}{cy}.
\]

The real part is constant. Hence different local Puiseux exponents cannot
acquire a hidden polynomial cancellation along this radial path. After
semisimple diagonalization and application of the transported fixed
functional:

- a surviving negative exponent grows exponentially in `1/y`;
- a surviving positive exponent decays exponentially in `1/y`; and
- a surviving zero exponent is constant in the local coordinate, while
  undoing the slash contributes exactly a nonzero multiple of `y^(-k)`.

The finite principal part ensures that there is a first surviving negative
mode when one exists. Semisimplicity and the assumed ordinary Puiseux
expansion exclude powers of the local variable's logarithm. Cancellation by
the fixed projection can delete a whole mode, but it cannot create another
polynomial power.

Thus a nonzero nonexponential radial power must be `-k`. The two powers in
each displayed row are different, so no one fixed weight works for `P`, `R`,
or `L`.

This argument uses finite rational cusps. It does not use the cusp at
infinity. It also genuinely needs all of the stated restrictions:
semisimple parabolic monodromy, ordinary meromorphic Puiseux expansions,
finite principal parts, one common weight, and one fixed projection. The
packet correctly excludes logarithmic Jordan-block expansions and
nonholomorphic corrections that change the cusp powers.

## 4. Mellin products, reflection, and the constant-matrix attack

The divisor convolutions are in the correct order:

\[
 D_A(s)=\zeta(s)\beta(s-1),
 \qquad
 D_\vee(s)=\zeta(s-1)\beta(s).
\]

Termwise integration of `exp(-2 pi n y)` on a common right half-plane gives
the two displayed Mellin transforms. Meromorphic continuation then gives the
claimed identities globally.

For the primitive odd character modulo four,

\[
 \left(\frac4\pi\right)^{(u+1)/2}
 \Gamma\!\left(\frac{u+1}{2}\right)\beta(u)
 =
 \left(\frac4\pi\right)^{(2-u)/2}
 \Gamma\!\left(\frac{2-u}{2}\right)\beta(1-u).
\]

Using `u=s-1` together with the zeta functional equation gives

\[
 \frac{\mathcal M_A(s)}{\mathcal M_\vee(2-s)}
 =\frac{2^{3-2s}}\pi
 \Gamma\!\left(\frac{s+1}{2}\right)
 \Gamma\!\left(\frac{1-s}{2}\right)
 \sin\!\left(\frac{\pi s}{2}\right)
 =2^{3-2s}\tan\!\left(\frac{\pi s}{2}\right).
\]

Replacing `s` by `2-s` gives

\[
 \mathcal M_\vee(s)
 =-2^{1-2s}\cot\!\left(\frac{\pi s}{2}\right)
  \mathcal M_A(2-s).
\]

Multiplication of both components by `2^s` therefore produces exactly

\[
 J(s)=
 \begin{pmatrix}
 0&2\tan(\pi s/2)\\
 -\tfrac12\cot(\pi s/2)&0
 \end{pmatrix}.
\]

A fixed similarity cannot make this particular matrix constant. There is a
separate logical attack: could the same two functions satisfy some other
constant-matrix reflection?

Put

\[
 X(s)=2^s\binom{\mathcal M_A(s)}{\mathcal M_\vee(s)},
 \qquad
 r(s)=\frac{X_1(s)}{X_2(s)}
 =\frac{\zeta(s)\beta(s-1)}{\zeta(s-1)\beta(s)}.
\]

If `X(s)=C X(2-s)` for a constant matrix with first row `(a,b)`, comparison
with the first row of `J(s)` would force

\[
 a\,r(2-s)+b=2\tan(\pi s/2). \tag{1}
\]

At every positive even `s`, `r(2-s)=0` by the trivial-zero pattern, while
the tangent also vanishes. Hence (1) forces `b=0`. At `s=3`, `r(2-s)=r(-1)`
has a double pole: its denominator contains the two simple zeros
`zeta(-2)` and `beta(-1)`, while its numerator is nonzero. The tangent has
only a simple pole. No constant `a` can satisfy (1). Thus there is no
alternative constant matrix. A fixed change of basis would conjugate such a
constant matrix and cannot evade this contradiction.

This closes the only nontrivial uniqueness issue left implicit in the frozen
proof.

## 5. Exact finite-rational scope

For nonzero rational diagonal multipliers `u(s)` and `v(s)`, the first
off-diagonal reflection entry becomes

\[
 2\frac{u(s)}{v(2-s)}\tan(\pi s/2).
\]

The rational factor has only finitely many zeros and poles. It therefore
cannot cancel the infinitely many tangent zeros and poles. The cotangent
entry has the same obstruction. A subsequent fixed basis change cannot make
a nonconstant reflection matrix constant. Finite additive polar terms do not
alter this homogeneous infinite pole-zero pattern.

The conclusion is exactly as narrow as the statement and self-audit say. It
covers diagonal rational Mellin normalizations arising from finitely many
Euler derivatives or antiderivatives, together with finitely many polar
period terms. It is not a classification of arbitrary nondiagonal,
nonrational, infinite-depth, mock, quantum, or nonholomorphic repairs.

## 6. Whittaker/Bessel normalization and same-index circularity

The gamma quotient in the packet is correct. The existence and coefficient
scope can also be attacked explicitly. Define completed Dirichlet products

\[
 \Phi_A(s)=
 2^s\pi^{-s}\Gamma(s/2)^2\zeta(s)\beta(s-1)
\]

and

\[
 \Phi_\vee(s)=
 2^{s+1}\pi^{-s}
 \Gamma((s-1)/2)\Gamma((s+1)/2)
 \zeta(s-1)\beta(s).
\]

The separate completed zeta and beta equations give the constant swap

\[
 \Phi_A(s)=\Phi_\vee(2-s),
 \qquad
 \Phi_\vee(s)=\Phi_A(2-s).
\]

The standard Mellin formula for `K_nu` shows that the corresponding kernels
can be taken as

\[
 W_A(y)=4K_0(\pi y),
 \qquad
 W_\vee(y)=8K_1(\pi y).
\]

Therefore the normalized sums have the form

\[
 \sum_{n\ge1}A(n)W_A(ny),
 \qquad
 \sum_{n\ge1}A^\vee(n)W_\vee(ny).
\]

Only the archimedean kernels changed. No index or Dirichlet coefficient was
replaced.

For odd `n`, every divisor is odd and

\[
 \chi_4(n/d)=\chi_4(n)\chi_4(d),
\]

because `chi_4(d)^2=1`. Hence

\[
 A^\vee(n)
 =\chi_4(n)\sum_{d\mid n}d\chi_4(d)
 =\chi_4(n)A(n).
\]

This identity is false in general at even indices, and the packet correctly
does not assert it there. At every odd semiprime target, `chi_4(N)` is the
public sign determined by `N mod 4`. Extraction of the dual amplitude at the
same index is therefore equivalent to extraction of the original amplitude.

The named F203 source proves the semiprime factor extraction on its promise.
For the fixed `m=2` coefficient, the four residue cases also show directly
that the algebra works for every distinct odd semiprime: from `A(N)` one
gets either `p+q` or `|p-q|`, and then the two factors by an exact square
root. No balance assumption is used in this fixed-character calculation.

This audit validates the natural Mellin/Bessel pair. It does not promote a
claim that every possible nonholomorphic completion preserves these two
coefficient sequences. The frozen packet makes no such claim.

## 7. Algorithmic and open-case boundary

The reflection is a relation between complete kernel sums. Its displayed
dual term at index `N` is at the same index and contains the same hidden
amplitude up to a public sign. No smaller public integer or coefficient
recurrence appears in this construction.

The `Theta(N)` sentence concerns only a direct dense truncation through
`q^N`. Such a representation has `Theta(N)` positions, which is exponential
in the binary input length. It is not a coefficient-complexity lower bound.

The candidate correctly leaves open nonsemisimple logarithmic cusp data,
additional arithmetic shadows, nonpolynomial quantum cocycles, growing
state dimension, nonlinear identities, and adaptive integer-specific
decoders. It also does not claim a lower bound against sparse or implicit
coefficient extraction.

## Hostile attacks that did not refute the candidate

I checked:

- the q-gamma power and every nonzero radial constant;
- the binary product and Lambert signs;
- the residues at `s=1,0,-1,-2` and the first omitted order;
- fixed-projection cancellations after exact cusp transport;
- the need for semisimple monodromy and a finite principal part;
- both Dirichlet convolution orders;
- the conductor-four beta equation and every power of two;
- the tangent/cotangent matrix and its reflected sign;
- the possibility of a second, hidden constant matrix;
- fixed basis changes and the stated finite diagonal rational repairs;
- an explicit Bessel realization of the archimedean repair;
- the odd-index identity and its even-index exclusion;
- the inherited semiprime factor extraction; and
- the distinction between dense truncation cost and a general lower bound.
