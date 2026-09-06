# F280 V2 fresh hostile proof and literature-composition audit

## Verdict

**STRICT PASS.** The additive V2 overlay repairs the sole V1 formal defect.
The polynomial-\(N\) Harvey--Hittmeir comparison is now restricted to one
fixed \(0<\delta<1\). In that range the source theorem is admissible for all
sufficiently large integer inputs, and both displayed substituted costs are
valid upper bounds. V2 makes no claim for \(\delta\geq1\).

The numerical-quasipolynomial conclusion, both all-input source interfaces,
the local gcd composition, the synchronized-order result, the counterexample,
and every stated project-lane boundary survive fresh review. This verdict is
not inherited from the V1 hostile audit.

V1 remains an immutable failed packet. This audit does not reclassify V1 and
does not promote V2.

## Authentication

I authenticated `V2_FROZEN.sha256` before reading the V2 mathematical files.
The observed root was exactly

```text
9a451b1c294c770d8c7f936bd9ad8d5f34abe2b002eabf81274a2349bfc95f76  V2_FROZEN.sha256
```

Every listed V2 entry matched:

```text
36d2323aa63822f23b55b5daa5aa98032592a4c3112040ab6d4bb33427143083  V2_STATEMENT.md
9d4e1a7d57c8fe2023f38e83cb42044f0b08d5852145c370b4edd18d2b9c94ab  V2_PROOF.md
70207ee037ae0f6fe1f012e92fc4acfbb3662dc9ec6e494433685ea9d5c1b757  V2_SELF_AUDIT.md
80c3fe363f9552845c816b9dc1c9d03bb5471675ad3008e3289658794f0731d6  V2_PROVENANCE.md
7863c2f8a02c40b942997db49453ab3896548c2d5da24c06d528c8ce6ae0cb56  V2_MANIFEST.md
```

I then authenticated the imported V1 root and every V1 entry:

```text
a3ecad88c09874a5fcbbe5025596561910aeb5330dbe91206fabc2d49d7965db  FROZEN.sha256
0d4a9ad469b961855cf77518b29926dfecaf958884a85b73e17f0ebf6f75016d  STATEMENT.md
6a7871d91a5bd44eb08778633b04f7f0239ded8ca95392481bd6059491c006df  PROOF.md
4dce3fe66ffbfeda0b4aaea0d47522631633d638ca93266120b5cfbf038a44e2  SELF_AUDIT.md
f36a8927e905a8a1c6bf61f8477be50b7b3458a480c271200b8b9a7a485b9733  PROVENANCE.md
818aefe8ae8d13488d4b730881962e48f2b5a403b6bcc8695aca178eca50c85d  MANIFEST.md
```

The separately preserved V1 hostile audit also matched its immutable anchor:

```text
57292f18bea502f64b50639361492bab6e441a8b339f583658a654998a687533  HOSTILE_AUDIT.md
```

I read the authenticated V1 and V2 statement, proof, self-audit,
provenance, manifest, and V1 hostile-audit files in full.

## Primary-source authentication and review

Authenticated local copies of both cited versioned PDFs were available. No
remote access was used.

```text
0e957bacebc0b74f363436ab09b70085f4ad83c45dee93bda8aef19fbfdcbff0  arXiv:2601.11131v2
f3100236ec455410b657e2cb9a2983d4e0120232d102a571dcc61611a94d4fb1  arXiv:2605.09592v1
```

The Harvey--Hittmeir PDF has 412025 bytes and 13 pages. Its embedded arXiv
record is v2 dated 5 June 2026. Its title and authors match the packet. The
Nir PDF has 293158 bytes and 8 pages. Its embedded arXiv record is v1 dated
10 May 2026. Its title and author match the packet.

Direct inspection confirms the following exact interfaces.

1. Harvey--Hittmeir Theorem 1.1 accepts integers \(N\geq3\) and
   \(1\leq D<N-1\). It deterministically returns a nontrivial divisor or a
   unit of global order greater than \(D\), with the packet's time bound,
   small-\(D\) convention, and stated space bound.
