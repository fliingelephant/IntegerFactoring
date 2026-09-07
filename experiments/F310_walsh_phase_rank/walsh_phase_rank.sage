"""Exact finite-field ranks of fixed-order Boolean Walsh phase matrices."""
import json, os, random, resource, signal, threading, time
from pathlib import Path

from sage.all import GF, matrix

SEED=31020260907
RANK_PRIME=65521
OUTER_TIMEOUT_SECONDS=30
INTERNAL_TIMEOUT_SECONDS=28
MEMORY_BUDGET_BYTES=1024*1024*1024
MEMORY_POLL_SECONDS=0.01

def phase_value(x,N,L,s):
    denominator=1+2*x
    assert denominator&1
    y=(((N-1)//2-x)*pow(denominator,-1,L))%L
    return -1 if ((x>>(s-1))^(y>>(s-1)))&1 else 1

def memory_watch(stop):
    while not stop.wait(MEMORY_POLL_SECONDS):
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>MEMORY_BUDGET_BYTES:
            os._exit(86)

def run_case(s,N,label,field):
    started=time.monotonic()
    L=1<<s
    M=2*L
    r=(s-1)//2
    row_count=1<<r
    column_count=1<<(s-1-r)
    half=L//2
    phases=[]
    periodic_checks=0
    for x in range(half):
        value=phase_value(x,N,L,s)
        assert phase_value(x+half,N,L,s)==value
        phases.append(value)
        periodic_checks+=1
    A=matrix(field,row_count,column_count,
             lambda a,b: phases[a+(1<<r)*b])
    rank=int(A.rank())
    pivot_columns=[int(value) for value in A.pivots()]
    column_basis=A.matrix_from_columns(pivot_columns)
    independent_rows=[int(value) for value in column_basis.transpose().pivots()]
    minor=A.matrix_from_rows_and_columns(independent_rows,pivot_columns)
    determinant=int(minor.det())
    assert len(pivot_columns)==rank
    assert len(independent_rows)==rank
    assert determinant%RANK_PRIME!=0
    return dict(
        label=label,
        N=N,
        M=M,
        L=L,
        s=s,
        r=r,
        shape=[row_count,column_count],
        rank=rank,
        full_rank=rank==min(row_count,column_count),
        pivot_columns=pivot_columns,
        independent_rows=independent_rows,
        minor_determinant_mod_prime=determinant,
        phase_period=half,
        phase_period_checks=periodic_checks,
        positive_phases=sum(value==1 for value in phases),
        negative_phases=sum(value==-1 for value in phases),
        zero_inverse_denominators=0,
        factors_used=False,
        walltime_seconds=time.monotonic()-started,
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    )

def seeded_input(rng,M,excluded):
    while True:
        value=rng.randrange(8*M,16*M)|1
        if value not in excluded:
            return value

signal.signal(signal.SIGALRM,
              lambda signum,frame: (_ for _ in ()).throw(TimeoutError('internal 28-second alarm')))
signal.alarm(INTERNAL_TIMEOUT_SECONDS)
stop=threading.Event()
watcher=threading.Thread(target=memory_watch,args=(stop,),daemon=True)
watcher.start()
started=time.monotonic()
rng=random.Random(SEED)
field=GF(RANK_PRIME)
rows=[]
status='passed'
error=None
scale_decision=None
try:
    for s in [7,9,11]:
        M=1<<(s+1)
        fixed=9*M+1
        seeded=seeded_input(rng,M,{fixed})
        rows.append(run_case(s,fixed,'9M+1',field))
        rows.append(run_case(s,seeded,'seeded',field))
    pilot_walltime=time.monotonic()-started
    pilot_peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    scale_decision=pilot_walltime<5 and pilot_peak<512*1024*1024
    if scale_decision:
        for s in [13,15,17]:
            M=1<<(s+1)
            fixed=[9*M+1,9*M+3,9*M+5]
            seeded=seeded_input(rng,M,set(fixed))
            for offset,N in zip([1,3,5],fixed):
                rows.append(run_case(s,N,f'9M+{offset}',field))
            rows.append(run_case(s,seeded,'seeded',field))
    else:
        status='pilot_only'
except BaseException as exc:
    status='failed'
    error=f'{type(exc).__name__}: {exc}'
finally:
    signal.alarm(0)
    stop.set()
    watcher.join()

result=dict(
    status=status,
    error=error,
    seed=SEED,
    rank_field_prime=RANK_PRIME,
    cases=rows,
    scale_decision=scale_decision,
    case_count=len(rows),
    total_walltime_seconds=time.monotonic()-started,
    peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    outer_timeout_seconds=OUTER_TIMEOUT_SECONDS,
    internal_timeout_seconds=INTERNAL_TIMEOUT_SECONDS,
    memory_budget_bytes=MEMORY_BUDGET_BYTES,
    matrix_definition='A[a,b]=phase(a+2^r*b) after the proved L/2 period reduction.',
    scope='Exact finite evidence for one fixed low-bit/high-bit matrix order. No algorithmic lower bound.',
)
base=Path(__file__).with_name('walsh_phase_rank')
Path(f'{base}.json').write_text(json.dumps(result,indent=2)+'\n')
log_lines=[
    'F310_WALSH_PHASE_RANK',
    f'status={status}',
    f'seed={SEED}',
    f'rank_field_prime={RANK_PRIME}',
    f'scale_decision={scale_decision}',
    f'case_count={len(rows)}',
    f'total_walltime_seconds={result["total_walltime_seconds"]:.9f}',
    f'peak_rss_bytes={result["peak_rss_bytes"]}',
    f'outer_timeout_seconds={OUTER_TIMEOUT_SECONDS}',
    f'internal_timeout_seconds={INTERNAL_TIMEOUT_SECONDS}',
    f'memory_budget_bytes={MEMORY_BUDGET_BYTES}',
]
log_lines.extend(
    f'case={row["label"]} s={row["s"]} N={row["N"]} '
    f'shape={row["shape"][0]}x{row["shape"][1]} rank={row["rank"]} '
    f'determinant={row["minor_determinant_mod_prime"]} '
    f'walltime_seconds={row["walltime_seconds"]:.9f} '
    f'peak_rss_bytes={row["peak_rss_bytes"]}'
    for row in rows
)
log_lines.append('interpretation=exact finite rank evidence for this fixed ordering only; no lower bound')
log='\n'.join(log_lines)+'\n'
Path(f'{base}.log').write_text(log)
print(log,end='')
if status=='failed':
    raise RuntimeError(error)
