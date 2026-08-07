# Fresh hostile audit of F71

## Verdict: PASS

I audited only
`experiments/F71_cyclotomic_feedback_trap/RESULT.md`. Before reading it, I
verified its SHA-256 as

```text
3d769c9760f1b947d3023979cfef83d0d3a9d71ee9444eeef9169344910579a1
```

I found no blocking mathematical error, missing quantifier, decoder escape, or
scope overclaim in the stated endpoint-only obstruction.

## 1. Seed arithmetic and order modulo prime powers

The seed identity is exact:

\[
c^3-1=(c-1)(c^2+c+1)=(c-1)N.
\]

Also \(\gcd(c,N)=1\), because \(N\equiv1\pmod c\). Let
\(p^a\Vert N\). The identity gives \(c^3\equiv1\pmod{p^a}\). Hence the
order of \(c\) modulo \(p^a\) divides three. If that order were one, then
\(c\equiv1\pmod p\), so

\[
0\equiv c^2+c+1\equiv3\pmod p.
\]

This would give \(p=3\), contrary to \(3\nmid N\). Thus the order is exactly
three in every prime-power component. Consequently the order modulo \(N\) is
also exactly three, and

\[
\langle c\rangle=\{1,c,c^2\}\pmod N.
\]

Because \(c\ge3\), the inequalities \(1<c<c^2<N\) hold. These are therefore
the stated canonical representatives. Their positive divisors, and the
divisors of any retained raw power \(c^e\), are powers of the sole prime
block \(c\).

## 2. Trivial state, canonical feedback, and raw powers

For every integer \(e\ge0\), reduction is exactly

\[
c^e\bmod N\in\{1,c,c^2\},
\]

with the representative determined by \(e\bmod3\). The identity state is
illegal under \(1<g<N\). If it is nevertheless retained, its inverse relation
is only \(1\cdot1=1\), so it supplies neither a block nor a nontrivial
relation value. The other two states are mutual inverses and both give the
same value \(c^3\).

For a retained raw power \(G=c^e\), let its canonical inverse be
\(w=c^j\), where \(j\in\{0,1,2\}\). Then \(e+j\equiv0\pmod3\), and for an
oversized positive power

\[
Gw=c^{e+j}=c^{3t},\qquad t\ge1.
\]

Thus raw retention does not change the prime support. Products, powers, gcd
refinement, and exact perfect-power roots of endpoint or relation values all
remain in \(\{c^k:k\ge0\}\). This supplies the required induction for every
finite endpoint-feedback transcript.

## 3. Direct sign, difference, and discriminant screens

The sign claims are correct. A nonidentity subgroup element has order three
in every prime-power component. It can be neither \(1\) nor \(-1\) modulo a
prime divisor of the odd number \(N\). Hence all four gcds in (3) are one.
Equivalently, the potentially delicate minus case reduces to
\(\gcd(c-1,N)\mid3\), and the hypothesis removes the only possibility.
For an identity residue, the minus screen gives \(N\) and the plus screen
gives one because \(N\) is odd.

For a nonidentity inverse pair, the difference is congruent up to sign to
\(c-c^2=c(1-c)\). Since \(\gcd(c,N)=1\) and
\(\gcd(c-1,N)=1\), its gcd with \(N\) is one. For an identity pair, the
difference is zero modulo \(N\), so the result is global.

For \(d=G-w\), the discriminant identity is

\[
d^2+4=(G+w)^2-4Gw+4\equiv(G+w)^2\pmod N.
\]

In a nonidentity orientation, \(G+w\equiv c+c^2\equiv-1\pmod N\); in the
identity orientation it is congruent to two. Therefore
\(d^2+4\equiv1\) or \(4\pmod N\), respectively. Both residues are units
because \(N\) is odd. The discriminant gcd is therefore one. No direct screen
returns a proper divisor.

## 4. Full rational-square decoder

All generated relation values have the form \(c^{3t_i}\). For integer
coefficients \(z_i\), including negative coefficients, their rational product
is

\[
c^{3S},\qquad S=\sum_i z_i t_i.
\]

It is a rational square exactly when \(3S\) is even, equivalently when
\(S\) is even. Its canonical positive rational root is then

\[
c^{3S/2}=(c^3)^{S/2}\equiv1\pmod N.
\]

