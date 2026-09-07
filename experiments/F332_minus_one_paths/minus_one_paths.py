#!/usr/bin/env python3
"""F332: bounded public a=-1 reflection and adjacent-block paths."""

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time
import traceback


ROOT = Path(__file__).resolve().parents[2]
F326_DIR = ROOT / "experiments" / "F326_direct_gauss_pairing"
F326_SOURCE = F326_DIR / "direct_gauss_pairing.py"
F326_SOURCE_SHA256 = "7829cc45822021c64c42842a2c938b15c52df85e30ae694efcdd4171c5012f73"
F328_INPUT = ROOT / "experiments" / "F328_capped_rabin_paths" / "moduli.json"
F328_INPUT_SHA256 = "acf09b285c57c39cfcb93d3cd77addce909498e224955fd0ec9d2e4d86ee0428"
F330_PROOF = ROOT / "experiments" / "F330_short_path_conditions" / "PROOF.md"
F330_RATIONAL = ROOT / "experiments" / "F330_short_path_conditions" / "RATIONAL_PATHS.md"
sys.path.insert(0, str(F326_DIR))
from direct_gauss_pairing import GaussPairing, auxiliary  # noqa: E402


INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024
LIFT_BIT_LIMIT = 4096
INITIAL_CAP = 8192
EXTENDED_CAP = 262144
METHODS = ("reflection", "adjacent_block")


def peak_rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    target = Path(path)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(target)


def centered_rep(value, n):
    h = (n - 1) // 2
    return (value + h) % n - h


def even_to_coordinate(u, n):
    h = (n - 1) // 2
    return u if u <= h else n - u


class WordStats:
    def __init__(self):
        self.counts = Counter()
        self.bigrams = Counter()
        self.maximum_same_run = Counter()
        self.previous = None
        self.same_run = 0
        self.alternating_run = 0
        self.maximum_alternating_run = 0
        self.length = 0

    def add(self, letter):
        self.counts[letter] += 1
        self.length += 1
        if letter == self.previous:
            self.same_run += 1
            self.alternating_run = 1
        else:
            self.same_run = 1
            self.alternating_run += 1
            if self.previous is not None:
                self.bigrams[self.previous + letter] += 1
        self.maximum_same_run[letter] = max(
            self.maximum_same_run[letter], self.same_run
        )
        self.maximum_alternating_run = max(
            self.maximum_alternating_run, self.alternating_run
        )
        self.previous = letter

    def record(self):
        return {
            "length": self.length,
            "counts": dict(self.counts),
            "bigram_counts": dict(self.bigrams),
            "maximum_same_run_by_letter": dict(self.maximum_same_run),
            "maximum_alternating_run": self.maximum_alternating_run,
        }


class LiftTracker:
    def __init__(self, u, v, n, positive, label):
        self.u = u
        self.v = v
        self.n = n
        self.positive = positive
        self.label = label
        self.active = True
        self.updates_recorded = 0
        self.maximum_bit_length = max(abs(u).bit_length(), abs(v).bit_length())
        self.saturation = None
        self.first_norm_gt_2n = None
        self.state_prefix = []
        self._record_state(0, "initial")

    def _record_state(self, update_index, letter):
        if len(self.state_prefix) < 32:
            self.state_prefix.append(
                {
                    "update_index": update_index,
                    "letter": letter,
                    "U": self.u,
                    "V": self.v,
                }
            )
        if self.positive and self.first_norm_gt_2n is None:
            norm = self.u * self.u + self.v * self.v
            if norm > 2 * self.n:
                self.first_norm_gt_2n = {
                    "update_index": update_index,
                    "letter": letter,
                    "U": self.u,
                    "V": self.v,
                    "norm": norm,
                    "two_N": 2 * self.n,
                }

    def update(self, new_u, new_v, letter):
        if not self.active:
            return
        bit_length = max(abs(new_u).bit_length(), abs(new_v).bit_length())
        if bit_length > LIFT_BIT_LIMIT:
            self.saturation = {
                "before_update_index": self.updates_recorded + 1,
                "letter": letter,
                "candidate_max_bit_length": bit_length,
                "last_exact_U": self.u,
                "last_exact_V": self.v,
            }
            self.active = False
            return
        self.u, self.v = new_u, new_v
        self.updates_recorded += 1
        self.maximum_bit_length = max(self.maximum_bit_length, bit_length)
        self._record_state(self.updates_recorded, letter)

    def record(self):
        return {
            "label": self.label,
            "positive": self.positive,
            "bit_limit": LIFT_BIT_LIMIT,
            "active_at_stop": self.active,
            "updates_recorded": self.updates_recorded,
            "maximum_bit_length_recorded": self.maximum_bit_length,
            "last_exact_U": self.u,
            "last_exact_V": self.v,
            "saturation": self.saturation,
            "first_norm_gt_2N": self.first_norm_gt_2n,
            "state_prefix": self.state_prefix,
        }


