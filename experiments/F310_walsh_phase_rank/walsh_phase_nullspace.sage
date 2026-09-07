"""Exact rational right nullspaces for the structured F310 phase matrices."""
import json, math, os, resource, signal, threading, time
from pathlib import Path

from sage.all import QQ, matrix

OUTER_TIMEOUT_SECONDS=30
INTERNAL_TIMEOUT_SECONDS=28
MEMORY_BUDGET_BYTES=1024*1024*1024
MEMORY_POLL_SECONDS=0.01

def phase_value(x,N,L,s):
    denominator=1+2*x
    assert denominator&1
    y=(((N-1)//2-x)*pow(denominator,-1,L))%L
    return -1 if ((x>>(s-1))^(y>>(s-1)))&1 else 1

def primitive_integer_vector(vector):
    denominator=1
    for value in vector:
        denominator=math.lcm(denominator,int(value.denominator()))
    integers=[int(value*denominator) for value in vector]
    common=0
    for value in integers:
        common=math.gcd(common,abs(value))
    assert common>0
    integers=[value//common for value in integers]
    first=next(value for value in integers if value)
    if first<0:
        integers=[-value for value in integers]
    return integers

def memory_watch(stop):
    while not stop.wait(MEMORY_POLL_SECONDS):
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>MEMORY_BUDGET_BYTES:
            os._exit(86)

def run_case(s):
    started=time.monotonic()
    L=1<<s
    M=2*L
    N=9*M+1
    r=(s-1)//2
    row_count=1<<r
    column_count=1<<(s-1-r)
    phases=[phase_value(x,N,L,s) for x in range(L//2)]
    A=matrix(QQ,row_count,column_count,
             lambda a,b: phases[a+(1<<r)*b])
    rank=int(A.rank())
    basis=A.right_kernel().basis()
    vectors=[]
    for index,vector in enumerate(basis):
        integers=primitive_integer_vector(vector)
        assert not any(A*matrix(QQ,column_count,1,integers))
        support=[position for position,value in enumerate(integers) if value]
        vectors.append(dict(
            index=index,
            vector=integers,
            support=support,
            support_size=len(support),
            max_absolute_entry=max(abs(value) for value in integers),
            first_nonzero_index=support[0],
            first_nonzero_value=integers[support[0]],
            primitive_gcd=math.gcd(*[abs(value) for value in integers]),
        ))
    assert len(vectors)==column_count-rank
    return dict(
        N=N,
        M=M,
        L=L,
        s=s,
        r=r,
        shape=[row_count,column_count],
        rank_over_QQ=rank,
        nullity=column_count-rank,
        right_nullspace=vectors,
        factors_used=False,
        zero_inverse_denominators=0,
        walltime_seconds=time.monotonic()-started,
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    )

signal.signal(signal.SIGALRM,
              lambda signum,frame: (_ for _ in ()).throw(TimeoutError('internal 28-second alarm')))
signal.alarm(INTERNAL_TIMEOUT_SECONDS)
stop=threading.Event()
watcher=threading.Thread(target=memory_watch,args=(stop,),daemon=True)
watcher.start()
started=time.monotonic()
rows=[]
status='passed'
error=None
try:
    for s in [7,9,11,13]:
        rows.append(run_case(s))
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
    cases=rows,
    case_count=len(rows),
    total_walltime_seconds=time.monotonic()-started,
    peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    outer_timeout_seconds=OUTER_TIMEOUT_SECONDS,
    internal_timeout_seconds=INTERNAL_TIMEOUT_SECONDS,
    memory_budget_bytes=MEMORY_BUDGET_BYTES,
    scope='Exact QQ nullspaces for N=9M+1 and the four specified fixed-order matrices only.',
)
base=Path(__file__).with_name('walsh_phase_nullspace')
Path(f'{base}.json').write_text(json.dumps(result,indent=2)+'\n')
log_lines=[
    'F310_WALSH_PHASE_NULLSPACE',
    f'status={status}',
    f'case_count={len(rows)}',
    f'total_walltime_seconds={result["total_walltime_seconds"]:.9f}',
    f'peak_rss_bytes={result["peak_rss_bytes"]}',
    f'outer_timeout_seconds={OUTER_TIMEOUT_SECONDS}',
    f'internal_timeout_seconds={INTERNAL_TIMEOUT_SECONDS}',
    f'memory_budget_bytes={MEMORY_BUDGET_BYTES}',
]
for row in rows:
    log_lines.append(
        f'case=s{row["s"]} N={row["N"]} shape={row["shape"][0]}x{row["shape"][1]} '
        f'rank_QQ={row["rank_over_QQ"]} nullity={row["nullity"]} '
        f'walltime_seconds={row["walltime_seconds"]:.9f} peak_rss_bytes={row["peak_rss_bytes"]}'
    )
    for vector in row['right_nullspace']:
        log_lines.append(
            f'  vector={vector["index"]} support={vector["support"]} '
            f'entries={vector["vector"]}'
        )
log_lines.append('interpretation=exact finite QQ nullspaces for the fixed order only; no general theorem or lower bound')
log='\n'.join(log_lines)+'\n'
Path(f'{base}.log').write_text(log)
print(log,end='')
if status=='failed':
    raise RuntimeError(error)
