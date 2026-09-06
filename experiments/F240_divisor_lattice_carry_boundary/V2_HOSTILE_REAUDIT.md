# F240 V2 hostile re-audit

## Verdict

**PASS at the stated proof-only scope.**

V2 applies the exact repair required by the preserved V1 hostile audit.  The
decoder rejects every tuple with `(a,b)=(0,0)`.  Every true tuple that passes
this gate has `b>0`, so its recovery equation is a genuine quadratic that
contains the factor `p`.  The repair covers all two-zero-center tuples, not
only the witness at `B=N-1,u=1`.

I found no new mathematical defect.  The carry identities, the `d=2`
round-half-up offset, the residual-window direction, the multiplicative
support optimum, and the additive-selector scope all reconstruct correctly.

I did not edit a frozen input or a durable ledger.  I used no numerical
search, mathematical experiment, or external source.  I wrote only this
re-audit.

## 1. Frozen-input integrity

I recomputed all five supplied V2 digests before reading any V2 content.
Every digest matched.  I then obtained the preserved V1 hostile-audit digest
from the authenticated V2 manifest and provenance, verified that digest, and
only then read the V1 hostile audit.

| Artifact | Expected and observed SHA-256 | Result |
|---|---|---|
| `V2_STATEMENT.md` | `d74ea1c31f24a59b643dc38d69326be553bc3944ef80cee4f72a7a2e607e9914` | match |
| `V2_PROOF.md` | `1a4bb957465f2bceb0ce3166df5f1c56d7ece68af36a4a5f9cafa426aa3dd758` | match |
| `V2_SELF_AUDIT.md` | `010610012643682a422e61eb37d3bc7c9230463ba2695f3795cbee6c141581e2` | match |
| `V2_PROVENANCE.md` | `c1e515dd9efd3925c63b0aa2991a9ec87367ba5d29b07be1aad5c6d740fd53da` | match |
| `V2_MANIFEST.md` | `5fdd14f303accab5ea17affc1b3f737348be9786c1ced445fb0dd6b96442ff40` | match |
| `HOSTILE_AUDIT.md` | `4cd1acc3f3fdfe387a9c016c64602baebe81156463bf01ae40726df6f1c9e7be` | match |

## 2. Centered-carry reconstruction

Round-half-up gives

\[
a-\frac12\le \frac{up}{B}<a+\frac12,
\]

so

\[
-\frac B2\le x=up-aB<\frac B2.
\]

The same result holds for `y`.  Since `B | N-1`,

\[
xy\equiv (up)(uq)=u^2N\equiv u^2\pmod B.
\]

Thus

\[
c=\frac{xy-u^2}{B}
\]

is an integer.  Expanding `(aB+x)(bB+y)=u^2N`, using
`N=1+BH_B`, and substituting `xy=u^2+cB` gives

\[
u^2H_B=abB+ay+bx+c. \tag{R1}
\]

Independently,

\[
u(aq+bp)=2abB+ay+bx.
\]

Combining this identity with (R1) gives the stated sign:

\[
uT=u^2H_B+abB-c,
\qquad T=aq+bp.
\]

Finally,

\[
bp^2-Tp+aN=0
\]

and

\[
T^2-4abN=(aq-bp)^2.
\]

The carry sign, quadratic orientation, and square discriminant are all
correct.

The offset implications also follow exactly.  If `|x|<=X`, then
`|y|<B/2`, and hence

\[
|c|\le \frac{|x||y|+u^2}{B}
\le \frac X2+\frac{u^2}{B}.
\]

If `|c|<=C`, then

\[
|xy|=|u^2+cB|\le u^2+CB,
\]

which gives only

\[
\min(|x|,|y|)\le\sqrt{u^2+CB}.
\]

V2 correctly makes no selection or small-residue claim from this
square-root bound.

## 3. Exhaustive decoder and endpoint audit

For a true tuple, positivity and round-half-up give

\[
a=0\Longleftrightarrow 2up<B,
\qquad
b=0\Longleftrightarrow 2uq<B. \tag{R2}
\]

Since `p<q`, `b=0` implies `a=0`.  This makes the following split
exhaustive.

| True center case | Recovery equation | Result |
|---|---|---|
| `a=b=0` | `0=0` | The decoder skips the tuple. |
| `a=0<b` | `bX(X-p)=0` | The roots are `0,p`; the proper-factor test selects `p`. |
| `a>0,b=0` | Impossible by (R2) | No true tuple enters the linear branch. |
| `a>0,b>0` | Genuine quadratic with root `p` | The square-discriminant branch enumerates `p`. |

The arbitrary-guess branches are also safe.  When `b>0`, the decoder
returns only an integer proper divisor of `N`.  When `b=0`, the gate forces
`a>0`; requiring `T!=0` makes the linear candidate `aN/T` defined, and the
same range and exact-divisibility checks make any return value safe.  The
linear branch is not needed for a true tuple.

The V1 counterexample is repaired.  At `B=M=N-1,u=1`, distinct odd primes
give

\[
2p<M\Longleftrightarrow p(q-2)>1,
\qquad
2q<M\Longleftrightarrow q(p-2)>1.
\]

Both inequalities hold.  Therefore

\[
a=b=0,
\qquad x=p,
\qquad y=q,
\qquad c=1,
\qquad T=0.
\]

The polynomial is identically zero.  V2 now rejects this tuple before
candidate recovery.  The same gate rejects every other true tuple with two
zero centers.

A zero discriminant causes no remaining failure.  For a true tuple that
passes the gate, `b>0` and `p` is a root.  If the discriminant is zero, the
quadratic has the repeated root `p`, so the decoder still tests `p`.

Zero centered residues are also safe.  Since `B | N-1`, one has
`gcd(B,pq)=1`.  Hence