def verify_output(n, output):
    if output is None:
        return
    if output["type"] == "factor":
        divisor = output["value"]
        if not (1 < divisor < n and n % divisor == 0):
            raise ArithmeticError("invalid factor output")
    else:
        root = output["value"]
        if root * root % n != n - 1:
            raise ArithmeticError("invalid square root of -1")


def frozen_f326_path(n, method, cap):
    pairing = GaussPairing(n, n - 1)
    assert pairing.L == 0 and pairing.d == (n + 1) // 2
    current = 0
    trace = []
    output = None
    for step in range(1, cap + 1):
        coordinate = pairing.select(current)
        image, branch = pairing.F(coordinate)
        row = {
            "fine_call": step,
            "coordinate": coordinate,
            "F_image": image,
            "F_branch": branch,
        }
        if image == coordinate:
            decoded = pairing.decode(coordinate, branch)
            output = {
                "type": "factor" if "factor" in decoded else "root",
                "value": decoded.get("factor", decoded.get("root")),
                "coordinate": coordinate,
                "branch": branch,
            }
            row["terminal"] = True
            trace.append(row)
            break
        image_rank = pairing.rank(image)
        current = auxiliary(image_rank, pairing.L, pairing.d, method)
        row.update({"terminal": False, "next_coordinate": pairing.select(current)})
        trace.append(row)
    return {
        "status": "completed" if output else "censored",
        "fine_F_calls": len(trace),
        "trace": trace,
        "output": output,
    }


