# F280 V2 provenance

## Immutable V1 chain

F280 V2 is an additive repair over the V1 frozen root

```text
a3ecad88c09874a5fcbbe5025596561910aeb5330dbe91206fabc2d49d7965db  FROZEN.sha256
```

The exact V1 statement imported by `V2_STATEMENT.md` is

```text
0d4a9ad469b961855cf77518b29926dfecaf958884a85b73e17f0ebf6f75016d  STATEMENT.md
```

The exact V1 proof imported by `V2_PROOF.md` is

```text
6a7871d91a5bd44eb08778633b04f7f0239ded8ca95392481bd6059491c006df  PROOF.md
```

The preserved fresh hostile audit has SHA-256

```text
57292f18bea502f64b50639361492bab6e441a8b339f583658a654998a687533  HOSTILE_AUDIT.md
```

That audit found one formal endpoint defect and no defect in the two source
interfaces, either all-local composition, the synchronized-order saturation
argument, or the project-lane boundaries.

## Exact repair origin

V1 Statement Section 5 applied the Harvey--Hittmeir cost formula to
\(D=N^\delta\) for fixed \(\delta>0\). The exact primary theorem accepts
only \(1\le D<N-1\). V2 therefore restricts the comparison to fixed
\(0<\delta<1\), for which \(D<N-1\) holds for all sufficiently large
admissible integer inputs. V2 makes no other normative change.

## Primary literature

V2 adds no literature source and changes no source attribution. It imports
the exact V1 primary-source record:

| Source | Version | Bytes | Pages | SHA-256 |
|---|---|---:|---:|---|
| David Harvey and Markus Hittmeir, *Deterministic methods for finding elements of large multiplicative order* | [arXiv:2601.11131v2](https://arxiv.org/abs/2601.11131v2), 5 June 2026 | 412025 | 13 | `0e957bacebc0b74f363436ab09b70085f4ad83c45dee93bda8aef19fbfdcbff0` |
| Itamar Nir, *Deterministically finding an element of large order in* \(\mathbb Z_N^*\) | [arXiv:2605.09592v1](https://arxiv.org/abs/2605.09592v1), 10 May 2026 | 293158 | 8 | `f3100236ec455410b657e2cb9a2983d4e0120232d102a571dcc61611a94d4fb1` |

Harvey--Hittmeir Theorem 1.1 is the source of the repaired domain
\(D<N-1\). The theorem's factor-or-high-order output, time bound, stated
space bound, and lack of a theorem-wide \(D^{O(1)}\) ordinary-height bound
are unchanged. Nir's theorem and proposition interfaces are unchanged.

## Unchanged local provenance

The P139, P161--P170, P187, P205, P212, F259, and F260 records remain
comparison interfaces, not new premises. V2 does not revise them. The
bounded-height theorem still comes from Nir Proposition 1.2 followed by the
explicit gcd scan. The faster unrestricted-height theorem still comes from
Harvey--Hittmeir Theorem 1.1 followed by that scan.

## Evidence and promotion boundary

No new empirical evidence supports V2. No code or experiment belongs to the
repair. The preserved hostile FAIL is not overwritten or reclassified. V2
requires a fresh hostile audit and a fresh statement-only reconstruction
before any promotion decision.
