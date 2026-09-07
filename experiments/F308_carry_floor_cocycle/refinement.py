"""Root's full-residue polarization of R; reuse F305's actual marginal code.

Only the named function definition is loaded, not F305's experiment driver.
30 second alarm; initial small controls, optional named large bit size.
"""
import ast, json, math, random, resource, signal, sys, time
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

signal.alarm(30)
start=time.monotonic()
source=Path('experiments/F305_input_carry_transport/input_transport.py')
tree=ast.parse(source.read_text())
definition=next(node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name=='marginal_bank')
exec(compile(ast.Module(body=[definition],type_ignores=[]),str(source),'exec'))
rng=random.Random(3082)
rows=[]
if len(sys.argv)==1:
    for k in range(3,10):
        M=1<<k
        units=range(1,M,2)
        mu={w:pow(w,-1,M)*((w*pow(w,-1,M)-1)//M) for w in units}
        for trial in range(4):
            A=rng.randrange(1,M,2)
            B=rng.randrange(1,M,2)
            for d in (0,-M//3,M//3):
                VAB=marginal_bank(M,A*B,d)[0][(2,2)]
                VB=marginal_bank(M,B,0)[0][(2,2)]
                VA=marginal_bank(M,A,d)[0][(2,2)]
                numerator=(VAB-A*A*VB-B*B*VA)%(2*M)
                assert numerator%2==0
                R=(numerator//2)*pow(A,-1,M)%M
                actual=sum(pow(w,-1,M)**2*(B*w//M)*((A*(B*w%M)-d)//M) for w in units)%M
                assert R==actual
                if d==0:
                    assert VAB%2==VB%2==VA%2==0
                    SA=(sum(mu[w]*(A*w//M) for w in units)-(VA//2)*pow(A,-1,M))%M
                    SB=(sum(mu[w]*(B*w//M) for w in units)-(VB//2)*pow(B,-1,M))%M
                    SAB=(sum(mu[w]*(A*B*w//M) for w in units)-(VAB//2)*pow(A*B,-1,M))%M
                    K=sum((A*w//M)*(B*pow(w,-1,M)//M) for w in units)%M
                    assert (SAB-B*SA-A*SB+K)%M==0
                rows.append(dict(k=k,A=A,B=B,d=d,R_mod_M=R))
    name='refinement_small'
else:
    k=int(sys.argv[1])
    M=1<<k
    A=(M//3)|1
    B=(M//5)|1
    d=M//7
    values=[]
    for slope,cut in ((A*B,d),(B,0),(A,d)):
        tick=time.monotonic()
        bank,stats=marginal_bank(M,slope,cut)
        values.append(bank[(2,2)])
        rows.append(dict(k=k,slope=slope,d=cut,V=bank[(2,2)],stats=stats,seconds=time.monotonic()-tick))
    numerator=(values[0]-A*A*values[1]-B*B*values[2])%(2*M)
    assert numerator%2==0
    R=numerator//2*pow(A,-1,M)%M
    rows.append(dict(R_mod_M=R))
    name='refinement_k'+str(k)
result=dict(rows=rows,seconds=time.monotonic()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_name(name+'.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result if len(sys.argv)>1 else dict(checks=len(rows),seconds=result['seconds'],peak_rss_bytes=result['peak_rss_bytes']),indent=2))