def cheap_fine_path(n, method, cap, retain_trace=False):
    assert n > 1 and n % 4 == 1
    assert method in ("reflection", "adjacent")
    h = (n - 1) // 2
    d = (n + 1) // 2
    current = 0
    counters = Counter()
    trace = []
    output = None
    reflection_word = WordStats()
    adjacent_matrix_word = WordStats()
    adjacent_even_word = WordStats()
    lift = None
    started = time.perf_counter()

    for step in range(1, cap + 1):
        row = {"fine_call": step, "coordinate": current}
        if current == 0:
            image, branch = 1, "swap_0_1"
        elif current == 1:
            image, branch = 0, "swap_0_1"
            counters["special_one_guards"] += 1
        else:
            counters["gcd_calls"] += 1
            divisor = math.gcd(current, n)
            if divisor > 1:
                image, branch = current, "fixed_nonunit"
                output = {
                    "type": "factor",
                    "value": divisor,
                    "coordinate": current,
                    "branch": branch,
                }
            else:
                counters["modular_inversions"] += 1
                inverse = centered_rep(pow(current, -1, n), n)
                image = abs(inverse)
                branch = "first_inverse" if inverse > 0 else "scaled_inverse"
                if image == current:
                    if inverse > 0:
                        counters["gcd_calls"] += 1
                        divisor = math.gcd(current - 1, n)
                        output = {
                            "type": "factor",
                            "value": divisor,
                            "coordinate": current,
                            "branch": branch,
                        }
                    else:
                        output = {
                            "type": "root",
                            "value": inverse,
                            "coordinate": current,
                            "branch": branch,
                        }

        row.update({"F_image": image, "F_branch": branch})
        if output is not None:
            verify_output(n, output)
            row["terminal"] = True
            if retain_trace or len(trace) < 64:
                trace.append(row)
            break

        if method == "reflection":
            next_coordinate = 0 if image == 0 else d - image
            if current == 0:
                lift = LiftTracker(-2, 1, n, False, "reflection_z")
            elif current not in (0, 1):
                sigma = -1 if inverse > 0 else 1
                reflection_word.add("+" if sigma > 0 else "-")
                if lift.active:
                    assert lift.v % n != 0
                    assert lift.u * pow(lift.v, -1, n) % n == (2 * current - 1) % n
                    new_u, new_v = 4 * sigma * lift.v, lift.u + lift.v
                    lift.update(new_u, new_v, "+" if sigma > 0 else "-")
        else:
            next_coordinate = image + (1 if image % 2 else -1) if image else 0
            if current == 0:
                lift = LiftTracker(2, 1, n, True, "adjacent_fine_x")
            elif current not in (0, 1):
                sign = 1 if inverse > 0 else -1
                epsilon = 1 if image % 2 else -1
                matrix_letter = ("+" if epsilon > 0 else "-") + (
                    "+" if sign > 0 else "-"
                )
                adjacent_matrix_word.add(matrix_letter)
                if sign < 0 and adjacent_matrix_word.maximum_same_run[matrix_letter] > 2:
                    raise ArithmeticError("forbidden triple negative-inverse branch")
                even_u = current if current % 2 == 0 else n - current
                ordinary_inverse = pow(even_u, -1, n)
                even_letter = "+" if ordinary_inverse % 2 else "-"
                adjacent_even_word.add(even_letter)
                next_even = (
                    ordinary_inverse + 1
                    if ordinary_inverse % 2
                    else n + 1 - ordinary_inverse
                )
                assert even_to_coordinate(next_even, n) == next_coordinate
                if lift.active:
                    assert lift.u * pow(lift.v, -1, n) % n == current
                    new_u = epsilon * lift.u + sign * lift.v
                    new_v = lift.u
                    lift.update(new_u, new_v, matrix_letter)

        row.update({"terminal": False, "next_coordinate": next_coordinate})
        if retain_trace or len(trace) < 64:
            trace.append(row)
        current = next_coordinate

    return {
        "method": method,
        "cap_type": "fine_F_calls",
        "cap": cap,
        "status": "completed" if output else "censored",
        "fine_F_calls": step,
        "output": output,
        "operation_counts": dict(counters),
        "reflection_sigma_word": reflection_word.record(),
        "adjacent_matrix_word": adjacent_matrix_word.record(),
        "adjacent_even_word": adjacent_even_word.record(),
        "lift": lift.record() if lift else None,
        "trace_prefix": trace,
        "walltime_seconds": time.perf_counter() - started,
    }


