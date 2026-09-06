# F165-R01 V1 blind-reconstruction prelaunch failure

## Status

The reconstruction was stopped before source freeze, registration, or any
mathematical run. It produced no computational evidence.

The frozen V1 blind statement has SHA-256

`be2d147b9595649bd0ecfa30fe63f848a263a764debe074808adf2e1ddee2589`.

## Exact mismatch

V1 required every original endpoint presentation \((c,w)\) or \((z,w)\) to
enter integer refinement before exact-value deletion.

The registered F165-D01 implementation has narrower semantics. It first keeps
one record for each distinct exact value

\[
A=cw
\quad\hbox{or}\quad
A=zw,
\]

and then passes the single labelled integer \(A\) to the factor-free parity
decoder. It does not pass the two original endpoints as separate refinement
inputs. An equal exact value does not retain an alternate endpoint
presentation.

These workflows can name different integer blocks even though they have the
same exact square-class columns. Therefore an independent replay of V1 would
not reconstruct the registered experiment.

## Consequence

The F165-D01 result remains evidence for recursive feedback in the
exact-value relation decoder. It is not evidence for a persistent
presentation-complete endpoint ledger.

A fresh V2 blind statement must reproduce the exact-value-only semantics.
Any later order experiment over newly named endpoint blocks must use a
separate persistent endpoint-presentation ledger.

