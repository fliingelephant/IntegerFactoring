"""Two moving finite simple poles plus an optional simple pole at infinity."""
import json, os, random, resource, signal, threading, time
from pathlib import Path

SEED=31120260908
OUTER_TIMEOUT_SECONDS=30
INTERNAL_TIMEOUT_SECONDS=28
MEMORY_BUDGET_BYTES=512*1024*1024
MEMORY_POLL_SECONDS=0.01

folder=Path(__file__).resolve().parent
prior=json.loads((folder/'output.json').read_text())

def mul(a,b,poly,m):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a>>m:a^=poly
    return z

def affine_quotient(word,ones,coordinate_words,m):
    constant=word&1
    out=word^(ones if constant else 0)
    for j in range(m):
        if ((word>>(1<<j))&1)^constant:
            out^=coordinate_words[j]
    return out

def translate_word(word,r,q):
    out=0
    for x in range(q):
        if word>>x&1:out|=1<<(x^r)
    return out

def walsh_max(word,q):
    values=[1-2*((word>>x)&1) for x in range(q)]
    h=1
    while h<q:
        for a in range(0,q,2*h):
            for j in range(h):
                left,right=values[a+j],values[a+j+h]
                values[a+j],values[a+j+h]=left+right,left-right
        h*=2
    return max(abs(value) for value in values)

def memory_watch(stop):
    while not stop.wait(MEMORY_POLL_SECONDS):
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>MEMORY_BUDGET_BYTES:
            os._exit(86)

def field_tables(m,poly):
    q=1<<m
    inverse=[0]*q
    for x in range(1,q):
        a=x;b=q-2;z=1
        while b:
            if b&1:z=mul(z,a,poly,m)
            b>>=1;a=mul(a,a,poly,m)
        inverse[x]=z
        assert mul(x,z,poly,m)==1
    trace=[]
    for x in range(q):
        value=x;total=0
        for _ in range(m):
            total^=value
            value=mul(value,value,poly,m)
        assert total in [0,1]
        trace.append(total)
    return inverse,trace

def search_field(m,target_rows):
    field_start=time.monotonic()
    q=1<<m
    poly=int(next(row['polynomial'] for row in prior['fields'] if row['m']==m),16)
    inverse,trace=field_tables(m,poly)
    ones=(1<<q)-1
    coordinate_words=[sum(((x>>j)&1)<<x for x in range(q)) for j in range(m)]
    linear_words=[]
    trace_mask_to_a={}
    for a in range(q):
        word=sum(trace[mul(a,x,poly,m)]<<x for x in range(q))
        linear_words.append(word)
        mask=sum(trace[mul(a,1<<j,poly,m)]<<j for j in range(m))
        assert mask not in trace_mask_to_a
        trace_mask_to_a[mask]=a
    assert len(trace_mask_to_a)==q

    base_words={}
    for b in range(1,q):
        base_words[b]=sum(trace[mul(b,inverse[x],poly,m)]<<x for x in range(q))

    buckets={}
    generated=0
    for r in range(q):
        for b in range(1,q):
            translated=translate_word(base_words[b],r,q)
            for t in [0,1]:
                word=translated^(t<<r)
                key=affine_quotient(word,ones,coordinate_words,m)
                generated+=1
                bucket=buckets.setdefault(key,[])
                if len(bucket)<2 and all(witness['r']!=r for witness in bucket):
                    bucket.append(dict(r=r,b=b,t=t,word=word,key=key))
    retained=[witness for bucket in buckets.values() for witness in bucket]
    assert generated==2*q*(q-1)
    assert all(len(bucket)<=2 and len({w['r'] for w in bucket})==len(bucket)
               for bucket in buckets.values())

    results=[]
    for target_row in target_rows:
        target_start=time.monotonic()
        target=int(target_row['truth_hex'],16)
        target_quotient=affine_quotient(target,ones,coordinate_words,m)
        maximum=walsh_max(target,q)
        rejected=maximum>2 and (maximum-2)**2>16*q
        models=[]
        pair_probes=0
        if not rejected:
            seen=set()
            for first in retained:
                complement=target_quotient^first['key']
                for second in buckets.get(complement,[]):
                    pair_probes+=1
                    if first['r']==second['r']:continue
                    ordered=sorted([first,second],key=lambda item:(item['r'],item['b'],item['t']))
                    left,right=ordered
                    residual=target^left['word']^right['word']
                    assert affine_quotient(residual,ones,coordinate_words,m)==0
                    epsilon=residual&1
                    linear_mask=sum(((((residual>>(1<<j))&1)^epsilon)<<j) for j in range(m))
                    a=trace_mask_to_a[linear_mask]
                    affine=linear_words[a]^(ones if epsilon else 0)
                    assert residual==affine
                    model_word=left['word']^right['word']^affine
                    assert model_word==target
                    identity=(left['r'],left['b'],left['t'],right['r'],right['b'],right['t'],a,epsilon)
                    if identity in seen:continue
                    seen.add(identity)
                    models.append(dict(
                        a=a,
                        epsilon=epsilon,
                        first_pole=dict(r=left['r'],b=left['b'],temporary_pole_bit=left['t']),
                        second_pole=dict(r=right['r'],c=right['b'],temporary_pole_bit=right['t']),
                        actual_filled_pole_bits=[(target>>left['r'])&1,(target>>right['r'])&1],
                        verified_full_truth_table=True,
                    ))
        results.append(dict(
            m=m,
            q=q,
            M=target_row['M'],
            L=2*q,
            N=target_row['N'],
            original_residue=target_row['N']-8*target_row['M'],
            encoding=target_row['encoding'],
            truth_hex=target_row['truth_hex'],
            walsh_max=maximum,
            walsh_bound_test='walsh_max <= 4*sqrt(q)+2',
            walsh_prescreen_rejected=rejected,
            search_attempted=not rejected,
            pair_probes=pair_probes,
            model_count=len(models),
            models=models,
            walltime_seconds=time.monotonic()-target_start,
        ))
    return dict(
        m=m,
        q=q,
        field_polynomial=hex(poly),
        singlepole_parameters_generated=generated,
        affine_quotient_keys=len(buckets),
        retained_witnesses=len(retained),
        maximum_witnesses_per_key=2,
        target_count=len(results),
        walsh_rejections=sum(row['walsh_prescreen_rejected'] for row in results),
        searched_targets=sum(row['search_attempted'] for row in results),
        fitted_targets=sum(bool(row['model_count']) for row in results),
        found_models=sum(row['model_count'] for row in results),
        rows=results,
        walltime_seconds=time.monotonic()-field_start,
        peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    )

