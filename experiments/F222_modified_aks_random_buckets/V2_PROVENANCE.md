# F222 V2 provenance

## Preserved V1 packet

The original F222 files remain unchanged:

- statement: `e3d860bfb2558a365aa6389fb59460060c11566a6349ff4dc6a613ac4b4c143b`
- proof: `33780d9494fbadc933ae1a05aa2c779dfeadb0c1e668752e7116aba510b51171`
- self-audit: `775907003bb1b0ffc97f7d5a95767deb4cf7c6ea02bb82e98e2317b7bcccb0bb`
- result: `610d783a7157ef5672ddf20b38666732a32ec0e1966c14e3a4a267c75ca76564`

V2 strengthens the coefficient channel and weakens V1's unnecessary
`p>d^2+1` premise.  It does not rely on the F222-D01 finite run.

## External theorem

R. C. Baker, G. Harman, and J. Pintz, *The Difference Between Consecutive
Primes, II*, Proceedings of the London Mathematical Society 83 (2001),
532--562, Theorem 1, DOI `10.1112/plms/83.3.532`.

The primary source states that `[x-x^0.525,x]` contains primes for all
sufficiently large `x`.  V2 uses only that theorem statement.

## Review status

V2 has only the included self-audit.  It has no fresh hostile audit or blind
reconstruction and must not be promoted without both.

