import json
import math
import os
import sys


def local_record(N, p, ell):
    h = Mod(N, ell).multiplicative_order()
    target = Mod(p, ell)
    exponent = None if target^h != 1 else discrete_log(target, Mod(N, ell), ord=h)
    return {
        "ell": int(ell),
        "h": int(h),
        "i": None if exponent is None else int(exponent),
    }


def compatible(a_i, a_h, b_i, b_h):
    return (a_i - b_i) % math.gcd(a_h, b_h) == 0


def best_compatible(records, cap):
    accepted = [r for r in records if r["i"] is not None]
    if len(accepted) > 22:
        raise RuntimeError("accepted-prime exhaustive-search cap exceeded")
    best_product = 1
    best_lcm = 1
    best_primes = []
    for mask in range(1 << len(accepted)):
        chosen = []
        modulus = 1
        product = 1
        ok = True
        for j, record in enumerate(accepted):
            if not ((mask >> j) & 1):
                continue
            if any(not compatible(record["i"], record["h"], prior["i"], prior["h"])
                   for prior in chosen):
                ok = False
                break
            modulus = math.lcm(modulus, record["h"])
            if cap is not None and modulus > cap:
                ok = False
                break
            product *= record["ell"]
            chosen.append(record)
        if ok and product > best_product:
            best_product = product
            best_lcm = modulus
            best_primes = [r["ell"] for r in chosen]
    return {
        "product": int(best_product),
        "exponent_lcm": int(best_lcm),
        "primes": best_primes,
    }


def summarize(records, cap):
    unique = {r["ell"]: r for r in records}
    records = [unique[ell] for ell in sorted(unique)]
    accepted = [r for r in records if r["i"] is not None]
    local_product = math.prod(r["ell"] for r in accepted)
    return {
        "prime_count": len(records),
        "accepted_count": len(accepted),
        "local_product": int(local_product),
        "capped": best_compatible(records, cap),
        "uncapped": best_compatible(records, None),
        "records": records,
    }


rows = []
for p in prime_range(2^9, 2^14):
    for ratio_num, ratio_den in [(105, 100), (125, 100), (150, 100), (190, 100)]:
        q = next_prime((ratio_num * int(p) + ratio_den - 1) // ratio_den - 1)
        if not (p < q < 2 * p):
            continue
        N = int(p * q)
        n = N.bit_length()
        cap = n^4
        levels = []
        pooled = []
        top = None
        for j in range((n + 1) // 2, n):
            A = N % (1 << j)
            factors = factor(A)
            records = [local_record(N, int(p), int(ell)) for ell, _ in factors if ell != 2]
            pooled.extend(records)
            level = {
                "j": j,
                "A": int(A),
                "factorization": [[int(ell), int(e)] for ell, e in factors],
                "summary": summarize(records, cap),
            }
            levels.append(level)
            if j == n - 1:
                top = level
        floor_root, exact_root = ZZ(N).nth_root(4, truncate_mode=True)
        threshold = int(floor_root if exact_root else floor_root + 1)
        pooled_summary = summarize(pooled, cap)
        rows.append({
            "p": int(p),
            "q": int(q),
            "N": N,
            "n": n,
            "threshold": threshold,
            "top": top,
            "pooled": pooled_summary,
            "levels": levels,
        })

summary = {
    "row_count": len(rows),
    "top_local_terminal": sum(r["top"]["summary"]["local_product"] >= r["threshold"] for r in rows),
    "top_capped_terminal": sum(r["top"]["summary"]["capped"]["product"] >= r["threshold"] for r in rows),
    "top_uncapped_terminal": sum(r["top"]["summary"]["uncapped"]["product"] >= r["threshold"] for r in rows),
    "pooled_local_terminal": sum(r["pooled"]["local_product"] >= r["threshold"] for r in rows),
    "pooled_capped_terminal": sum(r["pooled"]["capped"]["product"] >= r["threshold"] for r in rows),
    "pooled_uncapped_terminal": sum(r["pooled"]["uncapped"]["product"] >= r["threshold"] for r in rows),
    "rows_with_no_top_acceptance": sum(r["top"]["summary"]["accepted_count"] == 0 for r in rows),
    "rows_with_no_pooled_acceptance": sum(r["pooled"]["accepted_count"] == 0 for r in rows),
}

with open(os.environ.get("F226_OUTPUT_NAME", "D01_OUTPUT.json"), "w") as output:
    json.dump({"summary": summary, "rows": rows}, output, indent=2, sort_keys=True)

print(json.dumps(summary, indent=2, sort_keys=True))
