#!/usr/bin/env python3
"""Independent hostile verifier for F103.

This verifier does not import the F103 candidate or the pinned F98 module.  It
reconstructs the public record stream and P66 rows locally, then compares its
results with the frozen candidate and F102 artifacts.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import re
import sys
import time
import traceback
from collections import Counter, deque
from pathlib import Path


EXPECTED_N = 202_537_109
PREFIX_RAW_COUNT = 5_616


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_nth_root(value: int, exponent: int) -> int | None:
    low = 1
    high = 1 << ((value.bit_length() + exponent - 1) // exponent + 1)
    while low + 1 < high:
        middle = (low + high) // 2
        power = middle**exponent
        if power == value:
            return middle
        if power < value:
            low = middle
        else:
            high = middle
    return low if low**exponent == value else None


def primitive_root(value: int) -> tuple[int, int]:
    for exponent in range(value.bit_length(), 1, -1):
        root = exact_nth_root(value, exponent)
        if root is not None:
            return root, exponent
    return value, 1


def seed_gcd_basis(endpoint_values: list[int]):
    """Independent FIFO gcd refinement with full endpoint exponents."""
    pending = deque(
        (value, {endpoint: 1})
        for endpoint, value in enumerate(endpoint_values)
        if value > 1
    )
    stable: list[tuple[int, dict[int, int]]] = []

    while pending:
        value, signature = pending.popleft()
        if value == 1:
            continue
        root, power = primitive_root(value)
        if power > 1:
            value = root
            signature = {endpoint: exponent * power for endpoint, exponent in signature.items()}

        for position, (old_value, old_signature) in enumerate(stable):
            common = math.gcd(value, old_value)
            if common == 1:
                continue
            stable.pop(position)
            if value == old_value:
                merged = dict(signature)
                for endpoint, exponent in old_signature.items():
                    merged[endpoint] = merged.get(endpoint, 0) + exponent
                pending.append((value, merged))
                break
            pending.extend(
                (
                    (common, signature),
                    (value // common, signature),
                    (common, old_signature),
                    (old_value // common, old_signature),
                )
            )
            break
        else:
            stable.append((value, signature))

    stable.sort(key=lambda item: item[0])
    prefix = 1
    reconstructed = [1] * len(endpoint_values)
    for value, signature in stable:
        if primitive_root(value)[1] != 1:
            raise AssertionError("seed basis retained a perfect power")
        if math.gcd(prefix, value) != 1:
            raise AssertionError("seed basis is not pairwise coprime")
        prefix *= value
        for endpoint, exponent in signature.items():
            reconstructed[endpoint] *= value**exponent
    if reconstructed != endpoint_values:
        raise AssertionError("seed basis does not reconstruct endpoints")
    return stable


def seed_columns(basis: list[tuple[int, dict[int, int]]], relation_count: int):
    incidence: list[list[tuple[int, int]]] = [[] for _ in range(2 * relation_count)]
    for block, (_, signature) in enumerate(basis):
        for endpoint, exponent in signature.items():
            incidence[endpoint].append((block, exponent))
    columns = []
    for relation in range(relation_count):
        column: dict[int, int] = {}
        for endpoint in (2 * relation, 2 * relation + 1):
            for block, exponent in incidence[endpoint]:
                column[block] = column.get(block, 0) + exponent
        columns.append(column)
    return columns


def generate_records(modulus: int):
    n = modulus.bit_length()
    bound = n * n
    trial_hits = []
    for value in range(2, bound + 1):
        divisor = math.gcd(value, modulus)
        if 1 < divisor < modulus:
            trial_hits.append((value, divisor))

    records: list[dict[str, object]] = []
    endpoints: list[int] = []
    seen_residues: set[int] = set()
    direct_hits: list[dict[str, object]] = []

    def retain(c: int, provenance: dict[str, object]) -> None:
        if c in seen_residues:
            return
        seen_residues.add(c)
        w = pow(c, -1, modulus)
        minus = math.gcd(c - w, modulus)
        plus = math.gcd(c + w, modulus)
        if 1 < minus < modulus or 1 < plus < modulus:
            direct_hits.append(
                {
                    "c": c,
                    "w": w,
                    "gcd_minus": minus,
                    "gcd_plus": plus,
                    "provenance": provenance,
                }
            )
            return
        records.append({"c": c, "w": w, "P": c * w, "provenance": provenance})
        endpoints.extend((c, w))

    for seed in range(2, n + 1):
        retain(seed, {"kind": "initial_seed", "seed": seed})

    initial_basis = seed_gcd_basis(endpoints)
    columns = seed_columns(initial_basis, len(records))
    active: list[tuple[int, tuple[int, int]]] = []
    for relation, column in enumerate(columns):
        if not any(exponent & 1 for exponent in column.values()):
            continue
        full_support = sorted(initial_basis[block][0] for block in column)
        pair = (full_support[0], 1) if len(full_support) == 1 else tuple(full_support[:2])
        active.append((relation, pair))
        if len(active) == n:
            break

    for relation, (u, v) in active:
        u_power = 1
        v_power = 1
        for exponent in range(bound + 1):
            for orientation, c in (
                ("u_power_times_v", u_power * v % modulus),
                ("u_times_v_power", u * v_power % modulus),
            ):
                retain(
                    c,
                    {
                        "kind": "feedback_trajectory",
                        "active_relation_index_zero_based": relation,
                        "u": u,
                        "v": v,
                        "exponent": exponent,
                        "orientation": orientation,
                    },
                )
            u_power = u_power * u % modulus
            v_power = v_power * v % modulus

    unique_records: list[tuple[int, dict[str, object]]] = []
    seen_values: set[int] = set()
    removed_ones = 0
    removed_duplicates = 0
    for raw_index, record in enumerate(records):
        value = int(record["P"])
        if value == 1:
            removed_ones += 1
            continue
        if value in seen_values:
            removed_duplicates += 1
            continue
        seen_values.add(value)
        unique_records.append((raw_index, record))

    return {
        "n": n,
        "B": bound,
        "trial_hits": trial_hits,
        "direct_hits": direct_hits,
        "records": records,
        "unique_records": unique_records,
        "removed_ones": removed_ones,
        "removed_duplicates": removed_duplicates,
        "active": active,
        "seed_basis_blocks": len(initial_basis),
    }


def p66_rows(unique_records: list[tuple[int, dict[str, object]]], progress_label: str):
    work: list[tuple[int, int]] = []
    relation_values = []
    for column, (_, record) in enumerate(unique_records):
        c = int(record["c"])
        w = int(record["w"])
        product = int(record["P"])
        if c * w != product or product % EXPECTED_N != 1:
            raise AssertionError("invalid exact relation in P66 input")
        mask = 1 << column
        work.extend(((c, mask), (w, mask)))
        relation_values.append(product)

    stable: list[tuple[int, int]] = []
    refinements = 0
    gcd_tests = 0
    next_progress = 200_000_000
    while work:
        value, mask = work.pop()
        for position, (basis_value, basis_mask) in enumerate(stable):
            gcd_tests += 1
            if gcd_tests == next_progress:
                print(
                    f"{progress_label}: gcd_tests={gcd_tests} stable={len(stable)} work={len(work)}",
                    flush=True,
                )
                next_progress += 200_000_000
            divisor = math.gcd(value, basis_value)
            if divisor == 1:
                continue
            stable.pop(position)
            refinements += 1
            for new_value, new_mask in (
                (divisor, mask ^ basis_mask),
                (value // divisor, mask),
                (basis_value // divisor, basis_mask),
            ):
                if new_value > 1 and new_mask:
                    work.append((new_value, new_mask))
            break
        else:
            stable.append((value, mask))

    prefix_product = 1
    square_blocks = 0
    rows = []
    for value, mask in stable:
        if math.gcd(prefix_product, value) != 1:
            raise AssertionError("P66 output blocks are not pairwise coprime")
        prefix_product *= value
        root = math.isqrt(value)
        if root * root == value:
            square_blocks += 1
        else:
            rows.append(mask)
    print(
        f"{progress_label}: done gcd_tests={gcd_tests} rows={len(rows)} refinements={refinements}",
        flush=True,
    )
    return {
        "rows": rows,
        "values": relation_values,
        "coprime_blocks": len(stable),
        "square_blocks": square_blocks,
        "refinements": refinements,
        "gcd_tests": gcd_tests,
        "row_multiset_sha256": hashlib.sha256(
            ",".join(map(str, sorted(rows))).encode()
        ).hexdigest(),
    }


def gf2_rank(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = original
        while row:
            low = row & -row
            pivot = low.bit_length() - 1
            known = pivots.get(pivot)
            if known is None:
                pivots[pivot] = row
                break
            row ^= known
    return len(pivots)


def candidate_kernel_basis(rows: list[int], column_count: int) -> list[int]:
    pivots: dict[int, int] = {}
    for original in rows:
        row = original
        while row:
            pivot = row.bit_length() - 1
            known = pivots.get(pivot)
            if known is None:
                pivots[pivot] = row
                break
            row ^= known
    kernel = []
    pivot_columns = set(pivots)
    for free_column in range(column_count):
        if free_column in pivot_columns:
            continue
        vector = 1 << free_column
        for pivot in sorted(pivots):
            if (pivots[pivot] & vector).bit_count() & 1:
                vector ^= 1 << pivot
        if any((row & vector).bit_count() & 1 for row in pivots.values()):
            raise AssertionError("independent kernel reconstruction failed")
        kernel.append(vector)
    return kernel


def bit_indices(mask: int) -> list[int]:
    result = []
    while mask:
        bit = mask & -mask
        result.append(bit.bit_length() - 1)
        mask ^= bit
    return result


def exact_root_evidence(values: list[int], columns: list[int], modulus: int):
    product = math.prod(values[column] for column in columns)
    root = math.isqrt(product)
    if root * root != product:
        raise AssertionError("selected relation product is not an exact square")
    return {
        "support": len(columns),
        "root_mod_N": root % modulus,
        "gcd_minus": math.gcd(root - 1, modulus),
        "gcd_plus": math.gcd(root + 1, modulus),
        "exact_root_digits": len(str(root)),
        "exact_root_sha256": hashlib.sha256(str(root).encode()).hexdigest(),
    }


def simultaneous_peel(rows: list[int], column_count: int):
    active = (1 << column_count) - 1
    iterations = 0
    removed_by_round = []
    while True:
        forced = 0
        for row in rows:
            support = row & active
            if support and not support & (support - 1):
                forced |= support
        if not forced:
            break
        active &= ~forced
        removed_by_round.append(forced.bit_count())
        iterations += 1
    return active, iterations, removed_by_round


def heap_peel(rows: list[int], column_count: int, largest_row_first: bool):
    import heapq

    active = (1 << column_count) - 1
    degrees = [row.bit_count() for row in rows]
    column_rows: list[list[int]] = [[] for _ in range(column_count)]
    for row_index, row in enumerate(rows):
        value = row
        while value:
            bit = value & -value
            column_rows[bit.bit_length() - 1].append(row_index)
            value ^= bit
    heap = [(-row if largest_row_first else row) for row, degree in enumerate(degrees) if degree == 1]
    heapq.heapify(heap)
    while heap:
        encoded = heapq.heappop(heap)
        row = -encoded if largest_row_first else encoded
        if degrees[row] != 1:
            continue
        lone = rows[row] & active
        if lone.bit_count() != 1:
            raise AssertionError("sequential peel encountered inconsistent degree")
        active ^= lone
        column = lone.bit_length() - 1
        for incident in column_rows[column]:
            degrees[incident] -= 1
            if degrees[incident] == 1:
                heapq.heappush(heap, -incident if largest_row_first else incident)
    return active


def component_sizes(rows: list[int], core_columns: list[int]):
    position = {column: index for index, column in enumerate(core_columns)}
    parent = list(range(len(core_columns)))
    sizes = [1] * len(core_columns)

    def find(item: int) -> int:
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def union(left: int, right: int) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root == right_root:
            return
        if sizes[left_root] < sizes[right_root]:
            left_root, right_root = right_root, left_root
        parent[right_root] = left_root
        sizes[left_root] += sizes[right_root]

    active = sum(1 << column for column in core_columns)
    for row in rows:
        support = bit_indices(row & active)
        if len(support) < 2:
            continue
        first = position[support[0]]
        for column in support[1:]:
            union(first, position[column])
    counts = Counter(find(index) for index in range(len(core_columns)))
    return sorted(counts.values(), reverse=True)


def summarize_matrix(matrix: dict[str, object], column_count: int):
    rows = list(matrix["rows"])
    rank = gf2_rank(rows)
    simultaneous, rounds, round_counts = simultaneous_peel(rows, column_count)
    smallest = heap_peel(rows, column_count, False)
    largest = heap_peel(rows, column_count, True)
    if not simultaneous == smallest == largest:
        raise AssertionError("independent peeling schedules disagree")
    columns = bit_indices(simultaneous)
    core_rows = [row & simultaneous for row in rows if row & simultaneous]
    core_rank = gf2_rank(core_rows)
    return {
        "columns": column_count,
        "rows": len(rows),
        "rank": rank,
        "nullity": column_count - rank,
        "initial_degree_one_rows": sum(row.bit_count() == 1 for row in rows),
        "peeled_columns": column_count - len(columns),
        "core_columns": len(columns),
        "core_rows": len(core_rows),
        "core_rank": core_rank,
        "core_nullity": len(columns) - core_rank,
        "kernel_preserved": column_count - rank == len(columns) - core_rank,
        "order_schedules_equal": True,
        "simultaneous_rounds": rounds,
        "simultaneous_removed_by_round": round_counts,
        "core_component_sizes": component_sizes(rows, columns),
        "core_columns_zero_based": columns,
        "core_columns_sha256": hashlib.sha256(
            ",".join(map(str, columns)).encode()
        ).hexdigest(),
    }


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = call_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def static_source_audit(candidate_source: Path, f98_source: Path):
    allowed_import_roots = {
        "__future__",
        "argparse",
        "hashlib",
        "importlib",
        "json",
        "math",
        "time",
        "collections",
        "pathlib",
    }
    forbidden_call_tails = {
        "factor",
        "factorint",
        "factor_integer",
        "is_prime",
        "isprime",
        "prime_factors",
        "multiplicative_order",
        "order",
        "discrete_log",
    }
    result = {}
    for label, path in (("candidate", candidate_source), ("pinned_f98", f98_source)):
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(path))
        imports = set()
        calls = []
        large_integer_literals = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                imports.add(node.module or "")
            elif isinstance(node, ast.Call):
                calls.append(call_name(node.func))
            elif isinstance(node, ast.Constant) and isinstance(node.value, int) and node.value >= 1_000:
                large_integer_literals.append(node.value)
        forbidden_calls = sorted(
            name for name in calls if name.rsplit(".", 1)[-1] in forbidden_call_tails
        )
        disallowed_imports = sorted(
            name for name in imports if name.split(".", 1)[0] not in allowed_import_roots
        )
        result[label] = {
            "sha256": sha256_file(path),
            "imports": sorted(imports),
            "disallowed_imports": disallowed_imports,
            "forbidden_calls": forbidden_calls,
            "large_integer_literals": sorted(set(large_integer_literals)),
        }
    result["candidate_import_target_literal_present"] = "public_factorization_free_replay.py" in candidate_source.read_text(encoding="utf-8")
    result["no_forbidden_operations_found"] = all(
        not result[label]["disallowed_imports"] and not result[label]["forbidden_calls"]
        for label in ("candidate", "pinned_f98")
    )
    return result


def parse_manifest_hashes(manifest: Path):
    entries = {}
    pattern = re.compile(r"^([0-9a-f]{64})\s+(.+)$")
    for line in manifest.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            entries[match.group(2)] = match.group(1)
    return entries


def run(args: argparse.Namespace):
    started = time.monotonic()
    candidate_dir = args.candidate_dir.resolve()
    f98_source = args.f98_source.resolve()
    f102_output_path = args.f102_output.resolve()
    candidate_source = candidate_dir / "public_core_replay.py"
    candidate_output_path = candidate_dir / "OUTPUT.json"
    manifest_path = candidate_dir / "RUN_MANIFEST.md"

    failures: list[str] = []
    checks = 0

    def check(label: str, actual: object, expected: object) -> None:
        nonlocal checks
        checks += 1
        if actual != expected:
            failures.append(f"{label}: expected {expected!r}, got {actual!r}")

    manifest_hashes = parse_manifest_hashes(manifest_path)
    manifest_actual = {}
    for relative, expected_hash in manifest_hashes.items():
        path = (candidate_dir / relative).resolve()
        actual_hash = sha256_file(path)
        manifest_actual[relative] = actual_hash
        check(f"manifest hash {relative}", actual_hash, expected_hash)

    candidate_output = json.loads(candidate_output_path.read_text(encoding="utf-8"))
    f102_output = json.loads(f102_output_path.read_text(encoding="utf-8"))
    source_audit = static_source_audit(candidate_source, f98_source)
    check("candidate/F98 forbidden static calls", source_audit["no_forbidden_operations_found"], True)
    check("candidate import target", source_audit["candidate_import_target_literal_present"], True)
    check("candidate F98 source hash", candidate_output["f98_source_sha256"], sha256_file(f98_source))

    replay = generate_records(EXPECTED_N)
    records = replay["records"]
    unique_records = replay["unique_records"]
    check("N", candidate_output["N"], EXPECTED_N)
    check("n", replay["n"], 28)
    check("B", replay["B"], 784)
    check("trial hits", replay["trial_hits"], [])
    check("direct sign hits", replay["direct_hits"], [])
    check("retained relations", len(records), 12_549)
    check("candidate retained relations", candidate_output["retained_relation_count"], len(records))
    check("removed P=1", replay["removed_ones"], 1)
    check("removed duplicate values", replay["removed_duplicates"], 3_134)
    check("unique relations", len(unique_records), 9_414)
    check("candidate unique relations", candidate_output["unique_relation_count"], len(unique_records))
    active_pairs = [list(pair) for _, pair in replay["active"]]
    check("active pairs", candidate_output["active_pairs"], active_pairs)
    print(
        f"replay: records={len(records)} unique={len(unique_records)} active_pairs={len(active_pairs)}",
        flush=True,
    )

    full_matrix = p66_rows(unique_records, "full P66")
    full = summarize_matrix(full_matrix, len(unique_records))
    prefix_records = [item for item in unique_records if item[0] < PREFIX_RAW_COUNT]
    prefix_matrix = p66_rows(prefix_records, "prefix P66")
    prefix = summarize_matrix(prefix_matrix, len(prefix_records))

    expected_full = {
        "columns": 9_414,
        "rows": 11_015,
        "rank": 8_926,
        "nullity": 488,
        "initial_degree_one_rows": 7_866,
        "peeled_columns": 7_633,
        "core_columns": 1_781,
        "core_rows": 1_298,
        "core_rank": 1_293,
        "core_nullity": 488,
        "kernel_preserved": True,
        "core_component_sizes": [1_781],
        "core_columns_sha256": "5e18521931048141bdc4c09f23af1b8b9e7d0b5b95bb70b42b420443c6f2cbc8",
    }
    expected_prefix = {
        "columns": 4_293,
        "rows": 5_607,
        "rank": 4_291,
        "nullity": 2,
        "initial_degree_one_rows": 4_012,
        "peeled_columns": 3_920,
        "core_columns": 373,
        "core_rows": 387,
        "core_rank": 371,
        "core_nullity": 2,
        "kernel_preserved": True,
        "core_component_sizes": [373],
        "core_columns_sha256": "9b75bad6177686931cc714931b37bdf4e42823db4d0121b7e8859dff3c1260df",
    }
    for label, actual, expected in (("full", full, expected_full), ("prefix", prefix, expected_prefix)):
        for key, expected_value in expected.items():
            check(f"{label} {key}", actual[key], expected_value)
            candidate_section = candidate_output["full" if label == "full" else "raw_prefix_5616"]
            check(f"candidate {label} {key}", candidate_section[key], actual[key])
        check(f"{label} three peeling schedules", actual["order_schedules_equal"], True)

    for label, matrix, expected_stats in (
        (
            "full",
            full_matrix,
            {"coprime_blocks": 11_015, "square_blocks": 0, "refinements": 62_643, "gcd_tests": 814_589_842},
        ),
        (
            "prefix",
            prefix_matrix,
            {"coprime_blocks": 5_607, "square_blocks": 0, "refinements": 27_865, "gcd_tests": 193_286_162},
        ),
    ):
        candidate_stats = candidate_output[f"{label}_matrix_stats"]
        for key, expected_value in expected_stats.items():
            check(f"{label} P66 {key}", matrix[key], expected_value)
            check(f"candidate {label} P66 {key}", candidate_stats[key], matrix[key])

    check("F102 full core hash", f102_output["full"]["core_columns_sha256"], full["core_columns_sha256"])
    check("F102 prefix core hash", f102_output["raw_prefix_5616"]["core_columns_sha256"], prefix["core_columns_sha256"])
    check("F102 full core columns", f102_output["full"]["core_columns"], full["core_columns"])
    check("F102 prefix core columns", f102_output["raw_prefix_5616"]["core_columns"], prefix["core_columns"])

    core_set = set(full["core_columns_zero_based"])
    provenance_kinds = Counter()
    provenance_families = Counter()
    provenance_orientations = Counter()
    for column in core_set:
        provenance = unique_records[column][1]["provenance"]
        kind = str(provenance["kind"])
        provenance_kinds[kind] += 1
        if kind == "initial_seed":
            provenance_families[f"seed:{provenance['seed']}"] += 1
            provenance_orientations["seed"] += 1
        else:
            provenance_families[
                f"{provenance['active_relation_index_zero_based']}:"
                f"{provenance['u']}:{provenance['v']}"
            ] += 1
            provenance_orientations[str(provenance["orientation"])] += 1
    provenance = {
        "kinds": dict(sorted(provenance_kinds.items())),
        "families": dict(sorted(provenance_families.items())),
        "orientations": dict(sorted(provenance_orientations.items())),
    }
    check("candidate provenance kinds", candidate_output["full_core_provenance_counts"], provenance["kinds"])
    check("candidate provenance families", candidate_output["full_core_family_counts"], provenance["families"])
    check("candidate provenance orientations", candidate_output["full_core_orientation_counts"], provenance["orientations"])
    check("F102 provenance kinds", f102_output["full_core_provenance_counts"], provenance["kinds"])
    check("F102 provenance families", f102_output["full_core_family_counts"], provenance["families"])
    check("F102 provenance orientations", f102_output["full_core_orientation_counts"], provenance["orientations"])

    selected = candidate_output["first_useful_basis_vector"]["selected_columns_zero_based"]
    check("certificate support field", candidate_output["first_useful_basis_vector"]["support"], len(selected))
    check("certificate support", len(selected), 166)
    check("certificate columns distinct", len(set(selected)), len(selected))
    check("certificate equals F102", selected, f102_output["public_166_selected_columns_zero_based"])
    check("certificate inside core", set(selected).issubset(core_set), True)
    certificate_mask = sum(1 << column for column in selected)
    check(
        "certificate row parity",
        any((row & certificate_mask).bit_count() & 1 for row in full_matrix["rows"]),
        False,
    )
    certificate = exact_root_evidence(full_matrix["values"], selected, EXPECTED_N)
    check("certificate residue", certificate["root_mod_N"], 132_013_085)
    check("certificate gcd minus", certificate["gcd_minus"], 19_727)
    check("certificate gcd plus", certificate["gcd_plus"], 10_267)
    check(
        "candidate certificate residue",
        candidate_output["first_useful_basis_vector"]["root_mod_N"],
        certificate["root_mod_N"],
    )
    check(
        "candidate certificate gcd minus",
        candidate_output["first_useful_basis_vector"]["gcd_root_minus_one_N"],
        certificate["gcd_minus"],
    )
    check(
        "candidate certificate gcd plus",
        candidate_output["first_useful_basis_vector"]["gcd_root_plus_one_N"],
        certificate["gcd_plus"],
    )

    kernel = candidate_kernel_basis(full_matrix["rows"], len(unique_records))
    check("kernel dimension by reconstruction", len(kernel), 488)
    first_useful = None
    global_plus = 0
    global_minus = 0
    for ordinal, vector in enumerate(kernel, 1):
        columns = bit_indices(vector)
        evidence = exact_root_evidence(full_matrix["values"], columns, EXPECTED_N)
        if evidence["root_mod_N"] == 1:
            global_plus += 1
            continue
        if evidence["root_mod_N"] == EXPECTED_N - 1:
            global_minus += 1
            continue
        first_useful = {"basis_ordinal": ordinal, "columns": columns, **evidence}
        break
    if first_useful is None:
        failures.append("independent kernel basis has no useful vector")
    else:
        check("first useful columns", first_useful["columns"], selected)
        check("first useful residue", first_useful["root_mod_N"], 132_013_085)

    log_text = (candidate_dir / "RUN.log").read_text(encoding="utf-8")
    check("candidate run timeout", "timeout_seconds=180" in log_text, True)
    check("candidate run exit", "exit_code=0" in log_text, True)
    check("candidate output status", candidate_output["status"], "PASS")
    check("candidate forbidden list", candidate_output["forbidden_operations_used"], [])

    output = {
        "status": "PASS" if not failures else "FAIL",
        "failures": failures,
        "checks": checks,
        "elapsed_seconds": time.monotonic() - started,
        "independence": {
            "imports_candidate": False,
            "imports_pinned_f98": False,
            "record_generation": "local iterative modular replay",
            "seed_basis": "independent FIFO exact-root/gcd refinement",
            "peeling": "simultaneous fixed point plus min-row and max-row schedules",
            "rank": "independent lowest-pivot GF(2) elimination",
            "connectedness": "union-find on the core incidence graph",
        },
        "manifest_claimed_hashes": manifest_hashes,
        "manifest_actual_hashes": manifest_actual,
        "f102_output_sha256": sha256_file(f102_output_path),
        "static_source_audit": source_audit,
        "replay": {
            "N": EXPECTED_N,
            "n": replay["n"],
            "B": replay["B"],
            "trial_hits": replay["trial_hits"],
            "direct_hits": replay["direct_hits"],
            "retained_relations": len(records),
            "removed_P_equals_1": replay["removed_ones"],
            "removed_duplicate_values": replay["removed_duplicates"],
            "unique_relations": len(unique_records),
            "seed_basis_blocks": replay["seed_basis_blocks"],
            "active_pairs": active_pairs,
        },
        "full_matrix_stats": {key: full_matrix[key] for key in ("coprime_blocks", "square_blocks", "refinements", "gcd_tests", "row_multiset_sha256")},
        "prefix_matrix_stats": {key: prefix_matrix[key] for key in ("coprime_blocks", "square_blocks", "refinements", "gcd_tests", "row_multiset_sha256")},
        "full": full,
        "raw_prefix_5616": prefix,
        "provenance": provenance,
        "certificate": certificate,
        "certificate_columns_zero_based": selected,
        "kernel_basis": {
            "dimension": len(kernel),
            "global_plus_before_first_useful": global_plus,
            "global_minus_before_first_useful": global_minus,
            "first_useful": first_useful,
        },
        "F102_comparison": {
            "full_prime_rows": f102_output["full"]["row_count"],
            "full_public_rows": full["rows"],
            "full_prime_core_rows": f102_output["full"]["core_rows"],
            "full_public_core_rows": full["core_rows"],
            "full_core_hash_equal": f102_output["full"]["core_columns_sha256"] == full["core_columns_sha256"],
            "prefix_prime_rows": f102_output["raw_prefix_5616"]["row_count"],
            "prefix_public_rows": prefix["rows"],
            "prefix_core_hash_equal": f102_output["raw_prefix_5616"]["core_columns_sha256"] == prefix["core_columns_sha256"],
        },
    }
    return output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-dir", type=Path, required=True)
    parser.add_argument("--f98-source", type=Path, required=True)
    parser.add_argument("--f102-output", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        output = run(args)
    except BaseException as error:
        output = {
            "status": "FAIL",
            "failures": [f"{type(error).__name__}: {error}"],
            "traceback": traceback.format_exc(),
        }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"strict_status={output['status']}", flush=True)
    for failure in output.get("failures", []):
        print(f"FAIL: {failure}", flush=True)
    return 0 if output["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
