"""F294 exact near-affine half-window counts and slope-block averaging.

One process, 25-second alarm, estimated <128 MB. Random parameters are seeded;
actual inverse-chart checks retain their coefficient/window coupling.
"""
import json
import random
import signal
import time

def floor_sum(n,m,a,b):
    total=0
    while True:
        total+=(n-1)*n*(a//m)//2+n*(b//m)
        a%=m
        b%=m
        y=a*n+b
        if y<m:
            return total
        n,b=y//m,y%m
        m,a=a,m

def affine_half(Q,a,c):
    H=Q//2
    return floor_sum(H,Q,a,c)-floor_sum(H,Q,a,c-H)

def quadratic_half(K,R,beta,alpha,C):
    return quadratic_window(K,R,beta,alpha,C,1<<(K-1))

def quadratic_window(K,R,beta,alpha,C,length):
    Q=1<<K
    if R>=K:
        return floor_sum(length,Q,alpha,C)-floor_sum(length,Q,alpha,C-Q//2)
    L=1<<(K-R)
    H=1<<R
    coefficient=(1<<R)*beta
    total=0
    for l in range(min(L,length)):
        n=(length-1-l)//L+1
        offset=(alpha*l+C+coefficient*l*l)//L
        total+=floor_sum(n,H,alpha,offset)-floor_sum(n,H,alpha,offset-H//2)
    return total

def triangular(m,z):
    return abs(z%m-m//2)

def special(r,t,beta,c):
    m=1<<r
    if r==1:
        return 2*triangular(m,c) if t%2 else 1
    if t%2:
        return m*m//4
    z=(t//2)*pow(beta,-1,m)%m
    C=(c-beta*z*z)%m
    if r%2==0:
        return m*m//4+(1<<(r//2))*(triangular(m,C)+triangular(m,C+beta*(m//4))-m//2)
    return m*m//4+(1<<((r+1)//2))*(triangular(m,C+beta*(m//8))-m//4)

def block(r,a,beta,D,u,t0,A=0,B=0):
    m=1<<r
    return block_window(r,a,beta,D,u,t0,A,B,m*m//2)

def block_window(r,a,beta,D,u,t0,A,B,length):
    m=1<<r
    L=1<<(r-u)
    alpha=a+m*t0
    input_start=-(-A//L)
    output_start=-(-(B-D)//L)
    R=2*r-u
    coefficient=(1<<R)*beta
    residual_alpha=alpha+2*coefficient*input_start
    residual_C=alpha*input_start+coefficient*input_start*input_start-output_start
    exceptional=-(-(A+length)//L)-input_start
    residual=quadratic_window(r+u,R,beta,residual_alpha,residual_C,exceptional)
    baseline=L*(length-exceptional)//2
    return baseline+L*residual

def brute(r,alpha,beta,D,A=0,B=0):
    m=1<<r
    q=m*m
    return sum(((alpha*j+m*beta*j*j+D-B)%q)<q//2
               for i in range(q//2) for j in ((A+i)%q,))

if __name__=='__main__':
    signal.alarm(25)
    start=time.monotonic()
    rng=random.Random(202609070326)
    special_rows=[]
    block_rows=[]
    chart_rows=[]
    window_rows=[]
    decoupling_witness=None
    for r in range(1,9):
        m=1<<r
        q=m*m
        for _ in range(12):
            t=rng.randrange(m)
            beta=rng.randrange(m)|1
            c=rng.randrange(m)
            alpha=(1+m*t)%q
            got=special(r,t,beta,c)
            exact=brute(r,alpha,beta,m*c)
            assert got==exact
            negative=brute(r,(-alpha)%q,beta,m*c)
            epsilon=1 if c<m//2 else -1
            assert exact+negative==q//2+epsilon
            special_rows.append(dict(r=r,t=t,beta=beta,c=c,count=got,negative_count=negative))
    for r in range(2,7):
        m=1<<r
        q=m*m
        for _ in range(5):
            a=rng.randrange(m)|1
            beta=rng.randrange(m)|1
            D=rng.randrange(q)
            A=rng.randrange(q)
            B=rng.randrange(q)
            values=[brute(r,a+m*t,beta,D,A,B) for t in range(m)]
            for u in range(r+1):
                t0=rng.randrange(1<<u)
                expected=sum(values[t] for t in range(t0,m,1<<u))
                got=block(r,a,beta,D,u,t0,A,B)
                assert got==expected,(r,a,beta,D,u,t0,A,B,got,expected)
                block_rows.append(dict(r=r,a=a,beta=beta,D=D,u=u,t0=t0,
                    input_start=A,output_start=B,count=got,
                    residual_affine_terms=1<<max(0,2*u-r)))
            length=rng.randrange(q+1)
            values=[sum((( (a+m*t)*j+m*beta*j*j+D-B)%q)<q//2
                        for i in range(length) for j in ((A+i)%q,)) for t in range(m)]
            for u in range(r+1):
                t0=rng.randrange(1<<u)
                expected=sum(values[t] for t in range(t0,m,1<<u))
                got=block_window(r,a,beta,D,u,t0,A,B,length)
                assert got==expected
                window_rows.append(dict(r=r,a=a,beta=beta,D=D,u=u,t0=t0,
                    input_start=A,input_length=length,output_start=B,count=got))
    for N in (147053,8464705853):
        for r in range(2,6):
            m=1<<r
            q=m*m
            modulus=m*q
            for u0 in (1,(rng.randrange(m)|1)):
                v0=N*pow(u0,-1,modulus)%modulus
                alpha=-N*pow(u0,-1,q)**2%q
                beta=N*pow(u0,-1,m)**3%m
                D=v0//m
                for j in range(q):
                    actual=N*pow(u0+m*j,-1,modulus)%modulus
                    predicted=v0%m+m*((alpha*j+m*beta*j*j+D)%q)
                    assert actual==predicted
                count=brute(r,alpha,beta,D)
                j0=rng.randrange(q)
                u1=(u0+m*j0)%modulus
                alpha1=(alpha+2*m*beta*j0)%q
                D1=(D+alpha*j0+m*beta*j0*j0)%q
                assert alpha1==-N*pow(u1,-1,q)**2%q
                assert D1==(N*pow(u1,-1,modulus)%modulus)//m
                assert brute(r,alpha1,beta,D1,(-j0)%q,0)==count
                gamma=N*pow(u0,-1,q)%q
                normalized=sum((u0*z)%q<q//2 and
                    (D+gamma*(-z+m*z*z))%q<q//2 for z in range(q))
                assert normalized==count
                a=alpha%m
                t=(alpha-a)//m
                decoupled=block(r,a,beta,D,1,t%2)
                faithful=sum(brute(r,(alpha+2*m*beta*z)%q,beta,
                    (D+alpha*z+m*beta*z*z)%q,(-z)%q,0) for z in range(m//2))
                assert faithful==(m//2)*count
                row=dict(N=N,r=r,u0=u0,v0=v0,alpha=alpha,beta=beta,D=D,
                    j0=j0,shifted_alpha=alpha1,shifted_D=D1,
                    shifted_input_start=(-j0)%q,count=count,gamma=gamma,
                    faithful_origin_sum=faithful,decoupled_slope_sum=decoupled)
                chart_rows.append(row)
                if faithful!=decoupled and decoupling_witness is None:
                    decoupling_witness=row
    assert decoupling_witness is not None
    print(json.dumps(dict(seed=202609070326,elapsed_seconds=time.monotonic()-start,
        special_checks=special_rows,block_checks=block_rows,window_checks=window_rows,chart_checks=chart_rows,
        decoupling_witness=decoupling_witness),indent=2))
