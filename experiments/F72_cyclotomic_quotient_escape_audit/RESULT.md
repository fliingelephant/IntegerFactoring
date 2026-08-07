# Hostile audit of F72

## Verdict

**PASS.** I found no blocking algebraic, number-theoretic, algorithmic-source,
or scope defect.

I audited only
`experiments/F72_cyclotomic_quotient_escape/RESULT.md`. Before reading it, I
computed its SHA-256 as

```text
c6a02473aa6efd340bfec009d0fb9581cd164b4ce80d4b32b9969d00d53b6c10
```

which is the required hash. In this report I rename the trial-division bound
in Section 6 to (H), because the candidate reuses (B) for both that bound
and the factor (3s^2+3s+1).

## 1. Base factorization and gcd claims

Let

\[
c=3s^2-1,\qquad N=c^2+c+1,
\]

and let

\[
A=3s^2-3s+1,\qquad B=3s^2+3s+1.
\]

Direct expansion gives

\[
AB=(3s^2+1)^2-(3s)^2=9s^4-3s^2+1=N.
\]

For even (s\ge2), (A) and (B) are odd and greater than one, and both
are (1\pmod 3). If a prime divides both, it divides (B-A=6s). But
(A\equiv B\equiv1\pmod s), neither factor is divisible by (2), and
neither is divisible by (3). Thus no such prime exists and

\[
\gcd(A,B)=1.
\]

This proves that (N=AB) is an odd composite with two coprime nontrivial
factors. Also (c\equiv-1\pmod3), so (N\equiv1\pmod3).

## 2. Exact local order and the endpoint trap

The identity

\[
c^3-1=(c-1)(c^2+c+1)=(c-1)N
\]

is exact. Hence the order of (c) modulo every (p^a\Vert N) divides
three. If (c\equiv1\pmod p), then (0\equiv N\equiv3\pmod p), forcing
(p=3), which is impossible. The order modulo (p^a) is therefore exactly
three. Consequently (1,c,c^2) are distinct modulo every prime divisor of
(N), and neither (c) nor (c^2) is locally (1) or (-1). Since
(1<c<c^2<N), these are also the canonical representatives.

This validates all of the endpoint screen claims:

- unequal powers among (1,c,c^2) have gcd-one differences with (N);
- equal powers give only the global gcd (N);
- sign screens on (c) and (c^2) give gcd one;
- for the inverse pair (c,c^2),
  \((c-c^2)^2+4\equiv(c+c^2)^2\equiv1\pmod N\), so its discriminant
  screen also gives gcd one.

The composite-block issue does not invalidate the trap. Starting from the
integer endpoints (c,c^2), every raw product is (c^e). Gcd refinement
and exact division between such products still return powers of the same
block. If (c) is not a perfect power, maximal perfect-power extraction of
(c^e) recovers the same primitive base (c); it does not factor the
possibly composite integer (c).

A relation obtained only from endpoint occurrences has value (c^{3t}),
because its residue is one exactly when its exponent is divisible by three.
For the robust subfamily, a prime (ell) has (v_\ell(c)=1). Thus any
product or ratio of relation values has the form (c^{3T}), and it can be a
rational square only if (3T) is even. Hence (T) is even and its positive
root is

\[
c^{3T/2}\equiv1\pmod N.
\]

The same conclusion follows from the weaker condition that (c) is not a
perfect power: then some prime valuation of (c) is odd. Therefore the full
endpoint-only square decoder has only the residue-one image. Composite
internal structure in (c) supplies no second gcd-free block.

## 3. The quotient is outside the declared source

The seed relation quotient is exactly

\[
q_0=\frac{c^3-1}{N}=c-1.
\]

Under the source declared in the candidate, endpoint multiplication,
canonical inversion, gcd refinement, exact division, and perfect-power
extraction produce only powers of the primitive block (c), with canonical
residues in \(\{1,c,c^2\}\). Since (c\ge11),

\[
1<c-1<c,
\]

so (c-1) is neither an endpoint representative nor any nonnegative power
of (c); negative powers are nonintegral. It also cannot arise from gcd
refinement of powers of (c). Thus the quotient is genuinely outside the
declared multiplicative endpoint source.

The integer (c-1) is, of course, already computable from (c), and a sign
screen uses it as a gcd operand. The candidate does not claim otherwise.
Its boundary is state promotion: a failed gcd screen does not feed its
operand as a new block, whereas Section 4 explicitly feeds the relation
quotient. The theorem is valid as an operation-set separation, not as an
information-theoretic separation. Section 7 states this boundary accurately.

## 4. Quotient-fed square and exact extraction

Put (g=c-1). Since (c\equiv2\pmod3),