def adjacent_block_path(n, block_cap, retain_trace=False):
    assert n > 1 and n % 4 == 1
    h = (n - 1) // 2
    d = (n + 1) // 2
    u, v = 2, d
    lift = LiftTracker(2, 1, n, True, "adjacent_positive_blocks")
    word = WordStats()
    counters = Counter()
    fine_calls = 1
    fine_trace = [
        {
            "fine_call": 1,
            "coordinate": 0,
            "F_image": 1,
            "F_branch": "swap_0_1",
            "terminal": False,
            "next_coordinate": 2,
        }
    ]
    block_trace = []
    output = None
    special_guard = None
    started = time.perf_counter()

    def append_fine(row):
        if retain_trace or len(fine_trace) < 64:
            fine_trace.append(row)

    for block_iteration in range(1, block_cap + 1):
        counters["block_iterations"] += 1
        assert 1 <= u < n and u % 2 == 0
        assert 1 <= v < n and v % 2 == 1 and u * v % n == 1
        coordinate = even_to_coordinate(u, n)
        if lift.active:
            assert lift.u * pow(lift.v, -1, n) % n == u
        block_row = {
            "block_iteration": block_iteration,
            "u": u,
            "v": v,
            "coordinate": coordinate,
            "fine_calls_before": fine_calls,
        }

        counters["root_tests"] += 1
        if u * u % n == n - 1:
            fine_calls += 1
            output = {
                "type": "root",
                "value": u,
                "coordinate": coordinate,
                "branch": "scaled_inverse",
                "terminal_position": "block_start",
            }
            verify_output(n, output)
            append_fine(
                {
                    "fine_call": fine_calls,
                    "coordinate": coordinate,
                    "terminal": True,
                    "F_branch": "scaled_inverse",
                }
            )
            block_row.update({"terminal": True, "output": output})
            block_trace.append(block_row)
            break

        counters["gcd_calls"] += 1
        divisor = math.gcd(u + 1, n)
        if 1 < divisor < n:
            intermediate_u = v + 1
            intermediate_coordinate = even_to_coordinate(intermediate_u, n)
            assert math.gcd(intermediate_coordinate, n) == divisor
            append_fine(
                {
                    "fine_call": fine_calls + 1,
                    "coordinate": coordinate,
                    "terminal": False,
                    "next_coordinate": intermediate_coordinate,
                }
            )
            append_fine(
                {
                    "fine_call": fine_calls + 2,
                    "coordinate": intermediate_coordinate,
                    "terminal": True,
                    "F_branch": "fixed_nonunit",
                }
            )
            fine_calls += 2
            if lift.active:
                lift.update(lift.u + lift.v, lift.u, "terminal_partial_P")
            output = {
                "type": "factor",
                "value": divisor,
                "coordinate": intermediate_coordinate,
                "branch": "fixed_nonunit",
                "terminal_position": "intermediate_plus",
            }
            verify_output(n, output)
            block_row.update(
                {
                    "terminal": True,
                    "terminal_partial_letter": "P",
                    "intermediate_u": intermediate_u,
                    "output": output,
                }
            )
            block_trace.append(block_row)
            break
        if divisor != 1:
            raise ArithmeticError("u+1 gcd reached N outside a special guard")

        counters["modular_inversions"] += 1
        z = pow(u + 1, -1, n)
        old_u, old_v = u, v
        if z % 2:
            letter = "P"
            new_u, new_v = old_v + 1, n + 1 - z
            append_fine(
                {
                    "fine_call": fine_calls + 1,
                    "coordinate": coordinate,
                    "terminal": False,
                    "next_coordinate": even_to_coordinate(new_u, n),
                }
            )
            fine_calls += 1
            if lift.active:
                lift.update(lift.u + lift.v, lift.u, letter)
        else:
            letter = "Q"
            intermediate_u = old_v + 1
            intermediate_coordinate = even_to_coordinate(intermediate_u, n)
            append_fine(
                {
                    "fine_call": fine_calls + 1,
                    "coordinate": coordinate,
                    "terminal": False,
                    "next_coordinate": intermediate_coordinate,
                }
            )
            if intermediate_u == n - 1:
                append_fine(
                    {
                        "fine_call": fine_calls + 2,
                        "coordinate": 1,
                        "terminal": False,
                        "F_branch": "swap_0_1",
                        "next_coordinate": 0,
                    }
                )
                fine_calls += 2
                special_guard = {
                    "type": "intermediate_N_minus_1_returns_zero",
                    "block_iteration": block_iteration,
                    "u": old_u,
                    "v": old_v,
                }
                block_row.update({"special_guard": special_guard, "terminal": False})
                block_trace.append(block_row)
                break
            intermediate_square = intermediate_coordinate * intermediate_coordinate % n
            if intermediate_square in (1, n - 1):
                fine_calls += 2
                if intermediate_square == n - 1:
                    output = {
                        "type": "root",
                        "value": intermediate_u,
                        "coordinate": intermediate_coordinate,
                        "branch": "scaled_inverse",
                        "terminal_position": "Q_intermediate",
                    }
                else:
                    counters["gcd_calls"] += 1
                    factor = math.gcd(intermediate_coordinate - 1, n)
                    output = {
                        "type": "factor",
                        "value": factor,
                        "coordinate": intermediate_coordinate,
                        "branch": "first_inverse",
                        "terminal_position": "Q_intermediate",
                    }
                verify_output(n, output)
                if lift.active:
                    lift.update(lift.u + lift.v, lift.u, "terminal_partial_P")
                append_fine(
                    {
                        "fine_call": fine_calls,
                        "coordinate": intermediate_coordinate,
                        "terminal": True,
                        "F_branch": output["branch"],
                    }
                )
                block_row.update(
                    {
                        "terminal": True,
                        "terminal_partial_letter": "P",
                        "intermediate_u": intermediate_u,
                        "output": output,
                    }
                )
                block_trace.append(block_row)
                break
            new_u, new_v = z, old_u + 1
            append_fine(
                {
                    "fine_call": fine_calls + 2,
                    "coordinate": intermediate_coordinate,
                    "terminal": False,
                    "next_coordinate": even_to_coordinate(new_u, n),
                }
            )
            fine_calls += 2
            if lift.active:
                lift.update(lift.v, lift.u + lift.v, letter)

        word.add(letter)
        counters["moving_blocks_completed"] += 1
        u, v = new_u, new_v
        assert u % 2 == 0 and v % 2 == 1 and u * v % n == 1
        block_row.update(
            {
                "terminal": False,
                "letter": letter,
                "z": z,
                "new_u": u,
                "new_v": v,
                "fine_calls_after": fine_calls,
            }
        )
        if retain_trace or len(block_trace) < 64:
            block_trace.append(block_row)

    status = "completed" if output else (
        "special_guard_return" if special_guard else "censored"
    )
    return {
        "method": "adjacent_block",
        "cap_type": "block_iterations",
        "block_cap": block_cap,
        "status": status,
        "block_iterations": counters["block_iterations"],
        "moving_blocks_completed": counters["moving_blocks_completed"],
        "equivalent_fine_F_calls": fine_calls,
        "output": output,
        "special_guard": special_guard,
        "operation_counts": dict(counters),
        "block_word": word.record(),
        "lift": lift.record(),
        "fine_trace_prefix": fine_trace,
        "block_trace_prefix": block_trace,
        "walltime_seconds": time.perf_counter() - started,
    }


