# F260-D03 V3 static review

Review type: manual source and document inspection only.

No compiler, parser execution mode, binary, runner, corpus generator, remote
host, or cohort was used. This record does not qualify target compilation,
runtime, memory, output projection, or runner behavior.

## Narrow repair result

The prepared source addresses the complete D02 hostile boundary without a
known score, grammar-scope, cohort, or selection-rule change:

- Sequence, word, and factored candidates are first grouped by semantic
  fingerprint. Each group keeps the lexicographically first complete
  normalized syntax. Type ordering and the 4,096 cap occur only afterward.
- Every two-sequence word sorts its two retained child syntaxes before it
  constructs the word name. The canonical name is therefore the byte string
  used by the modulo-five syntax hash, semantic fingerprint, candidate ID,
  ranking tie-break, grammar output, and selection parser.
- The known D02 `dyadic_carry` duplicate is resolved by the general rule, not
  by a special case.
- Word residual minima and maxima are initialized from the first word row,
  updated per row, merged across worker cells, and emitted beside both means.
  The source refuses a word aggregate without initialized extrema.
- The runner expects 45 fields in both aggregate files. All D03 output,
  digest, manifest, path, and final-status labels are internally consistent.
- The D02 master seed and all score, source, transform, cohort, ranking,
  selection, lead, deadline, and resource constants remain unchanged.

## Pending evidence

Compilation, self-test, benchmark, target libraries, runtime projections, and
runner behavior remain unvalidated. A fresh independent hostile audit must
review the exact frozen hashes. `VALIDATION_PENDING.md` controls launch
qualification.
