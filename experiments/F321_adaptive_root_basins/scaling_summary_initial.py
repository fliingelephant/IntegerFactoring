"""Finite log-log summaries of the six preselected balanced scale inputs.

No rerun or uncapped expectation is inferred. Estimated use <1 s /64 MiB;
only retained small JSON files are read. A 10-second alarm bounds this run.
"""
import hashlib
import json
import math
from pathlib import Path
import resource
import signal
import time

signal.alarm(10)
started = time.monotonic()
packet = Path(__file__).resolve().parent
scale_path = packet / 'scale_output.json'
rho_path = packet / 'rho_work_output.json'
scale = json.loads(scale_path.read_text())
rho = {row['N']: row for row in json.loads(rho_path.read_text())['cases']}
rows = []
for case in scale['cases']:
    if case['kind'] != 'balanced':
        continue
    adaptive = case['methods']['adaptive_roots']['summary']
    control = rho[case['N']]['rho_work_matched']['summary']
    assert adaptive['success_count'] == adaptive['trial_count']
    assert control['success_count'] == control['trial_count']
    rows.append(dict(p=case['p'], q=case['q'], N=case['N'],
                     trials=adaptive['trial_count'],
                     adaptive_gcd=adaptive['mean_gcd_calls_all_trials'],
                     adaptive_multiplications=adaptive['mean_modular_multiplications_all_trials'],
                     rho_multiplications=control['mean_modular_multiplications_all_trials']))
assert len(rows) == 6
x = [math.log2(row['p']) for row in rows]
xbar = sum(x)/len(x)
fits = {}
for name in ('adaptive_gcd', 'adaptive_multiplications', 'rho_multiplications'):
    y = [math.log2(row[name]) for row in rows]
    ybar = sum(y)/len(y)
    slope = sum((a-xbar)*(b-ybar) for a, b in zip(x, y))/sum((a-xbar)**2 for a in x)
    intercept = ybar-slope*xbar
    residual = sum((b-intercept-slope*a)**2 for a, b in zip(x, y))
    variation = sum((b-ybar)**2 for b in y)
    fits[name] = dict(log2_slope=slope, log2_intercept=intercept,
                      descriptive_r_squared=1-residual/variation)
result = dict(status='finite descriptive fits, not an asymptotic or probability theorem',
              selection='all six balanced scale cases; 32 trials each; no censors in either selected method',
              inputs={path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                      for path in (scale_path, rho_path)},
              source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              rows=rows, fits=fits, seconds=time.monotonic()-started,
              peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
(packet/'scaling_summary.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({key: value for key, value in result.items() if key != 'rows'}, indent=2))
