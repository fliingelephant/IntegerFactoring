# F194 hostile audit

## Frozen-input verification

The manifest declares these three inputs. Their observed SHA-256 digests
match byte for byte:

| Frozen input | Manifest SHA-256 | Observed SHA-256 | Result |
|---|---|---|---|
| `STATEMENT.md` | `d5ec288bb9b4f4e3fbf5cdad9c51bbcc1fb7d8560f9dd2c5a7b45c698a9ebd25` | `d5ec288bb9b4f4e3fbf5cdad9c51bbcc1fb7d8560f9dd2c5a7b45c698a9ebd25` | match |
| `PROOF.md` | `ac2f813a83a4c499aeda1defec5a1445b09bc1e94c24ce1b5048753116afc29a` | `ac2f813a83a4c499aeda1defec5a1445b09bc1e94c24ce1b5048753116afc29a` | match |
| `SELF_AUDIT.md` | `8fe673fbfba9116bed3444c0ad0133a80df943c3ce15439d06958a7cc5260cdf` | `8fe673fbfba9116bed3444c0ad0133a80df943c3ce15439d06958a7cc5260cdf` | match |

All three files were then read in full.

## Exact verdict

**FAIL — the frozen candidate is not promotion-ready.**

The numbered algebraic identities can be reconstructed under the balanced,
distinct-odd-semiprime promise. However, the frozen proof contains a false
inequality in the proof of Theorem 2. In addition, three concluding boundary
claims are not established with the precision or complexity hypotheses that
their wording requires. These are defects in the frozen version. The fact
that the false inequality has a short replacement does not turn this audit
into a pass; inserting that replacement would be a new version.

The promotion-blocking findings are:

1. In Section 3 of `PROOF.md`, the chain

   \[
   B+1<2p\le q+1
   \]

   is false in general. The promise says (q<2p), essentially the opposite
   comparison. For the permitted input (p=11,q=17), one has
   (B=\lfloor\sqrt{187}\rfloor=13>p), while (2p=22>18=q+1).
   The conclusion (2m<q) is true, but the written proof reaches it through
   a false assertion. A valid independent derivation is recorded below only
   to classify the defect; it is not silently substituted into the frozen
   proof.

2. Full source support in every cyclic bucket proves equality of Boolean
   support sets. It does not, without a definition of the observation model,
   prove that “provenance alone cannot separate” anything. Provenance can
   retain multiplicity, source labels, or pre-alias information. “Cyclic
   sketch,” “provenance,” and “separate” are not defined. The exact support
   incidence claim is valid; the stated provenance impossibility is not a
   formal consequence of it.

3. Testing (R) gaps costs (O(R)) trials, up to polynomial factors in the
   input bit length. It is QP only if the *numerical value* of (R) is QP in
   the input length. The statement does not formally impose that bound when
   it states the dichotomy, and “QP-size cyclic sketch” is not defined well
   enough to supply it retroactively.

4. The carry corollary proves recovery from the pair
   ((h\bmod 2^t,C\bmod 2^t)). It does not prove that an evaluator for
   (h\bmod2^t) alone is a factoring primitive, because no QP procedure for
   (C\bmod2^t) is supplied. An exact evaluator for the integer (h) cannot
   be what is meant: (h) has exponentially many output bits. The final
   “therefore” must specify a modular carry interface and either include the
   coefficient residue in that interface or prove it separately accessible.

The first item alone forces the hostile-audit verdict. The remaining items
prevent the informal boundary language from being promoted as a proved
algorithmic limitation or sufficient QP interface.

## 1. Balance and exact numerical ranges

From (p<q<2p),

\[
p^2<pq<2p^2.
\]

Taking square roots and then using (B=\lfloor\sqrt N\rfloor) gives

\[
p\le B<\sqrt2,p<2p.
\]

Also (sqrt{pq}<q), because (p<q), so (B<q). Hence among
(1,\ldots,B), the only positive integer divisible by either hidden prime
is (p): (q>B), and (2p>B).

These inequalities are valid for all inputs in scope. They do not extend to
unbalanced semiprimes or prime powers.

## 2. Exact one-jump cancellation

For (kle B), the exact integer identity is

\[
k!A_k=\prod_{i=1}^k(i-N).
\tag{A1}
\]

If (k<p), all (i) are units modulo (N). Dividing only by those units
in (mathbb Z/Nmathbb Z) gives

