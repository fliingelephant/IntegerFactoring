"""F299/F31 exact global odd-frequency and affine-class pilot.

60-second alarm; estimated peak below512MiB. No Barvinok implementation
is invoked: fixed-class polytope counts are verified by small enumeration.
"""
from sage.all import CyclotomicField, QQ
import json
import random
import resource
import signal
import time
from pathlib import Path

signal.alarm(60)
started=time.monotonic()
rng=random.Random(2992608)
inputs=[(8,1,45,13),(16,1,109,230),(16,1,109,0)]
for m in (8,16,32,64):
    for _ in range(2):
        inputs.append((m,rng.randrange(1,m*m,2),rng.randrange(1,m*m,2),rng.randrange(m*m)))
rows=[]
coset_checks=0
flatten_checks=0
linear_class_checks=0
for m,u,gamma,D in inputs:
    q=m*m
    d=gamma*pow(u,-1,q)%q
    beta=gamma*pow(u,-2,m)%m
    psi=[beta*i*i+(D-d*i)//m for i in range(m)]
    field=CyclotomicField(m)
    omega=field.gen()
    powers=[omega**j for j in range(m)]
    theta={b:sum(powers[b*v%m] for v in psi) for b in range(1,m,2)}
    frame={b:theta[b]/((1-powers[-d*b%m])*(1-powers[-b%m])) for b in theta}
    count=QQ(q)/4+QQ(4)/m*sum(frame.values())
    direct=sum(1 for i in range(m) for v in range(m//2) if (psi[i]-d*v)%m<m//2)
    assert count==direct
    normal_p={b:2*min((b*beta)%(m//2),m//2-(b*beta)%(m//2)) for b in theta}
    assert len(set(normal_p.values()))==m//8
    assert all(normal_p[b]==normal_p[(b+m//2)%m] for b in theta)
    descents=[]
    r=2
    while r<=m//2:
        L=m//r
        child=[0]*L
        for i in range(m):
            for j in range(r):
                value=(psi[i]-d*j)//r
                flattened=(m*beta*i*i+D-d*i-m*d*j)//(m*r)
                assert value==flattened
                flatten_checks+=1
                child[value%L]+=1
        eta=powers[r]
        rhs_frames=[]
        for b0 in range(1,L,2):
            lhs=sum(frame[b0+L*t] for t in range(r))
            rhs=r*sum(child[h]*eta**(b0*h) for h in range(L))/((1-eta**(-d*b0))*(1-eta**(-b0)))
            assert lhs==rhs
            coset_checks+=1
            rhs_frames.append(rhs)
        assert QQ(q)/4+QQ(4)/m*sum(rhs_frames)==direct
        child_count=sum(child[h]*sum(1 for y in range(L//2) if(h-d*y)%L<L//2) for h in range(L))
        assert child_count==direct
        descents.append(dict(r=r,L=L,carry_denominator=m*r,total_scale=L*m*r,
                             index_pairs=m*r,outer_frames=L//2,
                             child_histogram=child,count=int(child_count)))
        r*=2
    residue_bits=(m.bit_length()-1)//2
    r=1<<residue_bits
    L=m//r
    kappa=beta*r%L
    assert (2*kappa)%L==0
    classes=[]
    for i0 in range(r):
        E=(m*beta*i0*i0-d*i0+D)//r
        A=m*(2*beta*i0+kappa)-d
        class_count=0
        for x in range(L):
            for v in range(m//2):
                affine=A*x+E-L*d*v
                counted=affine%(m*L)<m*L//2
                original=(psi[i0+r*x]-d*v)%m<m//2
                assert counted==original
                linear_class_checks+=1
                class_count+=counted
        classes.append(dict(i0=i0,E=E,A=A,count=int(class_count)))
    assert sum(c['count'] for c in classes)==direct
    general_windows=[]
    for ilo,ihi,vlo,vhi,ylo,yhi in ((1,m-1,2,m//2+1,1,m-1),(m//4,3*m//4,0,m//3+1,m//4,m//2+1)):
        expected=sum(1 for i in range(ilo,ihi) for v in range(vlo,vhi) if ylo<=(psi[i]-d*v)%m<yhi)
        observed=0
        for c0 in classes:
            for x in range(L):
                if not ilo<=c0['i0']+r*x<ihi:
                    continue
                for v in range(vlo,vhi):
                    observed+=L*ylo<=(c0['A']*x+c0['E']-L*d*v)%(m*L)<L*yhi
        assert observed==expected
        general_windows.append(dict(I=[ilo,ihi],V=[vlo,vhi],Y=[ylo,yhi],count=int(expected)))
    root_r=omega**(m//r)
    nonzero_modes=[k for k in range(r) if sum(c['count']*root_r**(k*c['i0']) for c in classes)!=0]
    rows.append(dict(m=m,q=q,u=u,gamma=gamma,D=D,d=d,beta=beta,count=int(direct),
                     original_distinct_normal_p=len(set(normal_p.values())),
                     descents=descents,linearization_r=r,linearization_L=L,kappa=kappa,
                     general_window_checks=general_windows,
                     classes=classes,nonzero_class_fourier_modes=nonzero_modes))
out=dict(packet='F299',route='F31',seed=2992608,
         status='exact_finite_global_covariance_and_linear_polytope_certificates',
         runtime_seconds=time.monotonic()-started,
         max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         coset_checks=coset_checks,flatten_checks=flatten_checks,
         linear_class_checks=linear_class_checks,rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
