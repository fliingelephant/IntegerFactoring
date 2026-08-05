#!/usr/bin/env python3
"""Independent double-and-add audit of the retained F12 finite certificate."""

import argparse
import hashlib
import json
import math
from pathlib import Path


def add(p1, p2, a, prime):
    if p1 is None: return p2
    if p2 is None: return p1
    x1, y1 = p1; x2, y2 = p2
    if x1 == x2:
        if (y1 + y2) % prime == 0: return None
        lam = (3*x1*x1+a) * pow(2*y1, -1, prime) % prime
    else:
        lam = (y2-y1) * pow(x2-x1, -1, prime) % prime
    x3 = (lam*lam-x1-x2) % prime
    return x3, (lam*(x1-x3)-y1) % prime


def multiply(k, point, a, prime):
    result = None
    addend = point
    while k:
        if k & 1: result = add(result, addend, a, prime)
        addend = add(addend, addend, a, prime)
        k >>= 1
    return result


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--parameters", required=True)
    parser.add_argument("--certificate", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    params = json.loads(Path(args.parameters).read_text())
    cert = json.loads(Path(args.certificate).read_text())
    if cert["status"] != "pass": raise SystemExit("certificate did not pass")
    a = params["curve"]["A"]
    expected = {101: (112, (11, 101)), 103: (106, (5, 101))}
    checks = []
    for prime, (order, pair) in expected.items():
        point = (params["point"]["x"] % prime, params["point"]["y"] % prime)
        data = cert["local"][str(prime)]
        if data["point_order"] != order or tuple(data["first_collision"]) != pair:
            raise SystemExit("retained order/collision mismatch")
        if multiply(order, point, a, prime) is not None:
            raise SystemExit("claimed order does not annihilate point")
        for divisor in sorted(set(d for d in range(1, order) if order % d == 0)):
            if multiply(divisor, point, a, prime) is None:
                raise SystemExit("claimed order is not minimal")
        left, right = multiply(pair[0], point, a, prime), multiply(pair[1], point, a, prime)
        if left is None or right is None or left[0] != right[0] or (left[1] + right[1]) % prime:
            raise SystemExit("collision is not denominator-clean opposition")
        for i in range(1, pair[0] + 1):
            last_j = params["m"] if i < pair[0] else pair[1] - 1
            for j in range(i + 1, last_j + 1):
                pi, pj = multiply(i, point, a, prime), multiply(j, point, a, prime)
                if pi[0] == pj[0]: raise SystemExit("earlier lexicographic collision found")
        checks.append({"prime": prime, "order": order, "first_collision": pair})
    manifest = {}
    for line in Path(args.manifest).read_text().splitlines():
        value, name = line.split(maxsplit=1)
        manifest[name.strip()] = value
    relative = "outputs/finite_certificate.json"
    if manifest.get(relative) != sha256(args.certificate): raise SystemExit("certificate hash mismatch")
    Path(args.output).write_text(json.dumps({"status":"pass","independent_checks":checks}, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__": main()
