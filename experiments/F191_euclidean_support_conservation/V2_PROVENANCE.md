# F191 V2 failure and provenance record

## Preserved V1

V1 remains frozen and unmodified:

- `STATEMENT.md`:
  `6747d7c6b121565bb1cbabb0041f7f11cb1f2f3306eb27beb126f3e4714bb124`
- `PROOF.md`:
  `21dfd6a74efc318434f54f5c7575b10c9d299b8e315459d20fd9643410cef455`
- `SELF_AUDIT.md`:
  `1bd8c60477f4bb8ccba50923e129333c0b48c5bf23312a21ac7ea1457c7ab7a5`

The fresh V1 hostile audit is preserved as `HOSTILE_AUDIT.md`, SHA-256
`d3ae15732f7f1beccd1d5a9c37cabf2a8ab11d821069822b7e7f69755ee2de69`.
Its strict verdict was **FAIL**.

## Exact V1 failure

The V1 live interface asked only for quotients or carries divisible by every
surviving support prime and then claimed that P163 could use those values
directly. This omitted P163's admissibility conditions. Such a value can be
zero, negative, or have magnitude at least \(N/2\). The audit also found a
minor zero-divisor carrier hole and a possible cycle if the bank bound
depends on the roughness cap selected from that same bound.

The audit accepted the exact support-conservation law, the balanced
\(X=N+c\) counterexample, the endpoint count, the finite permutation-bank
union bound, and the conditional group-theoretic size argument.

## V2 repair boundary

V2 changes only the failed interfaces:

1. A direct P163 handoff must output public integers \(A_j\) with
   \(0<|A_j|<N/2\) and support coverage, at total numerical-QP cost.
2. An unrestricted quotient or carry instead needs a separate
   support-preserving size-localization theorem.
3. The nonunit-divisor branch calls \(D\) a carrier only for \(D\ne0\).
4. The QP bank budget is fixed independently of \(T\), or an explicit
   uniform-dominance premise \(4B_\star(n,T(n))<T(n)\) is required.

The finite theorem, its constants, its endpoint count, and its canonical
counterexample are unchanged. No durable ledger was edited and no
mathematical computation was run.
