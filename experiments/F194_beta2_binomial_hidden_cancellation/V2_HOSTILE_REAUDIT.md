# F194 V2 hostile re-audit

## Frozen-input verification

The V2 manifest was read before the candidate. Every declared SHA-256 digest
matches the observed bytes:

| Frozen input | Declared and observed SHA-256 | Result |
|---|---|---|
| `V2_STATEMENT.md` | `95764227ebc288a528c7425c5593e9a75d7ad9030556c4a9c12b00c0c85f48ab` | match |
| `V2_PROOF.md` | `ea19a8a5fe2410e24841876a5b04c4e6e23e4f9f466838e0a9ebaf83ffcbb029` | match |
| `V2_SELF_AUDIT.md` | `3b04854c356f7076841e47e088aff34b2007cc503400996e7efc011144bb8dbb` | match |
| `V2_PROVENANCE.md` | `a7d5e7fdddfe9688797cf5bb0052ae12d4278d04eddb8df1fd3e995059077a61` | match |

The preserved V1 hostile audit also has its provenance-declared digest:

```text
a3f49a53f54ac7bb69488958e7b1141d2206c61a834ef28bdd6e6c46d1be5fb9
```

The four V2 inputs and the V1 hostile audit were read in full.

## Exact verdict

**FAIL for the exact frozen package; PASS for the mathematical
statement-and-proof pair.**

All requested mathematical claims reconstruct under their stated narrow
scope. The false V1 inequality is exactly repaired. The cyclic claim is now
strictly Boolean incidence, the gap bound is numerical-QP, and the carry
primitive now requires the joint modular pair.

The exact package nevertheless contains one factual provenance defect.
`V2_PROVENANCE.md` says:

> V2 makes only the four repairs listed in `V2_SELF_AUDIT.md`.

But the cited self-audit lists five V2 changes:

1. replace the false central-binomial inequality;
2. narrow cyclic provenance to Boolean source incidence;
3. impose a numerical-QP bound on (R);
4. replace the standalone carry with the joint residue pair;
5. remove the unsupported claim about standard holonomic algorithms.

The fifth change is also visible in the V1 hostile audit and V2 statement.
Thus “four repairs listed” is false. Because provenance is one of the frozen
inputs expressly included in this re-audit, the exact frozen package cannot
receive an unqualified pass. This is a documentation defect, not a defect in
Theorems 1--4 or the modular-carry corollary.

No other promotion-blocking defect was found. The remainder of this audit
records the complete reconstruction and the precise interpretation required
for each sufficiency or complexity phrase.

## 1. The V1 inequality is exactly repaired

Let (m=\lceil B/2\rceil). V2 no longer uses the false V1 comparison
(2p\le q+1). Instead it proves

\[
2m\le B+1\le q.
\]

The first inequality follows directly from the ceiling. The second follows
from (B<q) and integrality. If (2m=q), an even integer equals the odd
prime (q), which is impossible. Therefore (2m<q).

The other half of the range is also valid:

\[
m\le\frac{B+1}{2}<p.
\]

Indeed, (B<\sqrt2,p), and
(sqrt2,p+1<2p) for every odd prime (p\ge3). Thus V2 establishes

\[
m<p\le2m<q
\]

without the V1 error. The repair is present in both `V2_PROOF.md` and the
summary in `V2_SELF_AUDIT.md`.

## 2. Balance ranges

The promise (p<q<2p) gives

\[
p^2<N=pq<2p^2.
\]

Consequently,

\[
p\le B<\sqrt2,p<2p.
\]

Also (sqrt{pq}<q), so (B<q). The prefix (1,\ldots,B) therefore
contains (p), but contains neither (2p) nor (q). These are exactly the
range facts used later; no unbalanced or repeated-prime input is covered.

## 3. One-jump cancellation, AKS coefficient, and signs

For every (k), the integer identity

\[
k!A_k=\prod_{i=1}^k(i-N)
\tag{A1}
\]

holds. If (k<p), all (1\le i\le k) are units modulo (N), so each
quotient ((i-N)i^{-1}) is one and (A_k\equiv1\pmod N).

For (p\le k\le B), define

\[
U=\prod_{\substack{1\le i\le k\\i\ne p}}i,
\qquad
V=\prod_{\substack{1\le i\le k\\i\ne p}}(i-N).
\]

The balance range makes (U) coprime to (N). Isolating the unique
nonunit in (A1) gives an equality in the integers:

\[
pUA_k=(p-N)V=p(1-q)V.
\]

V2 cancels (p) here, in (mathbb Z), before reducing:

\[
UA_k=(1-q)V.
\]

Reduction gives (V\equiv U\pmod N), after which only the unit (U) is
inverted. Hence

\[
A_k\equiv1-q\pmod N.
\]

There is no illegal division by (p) in (mathbb Z/Nmathbb Z).

For (1\le k\le B),

\[
k\binom Nk=N\binom{N-1}{k-1}.
\]

