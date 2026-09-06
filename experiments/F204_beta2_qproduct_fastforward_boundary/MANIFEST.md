# F204 manifest

## Frozen candidate files

- `STATEMENT.md`
  - SHA-256: `020717143764c86138c4ac0d211924884330385c2d7a578c1e1c4a540c2f5929`
- `PROOF.md`
  - SHA-256: `705dff58fcda88f8d7906e9019289f7d8ba73e0d85e56ab7a3e5dcefa3e87c91`
- `SELF_AUDIT.md`
  - SHA-256: `599242dbd73060d9da399905ff5f5883fdd62f2495057034c21446d8bd8bcd3f`
- `PROVENANCE.md`
  - SHA-256: `37c45bc636a8609231143e0318a2581c5805701386100e193da148f76185c8e0`

## Evidence class

Frozen proof-only candidate. No mathematical computation was run. Hashing was
used only to freeze the text. No durable registry, proved ledger, failed
ledger, or progress ledger was changed.

## Highest-risk claims to audit

1. The scalar cusp argument. Check the q-gamma exponent and constant, the
   limit at the cusp one-half, the conversion from a zero local Fourier
   exponent to radial power `y^(-k)`, and the exact need for the stated
   scalar meromorphic cusp hypotheses.
2. The primitive reduction of a rational-function Mahler identity. Check that
   denominator and content clearing leaves a nonzero mod-two relation with at
   least one Mahler multiplier, and that distinct Frobenius powers give a
   nonzero algebraic equation.
3. The infinite two-kernel witness. Check the valuation
   `v_2(M-1)=f+1`, the implication `x = plus or minus 1 mod 2^f`, and the
   strict bound `M<(2^f-1)^2` for `f>=e+2`.
4. The odd-prime root norm. Check the split between indices divisible and not
   divisible by `ell`, both dilation exponents, and the correction term in the
   coefficient recurrence.
5. The exact scope. Reject any reading as a general nonmodularity theorem for
   arbitrary orbit expressions, a nonlinear Mahler obstruction, a factoring
   lower bound, or an objection to one-child bitwise recursion.

## Required reviews

1. Recompute all four content hashes before reading the packet.
2. Run a fresh hostile audit of the frozen statement and proof.
3. If that audit passes, run a fresh strict statement-only reconstruction.
4. Promote only after both reviews pass and all frozen hashes are rechecked.
