# F139 preserved failed certificate — packed base at N=667 factors

## Failed claim

The first selected witness used

```text
N = 667 = 23 * 29
B = 5
q = 7 * 19 = 133
iota_N(q) = 331
```

Its anchored columns did have the advertised parity and rank properties.
The preregistered verifier returned `PASS` for those incomplete checks.

## Fatal omitted screen

The packed base must run its own endpoint sign screens before any anchored
layer is used. Here

\[
\gcd(133-331,667)=1,
\qquad
\boxed{\gcd(133+331,667)=29}.
\]

Thus the operation factors \(N\) immediately. It never reaches the proposed
no-factor rank obstruction. The certificate cannot support the F139 failure
statement.

The original preregistration, pins, verifier, two output-only serialization
failures, and arithmetically passing but scope-incomplete output are preserved
with `667` in their filenames. They are not evidence for the corrected
candidate.
