#!/usr/bin/env python3
"""Test whether the exact high-bit word gains Prouhet-type vanishing moments."""
import json
import signal
import time
from pathlib import Path

signal.alarm(30)
started = time.monotonic()
rows = []
for k in range(3, 25):
    if time.monotonic()-started > 18:
        break
    modulus = 1 << k
    half_period = 1 << (k-3)
    moments = [0]*6
    u = 1
    for j in range(half_period):
        sign = 1 if u < modulus//2 else -1
        power = 1
        for order in range(6):
            moments[order] += sign*power
            power *= j
        u = 5*u % modulus
    first = next((i for i,v in enumerate(moments) if v),None)
    row = {'k':k,'half_period':half_period,'half_word_power_moments':moments,
           'zero_order_at_one':None if first is None else first+1}
    rows.append(row)
    print(k,'zero_order',row['zero_order_at_one'],'half_word_sum',moments[0],flush=True)
result = {'family':'route:F31','experiment':'experiment:F293_carry_convolution',
          'status':'exact_finite_moment_pilot',
          'resource_plan':{'seconds':20,'timeout_seconds':30,'peak_mb':64,'processes':1},
          'elapsed_seconds':time.monotonic()-started,'rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
