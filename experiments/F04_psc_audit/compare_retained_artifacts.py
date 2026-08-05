"""Cross-check the independent F04 PSC audit against retained C13 artifacts.

Approach-family ID: F04_psc_audit.  This script performs no mathematics; it
checks that independently generated certificate fields and the full decisive
prefix agree with the retained outputs byte-for-value where applicable.
"""

import argparse
import hashlib
import json
import os
import time


FAMILY = "F04_psc_audit"


def file_sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path):
    with open(path) as handle:
        return json.load(handle)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--retained-global", required=True)
    parser.add_argument("--retained-prefix", required=True)
    parser.add_argument("--retained-discovery", required=True)
    parser.add_argument("--independent-global", required=True)
    parser.add_argument("--independent-local", required=True)
    parser.add_argument("--source", action="append", default=[])
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = time.monotonic()

    retained_global = load_json(args.retained_global)
    retained_prefix = load_json(args.retained_prefix)
    retained_discovery = load_json(args.retained_discovery)
    independent_global = load_json(args.independent_global)
    independent_local = load_json(args.independent_local)

    global_comparisons = {
        "global_degree_H": (
            retained_global["global_degree_H"],
            independent_global["global_degree_H"],
        ),
        "global_H_leading_coefficient_mod_N": (
            retained_global["global_H_leading_coefficient_mod_N"],
            independent_global["global_H_leading_coefficient_mod_N"],
        ),
        "global_H_sha256": (
            retained_global["global_H_sha256"],
            independent_global["global_H_sha256"],
        ),
        "matrix_dimension": (
            retained_global["matrix_dimension"],
            independent_global["first_nontrivial_gcd"]["matrix_dimension"],
        ),
        "determinant_mod_N": (
            retained_global["determinant_mod_N"],
            independent_global["first_nontrivial_gcd"]["determinant_mod_N"],
        ),
        "gcd_with_N": (
            retained_global["gcd_with_N"],
            independent_global["first_nontrivial_gcd"]["gcd_with_N"],
        ),
        "cofactor": (
            retained_global["cofactor_after_gcd"],
            independent_global["recovered_cofactor"],
        ),
        "integer_determinant_bit_length": (
            retained_global["integer_determinant_bit_length"],
            independent_global["first_nontrivial_gcd"][
                "integer_determinant_bit_length"
            ],
        ),
    }
    assert all(left == right for left, right in global_comparisons.values())

    retained_rows = retained_prefix["all_residues"]
    independent_rows = [
        {
            "index": row["index"],
            "residues": row["residues"],
            "zero_mismatch": row["zero_mismatch"],
        }
        for row in independent_local["determinant_rows"][: len(retained_rows)]
    ]
    assert retained_rows == independent_rows
    prefix_digest = hashlib.sha256()
    for row in independent_rows:
        for residue in row["residues"]:
            prefix_digest.update(residue.to_bytes(4, "big"))
    assert prefix_digest.hexdigest() == retained_prefix["residue_sequence_sha256"]
    assert retained_prefix["local_degrees"] == independent_local["local_degrees"]
    assert retained_prefix["first_mismatch"] == {
        "index": independent_local["first_zero_mismatch"]["index"],
        "residues": independent_local["first_zero_mismatch"]["residues"],
        "zero_mismatch": independent_local["first_zero_mismatch"]["zero_mismatch"],
    }

    discovery_first = retained_discovery["first_mismatch"]
    assert discovery_first["index"] == independent_local["first_zero_mismatch"]["index"]
    assert discovery_first["defining_determinant_mod_p"] == independent_local[
        "first_zero_mismatch"
    ]["residues"][0]
    assert discovery_first["defining_determinant_mod_q"] == independent_local[
        "first_zero_mismatch"
    ]["residues"][1]
    discovery_row = retained_discovery["rows"][0]
    independent_mismatches = [
        row["index"]
        for row in independent_local["determinant_rows"]
        if row["zero_mismatch"]
    ]
    independent_zeros = [
        [
            row["index"]
            for row in independent_local["determinant_rows"]
            if row["residues"][component] == 0
        ]
        for component in range(2)
    ]
    assert independent_mismatches == discovery_row["mismatch_indices"]
    assert independent_zeros[0] == discovery_row["zero_indices_mod_p"]
    assert independent_zeros[1] == discovery_row["zero_indices_mod_q"]

    result = {
        "approach_family": FAMILY,
        "source": os.path.abspath(__file__),
        "global_field_comparisons": {
            key: {"retained": values[0], "independent": values[1], "match": True}
            for key, values in global_comparisons.items()
        },
        "full_prefix_rows_compared": len(retained_rows),
        "full_prefix_exact_match": True,
        "full_direct_zero_masks_match_discovery_PRS_masks": True,
        "full_direct_mismatch_indices_match_discovery": True,
        "discovery_decisive_residues_match": True,
        "source_sha256": {
            os.path.abspath(path): file_sha256(path) for path in args.source
        },
        "elapsed_seconds": time.monotonic() - started,
        "audit_passed": True,
    }
    with open(args.output, "w") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps(result, sort_keys=True), flush=True)


main()
