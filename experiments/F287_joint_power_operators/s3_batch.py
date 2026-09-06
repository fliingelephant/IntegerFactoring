"""Exact three-base h2 batching counts; offline prime labels.
<1 second and <32 MB expected; standard Python only.
"""
import json
from collections import Counter

rows=[]
for p,q in [(11,17),(43,47),(101,149),(383,643),(613,887),(1259,1783)]:
    local=[]
    for ell,r in [(p,q),(q,p)]:
        masks=Counter()
        for t in range(2,ell):
            bases=[t,(1-t)%ell,t*pow(t-1,-1,ell)%ell]
            powers=[pow(s,r,ell) for s in bases]
            if any(v in (1,s) for s,v in zip(bases,powers)): continue
            mask=sum((int((v*v+2*(s-1)*v-s)%ell==0)<<i) for i,(s,v) in enumerate(zip(bases,powers)))
            masks[mask]+=1
        local.append(dict(prime=ell,masks=dict(sorted(masks.items())),eligible=sum(masks.values())))
    a,b=local
    den=a['eligible']*b['eligible']
    same=sum(a['masks'].get(m,0)*b['masks'].get(m,0) for m in range(8))
    single=sum(x*y for ma,x in a['masks'].items() for mb,y in b['masks'].items() if (ma&1)!=(mb&1))
    rows.append(dict(p=p,q=q,local=local,three_base_split=[den-same,den],single_base_split=[single,den]))
print(json.dumps(dict(scope='Exact finite batch comparison conditioned on all three screens and all three Fermat gcds being 1',rows=rows),indent=2))
