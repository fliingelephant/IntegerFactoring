#!/usr/bin/env sage

"""F140-D01: finite discovery for canonical recentering paths.

This is a bounded search only.  It does not prove an unbounded statement.
"""

import hashlib
import json
import operator
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "OUTPUT.json"
CORPUS_PRIME_MAX = int(97)
C_VALUES = tuple(map(int, (5, 7, 11)))
MAX_DEPTH = int(10)
MAX_EXPANSIONS_PER_CASE = int(250000)


def proper_gcd(x, N):
    d = gcd(ZZ(x), ZZ(N))
    return 1 < d < N


def parity_vector(value, row_index):
    vector = 0
    for prime, exponent in factor(ZZ(value)):
        if exponent % 2:
            prime = int(prime)
            if prime not in row_index:
                row_index[prime] = len(row_index)
            vector = operator.xor(vector, 1 << row_index[prime])
    return vector


def extend_basis(vector, basis):
    reduced = vector
    while reduced:
        pivot = reduced.bit_length() - 1
        if pivot not in basis:
            updated = dict(basis)
            updated[pivot] = reduced
            return updated
        reduced = operator.xor(reduced, basis[pivot])
    return None


def relation_nodes(N, C):
    nodes_by_q = {}
    endpoints_by_q = {}
    anchors = tuple(int(a) for a in prime_range(2, C + 1))
    for q in range(2, (N - 1) // C + 1):
        if gcd(q, N) != 1:
            continue
        w = int(inverse_mod(q, N))
        k = (q * w - 1) // N
        nodes = []
        endpoints = []
        for anchor in anchors:
            if gcd(anchor, N * q) != 1:
                continue
            digit = int((-w * inverse_mod(N, anchor)) % anchor)
            H = w + digit * N
            if H % anchor:
                raise AssertionError("anchor divisibility failed")
            left = anchor * q
            right = H // anchor
            if not (1 <= left < N and 1 <= right < N):
                raise AssertionError("noncanonical endpoint")
            endpoints.extend(((anchor, digit, "left", left),
                              (anchor, digit, "right", right)))
            if digit == 0:
                continue
            if proper_gcd(left - right, N) or proper_gcd(left + right, N):
                continue
            carry = k + digit * q
            value = 1 + carry * N
            if left * right != value:
                raise AssertionError("exact value mismatch")
            nodes.append({
                "q": q,
                "w": w,
                "k": k,
                "anchor": anchor,
                "digit": digit,
                "H": H,
                "left": left,
                "right": right,
                "carry": carry,
                "value": value,
            })
        if nodes:
            nodes_by_q[q] = nodes
            endpoints_by_q[q] = endpoints

    # A conditional release is any prime factor of the retained right endpoint.
    # A public release is an exact gcd with a different endpoint in the same
    # complete anchor star.  The latter needs no integer factorization oracle.
    for q, nodes in nodes_by_q.items():
        endpoints = endpoints_by_q[q]
        for node in nodes:
            conditional = set()
            for prime, _ in factor(ZZ(node["right"])):
                prime = int(prime)
                if 1 < prime < N // C and gcd(prime, N) == 1 and prime != q:
                    conditional.add(prime)
            public = set()
            for anchor, digit, side, endpoint in endpoints:
                if (anchor == node["anchor"] and digit == node["digit"]
                        and side == "right"):
                    continue
                released = int(gcd(node["right"], endpoint))
                if (1 < released < N // C and gcd(released, N) == 1
                        and released != q and released != node["right"]):
                    public.add(released)
            node["conditional_releases"] = sorted(conditional)
            node["public_releases"] = sorted(public)
    return nodes_by_q


def search_case(N, C, release_key):
    nodes_by_q = relation_nodes(N, C)
    row_index = {}
    for nodes in nodes_by_q.values():
        for node in nodes:
            node["parity"] = parity_vector(node["value"], row_index)

    best = None
    expansions = 0

    def score(path, quotients):
        small = sum(j < C for j in quotients)
        large = len(quotients) - small
        alternations = sum(
            (quotients[i] < C) != (quotients[i - 1] < C)
            for i in range(1, len(quotients))
        )
        all_small = int(bool(quotients) and small == len(quotients))
        alternating = int(len(quotients) >= 2 and alternations == len(quotients) - 1)
        return (len(path), alternating, alternations, all_small, small, large)

    def freeze(path, quotients, releases):
        return {
            "N": N,
            "factorization": [[int(p), int(e)] for p, e in factor(ZZ(N))],
            "C": C,
            "release_mode": release_key,
            "score": list(map(int, score(path, quotients))),
            "quotients": list(quotients),
            "releases": list(releases),
            "nodes": [
                {key: int(node[key]) for key in (
                    "q", "w", "k", "anchor", "digit", "H", "left",
                    "right", "carry", "value"
                )}
                for node in path
            ],
            "rank": len(path),
            "nullity": 0,
        }

    def visit(path, quotients, releases, seen_q, seen_carry, basis):
        nonlocal best, expansions
        if expansions >= MAX_EXPANSIONS_PER_CASE:
            return
        expansions += 1
        candidate = freeze(path, quotients, releases)
        if best is None or tuple(candidate["score"]) > tuple(best["score"]):
            best = candidate
        if len(path) >= MAX_DEPTH:
            return
        current = path[-1]
        for released in current[release_key]:
            if released in seen_q or released not in nodes_by_q:
                continue
            quotient = current["carry"] // released
            remainder = current["carry"] % released
            # Check the exact P124 canonical carry law.
            expected_w = int(inverse_mod(released, N))
            expected_k = (released * expected_w - 1) // N
            if remainder != expected_k:
                raise AssertionError("divisor carry law failed")
            for child in nodes_by_q[released]:
                if child["carry"] in seen_carry:
                    continue
                updated_basis = extend_basis(child["parity"], basis)
                if updated_basis is None:
                    continue
                visit(
                    path + [child],
                    quotients + [quotient],
                    releases + [released],
                    seen_q | {released},
                    seen_carry | {child["carry"]},
                    updated_basis,
                )

    for q in sorted(nodes_by_q):
        for node in nodes_by_q[q]:
            basis = extend_basis(node["parity"], {})
            if basis is not None:
                visit([node], [], [], {q}, {node["carry"]}, basis)
            if expansions >= MAX_EXPANSIONS_PER_CASE:
                break
        if expansions >= MAX_EXPANSIONS_PER_CASE:
            break
    if best is not None:
        best["expansions"] = expansions
        best["capped"] = expansions >= MAX_EXPANSIONS_PER_CASE
    return best


def main():
    corpus = []
    primes = [int(p) for p in prime_range(11, CORPUS_PRIME_MAX + 1)]
    for i, p in enumerate(primes):
        for q in primes[i + 1:]:
            if q >= 2 * p:
                break
            corpus.append((p * q, p, q))

    records = []
    best_by_mode = {}
    for N, p, q in corpus:
        for C in C_VALUES:
            if N <= C * C:
                continue
            for release_key in ("public_releases", "conditional_releases"):
                best = search_case(N, C, release_key)
                if best is None:
                    continue
                records.append({
                    "N": N,
                    "p": p,
                    "q": q,
                    "C": int(C),
                    "release_mode": release_key,
                    "score": best["score"],
                    "capped": best["capped"],
                })
                old = best_by_mode.get(release_key)
                key = (tuple(best["score"]), -N, -C)
                if old is None or key > old[0]:
                    best_by_mode[release_key] = (key, best)

    source_hash = hashlib.sha256((ROOT / "search_paths.sage").read_bytes()).hexdigest()
    output = {
        "experiment": "F140-D01",
        "scope": "finite discovery only",
        "source_sha256": source_hash,
        "parameters": {
            "corpus_prime_max": int(CORPUS_PRIME_MAX),
            "C_values": list(map(int, C_VALUES)),
            "max_depth": int(MAX_DEPTH),
            "max_expansions_per_case": int(MAX_EXPANSIONS_PER_CASE),
            "corpus_size": int(len(corpus)),
        },
        "best": {mode: pair[1] for mode, pair in best_by_mode.items()},
        "case_summaries": records,
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "experiment": output["experiment"],
        "source_sha256": source_hash,
        "corpus_size": len(corpus),
        "best_scores": {
            mode: data[1]["score"] for mode, data in best_by_mode.items()
        },
        "output": str(OUTPUT),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
