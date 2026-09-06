import json
import math
import os


def local_record(N, p, ell):
    if N % ell == 0:
        return {"ell": int(ell), "h": 0, "i": None, "factor": True}
    h = Mod(N, ell).multiplicative_order()
    target = Mod(p, ell)
    exponent = None if target^h != 1 else discrete_log(target, Mod(N, ell), ord=h)
    return {
        "ell": int(ell),
        "h": int(h),
        "i": None if exponent is None else int(exponent),
        "factor": False,
    }


def compatible(a_i, a_h, b_i, b_h):
    return (a_i - b_i) % math.gcd(a_h, b_h) == 0


def best_compatible(records, cap):
    accepted = [r for r in records if r["i"] is not None]
    if len(accepted) > 22:
        raise RuntimeError("accepted-prime exhaustive-search cap exceeded")
    best_product = 1
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
            if modulus > cap:
                ok = False
                break
            product *= record["ell"]
            chosen.append(record)
        if ok and product > best_product:
            best_product = product
    return best_product


with open("D06_OUTPUT.json") as source:
    d06 = json.load(source)
targets = [row for row in d06["failures"] if row["accepted_count"] == 0]

factor_cache = {}
rows = []
for row in targets:
    p = row["p"]
    q = row["q"]
    N = row["N"]
    n = row["n"]
    m = n // 2
    cap = n^4
    threshold = row["threshold"]
    record_cache = {}
    successes = 0
    gcd_successes = 0
    for R in range(1, 1 << m, 2):
        primes = set()
        for j in range(2, m + 1):
            A = R % (1 << j)
            cache_key = (m, A)
            if cache_key not in factor_cache:
                factor_cache[cache_key] = [int(ell) for ell, _ in factor(A)]
            primes.update(factor_cache[cache_key])
        factor_hit = any(N % ell == 0 for ell in primes)
        if factor_hit:
            successes += 1
            gcd_successes += 1
            continue
        for ell in primes:
            if ell not in record_cache:
                record_cache[ell] = local_record(N, p, ell)
        records = [record_cache[ell] for ell in sorted(primes)]
        successes += best_compatible(records, cap) >= threshold
    denominator = 1 << (m - 1)
    rows.append({
        "p": p,
        "q": q,
        "N": N,
        "n": n,
        "m": m,
        "successes": successes,
        "gcd_successes": gcd_successes,
        "denominator": denominator,
        "success_rate": successes / denominator,
    })

result = {
    "summary": {
        "row_count": len(rows),
        "minimum_success_rate": min(row["success_rate"] for row in rows),
        "maximum_success_rate": max(row["success_rate"] for row in rows),
        "mean_success_rate": sum(row["success_rate"] for row in rows) / len(rows),
    },
    "rows": sorted(rows, key=lambda row: row["success_rate"]),
}
with open(os.environ.get("F226_OUTPUT_NAME", "D07_OUTPUT.json"), "w") as output:
    json.dump(result, output, default=int, indent=2, sort_keys=True)
print(json.dumps(result, default=int, indent=2, sort_keys=True))

