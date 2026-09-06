# F138 local replay sandbox failure

The root agent first replayed the registered maximum-digit Sage verifier in
the workspace sandbox. Sage stopped before the mathematical checks because
its default state directory under `.sage` was not writable in that sandbox.

This was an environment failure, not a failed arithmetic assertion. The
subsequent authorized replay of the same pinned verifier returned `PASS` and
reproduced the pinned JSON evidence. `HOSTILE_AUDIT.md` independently reran
all three verifiers and reproduced all three pinned JSON files.

The first command's log path was reused by the passing replay, so the raw
permission-error text is no longer present. This note preserves that fact
instead of treating the first attempt as a successful run.
