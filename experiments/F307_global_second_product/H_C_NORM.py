"""Non-enumerative h_c norm residual and exact third-digit controls."""
import json, math, resource, signal, sys, time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'F304_guarded_digit_circuits'))
from MOBIUS_BANK import bank
signal.alarm(30); start=time.monotonic(); rows=[]
for s in range(3,11):
    L=1<<s
    for r in range(1,s+1):
        c=1<<r; m=L*c; P=3*s+2*r; modulus=1<<P
        moments,_,stats=bank(s,-1,1,c,0,1)
        Sbar=moments[1,1]
        assert c*Sbar%L==0
        qbar=c*Sbar//L
        J=(P-1)//(2*r)
        powers=[]
        for j in range(2*J+1):
            powers.append((L**(j+1)-sum(math.comb(j+1,t)*powers[t] for t in range(j)))//(j+1))
        elements=[1]
        for j in range(1,J+1):
            numerator=sum((-1)**(t-1)*elements[j-t]*powers[2*t] for t in range(1,j+1))
            assert numerator%j==0
            elements.append(numerator//j)
        rho=sum(e*pow(-c*c,j,modulus) for j,e in enumerate(elements))%modulus
        numerator=(rho-1+m*qbar-m*m*(qbar*(qbar-1)//2))%modulus
        assert numerator%(m*m)==0
        E=(numerator//(m*m))%L
        # Enumeration only in the independent audit below.
        S=Q=B=0; S2=Q2=0
        for x in range(L):
            y=x*pow(1+c*x,-1,L)%L
            z=x*pow(1+2*c*x,-1,L)%L
            q=((1+c*x)*y-x)//L; q2=((1+2*c*x)*z-x)//L
            S+=x*y; Q+=q; B+=q*(q-1)//2; S2+=x*z; Q2+=q2
        assert Q*L==c*S
        assert (Q2-2*Q)*L==2*c*(S2-S)
        third=(S-Sbar)//(L*L)
        assert S% (L*L)==Sbar and B%L==(-third-E)%L
        rows.append(dict(s=s,r=r,L=L,c=c,known_S_modL2=Sbar,known_norm_residual=E,
                         third_S_digit=third%L,B=B%L,zero_third_prediction=(-E)%L,
                         norm_precision_bits=P,norm_states=J+1,P240_bank=stats))
result=dict(rows=rows,cases=len(rows),runtime_seconds=time.monotonic()-start,
            peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            scope='P240 and the norm residual are non-enumerative; the missing third S digit is only an exact audit value.')
Path(__file__).with_name('H_C_NORM_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(cases=len(rows),zero_third_failures=sum(x['B']!=x['zero_third_prediction'] for x in rows),
                     runtime_seconds=result['runtime_seconds'],peak_rss_bytes=result['peak_rss_bytes']),indent=2))
