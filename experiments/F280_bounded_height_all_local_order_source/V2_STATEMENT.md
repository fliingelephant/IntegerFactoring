# F280 V2 — additive polynomial-range endpoint repair

## Status and authenticated base

F280 V2 is an additive proof-only repair candidate. It is not promoted.
It creates no code, search, run, dataset, or durable-ledger entry.

The normative base statement is the immutable V1 file `STATEMENT.md` with
SHA-256

```text
0d4a9ad469b961855cf77518b29926dfecaf958884a85b73e17f0ebf6f75016d
```

A statement-only reviewer must authenticate that exact V1 file, read it in
full, and then apply the single replacement below. The resulting text is the
complete V2 statement. No other V1 definition, hypothesis, theorem, proof
obligation, cost, comparison, boundary, or exclusion changes.

## Exact normative replacement

In V1 `STATEMENT.md`, Section 5, replace the block beginning

```text
For comparison, if \(D=N^\delta\) with fixed \(\delta>0\), the
```

and ending

```text
They are not lower bounds for other order or factoring algorithms.
```

by the following block:

> For comparison, if
> \[
>  D=N^\delta
> \]
> with fixed \(0<\delta<1\), then \(D<N-1\) for all sufficiently
> large \(N\). This is precisely the input-domain condition from
> Harvey--Hittmeir Theorem 1.1 that is relevant to this comparison. The
> Harvey--Hittmeir global source construction alone costs
> \[
>  N^{\delta/2+o(1)}.
> \tag{19}
> \]
> The explicit all-local postprocessor in Theorem 2 costs
> \(N^{\delta+o(1)}\). These are upper-bound accounting statements. They
> are not lower bounds for other order or factoring algorithms.

The restriction \(0<\delta<1\) is normative. The cases \(\delta=1\) and
\(\delta>1\) are not Harvey--Hittmeir inputs because they violate
\(D<N-1\). Algebraic substitution into a cost expression does not extend the
algorithm beyond that domain.

## Unchanged theorem interfaces

The following V1 content is imported without change.

1. Harvey--Hittmeir Theorem 1.1 is used only for
   \(N\ge3\) and \(1\le D<N-1\). It returns a nontrivial factor or a
   global-order-\(>D\) unit with the V1 time and space bounds.
2. Nir Theorem 1.1 retains its strict subexponential lower threshold on
   \(D\), its factor/unit/prime outcomes, and its stated time bound.
3. Nir Proposition 1.2 retains the arbitrary positive \(D<N\) interface,
   the \(O(D^{5/2+o(1)}\operatorname{polylog}N)\) time bound, and the
   ordinary output height \(2\le a\le D^2+D\).
4. V1 Theorem 1 retains its factor/prime/bounded-height all-local
   trichotomy for \(N\ge3\) and positive \(D<N\).
5. V1 Theorem 2 retains its factor/all-local interface for
   \(N\ge3\) and \(1\le D<N-1\), including the explicit linear local-scan
   term.
6. V1 Corollary 3 retains its numerical-QP conclusion and its exclusion of
   Nir Theorem 1.1 from the numerical-QP parameter range.
7. V1 Propositions 4 and 5, the P139/P161--P170/P187/P205/P212 and
   F259/F260 comparisons, the search-admission rule, and all exact
   exclusions are unchanged.

## Exact V2 scope

V2 repairs only the polynomial-\(N\) comparison endpoint. It does not add a
factoring algorithm, a height theorem for the Harvey--Hittmeir output, a
sublinear all-local certificate, a rough-order theorem, a P205 word, a
carry or quotient transfer, a distribution law, or an impossibility result.