\[
A_k=\prod_{i=1}^k (i-N)i^{-1}\equiv1\pmod N.
\]

Now suppose (p\le k\le B), and put

\[
U=\prod_{\substack{1\le i\le k\\i\ne p}}i,
\qquad
V=\prod_{\substack{1\le i\le k\\i\ne p}}(i-N).
\]

The range proved above makes (U) a unit modulo (N). Isolating the one
nonunit in (A1) gives the equality in (mathbb Z)

\[
pUA_k=(p-N)V=p(1-q)V.
\]

Cancellation of (p) occurs in the integers, before reduction:

\[
UA_k=(1-q)V.
\]

Only now reduce modulo (N). Since (V\equiv U\pmod N) and (U) is a
unit,

\[
A_k\equiv1-q\pmod N.
\]

Thus the proof does not divide by the zero divisor (p) modulo (N).
The post-jump value and the claimed uniqueness of the jump are correct on
the declared prefix.

The recurrence also checks exactly. From the ratio of adjacent binomial
coefficients,

\[
(k+1)A_{k+1}=-(N-1-k)A_k=(k+1-N)A_k,
\]

so

\[
(k+1)(A_{k+1}-A_k)=-NA_k.
\]

At the transition (k+1=p), the exact integer division exposes the factor
(N/p=q). This is a mechanism statement, not an efficient method for
jumping directly to the remote coefficient.

## 3. AKS coefficients, alternating sign, and the endpoint gcd

For (1\le k\le B),

\[
k\binom Nk=N\binom{N-1}{k-1}.
\]

If (k\ne p), then (k) is a unit modulo (N), and hence
(inom Nk\equiv0\pmod N). If (k=p), exact integer cancellation gives

\[
\binom Np=q\binom{N-1}{p-1}.
\]

Because (p-1) is even and lies before the jump,

\[
\binom{N-1}{p-1}=A_{p-1}\equiv1\pmod N,
\]

so the exceptional coefficient is (q), not (-q).

The alternating-prefix identity

\[
\sum_{k=0}^{B}(-1)^k\binom Nk=(-1)^B\binom{N-1}{B}
\]

leaves the terms at (k=0) and (k=p). Since (p) is odd, their sum is
(1-q). Therefore

\[
(-1)^B C\equiv1-q\pmod N,
\qquad C=\binom{N-1}{B}.
\]

It follows that ((-1)^BC-1\equiv-q\pmod{pq}). This integer is divisible
by (q), and after division by (q) it is congruent to (-1) modulo (p).
Its gcd with (N) is therefore exactly (q).

For odd (B), (C\equiv q-1\pmod N). For even (B),
(C\equiv1-q\equiv N-q+1\pmod N). Both representatives lie in
([0,N)), so the canonical-residue formula and all signs are correct.

Conversely, the AKS prefix implies the one-jump word through the same
alternating-prefix identity at every (k\le B). Thus “equivalently” is
valid within the declared range.

## 4. Both central-binomial gcds

Let (m=\lceil B/2\rceil). The safe derivation, independent of the false
line in the frozen proof, is:

\[
m\le\frac{B+1}{2}<p,
\qquad
p\le B\le2m.
\]

The strict first inequality follows from
(B<\sqrt2p) and (sqrt2p+1<2p) for odd (p\ge3).
Furthermore, (2m\le B+1\). Since (B<q) and both are integers,
(B+1\le q). Equality (2m=q) is impossible because (2m) is even and
(q) is odd. Hence

\[
m<p\le2m<q.
\tag{A2}
\]

This establishes the theorem's inequality, but it is not the argument
written in the frozen proof.

In

\[
\binom{2m}{m}=\frac{(m+1)\cdots(2m)}{m!},
\]

the denominator is coprime to (N). By (A2), the numerator contains exactly
one multiple of (p), namely (p), and no multiple of (q). Thus its
(p)-adic valuation is one and its (q)-adic valuation is zero. Because
(N=pq) is squarefree,

\[
\gcd\!\left(N,\binom{2m}{m}\right)=p.
\]

For the second binomial coefficient, (B!\) contains exactly the one
multiple (p), and no multiple of (q). The numerator interval
([B+1,2B]) contains (2p), because (B<2p\le2B), and contains (q),
because (B<q<2p\le2B). It contains no second multiple of (q), since
(B<q) implies (2B<2q). It contains no additional multiple of (p):

\[
2B<2\sqrt2,p<3p.
\]

