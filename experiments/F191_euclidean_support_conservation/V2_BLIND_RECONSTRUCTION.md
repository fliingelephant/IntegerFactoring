# F191 V2 blind reconstruction

## Source discipline, hash, and verdict

This reconstruction used only `PROMPT.md` and `V2_STATEMENT.md`. It did not
use a proof, audit, manifest, provenance record, durable ledger, or another
F191 artifact. No mathematical experiment or finite search was used.

The independently computed SHA-256 of `V2_STATEMENT.md` is

```text
4666ed13b2318932a357c5a35ef4021c83355bf78cfeab3ffa1eb7bd6c8ac9ce
```

**VERDICT: PASS.** Every mathematical claim in the supplied statement follows
from the hypotheses stated there. In particular, the direct-child condition
is the strict condition (0<|A|<N/2); zero is never treated as a support
carrier. The unconditional roughness-cap conclusion uses a bank bound fixed
before, and independent of, that cap. The cap-dependent version is only the
conditional statement with the dominating numerical-QP function exhibited in
advance.

The references P161, P163, and P164 are treated as names for the interfaces
that `V2_STATEMENT.md` itself specifies. No assertion about material outside
that statement is needed below.

## Preliminary size and support facts

Let

\[
n=\left\lceil\log_2(N+1)\right\rceil.
\]

Then (N<2^n). Hence any nonzero integer (A) satisfying
(0<|A|<N/2) also satisfies

\[
1\le |A|<2^{n-1}.
\]

Thus (|A|) is a positive integer with at most (n-1) bits. This proves why
the displayed strict size condition in the statement is the relevant direct
P163 condition. The condition is not merely (|A|<N/2): (A=0) has no
finite rational-prime support and gives no positive auxiliary integer.

For a nonzero integer (A), saying that it has (ell)-support means exactly
that the prime (ell) divides (A), or equivalently divides (|A|).

## 1. Reconstruction of the support-conservation law

Assume that (ell) is prime,

\[
\ell\mid X,\qquad X=QD+R,
\]

and first suppose that (ell\nmid D). Reduction modulo (ell) gives

\[
0\equiv QD+R\pmod\ell,
\qquad	ext{so}\qquad
R\equiv-QD\pmod\ell.
\]

Because (D) is a unit modulo the prime (ell),

\[
R\equiv0\pmod\ell
\quad\Longleftrightarrow\quad
Q\equiv0\pmod\ell.
\]

This is exactly

\[
\ell\mid R\quad\Longleftrightarrow\quad\ell\mid Q.
\]

If instead (ellmid D) and (D\ne0), then (|D|) has (ell) in its
prime support. It is a direct admissible child only if the additional bounds

\[
0<|D|<N/2
\]

hold. If (D=0), the divisibility convention (ellmid0) does not turn zero
into a positive support carrier, so this degenerate case gives no direct
auxiliary.

Now take (D=N) and assume (gcd(ell,N)=1). Then (ell\nmid N), so the
same equivalence applies to every exact decomposition

\[
X=QN+R,
\]

including ordinary division and centered division. The extra centered bound
(|R|<N/2) does not change the congruence. Therefore:

- if (ell\nmid Q), then (ell\nmid R), so factoring the nonzero integer
  (|R|) cannot produce (ell);
- if (ellmid R), then (ellmid Q) already held before the remainder was
  used.

This proof uses only the integer equality (X=QD+R). It is consequently
independent of whether (X) was written explicitly or arose as a polynomial
value, resultant, factorial value, cyclotomic value, or succinct power. The
conclusion applies whenever the localization operation is that Euclidean
equality.

## 2. Reconstruction of the canonical counterexample

Assume

\[
N\ge7,\qquad 3\le\ell<N/2,
\qquad \ell\text{ an odd prime},
\qquad \gcd(\ell,N)=1.
\]

For odd (ell), the integers

\[
-{\ell-1\over2},\ldots,-1,0,1,\ldots,{\ell-1\over2}
\]

form a complete residue system modulo (ell). Thus there is a unique
balanced representative (c) with

\[
c\equiv-N\pmod\ell,
\qquad |c|\le {\ell-1\over2}.
\]

It is nonzero because (ell\nmid N). Therefore

\[
0<|c|\le {\ell-1\over2}< {\ell\over2}< {N\over4}.
\]

Set (X=N+c). The defining congruence for (c) gives

\[
X\equiv0\pmod\ell.
\]

