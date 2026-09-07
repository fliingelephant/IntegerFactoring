"""Exact edge controls for the canonical Möbius moment bank."""
import json, resource, signal, time
from pathlib import Path

from MOBIUS_BANK import bank

TIMEOUT_SECONDS=30
MEMORY_BUDGET_BYTES=512*1024*1024

signal.alarm(TIMEOUT_SECONDS)
start=time.monotonic()
cases=[
    dict(name='s1_D0_zero_n',s=1,A=-1,B=3,C=4,n=0,D=0),
    dict(name='s1_D1_negative_n',s=1,A=5,B=-3,C=6,n=-7,D=1),
    dict(name='s2_D0_negative_n',s=2,A=-5,B=-1,C=8,n=-4,D=0),
    dict(name='s2_D1_zero_n',s=2,A=3,B=-7,C=10,n=0,D=1),
    dict(name='s3_D0_negative_n',s=3,A=7,B=-9,C=16,n=-11,D=0),
    dict(name='s3_D1_zero_n',s=3,A=-3,B=5,C=18,n=0,D=1),
    dict(name='s4_D0_negative_n',s=4,A=-11,B=3,C=32,n=-25,D=0),
    dict(name='s4_D1_zero_n',s=4,A=9,B=-5,C=34,n=0,D=1),
]
rows=[]
checks=0
for case in cases:
    case_start=time.monotonic()
    s,A,B,C,n,D=(case[key] for key in ['s','A','B','C','n','D'])
    L=1<<s
    assert C>L and C>0 and C%2==0 and A%2 and B%2
    moments,Q,counts=bank(s,A,B,C,n,D)
    points=[]
    expected_Q=[]
    for x in range(L):
        denominator=B+C*x
        y=(n-A*x)*pow(denominator,-1,L)%L
        q_numerator=denominator*y-(n-A*x)
        assert q_numerator%L==0
        q=q_numerator//L
        points.append((x,y))
        if not expected_Q:
            expected_Q=[0]*(D+1)
        inverse=pow(denominator,-1,L)
        for j in range(D+1):
            expected_Q[j]+=q*inverse*pow(y,j,L)
    expected_Q=[value%L for value in expected_Q]
    requested_Q=Q[:D+1]
    assert len(requested_Q)==D+1
    assert requested_Q==expected_Q
    checks+=D+1
    expected_moments={}
    for i in range(D+1):
        for j in range(D+1):
            expected=sum(x**i*y**j for x,y in points)%(L*L)
            assert moments[i,j]==expected
            expected_moments[f'{i},{j}']=expected
            checks+=1
    rows.append(dict(
        **case,
        L=L,
        requested_Q=requested_Q,
        moments=expected_moments,
        oracle=counts,
        checks=(D+1)+(D+1)**2,
        runtime_seconds=time.monotonic()-case_start,
    ))
signal.alarm(0)
result=dict(
    status='passed',
    cases=rows,
    exact_checks=checks,
    runtime_seconds=time.monotonic()-start,
    peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    timeout_seconds=TIMEOUT_SECONDS,
    memory_budget_bytes=MEMORY_BUDGET_BYTES,
    scope='Exact enumeration only for eight edge controls with L at most 16.',
)
assert result['peak_rss_bytes']<=MEMORY_BUDGET_BYTES
base=Path(__file__).with_name('MOBIUS_EDGE_CONTROL')
Path(f'{base}_output.json').write_text(json.dumps(result,indent=2)+'\n')
log_lines=[
    'MOBIUS_EDGE_CONTROL',
    f"status={result['status']}",
    f"exact_checks={checks}",
    f"runtime_seconds={result['runtime_seconds']:.9f}",
    f"peak_rss_bytes={result['peak_rss_bytes']}",
    f"timeout_seconds={TIMEOUT_SECONDS}",
    f"memory_budget_bytes={MEMORY_BUDGET_BYTES}",
]
log_lines.extend(
    f"case={row['name']} s={row['s']} D={row['D']} L={row['L']} "
    f"checks={row['checks']} runtime_seconds={row['runtime_seconds']:.9f}"
    for row in rows
)
log='\n'.join(log_lines)+'\n'
Path(f'{base}_run.log').write_text(log)
print(log,end='')