Thus the numerator and denominator have equal (p)-adic valuation one,
while the numerator has one unmatched factor (q). Consequently

\[
\gcd\!\left(N,\binom{2B}{B}\right)=q.
\]

Both gcd identities are mathematically correct. The hostile defect is the
false intermediate inequality in their frozen proof, which the self-audit
did not detect.

## 5. Polynomial-moment collapse

For every (W\in\mathbb Z[T]), polynomial division by the monic polynomial
(T) gives another integer polynomial (V) with

\[
W(T)-W(0)=TV(T).
\]

Therefore

\[
\begin{aligned}
\sum_{k=1}^{N-1}(W(k)-W(0))\binom Nk
&=\sum_{k=1}^{N-1}kV(k)\binom Nk\\
&=N\sum_{k=1}^{N-1}V(k)\binom{N-1}{k-1},
\end{aligned}
\]

which is divisible by (N) in the integers. The remaining constant part is

\[
W(0)\sum_{k=1}^{N-1}\binom Nk=W(0)(2^N-2).
\]

Equation (8) follows without a degree bound. This is an algebraic identity,
not an algorithmic lower bound. “Any succinct description” is harmless only
in that identity sense; no representation model or evaluation complexity for
a succinctly described high-degree (W) is proved.

## 6. Circuit, derivative, Frobenius identities, and exact local orders

Repeated squaring constructs ((1+X)^N) and (X^N) with (O(\log N))
arithmetic-circuit gates. Formal differentiation gives

\[
E_N'(X)=N(1+X)^{N-1}-NX^{N-1}=0
\]

in ((\mathbb Z/N\mathbb Z)[X]).

In characteristic (p), Frobenius additivity gives

\[
\begin{aligned}
E_N
&=((1+X)^q)^p-1-(X^q)^p\\
&=((1+X)^q-1-X^q)^p.
\end{aligned}
\]

The inner polynomial has zero constant coefficient and linear coefficient
(q\not\equiv0\pmod p). Its exact (X)-adic order is one, and its
(p)-th power has exact order (p). The same argument modulo (q), with
linear coefficient (p\not\equiv0\pmod q), gives exact order (q).

For the explicit expansion modulo (p), let (d=q-p). The promise gives
(1\le d<p). In characteristic (p),

\[
\begin{aligned}
(1+X)^q-1-X^q
&=(1+X^p)(1+X)^d-1-X^pX^d\\
&=\sum_{j=1}^{d}\binom djX^j
  +X^p\sum_{j=0}^{d-1}\binom djX^j.
\end{aligned}
\]

Raising to the (p)-th power multiplies every exponent by (p), kills all
mixed terms, and leaves prime-field coefficients fixed. The two exponent
ranges are disjoint because (pd<p^2). This gives exactly (12).

Modulo (q),

\[
(1+X)^p-1-X^p=\sum_{j=1}^{p-1}\binom pjX^j,
\]

and the (q)-th power gives exactly (13). For (12), no
(inom dj) is divisible by (p), because all factorial arguments are
less than (p). For (13), no (inom pj) is divisible by (q), because
the (q)-adic valuations of (p!,j!,(p-j)!) are all zero. Thus every
displayed coefficient is nonzero in the stated local field. Equations
(10)--(13) and both exact order claims pass reconstruction.

## 7. Cyclic support and the bounded-gap branch

Assume (r,R) are positive integers with (r\le R<p). Coprimality with
(N=pq) is automatic, so multiplication by either (p) or (q) permutes
(mathbb Z/rmathbb Z).

If (d\ge R), equation (12) contains the nonzero source terms with exponents

\[
p,2p,\ldots,rp,
\]

because (r\le d). These exponents meet every residue class modulo (r).
Equation (13) contains the nonzero source terms

\[
q,2q,\ldots,rq,
\]

because (r\le R<p), and they also meet every residue class. Hence the
Boolean source-support set of each local expansion is all of
(mathbb Z/rmathbb Z). This exact incidence statement is correct. It
does not assert that the *sum* in every bucket is nonzero; cancellation can
occur.

If (d<R), enumerate (delta=1,\ldots,R-1). At (delta=d),

\[
\delta^2+4N=(q-p)^2+4pq=(p+q)^2.
\]

An exact square root then recovers

\[
p=\frac{\sqrt{\delta^2+4N}-\delta}{2},
\qquad
q=\frac{\sqrt{\delta^2+4N}+\delta}{2}.
\]

