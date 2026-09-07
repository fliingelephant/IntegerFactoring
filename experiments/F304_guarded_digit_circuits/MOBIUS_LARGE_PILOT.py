"""Bounded non-enumerative pilots for the original first-quotient patch."""
import json, os, resource, signal, threading, time
from pathlib import Path

from MOBIUS_BANK import bank

TIMEOUT_SECONDS=30
MEMORY_BUDGET_BYTES=512*1024*1024
MEMORY_POLL_SECONDS=0.01
PREFLIGHT=dict(
    observed_at='2026-09-07T08:41:24+0800',
    load_averages=[1.93,2.05,2.06],
    physical_memory_bytes=17179869184,
    system_memory_free_percent=71,
    busiest_process='suggestd at 100% CPU and 143424 KiB RSS',
    codex_process='codex at 1.3% CPU and 710864 KiB RSS',
)

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
rows=[]
for k in [33,65]:
    if k==65:
        first=rows[0]
        comfortable=first['runtime_seconds']<5 and first['peak_rss_bytes']<256*1024*1024
        if not comfortable:
            rows.append(dict(k=65,status='skipped',reason='The k=33 pilot did not leave the stated time or memory headroom.'))
            break
    case_start=time.monotonic()
    L=1<<k
    N=9*L+1
    A=B=1
    C=2
    n=(N-1)//2
    moments,Q,counts=bank(k,A,B,C,n,3)
    marginal_checks={}
    for j in range(4):
        expected=power_sum(L,j)%(L*L)
        assert moments[0,j]==expected
        marginal_checks[f'0,{j}']=expected
    for i in range(1,4):
        expected=power_sum(L,i)%(L*L)
        assert moments[i,0]==expected
        marginal_checks[f'{i},0']=expected
    row=dict(
        k=k,
        status='passed',
        D=3,
        N=N,
        A=A,
        B=B,
        C=C,
        n=n,
        marginal_checks=marginal_checks,
        moments={f'{i},{j}':value for (i,j),value in moments.items()},
        Q=Q,
        oracle=counts,
        checked_claim='Only S_i0 and S_0j were checked against universal marginal sums.',
        mixed_status='Computed and recorded, but not independently verified.',
        runtime_seconds=time.monotonic()-case_start,
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    )
    assert row['peak_rss_bytes']<=MEMORY_BUDGET_BYTES
    rows.append(row)
stop.set()
watcher.join()
signal.alarm(0)
result=dict(
    status='passed' if all(row['status']=='passed' for row in rows) else 'partial',
    pilots=rows,
    preflight=PREFLIGHT,
    resource_estimate=dict(
        k65_carry_indices=70,
        k65_guard_precision_bits=197,
        k65_universal_power_indices=347,
        k65_largest_power_bits_upper_bound=22556,
        k65_estimated_modular_series_terms_under=600000,
        expected_peak_rss_bytes_under=128*1024*1024,
    ),
    runtime_seconds=time.monotonic()-start,
    peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    timeout_seconds=TIMEOUT_SECONDS,
    memory_budget_bytes=MEMORY_BUDGET_BYTES,
    memory_watch_poll_seconds=MEMORY_POLL_SECONDS,
    enumeration_performed=False,
    scope='One-map first-quotient pilots. Large mixed outputs are not independently verified.',
)
base=Path(__file__).with_name('MOBIUS_LARGE_PILOT')
Path(f'{base}_output.json').write_text(json.dumps(result,indent=2)+'\n')
log_lines=[
    'MOBIUS_LARGE_PILOT',
    f"status={result['status']}",
    f"runtime_seconds={result['runtime_seconds']:.9f}",
    f"peak_rss_bytes={result['peak_rss_bytes']}",
    f"timeout_seconds={TIMEOUT_SECONDS}",
    f"memory_budget_bytes={MEMORY_BUDGET_BYTES}",
    f"preflight_load_averages={PREFLIGHT['load_averages']}",
    f"preflight_memory_free_percent={PREFLIGHT['system_memory_free_percent']}",
]
log_lines.extend(
    f"pilot=k{row['k']} status={row['status']} "
    + (f"runtime_seconds={row['runtime_seconds']:.9f} peak_rss_bytes={row['peak_rss_bytes']}" if row['status']=='passed' else f"reason={row['reason']}")
    for row in rows
)
log_lines.append('verification=universal marginals only; large mixed values were not independently verified')
log='\n'.join(log_lines)+'\n'
Path(f'{base}_run.log').write_text(log)
print(log,end='')
