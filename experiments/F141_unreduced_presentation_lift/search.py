from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

from sage.all import GF, Integer, matrix, proof


proof.all(True)

HERE = Path(__file__).resolve().parent


def proper_gcd(d, n):
    return 1 < d < n


def parity_support(value):
    return tuple(
        int(prime) for prime, exponent in Integer(value).factor()
        if exponent % 2
    )


def ledger_record(values, residues, n):
    supports = [parity_support(value) for value in values]
    rows = sorted({prime for support in supports for prime in support})
    row_index = {prime: index for index, prime in enumerate(rows)}
    columns = [
        sum(Integer(1) << row_index[prime] for prime in support)
        for support in supports
    ]
    parity_matrix = matrix(
        GF(2),
        len(rows),
        len(values),
        lambda row, column: (columns[column] >> row) & 1,
    )
    kernel_basis = parity_matrix.right_kernel().basis()
    basis_records = []
    image_non_global = False
    for vector in kernel_basis:
        selected = [index for index, bit in enumerate(vector) if bit]
        product = Integer(1)
        for index in selected:
            product *= values[index]
        if not product.is_square():
            raise RuntimeError("kernel vector did not give an exact square")
        root = product.sqrt()
        minus = root.__sub__(1).gcd(n)
        plus = root.__add__(1).gcd(n)
        useful = proper_gcd(minus, n) or proper_gcd(plus, n)
        image_non_global = image_non_global or useful
        basis_records.append(
            {
                "selected_indices": selected,
                "selected_residues": [int(residues[index]) for index in selected],
                "weight": len(selected),
                "root_mod_N": int(root % n),
                "minus_gcd": int(minus),
                "plus_gcd": int(plus),
                "useful": bool(useful),
            }
        )
    return {
        "rows": rows,
        "columns": [int(column) for column in columns],
        "rank": int(parity_matrix.rank()),
        "nullity": int(len(values) - parity_matrix.rank()),
        "image_non_global": bool(image_non_global),
        "basis_records": basis_records,
    }


def subset_record(indices, values, residues, n):
    product = Integer(1)
    for index in indices:
        product *= values[index]
    if not product.is_square():
        return None
    root = product.sqrt()
    minus = (root - 1).gcd(n)
    plus = (root + 1).gcd(n)
    if not (proper_gcd(minus, n) or proper_gcd(plus, n)):
        return None
    return {
        "selected_indices": list(indices),
        "selected_exponents": [indices[index] + 1 for index in range(len(indices))],
        "selected_residues": [int(residues[index]) for index in indices],
        "values": [int(values[index]) for index in indices],
        "root_mod_N": int(root % n),
        "minus_gcd": int(minus),
        "plus_gcd": int(plus),
    }


def first_low_weight_witness(values, residues, n, same_residue):
    supports = [set(parity_support(value)) for value in values]
    for weight in (1, 2, 3):
        for indices in combinations(range(len(values)), weight):
            selected_residues = [residues[index] for index in indices]
            if same_residue:
                if weight != 2 or selected_residues[0] != selected_residues[1]:
                    continue
            elif weight < 2 or len(set(selected_residues)) != weight:
                continue
            if not same_residue:
                # Require a binary circuit, not a union of smaller square
                # subsets.  At weights two and three this is equivalent to
                # nonzero, pairwise-distinct column supports.
                selected_supports = [supports[index] for index in indices]
                if any(not support for support in selected_supports):
                    continue
                if len({tuple(sorted(support)) for support in selected_supports}) != weight:
                    continue
            parity = set()
            for index in indices:
                parity.symmetric_difference_update(supports[index])
            if parity:
                continue
            record = subset_record(indices, values, residues, n)
            if record is not None:
                record["weight"] = weight
                return record
    return None


