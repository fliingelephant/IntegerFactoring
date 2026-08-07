import json
import time
from pathlib import Path

from F65_D01_scan import analyze_variant, collect_offset_relations, next_prime


RUN = "F65-D02"
TARGET_FACTOR_BITS = 30
RATIO = (4, 3)
OUTPUT = Path(__file__).resolve().parent.parent / "output" / f"{RUN}.json"


def main():
    started = time.monotonic()
    p = next_prime(1 << TARGET_FACTOR_BITS)
    numerator, denominator = RATIO
    lower_bound = max(p + 2, (numerator * p + denominator - 1) // denominator)
    q = next_prime(lower_bound)
    modulus = p * q
    raw, direct_events = collect_offset_relations(modulus)
    print(
        f"input N={modulus} bits={modulus.bit_length()} raw={len(raw)} "
        f"direct={len(direct_events)}",
        flush=True,
    )
    variant = analyze_variant(modulus, raw, False)
    print(
        f"blocks={variant['block_count']} "
        f"legal_hits={variant['legal_pair_screens']['screen_hit_count']} "
        f"signed_hits={variant['signed_pair_screens']['screen_hit_count']}",
        flush=True,
    )
    output = {
        "N": modulus,
        "direct_events": direct_events,
        "disposition": (
            "One finite larger-input stress test. A hit cannot prove an all-input "
            "law, and a miss kills only this exact transcript and menu."
        ),
        "elapsed_seconds": time.monotonic() - started,
        "input_bits": modulus.bit_length(),
        "p": p,
        "q": q,
        "ratio": list(RATIO),
        "raw_relation_count": len(raw),
        "run": RUN,
        "target_factor_bits": TARGET_FACTOR_BITS,
        "unique_variant": variant,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("x", encoding="utf-8") as handle:
        json.dump(output, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(f"wrote={OUTPUT} elapsed={output['elapsed_seconds']:.6f}", flush=True)


if __name__ == "__main__":
    main()

