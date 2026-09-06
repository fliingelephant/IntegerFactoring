# F280 fresh hostile proof and literature-composition audit

## Verdict

**FAIL, for one formal parameter-endpoint defect.** The two primary-source
interfaces, the bounded-height all-local composition, the faster
Harvey--Hittmeir composition, and the stated project-lane boundaries survive
hostile review. However, the polynomial-\(N\) comparison is stated for every
fixed \(\delta>0\), while the Harvey--Hittmeir algorithm requires
\(D<N-1\). For \(D=N^\delta\), this requires \(0<\delta<1\). The packet's
unrestricted endpoint includes \(\delta=1\) and \(\delta>1\), where the cited
algorithm is not admissible.

This is a narrow statement defect. It does not invalidate Theorems 1 or 2,
the all-local postprocessor, or the numerical-QP conclusions. No frozen byte
was repaired.

## Authentication

I authenticated the frozen root and all five entries before reading any of
the five mathematical files. The observed hashes were:

```text
a3ecad88c09874a5fcbbe5025596561910aeb5330dbe91206fabc2d49d7965db  FROZEN.sha256
0d4a9ad469b961855cf77518b29926dfecaf958884a85b73e17f0ebf6f75016d  STATEMENT.md
6a7871d91a5bd44eb08778633b04f7f0239ded8ca95392481bd6059491c006df  PROOF.md
4dce3fe66ffbfeda0b4aaea0d47522631633d638ca93266120b5cfbf038a44e2  SELF_AUDIT.md
f36a8927e905a8a1c6bf61f8477be50b7b3458a480c271200b8b9a7a485b9733  PROVENANCE.md
818aefe8ae8d13488d4b730881962e48f2b5a403b6bcc8695aca178eca50c85d  MANIFEST.md
```

The root and every entry matched `FROZEN.sha256` exactly. I then read
`STATEMENT.md`, `PROOF.md`, `SELF_AUDIT.md`, `PROVENANCE.md`, and
`MANIFEST.md` in full.

## Promotion-blocking defect: the \(D=N^\delta\) range is too broad

Statement equation (19) and its proof say:

\[
 D=N^\delta\quad\text{for fixed }\delta>0,
\]

and then attribute the cost

\[
 T_{\rm HH}(N,D)=N^{\delta/2+o(1)}
\]

to the Harvey--Hittmeir source construction. They likewise attribute
\(N^{\delta+o(1)}\) to the explicit all-local scan.

Harvey--Hittmeir Theorem 1.1 has the exact input condition

\[
 1\le D<N-1.
\]

For \(D=N^\delta\), admissibility holds eventually only when
\(0<\delta<1\). At \(\delta=1\), \(D=N\); for \(\delta>1\), \(D>N\).
Neither is an input to the cited theorem. Algebraic substitution into the
displayed cost expression does not create an algorithm outside its domain.

The surrounding phrase “for all sufficiently large admissible inputs” is in
the preceding numerical-QP paragraph. It does not repair this separate
polynomial-\(N\) comparison, which positively says that the named source
construction has the displayed cost. A revised packet must restrict this
comparison to \(0<\delta<1\), or state it only for admissible choices. The
frozen packet cannot be changed in place.

## Exact primary-source checks

I independently downloaded and authenticated the exact versioned primary
PDFs cited by the packet.

```text
0e957bacebc0b74f363436ab09b70085f4ad83c45dee93bda8aef19fbfdcbff0  arXiv:2601.11131v2
f3100236ec455410b657e2cb9a2983d4e0120232d102a571dcc61611a94d4fb1  arXiv:2605.09592v1
```

The first file has 412025 bytes and 13 pages. Its title and authors are
David Harvey and Markus Hittmeir, *Deterministic methods for finding
elements of large multiplicative order*. The second has 293158 bytes and 8
pages. Its title and author are Itamar Nir, *Deterministically finding an
element of large order in* \(\mathbb Z_N^*\). These values match
`PROVENANCE.md` exactly.

Harvey--Hittmeir Theorem 1.1 states exactly the following interface:

- \(N\ge3\), \(D\ge1\), and \(D<N-1\);
- output a nontrivial divisor of \(N\), or
  \(\alpha\in\mathbb Z_N^*\) with \(\operatorname{ord}_N(\alpha)>D\);
- deterministic multitape-Turing time
  \(O(D^{1/2}\log D\,\log N/\sqrt{\log\log D})\);
- stated space
  \(O(D^{1/2}\log N/\sqrt{\log\log D})\).

The paper supplies the packet's small-\(D\) convention for \(\log\log D\).
It represents residues in \([0,N)\). It does not state a theorem-wide
ordinary-height bound \(D^{O(1)}\). Lemma 2.1 returns the exact order when it
is at most \(D\), Lemma 2.3 supplies the rational-prime local-order screens,
and Lemma 2.2 combines known factored orders into their lcm order. Algorithm
3.1 can return a scanned \(\beta\), but it can instead return an
lcm-combined residue. F280's height limitation is therefore exact.

Nir Theorem 1.1 states exactly:

- positive integers \(D<N\);
- \(D>\exp(\sqrt{2\log N\log\log N})\);
- output a high-global-order unit, a nontrivial factor, or the correct report
  that \(N\) is prime;
- deterministic time \(O(D^{1/2+o(1)})\).

Nir states no space bound. Proposition 1.2 has the same three outcomes for
every positive \(D<N\), with time
\(O(D^{5/2+o(1)}\operatorname{polylog}N)\). Its proof explicitly scans the
ordinary integers \(2,3,\ldots,D^2+D\). Thus any high-order output from this
algorithm has the packet's claimed ordinary height. The main theorem's
threshold implies \(\log N=D^{o(1)}\), but it is not numerical-QP in the
input bit length. F280 distinguishes these two Nir interfaces correctly.

