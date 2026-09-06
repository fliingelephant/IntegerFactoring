"""F301 / route:F31: interval-isolated imaginary poles and positive residues.

One Sage process, estimated<512MiB and<20s; 45-second alarm. Preflight06:11:
load2.90/2.31/2.14,73% available memory, no other numerical process.
"""

from sage.all import QQ, RealIntervalField
import json
import math
import resource
import signal
import time
from pathlib import Path

signal.alarm(45)
started = time.monotonic()
RIF = RealIntervalField(200)
pi = RIF.pi()
target_width = QQ(1)/(1 << 70)
rows = []
value_checks = 0
pole_count = 0
for m in (8,32,256):
    k = m.bit_length()-1
    repeat = 2
    while 3**repeat < 32*m:
        repeat += 2
    scales = [1 << j for j in range(k+2)]
    scale_sum = sum(scales)
    degree = repeat*len(scales)
    upper_bound = QQ(2*repeat*scale_sum)
    derivative_lower = QQ(2*repeat*scale_sum)/(upper_bound**2+max(scales)**2)
    poles = []
    for level in range(degree//2):
        lower, upper = QQ(0), upper_bound
        iterations = 0
        while upper-lower > target_width:
            midpoint = (lower+upper)/2
            phase = 2*repeat*sum((RIF(a)/RIF(midpoint)).arctan() for a in scales)
            residual = phase-(2*level+1)*pi
            if residual.lower() > 0:
                lower = midpoint
            elif residual.upper() < 0:
                upper = midpoint
            else:
                error = max(abs(residual.lower().exact_rational()),
                            abs(residual.upper().exact_rational()))
                radius = error/derivative_lower
                lower = max(lower,midpoint-radius)
                upper = min(upper,midpoint+radius)
            iterations += 1
        y = RIF(lower,upper)
        residue = 1/(repeat*sum(RIF(a)/(y*y+a*a) for a in scales))
        assert residue.lower() > 0
        poles.append((lower,upper,y,residue,iterations))
    poles.sort(key=lambda item:item[0])
    assert poles[0][0] > (pi/(4*repeat)).upper()
    assert poles[-1][1] < (RIF(2*repeat*scale_sum)/pi).lower()
    for left,right in zip(poles,poles[1:]):
        assert right[0]-left[1] > (pi/(2*repeat)).upper()
    normalization = sum(2*pole[3] for pole in poles)
    assert 0 in normalization-repeat*scale_sum
    for x in (1,3,5,m//2,m-1,2*m-1,-3,-(m-1)):
        plus = math.prod(x+a for a in scales)**repeat
        minus = math.prod(x-a for a in scales)**repeat
        exact = QQ(plus-minus)/(plus+minus)
        partial = sum(2*residue*x/(x*x+y*y) for _,_,y,residue,_ in poles)
        difference = partial-RIF(exact)
        assert 0 in difference
        assert difference.absolute_diameter() < (RIF(1)/(1 << 45)).lower()
        value_checks += 1
    pole_count += len(poles)
    rows.append({"m":m,"even_repeat":repeat,"degree":degree,
                 "positive_poles":len(poles),"sum_all_residues":str(normalization),
                 "exact_residue_sum":repeat*scale_sum,
                 "poles":[{"lower":str(lower),"upper":str(upper),
                           "positive_residue":str(residue),"bisections":iterations}
                          for lower,upper,_,residue,iterations in poles]})

result = {"status":"complete","family":"route:F31","precision_bits":200,
          "root_width_bound":"2^-70","positive_poles_isolated":pole_count,
          "partial_fraction_value_checks":value_checks,"cases":rows,
          "scope":"Rigorous real-interval root brackets and identity enclosures; no modular graph sum is accelerated.",
          "runtime_seconds":time.monotonic()-started,
          "peak_rss_bytes":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({key:result[key] for key in ("status","positive_poles_isolated",
                "partial_fraction_value_checks","runtime_seconds","peak_rss_bytes")}))