Every trial has bit complexity polynomial in (n+\log R), but there are
(R-1) trials. Thus the total is

\[
O\!\left(R\,\operatorname{poly}(n+\log R)\right).
\]

This is numerical-QP in (n) only under a numerical-QP bound on (R).

Nothing in the full-support proof excludes a sketch that retains source
multiplicity, source identities, coefficients, or cancellation data. In
particular, the word “provenance” normally suggests more than a Boolean
support set. The frozen claim must be narrowed to Boolean support, or a
formal sketch interface and indistinguishability statement must be supplied.
The sentence as written is not a proved lower bound.

## 8. Signed quotient carry

The congruence

\[
(-1)^BC\equiv1-q\pmod N
\]

does prove that

\[
h=\frac{(-1)^BC-(1-q)}N
\]

is an integer. Rearrangement gives

\[
q=1+hN-(-1)^BC.
\]

Since (N) is odd, it is invertible modulo (2^t). Thus residues of both
(h) and (C) determine (q\bmod2^t), and (2^t>q) makes the canonical
residue equal to the integer (q).

For fixed (C\bmod2^t), every proposed residue (widetilde q) does indeed
give one and only one compatible carry residue,

\[
\widetilde h\equiv
N^{-1}\bigl(\widetilde q-1+(-1)^BC\bigr)\pmod{2^t}.
\]

This proves only that the displayed linear congruence, with an unrestricted
hidden (h), has full projection onto the (q)-coordinate. It does not
prove an unconditional information or computational lower bound for
(C\bmod2^t), and it does not follow merely from this compatibility that no
other relation involving that residue can constrain a factor. The phrase
“does not constrain (q)” must be read in this limited algebraic sense.

The size issue is material. The canonical-residue formulas show more
explicitly that, for some integer (a\ge0),

\[
\begin{array}{c|c|c}
 & C & h\\ \hline
B\text{ odd} & aN+q-1 & -a\\
B\text{ even} & aN+N-q+1 & a+1.
\end{array}
\]

Thus (|h|) is of order (C/N). Here (B=2^{\Theta(n)}), and the standard
bound

\[
\binom{N-1}{B}\ge\left(\frac{N-1}{B}\right)^B
\]

shows that (C), and hence (h), has (2^{\Theta(n)}) bits (up to the
irrelevant small instances). An algorithm cannot output exact (h) in QP
bit complexity. A viable interface must ask for only (h\bmod2^t), with
(t=O(n)).

But the proved recovery uses (C\bmod2^t) as a second input. The candidate
does not give or analyze an algorithm for obtaining this residue in QP time.
Therefore its final assertion that a QP evaluator for the carry (14) is
“the surviving positive primitive” does not follow as a standalone factoring
reduction. A precise revised claim could be conditional on a joint evaluator
for the two residues, or could add a proved QP evaluator for the coefficient
residue. That revision is not present in the frozen candidate.

## 9. Scope and complexity disposition

The following statements survive exactly as algebraic claims under the
balanced distinct-odd-semiprime promise:

- the one-jump word, exceptional AKS coefficient, sign, endpoint gcd, and
  canonical residue;
- both central-binomial gcd identities;
- the polynomial-moment identity;
- the (O(\log N))-gate powering representation, zero derivative, local
  Frobenius identities, explicit expansions, coefficient nonvanishing, and
  exact local (X)-adic orders;
- full Boolean source support in the cyclic buckets when (d\ge R\);
- bounded-gap recovery in (O(R\operatorname{poly}(n+\log R))) bit time;
- the signed-carry congruence and conditional two-residue recovery.

None of these supplies a QP evaluator for the remote coefficient, a QP
factoring algorithm even for all balanced semiprimes, or an all-input
factoring theorem. The candidate correctly disclaims those results.

The statements that “ordinary baby-step/giant-step product or holonomic
methods remain exponential” and that “standard truncation” has a specified
cost are contextual rather than proved model-specific theorems. The raw
truncation statement is justified because (B=\Theta(\sqrt N)=2^{\Theta(n)}).
The broader method claim has no formal definition, algorithm, or cost
analysis and cannot carry verifier-backed status. Likewise, no lower bound
against a different succinct evaluator follows.

Because the candidate is frozen, the false Section 3 inequality and the
overbroad interface language must be preserved as findings and addressed in
a new version. They cannot be repaired inside this audit.
