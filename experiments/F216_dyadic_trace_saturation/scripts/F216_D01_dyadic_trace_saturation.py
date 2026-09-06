#!/usr/bin/env python3

import hashlib
import json
import random
import time


def trace_image(n, t):
    modulus = 1 << t
    return {
        (u + n * pow(u, -1, modulus)) % modulus
        for u in range(1, modulus, 2)
    }


def sqrt_one_mod_eight(x, t):
    a = 1
    for k in range(3, t):
        modulus = 1 << (k + 1)
        if (a * a - x) % modulus:
            a += 1 << (k - 1)
    assert (a * a - x) % (1 << t) == 0
    return a


def predicted_representative(d, t):
    modulus = 1 << t
    if d == 3:
        return set(range(4, modulus, 8))
    if d == 7:
        return set(range(0, modulus, 8))
    if d == 5:
        return {
            s
            for s in range(modulus)
            if s % 32 in (6, 26)
        }
    return None


def predicted_one_count(t):
    if t % 2:
        return ((1 << (t - 4)) + 10) // 3
    return ((1 << (t - 4)) + 8) // 3


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2, 3, 5, 7, 11):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def next_prime(n):
    n |= 1
    while not is_prime(n):
        n += 2
    return n


def main():
    started = time.time()
    failures = []
    rows = []

    representative_images = {}
    for t in range(5, 19):
        for d in (1, 3, 5, 7):
            image = trace_image(d, t)
            representative_images[d, t] = image
            if d == 1:
                expected = predicted_one_count(t)
                ok = len(image) == expected
                detail = {"expected_count": expected}
            else:
                expected_image = predicted_representative(d, t)
                ok = image == expected_image
                detail = {"expected_count": len(expected_image)}
            if t >= 8:
                ok = ok and len(image) * 64 >= (1 << t)
            row = {
                "kind": "representative",
                "split": "train" if t <= 14 else "holdout",
                "d": d,
                "t": t,
                "count": len(image),
                "density": len(image) / (1 << t),
                "ok": ok,
                **detail,
            }
            rows.append(row)
            if not ok:
                failures.append(row)

    rng = random.Random(216_20260813)
    for index in range(32):
        n = rng.getrandbits(40) | 1 | (1 << 39)
        d = n % 8
        for t in (8, 12, 16):
            modulus = 1 << t
            x = n * pow(d, -1, modulus) % modulus
            a = sqrt_one_mod_eight(x, t)
            image = trace_image(n, t)
            normalized = {s * pow(a, -1, modulus) % modulus for s in image}
            ok = normalized == representative_images[d, t]
            ok = ok and len(image) * 64 >= modulus
            row = {
                "kind": "square_class_holdout",
                "index": index,
                "n": n,
                "d": d,
                "t": t,
                "a": a,
                "count": len(image),
                "normalized_sha256": hashlib.sha256(
                    ",".join(map(str, sorted(normalized))).encode()
                ).hexdigest(),
                "ok": ok,
            }
            rows.append(row)
            if not ok:
                failures.append(row)

    semiprimes = []
    seed = 1 << 15
    for index in range(16):
        p = next_prime(seed + 733 * index)
        q = next_prime(p + 1009 + 97 * index)
        assert p < q < 2 * p
        n = p * q
        t = 16
        image = trace_image(n, t)
        trace = (p + q) % (1 << t)
        ok = trace in image
        row = {
            "kind": "factor_trace_holdout",
            "index": index,
            "n": n,
            "n_mod_8": n % 8,
            "t": t,
            "trace_label": trace,
            "count": len(image),
            "ok": ok,
        }
        semiprimes.append({"n": n, "p": p, "q": q})
        rows.append(row)
        if not ok:
            failures.append(row)

    output = {
        "experiment": "F216-D01 dyadic trace saturation",
        "all_passed": not failures,
        "failure_count": len(failures),
        "row_count": len(rows),
        "representative_train_rows": 40,
        "representative_holdout_rows": 16,
        "square_class_holdout_rows": 96,
        "factor_trace_holdout_rows": 16,
        "minimum_density_t_ge_8": min(
            row["count"] / (1 << row["t"])
            for row in rows
            if row["t"] >= 8
        ),
        "elapsed_seconds": time.time() - started,
        "failures": failures,
        "semiprime_labels": semiprimes,
        "rows": rows,
    }
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
