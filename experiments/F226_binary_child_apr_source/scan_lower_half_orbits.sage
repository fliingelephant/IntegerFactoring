import json
import math
import os


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
            if modulus > cap:
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


row_count = 0
terminal_count = 0
no_acceptance_count = 0
failures = []
by_n = {}

for p in prime_range(2^9, 2^14):
    for ratio_num, ratio_den in [(105, 100), (125, 100), (150, 100), (190, 100)]:
        q = next_prime((ratio_num * int(p) + ratio_den - 1) // ratio_den - 1)
        if not (p < q < 2 * p):
            continue
        N = int(p * q)
        n = N.bit_length()
        cap = n^4
        children = {}
        records_by_prime = {}
        for j in range(2, n // 2 + 1):
            A = N % (1 << j)
            if A in children:
                continue
            factors = factor(A)
            child_records = []
            for ell, _ in factors:
                if ell == 2:
                    continue
                record = local_record(N, int(p), int(ell))
                records_by_prime[record["ell"]] = record
                child_records.append(record)
            children[A] = {
                "A": int(A),
                "first_j": j,
                "factorization": [[int(ell), int(e)] for ell, e in factors],
                "records": child_records,
            }
        records = [records_by_prime[ell] for ell in sorted(records_by_prime)]
        accepted_count = sum(r["i"] is not None for r in records)
        best = best_compatible(records, cap)
        floor_root, exact_root = ZZ(N).nth_root(4, truncate_mode=True)
        threshold = int(floor_root if exact_root else floor_root + 1)
        terminal = best["product"] >= threshold

        row_count += 1
        terminal_count += terminal
        no_acceptance_count += accepted_count == 0
        bucket = by_n.setdefault(str(n), {"rows": 0, "terminal": 0, "no_acceptance": 0})
        bucket["rows"] += 1
        bucket["terminal"] += terminal
        bucket["no_acceptance"] += accepted_count == 0
        if not terminal:
            failures.append({
                "p": int(p),
                "q": int(q),
                "N": N,
                "n": n,
                "threshold": threshold,
                "accepted_count": accepted_count,
                "best": best,
                "children": [children[A] for A in sorted(children)],
            })

result = {
    "summary": {
        "row_count": row_count,
        "terminal_count": terminal_count,
        "failure_count": len(failures),
        "no_acceptance_count": no_acceptance_count,
        "by_n": by_n,
    },
    "failures": failures,
}
with open(os.environ.get("F226_OUTPUT_NAME", "D05_OUTPUT.json"), "w") as output:
    json.dump(result, output, default=int, indent=2, sort_keys=True)
print(json.dumps(result["summary"], default=int, indent=2, sort_keys=True))
