"""F322 bounded comparison; supplied primes are offline instance labels only."""
import json
import math
import random
import resource
import signal
import time
from parity_paths import run

signal.alarm(25)
t = time.monotonic()
rng = random.Random(322)
rows = []
for p,q in [(11,19),(31,43),(101,107),(251,263),(503,509)]:
    n=p*q
    for trial in range(12):
        # Character labels select a diagnostic promise class, not algorithm actions.
        while True:
            a=rng.randrange(1,n)
            if math.gcd(a,n)==1 and pow(a,(p-1)//2,p)==p-1 and pow(a,(q-1)//2,q)==q-1:
                break
        while True:
            b=rng.randrange(1,n)
            if math.gcd(b,n)==1 and (pow(b,(p-1)//2,p)==p-1) != (pow(b,(q-1)//2,q)==q-1):
                break
        for matching in ['adjacent','negation']:
            row=run(n,a,b,False,matching)
            assert 'factor' in row['result']
            row.update(p=p,q=q,trial=trial)
            rows.append(row)
out=dict(status='completed',seed=322,rows=rows,elapsed_seconds=time.monotonic()-t,
         max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
with open('experiments/F322_ppa_collision_structure/scaling.json','w') as f:
    json.dump(out,f,indent=2)
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
for n in sorted(set(r['n'] for r in rows)):
    for m in ['adjacent','negation']:
        rr=[r for r in rows if r['n']==n and r['matching']==m]
        print(n,m,'mean_steps',sum(r['steps'] for r in rr)/len(rr),'max_steps',max(r['steps'] for r in rr),'max_branch_run',max(r['max_same_branch'] for r in rr))