2. Harvey--Hittmeir Lemma 2.1 gives the exact bounded-order search. Lemma
   2.3 gives the rational-prime local-order screens. Lemma 2.2 combines
   known factored orders into their lcm order. Algorithm 3.1 can return a
   small scanned base or an lcm-combined residue. The source does not state
   a theorem-wide ordinary-height bound \(D^{O(1)}\).
3. Nir Theorem 1.1 has the strict threshold
   \(D>\exp\sqrt{2\log N\log\log N}\), the factor/unit/prime trichotomy,
   and time \(O(D^{1/2+o(1)})\).
4. Nir Proposition 1.2 accepts every pair of positive integers \(D<N\),
   has the same three outcomes, and takes
   \(O(D^{5/2+o(1)}\operatorname{polylog}N)\) time. Its proof scans the
   ordinary integers \(2,\ldots,D^2+D\), so a high-order output has exactly
   the height bound used by F280.

## Exact endpoint repair

Let \(D=N^\delta\) for one fixed \(0<\delta<1\), subject to the standing
integer-input convention. Then

\[
 \frac{D}{N-1}
 =\frac{N^{\delta-1}}{1-1/N}
 \longrightarrow0.
\]

Thus \(1\leq D<N-1\) for every sufficiently large admissible input. This is
the exact Harvey--Hittmeir domain condition. At \(\delta=1\), \(D=N\); for
\(\delta>1\), \(D>N\). Those cases are outside the cited algorithm and are
explicitly excluded by V2.

Substitution into the authenticated source bound gives

\[
 O\!\left(
 N^{\delta/2}
 \frac{\log(N^\delta)}{\sqrt{\log\log(N^\delta)}}
 \log N
 \right)
 =N^{\delta/2+o(1)}.
\]

With \(n=\Theta(\log N)\) and standard fast deterministic integer
arithmetic, the explicit local scan has cost

\[
 O(D\mathsf M(n)\log n)=N^{\delta+o(1)}.
\]

Both are upper-bound accounting statements for the named constructions.
Neither is a lower bound. V2 does not silently extend the source formula to
an inadmissible parameter.

`V2_STATEMENT.md` identifies the unique V1 Section 5 comparison block and
supplies its complete replacement. `V2_PROOF.md` does the same for the
terminal comparison in V1 Proof Section 4. The old \(\delta>0\) text appears
in V2 only as an authenticated replacement anchor or historical description;
it is not normative V2 content.

## Composition and theorem checks

For a source-certified unit \(a\) with \(\operatorname{ord}_N(a)>D\), put

\[
 g_e=\gcd(a^e-1,N),\qquad1\leq e\leq D.
\]

A value \(g_e=N\) would imply \(\operatorname{ord}_N(a)\mid e\leq D\), so
it is impossible. A proper gcd factors \(N\). If a rational prime \(p\mid N\)
had local order \(r\leq D\), then \(p\mid g_r\). Therefore, if no factor is
returned, every \(g_e=1\) and every rational-prime local order exceeds
\(D\). This argument remains valid for nonsquarefree inputs: a partial
prime-power gcd is proper, while a saturated gcd contradicts the source
order.

Successive modular powers and fast gcds give the stated
\(O(D\mathsf M(n)\log n)\) cost. Nir's Proposition 1.2 bound absorbs this
linear scan. The Harvey--Hittmeir composition correctly displays it as a
separate term. The length-\(D\) transcript is valid together with the
source-certified unit premise; the packet makes no succinct-certificate
claim.

Consequently:

1. V1 Theorem 1 remains valid for every \(N\geq3\) and positive \(D<N\).
   It returns a factor, a correct prime report, or an ordinary
   \(2\leq a\leq D^2+D\) satisfying every-local order greater than \(D\).
2. V1 Theorem 2 remains valid for every \(N\geq3\) and
   \(1\leq D<N-1\). It returns a factor or an all-local unit, with the exact
   sum of the source and explicit scan costs. It has no theorem-wide
   \(D^{O(1)}\) ordinary-height promise.

## Numerical-QP comparison

