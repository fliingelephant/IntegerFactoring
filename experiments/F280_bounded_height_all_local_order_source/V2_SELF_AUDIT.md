# F280 V2 author self-audit

## Status

This is the author's audit of one additive endpoint repair. It is not a
fresh hostile audit, an independent statement-only reconstruction, a
promotion, or a computational experiment.

## Immutable inputs

The V2 overlay imports these immutable V1 files:

```text
0d4a9ad469b961855cf77518b29926dfecaf958884a85b73e17f0ebf6f75016d  STATEMENT.md
6a7871d91a5bd44eb08778633b04f7f0239ded8ca95392481bd6059491c006df  PROOF.md
4dce3fe66ffbfeda0b4aaea0d47522631633d638ca93266120b5cfbf038a44e2  SELF_AUDIT.md
f36a8927e905a8a1c6bf61f8477be50b7b3458a480c271200b8b9a7a485b9733  PROVENANCE.md
818aefe8ae8d13488d4b730881962e48f2b5a403b6bcc8695aca178eca50c85d  MANIFEST.md
```

Their `FROZEN.sha256` root is
`a3ecad88c09874a5fcbbe5025596561910aeb5330dbe91206fabc2d49d7965db`.
The fresh V1 hostile audit is preserved with SHA-256
`57292f18bea502f64b50639361492bab6e441a8b339f583658a654998a687533`.

## Repair check

1. The V1 statement used \(D=N^\delta\) for every fixed \(\delta>0\) in
   its polynomial-\(N\) Harvey--Hittmeir comparison.
2. Harvey--Hittmeir Theorem 1.1 requires \(1\le D<N-1\).
3. If \(D=N^\delta\) with fixed \(0<\delta<1\), then
   \(N^\delta/(N-1)\to0\). Thus the cited algorithm is admissible for all
   sufficiently large inputs.
4. If \(\delta\ge1\), then \(D=N^\delta\ge N\), so the cited algorithm is
   not admissible.
5. V2 makes exactly this restriction in the normative statement and its
   proof. It does not change either cost after the domain is satisfied.

## Regression checks

6. The Harvey--Hittmeir inputs, outputs, time, space, and height limitation
   are unchanged.
7. The Nir main-theorem threshold, Proposition 1.2 interface, primality
   output, time bounds, and scanned height are unchanged.
8. The length-\(D\) gcd scan still upgrades global order to every
   rational-prime local order for general, possibly nonsquarefree, \(N\).
9. The Nir composition still returns a factor, a correct prime report, or
   an ordinary \(a\le D^2+D\) with every local order above \(D\).
10. The Harvey--Hittmeir composition still displays the source and explicit
    local-scan costs separately and has no theorem-wide \(D^{O(1)}\)
    ordinary-height claim.
11. The numerical-QP result and the exclusion of Nir Theorem 1.1 from that
    range are unchanged.
12. Synchronized exact orders remain factored common capacity. Their lcm
    divides every \(p-1\), and the \((N-1)^n\) baseline still saturates all
    of their rational-primary multiplicities relevant to F259/F260.
13. The \(N=77,D=10,a=2\) counterexample and its narrow P205 bare-base
    conclusion are unchanged.
14. Every P139/P161--P170/P187/P205/P212 and F259/F260 interface boundary,
    every nonclaim, and the methodological status of the no-search rule are
    unchanged.

## Resource and status check

No source code, generator, executable, benchmark, dataset, local research
computation, remote computation, frozen V1 edit, or durable-ledger edit
belongs to V2. V2 awaits a fresh hostile audit and an independent
statement-only reconstruction. It is not promoted.
