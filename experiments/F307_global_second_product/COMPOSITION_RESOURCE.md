# Composition continuation resource record

Each pilot was estimated below 30 seconds and 128 MiB, with one process at
a time. Both sources install a 30-second alarm. Preflight at 09:21 local
time on 2026-09-07 reported 70% available memory and load 2.23,2.03,2.04.

Commands:

    python3 experiments/F307_global_second_product/COMPOSITION.py > experiments/F307_global_second_product/COMPOSITION_run.log 2>&1
    python3 experiments/F307_global_second_product/H_C_NORM.py > experiments/F307_global_second_product/H_C_NORM_run.log 2>&1

The first run used 0.010939 seconds and 17,350,656 peak RSS bytes. The second
used 0.017216 seconds and 17,235,968 peak RSS bytes. The non-enumerative norm
and moment gates are separate from their canonical-point audit loops.
