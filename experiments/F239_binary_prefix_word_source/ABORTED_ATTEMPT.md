# F239 aborted broad attempt

- Preregistration SHA-256:
  `0ae27d2388282828ca10150d13abe5213a81d718f1a7d28d9eb899579dd5f412`.
- Command: `/tmp/f239_scan broad experiments/F239_binary_prefix_word_source/broad.out`.
- Exit status: `134`.
- Diagnostic: `std::runtime_error: quotient incidence mismatch`.
- Output: `broad.out` was opened but remained empty.
- Root cause: the local congruence cross-check was incorrectly applied to
  the residual prime two.  `PREREG_CORRIGENDUM_2.md` gives the exact repair.
- Evidence status: no row summary or broad-domain result was produced.  The
  attempt is not evidence for or against a word source.
