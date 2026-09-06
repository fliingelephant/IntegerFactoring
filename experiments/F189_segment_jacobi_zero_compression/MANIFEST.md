# F189 manifest

## Status

Frozen proof-only candidate awaiting hostile audit.

No mathematical research computation was run. No durable proof or failure
ledger was edited by this candidate.

## Frozen artifacts

| Artifact | SHA-256 |
|---|---|
| STATEMENT.md | 2e7c4df447013db2e5ebc5d51045eec0abff3a36f1bf59760d74ae31f4adbfc1 |
| PROOF.md | ced9a963f902541836a1214a2d7afea4616ae53d7360b26c4d47e3434247c03e |
| SELF_AUDIT.md | 9fbba1461d4afcf3825609f461563fbdd61f50ae4035f44044562c0523cc56b1 |

## Candidate result

For every odd modulus, the segment-Jacobi zero predicate is exactly the
presence of a nonunit in the interval. The totalized half-floor identity

\[
 F(x,N)+F(N,x)
 =\frac{(x-1)(N-1)}4+\frac{\gcd(x,N)-1}{2}
\]

shows that the information omitted by coprime Gauss parity is exactly the
short-interval weighted hidden-divisor hit count.

A uniform QP zero oracle would isolate a proper factor with one queried child
per binary level. On the affine two-seed source at the P34 numerical scale,
the exact useful probability conditional on the unit branch is

\[
 \frac{T-1}{p-1}+\frac{T-1}{q-1}
 -\frac{(T-1)^2}{(p-1)(q-1)}
 -\frac{T-1}{(p-1)(q-1)}
 >\frac1{40}.
\]

The packet does not construct this oracle.

The exact named-model boundaries are:

- recurrence order \(\operatorname{rad}(N)\) for the literal zero mask;
- recurrence order \(p+q-1\) after the public global-zero correction for
  squarefree \(N=pq\);
- exactly \(\operatorname{rad}(N)\) states for the explicit binary DFA;
- a Kummer carry in the hidden prime base for the factorial/binomial form.

These are representation bounds, not a classical factoring lower bound.

## Closest prior route and material difference

P34 gives the exact balanced-semiprime Boolean pooled-zero probability and
an \(N^{1/4+o(1)}\) evaluator. F175 proves exponential width only for named
read-once functional representations of the original Boolean product.

F189 studies a different two-seed affine pool and asks only for its
segment-Jacobi zero predicate, not the shifted-factorial residue or the
original \(Q_K\). Its materially new contribution is the noncoprime
half-floor identity and the exact identification of the missing zero
correction with a weighted short-interval gcd count.

## Required verification

1. Fresh hostile proof audit of all three frozen inputs.
2. Fresh statement-only reconstruction if the hostile audit passes.
3. Only then may root consider promotion.
