#!/usr/bin/env sage
"""Direct determinant check that (a,j)=(1,47) is the first PSC mismatch.

Family: F04_psckill.  The factors are used only to certify the two local
reductions of the fixed finite witness.  Unlike the discovery scan, this
source forms every defining Sylvester-map matrix for j=0,...,47 directly.
"""

import hashlib
import json
import os
import time


FAMILY = "F04_psckill"
N = 79403
FACTORS = (271, 293)
R = 269
SHIFT = 1
LAST_INDEX = 47


def quotient_power(base, exponent, modulus):
    result = base.parent().one()
    while exponent:
        if exponent & 1:
            result = (result * base).mod(modulus)
        exponent >>= 1
        if exponent:
            base = (base * base).mod(modulus)
    return result


def local_error(characteristic):
    field = GF(characteristic)
    ring = PolynomialRing(field, "x")
    x = ring.gen()
    p_polynomial = x**R - 1
    h = quotient_power(x + field(SHIFT), N, p_polynomial)
    h -= x ** (N % R)
    h -= field(SHIFT)
    return field, p_polynomial, h


def determinant_at(field, p_polynomial, h, formal_n, j):
    rows = range(j, R + formal_n - j)
    columns = []
    for polynomial, shift_count in ((p_polynomial, formal_n - j), (h, R - j)):
        for column_shift in range(shift_count):
            columns.append([
                field(polynomial[degree - column_shift])
                if degree >= column_shift else field(0)
                for degree in rows
            ])
    dimension = R + formal_n - 2 * j
    defining_matrix = matrix(
        field, dimension, dimension,
        lambda row, column: columns[column][row],
    )
    return int(defining_matrix.det())


def main():
    started = time.monotonic()
    local_data = [local_error(characteristic) for characteristic in FACTORS]
    formal_n = max(int(item[2].degree()) for item in local_data)
    residue_rows = []
    digest = hashlib.sha256()
    for j in range(LAST_INDEX + 1):
        residues = [
            determinant_at(field, p_polynomial, h, formal_n, j)
            for field, p_polynomial, h in local_data
        ]
        mismatch = (residues[0] == 0) != (residues[1] == 0)
        residue_rows.append({"index": j, "residues": residues, "zero_mismatch": mismatch})
        for residue in residues:
            digest.update(int(residue).to_bytes(4, "big"))
        print(f"family={FAMILY} index={j}/{LAST_INDEX} mismatch={mismatch}", flush=True)
    assert all(not row["zero_mismatch"] for row in residue_rows[:-1])
    assert residue_rows[-1] == {"index": 47, "residues": [0, 173], "zero_mismatch": True}
    result = {
        "approach_family": FAMILY,
        "source": os.path.abspath(__file__),
        "N": N,
        "factors_used_for_finite_local_certificate": list(FACTORS),
        "r": R,
        "shift": SHIFT,
        "global_formal_degree": formal_n,
        "local_degrees": [int(item[2].degree()) for item in local_data],
        "checked_indices": [0, LAST_INDEX],
        "first_mismatch": residue_rows[-1],
        "all_residues": residue_rows,
        "residue_sequence_sha256": digest.hexdigest(),
        "elapsed_seconds": time.monotonic() - started,
    }
    output = "experiments/F04_psckill/output/F04-PSC-R06.json"
    with open(output, "w") as handle:
        json.dump(result, handle, indent=2, sort_keys=True, default=int)
        handle.write("\n")


main()
