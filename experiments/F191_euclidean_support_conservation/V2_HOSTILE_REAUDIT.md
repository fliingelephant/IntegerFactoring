# F191 V2 hostile re-audit

## Strict verdict

**PASS.** V2 repairs every defect in the preserved V1 hostile audit. The
exact support law, balanced counterexample, and finite permutation-bank
theorem remain correct. The repaired roughness-cap quantifier is
noncircular, and the repaired direct interface supplies exactly the public
positive, short support-covering list required by P163.

This verdict is only for the stated named-model obstruction. It does not
promote the permutation model to the actual P164 transcript. It does not
close the P164-to-P163 branch or prove a factoring lower bound.

## Frozen-file integrity

Every hash in `V2_MANIFEST.md` matches its frozen file:

- `V2_STATEMENT.md`:
  `4666ed13b2318932a357c5a35ef4021c83355bf78cfeab3ffa1eb7bd6c8ac9ce`
- `V2_PROOF.md`:
  `807d7c7e30ec7950e083bd9624050a1859fe724ce74843bcb16b64f3b184ca39`
- `V2_SELF_AUDIT.md`:
  `6ef91e68f5bd64ef3640049b07cf9132306ce6fa706933065cdcfb18afe8f275`
- `V2_PROVENANCE.md`:
  `105a343c01b27abf467cf740d080af6bae012f754315988c6f2e491562ba753e`

The preserved V1 files still match `MANIFEST.md` and the hashes repeated in
`V2_PROVENANCE.md`:

- `STATEMENT.md`:
  `6747d7c6b121565bb1cbabb0041f7f11cb1f2f3306eb27beb126f3e4714bb124`
- `PROOF.md`:
  `21dfd6a74efc318434f54f5c7575b10c9d299b8e315459d20fd9643410cef455`
- `SELF_AUDIT.md`:
  `1bd8c60477f4bb8ccba50923e129333c0b48c5bf23312a21ac7ea1457c7ab7a5`

The preserved V1 hostile audit also remains unchanged:

- `HOSTILE_AUDIT.md`:
  `d3ae15732f7f1beccd1d5a9c37cabf2a8ab11d821069822b7e7f69755ee2de69`

Hashing was the only machine computation used.

## Exact support law and the zero divisor

From

\[
X=QD+R,
\qquad
\ell\mid X,
\]

one gets

\[
R\equiv-QD\pmod\ell.
\]

When \(\ell\nmid D\), multiplication by \(D\) is invertible modulo the
prime \(\ell\). Therefore

\[
\ell\mid R
\quad\Longleftrightarrow\quad
\ell\mid Q.
\]

No size, sign, representation, or Euclidean-choice premise is hidden in
this equivalence.

When \(\ell\mid D\) and \(D\ne0\), \(D\) has \(\ell\)-support. V2 now
separates that support fact from direct P163 admission. It requires
\(0<|D|<N/2\) for the latter. When \(D=0\), V2 makes no carrier claim for
the zero divisor. The identity becomes \(X=R\), and the pre-existing value
of \(R\) gains no new localization property. The V1 zero-divisor hole is
closed.

## Balanced \(X=N+c\) counterexample

The balanced representative of \(-N\bmod\ell\) is nonzero because
\(\gcd(\ell,N)=1\). For odd \(\ell\), it is unique and satisfies

\[
0<|c|\le(\ell-1)/2<\ell/2<N/4.
\]

Thus \(X=N+c\) is an exact \(\ell\)-multiple and its unique centered
decomposition is

\[
X=1\cdot N+c.
\]

Both child magnitudes are nonzero and below \(N/2\). Neither child is
divisible by \(\ell\). The example has no endpoint, sign, or uniqueness
gap.

## Nearest-quotient and finite-bank audit

For one permutation, counting \(u\) is exactly the same as counting
\(b\in\{0,\ldots,N-1\}\). Odd \(N\) excludes a nearest-integer tie: an
equality

\[
2\ell b=(2t+1)N
\]

would equate an even integer with an odd integer. Since
\(0\le\ell b/N<\ell\), the centered quotient lies in
\(\{0,\ldots,\ell\}\).

The support law makes the quotient and remainder exceptional sets equal,
not merely equinumerous. In the quotient range, divisibility by \(\ell\)
occurs exactly at \(Q=0\) and \(Q=\ell\). These cases are exactly

\[
0\le b<N/(2\ell)
\quad\text{and}\quad
N-N/(2\ell)<b<N.
\]