def exact_controls():
    rows = []
    earlier_witnesses = []
    counts = Counter()
    for n in range(5, 102, 4):
        reflection_reference = frozen_f326_path(n, "rank_reflection", n)
        adjacent_reference = frozen_f326_path(n, "delete_adjacent", n)
        reflection = cheap_fine_path(n, "reflection", n, retain_trace=True)
        adjacent = cheap_fine_path(n, "adjacent", n, retain_trace=True)
        block = adjacent_block_path(n, n, retain_trace=True)
        assert reflection["status"] == reflection_reference["status"] == "completed"
        assert adjacent["status"] == adjacent_reference["status"] == "completed"
        assert block["status"] == "completed"
        for candidate, reference in (
            (reflection, reflection_reference),
            (adjacent, adjacent_reference),
        ):
            assert candidate["fine_F_calls"] == reference["fine_F_calls"]
            assert [
                (row["coordinate"], row.get("F_image"), row.get("F_branch"), row.get("next_coordinate"))
                for row in candidate["trace_prefix"]
            ] == [
                (row["coordinate"], row.get("F_image"), row.get("F_branch"), row.get("next_coordinate"))
                for row in reference["trace"]
            ]
            assert candidate["output"]["type"] == reference["output"]["type"]
            if candidate["output"]["type"] == "factor":
                assert candidate["output"]["value"] == reference["output"]["value"]
            else:
                assert candidate["output"]["value"] ** 2 % n == n - 1
                assert reference["output"]["value"] ** 2 % n == n - 1

        assert block["equivalent_fine_F_calls"] == adjacent_reference["fine_F_calls"]
        assert [row["coordinate"] for row in block["fine_trace_prefix"]] == [
            row["coordinate"] for row in adjacent_reference["trace"]
        ]
        assert block["output"]["type"] == adjacent_reference["output"]["type"]
        assert block["output"]["coordinate"] == adjacent_reference["output"]["coordinate"]
        if block["output"]["type"] == "factor":
            assert block["output"]["value"] == adjacent_reference["output"]["value"]
        else:
            assert block["output"]["value"] ** 2 % n == n - 1
            assert adjacent_reference["output"]["value"] ** 2 % n == n - 1

        paired_roots = root_pair_postprocessing(n, reflection, block)
        if paired_roots["status"] == "completed" and paired_roots["factor"]:
            assert n % paired_roots["factor"] == 0

        witness = block["lift"]["first_norm_gt_2N"]
        if witness:
            earlier_witnesses.append({"n": n, **witness})
        rows.append(
            {
                "n": n,
                "kind": "prime" if all(n % p for p in range(2, math.isqrt(n) + 1)) else "composite",
                "reflection": reflection,
                "adjacent_fine": adjacent,
                "adjacent_block": block,
                "root_pair_postprocessing": paired_roots,
            }
        )
        counts["moduli"] += 1
        counts["frozen_path_comparisons"] += 3

    n61 = next(row for row in rows if row["n"] == 61)["adjacent_block"]
    expected_letters = list("PPQQPQ")
    observed_letters = [
        row["letter"] for row in n61["block_trace_prefix"] if "letter" in row
    ]
    expected_lifts = [(2, 1), (3, 2), (5, 3), (3, 8), (8, 11), (19, 8), (8, 27)]
    observed_lifts = [
        (row["U"], row["V"]) for row in n61["lift"]["state_prefix"][:7]
    ]
    expected_u = [2, 32, 22, 8, 34, 10, 50]
    observed_u = [
        (u * pow(v, -1, 61)) % 61 for u, v in observed_lifts
    ]
    assert observed_letters == expected_letters
    assert observed_lifts == expected_lifts
    assert observed_u == expected_u
    assert n61["lift"]["first_norm_gt_2N"] == {
        "update_index": 4,
        "letter": "Q",
        "U": 8,
        "V": 11,
        "norm": 185,
        "two_N": 122,
    }
    assert n61["output"]["type"] == "root" and n61["output"]["value"] == 50
    return {
        "status": "passed",
        "scope": (
            "Every N=1 mod 4 through 101, including primes and composites. "
            "Both fine formulas and the compressed kernel are compared with "
            "the frozen F326 path through the exact terminal endpoint."
        ),
        "counts": dict(counts),
        "rows": rows,
        "N61_counterexample": {
            "letters": observed_letters,
            "positive_lifts": observed_lifts,
            "even_modular_u": observed_u,
            "first_norm_gt_2N": n61["lift"]["first_norm_gt_2N"],
            "terminal_norm": 8 * 8 + 27 * 27,
            "terminal_norm_over_N": 13,
            "terminal_root": 50,
        },
        "all_first_norm_gt_2N_witnesses": earlier_witnesses,
    }


