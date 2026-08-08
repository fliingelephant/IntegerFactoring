# Proof-blind failed attempts

The timeout runner preserves every attempt in
`proof_blind_reconstruction_attempts/` and only promotes a successful attempt
to the canonical output and log names.

## 20260808T013636.874466Z

Status: failed during the seed-only public decoder check.

Cause: the first implementation assumed that continuing to feedback required
a zero-dimensional seed kernel. The public source only requires its declared
kernel scan to find no useful non-global square root. The seed kernel can be
nonzero when all scanned roots are global. The reconstruction now verifies
that exact condition.

Preserved log:
`proof_blind_reconstruction_attempts/20260808T013636.874466Z.log`

## 20260808T013706.810986Z

Status: executable exit 0, but fixed-claim validation failed.

Cause: the reconstructed initial gcd-free presentation did not discard an
arithmetic block of value one after a split. This introduced false `(1, 1)`
active pairs. It produced 7,065 raw relations instead of 12,549. The allowed
public source discards value one at the top of its refinement loop. The
reconstruction now does the same.

Preserved artifacts:
`proof_blind_reconstruction_attempts/20260808T013706.810986Z.output.json` and
`proof_blind_reconstruction_attempts/20260808T013706.810986Z.log`