Every (k\ne p) in this range is a unit modulo (N), so its coefficient
is zero. At (k=p), exact integer cancellation yields

\[
\binom Np=q\binom{N-1}{p-1}\equiv q\pmod N,
\]

because (p-1) is even and before the jump. Thus the exceptional AKS
coefficient has sign (+q).

The alternating-prefix identity gives

\[
(-1)^B\binom{N-1}{B}
=\sum_{k=0}^{B}(-1)^k\binom Nk
\equiv1-q\pmod N,
\]

because (p) is odd. Therefore the signed shift is congruent to (-q),
and

\[
\gcd\!\left(N,(-1)^B\binom{N-1}{B}-1\right)=q.
\]

The canonical endpoint residues in (4) follow by multiplying by the known
sign. The statement also calls the remote coefficient a unit. This is
correct: it is nonzero modulo (q), and it could vanish modulo (p) only
if (q\equiv1\pmod p). Under (p<q<2p), that would force (q=p+1),
which is even and greater than (2), hence not prime.

Finally, the exact adjacent-binomial identity is

\[
(k+1)A_{k+1}=(k+1-N)A_k,
\]

equivalently

\[
(k+1)(A_{k+1}-A_k)=-NA_k.
\]

The only nonunit transition in the prefix is (k+1=p), where exact
division contains (N/p=q). This explains the word; it does not give a
succinct endpoint evaluator.

## 4. Both central-binomial valuations

The repaired inequalities give

\[
m<p\le2m<q<2p.
\]

In

\[
\binom{2m}{m}=\frac{(m+1)\cdots(2m)}{m!},
\]

the denominator is coprime to (pq). The numerator interval contains the
single multiple (p) and no multiple of (q). Its (p)-valuation is one
and its (q)-valuation is zero, so the gcd with squarefree (N) is (p).

For

\[
\binom{2B}{B}=\frac{(B+1)\cdots(2B)}{B!},
\]

the denominator contains (p) exactly once and contains no (q). The
numerator interval contains (2p), since (B<2p\le2B), and contains (q),
since (B<q<2p\le2B). It has no further multiple of (p), because

\[
2B<2\sqrt2,p<3p,
\]

and no second multiple of (q), because (2B<2q). The single numerator
and denominator (p)-valuations cancel, while one (q)-valuation remains.
Thus

\[
\gcd\!\left(N,\binom{2B}{B}\right)=q.
\]

All relevant prime multiples and their valuations are counted. Both gcd
claims pass.

## 5. Polynomial moments

For (W\in\mathbb Z[T]), there is (V\in\mathbb Z[T]) such that

\[
W(T)-W(0)=TV(T).
\]

Using (k\binom Nk=N\binom{N-1}{k-1}) in the integers,

\[
\sum_{k=1}^{N-1}(W(k)-W(0))\binom Nk
=N\sum_{k=1}^{N-1}V(k)\binom{N-1}{k-1},
\]

which vanishes modulo (N). The constant part is

\[
W(0)\sum_{k=1}^{N-1}\binom Nk=W(0)(2^N-2).
\]

This proves (8) for every integer polynomial, with no degree restriction.
V2 correctly labels it only an algebraic collapse. It makes no evaluation,
circuit, or lower-bound inference from a succinct high-degree description.

## 6. Frobenius expansions and exact local orders

Binary powering supplies (O(\log N)) arithmetic gates for each power in

\[
E_N=(1+X)^N-1-X^N.
\]

Its formal derivative over (mathbb Z/Nmathbb Z) is

\[
E_N'=N(1+X)^{N-1}-NX^{N-1}=0.
\]

In characteristic (p), Frobenius gives

\[
E_N=((1+X)^q-1-X^q)^p.
\]

The inner polynomial has zero constant term and nonzero linear coefficient
(q\bmod p), so it has exact (X)-adic order one. Its (p)-th power has
exact order (p). Interchanging (p,q) gives (11) and exact order (q).

For the explicit formula modulo (p), put (d=q-p), so (1\le d<p).
Then

\[
\begin{aligned}
(1+X)^q-1-X^q
&=(1+X^p)(1+X)^d-1-X^pX^d\\
&=\sum_{j=1}^{d}\binom djX^j
  +X^p\sum_{j=0}^{d-1}\binom djX^j.
\end{aligned}
\]

Taking the (p)-th power kills mixed terms, multiplies all exponents by
(p), and fixes prime-field coefficients. It gives (12). The two exponent
ranges cannot overlap because (pd<p^2). Every (inom dj) is nonzero
modulo (p), since all factorial arguments are below (p).

Modulo (q), the inner polynomial is

\[
\sum_{j=1}^{p-1}\binom pjX^j.
\]

Its (q)-th power gives (13). No displayed (inom pj) is divisible by
(q), because (p!,j!,(p-j)!) all have (q)-valuation zero. Thus the
expansions, nonvanishing claims, disjoint exponent ranges, and exact local
orders all pass.

## 7. Numerical-QP gap recovery

