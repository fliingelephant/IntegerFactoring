"""F296 / F31: exact cut/phase certificates and Mordell quadrature checks.

One 60-second pilot, estimated peak below512MiB. Numerical integral checks
are distinguished from exact cyclotomic and rational phase equalities.
"""
from sage.all import CyclotomicField, QQ, floor, ceil
import mpmath as mp
import json
import random
import resource
import signal
import time
from pathlib import Path

signal.alarm(60)
started=time.monotonic()
rng=random.Random(2962608)
inputs=[(8,1,45,13,1),(16,1,109,230,1)]
for m in (8,16,32,64):
    inputs.append((m,rng.randrange(1,m*m,2),rng.randrange(1,m*m,2),rng.randrange(m*m),rng.randrange(1,m,2)))
mp.mp.dps=45
rows=[]
phase_checks=0
for m,u,gamma,D,b0 in inputs:
    q=m*m
    d=gamma*pow(u,-1,q)%q
    beta=gamma*pow(u,-2,m)%m
    a=d%m
    b=m-1-D%m
    H=(a*(m-1)+b)//m
    A=b0*beta%m
    B=-b0*(d//m)%m
    normalized_A=A
    normalized_B=B
    conjugate=False
    if normalized_A>m//2:
        normalized_A-=m
    if normalized_A>m//4:
        normalized_A-=m//2
        normalized_B+=m//2
    if normalized_A< -m//4:
        normalized_A+=m//2
        normalized_B+=m//2
    if normalized_A<0:
        normalized_A=-normalized_A
        normalized_B=-normalized_B
        conjugate=True
    normalized_B%=m
    alpha=QQ(normalized_B)/m
    tau=QQ(normalized_A)/m
    p=2*normalized_A
    field=CyclotomicField(4*m)
    root=field.gen()
    omega=root**4
    original_Z=omega**(-b0)
    Z=omega**(b0 if conjugate else -b0)
    endpoints=[int(ceil(QQ(m*j-b)/a))-1 for j in range(1,H+1)]
    transformed=[(normalized_B+normalized_A+p*n)//m for n in endpoints]
    cut_c=-b-1
    cut_k=(p*cut_c+a*(normalized_B+normalized_A))//m
    cut_zeta=(p*cut_c+a*(normalized_B+normalized_A))%m
    linear_cut=[(p*j+cut_k)//a for j in range(1,H+1)]
    cut_delta=[int(m*((p*j+cut_k)%a)+cut_zeta<p*((m*j+cut_c)%a)) for j in range(1,H+1)]
    assert transformed==[R-delta for R,delta in zip(linear_cut,cut_delta)]
    original_prefix=[sum(omega**(A*k*k+B*k) for k in range(n+1)) for n in endpoints]
    normalized_prefix=[sum(omega**(normalized_A*k*k+normalized_B*k) for k in range(n+1)) for n in endpoints]
    assert original_prefix==[x.conjugate() if conjugate else x for x in normalized_prefix]
    cut=sum(omega**(A*i*i+B*i)*original_Z**((a*i+b)//m) for i in range(m))
    full=sum(omega**(A*i*i+B*i) for i in range(m))
    original_moment=sum(original_Z**j*v for j,v in enumerate(original_prefix))
    assert cut==original_Z**H*full-(original_Z-1)*original_moment
    groups={}
    for j,(n,r) in enumerate(zip(endpoints,transformed)):
        X=QQ(2*n+1)/2
        z=alpha+2*tau*X-r-QQ(1)/2
        # Check the root's Fresnel phase cancellation exactly modulo1.
        Ephase=QQ(r)/2+alpha*X+tau*X*X
        first=Ephase-(z+QQ(1)/2)**2/(4*tau)+(alpha-r)**2/(4*tau)
        second=Ephase-(QQ(1)/2-z)**2/(4*tau)+(alpha-r-1)**2/(4*tau)-QQ(1)/2
        assert first.denominator()==1 and second.denominator()==1
        phase_checks+=2
        coefficient=-QQ(1)/2*root**(m+2*m*r+(2*n+1)*(2*normalized_B+normalized_A*(2*n+1)))*Z**j
        key=int((normalized_B+normalized_A+p*n)%m)
        groups[key]=groups.get(key,field(0))+coefficient
    nonzero={r:c for r,c in groups.items() if c}
    alpha_mp=mp.mpf(int(alpha.numerator()))/int(alpha.denominator())
    tau_mp=mp.mpf(int(tau.numerator()))/int(tau.denominator())
    Z_mp=mp.exp(2j*mp.pi*(b0 if conjugate else -b0)/m)
    common_phase=mp.exp(-mp.pi*1j*(alpha_mp-tau_mp/2))
    cache={}
    for arg in [alpha-tau+QQ(1)/2]+[-QQ(1)/2+QQ(r)/m for r in nonzero]:
        arg_mp=mp.mpf(int(arg.numerator()))/int(arg.denominator())
        rotation=mp.exp(mp.pi*1j/4)
        integral=2*rotation*mp.quad(lambda y:mp.exp(-mp.pi*(2*tau_mp)*y*y)*mp.cosh(2*mp.pi*arg_mp*rotation*y)/mp.cosh(mp.pi*rotation*y),[0,1,2,4,8,16,mp.inf])
        cache[arg]=mp.conj(integral)
    common=-mp.j/2*common_phase*cache[alpha-tau+QQ(1)/2]*sum(Z_mp**j for j in range(H))
    boundary=mp.mpc(0)
    for arg_residue,coefficient in nonzero.items():
        coefficients=list(coefficient)
        value=sum(mp.mpf(str(v))*mp.exp(2j*mp.pi*k/(4*m)) for k,v in enumerate(coefficients))
        boundary+=value*cache[-QQ(1)/2+QQ(arg_residue)/m]
    dual_alpha=alpha_mp/(2*tau_mp)
    dual_tau=-1/(4*tau_mp)
    prefactor=mp.exp(mp.pi*1j/4-mp.pi*1j*alpha_mp**2/(2*tau_mp))/mp.sqrt(2*tau_mp)
    main=prefactor*sum(Z_mp**j*sum(mp.exp(2j*mp.pi*(dual_alpha*k+dual_tau*k*k)) for k in range(r+1)) for j,r in enumerate(transformed))
    bulk=mp.mpc(0)
    Rmax=max(linear_cut,default=-1)
    for h in range(Rmax+1):
        start=max(1,int(ceil(QQ(a*h-cut_k)/p)))
        geometric=mp.mpc(0) if start>H else (Z_mp**(start-1)-Z_mp**H)/(1-Z_mp)
        bulk+=mp.exp(2j*mp.pi*(dual_alpha*h+dual_tau*h*h))*geometric
    cut_correction=sum(Z_mp**j*mp.exp(2j*mp.pi*(dual_alpha*R+dual_tau*R*R)) for j,(R,delta) in enumerate(zip(linear_cut,cut_delta)) if delta)
    assert abs(main-prefactor*(bulk-cut_correction))<mp.mpf('1e-32')
    direct=sum(Z_mp**j*sum(mp.exp(2j*mp.pi*(alpha_mp*k+tau_mp*k*k)) for k in range(n+1)) for j,n in enumerate(endpoints))
    error=abs(direct-main-common-boundary)
    if error>=mp.mpf('1e-32'):
        print(json.dumps(dict(m=m,alpha=str(alpha),tau=str(tau),direct=str(direct),main=str(main),common=str(common),boundary=str(boundary),h_values={str(k):str(v) for k,v in cache.items()})),flush=True)
        for n,r in zip(endpoints,transformed):
            nn=mp.mpf(n)+mp.mpf('0.5')
            direct_n=sum(mp.exp(2j*mp.pi*(alpha_mp*k+tau_mp*k*k)) for k in range(n+1))
            main_n=prefactor*sum(mp.exp(2j*mp.pi*(dual_alpha*k+dual_tau*k*k)) for k in range(r+1))
            remainder_n=-mp.j/2*common_phase*cache[alpha-tau+QQ(1)/2]-mp.j/2*(-1)**r*mp.exp(2j*mp.pi*nn*(alpha_mp+tau_mp*nn))*cache[-QQ(1)/2+QQ((normalized_B+normalized_A+p*n)%m)/m]
            print(n,r,str(direct_n-main_n-remainder_n),flush=True)
    assert error<mp.mpf('1e-32'),str(error)
    rows.append(dict(m=m,q=q,u=u,gamma=gamma,D=D,b0=b0,d=d,a=a,b=b,H=H,A=A,B=B,
                     normalized_A=normalized_A,normalized_B=normalized_B,conjugate=conjugate,
                     p=p,endpoints=endpoints,transformed_endpoints=transformed,
                     cut_k=cut_k,cut_zeta=cut_zeta,linear_cut=linear_cut,
                     cut_delta_indices=[j+1 for j,diff in enumerate(cut_delta) if diff],
                     new_bulk_length=Rmax+1,
                     original_total_prefix_terms=sum(n+1 for n in endpoints),
                     transformed_total_prefix_terms=sum(r+1 for r in transformed),
                     distinct_mordell_arguments=len(groups),nonzero_grouped_arguments=len(nonzero),
                     common_argument=str(alpha-tau+QQ(1)/2),
                     argument_base='-1/2',argument_residues=sorted(nonzero),
                     grouped_coefficients={str(r):str(c) for r,c in nonzero.items()},
                     direct=str(direct),dual_main=str(main),common_boundary=str(common),
                     variable_boundary=str(boundary),numeric_error=str(error)))
output=dict(packet='F296',route='F31',seed=2962608,
            status='exact_cut_phase_certificates_and_nonrigorous_high_precision_integral_checks',
            runtime_seconds=time.monotonic()-started,
            max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            exact_fresnel_phase_checks=phase_checks,rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
