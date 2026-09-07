"""F313 canonical lift cocycle and complete cross bit; 30s / <256MiB."""
from pathlib import Path
import json, random, resource, signal, time

signal.alarm(30)
start=time.monotonic()
rng=random.Random(313)

def group_log(A,M):
    sigma=int(A%4==3)
    target=(-A if sigma else A)%M
    exponent,current,step=0,1,5
    for j in range(M.bit_length()-3):
        if ((target-current)>>(j+2))&1:
            exponent+=1<<j
            current=current*step%M
        step=step*step%M
    assert current==target
    return sigma,exponent

def K_mod4(A,B,M):
    T=M//4
    sa,a=group_log(A,M)
    sb,b=group_log(B,M)
    eta_a=pow(5,a,2*M)//M
    eta_b=pow(5,b,2*M)//M
    value=max(0,a+b-T+1)+eta_a*b+eta_b*a+sb*a+sa*b
    for r in (0,a,b,(a+b)%T):
        if r%2==0:
            value+=pow(5,r//2,2*M)//M+pow(5,r//2+T//2,2*M)//M
    value+=(A//M)*b+(B//M)*a
    return 2*(value%2)

counts=dict(log=0,cocycle=0,cross=0,raw_cross=0)
rows=[]
for k in range(3,10):
    M=1<<k
    T=M//4
    units=list(range(1,M,2))
    logs={A:group_log(A,M) for A in units}
    counts['log']+=len(units)
    eta=[pow(5,j,2*M)//M for j in range(T)]
    pairs=[(A,B) for A in units for B in units] if k<=5 else [(rng.choice(units),rng.choice(units)) for _ in range(96)]
    for A,B in pairs:
        sa,a=logs[A]
        sb,b=logs[B]
        actual=sum((A*w//M)*(B*pow(w,-1,M)//M) for w in units)%4
        predicted=K_mod4(A,B,M)
        assert actual==predicted
        counts['cross']+=1
        rawA,rawB=A+M*rng.randrange(3),B+M*rng.randrange(3)
        raw_actual=sum((rawA*w//M)*(rawB*pow(w,-1,M)//M) for w in units)%4
        assert K_mod4(rawA,rawB,M)==raw_actual
        counts['raw_cross']+=1
        w=rng.choice(units)
        sw,j=logs[w]
        c=((a+j)//T+eta[a]+eta[j]+eta[(a+j)%T])%2
        assert c==(A*w//M)%2
        counts['cocycle']+=1
        if len(rows)<12 or (k==9 and len(rows)<20):
            rows.append(dict(M=M,A=A,B=B,signA=sa,logA=a,signB=sb,logB=b,K_mod4=actual))

large=[]
for k in (32,64,128,256):
    M=1<<k
    A=(M//3)|1
    B=(M//5)|1
    tick=time.monotonic()
    value=K_mod4(A,B,M)
    large.append(dict(k=k,A=A,B=B,K_mod4=value,seconds=time.monotonic()-tick))
result=dict(counts=counts,rows=rows,large=large,seconds=time.monotonic()-start,
            peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({key:value for key,value in result.items() if key!='rows'},indent=2))
