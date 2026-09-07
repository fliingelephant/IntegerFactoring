"""F313 all-input unshifted T/2 mod2 via a complete lifted linear window."""
from pathlib import Path
import ast, json, random, resource, signal, time

signal.alarm(30)
start=time.monotonic()
tree=ast.parse(Path(__file__).with_name('pilot.py').read_text())
node=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='group_log')
exec(compile(ast.Module(body=[node],type_ignores=[]),'pilot.py','exec'))

def floor_sum(n,m,a,b):
    result=0
    while True:
        aa,a=divmod(a,m)
        bb,b=divmod(b,m)
        result+=aa*n*(n-1)//2+bb*n
        y=a*n+b
        if y<m:
            return result
        n,b=divmod(y,m)
        m,a=a,m

def transport_bit(N,M):
    sigma,a=group_log(N,M)
    T=M//4
    C=pow(5,a,2*M)
    eta=C//M
    gamma=0
    for r in (0,a):
        if r%2==0:
            gamma+=pow(5,r//2,2*M)//M+pow(5,r//2+T//2,2*M)//M
    D=floor_sum(T,M,4*C,C)-2*floor_sum(T,2*M,4*C,C)
    assert (D-a)%2==0
    return (sigma+gamma+eta+(D-a)//2)%2,dict(sigma=sigma,a=a,C=C,D=D,eta=eta)

checks=0
rows=[]
rng=random.Random(3133)
for k in range(3,12):
    M=1<<k
    units=range(1,M,2)
    mu={w:pow(w,-1,M)*((w*pow(w,-1,M)-1)//M) for w in units}
    inputs=list(units) if k<=9 else [rng.randrange(1,M,2) for _ in range(100)]
    for N in inputs:
        predicted,details=transport_bit(N,M)
        actual=sum(mu[w]*(N*w//M) for w in units)
        assert actual%2==0
        assert predicted==(actual//2)%2
        checks+=1
        if len(rows)<12 or N in (3,5,7):
            rows.append(dict(k=k,N=N,t=predicted,**details))
large=[]
for k in (32,64,128,256,512):
    M=1<<k
    N=(M//3)|1
    tick=time.monotonic()
    value,details=transport_bit(N,M)
    large.append(dict(k=k,N=N,t=value,seconds=time.monotonic()-tick,**details))
result=dict(checks=checks,rows=rows,large=large,seconds=time.monotonic()-start,
            peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({key:value for key,value in result.items() if key!='rows'},indent=2))