This contains the binary-selection calculation in (8) and also checks the
claimed complete integer relation space. The exponent lattice lies in
\(3\mathbb Z\). Its \(2\)-saturation still lies in \(3\mathbb Z\), because
three is coprime to every power of two. Thus saturation cannot produce a
root whose exponent is nonzero modulo three.

For canonical relations, every column has the one-bit parity vector, so the
binary kernel is exactly the even-weight subspace and (7) follows. With the
document's exact-positive-root convention, the decoder image is precisely
\(\{1\}\). Allowing the other algebraic sign would add only the global value
\(-1\), which also cannot split \(N\).

## 5. Perfect-power claims

Exact roots of \(c^2\), raw endpoints \(c^e\), and relation values
\(c^{3t}\) have only the prime support \(c\). The other displayed public
square is also correct:

\[
4N-3=4(c^2+c+1)-3=(2c+1)^2.
\]

Its root does not split \(N\), since

\[
\gcd(2c+1,N)\mid\gcd((2c+1)^2,N)
=\gcd(4N-3,N)=\gcd(3,N)=1.
\]

The value \(2c+1\) is not a power of \(c\), but this is not a closure defect:
the result defines feedback from endpoint blocks and later explicitly places
non-endpoint integer data and new independent blocks outside its scope. It
does not authorize feeding this auxiliary public root back as an endpoint.
The same explicit boundary applies to the quotient \(c-1\). Within the
declared source rule, no second block is created.

For the infinite family, either one of the two asserted valuation-one prime
divisors already rules out \(N=y^k\) with \(k\ge2\), since all prime
valuations of such a power are divisible by \(k\). Having two such divisors
is stronger than necessary.

## 6. CRT--Dirichlet family

For each integer \(B\ge3\), distinct primes
\(\ell_1,\ell_2>B\) with \(\ell_i\equiv1\pmod3\) exist. Their unit groups
contain elements of exact order three. A nontrivial cube root \(r_i\) is a
root of \(F(X)=X^2+X+1\). It is simple: if
\(2r_i+1\equiv0\pmod{\ell_i}\), substitution gives
\(F(r_i)\equiv3/4\), forcing \(\ell_i=3\), impossible here.

Hensel lifting therefore gives exactly one root lift modulo \(\ell_i^2\).
Choosing any other lift \(a_i\) gives

\[
v_{\ell_i}(F(a_i))=1.
\]

The moduli in (11) are pairwise coprime: the \(\ell_i\) exceed \(B\), and
the remaining moduli are distinct primes at most \(B\). Every prescribed
residue is a unit, including each \(a_i\), because it reduces to the nonzero
root \(r_i\). The CRT class is therefore reduced. Dirichlet's theorem gives
infinitely many prime values of \(c\) in that fixed class.

Polynomial congruence modulo \(\ell_i^2\) transfers the chosen lift property
to every such \(c\), so

\[
v_{\ell_1}(N)=v_{\ell_2}(N)=1.
\]

Thus \(N\) is composite, has two distinct prime divisors, and is not a
perfect power. The small-prime exclusion is exhaustive:

- \(2\nmid N\) because \(c\) is odd;
- \(F(c)\equiv F(2)\equiv1\pmod3\);
- for each prime \(5\le q\le B\),
  \(F(c)\equiv F(1)=3\not\equiv0\pmod q\).

Hence every prime divisor of \(N\) exceeds \(B\). Selecting one constructed
prime \(c\) for each unbounded sequence of values of \(B\) gives a sequence
whose least prime divisor tends to infinity. All theorem quantifiers are
satisfied.

## 7. Witness and scope

For \(c=11\), the arithmetic is correct:

\[
N=133=7\cdot19,\qquad 11^3=1331=1+10\cdot133.
\]

The residue of 11 has order three modulo both 7 and 19. Two duplicate
relations give exact root \(11^3\equiv1\pmod{133}\), as claimed.

The proved statement is an obstruction only for feedback generated from the
sole existing endpoint block, with products, powers, canonical inversion,
the listed refinement and direct screens, and the complete square decoder.
It does not claim hardness, a lower bound for arbitrary factoring, or closure
after introducing an independent block, quotient, additive datum, or order
method. Those exclusions match the proof and prevent no hidden
generalization. The named comparisons in the final section are not premises
of the proof; the substantive within-document claims attached to them
(duplicate parity closure, global decoder roots, and absence of endpoint
refinement gain) follow from the calculations above.

No blocking defect remains.
