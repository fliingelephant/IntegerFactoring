# Proof-blind reconstruction target: quotient escape from an endpoint trap

Read only this statement. Do not read any other F70--F72 artifact, audit,
reconstruction, project theorem file, registry, progress note, or git history.
Reconstruct every proof independently. Report PASS only if every stated claim
and scope boundary follows.

## Family

Let \(s\ge2\) be even and put

\[
c=3s^2-1,
\qquad
N=c^2+c+1,
\]

\[
A=3s^2-3s+1,
\qquad
B=3s^2+3s+1.
\]

Prove

\[
N=AB,
\qquad
\gcd(A,B)=1,
\]

and show that \(A,B\) are odd nontrivial factors. Also prove
\(3\nmid N\).

## Endpoint-only source

Start from

\[
c\cdot c^2=c^3=1+(c-1)N. \tag{1}
\]

For every prime power \(p^a\Vert N\), prove that \(c\) has exact order three.
Deduce

\[
\langle c\rangle=\{1,c,c^2\}\pmod N
\]

and that this subgroup has no direct sign separator.

The declared endpoint-only source can:

1. form products or powers of authorized occurrences of the endpoint block;
2. retain the raw power or reduce it canonically modulo \(N\);
3. take a canonical inverse and append the relation;
4. use integer gcd refinement and exact perfect-power extraction;
5. use direct sign, inverse-pair difference and discriminant screens;
6. apply the complete rational-square decoder.

Assume \(c\) is not a perfect power. Prove that the gcd-free endpoint basis
remains the single possibly composite block \(c\); every raw relation value is
\(c^{3t}\); and every rational-square relation root is \(1\pmod N\).
Thus arbitrary endpoint occurrence amplification does not escape.

## Quotient promotion

The public quotient in (1) is

\[
q_0=c-1.
\]

Prove that it is outside the declared endpoint source. Promote it to the state

\[
g=c-1.
\]

Prove that its canonical inverse is

\[
w=\frac{c^2-1}{3}=s^2g,
\]

and that

\[
gw=R^2=1+(s^2-1)N,
\qquad
R=s(c-1).
\]

Verify

\[
R-1=(s-1)B,
\qquad
R+1=(s+1)A,
\]

and deduce the exact extraction

\[
\gcd(R-1,N)=B,
\qquad
\gcd(R+1,N)=A.
\]

## Earlier screens

Assume that no prime at most \(13\) divides \(N\). With \(d=g-w\), prove that
all of these gcds are one:

\[
\gcd(g\pm1,N),\quad
\gcd(w\pm1,N),\quad
\gcd(d,N),\quad
\gcd(d^2+4,N).
\]

Use

\[
d^2+4\equiv(g+w)^2\pmod N,
\qquad
g+w=g(s^2+1),
\]

and prove that every common divisor of \(s^2+1\) and \(N\) divides \(13\).
Conclude that the exact-square screen is the first successful declared screen.

## Infinite robust subfamily

Fix an integer threshold \(H\ge13\). Choose a prime

\[
\ell>H,\qquad \ell\equiv1\pmod {12}.
\]

Choose a residue \(a\pmod{\ell^2}\) such that

\[
3a^2-1\equiv0\pmod\ell,
\qquad
3a^2-1\not\equiv0\pmod{\ell^2}.
\]

Let \(M_H\) be the product of all primes at most \(H\). Use CRT to take
infinitely many positive integers \(s\) with

\[
s\equiv0\pmod {M_H},
\qquad
s\equiv a\pmod{\ell^2}.
\]

Prove that:

1. every such \(s\) is even;
2. every prime factor of \(c\), \(A\), \(B\), and hence \(N\), exceeds \(H\);
3. \(v_\ell(c)=1\), so \(c\) is not a perfect power;
4. the endpoint source remains trapped after trial division through \(H\) and
   perfect-power preprocessing;
5. quotient promotion still factors \(N\).

## Classification

Decide whether this establishes the narrow operation-set separation:

> Multiplicative endpoint feedback can remain trapped at the full subgroup
> and decoder levels, while promotion of a public relation quotient creates a
> new exact square and factors an infinite special family.

State explicitly that the quotient is public, the family is deliberately
manufactured and recognizable, and the proof gives no general quotient bias,
all-input sampler, inverse-polynomial success law, publication-level novelty
claim, or unrestricted factoring algorithm.
