"""F291 exact global-direction dominance certificates.

One process, 15-second alarm, estimated <64 MB. No factor labels used.
Every issued certificate is checked over all shears at the pilot modulus.
"""
import json
import math
from pathlib import Path
import random
import signal
import time

def winner(T,W,a,b,s,d):
    Q=2*s*s
    delta=s*d
    c1=(T*b*Q,2*W*b*Q)
    c2=(T*(-b*delta+a*s),2*W*(-b*delta-a*s))
    e1,e2=(1,0),(0,1)
    while True:
        n1=c1[0]**2+c1[1]**2
        if c2[0]**2+c2[1]**2<n1:
            c1,c2,e1,e2=c2,c1,e2,e1
            n1=c1[0]**2+c1[1]**2
        mu=(2*(c1[0]*c2[0]+c1[1]*c2[1])+n1)//(2*n1)
        if not mu:
            break
        c2=(c2[0]-mu*c1[0],c2[1]-mu*c1[1])
        e2=(e2[0]-mu*e1[0],e2[1]-mu*e1[1])
    A=Q*e1[0]-delta*e1[1]
    B=s*e1[1]
    g=math.gcd(A,B)
    A,B=A//g,B//g
    if A<0 or (A==0 and B<0):
        A,B=-A,-B
    return A,B

def weight2(T,W,a,b,A,B):
    return (T*(b*A+a*B))**2+(2*W*(b*A-a*B))**2

if __name__=='__main__':
    signal.alarm(15)
    started=time.monotonic()
    rng=random.Random(202609070240)
    path=Path(__file__).with_name('output.json')
    inputs=json.loads(path.read_text())['inputs']
    rows=[]
    for label in inputs:
        if label['e']!=16:
            continue
        N=label['N']
        r=7
        s=1<<r
        R=2*s
        for a,b in ((1,1),(2,1)):
            U=math.isqrt(17*a*b*N//4)
            zlo=math.isqrt(4*a*b*N)
            zlo+=zlo*zlo<4*a*b*N
            T=U-zlo
            W=math.isqrt(U*U-4*a*b*N)
            tested=issued=checks=0
            certificates=[]
            while tested<64:
                A=rng.randrange(-4*math.isqrt(s),4*math.isqrt(s)+1)
                B=rng.randrange(1,4*math.isqrt(s)+1)|1
                if math.gcd(A,B)!=1:
                    continue
                tested+=1
                star=(-A*pow(B,-1,R))%R
                E=winner(T,W,a,b,s,star)
                fD=weight2(T,W,a,b,A,B)
                fE=weight2(T,W,a,b,*E)
                gE=math.gcd(E[0]+E[1]*star,R)
                if fE*R*R>=fD*gE*gE:
                    continue
                issued+=1
                for d in range(R):
                    gD=math.gcd(A+B*d,R)
                    ge=math.gcd(E[0]+E[1]*d,R)
                    assert fE*gD*gD<fD*ge*ge
                    checks+=1
                certificates.append(dict(D=[A,B],star=star,E=list(E),
                    squared_weight_D=fD,squared_weight_E=fE,gcd_at_star_E=gE))
            selected=set()
            selected_even_B=0
            for u in range(1,s,2):
                Q=2*s*s
                delta=N*(pow(u+s,-1,Q)-pow(u,-1,Q))%Q
                D=winner(T,W,a,b,s,delta//s)
                selected.add(D)
                if D[1]%2==0:
                    selected_even_B+=1
                    continue
                star=(-D[0]*pow(D[1],-1,R))%R
                E=winner(T,W,a,b,s,star)
                assert weight2(T,W,a,b,*E)*R*R>=weight2(T,W,a,b,*D)*math.gcd(E[0]+E[1]*star,R)**2
            rows.append(dict(N=N,family=label['family'],normal=[a,b],r=r,
                candidates=tested,global_certificates=issued,all_shear_checks=checks,
                selected_directions=len(selected),selected_even_B=selected_even_B,
                certificates=certificates))
    print(json.dumps(dict(seed=202609070240,elapsed_seconds=time.monotonic()-started,rows=rows),indent=2))