The stronger bounds (3N/4<X<5N/4) follow from (|c|<N/4), and imply the
claimed weaker bounds

\[
N/2<X<3N/2.
\]

Since (|c|<N/2), the canonical centered division of (X) by (N) is

\[
X=1\cdot N+c.
\]

Both children meet the strict direct-child size condition:

\[
0<1<N/2,
\qquad
0<|c|<N/2.
\]

Neither has (ell)-support. Clearly (ell\nmid1), and
(0<|c|<ell) implies (ell\nmid c). Thus (X) is an exact
(ell)-multiple within (N/2) of (N), while its centered quotient and
centered remainder are both admissible smaller nonzero integers that miss
(ell). This reconstructs all claims in the canonical example.

## 3. Reconstruction of the permutation-bank theorem

Assume that (N) is odd, (ell<N/2) is prime,
(gcd(ell,N)=1), and each (pi_i) is a permutation of
({0,ldots,N-1}). Fix one selector (i), write

\[
k=\pi_i(u),qquad 0\le k\le N-1,
\]

and center-divide

\[
\ell k=Q_i(u)N+R_i(u),
\qquad |R_i(u)|<N/2.
\]

Because (N) is odd, an integer cannot lie exactly halfway between two
integer multiples of (N): an equality (2\ell k=(2q+1)N) would equate an
even integer with an odd integer. Thus the nearest-integer quotient is
unique.

### The one-selector count

The real number (ell k/N) lies in the interval ([0,ell)). Its nearest
integer therefore belongs to

\[
Q_i(u)\in\{0,1,\ldots,\ell}.
\]

The only multiples of (ell) in this set are (0) and (ell). The
quotient can equal (0) only when

\[
{\ell k\over N}<\frac12,
\qquad	ext{equivalently}\qquad
k<{N\over2\ell},
\]

and it can equal (ell) only when

\[
{\ell k\over N}>\ell-\frac12,
\qquad	ext{equivalently}\qquad
k>N-{N\over2\ell}.
\]

Each of these two endpoint intervals contains at most
(N/(2\ell)+1) integers. Hence at most

\[
2\left({N\over2\ell}+1\right)
={N\over\ell}+2
\]

values of (k) give a quotient divisible by (ell). Since (pi_i) is a
permutation, the same bound holds for the number of parameters (u).

Apply the support-conservation law with (X=ell k) and (D=N). It gives,
pointwise in (u),

\[
\ell\mid Q_i(u)quad\Longleftrightarrow\quad
\ell\mid R_i(u).
\]

The two parameter sets are therefore equal, and

\[
\#\{u:\ell\mid Q_i(u)\}
=\#\{u:\ell\mid R_i(u)\}
\le {N\over\ell}+2.
\]

### The bank union bound

For a prime (ell), the condition
(ellmid Q_i(u)R_i(u)) means that (ell) divides at least one factor.
For each selector this happens on at most (N/\ell+2) parameters. A union
bound over the (B) selectors gives

\[
\#\{u:\exists i,\ \ell\mid Q_i(u)R_i(u)\}
\le B\left({N\over\ell}+2\right).
\]

If

\[
\ell\ge4B,
\qquad
N\ge8B,
\]

then

\[
B\left({N\over\ell}+2\right)
\le {N\over4}+2B
\le {N\over2}.
\]

There are (N) possible parameters. Thus the complement is nonempty, and
one can choose a parameter (u) for which every (Q_i(u)) and every
(R_i(u)) misses (ell), although every input
(X_i(u)=ell\pi_i(u)) is divisible by (ell).

It remains important to prove, rather than assume, that all selected
children are admissible. From the earlier quotient range,
(0\le Q_i(u)\le\ell). The endpoints (0) and (ell) are divisible by
(ell), so the selected good parameter excludes both. Therefore

\[
1\le Q_i(u)\le\ell-1<N/2.
\]

The centered construction already gives (|R_i(u)|<N/2). Also (R_i(u))
cannot be zero, because every prime divides zero and the good parameter was
chosen to satisfy (ell\nmid R_i(u)). Hence

\[
0<|R_i(u)|<N/2.
\]

Consequently all (2B) children are nonzero, strictly smaller than (N/2),
and have at most (n-1) bits, yet none has (ell)-support.

### Quantifier order for (B_\star) and (T)

The unconditional specialization has the following order.

1. Fix a numerical function (B_\star(n)\ge1), independently of any
   roughness cap, and constants (c,C>0) such that
   \[
   B_\star(n)\le2^{c(\log_2(n+2))^C}.
   \]