def fixed_certificate():
    p = Integer(1238926361552897)
    q = Integer(5704689200685129054721)
    n_value = p * q
    m = Integer(256)
    bit_parameter = Integer((n_value + 1).nbits())
    l_parameter = Integer((bit_parameter + 1).nbits())
    e_cap = Integer(2) ** (l_parameter ** 2)
    u1 = Integer(2)
    u2 = Integer(2) ** (2 * m + 1)
    residue = Integer(2)
    inverse = (n_value + 1) // 2
    canonical = residue * inverse
    lift1 = u1 * inverse
    lift2 = u2 * inverse
    product = lift1 * lift2
    root = Integer(2) ** (m + 1) * inverse
    checks = {
        "p_prime": bool(p.is_prime(proof=True)),
        "q_prime": bool(q.is_prime(proof=True)),
        "p_divides_plus": bool((Integer(2) ** m + 1) % p == 0),
        "q_divides_minus": bool((Integer(2) ** m - 1) % q == 0),
        "factors_exceed_seed_cap": bool(min(p, q) > e_cap + 1),
        "exponents_allowed": bool(2 * m + 1 <= e_cap),
        "base_two_is_seed": bool(2 <= e_cap + 1),
        "same_residue": bool(u1 % n_value == u2 % n_value == residue),
        "canonical_inverse": bool(inverse == residue.inverse_mod(n_value)),
        "minus_screen_null": bool((residue - inverse).gcd(n_value) == 1),
        "plus_screen_null": bool((residue + inverse).gcd(n_value) == 1),
        "canonical_value": bool(canonical == n_value + 1),
        "canonical_nonsquare": bool(not canonical.is_square()),
        "equal_lift_parity": bool(parity_support(lift1) == parity_support(lift2)),
        "lift_product_square": bool(product == root ** 2),
        "root_reduction": bool(root % n_value == Integer(2) ** m % n_value),
        "minus_gcd_is_q": bool((root - 1).gcd(n_value) == q),
        "plus_gcd_is_p": bool((root + 1).gcd(n_value) == p),
    }
    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "p": int(p),
        "q": int(q),
        "N": int(n_value),
        "N_bits": int(n_value.nbits()),
        "n": int(bit_parameter),
        "L": int(l_parameter),
        "E": int(e_cap),
        "m": int(m),
        "exponents": [1, int(2 * m + 1)],
        "residue": int(residue),
        "inverse": int(inverse),
        "canonical_value": int(canonical),
        "lift_values": [int(lift1), int(lift2)],
        "root_mod_N": int(root % n_value),
        "minus_gcd": int((root - 1).gcd(n_value)),
        "plus_gcd": int((root + 1).gcd(n_value)),
        "checks": checks,
    }


