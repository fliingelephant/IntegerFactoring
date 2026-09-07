#!/usr/bin/env python3
"""Exact small check of F325's globally induced ordered-subset matching."""

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


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from linear_patch_jumps import (
    Pairing,
    ReflectionMatching,
    is_d_state,
    make_node,
    modified_r,
    split_node,
)


INTERNAL_TIMEOUT_SECONDS = 28
HARD_TIMEOUT_SECONDS = 30
MEMORY_LIMIT_BYTES = 512 * 1024 * 1024


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


def traced_partner(pairing, matching, retained, node):
    """Follow s,(r*,s)* through deleted D vertices to the next retained node."""
    current, _ = matching.apply(node)
    deleted_seen = set()
    deleted_count = 0
    while current not in retained:
        assert is_d_state(pairing, current)
        assert current not in deleted_seen
        deleted_seen.add(current)
        deleted_count += 1
        current, branch = modified_r(pairing, current)
        assert branch == "D:negate_modified"
        assert is_d_state(pairing, current)
        current, _ = matching.apply(current)
    return current, deleted_count


def explicit_partner(pairing, matching, positives, node):
    layer, x = split_node(pairing, node)
    external = make_node(pairing, 0, -pairing.h)
    if layer == 0 and x == -pairing.h:
        return make_node(pairing, 1, -positives[-1] if positives else 0)
    if layer != 1:
        return matching.apply(node)[0]
    if x == 0:
        return make_node(pairing, 1, positives[0]) if positives else external
    if x > 0:
        index = positives.index(x)
        return (
            make_node(pairing, 1, 0)
            if index == 0
            else make_node(pairing, 1, -positives[index - 1])
        )
    index = positives.index(-x)
    return (
        make_node(pairing, 1, positives[index + 1])
        if index + 1 < len(positives)
        else external
    )


def run(limit):
    started = time.perf_counter()
    counts = Counter()
    chain_histogram = Counter()
    max_deleted_chain = None
    examples = []
    for n in range(3, limit + 1, 2):
        units = [value for value in range(1, n) if math.gcd(value, n) == 1]
        for a in units:
            for b in units:
                pairing = Pairing(n, a, b)
                matching = ReflectionMatching(pairing, (1, 1, 1))
                retained = {
                    node for node in range(3 * n) if not is_d_state(pairing, node)
                }
                positives = [
                    x
                    for x in range(1, pairing.h + 1)
                    if make_node(pairing, 1, x) in retained
                ]
                assert all(
                    make_node(pairing, 1, -x) in retained for x in positives
                )
                assert len(retained) == 2 * n + 1 + 2 * len(positives)

                direct = {}
                for node in retained:
                    original_node, _ = pairing.r(node)
                    modified_node, _ = modified_r(pairing, node)
                    assert original_node == modified_node
                    assert original_node in retained
                    counts["restricted_r_invariant_states"] += 1

                    traced, deleted_count = traced_partner(
                        pairing, matching, retained, node
                    )
                    explicit = explicit_partner(pairing, matching, positives, node)
                    assert traced == explicit
                    direct[node] = explicit
                    chain_histogram[deleted_count] += 1
                    if max_deleted_chain is None or deleted_count > max_deleted_chain[0]:
                        max_deleted_chain = (deleted_count, n, a, b, node, explicit)
                    counts["induced_partner_checks"] += 1

                assert all(direct[direct[node]] == node for node in retained)
                fixed = [node for node in retained if direct[node] == node]
                assert fixed == [make_node(pairing, 2, -pairing.h)]
                counts["pairings"] += 1
                counts["retained_states"] += len(retained)
                counts["deleted_d_states"] += 3 * n - len(retained)
                counts["sole_fixed_point_checks"] += 1
                if len(examples) < 12 and (not positives or a == n - 1):
                    examples.append(
                        {
                            "n": n,
                            "a": a,
                            "b": b,
                            "positive_E": positives,
                            "retained_states": len(retained),
                            "deleted_D_states": 3 * n - len(retained),
                        }
                    )

    return {
        "status": "passed",
        "experiment": "F325_linear_patch_jumps_induced_matching_check",
        "scope": (
            "All odd N through the limit and every ordered pair of units a,b. "
            "The explicit ordered-subset matching is compared with direct "
            "s,(r*,s)* traversal through every deleted D chain."
        ),
        "limit": limit,
        "counts": dict(counts),
        "deleted_chain_length_histogram": {
            str(key): value for key, value in sorted(chain_histogram.items())
        },
        "max_deleted_chain": {
            "length": max_deleted_chain[0],
            "n": max_deleted_chain[1],
            "a": max_deleted_chain[2],
            "b": max_deleted_chain[3],
            "from_node": max_deleted_chain[4],
            "to_node": max_deleted_chain[5],
        },
        "selected_examples": examples,
        "source_sha256": sha256(Path(__file__)),
        "dependency_sha256": sha256(HERE / "linear_patch_jumps.py"),
        "internal_timeout_seconds": INTERNAL_TIMEOUT_SECONDS,
        "hard_timeout_seconds": HARD_TIMEOUT_SECONDS,
        "memory_limit_bytes": MEMORY_LIMIT_BYTES,
        "walltime_seconds": time.perf_counter() - started,
        "peak_rss_bytes": peak_rss_bytes(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=31)
    parser.add_argument("--output", required=True)
    parser.add_argument("--status", required=True)
    arguments = parser.parse_args()

    def timeout_handler(_signal_number, _frame):
        raise TimeoutError("internal 28-second alarm fired")

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(INTERNAL_TIMEOUT_SECONDS)
    write_json(
        arguments.status,
        {
            "status": "running",
            "limit": arguments.limit,
            "source_sha256": sha256(Path(__file__)),
            "dependency_sha256": sha256(HERE / "linear_patch_jumps.py"),
        },
    )
    try:
        payload = run(arguments.limit)
        if payload["peak_rss_bytes"] > MEMORY_LIMIT_BYTES:
            raise MemoryError("peak RSS exceeded 512 MiB")
        write_json(arguments.output, payload)
        write_json(
            arguments.status,
            {
                key: payload[key]
                for key in (
                    "status",
                    "experiment",
                    "limit",
                    "source_sha256",
                    "dependency_sha256",
                    "internal_timeout_seconds",
                    "hard_timeout_seconds",
                    "memory_limit_bytes",
                    "walltime_seconds",
                    "peak_rss_bytes",
                )
            },
        )
        print(json.dumps(payload, sort_keys=True))
    except BaseException as exception:
        failure = {
            "status": "failed",
            "experiment": "F325_linear_patch_jumps_induced_matching_check",
            "limit": arguments.limit,
            "source_sha256": sha256(Path(__file__)),
            "dependency_sha256": sha256(HERE / "linear_patch_jumps.py"),
            "exception_type": type(exception).__name__,
            "exception": str(exception),
            "traceback": traceback.format_exc(),
            "peak_rss_bytes": peak_rss_bytes(),
        }
        write_json(arguments.output, failure)
        write_json(arguments.status, failure)
        print(json.dumps(failure, sort_keys=True))
        raise
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    main()