def load_public_moduli():
    if sha256(F328_INPUT) != F328_INPUT_SHA256:
        raise RuntimeError("the retained F328 modulus input hash changed")
    payload = json.loads(F328_INPUT.read_text())
    rows = [row for row in payload["moduli"] if row["n"] % 4 == 1]
    assert len(rows) == 7
    for row in rows:
        assert row["p_offline"] * row["q_offline"] == row["n"]
        row["offline_root_label"] = (
            "impossible_Blum"
            if row["p_offline"] % 4 == row["q_offline"] % 4 == 3
            else "possible_both_primes_1_mod_4"
        )
    return rows


def root_pair_postprocessing(n, reflection, block):
    if not (
        reflection["status"] == block["status"] == "completed"
        and reflection["output"]["type"] == block["output"]["type"] == "root"
    ):
        return {
            "status": "not_applicable",
            "reason": "both traversals did not return square roots",
        }
    root_reflection = reflection["output"]["value"]
    root_adjacent = block["output"]["value"]
    started = time.perf_counter()
    divisor = math.gcd(root_adjacent - root_reflection, n)
    elapsed = time.perf_counter() - started
    if 1 < divisor < n:
        output_type = "proper_factor"
        factor = divisor
    elif divisor == n:
        output_type = "same_root_failure"
        factor = None
    else:
        output_type = "global_opposite_failure"
        factor = None
        assert (root_adjacent + root_reflection) % n == 0
    reflection_counts = reflection["operation_counts"]
    block_counts = block["operation_counts"]
    return {
        "status": "completed",
        "root_reflection": root_reflection,
        "root_adjacent": root_adjacent,
        "difference_gcd": divisor,
        "output_type": output_type,
        "factor": factor,
        "gcd_calls": 1,
        "walltime_seconds": elapsed,
        "charged_combined": {
            "reflection_fine_F_calls": reflection["fine_F_calls"],
            "adjacent_block_iterations": block["block_iterations"],
            "adjacent_equivalent_fine_F_calls": block["equivalent_fine_F_calls"],
            "gcd_calls": reflection_counts.get("gcd_calls", 0)
            + block_counts.get("gcd_calls", 0)
            + 1,
            "modular_inversions": reflection_counts.get("modular_inversions", 0)
            + block_counts.get("modular_inversions", 0),
            "walltime_seconds": reflection["walltime_seconds"]
            + block["walltime_seconds"]
            + elapsed,
        },
    }