def small_corpus():
    primes = [Integer(value) for value in range(7, 200) if Integer(value).is_prime(proof=True)]
    summary = {
        "semiprimes": 0,
        "slice_direct_null": 0,
        "canonical_global_lifted_non_global": 0,
        "same_residue_useful_pair": 0,
        "all_distinct_useful_weight_two_or_three": 0,
        "canonical_global_lifted_non_global_with_all_distinct_circuit": 0,
        "useful_weight_one": 0,
    }
    first = {
        "canonical_global_lifted_non_global": None,
        "same_residue_useful_pair": None,
        "all_distinct_useful_weight_two_or_three": None,
        "canonical_global_lifted_non_global_with_all_distinct_circuit": None,
        "useful_weight_one": None,
    }
    for p, q in combinations(primes, 2):
        n_value = p * q
        summary["semiprimes"] += 1
        positions = []
        direct_null = True
        for exponent in range(1, 25):
            unreduced = Integer(2) ** exponent
            residue = unreduced % n_value
            if residue == 0:
                direct_null = False
                break
            inverse = residue.inverse_mod(n_value)
            minus = (residue - inverse).gcd(n_value)
            plus = (residue + inverse).gcd(n_value)
            if proper_gcd(minus, n_value) or proper_gcd(plus, n_value):
                direct_null = False
                break
            positions.append((exponent, unreduced, residue, inverse))
        if not direct_null:
            continue
        summary["slice_direct_null"] += 1

        canonical_values = []
        canonical_residues = []
        seen_residues = set()
        seen_values = set()
        for _, _, residue, inverse in positions:
            if residue in seen_residues:
                continue
            seen_residues.add(residue)
            value = residue * inverse
            if value == 1 or value in seen_values:
                continue
            seen_values.add(value)
            canonical_values.append(value)
            canonical_residues.append(residue)

        lifted_values = []
        lifted_residues = []
        lifted_exponents = []
        seen_lifts = set()
        for exponent, unreduced, residue, inverse in positions:
            value = unreduced * inverse
            if value == 1 or value in seen_lifts:
                continue
            seen_lifts.add(value)
            lifted_values.append(value)
            lifted_residues.append(residue)
            lifted_exponents.append(exponent)

        canonical = ledger_record(canonical_values, canonical_residues, n_value)
        lifted = ledger_record(lifted_values, lifted_residues, n_value)
        category = not canonical["image_non_global"] and lifted["image_non_global"]
        if category:
            summary["canonical_global_lifted_non_global"] += 1
            if first["canonical_global_lifted_non_global"] is None:
                useful_basis = next(item for item in lifted["basis_records"] if item["useful"])
                first["canonical_global_lifted_non_global"] = {
                    "p": int(p),
                    "q": int(q),
                    "N": int(n_value),
                    "canonical_rank": canonical["rank"],
                    "canonical_nullity": canonical["nullity"],
                    "lifted_rank": lifted["rank"],
                    "lifted_nullity": lifted["nullity"],
                    "useful_basis": useful_basis,
                    "useful_basis_exponents": [
                        lifted_exponents[index]
                        for index in useful_basis["selected_indices"]
                    ],
                    "useful_basis_values": [
                        int(lifted_values[index])
                        for index in useful_basis["selected_indices"]
                    ],
                }

        same = first_low_weight_witness(lifted_values, lifted_residues, n_value, True)
        if same is not None:
            summary["same_residue_useful_pair"] += 1
            if first["same_residue_useful_pair"] is None:
                same.update({"p": int(p), "q": int(q), "N": int(n_value)})
                same["selected_exponents"] = [lifted_exponents[index] for index in same["selected_indices"]]
                first["same_residue_useful_pair"] = same

        weight_one = None
        for index, value in enumerate(lifted_values):
            if parity_support(value):
                continue
            weight_one = subset_record((index,), lifted_values, lifted_residues, n_value)
            if weight_one is not None:
                break
        if weight_one is not None:
            summary["useful_weight_one"] += 1
            if first["useful_weight_one"] is None:
                weight_one.update({"p": int(p), "q": int(q), "N": int(n_value)})
                weight_one["selected_exponents"] = [lifted_exponents[index] for index in weight_one["selected_indices"]]
                first["useful_weight_one"] = weight_one

        distinct = first_low_weight_witness(lifted_values, lifted_residues, n_value, False)
        if distinct is not None:
            distinct.update({"p": int(p), "q": int(q), "N": int(n_value)})
            distinct["selected_exponents"] = [
                lifted_exponents[index] for index in distinct["selected_indices"]
            ]
            summary["all_distinct_useful_weight_two_or_three"] += 1
            if first["all_distinct_useful_weight_two_or_three"] is None:
                first["all_distinct_useful_weight_two_or_three"] = dict(distinct)
            if category:
                summary["canonical_global_lifted_non_global_with_all_distinct_circuit"] += 1
                if first["canonical_global_lifted_non_global_with_all_distinct_circuit"] is None:
                    first["canonical_global_lifted_non_global_with_all_distinct_circuit"] = dict(distinct)

    return {"summary": summary, "first_witnesses": first}


fixed = fixed_certificate()
corpus = small_corpus()
source_hash = sha256(Path(__file__).read_bytes()).hexdigest()
output = {
    "status": "PASS" if fixed["status"] == "PASS" else "FAIL",
    "source_sha256": source_hash,
    "fixed_certificate": fixed,
    "small_corpus": corpus,
}
serialized = json.dumps(output, sort_keys=True, indent=2)
(HERE / "OUTPUT.json").write_text(serialized + "\n", encoding="utf-8")
print(serialized)
