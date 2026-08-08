# F101 — larger direct-null C2T stress test

## Question

Test whether the retained-relation decoder that succeeds in F98 still closes
on the first recorded 41-bit direct-screen-null input

\[
N=1{,}200{,}002{,}599{,}997.
\]

This is a factor-assisted finite diagnostic. It cannot prove an asymptotic
success law.

## Intended first run

Use the existing F98 launcher `run_single_1m_sage_with_timeout.py`. It sets a
hard 120-second timeout and calls the existing Sage factor-assisted replay.
Do not change the interpreter, launcher, decoder, or timeout without an
explicit workflow decision.
