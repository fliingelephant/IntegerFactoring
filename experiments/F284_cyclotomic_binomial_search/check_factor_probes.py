"""Exact illustrative probes; no sampling or complexity claim."""

from fractions import Fraction
import json
from math import comb, gcd, isqrt
from pathlib import Path
import signal

signal.alarm(5)
rows = []
for modulus in (247, 391):
    b = isqrt(modulus)
    probes = {
        "central_binomial": Fraction(comb(2 * b, b)),
        "c1": Fraction(b**2, 2),
        "c2": Fraction(b**2 * (3 * b**2 + 2 * b + 1), 24),
        "c3": Fraction(b**4 * (b + 1)**2, 48),
        "H2": Fraction(b**2 * (2 * b + 1), 12),
        "H3": Fraction(b**5 * (b - 1) * (5 * b + 3) * (2 * b + 1)**2, 2160),
    }
    for name, value in probes.items():
        assert gcd(value.denominator, modulus) == 1
        residue = value.numerator * pow(value.denominator, -1, modulus) % modulus
        rows.append({"N": modulus, "B": b, "probe": name,
                     "value": str(value), "residue": residue,
                     "gcd": gcd(residue, modulus)})
assert next(r["gcd"] for r in rows if r["N"] == 391 and r["probe"] == "c2") == 17
assert next(r["gcd"] for r in rows if r["N"] == 247 and r["probe"] == "H3") == 13
target = Path(__file__).resolve().parent / "output/factor_probes.json"
target.write_text(json.dumps(rows, indent=2) + "\n")
print(f"Verified {len(rows)} exact probe residues; output={target}")
