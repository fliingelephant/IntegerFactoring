# F59 hostile source-proof audit

**Verdict: FAIL as a complete registered scan.** The arithmetic decoder
passes. The retained rank and basis-root results are mathematically sound.
However, the walk source can omit a direct factor event at the step cap, and
the runner can hide a source failure. Thus the exact direct-event totals and
the registered success status do not yet meet the declared standard.

I read the complete manifest, D01 source and runner, D01 output, A01 source and
output, and the complete F58 generic decoder theorem. I did not run a research
computation.

## 1. Decoder audit: PASS

### Parity refinement preserves every square class

An active entry `(b, mask)` says which retained relations contain the class of
`b` with odd exponent. Suppose entries `(x, alpha)` and `(y, beta)` meet at
`d = gcd(x, y)`. The replacement is

```text
(d, alpha XOR beta), (x/d, alpha), (y/d, beta).
```

For each relation column, the old and new products differ by an even power of
`d`. They therefore have the same rational square class. This remains true
when one value divides the other or when the values are equal.

A zero mask is safe to remove. Such a block has even exponent in every
relation. It contributes a square to every subset product. Removing it can
prevent a later numeric split, but any pieces made only through that split
would carry the same nonzero mask. They add no new binary condition.

### Refinement terminates and leaves coprime blocks

Ignore masks for this proof. Use

\[
\Phi=\sum_p\sum_b v_p(b)^2.
\]

Each collision with a nontrivial gcd decreases this nonnegative integer by at
least one. Omitting a value because its mask is zero only decreases it more.
Thus the loop terminates. A value enters `stable` only after it is coprime to
all current stable values. A later collision removes the affected stable
value and sends all pieces back to `work`. Therefore all final stable values
are pairwise coprime.

### The binary kernel is exact

For each surviving nonsquare coprime block, its mask is one binary equation.
A selected product is a square exactly when every nonsquare block occurs an
even number of times. A square block needs no equation. Pairwise coprimality
prevents an odd prime valuation from cancelling between different blocks.
Thus the row kernel is exactly the set of square subsets.

`binary_kernel_basis` uses the highest set bit as each pivot. It then solves
pivots in increasing order for each free column. The returned vectors are in
the kernel, are independent because they have distinct free columns, and have
the correct count. They are a complete kernel basis.

### Root tests are correct

For each basis vector, D01 multiplies the selected positive values, computes
the exact positive integer root, and asserts that its square is the product.
Every retained value is `1 mod N`, so the root is a square root of one modulo
`N`. On the declared product of two distinct odd primes, a root other than
global `+1` or `-1` gives a proper factor from each of `gcd(root-1, N)` and
`gcd(root+1, N)`. The assertions are valid.

Testing a kernel basis is complete. The root image is a homomorphism on the
kernel. If every basis image is global, every kernel image is global. Hence a
useful square subset cannot be missed by testing only the basis.

### Preprocessing is safe

The `k=0` value is one and has root image one. Equal `k` values give the same
integer `A = Nk+1`. Two copies contribute `A^2`, whose positive root is
`A = 1 mod N`. Reducing each equal-`k` class to one representative therefore
preserves all attainable modular root images. The source applies both rules
before it assigns columns.

The decoder uses only `N`, sampled units, their public modular inverses, gcd,
exact division, integer square root, and binary elimination. The known factors
`p` and `q` are not used by the sampler or decoder. Starting refinement from
the known transcript pair `(u, v)` is not an oracle: both values were computed
from `N` and the sampled `u`.

## 2. Source audit: one blocking defect

Independent sampling is correct for the declared finite diagnostic.
`randrange(1, N)` has no range-reduction bias, and rejection on `gcd(u,N)=1`
gives the uniform distribution on units under the PRNG model. Child seeds are
stored. The random-tail source uses exactly `n` accepted unit starts. Both
tail sources append at most `n` relations per start, so their raw batch count
is at most `n^2`. Offset starts depend only on public `N`.

