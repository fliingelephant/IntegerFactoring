# F245 V2 self-audit

## Verdict

Self-audited candidate only.  V2 preserves V1 and repairs its strict blind
failure by restating the exact marker, torus, common-order, and Las Vegas
interfaces used by the combined obstruction.

## Checks

- The inverse-quotient atom and residue constants are unchanged.
- Conditional uniformity is with respect to the complete filtration.
- Every selected factor is positive and nonzero; every signed-power
  exponent is a positive integer.
- The marker construction and primitive-order implication are stated.
- The clean torus upper bound follows from local cyclic return counts.
- Nonclean norm-gcd exits are included at exponential scale.
- Common-order accumulation is bounded by the explicit gcd table.
- Markov truncation closes the expected-time Las Vegas reading.
- Signed and noncanonical Hilbert--90 carries remain outside the uniform
  quotient grammar.

## Scope risks for a fresh audit

1. Check that the concise CRT--Linnik construction really supports one
   absolute marker/input-length constant.
2. Check that every Miller-chain factor needs a local return under the final
   exponent.
3. Check the nonclean norm-zero probability without assuming split type.
4. Reject any extension from fresh conditional-uniform seeds to biased or
   dependent inverse descent.
