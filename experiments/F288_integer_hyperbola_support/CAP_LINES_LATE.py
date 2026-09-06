"""Additional deterministic late-DFS stress, preserving the random audit.

Both factors have all-one low r bits; they occupy the last DFS subtree at
that depth. Labels only construct inputs and audit the completed searches.
One process, hard10s, soft budgets inherited from CAP_LINES_RANDOM.run.
"""
import json
import random
import signal
import time
import CAP_LINES_RANDOM as audit

SEED=202609070214

if __name__=='__main__':
    signal.alarm(10)
    start=time.monotonic()
    rng=random.Random(SEED)
    rows=[]
    inputs=[]
    for e in (12,16,20,24,28):
        B=1<<e
        r=max(2,2*e//3-3)
        s=1<<r
        factors=[]
        for low,high in ((9*B//8,11*B//8),(3*B//2,15*B//8)):
            while True:
                z=rng.randrange(low//s,high//s)*s+s-1
                if low<=z<high and audit.isprime(z):
                    factors.append(z)
                    break
        p,q=factors
        N=p*q
        inputs.append(dict(e=e,N=N,p=p,q=q,residue_bits=r,residue=s-1,
                          dfs_rank=(1<<(r-1))-1))
        for a,b in ((1,1),(2,1)):
            result=audit.run(N,a,b)
            expected=sorted((x,y) for x,y in ((p,q),(q,p)) if a*x+b*y<=result['U'])
            if result['status']=='complete':
                assert result['factors']==expected
            rows.append(dict(e=e,**result))
    print(json.dumps(dict(seed=SEED,elapsed_seconds=time.monotonic()-start,
        inputs=inputs,rows=rows),indent=2))
