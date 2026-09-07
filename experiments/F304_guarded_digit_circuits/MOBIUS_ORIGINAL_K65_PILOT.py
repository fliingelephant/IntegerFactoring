"""Correctly coupled original-input first-quotient pilot at k=65."""
import json, os, resource, signal, threading, time
from pathlib import Path

from MOBIUS_BANK import bank

TIMEOUT_SECONDS=30
MEMORY_BUDGET_BYTES=512*1024*1024
MEMORY_POLL_SECONDS=0.01

def power_sum(L,j):
    if j==0:return L
    if j==1:return L*(L-1)//2
    if j==2:return L*(L-1)*(2*L-1)//6
    if j==3:return (L*(L-1)//2)**2
    raise ValueError(j)

def memory_watch(stop):
    while not stop.wait(MEMORY_POLL_SECONDS):
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>MEMORY_BUDGET_BYTES:
            os._exit(86)

signal.alarm(TIMEOUT_SECONDS)
stop=threading.Event()
watcher=threading.Thread(target=memory_watch,args=(stop,),daemon=True)
watcher.start()
start=time.monotonic()
k=65
M=1<<k
L=M//2
s=k-1
N=9*M+1
A=B=1
C=2
n=(N-1)//2
largest_power_two=1<<((N//8).bit_length()-1)
assert largest_power_two<=N//8 and largest_power_two==M
moments,Q,counts=bank(s,A,B,C,n,3)
assert moments[0,0]==L
marginal_checks={}
for j in range(4):
    expected=power_sum(L,j)%(L*L)
    assert moments[0,j]==expected
    marginal_checks[f'0,{j}']=expected
for i in range(1,4):
    expected=power_sum(L,i)%(L*L)
    assert moments[i,0]==expected
    marginal_checks[f'{i},0']=expected
stop.set()
watcher.join()
signal.alarm(0)
result=dict(
    status='passed',
    k=k,
    M=M,
    L=L,
    s=s,
    N=N,
    A=A,
    B=B,
    C=C,
    n=n,
    D=3,
    largest_power_two_at_most_N_over_8=largest_power_two,
    S00=moments[0,0],
    marginal_checks=marginal_checks,
    moments={f'{i},{j}':value for (i,j),value in moments.items()},
    Q=Q,
    oracle=counts,
    checked_claim='The original-input coupling and only S_i0 and S_0j universal marginals were checked.',
    mixed_status='Computed and recorded, but not independently verified.',
    runtime_seconds=time.monotonic()-start,
    peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    timeout_seconds=TIMEOUT_SECONDS,
    memory_budget_bytes=MEMORY_BUDGET_BYTES,
    memory_watch_poll_seconds=MEMORY_POLL_SECONDS,
    enumeration_performed=False,
    resource_estimate=dict(
        carry_indices=69,
        guard_precision_bits=194,
        universal_power_indices=342,
        largest_power_bits_upper_bound=21889,
        estimated_modular_series_terms_under=575000,
        expected_peak_rss_bytes_under=128*1024*1024,
    ),
    preflight_basis='The immediately preceding two-map pilot took 0.604 seconds and 18.3 MB peak RSS on the same host.',
    scope='Correct original M=2^65 first-quotient map with L=M/2. Large mixed outputs are not independently verified.',
)
assert result['peak_rss_bytes']<=MEMORY_BUDGET_BYTES
base=Path(__file__).with_name('MOBIUS_ORIGINAL_K65_PILOT')
Path(f'{base}_output.json').write_text(json.dumps(result,indent=2)+'\n')
log='\n'.join([
    'MOBIUS_ORIGINAL_K65_PILOT',
    f"status={result['status']}",
    f"k={k}",
    f"M={M}",
    f"L={L}",
    f"s={s}",
    f"N={N}",
    f"largest_power_two_at_most_N_over_8={largest_power_two}",
    f"S00={moments[0,0]}",
    f"runtime_seconds={result['runtime_seconds']:.9f}",
    f"peak_rss_bytes={result['peak_rss_bytes']}",
    f"timeout_seconds={TIMEOUT_SECONDS}",
    f"memory_budget_bytes={MEMORY_BUDGET_BYTES}",
    'verification=original coupling and universal marginals only; large mixed values were not independently verified',
])+'\n'
Path(f'{base}_run.log').write_text(log)
print(log,end='')