\[
w=\frac{c^2-1}{3}=\frac{(c-1)(c+1)}3=s^2g
\]

is an integer. It satisfies (1<w<N). Moreover,

\[
gw=s^2(c-1)^2=R^2,\qquad R=s(c-1),
\]

and direct expansion gives

\[
R^2-1=(s^2-1)N.
\]

Hence (gw\equiv1\pmod N), so (w) is exactly the canonical inverse of
(g). The root identities are also exact:

\[
R-1=(s-1)B,\qquad R+1=(s+1)A.
\]

Substitution of (s=1) modulo (s-1) gives
(A\equiv1\pmod{s-1}), and substitution of (s=-1) modulo (s+1)
gives (B\equiv1\pmod{s+1}). Therefore

\[
\gcd(s-1,A)=\gcd(s+1,B)=1.
\]

Together with (gcd(A,B)=1), this yields the exact, not merely nontrivial,
extractions

\[
\gcd(R-1,N)=B,\qquad \gcd(R+1,N)=A.
\]

## 5. All declared pre-square screens fail

Assume no prime at most (13) divides (N). First,

\[
\gcd(g+1,N)=\gcd(c,N)=1.
\]

Polynomial division gives

\[
N=(c+3)(c-2)+7,
\]

so (gcd(g-1,N)=1) under the assumption. Because (g) is a unit and
(gw\equiv1\pmod N), the corresponding sign gcds for (w) are the same.
Likewise multiplication by the unit (g) shows

\[
\gcd(g-w,N)=\gcd(g^2-1,N)=1.
\]

For (d=g-w),

\[
d^2+4\equiv(g+w)^2\pmod N,
\qquad g+w=g(s^2+1).
\]

The factor (g) is a unit modulo (N). Writing (x=s^2),

\[
9x^2-3x+1=(x+1)(9x-12)+13,
\]

so every common divisor of (s^2+1) and (N) divides (13). The
discriminant gcd is therefore one. Thus every listed sign, inverse-pair
difference, and discriminant screen fails before the exact-square screen
(gw=R^2), which succeeds.

## 6. CRT--Dirichlet robustness and exact valuation

Fix a threshold (H\ge13). Dirichlet's theorem supplies a prime
(ell>H) with (ell\equiv1\pmod{12}). Quadratic reciprocity then gives
((3/\ell)=1), so (f(x)=3x^2-1) has a root (r\pmod\ell). Since
(f'(r)=6r\not\equiv0\pmod\ell), exactly one of the (ell) lifts of
(r) modulo (ell^2) is a root modulo (ell^2). Any other lift (a)
satisfies

\[
f(a)\equiv0\pmod\ell,\qquad f(a)\not\equiv0\pmod{\ell^2}.
\]

The moduli (M_H=\prod_{q\le H}q) and (ell^2) are coprime. CRT therefore
gives an infinite progression

\[
s\equiv0\pmod{M_H},\qquad s\equiv a\pmod{\ell^2}.
\]

It contains infinitely many positive even (s\ge2). For every prime
(q\le H),

\[
c\equiv-1\pmod q,\qquad A\equiv B\equiv1\pmod q,
\]

so all prime factors of both (c) and (N=AB) exceed (H). Also
(s\equiv a\pmod{\ell^2}) implies

\[
v_\ell(c)=v_\ell(3s^2-1)=1.
\]

Hence (c) is not a perfect power. By taking any sufficiently large
positive member of the progression, one also has (c>\ell). Then
(ell\mid c) is a proper divisor, so (c) is composite. Discarding the
finitely many smaller representatives leaves an infinite family of
composite, non-perfect-power, one-block (c)'s. This explicitly resolves
the composite-gcd-free-block case and proves the claimed growing
least-prime-factor property.

## 7. Scope audit

The construction proves exactly a source-closure failure: multiplicative
endpoint feedback remains trapped, but promotion of the public relation
quotient adds a new block and yields a square whose root separates the two
local signs. It does not prove that quotient feedback is useful on general
inputs. It does not hide the fact that this family is recognizable and
already has the explicit factorization (N=AB). The candidate's final scope
paragraph excludes a general selector, a success probability, and an
unrestricted factoring algorithm. Those exclusions match what was proved.

## Nonblocking presentation issues

1. Section 6 shadows the already-defined factor (B) with the
   trial-division bound. Renaming the bound to (H) removes the ambiguity.
2. Composite (c) follows by choosing a sufficiently large positive CRT
   representative, as shown above. The candidate states non-perfect-power
   explicitly but could state this one-line restriction explicitly too.

Neither issue affects the theorem or its infinite-family claim.