The defect is at `F59_D01_scan.py` lines 80--93. The code checks whether the
current state is a nonunit before a transition. It appends the transition and
sets `state = quotient`. If this is the last allowed transition, the loop ends
without checking the new endpoint. A nonunit quotient at that point exposes a
factor but is not recorded.

This is a real logical gap. For example, with `N=15`, start `u=7`, and a
one-step cap, the canonical inverse is 13 and the quotient is 6. The source
returns the relation but never records `gcd(6,15)=3`.

Therefore these output fields are not certified as complete:

- `direct_gcd_events` for random-tail and offset batches;
- the A01 totals of seven random-tail and two offset direct events;
- the manifest statement that every terminal direct event was counted.

The omission does not change the relation list or any decoder rank or root.
An immediate endpoint check would append the same last relation and then
record the factor. Thus the batch-decoder conclusions below survive. The
current JSON does not store final states for each prefix, so an artifact-only
audit cannot recover the missed count. A deterministic replay or a corrected
new run is necessary to obtain exact direct-event totals. I did not run it.

## 3. Runner audit: FAIL

`run_F59_D01.sh` uses

```sh
/opt/homebrew/bin/timeout ... python ... 2>&1 | tee logs/F59-D01.log
```

with `set -eu` but without pipeline failure propagation. POSIX `sh` reports
the status of `tee`, not the status of `timeout` or Python. A timeout or Python
failure can therefore produce runner exit status zero. A stale output file
could also remain from an earlier launch.

The present log ends normally, the output is complete, its hash is pinned, and
A01 parsed all 12 inputs. This is strong evidence that D01 itself completed.
It does not make the runner correct. The registered runner must preserve the
source exit status, and the corrected runner must be used for the replacement
run.

## 4. Output and inference audit

Subject to the narrow defects above, the output supports these finite facts:

- All 96 independent batches had full square-class rank after the declared
  zero and duplicate preprocessing.
- All 96 random-tail batches also had full square-class rank.
- All 12 deterministic offset batches had a nonzero kernel. Their total
  dimension was 19. The tested basis roots were 18 global `-1` roots and one
  global `+1` root. None was useful for batch factor extraction.
- No tested batch had a non-global basis root. By the decoder proof, no tested
  preprocessed batch contained an untested useful square subset.
- The reported 22 independent rejection events are complete. The reported
  tail and offset direct-event totals are lower bounds until the endpoint bug
  is repaired and replayed.

The deterministic offset rank defect is partly built in. The first start is
`N-1`; its inverse is `N-1`, and it gives

\[
N(N-2)+1=(N-1)^2.
\]

This guarantees at least one kernel vector with global root `-1` for every
offset batch. Therefore “12 of 12 offset batches have a nonzero kernel” is not
new source evidence by itself. The seven dimensions above this forced
baseline are also global in the chosen bases.

The finite full-rank outcome is valid kill evidence against these exact
`n^2` independent and random-tail schedules. It says nothing about larger
polynomial schedules, other correlated sources, or all inputs. It does not
prove a factoring algorithm or an asymptotic obstruction.

## 5. Secondary record defects

These items do not change the decoder mathematics, but the final record should
correct them:

- The manifest says D01 records “coprime blocks” and “square flags.” The JSON
  stores only block counts, the square-block count, and the maximum block bit
  length. It does not store block values, masks, or per-block flags.
- A01 checks hashes and scalar identities. It does not independently recompute
  relations, coprime blocks, the binary kernel, or roots, because D01 does not
  retain those data. Its verdict is correctly limited to artifact and internal
  consistency, but it cannot validate decoder arithmetic on its own.
- The manifest opening still says the separate audit is pending, while its
  later A01 section says that audit completed.

## Required disposition

Do not discard the D01 rank and root evidence. Mark the current direct-event
totals as incomplete. Repair the endpoint check and runner status propagation,
preregister a replacement run, and replay the same declared seeds and inputs.
Compare all rank and root fields with D01; they should remain unchanged. Only
after that replay passes an artifact audit should the complete scan receive a
PASS.
