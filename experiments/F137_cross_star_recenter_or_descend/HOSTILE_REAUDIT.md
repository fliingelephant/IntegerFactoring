# F137 corrected hostile re-audit — PASS

## Verdict

**PASS.** The corrected frozen statement and proof fix every objection in
`HOSTILE_AUDIT_FAILED.md`. A fresh hostile audit found no counterexample,
missing hypothesis, or scope overclaim.

Audited frozen hashes:

- `STATEMENT.md`:
  `2126e93be2be3abbca52ccb46615d3be8a2319c4dd064d8a5fa7705cd8084098`
- `PROOF.md`:
  `2f973e801b849693d9f5f0951556bb6978eb6f4e0236387b17fc38a686deeecc`

The accepted result is conditional and pathwise. It is not a closure theorem
or a factoring algorithm.

## Repairs from the failed audit

All earlier failures are repaired.

1. The parent now has an explicit eligible anchor \(\ell\). The inequalities
   \(\ell q<N\) and \(0<H/\ell<N\) make its endpoint presentation canonical.
2. The released block now satisfies \(r<N/C\). Every eligible child anchor
   \(a\le C\) therefore has \(ar<N\), while its induced coendpoint is also
   below \(N\).
3. Operational claims quantify only the digits actually emitted by eligible
   child anchors. The quotient digit \(j\) is explicitly virtual and need not
   occur.
4. If an observed child arm repeats the old exact value, both endpoint sign
   screens run before exact-value deduplication.
5. The statement defines \(n\), attributes the carry-remainder law to
   P70/P80, and restricts the increment to recentering, overlap, and
   two-step contraction.

## Independent algebraic reconstruction

From \(r(qS)=1+KN\) and \(qS=jN+t\), with \(1\le t<N\),

\[
rt\equiv1\pmod N.
\]

All divisors of \(H\) are units modulo \(N\), so inverse uniqueness gives
\(t=\iota_N(r)\). If \(rt=1+k_rN\), exact coefficient comparison gives

\[
K=jr+k_r,
\qquad
1\le k_r<r.
\]

Thus \(j=\lfloor K/r\rfloor\) and \(k_r=K\bmod r\). Also,

\[
qS=t+jN=H'_j.
\]

Since \(qS\) is coprime to \(N\), for every \(b\ne j\),

\[
\gcd(qS,H'_b)
=\gcd(qS,N(b-j))
=\gcd(qS,b-j)
\le |b-j|.
\]

If \(j<C\), every different observed digit lies in \([0,C-1]\), so this
gcd is strictly below \(C\). If \(j\ge C\), then

\[
Cr\le jr<K=k+Aq<Cq,
\]

which proves \(r<q\).

## Canonical child positions and duplicate screens

For an eligible child anchor \(a\), the unique digit \(b_a<a\) satisfies
\(a\mid t+b_aN\). The bounds

\[
ar<N,
\qquad
0<t+b_aN<aN
\]

put both child endpoints in \(\{1,\ldots,N-1\}\). Their product is
\(r(t+b_aN)\equiv1\pmod N\), so these are genuine canonical source
positions. If \(b_a=j\), the exact value equals the parent value, but the
statement correctly retains and screens the endpoint presentation first.

## Two-step contraction and path bound

For a large-quotient transition \(q_0\to q_1\), let
\(\delta=q_0-q_1>0\). The first carry obeys

\[
k_1<C\delta.
\]

If \(\delta\ge q_0/(C+1)\), the first step already reaches
\(q_1\le Cq_0/(C+1)\), and the second large step strictly decreases again.
Otherwise the second digit \(A_1\le C-1\) gives

\[
Cq_2
\le j_1q_2
<k_1+A_1q_1
<C\delta+(C-1)q_1,
\]

and substitution yields

\[
q_2<\frac{C}{C+1}q_0.
\]

Pairing transitions in an all-large path and using
\(\log(1+1/C)\ge1/(C+1)\) gives \(O(C\log N)\) steps. The statement
correctly says that this does not control branching or paths interrupted by
small-quotient recentering.

## Independent finite checks

An independent exact-integer enumeration covered all valid operational
transitions for

\[
3\le N\le250,
\qquad
2\le C\le10.
\]

It checked 210,755 one-step transitions and 36,285 consecutive
large-quotient pairs. It verified parent and child canonicality, inverse and
carry identities, observed-digit overlap, strict descent, and two-step
contraction. No counterexample occurred.

The \(N=143\) certificate was recomputed. Both parent arms are canonical,
both released blocks satisfy the cutoff, all displayed quotients and carries
are exact, and the duplicate child endpoints \((95,140)\) have

\[
\gcd(95-140,143)=
\gcd(95+140,143)=1.
\]

## Accepted scope

F137 proves an exact conditional law for one release-and-reanchor transition
and a contraction law for two consecutive large-quotient transitions. It
does not bound the full adaptive transcript, force a parity cycle, control
the normalized-root image, or factor every input. The novelty language is
limited to the internal increment beyond P70/P80 and P122; it makes no
publication-level literature claim.
