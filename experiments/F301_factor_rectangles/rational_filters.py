"""F301 / route:F31: exact rational step bounds and certified rectangle sums.

One Sage process; estimated<512MiB and<30s, 60-second alarm. Preflight at
06:00 local: load2.03/2.09/2.04,73% available memory, no numerical process.
The graph sums enumerate every unit; this is not a fast factoring algorithm.
"""

from sage.all import RealIntervalField
import json
import math
import resource
import signal
import time
from fractions import Fraction
from pathlib import Path

signal.alarm(60)
started = time.monotonic()
RIF = RealIntervalField(200)
tables = {}
bound_rows = []
integer_checks = 0
for k in range(3, 17):
    m = 1 << k
    repeat = 2
    while 3**repeat < 32*m:
        repeat += 2
    powers = [1 << j for j in range(k+2)]
    weights = {}
    max_operand_bits = 0
    for x in range(1, 2*m, 2):
        plus = math.prod(x+power for power in powers)**repeat
        minus = math.prod(x-power for power in powers)**repeat
        assert plus > 0 and minus >= 0
        assert 3**repeat*minus <= plus
        integer_checks += 1
        max_operand_bits = max(max_operand_bits,plus.bit_length(),minus.bit_length())
        if m <= 256:
            denominator = RIF(plus)+RIF(minus)
            weights[x] = RIF(plus)/denominator
            weights[-x] = RIF(minus)/denominator
    if m <= 256:
        tables[m] = weights
    bound_rows.append({"m":m,"even_repeat":repeat,"degree":(k+2)*repeat,
                       "tested_positive_odd_arguments":m,
                       "max_integer_operand_bits":max_operand_bits,
                       "exact_step_error_bound":f"1/{3**repeat}"})

rectangle_rows = []
ratio = Fraction(17,16)
enumerated_units = 0
for N in (289,323,437,667,1009,2021,4093):
    m = 1 << ((N//8).bit_length()-1)
    weights = tables[m]
    graph = [(u,N*pow(u,-1,m)%m) for u in range(1,m,2)]
    left = Fraction(16)
    box_index = 0
    while left*left <= N:
        A, B = max(17,math.ceil(left)), min(math.isqrt(N),math.floor(ratio*left))
        C, D = max(1,math.ceil(N/(ratio*left))), min(m-1,math.floor(N/left))
        if A <= B and C <= D:
            truth = sum(A<=u<=B and C<=v<=D for u,v in graph)
            score = RIF(0)
            for u,v in graph:
                score += (weights[2*u-2*A+1]*weights[2*B+1-2*u]
                          *weights[2*v-2*C+1]*weights[2*D+1-2*v])
            enumerated_units += len(graph)
            error_bound = RIF(1)/8
            lower_integer = int((score-error_bound).lower().ceil())
            upper_integer = int((score+error_bound).upper().floor())
            assert lower_integer == upper_integer == truth
            rectangle_rows.append({"N":N,"m":m,"box_index":box_index,
                                   "x_interval":[A,B],"y_interval":[C,D],
                                   "exact_count":truth,"filter_sum_enclosure":str(score),
                                   "certified_count":lower_integer})
        box_index += 1
        left *= ratio

result = {"status":"complete","family":"route:F31","interval_precision_bits":200,
          "exact_integer_step_checks":integer_checks,"step_bounds":bound_rows,
          "rectangle_checks":rectangle_rows,"enumerated_graph_units":enumerated_units,
          "scope":"Exact integer inequalities and rigorous real-interval sums plus the proved1/8 approximation bound; graph enumeration remains numerical in m.",
          "runtime_seconds":time.monotonic()-started,
          "peak_rss_bytes":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"status":"complete","integer_checks":integer_checks,
                  "rectangle_checks":len(rectangle_rows),"enumerated_units":enumerated_units,
                  "runtime_seconds":result["runtime_seconds"],"peak_rss_bytes":result["peak_rss_bytes"]}))
