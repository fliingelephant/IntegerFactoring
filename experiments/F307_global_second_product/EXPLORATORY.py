"""Retained initial small tables; no asymptotic inference."""
import json, signal
from pathlib import Path
signal.alarm(30)
rows=[]
for R in [8,16]:
    for A,B in [(1,1),(3,5),(5,3)]:
        h=[]
        for n in range(R):
            total=0
            for x in range(R):
                y=(n-A*x)*pow(B,-1,R)%R
                q=x*y+(A*x+B*y-n)//R
                total+=q*(q-1)//2
            h.append(total%(R*R))
        rows.append(dict(R=R,A=A,B=B,block_values=h))
diagonal=[]
for k in range(3,9):
    M=1<<k; values=[]
    for N in range(1,M,2):
        total=0
        for u in range(1,M,2):
            v=N*pow(u,-1,M)%M; q=(u*v-N)//M
            total+=q*(q-1)//2
        values.append(total%M)
    diagonal.append(dict(k=k,values=values))
out=dict(block_tables=rows,unshifted_tables=diagonal,scope='Exploratory tables only; no contraction claimed from these patterns.')
Path(__file__).with_name('EXPLORATORY_output.json').write_text(json.dumps(out,indent=2)+'\n')
print('Retained six block tables and six unshifted whole-graph tables.')
