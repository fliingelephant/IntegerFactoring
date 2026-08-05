"""Fresh timing probe for direct quotient-ring exponentiation (F04 reconstruction)."""

import json
import sys
import time


if len(sys.argv) != 3:
    raise SystemExit("usage: sage benchmark_direct.sage MODULUS EXPONENT")

modulus = ZZ(sys.argv[1])
exponent = ZZ(sys.argv[2])
r = 2953
field = GF(modulus)
polynomials = PolynomialRing(field, "x")
x = polynomials.gen()
quotient = polynomials.quotient(x**r - 1, "y")
y = quotient.gen()

start = time.monotonic()
value = (y + 1) ** exponent - y**exponent - 1
coefficients = value.lift().list()
coefficients += [field.zero()] * (r - len(coefficients))
elapsed = time.monotonic() - start

print(json.dumps({
    "approach_family": "F04_reconstruct",
    "modulus": int(modulus),
    "exponent": int(exponent),
    "r": int(r),
    "a": int(1),
    "elapsed_seconds": elapsed,
    "zero_count": int(sum(c == 0 for c in coefficients)),
    "checksum": int(sum((i + 1) * ZZ(c) for i, c in enumerate(coefficients)) % modulus),
}, sort_keys=True))