def public_run(modulus_id, fine_cap, block_cap, methods):
    matches = [row for row in load_public_moduli() if row["modulus_id"] == modulus_id]
    if len(matches) != 1:
        raise ValueError("modulus id does not select one retained input")
    modulus = matches[0]
    n = modulus["n"]
    results = {}
    if "reflection" in methods:
        results["reflection"] = cheap_fine_path(n, "reflection", fine_cap)
    if "adjacent_block" in methods:
        results["adjacent_block"] = adjacent_block_path(n, block_cap)
    pair = (
        root_pair_postprocessing(n, results["reflection"], results["adjacent_block"])
        if set(results) == set(METHODS)
        else {"status": "not_evaluated", "reason": "both methods not run in this job"}
    )
    return {
        "status": "passed",
        "experiment": "F332_minus_one_paths",
        "route": "route:F31",
        "mode": "public",
        "public_input": {"n": n, "a": n - 1},
        "modulus_label": modulus,
        "methods_requested": methods,
        "fine_F_call_cap": fine_cap,
        "adjacent_block_iteration_cap": block_cap,
        "cap_scope": (
            "The equal numeric caps measure different coverage. Reflection is "
            "capped in fine F calls. The compressed adjacent kernel is capped in "
            "P/Q block iterations and records its equivalent fine F calls."
        ),
        "results": results,
        "root_pair_postprocessing": pair,
        "solver_isolation": (
            "Each solver receives only public N=-a mod N and its cap. Offline "
            "factor labels classify root possibility after the run and never enter "
            "a transition or stopping test."
        ),
    }