## Hostile proof checks that pass

### Global order to every-local order

Let a source return a unit \(a\) with \(\operatorname{ord}_N(a)>D\). For
\(1\le e\le D\), a gcd

\[
 g_e=\gcd(a^e-1,N)
\]

cannot equal \(N\), because that would give
\(\operatorname{ord}_N(a)\mid e\). If a rational prime \(p\mid N\) had
\(\operatorname{ord}_p(a)=r\le D\), then \(p\mid g_r\). Therefore the scan
returns a proper factor or every \(g_e=1\), in which case every rational-prime
local order exceeds \(D\). This remains valid for repeated prime powers: a
partial prime-power gcd is proper, while a saturated gcd contradicts the
global-order premise.

Successive modular powers use \(D\) modular multiplications and \(D\) gcds
on \(O(n)\)-bit integers. The displayed
\(O(D\mathsf M(n)\log n)\) bit bound is valid and is absorbed by Nir's
arbitrary-\(D\) cost. In the Harvey--Hittmeir composition it must remain as a
separate, asymptotically dominant term. F280 does not falsely preserve the
source's square-root dependence after all-local certification.

The surviving scan equalities are an explicit length-\(D\) transcript. The
source algorithms already establish that the returned element is a unit; a
standalone verifier can additionally recompute \(\gcd(a,N)=1\) at negligible
cost. The packet makes no succinct-certificate claim.

### Bounded height and primality outcomes

Nir Proposition 1.2 supports all positive \(D<N\), including the endpoint
\(D=N-1\). It may correctly report primality. Its scanned high-order output
is an ordinary integer at most \(D^2+D\). The postprocessor preserves that
integer, so Theorem 1's factor/prime/all-local trichotomy is valid for general
\(N\), including even and nonsquarefree composites.

Harvey--Hittmeir supports only \(D<N-1\) and never uses a prime-report
outcome. F280's Theorem 2 preserves that two-outcome interface. Its canonical
representative is below \(N\), but no cited theorem makes it
\(D^{O(1)}\).

### Numerical-QP range

For fixed numerical-QP \(D(n)\), every displayed fixed power of \(D\), every
polynomial in \(n\), and the Nir height \(D^2+D\) remain numerical QP.
Such \(D\) is eventually below \(N-1\). Conversely, Nir's main threshold has

\[
 \log D=\Theta(\sqrt{n\log n}),
\]

which exceeds every fixed power of \(\log n\). These conclusions are exact.
Only the separate \(D=N^\delta\) comparison has the endpoint defect above.

### Synchronized orders, factorization, and multiplicity saturation

After an exact global order \(m_i\) is found and factored, passing all
prime-divisor screens proves

\[
 \operatorname{ord}_p(b_i)=m_i
 \quad\text{for every rational prime }p\mid N.
\]

Thus the known, fully factored lcm \(M\) divides every \(p-1\). For a
semiprime \(N=pq\), it follows that

\[
 M\mid\gcd(p-1,q-1)\mid N-1.
\]

This is common capacity, not a localization or orientation object.

F280 also handles primary multiplicities correctly. If
\(\ell\mid N-1\), then for every rational prime \(p\mid N\),

\[
 \ell^{v_\ell(p-1)}\le p-1<N<2^n,
\]

so \(v_\ell(p-1)<n\), while
\(v_\ell((N-1)^n)\ge n\). Hence multiplying the F259/F260 baseline by
\(M\), or by any power of \(M\), cannot change its gcd with either hidden
\(p-1\). The packet does not confuse support containment with a claim that
the factored lcm is useless in every algorithm.

### Counterexample and project-lane boundaries

The counterexample \(N=77\), \(D=10\), \(a=2\) is exact:

\[
 \operatorname{ord}_7(2)=3,
 \quad \operatorname{ord}_{11}(2)=10,
 \quad \operatorname{ord}_{77}(2)=30.
\]

It simultaneously refutes global-to-all-local, local-order equality, and
\(D\)-roughness. For P205,
\(d=2\) and the residuals are \(3\) and \(5\); the bare word \(W=a=2\)
absorbs neither. The packet correctly limits this example to the bare-base
implication and does not claim that every future derived word must fail.

The comparisons with P139, P161--P170, P187, P205, and P212 match their
promoted interfaces. P139 already contains Harvey--Hittmeir plus the local
scan. The new source feature is Nir's ordinary-height bound. Large local
order does not provide rough prime support, a resultant support cover, a
recursive child, a Jacobi/Paley evaluator, an ACD selector, a separating
representation, an inversion-torsor orientation, or a P205 residual-absorbing
word. A deterministic scanned integer is biased and is outside P212's
fresh-uniform restricted grammar; this supplies no positive distribution
law.

The F259 V2 and F260 V3 frozen grammars use the saturated
\((N-1)^n\) baseline. Their Pell, quotient, carry, determinant, collision,
and P205-word candidates require explicit integer transfers. Neither primary
order theorem provides one. F280 therefore does not claim a theorem about a
grammar extension that it has not defined.

## Search and scope boundary

The sentence that no search is justified before a transfer theorem is a
project admission rule. It is not a mathematical impossibility result.
`PROOF.md` says this explicitly, and the exact exclusions preserve future
biased-source, carry, quotient, determinant, decoder, and batch-certificate
routes. Finite experimentation could suggest a transfer, but it would not by
itself prove the all-input or inverse-QP progress law required by the stated
factoring transition.

No code was created or changed. No local or remote experiment was run. No
ledger or frozen artifact was edited.