signal.signal(signal.SIGALRM,
              lambda signum,frame: (_ for _ in ()).throw(TimeoutError('internal 28-second alarm')))
signal.alarm(INTERNAL_TIMEOUT_SECONDS)
stop=threading.Event()
watcher=threading.Thread(target=memory_watch,args=(stop,),daemon=True)
watcher.start()
started=time.monotonic()
rng=random.Random(SEED)
fields=[]
status='passed'
error=None
scale_stop=None
selected_q256_residues=sorted(rng.sample(list(range(1,512,2)),16))
try:
    for m in [5,6,7,8]:
        if m>=7 and (time.monotonic()-started>8 or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>256*1024*1024):
            scale_stop=f'before q={1<<m}: pilot no longer left the required headroom'
            status='partial'
            break
        q=1<<m
        selected=None if m<8 else set(selected_q256_residues)
        target_rows=[]
        for row in prior['rows']:
            if row['m']!=m:continue
            residue=row['N']-8*row['M']
            if selected is None or residue in selected:
                target_rows.append(row)
        expected=(2*q) if m<8 else 32
        assert len(target_rows)==expected
        fields.append(search_field(m,target_rows))
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
    selected_q256_original_residues=selected_q256_residues,
    fields=fields,
    completed_q=[field['q'] for field in fields],
    scale_stop=scale_stop,
    total_targets=sum(field['target_count'] for field in fields),
    total_walsh_rejections=sum(field['walsh_rejections'] for field in fields),
    total_searched_targets=sum(field['searched_targets'] for field in fields),
    total_fitted_targets=sum(field['fitted_targets'] for field in fields),
    total_found_models=sum(field['found_models'] for field in fields),
    total_walltime_seconds=time.monotonic()-started,
    peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    outer_timeout_seconds=OUTER_TIMEOUT_SECONDS,
    internal_timeout_seconds=INTERNAL_TIMEOUT_SECONDS,
    memory_budget_bytes=MEMORY_BUDGET_BYTES,
    witness_policy='At most two witnesses with distinct pole locations for each affine-quotient key.',
    coverage='Exhaustive original residues up to complement for q=32,64,128; seeded 16-residue subset for q=256; both encodings.',
    scope='Two distinct moving finite simple poles, nonzero residues, arbitrary affine trace, and two freely filled pole bits. No genus or complexity lower bound.',
)
(folder/'MOVING_POLES_output.json').write_text(json.dumps(result,indent=2)+'\n')
log_lines=[
    'F311_MOVING_POLES',
    f'status={status}',
    f'seed={SEED}',
    f'completed_q={result["completed_q"]}',
    f'total_targets={result["total_targets"]}',
    f'total_walsh_rejections={result["total_walsh_rejections"]}',
    f'total_searched_targets={result["total_searched_targets"]}',
    f'total_fitted_targets={result["total_fitted_targets"]}',
    f'total_found_models={result["total_found_models"]}',
    f'total_walltime_seconds={result["total_walltime_seconds"]:.9f}',
    f'peak_rss_bytes={result["peak_rss_bytes"]}',
    f'outer_timeout_seconds={OUTER_TIMEOUT_SECONDS}',
    f'internal_timeout_seconds={INTERNAL_TIMEOUT_SECONDS}',
    f'memory_budget_bytes={MEMORY_BUDGET_BYTES}',
]
for field in fields:
    log_lines.append(
        f'q={field["q"]} targets={field["target_count"]} '
        f'rejected={field["walsh_rejections"]} searched={field["searched_targets"]} '
        f'fitted={field["fitted_targets"]} models={field["found_models"]} '
        f'keys={field["affine_quotient_keys"]} witnesses={field["retained_witnesses"]} '
        f'walltime_seconds={field["walltime_seconds"]:.9f} peak_rss_bytes={field["peak_rss_bytes"]}'
    )
    for row in field['rows']:
        if row['walsh_prescreen_rejected'] or row['model_count']:
            log_lines.append(
                f'  N={row["N"]} residue={row["original_residue"]} encoding={row["encoding"]} '
                f'walsh_max={row["walsh_max"]} rejected={row["walsh_prescreen_rejected"]} '
                f'models={row["model_count"]}'
            )
            for model in row['models']:
                log_lines.append(f'    model={model}')
log_lines.append('interpretation=bounded exact search in the specified moving-pole family only')
log='\n'.join(log_lines)+'\n'
(folder/'MOVING_POLES_run.log').write_text(log)
print(log,end='')
if status=='failed':
    raise RuntimeError(error)
