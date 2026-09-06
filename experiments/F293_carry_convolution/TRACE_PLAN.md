# A discriminating larger exact sequence

The complete convolution pilot exposes roughly square-root-sized fluctuations.
Test the concrete hypothesis that, at a fixed residue N, their dependence on
k has a short constant-coefficient recurrence, as a fixed finite-dimensional
Frobenius-trace model would require. A finite fit is not a theorem: reserve a
later range for validation and report failed orders explicitly.

Compute N=1,3,5 through k=34, subject to a 25-second global run budget, using
the signed multiplicative convolution already derived. Half-period sign and
reflection symmetries reduce a coefficient to at most M/16 sign products.
The code obtains the needed group index by bit lifting at the known modulus;
it does not factor an input or use supplied hidden factors.

The source is standalone Rust compiled with optimization. It uses constant
memory and unsigned wrapping products, valid before reduction modulo2^k.
Small cases are checked against a separate inverse-graph enumeration. A
partial budget row is not a completed coefficient.

Resource estimate: under 64 MB runtime memory and 25 seconds on one core;
under 512 MB and a few seconds to compile. Inspect resources before launching.
Retain source, raw JSON-lines output and log, and recurrence analysis separately.
No remote job is needed unless the bounded pilot establishes a useful reason
to scale further.