def aggregate_jobs(paths):
    jobs = []
    hashes = {}
    for path_text in paths:
        path = Path(path_text)
        payload = json.loads(path.read_text())
        assert payload["status"] == "passed" and payload["mode"] == "public"
        jobs.append(payload)
        hashes[path.name] = sha256(path)
    by_modulus = {}
    for row in load_public_moduli():
        relevant = [job for job in jobs if job["public_input"]["n"] == row["n"]]
        if not relevant:
            continue
        completed = {}
        for method in METHODS:
            candidates = [
                job["results"][method]
                for job in relevant
                if method in job["results"]
                and job["results"][method]["status"] == "completed"
            ]
            if candidates:
                completed[method] = min(
                    candidates,
                    key=lambda result: result.get(
                        "fine_F_calls", result.get("equivalent_fine_F_calls")
                    ),
                )
        combined_pair = (
            root_pair_postprocessing(
                row["n"], completed["reflection"], completed["adjacent_block"]
            )
            if set(completed) == set(METHODS)
            else {
                "status": "not_applicable",
                "reason": "both completed method outputs are unavailable",
            }
        )
        by_modulus[row["modulus_id"]] = {
            "n": row["n"],
            "offline_root_label": row["offline_root_label"],
            "jobs": relevant,
            "combined_root_postprocessing": combined_pair,
        }
    return {
        "status": "passed",
        "experiment": "F332_minus_one_paths",
        "route": "route:F31",
        "mode": "aggregate",
        "moduli_present": len(by_modulus),
        "by_modulus": by_modulus,
        "job_sha256": hashes,
        "scope": (
            "Pure per-method outputs remain unchanged. Root-pair gcd postprocessing "
            "is recorded only in jobs that contain two verified roots."
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("exact", "public", "aggregate"), required=True)
    parser.add_argument("--modulus-id")
    parser.add_argument("--fine-cap", type=int, default=INITIAL_CAP)
    parser.add_argument("--block-cap", type=int, default=INITIAL_CAP)
    parser.add_argument("--method", action="append", choices=METHODS)
    parser.add_argument("--job", action="append", default=[])
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    parser.add_argument("--log", required=True)
    arguments = parser.parse_args()
    started = time.perf_counter()
    source_hash = sha256(Path(__file__))
    input_hashes = {
        "F326_source": sha256(F326_SOURCE),
        "F328_moduli": sha256(F328_INPUT),
        "F330_PROOF": sha256(F330_PROOF),
        "F330_RATIONAL_PATHS": sha256(F330_RATIONAL),
    }
    if input_hashes["F326_source"] != F326_SOURCE_SHA256:
        raise RuntimeError("frozen F326 source hash changed")
    if input_hashes["F328_moduli"] != F328_INPUT_SHA256:
        raise RuntimeError("frozen F328 modulus hash changed")

    log_path = Path(arguments.log)
    log_path.write_text("")

    def log(event, **values):
        with log_path.open("a") as stream:
            stream.write(json.dumps({"event": event, **values}, sort_keys=True) + "\n")

    def timeout_handler(_signal_number, _frame):
        raise TimeoutError("internal 28-second alarm fired")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    running = {
        "status": "running",
        "experiment": "F332_minus_one_paths",
        "mode": arguments.mode,
        "source_sha256": source_hash,
        "input_hashes": input_hashes,
    }
    write_json(arguments.status, running)
    log("start", **running)
    try:
        if arguments.mode == "exact":
            payload = {
                **running,
                "status": "passed",
                "exact_controls": exact_controls(),
            }
        elif arguments.mode == "public":
            if not arguments.modulus_id:
                parser.error("public mode requires --modulus-id")
            methods = tuple(arguments.method or METHODS)
            payload = {
                **running,
                **public_run(
                    arguments.modulus_id,
                    arguments.fine_cap,
                    arguments.block_cap,
                    methods,
                ),
            }
        else:
            if not arguments.job:
                parser.error("aggregate mode requires job files")
            payload = {**running, **aggregate_jobs(arguments.job)}
        payload["internal_timeout_seconds"] = INTERNAL_TIMEOUT_SECONDS
        payload["hard_timeout_seconds"] = HARD_TIMEOUT_SECONDS
        payload["memory_limit_bytes"] = MEMORY_LIMIT_BYTES
        payload["lift_bit_limit"] = LIFT_BIT_LIMIT
        payload["process_walltime_seconds"] = time.perf_counter() - started
        payload["peak_rss_bytes"] = peak_rss_bytes()
        if payload["peak_rss_bytes"] > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 512 MiB")
        write_json(arguments.output, payload)
        status = {
            key: payload[key]
            for key in (
                "status",
                "experiment",
                "mode",
                "source_sha256",
                "input_hashes",
                "internal_timeout_seconds",
                "hard_timeout_seconds",
                "memory_limit_bytes",
                "lift_bit_limit",
                "process_walltime_seconds",
                "peak_rss_bytes",
            )
        }
        status["output"] = arguments.output
        write_json(arguments.status, status)
        log("passed", **status)
    except BaseException as exception:
        failure = {
            **running,
            "status": "failed",
            "exception_type": type(exception).__name__,
            "exception": str(exception),
            "traceback": traceback.format_exc(),
            "process_walltime_seconds": time.perf_counter() - started,
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, failure)
        write_json(arguments.status, failure)
        log("failed", **failure)
        raise
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    main()
