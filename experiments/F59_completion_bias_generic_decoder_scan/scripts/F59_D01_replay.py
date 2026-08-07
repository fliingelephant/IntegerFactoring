import json
import random
import time
from pathlib import Path

from F59_replay_core import (
    decode_relations,
    direct_event_summary,
    next_prime,
    relation,
    sample_unit,
    self_check,
    summarize_trials,
    walk_prefix,
)


RUN = "F59-D01-R2"
FAMILY = "F26"
TARGET_FACTOR_BITS = (10, 14, 18, 22)
RATIOS = ((21, 20), (4, 3), (7, 4))
TRIALS = 8
MASTER_SEED = 0xF59D01
OUTPUT = Path(__file__).resolve().parent.parent / "output" / f"{RUN}.json"


started = time.monotonic()
self_checks = self_check()
master = random.Random(MASTER_SEED)
input_records = []

for target_bits in TARGET_FACTOR_BITS:
    prime_p = next_prime(1 << target_bits)
    for ratio_numerator, ratio_denominator in RATIOS:
        lower_q = (ratio_numerator * prime_p + ratio_denominator - 1) // ratio_denominator
        prime_q = next_prime(max(prime_p + 2, lower_q))
        modulus = prime_p * prime_q
        input_bits = modulus.bit_length()
        batch_size = input_bits * input_bits

        iid_trials = []
        tail_trials = []
        for trial_index in range(TRIALS):
            iid_seed = master.getrandbits(64)
            iid_rng = random.Random(iid_seed)
            iid_direct = {}
            iid_relations = [
                relation(modulus, sample_unit(iid_rng, modulus, iid_direct))
                for _ in range(batch_size)
            ]
            iid_result = decode_relations(modulus, iid_relations)
            iid_result.update(
                {
                    "trial": trial_index,
                    "stream_seed": iid_seed,
                    "direct_gcd_events": direct_event_summary(iid_direct),
                }
            )
            iid_trials.append(iid_result)

            tail_seed = master.getrandbits(64)
            tail_rng = random.Random(tail_seed)
            tail_direct = {}
            tail_relations = []
            for _ in range(input_bits):
                start = sample_unit(tail_rng, modulus, tail_direct)
                tail_relations.extend(walk_prefix(modulus, start, input_bits, tail_direct))
            tail_result = decode_relations(modulus, tail_relations)
            tail_result.update(
                {
                    "trial": trial_index,
                    "stream_seed": tail_seed,
                    "start_count": input_bits,
                    "step_cap_per_start": input_bits,
                    "direct_gcd_events": direct_event_summary(tail_direct),
                }
            )
            tail_trials.append(tail_result)

        offset_direct = {}
        offset_relations = []
        for offset in range(1, input_bits + 1):
            offset_relations.extend(
                walk_prefix(modulus, modulus - offset, input_bits, offset_direct)
            )
        offset_result = decode_relations(modulus, offset_relations)
        offset_result.update(
            {
                "start_count": input_bits,
                "step_cap_per_start": input_bits,
                "direct_gcd_events": direct_event_summary(offset_direct),
            }
        )

        record = {
            "target_factor_bits": target_bits,
            "ratio_numerator": ratio_numerator,
            "ratio_denominator": ratio_denominator,
            "p": prime_p,
            "q": prime_q,
            "q_over_p": prime_q / prime_p,
            "N": modulus,
            "input_bits": input_bits,
            "declared_batch_size_n_squared": batch_size,
            "iid_single_step": {
                "summary": summarize_trials(iid_trials),
                "trials": iid_trials,
            },
            "random_tail_prefixes": {
                "summary": summarize_trials(tail_trials),
                "trials": tail_trials,
            },
            "deterministic_offset_tail_prefixes": offset_result,
        }
        input_records.append(record)
        print(
            json.dumps(
                {
                    "N": modulus,
                    "bits": input_bits,
                    "ratio": [ratio_numerator, ratio_denominator],
                    "iid_nonzero_kernel_trials": record["iid_single_step"]["summary"]["trials_with_nonzero_kernel"],
                    "iid_useful_trials": record["iid_single_step"]["summary"]["trials_with_useful_basis_root"],
                    "tail_nonzero_kernel_trials": record["random_tail_prefixes"]["summary"]["trials_with_nonzero_kernel"],
                    "tail_useful_trials": record["random_tail_prefixes"]["summary"]["trials_with_useful_basis_root"],
                    "offset_kernel_dimension": offset_result["kernel_dimension"],
                    "offset_useful": offset_result["factor_found_by_batch_decoder"],
                },
                sort_keys=True,
            ),
            flush=True,
        )

elapsed = time.monotonic() - started
payload = {
    "run": RUN,
    "family": FAMILY,
    "disposition": "corrected finite seeded replay; no asymptotic inference",
    "replays": "F59-D01",
    "master_seed": MASTER_SEED,
    "target_factor_bits": TARGET_FACTOR_BITS,
    "ratios": RATIOS,
    "trials_per_random_source": TRIALS,
    "batch_rule": "n^2 single-step relations, or n starts times at most n descent steps",
    "decoder": "factor-free parity gcd refinement followed by exact kernel-basis roots",
    "repairs": [
        "gcd-check the endpoint produced by the final capped transition",
        "runner preserves timeout and Python exit status",
    ],
    "self_checks": self_checks,
    "elapsed_seconds": elapsed,
    "records": input_records,
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT.open("w", encoding="utf-8") as handle:
    json.dump(payload, handle, indent=2, sort_keys=True)
    handle.write("\n")

print(json.dumps({"output": str(OUTPUT), "elapsed_seconds": elapsed}, sort_keys=True))