V2 explicitly assumes a positive numerical-QP bound (R(n)<p). Read (R)
as integer-valued, or replace it by its integer floor. If (d<R), the true
integer (d=q-p) occurs in the enumeration (1\le\delta<R). At that value,

\[
\delta^2+4N=(q-p)^2+4pq=(p+q)^2,
\]

and the displayed formulas recover (p,q).

There are fewer than (R(n)) trials. Since (delta<R<p), every tested
integer (delta^2+4N) has (O(n)) bits. Exact square testing, addition,
and the final divisions by two have polynomial bit complexity. Hence the
total deterministic cost is

\[
O\!\left(R(n)\operatorname{poly}(n)\right),
\]

which remains numerical-QP. A returned factor pair can be multiplied to
verify it, so an accidental square at an earlier gap cannot create an
incorrect output.

The condition (R(n)<p) is part of this narrow dichotomy. It is not a
publicly verified promise in the algorithm, and V2 does not claim that the
gap branch alone factors every input. Under that conditional scope, the
complexity wording is sound.

## 8. Strict Boolean cyclic incidence

Assume (d\ge R) and (1\le r\le R<p). Because (p,q) are primes larger
than (r), multiplication by either is a permutation of
(mathbb Z/rmathbb Z).

The first sum of (12) contains nonzero source monomials at

\[
p,2p,\ldots,rp,
\]

because (r\le d). These meet every residue class modulo (r). Equation
(13) contains nonzero sources at

\[
q,2q,\ldots,rq,
\]

because (r<p), and these also meet every class. Therefore the set of
buckets receiving at least one displayed source monomial is all of
(mathbb Z/rmathbb Z) in each local expansion.

V2 claims no more. It explicitly excludes collected coefficients,
cancellation, multiplicity, source labels, and richer provenance. In
particular, it does not claim that the net coefficient in every cyclic
bucket is nonzero. The previous V1 overreach is exactly removed.

## 9. Joint modular carry interface

Equation (21) makes

\[
h=\frac{(-1)^BC-(1-q)}N
\]

an integer, and rearrangement gives

\[
q=1+hN-(-1)^BC.
\]

Thus the pair

\[
(C\bmod2^t,h\bmod2^t)
\]

determines (q\bmod2^t). If (2^t>q), its canonical representative is
the integer (q). Conversely, because (N) is odd, fixing the first
residue leaves exactly one compatible carry residue for each proposed
(q\bmod2^t):

\[
h\equiv N^{-1}\bigl(q-1+(-1)^BC\bigr)\pmod{2^t}.
\]

V2 correctly limits this last statement to the displayed congruence. It
claims neither an information lower bound nor an evaluator for either
coordinate.

The joint interface repairs the V1 sufficiency gap. A public valid choice is
(t=n), because the project definition of input length gives
(2^n\ge N+1>q). Both returned residues then have (O(n)) bits. One modular
multiplication, addition, and canonical reduction recover (q) in
polynomial additional bit time. No exact output of the exponentially large
integer (h) is requested.

## 10. Audit of every stated sufficient primitive

The three final interfaces are sufficient under the ordinary uniform,
factor-free reading of “compute” or “recover”:

1. If a QP routine computes
   (igl((-1)^BC-1\bigr)\bmod N), Euclid's algorithm returns (q) from
   (3) in polynomial additional bit time. The phrase “the residue in (3)” is
   slightly informal because (3) is written as a gcd, but the intended
   signed-shift residue is unambiguous from context.
2. If one QP routine computes both residues in (15) for the public choice
   (t=n), Section 9 recovers and verifies (q) with polynomial overhead.
   A carry-only evaluator would not suffice, but V2 no longer claims one.
3. The two exact local orders proved in Theorem 4 are the integers (p) and
   (q). A routine that, from the public input (N) and its public circuit,
   returns either order has returned a nontrivial factor. This clause must be
   read as a factor-free black-box interface. If the routine were instead
   handed the hidden projection modulo (p) or (q), the interface would be
   circular. V2 supplies no such routine and makes no hidden-access claim.

Each interface is conditional. None is presented as an existing algorithm,
and none upgrades the result to factoring arbitrary composites.

Finally, (B=\lfloor\sqrt N\rfloor=2^{\Theta(n)}), so direct truncation
through degree (B) really does store (B+1=2^{\Theta(n)}) coordinates.
This is a count for that explicit representation only. V2 makes no time
lower bound for all algorithms and has removed V1's unsupported claim about
ordinary holonomic methods.

## 11. Final disposition

The false V1 inequality, undefined provenance language, missing numerical
bound on (R), carry-only interface, and unsupported holonomic-method phrase
are all substantively repaired. The full mathematical V2 statement and
proof pass hostile reconstruction at their declared balanced-semiprime
scope.

The exact frozen package fails solely because its provenance says there are
four listed repairs when the cited self-audit lists five. Any correction to
that frozen statement must be preserved as a new version rather than edited
into V2.
