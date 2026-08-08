# F113 — broaden the failed `(2,v)` menu to all small seed pairs

## Question

F112 found that the fixed `(2,v)` appended menu fails on all seven 46-bit
global-root cases.  Does the complete nonadaptive menu of unordered seed
pairs rescue those exact counterexamples?

## Source

Use the same frozen first layer.  Then append both trajectories for every

```text
2 <= u < v <= n
```

in lexicographic order, through exponent `n^2`.  Keep one joint decoder.  The
menu is fixed before any generated relation is inspected and has `O(n^4)`
residue positions.

The implementation is factor-assisted.  Both factors are inputs only for the
diagnostic decoder and result check.  Any fixed positive witness requires a
factor-free replay before promotion.

## Outcomes

- A factor after `u>2` shows that the F112 failure is a narrow-menu failure.
- A complete null is evidence against this exact all-seed-pair source on that
  input.

Neither outcome gives an all-input theorem.
