"""Exact rational controls; enumeration supplies moments, not a fast oracle."""
import json, math, resource, signal, time
from fractions import Fraction as F
from pathlib import Path

signal.alarm(60)
start = time.monotonic()
ZERO = (F(0), F(0))
ONE = (F(1), F(0))

def add(a, b):
    return a[0]+b[0], a[1]+b[1]

def mul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]

def scale(a, x):
    return a[0]*x, a[1]*x

def inv(a):
    d = a[0]**2+a[1]**2
    return a[0]/d, -a[1]/d

def recip(a, z):
    return inv((a-z[0], -z[1]))

def norm2(a):
    return a[0]**2+a[1]**2

def encode(a):
    return [str(v) for v in a]

rows = []
cache = json.load(open('experiments/F301_factor_rectangles/rational_poles.json'))
for M, N in [(32,481),(32,497),(64,1001),(128,1995)]:
    L = M//2
    lower = [(a, (N*pow(a,-1,L))%L) for a in range(1,L,2)]
    signs = [1-2*((N-a*b)//L % 2) for a,b in lower]
    C = sum(s == 1 for s in signs)
    muL = sum(a*b for a,b in lower)
    muM = sum(a*((N*pow(a,-1,M))%M) for a in range(1,M,2))
    assert muM == 2*muL+L**3//2+L**2*C
    heights = [('rational_far', F(M)), ('rational_very_far', F(M*M))]
    if M == 32:
        case = next(c for c in cache['cases'] if c['m']==M)
        for label,p in [('cached_near',case['poles'][0]),('cached_far',case['poles'][-1])]:
            heights.append((label,(F(p['lower'])+F(p['upper']))/4))
    for label,y in heights:
        # Half-integer real parts from public integer windows near sqrt(N).
        A = math.isqrt(N)
        z,w = (F(2*A-1,2), y), (F(2*A+1,2), y)
        exact = ZERO
        for a in range(1,M,2):
            b = N*pow(a,-1,M)%M
            exact = add(exact,mul(recip(a,z),recip(b,w)))
        unsigned,signed = ZERO,ZERO
        for (a,b),sigma in zip(lower,signs):
            az,bw,azL,bwL=recip(a,z),recip(b,w),recip(a+L,z),recip(b+L,w)
            unsigned=add(unsigned,scale(mul(add(az,azL),add(bw,bwL)),F(1,2)))
            signed=add(signed,scale(mul(add(az,scale(azL,-1)),add(bw,scale(bwL,-1))),F(sigma,2)))
        assert add(unsigned,signed)==exact
        eta=F(1,M**6)
        row=dict(M=M,N=N,label=label,poles=[encode(z),encode(w)],C=C,tau00=sum(signs),lift_exact=True,
                 dropping_carry_exceeds_target=norm2(signed)>eta**2,target=str(eta),signed_component_float=[float(x) for x in signed])
        rho=F(L,2)/y
        if rho>=1:
            row['taylor']='global geometric bound unavailable'
        elif label.startswith('cached'):
            row['taylor']='not run: cached rational midpoint used for exact lift only'
        else:
            K=1
            while True:
                E=rho**K/(y*(1-rho))
                bound=L*(E/y+E/(y*(1-rho)))
                if bound<=eta: break
                K+=1
            center=F(L,2)
            coeff=[]
            for pole in [z,w]:
                h=inv((pole[0]-center,pole[1])); hL=inv((pole[0]-L-center,pole[1]))
                hp,hLp=h,hL; ss=[]; dd=[]
                for i in range(K):
                    ss.append(scale(add(hp,hLp),-1)); dd.append(add(hLp,scale(hp,-1)))
                    hp,hLp=mul(hp,h),mul(hLp,hL)
                coeff.append((ss,dd))
            moments=[[0]*K for _ in range(K)]; twists=[[0]*K for _ in range(K)]
            for (a,b),sigma in zip(lower,signs):
                xp,yp=[1],[1]
                for i in range(1,K): xp.append(xp[-1]*(a-center)); yp.append(yp[-1]*(b-center))
                for i in range(K):
                    for j in range(K):
                        v=xp[i]*yp[j]; moments[i][j]+=v; twists[i][j]+=sigma*v
            approx=ZERO
            for i in range(K):
                for j in range(K):
                    approx=add(approx,scale(mul(coeff[0][0][i],coeff[1][0][j]),F(moments[i][j],2)))
                    approx=add(approx,scale(mul(coeff[0][1][i],coeff[1][1][j]),F(twists[i][j],2)))
            error=add(approx,scale(exact,-1))
            assert norm2(error)<=bound**2
            row.update(taylor='certified',degree_terms=K,moment_states=2*K*K,
                       bound=str(bound),error_float=[float(x) for x in error],
                       moment_construction_points=len(lower),moment_construction_scalar_updates=2*len(lower)*K*K)
        rows.append(row)
result=dict(rows=rows,scope='Original fixed N; exact enumeration is the control and moment constructor, not a quasipolynomial evaluator.',
            runtime_seconds=time.monotonic()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path(__file__).with_name('output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(cases=len(rows),runtime_seconds=result['runtime_seconds'],peak_rss_bytes=result['peak_rss_bytes'],
                     taylor=[(r['M'],r['label'],r.get('degree_terms'),r.get('moment_states')) for r in rows]),indent=2))
