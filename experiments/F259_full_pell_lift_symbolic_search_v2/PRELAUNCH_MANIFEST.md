# F259-D02 V2 prelaunch manifest

Status: repair packet prepared; execution validation pending.

V1 remains unchanged in
`experiments/F259_full_pell_lift_symbolic_search`. Its hostile audit is
unchanged and has SHA-256
`ef242ae9fb611f7d47fd3fb599f6ce07c34171fc4bc07d96c362ae16a153cb75`.
V1 is frozen FAIL and must not be repaired or launched.

V2 uses reserved experiment ID `F259-D02`. It preserves the V1 public Pell
source, scope shapes and caps, cohort seed and counts, 22 family names, and
255 word shapes. It changes only the invalid semantics and validation/report
contract identified before any cohort was opened:

- zero first carries remain zero;
- second-carry cores and target-15 routes are evaluated when `c=0`;
- identity mining uses exactly the twelve displayed cocycle terms;
- every public cleanup factor preserves a certificate;
- public `N`-power stripping is counted;
- direct cleanup-free rows and strict P205 rows have separate meanings;
- family and word reporting is complete and dimension-checked;
- F258/F260/F261/F263/F264 firewalls cover all executable modes;
- benchmark projection, resource, deadline, output, and report gates are
  executable requirements.

No C++ binary was compiled or executed during packet preparation. The local
Mac has no Boost Multiprecision header. Substituting a different arithmetic
library would change the requested workflow. The target has the required
header, but F258 is active and the V2 incompatibility gate forbids target
compilation, self-test, and benchmark. No cohort was generated or scored.

The local pre-edit resource inspection showed load averages near 1.9 on a
16 GiB Mac and 68 percent memory available. The planned validation modes are
resource-light, but process inspection is sandbox-restricted and target
nonoverlap is false while F258 runs. Validation therefore remains pending
rather than silently changing hosts or gates.

A fresh hostile pre-run audit is mandatory. The exact request and artifact
hashes are in `AUDIT_REQUEST.md` and `FROZEN.sha256`.