The strict endpoints are correct because ties do not occur. Each interval
contains at most \(N/(2\ell)+1\) integers. Hence one selector has at most
\(N/\ell+2\) exceptional parameters.

No independence premise enters the bank argument. The union bound gives

\[
B(N/\ell+2)\le N/4+N/4=N/2<N
\]

from \(\ell\ge4B\) and \(N\ge8B\). A parameter outside the union exists.
For that parameter, every quotient avoids both endpoints, so

\[
1\le Q_i\le\ell-1<N/2.
\]

Every centered remainder is nonzero, since a zero remainder would be in
the exceptional set, and it satisfies \(0<|R_i|<N/2\). Thus the selected
children fail only in support. They do not fail through a zero or size
loophole.

## Hidden prime-power size argument

Let \(p^e\) be a maximal hidden prime-power component and let \(g\) be a
P161 local order. The promoted P161 contract gives \(\gcd(g,N)=1\), hence
\(p\nmid g\). The kernel of

\[
(\mathbb Z/p^e\mathbb Z)^\times
\longrightarrow
(\mathbb Z/p\mathbb Z)^\times
\]

is a \(p\)-group. Its intersection with the cyclic subgroup of order
\(g\) is therefore trivial. Reduction preserves that subgroup's order, so
\(g\mid p-1\). Every prime \(\ell\mid g\) satisfies \(\ell\le p-1\).

If another maximal prime-power component is present, its odd cofactor is at
least three, so \(p\le N/3\). If \(N=p^e\) with \(e\ge2\), then
\(p\le\sqrt N<N/2\). In both cases

\[
\ell<N/2.
\]

This argument uses exactly the promoted P161 coprime-order premise. It does
not assume that the full unit group modulo \(p^e\) injects into the prime
field.

## Roughness-cap quantifiers and QP bounds

V2 fixes the integer-valued numerical-QP budget \(B_\star(n)\) before it
chooses the P161 cap, and requires the budget to be independent of that cap.
The bound

\[
B_\star(n)\le2^{c(\log_2(n+2))^C}
\]

is numerical QP. Therefore \(T(n)=4B_\star(n)+1\) is also numerical QP
and is an admissible P161 cap. For \(B\le B_\star(n)\), every surviving
order prime obeys

\[
\ell>T(n)>4B_\star(n)\ge4B.
\]

Together with \(\ell<N/2\), this gives \(N>2\ell>8B\). There is no
backward dependence on \(T\).

For a cap-dependent budget \(B_\star(n,T)\), V2 does not infer a fixed
point. It states the result only under the separate premise that a public
numerical-QP function \(T(n)\) is exhibited with

\[
4B_\star(n,T(n))<T(n).
\]

That premise is exactly what the finite-bank inequalities need. The V1
quantifier defect is closed without an unsupported asymptotic claim.

## Exact P163 admission

The promoted P163 interface requires a public QP support-covering list whose
nonunit entries have at most \(n-1\) bits. V2 requires a public list, at
total numerical-QP cost, with

\[
0<|A_j|<N/2
\]

for every entry and with support coverage for every surviving local-order
prime. Since \(n=\lceil\log_2(N+1)\rceil\), one has \(N<2^n\), and hence

\[
|A_j|<N/2<2^{n-1}.
\]

Thus every nonunit \(|A_j|\) has at most \(n-1\) bits. Absolute values
preserve rational-prime support. Unit entries can be removed. These
conditions are sufficient for direct P163 admission, with no missing sign,
zero, length, list-size, or construction-cost premise.

V2 also states the complementary boundary correctly. A divisible but zero
or oversized quotient or carry is not a direct P163 input. It needs a
separate numerical-QP support-preserving localization theorem.

## Scope and repair boundary

The finite theorem assumes permutations of the full parameter set. It does
not claim the same count for a nonpermutation map concentrated in the two
endpoint intervals. It also does not claim that the actual P164 transcript
has the permutation property. V2 expressly leaves correlated floor
concentration, non-Euclidean selectors, and direct factor or common-order
constructions open.

A textual comparison with frozen V1 shows no change to the exact congruence
argument, balanced example, endpoint count, union-bound constants, or valid
child bounds. Apart from equation renumbering and clarifying wording, V2
changes only the defects identified by the V1 audit:

1. it excludes \(D=0\) as a carrier;
2. it requires the exact P163 nonzero and size bounds;
3. it requires a separate localization theorem for unrestricted values;
4. it orders \(B_\star\) before \(T\), or makes uniform dominance an
   explicit premise.

No new model claim or unaudited bridge was added.