\[
x=0\Longleftrightarrow B\mid u,
\]

and this condition also gives `y=0`.  Writing `u=tB` gives

\[
a=tp,
\qquad b=tq,
\qquad c=-t^2B,
\]

and the recovery equation is

\[
tq(X-p)^2=0.
\]

Thus simultaneous zero residues produce positive centers and a valid
repeated root.  The displayed `B=1` case is a special case of this identity.

The half-tie convention is consistent at every endpoint.  The included
endpoint is `x=-B/2`; it implies `a>=1`, and monotonicity of round-half-up
then gives `b>=a`.  If `y=-B/2`, then `b>=1`.  The positive endpoint
`B/2` is excluded.  No included half-tie can create the rejected
two-zero-center case.

## 4. The P205 common-divisor point

Writing

\[
p-1=ds_p,
\qquad q-1=ds_q,
\qquad \gcd(s_p,s_q)=1
\]

gives

\[
M=d(s_p+s_q+ds_ps_q). \tag{R3}
\]

Therefore `d | M`.  If `A=M/d`, then

\[
A\equiv s_q\pmod {s_p},
\qquad
A\equiv s_p\pmod {s_q}.
\]

Thus `A` is coprime to both residuals.  For every prime `ell | s_i`,

\[
v_\ell(M)=v_\ell(d),
\]

so `ell | M` exactly when `ell | d`.  V2 uses this only as a support and
valuation statement.

Both `p-1` and `q-1` are even, so `d` is even.  At `B=d,u=1`, if `d>=4`,

\[
\frac pd=s_p+\frac1d
\]

lies strictly below the half-tie.  Hence `a=s_p,x=1`, and similarly
`b=s_q,y=1`.  Therefore `c=0`.

If `d=2`, then

\[
\frac p2=s_p+\frac12.
\]

Round-half-up gives `a=s_p+1` and `x=-1`.  It also gives
`b=s_q+1` and `y=-1`.  Their product is `1`, so `c=0`.  The additive-one
offset in the sole `B=d` tie case is correct.

The residual-window direction is also exact:

\[
s_p\le R
\Longleftrightarrow
d\ge\frac{p-1}{R}.
\]

Because `d | M` and `d<=p-1`, absence of every divisor of `M` from the
stated interval excludes `d` and forces `s_p>R`.  The presence of an
unrelated divisor gives no converse.  This is a numerical-size conclusion,
not a smoothness conclusion.

## 5. Exact optimum in the divisor-only grammar

Every allowed multiplicative word has prime support contained in the prime
support of `M`.  Gcd, lcm, and exact integer division do not add a new
prime.  Therefore every full primary part of `s_i` on a prime not dividing
`M` survives in

\[
\frac{s_i}{\gcd(s_i,W)}.
\]

This proves

\[
s_i^{\perp M}\mid\frac{s_i}{\gcd(s_i,W)}.
\]

The public word `W_*=M^n` attains equality.  Since

\[
s_i<N<2^n,
\]

every valuation `v_ell(s_i)` is strictly less than `n`.  For every
`ell | M`,

\[
v_\ell(M^n)=n v_\ell(M)\ge n.
\]

Thus `M^n` absorbs the complete part of each residual supported on `M`, for
both residuals at once, and leaves exactly the exterior part.  Its bit
length is `O(n^2)`.  It is an allowed one-divisor word and does not require
the factorization of `M`.

The optional baseline statement is the same support argument with `M`
replaced by `ML`.  The exponent `n` saturates every residual valuation on
that support.  For integral `R`, choosing `L=R!` adds every prime at most
`R`.  A complexity use of this extension still requires `L` to have an
appropriately bounded bit length.  V2's self-audit states this qualification;
the theorem itself makes only the support claim.

The optimum does not apply to addition, subtraction, shifted divisors,
carry children, modular residues, or any other integer with new prime
support.  The conclusion is exact only inside the declared multiplicative
grammar.

## 6. Additive selector and scope

The additive identities reconstruct directly:

\[
aB+x-u=u(p-1),
\qquad
bB+y-u=u(q-1).
\]

Each positive integer contains the corresponding residual in full.  Thus a
correct selected center-residue pair gives a valid P205 word.  If both
centers and the carry are selected at a true nondegenerate tuple, Section 3
gives a directly verified factor candidate.  Degenerate guesses can remain
in a bank because the decoder skips them.

The carry child

\[
xy=u^2+cB
\]

does not label the signed divisor `x`.  Factoring a nonzero child and
enumerating all its divisors are different operations.  A product of the
first `t` primes has `2^t` positive divisors and bit length
`Theta(t log t)`, so the number of divisors can be super-quasipolynomial in
the bit length.  This is an output-size warning for exhaustive enumeration.
It is not a selector lower bound and is not a claim about every carry child.
The zero-product child is publicly recognizable and is outside that
enumeration example.

There is one non-blocking wording residue in `V2_PROOF.md`: the primorial
estimate must use the first `t` primes, or another controlled prime
sequence, rather than an arbitrary set of `t` distinct primes.  The theorem
uses only the existential example, and the required controlled choice
exists.  This wording does not affect any stated boundary.

When `u=a=1`, one has `x=p-B`.  Scanning a bounded signed offset already
tests `B+x` as a factor.  V2 correctly does not count this direct factor
window as a separate carry gain.

The final scope is narrow and accurate.  V2 proves no all-input factoring
algorithm, no efficient divisor selector, no residual-smoothness theorem,
and no lower bound against methods outside its multiplicative grammar.
Additive divisor rules and semiprime-specific selectors remain open.

## Final result

**PASS.**  The V1 decoder defect is fully repaired, including all zero-center,
zero-residue, zero-discriminant, and round-half-up endpoint cases.  No claim
escapes the explicit divisor-only support scope.
