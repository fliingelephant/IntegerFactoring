# F124-D01 result: the full-supergroup gate is empty on the fixed corpus

## Result

The run completed the full fixed corpus. It found no feasible subgroup and no
decisive null.

- Fixed retained corpus: 69,060 semiprimes.
- Exact subgroup cap: 32,768.
- Feasible supergroups: zero.
- Inputs skipped by the exact size gate: 69,060.
- Status: `COMPLETE_NO_NULL`.

The smallest supergroup had size 75,900:

\[
N=152591=331\cdot461,
\qquad
|\widehat H_N|=75900.
\]

Its lattice index was two. It was still more than twice the preregistered
cap.

The largest computed supergroup had size 16,736,280. Across the complete
corpus:

- 69,032 supergroups had lattice index one. They were the full unit group.
- 28 supergroups had lattice index two.
- No other lattice index occurred.

All initial seed inverse-sign screens were null. There were zero proper gcd
hits across all retained inputs.

## What the run did

For each retained \((p,q)\), the source processed every seed from 2 through
\(n\). It factored the seed and canonical-inverse endpoints exactly. It then
formed the rational-prime generator set.

The run built complete local discrete-log tables. It computed the lattice
index as the gcd of all required two-by-two minors. It then computed

\[
|\widehat H_N|={(p-1)(q-1)\over\text{index}}
\]

with exact integer arithmetic.

Every computed size was above 32,768. Therefore the preregistered rule skipped
every input before explicit subgroup enumeration and P66 decoding. The
explicit-enumeration equality check had no feasible input on which to run.

## Exact conclusion

This run does **not** give a counterexample to the static F26-Q source. It also
does not give a positive factoring certificate.

It closes the declared finite full-supergroup kill test as a feasibility
attempt:

> On every one of the 69,060 fixed trial-hard semiprimes, the rational-prime
> endpoint supergroup is larger than the preregistered enumeration cap.

The result also shows why this supergroup is too coarse for this corpus. It is
almost always the full unit group. Enlarging the public block subgroup to this
supergroup removes the small-state condition needed by the proposed decisive
decoder test.

The result says nothing about a smaller public block subgroup, a sparse word
selector, recursive feedback, unreduced integer products, or another decoder.

## Run facts

- Pair count before the trial-hard gate: 69,506.
- Retained corpus count: 69,060.
- Processed corpus count: 69,060.
- Unprocessed count: zero.
- Source elapsed time: 3.214029 seconds.
- Runner elapsed time: 3.781035 seconds.
- Runner exit code: zero.
- Structured output size: 36,672,024 bytes.