If \(D\leq\exp((\log n)^C)\) for fixed \(C\), then every fixed power of
\(D\), every polynomial in \(n\), both composed running times, and the Nir
height \(D^2+D\) are numerical quasipolynomial. Such \(D\) is
\(2^{o(n)}\), so it is eventually below both \(N\) and \(N-1\).

The boundary in Nir's main theorem instead satisfies

\[
 \log D>\sqrt{2\log N\log\log N}
 =\Theta(\sqrt{n\log n}),
\]

which exceeds every fixed power of \(\log n\). Thus Nir Proposition 1.2,
not Nir Theorem 1.1, supplies the numerical-QP bounded-height interface.
The V2 endpoint repair does not change this conclusion.

## Synchronized orders and counterexample

If exact global orders \(m_i\) pass the prime-divisor screens, Lemma 2.3
gives \(\operatorname{ord}_p(b_i)=m_i\) for every rational prime
\(p\mid N\). Hence their lcm \(M\) divides every \(p-1\). For
\(N=pq\), this gives

\[
 M\mid\gcd(p-1,q-1)\mid N-1.
\]

For every prime \(\ell\mid N-1\), the definition
\(n=\lceil\log_2(N+1)\rceil\) gives
\(v_\ell(p-1)<n\), while
\(v_\ell((N-1)^n)\geq n\). Thus the F259/F260 baseline already saturates
every relevant rational-primary multiplicity, and multiplying it by such an
\(M\) cannot change its gcd with a hidden \(p-1\). This is only a common
capacity statement; it does not say that a known factored common order is
useless in every algorithm.

The counterexample is exact:

\[
 N=77,\quad D=10,\quad a=2,
\]

\[
 \operatorname{ord}_7(2)=3,\qquad
 \operatorname{ord}_{11}(2)=10,\qquad
 \operatorname{ord}_{77}(2)=30.
\]

It refutes global-to-local, synchronized-order, and \(D\)-roughness
implications. For the P205 residuals \(3\) and \(5\), the bare assignment
\(W=a=2\) absorbs neither. The packet correctly makes no claim about every
future word derived from the witness or its transcript.

## Lane and scope audit

The cited promoted statements and frozen search grammars confirm the packet's
declared boundaries.

- P139 already contains Harvey--Hittmeir followed by the explicit local
  scan. F280's additional source feature is Nir's ordinary height.
- Large local order supplies none of P161--P170's required rough support,
  support cover, resultant extinction, recursive child, independent action
  direction, Jacobi/Paley evaluator, ACD localization, or separating
  representation.
- The common modulus is symmetric in the hidden factors and supplies no
  P187 inversion-torsor orientation.
- P205 accepts an arbitrary public word, but neither source theorem outputs
  a residual-absorbing word. The counterexample is correctly limited to the
  returned base itself.
- P212 is a lower bound for a declared fresh-uniform, feedback-free grammar.
  Nir's deterministic scanned integer is biased, so that theorem does not
  apply. This exclusion supplies no success distribution.
- F259 and F260 use the saturated \((N-1)^n\) baseline. The synchronized
  lcm adds no unsaturated support, and no source theorem supplies a Pell,
  carry, quotient, collision, determinant, or P205-word transfer.

The requirement for an all-input or inverse-QP transfer law before opening a
new search is a project admission rule. It is not an impossibility theorem or
a lower bound against other algorithms.

## Qualifications preserved by this PASS

1. The repaired polynomial comparison is only for fixed
   \(0<\delta<1\) and sufficiently large admissible integer inputs.
2. The two polynomial-\(N\) costs are upper bounds for the named source and
   scan. They are not universal lower bounds.
3. The all-local postprocessor is explicitly linear in \(D\); no batched or
   sublinear certificate is claimed.
4. The bounded-height conclusion comes only from Nir Proposition 1.2. The
   Harvey--Hittmeir output has no theorem-wide \(D^{O(1)}\) height bound.
5. F280 proves no factoring algorithm, distribution law, carry law, P205
   word theorem, or impossibility theorem.
6. V2 is a proof-only additive repair. No code, compile, numerical
   experiment, remote access, ledger edit, frozen-byte edit, promotion, or
   commit belongs to this audit.