2. Only after that choice, define
   \[
   T(n)=4B_\star(n)+1.
   \]
3. Quantify over every bank size (B\le B_\star(n)) and every relevant
   prime (ell>T(n)).

For such a bank and prime,

\[
\ell>T(n)=4B_\star(n)+1>4B.
\]

In the stated composite branch, (ell<N/2), so

\[
N>2\ell>8B.
\]

Thus the hypotheses of the bank union bound hold.

Both (B_\star) and (T) are numerical-QP functions. To see this directly,
for the relevant input lengths (n\ge2), put
(L=\log_2(n+1)\ge1). Then

\[
\log_2(n+2)\le1+L\le2L.
\]

Thus the displayed bound for (B_\star) is bounded by
(2^{c2^C L^C}); if necessary, replacing (C) by the integer
(lceil C\rceil) preserves an upper bound because (L\ge1). Moreover,
since (B_\star\ge1),

\[
T=4B_\star+1\le5B_\star,
\]

and the fixed factor (5) is absorbed into the constant in the QP
exponent. This proves the numerical-QP claim without making (B_\star)
depend on (T).

If instead the proposed bound has the form (B_\star(n,T)), defining
(T=4B_\star(n,T)+1) would be circular and need not have a numerical-QP
solution. The valid statement has the different order

\[
\exists\,T(n)\text{ numerical-QP such that, for all relevant }n,
\qquad
4B_\star(n,T(n))<T(n),
\]

with this function exhibited before applying the bank theorem. Only then,
for every (B\le B_\star(n,T(n))) and every (ell>T(n)), does one get

\[
\ell>T(n)>4B_\star(n,T(n))\ge4B,
\]

and, using (ell<N/2), also (N>8B). Nothing in the counting proof gives
the existence of such a dominating (T) for an arbitrary two-variable
(B_\star). The conditional limitation in the supplied statement is
therefore necessary and correctly stated.

## 4. Reconstruction of the surviving interface and scope

Suppose a construction produces, at total numerical-QP cost, a public list

\[
A_1,\ldots,A_s
\]

of numerical-QP length such that every entry satisfies

\[
0<|A_j|<N/2,
\]

and every surviving local-order prime divides at least one entry. Then each
(|A_j|) is positive, has at most (n-1) bits by the preliminary size
argument, and retains exactly the rational-prime support of (A_j). Hence

\[
|A_1|,\ldots,|A_s|
\]

is directly admissible for the interface stated for P163. An entry of
absolute value one has empty prime support and can be omitted without
destroying coverage.

A quotient, remainder, carry, or modulus that is zero or is not proved to
have absolute value below (N/2) does not meet this interface. In
particular, (ellmid0) cannot be used to evade the nonzero condition. Such
an object can be useful only after a separate numerical-QP transformation
is proved to output admissible nonzero smaller integers while preserving the
needed support.

The conservation law proves that ordinary or centered Euclidean reduction,
by itself, supplies no such support-transfer theorem: with a unit modulus,
the remainder has (ell)-support exactly when the discarded quotient does.
The canonical example shows total support loss for one exact multiple, and
the permutation theorem shows simultaneous loss against any bank satisfying
the stated size relations.

These arguments concern only the transition

\[
\text{known large }\ell\text{-multiple}
\longrightarrow
\text{Euclidean or centered quotient and remainder}
\longrightarrow
\text{claimed admissible support child}.
\]

They do not address a separately proved correlated floor theorem that forces
an admissible (ell)-divisible quotient or carry, a non-Euclidean selector,
or a direct factor or common-order construction. Therefore the limited scope
and all stated non-exclusion claims follow exactly from what the proof does
and does not use.

## Final claim audit

- The congruence equivalence is proved for every integer decomposition under
  the exact unit hypothesis.
- The nonunit case is separated from admissibility, and (D=0) is explicitly
  rejected.
- The canonical counterexample satisfies divisibility, centered uniqueness,
  strict nonzero size bounds, and support loss for both children.
- The one-selector count, bank union bound, existence of a good parameter,
  and admissibility of all (2B) resulting children are proved.
- The independent-(T) and dependent-(T) cases use the correct quantifier
  order; no dominating cap is asserted for an arbitrary (B_\star(n,T)).
- The final interface includes positivity after absolute value, the
  (n-1)-bit consequence, QP list/cost requirements, and prime-support
  coverage.

No unsupported strengthening or missing case was found. The verdict remains
**PASS**.
